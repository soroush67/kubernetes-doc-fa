---
reviewers:
- nelvadas
title: محدوده‌های محدودیت
api_metadata:
- apiVersion: "v1"
  kind: "LimitRange"
content_type: concept
weight: 10
---

<!-- overview -->

به‌طور پیش‌فرض، کانتینرها روی یک کلاستر کوبرنتیز با
[منابع محاسباتی](/docs/concepts/configuration/manage-resources-containers/) نامحدود اجرا می‌شوند.
مدیران (که _اپراتورهای کلاستر_ نیز نامیده می‌شوند) با استفاده از [سهمیه‌های منابع](/docs/concepts/policy/resource-quotas/) کوبرنتیز
می‌توانند مصرف و ایجاد منابع کلاستر (مانند زمان CPU، حافظه و ذخیره‌سازی ماندگار) را درون یک
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} مشخص محدود کنند.
درون یک فضای نام، یک {{< glossary_tooltip text="Pod" term_id="Pod" >}} می‌تواند به همان اندازه CPU و حافظه مصرف کند که ResourceQuotaهای اعمال‌شده بر آن فضای نام اجازه می‌دهند.
به‌عنوان اپراتور کلاستر یا مدیر سطح فضای نام، ممکن است همچنین نگران
این باشید که یک آبجکت منفرد نتواند همهٔ منابع موجود درون یک فضای نام را در انحصار خود بگیرد.

LimitRange سیاستی برای محدودکردن تخصیص منابع (limits و requests) است که می‌توانید برای
هر نوع آبجکت قابل اعمال (مانند Pod یا {{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}}) در یک فضای نام مشخص کنید.

<!-- body -->

یک _LimitRange_ محدودیت‌هایی فراهم می‌کند که می‌توانند:

- حداقل و حداکثر مصرف منابع محاسباتی را برای هر Pod یا Container در یک فضای نام الزامی کنند.
- حداقل و حداکثر درخواست ذخیره‌سازی را برای هر
  {{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}} در یک فضای نام الزامی کنند.
- نسبتی میان request و limit برای یک منبع در یک فضای نام الزامی کنند.
- مقادیر پیش‌فرض request/limit را برای منابع محاسباتی در یک فضای نام تنظیم کنند و آن‌ها را به‌طور خودکار
  در زمان اجرا به Containerها تزریق کنند.

کوبرنتیز هر زمان که دست‌کم یک آبجکت LimitRange در یک فضای نام مشخص وجود داشته باشد،
تخصیص منابع به پادهای آن فضای نام را محدود می‌کند.

نام یک آبجکت LimitRange باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

## محدودیت‌ها بر limitها و requestهای منابع

- مدیر یک LimitRange در یک فضای نام ایجاد می‌کند.
- کاربران آبجکت‌هایی مانند Podها یا PersistentVolumeClaimها را در آن فضای نام ایجاد می‌کنند
  (یا تلاش می‌کنند ایجاد کنند).
- ابتدا، admission controller ‏LimitRange مقادیر پیش‌فرض request و limit را
  برای همهٔ پادها (و کانتینرهایشان) که الزامات منابع محاسباتی را تنظیم نکرده‌اند اعمال می‌کند.
- سپس، LimitRange مصرف را دنبال می‌کند تا اطمینان حاصل کند از حداقل،
  حداکثر و نسبت منابع تعریف‌شده در هر LimitRange موجود در فضای نام تجاوز نمی‌کند.
- اگر تلاش کنید آبجکتی (Pod یا PersistentVolumeClaim) را ایجاد یا به‌روزرسانی کنید که
  یکی از محدودیت‌های LimitRange را نقض می‌کند، درخواست شما به سرور API با کد وضعیت HTTP
  `403 Forbidden` و پیامی که محدودیت نقض‌شده را توضیح می‌دهد ناموفق خواهد بود.
- اگر در یک فضای نام LimitRangeای اضافه کنید که بر منابع مرتبط با محاسبات
  مانند `cpu` و `memory` اعمال می‌شود، باید requestها یا limitهایی برای آن مقادیر مشخص کنید.
  در غیر این صورت، سیستم ممکن است ایجاد Pod را رد کند.
- اعتبارسنجی‌های LimitRange فقط در مرحلهٔ پذیرش Pod انجام می‌شوند، نه روی پادهای در حال اجرا.
  اگر یک LimitRange را اضافه یا تغییر دهید، پادهایی که از قبل در آن فضای نام وجود دارند
  بدون تغییر باقی می‌مانند.
- اگر دو یا چند آبجکت LimitRange در فضای نام وجود داشته باشند، قطعی نیست
  که کدام مقدار پیش‌فرض اعمال خواهد شد.

## LimitRange و بررسی‌های پذیرش برای پادها

یک LimitRange سازگاری مقادیر پیش‌فرضی را که اعمال می‌کند بررسی **نمی‌کند**.
این بدان معناست که مقدار پیش‌فرض _limit_ که توسط LimitRange تنظیم می‌شود، ممکن است
کمتر از مقدار _request_ مشخص‌شده برای کانتینر در مشخصاتی باشد که یک کلاینت
به سرور API ارسال می‌کند. اگر چنین اتفاقی بیفتد، Pod نهایی قابل زمان‌بندی نخواهد بود.

برای مثال، یک LimitRange را با مانیفست زیر تعریف می‌کنید:
{{< note >}}
مثال‌های زیر درون فضای نام پیش‌فرض کلاستر شما عمل می‌کنند، زیرا پارامتر namespace
تعریف نشده است و محدودهٔ LimitRange به سطح فضای نام محدود است.
این بدان معناست که هرگونه ارجاع یا عملیات درون این مثال‌ها با
عناصری درون فضای نام پیش‌فرض کلاستر شما تعامل خواهد داشت. می‌توانید فضای نام
عملیاتی را با پیکربندی namespace در فیلد `metadata.namespace` بازنویسی کنید.
{{< /note >}}

{{% code_sample file="concepts/policy/limit-range/problematic-limit-range.yaml" %}}

همراه با یک Pod که request منبع CPU برابر `700m` را اعلام می‌کند، اما limitی اعلام نمی‌کند:

{{% code_sample file="concepts/policy/limit-range/example-conflict-with-limitrange-cpu.yaml" %}}

در این صورت آن Pod زمان‌بندی نخواهد شد و با خطایی مشابه زیر ناموفق خواهد بود:
```
Pod "example-conflict-with-limitrange-cpu" is invalid: spec.containers[0].resources.requests: Invalid value: "700m": must be less than or equal to cpu limit
```

اگر هم `request` و هم `limit` را تنظیم کنید، آن Pod جدید حتی با وجود همان LimitRange
با موفقیت زمان‌بندی خواهد شد:

{{% code_sample file="concepts/policy/limit-range/example-no-conflict-with-limitrange-cpu.yaml" %}}

## نمونه‌هایی از محدودیت‌های منابع

نمونه‌هایی از سیاست‌هایی که می‌توان با استفاده از LimitRange ایجاد کرد عبارت‌اند از:

- در یک کلاستر ۲ نودی با ظرفیت 8 GiB RAM و ۱۶ هسته، پادهای یک
  فضای نام را محدود کنید تا 100m از CPU را با حداکثر limit برابر 500m برای CPU، و 200Mi
  از حافظه را با حداکثر limit برابر 600Mi برای حافظه درخواست کنند.
- برای کانتینرهایی که بدون request برای cpu و حافظه در مشخصاتشان آغاز می‌شوند،
  limit و request پیش‌فرض CPU را 150m و request پیش‌فرض حافظه را 300Mi تعریف کنید.

در حالتی که مجموع limitهای فضای نام کمتر از مجموع limitهای
پادها/کانتینرها باشد، ممکن است رقابت بر سر منابع رخ دهد. در این حالت،
کانتینرها یا پادها ایجاد نخواهند شد.

نه رقابت و نه تغییرات در یک LimitRange بر منابعی که از قبل ایجاد شده‌اند تأثیر نخواهند گذاشت.

## {{% heading "whatsnext" %}}

برای مثال‌هایی از استفاده از limitها، ببینید:

- [نحوهٔ پیکربندی حداقل و حداکثر محدودیت‌های CPU برای هر فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/).
- [نحوهٔ پیکربندی حداقل و حداکثر محدودیت‌های حافظه برای هر فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/).
- [نحوهٔ پیکربندی requestها و limitهای پیش‌فرض CPU برای هر فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/).
- [نحوهٔ پیکربندی requestها و limitهای پیش‌فرض حافظه برای هر فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/).
- [نحوهٔ پیکربندی حداقل و حداکثر مصرف ذخیره‌سازی برای هر فضای نام](/docs/tasks/administer-cluster/limit-storage-consumption/#limitrange-to-limit-requests-for-storage).
- یک [مثال مفصل از پیکربندی سهمیه برای هر فضای نام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/).

برای زمینه و اطلاعات تاریخی، به [سند طراحی LimitRanger](https://git.k8s.io/design-proposals-archive/resource-management/admission_control_limit_range.md)
مراجعه کنید.
