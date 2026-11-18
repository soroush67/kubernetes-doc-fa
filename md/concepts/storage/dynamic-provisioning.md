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

با تأمین پویای حجم (dynamic volume provisioning) می‌توان حجم‌های ذخیره‌سازی را در هنگام نیاز ایجاد کرد.
بدون تأمین پویا، مدیران کلاستر باید برای ایجاد حجم‌های ذخیره‌سازی جدید، به‌صورت دستی
با ارائه‌دهندهٔ ابری یا ذخیره‌سازی خود تماس بگیرند و سپس
[آبجکت‌های `PersistentVolume`](/docs/concepts/storage/persistent-volumes/)
را برای نمایش آن‌ها در کوبرنتیز ایجاد کنند. قابلیت تأمین پویا نیاز مدیران کلاستر به
تأمین پیشاپیش ذخیره‌سازی را از بین می‌برد. در عوض، این قابلیت هنگامی که کاربران
[آبجکت‌های `PersistentVolumeClaim`](/docs/concepts/storage/persistent-volumes/)
را ایجاد می‌کنند، ذخیره‌سازی را به‌طور خودکار تأمین می‌کند.

<!-- body -->

## پیش‌زمینه

پیاده‌سازی تأمین پویای حجم بر پایهٔ آبجکت API با نام `StorageClass`
از گروه API `storage.k8s.io` است. مدیر کلاستر می‌تواند به هر تعداد که لازم باشد
آبجکت `StorageClass` تعریف کند. هر یک از این آبجکت‌ها یک *افزونهٔ حجم* (volume plugin)
(که *تأمین‌کننده* یا provisioner نیز نامیده می‌شود) را مشخص می‌کند که حجم را تأمین می‌کند،
و همچنین مجموعه‌ای از پارامترها را که هنگام تأمین باید به آن تأمین‌کننده ارسال شوند.
مدیر کلاستر می‌تواند چندین نوع ذخیره‌سازی (از سامانه‌های ذخیره‌سازی یکسان یا متفاوت)
را در یک کلاستر تعریف و در دسترس قرار دهد که هر کدام مجموعه‌ای سفارشی از پارامترها دارند.
این طراحی همچنین تضمین می‌کند که کاربران نهایی نگران پیچیدگی‌ها و ظرافت‌های چگونگی
تأمین ذخیره‌سازی نباشند و در عین حال بتوانند از میان چندین گزینهٔ ذخیره‌سازی انتخاب کنند.

برای جزئیات بیشتر، مفهوم [کلاس‌های ذخیره‌سازی](/docs/concepts/storage/storage-classes/) را ببینید.

## فعال‌سازی تأمین پویا

برای فعال‌سازی تأمین پویا، مدیر کلاستر باید از پیش یک یا چند آبجکت StorageClass
برای کاربران ایجاد کند.
آبجکت‌های StorageClass مشخص می‌کنند که هنگام فراخوانی تأمین پویا از کدام تأمین‌کننده
استفاده شود و چه پارامترهایی به آن ارسال شوند.
نام هر آبجکت StorageClass باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

مانیفست زیر کلاس ذخیره‌سازی‌ای با نام «slow» ایجاد می‌کند که دیسک‌های پایای
استاندارد و مشابه دیسک‌های معمولی را تأمین می‌کند.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: slow
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard
```

مانیفست زیر کلاس ذخیره‌سازی‌ای با نام «fast» ایجاد می‌کند که دیسک‌های پایای
مشابه SSD را تأمین می‌کند.

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

کاربران با درج یک کلاس ذخیره‌سازی در `PersistentVolumeClaim` خود، ذخیره‌سازی
تأمین‌شده به‌صورت پویا را درخواست می‌کنند. پیش از نسخهٔ v1.6 کوبرنتیز، این کار با
حاشیه‌نویسی (annotation) `volume.beta.kubernetes.io/storage-class` انجام می‌شد. اما این
حاشیه‌نویسی از نسخهٔ v1.9 منسوخ شده است. اکنون کاربران می‌توانند و باید به‌جای آن از فیلد
`storageClassName` در آبجکت `PersistentVolumeClaim` استفاده کنند. مقدار
این فیلد باید با نام یکی از `StorageClass`هایی که مدیر پیکربندی کرده است مطابقت داشته باشد
([فعال‌سازی تأمین پویا](#enabling-dynamic-provisioning) را ببینید).

برای مثال، کاربر برای انتخاب کلاس ذخیره‌سازی «fast» باید
PersistentVolumeClaim زیر را ایجاد کند:

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

این درخواست باعث می‌شود یک دیسک پایای مشابه SSD به‌طور خودکار
تأمین شود. هنگامی که این درخواست حذف شود، حجم نیز از بین می‌رود.

## رفتار پیش‌فرض

می‌توان تأمین پویا را در کلاستر به‌گونه‌ای فعال کرد که اگر هیچ کلاس ذخیره‌سازی‌ای
مشخص نشده باشد، همهٔ درخواست‌ها به‌صورت پویا تأمین شوند. مدیر کلاستر
می‌تواند این رفتار را به این روش فعال کند:

- علامت‌گذاری یک آبجکت `StorageClass` به‌عنوان *پیش‌فرض*.
- اطمینان از اینکه [کنترل‌کنندهٔ پذیرش `DefaultStorageClass`](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
  روی سرور API فعال است.

مدیر می‌تواند با افزودن
[حاشیه‌نویسی `storageclass.kubernetes.io/is-default-class`](/docs/reference/labels-annotations-taints/#storageclass-kubernetes-io-is-default-class)
به یک `StorageClass` مشخص، آن را به‌عنوان پیش‌فرض علامت‌گذاری کند.
هنگامی که یک `StorageClass` پیش‌فرض در کلاستر وجود داشته باشد و کاربر یک
`PersistentVolumeClaim` بدون تعیین `storageClassName` ایجاد کند،
کنترل‌کنندهٔ پذیرش `DefaultStorageClass` به‌طور خودکار فیلد
`storageClassName` را با اشاره به کلاس ذخیره‌سازی پیش‌فرض اضافه می‌کند.

توجه کنید که اگر حاشیه‌نویسی `storageclass.kubernetes.io/is-default-class`
را روی بیش از یک StorageClass در کلاستر خود برابر true قرار دهید و سپس
یک `PersistentVolumeClaim` بدون تنظیم `storageClassName` ایجاد کنید، کوبرنتیز
از جدیدترین StorageClass پیش‌فرض ایجادشده استفاده می‌کند.

## آگاهی از توپولوژی

در کلاسترهای [چندناحیه‌ای](/docs/setup/best-practices/multiple-zones/)، Podها می‌توانند در
ناحیه‌های (Zone) مختلف یک منطقه (Region) پخش شوند. پشتیبان‌های ذخیره‌سازی تک‌ناحیه‌ای باید در ناحیه‌هایی
تأمین شوند که Podها در آن‌ها زمان‌بندی شده‌اند. این کار با تنظیم
[حالت اتصال حجم](/docs/concepts/storage/storage-classes/#volume-binding-mode) امکان‌پذیر است.
