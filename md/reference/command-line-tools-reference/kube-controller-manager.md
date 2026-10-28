---
title: kube-controller-manager
content_type: tool-reference
weight: 30
auto_generated: true
description: >-
  
---


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


## {{% heading "synopsis" %}}


kube-controller-manager کوبرنتیز یک daemon است که حلقه‌های کنترل اصلی عرضه‌شده همراه با کوبرنتیز را در خود جای داده است. در کاربردهای رباتیک و اتوماسیون، حلقهٔ کنترل (control loop) حلقه‌ای بی‌پایان است که وضعیت یک سیستم را تنظیم و تثبیت می‌کند. در کوبرنتیز، کنترل‌کننده (controller) یک حلقهٔ کنترل است که وضعیت مشترک کلاستر را از طریق apiserver زیر نظر می‌گیرد و تغییراتی اعمال می‌کند تا وضعیت فعلی را به وضعیت مطلوب نزدیک کند. نمونه‌هایی از کنترل‌کننده‌هایی که امروزه همراه با کوبرنتیز عرضه می‌شوند عبارت‌اند از: replication controller، endpoints controller، namespace controller و serviceaccounts controller.

```
kube-controller-manager [flags]
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--allocate-node-cidrs</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا CIDRها برای Podها باید اختصاص داده شوند و روی ارائه‌دهنده ابری تنظیم شوند یا خیر. نیازمند --cluster-cidr است.</p></td>
</tr>

<tr>
<td colspan="2">--allow-metric-labels stringToString&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: []</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نگاشت از برچسب متریک (metric-label) به فهرست مقادیر مجاز آن برچسب. قالب کلید به‌صورت &lt;MetricName&gt;,&lt;LabelName&gt; است. قالب مقدار به‌صورت &lt;allowed_value&gt;,&lt;allowed_value&gt;... است؛ برای مثال metric1,label1='v1,v2,v3', metric1,label2='v1,v2,v3' metric2,label1='v1,v2,v3'.</p></td>
</tr>

<tr>
<td colspan="2">--allow-metric-labels-manifest string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل مانیفستی که نگاشت فهرست مجاز را در بر دارد. قالب این فایل مانند قالب فلگ --allow-metric-labels است، یعنی:<br/>allowListMapping:<br/>&quot;metric1,label1&quot;: &quot;value11,value12&quot;<br/>&quot;metric2,label2&quot;: &quot;&quot;<br/>توجه داشته باشید که فلگ --allow-metric-labels بر فایل مانیفست اولویت دارد و آن را بازنویسی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--attach-detach-reconcile-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>زمان انتظار هم‌گام‌سازی reconciler میان اتصال (attach) و جداسازی (detach) حجم‌ها. این مدت باید بیشتر از یک ثانیه باشد و افزایش این مقدار نسبت به مقدار پیش‌فرض ممکن است باعث ناهماهنگی حجم‌ها با Podها شود.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که به سرور «core» کوبرنتیز اشاره می‌کند و دسترسی کافی برای ایجاد tokenreviews.authentication.k8s.io را دارد. این گزینه اختیاری است. اگر خالی باشد، تمام درخواست‌های توکن ناشناس در نظر گرفته می‌شوند و هیچ CA کلاینتی در کلاستر جست‌وجو نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-skip-lookup</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر false باشد، از authentication-kubeconfig برای جست‌وجوی پیکربندی احراز هویت مفقود از کلاستر استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-cache-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های احراز‌کننده توکن مبتنی بر webhook در حافظه نهان.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-tolerate-lookup-failure</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، شکست در جست‌وجوی پیکربندی احراز هویت مفقود از کلاستر مهلک در نظر گرفته نمی‌شود. توجه داشته باشید که این امر می‌تواند منجر به احراز هویتی شود که با همه درخواست‌ها به‌صورت ناشناس رفتار می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-always-allow-paths strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/healthz,/readyz,/livez"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از مسیرهای HTTP که در حین مجوزدهی نادیده گرفته می‌شوند؛ یعنی این مسیرها بدون تماس با سرور «core» کوبرنتیز مجاز شمرده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل kubeconfig که به سرور «core» کوبرنتیز اشاره می‌کند و دسترسی کافی برای ایجاد subjectaccessreviews.authorization.k8s.io را دارد. این گزینه اختیاری است. اگر خالی باشد، تمام درخواست‌هایی که از مجوزدهی معاف نشده‌اند ممنوع می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-authorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های «مجاز» (authorized) از مجوزدهنده webhook در حافظه نهان.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-unauthorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های «غیرمجاز» (unauthorized) از مجوزدهنده webhook در حافظه نهان.</p></td>
</tr>

<tr>
<td colspan="2">--bind-address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آدرس IP که روی آن برای پورت --secure-port گوش داده می‌شود. اینترفیس‌های مرتبط باید برای سایر بخش‌های کلاستر و برای کلاینت‌های CLI/وب قابل دسترسی باشند. اگر خالی باشد یا آدرس نامشخص (0.0.0.0 یا ::) باشد، تمام اینترفیس‌ها و خانواده‌های آدرس IP مورد استفاده قرار می‌گیرند.</p></td>
</tr>

<tr>
<td colspan="2">--cert-dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری که گواهی‌های TLS در آن قرار دارند. اگر --tls-cert-file و --tls-private-key-file مشخص شده باشند، این فلگ نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cidr-allocator-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "RangeAllocator"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع تخصیص‌دهنده CIDR که باید استفاده شود</p></td>
</tr>

<tr>
<td colspan="2">--client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، هر درخواستی که گواهی کلاینتی ارائه کند که توسط یکی از مراجع موجود در client-ca-file امضا شده باشد، با هویتی متناظر با CommonName گواهی کلاینت احراز هویت می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cloud-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی ارائه‌دهنده ابری. رشته خالی به معنای نبود فایل پیکربندی است.</p></td>
</tr>

<tr>
<td colspan="2">--cloud-provider string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ارائه‌دهنده سرویس‌های ابری. رشته خالی به معنای نبود ارائه‌دهنده است.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-cidr string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدوده CIDR برای Podها در کلاستر. فقط زمانی استفاده می‌شود که --allocate-node-cidrs=true باشد؛ اگر false باشد، این گزینه نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-name string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kubernetes"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پیشوند نمونه (instance) برای کلاستر.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی گواهی CA از نوع X509 با کدگذاری PEM است و برای صدور گواهی‌های با دامنه کلاستر استفاده می‌شود. اگر این گزینه مشخص شود، هیچ فلگ اختصاصی‌تر --cluster-signing-* نباید مشخص شود.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 8760h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر مدت اعتباری که به گواهی‌های امضاشده داده می‌شود. هر CSR می‌تواند با تنظیم spec.expirationSeconds گواهی‌هایی با مدت کوتاه‌تر درخواست کند.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است و برای امضای گواهی‌های با دامنه کلاستر استفاده می‌شود. اگر این گزینه مشخص شود، هیچ فلگ اختصاصی‌تر --cluster-signing-* نباید مشخص شود.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-kube-apiserver-client-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی گواهی CA از نوع X509 با کدگذاری PEM است و برای صدور گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/kube-apiserver-client استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-kube-apiserver-client-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است و برای امضای گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/kube-apiserver-client استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-kubelet-client-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی گواهی CA از نوع X509 با کدگذاری PEM است و برای صدور گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/kube-apiserver-client-kubelet استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-kubelet-client-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است و برای امضای گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/kube-apiserver-client-kubelet استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-kubelet-serving-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی گواهی CA از نوع X509 با کدگذاری PEM است و برای صدور گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/kubelet-serving استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-kubelet-serving-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است و برای امضای گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/kubelet-serving استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-legacy-unknown-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی گواهی CA از نوع X509 با کدگذاری PEM است و برای صدور گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/legacy-unknown استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-signing-legacy-unknown-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام فایلی که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است و برای امضای گواهی‌ها برای امضاکننده (signer) با نام kubernetes.io/legacy-unknown استفاده می‌شود. اگر این گزینه مشخص شود، --cluster-signing-{cert,key}-file نباید تنظیم شده باشد.</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-cron-job-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های cron job که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = Jobهایی با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-daemonset-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های daemonset که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = daemonsetهایی با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-deployment-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های deployment که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = deploymentهایی با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-device-taint-eviction-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 8</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد عملیات‌هایی (خارج‌کردن Podها، به‌روزرسانی وضعیت DeviceTaintRule) که اجازه دارند به‌صورت همزمان اجرا شوند. عدد بزرگ‌تر = پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-disruption-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های PDB که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = به‌روزرسانی‌های PDB با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-endpoint-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد عملیات‌های هم‌گام‌سازی endpoint که به‌صورت همزمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر endpointها، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-ephemeralvolume-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد عملیات‌های هم‌گام‌سازی حجم موقت (ephemeral volume) که به‌صورت همزمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر حجم‌های موقت، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-gc-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 20</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد workerهای garbage collector که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند.</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-horizontal-pod-autoscaler-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های horizontal pod autoscaler که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = پردازش آبجکت‌های horizontal pod autoscaler با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر.</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-job-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های job که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = Jobهایی با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-namespace-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های namespace که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = خاتمه سریع‌تر فضای نام (namespace)، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-rc-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد replication controllerهایی که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = مدیریت replica با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-replicaset-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد replica setهایی که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = مدیریت replica با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-resource-quota-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد resource quotaهایی که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = مدیریت سهمیه با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-resourceclaim-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد عملیات‌هایی (ایجاد یا حذف ResourceClaimها) که اجازه دارند به‌صورت همزمان اجرا شوند. عدد بزرگ‌تر = پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-service-endpoint-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد عملیات‌های هم‌گام‌سازی endpoint سرویس که به‌صورت همزمان انجام می‌شوند. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر endpoint sliceها، اما بار CPU (و شبکه) بیشتر. مقدار پیش‌فرض 5 است.</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-serviceaccount-token-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های توکن service account که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = تولید توکن با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-statefulset-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد آبجکت‌های statefulset که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند. عدد بزرگ‌تر = statefulsetهایی با پاسخ‌گویی بیشتر، اما بار CPU (و شبکه) بیشتر</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-ttl-after-finished-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد workerهای ttl-after-finished-controller که اجازه دارند به‌صورت همزمان هم‌گام‌سازی شوند.</p></td>
</tr>

<tr>
<td colspan="2">--concurrent-validating-admission-policy-status-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد worker‌های ValidatingAdmissionPolicyStatusController که مجاز به همگام‌سازی هم‌زمان هستند.</p></td>
</tr>

<tr>
<td colspan="2">--configure-cloud-routes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعیین می‌کند که آیا CIDRهای تخصیص‌یافته توسط allocate-node-cidrs باید روی ارائه‌دهنده ابری پیکربندی شوند یا خیر.</p></td>
</tr>

<tr>
<td colspan="2">--contention-profiling</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت فعال بودن profiling، پروفایل‌گیری از block را فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--controller-shutdown-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار برای خاموش شدن کنترل‌کننده‌ها پیش از پایان دادن به فایل اجرایی</p></td>
</tr>

<tr>
<td colspan="2">--controller-start-interval duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصله زمانی بین راه‌اندازی controller managerها.</p></td>
</tr>

<tr>
<td colspan="2">--controllers strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "*"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از کنترل‌کننده‌هایی که باید فعال شوند. '*' همه کنترل‌کننده‌هایی را که به‌طور پیش‌فرض فعال هستند فعال می‌کند، 'foo' کنترل‌کننده‌ای با نام 'foo' را فعال می‌کند و '-foo' کنترل‌کننده‌ای با نام 'foo' را غیرفعال می‌کند.<br/>همه کنترل‌کننده‌ها: bootstrap-signer-controller, certificatesigningrequest-approving-controller, certificatesigningrequest-cleaner-controller, certificatesigningrequest-signing-controller, clusterrole-aggregation-controller, cronjob-controller, daemonset-controller, deployment-controller, device-taint-eviction-controller, disruption-controller, endpoints-controller, endpointslice-controller, endpointslice-mirroring-controller, ephemeral-volume-controller, garbage-collector-controller, horizontal-pod-autoscaler-controller, job-controller, kube-apiserver-serving-clustertrustbundle-publisher-controller, legacy-serviceaccount-token-cleaner-controller, namespace-controller, node-ipam-controller, node-lifecycle-controller, persistentvolume-attach-detach-controller, persistentvolume-binder-controller, persistentvolume-expander-controller, persistentvolume-protection-controller, persistentvolumeclaim-protection-controller, pod-garbage-collector-controller, podcertificaterequest-cleaner-controller, podgroup-protection-controller, replicaset-controller, replicationcontroller-controller, resourceclaim-controller, resourcepoolstatusrequest-controller, resourcequota-controller, root-ca-certificate-publisher-controller, selinux-warning-controller, service-cidr-controller, serviceaccount-controller, serviceaccount-token-controller, statefulset-controller, storage-version-migrator-controller, storageversion-garbage-collector-controller, taint-eviction-controller, token-cleaner-controller, ttl-after-finished-controller, ttl-controller, validatingadmissionpolicy-status-controller, volumeattributesclass-protection-controller<br/>کنترل‌کننده‌هایی که به‌طور پیش‌فرض غیرفعال هستند: bootstrap-signer-controller, selinux-warning-controller, token-cleaner-controller</p></td>
</tr>

<tr>
<td colspan="2">--disable-attach-detach-reconcile-sync</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>همگام‌سازی reconciler مربوط به attach و detach حجم (volume) را غیرفعال می‌کند. غیرفعال کردن این گزینه ممکن است باعث ناهماهنگی بین حجم‌ها و Podها شود. با احتیاط از آن استفاده کنید.</p></td>
</tr>

<tr>
<td colspan="2">--disable-force-detach-on-timeout</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از جداسازی اجباری (force detach) حجم‌ها بر اساس حداکثر زمان unmount و وضعیت نود جلوگیری می‌کند. اگر این پرچم روی true تنظیم شود، برای بازیابی از خرابی نود باید از قابلیت خاموش شدن غیرمنتظم نود (non-graceful node shutdown) استفاده کرد. به https://k8s.io/docs/storage-disable-force-detach-on-timeout/ مراجعه کنید.</p></td>
</tr>

<tr>
<td colspan="2">--disable-http2-serving</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، سرویس‌دهی HTTP2 غیرفعال خواهد شد [default=false]</p></td>
</tr>

<tr>
<td colspan="2">--disabled-metrics strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>این پرچم راهی اضطراری برای متریک‌هایی است که رفتار نادرست دارند. برای غیرفعال کردن یک متریک باید نام کامل (fully qualified) آن را وارد کنید. توجه: غیرفعال کردن متریک‌ها اولویت بالاتری نسبت به نمایش متریک‌های پنهان دارد.</p></td>
</tr>

<tr>
<td colspan="2">--emulated-version strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه‌هایی که اجزای مختلف قابلیت‌های خود (APIها، ویژگی‌ها و ...) را بر اساس آن‌ها شبیه‌سازی می‌کنند.<br/>در صورت تنظیم، جزء مورد نظر به‌جای نسخه باینری زیربنایی، رفتار این نسخه را شبیه‌سازی می‌کند.<br/>قالب نسخه فقط می‌تواند major.minor باشد، برای مثال: '--emulated-version=wardle=1.2,kube=1.31'.<br/>گزینه‌ها عبارت‌اند از: kube=1.34..1.37(default:1.37)<br/>اگر جزء مشخص نشود، به‌طور پیش‌فرض «kube» در نظر گرفته می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--enable-dynamic-provisioning&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تأمین پویا (dynamic provisioning) را برای محیط‌هایی که از آن پشتیبانی می‌کنند فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--enable-garbage-collector&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>garbage collector عمومی را فعال می‌کند. این مقدار باید با پرچم متناظر در kube-apiserver هماهنگ باشد.</p></td>
</tr>

<tr>
<td colspan="2">--enable-hostpath-provisioner</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>هنگام اجرا بدون ارائه‌دهنده ابری، تأمین PV از نوع HostPath را فعال می‌کند. این امر امکان آزمایش و توسعه قابلیت‌های تأمین را فراهم می‌کند. تأمین HostPath به هیچ شکلی پشتیبانی نمی‌شود، در کلاستر چندنودی کار نخواهد کرد و نباید برای هیچ منظوری جز آزمایش یا توسعه استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--enable-leader-migration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعیین می‌کند که آیا مهاجرت leader کنترل‌کننده (controller leader migration) فعال شود یا خیر.</p></td>
</tr>

<tr>
<td colspan="2">--endpoint-updates-batch-period duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>طول بازه دسته‌بندی به‌روزرسانی‌های endpoint. پردازش تغییرات Pod به‌اندازه این مدت به تأخیر می‌افتد تا با به‌روزرسانی‌های احتمالی بعدی ترکیب شود و تعداد کلی به‌روزرسانی‌های endpoint کاهش یابد. عدد بزرگ‌تر = تأخیر بیشتر در برنامه‌ریزی endpoint، اما تعداد کمتر نسخه‌های endpoint تولیدشده</p></td>
</tr>

<tr>
<td colspan="2">--endpointslice-updates-batch-period duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>طول بازه دسته‌بندی به‌روزرسانی‌های endpoint slice. پردازش تغییرات Pod به‌اندازه این مدت به تأخیر می‌افتد تا با به‌روزرسانی‌های احتمالی بعدی ترکیب شود و تعداد کلی به‌روزرسانی‌های endpoint کاهش یابد. عدد بزرگ‌تر = تأخیر بیشتر در برنامه‌ریزی endpoint، اما تعداد کمتر نسخه‌های endpoint تولیدشده</p></td>
</tr>

<tr>
<td colspan="2">--external-cloud-volume-plugin string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>افزونه‌ای که هنگام تنظیم cloud provider روی external استفاده می‌شود. می‌تواند خالی باشد و فقط زمانی باید تنظیم شود که cloud-provider برابر external است. در حال حاضر برای این استفاده می‌شود که node-ipam-controller، persistentvolume-binder-controller، persistentvolume-expander-controller و attach-detach-controller بتوانند با ارائه‌دهندگان ابری درون‌درخت (in-tree) کار کنند.</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates colonSeparatedMultimapStringString</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با کاما از جفت‌های component:key=value که feature gateهای ویژگی‌های آلفا/آزمایشی اجزای مختلف را توصیف می‌کنند.<br/>اگر جزء مشخص نشود، به‌طور پیش‌فرض «kube» در نظر گرفته می‌شود. این پرچم را می‌توان چندین بار به کار برد. برای مثال: --feature-gates 'wardle:featureA=true,wardle:featureB=false' --feature-gates 'kube:featureC=true'. گزینه‌ها عبارت‌اند از:<br/>kube:APIResponseCompression=true|false (BETA - default=true)<br/>kube:APIServerIdentity=true|false (BETA - default=true)<br/>kube:APIServerWebhookAuthenticationToken=true|false (ALPHA - default=false)<br/>kube:APIServingWithRoutine=true|false (ALPHA - default=false)<br/>kube:AllAlpha=true|false (ALPHA - default=false)<br/>kube:AllBeta=true|false (BETA - default=false)<br/>kube:AllowParsingUserUIDFromCertAuth=true|false (BETA - default=true)<br/>kube:AllowUnsafeMalformedObjectDeletion=true|false (BETA - default=true)<br/>kube:AtomicFIFO=true|false (BETA - default=true)<br/>kube:AtomicWriteVolumeUserFields=true|false (ALPHA - default=false)<br/>kube:AuthorizePodWebsocketUpgradeCreatePermission=true|false (BETA - default=true)<br/>kube:CBORServingAndStorage=true|false (ALPHA - default=false)<br/>kube:CPUManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>kube:CPUManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>kube:CRDObservedGenerationTracking=true|false (BETA - default=true)<br/>kube:CRIListStreaming=true|false (ALPHA - default=false)<br/>kube:CSIVolumeHealth=true|false (ALPHA - default=false)<br/>kube:ClearingNominatedNodeNameAfterBinding=true|false (BETA - default=true)<br/>kube:ClientsAllowCARotation=true|false (BETA - default=true)<br/>kube:ClientsAllowCBOR=true|false (ALPHA - default=false)<br/>kube:ClientsAllowTLSCacheGC=true|false (BETA - default=true)<br/>kube:ClientsPreferCBOR=true|false (ALPHA - default=false)<br/>kube:CloudControllerManagerWatchBasedRoutesReconciliation=true|false (ALPHA - default=false)<br/>kube:CloudControllerManagerWebhook=true|false (ALPHA - default=false)<br/>kube:ComponentFlagz=true|false (BETA - default=true)<br/>kube:ComponentStatusz=true|false (BETA - default=true)<br/>kube:CompositePodGroup=true|false (ALPHA - default=false)<br/>kube:ConcurrentWatchObjectDecode=true|false (BETA - default=true)<br/>kube:ConsistentListFromCacheSkipTimeoutFallback=true|false (ALPHA - default=false)<br/>kube:ConstrainedImpersonation=true|false (BETA - default=true)<br/>kube:ContainerCheckpoint=true|false (BETA - default=true)<br/>kube:ContainerRestartRules=true|false (BETA - default=true)<br/>kube:ContainerStopSignals=true|false (ALPHA - default=false)<br/>kube:ContextualLogging=true|false (BETA - default=true)<br/>kube:ControllerManagerReleaseLeaderElectionLockOnExit=true|false (ALPHA - default=false)<br/>kube:CoordinatedLeaderElection=true|false (BETA - default=false)<br/>kube:CrossNamespaceVolumeDataSource=true|false (ALPHA - default=false)<br/>kube:DRAConsumableCapacity=true|false (BETA - default=true)<br/>kube:DRADerivedAttributes=true|false (ALPHA - default=false)<br/>kube:DRADeviceBindingConditions=true|false (BETA - default=true)<br/>kube:DRADeviceCompatibilityGroups=true|false (ALPHA - default=false)<br/>kube:DRAFractionalCapacityRange=true|false (BETA - default=false)، یا DRAFractionalCapacityRange=true|false (BETA - default=true) اگر --min-compatibility-version&gt;=1.37<br/>kube:DRAListTypeAttributes=true|false (ALPHA - default=false)<br/>kube:DRANodeAllocatableResources=true|false (ALPHA - default=false)<br/>kube:DRAOptionalNodeOperations=true|false (ALPHA - default=false)<br/>kube:DRAPartitionableDevices=true|false (BETA - default=true)<br/>kube:DRAPartitionableDevicesType=true|false (ALPHA - default=false)<br/>kube:DRAResourceClaimGranularStatusAuthorization=true|false (BETA - default=true)<br/>kube:DRAResourcePoolStatus=true|false (ALPHA - default=false)<br/>kube:DRASchedulerFilterTimeout=true|false (BETA - default=true)<br/>kube:DRAWorkloadResourceClaims=true|false (BETA - default=false)<br/>kube:DeclarativeValidationBeta=true|false (BETA - default=true)<br/>kube:DefaultPodSysctls=true|false (ALPHA - default=false)<br/>kube:DeploymentReplicaSetTerminatingReplicas=true|false (BETA - default=true)<br/>kube:DetectCacheInconsistency=true|false (BETA - default=true)<br/>kube:EmptyDirVolumeMode=true|false (ALPHA - default=false)<br/>kube:EnvFiles=true|false (BETA - default=true)<br/>kube:EtcdRangeStream=true|false (BETA - default=true)<br/>kube:EventedPLEG=true|false (ALPHA - default=false)<br/>kube:EvictionRequestAPI=true|false (ALPHA - default=false)<br/>kube:ExcludeAdmissionWebhookVirtualResources=true|false (BETA - default=true)<br/>kube:ExtendWebSocketsToKubelet=true|false (BETA - default=true)<br/>kube:GRPCContainerProbeTLS=true|false (ALPHA - default=false)<br/>kube:GenericWorkload=true|false (BETA - default=false)<br/>kube:GracefulNodeShutdown=true|false (BETA - default=true)<br/>kube:GracefulNodeShutdownBasedOnPodPriority=true|false (BETA - default=true)<br/>kube:H2CContainerProbe=true|false (ALPHA - default=false)<br/>kube:HPAGeneration=true|false (BETA - default=true)<br/>kube:HPAOptimizedSelectorStore=true|false (BETA - default=true)<br/>kube:HPAScaleToZero=true|false (BETA - default=true)<br/>kube:HugepageAwareEviction=true|false (BETA - default=true)<br/>kube:ImageVolumeWithDigest=true|false (ALPHA - default=false)<br/>kube:InOrderInformersBatchProcess=true|false (BETA - default=true)<br/>kube:InPlacePodLevelResourcesVerticalScaling=true|false (BETA - default=true)<br/>kube:InPlacePodVerticalScalingExclusiveCPUs=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingExclusiveMemory=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingMemoryBackedVolumes=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingSchedulerPreemption=true|false (ALPHA - default=false)<br/>kube:InterPodAffinityHostnameFastPath=true|false (ALPHA - default=false)<br/>kube:KubeProxyNFTablesLocalhostNodePorts=true|false (ALPHA - default=false)<br/>kube:KubeletAllocatedPodsEndpoint=true|false (ALPHA - default=false)<br/>kube:KubeletCrashLoopBackOffMax=true|false (BETA - default=true)<br/>kube:KubeletEnsureSecretPulledImages=true|false (BETA - default=true)<br/>kube:KubeletInUserNamespace=true|false (BETA - default=true)<br/>kube:KubeletSeparateDiskGC=true|false (BETA - default=true)<br/>kube:KubeletServiceAccountTokenForCredentialProviders=true|false (BETA - default=true)<br/>kube:ListFromCacheSnapshot=true|false (BETA - default=true)<br/>kube:LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (BETA - default=false)<br/>kube:LoggingAlphaOptions=true|false (ALPHA - default=false)<br/>kube:LoggingBetaOptions=true|false (BETA - default=true)<br/>kube:ManifestBasedAdmissionControlConfig=true|false (BETA - default=true)<br/>kube:MatchLabelKeysInPodTopologySpread=true|false (BETA - default=true)<br/>kube:MatchLabelKeysInPodTopologySpreadSelectorMerge=true|false (BETA - default=true)<br/>kube:MaxUnavailableStatefulSet=true|false (BETA - default=true)<br/>kube:MemoryQoS=true|false (BETA - default=true)<br/>kube:MutablePVNodeAffinity=true|false (ALPHA - default=false)<br/>kube:MutablePodResourcesForSuspendedJobs=true|false (BETA - default=true)<br/>kube:MutableSchedulingDirectivesForSuspendedJobs=true|false (BETA - default=true)<br/>kube:NFTablesNetlink=true|false (BETA - default=true)<br/>kube:NativeHistograms=true|false (BETA - default=true)<br/>kube:NodeControllerLeaseCircuitBreaker=true|false (BETA - default=true)<br/>kube:NodeLifecycleConditions=true|false (ALPHA - default=false)<br/>kube:NominatedNodeNameForExpectation=true|false (BETA - default=true)<br/>kube:OpenAPIEnums=true|false (BETA - default=true)<br/>kube:OpportunisticBatching=true|false (BETA - default=true)<br/>kube:PersistentVolumeClaimUnusedSinceTime=true|false (BETA - default=true)<br/>kube:PodAndContainerStatsFromCRI=true|false (BETA - default=false)<br/>kube:PodDeletionCost=true|false (BETA - default=true)<br/>kube:PodGroupPreemptionPolicy=true|false (ALPHA - default=false)<br/>kube:PodLevelResourceManagers=true|false (BETA - default=false)<br/>kube:PodLevelResources=true|false (BETA - default=true)<br/>kube:PodLevelResourcesFixDefaulting=true|false (BETA - default=true)<br/>kube:PodLevelResourcesFixKubeletQOSClass=true|false (BETA - default=true)<br/>kube:PodLogsQuerySplitStreams=true|false (ALPHA - default=false)<br/>kube:PodTopologyLabelsAdmission=true|false (BETA - default=true)<br/>kube:PodsAPI=true|false (BETA - default=true)<br/>kube:PortForwardWebsockets=true|false (BETA - default=true)<br/>kube:QOSReserved=true|false (ALPHA - default=false)<br/>kube:ReduceDefaultCrashLoopBackOffDecay=true|false (ALPHA - default=false)<br/>kube:ReloadKubeletClientCAFile=true|false (BETA - default=true)<br/>kube:ReloadKubeletServerCertificateFile=true|false (BETA - default=true)<br/>kube:RemoteRequestHeaderUID=true|false (BETA - default=true)<br/>kube:ResourceHealthStatus=true|false (BETA - default=true)<br/>kube:ResourceHealthStatusMessage=true|false (BETA - default=true)<br/>kube:RestartAllContainersOnContainerExits=true|false (BETA - default=true)<br/>kube:RotateKubeletServerCertificate=true|false (BETA - default=true)<br/>kube:RuntimeClassInImageCriApi=true|false (ALPHA - default=false)<br/>kube:SchedulerAsyncAPICalls=true|false (BETA - default=false)<br/>kube:SchedulerAsyncPreemption=true|false (BETA - default=true)<br/>kube:SchedulerPopFromBackoffQ=true|false (BETA - default=true)<br/>kube:SchedulerPreQueueingHints=true|false (ALPHA - default=false)<br/>kube:ServiceAccountNodeAudienceRestriction=true|false (BETA - default=true)<br/>kube:ShardedListAndWatch=true|false (ALPHA - default=false)<br/>kube:SizeBasedListCostEstimate=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyDaemonSet=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyHPA=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyJob=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyReplicaSet=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyStatefulSet=true|false (BETA - default=true)<br/>kube:StatefulSetRecreateStrategy=true|false (ALPHA - default=false)<br/>kube:StatefulSetSemanticRevisionComparison=true|false (BETA - default=true)<br/>kube:StorageCapacityScoring=true|false (BETA - default=true)<br/>kube:StorageVersionAPI=true|false (ALPHA - default=false)<br/>kube:StorageVersionHash=true|false (BETA - default=true)<br/>kube:StrictIPCIDRValidation=true|false (BETA - default=true)<br/>kube:StructuredAuthenticationConfigurationEgressSelector=true|false (BETA - default=true)<br/>kube:StructuredAuthenticationConfigurationJWKSMetrics=true|false (BETA - default=true)<br/>kube:TaintTolerationComparisonOperators=true|false (ALPHA - default=false)<br/>kube:TokenRequestServiceAccountUIDValidation=true|false (BETA - default=true)<br/>kube:TopologyAwareWorkloadScheduling=true|false (ALPHA - default=false)<br/>kube:TopologyManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>kube:TopologyManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>kube:TranslateStreamCloseWebsocketRequests=true|false (BETA - default=true)<br/>kube:UnauthenticatedHTTP2DOSMitigation=true|false (BETA - default=true)<br/>kube:UnknownVersionInteroperabilityProxy=true|false (BETA - default=true)<br/>kube:UnlockWhileProcessingFIFO=true|false (BETA - default=true)<br/>kube:UserNamespacesHostNetworkSupport=true|false (ALPHA - default=false)<br/>kube:VolumeBindMountOptions=true|false (ALPHA - default=false)<br/>kube:VolumeLimitScaling=true|false (BETA - default=true)<br/>kube:WatchList=true|false (BETA - default=true)<br/>kube:WatchListClient=true|false (BETA - default=true)<br/>kube:WatchListCompression=true|false (BETA - default=true)<br/>kube:WebhookRoundTripLoadBalancing=true|false (BETA - default=true)<br/>kube:WindowsCPUAndMemoryAffinity=true|false (ALPHA - default=false)<br/>kube:WindowsGracefulNodeShutdown=true|false (BETA - default=true)<br/>kube:WorkloadWithJob=true|false (ALPHA - default=false)</p></td>
</tr>

<tr>
<td colspan="2">--flex-volume-plugin-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/usr/libexec/kubernetes/kubelet-plugins/volume/exec/"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر کامل دایرکتوری‌ای که افزونه flex volume باید در آن به‌دنبال افزونه‌های حجم (volume) شخص ثالث اضافی بگردد.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنما برای kube-controller-manager</p></td>
</tr>

<tr>
<td colspan="2">--horizontal-pod-autoscaler-cpu-initialization-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی پس از شروع به کار Pod که طی آن ممکن است نمونه‌های CPU نادیده گرفته شوند.</p></td>
</tr>

<tr>
<td colspan="2">--horizontal-pod-autoscaler-downscale-stabilization duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی که autoscaler در آن به عقب نگاه می‌کند و تعداد replicaها را به کمتر از هر توصیه‌ای که در آن بازه ارائه کرده است کاهش نمی‌دهد.</p></td>
</tr>

<tr>
<td colspan="2">--horizontal-pod-autoscaler-initial-readiness-delay duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی پس از شروع به کار Pod که طی آن تغییرات آمادگی (readiness) به‌عنوان آمادگی اولیه در نظر گرفته می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--horizontal-pod-autoscaler-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی همگام‌سازی تعداد Podها در horizontal pod autoscaler.</p></td>
</tr>

<tr>
<td colspan="2">--horizontal-pod-autoscaler-tolerance float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل تغییر (نسبت به 1.0) در نسبت متریک‌های مطلوب به واقعی که horizontal pod autoscaler برای در نظر گرفتن مقیاس‌دهی لازم دارد.</p></td>
</tr>

<tr>
<td colspan="2">--http2-max-streams-per-connection int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حد بیشینه تعداد streamها در یک اتصال HTTP/2 که سرور به کلاینت‌ها اعلام می‌کند. مقدار صفر به معنی استفاده از مقدار پیش‌فرض golang است.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار burst برای ارتباط با kubernetes apiserver.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-content-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "application/vnd.kubernetes.protobuf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع محتوای درخواست‌های ارسالی به apiserver.</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-qps float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 20</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار QPS برای ارتباط با kubernetes apiserver.</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل kubeconfig که شامل اطلاعات احراز مجوز و نشانی master است (نشانی master را می‌توان با پرچم master بازنویسی کرد).</p></td>
</tr>

<tr>
<td colspan="2">--large-cluster-size-threshold int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد نودهایی که از آن به بعد node-lifecycle-controller برای منطق جابه‌جایی (eviction) کلاستر را بزرگ در نظر می‌گیرد. برای کلاسترهایی با این اندازه یا کوچک‌تر، مقدار --secondary-node-eviction-rate به‌طور ضمنی با 0 بازنویسی می‌شود. توجه: اگر نودها در چندین zone قرار داشته باشند، این آستانه برای هر zone به‌عنوان آستانه اندازه نودهای آن zone در نظر گرفته می‌شود تا نرخ جابه‌جایی نودها به‌صورت مستقل تعیین شود.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پیش از اجرای حلقه اصلی، یک کلاینت انتخاب رهبر (leader election) راه‌اندازی می‌کند و رهبری را به دست می‌گیرد. هنگام اجرای مؤلفه‌های replicate‌شده برای دسترس‌پذیری بالا، این گزینه را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-lease-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که کاندیداهای غیررهبر پس از مشاهده تمدید رهبری صبر می‌کنند تا برای تصاحب رهبری یک slot رهبری که اشغال شده اما تمدید نشده است اقدام کنند. این مقدار در واقع بیشینه مدتی است که یک رهبر می‌تواند متوقف باشد تا کاندیدای دیگری جایگزین آن شود. این گزینه فقط در صورتی کاربرد دارد که انتخاب رهبر فعال باشد.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-renew-deadline duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصله زمانی بین تلاش‌های master فعلی برای تمدید slot رهبری پیش از آنکه از رهبری دست بکشد. این مقدار باید کمتر از مدت lease باشد. این گزینه فقط در صورتی کاربرد دارد که انتخاب رهبر فعال باشد.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-resource-lock string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "leases"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع آبجکت منبعی که برای قفل‌گذاری در هنگام انتخاب رهبر استفاده می‌شود. گزینه‌های پشتیبانی‌شده: 'leases'.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-resource-name string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kube-controller-manager"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام آبجکت منبعی که برای قفل‌گذاری در هنگام انتخاب رهبر استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-resource-namespace string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "kube-system"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فضای نام (namespace) آبجکت منبعی که برای قفل‌گذاری در هنگام انتخاب رهبر استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--leader-elect-retry-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که کلاینت‌ها باید بین تلاش‌های کسب و تمدید رهبری صبر کنند. این گزینه فقط در صورتی کاربرد دارد که انتخاب رهبر فعال باشد.</p></td>
</tr>

<tr>
<td colspan="2">--leader-migration-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل پیکربندی برای مهاجرت رهبر (leader migration) کنترل‌کننده‌ها، یا خالی بگذارید تا از مقداری استفاده شود که پیکربندی پیش‌فرض controller manager را منعکس می‌کند. فایل پیکربندی باید از نوع LeaderMigrationConfiguration، گروه controllermanager.config.k8s.io و نسخه v1alpha1 باشد.</p></td>
</tr>

<tr>
<td colspan="2">--legacy-service-account-token-clean-up-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 8760h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که باید از آخرین استفاده از یک توکن legacy service account بگذرد تا بتوان آن را حذف کرد.</p></td>
</tr>

<tr>
<td colspan="2">--log-flush-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد ثانیه‌ها بین دو flush متوالی لاگ‌ها</p></td>
</tr>

<tr>
<td colspan="2">--log-text-info-buffer-size quantity</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی با جریان‌های خروجی جداشده، پیام‌های info را می‌توان برای مدتی بافر کرد تا کارایی افزایش یابد. مقدار پیش‌فرض صفر بایت، بافرکردن را غیرفعال می‌کند. اندازه را می‌توان به‌صورت تعداد بایت (512)، مضرب‌های 1000 (1K)، مضرب‌های 1024 (2Ki) یا توان‌های آن‌ها (3M، 4G، 5Mi، 6Gi) مشخص کرد. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--log-text-split-stream</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی، پیام‌های خطا را در stderr و پیام‌های info را در stdout می‌نویسد. رفتار پیش‌فرض نوشتن یک جریان واحد در stdout است. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--logging-format string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "text"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب لاگ را تعیین می‌کند. قالب‌های مجاز: &quot;text&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--master string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی سرور API کوبرنتیز (هر مقداری را که در kubeconfig آمده است بازنویسی می‌کند).</p></td>
</tr>

<tr>
<td colspan="2">--max-endpoints-per-slice int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد endpointهایی که به یک EndpointSlice اضافه می‌شود. تعداد بیشتر endpoint در هر slice منجر به تعداد کمتر EndpointSlice اما منابع بزرگ‌تر می‌شود. مقدار پیش‌فرض 100 است.</p></td>
</tr>

<tr>
<td colspan="2">--min-compatibility-version strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل نسخه مؤلفه‌های control plane که سرور باید با آن سازگار باشد.<br/>باید کمتر از emulated-version یا برابر با آن باشد. قالب نسخه فقط می‌تواند major.minor باشد، برای مثال: '--min-compatibility-version=wardle=1.2,kube=1.31'.<br/>گزینه‌ها: kube=1.34..1.37(default:1.36)<br/>اگر مؤلفه مشخص نشود، مقدار پیش‌فرض &quot;kube&quot; است</p></td>
</tr>

<tr>
<td colspan="2">--min-resync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 12h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه همگام‌سازی مجدد (resync) در reflectorها به‌صورت تصادفی بین MinResyncPeriod و 2*MinResyncPeriod خواهد بود.</p></td>
</tr>

<tr>
<td colspan="2">--mirroring-concurrent-service-endpoint-syncs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد عملیات همگام‌سازی endpoint سرویس که endpointslice-mirroring-controller به‌صورت همزمان انجام می‌دهد. عدد بزرگ‌تر = به‌روزرسانی سریع‌تر EndpointSlice، اما بار CPU (و شبکه) بیشتر. مقدار پیش‌فرض 5 است.</p></td>
</tr>

<tr>
<td colspan="2">--mirroring-endpointslice-updates-batch-period duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>طول بازه دسته‌بندی به‌روزرسانی‌های EndpointSlice برای endpointslice-mirroring-controller. پردازش تغییرات EndpointSlice به اندازه این مدت به تأخیر می‌افتد تا با به‌روزرسانی‌های احتمالی پیش‌رو ترکیب شود و تعداد کل به‌روزرسانی‌های EndpointSlice کاهش یابد. عدد بزرگ‌تر = تأخیر بیشتر در برنامه‌ریزی endpointها، اما تعداد کمتر نسخه‌های endpoint تولیدشده</p></td>
</tr>

<tr>
<td colspan="2">--mirroring-max-endpoints-per-subset int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1000</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد endpointهایی که endpointslice-mirroring-controller به یک EndpointSlice اضافه می‌کند. تعداد بیشتر endpoint در هر slice منجر به تعداد کمتر EndpointSlice اما منابع بزرگ‌تر می‌شود. مقدار پیش‌فرض 100 است.</p></td>
</tr>

<tr>
<td colspan="2">--namespace-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی همگام‌سازی به‌روزرسانی‌های چرخه حیات فضای نام (namespace)</p></td>
</tr>

<tr>
<td colspan="2">--node-cidr-mask-size int32</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اندازه ماسک CIDR نود در کلاستر. مقدار پیش‌فرض برای IPv4 برابر 24 و برای IPv6 برابر 64 است.</p></td>
</tr>

<tr>
<td colspan="2">--node-cidr-mask-size-ipv4 int32</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اندازه ماسک CIDR نود برای IPv4 در کلاستر dual-stack. مقدار پیش‌فرض 24 است.</p></td>
</tr>

<tr>
<td colspan="2">--node-cidr-mask-size-ipv6 int32</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اندازه ماسک CIDR نود برای IPv6 در کلاستر dual-stack. مقدار پیش‌فرض 64 است.</p></td>
</tr>

<tr>
<td colspan="2">--node-eviction-rate float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد نودها در ثانیه که در صورت خرابی نود، Podهای آن‌ها حذف می‌شود، در حالی که zone سالم است (برای تعریف سالم/ناسالم به --unhealthy-zone-threshold مراجعه کنید). در کلاسترهای غیرچندزونه، zone به کل کلاستر اشاره دارد.</p></td>
</tr>

<tr>
<td colspan="2">--node-monitor-grace-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که اجازه می‌دهیم یک نود در حال اجرا پاسخگو نباشد، پیش از آنکه ناسالم علامت‌گذاری شود. این مقدار باید N برابر nodeStatusUpdateFrequency در kubelet باشد، که N تعداد دفعات مجاز تلاش مجدد kubelet برای ارسال وضعیت نود است. این مقدار همچنین باید از مجموع HTTP2_PING_TIMEOUT_SECONDS و HTTP2_READ_IDLE_TIMEOUT_SECONDS بزرگ‌تر باشد</p></td>
</tr>

<tr>
<td colspan="2">--node-monitor-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی همگام‌سازی NodeStatus در NodeLifecycleController.</p></td>
</tr>

<tr>
<td colspan="2">--node-startup-grace-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که اجازه می‌دهیم یک نودِ در حال راه‌اندازی پاسخگو نباشد، پیش از آنکه ناسالم علامت‌گذاری شود.</p></td>
</tr>

<tr>
<td colspan="2">--permit-address-sharing</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام bind کردن پورت از SO_REUSEADDR استفاده می‌شود. این کار امکان bind همزمان به IPهای wildcard مانند 0.0.0.0 و IPهای مشخص را فراهم می‌کند و از انتظار برای آزادشدن socketهای در حالت TIME_WAIT توسط کرنل جلوگیری می‌کند. [default=false]</p></td>
</tr>

<tr>
<td colspan="2">--permit-port-sharing</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام bind کردن پورت از SO_REUSEPORT استفاده می‌شود که اجازه می‌دهد بیش از یک نمونه روی یک نشانی و پورت یکسان bind شوند. [default=false]</p></td>
</tr>

<tr>
<td colspan="2">--profiling&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فعال‌سازی profiling از طریق رابط وب در host:port/debug/pprof/</p></td>
</tr>

<tr>
<td colspan="2">--pv-recycler-increment-timeout-nfs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار زمانی که به ازای هر Gi به ActiveDeadlineSeconds برای یک Pod پاک‌کننده (scrubber) مربوط به NFS افزوده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--pv-recycler-minimum-timeout-hostpath int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 60</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل مقدار ActiveDeadlineSeconds برای یک Pod بازیافت‌کننده (Recycler) از نوع HostPath. این گزینه فقط برای توسعه و آزمایش است و در کلاستر چندنودی کار نخواهد کرد.</p></td>
</tr>

<tr>
<td colspan="2">--pv-recycler-minimum-timeout-nfs int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 300</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل مقدار ActiveDeadlineSeconds برای یک Pod بازیافت‌کننده (Recycler) از نوع NFS</p></td>
</tr>

<tr>
<td colspan="2">--pv-recycler-pod-template-filepath-hostpath string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل تعریف Pod که به‌عنوان قالب برای بازیافت persistent volume از نوع HostPath استفاده می‌شود. این گزینه فقط برای توسعه و آزمایش است و در کلاستر چندنودی کار نخواهد کرد.</p></td>
</tr>

<tr>
<td colspan="2">--pv-recycler-pod-template-filepath-nfs string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل تعریف Pod که به‌عنوان قالب برای بازیافت persistent volume از نوع NFS استفاده می‌شود</p></td>
</tr>

<tr>
<td colspan="2">--pv-recycler-timeout-increment-hostpath int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار زمانی که به ازای هر Gi به ActiveDeadlineSeconds برای یک Pod پاک‌کننده (scrubber) از نوع HostPath افزوده می‌شود. این گزینه فقط برای توسعه و آزمایش است و در کلاستر چندنودی کار نخواهد کرد.</p></td>
</tr>

<tr>
<td colspan="2">--pvclaimbinder-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی همگام‌سازی persistent volumeها و persistent volume claimها</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-allowed-names strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست common nameهای گواهی کلاینت که مجاز به ارائه نام کاربری در هدرهای مشخص‌شده با --requestheader-username-headers هستند. اگر خالی باشد، هر گواهی کلاینتی که توسط مراجع موجود در --requestheader-client-ca-file اعتبارسنجی شده باشد مجاز است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بسته گواهی ریشه (root certificate bundle) که برای تأیید گواهی‌های کلاینت در درخواست‌های ورودی استفاده می‌شود، پیش از آنکه به نام‌های کاربری موجود در هدرهای مشخص‌شده با --requestheader-username-headers اعتماد شود. هشدار: به‌طور کلی نباید به این وابسته بود که احراز مجوز (authorization) برای درخواست‌های ورودی از قبل انجام شده است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-extra-headers-prefix strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "x-remote-extra-"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست پیشوندهای هدر درخواست که باید بررسی شوند. پیشنهاد می‌شود X-Remote-Extra- استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-group-headers strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "x-remote-group"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای تعیین گروه‌ها بررسی می‌شوند. پیشنهاد می‌شود X-Remote-Group استفاده شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-uid-headers strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای تعیین UIDها بررسی می‌شوند. پیشنهاد می‌شود X-Remote-Uid استفاده شود. نیازمند فعال بودن قابلیت RemoteRequestHeaderUID است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-username-headers strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "x-remote-user"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای تعیین نام‌های کاربری بررسی می‌شوند. X-Remote-User رایج است.</p></td>
</tr>

<tr>
<td colspan="2">--resource-quota-sync-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی همگام‌سازی وضعیت مصرف سهمیه (quota) در سیستم</p></td>
</tr>

<tr>
<td colspan="2">--root-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تنظیم، این مرجع گواهی ریشه (root certificate authority) در Secret مربوط به توکن service account گنجانده می‌شود. این مقدار باید یک بسته CA معتبر با کدگذاری PEM باشد.</p></td>
</tr>

<tr>
<td colspan="2">--route-reconciliation-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه زمانی تطبیق (reconcile) مسیرهایی که توسط ارائه‌دهنده ابری برای نودها ایجاد شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--secondary-node-eviction-rate float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.01</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد نودهایی که در هر ثانیه Podهای آن‌ها در صورت خرابی نود حذف می‌شوند، هنگامی که یک zone ناسالم است (برای تعریف سالم/ناسالم به --unhealthy-zone-threshold مراجعه کنید). در کلاسترهای غیرچندzone، zone به کل کلاستر اشاره دارد. اگر اندازه کلاستر از --large-cluster-size-threshold کوچک‌تر باشد، این مقدار به‌طور ضمنی با 0 جایگزین می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--secure-port int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10257</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورتی که HTTPS همراه با احراز هویت و احراز مجوز روی آن ارائه می‌شود. اگر 0 باشد، HTTPS اصلاً ارائه نمی‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-private-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تنظیم، توکن‌های قدیمی مبتنی بر Secret را فعال می‌کند. نام فایلی که حاوی کلید خصوصی RSA یا ECDSA با کدگذاری PEM است و برای امضای توکن‌های service account استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--service-cluster-ip-range string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدوده CIDR برای Serviceها در کلاستر. فقط زمانی استفاده می‌شود که --allocate-node-cidrs=true باشد؛ در غیر این صورت این گزینه نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--show-hidden-metrics-for-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه قبلی که می‌خواهید معیارهای (metrics) پنهان آن نمایش داده شود. فقط نسخه فرعی (minor) قبلی معنا دارد و مقادیر دیگر پذیرفته نخواهند شد. قالب آن &lt;major&gt;.&lt;minor&gt; است، برای مثال: '1.16'. هدف از این قالب آن است که اگر انتشار بعدی معیارهای بیشتری را پنهان کند، فرصت داشته باشید متوجه شوید، و هنگام حذف دائمی آن‌ها در انتشار پس از آن غافلگیر نشوید.</p></td>
</tr>

<tr>
<td colspan="2">--terminated-pod-gc-threshold int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 12500</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد Podهای خاتمه‌یافته‌ای که می‌توانند وجود داشته باشند، پیش از آنکه garbage collector مربوط به Podهای خاتمه‌یافته شروع به حذف آن‌ها کند. اگر مقدار &lt;= 0 باشد، garbage collector مربوط به Podهای خاتمه‌یافته غیرفعال است.</p></td>
</tr>

<tr>
<td colspan="2">--tls-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی گواهی x509 پیش‌فرض برای HTTPS. (گواهی CA، در صورت وجود، پس از گواهی سرور الحاق می‌شود). اگر ارائه HTTPS فعال باشد و --tls-cert-file و --tls-private-key-file مشخص نشده باشند، یک گواهی و کلید خودامضا برای نشانی عمومی تولید شده و در دایرکتوری مشخص‌شده با --cert-dir ذخیره می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--tls-cipher-suites strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مجموعه رمزنگاری‌ها (cipher suites) برای سرور، جداشده با ویرگول. اگر مشخص نشود، از cipher suiteهای پیش‌فرض Go استفاده می‌شود.<br/>مقادیر توصیه‌شده: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256.<br/>مقادیر ناامن: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_RC4_128_SHA.</p></td>
</tr>

<tr>
<td colspan="2">--tls-curve-preferences int32Slice&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: []</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از مقادیر عددی CurveID در crypto/tls زبان Go، جداشده با ویرگول، به‌عنوان سازوکارهای مجاز تبادل کلید برای سرور. مقادیر پشتیبانی‌شده به نسخه Go مورد استفاده بستگی دارد. برای مقادیر پشتیبانی‌شده در هر نسخه Go به https://pkg.go.dev/crypto/tls#CurveID مراجعه کنید. ترتیب فهرست نادیده گرفته می‌شود و Go سازوکارهای تبادل کلید را از میان این فهرست با استفاده از یک ترتیب ترجیحی داخلی انتخاب می‌کند. اگر مشخص نشود، از curveهای پیش‌فرض Go استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--tls-min-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل نسخه TLS پشتیبانی‌شده. مقادیر ممکن: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13</p></td>
</tr>

<tr>
<td colspan="2">--tls-private-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی کلید خصوصی x509 پیش‌فرض که با --tls-cert-file مطابقت دارد.</p></td>
</tr>

<tr>
<td colspan="2">--tls-sni-cert-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک جفت مسیر فایل گواهی x509 و کلید خصوصی که می‌تواند به‌صورت اختیاری با فهرستی از الگوهای دامنه (domain patterns) پایان یابد؛ این الگوها نام‌های دامنه کاملاً معتبر (fully qualified) هستند و ممکن است بخش‌های wildcard در ابتدا داشته باشند. الگوهای دامنه نشانی‌های IP را نیز می‌پذیرند، اما IP فقط زمانی باید استفاده شود که apiserver به نشانی IP درخواست‌شده توسط کلاینت دسترسی داشته باشد. اگر الگوی دامنه‌ای ارائه نشود، نام‌های موجود در گواهی استخراج می‌شوند. تطابق‌های بدون wildcard بر تطابق‌های wildcard اولویت دارند و الگوهای دامنه صریح بر نام‌های استخراج‌شده اولویت دارند. برای چند جفت کلید/گواهی، --tls-sni-cert-key را چندین بار استفاده کنید. مثال‌ها: &quot;example.crt,example.key&quot; یا &quot;foo.crt,foo.key:*.foo.com,foo.com&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--unhealthy-zone-threshold float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.55</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کسری از نودهای یک zone که باید در وضعیت Ready نباشند (حداقل ۳) تا آن zone ناسالم تلقی شود.</p></td>
</tr>

<tr>
<td colspan="2">--use-service-account-credentials</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، برای هر کنترل‌کننده از اعتبارنامه‌های جداگانه service account استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">-v, --v int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عدد مربوط به سطح جزئیات لاگ (log level verbosity)</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>--version و --version=raw اطلاعات نسخه را چاپ کرده و خارج می‌شوند؛ --version=vX.Y.Z... نسخه گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--vmodule pattern=N,...</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست تنظیمات pattern=N جداشده با ویرگول برای لاگ‌گیری فیلترشده بر اساس فایل (فقط برای قالب لاگ متنی کار می‌کند)</p></td>
</tr>

</tbody>
</table>
