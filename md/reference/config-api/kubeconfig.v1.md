---
title: kubeconfig (v1)
content_type: tool-reference
package: v1
auto_generated: true
---


## انواع منابع {#resource-types}


- [Config](#Config)
  
    
    

## `Config`     {#Config}
    


<p>Config اطلاعات لازم برای ساخت اتصال به کلاسترهای کوبرنتیز راه دور را به عنوان یک کاربر مشخص نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>Config</code></td></tr>
    
  
<tr><td><code>kind</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد قدیمی از TypeMeta در pkg/api/types.go.
TODO(jlowdermilk): این فیلد پس از حذف وابستگی‌های پایین‌دستی حذف شود.</p>
</td>
</tr>
<tr><td><code>apiVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد قدیمی از TypeMeta در pkg/api/types.go.
TODO(jlowdermilk): این فیلد پس از حذف وابستگی‌های پایین‌دستی حذف شود.</p>
</td>
</tr>
<tr><td><code>preferences,omitzero</code> <B>[Required]</B><br/>
<a href="#Preferences"><code>Preferences</code></a>
</td>
<td>
   <p>Preferences اطلاعات عمومی را برای استفاده در تعاملات خط فرمان (cli) نگه می‌دارد.
منسوخ‌شده: این فیلد از نسخه v1.34 منسوخ شده است و هیچ‌یک از مؤلفه‌های کوبرنتیز از آن استفاده نمی‌کنند.</p>
</td>
</tr>
<tr><td><code>clusters</code> <B>[Required]</B><br/>
<a href="#NamedCluster"><code>[]NamedCluster</code></a>
</td>
<td>
   <p>Clusters نگاشتی از نام‌های قابل ارجاع به پیکربندی‌های کلاستر است.</p>
</td>
</tr>
<tr><td><code>users</code> <B>[Required]</B><br/>
<a href="#NamedAuthInfo"><code>[]NamedAuthInfo</code></a>
</td>
<td>
   <p>AuthInfos نگاشتی از نام‌های قابل ارجاع به پیکربندی‌های کاربر است.</p>
</td>
</tr>
<tr><td><code>contexts</code> <B>[Required]</B><br/>
<a href="#NamedContext"><code>[]NamedContext</code></a>
</td>
<td>
   <p>Contexts نگاشتی از نام‌های قابل ارجاع به پیکربندی‌های context است.</p>
</td>
</tr>
<tr><td><code>current-context</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>CurrentContext نام contextی است که می‌خواهید به‌طور پیش‌فرض از آن استفاده کنید.</p>
</td>
</tr>
<tr><td><code>extensions</code><br/>
<a href="#NamedExtension"><code>[]NamedExtension</code></a>
</td>
<td>
   <p>Extensions اطلاعات اضافی را نگه می‌دارد. این فیلد برای توسعه‌دهندگان افزونه مفید است تا عملیات خواندن و نوشتن فیلدهای ناشناخته را بازنویسی نکند.</p>
</td>
</tr>
</tbody>
</table>

## `AuthInfo`     {#AuthInfo}
    

**Appears in:**

- [NamedAuthInfo](#NamedAuthInfo)


<p>AuthInfo شامل اطلاعاتی است که هویت را توصیف می‌کند. از این آبجکت برای اعلام هویت شما به کلاستر کوبرنتیز استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>client-certificate</code><br/>
<code>string</code>
</td>
<td>
   <p>ClientCertificate مسیر فایل گواهی کلاینت برای TLS است.</p>
</td>
</tr>
<tr><td><code>client-certificate-data</code><br/>
<code>[]byte</code>
</td>
<td>
   <p>ClientCertificateData شامل داده‌های رمزگذاری‌شده با PEM از یک فایل گواهی کلاینت برای TLS است. این مقدار بر ClientCertificate اولویت دارد.</p>
</td>
</tr>
<tr><td><code>client-key</code><br/>
<code>string</code>
</td>
<td>
   <p>ClientKey مسیر فایل کلید کلاینت برای TLS است.</p>
</td>
</tr>
<tr><td><code>client-key-data</code><br/>
<code>[]byte</code>
</td>
<td>
   <p>ClientKeyData شامل داده‌های رمزگذاری‌شده با PEM از یک فایل کلید کلاینت برای TLS است. این مقدار بر ClientKey اولویت دارد.</p>
</td>
</tr>
<tr><td><code>token</code><br/>
<code>string</code>
</td>
<td>
   <p>Token توکن حامل (bearer token) برای احراز هویت در کلاستر کوبرنتیز است.</p>
</td>
</tr>
<tr><td><code>tokenFile</code><br/>
<code>string</code>
</td>
<td>
   <p>TokenFile اشاره‌گری به فایلی است که شامل یک توکن حامل (مطابق توضیح بالا) است. اگر هم Token و هم TokenFile موجود باشند،
TokenFile به‌طور دوره‌ای خوانده می‌شود و آخرین مقداری که با موفقیت خوانده شده باشد بر Token اولویت دارد.</p>
</td>
</tr>
<tr><td><code>as</code><br/>
<code>string</code>
</td>
<td>
   <p>Impersonate نام کاربری است که باید جعل هویت (impersonate) شود. این نام با نام پرچم (flag) مطابقت دارد.</p>
</td>
</tr>
<tr><td><code>as-uid</code><br/>
<code>string</code>
</td>
<td>
   <p>ImpersonateUID شناسه یکتای (uid) کاربری است که باید جعل هویت شود.</p>
</td>
</tr>
<tr><td><code>as-groups</code><br/>
<code>[]string</code>
</td>
<td>
   <p>ImpersonateGroups گروه‌هایی است که باید جعل هویت شوند.</p>
</td>
</tr>
<tr><td><code>as-user-extra</code><br/>
<code>map[string][]string</code>
</td>
<td>
   <p>ImpersonateUserExtra شامل اطلاعات اضافی برای کاربر جعل‌هویت‌شده است.</p>
</td>
</tr>
<tr><td><code>username</code><br/>
<code>string</code>
</td>
<td>
   <p>Username نام کاربری برای احراز هویت پایه (basic authentication) در کلاستر کوبرنتیز است.</p>
</td>
</tr>
<tr><td><code>password</code><br/>
<code>string</code>
</td>
<td>
   <p>Password گذرواژه برای احراز هویت پایه (basic authentication) در کلاستر کوبرنتیز است.</p>
</td>
</tr>
<tr><td><code>auth-provider</code><br/>
<a href="#AuthProviderConfig"><code>AuthProviderConfig</code></a>
</td>
<td>
   <p>AuthProvider یک افزونه احراز هویت سفارشی را برای کلاستر کوبرنتیز مشخص می‌کند.</p>
</td>
</tr>
<tr><td><code>exec</code><br/>
<a href="#ExecConfig"><code>ExecConfig</code></a>
</td>
<td>
   <p>Exec یک افزونه احراز هویت سفارشی مبتنی بر exec را برای کلاستر کوبرنتیز مشخص می‌کند.</p>
</td>
</tr>
<tr><td><code>extensions</code><br/>
<a href="#NamedExtension"><code>[]NamedExtension</code></a>
</td>
<td>
   <p>Extensions اطلاعات اضافی را نگه می‌دارد. این فیلد برای توسعه‌دهندگان افزونه مفید است تا عملیات خواندن و نوشتن فیلدهای ناشناخته را بازنویسی نکند.</p>
</td>
</tr>
</tbody>
</table>

## `AuthProviderConfig`     {#AuthProviderConfig}
    

**Appears in:**

- [AuthInfo](#AuthInfo)


<p>AuthProviderConfig پیکربندی یک ارائه‌دهنده احراز هویت مشخص را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>config</code> <B>[Required]</B><br/>
<code>map[string]string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `Cluster`     {#Cluster}
    

**Appears in:**

- [NamedCluster](#NamedCluster)


<p>Cluster شامل اطلاعاتی درباره نحوه ارتباط با یک کلاستر کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>server</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Server آدرس کلاستر کوبرنتیز است (https://hostname:port).</p>
</td>
</tr>
<tr><td><code>tls-server-name</code><br/>
<code>string</code>
</td>
<td>
   <p>TLSServerName برای بررسی گواهی سرور استفاده می‌شود. اگر TLSServerName خالی باشد، از نام میزبانی که برای ارتباط با سرور استفاده شده است، استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>insecure-skip-tls-verify</code><br/>
<code>bool</code>
</td>
<td>
   <p>InsecureSkipTLSVerify بررسی اعتبار گواهی سرور را نادیده می‌گیرد. این کار اتصال‌های HTTPS شما را ناامن می‌کند.</p>
</td>
</tr>
<tr><td><code>certificate-authority</code><br/>
<code>string</code>
</td>
<td>
   <p>CertificateAuthority مسیر فایل گواهی مربوط به مرجع صدور گواهی (certificate authority) است.</p>
</td>
</tr>
<tr><td><code>certificate-authority-data</code><br/>
<code>[]byte</code>
</td>
<td>
   <p>CertificateAuthorityData شامل گواهی‌های مرجع صدور گواهی با رمزگذاری PEM است. این مقدار بر CertificateAuthority اولویت دارد.</p>
</td>
</tr>
<tr><td><code>proxy-url</code><br/>
<code>string</code>
</td>
<td>
   <p>ProxyURL نشانی URL پروکسی‌ای است که برای تمام درخواست‌های ارسال‌شده توسط این
کلاینت استفاده می‌شود. نشانی‌های URL با طرح‌های &quot;http&quot;، &quot;https&quot; و &quot;socks5&quot; پشتیبانی می‌شوند. اگر
این پیکربندی ارائه نشود یا رشته خالی باشد، کلاینت
تلاش می‌کند پیکربندی پروکسی را از متغیرهای محیطی http_proxy و
https_proxy بسازد. اگر این متغیرهای محیطی
تنظیم نشده باشند، کلاینت برای درخواست‌ها از پروکسی استفاده نمی‌کند.</p>
<p>پروکسی socks5 در حال حاضر از نقاط پایانی استریمینگ spdy (exec،
attach، port forward) پشتیبانی نمی‌کند.</p>
</td>
</tr>
<tr><td><code>disable-compression</code><br/>
<code>bool</code>
</td>
<td>
   <p>DisableCompression به کلاینت اجازه می‌دهد از فشرده‌سازی پاسخ برای تمام درخواست‌ها به سرور صرف‌نظر کند. این گزینه
زمانی که پهنای باند شبکه میان کلاینت و سرور فراوان است، با صرفه‌جویی در زمان
فشرده‌سازی (سمت سرور) و بازگشایی فشرده‌سازی (سمت کلاینت) برای تسریع درخواست‌ها (به‌ویژه درخواست‌های list) مفید است: https://github.com/kubernetes/kubernetes/issues/112296.</p>
</td>
</tr>
<tr><td><code>extensions</code><br/>
<a href="#NamedExtension"><code>[]NamedExtension</code></a>
</td>
<td>
   <p>Extensions اطلاعات اضافی را نگه می‌دارد. این فیلد برای توسعه‌دهندگان افزونه مفید است تا عملیات خواندن و نوشتن فیلدهای ناشناخته را بازنویسی نکند.</p>
</td>
</tr>
</tbody>
</table>

## `Context`     {#Context}
    

**Appears in:**

- [NamedContext](#NamedContext)


<p>Context یک چندتایی از ارجاع‌ها به یک کلاستر (چگونه با یک کلاستر کوبرنتیز ارتباط برقرار کنم)، یک کاربر (چگونه هویت خود را اعلام کنم) و یک فضای نام (namespace) (با چه زیرمجموعه‌ای از منابع می‌خواهم کار کنم) است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>cluster</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Cluster نام کلاستر برای این context است.</p>
</td>
</tr>
<tr><td><code>user</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>AuthInfo نام authInfo برای این context است.</p>
</td>
</tr>
<tr><td><code>namespace</code><br/>
<code>string</code>
</td>
<td>
   <p>Namespace فضای نام پیش‌فرضی است که برای درخواست‌های بدون مشخصات استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>extensions</code><br/>
<a href="#NamedExtension"><code>[]NamedExtension</code></a>
</td>
<td>
   <p>Extensions اطلاعات اضافی را نگه می‌دارد. این فیلد برای توسعه‌دهندگان افزونه مفید است تا عملیات خواندن و نوشتن فیلدهای ناشناخته را بازنویسی نکند.</p>
</td>
</tr>
</tbody>
</table>

## `ExecConfig`     {#ExecConfig}
    

**Appears in:**

- [AuthInfo](#AuthInfo)


<p>ExecConfig دستوری را برای ارائه اعتبارنامه‌های کلاینت مشخص می‌کند. این دستور اجرا می‌شود
و خروجی ساختاریافته‌ای شامل اعتبارنامه‌ها را در stdout تولید می‌کند.</p>
<p>برای مشخصات دقیق قالب ورودی و خروجی، به گروه API با نام client.authentication.k8s.io مراجعه کنید.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>command</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>دستوری که باید اجرا شود.</p>
</td>
</tr>
<tr><td><code>args</code><br/>
<code>[]string</code>
</td>
<td>
   <p>آرگومان‌هایی که هنگام اجرای دستور به آن ارسال می‌شوند.</p>
</td>
</tr>
<tr><td><code>env</code><br/>
<a href="#ExecEnvVar"><code>[]ExecEnvVar</code></a>
</td>
<td>
   <p>Env متغیرهای محیطی اضافی را که باید در اختیار فرایند قرار گیرند تعریف می‌کند. این‌ها
با محیط میزبان و همچنین متغیرهایی که client-go برای
ارسال آرگومان به افزونه استفاده می‌کند، ترکیب (union) می‌شوند.</p>
</td>
</tr>
<tr><td><code>apiVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه ورودی ترجیحی ExecInfo. ExecCredentials بازگردانده‌شده باید از
همان نسخه رمزگذاری ورودی استفاده کند.</p>
</td>
</tr>
<tr><td><code>installHint</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>این متن زمانی به کاربر نمایش داده می‌شود که فایل اجرایی به نظر
موجود نباشد. برای مثال، <code>brew install foo-cli</code> می‌تواند InstallHint مناسبی برای
foo-cli در سیستم‌های Mac OS باشد.</p>
</td>
</tr>
<tr><td><code>provideClusterInfo</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>ProvideClusterInfo تعیین می‌کند که آیا اطلاعات کلاستر، که ممکن است شامل داده‌های بسیار بزرگ CA باشد، به‌عنوان
بخشی از متغیر محیطی KUBERNETES_EXEC_INFO به این افزونه exec ارائه شود یا خیر. به‌طور پیش‌فرض
روی false تنظیم شده است. بسته k8s.io/client-go/tools/auth/exec متدهای کمکی برای
خواندن این متغیر محیطی فراهم می‌کند.</p>
</td>
</tr>
<tr><td><code>interactiveMode</code><br/>
<a href="#ExecInteractiveMode"><code>ExecInteractiveMode</code></a>
</td>
<td>
   <p>InteractiveMode رابطه این افزونه با ورودی استاندارد را تعیین می‌کند. مقادیر معتبر
عبارت‌اند از &quot;Never&quot; (این افزونه exec هرگز از ورودی استاندارد استفاده نمی‌کند)، &quot;IfAvailable&quot; (این
افزونه exec در صورت در دسترس بودن ورودی استاندارد می‌خواهد از آن استفاده کند) یا &quot;Always&quot; (این افزونه
exec برای کارکرد به ورودی استاندارد نیاز دارد). برای جزئیات بیشتر، مقادیر ExecInteractiveMode را ببینید.</p>
<p>اگر APIVersion برابر client.authentication.k8s.io/v1alpha1 یا
client.authentication.k8s.io/v1beta1 باشد، این فیلد اختیاری است و در صورت تنظیم‌نشدن،
مقدار پیش‌فرض آن &quot;IfAvailable&quot; است. در غیر این صورت، این فیلد الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `ExecEnvVar`     {#ExecEnvVar}
    

**Appears in:**

- [ExecConfig](#ExecConfig)


<p>ExecEnvVar برای تنظیم متغیرهای محیطی هنگام اجرای یک افزونه اعتبارنامه
مبتنی بر exec استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>value</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `ExecInteractiveMode`     {#ExecInteractiveMode}
    
(Alias of `string`)

**Appears in:**

- [ExecConfig](#ExecConfig)


<p>ExecInteractiveMode رشته‌ای است که رابطه یک افزونه exec با ورودی استاندارد را توصیف می‌کند.</p>




## `NamedAuthInfo`     {#NamedAuthInfo}
    

**Appears in:**

- [Config](#Config)


<p>NamedAuthInfo نام‌های مستعار را به اطلاعات احراز هویت مرتبط می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام مستعار این AuthInfo است.</p>
</td>
</tr>
<tr><td><code>user</code> <B>[Required]</B><br/>
<a href="#AuthInfo"><code>AuthInfo</code></a>
</td>
<td>
   <p>AuthInfo اطلاعات احراز هویت را نگه می‌دارد.</p>
</td>
</tr>
</tbody>
</table>

## `NamedCluster`     {#NamedCluster}
    

**Appears in:**

- [Config](#Config)


<p>NamedCluster نام‌های مستعار را به اطلاعات کلاستر مرتبط می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام مستعار این Cluster است.</p>
</td>
</tr>
<tr><td><code>cluster</code> <B>[Required]</B><br/>
<a href="#Cluster"><code>Cluster</code></a>
</td>
<td>
   <p>Cluster اطلاعات کلاستر را نگه می‌دارد.</p>
</td>
</tr>
</tbody>
</table>

## `NamedContext`     {#NamedContext}
    

**Appears in:**

- [Config](#Config)


<p>NamedContext نام‌های مستعار را به اطلاعات context مرتبط می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام مستعار این Context است.</p>
</td>
</tr>
<tr><td><code>context</code> <B>[Required]</B><br/>
<a href="#Context"><code>Context</code></a>
</td>
<td>
   <p>Context اطلاعات context را نگه می‌دارد.</p>
</td>
</tr>
</tbody>
</table>

## `NamedExtension`     {#NamedExtension}
    

**Appears in:**

- [Config](#Config)

- [AuthInfo](#AuthInfo)

- [Cluster](#Cluster)

- [Context](#Context)

- [Preferences](#Preferences)


<p>NamedExtension نام‌های مستعار را به اطلاعات افزونه (extension) مرتبط می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام مستعار این Extension است.</p>
</td>
</tr>
<tr><td><code>extension</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension"><code>k8s.io/apimachinery/pkg/runtime.RawExtension</code></a>
</td>
<td>
   <p>Extension اطلاعات افزونه را نگه می‌دارد.</p>
</td>
</tr>
</tbody>
</table>

## `Preferences`     {#Preferences}
    

**Appears in:**

- [Config](#Config)


<p>منسوخ‌شده: این ساختار از نسخه v1.34 منسوخ شده است و هیچ‌یک از مؤلفه‌های کوبرنتیز از آن استفاده نمی‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>colors</code><br/>
<code>bool</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>extensions</code><br/>
<a href="#NamedExtension"><code>[]NamedExtension</code></a>
</td>
<td>
   <p>Extensions اطلاعات اضافی را نگه می‌دارد. این فیلد برای توسعه‌دهندگان افزونه مفید است تا عملیات خواندن و نوشتن فیلدهای ناشناخته را بازنویسی نکند.</p>
</td>
</tr>
</tbody>
</table>
