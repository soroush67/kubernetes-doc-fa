---
title: PodGroup
id: podgroup
full_link: /docs/concepts/workloads/podgroup-api/
short_description: >
  هر PodGroup مجموعه‌ای از Podها را با سیاست و محدودیت‌های زمان‌بندی مشترک نمایش می‌دهد.

aka:
tags:
- core-object
- workload
---
هر PodGroup یک آبجکت زمان اجرا (runtime) است که گروهی از Podها را نمایش می‌دهد که با هم و به‌صورت یک واحد واحد زمان‌بندی می‌شوند. در حالی که
[Workload API](/docs/concepts/workloads/workload-api/) الگوهای سیاست زمان‌بندی را تعریف می‌کند، PodGroupها همتای زمان اجرای این الگوها هستند و هم سیاست و هم وضعیت زمان‌بندی یک نمونهٔ مشخص از آن گروه را در خود نگه می‌دارند.
