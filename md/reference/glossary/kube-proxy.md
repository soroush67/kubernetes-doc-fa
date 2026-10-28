---
title: kube-proxy
id: kube-proxy
full_link: /docs/reference/command-line-tools-reference/kube-proxy/
short_description: >
  `kube-proxy` یک پراکسی شبکه است که روی هر نود در کلاستر اجرا می‌شود.

aka:
tags:
- fundamental
- networking
---
 kube-proxy یک پراکسی شبکه است که روی هر
{{< glossary_tooltip text="نود" term_id="node" >}} در کلاستر شما اجرا می‌شود
و بخشی از مفهوم {{< glossary_tooltip term_id="service">}} در کوبرنتیز را پیاده‌سازی می‌کند.

<!--more-->

[kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
قواعد شبکه را روی نودها مدیریت و نگهداری می‌کند. این قواعد شبکه امکان برقراری
ارتباط شبکه‌ای با Podهای شما را از طریق نشست‌های شبکه‌ای درون یا بیرون
کلاستر فراهم می‌کنند.

اگر لایه فیلتر کردن بسته‌ها (packet filtering) در سیستم‌عامل وجود داشته باشد و در دسترس باشد،
kube-proxy از آن استفاده می‌کند. در غیر این صورت، kube-proxy خودش ترافیک را هدایت (forward) می‌کند.
