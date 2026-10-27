---
reviewers:
- klueska
- pohly
title: قابلیت مشاهده‌پذیری منابع پویا
content_type: concept
weight: 30
api_metadata:
- apiVersion: "resource.k8s.io/v1alpha3"
  kind: "ResourcePoolStatusRequest"
---

<!-- overview -->

این صفحه نحوهٔ مشاهدهٔ وضعیت و سلامت منابعی را که به‌صورت پویا با DRA تخصیص داده می‌شوند، توضیح می‌دهد.

<!-- body -->

## مشاهده‌پذیری منابع پویا {#observability-dynamic-resources}

می‌توانید وضعیت منابعی را که به‌صورت پویا تخصیص داده شده‌اند، با هر یک از روش‌های زیر بررسی کنید:

* [متریک‌های دستگاه در kubelet](#monitoring-resources)
* [وضعیت ResourceClaim](#resourceclaim-device-status)
* [پایش سلامت دستگاه](#device-health-monitoring)

### متریک‌های دستگاه در kubelet {#monitoring-resources}

سرویس gRPC با نام `PodResourcesLister` در kubelet به شما امکان می‌دهد دستگاه‌های در حال استفاده را پایش کنید.
پیام `DynamicResource` اطلاعاتی را فراهم می‌کند که مختص تخصیص پویای منابع است، مانند نام دستگاه و نام claim. برای جزئیات بیشتر،
بخش
[پایش منابع افزونهٔ دستگاه](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#monitoring-device-plugin-resources)
را ببینید.

### وضعیت دستگاه در ResourceClaim {#resourceclaim-device-status}

{{< feature-state feature_gate_name="DRAResourceClaimDeviceStatus" >}}

درایورهای DRA می‌توانند داده‌های
[وضعیت (status)](/docs/concepts/overview/working-with-objects/#object-spec-and-status) مختص درایور
را برای هر دستگاه تخصیص‌یافته در فیلد `status.devices` از یک ResourceClaim گزارش کنند.
برای مثال، درایور ممکن است نشانی‌های IP تخصیص‌یافته به یک دستگاه رابط شبکه را فهرست کند. به‌روزرسانی این فیلد به مجوزهای RBAC مصنوعی (synthetic) خاصی نیاز دارد؛
بخش
[راهنمای مقاوم‌سازی - تخصیص پویای منابع](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
و
[مقاوم‌سازی تخصیص پویای منابع در کلاستر شما](/docs/tasks/administer-cluster/hardening-dra/)
را ببینید.

دقت اطلاعاتی که یک درایور در فیلد `status.devices` از ResourceClaim ثبت می‌کند، به خود درایور بستگی دارد. درایورها را ارزیابی کنید تا تصمیم بگیرید
آیا می‌توانید به این فیلد به‌عنوان تنها منبع اطلاعات دستگاه تکیه کنید.

اگر
[feature gate با نام `DRAResourceClaimDeviceStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourceClaimDeviceStatus) را غیرفعال کنید،
فیلد `status.devices` هنگام ذخیره‌شدن ResourceClaim به‌طور خودکار پاک می‌شود.
وضعیت دستگاه در ResourceClaim زمانی پشتیبانی می‌شود که یک درایور DRA بتواند یک ResourceClaim موجود را که فیلد `status.devices` در آن مقداردهی شده است، به‌روزرسانی کند.

در مثال زیر، فیلد `status.devices` از یک ResourceClaim توسط درایور (`resource-driver.example.com`) که مسئول مدیریت دستگاه تخصیص‌یافته است، مقداردهی شده است:

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

اگر دستگاهی تخصیص داده نشده باشد، درخواست درایور برای به‌روزرسانی فیلد `status.devices`
از ResourceClaim با آن دستگاه رد می‌شود. هنگامی که تخصیص یک دستگاه لغو می‌شود (از `status.allocation.devices` حذف می‌شود)، ورودی متناظر در
`status.devices` به‌طور خودکار حذف می‌شود.

برای جزئیات بیشتر دربارهٔ فیلد `status.devices`، مستندات مرجع API مربوط به
{{< api-reference page="resource/resource-claim-v1" anchor="ResourceClaimStatus" text="ResourceClaim" >}} را ببینید.

### پایش سلامت دستگاه {#device-health-monitoring}

{{< feature-state feature_gate_name="ResourceHealthStatus" >}}

کوبرنتیز سازوکاری برای پایش و گزارش سلامت منابع زیرساختی تخصیص‌یافتهٔ پویا فراهم می‌کند.
برای برنامه‌های حالت‌دار (stateful) که روی سخت‌افزارهای تخصصی اجرا می‌شوند، آگاهی از خرابی یا ناسالم شدن یک دستگاه بسیار مهم است. همچنین آگاهی از بازیابی دستگاه نیز مفید است.

برای استفاده از این قابلیت، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/resource-health-status/) با نام `ResourceHealthStatus` باید فعال باشد (از نسخهٔ v1.36 در مرحلهٔ بتا و به‌صورت پیش‌فرض فعال است) و درایور DRA باید سرویس gRPC با نام `DRAResourceHealth` را پیاده‌سازی کرده باشد.

هنگامی که یک درایور DRA تشخیص می‌دهد که یک دستگاه تخصیص‌یافته ناسالم شده است، این وضعیت را به kubelet گزارش می‌کند. سپس این اطلاعات سلامت مستقیماً در status مربوط به Pod نمایش داده می‌شود. kubelet فیلد `allocatedResourcesStatus` را در status هر کانتینر مقداردهی می‌کند و سلامت هر دستگاه اختصاص‌یافته به آن کانتینر را شرح می‌دهد. هر ورودی سلامت منبع می‌تواند شامل یک فیلد اختیاری `message` با زمینهٔ توضیحی قابل‌خواندن برای انسان دربارهٔ وضعیت سلامت باشد، مانند جزئیات خطا یا دلایل خرابی.

اگر kubelet در بازهٔ زمانی مشخص (timeout) هیچ به‌روزرسانی سلامتی از یک درایور DRA دریافت نکند، وضعیت سلامت دستگاه «Unknown» علامت‌گذاری می‌شود. درایورهای DRA می‌توانند این timeout را برای هر دستگاه با تنظیم فیلد `health_check_timeout_seconds` در پیام gRPC با نام `DeviceHealth` پیکربندی کنند. در صورت عدم تعیین، kubelet از timeout پیش‌فرض ۳۰ ثانیه استفاده می‌کند. این امر به انواع مختلف سخت‌افزار (برای مثال GPUها، FPGAها یا دستگاه‌های ذخیره‌سازی) اجازه می‌دهد بر اساس ویژگی‌های گزارش سلامت خود از مقادیر timeout مناسب استفاده کنند.

این قابلیت دید بسیار مهمی را برای کاربران و کنترل‌کننده‌ها فراهم می‌کند تا بتوانند به خرابی‌های سخت‌افزاری واکنش نشان دهند.
برای Podی که با شکست مواجه می‌شود، می‌توانید این status را بررسی کنید تا مشخص شود آیا شکست به یک دستگاه ناسالم مربوط بوده است یا خیر.

{{< note >}}
وضعیت سلامت دستگاه پس از پایان کار یک Pod (برای مثال، در حالت Failed) در status مربوط به Pod به‌روزرسانی نمی‌شود.
{{< /note >}}

## وضعیت استخر منابع {#resource-pool-status}

{{< feature-state feature_gate_name="DRAResourcePoolStatus" >}}

می‌توانید با استفاده از API با نام ResourcePoolStatusRequest، دسترس‌پذیری دستگاه‌ها را در استخرهای منابع (resource pool) جست‌وجو کنید. این API دید روشنی فراهم می‌کند که در استخرهای منابع DRA کلاستر شما چه تعداد دستگاه در دسترس، تخصیص‌یافته یا ناavailable هستند.

برای بررسی وضعیت استخر منابع:

1. یک ResourcePoolStatusRequest ایجاد کنید که نام درایور (الزامی) و به‌صورت اختیاری یک محدودیت برای تعداد استخرهای بازگردانده‌شده را مشخص کند. همچنین می‌توانید با تعیین نام استخر، نتیجه را به یک استخر محدود کنید:

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

1. status را بخوانید تا دسترس‌پذیری استخر را ببینید:

   ```shell
   kubectl get resourcepoolstatusrequest/check-gpus -o yaml
   ```

   status شامل موارد زیر است:
   - `poolCount`: تعداد کل استخرهایی که با فیلتر مطابقت دارند (در صورتی که فهرست به‌دلیل limit کوتاه شده باشد، ممکن است از تعداد استخرهای فهرست‌شده بیشتر باشد).
   - `pools`: فهرستی از جزئیات استخرها که هر یک شامل موارد زیر است:
     - `driver` و `poolName`: استخر را شناسایی می‌کنند.
     - `generation`: آخرین نسل (generation) استخر که در میان ResourceSliceها مشاهده شده است.
     - `resourceSliceCount`: تعداد ResourceSliceهایی که استخر را تشکیل می‌دهند.
     - `totalDevices`: مجموع دستگاه‌های موجود در استخر.
     - `allocatedDevices`: دستگاه‌هایی که در حال حاضر به claimها تخصیص یافته‌اند.
     - `availableDevices`: دستگاه‌های قابل تخصیص
       (totalDevices - allocatedDevices - unavailableDevices).
     - `unavailableDevices`: دستگاه‌هایی که به دلیل taintها یا سایر شرایط در دسترس نیستند.
     - `nodeName`: نودی که با استخر مرتبط است، در صورت وجود.
     - `validationError`: زمانی مقداردهی می‌شود که داده‌های استخر نتوانسته باشد به‌طور کامل اعتبارسنجی شود
       (برای مثال، در جریان استقرار یک generation جدید). در صورت مقداردهی، فیلدهای شمارش دستگاه
       ممکن است مقداردهی نشده باشند.
     - `partitionSummary`: برای استخرهای [قابل‌افراز (partitionable)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)،
       قابلیت تخصیص به‌ازای هر نوع افراز (به
       [خلاصهٔ افراز](#resource-pool-partition-summary) مراجعه کنید).
     - `shareableSummary`: برای استخرهایی که [دستگاه‌های اشتراک‌پذیر](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity) دارند،
       مصرف تجمیعی ظرفیت (به
       [خلاصهٔ اشتراک‌پذیری](#resource-pool-shareable-summary) مراجعه کنید).
   - `conditions`: شامل انواع condition با نام `Complete` (موفقیت) یا `Failed` (خطا) است.

1. پس از پایان کار، درخواست را حذف کنید:

   ```shell
   kubectl delete resourcepoolstatusrequest/check-gpus
   ```

آبجکت‌های ResourcePoolStatusRequest یک‌بار توسط یک کنترل‌کننده در kube-controller-manager پردازش می‌شوند. spec پس از ایجاد تغییرناپذیر است و کل آبجکت پس از مقداردهی status تغییرناپذیر می‌شود. برای دریافت داده‌های به‌روز دسترس‌پذیری، درخواست را حذف و دوباره ایجاد کنید. درخواست‌های تکمیل‌شده پس از ۱ ساعت به‌طور خودکار پاک‌سازی می‌شوند.

این قابلیت به مجوزهای RBAC صریح روی منبع ResourcePoolStatusRequest نیاز دارد. هیچ ClusterRole پیش‌فرضی این مجوز را شامل نمی‌شود.

وضعیت استخر منابع توسط
[feature gate با نام `DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)
در `kube-apiserver` و `kube-controller-manager` کنترل می‌شود.

### خلاصهٔ افراز {#resource-pool-partition-summary}

{{< feature-state feature_gate_name="DRAPartitionableDevicesType" >}}

یک دستگاه فیزیکی واحد مانند GPU ممکن است به‌صورت چند نوع افراز (partition) معرفی شود (برای مثال، یک GPU کامل در برابر یک برش MIG نیمه‌اندازه) که از شمارنده‌های مشترک یکسانی مصرف می‌کنند. از آنجا که این افرازها برای ظرفیت زیرین یکسانی با یکدیگر رقابت می‌کنند، شمارش ساده دستگاه‌ها به شما نمی‌گوید از هر نوع هنوز چه تعداد قابل تخصیص است. برای استخرهای [قابل‌افراز (partitionable)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)،
نمای `partitionSummary` به این پرسش پاسخ می‌دهد. این نما برای هر نوع افراز موارد زیر را گزارش می‌کند:

- `attribute`: نام کاملاً مشخص‌شدهٔ ویژگی دستگاه که مقدار آن این ورودی را گروه‌بندی می‌کند. این مقدار برابر با `spec.partitionTypeAttribute` در ResourceSlice است، یا اگر slice چیزی تعیین نکرده باشد، برابر با `spec.defaultPartitionTypeAttribute` در درخواست است.
- `type`: مقدار آن ویژگی روی دستگاه (برای مثال، `Full` یا `Half`).
- `total`: تعداد دستگاه‌های این نوع افراز در استخر.
- `allocatable`: تعداد دستگاه‌های *اضافی* از این نوع افراز که با توجه به مصرف فعلی شمارنده‌های مشترک هنوز می‌توانند تخصیص داده شوند.

ویژگی نام‌برده باید یک ویژگی از نوع رشته (string) باشد. اگر ویژگی نوع افراز در یک دستگاه قابل‌افراز وجود نداشته باشد یا رشته نباشد (برای مثال، عدد صحیح، بولی یا مقدار نسخه)، استخر به‌جای خلاصهٔ افراز یک خطای اعتبارسنجی گزارش می‌کند. برای
[ویژگی‌های از نوع فهرست](/docs/reference/command-line-tools-reference/feature-gates/#DRAListTypeAttributes)
هیچ رفتار ویژه‌ای در نظر گرفته نشده است؛
یک ویژگی غیررشته‌ای صرفاً به‌عنوان ویژگی نوع افراز معتبر نیست.

برای تولید این نما، درایور هر دستگاه قابل‌افراز را با یک ویژگی رشته‌ای برچسب‌گذاری می‌کند که مقدار آن نوع افراز را نام می‌برد و آن ویژگی را در فیلد `partitionTypeAttribute` از ResourceSlice مشخص می‌کند:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
# ...
spec:
  # Every partitionable device in this slice carries this attribute; devices
  # that share a value share the same shared-counter cost.
  partitionTypeAttribute: gpu.example.com/profile
```

اگر یک درایور هنوز برای اعلام `partitionTypeAttribute` به‌روزرسانی نشده باشد، یک درخواست همچنان می‌تواند با تعیین یک ویژگی جایگزین در spec خود، خلاصهٔ افراز را دریافت کند. `partitionTypeAttribute` خود slice همواره اولویت دارد؛ مقدار پیش‌فرض در سطح درخواست فقط برای دستگاه‌هایی اعمال می‌شود که slice آن‌ها چنین ویژگی‌ای اعلام نکرده است:

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

هنگامی که نه slice و نه درخواست هیچ ویژگی‌ای را نام نبرده باشند، یک استخر قابل‌افراز هیچ `partitionSummary` گزارش نمی‌کند.

نمای `partitionSummary` توسط
[feature gate با نام `DRAPartitionableDevicesType`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevicesType)
در `kube-apiserver` و `kube-controller-manager` کنترل می‌شود، که خود مستلزم فعال بودن feature gateهای
[`DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus)
و
[`DRAPartitionableDevices`](/docs/reference/command-line-tools-reference/feature-gates/#DRAPartitionableDevices)
است.

### خلاصهٔ اشتراک‌پذیری {#resource-pool-shareable-summary}

برای استخرهایی که شامل [دستگاه‌های اشتراک‌پذیر](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity) هستند
(دستگاه‌هایی که `allowMultipleAllocations` را تنظیم می‌کنند و می‌توانند توسط چند claim مصرف شوند)، `shareableSummary` مصرف تجمیعی ظرفیت را در سراسر استخر گزارش می‌کند:

- `fullyAvailableDevices`: دستگاه‌های اشتراک‌پذیری که هیچ ظرفیتی از آن‌ها مصرف نشده است.
- `partiallyAvailableDevices`: دستگاه‌های اشتراک‌پذیری که بخشی از ظرفیت آن‌ها، اما نه همهٔ آن، مصرف شده است.
- `capacity`: به‌ازای هر نام ظرفیت، مقادیر تجمیعی `total`، `consumed` و `available` (برابر `total` منهای `consumed`، که هرگز منفی نمی‌شود) در سراسر استخر.

`shareableSummary` فقط زمانی مقداردهی می‌شود که دست‌کم یک دستگاه در استخر اشتراک‌پذیر باشد. این بخش جزئی از قابلیت [وضعیت استخر منابع](#resource-pool-status)
است (feature gate با نام
[`DRAResourcePoolStatus`](/docs/reference/command-line-tools-reference/feature-gates/#DRAResourcePoolStatus))
و به `DRAPartitionableDevicesType` نیازی ندارد؛ دستگاه‌های اشتراک‌پذیری که این بخش خلاصه می‌کند از قابلیت
[ظرفیت قابل‌مصرف (consumable capacity)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#consumable-capacity)
می‌آیند.


## فرادادهٔ دستگاه DRA در کانتینرها {#device-metadata}

{{< feature-state state="beta" for_k8s_version="v1.37" >}}

درایورهای DRA می‌توانند فراداده‌های دستگاه مانند ویژگی‌های دستگاه (نشانی‌های باس PCI یا UUIDهای دستگاه‌های واسطه‌ای (mediated)) و پیکربندی شبکه را به‌صورت فایل‌های JSON مستقیماً در اختیار کانتینرها قرار دهند.
این امر به برنامه‌ها اجازه می‌دهد بدون پرس‌وجو از API کوبرنتیز یا استفاده از کنترل‌کننده‌های سفارشی، اطلاعات دستگاه‌های تخصیص‌یافته را کشف کنند.

KEP-5304 یک
[پروتکل فرادادهٔ دستگاه](#device-metadata-protocol) را تعریف می‌کند که درایورها باید از آن پیروی کنند
تا برنامه‌ها در درایورها و کلاسترهای مختلف ساختار یکسانی را ببینند.
[کتابخانهٔ افزونهٔ DRA kubelet](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin)
این پروتکل را پیاده‌سازی می‌کند.

فرادادهٔ دستگاه از همان قواعد دسترسی به دستگاه پیروی می‌کند: این فراداده تنها زمانی داخل یک کانتینر در دسترس است که آن کانتینر دستگاه را درخواست کرده باشد. برای جزئیات بیشتر، بخش
[درخواست دستگاه‌ها در بارهای کاری با استفاده از DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/#request-devices-workloads)
را ببینید.

### پروتکل فرادادهٔ دستگاه {#device-metadata-protocol}

این پروتکل از چهار قاعده تشکیل شده است:

1. **مسیر فایل‌ها.** فایل‌های فراداده درون کانتینرها در مسیر
   `/var/run/kubernetes.io/dra-device-attributes` قرار دارند. برای یک
   ResourceClaim که مستقیماً ارجاع داده شده است، مسیر برابر است با
   `resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json`. برای
   claimی که از یک ResourceClaimTemplate ایجاد شده است، مسیر برابر است با
   `resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json`،
   که در آن `podClaimName` همان `pod.spec.resourceClaims[].name` است.

   هنگامی که یک درخواست از [فهرست اولویت‌دار](/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#prioritized-list) استفاده می‌کند، فقط نام درخواست سطح بالا برای بخش مسیر `<requestName>` به کار می‌رود. فیلد
   `requests[].name` در فایل شامل ارجاع کامل
   `<request>/<subrequest>` است، مانند `gpu/high-memory`.

   ثابت‌های مسیر در
   [`k8s.io/dynamic-resource-allocation/api/metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata)
   تعریف شده‌اند.

1. **API مبتنی بر JSON.** هر فایل جریانی از یک یا چند آبجکت
   [`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata)
   است. هر آبجکت مطابق با قراردادهای API کوبرنتیز دارای `apiVersion` و `kind` است. همان فراداده به‌ازای هر نسخهٔ API پیکربندی‌شده یک‌بار و به ترتیبی که درایور انتخاب کرده است کدگذاری می‌شود. مصرف‌کنندگان از نخستین نسخه‌ای که قادر به رمزگشایی آن هستند استفاده می‌کنند و نسخه‌های ناشناخته را نادیده می‌گیرند. یک آبجکت نادرست‌ساختار (malformed) در یک نسخهٔ شناخته‌شده یک خطا محسوب می‌شود.

1. **نسل (Generation).** فایل اولیه مقدار `metadata.generation` را برابر `1` دارد.
   هر به‌روزرسانی generation را یک واحد افزایش می‌دهد تا مصرف‌کنندگان بتوانند تغییرات را تشخیص دهند.

1. **در دسترس قرار دادن در کانتینر.** کتابخانهٔ افزونهٔ DRA kubelet از
   {{< glossary_tooltip text="CDI" term_id="cdi" >}} برای bind-mount کردن هر فایل
   به‌صورت فقط‌خواندنی استفاده می‌کند. پیاده‌سازی‌های دیگر می‌توانند از سازوکار متفاوتی استفاده کنند، مادامی که
   فایل در مسیر موردنیاز ظاهر شود و فقط‌خواندنی باشد.

### فعال‌سازی فراداده دستگاه در یک درایور {#device-metadata-enable}

فراداده دستگاه (device metadata) یک قابلیت سمت درایور است. این قابلیت feature gate مخصوص کوبرنتیز ندارد و به‌طور پیش‌فرض در کتابخانه افزونه kubelet برای DRA غیرفعال است. درایور باید این قابلیت را فعال کند و نسخه‌هایی را که می‌نویسد، صراحتاً انتخاب کند:

```go
kubeletplugin.EnableDeviceMetadata(true, []schema.GroupVersion{
	metadatav1beta1.SchemeGroupVersion,
	metadatav1alpha1.SchemeGroupVersion,
})
```

نسخه `v1beta1` الزامی است. درایور می‌تواند برای سازگاری با مصرف‌کنندگان قدیمی‌تر، نسخه `v1alpha1` را نیز بنویسد. ترتیب عناصر در slice همان ترتیب آن‌ها در جریان فراداده است؛ فریمورک نسخه‌ها را مرتب نمی‌کند. درایورها باید جدیدترین نسخه را در ابتدا قرار دهند. فعال‌سازی فراداده دستگاه بدون هیچ نسخه‌ای، بدون `v1beta1` یا با یک نسخه ناشناخته باعث می‌شود افزونه هنگام راه‌اندازی با خطا مواجه شود.

درایور می‌تواند برای هر دستگاه آماده‌شده، فیلد
[`Device.Metadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Device)
را با
[`kubeletplugin.DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#DeviceMetadata)
مقداردهی کند. درایورها باید ویژگی‌هایی (attributes) را که برای آن دستگاه در ResourceSlice منتشر می‌کنند، در این فراداده نیز بگنجانند تا بارهای کاری در زمان اجرا همان اطلاعات را ببینند. درایورها همچنین می‌توانند ویژگی‌هایی را اضافه کنند که فقط در زمان اجرا اهمیت دارند. برای دستگاه‌های شبکه، درایورها می‌توانند پس از پیکربندی CNI با فراخوانی
[`UpdateRequestMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#Helper.UpdateRequestMetadata)
نام رابط‌ها، نشانی‌های IP و نشانی‌های سخت‌افزاری را اضافه کنند.

پیوندهای API افزونه kubelet که در بالا آمده‌اند، یکپارچه‌سازی را برای نویسندگان درایور شرح می‌دهند. فریمورک DRA هیچ flag خط فرمان عمومی تعریف نمی‌کند؛ بنابراین اپراتورهای کلاستر این قابلیت را از طریق پیکربندی استقراری که درایورشان ارائه می‌دهد، فعال می‌کنند.

هنگامی که این قابلیت فعال باشد، کتابخانه افزونه kubelet برای DRA هنگام آماده‌سازی دستگاه‌های تخصیص‌یافته، فایل‌های فراداده را می‌نویسد. این کتابخانه همچنین به‌طور پیش‌فرض مشخصات CDI را در مسیر `/var/run/cdi` می‌نویسد. container runtime باید به‌گونه‌ای پیکربندی شود که مشخصات CDI را از آن دایرکتوری شناسایی کند. کتابخانه حداقل نسخه مشخصات CDI لازم برای هر مشخصه تولیدشده را تعیین می‌کند.

وقتی یک درخواست، دستگاه‌هایی را از چند درایور DRA تخصیص می‌دهد، هر درایور فایل فراداده مخصوص خود را می‌نویسد. مصرف‌کنندگانی که نام درایور را می‌دانند، باید مسیر دقیق را از روی نام claim، درخواست و درایور بسازند. مصرف‌کنندگان نوشته‌شده با Go می‌توانند از
[`ReadResourceClaimMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#ReadResourceClaimMetadata)
یا
[`ReadResourceClaimTemplateMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#ReadResourceClaimTemplateMetadata)
برای خواندن و ادغام تمام فایل‌های هر درایور برای یک درخواست استفاده کنند.

### طرحواره فراداده {#device-metadata-schema}

هر آبجکت در یک فایل فراداده با API زیر مطابقت دارد:
[`DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata)
(`metadata.resource.k8s.io/v1beta1`).

این طرحواره شامل موارد زیر است:

- فراداده استاندارد آبجکت برای ResourceClaim، شامل نام، فضای نام (namespace)، UID و نسل (generation) فراداده.
- فیلد اختیاری `podClaimName` برای claim که از یک ResourceClaimTemplate تولید شده است.
- فهرستی از درخواست‌ها. هر درخواست یک نام الزامی و فهرستی از دستگاه‌های تخصیص‌یافته دارد.
- درایور، pool و نام هر دستگاه.
- ویژگی‌های اختیاری دستگاه و داده‌های شبکه.

مقادیر ویژگی‌ها از همان قالب ویژگی‌های دستگاه در ResourceSlice استفاده می‌کنند. هر ویژگی دقیقاً یک مقدار اسکالر (`int`، `bool`، `string` یا `version`) یا یک مقدار فهرستی (`ints`، `bools`، `strings` یا `versions`) دارد. مقادیر ظرفیت دستگاه در فراداده دستگاه گنجانده نمی‌شوند.

داده‌های شبکه می‌توانند شامل `interfaceName`، `ips` و `hardwareAddress` باشند.
برای محدودیت‌های فیلدها، به
[مستندات API مربوط به `DeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/api/metadata/v1beta1#DeviceMetadata)
مراجعه کنید.

مثال زیر یک آبجکت در جریان فراداده را برای یک دستگاه GPU نشان می‌دهد که از طریق یک ResourceClaimTemplate تخصیص یافته است:

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

افزونه kubelet برای DRA فراداده را پیش از نوشتن اعتبارسنجی نمی‌کند. مصرف‌کنندگان نوشته‌شده با Go می‌توانند هنگام رمزگشایی یک جریان، اعتبارسنجی تولیدشده را به‌صورت اختیاری فعال کنند. نتایج رمزگشایی و اعتبارسنجی از یکدیگر جدا هستند: خطای اعتبارسنجی مانع از بازگردانده شدن آبجکتی که با موفقیت رمزگشایی شده است نمی‌شود. برای نحوه استفاده، به
[دسترسی به فراداده دستگاه DRA](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/#read-metadata-application)
مراجعه کنید.

### فراداده فوری و تعویق‌یافته {#device-metadata-lifecycle}

در فراداده فوری (immediate)، درایور ویژگی‌ها یا داده‌های شبکه را هنگام آماده‌سازی claim فراهم می‌کند. افزونه kubelet برای DRA فایل را با نسل `1` پیش از آغاز به کار کانتینر مصرف‌کننده می‌نویسد.

در فراداده تعویق‌یافته (deferred)، درایور می‌تواند یک دستگاه را بدون ویژگی یا داده شبکه آماده کند. فایل اولیه با نسل `1` شامل هویت دستگاه است. درایور بعداً `UpdateRequestMetadata` را فراخوانی می‌کند تا کل جریان را به‌صورت اتمی جایگزین کند و نسل را افزایش دهد. به‌روزرسانی مستلزم وجود فایل اولیه است. اگر آماده‌سازی دستگاه برای یک درخواست هیچ دستگاهی برنگرداند، فریمورک برای آن درخواست نه فایل فراداده‌ای ایجاد می‌کند و نه دستگاه CDI مربوط به فراداده.

فراداده در تمام مدت عمر هر کانتینر مصرف‌کننده برای آن کانتینر در دسترس باقی می‌ماند. فریمورک پس از لغو آماده‌سازی (unprepare) claim، فایل‌های فراداده و مشخصات CDI را حذف می‌کند.

برای آشنایی با نحوه استفاده از فراداده دستگاه در بارهای کاری خود، به
[دسترسی به فراداده دستگاه DRA](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/)
مراجعه کنید.

### درایورهای سفارشی {#device-metadata-custom-drivers}

درایورهای سفارشی که از کتابخانه افزونه kubelet برای DRA استفاده نمی‌کنند، باید خودشان
[پروتکل فراداده دستگاه](#device-metadata-protocol) را پیاده‌سازی کنند. این کار شامل نوشتن جریان نسخه‌دار `DeviceMetadata` در مسیرهای صحیح، افزایش `metadata.generation` در هر به‌روزرسانی، و ارائه فایل‌ها به‌صورت فقط‌خواندنی از طریق CDI یا سازوکاری معادل است.
