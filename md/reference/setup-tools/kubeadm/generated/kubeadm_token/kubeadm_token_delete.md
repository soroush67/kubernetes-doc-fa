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


حذف توکن‌های راه‌اندازی (bootstrap token) روی سرور

### خلاصه



این دستور فهرستی از توکن‌های راه‌اندازی را برای شما حذف می‌کند.

مقدار [token-value] توکن کاملی به شکل "[a-z0-9]{6}.[a-z0-9]{16}" یا شناسهٔ توکنی به شکل "[a-z0-9]{6}" است که باید حذف شود.


```
kubeadm token delete [token-value] ...
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور delete</p></td>
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
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعیین می‌کند که حالت dry-run فعال باشد یا نه.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، مجموعه‌ای از مسیرهای استاندارد برای یافتن یک فایل kubeconfig موجود جست‌وجو می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم فایل ریشهٔ «واقعی» میزبان. با تنظیم این فلگ، kubeadm با chroot به مسیر داده‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
