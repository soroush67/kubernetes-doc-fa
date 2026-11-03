---
api_metadata:
  apiVersion: "resource.k8s.io/v1"
  import: "k8s.io/api/resource/v1"
  kind: "ResourceSlice"
content_type: "api_reference"
description: "ResourceSlice یک یا چند منبع را در یک pool از منابع مشابه که توسط یک درایور مشترک مدیریت می‌شوند، نمایش می‌دهد. یک pool می‌تواند بیش از یک ResourceSlice را در بر بگیرد و درایور تعیین می‌کند که دقیقاً چند ResourceSlice یک pool را تشکیل دهند.\n\nدر حال حاضر تنها منابع پشتیبانی‌شده، دستگاه‌هایی (device) با ویژگی‌ها (attributes) و ظرفیت‌ها (capacities) هستند. هر دستگاه در یک pool مشخص، صرف‌نظر از تعداد ResourceSliceها، باید نام یکتا داشته باشد. ResourceSliceای که یک دستگاه در آن منتشر می‌شود ممکن است با گذشت زمان تغییر کند. شناسه یکتای یک دستگاه چندتایی &lt;driver name&gt;, &lt;pool name&gt;, &lt;device name&gt; است.\n\nهرگاه درایور نیاز به به‌روزرسانی یک pool داشته باشد، عدد pool.Spec.Pool.Generation را افزایش می‌دهد و همه ResourceSliceها را با این عدد جدید و تعریف‌های جدید منابع به‌روزرسانی می‌کند. مصرف‌کننده باید فقط از ResourceSliceهایی استفاده کند که بالاترین شماره generation را دارند و بقیه را نادیده بگیرد.\n\nهنگام تخصیص همه منابع یک pool که با معیارهای مشخصی مطابقت دارند، یا هنگام جست‌وجوی بهترین راه‌حل میان چند گزینه مختلف، مصرف‌کننده باید تعداد ResourceSliceهای موجود در یک pool (که در هر ResourceSlice درج شده است) را بررسی کند تا مشخص شود دید او از pool کامل است یا خیر. اگر کامل نیست، باید منتظر بماند تا درایور به‌روزرسانی pool را به پایان برساند.\n\nبرای منابعی که محلی یک نود نیستند، نام نود تنظیم نمی‌شود. در این حالت، درایور می‌تواند از یک node selector برای مشخص کردن محل دسترس‌پذیر بودن دستگاه‌ها استفاده کند."
title: "ResourceSlice"
weight: 60
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


## ResourceSlice {#ResourceSlice}

ResourceSlice یک یا چند منبع را در یک pool از منابع مشابه که توسط یک درایور مشترک مدیریت می‌شوند، نمایش می‌دهد. یک pool می‌تواند بیش از یک ResourceSlice را در بر بگیرد و درایور تعیین می‌کند که دقیقاً چند ResourceSlice یک pool را تشکیل دهند.

در حال حاضر تنها منابع پشتیبانی‌شده، دستگاه‌هایی (device) با ویژگی‌ها (attributes) و ظرفیت‌ها (capacities) هستند. هر دستگاه در یک pool مشخص، صرف‌نظر از تعداد ResourceSliceها، باید نام یکتا داشته باشد. ResourceSliceای که یک دستگاه در آن منتشر می‌شود ممکن است با گذشت زمان تغییر کند. شناسه یکتای یک دستگاه چندتایی &lt;driver name&gt;, &lt;pool name&gt;, &lt;device name&gt; است.

هرگاه درایور نیاز به به‌روزرسانی یک pool داشته باشد، عدد pool.Spec.Pool.Generation را افزایش می‌دهد و همه ResourceSliceها را با این عدد جدید و تعریف‌های جدید منابع به‌روزرسانی می‌کند. مصرف‌کننده باید فقط از ResourceSliceهایی استفاده کند که بالاترین شماره generation را دارند و بقیه را نادیده بگیرد.

هنگام تخصیص همه منابع یک pool که با معیارهای مشخصی مطابقت دارند، یا هنگام جست‌وجوی بهترین راه‌حل میان چند گزینه مختلف، مصرف‌کننده باید تعداد ResourceSliceهای موجود در یک pool (که در هر ResourceSlice درج شده است) را بررسی کند تا مشخص شود دید او از pool کامل است یا خیر. اگر کامل نیست، باید منتظر بماند تا درایور به‌روزرسانی pool را به پایان برساند.

برای منابعی که محلی یک نود نیستند، نام نود تنظیم نمی‌شود. در این حالت، درایور می‌تواند از یک node selector برای مشخص کردن محل دسترس‌پذیر بودن دستگاه‌ها استفاده کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره (schema) نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#ResourceSliceSpec" >}}">ResourceSliceSpec</a></em></td>
      <td>اطلاعات منتشرشده توسط درایور را در بر دارد. تغییر spec به‌طور خودکار عدد metadata.generation را افزایش می‌دهد.</td>
    </tr>
  </tbody>
</table>


## ResourceSliceSpec {#ResourceSliceSpec}

ResourceSliceSpec اطلاعاتی را که درایور در یک ResourceSlice منتشر می‌کند در بر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allNodes</code><br/><em>boolean</em></td>
      <td>AllNodes نشان می‌دهد که همه نودها به منابع موجود در pool دسترسی دارند. دقیقاً یکی از NodeName، NodeSelector، AllNodes و PerDeviceNodeSelection باید تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>devices</code><br/><em><a href="{{< ref "#Device" >}}">Device array</a></em></td>
      <td>Devices برخی از دستگاه‌های این pool یا همه آن‌ها را فهرست می‌کند. نباید بیش از ۱۲۸ مورد داشته باشد. اگر هر دستگاهی از taintها استفاده کند یا شمارنده (counter) مصرف کند، این سقف ۶۴ است. در یک ResourceSlice فقط یکی از Devices و SharedCounters می‌تواند تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Driver درایور DRA را که اطلاعات ظرفیت را ارائه می‌دهد شناسایی می‌کند. می‌توان از یک field selector برای فهرست کردن فقط آبجکت‌های ResourceSlice با نام درایور مشخص استفاده کرد. باید یک زیردامنه DNS باشد و بهتر است به یک دامنه DNS متعلق به فروشنده درایور ختم شود. فقط باید از حروف کوچک استفاده کند. این فیلد تغییرناپذیر (immutable) است.</td>
    </tr>
    <tr>
      <td><code>nodeName</code><br/><em>string</em></td>
      <td>NodeName نودی را که منابع این pool را فراهم می‌کند شناسایی می‌کند. می‌توان از یک field selector برای فهرست کردن فقط آبجکت‌های ResourceSlice متعلق به یک نود مشخص استفاده کرد. از این فیلد می‌توان برای محدود کردن دسترسی نودها به ResourceSliceهایی با همان نام نود استفاده کرد. همچنین به autoscalerها نشان می‌دهد که افزودن نودهای جدید از همان نوع یک نود قدیمی ممکن است منابع جدیدی نیز در دسترس قرار دهد. دقیقاً یکی از NodeName، NodeSelector، AllNodes و PerDeviceNodeSelection باید تنظیم شود. این فیلد تغییرناپذیر است.</td>
    </tr>
    <tr>
      <td><code>nodeSelector</code><br/><em><a href="{{< ref "../definitions/node-selector-v1#NodeSelector" >}}">NodeSelector</a></em></td>
      <td>NodeSelector مشخص می‌کند که چه نودهایی به منابع موجود در pool دسترسی دارند، در حالتی که pool به یک نود واحد محدود نیست. باید دقیقاً یک term داشته باشد. دقیقاً یکی از NodeName، NodeSelector، AllNodes و PerDeviceNodeSelection باید تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>partitionTypeAttribute</code><br/><em>string</em></td>
      <td>PartitionTypeAttribute نام یک ویژگی رشته‌ای دستگاه (با نام کاملاً مشخص، مثلاً "gpu.example.com/profile") را مشخص می‌کند که مقدار آن نوع پارتیشن هر دستگاه را برچسب‌گذاری می‌کند، مانند "Full" یا "Half" برای یک GPU از نوع MIG. در صورت تنظیم، هر دستگاه پارتیشن‌پذیر در slice باید این ویژگی را داشته باشد و دستگاه‌هایی که مقدار یکسان دارند باید هزینه ConsumesCounters یکسانی داشته باشند.</td>
    </tr>
    <tr>
      <td><code>perDeviceNodeSelection</code><br/><em>boolean</em></td>
      <td>PerDeviceNodeSelection مشخص می‌کند که دسترسی نودها به منابع pool در سطح ResourceSlice تنظیم می‌شود یا در سطح هر دستگاه. اگر روی true تنظیم شود، هر دستگاه تعریف‌شده در ResourceSlice باید این مورد را به‌صورت جداگانه مشخص کند. دقیقاً یکی از NodeName، NodeSelector، AllNodes و PerDeviceNodeSelection باید تنظیم شود.</td>
    </tr>
    <tr>
      <td><code>pool</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#ResourcePool" >}}">ResourcePool</a></em></td>
      <td>Pool توضیح می‌دهد که این ResourceSlice به کدام pool تعلق دارد.</td>
    </tr>
    <tr>
      <td><code>sharedCounters</code><br/><em><a href="{{< ref "#CounterSet" >}}">CounterSet array</a></em></td>
      <td>SharedCounters فهرستی از counter setها را تعریف می‌کند که هر کدام یک نام و فهرستی از شمارنده‌های در دسترس دارند. نام counter setها باید در ResourcePool یکتا باشد. در یک ResourceSlice فقط یکی از Devices و SharedCounters می‌تواند تنظیم شود. حداکثر تعداد counter setها ۸ است.</td>
    </tr>
    <tr>
      <td><code>skipNodeOperations</code><br/><em>string array</em></td>
      <td>SkipNodeOperations عملیات منابع محلی نود (فراخوانی‌های gRPC) را فهرست می‌کند که هنگام تعیین ضرورت انجام عملیات روی نود، برای دستگاه‌های این slice نادیده گرفته می‌شوند. اگر همه دستگاه‌های تخصیص‌یافته یک درایور در یک claim یک عملیات را نادیده بگیرند، آن فراخوانی gRPC انجام نمی‌شود. مقادیر معتبر عبارت‌اند از:  - "NodePrepareResources": فراخوانی‌های gRPC مربوط به NodePrepareResources نادیده گرفته می‌شوند. این   مقدار را نمی‌توان مشخص کرد، مگر اینکه "NodeUnprepareResources" نیز فهرست شده باشد   (یا "*" مشخص شده باشد). - "NodeUnprepareResources": فراخوانی‌های gRPC مربوط به NodeUnprepareResources نادیده گرفته می‌شوند. - "*": همه عملیات منابع محلی نود نادیده گرفته می‌شوند.  مقادیر دیگری ممکن است در آینده اضافه شوند. kubelet باید مقادیر ناشناخته را نادیده بگیرد.</td>
    </tr>
  </tbody>
</table>


## ResourceSliceList {#ResourceSliceList}

ResourceSliceList مجموعه‌ای از ResourceSliceها است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره (schema) نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice array</a></em></td>
      <td>Items فهرست ResourceSliceهای منبع است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنباط کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست</td>
    </tr>
  </tbody>
</table>


## CapacityRequestPolicy {#CapacityRequestPolicy}

CapacityRequestPolicy مشخص می‌کند که درخواست‌ها چگونه ظرفیت دستگاه را مصرف می‌کنند.

نباید بیش از یک ValidRequestValues تنظیم شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>default</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Default مشخص می‌کند که یک درخواست، که در Capacity مربوط به DeviceRequest ورودی برای این ظرفیت ندارد، چه مقدار از آن را مصرف می‌کند.</td>
    </tr>
    <tr>
      <td><code>validRange</code><br/><em><a href="{{< ref "#CapacityRequestPolicyRange" >}}">CapacityRequestPolicyRange</a></em></td>
      <td>ValidRange بازه مقادیر قابل‌قبول را برای درخواست‌های مصرفی تعریف می‌کند. اگر این فیلد تنظیم شود، Default باید تعریف شده باشد و در ValidRange تعریف‌شده قرار بگیرد. اگر مقدار درخواستی در بازه تعریف‌شده نباشد، درخواست سیاست را نقض می‌کند و این دستگاه نمی‌تواند تخصیص داده شود. اگر درخواست ورودی برای این ظرفیت نداشته باشد، مقدار Default استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>validValues</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity array</a></em></td>
      <td>ValidValues مجموعه‌ای از مقادیر قابل‌قبول را برای درخواست‌های مصرفی تعریف می‌کند. نباید بیش از ۱۰ مورد داشته باشد. باید به‌صورت صعودی مرتب شده باشد. اگر این فیلد تنظیم شود، Default باید تعریف شده باشد و در فهرست ValidValues گنجانده شود. اگر مقدار درخواستی با هیچ مقدار معتبری برابر نباشد اما از برخی مقادیر معتبر کوچک‌تر باشد، زمان‌بند کوچک‌ترین مقدار معتبری را که بزرگ‌تر یا برابر درخواست است محاسبه می‌کند. یعنی: min(ceil(requestedValue) ∈ validValues)، به‌طوری که requestedValue ≤ max(validValues). اگر مقدار درخواستی از همه مقادیر معتبر بیشتر باشد، درخواست سیاست را نقض می‌کند و این دستگاه نمی‌تواند تخصیص داده شود.</td>
    </tr>
  </tbody>
</table>


## CapacityRequestPolicyRange {#CapacityRequestPolicyRange}

CapacityRequestPolicyRange بازه معتبر را برای مقادیر ظرفیت قابل‌مصرف تعریف می‌کند.

اگر feature gate با نام DRAFractionalCapacityRange فعال باشد و دست‌کم یکی از Min، Max یا Step یک مقدار کسری باشد (یعنی مقدار آن عدد صحیح نباشد)، به‌جای آن از محاسبات بر پایه میلی‌واحد (milli-unit) استفاده می‌شود که از مقادیر تا ۳ رقم اعشار پشتیبانی می‌کند (مثلاً 100m = 0.1). در این حالت، بزرگ‌ترین مقدار پشتیبانی‌شده نسبت به استفاده از اعداد صحیح ۶۴ بیتی ۱۰۰۰ برابر کوچک‌تر است. در غیر این صورت، همه مقایسه‌ها از طریق resource.Quantity.Value() با محاسبات عدد صحیح ۶۴ بیتی انجام می‌شوند.

  - اگر مقدار درخواستی کمتر از Min باشد، به مقدار Min گرد می‌شود.
  - اگر Step تنظیم شده باشد و مقدار درخواستی بین Min و Max باشد اما با Step هم‌تراز نباشد،
    به مقدار بعدی برابر با Min + (n * Step) گرد می‌شود.
  - اگر Step تنظیم نشده باشد، مقدار درخواستی در صورتی که در بازه Min تا Max (در صورت تنظیم) قرار بگیرد، بدون تغییر استفاده می‌شود.
  - اگر مقدار درخواستی یا گردشده از Max (در صورت تنظیم) بیشتر شود، درخواست سیاست را برآورده نمی‌کند
    و دستگاه نمی‌تواند تخصیص داده شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>max</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Max حد بالای ظرفیتی را که می‌توان درخواست کرد تعریف می‌کند. Max باید کوچک‌تر یا مساوی مقدار ظرفیت باشد. Min و requestPolicy.default باید کوچک‌تر یا مساوی مقدار بیشینه باشند.</td>
    </tr>
    <tr>
      <td><code>min</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Min حداقل ظرفیت مجاز را برای یک درخواست مصرف مشخص می‌کند. Min باید بزرگ‌تر یا مساوی صفر و کوچک‌تر یا مساوی مقدار ظرفیت باشد. requestPolicy.default باید بزرگ‌تر یا مساوی مقدار کمینه باشد.</td>
    </tr>
    <tr>
      <td><code>step</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Step اندازه گام بین مقادیر معتبر ظرفیت را در این بازه تعریف می‌کند. Max (در صورت تنظیم) و requestPolicy.default باید مضربی از Step باشند. Min + Step باید کوچک‌تر یا مساوی مقدار ظرفیت باشد.</td>
    </tr>
  </tbody>
</table>


## Counter {#Counter}

Counter کمیتی را توصیف می‌کند که به یک دستگاه مرتبط است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>value</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Value مشخص می‌کند که چه مقدار از یک شمارنده دستگاه در دسترس است.</td>
    </tr>
  </tbody>
</table>


## CounterSet {#CounterSet}

CounterSet یک مجموعه نام‌دار از شمارنده‌ها را تعریف می‌کند که دستگاه‌های تعریف‌شده در ResourcePool می‌توانند از آن‌ها استفاده کنند.

شمارنده‌ها به‌تنهایی قابل تخصیص نیستند، اما دستگاه‌ها می‌توانند به آن‌ها ارجاع دهند. هنگامی که یک دستگاه تخصیص داده می‌شود، بخشی از شمارنده‌ها که آن دستگاه استفاده می‌کند دیگر برای سایر دستگاه‌ها در دسترس نخواهد بود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>counters</code>&nbsp;<strong>*</strong><br/><em>object</em></td>
      <td>Counters مجموعه شمارنده‌های این CounterSet را تعریف می‌کند. نام هر شمارنده باید در آن مجموعه یکتا و یک DNS label باشد. حداکثر تعداد شمارنده‌ها ۳۲ است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name نام counter set را تعریف می‌کند. باید یک DNS label باشد.</td>
    </tr>
  </tbody>
</table>

## Device {#Device}

Device یک نمونه سخت‌افزاری مجزا را نشان می‌دهد که می‌توان آن را بر اساس ویژگی‌هایش انتخاب کرد. افزون بر name، دقیقاً یکی از فیلدها باید مقداردهی شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allNodes</code><br/><em>boolean</em></td>
      <td>AllNodes نشان می‌دهد که همه نودها به این دستگاه دسترسی دارند. فقط در صورتی باید مقداردهی شود که Spec.PerDeviceNodeSelection روی true تنظیم شده باشد. حداکثر یکی از NodeName، NodeSelector و AllNodes را می‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>allowMultipleAllocations</code><br/><em>boolean</em></td>
      <td>AllowMultipleAllocations مشخص می‌کند که آیا اجازه داده می‌شود دستگاه به چند DeviceRequest تخصیص یابد یا خیر. اگر AllowMultipleAllocations روی true تنظیم شود، دستگاه را می‌توان بیش از یک بار تخصیص داد و تمام ظرفیت آن قابل مصرف است، صرف‌نظر از اینکه requestPolicy تعریف شده باشد یا نه.</td>
    </tr>
    <tr>
      <td><code>attributes</code><br/><em>object</em></td>
      <td>Attributes مجموعه ویژگی‌های این دستگاه را تعریف می‌کند. نام هر ویژگی باید در این مجموعه یکتا باشد. حداکثر تعداد مجموع ویژگی‌ها و ظرفیت‌ها 32 است.</td>
    </tr>
    <tr>
      <td><code>bindingConditions</code><br/><em>string array</em></td>
      <td>BindingConditions شرایط لازم برای ادامه فرایند اتصال (binding) را تعریف می‌کند. برای ادامه اتصال Pod به نود در زمان زمان‌بندی Pod، همه این شرایط باید در شرایط وضعیت (status conditions) هر دستگاه با مقدار True تنظیم شده باشند. حداکثر تعداد شرایط اتصال 4 است. شرایط باید رشته‌ای معتبر برای نوع شرط (condition type) باشند. این فیلد بتا است و فعال‌سازی feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>bindingFailureConditions</code><br/><em>string array</em></td>
      <td>BindingFailureConditions شرایط شکست اتصال را تعریف می‌کند. این شرایط ممکن است در شرایط وضعیت هر دستگاه تنظیم شوند. اگر هر یک از آن‌ها روی "True" باشد، یعنی اتصال با شکست مواجه شده است. حداکثر تعداد شرایط شکست اتصال 4 است. شرایط باید رشته‌ای معتبر برای نوع شرط باشند. این فیلد بتا است و فعال‌سازی feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>bindsToNode</code><br/><em>boolean</em></td>
      <td>BindsToNode مشخص می‌کند که آیا استفاده از یک تخصیص شامل این دستگاه باید دقیقاً به نودی محدود شود که هنگام تخصیص claim انتخاب شده است. اگر روی true تنظیم شود، زمان‌بند مقدار ResourceClaim.Status.Allocation.NodeSelector را طوری تنظیم می‌کند که با نودی که تخصیص در آن انجام شده است مطابقت داشته باشد. این فیلد بتا است و فعال‌سازی feature gateهای DRADeviceBindingConditions و DRAResourceClaimDeviceStatus را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>capacity</code><br/><em>object</em></td>
      <td>Capacity مجموعه ظرفیت‌های این دستگاه را تعریف می‌کند. نام هر ظرفیت باید در این مجموعه یکتا باشد. حداکثر تعداد مجموع ویژگی‌ها و ظرفیت‌ها 32 است.</td>
    </tr>
    <tr>
      <td><code>consumesCounters</code><br/><em><a href="{{< ref "#DeviceCounterConsumption" >}}">DeviceCounterConsumption array</a></em></td>
      <td>ConsumesCounters فهرستی از ارجاع‌ها به sharedCounters و مجموعه شمارنده‌هایی را تعریف می‌کند که دستگاه از آن مجموعه‌های شمارنده مصرف خواهد کرد. برای هر counterSet فقط یک ورودی می‌تواند وجود داشته باشد. حداکثر تعداد مصرف‌های شمارنده برای هر دستگاه 2 است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name شناسه‌ای یکتا میان همه دستگاه‌هایی است که درایور در pool مدیریت می‌کند. باید یک DNS label باشد.</td>
    </tr>
    <tr>
      <td><code>nodeAllocatableResources</code><br/><em>object</em></td>
      <td>NodeAllocatableResources نگاشت منابع نود را تعریف می‌کند که درایور DRAِ ارائه‌دهنده این دستگاه آن‌ها را مدیریت می‌کند. این شامل منابعی است که هم‌اکنون در `status.allocatable` آبجکت v1.Node گزارش می‌شوند و منبع توسعه‌یافته (extended resource) نیستند (به https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources مراجعه کنید). نمونه‌ها عبارت‌اند از "cpu"، "memory"، "ephemeral-storage" و hugepages. افزون بر درخواست‌های معمولی که از طریق `spec` در Pod ثبت می‌شوند، این منابع را می‌توان از طریق claimها نیز درخواست کرد و درایور DRA آن‌ها را تخصیص می‌دهد. برای مثال، یک درایور DRA برای CPU ممکن است CPUهای اختصاصی یا وابستگی‌های حافظه کمکی نود را برای یک دستگاه شتاب‌دهنده تخصیص دهد. کلیدهای این نگاشت، نام منابع قابل تخصیص نود هستند (برای مثال "cpu" و "memory"). نام منابع توسعه‌یافته به‌عنوان کلید مجاز نیست.</td>
    </tr>
    <tr>
      <td><code>nodeName</code><br/><em>string</em></td>
      <td>NodeName نودی را مشخص می‌کند که دستگاه در آن در دسترس است. فقط در صورتی باید مقداردهی شود که Spec.PerDeviceNodeSelection روی true تنظیم شده باشد. حداکثر یکی از NodeName، NodeSelector و AllNodes را می‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>nodeSelector</code><br/><em><a href="{{< ref "../definitions/node-selector-v1#NodeSelector" >}}">NodeSelector</a></em></td>
      <td>NodeSelector نودهایی را تعریف می‌کند که دستگاه در آن‌ها در دسترس است. باید دقیقاً از یک term استفاده کند. فقط در صورتی باید مقداردهی شود که Spec.PerDeviceNodeSelection روی true تنظیم شده باشد. حداکثر یکی از NodeName، NodeSelector و AllNodes را می‌توان تنظیم کرد.</td>
    </tr>
    <tr>
      <td><code>taints</code><br/><em><a href="{{< ref "device-taint-rule-v1#DeviceTaint" >}}">DeviceTaint array</a></em></td>
      <td>در صورت تعیین، این‌ها taintهای تعریف‌شده توسط درایور هستند. حداکثر تعداد taintها 16 است. اگر برای هر دستگاهی در یک ResourceSlice taint تنظیم شود، حداکثر تعداد دستگاه‌های مجاز در هر ResourceSlice به‌جای 128 برابر 64 خواهد بود. این فیلد بتا است و فعال‌سازی feature gate با نام DRADeviceTaints را لازم دارد.</td>
    </tr>
  </tbody>
</table>


## DeviceAttribute {#DeviceAttribute}

DeviceAttribute باید دقیقاً یک فیلد مقداردهی‌شده داشته باشد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>bool</code><br/><em>boolean</em></td>
      <td>BoolValue یک مقدار درست/نادرست (true/false) است.</td>
    </tr>
    <tr>
      <td><code>bools</code><br/><em>boolean array</em></td>
      <td>BoolValues فهرستی غیرتهی از مقادیر درست/نادرست است.</td>
    </tr>
    <tr>
      <td><code>int</code><br/><em>integer</em></td>
      <td>IntValue یک عدد است.</td>
    </tr>
    <tr>
      <td><code>ints</code><br/><em>integer array</em></td>
      <td>IntValues فهرستی غیرتهی از اعداد است. این فیلد آلفا است و فعال‌سازی feature gate با نام DRAListTypeAttributes را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>string</code><br/><em>string</em></td>
      <td>StringValue یک رشته است. طول آن نباید بیش از 64 کاراکتر باشد.</td>
    </tr>
    <tr>
      <td><code>strings</code><br/><em>string array</em></td>
      <td>StringValues فهرستی غیرتهی از رشته‌هاست. طول هر رشته نباید بیش از 64 کاراکتر باشد. این فیلد آلفا است و فعال‌سازی feature gate با نام DRAListTypeAttributes را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>version</code><br/><em>string</em></td>
      <td>VersionValue یک نسخه معنایی (semantic version) مطابق مشخصات semver.org نسخه 2.0.0 است. طول آن نباید بیش از 64 کاراکتر باشد.</td>
    </tr>
    <tr>
      <td><code>versions</code><br/><em>string array</em></td>
      <td>VersionValues فهرستی غیرتهی از نسخه‌های معنایی مطابق مشخصات semver.org نسخه 2.0.0 است. طول هر رشته نسخه نباید بیش از 64 کاراکتر باشد. این فیلد آلفا است و فعال‌سازی feature gate با نام DRAListTypeAttributes را لازم دارد.</td>
    </tr>
  </tbody>
</table>


## DeviceCapacity {#DeviceCapacity}

DeviceCapacity مقداری را توصیف می‌کند که به یک دستگاه مربوط است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>requestPolicy</code><br/><em><a href="{{< ref "#CapacityRequestPolicy" >}}">CapacityRequestPolicy</a></em></td>
      <td>RequestPolicy تعیین می‌کند که وقتی اجازه داده می‌شود دستگاه میان چند تخصیص به اشتراک گذاشته شود، این DeviceCapacity چگونه باید مصرف شود. برای تنظیم requestPolicy، فیلد allowMultipleAllocations در Device باید روی true تنظیم شده باشد. اگر تنظیم نشود، درخواست‌های ظرفیت محدودیتی ندارند: درخواست‌ها می‌توانند هر مقدار از ظرفیت را مصرف کنند، مادامی که مجموع مصرف در همه تخصیص‌ها از ظرفیت تعریف‌شده دستگاه بیشتر نشود. اگر request نیز تنظیم نشده باشد، مقدار پیش‌فرض کل ظرفیت است.</td>
    </tr>
    <tr>
      <td><code>value</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>Value تعیین می‌کند دستگاه از یک ظرفیت مشخص چه مقدار دارد. این فیلد ظرفیت کل ثابت را نشان می‌دهد و تغییر نمی‌کند. مقدار مصرف‌شده به‌طور جداگانه توسط زمان‌بند پیگیری می‌شود و بر این مقدار تأثیری ندارد.</td>
    </tr>
  </tbody>
</table>


## DeviceCounterConsumption {#DeviceCounterConsumption}

DeviceCounterConsumption مجموعه‌ای از شمارنده‌ها را تعریف می‌کند که یک دستگاه از یک CounterSet مصرف خواهد کرد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>compatibilityGroups</code><br/><em>string array</em></td>
      <td>CompatibilityGroups فهرستی از نام‌های گروه مبهم (opaque) برای مصرف این مجموعه شمارنده است. دستگاه‌هایی که از یک مجموعه شمارنده یکسان مصرف می‌کنند، فقط در صورتی می‌توانند هم‌زمان تخصیص یابند («تخصیص مشترک» یا co-allocation) که دست‌کم یک گروه مشترک داشته باشند: اشتراک CompatibilityGroups همه دستگاه‌های دارای تخصیص مشترک روی آن مجموعه شمارنده باید غیرتهی باشد. دستگاه‌هایی که از مجموعه‌های شمارنده متفاوت مصرف می‌کنند، هرگز از طریق این فیلد با هم مقایسه نمی‌شوند. فیلد تنظیم‌نشده، مقدار صریح nil و فهرست خالی معادل‌اند و به معنای «بدون گروه» هستند: چنین دستگاهی فقط با دستگاه‌های هم‌ردیف روی همان مجموعه شمارنده که آن‌ها نیز گروهی ندارند قابل تخصیص مشترک است و هرگز با دستگاهی که یک گروه یا بیشتر اعلام کرده باشد تخصیص مشترک نمی‌شود. نام گروه‌ها مبهم هستند و فقط در pool مربوط به درایور منتشرکننده معنا دارند. حداکثر تعداد گروه‌ها 2 است و نام‌ها باید یکتا باشند.</td>
    </tr>
    <tr>
      <td><code>counterSet</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>CounterSet نام مجموعه‌ای است که شمارنده‌های تعریف‌شده از آن مصرف می‌شوند.</td>
    </tr>
    <tr>
      <td><code>counters</code>&nbsp;<strong>*</strong><br/><em>object</em></td>
      <td>Counters شمارنده‌هایی را تعریف می‌کند که دستگاه مصرف خواهد کرد. حداکثر تعداد شمارنده‌ها 32 است.</td>
    </tr>
  </tbody>
</table>


## NodeAllocatableMapping {#NodeAllocatableMapping}

NodeAllocatableMapping تعریف می‌کند که یک تخصیص DRA چگونه مستقیماً به مقداری از منبع قابل تخصیص نود تبدیل می‌شود. این نگاشت را می‌توان یا از تعداد دستگاه‌های تخصیص‌یافته (از طریق deviceMultiplier) یا از ظرفیت مصرف‌شده مشخص (از طریق capacityKey و capacityMultiplier) به دست آورد. این دو گزینه متقابلاً ناسازگارند. Kubelet این مقدار منبع نگاشت‌شده از claim را در cgroup سطح Pod به هر دو بخش requests و limits و در cgroup سطح کانتینر برای هر کانتینری که به claim ارجاع می‌دهد به limits اضافه می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>capacityKey</code><br/><em>string</em></td>
      <td>CapacityKey به نام یک ظرفیت ارجاع می‌دهد که به‌عنوان کلید در نگاشت `spec.devices[*].capacity` تعریف شده است. وقتی این فیلد تنظیم شود، مقدار مرتبط با این کلید در نگاشت `status.allocation.devices.results[*].consumedCapacity` (برای یک تخصیص claim مشخص) مقدار پایه منبع قابل تخصیص نود را تعیین می‌کند. فیلد `capacityMultiplier` نیز باید تنظیم شود و در مقدار پایه ضرب می‌شود. برای مثال، اگر `spec.devices[*].capacity` ورودی "dra.example.com/memory": "128Gi" داشته باشد و این فیلد روی "dra.example.com/memory" تنظیم شده باشد، آنگاه برای تخصیص claim ای که { "dra.example.com/memory": "4Gi" } را مصرف می‌کند، مقدار پایه نگاشت منبع قابل تخصیص نود برابر "4Gi" خواهد بود. مقدار نهایی منبع قابل تخصیص نود برابر `consumedCapacity[capacityKey]` * `capacityMultiplier` است.</td>
    </tr>
    <tr>
      <td><code>capacityMultiplier</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>CapacityMultiplier به‌عنوان ضریبی برای ظرفیت تخصیص‌یافته‌ی مصرف‌شده به کار می‌رود. فقط در صورتی معتبر است که `capacityKey` تنظیم شده باشد. مقدار نهایی منبع قابل تخصیص نود برابر `consumedCapacity[capacityKey]` * `capacityMultiplier` است. برای مثال، اگر ظرفیت "dra.example.com/cores" یک Device مصرف شود و هر «core» معادل 2 "cpu" باشد، نگاشت چنین خواهد بود: {ResourceName: "cpu", capacityKey: "dra.example.com/cores", capacityMultiplier: "2"}. اگر یک claim تعداد 8 "dra.example.com/cores" مصرف کند، سهم CPU برابر 8 * 2 = 16 است.</td>
    </tr>
    <tr>
      <td><code>deviceMultiplier</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>DeviceMultiplier به‌عنوان ضریبی برای تعداد دستگاه‌های تخصیص‌یافته در claim به کار می‌رود. مقدار نهایی منبع قابل تخصیص نود برابر `deviceCount` * `deviceMultiplier` است. برای مثال، درایور DRAای که هر مجتمع حافظه نهان (cache complex یا CCX) را به‌صورت یک دستگاه نشان می‌دهد، در `nodeAllocatableResources` خود مقدار {ResourceName: "cpu", deviceMultiplier: "8"} را خواهد داشت. اگر 2 دستگاه (CCX) به claim تخصیص یابد، 2 * 8 = 16 واحد CPU تخصیص‌یافته در نظر گرفته می‌شود. این فیلد فقط زمانی معتبر است که `capacityKey` و `capacityMultiplier` تنظیم نشده باشند.</td>
    </tr>
  </tbody>
</table>


## NodeAllocatableOverhead {#NodeAllocatableOverhead}

NodeAllocatableOverhead سربارهای منبع کمکی را تعریف می‌کند که هنگام تخصیص یک دستگاه ایجاد می‌شوند. سربار را می‌توان به‌صورت هزینه ثابت برای هر Pod ارجاع‌دهنده به claim، هزینه متغیر برای هر ارجاع کانتینر، یا هر دو مشخص کرد. Kubelet این سربار را با افزودن آن به cgroupهای سطح Pod و سطح کانتینر برای کانتینرهای ارجاع‌دهنده محاسبه می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>perContainer</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>PerContainer به ازای هر ارجاع کانتینر به claim اعمال می‌شود. این فیلد سربار را به‌صورت خطی متناسب با تعداد کانتینرهایی که فعالانه از دستگاه استفاده می‌کنند مدل می‌کند. وقتی هم PerPod و هم PerContainer مشخص شده باشند، سربار کل تخصیص‌یافته برای هر Pod ارجاع‌دهنده به claim چنین محاسبه می‌شود: Quantity = PerPod + (PerContainer * NumReferences). Kubelet این سربار را در cgroupها به این شکل محاسبه می‌کند: - cgroup سطح Pod (requests و limits): Kubelet مقدار PerPod + (PerContainer * NumReferences) را اضافه می‌کند. - cgroup سطح کانتینر (فقط limits): Kubelet برای هر کانتینر ارجاع‌دهنده مقدار PerPod + PerContainer را اضافه می‌کند. با این کار هر کانتینر به‌تنهایی می‌تواند به سربار سطح Pod دسترسی داشته باشد، در حالی که cgroup والد کل مصرف را محدود می‌کند تا PerPod دقیقاً یک بار محاسبه شود.</td>
    </tr>
    <tr>
      <td><code>perPod</code><br/><em><a href="{{< ref "../definitions/quantity-resource#Quantity" >}}">Quantity</a></em></td>
      <td>PerPod سربازی است که به ازای هر Pod ارجاع‌دهنده به claim روی این نود فقط یک بار اعمال می‌شود. این سربار ثابت است و برای هر Pod ارجاع‌دهنده به claim ایجاد می‌شود.</td>
    </tr>
  </tbody>
</table>


## NodeAllocatableResource {#NodeAllocatableResource}

NodeAllocatableResource ترجمه واحدهای دستگاه/ظرفیت DRAِ درخواست‌شده به مقدار متناظر منبع قابل تخصیص نود را تعریف می‌کند. دست‌کم یکی از Mapping یا Overhead باید مشخص شود. مشخص نکردن هیچ‌کدام پیکربندی نامعتبر است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>mapping</code><br/><em><a href="{{< ref "#NodeAllocatableMapping" >}}">NodeAllocatableMapping</a></em></td>
      <td>Mapping زمانی استفاده می‌شود که دستگاه مستقیماً یک منبع قابل تخصیص نود مانند CPU یا حافظه استاندارد را مدل کند (برای مثال با یک درایور DRA برای CPU). مقدار محاسبه‌شده دقیقاً یک بار برای هر نمونه claim روی نود در نظر گرفته می‌شود. برای جلوگیری از اصطکاک در ایزوله‌سازی cgroup نود، زمان‌بند صراحتاً از اشتراک‌گذاری claimهای دستگاه نگاشت‌شده میان چند Pod جلوگیری می‌کند.</td>
    </tr>
    <tr>
      <td><code>overhead</code><br/><em><a href="{{< ref "#NodeAllocatableOverhead" >}}">NodeAllocatableOverhead</a></em></td>
      <td>Overhead شامل فیلدهایی برای مدل‌سازی سربار کمکی است که هنگام تخصیص دستگاه‌هایی ایجاد می‌شود که خودشان یک منبع قابل تخصیص نود را مدل نمی‌کنند (برای مثال سربار حافظه میزبان برای GPUها). اشتراک‌گذاری claimهای دارای سربار میان چند Pod مجاز است. سربار قابل تخصیص نود برای هر Pod ارجاع‌دهنده به claim به‌طور جداگانه محاسبه می‌شود. سربار همیشه از ظرفیت قابل تخصیص نود برای آن منبع کسر می‌شود، حتی اگر برای همان منبع mapping نیز مشخص شده باشد. برای مثال: اگر دستگاهی ظرفیت حافظه هر سوکت را از طریق Mapping (با CapacityKey) به‌صورت یک pool ظرفیت قابل مصرف مدل کند، هر سربار مشخص‌شده برای همان منبع از ظرفیت قابل تخصیص عمومی نود کسر می‌شود، نه از pool ظرفیت هر سوکت در Mapping.</td>
    </tr>
  </tbody>
</table>

## NodeSelectorRequirement {#NodeSelectorRequirement}

یک NodeSelectorRequirement انتخابگری است که شامل یک کلید، یک عملگر و مجموعه‌ای از مقادیر است؛ عملگر رابطهٔ کلید را با مقادیر مشخص می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>کلید برچسبی که انتخابگر به آن اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>operator</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>رابطهٔ یک کلید را با مجموعه‌ای از مقادیر مشخص می‌کند. عملگرهای معتبر عبارت‌اند از In، NotIn، Exists، DoesNotExist، Gt و Lt.<br/><br/>مقادیر enum ممکن:<br/> - `"DoesNotExist"`<br/> - `"Exists"`<br/> - `"Gt"`<br/> - `"In"`<br/> - `"Lt"`<br/> - `"NotIn"`</td>
    </tr>
    <tr>
      <td><code>values</code><br/><em>string array</em></td>
      <td>آرایه‌ای از مقادیر رشته‌ای. اگر عملگر In یا NotIn باشد، آرایهٔ values نباید خالی باشد. اگر عملگر Exists یا DoesNotExist باشد، آرایهٔ values باید خالی باشد. اگر عملگر Gt یا Lt باشد، آرایهٔ values باید دقیقاً یک عنصر داشته باشد که به‌صورت عدد صحیح تفسیر می‌شود. این آرایه در جریان strategic merge patch جایگزین می‌شود.</td>
    </tr>
  </tbody>
</table>


## ResourcePool {#ResourcePool}

ResourcePool مشخص می‌کند ResourceSliceها به کدام pool تعلق دارند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>generation</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>Generation تغییرات یک pool را در طول زمان دنبال می‌کند. هرگاه یک درایور چیزی را دربارهٔ یک یا چند منبع در یک pool تغییر دهد، باید generation را در همهٔ ResourceSliceهایی که بخشی از آن pool هستند تغییر دهد. مصرف‌کنندگان ResourceSliceها باید فقط منابع pool با بالاترین شمارهٔ generation را در نظر بگیرند. درایورها می‌توانند generation را بازنشانی کنند. این کار برای مصرف‌کنندگان مشکلی ایجاد نمی‌کند، به شرط آنکه همهٔ ResourceSliceهای یک pool به‌روزرسانی شوند تا با آن هماهنگ باشند یا حذف شوند. این سازوکار همراه با ResourceSliceCount به مصرف‌کنندگان امکان می‌دهد poolهایی را که از چند ResourceSlice تشکیل شده‌اند و در وضعیت ناقص قرار دارند شناسایی کنند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name برای شناسایی pool استفاده می‌شود. برای دستگاه‌های محلی نود، این مقدار اغلب نام نود است، اما این الزامی نیست. با استفاده از field selector می‌توان فقط آبجکت‌های ResourceSlice متعلق به یک pool مشخص را فهرست کرد. طول آن نباید از ۲۵۳ نویسه بیشتر باشد و باید از یک یا چند زیردامنهٔ DNS تشکیل شده باشد که با اسلش از هم جدا شده‌اند. این فیلد تغییرناپذیر (immutable) است.</td>
    </tr>
    <tr>
      <td><code>resourceSliceCount</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>ResourceSliceCount تعداد کل ResourceSliceهای pool در این شمارهٔ generation است. باید بزرگ‌تر از صفر باشد. مصرف‌کنندگان می‌توانند از آن برای بررسی اینکه همهٔ ResourceSliceهای متعلق به یک pool را دیده‌اند یا نه استفاده کنند.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /apis/resource.k8s.io/v1/resourceslices



#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست پردازش بیشتری نمی‌شود. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند مرتبط است. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری فقط آخرین فیلدی را که رمزگشا (decoder) با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 بود. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این مقدار در نسخهٔ v1.23 و بعد از آن پیش‌فرض است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل همهٔ فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /apis/resource.k8s.io/v1/resourceslices/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceSlice</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست پردازش بیشتری نمی‌شود. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند مرتبط است. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر apply (یعنی JsonPatch، MergePatch و StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری فقط آخرین فیلدی را که رمزگشا (decoder) با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 بود. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این مقدار در نسخهٔ v1.23 و بعد از آن پیش‌فرض است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل همهٔ فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند؛ یعنی کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است دوباره به دست می‌گیرد. پرچم force برای درخواست‌های patch غیر apply باید تنظیم نشده باشد.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

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


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace

#### HTTP Request

PUT /apis/resource.k8s.io/v1/resourceslices/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceSlice</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست پردازش بیشتری نمی‌شود. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند مرتبط است. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، همان‌طور که در https://golang.org/pkg/unicode/#IsPrint تعریف شده است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری فقط آخرین فیلدی را که رمزگشا (decoder) با آن مواجه می‌شود در نظر می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 بود. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این مقدار در نسخهٔ v1.23 و بعد از آن پیش‌فرض است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل همهٔ فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete

#### HTTP Request

DELETE /apis/resource.k8s.io/v1/resourceslices/{name}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceSlice</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وقتی این پارامتر وجود داشته باشد، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست پردازش بیشتری نمی‌شود. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت (grace period) پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، به‌طور پیش‌فرض مقداری مختص هر آبجکت به کار می‌رود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) ناتوانی در تبدیل داده‌های آن، برای مثال شکست در رمزگشایی (decryption)، یا ب) ناتوانی در رمزگشایی آن به یک آبجکت (decode)، نتوان آن را با موفقیت از ذخیره‌ساز زیرین بازیابی کرد. نکته: حذف ناایمن، محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاریِ مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به جریان عادی حذف وابسته باشد، ممکن است کلاستر دچار اختلال جدی شود. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آن را صراحتاً فعال کند.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. مشخص می‌کند که آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true یا false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول: 'Orphan' - آبجکت‌های وابسته را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد آبجکت‌های وابسته را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ آبجکت‌های وابسته را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

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


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/resource.k8s.io/v1/resourceslices



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه‌ی یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از «کلید بعدی» آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، اصلاح یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true است پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست نمی‌دهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته منجر به پاسخ خطا و توقف پردازش درخواست می‌شود. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مرحله‌های dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان، بر حسب ثانیه، پیش از آنکه آبجکت باید حذف شود. مقدار باید عددی صحیح و نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دوره‌ی مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت تعیین می‌شود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناامن منبع را فعال می‌کند. یک منبع در صورتی خراب در نظر گرفته می‌شود که به‌دلیل الف) غیرقابل تبدیل بودن داده‌های آن، مثلاً شکست در رمزگشایی، یا ب) شکست در رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌ساز زیرین بازیابی کرد. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به جریان عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید برای فعال‌سازی آن صراحتاً اقدام کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌ی فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه‌ی بعدی نتایج به کار برد. تعیین limit ممکن است تعداد کمتری از موارد درخواست‌شده (حتی صفر مورد) را برگرداند، در صورتی که همه‌ی آبجکت‌های درخواست‌شده فیلتر شوند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا خیر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. این فیلد زمانی که watch برابر true است پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، اصلاح یا حذف شده است، در درخواست‌های ادامه‌ی بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه‌ی بسیار بزرگ از limit استفاده می‌کند، بتواند مطمئن باشد همه‌ی آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه‌ی 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true یا false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مخصوص هر منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همه‌ی وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را برای این تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود resourceVersionMatch برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه‌ی `sendInitialEvents` تنظیم شده باشد، لازم است گزینه‌ی `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به این صورت تفسیر می‌شود: «داده‌هایی دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای دست‌کم به‌تازگی مقدار ارائه‌شده در ListOptions همگام‌سازی شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام‌سازی شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه‌ی هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه‌ی object استفاده می‌کنند (مثلاً "object.metadata.uid") و نه قالب fieldSelector (یعنی "metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL با single-quote و پیشوند '0x' هستند و کران پایین شمول‌شده (inclusive) و کران بالای شمول‌نشده (exclusive) را در فضای هش FNV-1a شصت‌وچهار بیتی تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای شمول‌نشده برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت‌زمان فراخوانی را، فارغ از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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

GET /apis/resource.k8s.io/v1/resourceslices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceSlice</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSlice" >}}">ResourceSlice</a></em></td>
    </tr>
  </tbody>
</table>

### `get` List

#### HTTP Request

GET /apis/resource.k8s.io/v1/resourceslices



#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch از نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و نباید انتظار داشته باشند که سرور در طول یک نشست (session) حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی با پارامترهای کاملاً یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور می‌تواند مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue تعیین‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired و همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. به‌طور پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. به‌طور پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواست‌شده آیتم (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت نتایج بسیار بزرگ در بخش‌های کوچک‌تر از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را بازتاب می‌دهند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) در آبجکت‌های تحت نظارت را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌هایی دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو object-rooted به سبک CEL استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌نقل‌قول قرار می‌گیرند و پیشوند '0x' دارند. این مقادیر کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "resource-slice-v1#ResourceSliceList" >}}">ResourceSliceList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/watch/resourceslices/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ResourceSlice</td>
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
      <td>allowWatchBookmarks درخواست می‌کند رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی برگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور می‌تواند مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور با فهرستی که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است پاسخ می‌دهد و این فهرست با نتایج قبلی ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion برگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
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
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) برگرداند و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های برگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند درخواست از چه نسخه‌های منبعی ممکن است پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (برای مثال "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") پیروی نمی‌کنند. مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که در تک‌کوتیشن قرار می‌گیرند، با پیشوند '0x' شروع می‌شوند و کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش 64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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

GET /apis/resource.k8s.io/v1/watch/resourceslices



#### پارامترهای Query

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از یک کوئری قبلی را با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌برداری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور شروع کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است کمتر از تعداد درخواستی (حتی صفر مورد) بازگرداند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت نتایج یک فهرست بسیار بزرگ در بخش‌های کوچک‌تر از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده خواهد کرد. اگر آبجکت‌ها در طول فهرست‌برداری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه نتیجه اول فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظارت (پس از آن RV) را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شود، تنظیم گزینه `resourceVersionMatch` نیز الزامی است. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معناست که «داده‌ها دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشند». رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلیل سازگاری با نسخه‌های قبلی)، مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. در حال حاضر مسیرهای زیر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal در CEL هستند که درون single-quote قرار می‌گیرند و پیشوند '0x' دارند. این دو، کران پایین (شامل خود مقدار) و کران بالا (بدون خود مقدار) را بر فضای hash ‏64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای انحصاری برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به وجود یا نبود هرگونه فعالیت محدود می‌کند.</td>
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
