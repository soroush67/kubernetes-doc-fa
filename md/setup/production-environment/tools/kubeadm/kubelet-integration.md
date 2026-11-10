---
reviewers:
- sig-cluster-lifecycle
title: پیکربندی هر kubelet در کلاستر با استفاده از kubeadm
content_type: concept
weight: 80
---

<!-- overview -->

{{% dockershim-removal %}}

{{< feature-state for_k8s_version="v1.11" state="stable" >}}

چرخهٔ عمر ابزار خط فرمان kubeadm از چرخهٔ عمر
[kubelet](/docs/reference/command-line-tools-reference/kubelet) جداست. kubelet یک دیمن (daemon) است که
روی هر نود در کلاستر کوبرنتیز اجرا می‌شود. کاربر ابزار خط فرمان kubeadm را هنگام راه‌اندازی اولیه یا ارتقای کوبرنتیز
اجرا می‌کند، در حالی که kubelet همواره در پس‌زمینه در حال اجراست.

از آنجا که kubelet یک دیمن است، باید یک سیستم init یا مدیر سرویس آن را نگهداری کند.
هنگامی که kubelet با بسته‌های DEB یا RPM نصب می‌شود، systemd برای مدیریت kubelet پیکربندی می‌شود.
می‌توانید به‌جای آن از مدیر سرویس دیگری استفاده کنید، اما باید آن را به‌صورت دستی پیکربندی کنید.

برخی از جزئیات پیکربندی kubelet باید در همهٔ kubeletهای کلاستر یکسان باشد، در حالی که
برخی جنبه‌های دیگر پیکربندی باید برای هر kubelet جداگانه تنظیم شود تا با ویژگی‌های متفاوت
هر ماشین (مانند سیستم‌عامل، ذخیره‌سازی و شبکه) سازگار باشد. می‌توانید پیکربندی kubeletهای خود را
به‌صورت دستی مدیریت کنید، اما اکنون kubeadm نوع API با نام `KubeletConfiguration` را برای
[مدیریت متمرکز پیکربندی‌های kubelet](#configure-kubelets-using-kubeadm) فراهم می‌کند.

<!-- body -->

## الگوهای پیکربندی kubelet

بخش‌های زیر الگوهایی از پیکربندی kubelet را شرح می‌دهند که با استفاده از kubeadm ساده‌تر می‌شوند
و دیگر لازم نیست پیکربندی kubelet را برای هر Node به‌صورت دستی مدیریت کنید.

### انتشار پیکربندی سطح کلاستر به هر kubelet

می‌توانید مقادیر پیش‌فرضی را در اختیار kubelet بگذارید تا دستورهای `kubeadm init` و `kubeadm join`
از آن‌ها استفاده کنند. از نمونه‌های جالب می‌توان به استفاده از یک محیط اجرای کانتینر دیگر یا تنظیم زیرشبکهٔ پیش‌فرض
مورداستفادهٔ سرویس‌ها اشاره کرد.

اگر می‌خواهید سرویس‌هایتان از زیرشبکهٔ `10.96.0.0/12` به‌عنوان زیرشبکهٔ پیش‌فرض استفاده کنند، می‌توانید
پارامتر `--service-cidr` را به kubeadm بدهید:

```bash
kubeadm init --service-cidr 10.96.0.0/12
```

از این پس IPهای مجازی سرویس‌ها از این زیرشبکه تخصیص داده می‌شوند. همچنین باید نشانی DNS مورداستفادهٔ
kubelet را با فلگ `--cluster-dns` تنظیم کنید. این تنظیم باید برای همهٔ kubeletها روی همهٔ
مدیرها و Nodeهای کلاستر یکسان باشد. kubelet یک آبجکت API نسخه‌دار و ساخت‌یافته فراهم می‌کند
که می‌تواند بیشتر پارامترهای kubelet را پیکربندی کند و این پیکربندی را به همهٔ kubeletهای در حال اجرا
در کلاستر برساند. نام این آبجکت
[`KubeletConfiguration`](/docs/reference/config-api/kubelet-config.v1beta1/) است.
با `KubeletConfiguration` کاربر می‌تواند فلگ‌هایی مانند نشانی‌های IP مربوط به DNS کلاستر را به‌صورت
فهرستی از مقادیر برای یک کلید با نگارش camelCase مشخص کند؛ مثال زیر این موضوع را نشان می‌دهد:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDNS:
- 10.96.0.10
```

برای جزئیات بیشتر دربارهٔ `KubeletConfiguration` به [این بخش](#configure-kubelets-using-kubeadm) نگاهی بیندازید.

### ارائهٔ جزئیات پیکربندی ویژهٔ هر نمونه

برخی میزبان‌ها به دلیل تفاوت در سخت‌افزار، سیستم‌عامل، شبکه یا سایر پارامترهای ویژهٔ میزبان،
به پیکربندی‌های خاصی برای kubelet نیاز دارند. فهرست زیر چند نمونه را ارائه می‌دهد.

- مسیر فایل تفکیک نام DNS که با فلگ پیکربندی `--resolv-conf` در kubelet مشخص می‌شود،
  ممکن است در سیستم‌عامل‌های مختلف یا بسته به اینکه از `systemd-resolved` استفاده می‌کنید یا نه،
  متفاوت باشد. اگر این مسیر نادرست باشد، تفکیک نام DNS روی Nodeای که kubelet آن
  به‌اشتباه پیکربندی شده است با شکست مواجه می‌شود.

- مقدار `.metadata.name` در آبجکت API مربوط به Node به‌طور پیش‌فرض برابر با نام میزبان ماشین قرار می‌گیرد،
  مگر اینکه از یک ارائه‌دهندهٔ ابری استفاده کنید. اگر لازم است نام Node با نام میزبان ماشین متفاوت باشد،
  می‌توانید با فلگ `--hostname-override` رفتار پیش‌فرض را تغییر دهید.

- در حال حاضر kubelet نمی‌تواند درایور cgroup مورداستفادهٔ محیط اجرای کانتینر را به‌طور خودکار تشخیص دهد،
  اما برای تضمین سلامت kubelet، مقدار `--cgroup-driver` باید با درایور cgroup مورداستفادهٔ
  محیط اجرای کانتینر مطابقت داشته باشد.

- برای مشخص کردن محیط اجرای کانتینر باید نقطهٔ پایانی (endpoint) آن را با فلگ
`--container-runtime-endpoint=<path>` تنظیم کنید.

روش توصیه‌شده برای اعمال چنین پیکربندی‌های ویژهٔ هر نمونه، استفاده از
[وصله‌های `KubeletConfiguration`](/docs/setup/production-environment/tools/kubeadm/control-plane-flags#patches) است.

## پیکربندی kubeletها با استفاده از kubeadm

اگر یک آبجکت API سفارشی از نوع
[`KubeletConfiguration`](/docs/reference/config-api/kubelet-config.v1beta1/)
از طریق یک فایل پیکربندی، مانند `kubeadm ... --config some-config-file.yaml`، ارسال شود،
می‌توان kubeletای را که kubeadm راه‌اندازی می‌کند پیکربندی کرد.

با اجرای `kubeadm config print init-defaults --component-configs KubeletConfiguration` می‌توانید
همهٔ مقادیر پیش‌فرض این ساختار را ببینید.

همچنین می‌توان وصله‌های ویژهٔ هر نمونه را روی `KubeletConfiguration` پایه اعمال کرد.
برای جزئیات بیشتر به [سفارشی‌سازی kubelet](/docs/setup/production-environment/tools/kubeadm/control-plane-flags#customizing-the-kubelet)
مراجعه کنید.

### روند کار هنگام استفاده از `kubeadm init`

هنگامی که `kubeadm init` را فراخوانی می‌کنید، پیکربندی kubelet در مسیر
`/var/lib/kubelet/config.yaml` روی دیسک نوشته می‌شود و همچنین در یک ConfigMap با نام
`kubelet-config` در فضای نام (namespace) `kube-system` کلاستر بارگذاری می‌شود.
افزون بر این، ابزار kubeadm سوکت CRI روی نود را تشخیص می‌دهد و جزئیات آن را
(از جمله مسیر سوکت) در یک پیکربندی محلی، یعنی `/var/lib/kubelet/instance-config.yaml`، می‌نویسد.
یک فایل پیکربندی kubelet نیز در `/etc/kubernetes/kubelet.conf` نوشته می‌شود
که پیکربندی پایهٔ سطح کلاستر را برای همهٔ kubeletهای کلاستر در بر دارد. این فایل پیکربندی
به گواهی‌های کلاینتی اشاره می‌کند که kubelet با آن‌ها می‌تواند با سرور API ارتباط برقرار کند. به این ترتیب
نیاز به
[انتشار پیکربندی سطح کلاستر به هر kubelet](#propagating-cluster-level-configuration-to-each-kubelet)
برطرف می‌شود.

برای پاسخ به الگوی دوم، یعنی
[ارائهٔ جزئیات پیکربندی ویژهٔ هر نمونه](#providing-instance-specific-configuration-details)،
kubeadm یک فایل محیطی در `/var/lib/kubelet/kubeadm-flags.env` می‌نویسد که فهرستی از
فلگ‌هایی را که باید هنگام شروع kubelet به آن داده شوند در بر دارد. فلگ‌ها در این فایل به این شکل آمده‌اند:

```bash
KUBELET_KUBEADM_ARGS="--flag1=value1 --flag2=value2 ..."
```

این فایل افزون بر فلگ‌هایی که هنگام شروع kubelet استفاده می‌شوند، پارامترهای پویا
مانند درایور cgroup را نیز در بر دارد.

پس از نوشتن این دو فایل روی دیسک، اگر از systemd استفاده می‌کنید، kubeadm تلاش می‌کند
دو دستور زیر را اجرا کند:

```bash
systemctl daemon-reload && systemctl restart kubelet
```

اگر بارگذاری مجدد و راه‌اندازی دوباره موفقیت‌آمیز باشند، روند عادی `kubeadm init` ادامه می‌یابد.

### روند کار هنگام استفاده از `kubeadm join`

هنگامی که `kubeadm join` را اجرا می‌کنید، kubeadm از اعتبارنامهٔ Bootstrap Token برای انجام
یک راه‌اندازی TLS (TLS bootstrap) استفاده می‌کند. این فرایند اعتبارنامهٔ لازم برای دانلود
ConfigMap با نام `kubelet-config` را دریافت می‌کند و آن را در `/var/lib/kubelet/config.yaml` می‌نویسد.
افزون بر این، ابزار kubeadm سوکت CRI روی نود را تشخیص می‌دهد و جزئیات آن را
(از جمله مسیر سوکت) در یک پیکربندی محلی، یعنی `/var/lib/kubelet/instance-config.yaml`، می‌نویسد.
فایل محیطی پویا دقیقاً به همان روش `kubeadm init` تولید می‌شود.

سپس `kubeadm` دو دستور زیر را برای بارگذاری پیکربندی جدید در kubelet اجرا می‌کند:

```bash
systemctl daemon-reload && systemctl restart kubelet
```

پس از اینکه kubelet پیکربندی جدید را بارگذاری کرد، kubeadm فایل KubeConfig با نام
`/etc/kubernetes/bootstrap-kubelet.conf` را می‌نویسد که یک گواهی CA و یک Bootstrap Token
در بر دارد. kubelet از این‌ها برای انجام راه‌اندازی TLS و دریافت یک اعتبارنامهٔ یکتا استفاده می‌کند؛
این اعتبارنامه در `/etc/kubernetes/kubelet.conf` ذخیره می‌شود.

هنگامی که فایل `/etc/kubernetes/kubelet.conf` نوشته شد، kubelet انجام راه‌اندازی TLS را به پایان رسانده است.
kubeadm پس از تکمیل راه‌اندازی TLS، فایل `/etc/kubernetes/bootstrap-kubelet.conf` را حذف می‌کند.

##  فایل drop-in مربوط به kubelet برای systemd

بستهٔ `kubeadm` همراه با پیکربندی‌ای عرضه می‌شود که تعیین می‌کند systemd چگونه kubelet را اجرا کند.
توجه داشته باشید که دستور خط فرمان kubeadm هرگز به این فایل drop-in دست نمی‌زند.

این فایل پیکربندی که
[بستهٔ](https://github.com/kubernetes/release/blob/cd53840/cmd/krel/templates/latest/kubeadm/10-kubeadm.conf) `kubeadm` نصب می‌کند، در
`/usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf` نوشته می‌شود و systemd از آن استفاده می‌کند.
این فایل، فایل پایهٔ
[`kubelet.service`](https://github.com/kubernetes/release/blob/cd53840/cmd/krel/templates/latest/kubelet/kubelet.service)
را تکمیل می‌کند.

اگر می‌خواهید این تنظیمات را بیشتر تغییر دهید، می‌توانید دایرکتوری `/etc/systemd/system/kubelet.service.d/`
(و نه `/usr/lib/systemd/system/kubelet.service.d/`) را بسازید و سفارشی‌سازی‌های خود را در فایلی در آنجا قرار دهید.
برای مثال، می‌توانید یک فایل محلی جدید با نام `/etc/systemd/system/kubelet.service.d/local-overrides.conf`
اضافه کنید تا تنظیمات unit را که `kubeadm` پیکربندی کرده است بازنویسی کنید.

محتوایی که احتمالاً در `/usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf` خواهید یافت، به این شکل است:

{{< note >}}
محتوای زیر تنها یک نمونه است. اگر نمی‌خواهید از مدیر بسته استفاده کنید،
راهنمای ارائه‌شده در بخش ([بدون مدیر بسته](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#k8s-install-2))
را دنبال کنید.
{{< /note >}}

```none
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
# This is a file that "kubeadm init" and "kubeadm join" generate at runtime, populating
# the KUBELET_KUBEADM_ARGS variable dynamically
EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
# This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably,
# the user should use the .NodeRegistration.KubeletExtraArgs object in the configuration files instead.
# KUBELET_EXTRA_ARGS should be sourced from this file.
EnvironmentFile=-/etc/default/kubelet
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS
```

این فایل مکان‌های پیش‌فرض همهٔ فایل‌هایی را که kubeadm برای kubelet مدیریت می‌کند مشخص می‌کند.

- فایل KubeConfig مورداستفاده برای راه‌اندازی TLS، `/etc/kubernetes/bootstrap-kubelet.conf` است،
  اما تنها در صورتی استفاده می‌شود که `/etc/kubernetes/kubelet.conf` وجود نداشته باشد.
- فایل KubeConfig حاوی هویت یکتای kubelet، `/etc/kubernetes/kubelet.conf` است.
- فایل حاوی ComponentConfig مربوط به kubelet، `/var/lib/kubelet/config.yaml` است.
- فایل محیطی پویا که `KUBELET_KUBEADM_ARGS` را در بر دارد، از `/var/lib/kubelet/kubeadm-flags.env` بارگذاری می‌شود.
- فایلی که می‌تواند فلگ‌های بازنویسی‌شده توسط کاربر را از طریق `KUBELET_EXTRA_ARGS` در بر داشته باشد، از
  `/etc/default/kubelet` (برای DEBها) یا `/etc/sysconfig/kubelet` (برای RPMها) بارگذاری می‌شود. متغیر `KUBELET_EXTRA_ARGS`
  در انتهای زنجیرهٔ فلگ‌ها قرار دارد و در صورت تعارض تنظیمات، بالاترین اولویت را دارد.

## فایل‌های اجرایی کوبرنتیز و محتوای بسته‌ها

بسته‌های DEB و RPM که همراه با نسخه‌های کوبرنتیز عرضه می‌شوند عبارت‌اند از:

| نام بسته | توضیحات |
|--------------|-------------|
| `kubeadm`    | ابزار خط فرمان `/usr/bin/kubeadm` و [فایل drop-in مربوط به kubelet](#the-kubelet-drop-in-file-for-systemd) را برای kubelet نصب می‌کند. |
| `kubelet`    | فایل اجرایی `/usr/bin/kubelet` را نصب می‌کند. |
| `kubectl`    | فایل اجرایی `/usr/bin/kubectl` را نصب می‌کند. |
| `cri-tools` | فایل اجرایی `/usr/bin/crictl` را از [مخزن git پروژهٔ cri-tools](https://github.com/kubernetes-sigs/cri-tools) نصب می‌کند. |
| `kubernetes-cni` | فایل‌های اجرایی `/opt/cni/bin` را از [مخزن git پروژهٔ plugins](https://github.com/containernetworking/plugins) نصب می‌کند. |
