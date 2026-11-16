---
reviewers:
- klueska
- pohly
title: مشاهده‌پذیری منابع پویا
content_type: concept
weight: 30
api_metadata:
- apiVersion: "resource.k8s.io/v1alpha3"
  kind: "ResourcePoolStatusRequest"
---

<!-- overview -->

این صفحه توضیح می‌دهد که چگونه می‌توان وضعیت و سلامت منابعی را که با DRA به‌صورت پویا تخصیص داده می‌شوند مشاهده کرد.

<!-- body -->

## مشاهده‌پذیری منابع پویا {#observability-dynamic-resources}

برای بررسی وضعیت منابعی که به‌صورت پویا تخصیص داده شده‌اند، می‌توانید از هر یک از روش‌های زیر استفاده کنید:

* [متریک‌های دستگاه در kubelet](#monitoring-resources)
* [وضعیت ResourceClaim](#resourceclaim-device-status)
* [پایش سلامت دستگاه](#device-health-monitoring)

### متریک‌های دستگاه در kubelet {#monitoring-resources}

با سرویس gRPC به نام `PodResourcesLister` در kubelet می‌توانید دستگاه‌های در حال استفاده را پایش کنید. پیام `DynamicResource` اطلاعاتی مختص تخصیص پویای منابع، مانند نام دستگاه و نام claim، ارائه می‌دهد. برای جزئیات بیشتر، به [پایش منابع افزونه‌های دستگاه](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources) مراجعه کنید.

### وضعیت دستگاه در ResourceClaim {#resourceclaim-device-status}

{{< feature-state feature_gate_name="DRAResourceClaimDeviceStatus" >}}

درایورهای DRA می‌توانند داده‌های [وضعیت دستگاه](/docs/concepts/overview/working-with-objects/#object-spec-and-status) مختص خود را برای هر دستگاه تخصیص‌یافته در فیلد `status.devices` یک ResourceClaim گزارش کنند. برای مثال، درایور ممکن است نشانی‌های IP اختصاص‌یافته به یک دستگاه رابط شبکه را فهرست کند. به‌روزرسانی این فیلد به مجوزهای RBAC مصنوعی (synthetic) خاصی نیاز دارد؛ برای جزئیات، به [راهنمای مقاوم‌سازی - تخصیص پویای منابع](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/) و [مقاوم‌سازی تخصیص پویای منابع در کلاستر](/docs/tasks/administer-cluster/hardening-dra/) مراجعه کنید.

دقت اطلاعاتی که یک درایور به فیلد `status.devices` در ResourceClaim اضافه می‌کند به خود درایور بستگی دارد. درایورها را ارزیابی کنید تا تصمیم بگیرید آیا می‌توانید به این فیلد به‌عنوان تنها منبع اطلاعات دستگاه تکیه کنید یا خیر.

اگر [feature gate با نام `DRAResourceClaimDeviceStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourceClaimDeviceStatus) را غیرفعال کنید، فیلد `status.devices` هنگام ذخیره‌سازی ResourceClaim به‌طور خودکار پاک می‌شود. وضعیت دستگاه در ResourceClaim زمانی پشتیبانی می‌شود که درایور DRA بتواند یک ResourceClaim موجود را که فیلد `status.devices` آن تنظیم شده است به‌روزرسانی کند.

در مثال زیر، فیلد `status.devices` یک ResourceClaim را درایوری (`resource-driver.example.com`) پر کرده است که مسئول مدیریت دستگاه تخصیص‌یافته است:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  name: macvlan-eth0
spec:
...
status:
  allocation:
    devices:
      results:
      - device: eth0
        driver: resource-driver.example.com
        pool: nic-worker-a
        request: macvlan-eth0
        shareID: 8e7acdf9-0290-4ecd-a801-a654b021d2b7
        consumedCapacity:
          resource-driver.example.com/bandwidth: 1G
  devices:
  - conditions:
    - lastTransitionTime: "2025-10-21T08:38:17Z"
      message: Device successfully allocated and assigned to the pod
      reason: NetworkReady
      status: "True"
      type: NetworkReady
    device: eth0
    driver: resource-driver.example.com
    networkData:
      hardwareAddress: 00:01:ec:84:fb:51
      interfaceName: net1
      ips:
      - 10.10.1.2/24
      - 2001:db8::1/64
    pool: nic-worker-a
    shareID: 8e7acdf9-0290-4ecd-a801-a654b021d2b7
```

اگر دستگاهی تخصیص داده نشده باشد، درخواست درایور برای به‌روزرسانی فیلد `status.devices` در ResourceClaim با آن دستگاه رد می‌شود. وقتی تخصیص یک دستگاه لغو می‌شود (یعنی از `status.allocation.devices` حذف می‌شود)، ورودی متناظر آن در `status.devices` به‌طور خودکار حذف می‌شود.

برای جزئیات فیلد `status.devices`، به مرجع API
{{< api-reference page="resource/resource-claim-v1" anchor="ResourceClaimStatus" text="ResourceClaim" >}} مراجعه کنید.

### پایش سلامت دستگاه {#device-health-monitoring}

{{< feature-state feature_gate_name="ResourceHealthStatus" >}}

کوبرنتیز سازوکاری برای پایش و گزارش سلامت منابع زیرساختی‌ای فراهم می‌کند که به‌صورت پویا تخصیص داده شده‌اند. برای برنامه‌های stateful که روی سخت‌افزارهای تخصصی اجرا می‌شوند، دانستن اینکه چه زمانی یک دستگاه از کار افتاده یا ناسالم شده اهمیت حیاتی دارد. همچنین مفید است بدانید آیا دستگاه دوباره بازیابی می‌شود یا خیر.

برای استفاده از این قابلیت، باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/resource-health-status/) با نام `ResourceHealthStatus` فعال باشد (این قابلیت از نسخهٔ v1.36 در مرحلهٔ بتا است و به‌طور پیش‌فرض فعال است) و درایور DRA نیز باید سرویس gRPC با نام `DRAResourceHealth` را پیاده‌سازی کند.

وقتی یک درایور DRA تشخیص دهد که یک دستگاه تخصیص‌یافته ناسالم شده است، این وضعیت را به kubelet گزارش می‌دهد. سپس این اطلاعات سلامت مستقیماً در وضعیت Pod نمایش داده می‌شود. kubelet فیلد `allocatedResourcesStatus` را در وضعیت هر کانتینر پر می‌کند و سلامت هر دستگاهی را که به آن کانتینر اختصاص یافته است به‌تفصیل نشان می‌دهد. هر ورودی سلامت منبع می‌تواند یک فیلد اختیاری `message` نیز داشته باشد که توضیحات خوانا و بیشتری دربارهٔ وضعیت سلامت، مانند جزئیات خطا یا علت‌های خرابی، ارائه می‌دهد.

اگر kubelet در یک بازهٔ زمانی مشخص هیچ به‌روزرسانی سلامتی از درایور DRA دریافت نکند، وضعیت سلامت دستگاه به «Unknown» تغییر می‌کند. درایورهای DRA می‌توانند این مهلت زمانی را به‌صورت جداگانه برای هر دستگاه، با تنظیم فیلد `health_check_timeout_seconds` در پیام gRPC با نام `DeviceHealth`، پیکربندی کنند. اگر این مقدار مشخص نشود، kubelet از مهلت پیش‌فرض ۳۰ ثانیه استفاده می‌کند. به این ترتیب، انواع مختلف سخت‌افزار (برای مثال GPUها، FPGAها یا دستگاه‌های ذخیره‌سازی) می‌توانند متناسب با ویژگی‌های گزارش‌دهی سلامت خود از مقادیر مهلت مناسب استفاده کنند.

این قابلیت دید بسیار مهمی در اختیار کاربران و کنترل‌کننده‌ها قرار می‌دهد تا بتوانند به خرابی‌های سخت‌افزاری واکنش نشان دهند. برای Podای که با خطا مواجه شده است، می‌توانید این وضعیت را بررسی کنید تا مشخص شود آیا خرابی به یک دستگاه ناسالم مربوط بوده است یا خیر.

{{< note >}}
پس از خاتمهٔ یک Pod (برای مثال، در وضعیت Failed)، وضعیت سلامت دستگاه دیگر در وضعیت Pod به‌روزرسانی نمی‌شود.
{{< /note >}}

## وضعیت مخزن منابع {#resource-pool-status}

{{< feature-state feature_gate_name="DRAResourcePoolStatus" >}}

با استفاده از API مربوط به ResourcePoolStatusRequest می‌توانید میزان در دسترس بودن دستگاه‌ها را در مخزن‌های منابع (resource pool) پرس‌وجو کنید. این API نشان می‌دهد که در مخزن‌های منابع DRA کلاستر شما چه تعداد دستگاه در دسترس، تخصیص‌یافته یا غیرقابل‌دسترس هستند.

برای بررسی وضعیت مخزن منابع:

1. یک ResourcePoolStatusRequest ایجاد کنید و در آن نام درایور (الزامی) و در صورت تمایل، حدی برای تعداد مخزن‌های بازگردانده‌شده مشخص کنید. همچنین می‌توانید با تعیین نام یک مخزن، نتیجه را به همان یک مخزن محدود کنید:

   ```yaml
   apiVersion: resource.k8s.io/v1alpha3
   kind: ResourcePoolStatusRequest
   metadata:
     name: check-gpus
   spec:
     driver: example.com/gpu
     # Optional: filter to a specific pool
     # poolName: my-pool
     # Optional: limit number of pools returned (default: 100, max: 1000)
     # limit: 10
   ```

1. منتظر بمانید تا کنترل‌کننده درخواست را پردازش کند:

   ```shell
   kubectl wait --for=condition=Complete resourcepoolstatusrequest/check-gpus --timeout=30s
   ```

1. برای مشاهدهٔ میزان در دسترس بودن مخزن‌ها، وضعیت را بخوانید:

   ```shell
   kubectl get resourcepoolstatusrequest/check-gpus -o yaml
   ```

   وضعیت شامل موارد زیر است:
   - `poolCount`: تعداد کل مخزن‌هایی که با فیلتر مطابقت دارند (اگر فهرست به دلیل حد تعیین‌شده کوتاه شده باشد، ممکن است این عدد از تعداد مخزن‌های فهرست‌شده بیشتر باشد).
   - `pools`: فهرستی از جزئیات مخزن‌ها که هر کدام شامل موارد زیر است:
     - `driver` و `poolName`: مخزن را مشخص می‌کنند.
     - `generation`: آخرین نسل (generation) مخزن که در میان ResourceSliceها مشاهده شده است.
     - `resourceSliceCount`: تعداد ResourceSliceهایی که مخزن را تشکیل می‌دهند.
     - `totalDevices`: تعداد کل دستگاه‌های مخزن.
     - `allocatedDevices`: دستگاه‌هایی که در حال حاضر به claimها تخصیص داده شده‌اند.
     - `availableDevices`: دستگاه‌هایی که برای تخصیص در دسترس هستند
       (totalDevices - allocatedDevices - unavailableDevices).
     - `unavailableDevices`: دستگاه‌هایی که به دلیل taintها یا شرایط دیگر در دسترس نیستند.
     - `nodeName`: نود مرتبط با مخزن، در صورت وجود.
     - `validationError`: زمانی تنظیم می‌شود که داده‌های مخزن به‌طور کامل اعتبارسنجی نشده باشد (برای مثال، در حین انتشار یک نسل جدید). در این حالت، ممکن است فیلدهای شمارش دستگاه تنظیم نشده باشند.
     - `partitionSummary`: برای مخزن‌های [قابل‌پارتیشن‌بندی](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)، قابلیت تخصیص را به تفکیک هر نوع پارتیشن نشان می‌دهد (به [خلاصهٔ پارتیشن‌ها](#resource-pool-partition-summary) مراجعه کنید).
     - `shareableSummary`: برای مخزن‌هایی که [دستگاه‌های اشتراک‌پذیر](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity) دارند، مصرف تجمیعی ظرفیت را نشان می‌دهد (به [خلاصهٔ اشتراک‌پذیری](#resource-pool-shareable-summary) مراجعه کنید).
   - `conditions`: شامل انواع شرط `Complete` (موفقیت) یا `Failed` (خطا) است.

1. پس از پایان کار، درخواست را حذف کنید:

   ```shell
   kubectl delete resourcepoolstatusrequest/check-gpus
   ```

آبجکت‌های ResourcePoolStatusRequest تنها یک بار و توسط یک کنترل‌کننده در kube-controller-manager پردازش می‌شوند. بخش spec پس از ایجاد تغییرناپذیر است و پس از پر شدن وضعیت، کل آبجکت تغییرناپذیر می‌شود. برای دریافت داده‌های به‌روز دربارهٔ در دسترس بودن دستگاه‌ها، درخواست را حذف و دوباره ایجاد کنید. درخواست‌های تکمیل‌شده پس از یک ساعت به‌طور خودکار پاک می‌شوند.

این قابلیت به مجوزهای صریح RBAC روی منبع ResourcePoolStatusRequest نیاز دارد. هیچ‌یک از ClusterRoleهای پیش‌فرض این مجوز را ندارند.

وضعیت مخزن منابع با [feature gate با نام `DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus) در `kube-apiserver` و `kube-controller-manager` کنترل می‌شود.

### خلاصهٔ پارتیشن‌ها {#resource-pool-partition-summary}

{{< feature-state feature_gate_name="DRAPartitionableDevicesType" >}}

یک دستگاه فیزیکی واحد، مانند یک GPU، ممکن است در قالب چند نوع پارتیشن عرضه شود (برای مثال، یک GPU کامل در برابر یک برش MIG با نصف اندازه) که همگی از شمارنده‌های مشترک یکسانی مصرف می‌کنند. از آنجا که این پارتیشن‌ها بر سر ظرفیت زیربنایی یکسانی رقابت می‌کنند، شمارش سادهٔ دستگاه‌ها نشان نمی‌دهد که از هر نوع هنوز چند عدد قابل تخصیص است. برای مخزن‌های [قابل‌پارتیشن‌بندی](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)، نمای `partitionSummary` به این پرسش پاسخ می‌دهد. این نما برای هر نوع پارتیشن موارد زیر را گزارش می‌کند:

- `attribute`: نام کامل ویژگی دستگاه که مقدار آن مبنای گروه‌بندی این ورودی است. این نام همان `spec.partitionTypeAttribute` در ResourceSlice است، یا اگر slice هیچ ویژگی‌ای اعلام نکرده باشد، `spec.defaultPartitionTypeAttribute` در درخواست.
- `type`: مقدار آن ویژگی روی دستگاه (برای مثال، `Full` یا `Half`).
- `total`: تعداد دستگاه‌های این نوع پارتیشن در مخزن.
- `allocatable`: تعداد دستگاه‌های *اضافی* از این نوع پارتیشن که با توجه به مصرف فعلی شمارنده‌های مشترک هنوز می‌توان تخصیص داد.

ویژگی نام‌برده باید از نوع رشته‌ای باشد. اگر ویژگی نوع پارتیشن در یک دستگاه قابل‌پارتیشن‌بندی وجود نداشته باشد یا رشته‌ای نباشد (برای مثال، مقداری از نوع عدد صحیح، بولی یا نسخه باشد)، مخزن به‌جای خلاصهٔ پارتیشن‌ها یک خطای اعتبارسنجی گزارش می‌کند. برای [ویژگی‌های فهرستی](/docs/reference/command-line-tools-reference/feature-gates/#DRAListTypeAttributes) رفتار خاصی وجود ندارد؛ هر ویژگی غیررشته‌ای صرفاً ویژگی معتبری برای نوع پارتیشن به شمار نمی‌آید.

برای تولید این نما، درایور به هر دستگاه قابل‌پارتیشن‌بندی یک ویژگی رشته‌ای می‌دهد که مقدار آن نام نوع پارتیشن است، و نام آن ویژگی را در فیلد `partitionTypeAttribute` در ResourceSlice درج می‌کند:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
# ...
spec:
  # Every partitionable device in this slice carries this attribute; devices
  # that share a value share the same shared-counter cost.
  partitionTypeAttribute: gpu.example.com/profile
```

اگر درایوری هنوز به‌روزرسانی نشده باشد تا `partitionTypeAttribute` را اعلام کند، یک درخواست همچنان می‌تواند با نام بردن از یک ویژگی جایگزین در spec خود، خلاصهٔ پارتیشن‌ها را دریافت کند. مقدار `partitionTypeAttribute` خود slice همواره اولویت دارد و مقدار پیش‌فرض در سطح درخواست فقط برای دستگاه‌هایی اعمال می‌شود که slice آن‌ها چنین ویژگی‌ای اعلام نکرده است:

```yaml
apiVersion: resource.k8s.io/v1alpha3
kind: ResourcePoolStatusRequest
metadata:
  name: check-gpu-partitions
spec:
  driver: gpu.example.com
  # Fallback grouping attribute for slices that don't declare one themselves.
  defaultPartitionTypeAttribute: gpu.example.com/profile
```

اگر نه slice و نه درخواست هیچ ویژگی‌ای را نام نبرده باشند، مخزن قابل‌پارتیشن‌بندی هیچ `partitionSummary`ای گزارش نمی‌کند.

نمای `partitionSummary` با [feature gate با نام `DRAPartitionableDevicesType`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevicesType) در `kube-apiserver` و `kube-controller-manager` کنترل می‌شود. این feature gate به نوبهٔ خود مستلزم فعال بودن feature gateهای [`DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus) و [`DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices) است.

### خلاصهٔ اشتراک‌پذیری {#resource-pool-shareable-summary}

برای مخزن‌هایی که [دستگاه‌های اشتراک‌پذیر](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity) دارند (دستگاه‌هایی که `allowMultipleAllocations` را تنظیم کرده‌اند و چند claim می‌توانند از آن‌ها استفاده کنند)، `shareableSummary` مصرف تجمیعی ظرفیت را در کل مخزن گزارش می‌کند:

- `fullyAvailableDevices`: دستگاه‌های اشتراک‌پذیری که هیچ بخشی از ظرفیت آن‌ها مصرف نشده است.
- `partiallyAvailableDevices`: دستگاه‌های اشتراک‌پذیری که بخشی از ظرفیت آن‌ها، و نه همهٔ آن، مصرف شده است.
- `capacity`: به تفکیک نام هر ظرفیت، مقادیر تجمیعی `total`، `consumed` و `available` (یعنی `total` منهای `consumed` که هرگز منفی نمی‌شود) در کل مخزن.

فیلد `shareableSummary` فقط زمانی پر می‌شود که دست‌کم یکی از دستگاه‌های مخزن اشتراک‌پذیر باشد. این فیلد بخشی از قابلیت [وضعیت مخزن منابع](#resource-pool-status) (یعنی feature gate با نام [`DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)) است و به `DRAPartitionableDevicesType` نیازی ندارد؛ دستگاه‌های اشتراک‌پذیری که خلاصه می‌کند از قابلیت [ظرفیت قابل‌مصرف](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity) می‌آیند.


## فراداده‌های دستگاه DRA در کانتینرها {#device-metadata}

{{< feature-state state="beta" for_k8s_version="v1.37" >}}

درایورهای DRA می‌توانند فراداده‌های دستگاه، مانند ویژگی‌های دستگاه (نشانی‌های گذرگاه PCI یا UUIDهای دستگاه‌های mediated) و پیکربندی شبکه، را در قالب فایل‌های JSON مستقیماً در اختیار کانتینرها قرار دهند. به این ترتیب، برنامه‌ها می‌توانند بدون پرس‌وجو از API کوبرنتیز یا استفاده از کنترل‌کننده‌های سفارشی، اطلاعات دستگاه‌های تخصیص‌یافته را به دست آورند.

سند KEP-5304 یک [پروتکل فرادادهٔ دستگاه](#device-metadata-protocol) تعریف می‌کند که درایورها باید از آن پیروی کنند تا برنامه‌ها در همهٔ درایورها و کلاسترها با ساختار یکسانی روبه‌رو شوند. [کتابخانهٔ افزونهٔ kubelet برای DRA](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin) این پروتکل را پیاده‌سازی می‌کند.

فراداده‌های دستگاه از همان قواعد دسترسی به دستگاه پیروی می‌کنند: این فراداده‌ها فقط زمانی درون یک کانتینر در دسترس هستند که آن کانتینر دستگاه را درخواست کرده باشد. برای جزئیات، به [درخواست دستگاه در بارهای کاری با استفاده از DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/#request-devices-workloads) مراجعه کنید.

### پروتکل فرادادهٔ دستگاه {#device-metadata-protocol}

این پروتکل از چهار قاعده تشکیل شده است:

1. **مسیرهای فایل.** فایل‌های فراداده درون کانتینرها در مسیر `/var/run/kubernetes.io/dra-device-attributes` قرار دارند. برای ResourceClaimای که مستقیماً به آن ارجاع داده شده است، مسیر به‌صورت `resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json` است. برای claimای که از یک ResourceClaimTemplate ایجاد شده است، مسیر به‌صورت `resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json` است که در آن `podClaimName` همان `pod.spec.resourceClaims[].name` است.

   وقتی یک درخواست از [فهرست اولویت‌دار](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#prioritized-list) استفاده می‌کند، فقط نام درخواست سطح بالا برای بخش `<requestName>` مسیر به کار می‌رود. فیلد `requests[].name` در فایل، ارجاع کامل `<request>/<subrequest>` را در خود دارد، مانند `gpu/high-memory`.

   ثابت‌های مسیر در [`k8s.io/dynamic-resource-allocation/api/metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata) تعریف شده‌اند.

1. **API مبتنی بر JSON.** هر فایل جریانی از یک یا چند آبجکت [`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata) است. هر آبجکت، مطابق با قراردادهای API کوبرنتیز، دارای `apiVersion` و `kind` است. فراداده‌های یکسان برای هر نسخهٔ API پیکربندی‌شده یک بار و به ترتیبی که درایور انتخاب کرده است کدگذاری می‌شوند. مصرف‌کنندگان از نخستین نسخه‌ای استفاده می‌کنند که بتوانند رمزگشایی کنند و از نسخه‌های ناشناخته صرف‌نظر می‌کنند. وجود آبجکتی بدساخت در یک نسخهٔ شناخته‌شده خطا محسوب می‌شود.

1. **نسل.** در فایل اولیه، مقدار `metadata.generation` برابر با `1` است. هر به‌روزرسانی این نسل را یک واحد افزایش می‌دهد تا مصرف‌کنندگان بتوانند تغییرات را تشخیص دهند.

1. **در اختیار قرار دادن برای کانتینر.** کتابخانهٔ افزونهٔ kubelet برای DRA از {{< glossary_tooltip text="CDI" term_id="cdi" >}} استفاده می‌کند تا هر فایل را به‌صورت فقط‌خواندنی bind-mount کند. پیاده‌سازی‌های دیگر می‌توانند از سازوکار متفاوتی استفاده کنند، به شرط آنکه فایل در مسیر الزامی ظاهر شود و فقط‌خواندنی باشد.

### فعال‌سازی فراداده‌ی دستگاه در یک درایور {#device-metadata-enable}

فراداده‌ی دستگاه (device metadata) قابلیتی در سمت درایور است. این قابلیت هیچ feature gate کوبرنتیزی ندارد و در کتابخانه‌ی افزونه‌ی kubelet مربوط به DRA به‌طور پیش‌فرض غیرفعال است. هر درایور باید این قابلیت را فعال کند و نسخه‌هایی را که می‌نویسد به‌صراحت انتخاب کند:

```go
kubeletplugin.EnableDeviceMetadata(true, []schema.GroupVersion{
	metadatav1beta1.SchemeGroupVersion,
	metadatav1alpha1.SchemeGroupVersion,
})
```

وجود نسخه‌ی `v1beta1` الزامی است. درایور می‌تواند برای سازگاری با مصرف‌کننده‌های قدیمی‌تر، نسخه‌ی `v1alpha1` را نیز بنویسد. ترتیب نسخه‌ها در این slice همان ترتیب آن‌ها در جریان فراداده است و چارچوب، نسخه‌ها را مرتب نمی‌کند. بهتر است درایورها جدیدترین نسخه را در ابتدا قرار دهند. اگر فراداده‌ی دستگاه بدون هیچ نسخه‌ای، بدون `v1beta1` یا با نسخه‌ای ناشناخته فعال شود، افزونه هنگام راه‌اندازی با شکست مواجه می‌شود.

درایور می‌تواند برای هر دستگاه آماده‌شده، فیلد [`Device.Metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Device) را با [`kubeletplugin.DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#DeviceMetadata) پر کند. بهتر است درایورها ویژگی‌هایی را که برای آن دستگاه در ResourceSlice منتشر می‌کنند، در این فراداده نیز بگنجانند تا بارهای کاری در زمان اجرا همان اطلاعات را ببینند. درایورها همچنین می‌توانند ویژگی‌هایی را اضافه کنند که فقط در زمان اجرا اهمیت دارند. درایورهای دستگاه‌های شبکه می‌توانند پس از پیکربندی CNI، با فراخوانی [`UpdateRequestMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Helper.UpdateRequestMetadata) نام رابط‌ها، نشانی‌های IP و نشانی‌های سخت‌افزاری را اضافه کنند.

پیوندهای بالا به API افزونه‌ی kubelet، نحوه‌ی یکپارچه‌سازی را برای نویسندگان درایور شرح می‌دهند. چارچوب DRA هیچ پرچم خط فرمان عمومی‌ای تعریف نمی‌کند؛ از این رو، گردانندگان کلاستر این قابلیت را از طریق پیکربندی استقراری که درایورشان ارائه می‌دهد فعال می‌کنند.

در صورت فعال بودن این قابلیت، کتابخانه‌ی افزونه‌ی kubelet مربوط به DRA هنگام آماده‌سازی دستگاه‌های تخصیص‌یافته، فایل‌های فراداده را می‌نویسد. این کتابخانه همچنین مشخصات CDI را به‌طور پیش‌فرض در `/var/run/cdi` می‌نویسد. محیط اجرای کانتینر باید طوری پیکربندی شود که مشخصات CDI را از این دایرکتوری کشف کند. کتابخانه، حداقل نسخه‌ی مشخصات CDI لازم برای هر مشخصات تولیدشده را تعیین می‌کند.

وقتی یک درخواست، دستگاه‌هایی را از چند درایور DRA تخصیص می‌دهد، هر درایور فایل فراداده‌ی خودش را می‌نویسد. مصرف‌کننده‌هایی که نام درایور را می‌دانند، بهتر است مسیر دقیق را از نام claim، نام درخواست و نام درایور بسازند. مصرف‌کننده‌های نوشته‌شده به زبان Go می‌توانند با استفاده از [`ReadResourceClaimMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#ReadResourceClaimMetadata) یا [`ReadResourceClaimTemplateMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#ReadResourceClaimTemplateMetadata) همه‌ی فایل‌های مربوط به درایورهای یک درخواست را بخوانند و ادغام کنند.

### طرح‌واره‌ی فراداده {#device-metadata-schema}

هر آبجکت در فایل فراداده با API‏ [`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata) ‏(`metadata.resource.k8s.io/v1beta1`) مطابقت دارد.

این طرح‌واره شامل موارد زیر است:

- فراداده‌ی استاندارد آبجکت برای ResourceClaim، شامل نام، فضای نام (namespace)، UID و نسل (generation) فراداده‌ی آن.
- فیلد اختیاری `podClaimName` برای claimای که از یک ResourceClaimTemplate تولید شده است.
- فهرستی از درخواست‌ها. هر درخواست یک نام الزامی و فهرستی از دستگاه‌های تخصیص‌یافته دارد.
- درایور، pool و نام هر دستگاه.
- ویژگی‌های اختیاری دستگاه و داده‌های شبکه.

مقادیر ویژگی‌ها همان نمایشی را دارند که ویژگی‌های دستگاه در ResourceSlice دارند. هر ویژگی دقیقاً یک مقدار تکی (`int`، `bool`، `string` یا `version`) یا یک مقدار فهرستی (`ints`، `bools`، `strings` یا `versions`) دارد. مقادیر ظرفیت دستگاه در فراداده‌ی دستگاه گنجانده نمی‌شوند.

داده‌های شبکه می‌توانند شامل `interfaceName`، `ips` و `hardwareAddress` باشند. برای آشنایی با محدودیت‌های فیلدها، [مستندات API‏ `DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata) را ببینید.

مثال زیر یک آبجکت را در جریان فراداده‌ی یک دستگاه GPU نشان می‌دهد که از طریق یک ResourceClaimTemplate تخصیص یافته است:

```json
{
  "kind": "DeviceMetadata",
  "apiVersion": "metadata.resource.k8s.io/v1beta1",
  "metadata": {
    "name": "pod0-gpu-2kqrd",
    "namespace": "gpu-test1",
    "uid": "c7e7b22e-239b-4498-b27c-7f1344481e14",
    "generation": 1
  },
  "podClaimName": "gpu",
  "requests": [
    {
      "name": "gpu",
      "devices": [
        {
          "driver": "gpu.example.com",
          "pool": "worker-0",
          "name": "gpu-0",
          "attributes": {
            "driverVersion": {
              "version": "1.0.0"
            },
            "index": {
              "int": 0
            },
            "model": {
              "string": "LATEST-GPU-MODEL"
            },
            "uuid": {
              "string": "gpu-18db0e85-99e9-c746-8531-ffeb86328b39"
            }
          }
        }
      ]
    }
  ]
}
```

افزونه‌ی kubelet مربوط به DRA پیش از نوشتن فراداده، آن را اعتبارسنجی نمی‌کند. مصرف‌کننده‌های نوشته‌شده به زبان Go می‌توانند هنگام رمزگشایی یک جریان، اعتبارسنجی تولیدشده را به‌دلخواه فعال کنند. رمزگشایی و اعتبارسنجی نتایج جداگانه‌ای دارند: خطای اعتبارسنجی مانع بازگرداندن آبجکتی نمی‌شود که با موفقیت رمزگشایی شده است. برای آشنایی با نحوه‌ی استفاده، [دسترسی به فراداده‌ی دستگاه DRA](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/#read-metadata-application) را ببینید.

### فراداده‌ی فوری و تأخیری {#device-metadata-lifecycle}

در فراداده‌ی فوری، درایور ویژگی‌ها یا داده‌های شبکه را هنگام آماده‌سازی claim فراهم می‌کند. افزونه‌ی kubelet مربوط به DRA پیش از شروع کانتینر مصرف‌کننده، فایل را با نسل `1` می‌نویسد.

در فراداده‌ی تأخیری، درایور می‌تواند دستگاه را بدون ویژگی‌ها یا داده‌های شبکه آماده کند. فایل اولیه با نسل `1` شامل هویت دستگاه است. درایور بعداً با فراخوانی `UpdateRequestMetadata` کل جریان را به‌صورت اتمی جایگزین می‌کند و نسل را یک واحد افزایش می‌دهد. به‌روزرسانی مستلزم وجود فایل اولیه است. اگر آماده‌سازی دستگاه برای یک درخواست هیچ دستگاهی برنگرداند، چارچوب برای آن درخواست نه فایل فراداده‌ای می‌سازد و نه دستگاه CDI فراداده‌ای.

فراداده در تمام طول عمر هر کانتینر مصرف‌کننده، برای آن کانتینر در دسترس می‌ماند. چارچوب پس از لغو آماده‌سازی claim، فایل‌های فراداده و مشخصات CDI را حذف می‌کند.

برای آشنایی با نحوه‌ی استفاده از فراداده‌ی دستگاه در بارهای کاری خود، [دسترسی به فراداده‌ی دستگاه DRA](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/) را ببینید.

### درایورهای سفارشی {#device-metadata-custom-drivers}

درایورهای سفارشی که از کتابخانه‌ی افزونه‌ی kubelet مربوط به DRA استفاده نمی‌کنند، باید [پروتکل فراداده‌ی دستگاه](#device-metadata-protocol) را خودشان پیاده‌سازی کنند. این کار شامل نوشتن جریان نسخه‌دار `DeviceMetadata` در مسیرهای درست، افزایش `metadata.generation` در هر به‌روزرسانی، و در دسترس قرار دادن فایل‌ها به‌صورت فقط‌خواندنی از طریق CDI یا سازوکاری معادل است.
