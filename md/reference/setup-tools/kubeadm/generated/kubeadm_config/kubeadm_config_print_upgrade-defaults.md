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


پیکربندی پیش‌فرض ارتقا را که می‌توان برای 'kubeadm upgrade' از آن استفاده کرد، چاپ می‌کند.

### خلاصه



این فرمان آبجکت‌هایی مانند پیکربندی پیش‌فرض ارتقا را که 'kubeadm upgrade' از آن استفاده می‌کند، چاپ می‌کند.

توجه کنید که مقادیر حساس، مانند فیلدهای Bootstrap Token، با مقادیر جایگزینی مانند "abcdef.0123456789abcdef" عوض می‌شوند تا اعتبارسنجی با موفقیت انجام شود، اما محاسبهٔ واقعی برای ساخت توکن صورت نگیرد.


```
kubeadm config print upgrade-defaults [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای فرمان upgrade-defaults</p></td>
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
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، می‌توان مجموعه‌ای از مسیرهای استاندارد را برای یافتن فایل kubeconfig موجود جست‌وجو کرد.</p></td>
</tr>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم فایل ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر داده‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
