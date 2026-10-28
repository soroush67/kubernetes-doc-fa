---
title: ReplicaSet
id: replica-set
full_link: /docs/concepts/workloads/controllers/replicaset/
short_description: >
 ReplicaSet تضمین می‌کند که تعداد مشخصی از replicaهای Pod در هر زمان در حال اجرا باشند

aka: 
tags:
- fundamental
- core-object
- workload
---
 یک ReplicaSet (تلاش می‌کند) مجموعه‌ای از Podهای replica را در هر لحظه در حال اجرا نگه دارد.

<!--more-->

آبجکت‌های بار کاری مانند {{< glossary_tooltip term_id="deployment" >}} از ReplicaSetها استفاده می‌کنند تا اطمینان حاصل کنند که تعداد پیکربندی‌شده از {{< glossary_tooltip term_id="pod" text="Podها" >}} بر اساس spec آن ReplicaSet در کلاستر شما در حال اجرا هستند.
