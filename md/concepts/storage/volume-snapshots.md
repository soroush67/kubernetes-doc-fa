---
reviewers:
- saad-ali
- thockin
- msau42
- jingxu97
- xing-yang
- yuxiangqian
title: Volume Snapshotها
content_type: concept
weight: 60
---

<!-- overview -->

در کوبرنتیز، یک _VolumeSnapshot_ نمایانگر یک snapshot از یک حجم روی یک سیستم
ذخیره‌سازی است. این سند فرض می‌کند که از پیش با
[حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/) کوبرنتیز آشنا هستید.

<!-- body -->

## مقدمه

همان‌طور که منابع API `PersistentVolume` و `PersistentVolumeClaim` برای
تأمین حجم برای کاربران و مدیران استفاده می‌شوند، منابع API `VolumeSnapshotContent`
و `VolumeSnapshot` نیز برای ایجاد volume snapshot برای
کاربران و مدیران فراهم شده‌اند.

یک `VolumeSnapshotContent` یک snapshot گرفته‌شده از حجمی در کلاستر است که
توسط مدیر تأمین شده است. این یک منبع در کلاستر است، درست همان‌طور
که یک PersistentVolume یک منبع کلاستر است.

یک `VolumeSnapshot` درخواست snapshot از یک حجم توسط یک کاربر است. این مفهوم مشابه
یک PersistentVolumeClaim است.

`VolumeSnapshotClass` به شما امکان می‌دهد ویژگی‌های مختلفی را برای یک
`VolumeSnapshot` مشخص کنید. این ویژگی‌ها ممکن است میان snapshotهایی که از یک
حجم روی سیستم ذخیره‌سازی گرفته می‌شوند متفاوت باشند و بنابراین نمی‌توان آن‌ها را با استفاده از همان
`StorageClass` یک `PersistentVolumeClaim` بیان کرد.

Volume snapshotها روشی استاندارد در اختیار کاربران کوبرنتیز قرار می‌دهند تا محتوای یک حجم را
در یک لحظهٔ مشخص بدون ایجاد یک حجم کاملاً جدید کپی کنند. این
قابلیت، برای مثال، به مدیران پایگاه داده امکان می‌دهد پیش از
انجام تغییرات ویرایشی یا حذفی، از پایگاه‌های داده پشتیبان بگیرند.

کاربران هنگام استفاده از این قابلیت باید از موارد زیر آگاه باشند:

- آبجکت‌های API `VolumeSnapshot`، `VolumeSnapshotContent` و `VolumeSnapshotClass`
  {{< glossary_tooltip term_id="CustomResourceDefinition" text="CRD" >}} هستند و
  بخشی از API هسته نیستند.
- پشتیبانی از `VolumeSnapshot` تنها برای درایورهای CSI در دسترس است.
- به‌عنوان بخشی از فرایند استقرار `VolumeSnapshot`، تیم کوبرنتیز
  یک snapshot controller برای استقرار در control plane و یک کانتینر کمکی sidecar
  به نام csi-snapshotter برای استقرار همراه با درایور CSI فراهم می‌کند.
  snapshot controller مراقب آبجکت‌های `VolumeSnapshot` و `VolumeSnapshotContent` است
  و مسئول ایجاد و حذف آبجکت `VolumeSnapshotContent` است.
  sidecar csi-snapshotter مراقب آبجکت‌های `VolumeSnapshotContent` است و عملیات‌های
  `CreateSnapshot` و `DeleteSnapshot` را روی یک endpoint CSI آغاز می‌کند.
- همچنین یک سرور validating webhook وجود دارد که اعتبارسنجی سخت‌گیرانه‌تری روی
  آبجکت‌های snapshot فراهم می‌کند. این سرور باید توسط توزیع‌های کوبرنتیز همراه با
  snapshot controller و CRDها نصب شود، نه توسط درایورهای CSI. این سرور باید در همهٔ
  کلاسترهای کوبرنتیزی که قابلیت snapshot در آن‌ها فعال است نصب شود.
- درایورهای CSI ممکن است قابلیت volume snapshot را پیاده‌سازی کرده باشند یا نکرده باشند.
  درایورهای CSI که از volume snapshot پشتیبانی می‌کنند احتمالاً از
  csi-snapshotter استفاده می‌کنند. برای جزئیات، [مستندات درایور CSI](https://kubernetes-csi.github.io/docs/) را ببینید.
- نصب CRDها و snapshot controller بر عهدهٔ توزیع کوبرنتیز است.

برای کاربردهای پیشرفته، مانند ایجاد snapshotهای گروهی از چندین حجم، مستندات خارجی
[CSI Volume Group Snapshot](https://kubernetes-csi.github.io/docs/group-snapshot-restore-feature.html) را ببینید.

در کلاسترهایی که یک snapshot تنها از بخشی از کلاستر قابل استفاده است (برای مثال،
snapshot یک حجم در یک zone از یک کلاستر چند-zone بدون ذخیره‌سازی مشترک)،
توپولوژی snapshot را می‌توان ثبت کرد و هنگام بازیابی از آن رعایت کرد. برای
جزئیات، [مستندات CSI](https://kubernetes-csi.github.io/docs/introduction.html)
خارجی را ببینید.

## چرخهٔ عمر volume snapshot و volume snapshot content

`VolumeSnapshotContents` منابعی در کلاستر هستند. `VolumeSnapshots` درخواست‌هایی
برای آن منابع‌اند. تعامل میان `VolumeSnapshotContents` و `VolumeSnapshots`
از این چرخهٔ عمر پیروی می‌کند:

### تأمین Volume Snapshot

snapshotها به دو روش ممکن است تأمین شوند: از پیش تأمین‌شده یا تأمین‌شده به‌صورت پویا.

#### از پیش تأمین‌شده {#static}

مدیر کلاستر تعدادی `VolumeSnapshotContents` ایجاد می‌کند. این آبجکت‌ها جزئیات
volume snapshot واقعی روی سیستم ذخیره‌سازی را که برای استفادهٔ کاربران کلاستر در دسترس است در خود دارند.
آن‌ها در API کوبرنتیز وجود دارند و برای مصرف در دسترس هستند.

#### پویا

به‌جای استفاده از یک snapshot از پیش موجود، می‌توانید درخواست کنید که یک snapshot به‌صورت پویا
از یک PersistentVolumeClaim گرفته شود. [VolumeSnapshotClass](/docs/concepts/storage/volume-snapshot-classes/)
پارامترهای خاص ارائه‌دهندهٔ ذخیره‌سازی را برای استفاده هنگام گرفتن snapshot مشخص می‌کند.

### اتصال

snapshot controller اتصال یک آبجکت `VolumeSnapshot` به یک آبجکت
`VolumeSnapshotContent` مناسب را، هم در سناریوهای از پیش تأمین‌شده و هم در سناریوهای تأمین پویا، بر عهده دارد.
این اتصال یک نگاشت یک‌به‌یک است.

در مورد اتصال از پیش تأمین‌شده، VolumeSnapshot تا زمانی که
آبجکت VolumeSnapshotContent درخواستی ایجاد نشود متصل‌نشده باقی می‌ماند.

### محافظت از Persistent Volume Claim به‌عنوان مبدأ Snapshot

هدف از این محافظت اطمینان از این است که آبجکت‌های API
{{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}}
در حال استفاده، در حین گرفتن snapshot از آن‌ها از سیستم حذف نشوند
(زیرا این کار ممکن است به از دست رفتن داده منجر شود).

در حالی که از یک PersistentVolumeClaim snapshot گرفته می‌شود، آن PersistentVolumeClaim
در حال استفاده است. اگر یک آبجکت API PersistentVolumeClaim را که به‌طور فعال به‌عنوان مبدأ snapshot
استفاده می‌شود حذف کنید، آبجکت PersistentVolumeClaim بلافاصله حذف نمی‌شود. بلکه حذف
آبجکت PersistentVolumeClaim تا زمانی که snapshot در وضعیت readyToUse قرار گیرد یا لغو شود به تعویق می‌افتد.

### حذف

حذف با حذف آبجکت `VolumeSnapshot` آغاز می‌شود و از `DeletionPolicy`
پیروی می‌شود. اگر `DeletionPolicy` برابر `Delete` باشد، snapshot ذخیره‌سازی زیربنایی
همراه با آبجکت `VolumeSnapshotContent` حذف می‌شود. اگر `DeletionPolicy` برابر
`Retain` باشد، هم snapshot زیربنایی و هم `VolumeSnapshotContent` باقی می‌مانند.

## VolumeSnapshotها

هر VolumeSnapshot شامل یک spec و یک status است.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: new-snapshot-test
spec:
  volumeSnapshotClassName: csi-hostpath-snapclass
  source:
    persistentVolumeClaimName: pvc-test
```

`persistentVolumeClaimName` نام منبع دادهٔ PersistentVolumeClaim
برای snapshot است. این فیلد برای تأمین پویای یک snapshot الزامی است.

یک volume snapshot می‌تواند با مشخص کردن نام یک
[VolumeSnapshotClass](/docs/concepts/storage/volume-snapshot-classes/)
با استفاده از ویژگی `volumeSnapshotClassName` یک کلاس خاص را درخواست کند. اگر چیزی تنظیم نشود،
در صورت وجود از کلاس پیش‌فرض استفاده می‌شود.

برای snapshotهای از پیش تأمین‌شده، باید یک `volumeSnapshotContentName`
را به‌عنوان مبدأ snapshot مشخص کنید، همان‌طور که در مثال زیر نشان داده شده است. فیلد مبدأ
`volumeSnapshotContentName` برای snapshotهای از پیش تأمین‌شده الزامی است.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: test-snapshot
spec:
  source:
    volumeSnapshotContentName: test-content
```

## Volume Snapshot Contentها

هر VolumeSnapshotContent شامل یک spec و یک status است. در تأمین پویا،
snapshot common controller آبجکت‌های `VolumeSnapshotContent` را ایجاد می‌کند. در ادامه یک نمونه آمده است:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
  name: snapcontent-72d9a349-aacd-42d2-a240-d775650d2455
spec:
  deletionPolicy: Delete
  driver: hostpath.csi.k8s.io
  source:
    volumeHandle: ee0cfb94-f8d4-11e9-b2d8-0242ac110002
  sourceVolumeMode: Filesystem
  volumeSnapshotClassName: csi-hostpath-snapclass
  volumeSnapshotRef:
    name: new-snapshot-test
    namespace: default
    uid: 72d9a349-aacd-42d2-a240-d775650d2455
```

`volumeHandle` شناسهٔ یکتای حجمی است که روی backend ذخیره‌سازی ایجاد شده
و درایور CSI هنگام ایجاد حجم آن را بازگردانده است. این فیلد
برای تأمین پویای یک snapshot الزامی است.
این فیلد حجم مبدأ snapshot را مشخص می‌کند.

برای snapshotهای از پیش تأمین‌شده، شما (به‌عنوان مدیر کلاستر) مسئول
ایجاد آبجکت `VolumeSnapshotContent` به شکل زیر هستید.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
  name: new-snapshot-content-test
spec:
  deletionPolicy: Delete
  driver: hostpath.csi.k8s.io
  source:
    snapshotHandle: 7bdd0de3-aaeb-11e8-9aae-0242ac110002
  sourceVolumeMode: Filesystem
  volumeSnapshotRef:
    name: new-snapshot-test
    namespace: default
```

`snapshotHandle` شناسهٔ یکتای volume snapshot ایجادشده روی
backend ذخیره‌سازی است. این فیلد برای snapshotهای از پیش تأمین‌شده الزامی است.
این فیلد شناسهٔ snapshot CSI روی سیستم ذخیره‌سازی را که این
`VolumeSnapshotContent` نمایانگر آن است مشخص می‌کند.

`sourceVolumeMode` حالت حجمی است که از آن snapshot گرفته می‌شود. مقدار
فیلد `sourceVolumeMode` می‌تواند `Filesystem` یا `Block` باشد. اگر
حالت حجم مبدأ مشخص نشده باشد، کوبرنتیز با snapshot طوری رفتار می‌کند که گویی
حالت حجم مبدأ ناشناخته است.

`volumeSnapshotRef` ارجاع به `VolumeSnapshot` متناظر است. توجه داشته باشید که
هنگامی که `VolumeSnapshotContent` به‌عنوان یک snapshot از پیش تأمین‌شده ایجاد می‌شود،
`VolumeSnapshot` ارجاع‌داده‌شده در `volumeSnapshotRef` ممکن است هنوز وجود نداشته باشد.

## تبدیل حالت حجم یک Snapshot {#convert-volume-mode}

اگر API مربوط به `VolumeSnapshots` که روی کلاستر شما نصب شده است از فیلد `sourceVolumeMode`
پشتیبانی کند، آنگاه API این توانایی را دارد که از تبدیل حالت یک حجم توسط
کاربران غیرمجاز جلوگیری کند.

برای بررسی اینکه آیا کلاستر شما این قابلیت را دارد، دستور زیر را اجرا کنید:

```yaml
$ kubectl get crd volumesnapshotcontent -o yaml
```

اگر می‌خواهید به کاربران اجازه دهید یک `PersistentVolumeClaim` را از یک
`VolumeSnapshot` موجود، اما با حالت حجمی متفاوت از مبدأ، ایجاد کنند، حاشیه‌نویسی
`snapshot.storage.kubernetes.io/allow-volume-mode-change: "true"` باید به
`VolumeSnapshotContent` متناظر با `VolumeSnapshot` افزوده شود.

برای snapshotهای از پیش تأمین‌شده، `spec.sourceVolumeMode` باید توسط
مدیر کلاستر مقداردهی شود.

نمونه‌ای از منبع `VolumeSnapshotContent` با این قابلیت فعال به این شکل خواهد بود:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotContent
metadata:
  name: new-snapshot-content-test
  annotations:
    - snapshot.storage.kubernetes.io/allow-volume-mode-change: "true"
spec:
  deletionPolicy: Delete
  driver: hostpath.csi.k8s.io
  source:
    snapshotHandle: 7bdd0de3-aaeb-11e8-9aae-0242ac110002
  sourceVolumeMode: Filesystem
  volumeSnapshotRef:
    name: new-snapshot-test
    namespace: default
```

## توپولوژی Volume Snapshot

در برخی کلاسترها یک snapshot تنها از بخشی از کلاستر قابل استفاده است. برای مثال، در
یک کلاستر چند-zone که ذخیره‌سازی میان zoneها مشترک نیست، snapshot یک حجم
در یک zone تنها از همان zone قابل استفاده است: حجم‌هایی که از snapshot بازیابی می‌شوند تنها
در جایی قابل ایجادند که داده‌های snapshot در آن قرار دارد.

هنگامی که قابلیت `VolumeSnapshotTopology` فعال باشد، این توپولوژی ثبت و
رعایت می‌شود:

- مدیر کلاستر می‌تواند `allowedTopologies` را روی یک
  [VolumeSnapshotClass](/docs/concepts/storage/volume-snapshot-classes/) تنظیم کند تا
  مشخص کند snapshotهایی که به‌صورت پویا ایجاد می‌شوند باید از کجا قابل استفاده باشند.
- درایور CSI گزارش می‌دهد که یک snapshot از کجا قابل استفاده است و sidecar
  csi-snapshotter آن را در `VolumeSnapshotContent.spec.nodeAffinity` ثبت می‌کند.
- هنگامی که یک حجم را از یک snapshot تأمین می‌کنید، از این توپولوژی برای قرار دادن
  حجم بازیابی‌شده در جایی که داده‌های snapshot در دسترس است استفاده می‌شود.

این یک قابلیت آلفای sidecarهای CSI است که با
feature gate `VolumeSnapshotTopology` روی csi-snapshotter و external-provisioner فعال می‌شود.
برای جزئیات، [مستندات CSI](https://kubernetes-csi.github.io/docs/introduction.html)
خارجی را ببینید.

## تأمین حجم‌ها از Snapshotها

می‌توانید با استفاده از فیلد _dataSource_ در آبجکت `PersistentVolumeClaim`
یک حجم جدید تأمین کنید که از پیش با داده‌های یک snapshot پر شده باشد.

برای جزئیات بیشتر، ببینید:
[Volume Snapshot و بازیابی حجم از Snapshot](/docs/concepts/storage/persistent-volumes/#volume-snapshot-and-restore-volume-from-snapshot-support).
