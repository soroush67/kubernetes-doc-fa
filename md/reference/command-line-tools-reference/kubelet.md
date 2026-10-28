---
title: kubelet
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


kubelet عامل اصلی «نود» (node agent) است که روی هر نود اجرا می‌شود. این مؤلفه می‌تواند نود را با یکی از روش‌های زیر در apiserver ثبت کند: با استفاده از نام میزبان (hostname)؛ با استفاده از یک پرچم (flag) که نام میزبان را بازنویسی می‌کند؛ یا با استفاده از منطق مخصوص یک ارائه‌دهنده ابری (cloud provider).

kubelet بر اساس PodSpec کار می‌کند. PodSpec یک آبجکت YAML یا JSON است که یک pod را توصیف می‌کند. kubelet مجموعه‌ای از PodSpecها را که از طریق سازوکارهای گوناگون (عمدتاً از طریق apiserver) در اختیارش قرار می‌گیرد دریافت می‌کند و اطمینان می‌دهد که کانتینرهای توصیف‌شده در این PodSpecها در حال اجرا و سالم باشند. kubelet کانتینرهایی را که توسط کوبرنتیز ایجاد نشده‌اند مدیریت نمی‌کند.

علاوه بر PodSpec دریافتی از apiserver، دو روش دیگر نیز برای ارائه مانیفست کانتینر به kubelet وجود دارد.

فایل: مسیری که به‌صورت یک پرچم در خط فرمان داده می‌شود. فایل‌های موجود در این مسیر به‌طور دوره‌ای برای یافتن به‌روزرسانی‌ها پایش می‌شوند. بازه پایش به‌طور پیش‌فرض ۲۰ ثانیه است و از طریق یک پرچم قابل پیکربندی است.

نقطه پایانی HTTP (HTTP endpoint): نقطه پایانی HTTP که به‌صورت یک پارامتر در خط فرمان داده می‌شود. این نقطه پایانی هر ۲۰ ثانیه بررسی می‌شود (این بازه نیز با یک پرچم قابل پیکربندی است).

```
kubelet [flags]
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آدرس IP که Kubelet روی آن سرویس‌دهی می‌کند (برای گوش دادن روی تمام اینترفیس‌ها و خانواده‌های آدرس IP مقدار '0.0.0.0' یا '::' را تنظیم کنید) (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--allowed-unsafe-sysctls strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مجاز، جداشده با کاما، از sysctlهای ناایمن یا الگوهای sysctl ناایمن (که به * ختم می‌شوند). استفاده از این موارد با مسئولیت خودتان است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--anonymous-auth&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>درخواست‌های ناشناس به سرور Kubelet را فعال می‌کند. درخواست‌هایی که توسط روش احراز هویت دیگری رد نشوند، به‌عنوان درخواست ناشناس در نظر گرفته می‌شوند. درخواست‌های ناشناس دارای نام کاربری system:anonymous و نام گروه system:unauthenticated هستند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای تعیین احراز هویت توکن‌های bearer از TokenReview API استفاده می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-cache-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های احراز‌کننده توکن webhook در حافظه نهان. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--authorization-mode string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "AlwaysAllow"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حالت مجوزدهی برای سرور Kubelet. گزینه‌های معتبر AlwaysAllow یا Webhook هستند. حالت Webhook برای تعیین مجوزدهی از SubjectAccessReview API استفاده می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-authorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های «مجاز» (authorized) از مجوزدهنده webhook در حافظه نهان. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-unauthorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های «غیرمجاز» (unauthorized) از مجوزدهنده webhook در حافظه نهان. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--bootstrap-kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر یک فایل kubeconfig که برای دریافت گواهی کلاینت برای kubelet استفاده می‌شود. اگر فایل مشخص‌شده با --kubeconfig وجود نداشته باشد، از bootstrap kubeconfig برای درخواست گواهی کلاینت از API server استفاده می‌شود. در صورت موفقیت، یک فایل kubeconfig که به گواهی کلاینت و کلید تولیدشده ارجاع می‌دهد در مسیر مشخص‌شده با --kubeconfig نوشته می‌شود. فایل گواهی کلاینت و کلید در دایرکتوری مشخص‌شده با --cert-dir ذخیره خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--cert-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/var/lib/kubelet/pki"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری که گواهی‌های TLS در آن قرار دارند. اگر --tls-cert-file و --tls-private-key-file ارائه شده باشند، این پرچم نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--cgroup-driver string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "cgroupfs"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>درایوری که kubelet برای مدیریت cgroupها روی میزبان از آن استفاده می‌کند. مقادیر ممکن: 'cgroupfs'، 'systemd' (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cgroup-root string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>cgroup ریشه اختیاری برای استفاده توسط podها. این مورد توسط container runtime و در حد امکان (best effort) مدیریت می‌شود. مقدار پیش‌فرض: '' که به معنای استفاده از مقدار پیش‌فرض container runtime است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cgroups-per-qos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ایجاد سلسله‌مراتب cgroup مربوط به QoS را فعال می‌کند؛ در صورت true بودن، cgroupهای سطح بالای QoS و cgroupهای podها ایجاد می‌شوند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تنظیم، هر درخواستی که گواهی کلاینتی ارائه کند که توسط یکی از مراجع موجود در client-ca-file امضا شده باشد، با هویتی متناظر با CommonName گواهی کلاینت احراز هویت می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cloud-provider string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ارائه‌دهنده سرویس‌های ابری. برای اجرا بدون ارائه‌دهنده ابری، آن را روی رشته خالی تنظیم کنید. برای اجرا با یک ارائه‌دهنده ابری خارجی، آن را روی 'external' تنظیم کنید.</p></td>
</tr>

<tr>
<td colspan="2">--cluster-dns strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست آدرس‌های IP سرورهای DNS، جداشده با کاما. این مقدار برای سرور DNS کانتینرها در Podهایی با &quot;dnsPolicy=ClusterFirst&quot; استفاده می‌شود. توجه: تمام سرورهای DNS موجود در این فهرست باید مجموعه رکوردهای یکسانی را ارائه کنند، در غیر این صورت ممکن است تفکیک نام در داخل کلاستر به‌درستی کار نکند. هیچ تضمینی وجود ندارد که برای تفکیک نام با کدام سرور DNS ارتباط برقرار شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cluster-domain string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دامنه این کلاستر. در صورت تنظیم، kubelet تمام کانتینرها را طوری پیکربندی می‌کند که علاوه بر دامنه‌های جست‌وجوی میزبان، این دامنه را نیز جست‌وجو کنند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>Kubelet پیکربندی اولیه خود را از این فایل بارگذاری می‌کند. مسیر می‌تواند مطلق یا نسبی باشد؛ مسیرهای نسبی از دایرکتوری کاری فعلی Kubelet شروع می‌شوند. برای استفاده از مقادیر پیش‌فرض داخلی پیکربندی، این پرچم را حذف کنید. پرچم‌های خط فرمان، پیکربندی این فایل را بازنویسی می‌کنند.</p></td>
</tr>

<tr>
<td colspan="2">--config-dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری حاوی فایل‌های پیکربندی drop-in که تنظیمات مقادیر پیش‌فرض و فایل --config را بازنویسی می‌کنند. مسیر می‌تواند مطلق یا نسبی باشد؛ مسیرهای نسبی از دایرکتوری کاری فعلی Kubelet شروع می‌شوند. فایل‌های drop-in باید پسوند '.conf' داشته باشند (مثلاً '99-kubelet-address.conf') و به ترتیب واژه‌نامه‌ای (lexical) پردازش می‌شوند. فقط فایل‌های '.conf' بارگذاری می‌شوند و سایر فایل‌ها نادیده گرفته می‌شوند. تمام فایل‌های .conf موجود در دایرکتوری و زیردایرکتوری‌های آن به ترتیب واژه‌نامه‌ای پردازش می‌شوند. [default='']</p></td>
</tr>

<tr>
<td colspan="2">--container-log-max-files int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>&lt;هشدار: قابلیت بتا&gt; حداکثر تعداد فایل‌های لاگ کانتینر را که می‌توانند برای یک کانتینر وجود داشته باشند تعیین می‌کند. این عدد باید &gt;= 2 باشد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--container-log-max-size string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "10Mi"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>&lt;هشدار: قابلیت بتا&gt; حداکثر اندازه (مثلاً 10Mi) فایل لاگ کانتینر را پیش از چرخش (rotate) تعیین می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--container-runtime-endpoint string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "unix:///run/containerd/containerd.sock"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نقطه پایانی (endpoint) سرویس container runtime. Unix Domain Socketها در لینوکس پشتیبانی می‌شوند، در حالی که endpointهای npipe و tcp در ویندوز پشتیبانی می‌شوند. مثال‌ها: 'unix:///path/to/runtime.sock'، 'npipe:////./pipe/runtime' (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--contention-profiling</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت فعال بودن profiling، پروفایل‌گیری از بلاک‌ها (block profiling) را فعال می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cpu-cfs-quota&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اعمال سهمیه CPU CFS را برای کانتینرهایی که محدودیت CPU مشخص می‌کنند فعال می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cpu-cfs-quota-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100ms</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار دوره سهمیه CPU CFS (cpu.cfs_period_us) را تنظیم می‌کند. مقدار پیش‌فرض برابر با مقدار پیش‌فرض هسته لینوکس است. برای تنظیم مقادیر غیرپیش‌فرض، feature gate با نام CustomCPUCFSQuotaPeriod لازم است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cpu-manager-policy string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>سیاست CPU Manager مورد استفاده. مقادیر ممکن: 'none'، 'static'. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cpu-manager-policy-options &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از گزینه‌های سیاست CPU Manager به‌صورت key=value برای تنظیم دقیق رفتار آن‌ها. در صورت ارائه نشدن، رفتار پیش‌فرض حفظ می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--cpu-manager-reconcile-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>&lt;هشدار: قابلیت آلفا&gt; دوره تطبیق (reconciliation) در CPU Manager. مثال‌ها: '10s' یا '1m'. در صورت ارائه نشدن، مقدار پیش‌فرض برابر با 'NodeStatusUpdateFrequency' است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--enable-controller-attach-detach&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کنترل‌کننده Attach/Detach را برای مدیریت اتصال و جداسازی حجم‌های (volume) زمان‌بندی‌شده روی این نود فعال می‌کند و اجرای هرگونه عملیات attach/detach را توسط kubelet غیرفعال می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--enable-debugging-handlers&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>endpointهای سرور را برای جمع‌آوری لاگ و اجرای محلی کانتینرها و دستورها فعال می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--enable-server&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>سرور Kubelet را فعال می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--enforce-node-allocatable strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "pods"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با کاما از سطوح اعمال node allocatable که باید توسط kubelet اعمال شوند. گزینه‌های قابل قبول عبارت‌اند از 'none'، 'pods'، 'system-reserved'، 'system-reserved-compressible'، 'kube-reserved' و 'kube-reserved-compressible'. اگر هر یک از چهار گزینه آخر مشخص شود، باید به‌ترتیب '--system-reserved-cgroup' و '--kube-reserved-cgroup' نیز تنظیم شوند. اگر 'none' مشخص شود، نباید هیچ گزینه دیگری تنظیم شود. برای جزئیات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/ مراجعه کنید. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--event-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر اندازه رکوردهای رویداد در حالت انفجاری (burst)؛ به‌طور موقت اجازه می‌دهد رکوردهای رویداد تا این عدد به‌صورت burst ارسال شوند، بدون آن‌که از event-qps فراتر روند. این عدد باید &gt;= 0 باشد. اگر 0 باشد، از DefaultBurst با مقدار 100 استفاده می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--event-qps int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نرخ QPS برای محدود کردن ایجاد رویدادها (event). این عدد باید بزرگ‌تر یا مساوی 0 باشد. اگر 0 باشد، هیچ محدودیتی اعمال نمی‌شود. توجه: اگر تنظیم نشود، مقدار پیش‌فرض پیکربندی kubelet اعمال می‌شود که در حال حاضر 50 است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--eviction-hard &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از آستانه‌های تخلیه (eviction) (برای مثال memory.available&lt;1Gi) که در صورت برقرار شدن، تخلیه Pod را فعال می‌کنند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--eviction-max-pod-grace-period int32</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر مهلت مجاز (به ثانیه) برای خاتمه دادن به Podها هنگامی که یک آستانه تخلیه نرم (soft eviction) برقرار شده است. اگر مقدار منفی باشد، مقدار مشخص‌شده در Pod ملاک خواهد بود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--eviction-minimum-reclaim &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از حداقل مقادیر بازیابی (برای مثال imagefs.available=2Gi) که مشخص می‌کند kubelet هنگام انجام تخلیه Pod، در صورتی که منبع مربوطه تحت فشار باشد، حداقل چه مقدار از آن منبع را بازیابی خواهد کرد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--eviction-pressure-transition-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمانی که kubelet باید پیش از خروج از وضعیت فشار تخلیه (eviction pressure) صبر کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--eviction-soft &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از آستانه‌های تخلیه (برای مثال memory.available&lt;1.5Gi) که در صورت برقرار بودن در طول یک مهلت متناظر، تخلیه Pod را فعال می‌کنند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--eviction-soft-grace-period &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از مهلت‌های تخلیه (برای مثال memory.available=1m30s) که مشخص می‌کنند یک آستانه تخلیه نرم باید چه مدت برقرار بماند تا تخلیه Pod فعال شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--exit-on-lock-contention</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا kubelet باید در صورت بروز تداخل بر سر فایل قفل (lock-file) خارج شود یا خیر.</p></td>
</tr>

<tr>
<td colspan="2">--experimental-allocatable-ignore-eviction</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>وقتی روی 'true' تنظیم شود، آستانه‌های تخلیه سخت (Hard Eviction Thresholds) هنگام محاسبه Node Allocatable نادیده گرفته می‌شوند. برای جزئیات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/ مراجعه کنید. [default=false] (منسوخ‌شده: در نسخه 1.25 یا نسخه‌های بعدی حذف خواهد شد.)</p></td>
</tr>

<tr>
<td colspan="2">--experimental-mounter-path string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آزمایشی] مسیر فایل اجرایی mounter. برای استفاده از mount پیش‌فرض، آن را خالی بگذارید. (منسوخ‌شده: در نسخه 1.25 یا نسخه‌های بعدی به نفع استفاده از CSI حذف خواهد شد.)</p></td>
</tr>

<tr>
<td colspan="2">--fail-cgroupv1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از راه‌اندازی kubelet روی میزبانی که از cgroup v1 استفاده می‌کند جلوگیری می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--fail-swap-on&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>باعث می‌شود در صورت فعال بودن swap روی نود، راه‌اندازی kubelet با شکست مواجه شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates &lt;comma-separated 'key=True|False' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از جفت‌های key=value که feature gateهای مربوط به قابلیت‌های آلفا/آزمایشی را توصیف می‌کنند. گزینه‌ها عبارت‌اند از:<br/>APIResponseCompression=true|false (BETA - default=true)<br/>APIServerIdentity=true|false (BETA - default=true)<br/>APIServerWebhookAuthenticationToken=true|false (ALPHA - default=false)<br/>APIServingWithRoutine=true|false (ALPHA - default=false)<br/>AllAlpha=true|false (ALPHA - default=false)<br/>AllBeta=true|false (BETA - default=false)<br/>AllowParsingUserUIDFromCertAuth=true|false (BETA - default=true)<br/>AllowUnsafeMalformedObjectDeletion=true|false (BETA - default=true)<br/>AtomicFIFO=true|false (BETA - default=true)<br/>AtomicWriteVolumeUserFields=true|false (ALPHA - default=false)<br/>AuthorizePodWebsocketUpgradeCreatePermission=true|false (BETA - default=true)<br/>CBORServingAndStorage=true|false (ALPHA - default=false)<br/>CPUManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>CPUManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>CRDObservedGenerationTracking=true|false (BETA - default=true)<br/>CRIListStreaming=true|false (ALPHA - default=false)<br/>CSIVolumeHealth=true|false (ALPHA - default=false)<br/>ClearingNominatedNodeNameAfterBinding=true|false (BETA - default=true)<br/>ClientsAllowCARotation=true|false (BETA - default=true)<br/>ClientsAllowCBOR=true|false (ALPHA - default=false)<br/>ClientsAllowTLSCacheGC=true|false (BETA - default=true)<br/>ClientsPreferCBOR=true|false (ALPHA - default=false)<br/>CloudControllerManagerWatchBasedRoutesReconciliation=true|false (ALPHA - default=false)<br/>CloudControllerManagerWebhook=true|false (ALPHA - default=false)<br/>ComponentFlagz=true|false (BETA - default=true)<br/>ComponentStatusz=true|false (BETA - default=true)<br/>CompositePodGroup=true|false (ALPHA - default=false)<br/>ConcurrentWatchObjectDecode=true|false (BETA - default=true)<br/>ConsistentListFromCacheSkipTimeoutFallback=true|false (ALPHA - default=false)<br/>ConstrainedImpersonation=true|false (BETA - default=true)<br/>ContainerCheckpoint=true|false (BETA - default=true)<br/>ContainerRestartRules=true|false (BETA - default=true)<br/>ContainerStopSignals=true|false (ALPHA - default=false)<br/>ContextualLogging=true|false (BETA - default=true)<br/>ControllerManagerReleaseLeaderElectionLockOnExit=true|false (ALPHA - default=false)<br/>CoordinatedLeaderElection=true|false (BETA - default=false)<br/>CrossNamespaceVolumeDataSource=true|false (ALPHA - default=false)<br/>DRAConsumableCapacity=true|false (BETA - default=true)<br/>DRADerivedAttributes=true|false (ALPHA - default=false)<br/>DRADeviceBindingConditions=true|false (BETA - default=true)<br/>DRADeviceCompatibilityGroups=true|false (ALPHA - default=false)<br/>DRAFractionalCapacityRange=true|false (BETA - default=false)، یا DRAFractionalCapacityRange=true|false (BETA - default=true) اگر --min-compatibility-version&gt;=1.37 باشد<br/>DRAListTypeAttributes=true|false (ALPHA - default=false)<br/>DRANodeAllocatableResources=true|false (ALPHA - default=false)<br/>DRAOptionalNodeOperations=true|false (ALPHA - default=false)<br/>DRAPartitionableDevices=true|false (BETA - default=true)<br/>DRAPartitionableDevicesType=true|false (ALPHA - default=false)<br/>DRAResourceClaimGranularStatusAuthorization=true|false (BETA - default=true)<br/>DRAResourcePoolStatus=true|false (ALPHA - default=false)<br/>DRASchedulerFilterTimeout=true|false (BETA - default=true)<br/>DRAWorkloadResourceClaims=true|false (BETA - default=false)<br/>DeclarativeValidationBeta=true|false (BETA - default=true)<br/>DefaultPodSysctls=true|false (ALPHA - default=false)<br/>DeploymentReplicaSetTerminatingReplicas=true|false (BETA - default=true)<br/>DetectCacheInconsistency=true|false (BETA - default=true)<br/>EmptyDirVolumeMode=true|false (ALPHA - default=false)<br/>EnvFiles=true|false (BETA - default=true)<br/>EtcdRangeStream=true|false (BETA - default=true)<br/>EventedPLEG=true|false (ALPHA - default=false)<br/>EvictionRequestAPI=true|false (ALPHA - default=false)<br/>ExcludeAdmissionWebhookVirtualResources=true|false (BETA - default=true)<br/>ExtendWebSocketsToKubelet=true|false (BETA - default=true)<br/>GRPCContainerProbeTLS=true|false (ALPHA - default=false)<br/>GenericWorkload=true|false (BETA - default=false)<br/>GracefulNodeShutdown=true|false (BETA - default=true)<br/>GracefulNodeShutdownBasedOnPodPriority=true|false (BETA - default=true)<br/>H2CContainerProbe=true|false (ALPHA - default=false)<br/>HPAGeneration=true|false (BETA - default=true)<br/>HPAOptimizedSelectorStore=true|false (BETA - default=true)<br/>HPAScaleToZero=true|false (BETA - default=true)<br/>HugepageAwareEviction=true|false (BETA - default=true)<br/>ImageVolumeWithDigest=true|false (ALPHA - default=false)<br/>InOrderInformersBatchProcess=true|false (BETA - default=true)<br/>InPlacePodLevelResourcesVerticalScaling=true|false (BETA - default=true)<br/>InPlacePodVerticalScalingExclusiveCPUs=true|false (ALPHA - default=false)<br/>InPlacePodVerticalScalingExclusiveMemory=true|false (ALPHA - default=false)<br/>InPlacePodVerticalScalingMemoryBackedVolumes=true|false (ALPHA - default=false)<br/>InPlacePodVerticalScalingSchedulerPreemption=true|false (ALPHA - default=false)<br/>InterPodAffinityHostnameFastPath=true|false (ALPHA - default=false)<br/>KubeProxyNFTablesLocalhostNodePorts=true|false (ALPHA - default=false)<br/>KubeletAllocatedPodsEndpoint=true|false (ALPHA - default=false)<br/>KubeletCrashLoopBackOffMax=true|false (BETA - default=true)<br/>KubeletEnsureSecretPulledImages=true|false (BETA - default=true)<br/>KubeletInUserNamespace=true|false (BETA - default=true)<br/>KubeletSeparateDiskGC=true|false (BETA - default=true)<br/>KubeletServiceAccountTokenForCredentialProviders=true|false (BETA - default=true)<br/>ListFromCacheSnapshot=true|false (BETA - default=true)<br/>LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (BETA - default=false)<br/>LoggingAlphaOptions=true|false (ALPHA - default=false)<br/>LoggingBetaOptions=true|false (BETA - default=true)<br/>ManifestBasedAdmissionControlConfig=true|false (BETA - default=true)<br/>MatchLabelKeysInPodTopologySpread=true|false (BETA - default=true)<br/>MatchLabelKeysInPodTopologySpreadSelectorMerge=true|false (BETA - default=true)<br/>MaxUnavailableStatefulSet=true|false (BETA - default=true)<br/>MemoryQoS=true|false (BETA - default=true)<br/>MutablePVNodeAffinity=true|false (ALPHA - default=false)<br/>MutablePodResourcesForSuspendedJobs=true|false (BETA - default=true)<br/>MutableSchedulingDirectivesForSuspendedJobs=true|false (BETA - default=true)<br/>NFTablesNetlink=true|false (BETA - default=true)<br/>NativeHistograms=true|false (BETA - default=true)<br/>NodeControllerLeaseCircuitBreaker=true|false (BETA - default=true)<br/>NodeLifecycleConditions=true|false (ALPHA - default=false)<br/>NominatedNodeNameForExpectation=true|false (BETA - default=true)<br/>OpenAPIEnums=true|false (BETA - default=true)<br/>OpportunisticBatching=true|false (BETA - default=true)<br/>PersistentVolumeClaimUnusedSinceTime=true|false (BETA - default=true)<br/>PodAndContainerStatsFromCRI=true|false (BETA - default=false)<br/>PodDeletionCost=true|false (BETA - default=true)<br/>PodGroupPreemptionPolicy=true|false (ALPHA - default=false)<br/>PodLevelResourceManagers=true|false (BETA - default=false)<br/>PodLevelResources=true|false (BETA - default=true)<br/>PodLevelResourcesFixDefaulting=true|false (BETA - default=true)<br/>PodLevelResourcesFixKubeletQOSClass=true|false (BETA - default=true)<br/>PodLogsQuerySplitStreams=true|false (ALPHA - default=false)<br/>PodTopologyLabelsAdmission=true|false (BETA - default=true)<br/>PodsAPI=true|false (BETA - default=true)<br/>PortForwardWebsockets=true|false (BETA - default=true)<br/>QOSReserved=true|false (ALPHA - default=false)<br/>ReduceDefaultCrashLoopBackOffDecay=true|false (ALPHA - default=false)<br/>ReloadKubeletClientCAFile=true|false (BETA - default=true)<br/>ReloadKubeletServerCertificateFile=true|false (BETA - default=true)<br/>RemoteRequestHeaderUID=true|false (BETA - default=true)<br/>ResourceHealthStatus=true|false (BETA - default=true)<br/>ResourceHealthStatusMessage=true|false (BETA - default=true)<br/>RestartAllContainersOnContainerExits=true|false (BETA - default=true)<br/>RotateKubeletServerCertificate=true|false (BETA - default=true)<br/>RuntimeClassInImageCriApi=true|false (ALPHA - default=false)<br/>SchedulerAsyncAPICalls=true|false (BETA - default=false)<br/>SchedulerAsyncPreemption=true|false (BETA - default=true)<br/>SchedulerPopFromBackoffQ=true|false (BETA - default=true)<br/>SchedulerPreQueueingHints=true|false (ALPHA - default=false)<br/>ServiceAccountNodeAudienceRestriction=true|false (BETA - default=true)<br/>ShardedListAndWatch=true|false (ALPHA - default=false)<br/>SizeBasedListCostEstimate=true|false (BETA - default=true)<br/>StaleControllerConsistencyDaemonSet=true|false (BETA - default=true)<br/>StaleControllerConsistencyHPA=true|false (BETA - default=true)<br/>StaleControllerConsistencyJob=true|false (BETA - default=true)<br/>StaleControllerConsistencyReplicaSet=true|false (BETA - default=true)<br/>StaleControllerConsistencyStatefulSet=true|false (BETA - default=true)<br/>StatefulSetRecreateStrategy=true|false (ALPHA - default=false)<br/>StatefulSetSemanticRevisionComparison=true|false (BETA - default=true)<br/>StorageCapacityScoring=true|false (BETA - default=true)<br/>StorageVersionAPI=true|false (ALPHA - default=false)<br/>StorageVersionHash=true|false (BETA - default=true)<br/>StrictIPCIDRValidation=true|false (BETA - default=true)<br/>StructuredAuthenticationConfigurationEgressSelector=true|false (BETA - default=true)<br/>StructuredAuthenticationConfigurationJWKSMetrics=true|false (BETA - default=true)<br/>TaintTolerationComparisonOperators=true|false (ALPHA - default=false)<br/>TokenRequestServiceAccountUIDValidation=true|false (BETA - default=true)<br/>TopologyAwareWorkloadScheduling=true|false (ALPHA - default=false)<br/>TopologyManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>TopologyManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>TranslateStreamCloseWebsocketRequests=true|false (BETA - default=true)<br/>UnauthenticatedHTTP2DOSMitigation=true|false (BETA - default=true)<br/>UnknownVersionInteroperabilityProxy=true|false (BETA - default=true)<br/>UnlockWhileProcessingFIFO=true|false (BETA - default=true)<br/>UserNamespacesHostNetworkSupport=true|false (ALPHA - default=false)<br/>VolumeBindMountOptions=true|false (ALPHA - default=false)<br/>VolumeLimitScaling=true|false (BETA - default=true)<br/>WatchList=true|false (BETA - default=true)<br/>WatchListClient=true|false (BETA - default=true)<br/>WatchListCompression=true|false (BETA - default=true)<br/>WebhookRoundTripLoadBalancing=true|false (BETA - default=true)<br/>WindowsCPUAndMemoryAffinity=true|false (ALPHA - default=false)<br/>WindowsGracefulNodeShutdown=true|false (BETA - default=true)<br/>WorkloadWithJob=true|false (ALPHA - default=false) (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--file-check-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 20s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصله زمانی بین بررسی‌های فایل‌های پیکربندی برای یافتن داده‌های جدید (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--hairpin-mode string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "promiscuous-bridge"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نحوه راه‌اندازی hairpin NAT توسط kubelet. این قابلیت به endpointهای یک Service اجازه می‌دهد در صورتی که بخواهند به Service خودشان دسترسی پیدا کنند، ترافیک را به خودشان متعادل‌سازی بار (loadbalance) کنند. مقادیر معتبر عبارت‌اند از &quot;promiscuous-bridge&quot;، &quot;hairpin-veth&quot; و &quot;none&quot;. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--healthz-bind-address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 127.0.0.1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی IP که سرور healthz روی آن سرویس‌دهی می‌کند (برای گوش دادن روی همه رابط‌ها و خانواده‌های نشانی IP، آن را روی '0.0.0.0' یا '::' تنظیم کنید) (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--healthz-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10248</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورت endpoint مربوط به healthz روی localhost (برای غیرفعال کردن، روی 0 تنظیم کنید) (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنما برای kubelet</p></td>
</tr>

<tr>
<td colspan="2">--hostname-override string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار آن خالی نباشد، از این رشته به‌جای نام میزبان (hostname) واقعی برای شناسایی استفاده خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--http-check-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 20s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصله زمانی بین بررسی‌های http برای یافتن داده‌های جدید (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--image-credential-provider-bin-dir string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری که فایل‌های اجرایی افزونه‌های ارائه‌دهنده اعتبارنامه (credential provider) در آن قرار دارند.</p></td>
</tr>

<tr>
<td colspan="2">--image-credential-provider-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر یک فایل پیکربندی افزونه ارائه‌دهنده اعتبارنامه (JSON/YAML/YML) یا یک دایرکتوری از چنین فایل‌هایی (که به ترتیب الفبایی ادغام می‌شوند؛ جستجو به‌صورت غیربازگشتی انجام می‌شود).</p></td>
</tr>

<tr>
<td colspan="2">--image-gc-high-threshold int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 85</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>درصد استفاده از دیسک که پس از رسیدن به آن، زباله‌روبی (garbage collection) ایمیج‌ها همواره اجرا می‌شود. مقادیر باید در بازه [0, 100] باشند. برای غیرفعال کردن زباله‌روبی ایمیج‌ها، مقدار را روی 100 تنظیم کنید. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--image-gc-low-threshold int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 80</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>درصد استفاده از دیسک که زباله‌روبی ایمیج‌ها پیش از رسیدن به آن هرگز اجرا نمی‌شود. کمترین میزان استفاده از دیسک که زباله‌روبی تا آن ادامه می‌یابد. مقادیر باید در بازه [0, 100] باشند و باید کمتر از مقدار --image-gc-high-threshold باشند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--image-service-endpoint string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نقطه پایانی (endpoint) سرویس ایمیج کانتینر. در صورت مشخص نشدن، به‌طور پیش‌فرض همان مقدار --container-runtime-endpoint خواهد بود. در لینوکس از Unix Domain Socket پشتیبانی می‌شود، در حالی که در ویندوز نقاط پایانی npipe و tcp پشتیبانی می‌شوند. نمونه‌ها: 'unix:///path/to/runtime.sock'، 'npipe:////./pipe/runtime' (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kernel-memcg-notification</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت فعال بودن، kubelet برای تشخیص عبور از آستانه‌های اخراج (eviction) حافظه، به‌جای نظرسنجی دوره‌ای (polling)، با اعلان memcg هسته یکپارچه می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار burst هنگام ارتباط با kube-apiserver کوبرنتیز. این عدد باید بزرگ‌تر یا مساوی 0 باشد. اگر 0 باشد از DefaultBurst با مقدار 100 استفاده می‌شود. این مقدار رویدادها (events) و APIهای ضربان قلب (heartbeat) نود را شامل نمی‌شود؛ محدودسازی نرخ آن‌ها با مجموعه‌ای دیگر از پرچم‌ها کنترل می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-content-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "application/vnd.kubernetes.protobuf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع محتوای (content type) درخواست‌های ارسالی به kube-apiserver. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kube-api-qps int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار QPS هنگام ارتباط با kube-apiserver کوبرنتیز. این عدد باید بزرگ‌تر یا مساوی 0 باشد. اگر 0 باشد از DefaultQPS با مقدار 50 استفاده می‌شود. این مقدار رویدادها (events) و APIهای ضربان قلب (heartbeat) نود را شامل نمی‌شود؛ محدودسازی نرخ آن‌ها با مجموعه‌ای دیگر از پرچم‌ها کنترل می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kube-reserved &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از جفت‌های ResourceName=ResourceQuantity (برای مثال cpu=200m,memory=500Mi,ephemeral-storage=1Gi,pid=1000) که منابع رزروشده برای مؤلفه‌های سیستمی کوبرنتیز را توصیف می‌کنند. در حال حاضر فقط cpu، memory، pid و ذخیره‌سازی موقت محلی (local ephemeral storage) برای فایل‌سیستم ریشه پشتیبانی می‌شوند. برای جزئیات بیشتر به https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ مراجعه کنید. [default=none] (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kube-reserved-cgroup string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مطلق cgroup سطح بالا که برای مدیریت مؤلفه‌های کوبرنتیز استفاده می‌شود و منابع محاسباتی آن‌ها از طریق پرچم '--kube-reserved' رزرو شده است. برای مثال '/kube-reserved'. [default=''] (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--kubeconfig string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر یک فایل kubeconfig که نحوه اتصال به API server را مشخص می‌کند. ارائه --kubeconfig حالت API server را فعال می‌کند و حذف آن حالت مستقل (standalone) را فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--kubelet-cgroups string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مطلق اختیاری cgroupها برای ایجاد و اجرای kubelet در آن‌ها. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--local-storage-capacity-isolation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، جداسازی ذخیره‌سازی موقت محلی فعال است. در غیر این صورت، قابلیت جداسازی ذخیره‌سازی محلی غیرفعال خواهد شد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--lock-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>&lt;هشدار: قابلیت آلفا&gt; مسیر فایلی که kubelet به‌عنوان فایل قفل از آن استفاده می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--log-flush-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد ثانیه‌ها بین دو بار تخلیه (flush) لاگ‌ها</p></td>
</tr>

<tr>
<td colspan="2">--log-text-info-buffer-size quantity</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی با جریان‌های خروجی تفکیک‌شده، پیام‌های اطلاعاتی را می‌توان برای مدتی بافر کرد تا کارایی افزایش یابد. مقدار پیش‌فرض صفر بایت، بافر کردن را غیرفعال می‌کند. اندازه را می‌توان به‌صورت تعداد بایت (512)، مضرب‌های 1000 (1K)، مضرب‌های 1024 (2Ki) یا توان‌های آن‌ها (3M، 4G، 5Mi، 6Gi) مشخص کرد. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--log-text-split-stream</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب متنی، پیام‌های خطا را در stderr و پیام‌های اطلاعاتی را در stdout می‌نویسد. رفتار پیش‌فرض نوشتن یک جریان واحد در stdout است. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--logging-format string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "text"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب لاگ را تعیین می‌کند. قالب‌های مجاز: &quot;text&quot;. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--make-iptables-util-chains&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، kubelet اطمینان حاصل می‌کند که قوانین کمکی iptables روی میزبان وجود دارند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--manifest-url string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL برای دسترسی به مشخصات (specification) اضافی Podهایی که باید اجرا شوند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--manifest-url-header colonSeparatedMultimapStringString</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای HTTP جداشده با کاما که هنگام دسترسی به نشانی ارائه‌شده در --manifest-url استفاده می‌شوند. چند هدر با نام یکسان به همان ترتیبی که ارائه شده‌اند افزوده می‌شوند. این پرچم را می‌توان چندین بار به کار برد. برای مثال: --manifest-url-header 'a:hello,b:again,c:world' --manifest-url-header 'b:beautiful' (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--max-open-files int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1000000</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد فایل‌هایی که فرایند kubelet می‌تواند باز کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--max-pods int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 110</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد Podهایی که می‌توانند روی این kubelet اجرا شوند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--maximum-dead-containers int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: -1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد نمونه‌های قدیمی کانتینرها که به‌صورت سراسری نگهداری می‌شوند. هر کانتینر مقداری فضای دیسک اشغال می‌کند. برای غیرفعال کردن، یک عدد منفی تنظیم کنید. (منسوخ‌شده: به‌جای آن از --eviction-hard یا --eviction-soft استفاده کنید. در نسخه‌ای در آینده حذف خواهد شد.)</p></td>
</tr>

<tr>
<td colspan="2">--maximum-dead-containers-per-container int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد نمونه‌های قدیمی که برای هر کانتینر نگهداری می‌شوند. هر کانتینر مقداری فضای دیسک اشغال می‌کند. (منسوخ‌شده: به‌جای آن از --eviction-hard یا --eviction-soft استفاده کنید. در نسخه‌ای در آینده حذف خواهد شد.)</p></td>
</tr>

<tr>
<td colspan="2">--memory-manager-policy string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "None"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>سیاست Memory Manager که باید استفاده شود. مقادیر ممکن: 'None'، 'Static'. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--minimum-container-ttl-duration duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل عمر یک کانتینر خاتمه‌یافته پیش از آنکه زباله‌روبی شود. نمونه‌ها: '300ms'، '10s' یا '2h45m' (منسوخ‌شده: به‌جای آن از --eviction-hard یا --eviction-soft استفاده کنید. در نسخه‌ای در آینده حذف خواهد شد.)</p></td>
</tr>

<tr>
<td colspan="2">--minimum-image-ttl-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل عمر یک ایمیج استفاده‌نشده پیش از آنکه زباله‌روبی شود. نمونه‌ها: '300ms'، '10s' یا '2h45m'. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--node-ip string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی IP نود (یا نشانی‌های IP دوپشته (dual-stack) جداشده با کاما). اگر تنظیم نشود، kubelet از نشانی IPv4 پیش‌فرض نود، در صورت وجود، و در غیر این صورت از نشانی IPv6 پیش‌فرض آن، در صورتی که نشانی IPv4 نداشته باشد، استفاده می‌کند. می‌توانید '::' را مشخص کنید تا نشانی IPv6 پیش‌فرض به نشانی IPv4 پیش‌فرض ترجیح داده شود. اگر cloud-provider روی external تنظیم شده باشد، این پرچم به راه‌اندازی اولیه (bootstrap) نود با IP متناظر کمک می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--node-labels &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برچسب‌هایی که هنگام ثبت نود در کلاستر افزوده می‌شوند. برچسب‌ها باید جفت‌های key=value باشند که با ',' از هم جدا شده‌اند. برچسب‌ها در فضای نام 'kubernetes.io' باید با یک پیشوند مجاز (kubelet.kubernetes.io، node.kubernetes.io) شروع شوند یا در مجموعه مجاز مشخص‌شده باشند (beta.kubernetes.io/arch، beta.kubernetes.io/instance-type، beta.kubernetes.io/os، failure-domain.beta.kubernetes.io/region، failure-domain.beta.kubernetes.io/zone، kubernetes.io/arch، kubernetes.io/hostname، kubernetes.io/os، node.kubernetes.io/instance-type، topology.kubernetes.io/region، topology.kubernetes.io/zone)</p></td>
</tr>

<tr>
<td colspan="2">--node-status-max-images int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 50</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد ایمیج‌هایی که در Node.Status.Images گزارش می‌شوند. اگر -1 مشخص شود، هیچ سقفی اعمال نخواهد شد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--node-status-update-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند kubelet هر چند وقت یک‌بار وضعیت نود را به master ارسال کند. توجه: هنگام تغییر این مقدار ثابت احتیاط کنید؛ این مقدار باید با nodeMonitorGracePeriod در nodecontroller سازگار باشد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--oom-score-adj int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: -999</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار oom-score-adj برای فرایند kubelet. مقادیر باید در بازه [-1000, 1000] باشند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--pod-cidr string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>CIDR مورد استفاده برای نشانی‌های IP پادها، که فقط در حالت مستقل (standalone) به کار می‌رود. در حالت کلاستر، این مقدار از master دریافت می‌شود. برای IPv6، حداکثر تعداد IPهای اختصاص‌یافته 65536 است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config کوبلت مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--pod-manifest-path string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری حاوی فایل‌های static pod که باید اجرا شوند، یا مسیر یک فایل static pod منفرد. فایل‌هایی که نام آن‌ها با نقطه شروع می‌شود نادیده گرفته می‌شوند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--pod-max-pids int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: -1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر تعداد پردازه‌ها به‌ازای هر Pod را تعیین می‌کند. اگر مقدار آن -1 باشد، kubelet به‌طور پیش‌فرض از ظرفیت pid قابل تخصیص نود استفاده می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--pods-per-core int32</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد Podهایی که به‌ازای هر هسته می‌توانند روی این kubelet اجرا شوند. مجموع Podها روی این kubelet نمی‌تواند از max-pods بیشتر شود؛ بنابراین اگر این محاسبه به تعداد Pod مجاز بیشتری روی kubelet منجر شود، از max-pods استفاده خواهد شد. مقدار 0 این محدودیت را غیرفعال می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10250</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورتی که kubelet روی آن سرویس‌دهی می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--protect-kernel-defaults</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>رفتار پیش‌فرض kubelet برای تنظیم هسته. اگر این گزینه تنظیم شود و هر یک از پارامترهای قابل تنظیم هسته با مقادیر پیش‌فرض kubelet متفاوت باشد، kubelet خطا می‌دهد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--provider-id string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسه یکتا برای شناسایی نود در پایگاه داده ماشین‌ها، یعنی cloudprovider.</p></td>
</tr>

<tr>
<td colspan="2">--qos-reserved &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>&lt;هشدار: قابلیت آلفا&gt; مجموعه‌ای از جفت‌های ResourceName=Percentage (مثلاً memory=50%) که توضیح می‌دهد درخواست‌های منابع Pod در سطح QoS چگونه رزرو می‌شوند. در حال حاضر فقط memory پشتیبانی می‌شود. فعال بودن feature gate با نام QOSReserved الزامی است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--read-only-port int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10255</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورت فقط‌خواندنی که kubelet بدون احراز هویت/مجوزدهی روی آن سرویس‌دهی می‌کند (برای غیرفعال کردن، مقدار 0 را تنظیم کنید). (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--register-node&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نود را در apiserver ثبت می‌کند. اگر <code>--kubeconfig</code> ارائه نشده باشد، این فلگ بی‌اثر است، زیرا kubelet هیچ apiserver‌ای برای ثبت‌نام در اختیار نخواهد داشت. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--register-with-taints []v1.Taint</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نود را با فهرست داده‌شده‌ای از taintها ثبت می‌کند (جداشده با ویرگول، به‌صورت &quot;&lt;key&gt;=&lt;value&gt;:&lt;effect&gt;&quot;). اگر register-node برابر false باشد، بی‌اثر است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--registry-burst int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر اندازه pullهای ناگهانی (bursty). به‌طور موقت اجازه می‌دهد pullها تا این تعداد افزایش ناگهانی داشته باشند، بدون آنکه از registry-qps فراتر روند. فقط در صورتی استفاده می‌شود که <code>--registry-qps</code> &gt; 0 باشد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--registry-qps int32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار بزرگ‌تر از 0 باشد، QPS دریافت (pull) از registry را به این مقدار محدود می‌کند. اگر 0 باشد، محدودیتی وجود ندارد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--reserved-cpus string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با ویرگول از CPUها یا بازه‌های CPU که برای استفاده سیستم و کوبرنتیز رزرو شده‌اند. این فهرست مشخص بر تعداد CPU تعیین‌شده در <code>--system-reserved</code> و <code>--kube-reserved</code> اولویت دارد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--reserved-memory reserved-memory</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با ویرگول از رزروهای حافظه برای نودهای NUMA (مثلاً <code>--reserved-memory 0:memory=1Gi,hugepages-1M=2Gi --reserved-memory 1:memory=2Gi</code>). مجموع کل برای هر نوع حافظه باید برابر با مجموع kube-reserved، system-reserved و eviction-threshold باشد. برای جزئیات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/#reserved-memory-flag مراجعه کنید. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--resolv-conf string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/etc/resolv.conf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل پیکربندی resolver که به‌عنوان مبنای پیکربندی تفکیک DNS کانتینرها استفاده می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--root-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/var/lib/kubelet"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر دایرکتوری برای مدیریت فایل‌های kubelet (مانت‌های حجم (volume) و غیره).</p></td>
</tr>

<tr>
<td colspan="2">--rotate-certificates</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گواهی‌های کلاینت kubelet را هنگام نزدیک شدن به زمان انقضا، با درخواست گواهی‌های جدید از kube-apiserver به‌طور خودکار چرخش (rotate) می‌دهد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--rotate-server-certificates</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گواهی‌های سرویس‌دهی kubelet را هنگام نزدیک شدن به زمان انقضا، با درخواست گواهی‌های جدید از kube-apiserver به‌طور خودکار درخواست و چرخش می‌دهد. فعال بودن feature gate با نام RotateKubeletServerCertificate و تأیید آبجکت‌های CertificateSigningRequest ارسال‌شده الزامی است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--runonce</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، پس از ایجاد Podها از فایل‌های static pod یا URLهای راه دور، خارج می‌شود. با <code>--enable-server</code> ناسازگار است (استفاده هم‌زمان ممکن نیست). (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--runtime-cgroups string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مطلق اختیاری cgroupها برای ایجاد و اجرای runtime در آن‌ها.</p></td>
</tr>

<tr>
<td colspan="2">--runtime-request-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>زمان انتظار (timeout) همه درخواست‌های runtime به‌جز درخواست‌های طولانی‌مدت، یعنی pull، logs، exec و attach. هنگام عبور از این مهلت، kubelet درخواست را لغو می‌کند، خطا برمی‌گرداند و بعداً دوباره تلاش می‌کند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--seccomp-default RuntimeDefault</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>استفاده از RuntimeDefault را به‌عنوان پروفایل پیش‌فرض seccomp برای همه بارهای کاری فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--serialize-image-pulls&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>ایمیج‌ها را یکی‌یکی دریافت (pull) می‌کند. توصیه می‌کنیم مقدار پیش‌فرض را روی نودهایی که docker daemon با نسخه &lt; 1.9 یا پشتیبان ذخیره‌سازی Aufs اجرا می‌کنند، تغییر <em>ندهید</em>. جزئیات بیشتر در Issue #10959 آمده است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--streaming-connection-idle-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 4h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر مدتی که یک اتصال جریانی (streaming) می‌تواند بیکار باشد، پیش از آنکه اتصال به‌طور خودکار بسته شود. مقدار 0 به معنای نبود محدودیت زمانی است. مثال: '5m'. توجه: همه اتصال‌ها به سرور kubelet حداکثر مدت‌زمان 4 ساعت دارند. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--sync-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر فاصله زمانی بین همگام‌سازی کانتینرهای در حال اجرا و پیکربندی. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--system-cgroups string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مطلق اختیاری cgroupهایی که همه پردازه‌های غیرهسته‌ای که هنوز درون یک cgroup زیر '/' قرار ندارند، در آن‌ها قرار داده می‌شوند. برای نبود کانتینر، خالی بگذارید. بازگرداندن این فلگ به حالت قبل نیازمند راه‌اندازی مجدد است. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--system-reserved &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از جفت‌های ResourceName=ResourceQuantity (مثلاً cpu=200m,memory=500Mi,ephemeral-storage=1Gi,pid=1000) که منابع رزروشده برای اجزای غیرکوبرنتیزی را توصیف می‌کنند. در حال حاضر فقط cpu، memory، pid و ذخیره‌سازی موقت محلی (local ephemeral storage) برای فایل‌سیستم ریشه پشتیبانی می‌شوند. برای جزئیات بیشتر به https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ مراجعه کنید. [default=none] (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--system-reserved-cgroup string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام مطلق cgroup سطح بالا که برای مدیریت اجزای غیرکوبرنتیزی استفاده می‌شود و منابع محاسباتی آن‌ها از طریق فلگ '--system-reserved' رزرو شده است. مثال: '/system-reserved'. [default=''] (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--tls-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی گواهی x509 که برای سرویس‌دهی HTTPS استفاده می‌شود (در صورت وجود، گواهی‌های میانی پس از گواهی سرور به آن الحاق می‌شوند). اگر <code>--tls-cert-file</code> و <code>--tls-private-key-file</code> ارائه نشوند، یک گواهی و کلید خودامضا برای آدرس عمومی تولید می‌شود و در دایرکتوری تعیین‌شده با <code>--cert-dir</code> ذخیره می‌گردد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--tls-cipher-suites strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی جداشده با ویرگول از cipher suiteها برای سرور. اگر حذف شود، cipher suiteهای پیش‌فرض Go استفاده خواهند شد.<br/>مقادیر توصیه‌شده: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256.<br/>مقادیر ناامن: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_RC4_128_SHA. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--tls-min-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل نسخه TLS پشتیبانی‌شده. مقادیر ممکن: VersionTLS10, VersionTLS11, VersionTLS12, VersionTLS13 (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--tls-private-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی کلید خصوصی x509 که با <code>--tls-cert-file</code> مطابقت دارد. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با فلگ <code>--config</code> کوبلت مشخص می‌شود تنظیم شود. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--topology-manager-policy string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "none"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>سیاست Topology Manager که باید استفاده شود. مقادیر ممکن: 'none'، 'best-effort'، 'restricted'، 'single-numa-node'. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--topology-manager-policy-options &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از گزینه‌های سیاست Topology Manager به‌صورت key=value که برای تنظیم دقیق رفتار آن استفاده می‌شود. در صورت مشخص نشدن، رفتار پیش‌فرض حفظ می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--topology-manager-scope string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "container"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دامنه‌ای که راهنمایی‌های توپولوژی (topology hints) در آن اعمال می‌شوند. Topology Manager راهنمایی‌ها را از Hint Providerها جمع‌آوری می‌کند و برای تضمین پذیرش Pod آن‌ها را در دامنه تعریف‌شده اعمال می‌کند. مقادیر ممکن: 'container'، 'pod'. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">-v, --v int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عدد مربوط به سطح جزئیات لاگ‌ها</p></td>
</tr>

<tr>
<td colspan="2">--version version[=true]</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>--version و --version=raw اطلاعات نسخه را چاپ می‌کنند و خارج می‌شوند؛ --version=vX.Y.Z... نسخه گزارش‌شده را تنظیم می‌کند</p></td>
</tr>

<tr>
<td colspan="2">--vmodule pattern=N,...</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از تنظیمات pattern=N که با کاما جدا شده‌اند، برای ثبت لاگ با فیلتر بر اساس فایل (فقط برای قالب لاگ متنی کار می‌کند)</p></td>
</tr>

<tr>
<td colspan="2">--volume-plugin-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/usr/libexec/kubernetes/kubelet-plugins/volume/exec/"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر کامل دایرکتوری‌ای که برای جست‌وجوی افزونه‌های حجم (volume) شخص ثالث اضافی در آن جست‌وجو می‌شود. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

<tr>
<td colspan="2">--volume-stats-agg-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازه‌ای را مشخص می‌کند که kubelet در آن میزان استفاده از دیسک حجم‌ها را برای همه Podها و حجم‌ها محاسبه و ذخیره موقت (cache) می‌کند. برای غیرفعال کردن محاسبات حجم، یک عدد منفی تنظیم کنید. (منسوخ‌شده: این پارامتر باید از طریق فایل پیکربندی که با پرچم --config مربوط به Kubelet مشخص می‌شود تنظیم گردد. برای اطلاعات بیشتر به https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/ مراجعه کنید.)</p></td>
</tr>

</tbody>
</table>
