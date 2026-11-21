---
title: LimitRange
id: limitrange
full_link:  /docs/concepts/policy/limit-range/
short_description: >
  محدودیت‌هایی برای محدودکردن مصرف منابع به‌ازای هر کانتینر یا Pod در یک فضای نام فراهم می‌کند.

aka: 
tags:
- core-object
- fundamental
- architecture
related:
 - pod
 - container

---
مصرف منابع را به‌ازای هر {{< glossary_tooltip text="کانتینر" term_id="container" >}} یا {{< glossary_tooltip text="Pod" term_id="pod" >}}
در یک {{< glossary_tooltip text="فضای نام (namespace)" term_id="namespace" >}} مشخص محدود می‌کند.

<!--more--> 

هر [LimitRange](/docs/concepts/policy/limit-range/) یا تعداد {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} قابل ایجاد را
(برای یک نوع منبع خاص) محدود می‌کند، یا میزان {{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}}
را که هر کانتینر یا Pod در یک فضای نام می‌تواند درخواست یا مصرف کند.
