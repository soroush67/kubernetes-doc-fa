---
title: ReplicationController
id: replication-controller
full_link: 
short_description: >
  یک آبجکت API (منسوخ‌شده) که یک برنامهٔ تکثیرشده را مدیریت می‌کند.

aka: 
tags:
- workload
- core-object
---
یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} مدیریت بار کاری
که یک برنامهٔ تکثیرشده را مدیریت می‌کند و تضمین می‌کند که
تعداد مشخصی از نمونه‌های یک {{< glossary_tooltip text="Pod" term_id="pod" >}} در حال اجرا باشند.

<!--more-->

لایهٔ control plane تضمین می‌کند که تعداد تعریف‌شده‌ای از Podها همواره در حال اجرا باشند؛
حتی اگر برخی از Podها از کار بیفتند، شما Podها را به‌صورت دستی حذف کنید یا تعداد زیادی از آن‌ها به اشتباه راه‌اندازی شوند.

{{< note >}}
منبع ReplicationController منسوخ شده است. به
{{< glossary_tooltip text="Deployment" term_id="deployment" >}} مراجعه کنید که عملکردی مشابه دارد.
{{< /note >}}
