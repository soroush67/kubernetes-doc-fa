---
title: پیکربندی WebhookAdmission (v1)
content_type: tool-reference
package: apiserver.config.k8s.io/v1
auto_generated: true
---
<p>پکیج v1 نسخهٔ v1 از API است.</p>


## انواع منابع 


- [WebhookAdmission](#apiserver-config-k8s-io-v1-WebhookAdmission)
  

## `WebhookAdmission`     {#apiserver-config-k8s-io-v1-WebhookAdmission}
    


<p>WebhookAdmission پیکربندی مربوط به کنترل‌کنندهٔ پذیرش webhook را فراهم می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>apiserver.config.k8s.io/v1</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>WebhookAdmission</code></td></tr>
    
  
<tr><td><code>kubeConfigFile</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p>KubeConfigFile مسیر فایل kubeconfig است.</p>
</td>
</tr>
<tr><td><code>staticManifestsDir</code><br/>
<code>string</code>
</td>
<td>
   <p>StaticManifestsDir مسیر دایرکتوری‌ای است که شامل پیکربندی‌های ایستای webhook است و این پیکربندی‌ها هنگام راه‌اندازی بارگذاری می‌شوند. فایل‌هایی با پسوندهای .yaml،
.yml و .json خوانده می‌شوند. تنها منابع
ValidatingWebhookConfiguration و MutatingWebhookConfiguration از نوع admissionregistration.k8s.io/v1
پشتیبانی می‌شوند.
استفاده از این فیلد مستلزم فعال بودن feature gate با نام ManifestBasedAdmissionControlConfig
است.</p>
</td>
</tr>
</tbody>
</table>
