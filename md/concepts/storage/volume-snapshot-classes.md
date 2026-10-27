---
reviewers:
- saad-ali
- thockin
- msau42
- jingxu97
- xing-yang
- yuxiangqian
title: Volume Snapshot Classها
content_type: concept
weight: 61 # just after volume snapshots
---

<!-- overview -->

این سند مفهوم VolumeSnapshotClass را در کوبرنتیز شرح می‌دهد. آشنایی
با [volume snapshotها](/docs/concepts/storage/volume-snapshots/) و
[storage classها](/docs/concepts/storage/storage-classes) توصیه می‌شود.

<!-- body -->

## مقدمه

همان‌طور که StorageClass روشی در اختیار مدیران قرار می‌دهد تا «کلاس‌های»
ذخیره‌سازی‌ای را که هنگام تأمین یک حجم ارائه می‌کنند توصیف کنند، VolumeSnapshotClass نیز
روشی برای توصیف «کلاس‌های» ذخیره‌سازی هنگام تأمین یک volume snapshot فراهم می‌کند.

## منبع VolumeSnapshotClass

هر VolumeSnapshotClass شامل فیلدهای `driver`، `deletionPolicy` و `parameters` است
که زمانی استفاده می‌شوند که یک VolumeSnapshot متعلق به آن کلاس باید
به‌صورت پویا تأمین شود.

نام یک آبجکت VolumeSnapshotClass اهمیت دارد و کاربران از طریق آن می‌توانند
یک کلاس خاص را درخواست کنند. مدیران نام و سایر پارامترهای
یک کلاس را هنگام نخستین ایجاد آبجکت‌های VolumeSnapshotClass تعیین می‌کنند و این آبجکت‌ها
پس از ایجاد قابل به‌روزرسانی نیستند.

{{< note >}}
نصب CRDها بر عهدهٔ توزیع کوبرنتیز است.
بدون وجود CRDهای لازم، ایجاد یک VolumeSnapshotClass با شکست مواجه می‌شود.
{{< /note >}}

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-hostpath-snapclass
driver: hostpath.csi.k8s.io
deletionPolicy: Delete
parameters:
```

مدیران می‌توانند با افزودن حاشیه‌نویسی
`snapshot.storage.kubernetes.io/is-default-class: "true"` یک VolumeSnapshotClass پیش‌فرض برای VolumeSnapshotهایی
که هیچ کلاس خاصی برای اتصال درخواست نمی‌کنند مشخص کنند:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-hostpath-snapclass
  annotations:
    snapshot.storage.kubernetes.io/is-default-class: "true"
driver: hostpath.csi.k8s.io
deletionPolicy: Delete
parameters:
```

اگر چندین درایور CSI وجود داشته باشد، می‌توان برای هر یک از آن‌ها
یک VolumeSnapshotClass پیش‌فرض مشخص کرد.

### وابستگی‌های VolumeSnapshotClass

هنگامی که یک VolumeSnapshot را بدون مشخص کردن VolumeSnapshotClass ایجاد می‌کنید، کوبرنتیز
به‌طور خودکار یک VolumeSnapshotClass پیش‌فرض را انتخاب می‌کند که درایور CSI آن با
درایور CSI مربوط به StorageClass آن PVC مطابقت دارد.

این رفتار به چندین آبجکت VolumeSnapshotClass پیش‌فرض اجازه می‌دهد در یک کلاستر هم‌زیستی داشته باشند، به شرط آنکه
هر یک با یک درایور CSI منحصربه‌فرد مرتبط باشد.

همیشه اطمینان حاصل کنید که برای هر درایور CSI تنها یک VolumeSnapshotClass پیش‌فرض وجود دارد. اگر
چندین آبجکت VolumeSnapshotClass پیش‌فرض با استفاده از یک درایور CSI یکسان ایجاد شوند،
ایجاد VolumeSnapshot با شکست مواجه می‌شود، زیرا کوبرنتیز نمی‌تواند تعیین کند از کدام‌یک استفاده کند.

### Driver

Volume snapshot classها یک driver دارند که تعیین می‌کند از کدام پلاگین حجم CSI
برای تأمین VolumeSnapshotها استفاده شود. این فیلد باید مشخص شود.

### DeletionPolicy

Volume snapshot classها یک [deletionPolicy](/docs/concepts/storage/volume-snapshots/#delete) دارند.
این فیلد به شما امکان می‌دهد پیکربندی کنید که هنگام حذف آبجکت VolumeSnapshotی که
یک VolumeSnapshotContent به آن متصل است، چه اتفاقی برای آن VolumeSnapshotContent بیفتد. deletionPolicy یک volume snapshot class می‌تواند
`Retain` یا `Delete` باشد. این فیلد باید مشخص شود.

اگر deletionPolicy برابر `Delete` باشد، snapshot ذخیره‌سازی زیربنایی
همراه با آبجکت VolumeSnapshotContent حذف می‌شود. اگر deletionPolicy برابر `Retain` باشد،
هم snapshot زیربنایی و هم VolumeSnapshotContent باقی می‌مانند.

## پارامترها

Volume snapshot classها پارامترهایی دارند که volume snapshotهای متعلق به
آن volume snapshot class را توصیف می‌کنند. بسته به `driver`، ممکن است پارامترهای متفاوتی
پذیرفته شوند.
