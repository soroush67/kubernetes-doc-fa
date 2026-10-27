---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
title: حجم‌ها
api_metadata:
- apiVersion: ""
  kind: "Volume"
content_type: concept
weight: 10
---

<!-- overview -->

_حجم‌های_ (volumes) کوبرنتیز روشی فراهم می‌کنند تا کانتینرهای یک {{< glossary_tooltip text="Pod" term_id="pod" >}}
بتوانند از طریق سیستم فایل به داده‌ها دسترسی داشته باشند و آن‌ها را به اشتراک بگذارند. انواع مختلفی از حجم وجود دارد که می‌توانید برای اهداف مختلف از آن‌ها استفاده کنید،
مانند:

- پر کردن یک فایل پیکربندی بر اساس یک {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}}
  یا یک {{< glossary_tooltip text="Secret" term_id="secret" >}}
- فراهم کردن فضای موقت (scratch) برای یک Pod
- اشتراک‌گذاری یک سیستم فایل میان دو کانتینر مختلف در یک Pod
- اشتراک‌گذاری یک سیستم فایل میان دو Pod مختلف (حتی اگر آن Podها روی نودهای مختلف اجرا شوند)
- ذخیرهٔ ماندگار داده‌ها به‌گونه‌ای که حتی در صورت راه‌اندازی مجدد یا جایگزینی Pod در دسترس باقی بمانند
- انتقال اطلاعات پیکربندی به برنامه‌ای که در یک کانتینر اجرا می‌شود، بر اساس جزئیات Podی
  که کانتینر در آن قرار دارد
  (برای مثال: اعلام اینکه Pod در کدام فضای نام اجرا می‌شود به یک {{< glossary_tooltip text="کانتینر sidecar" term_id="sidecar-container" >}})
- فراهم کردن دسترسی فقط‌خواندنی به داده‌های موجود در یک ایمیج کانتینر دیگر

اشتراک‌گذاری داده می‌تواند میان فرایندهای محلی مختلف درون یک کانتینر، یا میان کانتینرهای مختلف،
یا میان Podها باشد.

## چرا حجم‌ها مهم هستند

- **ماندگاری داده:** فایل‌های روی دیسک در یک کانتینر موقتی (ephemeral) هستند که این موضوع برای
  برنامه‌های غیربدیهی هنگام اجرا در کانتینرها مشکلاتی ایجاد می‌کند. یکی از مشکلات زمانی رخ می‌دهد که
  یک کانتینر از کار بیفتد (crash) یا متوقف شود؛ وضعیت کانتینر ذخیره نمی‌شود، بنابراین همهٔ
  فایل‌هایی که در طول عمر کانتینر ایجاد یا تغییر داده شده‌اند از دست می‌روند.
  پس از crash، kubelet کانتینر را با وضعیتی پاک راه‌اندازی مجدد می‌کند.

- **ذخیره‌سازی مشترک:** مشکل دیگر زمانی رخ می‌دهد که چندین کانتینر در یک `Pod` اجرا می‌شوند و
  نیاز به اشتراک‌گذاری فایل‌ها دارند. راه‌اندازی و دسترسی به یک سیستم فایل مشترک
  در میان همهٔ کانتینرها می‌تواند چالش‌برانگیز باشد.

انتزاع {{< glossary_tooltip text="حجم" term_id="volume" >}} در کوبرنتیز
می‌تواند به شما در حل هر دوی این مشکلات کمک کند.

پیش از آشنایی با حجم‌ها، PersistentVolumeها و PersistentVolumeClaimها، باید دربارهٔ
{{< glossary_tooltip term_id="Pod" text="Podها" >}} مطالعه کنید و مطمئن شوید که درک می‌کنید
کوبرنتیز چگونه از Podها برای اجرای کانتینرها استفاده می‌کند.
  
<!-- body -->

## حجم‌ها چگونه کار می‌کنند

کوبرنتیز از انواع بسیاری از حجم‌ها پشتیبانی می‌کند. یک {{< glossary_tooltip term_id="pod" text="Pod" >}}
می‌تواند هم‌زمان از هر تعداد نوع حجم استفاده کند.
انواع [حجم موقت](/docs/concepts/storage/ephemeral-volumes/) طول عمری وابسته به یک Pod مشخص دارند،
اما [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/) فراتر از
طول عمر هر Pod منفردی وجود دارند. هنگامی که یک Pod از بین می‌رود، کوبرنتیز حجم‌های موقت را نابود می‌کند؛
اما کوبرنتیز حجم‌های پایدار را نابود نمی‌کند.
برای هر نوع حجم در یک Pod مشخص، داده‌ها در طول راه‌اندازی‌های مجدد کانتینر حفظ می‌شوند.

در اصل، یک حجم یک دایرکتوری است که ممکن است داده‌هایی در آن باشد و
برای کانتینرهای یک pod قابل دسترسی است. اینکه آن دایرکتوری چگونه پدید می‌آید،
رسانه‌ای که پشتیبان آن است و محتوای آن، توسط نوع حجم خاصی
که استفاده می‌شود تعیین می‌شود.

برای استفاده از یک حجم، حجم‌هایی را که باید برای Pod فراهم شوند در `.spec.volumes` مشخص کنید
و اعلام کنید که آن حجم‌ها در کجای کانتینرها mount شوند، در `.spec.containers[*].volumeMounts`.

هنگامی که یک Pod راه‌اندازی می‌شود، یک فرایند در کانتینر دیدی از سیستم فایل می‌بیند که از محتوای اولیهٔ
{{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} به‌علاوهٔ حجم‌هایی
(در صورت تعریف) که درون کانتینر mount شده‌اند تشکیل شده است.
فرایند یک سیستم فایل ریشه می‌بیند که در ابتدا با محتوای ایمیج کانتینر مطابقت دارد.
هر نوشتنی درون آن سلسله‌مراتب سیستم فایل، در صورت مجاز بودن، بر آنچه آن فرایند
در دسترسی‌های بعدی به سیستم فایل می‌بیند اثر می‌گذارد.
حجم‌ها در [مسیرهای مشخص‌شده](#using-subpath) درون سیستم فایل کانتینر mount می‌شوند.
برای هر کانتینر تعریف‌شده در یک Pod، باید به‌طور مستقل مشخص کنید که
هر حجمی که کانتینر استفاده می‌کند در کجا mount شود.

حجم‌ها نمی‌توانند درون حجم‌های دیگر mount شوند (اما برای یک سازوکار مرتبط،
[استفاده از subPath](#using-subpath) را ببینید). همچنین، یک حجم نمی‌تواند شامل hard link به چیزی در
حجم دیگری باشد.

## انواع حجم‌ها {#volume-types}

کوبرنتیز از چندین نوع حجم پشتیبانی می‌کند.

### configMap

یک [ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/)
روشی برای تزریق داده‌های پیکربندی به Podها فراهم می‌کند.
داده‌های ذخیره‌شده در یک ConfigMap را می‌توان در یک حجم از نوع
`configMap` ارجاع داد و سپس توسط برنامه‌های کانتینری‌شده‌ای که در یک Pod اجرا می‌شوند مصرف کرد.

هنگام ارجاع به یک ConfigMap، نام ConfigMap را در
حجم ارائه می‌کنید. می‌توانید مسیری را که برای یک مدخل مشخص
در ConfigMap استفاده می‌شود سفارشی کنید. پیکربندی زیر نشان می‌دهد که چگونه
ConfigMap `log-config` را روی یک Pod به نام `configmap-pod` mount کنید:

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

ConfigMap `log-config` به‌صورت یک حجم mount می‌شود و همهٔ محتوای ذخیره‌شده در
مدخل `log_level` آن در مسیر `/etc/config/log_level.conf` درون Pod mount می‌شود.
توجه داشته باشید که این مسیر از `mountPath` حجم و `path`ی
که با کلید `log_level` مشخص شده است به دست می‌آید.

{{< note >}}

* پیش از استفاده از یک ConfigMap باید [آن را ایجاد کنید](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-a-configmap).

* یک ConfigMap همیشه به‌صورت `readOnly` mount می‌شود.

* کانتینری که از یک ConfigMap به‌عنوان mount حجم [`subPath`](#using-subpath) استفاده می‌کند،
  هنگام تغییر ConfigMap به‌روزرسانی‌ها را دریافت نخواهد کرد.
  
* داده‌های متنی با استفاده از کدگذاری نویسه‌ای UTF-8 به‌صورت فایل در دسترس قرار می‌گیرند.
  برای سایر کدگذاری‌های نویسه‌ای، از `binaryData` استفاده کنید.

{{< /note >}}

### downwardAPI {#downwardapi}

یک حجم `downwardAPI` داده‌های {{< glossary_tooltip term_id="downward-api" text="downward API" >}}
را در دسترس برنامه‌ها قرار می‌دهد. درون این حجم، می‌توانید داده‌های
ارائه‌شده را به‌صورت فایل‌های فقط‌خواندنی با قالب متن ساده بیابید.

{{< note >}}
کانتینری که از downward API به‌عنوان mount حجم [`subPath`](#using-subpath) استفاده می‌کند،
هنگام تغییر مقادیر فیلدها به‌روزرسانی‌ها را دریافت نمی‌کند.
{{< /note >}}

برای اطلاعات بیشتر، [ارائهٔ اطلاعات Pod به کانتینرها از طریق فایل‌ها](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
را ببینید.

### emptyDir {#emptydir}

برای Podی که یک حجم `emptyDir` تعریف می‌کند، حجم زمانی ایجاد می‌شود که Pod به یک نود تخصیص داده شود.
همان‌طور که از نامش پیداست، حجم `emptyDir` در ابتدا خالی است. همهٔ کانتینرهای Pod می‌توانند همان
فایل‌ها را در حجم `emptyDir` بخوانند و بنویسند، هرچند آن حجم می‌تواند در مسیرهای یکسان
یا متفاوتی در هر کانتینر mount شود. هنگامی که یک Pod به هر دلیلی از یک نود
حذف شود، داده‌های موجود در `emptyDir` برای همیشه پاک می‌شوند.

{{< note >}}
از کار افتادن یک کانتینر، Pod را از نود حذف *نمی‌کند*. داده‌های موجود در یک حجم `emptyDir`
در برابر crash کانتینرها ایمن هستند.
{{< /note >}}

برخی از کاربردهای `emptyDir` عبارت‌اند از:

* فضای موقت، مانند مرتب‌سازی ادغامی مبتنی بر دیسک
* ذخیرهٔ نقطهٔ بازرسی (checkpoint) یک محاسبهٔ طولانی برای بازیابی پس از crash
* نگهداری فایل‌هایی که یک کانتینر مدیریت محتوا واکشی می‌کند، در حالی که یک کانتینر
  وب‌سرور داده‌ها را ارائه می‌کند

فیلد `emptyDir.medium` کنترل می‌کند که حجم‌های `emptyDir` کجا ذخیره شوند. به‌طور
پیش‌فرض، حجم‌های `emptyDir` بسته به محیط شما روی هر رسانه‌ای که پشتیبان نود است،
مانند دیسک، SSD یا ذخیره‌سازی شبکه، ذخیره می‌شوند. اگر فیلد
`emptyDir.medium` را روی `"Memory"` تنظیم کنید، کوبرنتیز به‌جای آن یک tmpfs (سیستم فایل
مبتنی بر RAM) برای شما mount می‌کند. اگرچه tmpfs بسیار سریع است، آگاه باشید که برخلاف
دیسک‌ها، فایل‌هایی که می‌نویسید جزو محدودیت حافظهٔ کانتینری که آن‌ها را نوشته است محاسبه می‌شوند.

می‌توان برای رسانهٔ پیش‌فرض یک محدودیت اندازه مشخص کرد که ظرفیت
حجم `emptyDir` را محدود می‌کند. ذخیره‌سازی از
[ذخیره‌سازی موقت نود](/docs/concepts/storage/ephemeral-storage/#setting-requests-and-limits-for-local-ephemeral-storage) تخصیص داده می‌شود.
اگر این ذخیره‌سازی از منبع دیگری (برای مثال، فایل‌های لاگ یا لایه‌های overlay ایمیج) پر شود،
ممکن است ظرفیت `emptyDir` پیش از رسیدن به این محدودیت تمام شود.
اگر هیچ اندازه‌ای مشخص نشود، اندازهٔ حجم‌های مبتنی بر حافظه برابر حافظهٔ قابل تخصیص نود خواهد بود.

{{< caution >}}
لطفاً [اینجا](/docs/concepts/configuration/manage-resources-containers/#memory-backed-emptydir) را
برای نکاتی که باید از نظر مدیریت منابع هنگام استفاده از `emptyDir` مبتنی بر حافظه در نظر گرفت بررسی کنید.
{{< /caution >}}

{{< feature-state feature_gate_name="EmptyDirVolumeMode" >}}

فیلد `emptyDir.mode` به شما امکان می‌دهد بیت‌های مجوز Unix را روی دایرکتوری emptyDir تنظیم کنید
و مقداری میان `0000` و `01777` (مبنای هشت) مشخص کنید. این فیلد از همان الگوی
فیلد `defaultMode` در حجم‌های Secret و ConfigMap پیروی می‌کند. اگر `mode` مشخص نشود،
دایرکتوری با مجوزهای پیش‌فرض `0777` ایجاد می‌شود.

تنظیم یک mode سفارشی زمانی مفید است که بخواهید دسترسی را تنها به مالک و گروه محدود کنید
(برای مثال، `0750`)، یا sticky bit را روی یک دایرکتوری مشترک تنظیم کنید تا تنها مالکان فایل‌ها
بتوانند فایل‌های خود را حذف کنند (برای مثال، `01777`).

{{< note >}}
اگر `fsGroup` در security context مربوط به Pod تنظیم شده باشد، مجوزهای گروهی که
`fsGroup` اعمال می‌کند بر `mode` مشخص‌شده در اینجا اولویت دارند. فیلد `mode` در Windows هیچ اثری ندارد.
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

#### نمونهٔ پیکربندی emptyDir مبتنی بر حافظه

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

#### emptyDir و تغییر اندازهٔ درجای Pod

{{< feature-state feature_gate_name="InPlacePodVerticalScalingMemoryBackedVolumes" >}}

هنگامی که feature gate `InPlacePodVerticalScalingMemoryBackedVolumes` فعال باشد، می‌توانید `sizeLimit` حجم‌های `emptyDir` مبتنی بر حافظه (`medium: Memory`) را بدون راه‌اندازی مجدد Pod یا کانتینرهای آن به‌صورت پویا تنظیم کنید.

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

نوع حجم `fc` امکان mount کردن یک حجم ذخیره‌سازی بلوکی fibre channel موجود را
در یک Pod فراهم می‌کند. می‌توانید یک یا چند نام جهانی (WWN) هدف را
با استفاده از پارامتر `targetWWNs` در پیکربندی Volume خود مشخص کنید. اگر چندین WWN مشخص شود،
targetWWNs انتظار دارد که آن WWNها از اتصال‌های چندمسیره (multi-path) باشند.

{{< note >}}
باید پیش‌تر FC SAN Zoning را پیکربندی کنید تا آن LUNها (حجم‌ها) را به WWNهای هدف
تخصیص داده و mask کنید، تا میزبان‌های کوبرنتیز بتوانند به آن‌ها دسترسی داشته باشند.
{{< /note >}}

### gcePersistentDisk (منسوخ‌شده) {#gcepersistentdisk}

در کوبرنتیز {{< skew currentVersion >}}، همهٔ عملیات‌های نوع درون‌درختی `gcePersistentDisk`
به درایور {{< glossary_tooltip text="CSI" term_id="csi" >}} `pd.csi.storage.gke.io` هدایت می‌شوند.

درایور ذخیره‌سازی درون‌درختی `gcePersistentDisk` در نسخهٔ v1.17 کوبرنتیز منسوخ شد
و سپس در نسخهٔ v1.28 به‌طور کامل حذف شد.

پروژهٔ کوبرنتیز پیشنهاد می‌کند به‌جای آن از درایور ذخیره‌سازی شخص ثالث
[Google Compute Engine Persistent Disk CSI](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver)
استفاده کنید.

### gitRepo (غیرفعال) {#gitrepo}

{{< warning >}}

کوبرنتیز {{< skew latestVersion >}} درایور حجم `gitRepo` را شامل *نمی‌شود*.
آخرین نسخه‌ای که راهی برای استفاده از این درایور فراهم می‌کرد کوبرنتیز
v1.35 بود و این درایور از نسخهٔ فرعی [v1.11](/releases/1.11)
منسوخ شده است.

برای تأمین Podی که یک مخزن Git در آن mount شده باشد، می‌توانید یک حجم
[`emptyDir`](#emptydir) را در یک [init container](/docs/concepts/workloads/pods/init-containers/)
که مخزن را با استفاده از Git شبیه‌سازی (clone) می‌کند mount کنید و سپس [EmptyDir](#emptydir) را در کانتینر Pod mount کنید.

---

می‌توانید استفاده از حجم‌های `gitRepo` را در کلاستر خود با استفاده از
[سیاست‌ها](/docs/concepts/policy/)، مانند
[ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)، محدود کنید.
می‌توانید از عبارت Common Expression Language (CEL) زیر به‌عنوان
بخشی از یک سیاست برای رد استفاده از حجم‌های `gitRepo` استفاده کنید:

```cel
!has(object.spec.volumes) || !object.spec.volumes.exists(v, has(v.gitRepo))
```

{{< /warning >}}

### hostPath {#hostpath}

یک حجم `hostPath` یک فایل یا دایرکتوری از سیستم فایل نود میزبان را
در Pod شما mount می‌کند. بیشتر Podها به این نیازی ندارند، اما این حجم
راه گریز قدرتمندی برای برخی برنامه‌ها فراهم می‌کند.

{{< warning >}}
استفاده از نوع حجم `hostPath` خطرات امنیتی بسیاری به همراه دارد.
اگر می‌توانید از استفاده از حجم `hostPath` اجتناب کنید، این کار را بکنید. برای مثال،
یک [PersistentVolume از نوع `local`](#local) تعریف کنید و به‌جای آن از آن استفاده کنید.

اگر دسترسی به دایرکتوری‌های مشخصی روی نود را با استفاده از اعتبارسنجی
در زمان پذیرش (admission) محدود می‌کنید، آن محدودیت تنها زمانی مؤثر است که
علاوه بر آن الزام کنید هر mount از آن حجم `hostPath` **فقط‌خواندنی** باشد.
اگر به یک Pod غیرقابل اعتماد اجازهٔ mount خواندنی-نوشتنی هر مسیری از میزبان را بدهید،
کانتینرهای آن Pod ممکن است بتوانند mount خواندنی-نوشتنی میزبان را دور بزنند و از آن سوءاستفاده کنند.

---

هنگام استفاده از حجم‌های `hostPath`، چه به‌صورت فقط‌خواندنی mount شوند
و چه به‌صورت خواندنی-نوشتنی، احتیاط کنید، زیرا:

* دسترسی به سیستم فایل میزبان می‌تواند اعتبارنامه‌های ممتاز سیستم (مانند اعتبارنامه‌های kubelet) یا APIهای ممتاز
  (مانند سوکت container runtime) را افشا کند که می‌توان از آن‌ها برای فرار از کانتینر یا حمله به سایر
  بخش‌های کلاستر استفاده کرد.
* Podهایی با پیکربندی یکسان (مانند Podهایی که از یک PodTemplate ایجاد شده‌اند) ممکن است
  به دلیل تفاوت فایل‌های روی نودها، روی نودهای مختلف رفتار متفاوتی داشته باشند.
* استفاده از حجم `hostPath` به‌عنوان مصرف ذخیره‌سازی موقت در نظر گرفته نمی‌شود.
  باید مصرف دیسک را خودتان پایش کنید، زیرا مصرف بیش از حد دیسک توسط `hostPath`
  به فشار دیسک (disk pressure) روی نود منجر می‌شود.
{{< /warning >}}

برخی از کاربردهای `hostPath` عبارت‌اند از:

* اجرای کانتینری که به مؤلفه‌های سیستمی در سطح نود دسترسی نیاز دارد
  (مانند کانتینری که لاگ‌های سیستم را به یک مکان مرکزی منتقل می‌کند
  و با استفاده از یک mount فقط‌خواندنی از `/var/log` به آن لاگ‌ها دسترسی دارد)
* در دسترس قرار دادن فقط‌خواندنی یک فایل پیکربندی ذخیره‌شده روی سیستم میزبان
  برای یک {{< glossary_tooltip text="Pod ایستا" term_id="static-pod" >}}؛
  برخلاف Podهای عادی، Podهای ایستا نمی‌توانند به ConfigMapها دسترسی داشته باشند

#### انواع حجم `hostPath`

علاوه بر ویژگی الزامی `path`، می‌توانید به‌صورت اختیاری یک
`type` برای حجم `hostPath` مشخص کنید.

مقادیر در دسترس برای `type` عبارت‌اند از:

<!-- empty string represented using U+200C ZERO WIDTH NON-JOINER -->

| مقدار | رفتار |
|:------|:---------|
| `‌""` | رشتهٔ خالی (پیش‌فرض) برای سازگاری با نسخه‌های قبلی است، به این معنا که پیش از mount کردن حجم `hostPath` هیچ بررسی‌ای انجام نمی‌شود. |
| `DirectoryOrCreate` | اگر چیزی در مسیر داده‌شده وجود نداشته باشد، در صورت نیاز یک دایرکتوری خالی با مجوز 0755 و با همان گروه و مالکیت Kubelet در آنجا ایجاد می‌شود. |
| `Directory` | یک دایرکتوری باید در مسیر داده‌شده وجود داشته باشد. |
| `FileOrCreate` | اگر چیزی در مسیر داده‌شده وجود نداشته باشد، در صورت نیاز یک فایل خالی با مجوز 0644 و با همان گروه و مالکیت Kubelet در آنجا ایجاد می‌شود. |
| `File` | یک فایل باید در مسیر داده‌شده وجود داشته باشد. |
| `Socket` | یک سوکت UNIX باید در مسیر داده‌شده وجود داشته باشد. |
| `CharDevice` | _(فقط نودهای Linux)_ یک دستگاه نویسه‌ای باید در مسیر داده‌شده وجود داشته باشد. |
| `BlockDevice` | _(فقط نودهای Linux)_ یک دستگاه بلوکی باید در مسیر داده‌شده وجود داشته باشد. |

{{< caution >}}
حالت `FileOrCreate` دایرکتوری والد فایل را ایجاد **نمی‌کند**. اگر دایرکتوری والد
فایل mountشده وجود نداشته باشد، راه‌اندازی Pod با شکست مواجه می‌شود. برای اطمینان از کارکرد این حالت،
می‌توانید دایرکتوری‌ها و فایل‌ها را جداگانه mount کنید، همان‌طور که در
[نمونهٔ `FileOrCreate`](#hostpath-fileorcreate-example) برای `hostPath` نشان داده شده است.
{{< /caution >}}

برخی فایل‌ها یا دایرکتوری‌هایی که روی میزبان‌های زیربنایی ایجاد می‌شوند ممکن است تنها
توسط root قابل دسترسی باشند. در این صورت یا باید فرایند خود را به‌عنوان root در یک
[کانتینر ممتاز](/docs/tasks/configure-pod-container/security-context/) اجرا کنید
یا مجوزهای فایل را روی میزبان تغییر دهید تا بتوانید از یک حجم `hostPath` بخوانید یا در آن بنویسید.

#### نمونهٔ پیکربندی hostPath

{{< tabs name="hostpath_examples" >}}
{{< tab name="نود Linux" codelang="yaml" >}}
---
# This manifest mounts /data/foo on the host as /foo inside the
# single container that runs within the hostpath-example-linux Pod.
#
# The mount into the container is read-only.
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
    # mount /data/foo, but only if that directory already exists
    hostPath:
      path: /data/foo # directory location on host
      type: Directory # this field is optional
{{< /tab >}}
{{< tab name="نود Windows" codelang="yaml" >}}
---
# This manifest mounts C:\Data\foo on the host as C:\foo, inside the
# single container that runs within the hostpath-example-windows Pod.
#
# The mount into the container is read-only.
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
    # mount C:\Data\foo from the host, but only if that directory already exists
  - name: example-volume
    hostPath:
      path: "C:\\Data\\foo" # directory location on host
      type: Directory       # this field is optional
{{< /tab >}}
{{< /tabs >}}

#### نمونهٔ پیکربندی hostPath با FileOrCreate {#hostpath-fileorcreate-example}

مانیفست زیر یک Pod تعریف می‌کند که `/var/local/aaa` را
درون تنها کانتینر Pod mount می‌کند. اگر نود
از پیش مسیر `/var/local/aaa` را نداشته باشد، kubelet آن را
به‌صورت یک دایرکتوری ایجاد می‌کند و سپس آن را در Pod mount می‌کند.

اگر `/var/local/aaa` از پیش وجود داشته باشد اما دایرکتوری نباشد،
Pod با شکست مواجه می‌شود. افزون بر این، kubelet تلاش می‌کند
فایلی به نام `/var/local/aaa/1.txt` درون آن دایرکتوری ایجاد کند
(از دید میزبان)؛ اگر چیزی از پیش در
آن مسیر وجود داشته باشد و یک فایل عادی نباشد، Pod با شکست مواجه می‌شود.

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

منبع حجم `image` نمایانگر یک آبجکت OCI (یک ایمیج کانتینر یا
artifact) است که روی ماشین میزبان kubelet در دسترس است.

نمونه‌ای از استفاده از منبع حجم `image`:

{{% code_sample file="pods/image-volumes.yaml" %}}

حجم هنگام راه‌اندازی Pod، بسته به مقدار `pullPolicy`
ارائه‌شده، resolve می‌شود:

`Always`
: kubelet همیشه تلاش می‌کند ارجاع را pull کند. اگر pull با شکست مواجه شود،
  kubelet وضعیت Pod را روی `Failed` تنظیم می‌کند.

`Never`
: kubelet هرگز ارجاع را pull نمی‌کند و تنها از یک ایمیج یا artifact محلی استفاده می‌کند.
  اگر هر یک از لایه‌های ایمیج از پیش به‌صورت محلی موجود نباشد،
  یا اگر مانیفست آن ایمیج از پیش کش نشده باشد، Pod به وضعیت `Failed` درمی‌آید.

`IfNotPresent`
: kubelet در صورتی pull می‌کند که ارجاع از پیش روی دیسک موجود نباشد. اگر ارجاع
  موجود نباشد و pull با شکست مواجه شود، Pod به وضعیت `Failed` درمی‌آید.

اگر Pod حذف و دوباره ایجاد شود، حجم دوباره resolve می‌شود، به این معنا
که محتوای راه دور جدید هنگام ایجاد مجدد Pod در دسترس قرار می‌گیرد. شکست در
resolve یا pull ایمیج هنگام راه‌اندازی Pod مانع آغاز به کار کانتینرها می‌شود
و ممکن است تأخیر قابل توجهی ایجاد کند. شکست‌ها با استفاده از backoff عادی حجم
دوباره تلاش می‌شوند و در reason و message مربوط به Pod گزارش می‌شوند.

انواع آبجکت‌هایی که می‌توانند توسط این حجم mount شوند توسط
پیاده‌سازی container runtime روی ماشین میزبان تعریف می‌شوند. دست‌کم، باید شامل
همهٔ انواع معتبری باشند که فیلد ایمیج کانتینر پشتیبانی می‌کند. آبجکت OCI
در یک دایرکتوری واحد (`spec.containers[*].volumeMounts[*].mountPath`) mount می‌شود
و به‌صورت فقط‌خواندنی mount خواهد شد.

افزون بر این:

- mountهای [`subPath`](/docs/concepts/storage/volumes/#using-subpath) یا
  [`subPathExpr`](/docs/concepts/storage/volumes/#using-subpath-expanded-environment)
  برای کانتینرها (`spec.containers[*].volumeMounts[*].subPath`، `spec.containers[*].volumeMounts[*].subPathExpr`)
  تنها از کوبرنتیز v1.33 پشتیبانی می‌شوند.
- فیلد `spec.securityContext.fsGroupChangePolicy` هیچ اثری بر این
  نوع حجم ندارد.
- [کنترل‌کنندهٔ پذیرش `AlwaysPullImages`](/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages)
  برای این منبع حجم نیز، همانند ایمیج‌های کانتینر، کار می‌کند.

فیلدهای زیر برای نوع `image` در دسترس هستند:

`reference`
: ارجاع artifactی که باید استفاده شود. برای مثال، می‌توانید
  `registry.k8s.io/conformance:v{{< skew currentPatchVersion >}}` را مشخص کنید تا
  فایل‌ها از ایمیج آزمون انطباق (conformance) کوبرنتیز بارگذاری شوند. همانند
  `pod.spec.containers[*].image` رفتار می‌کند. Pull secretها به همان روشی
  که برای ایمیج کانتینر انجام می‌شود، یعنی با جست‌وجوی اعتبارنامه‌های نود، image
  pull secretهای service account و image pull secretهای spec مربوط به Pod، گردآوری می‌شوند. این فیلد اختیاری است تا
  مدیریت پیکربندی سطح بالاتر بتواند ایمیج‌های کانتینر را در
  کنترل‌کننده‌های بار کاری مانند Deploymentها و StatefulSetها مقداردهی پیش‌فرض یا بازنویسی کند.
  [اطلاعات بیشتر دربارهٔ ایمیج‌های کانتینر](/docs/concepts/containers/images).

`pullPolicy`
: سیاست pull کردن آبجکت‌های OCI. مقادیر ممکن عبارت‌اند از: `Always`، `Never` یا
  `IfNotPresent`. اگر تگ `:latest` مشخص شده باشد، پیش‌فرض `Always` است و در غیر این صورت
  `IfNotPresent`.

برای جزئیات بیشتر دربارهٔ نحوهٔ استفاده از این منبع حجم، نمونهٔ
[_استفاده از یک Image Volume با یک Pod_](/docs/tasks/configure-pod-container/image-volumes) را ببینید.

#### وضعیت Pod و حجم‌های `image` {#image-volume-pod-status}

{{< feature-state feature_gate_name="ImageVolumeWithDigest" >}}

اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `ImageVolumeWithDigest`
در کلاستر شما فعال باشد،
هر زمان که یک حجم `image` برای یک Pod مشخص کنید،
kubelet وضعیت Pod را به‌روزرسانی می‌کند تا _digest_
ایمیج کانتینری را که به‌عنوان منبع حجم استفاده می‌شود ثبت کند.

در ادامه نمونهٔ ساده‌شده‌ای از یک Pod در حال اجرا، به‌صورت YAML و شامل به‌روزرسانی وضعیت، آمده است.
به فیلد جدید `ImageRef` زیر `volumeMounts` در وضعیت کانتینر توجه کنید.

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

یک حجم `iscsi` امکان mount کردن یک حجم iSCSI (SCSI روی IP) موجود را
در Pod شما فراهم می‌کند. برخلاف `emptyDir` که با حذف یک Pod پاک می‌شود،
محتوای یک حجم `iscsi` حفظ می‌شود و حجم صرفاً
unmount می‌شود. این بدان معناست که یک حجم iscsi را می‌توان از پیش با داده‌ها پر کرد و
آن داده‌ها را میان Podها به اشتراک گذاشت.

{{< note >}}
پیش از استفاده از آن، باید سرور iSCSI خود را با حجم ایجادشده در حال اجرا داشته باشید.
{{< /note >}}

یکی از ویژگی‌های iSCSI این است که می‌تواند هم‌زمان توسط چندین مصرف‌کننده به‌صورت فقط‌خواندنی
mount شود. این بدان معناست که می‌توانید یک حجم را از پیش با مجموعه‌دادهٔ خود پر کنید
و سپس آن را به‌صورت موازی از هر تعداد Pod که نیاز دارید ارائه دهید. متأسفانه،
حجم‌های iSCSI تنها توسط یک مصرف‌کنندهٔ منفرد در حالت خواندنی-نوشتنی قابل mount هستند.
نویسندگان هم‌زمان مجاز نیستند.

### local

یک حجم `local` نمایانگر یک دستگاه ذخیره‌سازی محلی mountشده، مانند یک دیسک،
پارتیشن یا دایرکتوری است.

حجم‌های local تنها به‌عنوان PersistentVolume ایجادشده به‌صورت ایستا قابل استفاده هستند. تأمین
پویا پشتیبانی نمی‌شود.

در مقایسه با حجم‌های `hostPath`، حجم‌های `local` به شیوه‌ای ماندگار و
قابل حمل و بدون زمان‌بندی دستی Podها روی نودها استفاده می‌شوند. سیستم
با بررسی node affinity روی PersistentVolume از محدودیت‌های نود حجم آگاه است.

با این حال، حجم‌های `local` به دسترس‌پذیری نود زیربنایی
وابسته‌اند و برای همهٔ برنامه‌ها مناسب نیستند. اگر یک نود ناسالم شود،
حجم `local` برای Pod غیرقابل دسترس می‌شود. Podی که از این حجم استفاده می‌کند
قادر به اجرا نیست. برنامه‌هایی که از حجم‌های `local` استفاده می‌کنند باید بتوانند این
کاهش دسترس‌پذیری و همچنین از دست رفتن احتمالی داده را، بسته به
ویژگی‌های ماندگاری دیسک زیربنایی، تحمل کنند.

مثال زیر یک PersistentVolume را با استفاده از یک حجم `local` و
`nodeAffinity` نشان می‌دهد:

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
زمان‌بند کوبرنتیز از `nodeAffinity` مربوط به PersistentVolume برای زمان‌بندی
این Podها روی نود درست استفاده می‌کند.

`volumeMode` مربوط به PersistentVolume را می‌توان روی "Block" (به‌جای مقدار
پیش‌فرض "Filesystem") تنظیم کرد تا حجم local به‌صورت یک دستگاه بلوکی خام ارائه شود.

هنگام استفاده از حجم‌های local، توصیه می‌شود یک StorageClass با
`volumeBindingMode` برابر `WaitForFirstConsumer` ایجاد کنید. برای جزئیات بیشتر، نمونهٔ
[StorageClass](/docs/concepts/storage/storage-classes/#local) از نوع local را ببینید.
به تأخیر انداختن اتصال حجم تضمین می‌کند که تصمیم اتصال PersistentVolumeClaim
همراه با سایر محدودیت‌های نودی که Pod ممکن است داشته باشد نیز ارزیابی شود،
مانند الزامات منابع نود، انتخابگرهای نود، Pod affinity و Pod anti-affinity.

یک provisioner ایستای خارجی را می‌توان به‌طور جداگانه برای مدیریت بهتر
چرخهٔ عمر حجم local اجرا کرد. توجه داشته باشید که این provisioner هنوز از تأمین
پویا پشتیبانی نمی‌کند. برای نمونه‌ای از نحوهٔ اجرای یک provisioner محلی خارجی،
[راهنمای کاربر local volume provisioner](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner) را ببینید.

{{< note >}}
اگر از provisioner ایستای خارجی برای مدیریت چرخهٔ عمر حجم استفاده نشود،
PersistentVolume محلی نیازمند پاک‌سازی و حذف دستی توسط
کاربر است.
{{< /note >}}
