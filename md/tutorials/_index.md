---
title: آموزش‌ها
main_menu: true
no_list: true
weight: 60
content_type: concept
---

<!-- overview -->

این بخش از مستندات کوبرنتیز شامل آموزش‌هاست. هر آموزش نشان می‌دهد که چگونه
می‌توان به هدفی بزرگ‌تر از یک [وظیفه (task)](/docs/tasks/) دست یافت. معمولاً
هر آموزش چند بخش دارد و هر بخش از دنباله‌ای از گام‌ها تشکیل شده است. پیش از
شروع هر آموزش، بهتر است صفحهٔ [واژه‌نامهٔ استاندارد](/docs/reference/glossary/)
را برای مراجعه‌های بعدی نشانک‌گذاری کنید.

<!-- body -->

## مبانی

* [مبانی کوبرنتیز](/docs/tutorials/kubernetes-basics/) آموزشی تعاملی و عمیق است که به شما کمک می‌کند سیستم کوبرنتیز را بشناسید و برخی از قابلیت‌های پایه‌ای آن را امتحان کنید.
* [مقدمه‌ای بر کوبرنتیز (edX)](https://www.edx.org/course/introduction-kubernetes-linuxfoundationx-lfs158x#)
* [سلام Minikube](/docs/tutorials/hello-minikube/)

## پیکربندی

* [پیکربندی Redis با استفاده از ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)

## نوشتن Podها

* [به‌کارگیری کانتینرهای جانبی (Sidecar)](/docs/tutorials/configuration/pod-sidecar-containers/)

## برنامه‌های بدون حالت

* [در دسترس قرار دادن یک نشانی IP خارجی برای دسترسی به برنامه‌ای در کلاستر](/docs/tutorials/stateless-application/expose-external-ip-address/)
* [مثال: استقرار برنامهٔ دفتر مهمان PHP همراه با Redis](/docs/tutorials/stateless-application/guestbook/)

## برنامه‌های دارای حالت

* [مبانی StatefulSet](/docs/tutorials/stateful-application/basic-stateful-set/)
* [مثال: WordPress و MySQL با حجم‌های پایدار (Persistent Volumes)](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
* [مثال: استقرار Cassandra با StatefulSetها](/docs/tutorials/stateful-application/cassandra/)
* [اجرای ZooKeeper، یک سیستم توزیع‌شدهٔ CP](/docs/tutorials/stateful-application/zookeeper/)

## سرویس‌ها

* [اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/)
* [استفاده از IP مبدأ](/docs/tutorials/services/source-ip/)

## امنیت

* [اعمال استانداردهای امنیتی Pod در سطح کلاستر](/docs/tutorials/security/cluster-level-pss/)
* [اعمال استانداردهای امنیتی Pod در سطح فضای نام (namespace)](/docs/tutorials/security/ns-level-pss/)
* [محدود کردن دسترسی کانتینر به منابع با AppArmor](/docs/tutorials/security/apparmor/)
* [Seccomp](/docs/tutorials/security/seccomp/)

## مدیریت کلاستر

* [اجرای kubelet در حالت مستقل](/docs/tutorials/cluster-management/kubelet-standalone/)
* [پیکربندی حافظهٔ Swap روی نودهای کوبرنتیز](/docs/tutorials/cluster-management/provision-swap-memory/)
* [نصب درایورها و تخصیص دستگاه‌ها با DRA](/docs/tutorials/cluster-management/install-use-dra/)
* [بررسی سیاست‌های پذیرش اعتبارسنجی و تغییردهنده (Admission Policies)](/docs/tutorials/cluster-management/admission-policies/)

## {{% heading "whatsnext" %}}

اگر می‌خواهید آموزشی بنویسید، برای آشنایی با نوع صفحهٔ آموزش به
[انواع صفحهٔ محتوا](/docs/contribute/style/page-content-types/)
مراجعه کنید.
