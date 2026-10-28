---
title: بار کاری
id: workload
full_link: /docs/concepts/workloads/
short_description: >
   بار کاری (workload) یک برنامه کاربردی است که روی کوبرنتیز اجرا می‌شود.

aka: 
tags:
- fundamental
---
   بار کاری (workload) یک برنامه کاربردی است که روی کوبرنتیز اجرا می‌شود.

<!--more--> 

آبجکت‌های اصلی گوناگونی که انواع یا بخش‌های مختلف یک بار کاری را نمایش می‌دهند،
شامل آبجکت‌های DaemonSet، Deployment، Job، ReplicaSet و StatefulSet هستند.

برای مثال، یک بار کاری که شامل یک وب‌سرور و یک پایگاه داده است، ممکن است پایگاه داده را
در یک {{< glossary_tooltip term_id="StatefulSet" >}} و وب‌سرور را
در یک {{< glossary_tooltip term_id="Deployment" >}} اجرا کند.
