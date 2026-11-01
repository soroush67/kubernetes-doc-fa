---
api_metadata:
  apiVersion: "apiextensions.k8s.io/v1"
  import: "k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1"
  kind: "CustomResourceDefinition"
content_type: "api_reference"
description: "آبجکت CustomResourceDefinition منبعی را نشان می‌دهد که باید روی سرور API در دسترس قرار گیرد. نام آن باید حتماً در قالب &lt;.spec.name&gt;.&lt;.spec.group&gt; باشد."
title: "CustomResourceDefinition"
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

`apiVersion: apiextensions.k8s.io/v1`

`import "k8s.io/apiextensions-apiserver/pkg/apis/apiextensions/v1"`


## CustomResourceDefinition {#CustomResourceDefinition}

آبجکت CustomResourceDefinition منبعی را نشان می‌دهد که باید روی سرور API در دسترس قرار گیرد. نام آن باید حتماً در قالب &lt;.spec.name&gt;.&lt;.spec.group&gt; باشد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ (schema) نسخه‌دارِ این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را مشخص می‌کند. سرورها ممکن است این مقدار را از نقطهٔ پایانی (endpoint) که کلاینت درخواست‌هایش را به آن ارسال می‌کند، استنتاج کنند. این فیلد قابل به‌روزرسانی نیست و به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فرادادهٔ استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#CustomResourceDefinitionSpec" >}}">CustomResourceDefinitionSpec</a></em></td>
      <td>فیلد spec توصیف می‌کند که کاربر می‌خواهد منابع چگونه نمایش داده شوند.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#CustomResourceDefinitionStatus" >}}">CustomResourceDefinitionStatus</a></em></td>
      <td>فیلد status وضعیت واقعی CustomResourceDefinition را نشان می‌دهد.</td>
    </tr>
  </tbody>
</table>


## CustomResourceDefinitionSpec {#CustomResourceDefinitionSpec}

آبجکت CustomResourceDefinitionSpec توصیف می‌کند که کاربر می‌خواهد منبعش چگونه نمایش داده شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>conversion</code><br/><em><a href="{{< ref "#CustomResourceConversion" >}}">CustomResourceConversion</a></em></td>
      <td>فیلد conversion تنظیمات تبدیل را برای CRD تعریف می‌کند.</td>
    </tr>
    <tr>
      <td><code>group</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد group گروه API منبع سفارشی (custom resource) تعریف‌شده است. منابع سفارشی در مسیر `/apis/\<group>/...` ارائه می‌شوند. مقدار آن باید با نام CustomResourceDefinition (در قالب `\<names.plural>.\<group>`) مطابقت داشته باشد.</td>
    </tr>
    <tr>
      <td><code>names</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#CustomResourceDefinitionNames" >}}">CustomResourceDefinitionNames</a></em></td>
      <td>فیلد names نام منبع و نام نوع (kind) را برای منبع سفارشی مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>preserveUnknownFields</code><br/><em>boolean</em></td>
      <td>فیلد preserveUnknownFields نشان می‌دهد که فیلدهایی از آبجکت که در طرح‌وارهٔ OpenAPI مشخص نشده‌اند، باید هنگام ذخیرهٔ ماندگار در ذخیره‌سازی حفظ شوند. فیلدهای apiVersion، kind و metadata و نیز فیلدهای شناخته‌شدهٔ درون metadata همیشه حفظ می‌شوند. این فیلد منسوخ شده است و به‌جای آن باید `x-preserve-unknown-fields` را در `spec.versions[*].schema.openAPIV3Schema` برابر با true قرار داد. برای جزئیات، به https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#field-pruning مراجعه کنید.</td>
    </tr>
    <tr>
      <td><code>scope</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد scope نشان می‌دهد که دامنهٔ منبع سفارشی تعریف‌شده در سطح کلاستر است یا در سطح فضای نام (namespace). مقادیر مجاز `Cluster` و `Namespaced` هستند.</td>
    </tr>
    <tr>
      <td><code>versions</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "#CustomResourceDefinitionVersion" >}}">CustomResourceDefinitionVersion array</a></em></td>
      <td>فیلد versions فهرست همهٔ نسخه‌های API منبع سفارشی تعریف‌شده است. از نام نسخه‌ها برای محاسبهٔ ترتیب فهرست‌شدن نسخه‌های ارائه‌شده در کشف API (API discovery) استفاده می‌شود. اگر رشتهٔ نسخه «شبیه کوبرنتیز» (kube-like) باشد، بالاتر از رشته‌های نسخهٔ غیر kube-like قرار می‌گیرد؛ این رشته‌ها به ترتیب الفبایی (lexicographic) مرتب می‌شوند. نسخه‌های kube-like با حرف «v» آغاز می‌شوند، سپس یک عدد (نسخهٔ اصلی) می‌آید و پس از آن، به‌صورت اختیاری، رشتهٔ «alpha» یا «beta» و عددی دیگر (نسخهٔ فرعی) قرار می‌گیرد. این نسخه‌ها ابتدا بر اساس GA > beta > alpha (که در آن GA نسخه‌ای بدون پسوندی مانند beta یا alpha است) و سپس با مقایسهٔ نسخهٔ اصلی و پس از آن نسخهٔ فرعی مرتب می‌شوند. نمونه‌ای از یک فهرست مرتب‌شده از نسخه‌ها: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.</td>
    </tr>
  </tbody>
</table>


## CustomResourceDefinitionStatus {#CustomResourceDefinitionStatus}

آبجکت CustomResourceDefinitionStatus وضعیت CustomResourceDefinition را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>acceptedNames</code><br/><em><a href="{{< ref "#CustomResourceDefinitionNames" >}}">CustomResourceDefinitionNames</a></em></td>
      <td>فیلد acceptedNames شامل نام‌هایی است که در عمل برای ارائهٔ کشف (discovery) استفاده می‌شوند. این نام‌ها ممکن است با نام‌های موجود در spec متفاوت باشند.</td>
    </tr>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#CustomResourceDefinitionCondition" >}}">CustomResourceDefinitionCondition array</a></em></td>
      <td>فیلد conditions وضعیت جنبه‌های خاصی از یک CustomResourceDefinition را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>نسلی (generation) که کنترل‌کنندهٔ CRD مشاهده کرده است.</td>
    </tr>
    <tr>
      <td><code>storedVersions</code><br/><em>string array</em></td>
      <td>فیلد storedVersions همهٔ نسخه‌هایی از CustomResourceها را که تاکنون ذخیره شده‌اند فهرست می‌کند. ردیابی این نسخه‌ها مسیری برای مهاجرت نسخه‌های ذخیره‌شده در etcd فراهم می‌کند. این فیلد تغییرپذیر است تا یک کنترل‌کنندهٔ مهاجرت بتواند مهاجرت به نسخه‌ای دیگر را به پایان برساند (و اطمینان یابد که هیچ آبجکت قدیمی‌ای در ذخیره‌سازی باقی نمانده است) و سپس بقیهٔ نسخه‌ها را از این فهرست حذف کند. تا زمانی که نسخه‌ای در این فهرست وجود دارد، نمی‌توان آن را از `spec.versions` حذف کرد.</td>
    </tr>
  </tbody>
</table>


## CustomResourceDefinitionList {#CustomResourceDefinitionList}

آبجکت CustomResourceDefinitionList فهرستی از آبجکت‌های CustomResourceDefinition است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>فیلد APIVersion طرح‌وارهٔ نسخه‌دارِ این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و ممکن است مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition array</a></em></td>
      <td>فیلد items آبجکت‌های CustomResourceDefinition را به‌صورت جداگانه فهرست می‌کند.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>فیلد Kind یک مقدار رشته‌ای است که منبع REST متناظر با این آبجکت را مشخص می‌کند. سرورها ممکن است این مقدار را از نقطهٔ پایانی‌ای که کلاینت درخواست‌هایش را به آن ارسال می‌کند، استنتاج کنند. این فیلد قابل به‌روزرسانی نیست و به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فرادادهٔ استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
  </tbody>
</table>


## CustomResourceColumnDefinition {#CustomResourceColumnDefinition}

آبجکت CustomResourceColumnDefinition یک ستون را برای چاپ سمت سرور (server side printing) مشخص می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>description</code><br/><em>string</em></td>
      <td>فیلد description توصیفی خوانا برای انسان از این ستون است.</td>
    </tr>
    <tr>
      <td><code>format</code><br/><em>string</em></td>
      <td>فیلد format یک تعریف نوع اختیاری OpenAPI برای این ستون است. قالب 'name' روی ستون شناسهٔ اصلی اعمال می‌شود تا به کلاینت‌ها کمک کند تشخیص دهند که این ستون، نام منبع است. برای جزئیات، به https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types مراجعه کنید.</td>
    </tr>
    <tr>
      <td><code>jsonPath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد jsonPath یک مسیر سادهٔ JSON (یعنی با نشانه‌گذاری آرایه) است که روی هر منبع سفارشی ارزیابی می‌شود تا مقدار این ستون را تولید کند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نامی خوانا برای انسان برای این ستون است.</td>
    </tr>
    <tr>
      <td><code>priority</code><br/><em>integer</em></td>
      <td>فیلد priority عددی صحیح است که اهمیت نسبی این ستون را در مقایسه با ستون‌های دیگر تعریف می‌کند. اعداد کوچک‌تر اولویت بالاتری دارند. به ستون‌هایی که ممکن است در شرایط کمبود فضا حذف شوند، باید اولویتی بزرگ‌تر از ۰ داده شود.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type تعریف نوع OpenAPI برای این ستون است. برای جزئیات، به https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types مراجعه کنید.</td>
    </tr>
  </tbody>
</table>


## CustomResourceConversion {#CustomResourceConversion}

آبجکت CustomResourceConversion توصیف می‌کند که نسخه‌های مختلف یک CR چگونه به یکدیگر تبدیل می‌شوند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>strategy</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد strategy مشخص می‌کند که منابع سفارشی چگونه بین نسخه‌ها تبدیل می‌شوند. مقادیر مجاز عبارت‌اند از:<br/> - مقدار `"None"`: مبدل فقط apiVersion را تغییر می‌دهد و به هیچ فیلد دیگری در منبع سفارشی دست نمی‌زند.<br/> - مقدار `"Webhook"`: سرور API برای انجام تبدیل، یک وب‌هوک خارجی را فراخوانی می‌کند. این گزینه به اطلاعات بیشتری نیاز دارد. برای استفاده از آن، spec.preserveUnknownFields باید false باشد و spec.conversion.webhook تنظیم شده باشد.</td>
    </tr>
    <tr>
      <td><code>webhook</code><br/><em><a href="{{< ref "#WebhookConversion" >}}">WebhookConversion</a></em></td>
      <td>فیلد webhook نحوهٔ فراخوانی وب‌هوک تبدیل را توصیف می‌کند. وقتی `strategy` برابر با `"Webhook"` باشد، این فیلد الزامی است.</td>
    </tr>
  </tbody>
</table>


## CustomResourceDefinitionCondition {#CustomResourceDefinitionCondition}

آبجکت CustomResourceDefinitionCondition جزئیات وضعیت (condition) فعلی این پاد را در بر دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>فیلد lastTransitionTime آخرین زمانی است که شرط از یک وضعیت به وضعیت دیگر تغییر کرده است.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>فیلد message پیامی خوانا برای انسان است که جزئیات آخرین تغییر را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>observedGeneration</code><br/><em>integer</em></td>
      <td>فیلد observedGeneration مقدار ‎.metadata.generation را نشان می‌دهد که شرط بر اساس آن تنظیم شده است. برای مثال، اگر ‎.metadata.generation در حال حاضر ۱۲ باشد ولی ‎.status.conditions[x].observedGeneration برابر با ۹ باشد، شرط نسبت به وضعیت فعلی نمونه به‌روز نیست.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>فیلد reason دلیلی یکتا، تک‌کلمه‌ای و به‌صورت CamelCase برای آخرین تغییر شرط است.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد status وضعیت شرط است. مقدار آن می‌تواند True، False یا Unknown باشد.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد type نوع شرط است. انواع آن عبارت‌اند از Established، NamesAccepted و Terminating.</td>
    </tr>
  </tbody>
</table>


## CustomResourceDefinitionNames {#CustomResourceDefinitionNames}

آبجکت CustomResourceDefinitionNames نام‌هایی را مشخص می‌کند که این CustomResourceDefinition با آن‌ها ارائه می‌شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>categories</code><br/><em>string array</em></td>
      <td>فیلد categories فهرستی از منابع گروه‌بندی‌شده است که این منبع سفارشی به آن‌ها تعلق دارد (مثلاً 'all'). این مقدار در اسناد کشف API منتشر می‌شود و کلاینت‌ها از آن برای پشتیبانی از فراخوانی‌هایی مانند `kubectl get all` استفاده می‌کنند.</td>
    </tr>
    <tr>
      <td><code>kind</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد kind نوع سریال‌شدهٔ منبع است. این مقدار معمولاً به‌صورت CamelCase و مفرد است. نمونه‌های منبع سفارشی از این مقدار به‌عنوان ویژگی `kind` در فراخوانی‌های API استفاده می‌کنند.</td>
    </tr>
    <tr>
      <td><code>listKind</code><br/><em>string</em></td>
      <td>فیلد listKind نوع سریال‌شدهٔ فهرست برای این منبع است. مقدار پیش‌فرض آن "`kind`List" است.</td>
    </tr>
    <tr>
      <td><code>plural</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد plural نام جمع منبعی است که ارائه می‌شود. منابع سفارشی در مسیر `/apis/\<group>/\<version>/.../\<plural>` ارائه می‌شوند. مقدار آن باید با نام CustomResourceDefinition (در قالب `\<names.plural>.\<group>`) مطابقت داشته باشد و همهٔ حروف آن باید کوچک باشند.</td>
    </tr>
    <tr>
      <td><code>shortNames</code><br/><em>string array</em></td>
      <td>فیلد shortNames نام‌های کوتاه منبع است که در اسناد کشف API در دسترس قرار می‌گیرند و کلاینت‌ها از آن‌ها برای پشتیبانی از فراخوانی‌هایی مانند `kubectl get \<shortname>` استفاده می‌کنند. همهٔ حروف آن‌ها باید کوچک باشند.</td>
    </tr>
    <tr>
      <td><code>singular</code><br/><em>string</em></td>
      <td>فیلد singular نام مفرد منبع است. همهٔ حروف آن باید کوچک باشند. مقدار پیش‌فرض آن، `kind` با حروف کوچک است.</td>
    </tr>
  </tbody>
</table>


## CustomResourceDefinitionVersion {#CustomResourceDefinitionVersion}

آبجکت CustomResourceDefinitionVersion یک نسخه از CRD را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>additionalPrinterColumns</code><br/><em><a href="{{< ref "#CustomResourceColumnDefinition" >}}">CustomResourceColumnDefinition array</a></em></td>
      <td>فیلد additionalPrinterColumns ستون‌های اضافی‌ای را مشخص می‌کند که در خروجی Table برگردانده می‌شوند. برای جزئیات، به https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables مراجعه کنید. اگر هیچ ستونی مشخص نشود، یک ستون واحد استفاده می‌شود که سن منبع سفارشی را نمایش می‌دهد.</td>
    </tr>
    <tr>
      <td><code>deprecated</code><br/><em>boolean</em></td>
      <td>فیلد deprecated نشان می‌دهد که این نسخه از API منبع سفارشی منسوخ شده است. اگر مقدار آن true باشد، درخواست‌های API به این نسخه در پاسخ سرور یک سرآیند هشدار دریافت می‌کنند. مقدار پیش‌فرض false است.</td>
    </tr>
    <tr>
      <td><code>deprecationWarning</code><br/><em>string</em></td>
      <td>فیلد deprecationWarning هشدار پیش‌فرضی را که به کلاینت‌های API برگردانده می‌شود، جایگزین می‌کند. فقط زمانی می‌توان آن را تنظیم کرد که `deprecated` برابر با true باشد. هشدار پیش‌فرض اعلام می‌کند که این نسخه منسوخ شده است و در صورت وجود، استفاده از جدیدترین نسخهٔ ارائه‌شده با پایداری برابر یا بیشتر را توصیه می‌کند.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام نسخه است، مثلاً «v1»، «v2beta1» و غیره. اگر `served` برابر با true باشد، منابع سفارشی تحت این نسخه در مسیر `/apis/\<group>/\<version>/...` ارائه می‌شوند.</td>
    </tr>
    <tr>
      <td><code>schema</code><br/><em><a href="{{< ref "#CustomResourceValidation" >}}">CustomResourceValidation</a></em></td>
      <td>فیلد schema طرح‌واره‌ای را توصیف می‌کند که برای اعتبارسنجی، هرس (pruning) و مقداردهی پیش‌فرض این نسخه از منبع سفارشی استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>selectableFields</code><br/><em><a href="{{< ref "#SelectableField" >}}">SelectableField array</a></em></td>
      <td>فیلد selectableFields مسیرهای فیلدهایی را مشخص می‌کند که می‌توان از آن‌ها به‌عنوان انتخابگر فیلد (field selector) استفاده کرد. حداکثر ۸ فیلد قابل انتخاب مجاز است. به https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors مراجعه کنید.</td>
    </tr>
    <tr>
      <td><code>served</code>&nbsp;<strong>*</strong><br/><em>boolean</em></td>
      <td>فیلد served پرچمی است که ارائهٔ این نسخه از طریق REST APIها را فعال یا غیرفعال می‌کند.</td>
    </tr>
    <tr>
      <td><code>storage</code>&nbsp;<strong>*</strong><br/><em>boolean</em></td>
      <td>فیلد storage نشان می‌دهد که هنگام ذخیرهٔ ماندگار منابع سفارشی در ذخیره‌سازی باید از این نسخه استفاده شود. باید دقیقاً یک نسخه با storage=true وجود داشته باشد.</td>
    </tr>
    <tr>
      <td><code>subresources</code><br/><em><a href="{{< ref "#CustomResourceSubresources" >}}">CustomResourceSubresources</a></em></td>
      <td>فیلد subresources مشخص می‌کند که این نسخه از منبع سفارشی تعریف‌شده چه زیرمنابعی دارد.</td>
    </tr>
  </tbody>
</table>

## CustomResourceSubresourceScale {#CustomResourceSubresourceScale}

نوع CustomResourceSubresourceScale تعیین می‌کند که زیرمنبع (subresource) مربوط به scale برای CustomResourceها چگونه ارائه شود.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>labelSelectorPath</code><br/><em>string</em></td>
      <td>فیلد labelSelectorPath مسیر JSON درون یک منبع سفارشی را تعریف می‌کند که با `status.selector` در Scale متناظر است. فقط مسیرهای JSON بدون نشانه‌گذاری آرایه مجاز هستند. این مسیر باید یک مسیر JSON زیر `.status` یا `.spec` باشد. برای کار با HorizontalPodAutoscaler، تنظیم این فیلد الزامی است. فیلدی که این مسیر JSON به آن اشاره می‌کند باید یک فیلد رشته‌ای باشد (نه یک ساختار پیچیدهٔ انتخابگر) که یک انتخابگر برچسب سریال‌شده را به شکل رشته در خود دارد. اطلاعات بیشتر: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource اگر زیر مسیر داده‌شده در منبع سفارشی مقداری وجود نداشته باشد، مقدار `status.selector` در زیرمنبع `/scale` به‌طور پیش‌فرض رشتهٔ خالی خواهد بود.</td>
    </tr>
    <tr>
      <td><code>specReplicasPath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد specReplicasPath مسیر JSON درون یک منبع سفارشی را تعریف می‌کند که با `spec.replicas` در Scale متناظر است. فقط مسیرهای JSON بدون نشانه‌گذاری آرایه مجاز هستند. این مسیر باید یک مسیر JSON زیر `.spec` باشد. اگر زیر مسیر داده‌شده در منبع سفارشی مقداری وجود نداشته باشد، زیرمنبع `/scale` در پاسخ به درخواست GET خطا برمی‌گرداند.</td>
    </tr>
    <tr>
      <td><code>statusReplicasPath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد statusReplicasPath مسیر JSON درون یک منبع سفارشی را تعریف می‌کند که با `status.replicas` در Scale متناظر است. فقط مسیرهای JSON بدون نشانه‌گذاری آرایه مجاز هستند. این مسیر باید یک مسیر JSON زیر `.status` باشد. اگر زیر مسیر داده‌شده در منبع سفارشی مقداری وجود نداشته باشد، مقدار `status.replicas` در زیرمنبع `/scale` به‌طور پیش‌فرض 0 خواهد بود.</td>
    </tr>
  </tbody>
</table>


## CustomResourceSubresourceStatus {#CustomResourceSubresourceStatus}

نوع CustomResourceSubresourceStatus تعیین می‌کند که زیرمنبع status برای CustomResourceها چگونه ارائه شود. وضعیت با مسیر JSON `.status` درون یک CustomResource نمایش داده می‌شود. در صورت تنظیم: * یک زیرمنبع /status برای منبع سفارشی در دسترس قرار می‌گیرد * درخواست‌های PUT به زیرمنبع /status یک آبجکت منبع سفارشی دریافت می‌کنند و تغییرات همه‌چیز جز بخش status را نادیده می‌گیرند * درخواست‌های PUT/POST/PATCH به منبع سفارشی تغییرات بخش status را نادیده می‌گیرند

<hr>



## CustomResourceSubresources {#CustomResourceSubresources}

نوع CustomResourceSubresources زیرمنبع‌های status و scale را برای CustomResourceها تعریف می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>scale</code><br/><em><a href="{{< ref "#CustomResourceSubresourceScale" >}}">CustomResourceSubresourceScale</a></em></td>
      <td>فیلد scale نشان می‌دهد که منبع سفارشی باید یک زیرمنبع `/scale` ارائه کند که یک آبجکت Scale از نوع `autoscaling/v1` برمی‌گرداند.</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#CustomResourceSubresourceStatus" >}}">CustomResourceSubresourceStatus</a></em></td>
      <td>فیلد status نشان می‌دهد که منبع سفارشی باید یک زیرمنبع `/status` ارائه کند. در صورت فعال بودن: 1. درخواست‌هایی که به نقطهٔ پایانی اصلی منبع سفارشی ارسال می‌شوند، تغییرات بخش `status` آبجکت را نادیده می‌گیرند. 2. درخواست‌هایی که به زیرمنبع `/status` منبع سفارشی ارسال می‌شوند، تغییرات همه‌چیز جز بخش `status` آبجکت را نادیده می‌گیرند.</td>
    </tr>
  </tbody>
</table>


## CustomResourceValidation {#CustomResourceValidation}

نوع CustomResourceValidation فهرستی از روش‌های اعتبارسنجی برای CustomResourceها است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>openAPIV3Schema</code><br/><em><a href="{{< ref "#JSONSchemaProps" >}}">JSONSchemaProps</a></em></td>
      <td>فیلد openAPIV3Schema طرح‌وارهٔ (schema) OpenAPI v3 است که برای اعتبارسنجی و هرس (pruning) به کار می‌رود.</td>
    </tr>
  </tbody>
</table>


## ExternalDocumentation {#ExternalDocumentation}

نوع ExternalDocumentation امکان ارجاع به یک منبع خارجی را برای مستندات تکمیلی فراهم می‌کند.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>description</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>url</code><br/><em>string</em></td>
      <td></td>
    </tr>
  </tbody>
</table>


## JSON {#JSON}

نوع JSON هر مقدار معتبر JSON را نمایش می‌دهد. این نوع‌ها پشتیبانی می‌شوند: bool، int64، float64، string، []interface{}، map[string]interface{} و nil.

<hr>



## JSONSchemaProps {#JSONSchemaProps}

نوع JSONSchemaProps یک JSON-Schema مطابق با پیش‌نویس ۴ مشخصات (Specification Draft 4) است (http://json-schema.org/).

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>$ref</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>$schema</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>additionalItems</code><br/><em><a href="{{< ref "#JSONSchemaPropsOrBool" >}}">JSONSchemaPropsOrBool</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>additionalProperties</code><br/><em><a href="{{< ref "#JSONSchemaPropsOrBool" >}}">JSONSchemaPropsOrBool</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>allOf</code><br/><em><a href="{{< ref "#JSONSchemaProps" >}}">JSONSchemaProps array</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>anyOf</code><br/><em><a href="{{< ref "#JSONSchemaProps" >}}">JSONSchemaProps array</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>default</code><br/><em><a href="{{< ref "#JSON" >}}">JSON</a></em></td>
      <td>فیلد default یک مقدار پیش‌فرض برای فیلدهای تعریف‌نشدهٔ آبجکت است. مقداردهی پیش‌فرض یک قابلیت بتا است که تحت feature gate با نام CustomResourceDefaulting قرار دارد. برای مقداردهی پیش‌فرض، مقدار spec.preserveUnknownFields باید false باشد.</td>
    </tr>
    <tr>
      <td><code>definitions</code><br/><em>object</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>dependencies</code><br/><em>object</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>description</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>enum</code><br/><em><a href="{{< ref "#JSON" >}}">JSON array</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>example</code><br/><em><a href="{{< ref "#JSON" >}}">JSON</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>exclusiveMaximum</code><br/><em>boolean</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>exclusiveMinimum</code><br/><em>boolean</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>externalDocs</code><br/><em><a href="{{< ref "#ExternalDocumentation" >}}">ExternalDocumentation</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>format</code><br/><em>string</em></td>
      <td>فیلد format یک رشتهٔ قالب OpenAPI v3 است. قالب‌های ناشناخته نادیده گرفته می‌شوند. قالب‌های زیر اعتبارسنجی می‌شوند:  - bsonobjectid: یک شناسهٔ آبجکت bson، یعنی یک رشتهٔ هگزادسیمال 24 نویسه‌ای - uri: یک URI به همان شکلی که تابع net/url.ParseRequestURI در Golang تجزیه می‌کند - email: یک نشانی ایمیل به همان شکلی که تابع net/mail.ParseAddress در Golang تجزیه می‌کند - hostname: نمایش معتبر یک نام میزبان اینترنتی، طبق تعریف RFC 1034، بخش 3.1 [RFC1034]. - ipv4: یک نشانی IPv4 به همان شکلی که تابع net.ParseIP در Golang تجزیه می‌کند - ipv6: یک نشانی IPv6 به همان شکلی که تابع net.ParseIP در Golang تجزیه می‌کند - cidr: یک CIDR به همان شکلی که تابع net.ParseCIDR در Golang تجزیه می‌کند - mac: یک نشانی MAC به همان شکلی که تابع net.ParseMAC در Golang تجزیه می‌کند - uuid: یک UUID که حروف بزرگ را هم می‌پذیرد و با عبارت باقاعدهٔ (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ تعریف می‌شود - uuid3: یک UUID3 که حروف بزرگ را هم می‌پذیرد و با عبارت باقاعدهٔ (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ تعریف می‌شود - uuid4: یک UUID4 که حروف بزرگ را هم می‌پذیرد و با عبارت باقاعدهٔ (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ تعریف می‌شود - uuid5: یک UUID5 که حروف بزرگ را هم می‌پذیرد و با عبارت باقاعدهٔ (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ تعریف می‌شود - isbn: یک رشتهٔ عددی ISBN10 یا ISBN13 مانند "0321751043" یا "978-0321751041" - isbn10: یک رشتهٔ عددی ISBN10 مانند "0321751043" - isbn13: یک رشتهٔ عددی ISBN13 مانند "978-0321751041" - creditcard: یک شمارهٔ کارت اعتباری که با عبارت باقاعدهٔ ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ تعریف می‌شود و ممکن است نویسه‌های غیررقمی نیز در آن آمده باشد - ssn: یک شمارهٔ تأمین اجتماعی ایالات متحده مطابق با عبارت باقاعدهٔ ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: یک کد رنگ هگزادسیمال مانند "#FFFFFF: مطابق با عبارت باقاعدهٔ ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: یک کد رنگ RGB مانند "rgb(255,255,2559" - byte: داده‌های دودویی کدگذاری‌شده با base64 - password: هر نوع رشته‌ای - date: یک رشتهٔ تاریخ مانند "2006-01-02" طبق تعریف full-date در RFC3339 - duration: یک رشتهٔ مدت‌زمان مانند "22 ns" به همان شکلی که تابع time.ParseDuration در Golang تجزیه می‌کند، یا سازگار با قالب مدت‌زمان Scala - datetime: یک رشتهٔ تاریخ و زمان مانند "2014-12-15T19:30:20.000Z" طبق تعریف date-time در RFC3339.</td>
    </tr>
    <tr>
      <td><code>id</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>items</code><br/><em><a href="{{< ref "#JSONSchemaPropsOrArray" >}}">JSONSchemaPropsOrArray</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>maxItems</code><br/><em>integer</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>maxLength</code><br/><em>integer</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>maxProperties</code><br/><em>integer</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>maximum</code><br/><em>number</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>minItems</code><br/><em>integer</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>minLength</code><br/><em>integer</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>minProperties</code><br/><em>integer</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>minimum</code><br/><em>number</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>multipleOf</code><br/><em>number</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>not</code><br/><em><a href="{{< ref "#JSONSchemaProps" >}}">JSONSchemaProps</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>nullable</code><br/><em>boolean</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>oneOf</code><br/><em><a href="{{< ref "#JSONSchemaProps" >}}">JSONSchemaProps array</a></em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>pattern</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>patternProperties</code><br/><em>object</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>properties</code><br/><em>object</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>required</code><br/><em>string array</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>title</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>type</code><br/><em>string</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>uniqueItems</code><br/><em>boolean</em></td>
      <td></td>
    </tr>
    <tr>
      <td><code>x-kubernetes-embedded-resource</code><br/><em>boolean</em></td>
      <td>فیلد x-kubernetes-embedded-resource مشخص می‌کند که مقدار، یک runtime.Object تعبیه‌شدهٔ کوبرنتیز همراه با TypeMeta و ObjectMeta است. نوع آن باید object باشد. محدودسازی بیشتر آبجکت تعبیه‌شده مجاز است. فیلدهای kind، apiVersion و metadata به‌طور خودکار اعتبارسنجی می‌شوند. مقدار x-kubernetes-preserve-unknown-fields می‌تواند true باشد، اما اگر آبجکت به‌طور کامل مشخص شده باشد (تا سطح kind، apiVersion و metadata)، لزومی ندارد true باشد.</td>
    </tr>
    <tr>
      <td><code>x-kubernetes-int-or-string</code><br/><em>boolean</em></td>
      <td>فیلد x-kubernetes-int-or-string مشخص می‌کند که این مقدار یا یک عدد صحیح است یا یک رشته. اگر مقدار آن true باشد، نوع خالی مجاز است و تعیین type به‌عنوان فرزند anyOf در صورتی مجاز است که از یکی از الگوهای زیر پیروی کند:  1) anyOf:    - type: integer    - type: string 2) allOf:    - anyOf:      - type: integer      - type: string    - ... صفر یا بیشتر</td>
    </tr>
    <tr>
      <td><code>x-kubernetes-list-map-keys</code><br/><em>string array</em></td>
      <td>فیلد x-kubernetes-list-map-keys با مشخص کردن کلیدهایی که به‌عنوان اندیس map به کار می‌روند، یک آرایه با x-kubernetes-list-type از نوع `map` را حاشیه‌نویسی می‌کند.  این برچسب را فقط باید روی فهرست‌هایی به کار برد که افزونهٔ "x-kubernetes-list-type" آن‌ها روی "map" تنظیم شده است. همچنین مقادیری که برای این ویژگی مشخص می‌شوند باید فیلدهایی با نوع اسکالر از ساختار فرزند باشند (تودرتویی پشتیبانی نمی‌شود).  ویژگی‌های مشخص‌شده باید یا الزامی باشند یا مقدار پیش‌فرض داشته باشند تا وجود آن‌ها در همهٔ آیتم‌های فهرست تضمین شود.</td>
    </tr>
    <tr>
      <td><code>x-kubernetes-list-type</code><br/><em>string</em></td>
      <td>فیلد x-kubernetes-list-type یک آرایه را حاشیه‌نویسی می‌کند تا ساختار (topology) آن را دقیق‌تر توصیف کند. این افزونه را فقط باید روی فهرست‌ها به کار برد و می‌تواند یکی از 3 مقدار ممکن را داشته باشد:  1) `atomic`: فهرست مانند یک مقدار اسکالر، به‌عنوان یک موجودیت واحد در نظر گرفته می‌شود.      فهرست‌های اتمی هنگام به‌روزرسانی به‌طور کامل جایگزین می‌شوند. این افزونه      را می‌توان روی هر نوع فهرستی (struct، اسکالر و ...) به کار برد. 2) `set`:      مجموعه‌ها فهرست‌هایی هستند که نباید چند آیتم با مقدار یکسان داشته باشند. هر      مقدار باید یک اسکالر، یک آبجکت با x-kubernetes-map-type از نوع `atomic` یا یک      آرایه با x-kubernetes-list-type از نوع `atomic` باشد. 3) `map`:      این فهرست‌ها از این جهت شبیه mapها هستند که عناصرشان یک کلید غیراندیسی دارند      که برای شناسایی آن‌ها به کار می‌رود. ترتیب عناصر هنگام ادغام حفظ می‌شود. برچسب map      را فقط باید روی فهرستی به کار برد که عناصرش از نوع object هستند. مقدار پیش‌فرض برای آرایه‌ها atomic است.</td>
    </tr>
    <tr>
      <td><code>x-kubernetes-map-type</code><br/><em>string</em></td>
      <td>فیلد x-kubernetes-map-type یک آبجکت را حاشیه‌نویسی می‌کند تا ساختار آن را دقیق‌تر توصیف کند. این افزونه را فقط باید زمانی به کار برد که نوع، object باشد و می‌تواند یکی از 2 مقدار ممکن را داشته باشد:  1) `granular`:      این mapها، map واقعی (جفت‌های کلید-مقدار) هستند و هر یک از فیلدهایشان از      دیگری مستقل است (هر کدام را می‌توان با عامل‌های جداگانه دست‌کاری کرد). این      رفتار پیش‌فرض همهٔ mapها است. 2) `atomic`: فهرست مانند یک مقدار اسکالر، به‌عنوان یک موجودیت واحد در نظر گرفته می‌شود.      mapهای اتمی هنگام به‌روزرسانی به‌طور کامل جایگزین می‌شوند.</td>
    </tr>
    <tr>
      <td><code>x-kubernetes-preserve-unknown-fields</code><br/><em>boolean</em></td>
      <td>فیلد x-kubernetes-preserve-unknown-fields مانع می‌شود که مرحلهٔ رمزگشایی سرور API فیلدهایی را که در طرح‌وارهٔ اعتبارسنجی مشخص نشده‌اند هرس کند. این رفتار به‌صورت بازگشتی روی فیلدها اثر می‌گذارد، اما اگر در طرح‌واره ویژگی‌های تودرتو یا additionalProperties مشخص شده باشند، دوباره به رفتار عادی هرس بازمی‌گردد. مقدار این فیلد می‌تواند true یا تعریف‌نشده باشد. مقدار false ممنوع است.</td>
    </tr>
    <tr>
      <td><code>x-kubernetes-validations</code><br/><em><a href="{{< ref "#ValidationRule" >}}">ValidationRule array</a></em><br/><em>راهبرد وصله (patch strategy): ادغام بر اساس کلید <code>rule</code></em></td>
      <td>فیلد x-kubernetes-validations فهرستی از قواعد اعتبارسنجی را توصیف می‌کند که به زبان عبارت‌های CEL نوشته شده‌اند.</td>
    </tr>
  </tbody>
</table>


## JSONSchemaPropsOrArray {#JSONSchemaPropsOrArray}

نوع JSONSchemaPropsOrArray مقداری را نمایش می‌دهد که می‌تواند یا یک JSONSchemaProps باشد یا آرایه‌ای از JSONSchemaProps. این نوع عمدتاً برای اهداف سریال‌سازی وجود دارد.

<hr>



## JSONSchemaPropsOrBool {#JSONSchemaPropsOrBool}

نوع JSONSchemaPropsOrBool یک JSONSchemaProps یا یک مقدار بولی را نمایش می‌دهد. مقدار پیش‌فرض برای ویژگی بولی true است.

<hr>



## SelectableField {#SelectableField}

نوع SelectableField مسیر JSON فیلدی را مشخص می‌کند که می‌توان از آن در انتخابگرهای فیلد (field selectors) استفاده کرد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>jsonPath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد jsonPath یک مسیر ساده JSON است که روی هر منبع سفارشی ارزیابی می‌شود تا مقداری برای انتخابگر فیلد به دست آید. فقط مسیرهای JSON بدون نشانه‌گذاری آرایه مجاز هستند. این مسیر باید به فیلدی از نوع string، boolean یا integer اشاره کند. نوع‌هایی با مقادیر enum و رشته‌هایی که قالب دارند مجاز هستند. اگر jsonPath به فیلدی اشاره کند که در منبع وجود ندارد، حاصل ارزیابی آن رشتهٔ خالی خواهد بود. این مسیر نباید به فیلدهای metadata اشاره کند. الزامی است.</td>
    </tr>
  </tbody>
</table>


## ServiceReference {#ServiceReference}

نوع ServiceReference ارجاعی به Service.legacy.k8s.io را نگه می‌دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد name نام Service است. الزامی است.</td>
    </tr>
    <tr>
      <td><code>namespace</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد namespace فضای نام Service است. الزامی است.</td>
    </tr>
    <tr>
      <td><code>path</code><br/><em>string</em></td>
      <td>فیلد path یک مسیر URL اختیاری است که webhook از طریق آن فراخوانی می‌شود.</td>
    </tr>
    <tr>
      <td><code>port</code><br/><em>integer</em></td>
      <td>فیلد port یک پورت اختیاری Service است که webhook از طریق آن فراخوانی می‌شود. مقدار `port` باید یک شمارهٔ پورت معتبر (از 1 تا 65535، با احتساب هر دو) باشد. مقدار پیش‌فرض برای حفظ سازگاری با نسخه‌های قبلی 443 است.</td>
    </tr>
  </tbody>
</table>

## ValidationRule {#ValidationRule}

آبجکت ValidationRule یک قاعده‌ی اعتبارسنجی را توصیف می‌کند که به زبان عبارت CEL نوشته شده است.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>fieldPath</code><br/><em>string</em></td>
      <td>فیلد fieldPath مسیر فیلدی را نشان می‌دهد که هنگام ناموفق بودن اعتبارسنجی بازگردانده می‌شود. این مسیر باید یک مسیر JSON نسبی (یعنی با نماد آرایه) باشد که دامنه‌ی آن به محل این افزونه‌ی x-kubernetes-validations در اسکیما محدود است، و باید به یک فیلد موجود اشاره کند. برای مثال، وقتی اعتبارسنجی بررسی می‌کند که آیا یک ویژگی مشخص `foo` زیر نگاشت `testMap` وجود دارد، می‌توان fieldPath را `.testMap.foo` قرار داد. اگر اعتبارسنجی بررسی کند که دو فهرست باید ویژگی‌های یکتا داشته باشند، می‌توان fieldPath را برابر یکی از این دو فهرست قرار داد؛ برای مثال `.testList`. اندیس عددی فهرست پشتیبانی نمی‌شود. در حال حاضر، عملیات فرزند (child) برای اشاره به یک فیلد موجود پشتیبانی می‌شود. برای اطلاعات بیشتر به [پشتیبانی از JSONPath در کوبرنتیز](https://kubernetes.io/docs/reference/kubectl/jsonpath/) مراجعه کنید. اندیس عددی آرایه پشتیبانی نمی‌شود. برای نام فیلدهایی که نویسه‌های ویژه دارند، از `['specialName']` برای اشاره به نام فیلد استفاده کنید. برای مثال، اگر ویژگی `foo.34$` در فهرست `testList` آمده باشد، می‌توان fieldPath را `.testList['foo.34$']` قرار داد.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>فیلد message پیامی را نشان می‌دهد که هنگام ناموفق بودن اعتبارسنجی نمایش داده می‌شود. اگر Rule شامل شکست خط باشد، وجود این پیام الزامی است. پیام نباید شامل شکست خط باشد. اگر این فیلد تنظیم نشود، پیام برابر "failed rule: {Rule}" خواهد بود. برای مثال: "must be a URL with the host matching spec.host"</td>
    </tr>
    <tr>
      <td><code>messageExpression</code><br/><em>string</em></td>
      <td>فیلد messageExpression یک عبارت CEL تعریف می‌کند که حاصل ارزیابی آن، پیام شکست اعتبارسنجی است و هنگام ناموفق بودن این قاعده بازگردانده می‌شود. از آنجا که messageExpression به‌عنوان پیام شکست استفاده می‌شود، حاصل ارزیابی آن باید یک رشته باشد. اگر هر دو فیلد message و messageExpression در یک قاعده وجود داشته باشند، در صورت ناموفق بودن اعتبارسنجی از messageExpression استفاده می‌شود. اگر messageExpression به خطای زمان اجرا منجر شود، این خطا ثبت (log) می‌شود و پیام شکست اعتبارسنجی به گونه‌ای تولید می‌شود که گویی فیلد messageExpression تنظیم نشده است. اگر حاصل ارزیابی messageExpression رشته‌ای خالی، رشته‌ای فقط شامل فاصله یا رشته‌ای شامل شکست خط باشد، پیام شکست اعتبارسنجی باز هم به گونه‌ای تولید می‌شود که گویی فیلد messageExpression تنظیم نشده است، و این موضوع که messageExpression رشته‌ای خالی/رشته‌ای فقط شامل فاصله/رشته‌ای شامل شکست خط تولید کرده است نیز ثبت می‌شود. عبارت messageExpression به همه‌ی متغیرهایی که rule به آن‌ها دسترسی دارد، دسترسی دارد؛ تنها تفاوت در نوع مقدار بازگشتی است. مثال: "x must be less than max ("+string(self.max)+")"</td>
    </tr>
    <tr>
      <td><code>optionalOldSelf</code><br/><em>boolean</em></td>
      <td>فیلد optionalOldSelf برای آن به کار می‌رود که یک قاعده‌ی گذار (transition rule) حتی هنگام ایجاد اولیه‌ی آبجکت، یا وقتی آبجکت قدیمی فاقد مقدار است، ارزیابی شود. در صورت فعال بودن این فیلد، `oldSelf` یک مقدار اختیاری CEL خواهد بود که اگر مقدار قدیمی وجود نداشته باشد یا آبجکت تازه ایجاد شده باشد، مقدار آن `None` است. می‌توانید وجود oldSelf را با `oldSelf.hasValue()` بررسی کنید و پس از بررسی، مقدار آن را با `oldSelf.value()` استخراج کنید. برای اطلاعات بیشتر، مستندات CEL درباره‌ی انواع Optional را ببینید: https://pkg.go.dev/github.com/google/cel-go/cel#OptionalTypes تنظیم این فیلد فقط زمانی مجاز است که `oldSelf` در `rule` استفاده شده باشد.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>فیلد reason یک دلیل ماشین‌خوان برای شکست اعتبارسنجی فراهم می‌کند که وقتی درخواستی در این قاعده‌ی اعتبارسنجی رد شود، به فراخواننده بازگردانده می‌شود. کد وضعیت HTTP که به فراخواننده بازگردانده می‌شود، با دلیلِ نخستین قاعده‌ی اعتبارسنجیِ ناموفق مطابقت خواهد داشت. دلایلی که در حال حاضر پشتیبانی می‌شوند عبارت‌اند از: "FieldValueInvalid"، "FieldValueForbidden"، "FieldValueRequired" و "FieldValueDuplicate". اگر این فیلد تنظیم نشود، به‌طور پیش‌فرض از "FieldValueInvalid" استفاده می‌شود. کلاینت‌ها هنگام خواندن این مقدار باید همه‌ی دلایلی را که در آینده اضافه می‌شوند بپذیرند و دلایل ناشناخته را FieldValueInvalid در نظر بگیرند.<br/><br/>مقادیر ممکن enum:<br/> - مقدار `"FieldValueDuplicate"` برای گزارش تداخل مقادیری به کار می‌رود که باید یکتا باشند (مثلاً شناسه‌های یکتا).<br/> - مقدار `"FieldValueForbidden"` برای گزارش مقادیر معتبری (از نظر قواعد قالب‌بندی) به کار می‌رود که در برخی شرایط پذیرفته می‌شدند، اما در شرایط فعلی (مانند سیاست امنیتی) مجاز نیستند.<br/> - مقدار `"FieldValueInvalid"` برای گزارش مقادیر بدشکل به کار می‌رود (مثلاً عدم تطابق با regex، طول بیش از حد، یا خارج از محدوده بودن).<br/> - مقدار `"FieldValueRequired"` برای گزارش مقادیر الزامی‌ای به کار می‌رود که ارائه نشده‌اند (مثلاً رشته‌های خالی، مقادیر null یا آرایه‌های خالی).</td>
    </tr>
    <tr>
      <td><code>rule</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>فیلد Rule عبارتی را نشان می‌دهد که CEL آن را ارزیابی می‌کند. مرجع: https://github.com/google/cel-spec دامنه‌ی Rule به محل افزونه‌ی x-kubernetes-validations در اسکیما محدود است. متغیر `self` در عبارت CEL به مقدارِ همین دامنه مقید است. مثال: - قاعده‌ای با دامنه‌ی ریشه‌ی منبعی که زیرمنبع status دارد: {"rule": "self.status.actual \<= self.spec.maxDesired"}  اگر دامنه‌ی Rule آبجکتی دارای ویژگی (property) باشد، ویژگی‌های در دسترس آبجکت از طریق `self.field` قابل انتخاب‌اند و وجود فیلد را می‌توان با `has(self.field)` بررسی کرد. در عبارت‌های CEL، فیلدهایی که مقدار null دارند، فیلدهای غایب در نظر گرفته می‌شوند. اگر دامنه‌ی Rule آبجکتی دارای additionalProperties (یعنی یک نگاشت) باشد، مقادیر نگاشت از طریق `self[mapKey]` در دسترس‌اند، وجود کلید در نگاشت را می‌توان با `mapKey in self` بررسی کرد و همه‌ی مدخل‌های نگاشت از طریق ماکروها و توابع CEL مانند `self.all(...)` در دسترس‌اند. اگر دامنه‌ی Rule یک آرایه باشد، عناصر آرایه از طریق `self[i]` و همچنین از طریق ماکروها و توابع در دسترس‌اند. اگر دامنه‌ی Rule یک مقدار اسکالر باشد، `self` به همان مقدار اسکالر مقید می‌شود. مثال‌ها: - قاعده‌ای با دامنه‌ی نگاشتی از آبجکت‌ها: {"rule": "self.components['Widget'].priority \< 10"} - قاعده‌ای با دامنه‌ی فهرستی از اعداد صحیح: {"rule": "self.values.all(value, value >= 0 && value \< 100)"} - قاعده‌ای با دامنه‌ی یک مقدار رشته‌ای: {"rule": "self.startsWith('kube')"}  فیلدهای `apiVersion`، `kind`، `metadata.name` و `metadata.generateName` همیشه از ریشه‌ی آبجکت و از هر آبجکتی که با x-kubernetes-embedded-resource حاشیه‌نویسی شده باشد، در دسترس‌اند. هیچ ویژگی دیگری از metadata در دسترس نیست.  داده‌های ناشناخته‌ای که از طریق x-kubernetes-preserve-unknown-fields در منابع سفارشی حفظ می‌شوند، در عبارت‌های CEL در دسترس نیستند. این داده‌ها شامل موارد زیرند: - مقادیر فیلدهای ناشناخته‌ای که اسکیماهای آبجکت دارای x-kubernetes-preserve-unknown-fields حفظ می‌کنند. - ویژگی‌هایی از آبجکت که اسکیمای آن‌ها از یک «نوع ناشناخته» است. «نوع ناشناخته» به‌صورت بازگشتی چنین تعریف می‌شود:   - اسکیمایی بدون type که x-kubernetes-preserve-unknown-fields در آن برابر true است   - آرایه‌ای که اسکیمای items آن از یک «نوع ناشناخته» است   - آبجکتی که اسکیمای additionalProperties آن از یک «نوع ناشناخته» است  فقط ویژگی‌هایی در دسترس‌اند که نامشان به شکل `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` باشد. نام ویژگی‌های در دسترس، هنگام دسترسی در عبارت، طبق قواعد زیر escape می‌شوند: - رشته‌ی '__' به '__underscores__' escape می‌شود - نویسه‌ی '.' به '__dot__' escape می‌شود - نویسه‌ی '-' به '__dash__' escape می‌شود - نویسه‌ی '/' به '__slash__' escape می‌شود - نام ویژگی‌هایی که دقیقاً با یکی از کلیدواژه‌های رزروشده‌ی CEL مطابقت دارند، به '__{keyword}__' escape می‌شوند. این کلیدواژه‌ها عبارت‌اند از: 	  "true", "false", "null", "in", "as", "break", "const", "continue", "else", "for", "function", "if", 	  "import", "let", "loop", "package", "namespace", "return". مثال‌ها:   - قاعده‌ای که به ویژگی‌ای با نام "namespace" دسترسی دارد: {"rule": "self.__namespace__ > 0"}   - قاعده‌ای که به ویژگی‌ای با نام "x-prop" دسترسی دارد: {"rule": "self.x__dash__prop > 0"}   - قاعده‌ای که به ویژگی‌ای با نام "redact__d" دسترسی دارد: {"rule": "self.redact__underscores__d > 0"}  مقایسه‌ی برابری روی آرایه‌هایی که x-kubernetes-list-type آن‌ها 'set' یا 'map' است، ترتیب عناصر را نادیده می‌گیرد؛ یعنی [1, 2] == [2, 1]. الحاق آرایه‌هایی که x-kubernetes-list-type دارند، از معناشناسی همان نوع فهرست پیروی می‌کند:   - نوع 'set': عبارت `X + Y` اجتماعی را انجام می‌دهد که در آن موقعیت همه‌ی عناصر `X` در آرایه حفظ می‌شود و     عناصر غیرمشترک `Y` با حفظ ترتیب جزئی‌شان به انتهای آن افزوده می‌شوند.   - نوع 'map': عبارت `X + Y` ادغامی را انجام می‌دهد که در آن موقعیت همه‌ی کلیدهای `X` در آرایه حفظ می‌شود، اما وقتی مجموعه‌ی کلیدهای `X` و `Y` اشتراک داشته باشند،     مقادیر با مقادیر `Y` بازنویسی می‌شوند. عناصری از `Y` که     کلیدهای غیرمشترک دارند، با حفظ ترتیب جزئی‌شان به انتها افزوده می‌شوند.  اگر `rule` از متغیر `oldSelf` استفاده کند، به‌طور ضمنی یک `transition rule` است.  به‌طور پیش‌فرض، نوع متغیر `oldSelf` با نوع `self` یکسان است. وقتی `optionalOldSelf` برابر true باشد، متغیر `oldSelf` یک متغیر اختیاری CEL است  که نوع value() آن با نوع `self` یکسان است. برای جزئیات بیشتر، مستندات فیلد `optionalOldSelf` را ببینید.  قاعده‌های گذار به‌طور پیش‌فرض فقط روی درخواست‌های UPDATE اعمال می‌شوند و اگر مقدار قدیمی یافت نشود، از ارزیابی آن‌ها صرف‌نظر می‌شود. با true کردن `optionalOldSelf` می‌توانید یک قاعده‌ی گذار را بدون قید و شرط ارزیابی کنید.</td>
    </tr>
  </tbody>
</table>


## WebhookClientConfig {#WebhookClientConfig}

آبجکت WebhookClientConfig اطلاعات لازم برای برقراری اتصال TLS با وب‌هوک را در بر دارد.

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>caBundle</code><br/><em>string</em></td>
      <td>فیلد caBundle یک بسته‌ی CA با کدگذاری PEM است که برای اعتبارسنجی گواهی سرور وب‌هوک استفاده می‌شود. اگر مشخص نشود، از ریشه‌های اعتماد سیستم روی apiserver استفاده می‌شود.</td>
    </tr>
    <tr>
      <td><code>service</code><br/><em><a href="{{< ref "#ServiceReference" >}}">ServiceReference</a></em></td>
      <td>فیلد service ارجاعی به سرویسِ این وب‌هوک است. باید یکی از service یا url مشخص شود.  اگر وب‌هوک درون کلاستر اجرا می‌شود، باید از `service` استفاده کنید.</td>
    </tr>
    <tr>
      <td><code>url</code><br/><em>string</em></td>
      <td>فیلد url محل وب‌هوک را در قالب استاندارد URL (`scheme://host:port/path`) مشخص می‌کند. دقیقاً یکی از `url` یا `service` باید مشخص شود.  مقدار `host` نباید به سرویسی اشاره کند که درون کلاستر اجرا می‌شود؛ به جای آن از فیلد `service` استفاده کنید. ممکن است در برخی apiserverها، نام میزبان از طریق DNS خارجی تفکیک (resolve) شود (برای مثال، `kube-apiserver` نمی‌تواند DNS درون کلاستر را تفکیک کند، زیرا این کار لایه‌بندی را نقض می‌کند). مقدار `host` می‌تواند یک نشانی IP نیز باشد.  توجه داشته باشید که استفاده از `localhost` یا `127.0.0.1` به‌عنوان `host` پرخطر است، مگر اینکه با دقت فراوان این وب‌هوک را روی همه‌ی میزبان‌هایی اجرا کنید که apiserverی روی آن‌ها اجرا می‌شود که ممکن است نیاز به فراخوانی این وب‌هوک داشته باشد. چنین نصب‌هایی احتمالاً قابل‌حمل نیستند؛ یعنی راه‌اندازی آن‌ها در یک کلاستر جدید آسان نیست.  طرح (scheme) باید "https" باشد؛ یعنی URL باید با "https://" آغاز شود.  مسیر اختیاری است و در صورت وجود، می‌تواند هر رشته‌ای باشد که در URL مجاز است. می‌توانید از مسیر برای ارسال یک رشته‌ی دلخواه به وب‌هوک استفاده کنید؛ برای مثال، یک شناسه‌ی کلاستر.  تلاش برای استفاده از اطلاعات کاربر یا احراز هویت پایه، مانند "user:password@"، مجاز نیست. بخش‌های fragment ("#...") و پارامترهای کوئری ("?...") نیز مجاز نیستند.</td>
    </tr>
  </tbody>
</table>


## WebhookConversion {#WebhookConversion}

آبجکت WebhookConversion نحوه‌ی فراخوانی یک وب‌هوک تبدیل را توصیف می‌کند

<hr>

<table>
  <thead><tr><th>فیلد</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>clientConfig</code><br/><em><a href="{{< ref "#WebhookClientConfig" >}}">WebhookClientConfig</a></em></td>
      <td>فیلد clientConfig دستورالعمل‌های نحوه‌ی فراخوانی وب‌هوک را، در صورتی که strategy برابر `Webhook` باشد، مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>conversionReviewVersions</code>&nbsp;<strong>*</strong><br/><em>string array</em></td>
      <td>فیلد conversionReviewVersions فهرستی مرتب از نسخه‌های ترجیحی `ConversionReview` است که وب‌هوک انتظار دارد. سرور API نخستین نسخه‌ای از این فهرست را که پشتیبانی می‌کند، به کار می‌برد. اگر سرور API از هیچ‌یک از نسخه‌های این فهرست پشتیبانی نکند، تبدیل برای منبع سفارشی ناموفق خواهد بود. اگر یک پیکربندی ذخیره‌شده‌ی وب‌هوک نسخه‌های مجاز را مشخص کند اما هیچ نسخه‌ای را که برای سرور API شناخته‌شده است در بر نگیرد، فراخوانی‌های وب‌هوک ناموفق خواهند بود.</td>
    </tr>
  </tbody>
</table>



## عملیات {#Operations}

<hr>


### `post` ایجاد

#### درخواست HTTP

POST /apis/apiextensions.k8s.io/v1/customresourcedefinitions



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوش‌قالب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همه‌ی مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ ایجادکننده‌ی این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل‌چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند، چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: همه‌ی فیلدهای ناشناخته را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری که رمزگشا با آن‌ها روبه‌رو می‌شود، همه را به‌جز آخرین مورد نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه‌ی v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه‌ی v1.23 و نسخه‌های بعدی است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری‌ای وجود داشته باشد، درخواست را با خطای BadRequest ناموفق می‌کند. خطای بازگردانده‌شده از سرور، همه‌ی فیلدهای ناشناخته و تکراریِ مشاهده‌شده را در بر خواهد داشت.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
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
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>

### عملیات `patch`: وصله‌کردن

#### درخواست HTTP

PATCH /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. هر دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل‌چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>این پارامتر به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 به بعد است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور همهٔ فیلدهای ناشناخته و تکراری یافت‌شده را در بر خواهد داشت.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>این گزینه درخواست‌های Apply را «اجباری» می‌کند؛ یعنی کاربر مالکیت فیلدهای متعارضی را که متعلق به دیگران است دوباره به دست می‌گیرد. برای درخواست‌های patch غیر از apply، این پرچم نباید تنظیم شود.</td>
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
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجادشده (Created)</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `put`: جایگزینی

#### درخواست HTTP

PUT /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. هر دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>نامی است که به عامل یا موجودیتِ اعمال‌کنندهٔ این تغییرات نسبت داده می‌شود. طول این مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط نویسه‌های قابل‌چاپ را، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، در بر بگیرد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>این پارامتر به سرور اعلام می‌کند که با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن روبه‌رو می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری‌ای که با آن روبه‌رو می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 به بعد است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری‌ای وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور همهٔ فیلدهای ناشناخته و تکراری یافت‌شده را در بر خواهد داشت.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
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
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>ایجادشده</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>


### عملیات `delete`: حذف

#### درخواست HTTP

DELETE /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت قالب‌بندی‌شده و خوانا چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. هر دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمان باقی‌مانده تا حذف آبجکت، بر حسب ثانیه. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، مهلت پیش‌فرضِ نوع مشخص‌شده استفاده می‌شود. اگر مقداری تعیین نشود، مقدار پیش‌فرضِ هر آبجکت به کار می‌رود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناامن منبع آغاز می‌شود. منبعی خراب به شمار می‌رود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، برای نمونه رمزگشایی آن‌ها ناموفق است، یا ب) تبدیل آن به یک آبجکت ناموفق است. نکته: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. این فیلد مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true باشد، finalizer «orphan» به فهرست finalizerهای آبجکت افزوده می‌شود و اگر false باشد، از این فهرست حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و اگر انجام شود، به چه شیوه‌ای. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض ویژهٔ هر منبع تعیین می‌شود. مقادیر قابل‌قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
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
      <td>پذیرفته‌شده (Accepted)</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /apis/apiextensions.k8s.io/v1/customresourcedefinitions



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
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue را باید هنگام بازیابی نتایج بیشتر از سرور تنظیم کرد. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به همراه یک توکن continue پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست list دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر پایهٔ آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست list ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار (persist) شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. به‌طور پیش‌فرض همهٔ آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت‌زمانی بر حسب ثانیه که پیش از حذف آبجکت باید سپری شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت پیش‌فرض برای نوع مشخص‌شده استفاده می‌شود. در صورت مشخص‌نشدن، مقدار پیش‌فرض مختص هر آبجکت به کار می‌رود. صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب شکست بخورد، حذف ناامن منبع را آغاز می‌کند. یک منبع زمانی خراب در نظر گرفته می‌شود که نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد، به این دلیل که الف) داده‌های آن قابل تبدیل نیستند، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) کدگشایی (decode) آن به یک آبجکت ناموفق است. توجه: حذف ناامن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را انجام نمی‌دهد و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناامن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را از کار بیندازد. فقط در صورتی از آن استفاده کنید که واقعاً می‌دانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آگاهانه آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدودکردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. به‌طور پیش‌فرض همهٔ آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای بازیابی دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعدادی کمتر از آیتم‌های درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این وضعیت گاهی snapshot سازگار (consistent snapshot) نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت یک نتیجهٔ بسیار بزرگ در بخش‌های کوچک‌تر استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که هنگام محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. تعیین می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام «orphan» به فهرست finalizerهای آبجکت افزوده یا از آن حذف می‌شود. می‌توان یا این فیلد یا PropagationPolicy را تنظیم کرد، اما نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>تعیین می‌کند که آیا جمع‌آوری زباله (garbage collection) انجام شود و اگر آری، چگونه. می‌توان یا این فیلد یا OrphanDependents را تنظیم کرد، اما نه هر دو را. سیاست پیش‌فرض بر اساس مجموعهٔ finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به جمع‌آورندهٔ زباله اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که یک درخواست می‌تواند از کدام نسخه‌های منبع پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را بازسازی کند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی «Bookmark» ارسال می‌شود. این bookmark نسخهٔ منبع (ResourceVersion یا RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، گزینهٔ `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، به معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص‌کردن یک یا چند بازهٔ هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object پیروی می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر عبارت‌اند از:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای غیرشامل را روی فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch را فعال کنید.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت‌زمان فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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

GET /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>

### فهرست‌گیری با `get`

#### درخواست HTTP

GET /apis/apiextensions.k8s.io/v1/customresourcedefinitions



#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>فیلد allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی برگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال خواهد کرد. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام بازیابی نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار (consistent) نیاز داشته باشد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر پایه آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion برگردانده‌شده از سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) که فهرست آبجکت‌های برگردانده‌شده را بر اساس فیلدهایشان محدود می‌کند. به‌طور پیش‌فرض همه آبجکت‌ها برگردانده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری که فهرست آبجکت‌های برگردانده‌شده را بر اساس برچسب‌هایشان محدود می‌کند. به‌طور پیش‌فرض همه آبجکت‌ها برگردانده می‌شوند.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>فیلد limit حداکثر تعداد پاسخ‌هایی را تعیین می‌کند که یک فراخوانی list برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی مجموعه بعدی نتایج به کار برد. اگر همه آبجکت‌های درخواستی فیلتر شوند، تعیین limit ممکن است تعداد آیتم‌هایی کمتر از مقدار درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود.  سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجه یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این وضعیت گاهی snapshot سازگار (consistent snapshot) نامیده می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit یک نتیجه بسیار بزرگ را در قطعه‌های کوچک‌تر دریافت می‌کند، همه آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در حین فهرست‌گیری قطعه‌قطعه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersion محدودیتی تعیین می‌کند که مشخص می‌کند درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>فیلد resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید.  به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را بسازد. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند.  هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، گزینه `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به این صورت است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به‌معنای «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود.  مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>فیلد shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object (مثلاً "object.metadata.uid") استفاده می‌کنند، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd لیترال‌های رشته‌ای CEL درون تک‌نقل‌قول با پیشوند '0x' هستند که کران پایینِ شامل و کران بالای ناشامل را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای ناشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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
      <td>موفق (OK)</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinitionList" >}}">CustomResourceDefinitionList</a></em></td>
    </tr>
  </tbody>
</table>

### پایش (`get` Watch)

#### درخواست HTTP

GET /apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>با پارامتر allowWatchBookmarks، رویدادهای پایش (watch) از نوع "BOOKMARK" درخواست می‌شوند. سرورهایی که بوکمارک را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال بوکمارک‌ها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که بوکمارک‌ها در فواصل زمانی مشخصی برگردانده می‌شوند و همچنین نمی‌توانند فرض کنند که سرور در طول یک نشست اصلاً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع پایش نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام بازیابی نتایج بیشتر از سرور، باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما بر پایه جدیدترین تصویر لحظه‌ای (snapshot) است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند پایش را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های برگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست برمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست با مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای بازیابی دسته بعدی نتایج به کار برد. اگر همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعدادی کمتر از مقدار درخواستی (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همه نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. وقتی watch برابر true باشد، از این فیلد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue برگردانده می‌شوند، با نتیجه یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این وضعیت گاهی تصویر لحظه‌ای سازگار گفته می‌شود و تضمین می‌کند کلاینتی که با استفاده از limit نتایج بسیار بزرگ را در تکه‌های کوچک‌تر دریافت می‌کند، همه آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت برگردانده می‌شود که در زمان محاسبه نخستین نتیجه فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر برابر 'true' باشد، خروجی به شکل خوانا و قالب‌بندی‌شده چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. به‌طور پیش‌فرض تنظیم نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان پایش با رویدادهای ساختگی آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را بازتولید کند. پس از ارسال همه این رویدادها، یک رویداد ساختگی "Bookmark" ارسال می‌شود. این بوکمارک، ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان پایش طبق روال عادی ادامه می‌یابد و رویدادهای پایش مربوط به تغییرات (پس از RV) در آبجکت‌های پایش‌شده را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، گزینه `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست پایش به این صورت است:<br/> - مقدار `resourceVersionMatch` = NotOlderThan به‌صورت «داده‌ای دست‌کم به جدیدیِ `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگیِ نسخه ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد بوکمارک زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا اصلاً تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های برگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهایی که در حال حاضر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لفظی CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار، مدت فراخوانی را صرف‌نظر از وجود یا نبود فعالیت محدود می‌کند.</td>
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

### `get` پایش (watch) فهرست

#### درخواست HTTP

GET /apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاح‌دید سرور انجام می‌شود. کلاینت‌ها نباید فرض کنند که bookmarkها در فواصل زمانی مشخصی بازگردانده می‌شوند، و نیز نمی‌توانند فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینهٔ continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعریف می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجهٔ یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما بر پایهٔ آخرین snapshot است و با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از نخستین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، به شرط آنکه کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion که سرور بازگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض، همه‌چیز است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی list بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فرادادهٔ فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت دستهٔ بعدی نتایج به کار برد. اگر همهٔ آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است به بازگشت آیتم‌هایی کمتر از تعداد درخواست‌شده (حتی صفر آیتم) منجر شود؛ بنابراین کلاینت‌ها فقط باید از وجود فیلد continue برای تشخیص در دسترس بودن نتایج بیشتر استفاده کنند. سرورها ممکن است از آرگومان limit پشتیبانی نکنند و همهٔ نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با نتیجهٔ یک فراخوانی list واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور نخستین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی snapshot سازگار (consistent snapshot) گفته می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجهٔ بسیار بزرگ استفاده می‌کند، همهٔ آبجکت‌های ممکن را ببیند. اگر آبجکت‌ها در طول یک فهرست‌گیری بخش‌بندی‌شده به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که در زمان محاسبهٔ نخستین نتیجهٔ فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty-print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست را می‌توان از کدام نسخه‌های منبع پاسخ داد. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch تعیین می‌کند که resourceVersion چگونه بر فراخوانی‌های list اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های list که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این صورت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را بازسازی می‌کنند. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق روال عادی ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) در آبجکت‌های تحت پایش را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - اگر `resourceVersionMatch` = NotOlderThan باشد، به معنای «داده‌هایی دست‌کم به تازگی `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت تا یک `resourceVersion` دست‌کم به تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) true و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. این قالب از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازهٔ هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشهٔ object استفاده می‌کنند (مثلاً "object.metadata.uid")، نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL درون نقل‌قول تکی با پیشوند '0x' هستند که کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که در آن کران بالای غیرشامل برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این یک فیلد آلفا است و به فعال‌سازی feature gate با نام ShardedListAndWatch نیاز دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) برای فراخوانی list/watch. این مقدار مدت فراخوانی را، صرف‌نظر از وجود یا نبود هرگونه فعالیت، محدود می‌کند.</td>
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


### `patch` وصله کردن وضعیت

#### درخواست HTTP

PATCH /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty-print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی (dry run) پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ انجام‌دهندهٔ این تغییرات مرتبط است. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که شامل فیلدهای ناشناخته یا تکراری هستند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق سرآیند (header) استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطایی که سرور بازمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری‌ای است که با آن‌ها مواجه شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «اجباری» می‌کند. یعنی کاربر مالکیت فیلدهای متعارضی را که متعلق به دیگران است دوباره به دست می‌گیرد. پرچم Force باید برای درخواست‌های patch غیر apply تنظیم‌نشده باقی بماند.</td>
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
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن وضعیت

#### درخواست HTTP

GET /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty-print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>


### `put` جایگزینی وضعیت

#### درخواست HTTP

PUT /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام CustomResourceDefinition</td>
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
      <td>اگر 'true' باشد، خروجی به‌صورت خوانا (pretty-print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر اینکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست ادامه نمی‌یابد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل اجرای آزمایشی پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتِ انجام‌دهندهٔ این تغییرات مرتبط است. طول این مقدار باید حداکثر 128 نویسه باشد و فقط شامل نویسه‌های قابل چاپ، طبق تعریف https://golang.org/pkg/unicode/#IsPrint، باشد.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور اعلام می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که شامل فیلدهای ناشناخته یا تکراری هستند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق سرآیند استاندارد هشدار در پاسخ، یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در v1.23 و نسخه‌های بعدی است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest ناموفق می‌شود. خطایی که سرور بازمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری‌ای است که با آن‌ها مواجه شده است.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
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
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "custom-resource-definition-v1#CustomResourceDefinition" >}}">CustomResourceDefinition</a></em></td>
    </tr>
  </tbody>
</table>
