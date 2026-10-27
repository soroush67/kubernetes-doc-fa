---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
title: Storage Classها
api_metadata:
- apiVersion: "storage.k8s.io/v1"
  kind: "StorageClass"
content_type: concept
weight: 40
---

<!-- overview -->

این سند مفهوم StorageClass را در کوبرنتیز شرح می‌دهد. آشنایی
با [حجم‌ها](/docs/concepts/storage/volumes/) و
[حجم‌های پایدار](/docs/concepts/storage/persistent-volumes) توصیه می‌شود.

StorageClass روشی در اختیار مدیران قرار می‌دهد تا _کلاس‌های_ ذخیره‌سازی‌ای را
که ارائه می‌کنند توصیف کنند. کلاس‌های مختلف ممکن است به سطوح کیفیت خدمات،
یا به سیاست‌های پشتیبان‌گیری، یا به سیاست‌های دلخواهی که مدیران کلاستر تعیین می‌کنند
نگاشت شوند. خود کوبرنتیز دربارهٔ اینکه کلاس‌ها چه چیزی را نشان می‌دهند
دیدگاه خاصی ندارد.

مفهوم storage class در کوبرنتیز مشابه «پروفایل‌ها» در برخی دیگر از
طراحی‌های سیستم ذخیره‌سازی است.

<!-- body -->

## آبجکت‌های StorageClass

هر StorageClass شامل فیلدهای `provisioner`، `parameters` و
`reclaimPolicy` است که زمانی استفاده می‌شوند که یک PersistentVolume متعلق به
آن کلاس باید برای برآورده کردن یک PersistentVolumeClaim (PVC) به‌صورت پویا تأمین شود.

نام یک آبجکت StorageClass اهمیت دارد و کاربران از طریق آن می‌توانند
یک کلاس خاص را درخواست کنند. مدیران نام و سایر پارامترهای
یک کلاس را هنگام نخستین ایجاد آبجکت‌های StorageClass تعیین می‌کنند.

به‌عنوان مدیر، می‌توانید یک StorageClass پیش‌فرض مشخص کنید که برای همهٔ PVCهایی که
کلاس مشخصی درخواست نمی‌کنند اعمال شود. برای جزئیات بیشتر،
[مفهوم PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) را ببینید.

در ادامه نمونه‌ای از یک StorageClass آمده است:

{{% code_sample file="storage/storageclass-low-latency.yaml" %}}

## StorageClass پیش‌فرض

می‌توانید یک StorageClass را به‌عنوان پیش‌فرض کلاستر خود علامت‌گذاری کنید.
برای دستورالعمل تنظیم StorageClass پیش‌فرض، ببینید:
[تغییر StorageClass پیش‌فرض](/docs/tasks/administer-cluster/change-default-storage-class/).

هنگامی که یک PVC هیچ `storageClassName` مشخص نکند، StorageClass پیش‌فرض
استفاده می‌شود.

اگر حاشیه‌نویسی
[`storageclass.kubernetes.io/is-default-class`](/docs/reference/labels-annotations-taints/#storageclass-kubernetes-io-is-default-class)
را روی بیش از یک StorageClass در کلاستر خود true تنظیم کنید و سپس
یک PersistentVolumeClaim بدون تنظیم `storageClassName` ایجاد کنید، کوبرنتیز
از جدیدترین StorageClass پیش‌فرض ایجادشده استفاده می‌کند.

{{< note >}}
باید تلاش کنید تنها یک StorageClass در کلاستر خود داشته باشید که
به‌عنوان پیش‌فرض علامت‌گذاری شده است. دلیل اینکه کوبرنتیز اجازه می‌دهد
چندین StorageClass پیش‌فرض داشته باشید، فراهم کردن امکان مهاجرت بدون وقفه است.
{{< /note >}}

می‌توانید یک PersistentVolumeClaim را بدون مشخص کردن `storageClassName`
برای PVC جدید ایجاد کنید، و حتی زمانی که هیچ StorageClass پیش‌فرضی
در کلاستر شما وجود ندارد نیز می‌توانید این کار را انجام دهید. در این حالت، PVC جدید همان‌طور که تعریف کرده‌اید ایجاد می‌شود و
`storageClassName` آن PVC تا زمانی که یک پیش‌فرض در دسترس قرار گیرد تنظیم‌نشده باقی می‌ماند.

می‌توانید کلاستری بدون هیچ StorageClass پیش‌فرضی داشته باشید. اگر هیچ
StorageClassی را به‌عنوان پیش‌فرض علامت‌گذاری نکنید (و مثلاً یک ارائه‌دهندهٔ ابری نیز آن را برای شما تنظیم نکرده باشد)،
کوبرنتیز نمی‌تواند این مقداردهی پیش‌فرض را برای PersistentVolumeClaimهایی که به آن
نیاز دارند اعمال کند.

اگر یا هنگامی که یک StorageClass پیش‌فرض در دسترس قرار گیرد، control plane همهٔ
PVCهای موجود بدون `storageClassName` را شناسایی می‌کند. برای PVCهایی که یا مقدار
خالی برای `storageClassName` دارند یا این کلید را ندارند، control plane سپس
آن PVCها را به‌روزرسانی می‌کند تا `storageClassName` را مطابق StorageClass پیش‌فرض جدید تنظیم کند.
اگر یک PVC موجود دارید که `storageClassName` آن `""` است و یک
StorageClass پیش‌فرض پیکربندی می‌کنید، این PVC به‌روزرسانی نخواهد شد.

برای اینکه اتصال به PVهایی که `storageClassName` آن‌ها روی `""` تنظیم شده است
(در حالی که یک StorageClass پیش‌فرض وجود دارد) ادامه یابد، باید `storageClassName`
PVC مرتبط را روی `""` تنظیم کنید.

## Provisioner

هر StorageClass یک provisioner دارد که تعیین می‌کند از کدام پلاگین حجم
برای تأمین PVها استفاده شود. این فیلد باید مشخص شود.

| پلاگین حجم        | Provisioner داخلی |            نمونهٔ پیکربندی             |
| :------------------- | :------------------: | :-----------------------------------: |
| AzureFile            |       &#x2713;       |       [Azure File](#azure-file)       |
| CephFS               |          -           |                   -                   |
| FC                   |          -           |                   -                   |
| FlexVolume           |          -           |                   -                   |
| iSCSI                |          -           |                   -                   |
| Local                |          -           |            [Local](#local)            |
| NFS                  |          -           |              [NFS](#nfs)              |
| PortworxVolume       |       &#x2713;       |  [Portworx Volume](#portworx-volume)  |
| RBD                  |          -           |         [Ceph RBD](#ceph-rbd)         |
| VsphereVolume        |       &#x2713;       |          [vSphere](#vsphere)          |

شما به مشخص کردن provisionerهای «داخلی» فهرست‌شده در اینجا
(که نام آن‌ها با «kubernetes.io» آغاز می‌شود و همراه با کوبرنتیز
عرضه می‌شوند) محدود نیستید. همچنین می‌توانید provisionerهای خارجی را اجرا و مشخص کنید
که برنامه‌هایی مستقل هستند و از یک [مشخصه](https://github.com/kubernetes/design-proposals-archive/blob/main/storage/volume-provisioning.md)
تعریف‌شده توسط کوبرنتیز پیروی می‌کنند. نویسندگان provisionerهای خارجی اختیار کامل
دارند که کدشان کجا قرار گیرد، provisioner چگونه عرضه شود، چگونه باید
اجرا شود، از کدام پلاگین حجم (از جمله Flex) استفاده کند و غیره. مخزن
[kubernetes-sigs/sig-storage-lib-external-provisioner](https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner)
میزبان کتابخانه‌ای برای نوشتن provisionerهای خارجی است که بخش عمدهٔ
مشخصه را پیاده‌سازی می‌کند. برخی از provisionerهای خارجی در مخزن
[kubernetes-sigs/sig-storage-lib-external-provisioner](https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner) فهرست شده‌اند.

برای مثال، NFS یک provisioner داخلی ارائه نمی‌کند، اما می‌توان از یک provisioner
خارجی استفاده کرد. همچنین مواردی وجود دارد که فروشندگان ذخیره‌سازی
شخص ثالث provisioner خارجی خود را ارائه می‌کنند.

## سیاست بازپس‌گیری

PersistentVolumeهایی که به‌طور پویا توسط یک StorageClass ایجاد می‌شوند،
[سیاست بازپس‌گیری](/docs/concepts/storage/persistent-volumes/#reclaiming)ای
را خواهند داشت که در فیلد `reclaimPolicy` کلاس مشخص شده است و می‌تواند
`Delete` یا `Retain` باشد. اگر هنگام ایجاد یک آبجکت StorageClass هیچ `reclaimPolicy`
مشخص نشود، مقدار پیش‌فرض آن `Delete` خواهد بود.

PersistentVolumeهایی که به‌صورت دستی ایجاد شده و از طریق یک StorageClass مدیریت می‌شوند،
همان سیاست بازپس‌گیری‌ای را خواهند داشت که هنگام ایجاد به آن‌ها اختصاص داده شده است.

## گسترش حجم {#allow-volume-expansion}

PersistentVolumeها را می‌توان طوری پیکربندی کرد که قابل گسترش باشند. این امکان به شما اجازه می‌دهد
اندازهٔ حجم را با ویرایش آبجکت PVC متناظر و درخواست مقدار بزرگ‌تر جدیدی از
ذخیره‌سازی تغییر دهید.

انواع حجم زیر، هنگامی که StorageClass زیربنایی فیلد
`allowVolumeExpansion` را روی true تنظیم کرده باشد، از گسترش حجم پشتیبانی می‌کنند.

{{< table caption = "جدول انواع حجم و نسخهٔ کوبرنتیزی که نیاز دارند"  >}}

| نوع حجم          | نسخهٔ کوبرنتیز لازم برای گسترش حجم |
| :------------------- | :----------------------------------------------- |
| Azure File           | 1.11                                             |
| CSI                  | 1.24                                             |
| FlexVolume           | 1.13                                             |
| Portworx             | 1.11                                             |
| rbd                  | 1.11                                             |

{{< /table >}}

{{< note >}}
از قابلیت گسترش حجم تنها می‌توانید برای بزرگ کردن یک حجم استفاده کنید، نه برای کوچک کردن آن.
{{< /note >}}

## گزینه‌های mount

PersistentVolumeهایی که به‌طور پویا توسط یک StorageClass ایجاد می‌شوند،
گزینه‌های mountی را خواهند داشت که در فیلد `mountOptions` کلاس مشخص شده است.

اگر پلاگین حجم از گزینه‌های mount پشتیبانی نکند اما گزینه‌های mount
مشخص شده باشند، تأمین با شکست مواجه می‌شود. گزینه‌های mount نه در کلاس و نه در PV
اعتبارسنجی **نمی‌شوند**. اگر یک گزینهٔ mount نامعتبر باشد، mount کردن PV با شکست مواجه می‌شود.

## حالت اتصال حجم

فیلد `volumeBindingMode` کنترل می‌کند که
[اتصال حجم و تأمین پویا](/docs/concepts/storage/persistent-volumes/#provisioning)
چه زمانی باید رخ دهد. هنگامی که تنظیم نشده باشد، به‌طور پیش‌فرض از حالت `Immediate` استفاده می‌شود.

حالت `Immediate` نشان می‌دهد که اتصال حجم و تأمین
پویا به محض ایجاد PersistentVolumeClaim رخ می‌دهد. برای backendهای
ذخیره‌سازی که محدود به توپولوژی هستند و به‌صورت سراسری از همهٔ نودهای
کلاستر قابل دسترسی نیستند، PersistentVolumeها بدون آگاهی از الزامات زمان‌بندی Pod
متصل یا تأمین می‌شوند. این ممکن است به Podهای غیرقابل زمان‌بندی منجر شود.

مدیر کلاستر می‌تواند با مشخص کردن حالت `WaitForFirstConsumer` این مشکل را برطرف کند؛ این حالت
اتصال و تأمین یک PersistentVolume را تا زمان ایجاد یک Pod که از PersistentVolumeClaim استفاده می‌کند به تأخیر می‌اندازد.
PersistentVolumeها مطابق توپولوژی‌ای که توسط
محدودیت‌های زمان‌بندی Pod مشخص شده است انتخاب یا تأمین می‌شوند. این محدودیت‌ها شامل [الزامات
منابع](/docs/concepts/configuration/manage-resources-containers/)،
[انتخابگرهای نود](/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)،
[pod affinity و
anti-affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
و [taintها و tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration) هستند، اما به این‌ها محدود نمی‌شوند.

پلاگین‌های زیر از `WaitForFirstConsumer` همراه با تأمین پویا پشتیبانی می‌کنند:

- حجم‌های CSI، به شرط آنکه درایور CSI مربوط از آن پشتیبانی کند

پلاگین‌های زیر از `WaitForFirstConsumer` همراه با اتصال PersistentVolumeهای از پیش ایجادشده پشتیبانی می‌کنند:

- حجم‌های CSI، به شرط آنکه درایور CSI مربوط از آن پشتیبانی کند
- [`local`](#local)

{{< note >}}
اگر استفاده از `WaitForFirstConsumer` را انتخاب کنید، برای مشخص کردن node affinity
از `nodeName` در spec مربوط به Pod استفاده نکنید.
اگر در این حالت از `nodeName` استفاده شود، زمان‌بند دور زده می‌شود و PVC در وضعیت `pending` باقی می‌ماند.

به‌جای آن، می‌توانید از node selector برای `kubernetes.io/hostname` استفاده کنید:
{{< /note >}}

{{% code_sample language="yaml" file="storage/storageclass/pod-volume-binding.yaml" %}}

## توپولوژی‌های مجاز

هنگامی که اپراتور کلاستر حالت اتصال حجم `WaitForFirstConsumer` را مشخص می‌کند، در بیشتر موقعیت‌ها
دیگر لازم نیست تأمین را به توپولوژی‌های مشخصی محدود کرد. با این حال،
اگر همچنان لازم باشد، می‌توان `allowedTopologies` را مشخص کرد.

این مثال نشان می‌دهد که چگونه می‌توان توپولوژی حجم‌های تأمین‌شده را به
zoneهای مشخصی محدود کرد و باید به‌عنوان جایگزینی برای پارامترهای `zone` و `zones` در
پلاگین‌های پشتیبانی‌شده استفاده شود.

{{% code_sample language="yaml" file="storage/storageclass/storageclass-topology.yaml" %}}

## پارامترها

StorageClassها پارامترهایی دارند که حجم‌های متعلق به آن storage
class را توصیف می‌کنند. بسته به `provisioner`، ممکن است پارامترهای متفاوتی پذیرفته شوند.
هنگامی که یک پارامتر حذف شود، از یک مقدار پیش‌فرض استفاده می‌شود.

حداکثر ۵۱۲ پارامتر را می‌توان برای یک StorageClass تعریف کرد.
طول کل آبجکت parameters، شامل کلیدها و مقادیر آن، نمی‌تواند از
256 KiB بیشتر شود.

### AWS EBS

<!-- maintenance note: OK to remove all mention of awsElasticBlockStore once the v1.27 release of
Kubernetes has gone out of support -->

کوبرنتیز {{< skew currentVersion >}} نوع حجم `awsElasticBlockStore` را شامل نمی‌شود.

درایور ذخیره‌سازی درون‌درختی AWSElasticBlockStore در نسخهٔ v1.19 کوبرنتیز منسوخ شد
و سپس در نسخهٔ v1.27 به‌طور کامل حذف شد.

پروژهٔ کوبرنتیز پیشنهاد می‌کند به‌جای آن از درایور ذخیره‌سازی بیرون‌درختی
[AWS EBS](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) استفاده کنید.

در ادامه نمونه‌ای از StorageClass برای درایور AWS EBS CSI آمده است:

{{% code_sample language="yaml" file="storage/storageclass/storageclass-aws-ebs.yaml" %}}

`tagSpecification`: برچسب‌هایی (tag) با این پیشوند روی حجم‌های EBS که به‌صورت پویا تأمین شده‌اند اعمال می‌شوند.

### AWS EFS

برای پیکربندی ذخیره‌سازی AWS EFS، می‌توانید از درایور بیرون‌درختی [AWS_EFS_CSI_DRIVER](https://github.com/kubernetes-sigs/aws-efs-csi-driver) استفاده کنید.

{{% code_sample language="yaml" file="storage/storageclass/storageclass-aws-efs.yaml" %}}

- `provisioningMode`: نوع حجمی که باید توسط Amazon EFS تأمین شود. در حال حاضر، تنها تأمین مبتنی بر access point پشتیبانی می‌شود (`efs-ap`).
- `fileSystemId`: سیستم فایلی که access point زیر آن ایجاد می‌شود.
- `directoryPerms`: مجوزهای دایرکتوری ریشه‌ای که توسط access point ایجاد می‌شود.

برای جزئیات بیشتر، به مستندات [تأمین پویای AWS_EFS_CSI_Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/dynamic_provisioning/README.md) مراجعه کنید.


### NFS

برای پیکربندی ذخیره‌سازی NFS، می‌توانید از درایور درون‌درختی یا
[درایور NFS CSI برای کوبرنتیز](https://github.com/kubernetes-csi/csi-driver-nfs#readme)
(توصیه‌شده) استفاده کنید.

{{% code_sample language="yaml" file="storage/storageclass/storageclass-nfs.yaml" %}}

- `server`: نام میزبان یا نشانی IP سرور NFS.
- `path`: مسیری که توسط سرور NFS export شده است.
- `readOnly`: پرچمی که نشان می‌دهد آیا ذخیره‌سازی به‌صورت فقط‌خواندنی mount می‌شود یا نه (پیش‌فرض false).

کوبرنتیز یک provisioner داخلی برای NFS ندارد.
برای ایجاد یک StorageClass برای NFS باید از یک provisioner خارجی استفاده کنید.
در ادامه چند نمونه آمده است:

- [سرور NFS Ganesha و provisioner خارجی](https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner)
- [provisioner خارجی NFS subdir](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner)

### vSphere

دو نوع provisioner برای storage classهای vSphere وجود دارد:

- [CSI provisioner](#vsphere-provisioner-csi): `csi.vsphere.vmware.com`
- [vCP provisioner](#vcp-provisioner): `kubernetes.io/vsphere-volume`

provisionerهای درون‌درختی [منسوخ شده‌اند](/blog/2019/12/09/kubernetes-1-17-feature-csi-migration-beta/#why-are-we-migrating-in-tree-plugins-to-csi).
برای اطلاعات بیشتر دربارهٔ CSI provisioner، ببینید:
[درایور vSphere CSI کوبرنتیز](https://vsphere-csi-driver.sigs.k8s.io/) و
[مهاجرت vSphereVolume به CSI](/docs/concepts/storage/volumes/#vsphere-csi-migration).

#### CSI Provisioner {#vsphere-provisioner-csi}

provisioner مربوط به StorageClass در vSphere CSI با کلاسترهای Tanzu Kubernetes کار می‌کند.
برای یک نمونه، به [مخزن vSphere CSI](https://github.com/kubernetes-sigs/vsphere-csi-driver/blob/master/example/vanilla-k8s-RWM-filesystem-volumes/example-sc.yaml) مراجعه کنید.

#### vCP Provisioner

نمونه‌های زیر از provisioner مربوط به StorageClass در VMware Cloud Provider (vCP) استفاده می‌کنند.

1. یک StorageClass با قالب دیسکی که کاربر مشخص می‌کند ایجاد کنید.

   ```yaml
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast
   provisioner: kubernetes.io/vsphere-volume
   parameters:
     diskformat: zeroedthick
   ```

   `diskformat`: `thin`، `zeroedthick` و `eagerzeroedthick`. پیش‌فرض: `"thin"`.

2. یک StorageClass با یک قالب دیسک روی datastoreی که کاربر مشخص می‌کند ایجاد کنید.

   ```yaml
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast
   provisioner: kubernetes.io/vsphere-volume
   parameters:
     diskformat: zeroedthick
     datastore: VSANDatastore
   ```

   `datastore`: کاربر همچنین می‌تواند datastore را در StorageClass مشخص کند.
   حجم روی datastore مشخص‌شده در StorageClass ایجاد می‌شود
   که در این مورد `VSANDatastore` است. این فیلد اختیاری است. اگر
   datastore مشخص نشود، حجم روی datastoreی ایجاد می‌شود
   که در فایل پیکربندی vSphere که برای مقداردهی اولیهٔ vSphere Cloud
   Provider استفاده شده مشخص شده است.

3. مدیریت سیاست ذخیره‌سازی درون کوبرنتیز

   - استفاده از سیاست SPBM موجود در vCenter

     یکی از مهم‌ترین قابلیت‌های vSphere برای مدیریت ذخیره‌سازی،
     مدیریت مبتنی بر سیاست است. Storage Policy Based Management (SPBM) یک
     چارچوب سیاست ذخیره‌سازی است که یک control plane یکپارچهٔ واحد
     را در طیف گسترده‌ای از سرویس‌های داده و راه‌حل‌های ذخیره‌سازی فراهم می‌کند. SPBM به
     مدیران vSphere امکان می‌دهد بر چالش‌های اولیهٔ تأمین ذخیره‌سازی،
     مانند برنامه‌ریزی ظرفیت، سطوح خدمات متمایز و مدیریت
     ظرفیت ذخیره، غلبه کنند.

     سیاست‌های SPBM را می‌توان در StorageClass با استفاده از
     پارامتر `storagePolicyName` مشخص کرد.

   - پشتیبانی از سیاست Virtual SAN درون کوبرنتیز

     مدیران زیرساخت vSphere (VI) این امکان را خواهند داشت که قابلیت‌های
     ذخیره‌سازی سفارشی Virtual SAN را در هنگام تأمین پویای حجم مشخص کنند. اکنون
     می‌توانید الزامات ذخیره‌سازی، مانند کارایی و دسترس‌پذیری، را
     به شکل قابلیت‌های ذخیره‌سازی در هنگام تأمین پویای حجم تعریف کنید.
     الزامات قابلیت ذخیره‌سازی به یک سیاست Virtual SAN تبدیل می‌شوند
     که سپس هنگام ایجاد یک
     حجم پایدار (دیسک مجازی) به لایهٔ Virtual SAN ارسال می‌شود. دیسک مجازی برای برآورده کردن الزامات
     در سراسر datastore مربوط به Virtual SAN توزیع می‌شود.

     برای جزئیات بیشتر دربارهٔ نحوهٔ استفاده از سیاست‌های ذخیره‌سازی برای مدیریت حجم‌های پایدار،
     می‌توانید [مدیریت مبتنی بر سیاست ذخیره‌سازی برای تأمین پویای حجم‌ها](https://github.com/vmware-archive/vsphere-storage-for-kubernetes/blob/fa4c8b8ad46a85b6555d715dd9d27ff69839df53/documentation/policy-based-mgmt.md)
     را ببینید.

### Ceph RBD (منسوخ‌شده) {#ceph-rbd}

{{< note >}}
{{< feature-state state="deprecated" for_k8s_version="v1.28" >}}
این provisioner داخلی Ceph RBD منسوخ شده است. لطفاً از
[درایور CephFS RBD CSI](https://github.com/ceph/ceph-csi) استفاده کنید.
{{< /note >}}

{{% code_sample language="yaml" file="storage/storageclass/storageclass-ceph-rbd.yaml" %}}

- `monitors`: مانیتورهای Ceph، جداشده با کاما. این پارامتر الزامی است.
- `adminId`: شناسهٔ کلاینت Ceph که قادر به ایجاد ایمیج در pool است.
  پیش‌فرض "admin" است.
- `adminSecretName`: نام Secret برای `adminId`. این پارامتر الزامی است.
  secret ارائه‌شده باید از نوع "kubernetes.io/rbd" باشد.
- `adminSecretNamespace`: فضای نام مربوط به `adminSecretName`. پیش‌فرض "default" است.
- `pool`: pool مربوط به Ceph RBD. پیش‌فرض "rbd" است.
- `userId`: شناسهٔ کلاینت Ceph که برای نگاشت ایمیج RBD استفاده می‌شود. پیش‌فرض
  همان `adminId` است.
- `userSecretName`: نام Secret مربوط به Ceph برای `userId` جهت نگاشت ایمیج RBD. این Secret
  باید در همان فضای نام PVCها وجود داشته باشد. این پارامتر الزامی است.
  secret ارائه‌شده باید از نوع "kubernetes.io/rbd" باشد؛ برای مثال به این
  روش ایجاد شده باشد:

  ```shell
  kubectl create secret generic ceph-secret --type="kubernetes.io/rbd" \
    --from-literal=key='QVFEQ1pMdFhPUnQrSmhBQUFYaERWNHJsZ3BsMmNjcDR6RFZST0E9PQ==' \
    --namespace=kube-system
  ```

- `userSecretNamespace`: فضای نام مربوط به `userSecretName`.
- `fsType`: fsType پشتیبانی‌شده توسط کوبرنتیز. پیش‌فرض: `"ext4"`.
- `imageFormat`: قالب ایمیج Ceph RBD، "1" یا "2". پیش‌فرض "2" است.
- `imageFeatures`: این پارامتر اختیاری است و تنها در صورتی باید استفاده شود که
  `imageFormat` را روی "2" تنظیم کرده باشید. در حال حاضر تنها قابلیت `layering` پشتیبانی می‌شود.
  پیش‌فرض "" است و هیچ قابلیتی فعال نمی‌شود.

### Azure Disk

<!-- maintenance note: OK to remove all mention of azureDisk once the v1.27 release of
Kubernetes has gone out of support -->

کوبرنتیز {{< skew currentVersion >}} نوع حجم `azureDisk` را شامل نمی‌شود.

درایور ذخیره‌سازی درون‌درختی `azureDisk` در نسخهٔ v1.19 کوبرنتیز منسوخ شد
و سپس در نسخهٔ v1.27 به‌طور کامل حذف شد.

پروژهٔ کوبرنتیز پیشنهاد می‌کند به‌جای آن از درایور ذخیره‌سازی شخص ثالث
[Azure Disk](https://github.com/kubernetes-sigs/azuredisk-csi-driver) استفاده کنید.

### Azure File (منسوخ‌شده) {#azure-file}

{{% code_sample language="yaml" file="storage/storageclass/storageclass-azure-file.yaml" %}}

- `skuName`: ردهٔ SKU حساب ذخیره‌سازی Azure. پیش‌فرض خالی است.
- `location`: مکان حساب ذخیره‌سازی Azure. پیش‌فرض خالی است.
- `storageAccount`: نام حساب ذخیره‌سازی Azure. پیش‌فرض خالی است. اگر حساب
  ذخیره‌سازی ارائه نشود، همهٔ حساب‌های ذخیره‌سازی مرتبط با resource
  group جست‌وجو می‌شوند تا حسابی که با `skuName` و `location` مطابقت دارد پیدا شود. اگر
  حساب ذخیره‌سازی ارائه شود، باید در همان resource group کلاستر قرار داشته باشد
  و `skuName` و `location` نادیده گرفته می‌شوند.
- `secretNamespace`: فضای نام secretی که شامل نام و کلید حساب ذخیره‌سازی Azure
  است. پیش‌فرض همان فضای نام Pod است.
- `secretName`: نام secretی که شامل نام و کلید حساب ذخیره‌سازی Azure
  است. پیش‌فرض `azure-storage-account-<accountName>-secret` است.
- `readOnly`: پرچمی که نشان می‌دهد آیا ذخیره‌سازی به‌صورت فقط‌خواندنی mount می‌شود یا نه.
  پیش‌فرض false است، یعنی mount خواندنی/نوشتنی. این تنظیم بر
  تنظیم `ReadOnly` در VolumeMounts نیز تأثیر می‌گذارد.

در هنگام تأمین ذخیره‌سازی، یک secret با نامی که `secretName` تعیین می‌کند برای
اعتبارنامه‌های mount ایجاد می‌شود. اگر کلاستر هم
[RBAC](/docs/reference/access-authn-authz/rbac/) و هم
[Controller Roles](/docs/reference/access-authn-authz/rbac/#controller-roles) را فعال کرده باشد،
مجوز `create` برای منبع `secret` را به clusterrole
`system:controller:persistent-volume-binder` اضافه کنید.

در یک محیط چندمستأجری (multi-tenancy)، اکیداً توصیه می‌شود مقدار
`secretNamespace` را به‌صراحت تنظیم کنید، در غیر این صورت اعتبارنامه‌های حساب ذخیره‌سازی ممکن است
توسط کاربران دیگر خوانده شوند.

### حجم Portworx (منسوخ‌شده) {#portworx-volume}

{{% code_sample language="yaml" file="storage/storageclass/storageclass-portworx-volume.yaml" %}}

- `fs`: سیستم فایلی که باید ایجاد شود: `none/xfs/ext4` (پیش‌فرض: `ext4`).
- `block_size`: اندازهٔ بلوک بر حسب کیلوبایت (پیش‌فرض: `32`).
- `repl`: تعداد replicaهای همگامی که باید به شکل ضریب تکثیر
  `1..3` فراهم شوند (پیش‌فرض: `1`). در اینجا یک رشته انتظار می‌رود، یعنی
  `"1"` و نه `1`.
- `priority_io`: تعیین می‌کند که حجم از ذخیره‌سازی با کارایی بالاتر
  یا اولویت پایین‌تر ایجاد شود: `high/medium/low` (پیش‌فرض: `low`).
- `snap_interval`: بازهٔ زمانی بر حسب دقیقه برای زمان راه‌اندازی snapshotها.
  snapshotها بر اساس تفاوت با snapshot قبلی افزایشی هستند؛ مقدار 0
  snapshotها را غیرفعال می‌کند (پیش‌فرض: `0`). در اینجا یک رشته انتظار می‌رود، یعنی
  `"70"` و نه `70`.
- `aggregation_level`: تعداد بخش‌هایی (chunk) را که حجم میان آن‌ها
  توزیع می‌شود مشخص می‌کند؛ 0 نشان‌دهندهٔ حجم غیرتجمیعی است (پیش‌فرض: `0`). در اینجا یک رشته
  انتظار می‌رود، یعنی `"0"` و نه `0`
- `ephemeral`: مشخص می‌کند که آیا حجم باید پس از unmount پاک‌سازی شود
  یا پایدار بماند. در کاربرد `emptyDir` می‌توان این مقدار را true تنظیم کرد و
  در کاربرد `persistent volumes`، مانند پایگاه‌های داده‌ای همچون Cassandra، باید
  false تنظیم شود: `true/false` (پیش‌فرض `false`). در اینجا یک رشته انتظار می‌رود، یعنی
  `"true"` و نه `true`.

### Local

{{% code_sample language="yaml" file="storage/storageclass/storageclass-local.yaml" %}}

حجم‌های Local در کوبرنتیز {{< skew currentVersion >}} از تأمین پویا پشتیبانی نمی‌کنند؛
با این حال، همچنان باید یک StorageClass ایجاد شود تا اتصال حجم تا زمانی که یک Pod واقعاً
روی نود مناسب زمان‌بندی شود به تأخیر بیفتد. این موضوع با حالت اتصال حجم
`WaitForFirstConsumer` مشخص می‌شود.

به تأخیر انداختن اتصال حجم به زمان‌بند امکان می‌دهد هنگام انتخاب یک
PersistentVolume مناسب برای یک PersistentVolumeClaim، همهٔ محدودیت‌های
زمان‌بندی Pod را در نظر بگیرد.
