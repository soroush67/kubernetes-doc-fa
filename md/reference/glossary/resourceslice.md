---
title: ResourceSlice
id: resourceslice
full_link: /docs/reference/kubernetes-api/resource/resource-slice-v1/
short_description: >
  یک یا چند منبع زیرساختی، مانند دستگاه‌ها، را در مجموعه‌ای (pool) از منابع مشابه نشان می‌دهد.

tags:
- workload
---
 هر ResourceSlice نمایانگر یک یا چند منبع زیرساختی، مانند
{{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}}، است که به نودها متصل‌اند.
درایورها ResourceSliceها را در کلاستر ایجاد و مدیریت می‌کنند. از ResourceSliceها برای
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
استفاده می‌شود.

<!--more-->

هنگامی که یک {{< glossary_tooltip text="ResourceClaim" term_id="resourceclaim" >}}
ایجاد می‌شود، کوبرنتیز با استفاده از ResourceSliceها نودهایی را پیدا می‌کند که به منابعی
با قابلیت برآورده‌کردن آن درخواست دسترسی دارند. سپس کوبرنتیز منابع را به آن ResourceClaim
تخصیص می‌دهد و Pod را روی نودی زمان‌بندی می‌کند که به آن منابع دسترسی دارد.
