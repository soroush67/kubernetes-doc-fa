---
title: CompositePodGroup API
weight: 100
no_list: true
---

<!-- overview -->
{{< feature-state feature_gate_name="CompositePodGroup" >}}

هر `CompositePodGroup` یک آبجکت زمان اجرا است که یک گره غیربرگ را در یک سلسله‌مراتب چندسطحی از بار کاری نمایش می‌دهد. در حالی که [Workload API](/docs/concepts/workloads/workload-api/) الگوهای ایستای سیاست زمان‌بندی را تعریف می‌کند، آبجکت‌های `CompositePodGroup` و `PodGroup` همتایان زمان اجرای آن هستند و سیاست‌ها و ارجاع‌های سلسله‌مراتبی مربوط به یک نمونهٔ مشخص از بار کاری را در خود نگه می‌دارند.

<!-- body -->

## CompositePodGroup چیست؟

منبع API با نام `CompositePodGroup` بخشی از {{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1alpha3` است. پیش از استفاده از این API، باید این گروه API و همچنین [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `CompositePodGroup` در کلاستر شما فعال باشند.

هر `CompositePodGroup` مجموعه‌ای از گروه‌های فرزند را نمایش می‌دهد که می‌توانند آبجکت‌های `CompositePodGroup` یا `PodGroup` باشند. این آبجکت سیاست‌های زمان‌بندی، حالت‌های اختلال (disruption)، تنظیمات اولویت و محدودیت‌های اختیاری توپولوژی را در خود دارد که به‌صورت جمعی بر همهٔ گروه‌های فرزندش اعمال می‌شوند.

## ساختار API

هر `CompositePodGroup` از یک `spec` که رفتار زمان‌بندی مطلوب را برای گروه‌های فرزندش تعریف می‌کند، و یک زیرمنبع `status` تشکیل شده است.

### سیاست زمان‌بندی

هر `CompositePodGroup` یک [سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/) (`basic` یا `gang`) را در `spec.schedulingPolicy` در خود دارد. هنگامی که یک کنترل‌کنندهٔ بار کاری یک `CompositePodGroup` می‌سازد، این سیاست در زمان ایجاد از `CompositePodGroupTemplate` مربوط به `Workload` کپی می‌شود.

در سیاست `gang` برای یک `CompositePodGroup`، فیلد `minGroupCount` حداقل تعداد گروه‌های فرزندی را مشخص می‌کند که باید به‌طور هم‌زمان قابل زمان‌بندی باشند:

```yaml
spec:
  schedulingPolicy:
    gang:
      minGroupCount: 2
```

### ارجاع به گروه والد

منابع `CompositePodGroup` غیرریشه، گروه والد خود را با `spec.parentCompositePodGroupName` مشخص می‌کنند. در آبجکت‌های `CompositePodGroup` ریشه، این فیلد تنظیم نمی‌شود.

```yaml
spec:
  parentCompositePodGroupName: root-group-0
```

### ارجاع به بار کاری

فیلد `spec.workloadRef` آبجکت `CompositePodGroup` را به `CompositePodGroupTemplate` موجود در آبجکت `Workload` که از آن مشتق شده است، پیوند می‌دهد.

```yaml
spec:
  workloadRef:
    workloadName: hierarchical-workload
    templateName: replica-group
```

### وضعیت

طرح‌وارهٔ API مربوط به `CompositePodGroup` یک زیرمنبع `status` دارد. در نسخهٔ آلفا، فیلد `status` در نوع API وجود دارد، اما `kube-scheduler` شرایط وضعیت (status conditions) را برای آبجکت‌های `CompositePodGroup` به‌روزرسانی یا مقداردهی نمی‌کند. پیگیری وضعیت برای گروه‌های ترکیبی در نسخه‌های آینده پیاده‌سازی خواهد شد.

## ایجاد یک CompositePodGroup

کنترل‌کننده‌های بار کاری آبجکت‌های `CompositePodGroup` را در زمان اجرا و به‌طور خودکار از روی الگوهای `Workload` می‌سازند.

مانیفست زیر یک `CompositePodGroup` ریشه با سیاست زمان‌بندی gang ایجاد می‌کند که نیاز دارد دست‌کم ۲ گروه فرزند به‌طور هم‌زمان قابل زمان‌بندی باشند:

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

برای مشاهدهٔ جزئیات یک گروه ترکیبی مشخص:

```shell
kubectl describe compositepodgroup root-group-0
```

## اجزا چگونه در کنار هم قرار می‌گیرند

رابطهٔ میان کنترل‌کننده‌ها، Workloadها، CompositePodGroupها، PodGroupها و Podها از الگوی زیر پیروی می‌کند:

1. کنترل‌کنندهٔ بار کاری یک `Workload` می‌سازد که درختی از `CompositePodGroupTemplates` و `PodGroupTemplates` برگ را تعریف می‌کند.
2. کنترل‌کننده برای هر نمونهٔ زمان اجرا، یک `CompositePodGroup` ریشه، آبجکت‌های `CompositePodGroup` فرزند و آبجکت‌های `PodGroup` برگ را به‌ترتیب از بالا به پایین ایجاد می‌کند.
3. کنترل‌کننده `Pods` را ایجاد می‌کند که از طریق `spec.schedulingGroup.podGroupName` به `PodGroup` برگ خود ارجاع می‌دهند.

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

آبجکت `Workload` نقش یک الگوی سیاست بلندمدت را دارد، در حالی که منابع `CompositePodGroup` و `PodGroup` وضعیت زمان‌بندی زمان اجرا را برای هر نمونه مدیریت می‌کنند.

## {{% heading "whatsnext" %}}

* دربارهٔ [چرخهٔ عمر CompositePodGroup](/docs/concepts/workloads/compositepodgroup-api/lifecycle/) بخوانید.
* با [Workload API](/docs/concepts/workloads/workload-api/) و تعریف الگوها آشنا شوید.
* ببینید گروه‌های برگ در [PodGroup API](/docs/concepts/workloads/podgroup-api/) چگونه ساختاربندی می‌شوند.
* دربارهٔ [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) بخوانید.
* با [پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) آشنا شوید.
