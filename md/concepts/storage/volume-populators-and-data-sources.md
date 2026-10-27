---
title: Volume Populatorها و منابع داده
content_type: concept
weight: 71
---

<!-- overview -->

این سند _volume populatorها_ و _منابع داده_ (data sources) را در کوبرنتیز شرح می‌دهد.
آشنایی با [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/)
توصیه می‌شود.

<!-- body -->

هنگامی که یک {{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}} ایجاد می‌کنید،
حجمی که کوبرنتیز برای آن تأمین می‌کند معمولاً خالی آغاز می‌شود. یک _منبع داده_
به شما امکان می‌دهد به‌جای آن درخواست کنید که حجم جدید از پیش با داده‌های موجود پر شود.
_Volume populatorها_ کنترل‌کننده‌هایی هستند که این پر کردن را بر اساس
منبع داده‌ای که PersistentVolumeClaim به آن ارجاع می‌دهد انجام می‌دهند.

کوبرنتیز پشتیبانی داخلی از منابع داده‌ای دارد که
[یک حجم موجود را شبیه‌سازی (clone) می‌کنند](/docs/concepts/storage/volume-pvc-datasource/) یا
[یک volume snapshot را بازیابی می‌کنند](/docs/concepts/storage/volume-snapshots/). volume populatorهای
سفارشی این سازوکار را گسترش می‌دهند. منبع داده یک منبع سفارشی است، یعنی آبجکتی
که نوع آن توسط یک
{{< glossary_tooltip text="CustomResourceDefinition" term_id="CustomResourceDefinition" >}} تعریف شده است.
یک کنترل‌کنندهٔ populator مراقب PersistentVolumeClaimهایی است که به چنین منبعی ارجاع می‌دهند
و حجم جدید را از آن پر می‌کند.

## Volume populatorها و منابع داده

{{< feature-state for_k8s_version="v1.24" state="beta" >}}

کوبرنتیز از volume populatorهای سفارشی پشتیبانی می‌کند.
برای استفاده از volume populatorهای سفارشی، باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) `AnyVolumeDataSource` را برای
kube-apiserver و kube-controller-manager فعال کنید.

Volume populatorها از فیلدی در spec مربوط به PVC به نام `dataSourceRef` بهره می‌برند. برخلاف
فیلد `dataSource` که تنها می‌تواند شامل ارجاعی به یک PersistentVolumeClaim دیگر
یا به یک VolumeSnapshot باشد، فیلد `dataSourceRef` می‌تواند شامل ارجاعی به هر آبجکتی در
همان فضای نام باشد، به‌جز آبجکت‌های هسته (core) غیر از PVCها. برای کلاسترهایی که این feature
gate در آن‌ها فعال است، استفاده از `dataSourceRef` بر `dataSource` ترجیح دارد.

## ارجاع‌های منبع داده

فیلد `dataSourceRef` تقریباً همانند فیلد `dataSource` رفتار می‌کند. اگر یکی
مشخص شود و دیگری نه، API server به هر دو فیلد مقدار یکسانی می‌دهد. هیچ‌یک از
این دو فیلد پس از ایجاد قابل تغییر نیست و تلاش برای مشخص کردن مقادیر متفاوت برای این دو
فیلد به خطای اعتبارسنجی منجر می‌شود. بنابراین این دو فیلد همیشه محتوای
یکسانی خواهند داشت.

دو تفاوت میان فیلد `dataSourceRef` و فیلد `dataSource` وجود دارد که
کاربران باید از آن‌ها آگاه باشند:

* فیلد `dataSource` مقادیر نامعتبر را نادیده می‌گیرد (گویی فیلد خالی است)، در حالی که
  فیلد `dataSourceRef` هرگز مقادیر را نادیده نمی‌گیرد و در صورت استفاده از مقدار نامعتبر
  باعث خطا می‌شود. مقادیر نامعتبر هر آبجکت هسته (آبجکت‌های بدون apiGroup) به‌جز PVCها هستند.
* فیلد `dataSourceRef` می‌تواند شامل انواع مختلفی از آبجکت‌ها باشد، در حالی که فیلد `dataSource`
  تنها PVCها و VolumeSnapshotها را مجاز می‌داند.

هنگامی که قابلیت `CrossNamespaceVolumeDataSource` فعال باشد، تفاوت‌های دیگری نیز وجود دارد:

* فیلد `dataSource` تنها آبجکت‌های محلی را مجاز می‌داند، در حالی که فیلد `dataSourceRef`
  آبجکت‌ها را در هر فضای نامی مجاز می‌داند.
* هنگامی که فضای نام مشخص شود، `dataSource` و `dataSourceRef` همگام‌سازی نمی‌شوند.

کاربران باید در کلاسترهایی که feature gate در آن‌ها فعال است همیشه از `dataSourceRef` استفاده کنند و
در کلاسترهایی که فعال نیست به `dataSource` بازگردند. تحت هیچ شرایطی لازم نیست به هر دو فیلد
نگاه کرد. مقادیر تکراری با معناشناسی اندکی متفاوت تنها برای
سازگاری با نسخه‌های قبلی وجود دارند. به‌ویژه، ترکیبی از کنترل‌کننده‌های قدیمی‌تر و جدیدتر
می‌توانند با یکدیگر همکاری کنند، زیرا فیلدها یکسان هستند.

### استفاده از volume populatorها

Volume populatorها {{< glossary_tooltip text="کنترل‌کننده‌هایی" term_id="controller" >}} هستند که می‌توانند
حجم‌های غیرخالی ایجاد کنند که محتوای آن‌ها توسط یک منبع سفارشی (Custom Resource) تعیین می‌شود.
کاربران با ارجاع به یک منبع سفارشی از طریق فیلد `dataSourceRef` یک حجم پرشده ایجاد می‌کنند:

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

از آنجا که volume populatorها مؤلفه‌هایی خارجی هستند، تلاش برای ایجاد PVCی که از یکی از آن‌ها استفاده می‌کند
ممکن است در صورت نصب نبودن همهٔ مؤلفه‌های درست با شکست مواجه شود. کنترل‌کننده‌های خارجی باید
رویدادهایی روی PVC تولید کنند تا بازخوردی دربارهٔ وضعیت ایجاد ارائه دهند، از جمله هشدارهایی در صورتی که
PVC به دلیل نبود یک مؤلفه قابل ایجاد نباشد.

می‌توانید کنترل‌کنندهٔ آلفای [volume data source validator](https://github.com/kubernetes-csi/volume-data-source-validator)
را در کلاستر خود نصب کنید. این کنترل‌کننده در صورتی که هیچ populatorی
برای مدیریت آن نوع منبع داده ثبت نشده باشد، رویدادهای هشدار روی PVC تولید می‌کند. هنگامی که populator مناسبی برای یک PVC نصب شده باشد،
گزارش رویدادهای مربوط به ایجاد حجم و مشکلات حین این فرایند
بر عهدهٔ همان کنترل‌کنندهٔ populator است.

## منابع داده میان فضاهای نام

{{< feature-state for_k8s_version="v1.26" state="alpha" >}}

کوبرنتیز از منابع داده حجم میان فضاهای نام پشتیبانی می‌کند.
برای استفاده از منابع داده حجم میان فضاهای نام، باید
[feature gateهای](/docs/reference/command-line-tools-reference/feature-gates/) `AnyVolumeDataSource`
و `CrossNamespaceVolumeDataSource` را برای
kube-apiserver و kube-controller-manager فعال کنید.
همچنین باید feature gate `CrossNamespaceVolumeDataSource` را برای csi-provisioner فعال کنید.

فعال کردن feature gate `CrossNamespaceVolumeDataSource` به شما امکان می‌دهد
یک فضای نام را در فیلد dataSourceRef مشخص کنید.

{{< note >}}
هنگامی که برای یک منبع داده حجم فضای نام مشخص می‌کنید، کوبرنتیز پیش از پذیرش ارجاع،
وجود یک ReferenceGrant را در فضای نام دیگر بررسی می‌کند.
ReferenceGrant بخشی از APIهای افزونهٔ `gateway.networking.k8s.io` است.
برای جزئیات، [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/)
را در مستندات Gateway API ببینید.
این بدان معناست که پیش از استفاده از این سازوکار، باید کلاستر کوبرنتیز خود را دست‌کم با ReferenceGrant از
Gateway API گسترش دهید.
{{< /note >}}

### استفاده از یک منبع داده حجم میان فضاهای نام

{{< feature-state for_k8s_version="v1.26" state="alpha" >}}

یک ReferenceGrant ایجاد کنید تا مالک فضای نام بتواند ارجاع را بپذیرد.
یک حجم پرشده را با مشخص کردن یک منبع داده حجم میان فضاهای نام
از طریق فیلد `dataSourceRef` تعریف می‌کنید. باید از پیش یک ReferenceGrant معتبر
در فضای نام مبدأ داشته باشید:

   ```yaml
   apiVersion: gateway.networking.k8s.io/v1beta1
   kind: ReferenceGrant
   metadata:
     name: allow-ns1-pvc
     namespace: default
   spec:
     from:
     - group: ""
       kind: PersistentVolumeClaim
       namespace: ns1
     to:
     - group: snapshot.storage.k8s.io
       kind: VolumeSnapshot
       name: new-snapshot-demo
   ```

   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: foo-pvc
     namespace: ns1
   spec:
     storageClassName: example
     accessModes:
     - ReadWriteOnce
     resources:
       requests:
         storage: 1Gi
     dataSourceRef:
       apiGroup: snapshot.storage.k8s.io
       kind: VolumeSnapshot
       name: new-snapshot-demo
       namespace: default
     volumeMode: Filesystem
   ```

## {{% heading "whatsnext" %}}

* دربارهٔ [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/) بیاموزید.
* دربارهٔ [شبیه‌سازی حجم CSI](/docs/concepts/storage/volume-pvc-datasource/) بیاموزید.
* دربارهٔ [Volume Snapshotها](/docs/concepts/storage/volume-snapshots/) بیاموزید.
* دربارهٔ [feature gateهای](/docs/reference/command-line-tools-reference/feature-gates/)
  ذکرشده در این صفحه بخوانید.
