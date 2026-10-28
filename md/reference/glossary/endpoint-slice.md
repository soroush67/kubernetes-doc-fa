---
title: EndpointSlice
id: endpoint-slice
full_link: /docs/concepts/services-networking/endpoint-slices/
short_description: >
  EndpointSliceها آدرس‌های IP مربوط به Podها را برای Serviceها ردیابی می‌کنند.

aka:
tags:
- networking
---
EndpointSliceها آدرس‌های IP نقاط پایانی (endpoint) پشتیبان را ردیابی می‌کنند.
EndpointSliceها معمولاً به یک
{{< glossary_tooltip text="Service" term_id="service" >}} مرتبط هستند و نقاط پایانی پشتیبان معمولاً نمایانگر
{{< glossary_tooltip text="Podها" term_id="pod" >}} هستند.

<!--more-->
یک Service می‌تواند توسط چندین Pod پشتیبانی شود. کوبرنتیز نقاط پایانی پشتیبان یک Service را
با مجموعه‌ای از EndpointSliceها که با آن Service مرتبط هستند نمایش می‌دهد.
نقاط پایانی پشتیبان معمولاً، اما نه همیشه، Podهایی هستند که در کلاستر اجرا می‌شوند.

control plane معمولاً EndpointSliceها را به‌طور خودکار برای شما مدیریت می‌کند. با این حال،
EndpointSliceها را می‌توان برای {{< glossary_tooltip text="Serviceهایی" term_id="service" >}} که
{{< glossary_tooltip text="انتخابگر (selector)" term_id="selector" >}} برایشان تعیین نشده است، به‌صورت دستی تعریف کرد.
