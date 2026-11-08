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


ایجاد توکن‌های راه‌اندازی (bootstrap token) روی سرور

### خلاصه



این دستور یک توکن راه‌اندازی برای شما ایجاد می‌کند.
می‌توانید کاربردهای این توکن، «مدت اعتبار» (time to live) و در صورت نیاز توضیحی خوانا برای انسان را برای آن مشخص کنید.

مقدار [token] همان توکن واقعی است که باید نوشته شود.
این مقدار باید توکنی تصادفی باشد که به‌صورت امن تولید شده و قالب آن "[a-z0-9]{6}.[a-z0-9]{16}" است.
اگر [token] ارائه نشود، kubeadm به‌جای آن یک توکن تصادفی تولید می‌کند.


```
kubeadm token create [token]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--certificate-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر همراه با '--print-join-command' استفاده شود، فلگ کامل 'kubeadm join' را که برای پیوستن به کلاستر به‌عنوان control plane لازم است چاپ می‌کند. برای ایجاد یک کلید گواهی جدید باید از 'kubeadm init phase upload-certs --upload-certs' استفاده کنید.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--description string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توضیحی خوانا برای انسان دربارهٔ نحوهٔ استفاده از این توکن.</p></td>
</tr>

<tr>
<td colspan="2">--groups strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "system:bootstrappers:kubeadm:default-node-token"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروه‌های اضافی که این توکن هنگام استفاده برای احراز هویت، با عضویت در آن‌ها احراز هویت می‌شود. مقدار باید با الگوی &quot;\Asystem:bootstrappers:[a-z0-9:-]{0,255}[a-z0-9]\z&quot; مطابقت داشته باشد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور create</p></td>
</tr>

<tr>
<td colspan="2">--print-join-command</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>به‌جای چاپ کردن توکن به‌تنهایی، فلگ کامل 'kubeadm join' را که برای پیوستن به کلاستر با استفاده از این توکن لازم است چاپ می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 24h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که پس از آن توکن به‌طور خودکار حذف می‌شود (برای مثال 1s، 2m، 3h). اگر روی '0' تنظیم شود، توکن هرگز منقضی نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--usages strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "signing,authentication"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>روش‌های قابل استفاده از این توکن را مشخص می‌کند. می‌توانید --usages را چند بار به کار ببرید یا فهرستی از گزینه‌ها را که با کاما از هم جدا شده‌اند ارائه کنید. گزینه‌های معتبر: [signing,authentication]</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعیین می‌کند که حالت اجرای آزمایشی (dry-run) فعال باشد یا نه.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، مجموعه‌ای از مکان‌های استاندارد برای یافتن یک فایل kubeconfig موجود جست‌وجو می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--rootfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تنظیم این گزینه، kubeadm با chroot به مسیر ارائه‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
