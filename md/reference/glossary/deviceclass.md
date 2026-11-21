---
title: DeviceClass
id: deviceclass
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#deviceclass
short_description: >
  دسته‌ای از دستگاه‌ها در کلاستر. کاربران می‌توانند دستگاه‌های مشخصی را
  در یک DeviceClass درخواست کنند.
tags:
- extension
---
 دسته‌ای از {{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}} در
 کلاستر که می‌توان از آن‌ها در تخصیص پویای منابع (Dynamic Resource Allocation یا DRA) استفاده کرد.

<!--more-->

مدیران کلاستر یا مالکان دستگاه‌ها با استفاده از DeviceClassها مجموعه‌ای از
دستگاه‌ها را تعریف می‌کنند که می‌توان آن‌ها را درخواست کرد و در بارهای کاری به کار برد.
برای درخواست دستگاه‌ها باید
{{< glossary_tooltip text="ResourceClaimهایی" term_id="resourceclaim" >}}
ایجاد کرد که دستگاه‌ها را بر اساس پارامترهای مشخصی در یک DeviceClass فیلتر می‌کنند.

برای اطلاعات بیشتر، به
[تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#deviceclass)
مراجعه کنید.
