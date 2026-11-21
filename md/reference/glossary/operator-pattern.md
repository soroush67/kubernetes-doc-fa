---
title: الگوی اپراتور
id: operator-pattern
full_link: /docs/concepts/extend-kubernetes/operator/
short_description: >
  یک کنترل‌کنندهٔ تخصصی که برای مدیریت یک منبع سفارشی استفاده می‌شود

aka:
tags:
- architecture
---
[الگوی اپراتور](/docs/concepts/extend-kubernetes/operator/) (operator pattern) نوعی طراحی سیستم است که یک {{< glossary_tooltip term_id="controller" >}} را به یک یا چند منبع سفارشی (custom resource) پیوند می‌دهد.

<!--more-->

می‌توانید علاوه بر کنترل‌کننده‌های داخلی که بخشی از خود کوبرنتیز هستند، کنترل‌کننده‌های دیگری به کلاستر خود اضافه کنید و به این ترتیب کوبرنتیز را گسترش دهید.

اگر یک برنامهٔ در حال اجرا نقش کنترل‌کننده را ایفا کند و برای انجام وظایفی روی یک منبع سفارشیِ تعریف‌شده در control plane به API دسترسی داشته باشد، نمونه‌ای از الگوی اپراتور است.
