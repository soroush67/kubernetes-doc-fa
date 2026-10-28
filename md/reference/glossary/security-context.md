---
title: زمینه امنیتی (Security Context)
id: security-context
full_link: /docs/tasks/configure-pod-container/security-context/
short_description: >
  فیلد securityContext تنظیمات سطح دسترسی و کنترل دسترسی را برای یک Pod یا کانتینر تعریف می‌کند.

aka: 
tags:
- security
---
 فیلد `securityContext` تنظیمات سطح دسترسی و کنترل دسترسی را برای یک
{{< glossary_tooltip text="Pod" term_id="pod" >}}
یا {{< glossary_tooltip text="کانتینر" term_id="container" >}} تعریف می‌کند.

<!--more-->

در یک `securityContext` می‌توانید کاربری که فرایندها با آن اجرا می‌شوند، گروهی که فرایندها با آن اجرا می‌شوند و تنظیمات سطح دسترسی را تعریف کنید.
همچنین می‌توانید سیاست‌های امنیتی (برای مثال: SELinux، AppArmor یا seccomp) را پیکربندی کنید.

تنظیم `PodSpec.securityContext` بر همه کانتینرهای یک Pod اعمال می‌شود.
