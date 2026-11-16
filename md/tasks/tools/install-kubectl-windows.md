---
reviewers:
- mikedanese
title: نصب و راه‌اندازی kubectl در ویندوز
content_type: task
weight: 10
---

## {{% heading "prerequisites" %}}

باید از نسخه‌ای از kubectl استفاده کنید که حداکثر یک نسخهٔ فرعی (minor) با کلاستر شما اختلاف داشته باشد.
برای نمونه، کلاینت v{{< skew currentVersion >}} می‌تواند با control plane نسخه‌های
v{{< skew currentVersionAddMinor -1 >}}، v{{< skew currentVersionAddMinor 0 >}}
و v{{< skew currentVersionAddMinor 1 >}} ارتباط برقرار کند.
استفاده از جدیدترین نسخهٔ سازگار kubectl به جلوگیری از مشکلات پیش‌بینی‌نشده کمک می‌کند.

## نصب kubectl در ویندوز

برای نصب kubectl در ویندوز روش‌های زیر وجود دارد:

- [نصب فایل باینری kubectl در ویندوز (با دانلود مستقیم یا curl)](#install-kubectl-binary-on-windows-via-direct-download-or-curl)
- [نصب در ویندوز با Chocolatey، Scoop یا winget](#install-nonstandard-package-tools)

### نصب فایل باینری kubectl در ویندوز (با دانلود مستقیم یا curl)

1. برای نصب kubectl روی دستگاه ویندوزی خود دو گزینه دارید:

   - دانلود مستقیم:
     
     با مراجعه به [صفحهٔ انتشارهای کوبرنتیز](https://kubernetes.io/releases/download/#binaries)، فایل باینری جدیدترین انتشار وصله‌ای (patch) نسخهٔ {{< skew currentVersion >}} را مستقیماً برای معماری مورد نظر خود دانلود کنید. حتماً فایل باینری متناسب با معماری خود (مانند amd64، arm64 و غیره) را انتخاب کنید.
   
   - با استفاده از curl:

     اگر `curl` را نصب کرده‌اید، از این دستور استفاده کنید:

     ```powershell
     curl.exe -LO "https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kubectl.exe"
     ```

   {{< note >}}
   برای یافتن جدیدترین نسخهٔ پایدار (برای نمونه، جهت استفاده در اسکریپت‌ها)، به
   [https://dl.k8s.io/release/stable.txt](https://dl.k8s.io/release/stable.txt) مراجعه کنید.
   {{< /note >}}

1. اعتبارسنجی فایل باینری (اختیاری)

   فایل checksum مربوط به `kubectl` را دانلود کنید:

   ```powershell
   curl.exe -LO "https://dl.k8s.io/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kubectl.exe.sha256"
   ```

   فایل باینری `kubectl` را با فایل checksum اعتبارسنجی کنید:

   - با استفاده از Command Prompt و مقایسهٔ دستی خروجی `CertUtil` با فایل checksum دانلودشده:

     ```cmd
     CertUtil -hashfile kubectl.exe SHA256
     type kubectl.exe.sha256
     ```

   - با استفاده از PowerShell و خودکارسازی بررسی با عملگر `-eq` برای دریافت نتیجهٔ
     `True` یا `False`:

     ```powershell
      $(Get-FileHash -Algorithm SHA256 .\kubectl.exe).Hash -eq $(Get-Content .\kubectl.exe.sha256)
     ```

1. پوشهٔ فایل باینری `kubectl` را به انتها یا ابتدای متغیر محیطی `PATH` خود اضافه کنید.

1. آزمایش کنید تا مطمئن شوید نسخهٔ `kubectl` با نسخهٔ دانلودشده یکسان است:

   ```cmd
   kubectl version --client
   ```
   
   یا برای مشاهدهٔ جزئیات نسخه از این دستور استفاده کنید:

   ```cmd
   kubectl version --client --output=yaml
   ```



{{< note >}}
[Docker Desktop برای ویندوز](https://docs.docker.com/docker-for-windows/#kubernetes)
نسخهٔ مخصوص خود از `kubectl` را به `PATH` اضافه می‌کند. اگر پیش‌تر Docker Desktop را نصب کرده‌اید،
ممکن است لازم باشد مدخل `PATH` خود را پیش از مدخلی قرار دهید که نصب‌کنندهٔ Docker Desktop اضافه کرده است،
یا `kubectl` مربوط به Docker Desktop را حذف کنید.
{{< /note >}}

### نصب در ویندوز با Chocolatey، Scoop یا winget {#install-nonstandard-package-tools}

1. برای نصب kubectl در ویندوز می‌توانید از مدیر بستهٔ [Chocolatey](https://chocolatey.org)،
   نصب‌کنندهٔ خط فرمان [Scoop](https://scoop.sh) یا
   مدیر بستهٔ [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) استفاده کنید.

   {{< tabs name="kubectl_win_install" >}}
   {{% tab name="choco" %}}
   ```powershell
   choco install kubernetes-cli
   ```
   {{% /tab %}}
   {{% tab name="scoop" %}}
   ```powershell
   scoop install kubectl
   ```
   {{% /tab %}}
   {{% tab name="winget" %}}
   ```powershell
   winget install -e --id Kubernetes.kubectl
   ```
   {{% /tab %}}
   {{< /tabs >}}

1. آزمایش کنید تا مطمئن شوید نسخهٔ نصب‌شده به‌روز است:

   ```powershell
   kubectl version --client
   ```

1. به پوشهٔ خانگی (home) خود بروید:

   ```powershell
   # If you're using cmd.exe, run: cd %USERPROFILE%
   cd ~
   ```

1. پوشهٔ `.kube` را ایجاد کنید:

   ```powershell
   mkdir .kube
   ```

1. به پوشهٔ `.kube` که هم‌اکنون ایجاد کردید بروید:

   ```powershell
   cd .kube
   ```

1. kubectl را برای استفاده از یک کلاستر کوبرنتیز راه دور پیکربندی کنید:

   ```powershell
   New-Item config -type file
   ```

{{< note >}}
فایل config را با یک ویرایشگر متن دلخواه، مانند Notepad، ویرایش کنید.
{{< /note >}}

## بررسی پیکربندی kubectl

{{< include "included/verify-kubectl.md" >}}

## پیکربندی‌ها و افزونه‌های اختیاری kubectl

### فعال‌سازی تکمیل خودکار در پوسته

ابزار kubectl از تکمیل خودکار (autocompletion) برای Bash، Zsh، Fish و PowerShell پشتیبانی می‌کند
که می‌تواند بخش زیادی از تایپ کردن را برای شما کاهش دهد.

در ادامه، مراحل راه‌اندازی تکمیل خودکار برای PowerShell آمده است.

{{< include "included/optional-kubectl-configs-pwsh.md" >}}

### پیکربندی kuberc

برای اطلاعات بیشتر، [kuberc](/docs/reference/kubectl/kuberc) را ببینید.

### نصب افزونهٔ `kubectl convert`

{{< include "included/kubectl-convert-overview.md" >}}

1. جدیدترین انتشار را با این دستور دانلود کنید:

   ```powershell
   curl.exe -LO "https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kubectl-convert.exe"
   ```

1. فایل باینری را اعتبارسنجی کنید (اختیاری).

   فایل checksum مربوط به `kubectl-convert` را دانلود کنید:

   ```powershell
   curl.exe -LO "https://dl.k8s.io/v{{< skew currentPatchVersion >}}/bin/windows/amd64/kubectl-convert.exe.sha256"
   ```

   فایل باینری `kubectl-convert` را با فایل checksum اعتبارسنجی کنید:

   - با استفاده از Command Prompt و مقایسهٔ دستی خروجی `CertUtil` با فایل checksum دانلودشده:

     ```cmd
     CertUtil -hashfile kubectl-convert.exe SHA256
     type kubectl-convert.exe.sha256
     ```

   - با استفاده از PowerShell و خودکارسازی بررسی با عملگر `-eq` برای دریافت نتیجهٔ
     `True` یا `False`:

     ```powershell
     $($(CertUtil -hashfile .\kubectl-convert.exe SHA256)[1] -replace " ", "") -eq $(type .\kubectl-convert.exe.sha256)
     ```

1. پوشهٔ فایل باینری `kubectl-convert` را به انتها یا ابتدای متغیر محیطی `PATH` خود اضافه کنید.

1. بررسی کنید که افزونه با موفقیت نصب شده باشد.

   ```shell
   kubectl convert --help
   ```

   اگر خطایی مشاهده نکردید، یعنی افزونه با موفقیت نصب شده است.

1. پس از نصب افزونه، فایل‌های نصب را پاک کنید:

   ```powershell
   del kubectl-convert.exe
   del kubectl-convert.exe.sha256
   ```

## {{% heading "whatsnext" %}}

{{< include "included/kubectl-whats-next.md" >}}
