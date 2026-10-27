---
title: kube-apiserver
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


سرور API کوبرنتیز داده‌های آبجکت‌های API را که شامل Podها، Serviceها، replicationcontrollerها و موارد دیگر است، اعتبارسنجی و پیکربندی می‌کند. سرور API عملیات REST را سرویس‌دهی می‌کند و رابط کاربری (frontend) وضعیت مشترک کلاستر را فراهم می‌آورد که تمام اجزای دیگر از طریق آن با یکدیگر تعامل دارند.

```
kube-apiserver [flags]
```

## {{% heading "options" %}}

   <table style="width: 100%; table-layout: fixed;">
<colgroup>
<col span="1" style="width: 10px;" />
<col span="1" />
</colgroup>
<tbody>

<tr>
<td colspan="2">--admission-control strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فرایند Admission به دو مرحله تقسیم می‌شود. در مرحله اول فقط افزونه‌های admission از نوع mutating اجرا می‌شوند و در مرحله دوم فقط افزونه‌های admission از نوع validating اجرا می‌شوند. نام‌های فهرست زیر ممکن است نشان‌دهنده یک افزونه validating، یک افزونه mutating یا هر دو باشند. ترتیبی که افزونه‌ها به این فلگ داده می‌شوند اهمیتی ندارد. فهرستی که با کاما جدا شده است از: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, CertificateApproval, CertificateSigning, CertificateSubjectRestriction, ClusterTrustBundleAttest, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, DenyServiceExternalIPs, EventRateLimit, ExtendedResourceToleration, ImagePolicyWebhook, LimitPodHardAntiAffinityTopology, LimitRanger, MutatingAdmissionPolicy, MutatingAdmissionWebhook, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeDeclaredFeatureValidator, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PodGroupProtection, PodNodeSelector, PodResizeValidator, PodSecurity, PodTolerationRestriction, PodTopologyLabels, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook. (منسوخ‌شده: به‌جای آن از --enable-admission-plugins یا --disable-admission-plugins استفاده کنید. در نسخه‌ای در آینده حذف خواهد شد.)</p></td>
</tr>

<tr>
<td colspan="2">--admission-control-config-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی پیکربندی admission control.</p></td>
</tr>

<tr>
<td colspan="2">--advertise-address string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آدرس IP که apiserver از طریق آن به اعضای کلاستر اعلام می‌شود. این آدرس باید برای سایر اجزای کلاستر قابل دسترسی باشد. اگر خالی باشد، از --bind-address استفاده می‌شود. اگر --bind-address نیز مشخص نشده باشد، از اینترفیس پیش‌فرض میزبان استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--aggregator-reject-forwarding-redirect&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>Aggregator پاسخ‌های ریدایرکتِ هدایت‌شده را به کلاینت برنمی‌گرداند و آن‌ها را رد می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--allow-metric-labels stringToString&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: []</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نگاشتی از برچسب متریک (metric-label) به فهرست مقادیر مجاز آن برچسب. قالب کلید به‌صورت &lt;MetricName&gt;,&lt;LabelName&gt; است. قالب مقدار به‌صورت &lt;allowed_value&gt;,&lt;allowed_value&gt;... است؛ برای مثال metric1,label1='v1,v2,v3', metric1,label2='v1,v2,v3' metric2,label1='v1,v2,v3'.</p></td>
</tr>

<tr>
<td colspan="2">--allow-metric-labels-manifest string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل مانیفستی که نگاشت فهرست مجاز را در بر دارد. قالب فایل مانند فلگ --allow-metric-labels است، یعنی:<br/>allowListMapping:<br/>&quot;metric1,label1&quot;: &quot;value11,value12&quot;<br/>&quot;metric2,label2&quot;: &quot;&quot;<br/>توجه داشته باشید که فلگ --allow-metric-labels بر فایل مانیفست اولویت دارد و آن را بازنویسی می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--allow-privileged</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، کانتینرهای privileged مجاز هستند. [پیش‌فرض=false]</p></td>
</tr>

<tr>
<td colspan="2">--anonymous-auth&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>درخواست‌های ناشناس (anonymous) را به پورت امن API server فعال می‌کند. درخواست‌هایی که توسط روش احراز هویت دیگری رد نشوند، به‌عنوان درخواست ناشناس در نظر گرفته می‌شوند. درخواست‌های ناشناس نام کاربری system:anonymous و نام گروه system:unauthenticated دارند.</p></td>
</tr>

<tr>
<td colspan="2">--api-audiences strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسه‌های API. احراز‌کننده هویت توکن service account بررسی می‌کند که توکن‌های استفاده‌شده در برابر API دست‌کم به یکی از این audienceها مقید (bound) باشند. اگر فلگ --service-account-issuer پیکربندی شده باشد و این فلگ پیکربندی نشده باشد، مقدار پیش‌فرض این فیلد فهرستی تک‌عضوی حاوی URL صادرکننده (issuer) است.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-batch-buffer-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10000</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اندازه بافر برای نگهداری رویدادها پیش از دسته‌بندی و نوشتن. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-batch-max-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه یک دسته (batch). فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-batch-max-wait duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از نوشتن اجباری دسته‌ای که به بیشینه اندازه نرسیده است. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-batch-throttle-burst int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد درخواست‌هایی که هم‌زمان ارسال می‌شوند، در صورتی که ThrottleQPS پیش‌تر مورد استفاده قرار نگرفته باشد. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-batch-throttle-enable</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا محدودسازی نرخ (throttling) دسته‌ها فعال است یا خیر. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-batch-throttle-qps float</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه میانگین تعداد دسته‌ها در هر ثانیه. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-compress</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، فایل‌های لاگِ چرخش‌یافته (rotated) با gzip فشرده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-format string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "json"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب ذخیره‌سازی رویدادهای audit. مقدار &quot;legacy&quot; نشان‌دهنده قالب متنی تک‌خطی برای هر رویداد است. مقدار &quot;json&quot; نشان‌دهنده قالب ساختاریافته json است. قالب‌های شناخته‌شده legacy و json هستند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-maxage int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 366</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد روزی که فایل‌های قدیمی لاگ audit بر اساس زمان‌سنجی (timestamp) کدگذاری‌شده در نام فایل نگهداری می‌شوند. مقدار 0 به این معناست که فایل‌های قدیمی لاگ audit بر اساس سن حذف نمی‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-maxbackup int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد فایل‌های قدیمی لاگ audit که نگهداری می‌شوند. مقدار 0 به این معناست که محدودیتی برای تعداد فایل‌ها وجود ندارد.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-maxsize int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 100</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه فایل لاگ audit بر حسب مگابایت پیش از آنکه چرخش (rotate) داده شود. مقدار 0 چرخش را غیرفعال می‌کند (توصیه نمی‌شود).</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-mode string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "blocking"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهبرد ارسال رویدادهای audit. حالت Blocking به این معناست که ارسال رویدادها پاسخ‌های سرور را مسدود می‌کند. حالت Batch باعث می‌شود backend رویدادها را بافر کند و به‌صورت ناهمگام بنویسد. حالت‌های شناخته‌شده batch و blocking و blocking-strict هستند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-path string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، تمام درخواست‌هایی که به apiserver می‌رسند در این فایل ثبت می‌شوند. مقدار '-' به معنای خروجی استاندارد (standard out) است.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-truncate-enabled</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا کوتاه‌سازی (truncating) رویداد و دسته فعال است یا خیر.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-truncate-max-batch-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10485760</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه دسته‌ای که به backend زیرین ارسال می‌شود. اندازه واقعی سریال‌شده می‌تواند چند صد بایت بیشتر باشد. اگر یک دسته از این حد فراتر رود، به چند دسته با اندازه کوچک‌تر تقسیم می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-truncate-max-event-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 102400</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه رویداد audit که به backend زیرین ارسال می‌شود. اگر اندازه یک رویداد از این عدد بیشتر باشد، ابتدا درخواست و پاسخ حذف می‌شوند و اگر این کار اندازه را به‌اندازه کافی کاهش ندهد، رویداد دور انداخته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-log-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "audit.k8s.io/v1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروه و نسخه API که برای سریال‌سازی رویدادهای audit نوشته‌شده در لاگ استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-policy-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایلی که پیکربندی سیاست audit را تعریف می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-batch-buffer-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10000</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اندازه بافر برای نگهداری رویدادها پیش از دسته‌بندی و نوشتن. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-batch-max-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 400</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه یک دسته (batch). فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-batch-max-wait duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از نوشتن اجباری دسته‌ای که به بیشینه اندازه نرسیده است. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-batch-throttle-burst int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد درخواست‌هایی که هم‌زمان ارسال می‌شوند، در صورتی که ThrottleQPS پیش‌تر مورد استفاده قرار نگرفته باشد. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-batch-throttle-enable&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا محدودسازی نرخ (throttling) دسته‌ها فعال است یا خیر. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-batch-throttle-qps float&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه میانگین تعداد دسته‌ها در هر ثانیه. فقط در حالت batch استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-config-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایلی با قالب kubeconfig که پیکربندی webhook مربوط به audit را تعریف می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-initial-backoff duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان انتظار پیش از تلاش مجدد برای نخستین درخواست ناموفق.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-mode string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "batch"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهبرد ارسال رویدادهای audit. حالت Blocking به این معناست که ارسال رویدادها پاسخ‌های سرور را مسدود می‌کند. حالت Batch باعث می‌شود backend رویدادها را بافر کند و به‌صورت ناهمگام بنویسد. حالت‌های شناخته‌شده batch و blocking و blocking-strict هستند.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-truncate-enabled</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا کوتاه‌سازی (truncating) رویداد و دسته فعال است یا خیر.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-truncate-max-batch-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10485760</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه دسته‌ای که به backend زیرین ارسال می‌شود. اندازه واقعی سریال‌شده می‌تواند چند صد بایت بیشتر باشد. اگر یک دسته از این حد فراتر رود، به چند دسته با اندازه کوچک‌تر تقسیم می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-truncate-max-event-size int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 102400</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه اندازه رویداد audit که به backend زیرین ارسال می‌شود. اگر اندازه یک رویداد از این عدد بیشتر باشد، ابتدا درخواست و پاسخ حذف می‌شوند و اگر این کار اندازه را به‌اندازه کافی کاهش ندهد، رویداد دور انداخته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--audit-webhook-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "audit.k8s.io/v1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گروه و نسخه API که برای سریال‌سازی رویدادهای audit نوشته‌شده در webhook استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی پیکربندی احراز هویت (Authentication Configuration) برای پیکربندی احراز‌کننده هویت JWT Token یا احراز‌کننده هویت ناشناس (anonymous). اگر فایل، احراز‌کننده JWT Token را پیکربندی کند، این فلگ با فلگ‌های --oidc-* هم‌زمان قابل استفاده نیست. اگر فایل، احراز‌کننده Anonymous را پیکربندی کند، این فلگ با --anonymous-auth هم‌زمان قابل استفاده نیست.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-cache-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های webhook احراز‌کننده هویت توکن در حافظه نهان (cache).</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-config-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی پیکربندی webhook برای احراز هویت توکن با قالب kubeconfig. API server برای تعیین احراز هویت bearer tokenها از سرویس راه دور پرس‌وجو می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--authentication-token-webhook-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "v1beta1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه API مربوط به TokenReview در authentication.k8s.io که به webhook ارسال می‌شود و از آن انتظار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی پیکربندی مجوزدهی (Authorization Configuration) برای پیکربندی زنجیره authorizerها. این فلگ با سایر فلگ‌های --authorization-mode و --authorization-webhook-* هم‌زمان قابل استفاده نیست.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-mode strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مرتب‌شده‌ای از افزونه‌ها برای انجام مجوزدهی روی پورت امن. اگر --authorization-config استفاده نشود، مقدار پیش‌فرض AlwaysAllow است. فهرستی که با کاما جدا شده است از: AlwaysAllow,AlwaysDeny,ABAC,Webhook,RBAC,Node.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-policy-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی سیاست مجوزدهی با قالب json خط‌به‌خط که همراه با --authorization-mode=ABAC روی پورت امن استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-authorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های 'authorized' از webhook مجوزدهنده (authorizer) در حافظه نهان (cache).</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-cache-unauthorized-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری پاسخ‌های 'unauthorized' از webhook مجوزدهنده (authorizer) در حافظه نهان (cache).</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-config-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل حاوی پیکربندی webhook با قالب kubeconfig که همراه با --authorization-mode=Webhook استفاده می‌شود. API server برای تعیین دسترسی روی پورت امن API server از سرویس راه دور پرس‌وجو می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--authorization-webhook-version string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "v1beta1"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخهٔ API مربوط به SubjectAccessReview از گروه authorization.k8s.io که باید به webhook ارسال شود و از آن انتظار می‌رود.</p></td>
</tr>

<tr>
<td colspan="2">--bind-address string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 0.0.0.0</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>آدرس IP که برای گوش دادن روی پورت --secure-port استفاده می‌شود. اینترفیس‌های مرتبط باید برای بقیهٔ کلاستر و برای کلاینت‌های CLI/وب در دسترس باشند. اگر خالی باشد یا یک آدرس نامشخص (0.0.0.0 یا ::) باشد، همهٔ اینترفیس‌ها و خانواده‌های آدرس IP استفاده خواهند شد.</p></td>
</tr>

<tr>
<td colspan="2">--cert-dir string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/var/run/kubernetes"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دایرکتوری که گواهی‌های TLS در آن قرار دارند. اگر --tls-cert-file و --tls-private-key-file تعیین شده باشند، این فلگ نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تنظیم، هر درخواستی که گواهی کلاینتی را ارائه کند که توسط یکی از مراجع موجود در client-ca-file امضا شده باشد، با هویتی متناظر با CommonName آن گواهی کلاینت احراز هویت می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--contention-profiling</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورتی که profiling فعال باشد، block profiling را فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--coordinated-leadership-lease-duration duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 15s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان lease مورد استفاده برای انتخاب رهبر هماهنگ‌شده (Coordinated Leader Election).</p></td>
</tr>

<tr>
<td colspan="2">--coordinated-leadership-renew-deadline duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 10s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت تمدید lease در انتخاب رهبر هماهنگ‌شده.</p></td>
</tr>

<tr>
<td colspan="2">--coordinated-leadership-retry-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصلهٔ زمانی تلاش مجدد برای تمدید lease در انتخاب رهبر هماهنگ‌شده.</p></td>
</tr>

<tr>
<td colspan="2">--cors-allowed-origins strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست originهای مجاز برای CORS که با ویرگول از هم جدا شده‌اند. یک origin مجاز می‌تواند یک عبارت باقاعده (regular expression) باشد تا تطبیق زیردامنه‌ها را پشتیبانی کند. اگر این فهرست خالی باشد، CORS فعال نخواهد شد. لطفاً اطمینان حاصل کنید که هر عبارت کل نام میزبان را تطبیق می‌دهد؛ برای این کار، ابتدای آن را با '^' یا با گنجاندن پیشوند '//' و انتهای آن را با '$' یا با گنجاندن پسوند جداکنندهٔ پورت ':' مقید کنید. نمونه‌هایی از عبارت‌های معتبر عبارت‌اند از '//example.com(:|$)' و '^https://example.com(:|$)'</p></td>
</tr>

<tr>
<td colspan="2">--debug-socket-path string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای profiling از یک سوکت دامنهٔ یونیکس محافظت‌نشده (بدون authn/authz) با مسیر داده‌شده استفاده می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--default-not-ready-toleration-seconds int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 300</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار tolerationSeconds را برای toleration مربوط به notReady:NoExecute مشخص می‌کند که به‌طور پیش‌فرض به هر Pod که قبلاً چنین toleration ای نداشته باشد افزوده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--default-unreachable-toleration-seconds int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 300</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مقدار tolerationSeconds را برای toleration مربوط به unreachable:NoExecute مشخص می‌کند که به‌طور پیش‌فرض به هر Pod که قبلاً چنین toleration ای نداشته باشد افزوده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--delete-collection-workers int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تعداد workerهایی که برای فراخوانی DeleteCollection ایجاد می‌شوند. این workerها برای سرعت‌بخشیدن به پاک‌سازی فضای نام (namespace) استفاده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--disable-admission-plugins strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>افزونه‌های admission که باید غیرفعال شوند، هرچند در فهرست افزونه‌های فعال پیش‌فرض قرار دارند (NamespaceLifecycle, LimitRanger, ServiceAccount, TaintNodesByCondition, PodSecurity, Priority, DefaultTolerationSeconds, DefaultStorageClass, StorageObjectInUseProtection, PodGroupProtection, PersistentVolumeClaimResize, RuntimeClass, CertificateApproval, CertificateSigning, ClusterTrustBundleAttest, CertificateSubjectRestriction, DefaultIngressClass, PodTopologyLabels, NodeDeclaredFeatureValidator, PodResizeValidator, MutatingAdmissionPolicy, MutatingAdmissionWebhook, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook, ResourceQuota). فهرست افزونه‌های admission که با ویرگول جدا می‌شوند: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, CertificateApproval, CertificateSigning, CertificateSubjectRestriction, ClusterTrustBundleAttest, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, DenyServiceExternalIPs, EventRateLimit, ExtendedResourceToleration, ImagePolicyWebhook, LimitPodHardAntiAffinityTopology, LimitRanger, MutatingAdmissionPolicy, MutatingAdmissionWebhook, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeDeclaredFeatureValidator, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PodGroupProtection, PodNodeSelector, PodResizeValidator, PodSecurity, PodTolerationRestriction, PodTopologyLabels, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook. ترتیب افزونه‌ها در این فلگ اهمیتی ندارد.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>این فلگ راه گریزی برای متریک‌های دارای رفتار نادرست فراهم می‌کند. برای غیرفعال‌کردن یک متریک باید نام کاملاً مشخص (fully qualified) آن را ارائه کنید. توجه: غیرفعال‌کردن متریک‌ها اولویت بالاتری از نمایش متریک‌های پنهان دارد.</p></td>
</tr>

<tr>
<td colspan="2">--egress-selector-config-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل پیکربندی egress selector مربوط به apiserver.</p></td>
</tr>

<tr>
<td colspan="2">--emulated-version strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه‌هایی که اجزای مختلف قابلیت‌های خود (APIها، ویژگی‌ها و ...) را بر اساس آن شبیه‌سازی می‌کنند.<br/>در صورت تنظیم، جزء مورد نظر به‌جای نسخهٔ باینری زیرین، رفتار این نسخه را شبیه‌سازی می‌کند.<br/>قالب نسخه فقط می‌تواند major.minor باشد، برای مثال: '--emulated-version=wardle=1.2,kube=1.31'.<br/>گزینه‌ها عبارت‌اند از: kube=1.34..1.37(default:1.37)<br/>اگر جزء مشخص نشده باشد، مقدار پیش‌فرض &quot;kube&quot; است</p></td>
</tr>

<tr>
<td colspan="2">--emulation-forward-compatible</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، برای هر API در سطح بتا یا بالاتر که به‌طور پیش‌فرض یا از طریق --runtime-config در نسخهٔ شبیه‌سازی فعال است، نسخه‌های آیندهٔ آن با اولویت/پایداری بالاتر نیز به‌طور خودکار فعال می‌شوند، حتی اگر پس از نسخهٔ شبیه‌سازی معرفی شده باشند. فقط زمانی می‌توان آن را true قرار داد که نسخهٔ شبیه‌سازی پایین‌تر از نسخهٔ باینری باشد.</p></td>
</tr>

<tr>
<td colspan="2">--enable-admission-plugins strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>افزونه‌های admission که باید علاوه بر افزونه‌های فعال پیش‌فرض فعال شوند (NamespaceLifecycle, LimitRanger, ServiceAccount, TaintNodesByCondition, PodSecurity, Priority, DefaultTolerationSeconds, DefaultStorageClass, StorageObjectInUseProtection, PodGroupProtection, PersistentVolumeClaimResize, RuntimeClass, CertificateApproval, CertificateSigning, ClusterTrustBundleAttest, CertificateSubjectRestriction, DefaultIngressClass, PodTopologyLabels, NodeDeclaredFeatureValidator, PodResizeValidator, MutatingAdmissionPolicy, MutatingAdmissionWebhook, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook, ResourceQuota). فهرست افزونه‌های admission که با ویرگول جدا می‌شوند: AlwaysAdmit, AlwaysDeny, AlwaysPullImages, CertificateApproval, CertificateSigning, CertificateSubjectRestriction, ClusterTrustBundleAttest, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, DenyServiceExternalIPs, EventRateLimit, ExtendedResourceToleration, ImagePolicyWebhook, LimitPodHardAntiAffinityTopology, LimitRanger, MutatingAdmissionPolicy, MutatingAdmissionWebhook, NamespaceAutoProvision, NamespaceExists, NamespaceLifecycle, NodeDeclaredFeatureValidator, NodeRestriction, OwnerReferencesPermissionEnforcement, PersistentVolumeClaimResize, PodGroupProtection, PodNodeSelector, PodResizeValidator, PodSecurity, PodTolerationRestriction, PodTopologyLabels, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook. ترتیب افزونه‌ها در این فلگ اهمیتی ندارد.</p></td>
</tr>

<tr>
<td colspan="2">--enable-aggregator-routing</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیریابی درخواست‌های aggregator را به‌جای IP کلاستر، به IP نقاط پایانی (endpoints) فعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--enable-bootstrap-token-auth</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فعال می‌کند تا Secretهایی از نوع 'bootstrap.kubernetes.io/token' در فضای نام (namespace) 'kube-system' بتوانند برای احراز هویت در TLS bootstrapping استفاده شوند.</p></td>
</tr>

<tr>
<td colspan="2">--enable-garbage-collector&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>garbage collector عمومی را فعال می‌کند. حتماً باید با فلگ متناظر در kube-controller-manager همگام باشد.</p></td>
</tr>

<tr>
<td colspan="2">--enable-logs-handler</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، یک handler با مسیر /logs برای لاگ‌های apiserver نصب می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--enable-priority-and-fairness&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، handler مربوط به max-in-flight با یک handler پیشرفته‌تر جایگزین می‌شود که درخواست‌ها را با رعایت اولویت و انصاف (priority and fairness) در صف قرار می‌دهد و توزیع می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--encryption-provider-config string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی حاوی پیکربندی ارائه‌دهندگان رمزنگاری که برای ذخیرهٔ Secretها در etcd استفاده می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--encryption-provider-config-automatic-reload</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مشخص می‌کند که آیا فایل تعیین‌شده با --encryption-provider-config در صورت تغییر محتوای دیسک باید به‌طور خودکار بارگذاری مجدد شود یا خیر. تنظیم این گزینه روی true توانایی شناسایی یکتای افزونه‌های KMS مجزا از طریق endpointهای healthz سرور API را غیرفعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--endpoint-reconciler-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "lease"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>از یک endpoint reconciler استفاده می‌کند (master-count, lease, none). master-count منسوخ شده است و در نسخه‌ای آینده حذف خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-cafile string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل مرجع صدور گواهی SSL که برای ایمن‌سازی ارتباط با etcd استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-certfile string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل گواهی SSL که برای ایمن‌سازی ارتباط با etcd استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-compaction-interval duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصلهٔ زمانی درخواست‌های compaction. اگر 0 باشد، درخواست compaction از سوی apiserver غیرفعال است.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-count-metric-poll-period duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>دفعات پرس‌وجو از etcd برای دریافت تعداد منابع به‌ازای هر نوع. مقدار 0 جمع‌آوری این متریک را غیرفعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-db-metric-poll-interval duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فاصلهٔ زمانی درخواست‌ها برای پرس‌وجو از etcd و به‌روزرسانی متریک. مقدار 0 جمع‌آوری این متریک را غیرفعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-healthcheck-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت زمانی که هنگام بررسی سلامت etcd استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-keyfile string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل کلید SSL که برای ایمن‌سازی ارتباط با etcd استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-prefix string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "/registry"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پیشوندی که به ابتدای تمام مسیرهای منابع در etcd افزوده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-readycheck-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 2s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت زمانی که هنگام بررسی آمادگی etcd استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-servers strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست سرورهای etcd برای اتصال (scheme://ip:port) که با ویرگول از هم جدا شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--etcd-servers-overrides strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بازنویسی (override) سرورهای etcd به‌ازای هر منبع، که با ویرگول از هم جدا می‌شوند. قالب هر override به این صورت است: group/resource#servers، که در آن servers نشانی‌های URL هستند که با نقطه‌ویرگول از هم جدا می‌شوند. توجه کنید که این مورد فقط برای منابعی اعمال می‌شود که در این باینری سرور کامپایل شده‌اند. برای مثال: &quot;/pods#http://etcd4:2379;http://etcd5:2379,/events#http://etcd6:2379&quot;</p></td>
</tr>

<tr>
<td colspan="2">--event-ttl duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1h0m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان نگهداری رویدادها (events).</p></td>
</tr>

<tr>
<td colspan="2">--external-hostname string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نام میزبانی که هنگام تولید URLهای خارجی برای این master استفاده می‌شود (برای مثال Swagger API Docs یا OpenID Discovery).</p></td>
</tr>

<tr>
<td colspan="2">--feature-gates colonSeparatedMultimapStringString</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از جفت‌های component:key=value که با ویرگول از هم جدا شده‌اند و feature gateهای مربوط به ویژگی‌های آلفا/آزمایشی اجزای مختلف را توصیف می‌کنند.<br/>اگر جزء مشخص نشده باشد، مقدار پیش‌فرض &quot;kube&quot; است. این فلگ را می‌توان چندین بار تکرار کرد. برای مثال: --feature-gates 'wardle:featureA=true,wardle:featureB=false' --feature-gates 'kube:featureC=true'. گزینه‌ها عبارت‌اند از:<br/>kube:APIResponseCompression=true|false (BETA - default=true)<br/>kube:APIServerIdentity=true|false (BETA - default=true)<br/>kube:APIServerWebhookAuthenticationToken=true|false (ALPHA - default=false)<br/>kube:APIServingWithRoutine=true|false (ALPHA - default=false)<br/>kube:AllAlpha=true|false (ALPHA - default=false)<br/>kube:AllBeta=true|false (BETA - default=false)<br/>kube:AllowParsingUserUIDFromCertAuth=true|false (BETA - default=true)<br/>kube:AllowUnsafeMalformedObjectDeletion=true|false (BETA - default=true)<br/>kube:AtomicFIFO=true|false (BETA - default=true)<br/>kube:AtomicWriteVolumeUserFields=true|false (ALPHA - default=false)<br/>kube:AuthorizePodWebsocketUpgradeCreatePermission=true|false (BETA - default=true)<br/>kube:CBORServingAndStorage=true|false (ALPHA - default=false)<br/>kube:CPUManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>kube:CPUManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>kube:CRDObservedGenerationTracking=true|false (BETA - default=true)<br/>kube:CRIListStreaming=true|false (ALPHA - default=false)<br/>kube:CSIVolumeHealth=true|false (ALPHA - default=false)<br/>kube:ClearingNominatedNodeNameAfterBinding=true|false (BETA - default=true)<br/>kube:ClientsAllowCARotation=true|false (BETA - default=true)<br/>kube:ClientsAllowCBOR=true|false (ALPHA - default=false)<br/>kube:ClientsAllowTLSCacheGC=true|false (BETA - default=true)<br/>kube:ClientsPreferCBOR=true|false (ALPHA - default=false)<br/>kube:CloudControllerManagerWatchBasedRoutesReconciliation=true|false (ALPHA - default=false)<br/>kube:CloudControllerManagerWebhook=true|false (ALPHA - default=false)<br/>kube:ComponentFlagz=true|false (BETA - default=true)<br/>kube:ComponentStatusz=true|false (BETA - default=true)<br/>kube:CompositePodGroup=true|false (ALPHA - default=false)<br/>kube:ConcurrentWatchObjectDecode=true|false (BETA - default=true)<br/>kube:ConsistentListFromCacheSkipTimeoutFallback=true|false (ALPHA - default=false)<br/>kube:ConstrainedImpersonation=true|false (BETA - default=true)<br/>kube:ContainerCheckpoint=true|false (BETA - default=true)<br/>kube:ContainerRestartRules=true|false (BETA - default=true)<br/>kube:ContainerStopSignals=true|false (ALPHA - default=false)<br/>kube:ContextualLogging=true|false (BETA - default=true)<br/>kube:ControllerManagerReleaseLeaderElectionLockOnExit=true|false (ALPHA - default=false)<br/>kube:CoordinatedLeaderElection=true|false (BETA - default=false)<br/>kube:CrossNamespaceVolumeDataSource=true|false (ALPHA - default=false)<br/>kube:DRAConsumableCapacity=true|false (BETA - default=true)<br/>kube:DRADerivedAttributes=true|false (ALPHA - default=false)<br/>kube:DRADeviceBindingConditions=true|false (BETA - default=true)<br/>kube:DRADeviceCompatibilityGroups=true|false (ALPHA - default=false)<br/>kube:DRAFractionalCapacityRange=true|false (BETA - default=false)، یا DRAFractionalCapacityRange=true|false (BETA - default=true) اگر --min-compatibility-version&gt;=1.37 باشد<br/>kube:DRAListTypeAttributes=true|false (ALPHA - default=false)<br/>kube:DRANodeAllocatableResources=true|false (ALPHA - default=false)<br/>kube:DRAOptionalNodeOperations=true|false (ALPHA - default=false)<br/>kube:DRAPartitionableDevices=true|false (BETA - default=true)<br/>kube:DRAPartitionableDevicesType=true|false (ALPHA - default=false)<br/>kube:DRAResourceClaimGranularStatusAuthorization=true|false (BETA - default=true)<br/>kube:DRAResourcePoolStatus=true|false (ALPHA - default=false)<br/>kube:DRASchedulerFilterTimeout=true|false (BETA - default=true)<br/>kube:DRAWorkloadResourceClaims=true|false (BETA - default=false)<br/>kube:DeclarativeValidationBeta=true|false (BETA - default=true)<br/>kube:DefaultPodSysctls=true|false (ALPHA - default=false)<br/>kube:DeploymentReplicaSetTerminatingReplicas=true|false (BETA - default=true)<br/>kube:DetectCacheInconsistency=true|false (BETA - default=true)<br/>kube:EmptyDirVolumeMode=true|false (ALPHA - default=false)<br/>kube:EnvFiles=true|false (BETA - default=true)<br/>kube:EtcdRangeStream=true|false (BETA - default=true)<br/>kube:EventedPLEG=true|false (ALPHA - default=false)<br/>kube:EvictionRequestAPI=true|false (ALPHA - default=false)<br/>kube:ExcludeAdmissionWebhookVirtualResources=true|false (BETA - default=true)<br/>kube:ExtendWebSocketsToKubelet=true|false (BETA - default=true)<br/>kube:GRPCContainerProbeTLS=true|false (ALPHA - default=false)<br/>kube:GenericWorkload=true|false (BETA - default=false)<br/>kube:GracefulNodeShutdown=true|false (BETA - default=true)<br/>kube:GracefulNodeShutdownBasedOnPodPriority=true|false (BETA - default=true)<br/>kube:H2CContainerProbe=true|false (ALPHA - default=false)<br/>kube:HPAGeneration=true|false (BETA - default=true)<br/>kube:HPAOptimizedSelectorStore=true|false (BETA - default=true)<br/>kube:HPAScaleToZero=true|false (BETA - default=true)<br/>kube:HugepageAwareEviction=true|false (BETA - default=true)<br/>kube:ImageVolumeWithDigest=true|false (ALPHA - default=false)<br/>kube:InOrderInformersBatchProcess=true|false (BETA - default=true)<br/>kube:InPlacePodLevelResourcesVerticalScaling=true|false (BETA - default=true)<br/>kube:InPlacePodVerticalScalingExclusiveCPUs=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingExclusiveMemory=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingMemoryBackedVolumes=true|false (ALPHA - default=false)<br/>kube:InPlacePodVerticalScalingSchedulerPreemption=true|false (ALPHA - default=false)<br/>kube:InterPodAffinityHostnameFastPath=true|false (ALPHA - default=false)<br/>kube:KubeProxyNFTablesLocalhostNodePorts=true|false (ALPHA - default=false)<br/>kube:KubeletAllocatedPodsEndpoint=true|false (ALPHA - default=false)<br/>kube:KubeletCrashLoopBackOffMax=true|false (BETA - default=true)<br/>kube:KubeletEnsureSecretPulledImages=true|false (BETA - default=true)<br/>kube:KubeletInUserNamespace=true|false (BETA - default=true)<br/>kube:KubeletSeparateDiskGC=true|false (BETA - default=true)<br/>kube:KubeletServiceAccountTokenForCredentialProviders=true|false (BETA - default=true)<br/>kube:ListFromCacheSnapshot=true|false (BETA - default=true)<br/>kube:LocalStorageCapacityIsolationFSQuotaMonitoring=true|false (BETA - default=false)<br/>kube:LoggingAlphaOptions=true|false (ALPHA - default=false)<br/>kube:LoggingBetaOptions=true|false (BETA - default=true)<br/>kube:ManifestBasedAdmissionControlConfig=true|false (BETA - default=true)<br/>kube:MatchLabelKeysInPodTopologySpread=true|false (BETA - default=true)<br/>kube:MatchLabelKeysInPodTopologySpreadSelectorMerge=true|false (BETA - default=true)<br/>kube:MaxUnavailableStatefulSet=true|false (BETA - default=true)<br/>kube:MemoryQoS=true|false (BETA - default=true)<br/>kube:MutablePVNodeAffinity=true|false (ALPHA - default=false)<br/>kube:MutablePodResourcesForSuspendedJobs=true|false (BETA - default=true)<br/>kube:MutableSchedulingDirectivesForSuspendedJobs=true|false (BETA - default=true)<br/>kube:NFTablesNetlink=true|false (BETA - default=true)<br/>kube:NativeHistograms=true|false (BETA - default=true)<br/>kube:NodeControllerLeaseCircuitBreaker=true|false (BETA - default=true)<br/>kube:NodeLifecycleConditions=true|false (ALPHA - default=false)<br/>kube:NominatedNodeNameForExpectation=true|false (BETA - default=true)<br/>kube:OpenAPIEnums=true|false (BETA - default=true)<br/>kube:OpportunisticBatching=true|false (BETA - default=true)<br/>kube:PersistentVolumeClaimUnusedSinceTime=true|false (BETA - default=true)<br/>kube:PodAndContainerStatsFromCRI=true|false (BETA - default=false)<br/>kube:PodDeletionCost=true|false (BETA - default=true)<br/>kube:PodGroupPreemptionPolicy=true|false (ALPHA - default=false)<br/>kube:PodLevelResourceManagers=true|false (BETA - default=false)<br/>kube:PodLevelResources=true|false (BETA - default=true)<br/>kube:PodLevelResourcesFixDefaulting=true|false (BETA - default=true)<br/>kube:PodLevelResourcesFixKubeletQOSClass=true|false (BETA - default=true)<br/>kube:PodLogsQuerySplitStreams=true|false (ALPHA - default=false)<br/>kube:PodTopologyLabelsAdmission=true|false (BETA - default=true)<br/>kube:PodsAPI=true|false (BETA - default=true)<br/>kube:PortForwardWebsockets=true|false (BETA - default=true)<br/>kube:QOSReserved=true|false (ALPHA - default=false)<br/>kube:ReduceDefaultCrashLoopBackOffDecay=true|false (ALPHA - default=false)<br/>kube:ReloadKubeletClientCAFile=true|false (BETA - default=true)<br/>kube:ReloadKubeletServerCertificateFile=true|false (BETA - default=true)<br/>kube:RemoteRequestHeaderUID=true|false (BETA - default=true)<br/>kube:ResourceHealthStatus=true|false (BETA - default=true)<br/>kube:ResourceHealthStatusMessage=true|false (BETA - default=true)<br/>kube:RestartAllContainersOnContainerExits=true|false (BETA - default=true)<br/>kube:RotateKubeletServerCertificate=true|false (BETA - default=true)<br/>kube:RuntimeClassInImageCriApi=true|false (ALPHA - default=false)<br/>kube:SchedulerAsyncAPICalls=true|false (BETA - default=false)<br/>kube:SchedulerAsyncPreemption=true|false (BETA - default=true)<br/>kube:SchedulerPopFromBackoffQ=true|false (BETA - default=true)<br/>kube:SchedulerPreQueueingHints=true|false (ALPHA - default=false)<br/>kube:ServiceAccountNodeAudienceRestriction=true|false (BETA - default=true)<br/>kube:ShardedListAndWatch=true|false (ALPHA - default=false)<br/>kube:SizeBasedListCostEstimate=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyDaemonSet=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyHPA=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyJob=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyReplicaSet=true|false (BETA - default=true)<br/>kube:StaleControllerConsistencyStatefulSet=true|false (BETA - default=true)<br/>kube:StatefulSetRecreateStrategy=true|false (ALPHA - default=false)<br/>kube:StatefulSetSemanticRevisionComparison=true|false (BETA - default=true)<br/>kube:StorageCapacityScoring=true|false (BETA - default=true)<br/>kube:StorageVersionAPI=true|false (ALPHA - default=false)<br/>kube:StorageVersionHash=true|false (BETA - default=true)<br/>kube:StrictIPCIDRValidation=true|false (BETA - default=true)<br/>kube:StructuredAuthenticationConfigurationEgressSelector=true|false (BETA - default=true)<br/>kube:StructuredAuthenticationConfigurationJWKSMetrics=true|false (BETA - default=true)<br/>kube:TaintTolerationComparisonOperators=true|false (ALPHA - default=false)<br/>kube:TokenRequestServiceAccountUIDValidation=true|false (BETA - default=true)<br/>kube:TopologyAwareWorkloadScheduling=true|false (ALPHA - default=false)<br/>kube:TopologyManagerPolicyAlphaOptions=true|false (ALPHA - default=false)<br/>kube:TopologyManagerPolicyBetaOptions=true|false (BETA - default=true)<br/>kube:TranslateStreamCloseWebsocketRequests=true|false (BETA - default=true)<br/>kube:UnauthenticatedHTTP2DOSMitigation=true|false (BETA - default=true)<br/>kube:UnknownVersionInteroperabilityProxy=true|false (BETA - default=true)<br/>kube:UnlockWhileProcessingFIFO=true|false (BETA - default=true)<br/>kube:UserNamespacesHostNetworkSupport=true|false (ALPHA - default=false)<br/>kube:VolumeBindMountOptions=true|false (ALPHA - default=false)<br/>kube:VolumeLimitScaling=true|false (BETA - default=true)<br/>kube:WatchList=true|false (BETA - default=true)<br/>kube:WatchListClient=true|false (BETA - default=true)<br/>kube:WatchListCompression=true|false (BETA - default=true)<br/>kube:WebhookRoundTripLoadBalancing=true|false (BETA - default=true)<br/>kube:WindowsCPUAndMemoryAffinity=true|false (ALPHA - default=false)<br/>kube:WindowsGracefulNodeShutdown=true|false (BETA - default=true)<br/>kube:WorkloadWithJob=true|false (ALPHA - default=false)</p></td>
</tr>

<tr>
<td colspan="2">--goaway-chance float</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>برای جلوگیری از گیر کردن کلاینت‌های HTTP/2 روی یک apiserver واحد، یک اتصال به‌صورت تصادفی بسته می‌شود (GOAWAY). سایر درخواست‌های در حال پردازش کلاینت تحت تأثیر قرار نمی‌گیرند و کلاینت دوباره متصل می‌شود و احتمالاً پس از عبور مجدد از load balancer به apiserver دیگری می‌رسد. این آرگومان کسری از درخواست‌ها را تعیین می‌کند که GOAWAY برای آن‌ها ارسال می‌شود. کلاسترهایی که تنها یک apiserver دارند یا از load balancer استفاده نمی‌کنند نباید این گزینه را فعال کنند. حداقل مقدار 0 (غیرفعال) و حداکثر مقدار 0.02 (یک درخواست از هر ۵۰ درخواست) است؛ مقدار 0.001 (یک درخواست از هر ۱۰۰۰ درخواست) نقطه شروع پیشنهادی است.</p></td>
</tr>

<tr>
<td colspan="2">-h, --help</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>راهنمای kube-apiserver</p></td>
</tr>

<tr>
<td colspan="2">--http2-max-streams-per-connection int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حد بیشینه تعداد streamها در یک اتصال HTTP/2 که سرور به کلاینت‌ها اعلام می‌کند. مقدار صفر به معنی استفاده از مقدار پیش‌فرض golang است.</p></td>
</tr>

<tr>
<td colspan="2">--kubelet-certificate-authority string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی مرجع صدور گواهی (certificate authority).</p></td>
</tr>

<tr>
<td colspan="2">--kubelet-client-certificate string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل گواهی کلاینت برای TLS.</p></td>
</tr>

<tr>
<td colspan="2">--kubelet-client-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایل کلید کلاینت برای TLS.</p></td>
</tr>

<tr>
<td colspan="2">--kubelet-preferred-address-types strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "Hostname,InternalDNS,InternalIP,ExternalDNS,ExternalIP"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست NodeAddressTypeهای ترجیحی برای استفاده در اتصال‌های kubelet.</p></td>
</tr>

<tr>
<td colspan="2">--kubelet-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مهلت زمانی عملیات kubelet.</p></td>
</tr>

<tr>
<td colspan="2">--kubernetes-service-node-port int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار غیرصفر باشد، سرویس master کوبرنتیز (که apiserver آن را ایجاد و نگهداری می‌کند) از نوع NodePort خواهد بود و این مقدار به‌عنوان شماره پورت آن استفاده می‌شود. اگر مقدار صفر باشد، سرویس master کوبرنتیز از نوع ClusterIP خواهد بود.</p></td>
</tr>

<tr>
<td colspan="2">--lease-reuse-duration-seconds int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 60</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان بر حسب ثانیه که هر lease دوباره استفاده می‌شود. مقدار کمتر می‌تواند از استفاده مجدد تعداد زیادی آبجکت از یک lease یکسان جلوگیری کند. توجه داشته باشید که مقدار بسیار کوچک ممکن است در لایه ذخیره‌سازی مشکلات عملکردی ایجاد کند.</p></td>
</tr>

<tr>
<td colspan="2">--livez-grace-period duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>این گزینه بیشینه مدت زمانی را مشخص می‌کند که apiserver برای تکمیل فرایند راه‌اندازی و فعال شدن (live) نیاز دارد. از زمان شروع apiserver تا سپری شدن این مدت، /livez فرض می‌کند که post-start hookهای ناتمام با موفقیت کامل خواهند شد و بنابراین مقدار true برمی‌گرداند.</p></td>
</tr>

<tr>
<td colspan="2">--log-flush-frequency duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 5s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بیشینه تعداد ثانیه‌ها between دو flush متوالی لاگ</p></td>
</tr>

<tr>
<td colspan="2">--log-text-info-buffer-size quantity</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب text با جریان‌های خروجی جداگانه، پیام‌های اطلاعاتی را می‌توان برای مدتی بافر کرد تا عملکرد افزایش یابد. مقدار پیش‌فرض صفر بایت، بافر کردن را غیرفعال می‌کند. اندازه را می‌توان به‌صورت تعداد بایت (512)، مضرب‌های ۱۰۰۰ (1K)، مضرب‌های ۱۰۲۴ (2Ki) یا توان‌های آن‌ها (3M، 4G، 5Mi، 6Gi) مشخص کرد. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--log-text-split-stream</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>[آلفا] در قالب text، پیام‌های خطا در stderr و پیام‌های اطلاعاتی در stdout نوشته می‌شوند. رفتار پیش‌فرض نوشتن همه پیام‌ها در یک جریان واحد در stdout است. برای استفاده از این گزینه، feature gate با نام LoggingAlphaOptions را فعال کنید.</p></td>
</tr>

<tr>
<td colspan="2">--logging-format string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "text"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>قالب لاگ را تعیین می‌کند. قالب‌های مجاز: &quot;text&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--max-connection-bytes-per-sec int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر مقدار غیرصفر باشد، سرعت هر اتصال کاربر به این تعداد بایت در ثانیه محدود می‌شود. در حال حاضر فقط برای درخواست‌های بلندمدت اعمال می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--max-mutating-requests-inflight int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 200</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر --enable-priority-and-fairness برابر true باشد، مجموع این مقدار و --max-requests-inflight حد کل هم‌زمانی سرور را تعیین می‌کند (که باید مثبت باشد). در غیر این صورت، این فلگ بیشینه تعداد درخواست‌های تغییردهنده (mutating) در حال پردازش را محدود می‌کند و مقدار صفر محدودیت را به‌طور کامل غیرفعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--max-requests-inflight int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 400</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر --enable-priority-and-fairness برابر true باشد، مجموع این مقدار و --max-mutating-requests-inflight حد کل هم‌زمانی سرور را تعیین می‌کند (که باید مثبت باشد). در غیر این صورت، این فلگ بیشینه تعداد درخواست‌های غیرتغییردهنده (non-mutating) در حال پردازش را محدود می‌کند و مقدار صفر محدودیت را به‌طور کامل غیرفعال می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--min-compatibility-version strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداقل نسخه مؤلفه‌های control plane که سرور باید با آن سازگار باشد.<br/>باید کمتر از emulated-version یا برابر با آن باشد. قالب نسخه فقط می‌تواند major.minor باشد، برای مثال: '--min-compatibility-version=wardle=1.2,kube=1.31'.<br/>گزینه‌ها: kube=1.34..1.37 (پیش‌فرض: 1.36)<br/>اگر مؤلفه مشخص نشود، مقدار پیش‌فرض &quot;kube&quot; است</p></td>
</tr>

<tr>
<td colspan="2">--min-request-timeout int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1800</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک فیلد اختیاری که حداقل تعداد ثانیه‌هایی را مشخص می‌کند که یک handler باید یک درخواست را پیش از اعمال مهلت زمانی باز نگه دارد. در حال حاضر فقط handler درخواست watch آن را رعایت می‌کند و برای توزیع بار، مقداری تصادفی بزرگ‌تر از این عدد را به‌عنوان مهلت زمانی اتصال انتخاب می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود، گواهی سرور OpenID توسط یکی از مراجع موجود در oidc-ca-file تأیید می‌شود؛ در غیر این صورت از مجموعه CAهای ریشه میزبان استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-client-id string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسه کلاینت (client ID) برای کلاینت OpenID Connect؛ در صورت تنظیم oidc-issuer-url باید مقداردهی شود.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-groups-claim string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، نام یک claim سفارشی OpenID Connect برای مشخص کردن گروه‌های کاربر است. مقدار claim باید یک رشته یا آرایه‌ای از رشته‌ها باشد. این فلگ آزمایشی است؛ برای جزئیات بیشتر به مستندات احراز هویت مراجعه کنید.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-groups-prefix string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، این مقدار به‌عنوان پیشوند به همه گروه‌ها افزوده می‌شود تا از تداخل با سایر راهبردهای احراز هویت جلوگیری شود.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-issuer-url string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نشانی URL صادرکننده OpenID؛ فقط طرح HTTPS پذیرفته می‌شود. در صورت تنظیم، برای تأیید توکن OIDC JSON Web Token (JWT) استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-required-claim &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک جفت key=value که یک claim الزامی در ID Token را توصیف می‌کند. در صورت تنظیم، بررسی می‌شود که این claim با مقدار متناظر در ID Token وجود داشته باشد. برای تعیین چند claim، این فلگ را تکرار کنید.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-signing-algs strings&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "RS256"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست جداشده با ویرگول از الگوریتم‌های امضای نامتقارن JOSE مجاز. JWTهایی با مقادیر پشتیبانی‌شده برای هدر 'alg' عبارت‌اند از: RS256، RS384، RS512، ES256، ES384، ES512، PS256، PS384، PS512. این مقادیر در RFC 7518 به نشانی https://tools.ietf.org/html/rfc7518#section-3.1 تعریف شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-username-claim string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "sub"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>claim OpenID که به‌عنوان نام کاربری استفاده می‌شود. توجه داشته باشید که یکتا و تغییرناپذیر بودن claimهایی غیر از مقدار پیش‌فرض ('sub') تضمین نمی‌شود. این فلگ آزمایشی است؛ برای جزئیات بیشتر به مستندات احراز هویت مراجعه کنید.</p></td>
</tr>

<tr>
<td colspan="2">--oidc-username-prefix string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تعیین، این مقدار به‌عنوان پیشوند به همه نام‌های کاربری افزوده می‌شود. اگر تعیین نشود، برای جلوگیری از تداخل، به claimهای نام کاربری غیر از 'email' نشانی URL صادرکننده به‌عنوان پیشوند افزوده می‌شود. برای صرف‌نظر از هرگونه افزودن پیشوند، مقدار '-' را تعیین کنید.</p></td>
</tr>

<tr>
<td colspan="2">--peer-advertise-ip string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود و feature gate با نام UnknownVersionInteroperabilityProxy فعال باشد، kube-apiserverهای همتا از این IP استفاده می‌کنند تا درخواست‌ها را به این kube-apiserver پروکسی کنند، در مواردی که به دلیل اختلاف نسخه (version skew) بین kube-apiserverها، همتا قادر به رسیدگی به درخواست نباشد. این فلگ فقط در کلاسترهایی استفاده می‌شود که برای دسترس‌پذیری بالا با چند kube-apiserver پیکربندی شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--peer-advertise-port string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود و feature gate با نام UnknownVersionInteroperabilityProxy فعال باشد، kube-apiserverهای همتا از این پورت استفاده می‌کنند تا درخواست‌ها را به این kube-apiserver پروکسی کنند، در مواردی که به دلیل اختلاف نسخه (version skew) بین kube-apiserverها، همتا قادر به رسیدگی به درخواست نباشد. این فلگ فقط در کلاسترهایی استفاده می‌شود که برای دسترس‌پذیری بالا با چند kube-apiserver پیکربندی شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--peer-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر تنظیم شود و feature gate با نام UnknownVersionInteroperabilityProxy فعال باشد، از این فایل برای تأیید گواهی‌های سرویس‌دهی kube-apiserverهای همتا استفاده می‌شود. این فلگ فقط در کلاسترهایی استفاده می‌شود که برای دسترس‌پذیری بالا با چند kube-apiserver پیکربندی شده‌اند.</p></td>
</tr>

<tr>
<td colspan="2">--permit-address-sharing</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، هنگام bind کردن پورت از SO_REUSEADDR استفاده می‌شود. این امر امکان bind شدن هم‌زمان به IPهای wildcard مانند 0.0.0.0 و IPهای مشخص را فراهم می‌کند و از انتظار برای آزاد شدن سوکت‌های در حالت TIME_WAIT توسط کرنل جلوگیری می‌کند. [default=false]</p></td>
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
<td colspan="2">--proxy-client-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>گواهی کلاینت که برای اثبات هویت aggregator یا kube-apiserver هنگام نیاز به فراخوانی سرویس‌های خارجی در طول یک درخواست استفاده می‌شود. این شامل پروکسی کردن درخواست‌ها به api-server کاربر و فراخوانی افزونه‌های admission از نوع webhook است. انتظار می‌رود این گواهی دارای امضای CA مشخص‌شده در فلگ --requestheader-client-ca-file باشد. این CA در configmap با نام 'extension-apiserver-authentication' در فضای نام kube-system منتشر می‌شود. مؤلفه‌هایی که از kube-aggregator فراخوانی دریافت می‌کنند باید از آن CA برای انجام سهم خود از تأیید mutual TLS استفاده کنند.</p></td>
</tr>

<tr>
<td colspan="2">--proxy-client-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>کلید خصوصی گواهی کلاینت که برای اثبات هویت aggregator یا kube-apiserver هنگام نیاز به فراخوانی سرویس‌های خارجی در طول یک درخواست استفاده می‌شود. این شامل پروکسی کردن درخواست‌ها به api-server کاربر و فراخوانی افزونه‌های admission از نوع webhook است.</p></td>
</tr>

<tr>
<td colspan="2">--request-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک فیلد اختیاری که مدت زمانی را مشخص می‌کند که یک handler باید یک درخواست را پیش از اعمال مهلت زمانی باز نگه دارد. این مقدار، مهلت زمانی پیش‌فرض درخواست‌هاست، اما برای انواع خاصی از درخواست‌ها ممکن است توسط فلگ‌هایی مانند --min-request-timeout بازنویسی شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-allowed-names strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست common nameهای گواهی کلاینت که مجاز به ارائه نام کاربری در هدرهای مشخص‌شده با --requestheader-username-headers هستند. اگر خالی باشد، هر گواهی کلاینتی که توسط مراجع موجود در --requestheader-client-ca-file تأیید شده باشد مجاز است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-client-ca-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بسته گواهی ریشه برای تأیید گواهی‌های کلاینت در درخواست‌های ورودی، پیش از اعتماد به نام‌های کاربری موجود در هدرهای مشخص‌شده با --requestheader-username-headers. هشدار: به‌طور کلی نباید به این موضوع تکیه کرد که مجوزدهی (authorization) برای درخواست‌های ورودی از قبل انجام شده است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-extra-headers-prefix strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست پیشوندهای هدر درخواست که باید بررسی شوند. مقدار X-Remote-Extra- پیشنهاد می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-group-headers strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای یافتن گروه‌ها بررسی می‌شوند. مقدار X-Remote-Group پیشنهاد می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-uid-headers strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای یافتن UIDها بررسی می‌شوند. مقدار X-Remote-Uid پیشنهاد می‌شود. نیازمند فعال بودن قابلیت RemoteRequestHeaderUID است.</p></td>
</tr>

<tr>
<td colspan="2">--requestheader-username-headers strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست هدرهای درخواست که برای یافتن نام‌های کاربری بررسی می‌شوند. مقدار X-Remote-User رایج است.</p></td>
</tr>

<tr>
<td colspan="2">--runtime-config &lt;comma-separated 'key=value' pairs&gt;</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مجموعه‌ای از جفت‌های key=value که APIهای داخلی را فعال یا غیرفعال می‌کنند. گزینه‌های پشتیبانی‌شده عبارت‌اند از:<br/>v1=true|false برای گروه API هسته (core)<br/>&lt;group&gt;/&lt;version&gt;=true|false برای یک گروه و نسخه API مشخص (مثلاً apps/v1=true)<br/>api/all=true|false همه نسخه‌های API را کنترل می‌کند<br/>api/ga=true|false همه نسخه‌های API با قالب v[0-9]+ را کنترل می‌کند<br/>api/beta=true|false همه نسخه‌های API با قالب v[0-9]+beta[0-9]+ را کنترل می‌کند<br/>api/alpha=true|false همه نسخه‌های API با قالب v[0-9]+alpha[0-9]+ را کنترل می‌کند<br/>api/legacy منسوخ شده است و در نسخه‌ای در آینده حذف خواهد شد</p></td>
</tr>

<tr>
<td colspan="2">--runtime-config-emulation-forward-compatible</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، APIهایی که با group/version مشخص می‌شوند و در فلگ --runtime-config فعال شده‌اند، حتی در صورتی که پس از نسخه شبیه‌سازی (emulation version) معرفی شده باشند، نصب خواهند شد. اگر false باشد و هر یک از APIهایی که با group/version مشخص می‌شوند و در فلگ --runtime-config فعال شده‌اند پس از نسخه شبیه‌سازی معرفی شده باشند، سرور از راه‌اندازی بازمی‌ماند. این مقدار تنها در صورتی می‌تواند true باشد که نسخه شبیه‌سازی پایین‌تر از نسخه باینری باشد.</p></td>
</tr>

<tr>
<td colspan="2">--secure-port int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 6443</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>پورتی که HTTPS همراه با احراز هویت و مجوزدهی روی آن ارائه می‌شود. این پورت را نمی‌توان با مقدار 0 غیرفعال کرد.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-extend-token-expiration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تمدید انقضای projected service account را هنگام تولید توکن فعال می‌کند که به انتقال ایمن از توکن‌های قدیمی (legacy) به قابلیت توکن‌های service account مقید (bound) کمک می‌کند. اگر این فلگ فعال باشد، توکن‌هایی که توسط admission تزریق می‌شوند تا یک سال تمدید می‌شوند تا از بروز خطای غیرمنتظره در طول انتقال جلوگیری شود و مقدار service-account-max-token-expiration نادیده گرفته می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-issuer strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>شناسه صادرکننده توکن service account. صادرکننده این شناسه را در claim با نام &quot;iss&quot; توکن‌های صادرشده درج می‌کند. این مقدار یک رشته یا URI است. اگر این گزینه بر اساس مشخصات OpenID Discovery 1.0 یک URI معتبر نباشد، قابلیت ServiceAccountIssuerDiscovery حتی در صورتی که feature gate آن روی true تنظیم شده باشد، غیرفعال باقی می‌ماند. به‌شدت توصیه می‌شود که این مقدار با مشخصات OpenID مطابقت داشته باشد: https://openid.net/specs/openid-connect-discovery-1_0.html. در عمل، این به آن معناست که service-account-issuer باید یک URL از نوع https باشد. همچنین به‌شدت توصیه می‌شود که این URL قادر باشد اسناد OpenID discovery را در آدرس {service-account-issuer}/.well-known/openid-configuration ارائه دهد. وقتی این فلگ چندین بار مشخص شود، اولین مقدار برای تولید توکن‌ها استفاده می‌شود و همه مقادیر برای تعیین اینکه کدام صادرکنندگان پذیرفته شوند به کار می‌روند.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-jwks-uri string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>URI مربوط به JSON Web Key Set را در سند discovery که در مسیر /.well-known/openid-configuration ارائه می‌شود، بازنویسی می‌کند. این فلگ زمانی مفید است که سند discovery و مجموعه کلیدها از طریق URLی غیر از آدرس خارجی API server (که به‌صورت خودکار شناسایی می‌شود یا با external-hostname بازنویسی شده است) به relying partyها ارائه شوند.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-key-file strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی حاوی کلیدهای خصوصی یا عمومی RSA یا ECDSA از نوع x509 با کدگذاری PEM که برای تأیید توکن‌های ServiceAccount استفاده می‌شود. فایل مشخص‌شده می‌تواند شامل چندین کلید باشد و این فلگ را می‌توان چندین بار با فایل‌های متفاوت مشخص کرد. اگر مشخص نشود، از --tls-private-key-file استفاده می‌شود. هنگامی که --service-account-signing-key-file ارائه شده باشد، باید این فلگ نیز مشخص شود.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-lookup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، در چارچوب احراز هویت، وجود توکن‌های ServiceAccount در etcd اعتبارسنجی می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-max-token-expiration duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر مدت اعتبار توکنی که توسط صادرکننده توکن service account ایجاد می‌شود. اگر یک TokenRequest که در غیر این صورت معتبر است، مدت اعتباری بیشتر از این مقدار درخواست کند، توکن با مدت اعتبار برابر با همین مقدار صادر خواهد شد.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-signing-endpoint string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر سوکتی که یک امضاکننده JWT خارجی روی آن گوش می‌دهد. این فلگ با --service-account-signing-key-file و --service-account-key-file ناسازگار است و نمی‌توان آن‌ها را هم‌زمان به کار برد. نیازمند فعال‌سازی feature gate با نام ExternalServiceAccountTokenSigner است.</p></td>
</tr>

<tr>
<td colspan="2">--service-account-signing-key-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مسیر فایلی که شامل کلید خصوصی فعلی صادرکننده توکن service account است. صادرکننده توکن‌های ID صادرشده را با این کلید خصوصی امضا می‌کند.</p></td>
</tr>

<tr>
<td colspan="2">--service-cluster-ip-range string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدوده IP با نمادگذاری CIDR که از آن IPهای کلاستری Serviceها تخصیص داده می‌شود. این محدوده نباید با هیچ‌یک از محدوده‌های IP تخصیص‌یافته به نودها یا Podها هم‌پوشانی داشته باشد. حداکثر دو CIDR دوپشته‌ای (dual-stack) مجاز است.</p></td>
</tr>

<tr>
<td colspan="2">--service-node-port-range &lt;a string in the form 'N1-N2'&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 30000-32767</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>محدوده‌ای از پورت‌ها که برای Serviceهای با قابلیت دسترسی NodePort رزرو می‌شود. این محدوده نباید با محدوده پورت‌های موقت (ephemeral) روی نودها هم‌پوشانی داشته باشد. مثال: '30000-32767'. هر دو سر محدوده شامل می‌شوند.</p></td>
</tr>

<tr>
<td colspan="2">--show-hidden-metrics-for-version string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نسخه قبلی که می‌خواهید معیارهای پنهان‌شده آن نمایش داده شود. فقط نسخه فرعی (minor) قبلی معنا دارد و مقادیر دیگر پذیرفته نمی‌شوند. قالب آن &lt;major&gt;.&lt;minor&gt; است، برای مثال: '1.16'. هدف از این قالب آن است که اگر انتشار بعدی معیارهای بیشتری را پنهان کند، فرصت داشته باشید متوجه آن شوید و با حذف دائمی آن‌ها در انتشار پس از آن غافلگیر نشوید.</p></td>
</tr>

<tr>
<td colspan="2">--shutdown-delay-duration duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>مدت زمان تأخیر در خاتمه‌دادن. در این مدت، سرور همچنان درخواست‌ها را به‌طور عادی پاسخ می‌دهد. endpointهای /healthz و /livez موفقیت را برمی‌گردانند، اما /readyz بلافاصله شکست را برمی‌گرداند. خاتمه مطلوب (graceful termination) پس از سپری‌شدن این تأخیر آغاز می‌شود. از این گزینه می‌توان برای این استفاده کرد که load balancer ارسال ترافیک به این سرور را متوقف کند.</p></td>
</tr>

<tr>
<td colspan="2">--shutdown-send-retry-after</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>اگر true باشد، سرور HTTP تا زمانی که همه درخواست‌های در حال پردازشِ غیرطولانی‌مدت تخلیه شوند به گوش دادن ادامه می‌دهد؛ در این بازه، همه درخواست‌های ورودی با کد وضعیت 429 و هدر پاسخ 'Retry-After' رد می‌شوند و علاوه بر آن، هدر پاسخ 'Connection: close' تنظیم می‌شود تا اتصال TCP در زمان بیکاری قطع شود.</p></td>
</tr>

<tr>
<td colspan="2">--shutdown-watch-termination-grace-period duration</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>این گزینه در صورت تنظیم، بیشترین مدت مهلتی را مشخص می‌کند که apiserver در بازه خاموش‌شدن مطلوب سرور منتظر می‌ماند تا درخواست‌های watch فعال تخلیه شوند.</p></td>
</tr>

<tr>
<td colspan="2">--storage-backend string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>بک‌اند ذخیره‌سازی برای پایداری داده‌ها. گزینه‌ها: 'etcd3' (پیش‌فرض).</p></td>
</tr>

<tr>
<td colspan="2">--storage-initialization-timeout duration&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: 1m0s</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>حداکثر مدت انتظار برای راه‌اندازی اولیه ذخیره‌سازی پیش از اعلام آماده‌بودن apiserver. مقدار پیش‌فرض 1m است.</p></td>
</tr>

<tr>
<td colspan="2">--storage-media-type string&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: "application/vnd.kubernetes.protobuf"</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>نوع رسانه‌ای (media type) که برای ذخیره آبجکت‌ها در ذخیره‌سازی استفاده می‌شود. برخی منابع یا بک‌اندهای ذخیره‌سازی ممکن است فقط از یک نوع رسانه خاص پشتیبانی کنند و این تنظیم را نادیده بگیرند. انواع رسانه پشتیبانی‌شده: [application/json, application/yaml, application/vnd.kubernetes.protobuf]</p></td>
</tr>

<tr>
<td colspan="2">--strict-transport-security-directives strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست دستورهای (directives) HSTS که با کاما از هم جدا می‌شوند. اگر این فهرست خالی باشد، دستورهای HSTS اضافه نخواهند شد. مثال: 'max-age=31536000,includeSubDomains,preload'</p></td>
</tr>

<tr>
<td colspan="2">--tls-cert-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی حاوی گواهی x509 پیش‌فرض برای HTTPS. (گواهی CA، در صورت وجود، پس از گواهی سرور به آن الحاق می‌شود). اگر ارائه HTTPS فعال باشد و --tls-cert-file و --tls-private-key-file ارائه نشده باشند، یک گواهی و کلید خودامضا برای آدرس عمومی تولید و در دایرکتوری مشخص‌شده با --cert-dir ذخیره می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--tls-cipher-suites strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرست مجموعه‌رمزهای (cipher suites) سرور که با کاما از هم جدا می‌شوند. اگر حذف شود، از مجموعه‌رمزهای پیش‌فرض Go استفاده می‌شود.<br/>مقادیر ترجیحی: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305, TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256.<br/>مقادیر ناامن: TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_RC4_128_SHA.</p></td>
</tr>

<tr>
<td colspan="2">--tls-curve-preferences int32Slice&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: []</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از مقادیر عددی CurveID در crypto/tls زبان Go که با کاما از هم جدا شده‌اند و به‌عنوان سازوکارهای مجاز تبادل کلید برای سرور به کار می‌روند. مقادیر پشتیبانی‌شده به نسخه Go مورد استفاده بستگی دارد. برای مشاهده مقادیر پشتیبانی‌شده در هر نسخه Go به https://pkg.go.dev/crypto/tls#CurveID مراجعه کنید. ترتیب فهرست نادیده گرفته می‌شود و سازوکارهای تبادل کلید توسط Go از این فهرست و بر اساس یک ترتیب ترجیحی داخلی انتخاب می‌شوند. اگر حذف شود، از منحنی‌های پیش‌فرض Go استفاده می‌شود.</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایلی حاوی کلید خصوصی x509 پیش‌فرض که با --tls-cert-file مطابقت دارد.</p></td>
</tr>

<tr>
<td colspan="2">--tls-sni-cert-key string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>یک جفت مسیر فایل گواهی x509 و کلید خصوصی که می‌تواند در انتها فهرستی از الگوهای دامنه (domain patterns) داشته باشد؛ این الگوها نام‌های دامنه کاملاً معتبر (fully qualified) هستند و ممکن است بخش‌های wildcard در ابتدای آن‌ها آمده باشد. الگوهای دامنه آدرس‌های IP را نیز مجاز می‌دانند، اما IPها فقط در صورتی باید استفاده شوند که apiserver به آدرس IP درخواست‌شده توسط کلاینت دسترسی داشته باشد. اگر هیچ الگوی دامنه‌ای ارائه نشود، نام‌های موجود در گواهی استخراج می‌شوند. تطابق‌های بدون wildcard بر تطابق‌های wildcard اولویت دارند و الگوهای دامنه صریح بر نام‌های استخراج‌شده اولویت دارند. برای چند جفت کلید/گواهی، فلگ --tls-sni-cert-key را چندین بار به کار ببرید. مثال‌ها: &quot;example.crt,example.key&quot; یا &quot;foo.crt,foo.key:*.foo.com,foo.com&quot;.</p></td>
</tr>

<tr>
<td colspan="2">--token-auth-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>در صورت تنظیم، فایلی که برای ایمن‌سازی پورت امن API server از طریق احراز هویت مبتنی بر توکن استفاده می‌شود.</p></td>
</tr>

<tr>
<td colspan="2">--tracing-config-file string</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فایل پیکربندی ردیابی (tracing) مربوط به apiserver.</p></td>
</tr>

<tr>
<td colspan="2">-v, --v int</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>عددی برای تعیین سطح جزئیات لاگ</p></td>
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
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فهرستی از تنظیمات pattern=N که با کاما از هم جدا می‌شوند، برای ثبت لاگ با فیلتر بر اساس فایل (فقط در قالب لاگ متنی کار می‌کند)</p></td>
</tr>

<tr>
<td colspan="2">--watch-cache&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default: true</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>فعال‌سازی کش watch در apiserver</p></td>
</tr>

<tr>
<td colspan="2">--watch-cache-sizes strings</td>
</tr>
<tr>
<td></td><td style="line-height: 130%; word-wrap: break-word;"><p>تنظیمات اندازه کش watch برای برخی منابع (Podها، نودها و غیره) که با کاما از هم جدا می‌شوند. قالب هر تنظیم: resource[.group]#size است، که در آن resource حالت جمع با حروف کوچک (بدون نسخه) است، group برای منابع apiVersion v1 (API هسته قدیمی) حذف می‌شود و برای بقیه درج می‌شود، و size یک عدد است. این گزینه فقط برای منابعی معنا دارد که در apiserver تعبیه شده‌اند، نه منابعی که با CRDها تعریف شده‌اند یا از سرورهای خارجی تجمیع (aggregate) شده‌اند، و تنها در صورتی بررسی می‌شود که watch-cache فعال باشد. تنها مقدار معنادار برای size در اینجا صفر است که به معنای غیرفعال‌کردن کش watch برای منبع مربوطه است؛ همه مقادیر غیرصفر معادل هستند و به معنای غیرفعال‌نکردن کش watch برای آن منبع می‌باشند</p></td>
</tr>

</tbody>
</table>
