---
reviewers:
- jsafrane
- saad-ali
- msau42
- xing-yang
- pohly
title: حجم‌های موقت
content_type: concept
weight: 30
---

<!-- overview -->

این سند _حجم‌های موقت_ (ephemeral volumes) را در کوبرنتیز توضیح می‌دهد. آشنایی با
[حجم‌ها](/docs/concepts/storage/volumes/) توصیه می‌شود، به‌ویژه
PersistentVolumeClaim و PersistentVolume.

<!-- body -->

برخی برنامه‌ها به ذخیره‌سازی اضافی نیاز دارند، اما اهمیتی نمی‌دهند که آن داده‌ها
پس از راه‌اندازی مجدد به‌صورت پایدار نگهداری شوند یا خیر. برای مثال، سرویس‌های کش
معمولاً با محدودیت اندازه‌ی حافظه روبه‌رو هستند و می‌توانند داده‌هایی را که به‌ندرت
استفاده می‌شوند، با تأثیر اندکی بر عملکرد کلی، به ذخیره‌سازی‌ای کندتر از حافظه منتقل کنند.

برنامه‌های دیگر انتظار دارند برخی داده‌های ورودیِ فقط‌خواندنی، مانند داده‌های
پیکربندی یا کلیدهای محرمانه، در قالب فایل در دسترس باشند.

_حجم‌های موقت_ برای همین موارد کاربرد طراحی شده‌اند. از آنجا که حجم‌ها از چرخه‌ی عمر
Pod پیروی می‌کنند و همراه با Pod ایجاد و حذف می‌شوند، می‌توان Podها را بدون محدود شدن
به محلی که یک حجم پایدار (persistent volume) در آن در دسترس است، متوقف و دوباره راه‌اندازی کرد.

حجم‌های موقت به‌صورت _درون‌خطی_ (inline) در spec مربوط به Pod تعریف می‌شوند که
استقرار و مدیریت برنامه را ساده‌تر می‌کند.

### انواع حجم‌های موقت {#types-of-ephemeral-volumes}

کوبرنتیز از چند نوع حجم موقت برای اهداف مختلف پشتیبانی می‌کند:
- [emptyDir](/docs/concepts/storage/volumes/#emptydir): هنگام راه‌اندازی Pod خالی است
  و ذخیره‌سازی آن به‌صورت محلی از دایرکتوری پایه‌ی kubelet (معمولاً دیسک ریشه) یا از RAM تأمین می‌شود
- [configMap](/docs/concepts/storage/volumes/#configmap)،
  [downwardAPI](/docs/concepts/storage/volumes/#downwardapi)،
  [secret](/docs/concepts/storage/volumes/#secret): انواع مختلف داده‌های کوبرنتیز را
  به داخل یک Pod تزریق می‌کنند
- [image](/docs/concepts/storage/volumes/#image): امکان مانت کردن فایل‌ها یا آرتیفکت‌های ایمیج کانتینر
  را مستقیماً در یک Pod فراهم می‌کند.
- [حجم‌های موقت CSI](#csi-ephemeral-volumes):
  مشابه انواع حجم قبلی، اما توسط درایورهای ویژه‌ی {{< glossary_tooltip text="CSI" term_id="csi" >}} ارائه می‌شوند
  که به‌طور مشخص [از این قابلیت پشتیبانی می‌کنند](https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html)
- [حجم‌های موقت عمومی](#generic-ephemeral-volumes) که می‌توانند
  توسط تمام درایورهای ذخیره‌سازی که از حجم‌های پایدار نیز پشتیبانی می‌کنند ارائه شوند


`emptyDir`، `configMap`، `downwardAPI` و `secret` به‌عنوان
[ذخیره‌سازی موقت محلی](/docs/concepts/storage/ephemeral-storage/) ارائه می‌شوند.
این حجم‌ها توسط kubelet روی هر نود مدیریت می‌شوند.

حجم‌های موقت CSI *باید* توسط درایورهای ذخیره‌سازی CSI شخص ثالث ارائه شوند.

حجم‌های موقت عمومی *می‌توانند* توسط درایورهای ذخیره‌سازی CSI شخص ثالث ارائه شوند،
و نیز توسط هر درایور ذخیره‌سازی دیگری که از تأمین پویا (dynamic provisioning) پشتیبانی کند.
برخی درایورهای CSI به‌طور خاص برای حجم‌های موقت CSI نوشته شده‌اند و از تأمین پویا
پشتیبانی نمی‌کنند؛ بنابراین این درایورها را نمی‌توان برای حجم‌های موقت عمومی به کار برد.

مزیت استفاده از درایورهای شخص ثالث این است که می‌توانند قابلیت‌هایی ارائه دهند که
خود کوبرنتیز از آن‌ها پشتیبانی نمی‌کند؛ برای مثال ذخیره‌سازی با ویژگی‌های عملکردی
متفاوت از دیسکی که توسط kubelet مدیریت می‌شود، یا تزریق داده‌های متفاوت.

### حجم‌های موقت CSI {#csi-ephemeral-volumes}

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

{{< note >}}
حجم‌های موقت CSI تنها توسط زیرمجموعه‌ای از درایورهای CSI پشتیبانی می‌شوند.
[فهرست درایورهای](https://kubernetes-csi.github.io/docs/drivers.html) CSI در کوبرنتیز
نشان می‌دهد کدام درایورها از حجم‌های موقت پشتیبانی می‌کنند.
{{< /note >}}

از نظر مفهومی، حجم‌های موقت CSI مشابه انواع حجم `configMap`،
`downwardAPI` و `secret` هستند: ذخیره‌سازی به‌صورت محلی روی هر
نود مدیریت می‌شود و پس از زمان‌بندی Pod روی یک نود، همراه با سایر منابع محلی ایجاد می‌شود.
در این مرحله، کوبرنتیز دیگر مفهومی به نام زمان‌بندی مجدد Pod ندارد. ایجاد حجم باید
به‌گونه‌ای باشد که احتمال شکست آن اندک باشد، وگرنه راه‌اندازی Pod گیر می‌کند. به‌طور خاص،
[زمان‌بندی Pod با آگاهی از ظرفیت ذخیره‌سازی](/docs/concepts/storage/storage-capacity/)
برای این حجم‌ها پشتیبانی *نمی‌شود*. همچنین این حجم‌ها در حال حاضر مشمول
محدودیت‌های مصرف منابع ذخیره‌سازی یک Pod نیستند، زیرا kubelet تنها می‌تواند
این محدودیت‌ها را برای ذخیره‌سازی‌ای که خودش مدیریت می‌کند اعمال کند.


در ادامه نمونه‌ای از مانیفست یک Pod که از ذخیره‌سازی موقت CSI استفاده می‌کند آمده است:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: my-csi-app
spec:
  containers:
    - name: my-frontend
      image: busybox:1.28
      volumeMounts:
      - mountPath: "/data"
        name: my-csi-inline-vol
      command: [ "sleep", "1000000" ]
  volumes:
    - name: my-csi-inline-vol
      csi:
        driver: inline.storage.kubernetes.io
        volumeAttributes:
          foo: bar
```

`volumeAttributes` تعیین می‌کند که درایور چه حجمی را آماده کند. این ویژگی‌ها
مختص هر درایور هستند و استاندارد نشده‌اند. برای دستورالعمل‌های بیشتر، به مستندات
هر درایور CSI مراجعه کنید.

### محدودیت‌های درایور CSI {#csi-driver-restrictions}

حجم‌های موقت CSI به کاربران اجازه می‌دهند `volumeAttributes` را به‌عنوان بخشی از spec مربوط به Pod
مستقیماً به درایور CSI بدهند. درایور CSI‌ای که `volumeAttributes`ی را می‌پذیرد که
معمولاً به مدیران محدود است، برای استفاده در یک حجم موقت درون‌خطی مناسب نیست.
برای مثال، پارامترهایی که به‌طور معمول در StorageClass تعریف می‌شوند
نباید از طریق حجم‌های موقت درون‌خطی در اختیار کاربران قرار گیرند.

مدیران کلاستر که نیاز دارند درایورهای CSIِ مجاز برای استفاده به‌عنوان حجم درون‌خطی
در spec یک Pod را محدود کنند، می‌توانند از روش‌های زیر استفاده کنند:

- حذف `Ephemeral` از `volumeLifecycleModes` در spec مربوط به CSIDriver، که مانع از
  استفاده‌ی درایور به‌عنوان حجم موقت درون‌خطی می‌شود.
- استفاده از یک [admission webhook](/docs/reference/access-authn-authz/extensible-admission-controllers/)
  برای محدود کردن نحوه‌ی استفاده از این درایور.

### حجم‌های موقت عمومی {#generic-ephemeral-volumes}

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

حجم‌های موقت عمومی از این جهت مشابه حجم‌های `emptyDir` هستند که برای هر Pod
یک دایرکتوری برای داده‌های موقت فراهم می‌کنند که معمولاً پس از تأمین (provisioning)
خالی است. اما ممکن است قابلیت‌های اضافی نیز داشته باشند:

- ذخیره‌سازی می‌تواند محلی یا متصل به شبکه باشد.
- حجم‌ها می‌توانند اندازه‌ی ثابتی داشته باشند که Podها نمی‌توانند از آن فراتر روند.
- حجم‌ها ممکن است بسته به درایور و پارامترها، مقداری داده‌ی اولیه داشته باشند.
- عملیات رایج روی حجم‌ها، با فرض اینکه درایور از آن‌ها پشتیبانی کند، پشتیبانی می‌شوند؛ از جمله
  [گرفتن اسنپ‌شات](/docs/concepts/storage/volume-snapshots/)،
  [شبیه‌سازی (cloning)](/docs/concepts/storage/volume-pvc-datasource/)،
  [تغییر اندازه](/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)
  و [ردیابی ظرفیت ذخیره‌سازی](/docs/concepts/storage/storage-capacity/).

نمونه:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: my-app
spec:
  containers:
    - name: my-frontend
      image: busybox:1.28
      volumeMounts:
      - mountPath: "/scratch"
        name: scratch-volume
      command: [ "sleep", "1000000" ]
  volumes:
    - name: scratch-volume
      ephemeral:
        volumeClaimTemplate:
          metadata:
            labels:
              type: my-frontend-volume
          spec:
            accessModes: [ "ReadWriteOnce" ]
            storageClassName: "scratch-storage-class"
            resources:
              requests:
                storage: 1Gi
```

### چرخه‌ی عمر و PersistentVolumeClaim {#lifecycle-and-persistentvolumeclaim}

ایده‌ی کلیدی طراحی این است که
[پارامترهای یک درخواست حجم](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#ephemeralvolumesource-v1-core)
درون منبع حجم (volume source) یک Pod مجاز هستند. برچسب‌ها، حاشیه‌نویسی‌ها (annotations) و
مجموعه‌ی کامل فیلدهای یک PersistentVolumeClaim پشتیبانی می‌شوند. هنگامی که چنین Podی
ایجاد می‌شود، کنترل‌کننده‌ی حجم موقت (ephemeral volume controller) یک آبجکت PersistentVolumeClaim واقعی
را در همان فضای نام (namespace) Pod ایجاد می‌کند و اطمینان می‌یابد که
PersistentVolumeClaim هنگام حذف Pod حذف شود.

این کار اتصال حجم (volume binding) و/یا تأمین آن را فعال می‌کند؛ یا بلافاصله، اگر
{{< glossary_tooltip text="StorageClass" term_id="storage-class" >}} از اتصال فوری حجم استفاده کند، یا زمانی که Pod
به‌صورت آزمایشی روی یک نود زمان‌بندی می‌شود (حالت اتصال حجم `WaitForFirstConsumer`).
حالت دوم برای حجم‌های موقت عمومی توصیه می‌شود، زیرا در این صورت زمان‌بند
می‌تواند آزادانه نود مناسبی را برای Pod انتخاب کند. با اتصال فوری، زمان‌بند ناچار است
نودی را انتخاب کند که پس از در دسترس قرار گرفتن حجم، به آن دسترسی داشته باشد.

از نظر [مالکیت منبع](/docs/concepts/architecture/garbage-collection/#owners-dependents)،
Podی که ذخیره‌سازی موقت عمومی دارد، مالک PersistentVolumeClaimهایی است
که آن ذخیره‌سازی موقت را فراهم می‌کنند. هنگامی که Pod حذف می‌شود،
garbage collector کوبرنتیز PVC را حذف می‌کند، که معمولاً
به حذف حجم نیز منجر می‌شود، زیرا سیاست بازیابی (reclaim policy) پیش‌فرض
storage classها حذف حجم‌هاست. می‌توانید با استفاده از یک StorageClass با سیاست بازیابی `retain`
ذخیره‌سازی محلیِ شبه‌موقت ایجاد کنید: در این حالت ذخیره‌سازی از Pod بیشتر عمر می‌کند
و باید اطمینان حاصل کنید که پاکسازی حجم به‌صورت جداگانه انجام می‌شود.

تا زمانی که این PVCها وجود دارند، می‌توان از آن‌ها مانند هر PVC دیگری استفاده کرد.
به‌طور خاص، می‌توان در شبیه‌سازی حجم یا گرفتن اسنپ‌شات، به آن‌ها به‌عنوان منبع داده
ارجاع داد. آبجکت PVC همچنین وضعیت فعلی حجم را نگه می‌دارد.

### نام‌گذاری PersistentVolumeClaim {#persistentvolumeclaim-naming}

نام‌گذاری PVCهایی که به‌طور خودکار ایجاد می‌شوند قطعی (deterministic) است: نام
ترکیبی از نام Pod و نام حجم است که میان آن‌ها یک خط تیره (`-`) قرار می‌گیرد.
در مثال بالا، نام PVC برابر `my-app-scratch-volume` خواهد بود. این نام‌گذاری قطعی
تعامل با PVC را آسان‌تر می‌کند، زیرا پس از آنکه نام Pod و نام حجم مشخص شد،
نیازی به جست‌وجوی آن نیست.

نام‌گذاری قطعی همچنین احتمال تداخل میان Podهای مختلف
(مثلاً Podی با نام "pod-a" و حجم "scratch" و Pod دیگری با نام
"pod" و حجم "a-scratch" که هر دو به یک نام PVC یعنی
"pod-a-scratch" می‌رسند) و نیز میان Podها و PVCهایی که به‌صورت دستی ایجاد شده‌اند را به وجود می‌آورد.

این تداخل‌ها شناسایی می‌شوند: یک PVC تنها در صورتی برای حجم موقت
استفاده می‌شود که برای همان Pod ایجاد شده باشد. این بررسی بر اساس رابطه‌ی
مالکیت انجام می‌شود. یک PVC موجود بازنویسی یا
اصلاح نمی‌شود. اما این کار تداخل را برطرف نمی‌کند، زیرا بدون PVC
درست، Pod نمی‌تواند راه‌اندازی شود.

{{< caution >}}
هنگام نام‌گذاری Podها و حجم‌ها در یک فضای نام (namespace) مراقب باشید
تا این تداخل‌ها رخ ندهند.
{{< /caution >}}

### امنیت {#security}

استفاده از حجم‌های موقت عمومی به کاربران اجازه می‌دهد در صورتی که بتوانند Pod ایجاد کنند،
به‌طور غیرمستقیم PVC ایجاد کنند، حتی اگر مجوز ایجاد مستقیم PVC را نداشته باشند.
مدیران کلاستر باید از این موضوع آگاه باشند. اگر این امر با مدل امنیتی آن‌ها سازگار نیست،
باید از یک [admission webhook](/docs/reference/access-authn-authz/extensible-admission-controllers/)
استفاده کنند که آبجکت‌هایی مانند Podهای دارای حجم موقت عمومی را رد کند.

[سهمیه‌ی فضای نام (namespace) برای PVCها](/docs/concepts/policy/resource-quotas/#storage-resource-quota)
همچنان به‌طور معمول اعمال می‌شود؛ بنابراین حتی اگر به کاربران اجازه‌ی استفاده از این سازوکار جدید داده شود،
نمی‌توانند از آن برای دور زدن سایر سیاست‌ها استفاده کنند.

## {{% heading "whatsnext" %}}

### حجم‌های موقت مدیریت‌شده توسط kubelet {#ephemeral-volumes-managed-by-kubelet}

به [ذخیره‌سازی موقت محلی](/docs/concepts/storage/ephemeral-storage/) مراجعه کنید.

### حجم‌های موقت CSI {#csi-ephemeral-volumes-1}

- برای اطلاعات بیشتر درباره‌ی طراحی، به
  [KEP مربوط به حجم‌های CSI درون‌خطی موقت](https://github.com/kubernetes/enhancements/blob/ad6021b3d61a49040a3f835e12c8bb5424db2bbb/keps/sig-storage/20190122-csi-inline-volumes.md)
  مراجعه کنید.
- برای اطلاعات بیشتر درباره‌ی توسعه‌ی بعدی این قابلیت، به
  [issue پیگیری بهبود شماره‌ی ۵۹۶](https://github.com/kubernetes/enhancements/issues/596)
  مراجعه کنید.

### حجم‌های موقت عمومی {#generic-ephemeral-volumes-1}

- برای اطلاعات بیشتر درباره‌ی طراحی، به
  [KEP مربوط به حجم‌های درون‌خطی موقت عمومی](https://github.com/kubernetes/enhancements/blob/master/keps/sig-storage/1698-generic-ephemeral-volumes/README.md)
  مراجعه کنید.
