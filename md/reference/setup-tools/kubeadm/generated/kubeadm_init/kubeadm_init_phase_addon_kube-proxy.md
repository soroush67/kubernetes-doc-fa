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


افزونهٔ kube-proxy را روی یک کلاستر کوبرنتیز نصب می‌کند.

### خلاصه


اجزای افزونهٔ kube-proxy را از طریق سرور API نصب می‌کند.

```
kubeadm init phase addon kube-proxy [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی IP که سرور API اعلام می‌کند روی آن در حال گوش دادن است. اگر این مقدار تنظیم نشود، از رابط شبکهٔ پیش‌فرض استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--apiserver-bind-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 6443</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورتی که سرور API به آن متصل می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--control-plane-endpoint string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک نشانی IP یا نام DNS پایدار برای control plane مشخص می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kube-proxy</p></td>
</tr>

<tr>
<td colspan="2">--image-repository string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "registry.k8s.io"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رجیستری کانتینری را که ایمیج‌های control plane از آن دریافت می‌شوند انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشود، می‌توان مجموعه‌ای از مکان‌های استاندارد را برای یافتن یک فایل kubeconfig موجود جست‌وجو کرد.</p></td>
</tr>

<tr>
<td colspan="2">--kubernetes-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "stable-1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخهٔ مشخصی از کوبرنتیز را برای control plane انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--pod-network-cidr string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدودهٔ نشانی‌های IP شبکهٔ Pod را مشخص می‌کند. اگر این مقدار تنظیم شود، control plane به‌طور خودکار برای هر نود CIDR تخصیص می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--print-manifest</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مانیفست‌های افزونه را به‌جای نصب، در STDOUT چاپ می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم‌فایل ریشهٔ «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر تعیین‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
