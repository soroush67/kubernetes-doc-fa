---
title: چرخه‌ی حیات CompositePodGroup
content_type: concept
weight: 10
---

<!-- overview -->
{{< feature-state feature_gate_name="CompositePodGroup" >}}

یک [CompositePodGroup](/docs/concepts/workloads/compositepodgroup-api/) یک گره غیربرگ را
در سلسله‌مراتب چندسطحی `PodGroup` نمایش می‌دهد. برخلاف منابع `PodGroup`، منابع `CompositePodGroup`
مستقیماً شامل Podها نیستند. در عوض، سلسله‌مراتبی از آبجکت‌های `CompositePodGroup` و
`PodGroup` نوادگان را نگهداری می‌کنند و سیاست‌های زمان‌بندی‌ای را حمل می‌کنند که بر گروه‌های فرزندشان اعمال می‌شوند.

<!-- body -->

## مالکیت و جمع‌آوری زباله

یک آبجکت `CompositePodGroup`، همراه با منابع `CompositePodGroup` و `PodGroup`
نوادگانش، از طریق `ownerReferences` کوبرنتیز در مالکیت کنترل‌کننده‌ی بار کاری‌ای است که آن را ایجاد کرده است.
هنگامی که آبجکت بار کاری مالک حذف شود، جمع‌آوری زباله‌ی آبشاری (cascading garbage collection) به‌طور خودکار
سلسله‌مراتب گروه مرتبط را حذف می‌کند.

نام‌های `CompositePodGroup` باید درون یک فضای نام (namespace) یکتا باشند و باید
[زیردامنه‌های DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشند.

## ترتیب ایجاد

برای اطمینان از حل صحیح سلسله‌مراتب و زمان‌بندی درست، کنترل‌کننده‌های بار کاری منابع را به
ترتیب بالا به پایین ایجاد می‌کنند:

1. **`Workload`**: قالب‌های ایستا (`CompositePodGroupTemplates` و `PodGroupTemplates`) را تعریف می‌کند.
2. **`CompositePodGroup` ریشه**: با `spec.workloadRef`ای ایجاد می‌شود که به قالب ریشه در
   `Workload` اشاره می‌کند.
3. **`CompositePodGroups` و `PodGroups` نوادگان**: به‌صورت بالا به پایین ایجاد می‌شوند. هر گروه فرزند
   والد خود را با استفاده از `spec.parentCompositePodGroupName` و قالب خود را با استفاده از `spec.workloadRef` مشخص می‌کند.
4. **`Pods`**: با `spec.schedulingGroup.podGroupName`ای ایجاد می‌شوند که به `PodGroup` برگ آن‌ها اشاره می‌کند.

اگر یک گروه به `CompositePodGroup` والدی ارجاع دهد که وجود ندارد، یا اگر یک Pod به
`PodGroup`ای ارجاع دهد که هنوز ایجاد نشده است، زمان‌بند زمان‌بندی را تا زمانی که همه‌ی منابع والد
در سلسله‌مراتب وجود داشته باشند به تعویق می‌اندازد.

## محدودیت‌ها و قواعد اعتبارسنجی

- **نام زمان‌بند یکسان**: همه‌ی Podها در سراسر یک سلسله‌مراتب `CompositePodGroup` باید از
  `spec.schedulerName` یکسانی استفاده کنند. اگر عدم تطابقی شناسایی شود، زمان‌بند سلسله‌مراتب را
  به‌عنوان غیرقابل زمان‌بندی رد می‌کند.
- **اولویت یکسان**: همه‌ی Podها در سراسر یک سلسله‌مراتب `CompositePodGroup` باید
  مقدار یکسانی برای `spec.priority` مشخص کنند که باید با اولویت مشخص‌شده توسط گروه ریشه برابر باشد. اگر
  عدم تطابقی شناسایی شود، زمان‌بند سلسله‌مراتب را به‌عنوان غیرقابل زمان‌بندی رد می‌کند.
- **سیاست پیش‌دستی یکسان**: همه‌ی Podها در سراسر یک سلسله‌مراتب `CompositePodGroup` باید از
  `spec.preemptionPolicy` یکسانی استفاده کنند. افزون بر این، هنگامی که
  feature gate
  [PodGroupPreemptionPolicy](/docs/reference/command-line-tools-reference/feature-gates/podgroup-preemption-policy/)
  فعال باشد، سیاست پیش‌دستی گروه ریشه باید با سیاستی که
  Podها مشخص کرده‌اند برابر باشد. اگر عدم تطابقی شناسایی شود، زمان‌بند سلسله‌مراتب را به‌عنوان غیرقابل زمان‌بندی رد می‌کند.
- **حداکثر عمق تودرتویی**: سلسله‌مراتب قالب‌های گروه از حداکثر عمق ۴ سطح پشتیبانی می‌کند.
- **محدودیت تعداد اقلام فهرست**: حداکثر تعداد `CompositePodGroupTemplates` و
  `PodGroupTemplates` فرزند در هر سطح از یک `Workload`، ۸ است.
- **تغییرناپذیری تعداد گروه gang**: فیلد `spec.schedulingPolicy.gang.minGroupCount` در یک
  `CompositePodGroup` پس از ایجاد تغییرناپذیر است.
- **تغییرناپذیری ارجاع‌های سلسله‌مراتبی**: `spec.parentCompositePodGroupName` در گروه‌ها و
  `spec.schedulingGroup` در Podها پس از تنظیم شدن تغییرناپذیرند.

## {{% heading "whatsnext" %}}

* مرور کلی [API مربوط به CompositePodGroup](/docs/concepts/workloads/compositepodgroup-api/) را بخوانید.
* با [Workload API](/docs/concepts/workloads/workload-api/) و تعریف‌های قالب آشنا شوید.
* ببینید گروه‌های برگ در [API مربوط به PodGroup](/docs/concepts/workloads/podgroup-api/) چگونه ساختاربندی می‌شوند.
* درباره‌ی [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) بخوانید.
* با [پیش‌دستی آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/) آشنا شوید.
