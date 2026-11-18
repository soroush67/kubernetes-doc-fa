---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
title: حجم‌ها (Volumes)
api_metadata:
- apiVersion: ""
  kind: "Volume"
content_type: concept
weight: 10
---

<!-- overview -->

_حجم‌ها_ (volumes) در کوبرنتیز راهی فراهم می‌کنند تا کانتینرهای یک {{< glossary_tooltip text="Pod" term_id="pod" >}} بتوانند از طریق سیستم فایل به داده‌ها دسترسی داشته باشند و آن‌ها را به اشتراک بگذارند. انواع مختلفی از حجم وجود دارد که می‌توانید آن‌ها را برای مقاصد گوناگون به کار ببرید؛ برای نمونه:

- ساختن یک فایل پیکربندی بر پایهٔ یک {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}}
  یا یک {{< glossary_tooltip text="Secret" term_id="secret" >}}
- فراهم کردن فضای کاری موقت برای یک Pod
- به اشتراک گذاشتن یک سیستم فایل میان دو کانتینر متفاوت در یک Pod
- به اشتراک گذاشتن یک سیستم فایل میان دو Pod متفاوت (حتی اگر آن Podها روی نودهای مختلفی اجرا شوند)
- ذخیره‌سازی ماندگار داده‌ها، به‌گونه‌ای که حتی در صورت راه‌اندازی مجدد یا جایگزینی Pod نیز در دسترس بمانند
- انتقال اطلاعات پیکربندی به برنامه‌ای که در یک کانتینر اجرا می‌شود، بر پایهٔ جزئیات Podی که کانتینر در آن قرار دارد
  (برای نمونه: اعلام اینکه Pod در کدام فضای نام (namespace) اجرا می‌شود به یک {{< glossary_tooltip text="کانتینر جانبی" term_id="sidecar-container" >}})
- فراهم کردن دسترسی فقط‌خواندنی به داده‌های موجود در یک ایمیج کانتینر دیگر

اشتراک‌گذاری داده می‌تواند میان فرایندهای محلی مختلف درون یک کانتینر، میان کانتینرهای مختلف یا میان Podها انجام شود.

## چرا حجم‌ها اهمیت دارند

- **ماندگاری داده‌ها:** فایل‌های روی دیسک در یک کانتینر گذرا هستند و همین موضوع برای برنامه‌های پیچیده‌ای که در کانتینر اجرا می‌شوند مشکلاتی ایجاد می‌کند. یکی از این مشکلات زمانی رخ می‌دهد که کانتینر از کار بیفتد یا متوقف شود؛ در این حالت وضعیت کانتینر ذخیره نمی‌شود و همهٔ فایل‌هایی که در طول عمر کانتینر ایجاد یا تغییر داده شده‌اند از دست می‌روند. پس از ازکارافتادن، kubelet کانتینر را با وضعیتی پاک و از نو راه‌اندازی می‌کند.

- **ذخیره‌سازی مشترک:** مشکل دیگر زمانی پیش می‌آید که چند کانتینر در یک `Pod` اجرا می‌شوند و باید فایل‌هایی را با یکدیگر به اشتراک بگذارند. راه‌اندازی یک سیستم فایل مشترک و دسترسی به آن از همهٔ کانتینرها می‌تواند دشوار باشد.

مفهوم انتزاعی {{< glossary_tooltip text="حجم" term_id="volume" >}} در کوبرنتیز می‌تواند به شما در حل هر دو مشکل کمک کند.

پیش از آشنایی با حجم‌ها، PersistentVolumeها و PersistentVolumeClaimها، بهتر است دربارهٔ {{< glossary_tooltip term_id="Pod" text="Podها" >}} مطالعه کنید و مطمئن شوید که می‌دانید کوبرنتیز چگونه از Podها برای اجرای کانتینرها استفاده می‌کند.
  
<!-- body -->

## حجم‌ها چگونه کار می‌کنند

کوبرنتیز از انواع بسیاری از حجم‌ها پشتیبانی می‌کند. هر {{< glossary_tooltip term_id="pod" text="Pod" >}} می‌تواند هم‌زمان از هر تعداد نوع حجم استفاده کند.
طول عمر انواع [حجم‌های گذرا](/docs/concepts/storage/ephemeral-volumes/) به یک Pod مشخص وابسته است، اما [حجم‌های ماندگار](/docs/concepts/storage/persistent-volumes/) فراتر از طول عمر هر Pod منفرد باقی می‌مانند. هنگامی که یک Pod از بین می‌رود، کوبرنتیز حجم‌های گذرا را نابود می‌کند، اما حجم‌های ماندگار را نابود نمی‌کند.
در هر نوع حجمی که در یک Pod وجود دارد، داده‌ها در طول راه‌اندازی‌های مجدد کانتینر حفظ می‌شوند.

در اصل، حجم یک دایرکتوری است که ممکن است داده‌هایی در آن باشد و کانتینرهای یک Pod به آن دسترسی دارند. اینکه این دایرکتوری چگونه پدید می‌آید، چه رسانه‌ای پشتوانهٔ آن است و چه محتوایی دارد، به نوع حجم مورد استفاده بستگی دارد.

برای استفاده از یک حجم، حجم‌هایی را که باید در اختیار Pod قرار گیرند در `.spec.volumes` مشخص کنید و محل اتصال (mount) آن حجم‌ها در کانتینرها را در `.spec.containers[*].volumeMounts` تعریف کنید.

هنگامی که یک Pod اجرا می‌شود، فرایند درون کانتینر نمایی از سیستم فایل می‌بیند که از محتوای اولیهٔ {{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} به‌اضافهٔ حجم‌های متصل‌شده در کانتینر (در صورت تعریف) تشکیل شده است.
این فرایند یک سیستم فایل ریشه می‌بیند که در ابتدا با محتوای ایمیج کانتینر یکسان است.
هر نوشتنی درون این سلسله‌مراتب سیستم فایل، در صورت مجاز بودن، بر آنچه فرایند در دسترسی‌های بعدی به سیستم فایل می‌بیند اثر می‌گذارد.
حجم‌ها در [مسیرهای مشخص‌شده](#using-subpath) درون سیستم فایل کانتینر متصل می‌شوند.
برای هر کانتینری که در یک Pod تعریف شده است، باید به‌طور جداگانه مشخص کنید که هر حجم مورد استفادهٔ آن کانتینر در کجا متصل شود.

حجم‌ها نمی‌توانند درون حجم‌های دیگر متصل شوند (البته برای سازوکاری مرتبط، بخش [استفاده از subPath](#using-subpath) را ببینید). همچنین یک حجم نمی‌تواند پیوند سخت (hard link) به چیزی در حجمی دیگر داشته باشد.

## انواع حجم‌ها {#volume-types}

کوبرنتیز از چندین نوع حجم پشتیبانی می‌کند.

### configMap

یک [ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) راهی برای تزریق داده‌های پیکربندی به Podها فراهم می‌کند.
می‌توان در یک حجم از نوع `configMap` به داده‌های ذخیره‌شده در ConfigMap ارجاع داد و سپس برنامه‌های کانتینری‌شده‌ای که در Pod اجرا می‌شوند از آن داده‌ها استفاده کنند.

هنگام ارجاع به یک ConfigMap، نام آن را در حجم مشخص می‌کنید. همچنین می‌توانید مسیر مورد استفاده برای یک مدخل خاص از ConfigMap را سفارشی کنید. پیکربندی زیر نشان می‌دهد که چگونه ConfigMap با نام `log-config` در Podی به نام `configmap-pod` متصل می‌شود:

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

ConfigMap با نام `log-config` به‌صورت یک حجم متصل می‌شود و تمام محتوای ذخیره‌شده در مدخل `log_level` آن، در مسیر `/etc/config/log_level.conf` درون Pod قرار می‌گیرد.
توجه کنید که این مسیر از `mountPath` حجم و `path` متناظر با کلید `log_level` به دست می‌آید.

{{< note >}}

* پیش از استفاده از یک ConfigMap، باید [آن را ایجاد کنید](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-a-configmap).

* یک ConfigMap همیشه به‌صورت `readOnly` متصل می‌شود.

* کانتینری که از یک ConfigMap به‌صورت اتصال حجم [`subPath`](#using-subpath) استفاده می‌کند، هنگام تغییر ConfigMap به‌روزرسانی‌ها را دریافت نخواهد کرد.
  
* داده‌های متنی با کدگذاری نویسه‌ای UTF-8 به‌صورت فایل در دسترس قرار می‌گیرند.
  برای کدگذاری‌های نویسه‌ای دیگر، از `binaryData` استفاده کنید.

{{< /note >}}

### downwardAPI {#downwardapi}

حجم `downwardAPI` داده‌های {{< glossary_tooltip term_id="downward-api" text="downward API" >}} را در اختیار برنامه‌ها قرار می‌دهد. داده‌های ارائه‌شده را می‌توانید درون این حجم به‌صورت فایل‌های فقط‌خواندنی با قالب متن ساده بیابید.

{{< note >}}
کانتینری که از downward API به‌صورت اتصال حجم [`subPath`](#using-subpath) استفاده می‌کند، هنگام تغییر مقادیر فیلدها به‌روزرسانی‌ها را دریافت نمی‌کند.
{{< /note >}}

برای اطلاعات بیشتر، [ارائهٔ اطلاعات Pod به کانتینرها از طریق فایل‌ها](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/) را ببینید.

### emptyDir {#emptydir}

برای Podی که یک حجم `emptyDir` تعریف می‌کند، این حجم هنگام تخصیص Pod به یک نود ایجاد می‌شود.
همان‌طور که از نامش پیداست، حجم `emptyDir` در ابتدا خالی است. همهٔ کانتینرهای Pod می‌توانند فایل‌های یکسانی را در حجم `emptyDir` بخوانند و بنویسند، هرچند این حجم ممکن است در هر کانتینر در مسیری یکسان یا متفاوت متصل شده باشد. هنگامی که یک Pod به هر دلیلی از نود حذف شود، داده‌های موجود در `emptyDir` برای همیشه پاک می‌شوند.

{{< note >}}
ازکارافتادن یک کانتینر، Pod را از نود حذف *نمی‌کند*. داده‌های موجود در حجم `emptyDir` در برابر ازکارافتادن کانتینر امن هستند.
{{< /note >}}

برخی کاربردهای `emptyDir` عبارت‌اند از:

* فضای کاری موقت، مثلاً برای مرتب‌سازی ادغامی مبتنی بر دیسک
* ذخیرهٔ نقاط بازیابی (checkpoint) یک محاسبهٔ طولانی برای بازیابی پس از ازکارافتادن
* نگهداری فایل‌هایی که یک کانتینر مدیریت محتوا دریافت می‌کند، در حالی که یک کانتینر وب‌سرور آن داده‌ها را ارائه می‌دهد

فیلد `emptyDir.medium` تعیین می‌کند که حجم‌های `emptyDir` در کجا ذخیره شوند. به‌طور پیش‌فرض، حجم‌های `emptyDir` بسته به محیط شما روی هر رسانه‌ای که پشتوانهٔ نود است، مانند دیسک، SSD یا ذخیره‌سازی شبکه‌ای، ذخیره می‌شوند. اگر فیلد `emptyDir.medium` را روی `"Memory"` تنظیم کنید، کوبرنتیز به‌جای آن یک tmpfs (سیستم فایل مبتنی بر RAM) برای شما متصل می‌کند. با اینکه tmpfs بسیار سریع است، توجه داشته باشید که برخلاف دیسک‌ها، فایل‌هایی که می‌نویسید جزو محدودیت حافظهٔ کانتینری که آن‌ها را نوشته است محاسبه می‌شوند.

برای رسانهٔ پیش‌فرض می‌توان محدودیت اندازه تعیین کرد که ظرفیت حجم `emptyDir` را محدود می‌کند. این فضا از [ذخیره‌سازی گذرای نود](/docs/concepts/storage/ephemeral-storage/#setting-requests-and-limits-for-local-ephemeral-storage) تخصیص داده می‌شود.
اگر این فضا از منبع دیگری (برای نمونه فایل‌های لاگ یا لایه‌های ایمیج) پر شود، ممکن است ظرفیت `emptyDir` پیش از رسیدن به این محدودیت تمام شود.
اگر اندازه‌ای مشخص نشود، اندازهٔ حجم‌های مبتنی بر حافظه برابر با حافظهٔ قابل تخصیص نود در نظر گرفته می‌شود.

{{< caution >}}
برای نکات مربوط به مدیریت منابع هنگام استفاده از `emptyDir` مبتنی بر حافظه، [این بخش](/docs/concepts/configuration/manage-resources-containers/#memory-backed-emptydir) را بررسی کنید.
{{< /caution >}}

{{< feature-state feature_gate_name="EmptyDirVolumeMode" >}}

با فیلد `emptyDir.mode` می‌توانید بیت‌های مجوز یونیکس را برای دایرکتوری emptyDir تنظیم کنید و مقداری بین `0000` و `01777` (هشت‌هشتی) تعیین کنید. این فیلد از همان الگوی فیلد `defaultMode` در حجم‌های Secret و ConfigMap پیروی می‌کند. اگر `mode` مشخص نشود، دایرکتوری با مجوزهای پیش‌فرض `0777` ایجاد می‌شود.

تعیین حالت سفارشی زمانی مفید است که بخواهید دسترسی را فقط به مالک و گروه محدود کنید (برای نمونه `0750`)، یا بیت چسبنده (sticky bit) را روی یک دایرکتوری مشترک تنظیم کنید تا فقط مالکان فایل‌ها بتوانند فایل‌های خود را حذف کنند (برای نمونه `01777`).

{{< note >}}
اگر `fsGroup` در زمینهٔ امنیتی (security context) Pod تنظیم شده باشد، مجوزهای گروهی که `fsGroup` اعمال می‌کند بر `mode` مشخص‌شده در اینجا اولویت دارند. فیلد `mode` در ویندوز هیچ اثری ندارد.
{{< /note >}}

#### نمونهٔ پیکربندی emptyDir

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

#### نمونهٔ پیکربندی حافظه برای emptyDir

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

#### حجم emptyDir و تغییر اندازهٔ درجای Pod

{{< feature-state feature_gate_name="InPlacePodVerticalScalingMemoryBackedVolumes" >}}

هنگامی که feature gate با نام `InPlacePodVerticalScalingMemoryBackedVolumes` فعال باشد، می‌توانید مقدار `sizeLimit` حجم‌های `emptyDir` مبتنی بر حافظه (`medium: Memory`) را به‌صورت پویا و بدون راه‌اندازی مجدد Pod یا کانتینرهای آن تنظیم کنید.

برای جزئیات بیشتر، [تغییر اندازهٔ منابع CPU و حافظهٔ تخصیص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources/#resizing-memory-backed-emptydir-volumes) را ببینید.



#### نمونهٔ پیکربندی مجوزهای emptyDir

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

نوع حجم `fc` امکان اتصال یک حجم ذخیره‌سازی بلوکی فیبر نوری (fibre channel) موجود را به یک Pod فراهم می‌کند. می‌توانید یک یا چند نام جهانی هدف (WWN) را با پارامتر `targetWWNs` در پیکربندی حجم خود مشخص کنید. اگر چند WWN مشخص شود، `targetWWNs` انتظار دارد که آن WWNها از اتصال‌های چندمسیره (multi-path) باشند.

{{< note >}}
باید از قبل، منطقه‌بندی (Zoning) در FC SAN را برای تخصیص و پوشاندن آن LUNها (حجم‌ها) به WWNهای هدف پیکربندی کنید تا میزبان‌های کوبرنتیز بتوانند به آن‌ها دسترسی داشته باشند.
{{< /note >}}

### gcePersistentDisk (منسوخ‌شده) {#gcepersistentdisk}

در کوبرنتیز {{< skew currentVersion >}}، همهٔ عملیات مربوط به نوع درون‌درختی (in-tree) `gcePersistentDisk` به درایور {{< glossary_tooltip text="CSI" term_id="csi" >}} با نام `pd.csi.storage.gke.io` هدایت می‌شوند.

درایور ذخیره‌سازی درون‌درختی `gcePersistentDisk` در نسخهٔ v1.17 کوبرنتیز منسوخ شد و سپس در نسخهٔ v1.28 به‌طور کامل حذف شد.

پروژهٔ کوبرنتیز پیشنهاد می‌کند که به‌جای آن از درایور ذخیره‌سازی شخص ثالث [Google Compute Engine Persistent Disk CSI](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) استفاده کنید.

### gitRepo (غیرفعال) {#gitrepo}

{{< warning >}}

کوبرنتیز {{< skew latestVersion >}} درایور حجم `gitRepo` را در بر *ندارد*. آخرین نسخه‌ای که امکان استفاده از این درایور را فراهم می‌کرد کوبرنتیز v1.35 بود و این درایور از نسخهٔ فرعی [v1.11](/releases/1.11) منسوخ شده است.

برای راه‌اندازی Podی که یک مخزن Git در آن متصل شده باشد، می‌توانید یک حجم [`emptyDir`](#emptydir) را در یک [کانتینر آغازگر (init container)](/docs/concepts/workloads/pods/init-containers/) متصل کنید که مخزن را با Git کلون می‌کند، سپس [EmptyDir](#emptydir) را در کانتینر Pod متصل کنید.

---

می‌توانید استفاده از حجم‌های `gitRepo` را در کلاستر خود با [سیاست‌ها](/docs/concepts/policy/)، مانند [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)، محدود کنید.
می‌توانید عبارت زبان CEL (Common Expression Language) زیر را به‌عنوان بخشی از یک سیاست برای رد کردن استفاده از حجم‌های `gitRepo` به کار ببرید:

```cel
!has(object.spec.volumes) || !object.spec.volumes.exists(v, has(v.gitRepo))
```

{{< /warning >}}

### hostPath {#hostpath}

حجم `hostPath` یک فایل یا دایرکتوری را از سیستم فایل نود میزبان در Pod شما مانت می‌کند. بیشتر Podها به چنین قابلیتی نیاز ندارند، اما این نوع حجم برای برخی برنامه‌ها راه گریز قدرتمندی فراهم می‌کند.

{{< warning >}}
استفاده از نوع حجم `hostPath` خطرات امنیتی فراوانی دارد.
اگر می‌توانید از حجم `hostPath` استفاده نکنید، از آن اجتناب کنید. برای مثال، یک [PersistentVolume از نوع `local`](#local) تعریف کنید و به‌جای آن از همان استفاده کنید.

اگر دسترسی به دایرکتوری‌های مشخصی روی نود را با اعتبارسنجی در زمان پذیرش (admission-time validation) محدود می‌کنید، این محدودیت تنها زمانی مؤثر است که علاوه بر آن الزام کنید همهٔ مانت‌های آن حجم `hostPath` **فقط‌خواندنی** باشند. اگر به یک Pod غیرقابل‌اعتماد اجازه دهید هر مسیری از میزبان را به‌صورت خواندنی‌ونوشتنی مانت کند، کانتینرهای آن Pod ممکن است بتوانند از طریق این مانت خواندنی‌ونوشتنی میزبان، محدودیت‌ها را دور بزنند.

---

هنگام استفاده از حجم‌های `hostPath` احتیاط کنید، چه به‌صورت فقط‌خواندنی مانت شده باشند و چه به‌صورت خواندنی‌ونوشتنی، زیرا:

* دسترسی به سیستم فایل میزبان ممکن است اعتبارنامه‌های ممتاز سیستم (مانند اعتبارنامه‌های kubelet) یا APIهای ممتاز (مانند سوکت محیط اجرای کانتینر) را در معرض دید قرار دهد. از این موارد می‌توان برای فرار از کانتینر یا حمله به بخش‌های دیگر کلاستر استفاده کرد.
* Podهایی با پیکربندی یکسان (مثلاً Podهایی که از یک PodTemplate ساخته شده‌اند) ممکن است به دلیل تفاوت فایل‌ها روی نودهای مختلف، رفتار متفاوتی داشته باشند.
* مصرف حجم `hostPath` به‌عنوان مصرف ذخیره‌سازی موقت (ephemeral storage) محسوب نمی‌شود.
  باید مصرف دیسک را خودتان پایش کنید، زیرا مصرف بیش از حد دیسک توسط `hostPath` به فشار دیسک (disk pressure) روی نود منجر می‌شود.
{{< /warning >}}

برخی کاربردهای `hostPath` عبارت‌اند از:

* اجرای کانتینری که به اجزای سیستمی در سطح نود دسترسی نیاز دارد (مانند کانتینری که لاگ‌های سیستم را به یک مکان مرکزی منتقل می‌کند و برای دسترسی به این لاگ‌ها از مانت فقط‌خواندنی `/var/log` استفاده می‌کند)
* در دسترس قرار دادن یک فایل پیکربندی ذخیره‌شده روی سیستم میزبان به‌صورت فقط‌خواندنی برای یک {{< glossary_tooltip text="Pod ایستا" term_id="static-pod" >}}؛ برخلاف Podهای عادی، Podهای ایستا نمی‌توانند به ConfigMapها دسترسی داشته باشند

#### انواع حجم `hostPath`

علاوه بر ویژگی الزامی `path`، می‌توانید به‌صورت اختیاری یک `type` نیز برای حجم `hostPath` مشخص کنید.

مقادیر مجاز برای `type` عبارت‌اند از:

<!-- empty string represented using U+200C ZERO WIDTH NON-JOINER -->

| مقدار | رفتار |
|:------|:---------|
| `‌""` | رشتهٔ خالی (پیش‌فرض) برای سازگاری با نسخه‌های قبلی است و به این معناست که پیش از مانت کردن حجم `hostPath` هیچ بررسی‌ای انجام نمی‌شود. |
| `DirectoryOrCreate` | اگر در مسیر داده‌شده چیزی وجود نداشته باشد، در صورت نیاز یک دایرکتوری خالی با مجوز 0755 و با همان گروه و مالکیت Kubelet در آنجا ساخته می‌شود. |
| `Directory` | در مسیر داده‌شده باید یک دایرکتوری وجود داشته باشد. |
| `FileOrCreate` | اگر در مسیر داده‌شده چیزی وجود نداشته باشد، در صورت نیاز یک فایل خالی با مجوز 0644 و با همان گروه و مالکیت Kubelet در آنجا ساخته می‌شود. |
| `File` | در مسیر داده‌شده باید یک فایل وجود داشته باشد. |
| `Socket` | در مسیر داده‌شده باید یک سوکت UNIX وجود داشته باشد. |
| `CharDevice` | _(فقط نودهای لینوکسی)_ در مسیر داده‌شده باید یک دستگاه کاراکتری (character device) وجود داشته باشد. |
| `BlockDevice` | _(فقط نودهای لینوکسی)_ در مسیر داده‌شده باید یک دستگاه بلوکی (block device) وجود داشته باشد. |

{{< caution >}}
حالت `FileOrCreate` دایرکتوری والد فایل را **نمی‌سازد**. اگر دایرکتوری والد فایل مانت‌شده وجود نداشته باشد، Pod راه‌اندازی نمی‌شود. برای اطمینان از کارکرد این حالت، می‌توانید دایرکتوری‌ها و فایل‌ها را جداگانه مانت کنید؛ همان‌طور که در [مثال `FileOrCreate`](#hostpath-fileorcreate-example) برای `hostPath` نشان داده شده است.
{{< /caution >}}

برخی فایل‌ها یا دایرکتوری‌هایی که روی میزبان‌های زیرین ساخته می‌شوند ممکن است فقط برای کاربر root قابل دسترسی باشند. در این صورت، برای خواندن از حجم `hostPath` یا نوشتن در آن، یا باید فرایند خود را با کاربر root در یک [کانتینر ممتاز](/docs/tasks/configure-pod-container/security-context/) اجرا کنید یا مجوزهای فایل را روی میزبان تغییر دهید.

#### نمونهٔ پیکربندی hostPath

{{< tabs name="hostpath_examples" >}}
{{< tab name="نود لینوکسی" codelang="yaml" >}}
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
    # مسیر /data/foo را مانت کن، اما فقط اگر آن دایرکتوری از قبل وجود داشته باشد
    hostPath:
      path: /data/foo # محل دایرکتوری روی میزبان
      type: Directory # این فیلد اختیاری است
{{< /tab >}}
{{< tab name="نود ویندوزی" codelang="yaml" >}}
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
    # مسیر C:\Data\foo را از میزبان مانت کن، اما فقط اگر آن دایرکتوری از قبل وجود داشته باشد
  - name: example-volume
    hostPath:
      path: "C:\\Data\\foo" # محل دایرکتوری روی میزبان
      type: Directory       # این فیلد اختیاری است
{{< /tab >}}
{{< /tabs >}}

#### نمونهٔ پیکربندی hostPath با FileOrCreate {#hostpath-fileorcreate-example}

مانیفست زیر یک Pod تعریف می‌کند که مسیر `/var/local/aaa` را درون تنها کانتینر آن Pod مانت می‌کند. اگر مسیر `/var/local/aaa` از قبل روی نود وجود نداشته باشد، kubelet آن را به‌صورت یک دایرکتوری می‌سازد و سپس در Pod مانت می‌کند.

اگر `/var/local/aaa` از قبل وجود داشته باشد اما دایرکتوری نباشد، Pod با شکست مواجه می‌شود. علاوه بر این، kubelet تلاش می‌کند فایلی با نام `/var/local/aaa/1.txt` درون آن دایرکتوری (از دید میزبان) بسازد؛ اگر در آن مسیر از قبل چیزی وجود داشته باشد که فایل معمولی نیست، Pod با شکست مواجه می‌شود.

مانیفست نمونه در ادامه آمده است:

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

منبع حجم `image` نمایانگر یک آبجکت OCI (یک ایمیج کانتینر یا آرتیفکت) است که روی ماشین میزبان kubelet در دسترس است.

نمونه‌ای از استفاده از منبع حجم `image`:

{{% code_sample file="pods/image-volumes.yaml" %}}

این حجم هنگام راه‌اندازی Pod و بسته به مقدار `pullPolicy` ارائه‌شده تعیین (resolve) می‌شود:

`Always`
: ‏kubelet همیشه تلاش می‌کند ارجاع را دریافت (pull) کند. اگر دریافت با شکست مواجه شود، kubelet وضعیت Pod را `Failed` قرار می‌دهد.

`Never`
: ‏kubelet هرگز ارجاع را دریافت نمی‌کند و فقط از ایمیج یا آرتیفکت محلی استفاده می‌کند. اگر هر یک از لایه‌های ایمیج از قبل به‌صورت محلی موجود نباشد یا مانیفست آن ایمیج از قبل در حافظهٔ نهان ذخیره نشده باشد، وضعیت Pod به `Failed` تغییر می‌کند.

`IfNotPresent`
: ‏kubelet در صورتی ارجاع را دریافت می‌کند که از قبل روی دیسک موجود نباشد. اگر ارجاع موجود نباشد و دریافت آن با شکست مواجه شود، وضعیت Pod به `Failed` تغییر می‌کند.

اگر Pod حذف و دوباره ساخته شود، حجم دوباره تعیین می‌شود؛ به این معنا که با بازسازی Pod، محتوای جدید راه دور در دسترس قرار می‌گیرد. شکست در تعیین یا دریافت ایمیج در زمان راه‌اندازی Pod مانع از اجرای کانتینرها می‌شود و ممکن است تأخیر قابل‌توجهی ایجاد کند. تلاش دوباره برای موارد ناموفق با سازوکار عقب‌نشینی (backoff) معمول حجم‌ها انجام می‌شود و این خطاها در فیلدهای reason و message مربوط به Pod گزارش می‌شوند.

انواع آبجکت‌هایی که این حجم می‌تواند مانت کند را پیاده‌سازی محیط اجرای کانتینر روی ماشین میزبان تعیین می‌کند. این انواع دست‌کم باید همهٔ انواع معتبری را که فیلد ایمیج کانتینر پشتیبانی می‌کند در بر بگیرند. آبجکت OCI در یک دایرکتوری واحد (`spec.containers[*].volumeMounts[*].mountPath`) و به‌صورت فقط‌خواندنی مانت می‌شود.

علاوه بر این:

- مانت‌های [`subPath`](/docs/concepts/storage/volumes/#using-subpath) یا [`subPathExpr`](/docs/concepts/storage/volumes/#using-subpath-expanded-environment) برای کانتینرها (`spec.containers[*].volumeMounts[*].subPath`، `spec.containers[*].volumeMounts[*].subPathExpr`) فقط از نسخهٔ v1.33 کوبرنتیز به بعد پشتیبانی می‌شوند.
- فیلد `spec.securityContext.fsGroupChangePolicy` روی این نوع حجم تأثیری ندارد.
- [کنترل‌کنندهٔ پذیرش `AlwaysPullImages`](/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages) همان‌طور که برای ایمیج‌های کانتینر کار می‌کند، برای این منبع حجم نیز کار می‌کند.

فیلدهای زیر برای نوع `image` در دسترس هستند:

`reference`
: ارجاع آرتیفکتی که باید استفاده شود. برای مثال، می‌توانید `registry.k8s.io/conformance:v{{< skew currentPatchVersion >}}` را مشخص کنید تا فایل‌ها از ایمیج آزمون انطباق (conformance) کوبرنتیز بارگذاری شوند. رفتار این فیلد مانند `pod.spec.containers[*].image` است. Secretهای دریافت (pull secrets) نیز به همان روشی گردآوری می‌شوند که برای ایمیج کانتینر انجام می‌شود؛ یعنی با جست‌وجوی اعتبارنامه‌های نود، Secretهای دریافت ایمیج حساب سرویس و Secretهای دریافت ایمیج در مشخصات Pod. این فیلد اختیاری است تا ابزارهای مدیریت پیکربندی سطح بالاتر بتوانند ایمیج‌های کانتینر را در کنترل‌کننده‌های بار کاری مانند Deploymentها و StatefulSetها به‌صورت پیش‌فرض تعیین یا بازنویسی کنند.
  [اطلاعات بیشتر دربارهٔ ایمیج‌های کانتینر](/docs/concepts/containers/images).

`pullPolicy`
: سیاست دریافت آبجکت‌های OCI. مقادیر ممکن عبارت‌اند از: `Always`، `Never` یا `IfNotPresent`. اگر برچسب `:latest` مشخص شده باشد، مقدار پیش‌فرض `Always` و در غیر این صورت `IfNotPresent` است.

برای جزئیات بیشتر دربارهٔ نحوهٔ استفاده از این منبع حجم، مثال [_استفاده از حجم ایمیج در یک Pod_](/docs/tasks/configure-pod-container/image-volumes) را ببینید.

#### وضعیت Pod و حجم‌های `image` {#image-volume-pod-status}

{{< feature-state feature_gate_name="ImageVolumeWithDigest" >}}

اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ImageVolumeWithDigest` در کلاستر شما فعال باشد، هر بار که یک حجم `image` برای Pod مشخص کنید، kubelet وضعیت Pod را به‌روزرسانی می‌کند تا _digest_ ایمیج کانتینری را که به‌عنوان منبع حجم استفاده می‌شود ثبت کند.

در ادامه نمونهٔ ساده‌شده‌ای از یک Pod در حال اجرا، به‌صورت YAML و همراه با به‌روزرسانی وضعیت، آمده است.
به فیلد جدید `ImageRef` در زیر `volumeMounts` در وضعیت کانتینر توجه کنید.

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

با حجم `iscsi` می‌توانید یک حجم موجود iSCSI (یعنی SCSI بر بستر IP) را در Pod خود مانت کنید. برخلاف `emptyDir` که با حذف Pod پاک می‌شود، محتوای حجم `iscsi` حفظ می‌شود و حجم فقط از حالت مانت خارج می‌شود. بنابراین می‌توان حجم iscsi را از پیش با داده پر کرد و این داده‌ها را بین Podها به اشتراک گذاشت.

{{< note >}}
پیش از استفاده از این حجم، باید سرور iSCSI خودتان را در حال اجرا داشته باشید و حجم را روی آن ساخته باشید.
{{< /note >}}

یکی از ویژگی‌های iSCSI این است که چند مصرف‌کننده می‌توانند هم‌زمان آن را به‌صورت فقط‌خواندنی مانت کنند. بنابراین می‌توانید یک حجم را از پیش با مجموعه‌دادهٔ خود پر کنید و سپس آن را به‌صورت موازی از هر تعداد Pod که نیاز دارید ارائه دهید. متأسفانه حجم‌های iSCSI را فقط یک مصرف‌کننده می‌تواند در حالت خواندنی‌ونوشتنی مانت کند و نوشتن هم‌زمان چند نویسنده مجاز نیست.

### local

حجم `local` نمایانگر یک دستگاه ذخیره‌سازی محلی مانت‌شده، مانند دیسک، پارتیشن یا دایرکتوری است.

حجم‌های محلی را فقط می‌توان به‌صورت PersistentVolume ایستا (که به‌صورت دستی ساخته شده است) استفاده کرد. تأمین پویا (dynamic provisioning) پشتیبانی نمی‌شود.

در مقایسه با حجم‌های `hostPath`، حجم‌های `local` به شکلی پایدار و قابل‌حمل استفاده می‌شوند و نیازی نیست Podها را به‌صورت دستی روی نودها زمان‌بندی کنید. سیستم با بررسی وابستگی نود (node affinity) در PersistentVolume از محدودیت‌های نود مربوط به حجم آگاه می‌شود.

با این حال، حجم‌های `local` به در دسترس بودن نود زیرین وابسته‌اند و برای همهٔ برنامه‌ها مناسب نیستند. اگر نودی ناسالم شود، حجم `local` برای Pod غیرقابل‌دسترس می‌شود و Podی که از این حجم استفاده می‌کند نمی‌تواند اجرا شود. برنامه‌هایی که از حجم‌های `local` استفاده می‌کنند باید بتوانند این کاهش دسترس‌پذیری و همچنین احتمال از دست رفتن داده‌ها را، بسته به ویژگی‌های ماندگاری دیسک زیرین، تحمل کنند.

مثال زیر یک PersistentVolume را نشان می‌دهد که از حجم `local` و `nodeAffinity` استفاده می‌کند:

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

هنگام استفاده از حجم‌های `local` باید فیلد `nodeAffinity` را در PersistentVolume تنظیم کنید.
زمان‌بند کوبرنتیز از `nodeAffinity` در PersistentVolume استفاده می‌کند تا این Podها را روی نود درست زمان‌بندی کند.

برای ارائهٔ حجم محلی به‌صورت یک دستگاه بلوکی خام، می‌توان فیلد `volumeMode` در PersistentVolume را (به‌جای مقدار پیش‌فرض "Filesystem") روی "Block" تنظیم کرد.

هنگام استفاده از حجم‌های محلی، توصیه می‌شود یک StorageClass بسازید که `volumeBindingMode` آن روی `WaitForFirstConsumer` تنظیم شده باشد. برای جزئیات بیشتر، مثال [StorageClass](/docs/concepts/storage/storage-classes/#local) محلی را ببینید.
به تأخیر انداختن اتصال حجم تضمین می‌کند که تصمیم اتصال PersistentVolumeClaim همراه با سایر محدودیت‌های نود که Pod ممکن است داشته باشد ارزیابی شود؛ محدودیت‌هایی مانند نیازمندی‌های منابع نود، انتخابگرهای نود، وابستگی Pod (Pod affinity) و ضدوابستگی Pod (Pod anti-affinity).

برای مدیریت بهتر چرخهٔ عمر حجم محلی، می‌توان یک تأمین‌کنندهٔ ایستای خارجی (external static provisioner) را به‌صورت جداگانه اجرا کرد. توجه کنید که این تأمین‌کننده هنوز از تأمین پویا پشتیبانی نمی‌کند. برای نمونه‌ای از نحوهٔ اجرای یک تأمین‌کنندهٔ محلی خارجی، [راهنمای کاربر تأمین‌کنندهٔ حجم محلی](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) را ببینید.

{{< note >}}
اگر برای مدیریت چرخهٔ عمر حجم از تأمین‌کنندهٔ ایستای خارجی استفاده نشود، کاربر باید PersistentVolume محلی را به‌صورت دستی پاک‌سازی و حذف کند.
{{< /note >}}

### nfs

با حجم `nfs` می‌توانید یک اشتراک موجود NFS (سیستم فایل شبکه، Network File System) را در Pod مانت کنید. برخلاف `emptyDir` که با حذف Pod پاک می‌شود، محتوای حجم `nfs` حفظ می‌شود و حجم فقط از حالت مانت خارج می‌شود. بنابراین می‌توان حجم NFS را از پیش با داده پر کرد و این داده‌ها را بین Podها به اشتراک گذاشت. چند نویسنده می‌توانند هم‌زمان NFS را مانت کنند.

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
پیش از استفاده از این حجم، باید سرور NFS خودتان را در حال اجرا داشته باشید و اشتراک را روی آن صادر (export) کرده باشید.

همچنین توجه کنید که نمی‌توانید گزینه‌های مانت NFS را در مشخصات Pod تعیین کنید. می‌توانید گزینه‌های مانت را در سمت سرور تنظیم کنید یا از [/etc/nfsmount.conf](https://man7.org/linux/man-pages/man5/nfsmount.conf.5.html) استفاده کنید.
همچنین می‌توانید حجم‌های NFS را از طریق PersistentVolumeها مانت کنید که امکان تنظیم گزینه‌های مانت را فراهم می‌کنند.
{{< /note >}}

### persistentVolumeClaim {#persistentvolumeclaim}

از حجم `persistentVolumeClaim` برای مانت کردن یک [PersistentVolume](/docs/concepts/storage/persistent-volumes/) در Pod استفاده می‌شود. PersistentVolumeClaimها روشی هستند که کاربران با آن می‌توانند ذخیره‌سازی ماندگار (مانند یک حجم iSCSI) را بدون آگاهی از جزئیات محیط ابری خاص «درخواست» کنند.

برای جزئیات بیشتر، اطلاعات مربوط به [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/) را ببینید.

### portworxVolume (منسوخ‌شده) {#portworxvolume}

{{< feature-state for_k8s_version="v1.25" state="deprecated" >}}

حجم `portworxVolume` یک لایهٔ ذخیره‌سازی بلوکی کشسان است که به‌صورت هایپرکانورجد (hyperconverged) در کنار کوبرنتیز اجرا می‌شود. [Portworx](https://portworx.com/use-case/kubernetes-storage/) فضای ذخیره‌سازی هر سرور را شناسایی می‌کند، آن را بر اساس قابلیت‌ها رده‌بندی می‌کند و ظرفیت چندین سرور را با هم تجمیع می‌کند. Portworx درون ماشین‌های مجازی یا روی نودهای لینوکسی بدون لایهٔ مجازی‌سازی (bare metal) اجرا می‌شود.

یک حجم `portworxVolume` را می‌توان به‌صورت پویا از طریق کوبرنتیز ایجاد کرد، یا آن را از پیش فراهم کرد و درون یک Pod به آن ارجاع داد. در ادامه نمونه‌ای از یک Pod آمده است که به یک حجم Portworx ازپیش‌فراهم‌شده ارجاع می‌دهد:

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
پیش از استفاده از PortworxVolume با نام `pxvol` در Pod، مطمئن شوید که این حجم از قبل وجود دارد.
{{< /note >}}


#### مهاجرت Portworx به CSI
{{< feature-state feature_gate_name="CSIMigrationPortworx" >}}

در کوبرنتیز {{% skew currentVersion %}}، همهٔ عملیات مربوط به حجم‌های درون‌درختی (in-tree) Portworx به‌طور پیش‌فرض به درایور واسط ذخیره‌سازی کانتینر (CSI) با نام `pxd.portworx.com` هدایت می‌شوند. 
[درایور CSI پورت‌ورکس](https://docs.portworx.com/portworx-enterprise/operations/operate-kubernetes/storage-operations/csi) باید روی کلاستر نصب شده باشد.

### projected

حجم projected چندین منبع حجم موجود را در یک دایرکتوری واحد نگاشت می‌کند. برای جزئیات بیشتر، [حجم‌های projected](/docs/concepts/storage/projected-volumes/) را ببینید.

### secret

حجم `secret` برای انتقال اطلاعات حساس، مانند گذرواژه‌ها، به Podها استفاده می‌شود. می‌توانید Secretها را در API کوبرنتیز ذخیره کنید و آن‌ها را به‌صورت فایل سوار (mount) کنید تا Podها بدون وابستگی مستقیم به کوبرنتیز از آن‌ها استفاده کنند. پشتوانهٔ حجم‌های `secret`، سیستم‌فایل tmpfs (یک سیستم‌فایل مبتنی بر RAM) است؛ بنابراین این حجم‌ها هرگز روی حافظهٔ ماندگار نوشته نمی‌شوند.

{{< note >}}

* پیش از استفاده از یک Secret، باید آن را در API کوبرنتیز ایجاد کنید.

* هر Secret همیشه به‌صورت `readOnly` سوار می‌شود.

* کانتینری که از یک Secret به‌صورت سوارکردن حجم با [`subPath`](#using-subpath) استفاده می‌کند، به‌روزرسانی‌های آن Secret را دریافت نمی‌کند.

{{< /note >}}

برای جزئیات بیشتر، [پیکربندی Secretها](/docs/concepts/configuration/secret/) را ببینید.

## استفاده از subPath {#using-subpath}

گاهی مفید است که یک حجم را برای چند کاربرد مختلف در یک Pod به اشتراک بگذارید. ویژگی `volumeMounts[*].subPath` به‌جای ریشهٔ حجم ارجاع‌شده، یک مسیر فرعی درون آن را مشخص می‌کند.

مثال زیر نشان می‌دهد که چگونه می‌توان یک Pod با پشتهٔ LAMP (لینوکس، Apache، MySQL و PHP) را با استفاده از یک حجم مشترک واحد پیکربندی کرد. استفاده از این نمونه پیکربندی `subPath` در محیط عملیاتی توصیه نمی‌شود.

کد و دارایی‌های برنامهٔ PHP به پوشهٔ `html` حجم نگاشت می‌شوند و پایگاه دادهٔ MySQL در پوشهٔ `mysql` همان حجم ذخیره می‌شود. برای نمونه:

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

### استفاده از subPath با متغیرهای محیطی بسط‌یافته {#using-subpath-expanded-environment}

{{< feature-state for_k8s_version="v1.17" state="stable" >}}

برای ساختن نام دایرکتوری‌های `subPath` از متغیرهای محیطی downward API، از فیلد `subPathExpr` استفاده کنید. ویژگی‌های `subPath` و `subPathExpr` با یکدیگر ناسازگارند و نمی‌توان هر دو را هم‌زمان به کار برد.

در این مثال، یک `Pod` با استفاده از `subPathExpr` دایرکتوری `pod1` را درون حجم `hostPath` با مسیر `/var/log/pods` ایجاد می‌کند. حجم `hostPath` نام `Pod` را از `downwardAPI` دریافت می‌کند. دایرکتوری میزبان `/var/log/pods/pod1` در مسیر `/logs` درون کانتینر سوار می‌شود.

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

## منابع

رسانهٔ ذخیره‌سازی (مانند دیسک یا SSD) یک حجم `emptyDir` را رسانهٔ سیستم‌فایلی تعیین می‌کند که دایرکتوری ریشهٔ kubelet (معمولاً `/var/lib/kubelet`) روی آن قرار دارد. هیچ محدودیتی برای میزان فضایی که یک حجم `emptyDir` یا `hostPath` می‌تواند مصرف کند وجود ندارد و هیچ جداسازی‌ای نیز میان کانتینرها یا Podها برقرار نیست.

برای آشنایی با درخواست فضا از طریق مشخصات منابع، [نحوهٔ مدیریت منابع](/docs/concepts/configuration/manage-resources-containers/) را ببینید.

## افزونه‌های حجم بیرون از درخت

افزونه‌های حجم بیرون از درخت (out-of-tree) شامل {{< glossary_tooltip text="واسط ذخیره‌سازی کانتینر" term_id="csi" >}} (CSI) و همچنین FlexVolume (که منسوخ شده است) هستند. این افزونه‌ها به فروشندگان راهکارهای ذخیره‌سازی امکان می‌دهند افزونه‌های ذخیره‌سازی سفارشی بسازند، بی‌آنکه لازم باشد کد منبع افزونهٔ خود را به مخزن کوبرنتیز اضافه کنند.

پیش‌تر، همهٔ افزونه‌های حجم «درون‌درختی» بودند. افزونه‌های درون‌درختی همراه با فایل‌های اجرایی اصلی کوبرنتیز ساخته، پیوند (link) داده، کامپایل و منتشر می‌شدند. این یعنی افزودن یک سامانهٔ ذخیره‌سازی جدید (یک افزونهٔ حجم) به کوبرنتیز مستلزم ثبت کد در مخزن کد اصلی کوبرنتیز بود.

هم CSI و هم FlexVolume امکان می‌دهند افزونه‌های حجم مستقل از کد پایهٔ کوبرنتیز توسعه یابند و به‌عنوان افزونه (extension) روی کلاسترهای کوبرنتیز مستقر (نصب) شوند.

فروشندگان راهکارهای ذخیره‌سازی که قصد دارند یک افزونهٔ حجم بیرون از درخت بسازند، می‌توانند به [پرسش‌های متداول افزونه‌های حجم](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md) مراجعه کنند.

### csi

[واسط ذخیره‌سازی کانتینر](https://github.com/container-storage-interface/spec/blob/master/spec.md) (CSI) یک واسط استاندارد تعریف می‌کند تا سامانه‌های هماهنگ‌سازی کانتینر (مانند کوبرنتیز) بتوانند سامانه‌های ذخیره‌سازی دلخواه را در اختیار بارهای کاری کانتینری خود قرار دهند.

برای اطلاعات بیشتر، لطفاً [پیشنهاد طراحی CSI](https://git.k8s.io/design-proposals-archive/storage/container-storage-interface.md) را مطالعه کنید.

{{< note >}}
پشتیبانی از نسخه‌های 0.2 و 0.3 مشخصات CSI در کوبرنتیز v1.13 منسوخ شده است و در نسخه‌ای در آینده حذف خواهد شد.
{{< /note >}}

{{< note >}}
ممکن است درایورهای CSI با همهٔ نسخه‌های کوبرنتیز سازگار نباشند. لطفاً برای آگاهی از مراحل استقرار پشتیبانی‌شده برای هر نسخهٔ کوبرنتیز و جدول سازگاری، مستندات درایور CSI موردنظر را بررسی کنید.
{{< /note >}}

پس از آنکه یک درایور حجم سازگار با CSI روی کلاستر کوبرنتیز مستقر شد، کاربران می‌توانند از نوع حجم `csi` برای متصل‌کردن (attach) یا سوارکردن حجم‌هایی که آن درایور CSI ارائه می‌کند استفاده کنند.

یک حجم `csi` را می‌توان به سه روش مختلف در یک Pod استفاده کرد:

* از طریق ارجاع به یک [PersistentVolumeClaim](#persistentvolumeclaim)
* با یک [حجم موقت عمومی](/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes)
* با یک [حجم موقت CSI](/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes)، در صورتی که درایور از آن پشتیبانی کند

مدیران ذخیره‌سازی می‌توانند برای پیکربندی یک حجم ماندگار CSI از فیلدهای زیر استفاده کنند:

* `driver`: مقداری رشته‌ای که نام درایور حجم موردنظر را مشخص می‌کند. این مقدار باید با مقداری که درایور CSI در `GetPluginInfoResponse` برمی‌گرداند، مطابق تعریف [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#getplugininfo)، یکسان باشد. کوبرنتیز از این مقدار برای تشخیص اینکه کدام درایور CSI را فراخوانی کند استفاده می‌کند، و اجزای درایور CSI نیز با آن تشخیص می‌دهند کدام آبجکت‌های PV به آن درایور تعلق دارند.
* `volumeHandle`: مقداری رشته‌ای که حجم را به‌طور یکتا شناسایی می‌کند. این مقدار باید با مقداری که درایور CSI در فیلد `volume.id` از `CreateVolumeResponse` برمی‌گرداند، مطابق تعریف [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#createvolume)، یکسان باشد. این مقدار در همهٔ فراخوانی‌های درایور حجم CSI که به این حجم ارجاع می‌دهند، با عنوان `volume_id` ارسال می‌شود.
* `readOnly`: مقداری بولی و اختیاری که مشخص می‌کند آیا حجم باید به‌صورت فقط‌خواندنی «ControllerPublished» (متصل) شود یا نه. مقدار پیش‌فرض false است. این مقدار از طریق فیلد `readonly` در `ControllerPublishVolumeRequest` به درایور CSI ارسال می‌شود.
* `fsType`: اگر `VolumeMode` مربوط به PV برابر `Filesystem` باشد، می‌توان با این فیلد سیستم‌فایلی را مشخص کرد که باید برای سوارکردن حجم استفاده شود. اگر حجم هنوز قالب‌بندی نشده باشد و قالب‌بندی پشتیبانی شود، از این مقدار برای قالب‌بندی حجم استفاده می‌شود. این مقدار از طریق فیلد `VolumeCapability` در `ControllerPublishVolumeRequest`، `NodeStageVolumeRequest` و `NodePublishVolumeRequest` به درایور CSI ارسال می‌شود.
* `volumeAttributes`: نگاشتی از رشته به رشته که ویژگی‌های ایستای یک حجم را مشخص می‌کند. این نگاشت باید با نگاشتی که درایور CSI در فیلد `volume.attributes` از `CreateVolumeResponse` برمی‌گرداند، مطابق تعریف [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#createvolume)، یکسان باشد. این نگاشت از طریق فیلد `volume_context` در `ControllerPublishVolumeRequest`، `NodeStageVolumeRequest` و `NodePublishVolumeRequest` به درایور CSI ارسال می‌شود.
* `controllerPublishSecretRef`: ارجاعی به آبجکت Secret که اطلاعات حساس لازم برای تکمیل فراخوانی‌های CSI یعنی `ControllerPublishVolume` و `ControllerUnpublishVolume` را در بر دارد و به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد، می‌تواند خالی بماند. اگر Secret بیش از یک مقدار محرمانه داشته باشد، همهٔ آن‌ها ارسال می‌شوند.
* `nodeExpandSecretRef`: ارجاعی به Secret که اطلاعات حساس لازم برای تکمیل فراخوانی CSI یعنی `NodeExpandVolume` را در بر دارد و به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد، می‌تواند خالی بماند. اگر آبجکت بیش از یک مقدار محرمانه داشته باشد، همهٔ آن‌ها ارسال می‌شوند. هنگامی که داده‌های محرمانه را برای گسترش حجمِ آغازشده از سوی نود پیکربندی کرده باشید، kubelet آن داده‌ها را از طریق فراخوانی `NodeExpandVolume()` به درایور CSI می‌فرستد. همهٔ نسخه‌های پشتیبانی‌شدهٔ کوبرنتیز فیلد `nodeExpandSecretRef` را ارائه می‌کنند و این فیلد به‌طور پیش‌فرض در دسترس است. نسخه‌های کوبرنتیز پیش از v1.25 این پشتیبانی را نداشتند.
* [feature gate](/docs/reference/command-line-tools-reference/feature-gates-removed/) با نام `CSINodeExpandSecret` را برای هر kube-apiserver و برای kubelet روی همهٔ نودها فعال کنید. از نسخهٔ 1.27 کوبرنتیز، این قابلیت به‌طور پیش‌فرض فعال است و نیازی به فعال‌سازی صریح این feature gate نیست. همچنین باید از درایور CSI‌ای استفاده کنید که در عملیات تغییر اندازهٔ ذخیره‌سازیِ آغازشده از سوی نود، از داده‌های محرمانه پشتیبانی کند یا به آن‌ها نیاز داشته باشد.
* `nodePublishSecretRef`: ارجاعی به آبجکت Secret که اطلاعات حساس لازم برای تکمیل فراخوانی CSI یعنی `NodePublishVolume` را در بر دارد و به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد، می‌تواند خالی بماند. اگر آبجکت Secret بیش از یک مقدار محرمانه داشته باشد، همهٔ آن‌ها ارسال می‌شوند.
* `nodeStageSecretRef`: ارجاعی به آبجکت Secret که اطلاعات حساس لازم برای تکمیل فراخوانی CSI یعنی `NodeStageVolume` را در بر دارد و به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد، می‌تواند خالی بماند. اگر Secret بیش از یک مقدار محرمانه داشته باشد، همهٔ آن‌ها ارسال می‌شوند.

#### پشتیبانی CSI از حجم‌های بلوکی خام

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

فروشندگانی که درایورهای CSI خارجی دارند، می‌توانند پشتیبانی از حجم‌های بلوکی خام (raw block) را در بارهای کاری کوبرنتیز پیاده‌سازی کنند.

می‌توانید [PersistentVolume/PersistentVolumeClaim با پشتیبانی از حجم بلوکی خام](/docs/concepts/storage/persistent-volumes/#raw-block-volume-support) را طبق روال معمول و بدون هیچ تغییر ویژهٔ CSI راه‌اندازی کنید.

#### حجم‌های موقت CSI

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

می‌توانید حجم‌های CSI را مستقیماً در مشخصات Pod پیکربندی کنید. حجم‌هایی که به این شیوه تعریف می‌شوند موقت هستند و پس از راه‌اندازی مجدد Pod باقی نمی‌مانند. برای اطلاعات بیشتر، [حجم‌های موقت](/docs/concepts/storage/ephemeral-volumes/#csi-ephemeral-volumes) را ببینید.

برای اطلاعات بیشتر دربارهٔ نحوهٔ توسعهٔ یک درایور CSI، به [مستندات kubernetes-csi](https://kubernetes-csi.github.io/docs/) مراجعه کنید.

#### پراکسی CSI ویندوز

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

افزونه‌های نود CSI باید عملیات ممتاز (privileged) گوناگونی مانند پویش دستگاه‌های دیسک و سوارکردن سیستم‌فایل‌ها را انجام دهند. این عملیات در هر سیستم‌عامل میزبان متفاوت است. در نودهای کارگر لینوکسی، افزونه‌های نود CSI کانتینری‌شده معمولاً به‌صورت کانتینرهای ممتاز مستقر می‌شوند. در نودهای کارگر ویندوزی، عملیات ممتاز برای افزونه‌های نود CSI کانتینری‌شده به کمک [csi-proxy](https://github.com/kubernetes-csi/csi-proxy) پشتیبانی می‌شود؛ این ابزار یک فایل اجرایی مستقل است که جامعهٔ کاربری آن را نگهداری می‌کند و باید از پیش روی هر نود ویندوزی نصب شود.

برای جزئیات بیشتر، به راهنمای استقرار افزونهٔ CSI‌ای که قصد استقرارش را دارید مراجعه کنید.

#### مهاجرت از افزونه‌های درون‌درختی به درایورهای CSI

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

قابلیت `CSIMigration` عملیاتی را که روی افزونه‌های درون‌درختی موجود انجام می‌شود به افزونه‌های CSI متناظر (که انتظار می‌رود نصب و پیکربندی شده باشند) هدایت می‌کند. در نتیجه، هنگام گذار به یک درایور CSI که جایگزین یک افزونهٔ درون‌درختی می‌شود، اپراتورها نیازی ندارند هیچ تغییری در پیکربندی StorageClassها، PersistentVolumeها یا PersistentVolumeClaimهای موجود (که به افزونه‌های درون‌درختی ارجاع می‌دهند) ایجاد کنند.

{{< note >}}
PVهای موجودی که با یک افزونهٔ حجم درون‌درختی ایجاد شده‌اند، در آینده نیز بدون هیچ تغییری در پیکربندی قابل استفاده خواهند بود؛ حتی پس از آنکه مهاجرت به CSI برای آن نوع حجم کامل شود، و حتی پس از ارتقا به نسخه‌ای از کوبرنتیز که پشتیبانی داخلی (کامپایل‌شده) از آن نوع ذخیره‌سازی را ندارد.

به‌عنوان بخشی از این مهاجرت، شما یا یکی دیگر از مدیران کلاستر **باید** درایور CSI مناسب برای آن ذخیره‌سازی را نصب و پیکربندی کرده باشید. هستهٔ کوبرنتیز این نرم‌افزار را برای شما نصب نمی‌کند.

---

پس از این مهاجرت، می‌توانید PVCها و PVهای جدیدی نیز تعریف کنید که به یکپارچه‌سازی‌های ذخیره‌سازی قدیمی و داخلی ارجاع می‌دهند. به شرط آنکه درایور CSI مناسب را نصب و پیکربندی کرده باشید، ایجاد PV حتی برای حجم‌های کاملاً جدید نیز همچنان کار می‌کند. اکنون مدیریت واقعی ذخیره‌سازی از طریق درایور CSI انجام می‌شود.
{{< /note >}}

عملیات و قابلیت‌های پشتیبانی‌شده عبارت‌اند از: فراهم‌سازی/حذف، اتصال/جداسازی، سوارکردن/پیاده‌کردن و تغییر اندازهٔ حجم‌ها.

افزونه‌های درون‌درختی‌ای که از `CSIMigration` پشتیبانی می‌کنند و درایور CSI متناظرشان پیاده‌سازی شده است، در بخش [انواع حجم‌ها](#volume-types) فهرست شده‌اند.

### flexVolume (منسوخ‌شده)   {#flexvolume}

{{< feature-state for_k8s_version="v1.23" state="deprecated" >}}

واسط افزونهٔ FlexVolume یک واسط بیرون از درخت است که برای ارتباط با درایورهای ذخیره‌سازی از مدلی مبتنی بر اجرای فرمان (exec) استفاده می‌کند. فایل‌های اجرایی درایور FlexVolume باید در مسیر ازپیش‌تعریف‌شدهٔ افزونه‌های حجم روی هر نود، و در برخی موارد روی نودهای control plane نیز، نصب شوند.

Podها از طریق افزونهٔ حجم درون‌درختی `flexVolume` با درایورهای FlexVolume تعامل دارند.

[افزونه‌های](https://github.com/Microsoft/K8s-Storage-Plugins/tree/master/flexvolume/windows) FlexVolume زیر که به‌صورت اسکریپت‌های PowerShell روی میزبان مستقر می‌شوند، از نودهای ویندوزی پشتیبانی می‌کنند:

* [SMB](https://github.com/microsoft/K8s-Storage-Plugins/tree/master/flexvolume/windows/plugins/microsoft.com~smb.cmd)
* [iSCSI](https://github.com/microsoft/K8s-Storage-Plugins/tree/master/flexvolume/windows/plugins/microsoft.com~iscsi.cmd)

{{< note >}}
قابلیت FlexVolume منسوخ شده است. روش توصیه‌شده برای یکپارچه‌سازی ذخیره‌سازی خارجی با کوبرنتیز، استفاده از یک درایور CSI بیرون از درخت است.

نگهدارندگان درایورهای FlexVolume باید یک درایور CSI پیاده‌سازی کنند و به مهاجرت کاربران درایورهای FlexVolume به CSI کمک کنند. کاربران FlexVolume نیز باید بارهای کاری خود را به استفاده از درایور CSI معادل منتقل کنند.
{{< /note >}}

## انتشار مانت (Mount propagation)

{{< caution >}}
انتشار مانت یک قابلیت سطح پایین است که روی همهٔ انواع حجم (volume) به‌طور یکسان کار نمی‌کند. پروژهٔ کوبرنتیز توصیه می‌کند که انتشار مانت فقط با حجم‌های `hostPath` یا حجم‌های `emptyDir` مبتنی بر حافظه استفاده شود. برای اطلاعات بیشتر،
[مسئلهٔ شمارهٔ ۹۵۰۴۹ کوبرنتیز](https://github.com/kubernetes/kubernetes/issues/95049)
را ببینید.
{{< /caution >}}

با انتشار مانت می‌توان حجم‌هایی را که یک کانتینر مانت کرده است با کانتینرهای دیگرِ همان Pod، یا حتی با Podهای دیگرِ همان نود، به اشتراک گذاشت.

انتشار مانتِ هر حجم با فیلد `mountPropagation` در `containers[*].volumeMounts` کنترل می‌شود. مقدارهای مجاز این فیلد عبارت‌اند از:

* `None` - این مانتِ حجم هیچ‌یک از مانت‌های بعدی را که میزبان روی این حجم یا هر یک از زیرشاخه‌های آن انجام می‌دهد دریافت نمی‌کند. به همین ترتیب، هیچ‌یک از مانت‌هایی که کانتینر ایجاد می‌کند روی میزبان دیده نمی‌شود. این حالت پیش‌فرض است.

  این حالت معادل انتشار مانت `rprivate` است که در
  [`mount(8)`](https://man7.org/linux/man-pages/man8/mount.8.html) توضیح داده شده است.

  با این حال، هنگامی که انتشار `rprivate` قابل اعمال نباشد، محیط اجرای CRI ممکن است انتشار مانت `rslave` (یعنی `HostToContainer`) را انتخاب کند. شناخته‌شده است که cri-dockerd (Docker) وقتی منبع مانت شامل شاخهٔ ریشهٔ دیمن Docker (`/var/lib/docker`) باشد، انتشار مانت `rslave` را انتخاب می‌کند.

* `HostToContainer` - این مانتِ حجم همهٔ مانت‌های بعدی را که روی این حجم یا هر یک از زیرشاخه‌های آن انجام می‌شود دریافت می‌کند.

  به بیان دیگر، اگر میزبان چیزی را درون این مانتِ حجم مانت کند، کانتینر آن را در همان‌جا مانت‌شده می‌بیند.

  به همین ترتیب، اگر هر Podای که انتشار مانت `Bidirectional` روی همان حجم دارد چیزی را در آنجا مانت کند، کانتینرِ دارای انتشار مانت `HostToContainer` آن را می‌بیند.

  این حالت معادل انتشار مانت `rslave` است که در
  [`mount(8)`](https://man7.org/linux/man-pages/man8/mount.8.html) توضیح داده شده است.

* `Bidirectional` - این مانتِ حجم همانند مانت `HostToContainer` رفتار می‌کند. افزون بر این، همهٔ مانت‌های حجمی که کانتینر ایجاد می‌کند به میزبان و به همهٔ کانتینرهای همهٔ Podهایی که از همان حجم استفاده می‌کنند بازگردانده و منتشر می‌شوند.

  یک کاربرد رایج این حالت، Podای است که درایور FlexVolume یا CSI دارد، یا Podای که باید با استفاده از یک حجم `hostPath` چیزی را روی میزبان مانت کند.

  این حالت معادل انتشار مانت `rshared` است که در
  [`mount(8)`](https://man7.org/linux/man-pages/man8/mount.8.html) توضیح داده شده است.

  {{< warning >}}
  انتشار مانت `Bidirectional` می‌تواند خطرناک باشد. این حالت ممکن است به سیستم‌عامل میزبان آسیب بزند و به همین دلیل فقط در کانتینرهای ممتاز (privileged) مجاز است. آشنایی با رفتار هستهٔ لینوکس به‌شدت توصیه می‌شود. افزون بر این، هر مانتِ حجمی که کانتینرهای درون Podها ایجاد می‌کنند باید هنگام خاتمه به‌دست همان کانتینرها از بین برود (unmount شود).
  {{< /warning >}}

## مانت‌های فقط‌خواندنی

برای فقط‌خواندنی کردن یک مانت، فیلد `.spec.containers[*].volumeMounts[*].readOnly` را برابر `true` قرار دهید. این کار خودِ حجم را فقط‌خواندنی نمی‌کند، اما آن کانتینر مشخص دیگر نمی‌تواند در آن بنویسد. کانتینرهای دیگرِ Pod ممکن است همان حجم را به‌صورت خواندنی‌ـ‌نوشتنی مانت کنند.

در لینوکس، مانت‌های فقط‌خواندنی به‌طور پیش‌فرض به‌صورت بازگشتی فقط‌خواندنی نیستند. برای نمونه، Podای را در نظر بگیرید که `/mnt` میزبان را به‌عنوان یک حجم `hostPath` مانت می‌کند. اگر سیستم فایل دیگری (مانند tmpfs، NFS یا حافظهٔ USB) به‌صورت خواندنی‌ـ‌نوشتنی روی `/mnt/<SUBMOUNT>` مانت شده باشد، حجمِ مانت‌شده در کانتینر(ها) نیز یک `/mnt/<SUBMOUNT>` قابل‌نوشتن خواهد داشت، حتی اگر خودِ مانت فقط‌خواندنی تعریف شده باشد.

### مانت‌های فقط‌خواندنی بازگشتی

{{< feature-state feature_gate_name="RecursiveReadOnlyMounts" >}}

برای فعال کردن مانت‌های فقط‌خواندنی بازگشتی، باید feature gate با نام `RecursiveReadOnlyMounts` را برای kubelet و kube-apiserver فعال کنید ([feature gate](/docs/reference/command-line-tools-reference/feature-gates/)) و فیلد `.spec.containers[*].volumeMounts[*].recursiveReadOnly` را برای Pod تنظیم کنید.

مقدارهای مجاز عبارت‌اند از:

* `Disabled` (پیش‌فرض): هیچ اثری ندارد.

* `Enabled`: مانت را به‌صورت بازگشتی فقط‌خواندنی می‌کند. برای این کار باید همهٔ شرایط زیر برقرار باشند:

  * فیلد `readOnly` برابر `true` باشد.
  * فیلد `mountPropagation` تنظیم نشده باشد یا برابر `None` باشد.
  * میزبان با هستهٔ لینوکس نسخهٔ 5.12 یا بالاتر اجرا شود.
  * محیط اجرای کانتینر در [سطح CRI](/docs/concepts/architecture/cri) از مانت‌های فقط‌خواندنی بازگشتی پشتیبانی کند.
  * محیط اجرای کانتینر در سطح OCI از مانت‌های فقط‌خواندنی بازگشتی پشتیبانی کند.
    
  اگر هر یک از این شرایط برقرار نباشد، عملیات با شکست روبه‌رو می‌شود.

* `IfPossible`: تلاش می‌کند `Enabled` را اعمال کند و اگر هسته یا کلاس محیط اجرا (runtime class) از این قابلیت پشتیبانی نکند، به `Disabled` بازمی‌گردد.

نمونه:
{{% code_sample file="storage/rro.yaml" %}}

وقتی kubelet و kube-apiserver این ویژگی را بشناسند، فیلد `.status.containerStatuses[*].volumeMounts[*].recursiveReadOnly` برابر `Enabled` یا `Disabled` قرار می‌گیرد.

## مالک فایل

### مالکیت گروهی (GID)

مالکیت گروهیِ (GID) فایل‌های حجم با فیلد `spec.securityContext.fsGroup` در Pod کنترل می‌شود.

برای مراحل دقیق پیکربندی، به
[پیکربندی Security Context برای یک Pod یا کانتینر](/docs/tasks/configure-pod-container/security-context/)
مراجعه کنید.

### مالکیت کاربری (UID)

{{< feature-state feature_gate_name="AtomicWriteVolumeUserFields" >}}

با فعال کردن [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `AtomicWriteVolumeUserFields`، فیلدهای مالکیت کاربریِ (UID) فایل در حجم‌های `configMap`، `secret`، `downwardAPI` و `projected` فعال می‌شوند.

اگر `defaultUser` در سطح حجم مشخص شود، UID مالک همهٔ فایل‌های دادهٔ آن حجم را در زمان ایجاد تعیین می‌کند. در سطح هر آیتم، فیلد `user` UID مالکِ یک فایل مشخص را کنترل می‌کند و بر `defaultUser` اولویت دارد.

نمونه:

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

شناخته‌شده است که محیط‌های اجرای کانتینر زیر از مانت‌های فقط‌خواندنی بازگشتی پشتیبانی می‌کنند.

سطح CRI:

- [containerd](https://containerd.io/)، از نسخهٔ v2.0
- [CRI-O](https://cri-o.io/)، از نسخهٔ v1.30

سطح OCI:

- [runc](https://runc.io/)، از نسخهٔ v1.1
- [crun](https://github.com/containers/crun)، از نسخهٔ v1.8.6

## گزینه‌های bind mount

{{< feature-state feature_gate_name="VolumeBindMountOptions" >}}

با فیلد `.spec.containers[*].volumeMounts[*].bindMountOptions` می‌توانید پرچم‌های امنیتیِ bind mount لینوکس را روی هر مانتِ حجم اعمال کنید. مقدارهای مجاز عبارت‌اند از:

* `noexec` - از اجرای فایل‌های باینری روی حجمِ مانت‌شده جلوگیری می‌کند.
* `nodev` - فایل‌های ویژهٔ دستگاه (device special files) را روی حجمِ مانت‌شده نادیده می‌گیرد.
* `nosuid` - بیت‌های set-user-identifier یا set-group-identifier را روی حجمِ مانت‌شده نادیده می‌گیرد.

این گزینه‌ها برای هر کانتینر جداگانه اعمال می‌شوند؛ بنابراین کانتینرهای مختلفِ یک Pod می‌توانند یک حجم را با گزینه‌های bind mount متفاوت مانت کنند. این فیلد برای [حجم‌های ایمیج](#image) پشتیبانی نمی‌شود.

{{< note >}}
محیط اجرای کانتینر (مانند containerd یا CRI-O) باید از فیلد `mount_options` در پیام `Mount` در CRI پشتیبانی کند. اگر محیط اجرا پشتیبانی از آن را اعلام نکند، kubelet Podهایی را که از `bindMountOptions` استفاده می‌کنند رد می‌کند. این فیلد روی نودهای ویندوز هیچ اثری ندارد.
{{< /note >}}

## {{% heading "whatsnext" %}}

نمونهٔ [استقرار WordPress و MySQL با Persistent Volumeها](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/) را دنبال کنید.
