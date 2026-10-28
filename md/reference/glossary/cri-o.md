---
title: CRI-O
id: cri-o
full_link: https://cri-o.io/#what-is-cri-o
short_description: >
  یک container runtime سبک‌وزن که به‌طور ویژه برای کوبرنتیز ساخته شده است

aka:
tags:
- tool
---
ابزاری که به شما امکان می‌دهد container runtimeهای سازگار با OCI را با CRI کوبرنتیز به کار بگیرید.

<!--more-->

CRI-O پیاده‌سازی‌ای از {{< glossary_tooltip term_id="cri" >}} است
که امکان استفاده از runtimeهای {{< glossary_tooltip text="کانتینر" term_id="container" >}}
سازگار با [مشخصات runtime](https://www.github.com/opencontainers/runtime-spec)
پروژه Open Container Initiative (OCI) را فراهم می‌کند.

استقرار CRI-O به کوبرنتیز اجازه می‌دهد از هر runtime سازگار با OCI به‌عنوان container
runtime برای اجرای {{< glossary_tooltip text="Podها" term_id="pod" >}} استفاده کند و
ایمیج‌های کانتینر OCI را از registryهای راه‌دور دریافت کند.
