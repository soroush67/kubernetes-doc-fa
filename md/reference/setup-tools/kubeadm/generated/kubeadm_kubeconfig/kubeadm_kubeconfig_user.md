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


این دستور یک فایل kubeconfig برای یک کاربر اضافی تولید می‌کند.

```
kubeadm kubeconfig user [flags]
```

### نمونه‌ها

```
  # Output a kubeconfig file for an additional user named foo
  kubeadm kubeconfig user --client-name=foo
  
  # Output a kubeconfig file for an additional user named foo using a kubeadm config file bar
  kubeadm kubeconfig user --client-name=foo --config=bar
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--client-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام کاربر. اگر گواهی‌های کلاینت ایجاد شوند، از این نام به‌عنوان CN استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر یک فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور user</p></td>
</tr>

<tr>
<td colspan="2">--org strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>سازمان‌های گواهی کلاینت. اگر گواهی‌های کلاینت ایجاد شوند، از این مقدار به‌عنوان O استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکنی که باید به‌جای گواهی‌های کلاینت، به‌عنوان سازوکار احراز هویت این kubeconfig به کار رود.</p></td>
</tr>

<tr>
<td colspan="2">--validity-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 8760h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت اعتبار گواهی کلاینت. این مقدار فاصله‌ای زمانی نسبت به زمان کنونی است.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم فایل ریشه «واقعی» میزبان. با تعیین این گزینه، kubeadm با chroot به مسیر مشخص‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
