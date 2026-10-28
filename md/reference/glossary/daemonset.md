---
title: DaemonSet
id: daemonset
full_link: /docs/concepts/workloads/controllers/daemonset
short_description: >
  اطمینان حاصل می‌کند که یک نسخه از Pod روی مجموعه‌ای از نودهای یک کلاستر در حال اجرا است.

aka: 
tags:
- fundamental
- core-object
- workload
---
 اطمینان حاصل می‌کند که یک نسخه از {{< glossary_tooltip text="Pod" term_id="pod" >}} روی مجموعه‌ای از نودهای یک {{< glossary_tooltip text="کلاستر" term_id="cluster" >}} در حال اجرا است.

<!--more--> 

برای استقرار دیمن‌های سیستمی مانند جمع‌آورندگان لاگ و عامل‌های پایش به کار می‌رود که معمولاً باید روی هر {{< glossary_tooltip text="نود" term_id="node" >}} اجرا شوند.
