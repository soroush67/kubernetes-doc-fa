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


افزونهٔ CoreDNS را روی یک کلاستر کوبرنتیز نصب می‌کند

### خلاصه


این دستور اجزای افزونهٔ CoreDNS را از طریق API server نصب می‌کند. توجه کنید که با وجود استقرار سرور DNS، تا زمانی که CNI نصب نشود، این سرور زمان‌بندی نخواهد شد.

```
kubeadm init phase addon coredns [flags]
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
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد، در خروجی نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از زوج‌های key=value که feature gateهای قابلیت‌های مختلف را توصیف می‌کنند. گزینه‌ها عبارت‌اند از:<br/>RootlessControlPlane=true|false (آلفا - مقدار پیش‌فرض: false)</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور coredns</p></td>
</tr>

<tr>
<td colspan="2">--image-repository string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "registry.k8s.io"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رجیستری کانتینری را که ایمیج‌های control plane از آن دریافت می‌شوند، انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig مورد نیاز برای ارتباط با کلاستر را مشخص می‌کند. اگر این فلگ تنظیم نشده باشد، مجموعه‌ای از مکان‌های استاندارد را می‌توان برای یافتن یک فایل kubeconfig موجود جست‌وجو کرد.</p></td>
</tr>

<tr>
<td colspan="2">--kubernetes-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "stable-1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخهٔ مشخصی از کوبرنتیز را برای control plane انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--print-manifest</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مانیفست‌های افزونه را به‌جای نصب، در STDOUT چاپ می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--service-cidr string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "10.96.0.0/12"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدودهٔ دیگری از نشانی‌های IP را برای VIPهای Service به کار می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--service-dns-domain string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "cluster.local"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دامنهٔ دیگری را برای Serviceها به کار می‌گیرد؛ برای مثال &quot;myorg.internal&quot;.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تعیین این گزینه، kubeadm با chroot به مسیر مشخص‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
