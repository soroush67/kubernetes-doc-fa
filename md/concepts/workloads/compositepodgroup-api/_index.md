---
title: API مربوط به CompositePodGroup
weight: 25
no_list: true
---

<!-- overview -->
{{< feature-state feature_gate_name="CompositePodGroup" >}}

یک `CompositePodGroup` یک آبجکت زمان اجراست که یک گره غیربرگ را در سلسله‌مراتب چندسطحی یک بار کاری
نمایش می‌دهد. در حالی که [Workload API](/docs/concepts/workloads/workload-api/) قالب‌های ایستای سیاست زمان‌بندی
را تعریف می‌کند، آبجکت‌های `CompositePodGroup` و `PodGroup` همتایان زمان اجرای آن هستند که
سیاست‌ها و ارجاع‌های سلسله‌مراتبی را برای یک نمونه‌ی مشخص از بار کاری حمل می‌کنند.

<!-- body -->

## CompositePodGroup چیست؟

منبع API `CompositePodGroup` بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1alpha3` است. پیش از آنکه بتوانید از این API استفاده کنید،
آن گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `CompositePodGroup`
باید در کلاستر شما فعال باشند.

یک `CompositePodGroup` گروه‌بندی‌ای از گروه‌های فرزند (که می‌توانند آبجکت‌های `CompositePodGroup` یا
`PodGroup` باشند) را نمایش می‌دهد. این آبجکت سیاست‌های زمان‌بندی، حالت‌های اختلال، تنظیمات
اولویت، و قیدهای توپولوژی اختیاری را حمل می‌کند که به‌طور جمعی بر همه‌ی گروه‌های فرزند آن اعمال می‌شوند.

## ساختار API

یک `CompositePodGroup` از یک `spec` که رفتار زمان‌بندی مطلوب
گروه‌های فرزندش را تعریف می‌کند و یک زیرمنبع `status` تشکیل شده است.

### سیاست زمان‌بندی

هر `CompositePodGroup` یک [سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/)
(`basic` یا `gang`) را در `spec.schedulingPolicy` حمل می‌کند. هنگامی که یک کنترل‌کننده‌ی بار کاری یک
`CompositePodGroup` ایجاد می‌کند، این سیاست در زمان ایجاد از `CompositePodGroupTemplate` مربوط به `Workload`
کپی می‌شود.

برای سیاست `gang` روی یک `CompositePodGroup`، فیلد `minGroupCount`
حداقل تعداد گروه‌های فرزندی را مشخص می‌کند که باید به‌طور هم‌زمان قابل زمان‌بندی باشند:

```yaml
spec:
  schedulingPolicy:
    gang:
      minGroupCount: 2
```

### ارجاع به گروه والد

منابع `CompositePodGroup` غیرریشه، گروه والد خود را با استفاده از
`spec.parentCompositePodGroupName` مشخص می‌کنند. آبجکت‌های `CompositePodGroup` ریشه این فیلد را تنظیم‌نشده باقی می‌گذارند.

```yaml
spec:
  parentCompositePodGroupName: root-group-0
```

### ارجاع به Workload

فیلد `spec.workloadRef`، `CompositePodGroup` را به
`CompositePodGroupTemplate` موجود در آبجکت `Workload`ای که از آن مشتق شده است پیوند می‌دهد.

```yaml
spec:
  workloadRef:
    workloadName: hierarchical-workload
    templateName: replica-group
```

### وضعیت

شِمای API مربوط به `CompositePodGroup` شامل یک زیرمنبع `status` است. در نسخه‌ی آلفا،
فیلد `status` در نوع API وجود دارد، اما `kube-scheduler` شرایط وضعیت (status conditions) را برای آبجکت‌های `CompositePodGroup`
به‌روزرسانی یا مقداردهی نمی‌کند. ردیابی وضعیت برای گروه‌های
ترکیبی در نسخه‌های آینده پیاده‌سازی خواهد شد.

## ایجاد یک CompositePodGroup

کنترل‌کننده‌های بار کاری آبجکت‌های `CompositePodGroup` را در زمان اجرا به‌طور خودکار از قالب‌های `Workload`
ایجاد می‌کنند.

مانیفست زیر یک `CompositePodGroup` ریشه با سیاست زمان‌بندی gang ایجاد می‌کند
که مستلزم آن است که دست‌کم ۲ گروه فرزند به‌طور هم‌زمان قابل زمان‌بندی باشند:

```yaml
apiVersion: scheduling.k8s.io/v1alpha3
kind: CompositePodGroup
metadata:
  name: root-group-0
  namespace: default
spec:
  workloadRef:
    workloadName: hierarchical-workload
    templateName: root
  schedulingPolicy:
    gang:
      minGroupCount: 2
```

می‌توانید منابع `CompositePodGroup` موجود در کلاستر خود را بررسی کنید:

```shell
kubectl get compositepodgroups
```

برای مشاهده‌ی جزئیات یک گروه ترکیبی مشخص:

```shell
kubectl describe compositepodgroup root-group-0
```

## اجزا چگونه در کنار هم قرار می‌گیرند

رابطه‌ی میان کنترل‌کننده‌ها، Workloadها، CompositePodGroupها، PodGroupها و
Podها از این الگو پیروی می‌کند:

1. کنترل‌کننده‌ی بار کاری یک `Workload` ایجاد می‌کند که درختی از
   `CompositePodGroupTemplates` و `PodGroupTemplates` برگ را تعریف می‌کند.
2. برای هر نمونه‌ی زمان اجرا، کنترل‌کننده یک `CompositePodGroup` ریشه،
   آبجکت‌های `CompositePodGroup` نوادگان، و آبجکت‌های `PodGroup` برگ را به‌صورت بالا به پایین ایجاد می‌کند.
3. کنترل‌کننده `Pods`ی ایجاد می‌کند که از طریق
   `spec.schedulingGroup.podGroupName` به `PodGroup` برگ خود ارجاع می‌دهند.

مثال زیر یک سلسله‌مراتب کامل از مانیفست‌ها را برای یک بار کاری دوسطحی نشان می‌دهد:

```yaml
apiVersion: scheduling.k8s.io/v1alpha3
kind: Workload
metadata:
  name: hierarchical-workload
  namespace: default
spec:
  compositePodGroupTemplates:
  - name: root
    schedulingPolicy:
      gang:
        minGroupCount: 2
    podGroupTemplates:
    - name: workers-a
      schedulingPolicy:
        gang:
          minCount: 4
    - name: workers-b
      schedulingPolicy:
        gang:
          minCount: 4
---
apiVersion: scheduling.k8s.io/v1alpha3
kind: CompositePodGroup
metadata:
  name: root-group-0
  namespace: default
spec:
  workloadRef:
    workloadName: hierarchical-workload
    templateName: root
  schedulingPolicy:
    gang:
      minGroupCount: 2
---
apiVersion: scheduling.k8s.io/v1alpha3
kind: PodGroup
metadata:
  name: workers-a-0
  namespace: default
spec:
  parentCompositePodGroupName: root-group-0
  workloadRef:
    workloadName: hierarchical-workload
    templateName: workers-a
  schedulingPolicy:
    gang:
      minCount: 4
---
apiVersion: scheduling.k8s.io/v1alpha3
kind: PodGroup
metadata:
  name: workers-b-0
  namespace: default
spec:
  parentCompositePodGroupName: root-group-0
  workloadRef:
    workloadName: hierarchical-workload
    templateName: workers-b
  schedulingPolicy:
    gang:
      minCount: 4
---
apiVersion: v1
kind: Pod
metadata:
  name: worker-a-0
  namespace: default
spec:
  schedulingGroup:
    podGroupName: workers-a-0
  containers:
  - name: worker
    image: registry.k8s.io/pause:3.9
```

`Workload` به‌عنوان یک قالب سیاست بلندمدت عمل می‌کند، در حالی که منابع `CompositePodGroup` و
`PodGroup` وضعیت زمان‌بندی زمان اجرا را به‌ازای هر نمونه مدیریت می‌کنند.

## {{% heading "whatsnext" %}}

* درباره‌ی [چرخه‌ی حیات CompositePodGroup](/docs/concepts/workloads/compositepodgroup-api/lifecycle/) بخوانید.
* با [Workload API](/docs/concepts/workloads/workload-api/) و تعریف‌های قالب آشنا شوید.
* ببینید گروه‌های برگ در [API مربوط به PodGroup](/docs/concepts/workloads/podgroup-api/) چگونه ساختاربندی می‌شوند.
* درباره‌ی [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) بخوانید.
* با [پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) آشنا شوید.
