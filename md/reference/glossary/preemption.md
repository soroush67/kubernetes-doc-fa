---
title: پیش‌دستی (Preemption)
id: preemption
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption
short_description: >
  منطق پیش‌دستی در کوبرنتیز با بیرون‌راندن Podهای کم‌اولویتِ موجود روی یک نود، به Pod در حال انتظار کمک می‌کند تا نود مناسبی پیدا کند.

aka:
tags:
- operation
---
 منطق پیش‌دستی (preemption) در کوبرنتیز با بیرون‌راندن Podهای کم‌اولویتِ موجود روی یک {{< glossary_tooltip term_id="node" >}}، به {{< glossary_tooltip term_id="pod" >}} در حال انتظار کمک می‌کند تا نود مناسبی پیدا کند.

<!--more-->

اگر نتوان یک Pod را زمان‌بندی کرد، زمان‌بند تلاش می‌کند با [پیش‌دستی](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption) بر Podهای کم‌اولویت‌تر، زمان‌بندی Pod در حال انتظار را ممکن کند.
