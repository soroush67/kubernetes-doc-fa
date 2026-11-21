---
title: EndpointSlice
id: endpoint-slice
full_link: /docs/concepts/services-networking/endpoint-slices/
short_description: >
  آبجکت‌های EndpointSlice نشانی‌های IP پادها را برای Serviceها ردیابی می‌کنند.

aka:
tags:
- networking
---
آبجکت‌های EndpointSlice نشانی‌های IP نقطه‌های پایانی (endpoint) بک‌اند را ردیابی می‌کنند.
این آبجکت‌ها معمولاً با یک
{{< glossary_tooltip text="Service" term_id="service" >}} مرتبط هستند و نقطه‌های پایانی بک‌اند معمولاً نمایانگر
{{< glossary_tooltip text="پادها" term_id="pod" >}} هستند.

<!--more-->
یک Service می‌تواند چندین Pod پشتیبان داشته باشد. کوبرنتیز نقطه‌های پایانی پشتیبان یک Service را
با مجموعه‌ای از EndpointSliceهای مرتبط با همان Service نمایش می‌دهد.
این نقطه‌های پایانی پشتیبان معمولاً، اما نه همیشه، پادهایی هستند که در کلاستر اجرا می‌شوند.

معمولاً control plane آبجکت‌های EndpointSlice را به‌صورت خودکار برای شما مدیریت می‌کند. با این حال،
می‌توان EndpointSliceها را برای {{< glossary_tooltip text="Serviceهایی" term_id="service" >}} که برای آن‌ها هیچ
{{< glossary_tooltip text="انتخابگری (selector)" term_id="selector" >}} مشخص نشده است، به‌صورت دستی تعریف کرد.
