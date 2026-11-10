---
reviewers:
- sig-cluster-lifecycle
title: مدیریت گواهی‌ها با kubeadm
content_type: task
weight: 80
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.15" state="stable" >}}

گواهی‌های کلاینتی که [kubeadm](/docs/reference/setup-tools/kubeadm/) تولید می‌کند پس از یک سال منقضی می‌شوند.
این صفحه توضیح می‌دهد که چگونه تمدید گواهی‌ها را با kubeadm مدیریت کنید. همچنین سایر کارهای مرتبط با
مدیریت گواهی‌ها در kubeadm را پوشش می‌دهد.

پروژه کوبرنتیز توصیه می‌کند که به‌روزرسانی به آخرین نسخه‌های وصله (patch) را بی‌درنگ انجام دهید و
مطمئن شوید که یکی از نسخه‌های فرعی (minor) پشتیبانی‌شده کوبرنتیز را اجرا می‌کنید.
پیروی از این توصیه به حفظ امنیت شما کمک می‌کند.


## {{% heading "prerequisites" %}}


باید با [گواهی‌های PKI و الزامات آن‌ها در کوبرنتیز](/docs/setup/best-practices/certificates/) آشنا باشید.

باید بدانید که چگونه یک فایل [پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) را به دستورهای kubeadm بدهید.

این راهنما استفاده از دستور `openssl` را پوشش می‌دهد (که در صورت انتخاب روش امضای دستی گواهی‌ها
از آن استفاده می‌شود)، اما می‌توانید از ابزارهای دلخواه خود استفاده کنید.

در برخی از مراحل این راهنما برای دسترسی مدیریتی از `sudo` استفاده شده است. می‌توانید از هر ابزار معادلی استفاده کنید.

<!-- steps -->

## استفاده از گواهی‌های سفارشی {#custom-certificates}

به‌طور پیش‌فرض، kubeadm همه گواهی‌های لازم برای اجرای یک کلاستر را تولید می‌کند.
می‌توانید با فراهم کردن گواهی‌های خودتان این رفتار را تغییر دهید.

برای این کار، باید گواهی‌ها را در دایرکتوری‌ای قرار دهید که با فلگ `--cert-dir`
یا فیلد `certificatesDir` در `ClusterConfiguration` مربوط به kubeadm مشخص شده است.
این دایرکتوری به‌طور پیش‌فرض `/etc/kubernetes/pki` است.

اگر یک جفت گواهی و کلید خصوصی پیش از اجرای `kubeadm init` وجود داشته باشد،
kubeadm آن‌ها را بازنویسی نمی‌کند. برای مثال، این یعنی می‌توانید یک CA موجود را
در `/etc/kubernetes/pki/ca.crt` و `/etc/kubernetes/pki/ca.key` کپی کنید
تا kubeadm از همین CA برای امضای سایر گواهی‌ها استفاده کند.

## انتخاب الگوریتم رمزنگاری {#choosing-encryption-algorithm}

در kubeadm می‌توانید الگوریتم رمزنگاری مورد استفاده برای ایجاد کلیدهای عمومی و خصوصی را انتخاب کنید.
این کار با استفاده از فیلد `encryptionAlgorithm` در پیکربندی kubeadm انجام می‌شود:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
encryptionAlgorithm: <ALGORITHM>
```

مقدار `<ALGORITHM>` می‌تواند یکی از `RSA-2048` (پیش‌فرض)، `RSA-3072`، `RSA-4096` یا `ECDSA-P256` باشد.

## انتخاب دوره اعتبار گواهی‌ها {#choosing-cert-validity-period}

در kubeadm می‌توانید دوره اعتبار گواهی‌های CA و گواهی‌های برگ (leaf) را انتخاب کنید.
این کار با استفاده از فیلدهای `certificateValidityPeriod` و `caCertificateValidityPeriod`
در پیکربندی kubeadm انجام می‌شود:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
certificateValidityPeriod: 8760h # Default: 365 days × 24 hours = 1 year
caCertificateValidityPeriod: 87600h # Default: 365 days × 24 hours * 10 = 10 years
```

مقادیر این فیلدها از قالب پذیرفته‌شده برای
[مقادیر `time.Duration` در Go](https://pkg.go.dev/time#ParseDuration) پیروی می‌کنند و بزرگ‌ترین
واحد پشتیبانی‌شده `h` (ساعت) است.

## حالت CA خارجی {#external-ca-mode}

همچنین می‌توان فقط فایل `ca.crt` را فراهم کرد و فایل `ca.key` را فراهم نکرد
(این امکان فقط برای فایل CA ریشه وجود دارد و برای سایر جفت‌گواهی‌ها در دسترس نیست).
اگر همه گواهی‌ها و فایل‌های kubeconfig دیگر در جای خود باشند، kubeadm این وضعیت را تشخیص می‌دهد
و حالت «CA خارجی» را فعال می‌کند. در این حالت، kubeadm بدون وجود کلید CA روی دیسک
کار خود را ادامه می‌دهد.

در عوض، controller-manager را به‌صورت مستقل با `--controllers=csrsigner` اجرا کنید و
آن را به گواهی و کلید CA ارجاع دهید.

برای آماده‌سازی اعتبارنامه‌های مؤلفه‌ها در حالت CA خارجی، روش‌های گوناگونی وجود دارد.

### آماده‌سازی دستی اعتبارنامه‌های مؤلفه‌ها

صفحه [گواهی‌های PKI و الزامات آن‌ها](/docs/setup/best-practices/certificates/) اطلاعاتی
درباره نحوه آماده‌سازی دستی همه اعتبارنامه‌های مؤلفه‌هایی که kubeadm به آن‌ها نیاز دارد ارائه می‌کند.

این راهنما استفاده از دستور `openssl` را پوشش می‌دهد (که در صورت انتخاب روش امضای دستی گواهی‌ها
از آن استفاده می‌شود)، اما می‌توانید از ابزارهای دلخواه خود استفاده کنید.

### آماده‌سازی اعتبارنامه‌ها با امضای CSRهای تولیدشده توسط kubeadm

ابزار kubeadm می‌تواند [فایل‌های CSR تولید کند](#signing-csr) که می‌توانید آن‌ها را به‌صورت دستی با ابزارهایی مانند
`openssl` و CA خارجی خود امضا کنید. این فایل‌های CSR همه مشخصات اعتبارنامه‌هایی را دربر دارند
که مؤلفه‌های مستقرشده با kubeadm به آن‌ها نیاز دارند.

### آماده‌سازی خودکار اعتبارنامه‌های مؤلفه‌ها با استفاده از فازهای kubeadm

به‌عنوان جایگزین، می‌توان از دستورهای فاز (phase) در kubeadm برای خودکارسازی این فرایند استفاده کرد.

- به میزبانی بروید که می‌خواهید آن را به‌عنوان نود control plane در kubeadm با CA خارجی آماده کنید.
- فایل‌های CA خارجی خود، یعنی `ca.crt` و `ca.key`، را در مسیر `/etc/kubernetes/pki` روی آن نود کپی کنید.
- یک [فایل پیکربندی kubeadm](/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file) موقت
با نام `config.yaml` آماده کنید که بتوان آن را با `kubeadm init` استفاده کرد. مطمئن شوید که این فایل
همه اطلاعات مرتبط در سطح کلاستر یا مختص میزبان را که ممکن است در گواهی‌ها گنجانده شوند دربر دارد؛ مانند
`ClusterConfiguration.controlPlaneEndpoint`، `ClusterConfiguration.certSANs` و `InitConfiguration.APIEndpoint`.
- روی همان میزبان، دستورهای `kubeadm init phase kubeconfig all --config config.yaml` و
`kubeadm init phase certs all --config config.yaml` را اجرا کنید. با این کار همه فایل‌های kubeconfig
و گواهی‌های لازم در مسیر `/etc/kubernetes/` و زیردایرکتوری `pki` آن تولید می‌شوند.
- فایل‌های تولیدشده را بررسی کنید. فایل `/etc/kubernetes/pki/ca.key` را حذف کنید و فایل
`/etc/kubernetes/super-admin.conf` را حذف کنید یا به مکانی امن منتقل کنید.
- روی نودهایی که `kubeadm join` روی آن‌ها اجرا خواهد شد، فایل `/etc/kubernetes/kubelet.conf` را نیز حذف کنید.
این فایل فقط روی نخستین نودی لازم است که `kubeadm init` روی آن اجرا می‌شود.
- توجه کنید که برخی فایل‌ها، مانند `pki/sa.*`، `pki/front-proxy-ca.*` و `pki/etc/ca.*`، میان
نودهای control plane مشترک هستند. می‌توانید آن‌ها را یک بار تولید کنید و
[به‌صورت دستی توزیع کنید](/docs/setup/production-environment/tools/kubeadm/high-availability/#manual-certs)
روی نودهایی که `kubeadm join` روی آن‌ها اجرا خواهد شد، یا برای خودکارسازی این توزیع از قابلیت
[`--upload-certs`](/docs/setup/production-environment/tools/kubeadm/high-availability/#stacked-control-plane-and-etcd-nodes)
در `kubeadm init` و `--certificate-key` در `kubeadm join` استفاده کنید.

پس از آماده‌شدن اعتبارنامه‌ها روی همه نودها، `kubeadm init` و `kubeadm join` را روی این نودها اجرا کنید تا
به کلاستر بپیوندند. kubeadm از فایل‌های kubeconfig و گواهی‌های موجود در مسیر `/etc/kubernetes/`
و زیردایرکتوری `pki` آن استفاده خواهد کرد.

## انقضا و مدیریت گواهی‌ها {#check-certificate-expiration}

{{< note >}}
ابزار `kubeadm` نمی‌تواند گواهی‌هایی را که یک CA خارجی امضا کرده است مدیریت کند.
{{< /note >}}

برای بررسی زمان انقضای گواهی‌ها می‌توانید از زیردستور `check-expiration` استفاده کنید:

```shell
kubeadm certs check-expiration
```

خروجی مشابه زیر است:

```console
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Dec 30, 2020 23:36 UTC   364d                                    no
apiserver                  Dec 30, 2020 23:36 UTC   364d            ca                      no
apiserver-etcd-client      Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
apiserver-kubelet-client   Dec 30, 2020 23:36 UTC   364d            ca                      no
controller-manager.conf    Dec 30, 2020 23:36 UTC   364d                                    no
etcd-healthcheck-client    Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
etcd-peer                  Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
etcd-server                Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
front-proxy-client         Dec 30, 2020 23:36 UTC   364d            front-proxy-ca          no
scheduler.conf             Dec 30, 2020 23:36 UTC   364d                                    no

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Dec 28, 2029 23:36 UTC   9y              no
etcd-ca                 Dec 28, 2029 23:36 UTC   9y              no
front-proxy-ca          Dec 28, 2029 23:36 UTC   9y              no
```

این دستور زمان انقضا و زمان باقی‌مانده را برای گواهی‌های کلاینت در پوشه
`/etc/kubernetes/pki` و نیز برای گواهی کلاینتِ جاسازی‌شده در فایل‌های kubeconfig مورد استفاده
kubeadm (`admin.conf`، `controller-manager.conf` و `scheduler.conf`) نمایش می‌دهد.

افزون بر این، kubeadm به کاربر اطلاع می‌دهد که آیا گواهی به‌صورت خارجی مدیریت می‌شود یا نه؛ در این صورت،
کاربر باید خودش تمدید گواهی را به‌صورت دستی یا با ابزارهای دیگر مدیریت کند.

فایل پیکربندی `kubelet.conf` در فهرست بالا گنجانده نشده است، زیرا kubeadm
kubelet را برای [تمدید خودکار گواهی‌ها](/docs/tasks/tls/certificate-rotation/)
با گواهی‌های قابل چرخش در مسیر `/var/lib/kubelet/pki` پیکربندی می‌کند.
برای ترمیم گواهی کلاینت منقضی‌شده kubelet، به
[شکست در چرخش گواهی کلاینت kubelet](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/#kubelet-client-cert) مراجعه کنید.

{{< note >}}
روی نودهایی که با `kubeadm init` از نسخه‌های پیش از kubeadm 1.17 ایجاد شده‌اند،
[اشکالی](https://github.com/kubernetes/kubeadm/issues/1753) وجود دارد که باعث می‌شود محتوای
`kubelet.conf` را به‌صورت دستی تغییر دهید. پس از پایان `kubeadm init`، باید `kubelet.conf` را به‌روزرسانی کنید تا
به گواهی‌های کلاینت چرخش‌یافته kubelet اشاره کند؛ برای این کار، `client-certificate-data` و
`client-key-data` را با موارد زیر جایگزین کنید:

```yaml
client-certificate: /var/lib/kubelet/pki/kubelet-client-current.pem
client-key: /var/lib/kubelet/pki/kubelet-client-current.pem
```
{{< /note >}}

## تمدید خودکار گواهی‌ها

ابزار kubeadm همه گواهی‌ها را هنگام [ارتقای](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
control plane تمدید می‌کند.

این قابلیت برای ساده‌ترین موارد استفاده طراحی شده است؛
اگر نیازمندی خاصی برای تمدید گواهی‌ها ندارید و ارتقای نسخه کوبرنتیز را به‌طور منظم
(با فاصله کمتر از یک سال میان هر ارتقا) انجام می‌دهید، kubeadm کلاستر شما را به‌روز و
به اندازه کافی امن نگه می‌دارد.

اگر نیازمندی‌های پیچیده‌تری برای تمدید گواهی‌ها دارید، می‌توانید با دادن `--certificate-renewal=false`
به `kubeadm upgrade apply` یا `kubeadm upgrade node` از رفتار پیش‌فرض صرف‌نظر کنید.

## تمدید دستی گواهی‌ها

هر زمان که بخواهید، می‌توانید گواهی‌های خود را به‌صورت دستی با دستور `kubeadm certs renew` و
گزینه‌های خط فرمان مناسب تمدید کنید. اگر کلاستری با control plane تکثیرشده اجرا می‌کنید، این دستور
باید روی همه نودهای control plane اجرا شود.

این دستور تمدید را با استفاده از گواهی و کلید CA (یا front-proxy-CA) ذخیره‌شده در `/etc/kubernetes/pki` انجام می‌دهد.

دستور `kubeadm certs renew` گواهی‌های موجود را منبع معتبر برای ویژگی‌ها
(Common Name، Organization، subject alternative name) در نظر می‌گیرد و به ConfigMap
`kubeadm-config` تکیه نمی‌کند.
با این حال، پروژه کوبرنتیز توصیه می‌کند که گواهی ارائه‌شده و مقادیر مرتبط با آن در این ConfigMap
همگام نگه داشته شوند تا از هرگونه خطر سردرگمی جلوگیری شود.

پس از اجرای این دستور باید Podهای control plane را مجدداً راه‌اندازی کنید. این کار لازم است، زیرا
بارگذاری مجدد پویای گواهی‌ها در حال حاضر برای همه مؤلفه‌ها و گواهی‌ها پشتیبانی نمی‌شود.
[Podهای ایستا](/docs/tasks/configure-pod-container/static-pod/) را kubelet محلی مدیریت می‌کند،
نه API Server؛ بنابراین نمی‌توان از kubectl برای حذف و راه‌اندازی مجدد آن‌ها استفاده کرد.
برای راه‌اندازی مجدد یک Pod ایستا، می‌توانید فایل مانیفست آن را به‌طور موقت از `/etc/kubernetes/manifests/` بردارید
و ۲۰ ثانیه صبر کنید (مقدار `fileCheckFrequency` را در [ساختار KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/) ببینید).
اگر Pod دیگر در دایرکتوری مانیفست‌ها نباشد، kubelet آن را خاتمه می‌دهد.
سپس می‌توانید فایل را به جای خود برگردانید؛ پس از گذشت یک دوره `fileCheckFrequency` دیگر، kubelet
Pod را دوباره ایجاد می‌کند و تمدید گواهی برای آن مؤلفه کامل می‌شود.

دستور `kubeadm certs renew` می‌تواند هر گواهی مشخصی را تمدید کند یا با زیردستور `all` همه آن‌ها را تمدید کند:

```shell
# If you are running cluster with a replicated control plane, this command
# needs to be executed on all the control-plane nodes.
kubeadm certs renew all
```

### کپی کردن گواهی مدیر (اختیاری) {#admin-certificate-copy}

در کلاسترهایی که با kubeadm ساخته شده‌اند، معمولاً گواهی `admin.conf` در
`$HOME/.kube/config` کپی می‌شود؛ همان‌طور که در [ایجاد کلاستر با kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/) آمده است.
در چنین سیستمی، برای به‌روزرسانی محتوای `$HOME/.kube/config`
پس از تمدید `admin.conf`، می‌توانید دستورهای زیر را اجرا کنید:

```shell
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

## تمدید گواهی‌ها با API گواهی‌های کوبرنتیز

این بخش جزئیات بیشتری درباره نحوه تمدید دستی گواهی‌ها با استفاده از API گواهی‌های کوبرنتیز ارائه می‌کند.

{{< caution >}}
این موضوعات پیشرفته برای کاربرانی است که باید زیرساخت گواهی سازمان خود را با کلاستری
که با kubeadm ساخته شده است یکپارچه کنند. اگر پیکربندی پیش‌فرض kubeadm نیازهای شما را برآورده می‌کند،
بهتر است مدیریت گواهی‌ها را به kubeadm بسپارید.
{{< /caution >}}

### راه‌اندازی امضاکننده

مرجع صدور گواهی (Certificate Authority) کوبرنتیز به‌صورت پیش‌فرض و بدون پیکربندی کار نمی‌کند.
می‌توانید یک امضاکننده خارجی مانند [cert-manager](https://cert-manager.io/docs/configuration/ca/) پیکربندی کنید
یا از امضاکننده داخلی استفاده کنید.

امضاکننده داخلی بخشی از [`kube-controller-manager`](/docs/reference/command-line-tools-reference/kube-controller-manager/) است.

برای فعال کردن امضاکننده داخلی، باید فلگ‌های `--cluster-signing-cert-file` و
`--cluster-signing-key-file` را تنظیم کنید.

اگر کلاستر جدیدی ایجاد می‌کنید، می‌توانید از یک
[فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) kubeadm استفاده کنید:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
controllerManager:
  extraArgs:
  - name: "cluster-signing-cert-file"
    value: "/etc/kubernetes/pki/ca.crt"
  - name: "cluster-signing-key-file"
    value: "/etc/kubernetes/pki/ca.key"
```

### ایجاد درخواست‌های امضای گواهی (CSR)

برای ایجاد CSR با API کوبرنتیز، به [ایجاد CertificateSigningRequest](/docs/reference/access-authn-authz/certificate-signing-requests/#create-certificatessigningrequest)
مراجعه کنید.

## تمدید گواهی‌ها با CA خارجی

این بخش جزئیات بیشتری درباره نحوه تمدید دستی گواهی‌ها با استفاده از یک CA خارجی ارائه می‌کند.

برای یکپارچگی بهتر با CAهای خارجی، kubeadm می‌تواند درخواست‌های امضای گواهی (CSR) نیز تولید کند.
هر CSR درخواستی است که از یک CA برای دریافت گواهی امضاشده برای یک کلاینت ارسال می‌شود.
در اصطلاح kubeadm، هر گواهی‌ای که به‌طور معمول با یک CA روی دیسک امضا می‌شود، می‌تواند در عوض
به‌صورت یک CSR تولید شود. با این حال، خود CA را نمی‌توان به‌صورت CSR تولید کرد.

### تمدید با استفاده از درخواست‌های امضای گواهی (CSR)

تمدید گواهی‌ها با تولید CSRهای جدید و امضای آن‌ها با CA خارجی امکان‌پذیر است.
برای جزئیات بیشتر درباره کار با CSRهای تولیدشده توسط kubeadm، به بخش
[امضای درخواست‌های امضای گواهی (CSR) تولیدشده توسط kubeadm](#signing-csr) مراجعه کنید.

## چرخش مرجع صدور گواهی (CA) {#certificate-authority-rotation}

ابزار kubeadm به‌صورت پیش‌فرض از چرخش یا جایگزینی گواهی‌های CA پشتیبانی نمی‌کند.

برای اطلاعات بیشتر درباره چرخش یا جایگزینی دستی CA، به [چرخش دستی گواهی‌های CA](/docs/tasks/tls/manual-rotation-of-ca-certificates/) مراجعه کنید.

## فعال‌سازی گواهی‌های امضاشدهٔ سرویس‌دهی kubelet {#kubelet-serving-certs}

به‌طور پیش‌فرض، گواهی سرویس‌دهی kubelet که kubeadm مستقر می‌کند خودامضا (self-signed) است.
در نتیجه، اتصال سرویس‌های خارجی مانند
[metrics-server](https://github.com/kubernetes-sigs/metrics-server) به kubelet را نمی‌توان با TLS ایمن کرد.

برای اینکه kubeletها در یک کلاستر جدید kubeadm گواهی‌های سرویس‌دهیِ به‌درستی امضاشده دریافت کنند،
باید پیکربندی حداقلی زیر را به `kubeadm init` بدهید:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
serverTLSBootstrap: true
```

اگر کلاستر را از قبل ایجاد کرده‌اید، باید آن را به این صورت تطبیق دهید:
 - ConfigMap با نام `kubelet-config` را در فضای نام (namespace) `kube-system` پیدا و ویرایش کنید.
در این ConfigMap، مقدار کلید `kubelet` یک سند
[KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/)
است. این سند KubeletConfiguration را ویرایش کنید تا `serverTLSBootstrap: true` تنظیم شود.
- روی هر نود، فیلد `serverTLSBootstrap: true` را به `/var/lib/kubelet/config.yaml` اضافه کنید
و kubelet را با `systemctl restart kubelet` دوباره راه‌اندازی کنید.

فیلد `serverTLSBootstrap: true` راه‌اندازی اولیهٔ (bootstrap) گواهی‌های سرویس‌دهی kubelet را از طریق درخواست
آن‌ها از API با نام `certificates.k8s.io` فعال می‌کند. یکی از محدودیت‌های شناخته‌شده این است که
امضاکنندهٔ پیش‌فرض در kube-controller-manager، یعنی
[`kubernetes.io/kubelet-serving`](/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers)،
نمی‌تواند درخواست‌های امضای گواهی (CSR) مربوط به این گواهی‌ها را به‌طور خودکار تأیید کند.
بنابراین تأیید آن‌ها به اقدام کاربر یا یک کنترل‌کنندهٔ شخص ثالث نیاز دارد.

این CSRها را می‌توانید با دستور زیر مشاهده کنید:

```shell
kubectl get csr
```
```console
NAME        AGE     SIGNERNAME                        REQUESTOR                      CONDITION
csr-9wvgt   112s    kubernetes.io/kubelet-serving     system:node:worker-1           Pending
csr-lz97v   1m58s   kubernetes.io/kubelet-serving     system:node:control-plane-1    Pending
```

برای تأیید آن‌ها می‌توانید این کار را انجام دهید:
```shell
kubectl certificate approve <CSR-name>
```

به‌طور پیش‌فرض، این گواهی‌های سرویس‌دهی پس از یک سال منقضی می‌شوند. ابزار kubeadm فیلد
`rotateCertificates` در `KubeletConfiguration` را روی `true` تنظیم می‌کند؛ یعنی نزدیک به زمان انقضا،
مجموعهٔ جدیدی از CSRها برای گواهی‌های سرویس‌دهی ایجاد می‌شود که برای تکمیل چرخش گواهی باید تأیید شوند.
برای اطلاعات بیشتر، [چرخش گواهی](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#certificate-rotation)
را ببینید.

اگر به دنبال راهکاری برای تأیید خودکار این CSRها هستید، توصیه می‌شود با ارائه‌دهندهٔ ابری خود تماس بگیرید
و بپرسید آیا امضاکننده‌ای برای CSR دارند که هویت نود را با یک سازوکار خارج از باند (out of band) راستی‌آزمایی کند.

{{% thirdparty-content %}}

می‌توان از کنترل‌کننده‌های سفارشی شخص ثالث استفاده کرد:
- [kubelet-csr-approver](https://github.com/postfinance/kubelet-csr-approver)

چنین کنترل‌کننده‌ای تنها زمانی سازوکاری امن است که علاوه بر CommonName موجود در CSR،
نشانی‌های IP و نام‌های دامنهٔ درخواست‌شده را نیز راستی‌آزمایی کند. این کار مانع می‌شود که
عاملی مخرب با دسترسی به گواهی کلاینت یک kubelet، برای هر IP یا نام دامنه‌ای CSR درخواست گواهی سرویس‌دهی ایجاد کند.

## تولید فایل‌های kubeconfig برای کاربران دیگر {#kubeconfig-additional-users}

هنگام ایجاد کلاستر، `kubeadm init` گواهی موجود در `super-admin.conf` را طوری امضا می‌کند
که `Subject: O = system:masters, CN = kubernetes-super-admin` داشته باشد.
گروه [`system:masters`](/docs/reference/access-authn-authz/rbac/#user-facing-roles)
یک گروه ابرکاربری برای دسترسی اضطراری (break-glass) است که لایهٔ مجوزدهی (برای نمونه
[RBAC](/docs/reference/access-authn-authz/rbac/)) را دور می‌زند. ابزار kubeadm فایل `admin.conf` را نیز
روی نودهای control plane ایجاد می‌کند و این فایل گواهی‌ای با
`Subject: O = kubeadm:cluster-admins, CN = kubernetes-admin` دارد. گروه `kubeadm:cluster-admins`
از نظر منطقی به kubeadm تعلق دارد. اگر کلاستر شما از RBAC استفاده کند
(که پیش‌فرض kubeadm است)، گروه `kubeadm:cluster-admins` به ClusterRole با نام
[`cluster-admin`](/docs/reference/access-authn-authz/rbac/#user-facing-roles) متصل (bind) می‌شود.

{{< warning >}}
از اشتراک‌گذاری فایل‌های `super-admin.conf` یا `admin.conf` خودداری کنید. به‌جای آن، حتی برای کسانی
که در نقش مدیر کار می‌کنند، دسترسی با کمترین امتیاز (least privilege) ایجاد کنید و برای هر کاری
به‌جز دسترسی اضطراری از همین جایگزینِ کم‌امتیاز استفاده کنید.
{{< /warning >}}

برای تولید فایل‌های kubeconfig برای کاربران دیگر می‌توانید از دستور
[`kubeadm kubeconfig user`](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig) استفاده کنید.
این دستور ترکیبی از فلگ‌های خط فرمان و گزینه‌های
[پیکربندی kubeadm](/docs/reference/config-api/kubeadm-config.v1beta4/) را می‌پذیرد.
فایل kubeconfig تولیدشده در stdout نوشته می‌شود و می‌توان آن را با
`kubeadm kubeconfig user ... > somefile.conf` به یک فایل هدایت کرد.

نمونه‌ای از فایل پیکربندی که می‌توان با `--config` از آن استفاده کرد:

```yaml
# example.yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
# Will be used as the target "cluster" in the kubeconfig
clusterName: "kubernetes"
# Will be used as the "server" (IP or DNS name) of this cluster in the kubeconfig
controlPlaneEndpoint: "some-dns-address:6443"
# The cluster CA key and certificate will be loaded from this local directory
certificatesDir: "/etc/kubernetes/pki"
```

مطمئن شوید که این تنظیمات با تنظیمات کلاستر مقصد مورد نظر مطابقت دارند.
برای مشاهدهٔ تنظیمات یک کلاستر موجود از دستور زیر استفاده کنید:

```shell
kubectl get cm kubeadm-config -n kube-system -o=jsonpath="{.data.ClusterConfiguration}"
```

مثال زیر یک فایل kubeconfig با اعتبارنامه‌هایی که ۲۴ ساعت معتبرند برای کاربر جدید `johndoe`
که عضو گروه `appdevs` است تولید می‌کند:

```shell
kubeadm kubeconfig user --config example.yaml --org appdevs --client-name johndoe --validity-period 24h
```

مثال زیر یک فایل kubeconfig با اعتبارنامه‌های مدیر که یک هفته معتبرند تولید می‌کند:

```shell
kubeadm kubeconfig user --config example.yaml --client-name admin --validity-period 168h
```

## امضای درخواست‌های امضای گواهی (CSR) تولیدشده توسط kubeadm {#signing-csr}

با `kubeadm certs generate-csr` می‌توانید درخواست‌های امضای گواهی ایجاد کنید.
اجرای این دستور برای گواهی‌های معمولی، جفت فایل‌های `.csr` / `.key` تولید می‌کند. برای گواهی‌هایی
که در فایل‌های kubeconfig جاسازی می‌شوند، این دستور جفت `.csr` / `.conf` تولید می‌کند که در آن
کلید از قبل در فایل `.conf` جاسازی شده است.

هر فایل CSR همهٔ اطلاعات لازم برای امضای یک گواهی توسط مرجع صدور گواهی (CA) را در بر دارد.
ابزار kubeadm برای همهٔ گواهی‌ها و CSRهای خود از یک
[مشخصهٔ کاملاً تعریف‌شده](/docs/setup/best-practices/certificates/#all-certificates)
پیروی می‌کند.

پوشهٔ پیش‌فرض گواهی‌ها `/etc/kubernetes/pki` و پوشهٔ پیش‌فرض فایل‌های kubeconfig
`/etc/kubernetes` است. این مقادیر پیش‌فرض را می‌توان به‌ترتیب با فلگ‌های `--cert-dir` و
`--kubeconfig-dir` تغییر داد.

برای ارسال گزینه‌های سفارشی به `kubeadm certs generate-csr` از فلگ `--config` استفاده کنید
که، مشابه دستوراتی مانند `kubeadm init`، یک فایل
[پیکربندی kubeadm](/docs/reference/config-api/kubeadm-config.v1beta4/) می‌پذیرد. هر مشخصه‌ای،
مانند SANهای اضافی و نشانی‌های IP سفارشی، باید در همان فایل پیکربندی ذخیره شود و با ارسال آن
از طریق `--config` برای همهٔ دستورات مرتبط kubeadm به کار رود.

{{< note >}}
این راهنما از پوشهٔ پیش‌فرض کوبرنتیز، یعنی `/etc/kubernetes`، استفاده می‌کند که به دسترسی ابرکاربر نیاز دارد.
اگر هنگام پیروی از این راهنما از پوشه‌هایی استفاده می‌کنید که اجازهٔ نوشتن در آن‌ها را دارید
(که معمولاً یعنی `kubeadm` را با `--cert-dir` و `--kubeconfig-dir` اجرا می‌کنید)،
می‌توانید دستور `sudo` را حذف کنید.

در این صورت باید فایل‌هایی را که تولید کرده‌اید به داخل پوشهٔ `/etc/kubernetes` کپی کنید
تا `kubeadm init` یا `kubeadm join` آن‌ها را پیدا کنند.
{{< /note >}}

### آماده‌سازی فایل‌های CA و حساب سرویس

روی نود اصلی control plane، یعنی جایی که `kubeadm init` اجرا خواهد شد، دستورات زیر را اجرا کنید:

```shell
sudo kubeadm init phase certs ca
sudo kubeadm init phase certs etcd-ca
sudo kubeadm init phase certs front-proxy-ca
sudo kubeadm init phase certs sa
```

این دستورات پوشه‌های `/etc/kubernetes/pki` و `/etc/kubernetes/pki/etcd` را با همهٔ فایل‌های CA
خودامضا (گواهی‌ها و کلیدها) و فایل‌های حساب سرویس (کلیدهای عمومی و خصوصی) که kubeadm برای
یک نود control plane نیاز دارد پر می‌کنند.

{{< note >}}
اگر از یک CA خارجی استفاده می‌کنید، باید همین فایل‌ها را به‌صورت خارج از باند تولید کنید و
آن‌ها را به‌طور دستی در `/etc/kubernetes` روی نود اصلی control plane کپی کنید.

پس از امضای همهٔ CSRها، می‌توانید کلید CA ریشه (`ca.key`) را حذف کنید؛ همان‌طور که در بخش
[حالت CA خارجی](#external-ca-mode) آمده است.
{{< /note >}}

برای نودهای ثانویهٔ control plane (`kubeadm join --control-plane`) نیازی به اجرای دستورات بالا نیست.
بسته به اینکه کلاستر [با دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/high-availability)
را چگونه راه‌اندازی کرده‌اید، یا باید همین فایل‌ها را به‌طور دستی از نود اصلی control plane کپی کنید،
یا از قابلیت خودکار `--upload-certs` در `kubeadm init` استفاده کنید.

### تولید CSRها

دستور `kubeadm certs generate-csr` برای همهٔ گواهی‌های شناخته‌شده‌ای که kubeadm مدیریت می‌کند CSR
تولید می‌کند. پس از پایان اجرای دستور، باید فایل‌های `.csr`، `.conf` یا `.key` را که به آن‌ها
نیاز ندارید به‌طور دستی حذف کنید.

#### ملاحظات مربوط به kubelet.conf {#considerations-kubelet-conf}

این بخش هم برای نودهای control plane و هم برای نودهای کارگر کاربرد دارد.

اگر فایل `ca.key` را از نودهای control plane حذف کرده باشید
([حالت CA خارجی](#external-ca-mode))، kube-controller-manager فعال در این کلاستر نمی‌تواند
گواهی‌های کلاینت kubelet را امضا کند. اگر در محیط شما روش خارجی‌ای برای امضای این گواهی‌ها
وجود ندارد (مانند یک [امضاکنندهٔ خارجی](#set-up-a-signer))، می‌توانید `kubelet.conf.csr` را
همان‌طور که در این راهنما توضیح داده شده به‌طور دستی امضا کنید.

توجه کنید که این یعنی
[چرخش خودکار گواهی کلاینت kubelet](/docs/tasks/tls/certificate-rotation/#enabling-client-certificate-rotation)
نیز غیرفعال خواهد شد. در این صورت، نزدیک به زمان انقضای گواهی باید یک `kubelet.conf.csr` جدید
تولید کنید، گواهی را امضا کنید، آن را در `kubelet.conf` جاسازی کنید و kubelet را دوباره راه‌اندازی کنید.

اگر این موضوع در محیط شما صدق نمی‌کند، می‌توانید پردازش `kubelet.conf.csr` را روی نودهای ثانویهٔ
control plane و نودهای کارگر (همهٔ نودهایی که `kubeadm join ...` را اجرا می‌کنند) نادیده بگیرید؛
زیرا kube-controller-manager فعال مسئول امضای گواهی‌های جدید کلاینت kubelet خواهد بود.

{{< note >}}
فایل `kubelet.conf.csr` را باید روی نود اصلی control plane (میزبانی که در ابتدا `kubeadm init` را
روی آن اجرا کردید) پردازش کنید؛ زیرا `kubeadm` آن را نودی می‌داند که کلاستر را راه‌اندازی اولیه
می‌کند و به یک `kubelet.conf` از پیش پرشده نیاز است.
{{< /note >}}

#### نودهای control plane

دستور زیر را روی نودهای اصلی (`kubeadm init`) و ثانویهٔ (`kubeadm join --control-plane`)
control plane اجرا کنید تا همهٔ فایل‌های CSR تولید شوند:

```shell
sudo kubeadm certs generate-csr
```

اگر قرار است از etcd خارجی استفاده شود، راهنمای
[etcd خارجی با kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/#external-etcd-nodes)
را دنبال کنید تا بدانید کدام فایل‌های CSR روی نودهای kubeadm و etcd لازم هستند. سایر فایل‌های
`.csr` و `.key` در مسیر `/etc/kubernetes/pki/etcd` را می‌توان حذف کرد.

بر اساس توضیحات بخش
[ملاحظات مربوط به kubelet.conf](#considerations-kubelet-conf)، فایل‌های `kubelet.conf` و
`kubelet.conf.csr` را نگه دارید یا حذف کنید.

#### نودهای کارگر

بر اساس توضیحات بخش
[ملاحظات مربوط به kubelet.conf](#considerations-kubelet-conf)، در صورت تمایل دستور زیر را اجرا کنید:

```shell
sudo kubeadm certs generate-csr
```

و فقط فایل‌های `kubelet.conf` و `kubelet.conf.csr` را نگه دارید. همچنین می‌توانید مراحل مربوط
به نودهای کارگر را به‌طور کامل نادیده بگیرید.

### امضای CSRها برای همهٔ گواهی‌ها

{{< note >}}
اگر از CA خارجی استفاده می‌کنید و از قبل فایل‌های شمارهٔ سریال CA (`.srl`) برای `openssl` دارید،
می‌توانید این فایل‌ها را به نودی از kubeadm که CSRها روی آن پردازش می‌شوند کپی کنید.
فایل‌های `.srl` که باید کپی شوند عبارت‌اند از `/etc/kubernetes/pki/ca.srl`،
`/etc/kubernetes/pki/front-proxy-ca.srl` و `/etc/kubernetes/pki/etcd/ca.srl`.
سپس می‌توان این فایل‌ها را به نود جدیدی که فایل‌های CSR روی آن پردازش می‌شوند منتقل کرد.

اگر روی یک نود، فایل `.srl` مربوط به یک CA وجود نداشته باشد، اسکریپت زیر یک فایل SRL جدید
با یک شمارهٔ سریال آغازین تصادفی تولید می‌کند.

برای اطلاعات بیشتر دربارهٔ فایل‌های `.srl`، مستندات
[`openssl`](https://www.openssl.org/docs/man3.0/man1/openssl-x509.html)
مربوط به فلگ `--CAserial` را ببینید.
{{< /note >}}

این مرحله را برای همهٔ نودهایی که فایل CSR دارند تکرار کنید.

اسکریپت زیر را در پوشهٔ `/etc/kubernetes` بنویسید، به این پوشه بروید و اسکریپت را اجرا کنید.
این اسکریپت برای همهٔ فایل‌های CSR موجود در درخت `/etc/kubernetes` گواهی تولید می‌کند.

```bash
#!/bin/bash

# Set certificate expiration time in days
DAYS=365

# Process all CSR files except those for front-proxy and etcd
find ./ -name "*.csr" | grep -v "pki/etcd" | grep -v "front-proxy" | while read -r FILE;
do
    echo "* Processing ${FILE} ..."
    FILE=${FILE%.*} # Trim the extension
    if [ -f "./pki/ca.srl" ]; then
        SERIAL_FLAG="-CAserial ./pki/ca.srl"
    else
        SERIAL_FLAG="-CAcreateserial"
    fi
    openssl x509 -req -days "${DAYS}" -CA ./pki/ca.crt -CAkey ./pki/ca.key ${SERIAL_FLAG} \
        -in "${FILE}.csr" -out "${FILE}.crt"
    sleep 2
done

# Process all etcd CSRs
find ./pki/etcd -name "*.csr" | while read -r FILE;
do
    echo "* Processing ${FILE} ..."
    FILE=${FILE%.*} # Trim the extension
    if [ -f "./pki/etcd/ca.srl" ]; then
        SERIAL_FLAG=-CAserial ./pki/etcd/ca.srl
    else
        SERIAL_FLAG=-CAcreateserial
    fi
    openssl x509 -req -days "${DAYS}" -CA ./pki/etcd/ca.crt -CAkey ./pki/etcd/ca.key ${SERIAL_FLAG} \
        -in "${FILE}.csr" -out "${FILE}.crt"
done

# Process front-proxy CSRs
echo "* Processing ./pki/front-proxy-client.csr ..."
openssl x509 -req -days "${DAYS}" -CA ./pki/front-proxy-ca.crt -CAkey ./pki/front-proxy-ca.key -CAcreateserial \
    -in ./pki/front-proxy-client.csr -out ./pki/front-proxy-client.crt
```

### جاسازی گواهی‌ها در فایل‌های kubeconfig

این مرحله را برای همهٔ نودهایی که فایل CSR دارند تکرار کنید.

اسکریپت زیر را در پوشهٔ `/etc/kubernetes` بنویسید، به این پوشه بروید و اسکریپت را اجرا کنید.
این اسکریپت فایل‌های `.crt` را که در مرحلهٔ قبل از روی CSRها برای فایل‌های kubeconfig امضا شده‌اند
برمی‌دارد و آن‌ها را در فایل‌های kubeconfig جاسازی می‌کند.

```bash
#!/bin/bash

CLUSTER=kubernetes
find ./ -name "*.conf" | while read -r FILE;
do
    echo "* Processing ${FILE} ..."
    KUBECONFIG="${FILE}" kubectl config set-cluster "${CLUSTER}" --certificate-authority ./pki/ca.crt --embed-certs
    USER=$(KUBECONFIG="${FILE}" kubectl config view -o jsonpath='{.users[0].name}')
    KUBECONFIG="${FILE}" kubectl config set-credentials "${USER}" --client-certificate "${FILE}.crt" --embed-certs
done
```

### پاک‌سازی {#post-csr-cleanup}

این مرحله را روی همهٔ نودهایی که فایل CSR دارند انجام دهید.

اسکریپت زیر را در پوشهٔ `/etc/kubernetes` بنویسید، به این پوشه بروید و اسکریپت را اجرا کنید.

```bash
#!/bin/bash

# Cleanup CSR files
rm -f ./*.csr ./pki/*.csr ./pki/etcd/*.csr # Clean all CSR files

# Cleanup CRT files that were already embedded in kubeconfig files
rm -f ./*.crt
```

در صورت تمایل، فایل‌های `.srl` را به نود بعدی که باید پردازش شود منتقل کنید.

در صورت تمایل، اگر از CA خارجی استفاده می‌کنید، فایل `/etc/kubernetes/pki/ca.key` را حذف کنید؛
همان‌طور که در بخش [حالت CA خارجی](#external-ca-mode) توضیح داده شده است.

### راه‌اندازی اولیهٔ نود با kubeadm

پس از امضای فایل‌های CSR و قرارگرفتن گواهی‌های لازم روی میزبان‌هایی که می‌خواهید به‌عنوان نود
از آن‌ها استفاده کنید، می‌توانید با دستورات `kubeadm init` و `kubeadm join` از این نودها یک کلاستر
کوبرنتیز بسازید. ابزار kubeadm در طول `init` و `join` از گواهی‌ها، کلیدهای رمزنگاری و فایل‌های
kubeconfig موجودی استفاده می‌کند که در درخت `/etc/kubernetes` در سامانهٔ فایل محلی میزبان پیدا می‌کند.
