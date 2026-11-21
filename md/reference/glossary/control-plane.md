---
title: Control Plane
id: control-plane
full_link:
short_description: >
  لایهٔ هماهنگ‌سازی کانتینرها که API و رابط‌هایی را برای تعریف، استقرار و مدیریت چرخهٔ عمر کانتینرها در اختیار قرار می‌دهد.

aka:
tags:
- fundamental
---
 لایهٔ هماهنگ‌سازی (orchestration) کانتینرها که API و رابط‌هایی را برای تعریف، استقرار و مدیریت چرخهٔ عمر کانتینرها در اختیار قرار می‌دهد.

 <!--more--> 
 
 این لایه از مؤلفه‌های گوناگونی تشکیل شده است که از جملهٔ آن‌ها می‌توان به موارد زیر اشاره کرد (اما به آن‌ها محدود نمی‌شود):

 * {{< glossary_tooltip text="etcd" term_id="etcd" >}}
 * {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
 * {{< glossary_tooltip text="زمان‌بند" term_id="kube-scheduler" >}}
 * {{< glossary_tooltip text="مدیر کنترل‌کننده‌ها" term_id="kube-controller-manager" >}}
 * {{< glossary_tooltip text="مدیر کنترل‌کننده‌های ابری" term_id="cloud-controller-manager" >}}

 این مؤلفه‌ها را می‌توان به‌صورت سرویس‌های سنتی سیستم‌عامل (daemon) یا به‌صورت کانتینر اجرا کرد. میزبان‌هایی که این مؤلفه‌ها را اجرا می‌کنند، در گذشته {{< glossary_tooltip text="مستر" term_id="master" >}} (master) نامیده می‌شدند.
