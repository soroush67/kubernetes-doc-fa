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


گواهی‌نامه‌ای را که سرور API برای اتصال به kubelet از آن استفاده می‌کند تولید می‌کند و آن را در فایل‌های apiserver-kubelet-client.crt و apiserver-kubelet-client.key ذخیره می‌کند.

اگر هر دو فایل از قبل وجود داشته باشند، kubeadm از مرحلهٔ تولید صرف‌نظر می‌کند و همان فایل‌های موجود به کار می‌روند.

```
kubeadm init phase certs apiserver-kubelet-client [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--cert-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/pki"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیری که گواهی‌نامه‌ها در آن ذخیره و نگهداری می‌شوند.</p></td>
</tr>

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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای apiserver-kubelet-client</p></td>
</tr>

<tr>
<td colspan="2">--kubernetes-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "stable-1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخهٔ مشخصی از کوبرنتیز را برای control plane انتخاب می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم فایل ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر تعیین‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
