---
title: ServiceAccount
id: service-account
full_link: /docs/tasks/configure-pod-container/configure-service-account/
short_description: >
  یک هویت برای فرایندهایی فراهم می‌کند که درون یک Pod اجرا می‌شوند.

aka: 
tags:
- fundamental
- core-object
---
 یک هویت برای فرایندهایی فراهم می‌کند که درون یک {{< glossary_tooltip text="Pod" term_id="pod" >}} اجرا می‌شوند.

<!--more--> 

هنگامی که فرایندهای درون Podها به کلاستر دسترسی پیدا می‌کنند، API server آن‌ها را به‌عنوان یک service account مشخص، برای مثال `default`، احراز هویت می‌کند. هنگامی که یک Pod ایجاد می‌کنید، اگر service account را مشخص نکنید، service account پیش‌فرض (default) در همان {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} به‌طور خودکار به آن اختصاص داده می‌شود.
