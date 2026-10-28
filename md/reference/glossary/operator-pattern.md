---
title: الگوی اپراتور
id: operator-pattern
full_link: /docs/concepts/extend-kubernetes/operator/
short_description: >
  کنترل‌کننده‌ای تخصصی که برای مدیریت یک منبع سفارشی استفاده می‌شود

aka:
tags:
- architecture
---
[الگوی اپراتور](/docs/concepts/extend-kubernetes/operator/) طراحی سیستمی است که یک {{< glossary_tooltip term_id="controller" text="کنترل‌کننده" >}} را به یک یا چند منبع سفارشی (custom resource) متصل می‌کند.

<!--more-->

شما می‌توانید کوبرنتیز را با افزودن کنترل‌کننده‌ها به کلاستر خود، علاوه بر کنترل‌کننده‌های داخلی که بخشی از خود کوبرنتیز هستند، گسترش دهید.

اگر یک برنامه در حال اجرا نقش یک کنترل‌کننده را ایفا کند و برای انجام وظایف روی یک منبع سفارشی که در control plane تعریف شده است، به API دسترسی داشته باشد، این نمونه‌ای از الگوی اپراتور است.
