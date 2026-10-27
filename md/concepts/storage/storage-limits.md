---
reviewers:
- jsafrane
- saad-ali
- thockin
- msau42
title: محدودیت‌های حجم وابسته به نود
content_type: concept
weight: 90
---

<!-- overview -->

این صفحه بیشینهٔ تعداد حجم‌هایی را که می‌توان برای ارائه‌دهندگان ابری مختلف
به یک نود متصل (attach) کرد شرح می‌دهد.

ارائه‌دهندگان ابری مانند Google، Amazon و Microsoft معمولاً محدودیتی بر
تعداد حجم‌هایی که می‌توان به یک نود متصل کرد دارند. برای کوبرنتیز مهم است که
این محدودیت‌ها را رعایت کند. در غیر این صورت، Podهایی که روی یک نود زمان‌بندی شده‌اند ممکن است
در انتظار اتصال حجم‌ها گیر کنند.



<!-- body -->

## محدودیت‌های پیش‌فرض کوبرنتیز

زمان‌بند کوبرنتیز محدودیت‌های پیش‌فرضی بر تعداد حجم‌هایی
که می‌توان به یک نود متصل کرد دارد:

<table>
  <tr><th>سرویس ابری</th><th>بیشینهٔ حجم‌ها به ازای هر نود</th></tr>
  <tr><td><a href="https://aws.amazon.com/ebs/">Amazon Elastic Block Store (EBS)</a></td><td>39</td></tr>
  <tr><td><a href="https://cloud.google.com/persistent-disk/">Google Persistent Disk</a></td><td>16</td></tr>
  <tr><td><a href="https://azure.microsoft.com/en-us/services/storage/main-disks/">Microsoft Azure Disk Storage</a></td><td>16</td></tr>
</table>

## محدودیت‌های پویای حجم

{{< feature-state state="stable" for_k8s_version="v1.17" >}}

محدودیت‌های پویای حجم برای انواع حجم زیر پشتیبانی می‌شوند.

- Amazon EBS
- Google Persistent Disk
- Azure Disk
- CSI

برای حجم‌هایی که توسط پلاگین‌های حجم درون‌درختی مدیریت می‌شوند، کوبرنتیز به‌طور خودکار نوع
نود را تشخیص می‌دهد و بیشینهٔ مناسب تعداد حجم‌ها را برای آن نود اعمال می‌کند. برای مثال:

* در
<a href="https://cloud.google.com/compute/">Google Compute Engine</a>،
[بسته به نوع
نود](https://cloud.google.com/compute/docs/disks/#pdnumberlimits) حداکثر ۱۲۷ حجم را می‌توان به یک نود متصل کرد.

* برای دیسک‌های Amazon EBS روی انواع نمونهٔ M5، C5، R5، T3 و Z1D، کوبرنتیز تنها اجازهٔ اتصال ۲۵
حجم به یک نود را می‌دهد. برای سایر انواع نمونه در
<a href="https://aws.amazon.com/ec2/">Amazon Elastic Compute Cloud (EC2)</a>،
کوبرنتیز اجازهٔ اتصال ۳۹ حجم به یک نود را می‌دهد.

* در Azure، بسته به نوع نود، حداکثر ۶۴ دیسک را می‌توان به یک نود متصل کرد. برای جزئیات بیشتر، به [اندازه‌های ماشین‌های مجازی در Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes) مراجعه کنید.

* اگر یک درایور ذخیره‌سازی CSI بیشینهٔ تعداد حجم‌ها را برای یک نود اعلام کند (با استفاده از `NodeGetInfo`)، {{< glossary_tooltip text="kube-scheduler" term_id="kube-scheduler" >}} آن محدودیت را رعایت می‌کند.
برای جزئیات به [مشخصات CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md#nodegetinfo) مراجعه کنید.

* برای حجم‌هایی که توسط پلاگین‌های درون‌درختیِ مهاجرت‌داده‌شده به یک درایور CSI مدیریت می‌شوند، بیشینهٔ تعداد حجم‌ها همان مقداری است که درایور CSI گزارش می‌کند.

### شمار قابل تخصیص تغییرپذیر نود CSI

{{< feature-state feature_gate_name="MutableCSINodeAllocatableCount" >}}

درایورهای CSI می‌توانند بیشینهٔ تعداد حجم‌هایی را که می‌توان به یک نود متصل کرد در زمان اجرا به‌صورت پویا تنظیم کنند. این کار دقت زمان‌بندی را افزایش می‌دهد و شکست‌های زمان‌بندی pod ناشی از تغییر در دسترس‌پذیری منابع را کاهش می‌دهد.

برای استفاده از این قابلیت، باید feature gate `MutableCSINodeAllocatableCount` را روی مؤلفه‌های زیر فعال کنید:

- `kube-apiserver`
- `kubelet`

#### به‌روزرسانی‌های دوره‌ای

هنگامی که این قابلیت فعال باشد، درایورهای CSI می‌توانند با تنظیم فیلد `nodeAllocatableUpdatePeriodSeconds` در مشخصات `CSIDriver`، به‌روزرسانی‌های دوره‌ای محدودیت‌های حجم خود را درخواست کنند. برای مثال:

```yaml
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: hostpath.csi.k8s.io
spec:
  nodeAllocatableUpdatePeriodSeconds: 60
```

Kubelet به‌صورت دوره‌ای و با بازهٔ مشخص‌شده در `nodeAllocatableUpdatePeriodSeconds`، endpoint `NodeGetInfo` درایور CSI متناظر را فراخوانی می‌کند تا بیشینهٔ تعداد حجم‌های قابل اتصال را تازه‌سازی کند. کمترین مقدار مجاز برای این فیلد ۱۰ ثانیه است.

اگر یک عملیات اتصال حجم با خطای `ResourceExhausted` (کد gRPC 8) شکست بخورد، کوبرنتیز بی‌درنگ شمار حجم‌های قابل تخصیص آن نود را به‌روزرسانی می‌کند. افزون بر این، kubelet podهای متأثر را به‌عنوان Failed علامت‌گذاری می‌کند تا کنترل‌کننده‌های آن‌ها بتوانند ایجاد مجدد را مدیریت کنند. این کار از گیر کردن نامحدود podها در وضعیت `ContainerCreating` جلوگیری می‌کند.

### جلوگیری از قرارگیری Pod در نبود درایور CSI

{{< feature-state feature_gate_name="VolumeLimitScaling" >}}

[feature gate](/docs/reference/command-line-tools-reference/feature-gates#VolumeLimitScaling)
`VolumeLimitScaling` در کوبرنتیز v1.37 به‌طور پیش‌فرض فعال است.

با این حال، جلوگیری از قرارگیری pod روی نودهای بدون درایور CSI نیازمند فعال‌سازی صریح
از طریق فیلد `spec.preventPodSchedulingIfMissing` در آبجکت `CSIDriver` است.

مقدار پیش‌فرض فیلد `preventPodSchedulingIfMissing` برابر `false` است و اگر
نمی‌خواهید podها روی نودهای بدون درایور CSI زمان‌بندی شوند، باید آن را روی `true` تنظیم کنید. این تصمیم
برای پیش‌فرض بودن `false` به دلایل سازگاری با نسخه‌های قبلی و سازگاری
با [Cluster AutoScaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)
گرفته شده است، که ممکن است در مرحلهٔ مقیاس‌دهی خودکار از محدودیت‌های حجم CSI
آگاه نباشد (بخش زیر را ببینید).

```yaml
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: hostpath.csi.k8s.io
spec:
  preventPodSchedulingIfMissing: true
```


### محدودیت‌های اتصال حجم CSI و cluster autoscaler

[Cluster autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) زمانی می‌تواند محدودیت‌های حجم CSI
را در نظر بگیرد که
`--enable-csi-node-aware-scheduling=true` تنظیم شده باشد. این گزینه مستقل از
feature gate `VolumeLimitScaling` است.

اگر از cluster autoscaler استفاده می‌کنید، `spec.preventPodSchedulingIfMissing` را تنها زمانی روی
`true` تنظیم کنید که cluster autoscaler با
`--enable-csi-node-aware-scheduling=true` پیکربندی شده باشد. در غیر این صورت، شبیه‌سازی‌های زمان‌بندی آن
اطلاعات `CSINode` لازم برای نودهای جدید را شامل نمی‌شوند و cluster
autoscaler ممکن است برای Podهای در انتظاری که از حجم‌های CSI استفاده می‌کنند، در افزایش مقیاس شکست بخورد.
