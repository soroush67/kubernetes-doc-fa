---
title: پیکربندی kube-scheduler (v1)
content_type: tool-reference
package: kubescheduler.config.k8s.io/v1
auto_generated: true
---


## انواع منابع {#resource-types}


- [DefaultPreemptionArgs](#kubescheduler-config-k8s-io-v1-DefaultPreemptionArgs)
- [DynamicResourcesArgs](#kubescheduler-config-k8s-io-v1-DynamicResourcesArgs)
- [InterPodAffinityArgs](#kubescheduler-config-k8s-io-v1-InterPodAffinityArgs)
- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)
- [NodeAffinityArgs](#kubescheduler-config-k8s-io-v1-NodeAffinityArgs)
- [NodeResourcesBalancedAllocationArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesBalancedAllocationArgs)
- [NodeResourcesFitArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs)
- [PodTopologySpreadArgs](#kubescheduler-config-k8s-io-v1-PodTopologySpreadArgs)
- [VolumeBindingArgs](#kubescheduler-config-k8s-io-v1-VolumeBindingArgs)
  
    
    

## `ClientConnectionConfiguration`     {#ClientConnectionConfiguration}
    

**ظاهر شده در:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)


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
مقدار پیش‌فرض 'application/json' را بازنویسی می‌کند. این فیلد تمام اتصال‌هایی را که یک
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
   <p>qps تعداد پرس‌وجوهای مجاز در هر ثانیه را برای این اتصال کنترل می‌کند.</p>
</td>
</tr>
<tr><td><code>burst</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>burst اجازه می‌دهد زمانی که یک کلاینت از نرخ مجاز خود فراتر می‌رود، پرس‌وجوهای اضافی انباشته شوند.</p>
</td>
</tr>
</tbody>
</table>

## `DebuggingConfiguration`     {#DebuggingConfiguration}
    

**ظاهر شده در:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)


<p>DebuggingConfiguration پیکربندی ویژگی‌های مرتبط با اشکال‌زدایی (Debugging) را نگهداری می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>enableProfiling</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableProfiling پروفایل‌گیری را از طریق رابط وب در host:port/debug/pprof/ فعال می‌کند.</p>
</td>
</tr>
<tr><td><code>enableContentionProfiling</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableContentionProfiling در صورتی که
enableProfiling برابر true باشد، پروفایل‌گیری انسدادها (block profiling) را فعال می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `LeaderElectionConfiguration`     {#LeaderElectionConfiguration}
    

**ظاهر شده در:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)


<p>LeaderElectionConfiguration پیکربندی کلاینت‌های انتخاب رهبر (leader election)
را برای مؤلفه‌هایی که می‌توانند با فعال بودن انتخاب رهبر اجرا شوند تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>leaderElect</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>leaderElect به یک کلاینت انتخاب رهبر امکان می‌دهد پیش از اجرای حلقه اصلی
رهبری را به دست آورد. هنگام اجرای مؤلفه‌های replicate‌شده برای دسترس‌پذیری بالا،
این گزینه را فعال کنید.</p>
</td>
</tr>
<tr><td><code>leaseDuration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>leaseDuration مدت زمانی است که کاندیداهای غیررهبر، پس از مشاهده تمدید رهبری،
منتظر می‌مانند تا برای کسب رهبری یک جایگاه رهبری که اشغال شده اما تمدید نشده است اقدام کنند.
این مقدار در عمل بیشترین مدتی است که یک رهبر می‌تواند متوقف باشد تا
کاندیدای دیگری جایگزین آن شود. این مقدار فقط در صورتی کاربرد دارد که انتخاب رهبر
فعال باشد.</p>
</td>
</tr>
<tr><td><code>renewDeadline</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>renewDeadline فاصله زمانی بین تلاش‌های master فعلی برای
تمدید جایگاه رهبری، پیش از آن است که از رهبری دست بکشد. این مقدار باید کمتر
از مدت lease یا برابر با آن باشد. این مقدار فقط در صورتی کاربرد دارد که انتخاب
رهبر فعال باشد.</p>
</td>
</tr>
<tr><td><code>retryPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>retryPeriod مدت زمانی است که کلاینت‌ها باید میان تلاش‌های کسب
و تمدید رهبری صبر کنند. این مقدار فقط در صورتی کاربرد دارد که
انتخاب رهبر فعال باشد.</p>
</td>
</tr>
<tr><td><code>resourceLock</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceLock نوع آبجکت منبعی را مشخص می‌کند که برای قفل کردن
در چرخه‌های انتخاب رهبر استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>resourceName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName نام آبجکت منبعی را مشخص می‌کند که برای قفل کردن
در چرخه‌های انتخاب رهبر استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>resourceNamespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName فضای نام (namespace) آبجکت منبعی را مشخص می‌کند که برای قفل کردن
در چرخه‌های انتخاب رهبر استفاده خواهد شد.</p>
</td>
</tr>
</tbody>
</table>
  

## `DefaultPreemptionArgs`     {#kubescheduler-config-k8s-io-v1-DefaultPreemptionArgs}
    


<p>DefaultPreemptionArgs آرگومان‌های مورد استفاده برای پیکربندی
افزونه DefaultPreemption را نگهداری می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>DefaultPreemptionArgs</code></td></tr>
    
  
<tr><td><code>minCandidateNodesPercentage</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>MinCandidateNodesPercentage حداقل تعداد کاندیداها برای
فهرست کوتاه هنگام اجرای آزمایشی (dry run) پیش‌دستی (preemption) است که به‌صورت درصدی از تعداد نودها بیان می‌شود.
باید در بازه [0, 100] باشد. در صورت مشخص نشدن، پیش‌فرض آن 10% اندازه کلاستر است.</p>
</td>
</tr>
<tr><td><code>minCandidateNodesAbsolute</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>MinCandidateNodesAbsolute حداقل مطلق تعداد کاندیداها برای
فهرست کوتاه است. تعداد محتمل کاندیداهایی که برای اجرای آزمایشی
پیش‌دستی برشمرده می‌شوند با این فرمول به دست می‌آید:
numCandidates = max(numNodes * minCandidateNodesPercentage, minCandidateNodesAbsolute)
از واژه «محتمل» استفاده می‌کنیم زیرا عوامل دیگری مانند نقض PDB
نیز در تعداد کاندیداهای فهرست کوتاه نقش دارند. باید دست‌کم
0 نود باشد. در صورت مشخص نشدن، پیش‌فرض آن 100 نود است.</p>
</td>
</tr>
</tbody>
</table>

## `DynamicResourcesArgs`     {#kubescheduler-config-k8s-io-v1-DynamicResourcesArgs}
    


<p>DynamicResourcesArgs آرگومان‌های مورد استفاده برای پیکربندی افزونه DynamicResources را نگهداری می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>DynamicResourcesArgs</code></td></tr>
    
  
<tr><td><code>filterTimeout</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>FilterTimeout مدت زمانی را که عملیات فیلتر می‌تواند به ازای هر نود
برای جست‌وجوی دستگاه‌هایی که می‌توان برای زمان‌بندی یک پاد روی آن نود
تخصیص داد صرف کند، محدود می‌کند.</p>
<p>در سناریوهای معمول، این عملیات باید ظرف ۱۰ تا ۲۰۰
میلی‌ثانیه کامل شود، اما بسته به تعداد
درخواست‌ها به ازای هر ResourceClaim، تعداد ResourceClaimها، تعداد
دستگاه‌های منتشرشده در ResourceSliceها و پیچیدگی
درخواست‌ها می‌تواند طولانی‌تر هم باشد. بررسی‌های دیگری غیر از ارزیابی CEL نیز زمان می‌برند (بررسی‌های
مصرف، تطبیق ویژگی‌ها و غیره).</p>
<p>بنابراین افزونه زمان‌بند این مهلت زمانی را اعمال می‌کند. اگر به مهلت زمانی
برسیم، پاد برای آن نود غیرقابل زمان‌بندی در نظر گرفته می‌شود.
اگر فیلتر کردن برای نود یا نودهای دیگری موفق باشد، آن‌ها انتخاب می‌شوند.
اگر فیلتر کردن برای همه آن‌ها شکست بخورد، پاد در
صف غیرقابل زمان‌بندی قرار می‌گیرد. در صورتی که تغییرات
مثلاً در ResourceSliceها یا ResourceClaimها نشان دهد که
تلاش دیگری برای زمان‌بندی ممکن است موفق شود، دوباره بررسی خواهد شد. اگر این کار به‌طور مکرر شکست بخورد،
backoff نمایی تلاش‌های بعدی را کندتر می‌کند.</p>
<p>مقدار پیش‌فرض ۱۰ ثانیه است.
این مقدار برای جلوگیری از بدترین سناریوها کافی است و در عین حال بر
استفاده عادی از DRA تأثیری نمی‌گذارد. با این حال، فیلتر کردن کند می‌تواند زمان‌بندی پادها را
حتی برای پادهایی که از DRA استفاده نمی‌کنند نیز کند کند. مدیران می‌توانند مهلت زمانی را
پس از بررسی معیارهای
<code>scheduler_framework_extension_point_duration_seconds</code> کاهش دهند.</p>
<p>تنظیم آن روی صفر، مهلت زمانی را به‌طور کامل غیرفعال می‌کند.</p>
</td>
</tr>
<tr><td><code>bindingTimeout</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>BindingTimeout مشخص می‌کند نقطه توسعه PreBind در صورت وجود
BindingConditionهای دستگاه ResourceClaim حداکثر چه مدت می‌تواند منتظر برآورده شدن آن‌ها بماند.
در طول انتظار، زمان‌بند به‌طور دوره‌ای وضعیت دستگاه را بررسی می‌کند. اگر مهلت زمانی پیش از آن‌که همه شرط‌های لازم
برقرار شوند (یا هر یک از bindingFailureConditions برقرار شود) سپری شود، تخصیص
پاک می‌شود و پاد دوباره وارد صف زمان‌بندی می‌شود. توجه کنید که در صورت امکان، همان نود یا نود دیگری
ممکن است انتخاب شود؛ در غیر این صورت پاد در صف غیرقابل زمان‌بندی قرار می‌گیرد و
بر اساس تغییرات کلاستر و backoff دوباره تلاش می‌شود.</p>
<p>پیش‌فرض‌ها و feature gateها:</p>
<ul>
<li>زمانی که feature gate با نام DRADeviceBindingConditions فعال باشد، پیش‌فرض ۱۰ دقیقه است.</li>
<li>فقط زمانی اثر دارد که هر دو feature gate یعنی DRADeviceBindingConditions و
DRAResourceClaimDeviceStatus فعال باشند؛ در غیر این صورت این فیلد را حذف کنید.</li>
<li>زمانی که DRADeviceBindingConditions غیرفعال باشد، تنظیم این فیلد خطا محسوب می‌شود.</li>
</ul>
<p>مقادیر معتبر:</p>
<ul>
<li>
<blockquote>
<p>=1s (غیرصفر). هیچ حد بالایی اعمال نمی‌شود.</p>
</blockquote>
</li>
</ul>
<p>راهنمای تنظیم:</p>
<ul>
<li>مقادیر کمتر، زمان لازم برای تلاش مجدد را در مواقعی که دستگاه‌ها آماده نیستند کاهش می‌دهند، اما اگر
درایورها معمولاً به زمان بیشتری برای گزارش آماده بودن نیاز داشته باشند، می‌توانند
نوسان (churn) را افزایش دهند.</li>
<li>پیش از کاهش این مهلت زمانی، معیارهای تأخیر زمان‌بند (مثلاً مدت PreBind در
<code>scheduler_framework_extension_point_duration_seconds</code>) و رفتار
آماده‌سازی درایور را بررسی کنید.</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `InterPodAffinityArgs`     {#kubescheduler-config-k8s-io-v1-InterPodAffinityArgs}
    


<p>InterPodAffinityArgs آرگومان‌های مورد استفاده برای پیکربندی افزونه InterPodAffinity را نگهداری می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>InterPodAffinityArgs</code></td></tr>
    
  
<tr><td><code>hardPodAffinityWeight</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>HardPodAffinityWeight وزن امتیازدهی برای پادهای موجودی است که
دارای affinity سخت منطبق با پاد ورودی هستند.</p>
</td>
</tr>
<tr><td><code>ignorePreferredTermsOfExistingPods</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>IgnorePreferredTermsOfExistingPods زمان‌بند را طوری پیکربندی می‌کند که هنگام امتیازدهی به نودهای کاندیدا،
قواعد affinity ترجیحی پادهای موجود را نادیده بگیرد، مگر آن‌که پاد ورودی دارای affinity میان پادی باشد.</p>
</td>
</tr>
</tbody>
</table>

## `KubeSchedulerConfiguration`     {#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration}
    


<p>KubeSchedulerConfiguration یک زمان‌بند را پیکربندی می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>KubeSchedulerConfiguration</code></td></tr>
    
  
<tr><td><code>parallelism</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>Parallelism میزان موازی‌سازی در الگوریتم‌های زمان‌بندی پادها را تعیین می‌کند. باید بزرگ‌تر از 0 باشد. پیش‌فرض 16 است.</p>
</td>
</tr>
<tr><td><code>leaderElection</code> <B>[الزامی]</B><br/>
<a href="#LeaderElectionConfiguration"><code>LeaderElectionConfiguration</code></a>
</td>
<td>
   <p>LeaderElection پیکربندی کلاینت انتخاب رهبر را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>clientConnection</code> <B>[الزامی]</B><br/>
<a href="#ClientConnectionConfiguration"><code>ClientConnectionConfiguration</code></a>
</td>
<td>
   <p>ClientConnection فایل kubeconfig و تنظیمات اتصال کلاینت را که
سرور پراکسی هنگام ارتباط با apiserver از آن‌ها استفاده می‌کند مشخص می‌کند.</p>
</td>
</tr>
<tr><td><code>DebuggingConfiguration</code> <B>[الزامی]</B><br/>
<a href="#DebuggingConfiguration"><code>DebuggingConfiguration</code></a>
</td>
<td>
   <p>DebuggingConfiguration پیکربندی ویژگی‌های مرتبط با اشکال‌زدایی را نگهداری می‌کند.
TODO: We might wanna make this a substruct like Debugging componentbaseconfigv1alpha1.DebuggingConfiguration</p>
</td>
</tr>
<tr><td><code>percentageOfNodesToScore</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>PercentageOfNodesToScore درصدی از کل نودهاست که پس از یافتن آن تعداد نود مناسب
برای اجرای یک پاد، زمان‌بند جست‌وجوی خود را برای یافتن نودهای مناسب بیشتر در
کلاستر متوقف می‌کند. این کار به بهبود کارایی زمان‌بند کمک می‌کند. زمان‌بند همواره می‌کوشد
دست‌کم «minFeasibleNodesToFind» نود مناسب را بیابد، صرف‌نظر از مقدار این پرچم.
مثال: اگر اندازه کلاستر 500 نود و مقدار این پرچم 30 باشد،
زمان‌بند به‌محض یافتن 150 نود مناسب، جست‌وجوی نودهای مناسب بیشتر را متوقف می‌کند.
وقتی مقدار 0 باشد، درصد پیش‌فرض (۵٪ تا ۵۰٪ بر اساس اندازه کلاستر) از
نودها امتیازدهی می‌شوند. این مقدار توسط PercentageOfNodesToScore در سطح پروفایل بازنویسی می‌شود.</p>
</td>
</tr>
<tr><td><code>podInitialBackoffSeconds</code> <B>[الزامی]</B><br/>
<code>int64</code>
</td>
<td>
   <p>PodInitialBackoffSeconds مقدار backoff اولیه برای پادهای غیرقابل زمان‌بندی است.
در صورت تعیین، باید بزرگ‌تر از 0 باشد. اگر این مقدار null باشد، از مقدار پیش‌فرض (1 ثانیه)
استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>podMaxBackoffSeconds</code> <B>[الزامی]</B><br/>
<code>int64</code>
</td>
<td>
   <p>PodMaxBackoffSeconds حداکثر backoff برای پادهای غیرقابل زمان‌بندی است.
در صورت تعیین، باید بزرگ‌تر از podInitialBackoffSeconds باشد. اگر این مقدار null باشد،
از مقدار پیش‌فرض (10 ثانیه) استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>profiles</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile"><code>[]KubeSchedulerProfile</code></a>
</td>
<td>
   <p>Profiles پروفایل‌های زمان‌بندی‌ای هستند که kube-scheduler از آن‌ها پشتیبانی می‌کند. پادها
می‌توانند با تنظیم نام زمان‌بند مرتبط، زمان‌بندی تحت یک پروفایل خاص را انتخاب کنند. پادهایی که
هیچ نام زمان‌بندی مشخص نمی‌کنند، در صورت وجود پروفایل «default-scheduler» در اینجا، با
آن پروفایل زمان‌بندی می‌شوند.</p>
</td>
</tr>
<tr><td><code>extenders</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-Extender"><code>[]Extender</code></a>
</td>
<td>
   <p>Extenders فهرست افزونه‌های توسعه‌دهنده زمان‌بند (extender) هستند که هر یک مقادیر نحوه ارتباط
با extender را نگهداری می‌کند. این extenderها میان همه پروفایل‌های زمان‌بند مشترک هستند.</p>
</td>
</tr>
<tr><td><code>delayCacheUntilActive</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>DelayCacheUntilActive مشخص می‌کند کش‌کردن چه زمانی آغاز شود. اگر این مقدار true باشد و انتخاب رهبر فعال باشد،
زمان‌بند تا زمانی که رهبر نشده باشد، از پر کردن کش‌های informer خودداری می‌کند. این کار
منجر به failover کندتر می‌شود، اما در عوض هنگام انتظار برای رهبر شدن مصرف حافظه کمتری دارد.
پیش‌فرض false است.</p>
</td>
</tr>
</tbody>
</table>

## `NodeAffinityArgs`     {#kubescheduler-config-k8s-io-v1-NodeAffinityArgs}
    


<p>NodeAffinityArgs آرگومان‌های پیکربندی افزونه NodeAffinity را نگهداری می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>NodeAffinityArgs</code></td></tr>
    
  
<tr><td><code>addedAffinity</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#nodeaffinity-v1-core"><code>core/v1.NodeAffinity</code></a>
</td>
<td>
   <p>AddedAffinity علاوه بر NodeAffinity مشخص‌شده در PodSpec، بر همه پادها اعمال می‌شود.
یعنی نودها باید هم AddedAffinity و
هم .spec.NodeAffinity را برآورده کنند. AddedAffinity به‌طور پیش‌فرض خالی است (همه نودها
منطبق هستند).
هنگام استفاده از AddedAffinity، برخی پادها که الزامات affinity منطبق با
یک نود مشخص دارند (مانند پادهای Daemonset) ممکن است غیرقابل زمان‌بندی باقی بمانند.</p>
</td>
</tr>
</tbody>
</table>

## `NodeResourcesBalancedAllocationArgs`     {#kubescheduler-config-k8s-io-v1-NodeResourcesBalancedAllocationArgs}
    


<p>NodeResourcesBalancedAllocationArgs آرگومان‌های مورد استفاده برای پیکربندی افزونه NodeResourcesBalancedAllocation را نگهداری می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>NodeResourcesBalancedAllocationArgs</code></td></tr>
    
  
<tr><td><code>resources</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-ResourceSpec"><code>[]ResourceSpec</code></a>
</td>
<td>
   <p>منابعی که باید مدیریت شوند؛ در صورت مشخص نشدن، پیش‌فرض «cpu» و «memory» است.</p>
</td>
</tr>
</tbody>
</table>

## `NodeResourcesFitArgs`     {#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs}
    


<p>NodeResourcesFitArgs آرگومان‌های مورد استفاده برای پیکربندی افزونه NodeResourcesFit را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>NodeResourcesFitArgs</code></td></tr>
    
  
<tr><td><code>ignoredResources</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>IgnoredResources فهرست منابعی است که فیلتر NodeResources fit
باید آن‌ها را نادیده بگیرد. این مورد بر امتیازدهی اعمال نمی‌شود.</p>
</td>
</tr>
<tr><td><code>ignoredResourceGroups</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>IgnoredResourceGroups فهرست گروه‌های منابعی را تعیین می‌کند که فیلتر NodeResources fit باید آن‌ها را نادیده بگیرد.
برای مثال، اگر گروه برابر [&quot;example.com&quot;] باشد، همه نام‌های منبعی که با
&quot;example.com&quot; شروع می‌شوند، مانند &quot;example.com/aaa&quot; و &quot;example.com/bbb&quot;، نادیده گرفته می‌شوند.
نام یک گروه منبع نمی‌تواند شامل '/' باشد. این مورد بر امتیازدهی اعمال نمی‌شود.</p>
</td>
</tr>
<tr><td><code>scoringStrategy</code> <B>[Required]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-ScoringStrategy"><code>ScoringStrategy</code></a>
</td>
<td>
   <p>ScoringStrategy راهبرد امتیازدهی منابع نود را انتخاب می‌کند.
راهبرد پیش‌فرض LeastAllocated با وزن برابر برای &quot;cpu&quot; و &quot;memory&quot; است.</p>
</td>
</tr>
</tbody>
</table>

## `PodTopologySpreadArgs`     {#kubescheduler-config-k8s-io-v1-PodTopologySpreadArgs}
    


<p>PodTopologySpreadArgs آرگومان‌های مورد استفاده برای پیکربندی افزونه PodTopologySpread را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>PodTopologySpreadArgs</code></td></tr>
    
  
<tr><td><code>defaultConstraints</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#topologyspreadconstraint-v1-core"><code>[]core/v1.TopologySpreadConstraint</code></a>
</td>
<td>
   <p>DefaultConstraints محدودیت‌های توزیع توپولوژی را تعریف می‌کند که بر
Podهایی اعمال می‌شوند که هیچ محدودیتی را در <code>pod.spec.topologySpreadConstraints</code> تعریف نکرده‌اند.
مقدار <code>.defaultConstraints[*].labelSelectors</code> باید خالی باشد، زیرا این مقادیر
از عضویت Pod در Serviceها، ReplicationControllerها،
ReplicaSetها یا StatefulSetها استنتاج می‌شوند.
هنگامی که خالی نباشد، مقدار .defaultingType باید &quot;List&quot; باشد.</p>
</td>
</tr>
<tr><td><code>defaultingType</code><br/>
<a href="#kubescheduler-config-k8s-io-v1-PodTopologySpreadConstraintsDefaulting"><code>PodTopologySpreadConstraintsDefaulting</code></a>
</td>
<td>
   <p>DefaultingType مشخص می‌کند که .defaultConstraints چگونه استنتاج شوند. می‌تواند یکی از
مقادیر &quot;System&quot; یا &quot;List&quot; باشد.</p>
<ul>
<li>&quot;System&quot;: از محدودیت‌های تعریف‌شده توسط کوبرنتیز استفاده می‌کند که Podها را بین
نودها و zoneها توزیع می‌کنند.</li>
<li>&quot;List&quot;: از محدودیت‌های تعریف‌شده در .defaultConstraints استفاده می‌کند.</li>
</ul>
<p>مقدار پیش‌فرض &quot;System&quot; است.</p>
</td>
</tr>
</tbody>
</table>

## `VolumeBindingArgs`     {#kubescheduler-config-k8s-io-v1-VolumeBindingArgs}
    


<p>VolumeBindingArgs آرگومان‌های مورد استفاده برای پیکربندی افزونه VolumeBinding را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubescheduler.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>VolumeBindingArgs</code></td></tr>
    
  
<tr><td><code>bindTimeoutSeconds</code> <B>[Required]</B><br/>
<code>int64</code>
</td>
<td>
   <p>BindTimeoutSeconds مهلت زمانی بر حسب ثانیه برای عملیات اتصال حجم (volume binding) است.
مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای عدم انتظار است.
اگر این مقدار nil باشد، از مقدار پیش‌فرض (600) استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>shape</code><br/>
<a href="#kubescheduler-config-k8s-io-v1-UtilizationShapePoint"><code>[]UtilizationShapePoint</code></a>
</td>
<td>
   <p>Shape نقاطی را مشخص می‌کند که شکل تابع امتیاز را تعریف می‌کنند؛ این تابع
برای امتیازدهی به نودها بر اساس میزان استفاده از PVهای تأمین‌شده به کار می‌رود.
میزان استفاده با تقسیم کل ذخیره‌سازی درخواستی Pod
بر ظرفیت کل PVهای مناسب روی هر نود محاسبه می‌شود.
هر نقطه شامل میزان استفاده (در بازه ۰ تا ۱۰۰) و امتیاز
متناظر آن (در بازه ۰ تا ۱۰) است. می‌توانید با تعیین
امتیازهای متفاوت برای مقادیر مختلف میزان استفاده، اولویت را تنظیم کنید.
نقاط شکل پیش‌فرض عبارت‌اند از:</p>
<ol>
<li>امتیاز ۱۰ برای میزان استفاده ۰</li>
<li>امتیاز ۰ برای میزان استفاده ۱۰۰
همه نقاط باید بر اساس میزان استفاده به‌صورت صعودی مرتب شوند.</li>
</ol>
</td>
</tr>
</tbody>
</table>

## `Extender`     {#kubescheduler-config-k8s-io-v1-Extender}
    

**Appears in:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)


<p>Extender پارامترهای مورد استفاده برای ارتباط با extender را نگه می‌دارد. اگر یک verb مشخص نشده یا خالی باشد،
فرض بر این است که extender تصمیم گرفته است آن افزونه را ارائه نکند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>urlPrefix</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>URLPrefix که extender در آن در دسترس است</p>
</td>
</tr>
<tr><td><code>filterVerb</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Verb مربوط به فراخوانی filter؛ در صورت عدم پشتیبانی خالی است. این verb هنگام ارسال فراخوانی filter به extender به URLPrefix افزوده می‌شود.</p>
</td>
</tr>
<tr><td><code>preemptVerb</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Verb مربوط به فراخوانی preempt؛ در صورت عدم پشتیبانی خالی است. این verb هنگام ارسال فراخوانی preempt به extender به URLPrefix افزوده می‌شود.</p>
</td>
</tr>
<tr><td><code>prioritizeVerb</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Verb مربوط به فراخوانی prioritize؛ در صورت عدم پشتیبانی خالی است. این verb هنگام ارسال فراخوانی prioritize به extender به URLPrefix افزوده می‌شود.</p>
</td>
</tr>
<tr><td><code>weight</code> <B>[Required]</B><br/>
<code>int64</code>
</td>
<td>
   <p>ضریب عددی برای امتیاز نودهایی که فراخوانی prioritize تولید می‌کند.
وزن باید یک عدد صحیح مثبت باشد</p>
</td>
</tr>
<tr><td><code>bindVerb</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Verb مربوط به فراخوانی bind؛ در صورت عدم پشتیبانی خالی است. این verb هنگام ارسال فراخوانی bind به extender به URLPrefix افزوده می‌شود.
اگر این متد توسط extender پیاده‌سازی شده باشد، مسئولیت اتصال Pod به apiserver بر عهده extender است. تنها یک extender
می‌تواند این تابع را پیاده‌سازی کند.</p>
</td>
</tr>
<tr><td><code>enableHTTPS</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>EnableHTTPS مشخص می‌کند که آیا برای ارتباط با extender باید از https استفاده شود یا خیر</p>
</td>
</tr>
<tr><td><code>tlsConfig</code> <B>[Required]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-ExtenderTLSConfig"><code>ExtenderTLSConfig</code></a>
</td>
<td>
   <p>TLSConfig پیکربندی امنیت لایه انتقال را مشخص می‌کند</p>
</td>
</tr>
<tr><td><code>httpTimeout</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HTTPTimeout مدت مهلت زمانی برای یک فراخوانی به extender را مشخص می‌کند. انقضای مهلت filter باعث شکست زمان‌بندی Pod می‌شود. انقضای مهلت
prioritize نادیده گرفته می‌شود و برای انتخاب نود از اولویت‌های k8s یا سایر extenderها استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>nodeCacheCapable</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>NodeCacheCapable مشخص می‌کند که extender قادر به کش کردن اطلاعات نود است،
بنابراین زمان‌بند باید تنها اطلاعات حداقلی درباره نودهای واجد شرایط را ارسال کند،
با این فرض که extender جزئیات کامل همه نودهای کلاستر را پیش‌تر کش کرده است</p>
</td>
</tr>
<tr><td><code>managedResources</code><br/>
<a href="#kubescheduler-config-k8s-io-v1-ExtenderManagedResource"><code>[]ExtenderManagedResource</code></a>
</td>
<td>
   <p>ManagedResources فهرستی از منابع توسعه‌یافته (extended resources) است که توسط
این extender مدیریت می‌شوند.</p>
<ul>
<li>یک Pod در مراحل Filter، Prioritize و Bind
(اگر extender مسئول bind باشد) تنها در صورتی به extender ارسال می‌شود که Pod دست‌کم
یکی از منابع توسعه‌یافته موجود در این فهرست را درخواست کرده باشد. اگر خالی یا مشخص‌نشده باشد،
همه Podها به این extender ارسال خواهند شد.</li>
<li>اگر IgnoredByScheduler برای یک منبع روی true تنظیم شده باشد، kube-scheduler
بررسی آن منبع را در predicateها نادیده می‌گیرد.</li>
</ul>
</td>
</tr>
<tr><td><code>ignorable</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>Ignorable مشخص می‌کند که آیا extender قابل چشم‌پوشی است یا خیر؛ یعنی زمان‌بندی نباید
هنگامی که extender خطا برمی‌گرداند یا در دسترس نیست، با شکست مواجه شود.</p>
</td>
</tr>
</tbody>
</table>

## `ExtenderManagedResource`     {#kubescheduler-config-k8s-io-v1-ExtenderManagedResource}
    

**Appears in:**

- [Extender](#kubescheduler-config-k8s-io-v1-Extender)


<p>ExtenderManagedResource آرگومان‌های منابع توسعه‌یافته‌ای را توصیف می‌کند که
توسط یک extender مدیریت می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام منبع توسعه‌یافته است.</p>
</td>
</tr>
<tr><td><code>ignoredByScheduler</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>IgnoredByScheduler مشخص می‌کند که آیا kube-scheduler باید هنگام اعمال predicateها
این منبع را نادیده بگیرد یا خیر.</p>
</td>
</tr>
</tbody>
</table>

## `ExtenderTLSConfig`     {#kubescheduler-config-k8s-io-v1-ExtenderTLSConfig}
    

**Appears in:**

- [Extender](#kubescheduler-config-k8s-io-v1-Extender)


<p>ExtenderTLSConfig شامل تنظیمات فعال‌سازی TLS با extender است</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>insecure</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>دسترسی به سرور بدون تأیید گواهی TLS انجام می‌شود. فقط برای آزمایش.</p>
</td>
</tr>
<tr><td><code>serverName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>ServerName برای SNI به سرور ارسال می‌شود و در کلاینت برای بررسی گواهی‌های
سرور به کار می‌رود. اگر ServerName خالی باشد، از نام میزبانی که برای ارتباط با
سرور استفاده شده است، استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>certFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>سرور احراز هویت با گواهی کلاینت TLS را الزامی می‌کند</p>
</td>
</tr>
<tr><td><code>keyFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>سرور احراز هویت با گواهی کلاینت TLS را الزامی می‌کند</p>
</td>
</tr>
<tr><td><code>caFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>گواهی‌های ریشه مورد اعتماد برای سرور</p>
</td>
</tr>
<tr><td><code>certData</code> <B>[Required]</B><br/>
<code>[]byte</code>
</td>
<td>
   <p>CertData بایت‌های رمزگذاری‌شده با PEM را نگه می‌دارد (که معمولاً از فایل گواهی کلاینت خوانده می‌شوند).
CertData بر CertFile اولویت دارد</p>
</td>
</tr>
<tr><td><code>keyData</code> <B>[Required]</B><br/>
<code>[]byte</code>
</td>
<td>
   <p>KeyData بایت‌های رمزگذاری‌شده با PEM را نگه می‌دارد (که معمولاً از فایل کلید گواهی کلاینت خوانده می‌شوند).
KeyData بر KeyFile اولویت دارد</p>
</td>
</tr>
<tr><td><code>caData</code> <B>[Required]</B><br/>
<code>[]byte</code>
</td>
<td>
   <p>CAData بایت‌های رمزگذاری‌شده با PEM را نگه می‌دارد (که معمولاً از بسته گواهی‌های ریشه خوانده می‌شوند).
CAData بر CAFile اولویت دارد</p>
</td>
</tr>
</tbody>
</table>

## `KubeSchedulerProfile`     {#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile}
    

**Appears in:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)


<p>KubeSchedulerProfile یک پروفایل زمان‌بندی است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>schedulerName</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>SchedulerName نام زمان‌بندی است که به این پروفایل مرتبط است.
اگر SchedulerName با مقدار &quot;spec.schedulerName&quot; در Pod مطابقت داشته باشد، آن Pod
با این پروفایل زمان‌بندی می‌شود.</p>
</td>
</tr>
<tr><td><code>percentageOfNodesToScore</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>PercentageOfNodesToScore درصدی از کل نودهاست که پس از یافتن آن تعداد نود مناسب برای اجرای یک Pod،
زمان‌بند جست‌وجو برای نودهای مناسب بیشتر در کلاستر را متوقف می‌کند. این کار به بهبود عملکرد زمان‌بند کمک می‌کند. زمان‌بند همواره می‌کوشد
دست‌کم &quot;minFeasibleNodesToFind&quot; نود مناسب را بیابد، صرف‌نظر از مقدار این فلگ.
مثال: اگر اندازه کلاستر ۵۰۰ نود و مقدار این فلگ ۳۰ باشد،
زمان‌بند پس از یافتن ۱۵۰ نود مناسب، جست‌وجو برای نودهای مناسب بیشتر را متوقف می‌کند.
وقتی مقدار ۰ باشد، درصد پیش‌فرض (۵٪ تا ۵۰٪ بسته به اندازه کلاستر) از
نودها امتیازدهی خواهند شد. این مقدار PercentageOfNodesToScore سراسری را بازنویسی می‌کند. اگر خالی باشد،
از PercentageOfNodesToScore سراسری استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>plugins</code> <B>[Required]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-Plugins"><code>Plugins</code></a>
</td>
<td>
   <p>Plugins مجموعه افزونه‌هایی را مشخص می‌کند که باید فعال یا غیرفعال شوند.
افزونه‌های فعال‌شده آن‌هایی هستند که باید علاوه بر افزونه‌های
پیش‌فرض فعال شوند. افزونه‌های غیرفعال‌شده هر یک از افزونه‌های پیش‌فرض هستند که
باید غیرفعال شوند.
هنگامی که برای یک نقطه توسعه (extension point) هیچ افزونه فعال یا غیرفعالی مشخص نشده باشد،
در صورت وجود، افزونه‌های پیش‌فرض آن نقطه توسعه استفاده خواهند شد.
اگر یک افزونه QueueSort مشخص شود، همان افزونه QueueSort و همان
PluginConfig باید برای همه پروفایل‌ها مشخص شود.</p>
</td>
</tr>
<tr><td><code>pluginConfig</code> <B>[Required]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginConfig"><code>[]PluginConfig</code></a>
</td>
<td>
   <p>PluginConfig مجموعه‌ای اختیاری از آرگومان‌های سفارشی افزونه برای هر افزونه است.
حذف آرگومان‌های پیکربندی یک افزونه معادل استفاده از پیکربندی پیش‌فرض
آن افزونه است.</p>
</td>
</tr>
</tbody>
</table>

## `Plugin`     {#kubescheduler-config-k8s-io-v1-Plugin}
    

**Appears in:**

- [PluginSet](#kubescheduler-config-k8s-io-v1-PluginSet)


<p>Plugin نام یک افزونه و در صورت کاربرد، وزن آن را مشخص می‌کند. وزن فقط برای افزونه‌های Score و PlacementScore استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام افزونه را تعریف می‌کند</p>
</td>
</tr>
<tr><td><code>weight</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>Weight وزن افزونه را تعریف می‌کند و فقط برای افزونه‌های Score و PlacementScore استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `PluginConfig`     {#kubescheduler-config-k8s-io-v1-PluginConfig}
    

**Appears in:**

- [KubeSchedulerProfile](#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile)


<p>PluginConfig آرگومان‌هایی را مشخص می‌کند که باید هنگام مقداردهی اولیه به یک افزونه ارسال شوند.
افزونه‌ای که در چند نقطه توسعه فراخوانی می‌شود، یک‌بار مقداردهی اولیه می‌شود. Args می‌تواند ساختار دلخواه داشته باشد.
پردازش این Args بر عهده افزونه است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام افزونه‌ای را که پیکربندی می‌شود تعریف می‌کند</p>
</td>
</tr>
<tr><td><code>args</code> <B>[Required]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension"><code>k8s.io/apimachinery/pkg/runtime.RawExtension</code></a>
</td>
<td>
   <p>Args آرگومان‌هایی را تعریف می‌کند که هنگام مقداردهی اولیه به افزونه‌ها ارسال می‌شوند. Args می‌تواند ساختار دلخواه داشته باشد.</p>
</td>
</tr>
</tbody>
</table>

## `PluginSet`     {#kubescheduler-config-k8s-io-v1-PluginSet}
    

**Appears in:**

- [Plugins](#kubescheduler-config-k8s-io-v1-Plugins)


<p>PluginSet افزونه‌های فعال و غیرفعال را برای یک نقطه توسعه مشخص می‌کند.
اگر یک آرایه خالی، فاقد مقدار یا nil باشد، افزونه‌های پیش‌فرض در آن نقطه توسعه استفاده خواهند شد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>enabled</code> <B>[Required]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-Plugin"><code>[]Plugin</code></a>
</td>
<td>
   <p>Enabled افزونه‌هایی را مشخص می‌کند که باید علاوه بر افزونه‌های پیش‌فرض فعال شوند.
اگر افزونه پیش‌فرض نیز در فایل پیکربندی زمان‌بند تنظیم شده باشد، وزن افزونه
متناسب با آن بازنویسی می‌شود.
این افزونه‌ها پس از افزونه‌های پیش‌فرض و به همان ترتیبی که در اینجا مشخص شده است فراخوانی می‌شوند.</p>
</td>
</tr>
<tr><td><code>disabled</code> <B>[Required]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-Plugin"><code>[]Plugin</code></a>
</td>
<td>
   <p>Disabled افزونه‌های پیش‌فرضی را مشخص می‌کند که باید غیرفعال شوند.
هنگامی که لازم است همه افزونه‌های پیش‌فرض غیرفعال شوند، باید آرایه‌ای تنها شامل یک &quot;*&quot; ارائه شود.</p>
</td>
</tr>
</tbody>
</table>

## `Plugins`     {#kubescheduler-config-k8s-io-v1-Plugins}
    

**ظاهر شده در:**

- [KubeSchedulerProfile](#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile)


<p>Plugins شامل چندین نقطه توسعه (extension point) است. در صورت مشخص‌شدن، فهرست افزونه‌ها برای
یک نقطه توسعه مشخص، تنها افزونه‌هایی است که فعال می‌شوند. اگر یک نقطه توسعه
در پیکربندی حذف شود، مجموعه پیش‌فرض افزونه‌ها برای آن نقطه توسعه استفاده می‌شود.
افزونه‌های فعال‌شده به همان ترتیبی که در اینجا مشخص شده است و پس از افزونه‌های پیش‌فرض فراخوانی می‌شوند. اگر لازم باشد
پیش از افزونه‌های پیش‌فرض فراخوانی شوند، باید افزونه‌های پیش‌فرض غیرفعال شوند و دوباره در اینجا با ترتیب دلخواه فعال شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>preEnqueue</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PreEnqueue فهرستی از افزونه‌هاست که باید پیش از افزودن Podها به صف زمان‌بندی فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>queueSort</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>QueueSort فهرستی از افزونه‌هاست که باید هنگام مرتب‌سازی Podها در صف زمان‌بندی فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>preFilter</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PreFilter فهرستی از افزونه‌هاست که باید در نقطه توسعه &quot;PreFilter&quot; چارچوب زمان‌بندی فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>filter</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>Filter فهرستی از افزونه‌هاست که باید هنگام حذف نودهایی که نمی‌توانند Pod را اجرا کنند، فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>postFilter</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PostFilter فهرستی از افزونه‌هاست که پس از مرحله فیلتر کردن فراخوانی می‌شوند، اما فقط زمانی که هیچ نود مناسبی برای Pod یافت نشده باشد.</p>
</td>
</tr>
<tr><td><code>preScore</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PreScore فهرستی از افزونه‌هاست که پیش از امتیازدهی فراخوانی می‌شوند.</p>
</td>
</tr>
<tr><td><code>score</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>Score فهرستی از افزونه‌هاست که باید هنگام رتبه‌بندی نودهایی که از مرحله فیلتر کردن گذشته‌اند، فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>reserve</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>Reserve فهرستی از افزونه‌هاست که هنگام رزرو کردن یا آزادسازی منابع
پس از اختصاص یک نود برای اجرای Pod فراخوانی می‌شوند.</p>
</td>
</tr>
<tr><td><code>permit</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>Permit فهرستی از افزونه‌هاست که اتصال (binding) یک Pod را کنترل می‌کنند. این افزونه‌ها می‌توانند از اتصال یک Pod جلوگیری کنند یا آن را به تأخیر بیندازند.</p>
</td>
</tr>
<tr><td><code>preBind</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PreBind فهرستی از افزونه‌هاست که باید پیش از اتصال یک Pod فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>bind</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>Bind فهرستی از افزونه‌هاست که باید در نقطه توسعه &quot;Bind&quot; چارچوب زمان‌بندی فراخوانی شوند.
زمان‌بند این افزونه‌ها را به ترتیب فراخوانی می‌کند. به‌محض اینکه یکی از آن‌ها موفقیت را برگرداند، زمان‌بند از بقیه این افزونه‌ها صرف‌نظر می‌کند.</p>
</td>
</tr>
<tr><td><code>postBind</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PostBind فهرستی از افزونه‌هاست که باید پس از اتصال موفقیت‌آمیز یک Pod فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>multiPoint</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>MultiPoint یک بخش پیکربندی ساده‌شده برای فعال‌سازی افزونه‌ها در تمام نقاط توسعه معتبر است.
افزونه‌هایی که از طریق MultiPoint فعال شوند، به‌طور خودکار برای هر یک از نقاط توسعه‌ای که
افزونه پیاده‌سازی کرده است ثبت می‌شوند. غیرفعال کردن یک افزونه از طریق MultiPoint این رفتار را غیرفعال می‌کند.
غیرفعال کردن &quot;*&quot; از طریق MultiPoint نیز به همین صورت است (هیچ افزونه پیش‌فرضی به‌طور خودکار ثبت نخواهد شد).
افزونه‌ها همچنان می‌توانند از طریق نقاط توسعه مجزای خود غیرفعال شوند.</p>
<p>از نظر اولویت، پیکربندی افزونه از این سلسله‌مراتب پایه پیروی می‌کند:</p>
<ol>
<li>نقاط توسعه مشخص</li>
<li>افزونه‌های MultiPoint که صریحاً پیکربندی شده‌اند</li>
<li>مجموعه افزونه‌های پیش‌فرض، به‌عنوان افزونه‌های MultiPoint
این بدان معناست که افزونه‌ای با اولویت بالاتر ابتدا اجرا می‌شود و هر تنظیمی را در MultiPoint بازنویسی می‌کند.
افزونه‌هایی که کاربر صریحاً پیکربندی کرده است نیز اولویت بالاتری نسبت به افزونه‌های پیش‌فرض دارند.
در این سلسله‌مراتب، تنظیم Enabled بر Disabled اولویت دارد. برای مثال، اگر یک افزونه
هم در <code>multiPoint.Enabled</code> و هم در <code>multiPoint.Disabled</code> تنظیم شده باشد، آن افزونه فعال خواهد شد. به همین ترتیب،
قرار دادن <code>multiPoint.Disabled = '*'</code> و <code>multiPoint.Enabled = pluginA</code> همچنان آن افزونه خاص را
از طریق MultiPoint ثبت می‌کند. این رفتار مانند سایر پیکربندی‌های نقاط توسعه است.</li>
</ol>
</td>
</tr>
<tr><td><code>placementGenerate</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PlacementGenerate فهرستی از افزونه‌هاست که باید در چرخه زمان‌بندی گروه Pod و هنگام تعیین جایگذاری‌ها (placements) برای یک گروه Pod فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>placementScore</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PlacementScore فهرستی از افزونه‌هاست که باید در چرخه زمان‌بندی بار کاری و هنگام رتبه‌بندی تخصیص‌های گروه Pod فراخوانی شوند.</p>
</td>
</tr>
<tr><td><code>podGroupPostFilter</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-PluginSet"><code>PluginSet</code></a>
</td>
<td>
   <p>PodGroupPostFilter فهرستی از افزونه‌هاست که پس از مرحله زمان‌بندی بار کاری فراخوانی می‌شوند،
اما فقط زمانی که PodGroup قابل زمان‌بندی نباشد (معادل PostFilter برای Podهای منفرد).</p>
</td>
</tr>
</tbody>
</table>

## `PodTopologySpreadConstraintsDefaulting`     {#kubescheduler-config-k8s-io-v1-PodTopologySpreadConstraintsDefaulting}
    
(نام مستعار برای `string`)

**ظاهر شده در:**

- [PodTopologySpreadArgs](#kubescheduler-config-k8s-io-v1-PodTopologySpreadArgs)


<p>PodTopologySpreadConstraintsDefaulting تعیین می‌کند که محدودیت‌های پیش‌فرض
برای افزونه PodTopologySpread چگونه تنظیم شوند.</p>




## `RequestedToCapacityRatioParam`     {#kubescheduler-config-k8s-io-v1-RequestedToCapacityRatioParam}
    

**ظاهر شده در:**

- [ScoringStrategy](#kubescheduler-config-k8s-io-v1-ScoringStrategy)


<p>RequestedToCapacityRatioParam پارامترهای RequestedToCapacityRatio را تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>shape</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-UtilizationShapePoint"><code>[]UtilizationShapePoint</code></a>
</td>
<td>
   <p>Shape فهرستی از نقاط است که شکل تابع امتیازدهی را تعریف می‌کنند.</p>
</td>
</tr>
</tbody>
</table>

## `ResourceSpec`     {#kubescheduler-config-k8s-io-v1-ResourceSpec}
    

**ظاهر شده در:**

- [NodeResourcesBalancedAllocationArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesBalancedAllocationArgs)

- [ScoringStrategy](#kubescheduler-config-k8s-io-v1-ScoringStrategy)


<p>ResourceSpec یک منبع واحد را نمایش می‌دهد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام منبع.</p>
</td>
</tr>
<tr><td><code>weight</code> <B>[الزامی]</B><br/>
<code>int64</code>
</td>
<td>
   <p>وزن منبع.</p>
</td>
</tr>
</tbody>
</table>

## `ScoringStrategy`     {#kubescheduler-config-k8s-io-v1-ScoringStrategy}
    

**ظاهر شده در:**

- [NodeResourcesFitArgs](#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs)


<p>ScoringStrategy نوع راهبرد امتیازدهی (ScoringStrategyType) را برای افزونه منابع نود تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-ScoringStrategyType"><code>ScoringStrategyType</code></a>
</td>
<td>
   <p>Type مشخص می‌کند کدام راهبرد اجرا شود.</p>
</td>
</tr>
<tr><td><code>resources</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-ResourceSpec"><code>[]ResourceSpec</code></a>
</td>
<td>
   <p>منابعی که هنگام امتیازدهی در نظر گرفته می‌شوند.
مجموعه منابع پیش‌فرض شامل &quot;cpu&quot; و &quot;memory&quot; با وزن برابر است.
وزن‌های مجاز از ۱ تا ۱۰۰ هستند.
اگر وزن مشخص نشود یا صریحاً روی ۰ تنظیم شود، مقدار پیش‌فرض آن ۱ است.</p>
</td>
</tr>
<tr><td><code>requestedToCapacityRatio</code> <B>[الزامی]</B><br/>
<a href="#kubescheduler-config-k8s-io-v1-RequestedToCapacityRatioParam"><code>RequestedToCapacityRatioParam</code></a>
</td>
<td>
   <p>آرگومان‌های مختص راهبرد RequestedToCapacityRatio.</p>
</td>
</tr>
</tbody>
</table>

## `ScoringStrategyType`     {#kubescheduler-config-k8s-io-v1-ScoringStrategyType}
    
(نام مستعار برای `string`)

**ظاهر شده در:**

- [ScoringStrategy](#kubescheduler-config-k8s-io-v1-ScoringStrategy)


<p>ScoringStrategyType نوع راهبرد امتیازدهی است که در افزونه NodeResourcesFit استفاده می‌شود.</p>




## `UtilizationShapePoint`     {#kubescheduler-config-k8s-io-v1-UtilizationShapePoint}
    

**ظاهر شده در:**

- [VolumeBindingArgs](#kubescheduler-config-k8s-io-v1-VolumeBindingArgs)

- [RequestedToCapacityRatioParam](#kubescheduler-config-k8s-io-v1-RequestedToCapacityRatioParam)


<p>UtilizationShapePoint یک نقطه واحد از شکل تابع اولویت را نمایش می‌دهد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>utilization</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>میزان استفاده (محور x). مقادیر معتبر ۰ تا ۱۰۰ هستند. نودی که کاملاً مورد استفاده قرار گرفته باشد، به ۱۰۰ نگاشت می‌شود.</p>
</td>
</tr>
<tr><td><code>score</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>امتیازی که به میزان استفاده داده‌شده اختصاص می‌یابد (محور y). مقادیر معتبر ۰ تا ۱۰ هستند.</p>
</td>
</tr>
</tbody>
</table>
