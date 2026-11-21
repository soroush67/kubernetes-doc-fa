---
title: StatefulSet
id: statefulset
full_link: /docs/concepts/workloads/controllers/statefulset/
short_description: >
  هر StatefulSet استقرار و مقیاس‌دهی مجموعه‌ای از Podها را مدیریت می‌کند و برای هر Pod ذخیره‌سازی ماندگار و شناسه‌های پایدار فراهم می‌آورد.

aka: 
tags:
- fundamental
- core-object
- workload
- storage
---
 استقرار و مقیاس‌دهی مجموعه‌ای از {{< glossary_tooltip text="Podها" term_id="pod" >}} را مدیریت می‌کند *و ترتیب و یکتایی این Podها را تضمین می‌کند*.

<!--more--> 

هر StatefulSet، مانند یک {{< glossary_tooltip term_id="deployment" >}}، Podهایی را مدیریت می‌کند که بر پایهٔ مشخصات (spec) یکسانی از کانتینر ساخته شده‌اند. اما برخلاف Deployment، هر StatefulSet برای هر یک از Podهای خود هویتی ثابت و ماندگار نگه می‌دارد. این Podها از مشخصات یکسانی ساخته می‌شوند، ولی جایگزین‌پذیر نیستند&#58; هر کدام شناسه‌ای پایدار دارد که در هر بار زمان‌بندی مجدد حفظ می‌شود.

اگر می‌خواهید برای ماندگاری داده‌های بار کاری خود از حجم‌های (volume) ذخیره‌سازی استفاده کنید، می‌توانید StatefulSet را بخشی از راه‌حل خود قرار دهید. هرچند Podهای منفرد در یک StatefulSet ممکن است دچار خرابی شوند، شناسه‌های پایدار Podها کار تطبیق حجم‌های موجود با Podهای جدیدی را که جایگزین Podهای ازکارافتاده می‌شوند آسان‌تر می‌کنند.
