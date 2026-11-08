---
title: kubeadm init
content_type: concept
weight: 20
---

<!-- overview -->

این دستور یک نود control plane کوبرنتیز را مقداردهی اولیه می‌کند.

<!-- body -->

{{< include "generated/kubeadm_init/_index.md" >}}

### گردش کار init {#init-workflow}

دستور `kubeadm init` با اجرای مراحل زیر، یک نود control plane کوبرنتیز را راه‌اندازی می‌کند:

1. پیش از اعمال هر تغییری، مجموعه‌ای از بررسی‌های پیش از اجرا (pre-flight) را برای اعتبارسنجی وضعیت سیستم انجام می‌دهد. برخی از این بررسی‌ها فقط هشدار می‌دهند، اما برخی دیگر خطا به شمار می‌آیند و اجرای kubeadm را متوقف می‌کنند تا زمانی که مشکل برطرف شود یا کاربر پرچم `--ignore-preflight-errors=<list-of-errors>` را مشخص کند.

1. یک مرجع صدور گواهی (CA) خودامضا ایجاد می‌کند تا برای هر مؤلفهٔ کلاستر هویت تعریف کند. کاربر می‌تواند گواهی و/یا کلید CA خود را در پوشهٔ گواهی‌ها قرار دهد؛ این پوشه با `--cert-dir` پیکربندی می‌شود و مقدار پیش‌فرض آن `/etc/kubernetes/pki` است. گواهی‌های سرور API به‌ازای هر آرگومان `--apiserver-cert-extra-sans` مدخل‌های SAN بیشتری خواهند داشت و این مقادیر در صورت نیاز به حروف کوچک تبدیل می‌شوند.

1. فایل‌های kubeconfig را در `/etc/kubernetes/` می‌نویسد تا kubelet، controller-manager و زمان‌بند هر یک با هویت خود به سرور API متصل شوند. همچنین فایل‌های kubeconfig دیگری برای kubeadm به‌عنوان موجودیت مدیریتی (`admin.conf`) و برای کاربر مدیر ارشدی که می‌تواند RBAC را دور بزند (`super-admin.conf`) نوشته می‌شوند.

1. مانیفست‌های Pod ایستا را برای سرور API، controller-manager و زمان‌بند تولید می‌کند. اگر etcd خارجی ارائه نشده باشد، یک مانیفست Pod ایستای دیگر نیز برای etcd تولید می‌شود.

   مانیفست‌های Pod ایستا در `/etc/kubernetes/manifests` نوشته می‌شوند. kubelet این پوشه را زیر نظر دارد تا Podها را هنگام راه‌اندازی ایجاد کند.

   پس از آنکه Podهای control plane راه‌اندازی شدند و به اجرا درآمدند، روند `kubeadm init` می‌تواند ادامه یابد.

1. برچسب‌ها و taintها را روی نود control plane اعمال می‌کند تا هیچ بار کاری دیگری روی آن اجرا نشود.

1. توکنی تولید می‌کند که نودهای دیگر می‌توانند در آینده با آن خود را در control plane ثبت کنند. کاربر می‌تواند به‌صورت اختیاری، طبق توضیحات مستندات [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/)، توکنی را با `--token` ارائه کند.

1. تمام پیکربندی‌های لازم را برای پیوستن نودها از طریق سازوکارهای [توکن‌های راه‌انداز (Bootstrap Tokens)](/docs/reference/access-authn-authz/bootstrap-tokens/) و [راه‌اندازی TLS (TLS Bootstrap)](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) انجام می‌دهد:

   - یک ConfigMap می‌نویسد تا تمام اطلاعات لازم برای پیوستن در دسترس قرار گیرد و قوانین دسترسی RBAC مرتبط را تنظیم می‌کند.

   - به توکن‌های راه‌انداز اجازهٔ دسترسی به API امضای CSR را می‌دهد.

   - تأیید خودکار درخواست‌های جدید CSR را پیکربندی می‌کند.

   برای اطلاعات بیشتر، به [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) مراجعه کنید.

1. یک سرور DNS (یعنی CoreDNS) و مؤلفه‌های افزونهٔ kube-proxy را از طریق سرور API نصب می‌کند. توجه کنید که با وجود استقرار سرور DNS، این سرور تا پیش از نصب CNI زمان‌بندی نخواهد شد.

### استفاده از فازهای init در kubeadm {#init-phases}

با دستور `kubeadm init phase` می‌توانید یک نود control plane را به‌صورت فازبه‌فاز ایجاد کنید.

برای مشاهدهٔ فهرست مرتب فازها و زیرفازها می‌توانید `kubeadm init --help` را اجرا کنید. این فهرست در بالای صفحهٔ راهنما قرار دارد و توضیح هر فاز در کنار آن آمده است. توجه کنید که با اجرای `kubeadm init`، تمام فازها و زیرفازها دقیقاً به همین ترتیب اجرا می‌شوند.

برخی از فازها پرچم‌های مخصوص به خود را دارند؛ بنابراین اگر می‌خواهید فهرست گزینه‌های موجود را ببینید، `--help` را اضافه کنید. برای مثال:

```shell
sudo kubeadm init phase control-plane controller-manager --help
```

همچنین می‌توانید با `--help` فهرست زیرفازهای یک فاز والد مشخص را ببینید:

```shell
sudo kubeadm init phase control-plane --help
```

دستور `kubeadm init` پرچمی به نام `--skip-phases` نیز دارد که با آن می‌توان از اجرای برخی فازها صرف‌نظر کرد. این پرچم فهرستی از نام فازها را می‌پذیرد و این نام‌ها را می‌توان از فهرست مرتب بالا برداشت.

یک مثال:

```shell
sudo kubeadm init phase control-plane all --config=configfile.yaml
sudo kubeadm init phase etcd local --config=configfile.yaml
# you can now modify the control plane and etcd manifest files
sudo kubeadm init --skip-phases=control-plane,etcd --config=configfile.yaml
```

این مثال فایل‌های مانیفست control plane و etcd را بر اساس پیکربندی موجود در `configfile.yaml` در `/etc/kubernetes/manifests` می‌نویسد. به این ترتیب می‌توانید فایل‌ها را ویرایش کنید و سپس با `--skip-phases` از این فازها بگذرید. با اجرای آخرین دستور، یک نود control plane با فایل‌های مانیفست سفارشی ایجاد خواهید کرد.

{{< feature-state for_k8s_version="v1.22" state="beta" >}}

به‌عنوان راه جایگزین، می‌توانید از فیلد `skipPhases` در `InitConfiguration` استفاده کنید.

### استفاده از kubeadm init با فایل پیکربندی {#config-file}

{{< caution >}}
فایل پیکربندی هنوز در مرحلهٔ بتا است و ممکن است در نسخه‌های آینده تغییر کند.
{{< /caution >}}

می‌توان `kubeadm init` را به‌جای پرچم‌های خط فرمان با یک فایل پیکربندی تنظیم کرد و برخی قابلیت‌های پیشرفته‌تر شاید فقط به‌صورت گزینه‌های فایل پیکربندی در دسترس باشند. این فایل با پرچم `--config` ارسال می‌شود و باید یک ساختار `ClusterConfiguration` و به‌صورت اختیاری ساختارهای دیگری را در بر داشته باشد که با `---\n` از هم جدا شده‌اند. ترکیب `--config` با پرچم‌های دیگر ممکن است در برخی موارد مجاز نباشد.

پیکربندی پیش‌فرض را می‌توان با دستور [kubeadm config print](/docs/reference/setup-tools/kubeadm/kubeadm-config/) چاپ کرد.

اگر پیکربندی شما از آخرین نسخه استفاده نمی‌کند، **توصیه می‌شود** آن را با دستور [kubeadm config migrate](/docs/reference/setup-tools/kubeadm/kubeadm-config/) مهاجرت دهید.

برای اطلاعات بیشتر دربارهٔ فیلدها و نحوهٔ استفاده از پیکربندی، می‌توانید به [صفحهٔ مرجع API](/docs/reference/config-api/kubeadm-config.v1beta4/) مراجعه کنید.

### استفاده از kubeadm init با feature gateها {#feature-gates}

ابزار kubeadm از مجموعه‌ای از feature gateها پشتیبانی می‌کند که مختص خود آن هستند و فقط هنگام ایجاد کلاستر با `kubeadm init` می‌توان آن‌ها را اعمال کرد. این قابلیت‌ها می‌توانند رفتار کلاستر را کنترل کنند. پس از آنکه قابلیتی به مرحلهٔ GA برسد، feature gate آن حذف می‌شود.

برای ارسال یک feature gate می‌توانید از پرچم `--feature-gates` در `kubeadm init` استفاده کنید یا هنگام ارسال یک [فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/#kubeadm-k8s-io-v1beta4-ClusterConfiguration) با `--config`، مواردی را به فیلد `featureGates` اضافه کنید.

ارسال مستقیم [feature gateهای مؤلفه‌های اصلی کوبرنتیز](/docs/reference/command-line-tools-reference/feature-gates) به kubeadm پشتیبانی نمی‌شود. در عوض، می‌توان آن‌ها را از طریق [سفارشی‌سازی مؤلفه‌ها با API مربوط به kubeadm](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/) ارسال کرد.

فهرست feature gateها:

{{< table caption="kubeadm feature gates" >}}
قابلیت | پیش‌فرض | آلفا | بتا | GA | منسوخ‌شده
:-------|:--------|:------|:-----|:---|:----------
`RootlessControlPlane` | `false` | 1.22 | - | - | 1.31
{{< /table >}}

توضیحات feature gateها:

`RootlessControlPlane`
: با تنظیم این پرچم، کانتینرهای Pod ایستای مؤلفه‌های control plane که kubeadm مستقر می‌کند، یعنی `kube-apiserver`، `kube-controller-manager`، `kube-scheduler` و `etcd`، طوری پیکربندی می‌شوند که با کاربران غیر root اجرا شوند. اگر این پرچم تنظیم نشود، این مؤلفه‌ها با کاربر root اجرا می‌شوند. می‌توانید مقدار این feature gate را پیش از ارتقا به نسخهٔ جدیدتر کوبرنتیز تغییر دهید.

فهرست feature gateهای حذف‌شده:

{{< table caption="kubeadm removed feature gates" >}}
قابلیت | آلفا | بتا | GA | حذف‌شده
:-------|:------|:-----|:---|:-------
`ControlPlaneKubeletLocalMode` | 1.31 | 1.33 | 1.35 | 1.36
`EtcdLearnerMode` | 1.27 | 1.29 | 1.32 | 1.33
`IPv6DualStack` | 1.16 | 1.21 | 1.23 | 1.24
`NodeLocalCRISocket` | 1.32 | 1.34 | 1.36 | 1.37
`PublicKeysECDSA` | 1.19 | - | - | 1.37
`UnversionedKubeletConfigMap` | 1.22 | 1.23 | 1.25 | 1.26
`UpgradeAddonsBeforeControlPlane` | 1.28 | - | - | 1.31
`WaitForAllControlPlaneComponents` | 1.30 | 1.33 | 1.34 | 1.35
{{< /table >}}

توضیحات feature gateها:

`ControlPlaneKubeletLocalMode`
: با فعال بودن این feature gate، هنگام پیوستن یک نود control plane جدید، kubeadm کوبلت را طوری پیکربندی می‌کند که به kube-apiserver محلی متصل شود. این کار تضمین می‌کند که سیاست اختلاف نسخه‌ها (version skew) هنگام ارتقای تدریجی نقض نشود.

`EtcdLearnerMode`
: هنگام پیوستن یک نود control plane جدید، عضو جدیدی از etcd به‌صورت learner ایجاد می‌شود و فقط پس از همگام شدن کامل داده‌های etcd به عضو دارای حق رأی ارتقا می‌یابد.

`IPv6DualStack`
: این پرچم در دورهٔ توسعهٔ این قابلیت به پیکربندی مؤلفه‌ها برای پشتهٔ دوگانه کمک می‌کند. برای جزئیات بیشتر دربارهٔ پشتیبانی کوبرنتیز از پشتهٔ دوگانه، به [پشتیبانی از پشتهٔ دوگانه با kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/) مراجعه کنید.

`NodeLocalCRISocket`
: با فعال بودن این feature gate، ابزار kubeadm سوکت CRI هر نود را به‌جای خواندن از حاشیه‌نویسی (annotation) `kubeadm.alpha.kubernetes.io/cri-socket` روی آبجکت Node و نوشتن در آن، از فایل `/var/lib/kubelet/instance-config.yaml` می‌خواند و در همین فایل می‌نویسد. این فایل جدید به‌صورت یک وصلهٔ پیکربندی نمونه اعمال می‌شود، آن هم پیش از اعمال هر وصلهٔ دیگری که کاربر هنگام استفاده از پرچم `--patches` مدیریت می‌کند. این فایل فقط یک فیلد `containerRuntimeEndpoint` از [قالب فایل KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/) را در بر دارد. اگر این feature gate هنگام ارتقا فعال باشد، اما فایل `/var/lib/kubelet/instance-config.yaml` هنوز وجود نداشته باشد، kubeadm تلاش می‌کند مقدار سوکت CRI را از فایل `/var/lib/kubelet/kubeadm-flags.env` بخواند.

`PublicKeysECDSA`
: با این قابلیت می‌توان کلاستری ایجاد کرد که به‌جای الگوریتم پیش‌فرض RSA از گواهی‌های ECDSA استفاده می‌کند. تمدید گواهی‌های ECDSA موجود نیز با `kubeadm certs renew` پشتیبانی می‌شود، اما نمی‌توانید در حین کار یا هنگام ارتقا بین الگوریتم‌های RSA و ECDSA جابه‌جا شوید. نسخه‌های کوبرنتیز پیش از v1.31 اشکالی داشتند که باعث می‌شد کلیدهای فایل‌های kubeconfig تولیدشده، حتی با فعال بودن feature gate مربوط به `PublicKeysECDSA`، روی RSA تنظیم شوند. این feature gate به نفع قابلیت `encryptionAlgorithm` موجود در kubeadm v1beta4 منسوخ شده است.

`UnversionedKubeletConfigMap`
: این پرچم نام {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} را تعیین می‌کند که kubeadm داده‌های پیکربندی kubelet را در آن ذخیره می‌کند. اگر این پرچم مشخص نشود یا روی `true` تنظیم شود، نام ConfigMap برابر `kubelet-config` خواهد بود. اگر این پرچم را روی `false` تنظیم کنید، نام ConfigMap شامل نسخهٔ اصلی و فرعی کوبرنتیز می‌شود (برای مثال: `kubelet-config-{{< skew currentVersion >}}`). ابزار kubeadm اطمینان می‌دهد که قوانین RBAC برای خواندن و نوشتن آن ConfigMap با مقدار تعیین‌شده متناسب باشند. هنگامی که kubeadm این ConfigMap را می‌نویسد (در حین `kubeadm init` یا `kubeadm upgrade apply`)، مقدار `UnversionedKubeletConfigMap` را رعایت می‌کند. هنگام خواندن آن ConfigMap (در حین `kubeadm join`، `kubeadm reset`، `kubeadm upgrade` و مانند آن‌ها)، kubeadm ابتدا تلاش می‌کند از نام بدون نسخهٔ ConfigMap استفاده کند. اگر این تلاش موفق نباشد، kubeadm به نام قدیمی (نسخه‌دار) آن ConfigMap بازمی‌گردد.

`UpgradeAddonsBeforeControlPlane`
: این feature gate حذف شده است. این قابلیت در v1.28 به‌عنوان قابلیتی منسوخ معرفی شد و سپس در v1.31 حذف شد. برای مطالعهٔ مستندات نسخه‌های قدیمی‌تر، به نسخهٔ متناظر وب‌سایت مراجعه کنید.

`WaitForAllControlPlaneComponents`
: با فعال بودن این feature gate، ابزار kubeadm منتظر می‌ماند تا تمام مؤلفه‌های control plane (kube-apiserver، kube-controller-manager و kube-scheduler) روی نود control plane، وضعیت 200 را در endpointهای `/livez` یا `/healthz` خود گزارش کنند. این بررسی‌ها روی `https://ADDRESS:PORT/ENDPOINT` انجام می‌شوند.

  - مقدار `PORT` از `--secure-port` هر مؤلفه گرفته می‌شود.
  - مقدار `ADDRESS` برای kube-apiserver برابر `--advertise-address` و برای kube-controller-manager و kube-scheduler برابر `--bind-address` است.
  - مقدار `ENDPOINT` برای kube-controller-manager تا زمانی که از `/livez` نیز پشتیبانی کند، فقط `/healthz` است.

  اگر `ADDRESS` یا `PORT` سفارشی را در پیکربندی kubeadm مشخص کنید، همان مقادیر رعایت می‌شوند. بدون فعال بودن این feature gate، ابزار kubeadm فقط منتظر آماده شدن kube-apiserver روی نود control plane می‌ماند. فرایند انتظار بلافاصله پس از آنکه kubeadm، kubelet را روی میزبان راه‌اندازی کرد، آغاز می‌شود. اگر می‌خواهید وضعیت آماده را از همهٔ مؤلفه‌های control plane در طول اجرای دستور `kubeadm init` یا `kubeadm join` مشاهده کنید، توصیه می‌شود این feature gate را فعال کنید.

### افزودن پارامترهای kube-proxy {#kube-proxy}

برای اطلاعات دربارهٔ پارامترهای kube-proxy در پیکربندی kubeadm، به این منبع مراجعه کنید:

- [مرجع kube-proxy](/docs/reference/config-api/kube-proxy-config.v1alpha1/)

برای اطلاعات دربارهٔ فعال‌سازی حالت IPVS با kubeadm، به این منبع مراجعه کنید:

- [حالت IPVS](https://github.com/kubernetes/kubernetes/blob/master/pkg/proxy/ipvs/README.md)

### ارسال پرچم‌های سفارشی به مؤلفه‌های control plane {#control-plane-flags}

برای اطلاعات دربارهٔ ارسال پرچم به مؤلفه‌های control plane، به این منبع مراجعه کنید:

- [پرچم‌های control plane](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)

### اجرای kubeadm بدون اتصال به اینترنت {#without-internet-connection}

برای اجرای kubeadm بدون اتصال به اینترنت، باید ایمیج‌های لازم برای control plane را از قبل دریافت کنید.

با زیردستور `kubeadm config images` می‌توانید این ایمیج‌ها را فهرست و دریافت کنید:

```shell
kubeadm config images list
kubeadm config images pull
```

می‌توانید `--config` را همراه با یک [فایل پیکربندی kubeadm](#config-file) به دستورهای بالا بدهید تا فیلدهای `kubernetesVersion` و `imageRepository` را کنترل کنید.

تمام ایمیج‌های پیش‌فرض `registry.k8s.io` که kubeadm به آن‌ها نیاز دارد، از چند معماری پشتیبانی می‌کنند.

### استفاده از ایمیج‌های سفارشی {#custom-images}

ابزار kubeadm به‌طور پیش‌فرض ایمیج‌ها را از `registry.k8s.io` دریافت می‌کند. اگر نسخهٔ درخواستی کوبرنتیز یک برچسب CI باشد (مانند `ci/latest`)، از `gcr.io/k8s-staging-ci-images` استفاده می‌شود.

می‌توانید این رفتار را با [استفاده از kubeadm همراه با فایل پیکربندی](#config-file) تغییر دهید. سفارشی‌سازی‌های مجاز عبارت‌اند از:

* تعیین `kubernetesVersion` که بر نسخهٔ ایمیج‌ها اثر می‌گذارد.
* تعیین یک `imageRepository` جایگزین برای استفاده به‌جای `registry.k8s.io`.
* تعیین `imageRepository` و `imageTag` مشخص برای etcd یا CoreDNS.

مسیر ایمیج‌ها در `registry.k8s.io` پیش‌فرض و مخزن سفارشی تعیین‌شده با `imageRepository` ممکن است به دلایل سازگاری با نسخه‌های قبلی متفاوت باشد. برای مثال، ممکن است ایمیجی در مسیر `registry.k8s.io/subpath/image` زیرمسیر داشته باشد، اما هنگام استفاده از مخزن سفارشی، مسیر پیش‌فرض آن `my.customrepository.io/image` باشد.

برای آنکه ایمیج‌ها را در مسیرهایی از مخزن سفارشی خود قرار دهید که kubeadm بتواند از آن‌ها استفاده کند، باید این کارها را انجام دهید:

* ایمیج‌ها را با `kubeadm config images {list|pull}` از مسیرهای پیش‌فرض در `registry.k8s.io` دریافت کنید.
* ایمیج‌ها را به مسیرهای خروجی `kubeadm config images list --config=config.yaml` ارسال کنید؛ در این دستور، `config.yaml` شامل `imageRepository` سفارشی و/یا `imageTag` برای etcd و CoreDNS است.
* همان `config.yaml` را به `kubeadm init` بدهید.

#### ایمیج‌های سفارشی sandbox (pause) {#custom-pause-image}

برای تعیین ایمیج سفارشی برای این موارد، باید {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} خود را طوری پیکربندی کنید که از آن ایمیج استفاده کند. برای آگاهی از نحوهٔ تغییر این تنظیم، به مستندات محیط اجرای کانتینر خود مراجعه کنید. برای برخی از محیط‌های اجرای کانتینر، راهنمایی‌هایی نیز در مبحث [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/) وجود دارد.

### بارگذاری گواهی‌های control plane در کلاستر

با افزودن پرچم `--upload-certs` به `kubeadm init` می‌توانید گواهی‌های control plane را به‌طور موقت در یک Secret در کلاستر بارگذاری کنید. توجه کنید که این Secret پس از ۲ ساعت به‌طور خودکار منقضی می‌شود. گواهی‌ها با یک کلید ۳۲ بایتی رمزگذاری می‌شوند که می‌توان آن را با `--certificate-key` مشخص کرد. هنگام پیوستن نودهای control plane دیگر نیز می‌توان با ارسال `--control-plane` و `--certificate-key` به `kubeadm join`، از همین کلید برای دریافت گواهی‌ها استفاده کرد.

برای بارگذاری دوبارهٔ گواهی‌ها پس از انقضا می‌توان از دستور فاز زیر استفاده کرد:

```shell
kubeadm init phase upload-certs --upload-certs --config=SOME_YAML_FILE
```

{{< note >}}
هنگام ارسال [فایل پیکربندی](/docs/reference/config-api/kubeadm-config.v1beta4/) با `--config` می‌توان یک `certificateKey` ازپیش‌تعریف‌شده را در `InitConfiguration` ارائه کرد.
{{< /note >}}

اگر کلید گواهی ازپیش‌تعریف‌شده‌ای به `kubeadm init` و `kubeadm init phase upload-certs` داده نشود، کلید جدیدی به‌طور خودکار تولید می‌شود.

برای تولید کلید جدید در صورت نیاز می‌توان از دستور زیر استفاده کرد:

```shell
kubeadm certs certificate-key
```

### مدیریت گواهی با kubeadm

برای اطلاعات تفصیلی دربارهٔ مدیریت گواهی با kubeadm، به [مدیریت گواهی با kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/) مراجعه کنید. این سند اطلاعاتی دربارهٔ استفاده از CA خارجی، گواهی‌های سفارشی و تمدید گواهی ارائه می‌دهد.

### مدیریت فایل drop-in مربوط به kubeadm برای kubelet {#kubelet-drop-in}

بستهٔ `kubeadm` همراه با یک فایل پیکربندی برای اجرای `kubelet` با `systemd` ارائه می‌شود. توجه کنید که رابط خط فرمان kubeadm هرگز این فایل drop-in را تغییر نمی‌دهد. این فایل drop-in بخشی از بستهٔ DEB/RPM مربوط به kubeadm است.

برای اطلاعات بیشتر، به [مدیریت فایل drop-in مربوط به kubeadm برای systemd](/docs/setup/production-environment/tools/kubeadm/kubelet-integration/#the-kubelet-drop-in-file-for-systemd) مراجعه کنید.

### استفاده از kubeadm با محیط‌های اجرای CRI

ابزار kubeadm به‌طور پیش‌فرض تلاش می‌کند محیط اجرای کانتینر شما را تشخیص دهد. برای جزئیات بیشتر دربارهٔ این تشخیص، به [راهنمای نصب CRI در kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime) مراجعه کنید.

### تنظیم نام نود

ابزار kubeadm به‌طور پیش‌فرض نام نود را بر اساس نشانی میزبان ماشین تعیین می‌کند. با فلگ `--node-name` می‌توانید این تنظیم را تغییر دهید. این فلگ مقدار مناسب [`--hostname-override`](/docs/reference/command-line-tools-reference/kubelet/#options) را به kubelet می‌فرستد.

توجه داشته باشید که بازنویسی نام میزبان ممکن است [با عملکرد ارائه‌دهندگان ابری تداخل ایجاد کند](https://github.com/kubernetes/website/pull/8873).

### خودکارسازی kubeadm

به‌جای آنکه مانند [آموزش پایه kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)، توکن به‌دست‌آمده از `kubeadm init` را به تک‌تک نودها کپی کنید، می‌توانید توزیع توکن را به‌صورت موازی انجام دهید تا خودکارسازی آسان‌تر شود. برای پیاده‌سازی این خودکارسازی، باید نشانی IP نود control plane پس از راه‌اندازی را بدانید یا از یک نام DNS یا نشانی یک متعادل‌کننده بار استفاده کنید.

1. یک توکن تولید کنید. این توکن باید به شکل `<6 character string>.<16 character string>` باشد. به بیان دقیق‌تر، باید با عبارت منظم `[a-z0-9]{6}\.[a-z0-9]{16}` مطابقت داشته باشد.

   ابزار kubeadm می‌تواند این توکن را برای شما تولید کند:

   ```shell
   kubeadm token generate
   ```

1. نود control plane و نودهای کارگر را هم‌زمان با این توکن راه‌اندازی کنید. این نودها پس از بالا آمدن باید یکدیگر را پیدا کنند و کلاستر را تشکیل دهند. می‌توانید آرگومان `--token` یکسانی را هم در `kubeadm init` و هم در `kubeadm join` به کار ببرید.

1. هنگام پیوستن نودهای control plane بیشتر نیز می‌توانید همین کار را برای `--certificate-key` انجام دهید. این کلید را می‌توان با دستور زیر تولید کرد:

   ```shell
   kubeadm certs certificate-key
   ```

پس از آماده شدن کلاستر، می‌توانید با استفاده از فایل `/etc/kubernetes/admin.conf` روی یک نود control plane و با اعتبارنامه‌های مدیر با کلاستر ارتباط برقرار کنید یا به بخش [تولید فایل‌های kubeconfig برای کاربران بیشتر](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#kubeconfig-additional-users) مراجعه کنید.

توجه کنید که این شیوه راه‌اندازی، تضمین‌های امنیتی ضعیف‌تری دارد، زیرا امکان اعتبارسنجی هش CA ریشه را با `--discovery-token-ca-cert-hash` فراهم نمی‌کند؛ چون این هش هنگام آماده‌سازی نودها تولید نمی‌شود. برای جزئیات بیشتر، صفحه [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) را ببینید.

## {{% heading "whatsnext" %}}

* برای آشنایی بیشتر با مراحل `kubeadm init`، صفحه [kubeadm init phase](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/) را ببینید.
* برای راه‌اندازی یک نود کارگر کوبرنتیز و پیوستن آن به کلاستر، صفحه [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) را ببینید.
* برای ارتقای کلاستر کوبرنتیز به نسخه جدیدتر، صفحه [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) را ببینید.
* برای بازگرداندن تغییراتی که `kubeadm init` یا `kubeadm join` روی این میزبان ایجاد کرده‌اند، صفحه [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) را ببینید.
