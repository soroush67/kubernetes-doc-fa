---
title: جمع‌آوری زباله (Garbage Collection)
id: garbage-collection
full_link: /docs/concepts/architecture/garbage-collection/
short_description: >
  اصطلاحی جامع برای سازوکارهای گوناگونی که کوبرنتیز برای پاک‌سازی منابع کلاستر به کار می‌گیرد.

aka: 
tags:
- fundamental
- operation
---

جمع‌آوری زباله اصطلاحی جامع برای سازوکارهای گوناگونی است که کوبرنتیز برای پاک‌سازی منابع کلاستر به کار می‌گیرد.

<!--more-->

کوبرنتیز با جمع‌آوری زباله منابعی مانند
[کانتینرها و ایمیج‌های بلااستفاده](/docs/concepts/architecture/garbage-collection/#containers-images)،
[پادهای ناموفق](/docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)،
[آبجکت‌هایی که مالکشان منبع موردنظر است](/docs/concepts/overview/working-with-objects/owners-dependents/)،
[Jobهای تکمیل‌شده](/docs/concepts/workloads/controllers/ttlafterfinished/) و منابعی را
که منقضی شده یا با شکست مواجه شده‌اند پاک‌سازی می‌کند.
