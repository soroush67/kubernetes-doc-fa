---
title: لایه کنترل (Control Plane)
id: control-plane
full_link:
short_description: >
  لایه هماهنگ‌سازی کانتینرها که API و رابط‌هایی را برای تعریف، استقرار و مدیریت چرخه عمر کانتینرها در اختیار قرار می‌دهد.

aka:
tags:
- fundamental
---
 لایه هماهنگ‌سازی کانتینرها که API و رابط‌هایی را برای تعریف، استقرار و مدیریت چرخه عمر کانتینرها در اختیار قرار می‌دهد.

 <!--more--> 
 
 این لایه از اجزای مختلفی تشکیل شده است، از جمله (و نه محدود به):

 * {{< glossary_tooltip text="etcd" term_id="etcd" >}}
 * {{< glossary_tooltip text="API Server" term_id="kube-apiserver" >}}
 * {{< glossary_tooltip text="زمان‌بند (Scheduler)" term_id="kube-scheduler" >}}
 * {{< glossary_tooltip text="Controller Manager" term_id="kube-controller-manager" >}}
 * {{< glossary_tooltip text="Cloud Controller Manager" term_id="cloud-controller-manager" >}}

 این اجزا می‌توانند به‌صورت سرویس‌های سنتی سیستم‌عامل (daemon) یا به‌صورت کانتینر اجرا شوند. میزبان‌هایی که این اجزا را اجرا می‌کردند، در گذشته {{< glossary_tooltip text="master" term_id="master" >}} نامیده می‌شدند.
