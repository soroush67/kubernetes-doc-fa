---
title: چرخه عمر PodGroup
content_type: concept
weight: 10
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

یک [PodGroup](/docs/concepts/workloads/podgroup-api/) به‌عنوان یک واحد زمان‌بندی می‌شود و تا زمانی که Podهای آن
هنوز در حال اجرا هستند، در برابر حذف زودهنگام محافظت می‌شود.

<!-- body -->

## مالکیت و چرخه عمر

`PodGroups` از طریق `ownerReferences` استاندارد، متعلق به کنترل‌کننده بار کاری‌ای هستند که آن‌ها را ایجاد کرده است (برای مثال یک Job).
هنگامی که آبجکت مالک حذف شود، `PodGroups` به‌طور خودکار
توسط جمع‌آوری زباله حذف می‌شوند.

نام‌های `PodGroup` باید در یک فضای نام (namespace) یکتا باشند و باید
[زیردامنه‌های DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشند.

## ترتیب ایجاد

کنترل‌کننده‌ها باید آبجکت‌ها را به این ترتیب ایجاد کنند:

1. `Workload` — قالب سیاست زمان‌بندی.
2. `PodGroup` — نمونه زمان اجرا.
3. `Pods` — با `spec.schedulingGroup.podGroupName` که به `PodGroup` اشاره می‌کند.

اگر یک `PodGroup` شامل `podGroupTemplateRef` باشد که به `Workload`ای اشاره می‌کند که
وجود ندارد (یا در حال حذف است)، API server درخواست ایجاد `PodGroup` را رد می‌کند.
`Workload` ارجاع‌شده باید پیش از ایجاد `PodGroup` وجود داشته باشد.

اگر یک `Pod` به `PodGroup`ای ارجاع دهد که هنوز وجود ندارد، `Pod` در وضعیت pending باقی می‌ماند.
زمان‌بند (scheduler) پس از ایجاد `PodGroup`، به‌طور خودکار `Pod` را در صف زمان‌بندی قرار می‌دهد.

## محافظت در برابر حذف

یک `PodGroup` را تا زمانی که هر یک از Podهای آن هنوز در حال اجرا باشد نمی‌توان به‌طور کامل حذف کرد.
یک finalizer اختصاصی تضمین می‌کند که حذف تا زمانی که همه `Pods` ارجاع‌دهنده به
`PodGroup` به یک فاز پایانی (`Succeeded` یا `Failed`) برسند، مسدود بماند.

## PodGroupهای مدیریت‌شده توسط کنترل‌کننده و توسط کاربر

در بیشتر موارد، کنترل‌کننده‌های بار کاری (برای مثال Job) به‌طور خودکار `PodGroups` را ایجاد می‌کنند
(مدیریت‌شده توسط کنترل‌کننده). کنترل‌کننده `podGroupName` را برای هر Pod
در زمان ایجاد تعیین می‌کند، مشابه روشی که یک `DaemonSet` وابستگی نود (node affinity) را برای هر Pod تنظیم می‌کند.

اگر به کنترل بیشتری بر نام‌گذاری و چرخه عمر نیاز دارید، می‌توانید آبجکت‌های `PodGroup` را مستقیماً ایجاد کنید و
`spec.schedulingGroup.podGroupName` را خودتان در قالب‌های Pod تنظیم کنید
(مدیریت‌شده توسط کاربر). این کار کنترل کامل بر ایجاد و نام‌گذاری `PodGroup` را در اختیار شما قرار می‌دهد.

## محدودیت‌ها

* همه Podهای یک `PodGroup` باید از `.spec.schedulerName` یکسانی استفاده کنند.
  اگر ناهمخوانی تشخیص داده شود، زمان‌بند همه Podهای گروه را به‌عنوان غیرقابل زمان‌بندی رد می‌کند.
* همه Podهای یک `PodGroup` باید از `.spec.priority` یکسانی استفاده کنند.
  اگر ناهمخوانی تشخیص داده شود، زمان‌بند همه Podهای گروه را به‌عنوان غیرقابل زمان‌بندی رد می‌کند.
* همه Podهای یک `PodGroup` باید از `.spec.preemptionPolicy` یکسانی استفاده کنند.
  اگر ناهمخوانی تشخیص داده شود، زمان‌بند همه Podهای گروه را به‌عنوان غیرقابل زمان‌بندی رد می‌کند.
* فیلد `spec.schedulingGroup` روی یک Pod تغییرناپذیر است.
  پس از تنظیم، یک Pod نمی‌تواند به PodGroup دیگری منتقل شود.
* حداکثر تعداد `PodGroupTemplates` در یک `Workload` واحد 8 است.
* زمان‌بند اطلاعات وضعیت مربوط به وضعیت عملیاتی جاری یک PodGroup
  یا تلاش‌های زمان‌بندی بعدی پس از جای‌گذاری اولیه را به‌روزرسانی نمی‌کند. در نتیجه، وضعیت PodGroup
  هنگامی که Podهای موجود از کار بیفتند، بیرون رانده (evict) شوند یا خاتمه یابند، یا هنگامی که Podهای تازه مشاهده‌شده زمان‌بندی نشوند، به‌روزرسانی نمی‌شود.

## {{% heading "whatsnext" %}}

* با نمای کلی و ساختار [PodGroup API](/docs/concepts/workloads/podgroup-api/) آشنا شوید.
* با [Workload API](/docs/concepts/workloads/workload-api/) که `PodGroupTemplates` را فراهم می‌کند آشنا شوید.
* ببینید Podها چگونه از طریق فیلد [گروه زمان‌بندی (scheduling group)](/docs/concepts/workloads/pods/scheduling-group/) به PodGroup خود ارجاع می‌دهند.
* الگوریتم [زمان‌بندی گروهی (gang scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/) را درک کنید.
* برای جزئیات درباره `basic` و `gang`، [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) را بخوانید.
