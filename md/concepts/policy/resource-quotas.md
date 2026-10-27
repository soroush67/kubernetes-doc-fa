---
reviewers:
- derekwaynecarr
title: سهمیه‌های منابع
api_metadata:
- apiVersion: "v1"
  kind: "ResourceQuota"
content_type: concept
weight: 20
---

<!-- overview -->

هنگامی که چند کاربر یا تیم یک کلاستر با تعداد ثابتی از نودها را به اشتراک می‌گذارند،
این نگرانی وجود دارد که یک تیم بیش از سهم منصفانهٔ خود از منابع استفاده کند.

_سهمیه‌های منابع_ (resource quotas) ابزاری برای مدیران هستند تا به این نگرانی رسیدگی کنند.

یک سهمیهٔ منبع که با یک آبجکت ResourceQuota تعریف می‌شود، محدودیت‌هایی فراهم می‌کند که
مصرف تجمیعی منابع را برای هر {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} محدود می‌کنند. یک ResourceQuota همچنین می‌تواند
[تعداد آبجکت‌هایی را که می‌توان در یک فضای نام ایجاد کرد](#quota-on-object-count) بر اساس kind در API، و نیز مقدار کل
{{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}} را که آبجکت‌های API موجود در آن فضای نام
ممکن است مصرف کنند، محدود کند.

{{< caution >}}
نه رقابت بر سر منابع و نه تغییرات سهمیه بر منابعی که از قبل ایجاد شده‌اند تأثیر نخواهند گذاشت.
{{< /caution >}}

<!-- body -->

## ResourceQuotaهای کوبرنتیز چگونه کار می‌کنند

ResourceQuotaها به این صورت کار می‌کنند:

- تیم‌های مختلف در فضاهای نام مختلف کار می‌کنند. این تفکیک را می‌توان با
  [RBAC](/docs/reference/access-authn-authz/rbac/) یا هر سازوکار [مجوزدهی](/docs/reference/access-authn-authz/authorization/)
  دیگری الزامی کرد.

- مدیر کلاستر برای هر فضای نام دست‌کم یک ResourceQuota ایجاد می‌کند.
  - برای اطمینان از اینکه این الزام پابرجا می‌ماند، مدیر کلاستر باید دسترسی برای حذف یا به‌روزرسانی
    آن ResourceQuota را نیز محدود کند؛ برای مثال، با تعریف یک [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/).

- کاربران منابعی (پادها، سرویس‌ها و غیره) را در فضای نام ایجاد می‌کنند و سیستم سهمیه
  مصرف را دنبال می‌کند تا اطمینان حاصل کند از محدودیت‌های سخت منابع تعریف‌شده در ResourceQuota فراتر نمی‌رود.

  می‌توانید یک [محدوده (scope)](#quota-scopes) را بر ResourceQuota اعمال کنید تا مشخص کنید کجا اعمال شود،

- اگر ایجاد یا به‌روزرسانی یک منبع یکی از محدودیت‌های سهمیه را نقض کند، control plane آن درخواست را با کد وضعیت HTTP
  `403 Forbidden` رد می‌کند. خطا شامل پیامی است که محدودیتی را که نقض می‌شد توضیح می‌دهد.

- اگر سهمیه‌ها در یک فضای نام برای {{< glossary_tooltip text="منبعی" term_id="infrastructure-resource" >}}
  مانند `cpu` و `memory` فعال باشند، کاربران هنگام تعریف یک Pod باید requestها یا limitهایی برای آن مقادیر مشخص کنند؛ در غیر این صورت،
  سیستم سهمیه ممکن است ایجاد پاد را رد کند.

  [راهنمای گام‌به‌گام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/) سهمیهٔ منابع
  نمونه‌ای از نحوهٔ اجتناب از این مشکل را نشان می‌دهد.

{{< note >}}
* می‌توانید یک [LimitRange](/docs/concepts/policy/limit-range/) تعریف کنید
  تا مقادیر پیش‌فرض را بر پادهایی که هیچ الزام منبع محاسباتی ندارند تحمیل کند (تا کاربران مجبور نباشند انجام این کار را به خاطر بسپارند).
{{< /note >}}

اغلب پادها را مستقیماً ایجاد نمی‌کنید؛ برای مثال، معمولاً یک آبجکت [مدیریت بار کاری](/docs/concepts/workloads/controllers/)
مانند یک {{< glossary_tooltip term_id="deployment" >}} ایجاد می‌کنید. اگر Deploymentای ایجاد کنید که تلاش می‌کند بیش از
منابع موجود استفاده کند، ایجاد Deployment (یا سایر آبجکت‌های مدیریت بار کاری) **موفق می‌شود**، اما
ممکن است Deployment نتواند همهٔ پادهایی را که مدیریت می‌کند ایجاد کند. در این حالت می‌توانید وضعیت
Deployment را، برای مثال با `kubectl describe`، بررسی کنید تا ببینید چه اتفاقی افتاده است.

- برای منابع `cpu` و `memory`، ResourceQuotaها الزام می‌کنند که **هر**
  پاد (جدید) در آن فضای نام یک limit برای آن منبع تنظیم کند.
  اگر سهمیهٔ منبعی را در یک فضای نام برای `cpu` یا `memory` الزامی کنید،
  شما و سایر کلاینت‌ها **باید** برای هر Pod جدیدی که ارسال می‌کنید، `requests` یا `limits` را برای آن منبع
  مشخص کنید. اگر چنین نکنید، control plane ممکن است پذیرش
  آن Pod را رد کند.
- برای سایر منابع: ResourceQuota کار می‌کند و پادهایی را در فضای نام که
  limit یا request برای آن منبع تنظیم نکرده‌اند نادیده می‌گیرد. این بدان معناست که می‌توانید یک پاد جدید
  بدون limit/request برای ذخیره‌سازی موقت ایجاد کنید، حتی اگر سهمیهٔ منبع، ذخیره‌سازی موقت
  این فضای نام را محدود کرده باشد.

می‌توانید از یک [LimitRange](/docs/concepts/policy/limit-range/) برای تنظیم خودکار
یک request پیش‌فرض برای این منابع استفاده کنید.

نام یک آبجکت ResourceQuota باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

نمونه‌هایی از سیاست‌هایی که می‌توان با استفاده از فضاهای نام و سهمیه‌ها ایجاد کرد عبارت‌اند از:

- در یک کلاستر با ظرفیت 32 GiB RAM و ۱۶ هسته، به تیم A اجازه دهید از 20 GiB و ۱۰ هسته استفاده کند،
  به تیم B اجازه دهید از 10GiB و ۴ هسته استفاده کند، و 2GiB و ۲ هسته را برای تخصیص‌های آینده ذخیره نگه دارید.
- فضای نام «testing» را به استفاده از ۱ هسته و 1GiB RAM محدود کنید. اجازه دهید فضای نام «production»
  هر مقداری را استفاده کند.

در حالتی که ظرفیت کل کلاستر کمتر از مجموع سهمیه‌های فضاهای نام باشد،
ممکن است رقابت بر سر منابع رخ دهد. این وضعیت بر اساس اصل «اولویت با کسی است که زودتر بیاید» مدیریت می‌شود.


## فعال‌سازی سهمیهٔ منابع

پشتیبانی از ResourceQuota در بسیاری از توزیع‌های کوبرنتیز به‌طور پیش‌فرض فعال است. این پشتیبانی
زمانی فعال است که پرچم `--enable-admission-plugins=` در {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
`ResourceQuota` را به‌عنوان
یکی از آرگومان‌های خود داشته باشد.

یک سهمیهٔ منبع زمانی در یک فضای نام مشخص الزامی می‌شود که یک
ResourceQuota در آن فضای نام وجود داشته باشد.

## انواع سهمیهٔ منابع

سازوکار ResourceQuota به شما اجازه می‌دهد انواع مختلفی از محدودیت‌ها را الزامی کنید. این
بخش انواع محدودیتی را که می‌توانید الزامی کنید شرح می‌دهد.

### سهمیه برای منابع زیرساختی {#compute-resource-quota}

می‌توانید مجموع کل
[منابع محاسباتی](/docs/concepts/configuration/manage-resources-containers/)
را که می‌توان در یک فضای نام مشخص درخواست کرد محدود کنید.

انواع منبع زیر پشتیبانی می‌شوند:

| نام منبع | توضیح |
| ------------- | ----------- |
| `limits.cpu` | در میان همهٔ پادهایی که در وضعیت پایانی نیستند، مجموع limitهای CPU نمی‌تواند از این مقدار بیشتر شود. |
| `limits.memory` | در میان همهٔ پادهایی که در وضعیت پایانی نیستند، مجموع limitهای حافظه نمی‌تواند از این مقدار بیشتر شود. |
| `requests.cpu` | در میان همهٔ پادهایی که در وضعیت پایانی نیستند، مجموع requestهای CPU نمی‌تواند از این مقدار بیشتر شود. |
| `requests.memory` | در میان همهٔ پادهایی که در وضعیت پایانی نیستند، مجموع requestهای حافظه نمی‌تواند از این مقدار بیشتر شود. |
| `hugepages-<size>` | در میان همهٔ پادهایی که در وضعیت پایانی نیستند، تعداد requestهای huge page با اندازهٔ مشخص‌شده نمی‌تواند از این مقدار بیشتر شود. |
| `cpu` | همانند `requests.cpu` |
| `memory` | همانند `requests.memory` |

### سهمیه برای منابع توسعه‌یافته

علاوه بر منابع ذکرشده در بالا، در نسخهٔ 1.10، پشتیبانی سهمیه برای
[منابع توسعه‌یافته](/docs/concepts/configuration/manage-resources-containers/#extended-resources) اضافه شده است.

از آنجا که تخصیص بیش از ظرفیت (overcommit) برای منابع توسعه‌یافته مجاز نیست، مشخص‌کردن هم‌زمان `requests`
و `limits` برای یک منبع توسعه‌یافتهٔ یکسان در یک سهمیه معنایی ندارد. بنابراین برای منابع توسعه‌یافته، فقط اقلام سهمیه
با پیشوند `requests.` مجاز هستند.

منبع GPU را به‌عنوان مثال در نظر بگیرید؛ اگر نام منبع `nvidia.com/gpu` باشد و بخواهید
تعداد کل GPUهای درخواست‌شده در یک فضای نام را به ۴ محدود کنید، می‌توانید سهمیه‌ای به شکل زیر تعریف کنید:

* `requests.nvidia.com/gpu: 4`

برای جزئیات بیشتر به [مشاهده و تنظیم سهمیه‌ها](#viewing-and-setting-quotas) مراجعه کنید.

### سهمیه برای resource claimهای DRA

resource claimهای DRA (تخصیص پویای منابع) می‌توانند منابع DRA را بر اساس device class درخواست کنند. برای یک
device class نمونه با نام `examplegpu`، اگر بخواهید تعداد کل GPUهای درخواست‌شده در یک فضای نام را به ۴ محدود کنید،
می‌توانید سهمیه‌ای به شکل زیر تعریف کنید:

* `examplegpu.deviceclass.resource.k8s.io/devices: 4`

هنگامی که [تخصیص منابع توسعه‌یافته توسط DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#extended-resource)
فعال باشد، همان device class با نام `examplegpu` را می‌توان از طریق منبع توسعه‌یافته درخواست کرد؛ یا به‌صورت صریح،
زمانی که فیلد ExtendedResourceName در device class مقداری مانند `example.com/gpu` داشته باشد، که در این صورت می‌توانید سهمیه‌ای به شکل زیر تعریف کنید:

* `requests.example.com/gpu: 4`

یا به‌صورت ضمنی با استفاده از نام منبع توسعه‌یافتهٔ مشتق‌شده از نام device class ‏`examplegpu`، که در این صورت می‌توانید
سهمیه‌ای به شکل زیر تعریف کنید:

* `requests.deviceclass.resource.kubernetes.io/examplegpu: 4`

همهٔ دستگاه‌هایی که از طریق resource claimها یا منابع توسعه‌یافته درخواست می‌شوند، در هر سه سهمیهٔ
فهرست‌شده در بالا محاسبه می‌شوند. سهمیهٔ منبع توسعه‌یافته، برای مثال `requests.example.com/gpu: 4`، دستگاه‌هایی را که
افزونهٔ دستگاه فراهم می‌کند نیز محاسبه می‌کند.

برای جزئیات بیشتر به [مشاهده و تنظیم سهمیه‌ها](#viewing-and-setting-quotas) مراجعه کنید.

### سهمیه برای ذخیره‌سازی

می‌توانید مجموع کل [ذخیره‌سازی](/docs/concepts/storage/persistent-volumes/) حجم‌هایی را
که می‌توان در یک فضای نام مشخص درخواست کرد محدود کنید.

علاوه بر این، می‌توانید مصرف منابع ذخیره‌سازی را بر اساس
[StorageClass](/docs/concepts/storage/storage-classes/) مرتبط محدود کنید.

| نام منبع | توضیح |
| ------------- | ----------- |
| `requests.storage` | در میان همهٔ persistent volume claimها، مجموع requestهای ذخیره‌سازی نمی‌تواند از این مقدار بیشتر شود. |
| `persistentvolumeclaims` | تعداد کل [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) که می‌توانند در فضای نام وجود داشته باشند. |
| `<storage-class-name>.storageclass.storage.k8s.io/requests.storage` | در میان همهٔ persistent volume claimهای مرتبط با `<storage-class-name>`، مجموع requestهای ذخیره‌سازی نمی‌تواند از این مقدار بیشتر شود. |
| `<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` | در میان همهٔ persistent volume claimهای مرتبط با `<storage-class-name>`، تعداد کل [persistent volume claimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) که می‌توانند در فضای نام وجود داشته باشند. |

برای مثال، اگر بخواهید ذخیره‌سازی با StorageClass ‏`gold` را جدا از
StorageClass ‏`bronze` سهمیه‌بندی کنید، می‌توانید سهمیه‌ای به شکل زیر تعریف کنید:

* `gold.storageclass.storage.k8s.io/requests.storage: 500Gi`
* `bronze.storageclass.storage.k8s.io/requests.storage: 100Gi`

#### سهمیه برای ذخیره‌سازی موقت محلی

{{< feature-state for_k8s_version="v1.8" state="alpha" >}}


| نام منبع | توضیح |
| ------------- | ----------- |
| `requests.ephemeral-storage` | در میان همهٔ پادهای فضای نام، مجموع requestهای ذخیره‌سازی موقت محلی نمی‌تواند از این مقدار بیشتر شود. |
| `limits.ephemeral-storage` | در میان همهٔ پادهای فضای نام، مجموع limitهای ذخیره‌سازی موقت محلی نمی‌تواند از این مقدار بیشتر شود. |
| `ephemeral-storage` | همانند `requests.ephemeral-storage`. |

{{< note >}}
هنگام استفاده از یک محیط اجرای کانتینر CRI، لاگ‌های کانتینر در سهمیهٔ ذخیره‌سازی موقت محاسبه می‌شوند.
این امر می‌تواند به بیرون‌راندن غیرمنتظرهٔ پادهایی منجر شود که سهمیهٔ ذخیره‌سازی خود را تمام کرده‌اند.

برای جزئیات به [معماری لاگ‌گیری](/docs/concepts/cluster-administration/logging/) مراجعه کنید.
{{< /note >}}

### سهمیه بر تعداد آبجکت‌ها {#quota-on-object-count}

می‌توانید با استفاده از نحو زیر، برای *تعداد کل یک kind مشخص از {{< glossary_tooltip text="منبع" term_id="api-resource" >}}* در API کوبرنتیز سهمیه تعیین کنید:

* `count/<resource>.<group>` برای منابع گروه‌های API غیرهسته
* `count/<resource>` برای منابع گروه API هسته

برای مثال، API ‏PodTemplate در گروه API هسته قرار دارد؛ بنابراین اگر بخواهید تعداد
آبجکت‌های PodTemplate را در یک فضای نام محدود کنید، از `count/podtemplates` استفاده می‌کنید.

این انواع سهمیه برای محافظت در برابر اتمام فضای ذخیره‌سازی control plane مفید هستند. برای مثال، ممکن است
بخواهید با توجه به حجم زیاد Secretها، تعداد آن‌ها را در یک سرور محدود کنید. وجود تعداد بیش از حد Secret در یک کلاستر
در واقع می‌تواند از راه‌اندازی سرورها و کنترل‌کننده‌ها جلوگیری کند. می‌توانید برای Jobها سهمیه تعیین کنید تا در برابر
یک CronJob با پیکربندی نادرست محافظت شوید. CronJobهایی که تعداد بیش از حدی Job در یک فضای نام ایجاد می‌کنند، می‌توانند به منع سرویس (denial of service) منجر شوند.



اگر سهمیه‌ای را به این روش تعریف کنید، بر APIهای کوبرنتیز که بخشی از سرور API هستند و
بر هر منبع سفارشی مبتنی بر CustomResourceDefinition اعمال می‌شود.
برای مثال، برای ایجاد سهمیه بر منبع سفارشی `widgets` در گروه API ‏`example.com`،
از `count/widgets.example.com` استفاده کنید.
اگر از [تجمیع API](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) برای
افزودن APIهای سفارشی بیشتری استفاده کنید که به‌صورت CustomResourceDefinition تعریف نشده‌اند، control plane اصلی کوبرنتیز
سهمیه را برای API تجمیع‌شده الزامی نمی‌کند. انتظار می‌رود سرور API افزونه،
در صورتی که برای API سفارشی مناسب باشد، الزام سهمیه را فراهم کند.

##### نحو عمومی {#resource-quota-object-count-generic}

این فهرستی از نمونه‌های رایج انواع آبجکتی است که ممکن است بخواهید تحت سهمیهٔ تعداد آبجکت قرار دهید،
که بر اساس رشتهٔ پیکربندی مورد استفاده فهرست شده‌اند.

* `count/pods`
* `count/persistentvolumeclaims`
* `count/services`
* `count/secrets`
* `count/configmaps`
* `count/deployments.apps`
* `count/replicasets.apps`
* `count/statefulsets.apps`
* `count/jobs.batch`
* `count/cronjobs.batch`

##### نحو تخصصی {#resource-quota-object-count-specialized}

نحو دیگری فقط برای تعیین همین نوع سهمیه وجود دارد که فقط برای برخی kindهای API کار می‌کند.
انواع زیر پشتیبانی می‌شوند:

| نام منبع | توضیح |
| ------------- | ----------- |
| `configmaps` | تعداد کل ConfigMapهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `persistentvolumeclaims` | تعداد کل [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) که می‌توانند در فضای نام وجود داشته باشند. |
| `pods` | تعداد کل پادهایی در وضعیت غیرپایانی که می‌توانند در فضای نام وجود داشته باشند. یک پاد در صورتی در وضعیت پایانی است که `.status.phase in (Failed, Succeeded)` درست باشد. |
| `replicationcontrollers` | تعداد کل ReplicationControllerهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `resourcequotas` | تعداد کل ResourceQuotaهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `services` | تعداد کل Serviceهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `services.loadbalancers` | تعداد کل Serviceهایی از نوع `LoadBalancer` که می‌توانند در فضای نام وجود داشته باشند. |
| `services.nodeports` | تعداد کل `NodePorts` تخصیص‌یافته به Serviceهایی از نوع `NodePort` یا `LoadBalancer` که می‌توانند در فضای نام وجود داشته باشند. |
| `secrets` | تعداد کل Secretهایی که می‌توانند در فضای نام وجود داشته باشند. |

برای مثال، سهمیهٔ `pods` تعداد `pods` غیرپایانیِ ایجادشده در یک فضای نام واحد را
می‌شمارد و حداکثری بر آن الزامی می‌کند. ممکن است بخواهید سهمیهٔ `pods`
را بر یک فضای نام تعیین کنید تا از حالتی جلوگیری کنید که کاربری پادهای کوچک بسیاری ایجاد کند و
ذخیرهٔ IPهای Pod در کلاستر را تمام کند.

نمونه‌های بیشتری را می‌توانید در [مشاهده و تنظیم سهمیه‌ها](#viewing-and-setting-quotas) بیابید.

## مشاهده و تنظیم سهمیه‌ها {#viewing-and-setting-quotas}

kubectl از ایجاد، به‌روزرسانی و مشاهدهٔ سهمیه‌ها پشتیبانی می‌کند:

```shell
kubectl create namespace myspace
```

```shell
cat <<EOF > compute-resources.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-resources
spec:
  hard:
    requests.cpu: "1"
    requests.memory: "1Gi"
    limits.cpu: "2"
    limits.memory: "2Gi"
    requests.nvidia.com/gpu: 4
EOF
```

```shell
kubectl create -f ./compute-resources.yaml --namespace=myspace
```

```shell
cat <<EOF > object-counts.yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: object-counts
spec:
  hard:
    configmaps: "10"
    persistentvolumeclaims: "4"
    pods: "4"
    replicationcontrollers: "20"
    secrets: "10"
    services: "10"
    services.loadbalancers: "2"
EOF
```

```shell
kubectl create -f ./object-counts.yaml --namespace=myspace
```

```shell
kubectl get quota --namespace=myspace
```

```none
NAME                    AGE
compute-resources       30s
object-counts           32s
```

```shell
kubectl describe quota compute-resources --namespace=myspace
```

```none
Name:                    compute-resources
Namespace:               myspace
Resource                 Used  Hard
--------                 ----  ----
limits.cpu               0     2
limits.memory            0     2Gi
requests.cpu             0     1
requests.memory          0     1Gi
requests.nvidia.com/gpu  0     4
```

```shell
kubectl describe quota object-counts --namespace=myspace
```

```none
Name:                   object-counts
Namespace:              myspace
Resource                Used    Hard
--------                ----    ----
configmaps              0       10
persistentvolumeclaims  0       4
pods                    0       4
replicationcontrollers  0       20
secrets                 1       10
services                0       10
services.loadbalancers  0       2
```

kubectl همچنین از سهمیهٔ تعداد آبجکت برای همهٔ منابع استاندارد وابسته به فضای نام
با استفاده از نحو `count/<resource>.<group>` پشتیبانی می‌کند:

```shell
kubectl create namespace myspace
```

```shell
kubectl create quota test --hard=count/deployments.apps=2,count/replicasets.apps=4,count/pods=3,count/secrets=4 --namespace=myspace
```

```shell
kubectl create deployment nginx --image=nginx --namespace=myspace --replicas=2
```

```shell
kubectl describe quota --namespace=myspace
```

```
Name:                         test
Namespace:                    myspace
Resource                      Used  Hard
--------                      ----  ----
count/deployments.apps        1     2
count/pods                    2     3
count/replicasets.apps        1     4
count/secrets                 1     4
```

## سهمیه و ظرفیت کلاستر

ResourceQuotaها مستقل از ظرفیت کلاستر هستند. آن‌ها
در قالب واحدهای مطلق بیان می‌شوند. بنابراین، اگر نودهایی به کلاستر خود اضافه کنید، این کار به‌طور خودکار
به هر فضای نام توانایی مصرف منابع بیشتر را *نمی‌دهد*.

گاهی ممکن است سیاست‌های پیچیده‌تری مورد نیاز باشد، مانند:

- تقسیم متناسب کل منابع کلاستر میان چند تیم.
- اجازه به هر مستأجر (tenant) برای افزایش مصرف منابع در صورت نیاز، اما با یک
  محدودیت سخاوتمندانه برای جلوگیری از اتمام تصادفی منابع.
- تشخیص تقاضا از یک فضای نام، افزودن نودها و افزایش سهمیه.

چنین سیاست‌هایی را می‌توان با استفاده از `ResourceQuotas` به‌عنوان اجزای سازنده پیاده‌سازی کرد،
با نوشتن یک «کنترل‌کننده» که مصرف سهمیه را زیر نظر می‌گیرد و محدودیت‌های سخت سهمیهٔ
هر فضای نام را بر اساس سیگنال‌های دیگر تنظیم می‌کند.

توجه داشته باشید که سهمیهٔ منابع، منابع تجمیعی کلاستر را تقسیم می‌کند، اما هیچ
محدودیتی در مورد نودها ایجاد نمی‌کند: پادهایی از چند فضای نام ممکن است روی یک نود اجرا شوند.

## محدوده‌های سهمیه {#quota-scopes}

هر سهمیه می‌تواند مجموعه‌ای از `scopes` مرتبط داشته باشد. یک سهمیه فقط زمانی مصرف یک منبع را اندازه می‌گیرد که آن منبع با
اشتراک محدوده‌های برشمرده منطبق باشد.

هنگامی که یک محدوده به سهمیه اضافه می‌شود، تعداد منابعی را که سهمیه پشتیبانی می‌کند به منابع مربوط به آن محدوده محدود می‌کند.
مشخص‌کردن منابعی در سهمیه که بیرون از مجموعهٔ مجاز باشند، به خطای اعتبارسنجی منجر می‌شود.

کوبرنتیز {{< skew currentVersion >}} از محدوده‌های زیر پشتیبانی می‌کند:

| محدوده | توضیح |
| ----- | ----------- |
| [`BestEffort`](#quota-scope-best-effort) | با پادهایی منطبق می‌شود که کیفیت سرویس best effort دارند. |
| [`CrossNamespacePodAffinity`](#cross-namespace-pod-affinity-scope) | با پادهایی منطبق می‌شود که [عبارت‌های (ضد)وابستگی](/docs/concepts/scheduling-eviction/assign-pod-node) پاد میان فضاهای نام دارند. |
| [`NotBestEffort`](#quota-scope-non-best-effort) | با پادهایی منطبق می‌شود که کیفیت سرویس best effort ندارند. |
| [`NotTerminating`](#quota-scope-non-terminating) | با پادهایی منطبق می‌شود که `.spec.activeDeadlineSeconds` آن‌ها `nil` است |
| [`PriorityClass`](#resource-quota-per-priorityclass) | با پادهایی منطبق می‌شود که به [priority class](/docs/concepts/scheduling-eviction/pod-priority-preemption) مشخص‌شده ارجاع می‌دهند. |
| [`Terminating`](#quota-scope-terminating) | با پادهایی منطبق می‌شود که `.spec.activeDeadlineSeconds` آن‌ها >= `0` است |
| [`VolumeAttributesClass`](#quota-scope-volume-attributes-class) | با PersistentVolumeClaimهایی منطبق می‌شود که به [volume attributes class](/docs/concepts/storage/volume-attributes-classes) مشخص‌شده ارجاع می‌دهند. |

ResourceQuotaهایی که محدوده‌ای برایشان تنظیم شده است می‌توانند یک فیلد اختیاری `scopeSelector` نیز داشته باشند. یک یا چند _عبارت تطبیق_ (match expression) تعریف می‌کنید
که یک `operators` و در صورت لزوم مجموعه‌ای از `values` را برای تطبیق مشخص می‌کنند. برای مثال:

```yaml
  scopeSelector:
    matchExpressions:
      - scopeName: BestEffort # Match pods that have best effort quality of service
        operator: Exists # optional; "Exists" is implied for BestEffort scope
```

`scopeSelector` از مقادیر زیر در فیلد `operator` پشتیبانی می‌کند:

* `In`
* `NotIn`
* `Exists`
* `DoesNotExist`

اگر `operator` برابر `In` یا `NotIn` باشد، فیلد `values` باید دست‌کم
یک مقدار داشته باشد. برای مثال:

```yaml
  scopeSelector:
    matchExpressions:
      - scopeName: PriorityClass
        operator: In
        values:
          - middle
```

اگر `operator` برابر `Exists` یا `DoesNotExist` باشد، فیلد `values` *نباید*
مشخص شود.

### محدودهٔ پادهای Best effort {#quota-scope-best-effort}

این محدوده فقط سهمیهٔ مصرف‌شده توسط پادها را دنبال می‌کند.
فقط با پادهایی منطبق می‌شود که [کلاس QoS](/docs/concepts/workloads/pods/pod-qos/)
[best effort](/docs/concepts/workloads/pods/pod-qos/#besteffort) دارند.

`operator` برای یک `scopeSelector` باید `Exists` باشد.

### محدودهٔ پادهای غیر Best effort {#quota-scope-non-best-effort}

این محدوده فقط سهمیهٔ مصرف‌شده توسط پادها را دنبال می‌کند.
فقط با پادهایی منطبق می‌شود که [کلاس QoS](/docs/concepts/workloads/pods/pod-qos/)
[Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed)
یا [Burstable](/docs/concepts/workloads/pods/pod-qos/#burstable) دارند.

`operator` برای یک `scopeSelector` باید `Exists` باشد.

### محدودهٔ پادهای غیر Terminating {#quota-scope-non-terminating}

این محدوده فقط سهمیهٔ مصرف‌شده توسط پادهایی را دنبال می‌کند که terminating نیستند. `operator` برای یک `scopeSelector`
باید `Exists` باشد.

یک Pod در صورتی terminating نیست که فیلد `.spec.activeDeadlineSeconds` آن تنظیم نشده باشد.

می‌توانید از یک ResourceQuota با این محدوده برای مدیریت منابع زیر استفاده کنید:

* `count.pods`
* `pods`
* `cpu`
* `memory`
* `requests.cpu`
* `requests.memory`
* `limits.cpu`
* `limits.memory`

### محدودهٔ پادهای Terminating {#quota-scope-terminating}

این محدوده فقط سهمیهٔ مصرف‌شده توسط پادهایی را دنبال می‌کند که terminating هستند. `operator` برای یک `scopeSelector`
باید `Exists` باشد.

یک Pod در صورتی _terminating_ در نظر گرفته می‌شود که فیلد `.spec.activeDeadlineSeconds` آن روی هر عددی تنظیم شده باشد.

می‌توانید از یک ResourceQuota با این محدوده برای مدیریت منابع زیر استفاده کنید:

* `count.pods`
* `pods`
* `cpu`
* `memory`
* `requests.cpu`
* `requests.memory`
* `limits.cpu`
* `limits.memory`

### محدودهٔ وابستگی پاد میان فضاهای نام {#cross-namespace-pod-affinity-scope}
 
{{< feature-state for_k8s_version="v1.24" state="stable" >}}

می‌توانید از [محدودهٔ سهمیهٔ](#quota-scopes) `CrossNamespacePodAffinity` برای محدودکردن اینکه کدام فضاهای نام مجاز به
داشتن پادهایی با عبارت‌های وابستگی (affinity) میان فضاهای نام هستند استفاده کنید. به‌طور خاص، این محدوده کنترل می‌کند کدام پادها مجازند
فیلدهای `namespaces` یا `namespaceSelector` را در [عبارت‌های (ضد)وابستگی](/docs/concepts/scheduling-eviction/assign-pod-node) پاد تنظیم کنند.

جلوگیری از استفادهٔ کاربران از عبارت‌های وابستگی میان فضاهای نام ممکن است مطلوب باشد، زیرا یک پاد
با محدودیت‌های ضدوابستگی می‌تواند مانع زمان‌بندی پادهای همهٔ فضاهای نام دیگر
در یک دامنهٔ خرابی (failure domain) شود.

با استفاده از این محدوده، شما (به‌عنوان مدیر کلاستر) می‌توانید از اینکه فضاهای نام مشخصی - مانند `foo-ns` در مثال زیر -
پادهایی داشته باشند که از وابستگی پاد میان فضاهای نام استفاده می‌کنند جلوگیری کنید. این را با ایجاد یک آبجکت ResourceQuota در
آن فضای نام با محدودهٔ `CrossNamespacePodAffinity` و محدودیت سخت 0 پیکربندی می‌کنید:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: disable-cross-namespace-affinity
  namespace: foo-ns
spec:
  hard:
    pods: "0"
  scopeSelector:
    matchExpressions:
    - scopeName: CrossNamespacePodAffinity
      operator: Exists
```

اگر می‌خواهید استفاده از `namespaces` و `namespaceSelector` را به‌طور پیش‌فرض ممنوع کنید و
فقط برای فضاهای نام مشخصی مجاز بدانید، می‌توانید `CrossNamespacePodAffinity`
را به‌عنوان یک منبع محدودشده پیکربندی کنید؛ برای این کار پرچم `--admission-control-config-file` در kube-apiserver
را روی مسیر فایل پیکربندی زیر تنظیم کنید:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: "ResourceQuota"
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: ResourceQuotaConfiguration
    limitedResources:
    - resource: pods
      matchScopes:
      - scopeName: CrossNamespacePodAffinity
        operator: Exists
```

با پیکربندی بالا، پادها فقط در صورتی می‌توانند از `namespaces` و `namespaceSelector` در وابستگی پاد استفاده کنند
که فضای نامی که در آن ایجاد می‌شوند یک آبجکت سهمیهٔ منبع با
محدودهٔ `CrossNamespacePodAffinity` و محدودیت سختی بزرگ‌تر یا مساوی با تعداد پادهایی که از آن فیلدها استفاده می‌کنند داشته باشد.

### محدودهٔ PriorityClass {#resource-quota-per-priorityclass}

{{< feature-state for_k8s_version="v1.17" state="stable" >}}

یک ResourceQuota با محدودهٔ PriorityClass فقط با پادهایی منطبق می‌شود که
[priority class](/docs/concepts/scheduling-eviction/pod-priority-preemption) مشخصی دارند، و فقط
در صورتی که یکی از `scopeSelector`های موجود در مشخصات سهمیه، آن Pod مشخص را انتخاب کند.

پادها را می‌توان با یک [اولویت](/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority) مشخص ایجاد کرد.
می‌توانید با استفاده از فیلد `scopeSelector` در مشخصات سهمیه، مصرف منابع سیستم توسط یک پاد را بر اساس اولویت آن
کنترل کنید.


هنگامی که سهمیه با استفاده از فیلد `scopeSelector` برای PriorityClass محدوده‌بندی شود، ResourceQuota
فقط می‌تواند منابع زیر را دنبال (و محدود) کند:

* `pods`
* `cpu`
* `memory`
* `ephemeral-storage`
* `limits.cpu`
* `limits.memory`
* `limits.ephemeral-storage`
* `requests.cpu`
* `requests.memory`
* `requests.ephemeral-storage`

#### مثال {#quota-scope-priorityclass-example}

این مثال یک ResourceQuota ایجاد می‌کند و آن را با پادهایی با اولویت‌های مشخص منطبق می‌کند. این مثال
به این صورت کار می‌کند:

- پادهای کلاستر یکی از سه [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) «low»، «medium» و «high» را دارند.
  - اگر می‌خواهید این را امتحان کنید، از یک کلاستر آزمایشی استفاده کنید و پیش از ادامه، آن سه PriorityClass را راه‌اندازی کنید.
- برای هر اولویت یک آبجکت سهمیه ایجاد می‌شود.

این مجموعه از ResourceQuotaها را بررسی کنید:

{{% code_sample file="policy/quota.yaml" %}}

YAML را با استفاده از `kubectl create` اعمال کنید.

```shell
kubectl create -f https://k8s.io/examples/policy/quota.yaml
```

```
resourcequota/pods-high created
resourcequota/pods-medium created
resourcequota/pods-low created
```

با استفاده از `kubectl describe quota` تأیید کنید که سهمیهٔ `Used` برابر `0` است.

```shell
kubectl describe quota
```

```
Name:       pods-high
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     1k
memory      0     200Gi
pods        0     10


Name:       pods-low
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     5
memory      0     10Gi
pods        0     10


Name:       pods-medium
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     10
memory      0     20Gi
pods        0     10
```

یک پاد با اولویت «high» ایجاد کنید.

{{% code_sample file="policy/high-priority-pod.yaml" %}}

برای ایجاد Pod:

```shell
kubectl create -f https://k8s.io/examples/policy/high-priority-pod.yaml

```

تأیید کنید که آمار «Used» برای سهمیهٔ اولویت «high»، یعنی `pods-high`، تغییر کرده است و
دو سهمیهٔ دیگر بدون تغییر باقی مانده‌اند.

```shell
kubectl describe quota
```

```
Name:       pods-high
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         500m  1k
memory      10Gi  200Gi
pods        1     10


Name:       pods-low
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     5
memory      0     10Gi
pods        0     10


Name:       pods-medium
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     10
memory      0     20Gi
pods        0     10
```

#### محدودکردن پیش‌فرض مصرف PriorityClass

ممکن است مطلوب باشد که پادهایی با یک اولویت مشخص، مانند «cluster-services»،
در یک فضای نام فقط و فقط در صورتی مجاز باشند که یک آبجکت سهمیهٔ منطبق وجود داشته باشد.

با این سازوکار، اپراتورها می‌توانند استفاده از برخی priority classهای با اولویت بالا را
به تعداد محدودی از فضاهای نام محدود کنند و همهٔ فضاهای نام
به‌طور پیش‌فرض قادر به مصرف این priority classها نخواهند بود.

برای الزامی‌کردن این موضوع، باید از پرچم `--admission-control-config-file` در `kube-apiserver`
برای ارسال مسیر فایل پیکربندی زیر استفاده کرد:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: "ResourceQuota"
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: ResourceQuotaConfiguration
    limitedResources:
    - resource: pods
      matchScopes:
      - scopeName: PriorityClass
        operator: In
        values: ["cluster-services"]
```

سپس یک آبجکت سهمیهٔ منبع در فضای نام `kube-system` ایجاد کنید:

{{% code_sample file="policy/priority-class-resourcequota.yaml" %}}

```shell
kubectl apply -f https://k8s.io/examples/policy/priority-class-resourcequota.yaml -n kube-system
```

```none
resourcequota/pods-cluster-services created
```

در این حالت، ایجاد یک پاد در صورتی مجاز خواهد بود که:

1. `priorityClassName` مربوط به Pod مشخص نشده باشد.
1. `priorityClassName` مربوط به Pod روی مقداری غیر از `cluster-services` تنظیم شده باشد.
1. `priorityClassName` مربوط به Pod روی `cluster-services` تنظیم شده باشد، قرار باشد Pod
   در فضای نام `kube-system` ایجاد شود و از بررسی سهمیهٔ منبع گذشته باشد.

درخواست ایجاد یک Pod در صورتی رد می‌شود که `priorityClassName` آن روی `cluster-services` تنظیم شده باشد
و قرار باشد در فضای نامی غیر از `kube-system` ایجاد شود.

### محدودهٔ VolumeAttributesClass {#quota-scope-volume-attributes-class}

{{< feature-state feature_gate_name="VolumeAttributesClass" >}}

این محدوده فقط سهمیهٔ مصرف‌شده توسط PersistentVolumeClaimها را دنبال می‌کند.

PersistentVolumeClaimها را می‌توان با یک
[VolumeAttributesClass](/docs/concepts/storage/volume-attributes-classes/) مشخص ایجاد کرد و ممکن است پس از ایجاد تغییر کنند.
می‌توانید با استفاده از فیلد `scopeSelector` در مشخصات سهمیه، مصرف منابع ذخیره‌سازی توسط یک PVC را بر اساس
VolumeAttributesClassهای مرتبط کنترل کنید.

PVC از طریق فیلدهای زیر به VolumeAttributesClass مرتبط ارجاع می‌دهد:

* `spec.volumeAttributesClassName`
* `status.currentVolumeAttributesClassName`
* `status.modifyVolumeStatus.targetVolumeAttributesClassName`

یک ResourceQuota مرتبط فقط در صورتی منطبق و مصرف می‌شود که ResourceQuota یک `scopeSelector` داشته باشد که PVC را انتخاب کند.

هنگامی که سهمیه با استفاده از فیلد `scopeSelector` برای volume attributes class محدوده‌بندی شود، آبجکت سهمیه محدود می‌شود به اینکه فقط منابع زیر را دنبال کند:

* `persistentvolumeclaims`
* `requests.storage`

برای آشنایی بیشتر با این موضوع، [محدودکردن مصرف ذخیره‌سازی](/docs/tasks/administer-cluster/limit-storage-consumption/) را بخوانید.


## {{% heading "whatsnext" %}}

- یک [مثال مفصل از نحوهٔ استفاده از سهمیهٔ منابع](/docs/tasks/administer-cluster/quota-api-object/) را ببینید.
- [مرجع API](/docs/reference/kubernetes-api/core/resource-quota-v1/) مربوط به ResourceQuota را بخوانید
- دربارهٔ [LimitRangeها](/docs/concepts/policy/limit-range/) بیاموزید
- برای اطلاعات بیشتر می‌توانید [سند طراحی ResourceQuota](https://git.k8s.io/design-proposals-archive/resource-management/admission_control_resource_quota.md)
  تاریخی را بخوانید.
- همچنین می‌توانید [سند طراحی پشتیبانی سهمیه برای priority class](https://git.k8s.io/design-proposals-archive/scheduling/pod-priority-resourcequota.md) را بخوانید.
