---
title: kube-proxy
id: kube-proxy
full_link: /docs/reference/command-line-tools-reference/kube-proxy/
short_description: >
  مؤلفه‌ی `kube-proxy` یک پروکسی شبکه است که روی هر نود کلاستر اجرا می‌شود.

aka:
tags:
- fundamental
- networking
---
 مؤلفه‌ی kube-proxy یک پروکسی شبکه است که روی هر
{{< glossary_tooltip text="نود" term_id="node" >}} در کلاستر شما اجرا می‌شود
و بخشی از مفهوم {{< glossary_tooltip term_id="service">}} در کوبرنتیز را
پیاده‌سازی می‌کند.

<!--more-->

مؤلفه‌ی [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
قوانین شبکه (network rules) را روی نودها نگهداری می‌کند. این قوانین امکان
برقراری ارتباط شبکه‌ای با Podهای شما را از نشست‌های شبکه‌ای داخل یا خارج از
کلاستر فراهم می‌کنند.

اگر سیستم‌عامل لایه‌ی فیلتر بسته‌ها (packet filtering) داشته باشد و این لایه در
دسترس باشد، kube-proxy از آن استفاده می‌کند. در غیر این صورت، kube-proxy خودش
ترافیک را هدایت می‌کند.
