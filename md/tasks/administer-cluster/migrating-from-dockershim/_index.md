---
title: "مهاجرت از dockershim"
weight: 20
content_type: task
no_list: true
---

<!-- overview -->

این بخش اطلاعاتی را ارائه می‌کند که هنگام مهاجرت از dockershim به دیگر محیط‌های اجرای کانتینر (container runtime) باید بدانید.

از زمان اعلام [منسوخ شدن dockershim](/blog/2020/12/08/kubernetes-1-20-release-announcement/#dockershim-deprecation)
در کوبرنتیز 1.20، پرسش‌هایی درباره‌ی تأثیر این تغییر بر بارهای کاری و نصب‌های مختلف کوبرنتیز مطرح شده است. [پرسش‌های متداول درباره‌ی حذف Dockershim](/blog/2022/02/17/dockershim-faq/) به شما کمک می‌کند تا این مسئله را بهتر درک کنید.

با انتشار نسخه‌ی v1.24، ‏dockershim از کوبرنتیز حذف شد.
اگر از Docker Engine از طریق dockershim به‌عنوان محیط اجرای کانتینر خود استفاده می‌کنید و می‌خواهید به v1.24 ارتقا دهید، توصیه می‌شود یا به محیط اجرای دیگری مهاجرت کنید یا راه جایگزینی برای دریافت پشتیبانی از Docker Engine بیابید.
برای آشنایی با گزینه‌های خود، بخش [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/) را ببینید.

نسخه‌ای از کوبرنتیز که dockershim را دارد (1.23) دیگر پشتیبانی نمی‌شود و پشتیبانی از v1.24 نیز [به‌زودی](/releases/#release-v1-24) پایان می‌یابد. حتماً
[مشکلاتی](https://github.com/kubernetes/kubernetes/issues) را که در جریان مهاجرت با آن‌ها روبه‌رو شده‌اید گزارش دهید تا این مشکلات به‌موقع برطرف شوند و کلاستر شما برای حذف dockershim آماده باشد. پس از پایان پشتیبانی از v1.24، اگر مشکلات جدی‌ای کلاستر شما را تحت تأثیر قرار دهند، باید برای دریافت پشتیبانی با ارائه‌دهنده‌ی کوبرنتیز خود تماس بگیرید یا چند نسخه را به‌طور هم‌زمان ارتقا دهید.

ممکن است کلاستر شما بیش از یک نوع نود داشته باشد، هرچند این پیکربندی رایج نیست.

کارهای زیر به شما در مهاجرت کمک می‌کنند:

* [بررسی اینکه آیا حذف Dockershim بر شما تأثیر می‌گذارد](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
* [مهاجرت عامل‌های تله‌متری و امنیتی از dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)


## {{% heading "whatsnext" %}}

* برای آشنایی با گزینه‌های جایگزین، بخش [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/) را ببینید.
* اگر در زمینه‌ی مهاجرت از dockershim با نقص یا نگرانی فنی دیگری روبه‌رو شدید، می‌توانید آن را از طریق [گزارش یک مشکل](https://github.com/kubernetes/kubernetes/issues/new/choose) به پروژه‌ی کوبرنتیز اطلاع دهید.
