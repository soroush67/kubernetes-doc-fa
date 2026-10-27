---
reviewers:
- gnufied
- jsafrane
- msau42
- xing-yang
title: پایش سلامت حجم
content_type: concept
weight: 100
---

<!-- overview -->

{{< feature-state feature_gate_name="CSIVolumeHealth" >}}

پایش سلامت حجم CSI به یک درایور {{< glossary_tooltip text="CSI" term_id="csi" >}}
امکان می‌دهد مشکلات سلامت یک حجم یا backend ذخیره‌سازی آن را مستقیماً به
کوبرنتیز گزارش دهد. درایور از طریق RPCهای CSI گزارش می‌دهد و کوبرنتیز این گزارش‌ها را در
سه فیلد وضعیت نمایان می‌کند:
`.status.healthStatus` در {{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}}،
`.status.volumeHealth` در {{< glossary_tooltip text="Pod" term_id="pod" >}}
و `.status.storageHealth` در
[CSINode](/docs/reference/kubernetes-api/storage/csi-node-v1/).
ابزارهای خودکارسازی می‌توانند به‌جای بازسازی سلامت حجم از
{{< glossary_tooltip text="رویدادهای (Events)" term_id="event" >}} موقت یا از داشبوردهای
خاص فروشندگان، این فیلدهای وضعیت ماندگار را زیر نظر بگیرند.

{{< note >}}
feature gate `CSIVolumeHealth` از کوبرنتیز v1.21 وجود داشته است، اما
سازوکاری که در این صفحه شرح داده شده یک بازطراحی است که جایگزین پیاده‌سازی
آلفای اولیه می‌شود. برای اینکه چه چیزی تغییر کرده است، [محدودیت‌ها](#limitations) را ببینید.
{{< /note >}}

<!-- body -->

## نحوهٔ کار

مشخصات CSI چهار RPC برای گزارش سلامت تعریف می‌کند:

- روی پلاگین کنترل‌کنندهٔ CSI: `ControllerListVolumeHealth` و
  `ControllerGetVolumeHealth`، برای سلامت هر حجم از دید کنترل‌کننده.
- روی پلاگین نود CSI: `NodeGetVolumeHealth`، برای سلامت هر حجم از دید نود،
  و `NodeGetStorageHealth`، برای سلامت backend ذخیره‌سازی آن‌گونه که
  از آن نود دیده می‌شود.

یک درایور تنها باید RPCهایی را که می‌خواهد پشتیبانی کند پیاده‌سازی کند و پشتیبانی را
از طریق قابلیت‌های پلاگین CSI اعلام می‌کند. درایوری که هیچ‌یک از این RPCها را پیاده‌سازی نکند هرگز
بررسی (probe) نمی‌شود و گزارش‌دهی برای آن درایور غیرفعال باقی می‌ماند. درایوری که
قابلیت `LIST_VOLUME_HEALTH` کنترل‌کننده را اعلام می‌کند باید `GET_VOLUME_HEALTH` را نیز اعلام کند؛
sidecar `csi-external-health-monitor-controller` این الزام را اعمال می‌کند.

هر گزارش سلامت یک `status` دارد که از مجموعه‌ای کوچک و قابل تجزیه توسط ماشین از
مقادیر انتخاب می‌شود، همراه با یک `reason` تعریف‌شده توسط درایور و یک
`message` اختیاری قابل خواندن برای انسان:

- مقادیر وضعیت در سطح حجم (برای `PersistentVolumeClaim.status.healthStatus`
  و `Pod.status.volumeHealth` استفاده می‌شوند): `Inaccessible`، `DataLoss`، `Degraded`.
- مقادیر وضعیت backend ذخیره‌سازی (برای `CSINode.status.storageHealth` استفاده می‌شوند):
  `StorageUnreachable`، `StorageDegraded`.

گزارش‌های سمت نود و سمت کنترل‌کننده مستقل از یکدیگرند: یک حجم ممکن است
از نودی که مسیر داده‌اش به backend را از دست داده است `Inaccessible` باشد، در حالی که
پلاگین کنترل‌کننده همچنان حجم را سالم گزارش می‌کند، و برعکس.

## سلامت گزارش‌شده روی Podها

برای حجم‌هایی که از یک درایور CSI با پشتیبانی از RPC سمت نود `NodeGetVolumeHealth` استفاده می‌کنند،
{{< glossary_tooltip term_id="kubelet" text="kubelet" >}} به‌صورت دوره‌ای آن
RPC را برای هر حجم CSI که برای یک Pod mount کرده است فراخوانی می‌کند و نتیجه را در
`pod.status.volumeHealth` می‌نویسد که با نام حجم از `pod.spec.volumes` کلیدگذاری شده است. بازهٔ
بررسی، تنظیم `volumeStatsAggPeriod` در kubelet (فلگ خط فرمان
`--volume-stats-agg-period`) است.

```yaml
apiVersion: v1
kind: Pod
# ...
status:
  volumeHealth:
  - name: my-volume
    healthConditions:
    - status: Inaccessible
      reason: VolumeNotFound
      message: "volume not found on the storage backend"
    lastTransitionTime: "2026-07-20T12:00:00Z"
```

kubelet تنها در `pods/status` می‌نویسد؛ زیرمنبعی که از پیش مجاز است آن را
برای Podهای متصل به نود خود به‌روزرسانی کند، بنابراین برای این فیلد
هیچ مجوز جدیدی لازم نیست.

## سلامت گزارش‌شده روی CSINode

برای هر درایور CSI ثبت‌شده روی یک نود که از `NodeGetStorageHealth` پشتیبانی می‌کند،
kubelet به‌صورت دوره‌ای آن RPC را فراخوانی می‌کند و نتیجه را در
`csinode.status.storageHealth` می‌نویسد که با نام درایور کلیدگذاری شده است.

```yaml
apiVersion: storage.k8s.io/v1
kind: CSINode
# ...
status:
  storageHealth:
  - name: csi.example.com
    healthConditions:
    - status: StorageUnreachable
      reason: NetworkPartition
      message: "data path to the storage backend is unreachable from this node"
```

یک مدخل `StorageHealthCondition` می‌تواند به‌صورت اختیاری دامنهٔ خود را به یک
`accessMode` یا `volumeMode` مشخص محدود کند، برای backendهایی که به‌صورت نامتقارن دچار افت کیفیت می‌شوند (برای مثال، یک
مشکل شبکه که بر دسترسی `ReadWriteMany` اثر می‌گذارد اما بر `ReadWriteOnce` نه).

نوشتن در `csinodes/status` قابلیت جدیدی است که این قابلیت اضافه می‌کند:
[حالت مجوزدهی Node](/docs/reference/access-authn-authz/node/) و
پلاگین پذیرش NodeRestriction تنها به یک kubelet اجازه می‌دهند آبجکت `CSINode`
منطبق با نود خودش را patch کند، و تنها در حالی که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `CSIVolumeHealth`
فعال باشد.

## سلامت گزارش‌شده روی PersistentVolumeClaimها

سلامت حجم از دید کنترل‌کننده توسط sidecar `csi-external-health-monitor-controller`
که در کنار پلاگین کنترل‌کنندهٔ یک درایور CSI اجرا می‌شود، در `persistentvolumeclaim.status.healthStatus`
نوشته می‌شود. این sidecar `ControllerListVolumeHealth` را فراخوانی می‌کند (یا در صورت نیاز
برای هر حجم به `ControllerGetVolumeHealth` بازمی‌گردد) و نتیجه را می‌نویسد:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
# ...
status:
  healthStatus:
    healthConditions:
    - status: Inaccessible
      reason: VolumeNotFound
      message: "volume not found on the storage backend"
    lastTransitionTime: "2026-07-20T12:00:00Z"
```

هیچ نودی هرگز در این فیلد نمی‌نویسد؛ تنها sidecar که در control plane اجرا می‌شود این کار را انجام می‌دهد.
این کار مانع می‌شود که یک نود آسیب‌دیده یا دارای رفتار نادرست بتواند بر آنچه سایر
کاربران کلاستر روی یک PVC می‌بینند اثر بگذارد.

در دسترس بودن این مسیر برای یک درایور مشخص به این بستگی دارد که آن درایور، و
استقرار sidecar `csi-external-health-monitor-controller` آن،
RPCهای جدید کنترل‌کننده را پذیرفته باشند.

## فعال‌سازی پایش سلامت حجم

پایش سلامت حجم با یک
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) واحد،
`CSIVolumeHealth`، هم روی `kube-apiserver` و هم روی kubelet کنترل می‌شود:

- روی `kube-apiserver`، فعال کردن feature gate امکان نوشتن و خواندن فیلدهای وضعیت جدید
  را فراهم می‌کند؛ غیرفعال کردن آن فیلدها را در نوشتن بعدی روی آبجکت حذف می‌کند،
  در حالی که مقادیر از پیش ذخیره‌شده حفظ می‌شوند.
- روی kubelet، فعال کردن feature gate بررسی دوره‌ای سمت نود را
  که در بالا شرح داده شد آغاز می‌کند.

پایش سمت کنترل‌کننده، که `persistentvolumeclaim.status.healthStatus` را پر می‌کند،
feature gate جداگانه‌ای ندارد. استقرار sidecar `csi-external-health-monitor-controller`
در کنار پلاگین کنترل‌کنندهٔ درایور CSI شما، خود به معنای فعال‌سازی سمت کنترل‌کننده است.

فعال کردن feature gate به‌تنهایی باعث نمایان شدن هیچ اطلاعات سلامتی
نمی‌شود: یک درایور CSI نیز باید RPCهای متناظر را اعلام و پیاده‌سازی کند.
مستندات درایور CSI خود را بررسی کنید تا ببینید از کدام‌یک از این چهار RPC، اگر از هیچ‌کدام،
پشتیبانی می‌کند.

## پایش

kubelet یک متریک gauge با نام `csi_node_storage_health_status` ارائه می‌کند که با
`driver_name`، `status` و `reason` برچسب‌گذاری شده است و برای هر condition مربوط به backend ذخیره‌سازی
که در حال حاضر برای یک درایور روی آن نود گزارش شده است مقدار `1` دارد.

## محدودیت‌ها

- کوبرنتیز تنها این گزارش‌های سلامت را نمایان می‌کند؛ بر اساس آن‌ها اقدامی انجام نمی‌دهد.
  هیچ بخشی از کوبرنتیز به‌خودی‌خود Podها را دوباره زمان‌بندی نمی‌کند، حجم‌ها را جابه‌جا (fail over) نمی‌کند یا به هر شکل دیگری
  به condition گزارش‌شده واکنش نشان نمی‌دهد. ساختن یک کنترل‌کنندهٔ اصلاحی بر پایهٔ
  این فیلدهای وضعیت به اپراتورهای کلاستر و فروشندگان واگذار شده است.
- یک پیاده‌سازی قدیمی‌تر و آلفا از همین feature gate `CSIVolumeHealth` (در دسترس
  از کوبرنتیز v1.21) وضعیت‌های غیرعادی حجم را با استفاده از Eventهای کوبرنتیز
  و متریک `kubelet_volume_stats_health_status_abnormal` گزارش می‌کرد. آن سازوکار
  با فیلدهای وضعیت و RPCهای توصیف‌شده در این صفحه جایگزین شده است و دیگر
  وجود ندارد.

## {{% heading "whatsnext" %}}

- برای طراحی کامل، [KEP-1432](https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/1432-volume-health-monitor)
  را بخوانید.
- برای اینکه بدانید کدام درایورهای CSI پایش سلامت حجم را پیاده‌سازی می‌کنند،
  [مستندات درایورهای CSI](https://kubernetes-csi.github.io/docs/drivers.html) را ببینید.
