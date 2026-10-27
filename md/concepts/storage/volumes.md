---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
title: Volumes
api_metadata:
- apiVersion: ""
  kind: "Volume"
content_type: concept
weight: 10
---

<!-- overview -->

_حجم‌های_ (volumes) کوبرنتیز راهی را فراهم می‌کنند تا کانتینرها در یک {{< glossary_tooltip text="Pod" term_id="pod" >}}
بتوانند از طریق سیستم فایل به داده‌ها دسترسی داشته باشند و آن‌ها را به اشتراک بگذارند. انواع مختلفی از حجم وجود دارد که می‌توانید برای مقاصد گوناگون از آن‌ها استفاده کنید،
از جمله:

- پر کردن یک فایل پیکربندی بر اساس یک {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}}
  یا یک {{< glossary_tooltip text="Secret" term_id="secret" >}}
- فراهم کردن مقداری فضای موقت (scratch) برای یک Pod
- اشتراک‌گذاری یک سیستم فایل بین دو کانتینر مختلف در همان Pod
- اشتراک‌گذاری یک سیستم فایل بین دو Pod مختلف (حتی اگر آن Podها روی نودهای مختلف اجرا شوند)
- ذخیره‌سازی پایدار داده‌ها به‌گونه‌ای که حتی با راه‌اندازی مجدد یا جایگزینی Pod نیز در دسترس باقی بمانند
- ارسال اطلاعات پیکربندی به برنامه‌ای که در یک کانتینر اجرا می‌شود، بر اساس جزئیات Podی که کانتینر در آن قرار دارد
  (برای مثال: اعلام اینکه Pod در کدام فضای نام (namespace) در حال اجراست به یک {{< glossary_tooltip text="کانتینر sidecar" term_id="sidecar-container" >}})
- فراهم کردن دسترسی فقط‌خواندنی به داده‌ها در یک ایمیج کانتینر دیگر

اشتراک‌گذاری داده می‌تواند بین فرایندهای محلی مختلف درون یک کانتینر، یا بین کانتینرهای مختلف،
یا بین Podها انجام شود.

## اهمیت حجم‌ها

- **پایداری داده:** فایل‌های روی دیسکِ یک کانتینر موقتی هستند و این موضوع برای
  برنامه‌های غیرساده‌ای که درون کانتینرها اجرا می‌شوند مشکلاتی ایجاد می‌کند. یکی از این مشکلات زمانی رخ می‌دهد که
  یک کانتینر از کار بیفتد یا متوقف شود؛ در این حالت وضعیت کانتینر ذخیره نمی‌شود و بنابراین تمام
  فایل‌هایی که در طول عمر کانتینر ایجاد یا تغییر داده شده‌اند از دست می‌روند.
  پس از یک خرابی، kubelet کانتینر را با یک وضعیت پاک دوباره راه‌اندازی می‌کند.

- **ذخیره‌سازی مشترک:** مشکل دیگر زمانی پیش می‌آید که چندین کانتینر در یک `Pod` در حال اجرا هستند و
  باید فایل‌ها را به اشتراک بگذارند. راه‌اندازی یک سیستم فایل مشترک و دسترسی به آن
  در میان تمام کانتینرها می‌تواند دشوار باشد.

انتزاع {{< glossary_tooltip text="حجم" term_id="volume" >}} در کوبرنتیز
می‌تواند به شما در حل هر دوی این مشکلات کمک کند.

پیش از آنکه درباره حجم‌ها، PersistentVolumeها و PersistentVolumeClaimها بیاموزید، باید درباره
{{< glossary_tooltip term_id="Pod" text="Podها" >}} مطالعه کنید و مطمئن شوید که می‌دانید
کوبرنتیز چگونه از Podها برای اجرای کانتینرها استفاده می‌کند.
  
<!-- body -->

## حجم‌ها چگونه کار می‌کنند

کوبرنتیز از انواع زیادی از حجم‌ها پشتیبانی می‌کند. یک {{< glossary_tooltip term_id="pod" text="Pod" >}}
می‌تواند همزمان از هر تعداد نوع حجم استفاده کند.
انواع [حجم موقت](/docs/concepts/storage/ephemeral-volumes/) عمری دارند که به یک Pod مشخص وابسته است،
اما [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/) فراتر از
عمر هر Pod منفرد وجود دارند. هنگامی که یک Pod از بین می‌رود، کوبرنتیز حجم‌های موقت را نابود می‌کند؛
با این حال، کوبرنتیز حجم‌های پایدار را نابود نمی‌کند.
برای هر نوع حجم در یک Pod مشخص، داده‌ها در طول راه‌اندازی مجدد کانتینرها حفظ می‌شوند.

در اصل، یک حجم دایرکتوریِ است که ممکن است داده‌هایی در آن وجود داشته باشد و
کانتینرهای درون یک Pod به آن دسترسی دارند. اینکه این دایرکتوری چگونه ایجاد می‌شود،
چه رسانه‌ای پشتوانه آن است و محتوای آن چیست، توسط نوع خاص
حجمِ مورد استفاده تعیین می‌شود.

برای استفاده از یک حجم، حجم‌هایی را که باید برای Pod فراهم شوند در `.spec.volumes` مشخص کنید
و محل اتصال (mount) آن حجم‌ها را درون کانتینرها در `.spec.containers[*].volumeMounts` تعریف کنید.

هنگامی که یک Pod راه‌اندازی می‌شود، فرایند درون کانتینر نمایی از سیستم فایل را می‌بیند که از محتوای اولیه
{{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} به‌علاوه حجم‌ها
(در صورت تعریف‌شدن) که درون کانتینر mount شده‌اند، تشکیل شده است.
فرایند یک سیستم فایل ریشه را می‌بیند که در ابتدا با محتوای ایمیج کانتینر مطابقت دارد.
هر نوشتن در این سلسله‌مراتب سیستم فایل، در صورت مجاز بودن، بر آنچه آن فرایند
در دسترسی‌های بعدی به سیستم فایل می‌بیند اثر می‌گذارد.
حجم‌ها در [مسیرهای مشخص‌شده](#using-subpath) درون سیستم فایل کانتینر mount می‌شوند.
برای هر کانتینر تعریف‌شده در یک Pod، باید محل mount کردن هر حجمی را که آن کانتینر استفاده می‌کند
به‌طور مستقل مشخص کنید.

حجم‌ها نمی‌توانند درون حجم‌های دیگر mount شوند (اما برای یک سازوکار مرتبط
به [استفاده از subPath](#using-subpath) مراجعه کنید). همچنین، یک حجم نمی‌تواند شامل hard link به چیزی
در حجم دیگر باشد.

## انواع حجم‌ها {#volume-types}

کوبرنتیز از چند نوع حجم پشتیبانی می‌کند.

### configMap

یک [ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/)
راهی برای تزریق داده‌های پیکربندی به Podها فراهم می‌کند.
داده‌های ذخیره‌شده در یک ConfigMap را می‌توان در یک حجم از نوع
`configMap` ارجاع داد و سپس توسط برنامه‌های کانتینری‌شده‌ای که در یک Pod اجرا می‌شوند مصرف کرد.

هنگام ارجاع به یک ConfigMap، نام آن ConfigMap را در
حجم مشخص می‌کنید. می‌توانید مسیری را که برای یک
ورودی خاص در ConfigMap استفاده می‌شود سفارشی کنید. پیکربندی زیر نشان می‌دهد چگونه
ConfigMap با نام `log-config` را روی یک Pod با نام `configmap-pod` mount کنید:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod
spec:
  containers:
    - name: test
      image: busybox:1.28
      command: ['sh', '-c', 'echo "The app is running!" && tail -f /dev/null']
      volumeMounts:
        - name: config-vol
          mountPath: /etc/config
  volumes:
    - name: config-vol
      configMap:
        name: log-config
        items:
          - key: log_level
            path: log_level.conf
```

ConfigMap با نام `log-config` به‌صورت یک حجم mount می‌شود و تمام محتوای ذخیره‌شده در
ورودی `log_level` آن در مسیر `/etc/config/log_level.conf` درون Pod mount می‌شود.
توجه کنید که این مسیر از `mountPath` حجم و `path`
مربوط به کلید `log_level` ساخته می‌شود.

{{< note >}}

* باید پیش از استفاده از یک ConfigMap، آن را [ایجاد کنید](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-a-configmap).

* یک ConfigMap همیشه به‌صورت `readOnly` mount می‌شود.

* کانتینری که از یک ConfigMap به‌عنوان mount حجم از نوع [`subPath`](#using-subpath) استفاده می‌کند،
  هنگام تغییر ConfigMap به‌روزرسانی‌ها را دریافت نخواهد کرد.
  
* داده‌های متنی با کدگذاری نویسه UTF-8 به‌صورت فایل در دسترس قرار می‌گیرند.
  برای سایر کدگذاری‌های نویسه، از `binaryData` استفاده کنید.

{{< /note >}}

### downwardAPI {#downwardapi}

یک حجم `downwardAPI` داده‌های {{< glossary_tooltip term_id="downward-api" text="downward API" >}}
را در اختیار برنامه‌ها قرار می‌دهد. درون این حجم، می‌توانید داده‌های در دسترس‌گذاشته‌شده را
به‌صورت فایل‌های فقط‌خواندنی با قالب متن ساده پیدا کنید.

{{< note >}}
کانتینری که از downward API به‌عنوان mount حجم از نوع [`subPath`](#using-subpath) استفاده می‌کند،
هنگام تغییر مقادیر فیلدها به‌روزرسانی‌ها را دریافت نمی‌کند.
{{< /note >}}

برای کسب اطلاعات بیشتر، [در دسترس قرار دادن اطلاعات Pod برای کانتینرها از طریق فایل‌ها](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
را ببینید.

### emptyDir {#emptydir}

برای یک Pod که یک حجم `emptyDir` تعریف می‌کند، این حجم هنگامی ایجاد می‌شود که Pod به یک نود اختصاص داده شود.
همان‌طور که از نامش پیداست، حجم `emptyDir` در ابتدا خالی است. تمام کانتینرهای درون Pod می‌توانند همان
فایل‌ها را در حجم `emptyDir` بخوانند و بنویسند، هرچند این حجم می‌تواند در هر کانتینر در مسیرهای یکسان
یا متفاوت mount شود. هنگامی که یک Pod به هر دلیلی از یک نود حذف شود،
داده‌های `emptyDir` برای همیشه پاک می‌شوند.

{{< note >}}
از کار افتادن یک کانتینر، Pod را از نود حذف *نمی‌کند*. داده‌های یک حجم `emptyDir`
در برابر از کار افتادن کانتینرها ایمن هستند.
{{< /note >}}

برخی کاربردهای `emptyDir` عبارت‌اند از:

* فضای موقت (scratch)، مانند مرتب‌سازی ادغامی مبتنی بر دیسک
* ایجاد نقطه بازرسی (checkpoint) برای یک محاسبه طولانی جهت بازیابی پس از خرابی‌ها
* نگهداری فایل‌هایی که یک کانتینر مدیریت محتوا واکشی می‌کند، در حالی که یک کانتینر
  وب‌سرور داده‌ها را ارائه می‌دهد

فیلد `emptyDir.medium` مشخص می‌کند که حجم‌های `emptyDir` کجا ذخیره شوند. به‌طور
پیش‌فرض، حجم‌های `emptyDir` روی هر رسانه‌ای که پشتوانه نود است ذخیره می‌شوند،
مانند دیسک، SSD یا ذخیره‌سازی شبکه‌ای، بسته به محیط شما. اگر
فیلد `emptyDir.medium` را روی `"Memory"` تنظیم کنید، کوبرنتیز به‌جای آن یک tmpfs (سیستم فایل
مبتنی بر RAM) برای شما mount می‌کند. اگرچه tmpfs بسیار سریع است، توجه داشته باشید که برخلاف
دیسک‌ها، فایل‌هایی که می‌نویسید در محدودیت حافظه کانتینری که آن‌ها را نوشته محاسبه می‌شوند.

می‌توان برای رسانه پیش‌فرض یک محدودیت اندازه مشخص کرد که ظرفیت
حجم `emptyDir` را محدود می‌کند. فضای ذخیره‌سازی از
[ذخیره‌سازی موقت نود](/docs/concepts/storage/ephemeral-storage/#setting-requests-and-limits-for-local-ephemeral-storage) اختصاص داده می‌شود.
اگر این فضا از منبع دیگری پر شود (برای مثال، فایل‌های گزارش یا overlayهای ایمیج)،
ممکن است ظرفیت `emptyDir` پیش از رسیدن به این محدودیت تمام شود.
اگر اندازه‌ای مشخص نشود، اندازه حجم‌های مبتنی بر حافظه برابر با حافظه قابل تخصیص (allocatable) نود خواهد بود.

{{< caution >}}
لطفاً برای نکاتی که هنگام استفاده از `emptyDir` مبتنی بر حافظه از نظر مدیریت منابع باید در نظر داشت،
[اینجا](/docs/concepts/configuration/manage-resources-containers/#memory-backed-emptydir) را بررسی کنید.
{{< /caution >}}

{{< feature-state feature_gate_name="EmptyDirVolumeMode" >}}

فیلد `emptyDir.mode` به شما امکان می‌دهد بیت‌های مجوز یونیکس را روی دایرکتوری emptyDir تنظیم کنید
و مقداری بین `0000` و `01777` (در مبنای هشت) مشخص نمایید. این رویکرد همان الگوی فیلد
`defaultMode` در حجم‌های Secret و ConfigMap را دنبال می‌کند. اگر `mode` مشخص نشود،
دایرکتوری با مجوزهای پیش‌فرض `0777` ایجاد می‌شود.

تنظیم یک mode سفارشی زمانی مفید است که بخواهید دسترسی را فقط به مالک و گروه محدود کنید
(برای مثال، `0750`)، یا بیت sticky را روی یک دایرکتوری مشترک تنظیم کنید تا فقط مالکان فایل‌ها
بتوانند فایل‌های خودشان را حذف کنند (برای مثال، `01777`).

{{< note >}}
اگر `fsGroup` در زمینه امنیتی (security context) Pod تنظیم شده باشد، مجوزهای گروهی که توسط
`fsGroup` اعمال می‌شوند بر `mode` مشخص‌شده در اینجا اولویت دارند. فیلد `mode` در ویندوز تأثیری ندارد.
{{< /note >}}

#### نمونه پیکربندی emptyDir

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir:
      sizeLimit: 500Mi
```

#### نمونه پیکربندی emptyDir مبتنی بر حافظه

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir:
      sizeLimit: 500Mi
      medium: Memory
```

#### emptyDir و تغییر اندازه درجای Pod

{{< feature-state feature_gate_name="InPlacePodVerticalScalingMemoryBackedVolumes" >}}

هنگامی که feature gate با نام `InPlacePodVerticalScalingMemoryBackedVolumes` فعال باشد، می‌توانید `sizeLimit` حجم‌های `emptyDir` مبتنی بر حافظه (`medium: Memory`) را بدون راه‌اندازی مجدد Pod یا کانتینرهای آن، به‌صورت پویا تنظیم کنید.

برای جزئیات بیشتر، [تغییر اندازه منابع CPU و حافظه اختصاص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/#resizing-memory-backed-emptydir-volumes) را ببینید.



#### نمونه پیکربندی مجوزهای emptyDir

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir:
      mode: 01777
```

### fc (fibre channel) {#fc}

نوع حجم `fc` اجازه می‌دهد یک حجم ذخیره‌سازی بلوکی fibre channel موجود
در یک Pod mount شود. می‌توانید یک یا چند world wide name (WWN) هدف را
با استفاده از پارامتر `targetWWNs` در پیکربندی Volume خود مشخص کنید. اگر چندین WWN مشخص شده باشد،
targetWWNs انتظار دارد که این WWNها از اتصال‌های چندمسیره (multi-path) باشند.

{{< note >}}
باید از پیش FC SAN Zoning را پیکربندی کنید تا آن LUNها (حجم‌ها) به WWNهای هدف اختصاص یابند و مخفی‌سازی (mask) شوند
تا میزبان‌های کوبرنتیز بتوانند به آن‌ها دسترسی داشته باشند.
{{< /note >}}

### gcePersistentDisk (منسوخ‌شده) {#gcepersistentdisk}

در کوبرنتیز {{< skew currentVersion >}}، تمام عملیات مربوط به نوع درون‌درختی (in-tree) `gcePersistentDisk`
به درایور {{< glossary_tooltip text="CSI" term_id="csi" >}} با نام `pd.csi.storage.gke.io` هدایت می‌شود.

درایور ذخیره‌سازی درون‌درختی `gcePersistentDisk` در نسخه v1.17 کوبرنتیز منسوخ شد
و سپس در نسخه v1.28 به‌طور کامل حذف گردید.

پروژه کوبرنتیز پیشنهاد می‌کند که به‌جای آن از
درایور ذخیره‌سازی شخص ثالث [Google Compute Engine Persistent Disk CSI](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver)
استفاده کنید.

### gitRepo (غیرفعال) {#gitrepo}

{{< warning >}}

کوبرنتیز {{< skew latestVersion >}} درایور حجم `gitRepo` را *شامل نمی‌شود*.
آخرین نسخه‌ای که راهی برای استفاده از این درایور فراهم می‌کرد کوبرنتیز
v1.35 بود، و این درایور از نسخه فرعی [v1.11](/releases/1.11) منسوخ شده است.

برای ایجاد یک Pod که یک مخزن Git روی آن mount شده است، می‌توانید یک حجم
[`emptyDir`](#emptydir) را درون یک [init container](/docs/concepts/workloads/pods/init-containers/)
mount کنید که مخزن را با استفاده از Git کلون می‌کند، سپس آن [EmptyDir](#emptydir) را در کانتینر Pod mount کنید.

---

می‌توانید استفاده از حجم‌های `gitRepo` را در کلاستر خود با استفاده از
[سیاست‌ها](/docs/concepts/policy/)، مانند
[ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)،
محدود کنید.
می‌توانید از عبارت Common Expression Language (CEL) زیر به‌عنوان
بخشی از یک سیاست برای رد استفاده از حجم‌های `gitRepo` بهره ببرید:

```cel
!has(object.spec.volumes) || !object.spec.volumes.exists(v, has(v.gitRepo))
```

{{< /warning >}}

### hostPath {#hostpath}

یک حجم (volume) از نوع `hostPath` یک فایل یا دایرکتوری را از سیستم فایل نودِ میزبان به درون Pod شما مانت می‌کند. اغلب Podها به این قابلیت نیازی ندارند، اما این نوع حجم برای برخی برنامه‌ها یک راه فرار قدرتمند فراهم می‌کند.

{{< warning >}}
استفاده از نوع حجم `hostPath` خطرات امنیتی متعددی به همراه دارد.
اگر می‌توانید از استفاده از حجم `hostPath` پرهیز کنید، این کار را انجام دهید. برای مثال،
یک [PersistentVolume از نوع `local`](#local) تعریف کنید و به‌جای آن از آن استفاده کنید.

اگر دسترسی به دایرکتوری‌های مشخصی روی نود را با اعتبارسنجی در زمان پذیرش (admission-time validation) محدود می‌کنید، این محدودیت تنها زمانی مؤثر است که علاوه بر آن، الزام کنید هر مانتِ آن حجم `hostPath` به‌صورت **فقط‌خواندنی** باشد. اگر مانت خواندن‌ـ‌نوشتنی هر مسیر میزبان را توسط یک Pod نامعتبر (untrusted) مجاز کنید، کانتینرهای آن Pod ممکن است بتوانند مانت خواندن‌ـ‌نوشتنی میزبان را دور بزنند.

---

هنگام استفاده از حجم‌های `hostPath`، چه به‌صورت فقط‌خواندنی و چه به‌صورت خواندن‌ـ‌نوشتنی مانت شده باشند، احتیاط کنید، زیرا:

* دسترسی به سیستم فایل میزبان می‌تواند اعتبارنامه‌های سیستمی دارای سطح دسترسی بالا (مانند اعتبارنامه‌های kubelet) یا APIهای دارای سطح دسترسی بالا (مانند سوکت container runtime) را افشا کند که می‌توان از آن‌ها برای فرار از کانتینر یا حمله به سایر بخش‌های کلاستر استفاده کرد.
* Podهایی با پیکربندی یکسان (مثلاً ایجادشده از یک PodTemplate) ممکن است به دلیل تفاوت فایل‌ها روی نودهای مختلف، رفتار متفاوتی داشته باشند.
* مصرف حجم `hostPath` به‌عنوان مصرف ذخیره‌سازی موقت (ephemeral storage) محاسبه نمی‌شود.
  باید مصرف دیسک را خودتان پایش کنید، زیرا مصرف بیش‌ازحد دیسک توسط `hostPath` به فشار دیسک (disk pressure) روی نود منجر می‌شود.
{{< /warning >}}

برخی کاربردهای `hostPath` عبارت‌اند از:

* اجرای کانتینری که به مؤلفه‌های سیستمی سطح نود نیاز دارد
  (مانند کانتینری که لاگ‌های سیستم را به یک مکان مرکزی منتقل می‌کند
  و با استفاده از یک مانت فقط‌خواندنی از `/var/log` به آن لاگ‌ها دسترسی پیدا می‌کند)
* در دسترس قرار دادن یک فایل پیکربندی ذخیره‌شده روی سیستم میزبان به‌صورت فقط‌خواندنی
  برای یک {{< glossary_tooltip text="Pod ایستا" term_id="static-pod" >}}؛
  برخلاف Podهای معمولی، Podهای ایستا نمی‌توانند به ConfigMapها دسترسی داشته باشند

#### انواع حجم `hostPath`

علاوه بر ویژگی الزامی `path`، می‌توانید به‌صورت اختیاری یک
`type` برای حجم `hostPath` مشخص کنید.

مقادیر در دسترس برای `type` عبارت‌اند از:

<!-- empty string represented using U+200C ZERO WIDTH NON-JOINER -->

| مقدار | رفتار |
|:------|:---------|
| `‌""` | رشته خالی (پیش‌فرض) برای سازگاری با نسخه‌های قبلی است و به این معناست که پیش از مانت کردن حجم `hostPath` هیچ بررسی‌ای انجام نمی‌شود. |
| `DirectoryOrCreate` | اگر در مسیر داده‌شده چیزی وجود نداشته باشد، در صورت نیاز یک دایرکتوری خالی با مجوز 0755 در آنجا ایجاد می‌شود که گروه و مالکیت آن با Kubelet یکسان است. |
| `Directory` | باید یک دایرکتوری در مسیر داده‌شده وجود داشته باشد. |
| `FileOrCreate` | اگر در مسیر داده‌شده چیزی وجود نداشته باشد، در صورت نیاز یک فایل خالی با مجوز 0644 در آنجا ایجاد می‌شود که گروه و مالکیت آن با Kubelet یکسان است. |
| `File` | باید یک فایل در مسیر داده‌شده وجود داشته باشد. |
| `Socket` | باید یک سوکت UNIX در مسیر داده‌شده وجود داشته باشد. |
| `CharDevice` | _(فقط نودهای لینوکسی)_ باید یک دستگاه کاراکتری (character device) در مسیر داده‌شده وجود داشته باشد. |
| `BlockDevice` | _(فقط نودهای لینوکسی)_ باید یک دستگاه بلوکی (block device) در مسیر داده‌شده وجود داشته باشد. |

{{< caution >}}
حالت `FileOrCreate` دایرکتوری والد فایل را **ایجاد نمی‌کند**. اگر دایرکتوری والد
فایل مانت‌شده وجود نداشته باشد، Pod شروع به کار نمی‌کند. برای اطمینان از کارکرد این حالت،
می‌توانید دایرکتوری‌ها و فایل‌ها را جداگانه مانت کنید، همان‌طور که در
[مثال `FileOrCreate`](#hostpath-fileorcreate-example) برای `hostPath` نشان داده شده است.
{{< /caution >}}

برخی فایل‌ها یا دایرکتوری‌های ایجادشده روی میزبان‌های زیرین ممکن است فقط برای root
قابل دسترسی باشند. در این صورت یا باید فرایند خود را به‌عنوان root درون یک
[کانتینر دارای دسترسی ویژه (privileged)](/docs/tasks/configure-pod-container/security-context/)
اجرا کنید، یا مجوزهای فایل را روی میزبان تغییر دهید تا بتوانید از حجم `hostPath` بخوانید یا در آن بنویسید.

#### نمونه پیکربندی hostPath

{{< tabs name="hostpath_examples" >}}
{{< tab name="Linux node" codelang="yaml" >}}
---
# این مانیفست مسیر /data/foo روی میزبان را به‌صورت /foo درون
# تنها کانتینری که در Pod با نام hostpath-example-linux اجرا می‌شود مانت می‌کند.
#
# مانت درون کانتینر فقط‌خواندنی است.
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-example-linux
spec:
  os: { name: linux }
  nodeSelector:
    kubernetes.io/os: linux
  containers:
  - name: example-container
    image: registry.k8s.io/test-webserver
    volumeMounts:
    - mountPath: /foo
      name: example-volume
      readOnly: true
  volumes:
  - name: example-volume
    # مسیر /data/foo را مانت می‌کند، اما فقط اگر آن دایرکتوری از قبل وجود داشته باشد
    hostPath:
      path: /data/foo # مکان دایرکتوری روی میزبان
      type: Directory # این فیلد اختیاری است
{{< /tab >}}
{{< tab name="Windows node" codelang="yaml" >}}
---
# این مانیفست مسیر C:\Data\foo روی میزبان را به‌صورت C:\foo درون
# تنها کانتینری که در Pod با نام hostpath-example-windows اجرا می‌شود مانت می‌کند.
#
# مانت درون کانتینر فقط‌خواندنی است.
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-example-windows
spec:
  os: { name: windows }
  nodeSelector:
    kubernetes.io/os: windows
  containers:
  - name: example-container
    image: microsoft/windowsservercore:1709
    volumeMounts:
    - name: example-volume
      mountPath: "C:\\foo"
      readOnly: true
  volumes:
    # مسیر C:\Data\foo را از میزبان مانت می‌کند، اما فقط اگر آن دایرکتوری از قبل وجود داشته باشد
  - name: example-volume
    hostPath:
      path: "C:\\Data\\foo" # مکان دایرکتوری روی میزبان
      type: Directory       # این فیلد اختیاری است
{{< /tab >}}
{{< /tabs >}}

#### نمونه پیکربندی hostPath با FileOrCreate {#hostpath-fileorcreate-example}

مانیفست زیر یک Pod تعریف می‌کند که مسیر `/var/local/aaa` را
درون تنها کانتینر Pod مانت می‌کند. اگر نود از قبل مسیر `/var/local/aaa` را
نداشته باشد، kubelet آن را به‌صورت یک دایرکتوری ایجاد می‌کند و سپس آن را درون Pod مانت می‌کند.

اگر `/var/local/aaa` از قبل وجود داشته باشد اما دایرکتوری نباشد،
Pod با شکست مواجه می‌شود. علاوه بر این، kubelet تلاش می‌کند
فایلی با نام `/var/local/aaa/1.txt` را درون آن دایرکتوری ایجاد کند
(از دید میزبان)؛ اگر در آن مسیر از قبل چیزی وجود داشته باشد
و فایل معمولی نباشد، Pod با شکست مواجه می‌شود.

مانیفست نمونه به شرح زیر است:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-webserver
spec:
  os: { name: linux }
  nodeSelector:
    kubernetes.io/os: linux
  containers:
  - name: test-webserver
    image: registry.k8s.io/test-webserver:latest
    volumeMounts:
    - mountPath: /var/local/aaa
      name: mydir
    - mountPath: /var/local/aaa/1.txt
      name: myfile
  volumes:
  - name: mydir
    hostPath:
      # Ensure the file directory is created.
      path: /var/local/aaa
      type: DirectoryOrCreate
  - name: myfile
    hostPath:
      path: /var/local/aaa/1.txt
      type: FileOrCreate
```

### image

{{< feature-state feature_gate_name="ImageVolume" >}}

یک منبع حجم از نوع `image` یک آبجکت OCI (یک ایمیج کانتینر یا
artifact) را نمایندگی می‌کند که روی ماشین میزبان kubelet در دسترس است.

نمونه‌ای از استفاده از منبع حجم `image` به شرح زیر است:

{{% code_sample file="pods/image-volumes.yaml" %}}

حجم در زمان راه‌اندازی Pod و بسته به مقدار `pullPolicy` ارائه‌شده، resolve می‌شود:

`Always`
: kubelet همیشه تلاش می‌کند مرجع را pull کند. اگر pull با شکست مواجه شود،
  kubelet وضعیت Pod را `Failed` قرار می‌دهد.

`Never`
: kubelet هرگز مرجع را pull نمی‌کند و فقط از ایمیج یا artifact محلی استفاده می‌کند.
  اگر هر یک از لایه‌های ایمیج از قبل به‌صورت محلی موجود نباشد،
  یا مانیفست آن ایمیج از قبل کش نشده باشد، Pod در وضعیت `Failed` قرار می‌گیرد.

`IfNotPresent`
: kubelet در صورتی pull می‌کند که مرجع از قبل روی دیسک موجود نباشد. اگر مرجع موجود نباشد
  و pull با شکست مواجه شود، Pod در وضعیت `Failed` قرار می‌گیرد.

اگر Pod حذف و دوباره ایجاد شود، حجم دوباره resolve می‌شود؛ به این معنا
که محتوای راه‌دور جدید هنگام ایجاد مجدد Pod در دسترس قرار می‌گیرد. شکست در
resolve یا pull کردن ایمیج در زمان راه‌اندازی Pod مانع شروع به کار کانتینرها می‌شود
و ممکن است تأخیر قابل‌توجهی ایجاد کند. شکست‌ها با استفاده از backoff معمول حجم
دوباره امتحان می‌شوند و در reason و message مربوط به Pod گزارش خواهند شد.

انواع آبجکت‌هایی که می‌توان با این حجم مانت کرد، توسط پیاده‌سازی
container runtime روی ماشین میزبان تعیین می‌شود. حداقل، این انواع باید شامل
همه انواع معتبری باشند که فیلد ایمیج کانتینر پشتیبانی می‌کند. آبجکت OCI
در یک دایرکتوری واحد (`spec.containers[*].volumeMounts[*].mountPath`) مانت می‌شود
و به‌صورت فقط‌خواندنی مانت خواهد شد.

علاوه بر این:

- مانت‌های [`subPath`](/docs/concepts/storage/volumes/#using-subpath) یا
  [`subPathExpr`](/docs/concepts/storage/volumes/#using-subpath-expanded-environment)
  برای کانتینرها (`spec.containers[*].volumeMounts[*].subPath`، `spec.containers[*].volumeMounts[*].subPathExpr`)
  تنها از کوبرنتیز v1.33 به بعد پشتیبانی می‌شوند.
- فیلد `spec.securityContext.fsGroupChangePolicy` روی این نوع حجم
  تأثیری ندارد.
- [Admission Controller با نام `AlwaysPullImages`](/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages)
  برای این منبع حجم نیز همانند ایمیج‌های کانتینر کار می‌کند.

فیلدهای زیر برای نوع `image` در دسترس هستند:

`reference`
: مرجع artifact که باید استفاده شود. برای مثال، می‌توانید
  `registry.k8s.io/conformance:v{{< skew currentPatchVersion >}}` را مشخص کنید تا
  فایل‌ها از ایمیج آزمون انطباق (conformance) کوبرنتیز بارگیری شوند. به همان روش
  `pod.spec.containers[*].image` رفتار می‌کند. Pull secretها به همان روشی که برای ایمیج کانتینر
  انجام می‌شود، با جست‌وجوی اعتبارنامه‌های نود، pull secretهای ایمیج مربوط به service account
  و pull secretهای ایمیج در مشخصات Pod گردآوری می‌شوند. این فیلد اختیاری است تا
  مدیریت پیکربندی در سطح بالاتر بتواند ایمیج‌های کانتینر را در
  کنترل‌کننده‌های بار کاری مانند Deployment و StatefulSet به‌صورت پیش‌فرض تنظیم یا بازنویسی کند.
  [اطلاعات بیشتر درباره ایمیج‌های کانتینر](/docs/concepts/containers/images).

`pullPolicy`
: سیاست pull کردن آبجکت‌های OCI. مقادیر ممکن عبارت‌اند از: `Always`، `Never` یا
  `IfNotPresent`. اگر تگ `:latest` مشخص شده باشد، مقدار پیش‌فرض `Always` است،
  و در غیر این صورت `IfNotPresent`.

برای جزئیات بیشتر درباره نحوه استفاده از این منبع حجم، مثال
[_استفاده از Image Volume در یک Pod_](/docs/tasks/configure-pod-container/image-volumes)
را ببینید.

#### وضعیت Pod و حجم‌های `image` {#image-volume-pod-status}

{{< feature-state feature_gate_name="ImageVolumeWithDigest" >}}

اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ImageVolumeWithDigest`
در کلاستر شما فعال باشد،
آنگاه هرگاه برای یک Pod یک حجم `image` مشخص کنید،
kubelet وضعیت Pod را به‌روزرسانی می‌کند تا _digest_
ایمیج کانتینری را که به‌عنوان منبع حجم استفاده می‌شود ثبت کند.

در ادامه یک نمونه ساده‌شده از یک Pod در حال اجرا، به‌صورت YAML و همراه با به‌روزرسانی وضعیت آمده است.
به فیلد جدید `ImageRef` در `volumeMounts` درون وضعیت کانتینر توجه کنید.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: default
spec:
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: docker.io/library/debian:12
    volumeMounts:
    - name: artifact
      mountPath: /data
  volumes:
  - name: artifact
    image:
      reference: quay.io/crio/artifact:v2
      pullPolicy: IfNotPresent
status:
  containerStatuses:
  - containerID: containerd://examplecontainerid1234567890abcdef
    image: docker.io/library/debian:12
    imageID: docker-pullable://docker.io/library/debian@sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
    volumeMounts:
    - name: artifact
      mountPath: /data
      readOnly: true
      imageRef: quay.io/crio/artifact@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

### iscsi

یک حجم `iscsi` اجازه می‌دهد یک حجم iSCSI (SCSI over IP) موجود به درون Pod شما مانت شود. برخلاف `emptyDir` که با حذف Pod پاک می‌شود،
محتوای حجم `iscsi` حفظ می‌شود و حجم صرفاً
از حالت مانت خارج (unmount) می‌شود. این بدان معناست که یک حجم iscsi می‌تواند از قبل با داده پر شود و
این داده‌ها میان Podها به اشتراک گذاشته شوند.

{{< note >}}
پیش از استفاده از آن، باید سرور iSCSI خودتان را اجرا کرده و حجم را روی آن ایجاد کرده باشید.
{{< /note >}}

یکی از ویژگی‌های iSCSI این است که می‌تواند به‌صورت فقط‌خواندنی توسط چندین مصرف‌کننده
به‌طور هم‌زمان مانت شود. این بدان معناست که می‌توانید یک حجم را از قبل با مجموعه داده خود پر کنید
و سپس آن را به‌صورت موازی از هر تعداد Pod که نیاز دارید ارائه دهید. متأسفانه،
حجم‌های iSCSI را در حالت خواندن‌ـ‌نوشتنی تنها یک مصرف‌کننده می‌تواند مانت کند.
نویسنده‌های هم‌زمان مجاز نیستند.

### local

یک حجم `local` یک دستگاه ذخیره‌سازی محلی مانت‌شده مانند دیسک،
پارتیشن یا دایرکتوری را نمایندگی می‌کند.

حجم‌های محلی را فقط می‌توان به‌صورت یک PersistentVolume که به‌طور ایستا ایجاد شده است استفاده کرد. تأمین پویا
(dynamic provisioning) پشتیبانی نمی‌شود.

در مقایسه با حجم‌های `hostPath`، حجم‌های `local` به شیوه‌ای پایدار و
قابل‌حمل استفاده می‌شوند، بدون اینکه نیاز باشد Podها را به‌صورت دستی به نودها زمان‌بندی کنید. سیستم
با بررسی node affinity روی PersistentVolume از محدودیت‌های نود مربوط به حجم آگاه است.

با این حال، حجم‌های `local` وابسته به در دسترس بودن نود زیرین هستند
و برای همه برنامه‌ها مناسب نیستند. اگر نودی ناسالم شود،
حجم `local` برای Pod غیرقابل دسترس می‌شود. Podی که از این حجم استفاده می‌کند
نمی‌تواند اجرا شود. برنامه‌هایی که از حجم‌های `local` استفاده می‌کنند باید بتوانند این
کاهش در دسترس بودن و همچنین از دست رفتن احتمالی داده‌ها را تحمل کنند، که بسته به
ویژگی‌های دوام دیسک زیرین است.

مثال زیر یک PersistentVolume را نشان می‌دهد که از حجم `local` و
`nodeAffinity` استفاده می‌کند:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage
  local:
    path: /mnt/disks/ssd1
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - example-node
```

هنگام استفاده از حجم‌های `local` باید `nodeAffinity` مربوط به PersistentVolume را تنظیم کنید.
زمان‌بند کوبرنتیز از `nodeAffinity` مربوط به PersistentVolume استفاده می‌کند تا
این Podها را به نود صحیح زمان‌بندی کند.

مقدار `volumeMode` در PersistentVolume را می‌توان روی "Block" (به‌جای مقدار پیش‌فرض
"Filesystem") تنظیم کرد تا حجم محلی به‌صورت یک دستگاه بلوکی خام (raw block device) در دسترس قرار گیرد.

هنگام استفاده از حجم‌های محلی، توصیه می‌شود یک StorageClass با
`volumeBindingMode` برابر با `WaitForFirstConsumer` ایجاد کنید. برای جزئیات بیشتر،
مثال [StorageClass](/docs/concepts/storage/storage-classes/#local) محلی را ببینید.
به تأخیر انداختن اتصال حجم (volume binding) تضمین می‌کند که تصمیم اتصال PersistentVolumeClaim
با سایر محدودیت‌های نودی که Pod ممکن است داشته باشد نیز ارزیابی شود،
مانند نیازمندی‌های منابع نود، انتخابگرهای (selector) نود، affinity و anti-affinity مربوط به Pod.

برای مدیریت بهتر چرخه عمر حجم محلی، می‌توان یک تأمین‌کننده ایستای خارجی (external static provisioner) را به‌صورت جداگانه اجرا کرد.
توجه داشته باشید که این provisioner هنوز از تأمین پویا پشتیبانی نمی‌کند. برای مشاهده نمونه‌ای از نحوه اجرای یک provisioner محلی خارجی، به
[راهنمای کاربر local volume provisioner](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) مراجعه کنید.

{{< note >}}
اگر برای مدیریت چرخه عمر حجم از تأمین‌کننده ایستای خارجی استفاده نشود،
PersistentVolume محلی نیازمند پاک‌سازی و حذف دستی توسط کاربر است.
{{< /note >}}

### nfs

یک حجم `nfs` اجازه می‌دهد یک اشتراک NFS (Network File System) موجود
به درون یک Pod مانت شود. برخلاف `emptyDir` که با حذف Pod
پاک می‌شود، محتوای حجم `nfs` حفظ می‌شود و حجم صرفاً
از حالت مانت خارج می‌شود. این بدان معناست که یک حجم NFS می‌تواند از قبل با داده پر شود و
این داده‌ها میان Podها به اشتراک گذاشته شوند. NFS را می‌توان به‌طور هم‌زمان توسط چندین
نویسنده مانت کرد.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /my-nfs-data
      name: test-volume
  volumes:
  - name: test-volume
    nfs:
      server: my-nfs-server.example.com
      path: /my-nfs-volume
      readOnly: true
```

{{< note >}}
پیش از استفاده از آن، باید سرور NFS خودتان را اجرا کرده و اشتراک را export کرده باشید.

همچنین توجه داشته باشید که نمی‌توانید گزینه‌های مانت NFS را در مشخصات Pod تعیین کنید. می‌توانید گزینه‌های مانت را یا در سمت سرور تنظیم کنید یا
از [/etc/nfsmount.conf](https://man7.org/linux/man-pages/man5/nfsmount.conf.5.html) استفاده کنید.
همچنین می‌توانید حجم‌های NFS را از طریق PersistentVolumeها مانت کنید که امکان تنظیم گزینه‌های مانت را فراهم می‌کنند.
{{< /note >}}

### persistentVolumeClaim {#persistentvolumeclaim}

یک حجم `persistentVolumeClaim` برای مانت کردن یک
[PersistentVolume](/docs/concepts/storage/persistent-volumes/) به درون یک Pod استفاده می‌شود. PersistentVolumeClaimها
راهی برای کاربران هستند تا بدون آگاهی از جزئیات محیط ابری خاص،
ذخیره‌سازی پایدار (مانند یک حجم iSCSI) را «درخواست» (claim) کنند.

برای جزئیات بیشتر، اطلاعات مربوط به [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) را ببینید.

### portworxVolume (منسوخ‌شده) {#portworxvolume}

{{< feature-state for_k8s_version="v1.25" state="deprecated" >}}

یک `portworxVolume` لایه‌ای ذخیره‌سازی بلاکی و الاستیک است که به‌صورت hyperconverged همراه با
کوبرنتیز اجرا می‌شود. [Portworx](https://portworx.com/use-case/kubernetes-storage/) ذخیره‌سازی موجود
در یک سرور را شناسایی (fingerprint) می‌کند، آن را بر اساس قابلیت‌ها در لایه‌های مختلف دسته‌بندی می‌کند و ظرفیت چندین سرور را یکپارچه می‌سازد.
Portworx درون ماشین‌های مجازی (in-guest) یا روی نودهای لینوکسی bare metal اجرا می‌شود.

یک `portworxVolume` را می‌توان به‌صورت پویا از طریق کوبرنتیز ایجاد کرد، یا می‌توان آن را
از پیش تأمین (pre-provision) کرد و درون یک Pod به آن ارجاع داد.
در ادامه نمونه‌ای از یک Pod آمده است که به یک حجم Portworx از پیش تأمین‌شده ارجاع می‌دهد:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-portworx-volume-pod
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /mnt
      name: pxvol
  volumes:
  - name: pxvol
    # This Portworx volume must already exist.
    portworxVolume:
      volumeID: "pxvol"
      fsType: "<fs-type>"
```

{{< note >}}
پیش از استفاده از PortworxVolume در Pod، مطمئن شوید که یک PortworxVolume موجود با نام `pxvol` دارید.
{{< /note >}}


#### مهاجرت CSI برای Portworx {#portworx-csi-migration}
{{< feature-state feature_gate_name="CSIMigrationPortworx" >}}

در کوبرنتیز {{% skew currentVersion %}}، تمام عملیات مربوط به حجم‌های Portworx درون‌درخت (in-tree)
به‌طور پیش‌فرض به درایور `pxd.portworx.com` از نوع
Container Storage Interface (CSI) هدایت می‌شوند.
[درایور Portworx CSI](https://docs.portworx.com/portworx-enterprise/operations/operate-kubernetes/storage-operations/csi)
باید روی کلاستر نصب شده باشد.

### projected

یک حجم projected چندین منبع حجم موجود را در یک دایرکتوری یکسان نگاشت می‌کند. برای جزئیات بیشتر، به [حجم‌های projected](/docs/concepts/storage/projected-volumes/) مراجعه کنید.

### secret

یک حجم `secret` برای انتقال اطلاعات حساس، مانند گذرواژه‌ها، به
Podها استفاده می‌شود. می‌توانید secretها را در API کوبرنتیز ذخیره کنید و آن‌ها را به‌صورت فایل برای
استفاده Podها mount کنید، بدون آنکه مستقیماً به کوبرنتیز وابسته شوید. حجم‌های `secret` بر پایه
tmpfs (یک فایل‌سیستم مبتنی بر RAM) هستند، بنابراین هرگز روی
ذخیره‌سازی غیرفرار نوشته نمی‌شوند.

{{< note >}}

* پیش از آنکه بتوانید از یک Secret استفاده کنید، باید آن را در API کوبرنتیز ایجاد کنید.

* یک Secret همیشه به‌صورت `readOnly` mount می‌شود.

* کانتینری که از یک Secret به‌عنوان mount حجمِ [`subPath`](#using-subpath) استفاده می‌کند،
  به‌روزرسانی‌های Secret را دریافت نخواهد کرد.

{{< /note >}}

برای جزئیات بیشتر، به [پیکربندی Secretها](/docs/concepts/configuration/secret/) مراجعه کنید.

## استفاده از subPath {#using-subpath}

گاهی اوقات مفید است که یک حجم برای چند کاربرد در یک Pod به اشتراک گذاشته شود.
ویژگی `volumeMounts[*].subPath` به‌جای ریشه حجم، یک زیرمسیر درون حجم ارجاع‌شده را مشخص می‌کند.

مثال زیر نشان می‌دهد چگونه یک Pod را با پشته LAMP (لینوکس، Apache، MySQL، PHP)
و با استفاده از یک حجم مشترک واحد پیکربندی کنید. این پیکربندی نمونه‌ی `subPath` برای
استفاده در محیط تولید توصیه نمی‌شود.

کد و دارایی‌های (assets) برنامه PHP به پوشه `html` حجم نگاشت می‌شوند و
پایگاه‌داده MySQL در پوشه `mysql` حجم ذخیره می‌شود. برای مثال:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-lamp-site
spec:
    containers:
    - name: mysql
      image: mysql
      env:
      - name: MYSQL_ROOT_PASSWORD
        value: "rootpasswd"
      volumeMounts:
      - mountPath: /var/lib/mysql
        name: site-data
        subPath: mysql
    - name: php
      image: php:7.0-apache
      volumeMounts:
      - mountPath: /var/www/html
        name: site-data
        subPath: html
    volumes:
    - name: site-data
      persistentVolumeClaim:
        claimName: my-lamp-site-data
```

### استفاده از subPath همراه با متغیرهای محیطی بسط‌یافته {#using-subpath-expanded-environment}

{{< feature-state for_k8s_version="v1.17" state="stable" >}}

از فیلد `subPathExpr` برای ساخت نام دایرکتوری‌های `subPath` از
متغیرهای محیطی downward API استفاده کنید.
ویژگی‌های `subPath` و `subPathExpr` متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان به کار برد.

در این مثال، یک `Pod` از `subPathExpr` برای ایجاد دایرکتوری `pod1` درون
حجم `hostPath` با مسیر `/var/log/pods` استفاده می‌کند.
حجم `hostPath` نام `Pod` را از `downwardAPI` می‌گیرد.
دایرکتوری میزبان `/var/log/pods/pod1` در مسیر `/logs` درون کانتینر mount می‌شود.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  containers:
  - name: container1
    env:
    - name: POD_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    image: busybox:1.28
    command: [ "sh", "-c", "while [ true ]; do echo 'Hello'; sleep 10; done | tee -a /logs/hello.txt" ]
    volumeMounts:
    - name: workdir1
      mountPath: /logs
      # The variable expansion uses round brackets (not curly brackets).
      subPathExpr: $(POD_NAME)
  restartPolicy: Never
  volumes:
  - name: workdir1
    hostPath:
      path: /var/log/pods
```

## منابع {#resources}

رسانه ذخیره‌سازی (مانند دیسک یا SSD) یک حجم `emptyDir` بر اساس
رسانه‌ی فایل‌سیستمی تعیین می‌شود که دایرکتوری ریشه kubelet (معمولاً
`/var/lib/kubelet`) را در خود دارد. هیچ محدودیتی برای میزان فضایی که یک حجم `emptyDir` یا
`hostPath` می‌تواند مصرف کند وجود ندارد و هیچ ایزولاسیونی میان کانتینرها یا
Podها در کار نیست.

برای آشنایی با درخواست فضا با استفاده از مشخصات منبع (resource specification)، به
[نحوه مدیریت منابع](/docs/concepts/configuration/manage-resources-containers/) مراجعه کنید.

## افزونه‌های حجم خارج از درخت (Out-of-tree) {#out-of-tree-volume-plugins}

افزونه‌های حجم خارج از درخت شامل
{{< glossary_tooltip text="Container Storage Interface" term_id="csi" >}} (CSI) و همچنین
FlexVolume (که منسوخ شده است) می‌شوند. این افزونه‌ها به فروشندگان ذخیره‌سازی امکان می‌دهند افزونه‌های ذخیره‌سازی سفارشی بسازند،
بدون آنکه کد منبع افزونه خود را به مخزن کد کوبرنتیز اضافه کنند.

پیش‌تر، همه افزونه‌های حجم «درون‌درخت» (in-tree) بودند. افزونه‌های «درون‌درخت» همراه با باینری‌های هسته کوبرنتیز
ساخته، لینک، کامپایل و توزیع می‌شدند. این بدان معنا بود که افزودن یک سامانه ذخیره‌سازی جدید به
کوبرنتیز (یک افزونه حجم) مستلزم ثبت کد در مخزن کد هسته کوبرنتیز بود.

هم CSI و هم FlexVolume اجازه می‌دهند افزونه‌های حجم مستقل از
کدبیس کوبرنتیز توسعه یابند و به‌عنوان افزونه (extension) روی کلاسترهای کوبرنتیز مستقر (نصب) شوند.

فروشندگان ذخیره‌سازی که قصد ساخت یک افزونه حجم خارج از درخت را دارند، می‌توانند به
[پرسش‌های متداول افزونه حجم](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md) مراجعه کنند.

### csi

[Container Storage Interface](https://github.com/container-storage-interface/spec/blob/master/spec.md)
(CSI) یک رابط استاندارد برای سامانه‌های هماهنگ‌سازی کانتینر (مانند
کوبرنتیز) تعریف می‌کند تا سامانه‌های ذخیره‌سازی دلخواه را در اختیار بارهای کاری کانتینری خود قرار دهند.

برای اطلاعات بیشتر، [پیشنهاد طراحی CSI](https://git.k8s.io/design-proposals-archive/storage/container-storage-interface.md)
را مطالعه کنید.

{{< note >}}
پشتیبانی از نسخه‌های 0.2 و 0.3 مشخصات CSI در کوبرنتیز
v1.13 منسوخ شده و در یک نسخه آینده حذف خواهد شد.
{{< /note >}}

{{< note >}}
ممکن است درایورهای CSI با همه نسخه‌های کوبرنتیز سازگار نباشند.
لطفاً برای مشاهده مراحل استقرار پشتیبانی‌شده برای هر نسخه کوبرنتیز و جدول سازگاری،
مستندات درایور CSI مورد نظر را بررسی کنید.
{{< /note >}}

پس از آنکه یک درایور حجم سازگار با CSI روی یک کلاستر کوبرنتیز مستقر شد، کاربران
می‌توانند از نوع حجم `csi` برای attach یا mount کردن حجم‌هایی که توسط
درایور CSI ارائه می‌شوند استفاده کنند.

یک حجم `csi` را می‌توان به سه روش مختلف در یک Pod به کار برد:

* از طریق ارجاع به یک [PersistentVolumeClaim](#persistentvolumeclaim)
* با یک [حجم ephemeral عمومی](/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes)
* با یک [حجم ephemeral از نوع CSI](/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes)
  در صورتی که درایور از آن پشتیبانی کند

فیلدهای زیر برای پیکربندی یک حجم پایدار (persistent volume) از نوع CSI در اختیار مدیران ذخیره‌سازی قرار دارند:

* `driver`: یک مقدار رشته‌ای که نام درایور حجم مورد استفاده را مشخص می‌کند.
  این مقدار باید با مقداری که درایور CSI در `GetPluginInfoResponse` برمی‌گرداند و در
  [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#getplugininfo)
  تعریف شده است، مطابقت داشته باشد.
  کوبرنتیز از آن برای شناسایی اینکه کدام درایور CSI باید فراخوانی شود استفاده می‌کند، و مؤلفه‌های
  درایور CSI نیز از آن برای شناسایی اینکه کدام آبجکت‌های PV به درایور CSI تعلق دارند بهره می‌برند.
* `volumeHandle`: یک مقدار رشته‌ای که حجم را به‌طور یکتا شناسایی می‌کند. این مقدار
  باید با مقداری که درایور CSI در فیلد `volume.id` از
  `CreateVolumeResponse` برمی‌گرداند و در
  [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#createvolume) تعریف شده است، مطابقت داشته باشد.
  هنگام ارجاع به حجم، این مقدار در تمام فراخوانی‌ها به درایور حجم CSI به‌صورت `volume_id` ارسال می‌شود.
* `readOnly`: یک مقدار بولین اختیاری که مشخص می‌کند آیا حجم باید به‌صورت فقط‌خواندنی
  «ControllerPublished» (attach) شود یا خیر. مقدار پیش‌فرض false است. این مقدار
  از طریق فیلد `readonly` در `ControllerPublishVolumeRequest` به درایور CSI ارسال می‌شود.
* `fsType`: اگر `VolumeMode` مربوط به PV برابر `Filesystem` باشد، می‌توان از این فیلد
  برای تعیین فایل‌سیستمی که باید برای mount کردن حجم استفاده شود بهره برد. اگر
  حجم فرمت نشده باشد و فرمت‌کردن پشتیبانی شود، این مقدار
  برای فرمت‌کردن حجم به کار می‌رود.
  این مقدار از طریق فیلد `VolumeCapability` در
  `ControllerPublishVolumeRequest`، `NodeStageVolumeRequest` و
  `NodePublishVolumeRequest` به درایور CSI ارسال می‌شود.
* `volumeAttributes`: یک نگاشت از رشته به رشته که ویژگی‌های ایستای
  یک حجم را مشخص می‌کند. این نگاشت باید با نگاشتی که درایور CSI در فیلد
  `volume.attributes` از `CreateVolumeResponse` برمی‌گرداند و در
  [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#createvolume) تعریف شده است، مطابقت داشته باشد.
  این نگاشت از طریق فیلد `volume_context` در
  `ControllerPublishVolumeRequest`، `NodeStageVolumeRequest` و
  `NodePublishVolumeRequest` به درایور CSI ارسال می‌شود.
* `controllerPublishSecretRef`: ارجاعی به آبجکت secret که حاوی
  اطلاعات حساسی است که برای تکمیل فراخوانی‌های CSI با نام
  `ControllerPublishVolume` و `ControllerUnpublishVolume` به درایور CSI ارسال می‌شود. این فیلد
  اختیاری است و در صورتی که secret موردنیاز نباشد می‌تواند خالی بماند. اگر Secret
  بیش از یک secret داشته باشد، همه secretها ارسال می‌شوند.
* `nodeExpandSecretRef`: ارجاعی به secret که حاوی اطلاعات حساسی است
  که برای تکمیل فراخوانی CSI با نام
  `NodeExpandVolume` به درایور CSI ارسال می‌شود. این فیلد اختیاری است و در صورتی که
  secret موردنیاز نباشد می‌تواند خالی بماند. اگر آبجکت بیش از یک secret داشته باشد، همه
  secretها ارسال می‌شوند. هنگامی که داده‌های secret را برای گسترش حجم آغازشده توسط نود
  پیکربندی کرده باشید، kubelet آن داده‌ها را از طریق فراخوانی `NodeExpandVolume()`
  به درایور CSI ارسال می‌کند. همه نسخه‌های پشتیبانی‌شده کوبرنتیز فیلد
  `nodeExpandSecretRef` را ارائه می‌دهند و به‌طور پیش‌فرض در دسترس است. نسخه‌های کوبرنتیز
  پیش از v1.25 این پشتیبانی را نداشتند.
* [feature gate](/docs/reference/command-line-tools-reference/feature-gates-removed/)
  با نام `CSINodeExpandSecret` را برای هر kube-apiserver و برای kubelet روی هر
  نود فعال کنید. از کوبرنتیز نسخه 1.27 به بعد، این قابلیت به‌طور پیش‌فرض فعال است
  و نیازی به فعال‌سازی صریح feature gate نیست.
  همچنین باید از درایور CSI‌ای استفاده کنید که در عملیات تغییر اندازه ذخیره‌سازی آغازشده توسط نود،
  از داده‌های secret پشتیبانی می‌کند یا آن‌ها را الزامی می‌داند.
* `nodePublishSecretRef`: ارجاعی به آبجکت secret که حاوی
  اطلاعات حساسی است که برای تکمیل فراخوانی CSI با نام
  `NodePublishVolume` به درایور CSI ارسال می‌شود. این فیلد اختیاری است و در صورتی که
  secret موردنیاز نباشد می‌تواند خالی بماند. اگر آبجکت secret بیش از یک secret داشته باشد، همه
  secretها ارسال می‌شوند.
* `nodeStageSecretRef`: ارجاعی به آبجکت secret که حاوی
  اطلاعات حساسی است که برای تکمیل فراخوانی CSI با نام
  `NodeStageVolume` به درایور CSI ارسال می‌شود. این فیلد اختیاری است و در صورتی که secret
  موردنیاز نباشد می‌تواند خالی بماند. اگر Secret بیش از یک secret داشته باشد، همه secretها
  ارسال می‌شوند.

#### پشتیبانی از حجم بلاکی خام (raw block) در CSI {#csi-raw-block-volume-support}

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

فروشندگانی که درایورهای CSI خارجی دارند می‌توانند پشتیبانی از حجم بلاکی خام را
در بارهای کاری کوبرنتیز پیاده‌سازی کنند.

می‌توانید
[PersistentVolume/PersistentVolumeClaim را با پشتیبانی از حجم بلاکی خام](/docs/concepts/storage/persistent-volumes/#raw-block-volume-support)
مانند همیشه و بدون هیچ تغییر مختص CSI راه‌اندازی کنید.

#### حجم‌های ephemeral در CSI {#csi-ephemeral-volumes}

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

می‌توانید حجم‌های CSI را مستقیماً درون مشخصات Pod پیکربندی کنید.
حجم‌هایی که به این روش مشخص می‌شوند ephemeral هستند و با راه‌اندازی مجدد Pod
باقی نمی‌مانند. برای اطلاعات بیشتر، به
[حجم‌های Ephemeral](/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes)
مراجعه کنید.

برای اطلاعات بیشتر درباره نحوه توسعه یک درایور CSI، به
[مستندات kubernetes-csi](https://kubernetes-csi.github.io/docs/) مراجعه کنید.

#### Windows CSI proxy {#windows-csi-proxy}

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

افزونه‌های نود CSI باید عملیات ممتاز (privileged) متعددی مانند اسکن دستگاه‌های دیسک
و mount کردن فایل‌سیستم‌ها را انجام دهند. این عملیات برای هر سیستم‌عامل میزبان
متفاوت است. برای نودهای کارگر لینوکسی، افزونه‌های نود CSI کانتینری معمولاً
به‌صورت کانتینرهای ممتاز مستقر می‌شوند. برای نودهای کارگر ویندوزی،
عملیات ممتاز افزونه‌های نود CSI کانتینری با استفاده از
[csi-proxy](https://github.com/kubernetes-csi/csi-proxy) پشتیبانی می‌شود؛ این ابزار یک باینری مستقل
و تحت مدیریت جامعه کاربری است که باید از پیش روی هر نود ویندوزی نصب شود.

برای جزئیات بیشتر، به راهنمای استقرار افزونه CSI‌ای که می‌خواهید مستقر کنید مراجعه کنید.

#### مهاجرت از افزونه‌های درون‌درخت به درایورهای CSI {#migrating-to-csi-drivers-from-in-tree-plugins}

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

قابلیت `CSIMigration` عملیات مربوط به افزونه‌های درون‌درخت موجود را
به افزونه‌های CSI متناظر هدایت می‌کند (که انتظار می‌رود نصب و پیکربندی شده باشند).
در نتیجه، اپراتورها هنگام گذار به درایور CSI‌ای که جایگزین یک افزونه درون‌درخت می‌شود، لازم نیست هیچ تغییری
در پیکربندی StorageClassها، PersistentVolumeها یا PersistentVolumeClaimهای موجود
(که به افزونه‌های درون‌درخت ارجاع می‌دهند) اعمال کنند.

{{< note >}}
PVهای موجودی که توسط یک افزونه حجم درون‌درخت ایجاد شده‌اند، در آینده نیز بدون هیچ تغییر پیکربندی قابل استفاده خواهند بود،
حتی پس از تکمیل مهاجرت به CSI برای آن نوع حجم، و حتی پس از ارتقا به
نسخه‌ای از کوبرنتیز که پشتیبانی کامپایل‌شده برای آن نوع ذخیره‌سازی را ندارد.

به‌عنوان بخشی از آن مهاجرت، شما - یا مدیر دیگری از کلاستر - **باید** درایور CSI
مناسب را برای آن ذخیره‌سازی نصب و پیکربندی کرده باشید. هسته کوبرنتیز آن نرم‌افزار را برای شما نصب نمی‌کند.

---

پس از آن مهاجرت، همچنین می‌توانید PVC و PVهای جدیدی تعریف کنید که به یکپارچه‌سازی‌های ذخیره‌سازی
قدیمی و توکار ارجاع می‌دهند.
مشروط بر اینکه درایور CSI مناسب نصب و پیکربندی شده باشد، ایجاد PV همچنان کار می‌کند،
حتی برای حجم‌های کاملاً جدید. مدیریت واقعی ذخیره‌سازی اکنون از طریق
درایور CSI انجام می‌شود.
{{< /note >}}

عملیات و قابلیت‌های پشتیبانی‌شده شامل موارد زیر است:
تأمین/حذف (provisioning/delete)، اتصال/جداسازی (attach/detach)، mount/unmount و تغییر اندازه حجم‌ها.

افزونه‌های درون‌درختی که از `CSIMigration` پشتیبانی می‌کنند و درایور CSI متناظر برای آن‌ها پیاده‌سازی شده است،
در [انواع حجم‌ها](#volume-types) فهرست شده‌اند.

### flexVolume (منسوخ‌شده)   {#flexvolume}

{{< feature-state for_k8s_version="v1.23" state="deprecated" >}}

FlexVolume یک رابط افزونه خارج از درخت است که از یک مدل مبتنی بر exec برای ارتباط
با درایورهای ذخیره‌سازی استفاده می‌کند. باینری‌های درایور FlexVolume باید در یک
مسیر افزونه حجم از پیش تعریف‌شده روی هر نود، و در برخی موارد روی نودهای control plane نیز، نصب شوند.

Podها از طریق افزونه حجم درون‌درخت `flexVolume` با درایورهای FlexVolume تعامل می‌کنند.

[افزونه‌های](https://github.com/Microsoft/K8s-Storage-Plugins/tree/master/flexvolume/windows) FlexVolume زیر
که به‌صورت اسکریپت‌های PowerShell روی میزبان مستقر می‌شوند، از نودهای ویندوزی پشتیبانی می‌کنند:

* [SMB](https://github.com/microsoft/K8s-Storage-Plugins/tree/master/flexvolume/windows/plugins/microsoft.com~smb.cmd)
* [iSCSI](https://github.com/microsoft/K8s-Storage-Plugins/tree/master/flexvolume/windows/plugins/microsoft.com~iscsi.cmd)

{{< note >}}
FlexVolume منسوخ شده است. استفاده از یک درایور CSI خارج از درخت، روش توصیه‌شده برای یکپارچه‌سازی ذخیره‌سازی خارجی با کوبرنتیز است.

نگهدارندگان درایور FlexVolume باید یک درایور CSI پیاده‌سازی کنند و به مهاجرت کاربران درایورهای FlexVolume به CSI کمک کنند.
کاربران FlexVolume باید بارهای کاری خود را به‌گونه‌ای منتقل کنند که از درایور CSI معادل استفاده کنند.
{{< /note >}}

## انتشار mount (Mount propagation)

{{< caution >}}
انتشار mount یک قابلیت سطح پایین است که روی همه انواع حجم (volume) به‌صورت یکسان کار نمی‌کند. پروژه کوبرنتیز توصیه می‌کند که از انتشار mount فقط با حجم‌های `hostPath` یا `emptyDir` مبتنی بر حافظه استفاده شود. برای اطلاعات بیشتر به
[Kubernetes issue #95049](https://github.com/kubernetes/kubernetes/issues/95049)
مراجعه کنید.
{{< /caution >}}

انتشار mount امکان می‌دهد حجم‌هایی که توسط یک کانتینر mount شده‌اند، با کانتینرهای دیگر در همان Pod یا حتی با Podهای دیگر روی همان نود به اشتراک گذاشته شوند.

انتشار mount یک حجم توسط فیلد `mountPropagation` در `containers[*].volumeMounts` کنترل می‌شود. مقادیر آن عبارت‌اند از:

* `None` - این mount حجم، هیچ mount بعدی‌ای را که توسط میزبان روی این حجم یا هر یک از زیرپوشه‌های آن انجام شود دریافت نخواهد کرد.
  به همین ترتیب، هیچ mount ایجادشده توسط کانتینر روی میزبان قابل مشاهده نخواهد بود. این حالت پیش‌فرض است.

  این حالت معادل انتشار mount از نوع `rprivate` است، همان‌گونه که در
  [`mount(8)`](https://man7.org/linux/man-pages/man8/mount.8.html)
  توضیح داده شده است.

  با این حال، اگر انتشار `rprivate` قابل اعمال نباشد، ممکن است محیط اجرایی CRI انتشار mount از نوع `rslave` (یعنی `HostToContainer`) را انتخاب کند.
  cri-dockerd (Docker) شناخته‌شده است که وقتی منبع mount شامل دایرکتوری ریشه daemon داکر (`/var/lib/docker`) باشد، انتشار mount از نوع `rslave` را انتخاب می‌کند.

* `HostToContainer` - این mount حجم، تمام mountهای بعدی را که روی این حجم یا هر یک از زیرپوشه‌های آن انجام شوند دریافت خواهد کرد.

  به بیان دیگر، اگر میزبان چیزی را داخل mount حجم، mount کند، کانتینر آن را در همان‌جا mount شده خواهد دید.

  به همین ترتیب، اگر هر Pod با انتشار mount از نوع `Bidirectional` روی همان حجم چیزی را mount کند، کانتینری که انتشار mount آن `HostToContainer` است آن را خواهد دید.

  این حالت معادل انتشار mount از نوع `rslave` است، همان‌گونه که در
  [`mount(8)`](https://man7.org/linux/man-pages/man8/mount.8.html)
  توضیح داده شده است.

* `Bidirectional` - این mount حجم همانند mount از نوع `HostToContainer` رفتار می‌کند.
  علاوه بر آن، تمام mountهای حجم که توسط کانتینر ایجاد می‌شوند به میزبان و به همه کانتینرهای همه Podهایی که از همان حجم استفاده می‌کنند، منتشر می‌شوند.

  یک مورد استفاده معمول برای این حالت، Pod دارای FlexVolume یا درایور CSI است، یا Podی که لازم است با استفاده از یک حجم `hostPath` چیزی را روی میزبان mount کند.

  این حالت معادل انتشار mount از نوع `rshared` است، همان‌گونه که در
  [`mount(8)`](https://man7.org/linux/man-pages/man8/mount.8.html)
  توضیح داده شده است.

  {{< warning >}}
  انتشار mount از نوع `Bidirectional` می‌تواند خطرناک باشد. این حالت می‌تواند به سیستم‌عامل میزبان آسیب برساند و به همین دلیل فقط در کانتینرهای دارای دسترسی ویژه (privileged) مجاز است. آشنایی با رفتار هسته لینوکس به‌شدت توصیه می‌شود.
  علاوه بر این، هر mount حجمی که توسط کانتینرهای داخل Podها ایجاد شده باشد، باید هنگام پایان کار کانتینر توسط همان کانتینرها از بین برده شود (unmount شود).
  {{< /warning >}}

## mountهای فقط‌خواندنی

می‌توان با تنظیم فیلد `.spec.containers[*].volumeMounts[*].readOnly` روی `true`، یک mount را فقط‌خواندنی کرد.
این کار خود حجم را فقط‌خواندنی نمی‌کند، اما همان کانتینر خاص قادر به نوشتن روی آن نخواهد بود.
کانتینرهای دیگر در Pod می‌توانند همان حجم را به‌صورت خواندنی-نوشتنی mount کنند.

در لینوکس، mountهای فقط‌خواندنی به‌طور پیش‌فرض به‌صورت بازگشتی فقط‌خواندنی نیستند.
برای مثال، Podی را در نظر بگیرید که مسیر `/mnt` میزبان را به‌صورت یک حجم `hostPath` mount می‌کند. اگر سیستم فایل دیگری (مانند tmpfs، NFS یا ذخیره‌ساز USB) به‌صورت خواندنی-نوشتنی روی `/mnt/<SUBMOUNT>` mount شده باشد، حجمی که داخل کانتینر(ها) mount شده است نیز دارای `/mnt/<SUBMOUNT>` قابل نوشتن خواهد بود، حتی اگر خود mount به‌صورت فقط‌خواندنی مشخص شده باشد.

### mountهای فقط‌خواندنی بازگشتی

{{< feature-state feature_gate_name="RecursiveReadOnlyMounts" >}}

mountهای فقط‌خواندنی بازگشتی را می‌توان با فعال‌کردن
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) به نام
`RecursiveReadOnlyMounts` برای kubelet و kube-apiserver، و تنظیم فیلد `.spec.containers[*].volumeMounts[*].recursiveReadOnly`
برای یک Pod فعال کرد.

مقادیر مجاز عبارت‌اند از:

* `Disabled` (پیش‌فرض): بدون اثر.

* `Enabled`: mount را به‌صورت بازگشتی فقط‌خواندنی می‌کند.
  لازم است همه الزامات زیر برآورده شوند:

  * `readOnly` روی `true` تنظیم شده باشد
  * `mountPropagation` تنظیم نشده یا روی `None` تنظیم شده باشد
  * میزبان با هسته لینوکس نسخه 5.12 یا بالاتر اجرا شود
  * محیط اجرایی کانتینر [در سطح CRI](/docs/concepts/architecture/cri) از mountهای فقط‌خواندنی بازگشتی پشتیبانی کند
  * محیط اجرایی کانتینر در سطح OCI از mountهای فقط‌خواندنی بازگشتی پشتیبانی کند.

  اگر هر یک از این موارد برقرار نباشد، با شکست مواجه می‌شود.

* `IfPossible`: تلاش می‌کند `Enabled` را اعمال کند و در صورتی که این قابلیت توسط هسته یا runtime class پشتیبانی نشود، به `Disabled` بازمی‌گردد.

مثال:
{{% code_sample file="storage/rro.yaml" %}}

زمانی که این ویژگی توسط kubelet و kube-apiserver شناسایی شود، فیلد `.status.containerStatuses[*].volumeMounts[*].recursiveReadOnly` روی `Enabled` یا `Disabled` تنظیم می‌شود.

## مالک فایل

### مالکیت گروهی (GID)

مالکیت گروهی فایل‌های حجم (GID) توسط `spec.securityContext.fsGroup` در Pod کنترل می‌شود.

برای مشاهده مراحل دقیق پیکربندی، به
[پیکربندی Security Context برای یک Pod یا کانتینر](/docs/tasks/configure-pod-container/security-context/)
مراجعه کنید.

### مالکیت کاربری (UID)

{{< feature-state feature_gate_name="AtomicWriteVolumeUserFields" >}}

فعال‌کردن [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) به نام `AtomicWriteVolumeUserFields`
فیلدهای مالکیت کاربری فایل (UID) را برای حجم‌های `configMap`، `secret`، `downwardAPI` و `projected` فعال می‌کند.

هنگامی که `defaultUser` در سطح حجم مشخص شود، UID مالک را برای همه فایل‌های داده آن در زمان ایجاد تنظیم می‌کند.
در سطح هر آیتم، فیلد `user` مالک UID یک فایل مجزا را کنترل می‌کند و بر `defaultUser` اولویت دارد.

مثال:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: volume-user-fields-example
spec:
  containers:
  - name: test
    image: busybox:1.28
    command: ['sh', '-c', 'echo "The app is running!" && tail -f /dev/null']
    volumeMounts:
    - name: volA
      mountPath: /mnt/volA
    - name: volB
      mountPath: /mnt/volB
    - name: volC
      mountPath: /mnt/volC
  volumes:
  - name: volA
    configMap:
      defaultUser: 1000
      name: cm1
      items:
      - key: foo # Owner=defaultUser
        path: foo
      - key: bar # Owner=user
        path: bar
        user: 1001
  - name: volB
    secret: # Owner=defaultUser
      defaultUser: 1000
      secretName: secret1
  - name: volC
    projected:
      sources:
      - secret:
          name: secret2
          items:
          - key: moo # Owner=root
            path: moo
          - key: baa # Owner=user
            path: baa
            user: 1000
```

#### پیاده‌سازی‌ها {#implementations-rro}

{{% thirdparty-content %}}

محیط‌های اجرایی کانتینر زیر به‌عنوان پشتیبان mountهای فقط‌خواندنی بازگشتی شناخته می‌شوند.

در سطح CRI:

- [containerd](https://containerd.io/)، از نسخه 2.0
- [CRI-O](https://cri-o.io/)، از نسخه 1.30

در سطح OCI:

- [runc](https://runc.io/)، از نسخه 1.1
- [crun](https://github.com/containers/crun)، از نسخه 1.8.6

## گزینه‌های bind mount

{{< feature-state feature_gate_name="VolumeBindMountOptions" >}}

فیلد `.spec.containers[*].volumeMounts[*].bindMountOptions` به شما امکان می‌دهد پرچم‌های (flag) bind mount لینوکس مرتبط با امنیت را روی هر mount حجم اعمال کنید. مقادیر مجاز عبارت‌اند از:

* `noexec` - از اجرای فایل‌های باینری روی حجم mountشده جلوگیری می‌کند
* `nodev` - فایل‌های ویژه دستگاه را روی حجم mountشده نادیده می‌گیرد
* `nosuid` - بیت‌های set-user-identifier یا set-group-identifier را روی حجم mountشده نادیده می‌گیرد

این گزینه‌ها به‌ازای هر کانتینر اعمال می‌شوند؛ بنابراین کانتینرهای مختلف در همان Pod می‌توانند همان حجم را با گزینه‌های bind mount متفاوت mount کنند. این فیلد با
[حجم‌های ایمیج](#image) پشتیبانی نمی‌شود.

{{< note >}}
محیط اجرایی کانتینر (مانند containerd یا CRI-O) باید از فیلد `mount_options` در پیام `Mount` مربوط به CRI پشتیبانی کند. اگر محیط اجرایی اعلام پشتیبانی نکند، kubelet Podهایی را که از `bindMountOptions` استفاده می‌کنند رد می‌کند. این فیلد روی نودهای ویندوز اثری ندارد.
{{< /note >}}

## {{% heading "whatsnext" %}}

یک مثال از [استقرار WordPress و MySQL با Persistent Volumeها](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/) را دنبال کنید.
