---
title: DeviceClass
id: deviceclass
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#deviceclass
short_description: >
  دسته‌ای از دستگاه‌ها در کلاستر. کاربران می‌توانند دستگاه‌های مشخصی را در یک DeviceClass درخواست (claim) کنند.
tags:
- extension
---
 دسته‌ای از {{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}} در کلاستر که می‌توان آن‌ها را همراه با تخصیص پویای منابع (DRA) به کار برد.

<!--more-->

مدیران یا مالکان دستگاه‌ها از DeviceClassها برای تعریف مجموعه‌ای از دستگاه‌ها استفاده می‌کنند که می‌توان آن‌ها را درخواست (claim) کرد و در بارهای کاری به کار گرفت. دستگاه‌ها با ایجاد {{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} درخواست می‌شوند؛ این ResourceClaimها بر اساس پارامترهای مشخص دستگاه در یک DeviceClass فیلتر می‌کنند.

برای اطلاعات بیشتر، به
[تخصیص پویای منابع (Dynamic Resource Allocation)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#deviceclass)
مراجعه کنید.
