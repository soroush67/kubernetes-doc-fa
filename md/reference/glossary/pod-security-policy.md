---
title: سیاست امنیتی Pod
id: pod-security-policy
full_link: /docs/concepts/security/pod-security-policy/
short_description: >
  یک API حذف‌شده که محدودیت‌های امنیتی Pod را اعمال می‌کرد.
aka: 
tags:
- security
---
یکی از APIهای پیشین کوبرنتیز که هنگام ایجاد و به‌روزرسانی {{< glossary_tooltip term_id="pod" >}} محدودیت‌های امنیتی را اعمال می‌کرد.

<!--more--> 

منبع PodSecurityPolicy از نسخهٔ v1.21 کوبرنتیز منسوخ (deprecated) شد و در نسخهٔ v1.25 حذف شد.
به‌جای آن، از [پذیرش امنیتی Pod (Pod Security Admission)](/docs/concepts/security/pod-security-admission/) یا یک افزونهٔ پذیرش (admission plugin) شخص ثالث استفاده کنید.
