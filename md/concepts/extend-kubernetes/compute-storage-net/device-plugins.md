---
title: افزونه‌های دستگاه
description: >
  با افزونه‌های دستگاه می‌توانید کلاستر خود را برای پشتیبانی از دستگاه‌ها یا منابعی پیکربندی کنید
  که به راه‌اندازی مختص فروشنده نیاز دارند، مانند GPUها، NICها، FPGAها یا حافظهٔ اصلی غیرفرار.
content_type: concept
weight: 20
---

<!-- overview -->
{{< feature-state for_k8s_version="v1.26" state="stable" >}}

کوبرنتیز چارچوبی برای افزونه‌های دستگاه (device plugin) فراهم می‌کند. با این چارچوب می‌توانید منابع سخت‌افزاری سیستم را به {{< glossary_tooltip term_id="kubelet" >}} اعلام کنید.

فروشندگان به‌جای سفارشی‌سازی کد خود کوبرنتیز، می‌توانند یک افزونهٔ دستگاه پیاده‌سازی کنند. شما این افزونه را یا به‌صورت دستی یا به‌صورت یک {{< glossary_tooltip term_id="daemonset" >}} مستقر می‌کنید. دستگاه‌های هدف شامل GPUها، NICهای پرکارایی، FPGAها، آداپتورهای InfiniBand و سایر منابع محاسباتی مشابهی هستند که ممکن است به راه‌اندازی اولیه و پیکربندی مختص فروشنده نیاز داشته باشند.

<!-- body -->

## ثبت افزونهٔ دستگاه

سرویس gRPC با نام `Registration` را kubelet در اختیار قرار می‌دهد:

```gRPC
service Registration {
	rpc Register(RegisterRequest) returns (Empty) {}
}
```

یک افزونهٔ دستگاه می‌تواند از طریق این سرویس gRPC خود را در kubelet ثبت کند. افزونهٔ دستگاه هنگام ثبت باید موارد زیر را ارسال کند:

* نام سوکت یونیکس (Unix socket) خود.
* نسخه‌ای از API افزونهٔ دستگاه که افزونه بر اساس آن ساخته شده است.
* مقدار `ResourceName` که می‌خواهد اعلام کند. این مقدار باید از
  [طرح نام‌گذاری منابع توسعه‌یافته](/docs/concepts/configuration/manage-resources-containers/#extended-resources)
  و به شکل `vendor-domain/resourcetype` پیروی کند.
  (برای مثال، یک GPU از NVIDIA با نام `nvidia.com/gpu` اعلام می‌شود.)

پس از ثبت موفق، افزونهٔ دستگاه فهرست دستگاه‌هایی را که مدیریت می‌کند برای kubelet می‌فرستد. از آن پس kubelet مسئول است این منابع را، به‌عنوان بخشی از به‌روزرسانی وضعیت نود، به سرور API اعلام کند. برای مثال، پس از آنکه یک افزونهٔ دستگاه منبع `hardware-vendor.example/foo` را در kubelet ثبت کرد و دو دستگاه سالم را روی یک نود گزارش داد، وضعیت نود به‌روزرسانی می‌شود تا نشان دهد ۲ دستگاه «Foo» روی آن نود نصب شده و در دسترس است.

سپس کاربران می‌توانند دستگاه‌ها را به‌عنوان بخشی از مشخصات Pod درخواست کنند (به [`container`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container) مراجعه کنید). درخواست منابع توسعه‌یافته مشابه شیوهٔ مدیریت درخواست‌ها (requests) و محدودیت‌ها (limits) برای سایر منابع است، با این تفاوت‌ها:
* منابع توسعه‌یافته فقط به‌صورت منابع عدد صحیح پشتیبانی می‌شوند و نمی‌توان آن‌ها را بیش از ظرفیت تخصیص داد (overcommit).
* دستگاه‌ها را نمی‌توان میان کانتینرها به اشتراک گذاشت.

### مثال {#example-pod}

فرض کنید در یک کلاستر کوبرنتیز، افزونهٔ دستگاهی اجرا می‌شود که منبع `hardware-vendor.example/foo` را روی برخی نودها اعلام می‌کند. در ادامه نمونه‌ای از یک Pod آمده است که این منبع را برای اجرای یک بار کاری نمایشی درخواست می‌کند:

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

1. راه‌اندازی اولیه. در این مرحله، افزونهٔ دستگاه راه‌اندازی اولیه و پیکربندی مختص فروشنده را انجام می‌دهد تا از آماده بودن دستگاه‌ها اطمینان حاصل کند.

1. افزونه یک سرویس gRPC را با یک سوکت یونیکس در مسیر میزبان `/var/lib/kubelet/device-plugins/` راه‌اندازی می‌کند که رابط‌های زیر را پیاده‌سازی می‌کند (این مسیر به‌صورت ثابت در کد تعریف شده است و نه فلگ `--root-dir` در kubelet و نه هیچ پیکربندی دیگری بر آن اثری ندارد):

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
   لازم نیست افزونه‌ها برای `GetPreferredAllocation()` یا `PreStartContainer()` پیاده‌سازی کاربردی ارائه دهند. فلگ‌هایی که در دسترس بودن این فراخوانی‌ها را نشان می‌دهند، در صورت وجود، باید در پیام `DevicePluginOptions` تنظیم شوند؛ این پیام در پاسخ به فراخوانی `GetDevicePluginOptions()` بازگردانده می‌شود. پیش از فراخوانی مستقیم هر یک از این توابع اختیاری، `kubelet` همیشه `GetDevicePluginOptions()` را فراخوانی می‌کند تا ببیند کدام‌یک در دسترس هستند.
   {{< /note >}}

1. افزونه از طریق سوکت یونیکس در مسیر میزبان `/var/lib/kubelet/device-plugins/kubelet.sock` خود را در kubelet ثبت می‌کند.

   {{< note >}}
   ترتیب این گردش کار اهمیت دارد. برای ثبت موفق، افزونه حتماً باید پیش از ثبت خود در kubelet، ارائهٔ سرویس gRPC را آغاز کرده باشد.
   {{< /note >}}

1. پس از ثبت موفق، افزونهٔ دستگاه در حالت سرویس‌دهی اجرا می‌شود. در این حالت، افزونه پیوسته سلامت دستگاه‌ها را پایش می‌کند و هر تغییری را در وضعیت دستگاه‌ها به kubelet گزارش می‌دهد. پاسخ‌گویی به درخواست‌های gRPC از نوع `Allocate` نیز بر عهدهٔ آن است. افزونهٔ دستگاه ممکن است در طول `Allocate` آماده‌سازی‌های مختص دستگاه را انجام دهد؛ برای مثال، پاک‌سازی GPU یا راه‌اندازی اولیهٔ QRNG. اگر این عملیات موفق باشد، افزونهٔ دستگاه یک `AllocateResponse` بازمی‌گرداند که پیکربندی‌های محیط اجرای کانتینر را برای دسترسی به دستگاه‌های تخصیص‌یافته در بر دارد. سپس kubelet این اطلاعات را به محیط اجرای کانتینر منتقل می‌کند.

   هر `AllocateResponse` شامل صفر یا چند آبجکت `ContainerAllocateResponse` است. افزونهٔ دستگاه در این آبجکت‌ها تغییراتی را تعریف می‌کند که باید در تعریف کانتینر اعمال شوند تا دسترسی به دستگاه فراهم شود. این تغییرات عبارت‌اند از:

   * [حاشیه‌نویسی‌ها (annotations)](/docs/concepts/overview/working-with-objects/annotations/)
   * فایل‌های دستگاه (device nodes)
   * متغیرهای محیطی
   * اتصال‌ها (mounts)
   * نام‌های کامل دستگاه CDI

   {{< note >}}
   برای آنکه Device Manager (مدیر دستگاه) بتواند نام‌های کامل دستگاه CDI را پردازش کند، باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `DevicePluginCDIDevices` هم در kubelet و هم در kube-apiserver فعال باشد. این قابلیت در نسخهٔ v1.28 کوبرنتیز به‌صورت آلفا اضافه شد، در v1.29 به بتا و در v1.31 به GA ارتقا یافت.
   {{< /note >}}

### مدیریت راه‌اندازی مجدد kubelet

از افزونهٔ دستگاه انتظار می‌رود راه‌اندازی مجدد kubelet را تشخیص دهد و خود را دوباره در نمونهٔ جدید kubelet ثبت کند. هر نمونهٔ جدید kubelet هنگام شروع، همهٔ سوکت‌های یونیکس موجود در مسیر `/var/lib/kubelet/device-plugins` (مسیر ثابت افزونه‌های دستگاه) را حذف می‌کند. افزونهٔ دستگاه می‌تواند حذف سوکت یونیکس خود را پایش کند و با رخ دادن چنین رویدادی، خود را دوباره ثبت کند.

### افزونهٔ دستگاه و دستگاه‌های ناسالم

گاهی دستگاه‌ها از کار می‌افتند یا خاموش می‌شوند. در این حالت، افزونهٔ دستگاه مسئول است kubelet را با استفاده از API مربوط به `ListAndWatchResponse` از این وضعیت آگاه کند.

وقتی دستگاهی ناسالم علامت‌گذاری شود، kubelet تعداد قابل‌تخصیص (allocatable) این منبع را روی نود کاهش می‌دهد تا نشان دهد چند دستگاه برای زمان‌بندی Podهای جدید قابل استفاده است. تعداد ظرفیت (capacity) این منبع تغییری نمی‌کند.

آن دسته از Podهایی که به دستگاه‌های خراب تخصیص داده شده بودند، همچنان به همان دستگاه تخصیص‌یافته باقی می‌مانند. معمولاً کدی که به دستگاه وابسته است شروع به خطا دادن می‌کند. در این حالت، اگر `restartPolicy` آن Pod برابر `Always` نباشد، ممکن است Pod به فاز Failed برود؛ در غیر این صورت، وارد حلقهٔ خرابی (crash loop) می‌شود.

پیش از نسخهٔ v1.31 کوبرنتیز، راه تشخیص اینکه آیا یک Pod با دستگاه خراب مرتبط است یا نه، استفاده از [API مربوط به PodResources](#monitoring-device-plugin-resources) بود.

{{< feature-state feature_gate_name="ResourceHealthStatus" >}}

وقتی feature gate با نام `ResourceHealthStatus` فعال باشد (این قابلیت از نسخهٔ v1.36 در وضعیت بتا است و به‌طور پیش‌فرض فعال است)، فیلد `allocatedResourcesStatus` به وضعیت هر کانتینر، درون `.status` هر Pod، افزوده می‌شود. فیلد `allocatedResourcesStatus` اطلاعات سلامت هر دستگاهی را که به کانتینر تخصیص داده شده است گزارش می‌دهد. هر مدخل سلامت منبع می‌تواند یک فیلد اختیاری `message` نیز داشته باشد که توضیحات بیشتری را به زبانی خوانا برای انسان دربارهٔ وضعیت سلامت ارائه می‌دهد، مانند جزئیات خطا یا دلایل خرابی.

برای یک Pod ناموفق، یا هنگامی که به وجود خطایی مشکوک هستید، می‌توانید از این وضعیت استفاده کنید تا دریابید آیا رفتار Pod ممکن است با خرابی دستگاه مرتبط باشد یا نه. برای مثال، اگر یک شتاب‌دهنده رویداد دمای بیش از حد را گزارش دهد، فیلد `allocatedResourcesStatus` ممکن است این موضوع را نشان دهد.


## استقرار افزونهٔ دستگاه

می‌توانید افزونهٔ دستگاه را به‌صورت یک DaemonSet، به‌صورت یک بسته برای سیستم‌عامل نود، یا به‌صورت دستی مستقر کنید.

دایرکتوری استاندارد `/var/lib/kubelet/device-plugins` (که در kubelet به‌صورت ثابت تعریف شده است) به دسترسی ممتاز نیاز دارد؛ بنابراین افزونهٔ دستگاه باید در یک زمینهٔ امنیتی ممتاز (privileged security context) اجرا شود. اگر افزونهٔ دستگاه را به‌صورت DaemonSet مستقر می‌کنید، مسیر `/var/lib/kubelet/device-plugins` باید به‌صورت یک {{< glossary_tooltip term_id="volume" >}} در [PodSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) افزونه متصل (mount) شود.

اگر رویکرد DaemonSet را انتخاب کنید، می‌توانید برای این کارها به کوبرنتیز تکیه کنید: قرار دادن Pod افزونهٔ دستگاه روی نودها، راه‌اندازی مجدد Pod دیمن پس از خرابی، و کمک به خودکارسازی ارتقاها.

## سازگاری API

پیش‌تر، طرح نسخه‌گذاری ایجاب می‌کرد که نسخهٔ API افزونهٔ دستگاه دقیقاً با نسخهٔ kubelet مطابقت داشته باشد. از زمانی که این قابلیت در نسخهٔ v1.12 به بتا ارتقا یافت، این دیگر یک الزام قطعی نیست. این API نسخه‌گذاری شده است و از زمان ارتقای این قابلیت به بتا پایدار بوده است. به همین دلیل، ارتقای kubelet باید بدون مشکل انجام شود؛ با این حال، ممکن است پیش از پایدارسازی همچنان تغییراتی در API رخ دهد و از این رو تضمینی وجود ندارد که ارتقاها بدون ناسازگاری انجام شوند.

{{< note >}}
اگرچه مؤلفهٔ Device Manager در کوبرنتیز قابلیتی با دسترس‌پذیری عمومی (GA) است، _API افزونهٔ دستگاه_ پایدار نیست. برای اطلاعات دربارهٔ API افزونهٔ دستگاه و سازگاری نسخه‌ها، [نسخه‌های API افزونهٔ دستگاه](/docs/reference/node/device-plugin-api-versions/) را بخوانید.
{{< /note >}}

کوبرنتیز به‌عنوان یک پروژه به توسعه‌دهندگان افزونه‌های دستگاه توصیه می‌کند که:

* تغییرات API افزونهٔ دستگاه را در نسخه‌های آینده دنبال کنند.
* از چند نسخهٔ API افزونهٔ دستگاه پشتیبانی کنند تا سازگاری رو به عقب و رو به جلو حفظ شود.

برای اجرای افزونه‌های دستگاه روی نودهایی که باید به نسخه‌ای از کوبرنتیز با نسخهٔ جدیدتری از API افزونهٔ دستگاه ارتقا یابند، پیش از ارتقای این نودها، افزونه‌های دستگاه خود را طوری ارتقا دهید که از هر دو نسخه پشتیبانی کنند. با این رویکرد، تخصیص دستگاه‌ها در طول ارتقا بدون وقفه ادامه خواهد یافت.

## پایش منابع افزونه‌های دستگاه

{{< feature-state for_k8s_version="v1.28" state="stable" >}}

برای پایش منابعی که افزونه‌های دستگاه فراهم می‌کنند، عامل‌های پایش (monitoring agents) باید بتوانند مجموعهٔ دستگاه‌های در حال استفاده روی نود را کشف کنند و فراداده‌ای به دست آورند که مشخص کند هر معیار (metric) باید به کدام کانتینر مرتبط شود. معیارهای [Prometheus](https://prometheus.io/) که عامل‌های پایش دستگاه ارائه می‌دهند باید از [رهنمودهای ابزارگذاری کوبرنتیز](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-instrumentation/metric-instrumentation.md) پیروی کنند و کانتینرها را با برچسب‌های Prometheus با نام‌های `pod`، `namespace` و `container` شناسایی کنند.

برای کشف دستگاه‌های در حال استفاده و ارائهٔ فراداده برای این دستگاه‌ها، kubelet یک سرویس gRPC فراهم می‌کند:

```gRPC
// PodResourcesLister is a service provided by the kubelet that provides information about the
// node resources consumed by pods and containers on the node
service PodResourcesLister {
    rpc List(ListPodResourcesRequest) returns (ListPodResourcesResponse) {}
    rpc GetAllocatableResources(AllocatableResourcesRequest) returns (AllocatableResourcesResponse) {}
    rpc Get(GetPodResourcesRequest) returns (GetPodResourcesResponse) {}
}
```

### نقطهٔ پایانی gRPC با نام `List` {#grpc-endpoint-list}

نقطهٔ پایانی `List` اطلاعاتی دربارهٔ منابع Podهای در حال اجرا ارائه می‌دهد؛ از جمله جزئیاتی مانند شناسهٔ CPUهایی که به‌طور انحصاری تخصیص یافته‌اند، شناسهٔ دستگاه همان‌گونه که افزونه‌های دستگاه گزارش کرده‌اند، و شناسهٔ نود NUMA که این دستگاه‌ها در آن تخصیص یافته‌اند. همچنین در ماشین‌های مبتنی بر NUMA، اطلاعات مربوط به حافظه و hugepageهای رزروشده برای هر کانتینر را نیز در بر دارد.

از نسخهٔ v1.27 کوبرنتیز، نقطهٔ پایانی `List` می‌تواند اطلاعاتی دربارهٔ آن دسته از منابع Podهای در حال اجرا ارائه دهد که از طریق API مربوط به `DynamicResourceAllocation` در `ResourceClaims` تخصیص یافته‌اند. از نسخهٔ v1.34 کوبرنتیز، این قابلیت به‌طور پیش‌فرض فعال است.


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
مقدار cpu_ids در `ContainerResources` نقطهٔ پایانی `List` با CPUهای انحصاری‌ای متناظر است که به یک کانتینر مشخص تخصیص یافته‌اند. اگر هدف، ارزیابی CPUهایی باشد که به مخزن مشترک (shared pool) تعلق دارند، باید نقطهٔ پایانی `List` را همراه با نقطهٔ پایانی `GetAllocatableResources` به کار برد، همان‌طور که در ادامه توضیح داده شده است:
1. تابع `GetAllocatableResources` را فراخوانی کنید تا فهرست همهٔ CPUهای قابل‌تخصیص را به دست آورید.
2. تابع `GetCpuIds` را روی همهٔ `ContainerResources`های سیستم فراخوانی کنید.
3. همهٔ CPUهای حاصل از فراخوانی‌های `GetCpuIds` را از نتیجهٔ فراخوانی `GetAllocatableResources` کم کنید.
{{< /note >}}

### نقطهٔ پایانی gRPC با نام `GetAllocatableResources` {#grpc-endpoint-getallocatableresources}

{{< feature-state state="stable" for_k8s_version="v1.28" >}}

نقطهٔ پایانی GetAllocatableResources اطلاعاتی دربارهٔ منابعی ارائه می‌دهد که در ابتدا روی نود کارگر در دسترس هستند. این نقطهٔ پایانی اطلاعاتی بیش از آنچه kubelet به APIServer صادر می‌کند در اختیار می‌گذارد.

{{< note >}}
از `GetAllocatableResources` فقط باید برای ارزیابی منابع [قابل‌تخصیص](/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) (allocatable) یک نود استفاده کرد. اگر هدف ارزیابی منابع آزاد یا تخصیص‌نیافته است، باید آن را همراه با نقطهٔ پایانی List() به کار برد. نتیجه‌ای که از `GetAllocatableResources` به دست می‌آید ثابت می‌ماند، مگر آنکه منابع زیربنایی که در اختیار kubelet قرار گرفته‌اند تغییر کنند. این اتفاق به‌ندرت رخ می‌دهد، اما هنگامی که رخ دهد (برای نمونه: اتصال یا جداسازی داغ (hotplug/hotunplug) یا تغییر وضعیت سلامت دستگاه)، انتظار می‌رود کلاینت نقطهٔ پایانی `GetAllocatableResources` را فراخوانی کند.

با این حال، در صورت به‌روزرسانی CPU یا حافظه یا هر دو، فراخوانی نقطهٔ پایانی `GetAllocatableResources` کافی نیست و برای بازتاب ظرفیت و مقدار قابل‌تخصیص صحیح منابع، باید Kubelet را دوباره راه‌اندازی کرد.
{{< /note >}}

```gRPC
// AllocatableResourcesResponses contains information about all the devices known by the kubelet
message AllocatableResourcesResponse {
    repeated ContainerDevices devices = 1;
    repeated int64 cpu_ids = 2;
    repeated ContainerMemory memory = 3;
}
```

ساختار `ContainerDevices` اطلاعات توپولوژی را نیز ارائه می‌دهد و مشخص می‌کند که دستگاه به کدام سلول‌های NUMA وابستگی (affinity) دارد. سلول‌های NUMA با یک شناسهٔ عددی مبهم (opaque) شناسایی می‌شوند که مقدار آن با آنچه پلاگین‌های دستگاه [هنگام ثبت خود در kubelet](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager) گزارش می‌کنند سازگار است.

این سرویس gRPC از طریق یک سوکت یونیکس در مسیر `pod-resources/kubelet.sock` درون دایرکتوری ریشهٔ kubelet (معمولاً `/var/lib/kubelet/pod-resources/kubelet.sock`) ارائه می‌شود. عامل‌های پایش منابع پلاگین دستگاه را می‌توان به‌صورت یک daemon یا یک DaemonSet مستقر کرد. دسترسی به دایرکتوری استاندارد `pod-resources` درون دایرکتوری ریشهٔ kubelet (معمولاً `/var/lib/kubelet/pod-resources`) به مجوز ممتاز نیاز دارد؛ بنابراین عامل‌های پایش باید در یک زمینهٔ امنیتی ممتاز (privileged security context) اجرا شوند. اگر عامل پایش دستگاه به‌صورت DaemonSet اجرا می‌شود، دایرکتوری `pod-resources` باید به‌عنوان یک {{< glossary_tooltip term_id="volume" >}} در [PodSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) عامل پایش دستگاه mount شود.

{{< note >}}

هنگام دسترسی به `pod-resources/kubelet.sock` از یک DaemonSet یا هر برنامهٔ دیگری که به‌صورت کانتینر روی میزبان مستقر شده و سوکت را به‌عنوان حجم mount می‌کند، بهتر است به‌جای خود فایل سوکت، دایرکتوری `pod-resources` را mount کنید. با این کار اطمینان حاصل می‌شود که کانتینر پس از راه‌اندازی دوبارهٔ kubelet می‌تواند دوباره به این سوکت متصل شود.

روی یک نود لینوکسی معمولی، این به معنای mount کردن `/var/lib/kubelet/pod-resources/` به‌جای `/var/lib/kubelet/pod-resources/kubelet.sock` است.

‏mountهای کانتینر، بسته به آنچه mount شده است، از طریق inode ارجاع‌دهنده به سوکت یا دایرکتوری مدیریت می‌شوند. هنگامی که kubelet دوباره راه‌اندازی می‌شود، سوکت حذف و سوکت جدیدی ایجاد می‌شود، در حالی که دایرکتوری دست‌نخورده باقی می‌ماند. در نتیجه inode اصلی سوکت غیرقابل‌استفاده می‌شود، اما inode دایرکتوری همچنان کار خواهد کرد.

{{< /note >}}

### نقطهٔ پایانی gRPC با نام `Get` {#grpc-endpoint-get}

{{< feature-state state="beta" for_k8s_version="v1.34" >}}

نقطهٔ پایانی `Get` اطلاعاتی دربارهٔ منابع یک Pod در حال اجرا ارائه می‌دهد. اطلاعاتی که این نقطهٔ پایانی در اختیار می‌گذارد مشابه اطلاعاتی است که در نقطهٔ پایانی `List` توضیح داده شد. نقطهٔ پایانی `Get` به `PodName` و `PodNamespace` مربوط به Pod در حال اجرا نیاز دارد.

```gRPC
// GetPodResourcesRequest contains information about the pod
message GetPodResourcesRequest {
    string pod_name = 1;
    string pod_namespace = 2;
}
```

نقطهٔ پایانی `Get` می‌تواند اطلاعات Pod مربوط به منابع پویایی را که از طریق API تخصیص پویای منابع (dynamic resource allocation) تخصیص یافته‌اند ارائه دهد. از کوبرنتیز v1.34، این قابلیت به‌طور پیش‌فرض فعال است.

## یکپارچگی پلاگین دستگاه با مدیر توپولوژی

{{< feature-state for_k8s_version="v1.27" state="stable" >}}

مدیر توپولوژی (Topology Manager) یکی از مؤلفه‌های Kubelet است که امکان هماهنگ‌سازی منابع را به شیوه‌ای همسو با توپولوژی فراهم می‌کند. برای این منظور، API پلاگین دستگاه گسترش یافت تا ساختار `TopologyInfo` را در بر بگیرد.

```gRPC
message TopologyInfo {
    repeated NUMANode nodes = 1;
}

message NUMANode {
    int64 ID = 1;
}
```

پلاگین‌های دستگاهی که می‌خواهند از مدیر توپولوژی بهره ببرند، می‌توانند هنگام ثبت دستگاه، یک ساختار TopologyInfo پرشده را همراه با شناسه‌های دستگاه و وضعیت سلامت آن بازگردانند. سپس مدیر دستگاه از این اطلاعات برای مشورت با مدیر توپولوژی و گرفتن تصمیم‌های مربوط به تخصیص منابع استفاده می‌کند.

ساختار `TopologyInfo` از تنظیم فیلد `nodes` با مقدار `nil` یا فهرستی از نودهای NUMA پشتیبانی می‌کند. با این کار، پلاگین دستگاه می‌تواند دستگاهی را اعلام کند که چندین نود NUMA را در بر می‌گیرد.

تنظیم `TopologyInfo` روی `nil` یا ارائهٔ فهرستی خالی از نودهای NUMA برای یک دستگاه مشخص، نشان می‌دهد که پلاگین دستگاه برای آن دستگاه هیچ ترجیحی از نظر وابستگی NUMA ندارد.

نمونه‌ای از یک ساختار `TopologyInfo` که یک پلاگین دستگاه برای یک دستگاه پر کرده است:

```
pluginapi.Device{ID: "25102017", Health: pluginapi.Healthy, Topology:&pluginapi.TopologyInfo{Nodes: []*pluginapi.NUMANode{&pluginapi.NUMANode{ID: 0,},}}}
```

## نمونه‌هایی از پلاگین‌های دستگاه {#examples}

{{% thirdparty-content %}}

در ادامه چند نمونه از پیاده‌سازی‌های پلاگین دستگاه آمده است:

* ‏[Akri](https://github.com/project-akri/akri)، که به شما امکان می‌دهد دستگاه‌های لبه‌ای ناهمگون (مانند دوربین‌های IP و دستگاه‌های USB) را به‌سادگی در دسترس قرار دهید.
* [پلاگین دستگاه AMD GPU](https://github.com/ROCm/k8s-device-plugin)
* [پلاگین دستگاه عمومی](https://github.com/squat/generic-device-plugin) برای دستگاه‌های عمومی لینوکس و دستگاه‌های USB
* ‏[HAMi](https://github.com/Project-HAMi/HAMi)، میان‌افزار مجازی‌سازی محاسبات ناهمگون هوش مصنوعی (برای نمونه NVIDIA، Cambricon، Hygon، Iluvatar، MThreads، Ascend و Metax)
* [پلاگین‌های دستگاه Intel](https://github.com/intel/intel-device-plugins-for-kubernetes) برای دستگاه‌های GPU، FPGA، QAT، VPU، SGX، DSA، DLB و IAA شرکت Intel
* [پلاگین‌های دستگاه KubeVirt](https://github.com/kubevirt/kubernetes-device-plugins) برای مجازی‌سازی با پشتیبانی سخت‌افزاری
* [پلاگین دستگاه NVIDIA GPU](https://github.com/NVIDIA/k8s-device-plugin)، پلاگین دستگاه رسمی NVIDIA برای در دسترس قرار دادن GPUهای NVIDIA و پایش سلامت آن‌ها
* [پلاگین دستگاه NVIDIA GPU برای Container-Optimized OS](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/cmd/nvidia_gpu)
* [پلاگین دستگاه RDMA](https://github.com/hustcat/k8s-rdma-device-plugin)
* [پلاگین دستگاه SocketCAN](https://github.com/collabora/k8s-socketcan)
* [پلاگین دستگاه Solarflare](https://github.com/vikaschoudhary16/sfc-device-plugin)
* [پلاگین دستگاه شبکهٔ SR-IOV](https://github.com/intel/sriov-network-device-plugin)
* [پلاگین‌های دستگاه Xilinx FPGA](https://github.com/Xilinx/FPGA_as_a_Service/tree/master/k8s-device-plugin) برای دستگاه‌های FPGA شرکت Xilinx

## {{% heading "whatsnext" %}}

* دربارهٔ [زمان‌بندی منابع GPU](/docs/tasks/manage-gpus/scheduling-gpus/) با استفاده از پلاگین‌های دستگاه بیاموزید.
* دربارهٔ [اعلام منابع توسعه‌یافته](/docs/tasks/administer-cluster/extended-resource-node/) روی یک نود بیاموزید.
* دربارهٔ [مدیر توپولوژی](/docs/tasks/administer-cluster/topology-manager/) بیاموزید.
* دربارهٔ استفاده از [شتاب‌دهی سخت‌افزاری برای TLS در ingress](/blog/2019/04/24/hardware-accelerated-ssl/tls-termination-in-ingress-controllers-using-kubernetes-device-plugins-and-runtimeclass/) در کوبرنتیز مطالعه کنید.
* دربارهٔ [تخصیص منابع توسعه‌یافته با DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#extended-resource) بیشتر بخوانید.
