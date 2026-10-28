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

وقتی چند کاربر یا تیم از یک کلاستر با تعداد ثابتی نود به‌طور مشترک استفاده می‌کنند،
این نگرانی وجود دارد که یک تیم بیش از سهم منصفانهٔ خود از منابع استفاده کند.

_سهمیه‌های منابع_ (resource quotas) ابزاری است که مدیران کلاستر برای رفع این نگرانی در اختیار دارند.

هر سهمیهٔ منبع با یک آبجکت ResourceQuota تعریف می‌شود و محدودیت‌هایی فراهم می‌کند که مجموع مصرف منابع را در هر {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} محدود می‌کند. یک ResourceQuota همچنین می‌تواند
[تعداد آبجکت‌هایی را که می‌توان در یک فضای نام ایجاد کرد](#quota-on-object-count) بر اساس نوع API محدود کند. افزون بر این، می‌تواند مقدار کل
{{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}} را که آبجکت‌های API موجود در آن فضای نام مصرف می‌کنند نیز محدود کند.

{{< caution >}}
نه رقابت بر سر منابع و نه تغییر سهمیه‌ها، هیچ‌کدام بر منابعی که از قبل ایجاد شده‌اند اثری ندارد.
{{< /caution >}}

<!-- body -->

## نحوهٔ کار ResourceQuotaها در کوبرنتیز

ResourceQuotaها به این شکل کار می‌کنند:

- تیم‌های مختلف در فضاهای نام مختلف کار می‌کنند. این جداسازی را می‌توان با
  [RBAC](/docs/reference/access-authn-authz/rbac/) یا هر سازوکار [مجوزدهی](/docs/reference/access-authn-authz/authorization/) دیگری
  اعمال کرد.

- مدیر کلاستر برای هر فضای نام دست‌کم یک ResourceQuota ایجاد می‌کند.
  - برای اطمینان از اینکه این محدودیت همچنان اعمال شود، مدیر کلاستر باید دسترسی به حذف یا به‌روزرسانی
    آن ResourceQuota را نیز محدود کند؛ برای مثال، با تعریف یک [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/).

- کاربران منابعی (مانند پادها، سرویس‌ها و غیره) را در فضای نام ایجاد می‌کنند و سیستم سهمیه
  میزان مصرف را پیگیری می‌کند تا مطمئن شود از محدودیت‌های سخت (hard limits) تعریف‌شده در ResourceQuota فراتر نمی‌رود.

  می‌توانید یک [دامنه](#quota-scopes) (scope) به ResourceQuota اعمال کنید تا محدودهٔ اعمال آن را مشخص کنید.

- اگر ایجاد یا به‌روزرسانی یک منبع، یکی از محدودیت‌های سهمیه را نقض کند، control plane آن درخواست را با کد وضعیت HTTP
  `403 Forbidden` رد می‌کند. این خطا شامل پیامی است که محدودیتِ نقض‌شده را توضیح می‌دهد.

- اگر سهمیه در یک فضای نام برای {{< glossary_tooltip text="منابعی" term_id="infrastructure-resource" >}}
  مانند `cpu` و `memory` فعال باشد، کاربران هنگام تعریف یک Pod باید درخواست‌ها (requests) یا محدودیت‌ها (limits) را برای این مقادیر مشخص کنند؛ در غیر این صورت،
  ممکن است سیستم سهمیه ایجاد پاد را رد کند.

  [راهنمای گام‌به‌گام](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/) سهمیهٔ منابع
  نمونه‌ای از نحوهٔ پرهیز از این مشکل را نشان می‌دهد.

{{< note >}}
* می‌توانید یک [LimitRange](/docs/concepts/policy/limit-range/) تعریف کنید
  تا برای پادهایی که هیچ نیازمندی منابع محاسباتی مشخص نکرده‌اند، مقادیر پیش‌فرض اعمال شود (تا کاربران مجبور نباشند این کار را به خاطر بسپارند).
{{< /note >}}

معمولاً پادها را مستقیماً ایجاد نمی‌کنید؛ برای مثال، بیشتر یک آبجکت [مدیریت بار کاری](/docs/concepts/workloads/controllers/)
مانند یک {{< glossary_tooltip term_id="deployment" >}} ایجاد می‌کنید. اگر Deploymentای ایجاد کنید که بخواهد بیش از
منابع موجود استفاده کند، ایجاد آن Deployment (یا هر آبجکت مدیریت بار کاری دیگر) **موفقیت‌آمیز است**، اما
ممکن است آن Deployment نتواند همهٔ پادهایی را که مدیریت می‌کند ایجاد کند. در این حالت می‌توانید وضعیت
Deployment را، برای مثال با `kubectl describe`، بررسی کنید تا ببینید چه اتفاقی افتاده است.

- برای منابع `cpu` و `memory`، ResourceQuotaها الزام می‌کنند که **هر**
  پاد (جدید) در آن فضای نام، محدودیتی برای آن منبع تعیین کند.
  اگر در یک فضای نام سهمیهٔ منبعی برای `cpu` یا `memory` اعمال کنید،
  شما و سایر کلاینت‌ها **باید** برای هر Pod جدیدی که ارسال می‌کنید، `requests` یا `limits` را برای آن منبع مشخص کنید.
  در غیر این صورت، ممکن است control plane پذیرش آن Pod را رد کند.
- برای سایر منابع: ResourceQuota کار می‌کند و پادهایی را در فضای نام که محدودیت یا درخواستی برای آن منبع
  تعیین نکرده‌اند نادیده می‌گیرد. این یعنی اگر سهمیهٔ منبع، ذخیره‌سازی موقت (ephemeral storage) این فضای نام را محدود کرده باشد،
  باز هم می‌توانید پاد جدیدی بدون محدودیت یا درخواست برای ذخیره‌سازی موقت ایجاد کنید.

می‌توانید از یک [LimitRange](/docs/concepts/policy/limit-range/) استفاده کنید تا برای این منابع
به‌طور خودکار یک درخواست پیش‌فرض تعیین شود.

نام هر آبجکت ResourceQuota باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

نمونه‌هایی از سیاست‌هایی که می‌توان با استفاده از فضاهای نام و سهمیه‌ها ایجاد کرد عبارت‌اند از:

- در کلاستری با ظرفیت ۳۲ گیبی‌بایت RAM و ۱۶ هسته، به تیم A اجازه دهید ۲۰ گیبی‌بایت و ۱۰ هسته استفاده کند،
  به تیم B اجازه دهید ۱۰ گیبی‌بایت و ۴ هسته استفاده کند و ۲ گیبی‌بایت و ۲ هسته را برای تخصیص‌های آینده رزرو کنید.
- فضای نام «testing» را به استفاده از ۱ هسته و ۱ گیبی‌بایت RAM محدود کنید و اجازه دهید فضای نام «production»
  به هر میزانی استفاده کند.

در حالتی که ظرفیت کل کلاستر کمتر از مجموع سهمیه‌های فضاهای نام باشد،
ممکن است بر سر منابع رقابت ایجاد شود. این وضعیت بر اساس اصل «اولویت با کسی است که زودتر بیاید» مدیریت می‌شود.


## فعال‌سازی سهمیهٔ منابع

پشتیبانی از ResourceQuota در بسیاری از توزیع‌های کوبرنتیز به‌طور پیش‌فرض فعال است. این قابلیت
زمانی فعال است که فلگ `--enable-admission-plugins=` در {{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
مقدار `ResourceQuota` را به‌عنوان یکی از آرگومان‌های خود داشته باشد.

سهمیهٔ منابع زمانی در یک فضای نام خاص اعمال می‌شود که یک
ResourceQuota در آن فضای نام وجود داشته باشد.

## انواع سهمیهٔ منابع

سازوکار ResourceQuota امکان اعمال انواع مختلفی از محدودیت‌ها را فراهم می‌کند. این
بخش انواع محدودیت‌هایی را که می‌توانید اعمال کنید شرح می‌دهد.

### سهمیه برای منابع زیرساختی {#compute-resource-quota}

می‌توانید مجموع کل
[منابع محاسباتی](/docs/concepts/configuration/manage-resources-containers/)
را که می‌توان در یک فضای نام مشخص درخواست کرد محدود کنید.

انواع منابع زیر پشتیبانی می‌شوند:

| نام منبع | توضیحات |
| ------------- | ----------- |
| `limits.cpu` | در میان همهٔ پادهایی که در وضعیت غیرپایانی هستند، مجموع محدودیت‌های CPU نمی‌تواند از این مقدار بیشتر شود. |
| `limits.memory` | در میان همهٔ پادهایی که در وضعیت غیرپایانی هستند، مجموع محدودیت‌های حافظه نمی‌تواند از این مقدار بیشتر شود. |
| `requests.cpu` | در میان همهٔ پادهایی که در وضعیت غیرپایانی هستند، مجموع درخواست‌های CPU نمی‌تواند از این مقدار بیشتر شود. |
| `requests.memory` | در میان همهٔ پادهایی که در وضعیت غیرپایانی هستند، مجموع درخواست‌های حافظه نمی‌تواند از این مقدار بیشتر شود. |
| `hugepages-<size>` | در میان همهٔ پادهایی که در وضعیت غیرپایانی هستند، تعداد درخواست‌های huge page با اندازهٔ مشخص‌شده نمی‌تواند از این مقدار بیشتر شود. |
| `cpu` | همانند `requests.cpu` |
| `memory` | همانند `requests.memory` |

### سهمیه برای منابع توسعه‌یافته

علاوه بر منابعی که در بالا ذکر شد، در نسخهٔ 1.10 پشتیبانی از سهمیه برای
[منابع توسعه‌یافته](/docs/concepts/configuration/manage-resources-containers/#extended-resources) (extended resources) اضافه شده است.

از آنجا که تخصیص بیش از ظرفیت (overcommit) برای منابع توسعه‌یافته مجاز نیست، تعیین هم‌زمان `requests`
و `limits` برای یک منبع توسعه‌یافتهٔ واحد در یک سهمیه معنایی ندارد. بنابراین برای منابع توسعه‌یافته، فقط آیتم‌های سهمیه‌ای
مجاز هستند که پیشوند `requests.` دارند.

منبع GPU را به‌عنوان مثال در نظر بگیرید. اگر نام منبع `nvidia.com/gpu` باشد و بخواهید
تعداد کل GPUهای درخواست‌شده در یک فضای نام را به ۴ محدود کنید، می‌توانید سهمیه را به این صورت تعریف کنید:

* `requests.nvidia.com/gpu: 4`

برای جزئیات بیشتر، [مشاهده و تنظیم سهمیه‌ها](#viewing-and-setting-quotas) را ببینید.

### سهمیه برای درخواست‌های منبع DRA

درخواست‌های منبع (resource claims) در DRA (تخصیص پویای منابع یا Dynamic Resource Allocation) می‌توانند منابع DRA را بر اساس کلاس دستگاه (device class) درخواست کنند. برای مثال، فرض کنید
یک کلاس دستگاه به نام `examplegpu` دارید و می‌خواهید تعداد کل GPUهای درخواست‌شده در یک فضای نام را به ۴ محدود کنید.
در این صورت می‌توانید سهمیه را به این صورت تعریف کنید:

* `examplegpu.deviceclass.resource.k8s.io/devices: 4`

وقتی [تخصیص منابع توسعه‌یافته با DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#extended-resource)
فعال باشد، همان کلاس دستگاه با نام `examplegpu` را می‌توان از طریق منبع توسعه‌یافته درخواست کرد. این کار یا به‌صورت صریح انجام می‌شود،
یعنی زمانی که فیلد ExtendedResourceName کلاس دستگاه مقداری مانند `example.com/gpu` داشته باشد؛ در این حالت می‌توانید سهمیه را به این صورت تعریف کنید:

* `requests.example.com/gpu: 4`

یا به‌صورت ضمنی، با استفاده از نام منبع توسعه‌یافته‌ای که از نام کلاس دستگاه `examplegpu` مشتق می‌شود؛ در این حالت می‌توانید
سهمیه را به این صورت تعریف کنید:

* `requests.deviceclass.resource.kubernetes.io/examplegpu: 4`

همهٔ دستگاه‌هایی که از طریق درخواست‌های منبع یا منابع توسعه‌یافته درخواست می‌شوند، در هر سه سهمیهٔ
فهرست‌شده در بالا محاسبه می‌شوند. سهمیهٔ منبع توسعه‌یافته، برای مثال `requests.example.com/gpu: 4`، دستگاه‌هایی را که
افزونهٔ دستگاه (device plugin) فراهم می‌کند نیز محاسبه می‌کند.

برای جزئیات بیشتر، [مشاهده و تنظیم سهمیه‌ها](#viewing-and-setting-quotas) را ببینید.

### سهمیه برای ذخیره‌سازی

می‌توانید مجموع کل [ذخیره‌سازی](/docs/concepts/storage/persistent-volumes/) حجم‌هایی (volumes)
را که می‌توان در یک فضای نام مشخص درخواست کرد محدود کنید.

افزون بر این، می‌توانید مصرف منابع ذخیره‌سازی را بر اساس
[StorageClass](/docs/concepts/storage/storage-classes/) مرتبط با آن‌ها محدود کنید.

| نام منبع | توضیحات |
| ------------- | ----------- |
| `requests.storage` | در میان همهٔ درخواست‌های حجم ماندگار (persistent volume claims)، مجموع درخواست‌های ذخیره‌سازی نمی‌تواند از این مقدار بیشتر شود. |
| `persistentvolumeclaims` | تعداد کل [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) که می‌توانند در فضای نام وجود داشته باشند. |
| `<storage-class-name>.storageclass.storage.k8s.io/requests.storage` | در میان همهٔ درخواست‌های حجم ماندگار مرتبط با `<storage-class-name>`، مجموع درخواست‌های ذخیره‌سازی نمی‌تواند از این مقدار بیشتر شود. |
| `<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` | در میان همهٔ درخواست‌های حجم ماندگار مرتبط با `<storage-class-name>`، تعداد کل [درخواست‌های حجم ماندگار](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) که می‌توانند در فضای نام وجود داشته باشند. |

برای مثال، اگر بخواهید برای ذخیره‌سازی با StorageClass `gold` سهمیه‌ای جدا از
StorageClass `bronze` تعیین کنید، می‌توانید سهمیه را به این صورت تعریف کنید:

* `gold.storageclass.storage.k8s.io/requests.storage: 500Gi`
* `bronze.storageclass.storage.k8s.io/requests.storage: 100Gi`

#### سهمیه برای ذخیره‌سازی موقت محلی

{{< feature-state for_k8s_version="v1.8" state="alpha" >}}


| نام منبع | توضیحات |
| ------------- | ----------- |
| `requests.ephemeral-storage` | در میان همهٔ پادهای فضای نام، مجموع درخواست‌های ذخیره‌سازی موقت محلی نمی‌تواند از این مقدار بیشتر شود. |
| `limits.ephemeral-storage` | در میان همهٔ پادهای فضای نام، مجموع محدودیت‌های ذخیره‌سازی موقت محلی نمی‌تواند از این مقدار بیشتر شود. |
| `ephemeral-storage` | همانند `requests.ephemeral-storage`. |

{{< note >}}
هنگام استفاده از یک محیط اجرای کانتینر مبتنی بر CRI، لاگ‌های کانتینر نیز جزو سهمیهٔ ذخیره‌سازی موقت محاسبه می‌شوند.
این موضوع ممکن است به بیرون‌راندن (eviction) غیرمنتظرهٔ پادهایی منجر شود که سهمیهٔ ذخیره‌سازی خود را به پایان رسانده‌اند.

برای جزئیات بیشتر به [معماری لاگ‌گیری](/docs/concepts/cluster-administration/logging/) مراجعه کنید.
{{< /note >}}

### سهمیه برای تعداد آبجکت‌ها

می‌توانید برای *تعداد کل یک نوع خاص از {{< glossary_tooltip text="منبع" term_id="api-resource" >}}* در API کوبرنتیز سهمیه تعیین کنید.
برای این کار از نحو زیر استفاده کنید:

* `count/<resource>.<group>` برای منابعی که به گروه‌های API غیرهسته‌ای تعلق دارند
* `count/<resource>` برای منابعی که به گروه API هسته تعلق دارند

برای مثال، API مربوط به PodTemplate در گروه API هسته قرار دارد؛ بنابراین اگر بخواهید تعداد
آبجکت‌های PodTemplate را در یک فضای نام محدود کنید، از `count/podtemplates` استفاده می‌کنید.

این نوع سهمیه‌ها برای جلوگیری از تمام شدن فضای ذخیره‌سازی control plane مفید هستند. برای مثال، ممکن است
بخواهید با توجه به حجم زیاد Secretها، تعداد آن‌ها را در یک سرور محدود کنید. وجود تعداد بیش از حد Secret در یک کلاستر
در عمل می‌تواند مانع راه‌اندازی سرورها و کنترل‌کننده‌ها شود. همچنین می‌توانید برای Jobها سهمیه تعیین کنید تا از
خطرات یک CronJob با پیکربندی نادرست در امان بمانید. CronJobهایی که Jobهای بیش از حدی در یک فضای نام ایجاد می‌کنند، می‌توانند به حملهٔ منع سرویس (denial of service) منجر شوند.



اگر سهمیه را به این روش تعریف کنید، این سهمیه بر APIهای کوبرنتیز که بخشی از سرور API هستند و
نیز بر هر منبع سفارشی مبتنی بر CustomResourceDefinition اعمال می‌شود.
برای مثال، برای ایجاد سهمیه روی منبع سفارشی `widgets` در گروه API `example.com`،
از `count/widgets.example.com` استفاده کنید.
اگر از [تجمیع API](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) (API aggregation) برای
افزودن APIهای سفارشی دیگری استفاده کنید که به‌صورت CustomResourceDefinition تعریف نشده‌اند، control plane هستهٔ کوبرنتیز
سهمیه را برای API تجمیع‌شده اعمال نمی‌کند. انتظار می‌رود سرور API افزونه، در صورتی که برای API سفارشی مناسب باشد،
اعمال سهمیه را خودش فراهم کند.

##### نحو عمومی {#resource-quota-object-count-generic}

فهرست زیر نمونه‌هایی رایج از انواع آبجکت‌هایی است که ممکن است بخواهید تحت سهمیهٔ تعداد آبجکت قرار دهید.
این نمونه‌ها بر اساس رشتهٔ پیکربندی‌ای که باید استفاده کنید فهرست شده‌اند.

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

نحو دیگری نیز برای تعیین همین نوع سهمیه وجود دارد که فقط برای برخی از انواع API کار می‌کند.
انواع زیر پشتیبانی می‌شوند:

| نام منبع | توضیحات |
| ------------- | ----------- |
| `configmaps` | تعداد کل ConfigMapهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `persistentvolumeclaims` | تعداد کل [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) که می‌توانند در فضای نام وجود داشته باشند. |
| `pods` | تعداد کل پادهایی در وضعیت غیرپایانی که می‌توانند در فضای نام وجود داشته باشند. یک پاد زمانی در وضعیت پایانی است که عبارت `.status.phase in (Failed, Succeeded)` درست باشد. |
| `replicationcontrollers` | تعداد کل ReplicationControllerهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `resourcequotas` | تعداد کل ResourceQuotaهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `services` | تعداد کل Serviceهایی که می‌توانند در فضای نام وجود داشته باشند. |
| `services.loadbalancers` | تعداد کل Serviceهایی از نوع `LoadBalancer` که می‌توانند در فضای نام وجود داشته باشند. |
| `services.nodeports` | تعداد کل `NodePorts` تخصیص‌یافته به Serviceهایی از نوع `NodePort` یا `LoadBalancer` که می‌توانند در فضای نام وجود داشته باشند. |
| `secrets` | تعداد کل Secretهایی که می‌توانند در فضای نام وجود داشته باشند. |

برای مثال، سهمیهٔ `pods` تعداد `pods` غیرپایانیِ ایجادشده در یک فضای نام را می‌شمارد
و سقفی برای آن اعمال می‌کند. ممکن است بخواهید سهمیهٔ `pods` را روی یک فضای نام تعیین کنید
تا از وضعیتی جلوگیری کنید که در آن کاربری تعداد زیادی پاد کوچک ایجاد می‌کند و
ذخیرهٔ IPهای پاد در کلاستر را به پایان می‌رساند.

نمونه‌های بیشتری را می‌توانید در [مشاهده و تنظیم سهمیه‌ها](#viewing-and-setting-quotas) بیابید.

## مشاهده و تنظیم سهمیه‌ها

ابزار kubectl از ایجاد، به‌روزرسانی و مشاهدهٔ سهمیه‌ها پشتیبانی می‌کند:

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

ابزار kubectl همچنین با استفاده از نحو `count/<resource>.<group>` از سهمیهٔ تعداد آبجکت برای همهٔ
منابع استاندارد وابسته به فضای نام پشتیبانی می‌کند:

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

ResourceQuotaها مستقل از ظرفیت کلاستر هستند و با واحدهای مطلق بیان می‌شوند.
بنابراین اگر نودهایی به کلاستر خود اضافه کنید، این کار به‌طور خودکار به هر فضای نام
امکان مصرف منابع بیشتر را *نمی‌دهد*.

گاهی ممکن است سیاست‌های پیچیده‌تری مورد نیاز باشد، مانند:

- تقسیم متناسب کل منابع کلاستر میان چند تیم.
- اجازه دادن به هر مستأجر (tenant) برای افزایش مصرف منابع در صورت نیاز، همراه با یک
  محدودیت سخاوتمندانه برای جلوگیری از تمام شدن تصادفی منابع.
- تشخیص تقاضا در یک فضای نام، افزودن نود و افزایش سهمیه.

چنین سیاست‌هایی را می‌توان با استفاده از `ResourceQuotas` به‌عنوان اجزای سازنده پیاده‌سازی کرد؛
به این صورت که یک «کنترل‌کننده» نوشته شود که میزان مصرف سهمیه را زیر نظر بگیرد و محدودیت‌های سخت
سهمیهٔ هر فضای نام را بر اساس سیگنال‌های دیگر تنظیم کند.

توجه کنید که سهمیهٔ منابع، مجموع منابع کلاستر را تقسیم می‌کند، اما هیچ محدودیتی
در مورد نودها ایجاد نمی‌کند: پادهایی از چند فضای نام مختلف ممکن است روی یک نود اجرا شوند.

## دامنه‌های سهمیه

هر سهمیه می‌تواند مجموعه‌ای از `scopes` (دامنه‌ها) داشته باشد. سهمیه مصرف یک منبع را فقط زمانی اندازه می‌گیرد که آن منبع با اشتراک دامنه‌های فهرست‌شده مطابقت داشته باشد.

وقتی دامنه‌ای به سهمیه افزوده می‌شود، منابعی که سهمیه پشتیبانی می‌کند به منابع مرتبط با آن دامنه محدود می‌شوند. اگر در سهمیه منابعی خارج از این مجموعهٔ مجاز مشخص شود، خطای اعتبارسنجی رخ می‌دهد.

کوبرنتیز {{< skew currentVersion >}} از دامنه‌های زیر پشتیبانی می‌کند:

| دامنه | توضیح |
| ----- | ----------- |
| [`BestEffort`](#quota-scope-best-effort) | با پادهایی مطابقت دارد که کیفیت سرویس best effort دارند. |
| [`CrossNamespacePodAffinity`](#cross-namespace-pod-affinity-scope) | با پادهایی مطابقت دارد که [شرط‌های affinity (یا anti-affinity)](/docs/concepts/scheduling-eviction/assign-pod-node) بین‌فضای‌نامی دارند. |
| [`NotBestEffort`](#quota-scope-non-best-effort) | با پادهایی مطابقت دارد که کیفیت سرویس best effort ندارند. |
| [`NotTerminating`](#quota-scope-non-terminating) | با پادهایی مطابقت دارد که مقدار `.spec.activeDeadlineSeconds` در آن‌ها `nil` است. |
| [`PriorityClass`](#resource-quota-per-priorityclass) | با پادهایی مطابقت دارد که به [کلاس اولویت](/docs/concepts/scheduling-eviction/pod-priority-preemption) مشخص‌شده ارجاع می‌دهند. |
| [`Terminating`](#quota-scope-terminating) | با پادهایی مطابقت دارد که در آن‌ها `.spec.activeDeadlineSeconds` >= `0` است. |
| [`VolumeAttributesClass`](#quota-scope-volume-attributes-class) | با PersistentVolumeClaimهایی مطابقت دارد که به [کلاس ویژگی‌های حجم](/docs/concepts/storage/volume-attributes-classes) مشخص‌شده ارجاع می‌دهند. |

آبجکت‌های ResourceQuota که دامنه برایشان تعیین شده است، می‌توانند فیلد اختیاری `scopeSelector` نیز داشته باشند. در این فیلد یک یا چند _عبارت تطبیق_ (match expression) تعریف می‌کنید که هر کدام یک `operators` و در صورت لزوم مجموعه‌ای از `values` را برای تطبیق مشخص می‌کند. برای مثال:

```yaml
  scopeSelector:
    matchExpressions:
      - scopeName: BestEffort # Match pods that have best effort quality of service
        operator: Exists # optional; "Exists" is implied for BestEffort scope
```

فیلد `scopeSelector` از مقادیر زیر در فیلد `operator` پشتیبانی می‌کند:

* `In`
* `NotIn`
* `Exists`
* `DoesNotExist`

اگر مقدار `operator` برابر `In` یا `NotIn` باشد، فیلد `values` باید دست‌کم یک مقدار داشته باشد. برای مثال:

```yaml
  scopeSelector:
    matchExpressions:
      - scopeName: PriorityClass
        operator: In
        values:
          - middle
```

اگر مقدار `operator` برابر `Exists` یا `DoesNotExist` باشد، فیلد `values` *نباید* مشخص شود.

### دامنهٔ پادهای best effort {#quota-scope-best-effort}

این دامنه فقط سهمیهٔ مصرف‌شده توسط پادها را ردیابی می‌کند و فقط با پادهایی مطابقت دارد که
[کلاس QoS](/docs/concepts/workloads/pods/pod-qos/) آن‌ها [best effort](/docs/concepts/workloads/pods/pod-qos/#besteffort) است.

مقدار `operator` در `scopeSelector` باید `Exists` باشد.

### دامنهٔ پادهای غیر best effort {#quota-scope-non-best-effort}

این دامنه فقط سهمیهٔ مصرف‌شده توسط پادها را ردیابی می‌کند و فقط با پادهایی مطابقت دارد که
[کلاس QoS](/docs/concepts/workloads/pods/pod-qos/) آن‌ها [Guaranteed](/docs/concepts/workloads/pods/pod-qos/#guaranteed)
یا [Burstable](/docs/concepts/workloads/pods/pod-qos/#burstable) است.

مقدار `operator` در `scopeSelector` باید `Exists` باشد.

### دامنهٔ پادهای غیرپایان‌یابنده {#quota-scope-non-terminating}

این دامنه فقط سهمیهٔ مصرف‌شده توسط پادهایی را ردیابی می‌کند که پایان‌یابنده نیستند. مقدار `operator` در
`scopeSelector` باید `Exists` باشد.

پادی که فیلد `.spec.activeDeadlineSeconds` آن تنظیم نشده باشد، پایان‌یابنده به شمار نمی‌آید.

با یک ResourceQuota با این دامنه می‌توانید منابع زیر را مدیریت کنید:

* `count.pods`
* `pods`
* `cpu`
* `memory`
* `requests.cpu`
* `requests.memory`
* `limits.cpu`
* `limits.memory`

### دامنهٔ پادهای پایان‌یابنده {#quota-scope-terminating}

این دامنه فقط سهمیهٔ مصرف‌شده توسط پادهای پایان‌یابنده را ردیابی می‌کند. مقدار `operator` در
`scopeSelector` باید `Exists` باشد.

پادی که فیلد `.spec.activeDeadlineSeconds` آن روی هر عددی تنظیم شده باشد، _پایان‌یابنده_ به شمار می‌آید.

با یک ResourceQuota با این دامنه می‌توانید منابع زیر را مدیریت کنید:

* `count.pods`
* `pods`
* `cpu`
* `memory`
* `requests.cpu`
* `requests.memory`
* `limits.cpu`
* `limits.memory`

### دامنهٔ affinity بین‌فضای‌نامی پاد
 
{{< feature-state for_k8s_version="v1.24" state="stable" >}}

با [دامنهٔ سهمیهٔ](#quota-scopes) `CrossNamespacePodAffinity` می‌توانید تعیین کنید کدام فضاهای نام اجازه دارند
پادهایی با شرط‌های affinity بین‌فضای‌نامی داشته باشند. به‌طور مشخص، این دامنه تعیین می‌کند کدام پادها مجازند
فیلدهای `namespaces` یا `namespaceSelector` را در [شرط‌های affinity (یا anti-affinity)](/docs/concepts/scheduling-eviction/assign-pod-node) پاد تنظیم کنند.

ممکن است بخواهید کاربران را از به‌کاربردن شرط‌های affinity بین‌فضای‌نامی بازدارید، زیرا پادی که
محدودیت‌های anti-affinity دارد می‌تواند مانع زمان‌بندی پادهای همهٔ فضاهای نام دیگر
در یک دامنهٔ خرابی (failure domain) شود.

با این دامنه، شما (به‌عنوان مدیر کلاستر) می‌توانید مانع شوید که برخی فضاهای نام، مانند `foo-ns` در مثال زیر،
پادهایی با affinity بین‌فضای‌نامی داشته باشند. برای این کار یک آبجکت ResourceQuota با دامنهٔ
`CrossNamespacePodAffinity` و حد سخت ۰ در آن فضای نام ایجاد می‌کنید:

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

اگر می‌خواهید استفاده از `namespaces` و `namespaceSelector` به‌طور پیش‌فرض ممنوع باشد و
فقط برای فضاهای نام مشخصی مجاز شود، می‌توانید `CrossNamespacePodAffinity` را به‌عنوان
یک منبع محدود پیکربندی کنید. برای این کار فلگ `--admission-control-config-file` در kube-apiserver
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

با پیکربندی بالا، پادها فقط زمانی می‌توانند از `namespaces` و `namespaceSelector` در affinity پاد استفاده کنند
که در فضای نامی که در آن ایجاد می‌شوند یک آبجکت سهمیهٔ منبع با دامنهٔ
`CrossNamespacePodAffinity` وجود داشته باشد و حد سخت آن بزرگ‌تر یا مساوی تعداد پادهایی باشد که از این فیلدها استفاده می‌کنند.

### دامنهٔ PriorityClass {#resource-quota-per-priorityclass}

{{< feature-state for_k8s_version="v1.17" state="stable" >}}

یک ResourceQuota با دامنهٔ PriorityClass فقط با پادهایی مطابقت دارد که
[کلاس اولویت](/docs/concepts/scheduling-eviction/pod-priority-preemption) مشخصی دارند، و آن هم فقط
در صورتی که یکی از `scopeSelector`های مشخصات سهمیه آن پاد را انتخاب کند.

پادها را می‌توان با [اولویت](/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority) مشخصی ایجاد کرد.
با استفاده از فیلد `scopeSelector` در مشخصات سهمیه، می‌توانید مصرف منابع سیستم توسط هر پاد را
بر اساس اولویت آن کنترل کنید.


وقتی دامنهٔ سهمیه با فیلد `scopeSelector` به PriorityClass محدود شود، ResourceQuota
فقط می‌تواند منابع زیر را ردیابی (و محدود) کند:

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

در این مثال یک ResourceQuota ایجاد می‌شود و با پادهایی با اولویت‌های مشخص تطبیق داده می‌شود.
روند مثال به این صورت است:

- پادهای کلاستر یکی از سه [PriorityClass](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) «low»، «medium» و «high» را دارند.
  - اگر می‌خواهید این مثال را امتحان کنید، از یک کلاستر آزمایشی استفاده کنید و پیش از ادامه، این سه PriorityClass را راه‌اندازی کنید.
- برای هر اولویت یک آبجکت سهمیه ایجاد می‌شود.

این مجموعه از ResourceQuotaها را بررسی کنید:

{{% code_sample file="policy/quota.yaml" %}}

فایل YAML را با `kubectl create` اعمال کنید.

```shell
kubectl create -f https://k8s.io/examples/policy/quota.yaml
```

```
resourcequota/pods-high created
resourcequota/pods-medium created
resourcequota/pods-low created
```

با `kubectl describe quota` بررسی کنید که مقدار `Used` سهمیه برابر `0` است.

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

برای ایجاد پاد:

```shell
kubectl create -f https://k8s.io/examples/policy/high-priority-pod.yaml

```

بررسی کنید که آمار «Used» برای سهمیهٔ اولویت «high»، یعنی `pods-high`، تغییر کرده و
دو سهمیهٔ دیگر بدون تغییر مانده‌اند.

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

گاهی لازم است پادهایی با اولویتی مشخص، مانند «cluster-services»، فقط و فقط در صورتی
در یک فضای نام مجاز باشند که یک آبجکت سهمیهٔ متناظر در آن وجود داشته باشد.

با این سازوکار، اپراتورها می‌توانند استفاده از برخی کلاس‌های اولویت بالا را به تعداد محدودی
از فضاهای نام منحصر کنند، و همهٔ فضاهای نام به‌طور پیش‌فرض نمی‌توانند این کلاس‌های اولویت را مصرف کنند.

برای اعمال این محدودیت، باید با فلگ `--admission-control-config-file` در `kube-apiserver`
مسیر فایل پیکربندی زیر را ارسال کنید:

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

در این حالت، ایجاد پاد در موارد زیر مجاز است:

1. فیلد `priorityClassName` پاد مشخص نشده باشد.
1. فیلد `priorityClassName` پاد مقداری غیر از `cluster-services` داشته باشد.
1. فیلد `priorityClassName` پاد روی `cluster-services` تنظیم شده باشد، پاد قرار باشد
   در فضای نام `kube-system` ایجاد شود و بررسی سهمیهٔ منبع را با موفقیت گذرانده باشد.

اگر `priorityClassName` پاد روی `cluster-services` تنظیم شده باشد و پاد قرار باشد
در فضای نامی غیر از `kube-system` ایجاد شود، درخواست ایجاد آن رد می‌شود.

### دامنهٔ VolumeAttributesClass {#quota-scope-volume-attributes-class}

{{< feature-state feature_gate_name="VolumeAttributesClass" >}}

این دامنه فقط سهمیهٔ مصرف‌شده توسط PersistentVolumeClaimها را ردیابی می‌کند.

هر PersistentVolumeClaim را می‌توان با یک
[VolumeAttributesClass](/docs/concepts/storage/volume-attributes-classes/) مشخص ایجاد کرد و ممکن است پس از ایجاد تغییر کند.
با استفاده از فیلد `scopeSelector` در مشخصات سهمیه، می‌توانید مصرف منابع ذخیره‌سازی توسط هر PVC را
بر اساس VolumeAttributesClassهای مرتبط با آن کنترل کنید.

هر PVC از طریق فیلدهای زیر به VolumeAttributesClass مرتبط ارجاع می‌دهد:

* `spec.volumeAttributesClassName`
* `status.currentVolumeAttributesClassName`
* `status.modifyVolumeStatus.targetVolumeAttributesClassName`

یک ResourceQuota مرتبط فقط زمانی تطبیق داده و مصرف می‌شود که `scopeSelector` آن، PVC را انتخاب کند.

وقتی دامنهٔ سهمیه با فیلد `scopeSelector` به کلاس ویژگی‌های حجم محدود شود، آبجکت سهمیه فقط می‌تواند منابع زیر را ردیابی کند:

* `persistentvolumeclaims`
* `requests.storage`

برای اطلاعات بیشتر، [محدودکردن مصرف ذخیره‌سازی](/docs/tasks/administer-cluster/limit-storage-consumption/) را بخوانید.


## {{% heading "whatsnext" %}}

- [مثالی مفصل از نحوهٔ استفاده از سهمیهٔ منبع](/docs/tasks/administer-cluster/quota-api-object/) را ببینید.
- [مرجع API](/docs/reference/kubernetes-api/core/resource-quota-v1/) مربوط به ResourceQuota را بخوانید.
- دربارهٔ [LimitRangeها](/docs/concepts/policy/limit-range/) بیاموزید.
- برای اطلاعات بیشتر می‌توانید [سند طراحی تاریخی ResourceQuota](https://git.k8s.io/design-proposals-archive/resource-management/admission_control_resource_quota.md)
  را بخوانید.
- همچنین می‌توانید [سند طراحی پشتیبانی سهمیه از کلاس اولویت](https://git.k8s.io/design-proposals-archive/scheduling/pod-priority-resourcequota.md) را بخوانید.
