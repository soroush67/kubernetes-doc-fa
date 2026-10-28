---
title: Preemption
id: preemption
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption
short_description: >
  منطق Preemption در کوبرنتیز به یک Pod در حالت انتظار کمک می‌کند تا با بیرون‌راندن (evict) Podهای با اولویت پایین‌تر از یک نود، نود مناسبی برای خود پیدا کند.

aka:
tags:
- operation
---
 منطق Preemption در کوبرنتیز به یک {{< glossary_tooltip term_id="pod" >}} در حالت انتظار کمک می‌کند تا با بیرون‌راندن (evict) Podهای با اولویت پایین‌تر که روی یک {{< glossary_tooltip term_id="node" >}} موجود هستند، نود مناسبی برای خود پیدا کند.

<!--more-->

اگر زمان‌بندی یک Pod امکان‌پذیر نباشد، زمان‌بند تلاش می‌کند Podهای با اولویت پایین‌تر را [preempt](/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption) کند تا زمان‌بندی Pod در حالت انتظار ممکن شود.
