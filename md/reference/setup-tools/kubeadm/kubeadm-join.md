---
reviewers:
- luxas
- jbeda
title: kubeadm join
content_type: concept
weight: 30
---
<!-- overview -->
این دستور یک نود جدید کوبرنتیز را مقداردهی اولیه می‌کند و آن را به کلاستر موجود می‌پیوندد.

<!-- body -->
{{< include "generated/kubeadm_join/_index.md" >}}

### گردش کار پیوستن {#join-workflow}

دستور `kubeadm join` یک نود کارگر یا یک نود control plane کوبرنتیز را راه‌اندازی اولیه (bootstrap) می‌کند و آن را به کلاستر می‌افزاید. این عملیات برای نودهای کارگر شامل مراحل زیر است:

1. ابتدا kubeadm اطلاعات لازم کلاستر را از API server دریافت می‌کند. این ابزار به‌طور پیش‌فرض برای تأیید اصالت این داده‌ها از توکن راه‌اندازی اولیه و هش کلید مرجع صدور گواهی (CA) استفاده می‌کند. همچنین می‌توان CA ریشه را مستقیماً از طریق یک فایل یا URL کشف کرد.

1. پس از مشخص شدن اطلاعات کلاستر، kubelet می‌تواند فرایند راه‌اندازی اولیه TLS را آغاز کند.

   در این فرایند، از توکن مشترک برای احراز هویت موقت در API server کوبرنتیز استفاده می‌شود تا یک درخواست امضای گواهی (CSR) ارسال شود. control plane به‌طور پیش‌فرض این درخواست را به‌صورت خودکار امضا می‌کند.

1. در پایان، kubeadm مؤلفه kubelet محلی را طوری پیکربندی می‌کند که با هویت قطعی اختصاص‌یافته به نود به API server متصل شود.

برای نودهای control plane مراحل دیگری نیز انجام می‌شود:

1. دریافت گواهی‌های مشترک میان نودهای control plane از کلاستر (در صورتی که کاربر صریحاً آن را درخواست کرده باشد).

1. تولید مانیفست‌های مؤلفه‌های control plane، گواهی‌ها و kubeconfig.

1. افزودن عضو محلی جدید etcd.

### استفاده از مراحل پیوستن با kubeadm {#join-phases}

با استفاده از `kubeadm join phase` می‌توانید فرایند پیوستن یک نود به کلاستر را مرحله‌به‌مرحله انجام دهید.

برای مشاهده فهرست مرتب مراحل و زیرمراحل، دستور `kubeadm join --help` را اجرا کنید. این فهرست در بالای صفحه راهنما قرار دارد و کنار هر مرحله توضیحی درباره آن آمده است. توجه کنید که با اجرای `kubeadm join`، همه مراحل و زیرمراحل دقیقاً به همین ترتیب اجرا می‌شوند.

برخی مراحل فلگ‌های مخصوص به خود دارند. بنابراین اگر می‌خواهید فهرست گزینه‌های موجود را ببینید، `--help` را اضافه کنید؛ برای نمونه:

```shell
kubeadm join phase kubelet-start --help
```

دستور `kubeadm join phase` نیز مانند دستور [kubeadm init phase](/docs/reference/setup-tools/kubeadm/kubeadm-init/#init-phases) امکان می‌دهد با فلگ `--skip-phases` فهرستی از مراحل را نادیده بگیرید.

برای نمونه:

```shell
sudo kubeadm join --skip-phases=preflight --config=config.yaml
```

{{< feature-state for_k8s_version="v1.22" state="beta" >}}

همچنین می‌توانید از فیلد `skipPhases` در `JoinConfiguration` استفاده کنید.

### تشخیص CA مورد اعتماد کلاستر

سازوکار کشف kubeadm چند گزینه دارد که هر یک از نظر امنیتی مزایا و معایب خود را دارند. روش مناسب برای محیط شما به شیوه تأمین نودها و انتظارات امنیتی شما از شبکه و چرخه عمر نودها بستگی دارد.

#### کشف مبتنی بر توکن با پین‌کردن CA

این حالت، حالت پیش‌فرض kubeadm است. در این حالت، kubeadm پیکربندی کلاستر (از جمله CA ریشه) را دریافت می‌کند و آن را با استفاده از توکن اعتبارسنجی می‌کند. همچنین بررسی می‌کند که کلید عمومی CA ریشه با هش ارائه‌شده مطابقت داشته باشد و گواهی API server تحت CA ریشه معتبر باشد.

قالب هش کلید CA به‌صورت `sha256:<hex_encoded_hash>` است. مقدار هش به‌طور پیش‌فرض در پایان اجرای دستور `kubeadm init` یا در خروجی دستور `kubeadm token create --print-join-command` چاپ می‌شود. این مقدار قالبی استاندارد دارد (به [RFC7469](https://tools.ietf.org/html/rfc7469#section-2.4) مراجعه کنید) و ابزارهای شخص ثالث یا سامانه‌های تأمین نیز می‌توانند آن را محاسبه کنند. برای نمونه، با رابط خط فرمان OpenSSL:

```shell
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
```

**نمونه دستورهای `kubeadm join`:**

برای نودهای کارگر:

```shell
kubeadm join --discovery-token abcdef.1234567890abcdef --discovery-token-ca-cert-hash sha256:1234..cdef 1.2.3.4:6443
```

برای نودهای control plane:

```shell
kubeadm join --discovery-token abcdef.1234567890abcdef --discovery-token-ca-cert-hash sha256:1234..cdef --control-plane 1.2.3.4:6443
```

اگر دستور `kubeadm init` با `--upload-certs` اجرا شده باشد، می‌توانید `join` را برای یک نود control plane همراه با `--certificate-key` نیز اجرا کنید تا گواهی‌ها روی این نود کپی شوند.

**مزایا:**

- نودهای در حال راه‌اندازی می‌توانند ریشه اعتماد نود control plane را به‌صورت امن کشف کنند، حتی اگر سایر نودهای کارگر یا شبکه به خطر افتاده باشند.

- اجرای دستی آن آسان است، زیرا تمام اطلاعات لازم در یک دستور `kubeadm join` می‌گنجد.

**معایب:**

- هش CA معمولاً تا پیش از تأمین نود control plane مشخص نیست و همین موضوع ممکن است ساخت ابزارهای تأمین خودکار مبتنی بر kubeadm را دشوارتر کند. با تولید CA از پیش می‌توانید این محدودیت را برطرف کنید.

#### کشف مبتنی بر توکن بدون پین‌کردن CA

این حالت برای امضای (HMAC-SHA256) اطلاعات کشف که ریشه اعتماد control plane را برقرار می‌کند، تنها به توکن متقارن متکی است. برای استفاده از این حالت، نودهای در حال پیوستن باید با `--discovery-token-unsafe-skip-ca-verification` از اعتبارسنجی هش کلید عمومی CA صرف‌نظر کنند. در صورت امکان بهتر است از یکی از حالت‌های دیگر استفاده کنید.

**نمونه دستور `kubeadm join`:**

```shell
kubeadm join --token abcdef.1234567890abcdef --discovery-token-unsafe-skip-ca-verification 1.2.3.4:6443
```

**مزایا:**

- همچنان در برابر بسیاری از حملات سطح شبکه محافظت می‌کند.

- می‌توان توکن را از پیش تولید کرد و آن را با نود control plane و نودهای کارگر به اشتراک گذاشت تا این نودها بدون هماهنگی و به‌صورت موازی راه‌اندازی شوند. به همین دلیل، این حالت در بسیاری از سناریوهای تأمین کاربرد دارد.

**معایب:**

- اگر مهاجم بتواند از طریق یک آسیب‌پذیری، توکن راه‌اندازی اولیه را به سرقت ببرد، می‌تواند با استفاده از آن توکن (همراه با دسترسی در سطح شبکه) خود را به‌جای نود control plane به سایر نودهای در حال راه‌اندازی جا بزند. این مصالحه ممکن است برای محیط شما مناسب باشد یا نباشد.

#### کشف مبتنی بر فایل یا HTTPS

این حالت روشی خارج از باند برای برقراری ریشه اعتماد میان نود control plane و نودهای در حال راه‌اندازی فراهم می‌کند. اگر با kubeadm تأمین خودکار می‌سازید، استفاده از این حالت را بررسی کنید. فایل کشف در قالب یک فایل [kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) معمولی کوبرنتیز است.

اگر فایل کشف حاوی اطلاعات احراز هویت نباشد، از توکن کشف TLS استفاده می‌شود.

**نمونه دستورهای `kubeadm join`:**

- فایل محلی: `kubeadm join --discovery-file path/to/file.conf`

- نشانی HTTPS راه دور: `kubeadm join --discovery-file https://url/file.conf`

**مزایا:**

- نودهای در حال راه‌اندازی می‌توانند ریشه اعتماد نود control plane را به‌صورت امن کشف کنند، حتی اگر شبکه یا سایر نودهای کارگر به خطر افتاده باشند.

**معایب:**

- باید روشی برای انتقال اطلاعات کشف از نود control plane به نودهای در حال راه‌اندازی داشته باشید. اگر فایل کشف حاوی اطلاعات احراز هویت باشد، باید آن را محرمانه نگه دارید و از طریق یک کانال امن منتقل کنید. این کار ممکن است با امکانات ارائه‌دهنده ابری یا ابزار تأمین شما شدنی باشد.

#### استفاده از اعتبارنامه‌های سفارشی kubelet با `kubeadm join`

برای آنکه `kubeadm join` از اعتبارنامه‌های ازپیش‌تعریف‌شده kubelet استفاده کند و راه‌اندازی اولیه TLS کلاینت و تأیید CSR را برای نود جدید نادیده بگیرد، مراحل زیر را انجام دهید:

1. روی یک نود control plane فعال در کلاستر که فایل `/etc/kubernetes/pki/ca.key` را در اختیار دارد، دستور `kubeadm kubeconfig user --org system:nodes --client-name system:node:$NODE > kubelet.conf` را اجرا کنید. مقدار `$NODE` باید برابر با نام نود جدید باشد.
2. فایل `kubelet.conf` حاصل را به‌صورت دستی ویرایش کنید تا نام کلاستر و نقطه پایانی سرور را تنظیم کنید، یا دستور `kubeadm kubeconfig user --config` را اجرا کنید (این دستور `InitConfiguration` را می‌پذیرد).

اگر کلاستر شما فایل `ca.key` را ندارد، باید گواهی‌های جاسازی‌شده در `kubelet.conf` را به‌صورت خارجی امضا کنید. برای اطلاعات بیشتر، به [گواهی‌ها و الزامات PKI](/docs/setup/best-practices/certificates/) و [مدیریت گواهی‌ها با kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#external-ca-mode) مراجعه کنید.

1. فایل `kubelet.conf` حاصل را در مسیر `/etc/kubernetes/kubelet.conf` روی نود جدید کپی کنید.
2. دستور `kubeadm join` را با فلگ `--ignore-preflight-errors=FileAvailable--etc-kubernetes-kubelet.conf` روی نود جدید اجرا کنید.

### امن‌تر کردن نصب {#securing-more}

تنظیمات پیش‌فرض kubeadm ممکن است برای همه مناسب نباشد. این بخش شرح می‌دهد که چگونه می‌توان امنیت نصب kubeadm را به بهای کاهش اندکی از سهولت استفاده افزایش داد.

#### غیرفعال کردن تأیید خودکار گواهی‌های کلاینت نود

به‌طور پیش‌فرض، یک تأییدکننده خودکار CSR فعال است که در صورت استفاده از توکن راه‌اندازی اولیه برای احراز هویت، عملاً هر درخواست گواهی کلاینت kubelet را تأیید می‌کند. اگر نمی‌خواهید کلاستر گواهی‌های کلاینت kubelet را به‌صورت خودکار تأیید کند، می‌توانید با اجرای این دستور این قابلیت را غیرفعال کنید:

```shell
kubectl delete clusterrolebinding kubeadm:node-autoapprove-bootstrap
```

پس از آن، `kubeadm join` تا زمانی که مدیر، CSR در حال انتظار را به‌صورت دستی تأیید کند، مسدود می‌ماند:

1. با استفاده از `kubectl get csr` می‌توانید ببینید که CSR اصلی در وضعیت Pending قرار دارد.

   ```shell
   kubectl get csr
   ```

   خروجی مشابه زیر است:

   ```
   NAME                                                   AGE       REQUESTOR                 CONDITION
   node-csr-c69HXe7aYcqkS1bKmH4faEnHAWxn6i2bHZ2mD04jZyQ   18s       system:bootstrap:878f07   Pending
   ```

2. مدیر می‌تواند با `kubectl certificate approve` درخواست CSR را تأیید کند. این عملیات به کنترل‌کننده امضای گواهی اعلام می‌کند که گواهی‌ای با ویژگی‌های درخواست‌شده در CSR برای درخواست‌کننده صادر کند.

   ```shell
   kubectl certificate approve node-csr-c69HXe7aYcqkS1bKmH4faEnHAWxn6i2bHZ2mD04jZyQ
   ```

   خروجی مشابه زیر است:

   ```
   certificatesigningrequest "node-csr-c69HXe7aYcqkS1bKmH4faEnHAWxn6i2bHZ2mD04jZyQ" approved
   ```

3. با این کار، منبع CSR به وضعیت Active تغییر می‌کند.

   ```shell
   kubectl get csr
   ```

   خروجی مشابه زیر است:

   ```
   NAME                                                   AGE       REQUESTOR                 CONDITION
   node-csr-c69HXe7aYcqkS1bKmH4faEnHAWxn6i2bHZ2mD04jZyQ   1m        system:bootstrap:878f07   Approved,Issued
   ```

به این ترتیب، `kubeadm join` تنها در صورتی موفق می‌شود که `kubectl certificate approve` اجرا شده باشد.

#### غیرفعال کردن دسترسی عمومی به ConfigMap با نام `cluster-info`

برای آنکه فرایند پیوستن تنها با تکیه بر توکن به‌عنوان اطلاعات اعتبارسنجی انجام شود، یک ConfigMap حاوی داده‌های لازم برای اعتبارسنجی هویت نود control plane به‌طور پیش‌فرض به‌صورت عمومی در دسترس قرار می‌گیرد. با اینکه این ConfigMap هیچ داده خصوصی‌ای ندارد، برخی کاربران ممکن است همچنان بخواهند دسترسی به آن را غیرفعال کنند. با این کار، امکان استفاده از فلگ `--discovery-token` در فرایند `kubeadm join` از بین می‌رود. مراحل انجام این کار به شرح زیر است:

* فایل `cluster-info` را از API server دریافت کنید:

```shell
kubectl -n kube-public get cm cluster-info -o jsonpath='{.data.kubeconfig}' | tee cluster-info.yaml
```

خروجی مشابه زیر است:

```yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: <ca-cert>
    server: https://<ip>:<port>
  name: ""
contexts: []
current-context: ""
preferences: {}
users: []
```

* از فایل `cluster-info.yaml` به‌عنوان آرگومان `kubeadm join --discovery-file` استفاده کنید.

* دسترسی عمومی به ConfigMap با نام `cluster-info` را غیرفعال کنید:

```shell
kubectl -n kube-public delete rolebinding kubeadm:bootstrap-signer-clusterinfo
```

این دستورها باید پس از `kubeadm init` و پیش از `kubeadm join` اجرا شوند.

### استفاده از kubeadm join با فایل پیکربندی {#config-file}

{{< caution >}}
فایل پیکربندی همچنان در مرحله بتا قرار دارد و ممکن است در نسخه‌های آینده تغییر کند.
{{< /caution >}}

می‌توان `kubeadm join` را به‌جای فلگ‌های خط فرمان با یک فایل پیکربندی تنظیم کرد و برخی قابلیت‌های پیشرفته‌تر ممکن است تنها به‌صورت گزینه‌های فایل پیکربندی در دسترس باشند. این فایل با فلگ `--config` ارسال می‌شود و باید شامل ساختار `JoinConfiguration` باشد. ترکیب `--config` با سایر فلگ‌ها ممکن است در برخی موارد مجاز نباشد.

پیکربندی پیش‌فرض را می‌توان با دستور [kubeadm config print](/docs/reference/setup-tools/kubeadm/kubeadm-config/#cmd-config-print) چاپ کرد.

اگر پیکربندی شما از آخرین نسخه استفاده نمی‌کند، **توصیه می‌شود** با دستور [kubeadm config migrate](/docs/reference/setup-tools/kubeadm/kubeadm-config/#cmd-config-migrate) آن را مهاجرت دهید.

برای اطلاعات بیشتر درباره فیلدها و نحوه استفاده از پیکربندی، به [مرجع API](/docs/reference/config-api/kubeadm-config.v1beta4/) مراجعه کنید.

## {{% heading "whatsnext" %}}

* برای راه‌اندازی اولیه یک نود control plane کوبرنتیز، به [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) مراجعه کنید.
* برای مدیریت توکن‌های `kubeadm join`، به [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/) مراجعه کنید.
* برای بازگرداندن هر تغییری که `kubeadm init` یا `kubeadm join` روی این میزبان ایجاد کرده است، به [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) مراجعه کنید.
