---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "PersistentVolume"
content_type: "api_reference"
description: "PersistentVolume (PV) یک منبع ذخیره‌سازی است که توسط مدیر کلاستر فراهم می‌شود. این منبع مشابه یک نود است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes"
title: "PersistentVolume"
weight: 80
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## PersistentVolume {#PersistentVolume}

PersistentVolume (PV) یک منبع ذخیره‌سازی است که مدیر کلاستر آن را فراهم می‌کند. این منبع مشابه یک نود است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointی که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. این فیلد قابل به‌روزرسانی نیست و به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#PersistentVolumeSpec" >}}">PersistentVolumeSpec</a></em></td>
      <td>spec مشخصات یک persistent volume را تعریف می‌کند که متعلق به کلاستر است و مدیر کلاستر آن را فراهم کرده است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#PersistentVolumeStatus" >}}">PersistentVolumeStatus</a></em></td>
      <td>status اطلاعات و وضعیت فعلی persistent volume را نشان می‌دهد. این فیلد توسط سیستم مقداردهی می‌شود و فقط خواندنی است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistent-volumes</td>
    </tr>
  </tbody>
</table>


## PersistentVolumeSpec {#PersistentVolumeSpec}

PersistentVolumeSpec مشخصات یک persistent volume است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>accessModes</code><br/><em>string array</em></td>
      <td>accessModes شامل تمام روش‌هایی است که حجم (volume) را می‌توان با آن‌ها mount کرد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes</td>
    </tr>
    <tr>
      <td><code>awsElasticBlockStore</code><br/><em><a href="{{< ref "#AWSElasticBlockStoreVolumeSource" >}}">AWSElasticBlockStoreVolumeSource</a></em></td>
      <td>awsElasticBlockStore یک منبع AWS Disk را نشان می‌دهد که به ماشین میزبان kubelet متصل می‌شود و سپس در اختیار Pod قرار می‌گیرد. منسوخ‌شده: AWSElasticBlockStore منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام awsElasticBlockStore به درایور CSI با نام ebs.csi.aws.com هدایت می‌شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</td>
    </tr>
    <tr>
      <td><code>azureDisk</code><br/><em><a href="{{< ref "#AzureDiskVolumeSource" >}}">AzureDiskVolumeSource</a></em></td>
      <td>azureDisk یک Azure Data Disk را نشان می‌دهد که روی میزبان mount می‌شود و به‌صورت bind mount در اختیار Pod قرار می‌گیرد. منسوخ‌شده: AzureDisk منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام azureDisk به درایور CSI با نام disk.csi.azure.com هدایت می‌شوند.</td>
    </tr>
    <tr>
      <td><code>azureFile</code><br/><em><a href="{{< ref "#AzureFilePersistentVolumeSource" >}}">AzureFilePersistentVolumeSource</a></em></td>
      <td>azureFile یک Azure File Service را نشان می‌دهد که روی میزبان mount می‌شود و به‌صورت bind mount در اختیار Pod قرار می‌گیرد. منسوخ‌شده: AzureFile منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام azureFile به درایور CSI با نام file.csi.azure.com هدایت می‌شوند.</td>
    </tr>
    <tr>
      <td><code>capacity</code><br/><em>object</em></td>
      <td>capacity توصیف‌کننده منابع و ظرفیت persistent volume است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity</td>
    </tr>
    <tr>
      <td><code>cephfs</code><br/><em><a href="{{< ref "#CephFSPersistentVolumeSource" >}}">CephFSPersistentVolumeSource</a></em></td>
      <td>cephFS یک Ceph FS mount روی میزبان را نشان می‌دهد که هم‌عمر با Pod است. منسوخ‌شده: CephFS منسوخ شده است و نوع in-tree با نام cephfs دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>cinder</code><br/><em><a href="{{< ref "#CinderPersistentVolumeSource" >}}">CinderPersistentVolumeSource</a></em></td>
      <td>cinder یک حجم cinder را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن mount شده است. منسوخ‌شده: Cinder منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام cinder به درایور CSI با نام cinder.csi.openstack.org هدایت می‌شوند. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
    <tr>
      <td><code>claimRef</code><br/><em><a href="{{< ref "../definitions/object-reference-v1#ObjectReference" >}}">ObjectReference</a></em></td>
      <td>claimRef بخشی از اتصال دوطرفه میان PersistentVolume و PersistentVolumeClaim است. انتظار می‌رود در حالت bound بودن، مقدار آن nil نباشد. claim.VolumeName اتصال مرجع و معتبر میان PV و PVC است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding</td>
    </tr>
    <tr>
      <td><code>csi</code><br/><em><a href="{{< ref "#CSIPersistentVolumeSource" >}}">CSIPersistentVolumeSource</a></em></td>
      <td>csi ذخیره‌سازی‌ای را نشان می‌دهد که یک درایور CSI خارجی آن را مدیریت می‌کند.</td>
    </tr>
    <tr>
      <td><code>fc</code><br/><em><a href="{{< ref "#FCVolumeSource" >}}">FCVolumeSource</a></em></td>
      <td>fc یک منبع Fibre Channel را نشان می‌دهد که به ماشین میزبان kubelet متصل می‌شود و سپس در اختیار Pod قرار می‌گیرد.</td>
    </tr>
    <tr>
      <td><code>flexVolume</code><br/><em><a href="{{< ref "#FlexPersistentVolumeSource" >}}">FlexPersistentVolumeSource</a></em></td>
      <td>flexVolume یک منبع حجم عمومی را نشان می‌دهد که با استفاده از یک افزونه مبتنی بر exec فراهم یا متصل می‌شود. منسوخ‌شده: FlexVolume منسوخ شده است. به‌جای آن از CSIDriver استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>flocker</code><br/><em><a href="{{< ref "#FlockerVolumeSource" >}}">FlockerVolumeSource</a></em></td>
      <td>flocker یک حجم Flocker را نشان می‌دهد که به ماشین میزبان kubelet متصل می‌شود و برای استفاده در اختیار Pod قرار می‌گیرد. این گزینه به در حال اجرا بودن سرویس کنترل Flocker وابسته است. منسوخ‌شده: Flocker منسوخ شده است و نوع in-tree با نام flocker دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>gcePersistentDisk</code><br/><em><a href="{{< ref "#GCEPersistentDiskVolumeSource" >}}">GCEPersistentDiskVolumeSource</a></em></td>
      <td>gcePersistentDisk یک منبع GCE Disk را نشان می‌دهد که به ماشین میزبان kubelet متصل می‌شود و سپس در اختیار Pod قرار می‌گیرد. مدیر کلاستر آن را فراهم می‌کند. منسوخ‌شده: GCEPersistentDisk منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام gcePersistentDisk به درایور CSI با نام pd.csi.storage.gke.io هدایت می‌شوند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</td>
    </tr>
    <tr>
      <td><code>glusterfs</code><br/><em><a href="{{< ref "#GlusterfsPersistentVolumeSource" >}}">GlusterfsPersistentVolumeSource</a></em></td>
      <td>glusterfs یک حجم Glusterfs را نشان می‌دهد که به میزبان متصل می‌شود و در اختیار Pod قرار می‌گیرد. مدیر کلاستر آن را فراهم می‌کند. منسوخ‌شده: Glusterfs منسوخ شده است و نوع in-tree با نام glusterfs دیگر پشتیبانی نمی‌شود. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md</td>
    </tr>
    <tr>
      <td><code>hostPath</code><br/><em><a href="{{< ref "#HostPathVolumeSource" >}}">HostPathVolumeSource</a></em></td>
      <td>hostPath یک دایرکتوری روی میزبان را نشان می‌دهد که توسعه‌دهنده یا آزمونگر آن را فراهم می‌کند. این گزینه فقط برای توسعه و آزمون روی یک نود مفید است! ذخیره‌سازی روی میزبان به هیچ شکلی پشتیبانی نمی‌شود و در یک کلاستر چندنودی کار نخواهد کرد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#hostpath</td>
    </tr>
    <tr>
      <td><code>iscsi</code><br/><em><a href="{{< ref "#ISCSIPersistentVolumeSource" >}}">ISCSIPersistentVolumeSource</a></em></td>
      <td>iscsi یک منبع ISCSI Disk را نشان می‌دهد که به ماشین میزبان kubelet متصل می‌شود و سپس در اختیار Pod قرار می‌گیرد. مدیر کلاستر آن را فراهم می‌کند.</td>
    </tr>
    <tr>
      <td><code>local</code><br/><em><a href="{{< ref "#LocalVolumeSource" >}}">LocalVolumeSource</a></em></td>
      <td>local ذخیره‌سازی متصل مستقیم را همراه با node affinity نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>mountOptions</code><br/><em>string array</em></td>
      <td>mountOptions فهرست گزینه‌های mount است؛ برای مثال ["ro", "soft"]. این گزینه‌ها اعتبارسنجی نمی‌شوند و در صورت نامعتبر بودن یکی از آن‌ها، mount به‌سادگی با شکست مواجه می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options</td>
    </tr>
    <tr>
      <td><code>nfs</code><br/><em><a href="{{< ref "#NFSVolumeSource" >}}">NFSVolumeSource</a></em></td>
      <td>nfs یک NFS mount روی میزبان را نشان می‌دهد. مدیر کلاستر آن را فراهم می‌کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#nfs</td>
    </tr>
    <tr>
      <td><code>nodeAffinity</code><br/><em><a href="{{< ref "#VolumeNodeAffinity" >}}">VolumeNodeAffinity</a></em></td>
      <td>nodeAffinity محدودیت‌هایی را تعریف می‌کند که مشخص می‌کنند این حجم از کدام نودها قابل دسترسی است. این فیلد بر زمان‌بندی Podهایی که از این حجم استفاده می‌کنند تأثیر می‌گذارد. اگر feature gate با نام MutablePVNodeAffinity فعال باشد، این فیلد قابل تغییر است.</td>
    </tr>
    <tr>
      <td><code>persistentVolumeReclaimPolicy</code><br/><em>string</em></td>
      <td>persistentVolumeReclaimPolicy مشخص می‌کند وقتی persistent volume از claim خود آزاد می‌شود چه اتفاقی برای آن می‌افتد. گزینه‌های معتبر عبارت‌اند از Retain (پیش‌فرض برای PersistentVolumeهای ایجادشده به‌صورت دستی)، Delete (پیش‌فرض برای PersistentVolumeهای فراهم‌شده به‌صورت پویا) و Recycle (منسوخ‌شده). افزونه حجمی که زیربنای این PersistentVolume است باید از Recycle پشتیبانی کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming<br/><br/>مقادیر ممکن enum:<br/> - `"Delete"` یعنی حجم هنگام آزاد شدن از claim خود از کوبرنتیز حذف می‌شود. افزونه حجم باید از حذف پشتیبانی کند.<br/> - `"Recycle"` یعنی حجم هنگام آزاد شدن از claim خود دوباره به مخزن persistent volumeهای متصل‌نشده بازگردانده می‌شود. افزونه حجم باید از بازیافت پشتیبانی کند.<br/> - `"Retain"` یعنی حجم برای بازیابی دستی توسط مدیر کلاستر در وضعیت (phase) فعلی خود، یعنی Released، باقی می‌ماند. سیاست پیش‌فرض Retain است.</td>
    </tr>
    <tr>
      <td><code>photonPersistentDisk</code><br/><em><a href="{{< ref "#PhotonPersistentDiskVolumeSource" >}}">PhotonPersistentDiskVolumeSource</a></em></td>
      <td>photonPersistentDisk یک دیسک پایدار PhotonController را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن mount شده است. منسوخ‌شده: PhotonPersistentDisk منسوخ شده است و نوع in-tree با نام photonPersistentDisk دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>portworxVolume</code><br/><em><a href="{{< ref "#PortworxVolumeSource" >}}">PortworxVolumeSource</a></em></td>
      <td>portworxVolume یک حجم portworx را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن mount شده است. منسوخ‌شده: PortworxVolume منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام portworxVolume به درایور CSI با نام pxd.portworx.com هدایت می‌شوند.</td>
    </tr>
    <tr>
      <td><code>quobyte</code><br/><em><a href="{{< ref "#QuobyteVolumeSource" >}}">QuobyteVolumeSource</a></em></td>
      <td>quobyte یک Quobyte mount روی میزبان را نشان می‌دهد که هم‌عمر با Pod است. منسوخ‌شده: Quobyte منسوخ شده است و نوع in-tree با نام quobyte دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>rbd</code><br/><em><a href="{{< ref "#RBDPersistentVolumeSource" >}}">RBDPersistentVolumeSource</a></em></td>
      <td>rbd یک Rados Block Device mount روی میزبان را نشان می‌دهد که هم‌عمر با Pod است. منسوخ‌شده: RBD منسوخ شده است و نوع in-tree با نام rbd دیگر پشتیبانی نمی‌شود. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md</td>
    </tr>
    <tr>
      <td><code>scaleIO</code><br/><em><a href="{{< ref "#ScaleIOPersistentVolumeSource" >}}">ScaleIOPersistentVolumeSource</a></em></td>
      <td>scaleIO یک persistent volume از نوع ScaleIO را نشان می‌دهد که به نودهای کوبرنتیز متصل و روی آن‌ها mount شده است. منسوخ‌شده: ScaleIO منسوخ شده است و نوع in-tree با نام scaleIO دیگر پشتیبانی نمی‌شود.</td>
    </tr>
    <tr>
      <td><code>storageClassName</code><br/><em>string</em></td>
      <td>storageClassName نام StorageClassی است که این persistent volume به آن تعلق دارد. مقدار خالی به این معناست که این حجم به هیچ StorageClassی تعلق ندارد.</td>
    </tr>
    <tr>
      <td><code>storageos</code><br/><em><a href="{{< ref "#StorageOSPersistentVolumeSource" >}}">StorageOSPersistentVolumeSource</a></em></td>
      <td>storageOS یک حجم StorageOS را نشان می‌دهد که به ماشین میزبان kubelet متصل می‌شود و روی Pod mount می‌شود. منسوخ‌شده: StorageOS منسوخ شده است و نوع in-tree با نام storageos دیگر پشتیبانی نمی‌شود. اطلاعات بیشتر: https://examples.k8s.io/volumes/storageos/README.md</td>
    </tr>
    <tr>
      <td><code>volumeAttributesClassName</code><br/><em>string</em></td>
      <td>نام VolumeAttributesClassی که این persistent volume به آن تعلق دارد. مقدار خالی مجاز نیست. اگر این فیلد تنظیم نشده باشد، یعنی این حجم به هیچ VolumeAttributesClassی تعلق ندارد. این فیلد قابل تغییر است و پس از آنکه حجم با موفقیت به یک کلاس جدید به‌روزرسانی شد، درایور CSI می‌تواند آن را تغییر دهد. برای یک PersistentVolume متصل‌نشده، volumeAttributesClassName در فرایند اتصال با PersistentVolumeClaimهای متصل‌نشده مطابقت داده می‌شود.</td>
    </tr>
    <tr>
      <td><code>volumeMode</code><br/><em>string</em></td>
      <td>volumeMode مشخص می‌کند که حجم برای استفاده با یک فایل‌سیستم فرمت‌شده در نظر گرفته شده است یا باید در حالت raw block باقی بماند. اگر این فیلد در spec ذکر نشود، مقدار Filesystem در نظر گرفته می‌شود.<br/><br/>مقادیر ممکن enum:<br/> - `"Block"` یعنی حجم با فایل‌سیستم فرمت نمی‌شود و به‌صورت یک raw block device باقی می‌ماند.<br/> - `"Filesystem"` یعنی حجم با یک فایل‌سیستم فرمت خواهد شد یا از قبل فرمت شده است.</td>
    </tr>
    <tr>
      <td><code>vsphereVolume</code><br/><em><a href="{{< ref "#VsphereVirtualDiskVolumeSource" >}}">VsphereVirtualDiskVolumeSource</a></em></td>
      <td>vsphereVolume یک حجم vSphere را نشان می‌دهد که به ماشین میزبان kubelet متصل و روی آن mount شده است. منسوخ‌شده: VsphereVolume منسوخ شده است. تمام عملیات مربوط به نوع in-tree با نام vsphereVolume به درایور CSI با نام csi.vsphere.vmware.com هدایت می‌شوند.</td>
    </tr>
  </tbody>
</table>


## PersistentVolumeStatus {#PersistentVolumeStatus}

PersistentVolumeStatus وضعیت فعلی یک persistent volume است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastPhaseTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>lastPhaseTransitionTime زمانی است که phase از یک مقدار به مقدار دیگر تغییر کرده است و با هر تغییر phase حجم، به‌طور خودکار به زمان جاری بازنشانی می‌شود.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>message پیامی قابل‌خواندن برای انسان است که جزئیات دلیل قرار داشتن حجم در این وضعیت را بیان می‌کند.</td>
    </tr>
    <tr>
      <td><code>phase</code><br/><em>string</em></td>
      <td>phase نشان می‌دهد که حجم در دسترس است، به یک claim متصل شده است یا از یک claim آزاد شده است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase<br/><br/>مقادیر ممکن enum:<br/> - `"Available"` برای PersistentVolumeهایی استفاده می‌شود که هنوز متصل نشده‌اند. حجم‌های Available توسط binder نگهداری می‌شوند و با PersistentVolumeClaimها مطابقت داده می‌شوند.<br/> - `"Bound"` برای PersistentVolumeهایی استفاده می‌شود که متصل شده‌اند.<br/> - `"Failed"` برای PersistentVolumeهایی استفاده می‌شود که پس از آزاد شدن از یک claim، بازیافت یا حذف صحیح آن‌ها با شکست مواجه شده است.<br/> - `"Pending"` برای PersistentVolumeهایی استفاده می‌شود که در دسترس نیستند.<br/> - `"Released"` برای PersistentVolumeهایی استفاده می‌شود که PersistentVolumeClaim متصل به آن‌ها حذف شده است. حجم‌های released پیش از آنکه دوباره در دسترس قرار گیرند باید بازیافت شوند. binder مربوط به persistent volume claim از این phase استفاده می‌کند تا به فرایندی دیگر اعلام کند که منبع را بازیابی کند.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>reason یک رشته کوتاه به‌صورت CamelCase است که هر نوع شکست را توصیف می‌کند و برای تجزیه توسط ماشین و نمایش مرتب در CLI در نظر گرفته شده است.</td>
    </tr>
  </tbody>
</table>

## PersistentVolumeList {#PersistentVolumeList}

PersistentVolumeList فهرستی از آیتم‌های PersistentVolume است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این بازنمایی از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">آرایه PersistentVolume</a></em></td>
      <td>items فهرستی از حجم‌های پایدار (persistent volume) است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/persistent-volumes</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind مقداری رشته‌ای است که منبع REST را مشخص می‌کند که این آبجکت نمایانگر آن است. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌هایش را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست و به صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## AWSElasticBlockStoreVolumeSource {#AWSElasticBlockStoreVolumeSource}

یک منبع Persistent Disk در AWS را نمایش می‌دهد.

دیسک AWS EBS باید پیش از اتصال (mount) به کانتینر وجود داشته باشد. همچنین دیسک باید در همان zone از AWS باشد که kubelet در آن قرار دارد. دیسک AWS EBS را فقط می‌توان یک بار به‌صورت خواندن/نوشتن mount کرد. حجم‌های AWS EBS از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایل حجمی است که می‌خواهید mount کنید. نکته: مطمئن شوید نوع سیستم فایل را سیستم‌عامل میزبان پشتیبانی می‌کند. مثال‌ها: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</td>
    </tr>
    <tr>
      <td><code>partition</code><br/><em>integer</em></td>
      <td>partition پارتیشنی در حجم است که می‌خواهید mount کنید. اگر مشخص نشود، به‌طور پیش‌فرض mount بر اساس نام حجم انجام می‌شود. مثال‌ها: برای حجم /dev/sda1، پارتیشن را "1" تعیین می‌کنید. به همین ترتیب، پارتیشن حجم /dev/sda برابر "0" است (یا می‌توانید این ویژگی را خالی بگذارید).</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>مقدار true برای readOnly تنظیم readOnly را در VolumeMounts اعمال می‌کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</td>
    </tr>
    <tr>
      <td><code>volumeID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volumeID شناسه یکتای منبع persistent disk در AWS (حجم Amazon EBS) است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</td>
    </tr>
  </tbody>
</table>


## AzureDiskVolumeSource {#AzureDiskVolumeSource}

AzureDisk یک Azure Data Disk را نمایش می‌دهد که روی میزبان mount شده و به‌صورت bind mount به pod متصل می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>cachingMode</code><br/><em>string</em></td>
      <td>cachingMode حالت کش میزبان (Host Caching) است: None، Read Only، Read Write.<br/><br/>مقادیر enum ممکن:<br/> - `"None"`<br/> - `"ReadOnly"`<br/> - `"ReadWrite"`</td>
    </tr>
    <tr>
      <td><code>diskName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>diskName نام دیسک داده در blob storage است.</td>
    </tr>
    <tr>
      <td><code>diskURI</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>diskURI نشانی URI دیسک داده در blob storage است.</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این نوع باید از سوی سیستم‌عامل میزبان پشتیبانی شود. مثال: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>مقادیر مورد انتظار kind عبارتند از Shared: چند blob disk در هر حساب ذخیره‌سازی (storage account)؛ Dedicated: یک blob disk در هر حساب ذخیره‌سازی؛ Managed: دیسک داده مدیریت‌شده Azure (فقط در availability set مدیریت‌شده). مقدار پیش‌فرض shared است.<br/><br/>مقادیر enum ممکن:<br/> - `"Dedicated"`<br/> - `"Managed"`<br/> - `"Shared"`</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>مقدار پیش‌فرض readOnly برابر false (خواندن/نوشتن) است. مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند.</td>
    </tr>
  </tbody>
</table>


## AzureFilePersistentVolumeSource {#AzureFilePersistentVolumeSource}

AzureFile یک Azure File Service را نمایش می‌دهد که روی میزبان mount شده و به‌صورت bind mount به pod متصل می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>مقدار پیش‌فرض readOnly برابر false (خواندن/نوشتن) است. مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>secretName نام Secret ای است که حاوی نام و کلید حساب ذخیره‌سازی Azure (Azure Storage Account) است.</td>
    </tr>
    <tr>
      <td><code>secretNamespace</code><br/><em>string</em></td>
      <td>secretNamespace فضای نام Secret ای است که حاوی نام و کلید حساب ذخیره‌سازی Azure است. مقدار پیش‌فرض همان فضای نام Pod است.</td>
    </tr>
    <tr>
      <td><code>shareName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>shareName نام اشتراک (Share) در Azure است.</td>
    </tr>
  </tbody>
</table>


## CSIPersistentVolumeSource {#CSIPersistentVolumeSource}

ذخیره‌سازی‌ای را نمایش می‌دهد که توسط یک درایور حجم CSI خارجی مدیریت می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>controllerExpandSecretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>controllerExpandSecretRef ارجاعی به آبجکت Secret است که اطلاعات حساسی را در خود دارد و برای تکمیل فراخوانی CSI ControllerExpandVolume به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد می‌تواند خالی بماند. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>controllerPublishSecretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>controllerPublishSecretRef ارجاعی به آبجکت Secret است که اطلاعات حساسی را در خود دارد و برای تکمیل فراخوانی‌های CSI ControllerPublishVolume و ControllerUnpublishVolume به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد می‌تواند خالی بماند. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>driver نام درایوری است که برای این حجم استفاده می‌شود. الزامی است.</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این نوع باید از سوی سیستم‌عامل میزبان پشتیبانی شود. مثال: "ext4"، "xfs"، "ntfs".</td>
    </tr>
    <tr>
      <td><code>nodeExpandSecretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>nodeExpandSecretRef ارجاعی به آبجکت Secret است که اطلاعات حساسی را در خود دارد و برای تکمیل فراخوانی CSI NodeExpandVolume به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد می‌توان آن را حذف کرد. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>nodePublishSecretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>nodePublishSecretRef ارجاعی به آبجکت Secret است که اطلاعات حساسی را در خود دارد و برای تکمیل فراخوانی‌های CSI NodePublishVolume و NodeUnpublishVolume به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد می‌تواند خالی بماند. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>nodeStageSecretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>nodeStageSecretRef ارجاعی به آبجکت Secret است که اطلاعات حساسی را در خود دارد و برای تکمیل فراخوانی‌های CSI NodeStageVolume و NodeStageVolume و NodeUnstageVolume به درایور CSI ارسال می‌شود. این فیلد اختیاری است و اگر به Secret نیازی نباشد می‌تواند خالی بماند. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها ارسال می‌شوند.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>مقدار readOnly که به ControllerPublishVolumeRequest ارسال می‌شود. مقدار پیش‌فرض false (خواندن/نوشتن) است.</td>
    </tr>
    <tr>
      <td><code>volumeAttributes</code><br/><em>object</em></td>
      <td>volumeAttributes مربوط به حجمی که باید منتشر (publish) شود.</td>
    </tr>
    <tr>
      <td><code>volumeHandle</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volumeHandle نام یکتای حجم است که CreateVolume در افزونه حجم CSI برمی‌گرداند و در همه فراخوانی‌های بعدی برای ارجاع به حجم استفاده می‌شود. الزامی است.</td>
    </tr>
  </tbody>
</table>


## CephFSPersistentVolumeSource {#CephFSPersistentVolumeSource}

یک mount از Ceph Filesystem را نمایش می‌دهد که تا پایان عمر pod باقی می‌ماند. حجم‌های Cephfs از مدیریت مالکیت یا برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>monitors</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>monitors الزامی است: Monitors مجموعه‌ای از مانیتورهای Ceph است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>path</code><br/><em>string</em></td>
      <td>path اختیاری است: به‌جای کل درخت Ceph، به‌عنوان ریشه mount شده استفاده می‌شود. مقدار پیش‌فرض / است.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly اختیاری است: مقدار پیش‌فرض false (خواندن/نوشتن) است. مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>secretFile</code><br/><em>string</em></td>
      <td>secretFile اختیاری است: SecretFile مسیر key ring مربوط به User است. مقدار پیش‌فرض /etc/ceph/user.secret است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>secretRef اختیاری است: SecretRef ارجاعی به Secret احراز هویت مربوط به User است. مقدار پیش‌فرض خالی است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>user اختیاری است: User نام کاربر rados است. مقدار پیش‌فرض admin است. اطلاعات بیشتر: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it</td>
    </tr>
  </tbody>
</table>


## CinderPersistentVolumeSource {#CinderPersistentVolumeSource}

یک منبع حجم cinder در Openstack را نمایش می‌دهد. حجم Cinder باید پیش از mount شدن به کانتینر وجود داشته باشد. همچنین حجم باید در همان region ای باشد که kubelet در آن قرار دارد. حجم‌های Cinder از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این نوع باید از سوی سیستم‌عامل میزبان پشتیبانی شود. مثال‌ها: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly اختیاری است: مقدار پیش‌فرض false (خواندن/نوشتن) است. مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>secretRef اختیاری است: به آبجکت Secret ای اشاره می‌کند که پارامترهای لازم برای اتصال به OpenStack را در خود دارد.</td>
    </tr>
    <tr>
      <td><code>volumeID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volumeID برای شناسایی حجم در cinder استفاده می‌شود. اطلاعات بیشتر: https://examples.k8s.io/mysql-cinder-pd/README.md</td>
    </tr>
  </tbody>
</table>


## FCVolumeSource {#FCVolumeSource}

یک حجم Fibre Channel را نمایش می‌دهد. حجم‌های Fibre Channel را فقط می‌توان یک بار به‌صورت خواندن/نوشتن mount کرد. حجم‌های Fibre Channel از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این نوع باید از سوی سیستم‌عامل میزبان پشتیبانی شود. مثال: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>lun</code><br/><em>integer</em></td>
      <td>lun اختیاری است: شماره lun هدف FC.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly اختیاری است: مقدار پیش‌فرض false (خواندن/نوشتن) است. مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند.</td>
    </tr>
    <tr>
      <td><code>targetWWNs</code><br/><em>string array</em></td>
      <td>targetWWNs اختیاری است: نام‌های جهانی (WWN) هدف FC.</td>
    </tr>
    <tr>
      <td><code>wwids</code><br/><em>string array</em></td>
      <td>wwids اختیاری است: شناسه‌های جهانی (wwid) حجم FC. باید یا wwids یا ترکیب targetWWNs و lun تنظیم شود، اما نه هر دو به‌طور هم‌زمان.</td>
    </tr>
  </tbody>
</table>


## FlexPersistentVolumeSource {#FlexPersistentVolumeSource}

FlexPersistentVolumeSource یک منبع حجم پایدار عمومی را نمایش می‌دهد که با استفاده از یک افزونه مبتنی بر exec فراهم (provision) یا متصل (attach) می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>driver نام درایوری است که برای این حجم استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این نوع باید از سوی سیستم‌عامل میزبان پشتیبانی شود. مثال: "ext4"، "xfs"، "ntfs". سیستم فایل پیش‌فرض به اسکریپت FlexVolume بستگی دارد.</td>
    </tr>
    <tr>
      <td><code>options</code><br/><em>object</em></td>
      <td>options اختیاری است: این فیلد در صورت وجود، گزینه‌های فرمان اضافی را نگه می‌دارد.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly اختیاری است: مقدار پیش‌فرض false (خواندن/نوشتن) است. مقدار ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>secretRef اختیاری است: SecretRef ارجاعی به آبجکت Secret است که اطلاعات حساسی را در خود دارد و به اسکریپت‌های افزونه ارسال می‌شود. اگر هیچ آبجکت Secret ای مشخص نشده باشد، این فیلد می‌تواند خالی بماند. اگر آبجکت Secret بیش از یک secret داشته باشد، همه آن‌ها به اسکریپت‌های افزونه ارسال می‌شوند.</td>
    </tr>
  </tbody>
</table>


## FlockerVolumeSource {#FlockerVolumeSource}

یک حجم Flocker را نمایش می‌دهد که توسط عامل Flocker mount شده است. باید یک و فقط یکی از datasetName و datasetUUID تنظیم شود. حجم‌های Flocker از مدیریت مالکیت یا برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>datasetName</code><br/><em>string</em></td>
      <td>datasetName نام مجموعه‌داده (dataset) است که به‌صورت metadata -> name روی مجموعه‌داده برای Flocker ذخیره می‌شود و باید منسوخ‌شده (deprecated) در نظر گرفته شود.</td>
    </tr>
    <tr>
      <td><code>datasetUUID</code><br/><em>string</em></td>
      <td>datasetUUID شناسه UUID مجموعه‌داده است. این مقدار شناسه یکتای یک مجموعه‌داده Flocker است.</td>
    </tr>
  </tbody>
</table>

## GCEPersistentDiskVolumeSource {#GCEPersistentDiskVolumeSource}

نمایانگر یک منبع Persistent Disk در Google Compute Engine است.

یک GCE PD باید پیش از mount شدن به کانتینر وجود داشته باشد. دیسک باید در همان پروژه و zone مربوط به GCE که kubelet در آن قرار دارد، باشد. یک GCE PD را می‌توان فقط یک بار به‌صورت خواندن/نوشتن یا چندین بار به‌صورت فقط‌خواندنی mount کرد. GCE PDها از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایل حجمی است که می‌خواهید mount کنید. نکته: مطمئن شوید که نوع سیستم فایل توسط سیستم‌عامل میزبان پشتیبانی می‌شود. مثال‌ها: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</td>
    </tr>
    <tr>
      <td><code>partition</code><br/><em>integer</em></td>
      <td>partition پارتیشنی از حجم است که می‌خواهید mount کنید. اگر مشخص نشود، به‌صورت پیش‌فرض mount بر اساس نام حجم انجام می‌شود. مثال‌ها: برای حجم /dev/sda1، پارتیشن را "1" تعیین می‌کنید. به‌همین ترتیب، پارتیشن حجم /dev/sda برابر "0" است (یا می‌توانید این ویژگی را خالی بگذارید). اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</td>
    </tr>
    <tr>
      <td><code>pdName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>pdName نام یکتای منبع PD در GCE است. برای شناسایی دیسک در GCE استفاده می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند. مقدار پیش‌فرض false است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</td>
    </tr>
  </tbody>
</table>


## GlusterfsPersistentVolumeSource {#GlusterfsPersistentVolumeSource}

نمایانگر یک mount از Glusterfs است که تا پایان عمر pod باقی می‌ماند. حجم‌های Glusterfs از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>endpoints</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>endpoints نام endpoint است که توپولوژی Glusterfs را شرح می‌دهد. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod</td>
    </tr>
    <tr>
      <td><code>endpointsNamespace</code><br/><em>string</em></td>
      <td>endpointsNamespace فضای نامی است که endpoint مربوط به Glusterfs را در بر دارد. اگر این فیلد خالی باشد، EndpointNamespace به‌صورت پیش‌فرض همان فضای نام PVC متصل‌شده خواهد بود. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیر حجم Glusterfs است. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا باعث می‌شود حجم Glusterfs با دسترسی فقط‌خواندنی mount شود. مقدار پیش‌فرض false است. اطلاعات بیشتر: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod</td>
    </tr>
  </tbody>
</table>


## HostPathVolumeSource {#HostPathVolumeSource}

نمایانگر یک مسیر میزبان است که به یک pod نگاشت می‌شود. حجم‌های host path از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیر دایرکتوری روی میزبان است. اگر مسیر یک symlink باشد، لینک دنبال می‌شود تا به مسیر واقعی برسد. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#hostpath</td>
    </tr>
    <tr>
      <td><code>type</code><br/><em>string</em></td>
      <td>type نوع حجم HostPath است. مقدار پیش‌فرض "" است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#hostpath<br/><br/>مقادیر ممکن enum:<br/> - `""` برای سازگاری با نسخه‌های قبلی است؛ در صورت تنظیم نشدن، آن را خالی بگذارید<br/> - `"BlockDevice"` یک دستگاه بلوکی باید در مسیر داده‌شده وجود داشته باشد<br/> - `"CharDevice"` یک دستگاه کاراکتری باید در مسیر داده‌شده وجود داشته باشد<br/> - `"Directory"` یک دایرکتوری باید در مسیر داده‌شده وجود داشته باشد<br/> - `"DirectoryOrCreate"` اگر در مسیر داده‌شده چیزی وجود نداشته باشد، در صورت نیاز یک دایرکتوری خالی با file mode برابر 0755 و با همان گروه و مالکیت Kubelet در آنجا ایجاد می‌شود.<br/> - `"File"` یک فایل باید در مسیر داده‌شده وجود داشته باشد<br/> - `"FileOrCreate"` اگر در مسیر داده‌شده چیزی وجود نداشته باشد، در صورت نیاز یک فایل خالی با file mode برابر 0644 و با همان گروه و مالکیت Kubelet در آنجا ایجاد می‌شود.<br/> - `"Socket"` یک سوکت UNIX باید در مسیر داده‌شده وجود داشته باشد</td>
    </tr>
  </tbody>
</table>


## ISCSIPersistentVolumeSource {#ISCSIPersistentVolumeSource}

ISCSIPersistentVolumeSource نمایانگر یک دیسک ISCSI است. حجم‌های ISCSI را فقط یک بار می‌توان به‌صورت خواندن/نوشتن mount کرد. حجم‌های ISCSI از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>chapAuthDiscovery</code><br/><em>boolean</em></td>
      <td>chapAuthDiscovery مشخص می‌کند که آیا احراز هویت iSCSI Discovery CHAP پشتیبانی شود یا خیر</td>
    </tr>
    <tr>
      <td><code>chapAuthSession</code><br/><em>boolean</em></td>
      <td>chapAuthSession مشخص می‌کند که آیا احراز هویت iSCSI Session CHAP پشتیبانی شود یا خیر</td>
    </tr>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایل حجمی است که می‌خواهید mount کنید. نکته: مطمئن شوید که نوع سیستم فایل توسط سیستم‌عامل میزبان پشتیبانی می‌شود. مثال‌ها: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#iscsi</td>
    </tr>
    <tr>
      <td><code>initiatorName</code><br/><em>string</em></td>
      <td>initiatorName نام سفارشی iSCSI Initiator است. اگر initiatorName همزمان با iscsiInterface مشخص شود، یک رابط iSCSI جدید با الگوی \<target portal>:\<volume name> برای اتصال ایجاد خواهد شد.</td>
    </tr>
    <tr>
      <td><code>iqn</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>iqn همان Target iSCSI Qualified Name است.</td>
    </tr>
    <tr>
      <td><code>iscsiInterface</code><br/><em>string</em></td>
      <td>iscsiInterface نام رابطی است که از انتقال iSCSI استفاده می‌کند. مقدار پیش‌فرض 'default' (tcp) است.</td>
    </tr>
    <tr>
      <td><code>lun</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>lun شماره Lun مربوط به iSCSI Target است.</td>
    </tr>
    <tr>
      <td><code>portals</code><br/><em>string array</em></td>
      <td>portals فهرست iSCSI Target Portal است. هر Portal یا یک IP است یا، اگر پورت با مقدار پیش‌فرض (معمولاً پورت‌های TCP شماره 860 و 3260) متفاوت باشد، به شکل ip_addr:port است.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>secretRef همان Secret مربوط به CHAP برای احراز هویت iSCSI target و initiator است</td>
    </tr>
    <tr>
      <td><code>targetPortal</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>targetPortal همان iSCSI Target Portal است. Portal یا یک IP است یا، اگر پورت با مقدار پیش‌فرض (معمولاً پورت‌های TCP شماره 860 و 3260) متفاوت باشد، به شکل ip_addr:port است.</td>
    </tr>
  </tbody>
</table>


## LocalVolumeSource {#LocalVolumeSource}

Local نمایانگر ذخیره‌سازی متصل مستقیم به نود همراه با node affinity است

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این فیلد فقط زمانی اعمال می‌شود که Path یک دستگاه بلوکی باشد. باید نوع سیستم فایلی باشد که سیستم‌عامل میزبان از آن پشتیبانی می‌کند. مثال: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور پیش‌فرض یک سیستم فایل به‌صورت خودکار انتخاب می‌شود.</td>
    </tr>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیر کامل حجم روی نود است. این مسیر می‌تواند یک دایرکتوری یا یک دستگاه بلوکی (دیسک، پارتیشن و غیره) باشد.</td>
    </tr>
  </tbody>
</table>


## NFSVolumeSource {#NFSVolumeSource}

نمایانگر یک mount از NFS است که تا پایان عمر pod باقی می‌ماند. حجم‌های NFS از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>path مسیری است که سرور NFS آن را export می‌کند. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#nfs</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا باعث می‌شود export مربوط به NFS با دسترسی فقط‌خواندنی mount شود. مقدار پیش‌فرض false است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#nfs</td>
    </tr>
    <tr>
      <td><code>server</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>server نام میزبان یا نشانی IP سرور NFS است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#nfs</td>
    </tr>
  </tbody>
</table>


## PhotonPersistentDiskVolumeSource {#PhotonPersistentDiskVolumeSource}

نمایانگر یک منبع دیسک پایدار Photon Controller است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. باید نوع سیستم فایلی باشد که سیستم‌عامل میزبان از آن پشتیبانی می‌کند. مثال: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>pdID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>pdID شناسه‌ای است که دیسک پایدار Photon Controller را مشخص می‌کند</td>
    </tr>
  </tbody>
</table>


## PortworxVolumeSource {#PortworxVolumeSource}

PortworxVolumeSource نمایانگر یک منبع حجم Portworx است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fSType نوع سیستم فایلی را که باید mount شود مشخص می‌کند. باید نوع سیستم فایلی باشد که سیستم‌عامل میزبان از آن پشتیبانی می‌کند. مثال: "ext4"، "xfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly به‌طور پیش‌فرض false است (خواندن/نوشتن). ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند.</td>
    </tr>
    <tr>
      <td><code>volumeID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volumeID یک حجم Portworx را به‌طور یکتا شناسایی می‌کند</td>
    </tr>
  </tbody>
</table>


## QuobyteVolumeSource {#QuobyteVolumeSource}

نمایانگر یک mount از Quobyte است که تا پایان عمر pod باقی می‌ماند. حجم‌های Quobyte از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی نمی‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>group</code><br/><em>string</em></td>
      <td>group گروهی است که دسترسی به حجم به آن نگاشت می‌شود. به‌طور پیش‌فرض هیچ گروهی تعیین نشده است</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا باعث می‌شود حجم Quobyte با دسترسی فقط‌خواندنی mount شود. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>registry</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>registry یک یا چند سرویس Quobyte Registry را نشان می‌دهد که به‌صورت رشته و در قالب جفت host:port مشخص می‌شود (چند مورد با کاما از هم جدا می‌شوند) و به‌عنوان رجیستری مرکزی حجم‌ها عمل می‌کند</td>
    </tr>
    <tr>
      <td><code>tenant</code><br/><em>string</em></td>
      <td>tenant مالک حجم Quobyte داده‌شده در Backend است. همراه با حجم‌های Quobyte که به‌صورت پویا ایجاد می‌شوند استفاده می‌شود و مقدار آن را افزونه تعیین می‌کند</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>user کاربری است که دسترسی به حجم به آن نگاشت می‌شود. به‌طور پیش‌فرض کاربر serivceaccount است</td>
    </tr>
    <tr>
      <td><code>volume</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volume رشته‌ای است که با نام، به یک حجم Quobyte که از قبل ایجاد شده است ارجاع می‌دهد.</td>
    </tr>
  </tbody>
</table>


## RBDPersistentVolumeSource {#RBDPersistentVolumeSource}

نمایانگر یک mount از Rados Block Device است که تا پایان عمر pod باقی می‌ماند. حجم‌های RBD از مدیریت مالکیت و برچسب‌گذاری مجدد SELinux پشتیبانی می‌کنند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایل حجمی است که می‌خواهید mount کنید. نکته: مطمئن شوید که نوع سیستم فایل توسط سیستم‌عامل میزبان پشتیبانی می‌شود. مثال‌ها: "ext4"، "xfs"، "ntfs". در صورت مشخص نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/storage/volumes#rbd</td>
    </tr>
    <tr>
      <td><code>image</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>image نام ایمیج rados است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>keyring</code><br/><em>string</em></td>
      <td>keyring مسیر key ring مربوط به RBDUser است. مقدار پیش‌فرض /etc/ceph/keyring است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>monitors</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>monitors مجموعه‌ای از Ceph monitorها است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>pool</code><br/><em>string</em></td>
      <td>pool نام rados pool است. مقدار پیش‌فرض rbd است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند. مقدار پیش‌فرض false است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>secretRef نام Secret احراز هویت برای RBDUser است. در صورت تعیین، بر keyring اولویت دارد. مقدار پیش‌فرض nil است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
    <tr>
      <td><code>user</code><br/><em>string</em></td>
      <td>user نام کاربر rados است. مقدار پیش‌فرض admin است. اطلاعات بیشتر: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it</td>
    </tr>
  </tbody>
</table>


## ScaleIOPersistentVolumeSource {#ScaleIOPersistentVolumeSource}

ScaleIOPersistentVolumeSource نمایانگر یک حجم پایدار ScaleIO است

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. باید نوع سیستم فایلی باشد که سیستم‌عامل میزبان از آن پشتیبانی می‌کند. مثال: "ext4"، "xfs"، "ntfs". مقدار پیش‌فرض "xfs" است</td>
    </tr>
    <tr>
      <td><code>gateway</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>gateway نشانی میزبان ScaleIO API Gateway است.</td>
    </tr>
    <tr>
      <td><code>protectionDomain</code><br/><em>string</em></td>
      <td>protectionDomain نام ScaleIO Protection Domain برای ذخیره‌سازی پیکربندی‌شده است.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>readOnly به‌طور پیش‌فرض false است (خواندن/نوشتن). ReadOnly در اینجا تنظیم ReadOnly را در VolumeMounts اعمال می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretRef</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#SecretReference" >}}">SecretReference</a></em></td>
      <td>secretRef به Secret مربوط به کاربر ScaleIO و سایر اطلاعات حساس ارجاع می‌دهد. اگر این مقدار ارائه نشود، عملیات Login با شکست مواجه می‌شود.</td>
    </tr>
    <tr>
      <td><code>sslEnabled</code><br/><em>boolean</em></td>
      <td>sslEnabled پرچمی برای فعال یا غیرفعال کردن ارتباط SSL با Gateway است. مقدار پیش‌فرض false است</td>
    </tr>
    <tr>
      <td><code>storageMode</code><br/><em>string</em></td>
      <td>storageMode مشخص می‌کند که ذخیره‌سازی یک حجم باید ThickProvisioned باشد یا ThinProvisioned. مقدار پیش‌فرض ThinProvisioned است.</td>
    </tr>
    <tr>
      <td><code>storagePool</code><br/><em>string</em></td>
      <td>storagePool همان ScaleIO Storage Pool مرتبط با protection domain است.</td>
    </tr>
    <tr>
      <td><code>system</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>system نام سامانه ذخیره‌سازی است، به همان صورت که در ScaleIO پیکربندی شده است.</td>
    </tr>
    <tr>
      <td><code>volumeName</code><br/><em>string</em></td>
      <td>volumeName نام حجمی است که پیش‌تر در سامانه ScaleIO ایجاد شده و با این منبع حجم مرتبط است.</td>
    </tr>
  </tbody>
</table>

## SecretReference {#SecretReference}

SecretReference به یک Secret اشاره می‌کند. این آبجکت اطلاعات کافی برای بازیابی Secret در هر فضای نام (namespace) را در خود دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>name برای ارجاع به یک منبع Secret استفاده می‌شود و در هر فضای نام یکتا است.</td>
    </tr>
    <tr>
      <td><code>namespace</code><br/><em>string</em></td>
      <td>namespace فضایی را تعیین می‌کند که نام Secret باید در آن یکتا باشد.</td>
    </tr>
  </tbody>
</table>


## StorageOSPersistentVolumeSource {#StorageOSPersistentVolumeSource}

یک منبع حجم پایدار StorageOS را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این مقدار باید نوع سیستم فایلی باشد که سیستم عامل میزبان از آن پشتیبانی می‌کند؛ برای مثال "ext4"، "xfs" یا "ntfs". در صورت تعیین نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>readOnly</code><br/><em>boolean</em></td>
      <td>مقدار پیش‌فرض readOnly برابر false (خواندن/نوشتن) است. تنظیم ReadOnly در اینجا، تنظیم ReadOnly در VolumeMounts را اجباری می‌کند.</td>
    </tr>
    <tr>
      <td><code>secretRef</code><br/><em><a href="{{< ref "../definitions/object-reference-v1#ObjectReference" >}}">ObjectReference</a></em></td>
      <td>secretRef مشخص می‌کند که برای دریافت اعتبارنامه‌های API مربوط به StorageOS از کدام Secret استفاده شود. اگر تعیین نشود، مقادیر پیش‌فرض امتحان می‌شوند.</td>
    </tr>
    <tr>
      <td><code>volumeName</code><br/><em>string</em></td>
      <td>volumeName نام قابل‌خواندن برای انسان در حجم StorageOS است. نام حجم‌ها فقط در یک فضای نام یکتا است.</td>
    </tr>
    <tr>
      <td><code>volumeNamespace</code><br/><em>string</em></td>
      <td>volumeNamespace دامنه حجم را در StorageOS مشخص می‌کند. اگر فضای نامی تعیین نشود، از فضای نام Pod استفاده می‌شود. این کار باعث می‌شود محدوده‌بندی نام‌ها در کوبرنتیز برای یکپارچگی بیشتر در StorageOS نیز بازتاب داده شود. برای بازنویسی رفتار پیش‌فرض، VolumeName را روی هر نامی تنظیم کنید. اگر از فضای نام در StorageOS استفاده نمی‌کنید، مقدار آن را روی "default" قرار دهید. فضاهای نامی که از قبل در StorageOS وجود نداشته باشند ایجاد خواهند شد.</td>
    </tr>
  </tbody>
</table>


## VolumeNodeAffinity {#VolumeNodeAffinity}

VolumeNodeAffinity محدودیت‌هایی را تعریف می‌کند که تعیین می‌کنند این حجم از کدام نودها قابل دسترسی است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>required</code><br/><em><a href="{{< ref "../definitions/node-selector-v1#NodeSelector" >}}">NodeSelector</a></em></td>
      <td>required محدودیت‌های سخت‌گیرانه نود را مشخص می‌کند که باید برآورده شوند.</td>
    </tr>
  </tbody>
</table>


## VsphereVirtualDiskVolumeSource {#VsphereVirtualDiskVolumeSource}

یک منبع حجم vSphere را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fsType</code><br/><em>string</em></td>
      <td>fsType نوع سیستم فایلی است که باید mount شود. این مقدار باید نوع سیستم فایلی باشد که سیستم عامل میزبان از آن پشتیبانی می‌کند؛ برای مثال "ext4"، "xfs" یا "ntfs". در صورت تعیین نشدن، به‌طور ضمنی "ext4" در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>storagePolicyID</code><br/><em>string</em></td>
      <td>storagePolicyID شناسه پروفایل Storage Policy Based Management (SPBM) است که با StoragePolicyName مرتبط است.</td>
    </tr>
    <tr>
      <td><code>storagePolicyName</code><br/><em>string</em></td>
      <td>storagePolicyName نام پروفایل Storage Policy Based Management (SPBM) است.</td>
    </tr>
    <tr>
      <td><code>volumePath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>volumePath مسیری است که vmdk مربوط به حجم vSphere را مشخص می‌کند.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /api/v1/persistentvolumes



#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته برای دستور dryRun به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول این مقدار باید کمتر از یا برابر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از فیلدهای تکراری، فقط آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود در نظر گرفته می‌شود. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /api/v1/persistentvolumes/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته برای دستور dryRun به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول این مقدار باید کمتر از یا برابر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از فیلدهای تکراری، فقط آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود در نظر گرفته می‌شود. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. به این معنا که کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر از apply، پرچم force نباید تنظیم شده باشد.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace

#### HTTP Request

PUT /api/v1/persistentvolumes/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته برای دستور dryRun به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول این مقدار باید کمتر از یا برابر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از فیلدهای تکراری، فقط آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود در نظر گرفته می‌شود. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل تمام فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف

#### درخواست HTTP

DELETE /api/v1/persistentvolumes/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. اگر دستور dryRun نامعتبر یا ناشناخته باشد، پاسخ خطا برگردانده می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عددی صحیح و نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. مقدار صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف به‌دلیل خطای خرابی آبجکت (corrupt object) شکست بخورد، حذف ناایمن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که به یکی از این دو دلیل نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد: الف) داده‌های آن قابل تبدیل نباشد، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) رمزگشایی (decode) آن به آبجکت با شکست مواجه شود. توجه: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آن را صراحتاً فعال کند.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. تعیین می‌کند که آبجکت‌های وابسته به‌صورت یتیم (orphan) رها شوند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که garbage collection انجام شود یا خیر و به چه روشی. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم رها می‌شوند؛ 'Background' - به garbage collector اجازه داده می‌شود وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /api/v1/persistentvolumes



#### پارامترهای کوئری

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک کوئری قبلی را با پارامترهای کوئری یکسان (به‌جز مقدار خود continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از "کلید بعدی" باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. اگر دستور dryRun نامعتبر یا ناشناخته باشد، پاسخ خطا برگردانده می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض شامل همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عددی صحیح و نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. مقدار صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف به‌دلیل خطای خرابی آبجکت (corrupt object) شکست بخورد، حذف ناایمن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که به یکی از این دو دلیل نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد: الف) داده‌های آن قابل تبدیل نباشد، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) رمزگشایی (decode) آن به آبجکت با شکست مواجه شود. توجه: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آن را صراحتاً فعال کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض شامل همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان با همان کوئری اولیه از آن برای دریافت مجموعه بعدی نتایج استفاده کرد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تعداد کمتری از موارد درخواست‌شده (حتی صفر مورد) را برگرداند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند پارامتر limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این ویژگی گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. تعیین می‌کند که آبجکت‌های وابسته به‌صورت یتیم (orphan) رها شوند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که garbage collection انجام شود یا خیر و به چه روشی. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم رها می‌شوند؛ 'Background' - به garbage collector اجازه داده می‌شود وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion در فراخوانی‌های فهرست چگونه اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، تنظیم گزینه `resourceVersionMatch` نیز الزامی است. معنای درخواست watch به این شرح است:<br/> - `resourceVersionMatch` = NotOlderThan به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا یک `resourceVersion` همان‌قدر تازه‌تر از مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector (یعنی "metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های تک‌نقل‌قولی CEL با پیشوند '0x' هستند که کران پایین شامل و کران بالای غیرشامل را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال بودن feature gate با نام ShardedListAndWatch را می‌طلبد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت زمان فراخوانی را محدود می‌کند، صرف‌نظر از هر فعالیت یا عدم فعالیتی.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن

#### درخواست HTTP

GET /api/v1/persistentvolumes/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست

#### درخواست HTTP

GET /api/v1/persistentvolumes



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور، باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک پرس‌وجوی قبلی و با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را از کلید بعدی و از آخرین snapshot برمی‌گرداند که با نتایج فهرست قبلی ناسازگار است - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. به‌طور پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. به‌طور پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراوداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این حالت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، ویرایش یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه نتیجه اولین فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات، به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات، به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شود، گزینه `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به‌معنای «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» است و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions جدید است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به‌دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به‌کار نمی‌برد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون single-quote قرار می‌گیرند و پیشوند '0x' دارند؛ این دو مقدار به‌ترتیب کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash ‏64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و فعال بودن feature gate با نام ShardedListAndWatch را الزامی می‌کند.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار، فارغ از هرگونه فعالیت یا عدم فعالیت، مدت زمان فراخوانی را محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolumeList" >}}">PersistentVolumeList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### درخواست HTTP

GET /api/v1/watch/persistentvolumes/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌ای زمانی مشخص بازگردانده می‌شوند و نیز نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافتی همراه خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، اصلاح یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به وجود فیلد continue تکیه کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، اصلاح یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، گزینه `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا یک `resourceVersion` هم‌تازه با مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر منطقی OR) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") استفاده نمی‌کند. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL و داخل تک‌کوتیشن با پیشوند '0x' هستند که کران پایین شامل‌شونده و کران بالای شامل‌نشونده را در فضای hash ‏64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال بودن feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List

#### درخواست HTTP

GET /api/v1/watch/persistentvolumes



#### پارامترهای Query

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch از نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی ارسال می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک کوئری قبلی را با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده باشند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) برگرداند و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و اطمینان می‌دهد کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکتی در طول فهرست‌گیری تکه‌تکه به‌روزرسانی شود، نسخه‌ای از آبجکت که در زمان محاسبه نتیجه اول فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای متناظر با تغییراتِ (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، تنظیم گزینه `resourceVersionMatch` نیز الزامی است. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده تازه باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") استفاده نمی‌کند. مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL و داخل single quote با پیشوند '0x' هستند که کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای hash ‏64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را محدود می‌کند، صرف‌نظر از هر فعالیت یا عدم فعالیتی.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch Status

#### درخواست HTTP

PATCH /api/v1/persistentvolumes/{name}/status


#### پارامترهای Path

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### پارامترهای Query

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به یک پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند نسبت داده می‌شود. طول مقدار باید کمتر از یا برابر با ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، به‌صورتی که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است. این فیلد برای درخواست‌های apply (‏application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (‏JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. در صورت نبود خطای دیگر، درخواست همچنان موفق می‌شود و فقط آخرین مورد از هر فیلد تکراری ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest ناموفق می‌کند. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. این یعنی کاربر فیلدهای دچار تعارضی را که متعلق به دیگران است دوباره در اختیار می‌گیرد. پرچم force برای درخواست‌های patch از نوع غیر apply باید تنظیم‌نشده باشد.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای Body

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>


### `get` Read Status

#### درخواست HTTP

GET /api/v1/persistentvolumes/{name}/status


#### پارامترهای Path

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### پارامترهای Query

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace Status

#### درخواست HTTP

PUT /api/v1/persistentvolumes/{name}/status


#### پارامترهای Path

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام PersistentVolume</td>
    </tr>
  </tbody>
</table>


#### پارامترهای Query

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به یک پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند نسبت داده می‌شود. طول مقدار باید کمتر از یا برابر با ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، به‌صورتی که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. در صورت نبود خطای دیگر، درخواست همچنان موفق می‌شود و فقط آخرین مورد از هر فیلد تکراری ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest ناموفق می‌کند. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مواجه‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای Body

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "persistent-volume-v1#PersistentVolume" >}}">PersistentVolume</a></em></td>
    </tr>
  </tbody>
</table>
