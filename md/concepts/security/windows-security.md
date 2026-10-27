---
reviewers:
- jayunit100
- jsturtevant
- marosset
- perithompson
title:    امنیت برای نودهای Windows
content_type: concept
weight: 40
---

<!-- overview -->

این صفحه ملاحظات امنیتی و بهترین روش‌های مختص سیستم‌عامل Windows را شرح می‌دهد.

<!-- body -->

## محافظت از داده‌های Secret روی نودها

در Windows، داده‌های Secretها به‌صورت متن ساده (clear text) در ذخیره‌سازی محلی نود نوشته می‌شوند
(در مقایسه با استفاده از tmpfs / فایل‌سیستم‌های درون حافظه در Linux). به‌عنوان اپراتور کلاستر،
باید هر دو اقدام اضافی زیر را انجام دهید:

1. از ACLهای فایل برای ایمن‌سازی مکان فایل‌های Secretها استفاده کنید.
1. رمزنگاری در سطح حجم (volume) را با استفاده از
   [BitLocker](https://docs.microsoft.com/windows/security/information-protection/bitlocker/bitlocker-how-to-deploy-on-windows-server)
   اعمال کنید.

## کاربران کانتینر

می‌توان [RunAsUsername](/docs/tasks/configure-pod-container/configure-runasusername)
را برای Podها یا کانتینرهای Windows مشخص کرد تا فرایندهای کانتینر با یک کاربر مشخص اجرا شوند.
این قابلیت تقریباً معادل
[RunAsUser](/docs/concepts/security/pod-security-policy/#users-and-groups) است.

کانتینرهای Windows دو حساب کاربری پیش‌فرض ارائه می‌دهند: ContainerUser و ContainerAdministrator.
تفاوت‌های این دو حساب کاربری در بخش
[When to use ContainerAdmin and ContainerUser user accounts](https://docs.microsoft.com/virtualization/windowscontainers/manage-containers/container-security#when-to-use-containeradmin-and-containeruser-user-accounts)
از مستندات _Secure Windows containers_ مایکروسافت توضیح داده شده است.

کاربران محلی را می‌توان در طول فرایند ساخت ایمیج کانتینر به ایمیج‌های کانتینر افزود.

{{< note >}}

* ایمیج‌های مبتنی بر [Nano Server](https://hub.docker.com/_/microsoft-windows-nanoserver) به‌صورت پیش‌فرض
  با کاربر `ContainerUser` اجرا می‌شوند
* ایمیج‌های مبتنی بر [Server Core](https://hub.docker.com/_/microsoft-windows-servercore) به‌صورت پیش‌فرض
  با کاربر `ContainerAdministrator` اجرا می‌شوند

{{< /note >}}

کانتینرهای Windows همچنین می‌توانند با استفاده از
[Group Managed Service Accounts](/docs/tasks/configure-pod-container/configure-gmsa/)
به‌عنوان هویت‌های Active Directory اجرا شوند.

## ایزوله‌سازی امنیتی در سطح Pod

سازوکارهای security context در سطح Pod که مختص Linux هستند (مانند SELinux، AppArmor، Seccomp یا
قابلیت‌های سفارشی POSIX) روی نودهای Windows پشتیبانی نمی‌شوند.

کانتینرهای دارای دسترسی ویژه (Privileged) روی Windows [پشتیبانی نمی‌شوند](/docs/concepts/windows/intro/#compatibility-v1-pod-spec-containers-securitycontext).
در عوض، می‌توان از [کانتینرهای HostProcess](/docs/tasks/configure-pod-container/create-hostprocess-pod)
روی Windows استفاده کرد تا بسیاری از کارهایی که کانتینرهای دارای دسترسی ویژه در Linux انجام می‌دهند، انجام شود.
