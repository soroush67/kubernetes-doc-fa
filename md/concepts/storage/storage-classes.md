---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
title: کلاس‌های ذخیره‌سازی
api_metadata:
- apiVersion: "storage.k8s.io/v1"
  kind: "StorageClass"
content_type: concept
weight: 40
---

<!-- overview -->

این سند مفهوم StorageClass را در کوبرنتیز شرح می‌دهد. پیشنهاد می‌شود پیش از مطالعه‌ی آن با [حجم‌ها (volumes)](/docs/concepts/storage/volumes/) و
[حجم‌های پایدار (persistent volumes)](/docs/concepts/storage/persistent-volumes) آشنا باشید.

هر StorageClass راهی در اختیار مدیران قرار می‌دهد تا _کلاس‌های_ ذخیره‌سازی‌ای را که ارائه می‌کنند توصیف کنند. کلاس‌های مختلف ممکن است با سطوح کیفیت خدمات، سیاست‌های پشتیبان‌گیری یا هر سیاست دلخواهی که مدیران کلاستر تعیین می‌کنند متناظر باشند. خود کوبرنتیز درباره‌ی معنای این کلاس‌ها هیچ دیدگاه از پیش تعیین‌شده‌ای ندارد.

مفهوم کلاس ذخیره‌سازی در کوبرنتیز به «پروفایل‌ها» در طراحی برخی دیگر از سامانه‌های ذخیره‌سازی شباهت دارد.

<!-- body -->

## آبجکت‌های StorageClass

هر StorageClass فیلدهای `provisioner`، `parameters` و `reclaimPolicy` را دارد. این فیلدها زمانی به کار می‌روند که لازم باشد یک PersistentVolume متعلق به آن کلاس به‌صورت پویا تأمین شود تا یک PersistentVolumeClaim (PVC) را برآورده کند.

نام آبجکت StorageClass اهمیت دارد، زیرا کاربران با همین نام یک کلاس مشخص را درخواست می‌کنند. مدیران نام و سایر پارامترهای هر کلاس را هنگام ایجاد نخستین آبجکت‌های StorageClass تعیین می‌کنند.

شما به‌عنوان مدیر می‌توانید یک StorageClass پیش‌فرض تعیین کنید که برای همه‌ی PVCهایی که کلاس مشخصی درخواست نمی‌کنند اعمال شود. برای جزئیات بیشتر،
[مفهوم PersistentVolumeClaim](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) را ببینید.

در ادامه نمونه‌ای از یک StorageClass آمده است:

{{% code_sample file="storage/storageclass-low-latency.yaml" %}}

## StorageClass پیش‌فرض

می‌توانید یک StorageClass را به‌عنوان پیش‌فرض کلاستر خود علامت‌گذاری کنید.
برای دستورالعمل تنظیم StorageClass پیش‌فرض،
[تغییر StorageClass پیش‌فرض](/docs/tasks/administer-cluster/change-default-storage-class/) را ببینید.

هنگامی که یک PVC مقدار `storageClassName` را مشخص نکند، StorageClass پیش‌فرض به کار می‌رود.

اگر حاشیه‌نویسی (annotation)
[`storageclass.kubernetes.io/is-default-class`](/docs/reference/labels-annotations-taints/#storageclass-kubernetes-io-is-default-class)
را روی بیش از یک StorageClass در کلاستر خود برابر true قرار دهید و سپس یک PersistentVolumeClaim بدون تنظیم `storageClassName` ایجاد کنید، کوبرنتیز از جدیدترین StorageClass پیش‌فرضِ ایجادشده استفاده می‌کند.

{{< note >}}
بهتر است تلاش کنید فقط یک StorageClass در کلاستر شما به‌عنوان پیش‌فرض علامت‌گذاری شده باشد. دلیل اینکه کوبرنتیز اجازه می‌دهد چند StorageClass پیش‌فرض داشته باشید، امکان‌پذیر کردن مهاجرت بی‌وقفه است.
{{< /note >}}

می‌توانید یک PersistentVolumeClaim ایجاد کنید و برای این PVC جدید مقدار `storageClassName` را مشخص نکنید؛ این کار حتی زمانی که هیچ StorageClass پیش‌فرضی در کلاستر شما وجود ندارد نیز ممکن است. در این حالت، PVC جدید همان‌گونه که تعریفش کرده‌اید ایجاد می‌شود و `storageClassName` آن تا زمانی که یک کلاس پیش‌فرض در دسترس قرار گیرد، بدون مقدار باقی می‌ماند.

می‌توانید کلاستری بدون هیچ StorageClass پیش‌فرضی داشته باشید. اگر هیچ StorageClassای را به‌عنوان پیش‌فرض علامت‌گذاری نکنید (و مثلاً یک ارائه‌دهنده‌ی ابری نیز چنین کلاسی را برایتان تنظیم نکرده باشد)، کوبرنتیز نمی‌تواند مقدار پیش‌فرض را برای PersistentVolumeClaimهایی که به آن نیاز دارند اعمال کند.

اگر یا هنگامی که یک StorageClass پیش‌فرض در دسترس قرار گیرد، control plane همه‌ی PVCهای موجودِ بدون `storageClassName` را شناسایی می‌کند. سپس control plane آن PVCهایی را که یا مقدار `storageClassName` در آن‌ها خالی است یا اصلاً این کلید را ندارند، به‌روزرسانی می‌کند تا `storageClassName` آن‌ها با StorageClass پیش‌فرض جدید مطابقت داشته باشد.
اگر PVC موجودی داشته باشید که `storageClassName` آن برابر `""` است و یک StorageClass پیش‌فرض پیکربندی کنید، این PVC به‌روزرسانی نخواهد شد.

برای اینکه اتصال به PVهایی که `storageClassName` آن‌ها برابر `""` است حفظ شود (در حالی که یک StorageClass پیش‌فرض وجود دارد)، باید `storageClassName` مربوط به PVC متناظر را برابر `""` قرار دهید.

## تأمین‌کننده

هر StorageClass یک تأمین‌کننده (provisioner) دارد که تعیین می‌کند برای تأمین PVها از کدام افزونه‌ی حجم استفاده شود. این فیلد باید حتماً مشخص شود.

| افزونه‌ی حجم        | تأمین‌کننده‌ی داخلی |            نمونه‌ی پیکربندی             |
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

شما محدود به استفاده از تأمین‌کننده‌های «داخلی» فهرست‌شده در اینجا نیستید (تأمین‌کننده‌هایی که نامشان با پیشوند "kubernetes.io" آغاز می‌شود و همراه با کوبرنتیز عرضه می‌شوند). می‌توانید تأمین‌کننده‌های خارجی را نیز اجرا و مشخص کنید؛ این تأمین‌کننده‌ها برنامه‌هایی مستقل هستند که از یک [مشخصه](https://github.com/kubernetes/design-proposals-archive/blob/main/storage/volume-provisioning.md) تعریف‌شده توسط کوبرنتیز پیروی می‌کنند. نویسندگان تأمین‌کننده‌های خارجی درباره‌ی محل نگهداری کد، شیوه‌ی عرضه‌ی تأمین‌کننده، نحوه‌ی اجرای آن، افزونه‌ی حجمی که استفاده می‌کند (از جمله Flex) و موارد مشابه اختیار کامل دارند. مخزن
[kubernetes-sigs/sig-storage-lib-external-provisioner](https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner)
کتابخانه‌ای برای نوشتن تأمین‌کننده‌های خارجی در خود دارد که بخش عمده‌ی این مشخصه را پیاده‌سازی می‌کند. برخی از تأمین‌کننده‌های خارجی در مخزن
[kubernetes-sigs/sig-storage-lib-external-provisioner](https://github.com/kubernetes-sigs/sig-storage-lib-external-provisioner) فهرست شده‌اند.

برای مثال، NFS تأمین‌کننده‌ی داخلی ندارد، اما می‌توان از یک تأمین‌کننده‌ی خارجی برای آن استفاده کرد. همچنین مواردی وجود دارد که فروشندگان شخص ثالثِ ذخیره‌سازی، تأمین‌کننده‌ی خارجی خودشان را ارائه می‌کنند.

## سیاست بازپس‌گیری

برای PersistentVolumeهایی که به‌صورت پویا توسط یک StorageClass ایجاد می‌شوند، [سیاست بازپس‌گیری](/docs/concepts/storage/persistent-volumes/#reclaiming) همان مقداری خواهد بود که در فیلد `reclaimPolicy` کلاس مشخص شده است؛ این مقدار می‌تواند `Delete` یا `Retain` باشد. اگر هنگام ایجاد آبجکت StorageClass مقداری برای `reclaimPolicy` مشخص نشود، مقدار پیش‌فرض آن `Delete` خواهد بود.

PersistentVolumeهایی که به‌صورت دستی ایجاد شده و از طریق یک StorageClass مدیریت می‌شوند، همان سیاست بازپس‌گیری‌ای را خواهند داشت که هنگام ایجاد به آن‌ها اختصاص داده شده است.

## گسترش حجم {#allow-volume-expansion}

می‌توان PersistentVolumeها را به‌گونه‌ای پیکربندی کرد که قابل گسترش باشند. با این کار می‌توانید اندازه‌ی حجم را با ویرایش آبجکت PVC متناظر و درخواست مقدار بیشتری از فضای ذخیره‌سازی تغییر دهید.

انواع حجم زیر، زمانی که فیلد `allowVolumeExpansion` در StorageClass زیربنایی برابر true باشد، از گسترش حجم پشتیبانی می‌کنند.

{{< table caption = "جدول انواع حجم و نسخه‌ی کوبرنتیزِ موردنیاز آن‌ها"  >}}

| نوع حجم          | نسخه‌ی کوبرنتیزِ موردنیاز برای گسترش حجم |
| :------------------- | :----------------------------------------------- |
| Azure File           | 1.11                                             |
| CSI                  | 1.24                                             |
| FlexVolume           | 1.13                                             |
| Portworx             | 1.11                                             |
| rbd                  | 1.11                                             |

{{< /table >}}

{{< note >}}
از قابلیت گسترش حجم فقط می‌توانید برای بزرگ کردن یک حجم استفاده کنید، نه برای کوچک کردن آن.
{{< /note >}}

## گزینه‌های mount

PersistentVolumeهایی که به‌صورت پویا توسط یک StorageClass ایجاد می‌شوند، گزینه‌های mount مشخص‌شده در فیلد `mountOptions` کلاس را خواهند داشت.

اگر افزونه‌ی حجم از گزینه‌های mount پشتیبانی نکند اما این گزینه‌ها مشخص شده باشند، تأمین با شکست مواجه می‌شود. گزینه‌های mount نه در کلاس و نه در PV اعتبارسنجی **نمی‌شوند**. اگر یک گزینه‌ی mount نامعتبر باشد، mount کردن PV با شکست مواجه می‌شود.

## حالت اتصال حجم

فیلد `volumeBindingMode` تعیین می‌کند که
[اتصال حجم و تأمین پویا](/docs/concepts/storage/persistent-volumes/#provisioning)
چه زمانی انجام شود. اگر این فیلد تنظیم نشده باشد، به‌طور پیش‌فرض از حالت `Immediate` استفاده می‌شود.

حالت `Immediate` نشان می‌دهد که اتصال حجم و تأمین پویا بلافاصله پس از ایجاد PersistentVolumeClaim انجام می‌شود. در مورد پشتیبان‌های ذخیره‌سازی‌ای که محدود به توپولوژی هستند و از همه‌ی نودهای کلاستر به‌صورت سراسری در دسترس نیستند، PersistentVolumeها بدون آگاهی از الزامات زمان‌بندی Pod متصل یا تأمین می‌شوند. این وضعیت ممکن است به Podهایی منجر شود که قابل زمان‌بندی نیستند.

مدیر کلاستر می‌تواند با تعیین حالت `WaitForFirstConsumer` این مشکل را برطرف کند؛ این حالت اتصال و تأمین PersistentVolume را تا زمان ایجاد یک Pod که از PersistentVolumeClaim استفاده می‌کند به تأخیر می‌اندازد. در این صورت، PersistentVolumeها مطابق با توپولوژی‌ای که محدودیت‌های زمان‌بندی Pod مشخص می‌کنند انتخاب یا تأمین می‌شوند. این محدودیت‌ها شامل [الزامات منابع](/docs/concepts/configuration/manage-resources-containers/)،
[انتخابگرهای نود](/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)،
[وابستگی و ناوابستگی Pod](/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
و [taintها و tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration) هستند، اما به این موارد محدود نمی‌شوند.

افزونه‌های زیر از `WaitForFirstConsumer` همراه با تأمین پویا پشتیبانی می‌کنند:

- حجم‌های CSI، به شرط آنکه درایور CSI مربوطه از این قابلیت پشتیبانی کند

افزونه‌های زیر از `WaitForFirstConsumer` همراه با اتصال PersistentVolumeهای از پیش ایجادشده پشتیبانی می‌کنند:

- حجم‌های CSI، به شرط آنکه درایور CSI مربوطه از این قابلیت پشتیبانی کند
- [`local`](#local)

{{< note >}}
اگر تصمیم دارید از `WaitForFirstConsumer` استفاده کنید، برای مشخص کردن وابستگی نود از `nodeName` در مشخصات Pod استفاده نکنید.
اگر در این حالت از `nodeName` استفاده شود، زمان‌بند دور زده می‌شود و PVC در وضعیت `pending` باقی می‌ماند.

به‌جای آن می‌توانید از انتخابگر نود برای `kubernetes.io/hostname` استفاده کنید:
{{< /note >}}

{{% code_sample language="yaml" file="storage/storageclass/pod-volume-binding.yaml" %}}

## توپولوژی‌های مجاز

هنگامی که اپراتور کلاستر حالت اتصال حجم `WaitForFirstConsumer` را مشخص می‌کند، در بیشتر موقعیت‌ها دیگر لازم نیست تأمین را به توپولوژی‌های خاصی محدود کرد. با این حال، اگر همچنان لازم باشد، می‌توان `allowedTopologies` را مشخص کرد.

این مثال نشان می‌دهد که چگونه می‌توان توپولوژی حجم‌های تأمین‌شده را به zoneهای خاصی محدود کرد. این روش باید در افزونه‌های پشتیبانی‌شده جایگزین پارامترهای `zone` و `zones` شود.

{{% code_sample language="yaml" file="storage/storageclass/storageclass-topology.yaml" %}}

## پارامترها

هر StorageClass پارامترهایی دارد که حجم‌های متعلق به آن کلاس ذخیره‌سازی را توصیف می‌کنند. بسته به `provisioner`، ممکن است پارامترهای متفاوتی پذیرفته شوند. هنگامی که پارامتری حذف شود، از یک مقدار پیش‌فرض استفاده می‌شود.

برای هر StorageClass حداکثر ۵۱۲ پارامتر می‌توان تعریف کرد.
طول کل آبجکت parameters، شامل کلیدها و مقادیر آن، نمی‌تواند از 256 KiB بیشتر باشد.

### AWS EBS

<!-- maintenance note: OK to remove all mention of awsElasticBlockStore once the v1.27 release of
Kubernetes has gone out of support -->

کوبرنتیز {{< skew currentVersion >}} نوع حجم `awsElasticBlockStore` را شامل نمی‌شود.

درایور ذخیره‌سازی درون‌درختی (in-tree) با نام AWSElasticBlockStore در نسخه‌ی v1.19 کوبرنتیز منسوخ شد و سپس در نسخه‌ی v1.27 به‌طور کامل حذف شد.

پروژه‌ی کوبرنتیز پیشنهاد می‌کند به‌جای آن از درایور ذخیره‌سازی برون‌درختی (out-of-tree) [AWS EBS](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) استفاده کنید.

در ادامه نمونه‌ای از یک StorageClass برای درایور CSI مربوط به AWS EBS آمده است:

{{% code_sample language="yaml" file="storage/storageclass/storageclass-aws-ebs.yaml" %}}

پارامتر `tagSpecification`: برچسب‌های (tags) دارای این پیشوند روی حجم‌های EBS که به‌صورت پویا تأمین می‌شوند اعمال می‌شوند.

### AWS EFS

برای پیکربندی ذخیره‌سازی AWS EFS، می‌توانید از درایور برون‌درختی [AWS_EFS_CSI_DRIVER](https://github.com/kubernetes-sigs/aws-efs-csi-driver) استفاده کنید.

{{% code_sample language="yaml" file="storage/storageclass/storageclass-aws-efs.yaml" %}}

- `provisioningMode`: نوع حجمی که Amazon EFS باید تأمین کند. در حال حاضر فقط تأمین مبتنی بر access point (`efs-ap`) پشتیبانی می‌شود.
- `fileSystemId`: سیستم فایلی که access point زیر آن ایجاد می‌شود.
- `directoryPerms`: مجوزهای دایرکتوری ریشه‌ای که access point ایجاد می‌کند.

برای جزئیات بیشتر، به مستندات [AWS_EFS_CSI_Driver Dynamic Provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/efs/dynamic_provisioning/README.md) مراجعه کنید.


### NFS

برای پیکربندی ذخیره‌سازی NFS می‌توانید از درایور درون‌درختی یا
[درایور CSI مربوط به NFS برای کوبرنتیز](https://github.com/kubernetes-csi/csi-driver-nfs#readme)
(توصیه‌شده) استفاده کنید.

{{% code_sample language="yaml" file="storage/storageclass/storageclass-nfs.yaml" %}}

- `server`: نام میزبان یا نشانی IP سرور NFS.
- `path`: مسیری که سرور NFS آن را export می‌کند.
- `readOnly`: پرچمی که نشان می‌دهد آیا ذخیره‌سازی به‌صورت فقط‌خواندنی mount می‌شود یا نه (پیش‌فرض false).

کوبرنتیز تأمین‌کننده‌ی داخلی برای NFS ندارد.
برای ایجاد یک StorageClass برای NFS باید از یک تأمین‌کننده‌ی خارجی استفاده کنید.
در ادامه چند نمونه آمده است:

- [سرور NFS Ganesha و تأمین‌کننده‌ی خارجی](https://github.com/kubernetes-sigs/nfs-ganesha-server-and-external-provisioner)
- [تأمین‌کننده‌ی خارجی NFS subdir](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner)

### vSphere

برای کلاس‌های ذخیره‌سازی vSphere دو نوع تأمین‌کننده وجود دارد:

- [تأمین‌کننده‌ی CSI](#vsphere-provisioner-csi): `csi.vsphere.vmware.com`
- [تأمین‌کننده‌ی vCP](#vcp-provisioner): `kubernetes.io/vsphere-volume`

تأمین‌کننده‌های درون‌درختی [منسوخ شده‌اند](/blog/2019/12/09/kubernetes-1-17-feature-csi-migration-beta/#why-are-we-migrating-in-tree-plugins-to-csi).
برای اطلاعات بیشتر درباره‌ی تأمین‌کننده‌ی CSI،
[درایور CSI مربوط به vSphere برای کوبرنتیز](https://vsphere-csi-driver.sigs.k8s.io/) و
[مهاجرت CSI برای vSphereVolume](/docs/concepts/storage/volumes/#vsphere-csi-migration) را ببینید.

#### تأمین‌کننده‌ی CSI {#vsphere-provisioner-csi}

تأمین‌کننده‌ی StorageClass مربوط به vSphere CSI با کلاسترهای Tanzu Kubernetes کار می‌کند.
برای دیدن یک نمونه، به [مخزن vSphere CSI](https://github.com/kubernetes-sigs/vsphere-csi-driver/blob/master/example/vanilla-k8s-RWM-filesystem-volumes/example-sc.yaml) مراجعه کنید.

#### تأمین‌کننده‌ی vCP

مثال‌های زیر از تأمین‌کننده‌ی StorageClass مربوط به VMware Cloud Provider (vCP) استفاده می‌کنند.

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

   مقادیر مجاز `diskformat`: `thin`، `zeroedthick` و `eagerzeroedthick`. پیش‌فرض: `"thin"`.

2. یک StorageClass با قالب دیسک روی یک datastore که کاربر مشخص می‌کند ایجاد کنید.

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

   پارامتر `datastore`: کاربر می‌تواند datastore را نیز در StorageClass مشخص کند.
   حجم روی datastore مشخص‌شده در StorageClass ایجاد می‌شود که در این مثال `VSANDatastore` است. این فیلد اختیاری است. اگر datastore مشخص نشود، حجم روی datastoreای ایجاد می‌شود که در فایل پیکربندی vSphere مورد استفاده برای راه‌اندازی vSphere Cloud Provider مشخص شده است.

3. مدیریت سیاست ذخیره‌سازی در کوبرنتیز

   - استفاده از سیاست SPBM موجود در vCenter

     یکی از مهم‌ترین قابلیت‌های vSphere برای مدیریت ذخیره‌سازی، مدیریت مبتنی بر سیاست است. مدیریت ذخیره‌سازی مبتنی بر سیاست (SPBM) چارچوبی برای سیاست‌های ذخیره‌سازی است که یک صفحه‌ی کنترل واحد و یکپارچه را در گستره‌ی وسیعی از سرویس‌های داده و راهکارهای ذخیره‌سازی فراهم می‌کند. با SPBM، مدیران vSphere می‌توانند بر چالش‌های اولیه‌ی تأمین ذخیره‌سازی، مانند برنامه‌ریزی ظرفیت، سطوح خدمات متمایز و مدیریت ظرفیت اضافی، غلبه کنند.

     سیاست‌های SPBM را می‌توان با پارامتر `storagePolicyName` در StorageClass مشخص کرد.

   - پشتیبانی از سیاست Virtual SAN در کوبرنتیز

     مدیران زیرساخت vSphere (VI) می‌توانند هنگام تأمین پویای حجم، قابلیت‌های ذخیره‌سازی سفارشی Virtual SAN را مشخص کنند. اکنون می‌توانید الزامات ذخیره‌سازی، مانند کارایی و دسترس‌پذیری، را در قالب قابلیت‌های ذخیره‌سازی هنگام تأمین پویای حجم تعریف کنید. این الزامات به یک سیاست Virtual SAN تبدیل می‌شوند و سپس هنگام ایجاد یک حجم پایدار (دیسک مجازی) به لایه‌ی Virtual SAN فرستاده می‌شوند. دیسک مجازی برای برآورده کردن این الزامات در سراسر datastore مربوط به Virtual SAN توزیع می‌شود.

     برای جزئیات بیشتر درباره‌ی نحوه‌ی استفاده از سیاست‌های ذخیره‌سازی برای مدیریت حجم‌های پایدار، می‌توانید [مدیریت ذخیره‌سازی مبتنی بر سیاست برای تأمین پویای حجم‌ها](https://github.com/vmware-archive/vsphere-storage-for-kubernetes/blob/fa4c8b8ad46a85b6555d715dd9d27ff69839df53/documentation/policy-based-mgmt.md) را ببینید.

### Ceph RBD (منسوخ‌شده) {#ceph-rbd}

{{< note >}}
{{< feature-state state="deprecated" for_k8s_version="v1.28" >}}
این تأمین‌کننده‌ی داخلی Ceph RBD منسوخ شده است. لطفاً از
[درایور CSI مربوط به CephFS RBD](https://github.com/ceph/ceph-csi) استفاده کنید.
{{< /note >}}

{{% code_sample language="yaml" file="storage/storageclass/storageclass-ceph-rbd.yaml" %}}

- `monitors`: مانیتورهای Ceph که با ویرگول از هم جدا می‌شوند. این پارامتر الزامی است.
- `adminId`: شناسه‌ی کلاینت Ceph که می‌تواند در pool ایمیج ایجاد کند.
  پیش‌فرض "admin" است.
- `adminSecretName`: نام Secret برای `adminId`. این پارامتر الزامی است.
  نوع Secret ارائه‌شده باید "kubernetes.io/rbd" باشد.
- `adminSecretNamespace`: فضای نام مربوط به `adminSecretName`. پیش‌فرض "default" است.
- `pool`: pool مربوط به Ceph RBD. پیش‌فرض "rbd" است.
- `userId`: شناسه‌ی کلاینت Ceph که برای نگاشت ایمیج RBD استفاده می‌شود. پیش‌فرض آن همان `adminId` است.
- `userSecretName`: نام Secret مربوط به Ceph برای `userId` جهت نگاشت ایمیج RBD. این Secret باید در همان فضای نامی باشد که PVCها در آن قرار دارند. این پارامتر الزامی است.
  نوع Secret ارائه‌شده باید "kubernetes.io/rbd" باشد؛ برای مثال، می‌توان آن را به این روش ایجاد کرد:

  ```shell
  kubectl create secret generic ceph-secret --type="kubernetes.io/rbd" \
    --from-literal=key='QVFEQ1pMdFhPUnQrSmhBQUFYaERWNHJsZ3BsMmNjcDR6RFZST0E9PQ==' \
    --namespace=kube-system
  ```

- `userSecretNamespace`: فضای نام مربوط به `userSecretName`.
- `fsType`: نوع سیستم فایلی که کوبرنتیز از آن پشتیبانی می‌کند. پیش‌فرض: `"ext4"`.
- `imageFormat`: قالب ایمیج Ceph RBD، "1" یا "2". پیش‌فرض "2" است.
- `imageFeatures`: این پارامتر اختیاری است و فقط در صورتی باید استفاده شود که `imageFormat` را برابر "2" قرار داده باشید. در حال حاضر تنها قابلیت پشتیبانی‌شده `layering` است.
  پیش‌فرض "" است و هیچ قابلیتی فعال نمی‌شود.

### Azure Disk

<!-- maintenance note: OK to remove all mention of azureDisk once the v1.27 release of
Kubernetes has gone out of support -->

کوبرنتیز {{< skew currentVersion >}} نوع حجم `azureDisk` را شامل نمی‌شود.

درایور ذخیره‌سازی درون‌درختی `azureDisk` در نسخه‌ی v1.19 کوبرنتیز منسوخ شد و سپس در نسخه‌ی v1.27 به‌طور کامل حذف شد.

پروژه‌ی کوبرنتیز پیشنهاد می‌کند به‌جای آن از درایور ذخیره‌سازی شخص ثالث [Azure Disk](https://github.com/kubernetes-sigs/azuredisk-csi-driver) استفاده کنید.

### Azure File (منسوخ‌شده) {#azure-file}

{{% code_sample language="yaml" file="storage/storageclass/storageclass-azure-file.yaml" %}}

- `skuName`: سطح SKU حساب ذخیره‌سازی Azure. مقدار پیش‌فرض آن خالی است.
- `location`: مکان حساب ذخیره‌سازی Azure. مقدار پیش‌فرض آن خالی است.
- `storageAccount`: نام حساب ذخیره‌سازی Azure. مقدار پیش‌فرض آن خالی است. اگر
  حساب ذخیره‌سازی مشخص نشود، همهٔ حساب‌های ذخیره‌سازی مرتبط با گروه منابع جست‌وجو
  می‌شوند تا حسابی پیدا شود که با `skuName` و `location` مطابقت داشته باشد. اگر
  حساب ذخیره‌سازی مشخص شود، باید در همان گروه منابعِ کلاستر قرار داشته باشد و در این
  حالت `skuName` و `location` نادیده گرفته می‌شوند.
- `secretNamespace`: فضای نام (namespace) Secret‌ای که نام و کلید حساب ذخیره‌سازی
  Azure را در خود دارد. مقدار پیش‌فرض آن همان فضای نام Pod است.
- `secretName`: نام Secret‌ای که نام و کلید حساب ذخیره‌سازی Azure را در خود دارد.
  مقدار پیش‌فرض آن `azure-storage-account-<accountName>-secret` است.
- `readOnly`: پرچمی که مشخص می‌کند آیا ذخیره‌سازی به‌صورت فقط‌خواندنی مونت شود یا نه.
  مقدار پیش‌فرض آن false است، یعنی مونت به‌صورت خواندنی/نوشتنی انجام می‌شود. این
  تنظیم بر تنظیم `ReadOnly` در VolumeMounts نیز اثر می‌گذارد.

در هنگام تأمین ذخیره‌سازی، یک Secret با نامی که در `secretName` تعیین شده است برای
اطلاعات احراز هویت مونت ایجاد می‌شود. اگر در کلاستر هم
[RBAC](/docs/reference/access-authn-authz/rbac/) و هم
[نقش‌های کنترل‌کننده](/docs/reference/access-authn-authz/rbac/#controller-roles)
فعال باشند، مجوز `create` را برای منبع `secret` به clusterrole
`system:controller:persistent-volume-binder` اضافه کنید.

در محیط‌های چندمستأجری (multi-tenancy)، اکیداً توصیه می‌شود مقدار `secretNamespace`
را به‌صراحت تنظیم کنید؛ در غیر این صورت ممکن است کاربران دیگر بتوانند اطلاعات
احراز هویت حساب ذخیره‌سازی را بخوانند.

### حجم Portworx (منسوخ‌شده) {#portworx-volume}

{{% code_sample language="yaml" file="storage/storageclass/storageclass-portworx-volume.yaml" %}}

- `fs`: فایل‌سیستمی که باید ایجاد شود: `none/xfs/ext4` (پیش‌فرض: `ext4`).
- `block_size`: اندازهٔ بلاک بر حسب کیلوبایت (پیش‌فرض: `32`).
- `repl`: تعداد رونوشت‌های همگامی که باید در قالب ضریب تکثیر `1..3` فراهم شوند
  (پیش‌فرض: `1`). در اینجا یک رشته انتظار می‌رود، یعنی `"1"` و نه `1`.
- `priority_io`: تعیین می‌کند که حجم از ذخیره‌سازی با کارایی بالاتر ایجاد شود یا از
  ذخیره‌سازی با اولویت پایین‌تر: `high/medium/low` (پیش‌فرض: `low`).
- `snap_interval`: بازهٔ زمانی بر حسب دقیقه برای تعیین زمان گرفتن اسنپ‌شات‌ها.
  اسنپ‌شات‌ها به‌صورت افزایشی و بر اساس تفاوت با اسنپ‌شات قبلی گرفته می‌شوند و مقدار
  0 گرفتن اسنپ‌شات را غیرفعال می‌کند (پیش‌فرض: `0`). در اینجا یک رشته انتظار می‌رود،
  یعنی `"70"` و نه `70`.
- `aggregation_level`: تعداد قطعه‌هایی را مشخص می‌کند که حجم میان آن‌ها توزیع می‌شود؛
  مقدار 0 نشان‌دهندهٔ حجم غیرتجمیعی است (پیش‌فرض: `0`). در اینجا یک رشته انتظار
  می‌رود، یعنی `"0"` و نه `0`.
- `ephemeral`: مشخص می‌کند که حجم پس از آن‌مونت شدن پاک‌سازی شود یا ماندگار بماند.
  در کاربرد `emptyDir` می‌توان این مقدار را true قرار داد و در کاربرد
  `persistent volumes`، مانند پایگاه‌داده‌هایی چون Cassandra، باید آن را false
  قرار داد: `true/false` (پیش‌فرض: `false`). در اینجا یک رشته انتظار می‌رود، یعنی
  `"true"` و نه `true`.

### محلی (Local)

{{% code_sample language="yaml" file="storage/storageclass/storageclass-local.yaml" %}}

حجم‌های محلی در کوبرنتیز {{< skew currentVersion >}} از تأمین پویا پشتیبانی
نمی‌کنند؛ با این حال، همچنان باید یک StorageClass ایجاد کنید تا اتصال حجم تا زمانی
که Pod واقعاً روی نود مناسب زمان‌بندی شود به تأخیر بیفتد. این رفتار با حالت اتصال
حجم `WaitForFirstConsumer` تعیین می‌شود.

با به تأخیر انداختن اتصال حجم، زمان‌بند می‌تواند هنگام انتخاب PersistentVolume
مناسب برای یک PersistentVolumeClaim همهٔ محدودیت‌های زمان‌بندی Pod را در نظر بگیرد.
