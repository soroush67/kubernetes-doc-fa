---
title: ReplicaSet
id: replica-set
full_link: /docs/concepts/workloads/controllers/replicaset/
short_description: >
 یک ReplicaSet تضمین می‌کند که تعداد مشخصی از نسخه‌های تکثیرشدهٔ Pod در هر لحظه در حال اجرا باشند

aka: 
tags:
- fundamental
- core-object
- workload
---
 هر ReplicaSet (تلاش می‌کند) مجموعه‌ای از Podهای تکثیرشده (replica) را در هر لحظه در حال اجرا نگه دارد.

<!--more-->

آبجکت‌های بار کاری (workload) مانند {{< glossary_tooltip term_id="deployment" >}} از ReplicaSetها استفاده می‌کنند تا اطمینان یابند تعداد پیکربندی‌شدهٔ {{< glossary_tooltip term_id="pod" text="Podها" >}}، مطابق با spec همان ReplicaSet، در کلاستر شما در حال اجرا هستند.
