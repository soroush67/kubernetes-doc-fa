---
title: kuberc (v1beta1)
content_type: tool-reference
package: kubectl.config.k8s.io/v1beta1
auto_generated: true
---


## انواع منابع (Resource Types)


- [Preference](#kubectl-config-k8s-io-v1beta1-Preference)
  

## `Preference`     {#kubectl-config-k8s-io-v1beta1-Preference}
    


<p>Preference عناصر فایل پیکربندی KubeRC را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubectl.config.k8s.io/v1beta1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>Preference</code></td></tr>
    
  
<tr><td><code>defaults</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1beta1-CommandDefaults"><code>[]CommandDefaults</code></a>
</td>
<td>
   <p>defaults امکان تغییر مقادیر پیش‌فرض گزینه‌های دستورها را فراهم می‌کند.
این قابلیت به‌ویژه زمانی مفید است که کاربر نمی‌خواهد هر بار گزینه‌ها را
به‌صورت صریح تنظیم کند.</p>
</td>
</tr>
<tr><td><code>aliases</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1beta1-AliasOverride"><code>[]AliasOverride</code></a>
</td>
<td>
   <p>aliases امکان تعریف نام‌های مستعار (alias) برای دستورهای موجود kubectl را، همراه با مقادیر پیش‌فرض اختیاری برای گزینه‌ها، فراهم می‌کند.
اگر نام alias با یک دستور داخلی تداخل داشته باشد، دستور داخلی همیشه اولویت دارد.
بازنویسی‌های گزینه‌ها که در بخش defaults تعریف شده‌اند، بر aliasهای مربوط به همان دستور اعمال نمی‌شوند.
عبارت kubectl [ALIAS NAME] [USER_OPTIONS] [USER_EXPLICIT_ARGS] به شکل زیر گسترش می‌یابد:
kubectl [COMMAND] # دستور داخلی که alias به آن اشاره می‌کند
[KUBERC_PREPEND_ARGS]
[USER_OPTIONS]
[KUBERC_OPTIONS] # سایر گزینه‌هایی که کاربر در [USER_OPTIONS] ارسال نکرده است
[USER_EXPLICIT_ARGS]
[KUBERC_APPEND_ARGS]
برای مثال:</p>
<ul>
<li>name: runx
command: run
options:
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
options:
<ul>
<li>name: output
default: wide
prependArgs:</li>
<li>node
دستور &quot;kubectl getn control-plane-1&quot; به &quot;kubectl get node control-plane-1 --output=wide&quot; گسترش می‌یابد.
دستور &quot;kubectl getn control-plane-1 --output=json&quot; به &quot;kubectl get node --output=json control-plane-1&quot; گسترش می‌یابد.</li>
</ul>
</li>
</ul>
</td>
</tr>
<tr><td><code>credentialPluginPolicy</code><br/>
<a href="#kubectl-config-k8s-io-v1beta1-CredentialPluginPolicy"><code>CredentialPluginPolicy</code></a>
</td>
<td>
   <p>credentialPluginPolicy سیاستی را مشخص می‌کند که تعیین می‌کند کدام یک از افزونه‌های اعتبارنامه (credential plugin) در client-go، در صورت وجود، اجازه اجرا دارند. مقدار آن باید یکی از { &quot;&quot;, &quot;AllowAll&quot;, &quot;DenyAll&quot;, &quot;Allowlist&quot; } باشد.
اگر سیاست برابر &quot;&quot; باشد، به &quot;AllowAll&quot; بازمی‌گردد (این کار برای حفظ سازگاری با نسخه‌های قبلی لازم است). اگر سیاست DenyAll باشد، هیچ
افزونه اعتبارنامه‌ای اجازه اجرا نخواهد داشت. اگر سیاست Allowlist باشد، فقط افزونه‌هایی
اجازه اجرا دارند که معیارهای مشخص‌شده در فیلد <code>credentialPluginAllowlist</code>
را برآورده کنند.</p>
</td>
</tr>
<tr><td><code>credentialPluginAllowlist</code><br/>
<a href="#kubectl-config-k8s-io-v1beta1-AllowlistEntry"><code>[]AllowlistEntry</code></a>
</td>
<td>
   <p>Allowlist فهرستی از ورودی‌های allowlist است. اگر هر یک از آن‌ها مطابقت داشته باشد،
فایل اجرایی مورد نظر اجازه اجرا دارد. یعنی نتیجه، OR منطقی
همه ورودی‌های allowlist است. اگر سیاست برابر &quot;Allowlist&quot; نباشد، این فهرست نباید
ارائه شود.</p>
<p>برای مثال:
credentialPluginAllowlist:</p>
<ul>
<li>name: cloud-provider-plugin</li>
<li>name: /usr/local/bin/my-plugin
در مثال بالا، کاربر به افزونه‌های اعتبارنامه
<code>cloud-provider-plugin</code> (که در جایی از PATH یافت می‌شود) و افزونه‌ای که در
مسیر صریح <code>/usr/local/bin/my-plugin</code> قرار دارد، اجازه اجرا می‌دهد.</li>
</ul>
</td>
</tr>
</tbody>
</table>

## `AliasOverride`     {#kubectl-config-k8s-io-v1beta1-AliasOverride}
    

**Appears in:**

- [Preference](#kubectl-config-k8s-io-v1beta1-Preference)


<p>AliasOverride تعریف‌های alias را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>name نام alias است که فقط می‌تواند شامل نویسه‌های الفبایی باشد.
اگر نام alias با یک دستور داخلی تداخل داشته باشد،
دستور داخلی استفاده می‌شود.</p>
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
   <p>prependArgs آرگومان‌هایی مانند نام منابع و غیره را ذخیره می‌کند.
این آرگومان‌ها پس از نام alias درج می‌شوند.</p>
</td>
</tr>
<tr><td><code>appendArgs</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>appendArgs آرگومان‌هایی مانند نام منابع و غیره را ذخیره می‌کند.
این آرگومان‌ها به انتهای USER_ARGS افزوده می‌شوند.</p>
</td>
</tr>
<tr><td><code>options</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1beta1-CommandOptionDefault"><code>[]CommandOptionDefault</code></a>
</td>
<td>
   <p>options برای ذخیره تعریف‌های گزینه‌های alias در نظر گرفته شده است.
options فقط مقدار پیش‌فرض گزینه را تغییر می‌دهد و اگر
کاربر مقداری را به‌صورت صریح ارسال کند، مقدار صریح استفاده می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `AllowlistEntry`     {#kubectl-config-k8s-io-v1beta1-AllowlistEntry}
    

**Appears in:**

- [Preference](#kubectl-config-k8s-io-v1beta1-Preference)


<p>AllowlistEntry یک ورودی در allowlist است. برای هر مورد allowlist، دست‌کم
یک فیلد باید غیرخالی باشد. ساختاری که همه فیلدهای آن خالی باشد
خطای پیکربندی نادرست محسوب می‌شود. هر فیلد یک معیار برای
اجراست. اگر چند فیلد مشخص شده باشد، معیارهای همه
فیلدهای مشخص‌شده باید برآورده شوند. یعنی نتیجه یک ورودی منفرد
AND منطقی همه بررسی‌های متناظر با فیلدهای مشخص‌شده در
همان ورودی است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>تطبیق نام به این صورت انجام می‌شود که ابتدا مسیر مطلق هر دو مورد، یعنی افزونه
و نام موجود در ورودی allowlist، با استفاده از <code>exec.LookPath</code> تعیین می‌شود. این
تابع برای هر دو فراخوانی می‌شود و رشته‌های حاصل باید برابر باشند. اگر
هر یک از فراخوانی‌های <code>exec.LookPath</code> به خطا منجر شود، بررسی <code>Name</code>
شکست‌خورده در نظر گرفته می‌شود.</p>
<p>منسوخ‌شده: به‌جای آن از Command استفاده کنید.</p>
</td>
</tr>
<tr><td><code>command</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>تطبیق دستور به این صورت انجام می‌شود که ابتدا مسیر مطلق هر دو مورد، یعنی افزونه
و نام موجود در ورودی allowlist، با استفاده از <code>exec.LookPath</code> تعیین می‌شود. این
تابع برای هر دو فراخوانی می‌شود و رشته‌های حاصل باید برابر باشند. اگر
هر یک از فراخوانی‌های <code>exec.LookPath</code> به خطا منجر شود، بررسی <code>Command</code>
شکست‌خورده در نظر گرفته می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `CommandDefaults`     {#kubectl-config-k8s-io-v1beta1-CommandDefaults}
    

**Appears in:**

- [Preference](#kubectl-config-k8s-io-v1beta1-Preference)


<p>CommandDefaults دستورها و مقادیر پیش‌فرض گزینه‌های مرتبط با آن‌ها را
ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>command</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>command به دستوری اشاره دارد که مقدار پیش‌فرض گزینه‌های آن تغییر می‌کند.</p>
</td>
</tr>
<tr><td><code>options</code> <B>[Required]</B><br/>
<a href="#kubectl-config-k8s-io-v1beta1-CommandOptionDefault"><code>[]CommandOptionDefault</code></a>
</td>
<td>
   <p>options فهرستی از گزینه‌هاست که مقادیر پیش‌فرض متفاوتی را ذخیره می‌کنند.</p>
</td>
</tr>
</tbody>
</table>

## `CommandOptionDefault`     {#kubectl-config-k8s-io-v1beta1-CommandOptionDefault}
    

**Appears in:**

- [AliasOverride](#kubectl-config-k8s-io-v1beta1-AliasOverride)

- [CommandDefaults](#kubectl-config-k8s-io-v1beta1-CommandDefaults)


<p>CommandOptionDefault نام و مقدار پیش‌فرض مشخص‌شده
یک گزینه را ذخیره می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام گزینه (به شکل بلند، بدون خط تیره).</p>
</td>
</tr>
<tr><td><code>default</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>مقدار پیش‌فرض به‌صورت رشته. kubectl آن را
به مقدار سازگار با گزینه تبدیل (parse) می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `CredentialPluginPolicy`     {#kubectl-config-k8s-io-v1beta1-CredentialPluginPolicy}
    
(Alias of `string`)

**Appears in:**

- [Preference](#kubectl-config-k8s-io-v1beta1-Preference)


<p>CredentialPluginPolicy سیاستی را مشخص می‌کند که تعیین می‌کند کدام یک از افزونه‌های اعتبارنامه (credential plugin) در client-go، در صورت وجود، اجازه اجرا دارند. مقدار آن باید یکی از { &quot;&quot;, &quot;AllowAll&quot;, &quot;DenyAll&quot;, &quot;Allowlist&quot; } باشد.
اگر سیاست برابر &quot;&quot; باشد، به &quot;AllowAll&quot; بازمی‌گردد (این کار برای حفظ سازگاری با نسخه‌های قبلی لازم است). اگر سیاست DenyAll باشد، هیچ
افزونه اعتبارنامه‌ای اجازه اجرا نخواهد داشت. اگر سیاست Allowlist باشد، فقط افزونه‌هایی
اجازه اجرا دارند که معیارهای مشخص‌شده در فیلد <code>credentialPluginAllowlist</code>
را برآورده کنند. اگر سیاست <code>Allowlist</code> نباشد اما allowlist ارائه شده باشد،
این وضعیت خطای پیکربندی محسوب می‌شود.</p>
