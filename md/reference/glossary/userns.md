---
title: فضای نام کاربر (user namespace)
id: userns
full_link: https://man7.org/linux/man-pages/man7/user_namespaces.7.html
short_description: >
  قابلیتی در هسته لینوکس برای شبیه‌سازی امتیازات ابرکاربر برای کاربران بدون امتیاز.

aka:
tags:
- security
---

قابلیتی در هسته برای شبیه‌سازی کاربر root که برای «کانتینرهای بدون root» (rootless containers) استفاده می‌شود.

<!--more-->

فضاهای نام کاربر قابلیتی در هسته لینوکس هستند که به کاربر غیر root امکان می‌دهند امتیازات ابرکاربر (root) را شبیه‌سازی کند؛
برای مثال، با این کار می‌توان کانتینرها را اجرا کرد بی‌آنکه کاربر در بیرون از کانتینر ابرکاربر باشد.

فضای نام کاربر در کاهش آسیب‌های ناشی از حملات احتمالی گریز از کانتینر (container break-out) مؤثر است.

در بحث فضاهای نام کاربر، منظور از فضای نام قابلیتی در هسته لینوکس است، نه
{{< glossary_tooltip text="فضای نام" term_id="namespace" >}} به معنایی که در کوبرنتیز به کار می‌رود.

<!-- TODO: https://kinvolk.io/blog/2020/12/improving-kubernetes-and-container-security-with-user-namespaces/ -->
