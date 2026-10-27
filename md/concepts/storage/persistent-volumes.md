---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
- xing-yang
title: حجم‌های پایدار
api_metadata:
- apiVersion: "v1"
  kind: "PersistentVolume"
- apiVersion: "v1"
  kind: "PersistentVolumeClaim"
feature:
  title: هماهنگ‌سازی ذخیره‌سازی
  description: >
    سیستم ذخیره‌سازی دلخواه خود را، چه از ذخیره‌سازی محلی، چه از یک ارائه‌دهندهٔ ابر عمومی و چه از یک سیستم ذخیره‌سازی شبکه‌ای مانند iSCSI یا NFS، به‌طور خودکار mount کنید.
content_type: concept
weight: 20
---

<!-- overview -->

این سند _حجم‌های پایدار_ (persistent volumes) را در کوبرنتیز شرح می‌دهد. آشنایی با
[حجم‌ها](/docs/concepts/storage/volumes/)، [StorageClassها](/docs/concepts/storage/storage-classes/)
و [VolumeAttributesClassها](/docs/concepts/storage/volume-attributes-classes/) توصیه می‌شود.

<!-- body -->

## مقدمه

مدیریت ذخیره‌سازی مسئله‌ای متمایز از مدیریت نمونه‌های محاسباتی است.
زیرسیستم PersistentVolume یک API برای کاربران و مدیران فراهم می‌کند
که جزئیات چگونگی فراهم‌شدن ذخیره‌سازی را از چگونگی مصرف آن جدا و انتزاعی می‌کند.
برای این منظور، دو منبع API جدید معرفی می‌کنیم: PersistentVolume و PersistentVolumeClaim.

یک _PersistentVolume_ (PV) بخشی از ذخیره‌سازی در کلاستر است که
توسط مدیر تأمین (provision) شده یا با استفاده از
[Storage Classها](/docs/concepts/storage/storage-classes/) به‌صورت پویا تأمین شده است. این یک منبع در
کلاستر است، درست همان‌طور که یک نود یک منبع کلاستر است. PVها مانند Volumeها پلاگین‌های حجم هستند،
اما چرخهٔ عمری مستقل از هر Pod منفردی که از PV استفاده می‌کند دارند.
این آبجکت API جزئیات پیاده‌سازی ذخیره‌سازی را، چه NFS باشد،
چه iSCSI و چه یک سیستم ذخیره‌سازی خاص یک ارائه‌دهندهٔ ابری، در خود نگه می‌دارد.

یک _PersistentVolumeClaim_ (PVC) درخواست ذخیره‌سازی از سوی یک کاربر است. این مفهوم مشابه
یک Pod است. Podها منابع نود را مصرف می‌کنند و PVCها منابع PV را مصرف می‌کنند. Podها می‌توانند
سطوح مشخصی از منابع (CPU و حافظه) را درخواست کنند. Claimها می‌توانند اندازه و
حالت‌های دسترسی مشخصی را درخواست کنند (برای مثال، می‌توانند به‌صورت ReadWriteOnce، ReadOnlyMany،
ReadWriteMany یا ReadWriteOncePod mount شوند؛ [AccessModes](#access-modes) را ببینید).

اگرچه PersistentVolumeClaimها به کاربر امکان می‌دهند منابع ذخیره‌سازی انتزاعی را مصرف کند،
معمولاً کاربران برای مسائل مختلف به PersistentVolumeهایی با ویژگی‌های متفاوت، مانند
کارایی، نیاز دارند. مدیران کلاستر باید بتوانند
انواع گوناگونی از PersistentVolumeها را ارائه دهند که در جنبه‌هایی فراتر از اندازه و حالت‌های دسترسی
با هم تفاوت دارند، بدون آنکه کاربران را با جزئیات پیاده‌سازی آن حجم‌ها درگیر کنند.
برای این نیازها، منبع _StorageClass_ وجود دارد.

[راهنمای گام‌به‌گام مفصل همراه با مثال‌های کاربردی](/docs/tutorials/configuration/configure-persistent-volume-storage) را ببینید.

## چرخهٔ عمر یک حجم و claim

PVها منابعی در کلاستر هستند. PVCها درخواست‌هایی برای آن منابع‌اند و همچنین
به‌عنوان رسید مطالبهٔ آن منبع عمل می‌کنند. تعامل میان PVها و PVCها از این چرخهٔ عمر پیروی می‌کند:

### تأمین (Provisioning)

PVها به دو روش ممکن است تأمین شوند: به‌صورت ایستا یا به‌صورت پویا.

#### ایستا

مدیر کلاستر تعدادی PV ایجاد می‌کند. این PVها جزئیات
ذخیره‌سازی واقعی را که برای استفادهٔ کاربران کلاستر در دسترس است در خود دارند. آن‌ها در
API کوبرنتیز وجود دارند و برای مصرف در دسترس هستند.

#### پویا

هنگامی که هیچ‌یک از PVهای ایستایی که مدیر ایجاد کرده است با PersistentVolumeClaim کاربر مطابقت نداشته باشد،
کلاستر ممکن است تلاش کند یک حجم را به‌طور پویا و مخصوص آن PVC تأمین کند.
این تأمین بر پایهٔ StorageClassها انجام می‌شود: PVC باید یک
[storage class](/docs/concepts/storage/storage-classes/) درخواست کند و
مدیر باید آن کلاس را ایجاد و پیکربندی کرده باشد تا تأمین پویا
انجام شود. Claimهایی که کلاس `""` را درخواست می‌کنند، در عمل
تأمین پویا را برای خود غیرفعال می‌کنند.

برای فعال‌سازی تأمین پویای ذخیره‌سازی بر پایهٔ storage class، مدیر کلاستر
باید [کنترل‌کنندهٔ پذیرش](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass) `DefaultStorageClass`
را روی API server فعال کند. این کار را می‌توان، برای نمونه، با اطمینان از اینکه `DefaultStorageClass`
در فهرست مرتب و جداشده با کاما از مقادیر فلگ `--enable-admission-plugins`
در مؤلفهٔ API server قرار دارد انجام داد. برای اطلاعات بیشتر دربارهٔ فلگ‌های خط فرمان API server،
مستندات [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/) را بررسی کنید.

### اتصال (Binding)

کاربر یک PersistentVolumeClaim با مقدار مشخصی از ذخیره‌سازی درخواستی و
حالت‌های دسترسی معین ایجاد می‌کند، یا در مورد تأمین پویا، پیش‌تر آن را ایجاد کرده است.
یک حلقهٔ کنترلی در control plane مراقب PVCهای جدید است، یک PV منطبق
(در صورت امکان) پیدا می‌کند و آن‌ها را به هم متصل می‌کند. اگر یک PV به‌طور پویا
برای یک PVC جدید تأمین شده باشد، این حلقه همیشه آن PV را به آن PVC متصل می‌کند. در غیر این صورت،
کاربر همیشه دست‌کم آنچه را درخواست کرده است دریافت می‌کند، اما ممکن است حجم
از مقدار درخواستی بیشتر باشد. پس از اتصال، اتصال‌های PersistentVolumeClaim انحصاری هستند،
صرف‌نظر از اینکه چگونه متصل شده‌اند. اتصال PVC به PV یک نگاشت یک‌به‌یک است
که از یک ClaimRef استفاده می‌کند؛ ClaimRef یک اتصال دوطرفه میان PersistentVolume
و PersistentVolumeClaim است.

اگر حجم منطبقی وجود نداشته باشد، Claimها به‌طور نامحدود متصل‌نشده باقی می‌مانند.
Claimها به محض در دسترس قرار گرفتن حجم‌های منطبق متصل خواهند شد. برای مثال،
کلاستری که با تعداد زیادی PV با اندازهٔ 50Gi تأمین شده باشد، با یک PVC که 100Gi درخواست می‌کند مطابقت نخواهد داشت.
این PVC زمانی می‌تواند متصل شود که یک PV با اندازهٔ 100Gi به کلاستر افزوده شود.

### استفاده

Podها از claimها به‌عنوان حجم استفاده می‌کنند. کلاستر claim را بررسی می‌کند تا حجم متصل‌شده را
پیدا کند و آن حجم را برای Pod mount می‌کند. برای حجم‌هایی که از چند
حالت دسترسی پشتیبانی می‌کنند، کاربر هنگام استفاده از claim خود
به‌عنوان حجم در یک Pod، حالت مورد نظر را مشخص می‌کند.

هنگامی که کاربر یک claim داشته باشد و آن claim متصل شده باشد، PV متصل‌شده تا زمانی که
کاربر به آن نیاز دارد متعلق به او است. کاربران Podها را زمان‌بندی می‌کنند و با گنجاندن یک بخش
`persistentVolumeClaim` در بلوک `volumes` یک Pod به PVهای مطالبه‌شدهٔ خود دسترسی پیدا می‌کنند.
برای جزئیات بیشتر در این باره، [Claimها به‌عنوان حجم](#claims-as-volumes) را ببینید.

### محافظت از آبجکت ذخیره‌سازی در حال استفاده

هدف قابلیت محافظت از آبجکت ذخیره‌سازی در حال استفاده (Storage Object in Use Protection) این است که اطمینان حاصل شود
PersistentVolumeClaimهایی (PVC) که به‌طور فعال توسط یک Pod استفاده می‌شوند و PersistentVolumeهایی (PV)
که به PVCها متصل هستند از سیستم حذف نشوند، زیرا این کار ممکن است به از دست رفتن داده منجر شود.

{{< note >}}
یک PVC زمانی به‌طور فعال توسط یک Pod استفاده می‌شود که یک آبجکت Pod وجود داشته باشد که از آن PVC استفاده می‌کند.
{{< /note >}}

اگر کاربر یک PVC را که به‌طور فعال توسط یک Pod استفاده می‌شود حذف کند، آن PVC بلافاصله حذف نمی‌شود.
حذف PVC تا زمانی که دیگر هیچ Podی به‌طور فعال از آن استفاده نکند به تعویق می‌افتد. همچنین،
اگر مدیر یک PV را که به یک PVC متصل است حذف کند، آن PV بلافاصله حذف نمی‌شود.
حذف PV تا زمانی که دیگر به هیچ PVCی متصل نباشد به تعویق می‌افتد.

می‌توانید ببینید که یک PVC محافظت‌شده است، هنگامی که وضعیت PVC برابر `Terminating` باشد و
فهرست `Finalizers` شامل `kubernetes.io/pvc-protection` باشد:

```shell
kubectl describe pvc hostpath
Name:          hostpath
Namespace:     default
StorageClass:  example-hostpath
Status:        Terminating
Volume:
Labels:        <none>
Annotations:   volume.beta.kubernetes.io/storage-class=example-hostpath
               volume.beta.kubernetes.io/storage-provisioner=example.com/hostpath
Finalizers:    [kubernetes.io/pvc-protection]
...
```

همچنین می‌توانید ببینید که یک PV محافظت‌شده است، هنگامی که وضعیت PV برابر `Terminating` باشد و
فهرست `Finalizers` نیز شامل `kubernetes.io/pv-protection` باشد:

```shell
kubectl describe pv task-pv-volume
Name:            task-pv-volume
Labels:          type=local
Annotations:     <none>
Finalizers:      [kubernetes.io/pv-protection]
StorageClass:    standard
Status:          Terminating
Claim:
Reclaim Policy:  Delete
Access Modes:    RWO
Capacity:        1Gi
Message:
Source:
    Type:          HostPath (bare host directory volume)
    Path:          /tmp/data
    HostPathType:
Events:            <none>
```

### بازپس‌گیری (Reclaiming)

هنگامی که کار کاربر با حجمش تمام شد، می‌تواند آبجکت‌های PVC را از
API حذف کند که این کار امکان بازپس‌گیری منبع را فراهم می‌کند. سیاست بازپس‌گیری (reclaim policy) یک PersistentVolume
به کلاستر می‌گوید که پس از آزاد شدن حجم از claim خود، با آن چه کند.
در حال حاضر، حجم‌ها می‌توانند نگه‌داشته (Retained)، بازیافت (Recycled) یا حذف (Deleted) شوند.

#### Retain

سیاست بازپس‌گیری `Retain` امکان بازپس‌گیری دستی منبع را فراهم می‌کند.
هنگامی که PersistentVolumeClaim حذف می‌شود، PersistentVolume همچنان وجود دارد
و حجم «آزادشده» (released) در نظر گرفته می‌شود. اما هنوز برای
claim دیگری در دسترس نیست، زیرا داده‌های مطالبه‌کنندهٔ قبلی روی حجم باقی مانده است.
مدیر می‌تواند با گام‌های زیر حجم را به‌صورت دستی بازپس بگیرد.

1. PersistentVolume را حذف کنید. دارایی ذخیره‌سازی مرتبط در زیرساخت خارجی
   پس از حذف PV همچنان وجود دارد.
1. داده‌های روی دارایی ذخیره‌سازی مرتبط را متناسب با آن به‌صورت دستی پاک‌سازی کنید.
1. دارایی ذخیره‌سازی مرتبط را به‌صورت دستی حذف کنید.

اگر می‌خواهید از همان دارایی ذخیره‌سازی دوباره استفاده کنید، یک PersistentVolume جدید با
همان تعریف دارایی ذخیره‌سازی ایجاد کنید.

#### Delete

برای پلاگین‌های حجمی که از سیاست بازپس‌گیری `Delete` پشتیبانی می‌کنند، حذف کردن
هم آبجکت PersistentVolume را از کوبرنتیز و هم دارایی ذخیره‌سازی مرتبط را
در زیرساخت خارجی حذف می‌کند. حجم‌هایی که به‌طور پویا تأمین شده‌اند
[سیاست بازپس‌گیری StorageClass خود](#reclaim-policy) را به ارث می‌برند که
مقدار پیش‌فرض آن `Delete` است. مدیر باید StorageClass را
مطابق انتظارات کاربران پیکربندی کند؛ در غیر این صورت، PV باید پس از ایجاد
ویرایش یا patch شود. ببینید:
[تغییر سیاست بازپس‌گیری یک PersistentVolume](/docs/tasks/administer-cluster/change-pv-reclaim-policy/).

#### Recycle

{{< warning >}}
سیاست بازپس‌گیری `Recycle` منسوخ شده است. به‌جای آن، رویکرد توصیه‌شده
استفاده از تأمین پویا است.
{{< /warning >}}

اگر پلاگین حجم زیربنایی پشتیبانی کند، سیاست بازپس‌گیری `Recycle` یک پاک‌سازی
پایه (`rm -rf /thevolume/*`) روی حجم انجام می‌دهد و آن را دوباره برای یک claim جدید در دسترس قرار می‌دهد.

با این حال، مدیر می‌تواند با استفاده از آرگومان‌های خط فرمان
controller manager کوبرنتیز، همان‌طور که در
[مرجع](/docs/reference/command-line-tools-reference/kube-controller-manager/) توضیح داده شده است، یک الگوی Pod بازیافت‌کنندهٔ سفارشی پیکربندی کند.
الگوی Pod بازیافت‌کنندهٔ سفارشی باید شامل مشخصهٔ `volumes` باشد، همان‌طور که
در مثال زیر نشان داده شده است:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pv-recycler
  namespace: default
spec:
  restartPolicy: Never
  volumes:
  - name: vol
    hostPath:
      path: /any/path/it/will/be/replaced
  containers:
  - name: pv-recycler
    image: "registry.k8s.io/busybox"
    command: ["/bin/sh", "-c", "test -e /scrub && rm -rf /scrub/..?* /scrub/.[!.]* /scrub/*  && test -z \"$(ls -A /scrub)\" || exit 1"]
    volumeMounts:
    - name: vol
      mountPath: /scrub
```

با این حال، مسیر مشخص‌شده در بخش `volumes` الگوی Pod بازیافت‌کنندهٔ سفارشی
با مسیر مشخص حجمی که در حال بازیافت است جایگزین می‌شود.

### finalizer محافظت از حذف PersistentVolume
{{< feature-state feature_gate_name="HonorPVReclaimPolicy" >}}

می‌توان finalizerهایی را به یک PersistentVolume افزود تا اطمینان حاصل شود PersistentVolumeهایی
که سیاست بازپس‌گیری `Delete` دارند، تنها پس از حذف ذخیره‌سازی پشتیبان حذف می‌شوند.

finalizer `external-provisioner.volume.kubernetes.io/finalizer` (معرفی‌شده
در v1.31) هم به حجم‌های CSI تأمین‌شده به‌صورت پویا و هم به حجم‌های CSI تأمین‌شده به‌صورت ایستا
افزوده می‌شود.

finalizer `kubernetes.io/pv-controller` (معرفی‌شده در v1.31) به
حجم‌های پلاگین درون‌درختی (in-tree) که به‌صورت پویا تأمین شده‌اند افزوده می‌شود و برای حجم‌های پلاگین درون‌درختی
که به‌صورت ایستا تأمین شده‌اند نادیده گرفته می‌شود.

در ادامه نمونه‌ای از یک حجم پلاگین درون‌درختی که به‌صورت پویا تأمین شده است آمده است:

```shell
kubectl describe pv pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Name:            pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Labels:          <none>
Annotations:     kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
                 pv.kubernetes.io/bound-by-controller: yes
                 pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
Finalizers:      [kubernetes.io/pv-protection kubernetes.io/pv-controller]
StorageClass:    vcp-sc
Status:          Bound
Claim:           default/vcp-pvc-1
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        1Gi
Node Affinity:   <none>
Message:
Source:
    Type:               vSphereVolume (a Persistent Disk resource in vSphere)
    VolumePath:         [vsanDatastore] d49c4a62-166f-ce12-c464-020077ba5d46/kubernetes-dynamic-pvc-74a498d6-3929-47e8-8c02-078c1ece4d78.vmdk
    FSType:             ext4
    StoragePolicyName:  vSAN Default Storage Policy
Events:                 <none>
```

finalizer `external-provisioner.volume.kubernetes.io/finalizer` برای حجم‌های CSI افزوده می‌شود.
در ادامه یک نمونه آمده است:

```shell
Name:            pvc-2f0bab97-85a8-4552-8044-eb8be45cf48d
Labels:          <none>
Annotations:     pv.kubernetes.io/provisioned-by: csi.vsphere.vmware.com
Finalizers:      [kubernetes.io/pv-protection external-provisioner.volume.kubernetes.io/finalizer]
StorageClass:    fast
Status:          Bound
Claim:           demo-app/nginx-logs
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        200Mi
Node Affinity:   <none>
Message:
Source:
    Type:              CSI (a Container Storage Interface (CSI) volume source)
    Driver:            csi.vsphere.vmware.com
    FSType:            ext4
    VolumeHandle:      44830fa8-79b4-406b-8b58-621ba25353fd
    ReadOnly:          false
    VolumeAttributes:      storage.kubernetes.io/csiProvisionerIdentity=1648442357185-8081-csi.vsphere.vmware.com
                           type=vSphere CNS Block Volume
Events:                <none>
```

هنگامی که feature flag `CSIMigration{provider}` برای یک پلاگین حجم درون‌درختی مشخص فعال باشد،
finalizer `kubernetes.io/pv-controller` با finalizer
`external-provisioner.volume.kubernetes.io/finalizer` جایگزین می‌شود.

این finalizerها تضمین می‌کنند که آبجکت PV تنها پس از حذف حجم از
backend ذخیره‌سازی حذف شود، به شرط آنکه سیاست بازپس‌گیری PV برابر `Delete` باشد. این
همچنین تضمین می‌کند که حجم، صرف‌نظر از ترتیب حذف PV و PVC،
از backend ذخیره‌سازی حذف شود.

### رزرو کردن یک PersistentVolume

control plane می‌تواند [PersistentVolumeClaimها را به PersistentVolumeهای منطبق متصل کند](#binding)
که در کلاستر وجود دارند. با این حال، اگر می‌خواهید یک PVC به یک PV مشخص متصل شود، باید آن‌ها را از پیش به هم متصل کنید.

با مشخص کردن یک PersistentVolume در یک PersistentVolumeClaim، اتصالی
میان آن PV و PVC مشخص اعلام می‌کنید. اگر آن PersistentVolume وجود داشته باشد و از طریق فیلد `claimRef` خود
PersistentVolumeClaimی را رزرو نکرده باشد، آنگاه PersistentVolume و
PersistentVolumeClaim به هم متصل خواهند شد.

این اتصال صرف‌نظر از برخی معیارهای تطبیق حجم، از جمله node affinity، انجام می‌شود.
control plane همچنان بررسی می‌کند که [storage class](/docs/concepts/storage/storage-classes/)،
حالت‌های دسترسی و اندازهٔ ذخیره‌سازی درخواستی معتبر باشند.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: foo-pvc
  namespace: foo
spec:
  storageClassName: "" # Empty string must be explicitly set otherwise default StorageClass will be set
  volumeName: foo-pv
  ...
```

این روش هیچ امتیاز اتصالی را برای PersistentVolume تضمین نمی‌کند.
اگر PersistentVolumeClaimهای دیگری بتوانند از PVی که مشخص می‌کنید استفاده کنند، ابتدا
باید آن حجم ذخیره‌سازی را رزرو کنید. PersistentVolumeClaim مربوط را
در فیلد `claimRef` آن PV مشخص کنید تا PVCهای دیگر نتوانند به آن متصل شوند.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: foo-pv
spec:
  storageClassName: ""
  claimRef:
    name: foo-pvc
    namespace: foo
  ...
```

این کار زمانی مفید است که بخواهید PersistentVolumeهایی را مصرف کنید که `persistentVolumeReclaimPolicy` آن‌ها
روی `Retain` تنظیم شده است، از جمله مواردی که از یک PV موجود دوباره استفاده می‌کنید.

### گسترش Persistent Volumes Claimها

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

پشتیبانی از گسترش PersistentVolumeClaimها (PVCها) به‌طور پیش‌فرض فعال است. می‌توانید
انواع حجم زیر را گسترش دهید:

* {{< glossary_tooltip text="csi" term_id="csi" >}} (شامل برخی انواع حجم
مهاجرت‌داده‌شده به CSI)
* flexVolume (منسوخ‌شده)
* portworxVolume (منسوخ‌شده)

تنها زمانی می‌توانید یک PVC را گسترش دهید که فیلد `allowVolumeExpansion` در storage class آن روی true تنظیم شده باشد.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: example-vol-default
provisioner: vendor-name.example/magicstorage
parameters:
  resturl: "http://192.168.10.100:8080"
  restuser: ""
  secretNamespace: ""
  secretName: ""
allowVolumeExpansion: true
```

برای درخواست یک حجم بزرگ‌تر برای یک PVC، آبجکت PVC را ویرایش کنید و اندازهٔ
بزرگ‌تری مشخص کنید. این کار گسترش حجمی را که پشتیبان PersistentVolume زیربنایی است آغاز می‌کند. هرگز
PersistentVolume جدیدی برای برآورده کردن claim ایجاد نمی‌شود. بلکه اندازهٔ یک حجم موجود تغییر داده می‌شود.

{{< warning >}}
ویرایش مستقیم اندازهٔ یک PersistentVolume می‌تواند از تغییر اندازهٔ خودکار آن حجم جلوگیری کند.
اگر ظرفیت یک PersistentVolume را ویرایش کنید و سپس `.spec` یک
PersistentVolumeClaim منطبق را ویرایش کنید تا اندازهٔ PersistentVolumeClaim با PersistentVolume برابر شود،
هیچ تغییر اندازه‌ای در ذخیره‌سازی رخ نمی‌دهد.
control plane کوبرنتیز می‌بیند که وضعیت مطلوب هر دو منبع با هم منطبق است
و نتیجه می‌گیرد که اندازهٔ حجم پشتیبان به‌صورت دستی
افزایش یافته است و نیازی به تغییر اندازه نیست.
{{< /warning >}}

#### گسترش حجم CSI

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

پشتیبانی از گسترش حجم‌های CSI به‌طور پیش‌فرض فعال است، اما همچنین لازم است
درایور CSI مورد نظر از گسترش حجم پشتیبانی کند. برای اطلاعات بیشتر به مستندات
درایور CSI مربوط مراجعه کنید.

#### تغییر اندازهٔ حجمی که دارای سیستم فایل است

تنها زمانی می‌توانید اندازهٔ حجم‌های دارای سیستم فایل را تغییر دهید که سیستم فایل XFS، Ext3 یا Ext4 باشد.

هنگامی که یک حجم دارای سیستم فایل باشد، سیستم فایل تنها زمانی تغییر اندازه می‌دهد که یک Pod جدید
از PersistentVolumeClaim در حالت `ReadWrite` استفاده کند. گسترش سیستم فایل یا هنگام راه‌اندازی یک Pod انجام می‌شود
یا زمانی که یک Pod در حال اجراست و سیستم فایل زیربنایی از گسترش آنلاین پشتیبانی می‌کند.

FlexVolumeها (منسوخ‌شده از کوبرنتیز v1.23) در صورتی امکان تغییر اندازه را می‌دهند که درایور با
قابلیت `RequiresFSResize` برابر `true` پیکربندی شده باشد. اندازهٔ FlexVolume را می‌توان هنگام راه‌اندازی مجدد Pod تغییر داد.

#### تغییر اندازهٔ یک PersistentVolumeClaim در حال استفاده

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

در این حالت، نیازی نیست Pod یا deploymentی را که از یک PVC موجود استفاده می‌کند حذف و دوباره ایجاد کنید.
هر PVC در حال استفاده، به محض گسترش سیستم فایل آن، به‌طور خودکار برای Pod خود در دسترس قرار می‌گیرد.
این قابلیت هیچ تأثیری بر PVCهایی که توسط یک Pod یا deployment استفاده نمی‌شوند ندارد. پیش از آنکه گسترش
کامل شود، باید یک Pod ایجاد کنید که از آن PVC استفاده کند.

همانند سایر انواع حجم، حجم‌های FlexVolume نیز هنگامی که توسط یک Pod در حال استفاده هستند می‌توانند گسترش یابند.

{{< note >}}
تغییر اندازهٔ FlexVolume تنها زمانی امکان‌پذیر است که درایور زیربنایی از تغییر اندازه پشتیبانی کند.
{{< /note >}}

#### بازیابی از خطا هنگام گسترش حجم‌ها

اگر کاربر اندازهٔ جدیدی را مشخص کند که بزرگ‌تر از آن است که سیستم ذخیره‌سازی زیربنایی
بتواند برآورده کند، گسترش PVC به‌طور پیوسته دوباره تلاش می‌شود تا زمانی که کاربر یا
مدیر کلاستر اقدامی انجام دهد. این وضعیت ممکن است نامطلوب باشد و از این رو
کوبرنتیز روش‌های زیر را برای بازیابی از چنین خطاهایی فراهم می‌کند.

{{< tabs name="recovery_methods" >}}
{{% tab name="به‌صورت دستی با دسترسی مدیر کلاستر" %}}

اگر گسترش ذخیره‌سازی زیربنایی با شکست مواجه شود، مدیر کلاستر می‌تواند وضعیت
Persistent Volume Claim (PVC) را به‌صورت دستی بازیابی کند و درخواست‌های تغییر اندازه را لغو کند.
در غیر این صورت، درخواست‌های تغییر اندازه بدون دخالت مدیر به‌طور پیوسته
توسط کنترل‌کننده دوباره تلاش می‌شوند.

1. PersistentVolume (PV) متصل به PersistentVolumeClaim (PVC) را
   با سیاست بازپس‌گیری `Retain` علامت‌گذاری کنید.
2. PVC را حذف کنید. از آنجا که PV سیاست بازپس‌گیری `Retain` دارد، هنگام ایجاد مجدد PVC
   هیچ داده‌ای از دست نمی‌دهیم.
3. مدخل `claimRef` را از مشخصات PV حذف کنید تا PVC جدید بتواند به آن متصل شود.
   این کار باید PV را به وضعیت `Available` درآورد.
4. PVC را با اندازه‌ای کوچک‌تر از PV دوباره ایجاد کنید و فیلد `volumeName`
   آن PVC را روی نام PV تنظیم کنید. این کار باید PVC جدید را به PV موجود متصل کند.
5. فراموش نکنید سیاست بازپس‌گیری PV را به حالت قبل بازگردانید.

{{% /tab %}}
{{% tab name="با درخواست گسترش به اندازه‌ای کوچک‌تر" %}}

اگر گسترش یک PVC با شکست مواجه شده باشد، می‌توانید گسترش را با
اندازه‌ای کوچک‌تر از مقدار درخواستی قبلی دوباره امتحان کنید. برای درخواست تلاش جدید برای گسترش با
اندازهٔ پیشنهادی کوچک‌تر، `.spec.resources` آن PVC را ویرایش کنید و مقداری کمتر از
مقداری که پیش‌تر امتحان کرده بودید انتخاب کنید.
این کار زمانی مفید است که گسترش به مقدار بالاتر به دلیل محدودیت ظرفیت موفق نشده باشد.
اگر چنین اتفاقی افتاده باشد، یا گمان کنید که ممکن است افتاده باشد، می‌توانید با مشخص کردن
اندازه‌ای که در محدودهٔ ظرفیت ارائه‌دهندهٔ ذخیره‌سازی زیربنایی است، گسترش را دوباره امتحان کنید. می‌توانید وضعیت
عملیات تغییر اندازه را با پایش `.status.allocatedResourceStatuses` و رویدادهای PVC دنبال کنید.

توجه داشته باشید که
اگرچه می‌توانید مقدار ذخیره‌سازی کمتری از آنچه پیش‌تر درخواست شده بود مشخص کنید،
مقدار جدید همچنان باید بیشتر از `.status.capacity` باشد.
کوبرنتیز از کوچک کردن یک PVC به کمتر از اندازهٔ فعلی آن پشتیبانی نمی‌کند.
{{% /tab %}}
{{% /tabs %}}

## انواع Persistent Volumeها

انواع PersistentVolume به‌صورت پلاگین پیاده‌سازی شده‌اند. کوبرنتیز در حال حاضر از پلاگین‌های زیر پشتیبانی می‌کند:

* [`csi`](/docs/concepts/storage/volumes/#csi) - Container Storage Interface (CSI)
* [`fc`](/docs/concepts/storage/volumes/#fc) - ذخیره‌سازی Fibre Channel (FC)
* [`hostPath`](/docs/concepts/storage/volumes/#hostpath) - حجم HostPath
  (فقط برای آزمایش روی یک نود؛ در یک کلاستر چندنودی کار نخواهد کرد؛
  به‌جای آن استفاده از حجم `local` را در نظر بگیرید)
* [`iscsi`](/docs/concepts/storage/volumes/#iscsi) - ذخیره‌سازی iSCSI (SCSI روی IP)
* [`local`](/docs/concepts/storage/volumes/#local) - دستگاه‌های ذخیره‌سازی محلی
  که روی نودها mount شده‌اند.
* [`nfs`](/docs/concepts/storage/volumes/#nfs) - ذخیره‌سازی Network File System (NFS)

انواع PersistentVolume زیر منسوخ شده‌اند اما همچنان در دسترس هستند.
اگر از این انواع حجم، به‌جز `flexVolume`، `cephfs` و `rbd`، استفاده می‌کنید،
لطفاً درایورهای CSI متناظر را نصب کنید.

* [`awsElasticBlockStore`](/docs/concepts/storage/volumes/#awselasticblockstore) - AWS Elastic Block Store (EBS)
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.23)
* [`azureDisk`](/docs/concepts/storage/volumes/#azuredisk) - Azure Disk
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.23)
* [`azureFile`](/docs/concepts/storage/volumes/#azurefile) - Azure File
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.24)
* [`cinder`](/docs/concepts/storage/volumes/#cinder) - Cinder (ذخیره‌سازی بلوکی OpenStack)
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.21)
* [`flexVolume`](/docs/concepts/storage/volumes/#flexvolume) - FlexVolume
  (**منسوخ‌شده** از v1.23، بدون برنامهٔ مهاجرت و بدون برنامه برای حذف پشتیبانی)
* [`gcePersistentDisk`](/docs/concepts/storage/volumes/#gcePersistentDisk) - GCE Persistent Disk
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.23)
* [`portworxVolume`](/docs/concepts/storage/volumes/#portworxvolume) - حجم Portworx
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.31)
* [`vsphereVolume`](/docs/concepts/storage/volumes/#vspherevolume) - حجم vSphere VMDK
  (**مهاجرت به‌طور پیش‌فرض فعال** از v1.25)

نسخه‌های قدیمی‌تر کوبرنتیز از انواع PersistentVolume درون‌درختی زیر نیز پشتیبانی می‌کردند:

* [`cephfs`](/docs/concepts/storage/volumes/#cephfs)
  (**در دسترس نیست** از v1.31)
* `flocker` - ذخیره‌سازی Flocker.
  (**در دسترس نیست** از v1.25)
* `glusterfs` - ذخیره‌سازی GlusterFS.
  (**در دسترس نیست** از v1.26)
* `photonPersistentDisk` - دیسک پایدار Photon controller.
  (**در دسترس نیست** از v1.15)
* `quobyte` - حجم Quobyte.
  (**در دسترس نیست** از v1.25)
* [`rbd`](/docs/concepts/storage/volumes/#rbd) - حجم Rados Block Device (RBD)
  (**در دسترس نیست** از v1.31)
* `scaleIO` - حجم ScaleIO.
  (**در دسترس نیست** از v1.21)
* `storageos` - حجم StorageOS.
  (**در دسترس نیست** از v1.25)

## Persistent Volumeها

هر PV شامل یک spec و یک status است که به ترتیب مشخصات و وضعیت حجم هستند.
نام یک آبجکت PersistentVolume باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  mountOptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
```

{{< note >}}
برای مصرف یک PersistentVolume در یک کلاستر ممکن است به برنامه‌های کمکی مرتبط با نوع حجم
نیاز باشد. در این مثال، PersistentVolume
از نوع NFS است و برنامهٔ کمکی /sbin/mount.nfs برای پشتیبانی از
mount کردن سیستم‌های فایل NFS لازم است.
{{< /note >}}

### ظرفیت

به‌طور کلی، یک PV ظرفیت ذخیره‌سازی مشخصی خواهد داشت. این ظرفیت با استفاده از ویژگی
`capacity` در PV تنظیم می‌شود که یک مقدار {{< glossary_tooltip term_id="quantity" >}} است.

در حال حاضر، اندازهٔ ذخیره‌سازی تنها منبعی است که می‌توان آن را تنظیم یا درخواست کرد.
ویژگی‌های آینده ممکن است شامل IOPS، توان عملیاتی (throughput) و موارد دیگر باشند.

### حالت حجم (Volume Mode)

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

کوبرنتیز از دو `volumeModes` برای PersistentVolumeها پشتیبانی می‌کند: `Filesystem` و `Block`.

`volumeMode` یک پارامتر اختیاری API است.
`Filesystem` حالت پیش‌فرضی است که هنگام حذف پارامتر `volumeMode` استفاده می‌شود.

حجمی با `volumeMode: Filesystem` در یک دایرکتوری درون Podها *mount* می‌شود. اگر حجم
توسط یک دستگاه بلوکی پشتیبانی شود و دستگاه خالی باشد، کوبرنتیز پیش از نخستین mount
یک سیستم فایل روی دستگاه ایجاد می‌کند.

می‌توانید مقدار `volumeMode` را روی `Block` تنظیم کنید تا از یک حجم به‌عنوان دستگاه بلوکی خام استفاده کنید.
چنین حجمی به‌صورت یک دستگاه بلوکی، بدون هیچ سیستم فایلی روی آن، در اختیار Pod قرار می‌گیرد.
این حالت برای فراهم کردن سریع‌ترین روش ممکن دسترسی Pod به یک حجم، بدون
هیچ لایهٔ سیستم فایلی میان Pod و حجم، مفید است. از سوی دیگر، برنامه‌ای
که در Pod اجرا می‌شود باید بداند چگونه با یک دستگاه بلوکی خام کار کند.
برای نمونه‌ای از نحوهٔ استفاده از یک حجم با `volumeMode: Block` در یک Pod،
[پشتیبانی از حجم بلوکی خام](#raw-block-volume-support) را ببینید.

### حالت‌های دسترسی (Access Modes)

یک PersistentVolume را می‌توان به هر روشی که ارائه‌دهندهٔ منبع پشتیبانی می‌کند روی یک میزبان mount کرد.
همان‌طور که در جدول زیر نشان داده شده است، ارائه‌دهندگان قابلیت‌های متفاوتی خواهند داشت
و حالت‌های دسترسی هر PV روی حالت‌های مشخصی که آن حجم خاص پشتیبانی می‌کند
تنظیم می‌شوند. برای مثال، NFS می‌تواند از چندین کلاینت خواندن/نوشتن پشتیبانی کند، اما یک
PV مشخص از نوع NFS ممکن است روی سرور به‌صورت فقط‌خواندنی export شده باشد. هر PV مجموعهٔ
حالت‌های دسترسی خود را دارد که قابلیت‌های همان PV خاص را توصیف می‌کند.

حالت‌های دسترسی عبارت‌اند از:

`ReadWriteOnce`
: حجم می‌تواند توسط یک نود منفرد به‌صورت خواندنی-نوشتنی mount شود. حالت دسترسی ReadWriteOnce
  همچنان می‌تواند به چندین pod اجازه دهد هنگامی که روی یک نود اجرا می‌شوند به آن حجم دسترسی داشته باشند
  (از آن بخوانند یا در آن بنویسند). برای دسترسی یک pod منفرد، لطفاً ReadWriteOncePod را ببینید.

`ReadOnlyMany`
: حجم می‌تواند توسط چندین نود به‌صورت فقط‌خواندنی mount شود.

`ReadWriteMany`
: حجم می‌تواند توسط چندین نود به‌صورت خواندنی-نوشتنی mount شود.

 `ReadWriteOncePod`
: {{< feature-state for_k8s_version="v1.29" state="stable" >}}
  حجم می‌تواند توسط یک Pod منفرد به‌صورت خواندنی-نوشتنی mount شود. اگر می‌خواهید اطمینان حاصل کنید
  که در کل کلاستر تنها یک pod می‌تواند آن PVC را بخواند یا در آن بنویسد، از حالت دسترسی
  ReadWriteOncePod استفاده کنید.

{{< note >}}
حالت دسترسی `ReadWriteOncePod` تنها برای حجم‌های
{{< glossary_tooltip text="CSI" term_id="csi" >}} و کوبرنتیز نسخهٔ
1.22 به بالا پشتیبانی می‌شود. برای استفاده از این قابلیت باید
[sidecarهای CSI](https://kubernetes-csi.github.io/docs/sidecar-containers.html) زیر
را به این نسخه‌ها یا بالاتر به‌روزرسانی کنید:

* [csi-provisioner:v3.0.0+](https://github.com/kubernetes-csi/external-provisioner/releases/tag/v3.0.0)
* [csi-attacher:v3.3.0+](https://github.com/kubernetes-csi/external-attacher/releases/tag/v3.3.0)
* [csi-resizer:v1.3.0+](https://github.com/kubernetes-csi/external-resizer/releases/tag/v1.3.0)
{{< /note >}}

در CLI، حالت‌های دسترسی به این صورت خلاصه می‌شوند:

* RWO - ReadWriteOnce
* ROX - ReadOnlyMany
* RWX - ReadWriteMany
* RWOP - ReadWriteOncePod

{{< note >}}
کوبرنتیز از حالت‌های دسترسی حجم برای تطبیق PersistentVolumeClaimها و PersistentVolumeها استفاده می‌کند.
در برخی موارد، حالت‌های دسترسی حجم همچنین محدود می‌کنند که PersistentVolume کجا می‌تواند mount شود.
حالت‌های دسترسی حجم پس از mount شدن ذخیره‌سازی، محافظت در برابر نوشتن را اعمال **نمی‌کنند**.
حتی اگر حالت‌های دسترسی به‌صورت ReadWriteOnce، ReadOnlyMany یا ReadWriteMany مشخص شده باشند،
هیچ محدودیتی روی حجم اعمال نمی‌کنند. برای مثال، حتی اگر یک PersistentVolume
به‌صورت ReadOnlyMany ایجاد شده باشد، هیچ تضمینی وجود ندارد که فقط‌خواندنی باشد. اگر حالت‌های دسترسی
به‌صورت ReadWriteOncePod مشخص شده باشند، حجم محدود می‌شود و تنها روی یک Pod منفرد می‌تواند mount شود.
{{< /note >}}

> __مهم!__ یک حجم در هر زمان تنها با استفاده از یک حالت دسترسی می‌تواند mount شود،
> حتی اگر از چندین حالت پشتیبانی کند.

| پلاگین حجم           | ReadWriteOnce          | ReadOnlyMany          | ReadWriteMany | ReadWriteOncePod       |
| :---                 | :---:                  | :---:                 | :---:         | -                      |
| AzureFile            | &#x2713;               | &#x2713;              | &#x2713;      | -                      |
| CephFS               | &#x2713;               | &#x2713;              | &#x2713;      | -                      |
| CSI                  | بسته به درایور  | بسته به درایور | بسته به درایور | بسته به درایور |
| FC                   | &#x2713;               | &#x2713;              | -             | -                      |
| FlexVolume           | &#x2713;               | &#x2713;              | بسته به درایور | -              |
| HostPath             | &#x2713;               | -                     | -             | -                      |
| iSCSI                | &#x2713;               | &#x2713;              | -             | -                      |
| NFS                  | &#x2713;               | &#x2713;              | &#x2713;      | -                      |
| RBD                  | &#x2713;               | &#x2713;              | -             | -                      |
| VsphereVolume        | &#x2713;               | -                     | - (هنگامی که Podها روی یک نود هم‌مکان باشند کار می‌کند) | - |
| PortworxVolume       | &#x2713;               | -                     | &#x2713;      | -                  | - |

### کلاس

یک PV می‌تواند یک کلاس داشته باشد که با تنظیم
ویژگی `storageClassName` روی نام یک
[StorageClass](/docs/concepts/storage/storage-classes/) مشخص می‌شود.
یک PV از یک کلاس خاص تنها می‌تواند به PVCهایی متصل شود که
آن کلاس را درخواست می‌کنند. یک PV بدون `storageClassName` هیچ کلاسی ندارد و تنها می‌تواند
به PVCهایی متصل شود که هیچ کلاس خاصی را درخواست نمی‌کنند.

در گذشته، حاشیه‌نویسی (annotation) `volume.beta.kubernetes.io/storage-class` به‌جای
ویژگی `storageClassName` استفاده می‌شد. این حاشیه‌نویسی همچنان کار می‌کند؛ با این حال،
در یکی از نسخه‌های آیندهٔ کوبرنتیز به‌طور کامل منسوخ خواهد شد.

### سیاست بازپس‌گیری

سیاست‌های بازپس‌گیری فعلی عبارت‌اند از:

* Retain -- بازپس‌گیری دستی
* Recycle -- پاک‌سازی پایه (`rm -rf /thevolume/*`)
* Delete -- حذف حجم

برای کوبرنتیز {{< skew currentVersion >}}، تنها انواع حجم `nfs` و `hostPath` از بازیافت پشتیبانی می‌کنند.

### گزینه‌های mount

مدیر کوبرنتیز می‌تواند گزینه‌های mount اضافی را برای زمانی که یک
Persistent Volume روی یک نود mount می‌شود مشخص کند.

{{< note >}}
همهٔ انواع Persistent Volume از گزینه‌های mount پشتیبانی نمی‌کنند.
{{< /note >}}

انواع حجم زیر از گزینه‌های mount پشتیبانی می‌کنند:

* `csi` (شامل انواع حجم مهاجرت‌داده‌شده به CSI)
* `iscsi`
* `nfs`

گزینه‌های mount اعتبارسنجی نمی‌شوند. اگر یک گزینهٔ mount نامعتبر باشد، mount با شکست مواجه می‌شود.

در گذشته، حاشیه‌نویسی `volume.beta.kubernetes.io/mount-options` به‌جای
ویژگی `mountOptions` استفاده می‌شد. این حاشیه‌نویسی همچنان کار می‌کند؛ با این حال،
در یکی از نسخه‌های آیندهٔ کوبرنتیز به‌طور کامل منسوخ خواهد شد.

### Node Affinity

{{< note >}}
برای بیشتر انواع حجم، نیازی به تنظیم این فیلد ندارید.
برای حجم‌های [local](/docs/concepts/storage/volumes/#local) باید این فیلد را به‌صراحت تنظیم کنید.
{{< /note >}}

یک PV می‌تواند node affinity مشخص کند تا محدودیت‌هایی تعریف کند که تعیین می‌کنند از کدام نودها
می‌توان به این حجم دسترسی داشت. Podهایی که از یک PV استفاده می‌کنند تنها روی نودهایی زمان‌بندی می‌شوند
که توسط node affinity انتخاب شده‌اند. برای مشخص کردن node affinity،
`nodeAffinity` را در `.spec` یک PV تنظیم کنید. مرجع API
[PersistentVolume](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/#PersistentVolumeSpec)
جزئیات بیشتری دربارهٔ این فیلد دارد.

#### به‌روزرسانی‌های node affinity

{{< feature-state feature_gate_name="MutablePVNodeAffinity" >}}

اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `MutablePVNodeAffinity` در کلاستر شما فعال باشد،
فیلد `.spec.nodeAffinity` یک PersistentVolume قابل تغییر است.
این امکان به مدیران کلاستر یا کنترل‌کنندهٔ ذخیره‌سازی خارجی اجازه می‌دهد هنگام مهاجرت داده‌ها، node affinity یک PersistentVolume را
بدون ایجاد وقفه در podهای در حال اجرا به‌روزرسانی کنند.

هنگام به‌روزرسانی node affinity، باید اطمینان حاصل کنید که node affinity جدید همچنان با نودهایی که حجم در حال حاضر روی آن‌ها استفاده می‌شود مطابقت دارد.
podهایی که affinity جدید را نقض می‌کنند، اگر از قبل در حال اجرا باشند، ممکن است به اجرای خود ادامه دهند. اما کوبرنتیز از این پیکربندی پشتیبانی نمی‌کند.
باید podهای ناقض را به‌زودی خاتمه دهید.
به دلیل کش در حافظه، podهایی که پس از به‌روزرسانی ایجاد می‌شوند ممکن است برای مدت کوتاهی همچنان مطابق node affinity قدیمی زمان‌بندی شوند.

برای استفاده از این قابلیت، باید feature gate `MutablePVNodeAffinity` را روی مؤلفه‌های زیر فعال کنید:

- `kube-apiserver`
- `kubelet`

### فاز (Phase)

یک PersistentVolume در یکی از فازهای زیر خواهد بود:

`Available`
: یک منبع آزاد که هنوز به هیچ claimی متصل نشده است

`Bound`
: حجم به یک claim متصل شده است

`Released`
: claim حذف شده است، اما منبع ذخیره‌سازی مرتبط هنوز توسط کلاستر بازپس گرفته نشده است

`Failed`
: بازپس‌گیری (خودکار) حجم با شکست مواجه شده است

می‌توانید نام PVC متصل به PV را با استفاده از `kubectl describe persistentvolume <name>` ببینید.

#### مهر زمانی گذار فاز

{{< feature-state feature_gate_name="PersistentVolumeLastPhaseTransitionTime" >}}

فیلد `.status` یک PersistentVolume می‌تواند شامل فیلد آلفای `lastPhaseTransitionTime` باشد. این فیلد
مهر زمانیِ آخرین گذار فاز حجم را ثبت می‌کند. برای حجم‌هایی که تازه ایجاد شده‌اند،
فاز روی `Pending` و `lastPhaseTransitionTime` روی
زمان فعلی تنظیم می‌شود.

## PersistentVolumeClaimها

هر PVC شامل یک spec و یک status است که به ترتیب مشخصات و وضعیت claim هستند.
نام یک آبجکت PersistentVolumeClaim باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}
```

### حالت‌های دسترسی

Claimها هنگام درخواست ذخیره‌سازی با حالت‌های دسترسی مشخص، از
[همان قراردادهای حجم‌ها](#access-modes) استفاده می‌کنند.

### حالت‌های حجم

Claimها از [همان قرارداد حجم‌ها](#volume-mode) برای نشان دادن
مصرف حجم به‌صورت سیستم فایل یا دستگاه بلوکی استفاده می‌کنند.

### نام حجم

Claimها می‌توانند از فیلد `volumeName` برای اتصال صریح به یک PersistentVolume مشخص استفاده کنند. همچنین می‌توانید
`volumeName` را تنظیم‌نشده باقی بگذارید، که نشان می‌دهد می‌خواهید کوبرنتیز یک PersistentVolume جدید
منطبق با claim راه‌اندازی کند.
اگر PV مشخص‌شده از قبل به PVC دیگری متصل باشد، اتصال
در وضعیت معلق (pending) گیر می‌کند.

### منابع

Claimها، مانند Podها، می‌توانند مقادیر مشخصی از یک منبع را درخواست کنند. در این مورد،
درخواست برای ذخیره‌سازی است. همان
[مدل منبع](https://git.k8s.io/design-proposals-archive/scheduling/resources.md)
هم برای حجم‌ها و هم برای claimها اعمال می‌شود.

{{< note >}}
برای حجم‌های `Filesystem`، درخواست ذخیره‌سازی به اندازهٔ «بیرونی» حجم اشاره دارد
(یعنی اندازهٔ تخصیص‌یافته از backend ذخیره‌سازی).
این بدان معناست که برای ارائه‌دهندگانی که
یک سیستم فایل را روی یک دستگاه بلوکی می‌سازند، اندازهٔ قابل نوشتن ممکن است به دلیل سربار سیستم فایل اندکی کمتر باشد.
این موضوع به‌ویژه در XFS که بسیاری از قابلیت‌های فراداده در آن به‌طور پیش‌فرض فعال هستند مشهود است.
{{< /note >}}

### انتخابگر (Selector)

Claimها می‌توانند یک
[انتخابگر برچسب](/docs/concepts/overview/working-with-objects/labels/#label-selectors)
مشخص کنند تا مجموعهٔ حجم‌ها را بیشتر فیلتر کنند.
تنها حجم‌هایی که برچسب‌هایشان با انتخابگر مطابقت دارد می‌توانند به claim متصل شوند.
انتخابگر می‌تواند از دو فیلد تشکیل شود:

* `matchLabels` - حجم باید برچسبی با این مقدار داشته باشد
* `matchExpressions` - فهرستی از الزامات که با مشخص کردن کلید، فهرست مقادیر،
  و عملگری که کلید و مقادیر را به هم مرتبط می‌کند ساخته می‌شود.
  عملگرهای معتبر شامل `In`، `NotIn`، `Exists` و `DoesNotExist` هستند.

همهٔ الزامات، چه از `matchLabels` و چه از `matchExpressions`، با هم
AND می‌شوند؛ یعنی همهٔ آن‌ها باید برآورده شوند تا تطبیق انجام شود.

### کلاس

یک claim می‌تواند با مشخص کردن نام یک
[StorageClass](/docs/concepts/storage/storage-classes/)
با استفاده از ویژگی `storageClassName` یک کلاس خاص را درخواست کند.
تنها PVهایی از کلاس درخواستی، یعنی آن‌هایی که `storageClassName` یکسانی با PVC دارند،
می‌توانند به PVC متصل شوند.

PVCها لزوماً نباید یک کلاس درخواست کنند. PVCی که `storageClassName` آن
برابر `""` تنظیم شده باشد، همیشه به‌عنوان درخواست یک PV بدون کلاس تفسیر می‌شود، بنابراین
تنها می‌تواند به PVهای بدون کلاس (بدون حاشیه‌نویسی یا با حاشیه‌نویسی برابر `""`) متصل شود.
PVCی که هیچ `storageClassName` ندارد دقیقاً همان نیست و کلاستر بسته به اینکه
[پلاگین پذیرش `DefaultStorageClass`](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
روشن باشد یا نه، با آن به شکل متفاوتی رفتار می‌کند.

* اگر پلاگین پذیرش روشن باشد، مدیر می‌تواند یک StorageClass پیش‌فرض مشخص کند.
  همهٔ PVCهایی که هیچ `storageClassName` ندارند تنها می‌توانند به PVهای آن کلاس پیش‌فرض متصل شوند.
  مشخص کردن StorageClass پیش‌فرض با تنظیم حاشیه‌نویسی
  `storageclass.kubernetes.io/is-default-class` برابر `true` در یک آبجکت StorageClass انجام می‌شود.
  اگر مدیر هیچ پیش‌فرضی مشخص نکند، کلاستر به ایجاد PVC
  طوری پاسخ می‌دهد که گویی پلاگین پذیرش خاموش است.
  اگر بیش از یک StorageClass پیش‌فرض مشخص شده باشد، هنگام تأمین پویای PVC
  جدیدترین پیش‌فرض استفاده می‌شود.
* اگر پلاگین پذیرش خاموش باشد، مفهومی به نام StorageClass پیش‌فرض وجود ندارد.
  همهٔ PVCهایی که `storageClassName` آن‌ها روی `""` تنظیم شده است تنها می‌توانند به PVهایی متصل شوند
  که `storageClassName` آن‌ها نیز روی `""` تنظیم شده است.
  با این حال، PVCهایی که `storageClassName` ندارند، پس از در دسترس قرار گرفتن StorageClass پیش‌فرض می‌توانند بعداً به‌روزرسانی شوند.
  اگر PVC به‌روزرسانی شود، دیگر به PVهایی که `storageClassName` آن‌ها نیز روی `""` تنظیم شده است متصل نخواهد شد.

برای جزئیات بیشتر، [تخصیص عطف به ماسبق StorageClass پیش‌فرض](#retroactive-default-storageclass-assignment) را ببینید.

بسته به روش نصب، ممکن است یک StorageClass پیش‌فرض
در هنگام نصب توسط addon manager در یک کلاستر کوبرنتیز مستقر شود.

هنگامی که یک PVC علاوه بر درخواست یک StorageClass، یک `selector` نیز مشخص کند،
الزامات با هم AND می‌شوند: تنها PVی از کلاس درخواستی و با
برچسب‌های درخواستی می‌تواند به PVC متصل شود.

{{< note >}}
در حال حاضر، برای PVCی با `selector` غیرخالی نمی‌توان یک PV را به‌صورت پویا تأمین کرد.
{{< /note >}}

در گذشته، حاشیه‌نویسی `volume.beta.kubernetes.io/storage-class` به‌جای
ویژگی `storageClassName` استفاده می‌شد. این حاشیه‌نویسی همچنان کار می‌کند؛ با این حال،
در یکی از نسخه‌های آیندهٔ کوبرنتیز پشتیبانی نخواهد شد.

#### تخصیص عطف به ماسبق StorageClass پیش‌فرض

{{< feature-state for_k8s_version="v1.28" state="stable" >}}

می‌توانید یک PersistentVolumeClaim را بدون مشخص کردن `storageClassName`
برای PVC جدید ایجاد کنید، و حتی زمانی که هیچ StorageClass پیش‌فرضی
در کلاستر شما وجود ندارد نیز می‌توانید این کار را انجام دهید. در این حالت، PVC جدید همان‌طور که تعریف کرده‌اید ایجاد می‌شود و
`storageClassName` آن PVC تا زمانی که یک پیش‌فرض در دسترس قرار گیرد تنظیم‌نشده باقی می‌ماند.

هنگامی که یک StorageClass پیش‌فرض در دسترس قرار می‌گیرد، control plane همهٔ
PVCهای موجود بدون `storageClassName` را شناسایی می‌کند. برای PVCهایی که یا مقدار
خالی برای `storageClassName` دارند یا این کلید را ندارند، control plane سپس
آن PVCها را به‌روزرسانی می‌کند تا `storageClassName` را مطابق StorageClass پیش‌فرض جدید تنظیم کند.
اگر یک PVC موجود دارید که `storageClassName` آن `""` است و یک
StorageClass پیش‌فرض پیکربندی می‌کنید، این PVC به‌روزرسانی نخواهد شد.

برای اینکه اتصال به PVهایی که `storageClassName` آن‌ها روی `""` تنظیم شده است
(در حالی که یک StorageClass پیش‌فرض وجود دارد) ادامه یابد، باید `storageClassName`
PVC مرتبط را روی `""` تنظیم کنید.

این رفتار به مدیران کمک می‌کند StorageClass پیش‌فرض را با حذف
نمونهٔ قدیمی ابتدا و سپس ایجاد یا تنظیم نمونهٔ دیگر تغییر دهند. این بازهٔ کوتاه که
هیچ پیش‌فرضی وجود ندارد باعث می‌شود PVCهای بدون `storageClassName` که در آن زمان ایجاد شده‌اند
هیچ پیش‌فرضی نداشته باشند، اما به لطف تخصیص عطف به ماسبق StorageClass پیش‌فرض،
این روش تغییر پیش‌فرض‌ها ایمن است.

### ردیابی PVCهای استفاده‌نشده

{{< feature-state feature_gate_name="PersistentVolumeClaimUnusedSinceTime" >}}

هنگامی که این قابلیت فعال باشد، کنترل‌کنندهٔ محافظت از PVC یک
[وضعیت (condition)](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) با نام `Unused` به هر
PersistentVolumeClaim اضافه می‌کند تا نشان دهد آیا در حال حاضر توسط یک
Pod غیرپایانی (non-terminal) ارجاع داده می‌شود یا خیر.

این condition دو حالت دارد:

`Unused` با status `"True"` (reason `NoPodsUsingPVC`)
: هیچ Pod غیرپایانی به این PVC ارجاع نمی‌دهد. `lastTransitionTime` زمانی را ثبت می‌کند که
  PVC استفاده‌نشده شده است.

`Unused` با status `"False"` (reason `PodUsingPVC`)
: دست‌کم یک Pod غیرپایانی در حال حاضر به این PVC ارجاع می‌دهد.
  `lastTransitionTime` زمانی را ثبت می‌کند که استفاده از PVC آغاز شده است.

یک Pod در صورتی غیرپایانی در نظر گرفته می‌شود که فاز آن `Succeeded` یا `Failed` نباشد.
این بدان معناست که یک Pod در وضعیت Pending (حتی Podی که هنوز زمان‌بندی نشده است)
به‌عنوان استفاده‌کننده از PVC به حساب می‌آید.

`lastTransitionTime` مربوط به condition `Unused` می‌تواند توسط مدیران
کلاستر، ابزارهای پایش و کنترل‌کننده‌های خارجی برای شناسایی PVCهایی که
مدت طولانی استفاده نشده‌اند به کار رود. برای مثال، برای یافتن همهٔ PVCهایی که
بیش از ۳۰ روز استفاده نشده‌اند، می‌توانید PVCهایی را جست‌وجو کنید که condition
`Unused` آن‌ها `status: "True"` دارد و `lastTransitionTime` آن‌ها قدیمی‌تر از ۳۰ روز است.

{{< note >}}
مدت استفاده‌نشدنی که این condition نشان می‌دهد ممکن است به دلیل تأخیرهای پردازش در کنترل‌کننده،
یا به این دلیل که قابلیت پس از استفاده‌نشده شدن PVC فعال شده است، کوتاه‌تر از
زمان واقعی استفاده‌نشدن باشد. این condition برای PVCهایی که `deletionTimestamp` آن‌ها تنظیم شده است
(یعنی PVCهایی که در حال حذف هستند) به‌روزرسانی نمی‌شود.
{{< /note >}}

## Claimها به‌عنوان حجم

Podها با استفاده از claim به‌عنوان حجم به ذخیره‌سازی دسترسی پیدا می‌کنند. Claimها باید در
همان فضای نام (namespace) Pod استفاده‌کننده از claim وجود داشته باشند. کلاستر claim را در
فضای نام Pod پیدا می‌کند و از آن برای دریافت PersistentVolume پشتیبان claim استفاده می‌کند.
سپس حجم روی میزبان و درون Pod mount می‌شود.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
```

### نکته‌ای دربارهٔ فضاهای نام

اتصال‌های PersistentVolume انحصاری هستند، و از آنجا که PersistentVolumeClaimها
آبجکت‌هایی وابسته به فضای نام هستند، mount کردن claimها با حالت‌های «Many» (`ROX`، `RWX`) تنها
درون یک فضای نام امکان‌پذیر است.

### PersistentVolumeهای از نوع `hostPath`

یک PersistentVolume از نوع `hostPath` از یک فایل یا دایرکتوری روی نود برای شبیه‌سازی
ذخیره‌سازی متصل به شبکه استفاده می‌کند. ببینید:
[نمونه‌ای از حجم از نوع `hostPath`](/docs/tutorials/configuration/configure-persistent-volume-storage/#create-a-persistentvolume).


## پشتیبانی از حجم بلوکی خام

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

پلاگین‌های حجم زیر از حجم‌های بلوکی خام، از جمله تأمین پویا در موارد
قابل اعمال، پشتیبانی می‌کنند:

* CSI (شامل برخی انواع حجم مهاجرت‌داده‌شده به CSI)
* FC (Fibre Channel)
* iSCSI
* حجم Local

### PersistentVolume با استفاده از یک حجم بلوکی خام {#persistent-volume-using-a-raw-block-volume}

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: block-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  persistentVolumeReclaimPolicy: Retain
  fc:
    targetWWNs: ["50060e801049cfd1"]
    lun: 0
    readOnly: false
```

### PersistentVolumeClaim درخواست‌کنندهٔ یک حجم بلوکی خام {#persistent-volume-claim-requesting-a-raw-block-volume}

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: block-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  resources:
    requests:
      storage: 10Gi
```

### مشخصات Pod با افزودن مسیر دستگاه بلوکی خام در کانتینر

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-block-volume
spec:
  containers:
    - name: fc-container
      image: fedora:26
      command: ["/bin/sh", "-c"]
      args: [ "tail -f /dev/null" ]
      volumeDevices:
        - name: data
          devicePath: /dev/xvda
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: block-pvc
```

{{< note >}}
هنگام افزودن یک دستگاه بلوکی خام برای یک Pod، به‌جای مسیر mount، مسیر دستگاه را در
کانتینر مشخص می‌کنید.
{{< /note >}}

### اتصال حجم‌های بلوکی

اگر کاربر با مشخص کردن فیلد `volumeMode` در spec مربوط به PersistentVolumeClaim
یک حجم بلوکی خام درخواست کند، قواعد اتصال اندکی با
نسخه‌های قبلی که این حالت را بخشی از spec در نظر نمی‌گرفتند تفاوت دارد.
در ادامه جدولی از ترکیب‌های ممکنی آمده است که کاربر و مدیر ممکن است برای
درخواست یک دستگاه بلوکی خام مشخص کنند. این جدول نشان می‌دهد که با توجه به این ترکیب‌ها حجم متصل خواهد شد
یا نه: ماتریس اتصال حجم برای حجم‌هایی که به‌صورت ایستا تأمین شده‌اند:

| volumeMode در PV | volumeMode در PVC  | نتیجه           |
| --------------|:---------------:| ----------------:|
|   مشخص‌نشده | مشخص‌نشده     | BIND             |
|   مشخص‌نشده | Block           | NO BIND          |
|   مشخص‌نشده | Filesystem      | BIND             |
|   Block       | مشخص‌نشده     | NO BIND          |
|   Block       | Block           | BIND             |
|   Block       | Filesystem      | NO BIND          |
|   Filesystem  | Filesystem      | BIND             |
|   Filesystem  | Block           | NO BIND          |
|   Filesystem  | مشخص‌نشده     | BIND             |

{{< note >}}
در نسخهٔ آلفا تنها حجم‌هایی که به‌صورت ایستا تأمین شده‌اند پشتیبانی می‌شوند. مدیران
باید هنگام کار با دستگاه‌های بلوکی خام این مقادیر را با دقت در نظر بگیرند.
{{< /note >}}

## پشتیبانی از Volume Snapshot و بازیابی حجم از Snapshot

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

Volume snapshotها تنها از پلاگین‌های حجم CSI بیرون‌درختی (out-of-tree) پشتیبانی می‌کنند.
برای جزئیات، [Volume Snapshotها](/docs/concepts/storage/volume-snapshots/) را ببینید.
پلاگین‌های حجم درون‌درختی منسوخ شده‌اند. می‌توانید دربارهٔ پلاگین‌های حجم منسوخ‌شده
در [پرسش‌های متداول پلاگین حجم](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md)
مطالعه کنید.

### ایجاد یک PersistentVolumeClaim از یک Volume Snapshot {#create-persistent-volume-claim-from-volume-snapshot}

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restore-pvc
spec:
  storageClassName: csi-hostpath-sc
  dataSource:
    name: new-snapshot-test
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## شبیه‌سازی حجم (Volume Cloning)

[شبیه‌سازی حجم](/docs/concepts/storage/volume-pvc-datasource/)
تنها برای پلاگین‌های حجم CSI در دسترس است.

### ایجاد PersistentVolumeClaim از یک PVC موجود {#create-persistent-volume-claim-from-an-existing-pvc}

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cloned-pvc
spec:
  storageClassName: my-csi-plugin
  dataSource:
    name: existing-src-pvc-name
    kind: PersistentVolumeClaim
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## Volume populatorها و منابع داده

[شبیه‌سازی حجم](#volume-cloning) و
[بازیابی از snapshot](#volume-snapshot-and-restore-volume-from-snapshot-support) یک حجم جدید را
از یک _منبع داده_ (data source) داخلی از پیش پر می‌کنند. _Volume populatorها_ این سازوکار را گسترش می‌دهند تا
یک PersistentVolumeClaim بتواند از انواع دیگری از منبع (یک منبع سفارشی) از پیش پر شود،
که از طریق فیلد `dataSourceRef` آن ارجاع داده می‌شود:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: populated-pvc
spec:
  dataSourceRef:
    name: example-name
    kind: ExampleDataSource
    apiGroup: example.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

برای جزئیات، از جمله منابع داده میان فضاهای نام، ببینید:
[Volume Populatorها و منابع داده](/docs/concepts/storage/volume-populators-and-data-sources/).

## نوشتن پیکربندی قابل حمل

اگر قالب‌ها یا نمونه‌های پیکربندی می‌نویسید که روی طیف گسترده‌ای از کلاسترها اجرا می‌شوند
و به ذخیره‌سازی پایدار نیاز دارند، توصیه می‌شود از الگوی زیر استفاده کنید:

- آبجکت‌های PersistentVolumeClaim را در بستهٔ پیکربندی خود (در کنار
  Deploymentها، ConfigMapها و غیره) بگنجانید.
- آبجکت‌های PersistentVolume را در پیکربندی نگنجانید، زیرا کاربری که پیکربندی را
  نمونه‌سازی می‌کند ممکن است مجوز ایجاد PersistentVolume نداشته باشد.
- به کاربر این امکان را بدهید که هنگام نمونه‌سازی قالب، نام یک storage class
  ارائه کند.
  - اگر کاربر نام storage class ارائه کند، آن مقدار را در فیلد
    `persistentVolumeClaim.storageClassName` قرار دهید.
    این کار باعث می‌شود اگر مدیر StorageClassها را در کلاستر فعال کرده باشد،
    PVC با storage class درست مطابقت پیدا کند.
  - اگر کاربر نام storage class ارائه نکند، فیلد
    `persistentVolumeClaim.storageClassName` را nil باقی بگذارید. این کار باعث می‌شود
    یک PV به‌طور خودکار با StorageClass پیش‌فرض کلاستر برای کاربر تأمین شود.
    بسیاری از محیط‌های کلاستر یک StorageClass پیش‌فرض نصب‌شده دارند،
    یا مدیران می‌توانند StorageClass پیش‌فرض خود را ایجاد کنند.
- در ابزارهای خود، PVCهایی را که پس از مدتی متصل نمی‌شوند زیر نظر بگیرید
  و این موضوع را به کاربر نشان دهید، زیرا ممکن است نشان دهد که کلاستر
  پشتیبانی از ذخیره‌سازی پویا ندارد (که در این صورت کاربر باید یک PV منطبق ایجاد کند)
  یا کلاستر هیچ سیستم ذخیره‌سازی ندارد (که در این صورت کاربر نمی‌تواند
  پیکربندی‌ای را که به PVC نیاز دارد مستقر کند).

## {{% heading "whatsnext" %}}

* دربارهٔ [ایجاد یک PersistentVolume](/docs/tutorials/configuration/configure-persistent-volume-storage/#create-a-persistentvolume) بیشتر بیاموزید.
* دربارهٔ [ایجاد یک PersistentVolumeClaim](/docs/tutorials/configuration/configure-persistent-volume-storage/#create-a-persistentvolumeclaim) بیشتر بیاموزید.
* [سند طراحی Persistent Storage](https://git.k8s.io/design-proposals-archive/storage/persistent-storage.md) را بخوانید.

### مراجع API {#reference}

دربارهٔ APIهای توصیف‌شده در این صفحه بخوانید:

* [`PersistentVolume`](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)
* [`PersistentVolumeClaim`](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)
