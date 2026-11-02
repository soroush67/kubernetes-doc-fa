---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "Endpoints"
content_type: "api_reference"
description: "Endpoints مجموعه‌ای از endpointهاست که سرویس واقعی را پیاده‌سازی می‌کنند. مثال:\n\n\t Name: &#34;mysvc&#34;,\n\t Subsets: [\n\t   {\n\t     Addresses: [{&#34;ip&#34;: &#34;10.10.1.1&#34;}, {&#34;ip&#34;: &#34;10.10.2.2&#34;}],\n\t     Ports: [{&#34;name&#34;: &#34;a&#34;, &#34;port&#34;: 8675}, {&#34;name&#34;: &#34;b&#34;, &#34;port&#34;: 309}]\n\t   },\n\t   {\n\t     Addresses: [{&#34;ip&#34;: &#34;10.10.3.3&#34;}],\n\t     Ports: [{&#34;name&#34;: &#34;a&#34;, &#34;port&#34;: 93}, {&#34;name&#34;: &#34;b&#34;, &#34;port&#34;: 76}]\n\t   },\n\t]\n\nEndpoints یک API قدیمی است و اطلاعات مربوط به همهٔ ویژگی‌های Service را در خود ندارد. برای دریافت اطلاعات کامل دربارهٔ endpointهای Service از discoveryv1.EndpointSlice استفاده کنید.\n\nمنسوخ‌شده: این API از نسخهٔ v1.33 به بعد منسوخ شده است. به‌جای آن از discoveryv1.EndpointSlice استفاده کنید."
title: "Endpoints"
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## Endpoints {#Endpoints}

Endpoints مجموعه‌ای از endpointهاست که سرویس واقعی را پیاده‌سازی می‌کنند. مثال:

	 Name: &#34;mysvc&#34;,
	 Subsets: [
	   {
	     Addresses: [{&#34;ip&#34;: &#34;10.10.1.1&#34;}, {&#34;ip&#34;: &#34;10.10.2.2&#34;}],
	     Ports: [{&#34;name&#34;: &#34;a&#34;, &#34;port&#34;: 8675}, {&#34;name&#34;: &#34;b&#34;, &#34;port&#34;: 309}]
	   },
	   {
	     Addresses: [{&#34;ip&#34;: &#34;10.10.3.3&#34;}],
	     Ports: [{&#34;name&#34;: &#34;a&#34;, &#34;port&#34;: 93}, {&#34;name&#34;: &#34;b&#34;, &#34;port&#34;: 76}]
	   },
	]

Endpoints یک API قدیمی است و اطلاعات مربوط به همهٔ ویژگی‌های Service را در خود ندارد. برای دریافت اطلاعات کامل دربارهٔ endpointهای Service از discoveryv1.EndpointSlice استفاده کنید.

منسوخ‌شده: این API از نسخهٔ v1.33 به بعد منسوخ شده است. به‌جای آن از discoveryv1.EndpointSlice استفاده کنید.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحوارهٔ نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از endpointی که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده‌های استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>subsets</code><br/><em><a href="{{< ref "#EndpointSubset" >}}">EndpointSubset array</a></em></td>
      <td>مجموعهٔ همهٔ endpointها برابر با اجتماع همهٔ subsetهاست. آدرس‌ها بر اساس IPهایی که به‌اشتراک می‌گذارند در subsetها قرار می‌گیرند. اگر یک آدرس چند پورت داشته باشد که برخی آماده و برخی ناآماده باشند (چون از کانتینرهای مختلف می‌آیند)، آن آدرس برای پورت‌های مختلف در subsetهای متفاوت نمایش داده می‌شود. هیچ آدرسی در یک subset نمی‌تواند هم در Addresses و هم در NotReadyAddresses ظاهر شود. مجموعه‌های آدرس و پورت که یک سرویس را تشکیل می‌دهند.</td>
    </tr>
  </tbody>
</table>


## EndpointsList {#EndpointsList}

EndpointsList فهرستی از endpointهاست. منسوخ‌شده: این API از نسخهٔ v1.33 به بعد منسوخ شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion طرحوارهٔ نسخه‌دار این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرحواره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints array</a></em></td>
      <td>فهرست endpointها.</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind یک مقدار رشته‌ای است که منبع REST مربوط به این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از endpointی که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. این فیلد قابل به‌روزرسانی نیست. به‌صورت CamelCase نوشته می‌شود. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده‌های استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## EndpointAddress {#EndpointAddress}

EndpointAddress یک چندتایی (tuple) است که یک آدرس IP منفرد را توصیف می‌کند. منسوخ‌شده: این API از نسخهٔ v1.33 به بعد منسوخ شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>hostname</code><br/><em>string</em></td>
      <td>نام میزبان (Hostname) این endpoint</td>
    </tr>
    <tr>
      <td><code>ip</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>آدرس IP این endpoint. نمی‌تواند آدرس loopback (‏127.0.0.0/8 یا ‎::1)، link-local (‏169.254.0.0/16 یا fe80::/10) یا link-local multicast (‏224.0.0.0/24 یا ff02::/16) باشد.</td>
    </tr>
    <tr>
      <td><code>nodeName</code><br/><em>string</em></td>
      <td>اختیاری: نودی که میزبان این endpoint است. از این مقدار می‌توان برای تعیین endpointهای محلی یک نود استفاده کرد.</td>
    </tr>
    <tr>
      <td><code>targetRef</code><br/><em><a href="{{< ref "../definitions/object-reference-v1#ObjectReference" >}}">ObjectReference</a></em></td>
      <td>ارجاع به آبجکتی که endpoint را فراهم می‌کند.</td>
    </tr>
  </tbody>
</table>


## EndpointPort {#EndpointPort}

EndpointPort یک چندتایی (tuple) است که یک پورت منفرد را توصیف می‌کند. منسوخ‌شده: این API از نسخهٔ v1.33 به بعد منسوخ شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>appProtocol</code><br/><em>string</em></td>
      <td>پروتکل کاربردی این پورت. این مقدار به‌عنوان یک راهنما برای پیاده‌سازی‌ها استفاده می‌شود تا برای پروتکل‌هایی که می‌شناسند رفتار غنی‌تری ارائه دهند. این فیلد از نحو استاندارد برچسب‌های کوبرنتیز پیروی می‌کند. مقادیر معتبر یکی از موارد زیر است:  * نام‌های پروتکل بدون پیشوند - این نام‌ها برای نام‌های استاندارد سرویس IANA رزرو شده‌اند (طبق RFC-6335 و https://www.iana.org/assignments/service-names).  * نام‌های پیشوندداری که کوبرنتیز تعریف کرده است:   * 'kubernetes.io/h2c' - HTTP/2 با آگاهی قبلی روی بستر متن‌ساده (cleartext) چنان‌که در https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior- شرح داده شده است.   * 'kubernetes.io/ws'  - WebSocket روی بستر متن‌ساده چنان‌که در https://www.rfc-editor.org/rfc/rfc6455 شرح داده شده است.   * 'kubernetes.io/wss' - WebSocket روی TLS چنان‌که در https://www.rfc-editor.org/rfc/rfc6455 شرح داده شده است.  * سایر پروتکل‌ها باید از نام‌های پیشوندداری استفاده کنند که پیاده‌سازی تعریف می‌کند، مانند mycompany.com/my-custom-protocol.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام این پورت. این نام باید با فیلد 'name' در ServicePort متناظر یکسان باشد. باید یک DNS_LABEL باشد. فقط در صورتی اختیاری است که تنها یک پورت تعریف شده باشد.</td>
    </tr>
    <tr>
      <td><code>port</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>شمارهٔ پورت endpoint.</td>
    </tr>
    <tr>
      <td><code>protocol</code><br/><em>string</em></td>
      <td>پروتکل IP این پورت. باید UDP، TCP یا SCTP باشد. مقدار پیش‌فرض TCP است.<br/><br/>مقادیر enum ممکن:<br/> - `"SCTP"` پروتکل SCTP است.<br/> - `"TCP"` پروتکل TCP است.<br/> - `"UDP"` پروتکل UDP است.</td>
    </tr>
  </tbody>
</table>


## EndpointSubset {#EndpointSubset}

EndpointSubset گروهی از آدرس‌ها با مجموعه‌ای مشترک از پورت‌هاست. مجموعهٔ بسط‌یافتهٔ endpointها برابر با حاصل‌ضرب دکارتی Addresses x Ports است. برای مثال، با فرض:

	{
	  Addresses: [{&#34;ip&#34;: &#34;10.10.1.1&#34;}, {&#34;ip&#34;: &#34;10.10.2.2&#34;}],
	  Ports:     [{&#34;name&#34;: &#34;a&#34;, &#34;port&#34;: 8675}, {&#34;name&#34;: &#34;b&#34;, &#34;port&#34;: 309}]
	}

مجموعهٔ endpointهای حاصل را می‌توان به‌این صورت دید:

	a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
	b: [ 10.10.1.1:309, 10.10.2.2:309 ]

منسوخ‌شده: این API از نسخهٔ v1.33 به بعد منسوخ شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>addresses</code><br/><em><a href="{{< ref "#EndpointAddress" >}}">EndpointAddress array</a></em></td>
      <td>آدرس‌های IP که پورت‌های مرتبطِ علامت‌گذاری‌شده به‌عنوان آماده را ارائه می‌دهند. استفادهٔ load balancerها و کلاینت‌ها از این endpointها ایمن در نظر گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>notReadyAddresses</code><br/><em><a href="{{< ref "#EndpointAddress" >}}">EndpointAddress array</a></em></td>
      <td>آدرس‌های IP که پورت‌های مرتبط را ارائه می‌دهند اما در حال حاضر به‌عنوان آماده علامت‌گذاری نشده‌اند، زیرا هنوز راه‌اندازی آن‌ها پایان نیافته است، اخیراً در بررسی آمادگی (readiness) ناموفق بوده‌اند یا اخیراً در بررسی زنده‌بودن (liveness) ناموفق بوده‌اند.</td>
    </tr>
    <tr>
      <td><code>ports</code><br/><em><a href="{{< ref "#EndpointPort" >}}">EndpointPort array</a></em></td>
      <td>شمارهٔ پورت‌هایی که روی آدرس‌های IP مرتبط در دسترس هستند.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /api/v1/namespaces/{namespace}/endpoints


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و حوزهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. مقدار نامعتبر یا ناشناختهٔ dryRun به یک پاسخ خطا می‌انجامد و درخواست دیگر پردازش نمی‌شود. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط است. طول مقدار باید کمتر از یا برابر با 128 کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ باشد، طبق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همهٔ فیلدهای ناشناخته را بی‌صدا از آبجکت حذف می‌کند و از فیلدهای تکراری فقط آخرین موردی را که رمزگشا (decoder) می‌بیند نگه می‌دارد. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این مقدار پیش‌فرض در v1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطایی که سرور برمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری یافت‌شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
      <td></td>
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
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /api/v1/namespaces/{namespace}/endpoints/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Endpoints</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و حوزهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. مقدار نامعتبر یا ناشناختهٔ dryRun به یک پاسخ خطا می‌انجامد و درخواست دیگر پردازش نمی‌شود. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط است. طول مقدار باید کمتر از یا برابر با 128 کاراکتر باشد و فقط شامل کاراکترهای قابل چاپ باشد، طبق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (‏application/apply-patch) الزامی است، اما برای انواع patch غیر apply (‏JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: همهٔ فیلدهای ناشناخته را بی‌صدا از آبجکت حذف می‌کند و از فیلدهای تکراری فقط آخرین موردی را که رمزگشا (decoder) می‌بیند نگه می‌دارد. این رفتار پیش‌فرض پیش از v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد درخواست همچنان موفق می‌شود و از فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این مقدار پیش‌فرض در v1.23 و بعد از آن است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطایی که سرور برمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری یافت‌شده است.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. به این معنا که کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است دوباره به دست می‌گیرد. برای درخواست‌های patch غیر apply نباید پرچم Force تنظیم شود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

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


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
  </tbody>
</table>

### `put` Replace

#### HTTP Request

PUT /api/v1/namespaces/{namespace}/endpoints/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Endpoints</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند محدوده برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا نهادی که این تغییرات را اعمال می‌کند اختصاص دارد. طول مقدار باید حداکثر ۱۲۸ نویسه باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور مشخص می‌کند که با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: هر فیلد ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شود نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین مورد دیده‌شده توسط رمزگشا نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخهٔ v1.23 بود. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. در صورت نبود خطای دیگر، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ماندگار می‌شود. این رفتار پیش‌فرض در نسخهٔ v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطایی که سرور برمی‌گرداند شامل همهٔ فیلدهای ناشناخته و تکراری شناسایی‌شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
      <td></td>
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
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete

#### HTTP Request

DELETE /api/v1/namespaces/{namespace}/endpoints/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Endpoints</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند محدوده برای تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ماندگار شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همهٔ مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه، پیش از آنکه آبجکت حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از مهلت پیش‌فرض (grace period) نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت تعیین می‌شود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) غیرقابل تبدیل بودن داده‌های آن، مثلاً در صورت شکست رمزگشایی، یا ب) ناتوانی در رمزگشایی به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد. نکته: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را مختل کند. فقط زمانی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true یا false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه شیوه‌ای. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص هر منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری است که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

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


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
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

### `delete` حذف مجموعه (Delete Collection)

#### درخواست HTTP

DELETE /api/v1/namespaces/{namespace}/endpoints


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینهٔ continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از یک کوئری قبلی را همراه با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از نو آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند؛ در این حالت سرور فهرستی را از کلید بعدی و اما از جدیدترین snapshot برمی‌گرداند که با نتایج فهرست قبلی ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ خواهند بود. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگشتی از سرور آغاز کنند، بدون آنکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست متوقف می‌گردد. مقادیر معتبر: - All: همهٔ مراحل dry run پردازش خواهند شد</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگشتی بر اساس فیلدهایشان. مقدار پیش‌فرض همهٔ آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان به ثانیه پیش از آنکه آبجکت باید حذف شود. مقدار باید عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، دورهٔ مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به‌ازای هر آبجکت تعیین می‌شود. صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع آغاز می‌شود. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) ناتوانی در تبدیل داده‌هایش، مثلاً شکست رمزگشایی، یا ب) ناتوانی در decode شدن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌سازی زیربنایی بازیابی کرد. توجه: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی پیش‌شرط‌ها را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید صراحتاً آن را فعال کند</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگشتی بر اساس برچسب‌هایشان. مقدار پیش‌فرض همهٔ آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده‌های فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعهٔ بعدی نتایج به کار برد. تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) برگرداند، در حالتی که همهٔ آبجکت‌های درخواستی فیلتر شوند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا خیر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همهٔ نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجهٔ دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگشتی هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی snapshot سازگار نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجهٔ بسیار بزرگ از limit استفاده می‌کند، همهٔ آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبهٔ اولین نتیجهٔ فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخهٔ 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا و چگونه garbage collection انجام شود. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مخصوص هر منبع تعیین می‌شود. مقادیر قابل قبول: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - سیاستی آبشاری که همهٔ وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی روی نسخه‌های منبعی تعیین می‌کند که یک درخواست می‌تواند از آن‌ها پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه دهد. پس از ارسال همهٔ این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعهٔ آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. هنگامی که گزینهٔ `sendInitialEvents` تنظیم شده باشد، لازم است گزینهٔ `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - `resourceVersionMatch` = NotOlderThan   به معنای «داده‌ای که دست‌کم به‌روز بودن `resourceVersion` ارائه‌شده را داشته باشد» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion` دست‌کم به‌تازگی مقدار ارائه‌شده در ListOptions همگام شده باشد.   اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظهٔ آغاز پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد،   خطای Invalid برگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلیل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگشتی را با یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای تعیین یک یا چند بازهٔ hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو آبجکت‌محور به سبک CEL (مثلاً "object.metadata.uid") پیروی می‌کند، نه قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal تک‌نقل‌قولی CEL با پیشوند '0x' هستند و کران پایین (شامل) و کران بالا (غیرشامل) را روی فضای hash ۶۴ بیتی FNV-1a تعریف می‌کنند. بازهٔ کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را محدود می‌کند، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت.</td>
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


### `get` خواندن (Read)

#### درخواست HTTP

GET /api/v1/namespaces/{namespace}/endpoints/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Endpoints</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدودهٔ احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا و مرتب چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
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
      <td><em><a href="{{< ref "endpoints-v1#Endpoints" >}}">Endpoints</a></em></td>
    </tr>
  </tbody>
</table>

### `get` List

#### HTTP Request

GET /api/v1/namespaces/{namespace}/endpoints


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
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
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا و مرتب (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد که درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch از نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند، و ارسال bookmarkها به صلاح‌دید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند و نیز نباید فرض کنند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک پرسمان قبلی و با پارامترهای پرسمان یکسان (به‌جز مقدار continue) استفاده کنند، و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور فهرستی را از کلید بعدی و از آخرین snapshot برمی‌گرداند که با نتایج فهرست قبلی ناسازگار است. آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، ویرایش یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد در صورتی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرسمان اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تنظیم limit ممکن است در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، کمتر از تعداد درخواستی آیتم (حتی صفر آیتم) برگرداند؛ بنابراین کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر، فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد در صورتی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، ویرایش یا حذف شده باشد، در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌کند درخواست از چه نسخه‌های منبعی ممکن است پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را بازتولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` = NotOlderThan   به‌معنای «داده‌هایی دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به تازگی مقدار ارائه‌شده در ListOptions است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود.  اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به‌دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و نه از قالب fieldSelector ("metadata.uid"). مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL و داخل تک‌نقل‌قول هستند و پیشوند '0x' دارند؛ این دو به‌ترتیب کران پایین (شامل) و کران بالا (غیرشامل) را در فضای هش FNV-1a ۶۴ بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای غیرشامل آن برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ شارد:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ شارد:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی فهرست/watch. این مقدار مدت زمان فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "endpoints-v1#EndpointsList" >}}">EndpointsList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` فهرست‌کردن همه فضاهای نام (namespace)

#### درخواست HTTP

GET /api/v1/endpoints



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند و همچنین نباید فرض کنند که سرور در طول یک نشست حتماً رویدادی از نوع BOOKMARK ارسال می‌کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی استفاده کنند که پارامترهای آن (به‌جز مقدار continue) دقیقاً یکسان باشند، و سرور می‌تواند مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌کردن را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است؛ آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، اصلاح یا حذف شده‌اند تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ می‌آیند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌هاست.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌هاست.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی مورد بازگرداند (حتی صفر مورد) و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، اصلاح یا حذف شده باشد، در درخواست‌های بعدیِ ادامه‌دار گنجانده نمی‌شود. به این حالت گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلایننتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست تکه‌تکه (chunked) به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که هنگام محاسبه نتیجه اول فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی برای نسخه‌های منبعی تعیین می‌کند که درخواست می‌تواند از آن‌ها پاسخ داده شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch متناظر با تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا یک `resourceVersion` همان‌قدر جدید با مقدار ارائه‌شده در ListOptions همگام شده باشد. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» (consistent read) تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (OR منطقی) برای مشخص کردن یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL با تک‌نقل‌قول و پیشوند '0x' هستند و کران پایین شمول‌پذیر (inclusive) و کران بالای شمول‌ناپذیر (exclusive) را در فضای هش 64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شمول‌ناپذیر برابر 2^64 است.  مثال‌ها:   تقسیم به 2 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد در مرحله آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت زمان فراخوانی را، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت، محدود می‌کند.</td>
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
      <td><em><a href="{{< ref "endpoints-v1#EndpointsList" >}}">EndpointsList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### HTTP Request

GET /api/v1/watch/namespaces/{namespace}/endpoints/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Endpoints</td>
    </tr>
    <tr>
      <td><code>namespace</code></td>
      <td><em>string</em></td>
      <td>نام آبجکت و محدوده احراز هویت، مانند تیم‌ها و پروژه‌ها</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>مقدار allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی برگردانده می‌شوند و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز خود مقدار continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک توکن continue پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از «کلید بعدی» شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>مقدار limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر موارد بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی مورد برگرداند (حتی صفر مورد)، و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به حضور فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در آن صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. گاهی به این ویژگی «snapshot سازگار» گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین یک فهرست‌گیری بخش‌بخش به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>مقدار resourceVersion محدودیتی تعیین می‌کند که یک درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>مقدار resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های موجود در مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به شکل `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، تنظیم گزینه `resourceVersionMatch` نیز الزامی است. معنای درخواست watch به این صورت است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌صورت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>مقدار shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت انتخابگر shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به همراه || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (برای مثال "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") استفاده نمی‌کنند. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌کوتیشن قرار می‌گیرند و پیشوند '0x' دارند؛ آن‌ها کران پایین شمول‌پذیر و کران بالای شمول‌ناپذیر را روی فضای هش FNV-1a ۶۴ بیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شمول‌ناپذیر برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را محدود می‌کند، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
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
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List

#### درخواست HTTP

GET /api/v1/watch/namespaces/{namespace}/endpoints


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


#### پارامترهای پرس‌وجو

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch از نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی ارسال می‌شوند و نیز نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue حاصل از نتیجه یک پرس‌وجوی قبلی را با پارامترهای پرس‌وجوی یکسان (به‌جز مقدار continue) استفاده کنند و سرور می‌تواند مقدار continueای را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، خواه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) یا تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از «کلید بعدی» آغاز می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است آغاز کنند و هیچ تغییری را از دست ندهند.</td>
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
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرس‌وجوی اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم برگرداند (حتی صفر آیتم)، و کلاینت‌ها باید برای تشخیص وجود نتایج بیشتر فقط به حضور فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را برمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که مشخص می‌سازد درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های مجموعه را تولید کند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از RV) را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، گزینه `resourceVersionMatch` نیز باید تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلیل سازگاری با نسخه‌های قبلی) true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخابگر شارد مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده فعلی:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌نقل‌قول قرار می‌گیرند و پیشوند '0x' دارند؛ این مقادیر کران پایین شامل‌شونده و کران بالای شامل‌نشونده را در فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به 2 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 شارد:     شارد 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     شارد 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     شارد 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     شارد 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch فعال شود.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت زمان فراخوانی را بدون توجه به فعالیت یا عدم فعالیت محدود می‌کند.</td>
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

### `get` مشاهده فهرست در همه فضاهای نام (Watch List All Namespaces)

#### درخواست HTTP

GET /api/v1/watch/endpoints



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند که رویدادهای watch از نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی ارسال می‌شوند و نیز نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار خود continue) استفاده کنند و سرور می‌تواند مقداری را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی سرور، سرور با خطای 410 ResourceExpired همراه با یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از آخرین snapshot گرفته شده است و با نتایج قبلی فهرست ناسازگار است: آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور شروع کنند، بدون اینکه هیچ تغییری را از دست بدهند.</td>
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
      <td>limit حداکثر تعداد پاسخ‌هایی است که برای یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی consistent snapshot گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) چاپ می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد از مرورگر یا ابزار HTTP خط فرمان (curl و wget) استفاده شده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از چه نسخه‌هایی از منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده (unset) است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌طور معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از آن RV) را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شده باشد، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به تازگی `resourceVersion` ارائه‌شده باشد»، و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار (consistent read)» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم‌نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت انتخاب shard مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر منطقی OR) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و قالب fieldSelector ("metadata.uid") را به کار نمی‌برد. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های لیترال CEL داخل single-quote با پیشوند '0x' هستند و کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای هش FNV-1a شصت‌وچهاربیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و برای استفاده از آن باید feature gate با نام ShardedListAndWatch فعال شود.</td>
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
