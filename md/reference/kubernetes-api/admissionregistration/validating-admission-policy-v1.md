---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "ValidatingAdmissionPolicy"
content_type: "api_reference"
description: "آبجکت ValidatingAdmissionPolicy تعریف یک سیاست اعتبارسنجی پذیرش را توصیف می‌کند که یک آبجکت را بدون تغییر دادن آن می‌پذیرد یا رد می‌کند."
title: "ValidatingAdmissionPolicy"
weight: 40
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


## ValidatingAdmissionPolicy {#ValidatingAdmissionPolicy}

آبجکت ValidatingAdmissionPolicy تعریف یک سیاست اعتبارسنجی پذیرش (admission validation policy) را توصیف می‌کند که یک آبجکت را بدون تغییر دادن آن می‌پذیرد یا رد می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ (schema) نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از نقطهٔ پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. مقدار آن به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فیلد metadata فرادادهٔ استاندارد آبجکت است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#ValidatingAdmissionPolicySpec" >}}">ValidatingAdmissionPolicySpec</a></em></td>
      <td>فیلد spec رفتار مطلوب ValidatingAdmissionPolicy را تعریف می‌کند.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#ValidatingAdmissionPolicyStatus" >}}">ValidatingAdmissionPolicyStatus</a></em></td>
      <td>فیلد status وضعیت فعلی ValidatingAdmissionPolicy را نشان می‌دهد؛ از جمله هشدارهایی که برای تشخیص اینکه آیا سیاست مطابق انتظار رفتار می‌کند یا نه، مفیدند. این فیلد را سیستم پر می‌کند و فقط‌خواندنی است.</td>
    </tr>
  </tbody>
</table>


## ValidatingAdmissionPolicySpec {#ValidatingAdmissionPolicySpec}

نوع ValidatingAdmissionPolicySpec مشخصات رفتار مطلوب AdmissionPolicy را تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>auditAnnotations</code><br/><em><a href="{{< ref "#AuditAnnotation" >}}">AuditAnnotation array</a></em></td>
      <td>فیلد auditAnnotations شامل عبارت‌های CEL است که برای تولید حاشیه‌نویسی‌های ممیزی (audit annotations) در رویداد ممیزی درخواست API به کار می‌روند. فیلدهای validations و auditAnnotations نمی‌توانند هر دو خالی باشند؛ وجود دست‌کم یکی از آن‌ها الزامی است.</td>
    </tr>
    <tr>
      <td><code>failurePolicy</code><br/><em>string</em></td>
      <td>فیلد failurePolicy نحوهٔ رسیدگی به خطاها را در سیاست پذیرش تعریف می‌کند. خطاها ممکن است ناشی از خطاهای تجزیهٔ عبارت CEL، خطاهای بررسی نوع، خطاهای زمان اجرا، و تعریف‌ها یا اتصال‌های (bindings) نامعتبر یا نادرست پیکربندی‌شدهٔ سیاست باشند. یک سیاست زمانی نامعتبر است که spec.paramKind به یک Kind ناموجود اشاره کند. یک اتصال زمانی نامعتبر است که spec.paramRef.name به منبعی ناموجود اشاره کند. فیلد failurePolicy تعیین نمی‌کند که با اعتبارسنجی‌هایی که حاصل ارزیابی‌شان false است چگونه رفتار شود. وقتی failurePolicy روی Fail تنظیم شده باشد، فیلد validationActions در ValidatingAdmissionPolicyBinding نحوهٔ اعمال خطاها را تعیین می‌کند. مقادیر مجاز Ignore یا Fail هستند. مقدار پیش‌فرض Fail است.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"Fail"` به این معناست که خطا در فراخوانی وب‌هوک (webhook) باعث شکست پذیرش می‌شود.<br/> - مقدار `"Ignore"` به این معناست که خطا در فراخوانی وب‌هوک نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>matchConditions</code><br/><em><a href="{{< ref "../definitions/match-condition-v1-admissionregistration#MatchCondition" >}}">MatchCondition array</a></em><br/><em>راهبرد وصله (patch strategy): ادغام بر اساس کلید <code>name</code></em></td>
      <td>فیلد matchConditions فهرستی از شرط‌هایی است که برای اعتبارسنجی یک درخواست باید برقرار باشند. شرط‌های تطبیق، درخواست‌هایی را پالایش می‌کنند که پیش‌تر با rules، namespaceSelector و objectSelector تطبیق یافته‌اند. فهرست خالی matchConditions با همهٔ درخواست‌ها تطبیق می‌یابد. حداکثر ۶۴ شرط تطبیق مجاز است.  اگر آبجکت پارامتری ارائه شده باشد، می‌توان مانند عبارت‌های اعتبارسنجی، از طریق دستگیرهٔ `params` به آن دسترسی داشت.  منطق دقیق تطبیق به ترتیب زیر است:   ۱. اگر حاصل ارزیابی هر یک از matchConditionها FALSE باشد، از سیاست صرف‌نظر می‌شود.   ۲. اگر حاصل ارزیابی همهٔ matchConditionها TRUE باشد، سیاست ارزیابی می‌شود.   ۳. اگر ارزیابی هر یک از matchConditionها به خطا منجر شود (ولی حاصل هیچ‌کدام FALSE نباشد):      - اگر failurePolicy=Fail باشد، درخواست رد می‌شود      - اگر failurePolicy=Ignore باشد، از سیاست صرف‌نظر می‌شود</td>
    </tr>
    <tr>
      <td><code>matchConstraints</code><br/><em><a href="{{< ref "../definitions/match-resources-v1-admissionregistration#MatchResources" >}}">MatchResources</a></em></td>
      <td>فیلد matchConstraints مشخص می‌کند که این سیاست برای اعتبارسنجی چه منابعی طراحی شده است. آبجکت AdmissionPolicy تنها زمانی به یک درخواست رسیدگی می‌کند که آن درخواست با _همهٔ_ قیدها (Constraints) تطبیق داشته باشد. با این حال، برای جلوگیری از قرار گرفتن کلاسترها در وضعیتی ناپایدار که نتوان آن را از طریق API بازیابی کرد، ValidatingAdmissionPolicy نمی‌تواند با ValidatingAdmissionPolicy و ValidatingAdmissionPolicyBinding تطبیق یابد. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>paramKind</code><br/><em><a href="{{< ref "../definitions/param-kind-v1-admissionregistration#ParamKind" >}}">ParamKind</a></em></td>
      <td>فیلد paramKind نوع منابعی را مشخص می‌کند که برای پارامتری‌کردن این سیاست به کار می‌روند. اگر این فیلد وجود نداشته باشد، این سیاست پارامتری ندارد و متغیر param در CEL در اختیار عبارت‌های اعتبارسنجی قرار نمی‌گیرد. اگر ParamKind به نوعی ناموجود اشاره کند، تعریف این سیاست نادرست پیکربندی شده است و FailurePolicy اعمال می‌شود. اگر paramKind مشخص شده باشد ولی paramRef در ValidatingAdmissionPolicyBinding تنظیم نشده باشد، مقدار متغیر params برابر null خواهد بود.</td>
    </tr>
    <tr>
      <td><code>validations</code><br/><em><a href="{{< ref "#Validation" >}}">Validation array</a></em></td>
      <td>فیلد validations شامل عبارت‌های CEL است که برای اعمال اعتبارسنجی به کار می‌روند. فیلدهای Validations و AuditAnnotations نمی‌توانند هر دو خالی باشند؛ وجود دست‌کم یکی از آن‌ها الزامی است.</td>
    </tr>
    <tr>
      <td><code>variables</code><br/><em><a href="{{< ref "../definitions/variable-v1-admissionregistration#Variable" >}}">Variable array</a></em><br/><em>راهبرد وصله: ادغام بر اساس کلید <code>name</code></em></td>
      <td>فیلد variables شامل تعریف متغیرهایی است که می‌توان در ترکیب سایر عبارت‌ها از آن‌ها استفاده کرد. هر متغیر به‌صورت یک عبارت CEL نام‌دار تعریف می‌شود. متغیرهایی که در اینجا تعریف می‌شوند، در سایر عبارت‌های سیاست زیر `variables` در دسترس خواهند بود، به‌جز در MatchConditions؛ زیرا MatchConditions پیش از بقیهٔ سیاست ارزیابی می‌شوند.  عبارت یک متغیر می‌تواند به متغیرهایی که پیش‌تر در فهرست تعریف شده‌اند ارجاع دهد، اما نه به متغیرهای بعدی. بنابراین متغیرها باید به ترتیب نخستین ظهورشان مرتب شده باشند و وابستگی چرخه‌ای نداشته باشند.</td>
    </tr>
  </tbody>
</table>


## ValidatingAdmissionPolicyStatus {#ValidatingAdmissionPolicyStatus}

نوع ValidatingAdmissionPolicyStatus وضعیت یک سیاست اعتبارسنجی پذیرش را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "../definitions/condition-v1-meta#Condition" >}}">Condition array</a></em></td>
      <td>فیلد conditions آخرین مشاهدات موجود از وضعیت فعلی یک سیاست را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>فیلد observedGeneration نسلی (generation) است که کنترل‌کننده مشاهده کرده است.</td>
    </tr>
    <tr>
      <td><code>typeChecking</code><br/><em><a href="{{< ref "#TypeChecking" >}}">TypeChecking</a></em></td>
      <td>فیلد typeChecking نتایج بررسی نوع هر عبارت را در بر دارد. وجود این فیلد نشان‌دهندهٔ تکمیل بررسی نوع است.</td>
    </tr>
  </tbody>
</table>


## ValidatingAdmissionPolicyList {#ValidatingAdmissionPolicyList}

نوع ValidatingAdmissionPolicyList فهرستی از ValidatingAdmissionPolicyها است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy array</a></em></td>
      <td>فهرست ValidatingAdmissionPolicyها.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از نقطهٔ پایانی که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. مقدار آن به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فیلد metadata فرادادهٔ استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## AuditAnnotation {#AuditAnnotation}

نوع AuditAnnotation توصیف می‌کند که چگونه برای یک درخواست API حاشیه‌نویسی ممیزی تولید شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد key کلید حاشیه‌نویسی ممیزی را مشخص می‌کند. کلیدهای حاشیه‌نویسی ممیزی یک ValidatingAdmissionPolicy باید یکتا باشند. کلید باید یک نام واجد شرایط (qualified name) به شکل ([A-Za-z0-9][-A-Za-z0-9_.]*) با طول حداکثر ۶۳ بایت باشد.  این کلید با نام منبع ValidatingAdmissionPolicy ترکیب می‌شود تا یک کلید حاشیه‌نویسی ممیزی به شکل "{ValidatingAdmissionPolicy name}/{key}" ساخته شود.  اگر یک وب‌هوک پذیرش (admission webhook) از همان نام منبع این ValidatingAdmissionPolicy و همان کلید حاشیه‌نویسی ممیزی استفاده کند، کلیدهای حاشیه‌نویسی یکسان خواهند بود. در این حالت، نخستین حاشیه‌نویسی‌ای که با این کلید نوشته شود در رویداد ممیزی گنجانده می‌شود و همهٔ حاشیه‌نویسی‌های بعدی با همان کلید کنار گذاشته می‌شوند.  این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>valueExpression</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد valueExpression عبارتی را نشان می‌دهد که CEL آن را برای تولید مقدار حاشیه‌نویسی ممیزی ارزیابی می‌کند. حاصل ارزیابی این عبارت باید یک رشته یا مقدار null باشد. اگر حاصل ارزیابی یک رشته باشد، حاشیه‌نویسی ممیزی با همان مقدار رشته‌ای گنجانده می‌شود. اگر حاصل ارزیابی null یا رشتهٔ خالی باشد، حاشیه‌نویسی ممیزی حذف می‌شود. طول valueExpression نمی‌تواند بیش از 5kb باشد. اگر طول نتیجهٔ valueExpression بیش از 10kb باشد، به 10kb کوتاه می‌شود.  اگر چند منبع ValidatingAdmissionPolicyBinding با یک درخواست API تطبیق داشته باشند، valueExpression برای هر اتصال جداگانه ارزیابی می‌شود. همهٔ مقادیر یکتایی که valueExpressionها تولید می‌کنند، در قالب فهرستی جداشده با ویرگول به هم پیوسته می‌شوند.  این فیلد الزامی است.</td>
    </tr>
  </tbody>
</table>


## ExpressionWarning {#ExpressionWarning}

نوع ExpressionWarning اطلاعات هشداری است که به یک عبارت مشخص مربوط می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fieldRef</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد fieldRef مسیر فیلدی است که به عبارت ارجاع می‌دهد. برای مثال، ارجاع به عبارتِ نخستین مورد validations برابر "spec.validations[0].expression" است.</td>
    </tr>
    <tr>
      <td><code>warning</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد warning محتوای اطلاعات بررسی نوع را به شکلی خوانا برای انسان در بر دارد. هر خط از هشدار شامل نوعی است که عبارت در برابر آن بررسی شده و پس از آن، خطای بررسی نوعی که کامپایلر گزارش کرده است.</td>
    </tr>
  </tbody>
</table>


## TypeChecking {#TypeChecking}

نوع TypeChecking نتایج بررسی نوع عبارت‌های موجود در ValidatingAdmissionPolicy را در بر دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expressionWarnings</code><br/><em><a href="{{< ref "#ExpressionWarning" >}}">ExpressionWarning array</a></em></td>
      <td>فیلد expressionWarnings هشدارهای بررسی نوع را برای هر عبارت در بر دارد.</td>
    </tr>
  </tbody>
</table>

## Validation {#Validation}

نوع Validation عبارتی از CEL را مشخص می‌کند که برای انجام اعتبارسنجی به کار می‌رود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>expression</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد expression عبارتی را نشان می‌دهد که CEL آن را ارزیابی می‌کند. مرجع: https://github.com/google/cel-spec عبارت‌های CEL به محتوای درخواست/پاسخ API دسترسی دارند. این محتوا در قالب متغیرهای CEL سازمان‌دهی شده است و چند متغیر کاربردی دیگر نیز در دسترس است:  - 'object' - آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است. - 'oldObject' - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است. - 'request' - ویژگی‌های درخواست API ([مرجع](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - منبع پارامتری که اتصال سیاست (policy binding) در حال ارزیابی به آن ارجاع می‌دهد. این متغیر فقط زمانی مقدار می‌گیرد که سیاست دارای ParamKind باشد. - 'namespaceObject' - آبجکت فضای نام (namespace) که آبجکت ورودی به آن تعلق دارد. مقدار آن برای منابعی که در سطح کلاستر تعریف می‌شوند برابر null است. - 'variables' - نگاشتی از متغیرهای ترکیبی که نام هر متغیر را به مقدار آن نگاشت می‌کند؛ این مقدار به‌صورت تنبل (lazy) ارزیابی می‌شود.   برای مثال، به متغیری با نام 'foo' می‌توان از طریق 'variables.foo' دسترسی داشت. - 'authorizer' - یک Authorizer در CEL. با آن می‌توان بررسی‌های مجوزدهی را برای هویت اصلی (کاربر یا حساب سرویس) درخواست انجام داد.   برای اطلاعات بیشتر به https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz مراجعه کنید. - 'authorizer.requestResource' - یک ResourceCheck در CEL که از 'authorizer' ساخته شده و با منبع درخواست   پیکربندی شده است.  فیلدهای `apiVersion`، `kind`، `metadata.name` و `metadata.generateName` همیشه از ریشهٔ آبجکت در دسترس هستند. هیچ ویژگی دیگری از metadata در دسترس نیست.  فقط نام ویژگی‌هایی به شکل `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` در دسترس هستند. هنگام دسترسی به نام ویژگی‌های در دسترس در عبارت، این نام‌ها طبق قواعد زیر escape می‌شوند: - '__' به '__underscores__' تبدیل می‌شود - '.' به '__dot__' تبدیل می‌شود - '-' به '__dash__' تبدیل می‌شود - '/' به '__slash__' تبدیل می‌شود - نام ویژگی‌هایی که دقیقاً با یکی از کلیدواژه‌های رزروشده (RESERVED) در CEL یکسان باشند، به '__{keyword}__' تبدیل می‌شوند. این کلیدواژه‌ها عبارت‌اند از: 	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if", 	  "import", "let", "loop", "package", "namespace", "return". مثال‌ها:   - عبارتی که به ویژگی‌ای با نام "namespace" دسترسی دارد: {"Expression": "object.__namespace__ > 0"}   - عبارتی که به ویژگی‌ای با نام "x-prop" دسترسی دارد: {"Expression": "object.x__dash__prop > 0"}   - عبارتی که به ویژگی‌ای با نام "redact__d" دسترسی دارد: {"Expression": "object.redact__underscores__d > 0"}  در آرایه‌هایی که نوع فهرستشان 'set' یا 'map' است، مقایسهٔ برابری ترتیب عناصر را نادیده می‌گیرد؛ یعنی [1, 2] == [2, 1]. الحاق آرایه‌هایی که x-kubernetes-list-type دارند از معناشناسی همان نوع فهرست پیروی می‌کند:   - 'set': عبارت `X + Y` اجتماعی را انجام می‌دهد که در آن جایگاه همهٔ عناصر `X` در آرایه حفظ می‌شود و     عناصر غیرمشترکِ `Y` با حفظ ترتیب جزئی خود به انتهای آرایه افزوده می‌شوند.   - 'map': عبارت `X + Y` ادغامی را انجام می‌دهد که در آن جایگاه همهٔ کلیدهای `X` در آرایه حفظ می‌شود، اما هرگاه مجموعهٔ کلیدهای `X` و `Y` اشتراک داشته باشند،     مقادیر با مقادیر `Y` بازنویسی می‌شوند. عناصری از `Y` که کلیدهای غیرمشترک دارند،     با حفظ ترتیب جزئی خود به انتهای آرایه افزوده می‌شوند. الزامی.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>فیلد message پیامی را نشان می‌دهد که هنگام شکست اعتبارسنجی نمایش داده می‌شود. اگر Expression شامل شکست خط باشد، تعیین message الزامی است. پیام نباید شامل شکست خط باشد. اگر این فیلد تنظیم نشود، پیام "failed rule: {Rule}" خواهد بود. برای مثال: "must be a URL with the host matching spec.host". اگر Expression شامل شکست خط باشد، تعیین message الزامی است. پیام نباید شامل شکست خط باشد. اگر این فیلد تنظیم نشود، پیام "failed Expression: {Expression}" خواهد بود.</td>
    </tr>
    <tr>
      <td><code>messageExpression</code><br/><em>string</em></td>
      <td>فیلد messageExpression یک عبارت CEL تعریف می‌کند که حاصل ارزیابی آن، پیام شکست اعتبارسنجی است و هنگام شکست این قاعده برگردانده می‌شود. از آنجا که messageExpression به‌عنوان پیام شکست به کار می‌رود، حاصل ارزیابی آن باید یک رشته باشد. اگر برای یک اعتبارسنجی هم message و هم messageExpression تعیین شده باشد، هنگام شکست اعتبارسنجی از messageExpression استفاده می‌شود. اگر messageExpression به خطای زمان اجرا منجر شود، این خطا ثبت می‌شود و پیام شکست اعتبارسنجی طوری تولید می‌شود که گویی فیلد messageExpression تنظیم نشده است. اگر حاصل ارزیابی messageExpression رشته‌ای خالی، رشته‌ای فقط شامل فاصله یا رشته‌ای شامل شکست خط باشد، پیام شکست اعتبارسنجی باز هم طوری تولید می‌شود که گویی فیلد messageExpression تنظیم نشده است و این واقعیت که messageExpression رشته‌ای خالی، رشته‌ای فقط شامل فاصله یا رشته‌ای شامل شکست خط تولید کرده است نیز ثبت می‌شود. عبارت messageExpression به همهٔ متغیرهایی که `expression` به آن‌ها دسترسی دارد دسترسی دارد، به جز 'authorizer' و 'authorizer.requestResource'. مثال: "object.x must be less than max ("+string(params.max)+")"</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>فیلد reason توضیحی ماشین‌خوان از علت شکست این اعتبارسنجی ارائه می‌دهد. اگر این نخستین اعتبارسنجیِ فهرست باشد که شکست می‌خورد، این علت همراه با کد پاسخ HTTP متناظر با آن در پاسخ HTTP به کلاینت به کار می‌رود. علت‌هایی که در حال حاضر پشتیبانی می‌شوند عبارت‌اند از: "Unauthorized"، "Forbidden"، "Invalid"، "RequestEntityTooLarge". اگر این فیلد تنظیم نشود، StatusReasonInvalid در پاسخ به کلاینت به کار می‌رود.</td>
    </tr>
  </tbody>
</table>



## عملیات {#Operations}

<hr>


### `post` ایجاد

#### درخواست HTTP

POST /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده (pretty) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ ایجادکنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، طبق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری که رمزگشا (decoder) با آن‌ها روبه‌رو می‌شود، همه به جز آخرین مورد نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطایی که سرور برمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
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
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد (Accepted)</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` وصله‌کردن

#### درخواست HTTP

PATCH /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ ایجادکنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، طبق تعریف https://golang.org/pkg/unicode/#IsPrint. این پارامتر برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه به جز آخرین مورد نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطایی که سرور برمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را به‌صورت «اجباری» اعمال می‌کند. یعنی کاربر مالکیت فیلدهای متعارضی را که به دیگران تعلق دارند دوباره به دست می‌گیرد. برای درخواست‌های patch غیر از apply، پرچم Force باید تنظیم‌نشده بماند.</td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی

#### درخواست HTTP

PUT /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا یک ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ ایجادکنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، طبق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه به جز آخرین مورد نادیده گرفته می‌شوند. این رفتار پیش‌فرض در نسخه‌های پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطایی که سرور برمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف

#### درخواست HTTP

DELETE /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده (pretty-printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار (persist) شوند. هر دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت (grace period) پیش‌فرضِ نوع مشخص‌شده استفاده می‌شود. اگر مشخص نشود، مقدار پیش‌فرضِ مختص هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر برابر true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناامن منبع آغاز می‌شود. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، برای مثال رمزگشایی (decryption) با شکست مواجه می‌شود، یا ب) تبدیل آن به یک آبجکت (decode) با شکست مواجه می‌شود. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاریِ مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از این گزینه استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. این فیلد مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر مقدار آن true/false باشد، finalizer «orphan» به فهرست finalizerهای آبجکت افزوده/از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه جمع‌آوری زباله (garbage collection) انجام شود. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرضِ مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies



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
      <td>گزینهٔ continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز داشته باشد، باید درخواست فهرست را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. در این حالت سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما بر پایهٔ آخرین اسنپ‌شات است و با نتایج فهرست قبلی ناسازگار است؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرطی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. هر دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت پیش‌فرضِ نوع مشخص‌شده استفاده می‌شود. اگر مشخص نشود، مقدار پیش‌فرضِ مختص هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر برابر true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب شکست بخورد، حذف ناامن منبع آغاز می‌شود. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، برای مثال رمزگشایی با شکست مواجه می‌شود، یا ب) تبدیل آن به یک آبجکت با شکست مواجه می‌شود. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاریِ مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از این گزینه استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در متادیتای فهرست با مقداری تنظیم می‌کند که می‌توان از آن همراه با همان کوئری اولیه برای دریافت مجموعهٔ بعدی نتایج استفاده کرد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعدادی کمتر از تعداد درخواستی (حتی صفر مورد) بازگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامهٔ بعدی گنجانده نمی‌شود. به این وضعیت گاهی اسنپ‌شات سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تری از یک نتیجهٔ بسیار بزرگ استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. این فیلد مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم شوند یا نه. اگر مقدار آن true/false باشد، finalizer «orphan» به فهرست finalizerهای آبجکت افزوده/از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه جمع‌آوری زباله انجام شود. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرضِ مختص منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی «Bookmark» ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به‌صورت «داده‌هایی دست‌کم به تازگیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگیِ مقدار ارائه‌شده در ListOptions باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو ریشه‌دار در object به سبک CEL استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون نقل‌قول تکی و با پیشوند '0x' هستند و کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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

GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>

### فهرست کردن با `get`

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies



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
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>فیلد allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که بوکمارک‌ها را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال بوکمارک‌ها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که بوکمارک‌ها در بازه‌ی زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه‌ی continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue به‌دست‌آمده از نتیجه‌ی یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور با فهرستی پاسخ می‌دهد که از کلید بعدی آغاز می‌شود، اما بر پایه‌ی آخرین اسنپ‌شات تهیه شده است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
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
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در متادیتای فهرست به مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه‌ی بعدی نتایج استفاده کرد. اگر همه‌ی آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است تعدادی کمتر از آیتم‌های درخواست‌شده (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجه‌ی صدور یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی «اسنپ‌شات سازگار» (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت یک نتیجه‌ی بسیار بزرگ در تکه‌های کوچک‌تر استفاده می‌کند، همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که مشخص می‌کند درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>گزینه‌ی `sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این بوکمارک، ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه‌ی `sendInitialEvents` تنظیم شده باشد، لازم است گزینه‌ی `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌ای دست‌کم به تازگیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه‌ی هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه‌ی object استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون نقل‌قول تکی و با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ شارد:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicyList" >}}">ValidatingAdmissionPolicyList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` درخواست Watch

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع «BOOKMARK» را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند، و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینهٔ continue را تنظیم کرد. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue یک نتیجهٔ کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی سرور، دیگر معتبر نباشد، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید دریافت فهرست را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر اساس آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض آن همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض آن همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده (metadata) فهرست برابر مقداری قرار می‌دهد که می‌توان با همان کوئری اولیه از آن برای دریافت دستهٔ بعدی نتایج استفاده کرد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواست‌شده (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از ارسال نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تری از یک نتیجهٔ بسیار بزرگ استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین دریافت بخش‌بخش فهرست به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر برابر 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض آن 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که یک درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض آن تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض آن تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را ارائه دهد. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی «Bookmark» ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan به‌صورت «داده‌هایی که دست‌کم به جدیدی `resourceVersion` ارائه‌شده باشند» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی نسخهٔ ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض آن در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت برابر false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (برای مثال "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این پارامتر مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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

### عملیات `get`: پایش فهرست (Watch List)

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی برگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست (session) اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر اساس جدیدترین snapshot تهیه شده و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion برگردانده‌شده از سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>مقدار limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در metadata فهرست با مقداری تنظیم می‌کند که می‌توان از آن همراه با همان پرس‌وجوی اولیه برای بازیابی دسته بعدی نتایج استفاده کرد. اگر همه آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است تعداد آیتم‌هایی کمتر از مقدار درخواست‌شده (تا صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همه نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود.  سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجه یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی snapshot سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشت.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات آبجکت‌های تحت پایش (پس از RV) را ارسال می‌کند.  هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - حالت `resourceVersionMatch` = NotOlderThan به معنای «داده‌ای دست‌کم به تازگیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود.  مقدار پیش‌فرض، در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی)، true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب برای مشخص کردن یک یا چند بازه hash از تابع shardRange() همراه با || (OR منطقی) استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL داخل نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای hash ‏64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال کردن feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار، مدت فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را پایش می‌کند و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف برمی‌گرداند. مقدار resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `patch`: اعمال وصله بر وضعیت (Patch Status)

#### درخواست HTTP

PATCH /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>مقدار fieldManager نامی است که به عامل یا موجودیتِ انجام‌دهنده این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 به بعد است. - Strict: اگر هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری یافت‌شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «اجباری» می‌کند. این یعنی کاربر مالکیت فیلدهای متعارضی را که متعلق به دیگران است دوباره به دست می‌گیرد. برای درخواست‌های patch غیر apply، پرچم Force باید تنظیم‌نشده باقی بماند.</td>
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
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `get`: خواندن وضعیت

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `put`: جایگزینی وضعیت

#### درخواست HTTP

PUT /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingAdmissionPolicy</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>مقدار fieldManager نامی است که به عامل یا موجودیتِ انجام‌دهنده این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای که بی‌صدا از آبجکت حذف می‌شود نادیده گرفته می‌شود و از میان فیلدهای تکراری، همه به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده گرفته می‌شوند. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، یک هشدار از طریق سرآیند استاندارد هشدار در پاسخ ارسال می‌شود. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین آن‌ها ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 به بعد است. - Strict: اگر هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای برگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری یافت‌شده است.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
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
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد (Created)</td>
      <td><em><a href="{{< ref "validating-admission-policy-v1#ValidatingAdmissionPolicy" >}}">ValidatingAdmissionPolicy</a></em></td>
    </tr>
  </tbody>
</table>
