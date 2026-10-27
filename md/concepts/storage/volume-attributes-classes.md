---
reviewers:
- msau42
- xing-yang
title: Volume Attributes Classها
content_type: concept
weight: 40
---
<!-- overview -->

{{< feature-state feature_gate_name="VolumeAttributesClass" >}}

این صفحه فرض می‌کند که با [StorageClassها](/docs/concepts/storage/storage-classes/)،
[حجم‌ها](/docs/concepts/storage/volumes/) و [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/)
در کوبرنتیز آشنا هستید.

<!-- body -->

VolumeAttributesClass روشی در اختیار مدیران قرار می‌دهد تا «کلاس‌های» تغییرپذیر
ذخیره‌سازی‌ای را که ارائه می‌کنند توصیف کنند. کلاس‌های مختلف ممکن است به سطوح مختلف کیفیت خدمات نگاشت شوند.
خود کوبرنتیز دربارهٔ اینکه این کلاس‌ها چه چیزی را نشان می‌دهند دیدگاه خاصی ندارد.

این قابلیت از نسخهٔ 1.34 به‌طور عمومی در دسترس (GA) است و کاربران می‌توانند آن را غیرفعال کنند.

همچنین تنها می‌توانید از VolumeAttributesClassها با ذخیره‌سازی‌ای استفاده کنید که توسط
{{< glossary_tooltip text="Container Storage Interface" term_id="csi" >}} پشتیبانی می‌شود، و تنها در جایی که
درایور CSI مربوط API `ModifyVolume` را پیاده‌سازی کرده باشد.

## API مربوط به VolumeAttributesClass

هر VolumeAttributesClass شامل `driverName` و `parameters` است که
زمانی استفاده می‌شوند که یک PersistentVolume (PV) متعلق به آن کلاس باید به‌صورت پویا تأمین
یا اصلاح شود.

نام یک آبجکت VolumeAttributesClass اهمیت دارد و کاربران از طریق آن می‌توانند یک کلاس خاص را درخواست کنند.
مدیران نام و سایر پارامترهای یک کلاس را هنگام نخستین ایجاد آبجکت‌های VolumeAttributesClass تعیین می‌کنند.
اگرچه نام یک آبجکت VolumeAttributesClass در یک `PersistentVolumeClaim` قابل تغییر است، پارامترهای یک کلاس موجود تغییرناپذیر هستند.

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: csi.storage.example.com
parameters:
  iops: "3000"
  throughput: "50Mi"
```

### Provisioner

هر VolumeAttributesClass یک provisioner دارد که تعیین می‌کند از کدام پلاگین حجم برای
تأمین PVها استفاده شود. فیلد `driverName` باید مشخص شود.

پشتیبانی از قابلیت VolumeAttributesClass در
[kubernetes-csi/external-provisioner](https://github.com/kubernetes-csi/external-provisioner) پیاده‌سازی شده است.

شما به مشخص کردن [kubernetes-csi/external-provisioner](https://github.com/kubernetes-csi/external-provisioner) محدود نیستید.
همچنین می‌توانید provisionerهای خارجی را اجرا و مشخص کنید
که برنامه‌هایی مستقل هستند و از مشخصه‌ای تعریف‌شده توسط کوبرنتیز پیروی می‌کنند.
نویسندگان provisionerهای خارجی اختیار کامل دارند که کدشان کجا قرار گیرد،
provisioner چگونه عرضه شود، چگونه باید اجرا شود، از کدام پلاگین حجم استفاده کند و غیره.

برای درک نحوهٔ کار provisioner با VolumeAttributesClass، به
[مستندات CSI external-provisioner](https://kubernetes-csi.github.io/docs/external-provisioner.html) مراجعه کنید.

### Resizer

هر VolumeAttributesClass یک resizer دارد که تعیین می‌کند از کدام پلاگین حجم
برای اصلاح PVها استفاده شود. فیلد `driverName` باید مشخص شود.

پشتیبانی از قابلیت اصلاح حجم برای VolumeAttributesClass در
[kubernetes-csi/external-resizer](https://github.com/kubernetes-csi/external-resizer) پیاده‌سازی شده است.

برای مثال، یک PersistentVolumeClaim موجود از یک VolumeAttributesClass به نام silver استفاده می‌کند:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: silver
  …
```

یک VolumeAttributesClass جدید به نام gold در کلاستر در دسترس است:

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: gold
driverName: csi.storage.example.com
parameters:
  iops: "4000"
  throughput: "60Mi"
```

کاربر نهایی می‌تواند PVC را با VolumeAttributesClass جدید gold به‌روزرسانی و اعمال کند:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: gold
  …
```

برای درک نحوهٔ کار resizer با VolumeAttributesClass، به
[مستندات CSI external-resizer](https://kubernetes-csi.github.io/docs/external-resizer.html) مراجعه کنید.

## پارامترها

VolumeAttributeClassها پارامترهایی دارند که حجم‌های متعلق به آن‌ها را توصیف می‌کنند. بسته به provisioner یا resizer
ممکن است پارامترهای متفاوتی پذیرفته شوند. برای مثال، مقدار `4000` برای پارامتر `iops`
و پارامتر `throughput` مختص GCE PD هستند.
هنگامی که یک پارامتر حذف شود، در زمان تأمین حجم از مقدار پیش‌فرض استفاده می‌شود.
اگر کاربر PVC را با VolumeAttributesClass دیگری که پارامترهایی از آن حذف شده است اعمال کند، بسته به
پیاده‌سازی درایور CSI ممکن است از مقدار پیش‌فرض آن پارامترها استفاده شود.
برای جزئیات بیشتر لطفاً به مستندات درایور CSI مربوط مراجعه کنید.

حداکثر ۵۱۲ پارامتر را می‌توان برای یک VolumeAttributesClass تعریف کرد.
طول کل آبجکت parameters، شامل کلیدها و مقادیر آن، نمی‌تواند از 256 KiB بیشتر شود.
