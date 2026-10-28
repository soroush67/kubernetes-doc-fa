---
title: پیکربندی ممیزی (Audit) در kube-apiserver (v1)
content_type: tool-reference
package: audit.k8s.io/v1
auto_generated: true
---


## انواع منابع 


- [Event](#audit-k8s-io-v1-Event)
- [EventList](#audit-k8s-io-v1-EventList)
- [Policy](#audit-k8s-io-v1-Policy)
- [PolicyList](#audit-k8s-io-v1-PolicyList)
  

## `Event`     {#audit-k8s-io-v1-Event}
    

**در این بخش‌ها ظاهر می‌شود:**

- [EventList](#audit-k8s-io-v1-EventList)


<p>Event تمام اطلاعاتی را که می‌توان در یک لاگ ممیزی API گنجاند، ثبت می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>audit.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>Event</code></td></tr>
    
  
<tr><td><code>level</code> <B>[الزامی]</B><br/>
<a href="#audit-k8s-io-v1-Level"><code>Level</code></a>
</td>
<td>
   <p>سطح ممیزی (AuditLevel) که رویداد در آن تولید شده است.</p>
</td>
</tr>
<tr><td><code>auditID</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID"><code>k8s.io/apimachinery/pkg/types.UID</code></a>
</td>
<td>
   <p>شناسه یکتای ممیزی که برای هر درخواست تولید می‌شود.</p>
</td>
</tr>
<tr><td><code>stage</code> <B>[الزامی]</B><br/>
<a href="#audit-k8s-io-v1-Stage"><code>Stage</code></a>
</td>
<td>
   <p>مرحله‌ای از پردازش درخواست که این نمونه از رویداد در آن تولید شده است.</p>
</td>
</tr>
<tr><td><code>requestURI</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>RequestURI همان URI درخواست است که کلاینت به سرور ارسال کرده است.</p>
</td>
</tr>
<tr><td><code>verb</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Verb فعل (verb) کوبرنتیز مرتبط با درخواست است.
برای درخواست‌های غیرمنبعی، این مقدار همان متد HTTP با حروف کوچک است.</p>
</td>
</tr>
<tr><td><code>user</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#userinfo-v1-authentication-k8s-io"><code>authentication/v1.UserInfo</code></a>
</td>
<td>
   <p>اطلاعات کاربر احراز هویت‌شده.</p>
</td>
</tr>
<tr><td><code>impersonatedUser</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#userinfo-v1-authentication-k8s-io"><code>authentication/v1.UserInfo</code></a>
</td>
<td>
   <p>اطلاعات کاربری که هویت او جعل (impersonate) شده است.</p>
</td>
</tr>
<tr><td><code>authenticationMetadata</code><br/>
<a href="#audit-k8s-io-v1-AuthenticationMetadata"><code>AuthenticationMetadata</code></a>
</td>
<td>
   <p>AuthenticationMetadata شامل جزئیاتی درباره نحوه احراز هویت درخواست است.</p>
</td>
</tr>
<tr><td><code>sourceIPs</code><br/>
<code>[]string</code>
</td>
<td>
   <p>IPهای مبدأ، یعنی جایی که درخواست از آن آغاز شده و پروکسی‌های میانی.
IPهای مبدأ به ترتیب زیر فهرست می‌شوند:</p>
<ol>
<li>IPهای موجود در هدر درخواست X-Forwarded-For</li>
<li>هدر X-Real-Ip، در صورتی که در فهرست X-Forwarded-For وجود نداشته باشد</li>
<li>آدرس راه دور (remote address) اتصال، در صورتی که با آخرین
IP موجود در فهرست تا این مرحله (X-Forwarded-For یا X-Real-Ip) مطابقت نداشته باشد.
توجه: همه IPها به‌جز آخرین مورد می‌توانند به‌صورت دلخواه توسط کلاینت تنظیم شوند.</li>
</ol>
</td>
</tr>
<tr><td><code>userAgent</code><br/>
<code>string</code>
</td>
<td>
   <p>UserAgent رشته user agent گزارش‌شده توسط کلاینت را ثبت می‌کند.
توجه کنید که UserAgent را کلاینت ارائه می‌کند و نباید به آن اعتماد کرد.</p>
</td>
</tr>
<tr><td><code>objectRef</code><br/>
<a href="#audit-k8s-io-v1-ObjectReference"><code>ObjectReference</code></a>
</td>
<td>
   <p>ارجاع به آبجکتی که این درخواست آن را هدف قرار داده است.
برای درخواست‌های از نوع List یا درخواست‌های غیرمنبعی کاربرد ندارد.</p>
</td>
</tr>
<tr><td><code>responseStatus</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#status-v1-meta"><code>meta/v1.Status</code></a>
</td>
<td>
   <p>وضعیت پاسخ؛ حتی زمانی که ResponseObject از نوع Status نباشد نیز مقداردهی می‌شود.
برای پاسخ‌های موفق، این مقدار فقط شامل Code و StatusSuccess خواهد بود.
برای پاسخ‌های خطا که از نوع status نیستند، این مقدار به‌صورت خودکار با Message خطا پر می‌شود.</p>
</td>
</tr>
<tr><td><code>requestObject</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Unknown"><code>k8s.io/apimachinery/pkg/runtime.Unknown</code></a>
</td>
<td>
   <p>آبجکت API موجود در درخواست، با قالب JSON. RequestObject همان‌گونه که در درخواست آمده است
(و احتمالاً دوباره با JSON کدگذاری شده) و پیش از تبدیل نسخه، اعمال مقادیر پیش‌فرض، admission یا
ادغام (merge) ثبت می‌شود. این یک نوع آبجکت نسخه‌دار خارجی است و ممکن است به‌تنهایی آبجکتی معتبر نباشد.
برای درخواست‌های غیرمنبعی حذف می‌شود. فقط در سطح Request و بالاتر ثبت می‌شود.</p>
</td>
</tr>
<tr><td><code>responseObject</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Unknown"><code>k8s.io/apimachinery/pkg/runtime.Unknown</code></a>
</td>
<td>
   <p>آبجکت API بازگردانده‌شده در پاسخ، با قالب JSON. ResponseObject پس از تبدیل
به نوع خارجی ثبت و به‌صورت JSON سریالایز می‌شود. برای درخواست‌های غیرمنبعی حذف می‌شود. فقط
در سطح Response ثبت می‌شود.</p>
</td>
</tr>
<tr><td><code>requestReceivedTimestamp</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#microtime-v1-meta"><code>meta/v1.MicroTime</code></a>
</td>
<td>
   <p>زمانی که درخواست به apiserver رسیده است.</p>
</td>
</tr>
<tr><td><code>stageTimestamp</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#microtime-v1-meta"><code>meta/v1.MicroTime</code></a>
</td>
<td>
   <p>زمانی که درخواست به مرحله ممیزی فعلی رسیده است.</p>
</td>
</tr>
<tr><td><code>annotations</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>Annotations یک نگاشت کلید-مقدار بدون ساختار است که همراه با رویداد ممیزی ذخیره می‌شود و ممکن است
توسط افزونه‌های فراخوانی‌شده در زنجیره پاسخ‌گویی به درخواست، از جمله افزونه‌های احراز هویت، مجوزدهی و
admission تنظیم شود. توجه کنید که این annotationها مربوط به رویداد ممیزی هستند و با
metadata.annotations آبجکت ارسال‌شده متناظر نیستند. کلیدها باید مؤلفه اطلاع‌دهنده را به‌طور یکتا مشخص کنند
تا از تداخل نام‌ها جلوگیری شود (برای مثال podsecuritypolicy.admission.k8s.io/policy). مقادیر
باید کوتاه باشند. Annotationها در سطح Metadata گنجانده می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `EventList`     {#audit-k8s-io-v1-EventList}
    


<p>EventList فهرستی از Eventهای ممیزی است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>audit.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>EventList</code></td></tr>
    
  
<tr><td><code>metadata</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>items</code> <B>[الزامی]</B><br/>
<a href="#audit-k8s-io-v1-Event"><code>[]Event</code></a>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `Policy`     {#audit-k8s-io-v1-Policy}
    

**در این بخش‌ها ظاهر می‌شود:**

- [PolicyList](#audit-k8s-io-v1-PolicyList)


<p>Policy پیکربندی ثبت لاگ ممیزی و قوانین مربوط به نحوه ثبت دسته‌های مختلف
درخواست‌ها را تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>audit.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>Policy</code></td></tr>
    
  
<tr><td><code>metadata</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#objectmeta-v1-meta"><code>meta/v1.ObjectMeta</code></a>
</td>
<td>
   <p>ObjectMeta برای سازگاری با زیرساخت API گنجانده شده است.</p>
برای فیلدهای <code>metadata</code> به مستندات API کوبرنتیز مراجعه کنید.</td>
</tr>
<tr><td><code>rules</code> <B>[الزامی]</B><br/>
<a href="#audit-k8s-io-v1-PolicyRule"><code>[]PolicyRule</code></a>
</td>
<td>
   <p>Rules مشخص می‌کنند که یک درخواست باید در کدام سطح ممیزی (Level) ثبت شود.
یک درخواست ممکن است با چندین قانون مطابقت داشته باشد؛ در این صورت، اولین قانون منطبق استفاده می‌شود.
سطح ممیزی پیش‌فرض None است، اما می‌توان آن را با یک قانون فراگیر (catch-all) در انتهای فهرست بازنویسی کرد.
PolicyRuleها کاملاً مرتب‌شده هستند.</p>
</td>
</tr>
<tr><td><code>omitStages</code><br/>
<a href="#audit-k8s-io-v1-Stage"><code>[]Stage</code></a>
</td>
<td>
   <p>OmitStages فهرستی از مراحل است که برای آن‌ها هیچ رویدادی ایجاد نمی‌شود. توجه کنید که این مورد را
می‌توان برای هر قانون نیز مشخص کرد؛ در آن صورت، اجتماع هر دو حذف می‌شود.</p>
</td>
</tr>
<tr><td><code>omitManagedFields</code><br/>
<code>bool</code>
</td>
<td>
   <p>OmitManagedFields مشخص می‌کند که آیا فیلدهای مدیریت‌شده (managed fields) در بدنه درخواست
و پاسخ از نوشته شدن در لاگ ممیزی API حذف شوند یا خیر.
این فیلد به‌عنوان مقدار پیش‌فرض سراسری استفاده می‌شود؛ مقدار 'true' فیلدهای مدیریت‌شده را حذف می‌کند،
و در غیر این صورت فیلدهای مدیریت‌شده در لاگ ممیزی API گنجانده می‌شوند.
توجه کنید که این مورد را می‌توان برای هر قانون نیز مشخص کرد؛ در آن صورت مقداری که در یک قانون
تعیین شده است، مقدار پیش‌فرض سراسری را بازنویسی می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `PolicyList`     {#audit-k8s-io-v1-PolicyList}
    


<p>PolicyList فهرستی از Policyهای ممیزی است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>audit.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>PolicyList</code></td></tr>
    
  
<tr><td><code>metadata</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#listmeta-v1-meta"><code>meta/v1.ListMeta</code></a>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>items</code> <B>[الزامی]</B><br/>
<a href="#audit-k8s-io-v1-Policy"><code>[]Policy</code></a>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `AuthenticationMetadata`     {#audit-k8s-io-v1-AuthenticationMetadata}
    

**در این بخش‌ها ظاهر می‌شود:**

- [Event](#audit-k8s-io-v1-Event)



<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>impersonationConstraint</code><br/>
<code>string</code>
</td>
<td>
   <p>ImpersonationConstraint فعلی (verb) است که با حالت جعل هویت محدودشده (constrained impersonation) مرتبط است و برای مجوزدهی
به ImpersonatedUser مرتبط با این رویداد ممیزی استفاده شده است. این فیلد فقط زمانی مقداردهی می‌شود که از جعل هویت محدودشده استفاده شده باشد.</p>
</td>
</tr>
</tbody>
</table>

## `GroupResources`     {#audit-k8s-io-v1-GroupResources}
    

**در این بخش‌ها ظاهر می‌شود:**

- [PolicyRule](#audit-k8s-io-v1-PolicyRule)


<p>GroupResources نشان‌دهنده انواع منابع در یک گروه API است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>group</code><br/>
<code>string</code>
</td>
<td>
   <p>Group نام گروه API است که منابع را در بر می‌گیرد.
رشته خالی نشان‌دهنده گروه API هسته (core) است.
<code>*</code> با همه گروه‌ها مطابقت دارد.</p>
</td>
</tr>
<tr><td><code>resources</code><br/>
<code>[]string</code>
</td>
<td>
   <p>Resources فهرستی از منابعی است که این قانون روی آن‌ها اعمال می‌شود.</p>
<p>برای مثال:</p>
<ul>
<li><code>pods</code> با podها مطابقت دارد.</li>
<li><code>pods/log</code> با زیرمنبع log مربوط به podها مطابقت دارد.</li>
<li><code>*</code> با همه منابع و زیرمنابع آن‌ها مطابقت دارد.</li>
<li><code>pods/*</code> با همه زیرمنابع podها مطابقت دارد.</li>
<li><code>*/scale</code> با همه زیرمنابع scale مطابقت دارد.</li>
</ul>
<p>اگر wildcard وجود داشته باشد، قانون اعتبارسنجی اطمینان حاصل می‌کند که منابع
با یکدیگر همپوشانی نداشته باشند.</p>
<p>فهرست خالی به این معناست که همه منابع و زیرمنابع در این گروه‌های API اعمال می‌شوند.</p>
</td>
</tr>
<tr><td><code>resourceNames</code><br/>
<code>[]string</code>
</td>
<td>
   <p>ResourceNames فهرستی از نام نمونه‌های منبع است که سیاست با آن‌ها مطابقت دارد.
استفاده از این فیلد مستلزم مشخص کردن Resources است.
فهرست خالی به این معناست که با هر نمونه از منبع مطابقت دارد.</p>
</td>
</tr>
</tbody>
</table>

## `Level`     {#audit-k8s-io-v1-Level}
    
(نام مستعار برای `string`)

**در این بخش‌ها ظاهر می‌شود:**

- [Event](#audit-k8s-io-v1-Event)

- [PolicyRule](#audit-k8s-io-v1-PolicyRule)


<p>Level میزان اطلاعاتی را که در طول ممیزی ثبت می‌شود تعریف می‌کند.</p>




## `ObjectReference`     {#audit-k8s-io-v1-ObjectReference}
    

**در این بخش‌ها ظاهر می‌شود:**

- [Event](#audit-k8s-io-v1-Event)


<p>ObjectReference اطلاعات کافی را در اختیار شما قرار می‌دهد تا بتوانید آبجکت ارجاع‌شده را بررسی یا اصلاح کنید.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>resource</code><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>namespace</code><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>uid</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID"><code>k8s.io/apimachinery/pkg/types.UID</code></a>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>apiGroup</code><br/>
<code>string</code>
</td>
<td>
   <p>APIGroup نام گروه API است که آبجکت ارجاع‌شده را در بر می‌گیرد.
رشته خالی نشان‌دهنده گروه API هسته (core) است.</p>
</td>
</tr>
<tr><td><code>apiVersion</code><br/>
<code>string</code>
</td>
<td>
   <p>APIVersion نسخه‌ای از گروه API است که آبجکت ارجاع‌شده را در بر می‌گیرد.</p>
</td>
</tr>
<tr><td><code>resourceVersion</code><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>subresource</code><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `PolicyRule`     {#audit-k8s-io-v1-PolicyRule}
    

**در این بخش‌ها ظاهر می‌شود:**

- [Policy](#audit-k8s-io-v1-Policy)


<p>PolicyRule درخواست‌ها را بر اساس فراداده (metadata) به یک سطح ممیزی (Level) نگاشت می‌کند.
درخواست‌ها باید با قوانین هر فیلد مطابقت داشته باشند (اشتراک قوانین).</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>level</code> <B>[الزامی]</B><br/>
<a href="#audit-k8s-io-v1-Level"><code>Level</code></a>
</td>
<td>
   <p>سطحی (Level) که درخواست‌های منطبق با این قانون در آن ثبت می‌شوند.</p>
</td>
</tr>
<tr><td><code>users</code><br/>
<code>[]string</code>
</td>
<td>
   <p>کاربرانی (بر اساس نام کاربر احراز هویت‌شده) که این قانون روی آن‌ها اعمال می‌شود.
فهرست خالی به این معناست که همه کاربران را شامل می‌شود.</p>
</td>
</tr>
<tr><td><code>userGroups</code><br/>
<code>[]string</code>
</td>
<td>
   <p>گروه‌های کاربری که این قانون روی آن‌ها اعمال می‌شود. کاربر در صورتی منطبق در نظر گرفته می‌شود
که عضو هر یک از UserGroups باشد.
فهرست خالی به این معناست که همه گروه‌های کاربری را شامل می‌شود.</p>
</td>
</tr>
<tr><td><code>verbs</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فعل‌هایی (verbs) که با این قانون مطابقت دارند.
فهرست خالی به این معناست که همه فعل‌ها را شامل می‌شود.</p>
</td>
</tr>
<tr><td><code>resources</code><br/>
<a href="#audit-k8s-io-v1-GroupResources"><code>[]GroupResources</code></a>
</td>
<td>
   <p>منابعی که این قانون با آن‌ها مطابقت دارد. فهرست خالی به این معناست که همه انواع در همه گروه‌های API را شامل می‌شود.</p>
</td>
</tr>
<tr><td><code>namespaces</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فضاهای نام (Namespaces) که این قانون با آن‌ها مطابقت دارد.
رشته خالی &quot;&quot; با منابعی که به فضای نام تعلق ندارند (non-namespaced) مطابقت دارد.
فهرست خالی به این معناست که همه فضاهای نام را شامل می‌شود.</p>
</td>
</tr>
<tr><td><code>nonResourceURLs</code><br/>
<code>[]string</code>
</td>
<td>
   <p>NonResourceURLs مجموعه‌ای از مسیرهای URL است که باید ممیزی شوند.
استفاده از <code>*</code> مجاز است، اما فقط به‌عنوان گام کامل و پایانی مسیر.
مثال‌ها:</p>
<ul>
<li><code>/metrics</code> - ثبت درخواست‌های مربوط به متریک‌های apiserver</li>
<li><code>/healthz*</code> - ثبت همه بررسی‌های سلامت (health checks)</li>
</ul>
</td>
</tr>
<tr><td><code>omitStages</code><br/>
<a href="#audit-k8s-io-v1-Stage"><code>[]Stage</code></a>
</td>
<td>
   <p>OmitStages فهرستی از مراحل است که برای آن‌ها هیچ رویدادی ایجاد نمی‌شود. توجه کنید که این مورد را
می‌توان در سطح کل سیاست نیز مشخص کرد؛ در آن صورت، اجتماع هر دو حذف می‌شود.
فهرست خالی به این معناست که هیچ محدودیتی اعمال نخواهد شد.</p>
</td>
</tr>
<tr><td><code>omitManagedFields</code><br/>
<code>bool</code>
</td>
<td>
   <p>OmitManagedFields مشخص می‌کند که آیا فیلدهای مدیریت‌شده (managed fields) در بدنه درخواست
و پاسخ از نوشته شدن در لاگ ممیزی API حذف شوند یا خیر.</p>
<ul>
<li>مقدار 'true' فیلدهای مدیریت‌شده را از لاگ ممیزی API حذف می‌کند</li>
<li>مقدار 'false' نشان می‌دهد که فیلدهای مدیریت‌شده باید در لاگ ممیزی API
گنجانده شوند
توجه کنید که مقدار مشخص‌شده در این قانون، در صورت وجود، مقدار پیش‌فرض سراسری را بازنویسی می‌کند
و اگر مقداری مشخص نشده باشد، مقدار پیش‌فرض سراسری که در
Policy.OmitManagedFields تعیین شده است معتبر خواهد بود.</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `Stage`     {#audit-k8s-io-v1-Stage}
    
(نام مستعار برای `string`)

**در این بخش‌ها ظاهر می‌شود:**

- [Event](#audit-k8s-io-v1-Event)

- [Policy](#audit-k8s-io-v1-Policy)

- [PolicyRule](#audit-k8s-io-v1-PolicyRule)


<p>Stage مراحلی از پردازش درخواست را تعریف می‌کند که رویدادهای ممیزی ممکن است در آن‌ها تولید شوند.</p>
