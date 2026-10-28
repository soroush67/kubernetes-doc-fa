---
title: احراز هویت کلاینت (v1)
content_type: tool-reference
package: client.authentication.k8s.io/v1
auto_generated: true
---


## انواع منابع 


- [ExecCredential](#client-authentication-k8s-io-v1-ExecCredential)
  

## `ExecCredential`     {#client-authentication-k8s-io-v1-ExecCredential}
    


<p>ExecCredential توسط افزونه‌های مبتنی بر exec برای انتقال اعتبارنامه‌ها به
انتقال‌دهنده‌های HTTP (HTTP transports) استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>client.authentication.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ExecCredential</code></td></tr>
    
  
<tr><td><code>spec</code> <B>[الزامی]</B><br/>
<a href="#client-authentication-k8s-io-v1-ExecCredentialSpec"><code>ExecCredentialSpec</code></a>
</td>
<td>
   <p>Spec شامل اطلاعاتی است که انتقال‌دهنده (transport) به افزونه ارسال می‌کند.</p>
</td>
</tr>
<tr><td><code>status</code><br/>
<a href="#client-authentication-k8s-io-v1-ExecCredentialStatus"><code>ExecCredentialStatus</code></a>
</td>
<td>
   <p>Status توسط افزونه تکمیل می‌شود و شامل اعتبارنامه‌هایی است که انتقال‌دهنده
باید برای برقراری ارتباط با API از آن‌ها استفاده کند.</p>
</td>
</tr>
</tbody>
</table>

## `Cluster`     {#client-authentication-k8s-io-v1-Cluster}
    

**در این موارد ظاهر می‌شود:**

- [ExecCredentialSpec](#client-authentication-k8s-io-v1-ExecCredentialSpec)


<p>Cluster شامل اطلاعاتی است که به یک افزونه exec امکان می‌دهد با
کلاستر کوبرنتیزی که احراز هویت نسبت به آن انجام می‌شود ارتباط برقرار کند.</p>
<p>برای اطمینان از اینکه این ساختار (struct) همه‌ی اطلاعات لازم برای برقراری ارتباط
با یک کلاستر کوبرنتیز را در بر دارد (دقیقاً مانند ارتباط از طریق kubeconfig)، فیلدها
باید با &quot;k8s.io/client-go/tools/clientcmd/api/v1&quot;.Cluster هم‌خوان باشند، به‌جز
CertificateAuthority، زیرا داده‌های CA همواره به‌صورت بایت به افزونه ارسال می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>server</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Server نشانی کلاستر کوبرنتیز است (https://hostname:port).</p>
</td>
</tr>
<tr><td><code>tls-server-name</code><br/>
<code>string</code>
</td>
<td>
   <p>TLSServerName برای SNI به سرور ارسال می‌شود و در کلاینت برای بررسی
گواهی‌های سرور مورد استفاده قرار می‌گیرد. اگر ServerName خالی باشد، از نام میزبانی
که برای برقراری ارتباط با سرور استفاده شده است، استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>insecure-skip-tls-verify</code><br/>
<code>bool</code>
</td>
<td>
   <p>InsecureSkipTLSVerify بررسی اعتبار گواهی سرور را نادیده می‌گیرد.
این کار اتصالات HTTPS شما را ناامن می‌کند.</p>
</td>
</tr>
<tr><td><code>certificate-authority-data</code><br/>
<code>[]byte</code>
</td>
<td>
   <p>CAData شامل گواهی‌های مرجع صدور گواهی (certificate authority) با کدگذاری PEM است.
اگر خالی باشد، باید از ریشه‌های سیستم (system roots) استفاده شود.</p>
</td>
</tr>
<tr><td><code>proxy-url</code><br/>
<code>string</code>
</td>
<td>
   <p>ProxyURL نشانی URL پروکسی‌ای است که برای تمام درخواست‌ها به این
کلاستر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>disable-compression</code><br/>
<code>bool</code>
</td>
<td>
   <p>DisableCompression به کلاینت اجازه می‌دهد فشرده‌سازی پاسخ را برای تمام درخواست‌ها به سرور غیرفعال کند. این کار
زمانی که پهنای باند شبکه‌ی میان کلاینت و سرور فراوان است، با صرفه‌جویی در زمان
فشرده‌سازی (سمت سرور) و بازگشایی فشرده‌سازی (سمت کلاینت)، برای تسریع درخواست‌ها (به‌ویژه درخواست‌های list) مفید است: https://github.com/kubernetes/kubernetes/issues/112296.</p>
</td>
</tr>
<tr><td><code>config</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime/#RawExtension"><code>k8s.io/apimachinery/pkg/runtime.RawExtension</code></a>
</td>
<td>
   <p>Config شامل داده‌های پیکربندی اضافی است که مختص افزونه‌ی exec
و مربوط به کلاستری است که احراز هویت نسبت به آن انجام می‌شود.</p>
<p>این داده از فیلد extensions[client.authentication.k8s.io/exec]
در آبجکت Cluster مربوط به clientcmd دریافت می‌شود:</p>
<p>clusters:</p>
<ul>
<li>name: my-cluster
cluster:
...
extensions:
<ul>
<li>name: client.authentication.k8s.io/exec  # reserved extension name for per cluster exec config
extension:
audience: 06e3fbd18de8  # arbitrary config</li>
</ul>
</li>
</ul>
<p>در برخی محیط‌ها، پیکربندی کاربر ممکن است در بسیاری از کلاسترها دقیقاً یکسان باشد
(یعنی همین افزونه‌ی exec را فراخوانی کند)، به‌جز برخی جزئیات که مختص هر کلاستر است،
مانند audience. این فیلد امکان می‌دهد پیکربندی مختص هر کلاستر مستقیماً
همراه با اطلاعات کلاستر مشخص شود. استفاده از این فیلد برای نگهداری داده‌های محرمانه
توصیه نمی‌شود، زیرا یکی از مزایای اصلی افزونه‌های exec این است که نیازی به ذخیره‌ی مستقیم
هیچ اطلاعات محرمانه‌ای در kubeconfig نیست.</p>
</td>
</tr>
</tbody>
</table>

## `ExecCredentialSpec`     {#client-authentication-k8s-io-v1-ExecCredentialSpec}
    

**در این موارد ظاهر می‌شود:**

- [ExecCredential](#client-authentication-k8s-io-v1-ExecCredential)


<p>ExecCredentialSpec شامل اطلاعات مختص درخواست و زمان اجرا است که توسط
انتقال‌دهنده (transport) ارائه می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>cluster</code><br/>
<a href="#client-authentication-k8s-io-v1-Cluster"><code>Cluster</code></a>
</td>
<td>
   <p>Cluster شامل اطلاعاتی است که به یک افزونه exec امکان می‌دهد با
کلاستر کوبرنتیزی که احراز هویت نسبت به آن انجام می‌شود ارتباط برقرار کند. توجه کنید که Cluster تنها
زمانی non-nil است که provideClusterInfo در پیکربندی ارائه‌دهنده‌ی exec برابر true تنظیم شده باشد (یعنی
ExecConfig.ProvideClusterInfo).</p>
</td>
</tr>
<tr><td><code>interactive</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p>Interactive مشخص می‌کند که آیا stdin به این افزونه‌ی exec ارسال شده است یا خیر.</p>
</td>
</tr>
</tbody>
</table>

## `ExecCredentialStatus`     {#client-authentication-k8s-io-v1-ExecCredentialStatus}
    

**در این موارد ظاهر می‌شود:**

- [ExecCredential](#client-authentication-k8s-io-v1-ExecCredential)


<p>ExecCredentialStatus شامل اعتبارنامه‌هایی است که انتقال‌دهنده (transport) باید از آن‌ها استفاده کند.</p>
<p>Token و ClientKeyData فیلدهای حساس هستند. این داده‌ها فقط باید به‌صورت درون‌حافظه‌ای
میان کلاینت و فرایند افزونه‌ی exec منتقل شوند. خود افزونه‌ی exec
نیز دست‌کم باید از طریق مجوزهای فایل محافظت شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>expirationTimestamp</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p>ExpirationTimestamp زمانی را مشخص می‌کند که اعتبارنامه‌های ارائه‌شده منقضی می‌شوند.</p>
</td>
</tr>
<tr><td><code>token</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>Token یک bearer token است که کلاینت برای احراز هویت درخواست‌ها از آن استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>clientCertificateData</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>گواهی‌های TLS کلاینت با کدگذاری PEM (شامل گواهی‌های میانی، در صورت وجود).</p>
</td>
</tr>
<tr><td><code>clientKeyData</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>کلید خصوصی با کدگذاری PEM برای گواهی بالا.</p>
</td>
</tr>
</tbody>
</table>
