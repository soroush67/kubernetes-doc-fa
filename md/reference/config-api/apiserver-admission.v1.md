---
title: kube-apiserver Admission (v1)
content_type: tool-reference
package: admission.k8s.io/v1
auto_generated: true
---


## انواع منابع {#resource-types}


- [AdmissionReview](#admission-k8s-io-v1-AdmissionReview)
  

## `AdmissionReview`     {#admission-k8s-io-v1-AdmissionReview}
    


<p>AdmissionReview یک درخواست/پاسخ بازبینی پذیرش (admission review) را توصیف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>admission.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>AdmissionReview</code></td></tr>
    
  
<tr><td><code>request</code><br/>
<a href="#admission-k8s-io-v1-AdmissionRequest"><code>AdmissionRequest</code></a>
</td>
<td>
   <p>request ویژگی‌های درخواست پذیرش را توصیف می‌کند.</p>
</td>
</tr>
<tr><td><code>response</code><br/>
<a href="#admission-k8s-io-v1-AdmissionResponse"><code>AdmissionResponse</code></a>
</td>
<td>
   <p>response ویژگی‌های پاسخ پذیرش را توصیف می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `AdmissionRequest`     {#admission-k8s-io-v1-AdmissionRequest}
    

**نمایش داده‌شده در:**

- [AdmissionReview](#admission-k8s-io-v1-AdmissionReview)


<p>AdmissionRequest مقدار admission.Attributes را برای درخواست پذیرش توصیف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>uid</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID"><code>k8s.io/apimachinery/pkg/types.UID</code></a>
</td>
<td>
   <p>uid شناسه‌ای برای هر درخواست/پاسخ مجزا است. این شناسه امکان تمایز نمونه‌های درخواستی را فراهم می‌کند که در غیر این صورت یکسان هستند
(درخواست‌های موازی، درخواست‌هایی که درخواست‌های قبلی آن‌ها چیزی را تغییر نداده‌اند و غیره).
UID برای ردیابی رفت‌وبرگشت (درخواست/پاسخ) میان KAS و WebHook در نظر گرفته شده است، نه درخواست کاربر.
این شناسه برای تطبیق ورودی‌های لاگ میان webhook و apiserver، چه برای ممیزی (auditing) و چه برای اشکال‌زدایی، مناسب است.</p>
</td>
</tr>
<tr><td><code>kind</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionKind"><code>meta/v1.GroupVersionKind</code></a>
</td>
<td>
   <p>kind نوع کاملاً مشخص‌شده (fully-qualified) آبجکتی است که ارسال می‌شود (برای مثال v1.Pod یا autoscaling.v1.Scale)</p>
</td>
</tr>
<tr><td><code>resource</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionResource"><code>meta/v1.GroupVersionResource</code></a>
</td>
<td>
   <p>resource منبع کاملاً مشخص‌شده‌ای است که درخواست شده است (برای مثال v1.pods)</p>
</td>
</tr>
<tr><td><code>subResource</code><br/>
<code>string</code>
</td>
<td>
   <p>subResource زیرمنبعی است که درخواست شده است، در صورت وجود (برای مثال &quot;status&quot; یا &quot;scale&quot;)</p>
</td>
</tr>
<tr><td><code>requestKind</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionKind"><code>meta/v1.GroupVersionKind</code></a>
</td>
<td>
   <p>requestKind نوع کاملاً مشخص‌شده درخواست اولیه API است (برای مثال v1.Pod یا autoscaling.v1.Scale).
اگر این مقدار مشخص شده باشد و با مقدار موجود در &quot;kind&quot; تفاوت داشته باشد، تطبیق و تبدیل معادل انجام شده است.</p>
<p>برای مثال، اگر Deploymentها را بتوان از طریق apps/v1 و apps/v1beta1 تغییر داد، و یک webhook قاعده‌ای با مقدار
<code>apiGroups:[&quot;apps&quot;], apiVersions:[&quot;v1&quot;], resources: [&quot;deployments&quot;]</code> و <code>matchPolicy: Equivalent</code> ثبت کرده باشد،
یک درخواست API به Deploymentهای apps/v1beta1 تبدیل می‌شود و به webhook ارسال می‌گردد
با <code>kind: {group:&quot;apps&quot;, version:&quot;v1&quot;, kind:&quot;Deployment&quot;}</code> (مطابق قاعده‌ای که webhook برای آن ثبت شده است)،
و <code>requestKind: {group:&quot;apps&quot;, version:&quot;v1beta1&quot;, kind:&quot;Deployment&quot;}</code> (که نشان‌دهنده نوع درخواست اولیه API است).</p>
<p>برای جزئیات بیشتر، مستندات فیلد &quot;matchPolicy&quot; را در نوع پیکربندی webhook ببینید.</p>
</td>
</tr>
<tr><td><code>requestResource</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#GroupVersionResource"><code>meta/v1.GroupVersionResource</code></a>
</td>
<td>
   <p>requestResource منبع کاملاً مشخص‌شده درخواست اولیه API است (برای مثال v1.pods).
اگر این مقدار مشخص شده باشد و با مقدار موجود در &quot;resource&quot; تفاوت داشته باشد، تطبیق و تبدیل معادل انجام شده است.</p>
<p>برای مثال، اگر Deploymentها را بتوان از طریق apps/v1 و apps/v1beta1 تغییر داد، و یک webhook قاعده‌ای با مقدار
<code>apiGroups:[&quot;apps&quot;], apiVersions:[&quot;v1&quot;], resources: [&quot;deployments&quot;]</code> و <code>matchPolicy: Equivalent</code> ثبت کرده باشد،
یک درخواست API به Deploymentهای apps/v1beta1 تبدیل می‌شود و به webhook ارسال می‌گردد
با <code>resource: {group:&quot;apps&quot;, version:&quot;v1&quot;, resource:&quot;deployments&quot;}</code> (مطابق منبعی که webhook برای آن ثبت شده است)،
و <code>requestResource: {group:&quot;apps&quot;, version:&quot;v1beta1&quot;, resource:&quot;deployments&quot;}</code> (که نشان‌دهنده منبع درخواست اولیه API است).</p>
<p>مستندات فیلد &quot;matchPolicy&quot; را در نوع پیکربندی webhook ببینید.</p>
</td>
</tr>
<tr><td><code>requestSubResource</code><br/>
<code>string</code>
</td>
<td>
   <p>requestSubResource نام زیرمنبع درخواست اولیه API است، در صورت وجود (برای مثال &quot;status&quot; یا &quot;scale&quot;).
اگر این مقدار مشخص شده باشد و با مقدار موجود در &quot;subResource&quot; تفاوت داشته باشد، تطبیق و تبدیل معادل انجام شده است.
مستندات فیلد &quot;matchPolicy&quot; را در نوع پیکربندی webhook ببینید.</p>
</td>
</tr>
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <p>name نام آبجکت است، همان‌گونه که در درخواست ارائه شده است. در عملیات CREATE، کلاینت می‌تواند name را حذف کند و
تولید نام را به سرور واگذار کند. در این صورت، این فیلد حاوی یک رشته خالی خواهد بود.</p>
</td>
</tr>
<tr><td><code>namespace</code><br/>
<code>string</code>
</td>
<td>
   <p>namespace فضای نامی (namespace) است که با درخواست مرتبط است (در صورت وجود).</p>
</td>
</tr>
<tr><td><code>operation</code><br/>
<a href="#admission-k8s-io-v1-Operation"><code>Operation</code></a>
</td>
<td>
   <p>operation عملیاتی است که در حال انجام است. این عملیات ممکن است با عملیات درخواست‌شده متفاوت باشد.
برای مثال، یک patch می‌تواند به عملیات CREATE یا UPDATE منجر شود.</p>
</td>
</tr>
<tr><td><code>userInfo</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#userinfo-v1-authentication-k8s-io"><code>authentication/v1.UserInfo</code></a>
</td>
<td>
   <p>userInfo اطلاعاتی درباره کاربر درخواست‌دهنده است</p>
</td>
</tr>
<tr><td><code>object</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension"><code>k8s.io/apimachinery/pkg/runtime.RawExtension</code></a>
</td>
<td>
   <p>object آبجکتی است که در درخواست ورودی قرار دارد.</p>
</td>
</tr>
<tr><td><code>oldObject</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension"><code>k8s.io/apimachinery/pkg/runtime.RawExtension</code></a>
</td>
<td>
   <p>oldObject آبجکت موجود است. فقط برای درخواست‌های DELETE و UPDATE مقداردهی می‌شود.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p>dryRun نشان می‌دهد که تغییرات برای این درخواست قطعاً پایدار (persist) نخواهند شد.
مقدار پیش‌فرض آن false است.</p>
</td>
</tr>
<tr><td><code>options</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension"><code>k8s.io/apimachinery/pkg/runtime.RawExtension</code></a>
</td>
<td>
   <p>options ساختار گزینه‌های عملیاتی است که در حال انجام است.
برای مثال <code>meta.k8s.io/v1.DeleteOptions</code> یا <code>meta.k8s.io/v1.CreateOptions</code>. این مقدار ممکن است
با گزینه‌هایی که فراخواننده ارائه کرده است متفاوت باشد. برای مثال، در یک درخواست patch
عملیات انجام‌شده ممکن است CREATE باشد؛ در این صورت Options از نوع
<code>meta.k8s.io/v1.CreateOptions</code> خواهد بود، حتی اگر فراخواننده <code>meta.k8s.io/v1.PatchOptions</code> را ارائه کرده باشد.</p>
</td>
</tr>
</tbody>
</table>

## `AdmissionResponse`     {#admission-k8s-io-v1-AdmissionResponse}
    

**نمایش داده‌شده در:**

- [AdmissionReview](#admission-k8s-io-v1-AdmissionReview)


<p>AdmissionResponse یک پاسخ پذیرش را توصیف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>uid</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/types#UID"><code>k8s.io/apimachinery/pkg/types.UID</code></a>
</td>
<td>
   <p>uid شناسه‌ای برای هر درخواست/پاسخ مجزا است.
این مقدار باید از AdmissionRequest متناظر کپی شود.</p>
</td>
</tr>
<tr><td><code>allowed</code><br/>
<code>bool</code>
</td>
<td>
   <p>allowed نشان می‌دهد که درخواست پذیرش مجاز شمرده شده است یا خیر.</p>
</td>
</tr>
<tr><td><code>status</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#status-v1-meta"><code>meta/v1.Status</code></a>
</td>
<td>
   <p>status نتیجه‌ای است که جزئیات اضافی درباره دلیل رد شدن یک درخواست پذیرش را در بر دارد.
اگر مقدار &quot;Allowed&quot; برابر &quot;true&quot; باشد، این فیلد به هیچ وجه بررسی نمی‌شود.</p>
</td>
</tr>
<tr><td><code>patch</code><br/>
<code>[]byte</code>
</td>
<td>
   <p>patch بدنه وصله (patch) است. در حال حاضر فقط &quot;JSONPatch&quot; پشتیبانی می‌شود که RFC 6902 را پیاده‌سازی می‌کند.</p>
</td>
</tr>
<tr><td><code>patchType</code><br/>
<a href="#admission-k8s-io-v1-PatchType"><code>PatchType</code></a>
</td>
<td>
   <p>patchType نوع Patch است. در حال حاضر فقط &quot;JSONPatch&quot; مجاز است.</p>
</td>
</tr>
<tr><td><code>auditAnnotations</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>auditAnnotations یک نگاشت کلید-مقدار بدون ساختار است که توسط admission controller راه دور تنظیم می‌شود (برای مثال error=image-blacklisted).
admission controllerهای MutatingAdmissionWebhook و ValidatingAdmissionWebhook کلیدها را با
نام admission webhook پیشوندگذاری می‌کنند (برای مثال imagepolicy.example.com/error=image-blacklisted). AuditAnnotations توسط
admission webhook ارائه می‌شود تا زمینه اضافی را به لاگ ممیزی این درخواست بیفزاید.</p>
</td>
</tr>
<tr><td><code>warnings</code><br/>
<code>[]string</code>
</td>
<td>
   <p>warnings فهرستی از پیام‌های هشدار است که به کلاینت API درخواست‌دهنده بازگردانده می‌شود.
پیام‌های هشدار مشکلی را توصیف می‌کنند که کلاینتِ ارسال‌کننده درخواست API باید آن را اصلاح کند یا از آن آگاه باشد.
در صورت امکان، هشدارها را به ۱۲۰ نویسه محدود کنید.
هشدارهای بیش از ۲۵۶ نویسه و تعداد زیاد هشدارها ممکن است کوتاه (truncate) شوند.</p>
</td>
</tr>
</tbody>
</table>

## `Operation`     {#admission-k8s-io-v1-Operation}
    
(نام مستعار برای `string`)

**نمایش داده‌شده در:**

- [AdmissionRequest](#admission-k8s-io-v1-AdmissionRequest)


<p>Operation نوع عملیات منبعی است که برای کنترل پذیرش بررسی می‌شود</p>




## `PatchType`     {#admission-k8s-io-v1-PatchType}
    
(نام مستعار برای `string`)

**نمایش داده‌شده در:**

- [AdmissionResponse](#admission-k8s-io-v1-AdmissionResponse)


<p>PatchType نوع وصله‌ای است که برای نمایش آبجکت تغییریافته استفاده می‌شود</p>
