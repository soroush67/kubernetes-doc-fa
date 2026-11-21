---
title: ServiceAccount
id: service-account
full_link: /docs/tasks/configure-pod-container/configure-service-account/
short_description: >
  یک هویت برای فرایندهایی فراهم می‌کند که در یک Pod اجرا می‌شوند.

aka: 
tags:
- fundamental
- core-object
---
 یک هویت برای فرایندهایی فراهم می‌کند که در یک {{< glossary_tooltip text="Pod" term_id="pod" >}} اجرا می‌شوند.

<!--more--> 

هنگامی که فرایندهای درون Podها به کلاستر دسترسی پیدا می‌کنند، API server آن‌ها را در قالب یک حساب سرویس (service account) مشخص، مثلاً `default`، احراز هویت می‌کند. اگر هنگام ایجاد یک Pod حساب سرویسی برای آن تعیین نکنید، حساب سرویس پیش‌فرضِ همان {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} به‌طور خودکار به آن اختصاص داده می‌شود.
