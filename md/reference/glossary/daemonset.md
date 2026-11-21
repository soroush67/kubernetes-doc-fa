---
title: DaemonSet
id: daemonset
full_link: /docs/concepts/workloads/controllers/daemonset
short_description: >
  اطمینان حاصل می‌کند که یک نسخه از یک Pod روی مجموعه‌ای از نودهای یک کلاستر در حال اجرا باشد.

aka: 
tags:
- fundamental
- core-object
- workload
---
 اطمینان حاصل می‌کند که یک نسخه از یک {{< glossary_tooltip text="Pod" term_id="pod" >}} روی مجموعه‌ای از نودهای یک {{< glossary_tooltip text="کلاستر" term_id="cluster" >}} در حال اجرا باشد.

<!--more--> 

از آن برای استقرار دیمن‌های سیستمی (system daemons)، مانند گردآورنده‌های لاگ و عامل‌های پایش، استفاده می‌شود که معمولاً باید روی هر {{< glossary_tooltip text="نود" term_id="node" >}} اجرا شوند.
