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


تولید کلیدها و درخواست‌های امضای گواهی

### خلاصه


این دستور برای همهٔ گواهی‌های موردنیاز اجرای control plane، کلید و درخواست امضای گواهی (CSR) تولید می‌کند. همچنین فایل‌های kubeconfig ناقصی می‌سازد که داده‌های کلید خصوصی در فیلد "users &gt; user &gt; client-key-data" آن‌ها قرار دارد و برای هر فایل kubeconfig نیز یک فایل همراه با پسوند ".csr" ایجاد می‌کند.

این دستور برای استفاده در [حالت مرجع صدور گواهی خارجی kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#external-ca-mode) طراحی شده است و CSRهایی تولید می‌کند که می‌توانید آن‌ها را برای امضا به مرجع صدور گواهی خارجی خود ارسال کنید.

پس از امضا، گواهی‌های با کدگذاری PEM را باید با پسوند ".crt" در کنار فایل‌های کلید ذخیره کنید. در مورد فایل‌های kubeconfig، گواهی امضاشده با کدگذاری PEM را باید با base64 کدگذاری کنید و در فیلد "users &gt; user &gt; client-certificate-data" فایل kubeconfig قرار دهید.

```
kubeadm certs generate-csr [flags]
```

### مثال‌ها

```
  # The following command will generate keys and CSRs for all control-plane certificates and kubeconfig files:
  kubeadm certs generate-csr --kubeconfig-dir /tmp/etc-k8s --cert-dir /tmp/etc-k8s/pki
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--cert-dir string</td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور generate-csr</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیری که فایل kubeconfig در آن ذخیره می‌شود.</p></td>
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
