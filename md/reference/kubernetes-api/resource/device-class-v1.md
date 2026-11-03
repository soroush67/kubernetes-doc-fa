---
api_metadata:
  apiVersion: "resource.k8s.io/v1"
  import: "k8s.io/api/resource/v1"
  kind: "DeviceClass"
content_type: "api_reference"
description: "DeviceClass یک منبع ارائه‌شده توسط فروشنده یا مدیر است که شامل پیکربندی دستگاه و انتخابگرها (selectors) می‌شود. می‌توان در درخواست‌های دستگاه یک claim به آن ارجاع داد تا این تنظیمات از پیش‌تعریف‌شده اعمال شوند. در سطح کلاستر تعریف می‌شود."
title: "DeviceClass"
weight: 10
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


## DeviceClass {#DeviceClass}

DeviceClass یک منبع ارائه‌شده توسط فروشنده یا مدیر است که شامل پیکربندی دستگاه و انتخابگرها (selectors) می‌شود. می‌توان در درخواست‌های دستگاه یک claim به آن ارجاع داد تا این تنظیمات از پیش‌تعریف‌شده اعمال شوند. در سطح کلاستر تعریف می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#DeviceClassSpec" >}}">DeviceClassSpec</a></em></td>
      <td>Spec مشخص می‌کند چه چیزی قابل تخصیص است و چگونه باید پیکربندی شود. این فیلد تغییرپذیر است. مصرف‌کنندگان باید آماده باشند که کلاس‌ها در هر زمان تغییر کنند، چه به‌دلیل به‌روزرسانی و چه به‌دلیل جایگزینی. تخصیص‌های claim یک‌بار و بر اساس مقادیری انجام می‌شود که در زمان تخصیص در کلاس‌ها تنظیم شده بودند. تغییر spec به‌طور خودکار عدد metadata.generation را افزایش می‌دهد.</td>
    </tr>
  </tbody>
</table>


## DeviceClassSpec {#DeviceClassSpec}

DeviceClassSpec در یک [DeviceClass] استفاده می‌شود تا مشخص کند چه چیزی قابل تخصیص است و چگونه باید پیکربندی شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>config</code><br/><em><a href="{{< ref "#DeviceClassConfiguration" >}}">DeviceClassConfiguration array</a></em></td>
      <td>Config پارامترهای پیکربندی را تعریف می‌کند که بر هر دستگاهی که از طریق این کلاس claim می‌شود اعمال می‌شوند. ممکن است نیاز برخی کلاس‌ها توسط چندین درایور برآورده شود، بنابراین هر نمونه از پیکربندی فروشنده دقیقاً بر یک درایور اعمال می‌شود. این پارامترها به درایور ارسال می‌شوند، اما هنگام تخصیص claim در نظر گرفته نمی‌شوند.</td>
    </tr>
    <tr>
      <td><code>extendedResourceName</code><br/><em>string</em></td>
      <td>ExtendedResourceName نام منبع توسعه‌یافته (extended resource) برای دستگاه‌های این کلاس است. از دستگاه‌های این کلاس می‌توان برای برآورده کردن درخواست‌های منبع توسعه‌یافته یک pod استفاده کرد. قالب آن مانند نام منبع توسعه‌یافته یک pod است. این نام باید در میان همه کلاس‌های دستگاه در یک کلاستر یکتا باشد. اگر دو کلاس دستگاه نام یکسانی داشته باشند، کلاسی که دیرتر ایجاد شده است برای برآورده کردن درخواست‌های منبع توسعه‌یافته یک pod انتخاب می‌شود. اگر دو کلاس هم‌زمان ایجاد شده باشند، کلاسی که نام آن از نظر ترتیب الفبایی (lexicographic) زودتر قرار می‌گیرد انتخاب می‌شود.</td>
    </tr>
    <tr>
      <td><code>selectors</code><br/><em><a href="{{< ref "#DeviceSelector" >}}">DeviceSelector array</a></em></td>
      <td>هر انتخابگر باید توسط دستگاهی که از طریق این کلاس claim می‌شود برآورده شود.</td>
    </tr>
  </tbody>
</table>


## DeviceClassList {#DeviceClassList}

DeviceClassList مجموعه‌ای از کلاس‌ها است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرح‌واره نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass array</a></em></td>
      <td>Items فهرست کلاس‌های منبع است.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST نمایش‌داده‌شده توسط این آبجکت را مشخص می‌کند. سرورها می‌توانند این مقدار را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست</td>
    </tr>
  </tbody>
</table>


## CELDeviceSelector {#CELDeviceSelector}

CELDeviceSelector شامل یک عبارت CEL برای انتخاب یک دستگاه است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Expression یک عبارت CEL است که یک دستگاه واحد را ارزیابی می‌کند. این عبارت باید زمانی که دستگاه مورد بررسی معیارهای موردنظر را برآورده می‌کند مقدار true و در غیر این صورت مقدار false برگرداند. هر نتیجه دیگری خطا محسوب می‌شود و باعث توقف تخصیص دستگاه‌ها می‌شود.  ورودی عبارت یک آبجکت با نام "device" است که ویژگی‌های زیر را دارد:  - driver (string): نام درایوری که این دستگاه را تعریف می‌کند.  - attributes (map[string]object): ویژگی‌های دستگاه که بر اساس پیشوند گروه‌بندی شده‌اند    (برای مثال device.attributes["dra.example.com"] به آبجکتی ارزیابی می‌شود که شامل همه    ویژگی‌هایی است که با پیشوند "dra.example.com" آمده‌اند).  - capacity (map[string]object): ظرفیت‌های دستگاه که بر اساس پیشوند گروه‌بندی شده‌اند.  - allowMultipleAllocations (bool): ویژگی allowMultipleAllocations دستگاه    (در نسخه v1.34 و بالاتر با فعال بودن DRAConsumableCapacity).  مثال: دستگاهی را با driver="dra.example.com" در نظر بگیرید که دو ویژگی با نام‌های "model" و "ext.example.com/family" و یک ظرفیت با نام "modules" ارائه می‌کند. ورودی این عبارت فیلدهای زیر را خواهد داشت:      device.driver     device.attributes["dra.example.com"].model     device.attributes["ext.example.com"].family     device.capacity["dra.example.com"].modules  فیلد device.driver را می‌توان برای بررسی یک درایور مشخص به کار برد، چه به‌عنوان پیش‌شرط سطح بالا (یعنی فقط می‌خواهید دستگاه‌های این درایور بررسی شوند) و چه به‌عنوان بخشی از یک عبارت چندبندی که قرار است دستگاه‌های درایورهای مختلف را بررسی کند.  نوع مقدار هر ویژگی را تعریف دستگاه مشخص می‌کند و کاربرانی که این عبارت‌ها را می‌نویسند باید به مستندات درایورهای مورد نظر خود مراجعه کنند. نوع مقدار هر ظرفیت Quantity است.  اگر در device.attributes یا device.capacity از یک پیشوند ناشناخته برای جست‌وجو استفاده شود، یک map خالی برگردانده می‌شود. هر ارجاع به یک فیلد ناشناخته باعث خطای ارزیابی و توقف تخصیص می‌شود.  یک عبارت مقاوم باید پیش از ارجاع به ویژگی‌ها، وجود آن‌ها را بررسی کند.  خطاهای رایج: - "no such key": از زنجیره اختیاری (optional chaining) یعنی .? همراه با orValue()   استفاده کنید یا برای فیلدهای اختیاری بررسی را با has() محافظت کنید.   برای جزئیات به CEL Optional Types مراجعه کنید:   https://pkg.go.dev/github.com/google/cel-go@v0.17.4/cel#OptionalTypes  برای دیدن نحو بیشتر عبارت‌های CEL و مثال‌ها به این نشانی مراجعه کنید: https://kubernetes.io/docs/reference/using-api/cel/  برای سهولت استفاده، تابع cel.bind() فعال است و می‌توان از آن برای ساده‌سازی عبارت‌هایی استفاده کرد که به چندین ویژگی با دامنه یکسان دسترسی دارند. برای مثال:      cel.bind(dra, device.attributes["dra.example.com"], dra.someBool && dra.anotherBool)  وقتی feature gate با نام DRAListTypeAttributes فعال باشد، تابع کمکی includes() در دسترس است و هم با ویژگی‌های اسکالر و هم با ویژگی‌های از نوع فهرست کار می‌کند. این تابع برای پشتیبانی از مهاجرت روان از ویژگی‌های اسکالر به ویژگی‌های از نوع فهرست و در عین حال ساده نگه داشتن عبارت‌های CEL معرفی شده است. برای مثال:      device.attributes["dra.example.com"].models.includes("some-model")  طول عبارت باید کمتر از یا برابر با 10 Ki باشد. هزینه ارزیابی آن نیز بر اساس تعداد تخمینی گام‌های منطقی محدود شده است.</td>
    </tr>
  </tbody>
</table>


## DeviceClassConfiguration {#DeviceClassConfiguration}

DeviceClassConfiguration در DeviceClass استفاده می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>opaque</code><br/><em><a href="{{< ref "#OpaqueDeviceConfiguration" >}}">OpaqueDeviceConfiguration</a></em></td>
      <td>Opaque پارامترهای پیکربندی مختص درایور را ارائه می‌کند.</td>
    </tr>
  </tbody>
</table>


## DeviceSelector {#DeviceSelector}

در DeviceSelector باید دقیقاً یک فیلد تنظیم شده باشد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>cel</code><br/><em><a href="{{< ref "#CELDeviceSelector" >}}">CELDeviceSelector</a></em></td>
      <td>CEL شامل یک عبارت CEL برای انتخاب یک دستگاه است.</td>
    </tr>
  </tbody>
</table>


## OpaqueDeviceConfiguration {#OpaqueDeviceConfiguration}

OpaqueDeviceConfiguration شامل پارامترهای پیکربندی یک درایور در قالبی است که فروشنده درایور تعریف کرده است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>driver</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Driver برای تعیین این استفاده می‌شود که این پارامترهای پیکربندی باید به کدام افزونه kubelet ارسال شوند. یک سیاست پذیرش (admission policy) که توسعه‌دهنده درایور ارائه می‌کند می‌تواند از این مقدار برای تصمیم‌گیری درباره‌ی نیاز به اعتبارسنجی آن‌ها استفاده کند. باید یک زیردامنه DNS باشد و بهتر است به یک دامنه DNS ختم شود که متعلق به فروشنده درایور است. فقط باید از حروف کوچک استفاده کند.</td>
    </tr>
    <tr>
      <td><code>parameters</code>&nbsp;<strong>*</strong><br/><em></em></td>
      <td>Parameters می‌تواند داده‌های دلخواه را در خود جای دهد. مسئولیت مدیریت اعتبارسنجی و نسخه‌بندی بر عهده توسعه‌دهنده درایور است. معمولاً این کار شامل خودشناسایی و یک نسخه ("kind" + "apiVersion" برای انواع کوبرنتیز) همراه با تبدیل بین نسخه‌های مختلف است. طول داده خام باید کمتر از یا برابر با 10 Ki باشد.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /apis/resource.k8s.io/v1/deviceclasses



#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر: - All: همه مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به بازیگر یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور دستور می‌دهد که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همه فیلدهای ناشناخته‌ای را که بی‌سروصدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق سرایند پاسخ هشدار استاندارد یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و فقط آخرین مورد از هر فیلد تکراری ماندگار خواهد شد. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر هر فیلد ناشناخته‌ای قرار باشد از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری خواهد بود که با آن‌ها مواجه شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
  </tbody>
</table>

### `patch` Patch

#### درخواست HTTP

PATCH /apis/resource.k8s.io/v1/deviceclasses/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام DeviceClass</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (یعنی JsonPatch، MergePatch و StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته بدون هشدار از آبجکت حذف می‌شوند و از میان فیلدهای تکراری فقط آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود در نظر گرفته می‌شود. این رفتار پیش‌فرض پیش از نسخه 1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌شود. در صورت نبود خطای دیگر، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه 1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل تمام فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. این یعنی کاربر مالکیت فیلدهای دارای تداخل را که در اختیار دیگران است دوباره به دست می‌آورد. برای درخواست‌های patch غیر از apply، پرچم force نباید تنظیم شود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
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
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace

#### درخواست HTTP

PUT /apis/resource.k8s.io/v1/deviceclasses/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام DeviceClass</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته بدون هشدار از آبجکت حذف می‌شوند و از میان فیلدهای تکراری فقط آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود در نظر گرفته می‌شود. این رفتار پیش‌فرض پیش از نسخه 1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌شود. در صورت نبود خطای دیگر، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه 1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگردانده‌شده از سرور شامل تمام فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete

#### درخواست HTTP

DELETE /apis/resource.k8s.io/v1/deviceclasses/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام DeviceClass</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان به ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دوره مهلت (grace period) پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به ازای هر آبجکت تعیین می‌شود. مقدار صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای آبجکت خراب (corrupt) ناموفق شود، حذف ناامن منبع آغاز می‌شود. یک منبع در صورتی خراب در نظر گرفته می‌شود که به دلیل الف) غیرقابل تبدیل بودن داده‌های آن، مثلاً شکست در رمزگشایی (decryption)، یا ب) ناموفق بودن رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌ساز زیربنایی بازیابی کرد. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به جریان عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید برای فعال‌سازی آن آگاهانه اقدام کند.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آبجکت‌های وابسته به حالت یتیم (orphan) درآیند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول: 'Orphan' - وابسته‌ها به حالت یتیم درمی‌آیند؛ 'Background' - به garbage collector اجازه داده می‌شود وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری (cascading) که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
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
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/resource.k8s.io/v1/deviceclasses



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک توکن continue خطای 410 ResourceExpired را برمی‌گرداند. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده ارسال کند؛ سرور فهرستی را از کلید بعدی و از جدیدترین snapshot برمی‌گرداند که با نتایج فهرست قبلی ناسازگار است؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true است پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. مقدار نامعتبر یا ناشناخته dryRun به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نمی‌گیرد. مقادیر معتبر عبارتند از: - All: تمام مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان به ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از دوره مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت تعیین می‌شود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. منبعی خراب در نظر گرفته می‌شود که به دلیل الف) غیرقابل تبدیل بودن داده‌هایش، برای مثال شکست در رمزگشایی، یا ب) شکست در رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌ساز زیرین بازیابی کرد. توجه: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌ساز حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به جریان عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد موارد کمتری از مقدار درخواستی (حتی صفر مورد) برگرداند و کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true است پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند با صدور یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه نتیجه اولین فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارتند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که تمام وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت کنونی آبجکت‌های موجود در مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای که دست‌کم به اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌کوتیشن قرار می‌گیرند و پیشوند '0x' دارند؛ آن‌ها کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای hash ‏FNV-1a ۶۴ بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و نیاز دارد feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار، فارغ از هرگونه فعالیت یا عدم فعالیت، مدت فراخوانی را محدود می‌کند.</td>
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

GET /apis/resource.k8s.io/v1/deviceclasses/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام DeviceClass</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "device-class-v1#DeviceClass" >}}">DeviceClass</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/deviceclasses



#### پارامترهای پرس‌وجو (Query Parameters)

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور می‌تواند مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراهرداده (metadata) فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعداد کمتری از موارد درخواست‌شده (حتی صفر مورد) را بازگرداند و کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت نتایج بسیار بزرگ در بخش‌های کوچک‌تر از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه نتیجه اول فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، باید گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و نه از قالب fieldSelector (یعنی "metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL داخل تک‌کوتیشن با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را بر فضای hash 64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی فهرست/watch. این مقدار مدت فراخوانی را، بدون توجه به فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "device-class-v1#DeviceClassList" >}}">DeviceClassList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### درخواست HTTP

GET /apis/resource.k8s.io/v1/watch/deviceclasses/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام DeviceClass</td>
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
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی برگردانده می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک continue token با خطای 410 ResourceExpired پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج قبلی فهرست سازگار نیست - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم برگرداند (حتی صفر آیتم)، و کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، ویرایش یا حذف شده باشد، در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این ویژگی گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای متناظر با تغییرات آبجکت‌های تحت نظر (پس از آن RV) را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر منطقی OR) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (مثلاً "object.metadata.uid") و نه قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون single-quote با پیشوند '0x' هستند و کران پایین شمولی و کران بالای غیرشمولی را در فضای hash ‏FNV-1a ۶۴ بیتی تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشمولی برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به هرگونه فعالیت یا عدم فعالیت محدود می‌کند.</td>
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

GET /apis/resource.k8s.io/v1/watch/deviceclasses



#### پارامترهای Query

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks درخواست می‌کند رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند bookmarkها در فاصله‌های زمانی مشخصی ارسال می‌شوند و نیز نباید فرض کنند سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک پرسوجوی قبلی با پارامترهای یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور ممکن است مقدار continue‌ای را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکنِ دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند، بی‌آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرسوجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواست‌شده (حتی صفر آیتم) برگرداند، در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد، در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی روی نسخه‌های منبعی تعیین می‌کند که درخواست می‌تواند از آن‌ها پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظارت را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم‌نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو شیء‌محور CEL (برای مثال "object.metadata.uid") استفاده می‌کنند، نه قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که داخل تک‌نقل‌قول قرار می‌گیرند و با پیشوند '0x' شروع می‌شوند. این دو مقدار به‌ترتیب کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch فعال شود.</td>
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
