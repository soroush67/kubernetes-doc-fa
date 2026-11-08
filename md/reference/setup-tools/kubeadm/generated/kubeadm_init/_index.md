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


برای راه‌اندازی control plane کوبرنتیز این دستور را اجرا کنید.

دستور «init» مراحل زیر را اجرا می‌کند:
```
preflight                     Run pre-flight checks
certs                         Certificate generation
  /ca                           Generate the self-signed Kubernetes CA to provision identities for other Kubernetes components
  /apiserver                    Generate the certificate for serving the Kubernetes API
  /apiserver-kubelet-client     Generate the certificate for the API server to connect to kubelet
  /front-proxy-ca               Generate the self-signed CA to provision identities for front proxy
  /front-proxy-client           Generate the certificate for the front proxy client
  /etcd-ca                      Generate the self-signed CA to provision identities for etcd
  /etcd-server                  Generate the certificate for serving etcd
  /etcd-peer                    Generate the certificate for etcd nodes to communicate with each other
  /etcd-healthcheck-client      Generate the certificate for liveness probes to healthcheck etcd
  /apiserver-etcd-client        Generate the certificate the apiserver uses to access etcd
  /sa                           Generate a private key for signing service account tokens along with its public key
kubeconfig                    Generate all kubeconfig files necessary to establish the control plane and the admin kubeconfig file
  /admin                        Generate a kubeconfig file for the admin to use and for kubeadm itself
  /super-admin                  Generate a kubeconfig file for the super-admin
  /kubelet                      Generate a kubeconfig file for the kubelet to use *only* for cluster bootstrapping purposes
  /controller-manager           Generate a kubeconfig file for the controller manager to use
  /scheduler                    Generate a kubeconfig file for the scheduler to use
etcd                          Generate static Pod manifest file for local etcd
  /local                        Generate the static Pod manifest file for a local, single-node local etcd instance
control-plane                 Generate all static Pod manifest files necessary to establish the control plane
  /apiserver                    Generates the kube-apiserver static Pod manifest
  /controller-manager           Generates the kube-controller-manager static Pod manifest
  /scheduler                    Generates the kube-scheduler static Pod manifest
kubelet-start                 Write kubelet settings and (re)start the kubelet
wait-control-plane            Wait for the control plane to start
upload-config                 Upload the kubeadm and kubelet configuration to a ConfigMap
  /kubeadm                      Upload the kubeadm ClusterConfiguration to a ConfigMap
  /kubelet                      Upload the kubelet component config to a ConfigMap
upload-certs                  Upload certificates to kubeadm-certs
mark-control-plane            Mark a node as a control-plane
bootstrap-token               Generates bootstrap tokens used to join a node to a cluster
kubelet-finalize              Updates settings relevant to the kubelet after TLS bootstrap
  /enable-client-cert-rotation  Enable kubelet client certificate rotation
addon                         Install required addons for passing conformance tests
  /coredns                      Install the CoreDNS addon to a Kubernetes cluster
  /kube-proxy                   Install the kube-proxy addon to a Kubernetes cluster
show-join-command             Show the join command for control-plane and worker node
```


```
kubeadm init [flags]
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی IP که سرور API اعلام می‌کند روی آن گوش می‌دهد. اگر این مقدار تنظیم نشود، رابط شبکهٔ پیش‌فرض به کار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--apiserver-bind-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 6443</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>درگاهی که سرور API به آن متصل (bind) می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--apiserver-cert-extra-sans strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام‌های جایگزین موضوع (SAN) اضافی و اختیاری برای گواهی سرویس‌دهی سرور API. این مقادیر می‌توانند هم نشانی IP و هم نام DNS باشند.</p></td>
</tr>

<tr>
<td colspan="2">--cert-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "/etc/kubernetes/pki"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیری که گواهی‌ها در آن ذخیره و نگهداری می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--certificate-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کلیدی که برای رمزگذاری گواهی‌های control plane در Secret با نام kubeadm-certs به کار می‌رود. این کلید رشته‌ای با کدگذاری هگزادسیمال است که یک کلید AES با اندازهٔ ۳۲ بایت را نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی kubeadm.</p></td>
</tr>

<tr>
<td colspan="2">--control-plane-endpoint string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک نشانی IP یا نام DNS پایدار برای control plane تعیین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--cri-socket string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکت CRI برای برقراری اتصال. اگر این مقدار خالی باشد، kubeadm تلاش می‌کند آن را به‌طور خودکار تشخیص دهد. از این گزینه فقط زمانی استفاده کنید که بیش از یک CRI نصب کرده‌اید یا سوکت CRI شما غیراستاندارد است.</p></td>
</tr>

<tr>
<td colspan="2">--dry-run</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هیچ تغییری اعمال نمی‌کند و فقط کارهایی را که انجام خواهند شد در خروجی نشان می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از جفت‌های key=value که feature gateهای قابلیت‌های مختلف را توصیف می‌کنند. گزینه‌ها عبارت‌اند از:<br/>RootlessControlPlane=true|false (آلفا - پیش‌فرض=false)</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای دستور init</p></td>
</tr>

<tr>
<td colspan="2">--ignore-preflight-errors strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از بررسی‌هایی که خطاهای آن‌ها به‌صورت هشدار نمایش داده می‌شود؛ برای نمونه: 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همهٔ بررسی‌ها را نادیده می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--image-repository string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "registry.k8s.io"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رجیستری کانتینری را که ایمیج‌های control plane از آن دریافت می‌شوند انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--kubernetes-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "stable-1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخهٔ مشخصی از کوبرنتیز را برای control plane انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--node-name string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام نود را تعیین می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--patches string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری‌ای که فایل‌هایی با نام &quot;target[suffix][+patchtype].extension&quot; در خود دارد؛ برای نمونه &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از &quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;، &quot;corednsdeployment&quot; یا &quot;kubeproxydaemonset&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد که با قالب‌های وصله‌ای پشتیبانی‌شده در kubectl مطابقت دارند. مقدار پیش‌فرض &quot;patchtype&quot; برابر با &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد. بخش &quot;suffix&quot; رشته‌ای اختیاری است که با آن می‌توان بر اساس ترتیب الفبایی-عددی تعیین کرد کدام وصله‌ها زودتر اعمال شوند.</p></td>
</tr>

<tr>
<td colspan="2">--pod-network-cidr string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدودهٔ نشانی‌های IP شبکهٔ Pod را تعیین می‌کند. اگر این مقدار تنظیم شود، control plane به‌طور خودکار برای هر نود CIDR تخصیص می‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--service-cidr string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "10.96.0.0/12"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدودهٔ دیگری از نشانی‌های IP را برای VIPهای Service به کار می‌گیرد.</p></td>
</tr>

<tr>
<td colspan="2">--service-dns-domain string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: "cluster.local"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دامنهٔ دیگری را برای Serviceها به کار می‌گیرد؛ برای نمونه &quot;myorg.internal&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--skip-certificate-key-print</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کلید رمزگذاری گواهی‌های control plane را چاپ نمی‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--skip-phases strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مراحلی که باید از اجرای آن‌ها صرف‌نظر شود.</p></td>
</tr>

<tr>
<td colspan="2">--skip-token-print</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکن راه‌اندازی پیش‌فرضی را که 'kubeadm init' تولید می‌کند چاپ نمی‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--token string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>توکنی که برای برقراری اعتماد دوطرفه میان نودها و نودهای control plane به کار می‌رود. قالب آن [a-z0-9]{6}.[a-z0-9]{16} است؛ برای نمونه abcdef.0123456789abcdef</p></td>
</tr>

<tr>
<td colspan="2">--token-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;پیش‌فرض: 24h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت‌زمانی که پس از آن توکن به‌طور خودکار حذف می‌شود (برای نمونه 1s، 2m یا 3h). اگر این مقدار '0' باشد، توکن هرگز منقضی نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--upload-certs</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گواهی‌های control plane را در Secret با نام kubeadm-certs بارگذاری می‌کند.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سیستم‌فایل ریشهٔ «واقعی» میزبان. با این گزینه، kubeadm با chroot به مسیر تعیین‌شده وارد می‌شود.</p></td>
</tr>

</tbody>
</table>
