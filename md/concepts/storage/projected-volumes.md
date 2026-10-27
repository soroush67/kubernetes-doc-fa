---
reviewers:
- marosset
- jsturtevant
- zshihang
title: حجم‌های Projected
content_type: concept
weight: 21 # just after persistent volumes
---

<!-- overview -->

این سند _حجم‌های projected_ را در کوبرنتیز شرح می‌دهد. آشنایی با [حجم‌ها](/docs/concepts/storage/volumes/) توصیه می‌شود.

<!-- body -->

## مقدمه

یک حجم `projected` چندین منبع حجم موجود را به یک دایرکتوری واحد نگاشت می‌کند.

در حال حاضر، انواع منبع حجم زیر را می‌توان project کرد:

* [`secret`](/docs/concepts/storage/volumes/#secret)
* [`downwardAPI`](/docs/concepts/storage/volumes/#downwardapi)
* [`configMap`](/docs/concepts/storage/volumes/#configmap)
* [`serviceAccountToken`](#serviceaccounttoken)
* [`clusterTrustBundle`](#clustertrustbundle)
* [`podCertificate`](#podcertificate)

همهٔ منابع باید در همان فضای نام (namespace) Pod باشند. برای جزئیات بیشتر،
سند طراحی [all-in-one volume](https://git.k8s.io/design-proposals-archive/node/all-in-one-volume.md) را ببینید.

### نمونهٔ پیکربندی با یک secret، یک downwardAPI و یک configMap {#example-configuration-secret-downwardapi-configmap}

{{% code_sample file="pods/storage/projected-secret-downwardapi-configmap.yaml" %}}

### نمونهٔ پیکربندی: secretها با تنظیم حالت مجوز غیرپیش‌فرض {#example-configuration-secrets-nondefault-permission-mode}

{{% code_sample file="pods/storage/projected-secrets-nondefault-permission-mode.yaml" %}}

هر منبع حجم projected در spec زیر `sources` فهرست می‌شود.
پارامترها تقریباً یکسان هستند، با دو استثنا:

* برای secretها، فیلد `secretName` به `name` تغییر کرده است تا با
  نام‌گذاری ConfigMap سازگار باشد.
* `defaultMode` را تنها می‌توان در سطح projected مشخص کرد و نه برای هر
  منبع حجم. با این حال، همان‌طور که در بالا نشان داده شد، می‌توانید `mode`
  را برای هر projection به‌صورت جداگانه و صریح تنظیم کنید.

## حجم‌های projected از نوع serviceAccountToken {#serviceaccounttoken}
می‌توانید توکن [service account](/docs/reference/access-authn-authz/authentication/#service-account-tokens) فعلی
را در مسیر مشخصی درون یک Pod تزریق کنید. برای مثال:

{{% code_sample file="pods/storage/projected-service-account-token.yaml" %}}

Pod نمونه یک حجم projected دارد که شامل توکن service account تزریق‌شده است.
کانتینرهای این Pod می‌توانند از آن توکن برای دسترسی به API server کوبرنتیز
استفاده کنند و با هویت [ServiceAccount مربوط به pod](/docs/tasks/configure-pod-container/configure-service-account/) احراز هویت شوند.
فیلد `audience` شامل مخاطب مورد نظر
توکن است. دریافت‌کنندهٔ توکن باید خود را با شناسه‌ای که در audience توکن
مشخص شده است معرفی کند و در غیر این صورت باید توکن را رد کند. این فیلد
اختیاری است و مقدار پیش‌فرض آن شناسهٔ API server است.

`expirationSeconds` مدت اعتبار مورد انتظار توکن service account است.
مقدار پیش‌فرض آن ۱ ساعت است و باید دست‌کم ۱۰ دقیقه (۶۰۰ ثانیه) باشد. مدیر
همچنین می‌تواند با مشخص کردن گزینهٔ `--service-account-max-token-expiration`
برای API server، بیشینهٔ مقدار آن را محدود کند. فیلد `path` یک مسیر نسبی به نقطهٔ mount
حجم projected را مشخص می‌کند.

{{< note >}}
کانتینری که از یک منبع حجم projected به‌عنوان mount حجم [`subPath`](/docs/concepts/storage/volumes/#using-subpath)
استفاده می‌کند، به‌روزرسانی‌های آن منابع حجم را دریافت نخواهد کرد.
{{< /note >}}

## حجم‌های projected از نوع clusterTrustBundle {#clustertrustbundle}

{{< feature-state feature_gate_name="ClusterTrustBundleProjection" >}}


منبع حجم projected از نوع `clusterTrustBundle` محتوای یک یا چند آبجکت
[ClusterTrustBundle](/docs/reference/access-authn-authz/certificate-signing-requests#cluster-trust-bundles)
را به‌صورت یک فایل خودبه‌روزشونده در سیستم فایل کانتینر تزریق می‌کند.

ClusterTrustBundleها را می‌توان یا بر اساس [نام](/docs/reference/access-authn-authz/certificate-signing-requests#ctb-signer-unlinked)
یا بر اساس [نام امضاکننده](/docs/reference/access-authn-authz/certificate-signing-requests#ctb-signer-linked) انتخاب کرد.

برای انتخاب بر اساس نام، از فیلد `name` برای تعیین یک آبجکت ClusterTrustBundle منفرد استفاده کنید.

برای انتخاب بر اساس نام امضاکننده، از فیلد `signerName` (و به‌صورت اختیاری فیلد
`labelSelector`) برای تعیین مجموعه‌ای از آبجکت‌های ClusterTrustBundle که از
نام امضاکنندهٔ داده‌شده استفاده می‌کنند بهره بگیرید. اگر `labelSelector` وجود نداشته باشد، همهٔ
ClusterTrustBundleهای آن امضاکننده انتخاب می‌شوند.

kubelet گواهی‌های موجود در آبجکت‌های ClusterTrustBundle انتخاب‌شده را تکرارزدایی می‌کند،
نمایش‌های PEM را نرمال‌سازی می‌کند (توضیحات و سرآیندها را کنار می‌گذارد)، گواهی‌ها را از نو مرتب می‌کند
و آن‌ها را در فایلی که با `path` نام‌گذاری شده است می‌نویسد.
با تغییر مجموعهٔ ClusterTrustBundleهای انتخاب‌شده یا محتوای آن‌ها، kubelet فایل را به‌روز نگه می‌دارد.

به‌طور پیش‌فرض، اگر ClusterTrustBundle نام‌برده پیدا نشود،
یا اگر `signerName` / `labelSelector` با هیچ ClusterTrustBundleی مطابقت نداشته باشند، kubelet از راه‌اندازی pod جلوگیری می‌کند.
اگر این رفتار آن چیزی نیست که می‌خواهید، فیلد `optional` را روی `true` تنظیم کنید
تا pod با یک فایل خالی در `path` راه‌اندازی شود.

{{% code_sample file="pods/storage/projected-clustertrustbundle.yaml" %}}

## حجم‌های projected از نوع podCertificate {#podcertificate}

{{< feature-state feature_gate_name="PodCertificateRequest" >}}


منبع حجم projected از نوع `podCertificate` به‌صورت ایمن یک کلید خصوصی
و زنجیرهٔ گواهی X.509 برای استفادهٔ pod به‌عنوان اعتبارنامهٔ کلاینت یا سرور تأمین می‌کند.
سپس Kubelet هنگامی که کلید خصوصی و زنجیرهٔ گواهی به انقضا نزدیک می‌شوند،
تجدید آن‌ها را بر عهده می‌گیرد. برنامه تنها باید اطمینان حاصل کند که
هنگام تغییر فایل، آن را بی‌درنگ با سازوکاری مانند `inotify` یا
پرس‌وجوی دوره‌ای (polling) دوباره بارگذاری می‌کند.

هر projection از نوع `podCertificate` از فیلدهای پیکربندی زیر پشتیبانی می‌کند:
* `signerName`:
  [امضاکننده‌ای](/docs/reference/access-authn-authz/certificate-signing-requests#signers)
  که می‌خواهید گواهی را صادر کند. توجه داشته باشید که امضاکننده‌ها ممکن است
  الزامات دسترسی خاص خود را داشته باشند و ممکن است از صدور گواهی برای pod شما خودداری کنند.
* `keyType`: نوع کلید خصوصی که باید تولید شود. مقادیر معتبر عبارت‌اند از
  `ED25519`، `ECDSAP256`، `ECDSAP384`، `ECDSAP521`، `RSA3072` و `RSA4096`.
* `maxExpirationSeconds`: بیشینهٔ طول عمری که برای گواهی صادرشده برای pod
  می‌پذیرید. اگر تنظیم نشود، مقدار پیش‌فرض آن `86400` (۲۴
  ساعت) خواهد بود. باید دست‌کم `3600` (۱ ساعت) و حداکثر `7862400` (۹۱ روز) باشد.
  امضاکننده‌های داخلی کوبرنتیز به بیشینهٔ طول عمر `86400` (۱
  روز) محدود هستند. امضاکننده مجاز است گواهی‌ای با طول عمری کوتاه‌تر
  از آنچه مشخص کرده‌اید صادر کند.
* `credentialBundlePath`: مسیر نسبی درون projection که بستهٔ
  اعتبارنامه باید در آن نوشته شود. بستهٔ اعتبارنامه یک فایل با قالب PEM
  است که نخستین بلوک آن یک بلوک "PRIVATE KEY" شامل یک
  کلید خصوصی سریال‌شده با PKCS#8 است و بلوک‌های باقی‌مانده بلوک‌های "CERTIFICATE"
  هستند که زنجیرهٔ گواهی (گواهی برگ و هر گواهی
  میانی) را تشکیل می‌دهند.
* `keyPath` و `certificateChainPath`: مسیرهای جداگانه‌ای که Kubelet باید
  *فقط* کلید خصوصی یا زنجیرهٔ گواهی را در آن‌ها بنویسد.
* `userAnnotations`: یک نگاشت که به شما امکان می‌دهد اطلاعات بیشتری را به
  پیاده‌سازی امضاکننده منتقل کنید. این نگاشت عیناً در فیلد
  `spec.unverifiedUserAnnotations` آبجکت‌های
  [PodCertificateRequest](/docs/reference/access-authn-authz/certificate-signing-requests#pod-certificate-requests)
  که Kubelet ایجاد می‌کند کپی می‌شود. مدخل‌ها مشمول همان اعتبارسنجی حاشیه‌نویسی‌های
  فرادادهٔ آبجکت هستند، با این تفاوت که همهٔ کلیدها باید پیشوند دامنه داشته باشند.
  هیچ محدودیتی روی مقادیر اعمال نمی‌شود، به‌جز یک محدودیت اندازهٔ کلی روی
  کل فیلد. جدا از این اعتبارسنجی‌های پایه، API server هیچ
  اعتبارسنجی اضافه‌ای انجام نمی‌دهد. پیاده‌سازی‌های امضاکننده باید هنگام مصرف این داده‌ها
  بسیار محتاط باشند. امضاکننده‌ها نباید بدون انجام گام‌های راستی‌آزمایی مناسب
  به‌طور ذاتی به این داده‌ها اعتماد کنند. امضاکننده‌ها باید کلیدها و مقادیری را که پشتیبانی می‌کنند
  مستند کنند. امضاکننده‌ها باید درخواست‌هایی را که شامل کلیدهای ناشناخته هستند رد کنند.

{{< note >}}

بیشتر برنامه‌ها باید استفاده از `credentialBundlePath` را ترجیح دهند، مگر اینکه به دلایل سازگاری
به کلید و گواهی‌ها در فایل‌های جداگانه نیاز داشته باشند. Kubelet
از یک راهبرد نوشتن اتمی مبتنی بر پیوندهای نمادین (symlink) استفاده می‌کند تا اطمینان حاصل کند هنگامی که
فایل‌هایی را که project می‌کند باز می‌کنید، یا محتوای قدیمی را می‌خوانید یا محتوای جدید را.
با این حال، اگر کلید و زنجیرهٔ گواهی را از فایل‌های جداگانه بخوانید، Kubelet
ممکن است اعتبارنامه‌ها را پس از نخستین خواندن و پیش از دومین خواندن شما چرخش دهد
و در نتیجه برنامهٔ شما یک کلید و گواهی ناهمخوان بارگذاری کند.

{{< /note >}}

{{% code_sample file="pods/storage/projected-podcertificate.yaml" %}}

## تعامل‌های SecurityContext

[پیشنهاد](https://git.k8s.io/enhancements/keps/sig-storage/2451-service-account-token-volumes#proposal)
مربوط به مدیریت مجوزهای فایل در بهبود حجم projected برای service account،
تنظیم درست مجوزهای مالکیت فایل‌های projected را معرفی کرد.

### Linux

در podهای Linux که یک حجم projected دارند و `RunAsUser` در
[`SecurityContext`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context) مربوط به Pod تنظیم شده است،
فایل‌های projected مالکیت درستی دارند که شامل مالکیت کاربر
کانتینر نیز می‌شود.

هنگامی که همهٔ کانتینرهای یک pod مقدار `runAsUser` یکسانی در
[`PodSecurityContext`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context)
یا
[`SecurityContext`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1) کانتینر خود داشته باشند،
kubelet اطمینان حاصل می‌کند که محتوای حجم `serviceAccountToken` متعلق به آن کاربر باشد
و حالت مجوز فایل توکن روی `0600` تنظیم شود.

{{< note >}}
{{< glossary_tooltip text="کانتینرهای موقت (Ephemeral containers)" term_id="ephemeral-container" >}}
که پس از ایجاد یک Pod به آن افزوده می‌شوند، مجوزهای حجمی را که هنگام ایجاد pod
تنظیم شده‌اند تغییر *نمی‌دهند*.

اگر مجوزهای حجم `serviceAccountToken` یک Pod به این دلیل روی `0600` تنظیم شده باشند که
همهٔ کانتینرهای دیگر Pod مقدار `runAsUser` یکسانی دارند، کانتینرهای موقت
باید از همان `runAsUser` استفاده کنند تا بتوانند توکن را بخوانند.
{{< /note >}}

### Windows

در podهای Windows که یک حجم projected دارند و `RunAsUsername` در
`SecurityContext` مربوط به Pod تنظیم شده است، به دلیل نحوهٔ مدیریت حساب‌های کاربری
در Windows، مالکیت اعمال نمی‌شود. Windows حساب‌های کاربر و گروه محلی را
در یک فایل پایگاه داده به نام Security Account Manager (SAM) ذخیره و مدیریت می‌کند. هر
کانتینر نمونهٔ خاص خود از پایگاه دادهٔ SAM را نگهداری می‌کند که میزبان
در زمان اجرای کانتینر هیچ دیدی به آن ندارد. کانتینرهای Windows
طوری طراحی شده‌اند که بخش حالت کاربر (user mode) سیستم‌عامل را جدا از میزبان اجرا کنند؛
از این رو یک پایگاه دادهٔ SAM مجازی نگهداری می‌شود. در نتیجه، kubelet که
روی میزبان اجرا می‌شود توانایی پیکربندی پویای مالکیت فایل‌های میزبان
برای حساب‌های مجازی‌شدهٔ کانتینر را ندارد. توصیه می‌شود اگر قرار است فایل‌های روی
ماشین میزبان با کانتینر به اشتراک گذاشته شوند، آن‌ها در mount حجم جداگانهٔ خود
خارج از `C:\` قرار داده شوند.

به‌طور پیش‌فرض، فایل‌های projected مالکیتی مانند آنچه برای
یک فایل حجم projected نمونه در زیر نشان داده شده است خواهند داشت:

```powershell
PS C:\> Get-Acl C:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crt | Format-List

Path   : Microsoft.PowerShell.Core\FileSystem::C:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crt
Owner  : BUILTIN\Administrators
Group  : NT AUTHORITY\SYSTEM
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Users Allow  ReadAndExecute, Synchronize
Audit  :
Sddl   : O:BAG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;0x1200a9;;;BU)
```

این بدان معناست که همهٔ کاربران مدیر مانند `ContainerAdministrator`
دسترسی خواندن، نوشتن و اجرا خواهند داشت، در حالی که کاربران غیرمدیر دسترسی خواندن و
اجرا خواهند داشت.

{{< note >}}
به‌طور کلی، اعطای دسترسی کانتینر به میزبان توصیه نمی‌شود، زیرا می‌تواند
راه را برای سوءاستفاده‌های امنیتی احتمالی باز کند.

ایجاد یک Pod در Windows با `RunAsUser` در `SecurityContext` آن باعث می‌شود
Pod برای همیشه در وضعیت `ContainerCreating` گیر کند. بنابراین توصیه می‌شود
از گزینهٔ `RunAsUser` که مخصوص Linux است با Podهای Windows استفاده نکنید.
{{< /note >}}
