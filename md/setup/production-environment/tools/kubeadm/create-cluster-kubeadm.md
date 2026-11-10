---
reviewers:
- sig-cluster-lifecycle
title: ایجاد یک کلاستر با kubeadm
content_type: task
weight: 30
---

<!-- overview -->

<img src="/images/kubeadm-stacked-color.png" align="right" width="150px"></img>
با استفاده از `kubeadm` می‌توانید یک کلاستر حداقلیِ کارآمد کوبرنتیز بسازید که با بهترین شیوه‌ها (best practices) سازگار است.
در واقع، با `kubeadm` می‌توانید کلاستری راه‌اندازی کنید که
[آزمون‌های انطباق کوبرنتیز](/blog/2017/10/software-conformance-certification/) را با موفقیت پشت سر بگذارد.
ابزار `kubeadm` از دیگر کارکردهای چرخه عمر کلاستر، مانند
[توکن‌های راه‌اندازی اولیه (bootstrap tokens)](/docs/reference/access-authn-authz/bootstrap-tokens/) و ارتقای کلاستر نیز پشتیبانی می‌کند.

ابزار `kubeadm` در این موارد گزینه مناسبی است:

- به روشی ساده برای امتحان کردن کوبرنتیز، احتمالاً برای نخستین بار، نیاز دارید.
- کاربر فعلی کوبرنتیز هستید و می‌خواهید راه‌اندازی کلاستر و آزمودن برنامه خود را خودکار کنید.
- به یک جزء سازنده در ابزارهای دیگر اکوسیستم و/یا ابزارهای نصب با دامنه‌ای گسترده‌تر نیاز دارید.

می‌توانید `kubeadm` را روی ماشین‌های گوناگونی نصب و استفاده کنید: لپ‌تاپ خود، مجموعه‌ای
از سرورهای ابری، یک Raspberry Pi و موارد دیگر. چه در ابر مستقر کنید و چه روی
زیرساخت داخلی (on-premises)، می‌توانید `kubeadm` را با سامانه‌های تأمین زیرساخت (provisioning)
مانند Ansible یا Terraform یکپارچه کنید.

## {{% heading "prerequisites" %}}

برای دنبال کردن این راهنما به موارد زیر نیاز دارید:

- یک یا چند ماشین با سیستم‌عامل لینوکسیِ سازگار با deb/rpm؛ برای مثال Ubuntu یا CentOS.
- دست‌کم ۲ گیبی‌بایت RAM برای هر ماشین؛ با مقدار کمتر، فضای چندانی برای برنامه‌هایتان باقی نمی‌ماند.
- دست‌کم ۲ CPU روی ماشینی که به‌عنوان نود control plane از آن استفاده می‌کنید.
- اتصال شبکه کامل میان همه ماشین‌های کلاستر. می‌توانید از شبکه عمومی
  یا خصوصی استفاده کنید.

همچنین باید از نسخه‌ای از `kubeadm` استفاده کنید که بتواند نسخه‌ای از کوبرنتیز را که
می‌خواهید در کلاستر جدید خود به کار ببرید، مستقر کند.

[سیاست نسخه‌ها و پشتیبانی از اختلاف نسخه در کوبرنتیز](/docs/setup/release/version-skew-policy/#supported-versions)
همان‌گونه که برای کل کوبرنتیز اعمال می‌شود، برای `kubeadm` نیز صادق است.
برای آگاهی از اینکه کدام نسخه‌های کوبرنتیز و `kubeadm` پشتیبانی می‌شوند، این سیاست را بررسی کنید.
این صفحه برای کوبرنتیز {{< param "version" >}} نوشته شده است.

وضعیت کلی ویژگی‌های ابزار `kubeadm` «در دسترس عمومی» (General Availability یا GA) است. برخی از زیرویژگی‌ها
هنوز در حال توسعه فعال هستند. ممکن است پیاده‌سازی فرایند ایجاد کلاستر با تکامل ابزار
اندکی تغییر کند، اما پیاده‌سازی کلی باید کاملاً پایدار باشد.

{{< note >}}
همه فرمان‌های زیرمجموعه `kubeadm alpha` بنا به تعریف، در سطح آلفا پشتیبانی می‌شوند.
{{< /note >}}

<!-- steps -->

## اهداف

* نصب یک کلاستر کوبرنتیز با یک control plane
* نصب یک شبکه Pod روی کلاستر تا Podهای شما بتوانند
  با یکدیگر ارتباط برقرار کنند

## دستورالعمل‌ها

### آماده‌سازی میزبان‌ها

#### نصب اجزا

یک {{< glossary_tooltip term_id="container-runtime" text="محیط اجرای کانتینر" >}}
و kubeadm را روی همه میزبان‌ها نصب کنید. برای دستورالعمل‌های دقیق و دیگر پیش‌نیازها،
[نصب kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) را ببینید.

{{< note >}}
اگر kubeadm را از قبل نصب کرده‌اید، برای آشنایی با نحوه ارتقای آن، دو گام نخست سند
[ارتقای نودهای لینوکسی](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes)
را ببینید.

هنگام ارتقا، kubelet هر چند ثانیه یک بار راه‌اندازی مجدد می‌شود، زیرا در یک حلقه خرابی (crashloop)
منتظر می‌ماند تا kubeadm به آن بگوید چه کاری انجام دهد. این حلقه خرابی قابل انتظار و عادی است.
پس از مقداردهی اولیه control plane، kubelet به‌طور عادی اجرا می‌شود.
{{< /note >}}

#### پیکربندی شبکه

ابزار kubeadm نیز مانند دیگر اجزای کوبرنتیز تلاش می‌کند یک IP قابل استفاده را روی
رابط‌های شبکه‌ای پیدا کند که با درگاه پیش‌فرض (default gateway) میزبان مرتبط هستند.
سپس هر جزء از این IP برای اعلام نشانی (advertising) و/یا گوش دادن (listening) استفاده می‌کند.

برای اینکه بفهمید این IP روی یک میزبان لینوکسی چیست، می‌توانید از فرمان زیر استفاده کنید:

```shell
ip route show # Look for a line starting with "default via"
```

{{< note >}}
اگر دو یا چند درگاه پیش‌فرض روی میزبان وجود داشته باشد، هر جزء کوبرنتیز تلاش می‌کند
از نخستین درگاهی استفاده کند که به آن برمی‌خورد و یک نشانی IP مناسب از نوع global unicast دارد.
هنگام این انتخاب، ترتیب دقیق درگاه‌ها ممکن است در سیستم‌عامل‌ها و نسخه‌های کرنل
مختلف متفاوت باشد.
{{< /note >}}

اجزای کوبرنتیز رابط شبکه سفارشی را به‌عنوان گزینه نمی‌پذیرند؛
بنابراین باید نشانی IP سفارشی را به‌صورت یک فلگ به همه نمونه‌های اجزایی
که به چنین پیکربندی سفارشی‌ای نیاز دارند، ارسال کرد.

{{< note >}}
اگر میزبان درگاه پیش‌فرض نداشته باشد و نشانی IP سفارشی نیز به یک جزء کوبرنتیز
ارسال نشود، ممکن است آن جزء با خطا خارج شود.
{{< /note >}}

برای پیکربندی نشانی اعلام‌شده API server در نودهای control plane که با هر دو فرمان
`init` و `join` ایجاد می‌شوند، می‌توان از فلگ `--apiserver-advertise-address` استفاده کرد.
ترجیحاً می‌توان این گزینه را در [API ابزار kubeadm](/docs/reference/config-api/kubeadm-config.v1beta4)
به‌صورت `InitConfiguration.localAPIEndpoint` و `JoinConfiguration.controlPlane.localAPIEndpoint` تنظیم کرد.

برای kubeletها در همه نودها، می‌توان گزینه `--node-ip` را در
`.nodeRegistration.kubeletExtraArgs` درون یک فایل پیکربندی kubeadm
(`InitConfiguration` یا `JoinConfiguration`) ارسال کرد.

برای پشته دوگانه (dual-stack)،
[پشتیبانی از پشته دوگانه با kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support) را ببینید.

نشانی‌های IP که به اجزای control plane اختصاص می‌دهید، بخشی از فیلدهای
subject alternative name در گواهی‌های X.509 آن‌ها می‌شوند. تغییر این نشانی‌های IP
مستلزم امضای گواهی‌های جدید و راه‌اندازی مجدد اجزای تحت تأثیر است تا تغییر
در فایل‌های گواهی اعمال شود. برای جزئیات بیشتر در این زمینه،
[تمدید دستی گواهی](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#manual-certificate-renewal)
را ببینید.

{{< warning >}}
پروژه کوبرنتیز این رویکرد (پیکربندی همه نمونه‌های اجزا با نشانی‌های IP سفارشی) را توصیه نمی‌کند.
در عوض، نگه‌دارندگان کوبرنتیز توصیه می‌کنند شبکه میزبان را طوری پیکربندی کنید
که IP درگاه پیش‌فرض همان IP باشد که اجزای کوبرنتیز به‌طور خودکار تشخیص می‌دهند و از آن استفاده می‌کنند.
در نودهای لینوکسی، می‌توانید برای پیکربندی شبکه از فرمان‌هایی مانند `ip route` استفاده کنید؛ ممکن است
سیستم‌عامل شما ابزارهای سطح بالاتری نیز برای مدیریت شبکه فراهم کند. اگر درگاه پیش‌فرض نود شما
یک نشانی IP عمومی است، باید فیلترکردن بسته‌ها یا دیگر تدابیر امنیتی را برای محافظت از
نودها و کلاستر خود پیکربندی کنید.
{{< /warning >}}

### آماده‌سازی ایمیج‌های کانتینر موردنیاز

این گام اختیاری است و تنها زمانی کاربرد دارد که بخواهید `kubeadm init` و `kubeadm join`
ایمیج‌های کانتینر پیش‌فرضِ میزبانی‌شده در `registry.k8s.io` را دانلود نکنند.

ابزار kubeadm فرمان‌هایی دارد که به شما کمک می‌کنند هنگام ایجاد کلاستری که نودهای آن
به اینترنت دسترسی ندارند، ایمیج‌های موردنیاز را از پیش دریافت (pre-pull) کنید.
برای جزئیات بیشتر، [اجرای kubeadm بدون اتصال به اینترنت](/docs/reference/setup-tools/kubeadm/kubeadm-init#without-internet-connection)
را ببینید.

ابزار kubeadm به شما امکان می‌دهد برای ایمیج‌های موردنیاز از یک مخزن ایمیج سفارشی استفاده کنید.
برای جزئیات بیشتر، [استفاده از ایمیج‌های سفارشی](/docs/reference/setup-tools/kubeadm/kubeadm-init#custom-images)
را ببینید.

### مقداردهی اولیه نود control plane

نود control plane ماشینی است که اجزای control plane روی آن اجرا می‌شوند؛ از جمله
{{< glossary_tooltip term_id="etcd" >}} (پایگاه داده کلاستر) و
{{< glossary_tooltip text="API Server" term_id="kube-apiserver" >}}
(که ابزار خط فرمان {{< glossary_tooltip text="kubectl" term_id="kubectl" >}}
با آن ارتباط برقرار می‌کند).

1. (توصیه‌شده) اگر قصد دارید این کلاستر `kubeadm` با یک control plane را
   به [دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/high-availability/)
   ارتقا دهید، باید `--control-plane-endpoint` را مشخص کنید تا نقطه پایانی (endpoint) مشترک همه نودهای control plane تعیین شود.
   این نقطه پایانی می‌تواند یک نام DNS یا نشانی IP یک متعادل‌کننده بار (load-balancer) باشد.
1. یک افزونه شبکه Pod انتخاب کنید و بررسی کنید که آیا لازم است آرگومانی
   به `kubeadm init` ارسال شود یا نه. بسته به اینکه کدام
   ارائه‌دهنده شخص ثالث را انتخاب می‌کنید، ممکن است لازم باشد `--pod-network-cidr` را
   روی مقداری مختص آن ارائه‌دهنده تنظیم کنید. [نصب افزونه شبکه Pod](#pod-network) را ببینید.
1. (اختیاری) ابزار `kubeadm` تلاش می‌کند محیط اجرای کانتینر را با استفاده از فهرستی از نقاط پایانی
   شناخته‌شده تشخیص دهد. برای استفاده از محیط اجرای کانتینر دیگری، یا اگر بیش از یک محیط اجرا
   روی نود تأمین‌شده نصب است، آرگومان `--cri-socket` را به `kubeadm` بدهید.
   [نصب محیط اجرا](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-runtime) را ببینید.

برای مقداردهی اولیه نود control plane، فرمان زیر را اجرا کنید:

```bash
kubeadm init <args>
```

### ملاحظاتی درباره apiserver-advertise-address و ControlPlaneEndpoint

از فلگ `--apiserver-advertise-address` می‌توان برای تنظیم نشانی اعلام‌شده API server همین
نود control plane استفاده کرد، در حالی که از `--control-plane-endpoint` می‌توان برای تنظیم نقطه پایانی مشترک
همه نودهای control plane بهره برد.

فلگ `--control-plane-endpoint` هم نشانی IP و هم نام‌های DNS را که به نشانی IP نگاشت می‌شوند، می‌پذیرد.
لطفاً برای ارزیابی راه‌حل‌های ممکن درباره چنین نگاشتی با مدیر شبکه خود تماس بگیرید.

نمونه‌ای از یک نگاشت در ادامه آمده است:

```
192.168.0.102 cluster-endpoint
```

در این نمونه، `192.168.0.102` نشانی IP این نود و `cluster-endpoint` یک نام DNS سفارشی است که به این IP نگاشت می‌شود.
با این کار می‌توانید `--control-plane-endpoint=cluster-endpoint` را به `kubeadm init` بدهید و همین نام DNS را به
`kubeadm join` ارسال کنید. بعدها در یک سناریوی دسترس‌پذیری بالا می‌توانید `cluster-endpoint` را طوری تغییر دهید
که به نشانی متعادل‌کننده بار شما اشاره کند.

ابزار kubeadm از تبدیل کلاستری با یک control plane که بدون `--control-plane-endpoint` ایجاد شده،
به یک کلاستر با دسترس‌پذیری بالا پشتیبانی نمی‌کند.

### اطلاعات بیشتر

برای اطلاعات بیشتر درباره آرگومان‌های `kubeadm init`، [راهنمای مرجع kubeadm](/docs/reference/setup-tools/kubeadm/) را ببینید.

برای پیکربندی `kubeadm init` با یک فایل پیکربندی،
[استفاده از kubeadm init با فایل پیکربندی](/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file) را ببینید.

برای سفارشی‌سازی اجزای control plane، از جمله اختصاص اختیاری IPv6 به کاوشگر زنده‌بودن (liveness probe)
برای اجزای control plane و سرور etcd، آرگومان‌های اضافی را مطابق مستندات
[آرگومان‌های سفارشی](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/) به هر جزء بدهید.

برای پیکربندی مجدد کلاستری که از قبل ایجاد شده است،
[پیکربندی مجدد کلاستر kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure) را ببینید.

برای اجرای دوباره `kubeadm init`، ابتدا باید [کلاستر را برچینید](#tear-down).

اگر نودی با معماری متفاوت را به کلاستر خود ملحق می‌کنید، مطمئن شوید که DaemonSetهای مستقرشده شما
از ایمیج کانتینر برای این معماری پشتیبانی می‌کنند.

فرمان `kubeadm init` ابتدا مجموعه‌ای از بررسی‌های اولیه را اجرا می‌کند تا مطمئن شود ماشین
برای اجرای کوبرنتیز آماده است. این بررسی‌ها هشدارها را نمایش می‌دهند و در صورت بروز خطا خارج می‌شوند. سپس
`kubeadm init` اجزای control plane کلاستر را دانلود و نصب می‌کند. این کار ممکن است چند دقیقه طول بکشد.
پس از پایان کار، باید خروجی زیر را ببینید:

```none
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a Pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  /docs/concepts/cluster-administration/addons/

You can now join any number of machines by running the following on each node
as root:

  kubeadm join <control-plane-host>:<control-plane-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

برای اینکه kubectl برای کاربر غیر root شما کار کند، فرمان‌های زیر را اجرا کنید؛ این فرمان‌ها
بخشی از خروجی `kubeadm init` نیز هستند:

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

همچنین اگر کاربر `root` هستید، می‌توانید فرمان زیر را اجرا کنید:

```bash
export KUBECONFIG=/etc/kubernetes/admin.conf
```

{{< warning >}}
فایل kubeconfig با نام `admin.conf` که `kubeadm init` تولید می‌کند، حاوی گواهی‌ای با
`Subject: O = kubeadm:cluster-admins, CN = kubernetes-admin` است. گروه `kubeadm:cluster-admins`
به ClusterRole داخلی `cluster-admin` متصل (bind) شده است.
فایل `admin.conf` را با هیچ‌کس به اشتراک نگذارید.

فرمان `kubeadm init` فایل kubeconfig دیگری به نام `super-admin.conf` نیز تولید می‌کند که حاوی گواهی‌ای با
`Subject: O = system:masters, CN = kubernetes-super-admin` است.
گروه `system:masters` یک گروه ابرکاربر برای مواقع اضطراری (break-glass) است که لایه مجوزدهی (برای مثال RBAC) را دور می‌زند.
فایل `super-admin.conf` را با هیچ‌کس به اشتراک نگذارید. توصیه می‌شود این فایل را به مکانی امن منتقل کنید.

برای آشنایی با نحوه استفاده از `kubeadm kubeconfig user` جهت تولید فایل‌های kubeconfig برای کاربران دیگر،
[تولید فایل‌های kubeconfig برای کاربران دیگر](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#kubeconfig-additional-users)
را ببینید.
{{< /warning >}}

فرمان `kubeadm join` را که `kubeadm init` در خروجی نمایش می‌دهد، یادداشت کنید.
برای [ملحق کردن نودها به کلاستر](#join-nodes) به این فرمان نیاز دارید.

این توکن برای احراز هویت متقابل میان نود control plane و نودهای در حال الحاق استفاده می‌شود.
توکنی که در اینجا آمده، محرمانه است. آن را در جای امنی نگه دارید، زیرا هر کسی که این
توکن را داشته باشد می‌تواند نودهای احراز هویت‌شده به کلاستر شما اضافه کند. می‌توانید با فرمان
`kubeadm token` این توکن‌ها را فهرست، ایجاد و حذف کنید.
[راهنمای مرجع kubeadm](/docs/reference/setup-tools/kubeadm/kubeadm-token/) را ببینید.

### نصب افزونه شبکه Pod {#pod-network}

{{< caution >}}
این بخش حاوی اطلاعات مهمی درباره پیکربندی شبکه و
ترتیب استقرار است.
پیش از ادامه، همه این توصیه‌ها را با دقت بخوانید.

**باید یک افزونه شبکه Pod مبتنی بر
{{< glossary_tooltip text="رابط شبکه کانتینر" term_id="cni" >}}
(CNI) مستقر کنید تا Podهای شما بتوانند با یکدیگر ارتباط برقرار کنند.
سرویس DNS کلاستر (CoreDNS) پیش از نصب شبکه راه‌اندازی نمی‌شود.**

- دقت کنید که شبکه Pod شما نباید با هیچ‌یک از شبکه‌های میزبان همپوشانی داشته باشد:
  در صورت وجود هرگونه همپوشانی، به احتمال زیاد با مشکل روبه‌رو خواهید شد.
  (اگر میان شبکه Pod ترجیحی افزونه شبکه خود و برخی از شبکه‌های میزبان
  تداخلی یافتید، باید یک بلوک CIDR مناسب را جایگزین آن کنید
  و سپس هنگام اجرای `kubeadm init` آن را با `--pod-network-cidr` به کار ببرید
  و در YAML افزونه شبکه خود نیز جایگزین کنید).

- به‌طور پیش‌فرض، `kubeadm` کلاستر شما را طوری پیکربندی می‌کند که از
  [RBAC](/docs/reference/access-authn-authz/rbac/) (کنترل دسترسی مبتنی بر نقش) استفاده کند
  و استفاده از آن را الزامی کند.
  مطمئن شوید که افزونه شبکه Pod شما و همه مانیفست‌هایی که برای استقرار آن
  استفاده می‌کنید، از RBAC پشتیبانی می‌کنند.

- اگر می‌خواهید برای کلاستر خود از IPv6 استفاده کنید (چه به‌صورت پشته دوگانه و چه
  به‌صورت شبکه تک‌پشته فقط IPv6)، مطمئن شوید که افزونه شبکه Pod شما
  از IPv6 پشتیبانی می‌کند.
  پشتیبانی از IPv6 در [نسخه v0.6.0](https://github.com/containernetworking/cni/releases/tag/v0.6.0) به CNI افزوده شد.

{{< /caution >}}

{{< note >}}
ابزار kubeadm باید نسبت به CNI بی‌طرف باشد و اعتبارسنجی ارائه‌دهندگان CNI خارج از دامنه آزمون‌های e2e فعلی ما است.
اگر با مشکلی مرتبط با یک افزونه CNI روبه‌رو شدید، باید آن را در سامانه پیگیری مشکلات (issue tracker)
همان افزونه ثبت کنید، نه در سامانه‌های پیگیری مشکلات kubeadm یا کوبرنتیز.
{{< /note >}}

چندین پروژه خارجی، شبکه‌های Pod کوبرنتیز را با استفاده از CNI فراهم می‌کنند و برخی از آن‌ها
از [سیاست شبکه (Network Policy)](/docs/concepts/services-networking/network-policies/) نیز پشتیبانی می‌کنند.

فهرستی از افزونه‌هایی را که
[مدل شبکه کوبرنتیز](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model)
را پیاده‌سازی می‌کنند، ببینید.

برای مشاهده فهرستی غیرجامع از افزونه‌های شبکه‌ای که کوبرنتیز پشتیبانی می‌کند، لطفاً به صفحه
[نصب افزونه‌ها](/docs/concepts/cluster-administration/addons/#networking-and-network-policy) مراجعه کنید.
می‌توانید افزونه شبکه Pod را با فرمان زیر روی نود control plane
یا نودی که اعتبارنامه‌های kubeconfig را در اختیار دارد، نصب کنید:

```bash
kubectl apply -f <add-on.yaml>
```

{{< note >}}
تنها تعداد اندکی از افزونه‌های CNI از ویندوز پشتیبانی می‌کنند. جزئیات بیشتر و دستورالعمل‌های پیکربندی را می‌توانید
در [افزودن نودهای کارگر ویندوزی](/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/#network-config) بیابید.
{{< /note >}}

در هر کلاستر تنها می‌توانید یک شبکه Pod نصب کنید.

پس از نصب شبکه Pod، می‌توانید با بررسی اینکه Pod مربوط به CoreDNS در خروجی
`kubectl get pods --all-namespaces` در وضعیت `Running` قرار دارد، از کارکرد درست آن اطمینان پیدا کنید.
پس از اینکه Pod مربوط به CoreDNS راه‌اندازی شد و در حال اجرا بود، می‌توانید با ملحق کردن نودهای خود ادامه دهید.

اگر شبکه شما کار نمی‌کند یا CoreDNS در وضعیت `Running` نیست،
[راهنمای عیب‌یابی](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/)
ابزار `kubeadm` را ببینید.

### برچسب‌های مدیریت‌شدهٔ نود

ابزار kubeadm به‌طور پیش‌فرض کنترل‌کنندهٔ پذیرش (admission controller) [NodeRestriction](/docs/reference/access-authn-authz/admission-controllers/#noderestriction) را فعال می‌کند. این کنترل‌کننده مشخص می‌کند که kubelet هنگام ثبت نود، کدام برچسب‌ها را می‌تواند خودش روی نود اعمال کند. در مستندات این کنترل‌کنندهٔ پذیرش آمده است که کدام برچسب‌ها را می‌توان با گزینهٔ `--node-labels` در kubelet به کار برد.

{{< caution >}}
به دلیل وجود کنترل‌کنندهٔ پذیرش `NodeRestriction`، **نمی‌توانید** با فلگ `--node-labels` در kubelet، برچسب‌های محدودشده (مانند `node-role.kubernetes.io/*`) را هنگام راه‌اندازی اولیه اعمال کنید.

اگر بکوشید برچسب‌های محدودشده را با این فلگ kubelet اضافه کنید، ثبت نود در API server با شکست روبه‌رو می‌شود.
{{< /caution >}}

برای اعمال دستی این برچسب‌ها، باید پس از پیوستن نود به کلاستر از دستور `kubectl label` استفاده کنید. مطمئن شوید که از یک kubeconfig دارای دسترسی ممتاز، مانند فایل `/etc/kubernetes/admin.conf` که kubeadm آن را مدیریت می‌کند، استفاده می‌کنید.

### جداسازی نود control plane

کلاستر شما به‌طور پیش‌فرض و به دلایل امنیتی، Podها را روی نودهای control plane زمان‌بندی نمی‌کند. اگر می‌خواهید بتوانید Podها را روی نودهای control plane زمان‌بندی کنید، برای نمونه در یک کلاستر کوبرنتیز تک‌ماشینی، این دستور را اجرا کنید:

```bash
kubectl taint nodes --all node-role.kubernetes.io/control-plane-
```

خروجی چیزی شبیه به این خواهد بود:

```
node "test-01" untainted
...
```

این دستور taint با عنوان `node-role.kubernetes.io/control-plane:NoSchedule` را از همهٔ نودهایی که آن را دارند، از جمله نودهای control plane، حذف می‌کند. در نتیجه زمان‌بند از این پس می‌تواند Podها را روی همهٔ نودها زمان‌بندی کند.

افزون بر این، می‌توانید دستور زیر را اجرا کنید تا برچسب [`node.kubernetes.io/exclude-from-external-load-balancers`](/docs/reference/labels-annotations-taints/#node-kubernetes-io-exclude-from-external-load-balancers) را از نود control plane حذف کنید؛ این برچسب نود را از فهرست سرورهای پشتیبان (backend) کنار می‌گذارد:

```bash
kubectl label nodes --all node.kubernetes.io/exclude-from-external-load-balancers-
```

### افزودن نودهای control plane بیشتر

برای آشنایی با مراحل ایجاد یک کلاستر kubeadm با دسترس‌پذیری بالا از طریق افزودن نودهای control plane بیشتر، به [ایجاد کلاسترهای با دسترس‌پذیری بالا با kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/) مراجعه کنید.

### افزودن نودهای کارگر {#join-nodes}

بارهای کاری شما روی نودهای کارگر (worker) اجرا می‌شوند.

صفحه‌های زیر نشان می‌دهند که چگونه می‌توان با دستور `kubeadm join` نودهای کارگر لینوکس و ویندوز را به کلاستر افزود:

* [افزودن نودهای کارگر لینوکس](/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/)
* [افزودن نودهای کارگر ویندوز](/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)

### (اختیاری) کنترل کلاستر از ماشین‌هایی غیر از نود control plane

برای آنکه kubectl روی رایانه‌ای دیگر (مثلاً لپ‌تاپ) بتواند با کلاستر شما ارتباط برقرار کند، باید فایل kubeconfig مدیر را به این شکل از نود control plane به ایستگاه کاری خود کپی کنید:

```bash
scp root@<control-plane-host>:/etc/kubernetes/admin.conf .
kubectl --kubeconfig ./admin.conf get nodes
```

{{< note >}}
در مثال بالا فرض شده است که دسترسی SSH برای کاربر root فعال است. اگر چنین نیست، می‌توانید فایل `admin.conf` را طوری کپی کنید که کاربر دیگری به آن دسترسی داشته باشد و سپس با همان کاربر عمل `scp` را انجام دهید.

فایل `admin.conf` به کاربر، دسترسی‌های _ابرکاربر_ (superuser) روی کلاستر می‌دهد. از این فایل باید با احتیاط و به‌ندرت استفاده کرد. برای کاربران عادی توصیه می‌شود یک اعتبارنامهٔ یکتا بسازید و دسترسی‌های لازم را به آن بدهید. این کار را می‌توانید با دستور `kubeadm kubeconfig user --client-name <CN>` انجام دهید. این دستور یک فایل KubeConfig را در STDOUT چاپ می‌کند که باید آن را در یک فایل ذخیره کنید و در اختیار کاربر خود بگذارید. پس از آن، با دستور `kubectl create (cluster)rolebinding` دسترسی‌ها را اعطا کنید.
{{< /note >}}

### (اختیاری) پراکسی کردن API Server به localhost

اگر می‌خواهید از بیرون کلاستر به API Server متصل شوید، می‌توانید از `kubectl proxy` استفاده کنید:

```bash
scp root@<control-plane-host>:/etc/kubernetes/admin.conf .
kubectl --kubeconfig ./admin.conf proxy
```

اکنون می‌توانید به‌صورت محلی از نشانی `http://localhost:8001/api/v1` به API Server دسترسی داشته باشید.

## پاک‌سازی {#tear-down}

اگر برای آزمایش، از سرورهای یک‌بارمصرف برای کلاستر خود استفاده کرده‌اید، می‌توانید آن‌ها را خاموش کنید و نیازی به پاک‌سازی بیشتر نیست. برای حذف ارجاع‌های محلی به کلاستر می‌توانید از `kubectl config delete-cluster` استفاده کنید.

اما اگر می‌خواهید کلاستر خود را به شکلی تمیزتر از کار بیندازید، ابتدا باید [نود را تخلیه کنید](/docs/reference/generated/kubectl/kubectl-commands#drain) و مطمئن شوید که نود خالی است؛ سپس پیکربندی نود را بردارید.

### حذف نود

با اعتبارنامه‌های مناسب با نود control plane ارتباط برقرار کنید و این دستور را اجرا کنید:

```bash
kubectl drain <node name> --delete-emptydir-data --force --ignore-daemonsets
```

پیش از حذف نود، وضعیتی را که `kubeadm` نصب کرده است بازنشانی کنید:

```bash
kubeadm reset
```

فرایند بازنشانی، قواعد iptables یا جدول‌های IPVS را بازنشانی یا پاک‌سازی نمی‌کند. اگر می‌خواهید iptables را بازنشانی کنید، باید این کار را به‌صورت دستی انجام دهید:

```bash
iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X
```

اگر می‌خواهید جدول‌های IPVS را بازنشانی کنید، باید دستور زیر را اجرا کنید:

```bash
ipvsadm -C
```

اکنون نود را حذف کنید:

```bash
kubectl delete node <node name>
```

اگر می‌خواهید از نو شروع کنید، دستور `kubeadm init` یا `kubeadm join` را با آرگومان‌های مناسب اجرا کنید.

### پاک‌سازی control plane

می‌توانید با اجرای `kubeadm reset` روی میزبان control plane، یک پاک‌سازی در حد امکان (best-effort) را آغاز کنید.

برای اطلاعات بیشتر دربارهٔ این زیرفرمان و گزینه‌های آن، به مستندات مرجع [`kubeadm reset`](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) مراجعه کنید.

## سیاست اختلاف نسخه {#version-skew-policy}

هرچند kubeadm اختلاف نسخه (version skew) با برخی از مؤلفه‌هایی را که مدیریت می‌کند مجاز می‌داند، توصیه می‌شود نسخهٔ kubeadm را با نسخه‌های مؤلفه‌های control plane، kube-proxy و kubelet یکسان نگه دارید.

### اختلاف نسخهٔ kubeadm با نسخهٔ کوبرنتیز

ابزار kubeadm را می‌توان با مؤلفه‌های کوبرنتیزی به کار برد که هم‌نسخهٔ kubeadm یا یک نسخه قدیمی‌تر از آن هستند. نسخهٔ کوبرنتیز را می‌توان با فلگ `--kubernetes-version` در `kubeadm init`، یا هنگام استفاده از `--config` با فیلد [`ClusterConfiguration.kubernetesVersion`](/docs/reference/config-api/kubeadm-config.v1beta4/)، برای kubeadm مشخص کرد. این گزینه نسخه‌های kube-apiserver، kube-controller-manager، kube-scheduler و kube-proxy را تعیین می‌کند.

مثال:

* نسخهٔ kubeadm برابر {{< skew currentVersion >}} است
* مقدار `kubernetesVersion` باید {{< skew currentVersion >}} یا {{< skew currentVersionAddMinor -1 >}} باشد

### اختلاف نسخهٔ kubeadm با kubelet

همانند نسخهٔ کوبرنتیز، kubeadm را می‌توان با نسخه‌ای از kubelet به کار برد که هم‌نسخهٔ kubeadm یا حداکثر سه نسخه قدیمی‌تر از آن باشد.

مثال:

* نسخهٔ kubeadm برابر {{< skew currentVersion >}} است
* نسخهٔ kubelet روی میزبان باید {{< skew currentVersion >}}، {{< skew currentVersionAddMinor -1 >}}،
  {{< skew currentVersionAddMinor -2 >}} یا {{< skew currentVersionAddMinor -3 >}} باشد

### اختلاف نسخهٔ kubeadm با kubeadm

نحوهٔ عملکرد فرمان‌های kubeadm روی نودهای موجود یا کل کلاسترهایی که kubeadm آن‌ها را مدیریت می‌کند، محدودیت‌های مشخصی دارد.

اگر نودهای جدیدی به کلاستر بپیوندند، فایل اجرایی kubeadm که برای `kubeadm join` به کار می‌رود باید با آخرین نسخه‌ای از kubeadm یکسان باشد که برای ایجاد کلاستر با `kubeadm init` یا برای ارتقای همان نود با `kubeadm upgrade` استفاده شده است. قواعد مشابهی برای سایر فرمان‌های kubeadm نیز برقرار است، به‌جز `kubeadm upgrade`.

مثال برای `kubeadm join`:

* از kubeadm نسخهٔ {{< skew currentVersion >}} برای ایجاد کلاستر با `kubeadm init` استفاده شده است
* نودهایی که به کلاستر می‌پیوندند باید از فایل اجرایی kubeadm با نسخهٔ {{< skew currentVersion >}} استفاده کنند

نودهایی که در حال ارتقا هستند باید از نسخه‌ای از kubeadm استفاده کنند که نسخهٔ MINOR آن با نسخهٔ kubeadm به‌کاررفته برای مدیریت نود یکسان باشد یا یک نسخهٔ MINOR جدیدتر از آن باشد.

مثال برای `kubeadm upgrade`:

* از kubeadm نسخهٔ {{< skew currentVersionAddMinor -1 >}} برای ایجاد یا ارتقای نود استفاده شده است
* نسخهٔ kubeadm که برای ارتقای نود به کار می‌رود باید {{< skew currentVersionAddMinor -1 >}}
  یا {{< skew currentVersion >}} باشد

برای آشنایی بیشتر با اختلاف نسخه میان مؤلفه‌های گوناگون کوبرنتیز، به [سیاست اختلاف نسخه](/releases/version-skew-policy/) مراجعه کنید.

## محدودیت‌ها {#limitations}

### تاب‌آوری کلاستر {#resilience}

کلاستری که در اینجا ایجاد شد، تنها یک نود control plane دارد که یک پایگاه دادهٔ etcd نیز روی آن اجرا می‌شود. به این معنا که اگر نود control plane از کار بیفتد، ممکن است کلاستر شما داده‌هایش را از دست بدهد و لازم باشد از ابتدا دوباره ساخته شود.

راهکارها:

* به‌طور منظم [از etcd نسخهٔ پشتیبان بگیرید](https://etcd.io/docs/v3.5/op-guide/recovery/). پوشهٔ دادهٔ etcd که kubeadm پیکربندی می‌کند، در مسیر `/var/lib/etcd` روی نود control plane قرار دارد.

* از چند نود control plane استفاده کنید. می‌توانید [گزینه‌های توپولوژی با دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/ha-topology/) را مطالعه کنید تا توپولوژی کلاستری را برگزینید که [دسترس‌پذیری بالا](/docs/setup/production-environment/tools/kubeadm/high-availability/) فراهم می‌کند.

### سازگاری با پلتفرم‌ها {#multi-platform}

بسته‌های deb/rpm و فایل‌های اجرایی kubeadm، مطابق با [پیشنهاد چندپلتفرمی](https://git.k8s.io/design-proposals-archive/multi-platform.md)، برای معماری‌های amd64، arm (۳۲ بیتی)، arm64، ppc64le و s390x ساخته می‌شوند.

از نسخهٔ v1.12 به بعد، ایمیج‌های کانتینر چندپلتفرمی برای control plane و افزونه‌ها نیز پشتیبانی می‌شوند.

تنها برخی از ارائه‌دهندگان شبکه برای همهٔ پلتفرم‌ها راه‌حل ارائه می‌کنند. لطفاً به فهرست ارائه‌دهندگان شبکه در بالا یا مستندات هر ارائه‌دهنده مراجعه کنید تا دریابید که آیا آن ارائه‌دهنده از پلتفرم انتخابی شما پشتیبانی می‌کند یا نه.

## عیب‌یابی {#troubleshooting}

اگر در کار با kubeadm به مشکل برخوردید، لطفاً به [مستندات عیب‌یابی](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/) ما مراجعه کنید.

<!-- discussion -->

## {{% heading "whatsnext" %}}

* با [Sonobuoy](https://github.com/heptio/sonobuoy) بررسی کنید که کلاستر شما به‌درستی کار می‌کند
* <a id="lifecycle" />برای جزئیات ارتقای کلاستر با `kubeadm`، به [ارتقای کلاسترهای kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
  مراجعه کنید.
* با کاربردهای پیشرفتهٔ `kubeadm` در [مستندات مرجع kubeadm](/docs/reference/setup-tools/kubeadm/) آشنا شوید
* دربارهٔ [مفاهیم](/docs/concepts/) کوبرنتیز و [`kubectl`](/docs/reference/kubectl/) بیشتر بیاموزید.
* برای فهرست کامل‌تری از افزونه‌های شبکهٔ Pod، صفحهٔ [شبکه‌بندی کلاستر](/docs/concepts/cluster-administration/networking/)
  را ببینید.
* <a id="other-addons" />برای آشنایی با افزونه‌های دیگر، از جمله ابزارهای ثبت لاگ، پایش، سیاست شبکه، مصورسازی و
  کنترل کلاستر کوبرنتیز، [فهرست افزونه‌ها](/docs/concepts/cluster-administration/addons/) را ببینید.
* نحوهٔ مدیریت لاگ‌های رویدادهای کلاستر و لاگ‌های برنامه‌های در حال اجرا در Podها را در کلاستر خود پیکربندی کنید.
  برای مروری بر آنچه این کار در بر دارد، به [معماری ثبت لاگ](/docs/concepts/cluster-administration/logging/)
  مراجعه کنید.

### بازخورد {#feedback}

* برای گزارش باگ‌ها، به [ردیاب مسائل kubeadm در GitHub](https://github.com/kubernetes/kubeadm/issues) مراجعه کنید
* برای دریافت پشتیبانی، به کانال
  [#kubeadm](https://kubernetes.slack.com/messages/kubeadm/) در Slack مراجعه کنید
* کانال عمومی Slack برای توسعهٔ SIG Cluster Lifecycle:
  [#sig-cluster-lifecycle](https://kubernetes.slack.com/messages/sig-cluster-lifecycle/)
* [اطلاعات SIG](https://github.com/kubernetes/community/tree/main/sig-cluster-lifecycle#readme) مربوط به SIG Cluster Lifecycle
* فهرست پستی SIG Cluster Lifecycle:
  [kubernetes-sig-cluster-lifecycle](https://groups.google.com/forum/#!forum/kubernetes-sig-cluster-lifecycle)
