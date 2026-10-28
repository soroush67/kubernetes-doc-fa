---
title: kubeadm Configuration (v1beta3)
content_type: tool-reference
package: kubeadm.k8s.io/v1beta3
auto_generated: true
---
<h2>Overview</h2>
<p>بسته v1beta3 نسخه v1beta3 از قالب فایل پیکربندی kubeadm را تعریف می‌کند.
این نسخه با رفع برخی مشکلات جزئی و افزودن چند فیلد جدید، قالب v1beta2 را بهبود می‌بخشد.</p>
<p>فهرست تغییرات نسبت به v1beta2:</p>
<ul>
<li>فیلد منسوخ‌شده &quot;ClusterConfiguration.useHyperKubeImage&quot; حذف شده است.
kubeadm دیگر از ایمیج hyperkube پشتیبانی نمی‌کند.</li>
<li>فیلد &quot;ClusterConfiguration.dns.type&quot; حذف شده است، زیرا CoreDNS تنها نوع سرور DNS است که kubeadm از آن پشتیبانی می‌کند.</li>
<li>تگ‌های &quot;datapolicy&quot; به فیلدهایی که اطلاعات محرمانه را نگه می‌دارند افزوده شده‌اند.
در نتیجه، هنگام چاپ ساختارهای API با klog، مقادیر این فیلدها حذف می‌شوند.</li>
<li>فیلدهای &quot;InitConfiguration.skipPhases&quot; و &quot;JoinConfiguration.skipPhases&quot; افزوده شده‌اند تا امکان رد کردن فهرستی از فازها در زمان اجرای دستور kubeadm init/join فراهم شود.</li>
<li>فیلدهای &quot;InitConfiguration.nodeRegistration.imagePullPolicy&quot; و &quot;JoinConfiguration.nodeRegistration.imagePullPolicy&quot;
افزوده شده‌اند تا بتوان سیاست دریافت ایمیج‌ها را در زمان اجرای &quot;init&quot; و &quot;join&quot; در kubeadm مشخص کرد.
مقدار آن باید یکی از &quot;Always&quot;، &quot;Never&quot; یا &quot;IfNotPresent&quot; باشد.
مقدار پیش‌فرض &quot;IfNotPresent&quot; است که رفتار موجود پیش از این افزوده شدن بوده است.</li>
<li>فیلدهای &quot;InitConfiguration.patches.directory&quot; و &quot;JoinConfiguration.patches.directory&quot; افزوده شده‌اند تا کاربر بتواند دایرکتوری‌ای را پیکربندی کند که پچ‌های مربوط به مؤلفه‌های مستقرشده توسط kubeadm از آن خوانده می‌شوند.</li>
<li>BootstrapToken* API و ابزارهای مرتبط با آن از گروه API با نام &quot;kubeadm&quot; به گروه جدیدی با نام &quot;bootstraptoken&quot; منتقل شده‌اند. نسخه v1beta3 از API مربوط به kubeadm دیگر ساختارهای BootstrapToken* را در بر نمی‌گیرد.</li>
</ul>
<p>مهاجرت از نسخه‌های قدیمی پیکربندی kubeadm</p>
<ul>
<li>kubeadm نسخه v1.15.x و جدیدتر را می‌توان برای مهاجرت از v1beta1 به v1beta2 به کار برد.</li>
<li>kubeadm نسخه v1.22.x و جدیدتر دیگر از v1beta1 و API های قدیمی‌تر پشتیبانی نمی‌کند، اما می‌توان از آن برای مهاجرت از v1beta2 به v1beta3 استفاده کرد.</li>
<li>kubeadm نسخه v1.27.x و جدیدتر دیگر از v1beta2 و API های قدیمی‌تر پشتیبانی نمی‌کند،</li>
</ul>
<h2>Basics</h2>
<p>روش توصیه‌شده برای پیکربندی kubeadm این است که یک فایل پیکربندی YAML با گزینه <code>--config</code> ارسال شود. برخی از
گزینه‌های پیکربندی تعریف‌شده در فایل پیکربندی kubeadm به‌صورت فلگ‌های خط فرمان نیز در دسترس هستند، اما در این روش
فقط رایج‌ترین و ساده‌ترین موارد استفاده پشتیبانی می‌شوند.</p>
<p>یک فایل پیکربندی kubeadm می‌تواند چندین نوع پیکربندی را در خود داشته باشد که با سه خط تیره (<code>---</code>) از یکدیگر جدا می‌شوند.</p>
<p>kubeadm از انواع پیکربندی زیر پشتیبانی می‌کند:</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ClusterConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>JoinConfiguration<span style="color:#bbb">
</span></pre><p>برای چاپ مقادیر پیش‌فرض اقدام‌های &quot;init&quot; و &quot;join&quot; از دستورات زیر استفاده کنید:</p>
<pre style="background-color:#fff">kubeadm config print init-defaults
kubeadm config print join-defaults
</pre><p>فهرست انواع پیکربندی که باید در یک فایل پیکربندی گنجانده شوند، به اقدامی که انجام می‌دهید
(<code>init</code> یا <code>join</code>) و به گزینه‌های پیکربندی که قصد استفاده از آن‌ها را دارید (مقادیر پیش‌فرض یا سفارشی‌سازی پیشرفته) بستگی دارد.</p>
<p>اگر برخی انواع پیکربندی ارائه نشوند یا فقط به‌صورت ناقص ارائه شوند، kubeadm از مقادیر پیش‌فرض استفاده می‌کند؛ مقادیر پیش‌فرضی که kubeadm فراهم می‌کند، در صورت نیاز شامل اعمال هماهنگی مقادیر میان مؤلفه‌ها نیز هستند (برای مثال
فلگ <code>--cluster-cidr</code> در controller manager و <code>clusterCIDR</code> در kube-proxy).</p>
<p>کاربران همیشه مجاز به بازنویسی مقادیر پیش‌فرض هستند، به‌جز زیرمجموعه کوچکی از تنظیمات که
از نظر امنیتی اهمیت دارند (برای مثال اعمال اجباری حالت مجوزدهی Node و RBAC در API server).</p>
<p>اگر کاربر نوع پیکربندی‌ای را ارائه کند که برای اقدام در حال انجام انتظار نمی‌رود، kubeadm
آن نوع‌ها را نادیده می‌گیرد و یک هشدار چاپ می‌کند.</p>
<h2>Kubeadm init configuration types</h2>
<p>هنگام اجرای kubeadm init با گزینه <code>--config</code>، انواع پیکربندی زیر قابل استفاده هستند:
InitConfiguration، ClusterConfiguration، KubeProxyConfiguration و KubeletConfiguration، اما تنها وجود یکی
از InitConfiguration و ClusterConfiguration الزامی است.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">bootstrapTokens</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">nodeRegistration</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span></pre><p>نوع InitConfiguration باید برای پیکربندی تنظیمات زمان اجرا استفاده شود که در مورد kubeadm init
شامل پیکربندی bootstrap token و تمام تنظیماتی است که مختص نودی هستند که kubeadm روی آن اجرا می‌شود، از جمله:</p>
<ul>
<li>
<p>NodeRegistration، که فیلدهای مرتبط با ثبت نود جدید در کلاستر را در بر دارد؛
از آن برای سفارشی‌سازی نام نود، سوکت CRI مورد استفاده یا هر تنظیم دیگری که باید فقط برای همین
نود اعمال شود (برای مثال آدرس IP نود) استفاده کنید.</p>
</li>
<li>
<p>LocalAPIEndpoint، که نشان‌دهنده endpoint نمونه API server است که باید روی این نود مستقر شود؛
برای مثال از آن برای سفارشی‌سازی آدرس advertise شده API server استفاده کنید.</p>
</li>
</ul>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
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
</span></pre><p>نوع ClusterConfiguration باید برای پیکربندی تنظیمات سراسری کلاستر استفاده شود،
از جمله تنظیمات مربوط به:</p>
<ul>
<li>
<p><code>networking</code> که پیکربندی توپولوژی شبکه کلاستر را در بر دارد؛ برای مثال از آن برای سفارشی‌سازی
زیرشبکه Pod یا زیرشبکه سرویس‌ها استفاده کنید.</p>
</li>
<li>
<p><code>etcd</code>: برای مثال از آن برای سفارشی‌سازی etcd محلی یا پیکربندی API server
جهت استفاده از یک کلاستر etcd خارجی استفاده کنید.</p>
</li>
<li>
<p>پیکربندی‌های kube-apiserver، kube-scheduler و kube-controller-manager؛ از آن‌ها برای سفارشی‌سازی مؤلفه‌های control plane
با افزودن تنظیمات سفارشی یا بازنویسی تنظیمات پیش‌فرض kubeadm استفاده کنید.</p>
</li>
</ul>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span></pre><p>نوع KubeProxyConfiguration باید برای تغییر پیکربندی‌ای استفاده شود که به نمونه‌های kube-proxy مستقرشده در کلاستر ارسال می‌شود.
اگر این آبجکت ارائه نشود یا فقط به‌صورت ناقص ارائه شود، kubeadm مقادیر پیش‌فرض را اعمال می‌کند.</p>
<p>برای مستندات رسمی kube-proxy به https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ یا
https://pkg.go.dev/k8s.io/kube-proxy/config/v1alpha1#KubeProxyConfiguration
مراجعه کنید.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span></pre><p>نوع KubeletConfiguration باید برای تغییر پیکربندی‌هایی استفاده شود که به تمام نمونه‌های kubelet مستقرشده در کلاستر ارسال می‌شوند.
اگر این آبجکت ارائه نشود یا فقط به‌صورت ناقص ارائه شود، kubeadm مقادیر پیش‌فرض را اعمال می‌کند.</p>
<p>برای مستندات رسمی kubelet به https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/ یا
https://pkg.go.dev/k8s.io/kubelet/config/v1beta1#KubeletConfiguration
مراجعه کنید.</p>
<p>در ادامه یک نمونه کاملاً تکمیل‌شده از یک فایل YAML واحد آمده است که شامل چندین
نوع پیکربندی است و می‌توان آن را در اجرای <code>kubeadm init</code> به کار برد.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>InitConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">bootstrapTokens</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- <span style="color:#000;font-weight:bold">token</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;9a08jv.c0izixklcxtmnze7&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">description</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;kubeadm bootstrap token&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">ttl</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;24h&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span>- <span style="color:#000;font-weight:bold">token</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;783bde.3f89s0fje9f38fhf&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">description</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;another bootstrap token&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">usages</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- authentication<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- signing<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">groups</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- system:bootstrappers:kubeadm:default-node-token<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">nodeRegistration</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;ec2-10-100-0-1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">criSocket</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/var/run/dockershim.sock&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">taints</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">key</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;kubeadmNode&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">value</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;someValue&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">effect</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;NoSchedule&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">kubeletExtraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">v</span>:<span style="color:#bbb"> </span><span style="color:#099">4</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">ignorePreflightErrors</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- IsPrivilegedUser<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">imagePullPolicy</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;IfNotPresent&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">localAPIEndpoint</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">advertiseAddress</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.100.0.1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">bindPort</span>:<span style="color:#bbb"> </span><span style="color:#099">6443</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">certificateKey</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;e6a2eb8581237ab72a4f494f30285ec12a9694d750b9785706a83bfcbbbd2204&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">skipPhases</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span>- addon/kube-proxy<span style="color:#bbb">
</span><span style="color:#bbb"></span>---<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>ClusterConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">etcd</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic"># one of local or external</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">local</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">imageRepository</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;registry.k8s.io&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">imageTag</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;3.2.24&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">dataDir</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/var/lib/etcd&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">listen-client-urls</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;http://10.100.0.1:2379&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">serverCertSANs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- <span style="color:#bbb"> </span><span style="color:#d14">&#34;ec2-10-100-0-1.compute-1.amazonaws.com&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">peerCertSANs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">      </span>- <span style="color:#d14">&#34;10.100.0.1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#998;font-style:italic"># external:</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#998;font-style:italic"># endpoints:</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#998;font-style:italic"># - &#34;10.100.0.1:2379&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#998;font-style:italic"># - &#34;10.100.0.2:2379&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#998;font-style:italic"># caFile: &#34;/etcd/kubernetes/pki/etcd/etcd-ca.crt&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#998;font-style:italic"># certFile: &#34;/etcd/kubernetes/pki/etcd/etcd.crt&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#998;font-style:italic"># keyFile: &#34;/etcd/kubernetes/pki/etcd/etcd.key&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">networking</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">serviceSubnet</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.96.0.0/16&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">podSubnet</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.244.0.0/24&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">dnsDomain</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;cluster.local&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kubernetesVersion</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;v1.21.0&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">controlPlaneEndpoint</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.100.0.1:6443&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiServer</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">authorization-mode</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;Node,RBAC&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;some-volume&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">hostPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">mountPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-pod-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">readOnly</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">false</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">pathType</span>:<span style="color:#bbb"> </span>File<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">certSANs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#d14">&#34;10.100.1.1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#d14">&#34;ec2-10-100-0-1.compute-1.amazonaws.com&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">timeoutForControlPlane</span>:<span style="color:#bbb"> </span>4m0s<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">controllerManager</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">&#34;node-cidr-mask-size&#34;: </span><span style="color:#d14">&#34;20&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;some-volume&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">hostPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">mountPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-pod-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">readOnly</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">false</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">pathType</span>:<span style="color:#bbb"> </span>File<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">scheduler</span>:<span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraArgs</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span><span style="color:#000;font-weight:bold">bind-address</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;10.100.0.1&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">  </span><span style="color:#000;font-weight:bold">extraVolumes</span>:<span style="color:#bbb">
</span><span style="color:#bbb">    </span>- <span style="color:#000;font-weight:bold">name</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;some-volume&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">hostPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">mountPath</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/some-pod-path&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">readOnly</span>:<span style="color:#bbb"> </span><span style="color:#000;font-weight:bold">false</span><span style="color:#bbb">
</span><span style="color:#bbb">      </span><span style="color:#000;font-weight:bold">pathType</span>:<span style="color:#bbb"> </span>File<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">certificatesDir</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;/etc/kubernetes/pki&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">imageRepository</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;registry.k8s.io&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">clusterName</span>:<span style="color:#bbb"> </span><span style="color:#d14">&#34;example-cluster&#34;</span><span style="color:#bbb">
</span><span style="color:#bbb"></span>---<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubelet.config.k8s.io/v1beta1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeletConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#998;font-style:italic"># kubelet specific options here</span><span style="color:#bbb">
</span><span style="color:#bbb"></span>---<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeproxy.config.k8s.io/v1alpha1<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>KubeProxyConfiguration<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#998;font-style:italic"># kube-proxy specific options here</span><span style="color:#bbb">
</span></pre><h2>Kubeadm join configuration types</h2>
<p>هنگام اجرای <code>kubeadm join</code> با گزینه <code>--config</code>، باید نوع JoinConfiguration ارائه شود.</p>
<pre style="background-color:#fff"><span style="color:#000;font-weight:bold">apiVersion</span>:<span style="color:#bbb"> </span>kubeadm.k8s.io/v1beta3<span style="color:#bbb">
</span><span style="color:#bbb"></span><span style="color:#000;font-weight:bold">kind</span>:<span style="color:#bbb"> </span>JoinConfiguration<span style="color:#bbb">
</span><span style="color:#bbb">  </span>...<span style="color:#bbb">
</span></pre><p>نوع JoinConfiguration باید برای پیکربندی تنظیمات زمان اجرا استفاده شود که در مورد <code>kubeadm join</code>
شامل روش discovery مورد استفاده برای دسترسی به اطلاعات کلاستر و تمام تنظیماتی است که مختص نودی هستند
که kubeadm روی آن اجرا می‌شود، از جمله:</p>
<ul>
<li>
<p><code>nodeRegistration</code>، که فیلدهای مرتبط با ثبت نود جدید در کلاستر را در بر دارد؛
از آن برای سفارشی‌سازی نام نود، سوکت CRI مورد استفاده یا هر تنظیم دیگری که باید فقط برای همین
نود اعمال شود (برای مثال آدرس IP نود) استفاده کنید.</p>
</li>
<li>
<p><code>apiEndpoint</code>، که نشان‌دهنده endpoint نمونه API server است که در نهایت باید روی این نود مستقر شود.</p>
</li>
</ul>
<p>منسوخ‌شده: v1beta3 به نفع v1beta4 منسوخ شده است و در یک نسخه آینده،
1.34 یا بعد از آن، حذف خواهد شد. لطفاً مهاجرت کنید</p>

## انواع منابع (Resource Types)


- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)
- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)
- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)
  
    
    

## `BootstrapToken`     {#BootstrapToken}
    

**در این بخش‌ها ظاهر می‌شود:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)


<p>BootstrapToken یک توکن بوت‌استرپ را توصیف می‌کند که به‌صورت یک Secret در کلاستر ذخیره می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>token</code> <B>[الزامی]</B><br/>
<a href="#BootstrapTokenString"><code>BootstrapTokenString</code></a>
</td>
<td>
   <p><code>token</code> برای برقراری اعتماد دوطرفه بین نودها و control planeها استفاده می‌شود.
از این توکن برای پیوستن نودها به کلاستر استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>description</code><br/>
<code>string</code>
</td>
<td>
   <p><code>description</code> یک پیام خوانا برای انسان تعیین می‌کند که توضیح می‌دهد این توکن چرا وجود دارد و برای چه
مقصودی استفاده می‌شود، تا سایر مدیران بتوانند هدف آن را بدانند.</p>
</td>
</tr>
<tr><td><code>ttl</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>ttl</code> مدت زمان بقای (time to live) این توکن را تعیین می‌کند. مقدار پیش‌فرض آن <code>24h</code> است.
فیلدهای <code>expires</code> و <code>ttl</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تعیین کرد.</p>
</td>
</tr>
<tr><td><code>expires</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#time-v1-meta"><code>meta/v1.Time</code></a>
</td>
<td>
   <p><code>expires</code> زمان انقضای این توکن را مشخص می‌کند. به‌طور پیش‌فرض، مقدار آن در زمان اجرا
و بر اساس <code>ttl</code> به‌صورت پویا تعیین می‌شود. فیلدهای <code>expires</code> و <code>ttl</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تعیین کرد.</p>
</td>
</tr>
<tr><td><code>usages</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>usages</code> روش‌هایی را که می‌توان از این توکن استفاده کرد توصیف می‌کند. به‌طور پیش‌فرض می‌توان از آن
برای برقراری اعتماد دوطرفه استفاده کرد، اما می‌توان این رفتار را در اینجا تغییر داد.</p>
</td>
</tr>
<tr><td><code>groups</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>groups</code> گروه‌های اضافی را مشخص می‌کند که در صورت استفاده از این توکن برای احراز هویت،
این توکن با آن گروه‌ها احراز هویت خواهد شد.</p>
</td>
</tr>
</tbody>
</table>

## `BootstrapTokenString`     {#BootstrapTokenString}
    

**در این بخش‌ها ظاهر می‌شود:**

- [BootstrapToken](#BootstrapToken)


<p>BootstrapTokenString توکنی با قالب <code>abcdef.abcdef0123456789</code> است که هم برای اعتبارسنجی در دسترس‌بودن عملی
API server از دیدگاه نودِ در حال پیوستن، و هم به‌عنوان روش احراز هویت نود در مرحله بوت‌استرپ
دستور &quot;kubeadm join&quot; استفاده می‌شود. این توکن کوتاه‌مدت است و باید کوتاه‌مدت باشد.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>-</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>-</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
</tbody>
</table>
  

## `ClusterConfiguration`     {#kubeadm-k8s-io-v1beta3-ClusterConfiguration}
    


<p>ClusterConfiguration شامل پیکربندی سراسری کلاستر برای یک کلاستر kubeadm است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta3</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>ClusterConfiguration</code></td></tr>
    
  
<tr><td><code>etcd</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Etcd"><code>Etcd</code></a>
</td>
<td>
   <p><code>etcd</code> پیکربندی etcd را در بر دارد.</p>
</td>
</tr>
<tr><td><code>networking</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Networking"><code>Networking</code></a>
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
   <p><code>controlPlaneEndpoint</code> یک آدرس IP یا نام DNS پایدار برای control plane تعیین می‌کند.
مقدار آن می‌تواند یک آدرس IP معتبر یا یک زیردامنه DNS مطابق RFC-1123 باشد که هر دو می‌توانند یک پورت TCP اختیاری داشته باشند.
اگر <code>controlPlaneEndpoint</code> مشخص نشده باشد، از <code>advertiseAddress</code> + <code>bindPort</code>
استفاده می‌شود؛ اگر <code>controlPlaneEndpoint</code> بدون پورت TCP مشخص شده باشد،
از <code>bindPort</code> استفاده می‌شود.
کاربردهای ممکن عبارت‌اند از:</p>
<ul>
<li>در یک کلاستر با بیش از یک نمونه control plane، آدرس
load balancer خارجیِ مستقر در جلوی نمونه‌های control plane
باید به این فیلد اختصاص داده شود.</li>
<li>در محیط‌هایی که بازیافت اجباری نودها اعمال می‌شود، می‌توان از <code>controlPlaneEndpoint</code>
برای اختصاص یک DNS پایدار به control plane استفاده کرد.</li>
</ul>
</td>
</tr>
<tr><td><code>apiServer</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-APIServer"><code>APIServer</code></a>
</td>
<td>
   <p><code>apiServer</code> شامل تنظیمات اضافی برای API server است.</p>
</td>
</tr>
<tr><td><code>controllerManager</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>controllerManager</code> شامل تنظیمات اضافی برای controller manager است.</p>
</td>
</tr>
<tr><td><code>scheduler</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>
   <p><code>scheduler</code> شامل تنظیمات اضافی برای زمان‌بند (scheduler) است.</p>
</td>
</tr>
<tr><td><code>dns</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-DNS"><code>DNS</code></a>
</td>
<td>
   <p><code>dns</code> گزینه‌های افزونه DNS نصب‌شده در کلاستر را تعریف می‌کند.</p>
</td>
</tr>
<tr><td><code>certificatesDir</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificatesDir</code> مشخص می‌کند که همه گواهی‌های موردنیاز در کجا ذخیره می‌شوند یا از کجا جست‌وجو می‌شوند.</p>
</td>
</tr>
<tr><td><code>imageRepository</code><br/>
<code>string</code>
</td>
<td>
   <p><code>imageRepository</code> رجیستری کانتینری را که ایمیج‌ها از آن دریافت می‌شوند تعیین می‌کند.
اگر خالی باشد، به‌طور پیش‌فرض از <code>registry.k8s.io</code> استفاده می‌شود.
اگر نسخه کوبرنتیز یک بیلد CI باشد (نسخه کوبرنتیز با <code>ci/</code> شروع شود)،
<code>gcr.io/k8s-staging-ci-images</code> به‌طور پیش‌فرض برای مؤلفه‌های control plane
و برای kube-proxy استفاده می‌شود، در حالی که <code>registry.k8s.io</code> برای سایر ایمیج‌ها استفاده خواهد شد.</p>
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
این نام در فایل‌های kubeconfig تولیدشده توسط kubeadm استفاده می‌شود و همچنین به‌عنوان مقدار
فلگ <code>--cluster-name</code> در kube-controller-manager ارسال می‌شود.
مقدار پیش‌فرض آن <code>&quot;kubernetes&quot;</code> است.</p>
</td>
</tr>
</tbody>
</table>

## `InitConfiguration`     {#kubeadm-k8s-io-v1beta3-InitConfiguration}
    


<p>InitConfiguration شامل فهرستی از عناصر است که اطلاعات زمان اجرای مختص &quot;kubeadm init&quot; را در بر دارند.
اطلاعات مختص <code>kubeadm init</code>. این فیلدها فقط در اولین اجرای <code>kubeadm init</code> استفاده می‌شوند.
پس از آن، اطلاعات این فیلدها در ConfigMap با نام <code>kubeadm-config</code> بارگذاری نمی‌شود؛
ConfigMap ای که برای نمونه توسط <code>kubeadm upgrade</code> استفاده می‌شود. این فیلدها باید omitempty باشند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta3</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>InitConfiguration</code></td></tr>
    
  
<tr><td><code>bootstrapTokens</code><br/>
<a href="#BootstrapToken"><code>[]BootstrapToken</code></a>
</td>
<td>
   <p><code>bootstrapTokens</code> در زمان اجرای <code>kubeadm init</code> در نظر گرفته می‌شود و مجموعه‌ای از Bootstrap Tokenها را برای ایجاد توصیف می‌کند.
این اطلاعات در configmap کلاستر kubeadm بارگذاری نمی‌شود، که بخشی از دلیل آن ماهیت حساس این اطلاعات است.</p>
</td>
</tr>
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> شامل فیلدهایی است که به ثبت نود control plane جدید
در کلاستر مربوط می‌شوند.</p>
</td>
</tr>
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p><code>localAPIEndpoint</code> نشانی endpoint نمونه API server را نشان می‌دهد که روی این نود
control plane مستقر شده است. در برپایی‌های HA، این فیلد با <code>ClusterConfiguration.controlPlaneEndpoint</code>
از این جهت تفاوت دارد که <code>controlPlaneEndpoint</code> endpoint سراسری کلاستر است که سپس
درخواست‌ها را میان API serverهای مجزا توزیع بار (load-balance) می‌کند.
این آبجکت پیکربندی به شما امکان می‌دهد تعیین کنید API server محلی چه IP/نام DNS و پورتی را
به‌عنوان نشانی دسترسی به خود اعلام کند. به‌طور پیش‌فرض، kubeadm تلاش می‌کند IP رابط پیش‌فرض
را به‌صورت خودکار تشخیص دهد و از آن استفاده کند، اما اگر این فرایند ناموفق بود، می‌توانید مقدار موردنظر را در اینجا تعیین کنید.</p>
</td>
</tr>
<tr><td><code>certificateKey</code><br/>
<code>string</code>
</td>
<td>
   <p><code>certificateKey</code> کلیدی را تعیین می‌کند که گواهی‌ها و کلیدها پیش از بارگذاری در یک Secret در کلاستر
در طول فاز <code>uploadcerts init</code> با آن رمزگذاری می‌شوند.
کلید گواهی یک رشته با کدگذاری هگزادسیمال است که یک کلید AES با اندازه ۳۲ بایت است.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> فهرستی از فازهاست که در طول اجرای دستور نادیده گرفته می‌شوند.
فهرست فازها را می‌توان با دستور <code>kubeadm init --help</code> به دست آورد.
فلگ &quot;--skip-phases&quot; بر این فیلد اولویت دارد.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> شامل گزینه‌های مربوط به اعمال پچ‌ها بر مؤلفه‌هایی است که kubeadm در طول
<code>kubeadm init</code> مستقر می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `JoinConfiguration`     {#kubeadm-k8s-io-v1beta3-JoinConfiguration}
    


<p>JoinConfiguration شامل عناصری است که یک نود مشخص را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
<tr><td><code>apiVersion</code><br/>string</td><td><code>kubeadm.k8s.io/v1beta3</code></td></tr>
<tr><td><code>kind</code><br/>string</td><td><code>JoinConfiguration</code></td></tr>
    
  
<tr><td><code>nodeRegistration</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions"><code>NodeRegistrationOptions</code></a>
</td>
<td>
   <p><code>nodeRegistration</code> شامل فیلدهایی است که به ثبت نود
control plane جدید در کلاستر مربوط می‌شوند.</p>
</td>
</tr>
<tr><td><code>caCertPath</code><br/>
<code>string</code>
</td>
<td>
   <p><code>caCertPath</code> مسیر مرجع صدور گواهی SSL است که برای ایمن‌سازی
ارتباطات بین یک نود و control plane استفاده می‌شود.
مقدار پیش‌فرض آن &quot;/etc/kubernetes/pki/ca.crt&quot; است.</p>
</td>
</tr>
<tr><td><code>discovery</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-Discovery"><code>Discovery</code></a>
</td>
<td>
   <p><code>discovery</code> گزینه‌هایی را مشخص می‌کند که kubelet در طول فرایند بوت‌استرپ TLS
از آن‌ها استفاده می‌کند.</p>
</td>
</tr>
<tr><td><code>controlPlane</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-JoinControlPlane"><code>JoinControlPlane</code></a>
</td>
<td>
   <p><code>controlPlane</code> نمونه control plane اضافی را تعریف می‌کند که باید روی نود در حال پیوستن مستقر شود.
اگر nil باشد، هیچ نمونه control plane اضافی مستقر نخواهد شد.</p>
</td>
</tr>
<tr><td><code>skipPhases</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>skipPhases</code> فهرستی از فازهاست که در طول اجرای دستور نادیده گرفته می‌شوند.
فهرست فازها را می‌توان با دستور <code>kubeadm join --help</code> به دست آورد.
فلگ <code>--skip-phases</code> بر این فیلد اولویت دارد.</p>
</td>
</tr>
<tr><td><code>patches</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-Patches"><code>Patches</code></a>
</td>
<td>
   <p><code>patches</code> شامل گزینه‌های مربوط به اعمال پچ‌ها بر مؤلفه‌هایی است که
kubeadm در طول <code>kubeadm join</code> مستقر می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `APIEndpoint`     {#kubeadm-k8s-io-v1beta3-APIEndpoint}
    

**در این بخش‌ها ظاهر می‌شود:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [JoinControlPlane](#kubeadm-k8s-io-v1beta3-JoinControlPlane)


<p>ساختار APIEndpoint شامل عناصر نمونه API server است که روی یک نود مستقر شده است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>advertiseAddress</code><br/>
<code>string</code>
</td>
<td>
   <p><code>advertiseAddress</code> آدرس IP را تعیین می‌کند که API server آن را اعلام (advertise) می‌کند.</p>
</td>
</tr>
<tr><td><code>bindPort</code><br/>
<code>int32</code>
</td>
<td>
   <p><code>bindPort</code> پورت امنی را تعیین می‌کند که API Server به آن متصل (bind) می‌شود.
مقدار پیش‌فرض آن 6443 است.</p>
</td>
</tr>
</tbody>
</table>

## `APIServer`     {#kubeadm-k8s-io-v1beta3-APIServer}
    

**در این بخش‌ها ظاهر می‌شود:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>APIServer شامل تنظیمات لازم برای استقرار API server در کلاستر است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ControlPlaneComponent</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-ControlPlaneComponent"><code>ControlPlaneComponent</code></a>
</td>
<td>(اعضای <code>ControlPlaneComponent</code> در این نوع تعبیه شده‌اند.)
   <span class="text-muted">توضیحی ارائه نشده است.</span></td>
</tr>
<tr><td><code>certSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>certSANs</code> نام‌های جایگزین موضوع (Subject Alternative Names یا SANs) اضافی را برای
گواهی امضای API Server تعیین می‌کند.</p>
</td>
</tr>
<tr><td><code>timeoutForControlPlane</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p><code>timeoutForControlPlane</code> مهلت انتظار برای ظاهر شدن API server را کنترل می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `BootstrapTokenDiscovery`     {#kubeadm-k8s-io-v1beta3-BootstrapTokenDiscovery}
    

**در این بخش‌ها ظاهر می‌شود:**

- [Discovery](#kubeadm-k8s-io-v1beta3-Discovery)


<p>BootstrapTokenDiscovery برای تعیین گزینه‌های کشف (discovery) مبتنی بر bootstrap token استفاده می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>token</code> <B>[الزامی]</B><br/>
<code>string</code>
</td>
<td>
   <p><code>token</code> توکنی است که برای اعتبارسنجی اطلاعات کلاستر دریافت‌شده از
control plane استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>apiServerEndpoint</code><br/>
<code>string</code>
</td>
<td>
   <p><code>apiServerEndpoint</code> یک IP یا نام دامنه برای API server است که اطلاعات
از آن دریافت خواهد شد.</p>
</td>
</tr>
<tr><td><code>caCertHashes</code><br/>
<code>[]string</code>
</td>
<td>
   <p><code>caCertHashes</code> مجموعه‌ای از pinهای کلید عمومی را مشخص می‌کند که در صورت استفاده از کشف مبتنی بر توکن
باید راستی‌آزمایی شوند. CA ریشه‌ای که در طول کشف یافت می‌شود باید با یکی از این مقادیر مطابقت داشته باشد.
تعیین یک مجموعه خالی، pin کردن CA ریشه را غیرفعال می‌کند که می‌تواند ناامن باشد.
هر هش به‌صورت <code>&lt;type&gt;:&lt;value&gt;</code> مشخص می‌شود که تنها نوع پشتیبانی‌شده فعلی
&quot;sha256&quot; است. این مقدار یک هش SHA-256 با کدگذاری هگزادسیمال از آبجکت Subject Public Key Info (SPKI)
در قالب ASN.1 با کدگذاری DER است. این هش‌ها را می‌توان برای مثال با OpenSSL محاسبه کرد.</p>
</td>
</tr>
<tr><td><code>unsafeSkipCAVerification</code><br/>
<code>bool</code>
</td>
<td>
   <p><code>unsafeSkipCAVerification</code> کشف مبتنی بر توکن را بدون راستی‌آزمایی CA
از طریق <code>caCertHashes</code> مجاز می‌کند. این کار می‌تواند امنیت kubeadm را تضعیف کند، زیرا سایر نودها می‌توانند
خود را به‌جای control plane جا بزنند.</p>
</td>
</tr>
</tbody>
</table>

## `ControlPlaneComponent`     {#kubeadm-k8s-io-v1beta3-ControlPlaneComponent}
    

**در این بخش‌ها ظاهر می‌شود:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)

- [APIServer](#kubeadm-k8s-io-v1beta3-APIServer)


<p>ControlPlaneComponent شامل تنظیمات مشترک مؤلفه‌های control plane کلاستر است.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>extraArgs</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p><code>extraArgs</code> مجموعه‌ای از فلگ‌های اضافی است که به مؤلفه control plane ارسال می‌شود.
کلید در این map نام فلگ است، همان‌گونه که در خط فرمان ظاهر می‌شود، اما
بدون خط تیره(های) ابتدایی.</p>
</td>
</tr>
<tr><td><code>extraVolumes</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-HostPathMount"><code>[]HostPathMount</code></a>
</td>
<td>
   <p><code>extraVolumes</code> مجموعه‌ای از حجم‌های (volume) اضافی میزبان است که روی مؤلفه control plane مونت می‌شوند.</p>
</td>
</tr>
</tbody>
</table>

## `DNS`     {#kubeadm-k8s-io-v1beta3-DNS}
    

**در این بخش‌ها ظاهر می‌شود:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>DNS افزونه DNS را تعریف می‌کند که باید در کلاستر استفاده شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[الزامی]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(اعضای <code>ImageMeta</code> در این نوع تعبیه شده‌اند.)
   <p><code>imageMeta</code> امکان سفارشی‌سازی ایمیج مورد استفاده برای مؤلفه DNS را فراهم می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `Discovery`     {#kubeadm-k8s-io-v1beta3-Discovery}
    

**نمایش داده می‌شود در:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>Discovery گزینه‌هایی را مشخص می‌کند که kubelet در طول فرایند TLS Bootstrap از آن‌ها استفاده می‌کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>bootstrapToken</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-BootstrapTokenDiscovery"><code>BootstrapTokenDiscovery</code></a>
</td>
<td>
   <p>فیلد <code>bootstrapToken</code> برای تنظیم گزینه‌های discovery مبتنی بر bootstrap token به کار می‌رود.
فیلدهای <code>bootstrapToken</code> و <code>file</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تنظیم کرد.</p>
</td>
</tr>
<tr><td><code>file</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-FileDiscovery"><code>FileDiscovery</code></a>
</td>
<td>
   <p>فیلد <code>file</code> برای مشخص کردن یک فایل یا یک URL به فایل kubeconfig به کار می‌رود که اطلاعات
کلاستر از آن بارگذاری می‌شود.
فیلدهای <code>bootstrapToken</code> و <code>file</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تنظیم کرد.</p>
</td>
</tr>
<tr><td><code>tlsBootstrapToken</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>tlsBootstrapToken</code> توکنی است که برای TLS bootstrapping استفاده می‌شود.
اگر <code>bootstrapToken</code> تنظیم شده باشد، مقدار پیش‌فرض این فیلد <code>.bootstrapToken.token</code> است، اما
می‌توان آن را بازنویسی کرد. اگر <code>file</code> تنظیم شده باشد و KubeConfigFile
حاوی هیچ اطلاعات احراز هویت دیگری نباشد، این فیلد <strong>باید تنظیم شود</strong>.</p>
</td>
</tr>
<tr><td><code>timeout</code><br/>
<a href="https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration"><code>meta/v1.Duration</code></a>
</td>
<td>
   <p>فیلد <code>timeout</code> مهلت زمانی discovery را تغییر می‌دهد.</p>
</td>
</tr>
</tbody>
</table>

## `Etcd`     {#kubeadm-k8s-io-v1beta3-Etcd}
    

**نمایش داده می‌شود در:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>Etcd شامل عناصری است که پیکربندی Etcd را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>local</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-LocalEtcd"><code>LocalEtcd</code></a>
</td>
<td>
   <p>فیلد <code>local</code> گزینه‌های پیکربندی نمونه etcd محلی را فراهم می‌کند.
فیلدهای <code>local</code> و <code>external</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تنظیم کرد.</p>
</td>
</tr>
<tr><td><code>external</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-ExternalEtcd"><code>ExternalEtcd</code></a>
</td>
<td>
   <p>فیلد <code>external</code> نحوه اتصال به یک کلاستر etcd خارجی را توصیف می‌کند.
فیلدهای <code>local</code> و <code>external</code> متقابلاً ناسازگارند و نمی‌توان هر دو را همزمان تنظیم کرد.</p>
</td>
</tr>
</tbody>
</table>

## `ExternalEtcd`     {#kubeadm-k8s-io-v1beta3-ExternalEtcd}
    

**نمایش داده می‌شود در:**

- [Etcd](#kubeadm-k8s-io-v1beta3-Etcd)


<p>ExternalEtcd یک کلاستر etcd خارجی را توصیف می‌کند.
kubeadm هیچ اطلاعی از محل قرارگیری فایل‌های گواهی ندارد و این فایل‌ها باید فراهم شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>endpoints</code> <B>[Required]</B><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>endpoints</code> شامل فهرست اعضای etcd است.</p>
</td>
</tr>
<tr><td><code>caFile</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>caFile</code> یک فایل SSL Certificate Authority (CA) است که برای ایمن‌سازی ارتباط etcd استفاده می‌شود.
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

## `FileDiscovery`     {#kubeadm-k8s-io-v1beta3-FileDiscovery}
    

**نمایش داده می‌شود در:**

- [Discovery](#kubeadm-k8s-io-v1beta3-Discovery)


<p>FileDiscovery برای مشخص کردن یک فایل یا یک URL به فایل kubeconfig به کار می‌رود که اطلاعات
کلاستر از آن بارگذاری می‌شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>kubeConfigPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>kubeConfigPath</code> برای مشخص کردن مسیر واقعی فایل یا URL فایل kubeconfig به کار می‌رود
که اطلاعات کلاستر از آن بارگذاری می‌شود.</p>
</td>
</tr>
</tbody>
</table>

## `HostPathMount`     {#kubeadm-k8s-io-v1beta3-HostPathMount}
    

**نمایش داده می‌شود در:**

- [ControlPlaneComponent](#kubeadm-k8s-io-v1beta3-ControlPlaneComponent)


<p>HostPathMount شامل عناصری است که حجم‌هایی (volumes) را توصیف می‌کنند که از میزبان mount می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>name</code> نام حجم (volume) درون قالب Pod است.</p>
</td>
</tr>
<tr><td><code>hostPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>hostPath</code> مسیری در میزبان است که درون Pod mount خواهد شد.</p>
</td>
</tr>
<tr><td><code>mountPath</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>mountPath</code> مسیری درون Pod است که <code>hostPath</code> در آن mount خواهد شد.</p>
</td>
</tr>
<tr><td><code>readOnly</code><br/>
<code>bool</code>
</td>
<td>
   <p>فیلد <code>readOnly</code> دسترسی نوشتن به حجم (volume) را کنترل می‌کند.</p>
</td>
</tr>
<tr><td><code>pathType</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#hostpathtype-v1-core"><code>core/v1.HostPathType</code></a>
</td>
<td>
   <p>فیلد <code>pathType</code> نوع <code>hostPath</code> است.</p>
</td>
</tr>
</tbody>
</table>

## `ImageMeta`     {#kubeadm-k8s-io-v1beta3-ImageMeta}
    

**نمایش داده می‌شود در:**

- [DNS](#kubeadm-k8s-io-v1beta3-DNS)

- [LocalEtcd](#kubeadm-k8s-io-v1beta3-LocalEtcd)


<p>ImageMeta امکان سفارشی‌سازی ایمیج مورد استفاده برای مؤلفه‌هایی را فراهم می‌کند که
از فرایند انتشار Kubernetes/Kubernetes منشأ نگرفته‌اند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>imageRepository</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>imageRepository</code> رجیستری کانتینری را تعیین می‌کند که ایمیج‌ها از آن دریافت (pull) می‌شوند.
اگر تنظیم نشود، به‌جای آن از <code>imageRepository</code> تعریف‌شده در ClusterConfiguration استفاده خواهد شد.</p>
</td>
</tr>
<tr><td><code>imageTag</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>imageTag</code> امکان تعیین یک تگ برای ایمیج را فراهم می‌کند.
در صورت تنظیم این مقدار، kubeadm هنگام ارتقا نسخه مؤلفه‌های یادشده را
به‌طور خودکار تغییر نمی‌دهد.</p>
</td>
</tr>
</tbody>
</table>

## `JoinControlPlane`     {#kubeadm-k8s-io-v1beta3-JoinControlPlane}
    

**نمایش داده می‌شود در:**

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>JoinControlPlane شامل عناصری است که یک نمونه control plane اضافی را توصیف می‌کنند
که باید روی نود در حال پیوستن مستقر شود.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>localAPIEndpoint</code><br/>
<a href="#kubeadm-k8s-io-v1beta3-APIEndpoint"><code>APIEndpoint</code></a>
</td>
<td>
   <p>فیلد <code>localAPIEndpoint</code> نقطه انتهایی (endpoint) نمونه API server را نشان می‌دهد که باید
روی این نود مستقر شود.</p>
</td>
</tr>
<tr><td><code>certificateKey</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>certificateKey</code> کلیدی است که برای رمزگشایی گواهی‌ها پس از
دریافت آن‌ها از secret هنگام پیوستن یک نود control plane جدید استفاده می‌شود.
کلید رمزنگاری متناظر در InitConfiguration قرار دارد.
کلید گواهی یک رشته با کدگذاری هگزادسیمال است که یک کلید AES با اندازه ۳۲ بایت است.</p>
</td>
</tr>
</tbody>
</table>

## `LocalEtcd`     {#kubeadm-k8s-io-v1beta3-LocalEtcd}
    

**نمایش داده می‌شود در:**

- [Etcd](#kubeadm-k8s-io-v1beta3-Etcd)


<p>LocalEtcd مشخص می‌کند که kubeadm باید یک کلاستر etcd را به‌صورت محلی اجرا کند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>ImageMeta</code> <B>[Required]</B><br/>
<a href="#kubeadm-k8s-io-v1beta3-ImageMeta"><code>ImageMeta</code></a>
</td>
<td>(اعضای <code>ImageMeta</code> در این نوع تعبیه شده‌اند.)
   <p>ImageMeta امکان سفارشی‌سازی ایمیج کانتینر مورد استفاده برای etcd را فراهم می‌کند.
مشخص کردن یک ایمیج سفارشی etcd به <code>kubeadm upgrade</code> اعلام می‌کند که این ایمیج توسط کاربر مدیریت می‌شود
و ارتقای آن باید نادیده گرفته شود.</p>
</td>
</tr>
<tr><td><code>dataDir</code> <B>[Required]</B><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>dataDir</code> دایرکتوری‌ای است که etcd داده‌های خود را در آن قرار می‌دهد.
مقدار پیش‌فرض آن &quot;/var/lib/etcd&quot; است.</p>
</td>
</tr>
<tr><td><code>extraArgs</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>فیلد <code>extraArgs</code> آرگومان‌های اضافی است که هنگام اجرای فایل باینری etcd
درون یک static Pod به آن داده می‌شود. هر کلید در این map نام فلگ است، همان‌گونه که در
خط فرمان ظاهر می‌شود، اما بدون خط تیره(های) ابتدایی.</p>
</td>
</tr>
<tr><td><code>serverCertSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>serverCertSANs</code> نام‌های جایگزین موضوع (SAN) اضافی را برای گواهی امضای
سرور etcd تعیین می‌کند.</p>
</td>
</tr>
<tr><td><code>peerCertSANs</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>peerCertSANs</code> نام‌های جایگزین موضوع (SAN) اضافی را برای گواهی امضای
peer در etcd تعیین می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `Networking`     {#kubeadm-k8s-io-v1beta3-Networking}
    

**نمایش داده می‌شود در:**

- [ClusterConfiguration](#kubeadm-k8s-io-v1beta3-ClusterConfiguration)


<p>Networking شامل عناصری است که پیکربندی شبکه کلاستر را توصیف می‌کنند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>serviceSubnet</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>serviceSubnet</code> زیرشبکه‌ای است که Serviceهای کوبرنتیز از آن استفاده می‌کنند. مقدار پیش‌فرض آن &quot;10.96.0.0/12&quot; است.</p>
</td>
</tr>
<tr><td><code>podSubnet</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>podSubnet</code> زیرشبکه‌ای است که Podها از آن استفاده می‌کنند.</p>
</td>
</tr>
<tr><td><code>dnsDomain</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>dnsDomain</code> دامنه DNS است که Serviceهای کوبرنتیز از آن استفاده می‌کنند. مقدار پیش‌فرض آن &quot;cluster.local&quot; است.</p>
</td>
</tr>
</tbody>
</table>

## `NodeRegistrationOptions`     {#kubeadm-k8s-io-v1beta3-NodeRegistrationOptions}
    

**نمایش داده می‌شود در:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>NodeRegistrationOptions شامل فیلدهایی است که به ثبت یک control-plane یا نود جدید
در کلاستر، چه از طریق <code>kubeadm init</code> و چه از طریق <code>kubeadm join</code>، مربوط می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>name</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>name</code> همان فیلد <code>.metadata.name</code> آبجکت Node API است که در این
عملیات <code>kubeadm init</code> یا <code>kubeadm join</code> ایجاد خواهد شد.
این فیلد همچنین در فیلد <code>CommonName</code> گواهی کلاینت kubelet برای
API server استفاده می‌شود.
در صورت ارائه نشدن، مقدار پیش‌فرض آن نام میزبان (hostname) نود است.</p>
</td>
</tr>
<tr><td><code>criSocket</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>criSocket</code> برای دریافت اطلاعات container runtime به کار می‌رود.
این اطلاعات برای استفاده مجدد در آینده، به‌صورت annotation روی آبجکت Node API درج خواهد شد.</p>
</td>
</tr>
<tr><td><code>taints</code> <B>[Required]</B><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#taint-v1-core"><code>[]core/v1.Taint</code></a>
</td>
<td>
   <p>فیلد <code>taints</code> taintهایی را مشخص می‌کند که آبجکت Node API باید با آن‌ها ثبت شود.
اگر این فیلد تنظیم نشده باشد، یعنی nil باشد، برای نودهای control-plane مقدار پیش‌فرض آن یک taint مربوط به control-plane خواهد بود.
اگر نمی‌خواهید نود control-plane شما taint داشته باشد، این فیلد را روی یک فهرست خالی تنظیم کنید،
یعنی در فایل YAML مقدار <code>taints: []</code> را بنویسید. این فیلد صرفاً برای ثبت Node استفاده می‌شود.</p>
</td>
</tr>
<tr><td><code>kubeletExtraArgs</code><br/>
<code>map[string]string</code>
</td>
<td>
   <p>فیلد <code>kubeletExtraArgs</code> آرگومان‌های اضافی را به kubelet منتقل می‌کند.
آرگومان‌های این فیلد از طریق فایل محیطی (environment file) که kubeadm در زمان اجرا می‌نویسد
و kubelet آن را بارگذاری می‌کند، به خط فرمان kubelet داده می‌شوند.
این مقادیر، پیکربندی عمومی در سطح پایه موجود در ConfigMap با نام <code>kubelet-config</code> را بازنویسی می‌کنند.
هنگام تجزیه (parse)، فلگ‌ها اولویت بالاتری دارند. این مقادیر محلی هستند و مختص نودی‌اند که
kubeadm روی آن در حال اجراست. هر کلید در این map نام فلگ است، همان‌گونه که در
خط فرمان ظاهر می‌شود، اما بدون خط تیره(های) ابتدایی.</p>
</td>
</tr>
<tr><td><code>ignorePreflightErrors</code><br/>
<code>[]string</code>
</td>
<td>
   <p>فیلد <code>ignorePreflightErrors</code> فهرستی از خطاهای pre-flight را فراهم می‌کند که هنگام
ثبت نود جاری نادیده گرفته می‌شوند، برای مثال <code>IsPrevilegedUser,Swap</code>.
مقدار <code>all</code> خطاهای همه بررسی‌ها را نادیده می‌گیرد.</p>
</td>
</tr>
<tr><td><code>imagePullPolicy</code><br/>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#pullpolicy-v1-core"><code>core/v1.PullPolicy</code></a>
</td>
<td>
   <p>فیلد <code>imagePullPolicy</code> سیاست دریافت ایمیج را در طول عملیات &quot;init&quot; و
&quot;join&quot; در kubeadm مشخص می‌کند.
مقدار این فیلد باید یکی از &quot;Always&quot;، &quot;IfNotPresent&quot; یا &quot;Never&quot; باشد.
اگر این فیلد تنظیم نشود، kubeadm مقدار پیش‌فرض آن را &quot;IfNotPresent&quot; قرار می‌دهد، یعنی در صورت نبودن
ایمیج‌های موردنیاز روی میزبان، آن‌ها را دریافت می‌کند.</p>
</td>
</tr>
</tbody>
</table>

## `Patches`     {#kubeadm-k8s-io-v1beta3-Patches}
    

**نمایش داده می‌شود در:**

- [InitConfiguration](#kubeadm-k8s-io-v1beta3-InitConfiguration)

- [JoinConfiguration](#kubeadm-k8s-io-v1beta3-JoinConfiguration)


<p>Patches شامل گزینه‌های مربوط به اعمال patch بر مؤلفه‌هایی است که توسط kubeadm مستقر می‌شوند.</p>


<table class="table">
<thead><tr><th width="30%">فیلد</th><th>توضیحات</th></tr></thead>
<tbody>
    
  
<tr><td><code>directory</code><br/>
<code>string</code>
</td>
<td>
   <p>فیلد <code>directory</code> مسیر دایرکتوری‌ای است که شامل فایل‌هایی با نام
&quot;target[suffix][+patchtype].extension&quot; است.
برای مثال، &quot;kube-apiserver0+merge.yaml&quot; یا فقط &quot;etcd.json&quot;. مقدار &quot;target&quot; می‌تواند یکی از
&quot;kube-apiserver&quot;، &quot;kube-controller-manager&quot;، &quot;kube-scheduler&quot;، &quot;etcd&quot;، &quot;kubeletconfiguration&quot; و
&quot;corednsdeployment&quot; باشد. مقدار &quot;patchtype&quot; می‌تواند یکی از &quot;strategic&quot;، &quot;merge&quot; یا &quot;json&quot; باشد و
این مقادیر با قالب‌های patch پشتیبانی‌شده توسط kubectl مطابقت دارند.
مقدار پیش‌فرض &quot;patchtype&quot; برابر &quot;strategic&quot; است. مقدار &quot;extension&quot; باید &quot;json&quot; یا &quot;yaml&quot; باشد.
مقدار &quot;suffix&quot; یک رشته اختیاری است که می‌توان از آن برای تعیین این‌که کدام patchها
زودتر و بر اساس ترتیب الفبایی-عددی اعمال شوند، استفاده کرد.</p>
</td>
</tr>
</tbody>
</table>
