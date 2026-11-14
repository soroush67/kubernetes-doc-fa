---
title: پیکربندی RunAsUserName برای پادها و کانتینرهای ویندوزی
content_type: task
weight: 40
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

این صفحه نشان می‌دهد که چگونه می‌توان از تنظیم `runAsUserName` برای Podها و کانتینرهایی که روی نودهای ویندوزی اجرا می‌شوند استفاده کرد. این تنظیم تقریباً معادل تنظیم `runAsUser` در لینوکس است و با آن می‌توانید برنامه‌های درون کانتینر را با نام کاربری‌ای غیر از نام کاربری پیش‌فرض اجرا کنید.



## {{% heading "prerequisites" %}}


باید یک کلاستر کوبرنتیز داشته باشید و ابزار خط فرمان kubectl نیز باید برای ارتباط با کلاستر شما پیکربندی شده باشد. انتظار می‌رود کلاستر نودهای کارگر ویندوزی داشته باشد تا پادهایی که کانتینرهایشان بارهای کاری ویندوزی را اجرا می‌کنند روی آن‌ها زمان‌بندی شوند.



<!-- steps -->

## تعیین نام کاربری برای یک Pod

برای تعیین نام کاربری‌ای که فرایندهای کانتینر Pod با آن اجرا می‌شوند، فیلد `securityContext` ([PodSecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podsecuritycontext-v1-core)) را در مشخصات Pod قرار دهید و درون آن، فیلد `windowsOptions` ([WindowsSecurityContextOptions](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#windowssecuritycontextoptions-v1-core)) را که شامل فیلد `runAsUserName` است اضافه کنید.

گزینه‌های زمینهٔ امنیتی ویندوز که برای یک Pod تعیین می‌کنید، روی همهٔ کانتینرها و کانتینرهای init آن Pod اعمال می‌شوند.

در ادامه یک فایل پیکربندی برای یک Pod ویندوزی آمده است که فیلد `runAsUserName` در آن تنظیم شده است:

{{% code_sample file="windows/run-as-username-pod.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/windows/run-as-username-pod.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod run-as-username-pod-demo
```

به یک پوسته (shell) در کانتینر در حال اجرا دسترسی پیدا کنید:

```shell
kubectl exec -it run-as-username-pod-demo -- powershell
```

بررسی کنید که پوسته با نام کاربری درست اجرا می‌شود:

```powershell
echo $env:USERNAME
```

خروجی باید به این صورت باشد:

```
ContainerUser
```

## تعیین نام کاربری برای یک کانتینر

برای تعیین نام کاربری‌ای که فرایندهای یک کانتینر با آن اجرا می‌شوند، فیلد `securityContext` ([SecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#securitycontext-v1-core)) را در مانیفست کانتینر قرار دهید و درون آن، فیلد `windowsOptions` ([WindowsSecurityContextOptions](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#windowssecuritycontextoptions-v1-core)) را که شامل فیلد `runAsUserName` است اضافه کنید.

گزینه‌های زمینهٔ امنیتی ویندوز که برای یک کانتینر تعیین می‌کنید، فقط روی همان کانتینر اعمال می‌شوند و تنظیمات انجام‌شده در سطح Pod را بازنویسی می‌کنند.

در ادامه فایل پیکربندی یک Pod با یک کانتینر آمده است که فیلد `runAsUserName` در آن هم در سطح Pod و هم در سطح کانتینر تنظیم شده است:

{{% code_sample file="windows/run-as-username-container.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/windows/run-as-username-container.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod run-as-username-container-demo
```

به یک پوسته در کانتینر در حال اجرا دسترسی پیدا کنید:

```shell
kubectl exec -it run-as-username-container-demo -- powershell
```

بررسی کنید که پوسته با نام کاربری درست (نام کاربری تنظیم‌شده در سطح کانتینر) اجرا می‌شود:

```powershell
echo $env:USERNAME
```

خروجی باید به این صورت باشد:

```
ContainerAdministrator
```

## محدودیت‌های نام کاربری ویندوز

برای استفاده از این قابلیت، مقدار تنظیم‌شده در فیلد `runAsUserName` باید یک نام کاربری معتبر باشد. این مقدار باید قالب `DOMAIN\USER` را داشته باشد که در آن بخش `DOMAIN\` اختیاری است. نام‌های کاربری ویندوز به بزرگی و کوچکی حروف حساس نیستند. افزون بر این، محدودیت‌هایی دربارهٔ `DOMAIN` و `USER` وجود دارد:

- فیلد `runAsUserName` نمی‌تواند خالی باشد و نمی‌تواند نویسه‌های کنترلی (مقادیر ASCII: `0x00-0x1F`، `0x7F`) داشته باشد.
- بخش `DOMAIN` باید یا یک نام NetBios یا یک نام DNS باشد که هر کدام محدودیت‌های خاص خود را دارند:
  - نام‌های NetBios: حداکثر ۱۵ نویسه دارند، نمی‌توانند با `.` (نقطه) شروع شوند و نمی‌توانند نویسه‌های زیر را داشته باشند: `\ / : * ? " < > |`
  - نام‌های DNS: حداکثر ۲۵۵ نویسه دارند، فقط شامل نویسه‌های حرفی‌عددی، نقطه و خط تیره هستند و نمی‌توانند با `.` (نقطه) یا `-` (خط تیره) شروع شوند یا پایان یابند.
- بخش `USER` حداکثر می‌تواند ۲۰ نویسه داشته باشد، نمی‌تواند *فقط* از نقطه یا فاصله تشکیل شده باشد و نمی‌تواند نویسه‌های زیر را داشته باشد: `" / \ [ ] : ; | = , + * ? < > @`.

نمونه‌هایی از مقادیر قابل‌قبول برای فیلد `runAsUserName`: `ContainerAdministrator`، `ContainerUser`، `NT AUTHORITY\NETWORK SERVICE`، `NT AUTHORITY\LOCAL SERVICE`.

برای اطلاعات بیشتر دربارهٔ این محدودیت‌ها، [اینجا](https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and) و [اینجا](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-5.1) را ببینید.



## {{% heading "whatsnext" %}}


* [راهنمای زمان‌بندی کانتینرهای ویندوزی در کوبرنتیز](/docs/concepts/windows/user-guide/)
* [مدیریت هویت بار کاری با حساب‌های سرویس مدیریت‌شدهٔ گروهی (GMSA)](/docs/concepts/windows/user-guide/#managing-workload-identity-with-group-managed-service-accounts)
* [پیکربندی GMSA برای پادها و کانتینرهای ویندوزی](/docs/tasks/configure-pod-container/configure-gmsa/)
