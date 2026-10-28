---
title: Garbage Collection
id: garbage-collection
full_link: /docs/concepts/architecture/garbage-collection/
short_description: >
  اصطلاحی جمعی برای سازوکارهای مختلفی که کوبرنتیز برای پاک‌سازی منابع کلاستر به کار می‌گیرد.

aka: 
tags:
- fundamental
- operation
---

جمع‌آوری زباله (Garbage Collection) اصطلاحی جمعی برای سازوکارهای مختلفی است که کوبرنتیز برای پاک‌سازی
منابع کلاستر از آن‌ها استفاده می‌کند.

<!--more-->

کوبرنتیز از جمع‌آوری زباله برای پاک‌سازی منابعی مانند
[کانتینرها و ایمیج‌های استفاده‌نشده](/docs/concepts/architecture/garbage-collection/#containers-images)،
[Podهای ناموفق](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)،
[آبجکت‌های متعلق به منبع هدف](/docs/concepts/overview/working-with-objects/owners-dependents/)،
[Jobهای تکمیل‌شده](/docs/concepts/workloads/controllers/ttlafterfinished/) و منابعی
که منقضی شده‌اند یا با شکست مواجه شده‌اند، استفاده می‌کند.
