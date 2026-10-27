---
reviewers:
- mikedanese
- thockin
title: محیط کانتینر
content_type: concept
weight: 20
---

<!-- overview -->

این صفحه منابعی را که در محیط کانتینر در اختیار کانتینرها قرار دارند توصیف می‌کند.




<!-- body -->

## محیط کانتینر

محیط کانتینر کوبرنتیز چندین منبع مهم را در اختیار کانتینرها قرار می‌دهد:

* یک سیستم فایل، که ترکیبی از یک [ایمیج](/docs/concepts/containers/images/) و یک یا چند [حجم](/docs/concepts/storage/volumes/) است.
* اطلاعاتی دربارهٔ خود کانتینر.
* اطلاعاتی دربارهٔ سایر آبجکت‌های کلاستر.

### اطلاعات کانتینر

*نام میزبان* (hostname) یک کانتینر، نام Podی است که کانتینر در آن اجرا می‌شود.
این نام از طریق فرمان `hostname` یا
فراخوانی تابع [`gethostname`](https://man7.org/linux/man-pages/man2/gethostname.2.html)
در libc در دسترس است.

نام Pod و فضای نام آن به‌صورت متغیرهای محیطی از طریق
[downward API](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/) در دسترس‌اند.

متغیرهای محیطی تعریف‌شده توسط کاربر در تعریف Pod نیز در اختیار کانتینر قرار دارند،
همچنین هر متغیر محیطی که به‌صورت ایستا در ایمیج کانتینر مشخص شده باشد.

### اطلاعات کلاستر

فهرستی از همهٔ سرویس‌هایی که هنگام ایجاد یک کانتینر در حال اجرا بوده‌اند، به‌صورت متغیرهای محیطی در اختیار آن کانتینر قرار می‌گیرد.
این فهرست به سرویس‌های درون همان فضای نامِ Pod کانتینر جدید و سرویس‌های control plane کوبرنتیز محدود است.

برای سرویسی به نام *foo* که مجموعه‌ای از Podها را در اختیار می‌گذارد و هر کدام کانتینری به نام *bar* اجرا می‌کنند،
متغیرهای زیر تعریف می‌شوند:

```shell
FOO_SERVICE_HOST=<the host the service is running on>
FOO_SERVICE_PORT=<the port the service is running on>
```

سرویس‌ها نشانی‌های IP اختصاصی دارند و در صورتی که
[افزونهٔ DNS](https://releases.k8s.io/v{{< skew currentPatchVersion >}}/cluster/addons/dns/) فعال باشد، از طریق DNS در اختیار کانتینر قرار دارند.



## {{% heading "whatsnext" %}}


* دربارهٔ [hookهای چرخهٔ عمر کانتینر](/docs/concepts/containers/container-lifecycle-hooks/) بیشتر بیاموزید.
* تجربهٔ عملی
  [پیوست کردن handlerها به رویدادهای چرخهٔ عمر کانتینر](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/) را کسب کنید.
