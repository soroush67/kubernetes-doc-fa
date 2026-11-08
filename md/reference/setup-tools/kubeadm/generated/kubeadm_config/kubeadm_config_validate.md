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


فایلی را که شامل API پیکربندی kubeadm است می‌خواند و هرگونه مشکل اعتبارسنجی را گزارش می‌کند

### خلاصه



با این دستور می‌توانید فایل API پیکربندی kubeadm را اعتبارسنجی کنید و هشدارها و خطاهای آن را گزارش بگیرید.
اگر خطایی وجود نداشته باشد، وضعیت خروج صفر و در غیر این صورت غیرصفر خواهد بود.
هر مشکلی در بازخوانی ساختار داده (unmarshaling)، مانند فیلدهای ناشناخته API، خطا ایجاد می‌کند. نسخه‌های ناشناخته API و
فیلدهایی با مقادیر نامعتبر نیز خطا ایجاد می‌کنند. بسته به محتوای فایل ورودی، ممکن است خطاها یا هشدارهای دیگری نیز گزارش شوند.

در این نسخه از kubeadm، نسخه‌های زیر از API پشتیبانی می‌شوند:
- kubeadm.k8s.io/v1beta4


```
kubeadm config validate [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--allow-deprecated-api</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اعتبارسنجی APIهای منسوخ‌شده را مجاز می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--allow-experimental-api</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اعتبارسنجی APIهای آزمایشی و منتشرنشده را مجاز می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای validate</p></td>
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
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، مجموعه‌ای از مکان‌های استاندارد برای یافتن فایل kubeconfig موجود جست‌وجو می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم فایل ریشه «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر مشخص‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
