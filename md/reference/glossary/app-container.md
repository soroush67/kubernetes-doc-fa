---
title: کانتینر برنامه
id: app-container
full_link:
short_description: >
  کانتینری که برای اجرای بخشی از یک بار کاری استفاده می‌شود. با init container مقایسه کنید.

aka:
tags:
- workload
---
 کانتینرهای برنامه (یا app containerها) {{< glossary_tooltip text="کانتینرهایی" term_id="container" >}} در یک {{< glossary_tooltip text="pod" term_id="pod" >}} هستند که پس از تکمیل اجرای تمام {{< glossary_tooltip text="init containerها" term_id="init-container" >}} آغاز می‌شوند.

<!--more-->

init container به شما امکان می‌دهد جزئیات مربوط به مقداردهی اولیه را که برای کل
{{< glossary_tooltip text="بار کاری" term_id="workload" >}} اهمیت دارند و پس از شروع به کار کانتینر برنامه نیازی به ادامه‌ی اجرای آن‌ها نیست، جدا کنید.
اگر برای یک pod هیچ init containerای پیکربندی نشده باشد، تمام کانتینرهای آن pod کانتینر برنامه هستند.
