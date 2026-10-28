---
title: پیکربندی kube-proxy (v1alpha1)
content_type: tool-reference
package: kubeproxy.config.k8s.io/v1alpha1
auto_generated: true
---


## انواع منبع 


- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)
  
    
    

## `FormatOptions`     {#FormatOptions}
    

**در این موارد ظاهر می‌شود:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>FormatOptions شامل گزینه‌هایی برای قالب‌های مختلف گزارش‌گیری (logging) است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>text</code> <B>[الزامی]</B><br/>
<a href="#TextOptions"><code>TextOptions</code></a>
</td>
<td>
   <p>[آلفا] Text شامل گزینه‌هایی برای قالب گزارش‌گیری &quot;text&quot; است.
فقط زمانی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
<tr><td><code>json</code> <B>[الزامی]</B><br/>
<a href="#JSONOptions"><code>JSONOptions</code></a>
</td>
<td>
   <p>[آلفا] JSON شامل گزینه‌هایی برای قالب گزارش‌گیری &quot;json&quot; است.
فقط زمانی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
</tbody>
</table>

## `JSONOptions`     {#JSONOptions}
    

**در این موارد ظاهر می‌شود:**

- [FormatOptions](#FormatOptions)


<p>JSONOptions شامل گزینه‌هایی برای قالب گزارش‌گیری &quot;json&quot; است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>OutputRoutingOptions</code> <B>[الزامی]</B><br/>
<a href="#OutputRoutingOptions"><code>OutputRoutingOptions</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `LogFormatFactory`     {#LogFormatFactory}
    


<p>LogFormatFactory پشتیبانی از یک قالب گزارش اضافی و غیرپیش‌فرض مشخص را فراهم می‌کند.</p>




## `LoggingConfiguration`     {#LoggingConfiguration}
    

**در این موارد ظاهر می‌شود:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)

- [KubeletConfiguration](#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)


<p>LoggingConfiguration شامل گزینه‌های گزارش‌گیری (logging) است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>format</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Format Flag ساختار پیام‌های گزارش را مشخص می‌کند.
مقدار پیش‌فرض format برابر <code>text</code> است.</p>
</td>
</tr>
<tr><td><code>flushFrequency</code> <B>[الزامی]</B><br/>
<a href="#TimeOrMetaDuration"><code>TimeOrMetaDuration</code></a>
</td>
<td>
   <p>بیشترین زمان مجاز بین دو عملیات flush گزارش‌ها.
اگر مقدار از نوع رشته باشد، به‌عنوان یک بازه زمانی (duration) تفسیر می‌شود (برای مثال &quot;1s&quot;).
اگر مقدار از نوع عدد صحیح باشد، بیشترین تعداد نانوثانیه را مشخص می‌کند (برای مثال 1s = 1000000000).
اگر بک‌اند گزارش‌گیری انتخاب‌شده پیام‌های گزارش را بدون بافر بنویسد، این مقدار نادیده گرفته می‌شود.</p>
</td>
</tr>
<tr><td><code>verbosity</code> <B>[الزامی]</B><br/>
<a href="#VerbosityLevel"><code>VerbosityLevel</code></a>
</td>
<td>
   <p>Verbosity آستانه‌ای است که تعیین می‌کند کدام پیام‌های گزارش ثبت شوند.
مقدار پیش‌فرض صفر است که فقط مهم‌ترین پیام‌ها را ثبت می‌کند.
مقادیر بالاتر پیام‌های بیشتری را فعال می‌کنند. پیام‌های خطا همیشه ثبت می‌شوند.</p>
</td>
</tr>
<tr><td><code>vmodule</code> <B>[الزامی]</B><br/>
<a href="#VModuleConfiguration"><code>VModuleConfiguration</code></a>
</td>
<td>
   <p>VModule آستانه verbosity را برای فایل‌های منفرد بازنویسی می‌کند.
فقط برای قالب گزارش &quot;text&quot; پشتیبانی می‌شود.</p>
</td>
</tr>
<tr><td><code>options</code> <B>[الزامی]</B><br/>
<a href="#FormatOptions"><code>FormatOptions</code></a>
</td>
<td>
   <p>[آلفا] Options شامل پارامترهای اضافی است که مختص قالب‌های مختلف گزارش‌گیری هستند.
فقط گزینه‌های قالب انتخاب‌شده استفاده می‌شوند، اما همه آن‌ها اعتبارسنجی می‌شوند.
فقط زمانی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
</tbody>
</table>

## `LoggingOptions`     {#LoggingOptions}
    


<p>LoggingOptions را می‌توان همراه با ValidateAndApplyWithOptions برای بازنویسی
برخی مقادیر پیش‌فرض سراسری به کار برد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ErrorStream</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/io#Writer"><code>io.Writer</code></a>
</td>
<td>
   <p>ErrorStream را می‌توان برای بازنویسی مقدار پیش‌فرض os.Stderr به کار برد.</p>
</td>
</tr>
<tr><td><code>InfoStream</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/io#Writer"><code>io.Writer</code></a>
</td>
<td>
   <p>InfoStream را می‌توان برای بازنویسی مقدار پیش‌فرض os.Stdout به کار برد.</p>
</td>
</tr>
</tbody>
</table>

## `OutputRoutingOptions`     {#OutputRoutingOptions}
    

**در این موارد ظاهر می‌شود:**

- [JSONOptions](#JSONOptions)

- [TextOptions](#TextOptions)


<p>OutputRoutingOptions شامل گزینه‌هایی است که هم توسط &quot;text&quot; و هم توسط &quot;json&quot; پشتیبانی می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>splitStream</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>[آلفا] SplitStream پیام‌های خطا را به stderr هدایت می‌کند، در حالی که پیام‌های اطلاعاتی
با بافر به stdout ارسال می‌شوند. رفتار پیش‌فرض این است که هر دو بدون بافر به stdout نوشته شوند.
فقط زمانی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
<tr><td><code>infoBufferSize</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#QuantityValue"><code>k8s.io/apimachinery/pkg/api/resource.QuantityValue</code></a>
</td>
<td>
   <p>[آلفا] InfoBufferSize اندازه جریان اطلاعات (info stream) را هنگام استفاده از جریان‌های جداگانه تعیین می‌کند.
مقدار پیش‌فرض صفر است که بافر را غیرفعال می‌کند.
فقط زمانی در دسترس است که feature gate با نام LoggingAlphaOptions فعال باشد.</p>
</td>
</tr>
</tbody>
</table>

## `TextOptions`     {#TextOptions}
    

**در این موارد ظاهر می‌شود:**

- [FormatOptions](#FormatOptions)


<p>TextOptions شامل گزینه‌هایی برای قالب گزارش‌گیری &quot;text&quot; است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>OutputRoutingOptions</code> <B>[الزامی]</B><br/>
<a href="#OutputRoutingOptions"><code>OutputRoutingOptions</code></a>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `TimeOrMetaDuration`     {#TimeOrMetaDuration}
    

**در این موارد ظاهر می‌شود:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>TimeOrMetaDuration صرفاً برای سازگاری با نسخه‌های قبلی در فیلد
flushFrequency وجود دارد و فیلدهای جدید باید از metav1.Duration استفاده کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>Duration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>Duration نگه‌دارنده بازه زمانی است.</p>
</td>
</tr>
<tr><td><code>-</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>SerializeAsString مشخص می‌کند که مقدار به‌صورت رشته یا عدد صحیح سریال‌سازی شود.</p>
</td>
</tr>
</tbody>
</table>

## `VModuleConfiguration`     {#VModuleConfiguration}
    
(نام مستعار برای `[]k8s.io/component-base/logs/api/v1.VModuleItem`)

**در این موارد ظاهر می‌شود:**

- [LoggingConfiguration](#LoggingConfiguration)


<p>VModuleConfiguration مجموعه‌ای از نام فایل‌ها یا الگوهای منفرد
و آستانه verbosity متناظر با هر یک است.</p>




## `VerbosityLevel`     {#VerbosityLevel}
    
(نام مستعار برای `uint32`)

**در این موارد ظاهر می‌شود:**

- [LoggingConfiguration](#LoggingConfiguration)



<p>VerbosityLevel نشان‌دهنده یک آستانه verbosity در klog یا logr است.</p>



  
    
    

## `ClientConnectionConfiguration`     {#ClientConnectionConfiguration}
    

**در این موارد ظاهر می‌شود:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>ClientConnectionConfiguration شامل جزئیات لازم برای ساخت یک کلاینت است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubeconfig</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>kubeconfig مسیر یک فایل KubeConfig است.</p>
</td>
</tr>
<tr><td><code>acceptContentTypes</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>acceptContentTypes هدر Accept را که کلاینت‌ها هنگام اتصال به یک سرور ارسال می‌کنند تعریف می‌کند و
مقدار پیش‌فرض 'application/json' را بازنویسی می‌کند. این فیلد همه اتصال‌هایی را که یک
کلاینت مشخص به سرور برقرار می‌کند کنترل می‌کند.</p>
</td>
</tr>
<tr><td><code>contentType</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>contentType نوع محتوایی است که هنگام ارسال داده از این کلاینت به سرور استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>qps</code> <B>[الزامی]</B><br/>
<code>float32</code>
</td>
<td>
   <p>qps تعداد درخواست‌های مجاز در هر ثانیه برای این اتصال را کنترل می‌کند.</p>
</td>
</tr>
<tr><td><code>burst</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>burst به درخواست‌های اضافی اجازه می‌دهد زمانی که کلاینت از نرخ مجاز خود فراتر می‌رود، انباشته شوند.</p>
</td>
</tr>
</tbody>
</table>

## `DebuggingConfiguration`     {#DebuggingConfiguration}
    

**در این موارد ظاهر می‌شود:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>DebuggingConfiguration شامل پیکربندی ویژگی‌های مرتبط با اشکال‌زدایی (debugging) است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>enableProfiling</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableProfiling پروفایل‌گیری (profiling) را از طریق رابط وب در host:port/debug/pprof/ فعال می‌کند.</p>
</td>
</tr>
<tr><td><code>enableContentionProfiling</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableContentionProfiling در صورتی که
enableProfiling برابر true باشد، پروفایل‌گیری block را فعال می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `LeaderElectionConfiguration`     {#LeaderElectionConfiguration}
    

**در این موارد ظاهر می‌شود:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>LeaderElectionConfiguration پیکربندی کلاینت‌های انتخاب رهبر (leader election)
را برای مؤلفه‌هایی که می‌توانند با فعال بودن leader election اجرا شوند تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>leaderElect</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>leaderElect باعث می‌شود یک کلاینت انتخاب رهبر پیش از اجرای حلقه اصلی، رهبری را به دست آورد.
این گزینه را هنگام اجرای مؤلفه‌های replicated برای دستیابی به دسترس‌پذیری بالا فعال کنید.</p>
</td>
</tr>
<tr><td><code>leaseDuration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>leaseDuration مدت زمانی است که نامزدهای غیررهبر پس از مشاهده تمدید رهبری صبر می‌کنند
تا برای کسب رهبری یک جایگاه رهبری که اشغال شده اما تمدید نشده است اقدام کنند.
این مقدار در عمل بیشترین مدتی است که یک رهبر می‌تواند متوقف باشد
پیش از آنکه نامزد دیگری جایگزین آن شود. فقط در صورتی کاربرد دارد که
leader election فعال باشد.</p>
</td>
</tr>
<tr><td><code>renewDeadline</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>renewDeadline فاصله زمانی بین تلاش‌های master فعلی برای تمدید جایگاه رهبری
پیش از آن است که از رهبری دست بکشد. این مقدار باید کمتر از
یا برابر با مدت lease باشد. فقط در صورتی کاربرد دارد که leader
election فعال باشد.</p>
</td>
</tr>
<tr><td><code>retryPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>retryPeriod مدت زمانی است که کلاینت‌ها باید بین تلاش‌های
کسب و تمدید رهبری صبر کنند. فقط در صورتی کاربرد دارد که
leader election فعال باشد.</p>
</td>
</tr>
<tr><td><code>resourceLock</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceLock نوع آبجکت منبعی را مشخص می‌کند که برای قفل کردن
در چرخه‌های انتخاب رهبر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>resourceName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName نام آبجکت منبعی را مشخص می‌کند که برای قفل کردن
در چرخه‌های انتخاب رهبر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>resourceNamespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName فضای نام (namespace) آبجکت منبعی را مشخص می‌کند که برای قفل کردن
در چرخه‌های انتخاب رهبر استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `KubeProxyConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration}
    


<p>KubeProxyConfiguration شامل همه‌ی موارد لازم برای پیکربندی
سرور پراکسی کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeproxy.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>KubeProxyConfiguration</code></td></tr>
    
  
<tr><td><code>featureGates</code> <B>[Required]</B><br/>
<code>map[string]bool</code>
</td>
<td>
   <p>featureGates نگاشتی از نام قابلیت‌ها به مقادیر بولی است که قابلیت‌های آلفا/آزمایشی را فعال یا غیرفعال می‌کند.</p>
</td>
</tr>
<tr><td><code>clientConnection</code> <B>[Required]</B><br/>
<a href="#ClientConnectionConfiguration"><code>ClientConnectionConfiguration</code></a>
</td>
<td>
   <p>clientConnection فایل kubeconfig و تنظیمات اتصال کلاینت را مشخص می‌کند که سرور پراکسی
هنگام ارتباط با apiserver از آن‌ها استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>logging</code> <B>[Required]</B><br/>
<a href="#LoggingConfiguration"><code>LoggingConfiguration</code></a>
</td>
<td>
   <p>logging گزینه‌های مربوط به ثبت لاگ را مشخص می‌کند.
برای اطلاعات بیشتر به <a href="https://github.com/kubernetes/component-base/blob/master/logs/options.go">Logs Options</a>
مراجعه کنید.</p>
</td>
</tr>
<tr><td><code>hostnameOverride</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>hostnameOverride در صورت غیرتهی بودن، به‌عنوان نام نودی که
kube-proxy روی آن اجرا می‌شود به کار می‌رود. اگر تنظیم نشده باشد، فرض می‌شود نام نود
با نام میزبان (hostname) نود یکسان است.</p>
</td>
</tr>
<tr><td><code>bindAddress</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>bindAddress می‌تواند برای بازنویسی برداشت kube-proxy از IP اصلی نود خود به کار رود.
توجه داشته باشید که این نام یک یادگار تاریخی است و kube-proxy
در واقع هیچ سوکتی را به این IP متصل (bind) نمی‌کند.</p>
</td>
</tr>
<tr><td><code>healthzBindAddress</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>healthzBindAddress آدرس IP و پورتی است که سرور بررسی سلامت روی آن سرویس‌دهی می‌کند و مقدار پیش‌فرض آن
&quot;0.0.0.0:10256&quot; است (اگر bindAddress تنظیم نشده باشد یا IPv4 باشد)، یا
&quot;[::]:10256&quot; (اگر bindAddress از نوع IPv6 باشد).</p>
</td>
</tr>
<tr><td><code>metricsBindAddress</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>metricsBindAddress آدرس IP و پورتی است که سرور متریک‌ها روی آن سرویس‌دهی می‌کند و مقدار پیش‌فرض آن
&quot;127.0.0.1:10249&quot; است (اگر bindAddress تنظیم نشده باشد یا IPv4 باشد)، یا
&quot;[::1]:10249&quot; (اگر bindAddress از نوع IPv6 باشد). (برای اتصال به همه‌ی اینترفیس‌ها،
مقدار را روی &quot;0.0.0.0:10249&quot; / &quot;[::]:10249&quot; تنظیم کنید.)</p>
</td>
</tr>
<tr><td><code>bindAddressHardFail</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>bindAddressHardFail در صورت true بودن، به kube-proxy می‌گوید که ناکامی در اتصال به یک
پورت را خطای مرگبار تلقی کند و خارج شود.</p>
</td>
</tr>
<tr><td><code>enableProfiling</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableProfiling پروفایل‌گیری از طریق رابط وب را روی handler مربوط به /debug/pprof فعال می‌کند.
handlerهای پروفایل‌گیری توسط سرور متریک‌ها مدیریت می‌شوند.</p>
</td>
</tr>
<tr><td><code>showHiddenMetricsForVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>showHiddenMetricsForVersion نسخه‌ای است که می‌خواهید متریک‌های پنهان آن نمایش داده شوند.</p>
</td>
</tr>
<tr><td><code>mode</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-ProxyMode"><code>ProxyMode</code></a>
</td>
<td>
   <p>mode مشخص می‌کند از کدام حالت پراکسی استفاده شود.</p>
</td>
</tr>
<tr><td><code>iptables</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-KubeProxyIPTablesConfiguration"><code>KubeProxyIPTablesConfiguration</code></a>
</td>
<td>
   <p>iptables شامل گزینه‌های پیکربندی مرتبط با iptables است.</p>
</td>
</tr>
<tr><td><code>ipvs</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-KubeProxyIPVSConfiguration"><code>KubeProxyIPVSConfiguration</code></a>
</td>
<td>
   <p>ipvs شامل گزینه‌های پیکربندی مرتبط با ipvs است.</p>
</td>
</tr>
<tr><td><code>nftables</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-KubeProxyNFTablesConfiguration"><code>KubeProxyNFTablesConfiguration</code></a>
</td>
<td>
   <p>nftables شامل گزینه‌های پیکربندی مرتبط با nftables است.</p>
</td>
</tr>
<tr><td><code>winkernel</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-KubeProxyWinkernelConfiguration"><code>KubeProxyWinkernelConfiguration</code></a>
</td>
<td>
   <p>winkernel شامل گزینه‌های پیکربندی مرتبط با winkernel است.</p>
</td>
</tr>
<tr><td><code>detectLocalMode</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-LocalMode"><code>LocalMode</code></a>
</td>
<td>
   <p>detectLocalMode حالتی را که برای تشخیص ترافیک محلی به کار می‌رود تعیین می‌کند؛ مقدار پیش‌فرض ClusterCIDR است.</p>
</td>
</tr>
<tr><td><code>detectLocal</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-DetectLocalConfiguration"><code>DetectLocalConfiguration</code></a>
</td>
<td>
   <p>detectLocal شامل تنظیمات اختیاری مرتبط با DetectLocalMode است.</p>
</td>
</tr>
<tr><td><code>clusterCIDR</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterCIDR محدوده‌ی CIDR پادهای کلاستر است. (برای کلاسترهای dual-stack
می‌توان یک جفت محدوده‌ی CIDR جداشده با ویرگول برای dual-stack تعیین کرد.) وقتی
DetectLocalMode روی ClusterCIDR تنظیم شده باشد، kube-proxy
ترافیکی را محلی در نظر می‌گیرد که IP مبدأ آن در این محدوده باشد. (در غیر این صورت
از این فیلد استفاده نمی‌شود.)</p>
</td>
</tr>
<tr><td><code>nodePortAddresses</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>nodePortAddresses فهرستی از محدوده‌های CIDR و/یا کلیدواژه‌هایی است که به محدوده‌های CIDR بسط می‌یابند.
سرویس‌های NodePort فقط روی IPهای نودی که در این فهرست پوشش داده شده‌اند در دسترس هستند.
کلیدواژه‌های پشتیبانی‌شده: 'primary' (آدرس‌های IPv4 و/یا IPv6 اصلی آبجکت Node)،
'localhost' (‏127.0.0.0/8 و ::1/128) و 'all' (‏0.0.0.0/0 و ::/0).
هر ترکیبی از کلیدواژه‌ها و CIDRهای معتبر را می‌توان در فهرست قرار داد.</p>
<p>سرویس‌دهی NodePortها روی IPهای loopback فقط در حالت iptables پشتیبانی می‌شود (فقط IPv4،
به iptables.localhostNodePorts مراجعه کنید)، و در حالت nftables فقط برای TCP و هنگامی که
feature gate با نام KubeProxyNFTablesLocalhostNodePorts فعال باشد و فهرست
به‌صراحت loopback را شامل شود (برای مثال 'localhost').</p>
<p>اگر تنظیم نشود، مقدار پیش‌فرض در حالت iptables و ipvs برابر 'all' و در حالت
nftables برابر 'primary' است.</p>
</td>
</tr>
<tr><td><code>oomScoreAdj</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>oomScoreAdj مقدار oom-score-adj برای فرایند kube-proxy است. مقادیر باید در بازه‌ی
[-1000, 1000] باشند.</p>
</td>
</tr>
<tr><td><code>conntrack</code> <B>[Required]</B><br/>
<a href="#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConntrackConfiguration"><code>KubeProxyConntrackConfiguration</code></a>
</td>
<td>
   <p>conntrack شامل گزینه‌های پیکربندی مرتبط با conntrack است.</p>
</td>
</tr>
<tr><td><code>configSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>configSyncPeriod مشخص می‌کند پیکربندی دریافتی از apiserver هر چند وقت یک‌بار تازه‌سازی شود. باید بزرگ‌تر
از 0 باشد.</p>
</td>
</tr>
<tr><td><code>portRange</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>portRange پیش‌تر برای پیکربندی پراکسی userspace به کار می‌رفت، اما اکنون استفاده نمی‌شود.</p>
</td>
</tr>
<tr><td><code>windowsRunAsService</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>windowsRunAsService در صورت true بودن، یکپارچگی با API مدیر کنترل سرویس ویندوز (Windows service control manager) را فعال می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `DetectLocalConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-DetectLocalConfiguration}
    

**Appears in:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>DetectLocalConfiguration شامل تنظیمات اختیاری مرتبط با گزینه‌ی DetectLocalMode است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>bridgeInterface</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>bridgeInterface نام یک اینترفیس bridge است. وقتی DetectLocalMode روی
LocalModeBridgeInterface تنظیم شده باشد، kube-proxy ترافیکی را محلی در نظر می‌گیرد که
از این bridge سرچشمه گرفته باشد.</p>
</td>
</tr>
<tr><td><code>interfaceNamePrefix</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>interfaceNamePrefix پیشوند نام اینترفیس است. وقتی DetectLocalMode روی
LocalModeInterfaceNamePrefix تنظیم شده باشد، kube-proxy ترافیکی را محلی در نظر می‌گیرد که
از هر اینترفیسی که نام آن با این پیشوند آغاز می‌شود سرچشمه گرفته باشد.</p>
</td>
</tr>
</tbody>
</table>

## `KubeProxyConntrackConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConntrackConfiguration}
    

**Appears in:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>KubeProxyConntrackConfiguration شامل تنظیمات conntrack برای
سرور پراکسی کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>maxPerCore</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>maxPerCore بیشینه‌ی تعداد اتصال‌های NAT است که به ازای هر هسته‌ی CPU ردیابی می‌شود
(مقدار 0 یعنی محدودیت را بدون تغییر بگذار و min را نادیده بگیر).</p>
</td>
</tr>
<tr><td><code>min</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>min کمینه‌ی تعداد رکوردهای ردیابی اتصال است که صرف‌نظر از maxPerCore تخصیص داده می‌شود
(برای اینکه محدودیت بدون تغییر بماند، maxPerCore=0 را تنظیم کنید).</p>
</td>
</tr>
<tr><td><code>tcpEstablishedTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>tcpEstablishedTimeout مشخص می‌کند یک اتصال TCP بیکار تا چه مدت باز نگه داشته شود
(برای مثال '2s'). برای تنظیم، باید بزرگ‌تر از 0 باشد.</p>
</td>
</tr>
<tr><td><code>tcpCloseWaitTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>tcpCloseWaitTimeout مشخص می‌کند یک ورودی conntrack بیکار
در وضعیت CLOSE_WAIT تا چه مدت در جدول conntrack
باقی بماند (برای مثال '60s'). برای تنظیم، باید بزرگ‌تر از 0 باشد.</p>
</td>
</tr>
<tr><td><code>tcpBeLiberal</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>tcpBeLiberal در صورت true بودن، kube-proxy مقدار conntrack را طوری پیکربندی می‌کند
که برای اتصال‌های TCP در حالت liberal اجرا شود و بسته‌هایی با
شماره‌های ترتیب خارج از پنجره (out-of-window) با وضعیت INVALID علامت‌گذاری نشوند.</p>
</td>
</tr>
<tr><td><code>udpTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>udpTimeout مشخص می‌کند یک ورودی conntrack بیکار UDP در
وضعیت UNREPLIED تا چه مدت در جدول conntrack باقی بماند
(برای مثال '30s'). برای تنظیم، باید بزرگ‌تر از 0 باشد.</p>
</td>
</tr>
<tr><td><code>udpStreamTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>udpStreamTimeout مشخص می‌کند یک ورودی conntrack بیکار UDP در
وضعیت ASSURED تا چه مدت در جدول conntrack باقی بماند
(برای مثال '300s'). برای تنظیم، باید بزرگ‌تر از 0 باشد.</p>
</td>
</tr>
</tbody>
</table>

## `KubeProxyIPTablesConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-KubeProxyIPTablesConfiguration}
    

**Appears in:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>KubeProxyIPTablesConfiguration شامل جزئیات پیکربندی مرتبط با iptables
برای سرور پراکسی کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>masqueradeBit</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>masqueradeBit بیتی از فضای fwmark در iptables است که در صورت استفاده از
حالت پراکسی iptables یا ipvs برای SNAT به کار می‌رود. مقادیر باید در بازه‌ی [0, 31] باشند.</p>
</td>
</tr>
<tr><td><code>masqueradeAll</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>masqueradeAll به kube-proxy می‌گوید در هنگام استفاده از حالت پراکسی iptables یا ipvs،
بر روی همه‌ی ترافیک ارسالی به IPهای cluster سرویس‌ها SNAT انجام دهد. این کار ممکن است با برخی
افزونه‌های CNI لازم باشد.</p>
</td>
</tr>
<tr><td><code>localhostNodePorts</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>localhostNodePorts در صورت false بودن، به kube-proxy می‌گوید رفتار قدیمی
اجازه‌ی دسترسی به سرویس‌های NodePort از طریق localhost را غیرفعال کند. (فقط در
حالت iptables و برای IPv4 اعمال می‌شود؛ NodePortهای localhost در حالت‌های پراکسی دیگر
یا با IPv6 هرگز مجاز نیستند.)</p>
</td>
</tr>
<tr><td><code>syncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>syncPeriod بازه‌ای است (برای مثال '5s'، '1m'، '2h22m') که مشخص می‌کند عملیات‌های مختلف
همگام‌سازی مجدد و پاک‌سازی هر چند وقت یک‌بار انجام شوند. باید بزرگ‌تر
از 0 باشد.</p>
</td>
</tr>
<tr><td><code>minSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>minSyncPeriod کمینه‌ی فاصله‌ی زمانی بین همگام‌سازی‌های مجدد قوانین iptables است (برای مثال '5s'،
'1m'، '2h22m'). مقدار 0 یعنی هر تغییر در Service یا EndpointSlice
به همگام‌سازی مجدد فوری iptables منجر می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `KubeProxyIPVSConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-KubeProxyIPVSConfiguration}
    

**Appears in:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>KubeProxyIPVSConfiguration شامل جزئیات پیکربندی مرتبط با ipvs
برای سرور پراکسی کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>syncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>syncPeriod بازه‌ای است (برای مثال '5s'، '1m'، '2h22m') که مشخص می‌کند عملیات‌های مختلف
همگام‌سازی مجدد و پاک‌سازی هر چند وقت یک‌بار انجام شوند. باید بزرگ‌تر
از 0 باشد.</p>
</td>
</tr>
<tr><td><code>minSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>minSyncPeriod کمینه‌ی فاصله‌ی زمانی بین همگام‌سازی‌های مجدد قوانین IPVS است (برای مثال '5s'، '1m'،
'2h22m'). مقدار 0 یعنی هر تغییر در Service یا EndpointSlice
به همگام‌سازی مجدد فوری IPVS منجر می‌شود.</p>
</td>
</tr>
<tr><td><code>scheduler</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>scheduler زمان‌بند IPVS مورد استفاده است.</p>
</td>
</tr>
<tr><td><code>excludeCIDRs</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>excludeCIDRs فهرستی از CIDRهاست که proxier مربوط به ipvs هنگام پاک‌سازی سرویس‌های ipvs
نباید به آن‌ها دست بزند.</p>
</td>
</tr>
<tr><td><code>strictARP</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>strictARP مقادیر arp_ignore و arp_announce را طوری پیکربندی می‌کند که از پاسخ دادن به پرس‌وجوهای ARP
از اینترفیس kube-ipvs0 جلوگیری شود.</p>
</td>
</tr>
<tr><td><code>tcpTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>tcpTimeout مقدار timeout است که برای نشست‌های TCP بیکار IPVS به کار می‌رود.
مقدار پیش‌فرض 0 است که مقدار timeout فعلی سیستم را حفظ می‌کند.</p>
</td>
</tr>
<tr><td><code>tcpFinTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>tcpFinTimeout مقدار timeout است که برای نشست‌های TCP در IPVS پس از دریافت FIN به کار می‌رود.
مقدار پیش‌فرض 0 است که مقدار timeout فعلی سیستم را حفظ می‌کند.</p>
</td>
</tr>
<tr><td><code>udpTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>udpTimeout مقدار timeout است که برای بسته‌های UDP در IPVS به کار می‌رود.
مقدار پیش‌فرض 0 است که مقدار timeout فعلی سیستم را حفظ می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `KubeProxyNFTablesConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-KubeProxyNFTablesConfiguration}
    

**Appears in:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>KubeProxyNFTablesConfiguration شامل جزئیات پیکربندی مرتبط با nftables
برای سرور پراکسی کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>masqueradeBit</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>masqueradeBit بیتی از فضای fwmark در iptables است که در صورت استفاده از
حالت پراکسی nftables برای SNAT به کار می‌رود. مقادیر باید در بازه‌ی [0, 31] باشند.</p>
</td>
</tr>
<tr><td><code>masqueradeAll</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>masqueradeAll به kube-proxy می‌گوید در هنگام استفاده از حالت nftables،
بر روی همه‌ی ترافیک ارسالی به IPهای cluster سرویس‌ها SNAT انجام دهد. این کار ممکن است با برخی افزونه‌های CNI لازم باشد.</p>
</td>
</tr>
<tr><td><code>syncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>syncPeriod بازه‌ای است (برای مثال '5s'، '1m'، '2h22m') که مشخص می‌کند عملیات‌های مختلف
همگام‌سازی مجدد و پاک‌سازی هر چند وقت یک‌بار انجام شوند. باید بزرگ‌تر
از 0 باشد.</p>
</td>
</tr>
<tr><td><code>minSyncPeriod</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>minSyncPeriod کمینه‌ی فاصله‌ی زمانی بین همگام‌سازی‌های مجدد قوانین iptables است (برای مثال '5s'،
'1m'، '2h22m'). مقدار 0 یعنی هر تغییر در Service یا EndpointSlice
به همگام‌سازی مجدد فوری iptables منجر می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `KubeProxyWinkernelConfiguration`     {#kubeproxy-config-k8s-io-v1alpha1-KubeProxyWinkernelConfiguration}
    

**ظاهر شده در:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>KubeProxyWinkernelConfiguration شامل تنظیمات Windows/HNS برای
سرور پروکسی کوبرنتیز است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>networkName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>networkName نام شبکه‌ای است که kube-proxy برای ایجاد endpointها و سیاست‌ها
از آن استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>sourceVip</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>sourceVip نشانی IP مربوط به endpoint مبدأ VIP است که هنگام توزیع بار (loadbalancing)
برای NAT استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>enableDSR</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableDSR به kube-proxy اعلام می‌کند که آیا سیاست‌های HNS باید
با DSR ایجاد شوند یا خیر.</p>
</td>
</tr>
<tr><td><code>rootHnsEndpointName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>rootHnsEndpointName نام hnsendpoint است که برای فضای نام شبکه ریشه (root network namespace)
به l2bridge متصل شده است.</p>
</td>
</tr>
<tr><td><code>forwardHealthCheckVip</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>forwardHealthCheckVip برای پورت بررسی سلامت (health check) در
Windows، VIP سرویس را بازارسال (forward) می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `LocalMode`     {#kubeproxy-config-k8s-io-v1alpha1-LocalMode}
    
(نام مستعار برای `string`)

**ظاهر شده در:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>LocalMode حالت‌هایی را نشان می‌دهد که برای تشخیص ترافیک محلی نود به کار می‌روند.</p>




## `ProxyMode`     {#kubeproxy-config-k8s-io-v1alpha1-ProxyMode}
    
(نام مستعار برای `string`)

**ظاهر شده در:**

- [KubeProxyConfiguration](#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)


<p>ProxyMode حالت‌هایی را نشان می‌دهد که سرور پروکسی کوبرنتیز از آن‌ها استفاده می‌کند.</p>
<p>در پلتفرم‌های Linux سه حالت پروکسی در دسترس است: <code>iptables</code>، <code>ipvs</code> و
<code>nftables</code>. در پلتفرم‌های Windows یک حالت پروکسی در دسترس است: <code>kernelspace</code>.</p>
<p>اگر حالت پروکسی مشخص نشود، یک حالت پروکسی پیش‌فرض استفاده خواهد شد (در حال حاضر
این حالت در Linux برابر <code>iptables</code> و در Windows برابر <code>kernelspace</code> است). اگر حالت پروکسی انتخاب‌شده
قابل استفاده نباشد (به دلیل نبود پشتیبانی هسته، نبود مؤلفه‌های فضای کاربر و غیره)، kube-proxy
با یک خطا خارج می‌شود.</p>
