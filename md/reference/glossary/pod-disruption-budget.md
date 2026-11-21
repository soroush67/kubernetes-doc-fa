---
id: pod-disruption-budget
title: بودجه اختلال پاد
full-link: /docs/concepts/workloads/pods/disruptions/
short_description: >
 آبجکتی که تعداد Podهای یک برنامه تکثیرشده را که به‌طور هم‌زمان بر اثر اختلال‌های داوطلبانه از دسترس خارج می‌شوند، محدود می‌کند.

aka:
 - PDB
related:
 - pod
 - container
tags:
 - operation
---

 با یک [بودجه اختلال پاد (Pod Disruption Budget)](/docs/concepts/workloads/pods/disruptions/)، مالک برنامه
 می‌تواند برای یک برنامه تکثیرشده آبجکتی ایجاد کند که تضمین می‌کند در هیچ لحظه‌ای
 تعداد یا درصد مشخصی از {{< glossary_tooltip text="Podها" term_id="pod" >}}
 که برچسب معینی دارند، به‌صورت داوطلبانه بیرون رانده (evict) نشوند.

<!--more--> 

بودجه‌های اختلال پاد نمی‌توانند از اختلال‌های غیرداوطلبانه جلوگیری کنند؛ با این حال،
این اختلال‌ها نیز از بودجه کسر می‌شوند.
