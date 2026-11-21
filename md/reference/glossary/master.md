---
title: Master
id: master
short_description: >
  اصطلاحی قدیمی که به‌عنوان مترادف نودهای اجراکنندهٔ control plane به کار می‌رود.

aka:
tags:
- fundamental
---
 اصطلاحی قدیمی است که به‌عنوان مترادف {{< glossary_tooltip text="نودهایی" term_id="node" >}} به کار می‌رود که میزبان {{< glossary_tooltip text="control plane" term_id="control-plane" >}} هستند.

<!--more-->
برخی ابزارهای آماده‌سازی (provisioning)، مانند {{< glossary_tooltip text="kubeadm" term_id="kubeadm" >}}، و نیز سرویس‌های مدیریت‌شده هنوز از این اصطلاح استفاده می‌کنند تا به {{< glossary_tooltip text="نودها" term_id="node" >}} با `kubernetes.io/role` {{< glossary_tooltip text="برچسب" term_id="label" >}} بزنند و محل قرارگیری {{< glossary_tooltip text="پادهای" term_id="pod" >}} {{< glossary_tooltip text="control plane" term_id="control-plane" >}} را کنترل کنند.
