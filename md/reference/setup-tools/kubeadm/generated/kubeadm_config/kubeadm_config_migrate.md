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


نسخهٔ قدیمی‌تر انواع API پیکربندی kubeadm را از یک فایل می‌خواند و آبجکت پیکربندی مشابه را برای نسخهٔ جدیدتر در خروجی می‌نویسد.

### خلاصه



با این دستور می‌توانید آبجکت‌های پیکربندی نسخه‌های قدیمی‌تر را به آخرین نسخهٔ پشتیبانی‌شده تبدیل کنید. این تبدیل به‌صورت محلی در ابزار خط فرمان انجام می‌شود و هیچ تغییری در کلاستر ایجاد نمی‌کند.
این نسخه از kubeadm از نسخه‌های API زیر پشتیبانی می‌کند:
- kubeadm.k8s.io/v1beta4

افزون بر این، ابزار kubeadm فقط می‌تواند پیکربندی را با نسخهٔ "kubeadm.k8s.io/v1beta4" بنویسد، اما هر دو نوع را می‌خواند.
بنابراین، صرف‌نظر از نسخه‌ای که در اینجا به پارامتر --old-config می‌دهید، آبجکت API خوانده می‌شود، از حالت سریالی خارج می‌شود، مقادیر پیش‌فرض را می‌گیرد، تبدیل و اعتبارسنجی می‌شود و سپس هنگام نوشتن در stdout یا در مسیر --new-config (در صورت تعیین) دوباره سریالی می‌شود.

به بیان دیگر، خروجی این دستور همان چیزی است که اگر این فایل را به "kubeadm init" بدهید، kubeadm در عمل به‌صورت داخلی می‌خواند.


```
kubeadm config migrate [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--allow-experimental-api</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهاجرت به APIهای آزمایشی و منتشرنشده را مجاز می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور migrate</p></td>
</tr>

<tr>
<td colspan="2">--new-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی معادل kubeadm که با نسخهٔ جدید API تولید می‌شود. این فلگ اختیاری است و اگر تعیین نشود، خروجی به STDOUT فرستاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--old-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm که از نسخهٔ قدیمی API استفاده می‌کند و باید تبدیل شود. تعیین این فلگ الزامی است.</p></td>
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
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشود، مجموعه‌ای از مکان‌های استاندارد برای یافتن یک فایل kubeconfig موجود جست‌وجو می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تعیین این فلگ، kubeadm با chroot به مسیر داده‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
