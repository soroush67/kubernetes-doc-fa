---
title: پیکربندی kube-apiserver (v1)
content_type: tool-reference
package: apiserver.config.k8s.io/v1
auto_generated: true
---
<p>بسته v1 نسخه v1 از API است.</p>


## انواع منبع 


- [AdmissionConfiguration](#apiserver-config-k8s-io-v1-AdmissionConfiguration)
- [AuthenticationConfiguration](#apiserver-config-k8s-io-v1-AuthenticationConfiguration)
- [AuthorizationConfiguration](#apiserver-config-k8s-io-v1-AuthorizationConfiguration)
- [EncryptionConfiguration](#apiserver-config-k8s-io-v1-EncryptionConfiguration)
- [TracingConfiguration](#apiserver-config-k8s-io-v1-TracingConfiguration)
  
    
    

## `TracingConfiguration`     {#TracingConfiguration}
    

**ظاهر می‌شود در:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)

- [TracingConfiguration](#apiserver-config-k8s-io-v1-TracingConfiguration)

- [TracingConfiguration](#apiserver-k8s-io-v1alpha1-TracingConfiguration)

- [TracingConfiguration](#apiserver-k8s-io-v1beta1-TracingConfiguration)


<p>TracingConfiguration پیکربندی نسخه‌بندی‌شده را برای کلاینت‌های ردیابی (tracing) OpenTelemetry فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>نشانی Endpoint مربوط به collector که این مؤلفه ردیابی‌ها (traces) را به آن گزارش می‌کند.
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
span والد خود پیروی می‌کند، و در غیر این صورت هرگز نمونه‌برداری نمی‌کند.</p>
</td>
</tr>
</tbody>
</table>
  

## `AdmissionConfiguration`     {#apiserver-config-k8s-io-v1-AdmissionConfiguration}
    


<p>AdmissionConfiguration پیکربندی نسخه‌بندی‌شده را برای admission controllerها فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AdmissionConfiguration</code></td></tr>
    
  
<tr><td><code>plugins</code><br/>
<a href="#apiserver-config-k8s-io-v1-AdmissionPluginConfiguration"><code>[]AdmissionPluginConfiguration</code></a>
</td>
<td>
   <p>Plugins امکان تعیین پیکربندی به ازای هر افزونه کنترل پذیرش (admission control) را فراهم می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `AuthenticationConfiguration`     {#apiserver-config-k8s-io-v1-AuthenticationConfiguration}
    


<p>AuthenticationConfiguration پیکربندی نسخه‌بندی‌شده را برای احراز هویت فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AuthenticationConfiguration</code></td></tr>
    
  
<tr><td><code>jwt</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-JWTAuthenticator"><code>[]JWTAuthenticator</code></a>
</td>
<td>
   <p>jwt فهرستی از احراز‌هویت‌کننده‌ها (authenticator) برای احراز هویت کاربران کوبرنتیز
با استفاده از توکن‌های سازگار با JWT است. احراز‌هویت‌کننده تلاش می‌کند یک ID token خام را تجزیه کند
و بررسی کند که توسط issuer پیکربندی‌شده امضا شده است. کلید عمومی لازم برای تأیید
امضا با استفاده از OIDC discovery از نقطه پایانی عمومی issuer کشف می‌شود.
برای هر توکن ورودی، هر احراز‌هویت‌کننده JWT به همان ترتیبی که در این فهرست مشخص شده است
آزموده می‌شود. توجه کنید که
سایر احراز‌هویت‌کننده‌ها ممکن است پیش از احراز‌هویت‌کننده‌های JWT یا پس از آن‌ها اجرا شوند.
جایگاه دقیق احراز‌هویت‌کننده‌های JWT نسبت به سایر
احراز‌هویت‌کننده‌ها نه تعریف شده است و نه در طول نسخه‌ها پایدار می‌ماند. از آنجا که
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
<a href="#apiserver-config-k8s-io-v1-AnonymousAuthConfig"><code>AnonymousAuthConfig</code></a>
</td>
<td>
   <p>در صورت وجود، نباید --anonymous-auth تنظیم شده باشد</p>
</td>
</tr>
</tbody>
</table>

## `AuthorizationConfiguration`     {#apiserver-config-k8s-io-v1-AuthorizationConfiguration}
    



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AuthorizationConfiguration</code></td></tr>
    
  
<tr><td><code>authorizers</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-AuthorizerConfiguration"><code>[]AuthorizerConfiguration</code></a>
</td>
<td>
   <p>Authorizers فهرستی مرتب از مجوزدهنده‌ها (authorizer) است که درخواست‌ها
در برابر آن‌ها مجاز شناخته می‌شوند.
این مورد مشابه فلگ --authorization-modes در kube-apiserver است.
باید دست‌کم یک مورد وجود داشته باشد.</p>
</td>
</tr>
</tbody>
</table>

## `EncryptionConfiguration`     {#apiserver-config-k8s-io-v1-EncryptionConfiguration}
    


<p>EncryptionConfiguration پیکربندی کامل ارائه‌دهندگان رمزنگاری را نگهداری می‌کند.
همچنین امکان استفاده از wildcardها را برای تعیین منابعی که باید رمزنگاری شوند فراهم می‌کند.
برای رمزنگاری همه منابع درون یک گروه از '<em>.<!-- raw HTML omitted -->' و برای رمزنگاری همه منابع از '</em>.<em>' استفاده کنید.
'</em>.' را می‌توان برای رمزنگاری همه منابع در گروه core به کار برد. '<em>.</em>' همه
منابع را رمزنگاری می‌کند، حتی منابع سفارشی‌ای که پس از راه‌اندازی API server اضافه می‌شوند.
استفاده از wildcardهایی که در یک فهرست منابع یا میان چند
ورودی هم‌پوشانی دارند مجاز نیست، زیرا بخشی از پیکربندی بی‌اثر خواهد بود.
فهرست‌های منابع به ترتیب پردازش می‌شوند و فهرست‌های قبلی تقدم دارند.</p>
<p>مثال:</p>
<pre><code>kind: EncryptionConfiguration
apiVersion: apiserver.config.k8s.io/v1
resources:
- resources:
  - events
  providers:
  - identity: {}  # do not encrypt events even though *.* is specified below
- resources:
  - secrets
  - configmaps
  - pandas.awesome.bears.example
  providers:
  - aescbc:
      keys:
      - name: key1
        secret: c2VjcmV0IGlzIHNlY3VyZQ==
- resources:
  - '*.apps'
  providers:
  - aescbc:
      keys:
      - name: key2
        secret: c2VjcmV0IGlzIHNlY3VyZSwgb3IgaXMgaXQ/Cg==
- resources:
  - '*.*'
  providers:
  - aescbc:
      keys:
      - name: key3
        secret: c2VjcmV0IGlzIHNlY3VyZSwgSSB0aGluaw==
</code></pre>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>EncryptionConfiguration</code></td></tr>
    
  
<tr><td><code>resources</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-ResourceConfiguration"><code>[]ResourceConfiguration</code></a>
</td>
<td>
   <p>resources فهرستی شامل منابع و ارائه‌دهندگان رمزنگاری متناظر با آن‌هاست.</p>
</td>
</tr>
</tbody>
</table>

## `TracingConfiguration`     {#apiserver-config-k8s-io-v1-TracingConfiguration}
    


<p>TracingConfiguration پیکربندی نسخه‌بندی‌شده را برای کلاینت‌های ردیابی (tracing) فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>TracingConfiguration</code></td></tr>
    
  
<tr><td><code>TracingConfiguration</code> <B>[الزامی]</B><br/>
<a href="#TracingConfiguration"><code>TracingConfiguration</code></a>
</td>
<td>
   <p>ساختار (struct) پیکربندی ردیابی پیکربندی مؤلفه را به‌صورت تعبیه‌شده (embed) در خود جای می‌دهد</p>
</td>
</tr>
</tbody>
</table>

## `AESConfiguration`     {#apiserver-config-k8s-io-v1-AESConfiguration}
    

**ظاهر می‌شود در:**

- [ProviderConfiguration](#apiserver-config-k8s-io-v1-ProviderConfiguration)


<p>AESConfiguration شامل پیکربندی API برای یک transformer از نوع AES است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>keys</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-Key"><code>[]Key</code></a>
</td>
<td>
   <p>keys فهرستی از کلیدهاست که برای ساخت transformer از نوع AES به کار می‌رود.
هر کلید باید برای AES-CBC دقیقاً ۳۲ بایت و برای AES-GCM ۱۶، ۲۴ یا ۳۲ بایت طول داشته باشد.</p>
</td>
</tr>
</tbody>
</table>

## `AdmissionPluginConfiguration`     {#apiserver-config-k8s-io-v1-AdmissionPluginConfiguration}
    

**ظاهر می‌شود در:**

- [AdmissionConfiguration](#apiserver-config-k8s-io-v1-AdmissionConfiguration)


<p>AdmissionPluginConfiguration پیکربندی یک افزونه (plug-in) واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام admission controller است.
باید با نام افزونه پذیرش (admission plugin) ثبت‌شده مطابقت داشته باشد.</p>
</td>
</tr>
<tr><td><code>path</code><br/>
<code>string</code>
</td>
<td>
   <p>Path مسیر فایل پیکربندی‌ای است که پیکربندی
افزونه را در خود دارد</p>
</td>
</tr>
<tr><td><code>configuration</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Unknown"><code>k8s.io/apimachinery/pkg/runtime.Unknown</code></a>
</td>
<td>
   <p>Configuration یک آبجکت پیکربندی تعبیه‌شده است که به‌عنوان پیکربندی افزونه به کار می‌رود.
در صورت وجود، به‌جای مسیر فایل پیکربندی از آن استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `AnonymousAuthCondition`     {#apiserver-config-k8s-io-v1-AnonymousAuthCondition}
    

**ظاهر می‌شود در:**

- [AnonymousAuthConfig](#apiserver-config-k8s-io-v1-AnonymousAuthConfig)


<p>AnonymousAuthCondition شرطی را توصیف می‌کند که تحت آن احراز هویت ناشناس
باید فعال شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>path</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Path مسیری که احراز هویت ناشناس برای آن فعال است.</p>
</td>
</tr>
</tbody>
</table>

## `AnonymousAuthConfig`     {#apiserver-config-k8s-io-v1-AnonymousAuthConfig}
    

**ظاهر می‌شود در:**

- [AuthenticationConfiguration](#apiserver-config-k8s-io-v1-AuthenticationConfiguration)


<p>AnonymousAuthConfig پیکربندی احراز‌هویت‌کننده ناشناس را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>enabled</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>conditions</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-AnonymousAuthCondition"><code>[]AnonymousAuthCondition</code></a>
</td>
<td>
   <p>در صورت تنظیم، احراز هویت ناشناس تنها زمانی مجاز است که درخواست یکی از
شرط‌ها را برآورده کند.</p>
</td>
</tr>
</tbody>
</table>

## `AudienceMatchPolicyType`     {#apiserver-config-k8s-io-v1-AudienceMatchPolicyType}
    
(نام مستعار برای `string`)

**ظاهر می‌شود در:**

- [Issuer](#apiserver-config-k8s-io-v1-Issuer)


<p>AudienceMatchPolicyType مجموعه‌ای از مقادیر معتبر برای issuer.audienceMatchPolicy است</p>




## `AuthorizerConfiguration`     {#apiserver-config-k8s-io-v1-AuthorizerConfiguration}
    

**ظاهر می‌شود در:**

- [AuthorizationConfiguration](#apiserver-config-k8s-io-v1-AuthorizationConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Type به نوع مجوزدهنده (authorizer) اشاره دارد.
&quot;Webhook&quot; در API server عمومی پشتیبانی می‌شود.
سایر API serverها ممکن است از انواع مجوزدهنده اضافی
مانند Node، RBAC، ABAC و غیره پشتیبانی کنند.</p>
</td>
</tr>
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name برای توصیف webhook به کار می‌رود.
این نام به‌صراحت در سازوکار پایش برای معیارها (metrics) استفاده می‌شود.
توجه: نام‌ها باید برچسب‌های DNS1123 مانند <code>myauthorizername</code> یا
زیردامنه‌هایی مانند <code>myauthorizer.example.domain</code> باشند.
الزامی است و مقدار پیش‌فرض ندارد</p>
</td>
</tr>
<tr><td><code>webhook</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-WebhookConfiguration"><code>WebhookConfiguration</code></a>
</td>
<td>
   <p>Webhook پیکربندی یک مجوزدهنده از نوع Webhook را تعریف می‌کند.
وقتی Type=Webhook است باید تعریف شود.
وقتی Type!=Webhook است نباید تعریف شود.</p>
</td>
</tr>
</tbody>
</table>

## `ClaimMappings`     {#apiserver-config-k8s-io-v1-ClaimMappings}
    

**ظاهر می‌شود در:**

- [JWTAuthenticator](#apiserver-config-k8s-io-v1-JWTAuthenticator)


<p>ClaimMappings پیکربندی نگاشت claim را فراهم می‌کند</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>username</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-PrefixedClaimOrExpression"><code>PrefixedClaimOrExpression</code></a>
</td>
<td>
   <p>username گزینه‌ای برای ویژگی نام کاربری است.
مقدار claim باید یک رشته منفرد باشد.
معادل فلگ‌های --oidc-username-claim و --oidc-username-prefix است.
اگر username.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای تولید کند.
اگر username.expression از 'claims.email' استفاده کند، آنگاه 'claims.email_verified' باید در
username.expression یا extra[<em>].valueExpression یا claimValidationRules[</em>].expression به کار رفته باشد.
نمونه‌ای از عبارت قاعده اعتبارسنجی claim که با اعتبارسنجی اعمال‌شده به‌صورت خودکار
هنگام تنظیم username.claim روی 'email' مطابقت دارد، 'claims.?email_verified.orValue(true) == true' است. با مقایسه صریح
مقدار با true، به بررسی نوع (type-checking) اجازه می‌دهیم ببیند نتیجه یک مقدار بولی خواهد بود، و اطمینان حاصل می‌کنیم که
claim غیربولی email_verified در زمان اجرا شناسایی می‌شود.</p>
<p>در رویکرد مبتنی بر فلگ، --oidc-username-claim و --oidc-username-prefix اختیاری هستند. اگر --oidc-username-claim تنظیم نشود،
مقدار پیش‌فرض &quot;sub&quot; است. در پیکربندی احراز هویت (authentication config) برای claim یا prefix مقدار پیش‌فرضی وجود ندارد. claim و prefix باید به‌صراحت تنظیم شوند.
برای claim، اگر --oidc-username-claim در رویکرد قدیمی مبتنی بر فلگ تنظیم نشده بود، در پیکربندی احراز هویت username.claim=&quot;sub&quot; را پیکربندی کنید.
برای prefix:
(۱) --oidc-username-prefix=&quot;-&quot;، هیچ پیشوندی به نام کاربری افزوده نمی‌شد. برای رفتار یکسان با استفاده از پیکربندی احراز هویت،
username.prefix=&quot;&quot; را تنظیم کنید
(۲) --oidc-username-prefix=&quot;&quot; و  --oidc-username-claim != &quot;email&quot;، پیشوند &quot;&lt;value of --oidc-issuer-url&gt;#&quot; بود. برای
رفتار یکسان با استفاده از پیکربندی احراز هویت، username.prefix=&quot;<!-- raw HTML omitted -->#&quot; را تنظیم کنید
(۳) --oidc-username-prefix=&quot;<!-- raw HTML omitted -->&quot;. برای رفتار یکسان با استفاده از پیکربندی احراز هویت، username.prefix=&quot;<!-- raw HTML omitted -->&quot; را تنظیم کنید</p>
</td>
</tr>
<tr><td><code>groups</code><br/>
<a href="#apiserver-config-k8s-io-v1-PrefixedClaimOrExpression"><code>PrefixedClaimOrExpression</code></a>
</td>
<td>
   <p>groups گزینه‌ای برای ویژگی گروه‌هاست.
مقدار claim باید یک claim از نوع رشته یا آرایه‌ای از رشته‌ها باشد.
اگر groups.claim تنظیم شده باشد، prefix باید مشخص شود (و می‌تواند رشته خالی باشد).
اگر groups.expression تنظیم شده باشد، عبارت باید یک مقدار رشته یا آرایه‌ای از رشته‌ها تولید کند.
مقادیر &quot;&quot;، [] و null به این معنا تلقی می‌شوند که نگاشت گروه وجود ندارد.</p>
</td>
</tr>
<tr><td><code>uid</code><br/>
<a href="#apiserver-config-k8s-io-v1-ClaimOrExpression"><code>ClaimOrExpression</code></a>
</td>
<td>
   <p>uid گزینه‌ای برای ویژگی uid است.
Claim باید یک claim منفرد از نوع رشته باشد.
اگر uid.expression تنظیم شده باشد، عبارت باید یک مقدار رشته‌ای تولید کند.</p>
</td>
</tr>
<tr><td><code>extra</code><br/>
<a href="#apiserver-config-k8s-io-v1-ExtraMapping"><code>[]ExtraMapping</code></a>
</td>
<td>
   <p>extra گزینه‌ای برای ویژگی extra است.
expression باید یک مقدار رشته یا آرایه‌ای از رشته‌ها تولید کند.
اگر مقدار خالی باشد، نگاشت extra وجود نخواهد داشت.</p>
<p>کلید/مقدار extra با مقدار ثابت (hard-coded)</p>
<ul>
<li>key: &quot;foo&quot;
valueExpression: &quot;'bar'&quot;
این به ویژگی extra زیر منجر می‌شود - foo: [&quot;bar&quot;]</li>
</ul>
<p>کلید ثابت، مقدار برگرفته از کپی مقدار claim</p>
<ul>
<li>key: &quot;foo&quot;
valueExpression: &quot;claims.some_claim&quot;
این به ویژگی extra زیر منجر می‌شود - foo: [value of some_claim]</li>
</ul>
<p>کلید ثابت، مقدار مشتق‌شده از مقدار claim</p>
<ul>
<li>key: &quot;admin&quot;
valueExpression: '(has(claims.is_admin) &amp;&amp; claims.is_admin) ? &quot;true&quot;:&quot;&quot;'
این به نتایج زیر منجر می‌شود:</li>
<li>اگر claim با نام is_admin وجود داشته باشد و true باشد، ویژگی extra - admin: [&quot;true&quot;]</li>
<li>اگر claim با نام is_admin وجود داشته باشد و false باشد یا اصلاً وجود نداشته باشد، هیچ ویژگی extra افزوده نخواهد شد</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `ClaimOrExpression`     {#apiserver-config-k8s-io-v1-ClaimOrExpression}
    

**ظاهر می‌شود در:**

- [ClaimMappings](#apiserver-config-k8s-io-v1-ClaimMappings)


<p>ClaimOrExpression پیکربندی یک claim یا عبارت واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim همان claim در JWT است که باید به کار رود.
باید یکی از claim یا expression تنظیم شود.
با expression به‌طور متقابل ناسازگار است (mutually exclusive).</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression عبارتی را نشان می‌دهد که توسط CEL ارزیابی می‌شود.</p>
<p>عبارت‌های CEL به محتوای claimهای توکن دسترسی دارند که در قالب یک متغیر CEL سازمان‌دهی شده‌اند:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claim است.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تودرتو را می‌توان با نشانه‌گذاری نقطه‌ای (dot notation) در دسترس قرار داد، مثلاً 'claims.foo.bar'.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim به‌طور متقابل ناسازگار است (mutually exclusive).</p>
</td>
</tr>
</tbody>
</table>

## `ClaimValidationRule`     {#apiserver-config-k8s-io-v1-ClaimValidationRule}
    

**نمایش داده شده در:**

- [JWTAuthenticator](#apiserver-config-k8s-io-v1-JWTAuthenticator)


<p>ClaimValidationRule پیکربندی یک قاعده اعتبارسنجی claim واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim نام یک claim الزامی است.
معادل پرچم --oidc-required-claim است.
فقط کلیدهای claim از نوع رشته پشتیبانی می‌شوند.
با expression و message متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
<tr><td><code>requiredValue</code><br/>
<code>string</code>
</td>
<td>
   <p>requiredValue مقدار یک claim الزامی است.
معادل پرچم --oidc-required-claim است.
فقط مقادیر claim از نوع رشته پشتیبانی می‌شوند.
اگر claim تنظیم شده باشد و requiredValue تنظیم نشده باشد، claim باید وجود داشته باشد و مقدار آن رشته خالی باشد.
با expression و message متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression بیانگر عبارتی است که توسط CEL ارزیابی خواهد شد.
باید یک مقدار بولین تولید کند.</p>
<p>عبارات CEL به محتوای claimهای توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claimها است.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تو در تو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مانند 'claims.foo.bar'.
برای موفقیت اعتبارسنجی، باید مقدار true برگردانده شود.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim و requiredValue متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
<tr><td><code>message</code><br/>
<code>string</code>
</td>
<td>
   <p>message پیام خطای برگردانده‌شده را زمانی که expression مقدار false برگرداند، سفارشی می‌کند.
message یک رشته لفظی است.
با claim و requiredValue متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
</tbody>
</table>

## `EgressSelectorType`     {#apiserver-config-k8s-io-v1-EgressSelectorType}
    
(نام مستعار برای `string`)

**نمایش داده شده در:**

- [Issuer](#apiserver-config-k8s-io-v1-Issuer)


<p>EgressSelectorType نشان‌دهنده این است که کدام egress selection باید برای ارسال ترافیک استفاده شود.</p>




## `ExtraMapping`     {#apiserver-config-k8s-io-v1-ExtraMapping}
    

**نمایش داده شده در:**

- [ClaimMappings](#apiserver-config-k8s-io-v1-ClaimMappings)


<p>ExtraMapping پیکربندی یک نگاشت extra واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>key</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>key رشته‌ای است که به‌عنوان کلید ویژگی extra استفاده می‌شود.
key باید یک مسیر دارای پیشوند دامنه باشد (مثلاً example.org/foo). تمام نویسه‌های قبل از اولین &quot;/&quot; باید یک
زیردامنه معتبر مطابق RFC 1123 باشند. تمام نویسه‌های بعد از اولین &quot;/&quot; باید
نویسه‌های معتبر مسیر HTTP مطابق RFC 3986 باشند.
key باید با حروف کوچک باشد.
باید یکتا باشد.</p>
</td>
</tr>
<tr><td><code>valueExpression</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>valueExpression یک عبارت CEL برای استخراج مقدار ویژگی extra است.
valueExpression باید یک رشته یا آرایه‌ای از رشته‌ها تولید کند.
مقادیر &quot;&quot;، [] و null به‌منزله وجود نداشتن نگاشت extra در نظر گرفته می‌شوند.
مقادیر رشته خالی موجود در یک آرایه رشته‌ای حذف می‌شوند.</p>
<p>عبارات CEL به محتوای claimهای توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claimها است.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تو در تو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مانند 'claims.foo.bar'.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
</tbody>
</table>

## `IdentityConfiguration`     {#apiserver-config-k8s-io-v1-IdentityConfiguration}
    

**نمایش داده شده در:**

- [ProviderConfiguration](#apiserver-config-k8s-io-v1-ProviderConfiguration)


<p>IdentityConfiguration یک struct خالی است که امکان استفاده از identity transformer را در پیکربندی provider فراهم می‌کند.</p>




## `Issuer`     {#apiserver-config-k8s-io-v1-Issuer}
    

**نمایش داده شده در:**

- [JWTAuthenticator](#apiserver-config-k8s-io-v1-JWTAuthenticator)


<p>Issuer پیکربندی تنظیمات خاص یک provider خارجی را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>url</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>url به نشانی issuer با قالب https://url یا https://url/path اشاره می‌کند.
این مقدار باید با claim «iss» در JWT ارائه‌شده و issuer برگردانده‌شده از discovery مطابقت داشته باشد.
مقدار آن با پرچم --oidc-issuer-url یکسان است.
اطلاعات discovery از &quot;{url}/.well-known/openid-configuration&quot; دریافت می‌شود، مگر اینکه با discoveryURL بازنویسی شود.
باید در میان تمام JWT authenticatorها یکتا باشد.
توجه داشته باشید که پیکربندی egress selection برای این اتصال شبکه استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>discoveryURL</code><br/>
<code>string</code>
</td>
<td>
   <p>discoveryURL، در صورت تعیین، نشانی مورد استفاده برای دریافت اطلاعات discovery را
به‌جای &quot;{url}/.well-known/openid-configuration&quot; بازنویسی می‌کند.
مقدار دقیقاً همان‌گونه که مشخص شده استفاده می‌شود، بنابراین در صورت نیاز، &quot;/.well-known/openid-configuration&quot;
باید در discoveryURL گنجانده شود.</p>
<p>فیلد &quot;issuer&quot; در اطلاعات discovery دریافت‌شده باید با فیلد &quot;issuer.url&quot;
در AuthenticationConfiguration مطابقت داشته باشد و برای اعتبارسنجی claim «iss» در JWT ارائه‌شده استفاده می‌شود.
این قابلیت برای سناریوهایی است که در آن‌ها endpointهای well-known و jwks در مکانی متفاوت از
issuer میزبانی می‌شوند (مانند میزبانی محلی در کلاستر).</p>
<p>مثال:
یک discovery url که با استفاده از Service کوبرنتیز با نام 'oidc' در فضای نام 'oidc-namespace' در دسترس قرار گرفته است
و اطلاعات discovery در '/.well-known/openid-configuration' موجود است.
discoveryURL: &quot;https://oidc.oidc-namespace/.well-known/openid-configuration&quot;
certificateAuthority برای تأیید اتصال TLS استفاده می‌شود و نام میزبان روی leaf certificate
باید روی 'oidc.oidc-namespace' تنظیم شده باشد.</p>
<p>curl https://oidc.oidc-namespace/.well-known/openid-configuration (.discoveryURL field)
{
issuer: &quot;https://oidc.example.com&quot; (.url field)
}</p>
<p>discoveryURL باید با url متفاوت باشد.
باید در میان تمام JWT authenticatorها یکتا باشد.
توجه داشته باشید که پیکربندی egress selection برای این اتصال شبکه استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>certificateAuthority</code><br/>
<code>string</code>
</td>
<td>
   <p>certificateAuthority شامل گواهی‌های مرجع صدور گواهی با کدگذاری PEM است
که برای اعتبارسنجی اتصال هنگام دریافت اطلاعات discovery استفاده می‌شود.
در صورت تنظیم نشدن، از تأییدکننده سیستم استفاده می‌شود.
مقدار آن با محتوای فایلی که پرچم --oidc-ca-file به آن ارجاع می‌دهد یکسان است.</p>
</td>
</tr>
<tr><td><code>audiences</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>audiences مجموعه مخاطبان (audience) قابل‌قبولی است که JWT باید برای آن‌ها صادر شده باشد.
دست‌کم یکی از مدخل‌ها باید با claim «aud» در JWTهای ارائه‌شده مطابقت داشته باشد.
مقدار آن با پرچم --oidc-client-id یکسان است (هرچند این فیلد از آرایه پشتیبانی می‌کند).
باید غیرتهی باشد.</p>
</td>
</tr>
<tr><td><code>audienceMatchPolicy</code><br/>
<a href="#apiserver-config-k8s-io-v1-AudienceMatchPolicyType"><code>AudienceMatchPolicyType</code></a>
</td>
<td>
   <p>audienceMatchPolicy تعیین می‌کند که فیلد &quot;audiences&quot; چگونه برای تطبیق با claim «aud» در JWT ارائه‌شده استفاده می‌شود.
مقادیر مجاز عبارت‌اند از:</p>
<ol>
<li>&quot;MatchAny&quot; هنگامی که چندین audience مشخص شده باشد و</li>
<li>خالی (یا تنظیم‌نشده) یا &quot;MatchAny&quot; هنگامی که یک audience مشخص شده باشد.</li>
</ol>
<ul>
<li>
<p>MatchAny: claim «aud» در JWT ارائه‌شده باید با دست‌کم یکی از مدخل‌های فیلد &quot;audiences&quot; مطابقت داشته باشد.
برای مثال، اگر &quot;audiences&quot; برابر [&quot;foo&quot;, &quot;bar&quot;] باشد، claim «aud» در JWT ارائه‌شده باید شامل &quot;foo&quot; یا &quot;bar&quot; باشد (و ممکن است هر دو را شامل شود).</p>
</li>
<li>
<p>&quot;&quot;: هنگامی که در فیلد &quot;audiences&quot; فقط یک audience مشخص شده باشد، سیاست تطبیق می‌تواند خالی (یا تنظیم‌نشده) باشد. claim «aud» در JWT ارائه‌شده باید شامل همان audience واحد باشد (و ممکن است شامل موارد دیگر نیز باشد).</p>
</li>
</ul>
<p>برای اعتبارسنجی دقیق‌تر audience، از claimValidationRules استفاده کنید.
مثال: claimValidationRule[].expression: 'sets.equivalent(claims.aud, [&quot;bar&quot;, &quot;foo&quot;, &quot;baz&quot;])' برای الزام تطبیق دقیق.</p>
</td>
</tr>
<tr><td><code>egressSelectorType</code><br/>
<a href="#apiserver-config-k8s-io-v1-EgressSelectorType"><code>EgressSelectorType</code></a>
</td>
<td>
   <p>egressSelectorType نشان‌دهنده این است که کدام egress selection باید برای ارسال تمام ترافیک مربوط
به این issuer (discovery، JWKS، claimهای توزیع‌شده و غیره) استفاده شود. اگر تعیین نشود، هیچ dialer سفارشی استفاده نمی‌شود.
در صورت تعیین، گزینه‌های معتبر &quot;controlplane&quot; و &quot;cluster&quot; هستند. این‌ها با
مقادیر متناظر در --egress-selector-config-file مطابقت دارند.</p>
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

## `JWTAuthenticator`     {#apiserver-config-k8s-io-v1-JWTAuthenticator}
    

**نمایش داده شده در:**

- [AuthenticationConfiguration](#apiserver-config-k8s-io-v1-AuthenticationConfiguration)


<p>JWTAuthenticator پیکربندی یک JWT authenticator واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>issuer</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-Issuer"><code>Issuer</code></a>
</td>
<td>
   <p>issuer شامل گزینه‌های پایه اتصال به provider سرویس OIDC است.</p>
</td>
</tr>
<tr><td><code>claimValidationRules</code><br/>
<a href="#apiserver-config-k8s-io-v1-ClaimValidationRule"><code>[]ClaimValidationRule</code></a>
</td>
<td>
   <p>claimValidationRules قواعدی هستند که برای اعتبارسنجی claimهای توکن به‌منظور احراز هویت کاربران اعمال می‌شوند.</p>
</td>
</tr>
<tr><td><code>claimMappings</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-ClaimMappings"><code>ClaimMappings</code></a>
</td>
<td>
   <p>claimMappings مشخص می‌کند که کدام claimهای یک توکن به‌عنوان ویژگی‌های کاربر در نظر گرفته شوند.</p>
</td>
</tr>
<tr><td><code>userValidationRules</code><br/>
<a href="#apiserver-config-k8s-io-v1-UserValidationRule"><code>[]UserValidationRule</code></a>
</td>
<td>
   <p>userValidationRules قواعدی هستند که پیش از تکمیل احراز هویت بر کاربر نهایی اعمال می‌شوند.
این قواعد امکان اعمال ناوردایی‌ها (invariants) را بر هویت‌های ورودی فراهم می‌کنند، مانند جلوگیری از
استفاده از پیشوند system: که معمولاً توسط مؤلفه‌های کوبرنتیز استفاده می‌شود.
قواعد اعتبارسنجی از نظر منطقی با AND با یکدیگر ترکیب می‌شوند و برای موفقیت اعتبارسنجی همگی باید true برگردانند.</p>
</td>
</tr>
</tbody>
</table>

## `KMSConfiguration`     {#apiserver-config-k8s-io-v1-KMSConfiguration}
    

**نمایش داده شده در:**

- [ProviderConfiguration](#apiserver-config-k8s-io-v1-ProviderConfiguration)


<p>KMSConfiguration شامل نام، اندازه کش و مسیر فایل پیکربندی برای یک envelope transformer مبتنی بر KMS است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>apiVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>apiVersion مربوط به KeyManagementService</p>
</td>
</tr>
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام افزونه KMS است که باید استفاده شود.</p>
</td>
</tr>
<tr><td><code>cachesize</code><br/>
<code>int32</code>
</td>
<td>
   <p>cachesize حداکثر تعداد Secretهایی است که در حافظه کش می‌شوند. مقدار پیش‌فرض ۱۰۰۰ است.
برای غیرفعال کردن کش، آن را روی یک مقدار منفی تنظیم کنید. این فیلد فقط برای providerهای KMS v1 مجاز است.</p>
</td>
</tr>
<tr><td><code>endpoint</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>endpoint نشانی شنود سرور gRPC است، برای مثال &quot;unix:///var/run/kms-provider.sock&quot;.</p>
</td>
</tr>
<tr><td><code>timeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>timeout برای فراخوانی‌های gRPC به kms-plugin (مثلاً 5s). مقدار پیش‌فرض ۳ ثانیه است.</p>
</td>
</tr>
</tbody>
</table>

## `Key`     {#apiserver-config-k8s-io-v1-Key}
    

**نمایش داده شده در:**

- [AESConfiguration](#apiserver-config-k8s-io-v1-AESConfiguration)

- [SecretboxConfiguration](#apiserver-config-k8s-io-v1-SecretboxConfiguration)


<p>Key شامل نام و secret کلید ارائه‌شده برای یک transformer است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام کلیدی است که هنگام ذخیره داده‌ها روی دیسک استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>secret</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>secret خود کلید واقعی است که با base64 کدگذاری شده است.</p>
</td>
</tr>
</tbody>
</table>

## `PrefixedClaimOrExpression`     {#apiserver-config-k8s-io-v1-PrefixedClaimOrExpression}
    

**نمایش داده شده در:**

- [ClaimMappings](#apiserver-config-k8s-io-v1-ClaimMappings)


<p>PrefixedClaimOrExpression پیکربندی یک claim دارای پیشوند یا یک عبارت واحد را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>claim</code><br/>
<code>string</code>
</td>
<td>
   <p>claim همان claim در JWT است که باید استفاده شود.
با expression متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
<tr><td><code>prefix</code><br/>
<code>string</code>
</td>
<td>
   <p>prefix به ابتدای مقدار claim افزوده می‌شود تا از تداخل با نام‌های موجود جلوگیری شود.
اگر claim تنظیم شده باشد، prefix نیز باید تنظیم شود و می‌تواند رشته خالی باشد.
با expression متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
<tr><td><code>expression</code><br/>
<code>string</code>
</td>
<td>
   <p>expression بیانگر عبارتی است که توسط CEL ارزیابی خواهد شد.</p>
<p>عبارات CEL به محتوای claimهای توکن دسترسی دارند که در قالب متغیر CEL سازمان‌دهی شده است:</p>
<ul>
<li>'claims' نگاشتی از نام claimها به مقادیر claimها است.
برای مثال، متغیری با نام 'sub' را می‌توان با 'claims.sub' در دسترس قرار داد.
claimهای تو در تو را می‌توان با نمادگذاری نقطه‌ای در دسترس قرار داد، مانند 'claims.foo.bar'.</li>
</ul>
<p>مستندات CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
<p>با claim و prefix متقابلاً ناسازگار است (هم‌زمان قابل استفاده نیستند).</p>
</td>
</tr>
</tbody>
</table>

## `ProviderConfiguration`     {#apiserver-config-k8s-io-v1-ProviderConfiguration}
    

**نمایش داده شده در:**

- [ResourceConfiguration](#apiserver-config-k8s-io-v1-ResourceConfiguration)


<p>ProviderConfiguration پیکربندی ارائه‌شده برای یک provider رمزنگاری را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>aesgcm</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-AESConfiguration"><code>AESConfiguration</code></a>
</td>
<td>
   <p>aesgcm پیکربندی transformer مربوط به AES-GCM است.</p>
</td>
</tr>
<tr><td><code>aescbc</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-AESConfiguration"><code>AESConfiguration</code></a>
</td>
<td>
   <p>aescbc پیکربندی transformer مربوط به AES-CBC است.</p>
</td>
</tr>
<tr><td><code>secretbox</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-SecretboxConfiguration"><code>SecretboxConfiguration</code></a>
</td>
<td>
   <p>secretbox پیکربندی transformer مبتنی بر Secretbox است.</p>
</td>
</tr>
<tr><td><code>identity</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-IdentityConfiguration"><code>IdentityConfiguration</code></a>
</td>
<td>
   <p>identity پیکربندی (خالی) identity transformer است.</p>
</td>
</tr>
<tr><td><code>kms</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-KMSConfiguration"><code>KMSConfiguration</code></a>
</td>
<td>
   <p>kms شامل نام، اندازه کش و مسیر فایل پیکربندی برای یک envelope transformer مبتنی بر KMS است.</p>
</td>
</tr>
</tbody>
</table>

## `ResourceConfiguration`     {#apiserver-config-k8s-io-v1-ResourceConfiguration}
    

**نمایش داده شده در:**

- [EncryptionConfiguration](#apiserver-config-k8s-io-v1-EncryptionConfiguration)


<p>ResourceConfiguration پیکربندی هر منبع را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>resources</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>resources فهرستی از منابع کوبرنتیز است که باید رمزنگاری شوند. نام منابع از <code>resource</code> یا <code>resource.group</code> مربوط به group/version/resource گرفته می‌شود.
مثال: pandas.awesome.bears.example یک منبع سفارشی با 'group': awesome.bears.example و 'resource': pandas است.
از '<em>.</em>' برای رمزنگاری تمام منابع و از '<em>.<!-- raw HTML omitted -->' برای رمزنگاری تمام منابع در یک گروه مشخص استفاده کنید.
مثال: '</em>.awesome.bears.example' تمام منابع گروه 'awesome.bears.example' را رمزنگاری می‌کند.
مثال: '*.' تمام منابع گروه core (مانند Podها، ConfigMapها و غیره) را رمزنگاری می‌کند.</p>
</td>
</tr>
<tr><td><code>providers</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-ProviderConfiguration"><code>[]ProviderConfiguration</code></a>
</td>
<td>
   <p>providers فهرستی از transformerها است که برای خواندن و نوشتن منابع روی دیسک استفاده می‌شوند.
مثال: aesgcm، aescbc، secretbox، identity، kms.</p>
</td>
</tr>
</tbody>
</table>

## `SecretboxConfiguration`     {#apiserver-config-k8s-io-v1-SecretboxConfiguration}
    

**نمایش داده شده در:**

- [ProviderConfiguration](#apiserver-config-k8s-io-v1-ProviderConfiguration)


<p>SecretboxConfiguration شامل پیکربندی API برای یک Secretbox transformer است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>keys</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-Key"><code>[]Key</code></a>
</td>
<td>
   <p>keys فهرستی از کلیدها است که برای ایجاد Secretbox transformer استفاده می‌شوند.
طول هر کلید باید ۳۲ بایت باشد.</p>
</td>
</tr>
</tbody>
</table>

## `UserValidationRule`     {#apiserver-config-k8s-io-v1-UserValidationRule}
    

**نمایش داده‌شده در:**

- [JWTAuthenticator](#apiserver-config-k8s-io-v1-JWTAuthenticator)


<p>UserValidationRule پیکربندی یک قانون اعتبارسنجی منفرد برای اطلاعات کاربر (user info) را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>expression</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>expression بیانگر عبارتی است که توسط CEL ارزیابی خواهد شد.
برای موفقیت اعتبارسنجی، این عبارت باید مقدار true برگرداند.</p>
<p>عبارت‌های CEL به محتوای UserInfo دسترسی دارند که در قالب یک متغیر CEL سازماندهی شده است:</p>
<ul>
<li>'user' - آبجکت authentication.k8s.io/v1، Kind=UserInfo
برای مشاهده تعریف آن به https://github.com/kubernetes/api/blob/release-1.28/authentication/v1/types.go#L105-L122 مراجعه کنید.
مستندات API: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#userinfo-v1-authentication-k8s-io</li>
</ul>
<p>مستندات مربوط به CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
<tr><td><code>message</code><br/>
<code>string</code>
</td>
<td>
   <p>message پیام خطای بازگردانده‌شده را زمانی که قانون مقدار false برمی‌گرداند، سفارشی می‌کند.
message یک رشته لفظی (literal) است.</p>
</td>
</tr>
</tbody>
</table>

## `WebhookConfiguration`     {#apiserver-config-k8s-io-v1-WebhookConfiguration}
    

**نمایش داده‌شده در:**

- [AuthorizerConfiguration](#apiserver-config-k8s-io-v1-AuthorizerConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>authorizedTTL</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمان ذخیره‌سازی در حافظه نهان (cache) برای پاسخ‌های «authorized» از authorizer مبتنی بر webhook.
معادل تنظیم فلگ <code>--authorization-webhook-cache-authorized-ttl</code> است.
پیش‌فرض: 5m0s</p>
</td>
</tr>
<tr><td><code>cacheAuthorizedRequests</code><br/>
<code>bool</code>
</td>
<td>
   <p>CacheAuthorizedRequests مشخص می‌کند که آیا درخواست‌های مجاز (authorized) باید در حافظه نهان ذخیره شوند یا خیر.
اگر روی true تنظیم شود، TTL تصمیم‌های ذخیره‌شده در حافظه نهان را می‌توان از طریق
فیلد AuthorizedTTL پیکربندی کرد.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>unauthorizedTTL</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمان ذخیره‌سازی در حافظه نهان (cache) برای پاسخ‌های «unauthorized» از authorizer مبتنی بر webhook.
معادل تنظیم فلگ <code>--authorization-webhook-cache-unauthorized-ttl</code> است.
پیش‌فرض: 30s</p>
</td>
</tr>
<tr><td><code>cacheUnauthorizedRequests</code><br/>
<code>bool</code>
</td>
<td>
   <p>CacheUnauthorizedRequests مشخص می‌کند که آیا درخواست‌های غیرمجاز (unauthorized) باید در حافظه نهان ذخیره شوند یا خیر.
اگر روی true تنظیم شود، TTL تصمیم‌های ذخیره‌شده در حافظه نهان را می‌توان از طریق
فیلد UnauthorizedTTL پیکربندی کرد.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>timeout</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مهلت زمانی (timeout) برای درخواست webhook.
حداکثر مقدار مجاز 30s است.
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>subjectAccessReviewVersion</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه API از SubjectAccessReview در authorization.k8s.io که باید به webhook ارسال شود
و از آن انتظار می‌رود.
معادل تنظیم فلگ <code>--authorization-webhook-version</code> است.
مقادیر معتبر: v1beta1، v1
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>matchConditionSubjectAccessReviewVersion</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>MatchConditionSubjectAccessReviewVersion نسخه SubjectAccessReview را مشخص می‌کند
که عبارت‌های CEL بر اساس آن ارزیابی می‌شوند.
مقادیر معتبر: v1
الزامی است و مقدار پیش‌فرض ندارد.</p>
</td>
</tr>
<tr><td><code>failurePolicy</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>تصمیم مجوزدهی را زمانی کنترل می‌کند که درخواست webhook به اتمام نرسد،
پاسخ نادرست (malformed) برگرداند یا ارزیابی matchConditions با خطا مواجه شود.
مقادیر معتبر:</p>
<ul>
<li>NoOpinion: ادامه به authorizerهای بعدی تا بررسی شود که آیا یکی از آن‌ها
درخواست را مجاز می‌کند یا خیر</li>
<li>Deny: رد درخواست بدون مراجعه به authorizerهای بعدی
الزامی است و مقدار پیش‌فرض ندارد.</li>
</ul>
</td>
</tr>
<tr><td><code>connectionInfo</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-WebhookConnectionInfo"><code>WebhookConnectionInfo</code></a>
</td>
<td>
   <p>ConnectionInfo نحوه ارتباط با webhook را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>matchConditions</code> <B>[الزامی]</B><br/>
<a href="#apiserver-config-k8s-io-v1-WebhookMatchCondition"><code>[]WebhookMatchCondition</code></a>
</td>
<td>
   <p>matchConditions فهرستی از شرایطی است که برای ارسال یک درخواست به این
webhook باید برقرار باشند. فهرست خالی matchConditions با همه درخواست‌ها مطابقت دارد.
حداکثر 64 شرط تطبیق مجاز است.</p>
<p>منطق دقیق تطبیق به ترتیب چنین است:</p>
<ol>
<li>اگر دست‌کم یکی از matchConditionها به FALSE ارزیابی شود، webhook نادیده گرفته می‌شود.</li>
<li>اگر همه matchConditionها به TRUE ارزیابی شوند، webhook فراخوانی می‌شود.</li>
<li>اگر دست‌کم یکی از matchConditionها به خطا ارزیابی شود (اما هیچ‌کدام FALSE نباشند):
<ul>
<li>اگر failurePolicy=Deny باشد، webhook درخواست را رد می‌کند</li>
<li>اگر failurePolicy=NoOpinion باشد، خطا نادیده گرفته می‌شود و webhook نادیده گرفته می‌شود</li>
</ul>
</li>
</ol>
</td>
</tr>
</tbody>
</table>

## `WebhookConnectionInfo`     {#apiserver-config-k8s-io-v1-WebhookConnectionInfo}
    

**نمایش داده‌شده در:**

- [WebhookConfiguration](#apiserver-config-k8s-io-v1-WebhookConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نحوه ارتباط webhook با سرور را کنترل می‌کند.
مقادیر معتبر:</p>
<ul>
<li>KubeConfigFile: از فایل مشخص‌شده در kubeConfigFile برای یافتن
سرور استفاده می‌شود.</li>
<li>InClusterConfig: از پیکربندی درون کلاستر (in-cluster) برای فراخوانی
API مربوط به SubjectAccessReview که توسط kube-apiserver ارائه می‌شود، استفاده می‌شود. این حالت برای
kube-apiserver مجاز نیست.</li>
</ul>
</td>
</tr>
<tr><td><code>kubeConfigFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>مسیر KubeConfigFile برای اطلاعات اتصال.
اگر connectionInfo.Type برابر KubeConfig باشد، الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `WebhookMatchCondition`     {#apiserver-config-k8s-io-v1-WebhookMatchCondition}
    

**نمایش داده‌شده در:**

- [WebhookConfiguration](#apiserver-config-k8s-io-v1-WebhookConfiguration)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>expression</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>expression بیانگر عبارتی است که توسط CEL ارزیابی خواهد شد و باید به مقدار bool ارزیابی شود.
عبارت‌های CEL به محتوای SubjectAccessReview در نسخه v1 دسترسی دارند.
اگر نسخه مشخص‌شده توسط subjectAccessReviewVersion در متغیر request برابر v1beta1 باشد،
پیش از ارزیابی عبارت CEL، محتوا به نسخه v1 تبدیل می‌شود.</p>
<ul>
<li>'resourceAttributes' اطلاعات مربوط به یک درخواست دسترسی به منبع را توصیف می‌کند و برای درخواست‌های غیرمنبعی تنظیم نشده است. برای مثال: has(request.resourceAttributes) &amp;&amp; request.resourceAttributes.namespace == 'default'</li>
<li>'nonResourceAttributes' اطلاعات مربوط به یک درخواست دسترسی غیرمنبعی را توصیف می‌کند و برای درخواست‌های منبعی تنظیم نشده است. برای مثال: has(request.nonResourceAttributes) &amp;&amp; request.nonResourceAttributes.path == '/healthz'.</li>
<li>'user' کاربری است که باید برای آن آزمون انجام شود. برای مثال: request.user == 'alice'</li>
<li>'groups' گروه‌هایی هستند که باید برای آن‌ها آزمون انجام شود. برای مثال: ('group1' in request.groups)</li>
<li>'extra' متناظر با متد user.Info.GetExtra() از authenticator است.</li>
<li>'uid' اطلاعات مربوط به کاربر درخواست‌کننده است. برای مثال: request.uid == '1'</li>
</ul>
<p>مستندات مربوط به CEL: https://kubernetes.io/docs/reference/using-api/cel/</p>
</td>
</tr>
</tbody>
</table>
