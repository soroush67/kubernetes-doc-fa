---
title: کنترل‌کننده
id: controller
full_link: /docs/concepts/architecture/controller/
short_description: >
  یک حلقه کنترل که وضعیت مشترک کلاستر را از طریق apiserver زیر نظر می‌گیرد و تغییراتی اعمال می‌کند تا وضعیت فعلی را به وضعیت مطلوب نزدیک‌تر کند.

aka: 
tags:
- architecture
- fundamental
---
در کوبرنتیز، کنترل‌کننده‌ها حلقه‌های کنترلی هستند که وضعیت
{{< glossary_tooltip term_id="cluster" text="کلاستر">}} شما را زیر نظر می‌گیرند و سپس در صورت نیاز تغییرات را اعمال یا درخواست می‌کنند.
هر کنترل‌کننده تلاش می‌کند وضعیت فعلی کلاستر را به وضعیت مطلوب نزدیک‌تر کند.

<!--more-->

کنترل‌کننده‌ها وضعیت مشترک کلاستر شما را از طریق
{{< glossary_tooltip text="apiserver" term_id="kube-apiserver" >}} (بخشی از
{{< glossary_tooltip term_id="control-plane" >}}) زیر نظر می‌گیرند.

برخی کنترل‌کننده‌ها نیز درون control plane اجرا می‌شوند و حلقه‌های کنترلی‌ای فراهم می‌کنند که برای عملکرد کوبرنتیز اساسی هستند. برای مثال: کنترل‌کننده deployment، کنترل‌کننده daemonset، کنترل‌کننده namespace و کنترل‌کننده persistent volume (و موارد دیگر) همگی درون
{{< glossary_tooltip term_id="kube-controller-manager" >}} اجرا می‌شوند.
