---
api_metadata:
  apiVersion: "resource.k8s.io/v1"
  import: "k8s.io/api/resource/v1"
  kind: "ResourceClaim"
content_type: "api_reference"
description: "ResourceClaim درخواستی را برای دسترسی به منابع کلاستر توصیف می‌کند که بارهای کاری از آن استفاده می‌کنند. برای مثال، اگر یک بار کاری به دستگاه شتاب‌دهنده‌ای با ویژگی‌های مشخص نیاز داشته باشد، این درخواست از طریق ResourceClaim بیان می‌شود. بخش status مشخص می‌کند که آیا این claim برآورده شده است یا خیر و کدام منابع به‌طور مشخص تخصیص داده شده‌اند."
title: "ResourceClaim"
weight: 30
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: resource.k8s.io/v1`

`import "k8s.io/api/resource/v1"`


## ResourceClaim {#ResourceClaim}

ResourceClaim درخواستی را برای دسترسی به منابع کلاستر توصیف می‌کند که بارهای کاری از آن استفاده می‌کنند. برای مثال، اگر یک بار کاری به دستگاه شتاب‌دهنده‌ای با ویژگی‌های مشخص نیاز داشته باشد، این درخواست از طریق ResourceClaim بیان می‌شود. بخش status مشخص می‌کند که آیا این claim برآورده شده است یا خیر و کدام منابع به‌طور مشخص تخصیص داده شده‌اند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST را نشان می‌دهد که این آبجکت بیانگر آن است. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#ResourceClaimSpec" >}}">ResourceClaimSpec</a></em></td>
      <td>Spec توصیف می‌کند که چه چیزی درخواست می‌شود و چگونه باید پیکربندی شود. spec تغییرناپذیر (immutable) است.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#ResourceClaimStatus" >}}">ResourceClaimStatus</a></em></td>
      <td>Status توصیف می‌کند که آیا claim آماده استفاده است و چه چیزی تخصیص داده شده است.</td>
    </tr>
  </tbody>
</table>


## ResourceClaimSpec {#ResourceClaimSpec}

ResourceClaimSpec مشخص می‌کند که در یک ResourceClaim چه چیزی درخواست می‌شود و چگونه باید پیکربندی شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>devices</code><br/><em><a href="{{< ref "#DeviceClaim" >}}">DeviceClaim</a></em></td>
      <td>Devices مشخص می‌کند که دستگاه‌ها چگونه درخواست شوند.</td>
    </tr>
  </tbody>
</table>


## ResourceClaimStatus {#ResourceClaimStatus}

ResourceClaimStatus پیگیری می‌کند که آیا منبع تخصیص داده شده است و نتیجه آن چه بوده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allocation</code><br/><em><a href="{{< ref "#AllocationResult" >}}">AllocationResult</a></em></td>
      <td>Allocation پس از آنکه claim با موفقیت تخصیص داده شد مقداردهی می‌شود.</td>
    </tr>
    <tr>
      <td><code>devices</code><br/><em><a href="{{< ref "#AllocatedDeviceStatus" >}}">AllocatedDeviceStatus array</a></em></td>
      <td>Devices شامل وضعیت هر دستگاهی است که برای این claim تخصیص داده شده است، به‌صورتی که درایور گزارش کرده است. این وضعیت می‌تواند اطلاعات مختص درایور را نیز شامل شود. هر مدخل متعلق به درایور مربوط به خود است.</td>
    </tr>
    <tr>
      <td><code>reservedFor</code><br/><em><a href="{{< ref "#ResourceClaimConsumerReference" >}}">ResourceClaimConsumerReference array</a></em><br/><em>patch strategy: merge on key <code>uid</code></em></td>
      <td>ReservedFor مشخص می‌کند که در حال حاضر چه موجودیت‌هایی مجاز به استفاده از claim هستند. Podی که به یک ResourceClaim ارجاع دهد که برای آن Pod رزرو نشده است، شروع به کار نخواهد کرد. claimی که در حال استفاده است یا به دلیل رزرو شدن ممکن است در حال استفاده باشد، نباید از حالت تخصیص خارج شود.  در کلاستری با چند نمونه زمان‌بند، ممکن است دو Pod به‌طور همزمان توسط زمان‌بندهای مختلف زمان‌بندی شوند. اگر هر دو به یک ResourceClaim ارجاع دهند که پیش‌تر به حداکثر تعداد مصرف‌کنندگان خود رسیده است، فقط یکی از Podها می‌تواند زمان‌بندی شود.  هر دو زمان‌بند تلاش می‌کنند Pod خود را به فیلد claim.status.reservedFor اضافه کنند، اما فقط به‌روزرسانی‌ای ذخیره می‌شود که زودتر به API server برسد. به‌روزرسانی دیگر با خطا مواجه می‌شود و زمان‌بندی که آن را ارسال کرده است می‌داند که باید Pod را به صف بازگرداند و منتظر بماند تا ResourceClaim دوباره قابل استفاده شود.  حداکثر ۲۵۶ رزرو از این نوع می‌تواند وجود داشته باشد. این مقدار ممکن است در آینده افزایش یابد، اما کاهش نخواهد یافت.</td>
    </tr>
  </tbody>
</table>


## ResourceClaimList {#ResourceClaimList}

ResourceClaimList مجموعه‌ای از claimها است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim array</a></em></td>
      <td>Items فهرست resource claimها است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST را نشان می‌دهد که این آبجکت بیانگر آن است. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست</td>
    </tr>
  </tbody>
</table>


## AllocatedDeviceStatus {#AllocatedDeviceStatus}

AllocatedDeviceStatus وضعیت یک دستگاه تخصیص‌یافته را در بر دارد، در صورتی که درایور تصمیم به گزارش آن بگیرد. این وضعیت می‌تواند اطلاعات مختص درایور را نیز شامل شود.

ترکیب Driver، Pool، Device و ShareID باید با کلید متناظر در Status.Allocation.Devices مطابقت داشته باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "../definitions/condition-v1-meta#Condition" >}}">Condition array</a></em></td>
      <td>Conditions شامل آخرین مشاهده از وضعیت دستگاه است. اگر دستگاه بر اساس ارجاع‌های پیکربندی class و claim پیکربندی شده باشد، شرط `Ready` باید True باشد.  نباید بیش از ۸ مدخل داشته باشد.</td>
    </tr>
    <tr>
      <td><code>data</code><br/><em></em></td>
      <td>Data شامل داده‌های دلخواه مختص درایور است.  طول داده خام باید کوچکتر یا مساوی ۱۰ Ki باشد.</td>
    </tr>
    <tr>
      <td><code>device</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Device با استفاده از نام یک نمونه دستگاه در pool منابع درایور به آن ارجاع می‌دهد. این مقدار باید یک DNS label باشد.</td>
    </tr>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Driver نام درایور DRA را مشخص می‌کند که پس از نیاز به claim روی یک نود، افزونه kubelet آن باید برای پردازش تخصیص فراخوانی شود.  باید یک DNS subdomain باشد و بهتر است به یک دامنه DNS ختم شود که متعلق به فروشنده درایور است. فقط باید از حروف کوچک استفاده کند.</td>
    </tr>
    <tr>
      <td><code>networkData</code><br/><em><a href="{{< ref "#NetworkDeviceData" >}}">NetworkDeviceData</a></em></td>
      <td>NetworkData شامل اطلاعات مرتبط با شبکه است که مختص این دستگاه است.</td>
    </tr>
    <tr>
      <td><code>pool</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>این نام به‌همراه نام درایور و فیلد نام دستگاه مشخص می‌کند که کدام دستگاه تخصیص داده شده است (`\<driver name>/\<pool name>/\<device name>`).  طول آن نباید بیش از ۲۵۳ نویسه باشد و می‌تواند شامل یک یا چند DNS sub-domain باشد که با اسلش از هم جدا شده‌اند.</td>
    </tr>
    <tr>
      <td><code>shareID</code><br/><em>string</em></td>
      <td>ShareID به‌طور یکتا یک سهم تخصیص‌یافته مجزا از دستگاه را شناسایی می‌کند.</td>
    </tr>
  </tbody>
</table>


## AllocationResult {#AllocationResult}

AllocationResult شامل ویژگی‌های یک منبع تخصیص‌یافته است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allocationTimestamp</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>AllocationTimestamp زمان تخصیص منابع را ذخیره می‌کند. تضمینی وجود ندارد که این فیلد مقداردهی شود؛ در این صورت آن زمان نامشخص است.  این یک فیلد بتا است و نیاز به فعال‌سازی feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus دارد.</td>
    </tr>
    <tr>
      <td><code>devices</code><br/><em><a href="{{< ref "#DeviceAllocationResult" >}}">DeviceAllocationResult</a></em></td>
      <td>Devices نتیجه تخصیص دستگاه‌ها است.</td>
    </tr>
    <tr>
      <td><code>nodeSelector</code><br/><em><a href="{{< ref "../definitions/node-selector-v1#NodeSelector" >}}">NodeSelector</a></em></td>
      <td>NodeSelector مشخص می‌کند منابع تخصیص‌یافته در کجا در دسترس هستند. اگر مقداردهی نشود، منابع در همه‌جا در دسترس‌اند.</td>
    </tr>
  </tbody>
</table>


## CapacityRequirements {#CapacityRequirements}

CapacityRequirements نیازمندی‌های ظرفیت را برای یک درخواست دستگاه مشخص تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>requests</code><br/><em>object</em></td>
      <td>Requests بیانگر درخواست‌های منبع مجزای دستگاه برای منابع متمایز است که دستگاه باید همه آن‌ها را فراهم کند.  این مقدار به‌عنوان یک شرط فیلتر اضافی در برابر ظرفیت در دسترس دستگاه استفاده می‌شود. از نظر معنایی، این معادل یک انتخابگر CEL به‌صورت `device.capacity[\<domain>].\<name>.compareTo(quantity(\<request quantity>)) >= 0` است. برای مثال، device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.  وقتی requestPolicy تعریف شده باشد، مقدار درخواستی بر اساس سیاست به نزدیک‌ترین مقدار معتبر بالاتر گرد می‌شود. اگر مقدار درخواستی را نتوان به مقدار معتبر تنظیم کرد—زیرا از حد مجاز requestPolicy فراتر می‌رود—دستگاه برای تخصیص نامناسب تلقی می‌شود.  برای هر ظرفیتی که صراحتاً درخواست نشده باشد: - اگر هیچ requestPolicy تنظیم نشده باشد، ظرفیت مصرفی پیش‌فرض برابر با کل ظرفیت دستگاه است   (یعنی کل دستگاه اشغال می‌شود). - اگر requestPolicy تنظیم شده باشد، ظرفیت مصرفی پیش‌فرض بر اساس همان سیاست تعیین می‌شود.  اگر دستگاه تخصیص چندگانه را مجاز کند، مقدار تجمعی در همه درخواست‌ها نباید از مقدار ظرفیت بیشتر شود. ظرفیت مصرف‌شده، که در صورت تعریف requestPolicy ممکن است بر اساس آن تنظیم شده باشد، در فیلد status.devices[*].consumedCapacity مربوط به resource claim ثبت می‌شود.</td>
    </tr>
  </tbody>
</table>


## DeviceAllocationConfiguration {#DeviceAllocationConfiguration}

DeviceAllocationConfiguration درون یک AllocationResult قرار می‌گیرد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>opaque</code><br/><em><a href="{{< ref "device-class-v1#OpaqueDeviceConfiguration" >}}">OpaqueDeviceConfiguration</a></em></td>
      <td>Opaque پارامترهای پیکربندی مختص درایور را فراهم می‌کند.</td>
    </tr>
    <tr>
      <td><code>requests</code><br/><em>string array</em></td>
      <td>Requests نام درخواست‌هایی را فهرست می‌کند که پیکربندی روی آن‌ها اعمال می‌شود. اگر خالی باشد، روی همه درخواست‌ها اعمال می‌شود.  ارجاع به زیردرخواست‌ها باید شامل نام درخواست اصلی باشد و می‌تواند زیردرخواست را با قالب \<main request>[/\<subrequest>] مشخص کند. اگر فقط درخواست اصلی ذکر شود، پیکربندی روی همه زیردرخواست‌ها اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>source</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Source ثبت می‌کند که پیکربندی از یک class می‌آید و بنابراین چیزی نیست که یک کاربر عادی بتواند آن را تنظیم کند، یا از یک claim می‌آید.<br/><br/>Possible enum values:<br/> - `"FromClaim"`<br/> - `"FromClass"`</td>
    </tr>
  </tbody>
</table>


## DeviceAllocationResult {#DeviceAllocationResult}

DeviceAllocationResult نتیجه تخصیص دستگاه‌ها است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>config</code><br/><em><a href="{{< ref "#DeviceAllocationConfiguration" >}}">DeviceAllocationConfiguration array</a></em></td>
      <td>این فیلد ترکیبی از همه پارامترهای پیکربندی claim و class است. درایورها می‌توانند آن‌ها را بر اساس یک پرچم از هم تشخیص دهند.  این شامل پارامترهای پیکربندی درایورهایی نیز می‌شود که هیچ دستگاه تخصیص‌یافته‌ای در نتیجه ندارند، زیرا این درایورها هستند که تعیین می‌کنند کدام پارامترهای پیکربندی را پشتیبانی کنند. آن‌ها می‌توانند پارامترهای پیکربندی ناشناخته را بی‌صدا نادیده بگیرند.</td>
    </tr>
    <tr>
      <td><code>results</code><br/><em><a href="{{< ref "#DeviceRequestAllocationResult" >}}">DeviceRequestAllocationResult array</a></em></td>
      <td>Results همه دستگاه‌های تخصیص‌یافته را فهرست می‌کند.</td>
    </tr>
  </tbody>
</table>


## DeviceClaim {#DeviceClaim}

DeviceClaim مشخص می‌کند که دستگاه‌ها چگونه با یک ResourceClaim درخواست شوند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>config</code><br/><em><a href="{{< ref "#DeviceClaimConfiguration" >}}">DeviceClaimConfiguration array</a></em></td>
      <td>این فیلد پیکربندی چند درایور بالقوه را نگه می‌دارد که می‌توانند درخواست‌های این claim را برآورده کنند. هنگام تخصیص claim نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>constraints</code><br/><em><a href="{{< ref "#DeviceConstraint" >}}">DeviceConstraint array</a></em></td>
      <td>مجموعه دستگاه‌هایی که برای claim تخصیص داده می‌شوند باید این محدودیت‌ها را برآورده کنند.</td>
    </tr>
    <tr>
      <td><code>requests</code><br/><em><a href="{{< ref "#DeviceRequest" >}}">DeviceRequest array</a></em></td>
      <td>Requests بیانگر درخواست‌های مجزا برای دستگاه‌های متمایز است که همه باید برآورده شوند. اگر خالی باشد، هیچ چیزی نیاز به تخصیص ندارد.</td>
    </tr>
  </tbody>
</table>


## DeviceClaimConfiguration {#DeviceClaimConfiguration}

DeviceClaimConfiguration برای پارامترهای پیکربندی در DeviceClaim استفاده می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>opaque</code><br/><em><a href="{{< ref "device-class-v1#OpaqueDeviceConfiguration" >}}">OpaqueDeviceConfiguration</a></em></td>
      <td>Opaque پارامترهای پیکربندی مختص درایور را فراهم می‌کند.</td>
    </tr>
    <tr>
      <td><code>requests</code><br/><em>string array</em></td>
      <td>Requests نام درخواست‌هایی را فهرست می‌کند که پیکربندی روی آن‌ها اعمال می‌شود. اگر خالی باشد، روی همه درخواست‌ها اعمال می‌شود.  ارجاع به زیردرخواست‌ها باید شامل نام درخواست اصلی باشد و می‌تواند زیردرخواست را با قالب \<main request>[/\<subrequest>] مشخص کند. اگر فقط درخواست اصلی ذکر شود، پیکربندی روی همه زیردرخواست‌ها اعمال می‌شود.</td>
    </tr>
  </tbody>
</table>

## DeviceConstraint {#DeviceConstraint}

DeviceConstraint باید به‌جز Requests دقیقاً یک فیلد دیگر را مقداردهی کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>distinctAttribute</code><br/><em>string</em></td>
      <td>DistinctAttribute الزام می‌کند که همه دستگاه‌های مورد نظر این attribute را داشته باشند و نوع و مقدار آن در میان این دستگاه‌ها یکتا باشد.  هنگامی که feature gate با نام DRAListTypeAttributes فعال باشد، مقایسه با معناشناسی مجموعه‌ای انجام می‌شود (یعنی ترتیب عناصر و تکرارها نادیده گرفته می‌شوند): attributeهای دارای مقدار لیستی باید در میان دستگاه‌ها دو‌به‌دو مجزا (بدون اشتراک) باشند. مقادیر اسکالر برای سازگاری با نسخه‌های قبلی به‌صورت مجموعه‌های تک‌عضوی در نظر گرفته می‌شوند.  این محدودیت عکس MatchAttribute عمل می‌کند و برای جلوگیری از تخصیص چند درخواست به یک دستگاه یکسان، با ایجاد تمایز در سطح attribute به کار می‌رود.  این قابلیت در سناریوهایی مفید است که درخواست‌های منبع باید توسط دستگاه‌های فیزیکی جداگانه برآورده شوند. برای مثال، کانتینری دو رابط شبکه درخواست می‌کند که باید از دو NIC فیزیکی متفاوت تخصیص داده شوند.</td>
    </tr>
    <tr>
      <td><code>matchAttribute</code><br/><em>string</em></td>
      <td>MatchAttribute الزام می‌کند که همه دستگاه‌های مورد نظر این attribute را داشته باشند و نوع و مقدار آن در میان این دستگاه‌ها یکسان باشد.  برای مثال، اگر "dra.example.com/numa" را مشخص کنید (این فقط یک مثال فرضی است!)، فقط دستگاه‌هایی که در یک نود NUMA یکسان قرار دارند انتخاب می‌شوند. دستگاهی که این attribute را نداشته باشد انتخاب نخواهد شد. همه دستگاه‌ها باید برای این attribute مقداری از یک نوع یکسان استفاده کنند، زیرا این موضوع بخشی از مشخصات آن است؛ اما اگر دستگاهی چنین نکند، آن نیز انتخاب نخواهد شد.  هنگامی که feature gate با نام DRAListTypeAttributes فعال باشد، مقایسه با معناشناسی مجموعه‌ای انجام می‌شود (یعنی ترتیب عناصر و تکرارها نادیده گرفته می‌شوند): attributeهای دارای مقدار لیستی زمانی تطابق دارند که اشتراک مقادیر در میان همه دستگاه‌ها تهی نباشد. مقادیر اسکالر برای سازگاری با نسخه‌های قبلی به‌صورت لیست‌های تک‌عضوی در نظر گرفته می‌شوند.  باید شامل پیشوند دامنه (domain) باشد.</td>
    </tr>
    <tr>
      <td><code>requests</code><br/><em>string array</em></td>
      <td>Requests فهرستی از یک یا چند درخواست در این claim است که باید به‌طور مشترک این محدودیت را برآورده کنند. اگر یک درخواست توسط چند دستگاه برآورده شود، همه آن دستگاه‌ها باید محدودیت را رعایت کنند. اگر این فیلد مشخص نشود، محدودیت برای همه درخواست‌های این claim اعمال می‌شود.  ارجاع به زیردرخواست‌ها باید شامل نام درخواست اصلی باشد و می‌تواند زیردرخواست را نیز با قالب \<main request>[/\<subrequest>] دربر بگیرد. اگر فقط درخواست اصلی ذکر شود، محدودیت برای همه زیردرخواست‌ها اعمال می‌شود.</td>
    </tr>
  </tbody>
</table>


## DeviceDerivedAttribute {#DeviceDerivedAttribute}

DeviceDerivedAttribute یک attribute مشتق‌شده را تعریف می‌کند که با CEL محاسبه می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Expression یک عبارت CEL است که روی هر دستگاه کاندیدا ارزیابی می‌شود. این عبارت باید به یک مقدار اسکالر ابتدایی (string، integer، boolean یا semver) یا فهرستی از این مقادیر اسکالر ([]string، []int64، []bool، []semver) ارزیابی شود تا به‌عنوان کلید گروه‌بندی مجازی عمل کند. هر نوع بازگشتی دیگر خطا محسوب می‌شود و ارزیابی CEL برای آن دستگاه را با شکست مواجه می‌کند.  ورودی عبارت، آبجکتی با نام "device" است که همان ویژگی‌های موجود در CELDeviceSelector را دارد.  اگر زمان‌بندی Pod برای برخی دستگاه‌ها با خطاهای زمان اجرای CEL روبه‌رو شود (مانند جست‌وجوی attributeای که تعریف نشده است)، تخصیص را متوقف می‌کند و زمان‌بندی Pod با شکست مواجه می‌شود. نمایش فوری خطاهای ارزیابی از شکست‌های بی‌صدای تطبیق توپولوژی که تشخیصشان بسیار دشوار است جلوگیری می‌کند. یک عبارت مقاوم باید، برای نمونه، پیش از ارجاع به attributeها وجود آن‌ها را بررسی کند تا از خطاهای ارزیابی در زمان اجرا پرهیز شود.  عبارت پس از آن ارزیابی می‌شود که دستگاه از سایر عبارت‌های انتخابگر (selector) درخواستی که این عبارت در آن به کار رفته عبور کرده باشد. این امر امکان نوشتن عبارت‌هایی را فراهم می‌کند که متناسب با دستگاه‌های درخواست‌شده نوشته شده‌اند (برای مثال، با فرض اینکه دستگاه متعلق به فروشنده‌ای خاص است و صرف‌نظر کردن از آن بررسی‌ها).  طول عبارت باید کمتر از یا برابر با 10 Ki باشد. هزینه ارزیابی آن نیز بر اساس تعداد تخمینی گام‌های منطقی محدود شده است؛ هزینه ترکیبی همه attributeهای مشتق‌شده در یک claim با یک بودجه هزینه CEL مشترک سقف‌گذاری می‌شود.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name شناسه این attribute مشتق‌شده است که در constraintها استفاده می‌شود.  این نام باید یک زیردامنه DNS باشد که پس از آن یک اسلش ("/") و سپس یک شناسه زبان C بیاید (مثلاً "example.com/numaNode" یا "derived/numaNode").  اگر نام انتخاب‌شده با یک attribute فیزیکی موجود از یک درایور مطابقت داشته باشد، عبارت attribute مشتق‌شده آن attribute فیزیکی را پوشش می‌دهد (shadow) و مقدار ارزیابی‌شده آن به‌جای مقدار فیزیکی در constraintها استفاده می‌شود. اگر هدف تعریف attribute مشتق‌شده‌ای است که فقط درون ResourceClaim به کار می‌رود و قرار نیست attribute موجودی را پوشش دهد، از پیشوند دامنه‌ای استفاده کنید که هیچ درایور DRA نباید از آن استفاده کند (مثلاً "derived/myAttribute").  تعریف attribute مشتق‌شده‌ای که حداقل در یک constraint استفاده نشود معتبر نیست.</td>
    </tr>
  </tbody>
</table>


## DeviceRequest {#DeviceRequest}

DeviceRequest درخواستی برای دستگاه‌های موردنیاز یک claim است. معمولاً این درخواست برای یک منبع واحد مانند یک دستگاه است، اما می‌توان چند دستگاه یکسان را نیز درخواست کرد. با FirstAvailable می‌توان فهرستی اولویت‌دار از درخواست‌ها نیز ارائه داد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>exactly</code><br/><em><a href="{{< ref "#ExactDeviceRequest" >}}">ExactDeviceRequest</a></em></td>
      <td>Exactly جزئیات یک درخواست واحد را مشخص می‌کند که برای برآورده شدن درخواست باید دقیقاً رعایت شود.  باید یکی از Exactly یا FirstAvailable مقداردهی شود.</td>
    </tr>
    <tr>
      <td><code>firstAvailable</code><br/><em><a href="{{< ref "#DeviceSubRequest" >}}">DeviceSubRequest array</a></em></td>
      <td>FirstAvailable شامل زیردرخواست‌هایی است که زمان‌بند دقیقاً یکی از آن‌ها را انتخاب می‌کند. زمان‌بند می‌کوشد آن‌ها را به همان ترتیبی که در این فهرست آمده‌اند برآورده کند. بنابراین اگر فهرست دو مورد داشته باشد، زمان‌بند تنها در صورتی مورد دوم را بررسی می‌کند که تشخیص دهد مورد اول قابل استفاده نیست.  DRA هنوز امتیازدهی (scoring) را پیاده‌سازی نکرده است، بنابراین زمان‌بند نخستین مجموعه دستگاه‌هایی را که همه درخواست‌های claim را برآورده می‌کند انتخاب می‌کند. اگر الزامات روی بیش از یک نود برآورده شوند، سایر قابلیت‌های زمان‌بندی تعیین می‌کنند کدام نود انتخاب شود. این بدان معناست که مجموعه دستگاه‌های تخصیص‌یافته به یک claim ممکن است بهینه‌ترین مجموعه موجود در کلاستر نباشد. امتیازدهی در آینده پیاده‌سازی خواهد شد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name برای ارجاع به این درخواست در ورودی pod.spec.containers[].resources.claims و در یک constraint از claim به کار می‌رود.  ارجاع با استفاده از نام در DeviceRequest، زمانی که فیلد Exactly مقداردهی شده باشد، یک درخواست را به‌طور یکتا مشخص می‌کند. هنگامی که فیلد FirstAvailable مقداردهی شده باشد، ارجاع به نام DeviceRequest با هر زیردرخواستی که زمان‌بند انتخاب کند تطابق خواهد داشت.  باید یک DNS label باشد.</td>
    </tr>
  </tbody>
</table>


## DeviceRequestAllocationResult {#DeviceRequestAllocationResult}

DeviceRequestAllocationResult نتیجه تخصیص برای یک درخواست را دربر می‌گیرد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>adminAccess</code><br/><em>boolean</em></td>
      <td>AdminAccess نشان می‌دهد که این دستگاه برای دسترسی مدیریتی تخصیص داده شده است. برای تعریف این حالت، فیلد متناظر در درخواست را ببینید.  اگر این فیلد تنظیم نشده یا برابر false باشد، دسترسی مدیریتی غیرفعال است؛ در غیر این صورت فعال است.</td>
    </tr>
    <tr>
      <td><code>bindingConditions</code><br/><em>string array</em></td>
      <td>BindingConditions شامل نسخه‌ای از BindingConditions در ResourceSlice متناظر در زمان تخصیص است.  این فیلد بتا است و فعال‌سازی feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>bindingFailureConditions</code><br/><em>string array</em></td>
      <td>BindingFailureConditions شامل نسخه‌ای از BindingFailureConditions در ResourceSlice متناظر در زمان تخصیص است.  این فیلد بتا است و فعال‌سازی feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>consumedCapacity</code><br/><em>object</em></td>
      <td>ConsumedCapacity میزان ظرفیت مصرف‌شده برای هر دستگاه را به‌عنوان بخشی از درخواست claim ردیابی می‌کند. مقدار مصرف‌شده ممکن است با مقدار درخواست‌شده تفاوت داشته باشد: در صورت وجود requestPolicy برای دستگاه، این مقدار به نزدیک‌ترین مقدار معتبر بر اساس آن رو به بالا گرد می‌شود (یعنی نمی‌تواند کمتر از مقدار درخواست‌شده باشد).  مجموع ظرفیت مصرف‌شده برای هر دستگاه نباید از Value در DeviceCapacity بیشتر شود.  این فیلد فقط برای دستگاه‌هایی مقداردهی می‌شود که تخصیص چندگانه را مجاز می‌دانند. همه ورودی‌های ظرفیت، حتی اگر مقدار مصرف‌شده صفر باشد، درج می‌شوند.</td>
    </tr>
    <tr>
      <td><code>device</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Device با نام یک نمونه دستگاه در resource pool مربوط به درایور، به آن دستگاه ارجاع می‌دهد. باید یک DNS label باشد.</td>
    </tr>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Driver نام درایور DRA را مشخص می‌کند که پس از نیاز به claim روی یک نود، باید افزونه kubelet آن برای پردازش تخصیص فراخوانی شود.  باید یک زیردامنه DNS باشد و بهتر است به یک دامنه DNS متعلق به فروشنده درایور ختم شود. فقط باید از حروف کوچک استفاده کند.</td>
    </tr>
    <tr>
      <td><code>pool</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>این نام به‌همراه نام درایور و فیلد نام دستگاه مشخص می‌کند کدام دستگاه تخصیص داده شده است (`\<driver name>/\<pool name>/\<device name>`).  طول آن نباید از 253 نویسه بیشتر باشد و می‌تواند شامل یک یا چند زیردامنه DNS باشد که با اسلش از هم جدا شده‌اند.</td>
    </tr>
    <tr>
      <td><code>request</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Request نام درخواستی در claim است که موجب تخصیص این دستگاه شده است. اگر به زیردرخواستی در فهرست firstAvailable یک DeviceRequest ارجاع دهد، این فیلد باید هم نام درخواست اصلی و هم زیردرخواست را با قالب \<main request>/\<subrequest> شامل شود.  ممکن است برای هر درخواست چند دستگاه تخصیص داده شده باشد.</td>
    </tr>
    <tr>
      <td><code>shareID</code><br/><em>string</em></td>
      <td>ShareID یک سهم تخصیص منفرد از دستگاه را به‌طور یکتا شناسایی می‌کند و زمانی استفاده می‌شود که دستگاه از چند تخصیص هم‌زمان پشتیبانی می‌کند. این مقدار به‌عنوان کلید اضافی در map برای تمایز سهم‌های هم‌زمان یک دستگاه یکسان عمل می‌کند.</td>
    </tr>
    <tr>
      <td><code>skipNodeOperations</code><br/><em>string array</em></td>
      <td>SkipNodeOperations عملیات منبع محلی نود (فراخوانی‌های gRPC) را فهرست می‌کند که هنگام تعیین ضرورت انجام عملیات روی نود، برای این دستگاه تخصیص‌یافته نادیده گرفته می‌شوند. اگر همه دستگاه‌های تخصیص‌یافته یک درایور در یک claim یک عملیات را نادیده بگیرند، آن فراخوانی gRPC انجام نمی‌شود. این فیلد نسخه‌ای از مقدار ResourceSlice.spec.skipNodeOperations در زمان تخصیص دستگاه است.</td>
    </tr>
    <tr>
      <td><code>tolerations</code><br/><em><a href="{{< ref "#DeviceToleration" >}}">DeviceToleration array</a></em></td>
      <td>نسخه‌ای از همه tolerationهای مشخص‌شده در درخواست، در زمان تخصیص دستگاه.  حداکثر تعداد tolerationها 16 است.  این فیلد بتا است و فعال‌سازی feature gate با نام DRADeviceTaints را لازم دارد.</td>
    </tr>
  </tbody>
</table>

## DeviceSubRequest {#DeviceSubRequest}

DeviceSubRequest درخواستی برای یک دستگاه را توصیف می‌کند که در آرایهٔ claim.spec.devices.requests[].firstAvailable ارائه شده است. هر یک از این درخواست‌ها معمولاً برای یک منبع واحد مانند یک دستگاه است، اما می‌تواند چند دستگاه یکسان را نیز درخواست کند.

DeviceSubRequest شبیه ExactDeviceRequest است، اما فیلد AdminAccess را ارائه نمی‌کند، زیرا آن فیلد فقط هنگام درخواست یک دستگاه مشخص پشتیبانی می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allocationMode</code><br/><em>string</em></td>
      <td>فیلد AllocationMode و فیلدهای مرتبط با آن تعیین می‌کنند که دستگاه‌ها برای برآورده کردن این زیردرخواست چگونه تخصیص داده شوند. مقادیر پشتیبانی‌شده عبارت‌اند از:  - ExactCount: این درخواست برای تعداد مشخصی دستگاه است.   این حالت پیش‌فرض است. تعداد دقیق در فیلد count   تعیین می‌شود.  - All: این زیردرخواست برای تمام دستگاه‌های منطبق در یک pool است.   اگر برخی از دستگاه‌ها از قبل تخصیص داده شده باشند، تخصیص با شکست مواجه می‌شود،   مگر اینکه adminAccess درخواست شده باشد.  اگر AllocationMode مشخص نشود، حالت پیش‌فرض ExactCount است. اگر حالت ExactCount باشد و count مشخص نشده باشد، تعداد پیش‌فرض یک است. سایر زیردرخواست‌ها باید این فیلد را مشخص کنند.  ممکن است در آینده حالت‌های بیشتری اضافه شوند. کلاینت‌ها باید از پردازش درخواست‌هایی که حالت ناشناخته دارند خودداری کنند.<br/><br/>Possible enum values:<br/> - `"All"`<br/> - `"ExactCount"`</td>
    </tr>
    <tr>
      <td><code>capacity</code><br/><em><a href="{{< ref "#CapacityRequirements" >}}">CapacityRequirements</a></em></td>
      <td>فیلد Capacity نیازمندی‌های منبع را برای هر ظرفیت (capacity) تعریف می‌کند.  اگر این فیلد تنظیم نشده باشد و دستگاه از تخصیص‌های چندگانه پشتیبانی کند، مقدار پیش‌فرض بر اساس requestPolicy برای هر ظرفیت اعمال می‌شود. برای ظرفیتی که requestPolicy ندارد، مقدار پیش‌فرض برابر با کل مقدار ظرفیت است.  این مقدار بر هر تخصیص دستگاه اعمال می‌شود. اگر Count > 1 باشد و تعداد دستگاه‌های برآورنده نیازمندی‌ها کافی نباشد، درخواست با شکست مواجه می‌شود. اگر AllocationMode روی All تنظیم شده باشد و دستگاه‌هایی وجود داشته باشند که از جهات دیگر با درخواست منطبق‌اند و این ظرفیت را با مقداری >= مقدار درخواستی دارند، اما نمی‌توان آن‌ها را به این درخواست تخصیص داد، درخواست با شکست مواجه می‌شود.</td>
    </tr>
    <tr>
      <td><code>count</code><br/><em>integer</em></td>
      <td>فیلد Count فقط زمانی استفاده می‌شود که حالت تعداد "ExactCount" باشد. مقدار آن باید بزرگ‌تر از صفر باشد. اگر AllocationMode برابر ExactCount باشد و این فیلد مشخص نشده باشد، مقدار پیش‌فرض یک است.</td>
    </tr>
    <tr>
      <td><code>derivedAttributes</code><br/><em><a href="{{< ref "#DeviceDerivedAttribute" >}}">DeviceDerivedAttribute array</a></em></td>
      <td>فیلد DerivedAttributes مجموعه‌ای از ویژگی‌های مجازی را تعریف می‌کند که برای هر دستگاه کاندید از طریق عبارت‌های CEL محاسبه می‌شوند. می‌توان در `.devices.constraints` به این ویژگی‌های مجازی ارجاع داد تا دستگاه‌های مختلف (مثلاً تخصیص هم‌زمان یک GPU و یک NIC روی همان نود NUMA) حتی در صورتی که درایورهایشان ویژگی‌های متفاوتی منتشر می‌کنند، با هم هم‌تراز و منطبق شوند. ویژگی‌های مشتق‌شده هنگام ارزیابی عبارت‌های انتخابگر (selector) در محیط CEL از طریق `device.attributes` در دسترس نیستند.  ویژگی‌های مشتق‌شده به شما امکان می‌دهند اطلاعات توپولوژی را در زمان زمان‌بندی استخراج، تبدیل یا نرمال‌سازی کنید (مانند استخراج اندیس NUMA از یک رشتهٔ توپولوژی پیچیده یا تغییر نام یک ویژگی مختص فروشنده) و آن را به یک نام ویژگی مجازی مشترک تبدیل کنید. سپس زمان‌بند هنگام تطبیق محدودیت‌ها، این ویژگی‌های مجازی را دقیقاً مانند ویژگی‌های ایستا ارزیابی می‌کند.  هر ویژگی مشتق‌شده‌ای که در این فهرست تعریف می‌شود باید دست‌کم توسط یک محدودیت MatchAttribute یا DistinctAttribute در فهرست `.devices.constraints` ارجاع داده شود.  حداکثر تعداد ویژگی‌های مشتق‌شده ۳۲ است.  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام DRADerivedAttributes را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>deviceClassName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد DeviceClassName به یک DeviceClass مشخص ارجاع می‌دهد که می‌تواند پیکربندی و انتخابگرهای اضافی تعریف کند تا این زیردرخواست آن‌ها را به ارث ببرد.  وجود یک کلاس الزامی است. کلاس‌های در دسترس به کلاستر بستگی دارند.  مدیران می‌توانند با نصب کلاس‌هایی که فقط انتخابگرهای دستگاه‌های مجاز را دارند، از این قابلیت برای محدود کردن دستگاه‌های قابل درخواست استفاده کنند. اگر کاربران آزادند بدون محدودیت هر چیزی را درخواست کنند، مدیران می‌توانند یک DeviceClass خالی بسازند تا کاربران به آن ارجاع دهند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>از Name می‌توان برای ارجاع به این زیردرخواست در فهرست محدودیت‌ها یا فهرست پیکربندی‌های claim استفاده کرد. ارجاع‌ها باید از قالب \<main request>/\<subrequest> پیروی کنند.  مقدار آن باید یک DNS label باشد.</td>
    </tr>
    <tr>
      <td><code>selectors</code><br/><em><a href="{{< ref "device-class-v1#DeviceSelector" >}}">DeviceSelector array</a></em></td>
      <td>Selectors معیارهایی را تعریف می‌کنند که یک دستگاه مشخص باید برآورده کند تا برای این زیردرخواست در نظر گرفته شود. برای اینکه یک دستگاه در نظر گرفته شود، همهٔ انتخابگرها باید برآورده شوند.</td>
    </tr>
    <tr>
      <td><code>tolerations</code><br/><em><a href="{{< ref "#DeviceToleration" >}}">DeviceToleration array</a></em></td>
      <td>در صورت مشخص شدن، tolerationهای درخواست را تعیین می‌کند.  برای تخصیص دستگاهی که taint با اثر NoSchedule دارد، toleration متناظر با NoSchedule لازم است. همین امر دربارهٔ NoExecute نیز صادق است.  علاوه بر این، اگر پس از تخصیص، هر یک از دستگاه‌های تخصیص‌یافته با اثر NoExecute دارای taint شود و این اثر تحمل نشده باشد، همهٔ podهایی که از ResourceClaim استفاده می‌کنند حذف می‌شوند تا از دستگاه خارج شوند. تا زمانی که این دستگاه‌های دارای taint وجود دارند، زمان‌بند اجازه نمی‌دهد podهای جدید claim را رزرو کنند. پس از خارج شدن همهٔ podها، تخصیص claim لغو می‌شود.  حداکثر تعداد tolerationها ۱۶ است.  این فیلد بتا است و برای استفاده از آن باید feature gate با نام DRADeviceTaints را فعال کنید.</td>
    </tr>
  </tbody>
</table>


## DeviceToleration {#DeviceToleration}

ResourceClaim‌ای که این DeviceToleration به آن پیوست شده است، هر taint منطبق با سه‌تایی &lt;key,value,effect&gt; را با استفاده از عملگر تطبیق &lt;operator&gt; تحمل می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>effect</code><br/><em>string</em></td>
      <td>Effect اثر taint را برای تطبیق مشخص می‌کند. مقدار خالی به معنای تطبیق با همهٔ اثرهای taint است. در صورت مشخص شدن، مقادیر مجاز NoSchedule و NoExecute هستند.<br/><br/>Possible enum values:<br/> - `"NoExecute"` هر podی را که در حال اجراست و taint دستگاه را تحمل نمی‌کند، خارج (evict) می‌کند.<br/> - `"NoSchedule"` اجازه نمی‌دهد podهای جدیدی که از دستگاه دارای taint استفاده می‌کنند زمان‌بندی شوند، مگر اینکه taint را تحمل کنند؛ اما به همهٔ podهایی که بدون عبور از زمان‌بند مستقیماً به Kubelet ارسال شده‌اند اجازهٔ شروع می‌دهد و همهٔ podهای در حال اجرا نیز به کار خود ادامه می‌دهند.<br/> - `"None"` بدون اثر؛ taint صرفاً جنبهٔ اطلاع‌رسانی دارد.</td>
    </tr>
    <tr>
      <td><code>key</code><br/><em>string</em></td>
      <td>Key کلید taint است که toleration بر آن اعمال می‌شود. مقدار خالی به معنای تطبیق با همهٔ کلیدهای taint است. اگر کلید خالی باشد، operator باید Exists باشد؛ این ترکیب به معنای تطبیق با همهٔ مقادیر و همهٔ کلیدهاست. باید یک نام برچسب (label) معتبر باشد.</td>
    </tr>
    <tr>
      <td><code>operator</code><br/><em>string</em></td>
      <td>Operator رابطهٔ یک کلید را با مقدار آن نشان می‌دهد. عملگرهای معتبر Exists و Equal هستند و مقدار پیش‌فرض Equal است. Exists معادل یک wildcard برای مقدار است، به‌طوری که یک ResourceClaim می‌تواند همهٔ taintهای یک دستهٔ مشخص را تحمل کند.<br/><br/>Possible enum values:<br/> - `"Equal"`<br/> - `"Exists"`</td>
    </tr>
    <tr>
      <td><code>tolerationSeconds</code><br/><em>integer</em></td>
      <td>TolerationSeconds مدت زمانی را نشان می‌دهد که toleration (که باید اثر NoExecute داشته باشد، وگرنه این فیلد نادیده گرفته می‌شود) taint را تحمل می‌کند. به‌طور پیش‌فرض تنظیم نشده است، یعنی taint برای همیشه تحمل می‌شود (خارج‌سازی انجام نمی‌شود). سیستم مقدار صفر و مقادیر منفی را برابر ۰ در نظر می‌گیرد (خارج‌سازی فوری). اگر مقدار بزرگ‌تر از صفر باشد، زمانی که pod باید خارج شود به‌صورت \<time when taint was adedd> + \<toleration seconds> محاسبه می‌شود.</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em>string</em></td>
      <td>Value مقدار taint است که toleration با آن تطبیق می‌یابد. اگر operator برابر Exists باشد، مقدار باید خالی باشد؛ در غیر این صورت یک رشتهٔ معمولی است. باید یک مقدار برچسب (label) معتبر باشد.</td>
    </tr>
  </tbody>
</table>


## ExactDeviceRequest {#ExactDeviceRequest}

ExactDeviceRequest درخواستی برای یک یا چند دستگاه یکسان است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>adminAccess</code><br/><em>boolean</em></td>
      <td>AdminAccess نشان می‌دهد که این claim برای دسترسی مدیریتی به دستگاه‌ها است. انتظار می‌رود claimهای دارای AdminAccess برای پایش یا سایر سرویس‌های مدیریتی یک دستگاه استفاده شوند.  این claimها همهٔ claimهای معمولی مربوط به دستگاه را از نظر حالت‌های دسترسی و هرگونه تخصیص منبع نادیده می‌گیرند.  اگر این فیلد تنظیم نشده یا روی false تنظیم شده باشد، دسترسی مدیریتی غیرفعال است؛ در غیر این صورت فعال است.</td>
    </tr>
    <tr>
      <td><code>allocationMode</code><br/><em>string</em></td>
      <td>فیلد AllocationMode و فیلدهای مرتبط با آن تعیین می‌کنند که دستگاه‌ها برای برآورده کردن این درخواست چگونه تخصیص داده شوند. مقادیر پشتیبانی‌شده عبارت‌اند از:  - ExactCount: این درخواست برای تعداد مشخصی دستگاه است.   این حالت پیش‌فرض است. تعداد دقیق در فیلد count   تعیین می‌شود.  - All: این درخواست برای تمام دستگاه‌های منطبق در یک pool است.   برای موفقیت تخصیص، دست‌کم یک دستگاه باید روی نود وجود داشته باشد.   اگر برخی از دستگاه‌ها از قبل تخصیص داده شده باشند، تخصیص با شکست مواجه می‌شود،   مگر اینکه adminAccess درخواست شده باشد.  اگر AllocationMode مشخص نشود، حالت پیش‌فرض ExactCount است. اگر حالت ExactCount باشد و count مشخص نشده باشد، تعداد پیش‌فرض یک است. سایر درخواست‌ها باید این فیلد را مشخص کنند.  ممکن است در آینده حالت‌های بیشتری اضافه شوند. کلاینت‌ها باید از پردازش درخواست‌هایی که حالت ناشناخته دارند خودداری کنند.<br/><br/>Possible enum values:<br/> - `"All"`<br/> - `"ExactCount"`</td>
    </tr>
    <tr>
      <td><code>capacity</code><br/><em><a href="{{< ref "#CapacityRequirements" >}}">CapacityRequirements</a></em></td>
      <td>فیلد Capacity نیازمندی‌های منبع را برای هر ظرفیت (capacity) تعریف می‌کند.  اگر این فیلد تنظیم نشده باشد و دستگاه از تخصیص‌های چندگانه پشتیبانی کند، مقدار پیش‌فرض بر اساس requestPolicy برای هر ظرفیت اعمال می‌شود. برای ظرفیتی که requestPolicy ندارد، مقدار پیش‌فرض برابر با کل مقدار ظرفیت است.  این مقدار بر هر تخصیص دستگاه اعمال می‌شود. اگر Count > 1 باشد و تعداد دستگاه‌های برآورنده نیازمندی‌ها کافی نباشد، درخواست با شکست مواجه می‌شود. اگر AllocationMode روی All تنظیم شده باشد و دستگاه‌هایی وجود داشته باشند که از جهات دیگر با درخواست منطبق‌اند و این ظرفیت را با مقداری >= مقدار درخواستی دارند، اما نمی‌توان آن‌ها را به این درخواست تخصیص داد، درخواست با شکست مواجه می‌شود.</td>
    </tr>
    <tr>
      <td><code>count</code><br/><em>integer</em></td>
      <td>فیلد Count فقط زمانی استفاده می‌شود که حالت تعداد "ExactCount" باشد. مقدار آن باید بزرگ‌تر از صفر باشد. اگر AllocationMode برابر ExactCount باشد و این فیلد مشخص نشده باشد، مقدار پیش‌فرض یک است.</td>
    </tr>
    <tr>
      <td><code>derivedAttributes</code><br/><em><a href="{{< ref "#DeviceDerivedAttribute" >}}">DeviceDerivedAttribute array</a></em></td>
      <td>فیلد DerivedAttributes مجموعه‌ای از ویژگی‌های مجازی را تعریف می‌کند که برای هر دستگاه کاندید از طریق عبارت‌های CEL محاسبه می‌شوند. می‌توان در `.devices.constraints` به این ویژگی‌های مجازی ارجاع داد تا دستگاه‌های مختلف (مثلاً تخصیص هم‌زمان یک GPU و یک NIC روی همان نود NUMA) حتی در صورتی که درایورهایشان ویژگی‌های متفاوتی منتشر می‌کنند، با هم هم‌تراز و منطبق شوند. ویژگی‌های مشتق‌شده هنگام ارزیابی عبارت‌های انتخابگر (selector) در محیط CEL از طریق `device.attributes` در دسترس نیستند.  ویژگی‌های مشتق‌شده به شما امکان می‌دهند اطلاعات توپولوژی را در زمان زمان‌بندی استخراج، تبدیل یا نرمال‌سازی کنید (مانند استخراج اندیس NUMA از یک رشتهٔ توپولوژی پیچیده یا تغییر نام یک ویژگی مختص فروشنده) و آن را به یک نام ویژگی مجازی مشترک تبدیل کنید. سپس زمان‌بند هنگام تطبیق محدودیت‌ها، این ویژگی‌های مجازی را دقیقاً مانند ویژگی‌های ایستا ارزیابی می‌کند.  هر ویژگی مشتق‌شده‌ای که در این فهرست تعریف می‌شود باید دست‌کم توسط یک محدودیت MatchAttribute یا DistinctAttribute در فهرست `.devices.constraints` ارجاع داده شود.  حداکثر تعداد ویژگی‌های مشتق‌شده ۳۲ است.  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام DRADerivedAttributes را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>deviceClassName</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد DeviceClassName به یک DeviceClass مشخص ارجاع می‌دهد که می‌تواند پیکربندی و انتخابگرهای اضافی تعریف کند تا این درخواست آن‌ها را به ارث ببرد.  تعیین DeviceClassName الزامی است.  مدیران می‌توانند با نصب کلاس‌هایی که فقط انتخابگرهای دستگاه‌های مجاز را دارند، از این قابلیت برای محدود کردن دستگاه‌های قابل درخواست استفاده کنند. اگر کاربران آزادند بدون محدودیت هر چیزی را درخواست کنند، مدیران می‌توانند یک DeviceClass خالی بسازند تا کاربران به آن ارجاع دهند.</td>
    </tr>
    <tr>
      <td><code>selectors</code><br/><em><a href="{{< ref "device-class-v1#DeviceSelector" >}}">DeviceSelector array</a></em></td>
      <td>Selectors معیارهایی را تعریف می‌کنند که یک دستگاه مشخص باید برآورده کند تا برای این درخواست در نظر گرفته شود. برای اینکه یک دستگاه در نظر گرفته شود، همهٔ انتخابگرها باید برآورده شوند.</td>
    </tr>
    <tr>
      <td><code>tolerations</code><br/><em><a href="{{< ref "#DeviceToleration" >}}">DeviceToleration array</a></em></td>
      <td>در صورت مشخص شدن، tolerationهای درخواست را تعیین می‌کند.  برای تخصیص دستگاهی که taint با اثر NoSchedule دارد، toleration متناظر با NoSchedule لازم است. همین امر دربارهٔ NoExecute نیز صادق است.  علاوه بر این، اگر پس از تخصیص، هر یک از دستگاه‌های تخصیص‌یافته با اثر NoExecute دارای taint شود و این اثر تحمل نشده باشد، همهٔ podهایی که از ResourceClaim استفاده می‌کنند حذف می‌شوند تا از دستگاه خارج شوند. تا زمانی که این دستگاه‌های دارای taint وجود دارند، زمان‌بند اجازه نمی‌دهد podهای جدید claim را رزرو کنند. پس از خارج شدن همهٔ podها، تخصیص claim لغو می‌شود.  حداکثر تعداد tolerationها ۱۶ است.  این فیلد بتا است و برای استفاده از آن باید feature gate با نام DRADeviceTaints را فعال کنید.</td>
    </tr>
  </tbody>
</table>


## NetworkDeviceData {#NetworkDeviceData}

NetworkDeviceData جزئیات مرتبط با شبکه را برای دستگاه تخصیص‌یافته فراهم می‌کند. درایورها یا مؤلفه‌های دیگر می‌توانند این اطلاعات را برای پیکربندی یا شناسایی دستگاه در یک بستر شبکه‌ای تکمیل کنند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>hardwareAddress</code><br/><em>string</em></td>
      <td>HardwareAddress آدرس سخت‌افزاری (مثلاً MAC Address) رابط شبکهٔ دستگاه را نشان می‌دهد.  طول آن نباید بیش از ۱۲۸ بایت باشد.</td>
    </tr>
    <tr>
      <td><code>interfaceName</code><br/><em>string</em></td>
      <td>InterfaceName نام رابط شبکه‌ای را که با دستگاه تخصیص‌یافته مرتبط است مشخص می‌کند. این نام می‌تواند نام یک رابط شبکهٔ فیزیکی یا مجازی باشد که در pod پیکربندی می‌شود.  طول آن نباید بیش از ۲۵۶ بایت باشد.</td>
    </tr>
    <tr>
      <td><code>ips</code><br/><em>string array</em></td>
      <td>IPs آدرس‌های شبکه‌ای را که به رابط شبکهٔ دستگاه اختصاص داده شده‌اند فهرست می‌کند. این فهرست می‌تواند شامل آدرس‌های IPv4 و IPv6 باشد. آدرس‌ها در نمادگذاری CIDR هستند که هم آدرس و هم ماسک زیرشبکهٔ مرتبط را شامل می‌شود؛ برای مثال: "192.0.2.5/24" برای IPv4 و "2001:db8::5/64" برای IPv6.</td>
    </tr>
  </tbody>
</table>


## ResourceClaimConsumerReference {#ResourceClaimConsumerReference}

ResourceClaimConsumerReference اطلاعات کافی برای یافتن مصرف‌کنندهٔ یک ResourceClaim را در خود دارد. کاربر باید منبعی در همان فضای نام (namespace) ResourceClaim باشد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiGroup</code><br/><em>string</em></td>
      <td>APIGroup گروه منبعی است که به آن ارجاع داده می‌شود. برای API هسته (core) خالی است. این مقدار با گروه موجود در APIVersion که هنگام ایجاد منابع استفاده می‌شود، مطابقت دارد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name نام منبعی است که به آن ارجاع داده می‌شود.</td>
    </tr>
    <tr>
      <td><code>resource</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Resource نوع منبعی است که به آن ارجاع داده می‌شود، برای مثال "pods".</td>
    </tr>
    <tr>
      <td><code>uid</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>UID دقیقاً یک نمونهٔ مشخص از منبع را شناسایی می‌کند.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>

### `post` Create

#### درخواست HTTP

`POST /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته dryRun باعث بازگشت پاسخ خطا می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از فیلدهای تکراری، فقط آخرین فیلدی را که رمزگشا (decoder) با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق سرایند استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### درخواست HTTP

`PATCH /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته dryRun باعث بازگشت پاسخ خطا می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از فیلدهای تکراری، فقط آخرین فیلدی را که رمزگشا (decoder) با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق سرایند استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. یعنی کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر از apply، پرچم force نباید تنظیم شده باشد.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace

#### درخواست HTTP

`PUT /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته dryRun باعث بازگشت پاسخ خطا می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از فیلدهای تکراری، فقط آخرین فیلدی را که رمزگشا (decoder) با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق سرایند استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه فیلدهای ناشناخته و تکراری شناسایی‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete

#### درخواست HTTP

`DELETE /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}`


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته dryRun باعث بازگشت پاسخ خطا می‌شود و درخواست دیگر پردازش نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر یعنی حذف فوری. اگر این مقدار nil باشد، دوره مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت اعمال می‌شود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) غیرقابل تبدیل بودن داده‌های آن، مثلاً شکست در رمزگشایی، یا ب) ناموفق بودن رمزگشایی آن به آبجکت، نتوان آن را با موفقیت از ذخیره‌ساز زیربنایی بازیابی کرد. توجه: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف متکی باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آن را صراحتاً فعال کند.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام «orphan» به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا زباله‌روبی (garbage collection) انجام شود و چگونه. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مخصوص هر منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند. سرور فهرستی را از کلید بعدی و از آخرین snapshot برمی‌گرداند که با نتایج قبلی فهرست ناسازگار است؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است شروع کنند و هیچ تغییری را از دست نخواهند داد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته باعث بازگشت پاسخ خطا می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگشتی بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح غیرمنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از دوره مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض برای هر آبجکت اعمال می‌شود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع آغاز می‌شود. یک منبع در این حالت‌ها خراب در نظر گرفته می‌شود که به‌دلیل الف) ناتوانی در تبدیل داده‌های آن، مثلاً شکست در رمزگشایی، یا ب) ناتوانی در رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به جریان عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگشتی بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراپیوند (metadata) فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواست‌شده (حتی صفر آیتم) برگرداند، در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند؛ کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه اولین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه شکلی. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص هر منبع تعیین می‌شود. مقادیر قابل قبول: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌دهد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan   به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با یک `resourceVersion`   که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه باشد همگام شده باشد.   اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای   که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد،   خطای Invalid برگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگشتی را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو ریشه‌گرفته از آبجکت به سبک CEL (مثلاً "object.metadata.uid") استفاده می‌کنند، نه قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL و داخل تک‌کوتیشن با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را در فضای hash ‏FNV-1a ۶۴ بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>

### `get` List

#### HTTP Request

GET /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت (auth scope)، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور، باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور می‌تواند مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی روی سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست سازگار نیست. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرطی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بی‌آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌هاست.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌هاست.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواست‌شده (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در آن صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی روی این تعیین می‌کند که درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، قویاً توصیه می‌شود resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، تنظیم گزینه `resourceVersionMatch` نیز الزامی است. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌هایی که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشند» و رویداد bookmark زمانی ارسال می‌شود که وضعیت با یک `resourceVersion` همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر منطقی OR) برای مشخص کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector (یعنی "metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که داخل تک‌نقل‌قول قرار می‌گیرند و پیشوند '0x' دارند؛ این دو مقدار به‌ترتیب کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash ‏64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaimList" >}}">ResourceClaimList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست همه فضاهای نام

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/resourceclaims



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و bookmarkها به صلاحدید سرور ارسال می‌شوند. کلاینت‌ها نباید فرض کنند bookmarkها در بازه زمانی مشخصی برگردانده می‌شوند و نباید فرض کنند سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک کوئری قبلی را با پارامترهای کوئری یکسان (به جز خود مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) یا تغییر پیکربندی سرور دیگر معتبر نباشد، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از "کلید بعدی" باشد، در پاسخ گنجانده می‌شوند. این فیلد وقتی watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج استفاده کرد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) برگرداند و کلاینت‌ها برای تشخیص وجود نتایج بیشتر فقط باید به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند نتیجه دیگری وجود ندارد. این فیلد وقتی watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده است، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از مرورگر یا ابزار HTTP خط فرمان (curl و wget) می‌آید.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را بر نسخه‌های منبعی که درخواست می‌تواند از آن‌ها پاسخ داده شود اعمال می‌کند. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند.  وقتی گزینه `sendInitialEvents` تنظیم شده باشد، تنظیم گزینه `resourceVersionMatch` نیز الزامی است. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا `resourceVersion`ی همگام شده باشد که به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL داخل تک‌کوتیشن با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای هش 64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای شامل‌نشونده آن برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌کردن feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به فعالیت یا عدم فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaimList" >}}">ResourceClaimList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته می‌شود و با نتایج قبلی فهرست ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) بازگرداند و کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه نتیجه اولین فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه دهد. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از آن RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به این معنا تفسیر می‌شود که «داده‌ها دست‌کم به تازگی `resourceVersion` ارائه‌شده باشند» و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal تک‌نقل‌قولی CEL با پیشوند '0x' هستند و کران پایین فراگیر (inclusive) و کران بالای ناشامل (exclusive) را بر فضای hash ‏FNV-1a ۶۴ بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است و کران بالای ناشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue مربوط به نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور می‌تواند مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است پاسخ می‌دهد. این فهرست با نتایج قبلی سازگار نیست: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد وقتی watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج از آن استفاده کرد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) بازگرداند و کلاینت‌ها برای تشخیص وجود نتایج بیشتر فقط باید به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد وقتی watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده است در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده می‌کند. اگر آبجکت‌ها در طول فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از چه نسخه‌های منبعی ممکن است پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را ارائه دهد. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌دهد و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") استفاده نمی‌کند. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که داخل single-quote قرار می‌گیرند و پیشوند '0x' دارند. این دو مقدار کران پایین (شامل خود مقدار) و کران بالا (بدون خود مقدار) را روی فضای hash الگوریتم FNV-1a ۶۴ بیتی تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای آن، که در بازه گنجانده نمی‌شود، برابر با 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز دارد که feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، بدون توجه به فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List All Namespaces

#### درخواست HTTP

درخواست `GET /apis/resource.k8s.io/v1/watch/resourceclaims`

#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند رویدادهای watch با نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌ای مشخص برگردانده می‌شوند، و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک توکن continue با خطای 410 ResourceExpired پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده ارسال کند. در این حالت سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است؛ آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از "کلید بعدی" باشد، در پاسخ می‌آیند. این فیلد هنگامی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است شروع کنند، بدون اینکه تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج از آن استفاده کرد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، کمتر از تعداد درخواست‌شده مورد (حتی صفر مورد) برگرداند و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد هنگامی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های برگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد در درخواست‌های بعدیِ ادامه‌دار نخواهد آمد. به این ویژگی گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده می‌کند. اگر آبجکت‌ها در طول فهرست‌گیریِ تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه نتیجه اول فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این شرح است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود که «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای دست‌کم به‌تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های برگردانده‌شده را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌نقل‌قول قرار می‌گیرند و پیشوند '0x' دارند؛ آن‌ها کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز دارد feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به هرگونه فعالیت یا عدم فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>

#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `patch` Patch Status

#### درخواست HTTP

درخواست `PATCH /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status`

#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه احراز هویت و مجوزدهی، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>

#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا می‌انجامد و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول این مقدار باید کمتر از ۱۲۸ کاراکتر یا برابر با آن باشد و فقط شامل کاراکترهای قابل چاپ باشد، به‌طوری که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است. این فیلد برای درخواست‌های apply (‏application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (‏JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از فیلدهای تکراری، همه را جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مواجه‌شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. یعنی کاربر فیلدهای دارای تعارض را که متعلق به دیگران است دوباره در اختیار می‌گیرد. پرچم Force باید برای درخواست‌های patch غیر از apply تنظیم نشده باشد.</td>
    </tr>
  </tbody>
</table>

#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>

#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Read Status

#### درخواست HTTP

درخواست `GET /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status`

#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه احراز هویت و مجوزدهی، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>

#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
  </tbody>
</table>

#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>

### `put` Replace Status

#### درخواست HTTP

درخواست `PUT /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status`

#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceClaim</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و دامنه احراز هویت و مجوزدهی، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>

#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا می‌انجامد و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول این مقدار باید کمتر از ۱۲۸ کاراکتر یا برابر با آن باشد و فقط شامل کاراکترهای قابل چاپ باشد، به‌طوری که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از فیلدهای تکراری، همه را جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری مواجه‌شده است.</td>
    </tr>
  </tbody>
</table>

#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>

#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-claim-v1#ResourceClaim" >}}">ResourceClaim</a></em></td>
    </tr>
  </tbody>
</table>
