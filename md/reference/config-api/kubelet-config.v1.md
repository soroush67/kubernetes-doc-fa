---
title: پیکربندی Kubelet (v1)
content_type: tool-reference
package: kubelet.config.k8s.io/v1
auto_generated: true
---


## انواع منابع {#resource-types}


- [CredentialProviderConfig](#kubelet-config-k8s-io-v1-CredentialProviderConfig)
  

## `CredentialProviderConfig`     {#kubelet-config-k8s-io-v1-CredentialProviderConfig}
    


<p>CredentialProviderConfig پیکربندیِ حاوی اطلاعات مربوط به هر یک از
exec credential providerها است. kubelet این پیکربندی را از دیسک می‌خواند و
هر provider را مطابق آنچه در نوع CredentialProvider مشخص شده است فعال می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CredentialProviderConfig</code></td></tr>
    
  
<tr><td><code>providers</code> <B>[الزامی]</B><br/>
<a href="#kubelet-config-k8s-io-v1-CredentialProvider"><code>[]CredentialProvider</code></a>
</td>
<td>
   <p>providers فهرستی از افزونه‌های credential provider است که kubelet آن‌ها را فعال می‌کند.
چند provider ممکن است با یک ایمیج واحد مطابقت داشته باشند؛ در این صورت اعتبارنامه‌های
همه‌ی providerها به kubelet بازگردانده می‌شود. اگر برای یک ایمیج واحد چند provider فراخوانی شوند،
نتایج با هم ترکیب می‌شوند. اگر providerها کلیدهای احراز هویت هم‌پوشان بازگردانند،
ابتدا مقدارِ provider‌ای که در این فهرست زودتر آمده است امتحان می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `CredentialProvider`     {#kubelet-config-k8s-io-v1-CredentialProvider}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CredentialProviderConfig](#kubelet-config-k8s-io-v1-CredentialProviderConfig)


<p>CredentialProvider نمایانگر یک افزونه‌ی exec است که kubelet آن را فراخوانی می‌کند. این افزونه فقط
زمانی فراخوانی می‌شود که ایمیجی که در حال pull شدن است با ایمیج‌هایی که افزونه مدیریت می‌کند مطابقت داشته باشد (به matchImages مراجعه کنید).</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام الزامیِ credential provider است. این نام باید با نام فایل اجرایی
provider، آن‌گونه که kubelet می‌بیند، مطابقت داشته باشد. فایل اجرایی باید در پوشه‌ی bin
مربوط به kubelet باشد (که با فلگ --image-credential-provider-bin-dir تعیین می‌شود).
این نام باید در میان همه‌ی providerها یکتا باشد.</p>
</td>
</tr>
<tr><td><code>matchImages</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>matchImages فهرست الزامی‌ای از رشته‌ها است که برای تطبیق با ایمیج‌ها به‌کار می‌رود تا
مشخص شود آیا این provider باید فراخوانی شود یا خیر. اگر یکی از رشته‌ها با ایمیجِ
درخواست‌شده از سوی kubelet مطابقت داشته باشد، افزونه فراخوانی می‌شود و فرصت می‌یابد
اعتبارنامه‌ها را ارائه دهد. انتظار می‌رود ایمیج‌ها شامل دامنه‌ی registry
و مسیر URL باشند.</p>
<p>هر مورد در matchImages یک الگو است که می‌تواند به‌صورت اختیاری شامل یک پورت و یک مسیر باشد.
در دامنه می‌توان از glob استفاده کرد، اما در پورت یا مسیر نمی‌توان. globها
به‌صورت زیردامنه مانند '<em>.k8s.io' یا 'k8s.</em>.io' و نیز دامنه‌های سطح بالا مانند 'k8s.<em>' پشتیبانی می‌شوند.
تطبیق زیردامنه‌های جزئی مانند 'app</em>.k8s.io' نیز پشتیبانی می‌شود. هر glob فقط می‌تواند با
یک بخش از زیردامنه مطابقت داشته باشد؛ بنابراین *.io با *.k8s.io مطابقت ندارد.</p>
<p>زمانی بین یک ایمیج و یک matchImage تطابق وجود دارد که همه‌ی شرایط زیر برقرار باشند:</p>
<ul>
<li>هر دو تعداد بخش‌های دامنه یکسانی داشته باشند و هر بخش مطابقت داشته باشد.</li>
<li>مسیر URL در imageMatch باید پیشوندی از مسیر URL ایمیج هدف باشد.</li>
<li>اگر imageMatch شامل پورت باشد، پورت باید در ایمیج نیز مطابقت داشته باشد.</li>
</ul>
<p>نمونه مقادیر matchImages:</p>
<ul>
<li>123456789.dkr.ecr.us-east-1.amazonaws.com</li>
<li>*.azurecr.io</li>
<li>gcr.io</li>
<li><em>.</em>.registry.io</li>
<li>registry.io:8080/path</li>
</ul>
</td>
</tr>
<tr><td><code>defaultCacheDuration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>defaultCacheDuration مدت‌زمان پیش‌فرضی است که افزونه اعتبارنامه‌ها را در حافظه نگهداری (cache) می‌کند،
در صورتی که مدت‌زمان cache در پاسخ افزونه ارائه نشده باشد. این فیلد الزامی است.</p>
</td>
</tr>
<tr><td><code>apiVersion</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه‌ی ورودیِ الزامیِ CredentialProviderRequest از نوع exec. CredentialProviderResponse بازگردانده‌شده
باید از همان نسخه‌ی رمزگذاری ورودی استفاده کند. مقادیر پشتیبانی‌شده‌ی فعلی عبارت‌اند از:</p>
<ul>
<li>credentialprovider.kubelet.k8s.io/v1</li>
</ul>
</td>
</tr>
<tr><td><code>args</code><br/>
<code>[]string</code>
</td>
<td>
   <p>آرگومان‌هایی که هنگام اجرای فرمان به آن ارسال می‌شوند.</p>
</td>
</tr>
<tr><td><code>env</code><br/>
<a href="#kubelet-config-k8s-io-v1-ExecEnvVar"><code>[]ExecEnvVar</code></a>
</td>
<td>
   <p>Env متغیرهای محیطی اضافی را که باید در اختیار فرایند قرار گیرند تعریف می‌کند. این‌ها
با محیط میزبان و همچنین متغیرهایی که client-go برای
ارسال آرگومان به افزونه استفاده می‌کند، ادغام (union) می‌شوند.</p>
</td>
</tr>
<tr><td><code>tokenAttributes</code><br/>
<a href="#kubelet-config-k8s-io-v1-ServiceAccountTokenAttributes"><code>ServiceAccountTokenAttributes</code></a>
</td>
<td>
   <p>tokenAttributes پیکربندی توکن service account است که به افزونه ارسال می‌شود.
credential provider با تنظیم این فیلد انتخاب می‌کند که برای pull ایمیج از توکن‌های service account استفاده کند.
وقتی این فیلد تنظیم شود، kubelet یک توکن service account تولید می‌کند که به Pod‌ای که
ایمیج برای آن pull می‌شود متصل (bound) است و آن را همراه با سایر
ویژگی‌های موردنیاز افزونه، به‌عنوان بخشی از CredentialProviderRequest به افزونه ارسال می‌کند.</p>
<p>فراداده‌ی service account و ویژگی‌های توکن به‌عنوان یک بُعد برای cache کردن
اعتبارنامه‌ها در kubelet استفاده می‌شوند. کلید cache از ترکیب فراداده‌ی service account
(namespace، name، UID و کلید+مقدار حاشیه‌نویسی‌ها (annotations) برای کلیدهای تعریف‌شده در
serviceAccountTokenAttribute.requiredServiceAccountAnnotationKeys و serviceAccountTokenAttribute.optionalServiceAccountAnnotationKeys) ساخته می‌شود.
فراداده‌ی Pod (namespace، name، UID) که در توکن service account وجود دارد، به‌عنوان یک بُعد
برای cache کردن اعتبارنامه‌ها در kubelet استفاده نمی‌شود. این بدان معناست که بارهای کاری‌ای که از همان service account استفاده می‌کنند
ممکن است در نهایت از اعتبارنامه‌های یکسانی برای pull ایمیج استفاده کنند. افزونه‌هایی که این رفتار را نمی‌خواهند، یا
افزونه‌هایی که در حالت pass-through کار می‌کنند، یعنی توکن service account را همان‌گونه که هست بازمی‌گردانند،
می‌توانند credentialProviderResponse.cacheDuration را برابر 0 قرار دهند. این کار cache شدن
اعتبارنامه‌ها را در kubelet غیرفعال می‌کند و افزونه برای هر pull ایمیج فراخوانی می‌شود. این امر
سربار تولید توکن را برای هر pull ایمیج به همراه دارد، اما تنها راه تضمین این است که
اعتبارنامه‌ها میان Podها به اشتراک گذاشته نشوند (حتی اگر از همان service account استفاده کنند).</p>
</td>
</tr>
</tbody>
</table>

## `ExecEnvVar`     {#kubelet-config-k8s-io-v1-ExecEnvVar}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CredentialProvider](#kubelet-config-k8s-io-v1-CredentialProvider)


<p>ExecEnvVar برای تنظیم متغیرهای محیطی هنگام اجرای یک افزونه‌ی اعتبارنامه‌ی مبتنی بر
exec استفاده می‌شود.</p>


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

## `ServiceAccountTokenAttributes`     {#kubelet-config-k8s-io-v1-ServiceAccountTokenAttributes}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CredentialProvider](#kubelet-config-k8s-io-v1-CredentialProvider)


<p>ServiceAccountTokenAttributes پیکربندی توکن service account است که به افزونه ارسال می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>serviceAccountTokenAudience</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>serviceAccountTokenAudience مخاطب موردنظر (audience) برای توکن service account پروجکت‌شده است.</p>
</td>
</tr>
<tr><td><code>cacheType</code> <B>[الزامی]</B><br/>
<a href="#kubelet-config-k8s-io-v1-ServiceAccountTokenCacheType"><code>ServiceAccountTokenCacheType</code></a>
</td>
<td>
   <p>cacheType نوع کلید cache را مشخص می‌کند که برای cache کردن اعتبارنامه‌های بازگردانده‌شده توسط افزونه
به‌کار می‌رود، زمانی که از توکن service account استفاده می‌شود.
محافظه‌کارانه‌ترین گزینه این است که مقدار آن را &quot;Token&quot; قرار دهید؛ به این معنا که kubelet اعتبارنامه‌های بازگردانده‌شده را
به‌ازای هر توکن cache می‌کند. اگر طول عمر اعتبارنامه‌ی بازگردانده‌شده محدود به طول عمر
توکن service account است، باید همین مقدار تنظیم شود.
اگر منطق دریافت اعتبارنامه در افزونه فقط به service account وابسته است و به claimهای مختص Pod وابسته نیست،
افزونه می‌تواند این مقدار را &quot;ServiceAccount&quot; قرار دهد. در این حالت، kubelet اعتبارنامه‌های بازگردانده‌شده را
به‌ازای هر service account، cache می‌کند. از این گزینه زمانی استفاده کنید که اعتبارنامه‌ی بازگردانده‌شده برای همه‌ی Podهایی که از همان service account استفاده می‌کنند معتبر باشد.</p>
</td>
</tr>
<tr><td><code>requireServiceAccount</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>requireServiceAccount مشخص می‌کند که آیا افزونه نیاز دارد Pod یک service account داشته باشد یا خیر.
اگر روی true تنظیم شود، kubelet فقط در صورتی افزونه را فراخوانی می‌کند که Pod دارای service account باشد.
اگر روی false تنظیم شود، kubelet افزونه را حتی در صورتی که Pod فاقد service account باشد نیز فراخوانی می‌کند
و در آن سناریو توکنی را در CredentialProviderRequest قرار نمی‌دهد. این برای افزونه‌هایی مفید است که
برای pull ایمیج Podهای فاقد service account (مثلاً static Podها) استفاده می‌شوند.</p>
</td>
</tr>
<tr><td><code>requiredServiceAccountAnnotationKeys</code><br/>
<code>[]string</code>
</td>
<td>
   <p>requiredServiceAccountAnnotationKeys فهرست کلیدهای حاشیه‌نویسی (annotation) است که افزونه به آن‌ها علاقه‌مند است
و حضورشان در service account الزامی است.
کلیدهای تعریف‌شده در این فهرست از service account متناظر استخراج می‌شوند و به‌عنوان بخشی از CredentialProviderRequest
به افزونه ارسال می‌گردند. اگر هر یک از کلیدهای تعریف‌شده در این فهرست
در service account وجود نداشته باشد، kubelet افزونه را فراخوانی نمی‌کند و خطا بازمی‌گرداند.
این فیلد اختیاری است و ممکن است خالی باشد. افزونه‌ها می‌توانند از این فیلد برای استخراج
اطلاعات اضافیِ موردنیاز برای دریافت اعتبارنامه‌ها یا برای اینکه بارهای کاری بتوانند انتخاب کنند که
از توکن‌های service account برای pull ایمیج استفاده کنند، بهره ببرند.
اگر خالی نباشد، requireServiceAccount باید روی true تنظیم شود.
کلیدهای این فهرست باید یکتا باشند.
این فهرست باید با optionalServiceAccountAnnotationKeys اشتراکی نداشته باشد (متقابلاً ناسازگار باشد).</p>
</td>
</tr>
<tr><td><code>optionalServiceAccountAnnotationKeys</code><br/>
<code>[]string</code>
</td>
<td>
   <p>optionalServiceAccountAnnotationKeys فهرست کلیدهای حاشیه‌نویسی (annotation) است که افزونه به آن‌ها علاقه‌مند است
و حضورشان در service account اختیاری است.
کلیدهای تعریف‌شده در این فهرست از service account متناظر استخراج می‌شوند و به‌عنوان بخشی از CredentialProviderRequest
به افزونه ارسال می‌گردند. افزونه مسئول اعتبارسنجیِ
وجود حاشیه‌نویسی‌ها و مقادیر آن‌ها است.
این فیلد اختیاری است و ممکن است خالی باشد. افزونه‌ها می‌توانند از این فیلد برای استخراج
اطلاعات اضافیِ موردنیاز برای دریافت اعتبارنامه‌ها استفاده کنند.
کلیدهای این فهرست باید یکتا باشند.</p>
</td>
</tr>
</tbody>
</table>

## `ServiceAccountTokenCacheType`     {#kubelet-config-k8s-io-v1-ServiceAccountTokenCacheType}
    
(نام مستعار برای `string`)

**در این بخش‌ها ظاهر می‌شود:**

- [ServiceAccountTokenAttributes](#kubelet-config-k8s-io-v1-ServiceAccountTokenAttributes)


<p>ServiceAccountTokenCacheType نوع کلید cache است که برای cache کردن اعتبارنامه‌های بازگردانده‌شده توسط افزونه
به‌کار می‌رود، زمانی که از توکن service account استفاده می‌شود.</p>
