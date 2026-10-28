---
title: پیکربندی kube-apiserver (v1beta1)
content_type: tool-reference
package: apiserver.k8s.io/v1beta1
auto_generated: true
---
<p>بسته v1beta1 نسخهٔ v1beta1 از API است.</p>


## انواع منابع 


- [AuthenticationConfiguration](#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)
- [AuthorizationConfiguration](#apiserver-k8s-io-v1beta1-AuthorizationConfiguration)
- [EgressSelectorConfiguration](#apiserver-k8s-io-v1beta1-EgressSelectorConfiguration)
- [TracingConfiguration](#apiserver-k8s-io-v1beta1-TracingConfiguration)
  
    
    

## `TracingConfiguration`     {#TracingConfiguration}
    

**در این موارد ظاهر می‌شود:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

- [TracingConfiguration](#apiserver-k8s-io-v1alpha1-TracingConfiguration)

- [TracingConfiguration](#apiserver-k8s-io-v1beta1-TracingConfiguration)


<p>TracingConfiguration پیکربندی نسخه‌بندی‌شده را برای کلاینت‌های ردیابی OpenTelemetry فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>نقطه پایانی (Endpoint) کالکتوری که این مؤلفه ردیابی‌ها (traces) را به آن گزارش می‌کند.
اتصال ناامن است و در حال حاضر از TLS پشتیبانی نمی‌کند.
توصیه می‌شود این مقدار تنظیم نشود و endpoint همان مقدار پیش‌فرض otlp grpc، یعنی localhost:4317، باشد.</p>
</td>
</tr>
<tr><td><code>samplingRatePerMillion</code><br/>
<code>int32</code>
</td>
<td>
   <p>SamplingRatePerMillion تعداد نمونه‌هایی است که به ازای هر یک میلیون span جمع‌آوری می‌شود.
توصیه می‌شود این مقدار تنظیم نشود. اگر تنظیم نشده باشد، نمونه‌بردار (sampler) از نرخ نمونه‌برداری
span والد خود پیروی می‌کند، اما در غیر این صورت هرگز نمونه‌برداری نمی‌کند.</p>
</td>
</tr>
</tbody>
</table>
  

## `AuthenticationConfiguration`     {#apiserver-k8s-io-v1beta1-AuthenticationConfiguration}
    


<p>AuthenticationConfiguration پیکربندی نسخه‌بندی‌شده را برای احراز هویت فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AuthenticationConfiguration</code></td></tr>
    
  
<tr><td><code>jwt</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-JWTAuthenticator"><code>[]JWTAuthenticator</code></a>
</td>
<td>
   <p>jwt فهرستی از احراز هویت‌کننده‌ها (authenticator) برای احراز هویت کاربران کوبرنتیز
با استفاده از توکن‌های سازگار با JWT است. احراز هویت‌کننده تلاش می‌کند یک توکن ID خام را تجزیه کند
و بررسی کند که توسط صادرکنندهٔ (issuer) پیکربندی‌شده امضا شده باشد. کلید عمومی لازم برای تأیید
امضا از نقطه پایانی عمومی صادرکننده با استفاده از OIDC discovery به دست می‌آید.
برای یک توکن ورودی، هر احراز هویت‌کنندهٔ JWT به ترتیبی که در این فهرست مشخص شده است
آزموده می‌شود. توجه کنید که
احراز هویت‌کننده‌های دیگر ممکن است پیش از احراز هویت‌کننده‌های JWT یا پس از آن‌ها اجرا شوند.
جایگاه دقیق احراز هویت‌کننده‌های JWT نسبت به سایر
احراز هویت‌کننده‌ها نه تعریف شده است و نه در نسخه‌های مختلف پایدار است. از آنجا که
هر احراز هویت‌کنندهٔ JWT باید نشانی صادرکنندهٔ منحصربه‌فرد داشته باشد، حداکثر یک
احراز هویت‌کنندهٔ JWT تلاش می‌کند توکن را از نظر رمزنگاری اعتبارسنجی کند.</p>
<p>حداقل بار (payload) معتبر JWT باید شامل claimهای زیر باشد:
{
&quot;iss&quot;: &quot;https://issuer.example.com&quot;,
&quot;aud&quot;: [&quot;audience&quot;],
&quot;exp&quot;: 1234567890,
&quot;<!-- raw HTML omitted -->&quot;: &quot;username&quot;
}</p>
</td>
</tr>
<tr><td><code>anonymous</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-AnonymousAuthConfig"><code>AnonymousAuthConfig</code></a>
</td>
<td>
   <p>در صورت وجود، نباید --anonymous-auth تنظیم شده باشد</p>
</td>
</tr>
</tbody>
</table>

## `AuthorizationConfiguration`     {#apiserver-k8s-io-v1beta1-AuthorizationConfiguration}
    



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AuthorizationConfiguration</code></td></tr>
    
  
<tr><td><code>authorizers</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-AuthorizerConfiguration"><code>[]AuthorizerConfiguration</code></a>
</td>
<td>
   <p>Authorizers فهرستی مرتب از مجوزدهنده‌ها (authorizer) است که
درخواست‌ها بر اساس آن‌ها مجاز می‌شوند.
این مشابه فلگ --authorization-modes در kube-apiserver است.
باید دست‌کم یک مورد وجود داشته باشد.</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelectorConfiguration`     {#apiserver-k8s-io-v1beta1-EgressSelectorConfiguration}
    


<p>EgressSelectorConfiguration پیکربندی نسخه‌بندی‌شده را برای کلاینت‌های egress selector فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>EgressSelectorConfiguration</code></td></tr>
    
  
<tr><td><code>egressSelections</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-EgressSelection"><code>[]EgressSelection</code></a>
</td>
<td>
   <p>connectionServices شامل فهرستی از پیکربندی‌های کلاینت egress selection است</p>
</td>
</tr>
</tbody>
</table>

## `TracingConfiguration`     {#apiserver-k8s-io-v1beta1-TracingConfiguration}
    


<p>TracingConfiguration پیکربندی نسخه‌بندی‌شده را برای کلاینت‌های ردیابی فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>TracingConfiguration</code></td></tr>
    
  
<tr><td><code>TracingConfiguration</code> <B>[Required]</B><br/>
<a href="#TracingConfiguration"><code>TracingConfiguration</code></a>
</td>
<td>
   <p>ساختار (struct) پیکربندی ردیابی پیکربندی مؤلفه را درون خود جاسازی کنید</p>
</td>
</tr>
</tbody>
</table>

## `AnonymousAuthCondition`     {#apiserver-k8s-io-v1beta1-AnonymousAuthCondition}
    

**در این موارد ظاهر می‌شود:**

- [AnonymousAuthConfig](#apiserver-k8s-io-v1beta1-AnonymousAuthConfig)


<p>AnonymousAuthCondition شرطی را توصیف می‌کند که تحت آن احراز هویت ناشناس
باید فعال شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>path</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>مسیری که احراز هویت ناشناس برای آن فعال است.</p>
</td>
</tr>
</tbody>
</table>

## `AnonymousAuthConfig`     {#apiserver-k8s-io-v1beta1-AnonymousAuthConfig}
    

**در این موارد ظاهر می‌شود:**

- [AuthenticationConfiguration](#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)


<p>AnonymousAuthConfig پیکربندی احراز هویت‌کنندهٔ ناشناس را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>enabled</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>conditions</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-AnonymousAuthCondition"><code>[]AnonymousAuthCondition</code></a>
</td>
<td>
   <p>در صورت تنظیم، احراز هویت ناشناس تنها زمانی مجاز است که درخواست یکی از
شرط‌ها را برآورده کند.</p>
</td>
</tr>
</tbody>
</table>

## `AudienceMatchPolicyType`     {#apiserver-k8s-io-v1beta1-AudienceMatchPolicyType}
    
(نام مستعار برای `string`)

**در این موارد ظاهر می‌شود:**

- [Issuer](#apiserver-k8s-io-v1beta1-Issuer)


<p>AudienceMatchPolicyType مجموعه‌ای از مقادیر معتبر برای issuer.audienceMatchPolicy است</p>




## `AuthorizerConfiguration`     {#apiserver-k8s-io-v1beta1-AuthorizerConfiguration}
    

**در این موارد ظاهر می‌شود:**

- [AuthorizationConfiguration](#apiserver-k8s-io-v1beta1-AuthorizationConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Type به نوع مجوزدهنده (authorizer) اشاره دارد.
&quot;Webhook&quot; در API server عمومی پشتیبانی می‌شود.
سایر API serverها ممکن است از انواع مجوزدهندهٔ اضافی
مانند Node، RBAC، ABAC و غیره پشتیبانی کنند.</p>
</td>
</tr>
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name برای توصیف webhook به کار می‌رود.
این نام به‌صراحت در سازوکار پایش برای متریک‌ها استفاده می‌شود.
توجه: نام‌ها باید برچسب‌های DNS1123 مانند <code>myauthorizername</code> یا
زیردامنه‌هایی مانند <code>myauthorizer.example.domain</code> باشند.
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>webhook</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-WebhookConfiguration"><code>WebhookConfiguration</code></a>
</td>
<td>
   <p>Webhook پیکربندی مجوزدهندهٔ Webhook را تعریف می‌کند.
وقتی Type=Webhook است باید تعریف شود.
وقتی Type!=Webhook است نباید تعریف شود.</p>
</td>
</tr>
</tbody>
</table>

## `ClaimMappings`     {#apiserver-k8s-io-v1beta1-ClaimMappings}
    

**در این موارد ظاهر می‌شود:**

- [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)


<p>ClaimMappings پیکربندی نگاشت claim را فراهم می‌کند</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>username</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-PrefixedClaimOrExpression"><code>PrefixedClaimOrExpression</code></a>
</td>
<td>
   <p>username گزینه‌ای برای صفت username است.
مقدار claim باید یک رشتهٔ منفرد باشد.
معادل فلگ‌های --oidc-username-claim و --oidc-username-prefix است.
اگر username.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای تولید کند.
اگر username.expression از 'claims.email' استفاده کند، آنگاه 'claims.email_verified' باید در
username.expression یا extra[<em>].valueExpression یا claimValidationRules[</em>].expression استفاده شود.
نمونه‌ای از عبارت قاعدهٔ اعتبارسنجی claim که با اعتبارسنجی‌ای که به‌طور خودکار
هنگام تنظیم username.claim روی 'email' اعمال می‌شود مطابقت دارد، عبارت 'claims.?email_verified.orValue(true) == true' است. با مقایسهٔ صریح
مقدار با true، به بررسی نوع (type-checking) اجازه می‌دهیم ببیند نتیجه یک مقدار بولی خواهد بود، و اطمینان حاصل می‌کنیم که
claim غیربولی email_verified در زمان اجرا شناسایی می‌شود.</p>
<p>در رویکرد مبتنی بر فلگ، --oidc-username-claim و --oidc-username-prefix اختیاری هستند. اگر --oidc-username-claim تنظیم نشده باشد،
مقدار پیش‌فرض &quot;sub&quot; است. در پیکربندی احراز هویت، برای claim یا prefix مقدار پیش‌فرضی وجود ندارد. claim و prefix باید به‌صراحت تنظیم شوند.
برای claim، اگر --oidc-username-claim در رویکرد قدیمی مبتنی بر فلگ تنظیم نشده بود، در پیکربندی احراز هویت username.claim=&quot;sub&quot; را پیکربندی کنید.
برای prefix:
(1) --oidc-username-prefix=&quot;-&quot;، هیچ پیشوندی به username افزوده نمی‌شد. برای رفتار یکسان با استفاده از پیکربندی احراز هویت،
username.prefix=&quot;&quot; را تنظیم کنید
(2) --oidc-username-prefix=&quot;&quot; و  --oidc-username-claim != &quot;email&quot;، پیشوند &quot;&lt;value of --oidc-issuer-url&gt;#&quot; بود. برای
رفتار یکسان با استفاده از پیکربندی احراز هویت، username.prefix=&quot;<!-- raw HTML omitted -->#&quot; را تنظیم کنید
(3) --oidc-username-prefix=&quot;<!-- raw HTML omitted -->&quot;. برای رفتار یکسان با استفاده از پیکربندی احراز هویت، username.prefix=&quot;<!-- raw HTML omitted -->&quot; را تنظیم کنید</p>
</td>
</tr>
<tr><td><code>groups</code><br/>
<a href="#apiserver-k8s-io-v1beta1-PrefixedClaimOrExpression"><code>PrefixedClaimOrExpression</code></a>
</td>
<td>
   <p>groups گزینه‌ای برای صفت groups است.
مقدار claim باید یک رشته یا آرایه‌ای از رشته‌ها باشد.
اگر groups.claim تنظیم شده باشد، prefix باید مشخص شود (و می‌تواند رشتهٔ خالی باشد).
اگر groups.expression تنظیم شده باشد، عبارت باید یک رشته یا آرایه‌ای از رشته‌ها تولید کند.
مقادیر &quot;&quot;، [] و null به این معنا در نظر گرفته می‌شوند که نگاشت گروه وجود ندارد.</p>
</td>
</tr>
<tr><td><code>uid</code><br/>
<a href="#apiserver-k8s-io-v1beta1-ClaimOrExpression"><code>ClaimOrExpression</code></a>
</td>
<td>
   <p>uid گزینه‌ای برای صفت uid است.
claim باید یک claim رشته‌ای منفرد باشد.
اگر uid.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای تولید کند.</p>
</td>
</tr>
<tr><td><code>extra</code><br/>
<a href="#apiserver-k8s-io-v1beta1-ExtraMapping"><code>[]ExtraMapping</code></a>
</td>
<td>
   <p>extra گزینه‌ای برای صفت extra است.
expression باید یک رشته یا آرایه‌ای از رشته‌ها تولید کند.
اگر مقدار خالی باشد، نگاشت extra وجود نخواهد داشت.</p>
<p>کلید/مقدار extra ثابت (hard-coded)</p>
<ul>
<li>key: &quot;foo&quot;
valueExpression: &quot;'bar'&quot;
این به یک صفت extra با مقدار foo: [&quot;bar&quot;] منجر می‌شود</li>
</ul>
<p>کلید ثابت، مقدار کپی‌شده از مقدار claim</p>
<ul>
<li>key: &quot;foo&quot;
valueExpression: &quot;claims.some_claim&quot;
این به یک صفت extra با مقدار foo: [value of some_claim] منجر می‌شود</li>
</ul>
<p>کلید ثابت، مقدار مشتق‌شده از مقدار claim</p>
<ul>
<li>key: &quot;admin&quot;
valueExpression: '(has(claims.is_admin) &amp;&amp; claims.is_admin) ? &quot;true&quot;:&quot;&quot;'
این به نتایج زیر منجر می‌شود:</li>
<li>اگر claim با نام is_admin وجود داشته باشد و true باشد، صفت extra به صورت admin: [&quot;true&quot;]</li>
<li>اگر claim با نام is_admin وجود داشته باشد و false باشد یا claim با نام is_admin وجود نداشته باشد، هیچ صفت extra اضافه نخواهد شد</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `ClaimOrExpression`     {#apiserver-k8s-io-v1beta1-ClaimOrExpression}
    

**در این موارد ظاهر می‌شود:**

- [ClaimMappings](#apiserver-k8s-io-v1beta1-ClaimMappings)


<p>ClaimOrExpression پیکربندی یک claim یا عبارت منفرد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim همان claim از JWT است که باید استفاده شود.
یکی از claim یا expression باید تنظیم شود.
با expression متقابلاً ناسازگار است (mutually exclusive).</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده‌اند:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claim است.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مثلاً 'claims.foo.bar'.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim متقابلاً ناسازگار است.</p>
</td>
</tr>
</tbody>
</table>

## `ClaimValidationRule`     {#apiserver-k8s-io-v1beta1-ClaimValidationRule}
    

**در این موارد ظاهر می‌شود:**

- [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)


<p>ClaimValidationRule پیکربندی یک قاعدهٔ اعتبارسنجی claim منفرد را فراهم می‌کند.</p>


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
با expression و message متقابلاً ناسازگار است.</p>
</td>
</tr>
<tr><td><code>requiredValue</code><br/>
<code>string</code>
</td>
<td>
   <p>requiredValue مقدار یک claim الزامی است.
معادل فلگ --oidc-required-claim است.
فقط مقادیر claim از نوع رشته پشتیبانی می‌شوند.
اگر claim تنظیم شده باشد و requiredValue تنظیم نشده باشد، claim باید با مقداری برابر رشتهٔ خالی وجود داشته باشد.
با expression و message متقابلاً ناسازگار است.</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی خواهد شد.
باید یک مقدار بولی تولید کند.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده‌اند:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claim است.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مثلاً 'claims.foo.bar'.
برای موفقیت اعتبارسنجی باید true برگرداند.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim و requiredValue متقابلاً ناسازگار است.</p>
</td>
</tr>
<tr><td><code>message</code><br/>
<code>string</code>
</td>
<td>
   <p>message پیام خطای برگردانده‌شده را زمانی که expression مقدار false برگرداند سفارشی می‌کند.
message یک رشتهٔ لفظی (literal) است.
با claim و requiredValue متقابلاً ناسازگار است.</p>
</td>
</tr>
</tbody>
</table>

## `Connection`     {#apiserver-k8s-io-v1beta1-Connection}
    

**در این موارد ظاهر می‌شود:**

- [EgressSelection](#apiserver-k8s-io-v1beta1-EgressSelection)


<p>Connection پیکربندی یک کلاینت egress selection منفرد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>proxyProtocol</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-ProtocolType"><code>ProtocolType</code></a>
</td>
<td>
   <p>Protocol پروتکلی است که برای اتصال از کلاینت به سرور konnectivity استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>transport</code><br/>
<a href="#apiserver-k8s-io-v1beta1-Transport"><code>Transport</code></a>
</td>
<td>
   <p>Transport پیکربندی‌های انتقال (transport) را تعریف می‌کند که برای اتصال به سرور konnectivity استفاده می‌کنیم.
اگر ProxyProtocol برابر HTTPConnect یا GRPC باشد، این مقدار الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelection`     {#apiserver-k8s-io-v1beta1-EgressSelection}
    

**در این موارد ظاهر می‌شود:**

- [EgressSelectorConfiguration](#apiserver-k8s-io-v1beta1-EgressSelectorConfiguration)


<p>EgressSelection پیکربندی یک کلاینت egress selection منفرد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام egress selection است.
مقادیر پشتیبانی‌شده در حال حاضر &quot;controlplane&quot;، &quot;master&quot;، &quot;etcd&quot; و &quot;cluster&quot; هستند.
egress selector با نام &quot;master&quot; به نفع &quot;controlplane&quot; منسوخ شده است</p>
</td>
</tr>
<tr><td><code>connection</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-Connection"><code>Connection</code></a>
</td>
<td>
   <p>connection اطلاعات دقیقی است که برای پیکربندی egress selection استفاده می‌شود</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelectorType`     {#apiserver-k8s-io-v1beta1-EgressSelectorType}
    
(نام مستعار برای `string`)

**در این موارد ظاهر می‌شود:**

- [Issuer](#apiserver-k8s-io-v1beta1-Issuer)


<p>EgressSelectorType نشان‌دهندهٔ این است که کدام egress selection باید برای ارسال ترافیک استفاده شود.</p>

## `ExtraMapping`     {#apiserver-k8s-io-v1beta1-ExtraMapping}
    

**نمایش داده می‌شود در:**

- [ClaimMappings](#apiserver-k8s-io-v1beta1-ClaimMappings)


<p>ExtraMapping پیکربندی یک نگاشت extra منفرد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>key</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>key رشته‌ای است که به‌عنوان کلید ویژگی extra استفاده می‌شود.
key باید یک مسیر دارای پیشوند دامنه باشد (برای مثال example.org/foo). تمام نویسه‌های پیش از اولین «/» باید یک
زیردامنه معتبر مطابق RFC 1123 باشند. تمام نویسه‌های پس از اولین «/» باید
نویسه‌های معتبر مسیر HTTP مطابق RFC 3986 باشند.
key باید با حروف کوچک نوشته شود.
یکتا بودن آن الزامی است.</p>
</td>
</tr>
<tr><td><code>valueExpression</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>valueExpression یک عبارت CEL برای استخراج مقدار ویژگی extra است.
valueExpression باید یک مقدار رشته‌ای یا آرایه‌ای از رشته‌ها تولید کند.
مقادیر «&quot;&quot;»، [] و null به این معنا در نظر گرفته می‌شوند که نگاشت extra وجود ندارد.
مقادیر رشته خالی که درون یک آرایه رشته‌ای قرار دارند، فیلتر و حذف می‌شوند.</p>
<p>عبارت‌های CEL به محتوای claims توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claim است.
برای مثال، متغیری با نام 'sub' از طریق 'claims.sub' قابل دسترسی است.
claimهای تو در تو را می‌توان با نمادگذاری نقطه‌ای مانند 'claims.foo.bar' در دسترس قرار داد.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
</tbody>
</table>

## `Issuer`     {#apiserver-k8s-io-v1beta1-Issuer}
    

**نمایش داده می‌شود در:**

- [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)


<p>Issuer پیکربندی تنظیمات مختص یک ارائه‌دهنده خارجی را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>url</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>url به نشانی issuer با قالب https://url یا https://url/path اشاره می‌کند.
این مقدار باید با claim با نام «iss» در JWT ارائه‌شده و با issuer بازگردانده‌شده از discovery مطابقت داشته باشد.
مقدار آن با پرچم --oidc-issuer-url یکسان است.
اطلاعات discovery از «{url}/.well-known/openid-configuration» دریافت می‌شود، مگر اینکه با discoveryURL بازنویسی شده باشد.
این مقدار باید میان تمام authenticatorهای JWT یکتا باشد.
توجه کنید که پیکربندی egress selection برای این اتصال شبکه‌ای استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>discoveryURL</code><br/>
<code>string</code>
</td>
<td>
   <p>discoveryURL، در صورت مشخص شدن، نشانی مورد استفاده برای دریافت اطلاعات discovery را
به‌جای «{url}/.well-known/openid-configuration» بازنویسی می‌کند.
مقدار مشخص‌شده دقیقاً به همان صورت استفاده می‌شود؛ بنابراین در صورت نیاز باید
«/.well-known/openid-configuration» در discoveryURL گنجانده شود.</p>
<p>فیلد «issuer» در اطلاعات discovery دریافت‌شده باید با فیلد «issuer.url»
در AuthenticationConfiguration مطابقت داشته باشد و برای اعتبارسنجی claim با نام «iss» در JWT ارائه‌شده استفاده می‌شود.
این برای سناریوهایی است که در آن‌ها endpointهای well-known و jwks در مکانی متفاوت از issuer
(مثلاً به‌صورت محلی در کلاستر) میزبانی می‌شوند.</p>
<p>مثال:
نشانی discovery که با استفاده از Service کوبرنتیز با نام 'oidc' در فضای نام (namespace) با نام 'oidc-namespace' در دسترس قرار گرفته است
و اطلاعات discovery در '/.well-known/openid-configuration' در دسترس است.
discoveryURL: &quot;https://oidc.oidc-namespace/.well-known/openid-configuration&quot;
certificateAuthority برای تأیید اتصال TLS استفاده می‌شود و نام میزبان در گواهی برگ (leaf)
باید روی 'oidc.oidc-namespace' تنظیم شده باشد.</p>
<p>curl https://oidc.oidc-namespace/.well-known/openid-configuration (.discoveryURL field)
{
issuer: &quot;https://oidc.example.com&quot; (.url field)
}</p>
<p>discoveryURL باید با url متفاوت باشد.
این مقدار باید میان تمام authenticatorهای JWT یکتا باشد.
توجه کنید که پیکربندی egress selection برای این اتصال شبکه‌ای استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>certificateAuthority</code><br/>
<code>string</code>
</td>
<td>
   <p>certificateAuthority شامل گواهی‌های مرجع گواهی (certificate authority) با کدگذاری PEM است
که برای اعتبارسنجی اتصال هنگام دریافت اطلاعات discovery استفاده می‌شود.
در صورت تنظیم نشدن، از تأییدکننده سیستم استفاده می‌شود.
مقدار آن با محتوای فایلی که پرچم --oidc-ca-file به آن اشاره می‌کند یکسان است.</p>
</td>
</tr>
<tr><td><code>audiences</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>audiences مجموعه مخاطبان (audience) قابل‌قبولی است که JWT باید برای آن‌ها صادر شده باشد.
دست‌کم یکی از مدخل‌ها باید با claim با نام «aud» در JWTهای ارائه‌شده مطابقت داشته باشد.
مقدار آن با پرچم --oidc-client-id یکسان است (هرچند این فیلد از آرایه پشتیبانی می‌کند).
باید غیرخالی باشد.</p>
</td>
</tr>
<tr><td><code>audienceMatchPolicy</code><br/>
<a href="#apiserver-k8s-io-v1beta1-AudienceMatchPolicyType"><code>AudienceMatchPolicyType</code></a>
</td>
<td>
   <p>audienceMatchPolicy تعیین می‌کند فیلد «audiences» چگونه برای تطبیق با claim با نام «aud» در JWT ارائه‌شده استفاده شود.
مقادیر مجاز عبارت‌اند از:</p>
<ol>
<li>«MatchAny» هنگامی که چند audience مشخص شده باشد و</li>
<li>خالی (یا تنظیم‌نشده) یا «MatchAny» هنگامی که یک audience مشخص شده باشد.</li>
</ol>
<ul>
<li>
<p>MatchAny: claim با نام «aud» در JWT ارائه‌شده باید دست‌کم با یکی از مدخل‌های فیلد «audiences» مطابقت داشته باشد.
برای مثال، اگر «audiences» برابر [&quot;foo&quot;, &quot;bar&quot;] باشد، claim با نام «aud» در JWT ارائه‌شده باید شامل «foo» یا «bar» باشد (و ممکن است شامل هر دو باشد).</p>
</li>
<li>
<p>&quot;&quot;: هنگامی که در فیلد «audiences» یک audience مشخص شده باشد، سیاست تطبیق می‌تواند خالی (یا تنظیم‌نشده) باشد. claim با نام «aud» در JWT ارائه‌شده باید شامل همان audience واحد باشد (و ممکن است شامل موارد دیگر نیز باشد).</p>
</li>
</ul>
<p>برای اعتبارسنجی دقیق‌تر audience، از claimValidationRules استفاده کنید.
مثال: claimValidationRule[].expression: 'sets.equivalent(claims.aud, [&quot;bar&quot;, &quot;foo&quot;, &quot;baz&quot;])' برای الزام به تطابق دقیق.</p>
</td>
</tr>
<tr><td><code>egressSelectorType</code><br/>
<a href="#apiserver-k8s-io-v1beta1-EgressSelectorType"><code>EgressSelectorType</code></a>
</td>
<td>
   <p>egressSelectorType نشان‌دهنده آن است که کدام egress selection باید برای ارسال تمام ترافیک مربوط
به این issuer (discovery، JWKS، claimهای توزیع‌شده و غیره) استفاده شود. در صورت مشخص نشدن، هیچ dialer سفارشی استفاده نمی‌شود.
در صورت مشخص شدن، گزینه‌های معتبر «controlplane» و «cluster» هستند. این‌ها با
مقادیر متناظر در --egress-selector-config-file مطابقت دارند.</p>
<ul>
<li>
<p>controlplane: برای ترافیکی که قرار است به control plane برود.</p>
</li>
<li>
<p>cluster: برای ترافیکی که قرار است به سامانه تحت مدیریت کوبرنتیز برود.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `JWTAuthenticator`     {#apiserver-k8s-io-v1beta1-JWTAuthenticator}
    

**نمایش داده می‌شود در:**

- [AuthenticationConfiguration](#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)


<p>JWTAuthenticator پیکربندی یک authenticator منفرد JWT را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>issuer</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-Issuer"><code>Issuer</code></a>
</td>
<td>
   <p>issuer شامل گزینه‌های پایه اتصال به ارائه‌دهنده OIDC است.</p>
</td>
</tr>
<tr><td><code>claimValidationRules</code><br/>
<a href="#apiserver-k8s-io-v1beta1-ClaimValidationRule"><code>[]ClaimValidationRule</code></a>
</td>
<td>
   <p>claimValidationRules قواعدی هستند که برای اعتبارسنجی claimهای توکن به‌منظور احراز هویت کاربران اعمال می‌شوند.</p>
</td>
</tr>
<tr><td><code>claimMappings</code> <B>[الزامی]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-ClaimMappings"><code>ClaimMappings</code></a>
</td>
<td>
   <p>claimMappings مشخص می‌کند کدام claimهای یک توکن به‌عنوان ویژگی‌های کاربر در نظر گرفته شوند.</p>
</td>
</tr>
<tr><td><code>userValidationRules</code><br/>
<a href="#apiserver-k8s-io-v1beta1-UserValidationRule"><code>[]UserValidationRule</code></a>
</td>
<td>
   <p>userValidationRules قواعدی هستند که پیش از تکمیل احراز هویت بر کاربر نهایی اعمال می‌شوند.
این قواعد امکان اعمال شرایط ثابت (invariant) بر هویت‌های ورودی را فراهم می‌کنند، مانند جلوگیری از
استفاده از پیشوند system: که معمولاً توسط مؤلفه‌های کوبرنتیز استفاده می‌شود.
قواعد اعتبارسنجی از نظر منطقی با AND با هم ترکیب می‌شوند و برای موفقیت اعتبارسنجی همگی باید true برگردانند.</p>
</td>
</tr>
</tbody>
</table>

## `PrefixedClaimOrExpression`     {#apiserver-k8s-io-v1beta1-PrefixedClaimOrExpression}
    

**نمایش داده می‌شود در:**

- [ClaimMappings](#apiserver-k8s-io-v1beta1-ClaimMappings)


<p>PrefixedClaimOrExpression پیکربندی یک claim دارای پیشوند یا یک عبارت منفرد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim همان claim از JWT است که باید استفاده شود.
با expression متقابلاً ناسازگار است (mutually exclusive).</p>
</td>
</tr>
<tr><td><code>prefix</code><br/>
<code>string</code>
</td>
<td>
   <p>prefix به ابتدای مقدار claim افزوده می‌شود تا از تداخل با نام‌های موجود جلوگیری شود.
اگر claim تنظیم شده باشد، prefix نیز باید تنظیم شود و می‌تواند رشته خالی باشد.
با expression متقابلاً ناسازگار است.</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression نمایانگر عبارتی است که توسط CEL ارزیابی خواهد شد.</p>
<p>عبارت‌های CEL به محتوای claims توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claim است.
برای مثال، متغیری با نام 'sub' از طریق 'claims.sub' قابل دسترسی است.
claimهای تو در تو را می‌توان با نمادگذاری نقطه‌ای مانند 'claims.foo.bar' در دسترس قرار داد.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim و prefix متقابلاً ناسازگار است.</p>
</td>
</tr>
</tbody>
</table>

## `ProtocolType`     {#apiserver-k8s-io-v1beta1-ProtocolType}
    
(نام مستعار برای `string`)

**نمایش داده می‌شود در:**

- [Connection](#apiserver-k8s-io-v1beta1-Connection)


<p>ProtocolType مجموعه‌ای از مقادیر معتبر برای Connection.ProtocolType است.</p>




## `TCPTransport`     {#apiserver-k8s-io-v1beta1-TCPTransport}
    

**نمایش داده می‌شود در:**

- [Transport](#apiserver-k8s-io-v1beta1-Transport)


<p>TCPTransport اطلاعات لازم برای اتصال به سرور konnectivity از طریق TCP را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>url</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>URL نشانی سرور konnectivity است که باید به آن متصل شد.
برای مثال می‌تواند &quot;https://127.0.0.1:8131&quot; باشد.</p>
</td>
</tr>
<tr><td><code>tlsConfig</code><br/>
<a href="#apiserver-k8s-io-v1beta1-TLSConfig"><code>TLSConfig</code></a>
</td>
<td>
   <p>TLSConfig پیکربندی لازم برای استفاده از TLS هنگام اتصال به سرور konnectivity است.</p>
</td>
</tr>
</tbody>
</table>

## `TLSConfig`     {#apiserver-k8s-io-v1beta1-TLSConfig}
    

**نمایش داده می‌شود در:**

- [TCPTransport](#apiserver-k8s-io-v1beta1-TCPTransport)


<p>TLSConfig اطلاعات احراز هویت لازم برای اتصال به سرور konnectivity را فراهم می‌کند.
فقط همراه با TCPTransport استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>caBundle</code><br/>
<code>string</code>
</td>
<td>
   <p>caBundle مسیر فایل مرجع گواهی (CA) است که برای تعیین اعتماد به سرور konnectivity استفاده می‌شود.
اگر TCPTransport.URL با http:// آغاز شده باشد، باید موجود نباشد یا خالی باشد.
اگر TCPTransport.URL با https:// آغاز شده باشد و این مقدار تعیین نشده باشد، از ریشه‌های اعتماد سیستم استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>clientKey</code><br/>
<code>string</code>
</td>
<td>
   <p>clientKey مسیر فایل کلید کلاینت است که در handshakeهای mtls با سرور konnectivity استفاده می‌شود.
اگر TCPTransport.URL با http:// آغاز شده باشد، باید موجود نباشد یا خالی باشد.
اگر TCPTransport.URL با https:// آغاز شده باشد، باید پیکربندی شود.</p>
</td>
</tr>
<tr><td><code>clientCert</code><br/>
<code>string</code>
</td>
<td>
   <p>clientCert مسیر فایل گواهی کلاینت است که در handshakeهای mtls با سرور konnectivity استفاده می‌شود.
اگر TCPTransport.URL با http:// آغاز شده باشد، باید موجود نباشد یا خالی باشد.
اگر TCPTransport.URL با https:// آغاز شده باشد، باید پیکربندی شود.</p>
</td>
</tr>
<tr><td><code>tlsServerName</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsServerName برای بررسی گواهی سرور استفاده می‌شود. اگر tlsServerName خالی باشد، از نام میزبانی که برای تماس با سرور استفاده شده است، استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `Transport`     {#apiserver-k8s-io-v1beta1-Transport}
    

**نمایش داده می‌شود در:**

- [Connection](#apiserver-k8s-io-v1beta1-Connection)


<p>Transport پیکربندی‌های انتقالی را تعریف می‌کند که برای برقراری اتصال با سرور konnectivity استفاده می‌کنیم.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>tcp</code><br/>
<a href="#apiserver-k8s-io-v1beta1-TCPTransport"><code>TCPTransport</code></a>
</td>
<td>
   <p>TCP پیکربندی TCP برای ارتباط با سرور konnectivity از طریق TCP است.
ProxyProtocol مربوط به GRPC در حال حاضر با انتقال TCP پشتیبانی نمی‌شود.
نیازمند آن است که دست‌کم یکی از TCP یا UDS تنظیم شده باشد.</p>
</td>
</tr>
<tr><td><code>uds</code><br/>
<a href="#apiserver-k8s-io-v1beta1-UDSTransport"><code>UDSTransport</code></a>
</td>
<td>
   <p>UDS پیکربندی UDS برای ارتباط با سرور konnectivity از طریق UDS است.
نیازمند آن است که دست‌کم یکی از TCP یا UDS تنظیم شده باشد.</p>
</td>
</tr>
</tbody>
</table>

## `UDSTransport`     {#apiserver-k8s-io-v1beta1-UDSTransport}
    

**نمایش داده می‌شود در:**

- [Transport](#apiserver-k8s-io-v1beta1-Transport)


<p>UDSTransport اطلاعات لازم برای اتصال به سرور konnectivity از طریق UDS را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>udsName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>UDSName نام unix domain socket است که برای اتصال به سرور konnectivity استفاده می‌شود.
این مقدار از پیشوند unix:// استفاده نمی‌کند. (برای مثال: /etc/srv/kubernetes/konnectivity-server/konnectivity-server.socket)</p>
</td>
</tr>
</tbody>
</table>

## `UserValidationRule`     {#apiserver-k8s-io-v1beta1-UserValidationRule}
    

**نمایش داده می‌شود در:**

- [JWTAuthenticator](#apiserver-k8s-io-v1beta1-JWTAuthenticator)


<p>UserValidationRule پیکربندی یک قاعده اعتبارسنجی منفرد برای اطلاعات کاربر (user info) را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>expression</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>expression نمایانگر عبارتی است که توسط CEL ارزیابی خواهد شد.
برای موفقیت اعتبارسنجی باید true برگرداند.</p>
<p>عبارت‌های CEL به محتوای UserInfo دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده است:</p>
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
   <p>message پیام خطای بازگردانده‌شده را زمانی که قاعده false برمی‌گرداند، سفارشی می‌کند.
message یک رشته literal است.</p>
</td>
</tr>
</tbody>
</table>

## `WebhookConfiguration`     {#apiserver-k8s-io-v1beta1-WebhookConfiguration}
    

**Appears in:**

- [AuthorizerConfiguration](#apiserver-k8s-io-v1beta1-AuthorizerConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>authorizedTTL</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمان نگهداری (cache) پاسخ‌های «authorized» از authorizer مبتنی بر webhook.
معادل تنظیم فلگ <code>--authorization-webhook-cache-authorized-ttl</code> است.
مقدار پیش‌فرض: 5m0s</p>
</td>
</tr>
<tr><td><code>cacheAuthorizedRequests</code><br/>
<code>bool</code>
</td>
<td>
   <p>CacheAuthorizedRequests مشخص می‌کند که آیا درخواست‌های مجاز باید cache شوند یا خیر.
اگر روی true تنظیم شود، TTL تصمیم‌های ذخیره‌شده در cache را می‌توان از طریق
فیلد AuthorizedTTL پیکربندی کرد.
مقدار پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>unauthorizedTTL</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمان نگهداری (cache) پاسخ‌های «unauthorized» از authorizer مبتنی بر webhook.
معادل تنظیم فلگ <code>--authorization-webhook-cache-unauthorized-ttl</code> است.
مقدار پیش‌فرض: 30s</p>
</td>
</tr>
<tr><td><code>cacheUnauthorizedRequests</code><br/>
<code>bool</code>
</td>
<td>
   <p>CacheUnauthorizedRequests مشخص می‌کند که آیا درخواست‌های غیرمجاز باید cache شوند یا خیر.
اگر روی true تنظیم شود، TTL تصمیم‌های ذخیره‌شده در cache را می‌توان از طریق
فیلد UnauthorizedTTL پیکربندی کرد.
مقدار پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>timeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مهلت زمانی (timeout) درخواست webhook.
حداکثر مقدار مجاز 30s است.
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>subjectAccessReviewVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه API مربوط به SubjectAccessReview از authorization.k8s.io که باید
به webhook ارسال شود و از آن انتظار می‌رود.
معادل تنظیم فلگ <code>--authorization-webhook-version</code> است.
مقادیر معتبر: v1beta1، v1
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>matchConditionSubjectAccessReviewVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>MatchConditionSubjectAccessReviewVersion نسخه‌ای از SubjectAccessReview را مشخص می‌کند
که عبارت‌های CEL بر اساس آن ارزیابی می‌شوند.
مقادیر معتبر: v1
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>failurePolicy</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>تصمیم مجوزدهی را زمانی کنترل می‌کند که درخواست webhook به پایان نرسد،
پاسخی نامعتبر برگرداند یا ارزیابی matchConditions با خطا مواجه شود.
مقادیر معتبر:</p>
<ul>
<li>NoOpinion: ادامه به authorizerهای بعدی تا بررسی شود که آیا یکی از
آن‌ها درخواست را مجاز می‌کند یا خیر</li>
<li>Deny: رد درخواست بدون مراجعه به authorizerهای بعدی
الزامی است و مقدار پیش‌فرض ندارد.</li>
</ul>
</td>
</tr>
<tr><td><code>connectionInfo</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-WebhookConnectionInfo"><code>WebhookConnectionInfo</code></a>
</td>
<td>
   <p>ConnectionInfo نحوه ارتباط با webhook را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>matchConditions</code> <B>[Required]</B><br/>
<a href="#apiserver-k8s-io-v1beta1-WebhookMatchCondition"><code>[]WebhookMatchCondition</code></a>
</td>
<td>
   <p>matchConditions فهرستی از شرایطی است که باید برقرار باشند تا یک درخواست به این
webhook ارسال شود. فهرست خالی matchConditions با همه درخواست‌ها مطابقت دارد.
حداکثر ۶۴ شرط تطبیق مجاز است.</p>
<p>منطق دقیق تطبیق به این ترتیب است:</p>
<ol>
<li>اگر دست‌کم یک matchCondition برابر FALSE ارزیابی شود، webhook نادیده گرفته می‌شود.</li>
<li>اگر همه matchConditionها برابر TRUE ارزیابی شوند، webhook فراخوانی می‌شود.</li>
<li>اگر دست‌کم یک matchCondition با خطا ارزیابی شود (اما هیچ‌کدام FALSE نباشند):
<ul>
<li>اگر failurePolicy=Deny باشد، webhook درخواست را رد می‌کند</li>
<li>اگر failurePolicy=NoOpinion باشد، خطا نادیده گرفته می‌شود و webhook رد می‌شود (فراخوانی نمی‌شود)</li>
</ul>
</li>
</ol>
</td>
</tr>
</tbody>
</table>

## `WebhookConnectionInfo`     {#apiserver-k8s-io-v1beta1-WebhookConnectionInfo}
    

**Appears in:**

- [WebhookConfiguration](#apiserver-k8s-io-v1beta1-WebhookConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نحوه ارتباط webhook با سرور را کنترل می‌کند.
مقادیر معتبر:</p>
<ul>
<li>KubeConfigFile: از فایل مشخص‌شده در kubeConfigFile برای یافتن
سرور استفاده می‌شود.</li>
<li>InClusterConfig: از پیکربندی درون‌کلاستری برای فراخوانی
SubjectAccessReview API که توسط kube-apiserver ارائه می‌شود استفاده می‌شود. این حالت
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

## `WebhookMatchCondition`     {#apiserver-k8s-io-v1beta1-WebhookMatchCondition}
    

**Appears in:**

- [WebhookConfiguration](#apiserver-k8s-io-v1beta1-WebhookConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>expression</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی است که توسط CEL ارزیابی خواهد شد و باید نتیجه آن از نوع bool باشد.
عبارت‌های CEL به محتوای SubjectAccessReview در نسخه v1 دسترسی دارند.
اگر نسخه مشخص‌شده توسط subjectAccessReviewVersion در متغیر request برابر v1beta1 باشد،
محتوا پیش از ارزیابی عبارت CEL به نسخه v1 تبدیل می‌شود.</p>
<ul>
<li>'resourceAttributes' اطلاعات مربوط به یک درخواست دسترسی به منبع را توصیف می‌کند و برای درخواست‌های غیرمنبعی تنظیم نمی‌شود. برای مثال: has(request.resourceAttributes) &amp;&amp; request.resourceAttributes.namespace == 'default'</li>
<li>'nonResourceAttributes' اطلاعات مربوط به یک درخواست دسترسی غیرمنبعی را توصیف می‌کند و برای درخواست‌های منبعی تنظیم نمی‌شود. برای مثال: has(request.nonResourceAttributes) &amp;&amp; request.nonResourceAttributes.path == '/healthz'.</li>
<li>'user' کاربری است که باید بررسی شود. برای مثال: request.user == 'alice'</li>
<li>'groups' گروه‌هایی است که باید بررسی شوند. برای مثال: ('group1' in request.groups)</li>
<li>'extra' با متد user.Info.GetExtra() از authenticator متناظر است.</li>
<li>'uid' اطلاعات مربوط به کاربر درخواست‌کننده است. برای مثال: request.uid == '1'</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
</tbody>
</table>
