---
title: کانتینر Init
id: init-container
full_link: /docs/concepts/workloads/pods/init-containers/
short_description: >
  یک یا چند کانتینر مقداردهی اولیه که پیش از اجرای هر کانتینر برنامه باید تا پایان اجرا شوند.
aka: 
tags:
- fundamental
---
 یک یا چند {{< glossary_tooltip text="کانتینر" term_id="container" >}} مقداردهی اولیه (initialization) که پیش از اجرای هر کانتینر برنامه باید تا پایان اجرا شوند.

<!--more--> 

کانتینرهای مقداردهی اولیه (init) مانند کانتینرهای عادی برنامه هستند، اما یک تفاوت دارند: این کانتینرها باید پیش از آنکه هیچ کانتینر برنامه‌ای بتواند شروع به کار کند، تا پایان اجرا شوند. کانتینرهای init به‌صورت پشت‌سرهم اجرا می‌شوند؛ یعنی هر کانتینر init باید پیش از آغاز کانتینر init بعدی تا پایان اجرا شود.

برخلاف {{< glossary_tooltip text="کانتینرهای sidecar" term_id="sidecar-container" >}}، کانتینرهای init پس از راه‌اندازی Pod در حال اجرا باقی نمی‌مانند.

برای اطلاعات بیشتر، [کانتینرهای init](/docs/concepts/workloads/pods/init-containers/) را بخوانید.
