---
title: Object
id: object
full_link: /docs/concepts/overview/working-with-objects/#kubernetes-objects
short_description: >
   موجودیتی در سیستم کوبرنتیز که بخشی از وضعیت کلاستر شما را نمایش می‌دهد.
aka:
tags:
- architecture
- fundamental
---
موجودیتی در سیستم کوبرنتیز. آبجکت یک
{{< glossary_tooltip text="منبع API" term_id="api-resource" >}} است که API کوبرنتیز
از آن برای نمایش وضعیت کلاستر شما استفاده می‌کند.
<!--more-->
آبجکت کوبرنتیز معمولاً یک «رکورد قصد و نیت» (record of intent) است؛ به محض اینکه آبجکت را ایجاد کنید،
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز پیوسته تلاش می‌کند تا
اطمینان حاصل کند که مورد نمایش‌داده‌شده توسط آن واقعاً وجود دارد.
با ایجاد یک آبجکت، در عمل به سیستم کوبرنتیز اعلام می‌کنید که می‌خواهید بخشی از بار کاری کلاستر شما
چه شکلی داشته باشد؛ این همان وضعیت مطلوب (desired state) کلاستر شماست.
