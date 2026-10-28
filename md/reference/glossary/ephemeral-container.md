---
title: Ephemeral Container
id: ephemeral-container
full_link: /docs/concepts/workloads/pods/ephemeral-containers/
short_description: >
  نوعی کانتینر که می‌توانید آن را به‌صورت موقت درون یک Pod اجرا کنید.

aka:
tags:
- fundamental
---
نوعی {{< glossary_tooltip term_id="container" text="کانتینر" >}} که می‌توانید آن را به‌صورت موقت درون یک {{< glossary_tooltip term_id="pod" >}} اجرا کنید.

<!--more-->

اگر می‌خواهید Podی را که با مشکل در حال اجراست بررسی کنید، می‌توانید یک ephemeral container به آن Pod اضافه کنید و عیب‌یابی را انجام دهید.
ephemeral containerها هیچ تضمینی درباره {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} یا زمان‌بندی ندارند،
و نباید از آن‌ها برای اجرای هیچ بخشی از خود بار کاری استفاده کنید.

ephemeral containerها توسط {{< glossary_tooltip text="Podهای استاتیک" term_id="static-pod" >}} پشتیبانی نمی‌شوند.
