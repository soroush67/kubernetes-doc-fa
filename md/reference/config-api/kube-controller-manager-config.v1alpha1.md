---
title: پیکربندی kube-controller-manager (v1alpha1)
content_type: tool-reference
package: kubecontrollermanager.config.k8s.io/v1alpha1
auto_generated: true
---


## انواع منابع {#resource-types}


- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)
- [LeaderMigrationConfiguration](#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration)
- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)
  
    
    

## `ClientConnectionConfiguration`     {#ClientConnectionConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

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
   <p>acceptContentTypes هدر Accept را که کلاینت‌ها هنگام اتصال به یک سرور ارسال می‌کنند تعریف می‌کند و مقدار پیش‌فرض
'application/json' را بازنویسی می‌کند. این فیلد تمام اتصال‌هایی را که یک کلاینت مشخص به سرور برقرار می‌کند کنترل می‌کند.</p>
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
   <p>qps تعداد کوئری‌های مجاز در هر ثانیه برای این اتصال را کنترل می‌کند.</p>
</td>
</tr>
<tr><td><code>burst</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>burst در صورتی که کلاینت از نرخ مجاز خود فراتر برود، اجازه می‌دهد کوئری‌های اضافی انباشته شوند.</p>
</td>
</tr>
</tbody>
</table>

## `DebuggingConfiguration`     {#DebuggingConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>DebuggingConfiguration پیکربندی ویژگی‌های مرتبط با اشکال‌زدایی (Debugging) را نگه می‌دارد.</p>


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
enableProfiling برابر true باشد، پروفایل‌گیری مسدودسازی (block profiling) را فعال می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `LeaderElectionConfiguration`     {#LeaderElectionConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [KubeSchedulerConfiguration](#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>LeaderElectionConfiguration پیکربندی کلاینت‌های انتخاب رهبر (leader election)
را برای مؤلفه‌هایی تعریف می‌کند که می‌توانند با فعال بودن انتخاب رهبر اجرا شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>leaderElect</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>leaderElect باعث می‌شود یک کلاینت انتخاب رهبر پیش از اجرای حلقه اصلی، رهبری را به دست آورد.
هنگام اجرای مؤلفه‌های تکثیرشده برای دسترس‌پذیری بالا، این گزینه را فعال کنید.</p>
</td>
</tr>
<tr><td><code>leaseDuration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>leaseDuration مدت زمانی است که کاندیداهای غیررهبر، پس از مشاهده تمدید رهبری،
منتظر می‌مانند تا برای به دست آوردن رهبری یک جایگاه رهبری که اشغال شده اما تمدید نشده است اقدام کنند.
این مقدار در عمل بیشترین مدت زمانی است که یک رهبر می‌تواند متوقف باشد تا
کاندیدای دیگری جایگزین او شود. این فیلد فقط زمانی کاربرد دارد که انتخاب رهبر
فعال باشد.</p>
</td>
</tr>
<tr><td><code>renewDeadline</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>renewDeadline فاصله زمانی بین تلاش‌های رهبر فعلی (acting master) برای
تمدید جایگاه رهبری است، پیش از آنکه از رهبری دست بکشد. این مقدار باید کمتر
از مدت lease یا برابر با آن باشد. این فیلد فقط زمانی کاربرد دارد که انتخاب
رهبر فعال باشد.</p>
</td>
</tr>
<tr><td><code>retryPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>retryPeriod مدت زمانی است که کلاینت‌ها باید بین تلاش‌های کسب و تمدید رهبری
منتظر بمانند. این فیلد فقط زمانی کاربرد دارد که
انتخاب رهبر فعال باشد.</p>
</td>
</tr>
<tr><td><code>resourceLock</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceLock نوع آبجکت منبعی را مشخص می‌کند که برای قفل‌کردن
در چرخه‌های انتخاب رهبر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>resourceName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName نام آبجکت منبعی را مشخص می‌کند که برای قفل‌کردن
در چرخه‌های انتخاب رهبر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>resourceNamespace</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resourceName فضای نام (namespace) آبجکت منبعی را مشخص می‌کند که برای قفل‌کردن
در چرخه‌های انتخاب رهبر استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `NodeControllerConfiguration`     {#NodeControllerConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)


<p>NodeControllerConfiguration شامل عناصری است که NodeController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentNodeSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentNodeSyncs تعداد workerهایی است که
نودها را به‌صورت همزمان همگام‌سازی می‌کنند.</p>
</td>
</tr>
<tr><td><code>ConcurrentNodeStatusUpdates</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentNodeStatusUpdates تعداد workerهایی است که
وضعیت نودها را به‌صورت همزمان به‌روزرسانی می‌کنند.
اگر مشخص نشده باشد یا برابر 0 باشد، به‌جای آن از ConcurrentNodeSyncs استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `ServiceControllerConfiguration`     {#ServiceControllerConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ServiceControllerConfiguration شامل عناصری است که ServiceController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentServiceSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentServiceSyncs تعداد سرویس‌هایی است که
مجاز به همگام‌سازی همزمان هستند. عدد بزرگ‌تر = مدیریت پاسخگوتر سرویس،
اما بار بیشتر روی CPU (و شبکه).</p>
</td>
</tr>
</tbody>
</table>
  

## `CloudControllerManagerConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration}
    


<p>CloudControllerManagerConfiguration شامل عناصری است که cloud-controller manager را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>cloudcontrollermanager.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>CloudControllerManagerConfiguration</code></td></tr>
    
  
<tr><td><code>Generic</code> <B>[الزامی]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration"><code>GenericControllerManagerConfiguration</code></a>
</td>
<td>
   <p>Generic پیکربندی یک controller-manager عمومی را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>KubeCloudShared</code> <B>[الزامی]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration"><code>KubeCloudSharedConfiguration</code></a>
</td>
<td>
   <p>KubeCloudSharedConfiguration پیکربندی ویژگی‌های مشترک را،
هم در cloud controller manager و هم در kube-controller manager، نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>NodeController</code> <B>[الزامی]</B><br/>
<a href="#NodeControllerConfiguration"><code>NodeControllerConfiguration</code></a>
</td>
<td>
   <p>NodeController پیکربندی ویژگی‌های مرتبط با کنترل‌کننده نود
را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>NodeLifecycleController</code> <B>[الزامی]</B><br/>
<code>k8s.io/cloud-provider/controllers/nodelifecycle/config/v1alpha1.NodeLifecycleControllerConfiguration</code>
</td>
<td>
   <p>NodeLifecycleController پیکربندی ویژگی‌های مرتبط با کنترل‌کننده چرخه عمر نود
را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>ServiceController</code> <B>[الزامی]</B><br/>
<a href="#ServiceControllerConfiguration"><code>ServiceControllerConfiguration</code></a>
</td>
<td>
   <p>ServiceControllerConfiguration پیکربندی ویژگی‌های مرتبط با ServiceController
را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>NodeStatusUpdateFrequency</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>NodeStatusUpdateFrequency فرکانسی است که کنترل‌کننده وضعیت نودها را با آن به‌روزرسانی می‌کند.</p>
</td>
</tr>
<tr><td><code>Webhook</code> <B>[الزامی]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-WebhookConfiguration"><code>WebhookConfiguration</code></a>
</td>
<td>
   <p>Webhook پیکربندی webhookهای میزبانی‌شده توسط cloud-controller-manager است.</p>
</td>
</tr>
</tbody>
</table>

## `CloudProviderConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudProviderConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [KubeCloudSharedConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration)


<p>CloudProviderConfiguration عمدتاً شامل عناصر مربوط به ارائه‌دهنده ابری (cloud provider) است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>Name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name ارائه‌دهنده سرویس‌های ابری است.</p>
</td>
</tr>
<tr><td><code>CloudConfigFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>cloudConfigFile مسیر فایل پیکربندی ارائه‌دهنده ابری است.</p>
</td>
</tr>
</tbody>
</table>

## `KubeCloudSharedConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>KubeCloudSharedConfiguration شامل عناصری است که میان kube-controller manager
و cloud-controller manager مشترک هستند، اما جزو genericconfig نیستند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>CloudProvider</code> <B>[الزامی]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudProviderConfiguration"><code>CloudProviderConfiguration</code></a>
</td>
<td>
   <p>CloudProviderConfiguration پیکربندی ویژگی‌های مرتبط با CloudProvider را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>ExternalCloudVolumePlugin</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>externalCloudVolumePlugin افزونه‌ای را مشخص می‌کند که هنگامی که cloudProvider برابر &quot;external&quot; است باید استفاده شود.
در حال حاضر ارائه‌دهندگان ابری موجود در مخزن (in repo) از آن برای مدیریت نود و حجم (volume) در KCM استفاده می‌کنند.</p>
</td>
</tr>
<tr><td><code>UseServiceAccountCredentials</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>useServiceAccountCredentials مشخص می‌کند که آیا کنترل‌کننده‌ها باید با
اعتبارنامه‌های جداگانه service account اجرا شوند یا خیر.</p>
</td>
</tr>
<tr><td><code>AllowUntaggedCloud</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>اجرا با نمونه‌های ابری بدون برچسب (untagged)</p>
</td>
</tr>
<tr><td><code>RouteReconciliationPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>routeReconciliationPeriod دوره زمانی تطبیق (reconcile) مسیرهایی است که ارائه‌دهنده ابری برای نودها ایجاد کرده است.</p>
</td>
</tr>
<tr><td><code>ClusterName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterName پیشوند نمونه‌ها (instance prefix) برای کلاستر است.</p>
</td>
</tr>
<tr><td><code>ClusterCIDR</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterCIDR محدوده CIDR برای Podها در کلاستر است.</p>
</td>
</tr>
<tr><td><code>AllocateNodeCIDRs</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>AllocateNodeCIDRs امکان تخصیص CIDRها برای Podها را فراهم می‌کند و در صورتی که
ConfigureCloudRoutes برابر true باشد، امکان تنظیم آن‌ها روی ارائه‌دهنده ابری را نیز فراهم می‌کند.</p>
</td>
</tr>
<tr><td><code>CIDRAllocatorType</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>CIDRAllocatorType تعیین می‌کند از چه نوع تخصیص‌دهنده CIDR برای Pod استفاده شود.</p>
</td>
</tr>
<tr><td><code>ConfigureCloudRoutes</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>configureCloudRoutes باعث می‌شود CIDRهای تخصیص‌یافته با allocateNodeCIDRs
روی ارائه‌دهنده ابری پیکربندی شوند.</p>
</td>
</tr>
<tr><td><code>NodeSyncPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeSyncPeriod دوره زمانی همگام‌سازی نودها از cloudprovider است. دوره‌های طولانی‌تر
باعث کاهش تعداد فراخوانی‌ها به ارائه‌دهنده ابری می‌شوند، اما ممکن است افزودن
نودهای جدید به کلاستر را به تأخیر بیندازند.</p>
</td>
</tr>
</tbody>
</table>

## `WebhookConfiguration`     {#cloudcontrollermanager-config-k8s-io-v1alpha1-WebhookConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)


<p>WebhookConfiguration شامل پیکربندی مربوط به
webhookهای میزبانی‌شده توسط cloud-controller-manager است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>Webhooks</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>Webhooks فهرست webhookهایی است که باید فعال یا غیرفعال شوند.
'*' به معنای &quot;همه webhookهایی که به‌طور پیش‌فرض فعال هستند&quot; است.
'foo' به معنای &quot;فعال‌کردن 'foo'&quot; است.
'-foo' به معنای &quot;غیرفعال‌کردن 'foo'&quot; است.
نخستین مورد برای یک نام مشخص برنده می‌شود.</p>
</td>
</tr>
</tbody>
</table>
  
  

## `LeaderMigrationConfiguration`     {#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [GenericControllerManagerConfiguration](#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration)


<p>LeaderMigrationConfiguration پیکربندی نسخه‌بندی‌شده برای تمام قفل‌های رهبر در حال مهاجرت را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>controllermanager.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>LeaderMigrationConfiguration</code></td></tr>
    
  
<tr><td><code>leaderName</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>LeaderName نام منبع انتخاب رهبر است که از مهاجرت محافظت می‌کند.
برای مثال 1-20-KCM-to-1-21-CCM</p>
</td>
</tr>
<tr><td><code>resourceLock</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>ResourceLock نوع آبجکت منبعی را مشخص می‌کند که برای قفل‌کردن استفاده می‌شود.
باید &quot;leases&quot; یا &quot;endpoints&quot; باشد.</p>
</td>
</tr>
<tr><td><code>controllerLeaders</code> <B>[الزامی]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-ControllerLeaderConfiguration"><code>[]ControllerLeaderConfiguration</code></a>
</td>
<td>
   <p>ControllerLeaders شامل فهرستی از پیکربندی‌های قفل رهبر در حال مهاجرت است.</p>
</td>
</tr>
</tbody>
</table>

## `ControllerLeaderConfiguration`     {#controllermanager-config-k8s-io-v1alpha1-ControllerLeaderConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [LeaderMigrationConfiguration](#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration)


<p>ControllerLeaderConfiguration پیکربندی یک قفل رهبر در حال مهاجرت را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Name نام کنترل‌کننده‌ای است که در حال مهاجرت است.
برای مثال service-controller، route-controller، cloud-node-controller و غیره</p>
</td>
</tr>
<tr><td><code>component</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Component نام مؤلفه‌ای است که کنترل‌کننده باید در آن اجرا شود.
برای مثال kube-controller-manager، cloud-controller-manager و غیره
یا '*' به این معنا که کنترل‌کننده می‌تواند تحت هر مؤلفه‌ای که در مهاجرت مشارکت دارد اجرا شود.</p>
</td>
</tr>
</tbody>
</table>

## `GenericControllerManagerConfiguration`     {#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration}
    

**در این بخش‌ها ظاهر می‌شود:**

- [CloudControllerManagerConfiguration](#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>GenericControllerManagerConfiguration پیکربندی یک controller-manager عمومی را نگه می‌دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>Port</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>port درگاهی است که سرویس http مربوط به controller-manager روی آن اجرا می‌شود.</p>
</td>
</tr>
<tr><td><code>Address</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>address آدرس IP است که سرویس روی آن ارائه می‌شود (برای همه رابط‌ها روی 0.0.0.0 تنظیم کنید).</p>
</td>
</tr>
<tr><td><code>MinResyncPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>minResyncPeriod دوره همگام‌سازی مجدد (resync) در reflectorها است؛ مقدار آن به‌صورت تصادفی بین
minResyncPeriod و 2*minResyncPeriod خواهد بود.</p>
</td>
</tr>
<tr><td><code>ClientConnection</code> <B>[الزامی]</B><br/>
<a href="#ClientConnectionConfiguration"><code>ClientConnectionConfiguration</code></a>
</td>
<td>
   <p>ClientConnection فایل kubeconfig و تنظیمات اتصال کلاینت را مشخص می‌کند
که سرور پراکسی هنگام ارتباط با apiserver از آن‌ها استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>ControllerStartInterval</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>مدت زمانی که باید بین راه‌اندازی controller managerها منتظر ماند</p>
</td>
</tr>
<tr><td><code>LeaderElection</code> <B>[الزامی]</B><br/>
<a href="#LeaderElectionConfiguration"><code>LeaderElectionConfiguration</code></a>
</td>
<td>
   <p>leaderElection پیکربندی کلاینت انتخاب رهبر را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>Controllers</code> <B>[الزامی]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>Controllers فهرست کنترل‌کننده‌هایی است که باید فعال یا غیرفعال شوند.
'*' به معنای &quot;همه کنترل‌کننده‌هایی که به‌طور پیش‌فرض فعال هستند&quot; است.
'foo' به معنای &quot;فعال‌کردن 'foo'&quot; است.
'-foo' به معنای &quot;غیرفعال‌کردن 'foo'&quot; است.
نخستین مورد برای یک نام مشخص برنده می‌شود.</p>
</td>
</tr>
<tr><td><code>Debugging</code> <B>[الزامی]</B><br/>
<a href="#DebuggingConfiguration"><code>DebuggingConfiguration</code></a>
</td>
<td>
   <p>DebuggingConfiguration پیکربندی ویژگی‌های مرتبط با اشکال‌زدایی (Debugging) را نگه می‌دارد.</p>
</td>
</tr>
<tr><td><code>LeaderMigrationEnabled</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>LeaderMigrationEnabled مشخص می‌کند که آیا Leader Migration باید برای controller manager فعال باشد یا خیر.</p>
</td>
</tr>
<tr><td><code>LeaderMigration</code> <B>[الزامی]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration"><code>LeaderMigrationConfiguration</code></a>
</td>
<td>
   <p>LeaderMigration پیکربندی Leader Migration را نگه می‌دارد.</p>
</td>
</tr>
</tbody>
</table>

## `KubeControllerManagerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration}
    


<p>KubeControllerManagerConfiguration شامل عناصری است که kube-controller manager را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubecontrollermanager.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>KubeControllerManagerConfiguration</code></td></tr>
    
  
<tr><td><code>Generic</code> <B>[الزامی]</B><br/>
<a href="#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration"><code>GenericControllerManagerConfiguration</code></a>
</td>
<td>
   <p>Generic پیکربندی یک controller-manager عمومی را در بر دارد.</p>
</td>
</tr>
<tr><td><code>KubeCloudShared</code> <B>[الزامی]</B><br/>
<a href="#cloudcontrollermanager-config-k8s-io-v1alpha1-KubeCloudSharedConfiguration"><code>KubeCloudSharedConfiguration</code></a>
</td>
<td>
   <p>KubeCloudSharedConfiguration پیکربندی قابلیت‌های مشترک را، هم برای cloud controller manager
و هم برای kube-controller manager، در بر دارد.</p>
</td>
</tr>
<tr><td><code>AttachDetachController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-AttachDetachControllerConfiguration"><code>AttachDetachControllerConfiguration</code></a>
</td>
<td>
   <p>AttachDetachControllerConfiguration پیکربندی قابلیت‌های مرتبط با
AttachDetachController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>CSRSigningController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningControllerConfiguration"><code>CSRSigningControllerConfiguration</code></a>
</td>
<td>
   <p>CSRSigningControllerConfiguration پیکربندی قابلیت‌های مرتبط با
CSRSigningController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>DaemonSetController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DaemonSetControllerConfiguration"><code>DaemonSetControllerConfiguration</code></a>
</td>
<td>
   <p>DaemonSetControllerConfiguration پیکربندی قابلیت‌های مرتبط با DaemonSetController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>DeploymentController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DeploymentControllerConfiguration"><code>DeploymentControllerConfiguration</code></a>
</td>
<td>
   <p>DeploymentControllerConfiguration پیکربندی قابلیت‌های مرتبط با
DeploymentController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>DisruptionController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DisruptionControllerConfiguration"><code>DisruptionControllerConfiguration</code></a>
</td>
<td>
   <p>DisruptionControllerConfiguration پیکربندی قابلیت‌های مرتبط با
DisruptionController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>StatefulSetController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-StatefulSetControllerConfiguration"><code>StatefulSetControllerConfiguration</code></a>
</td>
<td>
   <p>StatefulSetControllerConfiguration پیکربندی قابلیت‌های مرتبط با
StatefulSetController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>DeprecatedController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DeprecatedControllerConfiguration"><code>DeprecatedControllerConfiguration</code></a>
</td>
<td>
   <p>DeprecatedControllerConfiguration پیکربندی برخی از قابلیت‌های منسوخ‌شده را
در بر دارد.</p>
</td>
</tr>
<tr><td><code>EndpointController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointControllerConfiguration"><code>EndpointControllerConfiguration</code></a>
</td>
<td>
   <p>EndpointControllerConfiguration پیکربندی قابلیت‌های مرتبط با EndpointController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>EndpointSliceController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceControllerConfiguration"><code>EndpointSliceControllerConfiguration</code></a>
</td>
<td>
   <p>EndpointSliceControllerConfiguration پیکربندی قابلیت‌های مرتبط با
EndpointSliceController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>EndpointSliceMirroringController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceMirroringControllerConfiguration"><code>EndpointSliceMirroringControllerConfiguration</code></a>
</td>
<td>
   <p>EndpointSliceMirroringControllerConfiguration پیکربندی قابلیت‌های مرتبط با
EndpointSliceMirroringController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>EphemeralVolumeController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-EphemeralVolumeControllerConfiguration"><code>EphemeralVolumeControllerConfiguration</code></a>
</td>
<td>
   <p>EphemeralVolumeControllerConfiguration پیکربندی قابلیت‌های مرتبط با EphemeralVolumeController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>GarbageCollectorController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-GarbageCollectorControllerConfiguration"><code>GarbageCollectorControllerConfiguration</code></a>
</td>
<td>
   <p>GarbageCollectorControllerConfiguration پیکربندی قابلیت‌های مرتبط با
GarbageCollectorController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>HPAController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-HPAControllerConfiguration"><code>HPAControllerConfiguration</code></a>
</td>
<td>
   <p>HPAControllerConfiguration پیکربندی قابلیت‌های مرتبط با HPAController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>JobController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-JobControllerConfiguration"><code>JobControllerConfiguration</code></a>
</td>
<td>
   <p>JobControllerConfiguration پیکربندی قابلیت‌های مرتبط با JobController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>CronJobController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CronJobControllerConfiguration"><code>CronJobControllerConfiguration</code></a>
</td>
<td>
   <p>CronJobControllerConfiguration پیکربندی قابلیت‌های مرتبط با CronJobController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>LegacySATokenCleaner</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-LegacySATokenCleanerConfiguration"><code>LegacySATokenCleanerConfiguration</code></a>
</td>
<td>
   <p>LegacySATokenCleanerConfiguration پیکربندی قابلیت‌های مرتبط با LegacySATokenCleaner را در بر دارد.</p>
</td>
</tr>
<tr><td><code>NamespaceController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-NamespaceControllerConfiguration"><code>NamespaceControllerConfiguration</code></a>
</td>
<td>
   <p>NamespaceControllerConfiguration پیکربندی قابلیت‌های مرتبط با NamespaceController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>NodeIPAMController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-NodeIPAMControllerConfiguration"><code>NodeIPAMControllerConfiguration</code></a>
</td>
<td>
   <p>NodeIPAMControllerConfiguration پیکربندی قابلیت‌های مرتبط با NodeIPAMController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>NodeLifecycleController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-NodeLifecycleControllerConfiguration"><code>NodeLifecycleControllerConfiguration</code></a>
</td>
<td>
   <p>NodeLifecycleControllerConfiguration پیکربندی قابلیت‌های مرتبط با
NodeLifecycleController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>PersistentVolumeBinderController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeBinderControllerConfiguration"><code>PersistentVolumeBinderControllerConfiguration</code></a>
</td>
<td>
   <p>PersistentVolumeBinderControllerConfiguration پیکربندی قابلیت‌های مرتبط با
PersistentVolumeBinderController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>PodGCController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-PodGCControllerConfiguration"><code>PodGCControllerConfiguration</code></a>
</td>
<td>
   <p>PodGCControllerConfiguration پیکربندی قابلیت‌های مرتبط با PodGCController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>ReplicaSetController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicaSetControllerConfiguration"><code>ReplicaSetControllerConfiguration</code></a>
</td>
<td>
   <p>ReplicaSetControllerConfiguration پیکربندی قابلیت‌های مرتبط با ReplicaSet را در بر دارد.</p>
</td>
</tr>
<tr><td><code>ReplicationController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicationControllerConfiguration"><code>ReplicationControllerConfiguration</code></a>
</td>
<td>
   <p>ReplicationControllerConfiguration پیکربندی قابلیت‌های مرتبط با
ReplicationController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>ResourceQuotaController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ResourceQuotaControllerConfiguration"><code>ResourceQuotaControllerConfiguration</code></a>
</td>
<td>
   <p>ResourceQuotaControllerConfiguration پیکربندی قابلیت‌های مرتبط با
ResourceQuotaController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>SAController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-SAControllerConfiguration"><code>SAControllerConfiguration</code></a>
</td>
<td>
   <p>SAControllerConfiguration پیکربندی قابلیت‌های مرتبط با ServiceAccountController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>ServiceController</code> <B>[الزامی]</B><br/>
<a href="#ServiceControllerConfiguration"><code>ServiceControllerConfiguration</code></a>
</td>
<td>
   <p>ServiceControllerConfiguration پیکربندی قابلیت‌های مرتبط با ServiceController
را در بر دارد.</p>
</td>
</tr>
<tr><td><code>TTLAfterFinishedController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-TTLAfterFinishedControllerConfiguration"><code>TTLAfterFinishedControllerConfiguration</code></a>
</td>
<td>
   <p>TTLAfterFinishedControllerConfiguration پیکربندی قابلیت‌های مرتبط با
TTLAfterFinishedController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>ValidatingAdmissionPolicyStatusController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ValidatingAdmissionPolicyStatusControllerConfiguration"><code>ValidatingAdmissionPolicyStatusControllerConfiguration</code></a>
</td>
<td>
   <p>ValidatingAdmissionPolicyStatusControllerConfiguration پیکربندی قابلیت‌های مرتبط با
ValidatingAdmissionPolicyStatusController را در بر دارد.</p>
</td>
</tr>
<tr><td><code>DeviceTaintEvictionController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-DeviceTaintEvictionControllerConfiguration"><code>DeviceTaintEvictionControllerConfiguration</code></a>
</td>
<td>
   <p>DeviceTaintEvictionControllerConfiguration شامل عناصری است که کنترل‌کننده تخلیه ناشی از device taint را پیکربندی می‌کنند.</p>
</td>
</tr>
<tr><td><code>ResourceClaimController</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-ResourceClaimControllerConfiguration"><code>ResourceClaimControllerConfiguration</code></a>
</td>
<td>
   <p>ResourceClaimControllerConfiguration شامل عناصری است که کنترل‌کننده resource claim را پیکربندی می‌کنند.</p>
</td>
</tr>
</tbody>
</table>

## `AttachDetachControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-AttachDetachControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>AttachDetachControllerConfiguration شامل عناصری است که AttachDetachController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>DisableAttachDetachReconcilerSync</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>Reconciler یک حلقه دوره‌ای اجرا می‌کند تا با راه‌اندازی عملیات attach و detach،
وضعیت مطلوب را با وضعیت واقعی سیستم هماهنگ کند.
این پرچم، این هماهنگ‌سازی (reconcile) را فعال یا غیرفعال می‌کند. مقدار پیش‌فرض آن false است و بنابراین فعال است.</p>
</td>
</tr>
<tr><td><code>ReconcilerSyncLoopPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>ReconcilerSyncLoopPeriod مدت زمانی است که حلقه همگام‌سازی وضعیت‌های reconciler
میان اجراهای متوالی منتظر می‌ماند. مقدار پیش‌فرض آن ۶۰ ثانیه است.</p>
</td>
</tr>
<tr><td><code>disableForceDetachOnTimeout</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>DisableForceDetachOnTimeout در صورت فراتر رفتن از حداکثر زمان unmount،
detach اجباری را غیرفعال می‌کند. مقدار پیش‌فرض آن false است و بنابراین
detach اجباری هنگام unmount فعال است.</p>
</td>
</tr>
</tbody>
</table>

## `CSRSigningConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration}
    

**ظاهر شده در:**

- [CSRSigningControllerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningControllerConfiguration)


<p>CSRSigningConfiguration اطلاعات مربوط به یک امضاکننده CSR مشخص را در بر دارد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>CertFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>certFile نام فایلی است که حاوی گواهی X509 CA با کدگذاری PEM است
و برای صدور گواهی‌ها استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>KeyFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>keyFile نام فایلی است که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است
و برای صدور گواهی‌ها استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `CSRSigningControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>CSRSigningControllerConfiguration شامل عناصری است که CSRSigningController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ClusterSigningCertFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterSigningCertFile نام فایلی است که حاوی گواهی X509 CA با کدگذاری PEM است
و برای صدور گواهی‌های با دامنه کلاستر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>ClusterSigningKeyFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>clusterSigningCertFile نام فایلی است که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است
و برای صدور گواهی‌های با دامنه کلاستر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>KubeletServingSignerConfiguration</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>kubeletServingSignerConfiguration گواهی و کلیدی را در بر دارد که برای صدور گواهی‌ها برای امضاکننده kubernetes.io/kubelet-serving استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>KubeletClientSignerConfiguration</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>kubeletClientSignerConfiguration گواهی و کلیدی را در بر دارد که برای صدور گواهی‌ها برای kubernetes.io/kube-apiserver-client-kubelet استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>KubeAPIServerClientSignerConfiguration</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>kubeAPIServerClientSignerConfiguration گواهی و کلیدی را در بر دارد که برای صدور گواهی‌ها برای kubernetes.io/kube-apiserver-client استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>LegacyUnknownSignerConfiguration</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-CSRSigningConfiguration"><code>CSRSigningConfiguration</code></a>
</td>
<td>
   <p>legacyUnknownSignerConfiguration گواهی و کلیدی را در بر دارد که برای صدور گواهی‌ها برای kubernetes.io/legacy-unknown استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>ClusterSigningDuration</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>clusterSigningDuration حداکثر مدت اعتباری است که به گواهی‌های امضاشده داده می‌شود.
هر CSR می‌تواند با تنظیم spec.expirationSeconds گواهی‌هایی با اعتبار کوتاه‌تر درخواست کند.</p>
</td>
</tr>
</tbody>
</table>

## `CronJobControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-CronJobControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>CronJobControllerConfiguration شامل عناصری است که CrongJob2Controller را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentCronJobSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentCronJobSyncs تعداد آبجکت‌های job است که مجاز به
همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = jobهای پاسخگوتر،
اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
</tbody>
</table>

## `DaemonSetControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DaemonSetControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DaemonSetControllerConfiguration شامل عناصری است که DaemonSetController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentDaemonSetSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentDaemonSetSyncs تعداد آبجکت‌های daemonset است که مجاز به
همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = daemonsetهای پاسخگوتر،
اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
</tbody>
</table>

## `DeploymentControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DeploymentControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DeploymentControllerConfiguration شامل عناصری است که DeploymentController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentDeploymentSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentDeploymentSyncs تعداد آبجکت‌های deployment است که مجاز به
همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = deploymentهای پاسخگوتر،
اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
</tbody>
</table>

## `DeprecatedControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DeprecatedControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DeprecatedControllerConfiguration شامل عناصری است که قرار است منسوخ شوند.</p>




## `DeviceTaintEvictionControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DeviceTaintEvictionControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DeviceTaintEvictionControllerConfiguration شامل عناصری است که کنترل‌کننده تخلیه ناشی از device taint را پیکربندی می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentSyncs تعداد عملیات‌هایی (مانند حذف یک pod، به‌روزرسانی وضعیت ResourcClaim و غیره) است
که به‌صورت هم‌زمان انجام می‌شوند. عدد بزرگ‌تر = پردازش بیشتر، اما بار بیشتر بر CPU (و شبکه).</p>
<p>مقدار پیش‌فرض ۱۰ است.</p>
</td>
</tr>
</tbody>
</table>

## `DisruptionControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-DisruptionControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>DisruptionControllerConfiguration شامل عناصری است که DisruptionController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentDisruptionSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentDisruptionSyncs تعداد آبجکت‌های PodDisruptionBudget است که
مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = به‌روزرسانی‌های PDB
پاسخگوتر، اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
</tbody>
</table>

## `EndpointControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EndpointControllerConfiguration شامل عناصری است که EndpointController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentEndpointSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentEndpointSyncs تعداد عملیات همگام‌سازی endpoint است که
به‌صورت هم‌زمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر endpointها،
اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
<tr><td><code>EndpointUpdatesBatchPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>EndpointUpdatesBatchPeriod طول دوره دسته‌بندی به‌روزرسانی‌های endpoint را مشخص می‌کند.
پردازش تغییرات pod به اندازه این مدت به تأخیر می‌افتد تا با به‌روزرسانی‌های احتمالی
بعدی ترکیب شود و تعداد کل به‌روزرسانی‌های endpoint کاهش یابد.</p>
</td>
</tr>
</tbody>
</table>

## `EndpointSliceControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EndpointSliceControllerConfiguration شامل عناصری است که
EndpointSliceController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentServiceEndpointSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentServiceEndpointSyncs تعداد عملیات همگام‌سازی endpoint سرویس است
که به‌صورت هم‌زمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر
endpoint sliceها، اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
<tr><td><code>MaxEndpointsPerSlice</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>maxEndpointsPerSlice حداکثر تعداد endpointهایی است که به یک EndpointSlice
افزوده می‌شود. تعداد بیشتر endpoint در هر slice به معنای endpoint sliceهای
کمتر و بزرگ‌تر، اما منابع بزرگ‌تر است.</p>
</td>
</tr>
<tr><td><code>EndpointUpdatesBatchPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>EndpointUpdatesBatchPeriod طول دوره دسته‌بندی به‌روزرسانی‌های endpoint را مشخص می‌کند.
پردازش تغییرات pod به اندازه این مدت به تأخیر می‌افتد تا با به‌روزرسانی‌های احتمالی
بعدی ترکیب شود و تعداد کل به‌روزرسانی‌های endpoint کاهش یابد.</p>
</td>
</tr>
</tbody>
</table>

## `EndpointSliceMirroringControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EndpointSliceMirroringControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EndpointSliceMirroringControllerConfiguration شامل عناصری است که
EndpointSliceMirroringController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>MirroringConcurrentServiceEndpointSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>mirroringConcurrentServiceEndpointSyncs تعداد عملیات همگام‌سازی endpoint سرویس
است که به‌صورت هم‌زمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر
endpoint sliceها، اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
<tr><td><code>MirroringMaxEndpointsPerSubset</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>mirroringMaxEndpointsPerSubset حداکثر تعداد endpointهایی است که
برای یک EndpointSubset در یک EndpointSlice بازتاب (mirror) داده می‌شود.</p>
</td>
</tr>
<tr><td><code>MirroringEndpointUpdatesBatchPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>mirroringEndpointUpdatesBatchPeriod را می‌توان برای دسته‌بندی به‌روزرسانی‌های EndpointSlice
به کار برد. همه به‌روزرسانی‌هایی که با تغییرات EndpointSlice آغاز می‌شوند، تا حداکثر
'mirroringEndpointUpdatesBatchPeriod' به تأخیر می‌افتند. اگر در این بازه، آدرس‌های دیگری
در همان منبع Endpoints تغییر کنند، در قالب یک به‌روزرسانی واحد EndpointSlice
دسته‌بندی می‌شوند. مقدار پیش‌فرض ۰ به این معناست که هر به‌روزرسانی Endpoints
یک به‌روزرسانی EndpointSlice را راه‌اندازی می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `EphemeralVolumeControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-EphemeralVolumeControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>EphemeralVolumeControllerConfiguration شامل عناصری است که EphemeralVolumeController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentEphemeralVolumeSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentEphemeralVolumeSyncseSyncs تعداد عملیات همگام‌سازی حجم موقت (ephemeral volume) است
که به‌صورت هم‌زمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر حجم‌های موقت،
اما بار بیشتر بر CPU (و شبکه).</p>
</td>
</tr>
</tbody>
</table>

## `GarbageCollectorControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-GarbageCollectorControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>GarbageCollectorControllerConfiguration شامل عناصری است که GarbageCollectorController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>EnableGarbageCollector</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>زباله‌روب (garbage collector) عمومی را فعال می‌کند. این مقدار حتماً باید با فلگ متناظر آن در kube-apiserver هماهنگ باشد. هشدار: زباله‌روب عمومی یک قابلیت آلفا است.</p>
</td>
</tr>
<tr><td><code>ConcurrentGCSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentGCSyncs تعداد workerهای garbage collector است که مجاز به همگام‌سازی هم‌زمان هستند.</p>
</td>
</tr>
<tr><td><code>GCIgnoredResources</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-GroupResource"><code>[]GroupResource</code></a>
</td>
<td>
   <p>gcIgnoredResources فهرست GroupResourceهایی است که garbage collection باید آن‌ها را نادیده بگیرد.</p>
</td>
</tr>
</tbody>
</table>

## `GroupResource`     {#kubecontrollermanager-config-k8s-io-v1alpha1-GroupResource}
    

**ظاهر شده در:**

- [GarbageCollectorControllerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-GarbageCollectorControllerConfiguration)


<p>GroupResource یک منبع گروهی (group resource) را توصیف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>Group</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>group بخش گروه (group) از GroupResource است.</p>
</td>
</tr>
<tr><td><code>Resource</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>resource بخش منبع (resource) از GroupResource است.</p>
</td>
</tr>
</tbody>
</table>

## `HPAControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-HPAControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>HPAControllerConfiguration شامل عناصری است که HPAController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentHorizontalPodAutoscalerSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentHorizontalPodAutoscalerSyncs تعداد آبجکت‌های HPA است که مجاز به همگام‌سازی هم‌زمان هستند.
عدد بزرگ‌تر = پردازش پاسخگوتر HPA، اما بار CPU (و شبکه) بیشتر.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerSyncPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerSyncPeriod بازه زمانی همگام‌سازی تعداد Podها در horizontal pod autoscaler است.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerDownscaleStabilizationWindow</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerDowncaleStabilizationWindow بازه‌ای زمانی است که autoscaler در طول آن به عقب نگاه می‌کند و تعداد را به کمتر از هر توصیه‌ای که در آن بازه ارائه کرده است کاهش نمی‌دهد.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerTolerance</code> <B>[الزامی]</B><br/>
<code>float64</code>
</td>
<td>
   <p>HorizontalPodAutoscalerTolerance میزان تحمل (tolerance) را هنگامی تعیین می‌کند که مصرف منابع پیشنهاد افزایش یا کاهش مقیاس را می‌دهد.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerCPUInitializationPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerCPUInitializationPeriod بازه زمانی پس از شروع Pod است که در آن ممکن است نمونه‌های CPU نادیده گرفته شوند.</p>
</td>
</tr>
<tr><td><code>HorizontalPodAutoscalerInitialReadinessDelay</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>HorizontalPodAutoscalerInitialReadinessDelay بازه زمانی پس از شروع Pod است که در طول آن، تغییرات آمادگی (readiness) به‌گونه‌ای در نظر گرفته می‌شوند که گویی آمادگی برای نخستین بار تنظیم شده است. تنها اثر این موضوع آن است که
HPA نمونه‌های CPU مربوط به Podهای آماده‌نشده‌ای را که آخرین تغییر آمادگی آن‌ها در همین
بازه رخ داده است نادیده می‌گیرد.</p>
</td>
</tr>
</tbody>
</table>

## `JobControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-JobControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>JobControllerConfiguration شامل عناصری است که JobController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentJobSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentJobSyncs تعداد آبجکت‌های Job است که مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = Jobهای پاسخگوتر،
اما بار CPU (و شبکه) بیشتر.</p>
</td>
</tr>
</tbody>
</table>

## `LegacySATokenCleanerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-LegacySATokenCleanerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>LegacySATokenCleanerConfiguration شامل عناصری است که LegacySATokenCleaner را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>CleanUpPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>CleanUpPeriod مدت زمانی است که باید از آخرین استفاده از یک توکن حساب سرویس (service account) تولیدشده به‌صورت خودکار بگذرد تا بتوان آن را حذف کرد.</p>
</td>
</tr>
</tbody>
</table>

## `NamespaceControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-NamespaceControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>NamespaceControllerConfiguration شامل عناصری است که NamespaceController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>NamespaceSyncPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>namespaceSyncPeriod بازه زمانی همگام‌سازی به‌روزرسانی‌های چرخه عمر فضای نام (namespace) است.</p>
</td>
</tr>
<tr><td><code>ConcurrentNamespaceSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentNamespaceSyncs تعداد آبجکت‌های namespace است که مجاز به همگام‌سازی هم‌زمان هستند.</p>
</td>
</tr>
</tbody>
</table>

## `NodeIPAMControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-NodeIPAMControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>NodeIPAMControllerConfiguration شامل عناصری است که NodeIpamController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ServiceCIDR</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>serviceCIDR محدوده CIDR برای Serviceها در کلاستر است.</p>
</td>
</tr>
<tr><td><code>SecondaryServiceCIDR</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>secondaryServiceCIDR محدوده CIDR برای Serviceها در کلاستر است. این مقدار در کلاسترهای dual stack استفاده می‌شود. SecondaryServiceCIDR باید از خانواده IP متفاوتی نسبت به ServiceCIDR باشد.</p>
</td>
</tr>
<tr><td><code>NodeCIDRMaskSize</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>NodeCIDRMaskSize اندازه ماسک (mask) برای CIDR نودها در کلاستر است.</p>
</td>
</tr>
<tr><td><code>NodeCIDRMaskSizeIPv4</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>NodeCIDRMaskSizeIPv4 اندازه ماسک برای CIDR نودها در کلاستر dual-stack است.</p>
</td>
</tr>
<tr><td><code>NodeCIDRMaskSizeIPv6</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>NodeCIDRMaskSizeIPv6 اندازه ماسک برای CIDR نودها در کلاستر dual-stack است.</p>
</td>
</tr>
</tbody>
</table>

## `NodeLifecycleControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-NodeLifecycleControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>NodeLifecycleControllerConfiguration شامل عناصری است که NodeLifecycleController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>NodeEvictionRate</code> <B>[الزامی]</B><br/>
<code>float32</code>
</td>
<td>
   <p>nodeEvictionRate تعداد نودهایی در هر ثانیه است که در صورت خرابی نود، هنگامی که یک zone سالم است، Podهای روی آن‌ها حذف می‌شوند.</p>
</td>
</tr>
<tr><td><code>SecondaryNodeEvictionRate</code> <B>[الزامی]</B><br/>
<code>float32</code>
</td>
<td>
   <p>secondaryNodeEvictionRate تعداد نودهایی در هر ثانیه است که در صورت خرابی نود، هنگامی که یک zone ناسالم است، Podهای روی آن‌ها حذف می‌شوند.</p>
</td>
</tr>
<tr><td><code>NodeStartupGracePeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeStartupGracePeriod مدت زمانی است که اجازه می‌دهیم یک نودِ در حال راه‌اندازی بدون پاسخ بماند، پیش از آنکه آن را ناسالم علامت‌گذاری کنیم.</p>
</td>
</tr>
<tr><td><code>NodeMonitorGracePeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>nodeMontiorGracePeriod مدت زمانی است که اجازه می‌دهیم یک نودِ در حال اجرا بدون پاسخ بماند، پیش از آنکه آن را ناسالم علامت‌گذاری کنیم. این مقدار باید N برابر nodeStatusUpdateFrequency در kubelet باشد، که در آن N بیانگر تعداد دفعات مجاز تلاش مجدد برای ارسال وضعیت نود توسط kubelet است. این مقدار همچنین باید از مجموع
HTTP2_PING_TIMEOUT_SECONDS و HTTP2_READ_IDLE_TIMEOUT_SECONDS بزرگ‌تر باشد.</p>
</td>
</tr>
<tr><td><code>PodEvictionTimeout</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>podEvictionTimeout مهلت (grace period) حذف Podها روی نودهای خراب است.</p>
</td>
</tr>
<tr><td><code>LargeClusterSizeThreshold</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>secondaryNodeEvictionRate برای کلاسترهایی که اندازه آن‌ها کوچک‌تر یا مساوی largeClusterSizeThreshold است، به‌طور ضمنی با مقدار 0 بازنویسی می‌شود.</p>
</td>
</tr>
<tr><td><code>UnhealthyZoneThreshold</code> <B>[الزامی]</B><br/>
<code>float32</code>
</td>
<td>
   <p>یک zone در nodeEvictionRate و secondaryNodeEvictionRate ناسالم در نظر گرفته می‌شود، هنگامی که دست‌کم
unhealthyZoneThreshold (نه کمتر از ۳) از نودهای آن zone در وضعیت NotReady باشند.</p>
</td>
</tr>
<tr><td><code>NodeMonitorPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>NodeMonitorPeriod بازه زمانی همگام‌سازی NodeStatus در NodeLifecycleController است.</p>
</td>
</tr>
</tbody>
</table>

## `PersistentVolumeBinderControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeBinderControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>PersistentVolumeBinderControllerConfiguration شامل عناصری است که
PersistentVolumeBinderController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>PVClaimBinderSyncPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>pvClaimBinderSyncPeriod بازه زمانی همگام‌سازی persistent volumeها و persistent volume claimها است.</p>
</td>
</tr>
<tr><td><code>VolumeConfiguration</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-VolumeConfiguration"><code>VolumeConfiguration</code></a>
</td>
<td>
   <p>volumeConfiguration پیکربندی قابلیت‌های مرتبط با حجم (volume) را نگه می‌دارد.</p>
</td>
</tr>
</tbody>
</table>

## `PersistentVolumeRecyclerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeRecyclerConfiguration}
    

**ظاهر شده در:**

- [VolumeConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-VolumeConfiguration)


<p>PersistentVolumeRecyclerConfiguration شامل عناصری است که افزونه‌های persistent volume را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>MaximumRetry</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>maximumRetry تعداد دفعات تلاش مجددی است که PV recycler در صورت شکست در بازیافت PV انجام می‌دهد.</p>
</td>
</tr>
<tr><td><code>MinimumTimeoutNFS</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>minimumTimeoutNFS حداقل مقدار ActiveDeadlineSeconds برای استفاده در یک Pod بازیافت‌کننده (Recycler) از نوع NFS است.</p>
</td>
</tr>
<tr><td><code>PodTemplateFilePathNFS</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>podTemplateFilePathNFS مسیر فایل تعریف Pod است که به‌عنوان قالب برای بازیافت persistent volume از نوع NFS استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>IncrementTimeoutNFS</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>incrementTimeoutNFS مقدار زمانی است که به ازای هر Gi به ActiveDeadlineSeconds برای یک Pod پاک‌سازی‌کننده (scrubber) از نوع NFS افزوده می‌شود.</p>
</td>
</tr>
<tr><td><code>PodTemplateFilePathHostPath</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>podTemplateFilePathHostPath مسیر فایل تعریف Pod است که به‌عنوان قالب برای بازیافت persistent volume از نوع HostPath استفاده می‌شود. این گزینه صرفاً برای توسعه و آزمایش است و
در کلاستر چندنودی کار نخواهد کرد.</p>
</td>
</tr>
<tr><td><code>MinimumTimeoutHostPath</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>minimumTimeoutHostPath حداقل مقدار ActiveDeadlineSeconds برای استفاده در یک Pod بازیافت‌کننده (Recycler) از نوع HostPath است. این گزینه صرفاً برای توسعه و آزمایش است و در کلاستر چندنودی کار نخواهد کرد.</p>
</td>
</tr>
<tr><td><code>IncrementTimeoutHostPath</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>incrementTimeoutHostPath مقدار زمانی است که به ازای هر Gi به ActiveDeadlineSeconds برای یک Pod پاک‌سازی‌کننده (scrubber) از نوع HostPath افزوده می‌شود. این گزینه صرفاً برای توسعه و آزمایش است و در کلاستر چندنودی کار نخواهد کرد.</p>
</td>
</tr>
</tbody>
</table>

## `PodGCControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-PodGCControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>PodGCControllerConfiguration شامل عناصری است که PodGCController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>TerminatedPodGCThreshold</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>terminatedPodGCThreshold تعداد Podهای خاتمه‌یافته‌ای است که می‌توانند وجود داشته باشند،
پیش از آنکه garbage collector مربوط به Podهای خاتمه‌یافته شروع به حذف آن‌ها کند.
اگر مقدار آن &lt;= 0 باشد، garbage collector مربوط به Podهای خاتمه‌یافته غیرفعال است.</p>
</td>
</tr>
</tbody>
</table>

## `ReplicaSetControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicaSetControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ReplicaSetControllerConfiguration شامل عناصری است که ReplicaSetController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentRSSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentRSSyncs تعداد ReplicaSetهایی است که مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = مدیریت پاسخگوتر replicaها، اما بار CPU (و شبکه) بیشتر.</p>
</td>
</tr>
</tbody>
</table>

## `ReplicationControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ReplicationControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ReplicationControllerConfiguration شامل عناصری است که ReplicationController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentRCSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentRCSyncs تعداد replication controllerهایی است که مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = مدیریت پاسخگوتر replicaها،
اما بار CPU (و شبکه) بیشتر.</p>
</td>
</tr>
</tbody>
</table>

## `ResourceClaimControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ResourceClaimControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ResourceClaimControllerConfiguration شامل عناصری است که کنترل‌کننده resource claim را پیکربندی می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentSyncs تعداد عملیاتی (مانند حذف یک Pod، به‌روزرسانی وضعیت ResourcClaim و غیره) است
که به‌صورت هم‌زمان انجام می‌شوند. عدد بزرگ‌تر = پردازش بیشتر، اما بار CPU (و شبکه) بیشتر.</p>
<p>مقدار پیش‌فرض ۵۰ است.</p>
</td>
</tr>
</tbody>
</table>

## `ResourceQuotaControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ResourceQuotaControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ResourceQuotaControllerConfiguration شامل عناصری است که ResourceQuotaController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ResourceQuotaSyncPeriod</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>resourceQuotaSyncPeriod بازه زمانی همگام‌سازی وضعیت مصرف سهمیه (quota) در سامانه است.</p>
</td>
</tr>
<tr><td><code>ConcurrentResourceQuotaSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentResourceQuotaSyncs تعداد resource quotaهایی است که مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = مدیریت پاسخگوتر سهمیه،
اما بار CPU (و شبکه) بیشتر.</p>
</td>
</tr>
</tbody>
</table>

## `SAControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-SAControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>SAControllerConfiguration شامل عناصری است که ServiceAccountController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ServiceAccountKeyFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>serviceAccountKeyFile نام فایلی است که شامل یک کلید خصوصی RSA با کدگذاری PEM است
و برای امضای توکن‌های service account استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>ConcurrentSATokenSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentSATokenSyncs تعداد عملیات همگام‌سازی توکن service account است
که به‌صورت هم‌زمان انجام می‌شوند.</p>
</td>
</tr>
<tr><td><code>RootCAFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>rootCAFile مرجع صدور گواهی ریشه (root certificate authority) است که در Secret توکن service account درج می‌شود. این مقدار باید یک بسته CA معتبر با کدگذاری PEM باشد.</p>
</td>
</tr>
</tbody>
</table>

## `StatefulSetControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-StatefulSetControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>StatefulSetControllerConfiguration شامل عناصری است که StatefulSetController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentStatefulSetSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentStatefulSetSyncs تعداد آبجکت‌های StatefulSet است که مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = StatefulSetهای پاسخگوتر،
اما بار CPU (و شبکه) بیشتر.</p>
</td>
</tr>
</tbody>
</table>

## `TTLAfterFinishedControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-TTLAfterFinishedControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>TTLAfterFinishedControllerConfiguration شامل عناصری است که TTLAfterFinishedController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentTTLSyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>concurrentTTLSyncs تعداد workerهای collector مربوط به TTL-after-finished است که مجاز به همگام‌سازی هم‌زمان هستند.</p>
</td>
</tr>
</tbody>
</table>

## `ValidatingAdmissionPolicyStatusControllerConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-ValidatingAdmissionPolicyStatusControllerConfiguration}
    

**ظاهر شده در:**

- [KubeControllerManagerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)


<p>ValidatingAdmissionPolicyStatusControllerConfiguration شامل عناصری است که ValidatingAdmissionPolicyStatusController را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ConcurrentPolicySyncs</code> <B>[الزامی]</B><br/>
<code>int32</code>
</td>
<td>
   <p>ConcurrentPolicySyncs تعداد آبجکت‌های policy است که مجاز به همگام‌سازی هم‌زمان هستند. عدد بزرگ‌تر = بررسی سریع‌تر نوع (type checking)،
اما بار CPU (و شبکه) بیشتر.
مقدار پیش‌فرض ۵ است.</p>
</td>
</tr>
</tbody>
</table>

## `VolumeConfiguration`     {#kubecontrollermanager-config-k8s-io-v1alpha1-VolumeConfiguration}
    

**ظاهر شده در:**

- [PersistentVolumeBinderControllerConfiguration](#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeBinderControllerConfiguration)


<p>VolumeConfiguration شامل <em>تمام</em> فلگ‌های برشمرده‌شده‌ای است که برای پیکربندی همه‌ی افزونه‌های حجم (volume) در نظر گرفته شده‌اند. بر اساس این پیکربندی، باینری controller-manager نمونه‌های متعددی از
volume.VolumeConfig ایجاد می‌کند که هر یک فقط شامل پیکربندی موردنیاز همان افزونه است و سپس
به افزونه‌ی مربوطه ارسال می‌شود. باینری ControllerManager تنها بخشی از کد است
که می‌داند چه افزونه‌هایی پشتیبانی می‌شوند و هر فلگ به کدام افزونه مربوط است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>EnableHostPathProvisioning</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableHostPathProvisioning تأمین (provisioning) PV از نوع HostPath را هنگام اجرا بدون
ارائه‌دهنده‌ی ابری فعال می‌کند. این امر امکان آزمایش و توسعه‌ی قابلیت‌های تأمین را فراهم می‌کند. تأمین HostPath
به هیچ وجه پشتیبانی نمی‌شود، در کلاستر چندنودی کار نخواهد کرد و
نباید برای هیچ منظوری جز آزمایش یا توسعه استفاده شود.</p>
</td>
</tr>
<tr><td><code>EnableDynamicProvisioning</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>enableDynamicProvisioning تأمین حجم‌ها (volumes) را هنگام اجرا در محیطی که
از تأمین پویا پشتیبانی می‌کند فعال می‌کند. مقدار پیش‌فرض true است.</p>
</td>
</tr>
<tr><td><code>PersistentVolumeRecyclerConfiguration</code> <B>[الزامی]</B><br/>
<a href="#kubecontrollermanager-config-k8s-io-v1alpha1-PersistentVolumeRecyclerConfiguration"><code>PersistentVolumeRecyclerConfiguration</code></a>
</td>
<td>
   <p>persistentVolumeRecyclerConfiguration پیکربندی افزونه‌های حجم پایدار (persistent volume) را در بر دارد.</p>
</td>
</tr>
<tr><td><code>FlexVolumePluginDir</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>volumePluginDir مسیر کامل دایرکتوری‌ای است که افزونه‌ی حجم flex
باید در آن به جست‌وجوی افزونه‌های حجم اضافیِ شخص ثالث بپردازد.</p>
</td>
</tr>
</tbody>
</table>
