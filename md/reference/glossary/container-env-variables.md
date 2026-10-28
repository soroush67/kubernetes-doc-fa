---
title: متغیرهای محیطی کانتینر
id: container-env-variables
full_link: /docs/concepts/containers/container-environment/
short_description: >
  متغیرهای محیطی کانتینر جفت‌های name=value هستند که اطلاعات مفیدی را به کانتینرهای در حال اجرا در یک Pod ارائه می‌دهند.

aka: 
tags:
- fundamental
---
 متغیرهای محیطی کانتینر جفت‌های name=value هستند که اطلاعات مفیدی را به کانتینرهای در حال اجرا در یک {{< glossary_tooltip text="Pod" term_id="pod" >}} ارائه می‌دهند.

<!--more-->

متغیرهای محیطی کانتینر اطلاعاتی را که برنامه‌های کانتینری‌شده در حال اجرا به آن نیاز دارند، همراه با اطلاعاتی درباره جزئیات مهم مرتبط با {{< glossary_tooltip text="کانتینرها" term_id="container" >}} فراهم می‌کنند. برای مثال، جزئیات سیستم فایل، اطلاعات مربوط به خود کانتینر و سایر منابع کلاستر مانند endpointهای سرویس.
