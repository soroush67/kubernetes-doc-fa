---
reviewers:
- vincepri
- bart0sh
title: محیط‌های اجرای کانتینر
content_type: concept
weight: 20
---
<!-- overview -->

{{% dockershim-removal %}}

برای اینکه Podها بتوانند روی هر نود کلاستر اجرا شوند، باید روی آن نود یک
{{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}}
نصب کنید. این صفحه مراحل لازم را به‌طور خلاصه شرح می‌دهد و کارهای مرتبط با راه‌اندازی نودها را توضیح می‌دهد.

کوبرنتیز {{< skew currentVersion >}} الزام می‌کند که از محیط اجرایی‌ای استفاده کنید که با
{{< glossary_tooltip term_id="cri" text="رابط محیط اجرای کانتینر">}} (CRI) سازگار باشد.

برای اطلاعات بیشتر، [پشتیبانی از نسخه‌های CRI](#cri-versions) را ببینید.

این صفحه نمای کلی نحوهٔ استفاده از چند محیط اجرای کانتینر رایج را در کنار کوبرنتیز ارائه می‌دهد.

- [containerd](#containerd)
- [CRI-O](#cri-o)
- [Docker Engine](#docker)
- [Mirantis Container Runtime](#mcr)

{{< note >}}
نسخه‌های کوبرنتیز پیش از v1.24 یکپارچگی مستقیمی با Docker Engine داشتند که از طریق مؤلفه‌ای به نام _dockershim_ انجام می‌شد. این یکپارچگی مستقیم و ویژه دیگر بخشی از کوبرنتیز نیست (حذف آن
[اعلام شد](/blog/2020/12/08/kubernetes-1-20-release-announcement/#dockershim-deprecation)
و بخشی از انتشار v1.20 بود).
برای اینکه بدانید این حذف ممکن است چه تأثیری بر شما داشته باشد، می‌توانید
[بررسی کنید که آیا حذف Dockershim بر شما اثر می‌گذارد](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
را بخوانید. برای آشنایی با مهاجرت از dockershim، به
[مهاجرت از dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/) مراجعه کنید.

اگر نسخه‌ای از کوبرنتیز به‌جز v{{< skew currentVersion >}} را اجرا می‌کنید،
مستندات همان نسخه را بررسی کنید.
{{< /note >}}

<!-- body -->
## نصب و پیکربندی پیش‌نیازها

### پیکربندی شبکه

هستهٔ لینوکس به‌طور پیش‌فرض اجازهٔ مسیریابی بسته‌های IPv4 بین رابط‌های شبکه را نمی‌دهد. بیشتر پیاده‌سازی‌های شبکهٔ کلاستر کوبرنتیز این تنظیم را (در صورت نیاز) تغییر می‌دهند، اما برخی ممکن است انتظار داشته باشند که مدیر سیستم این کار را انجام دهد. (برخی نیز ممکن است انتظار داشته باشند پارامترهای sysctl دیگری تنظیم شوند، ماژول‌های هسته بارگذاری شوند و مانند آن؛ برای این موارد به مستندات پیاده‌سازی شبکهٔ مورد نظر خود مراجعه کنید.)

### فعال‌سازی ارسال بسته‌های IPv4 {#prerequisite-ipv4-forwarding-optional}

برای فعال‌سازی دستی ارسال بسته‌های IPv4 (IPv4 packet forwarding):

```bash
# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

با دستور زیر بررسی کنید که مقدار `net.ipv4.ip_forward` برابر 1 باشد:

```bash
sysctl net.ipv4.ip_forward
```

## درایورهای cgroup

در لینوکس، از {{< glossary_tooltip text="گروه‌های کنترل" term_id="cgroup" >}}
برای محدود کردن منابعی استفاده می‌شود که به فرایندها تخصیص داده می‌شوند.

هم {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و هم محیط اجرای کانتینر زیرین باید با گروه‌های کنترل در ارتباط باشند تا بتوانند
[مدیریت منابع برای Podها و کانتینرها](/docs/concepts/configuration/manage-resources-containers/)
را اعمال کنند و منابعی مانند درخواست‌ها و محدودیت‌های CPU و حافظه را تنظیم کنند. برای ارتباط با گروه‌های کنترل، kubelet و محیط اجرای کانتینر باید از یک *درایور cgroup* استفاده کنند.
بسیار مهم است که kubelet و محیط اجرای کانتینر از درایور cgroup یکسانی استفاده کنند و پیکربندی یکسانی داشته باشند.

دو درایور cgroup در دسترس است:

* [`cgroupfs`](#cgroupfs-cgroup-driver)
* [`systemd`](#systemd-cgroup-driver)

### درایور cgroupfs {#cgroupfs-cgroup-driver}

درایور `cgroupfs` همان [درایور cgroup پیش‌فرض در kubelet](/docs/reference/config-api/kubelet-config.v1beta1) است.
 وقتی از درایور `cgroupfs` استفاده می‌شود، kubelet و محیط اجرای کانتینر برای پیکربندی cgroupها مستقیماً با سیستم فایل cgroup در ارتباط هستند.

استفاده از درایور `cgroupfs` در حالتی که
[systemd](https://www.freedesktop.org/wiki/Software/systemd/) سیستم init است، توصیه **نمی‌شود**؛ زیرا systemd انتظار دارد فقط یک مدیر cgroup روی سیستم وجود داشته باشد. افزون بر این، اگر از [cgroup v2](/docs/concepts/architecture/cgroups) استفاده می‌کنید، به‌جای `cgroupfs` از درایور cgroup `systemd` استفاده کنید.

### درایور cgroup systemd {#systemd-cgroup-driver}

وقتی [systemd](https://www.freedesktop.org/wiki/Software/systemd/) به‌عنوان سیستم init یک توزیع لینوکس انتخاب شده باشد، فرایند init یک گروه کنترل ریشه (`cgroup`) ایجاد و مصرف می‌کند و نقش مدیر cgroup را بر عهده می‌گیرد.

سیستم systemd یکپارچگی تنگاتنگی با cgroupها دارد و برای هر واحد systemd یک cgroup تخصیص می‌دهد. در نتیجه، اگر از `systemd` به‌عنوان سیستم init همراه با درایور `cgroupfs` استفاده کنید، سیستم دو مدیر cgroup متفاوت خواهد داشت.

وجود دو مدیر cgroup به دو دیدگاه متفاوت از منابع موجود و در حال استفادهٔ سیستم منجر می‌شود. در برخی موارد، نودهایی که برای kubelet و محیط اجرای کانتینر از `cgroupfs` و برای سایر فرایندها از `systemd` استفاده می‌کنند، تحت فشار منابع ناپایدار می‌شوند.

راهکار کاهش این ناپایداری این است که وقتی systemd سیستم init انتخاب‌شده است، از `systemd` به‌عنوان درایور cgroup برای kubelet و محیط اجرای کانتینر استفاده کنید.

برای تنظیم `systemd` به‌عنوان درایور cgroup، گزینهٔ `cgroupDriver` را در
[`KubeletConfiguration`](/docs/tasks/administer-cluster/kubelet-config-file/)
ویرایش کنید و مقدار آن را `systemd` قرار دهید. برای مثال:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
...
cgroupDriver: systemd
```

اگر `systemd` را به‌عنوان درایور cgroup برای kubelet پیکربندی کنید، باید `systemd` را به‌عنوان درایور cgroup برای محیط اجرای کانتینر نیز پیکربندی کنید. برای دستورالعمل‌ها به مستندات محیط اجرای کانتینر خود مراجعه کنید. برای مثال:

*  [containerd](#containerd-systemd)
*  [CRI-O](#cri-o)

در کوبرنتیز {{< skew currentVersion >}}، اگر
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
`KubeletCgroupDriverFromCRI` فعال باشد و محیط اجرای کانتینر از RPC مربوط به CRI با نام `RuntimeConfig` پشتیبانی کند، kubelet درایور cgroup مناسب را به‌طور خودکار از محیط اجرا تشخیص می‌دهد و تنظیم `cgroupDriver` را در پیکربندی kubelet نادیده می‌گیرد.

با این حال، نسخه‌های قدیمی‌تر محیط‌های اجرای کانتینر (به‌طور مشخص، containerd 1.y و پایین‌تر) از RPC مربوط به CRI با نام `RuntimeConfig` پشتیبانی نمی‌کنند و ممکن است به این پرس‌وجو پاسخ درستی ندهند؛ در این حالت kubelet به استفاده از مقدار فلگ `--cgroup-driver` خود بازمی‌گردد.

در کوبرنتیز 1.38، این رفتار بازگشتی حذف خواهد شد و نسخه‌های قدیمی‌تر containerd با kubeletهای جدیدتر کار نخواهند کرد.

{{< caution >}}
تغییر درایور cgroup نودی که به کلاستر پیوسته است، عملیاتی حساس است.
اگر kubelet، Podها را با معناشناسی یک درایور cgroup ایجاد کرده باشد، تغییر درایور cgroup محیط اجرای کانتینر به درایوری دیگر ممکن است هنگام بازسازی sandbox مربوط به این Podهای موجود خطا ایجاد کند. راه‌اندازی مجدد kubelet نیز ممکن است این خطاها را برطرف نکند.

اگر ابزارهای خودکارسازی‌ای در اختیار دارید که این کار را امکان‌پذیر می‌کنند، نود را با نود دیگری که پیکربندی به‌روزشده دارد جایگزین کنید، یا آن را با استفاده از خودکارسازی دوباره نصب کنید.
{{< /caution >}}

## پشتیبانی از نسخه‌های CRI {#cri-versions}

محیط اجرای کانتینر شما باید از نسخهٔ v1 رابط محیط اجرای کانتینر پشتیبانی کند.

کوبرنتیز [از نسخهٔ v1.26 به بعد](/blog/2022/11/18/upcoming-changes-in-kubernetes-1-26/#cri-api-removal)
_فقط_ با نسخهٔ v1 از API مربوط به CRI کار می‌کند. اگر محیط اجرای کانتینری از API نسخهٔ v1 پشتیبانی نکند، kubelet به‌عنوان نود ثبت نمی‌شود.

## محیط‌های اجرای کانتینر

{{% thirdparty-content %}}

### containerd

این بخش مراحل لازم برای استفاده از containerd به‌عنوان محیط اجرای CRI را شرح می‌دهد.

برای نصب containerd روی سیستم خود، دستورالعمل‌های
[شروع کار با containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md)
را دنبال کنید. پس از ایجاد یک فایل پیکربندی معتبر `config.toml` به این مرحله بازگردید.

{{< tabs name="یافتن فایل config.toml" >}}
{{% tab name="Linux" %}}
این فایل را می‌توانید در مسیر `/etc/containerd/config.toml` پیدا کنید.
{{% /tab %}}
{{% tab name="Windows" %}}
این فایل را می‌توانید در مسیر `C:\Program Files\containerd\config.toml` پیدا کنید.
{{% /tab %}}
{{< /tabs >}}

در لینوکس، سوکت CRI پیش‌فرض برای containerd مسیر `/run/containerd/containerd.sock` است.
در ویندوز، نقطهٔ پایانی (endpoint) پیش‌فرض CRI مقدار `npipe://./pipe/containerd-containerd` است.

#### پیکربندی درایور cgroup `systemd` {#containerd-systemd}

برای استفاده از درایور cgroup `systemd` در `/etc/containerd/config.toml` همراه با `runc`، پیکربندی زیر را متناسب با نسخهٔ containerd خود تنظیم کنید.

نسخه‌های 1.x از containerd:

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  ...
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true
```

نسخه‌های 2.x از containerd:

```
[plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc]
  ...
  [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc.options]
    SystemdCgroup = true
```

اگر از [cgroup v2](/docs/concepts/architecture/cgroups) استفاده می‌کنید، درایور cgroup `systemd` توصیه می‌شود.

{{< note >}}
اگر containerd را از یک بسته (برای مثال RPM یا `.deb`) نصب کرده باشید، ممکن است متوجه شوید که افزونهٔ یکپارچه‌سازی CRI به‌طور پیش‌فرض غیرفعال است.

برای استفاده از containerd با کوبرنتیز، پشتیبانی از CRI باید فعال باشد. مطمئن شوید که `cri` در فهرست `disabled_plugins` در فایل `/etc/containerd/config.toml` قرار ندارد؛ اگر این فایل را تغییر داده‌اید، `containerd` را نیز دوباره راه‌اندازی کنید.

اگر پس از نصب اولیهٔ کلاستر یا پس از نصب یک CNI با چرخهٔ خرابی مکرر کانتینرها (crash loop) مواجه شدید، ممکن است پیکربندی containerd ارائه‌شده همراه بسته شامل پارامترهای پیکربندی ناسازگار باشد. در این صورت، پیکربندی containerd را همان‌طور که در
[getting-started.md](https://github.com/containerd/containerd/blob/main/docs/getting-started.md#advanced-topics)
آمده است با دستور `containerd config default > /etc/containerd/config.toml` بازنشانی کنید و سپس پارامترهای پیکربندی ذکرشده در بالا را متناسب با آن تنظیم کنید.
{{< /note >}}

اگر این تغییر را اعمال کردید، حتماً containerd را دوباره راه‌اندازی کنید:

```shell
sudo systemctl restart containerd
```

در کوبرنتیز v1.28، می‌توانید تشخیص خودکار درایور cgroup را به‌عنوان یک قابلیت آلفا فعال کنید. برای جزئیات بیشتر، [درایور cgroup systemd](#systemd-cgroup-driver) را ببینید.

#### جایگزین کردن ایمیج sandbox (pause) {#override-pause-image-containerd}

در [پیکربندی containerd](https://github.com/containerd/containerd/blob/main/docs/cri/config.md) خود می‌توانید با تنظیم پیکربندی زیر، ایمیج sandbox را جایگزین کنید:

```toml
[plugins."io.containerd.grpc.v1.cri"]
  sandbox_image = "registry.k8s.io/pause:3.10"
```

پس از به‌روزرسانی فایل پیکربندی، ممکن است لازم باشد `containerd` را نیز دوباره راه‌اندازی کنید: `systemctl restart containerd`.

### CRI-O

این بخش مراحل لازم برای نصب CRI-O به‌عنوان محیط اجرای کانتینر را شرح می‌دهد.

برای نصب CRI-O، [دستورالعمل‌های نصب CRI-O](https://github.com/cri-o/packaging/blob/main/README.md#usage) را دنبال کنید.

#### درایور cgroup

ابزار CRI-O به‌طور پیش‌فرض از درایور cgroup systemd استفاده می‌کند که به احتمال زیاد برای شما به‌خوبی کار خواهد کرد. برای تغییر به درایور cgroup `cgroupfs`، یا فایل `/etc/crio/crio.conf` را ویرایش کنید یا یک پیکربندی تکمیلی (drop-in) در `/etc/crio/crio.conf.d/02-cgroup-manager.conf` قرار دهید؛ برای مثال:

```toml
[crio.runtime]
conmon_cgroup = "pod"
cgroup_manager = "cgroupfs"
```

به تغییر `conmon_cgroup` نیز توجه کنید؛ هنگام استفاده از CRI-O با `cgroupfs`، مقدار این گزینه باید `pod` باشد. به‌طور کلی لازم است پیکربندی درایور cgroup در kubelet (که معمولاً از طریق kubeadm انجام می‌شود) و CRI-O با هم هماهنگ نگه داشته شود.

در کوبرنتیز v1.28، می‌توانید تشخیص خودکار درایور cgroup را به‌عنوان یک قابلیت آلفا فعال کنید. برای جزئیات بیشتر، [درایور cgroup systemd](#systemd-cgroup-driver) را ببینید.

برای CRI-O، سوکت CRI به‌طور پیش‌فرض `/var/run/crio/crio.sock` است.

#### جایگزین کردن ایمیج sandbox (pause) {#override-pause-image-cri-o}

در [پیکربندی CRI-O](https://github.com/cri-o/cri-o/blob/main/docs/crio.conf.5.md) خود می‌توانید مقدار پیکربندی زیر را تنظیم کنید:

```toml
[crio.image]
pause_image="registry.k8s.io/pause:3.10"
```

این گزینهٔ پیکربندی از بارگذاری مجدد زندهٔ پیکربندی پشتیبانی می‌کند؛ برای اعمال این تغییر، دستور `systemctl reload crio` را اجرا کنید یا سیگنال `SIGHUP` را به فرایند `crio` بفرستید.

### Docker Engine {#docker}

{{< note >}}
این دستورالعمل‌ها فرض می‌کنند که برای یکپارچه‌سازی Docker Engine با کوبرنتیز از آداپتور
[`cri-dockerd`](https://mirantis.github.io/cri-dockerd/) استفاده می‌کنید.
{{< /note >}}

1. روی هر یک از نودهای خود، Docker را مطابق با
  [نصب Docker Engine](https://docs.docker.com/engine/install/#server) برای توزیع لینوکس خود نصب کنید.

2. ابزار [`cri-dockerd`](https://mirantis.github.io/cri-dockerd/usage/install) را با پیروی از راهنمای بخش نصب در مستندات آن نصب کنید.

برای `cri-dockerd`، سوکت CRI به‌طور پیش‌فرض `/run/cri-dockerd.sock` است.

### Mirantis Container Runtime {#mcr}

محصول [Mirantis Container Runtime](https://docs.mirantis.com/mcr/25.0/overview.html) (MCR) یک محیط اجرای کانتینر تجاری است که پیش‌تر با نام Docker Enterprise Edition شناخته می‌شد.

می‌توانید Mirantis Container Runtime را با استفاده از مؤلفهٔ متن‌باز
[`cri-dockerd`](https://mirantis.github.io/cri-dockerd/) که همراه MCR ارائه می‌شود، با کوبرنتیز به کار ببرید.

برای آشنایی بیشتر با نحوهٔ نصب Mirantis Container Runtime، به
[راهنمای استقرار MCR](https://docs.mirantis.com/mcr/25.0/install.html) مراجعه کنید.

برای یافتن مسیر سوکت CRI، واحد systemd با نام `cri-docker.socket` را بررسی کنید.

#### جایگزین کردن ایمیج sandbox (pause) {#override-pause-image-cri-dockerd-mcr}

آداپتور `cri-dockerd` یک آرگومان خط فرمان می‌پذیرد که با آن مشخص می‌شود کدام ایمیج کانتینر به‌عنوان کانتینر زیرساخت Pod («ایمیج pause») استفاده شود.
آرگومان خط فرمانی که باید استفاده کنید `--pod-infra-container-image` است.

## {{% heading "whatsnext" %}}

کلاستر شما علاوه بر محیط اجرای کانتینر، به یک
[افزونهٔ شبکه](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model)
فعال و کارا نیز نیاز دارد.
