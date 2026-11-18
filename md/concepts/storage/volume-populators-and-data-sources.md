---
title: پرکننده‌های حجم و منابع داده
content_type: concept
weight: 71
---

<!-- overview -->

این سند _پرکننده‌های حجم_ (volume populators) و _منابع داده_ (data sources) را در کوبرنتیز شرح می‌دهد.
پیشنهاد می‌شود پیش از مطالعهٔ آن با [حجم‌های پایدار](/docs/concepts/storage/persistent-volumes/) آشنا باشید.

<!-- body -->

وقتی یک {{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}} ایجاد می‌کنید،
حجمی که کوبرنتیز برای آن فراهم می‌کند معمولاً در ابتدا خالی است. با یک _منبع داده_ می‌توانید
درخواست کنید که حجم جدید از پیش با داده‌های موجود پر شود. _پرکننده‌های حجم_ کنترل‌کننده‌هایی هستند
که این پرکردن را بر اساس منبع داده‌ای که PersistentVolumeClaim به آن ارجاع می‌دهد انجام می‌دهند.

کوبرنتیز به‌صورت داخلی از منابع داده‌ای پشتیبانی می‌کند که
[یک حجم موجود را شبیه‌سازی (clone) می‌کنند](/docs/concepts/storage/volume-pvc-datasource/) یا
[یک اسنپ‌شات حجم را بازیابی می‌کنند](/docs/concepts/storage/volume-snapshots/). پرکننده‌های حجم سفارشی
این سازوکار را گسترش می‌دهند. در این حالت، منبع داده یک منبع سفارشی است؛ یعنی آبجکتی که نوع آن با یک
{{< glossary_tooltip text="CustomResourceDefinition" term_id="CustomResourceDefinition" >}}
تعریف شده است. هر کنترل‌کنندهٔ پرکننده، PersistentVolumeClaimهایی را که به چنین منبعی ارجاع می‌دهند
زیر نظر می‌گیرد و حجم جدید را از روی آن پر می‌کند.

## پرکننده‌های حجم و منابع داده

{{< feature-state for_k8s_version="v1.24" state="beta" >}}

کوبرنتیز از پرکننده‌های حجم سفارشی پشتیبانی می‌کند.
برای استفاده از پرکننده‌های حجم سفارشی، باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `AnyVolumeDataSource` را برای
kube-apiserver و kube-controller-manager فعال کنید.

پرکننده‌های حجم از فیلدی در مشخصات PVC به نام `dataSourceRef` بهره می‌برند. فیلد `dataSource`
فقط می‌تواند ارجاعی به یک PersistentVolumeClaim دیگر یا به یک VolumeSnapshot داشته باشد؛ اما
فیلد `dataSourceRef` می‌تواند به هر آبجکتی در همان فضای نام (namespace) ارجاع دهد، به‌جز آبجکت‌های
هسته‌ای غیر از PVC. در کلاسترهایی که این feature gate در آن‌ها فعال است، استفاده از `dataSourceRef`
بر `dataSource` ترجیح دارد.

## ارجاع‌های منبع داده

رفتار فیلد `dataSourceRef` تقریباً همانند فیلد `dataSource` است. اگر یکی از این دو مشخص شود و
دیگری مشخص نشود، API server به هر دو فیلد مقدار یکسانی می‌دهد. هیچ‌یک از این دو فیلد پس از ایجاد
قابل تغییر نیست و تلاش برای تعیین مقادیر متفاوت برای آن‌ها به خطای اعتبارسنجی می‌انجامد. بنابراین
محتوای این دو فیلد همیشه یکسان خواهد بود.

دو تفاوت میان فیلد `dataSourceRef` و فیلد `dataSource` وجود دارد که کاربران باید از آن‌ها آگاه باشند:

* فیلد `dataSource` مقادیر نامعتبر را نادیده می‌گیرد (گویی فیلد خالی است)، درحالی‌که فیلد
  `dataSourceRef` هرگز مقادیر را نادیده نمی‌گیرد و در صورت استفاده از مقدار نامعتبر خطا ایجاد می‌کند.
  مقادیر نامعتبر شامل هر آبجکت هسته‌ای (آبجکت‌هایی که apiGroup ندارند) به‌جز PVCها است.
* فیلد `dataSourceRef` می‌تواند انواع مختلفی از آبجکت‌ها را در بر بگیرد، درحالی‌که فیلد `dataSource`
  فقط PVCها و VolumeSnapshotها را مجاز می‌داند.

هنگامی که قابلیت `CrossNamespaceVolumeDataSource` فعال باشد، تفاوت‌های دیگری نیز وجود دارد:

* فیلد `dataSource` فقط آبجکت‌های محلی را مجاز می‌داند، درحالی‌که فیلد `dataSourceRef`
  آبجکت‌های هر فضای نامی را می‌پذیرد.
* هنگامی که فضای نام مشخص شده باشد، `dataSource` و `dataSourceRef` با یکدیگر همگام نمی‌شوند.

کاربران باید در کلاسترهایی که این feature gate در آن‌ها فعال است همیشه از `dataSourceRef` استفاده کنند
و در کلاسترهایی که فعال نیست به `dataSource` بازگردند. در هیچ شرایطی لازم نیست هر دو فیلد بررسی شوند.
این مقادیر تکراری با معناشناسی اندکی متفاوت، صرفاً برای سازگاری با نسخه‌های پیشین وجود دارند. به‌ویژه،
چون این فیلدها یکسان هستند، ترکیبی از کنترل‌کننده‌های قدیمی‌تر و جدیدتر می‌توانند با یکدیگر همکاری کنند.

### استفاده از پرکننده‌های حجم

پرکننده‌های حجم {{< glossary_tooltip text="کنترل‌کننده‌هایی" term_id="controller" >}} هستند که می‌توانند
حجم‌های غیرخالی ایجاد کنند؛ حجم‌هایی که محتوای آن‌ها را یک منبع سفارشی (Custom Resource) تعیین می‌کند.
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

از آنجا که پرکننده‌های حجم مؤلفه‌هایی خارجی هستند، اگر همهٔ مؤلفه‌های لازم به‌درستی نصب نشده باشند،
تلاش برای ایجاد PVCای که از آن‌ها استفاده می‌کند ممکن است ناموفق شود. کنترل‌کننده‌های خارجی باید
رویدادهایی روی PVC تولید کنند تا دربارهٔ وضعیت ایجاد بازخورد بدهند؛ از جمله هشدارهایی در صورتی که
PVC به دلیل نبودِ یک مؤلفه قابل ایجاد نباشد.

می‌توانید کنترل‌کنندهٔ آلفای [اعتبارسنج منبع دادهٔ حجم](https://github.com/kubernetes-csi/volume-data-source-validator)
را در کلاستر خود نصب کنید. این کنترل‌کننده در صورتی که هیچ پرکننده‌ای برای رسیدگی به آن نوع منبع داده
ثبت نشده باشد، رویدادهای هشدار (Event) روی PVC تولید می‌کند. هنگامی که پرکنندهٔ مناسبی برای یک PVC
نصب شده باشد، گزارش رویدادهای مربوط به ایجاد حجم و مشکلات پیش‌آمده در طول این فرایند بر عهدهٔ
همان کنترل‌کنندهٔ پرکننده است.

## منابع داده میان فضاهای نام

{{< feature-state for_k8s_version="v1.26" state="alpha" >}}

کوبرنتیز از منابع دادهٔ حجم میان فضاهای نام پشتیبانی می‌کند.
برای استفاده از منابع دادهٔ حجم میان فضاهای نام، باید
[feature gateهای](/docs/reference/command-line-tools-reference/feature-gates/) `AnyVolumeDataSource`
و `CrossNamespaceVolumeDataSource` را برای kube-apiserver و kube-controller-manager فعال کنید.
همچنین باید feature gate با نام `CrossNamespaceVolumeDataSource` را برای csi-provisioner فعال کنید.

با فعال‌کردن feature gate با نام `CrossNamespaceVolumeDataSource` می‌توانید
یک فضای نام را در فیلد dataSourceRef مشخص کنید.

{{< note >}}
وقتی برای یک منبع دادهٔ حجم فضای نام تعیین می‌کنید، کوبرنتیز پیش از پذیرش ارجاع، وجود یک
ReferenceGrant را در فضای نام دیگر بررسی می‌کند.
ReferenceGrant بخشی از APIهای افزونهٔ `gateway.networking.k8s.io` است.
برای جزئیات بیشتر، [ReferenceGrant](https://gateway-api.sigs.k8s.io/reference/api-types/referencegrant/)
را در مستندات Gateway API ببینید.
این یعنی پیش از آنکه بتوانید از این سازوکار استفاده کنید، باید کلاستر کوبرنتیز خود را دست‌کم با
ReferenceGrant از Gateway API گسترش دهید.
{{< /note >}}

### استفاده از منبع دادهٔ حجم میان فضاهای نام

{{< feature-state for_k8s_version="v1.26" state="alpha" >}}

یک ReferenceGrant ایجاد کنید تا مالک فضای نام بتواند ارجاع را بپذیرد.
یک حجم پرشده را با مشخص‌کردن یک منبع دادهٔ حجم میان فضاهای نام از طریق فیلد `dataSourceRef`
تعریف می‌کنید. باید از قبل یک ReferenceGrant معتبر در فضای نام مبدأ داشته باشید:

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
* دربارهٔ [اسنپ‌شات‌های حجم](/docs/concepts/storage/volume-snapshots/) بیاموزید.
* دربارهٔ [feature gateهایی](/docs/reference/command-line-tools-reference/feature-gates/)
  که در این صفحه به آن‌ها اشاره شد مطالعه کنید.
