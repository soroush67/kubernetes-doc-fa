---
title: آبجکت
id: object
full_link: /docs/concepts/overview/working-with-objects/#kubernetes-objects
short_description: >
   موجودیتی در سیستم کوبرنتیز که بخشی از وضعیت کلاستر شما را نمایش می‌دهد.
aka:
tags:
- architecture
- fundamental
---
آبجکت موجودیتی در سیستم کوبرنتیز است. هر آبجکت یک
{{< glossary_tooltip text="منبع API" term_id="api-resource" >}} است که API کوبرنتیز
از آن برای نمایش وضعیت کلاستر شما استفاده می‌کند.
<!--more-->
هر آبجکت کوبرنتیز معمولاً یک «سابقهٔ نیت» (record of intent) است؛ یعنی پس از آنکه آبجکت را ایجاد کردید،
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز پیوسته تلاش می‌کند تا اطمینان یابد
چیزی که آن آبجکت نمایش می‌دهد واقعاً وجود دارد.
با ایجاد یک آبجکت، در واقع به سیستم کوبرنتیز می‌گویید که می‌خواهید آن بخش از
بار کاری کلاسترتان چگونه باشد؛ این همان وضعیت مطلوب (desired state) کلاستر شماست.
