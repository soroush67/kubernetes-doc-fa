---
title: Kubelet
id: kubelet
full_link: /docs/reference/command-line-tools-reference/kubelet
short_description: >
  عاملی که روی هر نود در کلاستر اجرا می‌شود و اطمینان می‌دهد که کانتینرها در یک Pod در حال اجرا هستند.

aka:
tags:
- fundamental
---
 عاملی که روی هر {{< glossary_tooltip text="نود" term_id="node" >}} در کلاستر اجرا می‌شود و اطمینان می‌دهد که {{< glossary_tooltip text="کانتینرها" term_id="container" >}} در یک {{< glossary_tooltip text="Pod" term_id="pod" >}} در حال اجرا هستند.

<!--more-->


مؤلفهٔ [kubelet](/docs/reference/command-line-tools-reference/kubelet/) مجموعه‌ای از PodSpecها را که از راه سازوکارهای گوناگون در اختیارش قرار می‌گیرند دریافت می‌کند و اطمینان می‌دهد که کانتینرهای توصیف‌شده در این PodSpecها در حال اجرا و سالم هستند. این مؤلفه کانتینرهایی را که کوبرنتیز ایجاد نکرده است مدیریت نمی‌کند.
