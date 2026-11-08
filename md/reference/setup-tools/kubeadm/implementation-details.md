---
reviewers:
- luxas
- jbeda
title: جزئیات پیاده‌سازی
content_type: concept
weight: 100
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.10" state="stable" >}}

دستورهای `kubeadm init` و `kubeadm join` در کنار هم تجربه کاربری خوبی برای ایجاد یک کلاستر خام کوبرنتیز از ابتدا و مطابق با بهترین شیوه‌ها فراهم می‌کنند. با این حال، شاید روشن نباشد که kubeadm این کار را _چگونه_ انجام می‌دهد.

این سند جزئیات بیشتری از آنچه در پشت صحنه رخ می‌دهد ارائه می‌کند تا دانش مربوط به بهترین شیوه‌های راه‌اندازی کلاستر کوبرنتیز به اشتراک گذاشته شود.

<!-- body -->

## اصول اصلی طراحی

کلاستری که `kubeadm init` و `kubeadm join` راه‌اندازی می‌کنند باید این ویژگی‌ها را داشته باشد:

- **امن**: این کلاستر باید جدیدترین بهترین شیوه‌ها را به کار بگیرد، از جمله:
  - اعمال اجباری RBAC
  - استفاده از Node Authorizer
  - استفاده از ارتباط امن میان مؤلفه‌های control plane
  - استفاده از ارتباط امن میان سرور API و kubeletها
  - محدودسازی دسترسی به API مربوط به kubelet
  - محدودسازی دسترسی مؤلفه‌های سیستمی مانند kube-proxy و CoreDNS به API
  - محدودسازی منابعی که یک Bootstrap Token می‌تواند به آن‌ها دسترسی داشته باشد
- **کاربرپسند**: کاربر نباید به اجرای چیزی بیش از چند دستور نیاز داشته باشد:
  - `kubeadm init`
  - `export KUBECONFIG=/etc/kubernetes/admin.conf`
  - `kubectl apply -f <network-plugin-of-choice.yaml>`
  - `kubeadm join --token <token> <endpoint>:<port>`
- **توسعه‌پذیر**:
  - این کلاستر _نباید_ هیچ ارائه‌دهنده شبکه خاصی را ترجیح دهد. پیکربندی شبکه کلاستر خارج از محدوده kubeadm است.
  - باید بتوان از یک فایل پیکربندی برای سفارشی‌سازی پارامترهای مختلف استفاده کرد.

## مقادیر و مسیرهای ثابت و شناخته‌شده

برای کاهش پیچیدگی و ساده‌تر شدن توسعه ابزارهای سطح بالاتری که بر پایه kubeadm ساخته می‌شوند، این ابزار مجموعه محدودی از مقادیر ثابت را برای مسیرها و نام فایل‌های شناخته‌شده به کار می‌برد.

دایرکتوری کوبرنتیز، یعنی `/etc/kubernetes`، در این برنامه مقداری ثابت است، زیرا در بیشتر موارد همین مسیر استفاده می‌شود و شهودی‌ترین مکان نیز هست. سایر مسیرها و نام فایل‌های ثابت عبارت‌اند از:

- مسیر `/etc/kubernetes/manifests` که kubelet باید مانیفست‌های Pod ایستا را در آن جست‌وجو کند. نام مانیفست‌های Pod ایستا عبارت‌اند از:

  - `etcd.yaml`
  - `kube-apiserver.yaml`
  - `kube-controller-manager.yaml`
  - `kube-scheduler.yaml`

- مسیر `/etc/kubernetes/` که فایل‌های kubeconfig حاوی هویت مؤلفه‌های control plane در آن ذخیره می‌شوند. نام فایل‌های kubeconfig عبارت‌اند از:

  - فایل `kubelet.conf` (و در زمان راه‌اندازی اولیه TLS، فایل `bootstrap-kubelet.conf`)
  - فایل `controller-manager.conf`
  - فایل `scheduler.conf`
  - فایل `admin.conf` برای مدیر کلاستر و خود kubeadm
  - فایل `super-admin.conf` برای مدیر ارشد کلاستر که می‌تواند RBAC را دور بزند

- نام فایل‌های گواهی و کلید:

  - فایل‌های `ca.crt` و `ca.key` برای مرجع صدور گواهی کوبرنتیز
  - فایل‌های `apiserver.crt` و `apiserver.key` برای گواهی سرور API
  - فایل‌های `apiserver-kubelet-client.crt` و `apiserver-kubelet-client.key` برای گواهی کلاینتی که سرور API با آن به‌صورت امن به kubeletها متصل می‌شود
  - فایل‌های `sa.pub` و `sa.key` برای کلیدی که controller manager هنگام امضای ServiceAccount از آن استفاده می‌کند
  - فایل‌های `front-proxy-ca.crt` و `front-proxy-ca.key` برای مرجع صدور گواهی پراکسی جلویی (front proxy)
  - فایل‌های `front-proxy-client.crt` و `front-proxy-client.key` برای کلاینت پراکسی جلویی

## قالب فایل پیکربندی kubeadm

بیشتر دستورهای kubeadm از پرچم `--config` پشتیبانی می‌کنند که با آن می‌توان یک فایل پیکربندی را از دیسک به دستور داد. قالب این فایل از طرح رایج `apiVersion` / `kind` در API کوبرنتیز پیروی می‌کند، اما قالب پیکربندی مؤلفه به شمار می‌رود. چند مؤلفه دیگر کوبرنتیز، مانند kubelet، نیز از پیکربندی مبتنی بر فایل پشتیبانی می‌کنند.

زیردستورهای مختلف kubeadm به فایل پیکربندی با `kind` متفاوتی نیاز دارند. برای نمونه، `InitConfiguration` برای `kubeadm init`، `JoinConfiguration` برای `kubeadm join`، `UpgradeConfiguration` برای `kubeadm upgrade` و `ResetConfiguration` برای `kubeadm reset` به کار می‌رود.

با دستور `kubeadm config migrate` می‌توان فایل پیکربندی با قالب قدیمی‌تر را به قالب جدیدتر (فعلی) مهاجرت داد. ابزار kubeadm فقط مهاجرت از قالب‌های منسوخ‌شده به قالب فعلی را پشتیبانی می‌کند.

برای جزئیات بیشتر، صفحه [مرجع پیکربندی kubeadm](/docs/reference/config-api/kubeadm-config.v1beta4/) را ببینید.

## طراحی داخلی گردش کار kubeadm init

دستور `kubeadm init` از دنباله‌ای از کارهای اتمی تشکیل شده است که در [گردش کار داخلی](/docs/reference/setup-tools/kubeadm/kubeadm-init/#init-workflow) `kubeadm init` شرح داده شده‌اند.

با دستور [`kubeadm init phase`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/) کاربران می‌توانند هر کار را جداگانه اجرا کنند. این دستور در نهایت یک API یا جعبه‌ابزار قابل استفاده مجدد و ترکیب‌پذیر فراهم می‌کند که سایر ابزارهای راه‌اندازی کوبرنتیز، ابزارهای خودکارسازی فناوری اطلاعات یا کاربران پیشرفته می‌توانند برای ایجاد کلاسترهای سفارشی از آن استفاده کنند.

### بررسی‌های پیش از اجرا

ابزار kubeadm پیش از شروع init مجموعه‌ای از بررسی‌های پیش از اجرا (preflight checks) را انجام می‌دهد تا پیش‌شرط‌ها را تأیید کند و از مشکلات رایج در راه‌اندازی کلاستر جلوگیری شود. کاربر می‌تواند با گزینه `--ignore-preflight-errors` برخی از این بررسی‌ها یا همه آن‌ها را نادیده بگیرد.

- [هشدار] اگر نسخه کوبرنتیز موردنظر (که با پرچم `--kubernetes-version` مشخص می‌شود) دست‌کم یک نسخه فرعی بالاتر از نسخه CLI مربوط به kubeadm باشد.
- الزامات سیستمی کوبرنتیز:
  - در صورت اجرا روی لینوکس:
    - [خطا] اگر نسخه هسته قدیمی‌تر از حداقل نسخه لازم باشد
    - [خطا] اگر زیرسیستم‌های لازم cgroups تنظیم نشده باشند
- [خطا] اگر نقطه پایانی CRI پاسخ ندهد
- [خطا] اگر کاربر root نباشد
- [خطا] اگر نام میزبان ماشین یک زیردامنه DNS معتبر نباشد
- [هشدار] اگر نام میزبان از طریق جست‌وجوی شبکه در دسترس نباشد
- [خطا] اگر نسخه kubelet پایین‌تر از حداقل نسخه kubelet پشتیبانی‌شده در kubeadm (نسخه فرعی فعلی منهای یک) باشد
- [خطا] اگر نسخه kubelet دست‌کم یک نسخه فرعی بالاتر از نسخه لازم control plane باشد (اختلاف نسخه پشتیبانی‌نشده)
- [هشدار] اگر سرویس kubelet وجود نداشته باشد یا غیرفعال باشد
- [هشدار] اگر firewalld فعال باشد
- [خطا] اگر bindPort سرور API یا پورت‌های 10250/10251/10252 در حال استفاده باشند
- [خطا] اگر پوشه `/etc/kubernetes/manifest` از قبل وجود داشته باشد و خالی نباشد
- [خطا] اگر swap روشن باشد
- [خطا] اگر دستورهای `ip`، `iptables`، `mount` و `nsenter` در مسیر دستورها وجود نداشته باشند
- [هشدار] اگر دستورهای `ethtool`، `tc` و `touch` در مسیر دستورها وجود نداشته باشند
- [هشدار] اگر پرچم‌های آرگومان اضافی سرور API، controller manager یا زمان‌بند شامل گزینه‌های نامعتبر باشند
- [هشدار] اگر اتصال به https://API.AdvertiseAddress:API.BindPort از پراکسی بگذرد
- [هشدار] اگر اتصال به زیرشبکه سرویس‌ها از پراکسی بگذرد (فقط نخستین نشانی بررسی می‌شود)
- [هشدار] اگر اتصال به زیرشبکه Podها از پراکسی بگذرد (فقط نخستین نشانی بررسی می‌شود)
- اگر etcd خارجی ارائه شده باشد:
  - [خطا] اگر نسخه etcd قدیمی‌تر از حداقل نسخه لازم باشد
  - [خطا] اگر گواهی‌ها یا کلیدهای etcd مشخص شده اما ارائه نشده باشند
- اگر etcd خارجی ارائه _نشده_ باشد (و در نتیجه etcd محلی نصب شود):
  - [خطا] اگر پورت 2379 در حال استفاده باشد
  - [خطا] اگر پوشه Etcd.DataDir از قبل وجود داشته باشد و خالی نباشد
- اگر حالت مجوزدهی ABAC باشد:
  - [خطا] اگر فایل abac_policy.json وجود نداشته باشد
- اگر حالت مجوزدهی WebHook باشد:
  - [خطا] اگر فایل webhook_authz.conf وجود نداشته باشد

{{< note >}}
بررسی‌های پیش از اجرا را می‌توان به‌صورت جداگانه با دستور [`kubeadm init phase preflight`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-preflight) اجرا کرد.
{{< /note >}}

### تولید گواهی‌های لازم

ابزار kubeadm جفت‌های گواهی و کلید خصوصی را برای اهداف مختلف تولید می‌کند:

- یک مرجع صدور گواهی خودامضا برای کلاستر کوبرنتیز که در فایل `ca.crt` و فایل کلید خصوصی `ca.key` ذخیره می‌شود

- یک گواهی سرویس‌دهی برای سرور API که با استفاده از `ca.crt` به‌عنوان CA تولید می‌شود و همراه با کلید خصوصی `apiserver.key` در فایل `apiserver.crt` ذخیره می‌شود. این گواهی باید نام‌های جایگزین زیر را داشته باشد:

  - نشانی clusterIP داخلی سرویس Kubernetes (نخستین نشانی در CIDR سرویس‌ها؛ برای نمونه `10.96.0.1` اگر زیرشبکه سرویس `10.96.0.0/12` باشد)
  - نام‌های DNS کوبرنتیز؛ برای نمونه `kubernetes.default.svc.cluster.local` اگر مقدار پرچم `--service-dns-domain` برابر با `cluster.local` باشد، به‌علاوه نام‌های DNS پیش‌فرض `kubernetes.default.svc`، `kubernetes.default` و `kubernetes`
  - نام نود
  - مقدار `--apiserver-advertise-address`
  - نام‌های جایگزین اضافی که کاربر مشخص کرده است

- یک گواهی کلاینت برای اتصال امن سرور API به kubeletها که با استفاده از `ca.crt` به‌عنوان CA تولید می‌شود و همراه با کلید خصوصی `apiserver-kubelet-client.key` در فایل `apiserver-kubelet-client.crt` ذخیره می‌شود.

- یک کلید خصوصی برای امضای توکن‌های ServiceAccount که در فایل `sa.key` و همراه با کلید عمومی `sa.pub` ذخیره می‌شود

- یک مرجع صدور گواهی برای پراکسی جلویی که همراه با کلید `front-proxy-ca.key` در فایل `front-proxy-ca.crt` ذخیره می‌شود

- یک گواهی کلاینت برای کلاینت پراکسی جلویی که با استفاده از `front-proxy-ca.crt` به‌عنوان CA تولید می‌شود و همراه با کلید خصوصی `front-proxy-client.key` در فایل `front-proxy-client.crt` ذخیره می‌شود

گواهی‌ها به‌طور پیش‌فرض در `/etc/kubernetes/pki` ذخیره می‌شوند، اما می‌توان این دایرکتوری را با پرچم `--cert-dir` تغییر داد.

به نکات زیر توجه کنید:

1. اگر جفت گواهی و کلید خصوصی موردنظر هر دو وجود داشته باشند و محتوای آن‌ها با مشخصات بالا سازگار تشخیص داده شود، از فایل‌های موجود استفاده می‌شود و مرحله تولید آن گواهی نادیده گرفته می‌شود. بنابراین کاربر می‌تواند، برای نمونه، یک CA موجود را در `/etc/kubernetes/pki/ca.{crt,key}` کپی کند تا kubeadm از همان فایل‌ها برای امضای بقیه گواهی‌ها استفاده کند. همچنین [استفاده از گواهی‌های سفارشی](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#custom-certificates) را ببینید.
1. برای CA می‌توان فایل `ca.crt` را بدون فایل `ca.key` ارائه کرد. اگر همه گواهی‌ها و فایل‌های kubeconfig دیگر از قبل موجود باشند، kubeadm این وضعیت را تشخیص می‌دهد و ExternalCA را فعال می‌کند. در این حالت کنترل‌کننده `csrsigner` در controller-manager نیز راه‌اندازی نخواهد شد.
1. اگر kubeadm در [حالت CA خارجی](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#external-ca-mode) اجرا شود، کاربر باید همه گواهی‌ها را ارائه کند، زیرا kubeadm نمی‌تواند آن‌ها را خودش تولید کند.
1. اگر kubeadm در حالت `--dry-run` اجرا شود، فایل‌های گواهی در یک پوشه موقت نوشته می‌شوند.
1. تولید گواهی‌ها را می‌توان به‌صورت جداگانه با دستور [`kubeadm init phase certs all`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-certs) اجرا کرد.

### تولید فایل‌های kubeconfig برای مؤلفه‌های control plane

ابزار kubeadm فایل‌های kubeconfig حاوی هویت مؤلفه‌های control plane را تولید می‌کند:

- یک فایل kubeconfig برای استفاده kubelet در زمان راه‌اندازی اولیه TLS، با مسیر `/etc/kubernetes/bootstrap-kubelet.conf`. این فایل شامل یک bootstrap-token یا گواهی‌های کلاینت جاسازی‌شده برای احراز هویت این نود در کلاستر است.

  این گواهی کلاینت باید:

  - طبق الزام ماژول [مجوزدهی نود](/docs/reference/access-authn-authz/node/) در سازمان `system:nodes` باشد.
  - نام مشترک (CN) آن `system:node:<hostname-lowercased>` باشد.

- یک فایل kubeconfig برای controller-manager با مسیر `/etc/kubernetes/controller-manager.conf`. در این فایل یک گواهی کلاینت با هویت controller-manager جاسازی شده است. مقدار CN این گواهی باید `system:kube-controller-manager` باشد، همان‌طور که به‌طور پیش‌فرض در [نقش‌های RBAC مؤلفه‌های اصلی](/docs/reference/access-authn-authz/rbac/#core-component-roles) تعریف شده است.

- یک فایل kubeconfig برای زمان‌بند با مسیر `/etc/kubernetes/scheduler.conf`. در این فایل یک گواهی کلاینت با هویت زمان‌بند جاسازی شده است. مقدار CN این گواهی باید `system:kube-scheduler` باشد، همان‌طور که به‌طور پیش‌فرض در [نقش‌های RBAC مؤلفه‌های اصلی](/docs/reference/access-authn-authz/rbac/#core-component-roles) تعریف شده است.

افزون بر این، یک فایل kubeconfig برای kubeadm به‌عنوان موجودیت مدیریتی تولید و در `/etc/kubernetes/admin.conf` ذخیره می‌شود. این فایل گواهی‌ای با `Subject: O = kubeadm:cluster-admins, CN = kubernetes-admin` دارد. گروه `kubeadm:cluster-admins` را kubeadm مدیریت می‌کند. این گروه در طول `kubeadm init` و با استفاده از فایل `super-admin.conf`، که به RBAC نیاز ندارد، به ClusterRole با نام `cluster-admin` متصل می‌شود. فایل `admin.conf` باید روی نودهای control plane بماند و نباید با کاربران دیگر به اشتراک گذاشته شود.

در طول `kubeadm init` یک فایل kubeconfig دیگر نیز تولید و در `/etc/kubernetes/super-admin.conf` ذخیره می‌شود. این فایل گواهی‌ای با `Subject: O = system:masters, CN = kubernetes-super-admin` دارد. گروه `system:masters` یک گروه ابرکاربر است که RBAC را دور می‌زند و به همین دلیل، فایل `super-admin.conf` در شرایط اضطراری که کلاستر بر اثر پیکربندی نادرست RBAC قفل شده باشد کاربرد دارد. فایل `super-admin.conf` باید در مکانی امن نگهداری شود و نباید با کاربران دیگر به اشتراک گذاشته شود.

برای اطلاعات بیشتر درباره RBAC و ClusterRoleها و گروه‌های داخلی، [اتصال نقش‌های کاربرمحور RBAC](/docs/reference/access-authn-authz/rbac/#user-facing-roles) را ببینید.

برای تولید فایل‌های kubeconfig برای کاربران دیگر می‌توانید دستور [`kubeadm kubeconfig user`](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/#cmd-kubeconfig-user) را اجرا کنید.

{{< caution >}}
فایل‌های پیکربندی تولیدشده شامل یک کلید احراز هویت جاسازی‌شده هستند و باید با آن‌ها مانند اطلاعات محرمانه رفتار کنید.
{{< /caution >}}

همچنین به نکات زیر توجه کنید:

1. گواهی `ca.crt` در همه فایل‌های kubeconfig جاسازی شده است.
1. اگر فایل kubeconfig موردنظر وجود داشته باشد و محتوای آن با مشخصات بالا سازگار تشخیص داده شود، از فایل موجود استفاده می‌شود و مرحله تولید آن kubeconfig نادیده گرفته می‌شود.
1. اگر kubeadm در [حالت ExternalCA](/docs/reference/setup-tools/kubeadm/kubeadm-init/#external-ca-mode) اجرا شود، کاربر باید همه فایل‌های kubeconfig لازم را نیز ارائه کند، زیرا kubeadm نمی‌تواند هیچ‌یک از آن‌ها را خودش تولید کند.
1. اگر kubeadm در حالت `--dry-run` اجرا شود، فایل‌های kubeconfig در یک پوشه موقت نوشته می‌شوند.
1. تولید فایل‌های kubeconfig را می‌توان به‌صورت جداگانه با دستور [`kubeadm init phase kubeconfig all`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-kubeconfig) اجرا کرد.

### تولید مانیفست‌های Pod ایستا برای مؤلفه‌های control plane

ابزار kubeadm فایل‌های مانیفست Pod ایستا را برای مؤلفه‌های control plane در مسیر `/etc/kubernetes/manifests` می‌نویسد. kubelet این پوشه را زیر نظر دارد تا Podهای موجود در آن را هنگام راه‌اندازی ایجاد کند.

مانیفست‌های Pod ایستا مجموعه‌ای از ویژگی‌های مشترک دارند:

- همهٔ Podهای ایستا در فضای نام (namespace) `kube-system` مستقر می‌شوند.
- همهٔ Podهای ایستا برچسب‌های `tier:control-plane` و `component:{component-name}` را می‌گیرند.
- همهٔ Podهای ایستا از کلاس اولویت `system-node-critical` استفاده می‌کنند.
- در همهٔ Podهای ایستا مقدار `hostNetwork: true` تنظیم می‌شود تا control plane بتواند پیش از پیکربندی شبکه راه‌اندازی شود؛ در نتیجه:

  * مقدار `address` که controller-manager و زمان‌بند برای ارجاع به سرور API از آن استفاده می‌کنند، `127.0.0.1` است.
  * اگر سرور etcd به‌صورت محلی راه‌اندازی شده باشد، نشانی `etcd-server` روی `127.0.0.1:2379` تنظیم می‌شود.

- انتخاب رهبر (leader election) هم برای controller-manager و هم برای زمان‌بند فعال است.
- هر یک از controller-manager و زمان‌بند به فایل kubeconfig مخصوص خود با هویتی یکتا ارجاع می‌دهند.
- همهٔ Podهای ایستا فلگ‌ها یا وصله‌های اضافی‌ای را که مشخص می‌کنید دریافت می‌کنند؛ این موضوع در [ارسال آرگومان‌های سفارشی به مؤلفه‌های control plane](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/) شرح داده شده است.
- همهٔ Podهای ایستا حجم‌های (volume) اضافی‌ای را که کاربر مشخص کرده است (از نوع Host path) دریافت می‌کنند.

توجه کنید که:

1. همهٔ ایمیج‌ها به‌طور پیش‌فرض از registry.k8s.io دریافت می‌شوند. برای سفارشی‌سازی مخزن ایمیج، به [استفاده از ایمیج‌های سفارشی](/docs/reference/setup-tools/kubeadm/kubeadm-init/#custom-images) مراجعه کنید.
1. اگر kubeadm در حالت `--dry-run` اجرا شود، فایل‌های Pod ایستا در یک پوشهٔ موقت نوشته می‌شوند.
1. تولید مانیفست Pod ایستا برای مؤلفه‌های control plane را می‌توان به‌تنهایی و با دستور [`kubeadm init phase control-plane all`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-control-plane) اجرا کرد.

#### سرور API

پارامترهای زیر که کاربران ارائه می‌کنند، بر مانیفست Pod ایستای سرور API اثر می‌گذارند:

- مقادیر `apiserver-advertise-address` و `apiserver-bind-port` برای اتصال سرور؛ اگر این مقادیر ارائه نشوند، به‌طور پیش‌فرض نشانی IP رابط شبکهٔ پیش‌فرض ماشین و پورت 6443 استفاده می‌شود.
- مقدار `service-cluster-ip-range` برای استفاده در Serviceها.
- اگر سرور etcd خارجی مشخص شده باشد، نشانی `etcd-servers` و تنظیمات TLS مربوط به آن (`etcd-cafile`، `etcd-certfile`، `etcd-keyfile`)؛ اگر سرور etcd خارجی ارائه نشود، از یک etcd محلی (از طریق شبکهٔ میزبان) استفاده می‌شود.
- اگر ارائه‌دهندهٔ ابری مشخص شده باشد، پارامتر `--cloud-provider` متناظر با آن پیکربندی می‌شود و در صورت وجود فایل پیکربندی، مسیر `--cloud-config` نیز تنظیم می‌شود (این قابلیت آزمایشی و در مرحلهٔ آلفا است و در نسخه‌ای در آینده حذف خواهد شد).

سایر فلگ‌های سرور API که بدون هیچ شرطی تنظیم می‌شوند عبارت‌اند از:

- فلگ `--insecure-port=0` برای جلوگیری از اتصال‌های ناامن به سرور API.
- فلگ `--enable-bootstrap-token-auth=true` برای فعال‌سازی ماژول احراز هویت `BootstrapTokenAuthenticator`. برای جزئیات بیشتر به [راه‌اندازی اولیهٔ TLS](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) مراجعه کنید.
- فلگ `--allow-privileged` با مقدار `true` (که برای نمونه kube proxy به آن نیاز دارد).
- فلگ `--requestheader-client-ca-file` با مقدار `front-proxy-ca.crt`.
- فلگ `--enable-admission-plugins` با این مقادیر:

  - افزونهٔ [`NamespaceLifecycle`](/docs/reference/access-authn-authz/admission-controllers/#namespacelifecycle)، برای مثال برای جلوگیری از حذف فضاهای نام رزروشدهٔ سیستم.
  - افزونه‌های [`LimitRanger`](/docs/reference/access-authn-authz/admission-controllers/#limitranger) و [`ResourceQuota`](/docs/reference/access-authn-authz/admission-controllers/#resourcequota) برای اعمال محدودیت‌ها بر فضاهای نام.
  - افزونهٔ [`ServiceAccount`](/docs/reference/access-authn-authz/admission-controllers/#serviceaccount) برای اعمال خودکارسازی حساب‌های سرویس.
  - افزونهٔ [`PersistentVolumeLabel`](/docs/reference/access-authn-authz/admission-controllers/#persistentvolumelabel) که برچسب‌های منطقه یا ناحیه را، مطابق تعریف ارائه‌دهندهٔ ابری، به PersistentVolumeها می‌افزاید (این کنترل‌کنندهٔ پذیرش منسوخ شده است و در نسخه‌ای در آینده حذف خواهد شد. از نسخهٔ v1.9 به بعد، اگر کاربر صراحتاً `gce` یا `aws` را به‌عنوان ارائه‌دهندهٔ ابری انتخاب نکند، kubeadm آن را به‌طور پیش‌فرض مستقر نمی‌کند).
  - افزونهٔ [`DefaultStorageClass`](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass) برای اعمال کلاس ذخیره‌سازی پیش‌فرض بر آبجکت‌های `PersistentVolumeClaim`.
  - افزونهٔ [`DefaultTolerationSeconds`](/docs/reference/access-authn-authz/admission-controllers/#defaulttolerationseconds).
  - افزونهٔ [`NodeRestriction`](/docs/reference/access-authn-authz/admission-controllers/#noderestriction) برای محدود کردن مواردی که kubelet می‌تواند تغییر دهد (برای مثال فقط Podهای همان نود).

- فلگ `--kubelet-preferred-address-types` با مقدار `InternalIP,ExternalIP,Hostname;`؛ با این تنظیم، دستور `kubectl logs` و سایر ارتباط‌های سرور API با kubelet در محیط‌هایی که نام میزبان نودها قابل تبدیل به نشانی نیست نیز کار می‌کنند.

- فلگ‌های مربوط به استفاده از گواهی‌های تولیدشده در مراحل قبل:

  - فلگ `--client-ca-file` با مقدار `ca.crt`
  - فلگ `--tls-cert-file` با مقدار `apiserver.crt`
  - فلگ `--tls-private-key-file` با مقدار `apiserver.key`
  - فلگ `--kubelet-client-certificate` با مقدار `apiserver-kubelet-client.crt`
  - فلگ `--kubelet-client-key` با مقدار `apiserver-kubelet-client.key`
  - فلگ `--service-account-key-file` با مقدار `sa.pub`
  - فلگ `--requestheader-client-ca-file` با مقدار `front-proxy-ca.crt`
  - فلگ `--proxy-client-cert-file` با مقدار `front-proxy-client.crt`
  - فلگ `--proxy-client-key-file` با مقدار `front-proxy-client.key`

- سایر فلگ‌ها برای ایمن‌سازی ارتباط‌های پراکسی جلویی ([تجمیع API](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)):

  - `--requestheader-username-headers=X-Remote-User`
  - `--requestheader-group-headers=X-Remote-Group`
  - `--requestheader-extra-headers-prefix=X-Remote-Extra-`
  - `--requestheader-allowed-names=front-proxy-client`

#### مدیر کنترل‌کننده‌ها

پارامترهای زیر که کاربران ارائه می‌کنند، بر مانیفست Pod ایستای مدیر کنترل‌کننده‌ها اثر می‌گذارند:

- اگر kubeadm با مشخص کردن `--pod-network-cidr` اجرا شود، قابلیت مدیریت زیرشبکه که برخی افزونه‌های شبکهٔ CNI به آن نیاز دارند، با تنظیم موارد زیر فعال می‌شود:

  - `--allocate-node-cidrs=true`
  - فلگ‌های `--cluster-cidr` و `--node-cidr-mask-size` مطابق با CIDR داده‌شده

سایر فلگ‌هایی که بدون هیچ شرطی تنظیم می‌شوند عبارت‌اند از:

- فلگ `--controllers` که همهٔ کنترل‌کننده‌های پیش‌فرض و نیز کنترل‌کننده‌های `BootstrapSigner` و `TokenCleaner` را برای راه‌اندازی اولیهٔ TLS فعال می‌کند. برای جزئیات بیشتر به [راه‌اندازی اولیهٔ TLS](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) مراجعه کنید.

- فلگ `--use-service-account-credentials` با مقدار `true`.

- فلگ‌های مربوط به استفاده از گواهی‌های تولیدشده در مراحل قبل:

  - فلگ `--root-ca-file` با مقدار `ca.crt`
  - فلگ `--cluster-signing-cert-file` با مقدار `ca.crt` اگر حالت CA خارجی غیرفعال باشد، و در غیر این صورت با مقدار `""`
  - فلگ `--cluster-signing-key-file` با مقدار `ca.key` اگر حالت CA خارجی غیرفعال باشد، و در غیر این صورت با مقدار `""`
  - فلگ `--service-account-private-key-file` با مقدار `sa.key`

#### زمان‌بند

پارامترهایی که کاربر ارائه می‌کند، بر مانیفست Pod ایستای زمان‌بند اثری ندارند.

### تولید مانیفست Pod ایستا برای etcd محلی

اگر etcd خارجی مشخص کرده باشید، این مرحله نادیده گرفته می‌شود؛ در غیر این صورت، kubeadm یک فایل مانیفست Pod ایستا تولید می‌کند تا نمونه‌ای محلی از etcd را در یک Pod با ویژگی‌های زیر ایجاد کند:

- روی `localhost:2379` گوش می‌دهد و از `HostNetwork=true` استفاده می‌کند.
- یک اتصال `hostPath` از `dataDir` به سیستم فایل میزبان ایجاد می‌کند.
- همهٔ فلگ‌های اضافی مشخص‌شده توسط کاربر را به کار می‌گیرد.

توجه کنید که:

1. ایمیج کانتینر etcd به‌طور پیش‌فرض از `registry.gcr.io` دریافت می‌شود. برای سفارشی‌سازی مخزن ایمیج، به [استفاده از ایمیج‌های سفارشی](/docs/reference/setup-tools/kubeadm/kubeadm-init/#custom-images) مراجعه کنید.
1. اگر kubeadm را در حالت `--dry-run` اجرا کنید، مانیفست Pod ایستای etcd در یک پوشهٔ موقت نوشته می‌شود.
1. می‌توانید تولید مانیفست Pod ایستا برای etcd محلی را مستقیماً با دستور [`kubeadm init phase etcd local`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-etcd) اجرا کنید.

### انتظار برای بالا آمدن control plane

در نودهای control plane، ابزار kubeadm حداکثر ۴ دقیقه منتظر می‌ماند تا مؤلفه‌های control plane و kubelet در دسترس قرار گیرند. این کار با بررسی سلامت از طریق نقطه‌های پایانی `/healthz` یا `/livez` هر مؤلفه انجام می‌شود.

پس از بالا آمدن control plane، ابزار kubeadm کارهای شرح‌داده‌شده در بندهای بعدی را انجام می‌دهد.

### ذخیرهٔ ClusterConfiguration ابزار kubeadm در یک ConfigMap برای مراجعات بعدی

ابزار kubeadm پیکربندی ارسال‌شده به `kubeadm init` را در یک ConfigMap با نام `kubeadm-config` در فضای نام `kube-system` ذخیره می‌کند.

به این ترتیب، عملیات‌هایی که kubeadm در آینده اجرا می‌کند (مانند `kubeadm upgrade`) می‌توانند وضعیت واقعی و فعلی کلاستر را تعیین کنند و بر پایهٔ این داده‌ها تصمیم‌های جدید بگیرند.

توجه کنید که:

1. پیش از ذخیرهٔ ClusterConfiguration، اطلاعات حساس مانند توکن از پیکربندی حذف می‌شوند.
1. بارگذاری پیکربندی نود control plane را می‌توان به‌تنهایی و با دستور [`kubeadm init phase upload-config`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-upload-config) اجرا کرد.

### علامت‌گذاری نود به‌عنوان control-plane

به‌محض در دسترس قرار گرفتن control plane، ابزار kubeadm اقدامات زیر را انجام می‌دهد:

- با برچسب `node-role.kubernetes.io/control-plane=""` نود را به‌عنوان control-plane مشخص می‌کند.
- لکهٔ (taint) `node-role.kubernetes.io/control-plane:NoSchedule` را روی نود اعمال می‌کند.

توجه کنید که فاز علامت‌گذاری control-plane را می‌توان به‌تنهایی و با دستور [`kubeadm init phase mark-control-plane`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-mark-control-plane) اجرا کرد.


### پیکربندی راه‌اندازی اولیهٔ TLS برای پیوستن نودها

ابزار kubeadm برای پیوستن نودهای جدید به کلاستر موجود از [احراز هویت با توکن‌های راه‌اندازی اولیه](/docs/reference/access-authn-authz/bootstrap-tokens/) استفاده می‌کند؛ برای جزئیات بیشتر، [پیشنهاد طراحی](https://git.k8s.io/design-proposals-archive/cluster-lifecycle/bootstrap-discovery.md) را نیز ببینید.

دستور `kubeadm init` اطمینان حاصل می‌کند که همه‌چیز برای این فرایند به‌درستی پیکربندی شده باشد. این کار شامل مراحل زیر و نیز تنظیم فلگ‌های سرور API و کنترل‌کننده است که در بندهای پیشین شرح داده شدند.

{{< note >}}
راه‌اندازی اولیهٔ TLS برای نودها را می‌توان با دستور [`kubeadm init phase bootstrap-token`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-bootstrap-token) پیکربندی کرد؛ این دستور همهٔ مراحل پیکربندی شرح‌داده‌شده در بندهای بعدی را اجرا می‌کند. همچنین می‌توان هر مرحله را به‌تنهایی اجرا کرد.
{{< /note >}}

#### ایجاد توکن راه‌اندازی اولیه

دستور `kubeadm init` نخستین توکن راه‌اندازی اولیه را ایجاد می‌کند؛ این توکن یا به‌طور خودکار تولید می‌شود یا کاربر آن را با فلگ `--token` ارائه می‌کند. مطابق مشخصات توکن راه‌اندازی اولیه، توکن باید به‌صورت یک Secret با نام `bootstrap-token-<token-id>` در فضای نام `kube-system` ذخیره شود.

توجه کنید که:

1. توکن پیش‌فرضی که `kubeadm init` ایجاد می‌کند، برای اعتبارسنجی کاربران موقت در فرایند راه‌اندازی اولیهٔ TLS استفاده می‌شود؛ این کاربران عضو گروه `system:bootstrappers:kubeadm:default-node-token` خواهند بود.
1. اعتبار توکن محدود است و به‌طور پیش‌فرض ۲۴ ساعت طول می‌کشد (این بازه را می‌توان با فلگ `—token-ttl` تغییر داد).
1. توکن‌های بیشتر را می‌توان با دستور [`kubeadm token`](/docs/reference/setup-tools/kubeadm/kubeadm-token/) ایجاد کرد؛ این دستور قابلیت‌های مفید دیگری نیز برای مدیریت توکن‌ها فراهم می‌کند.

#### اجازهٔ فراخوانی CSR API به نودهای در حال پیوستن

ابزار kubeadm اطمینان حاصل می‌کند که کاربران گروه `system:bootstrappers:kubeadm:default-node-token` بتوانند به API امضای گواهی دسترسی داشته باشند.

این کار با ایجاد یک ClusterRoleBinding با نام `kubeadm:kubelet-bootstrap` میان گروه بالا و نقش پیش‌فرض RBAC با نام `system:node-bootstrapper` انجام می‌شود.

#### راه‌اندازی تأیید خودکار برای توکن‌های راه‌اندازی اولیهٔ جدید

ابزار kubeadm اطمینان حاصل می‌کند که کنترل‌کنندهٔ csrapprover درخواست CSR مربوط به توکن راه‌اندازی اولیه را به‌طور خودکار تأیید کند.

این کار با ایجاد یک ClusterRoleBinding با نام `kubeadm:node-autoapprove-bootstrap` میان گروه `system:bootstrappers:kubeadm:default-node-token` و نقش پیش‌فرض `system:certificates.k8s.io:certificatesigningrequests:nodeclient` انجام می‌شود.

نقش `system:certificates.k8s.io:certificatesigningrequests:nodeclient` نیز باید ایجاد شود و مجوز POST را روی `/apis/certificates.k8s.io/certificatesigningrequests/nodeclient` اعطا کند.

#### راه‌اندازی چرخش گواهی نودها با تأیید خودکار

ابزار kubeadm اطمینان حاصل می‌کند که چرخش گواهی برای نودها فعال باشد و کنترل‌کنندهٔ csrapprover درخواست CSR مربوط به گواهی جدید نودها را به‌طور خودکار تأیید کند.

این کار با ایجاد یک ClusterRoleBinding با نام `kubeadm:node-autoapprove-certificate-rotation` میان گروه `system:nodes` و نقش پیش‌فرض `system:certificates.k8s.io:certificatesigningrequests:selfnodeclient` انجام می‌شود.

#### اجازهٔ دسترسی سرور API به API کوبلت

ابزار kubeadm اطمینان حاصل می‌کند که سرور API بتواند با گواهی کلاینت خود، `apiserver-kubelet-client.crt`، به API کوبلت دسترسی داشته باشد.

این کار با ایجاد یک ClusterRoleBinding با نام `kubeadm:apiserver-kubelet-client` میان کاربر `kube-apiserver-kubelet-client` و نقش پیش‌فرض RBAC با نام `system:kubelet-api-admin` انجام می‌شود.

#### ایجاد ConfigMap عمومی cluster-info

این فاز، ConfigMap با نام `cluster-info` را در فضای نام `kube-public` ایجاد می‌کند.

افزون بر این، یک Role و یک RoleBinding ایجاد می‌کند که دسترسی به این ConfigMap را به کاربران احراز هویت‌نشده (یعنی کاربران گروه RBAC با نام `system:unauthenticated`) می‌دهند.

{{< note >}}
دسترسی به ConfigMap با نام `cluster-info` محدودیت نرخ _ندارد_. اگر سرور API کلاستر خود را در معرض اینترنت قرار دهید، این موضوع ممکن است مشکل‌ساز باشد یا نباشد؛ بدترین سناریو در این حالت، حملهٔ منع سرویس (DoS) است که در آن مهاجم تمام درخواست‌های همزمانی را که kube-apiserver می‌تواند پردازش کند، صرف دریافت ConfigMap `cluster-info` می‌کند.
{{< /note >}}

### نصب افزونه‌ها

ابزار kubeadm سرور DNS داخلی و مؤلفه‌های افزونهٔ kube-proxy را از طریق سرور API نصب می‌کند.

{{< note >}}
این فاز را می‌توان به‌تنهایی و با دستور [`kubeadm init phase addon all`](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/#cmd-phase-addon) اجرا کرد.
{{< /note >}}

#### پراکسی

یک ServiceAccount برای `kube-proxy` در فضای نام `kube-system` ایجاد می‌شود؛ سپس kube-proxy به‌صورت یک DaemonSet مستقر می‌شود:

- اعتبارنامه‌های دسترسی به control plane (`ca.crt` و `token`) از ServiceAccount تأمین می‌شوند.
- مکان (URL) سرور API از یک ConfigMap به دست می‌آید.
- حساب ServiceAccount با نام `kube-proxy` به امتیازهای ClusterRole با نام `system:node-proxier` متصل می‌شود.

#### سرویس DNS

- سرویس CoreDNS برای سازگاری با افزونهٔ قدیمی `kube-dns`، نام `kube-dns` را دارد.

- یک ServiceAccount برای CoreDNS در فضای نام `kube-system` ایجاد می‌شود.

- حساب ServiceAccount با نام `coredns` به امتیازهای ClusterRole با نام `system:coredns` متصل می‌شود.

## طراحی داخلی فازهای kubeadm join

گردش کار داخلی `kubeadm join` نیز مانند `kubeadm init` از دنباله‌ای از کارهای اتمی تشکیل شده است.

این فرایند به دو بخش تقسیم می‌شود: کشف (که در آن نود به سرور API کوبرنتیز اعتماد می‌کند) و راه‌اندازی اولیهٔ TLS (که در آن سرور API کوبرنتیز به نود اعتماد می‌کند).

به [احراز هویت با توکن‌های راه‌اندازی اولیه](/docs/reference/access-authn-authz/bootstrap-tokens/) یا [پیشنهاد طراحی](https://git.k8s.io/design-proposals-archive/cluster-lifecycle/bootstrap-discovery.md) مربوط به آن مراجعه کنید.

### بررسی‌های پیش از اجرا

ابزار `kubeadm` پیش از آغاز عملیات پیوستن، مجموعه‌ای از بررسی‌های پیش از اجرا را انجام می‌دهد تا پیش‌شرط‌ها را تأیید کند و از مشکلات رایج هنگام راه‌اندازی کلاستر جلوگیری شود.

همچنین توجه کنید که:

1. بررسی‌های پیش از اجرای `kubeadm join` در اصل زیرمجموعه‌ای از بررسی‌های پیش از اجرای `kubeadm init` هستند.
1. اگر نود Windows را به کلاستر می‌پیوندانید، کنترل‌های مخصوص Linux نادیده گرفته می‌شوند.
1. در هر صورت، کاربر می‌تواند با گزینهٔ `--ignore-preflight-errors` بررسی‌های مشخصی از پیش از اجرا (یا در صورت لزوم همهٔ آن‌ها) را نادیده بگیرد.

### کشف cluster-info

برای کشف (discovery) دو روش اصلی وجود دارد. روش نخست، استفاده از یک توکن مشترک همراه با نشانی IP سرور API است. در روش دوم، فایلی ارائه می‌شود که زیرمجموعه‌ای از فایل استاندارد kubeconfig است.

#### کشف با توکن مشترک

اگر `kubeadm join` با `--discovery-token` اجرا شود، کشف با توکن انجام می‌شود. در این حالت، نود اساساً گواهی‌های CA کلاستر را از ConfigMap با نام `cluster-info` در فضای نام (namespace) `kube-public` دریافت می‌کند.

برای جلوگیری از حملات «مرد میانی» (man in the middle)، چند گام برداشته می‌شود:

- نخست، گواهی CA از طریق یک اتصال ناامن دریافت می‌شود. این کار از آن رو ممکن است که `kubeadm init` به کاربران `system:unauthenticated` اجازهٔ دسترسی به `cluster-info` را داده است.

- سپس گواهی CA از گام‌های اعتبارسنجی زیر می‌گذرد:

  - اعتبارسنجی پایه: شناسهٔ توکن با یک امضای JWT سنجیده می‌شود.
  - اعتبارسنجی کلید عمومی: از مقدار ارائه‌شده در `--discovery-token-ca-cert-hash` استفاده می‌شود. این مقدار در خروجی `kubeadm init` در دسترس است و با ابزارهای استاندارد نیز می‌توان آن را محاسبه کرد (این هش، مطابق RFC7469، روی بایت‌های آبجکت Subject Public Key Info (SPKI) محاسبه می‌شود). برای مجاز کردن بیش از یک کلید عمومی، می‌توان `--discovery-token-ca-cert-hash flag` را چند بار تکرار کرد.
  - به‌عنوان اعتبارسنجی تکمیلی، گواهی CA از طریق یک اتصال امن دریافت و با CA دریافت‌شده در ابتدا مقایسه می‌شود.

{{< note >}}
با ارسال فلگ `--discovery-token-unsafe-skip-ca-verification` در خط فرمان می‌توانید از اعتبارسنجی CA صرف‌نظر کنید. این کار مدل امنیتی kubeadm را تضعیف می‌کند، زیرا دیگران ممکن است خود را به‌جای سرور API کوبرنتیز جا بزنند.
{{< /note >}}

#### کشف با فایل یا HTTPS

اگر `kubeadm join` با `--discovery-file` اجرا شود، کشف با فایل انجام می‌شود. این فایل می‌تواند محلی باشد یا از یک نشانی HTTPS بارگیری شود. در حالت HTTPS، برای تأیید اتصال از مجموعه گواهی‌های CA نصب‌شده روی میزبان استفاده می‌شود.

در کشف با فایل، گواهی CA کلاستر درون خود فایل قرار دارد. در واقع، فایل کشف یک فایل kubeconfig است که فقط ویژگی‌های `server` و `certificate-authority-data` در آن تنظیم شده‌اند؛ این موضوع در مستند مرجع [`kubeadm join`](/docs/reference/setup-tools/kubeadm/kubeadm-join/#file-or-https-based-discovery) شرح داده شده است. پس از برقراری اتصال با کلاستر، kubeadm تلاش می‌کند به ConfigMap با نام `cluster-info` دسترسی پیدا کند و در صورت موجود بودن، از آن استفاده می‌کند.

## راه‌اندازی اولیهٔ TLS

پس از مشخص شدن اطلاعات کلاستر، فایل `bootstrap-kubelet.conf` نوشته می‌شود تا kubelet بتواند راه‌اندازی اولیهٔ TLS (TLS Bootstrapping) را انجام دهد.

سازوکار راه‌اندازی اولیهٔ TLS از توکن مشترک برای احراز هویت موقت با سرور API کوبرنتیز استفاده می‌کند تا یک درخواست امضای گواهی (CSR) برای جفت‌کلیدی که به‌صورت محلی ساخته شده است ارسال کند.

سپس این درخواست به‌طور خودکار تأیید می‌شود و عملیات با ذخیرهٔ فایل‌های `ca.crt` و `kubelet.conf` پایان می‌یابد. kubelet از این فایل‌ها برای پیوستن به کلاستر استفاده می‌کند و فایل `bootstrap-kubelet.conf` حذف می‌شود.

{{< note >}}
- احراز هویت موقت با توکن ذخیره‌شده در فرایند `kubeadm init` (یا با توکن‌های دیگری که با دستور `kubeadm token` ساخته شده‌اند) اعتبارسنجی می‌شود.
- نتیجهٔ احراز هویت موقت، کاربری عضو گروه `system:bootstrappers:kubeadm:default-node-token` است که در فرایند `kubeadm init` به API مربوط به CSR دسترسی گرفته است.
- تأیید خودکار CSR را کنترل‌کنندهٔ csrapprover، مطابق پیکربندی موجود در فرایند `kubeadm init`، مدیریت می‌کند.
{{< /note >}}

## طراحی داخلی گردش کار kubeadm upgrade

دستور `kubeadm upgrade` زیردستورهایی برای مدیریت ارتقای کلاستر کوبرنتیز ساخته‌شده با kubeadm دارد. باید `kubeadm upgrade apply` را روی یک نود control plane اجرا کنید (انتخاب این نود با شماست)؛ این دستور فرایند ارتقا را آغاز می‌کند. سپس `kubeadm upgrade node` را روی همهٔ نودهای باقی‌مانده، اعم از نودهای کارگر و نودهای control plane، اجرا می‌کنید.

هر دو دستور `kubeadm upgrade apply` و `kubeadm upgrade node` زیردستوری به نام `phase` دارند که دسترسی به مراحل داخلی فرایند ارتقا را فراهم می‌کند. برای جزئیات بیشتر، [`kubeadm upgrade phase`](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase/) را ببینید.

دستورهای کمکی دیگر برای ارتقا، `kubeadm upgrade plan` و `kubeadm upgrade diff` هستند.

همهٔ زیردستورهای ارتقا از ارسال فایل پیکربندی پشتیبانی می‌کنند.

### دستور kubeadm upgrade plan

می‌توانید پیش از اجرای `kubeadm upgrade apply`، به‌صورت اختیاری `kubeadm upgrade plan` را اجرا کنید. زیردستور `plan` بررسی می‌کند که چه نسخه‌هایی برای ارتقا در دسترس هستند و آیا کلاستر فعلی شما قابل ارتقا است یا نه.

### دستور kubeadm upgrade diff

این دستور نشان می‌دهد چه تفاوت‌هایی روی مانیفست‌های موجود پادهای ایستا (static pod) در نودهای control plane اعمال خواهد شد. برای انجام همین کار با جزئیات بیشتر، می‌توانید `kubeadm upgrade apply --dry-run` یا `kubeadm upgrade node --dry-run` را اجرا کنید.

### دستور kubeadm upgrade apply

دستور `kubeadm upgrade apply` کلاستر را برای ارتقای همهٔ نودها آماده می‌کند و نود control plane‌ای را که روی آن اجرا شده است نیز ارتقا می‌دهد. این دستور گام‌های زیر را انجام می‌دهد:

- بررسی‌های پیش از اجرا را مشابه `kubeadm init` و `kubeadm join` انجام می‌دهد و از بارگیری ایمیج‌های کانتینر و مناسب بودن وضعیت کلاستر برای ارتقا اطمینان حاصل می‌کند.
- فایل‌های مانیفست control plane را روی دیسک در مسیر `/etc/kubernetes/manifests` ارتقا می‌دهد و اگر فایل‌ها تغییر کرده باشند، منتظر می‌ماند تا kubelet مؤلفه‌ها را دوباره راه‌اندازی کند.
- پیکربندی‌های به‌روزشدهٔ kubeadm و kubelet را در ConfigMapهای `kubeadm-config` و `kubelet-config` (هر دو در فضای نام `kube-system`) در کلاستر بارگذاری می‌کند.
- پیکربندی به‌روزشدهٔ kubelet را برای این نود در `/var/lib/kubelet/config.yaml` می‌نویسد، فایل `/var/lib/kubelet/instance-config.yaml` نود را می‌خواند و فیلدهایی مانند `containerRuntimeEndpoint` را از این پیکربندی نمونه در `/var/lib/kubelet/config.yaml` وصله (patch) می‌کند.
- توکن راه‌انداز (bootstrap token) و ConfigMap با نام `cluster-info` را برای قواعد RBAC پیکربندی می‌کند. این کار همانند مرحلهٔ `kubeadm init` است و تضمین می‌کند که کلاستر همچنان از پیوستن نودها با توکن‌های راه‌انداز پشتیبانی کند.
- افزونه‌های kube-proxy و CoreDNS را به‌صورت مشروط ارتقا می‌دهد؛ شرط این کار آن است که همهٔ kube-apiserverهای موجود در کلاستر پیش‌تر به نسخهٔ هدف ارتقا یافته باشند.
- کارهای پس از ارتقا، مانند پاک‌سازی قابلیت‌های منسوخ‌شدهٔ مختص هر انتشار، را انجام می‌دهد.

### دستور kubeadm upgrade node

دستور `kubeadm upgrade node` پس از آغاز ارتقای کلاستر (با اجرای `kubeadm upgrade apply`)، یک نود control plane یا نود کارگر را ارتقا می‌دهد. این دستور با بررسی وجود فایل `/etc/kubernetes/manifests/kube-apiserver.yaml` تشخیص می‌دهد که آیا نود از نوع control plane است یا نه. اگر ابزار kubeadm این فایل را پیدا کند، نتیجه می‌گیرد که یک Pod از kube-apiserver روی این نود در حال اجراست.

- بررسی‌های پیش از اجرا را مشابه `kubeadm upgrade apply` انجام می‌دهد.
- در نودهای control plane، فایل‌های مانیفست control plane را روی دیسک در مسیر `/etc/kubernetes/manifests` ارتقا می‌دهد و اگر فایل‌ها تغییر کرده باشند، منتظر می‌ماند تا kubelet مؤلفه‌ها را دوباره راه‌اندازی کند.
- پیکربندی به‌روزشدهٔ kubelet را برای این نود در `/var/lib/kubelet/config.yaml` می‌نویسد، فایل `/var/lib/kubelet/instance-config.yaml` نود را می‌خواند و فیلدهایی مانند `containerRuntimeEndpoint` را از این پیکربندی نمونه در `/var/lib/kubelet/config.yaml` وصله می‌کند.
- (در نودهای control plane) {{< glossary_tooltip text="افزونه‌های" term_id="addons" >}} kube-proxy و CoreDNS را به‌صورت مشروط ارتقا می‌دهد؛ شرط این کار آن است که همهٔ سرورهای API موجود در کلاستر پیش‌تر به نسخهٔ هدف ارتقا یافته باشند.
- کارهای پس از ارتقا، مانند پاک‌سازی قابلیت‌های منسوخ‌شدهٔ مختص هر انتشار، را انجام می‌دهد.

## طراحی داخلی گردش کار kubeadm reset

می‌توانید زیردستور `kubeadm reset` را روی نودی به کار ببرید که پیش‌تر دستورهای kubeadm روی آن اجرا شده‌اند. این زیردستور پاک‌سازی نود را به‌صورت **بهترین تلاش ممکن** انجام می‌دهد. اگر برخی از اقدامات ناموفق باشند، باید خودتان مداخله و پاک‌سازی را به‌صورت دستی انجام دهید.

این دستور از مراحل (phase) پشتیبانی می‌کند. برای جزئیات بیشتر، [`kubeadm reset phase`](/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase/) را ببینید.

این دستور از فایل پیکربندی پشتیبانی می‌کند.

علاوه بر این:
- قواعد IPVS، iptables و nftables پاک‌سازی **نمی‌شوند**.
- پیکربندی CNI (افزونهٔ شبکه) پاک‌سازی **نمی‌شود**.
- پوشهٔ `.kube/` در دایرکتوری خانگی کاربر پاک‌سازی **نمی‌شود**.

این دستور مراحل زیر را دارد:
- بررسی‌های پیش از اجرا را روی نود انجام می‌دهد تا سالم بودن آن را مشخص کند.
- در نودهای control plane، همهٔ داده‌های محلی عضو etcd را حذف می‌کند.
- سرویس kubelet را متوقف می‌کند.
- کانتینرهای در حال اجرا را متوقف می‌کند.
- همهٔ دایرکتوری‌های mount‌شده در `/var/lib/kubelet` را unmount می‌کند.
- همهٔ فایل‌ها و دایرکتوری‌هایی را که kubeadm در `/var/lib/kubelet` و `/etc/kubernetes` مدیریت می‌کند حذف می‌کند.
