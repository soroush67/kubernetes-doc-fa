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


تنظیمات kubelet را می‌نویسد و kubelet را راه‌اندازی یا بازراه‌اندازی می‌کند

### خلاصه


این دستور فایلی حاوی KubeletConfiguration و یک فایل محیطی حاوی تنظیمات kubelet مختص نود را می‌نویسد و سپس kubelet را راه‌اندازی یا بازراه‌اندازی می‌کند.

```
kubeadm init phase kubelet-start [flags]
```

### مثال‌ها

```
  # Writes a dynamic environment file with kubelet flags from a InitConfiguration file.
  kubeadm init phase kubelet-start --config config.yaml
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکت CRI برای اتصال. اگر این مقدار خالی باشد، kubeadm تلاش می‌کند آن را به‌طور خودکار تشخیص دهد؛ فقط زمانی از این گزینه استفاده کنید که بیش از یک CRI نصب کرده باشید یا سوکت CRI شما غیراستاندارد باشد.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kubelet-start</p></td>
</tr>

<tr>
<td colspan="2">--image-repository string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "registry.k8s.io"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رجیستری کانتینری را انتخاب می‌کند که ایمیج‌های control plane از آن دریافت می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--node-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام نود را مشخص می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--patches string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری‌ای که فایل‌هایی با نام &quot;target[suffix][+patchtype].extension&quot; در آن قرار دارند؛ برای مثال &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از &quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;، &quot;corednsdeployment&quot; یا &quot;kubeproxydaemonset&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد و این مقادیر با قالب‌های patch پشتیبانی‌شده در kubectl مطابقت دارند. مقدار پیش‌فرض &quot;patchtype&quot; برابر با &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد. بخش &quot;suffix&quot; رشته‌ای اختیاری است که با آن می‌توان بر اساس ترتیب الفبایی-عددی تعیین کرد کدام patchها زودتر اعمال شوند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل‌سیستم ریشهٔ «واقعی» میزبان. با تعیین این گزینه، kubeadm با chroot به مسیر مشخص‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
