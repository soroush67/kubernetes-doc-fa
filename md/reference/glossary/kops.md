---
title: kOps (Kubernetes Operations)
id: kops
full_link: /docs/setup/production-environment/kops/
short_description: >
  kOps نه‌تنها به شما کمک می‌کند کلاستر کوبرنتیز با کیفیت تولیدی و دسترس‌پذیری بالا را ایجاد، حذف، ارتقا و نگهداری کنید، بلکه زیرساخت ابری موردنیاز را نیز فراهم می‌کند.

aka: 
tags:
- tool
- operation
---

`kOps` نه‌تنها به شما کمک می‌کند کلاستر کوبرنتیز با کیفیت تولیدی و دسترس‌پذیری بالا را ایجاد، حذف، ارتقا و نگهداری کنید، بلکه زیرساخت ابری موردنیاز را نیز فراهم می‌کند.

<!--more--> 

{{< note >}}
در حال حاضر AWS (Amazon Web Services) به‌طور رسمی پشتیبانی می‌شود؛ DigitalOcean، GCE و OpenStack در مرحله پشتیبانی بتا قرار دارند و Azure در مرحله آلفا است.
{{< /note >}}

`kOps` یک سیستم تأمین خودکار (provisioning) است:
  * نصب کاملاً خودکار
  * استفاده از DNS برای شناسایی کلاسترها
  * خودترمیمی: همه‌چیز در Auto-Scaling Groupها اجرا می‌شود
  * پشتیبانی از چند سیستم‌عامل (Amazon Linux، Debian، Flatcar، RHEL، Rocky و Ubuntu)
  * پشتیبانی از دسترس‌پذیری بالا (High-Availability)
  * امکان تأمین مستقیم زیرساخت یا تولید مانیفست‌های terraform
