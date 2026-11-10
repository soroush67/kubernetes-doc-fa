---
title: نصب kubeadm
content_type: task
weight: 10
card:
  name: setup
  weight: 40
  title: نصب ابزار راه‌اندازی kubeadm
---

<!-- overview -->

<img src="/images/kubeadm-stacked-color.png" align="right" width="150px"></img>
این صفحه نحوهٔ نصب جعبه‌ابزار `kubeadm` را نشان می‌دهد.
برای آشنایی با نحوهٔ ایجاد یک کلاستر با kubeadm پس از انجام این فرایند نصب،
صفحهٔ [ایجاد کلاستر با kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) را ببینید.

{{< doc-versions-list "installation guide" >}}

## {{% heading "prerequisites" %}}

* یک میزبان لینوکسی سازگار. پروژهٔ کوبرنتیز دستورالعمل‌های عمومی‌ای برای توزیع‌های لینوکس مبتنی بر
  Debian و Red Hat و نیز توزیع‌های فاقد مدیر بسته ارائه می‌کند.
* حداقل ۲ گیگابایت RAM برای هر ماشین (مقدار کمتر از این، فضای اندکی برای برنامه‌هایتان باقی می‌گذارد).
* حداقل ۲ CPU برای ماشین‌های control plane.
* اتصال شبکهٔ کامل میان همهٔ ماشین‌های کلاستر (شبکهٔ عمومی یا خصوصی، هر دو مناسب است).
* نام میزبان، نشانی MAC و product_uuid یکتا برای هر نود. برای جزئیات بیشتر [اینجا](#verify-mac-address) را ببینید.
* برخی پورت‌ها روی ماشین‌هایتان باز باشند. برای جزئیات بیشتر [اینجا](#check-required-ports) را ببینید.

{{< note >}}
نصب `kubeadm` با فایل‌های باینری‌ای انجام می‌شود که از پیوند پویا (dynamic linking) استفاده می‌کنند و فرض بر این است که سیستم مقصد شما `glibc` را فراهم می‌کند.
این فرض در بسیاری از توزیع‌های لینوکس (از جمله Debian، Ubuntu، Fedora، CentOS و غیره) معقول است،
اما در توزیع‌های سفارشی و سبک که به‌طور پیش‌فرض `glibc` را ندارند، مانند Alpine Linux، همیشه صادق نیست.
انتظار می‌رود توزیع یا `glibc` را داشته باشد یا یک
[لایهٔ سازگاری](https://wiki.alpinelinux.org/wiki/Running_glibc_programs)
داشته باشد که نمادهای مورد انتظار را فراهم کند.
{{< /note >}}

<!-- steps -->

## بررسی نسخهٔ سیستم‌عامل

{{% thirdparty-content %}}

{{< tabs name="operating_system_version_check" >}}
{{% tab name="Linux" %}}

* پروژهٔ kubeadm از کرنل‌های LTS پشتیبانی می‌کند. [فهرست کرنل‌های LTS](https://www.kernel.org/category/releases.html) را ببینید.
* می‌توانید نسخهٔ کرنل را با فرمان `uname -r` به دست آورید.

برای اطلاعات بیشتر، [الزامات کرنل لینوکس](/docs/reference/node/kernel-version-requirements/) را ببینید.

{{% /tab %}}

{{% tab name="Windows" %}}

* پروژهٔ kubeadm از نسخه‌های اخیر کرنل پشتیبانی می‌کند. برای فهرست کرنل‌های اخیر، [اطلاعات انتشار Windows Server](https://learn.microsoft.com/en-us/windows/release-health/windows-server-release-info) را ببینید.
* می‌توانید نسخهٔ کرنل (که نسخهٔ سیستم‌عامل نیز نامیده می‌شود) را با فرمان `systeminfo` به دست آورید.

برای اطلاعات بیشتر، [سازگاری نسخهٔ سیستم‌عامل Windows](/docs/concepts/windows/intro/#windows-os-version-support) را ببینید.

{{% /tab %}}
{{< /tabs >}}

هر کلاستر کوبرنتیز که با kubeadm ایجاد شود، به نرم‌افزارهایی وابسته است که از قابلیت‌های کرنل استفاده می‌کنند.
این نرم‌افزارها عبارت‌اند از
{{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}}،
{{< glossary_tooltip term_id="kubelet" text="kubelet">}} و یک افزونهٔ {{< glossary_tooltip text="رابط شبکهٔ کانتینر" term_id="cni" >}}، اما به این موارد محدود نمی‌شوند.

برای اینکه از خطاهای غیرمنتظره ناشی از نسخهٔ پشتیبانی‌نشدهٔ کرنل در امان بمانید، kubeadm بررسی پیش از اجرای
`SystemVerification` را انجام می‌دهد. اگر نسخهٔ کرنل پشتیبانی نشود، این بررسی ناموفق خواهد بود.

اگر می‌دانید کرنل شما قابلیت‌های لازم را فراهم می‌کند، می‌توانید این بررسی را نادیده بگیرید،
حتی اگر kubeadm از نسخهٔ آن پشتیبانی نکند.

## اطمینان از یکتا بودن نشانی MAC و product_uuid برای هر نود {#verify-mac-address}

* می‌توانید نشانی MAC رابط‌های شبکه را با فرمان `ip link` یا `ifconfig -a` به دست آورید.
* مقدار product_uuid را می‌توان با فرمان `sudo cat /sys/class/dmi/id/product_uuid` بررسی کرد.

به احتمال بسیار زیاد، دستگاه‌های سخت‌افزاری نشانی‌های یکتایی دارند، هرچند برخی ماشین‌های مجازی ممکن است
مقادیر یکسانی داشته باشند. کوبرنتیز از این مقادیر برای شناسایی یکتای نودهای کلاستر استفاده می‌کند.
اگر این مقادیر برای هر نود یکتا نباشند، ممکن است فرایند نصب
[با شکست مواجه شود](https://github.com/kubernetes/kubeadm/issues/31).

## بررسی آداپتورهای شبکه

اگر بیش از یک آداپتور شبکه دارید و اجزای کوبرنتیز از طریق مسیر پیش‌فرض در دسترس نیستند،
توصیه می‌کنیم مسیر (یا مسیرهای) IP اضافه کنید تا نشانی‌های کلاستر کوبرنتیز از آداپتور مناسب عبور کنند.

## بررسی پورت‌های لازم {#check-required-ports}

این [پورت‌های لازم](/docs/reference/networking/ports-and-protocols/)
باید باز باشند تا اجزای کوبرنتیز بتوانند با یکدیگر ارتباط برقرار کنند.
برای بررسی باز بودن یک پورت می‌توانید از ابزارهایی مانند [netcat](https://netcat.sourceforge.net) استفاده کنید. برای مثال:

```shell
nc 127.0.0.1 6443 -zv -w 2
```

افزونهٔ شبکهٔ پادی که استفاده می‌کنید نیز ممکن است به باز بودن برخی پورت‌ها نیاز داشته باشد.
از آنجا که این موضوع در هر افزونهٔ شبکهٔ پاد متفاوت است، لطفاً برای اطلاع از پورت‌های مورد نیاز،
مستندات آن افزونه‌ها را ببینید.

## پیکربندی swap {#swap-configuration}

رفتار پیش‌فرض kubelet این است که اگر حافظهٔ swap روی نود شناسایی شود، اجرا نشود.
این یعنی swap یا باید غیرفعال شود یا kubelet آن را تحمل کند.

* برای تحمل swap، `failSwapOn: false` را به پیکربندی kubelet یا به‌صورت آرگومان خط فرمان اضافه کنید.
  توجه: حتی اگر `failSwapOn: false` تنظیم شده باشد، بارهای کاری به‌طور پیش‌فرض به swap دسترسی نخواهند داشت.
  این رفتار را می‌توان با تنظیم `swapBehavior`، باز هم در فایل پیکربندی kubelet، تغییر داد. برای استفاده از swap،
  مقداری غیر از تنظیم پیش‌فرض `NoSwap` برای `swapBehavior` تعیین کنید.
  برای جزئیات بیشتر، [مدیریت حافظهٔ swap](/docs/concepts/cluster-administration/swap-memory-management) را ببینید.
* برای غیرفعال کردن swap، می‌توان از `sudo swapoff -a` استفاده کرد تا swap به‌طور موقت غیرفعال شود.
  برای اینکه این تغییر پس از راه‌اندازی مجدد نیز باقی بماند، بسته به نحوهٔ پیکربندی سیستمتان، مطمئن شوید
  swap در فایل‌های پیکربندی مانند `/etc/fstab` و `systemd.swap` غیرفعال شده است.


## نصب محیط اجرای کانتینر {#installing-runtime}

کوبرنتیز برای اجرای کانتینرها در Podها از یک
{{< glossary_tooltip term_id="container-runtime" text="محیط اجرای کانتینر" >}} استفاده می‌کند.

کوبرنتیز به‌طور پیش‌فرض از
{{< glossary_tooltip term_id="cri" text="رابط محیط اجرای کانتینر">}} (CRI)
برای ارتباط با محیط اجرای کانتینر انتخابی شما استفاده می‌کند.

اگر محیط اجرایی را مشخص نکنید، kubeadm به‌طور خودکار تلاش می‌کند با پیمایش فهرستی از نقاط پایانی (endpoint) شناخته‌شده،
محیط اجرای کانتینر نصب‌شده را شناسایی کند.

اگر چند محیط اجرای کانتینر شناسایی شود یا هیچ‌کدام شناسایی نشود، kubeadm خطا می‌دهد
و از شما می‌خواهد مشخص کنید از کدام‌یک می‌خواهید استفاده کنید.

برای اطلاعات بیشتر، [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/)
را ببینید.

{{< note >}}
موتور Docker رابط [CRI](/docs/concepts/architecture/cri/) را پیاده‌سازی نمی‌کند،
درحالی‌که این رابط شرط لازم برای کار کردن یک محیط اجرای کانتینر با کوبرنتیز است.
به همین دلیل، باید سرویس دیگری به نام [cri-dockerd](https://mirantis.github.io/cri-dockerd/)
نصب شود. cri-dockerd پروژه‌ای است مبتنی بر پشتیبانی داخلی قدیمی از Docker Engine
که در نسخهٔ 1.24 از kubelet [حذف شد](/dockershim).
{{< /note >}}

جدول‌های زیر نقاط پایانی شناخته‌شده برای سیستم‌عامل‌های پشتیبانی‌شده را نشان می‌دهند:

{{< tabs name="container_runtime" >}}
{{% tab name="Linux" %}}

{{< table caption="محیط‌های اجرای کانتینر در لینوکس" >}}
| محیط اجرا                            | مسیر سوکت دامنهٔ Unix                   |
|------------------------------------|----------------------------------------------|
| containerd                         | `unix:///var/run/containerd/containerd.sock` |
| CRI-O                              | `unix:///var/run/crio/crio.sock`             |
| Docker Engine (با استفاده از cri-dockerd)  | `unix:///var/run/cri-dockerd.sock`           |
{{< /table >}}

{{% /tab %}}

{{% tab name="Windows" %}}

{{< table caption="محیط‌های اجرای کانتینر در Windows" >}}
| محیط اجرا                            | مسیر named pipe در Windows                   |
|------------------------------------|----------------------------------------------|
| containerd                         | `npipe:////./pipe/containerd-containerd`     |
| Docker Engine (با استفاده از cri-dockerd)  | `npipe:////./pipe/cri-dockerd`               |
{{< /table >}}

{{% /tab %}}
{{< /tabs >}}

## نصب kubeadm، kubelet و kubectl

این بسته‌ها را روی همهٔ ماشین‌هایتان نصب خواهید کرد:

* `kubeadm`: فرمانی برای راه‌اندازی اولیهٔ (bootstrap) کلاستر.

* `kubelet`: جزئی که روی همهٔ ماشین‌های کلاستر اجرا می‌شود
  و کارهایی مانند راه‌اندازی پادها و کانتینرها را انجام می‌دهد.

* `kubectl`: ابزار خط فرمان برای ارتباط با کلاستر.

kubeadm، `kubelet` یا `kubectl` را برای شما نصب یا مدیریت **نمی‌کند**؛ بنابراین باید
مطمئن شوید نسخهٔ آن‌ها با نسخهٔ control plane کوبرنتیزی که می‌خواهید kubeadm برایتان نصب کند مطابقت دارد.
در غیر این صورت، خطر ناهمخوانی نسخه‌ها (version skew) وجود دارد که
می‌تواند به رفتار غیرمنتظره و پرخطا منجر شود. با این حال، ناهمخوانی به اندازهٔ _یک_ نسخهٔ فرعی میان
kubelet و control plane پشتیبانی می‌شود، اما نسخهٔ kubelet هرگز نباید از نسخهٔ API server
بالاتر باشد. برای مثال، kubelet با نسخهٔ 1.7.0 باید کاملاً با API server نسخهٔ 1.8.0 سازگار باشد،
اما عکس آن صادق نیست.

برای اطلاعات دربارهٔ نصب `kubectl`، [نصب و راه‌اندازی kubectl](/docs/tasks/tools/) را ببینید.

{{< warning >}}
این دستورالعمل‌ها همهٔ بسته‌های کوبرنتیز را از هرگونه ارتقای سیستمی مستثنا می‌کنند.
دلیل این کار آن است که ارتقای kubeadm و کوبرنتیز به
[توجه ویژه‌ای](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) نیاز دارد.
{{</ warning >}}

برای اطلاعات بیشتر دربارهٔ ناهمخوانی نسخه‌ها، موارد زیر را ببینید:

* [سیاست نسخه‌بندی و ناهمخوانی نسخه‌ها](/docs/setup/release/version-skew-policy/) در کوبرنتیز
* [سیاست ناهمخوانی نسخه‌ها](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#version-skew-policy) مختص kubeadm

{{% legacy-repos-deprecation %}}

{{< note >}}
برای هر نسخهٔ فرعی کوبرنتیز یک مخزن بستهٔ اختصاصی وجود دارد. اگر می‌خواهید
نسخهٔ فرعی‌ای غیر از v{{< skew currentVersion >}} نصب کنید، لطفاً راهنمای نصب
نسخهٔ فرعی مورد نظرتان را ببینید.
{{< /note >}}

{{< tabs name="k8s_install" >}}
{{% tab name="توزیع‌های مبتنی بر Debian" %}}

این دستورالعمل‌ها برای کوبرنتیز v{{< skew currentVersion >}} است.

1. نمایهٔ بسته‌های `apt` را به‌روزرسانی کنید و بسته‌های لازم برای استفاده از مخزن `apt` کوبرنتیز را نصب کنید:

   ```shell
   sudo apt-get update
   # apt-transport-https may be a dummy package; if so, you can skip that package
   sudo apt-get install -y apt-transport-https ca-certificates curl gpg
   ```

2. کلید امضای عمومی مخازن بستهٔ کوبرنتیز را دانلود کنید.
   برای همهٔ مخازن از یک کلید امضای یکسان استفاده می‌شود؛ بنابراین می‌توانید نسخهٔ موجود در URL را نادیده بگیرید:

   ```shell
   # If the directory `/etc/apt/keyrings` does not exist, it should be created before the curl command, read the note below.
   # sudo mkdir -p -m 755 /etc/apt/keyrings
   curl -fsSL https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   ```

{{< note >}}
در نسخه‌های قدیمی‌تر از Debian 12 و Ubuntu 22.04، دایرکتوری `/etc/apt/keyrings` به‌طور پیش‌فرض
وجود ندارد و باید پیش از اجرای فرمان curl ایجاد شود.
{{< /note >}}

3. مخزن `apt` مناسب کوبرنتیز را اضافه کنید. لطفاً توجه کنید که این مخزن فقط بسته‌های
   کوبرنتیز {{< skew currentVersion >}} را دارد؛ برای سایر نسخه‌های فرعی کوبرنتیز، باید
   نسخهٔ فرعی کوبرنتیز را در URL به نسخهٔ فرعی مورد نظرتان تغییر دهید
   (همچنین باید بررسی کنید که مستندات مربوط به همان نسخه‌ای از کوبرنتیز را می‌خوانید
   که قصد نصب آن را دارید).

   ```shell
   # This overwrites any existing configuration in /etc/apt/sources.list.d/kubernetes.list
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   ```

4. نمایهٔ بسته‌های `apt` را به‌روزرسانی کنید، kubelet، kubeadm و kubectl را نصب کنید و نسخهٔ آن‌ها را ثابت نگه دارید:

   ```shell
   sudo apt-get update
   sudo apt-get install -y kubelet kubeadm kubectl
   sudo apt-mark hold kubelet kubeadm kubectl
   ```

5. (اختیاری) پیش از اجرای kubeadm، سرویس kubelet را فعال کنید:

   ```shell
   sudo systemctl enable --now kubelet
   ```

{{% /tab %}}
{{% tab name="توزیع‌های مبتنی بر Red Hat" %}}

1. حالت SELinux را روی `permissive` تنظیم کنید:

   این دستورالعمل‌ها برای کوبرنتیز {{< skew currentVersion >}} است.

   ```shell
   # Set SELinux in permissive mode (effectively disabling it)
   sudo setenforce 0
   sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
   ```

{{< caution >}}
- قرار دادن SELinux در حالت permissive با اجرای `setenforce 0` و `sed ...`
  در عمل آن را غیرفعال می‌کند. این کار لازم است تا کانتینرها بتوانند به فایل‌سیستم میزبان
  دسترسی داشته باشند؛ برای مثال، برخی افزونه‌های شبکهٔ کلاستر به این دسترسی نیاز دارند. تا زمانی که
  پشتیبانی از SELinux در kubelet بهبود نیابد، باید این کار را انجام دهید.
- اگر می‌دانید SELinux را چگونه پیکربندی کنید، می‌توانید آن را فعال نگه دارید، اما ممکن است
  به تنظیماتی نیاز داشته باشد که kubeadm از آن‌ها پشتیبانی نمی‌کند.
{{< /caution >}}

2. مخزن `yum` کوبرنتیز را اضافه کنید. پارامتر `exclude` در
   تعریف مخزن تضمین می‌کند که بسته‌های مرتبط با کوبرنتیز هنگام اجرای یک
   `dnf update` معمولی ارتقا نیابند، زیرا ارتقای کوبرنتیز روال ویژه‌ای دارد که
   باید از آن پیروی شود. لطفاً توجه کنید که این مخزن
   فقط بسته‌های کوبرنتیز {{< skew currentVersion >}} را دارد؛ برای سایر
   نسخه‌های فرعی کوبرنتیز، باید نسخهٔ فرعی کوبرنتیز را
   در URL به نسخهٔ فرعی مورد نظرتان تغییر دهید (همچنین باید بررسی کنید که
   مستندات مربوط به همان نسخه‌ای از کوبرنتیز را می‌خوانید که
   قصد نصب آن را دارید).

   ```shell
   # This overwrites any existing configuration in /etc/yum.repos.d/kubernetes.repo
   cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   EOF
   ```

3. kubelet، kubeadm و kubectl را نصب کنید:

   برای سیستم‌های دارای DNF4 (Fedora < 41، RHEL/CentOS < 10):
   ```shell
   sudo dnf install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
   ```
   برای سیستم‌های Fedora دارای DNF5:
   ```shell
   sudo dnf install -y kubelet kubeadm kubectl --setopt=disable_excludes=kubernetes
   ```

   برای RHEL/CentOS 10 و نسخه‌های بعدی، برای جلوگیری از نصب `iptables` به‌عنوان وابستگی:
   ```shell
   sudo dnf install -y kubelet kubeadm kubectl --setopt=disable_excludes=kubernetes --setopt=install_weak_deps=False
   ```

4. (اختیاری) پیش از اجرای kubeadm، سرویس kubelet را فعال کنید:

   ```shell
   sudo systemctl enable --now kubelet
   ```

{{% /tab %}}
{{% tab name="بدون مدیر بسته" %}}
افزونه‌های CNI را نصب کنید (برای بیشتر شبکه‌های پاد لازم است):

```bash
CNI_PLUGINS_VERSION="v1.3.0"
ARCH="amd64"
DEST="/opt/cni/bin"
sudo mkdir -p "$DEST"
curl -L "https://github.com/containernetworking/plugins/releases/download/${CNI_PLUGINS_VERSION}/cni-plugins-linux-${ARCH}-${CNI_PLUGINS_VERSION}.tgz" | sudo tar -C "$DEST" -xz
```

دایرکتوری دانلود فایل‌های فرمان را تعریف کنید:

{{< note >}}
متغیر `DOWNLOAD_DIR` باید روی یک دایرکتوری قابل‌نوشتن تنظیم شود.
اگر از Flatcar Container Linux استفاده می‌کنید، `DOWNLOAD_DIR="/opt/bin"` را تنظیم کنید.
{{< /note >}}

```bash
DOWNLOAD_DIR="/usr/local/bin"
sudo mkdir -p "$DOWNLOAD_DIR"
```

در صورت تمایل، crictl را نصب کنید (برای تعامل با رابط محیط اجرای کانتینر (CRI) لازم است و برای kubeadm اختیاری است):

```bash
CRICTL_VERSION="v1.31.0"
ARCH="amd64"
curl -L "https://github.com/kubernetes-sigs/cri-tools/releases/download/${CRICTL_VERSION}/crictl-${CRICTL_VERSION}-linux-${ARCH}.tar.gz" | sudo tar -C $DOWNLOAD_DIR -xz
```

`kubeadm` و `kubelet` را نصب کنید و یک سرویس systemd برای `kubelet` اضافه کنید:

```bash
RELEASE="$(curl -sSL https://dl.k8s.io/release/stable.txt)"
ARCH="amd64"
cd $DOWNLOAD_DIR
sudo curl -L --remote-name-all https://dl.k8s.io/release/${RELEASE}/bin/linux/${ARCH}/{kubeadm,kubelet}
sudo chmod +x {kubeadm,kubelet}

RELEASE_VERSION="v0.16.2"
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/krel/templates/latest/kubelet/kubelet.service" | sed "s:/usr/bin:${DOWNLOAD_DIR}:g" | sudo tee /usr/lib/systemd/system/kubelet.service
sudo mkdir -p /usr/lib/systemd/system/kubelet.service.d
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/krel/templates/latest/kubeadm/10-kubeadm.conf" | sed "s:/usr/bin:${DOWNLOAD_DIR}:g" | sudo tee /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
```

{{< note >}}
برای توزیع‌های لینوکسی که به‌طور پیش‌فرض `glibc` را ندارند، لطفاً به یادداشت بخش
[پیش از شروع](#before-you-begin) مراجعه کنید.
{{< /note >}}

برای نصب `kubectl`، دستورالعمل‌های [صفحهٔ نصب ابزارها](/docs/tasks/tools/#kubectl) را دنبال کنید.

در صورت تمایل، پیش از اجرای kubeadm، سرویس kubelet را فعال کنید:

```bash
sudo systemctl enable --now kubelet
```

{{< note >}}
توزیع Flatcar Container Linux دایرکتوری `/usr` را به‌صورت فایل‌سیستمی فقط‌خواندنی mount می‌کند.
پیش از راه‌اندازی اولیهٔ کلاستر، باید گام‌های بیشتری برای پیکربندی یک دایرکتوری قابل‌نوشتن بردارید.
برای آشنایی با نحوهٔ راه‌اندازی یک دایرکتوری قابل‌نوشتن، [راهنمای عیب‌یابی kubeadm](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/#usr-mounted-read-only)
را ببینید.
{{< /note >}}
{{% /tab %}}
{{< /tabs >}}

اکنون kubelet هر چند ثانیه یک بار راه‌اندازی مجدد می‌شود، زیرا در یک چرخهٔ خرابی (crashloop) منتظر می‌ماند
تا kubeadm به آن بگوید چه کاری انجام دهد.

## عیب‌یابی

اگر در کار با kubeadm با مشکل روبه‌رو شدید، لطفاً به
[مستندات عیب‌یابی](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/) ما مراجعه کنید.

## {{% heading "whatsnext" %}}

* [استفاده از kubeadm برای ایجاد کلاستر](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
