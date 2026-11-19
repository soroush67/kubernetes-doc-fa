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

APIهای گواهی و بستهٔ اعتماد (trust bundle) در کوبرنتیز، تأمین خودکار اعتبارنامه‌های
[X.509](https://www.itu.int/rec/T-REC-X.509) را ممکن می‌کنند. این APIها رابطی برنامه‌نویسی‌شده در اختیار کلاینت‌های API کوبرنتیز
قرار می‌دهند تا بتوانند {{< glossary_tooltip term_id="certificate" text="گواهی‌های" >}} X.509 را از یک مرجع صدور گواهی (Certificate Authority یا CA) درخواست و دریافت کنند.

توزیع [بسته‌های اعتماد](#cluster-trust-bundles) نیز پشتیبانی می‌شود.

<!-- body -->

## درخواست‌های امضای گواهی

{{< feature-state for_k8s_version="v1.19" state="stable" >}}


از منبع [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/)
(CSR) برای درخواست امضای یک گواهی توسط امضاکننده‌ای مشخص استفاده می‌شود. پس از ثبت، این درخواست
پیش از امضای نهایی ممکن است تأیید یا رد شود.


### فرایند امضای درخواست

با نوع منبع CertificateSigningRequest، یک کلاینت می‌تواند بر اساس یک درخواست امضا،
صدور یک گواهی X.509 را درخواست کند.
آبجکت CertificateSigningRequest یک درخواست امضای PKCS#10 با کدگذاری PEM را در
فیلد `spec.request` در خود دارد. هر CertificateSigningRequest امضاکننده (گیرنده‌ای که درخواست
برای او فرستاده می‌شود) را با فیلد `spec.signerName` مشخص می‌کند.
توجه کنید که از نسخهٔ `certificates.k8s.io/v1` به بعد، `spec.signerName` کلیدی الزامی است.
در کوبرنتیز v1.22 و نسخه‌های بعدی، کلاینت‌ها می‌توانند به‌صورت اختیاری فیلد `spec.expirationSeconds`
را تنظیم کنند تا طول عمر مشخصی برای گواهی صادرشده درخواست کنند. کمترین مقدار معتبر
برای این فیلد `600`، یعنی ده دقیقه، است.

هر CertificateSigningRequest پس از ایجاد، باید پیش از امضا شدن تأیید شود.
بسته به امضاکنندهٔ انتخاب‌شده، ممکن است یک CertificateSigningRequest به‌طور خودکار
از سوی یک {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} تأیید شود.
در غیر این صورت، باید آن را به‌صورت دستی، یا از طریق REST API (یا client-go)
یا با اجرای `kubectl certificate approve`، تأیید کرد. به همین ترتیب، می‌توان یک CertificateSigningRequest را رد نیز کرد؛
در این حالت به امضاکنندهٔ پیکربندی‌شده اعلام می‌شود که نباید آن درخواست را امضا کند.

برای گواهی‌های تأییدشده، گام بعدی امضا است. کنترل‌کنندهٔ امضای مربوط
ابتدا بررسی می‌کند که شرایط امضا برقرار باشد و سپس گواهی را ایجاد می‌کند.
آنگاه این کنترل‌کننده CertificateSigningRequest را به‌روزرسانی می‌کند و گواهی جدید را در
فیلد `status.certificate` همان آبجکت CertificateSigningRequest موجود ذخیره می‌کند.
فیلد `status.certificate` یا خالی است یا یک گواهی X.509 با کدگذاری PEM در خود دارد.
تا زمانی که امضاکننده این کار را انجام نداده است، فیلد `status.certificate` در CertificateSigningRequest خالی می‌ماند.

پس از پر شدن فیلد `status.certificate`، درخواست تکمیل شده است و کلاینت‌ها اکنون می‌توانند
داده‌های PEM گواهی امضاشده را از منبع CertificateSigningRequest دریافت کنند.
اگر شرایط تأیید برقرار نباشد، امضاکننده‌ها می‌توانند امضای گواهی را رد کنند.

برای کاهش تعداد منابع CertificateSigningRequest قدیمی که در کلاستر باقی می‌مانند، یک کنترل‌کنندهٔ
جمع‌آوری زباله (garbage collection) به‌طور دوره‌ای اجرا می‌شود. این فرایند، CertificateSigningRequestهایی را
که وضعیتشان در مدتی معین تغییر نکرده است حذف می‌کند:

* درخواست‌های تأییدشده: پس از ۱ ساعت به‌طور خودکار حذف می‌شوند
* درخواست‌های ردشده: پس از ۱ ساعت به‌طور خودکار حذف می‌شوند
* درخواست‌های ناموفق: پس از ۱ ساعت به‌طور خودکار حذف می‌شوند
* درخواست‌های در انتظار: پس از ۲۴ ساعت به‌طور خودکار حذف می‌شوند
* همهٔ درخواست‌ها: پس از منقضی شدن گواهی صادرشده به‌طور خودکار حذف می‌شوند

### مجوزدهی برای امضای گواهی {#authorization}

برای اجازه دادن به ایجاد یک CertificateSigningRequest و بازیابی هر CertificateSigningRequest:

* افعال: `create`، `get`، `list`، `watch`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests`

برای نمونه:

{{% code_sample file="access/certificate-signing-request/clusterrole-create.yaml" %}}

برای اجازه دادن به تأیید یک CertificateSigningRequest:

* افعال: `get`، `list`، `watch`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests`
* افعال: `update`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests/approval`
* افعال: `approve`، گروه: `certificates.k8s.io`، منبع: `signers`، resourceName: `<signerNameDomain>/<signerNamePath>` یا `<signerNameDomain>/*`

برای نمونه:

{{% code_sample file="access/certificate-signing-request/clusterrole-approve.yaml" %}}

برای اجازه دادن به امضای یک CertificateSigningRequest:

* افعال: `get`، `list`، `watch`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests`
* افعال: `update`، گروه: `certificates.k8s.io`، منبع: `certificatesigningrequests/status`
* افعال: `sign`، گروه: `certificates.k8s.io`، منبع: `signers`، resourceName: `<signerNameDomain>/<signerNamePath>` یا `<signerNameDomain>/*`

{{% code_sample file="access/certificate-signing-request/clusterrole-sign.yaml" %}}


## امضاکننده‌ها

امضاکننده‌ها به‌صورت انتزاعی نمایانگر موجودیت یا موجودیت‌هایی هستند که ممکن است یک گواهی امنیتی را
امضا کنند یا امضا کرده باشند.

هر امضاکننده‌ای که بیرون از یک کلاستر خاص در دسترس قرار می‌گیرد، باید دربارهٔ نحوهٔ کارکرد خود
اطلاعاتی ارائه دهد تا مصرف‌کنندگان بفهمند این موضوع برای CertificateSigningRequestها
و (در صورت فعال بودن) [ClusterTrustBundleها](#cluster-trust-bundles) چه معنایی دارد.
این اطلاعات شامل موارد زیر است:

1. **توزیع اعتماد**: لنگرهای اعتماد (trust anchor) — یعنی گواهی‌های CA یا بسته‌های گواهی — چگونه توزیع می‌شوند.
1. **موضوع‌های (subject) مجاز**: هرگونه محدودیت، و رفتار امضاکننده هنگامی که موضوعی غیرمجاز درخواست شود.
1. **افزونه‌های x509 مجاز**: از جمله subjectAltNameهای IP، DNS،
   ایمیل، URI و غیره، و رفتار امضاکننده هنگامی که افزونه‌ای غیرمجاز درخواست شود.
1. **کاربردهای کلید / کاربردهای گستردهٔ کلید مجاز**: هرگونه محدودیت، و رفتار امضاکننده
   هنگامی که در CSR کاربردهایی متفاوت با کاربردهای تعیین‌شده از سوی امضاکننده مشخص شده باشد.
1. **انقضا/طول عمر گواهی**: اینکه آیا امضاکننده آن را ثابت تعیین می‌کند، مدیر می‌تواند آن را پیکربندی کند، یا با فیلد `spec.expirationSeconds` در CSR تعیین می‌شود و غیره؛
   و نیز رفتار امضاکننده هنگامی که انقضای تعیین‌شده از سوی امضاکننده با فیلد `spec.expirationSeconds` در CSR متفاوت باشد.
1. **مجاز/غیرمجاز بودن بیت CA**: و رفتار امضاکننده هنگامی که یک CSR درخواست گواهی CA داشته باشد ولی امضاکننده آن را مجاز نداند.

معمولاً پس از تأیید CSR و صدور گواهی، فیلد `status.certificate` در یک CertificateSigningRequest
تنها یک گواهی X.509 با کدگذاری PEM در خود دارد.
برخی امضاکننده‌ها چند گواهی را در فیلد `status.certificate` ذخیره می‌کنند. در
این حالت، مستندات امضاکننده باید معنای گواهی‌های اضافه را مشخص کند؛
برای نمونه، ممکن است این مجموعه شامل خود گواهی به‌همراه گواهی‌های میانی باشد
که باید در دست‌دهی (handshake) TLS ارائه شوند.

اگر می‌خواهید _لنگر اعتماد_ (گواهی ریشه) را در دسترس قرار دهید، این کار باید جدا
از CertificateSigningRequest و فیلد `status.certificate` آن انجام شود. برای نمونه،
می‌توانید از یک ClusterTrustBundle استفاده کنید.

قالب درخواست امضای PKCS#10 هیچ سازوکار استانداردی برای تعیین انقضا یا طول عمر
گواهی ندارد. بنابراین انقضا یا طول عمر باید از طریق فیلد `spec.expirationSeconds`
در آبجکت CSR تنظیم شود. هنگامی که `spec.expirationSeconds` مشخص نشده باشد، امضاکننده‌های داخلی
گزینهٔ پیکربندی `ClusterSigningDuration` (فلگ خط فرمان `--cluster-signing-duration` در kube-controller-manager)
را که مقدار پیش‌فرض آن ۱ سال است، به‌عنوان مقدار پیش‌فرض به کار می‌برند. هنگامی که `spec.expirationSeconds`
مشخص شده باشد، کمینهٔ `spec.expirationSeconds` و `ClusterSigningDuration` استفاده
می‌شود.

{{< note >}}
فیلد `spec.expirationSeconds` در کوبرنتیز v1.22 اضافه شد. نسخه‌های قدیمی‌تر کوبرنتیز این فیلد را رعایت نمی‌کنند.
سرورهای API کوبرنتیز پیش از v1.22 هنگام ایجاد آبجکت، این فیلد را بی‌صدا حذف می‌کنند.
{{< /note >}}

### امضاکننده‌های کوبرنتیز

کوبرنتیز امضاکننده‌های داخلی‌ای فراهم می‌کند که هر کدام یک `signerName` شناخته‌شده دارند:

1. `kubernetes.io/kube-apiserver-client`: گواهی‌هایی را امضا می‌کند که سرور API آن‌ها را به‌عنوان گواهی کلاینت می‌پذیرد.
   {{< glossary_tooltip term_id="kube-controller-manager" >}} هرگز درخواست‌های آن را به‌طور خودکار تأیید نمی‌کند.
   1. توزیع اعتماد: سرور API باید گواهی‌های امضاشده را به‌عنوان گواهی کلاینت بپذیرد. بستهٔ CA از هیچ راه دیگری توزیع نمی‌شود.
   1. موضوع‌های مجاز - هیچ محدودیتی روی موضوع وجود ندارد، اما تأییدکنندگان و امضاکنندگان می‌توانند از تأیید یا امضا خودداری کنند.
      برخی موضوع‌ها، مانند کاربران یا گروه‌هایی در سطح cluster-admin، در توزیع‌ها و نصب‌های مختلف متفاوت‌اند،
      اما پیش از تأیید و امضا شایستهٔ بررسی دقیق‌تری هستند.
      افزونهٔ پذیرش (admission plugin) `CertificateSubjectRestriction` به‌طور پیش‌فرض برای محدود کردن `system:masters` فعال است،
      اما این گروه اغلب تنها موضوع در سطح cluster-admin در یک کلاستر نیست.
   1. افزونه‌های x509 مجاز - افزونه‌های subjectAltName و کاربرد کلید را رعایت می‌کند و سایر افزونه‌ها را کنار می‌گذارد.
   1. کاربردهای کلید مجاز - باید شامل `["client auth"]` باشد. نباید کاربردهای کلیدی فراتر از `["digital signature", "key encipherment", "client auth"]` را شامل شود.
   1. انقضا/طول عمر گواهی - در پیاده‌سازی kube-controller-manager برای این امضاکننده، برابر با کمینهٔ
      گزینهٔ `--cluster-signing-duration` و، در صورت مشخص بودن، فیلد `spec.expirationSeconds` در آبجکت CSR تنظیم می‌شود.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/kube-apiserver-client-kubelet`: گواهی‌های کلاینتی را امضا می‌کند که سرور API آن‌ها را به‌عنوان
   گواهی کلاینت می‌پذیرد.
   ممکن است {{< glossary_tooltip term_id="kube-controller-manager" >}} درخواست‌های آن را به‌طور خودکار تأیید کند.
   1. توزیع اعتماد: سرور API باید گواهی‌های امضاشده را به‌عنوان گواهی کلاینت بپذیرد. بستهٔ CA
      از هیچ راه دیگری توزیع نمی‌شود.
   1. موضوع‌های مجاز - سازمان‌ها دقیقاً `["system:nodes"]` و نام مشترک (common name) برابر با "`system:node:${NODE_NAME}`" است.
   1. افزونه‌های x509 مجاز - افزونه‌های کاربرد کلید را رعایت می‌کند، افزونه‌های subjectAltName را ممنوع می‌کند و سایر افزونه‌ها را حذف می‌کند.
   1. کاربردهای کلید مجاز - `["key encipherment", "digital signature", "client auth"]` یا `["digital signature", "client auth"]`.
   1. انقضا/طول عمر گواهی - در پیاده‌سازی kube-controller-manager برای این امضاکننده، برابر با کمینهٔ
      گزینهٔ `--cluster-signing-duration` و، در صورت مشخص بودن، فیلد `spec.expirationSeconds` در آبجکت CSR تنظیم می‌شود.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/kubelet-serving`: گواهی‌های سرویس‌دهی (serving) را امضا می‌کند که سرور API آن‌ها را به‌عنوان گواهی سرویس‌دهی معتبر kubelet
   می‌پذیرد، اما هیچ تضمین دیگری ندارند.
   {{< glossary_tooltip term_id="kube-controller-manager" >}} هرگز درخواست‌های آن را به‌طور خودکار تأیید نمی‌کند.
   1. توزیع اعتماد: سرور API باید گواهی‌های امضاشده را برای خاتمه دادن به اتصال‌ها به یک kubelet معتبر بداند.
      بستهٔ CA از هیچ راه دیگری توزیع نمی‌شود.
   1. موضوع‌های مجاز - سازمان‌ها دقیقاً `["system:nodes"]` و نام مشترک برابر با "`system:node:${NODE_NAME}`" است.
   1. افزونه‌های x509 مجاز - افزونه‌های کاربرد کلید و subjectAltNameهای DNSName/IPAddress را رعایت می‌کند، افزونه‌های subjectAltName از نوع EmailAddress و
      URI را ممنوع می‌کند و سایر افزونه‌ها را حذف می‌کند. دست‌کم یک subjectAltName از نوع DNS یا IP باید وجود داشته باشد.
   1. کاربردهای کلید مجاز - `["key encipherment", "digital signature", "server auth"]` یا `["digital signature", "server auth"]`.
   1. انقضا/طول عمر گواهی - در پیاده‌سازی kube-controller-manager برای این امضاکننده، برابر با کمینهٔ
      گزینهٔ `--cluster-signing-duration` و، در صورت مشخص بودن، فیلد `spec.expirationSeconds` در آبجکت CSR تنظیم می‌شود.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/legacy-unknown`: هیچ تضمینی برای اعتماد ندارد. برخی توزیع‌های شخص ثالث کوبرنتیز
   ممکن است گواهی‌های کلاینتی را که با آن امضا شده‌اند بپذیرند. API پایدار CertificateSigningRequest (نسخهٔ `certificates.k8s.io/v1` و بعد از آن)
   اجازه نمی‌دهد `signerName` برابر با `kubernetes.io/legacy-unknown` تنظیم شود.
   {{< glossary_tooltip term_id="kube-controller-manager" >}} هرگز درخواست‌های آن را به‌طور خودکار تأیید نمی‌کند.
   1. توزیع اعتماد: هیچ. برای این امضاکننده در کلاستر کوبرنتیز هیچ اعتماد یا سازوکار توزیع استانداردی وجود ندارد.
   1. موضوع‌های مجاز - هر موضوعی
   1. افزونه‌های x509 مجاز - افزونه‌های subjectAltName و کاربرد کلید را رعایت می‌کند و سایر افزونه‌ها را کنار می‌گذارد.
   1. کاربردهای کلید مجاز - هر کاربردی
   1. انقضا/طول عمر گواهی - در پیاده‌سازی kube-controller-manager برای این امضاکننده، برابر با کمینهٔ
      گزینهٔ `--cluster-signing-duration` و، در صورت مشخص بودن، فیلد `spec.expirationSeconds` در آبجکت CSR تنظیم می‌شود.
   1. مجاز/غیرمجاز بودن بیت CA - مجاز نیست.

1. `kubernetes.io/kube-apiserver-serving`: گواهی‌هایی را امضا می‌کند که می‌توان از آن‌ها برای راستی‌آزمایی گواهی‌های سرویس‌دهی kube-apiserver
   استفاده کرد. امضا و تأیید بیرون از kube-controller-manager انجام می‌شوند.
    - {{< feature-state feature_gate_name="ClusterTrustBundle" >}}
    1. توزیع اعتماد: kube-apiserver از گواهی‌های امضاشده برای احراز هویت سرور در TLS
       استفاده می‌کند. بستهٔ CA با یک آبجکت ClusterTrustBundle توزیع می‌شود
       که با نام امضاکنندهٔ `kubernetes.io/kube-apiserver-serving` قابل شناسایی است.
    1. موضوع‌های مجاز - استفاده از خود «Subject» برای احراز هویت سرور در TLS طبق RFC2818 منسوخ شده است. با این حال،
       باید همچنان از همان قواعد مربوط به {{< glossary_tooltip text="SANهای" term_id="san" >}} از نوع DNS/IP
       که در بخش «افزونه‌های x509 مجاز» در ادامه آمده است پیروی کند.
    1. افزونه‌های x509 مجاز - افزونه‌های subjectAltName و کاربرد کلید را رعایت می‌کند. دست‌کم
       یک subjectAltName از نوع DNS یا IP باید وجود داشته باشد. مقادیر SAN از نوع DNS/IP در گواهی‌ها
       باید به نام میزبان/IP مربوط به kube-apiserver ارجاع دهند یا به آن تفکیک (resolve) شوند.
    1. کاربردهای کلید مجاز - ["key encipherment", "digital signature", "server auth"] یا ["digital signature", "server auth"].
    1. انقضا/طول عمر گواهی - بیشینهٔ طول عمر توصیه‌شده ۳۰ روز است.
    1. مجاز/غیرمجاز بودن بیت CA - پروژهٔ کوبرنتیز آن را توصیه نمی‌کند.

{{< note >}}
فیلد `spec.expirationSeconds` در کوبرنتیز v1.22 اضافه شد. نسخه‌های قدیمی‌تر کوبرنتیز این فیلد را رعایت نمی‌کنند.
سرورهای API کوبرنتیز پیش از v1.22 هنگام ایجاد آبجکت، این فیلد را بی‌صدا حذف می‌کنند.
{{< /note >}}

مؤلفهٔ kube-controller-manager برای همهٔ امضاکننده‌های داخلی به‌جز `kubernetes.io/kube-apiserver-serving`،
[امضای control plane](#signer-control-plane) را پیاده‌سازی می‌کند. خطاهای همهٔ این امضاکننده‌ها فقط در لاگ‌های kube-controller-manager گزارش می‌شوند.
امضای گواهی‌ها در دامنهٔ اعتماد امضاکنندهٔ `kubernetes.io/kube-apiserver-serving` به‌طور کامل در اختیار
مدیر یا مدیران کلاستر است.

هرگونه اعتماد بیرون از موارد شرح‌داده‌شده در بالا صرفاً
تصادفی است. برای نمونه، برخی توزیع‌ها ممکن است `kubernetes.io/legacy-unknown` را به‌عنوان گواهی کلاینت برای
kube-apiserver بپذیرند، اما این رفتار استاندارد نیست.
هیچ‌یک از این کاربردها به هیچ وجه با `.data[ca.crt]` در Secretهای توکن ServiceAccount ارتباطی ندارند. آن بستهٔ CA تنها
تضمین می‌کند که اتصال به سرور API از طریق سرویس پیش‌فرض (`kubernetes.default.svc`) قابل راستی‌آزمایی باشد.

### امضاکننده‌های سفارشی

شما همچنین می‌توانید امضاکنندهٔ سفارشی خود را معرفی کنید. نام این امضاکننده باید پیشوندی مشابه داشته باشد، اما از
نام دامنهٔ خودتان استفاده کند. برای نمونه، اگر نمایندهٔ یک پروژهٔ متن‌باز هستید که از دامنهٔ `open-fictional.example` استفاده می‌کند،
می‌توانید `issuer.open-fictional.example/service-mesh` را به‌عنوان نام امضاکننده به کار ببرید.

هر امضاکنندهٔ سفارشی برای صدور گواهی از API کوبرنتیز استفاده می‌کند. [امضاکننده‌های مبتنی بر API](#signer-api) را ببینید.

## امضا

### امضاکنندهٔ control plane {#signer-control-plane}

بخش control plane کوبرنتیز هر یک از
[امضاکننده‌های کوبرنتیز](/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers)
را به‌عنوان بخشی از kube-controller-manager پیاده‌سازی می‌کند.

برای یک نمونهٔ عملی از ایجاد یک CertificateSigningRequest و تأیید و
امضای آن به‌دست control plane کوبرنتیز، به
[صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/) مراجعه کنید.

{{< note >}}
پیش از کوبرنتیز v1.18، مؤلفهٔ kube-controller-manager هر CSRی را که
به‌عنوان تأییدشده علامت‌گذاری شده بود امضا می‌کرد.
{{< /note >}}

## تأیید یا رد  {#approval-rejection}

پیش از آنکه یک [امضاکننده](#signers) بر اساس یک CertificateSigningRequest گواهی صادر کند،
معمولاً بررسی می‌کند که صدور گواهی برای آن CSR _تأیید_ شده باشد.

### تأیید خودکار در control plane {#approval-rejection-control-plane}

مؤلفهٔ kube-controller-manager یک تأییدکنندهٔ داخلی برای گواهی‌هایی با
signerName برابر با `kubernetes.io/kube-apiserver-client-kubelet` دارد که بررسی مجوزهای گوناگون
روی CSRهای مربوط به اعتبارنامه‌های نود را به سازوکار مجوزدهی واگذار می‌کند.
این مؤلفه برای بررسی مجوز تأیید گواهی، منابع SubjectAccessReview را
با درخواست POST به سرور API می‌فرستد.

### تأیید یا رد با استفاده از `kubectl` {#approval-rejection-kubectl}

مدیر کوبرنتیز (با مجوزهای مناسب) می‌تواند CertificateSigningRequestها را با فرمان‌های
`kubectl certificate approve` و `kubectl certificate deny` به‌صورت دستی تأیید
(یا رد) کند.

برای تأیید یک CSR با kubectl:

```shell
kubectl certificate approve <certificate-signing-request-name>
```

به همین ترتیب، برای رد یک CSR:

```shell
kubectl certificate deny <certificate-signing-request-name>
```

### تأیید یا رد با استفاده از API کوبرنتیز {#approval-rejection-api-client}

کاربران REST API می‌توانند CSRها را با ارسال یک درخواست UPDATE به زیرمنبع `approval`
مربوط به CSR موردنظر تأیید کنند. برای نمونه، می‌توانید یک
{{< glossary_tooltip term_id="operator-pattern" text="اپراتور" >}} بنویسید که نوع خاصی از CSRها را
زیر نظر می‌گیرد و سپس برای تأیید آن‌ها یک UPDATE می‌فرستد.

هنگام ارسال درخواست تأیید یا رد، بسته به وضعیتی که تشخیص می‌دهید، یکی از شرط‌های وضعیت
`Approved` یا `Denied` را تنظیم کنید:

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

معمولاً `status.conditions.reason` را با یک کد دلیل ماشین‌پسند در قالب TitleCase
تنظیم می‌کنند؛ این تنها یک قرارداد است و می‌توانید هر مقداری که می‌خواهید
برای آن بگذارید. اگر می‌خواهید توضیحی برای خوانندگان انسانی اضافه کنید، از
فیلد `status.conditions.message` استفاده کنید.

## امضاکننده‌های مبتنی بر API {#signer-api}

کاربران REST API می‌توانند CSRها را با ارسال یک درخواست **update** به زیرمنبع `status` در CSR مورد نظر امضا کنند.

در این درخواست، فیلد `status.certificate` باید طوری تنظیم شود که گواهی امضاشده را در خود داشته باشد. این فیلد یک یا چند گواهی با کدگذاری PEM را در بر می‌گیرد.

همهٔ بلوک‌های PEM باید برچسب «CERTIFICATE» داشته باشند و هیچ سرآیندی (header) نداشته باشند. داده‌های کدگذاری‌شده نیز باید یک ساختار Certificate از نوع ASN.1 با کدگذاری BER باشند، همان‌طور که در [بخش ۴ از RFC5280](https://tools.ietf.org/html/rfc5280#section-4.1) توضیح داده شده است.

نمونه‌ای از محتوای یک گواهی:

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

محتوای غیر PEM ممکن است پیش یا پس از بلوک‌های PEM از نوع CERTIFICATE بیاید و اعتبارسنجی نمی‌شود. این امکان برای افزودن متن توضیحی در نظر گرفته شده است، همان‌طور که در [بخش ۵.۲ از RFC7468](https://www.rfc-editor.org/rfc/rfc7468#section-5.2) آمده است.

این فیلد در قالب JSON یا YAML با کدگذاری base-64 نمایش داده می‌شود.
پس از تأیید و امضای یک CertificateSigningRequest، گواهی امضاشده در فیلد `status.certificate` آن قرار می‌گیرد. یک CertificateSigningRequest که گواهی نمونهٔ بالا را در خود دارد، چنین شکلی خواهد داشت:

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
...
status:
  certificate: "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JS..."
```

## درخواست‌های PodCertificateRequest {#pod-certificate-requests}

{{< feature-state feature_gate_name="PodCertificateRequest" >}}


آبجکت‌های PodCertificateRequest آبجکت‌هایی در API هستند که برای تأمین گواهی برای بارهای کاری‌ای طراحی شده‌اند که به‌صورت Pod در کلاستر اجرا می‌شوند. کاربر معمولاً مستقیماً با PodCertificateRequestها کار نمی‌کند، بلکه از [منابع حجم (volume) تصویرشدهٔ podCertificate](
/docs/concepts/storage/projected-volumes#podcertificate) استفاده می‌کند. این منابع قابلیتی از `kubelet` هستند که تأمین امن کلید و تازه‌سازی خودکار گواهی را بر عهده دارند. برنامهٔ درون پاد فقط باید بداند گواهی‌ها را چگونه از سیستم فایل بخواند.

آبجکت‌های PodCertificateRequest شبیه CertificateSigningRequestها هستند، اما به‌دلیل کاربرد محدودترشان قالب ساده‌تری دارند.

هر PodCertificateRequest فیلدهای spec زیر را دارد:
* `signerName`: امضاکننده‌ای که این درخواست خطاب به آن است.
* `podName` و `podUID`: پادی که kubelet برای آن گواهی درخواست می‌کند.
* `serviceAccountName` و `serviceAccountUID`: ServiceAccount متناظر با پاد.
* `nodeName` و `nodeUID`: نود متناظر با پاد.
* `maxExpirationSeconds`: بیشترین طول عمری که نویسندهٔ بار کاری برای این گواهی می‌پذیرد. اگر مشخص نشود، مقدار پیش‌فرض ۲۴ ساعت است.
* `stubPKCS10Request`: یک CSR حداقلی از نوع
  [PKCS#10](https://www.rfc-editor.org/rfc/rfc2986). امضاکننده‌ها باید کلید عمومی را از این CSR استخراج کنند. معمولاً امضاکننده لازم نیست کار دیگری با این فیلد انجام دهد، زیرا امضای CSR را API server بررسی می‌کند. درخواست‌های kubelet فقط اطلاعات کلید عمومی را در CSR قرار می‌دهند.
* `unverifiedUserAnnotations`: نگاشتی (map) که کاربر با آن می‌تواند اطلاعات بیشتری را به پیاده‌سازی امضاکننده منتقل کند. این فیلد عیناً از فیلد `userAnnotations` در [منبع حجم تصویرشدهٔ podCertificate](/docs/concepts/storage/projected-volumes#podcertificate) کپی می‌شود. مدخل‌های آن همان اعتبارسنجی حاشیه‌نویسی‌های (annotation) فرادادهٔ آبجکت را دارند، با این تفاوت که همهٔ کلیدها باید پیشوند دامنه داشته باشند. هیچ محدودیتی روی مقادیر وجود ندارد، جز محدودیت اندازهٔ کلی برای کل فیلد. API server به‌جز این اعتبارسنجی‌های پایه، هیچ اعتبارسنجی دیگری انجام نمی‌دهد. پیاده‌سازی‌های امضاکننده باید هنگام استفاده از این داده‌ها بسیار محتاط باشند. امضاکننده‌ها نباید بدون انجام مراحل راستی‌آزمایی مناسب، ذاتاً به این داده‌ها اعتماد کنند. امضاکننده‌ها باید کلیدها و مقادیری را که پشتیبانی می‌کنند مستند کنند و درخواست‌هایی را که کلیدهای ناشناخته دارند رد کنند.

نودها به‌طور خودکار مجوز ایجاد PodCertificateRequestها و خواندن PodCertificateRequestهای مربوط به خود را (بر اساس فیلد `spec.nodeName`) دریافت می‌کنند. افزونهٔ پذیرش (admission plugin) `NodeRestriction`، در صورت فعال بودن، تضمین می‌کند که نودها فقط بتوانند PodCertificateRequestهایی ایجاد کنند که با پادی واقعی و در حال اجرا روی همان نود متناظر باشند.

پس از ایجاد، `spec` یک PodCertificateRequest تغییرناپذیر است.

برخلاف CSRها، PodCertificateRequestها مرحلهٔ تأیید ندارند. پس از ایجاد PodCertificateRequest، کنترل‌کنندهٔ امضاکننده مستقیماً تصمیم می‌گیرد درخواست را صادر کند یا رد کند. این کنترل‌کننده همچنین می‌تواند در صورت برخورد با خطایی دائمی هنگام صدور، درخواست را ناموفق علامت‌گذاری کند.

کنترل‌کنندهٔ امضا برای انجام هر یک از این کارها به مجوزهای مناسب هم روی نوع PodCertificateRequest و هم روی نام امضاکننده نیاز دارد:
* فعل‌ها: **update**، گروه: `certificates.k8s.io`، منبع:
  `podcertificaterequests/status`
* فعل‌ها: **sign**، گروه: `certificates.k8s.io`، منبع: `signers`،
  resourceName: `<signerNameDomain>/<signerNamePath>` یا `<signerNameDomain>/*`

کنترل‌کنندهٔ امضا آزاد است اطلاعاتی فراتر از محتوای درخواست را هم در نظر بگیرد، اما می‌تواند به درستی اطلاعات درون درخواست اتکا کند. برای مثال، کنترل‌کنندهٔ امضا ممکن است Pod را بارگذاری کند و حاشیه‌نویسی‌های آن را بخواند، یا روی ServiceAccount یک SubjectAccessReview انجام دهد.

کنترل‌کنندهٔ امضا برای صدور گواهی در پاسخ به یک درخواست، این کارها را انجام می‌دهد:
* یک شرط `Issued` به `status.conditions` اضافه می‌کند.
* گواهی صادرشده را در `status.certificateChain` قرار می‌دهد.
* فیلدهای `NotBefore` و `NotAfter` گواهی را در فیلدهای `status.notBefore` و `status.notAfter` قرار می‌دهد &mdash; این فیلدها برای کمک به اشکال‌زدایی به‌صورت غیرنرمال‌شده در API کوبرنتیز تکرار می‌شوند.
* با استفاده از `status.beginRefreshAt`، زمانی را برای شروع تلاش برای تازه‌سازی گواهی پیشنهاد می‌دهد.

کنترل‌کنندهٔ امضا برای رد یک درخواست، شرط «Denied» را به `status.conditions[]` اضافه می‌کند.

کنترل‌کنندهٔ امضا برای ناموفق علامت‌گذاری یک درخواست، شرط «Failed» را به `status.conditions[]` اضافه می‌کند.

همهٔ این شرط‌ها مانعهٔ‌الجمع هستند و باید وضعیت «True» داشته باشند. هیچ نوع شرط دیگری روی PodCertificateRequestها مجاز نیست. افزون بر این، پس از تنظیم هر یک از این شرط‌ها، فیلد `status` تغییرناپذیر می‌شود.

مانند همهٔ شرط‌ها، فیلد `status.conditions[].reason` باید کدی ماشین‌خوان با قالب TitleCase داشته باشد که شرط را توصیف می‌کند. فیلد `status.conditions[].message` برای توضیحی آزاد و قابل‌فهم برای انسان در نظر گرفته شده است.

برای اینکه PodCertificateRequestهای پایان‌یافته در کلاستر انباشته نشوند، یک کنترل‌کننده در `kube-controller-manager` همهٔ PodCertificateRequestهای قدیمی‌تر از ۱۵ دقیقه را حذف می‌کند. انتظار می‌رود همهٔ فرایندهای صدور گواهی در همین محدودیت ۱۵ دقیقه‌ای کامل شوند.

## بسته‌های اعتماد کلاستر {#cluster-trust-bundles}

{{< feature-state feature_gate_name="ClusterTrustBundle" >}}


هر ClusterTrustBundle آبجکتی در سطح کلاستر برای توزیع لنگرهای اعتماد X.509 (گواهی‌های ریشه) میان بارهای کاری درون کلاستر است. این آبجکت‌ها طوری طراحی شده‌اند که به‌خوبی با مفهوم [امضاکننده](#signers) در CertificateSigningRequestها کار کنند.

از ClusterTrustBundleها می‌توان در دو حالت استفاده کرد:
[پیوندخورده با امضاکننده](#ctb-signer-linked) و [بدون پیوند با امضاکننده](#ctb-signer-unlinked).

### ویژگی‌ها و اعتبارسنجی مشترک {#ctb-common}

محتوای فیلد `trustBundle` در همهٔ آبجکت‌های ClusterTrustBundle به‌طور سخت‌گیرانه اعتبارسنجی می‌شود. این فیلد باید یک یا چند گواهی X.509 با سریال‌سازی DER داشته باشد که هر کدام در یک بلوک PEM از نوع `CERTIFICATE` قرار گرفته‌اند. گواهی‌ها باید به‌عنوان گواهی‌های معتبر X.509 تجزیه شوند.

ویژگی‌های نامتداول PEM مانند داده‌های بین بلوک‌ها و سرآیندهای درون بلوک، یا هنگام اعتبارسنجی آبجکت رد می‌شوند یا مصرف‌کنندگان آبجکت می‌توانند آن‌ها را نادیده بگیرند. همچنین مصرف‌کنندگان مجازند گواهی‌های درون بسته را با ترتیبی دلخواه اما پایدار از آنِ خود مرتب کنند.

آبجکت‌های ClusterTrustBundle را باید درون کلاستر برای همه قابل‌خواندن دانست. اگر کلاستر شما از مجوزدهی [RBAC](/docs/reference/access-authn-authz/rbac/) استفاده می‌کند، همهٔ ServiceAccountها به‌طور پیش‌فرض مجوزی دارند که با آن می‌توانند همهٔ آبجکت‌های ClusterTrustBundle را **get**، **list** و **watch** کنند.
اگر از سازوکار مجوزدهی خودتان استفاده می‌کنید و ClusterTrustBundleها را در کلاستر فعال کرده‌اید، باید قاعده‌ای معادل تنظیم کنید تا این آبجکت‌ها درون کلاستر عمومی شوند و همان‌طور که انتظار می‌رود کار کنند.

اگر در کلاستر خود به‌طور پیش‌فرض مجوز فهرست کردن بسته‌های اعتماد کلاستر را ندارید، می‌توانید با جعل هویت (impersonate) یک حساب سرویس که به آن دسترسی دارید، ClusterTrustBundleهای موجود را ببینید:

```bash
kubectl get clustertrustbundles --as='system:serviceaccount:mynamespace:default'
```

### ClusterTrustBundleهای پیوندخورده با امضاکننده {#ctb-signer-linked}

ClusterTrustBundleهای پیوندخورده با امضاکننده، مانند نمونهٔ زیر، به یک _نام امضاکننده_ مرتبط هستند:

```yaml
apiVersion: certificates.k8s.io/v1
kind: ClusterTrustBundle
metadata:
  name: example.com:mysigner:foo
spec:
  signerName: example.com/mysigner
  trustBundle: "<... PEM data ...>"
```

این ClusterTrustBundleها قرار است به‌دست یک کنترل‌کنندهٔ مختص امضاکننده در کلاستر نگهداری شوند، به همین دلیل چند ویژگی امنیتی دارند:

* برای ایجاد یا به‌روزرسانی یک ClusterTrustBundle پیوندخورده با امضاکننده، باید مجوز **attest** روی امضاکننده را داشته باشید (فعل مجوزدهی سفارشی `attest`، گروه API `certificates.k8s.io` و مسیر منبع `signers`). می‌توانید مجوزدهی را برای نام منبع مشخص `<signerNameDomain>/<signerNamePath>` پیکربندی کنید یا الگویی مانند `<signerNameDomain>/*` را تطبیق دهید.
* نام ClusterTrustBundleهای پیوندخورده با امضاکننده **باید** پیشوندی برگرفته از فیلد `spec.signerName` آن‌ها داشته باشد. در این پیشوند، اسلش‌ها (`/`) با دونقطه (`:`) جایگزین می‌شوند و یک دونقطهٔ پایانی نیز اضافه می‌شود. پس از آن یک نام دلخواه می‌آید. برای مثال، امضاکنندهٔ `example.com/mysigner` را می‌توان به ClusterTrustBundle با نام `example.com:mysigner:<arbitrary-name>` پیوند داد.

بارهای کاری معمولاً ClusterTrustBundleهای پیوندخورده با امضاکننده را با ترکیبی از یک [انتخابگر (selector) فیلد](/docs/concepts/overview/working-with-objects/field-selectors/) روی نام امضاکننده و یک [انتخابگر برچسب](/docs/concepts/overview/working-with-objects/labels/#label-selectors) جداگانه مصرف می‌کنند.

### ClusterTrustBundleهای بدون پیوند با امضاکننده {#ctb-signer-unlinked}

فیلد `spec.signerName` در ClusterTrustBundleهای بدون پیوند با امضاکننده، مانند نمونهٔ زیر، خالی است:

```yaml
apiVersion: certificates.k8s.io/v1
kind: ClusterTrustBundle
metadata:
  name: foo
spec:
  # no signerName specified, so the field is blank
  trustBundle: "<... PEM data ...>"
```

این آبجکت‌ها عمدتاً برای کاربردهای پیکربندی کلاستر در نظر گرفته شده‌اند.
برخلاف رفتار گروه‌بندی معمول در ClusterTrustBundleهای پیوندخورده با امضاکننده، هر ClusterTrustBundle بدون پیوند با امضاکننده آبجکتی مستقل است.

ClusterTrustBundleهای بدون پیوند با امضاکننده نیازی به فعل `attest` ندارند. در عوض، دسترسی به آن‌ها را مستقیماً با سازوکارهای معمول، مانند کنترل دسترسی مبتنی بر نقش، کنترل می‌کنید.

برای تمایز از ClusterTrustBundleهای پیوندخورده با امضاکننده، نام ClusterTrustBundleهای بدون پیوند با امضاکننده **نباید** دونقطه (`:`) داشته باشد.

### دسترسی به ClusterTrustBundleها از درون پادها {#ctb-projection}

{{< feature-state feature_gate_name="ClusterTrustBundleProjection" >}}

محتوای ClusterTrustBundleها را می‌توان، مانند ConfigMapها و Secretها، به سیستم فایل کانتینر تزریق کرد.
برای جزئیات بیشتر، [منبع حجم تصویرشدهٔ clusterTrustBundle](/docs/concepts/storage/projected-volumes#clustertrustbundle) را ببینید.

## {{% heading "whatsnext" %}}

* [مدیریت گواهی‌های TLS در یک کلاستر](/docs/tasks/tls/managing-tls-in-a-cluster/) را بخوانید.
* [صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/) را بخوانید.
* کد منبع [امضاکنندهٔ](https://github.com/kubernetes/kubernetes/blob/32ec6c212ec9415f604ffc1f4c1f29b782968ff1/pkg/controller/certificates/signer/cfssl_signer.go) داخلی kube-controller-manager را ببینید.
* کد منبع [تأییدکنندهٔ](https://github.com/kubernetes/kubernetes/blob/32ec6c212ec9415f604ffc1f4c1f29b782968ff1/pkg/controller/certificates/approver/sarapprove.go) داخلی kube-controller-manager را ببینید.
* برای جزئیات خود X.509، به بخش ۳.۱ از [RFC 5280](https://tools.ietf.org/html/rfc5280#section-3.1) مراجعه کنید.
* برای آگاهی از نحو درخواست‌های امضای گواهی PKCS#10، به [RFC 2986](https://tools.ietf.org/html/rfc2986) مراجعه کنید.
* دربارهٔ API مربوط به ClusterTrustBundle بخوانید:
  * {{< page-api-reference kind="ClusterTrustBundle" >}}
