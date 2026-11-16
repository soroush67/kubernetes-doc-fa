---
reviewers:
- mikedanese
title: نصب و راه‌اندازی kubectl روی لینوکس
content_type: task
weight: 10
---

## {{% heading "prerequisites" %}}

نسخهٔ kubectl شما باید حداکثر یک نسخهٔ فرعی (minor) با نسخهٔ کلاستر اختلاف داشته باشد. برای مثال، یک کلاینت v{{< skew currentVersion >}} می‌تواند با control plane نسخه‌های v{{< skew currentVersionAddMinor -1 >}}، v{{< skew currentVersionAddMinor 0 >}} و v{{< skew currentVersionAddMinor 1 >}} ارتباط برقرار کند.
استفاده از جدیدترین نسخهٔ سازگار kubectl از بروز مشکلات پیش‌بینی‌نشده جلوگیری می‌کند.

## نصب kubectl روی لینوکس

برای نصب kubectl روی لینوکس، روش‌های زیر وجود دارد:

- [نصب فایل اجرایی kubectl با curl روی لینوکس](#install-kubectl-binary-with-curl-on-linux)
- [نصب با مدیر بستهٔ بومی سیستم‌عامل](#install-using-native-package-management)
- [نصب با سایر مدیران بسته](#install-using-other-package-management)

### نصب فایل اجرایی kubectl با curl روی لینوکس

1. آخرین نسخهٔ منتشرشده را با دستور زیر دانلود کنید:

   {{< tabs name="download_binary_linux" >}}
   {{< tab name="x86-64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   {{< /tab >}}
   {{< tab name="ARM64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
   {{< /tab >}}
   {{< /tabs >}}

   {{< note >}}
   برای دانلود یک نسخهٔ مشخص، بخش `$(curl -L -s https://dl.k8s.io/release/stable.txt)`
   را در دستور با شمارهٔ نسخهٔ موردنظر جایگزین کنید.

   برای مثال، برای دانلود نسخهٔ {{< skew currentPatchVersion >}} روی لینوکس x86-64، دستور زیر را وارد کنید:

   ```bash
   curl -LO https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/linux/amd64/kubectl
   ```

   و برای لینوکس ARM64، دستور زیر را وارد کنید:

   ```bash
   curl -LO https://dl.k8s.io/release/v{{< skew currentPatchVersion >}}/bin/linux/arm64/kubectl
   ```

   {{< /note >}}

1. اعتبارسنجی فایل اجرایی (اختیاری)

   فایل checksum مربوط به kubectl را دانلود کنید:

   {{< tabs name="download_checksum_linux" >}}
   {{< tab name="x86-64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
   {{< /tab >}}
   {{< tab name="ARM64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl.sha256"
   {{< /tab >}}
   {{< /tabs >}}

   فایل اجرایی kubectl را با فایل checksum اعتبارسنجی کنید:

   ```bash
   echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
   ```

   اگر فایل معتبر باشد، خروجی به این صورت است:

   ```console
   kubectl: OK
   ```

   اگر بررسی ناموفق باشد، دستور `sha256` با وضعیت غیرصفر خاتمه می‌یابد و خروجی‌ای مشابه زیر چاپ می‌کند:

   ```console
   kubectl: FAILED
   sha256sum: WARNING: 1 computed checksum did NOT match
   ```

   {{< note >}}
   فایل اجرایی و فایل checksum را از یک نسخه دانلود کنید.
   {{< /note >}}

1. نصب kubectl

   ```bash
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
   ```

   {{< note >}}
   اگر روی سیستم مقصد دسترسی root ندارید، همچنان می‌توانید kubectl را در پوشهٔ
   `~/.local/bin` نصب کنید:

   ```bash
   chmod +x kubectl
   mkdir -p ~/.local/bin
   mv ./kubectl ~/.local/bin/kubectl
   # and then append (or prepend) ~/.local/bin to $PATH
   ```

   {{< /note >}}

1. بررسی کنید که نسخهٔ نصب‌شده به‌روز باشد:

   ```bash
   kubectl version --client
   ```

   یا برای مشاهدهٔ جزئیات نسخه از این دستور استفاده کنید:

   ```cmd
   kubectl version --client --output=yaml
   ```

### نصب با مدیر بستهٔ بومی سیستم‌عامل

{{< tabs name="kubectl_install" >}}
{{% tab name="توزیع‌های مبتنی بر Debian" %}}

1. فهرست بسته‌های `apt` را به‌روزرسانی کنید و بسته‌های لازم برای استفاده از مخزن `apt` کوبرنتیز را نصب کنید:

   ```shell
   sudo apt-get update
   # apt-transport-https may be a dummy package; if so, you can skip that package
   sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
   ```

2. کلید عمومی امضای مخازن بستهٔ کوبرنتیز را دانلود کنید. همهٔ مخازن از یک کلید امضای یکسان استفاده می‌کنند؛ بنابراین می‌توانید نسخهٔ درج‌شده در URL را نادیده بگیرید:

   ```shell
   # If the folder `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
   # sudo mkdir -p -m 755 /etc/apt/keyrings
   curl -fsSL https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
   ```
   
{{< note >}}
در نسخه‌های قدیمی‌تر از Debian 12 و Ubuntu 22.04، پوشهٔ `/etc/apt/keyrings` به‌طور پیش‌فرض وجود ندارد و باید پیش از اجرای دستور curl ساخته شود.
{{< /note >}}

3. مخزن `apt` مناسب کوبرنتیز را اضافه کنید. اگر می‌خواهید از نسخه‌ای از کوبرنتیز غیر از {{< param "version" >}} استفاده کنید،
   در دستور زیر {{< param "version" >}} را با نسخهٔ فرعی موردنظر جایگزین کنید:

   ```shell
   # This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
   ```

{{< note >}}
برای ارتقای kubectl به یک نسخهٔ فرعی دیگر، باید پیش از اجرای `apt-get update` و `apt-get upgrade`، نسخهٔ درج‌شده در `/etc/apt/sources.list.d/kubernetes.list` را تغییر دهید. این فرایند در [تغییر مخزن بستهٔ کوبرنتیز](/docs/tasks/administer-cluster/kubeadm/change-package-repository/) با جزئیات بیشتری شرح داده شده است.
{{< /note >}}

4. فهرست بسته‌های `apt` را به‌روزرسانی کنید و سپس kubectl را نصب کنید:

   ```shell
   sudo apt-get update
   sudo apt-get install -y kubectl
   ```

{{% /tab %}}

{{% tab name="توزیع‌های مبتنی بر Red Hat" %}}

1. مخزن `yum` کوبرنتیز را اضافه کنید. اگر می‌خواهید از نسخه‌ای از کوبرنتیز
   غیر از {{< param "version" >}} استفاده کنید، در دستور زیر {{< param "version" >}} را
   با نسخهٔ فرعی موردنظر جایگزین کنید.

   ```bash
   # This overwrites any existing configuration in /etc/yum.repos.d/kubernetes.repo
   cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/repodata/repomd.xml.key
   EOF
   ```

{{< note >}}
برای ارتقای kubectl به یک نسخهٔ فرعی دیگر، باید پیش از اجرای `dnf update`، نسخهٔ درج‌شده در `/etc/yum.repos.d/kubernetes.repo` را تغییر دهید. این فرایند در [تغییر مخزن بستهٔ کوبرنتیز](/docs/tasks/administer-cluster/kubeadm/change-package-repository/) با جزئیات بیشتری شرح داده شده است.
{{< /note >}}

2. ابزار kubectl را با `dnf` نصب کنید:

   ```bash
   sudo dnf install -y kubectl
   ```

{{% /tab %}}

{{% tab name="توزیع‌های مبتنی بر SUSE" %}}

1. مخزن `zypper` کوبرنتیز را اضافه کنید. اگر می‌خواهید از نسخه‌ای از کوبرنتیز
   غیر از {{< param "version" >}} استفاده کنید، در دستور زیر {{< param "version" >}} را
   با نسخهٔ فرعی موردنظر جایگزین کنید.

   ```bash
   # This overwrites any existing configuration in /etc/zypp/repos.d/kubernetes.repo
   cat <<EOF | sudo tee /etc/zypp/repos.d/kubernetes.repo
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/repodata/repomd.xml.key
   EOF
   ```

{{< note >}}
برای ارتقای kubectl به یک نسخهٔ فرعی دیگر، باید پیش از اجرای `zypper update`،
نسخهٔ درج‌شده در `/etc/zypp/repos.d/kubernetes.repo` را تغییر دهید. این فرایند در
[تغییر مخزن بستهٔ کوبرنتیز](/docs/tasks/administer-cluster/kubeadm/change-package-repository/) با جزئیات بیشتری شرح داده شده است.
{{< /note >}}

2. ابزار `zypper` را به‌روزرسانی کنید و افزوده‌شدن مخزن جدید را تأیید کنید:
   
   ```bash
   sudo zypper update
   ```

   هنگامی که پیام زیر نمایش داده شد، کلید 't' یا 'a' را فشار دهید:

   ```
   New repository or package signing key received:

   Repository:       Kubernetes
   Key Fingerprint:  1111 2222 3333 4444 5555 6666 7777 8888 9999 AAAA
   Key Name:         isv:kubernetes OBS Project <isv:kubernetes@build.opensuse.org>
   Key Algorithm:    RSA 2048
   Key Created:      Thu 25 Aug 2022 01:21:11 PM -03
   Key Expires:      Sat 02 Nov 2024 01:21:11 PM -03 (expires in 85 days)
   Rpm Name:         gpg-pubkey-9a296436-6307a177

   Note: Signing data enables the recipient to verify that no modifications occurred after the data
   were signed. Accepting data with no, wrong or unknown signature can lead to a corrupted system
   and in extreme cases even to a system compromise.

   Note: A GPG pubkey is clearly identified by its fingerprint. Do not rely on the key's name. If
   you are not sure whether the presented key is authentic, ask the repository provider or check
   their web site. Many providers maintain a web page showing the fingerprints of the GPG keys they
   are using.

   Do you want to reject the key, trust temporarily, or trust always? [r/t/a/?] (r): a
   ```
   
3. ابزار kubectl را با `zypper` نصب کنید:

   ```bash
   sudo zypper install -y kubectl
   ```

{{% /tab %}}
{{< /tabs >}}

### نصب با سایر مدیران بسته

{{< tabs name="other_kubectl_install" >}}
{{% tab name="Snap" %}}
اگر از Ubuntu یا توزیع لینوکس دیگری استفاده می‌کنید که از مدیر بستهٔ
[snap](https://snapcraft.io/docs/core/install) پشتیبانی می‌کند، kubectl
به‌صورت یک برنامهٔ [snap](https://snapcraft.io/) در دسترس است.

```shell
snap install kubectl --classic
kubectl version --client
```

{{% /tab %}}

{{% tab name="Homebrew" %}}
اگر روی لینوکس از مدیر بستهٔ [Homebrew](https://docs.brew.sh/Homebrew-on-Linux)
استفاده می‌کنید، kubectl از این طریق قابل [نصب](https://docs.brew.sh/Homebrew-on-Linux#install) است.

```shell
brew install kubectl
kubectl version --client
```

{{% /tab %}}

{{< /tabs >}}

## بررسی پیکربندی kubectl

{{< include "included/verify-kubectl.md" >}}

## پیکربندی‌ها و افزونه‌های اختیاری kubectl

### فعال‌سازی تکمیل خودکار در پوسته

ابزار kubectl از تکمیل خودکار (autocompletion) برای Bash، Zsh، Fish و PowerShell پشتیبانی می‌کند
که می‌تواند حجم تایپ شما را به‌طور چشمگیری کاهش دهد.

در ادامه، روش راه‌اندازی تکمیل خودکار برای Bash، Fish و Zsh آمده است.

{{< tabs name="kubectl_autocompletion" >}}
{{< tab name="Bash" include="included/optional-kubectl-configs-bash-linux.md" />}}
{{< tab name="Fish" include="included/optional-kubectl-configs-fish.md" />}}
{{< tab name="Zsh" include="included/optional-kubectl-configs-zsh.md" />}}
{{< /tabs >}}

### پیکربندی kuberc

برای اطلاعات بیشتر، [kuberc](/docs/reference/kubectl/kuberc) را ببینید.

### نصب افزونهٔ `kubectl convert`

{{< include "included/kubectl-convert-overview.md" >}}

1. آخرین نسخهٔ منتشرشده را با دستور زیر دانلود کنید:

   {{< tabs name="download_convert_binary_linux" >}}
   {{< tab name="x86-64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert"
   {{< /tab >}}
   {{< tab name="ARM64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl-convert"
   {{< /tab >}}
   {{< /tabs >}}

1. اعتبارسنجی فایل اجرایی (اختیاری)

   فایل checksum مربوط به kubectl-convert را دانلود کنید:

   {{< tabs name="download_convert_checksum_linux" >}}
   {{< tab name="x86-64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert.sha256"
   {{< /tab >}}
   {{< tab name="ARM64" codelang="bash" >}}
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl-convert.sha256"
   {{< /tab >}}
   {{< /tabs >}}

   فایل اجرایی kubectl-convert را با فایل checksum اعتبارسنجی کنید:

   ```bash
   echo "$(cat kubectl-convert.sha256) kubectl-convert" | sha256sum --check
   ```

   اگر فایل معتبر باشد، خروجی به این صورت است:

   ```console
   kubectl-convert: OK
   ```

   اگر بررسی ناموفق باشد، دستور `sha256` با وضعیت غیرصفر خاتمه می‌یابد و خروجی‌ای مشابه زیر چاپ می‌کند:

   ```console
   kubectl-convert: FAILED
   sha256sum: WARNING: 1 computed checksum did NOT match
   ```

   {{< note >}}
   فایل اجرایی و فایل checksum را از یک نسخه دانلود کنید.
   {{< /note >}}

1. نصب kubectl-convert

   ```bash
   sudo install -o root -g root -m 0755 kubectl-convert /usr/local/bin/kubectl-convert
   ```

1. بررسی کنید که افزونه با موفقیت نصب شده باشد

   ```shell
   kubectl convert --help
   ```

   اگر خطایی مشاهده نکردید، یعنی افزونه با موفقیت نصب شده است.

1. پس از نصب افزونه، فایل‌های نصب را پاک کنید:

   ```bash
   rm kubectl-convert kubectl-convert.sha256
   ```

## {{% heading "whatsnext" %}}

{{< include "included/kubectl-whats-next.md" >}}
