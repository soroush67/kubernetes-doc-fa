---
title: kuberc (v1alpha1)
content_type: tool-reference
package: kubectl.config.k8s.io/v1alpha1
auto_generated: true
---


## انواع منبع (Resource Types) {#resource-types}


- [Preference](#kubectl-config-k8s-io-v1alpha1-Preference)
  

## `Preference`     {#kubectl-config-k8s-io-v1alpha1-Preference}
    


<p>Preference عناصر فایل پیکربندی KubeRC را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubectl.config.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>Preference</code></td></tr>
    
  
<tr><td><code>overrides</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1alpha1-CommandDefaults"><code>[]CommandDefaults</code></a>
</td>
<td>
   <p>overrides امکان تغییر مقادیر پیش‌فرض فلگ‌های دستورها را فراهم می‌کند.
این قابلیت به‌ویژه زمانی مفید است که کاربر نمی‌خواهد هر بار
فلگ‌ها را به‌صورت صریح تنظیم کند.</p>
</td>
</tr>
<tr><td><code>aliases</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1alpha1-AliasOverride"><code>[]AliasOverride</code></a>
</td>
<td>
   <p>aliases امکان تعریف نام‌های مستعار (alias) دستور را برای دستورهای موجود kubectl، همراه با مقادیر پیش‌فرض اختیاری فلگ‌ها فراهم می‌کند.
اگر نام alias با یکی از دستورهای داخلی (built-in) تداخل داشته باشد، دستور داخلی همیشه اولویت دارد.
بازنویسی‌های فلگ که در بخش overrides تعریف شده‌اند، برای aliasهای مربوط به همان دستور اعمال نمی‌شوند.
عبارت kubectl [ALIAS NAME] [USER_FLAGS] [USER_EXPLICIT_ARGS] به شکل زیر گسترش می‌یابد:
kubectl [COMMAND] # دستور داخلی که alias به آن اشاره می‌کند
[KUBERC_PREPEND_ARGS]
[USER_FLAGS]
[KUBERC_FLAGS] # بقیهٔ فلگ‌هایی که کاربر در [USER_FLAGS] ارائه نکرده است
[USER_EXPLICIT_ARGS]
[KUBERC_APPEND_ARGS]
برای مثال:</p>
<ul>
<li>name: runx
command: run
flags:
<ul>
<li>name: image
default: nginx
appendArgs:</li>
</ul>
<hr>
<ul>
<li>custom-arg1
برای مثال، اگر کاربر دستور &quot;kubectl runx test-pod&quot; را اجرا کند،
این دستور به &quot;kubectl run --image=nginx test-pod -- custom-arg1&quot; گسترش می‌یابد.</li>
</ul>
</li>
<li>name: getn
command: get
flags:
<ul>
<li>name: output
default: wide
prependArgs:</li>
<li>node
دستور &quot;kubectl getn control-plane-1&quot; به &quot;kubectl get node control-plane-1 --output=wide&quot; گسترش می‌یابد
و دستور &quot;kubectl getn control-plane-1 --output=json&quot; به &quot;kubectl get node --output=json control-plane-1&quot; گسترش می‌یابد.</li>
</ul>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `AliasOverride`     {#kubectl-config-k8s-io-v1alpha1-AliasOverride}
    

**ظاهر می‌شود در:**

- [Preference](#kubectl-config-k8s-io-v1alpha1-Preference)


<p>AliasOverride تعریف‌های alias را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام alias است و فقط می‌تواند شامل نویسه‌های الفبایی باشد.
اگر نام alias با یک دستور داخلی تداخل داشته باشد،
دستور داخلی استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>command</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>command یک دستور یا مجموعه‌ای از دستورها برای اجراست، مانند &quot;set env&quot; یا &quot;create&quot;.</p>
</td>
</tr>
<tr><td><code>prependArgs</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>prependArgs آرگومان‌هایی مانند نام منبع‌ها و موارد مشابه را ذخیره می‌کند.
این آرگومان‌ها پس از نام alias درج می‌شوند.</p>
</td>
</tr>
<tr><td><code>appendArgs</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>appendArgs آرگومان‌هایی مانند نام منبع‌ها و موارد مشابه را ذخیره می‌کند.
این آرگومان‌ها به انتهای USER_ARGS افزوده می‌شوند.</p>
</td>
</tr>
<tr><td><code>flags</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1alpha1-CommandOptionDefault"><code>[]CommandOptionDefault</code></a>
</td>
<td>
   <p>flags برای ذخیرهٔ تعریف‌های فلگ مربوط به alias در نظر گرفته شده است.
flags فقط مقدار پیش‌فرض فلگ را تغییر می‌دهد و اگر
کاربر مقداری را به‌صورت صریح ارائه کند، همان مقدار صریح استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `CommandDefaults`     {#kubectl-config-k8s-io-v1alpha1-CommandDefaults}
    

**ظاهر می‌شود در:**

- [Preference](#kubectl-config-k8s-io-v1alpha1-Preference)


<p>CommandDefaults دستورها و مقادیر پیش‌فرض گزینه‌های مرتبط با آن‌ها را
ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>command</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>command به دستوری اشاره می‌کند که مقدار پیش‌فرض فلگ آن تغییر می‌یابد.</p>
</td>
</tr>
<tr><td><code>flags</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1alpha1-CommandOptionDefault"><code>[]CommandOptionDefault</code></a>
</td>
<td>
   <p>flags فهرستی از فلگ‌هاست که مقادیر پیش‌فرض متفاوتی را ذخیره می‌کنند.</p>
</td>
</tr>
</tbody>
</table>

## `CommandOptionDefault`     {#kubectl-config-k8s-io-v1alpha1-CommandOptionDefault}
    

**ظاهر می‌شود در:**

- [AliasOverride](#kubectl-config-k8s-io-v1alpha1-AliasOverride)

- [CommandDefaults](#kubectl-config-k8s-io-v1alpha1-CommandDefaults)


<p>CommandOptionDefault نام و مقدار پیش‌فرض مشخص‌شدهٔ
یک گزینه را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام فلگ (به شکل بلند و بدون خط تیره).</p>
</td>
</tr>
<tr><td><code>default</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>مقدار پیش‌فرض به‌صورت رشته. این مقدار توسط
kubectl به مقدار سازگار با فلگ تبدیل (parse) می‌شود.</p>
</td>
</tr>
</tbody>
</table>
