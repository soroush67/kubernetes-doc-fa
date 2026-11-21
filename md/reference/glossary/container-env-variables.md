---
title: متغیرهای محیطی کانتینر
id: container-env-variables
full_link: /docs/concepts/containers/container-environment/
short_description: >
  متغیرهای محیطی کانتینر جفت‌های name=value هستند که اطلاعات مفیدی را در اختیار کانتینرهای در حال اجرا در یک Pod قرار می‌دهند.

aka: 
tags:
- fundamental
---
 متغیرهای محیطی کانتینر (container environment variables) جفت‌های name=value هستند که اطلاعات مفیدی را در اختیار کانتینرهای در حال اجرا در یک {{< glossary_tooltip text="پاد" term_id="pod" >}} قرار می‌دهند.

<!--more-->

متغیرهای محیطی کانتینر اطلاعاتی را فراهم می‌کنند که برنامه‌های کانتینری‌شدهٔ در حال اجرا به آن‌ها نیاز دارند. این متغیرها همچنین جزئیات مهم مرتبط با {{< glossary_tooltip text="کانتینرها" term_id="container" >}} را در اختیار برنامه‌ها می‌گذارند؛ برای نمونه، جزئیات سامانهٔ فایل، اطلاعاتی دربارهٔ خود کانتینر و دیگر منابع کلاستر مانند endpointهای سرویس.
