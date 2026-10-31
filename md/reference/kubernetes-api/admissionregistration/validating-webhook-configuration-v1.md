---
api_metadata:
  apiVersion: "admissionregistration.k8s.io/v1"
  import: "k8s.io/api/admissionregistration/v1"
  kind: "ValidatingWebhookConfiguration"
content_type: "api_reference"
description: "آبجکت ValidatingWebhookConfiguration پیکربندی یک وب‌هوک پذیرش را توصیف می‌کند. این وب‌هوک یک آبجکت را بدون تغییر دادن آن می‌پذیرد یا رد می‌کند."
title: "ValidatingWebhookConfiguration"
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

`apiVersion: admissionregistration.k8s.io/v1`

`import "k8s.io/api/admissionregistration/v1"`


## ValidatingWebhookConfiguration {#ValidatingWebhookConfiguration}

آبجکت ValidatingWebhookConfiguration پیکربندی یک وب‌هوک پذیرش (admission webhook) را توصیف می‌کند. این وب‌هوک یک آبجکت را بدون تغییر دادن آن می‌پذیرد یا رد می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌واره‌ی نسخه‌دارِ این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind مقداری رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointی که کلاینت درخواست‌هایش را به آن می‌فرستد استنتاج کنند. این مقدار قابل به‌روزرسانی نیست و به صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فیلد metadata فراداده‌ی استاندارد آبجکت است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.</td>
    </tr>
    <tr>
      <td><code>webhooks</code><br/><em><a href="{{< ref "#ValidatingWebhook" >}}">ValidatingWebhook array</a></em><br/><em>راهبرد patch: ادغام (merge) بر اساس کلید <code>name</code></em></td>
      <td>فیلد webhooks فهرستی از وب‌هوک‌ها به همراه منابع و عملیات‌هایی است که تحت تأثیر آن‌ها قرار می‌گیرند.</td>
    </tr>
  </tbody>
</table>


## ValidatingWebhookConfigurationList {#ValidatingWebhookConfigurationList}

آبجکت ValidatingWebhookConfigurationList فهرستی از ValidatingWebhookConfigurationهاست.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌واره‌ی نسخه‌دارِ این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration array</a></em></td>
      <td>فهرستی از ValidatingWebhookConfigurationها.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind مقداری رشته‌ای است که منبع REST متناظر با این آبجکت را نشان می‌دهد. سرورها ممکن است این مقدار را از endpointی که کلاینت درخواست‌هایش را به آن می‌فرستد استنتاج کنند. این مقدار قابل به‌روزرسانی نیست و به صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فیلد metadata فراداده‌ی استاندارد فهرست است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## ValidatingWebhook {#ValidatingWebhook}

آبجکت ValidatingWebhook یک وب‌هوک پذیرش و منابع و عملیات‌هایی را که این وب‌هوک بر آن‌ها اعمال می‌شود توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>admissionReviewVersions</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>فیلد admissionReviewVersions فهرستی مرتب از نسخه‌های ترجیحی `AdmissionReview` است که وب‌هوک انتظار دارد. سرور API تلاش می‌کند نخستین نسخه‌ای از این فهرست را که پشتیبانی می‌کند به کار ببرد. اگر سرور API از هیچ‌یک از نسخه‌های مشخص‌شده در این فهرست پشتیبانی نکند، اعتبارسنجی این آبجکت ناموفق خواهد بود. اگر یک پیکربندی وب‌هوکِ ذخیره‌شده نسخه‌های مجاز را مشخص کند و هیچ‌یک از نسخه‌های شناخته‌شده برای سرور API را در بر نگیرد، فراخوانی‌های این وب‌هوک با شکست مواجه می‌شوند و تابع سیاست خطا (failure policy) خواهند بود.</td>
    </tr>
    <tr>
      <td><code>clientConfig</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "../apiextensions/custom-resource-definition-v1#WebhookClientConfig" >}}">WebhookClientConfig</a></em></td>
      <td>فیلد clientConfig نحوه‌ی ارتباط با هوک را تعریف می‌کند. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>failurePolicy</code><br/><em>string</em></td>
      <td>فیلد failurePolicy تعیین می‌کند خطاهای ناشناخته‌ای که از endpoint پذیرش بازگردانده می‌شوند چگونه مدیریت شوند؛ مقادیر مجاز Ignore و Fail هستند. مقدار پیش‌فرض Fail است.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"Fail"` یعنی بروز خطا در فراخوانی وب‌هوک باعث شکست پذیرش می‌شود.<br/> - مقدار `"Ignore"` یعنی خطای فراخوانی وب‌هوک نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>matchConditions</code><br/><em><a href="{{< ref "../definitions/match-condition-v1-admissionregistration#MatchCondition" >}}">MatchCondition array</a></em><br/><em>راهبرد patch: ادغام (merge) بر اساس کلید <code>name</code></em></td>
      <td>فیلد matchConditions فهرستی از شرط‌هایی است که برای ارسال یک درخواست به این وب‌هوک باید برقرار باشند. شرط‌های تطبیق، درخواست‌هایی را فیلتر می‌کنند که پیش‌تر با rules، namespaceSelector و objectSelector تطبیق داده شده‌اند. فهرست خالی matchConditions با همه‌ی درخواست‌ها تطبیق پیدا می‌کند. حداکثر ۶۴ شرط تطبیق مجاز است.  منطق دقیق تطبیق (به ترتیب) چنین است:   ۱. اگر ارزیابی «هر یک» از matchConditionها FALSE باشد، از وب‌هوک صرف‌نظر می‌شود.   ۲. اگر ارزیابی «همه‌ی» matchConditionها TRUE باشد، وب‌هوک فراخوانی می‌شود.   ۳. اگر ارزیابی یکی از matchConditionها به خطا بینجامد (اما هیچ‌کدام FALSE نباشد):      - اگر failurePolicy=Fail باشد، درخواست رد می‌شود      - اگر failurePolicy=Ignore باشد، خطا نادیده گرفته می‌شود و از وب‌هوک صرف‌نظر می‌شود</td>
    </tr>
    <tr>
      <td><code>matchPolicy</code><br/><em>string</em></td>
      <td>فیلد matchPolicy تعیین می‌کند فهرست "rules" چگونه برای تطبیق درخواست‌های ورودی به کار رود. مقادیر مجاز "Exact" و "Equivalent" هستند.  - Exact: درخواست فقط در صورتی تطبیق داده می‌شود که دقیقاً با یکی از قواعد مشخص‌شده منطبق باشد. برای مثال، اگر deploymentها از طریق apps/v1، apps/v1beta1 و extensions/v1beta1 قابل تغییر باشند، اما "rules" فقط شامل `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]` باشد، درخواستی که به apps/v1beta1 یا extensions/v1beta1 ارسال شود به وب‌هوک فرستاده نمی‌شود.  - Equivalent: درخواست در صورتی تطبیق داده می‌شود که منبعی را که در rules فهرست شده است تغییر دهد، حتی اگر این کار از طریق گروه یا نسخه‌ی دیگری از API انجام شود. برای مثال، اگر deploymentها از طریق apps/v1، apps/v1beta1 و extensions/v1beta1 قابل تغییر باشند و "rules" فقط شامل `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]` باشد، درخواستی که به apps/v1beta1 یا extensions/v1beta1 ارسال شود به apps/v1 تبدیل و سپس به وب‌هوک فرستاده می‌شود.  مقدار پیش‌فرض "Equivalent" است.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"Equivalent"` یعنی اگر درخواست‌ها منبعی را که در rules فهرست شده است از طریق گروه یا نسخه‌ی دیگری از API تغییر دهند، باید به وب‌هوک فرستاده شوند.<br/> - مقدار `"Exact"` یعنی درخواست‌ها فقط در صورتی باید به وب‌هوک فرستاده شوند که دقیقاً با یک قاعده‌ی مشخص منطبق باشند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام وب‌هوک پذیرش است. این نام باید کاملاً واجد شرایط (fully qualified) باشد؛ برای مثال imagepolicy.kubernetes.io که در آن "imagepolicy" نام وب‌هوک و kubernetes.io نام سازمان است. این فیلد الزامی است.</td>
    </tr>
    <tr>
      <td><code>namespaceSelector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>فیلد namespaceSelector بر اساس اینکه فضای نام (namespace) یک آبجکت با انتخابگر (selector) تطبیق دارد یا نه، تعیین می‌کند که وب‌هوک روی آن آبجکت اجرا شود یا خیر. اگر خود آبجکت یک فضای نام باشد، تطبیق روی object.metadata.labels انجام می‌شود. اگر آبجکت منبع دیگری با دامنه‌ی کلاستر باشد، هرگز از وب‌هوک صرف‌نظر نمی‌شود.  برای مثال، برای اجرای وب‌هوک روی هر آبجکتی که فضای نام آن به "runlevel" با مقدار "0" یا "1" مرتبط نیست، انتخابگر را به این صورت تنظیم می‌کنید: "namespaceSelector": {   "matchExpressions": [     {       "key": "runlevel",       "operator": "NotIn",       "values": [         "0",         "1"       ]     }   ] }  اما اگر بخواهید وب‌هوک فقط روی آبجکت‌هایی اجرا شود که فضای نامشان به "environment" با مقدار "prod" یا "staging" مرتبط است، انتخابگر را به این صورت تنظیم می‌کنید: "namespaceSelector": {   "matchExpressions": [     {       "key": "environment",       "operator": "In",       "values": [         "prod",         "staging"       ]     }   ] }  برای مشاهده‌ی نمونه‌های بیشتری از انتخابگرهای برچسب، به https://kubernetes.io/docs/concepts/overview/working-with-objects/labels مراجعه کنید.  مقدار پیش‌فرض، یک LabelSelector خالی است که با همه چیز تطبیق پیدا می‌کند.</td>
    </tr>
    <tr>
      <td><code>objectSelector</code><br/><em><a href="{{< ref "../definitions/label-selector-v1-meta#LabelSelector" >}}">LabelSelector</a></em></td>
      <td>فیلد objectSelector بر اساس اینکه آبجکت برچسب‌های منطبق دارد یا نه، تعیین می‌کند که وب‌هوک اجرا شود یا خیر. این فیلد هم روی oldObject و هم روی newObject که قرار است به وب‌هوک ارسال شوند ارزیابی می‌شود و اگر هر یک از این دو آبجکت با انتخابگر منطبق باشد، تطبیق برقرار تلقی می‌شود. آبجکت null (یعنی oldObject در عملیات ایجاد یا newObject در عملیات حذف) یا آبجکتی که نمی‌تواند برچسب داشته باشد (مانند آبجکت DeploymentRollback یا PodProxyOptions) منطبق در نظر گرفته نمی‌شود. از انتخابگر آبجکت فقط زمانی استفاده کنید که وب‌هوک اختیاری (opt-in) باشد، زیرا کاربران نهایی می‌توانند با تنظیم برچسب‌ها از وب‌هوک پذیرش عبور کنند. مقدار پیش‌فرض، یک LabelSelector خالی است که با همه چیز تطبیق پیدا می‌کند.</td>
    </tr>
    <tr>
      <td><code>rules</code><br/><em><a href="{{< ref "../definitions/rule-with-operations-v1-admissionregistration#RuleWithOperations" >}}">RuleWithOperations array</a></em></td>
      <td>فیلد rules مشخص می‌کند که وب‌هوک به کدام عملیات‌ها روی کدام منابع یا زیرمنابع اهمیت می‌دهد. وب‌هوک به عملیاتی اهمیت می‌دهد که با _هر یک_ از قواعد (Rule) منطبق باشد. با این حال، برای جلوگیری از اینکه ValidatingAdmissionWebhookها و MutatingAdmissionWebhookها کلاستر را در وضعیتی قرار دهند که بازیابی از آن بدون غیرفعال‌سازی کامل افزونه ممکن نباشد، این وب‌هوک‌ها هرگز برای درخواست‌های پذیرشِ مربوط به آبجکت‌های ValidatingWebhookConfiguration و MutatingWebhookConfiguration فراخوانی نمی‌شوند.</td>
    </tr>
    <tr>
      <td><code>sideEffects</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد sideEffects مشخص می‌کند که آیا این وب‌هوک اثر جانبی دارد یا نه. مقادیر قابل قبول None و NoneOnDryRun هستند (وب‌هوک‌هایی که از طریق v1beta1 ایجاد شده‌اند ممکن است Some یا Unknown را نیز مشخص کنند). وب‌هوک‌هایی که اثر جانبی دارند «باید» یک سازوکار همسان‌سازی (reconciliation) پیاده‌سازی کنند، زیرا ممکن است درخواست در مرحله‌ای بعدی از زنجیره‌ی پذیرش رد شود و در نتیجه لازم باشد اثرات جانبی آن بازگردانده شوند. درخواست‌هایی که ویژگی dryRun دارند، اگر با وب‌هوکی با sideEffects == Unknown یا Some منطبق شوند، به‌طور خودکار رد می‌شوند.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"None"` یعنی فراخوانی وب‌هوک هیچ اثر جانبی ندارد.<br/> - مقدار `"NoneOnDryRun"` یعنی فراخوانی وب‌هوک ممکن است اثر جانبی داشته باشد، اما اگر درخواستِ در حال بررسی ویژگی dry-run داشته باشد، اثرات جانبی سرکوب می‌شوند.<br/> - مقدار `"Some"` یعنی فراخوانی وب‌هوک ممکن است اثر جانبی داشته باشد. اگر درخواستی با ویژگی dry-run موجب فراخوانی این وب‌هوک شود، آن درخواست در عوض با شکست مواجه می‌شود.<br/> - مقدار `"Unknown"` یعنی هیچ اطلاعاتی درباره‌ی اثرات جانبی فراخوانی وب‌هوک در دست نیست. اگر درخواستی با ویژگی dry-run موجب فراخوانی این وب‌هوک شود، آن درخواست در عوض با شکست مواجه می‌شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code><br/><em>integer</em></td>
      <td>فیلد timeoutSeconds مهلت زمانی (timeout) این وب‌هوک را مشخص می‌کند. پس از سپری شدن این مهلت، بسته به سیاست خطا، فراخوانی وب‌هوک نادیده گرفته می‌شود یا فراخوانی API با شکست مواجه می‌شود. مقدار مهلت زمانی باید بین ۱ تا ۳۰ ثانیه باشد. مقدار پیش‌فرض ۱۰ ثانیه است.</td>
    </tr>
  </tbody>
</table>



## عملیات {#Operations}

<hr>


### `post` ایجاد

#### درخواست HTTP

POST /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به شکل خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ذخیره شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه پیدا نمی‌کند. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ ایجادکننده‌ی این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: همه‌ی فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه‌ی v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد پاسخ هشدار، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه‌ی v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطایی که سرور بازمی‌گرداند شامل همه‌ی فیلدهای ناشناخته و تکراریِ یافت‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
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
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
  </tbody>
</table>

### `patch` اعمال وصله

#### درخواست HTTP

PATCH /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingWebhookConfiguration</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty-print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به بازگشت پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات مربوط می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: همهٔ فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که کدگشا (decoder) با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همهٔ فیلدهای ناشناخته و تکراری یافت‌شده را در بر خواهد داشت.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «اجباری» می‌کند؛ یعنی کاربر مالکیت فیلدهای دارای تعارض را که متعلق به دیگران هستند دوباره به دست می‌گیرد. برای درخواست‌های patch غیر apply، پرچم Force نباید تنظیم شود.</td>
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
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی

#### درخواست HTTP

PUT /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingWebhookConfiguration</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به بازگشت پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldManager نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات مربوط می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>فیلد fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: همهٔ فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که کدگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطای بازگشتی از سرور همهٔ فیلدهای ناشناخته و تکراری یافت‌شده را در بر خواهد داشت.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
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
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجاد شد</td>
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` حذف

#### درخواست HTTP

DELETE /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingWebhookConfiguration</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به بازگشت پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمانی برحسب ثانیه که پیش از حذف آبجکت باید سپری شود. مقدار آن باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت (grace period) پیش‌فرضِ نوع مشخص‌شده استفاده می‌شود. اگر مقداری مشخص نشود، مقدار پیش‌فرضِ هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر مقدار آن true باشد، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) ناموفق شود، حذف ناامن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، برای مثال به دلیل شکست در رمزگشایی، یا ب) کدگشایی آن به آبجکت ناموفق است. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، از بررسی‌های پیش‌شرط صرف‌نظر می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر مقدار آن true یا false باشد، finalizer «orphan» به‌ترتیب به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و به چه صورت. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرضِ مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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
      <td>موفق</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>پذیرفته شد</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations



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
      <td>گزینهٔ continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست list دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت، سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر اساس آخرین تصویر لحظه‌ای (snapshot) تهیه شده و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست list ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، مشخص می‌کند که تغییرات نباید ماندگار شوند. هر دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمانی بر حسب ثانیه که باید پیش از حذف آبجکت سپری شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص‌نشدن، مقدار پیش‌فرض مختص هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب شکست بخورد، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، مثلاً به علت شکست در رمزگشایی، یا ب) رمزگشایی آن به یک آبجکت با شکست مواجه می‌شود. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر برای فعال‌سازی آن باید صراحتاً آن را انتخاب کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی را تعیین می‌کند که یک فراخوانی list بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در متادیتای فهرست روی مقداری تنظیم می‌کند که می‌توان از آن همراه با همان کوئری اولیه برای بازیابی دستهٔ بعدی نتایج استفاده کرد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواست‌شده (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی تصویر لحظه‌ای سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجهٔ بسیار بزرگ استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری بخش‌بخش به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true/false باشد، finalizer با نام «orphan» به فهرست finalizerهای آبجکت افزوده/از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا و چگونه جمع‌آوری زباله (garbage collection) انجام شود. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض، تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود برای فراخوانی‌های listی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض، تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی «Bookmark» ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به‌صورت «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون نقل‌قول تکی با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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

GET /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingWebhookConfiguration</td>
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
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfiguration" >}}">ValidatingWebhookConfiguration</a></em></td>
    </tr>
  </tbody>
</table>

### دریافت فهرست با `get`

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت مرتب و خوانا (pretty-printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌ی زمانی مشخصی بازگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه‌ی continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه‌ی یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر اساس آخرین snapshot تهیه شده و با نتایج فهرست قبلی سازگار نیست: آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» (next key) باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سوی سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) است که فهرست آبجکت‌های بازگردانده‌شده را بر اساس فیلدهایشان محدود می‌کند. به‌طور پیش‌فرض همه‌ی آبجکت‌ها بازگردانده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری است که فهرست آبجکت‌های بازگردانده‌شده را بر اساس برچسب‌هایشان محدود می‌کند. به‌طور پیش‌فرض همه‌ی آبجکت‌ها بازگردانده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در metadata فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت دسته‌ی بعدی نتایج به کار برد. اگر همه‌ی آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است تعداد کمتری از موارد درخواستی (حتی صفر مورد) را برگرداند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همه‌ی نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه‌ی دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود.  سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجه‌ی یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این وضعیت گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت یک نتیجه‌ی بسیار بزرگ در قطعه‌های کوچک‌تر استفاده می‌کند، همه‌ی آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین دریافت قطعه‌قطعه‌ی فهرست به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبه‌ی نخستین نتیجه‌ی فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی بر نسخه‌های منبعی که درخواست می‌تواند از آن‌ها پاسخ داده شود اعمال می‌کند. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه روی فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازسازی کند. پس از ارسال همه‌ی این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه‌ی آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظارت را ارسال می‌کند.  وقتی گزینه‌ی `sendInitialEvents` تنظیم شده باشد، لازم است گزینه‌ی `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` برابر NotOlderThan باشد، به‌صورت «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ی آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد، مقدار پیش‌فرض true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با عملگر || (OR منطقی) برای مشخص کردن یک یا چند بازه‌ی هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه‌ی object (مانند "object.metadata.uid") استفاده می‌کنند، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون علامت نقل‌قول تکی و با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را در فضای هش ۶۴بیتی FNV-1a تعریف می‌کنند. بازه‌ی کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch است. این مقدار، صرف‌نظر از وجود یا نبود فعالیت، مدت فراخوانی را محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "validating-webhook-configuration-v1#ValidatingWebhookConfigurationList" >}}">ValidatingWebhookConfigurationList</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `get` برای Watch

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام ValidatingWebhookConfiguration</td>
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
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmarkها را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به تشخیص سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند، و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور، باید گزینهٔ continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) را به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید دریافت فهرست را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر پایهٔ آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند تا هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض آن همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض آن همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit بیشترین تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست با مقداری پر می‌کند که می‌توان آن را همراه همان پرس‌وجوی اولیه برای دریافت دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تعیین limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواست‌شده (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را برمی‌گردانند. اگر limit مشخص شده و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این حالت گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در بخش‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین دریافت بخش‌بخش فهرست به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به شکل خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که یک درخواست می‌تواند از کدام نسخه‌های منبع پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض آن تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض آن تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار NotOlderThan برای `resourceVersionMatch` به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت برابر false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (برای مثال "object.metadata.uid")، و نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون تک‌نقل‌قول با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحلهٔ آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار، مدت فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
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

### عملیات `get` برای Watch List

#### درخواست HTTP

GET /apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی بازگردانده می‌شوند، و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست هیچ رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام بازیابی نتایج بیشتر از سرور باید گزینهٔ continue را تنظیم کرد. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی آغاز می‌شود، اما بر پایهٔ آخرین snapshot است که با نتایج فهرست قبلی ناسازگار است؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، در صورتی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده از سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
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
      <td>پارامتر limit بیشینهٔ تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی مجموعهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است تعدادی کمتر از آیتم‌های درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. وقتی watch برابر true باشد، این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، ویرایش یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجهٔ بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان‌دهندهٔ یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بسازد. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - مقدار NotOlderThan برای `resourceVersionMatch` به معنای «داده‌ای دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به تازگی نسخهٔ ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌عنوان «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) برابر true و در غیر این صورت برابر false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() به همراه || (یای منطقی) برای تعیین یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول با پیشوند '0x' هستند که کران پایین شامل و کران بالای غیرشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این پارامتر مدت‌زمان فراخوانی را، صرف‌نظر از وجود یا نبود فعالیت، محدود می‌کند.</td>
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
