---
title: CRI-O
id: cri-o
full_link: https://cri-o.io/#what-is-cri-o
short_description: >
  یک محیط اجرای کانتینر سبک که به‌طور ویژه برای کوبرنتیز طراحی شده است

aka:
tags:
- tool
---
ابزاری که امکان استفاده از محیط‌های اجرای کانتینر سازگار با OCI را همراه با CRI کوبرنتیز فراهم می‌کند.

<!--more-->

پروژهٔ CRI-O پیاده‌سازی‌ای از {{< glossary_tooltip term_id="cri" >}} است و امکان استفاده از محیط‌های اجرای {{< glossary_tooltip text="کانتینر" term_id="container" >}} را فراهم می‌کند که با [مشخصات محیط اجرا](https://www.github.com/opencontainers/runtime-spec)ی ابتکار کانتینر باز (Open Container Initiative یا OCI) سازگار هستند.

با استقرار CRI-O، کوبرنتیز می‌تواند هر محیط اجرای سازگار با OCI را به‌عنوان محیط اجرای کانتینر برای اجرای {{< glossary_tooltip text="پادها" term_id="pod" >}} به کار گیرد و ایمیج‌های کانتینر OCI را از رجیستری‌های راه دور دریافت کند.
