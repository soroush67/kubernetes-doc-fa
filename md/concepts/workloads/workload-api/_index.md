---
title: "Workload API"
weight: 80
simple_list: true
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

منبع API با نوع `Workload` الزامات زمان‌بندی و ساختار یک برنامهٔ چند-Pod را تعریف می‌کند. کنترل‌کننده‌های بار کاری مانند [Job](/docs/concepts/workloads/controllers/job/) وضعیت زمان اجرای برنامه را مدیریت می‌کنند، اما `Workload` مشخص می‌کند که گروه‌های `Pods` چگونه باید زمان‌بندی شوند. کنترل‌کنندهٔ Job تنها کنترل‌کنندهٔ داخلی است که در زمان اجرا، آبجکت‌های [PodGroup](/docs/concepts/workloads/podgroup-api/) را از `PodGroupTemplates` موجود در `Workload` ایجاد می‌کند.

<!-- body -->

## Workload چیست؟

منبع Workload API بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}}
`scheduling.k8s.io/v1beta1` است. پیش از استفاده از این API، باید این گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/)ِ `GenericWorkload` در کلاستر شما فعال باشند.

هر `Workload` یک قالب سیاست ایستا و بلندمدت است. این قالب تعیین می‌کند که چه سیاست‌های زمان‌بندی‌ای باید بر گروه‌های Pod اعمال شوند، اما خودش وضعیت زمان اجرا را دنبال نمی‌کند. وضعیت زمان‌بندی در زمان اجرا را آبجکت‌های [PodGroup](/docs/concepts/workloads/podgroup-api/) نگه می‌دارند؛ کنترل‌کننده‌ها این آبجکت‌ها را از `PodGroupTemplates` موجود در `Workload` ایجاد می‌کنند.

## ساختار API

هر `Workload` از دو فیلد تشکیل می‌شود: فهرستی از `PodGroupTemplates` و یک ارجاع اختیاری به کنترل‌کننده. کل spec یک `Workload` پس از ایجاد تغییرناپذیر است؛ یعنی نمی‌توانید قالب‌های موجود را تغییر دهید، قالب جدیدی اضافه کنید یا قالبی را از `podGroupTemplates` حذف کنید.

### PodGroupTemplates

فهرست `spec.podGroupTemplates` اجزای متمایز بار کاری شما را تعریف می‌کند. برای مثال، یک Job یادگیری ماشین ممکن است یک قالب `driver` و یک قالب `worker` داشته باشد.

هر ورودی در `podGroupTemplates` باید موارد زیر را داشته باشد:
1. یک `name` یکتا که برای ارجاع به قالب در فیلد `spec.podGroupTemplateRef` از `PodGroup` استفاده می‌شود.
2. یک [سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/) (`basic` یا `gang`).

هر ورودی همچنین می‌تواند فیلدهای
[اولویت و حالت اختلال](/docs/concepts/workloads/workload-api/disruption-and-priority/)
را داشته باشد.

{{< note >}}
در نسخهٔ v1.36، فیلدهای [اولویت و حالت اختلال](/docs/concepts/workloads/workload-api/disruption-and-priority/)
با feature gateِ
[`WorkloadAwarePreemption`](/docs/reference/command-line-tools-reference/feature-gates/#WorkloadAwarePreemption)
فعال می‌شدند. این gate در نسخهٔ v1.37 در
[`GenericWorkload`](/docs/reference/command-line-tools-reference/feature-gates/#GenericWorkload) ادغام شد.
{{< /note >}}

حداکثر تعداد PodGroupTemplates در یک Workload برابر با ۸ است.

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: Workload
metadata:
  name: training-job-workload
  namespace: some-ns
spec:
  controllerRef:
    apiGroup: batch
    kind: Job
    name: training-job
  podGroupTemplates:
  - name: workers
    schedulingPolicy:
      gang:
        # The gang is schedulable only if 4 pods can run at once
        minCount: 4
    priorityClassName: high-priority
    disruptionMode:
      all: {}
```

وقتی یک کنترل‌کنندهٔ بار کاری از یکی از این قالب‌ها یک `PodGroup` ایجاد می‌کند، مقدار `schedulingPolicy` را در spec خودِ آن `PodGroup` کپی می‌کند. تغییرات `Workload` فقط بر `PodGroups` تازه‌ایجادشده اثر می‌گذارند، نه بر نمونه‌های موجود.

### ارجاع به آبجکت کنترل‌کنندهٔ بار کاری

فیلد `controllerRef`، Workload را به آبجکت سطح بالای مشخصی که برنامه را تعریف می‌کند، مانند یک [Job](/docs/concepts/workloads/controllers/job/) یا یک CRD سفارشی، پیوند می‌دهد. این فیلد برای مشاهده‌پذیری و ابزارها مفید است. از این داده برای زمان‌بندی یا مدیریت Workload استفاده نمی‌شود.

### CompositePodGroupTemplates

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gateِ [`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
و {{< glossary_tooltip text="گروه API" term_id="api-group" >}}ِ `scheduling.k8s.io/v1alpha3`
فعال باشند، می‌توانید با `CompositePodGroupTemplates` الزامات زمان‌بندی چندسطحی و سلسله‌مراتبی را در یک `Workload` تعریف کنید. این الزامات می‌توانند شامل اعمال قیدهای توپولوژی تودرتو در لایه‌های مختلف زیرساخت کلاستر (زمان‌بندی چندسطحی آگاه از توپولوژی)، زمان‌بندی همه-یا-هیچ در میان گروه‌های فرزند (زمان‌بندی گروهی چندسطحی) یا سیاست‌های اختلال در سطح گروه باشند.

می‌توان `CompositePodGroupTemplates` را با فیلد `spec.compositePodGroupTemplates` در API مربوط به `Workload` تعریف کرد. کنترل‌کننده‌های بار کاری در زمان اجرا، آبجکت‌های [CompositePodGroup](/docs/concepts/workloads/compositepodgroup-api/)
و [PodGroup](/docs/concepts/workloads/podgroup-api/) را از این قالب‌ها ایجاد می‌کنند تا وضعیت زمان‌بندی سلسله‌مراتب را در زمان اجرا نگه دارند. آبجکت‌های `PodGroup` گروه‌های Pod را در برگ‌ها مدیریت می‌کنند، در حالی که آبجکت‌های `CompositePodGroup` نمایانگر گروه‌های غیربرگ هستند و سیاست‌های زمان‌بندی را در میان گروه‌های فرزند اعمال می‌کنند.

{{< note >}}
در مشخصات یک `Workload`، فیلدهای `spec.compositePodGroupTemplates` و `spec.podGroupTemplates`
یک اجتماع انحصاری (union) تشکیل می‌دهند: هر `Workload` باید یا `spec.podGroupTemplates` (برای بارهای کاری تخت) یا `spec.compositePodGroupTemplates` (برای بارهای کاری سلسله‌مراتبی) را تعریف کند و نمی‌تواند هر دو را مشخص کند.
{{< /note >}}

#### ساختار و محدودیت‌ها

فیلد `spec.compositePodGroupTemplates` قالب‌های غیربرگ را در درخت سلسله‌مراتب قالب‌های گروه تعریف می‌کند. هر ورودی قالبی برای یک `CompositePodGroup` است و می‌تواند شامل موارد زیر باشد:

- **قالب‌های فرزند**: `CompositePodGroupTemplates` تودرتو (برای گروه‌های غیربرگ میانی) یا `PodGroupTemplates` (برای گروه‌های برگ که Podها را در بر دارند).
- **سیاست زمان‌بندی**: مشخص می‌کند که گروه‌های فرزندِ این گروه مرکب چگونه زمان‌بندی شوند:
  - `basic`: گروه‌های فرزند به‌طور مستقل پذیرش و زمان‌بندی می‌شوند.
  - `gang`: زمان‌بندی همه-یا-هیچ چندسطحی را در میان گروه‌های فرزند اعمال می‌کند.
    این سیاست به `minGroupCount` نیاز دارد که حداقل تعداد گروه‌های فرزندی را مشخص می‌کند که باید به‌طور همزمان قابل زمان‌بندی باشند تا گروه مرکب امکان‌پذیر باشد.
- **قیدهای زمان‌بندی**: [قیدهای توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
  اختیاری برای زمان‌بندی چندسطحی آگاه از توپولوژی.
- **اولویت، سیاست پیش‌دستی و حالت اختلال**: فیلدهای اختیاری `priorityClassName`،
  `disruptionMode` (`Single` یا `All`) و `preemptionPolicy` برای
  [پیش‌دستی آگاه از بار کاری](/docs/concepts/workloads/workload-api/disruption-and-priority/).

برای حفظ پایداری کلاستر و کارایی control plane، سلسله‌مراتب قالب‌های گروه محدودیت‌های زیر را اعمال می‌کند:

- **حداکثر عمق تودرتویی**: سلسله‌مراتب قالب‌های گروه حداکثر از عمق ۴ سطح پشتیبانی می‌کند.
- **محدودیت فهرست**: هر فهرست `compositePodGroupTemplates` و `podGroupTemplates` به‌طور قطعی حداکثر ۸ مورد می‌تواند داشته باشد.

{{< note >}}
در حال حاضر نمی‌توانید `CompositePodGroupTemplates` جدیدی اضافه کنید یا موارد موجود را حذف کنید. تنها می‌توانید مقدار `minCount` را در سیاست زمان‌بندی گروهی تعریف‌شده در `PodGroupTemplates` برگ تغییر دهید.
{{< /note >}}

#### مثال

مثال زیر یک `Workload` سلسله‌مراتبی را با یک قالب `CompositePodGroup` تعریف می‌کند که زمان‌بندی گروهی را در میان دو قالب `PodGroup` فرزند (`minGroupCount: 2`) اعمال می‌کند و هر یک از این قالب‌ها سیاست زمان‌بندی گروهی خود را مشخص می‌کند:

```yaml
apiVersion: scheduling.k8s.io/v1alpha3
kind: Workload
metadata:
  name: gang-of-gangs-workload
  namespace: default
spec:
  compositePodGroupTemplates:
  - name: root
    schedulingPolicy:
      gang:
        # Requires both child PodGroups to be schedulable together
        minGroupCount: 2
    podGroupTemplates:
    - name: workers-a
      schedulingPolicy:
        gang:
          # Requires 4 Pods in this group to be schedulable
          minCount: 4
    - name: workers-b
      schedulingPolicy:
        gang:
          # Requires 4 Pods in this group to be schedulable
          minCount: 4
```

## زمان‌بندی گروهی با Jobها

{{< feature-state feature_gate_name="WorkloadWithJob" >}}

هنگامی که feature gateِ
[`WorkloadWithJob`](/docs/reference/command-line-tools-reference/feature-gates/)
فعال باشد، کنترل‌کنندهٔ
[Job](/docs/concepts/workloads/controllers/job/) پیش از ایجاد هر Pod، پیکربندی
`.spec.scheduling` یک Job را به آبجکت‌های `Workload` و `PodGroup` تبدیل می‌کند. برای استفاده از زمان‌بندی گروهی، فیلد `.spec.scheduling.schedulingPolicy.gang` را روی Job تنظیم کنید. اگر `gang.minCount` حذف شود، مقدار پیش‌فرض آن برابر با `.spec.parallelism` در Job خواهد بود؛ بنابراین همهٔ Podها باید با هم قابل زمان‌بندی باشند تا هیچ‌یک از آن‌ها به نودها متصل شود.

اگر `.spec.scheduling` حذف شود، Job به‌طور پیش‌فرض از سیاست `basic` استفاده می‌کند که زمان‌بندی استاندارد Pod به Pod را حفظ می‌کند. در هر دو حالت، کنترل‌کنندهٔ Job آبجکت‌های `Workload` و `PodGroup` را برای شما ایجاد می‌کند و نیازی نیست خودتان آن‌ها را بسازید. سایر کنترل‌کننده‌های بار کاری (مانند JobSet) ممکن است آبجکت‌های `Workload` و `PodGroup` خود را به‌طور مستقل مدیریت کنند.

برای مشاهدهٔ مجموعهٔ کامل فیلدهای زمان‌بندی و مثال‌ها، به
[یکپارچه‌سازی با Workload APIها](/docs/concepts/workloads/controllers/job/#integrate-with-workload-apis) مراجعه کنید.

## {{% heading "whatsnext" %}}

* با [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) آشنا شوید.
* در نمای کلی [PodGroup API](/docs/concepts/workloads/podgroup-api/) ببینید که PodGroupها چگونه از Workloadها ایجاد می‌شوند.
* دربارهٔ اینکه Podها چگونه از طریق فیلد [گروه زمان‌بندی](/docs/concepts/workloads/pods/scheduling-group/) به PodGroup خود ارجاع می‌دهند، مطالعه کنید.
* با [زمان‌بندی بار کاری آگاه از توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/) آشنا شوید.
* الگوریتم [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) را درک کنید.
