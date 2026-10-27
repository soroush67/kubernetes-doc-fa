---
reviewers:
- liggitt
- mikedanese
- munnerz
- enj
title: گواهی‌ها و درخواست‌های امضای گواهی
api_metadata:
- apiVersion: "certificates.k8s.io/v1"
  kind: "CertificateSigningRequest"
  override_link_text: "CSR v1"
- apiVersion: "certificates.k8s.io/v1"
  kind: "PodCertificateRequest"
- apiVersion: "certificates.k8s.io/v1"
  kind: "ClusterTrustBundle"  
content_type: concept
weight: 60
---

<!-- overview -->

APIهای گواهی و trust bundle در کوبرنتیز با فراهم کردن یک رابط برنامه‌نویسی برای کلاینت‌های API کوبرنتیز، امکان خودکارسازی صدور اعتبارنامه‌های [X.509](https://www.itu.int/rec/T-REC-X.509) را فراهم می‌کنند. کلاینت‌ها با استفاده از این رابط می‌توانند {{< glossary_tooltip term_id="certificate" text="گواهی‌های" >}} X.509 را از یک مرجع صدور گواهی (Certificate Authority یا CA) درخواست کرده و دریافت کنند.

همچنین از توزیع [trust bundleها](#cluster-trust-bundles) پشتیبانی می‌شود.

<!-- body -->

## درخواست‌های امضای گواهی {#certificate-signing-requests}

{{< feature-state for_k8s_version="v1.19" state="stable" >}}


منبع [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/)
(CSR) برای درخواست امضای یک گواهی توسط یک امضاکننده (signer) مشخص استفاده می‌شود؛ پس از آن، درخواست می‌تواند پیش از امضای نهایی تأیید یا رد شود.


### فرایند امضای درخواست

نوع منبع CertificateSigningRequest به کلاینت اجازه می‌دهد درخواست کند که یک گواهی X.509 بر اساس یک درخواست امضا صادر شود.
آبجکت CertificateSigningRequest یک درخواست امضای PKCS#10 با کدگذاری PEM را در فیلد `spec.request` در خود دارد. CertificateSigningRequest امضاکننده (یعنی گیرنده‌ای که درخواست به آن ارسال می‌شود) را با استفاده از فیلد `spec.signerName` مشخص می‌کند.
توجه کنید که `spec.signerName` پس از نسخه API با نام `certificates.k8s.io/v1` یک کلید الزامی است.
در کوبرنتیز نسخه v1.22 و بعدتر، کلاینت‌ها می‌توانند به‌صورت اختیاری فیلد `spec.expirationSeconds` را تنظیم کنند تا مدت اعتبار مشخصی را برای گواهی صادرشده درخواست کنند. کمترین مقدار معتبر برای این فیلد `600` است، یعنی ده دقیقه.

پس از ایجاد، یک CertificateSigningRequest باید پیش از امضا تأیید شود.
بسته به امضاکننده انتخاب‌شده، ممکن است یک CertificateSigningRequest به‌صورت خودکار توسط یک {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} تأیید شود.
در غیر این صورت، یک CertificateSigningRequest باید به‌صورت دستی و از طریق REST API (یا client-go) یا با اجرای `kubectl certificate approve` تأیید شود. به همین ترتیب، یک CertificateSigningRequest را می‌توان رد نیز کرد؛ این کار به امضاکننده پیکربندی‌شده اعلام می‌کند که نباید درخواست را امضا کند.

برای گواهی‌های تأییدشده، مرحله بعد امضا است. کنترل‌کننده امضای مربوطه ابتدا بررسی می‌کند که شرایط امضا برقرار است و سپس یک گواهی ایجاد می‌کند.
سپس کنترل‌کننده امضا، CertificateSigningRequest را به‌روزرسانی می‌کند و گواهی جدید را در فیلد `status.certificate` از آبجکت CertificateSigningRequest موجود ذخیره می‌کند.
فیلد `status.certificate` یا خالی است یا یک گواهی X.509 با قالب PEM دارد.
فیلد `status.certificate` در CertificateSigningRequest تا زمانی که امضاکننده این کار را انجام ندهد خالی می‌ماند.

پس از آنکه فیلد `status.certificate` مقداردهی شد، درخواست تکمیل شده است و کلاینت‌ها اکنون می‌توانند داده PEM گواهی امضاشده را از منبع CertificateSigningRequest دریافت کنند.
در مقابل، اگر شرایط تأیید برقرار نباشد، امضاکننده‌ها می‌توانند از امضای گواهی خودداری کنند.

برای کاهش تعداد منابع قدیمی CertificateSigningRequest که در کلاستر باقی می‌مانند، یک کنترل‌کننده جمع‌آوری زباله (garbage collection) به‌صورت دوره‌ای اجرا می‌شود. این فرایند CertificateSigningRequestهایی را که برای مدتی وضعیتشان تغییر نکرده است حذف می‌کند:

* درخواست‌های تأییدشده: پس از ۱ ساعت به‌صورت خودکار حذف می‌شوند
* درخواست‌های ردشده: پس از ۱ ساعت به‌صورت خودکار حذف می‌شوند
* درخواست‌های ناموفق: پس از ۱ ساعت به‌صورت خودکار حذف می‌شوند
* درخواست‌های در حال انتظار: پس از ۲۴ ساعت به‌صورت خودکار حذف می‌شوند
* همه درخواست‌ها: پس از منقضی شدن گواهی صادرشده به‌صورت خودکار حذف می‌شوند

### مجوزدهی امضای گواهی {#authorization}

برای اجازه ایجاد یک CertificateSigningRequest و بازیابی هر CertificateSigningRequest:

* Verbها: `create`، `get`، `list`، `watch`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests`

برای مثال:

{{% code_sample file="access/certificate-signing-request/clusterrole-create.yaml" %}}

برای اجازه تأیید یک CertificateSigningRequest:

* Verbها: `get`، `list`، `watch`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests`
* Verbها: `update`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests/approval`
* Verbها: `approve`، گروه: `certificates.k8s.io`، منبع: `signers`، resourceName: `<signerNameDomain>/<signerNamePath>` یا `<signerNameDomain>/*`

برای مثال:

{{% code_sample file="access/certificate-signing-request/clusterrole-approve.yaml" %}}

برای اجازه امضای یک CertificateSigningRequest:

* Verbها: `get`، `list`، `watch`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests`
* Verbها: `update`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests/status`
* Verbها: `sign`، گروه: `certificates.k8s.io`، منبع: `signers`، resourceName: `<signerNameDomain>/<signerNamePath>` یا `<signerNameDomain>/*`

{{% code_sample file="access/certificate-signing-request/clusterrole-sign.yaml" %}}


## امضاکننده‌ها (Signers) {#signers}

امضاکننده‌ها به‌صورت انتزاعی نشان‌دهنده موجودیت یا موجودیت‌هایی هستند که ممکن است یک گواهی امنیتی را امضا کنند یا کرده باشند.

هر امضاکننده‌ای که برای استفاده در خارج از یک کلاستر مشخص در دسترس قرار می‌گیرد، باید اطلاعاتی درباره نحوه کار امضاکننده ارائه دهد تا مصرف‌کنندگان بتوانند معنای آن را برای CertificateSigningRequestها و (در صورت فعال بودن) [ClusterTrustBundleها](#cluster-trust-bundles) درک کنند.
این اطلاعات شامل موارد زیر است:

1. **توزیع اعتماد (Trust distribution)**: چگونگی توزیع trust anchorها (گواهی‌های CA یا بسته‌های گواهی).
1. **سوژه‌های مجاز (Permitted subjects)**: هرگونه محدودیت در این زمینه و رفتار سیستم در صورتی که سوژه غیرمجاز درخواست شود.
1. **افزونه‌های x509 مجاز**: شامل subjectAltNameهای IP، subjectAltNameهای DNS، subjectAltNameهای ایمیل، subjectAltNameهای URI و مانند آن، و رفتار سیستم در صورتی که افزونه غیرمجاز درخواست شود.
1. **کاربردهای کلید / کاربردهای کلید گسترش‌یافته مجاز**: هرگونه محدودیت در این زمینه و رفتار سیستم در صورتی که در CSR کاربردهایی متفاوت از کاربردهای تعیین‌شده توسط امضاکننده مشخص شده باشد.
1. **انقضا/مدت اعتبار گواهی**: اینکه آیا توسط امضاکننده ثابت است، توسط مدیر قابل پیکربندی است، توسط فیلد `spec.expirationSeconds` در CSR تعیین می‌شود و غیره، و رفتار سیستم در صورتی که انقضای تعیین‌شده توسط امضاکننده با فیلد `spec.expirationSeconds` در CSR متفاوت باشد.
1. **مجاز/غیرمجاز بودن بیت CA**: و رفتار سیستم در صورتی که یک CSR شامل درخواست گواهی CA باشد، در حالی که امضاکننده آن را مجاز نمی‌داند.

معمولاً فیلد `status.certificate` در یک CertificateSigningRequest، پس از تأیید CSR و صدور گواهی، شامل یک گواهی X.509 با کدگذاری PEM است.
برخی امضاکننده‌ها چندین گواهی را در فیلد `status.certificate` ذخیره می‌کنند. در این حالت، مستندات امضاکننده باید معنای گواهی‌های اضافی را مشخص کند؛ برای مثال، ممکن است این گواهی‌ها شامل گواهی اصلی به‌همراه گواهی‌های میانی باشند که در جریان TLS handshake ارائه می‌شوند.

اگر می‌خواهید _trust anchor_ (گواهی ریشه) را در دسترس قرار دهید، این کار باید جدا از CertificateSigningRequest و فیلد `status.certificate` آن انجام شود. برای مثال، می‌توانید از یک ClusterTrustBundle استفاده کنید.

قالب درخواست امضای PKCS#10 سازوکار استانداردی برای مشخص کردن انقضا یا مدت اعتبار گواهی ندارد. بنابراین انقضا یا مدت اعتبار باید از طریق فیلد `spec.expirationSeconds` در آبجکت CSR تعیین شود. امضاکننده‌های داخلی (built-in) در صورتی که `spec.expirationSeconds` مشخص نشده باشد، از گزینه پیکربندی `ClusterSigningDuration` (که مقدار پیش‌فرض آن ۱ سال است و معادل فلگ خط فرمان `--cluster-signing-duration` در kube-controller-manager است) به‌عنوان مقدار پیش‌فرض استفاده می‌کنند. وقتی `spec.expirationSeconds` مشخص شده باشد، کمینه مقدار `spec.expirationSeconds` و `ClusterSigningDuration` به کار می‌رود.

{{< note >}}
فیلد `spec.expirationSeconds` در کوبرنتیز v1.22 اضافه شد. نسخه‌های قدیمی‌تر کوبرنتیز این فیلد را رعایت نمی‌کنند.
سرورهای API کوبرنتیز پیش از v1.22 هنگام ایجاد آبجکت، این فیلد را بدون هیچ پیامی حذف می‌کنند.
{{< /note >}}

### امضاکننده‌های کوبرنتیز {#kubernetes-signers}

کوبرنتیز امضاکننده‌های داخلی‌ای فراهم می‌کند که هر کدام `signerName` شناخته‌شده‌ای دارند:

1. `kubernetes.io/kube-apiserver-client`: گواهی‌هایی را امضا می‌کند که سرور API آن‌ها را به‌عنوان گواهی کلاینت معتبر می‌شناسد.
   هرگز توسط {{< glossary_tooltip term_id="kube-controller-manager" >}} به‌صورت خودکار تأیید نمی‌شود.
   1. توزیع اعتماد: گواهی‌های امضاشده باید توسط سرور API به‌عنوان گواهی کلاینت پذیرفته شوند. بسته CA از هیچ راه دیگری توزیع نمی‌شود.
   1. سوژه‌های مجاز - هیچ محدودیتی برای سوژه وجود ندارد، اما تأییدکنندگان و امضاکنندگان می‌توانند تصمیم بگیرند که تأیید یا امضا نکنند.
      برخی سوژه‌ها مانند کاربران یا گروه‌های در سطح cluster-admin در توزیع‌ها و نصب‌های مختلف متفاوت‌اند،
      اما پیش از تأیید و امضا شایسته دقت و بررسی بیشتر هستند.
      admission plugin با نام `CertificateSubjectRestriction` به‌صورت پیش‌فرض فعال است تا `system:masters` را محدود کند،
      اما این سوژه اغلب تنها سوژه cluster-admin در یک کلاستر نیست.
   1. افزونه‌های x509 مجاز - subjectAltName و افزونه‌های کاربرد کلید را رعایت می‌کند و سایر افزونه‌ها را کنار می‌گذارد.
   1. کاربردهای کلید مجاز - باید شامل `["client auth"]` باشد. نباید شامل کاربردهای کلید فراتر از `["digital signature", "key encipherment", "client auth"]` باشد.
   1. انقضا/مدت اعتبار گواهی - در پیاده‌سازی این امضاکننده در kube-controller-manager، برابر است با کمینه
      گزینه `--cluster-signing-duration` یا، در صورت مشخص بودن، فیلد `spec.expirationSeconds` از آبجکت CSR.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/kube-apiserver-client-kubelet`: گواهی‌های کلاینتی را امضا می‌کند که سرور API آن‌ها را به‌عنوان گواهی کلاینت معتبر می‌شناسد.
   ممکن است توسط {{< glossary_tooltip term_id="kube-controller-manager" >}} به‌صورت خودکار تأیید شود.
   1. توزیع اعتماد: گواهی‌های امضاشده باید توسط سرور API به‌عنوان گواهی کلاینت پذیرفته شوند. بسته CA
      از هیچ راه دیگری توزیع نمی‌شود.
   1. سوژه‌های مجاز - سازمان‌ها (organizations) دقیقاً `["system:nodes"]` هستند و نام مشترک (common name) برابر "`system:node:${NODE_NAME}`" است.
   1. افزونه‌های x509 مجاز - افزونه‌های کاربرد کلید را رعایت می‌کند، افزونه‌های subjectAltName را ممنوع می‌کند و سایر افزونه‌ها را کنار می‌گذارد.
   1. کاربردهای کلید مجاز - `["key encipherment", "digital signature", "client auth"]` یا `["digital signature", "client auth"]`.
   1. انقضا/مدت اعتبار گواهی - در پیاده‌سازی این امضاکننده در kube-controller-manager، برابر است با کمینه
      گزینه `--cluster-signing-duration` یا، در صورت مشخص بودن، فیلد `spec.expirationSeconds` از آبجکت CSR.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/kubelet-serving`: گواهی‌های سرویس‌دهی (serving) را امضا می‌کند که سرور API آن‌ها را به‌عنوان گواهی معتبر سرویس‌دهی kubelet می‌پذیرد،
   اما هیچ تضمین دیگری ندارد.
   هرگز توسط {{< glossary_tooltip term_id="kube-controller-manager" >}} به‌صورت خودکار تأیید نمی‌شود.
   1. توزیع اعتماد: گواهی‌های امضاشده باید توسط سرور API به‌عنوان گواهی معتبر برای خاتمه دادن به اتصال‌ها به یک kubelet پذیرفته شوند.
      بسته CA از هیچ راه دیگری توزیع نمی‌شود.
   1. سوژه‌های مجاز - سازمان‌ها (organizations) دقیقاً `["system:nodes"]` هستند و نام مشترک (common name) برابر "`system:node:${NODE_NAME}`" است.
   1. افزونه‌های x509 مجاز - افزونه‌های کاربرد کلید و افزونه‌های subjectAltName از نوع DNSName/IPAddress را رعایت می‌کند، افزونه‌های subjectAltName از نوع EmailAddress و
      URI را ممنوع می‌کند و سایر افزونه‌ها را کنار می‌گذارد. دست‌کم یک subjectAltName از نوع DNS یا IP باید وجود داشته باشد.
   1. کاربردهای کلید مجاز - `["key encipherment", "digital signature", "server auth"]` یا `["digital signature", "server auth"]`.
   1. انقضا/مدت اعتبار گواهی - در پیاده‌سازی این امضاکننده در kube-controller-manager، برابر است با کمینه
      گزینه `--cluster-signing-duration` یا، در صورت مشخص بودن، فیلد `spec.expirationSeconds` از آبجکت CSR.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/legacy-unknown`: هیچ تضمینی برای اعتماد ندارد. برخی توزیع‌های شخص ثالث کوبرنتیز
   ممکن است گواهی‌های کلاینت امضاشده توسط آن را بپذیرند. API پایدار CertificateSigningRequest (نسخه `certificates.k8s.io/v1` و بعدتر)
   اجازه نمی‌دهد `signerName` برابر `kubernetes.io/legacy-unknown` تنظیم شود.
   هرگز توسط {{< glossary_tooltip term_id="kube-controller-manager" >}} به‌صورت خودکار تأیید نمی‌شود.
   1. توزیع اعتماد: هیچ. هیچ اعتماد یا توزیع استانداردی برای این امضاکننده در کلاستر کوبرنتیز وجود ندارد.
   1. سوژه‌های مجاز - هر مقداری
   1. افزونه‌های x509 مجاز - subjectAltName و افزونه‌های کاربرد کلید را رعایت می‌کند و سایر افزونه‌ها را کنار می‌گذارد.
   1. کاربردهای کلید مجاز - هر مقداری
   1. انقضا/مدت اعتبار گواهی - در پیاده‌سازی این امضاکننده در kube-controller-manager، برابر است با کمینه
      گزینه `--cluster-signing-duration` یا، در صورت مشخص بودن، فیلد `spec.expirationSeconds` از آبجکت CSR.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/kube-apiserver-serving`: گواهی‌هایی را امضا می‌کند که می‌توان از آن‌ها برای تأیید گواهی‌های serving مربوط به kube-apiserver استفاده کرد. امضا و تأیید خارج از kube-controller-manager انجام می‌شود.
    - {{< feature-state feature_gate_name="ClusterTrustBundle" >}}
    1. توزیع اعتماد: گواهی‌های امضاشده توسط kube-apiserver برای احراز هویت سرور در TLS استفاده می‌شوند. بسته CA با استفاده از یک آبجکت ClusterTrustBundle توزیع می‌شود
       که با نام امضاکننده `kubernetes.io/kube-apiserver-serving` قابل شناسایی است.
    1. سوژه‌های مجاز - خود «Subject» بر اساس RFC2818 برای احراز هویت سرور در TLS منسوخ شده است. با این حال،
       همچنان باید از همان قواعد مربوط به {{< glossary_tooltip text="SANها" term_id="san" >}}ی DNS/IP
       در بخش «افزونه‌های x509 مجاز» زیر پیروی کند.
    1. افزونه‌های x509 مجاز - subjectAltName و افزونه‌های کاربرد کلید را رعایت می‌کند. دست‌کم
       یک subjectAltName از نوع DNS یا IP باید وجود داشته باشد. SAN های DNS/IP گواهی‌ها
       باید به نام میزبان/IP مربوط به kube-apiserver تفسیر شوند/به آن اشاره کنند.
    1. کاربردهای کلید مجاز - ["key encipherment", "digital signature", "server auth"] یا ["digital signature", "server auth"].
    1. انقضا/مدت اعتبار گواهی - حداکثر مدت اعتبار توصیه‌شده ۳۰ روز است.
    1. مجاز/غیرمجاز بودن بیت CA - توسط پروژه کوبرنتیز توصیه نمی‌شود.

{{< note >}}
فیلد `spec.expirationSeconds` در کوبرنتیز v1.22 اضافه شد. نسخه‌های قدیمی‌تر کوبرنتیز این فیلد را رعایت نمی‌کنند.
سرورهای API کوبرنتیز پیش از v1.22 هنگام ایجاد آبجکت، این فیلد را بدون هیچ پیامی حذف می‌کنند.
{{< /note >}}

kube-controller-manager [امضای control plane](#signer-control-plane) را برای هر یک از امضاکننده‌های داخلی، به‌جز `kubernetes.io/kube-apiserver-serving`، پیاده‌سازی می‌کند. خطاهای مربوط به همه این امضاکننده‌ها فقط در لاگ‌های kube-controller-manager گزارش می‌شوند.
امضای گواهی‌ها در دامنه اعتماد امضاکننده `kubernetes.io/kube-apiserver-serving` کاملاً در اختیار مدیر یا مدیران کلاستر است.

هرگونه اعتماد خارج از موارد توصیف‌شده در بالا کاملاً اتفاقی است. برای مثال، برخی توزیع‌ها ممکن است `kubernetes.io/legacy-unknown` را به‌عنوان گواهی کلاینت برای
kube-apiserver بپذیرند، اما این یک استاندارد نیست.
هیچ‌یک از این کاربردها به هیچ شکلی به `.data[ca.crt]` در secretهای توکن ServiceAccount مرتبط نیستند. آن بسته CA فقط
برای تأیید اتصال به سرور API با استفاده از سرویس پیش‌فرض (`kubernetes.default.svc`) تضمین شده است.

### امضاکننده‌های سفارشی {#custom-signers}

همچنین می‌توانید امضاکننده سفارشی خودتان را معرفی کنید که باید نامی پیشونددار و مشابه داشته باشد، اما از نام دامنه خودتان استفاده کند. برای مثال، اگر نماینده یک پروژه متن‌باز هستید که از دامنه `open-fictional.example` استفاده می‌کند،
می‌توانید `issuer.open-fictional.example/service-mesh` را به‌عنوان نام امضاکننده به کار ببرید.

یک امضاکننده سفارشی از API کوبرنتیز برای صدور گواهی استفاده می‌کند. بخش [امضاکننده‌های مبتنی بر API](#signer-api) را ببینید.

## امضا {#signing}

### امضاکننده control plane {#signer-control-plane}

control plane کوبرنتیز هر یک از
[امضاکننده‌های کوبرنتیز](/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers)
را به‌عنوان بخشی از kube-controller-manager پیاده‌سازی می‌کند.

برای یک مثال عملی از ایجاد یک CertificateSigningRequest و تأیید و امضای آن توسط control plane کوبرنتیز، به
[صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/)
مراجعه کنید.

{{< note >}}
پیش از کوبرنتیز v1.18، kube-controller-manager هر CSR را که به‌عنوان تأییدشده علامت‌گذاری شده بود، امضا می‌کرد.
{{< /note >}}

## تأیید یا رد {#approval-rejection}

پیش از آنکه یک [امضاکننده](#signers) بر اساس یک CertificateSigningRequest گواهی صادر کند،
امضاکننده معمولاً بررسی می‌کند که صدور برای آن CSR _تأیید_ شده باشد.

### تأیید خودکار توسط control plane {#approval-rejection-control-plane}

kube-controller-manager یک تأییدکننده داخلی برای گواهی‌هایی با
signerName برابر `kubernetes.io/kube-apiserver-client-kubelet` ارائه می‌دهد که مجوزهای مختلف
مربوط به CSRها برای اعتبارنامه‌های نود را به مجوزدهی (authorization) واگذار می‌کند.
kube-controller-manager برای بررسی مجوز تأیید گواهی، منابع SubjectAccessReview را با POST به سرور API ارسال می‌کند.

### تأیید یا رد با استفاده از `kubectl` {#approval-rejection-kubectl}

یک مدیر کوبرنتیز (با مجوزهای مناسب) می‌تواند CertificateSigningRequestها را با استفاده از دستورهای `kubectl certificate
approve` و `kubectl certificate deny` به‌صورت دستی تأیید (یا رد) کند.

برای تأیید یک CSR با kubectl:

```shell
kubectl certificate approve <certificate-signing-request-name>
```

به همین ترتیب، برای رد یک CSR:

```shell
kubectl certificate deny <certificate-signing-request-name>
```

### تأیید یا رد با استفاده از API کوبرنتیز {#approval-rejection-api-client}

کاربران REST API می‌توانند CSRها را با ارسال یک درخواست UPDATE به زیرمنبع (subresource) `approval`
مربوط به CSR موردنظر تأیید کنند. برای مثال، می‌توانید یک
{{< glossary_tooltip term_id="operator-pattern" text="اپراتور" >}} بنویسید که نوع خاصی از CSR را زیر نظر بگیرد
و سپس برای تأیید آن‌ها یک UPDATE ارسال کند.

هنگامی که یک درخواست تأیید یا رد ارسال می‌کنید، بسته به وضعیتی که تعیین کرده‌اید، یکی از شرایط وضعیت (status condition) یعنی `Approved` یا `Denied` را تنظیم کنید:

برای CSRهای `Approved`:

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
...
status:
  conditions:
  - lastUpdateTime: "2020-02-08T11:37:35Z"
    lastTransitionTime: "2020-02-08T11:37:35Z"
    message: Approved by my custom approver controller
    reason: ApprovedByMyPolicy # You can set this to any string
    type: Approved
```

برای CSRهای `Denied`:

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
...
status:
  conditions:
  - lastUpdateTime: "2020-02-08T11:37:35Z"
    lastTransitionTime: "2020-02-08T11:37:35Z"
    message: Denied by my custom approver controller
    reason: DeniedByMyPolicy # You can set this to any string
    type: Denied
```

معمول است که `status.conditions.reason` را با یک کد دلیل ماشین‌پسند و با قالب TitleCase تنظیم کنند؛ این صرفاً یک قرارداد است، اما می‌توانید آن را روی هر مقداری که می‌خواهید تنظیم کنید. اگر می‌خواهید یادداشتی برای مطالعه انسان اضافه کنید، از فیلد `status.conditions.message` استفاده کنید.

## امضاکننده‌های مبتنی بر API {#signer-api}

کاربرانی که از REST API استفاده می‌کنند می‌توانند با ارسال یک درخواست **update** به زیرمنبع `status` مربوط به CSR موردنظر، آن را امضا کنند.

در این درخواست، فیلد `status.certificate` باید طوری مقداردهی شود که شامل گواهی امضاشده باشد. این فیلد شامل یک یا چند گواهی با کدگذاری PEM است.

تمام بلوک‌های PEM باید برچسب "CERTIFICATE" داشته باشند، هیچ هدری (header) نداشته باشند، و داده‌ی کدگذاری‌شده باید یک ساختار Certificate از نوع ASN.1 با کدگذاری BER باشد، همان‌گونه که در [بخش ۴ از RFC5280](https://tools.ietf.org/html/rfc5280#section-4.1) توضیح داده شده است.

نمونه‌ای از محتوای گواهی:

```
-----BEGIN CERTIFICATE-----
MIIDgjCCAmqgAwIBAgIUC1N1EJ4Qnsd322BhDPRwmg3b/oAwDQYJKoZIhvcNAQEL
BQAwXDELMAkGA1UEBhMCeHgxCjAIBgNVBAgMAXgxCjAIBgNVBAcMAXgxCjAIBgNV
BAoMAXgxCjAIBgNVBAsMAXgxCzAJBgNVBAMMAmNhMRAwDgYJKoZIhvcNAQkBFgF4
MB4XDTIwMDcwNjIyMDcwMFoXDTI1MDcwNTIyMDcwMFowNzEVMBMGA1UEChMMc3lz
dGVtOm5vZGVzMR4wHAYDVQQDExVzeXN0ZW06bm9kZToxMjcuMC4wLjEwggEiMA0G
CSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDne5X2eQ1JcLZkKvhzCR4Hxl9+ZmU3
+e1zfOywLdoQxrPi+o4hVsUH3q0y52BMa7u1yehHDRSaq9u62cmi5ekgXhXHzGmm
kmW5n0itRECv3SFsSm2DSghRKf0mm6iTYHWDHzUXKdm9lPPWoSOxoR5oqOsm3JEh
Q7Et13wrvTJqBMJo1GTwQuF+HYOku0NF/DLqbZIcpI08yQKyrBgYz2uO51/oNp8a
sTCsV4OUfyHhx2BBLUo4g4SptHFySTBwlpRWBnSjZPOhmN74JcpTLB4J5f4iEeA7
2QytZfADckG4wVkhH3C2EJUmRtFIBVirwDn39GXkSGlnvnMgF3uLZ6zNAgMBAAGj
YTBfMA4GA1UdDwEB/wQEAwIFoDATBgNVHSUEDDAKBggrBgEFBQcDAjAMBgNVHRMB
Af8EAjAAMB0GA1UdDgQWBBTREl2hW54lkQBDeVCcd2f2VSlB1DALBgNVHREEBDAC
ggAwDQYJKoZIhvcNAQELBQADggEBABpZjuIKTq8pCaX8dMEGPWtAykgLsTcD2jYr
L0/TCrqmuaaliUa42jQTt2OVsVP/L8ofFunj/KjpQU0bvKJPLMRKtmxbhXuQCQi1
qCRkp8o93mHvEz3mTUN+D1cfQ2fpsBENLnpS0F4G/JyY2Vrh19/X8+mImMEK5eOy
o0BMby7byUj98WmcUvNCiXbC6F45QTmkwEhMqWns0JZQY+/XeDhEcg+lJvz9Eyo2
aGgPsye1o3DpyXnyfJWAWMhOz7cikS5X2adesbgI86PhEHBXPIJ1v13ZdfCExmdd
M1fLPhLyR54fGaY+7/X8P9AZzPefAkwizeXwe9ii6/a08vWoiE4=
-----END CERTIFICATE-----
```

محتوای غیر PEM می‌تواند پیش از بلوک‌های PEM گواهی یا پس از آن‌ها ظاهر شود و اعتبارسنجی نمی‌شود؛ این امر برای امکان درج متن توضیحی است، همان‌گونه که در [بخش ۵.۲ از RFC7468](https://www.rfc-editor.org/rfc/rfc7468#section-5.2) شرح داده شده است.

هنگامی که این فیلد در قالب JSON یا YAML کدگذاری می‌شود، به‌صورت base-64 کدگذاری می‌گردد.
پس از آنکه یک CertificateSigningRequest تأیید و امضا شد، گواهی امضاشده در فیلد `status.certificate` قرار می‌گیرد. یک CertificateSigningRequest که شامل گواهی نمونه‌ی بالا باشد، به شکل زیر خواهد بود:

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
...
status:
  certificate: "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JS..."
```

## PodCertificateRequests {#pod-certificate-requests}

{{< feature-state feature_gate_name="PodCertificateRequest" >}}


PodCertificateRequestها آبجکت‌های API هستند که برای تأمین گواهی برای بارهای کاری در حال اجرا به‌صورت Pod در یک کلاستر طراحی شده‌اند. کاربر معمولاً مستقیماً با PodCertificateRequestها تعامل نمی‌کند، بلکه از [منابع حجم پروژکشن‌شده podCertificate](
/docs/concepts/storage/projected-volumes#podcertificate) استفاده می‌کند؛ این قابلیتی در `kubelet` است که تأمین امن کلید و نوسازی خودکار گواهی را بر عهده دارد. برنامه‌ی درون Pod فقط باید بداند که چگونه گواهی‌ها را از فایل‌سیستم بخواند.

PodCertificateRequestها شبیه CertificateSigningRequestها هستند، اما به‌دلیل کاربرد محدودتر، قالب ساده‌تری دارند.

یک PodCertificateRequest دارای فیلدهای spec زیر است:
* `signerName`: امضاکننده‌ای که این درخواست به آن ارسال شده است.
* `podName` و `podUID`: Podی که Kubelet برای آن گواهی درخواست می‌کند.
* `serviceAccountName` و `serviceAccountUID`: ServiceAccount متناظر با Pod.
* `nodeName` و `nodeUID`: Node متناظر با Pod.
* `maxExpirationSeconds`: بیشترین طول عمری که نویسنده‌ی بار کاری برای این گواهی می‌پذیرد. در صورت مشخص نشدن، مقدار پیش‌فرض ۲۴ ساعت است.
* `stubPKCS10Request`: یک CSR حداقلی با قالب [PKCS#10](https://www.rfc-editor.org/rfc/rfc2986). امضاکننده‌ها باید کلید عمومی را از این CSR استخراج کنند. معمولاً نیازی نیست امضاکننده اقدام دیگری روی این فیلد انجام دهد، زیرا امضای CSR توسط API server بررسی می‌شود. درخواست‌های Kubelet فقط شامل اطلاعات کلید عمومی در CSR خواهند بود.
* `unverifiedUserAnnotations`: نگاشتی که به کاربر امکان می‌دهد اطلاعات اضافی را به پیاده‌سازی امضاکننده ارسال کند. این مقدار عیناً از فیلد `userAnnotations` در [منبع حجم پروژکشن‌شده podCertificate](/docs/concepts/storage/projected-volumes#podcertificate) کپی می‌شود. ورودی‌ها تابع همان اعتبارسنجی حاشیه‌نویسی‌های (annotation) فراداده‌ی آبجکت هستند، با این افزوده که همه‌ی کلیدها باید پیشوند دامنه داشته باشند. هیچ محدودیتی بر مقادیر اعمال نمی‌شود، جز محدودیت اندازه‌ی کلی برای کل فیلد. جدا از این اعتبارسنجی‌های پایه، API server هیچ اعتبارسنجی اضافی انجام نمی‌دهد. پیاده‌سازی‌های امضاکننده باید در مصرف این داده بسیار محتاط باشند. امضاکننده‌ها نباید بدون انجام مراحل راستی‌آزمایی مناسب، به‌طور ذاتی به این داده اعتماد کنند. امضاکننده‌ها باید کلیدها و مقادیری را که پشتیبانی می‌کنند مستند کنند و باید درخواست‌هایی را که شامل کلیدهای ناشناخته هستند رد کنند.

نودها به‌طور خودکار مجوز ایجاد PodCertificateRequest و خواندن PodCertificateRequestهای مرتبط با خود (بر اساس فیلد `spec.nodeName`) را دریافت می‌کنند. افزونه‌ی پذیرش `NodeRestriction`، در صورت فعال بودن، تضمین می‌کند که نودها فقط بتوانند PodCertificateRequestهایی ایجاد کنند که متناظر با یک Pod واقعی باشد که هم‌اکنون روی آن نود در حال اجراست.

پس از ایجاد، `spec` یک PodCertificateRequest تغییرناپذیر (immutable) است.

برخلاف CSRها، PodCertificateRequestها مرحله‌ی تأیید ندارند. به‌محض ایجاد PodCertificateRequest، کنترل‌کننده‌ی امضاکننده مستقیماً درباره‌ی صدور یا رد درخواست تصمیم می‌گیرد. همچنین اگر هنگام تلاش برای صدور درخواست با خطای دائمی مواجه شود، می‌تواند درخواست را به‌عنوان ناموفق علامت‌گذاری کند.

برای انجام هر یک از این اقدامات، کنترل‌کننده‌ی امضاکننده باید هم روی نوع PodCertificateRequest و هم روی نام امضاکننده مجوزهای مناسب داشته باشد:
* Verbs: **update**، group: `certificates.k8s.io`، resource: `podcertificaterequests/status`
* Verbs: **sign**، group: `certificates.k8s.io`، resource: `signers`، resourceName: `<signerNameDomain>/<signerNamePath>` یا `<signerNameDomain>/*`

کنترل‌کننده‌ی امضاکننده آزاد است اطلاعاتی فراتر از آنچه در درخواست آمده است را نیز در نظر بگیرد، اما می‌تواند به صحت اطلاعات موجود در درخواست اتکا کند. برای مثال، کنترل‌کننده‌ی امضاکننده ممکن است Pod را بارگذاری کند و حاشیه‌نویسی‌های (annotation) تنظیم‌شده روی آن را بخواند، یا یک SubjectAccessReview روی ServiceAccount انجام دهد.

برای صدور گواهی در پاسخ به یک درخواست، کنترل‌کننده‌ی امضاکننده:
* یک شرط `Issued` به `status.conditions` اضافه می‌کند.
* گواهی صادرشده را در `status.certificateChain` قرار می‌دهد.
* فیلدهای `NotBefore` و `NotAfter` گواهی را در فیلدهای `status.notBefore` و `status.notAfter` قرار می‌دهد &mdash; این فیلدها برای کمک به اشکال‌زدایی در API کوبرنتیز به‌صورت denormalized نگهداری می‌شوند.
* با استفاده از `status.beginRefreshAt` زمانی را برای آغاز تلاش جهت نوسازی گواهی پیشنهاد می‌کند.

برای رد یک درخواست، کنترل‌کننده‌ی امضاکننده یک شرط "Denied" به `status.conditions[]` اضافه می‌کند.

برای علامت‌گذاری یک درخواست به‌عنوان ناموفق، کنترل‌کننده‌ی امضاکننده یک شرط "Failed" به `status.conditions[]` اضافه می‌کند.

همه‌ی این شرط‌ها متقابلاً ناسازگارند (mutually exclusive) و باید وضعیت "True" داشته باشند. هیچ نوع شرط دیگری روی PodCertificateRequestها مجاز نیست. علاوه بر این، به‌محض تنظیم هر یک از این شرط‌ها، فیلد `status` تغییرناپذیر می‌شود.

مانند همه‌ی شرط‌ها، فیلد `status.conditions[].reason` قرار است حاوی یک کد قابل‌خواندن برای ماشین باشد که شرط را به‌صورت TitleCase توصیف می‌کند. فیلد `status.conditions[].message` برای توضیح آزاد و قابل‌استفاده برای انسان در نظر گرفته شده است.

برای اطمینان از اینکه PodCertificateRequestهای پایانی‌شده در کلاستر انباشته نمی‌شوند، یک کنترل‌کننده در `kube-controller-manager` تمام PodCertificateRequestهای قدیمی‌تر از ۱۵ دقیقه را حذف می‌کند. انتظار می‌رود همه‌ی جریان‌های صدور گواهی در همین محدوده‌ی ۱۵ دقیقه‌ای تکمیل شوند.

## Cluster trust bundleها {#cluster-trust-bundles}

{{< feature-state feature_gate_name="ClusterTrustBundle" >}}


ClusterTrustBundle یک آبجکت با دامنه‌ی کلاستر است که برای توزیع لنگرهای اعتماد X.509 (گواهی‌های ریشه) به بارهای کاری درون کلاستر به کار می‌رود. این آبجکت‌ها طوری طراحی شده‌اند که با مفهوم [امضاکننده](#signers) در CertificateSigningRequestها به‌خوبی کار کنند.

ClusterTrustBundleها را می‌توان در دو حالت استفاده کرد:
[متصل به امضاکننده](#ctb-signer-linked) و [بدون اتصال به امضاکننده](#ctb-signer-unlinked).

### ویژگی‌ها و اعتبارسنجی مشترک {#ctb-common}

همه‌ی آبجکت‌های ClusterTrustBundle اعتبارسنجی سختگیرانه‌ای روی محتوای فیلد `trustBundle` خود دارند. این فیلد باید شامل یک یا چند گواهی X.509 با سریال‌سازی DER باشد که هر یک درون یک بلوک PEM از نوع `CERTIFICATE` قرار گرفته است. گواهی‌ها باید به‌عنوان گواهی‌های معتبر X.509 قابل تجزیه باشند.

ویژگی‌های نامعمول PEM، مانند داده‌های میان‌بلوکی و هدرهای درون‌بلوکی، یا در اعتبارسنجی آبجکت رد می‌شوند یا مصرف‌کنندگان آبجکت می‌توانند آن‌ها را نادیده بگیرند. علاوه بر این، مصرف‌کنندگان مجازند گواهی‌های موجود در bundle را با ترتیب دلخواه اما پایدار خودشان مرتب‌سازی مجدد کنند.

آبجکت‌های ClusterTrustBundle باید درون کلاستر قابل‌خواندن برای همگان در نظر گرفته شوند. اگر کلاستر شما از احراز مجوز [RBAC](/docs/reference/access-authn-authz/rbac/) استفاده می‌کند، همه‌ی ServiceAccountها یک مجوز پیش‌فرض دارند که به آن‌ها اجازه می‌دهد همه‌ی آبجکت‌های ClusterTrustBundle را **get**، **list** و **watch** کنند. اگر از سازوکار احراز مجوز خودتان استفاده می‌کنید و ClusterTrustBundleها را در کلاستر فعال کرده‌اید، باید قاعده‌ای معادل تنظیم کنید تا این آبجکت‌ها درون کلاستر عمومی شوند و همان‌گونه که انتظار می‌رود کار کنند.

اگر به‌صورت پیش‌فرض در کلاستر خود مجوز فهرست‌کردن cluster trust bundleها را ندارید، می‌توانید هویت یک service account را که به آن دسترسی دارید جعل (impersonate) کنید تا ClusterTrustBundleهای موجود را ببینید:

```bash
kubectl get clustertrustbundles --as='system:serviceaccount:mynamespace:default'
```

### ClusterTrustBundleهای متصل به امضاکننده {#ctb-signer-linked}

ClusterTrustBundleهای متصل به امضاکننده با یک _نام امضاکننده_ مرتبط می‌شوند، به این صورت:

```yaml
apiVersion: certificates.k8s.io/v1
kind: ClusterTrustBundle
metadata:
  name: example.com:mysigner:foo
spec:
  signerName: example.com/mysigner
  trustBundle: "<... PEM data ...>"
```

این ClusterTrustBundleها قرار است توسط یک کنترل‌کننده‌ی مختص امضاکننده در کلاستر نگهداری شوند، بنابراین چند ویژگی امنیتی دارند:

* برای ایجاد یا به‌روزرسانی یک ClusterTrustBundle متصل به امضاکننده، باید مجاز به انجام **attest** روی آن امضاکننده باشید (فعل مجوزدهی سفارشی `attest`، گروه API ‏`certificates.k8s.io`؛ مسیر منبع `signers`). می‌توانید احراز مجوز را برای نام منبع مشخص `<signerNameDomain>/<signerNamePath>` پیکربندی کنید یا الگویی مانند `<signerNameDomain>/*` را تطبیق دهید.
* ClusterTrustBundleهای متصل به امضاکننده **باید** با پیشوندی مشتق‌شده از فیلد `spec.signerName` خود نام‌گذاری شوند. اسلش‌ها (`/`) با دونقطه (`:`) جایگزین می‌شوند و یک دونقطه‌ی پایانی افزوده می‌شود. پس از آن یک نام دلخواه می‌آید. برای مثال، امضاکننده‌ی `example.com/mysigner` می‌تواند به ClusterTrustBundle با نام `example.com:mysigner:<arbitrary-name>` متصل شود.

ClusterTrustBundleهای متصل به امضاکننده معمولاً در بارهای کاری با ترکیبی از یک [انتخابگر فیلد (field selector)](/docs/concepts/overview/working-with-objects/field-selectors/) روی نام امضاکننده و یک [انتخابگر برچسب (label selector)](/docs/concepts/overview/working-with-objects/labels/#label-selectors) جداگانه مصرف می‌شوند.

### ClusterTrustBundleهای بدون اتصال به امضاکننده {#ctb-signer-unlinked}

ClusterTrustBundleهای بدون اتصال به امضاکننده فیلد `spec.signerName` خالی دارند، به این صورت:

```yaml
apiVersion: certificates.k8s.io/v1
kind: ClusterTrustBundle
metadata:
  name: foo
spec:
  # no signerName specified, so the field is blank
  trustBundle: "<... PEM data ...>"
```

این آبجکت‌ها عمدتاً برای موارد استفاده‌ی پیکربندی کلاستر در نظر گرفته شده‌اند. هر ClusterTrustBundle بدون اتصال به امضاکننده یک آبجکت مستقل است، برخلاف رفتار گروه‌بندی معمول ClusterTrustBundleهای متصل به امضاکننده.

ClusterTrustBundleهای بدون اتصال به امضاکننده نیازمند فعل `attest` نیستند. در عوض، دسترسی به آن‌ها را مستقیماً با سازوکارهای معمول، مانند کنترل دسترسی مبتنی بر نقش (RBAC)، کنترل می‌کنید.

برای تمایز آن‌ها از ClusterTrustBundleهای متصل به امضاکننده، نام ClusterTrustBundleهای بدون اتصال به امضاکننده **نباید** شامل دونقطه (`:`) باشد.

### دسترسی به ClusterTrustBundleها از داخل Podها {#ctb-projection}

{{< feature-state feature_gate_name="ClusterTrustBundleProjection" >}}

محتوای ClusterTrustBundleها را می‌توان، مشابه ConfigMapها و Secretها، به فایل‌سیستم کانتینر تزریق کرد.
برای جزئیات بیشتر به [منبع حجم پروژکشن‌شده clusterTrustBundle](/docs/concepts/storage/projected-volumes#clustertrustbundle) مراجعه کنید.

## {{% heading "whatsnext" %}}

* مطلب [مدیریت گواهی‌های TLS در یک کلاستر](/docs/tasks/tls/managing-tls-in-a-cluster/) را بخوانید
* مطلب [صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/) را بخوانید
* کد منبع [امضاکننده](https://github.com/kubernetes/kubernetes/blob/32ec6c212ec9415f604ffc1f4c1f29b782968ff1/pkg/controller/certificates/signer/cfssl_signer.go) داخلی kube-controller-manager را مشاهده کنید
* کد منبع [تأییدکننده](https://github.com/kubernetes/kubernetes/blob/32ec6c212ec9415f604ffc1f4c1f29b782968ff1/pkg/controller/certificates/approver/sarapprove.go) داخلی kube-controller-manager را مشاهده کنید
* برای جزئیات خود X.509، به بخش ۳.۱ از [RFC 5280](https://tools.ietf.org/html/rfc5280#section-3.1) مراجعه کنید
* برای اطلاع از نحو درخواست‌های امضای گواهی PKCS#10، به [RFC 2986](https://tools.ietf.org/html/rfc2986) مراجعه کنید
* درباره‌ی API مربوط به ClusterTrustBundle بخوانید:
  * {{< page-api-reference kind="ClusterTrustBundle" >}}
