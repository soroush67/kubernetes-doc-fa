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


مدیریت توکن‌های راه‌اندازی (bootstrap token)

### خلاصه



این دستور توکن‌های راه‌اندازی را مدیریت می‌کند. استفاده از آن اختیاری است و فقط در موارد کاربرد پیشرفته به آن نیاز پیدا می‌کنید.

به طور خلاصه، توکن‌های راه‌اندازی برای برقراری اعتماد دوطرفه میان یک کلاینت و یک سرور به کار می‌روند.
هنگامی که یک کلاینت (برای مثال نودی که در آستانهٔ پیوستن به کلاستر است) باید به سروری که با آن ارتباط برقرار می‌کند اعتماد کند، می‌توان از توکن راه‌اندازی استفاده کرد. در این حالت، توکنی با کاربرد "signing" به کار می‌رود.
توکن‌های راه‌اندازی همچنین می‌توانند امکان احراز هویت کوتاه‌مدت در API Server را فراهم کنند (در این حالت، توکن وسیله‌ای است که API Server با آن به کلاینت اعتماد می‌کند)؛ برای نمونه، هنگام انجام TLS Bootstrap.

توکن راه‌اندازی دقیقاً چیست؟
 - هر توکن راه‌اندازی یک Secret از نوع "bootstrap.kubernetes.io/token" در فضای نام (namespace) `kube-system` است.
 - قالب توکن راه‌اندازی باید به صورت "[a-z0-9]{6}.[a-z0-9]{16}" باشد. بخش نخست، شناسهٔ عمومی توکن و بخش دوم، Token Secret است که باید در هر شرایطی محرمانه بماند.
 - نام این Secret باید به صورت "bootstrap-token-(token-id)" باشد.

برای اطلاعات بیشتر دربارهٔ توکن‌های راه‌اندازی، به این نشانی مراجعه کنید:
  https://kubernetes.io/docs/admin/bootstrap-tokens/


```
kubeadm token [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که حالت dry-run فعال باشد یا نه.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور token</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، می‌توان مجموعه‌ای از مکان‌های استاندارد را برای یافتن یک فایل kubeconfig موجود جست‌وجو کرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر تعیین‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
