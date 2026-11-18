---
title: "PodGroup API"
weight: 90
no_list: true
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

هر PodGroup یک آبجکت زمان اجرا است که گروهی از Podها را نشان می‌دهد که به‌صورت یک واحد واحد با هم زمان‌بندی می‌شوند. در حالی که [Workload API](/docs/concepts/workloads/workload-api/) الگوهای سیاست زمان‌بندی را تعریف می‌کند، PodGroupها همتای زمان اجرای آن هستند و هم سیاست و هم وضعیت زمان‌بندی یک نمونهٔ مشخص از آن گروه را در خود نگه می‌دارند.

<!-- body -->

## PodGroup چیست؟

منبع PodGroup API بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}}
`scheduling.k8s.io/v1beta1` است. پیش از استفاده از این API، باید این گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) مربوط به `GenericWorkload`
در کلاستر شما فعال باشند.

هر PodGroup یک واحد زمان‌بندی مستقل است. این آبجکت گروهی از Podها را که باید با هم زمان‌بندی شوند تعریف می‌کند، سیاست زمان‌بندی حاکم بر جای‌گذاری آن‌ها را در خود دارد و وضعیت زمان اجرای آن تصمیم زمان‌بندی را ثبت می‌کند.

## ساختار API

هر PodGroup از یک `spec` تشکیل می‌شود که رفتار زمان‌بندی مطلوب را تعریف می‌کند و یک `status` که وضعیت فعلی زمان‌بندی را بازتاب می‌دهد.

### سیاست زمان‌بندی

هر PodGroup یک [سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/)
(`basic` یا `gang`) را در `spec.schedulingPolicy` در خود دارد. هنگامی که یک کنترل‌کنندهٔ بار کاری
PodGroup را ایجاد می‌کند، این سیاست در زمان ایجاد از PodGroupTemplate مربوط به Workload کپی می‌شود.
برای PodGroupهای مستقل، سیاست را خودتان مستقیماً تنظیم می‌کنید.

```yaml
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```

### ارجاع به الگو

فیلد اختیاری `spec.podGroupTemplateRef` هر PodGroup را به PodGroupTemplate موجود در Workloadی پیوند می‌دهد که از آن ایجاد شده است. این ارجاع برای مشاهده‌پذیری (observability) و ابزارها مفید است.

```yaml
spec:
  podGroupTemplateRef:
    workload:
      workloadName: training-policy
      podGroupTemplateName: worker
```

### اولویت و حالت اختلال

هر PodGroup همچنین می‌تواند `spec.priority`، `spec.preemptionPolicy` و
`spec.disruptionMode` مخصوص به خود را تعریف کند. اولویت و سیاست پیش‌دستی (preemption) با استفاده از فیلد
`spec.priorityClassName` تنظیم می‌شوند که به یک منبع `PriorityClass` اشاره می‌کند.
برای توضیح مفصل این فیلدها، به
[اختلال و اولویت Pod Group](/docs/concepts/workloads/workload-api/disruption-and-priority/)
مراجعه کنید.

هنگامی که یک کنترل‌کنندهٔ بار کاری PodGroup را ایجاد می‌کند، این فیلدها در زمان ایجاد از PodGroupTemplate مربوط به Workload کپی می‌شوند. برای PodGroupهای مستقل، این فیلدها را خودتان مستقیماً تنظیم می‌کنید.

```yaml
spec:
  disruptionMode:
    all: {}
  priorityClassName: high-priority
```

### درخواست دستگاه‌های DRA برای یک PodGroup

{{< feature-state feature_gate_name="DRAWorkloadResourceClaims" >}}

هر PodGroup می‌تواند
{{< glossary_tooltip text="دستگاه‌هایی" term_id="device" >}} را که از طریق
{{< glossary_tooltip text="تخصیص پویای منابع (DRA)" term_id="dra" >}}
در دسترس هستند، با فیلد `spec.resourceClaims` خود درخواست کند:

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

همهٔ Podهای متعلق به یک گروه می‌توانند
{{< glossary_tooltip text="ResourceClaimهای" term_id="resourceclaim" >}}
مرتبط با آن PodGroup را به اشتراک بگذارند. از آنجا که در `status.reservedFor` هر ResourceClaim
به‌جای تک‌تک Podها فقط به PodGroup ارجاع داده می‌شود، هر تعداد Pod در یک PodGroup می‌توانند
یک ResourceClaim را به اشتراک بگذارند. همچنین می‌توان برای هر PodGroup، ResourceClaimهایی را از
{{< glossary_tooltip text="ResourceClaimTemplateها" term_id="resourceclaimtemplate" >}}
تولید کرد تا Podهای هر PodGroup بتوانند دستگاه‌های تخصیص‌یافته به هر ResourceClaim تولیدشده را
به اشتراک بگذارند.

برای جزئیات بیشتر و یک مثال کامل‌تر، به
[مستندات DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#workload-resource-claims) مراجعه کنید.

### وضعیت

زمان‌بند فیلد `status.conditions` را به‌روزرسانی می‌کند تا گزارش دهد که آیا گروه با موفقیت زمان‌بندی شده است یا نه. شرط اصلی `PodGroupInitiallyScheduled` است که وقتی همهٔ Podهای لازم جای‌گذاری شده باشند مقدار `True` دارد و وقتی زمان‌بندی ناموفق باشد مقدار `False` دارد.

{{< note >}}
شرط `PodGroupInitiallyScheduled` فقط تصمیم اولیهٔ زمان‌بندی را بازتاب می‌دهد.
اگر Podها بعداً با شکست مواجه شوند یا بیرون رانده (evict) شوند، زمان‌بند این شرط را به‌روزرسانی نمی‌کند. برای جزئیات، به
[محدودیت‌ها](/docs/concepts/workloads/podgroup-api/lifecycle/#limitations)
مراجعه کنید.
{{< /note >}}

برای فهرست کامل شرط‌ها و دلایل، به صفحهٔ
[چرخهٔ حیات PodGroup](/docs/concepts/workloads/podgroup-api/lifecycle/#podgroup-status)
مراجعه کنید.

## ایجاد یک PodGroup

منبع PodGroup API بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}}
`scheduling.k8s.io/v1beta1` است.
(پیش از استفاده از این API، باید این گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) مربوط به `GenericWorkload`
در کلاستر شما فعال باشند.)

مانیفست زیر یک PodGroup با سیاست زمان‌بندی گروهی (gang) ایجاد می‌کند که لازم است دست‌کم ۴ Pod به‌طور همزمان قابل زمان‌بندی باشند:

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

## اجزا چگونه کنار هم قرار می‌گیرند

رابطهٔ میان کنترل‌کننده‌ها، Workloadها، PodGroupها و Podها از این الگو پیروی می‌کند:

1. کنترل‌کنندهٔ بار کاری یک Workload ایجاد می‌کند که PodGroupTemplateهایی همراه با سیاست‌های زمان‌بندی تعریف می‌کند.
2. کنترل‌کننده برای هر نمونهٔ زمان اجرا، یک PodGroup را از یکی از PodGroupTemplateهای Workload ایجاد می‌کند.
3. کنترل‌کننده Podهایی ایجاد می‌کند که از طریق فیلد `spec.schedulingGroup.podGroupName`
   به PodGroup ارجاع می‌دهند.

در حال حاضر، کنترل‌کنندهٔ [Job](/docs/concepts/workloads/controllers/job/) تنها کنترل‌کنندهٔ بار کاری داخلی است که از این الگو پیروی می‌کند.
کنترل‌کننده‌های سفارشی می‌توانند همین روند را برای انواع بار کاری خودشان پیاده‌سازی کنند.

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

آبجکت Workload نقش یک تعریف سیاست بلندمدت را دارد، در حالی که PodGroupها وضعیت زمان اجرای گذرا و مخصوص هر نمونه را مدیریت می‌کنند. در نتیجهٔ این جداسازی، به‌روزرسانی‌های وضعیت PodGroupهای مختلف بر سر آبجکت مشترک Workload با یکدیگر رقابت نمی‌کنند.

## گروه والد

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gate
[`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
فعال باشد، هر `PodGroup` می‌تواند نقش یک نود برگ را در یک سلسله‌مراتب چندسطحی از گروه‌ها ایفا کند
که از `PodGroups` و `CompositePodGroups` تشکیل شده است. هر `PodGroup` می‌تواند گروه والد خود را با فیلد
`spec.parentCompositePodGroupName` مشخص کند. با سازمان‌دهی یک بار کاری در قالب سلسله‌مراتبی از گروه‌ها،
می‌توان الزامات زمان‌بندی گروهی چندسطحی، محدودیت‌های توپولوژی چندسطحی و سرنوشت مشترک در برابر اختلال
میان بخش‌های مختلف بار کاری را بیان کرد.

برای جزئیات بیشتر دربارهٔ ساختارهای سلسله‌مراتبی گروه‌ها و زمان‌بندی گروهی چندسطحی، به نمای کلی
[CompositePodGroup API](/docs/concepts/workloads/compositepodgroup-api/) مراجعه کنید.

{{< note >}}
هر `PodGroup` که `spec.parentCompositePodGroupName` را مشخص می‌کند، باید `spec.workloadRef` را نیز مشخص کند
تا آن `PodGroup` را به الگوی خود در `Workload` پیوند دهد. آبجکت‌های `PodGroup` مستقل
(که بدون `spec.workloadRef` ایجاد شده‌اند) اجازه ندارند یک `CompositePodGroup` والد مشخص کنند.
{{< /note >}}

## {{% heading "whatsnext" %}}

* با [چرخهٔ حیات PodGroup](/docs/concepts/workloads/podgroup-api/lifecycle/) به‌طور مفصل آشنا شوید.
* دربارهٔ [Workload API](/docs/concepts/workloads/workload-api/) که PodGroupTemplateها را فراهم می‌کند، مطالعه کنید.
* ببینید Podها چگونه از طریق فیلد [گروه زمان‌بندی](/docs/concepts/workloads/pods/scheduling-group/) به PodGroup خود ارجاع می‌دهند.
* الگوریتم [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) را درک کنید.
