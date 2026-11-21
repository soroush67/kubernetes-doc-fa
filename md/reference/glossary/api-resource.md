---
title: منبع API
id: api-resource
full_link: /docs/reference/using-api/api-concepts/#standard-api-terminology
short_description: >
  موجودیتی در کوبرنتیز که نماینده‌ی یک نقطه‌ی پایانی (endpoint) روی سرور API کوبرنتیز است.

aka:
 - Resource
tags:
- architecture
---
منبع، موجودیتی در سامانه‌ی نوع‌های کوبرنتیز است که با یک نقطه‌ی پایانی (endpoint) روی {{< glossary_tooltip text="API کوبرنتیز" term_id="kubernetes-api" >}} متناظر است.
هر منبع معمولاً نماینده‌ی یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} است.
برخی منابع نیز نماینده‌ی عملیاتی روی آبجکت‌های دیگر هستند؛ برای نمونه، بررسی مجوز.
<!--more-->
هر منبع نماینده‌ی یک نقطه‌ی پایانی HTTP (URI) روی سرور API کوبرنتیز است و طرح‌واره‌ی (schema) آبجکت‌ها یا عملیات مربوط به آن منبع را تعریف می‌کند.
