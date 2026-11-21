---
title: کانتینر برنامه
id: app-container
full_link:
short_description: >
  کانتینری که برای اجرای بخشی از یک بار کاری استفاده می‌شود. آن را با کانتینر init مقایسه کنید.

aka:
tags:
- workload
---
 کانتینرهای برنامه (application containers یا app containers) آن دسته از {{< glossary_tooltip text="کانتینرهای" term_id="container" >}} یک {{< glossary_tooltip text="پاد" term_id="pod" >}} هستند که پس از پایان کار همهٔ {{< glossary_tooltip text="کانتینرهای init" term_id="init-container" >}} شروع به کار می‌کنند.

<!--more-->

با کانتینر init می‌توانید جزئیات مقداردهی اولیه را جدا کنید؛ جزئیاتی که برای کل
{{< glossary_tooltip text="بار کاری" term_id="workload" >}} اهمیت دارند، اما پس از شروع کانتینر برنامه
نیازی به ادامهٔ اجرای آن‌ها نیست.
اگر برای یک پاد هیچ کانتینر init پیکربندی نشده باشد، همهٔ کانتینرهای آن پاد کانتینر برنامه هستند.
