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


کلاستر کوبرنتیز خود را به نسخهٔ مشخص‌شده ارتقا دهید.

دستور "apply [version]" مرحله‌های زیر را اجرا می‌کند:
```
preflight        Run preflight checks before upgrade
control-plane    Upgrade the control plane
upload-config    Upload the kubeadm and kubelet configurations to ConfigMaps
  /kubeadm         Upload the kubeadm ClusterConfiguration to a ConfigMap
  /kubelet         Upload the kubelet configuration to a ConfigMap
kubelet-config   Upgrade the kubelet configuration for this node
bootstrap-token  Configures bootstrap token and cluster-info RBAC rules
addon            Upgrade the default kubeadm addons
  /coredns         Upgrade the CoreDNS addon
  /kube-proxy      Upgrade the kube-proxy addon
post-upgrade     Run post upgrade tasks
```


```
kubeadm upgrade apply [version]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--allow-experimental-upgrades</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه‌های ناپایدار کوبرنتیز را به‌عنوان گزینهٔ ارتقا نمایش می‌دهد و امکان ارتقا به نسخه‌های آلفا، بتا یا نامزد انتشار کوبرنتیز را فراهم می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--allow-release-candidate-upgrades</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه‌های نامزد انتشار کوبرنتیز را به‌عنوان گزینهٔ ارتقا نمایش می‌دهد و امکان ارتقا به این نسخه‌ها را فراهم می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--certificate-renewal&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گواهی‌های مؤلفه‌هایی را که هنگام ارتقا تغییر می‌کنند، تمدید می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ وضعیتی را تغییر نمی‌دهد و فقط عملیاتی را که انجام خواهند شد در خروجی نمایش می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-upgrade&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ارتقای etcd را انجام می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-f, --force</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ارتقا را حتی در صورت برآورده‌نشدن برخی پیش‌نیازها به‌اجبار انجام می‌دهد. استفاده از این گزینه به معنای فعال‌شدن حالت غیرتعاملی نیز هست.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور apply</p></td>
</tr>

<tr>
<td colspan="2">--ignore-preflight-errors strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از بررسی‌هایی که خطاهای آن‌ها به‌صورت هشدار نمایش داده می‌شوند؛ برای نمونه: 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همهٔ بررسی‌ها را نادیده می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/admin.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که برای ارتباط با کلاستر استفاده می‌شود. اگر این فلگ تنظیم نشده باشد، می‌توان مجموعه‌ای از مکان‌های استاندارد را برای یافتن یک فایل kubeconfig موجود جست‌وجو کرد.</p></td>
</tr>

<tr>
<td colspan="2">--patches string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری‌ای که فایل‌هایی با نام &quot;target[suffix][+patchtype].extension&quot; در آن قرار دارند؛ برای نمونه، &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از &quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;، &quot;corednsdeployment&quot; یا &quot;kubeproxydaemonset&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد و این مقادیر با قالب‌های وصله‌ای که kubectl پشتیبانی می‌کند مطابقت دارند. مقدار پیش‌فرض &quot;patchtype&quot; برابر با &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد. بخش &quot;suffix&quot; رشته‌ای اختیاری است و با آن می‌توان بر پایهٔ ترتیب الفبایی‑عددی تعیین کرد که کدام وصله‌ها زودتر اعمال شوند.</p></td>
</tr>

<tr>
<td colspan="2">--print-config</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که فایل پیکربندی مورد استفاده در ارتقا چاپ شود یا نه.</p></td>
</tr>

<tr>
<td colspan="2">--skip-phases strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مرحله‌هایی که باید از اجرای آن‌ها صرف‌نظر شود.</p></td>
</tr>

<tr>
<td colspan="2">-y, --yes</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ارتقا را بدون درخواست تأیید انجام می‌دهد (حالت غیرتعاملی).</p></td>
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
