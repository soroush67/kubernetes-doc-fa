---
title: "PodGroup API"
weight: 25
no_list: true
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

PodGroup یک آبجکت زمان اجرا است که گروهی از Podها را نشان می‌دهد که با هم و به‌عنوان یک واحد زمان‌بندی می‌شوند.
در حالی که [Workload API](/docs/concepts/workloads/workload-api/) قالب‌های سیاست زمان‌بندی را
تعریف می‌کند، PodGroupها همتایان زمان اجرای آن هستند که هم سیاست و هم وضعیت زمان‌بندی
یک نمونه مشخص از آن گروه را در خود دارند.

<!-- body -->

## PodGroup چیست؟

منبع API مربوط به PodGroup بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1beta1`
است و پیش از آنکه بتوانید از این API استفاده کنید، کلاستر شما باید آن گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `GenericWorkload`
را فعال کرده باشد.

PodGroup یک واحد زمان‌بندی خودبسنده است. این آبجکت گروه Podهایی را که باید با هم زمان‌بندی شوند تعریف می‌کند،
سیاست زمان‌بندی حاکم بر جای‌گذاری را در خود دارد و وضعیت زمان اجرای آن
تصمیم زمان‌بندی را ثبت می‌کند.

## ساختار API

یک PodGroup از یک `spec` که رفتار زمان‌بندی مطلوب را تعریف می‌کند و
یک `status` که وضعیت فعلی زمان‌بندی را منعکس می‌کند تشکیل شده است.

### سیاست زمان‌بندی

هر PodGroup یک [سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/)
(`basic` یا `gang`) را در `spec.schedulingPolicy` در خود دارد. هنگامی که یک کنترل‌کننده بار کاری
PodGroup را ایجاد می‌کند، این سیاست در زمان ایجاد از PodGroupTemplate مربوط به Workload کپی می‌شود.
برای PodGroupهای مستقل، سیاست را مستقیماً خودتان تنظیم می‌کنید.

```yaml
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```

### ارجاع به قالب

فیلد اختیاری `spec.podGroupTemplateRef`، PodGroup را به PodGroupTemplate موجود
در Workloadای که از آن ایجاد شده است پیوند می‌دهد. این ویژگی برای مشاهده‌پذیری و ابزارها سودمند است.

```yaml
spec:
  podGroupTemplateRef:
    workload:
      workloadName: training-policy
      podGroupTemplateName: worker
```

### اولویت و حالت اختلال (Disruption mode)

هر PodGroup همچنین می‌تواند `spec.priority`، `spec.preemptionPolicy` و
`spec.disruptionMode` مخصوص به خود را تعریف کند. اولویت و سیاست پیش‌دستی (preemption) با استفاده از
فیلد `spec.priorityClassName` تنظیم می‌شوند که به یک منبع `PriorityClass` اشاره می‌کند.
برای توضیح مفصل این فیلدها، به
[اختلال و اولویت Pod Group](/docs/concepts/workloads/workload-api/disruption-and-priority/)
مراجعه کنید.

هنگامی که یک کنترل‌کننده بار کاری PodGroup را ایجاد می‌کند، این فیلدها در زمان ایجاد از
PodGroupTemplate مربوط به Workload کپی می‌شوند. برای PodGroupهای مستقل،
فیلدها را مستقیماً خودتان تنظیم می‌کنید.

```yaml
spec:
  disruptionMode:
    all: {}
  priorityClassName: high-priority
```

### درخواست دستگاه‌های DRA برای یک PodGroup

{{< feature-state feature_gate_name="DRAWorkloadResourceClaims" >}}

{{< glossary_tooltip text="دستگاه‌هایی" term_id="device" >}} که از طریق
{{< glossary_tooltip text="تخصیص پویای منابع (DRA)" term_id="dra" >}}
در دسترس هستند، می‌توانند توسط یک PodGroup از طریق فیلد `spec.resourceClaims` آن درخواست شوند:

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: training-group
  namespace: some-ns
spec:
  ...
  resourceClaims:
  - name: pg-claim
    resourceClaimName: my-pg-claim
  - name: pg-claim-template
    resourceClaimTemplateName: my-pg-template
```

{{< glossary_tooltip text="ResourceClaimهای" term_id="resourceclaim" >}}
مرتبط با PodGroupها می‌توانند میان همه Podهای متعلق به گروه به اشتراک گذاشته شوند. با
وجود تنها یک ارجاع به PodGroup در `status.reservedFor` مربوط به ResourceClaim،
به‌جای ارجاع به تک‌تک Podها، هر تعداد Pod در یک PodGroup می‌توانند
یک ResourceClaim را به اشتراک بگذارند. همچنین ResourceClaimها را می‌توان از
{{< glossary_tooltip text="ResourceClaimTemplateها" term_id="resourceclaimtemplate" >}}
برای هر PodGroup تولید کرد تا دستگاه‌های تخصیص‌یافته به هر
ResourceClaim تولیدشده، میان Podهای هر PodGroup به اشتراک گذاشته شوند.

برای جزئیات بیشتر و یک مثال کامل‌تر، به
[مستندات DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#workload-resource-claims) مراجعه کنید.

### وضعیت (Status)

زمان‌بند `status.conditions` را به‌روزرسانی می‌کند تا گزارش دهد آیا گروه
با موفقیت زمان‌بندی شده است یا نه. شرط اصلی `PodGroupInitiallyScheduled` است که زمانی `True` است
که همه Podهای لازم جای‌گذاری شده باشند و زمانی `False` است که زمان‌بندی شکست بخورد.

{{< note >}}
شرط `PodGroupInitiallyScheduled` تنها تصمیم زمان‌بندی اولیه را منعکس می‌کند.
اگر Podها بعداً از کار بیفتند یا بیرون رانده (evict) شوند، زمان‌بند آن را به‌روزرسانی نمی‌کند. برای جزئیات به
[محدودیت‌ها](/docs/concepts/workloads/podgroup-api/lifecycle/#limitations)
مراجعه کنید.
{{< /note >}}

برای فهرست کامل شرط‌ها و دلایل، به صفحه [چرخه عمر PodGroup](/docs/concepts/workloads/podgroup-api/lifecycle/#podgroup-status)
مراجعه کنید.

## ایجاد یک PodGroup

منبع API مربوط به PodGroup بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1beta1` است.
(و پیش از آنکه بتوانید از این API استفاده کنید، کلاستر شما باید آن گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `GenericWorkload`
را فعال کرده باشد).

مانیفست زیر یک PodGroup با سیاست زمان‌بندی gang ایجاد می‌کند که لازم است
دست‌کم 4 Pod به‌طور هم‌زمان قابل زمان‌بندی باشند:

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: training-worker-0
  namespace: default
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```

می‌توانید PodGroupهای کلاستر خود را بررسی کنید:

```shell
kubectl get podgroups
```

برای دیدن وضعیت کامل، از جمله شرط‌های زمان‌بندی:

```shell
kubectl describe podgroup training-worker-0
```

## اجزا چگونه در کنار هم قرار می‌گیرند

رابطه میان کنترل‌کننده‌ها، Workloadها، PodGroupها و Podها از این الگو پیروی می‌کند:

1. کنترل‌کننده بار کاری یک Workload ایجاد می‌کند که PodGroupTemplateهایی با سیاست‌های زمان‌بندی تعریف می‌کند.
2. برای هر نمونه زمان اجرا، کنترل‌کننده یک PodGroup از یکی از PodGroupTemplateهای Workload ایجاد می‌کند.
3. کنترل‌کننده Podهایی ایجاد می‌کند که از طریق فیلد `spec.schedulingGroup.podGroupName`
   به PodGroup ارجاع می‌دهند.

کنترل‌کننده [Job](/docs/concepts/workloads/controllers/job/) در حال حاضر تنها کنترل‌کننده
بار کاری داخلی است که از این الگو پیروی می‌کند.
کنترل‌کننده‌های سفارشی می‌توانند همین روند را برای انواع بار کاری خود پیاده‌سازی کنند.

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: Workload
metadata:
  name: training-policy
spec:
  podGroupTemplates:
  - name: worker
    schedulingPolicy:
      gang:
        minCount: 4
---
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: training-worker-0
spec:
  podGroupTemplateRef:
    workload:
      workloadName: training-policy
      podGroupTemplateName: worker
  schedulingPolicy:
    gang:
      minCount: 4
---
apiVersion: v1
kind: Pod
metadata:
  name: worker-0
spec:
  schedulingGroup:
    podGroupName: training-worker-0
  containers:
  - name: ml-worker
    image: training:v1
```

Workload نقش یک تعریف سیاست بلندمدت را ایفا می‌کند، در حالی که PodGroupها وضعیت
زمان اجرای گذرا و مختص هر نمونه را مدیریت می‌کنند. این جداسازی به این معناست که به‌روزرسانی‌های وضعیت
PodGroupهای منفرد بر سر آبجکت Workload مشترک با یکدیگر رقابت نمی‌کنند.

## گروه والد

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gate [`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
فعال باشد، یک `PodGroup` می‌تواند به‌عنوان یک نود برگ در یک سلسله‌مراتب چندسطحی از گروه‌ها عمل کند که
از `PodGroups` و `CompositePodGroups` تشکیل شده است. یک `PodGroup` می‌تواند گروه والد خود را با استفاده از
فیلد `spec.parentCompositePodGroupName` مشخص کند. سازمان‌دهی یک بار کاری در قالب سلسله‌مراتبی از گروه‌ها را می‌توان
برای بیان الزامات زمان‌بندی gang چندسطحی، محدودیت‌های توپولوژی چندسطحی و
سرنوشت مشترک در برابر اختلال میان بخش‌های مختلف بار کاری به کار برد.

برای جزئیات بیشتر درباره ساختارهای گروهی سلسله‌مراتبی و زمان‌بندی gang چندسطحی، به
نمای کلی [CompositePodGroup API](/docs/concepts/workloads/compositepodgroup-api/) مراجعه کنید.

{{< note >}}
یک `PodGroup` که `spec.parentCompositePodGroupName` را مشخص می‌کند باید `spec.workloadRef` را نیز مشخص کند
تا `PodGroup` را به قالب خود در `Workload` پیوند دهد. آبجکت‌های `PodGroup` مستقل
(که بدون `spec.workloadRef` ایجاد شده‌اند) مجاز به مشخص کردن یک `CompositePodGroup` والد نیستند.
{{< /note >}}

## {{% heading "whatsnext" %}}

* با [چرخه عمر PodGroup](/docs/concepts/workloads/podgroup-api/lifecycle/) به‌طور مفصل آشنا شوید.
* درباره [Workload API](/docs/concepts/workloads/workload-api/) که PodGroupTemplateها را فراهم می‌کند مطالعه کنید.
* ببینید Podها چگونه از طریق فیلد [گروه زمان‌بندی (scheduling group)](/docs/concepts/workloads/pods/scheduling-group/) به PodGroup خود ارجاع می‌دهند.
* الگوریتم [زمان‌بندی گروهی (gang scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/) را درک کنید.
