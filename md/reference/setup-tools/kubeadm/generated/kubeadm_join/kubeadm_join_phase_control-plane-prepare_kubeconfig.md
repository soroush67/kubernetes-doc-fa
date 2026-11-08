<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->


### خلاصه


فایل kubeconfig را برای مؤلفه‌های control plane جدید تولید می‌کند.

```
kubeadm join phase control-plane-prepare kubeconfig [api-server-endpoint] [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--certificate-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از این کلید برای رمزگشایی Secretهای گواهی‌نامه‌ای که init بارگذاری کرده است استفاده می‌شود. کلید گواهی‌نامه رشته‌ای با کدگذاری هگزادسیمال است که یک کلید AES با اندازهٔ ۳۲ بایت را نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--control-plane</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک نمونهٔ جدید از control plane را روی این نود ایجاد می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر فایل، فایل یا نشانی URL که اطلاعات کلاستر از آن بارگذاری می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، توکنی که برای اعتبارسنجی اطلاعات کلاستر دریافت‌شده از سرور API به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token-ca-cert-hash strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، بررسی می‌کند که کلید عمومی CA ریشه با این هش مطابقت داشته باشد (قالب: &quot;&lt;type&gt;:&lt;value&gt;&quot;).</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token-unsafe-skip-ca-verification</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، پیوستن به کلاستر را بدون سنجاق‌کردن هش با --discovery-token-ca-cert-hash مجاز می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kubeconfig</p></td>
</tr>

<tr>
<td colspan="2">--tls-bootstrap-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکنی را مشخص می‌کند که هنگام پیوستن نود، برای احراز هویت موقت با control plane کوبرنتیز به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقادیر discovery-token و tls-bootstrap-token ارائه نشده باشند، از این توکن برای هر دوی آن‌ها استفاده می‌شود.</p></td>
</tr>

</tbody>
</table>



### گزینه‌های به‌ارث‌رسیده از دستورهای والد

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر ارائه‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
