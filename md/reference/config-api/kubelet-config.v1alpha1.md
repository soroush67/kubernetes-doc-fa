---
title: پیکربندی Kubelet (v1alpha1)
content_type: tool-reference
package: kubelet.config.k8s.io/v1alpha1
auto_generated: true
---


## انواع منابع {#resource-types}


- [CredentialProviderConfig](#kubelet-config-k8s-io-v1alpha1-CredentialProviderConfig)
- [ImagePullIntent](#kubelet-config-k8s-io-v1alpha1-ImagePullIntent)
- [ImagePulledRecord](#kubelet-config-k8s-io-v1alpha1-ImagePulledRecord)
  

## `CredentialProviderConfig`     {#kubelet-config-k8s-io-v1alpha1-CredentialProviderConfig}
    


<p>CredentialProviderConfig پیکربندی‌ای است که اطلاعات مربوط به هر یک از
ارائه‌دهندگان اعتبارنامه مبتنی بر exec را در بر دارد. Kubelet این پیکربندی را از دیسک می‌خواند و
هر ارائه‌دهنده را مطابق با آنچه توسط نوع CredentialProvider مشخص شده است فعال می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CredentialProviderConfig</code></td></tr>
    
  
<tr><td><code>providers</code> <B>[الزامی]</B><br/>
<a href="#kubelet-config-k8s-io-v1alpha1-CredentialProvider"><code>[]CredentialProvider</code></a>
</td>
<td>
   <p>providers فهرستی از افزونه‌های ارائه‌دهنده اعتبارنامه است که توسط kubelet فعال خواهند شد.
چند ارائه‌دهنده ممکن است با یک ایمیج واحد مطابقت پیدا کنند؛ در این صورت اعتبارنامه‌های
همه ارائه‌دهندگان به kubelet بازگردانده می‌شود. اگر برای یک ایمیج واحد چند ارائه‌دهنده فراخوانی شوند،
نتایج با یکدیگر ترکیب می‌شوند. اگر ارائه‌دهندگان کلیدهای احراز هویت هم‌پوشان بازگردانند،
مقدار ارائه‌دهنده‌ای که در این فهرست زودتر آمده است ابتدا امتحان می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `ImagePullIntent`     {#kubelet-config-k8s-io-v1alpha1-ImagePullIntent}
    


<p>ImagePullIntent رکوردی از تلاش kubelet برای pull کردن یک ایمیج است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ImagePullIntent</code></td></tr>
    
  
<tr><td><code>image</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Image مشخصات ایمیج است که از فیلد <code>image</code> یک کانتینر گرفته می‌شود.
نام فایل، هش SHA-256 این مقدار است. این کار برای پرهیز از کاراکترهایی است که
در نام فایل ناامن‌اند، مانند ':' و '/'.</p>
</td>
</tr>
</tbody>
</table>

## `ImagePulledRecord`     {#kubelet-config-k8s-io-v1alpha1-ImagePulledRecord}
    


<p>ImagePullRecord رکوردی از یک ایمیج است که توسط kubelet pull شده است.</p>
<p>اگر هیچ رکوردی در فیلد <code>kubernetesSecrets</code> وجود نداشته باشد و هر دو فیلد <code>nodeWideCredentials</code>
و <code>anonymous</code> برابر <code>false</code> باشند، اعتبارنامه‌ها باید در دفعه بعدی که
ایمیجِ نمایان‌شده توسط این رکورد درخواست می‌شود، دوباره بررسی شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ImagePulledRecord</code></td></tr>
    
  
<tr><td><code>lastUpdatedTime</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>LastUpdatedTime زمان آخرین به‌روزرسانی این رکورد است.</p>
</td>
</tr>
<tr><td><code>imageRef</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>ImageRef ارجاعی به ایمیجی است که این فایل نمایانگر آن است و
از CRI دریافت شده است.
نام فایل، هش SHA-256 این مقدار است. این کار برای پرهیز از کاراکترهایی است که
در نام فایل ناامن‌اند، مانند ':' و '/'.</p>
</td>
</tr>
<tr><td><code>credentialMapping</code> <B>[الزامی]</B><br/>
<a href="#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials"><code>map[string]ImagePullCredentials</code></a>
</td>
<td>
   <p>CredentialMapping مقدار <code>image</code> را به مجموعه اعتبارنامه‌هایی نگاشت می‌کند که
پیش‌تر با آن‌ها pull شده است.
<code>image</code> در این‌جا محتوای فیلد <code>image</code> کانتینر یک Pod است که
تگ/digest آن حذف شده است.</p>
<p>مثال:
کانتینر ایمیج <code>hello-world:latest@sha256:91fb4b041da273d5a3273b6d587d62d518300a6ad268b28628f74997b93171b2</code> را درخواست می‌کند:
&quot;credentialMapping&quot;: {
&quot;hello-world&quot;: { &quot;nodePodsAccessible&quot;: true }
}</p>
</td>
</tr>
</tbody>
</table>

## `CredentialProvider`     {#kubelet-config-k8s-io-v1alpha1-CredentialProvider}
    

**نمایش داده شده در:**

- [CredentialProviderConfig](#kubelet-config-k8s-io-v1alpha1-CredentialProviderConfig)


<p>CredentialProvider نمایانگر یک افزونه exec است که kubelet آن را فراخوانی می‌کند. افزونه فقط
زمانی فراخوانی می‌شود که ایمیجِ در حال pull با ایمیج‌هایی که افزونه مدیریت می‌کند مطابقت داشته باشد (به matchImages مراجعه کنید).</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام الزامی ارائه‌دهنده اعتبارنامه است. این نام باید با نام فایل اجرایی
ارائه‌دهنده، آن‌گونه که kubelet می‌بیند، مطابقت داشته باشد. فایل اجرایی باید در دایرکتوری bin
مربوط به kubelet باشد (که با فلگ --image-credential-provider-bin-dir تنظیم می‌شود).
این نام باید میان همه ارائه‌دهندگان یکتا باشد.</p>
</td>
</tr>
<tr><td><code>matchImages</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>matchImages فهرستی الزامی از رشته‌هاست که برای تطبیق با ایمیج‌ها به کار می‌رود تا
مشخص شود آیا این ارائه‌دهنده باید فراخوانی شود یا نه. اگر یکی از رشته‌ها با
ایمیج درخواست‌شده از سوی kubelet مطابقت داشته باشد، افزونه فراخوانی می‌شود و فرصت می‌یابد
اعتبارنامه ارائه دهد. انتظار می‌رود ایمیج‌ها شامل دامنه رجیستری
و مسیر URL باشند.</p>
<p>هر مورد در matchImages یک الگو است که می‌تواند به‌طور اختیاری شامل پورت و مسیر باشد.
Globها را می‌توان در دامنه به کار برد، اما در پورت یا مسیر نمی‌توان. Globها
به‌صورت زیردامنه‌هایی مانند <code>*.k8s.io</code> یا <code>k8s.*.io</code> و دامنه‌های سطح بالا مانند <code>k8s.*</code> پشتیبانی می‌شوند.
تطبیق زیردامنه‌های جزئی مانند <code>app*.k8s.io</code> نیز پشتیبانی می‌شود. هر glob فقط می‌تواند با
یک بخش زیردامنه مطابقت پیدا کند، بنابراین <code>*.io</code> با <code>*.k8s.io</code> مطابقت ندارد.</p>
<p>میان یک ایمیج و یک matchImage زمانی تطبیق وجود دارد که همه شرایط زیر برقرار باشند:</p>
<ul>
<li>هر دو تعداد بخش‌های دامنه یکسانی داشته باشند و هر بخش مطابقت داشته باشد.</li>
<li>مسیر URL مربوط به imageMatch باید پیشوندی از مسیر URL ایمیج هدف باشد.</li>
<li>اگر imageMatch شامل پورت باشد، پورت باید در ایمیج نیز مطابقت داشته باشد.</li>
</ul>
<p>نمونه مقادیر matchImages:</p>
<ul>
<li><code>123456789.dkr.ecr.us-east-1.amazonaws.com</code></li>
<li><code>*.azurecr.io</code></li>
<li><code>gcr.io</code></li>
<li><code>*.*.registry.io</code></li>
<li><code>registry.io:8080/path</code></li>
</ul>
</td>
</tr>
<tr><td><code>defaultCacheDuration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>defaultCacheDuration مدت زمان پیش‌فرضی است که افزونه اعتبارنامه‌ها را در حافظه نگهداری (cache) می‌کند،
در صورتی که مدت نگهداری در پاسخ افزونه ارائه نشده باشد. این فیلد الزامی است.</p>
</td>
</tr>
<tr><td><code>apiVersion</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه ورودی الزامی برای CredentialProviderRequest مربوط به exec. CredentialProviderResponse بازگردانده‌شده
باید حتماً از همان نسخه کدگذاری ورودی استفاده کند. مقادیر پشتیبانی‌شده فعلی عبارت‌اند از:</p>
<ul>
<li>credentialprovider.kubelet.k8s.io/v1alpha1</li>
</ul>
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
<a href="#kubelet-config-k8s-io-v1alpha1-ExecEnvVar"><code>[]ExecEnvVar</code></a>
</td>
<td>
   <p>Env متغیرهای محیطی اضافی را که باید در اختیار پروسه قرار گیرند تعریف می‌کند. این‌ها
با محیط میزبان و همچنین متغیرهایی که client-go برای
ارسال آرگومان به افزونه استفاده می‌کند، اجتماع می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `ExecEnvVar`     {#kubelet-config-k8s-io-v1alpha1-ExecEnvVar}
    

**نمایش داده شده در:**

- [CredentialProvider](#kubelet-config-k8s-io-v1alpha1-CredentialProvider)


<p>ExecEnvVar برای تنظیم متغیرهای محیطی هنگام اجرای افزونه اعتبارنامه
مبتنی بر exec استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>value</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `ImagePullCredentials`     {#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials}
    

**نمایش داده شده در:**

- [ImagePulledRecord](#kubelet-config-k8s-io-v1alpha1-ImagePulledRecord)


<p>ImagePullCredentials اعتبارنامه‌هایی را توصیف می‌کند که می‌توان برای pull کردن یک ایمیج از آن‌ها استفاده کرد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesSecrets</code><br/>
<a href="#kubelet-config-k8s-io-v1alpha1-ImagePullSecret"><code>[]ImagePullSecret</code></a>
</td>
<td>
   <p>KuberneteSecretCoordinates فهرستی از مختصات همه Secretهای کوبرنتیز است
که برای pull کردن ایمیج استفاده شده‌اند.</p>
</td>
</tr>
<tr><td><code>kubernetesServiceAccounts</code><br/>
<a href="#kubelet-config-k8s-io-v1alpha1-ImagePullServiceAccount"><code>[]ImagePullServiceAccount</code></a>
</td>
<td>
   <p>KubernetesServiceAccounts فهرستی از مختصات همه service accountهای کوبرنتیز است
که برای pull کردن ایمیج استفاده شده‌اند.</p>
</td>
</tr>
<tr><td><code>nodePodsAccessible</code><br/>
<code>bool</code>
</td>
<td>
   <p>NodePodsAccessible پرچمی است که نشان می‌دهد اعتبارنامه‌های pull برای
همه Podهای روی نود قابل دسترسی‌اند، یا اینکه برای pull به هیچ اعتبارنامه‌ای نیاز نیست.</p>
<p>اگر true باشد، با فیلد <code>kubernetesSecrets</code> متقابلاً ناسازگار است (نمی‌توانند هم‌زمان تنظیم شوند).</p>
</td>
</tr>
</tbody>
</table>

## `ImagePullSecret`     {#kubelet-config-k8s-io-v1alpha1-ImagePullSecret}
    

**نمایش داده شده در:**

- [ImagePullCredentials](#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials)


<p>ImagePullSecret نمایشی از مختصات یک آبجکت Secret کوبرنتیز است، به‌همراه
هش اعتبارنامه‌ای از اعتبارنامه‌های pull secret که این آبجکت در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>uid</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>credentialHash</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>CredentialHash مقدار SHA-256 است که از هش کردن محتوای اعتبارنامه‌های pull ایمیج
در Secretِ مشخص‌شده با مختصات UID/Namespace/Name به دست می‌آید.</p>
</td>
</tr>
</tbody>
</table>

## `ImagePullServiceAccount`     {#kubelet-config-k8s-io-v1alpha1-ImagePullServiceAccount}
    

**نمایش داده شده در:**

- [ImagePullCredentials](#kubelet-config-k8s-io-v1alpha1-ImagePullCredentials)


<p>ImagePullServiceAccount نمایشی از مختصات یک آبجکت service account کوبرنتیز است
که kubelet برای آن، توکن service account را برای دریافت اعتبارنامه‌های pull ایمیج به افزونه ارائه‌دهنده اعتبارنامه ارسال کرده است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>uid</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>
