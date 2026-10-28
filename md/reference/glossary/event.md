---
title: Event
id: event
full_link: /docs/reference/kubernetes-api/cluster-resources/event-v1/
short_description: >
   آبجکت‌های کوبرنتیز که تغییر وضعیتی را در کلاستر توصیف می‌کنند.
aka: 
tags:
- core-object
- fundamental
---
یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} کوبرنتیز که تغییرات وضعیت
یا رخدادهای قابل‌توجه در کلاستر را توصیف می‌کند.

<!--more-->
Eventها مدت زمان نگهداری محدودی دارند و محرک‌ها (triggers) و پیام‌ها ممکن است با گذشت زمان تغییر کنند.
مصرف‌کنندگان Event نباید به این امر تکیه کنند که زمان‌بندی یک Event با دلیل (reason) مشخص، همواره نشان‌دهنده‌ی یک محرک زیربنایی ثابت است،
و نیز نباید به ادامه‌ی وجود Eventهایی با آن دلیل اتکا کنند.

Eventها باید به‌عنوان داده‌ی اطلاعاتی، مکمل و با تلاش حداکثری (best-effort) در نظر گرفته شوند.

در کوبرنتیز، [ممیزی (auditing)](/docs/tasks/debug/debug-cluster/audit/) نوع متفاوتی از رکورد
Event تولید می‌کند (گروه API با نام `audit.k8s.io`).
