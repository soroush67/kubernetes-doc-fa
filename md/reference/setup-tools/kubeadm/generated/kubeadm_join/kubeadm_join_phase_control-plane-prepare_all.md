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


ماشین را برای میزبانی control plane آماده می‌کند.

```
kubeadm join phase control-plane-prepare all [api-server-endpoint] [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--apiserver-advertise-address string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر قرار باشد نود میزبان یک نمونهٔ جدید از control plane باشد، این گزینه نشانی IP‌ای را مشخص می‌کند که API Server اعلام می‌کند روی آن گوش می‌دهد. اگر این گزینه تنظیم نشود، از رابط شبکهٔ پیش‌فرض استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--apiserver-bind-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;مقدار پیش‌فرض: 6443</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر قرار باشد نود میزبان یک نمونهٔ جدید از control plane باشد، این گزینه پورتی را مشخص می‌کند که API Server به آن متصل می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--certificate-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از این کلید برای رمزگشایی Secretهای گواهی‌نامه که init بارگذاری کرده است استفاده می‌شود. کلید گواهی‌نامه رشته‌ای با کدگذاری هگزادسیمال است که یک کلید AES با اندازهٔ ۳۲ بایت را در خود دارد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک نمونهٔ جدید از control plane روی این نود ایجاد می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر فایل، فایل یا URLای را مشخص می‌کند که اطلاعات کلاستر از آن بارگذاری می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، توکنی را مشخص می‌کند که برای اعتبارسنجی اطلاعات کلاسترِ دریافت‌شده از API server به کار می‌رود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، اجازه می‌دهد نود بدون پین‌کردن با --discovery-token-ca-cert-hash به کلاستر بپیوندد.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای all</p></td>
</tr>

<tr>
<td colspan="2">--node-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام نود را مشخص می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--patches string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری‌ای که فایل‌هایی با نام &quot;target[suffix][+patchtype].extension&quot; در آن قرار دارند؛ برای مثال &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از &quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;، &quot;corednsdeployment&quot; یا &quot;kubeproxydaemonset&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد و این مقادیر با قالب‌های وصله‌ای که kubectl پشتیبانی می‌کند مطابقت دارند. مقدار پیش‌فرض &quot;patchtype&quot; برابر با &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد. بخش &quot;suffix&quot; رشته‌ای اختیاری است که با آن می‌توان بر اساس ترتیب الفبایی-عددی تعیین کرد کدام وصله‌ها زودتر اعمال شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقادیر discovery-token و tls-bootstrap-token ارائه نشده باشند، از این توکن برای هر دو استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر مشخص‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
