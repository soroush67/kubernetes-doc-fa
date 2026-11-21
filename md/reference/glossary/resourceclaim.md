---
title: ResourceClaim
id: resourceclaim
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceclaims-templates
short_description: >
  منابعی را که یک بار کاری به آن‌ها نیاز دارد، مانند دستگاه‌ها، توصیف می‌کند. هر ResourceClaim
  می‌تواند دستگاه‌هایی را از DeviceClassها درخواست کند.

tags:
- workload
---
 منابعی را که یک بار کاری به آن‌ها نیاز دارد، مانند
{{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}}، توصیف می‌کند. از ResourceClaimها
در
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
استفاده می‌شود تا Podها به یک منبع مشخص دسترسی پیدا کنند.

<!--more-->

هر ResourceClaim را می‌توان به دو روش ایجاد کرد: اپراتورهای بار کاری آن را می‌سازند یا کوبرنتیز آن را
بر اساس یک
{{< glossary_tooltip text="ResourceClaimTemplate" term_id="resourceclaimtemplate" >}} تولید می‌کند.
