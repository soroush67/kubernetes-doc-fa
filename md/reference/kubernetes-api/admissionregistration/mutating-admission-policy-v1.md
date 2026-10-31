---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "MutatingAdmissionPolicy"
content_type: "api_reference"
description: "نوع MutatingAdmissionPolicy تعریف یک سیاست تغییر در مرحله‌ی پذیرش را توصیف می‌کند که آبجکتِ واردشده به زنجیره‌ی پذیرش را تغییر می‌دهد."
title: "MutatingAdmissionPolicy"
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

`apiVersion: admissionregistration.k8s.io/v1`

`import "k8s.io/api/admissionregistration/v1"`


## MutatingAdmissionPolicy {#MutatingAdmissionPolicy}

نوع MutatingAdmissionPolicy تعریف یک سیاست تغییر در مرحله‌ی پذیرش (admission mutation policy) را توصیف می‌کند که آبجکتِ واردشده به زنجیره‌ی پذیرش را تغییر می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌واره‌ی نسخه‌دارِ این نمایش از یک آبجکت را تعیین می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از نقطه‌ی پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این مقدار قابل به‌روزرسانی نیست و با نگارش CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فیلد metadata فراداده‌ی استاندارد آبجکت است؛ اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#MutatingAdmissionPolicySpec" >}}">MutatingAdmissionPolicySpec</a></em></td>
      <td>فیلد spec رفتار مطلوب MutatingAdmissionPolicy را تعریف می‌کند.</td>
    </tr>
  </tbody>
</table>


## MutatingAdmissionPolicySpec {#MutatingAdmissionPolicySpec}

نوع MutatingAdmissionPolicySpec رفتار مطلوب سیاست پذیرش را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>failurePolicy</code><br/><em>string</em></td>
      <td>فیلد failurePolicy تعیین می‌کند که خطاهای سیاست پذیرش چگونه مدیریت شوند. خطاها ممکن است ناشی از خطاهای تجزیه‌ی عبارت CEL، خطاهای بررسی نوع، خطاهای زمان اجرا و تعریف‌ها یا اتصال‌های (bindings) نامعتبر یا نادرست پیکربندی‌شده‌ی سیاست باشند. یک سیاست در صورتی نامعتبر است که paramKind به یک Kind ناموجود اشاره کند. یک اتصال در صورتی نامعتبر است که paramRef.name به منبعی ناموجود اشاره کند. فیلد failurePolicy تعیین نمی‌کند که اعتبارسنجی‌هایی که نتیجه‌ی آن‌ها false است چگونه مدیریت شوند. مقادیر مجاز Ignore یا Fail هستند. مقدار پیش‌فرض Fail است.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"Fail"` به این معناست که خطا در فراخوانی وبهوک باعث شکست پذیرش می‌شود.<br/> - مقدار `"Ignore"` به این معناست که خطا در فراخوانی وبهوک نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>matchConditions</code><br/><em><a href="{{< ref "../definitions/match-condition-v1-admissionregistration#MatchCondition" >}}">آرایه‌ی MatchCondition</a></em><br/><em>راهبرد patch: ادغام بر اساس کلید <code>name</code></em></td>
      <td>فیلد matchConditions فهرستی از شرط‌هایی است که برای اعتبارسنجی یک درخواست باید برقرار باشند. شرط‌های تطابق، درخواست‌هایی را فیلتر می‌کنند که پیش‌تر با matchConstraints تطابق یافته‌اند. فهرست خالی matchConditions با همه‌ی درخواست‌ها تطابق دارد. حداکثر ۶۴ شرط تطابق مجاز است. اگر یک آبجکت پارامتر ارائه شود، می‌توان مانند عبارت‌های اعتبارسنجی، از طریق دستگیره‌ی `params` به آن دسترسی داشت. منطق دقیق تطابق (به ترتیب) چنین است:   1. اگر هر یک از matchConditionها به FALSE ارزیابی شود، از سیاست صرف‌نظر می‌شود.   2. اگر همه‌ی matchConditionها به TRUE ارزیابی شوند، سیاست ارزیابی می‌شود.   3. اگر ارزیابی هر یک از matchConditionها به خطا بینجامد (اما هیچ‌کدام FALSE نباشد):      - اگر failurePolicy=Fail باشد، درخواست رد می‌شود      - اگر failurePolicy=Ignore باشد، از سیاست صرف‌نظر می‌شود</td>
    </tr>
    <tr>
      <td><code>matchConstraints</code><br/><em><a href="{{< ref "../definitions/match-resources-v1-admissionregistration#MatchResources" >}}">MatchResources</a></em></td>
      <td>فیلد matchConstraints مشخص می‌کند که این سیاست برای اعتبارسنجی چه منابعی طراحی شده است. سیاست MutatingAdmissionPolicy تنها زمانی به یک درخواست توجه می‌کند که آن درخواست با _همه‌ی_ محدودیت‌ها تطابق داشته باشد. با این حال، برای جلوگیری از قرار گرفتن کلاسترها در وضعیتی ناپایدار که نتوان از طریق API آن را بازیابی کرد، MutatingAdmissionPolicy نمی‌تواند با MutatingAdmissionPolicy و MutatingAdmissionPolicyBinding تطابق داشته باشد. عملیات CREATE، UPDATE و CONNECT مجاز هستند. عملیات DELETE را نمی‌توان تطابق داد. مقدار '\*' با CREATE، UPDATE و CONNECT تطابق دارد. الزامی است.</td>
    </tr>
    <tr>
      <td><code>mutations</code><br/><em><a href="{{< ref "#Mutation" >}}">آرایه‌ی Mutation</a></em></td>
      <td>فیلد mutations شامل عملیاتی است که باید روی آبجکت‌های منطبق انجام شوند. این فیلد نمی‌تواند خالی باشد و دست‌کم یک تغییر (mutation) لازم است. تغییرها به ترتیب ارزیابی می‌شوند و بر اساس reinvocationPolicy دوباره فراخوانی می‌شوند. تغییرهای یک سیاست برای هر اتصال این سیاست فراخوانی می‌شوند و فراخوانی مجدد تغییرها نیز به‌ازای هر اتصال به‌طور جداگانه انجام می‌شود.</td>
    </tr>
    <tr>
      <td><code>paramKind</code><br/><em><a href="{{< ref "../definitions/param-kind-v1-admissionregistration#ParamKind" >}}">ParamKind</a></em></td>
      <td>فیلد paramKind نوع منابعی را مشخص می‌کند که برای پارامتری‌کردن این سیاست استفاده می‌شوند. اگر این فیلد وجود نداشته باشد، این سیاست هیچ پارامتری ندارد و متغیر CEL با نام param در اختیار عبارت‌های اعتبارسنجی قرار نمی‌گیرد. اگر paramKind به یک kind ناموجود اشاره کند، تعریف این سیاست نادرست پیکربندی شده است و FailurePolicy اعمال می‌شود. اگر paramKind مشخص شده باشد اما paramRef در MutatingAdmissionPolicyBinding تنظیم نشده باشد، مقدار متغیر params برابر null خواهد بود.</td>
    </tr>
    <tr>
      <td><code>reinvocationPolicy</code><br/><em>string</em></td>
      <td>فیلد reinvocationPolicy نشان می‌دهد که آیا تغییرها می‌توانند در یک ارزیابی پذیرش واحد، به‌ازای هر MutatingAdmissionPolicyBinding چندین بار فراخوانی شوند یا نه. مقادیر مجاز "Never" و "IfNeeded" هستند. مقدار Never: این تغییرها در یک ارزیابی پذیرش واحد بیش از یک بار به‌ازای هر اتصال فراخوانی نمی‌شوند. مقدار IfNeeded: این تغییرها ممکن است برای یک درخواست پذیرش واحد بیش از یک بار به‌ازای هر اتصال فراخوانی شوند و هیچ تضمینی درباره‌ی ترتیب آن‌ها نسبت به سایر افزونه‌های پذیرش، وبهوک‌های پذیرش، اتصال‌های این سیاست و سیاست‌های پذیرش وجود ندارد. تغییرها تنها زمانی دوباره فراخوانی می‌شوند که پس از فراخوانی این تغییر، تغییرهای دیگری آبجکت را دگرگون کنند. الزامی است.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"IfNeeded"` نشان می‌دهد که اگر سایر افزونه‌های پذیرش پس از فراخوانی اولیه‌ی تغییر، آبجکتِ در حال پذیرش را تغییر دهند، ممکن است این تغییر به‌عنوان بخشی از ارزیابی پذیرش دست‌کم یک بار دیگر فراخوانی شود.<br/> - مقدار `"Never"` نشان می‌دهد که این تغییر نباید در یک ارزیابی پذیرش واحد بیش از یک بار فراخوانی شود.</td>
    </tr>
    <tr>
      <td><code>variables</code><br/><em><a href="{{< ref "../definitions/variable-v1-admissionregistration#Variable" >}}">آرایه‌ی Variable</a></em></td>
      <td>فیلد variables شامل تعریف متغیرهایی است که می‌توان در ترکیب عبارت‌های دیگر از آن‌ها استفاده کرد. هر متغیر به‌صورت یک عبارت CEL نام‌دار تعریف می‌شود. متغیرهای تعریف‌شده در اینجا در سایر عبارت‌های سیاست، به‌جز matchConditions، زیر `variables` در دسترس خواهند بود؛ زیرا matchConditions پیش از بقیه‌ی سیاست ارزیابی می‌شوند. عبارت یک متغیر می‌تواند به متغیرهایی ارجاع دهد که پیش‌تر در فهرست تعریف شده‌اند، اما نمی‌تواند به متغیرهای بعدی ارجاع دهد. بنابراین متغیرها باید به ترتیب نخستین ظهور مرتب شوند و وابستگی چرخه‌ای نداشته باشند.</td>
    </tr>
  </tbody>
</table>


## MutatingAdmissionPolicyList {#MutatingAdmissionPolicyList}

نوع MutatingAdmissionPolicyList فهرستی از MutatingAdmissionPolicy است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌واره‌ی نسخه‌دارِ این نمایش از یک آبجکت را تعیین می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">آرایه‌ی MutatingAdmissionPolicy</a></em></td>
      <td>فهرست ValidatingAdmissionPolicy.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از نقطه‌ی پایانی که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این مقدار قابل به‌روزرسانی نیست و با نگارش CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فیلد metadata فراداده‌ی استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## ApplyConfiguration {#ApplyConfiguration}

نوع ApplyConfiguration مقادیر پیکربندی مطلوب یک آبجکت را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code><br/><em>string</em></td>
      <td>فیلد expression به‌وسیله‌ی CEL ارزیابی می‌شود تا یک پیکربندی اعمال (apply configuration) ایجاد شود. مرجع: https://github.com/google/cel-spec  پیکربندی‌های اعمال در CEL با مقداردهی اولیه‌ی آبجکت اعلان می‌شوند. برای مثال، عبارت CEL زیر یک پیکربندی اعمال برمی‌گرداند که یک فیلد واحد را تنظیم می‌کند:  	Object{ 	  spec: Object.spec{ 	    serviceAccountName: "example" 	  } 	}  پیکربندی‌های اعمال نمی‌توانند ساختارها (struct)، نگاشت‌ها (map) یا آرایه‌های اتمی را تغییر دهند، زیرا این کار خطر حذف ناخواسته‌ی مقادیری را دارد که در پیکربندی اعمال گنجانده نشده‌اند.  عبارت‌های CEL به انواع آبجکتی که برای ایجاد پیکربندی‌های اعمال لازم است دسترسی دارند:  - 'Object' - نوع CEL آبجکت منبع. - 'Object.\<fieldName>' - نوع CEL فیلد آبجکت (مانند 'Object.spec') - 'Object.\<fieldName1>.\<fieldName2>...\<fieldNameN>` - نوع CEL فیلد تودرتو (مانند 'Object.spec.containers')  عبارت‌های CEL به محتوای درخواست API که در قالب متغیرهای CEL سازمان‌دهی شده است و نیز به برخی متغیرهای مفید دیگر دسترسی دارند:  - 'object' - آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است. - 'oldObject' - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است. - 'request' - ویژگی‌های درخواست API ([مرجع](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - منبع پارامتری که اتصالِ سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. این متغیر تنها در صورتی مقدار می‌گیرد که سیاست دارای ParamKind باشد. - 'namespaceObject' - آبجکت فضای نام (namespace) که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابع در سطح کلاستر برابر null است. - 'variables' - نگاشتی از متغیرهای ترکیبی، از نام هر متغیر به مقدار آن که به‌صورت تنبل (lazy) ارزیابی می‌شود.   برای مثال، به متغیری با نام 'foo' می‌توان از طریق 'variables.foo' دسترسی داشت. - 'authorizer' - یک Authorizer در CEL. می‌توان از آن برای انجام بررسی‌های مجوزدهی برای هویت اصلی (کاربر یا حساب سرویس) درخواست استفاده کرد.   به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید - 'authorizer.requestResource' - یک ResourceCheck در CEL که از 'authorizer' ساخته شده و با منبع   درخواست پیکربندی شده است.  فیلدهای `apiVersion`، `kind`، `metadata.name` و `metadata.generateName` همیشه از ریشه‌ی آبجکت در دسترس هستند. هیچ ویژگی فراداده‌ی دیگری در دسترس نیست.  تنها نام ویژگی‌هایی به شکل `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` در دسترس هستند. الزامی است.</td>
    </tr>
  </tbody>
</table>


## JSONPatch {#JSONPatch}

نوع JSONPatch یک JSON Patch را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code><br/><em>string</em></td>
      <td>فیلد expression به‌وسیله‌ی CEL ارزیابی می‌شود تا یک [JSON patch](https://jsonpatch.com/) ایجاد شود. مرجع: https://github.com/google/cel-spec  عبارت expression باید آرایه‌ای از مقادیر JSONPatch برگرداند.  برای مثال، عبارت CEL زیر یک JSON patch برمی‌گرداند که یک مقدار را به‌صورت شرطی تغییر می‌دهد:  	  [ 	    JSONPatch{op: "test", path: "/spec/example", value: "Red"}, 	    JSONPatch{op: "replace", path: "/spec/example", value: "Green"} 	  ]  برای تعریف یک آبجکت به‌عنوان مقدار patch، از انواع Object استفاده کنید. برای مثال:  	  [ 	    JSONPatch{ 	      op: "add", 	      path: "/spec/selector", 	      value: Object.spec.selector{matchLabels: {"environment": "test"}} 	    } 	  ]  برای استفاده از رشته‌های حاوی '/' و '~' به‌عنوان کلیدهای مسیر JSONPatch، از "jsonpatch.escapeKey" استفاده کنید. برای مثال:  	  [ 	    JSONPatch{ 	      op: "add", 	      path: "/metadata/labels/" + jsonpatch.escapeKey("example.com/environment"), 	      value: "test" 	    }, 	  ]  عبارت‌های CEL به انواعی که برای ایجاد JSON patchها و آبجکت‌ها لازم است دسترسی دارند:  - 'JSONPatch' - نوع CEL عملیات JSON Patch. نوع JSONPatch فیلدهای 'op'، 'from'، 'path' و 'value' را دارد.   برای جزئیات بیشتر به [JSON patch](https://jsonpatch.com/) مراجعه کنید. فیلد 'value' می‌تواند هر یک از این انواع باشد: string،   integer، array، map یا object.  اگر فیلدهای 'path' و 'from' تنظیم شوند، باید رشته‌ای از نوع   [JSON pointer](https://datatracker.ietf.org/doc/html/rfc6901/) باشند که در آن می‌توان از تابع CEL با نام 'jsonpatch.escapeKey()'   برای نویسه‌گریزی (escape) کلیدهای مسیر حاوی '/' و '~' استفاده کرد. - 'Object' - نوع CEL آبجکت منبع. - 'Object.\<fieldName>' - نوع CEL فیلد آبجکت (مانند 'Object.spec') - 'Object.\<fieldName1>.\<fieldName2>...\<fieldNameN>` - نوع CEL فیلد تودرتو (مانند 'Object.spec.containers')  عبارت‌های CEL به محتوای درخواست API که در قالب متغیرهای CEL سازمان‌دهی شده است و نیز به برخی متغیرهای مفید دیگر دسترسی دارند:  - 'object' - آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است. - 'oldObject' - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است. - 'request' - ویژگی‌های درخواست API ([مرجع](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - منبع پارامتری که اتصالِ سیاستِ در حال ارزیابی به آن ارجاع می‌دهد. این متغیر تنها در صورتی مقدار می‌گیرد که سیاست دارای ParamKind باشد. - 'namespaceObject' - آبجکت فضای نامی که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابع در سطح کلاستر برابر null است. - 'variables' - نگاشتی از متغیرهای ترکیبی، از نام هر متغیر به مقدار آن که به‌صورت تنبل ارزیابی می‌شود.   برای مثال، به متغیری با نام 'foo' می‌توان از طریق 'variables.foo' دسترسی داشت. - 'authorizer' - یک Authorizer در CEL. می‌توان از آن برای انجام بررسی‌های مجوزدهی برای هویت اصلی (کاربر یا حساب سرویس) درخواست استفاده کرد.   به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید - 'authorizer.requestResource' - یک ResourceCheck در CEL که از 'authorizer' ساخته شده و با منبع   درخواست پیکربندی شده است.  عبارت‌های CEL به [کتابخانه‌های توابع CEL در کوبرنتیز](https://kubernetes.io/docs/reference/using-api/cel/#cel-options-language-features-and-libraries) و همچنین موارد زیر دسترسی دارند:  - 'jsonpatch.escapeKey' - نویسه‌گریزی کلیدهای JSONPatch را انجام می‌دهد. نویسه‌های '~' و  '/' به‌ترتیب به '~0' و `~1' تبدیل می‌شوند).  تنها نام ویژگی‌هایی به شکل `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` در دسترس هستند. الزامی است.</td>
    </tr>
  </tbody>
</table>


## Mutation {#Mutation}

نوع Mutation عبارت CEL را مشخص می‌کند که برای اعمال این تغییر استفاده می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>applyConfiguration</code><br/><em><a href="{{< ref "#ApplyConfiguration" >}}">ApplyConfiguration</a></em></td>
      <td>فیلد applyConfiguration مقادیر پیکربندی مطلوب یک آبجکت را تعریف می‌کند. این پیکربندی با استفاده از [structured merge diff](https://github.com/kubernetes-sigs/structured-merge-diff) روی آبجکت پذیرش اعمال می‌شود. برای ایجاد پیکربندی اعمال از یک عبارت CEL استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>jsonPatch</code><br/><em><a href="{{< ref "#JSONPatch" >}}">JSONPatch</a></em></td>
      <td>فیلد jsonPatch یک عملیات [JSON patch](https://jsonpatch.com/) را برای اعمال تغییر روی آبجکت تعریف می‌کند. برای ایجاد JSON patch از یک عبارت CEL استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>patchType</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد patchType راهبرد patch مورداستفاده را نشان می‌دهد. مقادیر مجاز "ApplyConfiguration" و "JSONPatch" هستند. الزامی است.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"ApplyConfiguration"`: مقدار ApplyConfiguration نشان می‌دهد که تغییر برای دگرگون کردن آبجکت از پیکربندی اعمال استفاده می‌کند.<br/> - مقدار `"JSONPatch"`: مقدار JSONPatch نشان می‌دهد که آبجکت از طریق JSON Patch تغییر داده می‌شود.</td>
    </tr>
  </tbody>
</table>



## عملیات {#Operations}

<hr>

### ایجاد (`post`)

#### درخواست HTTP

POST /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده (pretty-printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. این مقدار باید حداکثر 128 نویسه داشته باشد و فقط شامل نویسه‌های قابل چاپ باشد؛ نویسه‌های قابل چاپ در https://golang.org/pkg/unicode/#IsPrint تعریف شده‌اند.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: با این مقدار، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: با این مقدار، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، هشداری از طریق هدر استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: با این مقدار، اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همهٔ فیلدهای ناشناخته و تکراری‌ای است که با آن‌ها روبه‌رو شده است.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد (Accepted)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### وصله‌کردن (`patch`)

#### درخواست HTTP

PATCH /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام MutatingAdmissionPolicy</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. این مقدار باید حداکثر 128 نویسه داشته باشد و فقط شامل نویسه‌های قابل چاپ باشد؛ نویسه‌های قابل چاپ در https://golang.org/pkg/unicode/#IsPrint تعریف شده‌اند. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: با این مقدار، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: با این مقدار، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، هشداری از طریق هدر استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: با این مقدار، اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همهٔ فیلدهای ناشناخته و تکراری‌ای است که با آن‌ها روبه‌رو شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «به‌اجبار» اعمال می‌کند؛ یعنی کاربر مالکیت فیلدهای متعارضی را که متعلق به دیگران است دوباره به دست می‌گیرد. برای درخواست‌های patch غیر apply، پرچم Force نباید تنظیم شود.</td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### جایگزینی (`put`)

#### درخواست HTTP

PUT /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام MutatingAdmissionPolicy</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. این مقدار باید حداکثر 128 نویسه داشته باشد و فقط شامل نویسه‌های قابل چاپ باشد؛ نویسه‌های قابل چاپ در https://golang.org/pkg/unicode/#IsPrint تعریف شده‌اند.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: با این مقدار، فیلدهای ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شوند نادیده گرفته می‌شوند و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: با این مقدار، برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، هشداری از طریق هدر استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: با این مقدار، اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همهٔ فیلدهای ناشناخته و تکراری‌ای است که با آن‌ها روبه‌رو شده است.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### حذف (`delete`)

#### درخواست HTTP

DELETE /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام MutatingAdmissionPolicy</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمانی بر حسب ثانیه که پیش از حذف آبجکت باید سپری شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. اگر مقداری مشخص نشود، مقدار پیش‌فرض مختص هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که: الف) داده‌های آن قابل تبدیل نیستند، مثلاً رمزگشایی (decryption) آن‌ها شکست می‌خورد؛ یا ب) تبدیل (decode) آن به آبجکت با شکست مواجه می‌شود. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. این فیلد تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر مقدار آن true یا false باشد، finalizer «orphan» به‌ترتیب به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و اگر انجام شود، به چه صورت. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها یتیم می‌شوند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه داده می‌شود وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد (Accepted)</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `delete`: حذف مجموعه

#### درخواست HTTP

DELETE /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ آخرین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و درخواست بیش از این پردازش نمی‌شود. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمان، برحسب ثانیه، پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به ازای هر آبجکت تعیین می‌شود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب شکست بخورد، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیربنایی بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، مثلاً رمزگشایی شکست می‌خورد، یا ب) کدگشایی (decode) آن به یک آبجکت ناموفق است. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط زمانی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر برای فعال‌سازی آن باید صراحتاً آن را انتخاب کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>مقدار limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در متادیتای فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه همان کوئری اولیه برای بازیابی مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه، استفاده کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند نتیجهٔ دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی تصویر لحظه‌ای سازگار گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در قطعه‌های کوچک‌تر دریافت می‌کند، بتواند همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر مقدار آن true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا و چگونه جمع‌آوری زباله (garbage collection) انجام شود. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس finalizer موجود در metadata.finalizers و سیاست پیش‌فرض ویژهٔ هر منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شود، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به‌صورت «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا یک `resourceVersion` به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، مقدار پیش‌فرض true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار، مدت‌زمان فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
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


### عملیات `get`: خواندن

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام MutatingAdmissionPolicy</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicy" >}}">MutatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>

### دریافت فهرست با `get`

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/mutatingadmissionpolicies



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده (pretty-printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فواصل زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر اساس جدیدترین snapshot تهیه شده و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ (metadata) فهرست به مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است به بازگشت تعدادی کمتر از مقدار درخواست‌شده (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی snapshot سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را بازتولید می‌کنند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به‌صورت «داده‌هایی دست‌کم به جدیدیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض، در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "mutating-admission-policy-v1#MutatingAdmissionPolicyList" >}}">MutatingAdmissionPolicyList</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات Watch با `get`

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/watch/mutatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام MutatingAdmissionPolicy</td>
    </tr>
  </tbody>
</table>


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>فیلد allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوک‌مارک‌ها را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال بوک‌مارک‌ها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که بوک‌مارک‌ها در فاصله‌ی زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه‌ی continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه‌ی یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما بر پایه‌ی جدیدترین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست: آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) که فهرست آبجکت‌های بازگردانده‌شده را بر اساس فیلدهایشان محدود می‌کند. به‌طور پیش‌فرض همه‌ی آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری که فهرست آبجکت‌های بازگردانده‌شده را بر اساس برچسب‌هایشان محدود می‌کند. به‌طور پیش‌فرض همه‌ی آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌ی فهرست روی مقداری تنظیم می‌کند که می‌توان از آن همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه‌ی بعدی نتایج استفاده کرد. اگر همه‌ی آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواست‌شده (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همه‌ی نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجه‌ی یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی تصویر لحظه‌ای سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر از یک نتیجه‌ی بسیار بزرگ استفاده می‌کند، همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری بخش‌بخش به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان بر اساس کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازتولید کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوک‌مارک مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظارت را ارسال می‌کند. هنگامی که گزینه‌ی `sendInitialEvents` تنظیم شده باشد، لازم است گزینه‌ی `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این شرح است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به‌صورت «داده‌هایی دست‌کم به جدیدیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوک‌مارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ نسخه‌ی ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد بوک‌مارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت برابر false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه‌ی هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه‌ی object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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

### `get` پایش فهرست (Watch List)

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/watch/mutatingadmissionpolicies



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینهٔ continue را تنظیم کرد. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر اساس جدیدترین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، در صورتی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست با مقداری پر می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است به بازگشت آیتم‌هایی کمتر از مقدار درخواستی (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. اگر watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی از این ویژگی با عنوان snapshot سازگار یاد می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در بخش‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>گزینهٔ `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را تولید کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) در آبجکت‌های تحت پایش را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض، در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با عملگر || (یای منطقی) برای تعیین یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون تک‌نقل‌قول با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحلهٔ آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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
