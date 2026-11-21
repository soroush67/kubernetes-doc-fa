---
title: PriorityClass
id: priority-class
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass
short_description: >
  نگاشتی از نام یک کلاس به اولویت زمان‌بندی‌ای که یک Pod باید داشته باشد.
aka:
tags:
- core-object
---
هر PriorityClass کلاسی نام‌دار برای اولویت زمان‌بندی است که باید به Podهای عضو آن کلاس اختصاص داده شود.

<!--more-->

هر [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption)
آبجکتی بدون فضای نام (namespace) است که یک نام را به یک اولویت عددی صحیح نگاشت می‌کند و برای Podها به کار می‌رود. نام در فیلد `metadata.name` و مقدار اولویت در فیلد `value` مشخص می‌شود. بازهٔ اولویت‌ها از
‎-2147483648 تا 1000000000 (با احتساب هر دو مقدار) است. مقادیر بزرگ‌تر نشان‌دهندهٔ اولویت بالاترند.
