---
title: پیکربندی kube-apiserver (v1alpha1)
content_type: tool-reference
package: apiserver.k8s.io/v1alpha1
auto_generated: true
---
<p>بسته v1alpha1 نسخه v1alpha1 از API است.</p>


## انواع منابع 


- [AdmissionConfiguration](#apiserver-k8s-io-v1alpha1-AdmissionConfiguration)
- [AuthenticationConfiguration](#apiserver-k8s-io-v1alpha1-AuthenticationConfiguration)
- [AuthorizationConfiguration](#apiserver-k8s-io-v1alpha1-AuthorizationConfiguration)
- [EgressSelectorConfiguration](#apiserver-k8s-io-v1alpha1-EgressSelectorConfiguration)
- [TracingConfiguration](#apiserver-k8s-io-v1alpha1-TracingConfiguration)
  
    
    

## `TracingConfiguration`     {#TracingConfiguration}
    

**ظاهر می‌شود در:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

- [TracingConfiguration](#apiserver-k8s-io-v1alpha1-TracingConfiguration)


<p>TracingConfiguration پیکربندی نسخه‌بندی‌شده‌ای را برای کلاینت‌های ردیابی (tracing) OpenTelemetry فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>نقطه پایانی (endpoint) کالکتوری که این مؤلفه ردیابی‌ها را به آن گزارش می‌دهد.
اتصال ناامن است و در حال حاضر از TLS پشتیبانی نمی‌کند.
توصیه می‌شود این مقدار تنظیم نشود و endpoint همان مقدار پیش‌فرض otlp grpc، یعنی localhost:4317، باشد.</p>
</td>
</tr>
<tr><td><code>samplingRatePerMillion</code><br/>
<code>int32</code>
</td>
<td>
   <p>SamplingRatePerMillion تعداد نمونه‌هایی است که به ازای هر یک میلیون span جمع‌آوری می‌شود.
توصیه می‌شود این مقدار تنظیم نشود. اگر تنظیم نشود، نمونه‌بردار (sampler) از نرخ نمونه‌برداری
span والد خود پیروی می‌کند و در غیر این صورت هرگز نمونه‌برداری نمی‌کند.</p>
</td>
</tr>
</tbody>
</table>
  

## `AdmissionConfiguration`     {#apiserver-k8s-io-v1alpha1-AdmissionConfiguration}
    


<p>AdmissionConfiguration پیکربندی نسخه‌بندی‌شده‌ای را برای admission controllerها فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AdmissionConfiguration</code></td></tr>
    
  
<tr><td><code>plugins</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-AdmissionPluginConfiguration"><code>[]AdmissionPluginConfiguration</code></a>
</td>
<td>
   <p>Plugins امکان تعیین یک پیکربندی برای هر افزونه admission control را فراهم می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `AuthenticationConfiguration`     {#apiserver-k8s-io-v1alpha1-AuthenticationConfiguration}
    


<p>AuthenticationConfiguration پیکربندی نسخه‌بندی‌شده‌ای را برای احراز هویت فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AuthenticationConfiguration</code></td></tr>
    
  
<tr><td><code>jwt</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-JWTAuthenticator"><code>[]JWTAuthenticator</code></a>
</td>
<td>
   <p>jwt فهرستی از احراز‌هویت‌کننده‌ها (authenticator) است که کاربران کوبرنتیز را با استفاده از
توکن‌های سازگار با JWT احراز هویت می‌کنند. احراز‌هویت‌کننده تلاش می‌کند یک توکن ID خام را تجزیه کند
و بررسی کند که توسط issuer پیکربندی‌شده امضا شده باشد. کلید عمومی لازم برای تأیید
امضا با استفاده از OIDC discovery از نقطه پایانی عمومی issuer کشف می‌شود.
برای هر توکن ورودی، هر احراز‌هویت‌کننده JWT به ترتیبی که در این فهرست مشخص شده است
آزموده می‌شود. توجه داشته باشید که
سایر احراز‌هویت‌کننده‌ها ممکن است پیش از احراز‌هویت‌کننده‌های JWT یا پس از آن‌ها اجرا شوند.
جایگاه دقیق احراز‌هویت‌کننده‌های JWT نسبت به سایر
احراز‌هویت‌کننده‌ها نه تعریف شده است و نه در نسخه‌های مختلف پایدار است. از آنجا که
هر احراز‌هویت‌کننده JWT باید نشانی issuer یکتایی داشته باشد، حداکثر یک
احراز‌هویت‌کننده JWT تلاش می‌کند توکن را به‌صورت رمزنگاشتی اعتبارسنجی کند.</p>
<p>حداقل بار (payload) معتبر JWT باید شامل claimهای زیر باشد:
{
&quot;iss&quot;: &quot;https://issuer.example.com&quot;,
&quot;aud&quot;: [&quot;audience&quot;],
&quot;exp&quot;: 1234567890,
&quot;<!-- raw HTML omitted -->&quot;: &quot;username&quot;
}</p>
</td>
</tr>
<tr><td><code>anonymous</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-AnonymousAuthConfig"><code>AnonymousAuthConfig</code></a>
</td>
<td>
   <p>در صورت وجود، نباید --anonymous-auth تنظیم شده باشد</p>
</td>
</tr>
</tbody>
</table>

## `AuthorizationConfiguration`     {#apiserver-k8s-io-v1alpha1-AuthorizationConfiguration}
    



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AuthorizationConfiguration</code></td></tr>
    
  
<tr><td><code>authorizers</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-AuthorizerConfiguration"><code>[]AuthorizerConfiguration</code></a>
</td>
<td>
   <p>Authorizers فهرستی مرتب از مجوزدهنده‌ها (authorizer) است که درخواست‌ها
بر اساس آن‌ها مجاز شمرده می‌شوند.
این مورد مشابه فلگ --authorization-modes در kube-apiserver است.
باید حداقل یک مورد وجود داشته باشد.</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelectorConfiguration`     {#apiserver-k8s-io-v1alpha1-EgressSelectorConfiguration}
    


<p>EgressSelectorConfiguration پیکربندی نسخه‌بندی‌شده‌ای را برای کلاینت‌های egress selector فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>EgressSelectorConfiguration</code></td></tr>
    
  
<tr><td><code>egressSelections</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-EgressSelection"><code>[]EgressSelection</code></a>
</td>
<td>
   <p>connectionServices شامل فهرستی از پیکربندی‌های کلاینت egress selection است</p>
</td>
</tr>
</tbody>
</table>

## `TracingConfiguration`     {#apiserver-k8s-io-v1alpha1-TracingConfiguration}
    


<p>TracingConfiguration پیکربندی نسخه‌بندی‌شده‌ای را برای کلاینت‌های ردیابی (tracing) فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>TracingConfiguration</code></td></tr>
    
  
<tr><td><code>TracingConfiguration</code> <B>[الزامی]</B><br/>
<a href="#TracingConfiguration"><code>TracingConfiguration</code></a>
</td>
<td>
   <p>ساختار (struct) پیکربندی ردیابی پیکربندی مؤلفه را در خود جای می‌دهد</p>
</td>
</tr>
</tbody>
</table>

## `AdmissionPluginConfiguration`     {#apiserver-k8s-io-v1alpha1-AdmissionPluginConfiguration}
    

**ظاهر می‌شود در:**

- [AdmissionConfiguration](#apiserver-k8s-io-v1alpha1-AdmissionConfiguration)


<p>AdmissionPluginConfiguration پیکربندی یک افزونه (plug-in) واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام admission controller است.
باید با نام افزونه admission ثبت‌شده مطابقت داشته باشد.</p>
</td>
</tr>
<tr><td><code>path</code><br/>
<code>string</code>
</td>
<td>
   <p>Path مسیر فایل پیکربندی‌ای است که شامل پیکربندی
افزونه است</p>
</td>
</tr>
<tr><td><code>configuration</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Unknown"><code>k8s.io/apimachinery/pkg/runtime.Unknown</code></a>
</td>
<td>
   <p>Configuration یک آبجکت پیکربندی نهفته است که به‌عنوان پیکربندی افزونه به کار می‌رود.
در صورت وجود، به‌جای مسیر فایل پیکربندی از آن استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `AnonymousAuthCondition`     {#apiserver-k8s-io-v1alpha1-AnonymousAuthCondition}
    

**ظاهر می‌شود در:**

- [AnonymousAuthConfig](#apiserver-k8s-io-v1alpha1-AnonymousAuthConfig)


<p>AnonymousAuthCondition شرطی را توصیف می‌کند که تحت آن احراز هویت ناشناس
باید فعال شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>path</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>مسیری که احراز هویت ناشناس برای آن فعال است.</p>
</td>
</tr>
</tbody>
</table>

## `AnonymousAuthConfig`     {#apiserver-k8s-io-v1alpha1-AnonymousAuthConfig}
    

**ظاهر می‌شود در:**

- [AuthenticationConfiguration](#apiserver-k8s-io-v1alpha1-AuthenticationConfiguration)


<p>AnonymousAuthConfig پیکربندی احراز‌هویت‌کننده ناشناس را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>enabled</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>conditions</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-AnonymousAuthCondition"><code>[]AnonymousAuthCondition</code></a>
</td>
<td>
   <p>در صورت تنظیم، احراز هویت ناشناس تنها زمانی مجاز است که درخواست یکی از
شرط‌ها را برآورده کند.</p>
</td>
</tr>
</tbody>
</table>

## `AudienceMatchPolicyType`     {#apiserver-k8s-io-v1alpha1-AudienceMatchPolicyType}
    
(نام مستعار برای `string`)

**ظاهر می‌شود در:**

- [Issuer](#apiserver-k8s-io-v1alpha1-Issuer)


<p>AudienceMatchPolicyType مجموعه‌ای از مقادیر معتبر برای issuer.audienceMatchPolicy است</p>




## `AuthorizerConfiguration`     {#apiserver-k8s-io-v1alpha1-AuthorizerConfiguration}
    

**ظاهر می‌شود در:**

- [AuthorizationConfiguration](#apiserver-k8s-io-v1alpha1-AuthorizationConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Type به نوع مجوزدهنده (authorizer) اشاره دارد.
&quot;Webhook&quot; در API server عمومی پشتیبانی می‌شود.
سایر API serverها ممکن است از انواع مجوزدهنده دیگری
مانند Node، RBAC، ABAC و غیره پشتیبانی کنند.</p>
</td>
</tr>
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name برای توصیف webhook به کار می‌رود.
این نام به‌صراحت در سازوکار پایش برای متریک‌ها استفاده می‌شود.
نکته: نام‌ها باید برچسب‌های DNS1123 مانند <code>myauthorizername</code> یا
زیردامنه‌هایی مانند <code>myauthorizer.example.domain</code> باشند.
الزامی است و مقدار پیش‌فرض ندارد</p>
</td>
</tr>
<tr><td><code>webhook</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-WebhookConfiguration"><code>WebhookConfiguration</code></a>
</td>
<td>
   <p>Webhook پیکربندی یک مجوزدهنده Webhook را تعریف می‌کند.
در صورتی که Type=Webhook باشد باید تعریف شود.
در صورتی که Type!=Webhook باشد نباید تعریف شود.</p>
</td>
</tr>
</tbody>
</table>

## `ClaimMappings`     {#apiserver-k8s-io-v1alpha1-ClaimMappings}
    

**ظاهر می‌شود در:**

- [JWTAuthenticator](#apiserver-k8s-io-v1alpha1-JWTAuthenticator)


<p>ClaimMappings پیکربندی نگاشت claim را فراهم می‌کند</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>username</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-PrefixedClaimOrExpression"><code>PrefixedClaimOrExpression</code></a>
</td>
<td>
   <p>username یک گزینه برای ویژگی نام کاربری را نشان می‌دهد.
مقدار claim باید یک رشته منفرد باشد.
معادل فلگ‌های --oidc-username-claim و --oidc-username-prefix است.
اگر username.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای تولید کند.
اگر username.expression از 'claims.email' استفاده کند، آنگاه 'claims.email_verified' باید در
username.expression یا extra[<em>].valueExpression یا claimValidationRules[</em>].expression استفاده شود.
نمونه‌ای از عبارت قاعده اعتبارسنجی claim که با اعتبارسنجی خودکارِ اعمال‌شده
هنگام تنظیم username.claim روی 'email' مطابقت دارد، عبارت 'claims.?email_verified.orValue(true) == true' است. با مقایسه صریح
مقدار با true، اجازه می‌دهیم type-checking ببیند که نتیجه یک مقدار بولی خواهد بود، و اطمینان حاصل می‌کنیم که
claim غیربولی email_verified در زمان اجرا شناسایی شود.</p>
<p>در رویکرد مبتنی بر فلگ، فلگ‌های --oidc-username-claim و --oidc-username-prefix اختیاری هستند. اگر --oidc-username-claim تنظیم نشده باشد،
مقدار پیش‌فرض &quot;sub&quot; است. در پیکربندی احراز هویت، برای claim یا prefix مقدار پیش‌فرضی وجود ندارد. claim و prefix باید به‌صراحت تنظیم شوند.
برای claim، اگر در رویکرد قدیمی مبتنی بر فلگ، --oidc-username-claim تنظیم نشده بود، در پیکربندی احراز هویت username.claim=&quot;sub&quot; را تنظیم کنید.
برای prefix:
(1) --oidc-username-prefix=&quot;-&quot;: هیچ پیشوندی به نام کاربری افزوده نمی‌شد. برای رفتار یکسان با استفاده از پیکربندی احراز هویت،
username.prefix=&quot;&quot; را تنظیم کنید
(2) --oidc-username-prefix=&quot;&quot; و --oidc-username-claim != &quot;email&quot;: پیشوند &quot;&lt;value of --oidc-issuer-url&gt;#&quot; بود. برای
رفتار یکسان با استفاده از پیکربندی احراز هویت، username.prefix=&quot;<!-- raw HTML omitted -->#&quot; را تنظیم کنید
(3) --oidc-username-prefix=&quot;<!-- raw HTML omitted -->&quot;: برای رفتار یکسان با استفاده از پیکربندی احراز هویت، username.prefix=&quot;<!-- raw HTML omitted -->&quot; را تنظیم کنید</p>
</td>
</tr>
<tr><td><code>groups</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-PrefixedClaimOrExpression"><code>PrefixedClaimOrExpression</code></a>
</td>
<td>
   <p>groups یک گزینه برای ویژگی گروه‌ها را نشان می‌دهد.
مقدار claim باید یک رشته یا آرایه‌ای از رشته‌ها باشد.
اگر groups.claim تنظیم شده باشد، prefix باید مشخص شود (و می‌تواند رشته خالی باشد).
اگر groups.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای یا آرایه‌ای از رشته‌ها تولید کند.
مقادیر &quot;&quot;، [] و null به‌منزله نبود نگاشت گروه در نظر گرفته می‌شوند.</p>
</td>
</tr>
<tr><td><code>uid</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-ClaimOrExpression"><code>ClaimOrExpression</code></a>
</td>
<td>
   <p>uid یک گزینه برای ویژگی uid را نشان می‌دهد.
claim باید یک claim رشته‌ای منفرد باشد.
اگر uid.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای تولید کند.</p>
</td>
</tr>
<tr><td><code>extra</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-ExtraMapping"><code>[]ExtraMapping</code></a>
</td>
<td>
   <p>extra یک گزینه برای ویژگی extra را نشان می‌دهد.
expression باید یک مقدار رشته‌ای یا آرایه‌ای از رشته‌ها تولید کند.
اگر مقدار خالی باشد، نگاشت extra وجود نخواهد داشت.</p>
<p>کلید/مقدار extra با مقدار ثابت (hard-coded)</p>
<ul>
<li>key: &quot;foo&quot;
valueExpression: &quot;'bar'&quot;
این به یک ویژگی extra با مقدار foo: [&quot;bar&quot;] منجر می‌شود</li>
</ul>
<p>کلید ثابت، با مقداری که از روی مقدار claim کپی می‌شود</p>
<ul>
<li>key: &quot;foo&quot;
valueExpression: &quot;claims.some_claim&quot;
این به یک ویژگی extra با مقدار foo: [value of some_claim] منجر می‌شود</li>
</ul>
<p>کلید ثابت، با مقداری که از مقدار claim استخراج می‌شود</p>
<ul>
<li>key: &quot;admin&quot;
valueExpression: '(has(claims.is_admin) &amp;&amp; claims.is_admin) ? &quot;true&quot;:&quot;&quot;'
این به نتایج زیر منجر می‌شود:</li>
<li>اگر claim با نام is_admin وجود داشته باشد و true باشد، ویژگی extra با مقدار admin: [&quot;true&quot;]</li>
<li>اگر claim با نام is_admin وجود داشته باشد و false باشد یا اصلاً وجود نداشته باشد، هیچ ویژگی extra افزوده نخواهد شد</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `ClaimOrExpression`     {#apiserver-k8s-io-v1alpha1-ClaimOrExpression}
    

**ظاهر می‌شود در:**

- [ClaimMappings](#apiserver-k8s-io-v1alpha1-ClaimMappings)


<p>ClaimOrExpression پیکربندی یک claim یا عبارت واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim همان claim در JWT است که باید استفاده شود.
یا claim یا expression باید تنظیم شود.
با expression ناسازگار (mutually exclusive) است.</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب یک متغیر CEL سازماندهی شده‌اند:</p>
<ul>
<li>'claims' نگاشتی (map) از نام claimها به مقادیر claimهاست.
برای مثال، متغیری به نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نمادگذاری نقطه‌ای، مثلاً 'claims.foo.bar'، در دسترس قرار داد.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim ناسازگار (mutually exclusive) است.</p>
</td>
</tr>
</tbody>
</table>

## `ClaimValidationRule`     {#apiserver-k8s-io-v1alpha1-ClaimValidationRule}
    

**ظاهر می‌شود در:**

- [JWTAuthenticator](#apiserver-k8s-io-v1alpha1-JWTAuthenticator)


<p>ClaimValidationRule پیکربندی یک قاعده اعتبارسنجی claim واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim نام یک claim الزامی است.
معادل فلگ --oidc-required-claim است.
فقط کلیدهای claim از نوع رشته پشتیبانی می‌شوند.
با expression و message ناسازگار (mutually exclusive) است.</p>
</td>
</tr>
<tr><td><code>requiredValue</code><br/>
<code>string</code>
</td>
<td>
   <p>requiredValue مقدار یک claim الزامی است.
معادل فلگ --oidc-required-claim است.
فقط مقادیر claim از نوع رشته پشتیبانی می‌شوند.
اگر claim تنظیم شده باشد و requiredValue تنظیم نشده باشد، claim باید با مقداری برابر با رشته خالی وجود داشته باشد.
با expression و message ناسازگار (mutually exclusive) است.</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد.
باید یک مقدار بولی تولید کند.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب یک متغیر CEL سازماندهی شده‌اند:</p>
<ul>
<li>'claims' نگاشتی (map) از نام claimها به مقادیر claimهاست.
برای مثال، متغیری به نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نمادگذاری نقطه‌ای، مثلاً 'claims.foo.bar'، در دسترس قرار داد.
برای موفقیت اعتبارسنجی باید true برگرداند.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim و requiredValue ناسازگار (mutually exclusive) است.</p>
</td>
</tr>
<tr><td><code>message</code><br/>
<code>string</code>
</td>
<td>
   <p>message پیام خطای بازگردانده‌شده را زمانی که expression مقدار false برگرداند سفارشی می‌کند.
message یک رشته لفظی (literal) است.
با claim و requiredValue ناسازگار (mutually exclusive) است.</p>
</td>
</tr>
</tbody>
</table>

## `Connection`     {#apiserver-k8s-io-v1alpha1-Connection}
    

**ظاهر می‌شود در:**

- [EgressSelection](#apiserver-k8s-io-v1alpha1-EgressSelection)


<p>Connection پیکربندی یک کلاینت egress selection واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>proxyProtocol</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-ProtocolType"><code>ProtocolType</code></a>
</td>
<td>
   <p>Protocol پروتکلی است که برای اتصال از کلاینت به سرور konnectivity استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>transport</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-Transport"><code>Transport</code></a>
</td>
<td>
   <p>Transport پیکربندی‌های انتقال (transport) را تعریف می‌کند که برای برقراری ارتباط با سرور konnectivity به کار می‌روند.
اگر ProxyProtocol برابر HTTPConnect یا GRPC باشد، این فیلد الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelection`     {#apiserver-k8s-io-v1alpha1-EgressSelection}
    

**ظاهر شده در:**

- [EgressSelectorConfiguration](#apiserver-k8s-io-v1alpha1-EgressSelectorConfiguration)


<p>EgressSelection پیکربندی یک کلاینت انتخاب خروجی (egress) واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام انتخاب خروجی (egress selection) است.
مقادیر پشتیبانی‌شده در حال حاضر عبارت‌اند از &quot;controlplane&quot;، &quot;master&quot;، &quot;etcd&quot; و &quot;cluster&quot;.
انتخابگر خروجی &quot;master&quot; منسوخ شده و به‌جای آن باید از &quot;controlplane&quot; استفاده شود.</p>
</td>
</tr>
<tr><td><code>connection</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-Connection"><code>Connection</code></a>
</td>
<td>
   <p>connection اطلاعات دقیقی است که برای پیکربندی انتخاب خروجی (egress selection) به کار می‌رود.</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelectorType`     {#apiserver-k8s-io-v1alpha1-EgressSelectorType}
    
(نام مستعار برای `string`)

**ظاهر شده در:**

- [Issuer](#apiserver-k8s-io-v1alpha1-Issuer)


<p>EgressSelectorType نشان‌دهنده این است که برای ارسال ترافیک باید از کدام انتخاب خروجی (egress selection) استفاده شود.</p>




## `ExtraMapping`     {#apiserver-k8s-io-v1alpha1-ExtraMapping}
    

**ظاهر شده در:**

- [ClaimMappings](#apiserver-k8s-io-v1alpha1-ClaimMappings)


<p>ExtraMapping پیکربندی یک نگاشت اضافی (extra mapping) واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>key</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>key رشته‌ای است که به‌عنوان کلید ویژگی اضافی (extra attribute) به کار می‌رود.
key باید یک مسیر با پیشوند دامنه باشد (برای مثال example.org/foo). تمام نویسه‌های پیش از اولین &quot;/&quot; باید یک
زیردامنه معتبر مطابق RFC 1123 باشند. تمام نویسه‌های پس از اولین &quot;/&quot; باید
نویسه‌های معتبر مسیر HTTP مطابق RFC 3986 باشند.
key باید با حروف کوچک نوشته شود.
یکتا بودن آن الزامی است.</p>
</td>
</tr>
<tr><td><code>valueExpression</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>valueExpression یک عبارت CEL برای استخراج مقدار ویژگی اضافی است.
valueExpression باید یک مقدار رشته‌ای یا آرایه‌ای از رشته‌ها تولید کند.
مقادیر &quot;&quot;، [] و null به‌منزله نبودن نگاشت اضافی در نظر گرفته می‌شوند.
مقادیر رشته‌ای خالی موجود در یک آرایه رشته‌ای حذف می‌شوند.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب یک متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر آن‌هاست.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مانند 'claims.foo.bar'.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
</tbody>
</table>

## `Issuer`     {#apiserver-k8s-io-v1alpha1-Issuer}
    

**ظاهر شده در:**

- [JWTAuthenticator](#apiserver-k8s-io-v1alpha1-JWTAuthenticator)


<p>Issuer پیکربندی تنظیمات خاص یک ارائه‌دهنده خارجی را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>url</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>url به نشانی صادرکننده (issuer) با قالب https://url یا https://url/path اشاره می‌کند.
این مقدار باید با claim با نام &quot;iss&quot; در JWT ارائه‌شده و با issuer بازگردانده‌شده از discovery مطابقت داشته باشد.
مقدار آن همان مقدار پرچم --oidc-issuer-url است.
اطلاعات discovery از &quot;{url}/.well-known/openid-configuration&quot; دریافت می‌شود، مگر اینکه با discoveryURL بازنویسی شده باشد.
یکتا بودن آن در میان همه JWT authenticatorها الزامی است.
توجه داشته باشید که پیکربندی انتخاب خروجی (egress selection) برای این اتصال شبکه استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>discoveryURL</code><br/>
<code>string</code>
</td>
<td>
   <p>discoveryURL، در صورت تعیین، نشانی مورد استفاده برای دریافت اطلاعات discovery را
به‌جای &quot;{url}/.well-known/openid-configuration&quot; بازنویسی می‌کند.
مقدار دقیقاً همان‌گونه که مشخص شده استفاده می‌شود، بنابراین در صورت نیاز باید
&quot;/.well-known/openid-configuration&quot; در discoveryURL گنجانده شود.</p>
<p>فیلد &quot;issuer&quot; در اطلاعات discovery دریافت‌شده باید با فیلد &quot;issuer.url&quot;
در AuthenticationConfiguration مطابقت داشته باشد و برای اعتبارسنجی claim با نام &quot;iss&quot; در JWT ارائه‌شده به کار می‌رود.
این گزینه برای سناریوهایی است که در آن‌ها نقاط پایانی well-known و jwks در مکانی متفاوت
از issuer میزبانی می‌شوند (مانند میزبانی محلی در کلاستر).</p>
<p>مثال:
نشانی discovery که با استفاده از Service کوبرنتیز با نام 'oidc' در فضای نام (namespace) 'oidc-namespace' در دسترس قرار گرفته
و اطلاعات discovery در '/.well-known/openid-configuration' موجود است.
discoveryURL: &quot;https://oidc.oidc-namespace/.well-known/openid-configuration&quot;
certificateAuthority برای تأیید اتصال TLS به کار می‌رود و نام میزبان (hostname) روی گواهی برگ (leaf certificate)
باید روی 'oidc.oidc-namespace' تنظیم شده باشد.</p>
<p>curl https://oidc.oidc-namespace/.well-known/openid-configuration (.discoveryURL field)
{
issuer: &quot;https://oidc.example.com&quot; (.url field)
}</p>
<p>discoveryURL باید با url متفاوت باشد.
یکتا بودن آن در میان همه JWT authenticatorها الزامی است.
توجه داشته باشید که پیکربندی انتخاب خروجی (egress selection) برای این اتصال شبکه استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>certificateAuthority</code><br/>
<code>string</code>
</td>
<td>
   <p>certificateAuthority شامل گواهی‌های مرجع صدور گواهی (certificate authority) با کدگذاری PEM است
که برای اعتبارسنجی اتصال هنگام دریافت اطلاعات discovery استفاده می‌شود.
در صورت تنظیم‌نشدن، از تأییدکننده سیستم (system verifier) استفاده می‌شود.
مقدار آن همان محتوای فایلی است که پرچم --oidc-ca-file به آن اشاره می‌کند.</p>
</td>
</tr>
<tr><td><code>audiences</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>audiences مجموعه مخاطبان (audience) قابل‌قبولی است که JWT باید برای آن‌ها صادر شده باشد.
حداقل یکی از ورودی‌ها باید با claim با نام &quot;aud&quot; در JWTهای ارائه‌شده مطابقت داشته باشد.
مقدار آن همان مقدار پرچم --oidc-client-id است (البته این فیلد از آرایه پشتیبانی می‌کند).
باید غیرخالی باشد.</p>
</td>
</tr>
<tr><td><code>audienceMatchPolicy</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-AudienceMatchPolicyType"><code>AudienceMatchPolicyType</code></a>
</td>
<td>
   <p>audienceMatchPolicy تعیین می‌کند که فیلد &quot;audiences&quot; چگونه برای تطبیق با claim با نام &quot;aud&quot; در JWT ارائه‌شده به کار رود.
مقادیر مجاز عبارت‌اند از:</p>
<ol>
<li>&quot;MatchAny&quot; زمانی که چند مخاطب (audience) مشخص شده باشد، و</li>
<li>خالی (یا تنظیم‌نشده) یا &quot;MatchAny&quot; زمانی که یک مخاطب (audience) واحد مشخص شده باشد.</li>
</ol>
<ul>
<li>
<p>MatchAny: claim با نام &quot;aud&quot; در JWT ارائه‌شده باید با دست‌کم یکی از ورودی‌های فیلد &quot;audiences&quot; مطابقت داشته باشد.
برای مثال، اگر &quot;audiences&quot; برابر [&quot;foo&quot;, &quot;bar&quot;] باشد، claim با نام &quot;aud&quot; در JWT ارائه‌شده باید شامل &quot;foo&quot; یا &quot;bar&quot; باشد (و می‌تواند شامل هر دو نیز باشد).</p>
</li>
<li>
<p>&quot;&quot;: زمانی که در فیلد &quot;audiences&quot; فقط یک مخاطب (audience) مشخص شده باشد، سیاست تطبیق می‌تواند خالی (یا تنظیم‌نشده) باشد. claim با نام &quot;aud&quot; در JWT ارائه‌شده باید شامل همان مخاطب واحد باشد (و می‌تواند شامل مخاطبان دیگر نیز باشد).</p>
</li>
</ul>
<p>برای اعتبارسنجی دقیق‌تر مخاطبان، از claimValidationRules استفاده کنید.
مثال: claimValidationRule[].expression: 'sets.equivalent(claims.aud, [&quot;bar&quot;, &quot;foo&quot;, &quot;baz&quot;])' برای الزام به تطبیق دقیق.</p>
</td>
</tr>
<tr><td><code>egressSelectorType</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-EgressSelectorType"><code>EgressSelectorType</code></a>
</td>
<td>
   <p>egressSelectorType نشان‌دهنده این است که برای ارسال تمام ترافیک مربوط به
این issuer (شامل discovery، JWKS، claimهای توزیع‌شده و غیره) باید از کدام انتخاب خروجی (egress selection) استفاده شود. اگر مشخص نشود، هیچ dialer سفارشی استفاده نمی‌شود.
در صورت تعیین، گزینه‌های معتبر &quot;controlplane&quot; و &quot;cluster&quot; هستند. این‌ها با مقادیر متناظر
در --egress-selector-config-file مطابقت دارند.</p>
<ul>
<li>
<p>controlplane: برای ترافیکی که قرار است به control plane برود.</p>
</li>
<li>
<p>cluster: برای ترافیکی که قرار است به سامانه‌ای برود که توسط کوبرنتیز مدیریت می‌شود.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `JWTAuthenticator`     {#apiserver-k8s-io-v1alpha1-JWTAuthenticator}
    

**ظاهر شده در:**

- [AuthenticationConfiguration](#apiserver-k8s-io-v1alpha1-AuthenticationConfiguration)


<p>JWTAuthenticator پیکربندی یک JWT authenticator واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>issuer</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-Issuer"><code>Issuer</code></a>
</td>
<td>
   <p>issuer شامل گزینه‌های اولیه اتصال به ارائه‌دهنده OIDC است.</p>
</td>
</tr>
<tr><td><code>claimValidationRules</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-ClaimValidationRule"><code>[]ClaimValidationRule</code></a>
</td>
<td>
   <p>claimValidationRules قواعدی هستند که برای اعتبارسنجی claimهای توکن به‌منظور احراز هویت کاربران اعمال می‌شوند.</p>
</td>
</tr>
<tr><td><code>claimMappings</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-ClaimMappings"><code>ClaimMappings</code></a>
</td>
<td>
   <p>claimMappings مشخص می‌کند کدام claimهای یک توکن به‌عنوان ویژگی‌های کاربر در نظر گرفته شوند.</p>
</td>
</tr>
<tr><td><code>userValidationRules</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-UserValidationRule"><code>[]UserValidationRule</code></a>
</td>
<td>
   <p>userValidationRules قواعدی هستند که پیش از تکمیل احراز هویت بر کاربر نهایی اعمال می‌شوند.
این قواعد امکان اعمال ناوردایی‌ها (invariants) بر هویت‌های ورودی را فراهم می‌کنند، مانند جلوگیری از
استفاده از پیشوند system: که معمولاً توسط مؤلفه‌های کوبرنتیز استفاده می‌شود.
قواعد اعتبارسنجی از نظر منطقی با AND با یکدیگر ترکیب می‌شوند و برای موفقیت اعتبارسنجی همه باید مقدار true بازگردانند.</p>
</td>
</tr>
</tbody>
</table>

## `PrefixedClaimOrExpression`     {#apiserver-k8s-io-v1alpha1-PrefixedClaimOrExpression}
    

**ظاهر شده در:**

- [ClaimMappings](#apiserver-k8s-io-v1alpha1-ClaimMappings)


<p>PrefixedClaimOrExpression پیکربندی یک claim یا عبارت پیشونددار واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim همان claim مربوط به JWT است که باید استفاده شود.
با expression متقابلاً ناسازگار است (نمی‌توان هر دو را همزمان تعیین کرد).</p>
</td>
</tr>
<tr><td><code>prefix</code><br/>
<code>string</code>
</td>
<td>
   <p>prefix به ابتدای مقدار claim افزوده می‌شود تا از تداخل با نام‌های موجود جلوگیری شود.
اگر claim تنظیم شده باشد، باید prefix نیز تنظیم شود و می‌تواند رشته خالی باشد.
با expression متقابلاً ناسازگار است (نمی‌توان هر دو را همزمان تعیین کرد).</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب یک متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر آن‌هاست.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مانند 'claims.foo.bar'.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim و prefix متقابلاً ناسازگار است (نمی‌توان آن را همزمان با آن‌ها تعیین کرد).</p>
</td>
</tr>
</tbody>
</table>

## `ProtocolType`     {#apiserver-k8s-io-v1alpha1-ProtocolType}
    
(نام مستعار برای `string`)

**ظاهر شده در:**

- [Connection](#apiserver-k8s-io-v1alpha1-Connection)


<p>ProtocolType مجموعه‌ای از مقادیر معتبر برای Connection.ProtocolType است.</p>




## `TCPTransport`     {#apiserver-k8s-io-v1alpha1-TCPTransport}
    

**ظاهر شده در:**

- [Transport](#apiserver-k8s-io-v1alpha1-Transport)


<p>TCPTransport اطلاعات لازم برای اتصال به سرور konnectivity از طریق TCP را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>url</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>URL نشانی سرور konnectivity است که باید به آن متصل شد.
برای مثال می‌تواند &quot;https://127.0.0.1:8131&quot; باشد.</p>
</td>
</tr>
<tr><td><code>tlsConfig</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-TLSConfig"><code>TLSConfig</code></a>
</td>
<td>
   <p>TLSConfig پیکربندی لازم برای استفاده از TLS هنگام اتصال به سرور konnectivity است.</p>
</td>
</tr>
</tbody>
</table>

## `TLSConfig`     {#apiserver-k8s-io-v1alpha1-TLSConfig}
    

**ظاهر شده در:**

- [TCPTransport](#apiserver-k8s-io-v1alpha1-TCPTransport)


<p>TLSConfig اطلاعات احراز هویت لازم برای اتصال به سرور konnectivity را فراهم می‌کند.
فقط همراه با TCPTransport استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>caBundle</code><br/>
<code>string</code>
</td>
<td>
   <p>caBundle مسیر فایل CA است که برای تعیین اعتماد به سرور konnectivity به کار می‌رود.
اگر TCPTransport.URL با http:// آغاز شده باشد، باید وجود نداشته باشد یا خالی باشد.
اگر TCPTransport.URL با https:// آغاز شده باشد و این فیلد تعیین نشده باشد، به ریشه‌های اعتماد سیستم (system trust roots) بازمی‌گردد.</p>
</td>
</tr>
<tr><td><code>clientKey</code><br/>
<code>string</code>
</td>
<td>
   <p>clientKey مسیر فایل کلید کلاینت است که در handshakeهای mtls با سرور konnectivity استفاده می‌شود.
اگر TCPTransport.URL با http:// آغاز شده باشد، باید وجود نداشته باشد یا خالی باشد.
اگر TCPTransport.URL با https:// آغاز شده باشد، باید پیکربندی شود.</p>
</td>
</tr>
<tr><td><code>clientCert</code><br/>
<code>string</code>
</td>
<td>
   <p>clientCert مسیر فایل گواهی کلاینت است که در handshakeهای mtls با سرور konnectivity استفاده می‌شود.
اگر TCPTransport.URL با http:// آغاز شده باشد، باید وجود نداشته باشد یا خالی باشد.
اگر TCPTransport.URL با https:// آغاز شده باشد، باید پیکربندی شود.</p>
</td>
</tr>
<tr><td><code>tlsServerName</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsServerName برای بررسی گواهی سرور استفاده می‌شود. اگر tlsServerName خالی باشد، از نام میزبانی (hostname) که برای تماس با سرور به کار رفته است استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `Transport`     {#apiserver-k8s-io-v1alpha1-Transport}
    

**ظاهر شده در:**

- [Connection](#apiserver-k8s-io-v1alpha1-Connection)


<p>Transport پیکربندی‌های انتقال (transport) را تعریف می‌کند که برای برقراری اتصال به سرور konnectivity از آن‌ها استفاده می‌کنیم.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>tcp</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-TCPTransport"><code>TCPTransport</code></a>
</td>
<td>
   <p>TCP پیکربندی TCP برای ارتباط با سرور konnectivity از طریق TCP است.
ProxyProtocol مربوط به GRPC در حال حاضر با انتقال TCP پشتیبانی نمی‌شود.
نیازمند تنظیم دست‌کم یکی از TCP یا UDS است.</p>
</td>
</tr>
<tr><td><code>uds</code><br/>
<a href="#apiserver-k8s-io-v1alpha1-UDSTransport"><code>UDSTransport</code></a>
</td>
<td>
   <p>UDS پیکربندی UDS برای ارتباط با سرور konnectivity از طریق UDS است.
نیازمند تنظیم دست‌کم یکی از TCP یا UDS است.</p>
</td>
</tr>
</tbody>
</table>

## `UDSTransport`     {#apiserver-k8s-io-v1alpha1-UDSTransport}
    

**ظاهر شده در:**

- [Transport](#apiserver-k8s-io-v1alpha1-Transport)


<p>UDSTransport اطلاعات لازم برای اتصال به سرور konnectivity از طریق UDS را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>udsName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>UDSName نام unix domain socket برای اتصال به سرور konnectivity است.
این مقدار از پیشوند unix:// استفاده نمی‌کند. (برای مثال: /etc/srv/kubernetes/konnectivity-server/konnectivity-server.socket)</p>
</td>
</tr>
</tbody>
</table>

## `UserValidationRule`     {#apiserver-k8s-io-v1alpha1-UserValidationRule}
    

**ظاهر شده در:**

- [JWTAuthenticator](#apiserver-k8s-io-v1alpha1-JWTAuthenticator)


<p>UserValidationRule پیکربندی یک قاعده اعتبارسنجی اطلاعات کاربر (user info) واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>expression</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد.
برای موفقیت اعتبارسنجی باید مقدار true بازگرداند.</p>
<p>عبارت‌های CEL به محتوای UserInfo دسترسی دارند که در قالب یک متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'user' - آبجکت authentication.k8s.io/v1، Kind=UserInfo
برای تعریف آن به https://github.com/kubernetes/api/blob/release-1.28/authentication/v1/types.go#L105-L122 مراجعه کنید.
مستندات API: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#userinfo-v1-authentication-k8s-io</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
<tr><td><code>message</code><br/>
<code>string</code>
</td>
<td>
   <p>message پیام خطای بازگردانده‌شده را زمانی که قاعده مقدار false بازمی‌گرداند، سفارشی می‌کند.
message یک رشته لفظی (literal) است.</p>
</td>
</tr>
</tbody>
</table>

## `WebhookConfiguration`     {#apiserver-k8s-io-v1alpha1-WebhookConfiguration}
    

**ظاهر شده در:**

- [AuthorizerConfiguration](#apiserver-k8s-io-v1alpha1-AuthorizerConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>authorizedTTL</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمان نگهداری پاسخ‌های «مجاز» (authorized) در حافظه نهان از سوی authorizer مبتنی بر وب‌هوک.
معادل تنظیم فلگ <code>--authorization-webhook-cache-authorized-ttl</code> است.
مقدار پیش‌فرض: 5m0s</p>
</td>
</tr>
<tr><td><code>cacheAuthorizedRequests</code><br/>
<code>bool</code>
</td>
<td>
   <p>CacheAuthorizedRequests مشخص می‌کند که آیا درخواست‌های مجاز باید در حافظه نهان نگهداری شوند یا خیر.
اگر روی true تنظیم شود، TTL تصمیم‌های ذخیره‌شده در حافظه نهان را می‌توان از طریق
فیلد AuthorizedTTL پیکربندی کرد.
مقدار پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>unauthorizedTTL</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمان نگهداری پاسخ‌های «غیرمجاز» (unauthorized) در حافظه نهان از سوی authorizer مبتنی بر وب‌هوک.
معادل تنظیم فلگ <code>--authorization-webhook-cache-unauthorized-ttl</code> است.
مقدار پیش‌فرض: 30s</p>
</td>
</tr>
<tr><td><code>cacheUnauthorizedRequests</code><br/>
<code>bool</code>
</td>
<td>
   <p>CacheUnauthorizedRequests مشخص می‌کند که آیا درخواست‌های غیرمجاز باید در حافظه نهان نگهداری شوند یا خیر.
اگر روی true تنظیم شود، TTL تصمیم‌های ذخیره‌شده در حافظه نهان را می‌توان از طریق
فیلد UnauthorizedTTL پیکربندی کرد.
مقدار پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>timeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مهلت زمانی (timeout) درخواست وب‌هوک.
حداکثر مقدار مجاز 30s است.
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>subjectAccessReviewVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه API از SubjectAccessReview در authorization.k8s.io که باید به وب‌هوک ارسال شود
و از آن انتظار پاسخ می‌رود.
معادل تنظیم فلگ <code>--authorization-webhook-version</code> است.
مقادیر معتبر: v1beta1, v1
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>matchConditionSubjectAccessReviewVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>MatchConditionSubjectAccessReviewVersion نسخه SubjectAccessReview را مشخص می‌کند
که عبارت‌های CEL بر اساس آن ارزیابی می‌شوند.
مقادیر معتبر: v1
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>failurePolicy</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>تصمیم مجوزدهی را در زمانی تعیین می‌کند که درخواست وب‌هوک به پایان نرسد،
پاسخی نادرست‌ساختار (malformed) برگرداند، یا ارزیابی matchConditions با خطا مواجه شود.
مقادیر معتبر:</p>
<ul>
<li>NoOpinion: ادامه به سراغ authorizerهای بعدی تا بررسی شود آیا یکی از
آن‌ها درخواست را مجاز می‌کند یا خیر</li>
<li>Deny: رد درخواست بدون مراجعه به authorizerهای بعدی
الزامی است و مقدار پیش‌فرض ندارد.</li>
</ul>
</td>
</tr>
<tr><td><code>connectionInfo</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-WebhookConnectionInfo"><code>WebhookConnectionInfo</code></a>
</td>
<td>
   <p>ConnectionInfo نحوه ارتباط با وب‌هوک را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>matchConditions</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1alpha1-WebhookMatchCondition"><code>[]WebhookMatchCondition</code></a>
</td>
<td>
   <p>matchConditions فهرستی از شرایط است که برای ارسال یک درخواست به این
وب‌هوک باید برقرار باشند. فهرست خالی matchConditions با همه درخواست‌ها مطابقت دارد.
حداکثر ۶۴ شرط تطبیق مجاز است.</p>
<p>منطق دقیق تطبیق (به ترتیب) به شرح زیر است:</p>
<ol>
<li>اگر دست‌کم یک matchCondition به FALSE ارزیابی شود، وب‌هوک نادیده گرفته می‌شود.</li>
<li>اگر همه matchConditionها به TRUE ارزیابی شوند، وب‌هوک فراخوانی می‌شود.</li>
<li>اگر دست‌کم یک matchCondition به خطا ارزیابی شود (اما هیچ‌کدام FALSE نباشند):
<ul>
<li>اگر failurePolicy=Deny باشد، وب‌هوک درخواست را رد می‌کند</li>
<li>اگر failurePolicy=NoOpinion باشد، خطا نادیده گرفته می‌شود و وب‌هوک رد می‌شود</li>
</ul>
</li>
</ol>
</td>
</tr>
</tbody>
</table>

## `WebhookConnectionInfo`     {#apiserver-k8s-io-v1alpha1-WebhookConnectionInfo}
    

**ظاهر شده در:**

- [WebhookConfiguration](#apiserver-k8s-io-v1alpha1-WebhookConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نحوه ارتباط وب‌هوک با سرور را تعیین می‌کند.
مقادیر معتبر:</p>
<ul>
<li>KubeConfigFile: از فایل مشخص‌شده در kubeConfigFile برای یافتن
سرور استفاده می‌شود.</li>
<li>InClusterConfig: از پیکربندی درون کلاستری برای فراخوانی
API مربوط به SubjectAccessReview که توسط kube-apiserver ارائه می‌شود استفاده می‌شود. این حالت
برای kube-apiserver مجاز نیست.</li>
</ul>
</td>
</tr>
<tr><td><code>kubeConfigFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>مسیر KubeConfigFile برای اطلاعات اتصال.
اگر connectionInfo.Type برابر KubeConfig باشد، الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `WebhookMatchCondition`     {#apiserver-k8s-io-v1alpha1-WebhookMatchCondition}
    

**ظاهر شده در:**

- [WebhookConfiguration](#apiserver-k8s-io-v1alpha1-WebhookConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>expression</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد و باید نتیجه آن از نوع bool باشد.
عبارت‌های CEL به محتویات SubjectAccessReview در نسخه v1 دسترسی دارند.
اگر نسخه مشخص‌شده توسط subjectAccessReviewVersion در متغیر request برابر v1beta1 باشد،
محتویات پیش از ارزیابی عبارت CEL به نسخه v1 تبدیل می‌شوند.</p>
<ul>
<li>'resourceAttributes' اطلاعات مربوط به یک درخواست دسترسی به منبع را توصیف می‌کند و برای درخواست‌های غیرمنبعی تنظیم نمی‌شود. برای مثال: has(request.resourceAttributes) &amp;&amp; request.resourceAttributes.namespace == 'default'</li>
<li>'nonResourceAttributes' اطلاعات مربوط به یک درخواست دسترسی غیرمنبعی را توصیف می‌کند و برای درخواست‌های منبعی تنظیم نمی‌شود. برای مثال: has(request.nonResourceAttributes) &amp;&amp; request.nonResourceAttributes.path == '/healthz'.</li>
<li>'user' کاربری است که باید برای آن آزمون انجام شود. برای مثال: request.user == 'alice'</li>
<li>'groups' گروه‌هایی است که باید برای آن‌ها آزمون انجام شود. برای مثال: ('group1' in request.groups)</li>
<li>'extra' با متد user.Info.GetExtra() از authenticator متناظر است.</li>
<li>'uid' اطلاعات مربوط به کاربر درخواست‌کننده است. برای مثال: request.uid == '1'</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
</tbody>
</table>
