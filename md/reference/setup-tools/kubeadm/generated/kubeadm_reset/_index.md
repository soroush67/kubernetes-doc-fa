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


این فرمان تغییراتی را که `kubeadm init` یا `kubeadm join` روی این میزبان اعمال کرده‌اند، تا حد امکان بازمی‌گرداند.

فرمان `reset` فازهای زیر را اجرا می‌کند:
```
preflight           Run reset pre-flight checks
remove-etcd-member  Remove a local etcd member.
cleanup-node        Run cleanup node.
```


```
kubeadm reset [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری محل ذخیرهٔ گواهی‌ها. اگر این گزینه مشخص شود، محتوای این دایرکتوری پاک‌سازی می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cleanup-tmp-dir</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری &quot;/etc/kubernetes/tmp&quot; را پاک‌سازی می‌کند.</p></td>
</tr>

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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکت CRI برای اتصال. اگر این مقدار خالی باشد، kubeadm تلاش می‌کند آن را به‌طور خودکار تشخیص دهد. فقط زمانی از این گزینه استفاده کنید که بیش از یک CRI نصب کرده باشید یا سوکت CRI شما غیراستاندارد باشد.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری را اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد، در خروجی نشان می‌دهد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای فرمان reset</p></td>
</tr>

<tr>
<td colspan="2">--ignore-preflight-errors strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از بررسی‌هایی که خطاهایشان به‌صورت هشدار نمایش داده می‌شود؛ برای نمونه: 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همهٔ بررسی‌ها را نادیده می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، می‌توان مجموعه‌ای از مکان‌های استاندارد را برای یافتن فایل kubeconfig موجود جست‌وجو کرد.</p></td>
</tr>

<tr>
<td colspan="2">--skip-phases strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست فازهایی که باید از اجرای آن‌ها صرف‌نظر شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر تعیین‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
