---
reviewers:
- jpbetz
- cheftako
title: مهاجرت control plane تکثیرشده به استفاده از Cloud Controller Manager
linkTitle: "مهاجرت control plane تکثیرشده به استفاده از Cloud Controller Manager"
content_type: task
weight: 250
---

<!-- overview -->

{{< glossary_definition term_id="cloud-controller-manager" length="all" prepend="The cloud-controller-manager is">}}

## پیش‌زمینه

به‌عنوان بخشی از [تلاش برای جداسازی ارائه‌دهندگان ابری](/blog/2019/04/17/the-future-of-cloud-providers-in-kubernetes/)،
همهٔ کنترل‌کننده‌های مختص ابر باید از `kube-controller-manager` خارج شوند.
همهٔ کلاسترهای موجود که کنترل‌کننده‌های ابری را در `kube-controller-manager` اجرا می‌کنند،
باید مهاجرت کنند و این کنترل‌کننده‌ها را به‌جای آن در `cloud-controller-manager` مختص
ارائه‌دهندهٔ ابری اجرا کنند.

مهاجرت رهبر (Leader Migration) سازوکاری فراهم می‌کند که با آن، کلاسترهای با دسترس‌پذیری بالا (HA)
می‌توانند هنگام ارتقای control plane تکثیرشده، کنترل‌کننده‌های «مختص ابر» را به‌شکلی امن
میان `kube-controller-manager` و `cloud-controller-manager` جابه‌جا کنند. این کار از طریق یک
قفل منبع مشترک میان این دو مؤلفه انجام می‌شود. برای control plane تک‌نودی، یا اگر
در دسترس نبودن مدیران کنترل‌کننده در طول ارتقا قابل‌تحمل باشد، به مهاجرت رهبر نیازی نیست
و می‌توانید این راهنما را نادیده بگیرید.

برای فعال‌کردن مهاجرت رهبر، کافی است `--enable-leader-migration` را روی
`kube-controller-manager` یا `cloud-controller-manager` تنظیم کنید. مهاجرت رهبر فقط
در طول ارتقا کاربرد دارد و پس از پایان ارتقا می‌توان آن را با خیال راحت غیرفعال کرد
یا فعال نگه داشت.

این راهنما شما را گام‌به‌گام با فرایند دستی ارتقای control plane آشنا می‌کند؛ از حالتی که
`kube-controller-manager` با ارائه‌دهندهٔ ابری داخلی اجرا می‌شود، به حالتی که هر دو مؤلفهٔ
`kube-controller-manager` و `cloud-controller-manager` اجرا می‌شوند. اگر برای استقرار
و مدیریت کلاستر از ابزاری استفاده می‌کنید، برای دستورالعمل‌های مشخص مهاجرت به مستندات
آن ابزار و ارائه‌دهندهٔ ابری مراجعه کنید.

## {{% heading "prerequisites" %}}

فرض بر این است که control plane نسخهٔ N از کوبرنتیز را اجرا می‌کند و قرار است به
نسخهٔ N + 1 ارتقا یابد. با اینکه مهاجرت در همان نسخه نیز امکان‌پذیر است، بهتر است مهاجرت
به‌عنوان بخشی از یک ارتقا انجام شود تا تغییرات پیکربندی با هر انتشار هم‌راستا شوند.
نسخه‌های دقیق N و N + 1 به هر ارائه‌دهندهٔ ابری بستگی دارد. برای مثال، اگر یک ارائه‌دهندهٔ ابری
`cloud-controller-manager` را برای کار با کوبرنتیز 1.24 بسازد، N می‌تواند 1.23 و N + 1
می‌تواند 1.24 باشد.

نودهای control plane باید `kube-controller-manager` را با انتخاب رهبر (Leader Election)
فعال اجرا کنند که حالت پیش‌فرض است. در نسخهٔ N، ارائه‌دهندهٔ ابری داخلی (in-tree) باید
با فلگ `--cloud-provider` تنظیم شده باشد و `cloud-controller-manager` هنوز نباید
مستقر شده باشد.

ارائه‌دهندهٔ ابری خارجی (out-of-tree) باید `cloud-controller-manager` را همراه با
پیاده‌سازی مهاجرت رهبر ساخته باشد. اگر ارائه‌دهندهٔ ابری بسته‌های
`k8s.io/cloud-provider` و `k8s.io/controller-manager` را با نسخهٔ v0.21.0 یا بالاتر وارد
(import) کند، مهاجرت رهبر در دسترس خواهد بود. با این حال، در نسخه‌های پیش از v0.22.0،
مهاجرت رهبر در وضعیت آلفا است و لازم است feature gate `ControllerManagerLeaderMigration`
در `cloud-controller-manager` فعال شود.

این راهنما فرض می‌کند که kubelet هر نود control plane، مؤلفه‌های
`kube-controller-manager` و `cloud-controller-manager` را به‌صورت پادهای ایستا (static pod)
که با مانیفست‌هایشان تعریف شده‌اند، راه‌اندازی می‌کند. اگر این مؤلفه‌ها در محیط دیگری
اجرا می‌شوند، گام‌ها را متناسب با آن تنظیم کنید.

در زمینهٔ مجوزدهی، این راهنما فرض می‌کند که کلاستر از RBAC استفاده می‌کند. اگر حالت
مجوزدهی دیگری به مؤلفه‌های `kube-controller-manager` و `cloud-controller-manager`
مجوز می‌دهد، دسترسی‌های لازم را به روشی متناسب با همان حالت اعطا کنید.

<!-- steps -->

### اعطای دسترسی به Lease مهاجرت

مجوزهای پیش‌فرض مدیر کنترل‌کننده فقط اجازهٔ دسترسی به Lease اصلی آن را می‌دهند. برای
اینکه مهاجرت کار کند، دسترسی به یک Lease دیگر نیز لازم است.

می‌توانید با تغییر نقش `system::leader-locking-kube-controller-manager`، دسترسی کامل
به API مربوط به leaseها را به `kube-controller-manager` بدهید. در این راهنما فرض شده است
که نام lease مهاجرت `cloud-provider-extraction-migration` است.

```shell
kubectl patch -n kube-system role 'system::leader-locking-kube-controller-manager' -p '{"rules": [ {"apiGroups":[ "coordination.k8s.io"], "resources": ["leases"], "resourceNames": ["cloud-provider-extraction-migration"], "verbs": ["create", "list", "get", "update"] } ]}' --type=merge
```

همین کار را برای نقش `system::leader-locking-cloud-controller-manager` نیز انجام دهید.

```shell
kubectl patch -n kube-system role 'system::leader-locking-cloud-controller-manager' -p '{"rules": [ {"apiGroups":[ "coordination.k8s.io"], "resources": ["leases"], "resourceNames": ["cloud-provider-extraction-migration"], "verbs": ["create", "list", "get", "update"] } ]}' --type=merge
```

### پیکربندی اولیهٔ مهاجرت رهبر

مهاجرت رهبر می‌تواند به‌صورت اختیاری یک فایل پیکربندی دریافت کند که وضعیت تخصیص
کنترل‌کننده‌ها به مدیرها را نشان می‌دهد. در این مرحله، با ارائه‌دهندهٔ ابری داخلی،
`kube-controller-manager` کنترل‌کننده‌های `route`، `service` و `cloud-node-lifecycle` را
اجرا می‌کند. پیکربندی نمونهٔ زیر این تخصیص را نشان می‌دهد.

مهاجرت رهبر را می‌توان بدون پیکربندی نیز فعال کرد. برای جزئیات بیشتر،
[پیکربندی پیش‌فرض](#default-configuration) را ببینید.

```yaml
kind: LeaderMigrationConfiguration
apiVersion: controllermanager.config.k8s.io/v1
leaderName: cloud-provider-extraction-migration
resourceLock: leases
controllerLeaders:
  - name: route
    component: kube-controller-manager
  - name: service
    component: kube-controller-manager
  - name: cloud-node-lifecycle
    component: kube-controller-manager
```

به‌عنوان جایگزین، از آنجا که این کنترل‌کننده‌ها می‌توانند زیر هر یک از دو مدیر کنترل‌کننده
اجرا شوند، تنظیم `component` روی `*` برای هر دو طرف باعث می‌شود فایل پیکربندی برای هر دو
طرف مهاجرت یکسان باشد.

```yaml
# wildcard version
kind: LeaderMigrationConfiguration
apiVersion: controllermanager.config.k8s.io/v1
leaderName: cloud-provider-extraction-migration
resourceLock: leases
controllerLeaders:
  - name: route
    component: *
  - name: service
    component: *
  - name: cloud-node-lifecycle
    component: *
```

روی هر نود control plane، این محتوا را در `/etc/leadermigration.conf` ذخیره کنید و
مانیفست `kube-controller-manager` را طوری به‌روزرسانی کنید که این فایل در همان مسیر
درون کانتینر سوار (mount) شود. همچنین همین مانیفست را به‌روزرسانی کنید تا آرگومان‌های
زیر به آن افزوده شوند:

- `--enable-leader-migration` برای فعال‌کردن مهاجرت رهبر روی مدیر کنترل‌کننده
- `--leader-migration-config=/etc/leadermigration.conf` برای تعیین فایل پیکربندی

مؤلفهٔ `kube-controller-manager` را روی هر نود دوباره راه‌اندازی کنید. در این مرحله،
مهاجرت رهبر در `kube-controller-manager` فعال است و این مؤلفه برای مهاجرت آماده است.

### استقرار Cloud Controller Manager

در نسخهٔ N + 1، وضعیت مطلوب تخصیص کنترل‌کننده‌ها به مدیرها را می‌توان با یک فایل
پیکربندی جدید، مطابق نمونهٔ زیر، نشان داد. دقت کنید که فیلد `component` در هر یک از
`controllerLeaders` از `kube-controller-manager` به `cloud-controller-manager` تغییر
می‌کند. به‌عنوان جایگزین، می‌توانید از نسخهٔ wildcard که پیش‌تر ذکر شد استفاده کنید که
همین اثر را دارد.

```yaml
kind: LeaderMigrationConfiguration
apiVersion: controllermanager.config.k8s.io/v1
leaderName: cloud-provider-extraction-migration
resourceLock: leases
controllerLeaders:
  - name: route
    component: cloud-controller-manager
  - name: service
    component: cloud-controller-manager
  - name: cloud-node-lifecycle
    component: cloud-controller-manager
```

هنگام ایجاد نودهای control plane با نسخهٔ N + 1، این محتوا باید در
`/etc/leadermigration.conf` مستقر شود. مانیفست `cloud-controller-manager` باید طوری
به‌روزرسانی شود که فایل پیکربندی را به همان شیوهٔ `kube-controller-manager` نسخهٔ N
سوار کند. به همین ترتیب، `--enable-leader-migration` و
`--leader-migration-config=/etc/leadermigration.conf` را به آرگومان‌های
`cloud-controller-manager` بیفزایید.

یک نود control plane جدید با نسخهٔ N + 1 ایجاد کنید که مانیفست به‌روزشدهٔ
`cloud-controller-manager` را داشته باشد و فلگ `--cloud-provider` برای
`kube-controller-manager` روی `external` تنظیم شده باشد. در مؤلفهٔ
`kube-controller-manager` نسخهٔ N + 1 **نباید** مهاجرت رهبر فعال باشد؛ زیرا این مؤلفه
با ارائه‌دهندهٔ ابری خارجی دیگر کنترل‌کننده‌های مهاجرت‌داده‌شده را اجرا نمی‌کند و در نتیجه
در مهاجرت نقشی ندارد.

برای جزئیات بیشتر دربارهٔ نحوهٔ استقرار `cloud-controller-manager`، به
[مدیریت Cloud Controller Manager](/docs/tasks/administer-cluster/running-cloud-controller/)
مراجعه کنید.

### ارتقای control plane

اکنون control plane شامل نودهایی از هر دو نسخهٔ N و N + 1 است. نودهای نسخهٔ N فقط
`kube-controller-manager` را اجرا می‌کنند و نودهای نسخهٔ N + 1 هر دو مؤلفهٔ
`kube-controller-manager` و `cloud-controller-manager` را اجرا می‌کنند.
کنترل‌کننده‌های مهاجرت‌داده‌شده، همان‌طور که در پیکربندی مشخص شده است، بسته به اینکه
کدام مدیر کنترل‌کننده lease مهاجرت را در اختیار دارد، یا زیر `kube-controller-manager`
نسخهٔ N و یا زیر `cloud-controller-manager` نسخهٔ N + 1 اجرا می‌شوند. هیچ کنترل‌کننده‌ای
هرگز به‌طور هم‌زمان زیر هر دو مدیر کنترل‌کننده اجرا نخواهد شد.

به‌صورت چرخشی (rolling)، هر بار یک نود control plane جدید با نسخهٔ N + 1 ایجاد کنید و
یکی از نودهای نسخهٔ N را از کار بیندازید، تا جایی که control plane فقط شامل نودهای
نسخهٔ N + 1 باشد. اگر بازگشت (rollback) از نسخهٔ N + 1 به N لازم شد، نودهایی از نسخهٔ N را
که مهاجرت رهبر برای `kube-controller-manager` آن‌ها فعال است دوباره به control plane
بیفزایید و هر بار یکی از نودهای نسخهٔ N + 1 را جایگزین کنید تا فقط نودهای نسخهٔ N
باقی بمانند.

### (اختیاری) غیرفعال‌کردن مهاجرت رهبر {#disable-leader-migration}

اکنون که control plane ارتقا یافته است و هر دو مؤلفهٔ `kube-controller-manager` و
`cloud-controller-manager` با نسخهٔ N + 1 را اجرا می‌کند، کار مهاجرت رهبر به پایان رسیده
است و می‌توان آن را با خیال راحت غیرفعال کرد تا در یک منبع Lease صرفه‌جویی شود. فعال‌کردن
دوبارهٔ مهاجرت رهبر برای بازگشت در آینده نیز بی‌خطر است.

به‌صورت چرخشی، مانیفست `cloud-controller-manager` را به‌روزرسانی کنید تا هر دو فلگ
`--enable-leader-migration` و `--leader-migration-config=` حذف شوند. همچنین سوارکردن
`/etc/leadermigration.conf` را حذف کنید و در پایان خود فایل `/etc/leadermigration.conf`
را پاک کنید. برای فعال‌کردن دوبارهٔ مهاجرت رهبر، فایل پیکربندی را از نو بسازید و سوارکردن
آن و فلگ‌های فعال‌کنندهٔ مهاجرت رهبر را دوباره به `cloud-controller-manager` بیفزایید.

### پیکربندی پیش‌فرض

از کوبرنتیز 1.22 به بعد، مهاجرت رهبر یک پیکربندی پیش‌فرض ارائه می‌کند که برای تخصیص
پیش‌فرض کنترل‌کننده‌ها به مدیرها مناسب است.
برای فعال‌کردن پیکربندی پیش‌فرض، `--enable-leader-migration` را تنظیم کنید، اما
`--leader-migration-config=` را تنظیم نکنید.

برای `kube-controller-manager` و `cloud-controller-manager`، اگر هیچ فلگی وجود نداشته
باشد که ارائه‌دهندهٔ ابری داخلی را فعال کند یا مالکیت کنترل‌کننده‌ها را تغییر دهد،
می‌توان از پیکربندی پیش‌فرض استفاده کرد تا نیازی به ساخت دستی فایل پیکربندی نباشد.

### حالت خاص: مهاجرت کنترل‌کنندهٔ Node IPAM {#node-ipam-controller-migration}

اگر ارائه‌دهندهٔ ابری شما پیاده‌سازی‌ای از کنترل‌کنندهٔ Node IPAM ارائه می‌کند، باید به
پیاده‌سازی موجود در `cloud-controller-manager` روی بیاورید. کنترل‌کنندهٔ Node IPAM را در
`kube-controller-manager` نسخهٔ N + 1 با افزودن `--controllers=*,-nodeipam` به فلگ‌های
آن غیرفعال کنید. سپس `nodeipam` را به فهرست کنترل‌کننده‌های مهاجرت‌داده‌شده بیفزایید.

```yaml
# wildcard version, with nodeipam
kind: LeaderMigrationConfiguration
apiVersion: controllermanager.config.k8s.io/v1
leaderName: cloud-provider-extraction-migration
resourceLock: leases
controllerLeaders:
  - name: route
    component: *
  - name: service
    component: *
  - name: cloud-node-lifecycle
    component: *
  - name: nodeipam
-   component: *
```

## {{% heading "whatsnext" %}}

- پیشنهاد بهبود [Controller Manager Leader Migration](https://github.com/kubernetes/enhancements/tree/master/keps/sig-cloud-provider/2436-controller-manager-leader-migration)
  را مطالعه کنید.
