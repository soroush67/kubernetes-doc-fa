---
title: عیب‌یابی kubeadm
content_type: concept
weight: 20
---

<!-- overview -->

مانند هر برنامه‌ی دیگری، ممکن است هنگام نصب یا اجرای kubeadm با خطا روبه‌رو شوید.
در این صفحه چند سناریوی رایج خرابی فهرست شده و برای هر کدام مراحلی آمده است که به شما در درک و رفع مشکل کمک می‌کند.

اگر مشکل شما در فهرست زیر نیست، مراحل زیر را دنبال کنید:

- اگر فکر می‌کنید مشکل شما یک باگ در kubeadm است:
  - به [github.com/kubernetes/kubeadm](https://github.com/kubernetes/kubeadm/issues) بروید و issueهای موجود را جست‌وجو کنید.
  - اگر issue مرتبطی وجود ندارد، [یک issue جدید باز کنید](https://github.com/kubernetes/kubeadm/issues/new) و از قالب issue پیروی کنید.

- اگر درباره‌ی نحوه‌ی کار kubeadm مطمئن نیستید، می‌توانید در کانال `#kubeadm` در [Slack](https://slack.k8s.io/) بپرسید
  یا پرسشی در [StackOverflow](https://stackoverflow.com/questions/tagged/kubernetes) مطرح کنید. لطفاً برچسب‌های
  مرتبط مانند `#kubernetes` و `#kubeadm` را اضافه کنید تا دیگران بتوانند به شما کمک کنند.

<!-- body -->

## عدم امکان پیوستن نود v1.18 به کلاستر v1.17 به دلیل نبود RBAC

در نسخه‌ی v1.18، kubeadm از پیوستن نودی به کلاستر جلوگیری می‌کند که نودی با همان نام از قبل در کلاستر وجود داشته باشد.
برای این کار لازم بود RBAC به کاربر bootstrap-token اضافه شود تا بتواند آبجکت Node را با عمل GET دریافت کند.

اما این تغییر مشکلی ایجاد می‌کند: دستور `kubeadm join` در نسخه‌ی v1.18 نمی‌تواند به کلاستری بپیوندد که با kubeadm نسخه‌ی v1.17 ایجاد شده است.

برای دور زدن این مشکل دو گزینه دارید:

دستور `kubeadm init phase bootstrap-token` را با kubeadm نسخه‌ی v1.18 روی یک نود control-plane اجرا کنید.
توجه کنید که این کار بقیه‌ی مجوزهای bootstrap-token را نیز فعال می‌کند.

یا

قواعد RBAC زیر را به‌صورت دستی با `kubectl apply -f ...` اعمال کنید:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kubeadm:get-nodes
rules:
  - apiGroups:
      - ""
    resources:
      - nodes
    verbs:
      - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubeadm:get-nodes
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kubeadm:get-nodes
subjects:
  - apiGroup: rbac.authorization.k8s.io
    kind: Group
    name: system:bootstrappers:kubeadm:default-node-token
```

## پیدا نشدن `ebtables` یا فایل اجرایی مشابه هنگام نصب

اگر هنگام اجرای `kubeadm init` هشدارهای زیر را می‌بینید

```console
[preflight] WARNING: ebtables not found in system path
[preflight] WARNING: ethtool not found in system path
```

احتمالاً `ebtables`، `ethtool` یا فایل اجرایی مشابهی روی نود شما نصب نیست.
می‌توانید آن‌ها را با دستورهای زیر نصب کنید:

- کاربران Ubuntu/Debian دستور `apt install ebtables ethtool` را اجرا کنند.
- کاربران CentOS/Fedora دستور `dnf install ebtables ethtool` را اجرا کنند.

## مسدود ماندن kubeadm در انتظار control plane هنگام نصب

اگر متوجه شدید که `kubeadm init` پس از چاپ خط زیر متوقف می‌ماند:

```console
[apiclient] Created API client, waiting for the control plane to become ready
```

این وضعیت ممکن است دلایل متعددی داشته باشد. رایج‌ترین آن‌ها عبارت‌اند از:

- مشکلات اتصال شبکه. پیش از ادامه، بررسی کنید که ماشین شما اتصال کامل به شبکه دارد.
- کانتینرهای control plane مدام کرش می‌کنند (crashloop) یا هنگ کرده‌اند. برای بررسی این موضوع می‌توانید دستور `docker ps`
  را اجرا کنید و هر کانتینر را با اجرای `docker logs` بررسی کنید. برای سایر محیط‌های اجرای کانتینر، به
  [اشکال‌زدایی نودهای کوبرنتیز با crictl](/docs/tasks/debug/debug-cluster/crictl/) مراجعه کنید.

## مسدود ماندن kubeadm هنگام حذف کانتینرهای مدیریت‌شده

اگر محیط اجرای کانتینر متوقف شود و هیچ‌یک از کانتینرهای مدیریت‌شده توسط کوبرنتیز را حذف نکند،
ممکن است وضعیت زیر رخ دهد:

```shell
sudo kubeadm reset
```

```console
[preflight] Running pre-flight checks
[reset] Stopping the kubelet service
[reset] Unmounting mounted directories in "/var/lib/kubelet"
[reset] Removing kubernetes-managed containers
(block)
```

یک راه‌حل ممکن این است که محیط اجرای کانتینر را دوباره راه‌اندازی کنید و سپس `kubeadm reset` را دوباره اجرا کنید.
همچنین می‌توانید از `crictl` برای اشکال‌زدایی وضعیت محیط اجرای کانتینر استفاده کنید. به
[اشکال‌زدایی نودهای کوبرنتیز با crictl](/docs/tasks/debug/debug-cluster/crictl/) مراجعه کنید.

## قرار گرفتن Podها در وضعیت `RunContainerError`، `CrashLoopBackOff` یا `Error`

بلافاصله پس از `kubeadm init` نباید هیچ Podی در این وضعیت‌ها باشد.

- اگر _بلافاصله پس از_ `kubeadm init` Podهایی در یکی از این وضعیت‌ها وجود دارند، لطفاً یک
  issue در مخزن kubeadm باز کنید. تا زمانی که افزونه‌ی شبکه را مستقر نکرده‌اید، `coredns` (یا `kube-dns`)
  باید در وضعیت `Pending` باشد.
- اگر پس از استقرار افزونه‌ی شبکه، Podهایی را در وضعیت `RunContainerError`، `CrashLoopBackOff` یا `Error`
  می‌بینید و هیچ تغییری در `coredns` (یا `kube-dns`) رخ نمی‌دهد،
  به احتمال زیاد افزونه‌ی شبکه‌ی Pod که نصب کرده‌اید به‌نوعی خراب است.
  ممکن است لازم باشد مجوزهای RBAC بیشتری به آن بدهید یا از نسخه‌ی جدیدتری استفاده کنید. لطفاً
  در سامانه‌ی پیگیری issue ارائه‌دهنده‌ی شبکه‌ی Pod یک issue ثبت کنید تا مشکل در آنجا بررسی شود.

## ماندن `coredns` در وضعیت `Pending`

این رفتار **مورد انتظار** و بخشی از طراحی است. ابزار kubeadm به ارائه‌دهنده‌ی شبکه وابسته نیست، بنابراین مدیر کلاستر
باید [افزونه‌ی شبکه‌ی Pod](/docs/concepts/cluster-administration/addons/) دلخواه خود را نصب کند.
پیش از آنکه CoreDNS بتواند به‌طور کامل مستقر شود، باید یک شبکه‌ی Pod نصب کنید.
به همین دلیل، پیش از راه‌اندازی شبکه، وضعیت `Pending` دیده می‌شود.

## کار نکردن سرویس‌های `HostPort`

در دسترس بودن قابلیت‌های `HostPort` و `HostIP` به ارائه‌دهنده‌ی شبکه‌ی Pod شما بستگی دارد.
لطفاً با سازنده‌ی افزونه‌ی شبکه‌ی Pod تماس بگیرید تا بفهمید آیا قابلیت‌های
`HostPort` و `HostIP` در دسترس هستند یا نه.

پشتیبانی ارائه‌دهندگان CNI یعنی Calico، Canal و Flannel از HostPort تأیید شده است.

برای اطلاعات بیشتر، به
[مستندات portmap در CNI](https://github.com/containernetworking/plugins/blob/master/plugins/meta/portmap/README.md) مراجعه کنید.

اگر ارائه‌دهنده‌ی شبکه‌ی شما از افزونه‌ی portmap در CNI پشتیبانی نمی‌کند، ممکن است لازم باشد از
[قابلیت NodePort در سرویس‌ها](/docs/concepts/services-networking/service/#type-nodeport)
یا از `HostNetwork=true` استفاده کنید.

## در دسترس نبودن Podها از طریق IP سرویس آن‌ها

- بسیاری از افزونه‌های شبکه هنوز [حالت hairpin](/docs/tasks/debug/debug-application/debug-service/#a-pod-fails-to-reach-itself-via-the-service-ip)
  را فعال نمی‌کنند؛ این حالت به Podها امکان می‌دهد از طریق IP سرویس خود به خودشان دسترسی داشته باشند. این مشکل به
  [CNI](https://github.com/containernetworking/cni/issues/476) مربوط است. لطفاً با ارائه‌دهنده‌ی افزونه‌ی
  شبکه تماس بگیرید تا از آخرین وضعیت پشتیبانی آن از حالت hairpin مطلع شوید.

- اگر از VirtualBox (به‌طور مستقیم یا از طریق Vagrant) استفاده می‌کنید، باید
  مطمئن شوید که `hostname -i` یک آدرس IP قابل مسیریابی برمی‌گرداند. به‌طور پیش‌فرض، نخستین
  رابط شبکه به یک شبکه‌ی host-only غیرقابل مسیریابی متصل است. یک راه‌حل جایگزین
  ویرایش `/etc/hosts` است؛ برای نمونه به این
  [Vagrantfile](https://github.com/errordeveloper/k8s-playground/blob/22dd39dfc06111235620e6c4404a96ae146f26fd/Vagrantfile#L11)
  مراجعه کنید.

## خطاهای گواهی TLS

خطای زیر نشان‌دهنده‌ی احتمال عدم تطابق گواهی است.

```none
# kubectl get pods
Unable to connect to the server: x509: certificate signed by unknown authority (possibly because of "crypto/rsa: verification error" while trying to verify candidate authority certificate "kubernetes")
```

- بررسی کنید که فایل `$HOME/.kube/config` یک گواهی معتبر داشته باشد و در صورت نیاز
  گواهی را دوباره تولید کنید. گواهی‌های موجود در فایل kubeconfig
  با base64 کدگذاری شده‌اند. برای رمزگشایی گواهی می‌توانید از دستور `base64 --decode`
  و برای مشاهده‌ی اطلاعات گواهی از `openssl x509 -text -noout` استفاده کنید.

- متغیر محیطی `KUBECONFIG` را با دستور زیر حذف کنید:

  ```sh
  unset KUBECONFIG
  ```

  یا آن را روی مسیر پیش‌فرض `KUBECONFIG` تنظیم کنید:

  ```sh
  export KUBECONFIG=/etc/kubernetes/admin.conf
  ```

- راه‌حل دیگر، بازنویسی فایل `kubeconfig` موجود برای کاربر «admin» است:

  ```sh
  mv $HOME/.kube $HOME/.kube.bak
  mkdir $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
  ```

## شکست در چرخش گواهی کلاینت kubelet {#kubelet-client-cert}

به‌طور پیش‌فرض، kubeadm یک kubelet را با چرخش خودکار گواهی‌های کلاینت پیکربندی می‌کند و برای این کار از
پیوند نمادین `/var/lib/kubelet/pki/kubelet-client-current.pem` تعیین‌شده در `/etc/kubernetes/kubelet.conf` استفاده می‌کند.
اگر این فرایند چرخش با شکست مواجه شود، ممکن است خطاهایی مانند `x509: certificate has expired or is not yet valid`
را در لاگ‌های kube-apiserver ببینید. برای رفع این مشکل باید مراحل زیر را دنبال کنید:

1. از فایل‌های `/etc/kubernetes/kubelet.conf` و `/var/lib/kubelet/pki/kubelet-client*` روی نود معیوب نسخه‌ی پشتیبان بگیرید و سپس آن‌ها را حذف کنید.
1. روی یک نود control plane سالم در کلاستر که فایل `/etc/kubernetes/pki/ca.key` را دارد، دستور
   `kubeadm kubeconfig user --org system:nodes --client-name system:node:$NODE > kubelet.conf` را اجرا کنید.
   مقدار `$NODE` باید برابر با نام نود معیوب موجود در کلاستر باشد.
   فایل `kubelet.conf` حاصل را به‌صورت دستی ویرایش کنید تا نام کلاستر و نقطه‌ی پایانی سرور را تنظیم کنید،
   یا از `kubeconfig user --config` استفاده کنید (به [تولید فایل‌های kubeconfig برای کاربران اضافی](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#kubeconfig-additional-users) مراجعه کنید). اگر کلاستر شما
   فایل `ca.key` را ندارد، باید گواهی‌های جاسازی‌شده در `kubelet.conf` را به‌صورت خارجی امضا کنید.
1. فایل `kubelet.conf` حاصل را روی نود معیوب در مسیر `/etc/kubernetes/kubelet.conf` کپی کنید.
1. سرویس kubelet را روی نود معیوب دوباره راه‌اندازی کنید (`systemctl restart kubelet`) و منتظر بمانید تا
   فایل `/var/lib/kubelet/pki/kubelet-client-current.pem` دوباره ایجاد شود.
1. فایل `kubelet.conf` را به‌صورت دستی ویرایش کنید تا به گواهی‌های کلاینت چرخش‌یافته‌ی kubelet اشاره کند؛ برای این کار
   `client-certificate-data` و `client-key-data` را با موارد زیر جایگزین کنید:

   ```yaml
   client-certificate: /var/lib/kubelet/pki/kubelet-client-current.pem
   client-key: /var/lib/kubelet/pki/kubelet-client-current.pem
   ```

1. سرویس kubelet را دوباره راه‌اندازی کنید.
1. مطمئن شوید که نود به وضعیت `Ready` می‌رسد.

## کارت شبکه‌ی (NIC) پیش‌فرض هنگام استفاده از flannel به‌عنوان شبکه‌ی Pod در Vagrant

خطای زیر ممکن است نشان دهد که مشکلی در شبکه‌ی Pod وجود دارد:

```sh
Error from server (NotFound): the server could not find the requested resource
```

- اگر از flannel به‌عنوان شبکه‌ی Pod درون Vagrant استفاده می‌کنید، باید
  نام رابط شبکه‌ی پیش‌فرض را برای flannel مشخص کنید.

  معمولاً Vagrant دو رابط شبکه به همه‌ی ماشین‌های مجازی اختصاص می‌دهد. رابط اول که به همه‌ی میزبان‌ها
  آدرس IP `10.0.2.15` را می‌دهد، برای ترافیک خارجی است که از NAT عبور می‌کند.

  این موضوع ممکن است برای flannel مشکل ایجاد کند، زیرا flannel به‌طور پیش‌فرض از نخستین رابط شبکه‌ی میزبان استفاده می‌کند.
  در نتیجه، همه‌ی میزبان‌ها تصور می‌کنند آدرس IP عمومی یکسانی دارند. برای جلوگیری از این مشکل،
  فلگ `--iface eth1` را به flannel بدهید تا رابط دوم انتخاب شود.

## استفاده از IP غیرعمومی برای کانتینرها

در برخی موقعیت‌ها، دستورهای `kubectl logs` و `kubectl run` ممکن است در کلاستری که در سایر موارد
به‌درستی کار می‌کند، خطاهای زیر را برگردانند:

```console
Error from server: Get https://10.19.0.41:10250/containerLogs/default/mysql-ddc65b868-glc5m/mysql: dial tcp 10.19.0.41:10250: getsockopt: no route to host
```

- علت این مشکل ممکن است این باشد که کوبرنتیز از IPای استفاده می‌کند که نمی‌تواند با سایر IPهای
  ظاهراً هم‌زیرشبکه ارتباط برقرار کند؛ احتمالاً به دلیل سیاست ارائه‌دهنده‌ی ماشین.
- سرویس DigitalOcean یک IP عمومی و نیز یک IP خصوصی به `eth0` اختصاص می‌دهد؛ IP خصوصی به‌صورت داخلی
  به‌عنوان لنگر (anchor) برای قابلیت IP شناور آن استفاده می‌شود. با این حال، `kubelet` به‌جای IP عمومی،
  IP خصوصی را به‌عنوان `InternalIP` نود انتخاب می‌کند.

  برای بررسی این سناریو به‌جای `ifconfig` از `ip addr show` استفاده کنید، زیرا `ifconfig`
  آدرس IP مستعار مشکل‌ساز را نمایش نمی‌دهد. همچنین می‌توانید از یک نقطه‌ی پایانی API مخصوص
  DigitalOcean استفاده کنید تا IP لنگر را از درون droplet استعلام کنید:

  ```sh
  curl http://169.254.169.254/metadata/v1/interfaces/public/0/anchor_ipv4/address
  ```

  راه‌حل این است که با فلگ `--node-ip` به `kubelet` بگویید از کدام IP استفاده کند.
  هنگام استفاده از DigitalOcean، این IP می‌تواند IP عمومی (اختصاص‌یافته به `eth0`) یا
  اگر می‌خواهید از شبکه‌ی خصوصی اختیاری استفاده کنید، IP خصوصی (اختصاص‌یافته به `eth1`) باشد.
  برای این کار می‌توانید از بخش `kubeletExtraArgs` در
  [ساختار `NodeRegistrationOptions`](/docs/reference/config-api/kubeadm-config.v1beta4/#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions)
  در kubeadm استفاده کنید.

  سپس `kubelet` را دوباره راه‌اندازی کنید:

  ```sh
  systemctl daemon-reload
  systemctl restart kubelet
  ```

## قرار داشتن Podهای `coredns` در وضعیت `CrashLoopBackOff` یا `Error`

اگر نودهایی دارید که SELinux را با نسخه‌ی قدیمی‌تری از Docker اجرا می‌کنند، ممکن است با وضعیتی روبه‌رو شوید
که در آن Podهای `coredns` راه‌اندازی نمی‌شوند. برای حل این مشکل، می‌توانید یکی از گزینه‌های زیر را امتحان کنید:

- به [نسخه‌ی جدیدتری از Docker](/docs/setup/production-environment/container-runtimes/#docker) ارتقا دهید.

- [SELinux را غیرفعال کنید](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security-enhanced_linux/sect-security-enhanced_linux-enabling_and_disabling_selinux-disabling_selinux).

- مقدار `allowPrivilegeEscalation` را در Deployment مربوط به `coredns` روی `true` تنظیم کنید:

```bash
kubectl -n kube-system get deployment coredns -o yaml | \
  sed 's/allowPrivilegeEscalation: false/allowPrivilegeEscalation: true/g' | \
  kubectl apply -f -
```

یکی دیگر از علت‌های قرار گرفتن CoreDNS در وضعیت `CrashLoopBackOff` این است که یک Pod مربوط به CoreDNS که در کوبرنتیز مستقر شده، یک حلقه (loop) را تشخیص دهد.
[چندین راه‌حل](https://github.com/coredns/coredns/tree/master/plugin/loop#troubleshooting-loops-in-kubernetes-clusters)
وجود دارد تا کوبرنتیز هر بار که CoreDNS حلقه را تشخیص می‌دهد و خارج می‌شود، تلاش نکند Pod مربوط به CoreDNS را دوباره راه‌اندازی کند.

{{< warning >}}
غیرفعال کردن SELinux یا تنظیم `allowPrivilegeEscalation` روی `true` می‌تواند
امنیت کلاستر شما را به خطر بیندازد.
{{< /warning >}}

## راه‌اندازی مجدد پیوسته‌ی Podهای etcd

اگر با خطای زیر روبه‌رو شدید:

```
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:247: starting container process caused "process_linux.go:110: decoding init error from pipe caused \"read parent: connection reset by peer\""
```

این مشکل زمانی رخ می‌دهد که CentOS 7 را با Docker 1.13.1.84 اجرا کنید.
این نسخه از Docker ممکن است مانع از اجرای فرمان kubelet درون کانتینر etcd شود.

برای دور زدن این مشکل، یکی از گزینه‌های زیر را انتخاب کنید:

- به نسخه‌ی قدیمی‌تری از Docker، مانند 1.13.1-75، برگردید:

  ```
  dnf downgrade docker-1.13.1-75.git8633870.el7.centos.x86_64 docker-client-1.13.1-75.git8633870.el7.centos.x86_64 docker-common-1.13.1-75.git8633870.el7.centos.x86_64
  ```

- یکی از نسخه‌های توصیه‌شده‌ی جدیدتر، مانند 18.06، را نصب کنید:

  ```bash
  sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
  dnf install docker-ce-18.06.1.ce-3.el7.x86_64
  ```

## عدم امکان ارسال فهرست مقادیر جداشده با کاما به آرگومان‌های درون فلگ `--component-extra-args`

فلگ‌های `kubeadm init` مانند `--component-extra-args` به شما امکان می‌دهند آرگومان‌های سفارشی را به یکی از مؤلفه‌های
control-plane مانند kube-apiserver بدهید. با این حال، این سازوکار به دلیل نوع زیربنایی‌ای که برای تجزیه‌ی
مقادیر استفاده می‌شود (`mapStringString`) محدودیت دارد.

اگر بخواهید آرگومانی را ارسال کنید که از چند مقدار جداشده با کاما پشتیبانی می‌کند، مانند
`--apiserver-extra-args "enable-admission-plugins=LimitRanger,NamespaceExists"`، این فلگ با خطای
`flag: malformed pair, expect string=string` شکست می‌خورد. علت این است که فهرست آرگومان‌های
`--apiserver-extra-args` انتظار جفت‌های `key=value` را دارد و در این حالت `NamespacesExists`
کلیدی در نظر گرفته می‌شود که مقدار ندارد.

به‌عنوان راه دیگر، می‌توانید جفت‌های `key=value` را به این شکل از هم جدا کنید:
`--apiserver-extra-args "enable-admission-plugins=LimitRanger,enable-admission-plugins=NamespaceExists"`
اما در این صورت کلید `enable-admission-plugins` فقط مقدار `NamespaceExists` را خواهد داشت.

یک راه‌حل شناخته‌شده، استفاده از [فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm است.

## زمان‌بندی kube-proxy پیش از آنکه cloud-controller-manager نود را مقداردهی اولیه کند

در سناریوهای مربوط به ارائه‌دهندگان ابری، ممکن است kube-proxy پیش از آنکه cloud-controller-manager
آدرس‌های نود را مقداردهی اولیه کند، روی نودهای worker جدید زمان‌بندی شود. در این صورت kube-proxy
نمی‌تواند آدرس IP نود را به‌درستی دریافت کند و این موضوع بر عملکرد پراکسی در مدیریت
متعادل‌کننده‌های بار (load balancer) نیز اثر زنجیره‌ای می‌گذارد.

خطای زیر را می‌توان در Podهای kube-proxy مشاهده کرد:

```
server.go:610] Failed to retrieve node IP: host IP unknown; known addresses: []
proxier.go:340] invalid nodeIP, initializing kube-proxy with 127.0.0.1 as nodeIP
```

یک راه‌حل شناخته‌شده این است که DaemonSet مربوط به kube-proxy را patch کنید تا بتوان آن را صرف‌نظر از وضعیت نودهای
control-plane روی آن‌ها زمان‌بندی کرد و تا زمانی که شرایط محافظتی اولیه‌ی سایر نودها برطرف نشده است،
روی آن نودها اجرا نشود:

```
kubectl -n kube-system patch ds kube-proxy -p='{
  "spec": {
    "template": {
      "spec": {
        "tolerations": [
          {
            "key": "CriticalAddonsOnly",
            "operator": "Exists"
          },
          {
            "effect": "NoSchedule",
            "key": "node-role.kubernetes.io/control-plane"
          }
        ]
      }
    }
  }
}'
```

برای پیگیری این مشکل می‌توانید به issue مربوط به آن در [اینجا](https://github.com/kubernetes/kubeadm/issues/1027) مراجعه کنید.

## پوشه‌ی `/usr` روی نودها به‌صورت فقط‌خواندنی mount شده است {#usr-mounted-read-only}

در توزیع‌های لینوکسی مانند Fedora CoreOS یا Flatcar Container Linux، پوشه‌ی `/usr` به‌صورت یک سیستم‌فایل فقط‌خواندنی mount می‌شود.
اجزای کوبرنتیز مانند kubelet و kube-controller-manager برای [پشتیبانی از flex-volume](https://github.com/kubernetes/community/blob/ab55d85/contributors/devel/sig-storage/flexvolume.md)
از مسیر پیش‌فرض `/usr/libexec/kubernetes/kubelet-plugins/volume/exec/` استفاده می‌کنند، اما برای کارکرد این قابلیت، پوشه‌ی flex-volume _باید قابل نوشتن باشد_.

{{< note >}}
قابلیت FlexVolume در نسخه‌ی v1.23 کوبرنتیز منسوخ شد.
{{< /note >}}

برای دور زدن این مشکل، می‌توانید پوشه‌ی flex-volume را با استفاده از
[فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm پیکربندی کنید.

روی نود اصلی control plane (که با `kubeadm init` ایجاد شده است)، فایل زیر را با استفاده از
`--config` ارسال کنید:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
nodeRegistration:
  kubeletExtraArgs:
  - name: "volume-plugin-dir"
    value: "/opt/libexec/kubernetes/kubelet-plugins/volume/exec/"
---
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
controllerManager:
  extraArgs:
  - name: "flex-volume-plugin-dir"
    value: "/opt/libexec/kubernetes/kubelet-plugins/volume/exec/"
```

روی نودهایی که به کلاستر می‌پیوندند:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
nodeRegistration:
  kubeletExtraArgs:
  - name: "volume-plugin-dir"
    value: "/opt/libexec/kubernetes/kubelet-plugins/volume/exec/"
```

به‌عنوان راه‌حل جایگزین، می‌توانید فایل `/etc/fstab` را تغییر دهید تا mount پوشه‌ی `/usr` قابل نوشتن شود؛
اما توجه داشته باشید که با این کار یکی از اصول طراحی توزیع لینوکس را تغییر می‌دهید.

## دستور `kubeadm upgrade plan` پیام خطای `context deadline exceeded` را چاپ می‌کند

این پیام خطا هنگام ارتقای کلاستر کوبرنتیز با `kubeadm` در حالتی نمایش داده می‌شود که
از etcd خارجی استفاده می‌کنید. این یک باگ بحرانی نیست و به این دلیل رخ می‌دهد که
نسخه‌های قدیمی‌تر kubeadm نسخه‌ی کلاستر etcd خارجی را بررسی می‌کنند.
می‌توانید با اجرای `kubeadm upgrade apply ...` کار را ادامه دهید.

این مشکل از نسخه‌ی 1.19 برطرف شده است.

## دستور `kubeadm reset` پوشه‌ی `/var/lib/kubelet` را unmount می‌کند

اگر `/var/lib/kubelet` به‌صورت mount‌شده باشد، اجرای `kubeadm reset` عملاً آن را unmount می‌کند.

برای دور زدن این مشکل، پس از انجام عملیات `kubeadm reset`، پوشه‌ی `/var/lib/kubelet` را دوباره mount کنید.

این یک پسرفت (regression) است که در kubeadm 1.15 ایجاد شد. این مشکل در نسخه‌ی 1.20 برطرف شده است.

## امکان استفاده‌ی امن از metrics-server در کلاستر kubeadm وجود ندارد

در کلاستر kubeadm، می‌توان با ارسال `--kubelet-insecure-tls` به [metrics-server](https://github.com/kubernetes-sigs/metrics-server)،
از آن به‌صورت ناامن استفاده کرد. این کار برای کلاسترهای محیط عملیاتی توصیه نمی‌شود.

اگر می‌خواهید بین metrics-server و kubelet از TLS استفاده کنید، با مشکل روبه‌رو می‌شوید؛
زیرا kubeadm یک گواهی سرویس‌دهی خودامضا (self-signed) برای kubelet مستقر می‌کند. این موضوع می‌تواند
خطاهای زیر را در سمت metrics-server ایجاد کند:

```
x509: certificate signed by unknown authority
x509: certificate is valid for IP-foo not IP-bar
```

برای آشنایی با نحوه‌ی پیکربندی kubeletها در کلاستر kubeadm به‌گونه‌ای که گواهی‌های سرویس‌دهی به‌درستی امضاشده داشته باشند،
به [فعال‌سازی گواهی‌های سرویس‌دهی امضاشده‌ی kubelet](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#kubelet-serving-certs) مراجعه کنید.

همچنین [چگونه metrics-server را به‌صورت امن اجرا کنیم](https://github.com/kubernetes-sigs/metrics-server/blob/master/FAQ.md#how-to-run-metrics-server-securely) را ببینید.

## ارتقا به دلیل تغییر نکردن هش etcd شکست می‌خورد

این مورد فقط هنگام ارتقای یک نود control plane با فایل اجرایی kubeadm نسخه‌ی v1.28.3 یا بالاتر صدق می‌کند،
در حالتی که آن نود در حال حاضر با نسخه‌های v1.28.0، v1.28.1 یا v1.28.2 از kubeadm مدیریت می‌شود.

پیام خطایی که ممکن است با آن روبه‌رو شوید به این صورت است:

```
[upgrade/etcd] Failed to upgrade etcd: couldn't upgrade control plane. kubeadm has tried to recover everything into the earlier state. Errors faced: static Pod hash for component etcd on Node kinder-upgrade-control-plane-1 did not change after 5m0s: timed out waiting for the condition
[upgrade/etcd] Waiting for previous etcd to become available
I0907 10:10:09.109104    3704 etcd.go:588] [etcd] attempting to see if all cluster endpoints ([https://172.17.0.6:2379/ https://172.17.0.4:2379/ https://172.17.0.3:2379/]) are available 1/10
[upgrade/etcd] Etcd was rolled back and is now available
static Pod hash for component etcd on Node kinder-upgrade-control-plane-1 did not change after 5m0s: timed out waiting for the condition
couldn't upgrade control plane. kubeadm has tried to recover everything into the earlier state. Errors faced
k8s.io/kubernetes/cmd/kubeadm/app/phases/upgrade.rollbackOldManifests
	cmd/kubeadm/app/phases/upgrade/staticpods.go:525
k8s.io/kubernetes/cmd/kubeadm/app/phases/upgrade.upgradeComponent
	cmd/kubeadm/app/phases/upgrade/staticpods.go:254
k8s.io/kubernetes/cmd/kubeadm/app/phases/upgrade.performEtcdStaticPodUpgrade
	cmd/kubeadm/app/phases/upgrade/staticpods.go:338
...
```

علت این خطا آن است که نسخه‌های آسیب‌دیده یک فایل مانیفست etcd با مقادیر پیش‌فرض ناخواسته
در PodSpec تولید می‌کنند. در نتیجه، مقایسه‌ی مانیفست‌ها تفاوتی را نشان می‌دهد و
kubeadm انتظار تغییر در هش Pod را دارد، اما kubelet هرگز این هش را به‌روزرسانی نمی‌کند.

اگر این مشکل را در کلاستر خود مشاهده کردید، دو راه برای دور زدن آن وجود دارد:

- می‌توان ارتقای etcd را بین نسخه‌های آسیب‌دیده و v1.28.3 (یا بالاتر) با استفاده از دستور زیر نادیده گرفت:

  ```shell
  kubeadm upgrade {apply|node} [version] --etcd-upgrade=false
  ```

  اگر نسخه‌ی جدیدی از etcd در یکی از نسخه‌های وصله‌ای بعدی v1.28 معرفی شده باشد، این روش توصیه نمی‌شود.

- پیش از ارتقا، مانیفست static pod مربوط به etcd را وصله کنید تا ویژگی‌های پیش‌فرض مشکل‌ساز حذف شوند:

  ```patch
  diff --git a/etc/kubernetes/manifests/etcd_defaults.yaml b/etc/kubernetes/manifests/etcd_origin.yaml
  index d807ccbe0aa..46b35f00e15 100644
  --- a/etc/kubernetes/manifests/etcd_defaults.yaml
  +++ b/etc/kubernetes/manifests/etcd_origin.yaml
  @@ -43,7 +43,6 @@ spec:
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
  -      successThreshold: 1
        timeoutSeconds: 15
      name: etcd
      resources:
  @@ -59,26 +58,18 @@ spec:
          scheme: HTTP
        initialDelaySeconds: 10
        periodSeconds: 10
  -      successThreshold: 1
        timeoutSeconds: 15
  -    terminationMessagePath: /dev/termination-log
  -    terminationMessagePolicy: File
      volumeMounts:
      - mountPath: /var/lib/etcd
        name: etcd-data
      - mountPath: /etc/kubernetes/pki/etcd
        name: etcd-certs
  -  dnsPolicy: ClusterFirst
  -  enableServiceLinks: true
    hostNetwork: true
    priority: 2000001000
    priorityClassName: system-node-critical
  -  restartPolicy: Always
  -  schedulerName: default-scheduler
    securityContext:
      seccompProfile:
        type: RuntimeDefault
  -  terminationGracePeriodSeconds: 30
    volumes:
    - hostPath:
        path: /etc/kubernetes/pki/etcd
  ```

اطلاعات بیشتر درباره‌ی این باگ را می‌توانید در
[issue پیگیری](https://github.com/kubernetes/kubeadm/issues/2927) آن بیابید.
