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


بررسی‌های پیش‌نیاز (pre-flight) مربوط به join را اجرا می‌کند

### خلاصه


بررسی‌های پیش‌نیاز را برای `kubeadm join` اجرا می‌کند.

```
kubeadm join phase preflight [api-server-endpoint] [flags]
```

### مثال‌ها

```
  # Run join pre-flight checks using a config file.
  kubeadm join phase preflight --config kubeadm-config.yaml
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر قرار باشد این نود میزبان یک نمونهٔ جدید از control plane باشد، این گزینه نشانی IP‌ای را تعیین می‌کند که API Server اعلام می‌کند روی آن در حال گوش‌دادن است. اگر این مقدار تنظیم نشود، از رابط شبکهٔ پیش‌فرض استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--apiserver-bind-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 6443</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر قرار باشد این نود میزبان یک نمونهٔ جدید از control plane باشد، این گزینه پورتی را تعیین می‌کند که API Server به آن متصل می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--certificate-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از این کلید برای رمزگشایی Secretهای گواهی‌نامه که init بارگذاری کرده است استفاده کنید. کلید گواهی‌نامه رشته‌ای با کدگذاری هگزادسیمال است که یک کلید AES با اندازهٔ ۳۲ بایت را نشان می‌دهد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک نمونهٔ جدید از control plane را روی این نود ایجاد می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--cri-socket string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکت CRI برای اتصال. اگر این مقدار خالی باشد، kubeadm تلاش می‌کند آن را به‌طور خودکار تشخیص دهد. فقط زمانی از این گزینه استفاده کنید که بیش از یک CRI نصب کرده باشید یا سوکت CRI شما غیراستاندارد باشد.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر فایل، فایل یا URL‌ای است که اطلاعات کلاستر از آن بارگذاری می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، توکنی است که برای اعتبارسنجی اطلاعات کلاستر دریافت‌شده از API server به کار می‌رود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، اجازه می‌دهد نود بدون تثبیت هش از طریق <code>--discovery-token-ca-cert-hash</code> به کلاستر بپیوندد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای preflight</p></td>
</tr>

<tr>
<td colspan="2">--ignore-preflight-errors strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از بررسی‌هایی که خطاهای آن‌ها به‌صورت هشدار نمایش داده می‌شود. مثال: 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همهٔ بررسی‌ها را نادیده می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--node-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام نود را مشخص می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--tls-bootstrap-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکنی را مشخص می‌کند که هنگام پیوستن نود، برای احراز هویت موقت در control plane کوبرنتیز به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقادیر discovery-token و tls-bootstrap-token ارائه نشده باشند، از این توکن برای هر دوی آن‌ها استفاده می‌شود.</p></td>
</tr>

</tbody>
</table>



### گزینه‌های به‌ارث‌رسیده از فرمان‌های والد

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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تعیین این گزینه، kubeadm با chroot به مسیر ارائه‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
