---
title: پیکربندی Event Rate Limit (v1alpha1)
content_type: tool-reference
package: eventratelimit.admission.k8s.io/v1alpha1
auto_generated: true
---


## انواع منابع 


- [Configuration](#eventratelimit-admission-k8s-io-v1alpha1-Configuration)
  

## `Configuration`     {#eventratelimit-admission-k8s-io-v1alpha1-Configuration}
    


<p>Configuration پیکربندی مربوط به admission controller با نام EventRateLimit را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>eventratelimit.admission.k8s.io/v1alpha1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>Configuration</code></td></tr>
    
  
<tr><td><code>limits</code> <B>[Required]</B><br/>
<a href="#eventratelimit-admission-k8s-io-v1alpha1-Limit"><code>[]Limit</code></a>
</td>
<td>
   <p>limits محدودیت‌هایی هستند که بر درخواست‌های رویداد (event) دریافت‌شده اعمال می‌شوند.
محدودیت‌ها را می‌توان بر رویدادهای دریافت‌شده در سطح کل سرور، به‌ازای هر فضای نام (namespace)،
به‌ازای هر کاربر و به‌ازای هر ترکیب منبع+آبجکت (source+object) اعمال کرد.
حداقل یک محدودیت الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `Limit`     {#eventratelimit-admission-k8s-io-v1alpha1-Limit}
    

**در این بخش‌ها ظاهر می‌شود:**

- [Configuration](#eventratelimit-admission-k8s-io-v1alpha1-Configuration)


<p>Limit پیکربندی مربوط به یک نوع محدودیت مشخص است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>type</code> <B>[Required]</B><br/>
<a href="#eventratelimit-admission-k8s-io-v1alpha1-LimitType"><code>LimitType</code></a>
</td>
<td>
   <p>type نوع محدودیتی است که این پیکربندی بر آن اعمال می‌شود.</p>
</td>
</tr>
<tr><td><code>qps</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>qps تعداد درخواست‌های رویداد در هر ثانیه است که برای این نوع محدودیت مجاز شمرده می‌شود.
فیلدهای qps و burst با هم برای تعیین پذیرفته‌شدن یا نشدن یک درخواست رویداد مشخص به کار می‌روند.
qps تعیین می‌کند که پس از تمام‌شدن سهم burst درخواست‌ها، چه تعداد درخواست پذیرفته شود.</p>
</td>
</tr>
<tr><td><code>burst</code> <B>[Required]</B><br/>
<code>int32</code>
</td>
<td>
   <p>burst تعداد درخواست‌های رویداد در حالت burst است که برای این نوع محدودیت مجاز شمرده می‌شود.
فیلدهای qps و burst با هم برای تعیین پذیرفته‌شدن یا نشدن یک درخواست رویداد مشخص به کار می‌روند.
burst حداکثر اندازهٔ سهمیه‌ای را تعیین می‌کند که به یک bucket مشخص داده می‌شود.
برای مثال، اگر burst برابر ۱۰ و qps برابر ۳ باشد، admission control ابتدا ۱۰ درخواست را
می‌پذیرد و پس از آن درخواست‌ها را مسدود می‌کند. در هر ثانیه ۳ درخواست دیگر مجاز خواهد بود.
اگر بخشی از این سهمیه استفاده نشود، به ثانیهٔ بعد منتقل می‌شود،
تا زمانی که به حداکثر سهمیهٔ ۱۰ برسد.</p>
</td>
</tr>
<tr><td><code>cacheSize</code><br/>
<code>int32</code>
</td>
<td>
   <p>cacheSize اندازهٔ حافظهٔ نهان LRU برای این نوع محدودیت است. اگر یک bucket
از حافظهٔ نهان حذف شود، سهمیهٔ آن bucket بازنشانی می‌شود. اگر بعداً
درخواست‌های بیشتری برای یک bucket حذف‌شده دریافت شود، آن bucket
با وضعیتی تازه دوباره وارد حافظهٔ نهان می‌شود و یک سهمیهٔ کامل
از درخواست‌های burst به آن داده می‌شود.</p>
<p>اندازهٔ پیش‌فرض حافظهٔ نهان ۴۰۹۶ است.</p>
<p>اگر limitType برابر 'server' باشد، cacheSize نادیده گرفته می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `LimitType`     {#eventratelimit-admission-k8s-io-v1alpha1-LimitType}
    
(نام مستعار برای `string`)

**در این بخش‌ها ظاهر می‌شود:**

- [Limit](#eventratelimit-admission-k8s-io-v1alpha1-Limit)


<p>LimitType نوع محدودیت است (برای مثال، به‌ازای هر فضای نام (namespace)).</p>
