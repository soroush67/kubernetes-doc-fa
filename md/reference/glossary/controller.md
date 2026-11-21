---
title: کنترل‌کننده
id: controller
full_link: /docs/concepts/architecture/controller/
short_description: >
  حلقهٔ کنترلی که وضعیت مشترک کلاستر را از طریق apiserver زیر نظر می‌گیرد و با اعمال تغییرات می‌کوشد وضعیت فعلی را به وضعیت مطلوب نزدیک کند.

aka: 
tags:
- architecture
- fundamental
---
در کوبرنتیز، کنترل‌کننده‌ها (controllers) حلقه‌های کنترلی هستند که وضعیت
{{< glossary_tooltip term_id="cluster" text="کلاستر">}} شما را زیر نظر می‌گیرند و
سپس در صورت نیاز تغییراتی را اعمال یا درخواست می‌کنند.
هر کنترل‌کننده می‌کوشد وضعیت فعلی کلاستر را به وضعیت مطلوب نزدیک‌تر کند.

<!--more-->

کنترل‌کننده‌ها وضعیت مشترک کلاستر شما را از طریق
{{< glossary_tooltip text="apiserver" term_id="kube-apiserver" >}} (بخشی از
{{< glossary_tooltip term_id="control-plane" >}}) زیر نظر می‌گیرند.

برخی از کنترل‌کننده‌ها نیز درون control plane اجرا می‌شوند و حلقه‌های کنترلی‌ای را
فراهم می‌کنند که برای عملیات کوبرنتیز حیاتی هستند. برای نمونه، کنترل‌کنندهٔ
Deployment، کنترل‌کنندهٔ DaemonSet، کنترل‌کنندهٔ فضای نام (namespace) و کنترل‌کنندهٔ
حجم پایدار (persistent volume) (و موارد دیگر) همگی درون
{{< glossary_tooltip term_id="kube-controller-manager" >}} اجرا می‌شوند.
