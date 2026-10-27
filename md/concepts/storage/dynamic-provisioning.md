---
reviewers:
- saad-ali
- jsafrane
- thockin
- msau42
title: تأمین پویای حجم
content_type: concept
weight: 50
---

<!-- overview -->

تأمین پویای حجم (Dynamic volume provisioning) امکان می‌دهد حجم‌های ذخیره‌سازی به‌صورت درخواستی ایجاد شوند.
بدون تأمین پویا، مدیران کلاستر باید به‌صورت دستی
با ارائه‌دهندهٔ ابری یا ذخیره‌سازی خود تماس بگیرند تا حجم‌های ذخیره‌سازی جدید ایجاد شوند، و سپس
[آبجکت‌های `PersistentVolume`](/docs/concepts/storage/persistent-volumes/)
را برای نمایش آن‌ها در کوبرنتیز ایجاد کنند. قابلیت تأمین پویا نیاز مدیران کلاستر به
تأمین پیشاپیش ذخیره‌سازی را از میان برمی‌دارد. در عوض، هنگامی که کاربران
[آبجکت‌های `PersistentVolumeClaim`](/docs/concepts/storage/persistent-volumes/) ایجاد می‌کنند،
ذخیره‌سازی به‌طور خودکار تأمین می‌شود.

<!-- body -->

## پیش‌زمینه

پیاده‌سازی تأمین پویای حجم بر پایهٔ آبجکت API با نوع `StorageClass`
از گروه API با نام `storage.k8s.io` است. مدیر کلاستر می‌تواند هر تعداد
آبجکت `StorageClass` که لازم باشد تعریف کند، که هر یک یک *افزونهٔ حجم* (volume plugin) (یا همان
*provisioner*) را مشخص می‌کند که حجم را تأمین می‌کند، و همچنین مجموعه‌ای از پارامترها را که هنگام تأمین
به آن provisioner ارسال می‌شوند.
مدیر کلاستر می‌تواند انواع گوناگونی از ذخیره‌سازی (از همان سامانهٔ ذخیره‌سازی
یا از سامانه‌های متفاوت) را در یک کلاستر تعریف و ارائه کند، که هر کدام مجموعهٔ پارامترهای سفارشی خود را دارند. این طراحی همچنین تضمین می‌کند که کاربران نهایی
لازم نیست نگران پیچیدگی‌ها و جزئیات چگونگی تأمین ذخیره‌سازی باشند، اما همچنان
می‌توانند از میان چند گزینهٔ ذخیره‌سازی انتخاب کنند.

برای جزئیات بیشتر، به مفهوم [Storage Classes](/docs/concepts/storage/storage-classes/) مراجعه کنید.

## فعال‌سازی تأمین پویا

برای فعال‌سازی تأمین پویا، مدیر کلاستر باید از پیش یک یا چند آبجکت StorageClass
را برای کاربران ایجاد کند.
آبجکت‌های StorageClass مشخص می‌کنند که کدام provisioner باید استفاده شود و هنگام فراخوانی تأمین پویا
چه پارامترهایی باید به آن provisioner ارسال شوند.
نام یک آبجکت StorageClass باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

مانifest زیر یک storage class با نام «slow» ایجاد می‌کند که دیسک‌های پایدار (persistent disk)
از نوع دیسک استاندارد را تأمین می‌کند.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: slow
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard
```

مانifest زیر یک storage class با نام «fast» ایجاد می‌کند که دیسک‌های پایدار
از نوع SSD را تأمین می‌کند.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
```

## استفاده از تأمین پویا

کاربران با افزودن یک storage class به `PersistentVolumeClaim` خود، ذخیره‌سازی با تأمین پویا را درخواست می‌کنند. پیش از کوبرنتیز نسخهٔ v1.6، این کار از طریق
حاشیه‌نویسی (annotation) با نام `volume.beta.kubernetes.io/storage-class` انجام می‌شد. با این حال، این annotation
از نسخهٔ v1.9 منسوخ شده است. اکنون کاربران می‌توانند و باید به‌جای آن از
فیلد `storageClassName` در آبجکت `PersistentVolumeClaim` استفاده کنند. مقدار
این فیلد باید با نام یک `StorageClass` که مدیر پیکربندی کرده است مطابقت داشته باشد
(بخش [فعال‌سازی تأمین پویا](#enabling-dynamic-provisioning) را ببینید).

برای مثال، برای انتخاب storage class با نام «fast»، کاربر
PersistentVolumeClaim زیر را ایجاد می‌کند:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: claim1
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast
  resources:
    requests:
      storage: 30Gi
```

این claim موجب می‌شود یک Persistent Disk از نوع SSD به‌طور خودکار
تأمین شود. هنگامی که claim حذف شود، حجم نیز از بین می‌رود.

## رفتار پیش‌فرض

تأمین پویا را می‌توان روی یک کلاستر طوری فعال کرد که اگر هیچ storage class مشخص نشده باشد، همهٔ claimها
به‌صورت پویا تأمین شوند. مدیر کلاستر
می‌تواند این رفتار را از راه زیر فعال کند:

- علامت‌گذاری یک آبجکت `StorageClass` به‌عنوان *پیش‌فرض* (default).
- اطمینان از اینکه [admission controller با نام `DefaultStorageClass`](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
  روی سرور API فعال است.

مدیر می‌تواند با افزودن [annotation با نام `storageclass.kubernetes.io/is-default-class`](/docs/reference/labels-annotations-taints/#storageclass-kubernetes-io-is-default-class)
به یک `StorageClass` مشخص، آن را به‌عنوان پیش‌فرض علامت‌گذاری کند.
هنگامی که یک `StorageClass` پیش‌فرض در کلاستر وجود داشته باشد و کاربر یک
`PersistentVolumeClaim` ایجاد کند که `storageClassName` در آن مشخص نشده است،
admission controller با نام `DefaultStorageClass` به‌طور خودکار فیلد
`storageClassName` را که به storage class پیش‌فرض اشاره می‌کند اضافه می‌کند.

توجه داشته باشید که اگر annotation با نام `storageclass.kubernetes.io/is-default-class`
را روی بیش از یک StorageClass در کلاستر خود برابر true قرار دهید و سپس
یک `PersistentVolumeClaim` بدون `storageClassName` ایجاد کنید، کوبرنتیز
از جدیدترین StorageClass پیش‌فرضی که ایجاد شده است استفاده می‌کند.

## آگاهی از توپولوژی

در کلاسترهای [چندمنطقه‌ای (Multi-Zone)](/docs/setup/best-practices/multiple-zones/)، Podها می‌توانند در
چند Zone از یک Region پراکنده شوند. بک‌اندهای ذخیره‌سازی تک‌منطقه‌ای (Single-Zone) باید در Zoneهایی تأمین شوند که
Podها در آن‌ها زمان‌بندی می‌شوند. این کار را می‌توان با تنظیم
[حالت اتصال حجم (Volume Binding Mode)](/docs/concepts/storage/storage-classes/#volume-binding-mode) انجام داد.
