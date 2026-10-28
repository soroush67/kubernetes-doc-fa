---
title: فضای نام کاربر
id: userns
full_link: https://man7.org/linux/man-pages/man7/user_namespaces.7.html
short_description: >
  یک قابلیت هسته لینوکس برای شبیه‌سازی دسترسی‌های کاربر ریشه (superuser) برای کاربران بدون دسترسی ویژه.

aka:
tags:
- security
---

یک قابلیت هسته برای شبیه‌سازی کاربر root که برای «کانتینرهای بدون root» (rootless containers) استفاده می‌شود.

<!--more-->

فضای نام کاربر (user namespace) یک قابلیت هسته لینوکس است که به کاربر غیر root اجازه می‌دهد دسترسی‌های کاربر ریشه («root») را شبیه‌سازی کند؛
برای مثال، به‌منظور اجرای کانتینرها بدون آنکه کاربر در بیرون از کانتینر دارای دسترسی superuser باشد.

فضای نام کاربر در کاهش خسارت ناشی از حملات احتمالی فرار از کانتینر (container break-out) مؤثر است.

در زمینه فضاهای نام کاربر، این فضای نام یک قابلیت هسته لینوکس است و نه یک
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} به معنایی که در کوبرنتیز به کار می‌رود.

<!-- TODO: https://kinvolk.io/blog/2020/12/improving-kubernetes-and-container-security-with-user-namespaces/ -->
