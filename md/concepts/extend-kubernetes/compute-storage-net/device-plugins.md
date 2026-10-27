---
title: افزونه‌های دستگاه
description: >
  افزونه‌های دستگاه به شما اجازه می‌دهند کلاستر خود را با پشتیبانی از دستگاه‌ها یا منابعی پیکربندی کنید که به
  راه‌اندازی مخصوص فروشنده نیاز دارند، مانند GPUها، NICها، FPGAها یا حافظهٔ اصلی غیرفرار.
content_type: concept
weight: 20
---

<!-- overview -->
{{< feature-state for_k8s_version="v1.26" state="stable" >}}

کوبرنتیز یک چارچوب افزونهٔ دستگاه (device plugin) فراهم می‌کند که می‌توانید از آن برای اعلام منابع سخت‌افزاری سیستم
به {{< glossary_tooltip term_id="kubelet" >}} استفاده کنید.

فروشندگان به‌جای سفارشی‌سازی کد خود کوبرنتیز، می‌توانند یک
افزونهٔ دستگاه پیاده‌سازی کنند که شما آن را یا به‌صورت دستی یا به‌صورت یک {{< glossary_tooltip term_id="daemonset" >}} مستقر می‌کنید.
دستگاه‌های هدف شامل GPUها، NICهای با کارایی بالا، FPGAها، آداپتورهای InfiniBand
و سایر منابع محاسباتی مشابهی هستند که ممکن است به مقداردهی اولیه و راه‌اندازی
مخصوص فروشنده نیاز داشته باشند.

<!-- body -->

## ثبت افزونهٔ دستگاه

kubelet یک سرویس gRPC با نام `Registration` ارائه می‌دهد:

```gRPC
service Registration {
	rpc Register(RegisterRequest) returns (Empty) {}
}
```

یک افزونهٔ دستگاه می‌تواند از طریق این سرویس gRPC خود را در kubelet ثبت کند.
در طول ثبت، افزونهٔ دستگاه باید موارد زیر را ارسال کند:

* نام سوکت Unix خود.
* نسخهٔ API افزونهٔ دستگاه که بر اساس آن ساخته شده است.
* `ResourceName` که می‌خواهد اعلام کند. در اینجا `ResourceName` باید از
  [طرح نام‌گذاری منابع توسعه‌یافته](/docs/concepts/configuration/manage-resources-containers/#extended-resources)
  به شکل `vendor-domain/resourcetype` پیروی کند.
  (برای مثال، یک GPU از NVIDIA با نام `nvidia.com/gpu` اعلام می‌شود.)

پس از ثبت موفق، افزونهٔ دستگاه فهرست دستگاه‌هایی را که مدیریت می‌کند
به kubelet ارسال می‌کند و سپس kubelet مسئول اعلام آن منابع
به سرور API، به‌عنوان بخشی از به‌روزرسانی وضعیت نود توسط kubelet، است.
برای مثال، پس از اینکه یک افزونهٔ دستگاه `hardware-vendor.example/foo` را در kubelet ثبت کند
و دو دستگاه سالم را روی یک نود گزارش دهد، وضعیت نود به‌روزرسانی می‌شود
تا اعلام کند که نود ۲ دستگاه «Foo» نصب‌شده و در دسترس دارد.

سپس کاربران می‌توانند دستگاه‌ها را به‌عنوان بخشی از مشخصات یک Pod درخواست کنند
(به [`container`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) مراجعه کنید).
درخواست منابع توسعه‌یافته مشابه نحوهٔ مدیریت درخواست‌ها (requests) و محدودیت‌ها (limits) برای
سایر منابع است، با تفاوت‌های زیر:
* منابع توسعه‌یافته فقط به‌صورت منابع عدد صحیح پشتیبانی می‌شوند و نمی‌توان آن‌ها را بیش از ظرفیت تخصیص داد (overcommit).
* دستگاه‌ها را نمی‌توان میان کانتینرها به اشتراک گذاشت.

### مثال {#example-pod}

فرض کنید یک کلاستر کوبرنتیز افزونهٔ دستگاهی را اجرا می‌کند که منبع `hardware-vendor.example/foo`
را روی برخی نودها اعلام می‌کند. در اینجا مثالی از یک پاد آمده است که این منبع را برای اجرای یک بار کاری نمایشی درخواست می‌کند:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
spec:
  containers:
    - name: demo-container-1
      image: registry.k8s.io/pause:3.8
      resources:
        limits:
          hardware-vendor.example/foo: 2
#
# This Pod needs 2 of the hardware-vendor.example/foo devices
# and can only schedule onto a Node that's able to satisfy
# that need.
#
# If the Node has more than 2 of those devices available, the
# remainder would be available for other Pods to use.
```

## پیاده‌سازی افزونهٔ دستگاه

گردش کار کلی یک افزونهٔ دستگاه شامل مراحل زیر است:

1. مقداردهی اولیه. در این مرحله، افزونهٔ دستگاه مقداردهی اولیه و راه‌اندازی مخصوص فروشنده را
   انجام می‌دهد تا اطمینان حاصل کند دستگاه‌ها در وضعیت آماده قرار دارند.

1. افزونه یک سرویس gRPC را با یک سوکت Unix در مسیر میزبان
   `/var/lib/kubelet/device-plugins/` راه‌اندازی می‌کند (این مسیر به‌صورت ثابت در کد تعریف شده است و
   تحت تأثیر `--root-dir` در kubelet یا هر پیکربندی دیگری قرار نمی‌گیرد) که
   رابط‌های زیر را پیاده‌سازی می‌کند:

   ```gRPC
   service DevicePlugin {
         // GetDevicePluginOptions returns options to be communicated with Device Manager.
         rpc GetDevicePluginOptions(Empty) returns (DevicePluginOptions) {}

         // ListAndWatch returns a stream of List of Devices
         // Whenever a Device state change or a Device disappears, ListAndWatch
         // returns the new list
         rpc ListAndWatch(Empty) returns (stream ListAndWatchResponse) {}

         // Allocate is called during container creation so that the Device
         // Plugin can run device specific operations and instruct Kubelet
         // of the steps to make the Device available in the container
         rpc Allocate(AllocateRequest) returns (AllocateResponse) {}

         // GetPreferredAllocation returns a preferred set of devices to allocate
         // from a list of available ones. The resulting preferred allocation is not
         // guaranteed to be the allocation ultimately performed by the
         // devicemanager. It is only designed to help the devicemanager make a more
         // informed allocation decision when possible.
         rpc GetPreferredAllocation(PreferredAllocationRequest) returns (PreferredAllocationResponse) {}

         // PreStartContainer is called, if indicated by Device Plugin during registration phase,
         // before each container start. Device plugin can run device specific operations
         // such as resetting the device before making devices available to the container.
         rpc PreStartContainer(PreStartContainerRequest) returns (PreStartContainerResponse) {}
   }
   ```

   {{< note >}}
   افزونه‌ها ملزم نیستند پیاده‌سازی‌های کاربردی برای
   `GetPreferredAllocation()` یا `PreStartContainer()` ارائه دهند. پرچم‌هایی که در دسترس بودن
   این فراخوانی‌ها را نشان می‌دهند، در صورت وجود، باید در پیام `DevicePluginOptions`
   که در پاسخ به فراخوانی `GetDevicePluginOptions()` بازگردانده می‌شود تنظیم شوند. `kubelet`
   همواره پیش از فراخوانی مستقیم هر یک از توابع اختیاری، `GetDevicePluginOptions()` را فراخوانی می‌کند تا ببیند
   کدام‌یک در دسترس هستند.
   {{< /note >}}

1. افزونه خود را از طریق سوکت Unix در مسیر میزبان
   `/var/lib/kubelet/device-plugins/kubelet.sock` در kubelet ثبت می‌کند.

   {{< note >}}
   ترتیب گردش کار اهمیت دارد. برای ثبت موفق، افزونه باید پیش از ثبت خود در kubelet
   ارائهٔ سرویس gRPC را آغاز کرده باشد.
   {{< /note >}}

1. پس از ثبت موفق، افزونهٔ دستگاه در حالت ارائهٔ سرویس اجرا می‌شود و در این مدت
   سلامت دستگاه‌ها را پیوسته پایش می‌کند و هرگونه تغییر در وضعیت دستگاه را به kubelet گزارش می‌دهد.
   همچنین مسئول پاسخ‌گویی به درخواست‌های gRPC از نوع `Allocate` است. در طول `Allocate`، افزونهٔ دستگاه ممکن است
   آماده‌سازی مخصوص دستگاه را انجام دهد؛ برای مثال، پاک‌سازی GPU یا مقداردهی اولیهٔ QRNG.
   اگر عملیات موفق باشند، افزونهٔ دستگاه یک `AllocateResponse` بازمی‌گرداند که شامل پیکربندی‌های
   محیط اجرای کانتینر برای دسترسی به دستگاه‌های تخصیص‌یافته است. kubelet این اطلاعات را
   به محیط اجرای کانتینر منتقل می‌کند.

   یک `AllocateResponse` شامل صفر یا چند آبجکت `ContainerAllocateResponse` است. در این آبجکت‌ها،
   افزونهٔ دستگاه تغییراتی را تعریف می‌کند که باید در تعریف یک کانتینر اعمال شوند تا
   دسترسی به دستگاه فراهم شود. این تغییرات شامل موارد زیر است:

   * [حاشیه‌نویسی‌ها](/docs/concepts/overview/working-with-objects/annotations/)
   * نودهای دستگاه (device nodes)
   * متغیرهای محیطی
   * mountها
   * نام‌های کاملاً مشخص دستگاه CDI

   {{< note >}}
   پردازش نام‌های کاملاً مشخص دستگاه CDI توسط Device Manager مستلزم آن است
   که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `DevicePluginCDIDevices`
   هم برای kubelet و هم برای kube-apiserver فعال باشد. این قابلیت در کوبرنتیز v1.28 به‌عنوان قابلیت آلفا
   اضافه شد، در v1.29 به بتا و در v1.31 به GA ارتقا یافت.
   {{< /note >}}

### مدیریت راه‌اندازی مجدد kubelet

انتظار می‌رود یک افزونهٔ دستگاه راه‌اندازی مجدد kubelet را تشخیص دهد و خود را دوباره در نمونهٔ جدید
kubelet ثبت کند. یک نمونهٔ جدید kubelet هنگام شروع، همهٔ سوکت‌های Unix موجود در
`/var/lib/kubelet/device-plugins` (مسیر ثابت افزونه‌های دستگاه) را حذف می‌کند. یک افزونهٔ دستگاه می‌تواند حذف
سوکت Unix خود را پایش کند و پس از وقوع چنین رویدادی خود را دوباره ثبت کند.

### افزونهٔ دستگاه و دستگاه‌های ناسالم

مواردی پیش می‌آید که دستگاه‌ها دچار خرابی می‌شوند یا خاموش می‌شوند. مسئولیت افزونهٔ دستگاه
در این حالت، اطلاع‌دادن این وضعیت به kubelet با استفاده از API ‏`ListAndWatchResponse` است.

هنگامی که یک دستگاه ناسالم علامت‌گذاری شود، kubelet تعداد قابل تخصیص (allocatable)
این منبع را روی Node کاهش می‌دهد تا نشان دهد چه تعداد دستگاه برای زمان‌بندی پادهای جدید قابل استفاده است.
تعداد ظرفیت (capacity) منبع تغییر نخواهد کرد.

پادهایی که به دستگاه‌های خراب اختصاص داده شده بودند، همچنان به این دستگاه اختصاص‌یافته باقی می‌مانند.
معمولاً کدی که به دستگاه متکی است شروع به خطا کردن می‌کند و اگر `restartPolicy` برای Pod
برابر `Always` نباشد، ممکن است Pod به فاز Failed وارد شود، و در غیر این صورت وارد حلقهٔ crash شود.

پیش از کوبرنتیز v1.31، راه دانستن اینکه آیا یک Pod با
دستگاه خراب مرتبط است یا نه، استفاده از [PodResources API](#monitoring-device-plugin-resources) بود.

{{< feature-state feature_gate_name="ResourceHealthStatus" >}}

هنگامی که feature gate با نام `ResourceHealthStatus` فعال باشد (از v1.36 در وضعیت بتا و به‌طور پیش‌فرض فعال)،
فیلد `allocatedResourcesStatus`
به وضعیت هر کانتینر، درون `.status` هر Pod، اضافه می‌شود. فیلد `allocatedResourcesStatus`
اطلاعات سلامت هر دستگاه اختصاص‌یافته به کانتینر را گزارش می‌دهد.
هر ورودی سلامت منبع می‌تواند شامل یک فیلد اختیاری `message` با زمینهٔ تکمیلی و
قابل‌خواندن برای انسان دربارهٔ وضعیت سلامت باشد، مانند جزئیات خطا یا دلایل خرابی.

برای یک Pod ناموفق، یا در مواردی که به وجود خطا مشکوک هستید، می‌توانید از این وضعیت استفاده کنید تا دریابید آیا
رفتار Pod ممکن است با خرابی دستگاه مرتبط باشد یا نه. برای مثال، اگر یک شتاب‌دهنده
رویداد دمای بیش از حد را گزارش دهد، فیلد `allocatedResourcesStatus` ممکن است آن را گزارش کند.


## استقرار افزونهٔ دستگاه {#device-plugin-deployment}

می‌توانید یک افزونهٔ دستگاه را به‌صورت یک DaemonSet، به‌صورت یک بسته برای سیستم‌عامل نود خود،
یا به‌صورت دستی مستقر کنید.

دایرکتوری استاندارد `/var/lib/kubelet/device-plugins` (که در kubelet به‌صورت ثابت تعریف شده است) به دسترسی ممتاز (privileged) نیاز دارد،
بنابراین یک افزونهٔ دستگاه باید در یک زمینهٔ امنیتی ممتاز اجرا شود.
اگر افزونهٔ دستگاه را به‌صورت یک DaemonSet مستقر می‌کنید، `/var/lib/kubelet/device-plugins`
باید به‌عنوان یک {{< glossary_tooltip term_id="volume" >}}
در [PodSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) افزونه mount شود.

اگر رویکرد DaemonSet را انتخاب کنید، می‌توانید برای این کارها به کوبرنتیز تکیه کنید: قراردادن Pod
افزونهٔ دستگاه روی Nodeها، راه‌اندازی مجدد Pod دیمن پس از خرابی، و کمک به خودکارسازی ارتقاها.

## سازگاری API

پیش‌تر، طرح نسخه‌گذاری مستلزم آن بود که نسخهٔ API افزونهٔ دستگاه دقیقاً با
نسخهٔ Kubelet مطابقت داشته باشد. از زمان ارتقای این قابلیت به بتا در v1.12،
این دیگر یک الزام قطعی نیست. API نسخه‌گذاری شده است و از زمان ارتقای این قابلیت به بتا
پایدار بوده است. به همین دلیل، ارتقاهای kubelet باید بدون مشکل انجام شوند،
اما ممکن است همچنان پیش از پایدارسازی تغییراتی در API رخ دهد و در نتیجه تضمین نمی‌شود
که ارتقاها بدون ایجاد ناسازگاری باشند.

{{< note >}}
اگرچه جزء Device Manager در کوبرنتیز یک قابلیت با دسترس‌پذیری عمومی است،
_API افزونهٔ دستگاه_ پایدار نیست. برای اطلاعات دربارهٔ API افزونهٔ دستگاه و
سازگاری نسخه‌ها، [نسخه‌های API افزونهٔ دستگاه](/docs/reference/node/device-plugin-api-versions/) را بخوانید.
{{< /note >}}

کوبرنتیز، به‌عنوان یک پروژه، به توسعه‌دهندگان افزونه‌های دستگاه توصیه می‌کند که:

* تغییرات API افزونهٔ دستگاه را در نسخه‌های آینده دنبال کنند.
* از چند نسخه از API افزونهٔ دستگاه برای سازگاری رو به عقب/رو به جلو پشتیبانی کنند.

برای اجرای افزونه‌های دستگاه روی نودهایی که باید به نسخه‌ای از کوبرنتیز با
نسخهٔ جدیدتری از API افزونهٔ دستگاه ارتقا یابند، پیش از ارتقای این نودها، افزونه‌های دستگاه خود را
طوری ارتقا دهید که از هر دو نسخه پشتیبانی کنند. این رویکرد عملکرد پیوستهٔ
تخصیص دستگاه‌ها را در طول ارتقا تضمین می‌کند.

## پایش منابع افزونهٔ دستگاه {#monitoring-device-plugin-resources}

{{< feature-state for_k8s_version="v1.28" state="stable" >}}

برای پایش منابعی که افزونه‌های دستگاه فراهم می‌کنند، عامل‌های پایش باید بتوانند
مجموعهٔ دستگاه‌های در حال استفاده روی نود را کشف کنند و فراداده‌ای به دست آورند که مشخص کند
متریک باید به کدام کانتینر مرتبط شود. متریک‌های [Prometheus](https://prometheus.io/)
که عامل‌های پایش دستگاه ارائه می‌دهند باید از
[رهنمودهای ابزارگذاری کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-instrumentation/metric-instrumentation.md)
پیروی کنند و کانتینرها را با استفاده از برچسب‌های prometheus به نام‌های `pod`، `namespace` و `container` شناسایی کنند.

kubelet یک سرویس gRPC فراهم می‌کند تا کشف دستگاه‌های در حال استفاده و ارائهٔ فراداده
برای این دستگاه‌ها را ممکن سازد:

```gRPC
// PodResourcesLister is a service provided by the kubelet that provides information about the
// node resources consumed by pods and containers on the node
service PodResourcesLister {
    rpc List(ListPodResourcesRequest) returns (ListPodResourcesResponse) {}
    rpc GetAllocatableResources(AllocatableResourcesRequest) returns (AllocatableResourcesResponse) {}
    rpc Get(GetPodResourcesRequest) returns (GetPodResourcesResponse) {}
}
```

### نقطهٔ پایانی gRPC ‏`List` {#grpc-endpoint-list}

نقطهٔ پایانی `List` اطلاعاتی دربارهٔ منابع پادهای در حال اجرا ارائه می‌دهد، با جزئیاتی مانند
شناسهٔ CPUهای تخصیص‌یافتهٔ انحصاری، شناسهٔ دستگاه به همان شکلی که افزونه‌های دستگاه گزارش کرده‌اند و شناسهٔ
نود NUMA که این دستگاه‌ها در آن تخصیص یافته‌اند. همچنین برای ماشین‌های مبتنی بر NUMA، شامل
اطلاعاتی دربارهٔ حافظه و hugepageهای رزروشده برای یک کانتینر است.

از کوبرنتیز v1.27 به بعد، نقطهٔ پایانی `List` می‌تواند اطلاعاتی دربارهٔ منابع
پادهای در حال اجرا ارائه دهد که در `ResourceClaims` توسط API ‏`DynamicResourceAllocation` تخصیص یافته‌اند.
از کوبرنتیز v1.34 به بعد، این قابلیت به‌طور پیش‌فرض فعال است.


```gRPC
// ListPodResourcesResponse is the response returned by List function
message ListPodResourcesResponse {
    repeated PodResources pod_resources = 1;
}

// PodResources contains information about the node resources assigned to a pod
message PodResources {
    string name = 1;
    string namespace = 2;
    repeated ContainerResources containers = 3;
}

// ContainerResources contains information about the resources assigned to a container
message ContainerResources {
    string name = 1;
    repeated ContainerDevices devices = 2;
    repeated int64 cpu_ids = 3;
    repeated ContainerMemory memory = 4;
    repeated DynamicResource dynamic_resources = 5;
}

// ContainerMemory contains information about memory and hugepages assigned to a container
message ContainerMemory {
    string memory_type = 1;
    uint64 size = 2;
    TopologyInfo topology = 3;
}

// Topology describes hardware topology of the resource
message TopologyInfo {
        repeated NUMANode nodes = 1;
}

// NUMA representation of NUMA node
message NUMANode {
        int64 ID = 1;
}

// ContainerDevices contains information about the devices assigned to a container
message ContainerDevices {
    string resource_name = 1;
    repeated string device_ids = 2;
    TopologyInfo topology = 3;
}

// DynamicResource contains information about the devices assigned to a container by Dynamic Resource Allocation
message DynamicResource {
    string class_name = 1;
    string claim_name = 2;
    string claim_namespace = 3;
    repeated ClaimResource claim_resources = 4;
}

// ClaimResource contains per-plugin resource information
message ClaimResource {
    repeated CDIDevice cdi_devices = 1 [(gogoproto.customname) = "CDIDevices"];
}

// CDIDevice specifies a CDI device information
message CDIDevice {
    // Fully qualified CDI device name
    // for example: vendor.com/gpu=gpudevice1
    // see more details in the CDI specification:
    // https://github.com/container-orchestrated-devices/container-device-interface/blob/main/SPEC.md
    string name = 1;
}
```
{{< note >}}
cpu_ids در `ContainerResources` در نقطهٔ پایانی `List` متناظر با CPUهای انحصاری تخصیص‌یافته
به یک کانتینر مشخص است. اگر هدف ارزیابی CPUهایی باشد که به مخزن مشترک تعلق دارند، نقطهٔ پایانی `List`
باید همراه با نقطهٔ پایانی `GetAllocatableResources` و به شکلی که در ادامه
توضیح داده شده است استفاده شود:
1. `GetAllocatableResources` را فراخوانی کنید تا فهرستی از همهٔ CPUهای قابل تخصیص به دست آورید
2. `GetCpuIds` را روی همهٔ `ContainerResources` موجود در سیستم فراخوانی کنید
3. همهٔ CPUهای حاصل از فراخوانی‌های `GetCpuIds` را از نتیجهٔ فراخوانی `GetAllocatableResources` کم کنید
{{< /note >}}

### نقطهٔ پایانی gRPC ‏`GetAllocatableResources` {#grpc-endpoint-getallocatableresources}

{{< feature-state state="stable" for_k8s_version="v1.28" >}}

GetAllocatableResources اطلاعاتی دربارهٔ منابعی ارائه می‌دهد که در ابتدا روی نود کارگر در دسترس هستند.
این نقطهٔ پایانی اطلاعاتی بیش از آنچه kubelet به APIServer ارائه می‌دهد فراهم می‌کند.

{{< note >}}
`GetAllocatableResources` فقط باید برای ارزیابی منابع [قابل تخصیص](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable)
روی یک نود استفاده شود. اگر هدف ارزیابی منابع آزاد/تخصیص‌نیافته باشد، باید
همراه با نقطهٔ پایانی List() استفاده شود. نتیجهٔ به‌دست‌آمده از `GetAllocatableResources`
ثابت باقی می‌ماند، مگر اینکه منابع زیربنایی ارائه‌شده به kubelet تغییر کنند. این اتفاق به‌ندرت رخ می‌دهد، اما هنگامی
که رخ دهد (برای مثال: hotplug/hotunplug یا تغییر در سلامت دستگاه)، انتظار می‌رود کلاینت
نقطهٔ پایانی `GetAllocatableResources` را فراخوانی کند.

با این حال، در صورت به‌روزرسانی cpu و/یا حافظه، فراخوانی نقطهٔ پایانی `GetAllocatableResources` کافی نیست
و Kubelet باید دوباره راه‌اندازی شود تا ظرفیت و مقدار قابل تخصیص صحیح منابع را منعکس کند.
{{< /note >}}

```gRPC
// AllocatableResourcesResponses contains information about all the devices known by the kubelet
message AllocatableResourcesResponse {
    repeated ContainerDevices devices = 1;
    repeated int64 cpu_ids = 2;
    repeated ContainerMemory memory = 3;
}
```

`ContainerDevices` اطلاعات توپولوژی را ارائه می‌دهند و اعلام می‌کنند که دستگاه به کدام سلول‌های NUMA
وابستگی (affinity) دارد. سلول‌های NUMA با استفاده از یک شناسهٔ عدد صحیح مبهم (opaque) شناسایی می‌شوند که مقدار آن با
آنچه افزونه‌های دستگاه
[هنگام ثبت خود در kubelet](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager) گزارش می‌دهند سازگار است.

سرویس gRPC از طریق یک سوکت unix در مسیر `pod-resources/kubelet.sock` درون
دایرکتوری ریشهٔ kubelet (معمولاً `/var/lib/kubelet/pod-resources/kubelet.sock`) ارائه می‌شود.
عامل‌های پایش منابع افزونهٔ دستگاه را می‌توان به‌صورت یک دیمن یا به‌صورت یک DaemonSet مستقر کرد.
دایرکتوری استاندارد `pod-resources` درون دایرکتوری ریشهٔ kubelet (معمولاً
`/var/lib/kubelet/pod-resources`) به دسترسی ممتاز نیاز دارد، بنابراین عامل‌های پایش
باید در یک زمینهٔ امنیتی ممتاز اجرا شوند. اگر یک عامل پایش دستگاه به‌صورت
DaemonSet اجرا می‌شود، دایرکتوری `pod-resources` باید به‌عنوان یک
{{< glossary_tooltip term_id="volume" >}} در
[PodSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) عامل پایش دستگاه mount شود.

{{< note >}}

هنگام دسترسی به `pod-resources/kubelet.sock` از یک DaemonSet
یا هر برنامهٔ دیگری که به‌صورت کانتینر روی میزبان مستقر شده و سوکت را به‌عنوان
یک حجم mount می‌کند، روش خوب این است که به‌جای خود فایل سوکت، دایرکتوری `pod-resources`
را mount کنید. این کار تضمین می‌کند
که پس از راه‌اندازی مجدد kubelet، کانتینر بتواند دوباره به این سوکت متصل شود.

روی یک نود لینوکسی معمولی، این به معنای mount کردن `/var/lib/kubelet/pod-resources/`
به‌جای `/var/lib/kubelet/pod-resources/kubelet.sock` است.

mountهای کانتینر از طریق inode‌ای مدیریت می‌شوند که به سوکت یا دایرکتوری ارجاع می‌دهد،
بسته به اینکه چه چیزی mount شده باشد. هنگامی که kubelet دوباره راه‌اندازی می‌شود، سوکت حذف می‌شود
و سوکت جدیدی ایجاد می‌شود، در حالی که دایرکتوری دست‌نخورده باقی می‌ماند.
بنابراین inode اصلی سوکت غیرقابل استفاده می‌شود، اما inode دایرکتوری
همچنان کار خواهد کرد.

{{< /note >}}

### نقطهٔ پایانی gRPC ‏`Get` {#grpc-endpoint-get}

{{< feature-state state="beta" for_k8s_version="v1.34" >}}

نقطهٔ پایانی `Get` اطلاعاتی دربارهٔ منابع یک Pod در حال اجرا ارائه می‌دهد. این نقطهٔ پایانی اطلاعاتی
مشابه آنچه در نقطهٔ پایانی `List` توضیح داده شد ارائه می‌کند. نقطهٔ پایانی `Get` به `PodName`
و `PodNamespace` مربوط به Pod در حال اجرا نیاز دارد.

```gRPC
// GetPodResourcesRequest contains information about the pod
message GetPodResourcesRequest {
    string pod_name = 1;
    string pod_namespace = 2;
}
```

نقطهٔ پایانی `Get` می‌تواند اطلاعات Pod مرتبط با منابع پویایی را ارائه دهد
که توسط API تخصیص پویای منابع تخصیص یافته‌اند.
از کوبرنتیز v1.34 به بعد، این قابلیت به‌طور پیش‌فرض فعال است.

## یکپارچگی افزونهٔ دستگاه با Topology Manager {#device-plugin-integration-with-the-topology-manager}

{{< feature-state for_k8s_version="v1.27" state="stable" >}}

Topology Manager جزئی از Kubelet است که اجازه می‌دهد منابع به شیوه‌ای هم‌راستا با توپولوژی
هماهنگ شوند. برای این منظور، API افزونهٔ دستگاه گسترش یافت تا یک
struct با نام `TopologyInfo` را شامل شود.

```gRPC
message TopologyInfo {
    repeated NUMANode nodes = 1;
}

message NUMANode {
    int64 ID = 1;
}
```

افزونه‌های دستگاهی که می‌خواهند از Topology Manager بهره ببرند، می‌توانند یک struct ‏TopologyInfo
پرشده را به‌عنوان بخشی از ثبت دستگاه، همراه با شناسه‌های دستگاه و وضعیت سلامت دستگاه، بازگردانند.
سپس device manager از این اطلاعات برای مشورت با Topology Manager و اتخاذ
تصمیمات تخصیص منابع استفاده می‌کند.

`TopologyInfo` از تنظیم فیلد `nodes` به `nil` یا به فهرستی از نودهای NUMA پشتیبانی می‌کند. این
امکان به افزونهٔ دستگاه اجازه می‌دهد دستگاهی را اعلام کند که چند نود NUMA را در بر می‌گیرد.

تنظیم `TopologyInfo` به `nil` یا ارائهٔ فهرستی خالی از نودهای NUMA برای یک دستگاه مشخص
نشان می‌دهد که افزونهٔ دستگاه هیچ ترجیحی برای وابستگی NUMA آن دستگاه ندارد.

مثالی از یک struct ‏`TopologyInfo` که توسط یک افزونهٔ دستگاه برای یک دستگاه پر شده است:

```
pluginapi.Device{ID: "25102017", Health: pluginapi.Healthy, Topology:&pluginapi.TopologyInfo{Nodes: []*pluginapi.NUMANode{&pluginapi.NUMANode{ID: 0,},}}}
```

## نمونه‌هایی از افزونه‌های دستگاه {#examples}

{{% thirdparty-content %}}

در اینجا چند نمونه از پیاده‌سازی‌های افزونهٔ دستگاه آمده است:

* [Akri](https://github.com/project-akri/akri) که به شما اجازه می‌دهد دستگاه‌های پایانی ناهمگون (مانند دوربین‌های IP و دستگاه‌های USB) را به‌آسانی در دسترس قرار دهید.
* [افزونهٔ دستگاه AMD GPU](https://github.com/ROCm/k8s-device-plugin)
* [افزونهٔ دستگاه عمومی](https://github.com/squat/generic-device-plugin) برای دستگاه‌های عمومی لینوکس و دستگاه‌های USB
* [HAMi](https://github.com/Project-HAMi/HAMi) برای میان‌افزار مجازی‌سازی محاسبات ناهمگون هوش مصنوعی (برای مثال، NVIDIA، Cambricon، Hygon، Iluvatar، MThreads، Ascend، Metax)
* [افزونه‌های دستگاه Intel](https://github.com/intel/intel-device-plugins-for-kubernetes) برای
  دستگاه‌های Intel GPU، FPGA، QAT، VPU، SGX، DSA، DLB و IAA
* [افزونه‌های دستگاه KubeVirt](https://github.com/kubevirt/kubernetes-device-plugins) برای
  مجازی‌سازی با پشتیبانی سخت‌افزاری
* [افزونهٔ دستگاه NVIDIA GPU](https://github.com/NVIDIA/k8s-device-plugin)، افزونهٔ دستگاه رسمی
  NVIDIA برای در دسترس قرار دادن GPUهای NVIDIA و پایش سلامت GPU
* [افزونهٔ دستگاه NVIDIA GPU برای Container-Optimized OS](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/cmd/nvidia_gpu)
* [افزونهٔ دستگاه RDMA](https://github.com/hustcat/k8s-rdma-device-plugin)
* [افزونهٔ دستگاه SocketCAN](https://github.com/collabora/k8s-socketcan)
* [افزونهٔ دستگاه Solarflare](https://github.com/vikaschoudhary16/sfc-device-plugin)
* [افزونهٔ دستگاه شبکهٔ SR-IOV](https://github.com/intel/sriov-network-device-plugin)
* [افزونه‌های دستگاه Xilinx FPGA](https://github.com/Xilinx/FPGA_as_a_Service/tree/master/k8s-device-plugin) برای دستگاه‌های Xilinx FPGA

## {{% heading "whatsnext" %}}

* دربارهٔ [زمان‌بندی منابع GPU](/docs/tasks/manage-gpus/scheduling-gpus/) با استفاده از افزونه‌های
  دستگاه بیاموزید
* دربارهٔ [اعلام منابع توسعه‌یافته](/docs/tasks/administer-cluster/extended-resource-node/)
  روی یک نود بیاموزید
* دربارهٔ [Topology Manager](/docs/tasks/administer-cluster/topology-manager/) بیاموزید
* دربارهٔ استفاده از [شتاب‌دهی سخت‌افزاری برای TLS ingress](/blog/2019/04/24/hardware-accelerated-ssl/tls-termination-in-ingress-controllers-using-kubernetes-device-plugins-and-runtimeclass/)
  در کوبرنتیز بخوانید
* دربارهٔ [تخصیص منابع توسعه‌یافته توسط DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#extended-resource) بیشتر بخوانید
