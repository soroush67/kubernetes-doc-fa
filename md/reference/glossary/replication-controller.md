---
title: ReplicationController
id: replication-controller
full_link: 
short_description: >
  یک آبجکت API (منسوخ‌شده) که یک برنامه تکثیرشده را مدیریت می‌کند.

aka: 
tags:
- workload
- core-object
---
یک {{< glossary_tooltip text="آبجکت" term_id="object" >}} مدیریت بار کاری
که یک برنامه تکثیرشده را مدیریت می‌کند و اطمینان می‌دهد که
تعداد مشخصی از نمونه‌های یک {{< glossary_tooltip text="Pod" term_id="pod" >}} در حال اجرا هستند.

<!--more-->

control plane اطمینان حاصل می‌کند که تعداد تعریف‌شده‌ای از Podها در حال اجرا باشد، حتی اگر برخی از
Podها با خطا مواجه شوند، به‌صورت دستی Podها را حذف کنید، یا به‌اشتباه تعداد بیش از حدی از آن‌ها راه‌اندازی شود.

{{< note >}}
ReplicationController منسوخ شده است. به
{{< glossary_tooltip text="Deployment" term_id="deployment" >}} مراجعه کنید که عملکردی مشابه دارد.
{{< /note >}}
