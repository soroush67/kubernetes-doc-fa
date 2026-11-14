---
title: اجرای مؤلفه‌های نود کوبرنتیز با کاربر غیر root
content_type: task
min-kubernetes-server-version: 1.22
weight: 300
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.37" state="beta" >}}

این سند توضیح می‌دهد که چگونه می‌توان مؤلفه‌های نود کوبرنتیز مانند kubelet، CRI، OCI و CNI را
بدون دسترسی root و با استفاده از یک {{< glossary_tooltip text="فضای نام کاربر" term_id="userns" >}} اجرا کرد.

این روش با نام _حالت بدون root_ (rootless mode) نیز شناخته می‌شود.

{{< note >}}
این سند نحوهٔ اجرای مؤلفه‌های نود کوبرنتیز (و در نتیجه پادها) را با یک کاربر غیر root شرح می‌دهد.

اگر فقط می‌خواهید یک پاد را با کاربر غیر root اجرا کنید، به [SecurityContext](/docs/tasks/configure-pod-container/security-context/) مراجعه کنید.
{{< /note >}}

## {{% heading "prerequisites" %}}

{{% version-check %}}

* [فعال‌سازی Cgroup v2](https://rootlesscontaine.rs/getting-started/common/cgroup2/)
* [فعال‌سازی systemd همراه با نشست کاربر](https://rootlesscontaine.rs/getting-started/common/login/)
* [پیکربندی چند مقدار sysctl، بسته به توزیع لینوکس میزبان](https://rootlesscontaine.rs/getting-started/common/sysctl/)
* [اطمینان از اینکه کاربر فاقد امتیاز ویژهٔ شما در `/etc/subuid` و `/etc/subgid` فهرست شده است](https://rootlesscontaine.rs/getting-started/common/subuid/)
* فعال‌سازی [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `KubeletInUserNamespace`

<!-- steps -->

## اجرای کوبرنتیز درون Rootless Docker/Podman/nerdctl

### kind

ابزار [kind](https://kind.sigs.k8s.io/) از اجرای کوبرنتیز درون Rootless Docker، Rootless Podman یا Rootless nerdctl پشتیبانی می‌کند.

به [اجرای kind با Rootless Docker](https://kind.sigs.k8s.io/docs/user/rootless/) مراجعه کنید.

### minikube

ابزار [minikube](https://minikube.sigs.k8s.io/) نیز از اجرای کوبرنتیز درون Rootless Docker یا Rootless Podman پشتیبانی می‌کند.

به مستندات Minikube مراجعه کنید:

* [Rootless Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
* [Rootless Podman](https://minikube.sigs.k8s.io/docs/drivers/podman/)

### Usernetes

{{% thirdparty-content single="true" %}}

پروژهٔ [Usernetes](https://github.com/rootless-containers/usernetes) نیز از اجرای کوبرنتیز درون Rootless Docker، Rootless Podman یا Rootless nerdctl پشتیبانی می‌کند.

برخلاف kind و minikube، پروژهٔ Usernetes امکان تشکیل یک کلاستر از چندین نود Docker/Podman/nerdctl را با استفاده از VXLAN فراهم می‌کند.

برای نحوهٔ استفاده، به [مستندات Usernetes](https://github.com/rootless-containers/usernetes/blob/master/README.md) مراجعه کنید.

## اجرای کوبرنتیز درون کوبرنتیز، به‌صورت پادهای دارای فضای نام کاربر

{{% thirdparty-content single="true" %}}

### Usernetes

پروژهٔ [Usernetes](https://github.com/rootless-containers/usernetes) افزون بر حالت Kubernetes-in-Docker، از حالت Kubernetes-in-Kubernetes نیز پشتیبانی می‌کند.
در حالت Kubernetes-in-Kubernetes، نودهای یک کلاستر درونی به‌صورت پادهایی ایجاد می‌شوند که روی یک کلاستر بیرونی
و با [فضاهای نام کاربر](/docs/concepts/workloads/pods/user-namespaces/) فعال (`hostUsers: false`) اجرا می‌شوند.

برای نحوهٔ استفاده، به [مستندات Usernetes](https://github.com/rootless-containers/usernetes/blob/master/README.md) مراجعه کنید.

## اجرای کوبرنتیز درون کانتینرهای فاقد امتیاز ویژه

{{% thirdparty-content single="true" %}}

### sysbox

پروژهٔ [Sysbox](https://github.com/nestybox/sysbox) یک محیط اجرای کانتینر متن‌باز
(مشابه «runc») است که از اجرای بارهای کاری سطح سیستم مانند Docker
و کوبرنتیز درون کانتینرهای فاقد امتیاز ویژه پشتیبانی می‌کند؛ کانتینرهایی که با فضای نام
کاربر لینوکس ایزوله شده‌اند.

برای اطلاعات بیشتر، به [Sysbox Quick Start Guide: Kubernetes-in-Docker](https://github.com/nestybox/sysbox/blob/master/docs/quickstart/kind.md) مراجعه کنید.

ابزار Sysbox از اجرای کوبرنتیز درون کانتینرهای فاقد امتیاز ویژه پشتیبانی می‌کند، بی‌آنکه
به Cgroup v2 یا feature gate با نام `KubeletInUserNamespace` نیازی باشد. این کار را
با در دسترس قرار دادن فایل‌سیستم‌های `/proc` و `/sys` که به‌طور ویژه ساخته شده‌اند درون
کانتینر، به همراه چند روش پیشرفتهٔ دیگر مجازی‌سازی سیستم‌عامل انجام می‌دهد.

## اجرای کوبرنتیز بدون root به‌طور مستقیم روی میزبان

{{% thirdparty-content single="true" %}}

### K3s

توزیع [K3s](https://k3s.io/) به‌صورت آزمایشی از حالت بدون root پشتیبانی می‌کند.

برای نحوهٔ استفاده، به [اجرای K3s در حالت بدون root](https://rancher.com/docs/k3s/latest/en/advanced/#running-k3s-with-rootless-mode-experimental) مراجعه کنید.

### Usernetes (تا سال ۲۰۲۳)
نسل نخست [Usernetes](https://github.com/rootless-containers/usernetes) از اجرای کوبرنتیز بدون root به‌طور مستقیم روی میزبان پشتیبانی می‌کرد.
این حالت در سال ۲۰۲۳ بایگانی شد.

برای اطلاعات بایگانی‌شده، به [شاخهٔ `gen1` مخزن Usernetes](https://github.com/rootless-containers/usernetes/tree/gen1) مراجعه کنید.

## استقرار دستی نودی که kubelet را در یک فضای نام کاربر اجرا می‌کند {#userns-the-hard-way}

این بخش نکاتی را برای اجرای دستی کوبرنتیز در یک فضای نام کاربر ارائه می‌دهد.

{{< note >}}
مخاطب این بخش توسعه‌دهندگان توزیع‌های کوبرنتیز هستند، نه کاربران نهایی.
{{< /note >}}

### ایجاد فضای نام کاربر

نخستین گام، ایجاد یک {{< glossary_tooltip text="فضای نام کاربر" term_id="userns" >}} است.

اگر می‌خواهید کوبرنتیز را در کانتینری اجرا کنید که دارای فضای نام کاربر است، مانند
Rootless Docker/Podman یا LXC/LXD، همه‌چیز آماده است و می‌توانید به زیربخش بعدی بروید.

در غیر این صورت، باید خودتان با فراخوانی `unshare(2)` همراه با `CLONE_NEWUSER` یک فضای نام کاربر ایجاد کنید.

همچنین می‌توان با ابزارهای خط فرمان زیر، فضای نام کاربر را از فرایند والد جدا (unshare) کرد:

- [`unshare(1)`](https://man7.org/linux/man-pages/man1/unshare.1.html)
- [RootlessKit](https://github.com/rootless-containers/rootlesskit)
- [become-root](https://github.com/giuseppe/become-root)

پس از جدا کردن فضای نام کاربر، باید فضاهای نام دیگری مانند فضای نام mount را نیز جدا کنید.

پس از جدا کردن فضای نام mount، نیازی به فراخوانی `chroot()` یا `pivot_root()` *نیست*؛
با این حال، باید روی چندین دایرکتوری *درون* این فضای نام، فایل‌سیستم‌های قابل‌نوشتن mount کنید.

دست‌کم دایرکتوری‌های زیر باید *درون* فضای نام (و نه *بیرون* از آن) قابل‌نوشتن باشند:

- `/etc`
- `/run`
- `/var/logs`
- `/var/lib/kubelet`
- `/var/lib/cni`
- `/var/lib/containerd` (برای containerd)
- `/var/lib/containers` (برای CRI-O)

### ایجاد درخت cgroup تفویض‌شده

افزون بر فضای نام کاربر، به یک درخت cgroup قابل‌نوشتن با cgroup v2 نیز نیاز دارید.

{{< note >}}
پشتیبانی کوبرنتیز از اجرای مؤلفه‌های نود در فضاهای نام کاربر، به cgroup v2 نیاز دارد.
از cgroup v1 پشتیبانی نمی‌شود.
{{< /note >}}

اگر می‌خواهید کوبرنتیز را در Rootless Docker/Podman یا LXC/LXD روی میزبانی مبتنی بر systemd اجرا کنید، همه‌چیز آماده است.

در غیر این صورت، باید یک واحد systemd با ویژگی `Delegate=yes` ایجاد کنید تا یک درخت cgroup با مجوز نوشتن تفویض شود.

روی نود شما، systemd باید از پیش به‌گونه‌ای پیکربندی شده باشد که اجازهٔ تفویض را بدهد؛ برای جزئیات بیشتر، به
[cgroup v2](https://rootlesscontaine.rs/getting-started/common/cgroup2/) در مستندات Rootless
Containers مراجعه کنید.

### پیکربندی شبکه

{{% thirdparty-content single="true" %}}

فضای نام شبکهٔ مؤلفه‌های نود باید یک رابط غیر loopback داشته باشد که برای نمونه می‌توان آن را با
[slirp4netns](https://github.com/rootless-containers/slirp4netns)،
[VPNKit](https://github.com/moby/vpnkit) یا
[lxc-user-nic(1)](https://www.man7.org/linux/man-pages/man1/lxc-user-nic.1.html) پیکربندی کرد.

فضاهای نام شبکهٔ پادها را می‌توان با افزونه‌های معمولی CNI پیکربندی کرد.
برای شبکه‌بندی چندنودی، Flannel (VXLAN، 8472/UDP) به‌درستی کار می‌کند.

پورت‌هایی مانند پورت kubelet (10250/TCP) و پورت‌های سرویس `NodePort` باید با یک پورت‌فورواردر خارجی،
مانند RootlessKit، slirp4netns یا
[socat(1)](https://linux.die.net/man/1/socat)، از فضای نام شبکهٔ نود در دسترس میزبان قرار گیرند.

می‌توانید از پورت‌فورواردر K3s استفاده کنید.
برای جزئیات بیشتر، به [اجرای K3s در حالت بدون root](https://rancher.com/docs/k3s/latest/en/advanced/#known-issues-with-rootless-mode)
مراجعه کنید.
پیاده‌سازی آن را می‌توانید در [بستهٔ `pkg/rootlessports`](https://github.com/k3s-io/k3s/blob/v1.22.3+k3s1/pkg/rootlessports/controller.go) در k3s بیابید.

### پیکربندی CRI

مؤلفهٔ kubelet به یک محیط اجرای کانتینر وابسته است. باید یک محیط اجرای کانتینر مانند
containerd یا CRI-O را مستقر کنید و مطمئن شوید که پیش از راه‌اندازی kubelet، درون فضای نام کاربر در حال اجراست.

{{< tabs name="cri" >}}
{{% tab name="containerd" %}}

اجرای افزونهٔ CRI در containerd درون یک فضای نام کاربر، از نسخهٔ 1.4 containerd پشتیبانی می‌شود.

اجرای containerd درون یک فضای نام کاربر به پیکربندی‌های زیر نیاز دارد.

```toml
version = 2

[plugins."io.containerd.grpc.v1.cri"]
# Disable AppArmor
  disable_apparmor = true
# Ignore an error during setting oom_score_adj
  restrict_oom_score_adj = true
# Disable hugetlb cgroup v2 controller (because systemd does not support delegating hugetlb controller)
  disable_hugetlb_controller = true

[plugins."io.containerd.grpc.v1.cri".containerd]
# Using non-fuse overlayfs is also possible for kernel >= 5.11, but requires SELinux to be disabled
  snapshotter = "fuse-overlayfs"

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
# We use cgroupfs that is delegated by systemd, so we do not use SystemdCgroup driver
# (unless you run another systemd in the namespace)
  SystemdCgroup = false
```

مسیر پیش‌فرض فایل پیکربندی `/etc/containerd/config.toml` است.
این مسیر را می‌توان با `containerd -c /path/to/containerd/config.toml` مشخص کرد.

{{% /tab %}}
{{% tab name="CRI-O" %}}

اجرای CRI-O درون یک فضای نام کاربر، از نسخهٔ 1.22 CRI-O پشتیبانی می‌شود.

برای CRI-O باید متغیر محیطی `_CRIO_ROOTLESS=1` تنظیم شود.

پیکربندی‌های زیر نیز توصیه می‌شوند:

```toml
[crio]
  storage_driver = "overlay"
# Using non-fuse overlayfs is also possible for kernel >= 5.11, but requires SELinux to be disabled
  storage_option = ["overlay.mount_program=/usr/local/bin/fuse-overlayfs"]

[crio.runtime]
# We use cgroupfs that is delegated by systemd, so we do not use "systemd" driver
# (unless you run another systemd in the namespace)
  cgroup_manager = "cgroupfs"
```

مسیر پیش‌فرض فایل پیکربندی `/etc/crio/crio.conf` است.
این مسیر را می‌توان با `crio --config /path/to/crio/crio.conf` مشخص کرد.
{{% /tab %}}
{{< /tabs >}}

### پیکربندی kubelet

اجرای kubelet درون یک فضای نام کاربر به پیکربندی زیر نیاز دارد:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  KubeletInUserNamespace: true
# We use cgroupfs that is delegated by systemd, so we do not use "systemd" driver
# (unless you run another systemd in the namespace)
cgroupDriver: "cgroupfs"
```

هنگامی که feature gate با نام `KubeletInUserNamespace` فعال باشد، kubelet خطاهایی را که
ممکن است هنگام تنظیم مقادیر sysctl زیر روی نود رخ دهند، نادیده می‌گیرد.

- `vm.overcommit_memory`
- `vm.panic_on_oom`
- `kernel.panic`
- `kernel.panic_on_oops`
- `kernel.keys.root_maxkeys`
- `kernel.keys.root_maxbytes`.

درون یک فضای نام کاربر، kubelet هر خطایی را که هنگام تلاش برای باز کردن `/dev/kmsg` رخ دهد نیز نادیده می‌گیرد.
همچنین این feature gate به kube-proxy امکان می‌دهد خطای رخ‌داده هنگام تنظیم `RLIMIT_NOFILE` را نادیده بگیرد.

این feature gate، یعنی `KubeletInUserNamespace`، در کوبرنتیز نسخهٔ 1.22 با وضعیت «آلفا» معرفی شد.

اجرای kubelet درون یک فضای نام کاربر بدون استفاده از این feature gate نیز امکان‌پذیر است؛
این کار با mount کردن یک فایل‌سیستم proc که به‌طور ویژه ساخته شده است انجام می‌شود (همان کاری که [Sysbox](https://github.com/nestybox/sysbox) انجام می‌دهد)، اما به‌طور رسمی پشتیبانی نمی‌شود.

### پیکربندی kube-proxy

اجرای kube-proxy درون یک فضای نام کاربر به پیکربندی زیر نیاز دارد:

```yaml
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: "iptables" # or "userspace"
conntrack:
# Skip setting sysctl value "net.netfilter.nf_conntrack_max"
  maxPerCore: 0
# Skip setting "net.netfilter.nf_conntrack_tcp_timeout_established"
  tcpEstablishedTimeout: 0s
# Skip setting "net.netfilter.nf_conntrack_tcp_timeout_close"
  tcpCloseWaitTimeout: 0s
```

## محدودیت‌ها

- بیشتر درایورهای حجم (volume) «غیرمحلی» مانند `nfs` و `iscsi` کار نمی‌کنند.
  حجم‌های محلی مانند `local`، `hostPath`، `emptyDir`، `configMap`، `secret` و `downwardAPI` به‌درستی کار می‌کنند.

- برخی از افزونه‌های CNI ممکن است کار نکنند. Flannel (VXLAN) به‌درستی کار می‌کند.

برای اطلاعات بیشتر در این زمینه، به صفحهٔ [محدودیت‌ها و کارهای آینده](https://rootlesscontaine.rs/caveats/)
در وب‌سایت rootlesscontaine.rs مراجعه کنید.

## {{% heading "seealso" %}}

- [rootlesscontaine.rs](https://rootlesscontaine.rs/)
- [Rootless Containers 2020 (KubeCon NA 2020)](https://www.slideshare.net/AkihiroSuda/kubecon-na-2020-containerd-rootless-containers-2020)
- [اجرای kind با Rootless Docker](https://kind.sigs.k8s.io/docs/user/rootless/)
- [Usernetes](https://github.com/rootless-containers/usernetes)
- [اجرای K3s در حالت بدون root](https://rancher.com/docs/k3s/latest/en/advanced/#running-k3s-with-rootless-mode-experimental)
- [KEP-2033: Kubelet-in-UserNS (aka Rootless mode)](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/2033-kubelet-in-userns-aka-rootless)
