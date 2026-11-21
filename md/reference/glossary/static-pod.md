---
title: Static Pod
id: static-pod
full_link: /docs/tasks/configure-pod-container/static-pod/
short_description: >
  پادی که مستقیماً به‌وسیلهٔ دیمن kubelet روی یک نود مشخص مدیریت می‌شود.

aka: 
tags:
- fundamental
---

یک {{< glossary_tooltip text="پاد" term_id="pod" >}} که مستقیماً به‌وسیلهٔ دیمن {{< glossary_tooltip text="kubelet" term_id="kubelet" >}}
 روی یک نود مشخص مدیریت می‌شود،
<!--more-->

بی‌آنکه API server آن را زیر نظر داشته باشد.

پادهای ایستا (Static Pod) از {{< glossary_tooltip text="کانتینرهای موقت" term_id="ephemeral-container" >}} پشتیبانی نمی‌کنند.
