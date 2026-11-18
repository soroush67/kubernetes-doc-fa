---
reviewers:
- jayunit100
- jsturtevant
- marosset
- perithompson
title:    امنیت برای نودهای ویندوز
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه ملاحظات امنیتی و بهترین شیوه‌هایی را شرح می‌دهد که مختص سیستم‌عامل ویندوز هستند.

<!-- body -->

## محافظت از داده‌های Secret روی نودها

در ویندوز، داده‌های Secretها به‌صورت متن ساده (clear text) روی فضای ذخیره‌سازی محلی نود نوشته می‌شوند؛ در حالی که در لینوکس از tmpfs یا فایل‌سیستم‌های درون‌حافظه‌ای استفاده می‌شود. شما به‌عنوان اپراتور کلاستر باید هر دو اقدام تکمیلی زیر را انجام دهید:

1. با استفاده از ACLهای فایل، از محل ذخیره‌شدن فایل‌های Secretها محافظت کنید.
1. رمزنگاری در سطح حجم (volume) را با استفاده از
   [BitLocker](https://docs.microsoft.com/windows/security/information-protection/bitlocker/bitlocker-how-to-deploy-on-windows-server) اعمال کنید.

## کاربران کانتینر

برای اجرای پردازه‌های کانتینر با یک کاربر مشخص، می‌توان
[RunAsUsername](/docs/tasks/configure-pod-container/configure-runasusername)
را برای Podها یا کانتینرهای ویندوزی تعیین کرد. این تنظیم تقریباً معادل
[RunAsUser](/docs/concepts/security/pod-security-policy/#users-and-groups) است.

کانتینرهای ویندوز دو حساب کاربری پیش‌فرض با نام‌های ContainerUser و ContainerAdministrator ارائه می‌دهند.
تفاوت‌های این دو حساب کاربری در بخش
[چه زمانی از حساب‌های کاربری ContainerAdmin و ContainerUser استفاده کنیم](https://docs.microsoft.com/virtualization/windowscontainers/manage-containers/container-security#when-to-use-containeradmin-and-containeruser-user-accounts)
از مستندات _Secure Windows containers_ مایکروسافت توضیح داده شده است.

می‌توان در فرایند ساخت کانتینر، کاربران محلی را به ایمیج‌های کانتینر اضافه کرد.

{{< note >}}

* ایمیج‌های مبتنی بر [Nano Server](https://hub.docker.com/_/microsoft-windows-nanoserver) به‌طور پیش‌فرض با کاربر
  `ContainerUser` اجرا می‌شوند.
* ایمیج‌های مبتنی بر [Server Core](https://hub.docker.com/_/microsoft-windows-servercore) به‌طور پیش‌فرض با کاربر
  `ContainerAdministrator` اجرا می‌شوند.

{{< /note >}}

کانتینرهای ویندوز همچنین می‌توانند با بهره‌گیری از
[حساب‌های سرویس مدیریت‌شدهٔ گروهی (Group Managed Service Accounts)](/docs/tasks/configure-pod-container/configure-gmsa/)
با هویت‌های Active Directory اجرا شوند.

## جداسازی امنیتی در سطح Pod

سازوکارهای زمینهٔ امنیتی (security context) پاد که مختص لینوکس هستند، مانند SELinux، AppArmor، Seccomp یا قابلیت‌های سفارشی POSIX، روی نودهای ویندوز پشتیبانی نمی‌شوند.

کانتینرهای ممتاز (privileged) در ویندوز [پشتیبانی نمی‌شوند](/docs/concepts/windows/intro/#compatibility-v1-pod-spec-containers-securitycontext).
در عوض، در ویندوز می‌توان از [کانتینرهای HostProcess](/docs/tasks/configure-pod-container/create-hostprocess-pod)
برای انجام بسیاری از کارهایی استفاده کرد که در لینوکس با کانتینرهای ممتاز انجام می‌شوند.
