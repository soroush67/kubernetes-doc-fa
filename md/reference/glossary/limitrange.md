---
title: LimitRange
id: limitrange
full_link:  /docs/concepts/policy/limit-range/
short_description: >
  محدودیت‌هایی برای کنترل مصرف منابع در هر کانتینر یا Pod در یک فضای نام (namespace) فراهم می‌کند.

aka: 
tags:
- core-object
- fundamental
- architecture
related:
 - pod
 - container

---
مصرف منابع را به ازای هر {{< glossary_tooltip text="کانتینر" term_id="container" >}} یا {{< glossary_tooltip text="Pod" term_id="pod" >}} محدود می‌کند؛ این محدودیت‌ها برای یک {{< glossary_tooltip text="فضای نام (namespace)" term_id="namespace" >}} مشخص تعریف می‌شوند.

<!--more--> 

یک [LimitRange](/docs/concepts/policy/limit-range/) یا تعداد {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} قابل ایجاد (برای یک نوع منبع مشخص) را محدود می‌کند،
یا مقدار {{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}} را که کانتینرها یا Podهای منفرد در یک فضای نام می‌توانند درخواست یا مصرف کنند، محدود می‌سازد.
