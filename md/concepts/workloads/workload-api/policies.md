---
title: سیاست‌های زمان‌بندی PodGroup
content_type: concept
weight: 10
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

هر [PodGroup](/docs/concepts/workloads/podgroup-api/) باید یک سیاست زمان‌بندی را
در فیلد `spec.schedulingPolicy` خود اعلام کند. این سیاست تعیین می‌کند که زمان‌بند با
مجموعه‌ی Podهای گروه چگونه رفتار کند.

<!-- body -->

## انواع سیاست

فیلد `schedulingPolicy` از دو نوع سیاست پشتیبانی می‌کند: `basic` و `gang`.
باید دقیقاً یکی از آن‌ها را تعیین کنید.

### سیاست Basic

سیاست `basic` به زمان‌بند دستور می‌دهد همه‌ی Podها را بر مبنای بهترین تلاش (best-effort) ارزیابی کند.
برخلاف سیاست `gang`، یک PodGroup که از سیاست `basic` استفاده می‌کند، صرف‌نظر از اینکه
چه تعداد از Podهای آن در حال حاضر قابل زمان‌بندی هستند، امکان‌پذیر در نظر گرفته می‌شود.

دلیل اصلی استفاده از سیاست `basic`، سازمان‌دهی Podها در یک گروه برای مشاهده‌پذیری و مدیریت
بهتر است، در حالی که همچنان در یک
[چرخه‌ی زمان‌بندی PodGroup](/docs/concepts/scheduling-eviction/podgroup-scheduling/#podgroup-scheduling-cycle) واحد و اتمی با هم ارزیابی می‌شوند.

این سیاست برای گروه‌هایی مناسب است که به راه‌اندازی همزمان نیاز ندارند اما به‌طور منطقی
به یکدیگر تعلق دارند، یا برای باز کردن راه محدودیت‌های سطح گروهی که دلالتی بر
جای‌گذاری «همه یا هیچ» ندارند.

```yaml
schedulingPolicy:
  basic: {}
```

### سیاست Gang

سیاست `gang` زمان‌بندی «همه یا هیچ» را اعمال می‌کند. این سیاست برای بارهای کاری
به‌شدت وابسته به هم که راه‌اندازی ناقص در آن‌ها به بن‌بست یا هدررفت منابع می‌انجامد، ضروری است.

از این سیاست می‌توان برای [Jobها](/docs/concepts/workloads/controllers/job/)
یا هر فرایند دسته‌ای (batch) دیگری استفاده کرد که در آن همه‌ی workerها باید به‌طور همزمان اجرا شوند تا پیشرفتی حاصل شود.

سیاست `gang` به فیلد `minCount` نیاز دارد که حداقل تعداد Podهایی است که باید
به‌طور همزمان قابل زمان‌بندی باشند تا گروه امکان‌پذیر باشد:

```yaml
schedulingPolicy:
  gang:
    # The number of Pods that must be schedulable simultaneously
    # for the group to be admitted.
    minCount: 4
```

## تنظیم سیاست‌ها از طریق PodGroupTemplates

هنگام استفاده از [Workload API](/docs/concepts/workloads/workload-api/)، سیاست‌های
زمان‌بندی را درون `PodGroupTemplates` تعریف می‌کنید. کنترل‌کننده‌ی بار کاری سیاست را از
الگو در هر PodGroupی که ایجاد می‌کند کپی می‌کند و بدین ترتیب PodGroup خودبسنده می‌شود. تغییرات در
الگوهای Workload تنها بر PodGroupهای تازه‌ایجادشده اثر می‌گذارند، نه بر موارد موجود.

برای PodGroupهای مستقل (که بدون Workload ایجاد شده‌اند)، `spec.schedulingPolicy` را
مستقیماً روی خود PodGroup تنظیم می‌کنید.

## سیاست‌ها در CompositePodGroupها

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gate [`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
و {{< glossary_tooltip text="گروه API" term_id="api-group" >}} `scheduling.k8s.io/v1alpha3`
فعال باشند، `CompositePodGroupTemplates` در یک Workload و آبجکت‌های `CompositePodGroup` نیز
یک سیاست زمان‌بندی اعلام می‌کنند.

در حالی که سیاست زمان‌بندی در یک `PodGroup` بر مجموعه‌ای از Podهای منفرد حاکم است، سیاست
زمان‌بندی یک `CompositePodGroup` بر **گروه‌های فرزند** مستقیم آن حاکم است (که می‌توانند هم
آبجکت‌های `CompositePodGroup` و هم `PodGroup` باشند).

### انواع سیاست برای CompositePodGroupها

همانند `PodGroups`، فیلد `spec.schedulingPolicy` یک `CompositePodGroup` از دو
نوع پشتیبانی می‌کند:

- **`basic`**: گروه‌های فرزند درون `CompositePodGroup` به‌طور مستقل ارزیابی و پذیرفته می‌شوند.
- **`gang`**: زمان‌بندی چندسطحی همه یا هیچ را در میان گروه‌های فرزند اعمال می‌کند.
  `CompositePodGroup` تنها در صورتی قابل زمان‌بندی است که دست‌کم `minGroupCount` گروه فرزند بتوانند
  به‌طور همزمان زمان‌بندی شوند.

```yaml
schedulingPolicy:
  gang:
    # The minimum number of child groups that must be schedulable
    # simultaneously for this composite group to be admitted.
    minGroupCount: 2
```

### تنظیم سیاست‌های مرکب از طریق الگوها

هنگام استفاده از [Workload API](/docs/concepts/workloads/workload-api/)، سیاست‌های زمان‌بندی برای
`CompositePodGroups` درون `CompositePodGroupTemplates` تعریف می‌شوند. کنترل‌کننده‌های بار کاری
`schedulingPolicy` تعیین‌شده در الگوها را در هر `CompositePodGroup` که در زمان اجرا ایجاد می‌شود کپی می‌کنند.
برخلاف `PodGroupTemplates` برگ که در آن‌ها `minCount` قابل به‌روزرسانی است، `minGroupCount` در یک
`CompositePodGroupTemplate` تغییرناپذیر است.

## {{% heading "whatsnext" %}}

* برای اینکه ببینید سیاست‌ها در زمان اجرا چگونه منتقل می‌شوند، [PodGroup API](/docs/concepts/workloads/podgroup-api/) را ببینید.
* درباره‌ی [Workload API](/docs/concepts/workloads/workload-api/) که PodGroupTemplateها را تعریف می‌کند بیاموزید.
* درباره‌ی [زمان‌بندی PodGroup](/docs/concepts/scheduling-eviction/podgroup-scheduling/) بخوانید.
* درباره‌ی الگوریتم [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) بخوانید.
* درباره‌ی [بلوک‌های سازنده‌ی زمان‌بندی و کتابخانه‌ی workloadbuilder](/docs/concepts/workloads/workload-api/workloadbuilder/) که کنترل‌کننده‌ها برای تبدیل این سیاست‌ها به کار می‌برند بیاموزید.
