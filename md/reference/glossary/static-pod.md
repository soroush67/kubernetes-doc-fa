---
title: Static Pod
id: static-pod
full_link: /docs/tasks/configure-pod-container/static-pod/
short_description: >
  پادی که مستقیماً توسط دیمون kubelet روی یک نود مشخص مدیریت می‌شود.

aka: 
tags:
- fundamental
---

یک {{< glossary_tooltip text="پاد" term_id="pod" >}} که مستقیماً توسط دیمون {{< glossary_tooltip text="kubelet" term_id="kubelet" >}}
 روی یک نود مشخص مدیریت می‌شود،
<!--more-->

بدون آن‌که سرور API آن را مشاهده کند.

Static Podها از {{< glossary_tooltip text="کانتینرهای موقت" term_id="ephemeral-container" >}} (ephemeral containers) پشتیبانی نمی‌کنند.
