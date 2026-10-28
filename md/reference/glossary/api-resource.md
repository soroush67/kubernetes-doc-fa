---
title: منبع API
id: api-resource
full_link: /docs/reference/using-api/api-concepts/#standard-api-terminology
short_description: >
  یک موجودیت کوبرنتیز که نمایانگر یک endpoint روی سرور API کوبرنتیز است.

aka:
 - Resource
tags:
- architecture
---
یک موجودیت در سیستم نوع (type system) کوبرنتیز که با یک endpoint روی {{< glossary_tooltip text="API کوبرنتیز" term_id="kubernetes-api" >}} متناظر است.
یک منبع معمولاً نمایانگر یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} است.
برخی منابع نمایانگر یک عملیات روی آبجکت‌های دیگر هستند، مانند بررسی مجوز دسترسی.
<!--more-->
هر منبع نمایانگر یک endpoint از نوع HTTP (یا همان URI) روی سرور API کوبرنتیز است و طرحواره (schema) آبجکت‌ها یا عملیات مربوط به آن منبع را تعریف می‌کند.
