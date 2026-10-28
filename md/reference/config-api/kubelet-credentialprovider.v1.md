---
title: Kubelet CredentialProvider (v1)
content_type: tool-reference
package: credentialprovider.kubelet.k8s.io/v1
auto_generated: true
---


## انواع منابع (Resource Types) {#resource-types}


- [CredentialProviderRequest](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderRequest)
- [CredentialProviderResponse](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)
  

## `CredentialProviderRequest`     {#credentialprovider-kubelet-k8s-io-v1-CredentialProviderRequest}
    


<p>CredentialProviderRequest شامل ایمیجی است که kubelet برای آن به احراز هویت نیاز دارد.
kubelet این آبجکت درخواست را از طریق stdin به افزونه ارسال می‌کند. به‌طور کلی، افزونه‌ها
باید ترجیحاً با همان apiVersion‌ای پاسخ دهند که برایشان ارسال شده است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>credentialprovider.kubelet.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CredentialProviderRequest</code></td></tr>
    
  
<tr><td><code>image</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>image همان ایمیج کانتینری است که به‌عنوان بخشی از درخواست افزونه‌ی ارائه‌دهنده‌ی
اعتبارنامه (credential provider) در حال pull شدن است. افزونه‌ها می‌توانند به‌صورت اختیاری ایمیج را تجزیه (parse) کنند
تا هر اطلاعاتی را که برای دریافت اعتبارنامه‌ها لازم است استخراج نمایند.</p>
</td>
</tr>
<tr><td><code>serviceAccountToken</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>serviceAccountToken توکن service account است که به Podی متصل شده که ایمیج برای آن
pull می‌شود. این توکن تنها در صورتی به افزونه ارسال می‌شود که فیلد
tokenAttributes.serviceAccountTokenAudience در پیکربندی ارائه‌دهنده‌ی اعتبارنامه‌ی
kubelet تنظیم شده باشد.</p>
</td>
</tr>
<tr><td><code>serviceAccountAnnotations</code> <B>[Required]</B><br/>
<code>map[string]string</code>
</td>
<td>
   <p>serviceAccountAnnotations نگاشتی از حاشیه‌نویسی‌ها (annotations) روی service account است که به
Podی متصل شده که ایمیج برای آن pull می‌شود. فهرست annotationهای service account
که باید به افزونه ارسال شوند، در پیکربندی ارائه‌دهنده‌ی اعتبارنامه‌ی kubelet
تعیین می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `CredentialProviderResponse`     {#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse}
    


<p>CredentialProviderResponse شامل اعتبارنامه‌هایی است که kubelet باید برای ایمیج مشخص‌شده
در درخواست اولیه از آن‌ها استفاده کند. kubelet پاسخ افزونه را از طریق stdout می‌خواند.
این پاسخ باید با همان apiVersion مربوط به CredentialProviderRequest تنظیم شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>credentialprovider.kubelet.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CredentialProviderResponse</code></td></tr>
    
  
<tr><td><code>cacheKeyType</code> <B>[Required]</B><br/>
<a href="#credentialprovider-kubelet-k8s-io-v1-PluginCacheKeyType"><code>PluginCacheKeyType</code></a>
</td>
<td>
   <p>cacheKeyType نوع کلید کش را که باید بر اساس ایمیج ارائه‌شده در درخواست
استفاده شود مشخص می‌کند. سه مقدار معتبر برای نوع کلید کش وجود دارد: Image، Registry و
Global. اگر مقدار نامعتبری مشخص شود، kubelet از پاسخ استفاده نخواهد کرد.</p>
</td>
</tr>
<tr><td><code>cacheDuration</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cacheDuration مدت زمانی را نشان می‌دهد که اعتبارنامه‌های ارائه‌شده باید کش شوند.
kubelet از این فیلد برای تعیین مدت زمان کش درون‌حافظه‌ای اعتبارنامه‌ها
در AuthConfig استفاده می‌کند. اگر null باشد، kubelet از defaultCacheDuration مشخص‌شده در
CredentialProviderConfig استفاده می‌کند. اگر روی 0 تنظیم شود، kubelet مقدار AuthConfig ارائه‌شده را کش نخواهد کرد.</p>
</td>
</tr>
<tr><td><code>auth</code><br/>
<a href="#credentialprovider-kubelet-k8s-io-v1-AuthConfig"><code>map[string]AuthConfig</code></a>
</td>
<td>
   <p>auth نگاشتی است که اطلاعات احراز هویت ارسال‌شده به kubelet را در بر دارد.
هر کلید یک رشته‌ی تطبیق ایمیج (match image) است (توضیحات بیشتر در ادامه). مقدار authConfig متناظر
باید برای همه‌ی ایمیج‌هایی که با این کلید مطابقت دارند معتبر باشد. اگر برای ایمیج درخواست‌شده
نتوان هیچ اعتبارنامه‌ی معتبری برگرداند، افزونه باید این فیلد را روی null تنظیم کند.</p>
<p>هر کلید در این نگاشت الگویی است که می‌تواند به‌صورت اختیاری شامل یک پورت و یک مسیر باشد.
در دامنه می‌توان از glob استفاده کرد، اما در پورت یا مسیر نمی‌توان. globها
به‌صورت زیردامنه مانند '<em>.k8s.io' یا 'k8s.</em>.io' و دامنه‌های سطح بالا مانند 'k8s.<em>' پشتیبانی می‌شوند.
تطبیق زیردامنه‌های جزئی مانند 'app</em>.k8s.io' نیز پشتیبانی می‌شود. هر glob فقط می‌تواند با
یک بخش زیردامنه مطابقت داشته باشد، بنابراین *.io با *.k8s.io مطابقت ندارد.</p>
<p>kubelet زمانی ایمیج‌ها را با کلید مطابقت می‌دهد که همه‌ی شرایط زیر برقرار باشند:</p>
<ul>
<li>هر دو تعداد بخش‌های دامنه‌ی یکسانی داشته باشند و هر بخش مطابقت کند.</li>
<li>مسیر URL مربوط به imageMatch باید پیشوندی از مسیر URL ایمیج هدف باشد.</li>
<li>اگر imageMatch شامل پورت باشد، پورت باید در ایمیج نیز مطابقت داشته باشد.</li>
</ul>
<p>وقتی چندین کلید برگردانده شوند، kubelet همه‌ی کلیدها را به ترتیب معکوس پیمایش می‌کند، به‌طوری که:</p>
<ul>
<li>کلیدهای بلندتر پیش از کلیدهای کوتاه‌تر با همان پیشوند قرار می‌گیرند</li>
<li>کلیدهای بدون wildcard پیش از کلیدهای دارای wildcard با همان پیشوند قرار می‌گیرند.</li>
</ul>
<p>برای هر تطبیق مشخص، kubelet تلاش می‌کند ایمیج را با اعتبارنامه‌های ارائه‌شده pull کند
و پس از نخستین pull که با موفقیت احراز هویت شود، متوقف می‌شود.</p>
<p>نمونه‌ی کلیدها:</p>
<ul>
<li>123456789.dkr.ecr.us-east-1.amazonaws.com</li>
<li>*.azurecr.io</li>
<li>gcr.io</li>
<li><em>.</em>.registry.io</li>
<li>registry.io:8080/path</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `AuthConfig`     {#credentialprovider-kubelet-k8s-io-v1-AuthConfig}
    

**نمایش داده شده در:**

- [CredentialProviderResponse](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)


<p>AuthConfig شامل اطلاعات احراز هویت برای یک رجیستری کانتینر است.
در حال حاضر تنها احراز هویت مبتنی بر نام کاربری/گذرواژه پشتیبانی می‌شود، اما ممکن است
سازوکارهای احراز هویت بیشتری در آینده اضافه شوند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>username</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>username نام کاربری است که برای احراز هویت در رجیستری کانتینر استفاده می‌شود.
نام کاربری خالی نیز معتبر است.</p>
</td>
</tr>
<tr><td><code>password</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>password گذرواژه‌ای است که برای احراز هویت در رجیستری کانتینر استفاده می‌شود.
گذرواژه‌ی خالی نیز معتبر است.</p>
</td>
</tr>
</tbody>
</table>

## `PluginCacheKeyType`     {#credentialprovider-kubelet-k8s-io-v1-PluginCacheKeyType}
    
(نام مستعار برای `string`)

**نمایش داده شده در:**

- [CredentialProviderResponse](#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)
