---
title: بار کاری
id: workload
full_link: /docs/concepts/workloads/
short_description: >
   بار کاری (workload) برنامه‌ای است که روی کوبرنتیز اجرا می‌شود.

aka: 
tags:
- fundamental
---
   بار کاری (workload) برنامه‌ای است که روی کوبرنتیز اجرا می‌شود.

<!--more--> 

آبجکت‌های اصلی گوناگونی انواع یا بخش‌های مختلف یک بار کاری را نمایش می‌دهند؛ از جمله آبجکت‌های DaemonSet، Deployment، Job، ReplicaSet و StatefulSet.

برای مثال، در بار کاری‌ای که از یک وب‌سرور و یک پایگاه داده تشکیل شده است، ممکن است پایگاه داده در یک {{< glossary_tooltip term_id="StatefulSet" >}} و وب‌سرور در یک {{< glossary_tooltip term_id="Deployment" >}} اجرا شود.
