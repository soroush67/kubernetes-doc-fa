---
title: PriorityClass
id: priority-class
full_link: /docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass
short_description: >
  نگاشتی از نام یک کلاس به اولویت زمان‌بندی که یک Pod باید داشته باشد.
aka:
tags:
- core-object
---
PriorityClass یک کلاس نام‌گذاری‌شده برای اولویت زمان‌بندی است که باید به Pod های موجود در آن کلاس اختصاص داده شود.

<!--more-->

[PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#how-to-use-priority-and-preemption)
یک آبجکت بدون فضای نام (non-namespaced) است که یک نام را به یک اولویت عددی صحیح نگاشت می‌کند و برای Pod استفاده می‌شود. نام در فیلد `metadata.name` و مقدار اولویت در فیلد `value` مشخص می‌شود. اولویت‌ها در بازه‌ی -2147483648 تا 1000000000 (با احتساب هر دو مرز) قرار دارند. مقادیر بالاتر نشان‌دهنده‌ی اولویت بیشتر هستند.
