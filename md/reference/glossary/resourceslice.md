---
title: ResourceSlice
id: resourceslice
full_link: /docs/reference/kubernetes-api/resource/resource-slice-v1/
short_description: >
  یک یا چند منبع زیرساختی، مانند دستگاه‌ها، را در یک مخزن از منابع مشابه نمایش می‌دهد.

tags:
- workload
---
 یک یا چند منبع زیرساختی، مانند
{{< glossary_tooltip text="دستگاه‌ها" term_id="device" >}}،
را که به نودها متصل هستند نمایش می‌دهد. درایورها ResourceSliceها را در کلاستر ایجاد و مدیریت می‌کنند. ResourceSliceها برای
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
استفاده می‌شوند.

<!--more-->

هنگامی که یک {{< glossary_tooltip text="ResourceClaim" term_id="resourceclaim" >}} ایجاد می‌شود، کوبرنتیز از ResourceSliceها برای یافتن نودهایی استفاده می‌کند که به منابعِ قادر به برآوردن آن درخواست دسترسی دارند. کوبرنتیز منابع را به ResourceClaim تخصیص می‌دهد و Pod را روی نودی زمان‌بندی می‌کند که به آن منابع دسترسی داشته باشد.
