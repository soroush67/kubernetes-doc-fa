---
reviewers:
- janetkuo
title: پاک‌سازی خودکار Jobهای پایان‌یافته
content_type: concept
weight: 70
description: >-
  سازوکاری مبتنی بر طول عمر (time-to-live) برای پاک‌سازی Jobهای قدیمی که اجرایشان به پایان رسیده است.
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

هنگامی که Job شما به پایان رسید، مفید است که آن Job را در API نگه دارید (و آن را بلافاصله حذف نکنید)
تا بتوانید تشخیص دهید که Job موفق شده یا شکست خورده است.

{{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} TTL-after-finished کوبرنتیز یک
سازوکار TTL (طول عمر یا time to live) فراهم می‌کند تا طول عمر آبجکت‌های Job را که
اجرایشان به پایان رسیده است محدود کند.

<!-- body -->

## پاک‌سازی Jobهای پایان‌یافته

کنترل‌کننده TTL-after-finished تنها برای Jobها پشتیبانی می‌شود. می‌توانید از این سازوکار برای پاک‌سازی
خودکار Jobهای پایان‌یافته (چه `Complete` و چه `Failed`) با مشخص کردن
فیلد `.spec.ttlSecondsAfterFinished` یک Job استفاده کنید، همان‌طور که در این
[مثال](/docs/concepts/workloads/controllers/job/#clean-up-finished-jobs-automatically) آمده است.

کنترل‌کننده TTL-after-finished فرض می‌کند که یک Job، TTL ثانیه پس از پایان یافتن،
واجد شرایط پاک‌سازی است. زمان‌سنج از لحظه‌ای آغاز می‌شود که
وضعیت (status condition) Job تغییر کند و نشان دهد که Job یا `Complete` است یا `Failed`؛ پس از منقضی شدن TTL،
آن Job واجد شرایط حذف
[آبشاری (cascading)](/docs/concepts/architecture/garbage-collection/#cascading-deletion) می‌شود. هنگامی که
کنترل‌کننده TTL-after-finished یک Job را پاک‌سازی می‌کند، آن را به‌صورت آبشاری حذف می‌کند؛ یعنی
آبجکت‌های وابسته به آن را نیز همراه با آن حذف می‌کند.

کوبرنتیز تضمین‌های چرخه عمر آبجکت را روی Job رعایت می‌کند؛ مانند انتظار برای
[finalizerها](/docs/concepts/overview/working-with-objects/finalizers/).

می‌توانید ثانیه‌های TTL را در هر زمانی تنظیم کنید. در اینجا چند نمونه برای تنظیم
فیلد `.spec.ttlSecondsAfterFinished` یک Job آمده است:

* این فیلد را در مانیفست Job مشخص کنید تا Job بتواند مدتی پس از پایان یافتن
  به‌طور خودکار پاک‌سازی شود.
* این فیلد را برای Jobهای موجودی که پیش‌تر به پایان رسیده‌اند به‌صورت دستی تنظیم کنید تا
  واجد شرایط پاک‌سازی شوند.
* از یک
  [mutating admission webhook](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)
  برای تنظیم پویای این فیلد در زمان ایجاد Job استفاده کنید. مدیران کلاستر می‌توانند
  از این روش برای اعمال یک سیاست TTL برای Jobهای پایان‌یافته استفاده کنند.
* از یک
  [mutating admission webhook](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)
  برای تنظیم پویای این فیلد پس از پایان یافتن Job استفاده کنید و
  مقادیر TTL متفاوتی را بر اساس وضعیت Job و برچسب‌ها انتخاب کنید. در این حالت، webhook باید
  تغییرات `.status` مربوط به Job را تشخیص دهد و تنها زمانی TTL را تنظیم کند که Job
  در حال علامت‌گذاری به‌عنوان تکمیل‌شده باشد.
* کنترل‌کننده خود را بنویسید تا TTL پاک‌سازی را برای Jobهایی که با یک
  {{< glossary_tooltip term_id="selector" text="انتخابگر" >}} خاص مطابقت دارند مدیریت کند.

## ملاحظات

### به‌روزرسانی TTL برای Jobهای پایان‌یافته

می‌توانید دوره TTL، برای مثال فیلد `.spec.ttlSecondsAfterFinished` در Jobها، را
پس از ایجاد یا پایان یافتن Job تغییر دهید. اگر دوره TTL را پس از منقضی شدن
دوره `ttlSecondsAfterFinished` موجود افزایش دهید، کوبرنتیز نگهداری
آن Job را تضمین نمی‌کند، حتی اگر به‌روزرسانی برای افزایش TTL یک پاسخ موفق از API
بازگرداند.

### اختلاف زمانی (Time skew)

از آنجا که کنترل‌کننده TTL-after-finished از برچسب‌های زمانی ذخیره‌شده در Jobهای کوبرنتیز برای
تعیین منقضی شدن یا نشدن TTL استفاده می‌کند، این قابلیت به اختلاف زمانی
در کلاستر شما حساس است که ممکن است باعث شود control plane آبجکت‌های Job را
در زمان نادرست پاک‌سازی کند.

ساعت‌ها همیشه دقیق نیستند، اما اختلاف آن‌ها باید
بسیار اندک باشد. لطفاً هنگام تنظیم یک TTL غیرصفر از این خطر آگاه باشید.

## {{% heading "whatsnext" %}}

* [پاک‌سازی خودکار Jobها](/docs/concepts/workloads/controllers/job/#clean-up-finished-jobs-automatically) را بخوانید

* برای افزودن این سازوکار، به [پیشنهاد بهبود کوبرنتیز (Kubernetes Enhancement Proposal)](https://github.com/kubernetes/enhancements/blob/master/keps/sig-apps/592-ttl-after-finish/README.md)
  (KEP) مراجعه کنید.
