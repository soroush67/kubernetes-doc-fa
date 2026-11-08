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


مدیریت پیکربندی کلاستر kubeadm که در یک ConfigMap درون کلاستر ذخیره شده است

### خلاصه



در فضای نام (namespace) ‏kube-system یک ConfigMap به نام "kubeadm-config" وجود دارد که kubeadm پیکربندی داخلی کلاستر را در آن ذخیره می‌کند. رابط خط فرمان kubeadm از نسخهٔ v1.8.0 به بعد، این ConfigMap را به‌طور خودکار با پیکربندی به‌کاررفته در 'kubeadm init' ایجاد می‌کند؛ اما اگر کلاستر خود را با kubeadm نسخهٔ v1.7.x یا پایین‌تر راه‌اندازی کرده‌اید، باید این ConfigMap را با دستور 'kubeadm init phase upload-config' ایجاد کنید. این کار ضروری است تا 'kubeadm upgrade' بتواند کلاستر ارتقایافتهٔ شما را به‌درستی پیکربندی کند.


```
kubeadm config [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور config</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشود، می‌توان مجموعه‌ای از مسیرهای استاندارد را برای یافتن یک فایل kubeconfig موجود جست‌وجو کرد.</p></td>
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
