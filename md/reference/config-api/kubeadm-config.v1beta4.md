---
title: پیکربندی kubeadm (v1beta4)
content_type: tool-reference
package: kubeadm.k8s.io/v1beta4
auto_generated: true
---
<h2>نمای کلی</h2>
<p>بسته v1beta4 نسخه v1beta4 از قالب فایل پیکربندی kubeadm را تعریف می‌کند.
این نسخه با رفع چند مشکل جزئی و افزودن چند فیلد جدید، قالب v1beta3 را بهبود می‌بخشد.</p>
<p>فهرست تغییرات نسبت به v1beta3:</p>
<p>v1.35:</p>
<ul>
<li>افزودن فیلد <code>httpEndpoints</code> به <code>ClusterConfiguration.etcd.externalEtcd</code> که می‌توان از آن برای
پیکربندی نقاط پایانی HTTP برای ارتباط با etcd در v1beta4 استفاده کرد.
این فیلد برای جداکردن ترافیک HTTP (مانند نقاط پایانی <code>/metrics</code> و <code>/health</code>)
از ترافیک gRPC که توسط <code>endpoints</code> مدیریت می‌شود به کار می‌رود.
این جداسازی کنترل دسترسی بهتری را ممکن می‌کند، زیرا نقاط پایانی HTTP را می‌توان بدون
در معرض قراردادن رابط اصلی gRPC در دسترس قرار داد.
این فیلد با پیکربندی <code>--listen-client-http-urls</code> در etcd متناظر است.
در صورت مشخص‌نشدن، <code>endpoints</code> هم برای ترافیک gRPC و هم برای ترافیک HTTP استفاده خواهد شد.</li>
</ul>
<p>v1.34:</p>
<ul>
<li>افزودن &quot;ECDSA-P384&quot; به گزینه‌های مجاز الگوریتم رمزنگاری برای <code>ClusterConfiguration.encryptionAlgorithm</code>.</li>
</ul>
<p>v1.33:</p>
<ul>
<li>افزودن فیلد <code>EtcdUpgrade</code> به <code>UpgradeConfiguration.plan</code> که می‌توان از آن برای
کنترل نمایش یا عدم نمایش طرح ارتقای etcd استفاده کرد.</li>
</ul>
<p>v1.31:</p>
<ul>
<li>پشتیبانی از متغیرهای محیطی سفارشی در مؤلفه‌های control plane در <code>ClusterConfiguration</code>.
برای این کار از <code>apiServer.extraEnvs</code>، <code>controllerManager.extraEnvs</code>، <code>scheduler.extraEnvs</code> و
<code>etcd.local.extraEnvs</code> استفاده کنید.</li>
<li>نوع API با نام <code>ResetConfiguration</code> اکنون در v1beta4 پشتیبانی می‌شود.
کاربران می‌توانند با ارسال یک فایل <code>--config</code> به <code>kubeadm reset</code>، یک نود را بازنشانی کنند.</li>
<li>حالت اجرای آزمایشی (dry run) اکنون در <code>InitConfiguration</code> و <code>JoinConfiguration</code> قابل پیکربندی است.</li>
<li>نگاشت‌های موجود آرگومان‌های اضافی از نوع رشته/رشته با آرگومان‌های اضافی ساخت‌یافته جایگزین شده‌اند
که از موارد تکراری پشتیبانی می‌کنند. این تغییر در <code>ClusterConfiguration</code> برای <code>apiServer.extraArgs</code>،
<code>controllerManager.extraArgs</code>، <code>scheduler.extraArgs</code> و <code>etcd.local.extraArgs</code> اعمال می‌شود.
همچنین برای <code>nodeRegistration.kubeletExtraArgs</code> نیز اعمال می‌شود.</li>
<li>افزودن <code>ClusterConfiguration.encryptionAlgorithm</code> که می‌توان از آن برای تعیین الگوریتم
رمزنگاری نامتقارن مورد استفاده برای کلیدها و گواهی‌های این کلاستر استفاده کرد. مقدار آن می‌تواند یکی از
<code>&quot;RSA-2048&quot;</code> (پیش‌فرض)، <code>&quot;RSA-3072&quot;</code>، <code>&quot;RSA-4096&quot;</code> یا <code>&quot;ECDSA-P256&quot;</code> باشد.</li>
<li>افزودن <code>ClusterConfiguration.dns.disabled</code> و <code>ClusterConfiguration.proxy.disabled</code>
که می‌توان از آن‌ها برای غیرفعال‌کردن افزونه‌های CoreDNS و kube-proxy در زمان راه‌اندازی اولیه
کلاستر استفاده کرد. رد شدن از فازهای افزونه‌های مربوطه در زمان ایجاد کلاستر نیز
همین فیلدها را روی <code>true</code> تنظیم می‌کند.</li>
<li>افزودن فیلد <code>nodeRegistration.imagePullSerial</code> در <code>InitConfiguration</code> و <code>JoinConfiguration</code> که
می‌توان از آن برای کنترل اینکه kubeadm ایمیج‌ها را به‌صورت ترتیبی یا موازی دریافت کند، استفاده کرد.</li>
<li>API با نام <code>UpgradeConfiguration</code> در kubeadm اکنون هنگام ارسال
<code>--config</code> به زیردستورهای <code>kubeadm upgrade</code> در v1beta4 پشتیبانی می‌شود. استفاده از پیکربندی مؤلفه‌ها برای <code>kubelet</code> و <code>kube-proxy</code>،
<code>InitConfiguration</code> و <code>ClusterConfiguration</code> منسوخ شده است و هنگام ارسال <code>--config</code> به
زیردستورهای <code>upgrade</code> نادیده گرفته می‌شود.</li>
<li>افزودن ساختار <code>Timeouts</code> به <code>InitConfiguration</code>، <code>JoinConfiguration</code>، <code>ResetConfiguration</code> و <code>UpgradeConfiguration</code>
که می‌توان از آن برای پیکربندی مهلت‌های زمانی مختلف استفاده کرد.
فیلد <code>ClusterConfiguration.timeoutForControlPlane</code> با <code>Timeouts.controlPlaneComponentHealthCheck</code> جایگزین شده است.
فیلد <code>JoinConfiguration.discovery.timeout</code> با <code>timeouts.Discovery</code> جایگزین شده است.</li>
<li>افزودن فیلدهای <code>certificateValidityPeriod</code> و <code>caCertificateValidityPeriod</code> به <code>ClusterConfiguration</code>. این فیلدها
را می‌توان برای کنترل مدت اعتبار گواهی‌هایی که kubeadm در زیردستورهایی مانند <code>init</code>،
<code>join</code>، <code>upgrade</code> و <code>certs</code> تولید می‌کند، به کار برد. مقادیر پیش‌فرض همچنان ۱ سال برای گواهی‌های غیر CA و ۱۰ سال برای گواهی‌های
CA است. همچنان فقط گواهی‌های غیر CA با <code>kubeadm certs renew</code> قابل تمدید هستند.</li>
</ul>
<h1>مهاجرت از نسخه‌های قدیمی پیکربندی kubeadm</h1>
<ul>
<li>kubeadm نسخه v1.15.x و جدیدتر را می‌توان برای مهاجرت از v1beta1 به v1beta2 به کار برد.</li>
<li>kubeadm نسخه v1.22.x و جدیدتر دیگر از v1beta1 و APIهای قدیمی‌تر پشتیبانی نمی‌کند، اما می‌توان از آن برای مهاجرت از v1beta2 به v1beta3 استفاده کرد.</li>
<li>kubeadm نسخه v1.27.x و جدیدتر دیگر از v1beta2 و APIهای قدیمی‌تر پشتیبانی نمی‌کند.</li>
<li>kubeadm نسخه v1.31.x و جدیدتر را می‌توان برای مهاجرت از v1beta3 به v1beta4 به کار برد.</li>
</ul>
<h2>مفاهیم پایه</h2>
<p>روش توصیه‌شده برای پیکربندی kubeadm این است که یک فایل پیکربندی YAML را با گزینه
<code>--config</code> ارسال کنید. برخی از گزینه‌های پیکربندی تعریف‌شده در فایل پیکربندی
kubeadm به‌صورت فلگ‌های خط فرمان نیز در دسترس هستند، اما در این روش فقط
رایج‌ترین و ساده‌ترین موارد استفاده پشتیبانی می‌شوند.</p>
<p>یک فایل پیکربندی kubeadm می‌تواند شامل چندین نوع پیکربندی باشد که با سه خط تیره (<code>---</code>) از هم جدا می‌شوند.</p>
<p>kubeadm از انواع پیکربندی زیر پشتیبانی می‌کند:</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ClusterConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>JoinConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ResetConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>UpgradeConfiguration<span style="color:#bbb">
</span></pre><p>برای چاپ مقادیر پیش‌فرض اقدام‌های <code>init</code> و <code>join</code> از دستورهای زیر استفاده کنید:</p>
<pre style="background-color:#fff">kubeadm config print init-defaults
kubeadm config print join-defaults
kubeadm config print reset-defaults
kubeadm config print upgrade-defaults
</pre><p>فهرست انواع پیکربندی که باید در یک فایل پیکربندی گنجانده شوند، به اقدامی که
انجام می‌دهید (<code>init</code> یا <code>join</code>) و به گزینه‌های پیکربندی‌ای که قصد استفاده از آن‌ها را دارید (مقادیر پیش‌فرض یا سفارشی‌سازی پیشرفته) بستگی دارد.</p>
<p>اگر برخی از انواع پیکربندی ارائه نشوند یا فقط به‌صورت ناقص ارائه شوند، kubeadm از مقادیر پیش‌فرض استفاده می‌کند؛ مقادیر پیش‌فرضی
که kubeadm فراهم می‌کند شامل اعمال سازگاری مقادیر میان مؤلفه‌ها در صورت لزوم نیز هستند (برای مثال
فلگ <code>--cluster-cidr</code> در controller manager و <code>clusterCIDR</code> در kube-proxy).</p>
<p>کاربران همواره می‌توانند مقادیر پیش‌فرض را بازنویسی کنند، به‌جز زیرمجموعه کوچکی از تنظیمات
مرتبط با امنیت (برای مثال اعمال اجباری حالت مجوزدهی Node و RBAC در API server).</p>
<p>اگر کاربر نوع پیکربندی‌ای را ارائه کند که برای اقدامی که در حال انجام آن هستید مورد انتظار نیست، kubeadm
آن نوع‌ها را نادیده می‌گیرد و یک هشدار چاپ می‌کند.</p>
<h2>انواع پیکربندی kubeadm init</h2>
<p>هنگام اجرای kubeadm init با گزینه <code>--config</code>، می‌توان از انواع پیکربندی زیر استفاده کرد:
InitConfiguration، ClusterConfiguration، KubeProxyConfiguration و KubeletConfiguration، اما فقط یکی
از InitConfiguration و ClusterConfiguration الزامی است.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">bootstrapTokens</span>:<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">nodeRegistration</span>:<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span></pre><p>نوع InitConfiguration باید برای پیکربندی تنظیمات زمان اجرا به کار رود؛ این تنظیمات در مورد kubeadm init
شامل پیکربندی توکن bootstrap و همه تنظیماتی است که مختص نودی هستند که kubeadm
روی آن اجرا می‌شود، از جمله:</p>
<ul>
<li>
<p>NodeRegistration که شامل فیلدهای مربوط به ثبت نود جدید در کلاستر است؛
از آن برای سفارشی‌سازی نام نود، سوکت CRI مورد استفاده یا هر تنظیم دیگری که فقط باید روی این
نود اعمال شود (برای مثال IP نود) استفاده کنید.</p>
</li>
<li>
<p>LocalAPIEndpoint که نقطه پایانی نمونه API server را که باید روی این نود مستقر شود نشان می‌دهد؛
برای مثال از آن برای سفارشی‌سازی آدرس اعلان‌شده (advertise address) API server استفاده کنید.</p>
</li>
</ul>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ClusterConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">networking</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">etcd</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiServer</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>...<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span></pre><p>نوع ClusterConfiguration باید برای پیکربندی تنظیمات سراسری کلاستر به کار رود،
از جمله تنظیمات مربوط به:</p>
<ul>
<li>
<p><code>networking</code> که پیکربندی توپولوژی شبکه کلاستر را نگه می‌دارد؛ برای مثال از آن برای سفارشی‌سازی
زیرشبکه Pod یا زیرشبکه سرویس‌ها استفاده کنید.</p>
</li>
<li>
<p><code>etcd</code>: برای مثال از آن برای سفارشی‌سازی etcd محلی یا پیکربندی API server
برای استفاده از یک کلاستر etcd خارجی استفاده کنید.</p>
</li>
<li>
<p>پیکربندی‌های kube-apiserver، kube-scheduler و kube-controller-manager؛ از آن‌ها برای سفارشی‌سازی مؤلفه‌های control plane
با افزودن تنظیمات سفارشی یا بازنویسی تنظیمات پیش‌فرض kubeadm استفاده کنید.</p>
</li>
</ul>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span></pre><p>نوع KubeProxyConfiguration باید برای تغییر پیکربندی‌ای که به نمونه‌های kube-proxy مستقرشده
در کلاستر ارسال می‌شود به کار رود. اگر این آبجکت ارائه نشود یا فقط به‌صورت ناقص ارائه شود، kubeadm مقادیر پیش‌فرض را اعمال می‌کند.</p>
<p>برای مستندات رسمی kube-proxy به https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ یا
https://pkg.go.dev/k8s.io/kube-proxy/config/v1alpha1#KubeProxyConfiguration
مراجعه کنید.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span></pre><p>نوع KubeletConfiguration باید برای تغییر پیکربندی‌هایی که به همه نمونه‌های kubelet مستقرشده
در کلاستر ارسال می‌شوند به کار رود. اگر این آبجکت ارائه نشود یا فقط به‌صورت ناقص ارائه شود، kubeadm مقادیر پیش‌فرض را اعمال می‌کند.</p>
<p>برای مستندات رسمی kubelet به https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/ یا
https://pkg.go.dev/k8s.io/kubelet/config/v1beta1#KubeletConfiguration
مراجعه کنید.</p>
<p>در اینجا یک نمونه کاملاً تکمیل‌شده از یک فایل YAML واحد آمده است که شامل چندین
نوع پیکربندی برای استفاده در یک اجرای <code>kubeadm init</code> است.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">bootstrapTokens</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- <span style="color:#000;font-weight:bold">token</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;9a08jv.c0izixklcxtmnze7&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">description</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;kubeadm bootstrap token&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">ttl</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;24h&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span>- <span style="color:#000;font-weight:bold">token</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;783bde.3f89s0fje9f38fhf&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">description</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;another bootstrap token&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">usages</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- authentication<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- signing<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">groups</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- system:bootstrappers:kubeadm:default-node-token<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">nodeRegistration</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;ec2-10-100-0-1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">criSocket</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;unix:///var/run/containerd/containerd.sock&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">taints</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">key</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;kubeadmNode&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;someValue&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">effect</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;NoSchedule&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">kubeletExtraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>v<span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;5&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">ignorePreflightErrors</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- IsPrivilegedUser<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">imagePullPolicy</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;IfNotPresent&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">imagePullSerial</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">true</span><span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">localAPIEndpoint</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">advertiseAddress</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.100.0.1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">bindPort</span>:<span style="color:#bbb"> </span><span style="color:#099">6443</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">certificateKey</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;e6a2eb8581237ab72a4f494f30285ec12a9694d750b9785706a83bfcbbbd2204&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">skipPhases</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- preflight<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">timeouts</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">controlPlaneComponentHealthCheck</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;60s&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">kubenetesAPICall</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;40s&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span>---<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ClusterConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">etcd</span>:<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic"># one of local or external</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">local</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">imageRepository</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;registry.k8s.io&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">imageTag</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;3.2.24&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">dataDir</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/var/lib/etcd&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>listen-client-urls<span style="color:#bbb">
</span><span style="color:#bbb">        </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span>http://<span style="color:#099">10.100.0.1</span>:<span style="color:#099">2379</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">extraEnvs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>SOME_VAR<span style="color:#bbb">
</span><span style="color:#bbb">        </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span>SOME_VALUE<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">serverCertSANs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- ec2<span style="color:#099">-10-100-0-1.</span>compute<span style="color:#099">-1.</span>amazonaws.com<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">peerCertSANs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- <span style="color:#099">10.100.0.1</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic"># external:</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic">#   endpoints:</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic">#     - 10.100.0.1:2379</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic">#     - 10.100.0.2:2379</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic">#   caFile: &#34;/etcd/kubernetes/pki/etcd/etcd-ca.crt&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic">#   certFile: &#34;/etcd/kubernetes/pki/etcd/etcd.crt&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic">#   keyFile: &#34;/etcd/kubernetes/pki/etcd/etcd.key&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">networking</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">serviceSubnet</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.96.0.0/16&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">podSubnet</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.244.0.0/24&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">dnsDomain</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;cluster.local&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kubernetesVersion</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;v1.21.0&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">controlPlaneEndpoint</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.100.0.1:6443&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiServer</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>authorization-mode<span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span>Node,RBAC<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraEnvs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>SOME_VAR<span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span>SOME_VALUE<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;some-volume&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">hostPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">mountPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-pod-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">readOnly</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">false</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">pathType</span>:<span style="color:#bbb"> </span>File<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">certSANs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#d14">&#34;10.100.1.1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#d14">&#34;ec2-10-100-0-1.compute-1.amazonaws.com&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">controllerManager</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>node-cidr-mask-size<span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;20&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;some-volume&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">hostPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">mountPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-pod-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">readOnly</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">false</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">pathType</span>:<span style="color:#bbb"> </span>File<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">scheduler</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span>address<span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span><span style="color:#099">10.100.0.1</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;some-volume&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">hostPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">mountPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-pod-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">readOnly</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">false</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">pathType</span>:<span style="color:#bbb"> </span>File<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">certificatesDir</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/kubernetes/pki&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">imageRepository</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;registry.k8s.io&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">clusterName</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;example-cluster&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">encryptionAlgorithm</span>:<span style="color:#bbb"> </span>ECDSA-P256<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">dns</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">disabled</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">true</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic"># disable CoreDNS</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">proxy</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">disabled</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">true</span><span style="color:#bbb">   </span><span style="color:#998;font-style:italic"># disable kube-proxy</span><span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span>---<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#998;font-style:italic"># kubelet specific options here</span><span style="color:#bbb">
</span><span style="color:#bbb"></span>---<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#998;font-style:italic"># kube-proxy specific options here</span><span style="color:#bbb">
</span></pre><h2>انواع پیکربندی kubeadm join</h2>
<p>هنگام اجرای kubeadm join با گزینه --config، باید نوع JoinConfiguration ارائه شود.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>JoinConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">discovery</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">bootstrapToken</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">apiServerEndpoint</span>:<span style="color:#bbb"> </span>some-address:<span style="color:#099">6443</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">token</span>:<span style="color:#bbb"> </span>abcdef.0123456789abcdef<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">unsafeSkipCAVerification</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">true</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">tlsBootstrapToken</span>:<span style="color:#bbb"> </span>abcdef.0123456789abcdef<span style="color:#bbb">
</span></pre><p>نوع JoinConfiguration باید برای پیکربندی تنظیمات زمان اجرا به کار رود؛ این تنظیمات در مورد kubeadm join
شامل روش کشف (discovery) مورد استفاده برای دسترسی به اطلاعات کلاستر و همه تنظیماتی است که مختص
نودی هستند که kubeadm روی آن اجرا می‌شود، از جمله:</p>
<ul>
<li>
<p><code>nodeRegistration</code> که شامل فیلدهای مربوط به ثبت نود جدید در کلاستر است؛
از آن برای سفارشی‌سازی نام نود، سوکت CRI مورد استفاده یا هر تنظیم دیگری که فقط باید روی این
نود اعمال شود (برای مثال IP نود) استفاده کنید.</p>
</li>
<li>
<p><code>apiEndpoint</code> که نقطه پایانی نمونه API server را که در نهایت باید روی این نود مستقر شود نشان می‌دهد.</p>
</li>
</ul>
<h2>انواع پیکربندی kubeadm reset</h2>
<p>هنگام اجرای <code>kubeadm reset</code> با گزینه <code>--config</code>، باید نوع <code>ResetConfiguration</code> ارائه شود.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ResetConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span>...<span style="color:#bbb">
</span></pre><h2>انواع پیکربندی kubeadm upgrade</h2>
<p>هنگام اجرای <code>kubeadm upgrade</code> با گزینه <code>--config</code>، باید نوع <code>UpgradeConfiguration</code> ارائه شود.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta4<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>UpgradeConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apply</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">diff</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">node</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">plan</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span></pre><p>ساختار <code>UpgradeConfiguration</code> شامل چند زیرساختار است که هر کدام فقط برای زیردستورهای مختلف
<code>kubeadm upgrade</code> اعمال می‌شوند. برای مثال، زیرساختار <code>apply</code> با زیردستور <code>kubeadm upgrade apply</code> استفاده می‌شود
و در چنین حالتی همه زیرساختارهای دیگر نادیده گرفته می‌شوند.</p>

## انواع منبع (Resource Types)


- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)
- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)
- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)
- [ResetConfiguration](#kubeadm-k8s-io-v1beta4-ResetConfiguration)
- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)
  
    
    

## `BootstrapToken`     {#BootstrapToken}
    

**نمایش داده شده در:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)


<p>BootstrapToken یک توکن بوت‌استرپ را توصیف می‌کند که به‌صورت یک Secret در کلاستر ذخیره می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>token</code> <B>[الزامی]</B><br/>
<a href="#BootstrapTokenString"><code>BootstrapTokenString</code></a>
</td>
<td>
   <p><code>token</code> برای برقراری اعتماد دوطرفه بین نودها و control plane به کار می‌رود.
از آن برای پیوستن نودها به کلاستر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>description</code><br/>
<code>string</code>
</td>
<td>
   <p><code>description</code> پیامی خوانا برای انسان تعیین می‌کند که توضیح می‌دهد این توکن چرا وجود دارد و برای چه
منظوری استفاده می‌شود، تا سایر مدیران بتوانند هدف آن را بدانند.</p>
</td>
</tr>
<tr><td><code>ttl</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>ttl</code> مدت زمان زنده ماندن (time to live) این توکن را تعیین می‌کند. مقدار پیش‌فرض <code>24h</code> است.
<code>expires</code> و <code>ttl</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تنظیم کرد.</p>
</td>
</tr>
<tr><td><code>expires</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p><code>expires</code> زمان انقضای این توکن را مشخص می‌کند. به‌طور پیش‌فرض، مقدار آن در زمان اجرا و بر اساس
<code>ttl</code> به‌صورت پویا تنظیم می‌شود. <code>expires</code> و <code>ttl</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تنظیم کرد.</p>
</td>
</tr>
<tr><td><code>usages</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>usages</code> شیوه‌هایی را که می‌توان از این توکن استفاده کرد توصیف می‌کند. به‌طور پیش‌فرض می‌توان از آن
برای برقراری اعتماد دوطرفه استفاده کرد، اما این رفتار را می‌توان در اینجا تغییر داد.</p>
</td>
</tr>
<tr><td><code>groups</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>groups</code> گروه‌های اضافی را مشخص می‌کند که این توکن در صورت استفاده برای احراز هویت،
به‌عنوان آن‌ها احراز هویت می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `BootstrapTokenString`     {#BootstrapTokenString}
    

**نمایش داده شده در:**

- [BootstrapToken](#BootstrapToken)


<p>BootstrapTokenString توکنی با قالب <code>abcdef.abcdef0123456789</code> است که هم برای اعتبارسنجی در دسترس بودن عملی
API server از دید نودِ در حال پیوستن، و هم به‌عنوان روش احراز هویت نود در مرحله بوت‌استرپ
دستور &quot;kubeadm join&quot; به کار می‌رود. این توکن کوتاه‌مدت است و باید کوتاه‌مدت باشد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>-</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
<tr><td><code>-</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحاتی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>
  

## `ClusterConfiguration`     {#kubeadm-k8s-io-v1beta4-ClusterConfiguration}
    


<p>ClusterConfiguration شامل پیکربندی سراسری کلاستر برای یک کلاستر kubeadm است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ClusterConfiguration</code></td></tr>
    
  
<tr><td><code>etcd</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Etcd"><code>Etcd</code></a>
</td>
<td>
   <p><code>etcd</code> پیکربندی etcd را در بر دارد.</p>
</td>
</tr>
<tr><td><code>networking</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Networking"><code>Networking</code></a>
</td>
<td>
   <p><code>networking</code> پیکربندی توپولوژی شبکه کلاستر را در بر دارد.</p>
</td>
</tr>
<tr><td><code>kubernetesVersion</code><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> نسخه هدف control plane است.</p>
</td>
</tr>
<tr><td><code>controlPlaneEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p><code>controlPlaneEndpoint</code> یک آدرس IP یا نام DNS پایدار را برای control plane تعیین می‌کند؛
این مقدار می‌تواند یک آدرس IP معتبر یا یک زیردامنه DNS مطابق RFC-1123 باشد که هر دو می‌توانند همراه با پورت TCP اختیاری باشند.
اگر <code>controlPlaneEndpoint</code> مشخص نشده باشد، از <code>advertiseAddress</code> + <code>bindPort</code>
استفاده می‌شود؛ اگر <code>controlPlaneEndpoint</code> بدون پورت TCP مشخص شده باشد،
از <code>bindPort</code> استفاده می‌شود.
موارد استفاده ممکن عبارت‌اند از:</p>
<ul>
<li>در کلاستری با بیش از یک نمونه control plane، باید آدرس
load balancer خارجی که در مقابل نمونه‌های control plane قرار دارد، به این فیلد
اختصاص داده شود.</li>
<li>در محیط‌هایی که بازیافت اجباری نودها اعمال می‌شود، می‌توان از <code>controlPlaneEndpoint</code>
برای اختصاص یک DNS پایدار به control plane استفاده کرد.</li>
</ul>
</td>
</tr>
<tr><td><code>apiServer</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-APIServer"><code>APIServer</code></a>
</td>
<td>
   <p><code>apiServer</code> شامل تنظیمات اضافی برای API server است.</p>
</td>
</tr>
<tr><td><code>controllerManager</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>controllerManager</code> شامل تنظیمات اضافی برای controller manager است.</p>
</td>
</tr>
<tr><td><code>scheduler</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>scheduler</code> شامل تنظیمات اضافی برای زمان‌بند است.</p>
</td>
</tr>
<tr><td><code>dns</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-DNS"><code>DNS</code></a>
</td>
<td>
   <p><code>dns</code> گزینه‌های افزونه DNS نصب‌شده در کلاستر را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>proxy</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-Proxy"><code>Proxy</code></a>
</td>
<td>
   <p><code>proxy</code> گزینه‌های افزونه پراکسی نصب‌شده در کلاستر را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>certificatesDir</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificatesDir</code> مشخص می‌کند که تمام گواهی‌های موردنیاز کجا ذخیره شوند یا از کجا خوانده شوند.</p>
</td>
</tr>
<tr><td><code>imageRepository</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageRepository</code> رجیستری کانتینری را تعیین می‌کند که ایمیج‌ها از آن دریافت می‌شوند.
اگر خالی باشد، به‌طور پیش‌فرض از <code>registry.k8s.io</code> استفاده می‌شود.
اگر نسخه کوبرنتیز یک بیلد CI باشد (نسخه کوبرنتیز با <code>ci/</code> شروع شود)،
<code>gcr.io/k8s-staging-ci-images</code> به‌عنوان مقدار پیش‌فرض برای مؤلفه‌های control plane
و kube-proxy استفاده می‌شود، در حالی که <code>registry.k8s.io</code> برای سایر ایمیج‌ها به کار می‌رود.</p>
</td>
</tr>
<tr><td><code>featureGates</code><br/>
<code>map[string]bool</code>
</td>
<td>
   <p><code>featureGates</code> شامل feature gateهای مختص kubeadm است که کاربر آن‌ها را فعال کرده است.</p>
</td>
</tr>
<tr><td><code>clusterName</code><br/>
<code>string</code>
</td>
<td>
   <p>نام کلاستر.
این نام در فایل‌های kubeconfig که توسط kubeadm تولید می‌شوند استفاده می‌شود و همچنین
به‌عنوان مقدار فلگ <code>--cluster-name</code> به kube-controller-manager داده می‌شود.
مقدار پیش‌فرض <code>&quot;kubernetes&quot;</code> است.</p>
</td>
</tr>
<tr><td><code>encryptionAlgorithm</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-EncryptionAlgorithmType"><code>EncryptionAlgorithmType</code></a>
</td>
<td>
   <p><code>encryptionAlgorithm</code> نوع الگوریتم رمزنگاری نامتقارنی را که برای کلیدها و
گواهی‌ها به کار می‌رود مشخص می‌کند. می‌تواند یکی از مقادیر <code>&quot;RSA-2048&quot;</code> (پیش‌فرض)، <code>&quot;RSA-3072&quot;</code>، <code>&quot;RSA-4096&quot;</code>، <code>&quot;ECDSA-P256&quot;</code>
یا <code>&quot;ECDSA-P384&quot;</code> باشد.</p>
</td>
</tr>
<tr><td><code>certificateValidityPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>certificateValidityPeriod</code> مدت اعتبار گواهی‌های غیر CA تولیدشده توسط kubeadm را مشخص می‌کند.
مقدار پیش‌فرض: `8760h`` (365 روز * 24 ساعت = 1 سال)</p>
</td>
</tr>
<tr><td><code>caCertificateValidityPeriod</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>caCertificateValidityPeriod</code> مدت اعتبار گواهی CA تولیدشده توسط kubeadm را مشخص می‌کند.
مقدار پیش‌فرض: <code>87600h</code> (365 روز * 24 ساعت * 10 = 10 سال)</p>
</td>
</tr>
</tbody>
</table>

## `InitConfiguration`     {#kubeadm-k8s-io-v1beta4-InitConfiguration}
    


<p>InitConfiguration شامل فهرستی از عناصر است که اطلاعات زمان اجرای مختص &quot;kubeadm init&quot; را در بر می‌گیرند.
اطلاعات مختص <code>kubeadm init</code>. این فیلدها فقط در نخستین اجرای <code>kubeadm init</code> استفاده می‌شوند.
پس از آن، اطلاعات این فیلدها در ConfigMap با نام <code>kubeadm-config</code> که برای مثال
توسط <code>kubeadm upgrade</code> استفاده می‌شود، بارگذاری نمی‌شود. این فیلدها باید omitempty باشند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>InitConfiguration</code></td></tr>
    
  
<tr><td><code>bootstrapTokens</code><br/>
<a href="#BootstrapToken"><code>[]BootstrapToken</code></a>
</td>
<td>
   <p><code>bootstrapTokens</code> در زمان اجرای <code>kubeadm init</code> در نظر گرفته می‌شود و مجموعه‌ای از توکن‌های بوت‌استرپ را که باید ایجاد شوند توصیف می‌کند.
این اطلاعات، تا حدی به دلیل ماهیت حساس آن‌ها، در configmap کلاستر kubeadm بارگذاری نمی‌شود.</p>
</td>
</tr>
<tr><td><code>dryRun</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> مشخص می‌کند که آیا حالت اجرای آزمایشی (dry run) فعال است یا خیر؛ در این حالت هیچ تغییری اعمال نمی‌شود
و فقط آنچه انجام می‌شد در خروجی نمایش داده می‌شود.</p>
</td>
</tr>
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> شامل فیلدهای مربوط به ثبت نود control plane جدید
در کلاستر است.</p>
</td>
</tr>
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p><code>localAPIEndpoint</code> نشان‌دهنده endpoint نمونه API server است که روی این
نود control plane مستقر شده است. در محیط‌های HA، این مقدار با <code>ClusterConfiguration.controlPlaneEndpoint</code>
از این جهت تفاوت دارد که <code>controlPlaneEndpoint</code> endpoint سراسری کلاستر است که سپس
درخواست‌ها را میان API serverهای مجزا توزیع بار می‌کند.
این آبجکت پیکربندی به شما امکان می‌دهد مشخص کنید API server محلی چه IP/نام DNS و پورتی را
به‌عنوان نشانی دسترسی به خود اعلام کند. به‌طور پیش‌فرض، kubeadm سعی می‌کند IP رابط پیش‌فرض را
به‌صورت خودکار تشخیص دهد و از آن استفاده کند، اما اگر این فرایند ناموفق بود، می‌توانید مقدار موردنظر را در اینجا تنظیم کنید.</p>
</td>
</tr>
<tr><td><code>certificateKey</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificateKey</code> کلیدی را تعیین می‌کند که گواهی‌ها و کلیدها پیش از بارگذاری
در یک Secret در کلاستر، در مرحله <code>uploadcerts init</code> با آن رمزنگاری می‌شوند.
کلید گواهی یک رشته با کدگذاری هگزادسیمال است که یک کلید AES با اندازه 32 بایت است.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> فهرستی از فازهایی است که در زمان اجرای دستور نادیده گرفته می‌شوند.
فهرست فازها را می‌توان با دستور <code>kubeadm init --help</code> به‌دست آورد.
فلگ <code>--skip-phases</code> بر این فیلد اولویت دارد.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> شامل گزینه‌های مربوط به اعمال پچ‌ها بر مؤلفه‌هایی است که kubeadm در طول
<code>kubeadm init</code> مستقر می‌کند.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p><code>timeouts</code> شامل مهلت‌های زمانی گوناگونی است که بر دستورهای kubeadm اعمال می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `JoinConfiguration`     {#kubeadm-k8s-io-v1beta4-JoinConfiguration}
    


<p>JoinConfiguration شامل عناصری است که یک نود خاص را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>JoinConfiguration</code></td></tr>
    
  
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> مشخص می‌کند که آیا حالت اجرای آزمایشی (dry run) فعال است یا خیر؛ در صورت تنظیم، هیچ تغییری اعمال نمی‌شود
و فقط آنچه انجام می‌شد در خروجی نمایش داده می‌شود.</p>
</td>
</tr>
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> شامل فیلدهای مربوط به ثبت نود control plane جدید
در کلاستر است.</p>
</td>
</tr>
<tr><td><code>caCertPath</code><br/>
<code>string</code>
</td>
<td>
   <p><code>caCertPath</code> مسیر مرجع صدور گواهی SSL است که برای ایمن‌سازی ارتباطات
بین نود و control plane استفاده می‌شود.
مقدار پیش‌فرض &quot;/etc/kubernetes/pki/ca.crt&quot; است.</p>
</td>
</tr>
<tr><td><code>discovery</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-Discovery"><code>Discovery</code></a>
</td>
<td>
   <p><code>discovery</code> گزینه‌هایی را مشخص می‌کند که kubelet در فرایند بوت‌استرپ TLS از آن‌ها استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>controlPlane</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-JoinControlPlane"><code>JoinControlPlane</code></a>
</td>
<td>
   <p><code>controlPlane</code> نمونه control plane اضافی را که باید روی نودِ در حال پیوستن
مستقر شود تعریف می‌کند. اگر nil باشد، هیچ نمونه control plane اضافی مستقر نخواهد شد.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> فهرستی از فازهایی است که در زمان اجرای دستور نادیده گرفته می‌شوند.
فهرست فازها را می‌توان با دستور <code>kubeadm join --help</code> به‌دست آورد.
فلگ <code>--skip-phases</code> بر این فیلد اولویت دارد.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> شامل گزینه‌های مربوط به اعمال پچ‌ها بر مؤلفه‌هایی است که
kubeadm در طول <code>kubeadm join</code> مستقر می‌کند.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p><code>timeouts</code> شامل مهلت‌های زمانی گوناگونی است که بر دستورهای kubeadm اعمال می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `ResetConfiguration`     {#kubeadm-k8s-io-v1beta4-ResetConfiguration}
    


<p>ResetConfiguration شامل فهرستی از فیلدهایی است که به‌طور خاص اطلاعات زمان اجرایی مختص <code>kubeadm reset</code> هستند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ResetConfiguration</code></td></tr>
    
  
<tr><td><code>cleanupTmpDir</code><br/>
<code>bool</code>
</td>
<td>
   <p>فیلد <code>cleanupTmpDir</code> مشخص می‌کند که آیا دایرکتوری &quot;/etc/kubernetes/tmp&quot; در طول فرایند بازنشانی (reset) پاک‌سازی شود یا خیر.</p>
</td>
</tr>
<tr><td><code>certificatesDir</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>certificatesDir</code> دایرکتوری‌ای را مشخص می‌کند که گواهی‌ها در آن ذخیره می‌شوند.
در صورت تعیین، این دایرکتوری در طول فرایند بازنشانی پاک‌سازی خواهد شد.</p>
</td>
</tr>
<tr><td><code>criSocket</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>criSocket</code> برای دریافت اطلاعات container runtime و برای
حذف کانتینرها استفاده می‌شود.
اگر <code>criSocket</code> از طریق flag یا فایل پیکربندی مشخص نشده باشد، kubeadm تلاش می‌کند
به‌جای آن یک سوکت CRI معتبر را شناسایی کند.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p>فیلد <code>dryRun</code> مشخص می‌کند که آیا حالت اجرای آزمایشی (dry run) فعال است یا خیر. در صورت تنظیم‌شدن، هیچ تغییری اعمال نمی‌شود
و فقط خروجی کارهایی که انجام می‌شدند نمایش داده می‌شود.</p>
</td>
</tr>
<tr><td><code>force</code><br/>
<code>bool</code>
</td>
<td>
   <p>پرچم <code>force</code> به kubeadm دستور می‌دهد که نود را بدون درخواست تأیید بازنشانی کند.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>ignorePreflightErrors</code> فهرستی از خطاهای بررسی‌های پیش‌از‌اجرا (pre-flight) را مشخص می‌کند که در طول
فرایند بازنشانی نادیده گرفته می‌شوند؛ برای مثال <code>IsPrivilegedUser,Swap</code>.
مقدار <code>all</code> خطاهای همه بررسی‌ها را نادیده می‌گیرد.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>skipPhases</code> فهرستی از فازهایی است که در طول اجرای فرمان نادیده گرفته می‌شوند.
فهرست فازها را می‌توان با فرمان <code>kubeadm reset phase --help</code> به دست آورد.</p>
</td>
</tr>
<tr><td><code>unmountFlags</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>unmountFlags</code> فهرستی از پرچم‌های فراخوانی سیستمی <code>unmount2()</code> است که kubeadm می‌تواند هنگام جداسازی (unmount) 
دایرکتوری‌ها در طول &quot;reset&quot; از آن‌ها استفاده کند. این پرچم می‌تواند یکی از مقادیر <code>&quot;MNT_FORCE&quot;</code>، <code>&quot;MNT_DETACH&quot;</code>،
<code>&quot;MNT_EXPIRE&quot;</code> و <code>&quot;UMOUNT_NOFOLLOW&quot;</code> باشد. به‌طور پیش‌فرض این فهرست خالی است.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p>Timeouts شامل زمان‌های انتظار (timeout) گوناگونی است که برای فرمان‌های kubeadm اعمال می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `UpgradeConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeConfiguration}
    


<p>UpgradeConfiguration شامل فهرستی از گزینه‌هاست که مختص زیرفرمان‌های <code>kubeadm upgrade</code> هستند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta4</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>UpgradeConfiguration</code></td></tr>
    
  
<tr><td><code>apply</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradeApplyConfiguration"><code>UpgradeApplyConfiguration</code></a>
</td>
<td>
   <p>فیلد <code>apply</code> فهرستی از گزینه‌ها را در بر دارد که مختص فرمان <code>kubeadm upgrade apply</code> هستند.</p>
</td>
</tr>
<tr><td><code>diff</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradeDiffConfiguration"><code>UpgradeDiffConfiguration</code></a>
</td>
<td>
   <p>فیلد <code>diff</code> فهرستی از گزینه‌ها را در بر دارد که مختص فرمان <code>kubeadm upgrade diff</code> هستند.</p>
</td>
</tr>
<tr><td><code>node</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradeNodeConfiguration"><code>UpgradeNodeConfiguration</code></a>
</td>
<td>
   <p>فیلد <code>node</code> فهرستی از گزینه‌ها را در بر دارد که مختص فرمان <code>kubeadm upgrade node</code> هستند.</p>
</td>
</tr>
<tr><td><code>plan</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-UpgradePlanConfiguration"><code>UpgradePlanConfiguration</code></a>
</td>
<td>
   <p>فیلد <code>plan</code> فهرستی از گزینه‌ها را در بر دارد که مختص فرمان <code>kubeadm upgrade plan</code> هستند.</p>
</td>
</tr>
<tr><td><code>timeouts</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Timeouts"><code>Timeouts</code></a>
</td>
<td>
   <p>فیلد <code>timeouts</code> شامل زمان‌های انتظار (timeout) گوناگونی است که برای فرمان‌های kubeadm اعمال می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `APIEndpoint`     {#kubeadm-k8s-io-v1beta4-APIEndpoint}
    

**Appears in:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinControlPlane](#kubeadm-k8s-io-v1beta4-JoinControlPlane)


<p>ساختار APIEndpoint شامل عناصر یک نمونه API server است که روی یک نود مستقر شده است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>advertiseAddress</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>dvertiseAddress</code> آدرس IP را تعیین می‌کند که API server آن را اعلام (advertise) می‌کند.</p>
</td>
</tr>
<tr><td><code>bindPort</code><br/>
<code>int32</code>
</td>
<td>
   <p>فیلد <code>bindPort</code> درگاه امنی را تعیین می‌کند که API Server به آن متصل (bind) می‌شود.
مقدار پیش‌فرض ۶۴۴۳ است.</p>
</td>
</tr>
</tbody>
</table>

## `APIServer`     {#kubeadm-k8s-io-v1beta4-APIServer}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>APIServer شامل تنظیمات لازم برای استقرارهای API server در کلاستر است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ControlPlaneComponent</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>(اعضای <code>ControlPlaneComponent</code> در این نوع تعبیه (embed) شده‌اند.)
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>certSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>certSANs</code> نام‌های جایگزین موضوع (SAN) اضافی را برای گواهی امضای API Server تعیین می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `Arg`     {#kubeadm-k8s-io-v1beta4-Arg}
    

**Appears in:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta4-ControlPlaneComponent)

- [LocalEtcd](#kubeadm-k8s-io-v1beta4-LocalEtcd)

- [NodeRegistrationOptions](#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions)


<p>Arg یک آرگومان را با یک نام و یک مقدار نشان می‌دهد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>نام آرگومان.</p>
</td>
</tr>
<tr><td><code>value</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>مقدار آرگومان.</p>
</td>
</tr>
</tbody>
</table>

## `BootstrapTokenDiscovery`     {#kubeadm-k8s-io-v1beta4-BootstrapTokenDiscovery}
    

**Appears in:**

- [Discovery](#kubeadm-k8s-io-v1beta4-Discovery)


<p>BootstrapTokenDiscovery برای تعیین گزینه‌های کشف (discovery) مبتنی بر bootstrap token استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>token</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>token</code> توکنی است که برای اعتبارسنجی اطلاعات کلاستر دریافت‌شده از
control plane استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>apiServerEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>apiServerEndpoint</code> یک آدرس IP یا نام دامنه برای API server است که
اطلاعات از آن دریافت خواهد شد.</p>
</td>
</tr>
<tr><td><code>caCertHashes</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>caCertHashes</code> مجموعه‌ای از pinهای کلید عمومی را مشخص می‌کند که هنگام استفاده از کشف مبتنی بر توکن
بررسی می‌شوند. CA ریشه‌ای که در طول کشف پیدا می‌شود باید با یکی از این مقادیر مطابقت داشته باشد.
تعیین یک مجموعه خالی، pinning مربوط به CA ریشه را غیرفعال می‌کند که می‌تواند ناامن باشد.
هر هش به‌صورت <code>&lt;type&gt;:&lt;value&gt;</code> مشخص می‌شود که تنها نوع پشتیبانی‌شده در حال حاضر
&quot;sha256&quot; است. این مقدار، هش SHA-256 با کدگذاری هگزادسیمال از آبجکت Subject Public Key Info (SPKI)
در ASN.1 با کدگذاری DER است. این هش‌ها را می‌توان // برای مثال با OpenSSL محاسبه کرد.</p>
</td>
</tr>
<tr><td><code>unsafeSkipCAVerification</code><br/>
<code>bool</code>
</td>
<td>
   <p>فیلد <code>unsafeSkipCAVerification</code> کشف مبتنی بر توکن را بدون تأیید CA
از طریق <code>caCertHashes</code> مجاز می‌کند. این کار می‌تواند امنیت kubeadm را تضعیف کند، زیرا نودهای دیگر می‌توانند
خود را به‌جای control plane جا بزنند.</p>
</td>
</tr>
</tbody>
</table>

## `ControlPlaneComponent`     {#kubeadm-k8s-io-v1beta4-ControlPlaneComponent}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)

- [APIServer](#kubeadm-k8s-io-v1beta4-APIServer)


<p>ControlPlaneComponent شامل تنظیمات مشترک اجزای control plane کلاستر است.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>extraArgs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Arg"><code>[]Arg</code></a>
</td>
<td>
   <p>فیلد <code>extraArgs</code> مجموعه‌ای اضافی از پرچم‌ها (flags) است که به جزء control plane داده می‌شود.
نام هر آرگومان در این فهرست همان نام پرچم است که در خط فرمان ظاهر می‌شود، اما بدون خط تیره(های) ابتدایی.
آرگومان‌های اضافی، آرگومان‌های پیش‌فرض موجود را بازنویسی می‌کنند. آرگومان‌های اضافی تکراری مجاز هستند.</p>
</td>
</tr>
<tr><td><code>extraVolumes</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-HostPathMount"><code>[]HostPathMount</code></a>
</td>
<td>
   <p>فیلد <code>extraVolumes</code> مجموعه‌ای اضافی از حجم‌های (volume) میزبان است که روی جزء control plane مونت می‌شوند.</p>
</td>
</tr>
<tr><td><code>extraEnvs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-EnvVar"><code>[]EnvVar</code></a>
</td>
<td>
   <p>فیلد <code>extraEnvs</code> مجموعه‌ای اضافی از متغیرهای محیطی است که به جزء control plane داده می‌شود.
متغیرهای محیطی که با <code>extraEnvs</code> داده می‌شوند، هر متغیر محیطی موجود
یا متغیرهای محیطی <code>*_proxy</code> را که kubeadm به‌طور پیش‌فرض اضافه می‌کند، بازنویسی می‌کنند.</p>
</td>
</tr>
</tbody>
</table>

## `DNS`     {#kubeadm-k8s-io-v1beta4-DNS}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>DNS افزونه DNS را که باید در کلاستر استفاده شود تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(اعضای <code>ImageMeta</code> در این نوع تعبیه (embed) شده‌اند.)
   <p><code>imageMeta</code> امکان سفارشی‌سازی ایمیج مورد استفاده برای افزونه DNS را فراهم می‌کند.</p>
</td>
</tr>
<tr><td><code>disabled</code> <B>[Required]</B><br/>
<code>bool</code>
</td>
<td>
   <p>فیلد <code>disabled</code> مشخص می‌کند که آیا این افزونه در کلاستر غیرفعال شود یا خیر.</p>
</td>
</tr>
</tbody>
</table>

## `Discovery`     {#kubeadm-k8s-io-v1beta4-Discovery}
    

**Appears in:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)


<p>Discovery گزینه‌هایی را مشخص می‌کند که kubelet در طول فرایند TLS Bootstrap از آن‌ها استفاده می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>bootstrapToken</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-BootstrapTokenDiscovery"><code>BootstrapTokenDiscovery</code></a>
</td>
<td>
   <p>فیلد <code>bootstrapToken</code> برای تعیین گزینه‌های کشف مبتنی بر bootstrap token استفاده می‌شود.
<code>bootstrapToken</code> و <code>file</code> متقابلاً ناسازگارند (نمی‌توان هر دو را همزمان تعیین کرد).</p>
</td>
</tr>
<tr><td><code>file</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-FileDiscovery"><code>FileDiscovery</code></a>
</td>
<td>
   <p>فیلد <code>file</code> برای تعیین یک فایل یا URL به یک فایل kubeconfig استفاده می‌شود که اطلاعات
کلاستر از آن بارگذاری می‌شود. <code>bootstrapToken</code> و <code>file</code> متقابلاً ناسازگارند.</p>
</td>
</tr>
<tr><td><code>tlsBootstrapToken</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>tlsBootstrapToken</code> توکنی است که برای TLS bootstrapping استفاده می‌شود.
اگر <code>bootstrapToken</code> تنظیم شده باشد، مقدار پیش‌فرض این فیلد <code>bootstrapToken.token</code> است، اما
می‌توان آن را بازنویسی کرد. اگر <code>file</code> تنظیم شده باشد، در صورتی که KubeConfigFile
هیچ اطلاعات احراز هویت دیگری نداشته باشد، این فیلد <strong>باید تنظیم شود</strong>.</p>
</td>
</tr>
</tbody>
</table>

## `EncryptionAlgorithmType`     {#kubeadm-k8s-io-v1beta4-EncryptionAlgorithmType}
    
(نام مستعار برای `string`)

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>EncryptionAlgorithmType می‌تواند نوع الگوریتم رمزنگاری نامتقارن را تعریف کند.</p>




## `EnvVar`     {#kubeadm-k8s-io-v1beta4-EnvVar}
    

**Appears in:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta4-ControlPlaneComponent)

- [LocalEtcd](#kubeadm-k8s-io-v1beta4-LocalEtcd)


<p>EnvVar یک متغیر محیطی موجود در یک Container را نشان می‌دهد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>EnvVar</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#envvar-v1-core"><code>core/v1.EnvVar</code></a>
</td>
<td>(اعضای <code>EnvVar</code> در این نوع تعبیه (embed) شده‌اند.)
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>

## `Etcd`     {#kubeadm-k8s-io-v1beta4-Etcd}
    

**Appears in:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>Etcd شامل عناصری است که پیکربندی Etcd را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>local</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-LocalEtcd"><code>LocalEtcd</code></a>
</td>
<td>
   <p>فیلد <code>local</code> گزینه‌های پیکربندی نمونه etcd محلی را فراهم می‌کند.
<code>local</code> و <code>external</code> متقابلاً ناسازگارند.</p>
</td>
</tr>
<tr><td><code>external</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-ExternalEtcd"><code>ExternalEtcd</code></a>
</td>
<td>
   <p>فیلد <code>external</code> نحوه اتصال به یک کلاستر etcd خارجی را توصیف می‌کند.
<code>local</code> و <code>external</code> متقابلاً ناسازگارند.</p>
</td>
</tr>
</tbody>
</table>

## `ExternalEtcd`     {#kubeadm-k8s-io-v1beta4-ExternalEtcd}
    

**Appears in:**

- [Etcd](#kubeadm-k8s-io-v1beta4-Etcd)


<p>ExternalEtcd یک کلاستر etcd خارجی را توصیف می‌کند.
Kubeadm اطلاعی از محل قرارگیری فایل‌های گواهی ندارد و باید آن‌ها را در اختیارش قرار داد.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoints</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>endpoints</code> شامل فهرست اعضای etcd است.
این فیلد URLهای کلاینت (معمولاً endpointهای gRPC) را برای ارتباط با etcd مشخص می‌کند.
به‌طور پیش‌فرض، این endpointها هم ترافیک gRPC (پروتکل اصلی etcd)
و هم ترافیک HTTP (متریک‌ها، بررسی‌های سلامت) را مدیریت می‌کنند. با این حال، اگر <code>httpEndpoints</code> پیکربندی شده باشد،
ترافیک gRPC و HTTP را می‌توان برای امنیت و کارایی بهتر از یکدیگر جدا کرد.
معادل پیکربندی <code>--listen-client-urls</code> در etcd است.</p>
</td>
</tr>
<tr><td><code>httpEndpoints</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>httpEndpoints</code> endpointهای HTTP اختصاصی برای ارتباط با etcd هستند.
در صورت پیکربندی، ترافیک HTTP (مانند endpointهای <code>/metics</code> و <code>/health</code>) از
ترافیک gRPC که توسط <code>endpoints</code> مدیریت می‌شود جدا می‌شود. این جداسازی کنترل دسترسی بهتری را ممکن می‌سازد،
زیرا endpointهای HTTP را می‌توان بدون در معرض قراردادن رابط اصلی gRPC در دسترس قرار داد.
معادل پیکربندی <code>--listen-client-http-urls</code> در etcd است.
اگر مقداردهی نشود، <code>endpoints</code> هم برای ترافیک gRPC و هم برای ترافیک HTTP استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>caFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>caFile</code> یک فایل مرجع گواهی (CA) SSL است که برای ایمن‌سازی ارتباط etcd استفاده می‌شود.
در صورت استفاده از اتصال TLS الزامی است.</p>
</td>
</tr>
<tr><td><code>certFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>certFile</code> یک فایل گواهی SSL است که برای ایمن‌سازی ارتباط etcd استفاده می‌شود.
در صورت استفاده از اتصال TLS الزامی است.</p>
</td>
</tr>
<tr><td><code>keyFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>keyFile</code> یک فایل کلید SSL است که برای ایمن‌سازی ارتباط etcd استفاده می‌شود.
در صورت استفاده از اتصال TLS الزامی است.</p>
</td>
</tr>
</tbody>
</table>

## `FileDiscovery`     {#kubeadm-k8s-io-v1beta4-FileDiscovery}
    

**Appears in:**

- [Discovery](#kubeadm-k8s-io-v1beta4-Discovery)


<p>FileDiscovery برای تعیین یک فایل یا URL به یک فایل kubeconfig استفاده می‌شود که اطلاعات
کلاستر از آن بارگذاری می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">Field</th><th>Description</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubeConfigPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>kubeConfigPath</code> برای تعیین مسیر واقعی فایل یا URL فایل kubeconfig استفاده می‌شود
که اطلاعات کلاستر از آن بارگذاری می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `HostPathMount`     {#kubeadm-k8s-io-v1beta4-HostPathMount}
    

**ظاهر می‌شود در:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta4-ControlPlaneComponent)


<p>HostPathMount شامل عناصری است که حجم‌هایی (volumes) را توصیف می‌کنند که از میزبان مانت می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>name</code> نام حجم (volume) درون قالب Pod است.</p>
</td>
</tr>
<tr><td><code>hostPath</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>hostPath</code> مسیری در میزبان است که درون Pod مانت خواهد شد.</p>
</td>
</tr>
<tr><td><code>mountPath</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>mountPath</code> مسیری درون Pod است که <code>hostPath</code> در آن مانت خواهد شد.</p>
</td>
</tr>
<tr><td><code>readOnly</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>readOnly</code> دسترسی نوشتن به حجم (volume) را کنترل می‌کند.</p>
</td>
</tr>
<tr><td><code>pathType</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#hostpathtype-v1-core"><code>core/v1.HostPathType</code></a>
</td>
<td>
   <p><code>pathType</code> نوع <code>hostPath</code> است.</p>
</td>
</tr>
</tbody>
</table>

## `ImageMeta`     {#kubeadm-k8s-io-v1beta4-ImageMeta}
    

**ظاهر می‌شود در:**

- [DNS](#kubeadm-k8s-io-v1beta4-DNS)

- [LocalEtcd](#kubeadm-k8s-io-v1beta4-LocalEtcd)


<p>ImageMeta امکان سفارشی‌سازی ایمیجی را فراهم می‌کند که برای مؤلفه‌هایی استفاده می‌شود
که از فرایند انتشار Kubernetes/Kubernetes منشأ نگرفته‌اند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>imageRepository</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageRepository</code> رجیستری کانتینر را برای دریافت ایمیج‌ها تعیین می‌کند.
اگر تنظیم نشود، به‌جای آن از <code>imageRepository</code> تعریف‌شده در ClusterConfiguration استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>imageTag</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageTag</code> امکان تعیین یک تگ برای ایمیج را فراهم می‌کند.
در صورتی که این مقدار تنظیم شود، kubeadm هنگام ارتقا، نسخه‌ی مؤلفه‌های
یادشده را به‌طور خودکار تغییر نمی‌دهد.</p>
</td>
</tr>
</tbody>
</table>

## `JoinControlPlane`     {#kubeadm-k8s-io-v1beta4-JoinControlPlane}
    

**ظاهر می‌شود در:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)


<p>JoinControlPlane شامل عناصری است که یک نمونه‌ی control plane اضافی را توصیف می‌کنند که باید روی نود در حال پیوستن مستقر شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p><code>localAPIEndpoint</code> نشان‌دهنده‌ی نقطه‌ی انتهایی (endpoint) نمونه‌ی API server است که باید
روی این نود مستقر شود.</p>
</td>
</tr>
<tr><td><code>certificateKey</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificateKey</code> کلیدی است که برای رمزگشایی گواهی‌ها پس از
دریافت آن‌ها از Secret، هنگام پیوستن یک نود control plane جدید استفاده می‌شود.
کلید رمزنگاری متناظر در InitConfiguration قرار دارد.
کلید گواهی یک رشته‌ی کدگذاری‌شده‌ی هگزادسیمال است که یک کلید AES با اندازه‌ی ۳۲ بایت است.</p>
</td>
</tr>
</tbody>
</table>

## `LocalEtcd`     {#kubeadm-k8s-io-v1beta4-LocalEtcd}
    

**ظاهر می‌شود در:**

- [Etcd](#kubeadm-k8s-io-v1beta4-Etcd)


<p>LocalEtcd بیان می‌کند که kubeadm باید یک کلاستر etcd را به‌صورت محلی اجرا کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(اعضای <code>ImageMeta</code> در این نوع تعبیه شده‌اند.)
   <p>ImageMeta امکان سفارشی‌سازی ایمیج کانتینر مورد استفاده برای etcd را فراهم می‌کند.
مشخص کردن یک ایمیج سفارشی etcd به <code>kubeadm upgrade</code> اعلام می‌کند که این ایمیج توسط کاربر مدیریت می‌شود
و ارتقای آن باید نادیده گرفته شود.</p>
</td>
</tr>
<tr><td><code>dataDir</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>dataDir</code> دایرکتوری‌ای است که etcd داده‌های خود را در آن قرار می‌دهد.
مقدار پیش‌فرض &quot;/var/lib/etcd&quot; است.</p>
</td>
</tr>
<tr><td><code>extraArgs</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta4-Arg"><code>[]Arg</code></a>
</td>
<td>
   <p><code>extraArgs</code> آرگومان‌های اضافی هستند که هنگام اجرای فایل باینری etcd
درون یک Pod ایستا به آن داده می‌شوند. نام هر آرگومان در این فهرست همان نام فلگ است
که در خط فرمان ظاهر می‌شود، اما بدون خط تیره‌ی ابتدایی.
آرگومان‌های اضافی، آرگومان‌های پیش‌فرض موجود را بازنویسی می‌کنند.
آرگومان‌های اضافی تکراری مجاز هستند.</p>
</td>
</tr>
<tr><td><code>extraEnvs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-EnvVar"><code>[]EnvVar</code></a>
</td>
<td>
   <p><code>extraEnvs</code> مجموعه‌ای اضافی از متغیرهای محیطی است که به
مؤلفه‌ی control plane داده می‌شود. متغیرهای محیطی که با <code>extraEnvs</code> داده شوند،
هر متغیر محیطی موجود یا متغیرهای محیطی <code>*_proxy</code> را که kubeadm به‌طور پیش‌فرض اضافه می‌کند
بازنویسی می‌کنند.</p>
</td>
</tr>
<tr><td><code>serverCertSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>serverCertSANs</code> نام‌های جایگزین موضوع (SAN) اضافی را برای گواهی امضای
سرور etcd تنظیم می‌کند.</p>
</td>
</tr>
<tr><td><code>peerCertSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>peerCertSANs</code> نام‌های جایگزین موضوع (SAN) اضافی را برای گواهی امضای
peer در etcd تنظیم می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `Networking`     {#kubeadm-k8s-io-v1beta4-Networking}
    

**ظاهر می‌شود در:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>Networking شامل عناصری است که پیکربندی شبکه‌ی کلاستر را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>serviceSubnet</code><br/>
<code>string</code>
</td>
<td>
   <p><code>serviceSubnet</code> زیرشبکه‌ای است که Serviceهای کوبرنتیز از آن استفاده می‌کنند. مقدار پیش‌فرض &quot;10.96.0.0/12&quot; است.</p>
</td>
</tr>
<tr><td><code>podSubnet</code><br/>
<code>string</code>
</td>
<td>
   <p><code>podSubnet</code> زیرشبکه‌ای است که Podها از آن استفاده می‌کنند.</p>
</td>
</tr>
<tr><td><code>dnsDomain</code><br/>
<code>string</code>
</td>
<td>
   <p><code>dnsDomain</code> دامنه‌ی DNS است که Serviceهای کوبرنتیز از آن استفاده می‌کنند. مقدار پیش‌فرض &quot;cluster.local&quot; است.</p>
</td>
</tr>
</tbody>
</table>

## `NodeRegistrationOptions`     {#kubeadm-k8s-io-v1beta4-NodeRegistrationOptions}
    

**ظاهر می‌شود در:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)


<p>NodeRegistrationOptions شامل فیلدهایی است که به ثبت یک control-plane یا نود جدید
در کلاستر، چه از طریق <code>kubeadm init</code> و چه از طریق <code>kubeadm join</code>، مربوط می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <p><code>name</code> فیلد <code>.Metadata.Name</code> آبجکت Node API است که در این عملیات
<code>kubeadm init</code> یا <code>kubeadm join</code> ایجاد خواهد شد.
این فیلد همچنین در فیلد <code>CommonName</code> گواهی کلاینت kubelet برای
API server استفاده می‌شود.
در صورت عدم ارائه، مقدار پیش‌فرض آن نام میزبان (hostname) نود است.</p>
</td>
</tr>
<tr><td><code>criSocket</code><br/>
<code>string</code>
</td>
<td>
   <p><code>criSocket</code> برای بازیابی اطلاعات container runtime استفاده می‌شود.
این اطلاعات برای استفاده‌ی مجدد در آینده، به‌صورت annotation روی آبجکت Node API ثبت خواهد شد.</p>
</td>
</tr>
<tr><td><code>taints</code> <B>[الزامی]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#taint-v1-core"><code>[]core/v1.Taint</code></a>
</td>
<td>
   <p><code>taints</code> مشخص می‌کند که آبجکت Node API باید با چه taintهایی ثبت شود.
اگر این فیلد تنظیم نشده باشد، یعنی nil باشد، برای نودهای control-plane به‌طور پیش‌فرض با یک taint مربوط به control-plane مقداردهی می‌شود.
اگر نمی‌خواهید نود control-plane خود را taint کنید، این فیلد را روی یک فهرست خالی تنظیم کنید،
یعنی در فایل YAML مقدار <code>taints: []</code> را قرار دهید. این فیلد صرفاً برای ثبت Node استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>kubeletExtraArgs</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Arg"><code>[]Arg</code></a>
</td>
<td>
   <p><code>kubeletExtraArgs</code> آرگومان‌های اضافی را به kubelet منتقل می‌کند.
آرگومان‌های این‌جا از طریق فایل محیطی که kubeadm هنگام اجرا برای source شدن توسط kubelet می‌نویسد،
به خط فرمان kubelet داده می‌شوند.
این مقادیر پیکربندی پایه‌ی عمومی در ConfigMap با نام <code>kubelet-config</code> را بازنویسی می‌کنند.
هنگام تجزیه (parsing)، فلگ‌ها اولویت بالاتری دارند. این مقادیر محلی هستند و مختص نودی‌اند
که kubeadm روی آن در حال اجراست. نام هر آرگومان در این فهرست همان نام فلگ است که در
خط فرمان ظاهر می‌شود، اما بدون خط تیره‌ی ابتدایی. آرگومان‌های اضافی، آرگومان‌های
پیش‌فرض موجود را بازنویسی می‌کنند. آرگومان‌های اضافی تکراری مجاز هستند.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> فهرستی از خطاهای پیش‌پرواز (pre-flight) را ارائه می‌دهد که هنگام
ثبت نود فعلی نادیده گرفته می‌شوند، برای مثال 'IsPrivilegedUser,Swap'.
مقدار 'all' خطاهای همه‌ی بررسی‌ها را نادیده می‌گیرد.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> سیاست دریافت ایمیج را در عملیات <code>init</code> و
<code>join</code> در kubeadm مشخص می‌کند.
مقدار این فیلد باید یکی از &quot;Always&quot;، &quot;IfNotPresent&quot; یا &quot;Never&quot; باشد.
اگر این فیلد تنظیم نشود، kubeadm مقدار پیش‌فرض آن را &quot;IfNotPresent&quot; قرار می‌دهد، یعنی
در صورت نبودن ایمیج‌های موردنیاز روی میزبان، آن‌ها را دریافت می‌کند.</p>
</td>
</tr>
<tr><td><code>imagePullSerial</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>imagePullSerial</code> مشخص می‌کند که دریافت ایمیج‌ها توسط kubeadm باید به‌صورت سریالی انجام شود یا موازی.
پیش‌فرض: true</p>
</td>
</tr>
</tbody>
</table>

## `Patches`     {#kubeadm-k8s-io-v1beta4-Patches}
    

**ظاهر می‌شود در:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)

- [UpgradeApplyConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeApplyConfiguration)

- [UpgradeNodeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeNodeConfiguration)


<p>Patches شامل گزینه‌هایی است که به اعمال وصله (patch) بر مؤلفه‌های مستقرشده توسط kubeadm مربوط می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>directory</code><br/>
<code>string</code>
</td>
<td>
   <p><code>directory</code> مسیر دایرکتوری‌ای است که شامل فایل‌هایی با نام
&quot;target[suffix][+patchtype].extension&quot; است.
برای مثال، &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از
&quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot;
و &quot;corednsdeployment&quot; باشد.
مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد و این مقادیر با قالب‌های وصله‌ای
که kubectl پشتیبانی می‌کند مطابقت دارند.
مقدار پیش‌فرض &quot;patchtype&quot; برابر &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد.
مقدار &quot;suffix&quot; یک رشته‌ی اختیاری است که می‌توان از آن برای تعیین این‌که کدام وصله‌ها
زودتر و بر اساس ترتیب الفبایی-عددی اعمال شوند استفاده کرد.</p>
</td>
</tr>
</tbody>
</table>

## `Proxy`     {#kubeadm-k8s-io-v1beta4-Proxy}
    

**ظاهر می‌شود در:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta4-ClusterConfiguration)


<p>Proxy افزونه‌ی پروکسی را که باید در کلاستر استفاده شود تعریف می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>disabled</code> <B>[الزامی]</B><br/>
<code>bool</code>
</td>
<td>
   <p><code>disabled</code> مشخص می‌کند که آیا این افزونه در کلاستر غیرفعال شود یا خیر.</p>
</td>
</tr>
</tbody>
</table>

## `Timeouts`     {#kubeadm-k8s-io-v1beta4-Timeouts}
    

**ظاهر می‌شود در:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta4-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta4-JoinConfiguration)

- [ResetConfiguration](#kubeadm-k8s-io-v1beta4-ResetConfiguration)

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>Timeouts شامل مهلت‌های زمانی گوناگونی است که بر دستورهای kubeadm اعمال می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>controlPlaneComponentHealthCheck</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>controlPlaneComponentHealthCheck</code> مدت زمانی است که باید منتظر ماند تا یک مؤلفه‌ی control plane،
مانند API server، در طول <code>kubeadm init</code> و <code>kubeadm join</code> سالم شود.
پیش‌فرض: 4m</p>
</td>
</tr>
<tr><td><code>kubeletHealthCheck</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>kubeletHealthCheck</code> مدت زمانی است که باید منتظر ماند تا kubelet
در طول <code>kubeadm init</code> و <code>kubeadm join</code> سالم شود.
پیش‌فرض: 4m</p>
</td>
</tr>
<tr><td><code>kubernetesAPICall</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>kubernetesAPICall</code> مدت زمانی است که باید منتظر ماند تا کلاینت kubeadm یک درخواست به
API server را کامل کند. این مقدار برای همه‌ی انواع متدها (GET، POST و غیره) اعمال می‌شود.
پیش‌فرض: 1m</p>
</td>
</tr>
<tr><td><code>etcdAPICall</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>etcdAPICall</code> مدت زمانی است که باید منتظر ماند تا کلاینت etcd در kubeadm یک درخواست به
کلاستر etcd را کامل کند.
پیش‌فرض: 2m</p>
</td>
</tr>
<tr><td><code>tlsBootstrap</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>tlsBootstrap</code> مدت زمانی است که باید منتظر ماند تا kubelet راه‌اندازی اولیه‌ی TLS (TLS bootstrap)
را برای یک نود در حال پیوستن کامل کند.
پیش‌فرض: 5m</p>
</td>
</tr>
<tr><td><code>discovery</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>discovery</code> مدت زمانی است که باید منتظر ماند تا kubeadm هویت API server را
برای یک نود در حال پیوستن اعتبارسنجی کند.
پیش‌فرض: 5m</p>
</td>
</tr>
<tr><td><code>upgradeManifests</code> <B>[الزامی]</B><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>upgradeManifests</code> مهلت زمانی برای ارتقای مانیفست‌های Pod ایستا است.
پیش‌فرض: 5m</p>
</td>
</tr>
</tbody>
</table>

## `UpgradeApplyConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeApplyConfiguration}
    

**ظاهر شده در:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradeApplyConfiguration شامل فهرستی از گزینه‌های قابل پیکربندی است که مختص دستور &quot;kubeadm upgrade apply&quot; هستند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesVersion</code><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> نسخه هدف control plane است.</p>
</td>
</tr>
<tr><td><code>allowExperimentalUpgrades</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>allowExperimentalUpgrades</code> به kubeadm دستور می‌دهد نسخه‌های ناپایدار کوبرنتیز را به‌عنوان گزینه‌ی ارتقا نمایش دهد و امکان ارتقا به نسخه‌ی آلفا، بتا یا release candidate کوبرنتیز را فراهم می‌کند.
مقدار پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>allowRCUpgrades</code><br/>
<code>bool</code>
</td>
<td>
   <p>فعال‌کردن <code>allowRCUpgrades</code> باعث می‌شود نسخه‌های release candidate کوبرنتیز به‌عنوان گزینه‌ی ارتقا نمایش داده شوند و امکان ارتقا به یک نسخه‌ی release candidate کوبرنتیز فراهم شود.</p>
</td>
</tr>
<tr><td><code>certificateRenewal</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>certificateRenewal</code> به kubeadm دستور می‌دهد در طول ارتقاها گواهی‌ها را تمدید کند.
مقدار پیش‌فرض: true.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> مشخص می‌کند که آیا حالت اجرای آزمایشی (dry run) فعال است یا خیر. در صورت فعال بودن، هیچ تغییری اعمال نمی‌شود و فقط کارهایی که انجام می‌شدند نمایش داده می‌شوند.</p>
</td>
</tr>
<tr><td><code>etcdUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>etcdUpgrade</code> به kubeadm دستور می‌دهد در طول ارتقاها، etcd را نیز ارتقا دهد.
مقدار پیش‌فرض: true.</p>
</td>
</tr>
<tr><td><code>forceUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p>پرچم <code>forceUpgrade</code> به kubeadm دستور می‌دهد کلاستر را بدون درخواست تأیید ارتقا دهد.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> فهرستی از خطاهای pre-flight را فراهم می‌کند که در طول فرایند ارتقا نادیده گرفته می‌شوند،
مانند <code>IsPrivilegedUser,Swap</code>. مقدار <code>all</code> خطاهای همه‌ی بررسی‌ها را نادیده می‌گیرد.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> شامل گزینه‌های مربوط به اعمال patchها بر مؤلفه‌هایی است که kubeadm در طول <code>kubeadm upgrade</code> مستقر کرده است.</p>
</td>
</tr>
<tr><td><code>printConfig</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>printConfig</code> مشخص می‌کند که آیا فایل پیکربندی که در ارتقا استفاده خواهد شد باید چاپ شود یا خیر.</p>
</td>
</tr>
<tr><td><code>skipPhases</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> فهرستی از فازهایی است که در طول اجرای دستور نادیده گرفته می‌شوند.
توجه: این فیلد در حال حاضر برای <code>kubeadm upgrade apply</code> نادیده گرفته می‌شود، اما در آینده پشتیبانی خواهد شد.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> سیاست دریافت ایمیج را در عملیات <code>kubeadm upgrade apply</code> مشخص می‌کند.
مقدار این فیلد باید یکی از &quot;Always&quot;، &quot;IfNotPresent&quot; یا &quot;Never&quot; باشد.
اگر این فیلد تنظیم نشود، kubeadm مقدار آن را به‌صورت پیش‌فرض &quot;IfNotPresent&quot; قرار می‌دهد، یا در صورتی که ایمیج‌های موردنیاز روی میزبان موجود نباشند، آن‌ها را دریافت می‌کند.</p>
</td>
</tr>
<tr><td><code>imagePullSerial</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>imagePullSerial</code> مشخص می‌کند که دریافت ایمیج‌ها توسط kubeadm باید به‌صورت ترتیبی انجام شود یا موازی.
مقدار پیش‌فرض: true</p>
</td>
</tr>
</tbody>
</table>

## `UpgradeDiffConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeDiffConfiguration}
    

**ظاهر شده در:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradeDiffConfiguration شامل فهرستی از گزینه‌های قابل پیکربندی است که مختص دستور <code>kubeadm upgrade diff</code> هستند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesVersion</code><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> نسخه هدف control plane است.</p>
</td>
</tr>
<tr><td><code>contextLines</code><br/>
<code>int</code>
</td>
<td>
   <p><code>diffContextLines</code> تعداد خطوط زمینه (context) در diff است.</p>
</td>
</tr>
</tbody>
</table>

## `UpgradeNodeConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradeNodeConfiguration}
    

**ظاهر شده در:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradeNodeConfiguration شامل فهرستی از گزینه‌های قابل پیکربندی است که مختص دستور &quot;kubeadm upgrade node&quot; هستند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>certificateRenewal</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>certificateRenewal</code> به kubeadm دستور می‌دهد در طول ارتقاها گواهی‌ها را تمدید کند.
مقدار پیش‌فرض: true.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> مشخص می‌کند که آیا حالت اجرای آزمایشی (dry run) فعال است یا خیر. در صورت فعال بودن، هیچ تغییری اعمال نمی‌شود و فقط کارهایی که انجام می‌شدند نمایش داده می‌شوند.</p>
</td>
</tr>
<tr><td><code>etcdUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>etcdUpgrade</code> به kubeadm دستور می‌دهد در طول ارتقاها، etcd را نیز ارتقا دهد.
مقدار پیش‌فرض: true.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> فهرستی از خطاهای pre-flight را فراهم می‌کند که در طول فرایند ارتقا نادیده گرفته می‌شوند،
مانند 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همه‌ی بررسی‌ها را نادیده می‌گیرد.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> فهرستی از فازهایی است که در طول اجرای دستور نادیده گرفته می‌شوند.
فهرست فازها را می‌توان با دستور <code>kubeadm upgrade node phase --help</code> به‌دست آورد.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta4-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> شامل گزینه‌های مربوط به اعمال patchها بر مؤلفه‌هایی است که kubeadm در طول <code>kubeadm upgrade</code> مستقر کرده است.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p><code>imagePullPolicy</code> سیاست دریافت ایمیج را در عملیات <code>kubeadm upgrade node</code> مشخص می‌کند.
مقدار این فیلد باید یکی از &quot;Always&quot;، &quot;IfNotPresent&quot; یا &quot;Never&quot; باشد.
اگر این فیلد تنظیم نشود، kubeadm مقدار آن را به‌صورت پیش‌فرض &quot;IfNotPresent&quot; قرار می‌دهد، یا در صورتی که ایمیج‌های موردنیاز روی میزبان موجود نباشند، آن‌ها را دریافت می‌کند.</p>
</td>
</tr>
<tr><td><code>imagePullSerial</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>imagePullSerial</code> مشخص می‌کند که دریافت ایمیج‌ها توسط kubeadm باید به‌صورت ترتیبی انجام شود یا موازی.
مقدار پیش‌فرض: true</p>
</td>
</tr>
</tbody>
</table>

## `UpgradePlanConfiguration`     {#kubeadm-k8s-io-v1beta4-UpgradePlanConfiguration}
    

**ظاهر شده در:**

- [UpgradeConfiguration](#kubeadm-k8s-io-v1beta4-UpgradeConfiguration)


<p>UpgradePlanConfiguration شامل فهرستی از گزینه‌های قابل پیکربندی است که مختص دستور &quot;kubeadm upgrade plan&quot; هستند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubernetesVersion</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>kubernetesVersion</code> نسخه هدف control plane است.</p>
</td>
</tr>
<tr><td><code>allowExperimentalUpgrades</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>allowExperimentalUpgrades</code> به kubeadm دستور می‌دهد نسخه‌های ناپایدار کوبرنتیز را به‌عنوان گزینه‌ی ارتقا نمایش دهد و امکان ارتقا به نسخه‌ی آلفا، بتا یا release candidate کوبرنتیز را فراهم می‌کند.
مقدار پیش‌فرض: false</p>
</td>
</tr>
<tr><td><code>allowRCUpgrades</code><br/>
<code>bool</code>
</td>
<td>
   <p>فعال‌کردن <code>allowRCUpgrades</code> باعث می‌شود نسخه‌های release candidate کوبرنتیز به‌عنوان گزینه‌ی ارتقا نمایش داده شوند و امکان ارتقا به یک نسخه‌ی release candidate کوبرنتیز فراهم شود.</p>
</td>
</tr>
<tr><td><code>dryRun</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>dryRun</code> مشخص می‌کند که آیا حالت اجرای آزمایشی (dry run) فعال است یا خیر. در صورت فعال بودن، هیچ تغییری اعمال نمی‌شود و فقط کارهایی که انجام می‌شدند نمایش داده می‌شوند.</p>
</td>
</tr>
<tr><td><code>etcdUpgrade</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>etcdUpgrade</code> به kubeadm دستور می‌دهد در طول ارتقاها، etcd را نیز ارتقا دهد.
مقدار پیش‌فرض: true.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>ignorePreflightErrors</code> فهرستی از خطاهای pre-flight را فراهم می‌کند که در طول فرایند ارتقا نادیده گرفته می‌شوند،
مانند 'IsPrivilegedUser,Swap'. مقدار 'all' خطاهای همه‌ی بررسی‌ها را نادیده می‌گیرد.</p>
</td>
</tr>
<tr><td><code>printConfig</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>printConfig</code> مشخص می‌کند که آیا فایل پیکربندی که در ارتقا استفاده خواهد شد باید چاپ شود یا خیر.</p>
</td>
</tr>
</tbody>
</table>
