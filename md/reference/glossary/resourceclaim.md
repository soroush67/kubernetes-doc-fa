---
title: ResourceClaim
id: resourceclaim
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceclaims-templates
short_description: >
  منابعی را که یک بار کاری به آن‌ها نیاز دارد، مانند دستگاه‌ها، توصیف می‌کند. ResourceClaimها
  می‌توانند دستگاه‌ها را از DeviceClassها درخواست کنند.

tags:
- workload
---
 منابعی را که یک بار کاری به آن‌ها نیاز دارد، مانند
{{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}}، توصیف می‌کند. ResourceClaimها
در
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
برای فراهم کردن دسترسی Podها به یک منبع مشخص استفاده می‌شوند.

<!--more-->

ResourceClaimها را می‌توان اپراتورهای بار کاری ایجاد کنند یا کوبرنتیز آن‌ها را
بر اساس یک
{{< glossary_tooltip text="ResourceClaimTemplate" term_id="resourceclaimtemplate" >}}
تولید کند.
