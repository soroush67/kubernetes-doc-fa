---
title: PodGroup
id: podgroup
full_link: /docs/concepts/workloads/podgroup-api/
short_description: >
  یک PodGroup مجموعه‌ای از Podها را با سیاست و محدودیت‌های زمان‌بندی مشترک نمایش می‌دهد.

aka:
tags:
- core-object
- workload
---
یک PodGroup یک آبجکت زمان اجرا (runtime) است که گروهی از Podها را نمایش می‌دهد که به‌صورت یک واحد واحد با هم زمان‌بندی می‌شوند. در حالی که [Workload API](/docs/concepts/workloads/workload-api/) قالب‌های سیاست زمان‌بندی را تعریف می‌کند، PodGroupها نمونه‌های متناظر آن‌ها در زمان اجرا هستند که هم سیاست و هم وضعیت زمان‌بندی را برای یک نمونه مشخص از آن گروه در خود نگه می‌دارند.
