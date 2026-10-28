---
title: کنترل‌کننده پذیرش
id: admission-controller
full_link: /docs/reference/access-authn-authz/admission-controllers/
short_description: >
  قطعه‌ای از کد که درخواست‌های ارسالی به API server کوبرنتیز را پیش از ذخیره‌سازی (persistence) آبجکت رهگیری می‌کند.

aka:
tags:
- extension
- security
---
قطعه‌ای از کد که درخواست‌های ارسالی به API server کوبرنتیز را پیش از ذخیره‌سازی (persistence) آبجکت رهگیری می‌کند.

<!--more-->

کنترل‌کننده‌های پذیرش (Admission controllers) برای API server کوبرنتیز قابل پیکربندی هستند و می‌توانند از نوع «اعتبارسنجی» (validating)، «تغییردهنده» (mutating) یا هر دو باشند. هر کنترل‌کننده پذیرش می‌تواند درخواست را رد کند. کنترل‌کننده‌های تغییردهنده می‌توانند آبجکت‌هایی را که می‌پذیرند تغییر دهند؛ اما کنترل‌کننده‌های اعتبارسنجی چنین امکانی ندارند.

* [کنترل‌کننده‌های پذیرش در مستندات کوبرنتیز](/docs/reference/access-authn-authz/admission-controllers/)
