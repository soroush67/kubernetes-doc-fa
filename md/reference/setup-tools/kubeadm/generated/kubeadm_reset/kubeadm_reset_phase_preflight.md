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


بررسی‌های پیش از اجرای بازنشانی را اجرا می‌کند

### خلاصه


بررسی‌های پیش از اجرا (pre-flight) را برای دستور `kubeadm reset` اجرا می‌کند.

```
kubeadm reset phase preflight [flags]
```

### گزینه‌ها

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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-f, --force</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نود را بدون درخواست تأیید بازنشانی می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از بررسی‌ها که خطاهای آن‌ها به‌صورت هشدار نمایش داده می‌شوند. برای نمونه: 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همه بررسی‌ها را نادیده می‌گیرد.</p></td>
</tr>

</tbody>
</table>



### گزینه‌های به ارث رسیده از دستورهای والد

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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشه «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر مشخص‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
