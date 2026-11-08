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


این فرمان را روی هر ماشینی اجرا کنید که می‌خواهید به یک کلاستر موجود بپیوندد.

### خلاصه



هنگام پیوستن به کلاستری که با kubeadm راه‌اندازی شده است، باید اعتماد دوطرفه برقرار شود. این کار به دو بخش تقسیم می‌شود: کشف (discovery) که در آن نود به control plane کوبرنتیز اعتماد می‌کند، و راه‌اندازی اولیه TLS (TLS bootstrap) که در آن control plane کوبرنتیز به نود اعتماد می‌کند.

برای کشف، دو روش اصلی وجود دارد. روش نخست، استفاده از یک توکن مشترک همراه با نشانی IP سرور API است. روش دوم، ارائه فایلی است که زیرمجموعه‌ای از فایل استاندارد kubeconfig به شمار می‌رود. فایل discovery/kubeconfig از token، افزونه‌های احراز هویت client-go ("exec")، "tokenFile" و "authProvider" پشتیبانی می‌کند. این فایل می‌تواند محلی باشد یا از یک نشانی HTTPS بارگیری شود. شکل‌های این فرمان عبارت‌اند از kubeadm join --discovery-token abcdef.1234567890abcdef 1.2.3.4:6443، kubeadm join --discovery-file path/to/file.conf یا kubeadm join --discovery-file https://url/file.conf. فقط از یکی از این شکل‌ها می‌توان استفاده کرد. اگر اطلاعات کشف از یک URL بارگیری شود، استفاده از HTTPS الزامی است. در این حالت، بسته گواهی‌های CA نصب‌شده روی میزبان برای تأیید اتصال به کار می‌رود.

اگر برای کشف از توکن مشترک استفاده می‌کنید، باید فلگ --discovery-token-ca-cert-hash را نیز ارسال کنید تا کلید عمومی مرجع صدور گواهی (CA) ریشه‌ای که control plane کوبرنتیز ارائه می‌دهد اعتبارسنجی شود. مقدار این فلگ به شکل "&lt;hash-type&gt;:&lt;hex-encoded-value&gt;" مشخص می‌شود و نوع هش پشتیبانی‌شده "sha256" است. این هش بر روی بایت‌های آبجکت Subject Public Key Info (SPKI) محاسبه می‌شود (مطابق RFC7469). این مقدار در خروجی "kubeadm init" موجود است و با ابزارهای استاندارد نیز می‌توان آن را محاسبه کرد. برای مجاز کردن بیش از یک کلید عمومی، می‌توانید فلگ --discovery-token-ca-cert-hash را چند بار تکرار کنید.

اگر نمی‌توانید هش کلید عمومی CA را از پیش بدانید، می‌توانید با ارسال فلگ --discovery-token-unsafe-skip-ca-verification این اعتبارسنجی را غیرفعال کنید. این کار مدل امنیتی kubeadm را تضعیف می‌کند، زیرا نودهای دیگر ممکن است خود را به جای control plane کوبرنتیز جا بزنند.

سازوکار راه‌اندازی اولیه TLS نیز بر پایه یک توکن مشترک کار می‌کند. از این توکن برای احراز هویت موقت در control plane کوبرنتیز و ارسال درخواست امضای گواهی (CSR) برای یک جفت‌کلید ساخته‌شده به‌صورت محلی استفاده می‌شود. kubeadm به‌طور پیش‌فرض control plane کوبرنتیز را طوری تنظیم می‌کند که این درخواست‌های امضا را خودکار تأیید کند. این توکن با فلگ --tls-bootstrap-token abcdef.1234567890abcdef ارسال می‌شود.

اغلب برای هر دو بخش از یک توکن استفاده می‌شود. در این حالت، به جای تعیین جداگانه هر توکن می‌توان از فلگ --token استفاده کرد.


فرمان "join [api-server-endpoint]" مراحل زیر را اجرا می‌کند:
```
preflight               Run join pre-flight checks
control-plane-prepare   Prepare the machine for serving a control plane
  /download-certs         Download certificates shared among control-plane nodes from the kubeadm-certs Secret
  /certs                  Generate the certificates for the new control plane components
  /kubeconfig             Generate the kubeconfig for the new control plane components
  /control-plane          Generate the manifests for the new control plane components
kubelet-start           Write kubelet settings, certificates and (re)start the kubelet
etcd-join               Join etcd for control plane nodes
kubelet-wait-bootstrap  Wait for the kubelet to bootstrap itself
control-plane-join      Join a machine as a control plane instance
  /mark-control-plane     Mark a node as a control-plane
wait-control-plane      Wait for the control plane to start
```


```
kubeadm join [api-server-endpoint] [flags]
```

### گزینه‌ها

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--apiserver-advertise-address string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر قرار باشد این نود میزبان یک نمونه جدید control plane باشد، نشانی IP که API Server اعلام می‌کند روی آن گوش می‌دهد. اگر تنظیم نشود، رابط شبکه پیش‌فرض استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--apiserver-bind-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 6443</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر قرار باشد این نود میزبان یک نمونه جدید control plane باشد، پورتی که API Server به آن متصل می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--certificate-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از این کلید برای رمزگشایی Secretهای گواهی که init بارگذاری کرده است استفاده کنید. کلید گواهی رشته‌ای با کدگذاری هگزادسیمال است که یک کلید AES با اندازه ۳۲ بایت را نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--control-plane</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک نمونه جدید control plane روی این نود ایجاد می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--cri-socket string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکت CRI برای اتصال. اگر خالی باشد، kubeadm تلاش می‌کند این مقدار را خودکار تشخیص دهد. فقط در صورتی از این گزینه استفاده کنید که بیش از یک CRI نصب کرده‌اید یا سوکت CRI غیراستاندارد دارید.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر فایل، فایل یا URL که اطلاعات کلاستر از آن بارگیری می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، توکنی که برای اعتبارسنجی اطلاعات کلاستر دریافت‌شده از سرور API به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token-ca-cert-hash strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، بررسی می‌کند که کلید عمومی CA ریشه با این هش مطابقت داشته باشد (قالب: &quot;&lt;type&gt;:&lt;value&gt;&quot;).</p></td>
</tr>

<tr>
<td colspan="2">--discovery-token-unsafe-skip-ca-verification</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در کشف مبتنی بر توکن، پیوستن بدون تثبیت هش با --discovery-token-ca-cert-hash را مجاز می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای فرمان join</p></td>
</tr>

<tr>
<td colspan="2">--ignore-preflight-errors strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از بررسی‌هایی که خطاهایشان به‌صورت هشدار نمایش داده می‌شود. نمونه: 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همه بررسی‌ها را نادیده می‌گیرد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری حاوی فایل‌هایی با نام &quot;target[suffix][+patchtype].extension&quot;. برای مثال، &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از &quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;، &quot;corednsdeployment&quot; یا &quot;kubeproxydaemonset&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد و این مقادیر با قالب‌های patch پشتیبانی‌شده در kubectl مطابقت دارند. مقدار پیش‌فرض &quot;patchtype&quot; برابر &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد. بخش &quot;suffix&quot; رشته‌ای اختیاری است که با آن می‌توان ترتیب اعمال patchها را بر اساس ترتیب الفبایی-عددی تعیین کرد.</p></td>
</tr>

<tr>
<td colspan="2">--skip-phases strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مراحلی که باید از اجرای آن‌ها صرف‌نظر شود.</p></td>
</tr>

<tr>
<td colspan="2">--tls-bootstrap-token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکنی را مشخص می‌کند که هنگام پیوستن نود، برای احراز هویت موقت در control plane کوبرنتیز به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقادیر discovery-token و tls-bootstrap-token ارائه نشده باشند، از این توکن برای هر دو استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم فایل ریشه «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر ارائه‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
