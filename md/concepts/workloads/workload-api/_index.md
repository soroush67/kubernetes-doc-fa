---
title: "Workload API"
weight: 20
simple_list: true
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

منبع API با نام `Workload` الزامات زمان‌بندی و ساختار یک برنامه‌ی چند-Pod را
تعریف می‌کند. در حالی که کنترل‌کننده‌های بار کاری مانند [Job](/docs/concepts/workloads/controllers/job/)
وضعیت زمان اجرای برنامه را مدیریت می‌کنند، `Workload` مشخص می‌کند که گروه‌هایی از `Pods`
چگونه باید زمان‌بندی شوند. کنترل‌کننده‌ی Job تنها کنترل‌کننده‌ی داخلی است که در زمان اجرا
آبجکت‌های [PodGroup](/docs/concepts/workloads/podgroup-api/) را از
`PodGroupTemplates` آن `Workload` ایجاد می‌کند.

<!-- body -->

## Workload چیست؟

منبع API با نام Workload بخشی از
{{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1beta1`
است و پیش از آنکه بتوانید از این API استفاده کنید، باید آن گروه API و همچنین
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `GenericWorkload`
در کلاستر شما فعال باشند.

یک `Workload` یک الگوی سیاست ایستا و بلندمدت است. این الگو تعریف می‌کند که چه سیاست‌های
زمان‌بندی‌ای باید روی گروه‌هایی از Podها اعمال شوند، اما خودش وضعیت زمان اجرا را دنبال نمی‌کند.
وضعیت زمان‌بندی در زمان اجرا توسط آبجکت‌های [PodGroup](/docs/concepts/workloads/podgroup-api/)
نگهداری می‌شود که کنترل‌کننده‌ها آن‌ها را از `PodGroupTemplates` آن `Workload` ایجاد می‌کنند.

## ساختار API

یک `Workload` از دو فیلد تشکیل شده است: فهرستی از `PodGroupTemplates` و یک ارجاع
اختیاری به کنترل‌کننده. کل spec یک `Workload` پس از ایجاد تغییرناپذیر است: نمی‌توانید
الگوهای موجود را تغییر دهید، الگوهای جدید اضافه کنید یا الگوهایی را از `podGroupTemplates` حذف کنید.

### PodGroupTemplates

فهرست `spec.podGroupTemplates` اجزای متمایز بار کاری شما را تعریف می‌کند.
برای مثال، یک Job یادگیری ماشین ممکن است یک الگوی `driver` و یک الگوی `worker` داشته باشد.

هر مدخل در `podGroupTemplates` باید موارد زیر را داشته باشد:
1. یک `name` یکتا که برای ارجاع به الگو در `spec.podGroupTemplateRef` آن `PodGroup` استفاده می‌شود.
2. یک [سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/) (`basic` یا `gang`).

هر مدخل همچنین می‌تواند فیلدهای
[اولویت و حالت اختلال](/docs/concepts/workloads/workload-api/disruption-and-priority/)
داشته باشد.

{{< note >}}
در v1.36، فیلدهای [اولویت و حالت اختلال](/docs/concepts/workloads/workload-api/disruption-and-priority/)
توسط feature gate
[`WorkloadAwarePreemption`](/docs/reference/command-line-tools-reference/feature-gates/#WorkloadAwarePreemption)
فعال می‌شدند. این gate در v1.37 در
[`GenericWorkload`](/docs/reference/command-line-tools-reference/feature-gates/#GenericWorkload) ادغام شد.
{{< /note >}}

حداکثر تعداد PodGroupTemplateها در یک Workload برابر 8 است.

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

هنگامی که یک کنترل‌کننده‌ی بار کاری یک `PodGroup` را از یکی از این الگوها ایجاد می‌کند،
`schedulingPolicy` را در spec خودِ آن `PodGroup` کپی می‌کند. تغییرات در `Workload` تنها بر
`PodGroups` تازه‌ایجادشده اثر می‌گذارند، نه بر موارد موجود.

### ارجاع به آبجکت کنترل‌کننده‌ی بار کاری

فیلد `controllerRef` آن Workload را به آبجکت سطح‌بالای مشخصی که برنامه را تعریف می‌کند پیوند می‌دهد،
مانند یک [Job](/docs/concepts/workloads/controllers/job/) یا یک CRD سفارشی. این کار برای مشاهده‌پذیری و ابزارها مفید است.
این داده برای زمان‌بندی یا مدیریت Workload استفاده نمی‌شود.

### CompositePodGroupTemplates

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gate
[`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
و {{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1alpha3`
فعال باشند، می‌توانید از `CompositePodGroupTemplates` برای تعریف الزامات زمان‌بندی چندسطحی و سلسله‌مراتبی
در یک `Workload` استفاده کنید. این الزامات می‌توانند شامل اعمال محدودیت‌های توپولوژی تودرتو
در لایه‌های مختلف زیرساخت کلاستر (زمان‌بندی چندسطحی آگاه از توپولوژی)،
زمان‌بندی همه یا هیچ در میان گروه‌های فرزند (زمان‌بندی گروهی چندسطحی)، یا سیاست‌های اختلال
در سطح گروه باشند.

`CompositePodGroupTemplates` را می‌توان با استفاده از فیلد `spec.compositePodGroupTemplates` در
API آن `Workload` تعریف کرد. در زمان اجرا، کنترل‌کننده‌های بار کاری آبجکت‌های [CompositePodGroup](/docs/concepts/workloads/compositepodgroup-api/)
و [PodGroup](/docs/concepts/workloads/podgroup-api/) را از این الگوها ایجاد می‌کنند تا وضعیت زمان‌بندی
سلسله‌مراتب را در زمان اجرا نگهداری کنند. در حالی که آبجکت‌های `PodGroup` گروه‌هایی از Podها را در برگ‌ها مدیریت می‌کنند،
آبجکت‌های `CompositePodGroup` نماینده‌ی گروه‌های غیربرگ هستند که سیاست‌های زمان‌بندی را در میان گروه‌های فرزند اعمال می‌کنند.

{{< note >}}
در مشخصات یک `Workload`، فیلدهای `spec.compositePodGroupTemplates` و `spec.podGroupTemplates`
یک اجتماع انحصاری (union) تشکیل می‌دهند: یک `Workload` باید یا `spec.podGroupTemplates` (برای
بارهای کاری تخت) یا `spec.compositePodGroupTemplates` (برای بارهای کاری سلسله‌مراتبی) را تعریف کند، اما نمی‌تواند
هر دو را تعیین کند.
{{< /note >}}

#### ساختار و محدودیت‌ها

فیلد `spec.compositePodGroupTemplates` الگوهای غیربرگ را در یک درخت سلسله‌مراتبی
از الگوهای گروه تعریف می‌کند. هر مدخل نماینده‌ی الگویی برای یک `CompositePodGroup` است و می‌تواند شامل موارد زیر باشد:

- **الگوهای فرزند**: `CompositePodGroupTemplates` تودرتو (برای گروه‌های میانی
  غیربرگ) یا `PodGroupTemplates` (برای گروه‌های برگ که Podها را در بر دارند).
- **سیاست زمان‌بندی**: مشخص می‌کند که گروه‌های فرزند درون این گروه مرکب چگونه
  زمان‌بندی شوند:
  - `basic`: گروه‌های فرزند به‌طور مستقل پذیرفته و زمان‌بندی می‌شوند.
  - `gang`: زمان‌بندی چندسطحی همه یا هیچ را در میان گروه‌های فرزند اعمال می‌کند.
    به `minGroupCount` نیاز دارد که حداقل تعداد گروه‌های فرزندی را مشخص می‌کند
    که باید به‌طور همزمان قابل زمان‌بندی باشند تا گروه مرکب امکان‌پذیر باشد.
- **محدودیت‌های زمان‌بندی**:
  [محدودیت‌های توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/) اختیاری
  برای زمان‌بندی چندسطحی آگاه از توپولوژی.
- **اولویت، سیاست پس‌گیری و حالت اختلال**: فیلدهای اختیاری `priorityClassName`،
  `disruptionMode` (`Single` یا `All`) و `preemptionPolicy` برای
  [پس‌گیری آگاه از بار کاری](/docs/concepts/workloads/workload-api/disruption-and-priority/).

برای تضمین پایداری کلاستر و کارایی control plane، سلسله‌مراتب الگوهای گروه
محدودیت‌های زیر را اعمال می‌کند:

- **حداکثر عمق تودرتویی**: سلسله‌مراتب الگوهای گروه حداکثر از عمق
  4 سطح پشتیبانی می‌کند.
- **محدودیت فهرست**: هر فهرست `compositePodGroupTemplates` و `podGroupTemplates` به‌طور قطعی
  به حداکثر 8 آیتم محدود است.

{{< note >}}
در حال حاضر، نمی‌توانید `CompositePodGroupTemplates` جدید اضافه کنید یا موارد موجود را حذف کنید. تنها می‌توانید
مقدار `minCount` را در سیاست زمان‌بندی گروهی تعریف‌شده در `PodGroupTemplates` برگ تغییر دهید.
{{< /note >}}

#### مثال

مثال زیر یک `Workload` سلسله‌مراتبی را با یک الگوی `CompositePodGroup` تعریف می‌کند
که زمان‌بندی گروهی را در میان دو الگوی `PodGroup` فرزند (`minGroupCount: 2`) اعمال می‌کند،
که هر یک سیاست زمان‌بندی گروهی خاص خود را تعیین می‌کنند:

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

هنگامی که feature gate
[`WorkloadWithJob`](/docs/reference/command-line-tools-reference/feature-gates/)
فعال باشد، کنترل‌کننده‌ی
[Job](/docs/concepts/workloads/controllers/job/) پیکربندی
`.spec.scheduling` یک Job را پیش از ایجاد هر Podی به آبجکت‌های `Workload` و `PodGroup`
تبدیل می‌کند. شما با تنظیم
`.spec.scheduling.schedulingPolicy.gang` روی Job، زمان‌بندی گروهی را انتخاب می‌کنید؛ اگر `gang.minCount`
حذف شود، مقدار پیش‌فرض آن `.spec.parallelism` آن Job است، بنابراین همه‌ی Podها باید پیش از آنکه هیچ‌یک از آن‌ها
به نودها متصل شوند، با هم قابل زمان‌بندی باشند.

هنگامی که `.spec.scheduling` حذف شود، Job به‌طور پیش‌فرض از سیاست `basic` استفاده می‌کند که
زمان‌بندی استاندارد Pod به Pod را حفظ می‌کند. در هر دو حالت، کنترل‌کننده‌ی Job
`Workload` و `PodGroup` را برای شما ایجاد می‌کند، بنابراین لازم نیست خودتان آن‌ها را ایجاد کنید.
سایر کنترل‌کننده‌های بار کاری (مانند JobSet) ممکن است آبجکت‌های `Workload` و
`PodGroup` خود را به‌طور مستقل مدیریت کنند.

برای مجموعه‌ی کامل فیلدهای زمان‌بندی و مثال‌ها،
[یکپارچه‌سازی با Workload APIها](/docs/concepts/workloads/controllers/job/#integrate-with-workload-apis) را ببینید.

## {{% heading "whatsnext" %}}

* درباره‌ی [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) بیاموزید.
* ببینید PodGroupها چگونه از Workloadها ایجاد می‌شوند، در نمای کلی [PodGroup API](/docs/concepts/workloads/podgroup-api/).
* بخوانید که Podها چگونه از طریق فیلد [گروه زمان‌بندی](/docs/concepts/workloads/pods/scheduling-group/) به PodGroup خود ارجاع می‌دهند.
* درباره‌ی [زمان‌بندی بار کاری آگاه از توپولوژی](/docs/concepts/workloads/workload-api/topology-aware-scheduling/) بیاموزید.
* الگوریتم [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) را درک کنید.
