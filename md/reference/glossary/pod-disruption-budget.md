---
id: pod-disruption-budget
title: Pod Disruption Budget
full-link: /docs/concepts/workloads/pods/disruptions/
short_description: >
 آبجکتی که تعداد Podهای یک اپلیکیشن replicated را که هم‌زمان در اثر اختلال‌های داوطلبانه از دسترس خارج می‌شوند، محدود می‌کند.

aka:
 - PDB
related:
 - pod
 - container
tags:
 - operation
---

 [Pod Disruption Budget](/docs/concepts/workloads/pods/disruptions/) به مالک یک اپلیکیشن این امکان را می‌دهد که برای یک اپلیکیشن replicated آبجکتی ایجاد کند که تضمین می‌کند تعداد یا درصد مشخصی از {{< glossary_tooltip text="Podهای" term_id="pod" >}}
 دارای یک برچسب مشخص، در هیچ لحظه‌ای به‌صورت داوطلبانه بیرون‌رانی (evict) نخواهند شد.

<!--more--> 

اختلال‌های غیرداوطلبانه را نمی‌توان با PDBها از وقوع بازداشت؛ با این حال،
این اختلال‌ها در محاسبه‌ی بودجه (budget) لحاظ می‌شوند.
