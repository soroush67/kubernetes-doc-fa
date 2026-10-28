---
title: پیکربندی Kubelet (v1beta1)
content_type: tool-reference
package: kubelet.config.k8s.io/v1beta1
auto_generated: true
---


## انواع منابع {#resource-types}


- [CredentialProviderConfig](#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig)
- [ImagePullIntent](#kubelet-config-k8s-io-v1beta1-ImagePullIntent)
- [ImagePulledRecord](#kubelet-config-k8s-io-v1beta1-ImagePulledRecord)
- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)
- [SerializedNodeConfigSource](#kubelet-config-k8s-io-v1beta1-SerializedNodeConfigSource)
  
    
    

## `FormatOptions`     {#FormatOptions}
    

**نمایش داده‌شده در:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>FormatOptions شامل گزینه‌هایی برای قالب‌های مختلف لاگ‌گیری است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>text</code> <B>[Required]</B><br/>
<a href="#TextOptions"><code>TextOptions</code></a>
</td>
<td>
   <p>[آلفا] Text شامل گزینه‌هایی برای قالب لاگ‌گیری &quot;text&quot; است.
فقط در صورتی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
<tr><td><code>json</code> <B>[Required]</B><br/>
<a href="#JSONOptions"><code>JSONOptions</code></a>
</td>
<td>
   <p>[آلفا] JSON شامل گزینه‌هایی برای قالب لاگ‌گیری &quot;json&quot; است.
فقط در صورتی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
</tbody>
</table>

## `JSONOptions`     {#JSONOptions}
    

**نمایش داده‌شده در:**

- [FormatOptions](#FormatOptions)


<p>JSONOptions شامل گزینه‌هایی برای قالب لاگ‌گیری &quot;json&quot; است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>OutputRoutingOptions</code> <B>[Required]</B><br/>
<a href="#OutputRoutingOptions"><code>OutputRoutingOptions</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `LogFormatFactory`     {#LogFormatFactory}
    


<p>LogFormatFactory پشتیبانی از یک قالب لاگ اضافی و غیرپیش‌فرض مشخص را فراهم می‌کند.</p>




## `LoggingConfiguration`     {#LoggingConfiguration}
    

**نمایش داده‌شده در:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>LoggingConfiguration شامل گزینه‌های لاگ‌گیری است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>format</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Format Flag ساختار پیام‌های لاگ را مشخص می‌کند.
مقدار پیش‌فرض format برابر <code>text</code> است.</p>
</td>
</tr>
<tr><td><code>flushFrequency</code> <B>[Required]</B><br/>
<a href="#TimeOrMetaDuration"><code>TimeOrMetaDuration</code></a>
</td>
<td>
   <p>بیشینه زمان بین دو عملیات flush لاگ.
اگر مقدار از نوع رشته باشد، به‌صورت یک بازه زمانی (duration) تفسیر می‌شود (مثلاً &quot;1s&quot;).
اگر مقدار از نوع عدد صحیح باشد، بیشینه تعداد نانوثانیه‌ها را مشخص می‌کند (مثلاً 1s = 1000000000).
اگر بک‌اند لاگ‌گیری انتخاب‌شده پیام‌های لاگ را بدون بافر بنویسد، این مقدار نادیده گرفته می‌شود.</p>
</td>
</tr>
<tr><td><code>verbosity</code> <B>[Required]</B><br/>
<a href="#VerbosityLevel"><code>VerbosityLevel</code></a>
</td>
<td>
   <p>Verbosity آستانه‌ای است که تعیین می‌کند کدام پیام‌های لاگ
ثبت شوند. مقدار پیش‌فرض صفر است که فقط مهم‌ترین
پیام‌ها را ثبت می‌کند. مقادیر بالاتر پیام‌های بیشتری را فعال می‌کنند. پیام‌های خطا
همیشه ثبت می‌شوند.</p>
</td>
</tr>
<tr><td><code>vmodule</code> <B>[Required]</B><br/>
<a href="#VModuleConfiguration"><code>VModuleConfiguration</code></a>
</td>
<td>
   <p>VModule آستانه verbosity را برای فایل‌های منفرد بازنویسی می‌کند.
فقط برای قالب لاگ &quot;text&quot; پشتیبانی می‌شود.</p>
</td>
</tr>
<tr><td><code>options</code> <B>[Required]</B><br/>
<a href="#FormatOptions"><code>FormatOptions</code></a>
</td>
<td>
   <p>[آلفا] Options شامل پارامترهای اضافی مختص
قالب‌های مختلف لاگ‌گیری است. فقط گزینه‌های مربوط به قالب
انتخاب‌شده به کار گرفته می‌شوند، اما همه آن‌ها اعتبارسنجی می‌شوند.
فقط در صورتی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
</tbody>
</table>

## `LoggingOptions`     {#LoggingOptions}
    


<p>LoggingOptions را می‌توان همراه با ValidateAndApplyWithOptions برای بازنویسی
برخی مقادیر پیش‌فرض سراسری به کار برد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ErrorStream</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/io#Writer"><code>io.Writer</code></a>
</td>
<td>
   <p>ErrorStream را می‌توان برای بازنویسی مقدار پیش‌فرض os.Stderr به کار برد.</p>
</td>
</tr>
<tr><td><code>InfoStream</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/io#Writer"><code>io.Writer</code></a>
</td>
<td>
   <p>InfoStream را می‌توان برای بازنویسی مقدار پیش‌فرض os.Stdout به کار برد.</p>
</td>
</tr>
</tbody>
</table>

## `OutputRoutingOptions`     {#OutputRoutingOptions}
    

**نمایش داده‌شده در:**

- [JSONOptions](#JSONOptions)

- [TextOptions](#TextOptions)


<p>OutputRoutingOptions شامل گزینه‌هایی است که هم توسط &quot;text&quot; و هم توسط &quot;json&quot; پشتیبانی می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>splitStream</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>[آلفا] SplitStream پیام‌های خطا را به stderr هدایت می‌کند، در حالی که
پیام‌های اطلاعاتی با استفاده از بافر به stdout می‌روند. رفتار پیش‌فرض نوشتن
هر دو نوع پیام در stdout و بدون بافر است. فقط در صورتی در دسترس است که
feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
<tr><td><code>infoBufferSize</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#QuantityValue"><code>k8s.io/apimachinery/pkg/api/resource.QuantityValue</code></a>
</td>
<td>
   <p>[آلفا] InfoBufferSize اندازه جریان اطلاعات (info stream) را هنگام
استفاده از جریان‌های جداشده تعیین می‌کند. مقدار پیش‌فرض صفر است که بافر کردن را غیرفعال می‌کند.
فقط در صورتی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
</tbody>
</table>

## `TextOptions`     {#TextOptions}
    

**نمایش داده‌شده در:**

- [FormatOptions](#FormatOptions)


<p>TextOptions شامل گزینه‌هایی برای قالب لاگ‌گیری &quot;text&quot; است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>OutputRoutingOptions</code> <B>[Required]</B><br/>
<a href="#OutputRoutingOptions"><code>OutputRoutingOptions</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `TimeOrMetaDuration`     {#TimeOrMetaDuration}
    

**نمایش داده‌شده در:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>TimeOrMetaDuration صرفاً برای سازگاری با نسخه‌های قبلی برای فیلد
flushFrequency وجود دارد و فیلدهای جدید باید از metav1.Duration استفاده کنند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>Duration</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>Duration مقدار بازه زمانی را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>-</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>SerializeAsString مشخص می‌کند که مقدار به‌صورت رشته سریال‌سازی شود یا به‌صورت عدد صحیح.</p>
</td>
</tr>
</tbody>
</table>

## `TracingConfiguration`     {#TracingConfiguration}
    

**نمایش داده‌شده در:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>TracingConfiguration پیکربندی نسخه‌دار را برای کلاینت‌های ردیابی (tracing) OpenTelemetry فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>Endpoint مربوط به collector که این مؤلفه ردیابی‌ها (traces) را به آن گزارش می‌دهد.
اتصال ناامن است و در حال حاضر از TLS پشتیبانی نمی‌کند.
توصیه می‌شود این مقدار تنظیم نشود و endpoint همان مقدار پیش‌فرض otlp grpc یعنی localhost:4317 باشد.</p>
</td>
</tr>
<tr><td><code>samplingRatePerMillion</code><br/>
<code>int32</code>
</td>
<td>
   <p>SamplingRatePerMillion تعداد نمونه‌هایی است که به ازای هر یک میلیون span جمع‌آوری می‌شود.
توصیه می‌شود این مقدار تنظیم نشود. در صورت تنظیم نشدن، نمونه‌بردار (sampler) از نرخ نمونه‌برداری
span والد خود پیروی می‌کند، ولی در غیر این صورت هرگز نمونه‌برداری نمی‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `VModuleConfiguration`     {#VModuleConfiguration}
    
(نام مستعار برای `[]k8s.io/component-base/logs/api/v1.VModuleItem`)

**نمایش داده‌شده در:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>VModuleConfiguration مجموعه‌ای از نام فایل‌ها یا الگوهای منفرد
و آستانه verbosity متناظر با هرکدام است.</p>




## `VerbosityLevel`     {#VerbosityLevel}
    
(نام مستعار برای `uint32`)

**نمایش داده‌شده در:**

- [LoggingConfiguration](#LoggingConfiguration)



<p>VerbosityLevel نشان‌دهنده یک آستانه verbosity در klog یا logr است.</p>



  

## `CredentialProviderConfig`     {#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig}
    


<p>CredentialProviderConfig پیکربندی‌ای است که اطلاعات مربوط به
هر ارائه‌دهنده اعتبارنامه از نوع exec را در بر دارد. Kubelet این پیکربندی را از دیسک می‌خواند و
هر ارائه‌دهنده را بر اساس آنچه در نوع CredentialProvider مشخص شده است فعال می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CredentialProviderConfig</code></td></tr>
    
  
<tr><td><code>providers</code> <B>[Required]</B><br/>
<a href="#kubelet-config-k8s-io-v1beta1-CredentialProvider"><code>[]CredentialProvider</code></a>
</td>
<td>
   <p>providers فهرستی از افزونه‌های ارائه‌دهنده اعتبارنامه است که توسط kubelet فعال می‌شوند.
چند ارائه‌دهنده ممکن است با یک ایمیج واحد مطابقت داشته باشند؛ در این صورت اعتبارنامه‌های
همه ارائه‌دهندگان به kubelet بازگردانده می‌شود. اگر برای یک ایمیج واحد چند ارائه‌دهنده فراخوانی شوند،
نتایج با هم ترکیب می‌شوند. اگر ارائه‌دهندگان کلیدهای احراز هویت هم‌پوشان بازگردانند،
مقدار ارائه‌دهنده‌ای که در این فهرست زودتر آمده است ابتدا امتحان می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `ImagePullIntent`     {#kubelet-config-k8s-io-v1beta1-ImagePullIntent}
    


<p>ImagePullIntent رکوردی از تلاش kubelet برای pull کردن یک ایمیج است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ImagePullIntent</code></td></tr>
    
  
<tr><td><code>image</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Image مشخصات ایمیج است که از فیلد <code>image</code> یک Container گرفته می‌شود.
نام فایل، هش SHA-256 این مقدار است. این کار برای پرهیز از وجود
نویسه‌های نامناسب برای نام فایل مانند ':' و '/' انجام می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `ImagePulledRecord`     {#kubelet-config-k8s-io-v1beta1-ImagePulledRecord}
    


<p>ImagePullRecord رکوردی از ایمیجی است که توسط kubelet pull شده است.</p>
<p>اگر در فیلد <code>kubernetesSecrets</code> هیچ رکوردی وجود نداشته باشد و هر دو فیلد <code>nodeWideCredentials</code>
و <code>anonymous</code> برابر <code>false</code> باشند، اعتبارنامه‌ها باید در دفعه بعدی که
ایمیجِ نمایش‌داده‌شده توسط این رکورد درخواست می‌شود، دوباره بررسی شوند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ImagePulledRecord</code></td></tr>
    
  
<tr><td><code>lastUpdatedTime</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>LastUpdatedTime زمان آخرین به‌روزرسانی این رکورد است.</p>
</td>
</tr>
<tr><td><code>imageRef</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>ImageRef ارجاعی به ایمیجی است که این فایل نمایش می‌دهد و
از CRI دریافت شده است.
نام فایل، هش SHA-256 این مقدار است. این کار برای پرهیز از وجود
نویسه‌های نامناسب برای نام فایل مانند ':' و '/' انجام می‌شود.</p>
</td>
</tr>
<tr><td><code>credentialMapping</code> <B>[Required]</B><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ImagePullCredentials"><code>map[string]ImagePullCredentials</code></a>
</td>
<td>
   <p>CredentialMapping مقدار <code>image</code> را به مجموعه اعتبارنامه‌هایی نگاشت می‌کند که
پیش‌تر با آن‌ها pull شده است.
<code>image</code> در اینجا محتوای فیلد <code>image</code> کانتینر یک Pod است که
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

## `KubeletConfiguration`     {#kubelet-config-k8s-io-v1beta1-KubeletConfiguration}
    


<p>KubeletConfiguration شامل پیکربندی Kubelet است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>KubeletConfiguration</code></td></tr>
    
  
<tr><td><code>enableServer</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableServer سرور امن Kubelet را فعال می‌کند.
توجه: پورت ناامن Kubelet توسط گزینه readOnlyPort کنترل می‌شود.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>staticPodPath</code><br/>
<code>string</code>
</td>
<td>
   <p>staticPodPath مسیر دایرکتوری حاوی Podهای محلی (ایستا) برای اجرا،
یا مسیر یک فایل Pod ایستای منفرد است.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>podLogsDir</code><br/>
<code>string</code>
</td>
<td>
   <p>podLogsDir مسیر دایرکتوری ریشهٔ سفارشی است که kubelet برای قرار دادن فایل‌های لاگ Pod از آن استفاده می‌کند.
پیش‌فرض: &quot;/var/log/pods/&quot;
توجه: استفاده از پوشهٔ موقت به‌عنوان دایرکتوری لاگ توصیه نمی‌شود، زیرا ممکن است
در بسیاری از بخش‌ها رفتار پیش‌بینی‌نشده‌ای ایجاد کند.</p>
</td>
</tr>
<tr><td><code>syncFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>syncFrequency بیشینهٔ فاصلهٔ زمانی بین همگام‌سازی کانتینرهای در حال اجرا
و پیکربندی است.
پیش‌فرض: &quot;1m&quot;</p>
</td>
</tr>
<tr><td><code>fileCheckFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>fileCheckFrequency فاصلهٔ زمانی بین بررسی فایل‌های پیکربندی برای
یافتن داده‌های جدید است.
پیش‌فرض: &quot;20s&quot;</p>
</td>
</tr>
<tr><td><code>httpCheckFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>httpCheckFrequency فاصلهٔ زمانی بین بررسی http برای یافتن داده‌های جدید است.
پیش‌فرض: &quot;20s&quot;</p>
</td>
</tr>
<tr><td><code>staticPodURL</code><br/>
<code>string</code>
</td>
<td>
   <p>staticPodURL نشانی URL برای دسترسی به Podهای ایستا جهت اجراست.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>staticPodURLHeader</code><br/>
<code>map[string][]string</code>
</td>
<td>
   <p>staticPodURLHeader نگاشتی از لیست‌هاست که شامل سرآیندهای HTTP برای استفاده هنگام دسترسی به podURL است.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>address</code><br/>
<code>string</code>
</td>
<td>
   <p>address نشانی IP است که Kubelet روی آن سرویس‌دهی می‌کند (برای همهٔ
رابط‌ها روی 0.0.0.0 تنظیم کنید).
پیش‌فرض: &quot;0.0.0.0&quot;</p>
</td>
</tr>
<tr><td><code>port</code><br/>
<code>int32</code>
</td>
<td>
   <p>port پورتی است که Kubelet روی آن سرویس‌دهی می‌کند.
شمارهٔ پورت باید بین 1 تا 65535 (شامل هر دو مقدار) باشد.
پیش‌فرض: 10250</p>
</td>
</tr>
<tr><td><code>readOnlyPort</code><br/>
<code>int32</code>
</td>
<td>
   <p>readOnlyPort پورت فقط‌خواندنی است که Kubelet بدون
احراز هویت/مجوزدهی روی آن سرویس‌دهی می‌کند.
شمارهٔ پورت باید بین 1 تا 65535 (شامل هر دو مقدار) باشد.
تنظیم این فیلد روی 0 سرویس فقط‌خواندنی را غیرفعال می‌کند.
پیش‌فرض: 0 (غیرفعال)</p>
</td>
</tr>
<tr><td><code>tlsCertFile</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsCertFile فایل حاوی گواهی x509 برای HTTPS است (گواهی CA، در صورت وجود،
پس از گواهی سرور الحاق می‌شود). اگر tlsCertFile و
tlsPrivateKeyFile ارائه نشوند، یک گواهی و کلید خودامضا
برای نشانی عمومی تولید می‌شود و در دایرکتوری ارسال‌شده به پرچم --cert-dir
در Kubelet ذخیره می‌گردد.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>tlsPrivateKeyFile</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsPrivateKeyFile فایل حاوی کلید خصوصی x509 مطابق با tlsCertFile است.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>tlsCipherSuites</code><br/>
<code>[]string</code>
</td>
<td>
   <p>tlsCipherSuites فهرست cipher suiteهای مجاز برای سرور است.
توجه کنید که cipher suiteهای TLS 1.3 قابل پیکربندی نیستند.
مقادیر از ثابت‌های بستهٔ tls گرفته می‌شوند (https://golang.org/pkg/crypto/tls/#pkg-constants).
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>tlsCurvePreferences</code><br/>
<code>[]int32</code>
</td>
<td>
   <p>tlsCurvePreferences مجموعهٔ سازوکارهای مجاز تبادل کلید برای سرور است
که به‌صورت مقادیر عددی CurveID در crypto/tls زبان Go مشخص می‌شود.
مقادیر پشتیبانی‌شده به نسخهٔ Go مورد استفاده بستگی دارد.
برای مقادیر پشتیبانی‌شده در هر نسخهٔ Go به https://pkg.go.dev/crypto/tls#CurveID مراجعه کنید.
ترتیب فهرست نادیده گرفته می‌شود و سازوکارهای تبادل کلید
با استفاده از یک ترتیب ترجیحی داخلی توسط Go از میان این فهرست انتخاب می‌شوند.
اگر خالی باشد، منحنی‌های پیش‌فرض Go استفاده می‌شوند.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>tlsMinVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>tlsMinVersion حداقل نسخهٔ پشتیبانی‌شدهٔ TLS است.
مقادیر از ثابت‌های بستهٔ tls گرفته می‌شوند (https://golang.org/pkg/crypto/tls/#pkg-constants).
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>rotateCertificates</code><br/>
<code>bool</code>
</td>
<td>
   <p>rotateCertificates چرخش گواهی کلاینت را فعال می‌کند. Kubelet یک
گواهی جدید از API مربوط به certificates.k8s.io درخواست می‌کند. این کار نیازمند یک تأییدکننده است تا
درخواست‌های امضای گواهی را تأیید کند.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>serverTLSBootstrap</code><br/>
<code>bool</code>
</td>
<td>
   <p>serverTLSBootstrap راه‌اندازی اولیهٔ گواهی سرور را فعال می‌کند. به‌جای امضای
خودکار گواهی سرویس‌دهی، Kubelet یک گواهی از
API مربوط به 'certificates.k8s.io' درخواست می‌کند. این کار نیازمند یک تأییدکننده است تا
درخواست‌های امضای گواهی (CSR) را تأیید کند. هنگام تنظیم این فیلد، ویژگی
RotateKubeletServerCertificate باید فعال باشد.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>authentication</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletAuthentication"><code>KubeletAuthentication</code></a>
</td>
<td>
   <p>authentication مشخص می‌کند درخواست‌ها به سرور Kubelet چگونه احراز هویت می‌شوند.
پیش‌فرض‌ها:
anonymous:
enabled: false
webhook:
enabled: true
cacheTTL: &quot;2m&quot;</p>
</td>
</tr>
<tr><td><code>authorization</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletAuthorization"><code>KubeletAuthorization</code></a>
</td>
<td>
   <p>authorization مشخص می‌کند درخواست‌ها به سرور Kubelet چگونه مجوزدهی می‌شوند.
پیش‌فرض‌ها:
mode: Webhook
webhook:
cacheAuthorizedTTL: &quot;5m&quot;
cacheUnauthorizedTTL: &quot;30s&quot;</p>
</td>
</tr>
<tr><td><code>registryPullQPS</code><br/>
<code>int32</code>
</td>
<td>
   <p>registryPullQPS حد مجاز pull از رجیستری در هر ثانیه است.
مقدار نباید عددی منفی باشد.
تنظیم آن روی 0 به معنای نبود محدودیت است.
پیش‌فرض: 5</p>
</td>
</tr>
<tr><td><code>registryBurst</code><br/>
<code>int32</code>
</td>
<td>
   <p>registryBurst بیشینهٔ اندازهٔ pullهای انفجاری است و به‌طور موقت اجازه می‌دهد
pullها تا این عدد افزایش یابند، بدون آنکه همچنان از registryPullQPS فراتر روند.
مقدار نباید عددی منفی باشد.
فقط زمانی استفاده می‌شود که registryPullQPS بزرگ‌تر از 0 باشد.
پیش‌فرض: 10</p>
</td>
</tr>
<tr><td><code>imagePullCredentialsVerificationPolicy</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ImagePullCredentialsVerificationPolicy"><code>ImagePullCredentialsVerificationPolicy</code></a>
</td>
<td>
   <p>imagePullCredentialsVerificationPolicy تعیین می‌کند هنگامی که یک Pod ایمیجی را درخواست می‌کند که از قبل روی نود وجود دارد،
اعتبارنامه‌ها چگونه باید تأیید شوند:</p>
<ul>
<li>NeverVerify
<ul>
<li>هر کسی روی نود می‌تواند از هر ایمیج موجود روی نود استفاده کند</li>
</ul>
</li>
<li>NeverVerifyPreloadedImages
<ul>
<li>ایمیج‌هایی که توسط چیزی غیر از kubelet روی نود pull شده‌اند
بدون تأیید مجدد اعتبارنامه‌های pull قابل استفاده‌اند</li>
</ul>
</li>
<li>NeverVerifyAllowlistedImages
<ul>
<li>مانند &quot;NeverVerifyPreloadedImages&quot; اما فقط ایمیج‌های نود موجود در
<code>preloadedImagesVerificationAllowlist</code> نیازی به تأیید مجدد ندارند</li>
</ul>
</li>
<li>AlwaysVerify
<ul>
<li>همهٔ ایمیج‌ها نیازمند تأیید مجدد اعتبارنامه هستند</li>
</ul>
</li>
</ul>
</td>
</tr>
<tr><td><code>preloadedImagesVerificationAllowlist</code><br/>
<code>[]string</code>
</td>
<td>
   <p>preloadedImagesVerificationAllowlist فهرستی از ایمیج‌ها را مشخص می‌کند که برای
<code>imagePullCredentialsVerificationPolicy</code> با مقدار &quot;NeverVerifyAllowlistedImages&quot;
از تأیید مجدد اعتبارنامه معاف هستند.
این فهرست یک پسوند wildcard برای کل بخش مسیر، یعنی &quot;/*&quot;، را می‌پذیرد.
فقط از مشخصات ایمیج بدون تگ یا digest استفاده کنید.</p>
</td>
</tr>
<tr><td><code>eventRecordQPS</code><br/>
<code>int32</code>
</td>
<td>
   <p>eventRecordQPS بیشینهٔ تعداد رویدادهای ایجادشده در هر ثانیه است. اگر 0 باشد،
هیچ محدودیتی اعمال نمی‌شود. مقدار نمی‌تواند عددی منفی باشد.
پیش‌فرض: 50</p>
</td>
</tr>
<tr><td><code>eventBurst</code><br/>
<code>int32</code>
</td>
<td>
   <p>eventBurst بیشینهٔ اندازهٔ یک انفجار از ایجاد رویدادهاست و به‌طور موقت
اجازه می‌دهد ایجاد رویدادها تا این عدد افزایش یابد، بدون آنکه همچنان از
eventRecordQPS فراتر رود. این فیلد نمی‌تواند عددی منفی باشد و فقط
زمانی استفاده می‌شود که eventRecordQPS &gt; 0 باشد.
پیش‌فرض: 100</p>
</td>
</tr>
<tr><td><code>enableDebuggingHandlers</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableDebuggingHandlers نقاط انتهایی سرور را برای دسترسی به لاگ
و اجرای محلی کانتینرها و دستورات، از جمله قابلیت‌های exec،
attach، logs و portforward، فعال می‌کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>enableContentionProfiling</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableContentionProfiling در صورتی که enableDebuggingHandlers برابر true باشد، block profiling را فعال می‌کند.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>healthzPort</code><br/>
<code>int32</code>
</td>
<td>
   <p>healthzPort پورت نقطهٔ انتهایی healthz روی localhost است (برای غیرفعال‌سازی روی 0 تنظیم کنید).
عدد معتبر بین 1 تا 65535 است.
پیش‌فرض: 10248</p>
</td>
</tr>
<tr><td><code>healthzBindAddress</code><br/>
<code>string</code>
</td>
<td>
   <p>healthzBindAddress نشانی IP است که سرور healthz روی آن سرویس‌دهی می‌کند.
پیش‌فرض: &quot;127.0.0.1&quot;</p>
</td>
</tr>
<tr><td><code>oomScoreAdj</code><br/>
<code>int32</code>
</td>
<td>
   <p>oomScoreAdj مقدار oom-score-adj برای فرایند kubelet است. مقادیر
باید در بازهٔ [-1000, 1000] باشند.
پیش‌فرض: -999</p>
</td>
</tr>
<tr><td><code>clusterDomain</code><br/>
<code>string</code>
</td>
<td>
   <p>clusterDomain دامنهٔ DNS این کلاستر است. در صورت تنظیم، kubelet
همهٔ کانتینرها را طوری پیکربندی می‌کند که علاوه بر دامنه‌های جست‌وجوی
میزبان، این دامنه را نیز جست‌وجو کنند.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>clusterDNS</code><br/>
<code>[]string</code>
</td>
<td>
   <p>clusterDNS فهرستی از نشانی‌های IP برای سرور DNS کلاستر است. در صورت تنظیم،
kubelet همهٔ کانتینرها را طوری پیکربندی می‌کند که برای تفکیک DNS از این سرور
به‌جای سرورهای DNS میزبان استفاده کنند.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>streamingConnectionIdleTimeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>streamingConnectionIdleTimeout بیشترین زمانی است که یک اتصال جریانی
می‌تواند بیکار بماند، پیش از آنکه اتصال به‌طور خودکار بسته شود.
منسوخ‌شده: دیگر هیچ تأثیری ندارد.
پیش‌فرض: &quot;4h&quot;</p>
</td>
</tr>
<tr><td><code>nodeStatusUpdateFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeStatusUpdateFrequency فرکانسی است که kubelet وضعیت نود را محاسبه می‌کند
و بررسی می‌کند که آیا به‌روزرسانی در API server لازم است یا خیر. وضعیت
یا هنگام تغییر یا زمانی که از آخرین گزارش به اندازهٔ
nodeStatusReportFrequency گذشته باشد، به API server ارسال می‌شود.
پیش‌فرض: &quot;10s&quot;</p>
</td>
</tr>
<tr><td><code>nodeStatusReportFrequency</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeStatusReportFrequency فرکانسی است که kubelet در صورت تغییر نکردن وضعیت نود،
آن را به API server ارسال می‌کند. در صورت شناسایی هر تغییری، Kubelet
این فرکانس را نادیده می‌گیرد و وضعیت نود را بلافاصله ارسال می‌کند.
مقدار پیش‌فرض nodeStatusReportFrequency برابر 5m است. اما اگر
nodeStatusUpdateFrequency به‌صراحت تنظیم شده باشد،
مقدار پیش‌فرض nodeStatusReportFrequency برای سازگاری با نسخه‌های قبلی برابر
nodeStatusUpdateFrequency خواهد بود.
پیش‌فرض: &quot;5m&quot;</p>
</td>
</tr>
<tr><td><code>nodeLeaseDurationSeconds</code><br/>
<code>int32</code>
</td>
<td>
   <p>nodeLeaseDurationSeconds مدت زمانی است که Kubelet روی Lease متناظر با خود تنظیم می‌کند.
NodeLease با ایجاد یک lease توسط Kubelet و تمدید دوره‌ای آن، که به نام نود
در فضای نام kube-node-lease نام‌گذاری شده است، شاخصی از سلامت نود فراهم می‌کند.
اگر lease منقضی شود، نود را می‌توان ناسالم در نظر گرفت.
در حال حاضر lease طبق KEP-0009 هر 10 ثانیه تمدید می‌شود. در آینده، بازهٔ تمدید lease
ممکن است بر اساس مدت lease تنظیم شود.
مقدار فیلد باید بزرگ‌تر از 0 باشد.
پیش‌فرض: 40</p>
</td>
</tr>
<tr><td><code>imageMinimumGCAge</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>imageMinimumGCAge حداقل سن یک ایمیج استفاده‌نشده است، پیش از آنکه
garbage collection روی آن انجام شود.
مقدار فیلد باید بزرگ‌تر از 0 باشد.
اگر تنظیم نشده یا 0 باشد، پیش‌فرض 2m است.
پیش‌فرض: &quot;2m&quot;</p>
</td>
</tr>
<tr><td><code>imageMaximumGCAge</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>imageMaximumGCAge بیشترین مدتی است که یک ایمیج می‌تواند استفاده نشده باقی بماند، پیش از آنکه garbage collection روی آن انجام شود.
پیش‌فرض این فیلد &quot;0s&quot; است که این فیلد را غیرفعال می‌کند؛ یعنی ایمیج‌ها
بر اساس مدت طولانی استفاده‌نشدن، garbage collect نخواهند شد.
پیش‌فرض: &quot;0s&quot; (غیرفعال)</p>
</td>
</tr>
<tr><td><code>imageGCHighThresholdPercent</code><br/>
<code>int32</code>
</td>
<td>
   <p>imageGCHighThresholdPercent درصد استفاده از دیسک است که پس از آن
garbage collection ایمیج همیشه اجرا می‌شود. این درصد با
تقسیم مقدار این فیلد بر 100 محاسبه می‌شود، بنابراین این فیلد باید بین 0 تا
100 (شامل هر دو مقدار) باشد. در صورت تعیین، مقدار باید بزرگ‌تر از
imageGCLowThresholdPercent باشد.
پیش‌فرض: 85</p>
</td>
</tr>
<tr><td><code>imageGCLowThresholdPercent</code><br/>
<code>int32</code>
</td>
<td>
   <p>imageGCLowThresholdPercent درصد استفاده از دیسک است که پیش از آن
garbage collection ایمیج هرگز اجرا نمی‌شود. کمترین میزان استفاده از دیسک برای
garbage collection. این درصد با تقسیم مقدار این فیلد بر 100 محاسبه می‌شود،
بنابراین مقدار فیلد باید بین 0 تا 100 (شامل هر دو مقدار) باشد. در صورت تعیین،
مقدار باید کمتر از imageGCHighThresholdPercent باشد.
پیش‌فرض: 80</p>
</td>
</tr>
<tr><td><code>volumeStatsAggPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>volumeStatsAggPeriod فرکانس محاسبه و ذخیرهٔ موقت (cache) میزان استفاده از دیسک حجم‌ها
برای همهٔ Podهاست.
پیش‌فرض: &quot;1m&quot;</p>
</td>
</tr>
<tr><td><code>kubeletCgroups</code><br/>
<code>string</code>
</td>
<td>
   <p>kubeletCgroups نام مطلق cgroupهایی است که kubelet در آن‌ها ایزوله می‌شود.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>systemCgroups</code><br/>
<code>string</code>
</td>
<td>
   <p>systemCgroups نام مطلق cgroupهایی است که همهٔ فرایندهای غیرهسته‌ای که
هنوز در یک کانتینر نیستند در آن‌ها قرار داده می‌شوند. خالی بودن آن
به معنای نبود کانتینر است. بازگرداندن این پرچم به حالت قبل نیازمند راه‌اندازی مجدد است.
اگر این فیلد خالی نباشد، باید cgroupRoot مشخص شود.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>cgroupRoot</code><br/>
<code>string</code>
</td>
<td>
   <p>cgroupRoot همان cgroup ریشه برای استفاده توسط Podهاست. این مورد توسط
container runtime و در حد امکان (best effort) مدیریت می‌شود.</p>
</td>
</tr>
<tr><td><code>cgroupsPerQOS</code><br/>
<code>bool</code>
</td>
<td>
   <p>cgroupsPerQOS سلسله‌مراتب CGroup مبتنی بر QoS را فعال می‌کند: CGroupهای سطح بالا برای کلاس‌های QoS
و همهٔ Podهای Burstable و BestEffort زیر CGroup سطح بالای QoS مخصوص خود بالا آورده می‌شوند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>cgroupDriver</code><br/>
<code>string</code>
</td>
<td>
   <p>cgroupDriver درایوری است که kubelet برای مدیریت CGroupها روی میزبان استفاده می‌کند (cgroupfs
یا systemd).
پیش‌فرض: &quot;cgroupfs&quot;</p>
</td>
</tr>
<tr><td><code>cpuManagerPolicy</code><br/>
<code>string</code>
</td>
<td>
   <p>cpuManagerPolicy نام سیاستی است که باید استفاده شود.
پیش‌فرض: &quot;None&quot;</p>
</td>
</tr>
<tr><td><code>singleProcessOOMKill</code><br/>
<code>bool</code>
</td>
<td>
   <p>singleProcessOOMKill، در صورت true بودن، از تنظیم شدن پرچم <code>memory.oom.group</code> برای cgroupهای
کانتینر در cgroups v2 جلوگیری می‌کند. این امر باعث می‌شود فرایندهای درون کانتینر به‌جای OOM kill شدن به‌صورت گروهی،
به‌صورت جداگانه OOM kill شوند. یعنی اگر true باشد، رفتار با رفتار cgroups v1 هم‌راستا می‌شود.
در صورت عدم تعیین، مقدار پیش‌فرض به‌طور خودکار تعیین می‌شود.
در سیستم‌عامل‌های غیرلینوکسی مانند ویندوز، فقط null / absent مجاز است.
در لینوکس با cgroup v1، فقط null / absent و true مجازند.
در لینوکس با cgroup v2، null / absent، true و false مجازند. مقدار پیش‌فرض false است.</p>
</td>
</tr>
<tr><td><code>cpuManagerPolicyOptions</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>cpuManagerPolicyOptions مجموعه‌ای از key=value است که امکان تنظیم گزینه‌های اضافی
برای تنظیم دقیق رفتار سیاست‌های cpu manager را فراهم می‌کند.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>cpuManagerReconcilePeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cpuManagerReconcilePeriod دورهٔ تطبیق (reconciliation) برای CPU Manager است.
پیش‌فرض: &quot;10s&quot;</p>
</td>
</tr>
<tr><td><code>memoryManagerPolicy</code><br/>
<code>string</code>
</td>
<td>
   <p>memoryManagerPolicy نام سیاستی است که memory manager باید استفاده کند.
نیازمند فعال بودن feature gate با نام MemoryManager است.
پیش‌فرض: &quot;none&quot;</p>
</td>
</tr>
<tr><td><code>topologyManagerPolicy</code><br/>
<code>string</code>
</td>
<td>
   <p>topologyManagerPolicy نام سیاست topology manager برای استفاده است.
مقادیر معتبر عبارت‌اند از:</p>
<ul>
<li><code>restricted</code>: kubelet فقط Podهایی را مجاز می‌داند که برای منابع درخواست‌شده
هم‌ترازی بهینهٔ نود NUMA دارند؛</li>
<li><code>best-effort</code>: kubelet Podهایی را که هم‌ترازی NUMA برای منابع CPU و دستگاه دارند
ترجیح می‌دهد؛</li>
<li><code>none</code>: kubelet هیچ اطلاعی از هم‌ترازی NUMA منابع CPU و دستگاه یک Pod ندارد.</li>
<li><code>single-numa-node</code>: kubelet فقط Podهایی را مجاز می‌داند که یک هم‌ترازی NUMA واحد
برای منابع CPU و دستگاه دارند.</li>
</ul>
<p>پیش‌فرض: &quot;none&quot;</p>
</td>
</tr>
<tr><td><code>topologyManagerScope</code><br/>
<code>string</code>
</td>
<td>
   <p>topologyManagerScope دامنهٔ تولید topology hint را نشان می‌دهد
که topology manager درخواست می‌کند و hint providerها تولید می‌کنند. مقادیر معتبر عبارت‌اند از:</p>
<ul>
<li><code>container</code>: سیاست توپولوژی به‌صورت جداگانه برای هر کانتینر اعمال می‌شود.</li>
<li><code>pod</code>: سیاست توپولوژی به‌صورت جداگانه برای هر Pod اعمال می‌شود.</li>
</ul>
<p>پیش‌فرض: &quot;container&quot;</p>
</td>
</tr>
<tr><td><code>topologyManagerPolicyOptions</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>TopologyManagerPolicyOptions مجموعه‌ای از key=value است که امکان تنظیم گزینه‌های اضافی
برای تنظیم دقیق رفتار سیاست‌های topology manager را فراهم می‌کند.
نیازمند فعال بودن هر دو feature gate با نام‌های &quot;TopologyManager&quot; و &quot;TopologyManagerPolicyOptions&quot; است.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>qosReserved</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>qosReserved مجموعه‌ای از جفت‌های نام منبع به درصد است که
حداقل درصدی از یک منبع را که برای استفادهٔ انحصاری
لایهٔ QoS از نوع guaranteed رزرو شده است مشخص می‌کند.
منابع پشتیبانی‌شده در حال حاضر: &quot;memory&quot;
نیازمند فعال بودن feature gate با نام QOSReserved است.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>runtimeRequestTimeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>runtimeRequestTimeout مهلت زمانی برای همهٔ درخواست‌های runtime به‌جز درخواست‌های
طولانی‌مدت - pull، logs، exec و attach است.
پیش‌فرض: &quot;2m&quot;</p>
</td>
</tr>
<tr><td><code>hairpinMode</code><br/>
<code>string</code>
</td>
<td>
   <p>hairpinMode مشخص می‌کند Kubelet چگونه باید bridge کانتینر را
برای بسته‌های hairpin پیکربندی کند.
تنظیم این پرچم به endpointهای یک Service اجازه می‌دهد در صورتی که بخواهند به Service خودشان دسترسی پیدا کنند،
بار را به خودشان توزیع کنند. مقادیر:</p>
<ul>
<li>&quot;promiscuous-bridge&quot;: bridge کانتینر را promiscuous می‌کند.</li>
<li>&quot;hairpin-veth&quot;:       پرچم hairpin را روی رابط‌های veth کانتینر تنظیم می‌کند.</li>
<li>&quot;none&quot;:               هیچ کاری انجام نمی‌دهد.</li>
</ul>
<p>به‌طور کلی، برای دستیابی به hairpin NAT باید <code>--hairpin-mode=hairpin-veth to</code> را تنظیم کرد،
زیرا promiscuous-bridge وجود یک bridge کانتینر با نام cbr0 را فرض می‌کند.
پیش‌فرض: &quot;promiscuous-bridge&quot;</p>
</td>
</tr>
<tr><td><code>maxPods</code><br/>
<code>int32</code>
</td>
<td>
   <p>maxPods بیشینهٔ تعداد Podهایی است که می‌توانند روی این Kubelet اجرا شوند.
مقدار باید عددی صحیح و نامنفی باشد.
پیش‌فرض: 110</p>
</td>
</tr>
<tr><td><code>podCIDR</code><br/>
<code>string</code>
</td>
<td>
   <p>podCIDR همان CIDR برای استفاده در نشانی‌های IP پاد است و فقط در حالت مستقل (standalone) استفاده می‌شود.
در حالت کلاستر، این مقدار از control plane به‌دست می‌آید.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>podPidsLimit</code><br/>
<code>int64</code>
</td>
<td>
   <p>podPidsLimit بیشینهٔ تعداد PIDها در هر Pod است.
پیش‌فرض: -1</p>
</td>
</tr>
<tr><td><code>resolvConf</code><br/>
<code>string</code>
</td>
<td>
   <p>resolvConf فایل پیکربندی resolver است که به‌عنوان مبنای
پیکربندی تفکیک DNS کانتینر استفاده می‌شود.
اگر روی رشتهٔ خالی تنظیم شود، پیش‌فرض را بازنویسی می‌کند و عملاً جست‌وجوهای DNS را غیرفعال می‌کند.
پیش‌فرض: &quot;/etc/resolv.conf&quot;</p>
</td>
</tr>
<tr><td><code>runOnce</code><br/>
<code>bool</code>
</td>
<td>
   <p>runOnce باعث می‌شود Kubelet یک بار API server را برای Podها بررسی کند،
آن‌ها را علاوه بر Podهای مشخص‌شده توسط فایل‌های Pod ایستا اجرا کند و خارج شود.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>cpuCFSQuota</code><br/>
<code>bool</code>
</td>
<td>
   <p>cpuCFSQuota اعمال سهمیهٔ CPU CFS را برای کانتینرهایی که
محدودیت CPU مشخص می‌کنند فعال می‌کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>cpuCFSQuotaPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cpuCFSQuotaPeriod مقدار دورهٔ سهمیهٔ CPU CFS یعنی <code>cpu.cfs_period_us</code> است.
مقدار باید بین 1 میلی‌ثانیه و 1 ثانیه (شامل هر دو مقدار) باشد.
نیازمند فعال بودن feature gate با نام CustomCPUCFSQuotaPeriod است.
پیش‌فرض: &quot;100ms&quot;</p>
</td>
</tr>
<tr><td><code>nodeStatusMaxImages</code><br/>
<code>int32</code>
</td>
<td>
   <p>nodeStatusMaxImages تعداد ایمیج‌های گزارش‌شده در Node.status.images را محدود می‌کند.
مقدار باید بزرگ‌تر از 2- باشد.
توجه: اگر 1- مشخص شود، هیچ سقفی اعمال نمی‌شود. اگر 0 مشخص شود، هیچ ایمیجی بازگردانده نمی‌شود.
پیش‌فرض: 50</p>
</td>
</tr>
<tr><td><code>maxOpenFiles</code><br/>
<code>int64</code>
</td>
<td>
   <p>maxOpenFiles تعداد فایل‌هایی است که فرایند Kubelet می‌تواند باز کند.
مقدار باید عددی نامنفی باشد.
پیش‌فرض: 1000000</p>
</td>
</tr>
<tr><td><code>contentType</code><br/>
<code>string</code>
</td>
<td>
   <p>contentType نوع محتوای درخواست‌های ارسالی به apiserver است.
پیش‌فرض: &quot;application/vnd.kubernetes.protobuf&quot;</p>
</td>
</tr>
<tr><td><code>kubeAPIQPS</code><br/>
<code>int32</code>
</td>
<td>
   <p>kubeAPIQPS مقدار QPS برای استفاده هنگام ارتباط با apiserver کوبرنتیز است.
پیش‌فرض: 50</p>
</td>
</tr>
<tr><td><code>kubeAPIBurst</code><br/>
<code>int32</code>
</td>
<td>
   <p>kubeAPIBurst مقدار burst مجاز هنگام ارتباط با API server کوبرنتیز است.
این فیلد نمی‌تواند عددی منفی باشد.
پیش‌فرض: 100</p>
</td>
</tr>
<tr><td><code>serializeImagePulls</code><br/>
<code>bool</code>
</td>
<td>
   <p>serializeImagePulls در صورت فعال بودن، به Kubelet می‌گوید ایمیج‌ها را یکی‌یکی
pull کند. توصیه می‌کنیم مقدار پیش‌فرض را روی نودهایی که
docker daemon با نسخهٔ &lt; 1.9 یا backend ذخیره‌سازی Aufs اجرا می‌کنند
<em>تغییر ندهید</em>.
جزئیات بیشتر در Issue #10959 آمده است.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>maxParallelImagePulls</code><br/>
<code>int32</code>
</td>
<td>
   <p>MaxParallelImagePulls بیشینهٔ تعداد pullهای هم‌زمان ایمیج را تعیین می‌کند.
اگر SerializeImagePulls برابر true باشد، این فیلد را نمی‌توان تنظیم کرد.
تنظیم آن روی nil به معنای نبود محدودیت است.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>evictionHard</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionHard نگاشتی از نام سیگنال‌ها به مقادیر است که آستانه‌های eviction سخت را تعریف می‌کند.
برای مثال: <code>{&quot;memory.available&quot;: &quot;300Mi&quot;}</code>.
برای غیرفعال‌سازی صریح، یک آستانهٔ 0% یا 100% را روی یک منبع دلخواه ارسال کنید.
پیش‌فرض:
memory.available:  &quot;100Mi&quot;
nodefs.available:  &quot;10%&quot;
nodefs.inodesFree: &quot;5%&quot;
imagefs.available: &quot;15%&quot;</p>
</td>
</tr>
<tr><td><code>evictionSoft</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionSoft نگاشتی از نام سیگنال‌ها به مقادیر است که آستانه‌های eviction نرم را تعریف می‌کند.
برای مثال: <code>{&quot;memory.available&quot;: &quot;300Mi&quot;}</code>.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>evictionSoftGracePeriod</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionSoftGracePeriod نگاشتی از نام سیگنال‌ها به مقادیر است که مهلت‌های
(grace period) هر سیگنال eviction نرم را تعریف می‌کند. برای مثال: <code>{&quot;memory.available&quot;: &quot;30s&quot;}</code>.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>evictionPressureTransitionPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>evictionPressureTransitionPeriod مدت زمانی است که kubelet باید صبر کند
پیش از آنکه از وضعیت فشار eviction خارج شود.
مدت 0s به مقدار پیش‌فرض 5m تبدیل می‌شود.
پیش‌فرض: &quot;5m&quot;</p>
</td>
</tr>
<tr><td><code>evictionMaxPodGracePeriod</code><br/>
<code>int32</code>
</td>
<td>
   <p>evictionMaxPodGracePeriod بیشینهٔ مهلت مجاز (به ثانیه) برای استفاده
هنگام خاتمه دادن به Podها در واکنش به رسیدن به یک آستانهٔ eviction نرم است. این مقدار
در عمل مقدار terminationGracePeriodSeconds مربوط به Pod را در طول evictionهای نرم محدود می‌کند.
پیش‌فرض: 0</p>
</td>
</tr>
<tr><td><code>evictionMinimumReclaim</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>evictionMinimumReclaim نگاشتی از نام سیگنال‌ها به مقادیر است که حداقل میزان بازیابی (reclaim) را تعریف می‌کند؛
این مقادیر حداقل مقدار یک منبع مشخص را توصیف می‌کنند که kubelet هنگام
انجام eviction یک Pod، در حالی که آن منبع تحت فشار است، بازیابی خواهد کرد.
برای مثال: <code>{&quot;imagefs.available&quot;: &quot;2Gi&quot;}</code>.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>mergeDefaultEvictionSettings</code><br/>
<code>bool</code>
</td>
<td>
   <p>mergeDefaultEvictionSettings نشان می‌دهد که پیش‌فرض‌های فیلدهای evictionHard، evictionSoft، evictionSoftGracePeriod و evictionMinimumReclaim
باید با مقادیر مشخص‌شده برای آن فیلدها در این پیکربندی ادغام شوند.
سیگنال‌های مشخص‌شده در این پیکربندی اولویت دارند.
سیگنال‌هایی که در این پیکربندی مشخص نشده‌اند، پیش‌فرض‌های خود را به ارث می‌برند.
اگر false باشد و هر سیگنالی در این پیکربندی مشخص شده باشد، سایر سیگنال‌هایی که
در این پیکربندی مشخص نشده‌اند روی 0 تنظیم می‌شوند.
این مورد برای ادغام فیلدهایی اعمال می‌شود که پیش‌فرض دارند، و در حال حاضر فقط evictionHard مقادیر پیش‌فرض دارد.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>podsPerCore</code><br/>
<code>int32</code>
</td>
<td>
   <p>podsPerCore بیشینهٔ تعداد Podها به‌ازای هر هسته است. نمی‌تواند از maxPods بیشتر شود.
مقدار باید عددی صحیح و نامنفی باشد.
اگر 0 باشد، محدودیتی برای تعداد Podها وجود ندارد.
پیش‌فرض: 0</p>
</td>
</tr>
<tr><td><code>enableControllerAttachDetach</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableControllerAttachDetach کنترل‌کنندهٔ Attach/Detach را فعال می‌کند تا
اتصال/جداسازی حجم‌های زمان‌بندی‌شده روی این نود را مدیریت کند، و
kubelet را از اجرای هرگونه عملیات attach/detach بازمی‌دارد.
توجه: اتصال/جداسازی حجم‌های CSI توسط kubelet پشتیبانی نمی‌شود،
بنابراین برای این مورد استفاده باید این گزینه true باشد.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>protectKernelDefaults</code><br/>
<code>bool</code>
</td>
<td>
   <p>protectKernelDefaults، در صورت true بودن، باعث می‌شود Kubelet در صورتی که پرچم‌های
کرنل مطابق انتظارش نباشند خطا بدهد. در غیر این صورت Kubelet تلاش می‌کند
پرچم‌های کرنل را طوری تغییر دهد که با انتظارش مطابقت داشته باشند.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>makeIPTablesUtilChains</code><br/>
<code>bool</code>
</td>
<td>
   <p>makeIPTablesUtilChains، در صورت true بودن، باعث می‌شود Kubelet زنجیرهٔ
KUBE-IPTABLES-HINT را در iptables ایجاد کند تا به‌عنوان یک راهنما برای سایر مؤلفه‌ها دربارهٔ
پیکربندی iptables روی سیستم عمل کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>iptablesMasqueradeBit</code><br/>
<code>int32</code>
</td>
<td>
   <p>iptablesMasqueradeBit پیش‌تر ایجاد زنجیرهٔ KUBE-MARK-MASQ
را کنترل می‌کرد.
منسوخ‌شده: دیگر هیچ تأثیری ندارد.
پیش‌فرض: 14</p>
</td>
</tr>
<tr><td><code>iptablesDropBit</code><br/>
<code>int32</code>
</td>
<td>
   <p>iptablesDropBit پیش‌تر ایجاد زنجیرهٔ KUBE-MARK-DROP را کنترل می‌کرد.
منسوخ‌شده: دیگر هیچ تأثیری ندارد.
پیش‌فرض: 15</p>
</td>
</tr>
<tr><td><code>featureGates</code><br/>
<code>map[string]bool</code>
</td>
<td>
   <p>featureGates نگاشتی از نام ویژگی‌ها به مقادیر bool است که ویژگی‌های آزمایشی را فعال یا غیرفعال می‌کند.
این فیلد مقادیر پیش‌فرض داخلی موجود در
&quot;k8s.io/kubernetes/pkg/features/kube_features.go&quot; را به‌صورت تکه‌تکه تغییر می‌دهد.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>failSwapOn</code><br/>
<code>bool</code>
</td>
<td>
   <p>failSwapOn به Kubelet می‌گوید در صورت فعال بودن swap روی نود، راه‌اندازی نشود.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>memorySwap</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-MemorySwapConfiguration"><code>MemorySwapConfiguration</code></a>
</td>
<td>
   <p>memorySwap حافظهٔ swap در دسترس برای بارهای کاری کانتینر را پیکربندی می‌کند.</p>
</td>
</tr>
<tr><td><code>containerLogMaxSize</code><br/>
<code>string</code>
</td>
<td>
   <p>containerLogMaxSize یک مقدار (quantity) است که بیشینهٔ اندازهٔ فایل لاگ کانتینر را
پیش از چرخش (rotate) تعیین می‌کند. برای مثال: &quot;5Mi&quot; یا &quot;256Ki&quot;.
پیش‌فرض: &quot;10Mi&quot;</p>
</td>
</tr>
<tr><td><code>containerLogMaxFiles</code><br/>
<code>int32</code>
</td>
<td>
   <p>containerLogMaxFiles بیشینهٔ تعداد فایل‌های لاگ کانتینر را مشخص می‌کند که می‌توانند
برای یک کانتینر وجود داشته باشند.
پیش‌فرض: 5</p>
</td>
</tr>
<tr><td><code>containerLogMaxWorkers</code><br/>
<code>int32</code>
</td>
<td>
   <p>ContainerLogMaxWorkers بیشینهٔ تعداد workerهای هم‌زمان را که برای انجام
عملیات چرخش لاگ ایجاد می‌شوند مشخص می‌کند. برای غیرفعال کردن
جریان‌های کاری چرخش هم‌زمان لاگ، این عدد را روی 1 تنظیم کنید.
پیش‌فرض: 1</p>
</td>
</tr>
<tr><td><code>containerLogMonitorInterval</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>ContainerLogMonitorInterval مدت زمانی را مشخص می‌کند که در هر بار، لاگ‌های کانتینر برای
انجام عملیات چرخش لاگ پایش می‌شوند. مقدار پیش‌فرض آن 10 * time.Seconds است، اما می‌توان آن را
بر اساس نرخ تولید لاگ و اندازه‌ای که باید چرخش بر اساس آن انجام شود، به مقداری کوچک‌تر سفارشی کرد.
پیش‌فرض: 10s</p>
</td>
</tr>
<tr><td><code>configMapAndSecretChangeDetectionStrategy</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ResourceChangeDetectionStrategy"><code>ResourceChangeDetectionStrategy</code></a>
</td>
<td>
   <p>configMapAndSecretChangeDetectionStrategy حالتی است که مدیرهای ConfigMap و Secret
در آن اجرا می‌شوند. مقادیر معتبر عبارت‌اند از:</p>
<ul>
<li><code>Get</code>: kubelet آبجکت‌های لازم را مستقیماً از API server دریافت می‌کند؛</li>
<li><code>Cache</code>: kubelet برای آبجکت‌های دریافت‌شده از API server از cache مبتنی بر TTL استفاده می‌کند؛</li>
<li><code>Watch</code>: kubelet از watchها برای مشاهدهٔ تغییرات آبجکت‌هایی که به آن‌ها علاقه‌مند است استفاده می‌کند.</li>
</ul>
<p>پیش‌فرض: &quot;Watch&quot;</p>
</td>
</tr>
<tr><td><code>systemReserved</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>systemReserved مجموعه‌ای از جفت‌های ResourceName=ResourceQuantity (مثلاً cpu=200m,memory=150G) است
که منابع رزروشده برای مؤلفه‌های غیرکوبرنتیز را توصیف می‌کنند.
در حال حاضر فقط cpu و memory پشتیبانی می‌شوند.
برای جزئیات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources مراجعه کنید.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>kubeReserved</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>kubeReserved مجموعه‌ای از جفت‌های ResourceName=ResourceQuantity (مثلاً cpu=200m,memory=150G) است
که منابع رزروشده برای مؤلفه‌های سیستمی کوبرنتیز را توصیف می‌کنند.
در حال حاضر cpu، memory و ذخیره‌سازی محلی برای فایل‌سیستم ریشه پشتیبانی می‌شوند.
برای جزئیات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources
مراجعه کنید.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>reservedSystemCPUs</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>گزینهٔ reservedSystemCPUs فهرست CPUهای رزروشده برای threadهای سیستمی سطح میزبان
و threadهای مرتبط با کوبرنتیز را مشخص می‌کند. این گزینه به‌جای فهرست «پویا» که توسط systemReserved و kubeReserved ایجاد می‌شود،
یک فهرست CPU «ایستا» فراهم می‌کند.
این گزینه از systemReservedCgroup یا kubeReservedCgroup پشتیبانی نمی‌کند.</p>
</td>
</tr>
<tr><td><code>showHiddenMetricsForVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>showHiddenMetricsForVersion نسخهٔ قبلی است که می‌خواهید معیارهای پنهان آن را نمایش دهید.
فقط نسخهٔ minor قبلی معنادار است و مقادیر دیگر مجاز نخواهند بود.
قالب آن <code>&lt;major&gt;.&lt;minor&gt;</code> است، مثلاً: <code>1.16</code>.
هدف از این قالب آن است که مطمئن شوید فرصت دارید متوجه شوید
آیا نسخهٔ بعدی معیارهای بیشتری را پنهان می‌کند، تا اینکه
هنگام حذف دائمی آن‌ها در نسخهٔ پس از آن غافلگیر شوید.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>systemReservedCgroup</code><br/>
<code>string</code>
</td>
<td>
   <p>systemReservedCgroup به kubelet کمک می‌کند نام مطلق CGroup سطح بالا را که برای اعمال
رزرو منابع محاسباتی <code>systemReserved</code> برای daemonهای سیستم‌عامل استفاده می‌شود شناسایی کند.
برای اطلاعات بیشتر به مستند <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">Node Allocatable</a>
مراجعه کنید.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>kubeReservedCgroup</code><br/>
<code>string</code>
</td>
<td>
   <p>kubeReservedCgroup به kubelet کمک می‌کند نام مطلق CGroup سطح بالا را که برای اعمال
رزرو منابع محاسباتی <code>KubeReserved</code> برای daemonهای سیستمی نود کوبرنتیز استفاده می‌شود شناسایی کند.
برای اطلاعات بیشتر به مستند <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">Node Allocatable</a>
مراجعه کنید.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>enforceNodeAllocatable</code><br/>
<code>[]string</code>
</td>
<td>
   <p>این پرچم اعمال‌های مختلف Node Allocatable را که Kubelet باید انجام دهد مشخص می‌کند.
این پرچم فهرستی از گزینه‌ها را می‌پذیرد. گزینه‌های قابل قبول عبارت‌اند از <code>none</code>، <code>pods</code>،
<code>system-reserved</code>، <code>system-reserved-compressible</code>، <code>kube-reserved</code> و <code>kube-reserved-compressible</code>.
اگر <code>none</code> مشخص شود، هیچ گزینهٔ دیگری نباید مشخص شود.
هنگامی که گزینهٔ <code>system-reserved</code> در فهرست باشد، باید systemReservedCgroup مشخص شود.
هنگامی که گزینهٔ <code>kube-reserved</code> در فهرست باشد، باید kubeReservedCgroup مشخص شود.
اگر یک گزینهٔ <code>compressible</code> مشخص شود، گزینهٔ غیرقابل‌فشرده‌سازی متناظر نباید مشخص شود.
این فیلد فقط زمانی پشتیبانی می‌شود که <code>cgroupsPerQOS</code> روی true تنظیم شده باشد.
برای اطلاعات بیشتر به <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">Node Allocatable</a>
مراجعه کنید.
پیش‌فرض: [&quot;pods&quot;]</p>
</td>
</tr>
<tr><td><code>allowedUnsafeSysctls</code><br/>
<code>[]string</code>
</td>
<td>
   <p>یک فهرست مجاز (whitelist) جداشده با کاما از sysctlهای ناامن یا الگوهای sysctl (که به <code>*</code> ختم می‌شوند).
گروه‌های sysctl ناامن عبارت‌اند از <code>kernel.shm*</code>، <code>kernel.msg*</code>، <code>kernel.sem</code>، <code>fs.mqueue.*</code>
و <code>net.*</code>. برای مثال: &quot;<code>kernel.msg*,net.ipv4.route.min_pmtu</code>&quot;
پیش‌فرض: []</p>
</td>
</tr>
<tr><td><code>defaultPodSysctls</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>DefaultPodSysctls مجموعه‌ای از sysctlهای پیش‌فرض است که روی همهٔ Podها اعمال می‌شود.
می‌توان آن را با sysctlهای تنظیم‌شده در pod spec.securityContext.sysctls بازنویسی کرد.
گروه‌های دارای namespace پشتیبانی‌شده: <code>kernel.shm*</code>، <code>kernel.msg*</code>، <code>kernel.sem</code>، <code>fs.mqueue.*</code>، <code>net.*</code>، <code>kernel.domainname</code> و <code>user.*</code>.
برای مثال: {&quot;net.ipv4.ip_forward&quot;: &quot;1&quot;, &quot;kernel.shmall&quot;: &quot;1048576&quot;}</p>
</td>
</tr>
<tr><td><code>volumePluginDir</code><br/>
<code>string</code>
</td>
<td>
   <p>volumePluginDir مسیر کامل دایرکتوری است که در آن به‌دنبال افزونه‌های
حجم شخص ثالث اضافی جست‌وجو می‌شود.
پیش‌فرض: &quot;/usr/libexec/kubernetes/kubelet-plugins/volume/exec/&quot;</p>
</td>
</tr>
<tr><td><code>providerID</code><br/>
<code>string</code>
</td>
<td>
   <p>providerID، در صورت تنظیم، شناسهٔ یکتای نمونه‌ای را تعیین می‌کند که یک
provider خارجی (مثلاً cloudprovider) می‌تواند از آن برای شناسایی یک نود مشخص استفاده کند.
پیش‌فرض: &quot;&quot;</p>
</td>
</tr>
<tr><td><code>kernelMemcgNotification</code><br/>
<code>bool</code>
</td>
<td>
   <p>kernelMemcgNotification، در صورت تنظیم، به kubelet دستور می‌دهد برای تعیین اینکه آیا آستانه‌های eviction حافظه
فراتر رفته‌اند، به‌جای polling با اعلان memcg کرنل یکپارچه شود.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>logging</code> <B>[الزامی]</B><br/>
<a href="#LoggingConfiguration"><code>LoggingConfiguration</code></a>
</td>
<td>
   <p>logging گزینه‌های لاگ‌گیری را مشخص می‌کند.
برای اطلاعات بیشتر به <a href="https://github.com/kubernetes/component-base/blob/master/logs/options.go">Logs Options</a>
مراجعه کنید.
پیش‌فرض:
Format: text</p>
</td>
</tr>
<tr><td><code>enableSystemLogHandler</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableSystemLogHandler لاگ‌های سیستم را از طریق رابط وب در host:port/logs/ فعال می‌کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>enableSystemLogQuery</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableSystemLogQuery قابلیت پرس‌وجوی لاگ نود را روی نقطهٔ انتهایی /logs فعال می‌کند.
برای کارکرد این قابلیت، EnableSystemLogHandler نیز باید فعال باشد.
فعال کردن این قابلیت پیامدهای امنیتی دارد. توصیه می‌شود آن را فقط در صورت نیاز و برای اهداف اشکال‌زدایی
فعال کرده و در غیر این صورت غیرفعال نگه دارید.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>shutdownGracePeriod مجموع مدتی را مشخص می‌کند که نود باید خاموش شدن را به تأخیر بیندازد،
و نیز مجموع مهلت خاتمهٔ Podها در طول خاموش شدن نود را.
پیش‌فرض: &quot;0s&quot;</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriodCriticalPods</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>shutdownGracePeriodCriticalPods مدت زمانی را مشخص می‌کند که برای خاتمه دادن به Podهای
حیاتی در طول خاموش شدن نود استفاده می‌شود. این مقدار باید کمتر از shutdownGracePeriod باشد.
برای مثال، اگر shutdownGracePeriod=30s و shutdownGracePeriodCriticalPods=10s باشد،
در طول خاموش شدن نود، 20 ثانیهٔ اول برای خاتمهٔ مؤدبانهٔ Podهای عادی رزرو می‌شود و 10 ثانیهٔ آخر
برای خاتمه دادن به Podهای حیاتی رزرو می‌شود.
پیش‌فرض: &quot;0s&quot;</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriodByPodPriority</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ShutdownGracePeriodByPodPriority"><code>[]ShutdownGracePeriodByPodPriority</code></a>
</td>
<td>
   <p>shutdownGracePeriodByPodPriority مهلت خاموش شدن Podها را بر اساس
مقدار priority class مرتبط با آن‌ها مشخص می‌کند.
هنگامی که درخواست خاموش شدن دریافت می‌شود، Kubelet خاموش شدن همهٔ Podهای در حال اجرا روی نود را
با مهلتی که به اولویت Pod بستگی دارد آغاز می‌کند
و سپس منتظر می‌ماند همهٔ Podها خارج شوند.
هر ورودی در آرایه، زمان خاموش شدن مؤدبانهٔ یک Pod را نشان می‌دهد که مقدار priority class آن
در بازهٔ بین آن مقدار و ورودی بالاتر بعدی در فهرست قرار دارد، در زمانی که نود در حال خاموش شدن است.
برای مثال، برای اینکه به Podهای حیاتی 10 ثانیه، به Podهای با priority&gt;=10000 مدت 20 ثانیه و به
همهٔ Podهای باقی‌مانده 30 ثانیه برای خاموش شدن مهلت داده شود:</p>
<p>shutdownGracePeriodByPodPriority:</p>
<ul>
<li>priority: 2000000000
shutdownGracePeriodSeconds: 10</li>
<li>priority: 10000
shutdownGracePeriodSeconds: 20</li>
<li>priority: 0
shutdownGracePeriodSeconds: 30</li>
</ul>
<p>زمانی که Kubelet پیش از خروج منتظر می‌ماند حداکثر برابر بیشینهٔ همهٔ
مقادیر shutdownGracePeriodSeconds برای هر بازهٔ priority class حاضر روی نود خواهد بود.
هنگامی که همهٔ Podها خارج شدند یا به مهلت خود رسیدند، Kubelet قفل مهار خاموش شدن
(shutdown inhibit lock) را آزاد می‌کند.
نیازمند فعال بودن feature gate با نام GracefulNodeShutdown است.
اگر ShutdownGracePeriod یا ShutdownGracePeriodCriticalPods تنظیم شده باشد، این پیکربندی باید خالی باشد.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>crashLoopBackOff</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-CrashLoopBackOffConfig"><code>CrashLoopBackOffConfig</code></a>
</td>
<td>
   <p>CrashLoopBackOff شامل پیکربندی برای تغییر پارامترهای سطح نود در
رفتار راه‌اندازی مجدد کانتینر است.</p>
</td>
</tr>
<tr><td><code>reservedMemory</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-MemoryReservation"><code>[]MemoryReservation</code></a>
</td>
<td>
   <p>reservedMemory فهرستی جداشده با کاما از رزروهای حافظه برای نودهای NUMA را مشخص می‌کند.
این پارامتر فقط در بستر قابلیت memory manager معنا دارد.
memory manager حافظهٔ رزروشده را برای بارهای کاری کانتینر تخصیص نخواهد داد.
برای مثال، اگر یک NUMA0 با 10Gi حافظه دارید و reservedMemory
برای رزرو 1Gi حافظه در NUMA0 مشخص شده باشد، memory manager فرض می‌کند
که فقط 9Gi برای تخصیص در دسترس است.
می‌توانید تعداد و انواع حافظهٔ متفاوتی از نودهای NUMA را مشخص کنید.
می‌توانید این پارامتر را به‌کلی حذف کنید، اما باید توجه داشته باشید که مقدار
حافظهٔ رزروشده از همهٔ نودهای NUMA باید برابر با مقدار حافظه‌ای باشد که
توسط <a href="https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable">node allocatable</a> مشخص شده است.
اگر دست‌کم یک پارامتر node allocatable مقداری غیرصفر داشته باشد، لازم است
دست‌کم یک نود NUMA را مشخص کنید.
همچنین از مشخص کردن موارد زیر خودداری کنید:</p>
<ol>
<li>موارد تکراری، یعنی همان نود NUMA و همان نوع حافظه، اما با مقداری متفاوت.</li>
<li>محدودیت صفر برای هر نوع حافظه.</li>
<li>شناسه‌های نودهای NUMA که روی ماشین وجود ندارند.</li>
<li>انواع حافظه‌ای به‌جز memory و hugepages-<!-- raw HTML omitted --></li>
</ol>
<p>پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>enableProfilingHandler</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableProfilingHandler پروفایل‌گیری را از طریق رابط وب در host:port/debug/pprof/ فعال می‌کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>enableDebugFlagsHandler</code><br/>
<code>bool</code>
</td>
<td>
   <p>enableDebugFlagsHandler نقطهٔ انتهایی flags را از طریق رابط وب در host:port/debug/flags/v فعال می‌کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>seccompDefault</code><br/>
<code>bool</code>
</td>
<td>
   <p>SeccompDefault استفاده از <code>RuntimeDefault</code> را به‌عنوان پروفایل seccomp پیش‌فرض برای همهٔ بارهای کاری فعال می‌کند.
پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>memoryThrottlingFactor</code><br/>
<code>float64</code>
</td>
<td>
   <p>MemoryThrottlingFactor ضریبی را مشخص می‌کند که در محدودیت حافظه یا حافظهٔ قابل تخصیص نود ضرب می‌شود
تا هنگام تنظیم مقدار memory.high در cgroupv2 برای اعمال MemoryQoS به کار رود.
کاهش این ضریب، محدودیت high پایین‌تری برای cgroupهای کانتینر تعیین می‌کند و فشار بازیابی (reclaim) سنگین‌تری وارد می‌کند،
در حالی که افزایش آن فشار بازیابی کمتری وارد می‌کند. اگر nil باشد، memory.high تنظیم نمی‌شود.
برای جزئیات بیشتر به https://kep.k8s.io/2570 مراجعه کنید.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>memoryReservationPolicy</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-MemoryReservationPolicy"><code>MemoryReservationPolicy</code></a>
</td>
<td>
   <p>MemoryReservationPolicy نحوهٔ اعمال محافظت حافظهٔ cgroup v2 توسط kubelet را کنترل می‌کند.
&quot;None&quot; (پیش‌فرض): kubelet مقدار memory.min را برای کانتینرها و Podها تنظیم نمی‌کند،
و تضمین می‌کند که هیچ حافظهٔ سختی توسط کرنل قفل نشود.
&quot;TieredReservation&quot;: kubelet بر اساس درخواست‌های حافظه، memory.min را برای Podهای Guaranteed و memory.low را برای Podهای Burstable در cgroup v2 تنظیم می‌کند.
حافظهٔ Guaranteed هرگز توسط کرنل بازیابی نمی‌شود؛ حافظهٔ Burstable ترجیحاً حفظ می‌شود اما ممکن است تحت فشار شدید بازیابی شود.
برای جزئیات بیشتر به https://kep.k8s.io/2570 مراجعه کنید.
پیش‌فرض: None</p>
</td>
</tr>
<tr><td><code>registerWithTaints</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#taint-v1-core"><code>[]core/v1.Taint</code></a>
</td>
<td>
   <p>registerWithTaints آرایه‌ای از taintها است که هنگام ثبت خود kubelet به آبجکت نود اضافه می‌شوند.
این فیلد فقط زمانی اثر دارد که registerNode برابر true باشد
و هنگام ثبت اولیهٔ نود.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>registerNode</code><br/>
<code>bool</code>
</td>
<td>
   <p>registerNode ثبت خودکار نزد apiserver را فعال می‌کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>tracing</code><br/>
<a href="#TracingConfiguration"><code>TracingConfiguration</code></a>
</td>
<td>
   <p>Tracing پیکربندی نسخه‌بندی‌شده برای کلاینت‌های ردیابی OpenTelemetry را مشخص می‌کند.
برای جزئیات بیشتر به https://kep.k8s.io/2832 مراجعه کنید.
پیش‌فرض: nil</p>
</td>
</tr>
<tr><td><code>localStorageCapacityIsolation</code><br/>
<code>bool</code>
</td>
<td>
   <p>LocalStorageCapacityIsolation قابلیت ایزوله‌سازی ذخیره‌سازی موقت محلی را فعال می‌کند. تنظیم پیش‌فرض true است.
این قابلیت به کاربران اجازه می‌دهد برای ذخیره‌سازی موقت کانتینر request/limit تعیین کنند و آن را به روشی مشابه
cpu و memory مدیریت کنند. همچنین امکان تنظیم sizeLimit را برای حجم emptyDir فراهم می‌کند که در صورت
فراتر رفتن میزان استفاده از دیسک توسط حجم از این محدودیت، eviction Pod را فعال می‌کند.
این قابلیت به توانایی تشخیص صحیح میزان استفاده از دیسک فایل‌سیستم ریشه وابسته است. برای برخی سیستم‌ها،
مانند kind rootless، اگر این توانایی پشتیبانی نشود، ویژگی LocalStorageCapacityIsolation باید
غیرفعال شود. پس از غیرفعال شدن، کاربر نباید برای ذخیره‌سازی موقت کانتینر request/limit یا برای emptyDir مقدار sizeLimit تنظیم کند.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>containerRuntimeEndpoint</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>ContainerRuntimeEndpoint نقطهٔ انتهایی container runtime است.
Unix Domain Socketها در لینوکس پشتیبانی می‌شوند، در حالی که نقاط انتهایی npipe و tcp در ویندوز پشتیبانی می‌شوند.
مثال‌ها: 'unix:///path/to/runtime.sock'، 'npipe:////./pipe/runtime'</p>
</td>
</tr>
<tr><td><code>imageServiceEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>ImageServiceEndpoint نقطهٔ انتهایی سرویس ایمیج کانتینر است.
Unix Domain Socketها در لینوکس پشتیبانی می‌شوند، در حالی که نقاط انتهایی npipe و tcp در ویندوز پشتیبانی می‌شوند.
مثال‌ها: 'unix:///path/to/runtime.sock'، 'npipe:////./pipe/runtime'.
اگر مشخص نشود، مقدار موجود در containerRuntimeEndpoint استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>failCgroupV1</code><br/>
<code>bool</code>
</td>
<td>
   <p>FailCgroupV1 از راه‌اندازی شدن kubelet روی میزبان‌هایی که
از cgroup v1 استفاده می‌کنند جلوگیری می‌کند. به‌طور پیش‌فرض، این مقدار روی 'true' تنظیم شده است، یعنی
kubelet روی میزبان‌های cgroup v1 راه‌اندازی نخواهد شد، مگر اینکه این
گزینه به‌صراحت غیرفعال شود.
پیش‌فرض: true</p>
</td>
</tr>
<tr><td><code>userNamespaces</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-UserNamespaces"><code>UserNamespaces</code></a>
</td>
<td>
   <p>UserNamespaces شامل پیکربندی‌های User Namespace است.</p>
</td>
</tr>
</tbody>
</table>

## `SerializedNodeConfigSource`     {#kubelet-config-k8s-io-v1beta1-SerializedNodeConfigSource}
    


<p>SerializedNodeConfigSource امکان سریال‌سازی v1.NodeConfigSource را فراهم می‌کند.
این نوع به‌صورت داخلی توسط Kubelet برای ردیابی پیکربندی‌های پویای checkpoint‌شده استفاده می‌شود.
این نوع در گروه API با نام kubeletconfig وجود دارد، زیرا به‌عنوان یک ورودی نسخه‌دار برای Kubelet طبقه‌بندی می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubelet.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>SerializedNodeConfigSource</code></td></tr>
    
  
<tr><td><code>source</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#nodeconfigsource-v1-core"><code>core/v1.NodeConfigSource</code></a>
</td>
<td>
   <p>source منبعی است که در حال سریال‌سازی آن هستیم.</p>
</td>
</tr>
</tbody>
</table>

## `CrashLoopBackOffConfig`     {#kubelet-config-k8s-io-v1beta1-CrashLoopBackOffConfig}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>maxContainerRestartPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>maxContainerRestartPeriod حداکثر مدتی است که تأخیر backoff برای راه‌اندازی مجدد کانتینرها
می‌تواند تا آن مقدار افزایش یابد؛ حداقل ۱ ثانیه و حداکثر ۳۰۰ ثانیه. در صورت تنظیم نشدن،
مقدار پیش‌فرض برابر با حداکثر داخلی crashloopbackoff (۳۰۰ ثانیه) است.</p>
</td>
</tr>
</tbody>
</table>

## `CredentialProvider`     {#kubelet-config-k8s-io-v1beta1-CredentialProvider}
    

**Appears in:**

- [CredentialProviderConfig](#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig)


<p>CredentialProvider یک افزونه exec را نشان می‌دهد که kubelet آن را فراخوانی می‌کند. این افزونه تنها
زمانی فراخوانی می‌شود که ایمیجی که در حال pull شدن است با ایمیج‌هایی که افزونه مدیریت می‌کند مطابقت داشته باشد (به matchImages مراجعه کنید).</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام الزامی ارائه‌دهنده اعتبارنامه (credential provider) است. این نام باید با نام
فایل اجرایی ارائه‌دهنده، آن‌گونه که kubelet می‌بیند، مطابقت داشته باشد. فایل اجرایی باید در
پوشه bin مربوط به kubelet باشد (که با فلگ --image-credential-provider-bin-dir تنظیم می‌شود).
این نام باید در میان همه ارائه‌دهندگان یکتا باشد.</p>
</td>
</tr>
<tr><td><code>matchImages</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>matchImages فهرستی الزامی از رشته‌هاست که برای تطبیق با ایمیج‌ها به‌کار می‌رود تا
مشخص شود آیا این ارائه‌دهنده باید فراخوانی شود یا خیر. اگر یکی از رشته‌ها با ایمیج
درخواست‌شده از سوی kubelet مطابقت داشته باشد، افزونه فراخوانی می‌شود و فرصت می‌یابد
اعتبارنامه‌ها را ارائه دهد. انتظار می‌رود ایمیج‌ها شامل دامنه رجیستری
و مسیر URL باشند.</p>
<p>هر مدخل در matchImages یک الگو است که می‌تواند به‌صورت اختیاری شامل پورت و مسیر باشد.
در دامنه می‌توان از glob استفاده کرد، اما در پورت یا مسیر نمی‌توان. globها به‌صورت
زیردامنه مانند '<em>.k8s.io' یا 'k8s.</em>.io' و دامنه‌های سطح بالا مانند 'k8s.<em>' پشتیبانی می‌شوند.
تطبیق زیردامنه‌های جزئی مانند 'app</em>.k8s.io' نیز پشتیبانی می‌شود. هر glob فقط می‌تواند با
یک بخش زیردامنه مطابقت داشته باشد، بنابراین *.io با *.k8s.io مطابقت ندارد.</p>
<p>زمانی بین یک ایمیج و یک matchImage تطابق وجود دارد که همه موارد زیر برقرار باشند:</p>
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
<tr><td><code>defaultCacheDuration</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>defaultCacheDuration مدت‌زمان پیش‌فرضی است که افزونه اعتبارنامه‌ها را در حافظه نگه می‌دارد
(cache) در صورتی که مدت‌زمان cache در پاسخ افزونه ارائه نشده باشد. این فیلد الزامی است.</p>
</td>
</tr>
<tr><td><code>apiVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نسخه ورودی الزامی برای CredentialProviderRequest مربوط به exec. CredentialProviderResponse بازگردانده‌شده
باید از همان نسخه کدگذاری ورودی استفاده کند. مقادیر پشتیبانی‌شده فعلی عبارت‌اند از:</p>
<ul>
<li>credentialprovider.kubelet.k8s.io/v1beta1</li>
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
<a href="#kubelet-config-k8s-io-v1beta1-ExecEnvVar"><code>[]ExecEnvVar</code></a>
</td>
<td>
   <p>Env متغیرهای محیطی اضافی را تعریف می‌کند که در اختیار فرایند قرار می‌گیرند. این
متغیرها با محیط میزبان و همچنین متغیرهایی که client-go برای
ارسال آرگومان به افزونه استفاده می‌کند، ادغام (union) می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `ExecEnvVar`     {#kubelet-config-k8s-io-v1beta1-ExecEnvVar}
    

**Appears in:**

- [CredentialProvider](#kubelet-config-k8s-io-v1beta1-CredentialProvider)


<p>ExecEnvVar برای تنظیم متغیرهای محیطی هنگام اجرای افزونه اعتبارنامه مبتنی بر exec
استفاده می‌شود.</p>


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

## `ImagePullCredentials`     {#kubelet-config-k8s-io-v1beta1-ImagePullCredentials}
    

**Appears in:**

- [ImagePulledRecord](#kubelet-config-k8s-io-v1beta1-ImagePulledRecord)


<p>ImagePullCredentials اعتبارنامه‌هایی را توصیف می‌کند که می‌توان از آن‌ها برای pull کردن یک ایمیج استفاده کرد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesSecrets</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ImagePullSecret"><code>[]ImagePullSecret</code></a>
</td>
<td>
   <p>KubernetesSecretCoordinates فهرستی از مختصات همه Secretهای کوبرنتیز است
که برای pull کردن ایمیج استفاده شده‌اند.</p>
</td>
</tr>
<tr><td><code>kubernetesServiceAccounts</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-ImagePullServiceAccount"><code>[]ImagePullServiceAccount</code></a>
</td>
<td>
   <p>KubernetesServiceAccounts فهرستی از مختصات همه حساب‌های سرویس (service account) کوبرنتیز
است که برای pull کردن ایمیج استفاده شده‌اند.</p>
</td>
</tr>
<tr><td><code>nodePodsAccessible</code><br/>
<code>bool</code>
</td>
<td>
   <p>NodePodsAccessible پرچمی است که نشان می‌دهد اعتبارنامه‌های pull برای همه Podهای روی نود
قابل دسترس هستند، یا اینکه برای pull به هیچ اعتبارنامه‌ای نیاز نیست.</p>
<p>اگر مقدار آن true باشد، با فیلد <code>kubernetesSecrets</code> متقابلاً ناسازگار است (mutually exclusive).</p>
</td>
</tr>
</tbody>
</table>

## `ImagePullCredentialsVerificationPolicy`     {#kubelet-config-k8s-io-v1beta1-ImagePullCredentialsVerificationPolicy}
    
(Alias of `string`)

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>ImagePullCredentialsVerificationPolicy یک enum برای سیاستی است که زمانی اعمال می‌شود
که یک Pod ایمیجی را درخواست می‌کند که از قبل روی سیستم وجود دارد.</p>




## `ImagePullSecret`     {#kubelet-config-k8s-io-v1beta1-ImagePullSecret}
    

**Appears in:**

- [ImagePullCredentials](#kubelet-config-k8s-io-v1beta1-ImagePullCredentials)


<p>ImagePullSecret نمایشی از مختصات یک آبجکت Secret کوبرنتیز است، همراه با
یک هش اعتبارنامه از اعتبارنامه‌های pull که این آبجکت در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>uid</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>credentialHash</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>CredentialHash یک مقدار SHA-256 است که با هش کردن محتوای اعتبارنامه‌های pull ایمیج
در Secret مشخص‌شده با مختصات UID/Namespace/Name به دست می‌آید.</p>
</td>
</tr>
</tbody>
</table>

## `ImagePullServiceAccount`     {#kubelet-config-k8s-io-v1beta1-ImagePullServiceAccount}
    

**Appears in:**

- [ImagePullCredentials](#kubelet-config-k8s-io-v1beta1-ImagePullCredentials)


<p>ImagePullServiceAccount نمایشی از مختصات یک آبجکت حساب سرویس (service account) کوبرنتیز است
که kubelet برای آن توکن حساب سرویس را برای دریافت اعتبارنامه‌های pull ایمیج به افزونه ارائه‌دهنده اعتبارنامه ارسال کرده است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>uid</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `KubeletAnonymousAuthentication`     {#kubelet-config-k8s-io-v1beta1-KubeletAnonymousAuthentication}
    

**Appears in:**

- [KubeletAuthentication](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>enabled</code><br/>
<code>bool</code>
</td>
<td>
   <p>enabled درخواست‌های ناشناس (anonymous) به سرور kubelet را مجاز می‌کند.
درخواست‌هایی که توسط روش احراز هویت دیگری رد نشوند، به‌عنوان
درخواست ناشناس در نظر گرفته می‌شوند.
درخواست‌های ناشناس نام کاربری <code>system:anonymous</code> و نام گروه
<code>system:unauthenticated</code> دارند.</p>
</td>
</tr>
</tbody>
</table>

## `KubeletAuthentication`     {#kubelet-config-k8s-io-v1beta1-KubeletAuthentication}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>x509</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletX509Authentication"><code>KubeletX509Authentication</code></a>
</td>
<td>
   <p>x509 شامل تنظیمات مربوط به احراز هویت با گواهی کلاینت x509 است.</p>
</td>
</tr>
<tr><td><code>webhook</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletWebhookAuthentication"><code>KubeletWebhookAuthentication</code></a>
</td>
<td>
   <p>webhook شامل تنظیمات مربوط به احراز هویت با توکن bearer از طریق webhook است.</p>
</td>
</tr>
<tr><td><code>anonymous</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletAnonymousAuthentication"><code>KubeletAnonymousAuthentication</code></a>
</td>
<td>
   <p>anonymous شامل تنظیمات مربوط به احراز هویت ناشناس است.</p>
</td>
</tr>
</tbody>
</table>

## `KubeletAuthorization`     {#kubelet-config-k8s-io-v1beta1-KubeletAuthorization}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>mode</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletAuthorizationMode"><code>KubeletAuthorizationMode</code></a>
</td>
<td>
   <p>mode حالت مجوزدهی (authorization) است که بر درخواست‌های ارسالی به سرور kubelet اعمال می‌شود.
مقادیر معتبر <code>AlwaysAllow</code> و <code>Webhook</code> هستند.
حالت Webhook برای تعیین مجوز از API مربوط به SubjectAccessReview استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>webhook</code><br/>
<a href="#kubelet-config-k8s-io-v1beta1-KubeletWebhookAuthorization"><code>KubeletWebhookAuthorization</code></a>
</td>
<td>
   <p>webhook شامل تنظیمات مربوط به مجوزدهی Webhook است.</p>
</td>
</tr>
</tbody>
</table>

## `KubeletAuthorizationMode`     {#kubelet-config-k8s-io-v1beta1-KubeletAuthorizationMode}
    
(Alias of `string`)

**Appears in:**

- [KubeletAuthorization](#kubelet-config-k8s-io-v1beta1-KubeletAuthorization)





## `KubeletWebhookAuthentication`     {#kubelet-config-k8s-io-v1beta1-KubeletWebhookAuthentication}
    

**Appears in:**

- [KubeletAuthentication](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>enabled</code><br/>
<code>bool</code>
</td>
<td>
   <p>enabled احراز هویت با توکن bearer را که توسط API مربوط به
tokenreviews.authentication.k8s.io پشتیبانی می‌شود، فعال می‌کند.</p>
</td>
</tr>
<tr><td><code>cacheTTL</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cacheTTL ذخیره موقت (cache) نتایج احراز هویت را فعال می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `KubeletWebhookAuthorization`     {#kubelet-config-k8s-io-v1beta1-KubeletWebhookAuthorization}
    

**Appears in:**

- [KubeletAuthorization](#kubelet-config-k8s-io-v1beta1-KubeletAuthorization)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>cacheAuthorizedTTL</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cacheAuthorizedTTL مدت‌زمان ذخیره موقت (cache) پاسخ‌های «مجاز» (authorized) از
مجوزدهنده webhook است.</p>
</td>
</tr>
<tr><td><code>cacheUnauthorizedTTL</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>cacheUnauthorizedTTL مدت‌زمان ذخیره موقت (cache) پاسخ‌های «غیرمجاز» (unauthorized) از
مجوزدهنده webhook است.</p>
</td>
</tr>
</tbody>
</table>

## `KubeletX509Authentication`     {#kubelet-config-k8s-io-v1beta1-KubeletX509Authentication}
    

**Appears in:**

- [KubeletAuthentication](#kubelet-config-k8s-io-v1beta1-KubeletAuthentication)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>clientCAFile</code><br/>
<code>string</code>
</td>
<td>
   <p>clientCAFile مسیر یک بسته گواهی با کدگذاری PEM است. در صورت تنظیم، هر درخواستی
که گواهی کلاینتی ارائه دهد که توسط یکی از مراجع موجود در این بسته امضا شده باشد،
با نام کاربری متناظر با CommonName
و گروه‌های متناظر با Organization در گواهی کلاینت احراز هویت می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `MemoryReservation`     {#kubelet-config-k8s-io-v1beta1-MemoryReservation}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>MemoryReservation رزرو حافظه از انواع مختلف را برای هر نود NUMA مشخص می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>numaNode</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>limits</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#resourcelist-v1-core"><code>core/v1.ResourceList</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `MemoryReservationPolicy`     {#kubelet-config-k8s-io-v1beta1-MemoryReservationPolicy}
    
(Alias of `string`)

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>MemoryReservationPolicy تعریف می‌کند که kubelet چگونه حفاظت حافظه در cgroup v2 را اعمال کند.</p>




## `MemorySwapConfiguration`     {#kubelet-config-k8s-io-v1beta1-MemorySwapConfiguration}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)



<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>swapBehavior</code><br/>
<code>string</code>
</td>
<td>
   <p>swapBehavior میزان حافظه swap در دسترس بارهای کاری کانتینر را پیکربندی می‌کند. مقدار آن می‌تواند یکی از موارد زیر باشد:
&quot;&quot;، &quot;NoSwap&quot;: بارهای کاری نمی‌توانند از swap استفاده کنند؛ این گزینه پیش‌فرض است.
&quot;LimitedSwap&quot;: میزان استفاده بار کاری از swap محدود است. سقف swap متناسب با درخواست حافظه (memory request) کانتینر است.</p>
</td>
</tr>
</tbody>
</table>

## `ResourceChangeDetectionStrategy`     {#kubelet-config-k8s-io-v1beta1-ResourceChangeDetectionStrategy}
    
(Alias of `string`)

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>ResourceChangeDetectionStrategy حالتی را مشخص می‌کند که در آن
مدیرهای داخلی (secret و configmap) تغییرات آبجکت‌ها را شناسایی می‌کنند.</p>




## `ShutdownGracePeriodByPodPriority`     {#kubelet-config-k8s-io-v1beta1-ShutdownGracePeriodByPodPriority}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>ShutdownGracePeriodByPodPriority مهلت خاموش‌سازی (shutdown grace period) را برای Podها بر اساس مقدار priority class مرتبط با آن‌ها مشخص می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>priority</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>priority مقدار اولویتی است که با مهلت خاموش‌سازی مرتبط است.</p>
</td>
</tr>
<tr><td><code>shutdownGracePeriodSeconds</code> <B>[Required]</B><br/>
<code>int64</code>
</td>
<td>
   <p>shutdownGracePeriodSeconds مهلت خاموش‌سازی بر حسب ثانیه است.</p>
</td>
</tr>
</tbody>
</table>

## `UserNamespaces`     {#kubelet-config-k8s-io-v1beta1-UserNamespaces}
    

**Appears in:**

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>UserNamespaces شامل پیکربندی‌های فضای نام کاربر (User Namespace) است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>idsPerPod</code><br/>
<code>int64</code>
</td>
<td>
   <p>IDsPerPod طول نگاشت UIDها و GIDهاست.
این طول باید مضربی از ۶۵۵۳۶ و کمتر از 1&lt;&lt;32 باشد.
در سیستم‌عامل‌های غیر لینوکسی مانند ویندوز، فقط مقدار null یا نبودن مقدار مجاز است.</p>
<p>تغییر این مقدار ممکن است نیازمند ایجاد مجدد همه کانتینرهای روی نود باشد.</p>
<p>Default: 65536</p>
</td>
</tr>
</tbody>
</table>
