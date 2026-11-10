---
reviewers:
- sig-cluster-lifecycle
title: ایجاد کلاسترهای با دسترس‌پذیری بالا با kubeadm
content_type: task
weight: 60
---

<!-- overview -->

این صفحه دو رویکرد متفاوت برای راه‌اندازی یک کلاستر کوبرنتیز با دسترس‌پذیری بالا (highly available) به کمک kubeadm را توضیح می‌دهد:

- با نودهای control plane انباشته (stacked). این رویکرد به زیرساخت کمتری نیاز دارد. در آن، اعضای etcd و نودهای control plane در کنار هم قرار می‌گیرند.
- با یک کلاستر etcd خارجی. این رویکرد به زیرساخت بیشتری نیاز دارد. در آن، نودهای control plane و اعضای etcd از یکدیگر جدا هستند.

پیش از ادامه، باید با دقت بررسی کنید که کدام رویکرد بهتر با نیازهای برنامه‌ها و محیط شما سازگار است. صفحهٔ [گزینه‌های توپولوژی با دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/ha-topology/) مزایا و معایب هر یک را شرح می‌دهد.

اگر در راه‌اندازی کلاستر HA با مشکلی روبه‌رو شدید، لطفاً آن را در [سامانهٔ پیگیری مشکلات](https://github.com/kubernetes/kubeadm/issues/new) kubeadm گزارش دهید.

همچنین [مستندات ارتقا](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) را ببینید.

{{< caution >}}
این صفحه به اجرای کلاستر روی یک ارائه‌دهندهٔ ابری نمی‌پردازد. در محیط ابری، هیچ‌یک از دو رویکرد مستندشده در اینجا با آبجکت‌های Service از نوع LoadBalancer یا با PersistentVolumeهای پویا کار نمی‌کند.
{{< /caution >}}

## {{% heading "prerequisites" %}}

پیش‌نیازها به توپولوژی‌ای بستگی دارد که برای control plane کلاستر خود انتخاب کرده‌اید:

{{< tabs name="prerequisite_tabs" >}}
{{% tab name="etcd انباشته" %}}
<!--
    note to reviewers: these prerequisites should match the start of the
    external etc tab
-->

به موارد زیر نیاز دارید:

- سه ماشین یا بیشتر که [حداقل نیازمندی‌های kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin) را برای نودهای control plane برآورده کنند. داشتن تعداد فرد نود control plane می‌تواند در صورت از کار افتادن یک ماشین یا یک ناحیه (zone)، به انتخاب رهبر کمک کند.
  - از جمله یک {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} که از قبل راه‌اندازی شده و کار می‌کند
- سه ماشین یا بیشتر که [حداقل نیازمندی‌های kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin) را برای نودهای کارگر (worker) برآورده کنند
  - از جمله یک محیط اجرای کانتینر که از قبل راه‌اندازی شده و کار می‌کند
- اتصال شبکهٔ کامل میان همهٔ ماشین‌های کلاستر (شبکهٔ عمومی یا خصوصی)
- دسترسی ابرکاربر روی همهٔ ماشین‌ها با استفاده از `sudo`
  - می‌توانید از ابزار دیگری استفاده کنید؛ این راهنما در مثال‌ها از `sudo` استفاده می‌کند.
- دسترسی SSH از یک دستگاه به همهٔ نودهای سیستم
- ابزارهای `kubeadm` و `kubelet` که از قبل روی همهٔ ماشین‌ها نصب شده باشند.

_برای آشنایی با زمینهٔ موضوع، [توپولوژی etcd انباشته](/docs/setup/production-environment/tools/kubeadm/ha-topology/#stacked-etcd-topology) را ببینید._

{{% /tab %}}
{{% tab name="etcd خارجی" %}}
<!--
    note to reviewers: these prerequisites should match the start of the
    stacked etc tab
-->
به موارد زیر نیاز دارید:

- سه ماشین یا بیشتر که [حداقل نیازمندی‌های kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin) را برای نودهای control plane برآورده کنند. داشتن تعداد فرد نود control plane می‌تواند در صورت از کار افتادن یک ماشین یا یک ناحیه، به انتخاب رهبر کمک کند.
  - از جمله یک {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} که از قبل راه‌اندازی شده و کار می‌کند
- سه ماشین یا بیشتر که [حداقل نیازمندی‌های kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#before-you-begin) را برای نودهای کارگر برآورده کنند
  - از جمله یک محیط اجرای کانتینر که از قبل راه‌اندازی شده و کار می‌کند
- اتصال شبکهٔ کامل میان همهٔ ماشین‌های کلاستر (شبکهٔ عمومی یا خصوصی)
- دسترسی ابرکاربر روی همهٔ ماشین‌ها با استفاده از `sudo`
  - می‌توانید از ابزار دیگری استفاده کنید؛ این راهنما در مثال‌ها از `sudo` استفاده می‌کند.
- دسترسی SSH از یک دستگاه به همهٔ نودهای سیستم
- ابزارهای `kubeadm` و `kubelet` که از قبل روی همهٔ ماشین‌ها نصب شده باشند.

<!-- end of shared prerequisites -->

علاوه بر این، به موارد زیر نیز نیاز دارید:

- سه ماشین اضافی یا بیشتر که اعضای کلاستر etcd خواهند شد. داشتن تعداد فرد عضو در کلاستر etcd برای دستیابی به حد نصاب (quorum) بهینه در رأی‌گیری الزامی است.
  - روی این ماشین‌ها نیز باید `kubeadm` و `kubelet` نصب شده باشند.
  - این ماشین‌ها همچنین به یک محیط اجرای کانتینر نیاز دارند که از قبل راه‌اندازی شده و کار کند.

_برای آشنایی با زمینهٔ موضوع، [توپولوژی etcd خارجی](/docs/setup/production-environment/tools/kubeadm/ha-topology/#external-etcd-topology) را ببینید._
{{% /tab %}}
{{< /tabs >}}

### ایمیج‌های کانتینر

هر میزبان باید بتواند ایمیج‌ها را از رجیستری ایمیج کانتینر کوبرنتیز، یعنی `registry.k8s.io`، بخواند و دریافت کند. اگر بخواهید کلاستری با دسترس‌پذیری بالا مستقر کنید که میزبان‌های آن امکان دریافت ایمیج را ندارند، این کار شدنی است؛ اما باید به روش دیگری اطمینان حاصل کنید که ایمیج‌های کانتینر درست از قبل روی میزبان‌های مربوط در دسترس هستند.

### رابط خط فرمان {#kubectl}

برای مدیریت کوبرنتیز پس از راه‌اندازی کلاستر، باید [kubectl را نصب کنید](/docs/tasks/tools/#kubectl) روی رایانهٔ شخصی خود. نصب ابزار `kubectl` روی هر نود control plane نیز سودمند است، زیرا می‌تواند در عیب‌یابی کمک کند.

<!-- steps -->

## گام‌های نخست برای هر دو روش

### ایجاد متعادل‌کنندهٔ بار برای kube-apiserver

{{< note >}}
پیکربندی‌های فراوانی برای متعادل‌کننده‌های بار (load balancer) وجود دارد. مثال زیر تنها یکی از گزینه‌هاست و ممکن است نیازمندی‌های کلاستر شما پیکربندی متفاوتی را بطلبد.
{{< /note >}}

1. یک متعادل‌کنندهٔ بار برای kube-apiserver با نامی ایجاد کنید که در DNS قابل تفکیک (resolve) باشد.

   - در محیط ابری باید نودهای control plane را پشت یک متعادل‌کنندهٔ بار با هدایت TCP قرار دهید. این متعادل‌کننده ترافیک را میان همهٔ نودهای control plane سالم در فهرست مقصدهای خود توزیع می‌کند. بررسی سلامت برای apiserver، یک بررسی TCP روی پورتی است که kube-apiserver به آن گوش می‌دهد (مقدار پیش‌فرض `:6443`).

   - استفادهٔ مستقیم از نشانی IP در محیط ابری توصیه نمی‌شود.

   - متعادل‌کنندهٔ بار باید بتواند روی پورت apiserver با همهٔ نودهای control plane ارتباط برقرار کند. همچنین باید ترافیک ورودی را روی پورت شنود خود بپذیرد.

   - مطمئن شوید که نشانی متعادل‌کنندهٔ بار همواره با نشانی `ControlPlaneEndpoint` در kubeadm مطابقت دارد.

   - برای جزئیات بیشتر، راهنمای [Options for Software Load Balancing](https://git.k8s.io/kubeadm/docs/ha-considerations.md#options-for-software-load-balancing) را بخوانید.

1. نخستین نود control plane را به متعادل‌کنندهٔ بار اضافه کنید و اتصال را آزمایش کنید:

   ```shell
   nc -zv -w 2 <LOAD_BALANCER_IP> <PORT>
   ```

   دریافت خطای «connection refused» قابل انتظار است، زیرا سرور API هنوز در حال اجرا نیست. اما رخ دادن timeout به این معناست که متعادل‌کنندهٔ بار نمی‌تواند با نود control plane ارتباط برقرار کند. در صورت رخ دادن timeout، متعادل‌کنندهٔ بار را دوباره طوری پیکربندی کنید که بتواند با نود control plane ارتباط برقرار کند.

1. باقی نودهای control plane را به گروه مقصد متعادل‌کنندهٔ بار اضافه کنید.

## نودهای control plane و etcd انباشته

### گام‌ها برای نخستین نود control plane

1. control plane را مقداردهی اولیه کنید:

   ```sh
   sudo kubeadm init --control-plane-endpoint "LOAD_BALANCER_DNS:LOAD_BALANCER_PORT" --upload-certs
   ```

   - با فلگ `--kubernetes-version` می‌توانید نسخهٔ کوبرنتیز مورد استفاده را تعیین کنید. توصیه می‌شود نسخه‌های kubeadm، kubelet، kubectl و کوبرنتیز با هم مطابقت داشته باشند.
   - فلگ `--control-plane-endpoint` باید روی نشانی یا نام DNS و پورت متعادل‌کنندهٔ بار تنظیم شود.

   - از فلگ `--upload-certs` برای بارگذاری گواهی‌هایی در کلاستر استفاده می‌شود که باید میان همهٔ نمونه‌های control plane به اشتراک گذاشته شوند. اگر ترجیح می‌دهید گواهی‌ها را به‌صورت دستی یا با ابزارهای خودکارسازی میان نودهای control plane کپی کنید، این فلگ را حذف کنید و به بخش [توزیع دستی گواهی‌ها](#manual-certs) در ادامه مراجعه کنید.

   {{< note >}}
   فلگ‌های `--config` و `--certificate-key` در `kubeadm init` را نمی‌توان با هم به کار برد؛ بنابراین اگر می‌خواهید از [پیکربندی kubeadm](/docs/reference/config-api/kubeadm-config.v1beta4/) استفاده کنید، باید فیلد `certificateKey` را در جاهای مناسب پیکربندی (زیر `InitConfiguration` و `JoinConfiguration: controlPlane`) اضافه کنید.
   {{< /note >}}

   {{< note >}}
   برخی افزونه‌های شبکهٔ CNI به پیکربندی اضافی، مانند تعیین CIDR آی‌پی پادها، نیاز دارند و برخی دیگر نیازی به آن ندارند. [مستندات شبکهٔ CNI](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network) را ببینید. برای افزودن CIDR پادها، فلگ `--pod-network-cidr` را ارسال کنید، یا اگر از فایل پیکربندی kubeadm استفاده می‌کنید، فیلد `podSubnet` را زیر آبجکت `networking` در `ClusterConfiguration` تنظیم کنید.
   {{< /note >}}

   خروجی مشابه زیر است:

   ```sh
   ...
   You can now join any number of control-plane node by running the following command on each as a root:
       kubeadm join 192.168.0.200:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866 --control-plane --certificate-key f8902e114ef118304e561c3ecd4d0b543adc226b7a07f675f56564185ffe0c07

   Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
   As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use kubeadm init phase upload-certs to reload certs afterward.

   Then you can join any number of worker nodes by running the following on each as root:
       kubeadm join 192.168.0.200:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866
   ```

   - این خروجی را در یک فایل متنی کپی کنید. بعداً برای پیوستن نودهای control plane و نودهای کارگر به کلاستر به آن نیاز خواهید داشت.
   - هنگامی که `--upload-certs` همراه با `kubeadm init` به کار می‌رود، گواهی‌های control plane اصلی رمزگذاری شده و در Secret به نام `kubeadm-certs` بارگذاری می‌شوند.
   - برای بارگذاری دوبارهٔ گواهی‌ها و تولید یک کلید رمزگشایی جدید، دستور زیر را روی یکی از نودهای control plane که از قبل به کلاستر پیوسته است اجرا کنید:

     ```sh
     sudo kubeadm init phase upload-certs --upload-certs
     ```

   - همچنین می‌توانید هنگام `init` یک `--certificate-key` سفارشی تعیین کنید که بعداً `join` بتواند از آن استفاده کند. برای تولید چنین کلیدی می‌توانید از دستور زیر استفاده کنید:

     ```sh
     kubeadm certs certificate-key
     ```

   کلید گواهی رشته‌ای با کدگذاری hex است که یک کلید AES با اندازهٔ ۳۲ بایت را نشان می‌دهد.

   {{< note >}}
   اعتبار Secret به نام `kubeadm-certs` و کلید رمزگشایی پس از دو ساعت منقضی می‌شود.
   {{< /note >}}

   {{< caution >}}
   همان‌طور که در خروجی دستور آمده است، کلید گواهی به داده‌های حساس کلاستر دسترسی می‌دهد؛ آن را محرمانه نگه دارید!
   {{< /caution >}}

1. افزونهٔ CNI دلخواه خود را اعمال کنید:
   برای نصب ارائه‌دهندهٔ CNI، [این دستورالعمل‌ها را دنبال کنید](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#pod-network). مطمئن شوید که پیکربندی با CIDR پادهای تعیین‌شده در فایل پیکربندی kubeadm (در صورت وجود) مطابقت دارد.

   {{< note >}}
   باید افزونهٔ شبکه‌ای متناسب با کاربرد خود انتخاب کنید و پیش از رفتن به گام بعد آن را مستقر کنید. در غیر این صورت، نمی‌توانید کلاستر خود را به‌درستی راه‌اندازی کنید.
   {{< /note >}}

1. دستور زیر را وارد کنید و راه‌اندازی پادهای اجزای control plane را مشاهده کنید:

   ```sh
   kubectl get pod -n kube-system -w
   ```

### گام‌ها برای باقی نودهای control plane

برای هر نود control plane اضافی باید کارهای زیر را انجام دهید:

1. دستور join را که پیش‌تر خروجی `kubeadm init` روی نخستین نود در اختیارتان گذاشته بود اجرا کنید. این دستور باید چیزی شبیه به این باشد:

   ```sh
   sudo kubeadm join 192.168.0.200:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866 --control-plane --certificate-key f8902e114ef118304e561c3ecd4d0b543adc226b7a07f675f56564185ffe0c07
   ```

   - فلگ `--control-plane` به `kubeadm join` می‌گوید که یک control plane جدید ایجاد کند.
   - فلگ `--certificate-key ...` باعث می‌شود گواهی‌های control plane از Secret به نام `kubeadm-certs` در کلاستر دریافت شوند و با کلید داده‌شده رمزگشایی شوند.


{{< note >}}
از آنجا که نودهای کلاستر معمولاً به‌ترتیب مقداردهی اولیه می‌شوند، احتمالاً همهٔ پادهای CoreDNS روی نخستین نود control plane اجرا می‌شوند. برای دستیابی به دسترس‌پذیری بالاتر، پس از پیوستن دست‌کم یک نود جدید، پادهای CoreDNS را با دستور `kubectl -n kube-system rollout restart deployment coredns` دوباره متعادل کنید.
{{< /note >}}

## نودهای etcd خارجی

راه‌اندازی کلاستر با نودهای etcd خارجی شبیه به روند مورد استفاده برای etcd انباشته است، با این تفاوت که باید ابتدا etcd را راه‌اندازی کنید و اطلاعات etcd را در فایل پیکربندی kubeadm وارد کنید.

### راه‌اندازی کلاستر etcd

1. برای راه‌اندازی کلاستر etcd، این [دستورالعمل‌ها](/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/) را دنبال کنید.

1. دسترسی SSH را همان‌گونه که [اینجا](#manual-certs) توضیح داده شده است راه‌اندازی کنید.

1. فایل‌های زیر را از هر یک از نودهای etcd در کلاستر به نخستین نود control plane کپی کنید:

   ```sh
   export CONTROL_PLANE="ubuntu@10.0.0.7"
   scp /etc/kubernetes/pki/etcd/ca.crt "${CONTROL_PLANE}":
   scp /etc/kubernetes/pki/apiserver-etcd-client.crt "${CONTROL_PLANE}":
   scp /etc/kubernetes/pki/apiserver-etcd-client.key "${CONTROL_PLANE}":
   ```

   - مقدار `CONTROL_PLANE` را با `user@host` نخستین نود control plane جایگزین کنید.

### راه‌اندازی نخستین نود control plane

1. فایلی به نام `kubeadm-config.yaml` با محتوای زیر ایجاد کنید:

   ```yaml
   ---
   apiVersion: kubeadm.k8s.io/v1beta4
   kind: ClusterConfiguration
   kubernetesVersion: stable
   controlPlaneEndpoint: "LOAD_BALANCER_DNS:LOAD_BALANCER_PORT" # change this (see below)
   etcd:
     external:
       endpoints:
         - https://ETCD_0_IP:2379 # change ETCD_0_IP appropriately
         - https://ETCD_1_IP:2379 # change ETCD_1_IP appropriately
         - https://ETCD_2_IP:2379 # change ETCD_2_IP appropriately
       caFile: /etc/kubernetes/pki/etcd/ca.crt
       certFile: /etc/kubernetes/pki/apiserver-etcd-client.crt
       keyFile: /etc/kubernetes/pki/apiserver-etcd-client.key
   ```

   {{< note >}}
   تفاوت etcd انباشته و etcd خارجی در اینجا این است که راه‌اندازی etcd خارجی به یک فایل پیکربندی نیاز دارد که نقاط پایانی (endpoint) etcd را زیر آبجکت `external` برای `etcd` در خود داشته باشد. در توپولوژی etcd انباشته، این کار به‌صورت خودکار مدیریت می‌شود.
   {{< /note >}}

   - متغیرهای زیر را در الگوی پیکربندی با مقادیر مناسب برای کلاستر خود جایگزین کنید:

     - `LOAD_BALANCER_DNS`
     - `LOAD_BALANCER_PORT`
     - `ETCD_0_IP`
     - `ETCD_1_IP`
     - `ETCD_2_IP`

گام‌های زیر مشابه راه‌اندازی etcd انباشته هستند:

1. دستور `sudo kubeadm init --config kubeadm-config.yaml --upload-certs` را روی این نود اجرا کنید.

1. دستورهای join بازگردانده‌شده در خروجی را برای استفادهٔ بعدی در یک فایل متنی بنویسید.

1. افزونهٔ CNI دلخواه خود را اعمال کنید.

   {{< note >}}
   باید افزونهٔ شبکه‌ای متناسب با کاربرد خود انتخاب کنید و پیش از رفتن به گام بعد آن را مستقر کنید. در غیر این صورت، نمی‌توانید کلاستر خود را به‌درستی راه‌اندازی کنید.
   {{< /note >}}

### گام‌ها برای باقی نودهای control plane

گام‌ها همانند راه‌اندازی etcd انباشته است:

- مطمئن شوید که نخستین نود control plane به‌طور کامل مقداردهی اولیه شده است.
- هر نود control plane را با دستور joinی که در فایل متنی ذخیره کرده‌اید به کلاستر بپیوندانید. توصیه می‌شود نودهای control plane را یکی‌یکی به کلاستر بپیوندانید.
- فراموش نکنید که کلید رمزگشایی مربوط به `--certificate-key` به‌طور پیش‌فرض پس از دو ساعت منقضی می‌شود.

## کارهای رایج پس از راه‌اندازی اولیهٔ control plane

### نصب نودهای کارگر

نودهای کارگر را می‌توان با دستوری که پیش‌تر از خروجی `kubeadm init` ذخیره کرده‌اید به کلاستر پیوست داد:

```sh
sudo kubeadm join 192.168.0.200:6443 --token 9vr73a.a8uxyaju799qwdjv --discovery-token-ca-cert-hash sha256:7c2e69131a36ae2a042a339b33381c6d0d43887e2de83720eff5359e26aec866
```

## توزیع دستی گواهی‌ها {#manual-certs}

اگر تصمیم بگیرید `kubeadm init` را بدون فلگ `--upload-certs` اجرا کنید، باید گواهی‌ها را به‌صورت دستی از نود اصلی control plane به نودهای control plane که به کلاستر می‌پیوندند کپی کنید.

برای این کار روش‌های زیادی وجود دارد. مثال زیر از `ssh` و `scp` استفاده می‌کند:

اگر می‌خواهید همه نودها را از یک ماشین واحد کنترل کنید، به SSH نیاز دارید.

1. ‏ssh-agent را روی دستگاه اصلی خود که به همه نودهای دیگر سیستم دسترسی دارد فعال کنید:

   ```shell
   eval $(ssh-agent)
   ```

1. هویت SSH خود را به نشست اضافه کنید:

   ```shell
   ssh-add ~/.ssh/path_to_private_key
   ```

1. میان نودها با SSH ارتباط برقرار کنید تا مطمئن شوید اتصال به‌درستی کار می‌کند.

   - هنگام اتصال SSH به هر نود، فلگ `-A` را اضافه کنید. این فلگ به نودی که از طریق SSH وارد آن شده‌اید امکان می‌دهد به عامل SSH روی رایانه شما دسترسی داشته باشد. اگر به امنیت نشست کاربری خود روی آن نود کاملاً اطمینان ندارید، روش‌های جایگزین را بررسی کنید.

     ```shell
     ssh -A 10.0.0.7
     ```

   - هنگام استفاده از sudo روی هر نود، حتماً متغیرهای محیطی را حفظ کنید تا ارسال (forwarding) در SSH کار کند:

     ```shell
     sudo -E -s
     ```

1. پس از پیکربندی SSH روی همه نودها، باید اسکریپت زیر را پس از اجرای `kubeadm init` روی نخستین نود control plane اجرا کنید. این اسکریپت گواهی‌ها را از نخستین نود control plane به سایر نودهای control plane کپی می‌کند:

   در مثال زیر، به‌جای `CONTROL_PLANE_IPS` نشانی‌های IP سایر نودهای control plane را قرار دهید.

   ```sh
   USER=ubuntu # customizable
   CONTROL_PLANE_IPS="10.0.0.7 10.0.0.8"
   for host in ${CONTROL_PLANE_IPS}; do
       scp /etc/kubernetes/pki/ca.crt "${USER}"@$host:
       scp /etc/kubernetes/pki/ca.key "${USER}"@$host:
       scp /etc/kubernetes/pki/sa.key "${USER}"@$host:
       scp /etc/kubernetes/pki/sa.pub "${USER}"@$host:
       scp /etc/kubernetes/pki/front-proxy-ca.crt "${USER}"@$host:
       scp /etc/kubernetes/pki/front-proxy-ca.key "${USER}"@$host:
       scp /etc/kubernetes/pki/etcd/ca.crt "${USER}"@$host:etcd-ca.crt
       # Skip the next line if you are using external etcd
       scp /etc/kubernetes/pki/etcd/ca.key "${USER}"@$host:etcd-ca.key
   done
   ```

   {{< caution >}}
   فقط گواهی‌های فهرست بالا را کپی کنید. ابزار kubeadm تولید بقیه گواهی‌ها را با SANهای لازم برای نمونه‌های control plane که به کلاستر می‌پیوندند بر عهده می‌گیرد. اگر به اشتباه همه گواهی‌ها را کپی کنید، ممکن است ایجاد نودهای اضافی به دلیل نبودِ SANهای لازم با شکست روبه‌رو شود.
   {{< /caution >}}

1. سپس روی هر نود control plane که به کلاستر می‌پیوندد، باید پیش از اجرای `kubeadm join` اسکریپت زیر را اجرا کنید. این اسکریپت گواهی‌هایی را که پیش‌تر کپی شده‌اند از پوشه خانگی به `/etc/kubernetes/pki` منتقل می‌کند:

   ```sh
   USER=ubuntu # customizable
   mkdir -p /etc/kubernetes/pki/etcd
   mv /home/${USER}/ca.crt /etc/kubernetes/pki/
   mv /home/${USER}/ca.key /etc/kubernetes/pki/
   mv /home/${USER}/sa.pub /etc/kubernetes/pki/
   mv /home/${USER}/sa.key /etc/kubernetes/pki/
   mv /home/${USER}/front-proxy-ca.crt /etc/kubernetes/pki/
   mv /home/${USER}/front-proxy-ca.key /etc/kubernetes/pki/
   mv /home/${USER}/etcd-ca.crt /etc/kubernetes/pki/etcd/ca.crt
   # Skip the next line if you are using external etcd
   mv /home/${USER}/etcd-ca.key /etc/kubernetes/pki/etcd/ca.key
   ```
