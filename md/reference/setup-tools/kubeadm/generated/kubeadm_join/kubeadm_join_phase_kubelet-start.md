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


تنظیمات و گواهی‌های kubelet را می‌نویسد و kubelet را راه‌اندازی یا بازراه‌اندازی می‌کند

### خلاصه


فایلی حاوی KubeletConfiguration و یک فایل محیطی حاوی تنظیمات kubelet مختص نود را می‌نویسد و سپس kubelet را راه‌اندازی یا بازراه‌اندازی می‌کند.

```
kubeadm join phase kubelet-start [api-server-endpoint] [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--cri-socket string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکت CRI برای اتصال. اگر این مقدار خالی باشد، kubeadm تلاش می‌کند آن را به‌طور خودکار تشخیص دهد. فقط در صورتی از این گزینه استفاده کنید که بیش از یک CRI نصب کرده باشید یا سوکت CRI شما غیراستاندارد باشد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، اجازه می‌دهد نود بدون تثبیت هش از طریق --discovery-token-ca-cert-hash به کلاستر بپیوندد.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهد شد در خروجی نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kubelet-start</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری حاوی فایل‌هایی با نام &quot;target[suffix][+patchtype].extension&quot;؛ برای مثال، &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از &quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;، &quot;corednsdeployment&quot; یا &quot;kubeproxydaemonset&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد که با قالب‌های وصله (patch) پشتیبانی‌شده در kubectl مطابقت دارند. مقدار پیش‌فرض &quot;patchtype&quot; برابر با &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد. بخش &quot;suffix&quot; رشته‌ای اختیاری است که با آن می‌توان بر اساس ترتیب الفبایی-عددی تعیین کرد کدام وصله‌ها زودتر اعمال شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم‌فایل ریشه «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر ارائه‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
