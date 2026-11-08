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


گواهی کلاینت front proxy را تمدید می‌کند.

تمدید بدون هیچ شرطی و فارغ از تاریخ انقضای گواهی انجام می‌شود. ویژگی‌های اضافی مانند SANها از فایل‌ها و گواهی‌های موجود برداشته می‌شوند و نیازی به ارائهٔ دوبارهٔ آن‌ها نیست.

فرایند تمدید به‌طور پیش‌فرض می‌کوشد از مرجع صدور گواهی موجود در PKI محلیِ تحت مدیریت kubeadm استفاده کند. به‌عنوان جایگزین می‌توان از API گواهی کوبرنتیز برای تمدید گواهی استفاده کرد یا در آخرین گزینه، یک درخواست CSR تولید کرد.

پس از تمدید، برای اعمال تغییرات باید مؤلفه‌های control plane را دوباره راه‌اندازی کنید و اگر از این فایل در جای دیگری نیز استفاده می‌شود، گواهی تمدیدشده را دوباره در آنجا توزیع کنید.

```
kubeadm certs renew front-proxy-client [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیری که گواهی‌ها در آن ذخیره می‌شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای front-proxy-client</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، مجموعه‌ای از مکان‌های استاندارد برای یافتن یک فایل kubeconfig موجود جست‌وجو می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر ارائه‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
