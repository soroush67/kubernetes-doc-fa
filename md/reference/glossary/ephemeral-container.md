---
title: کانتینر موقت
id: ephemeral-container
full_link: /docs/concepts/workloads/pods/ephemeral-containers/
short_description: >
  نوعی کانتینر که می‌توانید آن را به‌طور موقت درون یک Pod اجرا کنید.

aka:
tags:
- fundamental
---
نوعی {{< glossary_tooltip term_id="container" >}} که می‌توانید آن را به‌طور موقت درون یک {{< glossary_tooltip term_id="pod" >}} اجرا کنید.

<!--more-->

اگر بخواهید Podی را که در حال اجراست و با مشکل روبه‌رو شده بررسی کنید، می‌توانید یک کانتینر موقت (ephemeral container) به آن Pod اضافه کنید و عیب‌یابی را انجام دهید.
کانتینرهای موقت هیچ تضمینی از نظر {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} یا زمان‌بندی ندارند و نباید از آن‌ها برای اجرای هیچ بخشی از خودِ بار کاری استفاده کنید.

{{< glossary_tooltip text="Podهای ایستا" term_id="static-pod" >}} از کانتینرهای موقت پشتیبانی نمی‌کنند.
