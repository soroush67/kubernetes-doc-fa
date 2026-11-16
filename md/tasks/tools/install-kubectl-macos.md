---
reviewers:
- mikedanese
title: نصب و راه‌اندازی kubectl در macOS
content_type: task
weight: 10
---

## {{% heading "prerequisites" %}}

نسخهٔ kubectl شما باید حداکثر یک نسخهٔ فرعی (minor) با نسخهٔ کلاستر اختلاف داشته باشد.
برای مثال، کلاینت v{{< skew currentVersion >}} می‌تواند با control plane نسخه‌های
v{{< skew currentVersionAddMinor -1 >}}، v{{< skew currentVersionAddMinor 0 >}}
و v{{< skew currentVersionAddMinor 1 >}} ارتباط برقرار کند.
استفاده از آخرین نسخهٔ سازگار kubectl به پیشگیری از مشکلات پیش‌بینی‌نشده کمک می‌کند.

## نصب kubectl در macOS

برای نصب kubectl در macOS روش‌های زیر وجود دارد:

- [نصب kubectl در macOS](#install-kubectl-on-macos)
  - [نصب فایل باینری kubectl با curl در macOS](#install-kubectl-binary-with-curl-on-macos)
  - [نصب با Homebrew در macOS](#install-with-homebrew-on-macos)
  - [نصب با Macports در macOS](#install-with-macports-on-macos)
- [بررسی پیکربندی kubectl](#verify-kubectl-configuration)
- [پیکربندی‌ها و افزونه‌های اختیاری kubectl](#optional-kubectl-configurations-and-plugins)
  - [فعال‌سازی تکمیل خودکار در شل](#enable-shell-autocompletion)
  - [نصب افزونهٔ `kubectl convert`](#install-kubectl-convert-plugin)

### نصب فایل باینری kubectl با curl در macOS

1. آخرین نسخهٔ منتشرشده را دانلود کنید:

   {{< tabs name="download_binary_macos" >}}
   {{< tab name="Intel" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
   {{< /tab >}}
   {{< tab name="Apple Silicon" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
   {{< /tab >}}
   {{< /tabs >}}

   {{< note >}}
   برای دانلود یک نسخهٔ مشخص، بخش `$(curl -L -s https://dl.k8s.io/release/stable.txt)`
   را در فرمان با شمارهٔ آن نسخه جایگزین کنید.

   برای مثال، برای دانلود نسخهٔ {{< skew currentPatchVersion >}} در macOS مبتنی بر Intel، فرمان زیر را وارد کنید:

   ```bash
   curl -LO "https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/darwin/amd64/kubectl"
   ```

   و برای macOS مبتنی بر Apple Silicon، فرمان زیر را وارد کنید:

   ```bash
   curl -LO "https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/darwin/arm64/kubectl"
   ```

   {{< /note >}}

1. اعتبارسنجی فایل باینری (اختیاری)

   فایل checksum مربوط به kubectl را دانلود کنید:

   {{< tabs name="download_checksum_macos" >}}
   {{< tab name="Intel" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl.sha256"
   {{< /tab >}}
   {{< tab name="Apple Silicon" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl.sha256"
   {{< /tab >}}
   {{< /tabs >}}
  
   فایل باینری kubectl را با فایل checksum اعتبارسنجی کنید:

   ```bash
   echo "$(cat kubectl.sha256)  kubectl" | shasum -a 256 --check
   ```

   اگر فایل معتبر باشد، خروجی چنین است:

   ```console
   kubectl: OK
   ```

   اگر بررسی ناموفق باشد، `shasum` با وضعیت غیرصفر خارج می‌شود و خروجی‌ای مشابه زیر چاپ می‌کند:

   ```console
   kubectl: FAILED
   shasum: WARNING: 1 computed checksum did NOT match
   ```

   {{< note >}}
   فایل باینری و فایل checksum را با نسخهٔ یکسان دانلود کنید.
   {{< /note >}}

1. فایل باینری kubectl را اجرایی کنید.

   ```bash
   chmod +x ./kubectl
   ```

1. فایل باینری kubectl را به مسیری منتقل کنید که در `PATH` سیستم شما قرار دارد.

   ```bash
   sudo mv ./kubectl /usr/local/bin/kubectl
   sudo chown root: /usr/local/bin/kubectl
   ```

   {{< note >}}
   مطمئن شوید که مسیر `/usr/local/bin` در متغیر محیطی PATH شما وجود دارد.
   {{< /note >}}

1. بررسی کنید که نسخهٔ نصب‌شده به‌روز باشد:

   ```bash
   kubectl version --client
   ```
   
   یا برای مشاهدهٔ جزئیات نسخه از فرمان زیر استفاده کنید:

   ```cmd
   kubectl version --client --output=yaml
   ```

1. پس از نصب و اعتبارسنجی kubectl، فایل checksum را حذف کنید:

   ```bash
   rm kubectl.sha256
   ```

### نصب با Homebrew در macOS

اگر از macOS و مدیر بستهٔ [Homebrew](https://brew.sh/) استفاده می‌کنید،
می‌توانید kubectl را با Homebrew نصب کنید.

1. فرمان نصب را اجرا کنید:

   ```bash
   brew install kubectl
   ```

   یا

   ```bash
   brew install kubernetes-cli
   ```

1. بررسی کنید که نسخهٔ نصب‌شده به‌روز باشد:

   ```bash
   kubectl version --client
   ```

### نصب با Macports در macOS

اگر از macOS و مدیر بستهٔ [Macports](https://macports.org/) استفاده می‌کنید،
می‌توانید kubectl را با Macports نصب کنید.

1. فرمان نصب را اجرا کنید:

   ```bash
   sudo port selfupdate
   sudo port install kubectl
   ```

1. بررسی کنید که نسخهٔ نصب‌شده به‌روز باشد:

   ```bash
   kubectl version --client
   ```

## بررسی پیکربندی kubectl

{{< include "included/verify-kubectl.md" >}}

## پیکربندی‌ها و افزونه‌های اختیاری kubectl

### فعال‌سازی تکمیل خودکار در شل

ابزار kubectl از تکمیل خودکار (autocompletion) برای Bash، Zsh، Fish و PowerShell
پشتیبانی می‌کند که می‌تواند در تایپ کردن صرفه‌جویی زیادی ایجاد کند.

در ادامه، مراحل راه‌اندازی تکمیل خودکار برای Bash، Fish و Zsh آمده است.

{{< tabs name="kubectl_autocompletion" >}}
{{< tab name="Bash" include="included/optional-kubectl-configs-bash-mac.md" />}}
{{< tab name="Fish" include="included/optional-kubectl-configs-fish.md" />}}
{{< tab name="Zsh" include="included/optional-kubectl-configs-zsh.md" />}}
{{< /tabs >}}

### پیکربندی kuberc

برای اطلاعات بیشتر، [kuberc](/docs/reference/kubectl/kuberc) را ببینید.

### نصب افزونهٔ `kubectl convert`

{{< include "included/kubectl-convert-overview.md" >}}

1. آخرین نسخهٔ منتشرشده را با فرمان زیر دانلود کنید:

   {{< tabs name="download_convert_binary_macos" >}}
   {{< tab name="Intel" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert"
   {{< /tab >}}
   {{< tab name="Apple Silicon" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert"
   {{< /tab >}}
   {{< /tabs >}}

1. اعتبارسنجی فایل باینری (اختیاری)

   فایل checksum مربوط به kubectl-convert را دانلود کنید:

   {{< tabs name="download_convert_checksum_macos" >}}
   {{< tab name="Intel" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl-convert.sha256"
   {{< /tab >}}
   {{< tab name="Apple Silicon" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl-convert.sha256"
   {{< /tab >}}
   {{< /tabs >}}

   فایل باینری kubectl-convert را با فایل checksum اعتبارسنجی کنید:

   ```bash
   echo "$(cat kubectl-convert.sha256)  kubectl-convert" | shasum -a 256 --check
   ```

   اگر فایل معتبر باشد، خروجی چنین است:

   ```console
   kubectl-convert: OK
   ```

   اگر بررسی ناموفق باشد، `shasum` با وضعیت غیرصفر خارج می‌شود و خروجی‌ای مشابه زیر چاپ می‌کند:

   ```console
   kubectl-convert: FAILED
   shasum: WARNING: 1 computed checksum did NOT match
   ```

   {{< note >}}
   فایل باینری و فایل checksum را با نسخهٔ یکسان دانلود کنید.
   {{< /note >}}

1. فایل باینری kubectl-convert را اجرایی کنید

   ```bash
   chmod +x ./kubectl-convert
   ```

1. فایل باینری kubectl-convert را به مسیری منتقل کنید که در `PATH` سیستم شما قرار دارد.

   ```bash
   sudo mv ./kubectl-convert /usr/local/bin/kubectl-convert
   sudo chown root: /usr/local/bin/kubectl-convert
   ```

   {{< note >}}
   مطمئن شوید که مسیر `/usr/local/bin` در متغیر محیطی PATH شما وجود دارد.
   {{< /note >}}

1. بررسی کنید که افزونه با موفقیت نصب شده باشد

   ```shell
   kubectl convert --help
   ```

   اگر با خطایی روبه‌رو نشدید، یعنی افزونه با موفقیت نصب شده است.

1. پس از نصب افزونه، فایل‌های نصب را پاک کنید:

   ```bash
   rm kubectl-convert kubectl-convert.sha256
   ```

### حذف kubectl در macOS

بسته به روشی که `kubectl` را نصب کرده‌اید، از یکی از روش‌های زیر استفاده کنید.

### حذف kubectl با خط فرمان

1.  محل فایل باینری `kubectl` را در سیستم خود پیدا کنید:

    ```bash
    which kubectl
    ```

1.  فایل باینری `kubectl` را حذف کنید:

    ```bash
    sudo rm <path>
    ```
    به‌جای `<path>` مسیر فایل باینری `kubectl` را که در مرحلهٔ قبل به دست آوردید قرار دهید. برای مثال: `sudo rm /usr/local/bin/kubectl`.

### حذف kubectl با Homebrew

اگر `kubectl` را با Homebrew نصب کرده‌اید، فرمان زیر را اجرا کنید:

```bash
brew remove kubectl
```
  
## {{% heading "whatsnext" %}}

{{< include "included/kubectl-whats-next.md" >}}
