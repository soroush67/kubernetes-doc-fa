---
reviewers:
- erictune
- lavalamp
- deads2k
- liggitt
title: احراز هویت
content_type: concept
weight: 10
---

<!-- overview -->
این صفحه مروری بر احراز هویت (authentication) در کوبرنتیز ارائه می‌کند و تمرکز آن بر احراز هویت در [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) است.

<!-- body -->
## کاربران در کوبرنتیز {#users-in-kubernetes}

همهٔ کلاسترهای کوبرنتیز دو دسته کاربر دارند: حساب‌های سرویس (service account) که توسط کوبرنتیز مدیریت می‌شوند، و کاربران عادی.

فرض بر این است که یک سرویس مستقل از کلاستر، کاربران عادی را به یکی از روش‌های زیر مدیریت می‌کند:

- مدیری که کلیدهای خصوصی را توزیع می‌کند
- یک مخزن کاربران مانند Keystone یا Google Accounts
- یک فایل حاوی فهرستی از نام‌های کاربری و گذرواژه‌ها

از این منظر، _کوبرنتیز آبجکتی که نمایانگر حساب‌های کاربران عادی باشد ندارد._
کاربران عادی را نمی‌توان از طریق یک فراخوانی API به کلاستر افزود.

با وجود اینکه کاربر عادی را نمی‌توان از طریق فراخوانی API افزود، هر کاربری که گواهی معتبری ارائه کند که توسط مرجع صدور گواهی (CA) کلاستر امضا شده باشد، احراز هویت‌شده در نظر گرفته می‌شود. در این پیکربندی، کوبرنتیز نام کاربری را از فیلد common name در بخش 'subject' گواهی (برای مثال "/CN=bob") تعیین می‌کند. از آنجا به بعد، زیرسامانهٔ کنترل دسترسی مبتنی بر نقش (RBAC) مشخص می‌کند که آیا کاربر مجاز است عملیات خاصی را روی یک منبع انجام دهد یا خیر.

در مقابل، حساب‌های سرویس کاربرانی هستند که توسط API کوبرنتیز مدیریت می‌شوند. این حساب‌ها به فضاهای نام (namespace) مشخصی وابسته‌اند و به‌صورت خودکار توسط API server یا به‌صورت دستی از طریق فراخوانی‌های API ایجاد می‌شوند. حساب‌های سرویس به مجموعه‌ای از اعتبارنامه‌ها (credentials) مرتبط‌اند که به‌صورت `Secrets` ذخیره می‌شوند و در پادها mount می‌شوند تا فرایندهای درون کلاستر بتوانند با API کوبرنتیز ارتباط برقرار کنند.

درخواست‌های API یا به یک کاربر عادی یا یک حساب سرویس مرتبط می‌شوند، یا به‌عنوان [درخواست‌های ناشناس](#anonymous-requests) در نظر گرفته می‌شوند. این بدان معناست که هر فرایندی در داخل یا خارج از کلاستر، از کاربر انسانی که `kubectl` را روی ایستگاه کاری خود تایپ می‌کند گرفته تا `kubelets` روی نودها و اجزای control plane، هنگام ارسال درخواست به API server باید احراز هویت شود، وگرنه به‌عنوان کاربر ناشناس در نظر گرفته می‌شود.

اگر تلاش کنید احراز هویت شوید و موفق باشد، API server به‌صورت خودکار شما را عضو گروه ویژهٔ `system:authenticated` قرار می‌دهد.

## راهبردهای احراز هویت {#authentication-strategies}

کوبرنتیز از گواهی‌های کلاینت، توکن‌های bearer یا یک پروکسی احراز هویت‌کننده برای احراز هویت درخواست‌های API از طریق افزونه‌های احراز هویت استفاده می‌کند. هنگامی که درخواست‌های HTTP به API server ارسال می‌شوند، افزونه‌ها تلاش می‌کنند ویژگی‌های زیر را با درخواست مرتبط کنند:

* نام کاربری (Username): رشته‌ای که کاربر نهایی را شناسایی می‌کند. مقادیر رایج می‌توانند `kube-admin` یا `jane@example.com` باشند.
* UID: رشته‌ای که کاربر نهایی را شناسایی می‌کند و تلاش می‌کند از نام کاربری ثابت‌تر و یکتاتر باشد.
* گروه‌ها (Groups): مجموعه‌ای از رشته‌ها که هر یک نشان‌دهندهٔ عضویت کاربر در یک مجموعهٔ منطقی نام‌دار از کاربران است. مقادیر رایج می‌توانند `system:masters` یا `devops-team` باشند.
* فیلدهای اضافی (Extra fields): نگاشتی از رشته‌ها به فهرستی از رشته‌ها که اطلاعات تکمیلی‌ای را نگه می‌دارد که ممکن است برای مجوزدهنده‌ها (authorizers) مفید باشد.

{{< note >}}
همهٔ مقادیر برای سامانهٔ احراز هویت مبهم (opaque) هستند و تنها زمانی اهمیت پیدا می‌کنند که توسط یک [مجوزدهنده (authorizer)](/docs/reference/access-authn-authz/authorization/) تفسیر شوند.
{{< /note >}}

## درخواست‌های ناشناس {#anonymous-requests}

در صورت فعال بودن، درخواست‌هایی که توسط سایر روش‌های احراز هویت پیکربندی‌شده رد نشوند، به‌عنوان درخواست‌های ناشناس در نظر گرفته می‌شوند و نام کاربری `system:anonymous` و گروه `system:unauthenticated` به آن‌ها داده می‌شود.

برای مثال، در سروری که احراز هویت با توکن پیکربندی شده و دسترسی ناشناس فعال است، درخواستی که یک bearer token نامعتبر ارائه کند، خطای `401 Unauthorized` دریافت می‌کند. درخواستی که هیچ bearer token ارائه نکند، به‌عنوان درخواست ناشناس در نظر گرفته می‌شود.

دسترسی ناشناس به‌طور پیش‌فرض فعال است اگر از [حالت مجوزدهی](/docs/reference/access-authn-authz/authorization/#authorization-modules) غیر از `AlwaysAllow` استفاده شود؛ می‌توانید با ارسال گزینهٔ خط فرمان `--anonymous-auth=false` به API server آن را غیرفعال کنید.
مجوزدهنده‌های داخلی ABAC و RBAC نیازمند مجوزدهی صریح برای کاربر `system:anonymous` یا گروه `system:unauthenticated` هستند؛ اگر قواعد سیاستی قدیمی (از کوبرنتیز نسخهٔ 1.5 یا پیش از آن) دارید، آن قواعد قدیمی که به کاربر `*` یا گروه `*` دسترسی می‌دهند، به‌طور خودکار دسترسی کاربران ناشناس را مجاز نمی‌کنند.

### پیکربندی احراز هویت‌کنندهٔ ناشناس {#anonymous-authenticator-configuration}

{{< feature-state feature_gate_name="AnonymousAuthConfigurableEndpoints" >}}

می‌توان از `AuthenticationConfiguration` برای پیکربندی احراز هویت‌کنندهٔ ناشناس استفاده کرد. اگر فیلد anonymous را در فایل `AuthenticationConfiguration` تنظیم کنید، نمی‌توانید گزینهٔ خط فرمان `--anonymous-auth` را تنظیم کنید.

مزیت اصلی پیکربندی احراز هویت‌کنندهٔ ناشناس با استفاده از فایل پیکربندی احراز هویت این است که علاوه بر فعال و غیرفعال کردن احراز هویت ناشناس، می‌توانید مشخص کنید کدام endpointها از احراز هویت ناشناس پشتیبانی کنند.

نمونه‌ای از فایل پیکربندی احراز هویت در ادامه آمده است:

{{< highlight yaml "linenos=false,hl_lines=2-5" >}}
---
#
# CAUTION: this is an example configuration.
#          Do not use this as-is for your own cluster!
#
apiVersion: apiserver.config.k8s.io/v1
kind: AuthenticationConfiguration
anonymous:
  enabled: true
  conditions:
  - path: /livez
  - path: /readyz
  - path: /healthz
{{< /highlight >}}

در پیکربندی بالا، تنها endpointهای `/livez`، `/readyz` و `/healthz` برای درخواست‌های ناشناس قابل دسترسی هستند. هر endpoint دیگری به‌صورت ناشناس قابل دسترسی نخواهد بود، حتی اگر پیکربندی مجوزدهی شما آن را مجاز بداند.

## روش‌های احراز هویت {#authentication-methods}

می‌توانید چندین روش احراز هویت را هم‌زمان فعال کنید. معمولاً باید دست‌کم از دو روش استفاده کنید:

- [توکن‌های حساب سرویس](/docs/concepts/security/service-accounts/#authenticating-credentials) برای ServiceAccountها
- دست‌کم یک روش دیگر برای احراز هویت کاربران (عادی)

روش‌های احراز هویت موجود عبارت‌اند از:

* [گواهی‌های کلاینت X.509](#x509-client-certificates)
* [توکن‌های Bootstrap](#bootstrap-tokens)
* [توکن‌های حساب سرویس](#service-account-tokens)
* [فایل توکن ایستا](#static-token-file)
* [یکپارچه‌سازی‌های خارجی](#external-integrations)
  * [JSON Web Tokens](#json-web-token-authentication)
  * [توکن‌های OpenID Connect](#openid-connect-tokens)
  * [احراز هویت توکن با Webhook](#webhook-token-authentication)
  * [پروکسی معکوس احراز هویت‌کننده](#authenticating-proxy)

هنگامی که چندین ماژول احراز هویت‌کننده فعال باشند، نخستین ماژولی که درخواست را با موفقیت احراز هویت کند، ارزیابی را کوتاه می‌کند (short-circuit) و ماژول‌های بعدی بررسی نمی‌شوند.
API server ترتیب اجرای احراز هویت‌کننده‌ها را تضمین نمی‌کند.

### گواهی‌های کلاینت X.509 {#x509-client-certificates}

هر کلاینت کوبرنتیز که گواهی کلاینت معتبری ارائه کند که توسط مرجع صدور گواهی (CA) _اعتماد کلاینت_ (client trust) کلاستر امضا شده باشد، احراز هویت‌شده در نظر گرفته می‌شود. در این پیکربندی، کوبرنتیز نام کاربری را از فیلد `commonName` در _subject_ گواهی تعیین می‌کند (برای مثال، `commonName=bob` نمایانگر کاربری با نام کاربری "bob" است).
از آنجا به بعد، سازوکارهای [مجوزدهی](/docs/reference/access-authn-authz/authorization) کوبرنتیز مشخص می‌کنند که آیا کاربر مجاز است عملیات خاصی را روی یک منبع انجام دهد یا خیر.

احراز هویت با گواهی کلاینت با ارسال گزینهٔ `--client-ca-file=<SOMEFILE>` به API server فعال می‌شود.
این گزینه مرجع صدور گواهی _اعتماد کلاینت_ کلاستر را پیکربندی می‌کند.
فایل مورد اشاره باید شامل یک یا چند مرجع صدور گواهی باشد که API server هنگام نیاز به اعتبارسنجی گواهی‌های کلاینت می‌تواند از آن‌ها استفاده کند.
اگر گواهی کلاینت ارائه و تأیید شود، common name موجود در subject به‌عنوان نام کاربری درخواست استفاده می‌شود. گواهی‌های کلاینت همچنین می‌توانند عضویت‌های گروهی کاربر را با استفاده از فیلدهای organization گواهی مشخص کنند. برای درج چند عضویت گروهی برای یک کاربر، چند فیلد organization را در گواهی قرار دهید.

برای آگاهی از نحوهٔ تولید گواهی کلاینت، به [مدیریت گواهی‌ها](/docs/tasks/administer-cluster/certificates/) مراجعه کنید، یا [مثال](#x509-client-certificates-example) کوتاهی را که در ادامهٔ همین صفحه آمده است مطالعه کنید.

#### گواهی‌های کلاینت سازگار با کوبرنتیز {#x509-client-certificates-k8s}

می‌توانید گواهی معتبری را که توسط یک CA در زنجیرهٔ اعتمادی صادر شده که API server برای گواهی‌های کلاینت می‌پذیرد، ارائه کنید و از آن برای احراز هویت در کوبرنتیز استفاده کنید.
گواهی باید معتبر باشد؛ API server این موضوع را بر اساس ویژگی‌های `notBefore` و `notAfter` استاندارد X.509 بررسی می‌کند، و گواهی باید دارای _extended key usage_ باشد که شامل احراز هویت کلاینت (`ClientAuth`) است.

{{< note >}}
کوبرنتیز {{< skew currentVersion >}} از _ابطال_ (revocation) گواهی پشتیبانی نمی‌کند.
هر گواهی صادرشده تا زمان انقضا معتبر باقی می‌ماند.
{{< /note >}}

##### نگاشت نام کاربری {#x509-client-certificates-k8s-username}

کوبرنتیز انتظار دارد گواهی کلاینت دارای ویژگی `commonName` (با OID برابر `2.5.4.3`) باشد که به‌عنوان نام کاربری سوژه استفاده می‌شود.

##### نگاشت شناسهٔ کاربر (User ID) {#user-id-mapping}

{{< feature-state feature_gate_name="AllowParsingUserUIDFromCertAuth" >}}

برای استفاده از این قابلیت، گواهی باید ویژگی `1.3.6.1.4.1.57683.2` را داشته باشد، و [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `AllowParsingUserUIDFromCertAuth` باید فعال باشد (به‌طور پیش‌فرض فعال است).

کوبرنتیز می‌تواند یک UID **اختیاری** کاربر را از گواهی استخراج کند.
UID با نام کاربری متفاوت است؛ مقداری مبهم (opaque) است که معنای آن را فردی که گواهی را درخواست کرده است، یا در غیر این صورت کسی که قواعد تأیید گواهی را تنظیم کرده است، تعیین می‌کند.

برای مثال، UID ممکن است در یک کلاستر `1042` (یک عدد صحیح ساده) باشد، اما گواهی دیگری ممکن است `d3f77937-ec82-4f16-8010-61821abe315a` (یک UUID) را به‌عنوان UID به کار ببرد.

در اینجا مثالی برای توضیح این موضوع آمده است. اگر گواهی‌ای دارید که common name آن روی "Ada Lovelace" تنظیم شده و گواهی همچنین دارای ویژگی `uid` (با OID برابر `0.9.2342.19200300.100.1.1`) با مقدار "aaking1815" است، کوبرنتیز نام کاربری کلاینت را "Ada Lovelace" در نظر می‌گیرد؛ کوبرنتیز ویژگی `uid` را نادیده می‌گیرد، زیرا OID اختصاصی CNCF که کوبرنتیز به دنبال آن است نیست.
اگر می‌خواهید `aaking1815` به‌عنوان UID توسط کوبرنتیز شناسایی شود، باید به‌عنوان مقدار ویژگی OID با شمارهٔ `1.3.6.1.4.1.57683.2` در subject گواهی تنظیم شود.

##### نگاشت گروه {#x509-client-certificates-k8s-group}

می‌توانید با گنجاندن ایستای اطلاعات گروه در گواهی، یک کاربر را به گروه‌ها نگاشت کنید. برای هر گروهی که کاربر عضو آن است، نام گروه را به‌عنوان یک `organization` (با OID برابر `2.5.6.4`) در subject گواهی خود اضافه کنید.
برای درج چند عضویت گروهی برای یک کاربر، چند organization را در subject گواهی قرار دهید (ترتیب اهمیتی ندارد).
برای کاربر نمونه، distinguished name یک گواهی ممکن است CN=Ada&nbsp;Lovelace,O=Users,O=Staff,O=Programmers باشد که او را در گروه‌های "Programmers"، "Staff"، "system:authenticated" و "Users" قرار می‌دهد.

قرار دادن اطلاعات گروه در گواهی اختیاری است؛ اگر هیچ گروهی در گواهی مشخص نکنید، کاربر فقط عضو "system:authenticated" خواهد بود.

##### گواهی‌های کلاینت نود {#x509-client-certificates-nodes}

کوبرنتیز می‌تواند همین رویکرد را برای هویت نود به کار ببرد؛ نودها کلاینت‌های API server کوبرنتیز هستند که یک {{<glossary_tooltip term_id="kubelet" text="kubelet">}} را اجرا می‌کنند
(همچنین، هرچند در اینجا اهمیت کمتری دارد، API server معمولاً کلاینت هر نود نیز هست).
برای مثال: نودی با نام "server-1a-antarctica42" و نام دامنهٔ "server-1a-antarctica42.cluster.example" می‌تواند از گواهی‌ای استفاده کند که برای "CN=system:node:server-1a-antarctica/42,O=system:nodes" صادر شده است. در این صورت نام کاربری نود "system:node:server-1a-antarctica/g42" است و نود عضو "system:authenticated" و "system:nodes" خواهد بود.

kubelet از گواهی و کلید خصوصی نود برای احراز هویت در API server کلاستر استفاده می‌کند.

{{< note >}}
هویت‌های ماشینی نودها با
{{< glossary_tooltip text="ServiceAccountها" term_id="service-account" >}}
یکسان نیستند.
{{< /note >}}

#### مثال {#x509-client-certificates-example}

می‌توانید از ابزار خط فرمان `openssl` برای تولید یک درخواست امضای گواهی (certificate signing request) استفاده کنید:

```bash
# This example assumes that you already have a private key alovelace.pem
openssl req -new -key alovelace.pem -out alovelace-csr.pem -subj "/CN=alovelace/O=app1/O=app2"
```

این دستور یک درخواست امضا برای نام کاربری "alovelace" ایجاد می‌کند که به دو گروه "app1" و "app2" تعلق دارد. سپس می‌توانید این درخواست امضا را توسط مرجع صدور گواهی اعتماد کلاینت کلاستر خود امضا کنید تا گواهی‌ای به دست آورید که بتوانید برای احراز هویت کلاینت در کلاستر خود استفاده کنید.

### توکن‌های Bootstrap {#bootstrap-tokens}

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

برای تسهیل راه‌اندازی اولیهٔ کلاسترهای جدید، کوبرنتیز نوعی توکن Bearer با مدیریت پویا به نام *Bootstrap Token* دارد. این توکن‌ها به‌صورت Secret در فضای نام `kube-system` ذخیره می‌شوند و در آنجا می‌توان آن‌ها را به‌صورت پویا مدیریت و ایجاد کرد. Controller Manager شامل یک کنترل‌کنندهٔ TokenCleaner است که توکن‌های bootstrap را هنگام انقضا حذف می‌کند.

توکن‌ها به شکل `[a-z0-9]{6}.[a-z0-9]{16}` هستند. مؤلفهٔ اول شناسهٔ توکن (Token ID) و مؤلفهٔ دوم رمز توکن (Token Secret) است. توکن را به‌صورت زیر در یک هدر HTTP مشخص می‌کنید:

```http
Authorization: Bearer 781292.db7bc3a58fc5f07e
```

باید احراز هویت‌کنندهٔ Bootstrap Token را با پرچم `--enable-bootstrap-token-auth` روی API Server فعال کنید. همچنین باید کنترل‌کنندهٔ TokenCleaner را از طریق آرگومان خط فرمان `--controllers` برای kube-controller-manager فعال کنید.
این کار با چیزی شبیه `--controllers=*,tokencleaner` انجام می‌شود.
اگر از ابزار `kubeadm` برای راه‌اندازی اولیهٔ کلاستر استفاده می‌کنید، این ابزار این کار را برای شما انجام می‌دهد.

این احراز هویت‌کننده با هویت `system:bootstrap:<Token ID>` احراز هویت می‌کند. این هویت در گروه `system:bootstrappers` قرار می‌گیرد. نام‌گذاری و گروه‌ها عمداً محدود شده‌اند تا کاربران را از استفاده از این توکن‌ها پس از مرحلهٔ راه‌اندازی اولیه منصرف کنند. از نام‌های کاربری و گروه می‌توان (و `kubeadm` نیز استفاده می‌کند) برای تدوین سیاست‌های مجوزدهی مناسب جهت پشتیبانی از راه‌اندازی اولیهٔ یک کلاستر بهره برد.

لطفاً برای مستندات تفصیلی دربارهٔ احراز هویت‌کنندهٔ Bootstrap Token و کنترل‌کننده‌ها، و همچنین نحوهٔ مدیریت این توکن‌ها با `kubeadm`، به [Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/) مراجعه کنید.

#### قرار دادن bearer token در درخواست {#putting-a-bearer-token-in-a-request}

هنگام استفاده از احراز هویت با bearer token از یک کلاینت HTTP، API server انتظار دارد هدر `Authorization` با مقدار `Bearer
<token>` وجود داشته باشد. bearer token باید دنباله‌ای از کاراکترها باشد که بتوان آن را تنها با استفاده از امکانات کدگذاری و نقل‌قول (quoting) خود HTTP در مقدار یک هدر HTTP قرار داد. برای مثال: اگر bearer token برابر `31ada4fd-adec-460c-809a-9e56ceb75269` باشد، در هدر HTTP به‌صورت زیر ظاهر می‌شود.

```http
Authorization: Bearer 31ada4fd-adec-460c-809a-9e56ceb75269
```


### توکن‌های حساب سرویس {#service-account-tokens}

حساب سرویس (service account) یک احراز هویت‌کنندهٔ خودکار فعال است که از bearer tokenهای امضاشده برای تأیید درخواست‌ها استفاده می‌کند. این افزونه دو پرچم اختیاری می‌پذیرد:

* `--service-account-key-file` فایلی حاوی کلیدهای خصوصی یا عمومی x509 RSA یا ECDSA با کدگذاری PEM که برای تأیید توکن‌های ServiceAccount استفاده می‌شود. فایل مشخص‌شده می‌تواند شامل چندین کلید باشد و پرچم را می‌توان چندین بار با فایل‌های مختلف مشخص کرد. اگر مشخص نشود، از --tls-private-key-file استفاده می‌شود.
* `--service-account-lookup` اگر فعال باشد، توکن‌هایی که از API حذف می‌شوند باطل (revoke) خواهند شد.

[ServiceAccountها](/docs/concepts/security/service-accounts/) معمولاً به‌صورت خودکار توسط API server ایجاد می‌شوند و از طریق `ServiceAccount` [Admission Controller](/docs/reference/access-authn-authz/admission-controllers/) با پادهای در حال اجرا در کلاستر مرتبط می‌شوند.
Bearer tokenها در مکان‌های شناخته‌شده‌ای در پادها mount می‌شوند و به کلاینت‌های درون کلاستر اجازه می‌دهند در API server احراز هویت شوند. ServiceAccountها را می‌توان با استفاده از فیلد `serviceAccountName` در `spec` یک Pod به‌صورت صریح با Podها مرتبط کرد.

{{< note >}}
`serviceAccountName` معمولاً حذف می‌شود، زیرا این کار به‌صورت خودکار انجام می‌شود.
{{< /note >}}

در اینجا مانیفست (جزئی) یک Deployment آمده است که با ServiceAccount به نام bob-the-bot اجرا می‌شود:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
spec:
  replicas: 3
  template:
    metadata:
    # ...
    spec:
      serviceAccountName: bob-the-bot
      containers:
      - name: nginx
        image: nginx:1.14.2
```

bearer tokenهای حساب سرویس برای استفاده در خارج از کلاستر کاملاً معتبرند و می‌توان از آن‌ها برای ایجاد هویت برای کارهای (job) بلندمدتی استفاده کرد که می‌خواهند با API کوبرنتیز ارتباط برقرار کنند. برای ایجاد دستی یک حساب سرویس، از دستور `kubectl create
serviceaccount (NAME)` استفاده کنید. این دستور یک حساب سرویس در فضای نام جاری ایجاد می‌کند.

```bash
kubectl create serviceaccount jenkins
```

```none
serviceaccount/jenkins created
```

می‌توانید یک توکن مرتبط را به‌صورت دستی ایجاد کنید:

```bash
kubectl create token jenkins
```

```none
eyJhbGciOiJSUzI1NiIsImtp...
```

توکن ایجادشده یک [JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519) (JWT) امضاشده است.

JWT امضاشده را می‌توان به‌عنوان bearer token برای احراز هویت با حساب سرویس مورد نظر استفاده کرد. برای اطلاع از نحوهٔ گنجاندن توکن در یک درخواست، [بالا](#putting-a-bearer-token-in-a-request) را ببینید. معمولاً این توکن‌ها برای دسترسی درون کلاستر به API server در پادها mount می‌شوند، اما از خارج از کلاستر نیز قابل استفاده‌اند.

حساب‌های سرویس با نام کاربری `system:serviceaccount:(NAMESPACE):(SERVICEACCOUNT)` احراز هویت می‌شوند و به گروه‌های `system:serviceaccounts` و `system:serviceaccounts:(NAMESPACE)` اختصاص می‌یابند.

{{< warning >}}
از آنجا که توکن‌های حساب سرویس را می‌توان در آبجکت‌های API از نوع Secret نیز ذخیره کرد، هر کاربری که دسترسی نوشتن به Secretها دارد می‌تواند یک توکن درخواست کند، و هر کاربری که دسترسی خواندن به آن Secretها دارد می‌تواند به‌عنوان آن حساب سرویس احراز هویت شود. در اعطای مجوزها به حساب‌های سرویس و قابلیت‌های خواندن یا نوشتن برای Secretها احتیاط کنید.
{{< /warning >}}

## یکپارچه‌سازی‌های خارجی {#external-integrations}

کوبرنتیز به‌صورت بومی از JWT و OpenID Connect (OIDC) پشتیبانی می‌کند؛ بخش [احراز هویت با JSON Web Token](#json-web-token-authentication) را ببینید.

یکپارچه‌سازی با سایر پروتکل‌های احراز هویت (برای مثال: LDAP، SAML، Kerberos و طرح‌های جایگزین X.509)
را می‌توان با استفاده از یک [پراکسی احراز هویت](#authenticating-proxy) یا با یکپارچه‌سازی با یک
[وب‌هوک احراز هویت](#webhook-token-authentication) انجام داد.

همچنین می‌توانید از هر روش سفارشی دیگری که [گواهی‌های X.509 کلاینت](#x509-client-certificates) را برای کلاینت‌ها صادر می‌کند استفاده کنید،
مشروط بر اینکه API server به گواهی‌های معتبر اعتماد کند.
برای آگاهی از نحوه ایجاد یک گواهی، بخش [گواهی‌های X.509 کلاینت](#x509-client-certificates) را مطالعه کنید.

اگر برای کلاینت‌ها گواهی صادر می‌کنید، این بر عهده شماست (به‌عنوان مدیر پلتفرم ابری)
که اطمینان حاصل کنید دوره اعتبار گواهی و سایر تصمیم‌های طراحی‌ای که اتخاذ می‌کنید، سطح امنیتی
مناسبی را فراهم می‌کنند.

### احراز هویت با JSON Web Token

می‌توانید کوبرنتیز را به‌گونه‌ای پیکربندی کنید که کاربران را با استفاده از توکن‌های سازگار با [JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519) (JWT) احراز هویت کند. سازوکار احراز هویت JWT برای توکن‌های ServiceAccount که خود کوبرنتیز صادر می‌کند به کار می‌رود، و همچنین می‌توانید از آن برای یکپارچه‌سازی با سایر منابع هویت استفاده کنید.

احراز هویت‌کننده تلاش می‌کند یک ID token خام را تجزیه کند و بررسی کند که توسط صادرکننده (issuer) پیکربندی‌شده امضا شده باشد.
برای توکن‌هایی که به‌صورت خارجی صادر شده‌اند، کلید عمومی لازم برای تأیید امضا با استفاده از OIDC discovery از نقطه پایانی عمومی صادرکننده کشف می‌شود.

حداقل payload معتبر JWT **باید** شامل claimهای زیر باشد:

```javascript
{
  "iss": "https://example.com",   // must match the issuer.url
  "aud": ["my-app"],              // at least one of the entries in issuer.audiences must match the "aud" claim in presented JWTs.
  "exp": 1234567890,              // token expiration as Unix time (the number of seconds elapsed since January 1, 1970 UTC)
  "<username-claim>": "user"      // this is the username claim configured in the claimMappings.username.claim or claimMappings.username.expression
}
```

#### نوع egress selector برای JWT

{{< feature-state feature_gate_name="StructuredAuthenticationConfigurationEgressSelector" >}}

فیلد `egressSelectorType` در پیکربندی صادرکننده JWT به شما امکان می‌دهد مشخص کنید که کدام _egress selector_ برای ارسال تمام ترافیک مرتبط با صادرکننده (discovery، JWKS، claimهای توزیع‌شده و غیره) استفاده شود.
استفاده از این قابلیت مستلزم فعال بودن feature gate با نام `StructuredAuthenticationConfigurationEgressSelector` است.

#### توکن‌های OpenID Connect

[OpenID Connect](https://openid.net/connect/) گونه‌ای از OAuth2 است که برخی ارائه‌دهندگان OAuth2، از جمله Microsoft Entra ID، Salesforce و Google، از آن پشتیبانی می‌کنند.
افزونه اصلی این پروتکل نسبت به OAuth2، فیلد اضافه‌ای است که همراه با access token بازگردانده می‌شود و [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) نام دارد.
این توکن یک JSON Web Token (JWT) با فیلدهای شناخته‌شده، مانند ایمیل کاربر، است که توسط سرور امضا شده است.

برای شناسایی کاربر، احراز هویت‌کننده از `id_token` (و نه `access_token`) موجود در [پاسخ توکن](https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse) OAuth2 به‌عنوان bearer token استفاده می‌کند. برای اطلاع از نحوه قرار دادن توکن در درخواست، [بالا](#putting-a-bearer-token-in-a-request) را ببینید.

{{< mermaid >}}
sequenceDiagram
    participant user as User
    participant idp as Identity Provider
    participant kube as kubectl
    participant api as API Server

    user ->> idp: 1. Log in to IdP
    activate idp
    idp -->> user: 2. Provide access_token,<br>id_token, and refresh_token
    deactivate idp
    activate user
    user ->> kube: 3. Call kubectl<br>with --token being the id_token<br>OR add tokens to .kube/config
    deactivate user
    activate kube
    kube ->> api: 4. Authorization: Bearer...
    deactivate kube
    activate api
    api ->> api: 5. Is JWT signature valid?
    api ->> api: 6. Has the JWT expired? (iat+exp)
    api ->> api: 7. User authorized?
    api -->> kube: 8. Authorized: Perform<br>action and return result
    deactivate api
    activate kube
    kube --x user: 9. Return result
    deactivate kube
{{< /mermaid >}}

1. وارد ارائه‌دهنده هویت (identity provider) خود شوید.
1. ارائه‌دهنده هویت شما یک `access_token`، یک `id_token` و یک `refresh_token` در اختیارتان قرار می‌دهد.
1. هنگام استفاده از `kubectl`، `id_token` خود را با آرگومان خط فرمان `--token` به کار ببرید یا آن را مستقیماً به `kubeconfig` خود اضافه کنید.
1. `kubectl` توکن `id_token` شما را در هدری به نام Authorization به سرور API ارسال می‌کند.
1. سرور API بررسی می‌کند که امضای JWT معتبر باشد.
1. بررسی کنید که `id_token` منقضی نشده باشد.

   اگر عبارات CEL در `AuthenticationConfiguration` پیکربندی شده باشند، اعتبارسنجی claim و/یا کاربر انجام می‌شود.

1. اطمینان حاصل می‌شود که کاربر مجاز است.
1. پس از تأیید مجوز، سرور API پاسخی را به `kubectl` بازمی‌گرداند.
1. `kubectl` بازخورد را به کاربر ارائه می‌دهد.

از آنجا که تمام داده‌های لازم برای اعتبارسنجی هویت شما در `id_token` وجود دارد، کوبرنتیز نیازی ندارد برای این منظور با ارائه‌دهنده هویت تماس بگیرد («phone home»). در مدلی که هر درخواست بدون حالت (stateless) است، این رویکرد راه‌حلی بسیار مقیاس‌پذیر برای احراز هویت فراهم می‌کند. با این حال چند چالش نیز دارد:

1. کوبرنتیز هیچ «رابط وب» برای آغاز فرایند احراز هویت ندارد. مرورگر یا رابطی برای دریافت اعتبارنامه‌ها وجود ندارد؛ به همین دلیل ابتدا باید نزد ارائه‌دهنده هویت خود احراز هویت شوید.
1. `id_token` را نمی‌توان باطل (revoke) کرد. این توکن مانند یک گواهی است، بنابراین باید کوتاه‌مدت باشد (فقط چند دقیقه)؛ در نتیجه دریافت مکرر توکن جدید در هر چند دقیقه می‌تواند بسیار آزاردهنده باشد.
1. برای احراز هویت در داشبورد کوبرنتیز، باید از دستور `kubectl proxy` یا یک reverse proxy استفاده کنید که `id_token` را تزریق می‌کند.

#### پیکربندی سرور API

##### استفاده از آرگومان‌های خط فرمان

برای فعال‌سازی این افزونه، آرگومان‌های خط فرمان زیر را برای سرور API پیکربندی کنید:

| پارامتر | توضیحات | مثال | الزامی |
| --------- | ----------- | ------- | ------- |
| `--oidc-issuer-url` | نشانی ارائه‌دهنده‌ای که به سرور API امکان می‌دهد کلیدهای عمومی امضا را کشف کند. فقط نشانی‌هایی که از طرح `https://` استفاده می‌کنند پذیرفته می‌شوند. این مقدار معمولاً نشانی discovery ارائه‌دهنده است که مسیر آن خالی شده است. | اگر نشانی OIDC discovery صادرکننده `https://accounts.provider.example/.well-known/openid-configuration` باشد، مقدار باید `https://accounts.provider.example` باشد | بله |
| `--oidc-client-id` | شناسه کلاینتی که همه توکن‌ها باید برای آن صادر شده باشند. | kubernetes | بله |
| `--oidc-username-claim` | claim در JWT که به‌عنوان نام کاربری استفاده می‌شود. به‌طور پیش‌فرض `sub` است که انتظار می‌رود شناسه یکتای کاربر نهایی باشد. مدیران می‌توانند بسته به ارائه‌دهنده خود claimهای دیگری مانند `email` یا `name` را انتخاب کنند. با این حال، برای جلوگیری از تداخل نام با افزونه‌های دیگر، به claimهایی غیر از `email` پیشوند نشانی صادرکننده افزوده می‌شود. | sub | خیر |
| `--oidc-username-prefix` | پیشوندی که به claimهای نام کاربری افزوده می‌شود تا از تداخل با نام‌های موجود (مانند کاربران `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های کاربری‌ای مانند `oidc:jane.doe` ایجاد می‌کند. اگر این آرگومان ارائه نشود و `--oidc-username-claim` مقداری غیر از `email` داشته باشد، پیشوند به‌طور پیش‌فرض `( Issuer URL )#` خواهد بود که در آن `( Issuer URL )` مقدار `--oidc-issuer-url` است. با مقدار `-` می‌توان افزودن هرگونه پیشوند را غیرفعال کرد. | `oidc:` | خیر |
| `--oidc-groups-claim` | claim در JWT که به‌عنوان گروه کاربر استفاده می‌شود. اگر این claim وجود داشته باشد، باید آرایه‌ای از رشته‌ها باشد. | groups | خیر |
| `--oidc-groups-prefix` | پیشوندی که به claimهای گروه افزوده می‌شود تا از تداخل با نام‌های موجود (مانند گروه‌های `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های گروهی مانند `oidc:engineering` و `oidc:infra` ایجاد می‌کند. | `oidc:` | خیر |
| `--oidc-required-claim` | یک جفت key=value که claim الزامی در ID Token را توصیف می‌کند. در صورت تنظیم، بررسی می‌شود که این claim با مقدار مطابق در ID Token وجود داشته باشد. برای مشخص کردن چند claim، این آرگومان را تکرار کنید. | `claim=value` | خیر |
| `--oidc-ca-file` | مسیر گواهی مرجع صدور گواهی (CA) که گواهی وب ارائه‌دهنده هویت شما را امضا کرده است. به‌طور پیش‌فرض از CAهای ریشه میزبان استفاده می‌شود. | `/etc/kubernetes/ssl/kc-ca.pem` | خیر |
| `--oidc-signing-algs` | الگوریتم‌های امضای پذیرفته‌شده. مقدار پیش‌فرض RS256 است. مقادیر مجاز عبارت‌اند از: RS256، RS384، RS512، ES256، ES384، ES512، PS256، PS384، PS512. این مقادیر در RFC 7518 به نشانی https://tools.ietf.org/html/rfc7518#section-3.1 تعریف شده‌اند. | `RS512` | خیر |

##### پیکربندی احراز هویت از طریق فایل {#using-authentication-configuration}

{{< feature-state feature_gate_name="StructuredAuthenticationConfiguration" >}}

رویکرد فایل پیکربندی به شما امکان می‌دهد چندین احراز هویت‌کننده JWT پیکربندی کنید که هر کدام `issuer.url` و `issuer.discoveryURL` یکتای خود را دارند. فایل پیکربندی حتی اجازه می‌دهد عبارات [CEL](/docs/reference/using-api/cel/) را برای نگاشت claimها به ویژگی‌های کاربر و برای اعتبارسنجی claimها و اطلاعات کاربر مشخص کنید.
سرور API همچنین هنگام تغییر فایل پیکربندی، احراز هویت‌کننده‌ها را به‌طور خودکار بارگذاری مجدد می‌کند.
می‌توانید از معیار (metric) با نام `apiserver_authentication_config_controller_automatic_reload_last_timestamp_seconds` برای پایش آخرین زمانی که پیکربندی توسط سرور API بارگذاری مجدد شده است استفاده کنید.

باید مسیر پیکربندی احراز هویت را با آرگومان خط فرمان `--authentication-config` برای سرور API مشخص کنید. اگر می‌خواهید به‌جای فایل پیکربندی از آرگومان‌های خط فرمان استفاده کنید، آن‌ها همچنان بدون تغییر کار خواهند کرد. برای دسترسی به قابلیت‌های جدید، مانند پیکربندی چندین احراز هویت‌کننده یا تنظیم چندین audience برای یک صادرکننده، باید به استفاده از فایل پیکربندی روی بیاورید.

برای استفاده از احراز هویت ساختاریافته، آرگومان خط فرمان `--authentication-config` را برای kube-apiserver مشخص کنید. نمونه‌ای از فایل پیکربندی احراز هویت ساختاریافته در ادامه نشان داده شده است.

{{< note >}}
اگر `--authentication-config` را همراه با هر یک از آرگومان‌های خط فرمان `--oidc-*` مشخص کنید، این یک پیکربندی نادرست است. در این حالت، سرور API خطا گزارش می‌کند و بلافاصله خارج می‌شود.
اگر می‌خواهید به استفاده از پیکربندی احراز هویت ساختاریافته روی بیاورید، باید آرگومان‌های خط فرمان `--oidc-*` را حذف کنید و به‌جای آن‌ها از فایل پیکربندی استفاده کنید.
{{< /note >}}

{{< highlight yaml "linenos=false,hl_lines=2-5" >}}
---
#
# CAUTION: this is an example configuration.
#          Do not use this for your own cluster!
#
apiVersion: apiserver.config.k8s.io/v1
kind: AuthenticationConfiguration
# list of authenticators to authenticate Kubernetes users using JWT compliant tokens.
# the maximum number of allowed authenticators is 64.
jwt:
- issuer:
    # url must be unique across all authenticators.
    # url must not conflict with issuer configured in --service-account-issuer.
    url: https://example.com # Same as --oidc-issuer-url.
    # discoveryURL, if specified, overrides the URL used to fetch discovery
    # information instead of using "{url}/.well-known/openid-configuration".
    # The exact value specified is used, so "/.well-known/openid-configuration"
    # must be included in discoveryURL if needed.
    #
    # The "issuer" field in the fetched discovery information must match the "issuer.url" field
    # in the AuthenticationConfiguration and will be used to validate the "iss" claim in the presented JWT.
    # This is for scenarios where the well-known and jwks endpoints are hosted at a different
    # location than the issuer (such as locally in the cluster).
    # discoveryURL must be different from url if specified and must be unique across all authenticators.
    discoveryURL: https://discovery.example.com/.well-known/openid-configuration
    # PEM encoded CA certificates used to validate the connection when fetching
    # discovery information. If not set, the system verifier will be used.
    # Same value as the content of the file referenced by the --oidc-ca-file command line argument.
    certificateAuthority: <PEM encoded CA certificates>    
    # audiences is the set of acceptable audiences the JWT must be issued to.
    # At least one of the entries must match the "aud" claim in presented JWTs.
    audiences:
    - my-app # Same as --oidc-client-id.
    - my-other-app
    # this is required to be set to "MatchAny" when multiple audiences are specified.
    audienceMatchPolicy: MatchAny
    # egressSelectorType is an indicator of which egress selection should be used for sending all traffic related
    # to this issuer (discovery, JWKS, distributed claims, etc).  If unspecified, no custom dialer is used.
    # The StructuredAuthenticationConfigurationEgressSelector feature gate must be enabled
    # before you can use the egressSelectorType field.
    # When specified, the valid choices are "controlplane" and "cluster".  These correspond to the associated
    # values in the --egress-selector-config-file.
    # - controlplane: for traffic intended to go to the control plane.
    # - cluster: for traffic intended to go to the system being managed by Kubernetes.
    egressSelectorType: <egress-selector-type>
  # rules applied to validate token claims to authenticate users.
  claimValidationRules:
    # Same as --oidc-required-claim key=value.
  - claim: hd
    requiredValue: example.com
    # Instead of claim and requiredValue, you can use expression to validate the claim.
    # expression is a CEL expression that evaluates to a boolean.
    # all the expressions must evaluate to true for validation to succeed.
  - expression: 'claims.hd == "example.com"'
    # Message customizes the error message seen in the API server logs when the validation fails.
    message: the hd claim must be set to example.com
  - expression: 'claims.exp - claims.nbf <= 86400'
    message: total token lifetime must not exceed 24 hours
  claimMappings:
    # username represents an option for the username attribute.
    # This is the only required attribute.
    username:
      # Same as --oidc-username-claim. Mutually exclusive with username.expression.
      claim: "sub"
      # Same as --oidc-username-prefix. Mutually exclusive with username.expression.
      # if username.claim is set, username.prefix is required.
      # Explicitly set it to "" if no prefix is desired.
      prefix: ""
      # Mutually exclusive with username.claim and username.prefix.
      # expression is a CEL expression that evaluates to a string.
      #
      # 1.  If username.expression uses 'claims.email', then 'claims.email_verified' must be used in
      #     username.expression or extra[*].valueExpression or claimValidationRules[*].expression.
      #     An example claim validation rule expression that matches the validation automatically
      #     applied when username.claim is set to 'email' is 'claims.?email_verified.orValue(true) == true'.
      #     By explicitly comparing the value to true, we let type-checking see the result will be a boolean, and
      #     to make sure a non-boolean email_verified claim will be caught at runtime.
      # 2.  If the username asserted based on username.expression is the empty string, the authentication
      #     request will fail.
      expression: 'claims.username + ":external-user"'
    # groups represents an option for the groups attribute.
    groups:
      # Same as --oidc-groups-claim. Mutually exclusive with groups.expression.
      claim: "sub"
      # Same as --oidc-groups-prefix. Mutually exclusive with groups.expression.
      # if groups.claim is set, groups.prefix is required.
      # Explicitly set it to "" if no prefix is desired.
      prefix: ""
      # Mutually exclusive with groups.claim and groups.prefix.
      # expression is a CEL expression that evaluates to a string or a list of strings.
      expression: 'claims.roles.split(",")'
    # uid represents an option for the uid attribute.
    uid:
      # Mutually exclusive with uid.expression.
      claim: 'sub'
      # Mutually exclusive with uid.claim
      # expression is a CEL expression that evaluates to a string.
      expression: 'claims.sub'
    # extra attributes to be added to the UserInfo object. Keys must be domain-prefix path and must be unique.
    extra:
      # key is a string to use as the extra attribute key.
      # key must be a domain-prefix path (e.g. example.org/foo). All characters before the first "/" must be a valid
      # subdomain as defined by RFC 1123. All characters trailing the first "/" must
      # be valid HTTP Path characters as defined by RFC 3986.
      # k8s.io, kubernetes.io and their subdomains are reserved for Kubernetes use and cannot be used.
      # key must be lowercase and unique across all extra attributes.
    - key: 'example.com/tenant'
      # valueExpression is a CEL expression that evaluates to a string or a list of strings.
      valueExpression: 'claims.tenant'
  # validation rules applied to the final user object.
  userValidationRules:
    # expression is a CEL expression that evaluates to a boolean.
    # all the expressions must evaluate to true for the user to be valid.
  - expression: "!user.username.startsWith('system:')"
    # Message customizes the error message seen in the API server logs when the validation fails.
    message: 'username cannot used reserved system: prefix'
  - expression: "user.groups.all(group, !group.startsWith('system:'))"
    message: 'groups cannot used reserved system: prefix'
{{< /highlight >}}

* عبارت قانون اعتبارسنجی claim

  `jwt.claimValidationRules[i].expression` عبارتی را نشان می‌دهد که توسط CEL ارزیابی می‌شود.
  عبارات CEL به محتوای payload توکن دسترسی دارند که در متغیر CEL با نام `claims` سازمان‌دهی شده است.
  `claims` نگاشتی (map) از نام claimها (به‌صورت رشته) به مقادیر claimها (از هر نوع) است.

* عبارت قانون اعتبارسنجی کاربر

  `jwt.userValidationRules[i].expression` عبارتی را نشان می‌دهد که توسط CEL ارزیابی می‌شود.
  عبارات CEL به محتوای `userInfo` دسترسی دارند که در متغیر CEL با نام `user` سازمان‌دهی شده است.
  برای آگاهی از schema مربوط به `user`، مستندات API با عنوان [UserInfo](/docs/reference/generated/kubernetes-api/v{{< skew currentVersion >}}/#userinfo-v1-authentication-k8s-io) را ببینید.

* عبارت نگاشت claim

  `jwt.claimMappings.username.expression`، `jwt.claimMappings.groups.expression`، `jwt.claimMappings.uid.expression` و
  `jwt.claimMappings.extra[i].valueExpression` عبارتی را نشان می‌دهند که توسط CEL ارزیابی می‌شود.
  عبارات CEL به محتوای payload توکن دسترسی دارند که در متغیر CEL با نام `claims` سازمان‌دهی شده است.
  `claims` نگاشتی (map) از نام claimها (به‌صورت رشته) به مقادیر claimها (از هر نوع) است.

  برای کسب اطلاعات بیشتر، [مستندات CEL](/docs/reference/using-api/cel/) را ببینید.

  در ادامه نمونه‌هایی از `AuthenticationConfiguration` با payloadهای مختلف توکن آمده است.

  {{< tabs name="example_configuration" >}}
  {{% tab name="توکن معتبر" %}}
  ```yaml
  apiVersion: apiserver.config.k8s.io/v1
  kind: AuthenticationConfiguration
  jwt:
  - issuer:
      url: https://example.com
      audiences:
      - my-app
    claimMappings:
      username:
        expression: 'claims.username + ":external-user"'
      groups:
        expression: 'claims.roles.split(",")'
      uid:
        expression: 'claims.sub'
      extra:
      - key: 'example.com/tenant'
        valueExpression: 'claims.tenant'
    userValidationRules:
    - expression: "!user.username.startsWith('system:')" # the expression will evaluate to true, so validation will succeed.
      message: 'username cannot used reserved system: prefix'
  ```

```bash
  TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY3dF9tOEROWmFTQk1oWGw5QXZTWGhBUC04Y0JmZ0JVbFVpTG5oQkgxdXMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJrdWJlcm5ldGVzIiwiZXhwIjoxNzAzMjMyOTQ5LCJpYXQiOjE3MDExMDcyMzMsImlzcyI6Imh0dHBzOi8vZXhhbXBsZS5jb20iLCJqdGkiOiI3YzMzNzk0MjgwN2U3M2NhYTJjMzBjODY4YWMwY2U5MTBiY2UwMmRkY2JmZWJlOGMyM2I4YjVmMjdhZDYyODczIiwibmJmIjoxNzAxMTA3MjMzLCJyb2xlcyI6InVzZXIsYWRtaW4iLCJzdWIiOiJhdXRoIiwidGVuYW50IjoiNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjRhIiwidXNlcm5hbWUiOiJmb28ifQ.TBWF2RkQHm4QQz85AYPcwLxSk-VLvQW-mNDHx7SEOSv9LVwcPYPuPajJpuQn9C_gKq1R94QKSQ5F6UgHMILz8OfmPKmX_00wpwwNVGeevJ79ieX2V-__W56iNR5gJ-i9nn6FYk5pwfVREB0l4HSlpTOmu80gbPWAXY5hLW0ZtcE1JTEEmefORHV2ge8e3jp1xGafNy6LdJWabYuKiw8d7Qga__HxtKB-t0kRMNzLRS7rka_SfQg0dSYektuxhLbiDkqhmRffGlQKXGVzUsuvFw7IGM5ZWnZgEMDzCI357obHeM3tRqpn5WRjtB8oM7JgnCymaJi-P3iCd88iu1xnzA
  ```

  که در آن payload توکن به شرح زیر است:

  ```json
    {
      "aud": "kubernetes",
      "exp": 1703232949,
      "iat": 1701107233,
      "iss": "https://example.com",
      "jti": "7c337942807e73caa2c30c868ac0ce910bce02ddcbfebe8c23b8b5f27ad62873",
      "nbf": 1701107233,
      "roles": "user,admin",
      "sub": "auth",
      "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db4a",
      "username": "foo"
    }
  ```

  توکن فوق همراه با `AuthenticationConfiguration` بالا، آبجکت `UserInfo` زیر را تولید می‌کند و کاربر با موفقیت احراز هویت می‌شود.

  ```json
  {
      "username": "foo:external-user",
      "uid": "auth",
      "groups": [
          "user",
          "admin"
      ],
      "extra": {
          "example.com/tenant": ["72f988bf-86f1-41af-91ab-2d7cd011db4a"]
      }
  }
  ```
  {{% /tab %}}
  {{% tab name="Fails claim validation" %}}
  ```yaml
  apiVersion: apiserver.config.k8s.io/v1
  kind: AuthenticationConfiguration
  jwt:
  - issuer:
      url: https://example.com
      audiences:
      - my-app
    claimValidationRules:
    - expression: 'claims.hd == "example.com"' # the token below does not have this claim, so validation will fail.
      message: the hd claim must be set to example.com
    claimMappings:
      username:
        expression: 'claims.username + ":external-user"'
      groups:
        expression: 'claims.roles.split(",")'
      uid:
        expression: 'claims.sub'
      extra:
      - key: 'example.com/tenant'
        valueExpression: 'claims.tenant'
    userValidationRules:
    - expression: "!user.username.startsWith('system:')" # the expression will evaluate to true, so validation will succeed.
      message: 'username cannot used reserved system: prefix'
  ```

  ```bash
  TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY3dF9tOEROWmFTQk1oWGw5QXZTWGhBUC04Y0JmZ0JVbFVpTG5oQkgxdXMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJrdWJlcm5ldGVzIiwiZXhwIjoxNzAzMjMyOTQ5LCJpYXQiOjE3MDExMDcyMzMsImlzcyI6Imh0dHBzOi8vZXhhbXBsZS5jb20iLCJqdGkiOiI3YzMzNzk0MjgwN2U3M2NhYTJjMzBjODY4YWMwY2U5MTBiY2UwMmRkY2JmZWJlOGMyM2I4YjVmMjdhZDYyODczIiwibmJmIjoxNzAxMTA3MjMzLCJyb2xlcyI6InVzZXIsYWRtaW4iLCJzdWIiOiJhdXRoIiwidGVuYW50IjoiNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjRhIiwidXNlcm5hbWUiOiJmb28ifQ.TBWF2RkQHm4QQz85AYPcwLxSk-VLvQW-mNDHx7SEOSv9LVwcPYPuPajJpuQn9C_gKq1R94QKSQ5F6UgHMILz8OfmPKmX_00wpwwNVGeevJ79ieX2V-__W56iNR5gJ-i9nn6FYk5pwfVREB0l4HSlpTOmu80gbPWAXY5hLW0ZtcE1JTEEmefORHV2ge8e3jp1xGafNy6LdJWabYuKiw8d7Qga__HxtKB-t0kRMNzLRS7rka_SfQg0dSYektuxhLbiDkqhmRffGlQKXGVzUsuvFw7IGM5ZWnZgEMDzCI357obHeM3tRqpn5WRjtB8oM7JgnCymaJi-P3iCd88iu1xnzA
  ```

  که در آن payload توکن به شرح زیر است:

  ```json
    {
      "aud": "kubernetes",
      "exp": 1703232949,
      "iat": 1701107233,
      "iss": "https://example.com",
      "jti": "7c337942807e73caa2c30c868ac0ce910bce02ddcbfebe8c23b8b5f27ad62873",
      "nbf": 1701107233,
      "roles": "user,admin",
      "sub": "auth",
      "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db4a",
      "username": "foo"
    }
  ```

  توکن فوق همراه با `AuthenticationConfiguration` بالا احراز هویت نخواهد شد، زیرا claim با نام
  `hd` روی `example.com` تنظیم نشده است. سرور API خطای `401 Unauthorized` را برمی‌گرداند.
  {{% /tab %}}
  {{% tab name="Fails user validation" %}}
  ```yaml
  apiVersion: apiserver.config.k8s.io/v1
  kind: AuthenticationConfiguration
  jwt:
  - issuer:
      url: https://example.com
      audiences:
      - my-app
    claimValidationRules:
    - expression: 'claims.hd == "example.com"'
      message: the hd claim must be set to example.com
    claimMappings:
      username:
        expression: '"system:" + claims.username' # this will prefix the username with "system:" and will fail user validation.
      groups:
        expression: 'claims.roles.split(",")'
      uid:
        expression: 'claims.sub'
      extra:
      - key: 'example.com/tenant'
        valueExpression: 'claims.tenant'
    userValidationRules:
    - expression: "!user.username.startsWith('system:')" # the username will be system:foo and expression will evaluate to false, so validation will fail.
      message: 'username cannot used reserved system: prefix'
  ```

  ```bash
  TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6ImY3dF9tOEROWmFTQk1oWGw5QXZTWGhBUC04Y0JmZ0JVbFVpTG5oQkgxdXMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJrdWJlcm5ldGVzIiwiZXhwIjoxNzAzMjMyOTQ5LCJoZCI6ImV4YW1wbGUuY29tIiwiaWF0IjoxNzAxMTEzMTAxLCJpc3MiOiJodHRwczovL2V4YW1wbGUuY29tIiwianRpIjoiYjViMDY1MjM3MmNkMjBlMzQ1YjZmZGZmY2RjMjE4MWY0YWZkNmYyNTlhYWI0YjdlMzU4ODEyMzdkMjkyMjBiYyIsIm5iZiI6MTcwMTExMzEwMSwicm9sZXMiOiJ1c2VyLGFkbWluIiwic3ViIjoiYXV0aCIsInRlbmFudCI6IjcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0YSIsInVzZXJuYW1lIjoiZm9vIn0.FgPJBYLobo9jnbHreooBlvpgEcSPWnKfX6dc0IvdlRB-F0dCcgy91oCJeK_aBk-8zH5AKUXoFTlInfLCkPivMOJqMECA1YTrMUwt_IVqwb116AqihfByUYIIqzMjvUbthtbpIeHQm2fF0HbrUqa_Q0uaYwgy8mD807h7sBcUMjNd215ff_nFIHss-9zegH8GI1d9fiBf-g6zjkR1j987EP748khpQh9IxPjMJbSgG_uH5x80YFuqgEWwq-aYJPQxXX6FatP96a2EAn7wfPpGlPRt0HcBOvq5pCnudgCgfVgiOJiLr_7robQu4T1bis0W75VPEvwWtgFcLnvcQx0JWg
  ```

  که در آن payload توکن به شرح زیر است:

  ```json
    {
      "aud": "kubernetes",
      "exp": 1703232949,
      "hd": "example.com",
      "iat": 1701113101,
      "iss": "https://example.com",
      "jti": "b5b0652372cd20e345b6fdffcdc2181f4afd6f259aab4b7e35881237d29220bc",
      "nbf": 1701113101,
      "roles": "user,admin",
      "sub": "auth",
      "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db4a",
      "username": "foo"
    }
  ```

  توکن فوق همراه با `AuthenticationConfiguration` بالا، آبجکت `UserInfo` زیر را تولید می‌کند:

  ```json
  {
      "username": "system:foo",
      "uid": "auth",
      "groups": [
          "user",
          "admin"
      ],
      "extra": {
          "example.com/tenant": ["72f988bf-86f1-41af-91ab-2d7cd011db4a"]
      }
  }
  ```

  این آبجکت در اعتبارسنجی کاربر ناموفق خواهد بود، زیرا نام کاربری با `system:` آغاز می‌شود.
  سرور API خطای `401 Unauthorized` را برمی‌گرداند.
  {{% /tab %}}
  {{< /tabs >}}



##### محدودیت‌ها {#oidc-limitations}

1. Distributed claimها از طریق عبارت‌های [CEL](/docs/reference/using-api/cel/) کار نمی‌کنند.

کوبرنتیز یک ارائه‌دهنده هویت (Identity Provider) مبتنی بر OpenID Connect ارائه نمی‌کند.
می‌توانید از یک ارائه‌دهنده هویت عمومی OpenID Connect موجود استفاده کنید یا ارائه‌دهنده هویت خودتان را
که پروتکل OpenID Connect را پشتیبانی می‌کند اجرا کنید.

برای اینکه یک ارائه‌دهنده هویت با کوبرنتیز کار کند، باید:

1. از [OpenID connect discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) پشتیبانی کند.

   کلید عمومی برای تأیید امضا، با استفاده از OIDC discovery از نقطه پایانی عمومی issuer کشف می‌شود.
   اگر از فایل پیکربندی احراز هویت استفاده می‌کنید، ارائه‌دهنده هویت نیازی ندارد نقطه پایانی discovery را به‌صورت عمومی در دسترس قرار دهد.
   می‌توانید نقطه پایانی discovery را در مکانی متفاوت از issuer (مثلاً به‌صورت محلی در داخل کلاستر) میزبانی کنید و
   `issuer.discoveryURL` را در فایل پیکربندی مشخص نمایید.

1. با TLS و با رمزنگارهای (cipher) منسوخ‌نشده اجرا شود.
1. گواهی امضاشده توسط یک CA داشته باشد (حتی اگر CA یک CA تجاری نباشد یا خودامضا باشد).

توضیحی درباره الزام شماره ۳ بالا، یعنی لزوم داشتن گواهی امضاشده توسط CA: اگر ارائه‌دهنده هویت خودتان را
مستقر می‌کنید، باید گواهی وب‌سرور ارائه‌دهنده هویت شما توسط گواهی‌ای امضا شده باشد که پرچم `CA` در آن روی `TRUE` تنظیم شده است،
حتی اگر خودامضا باشد. دلیل این امر آن است که پیاده‌سازی کلاینت TLS در GoLang در رعایت استانداردهای مربوط به اعتبارسنجی گواهی
بسیار سخت‌گیر است. اگر CA در دسترس ندارید، می‌توانید با استفاده از ابزارهای استاندارد تولید گواهی،
یک CA ساده و یک جفت گواهی و کلید امضاشده ایجاد کنید.

#### استفاده از kubectl {#using-kubectl}

##### گزینه ۱ - احراز‌هویت‌کننده OIDC

گزینه اول استفاده از احراز‌هویت‌کننده `oidc` در kubectl است که `id_token` را به‌عنوان bearer token
برای همه درخواست‌ها تنظیم می‌کند و پس از انقضای توکن، آن را تازه‌سازی می‌کند. پس از ورود به ارائه‌دهنده هویت خود، از
kubectl برای افزودن `id_token`، `refresh_token`، `client_id` و `client_secret` به‌منظور پیکربندی افزونه استفاده کنید.

ارائه‌دهندگانی که `id_token` را به‌عنوان بخشی از پاسخ refresh token برنمی‌گردانند، توسط این افزونه
پشتیبانی نمی‌شوند و باید از [گزینه ۲](#option-2-use-the-token-option) (مشخص کردن `--token`) استفاده کنند.

```bash
kubectl config set-credentials USER_NAME \
   --auth-provider=oidc \
   --auth-provider-arg=idp-issuer-url=( issuer url ) \
   --auth-provider-arg=client-id=( your client id ) \
   --auth-provider-arg=client-secret=( your client secret ) \
   --auth-provider-arg=refresh-token=( your refresh token ) \
   --auth-provider-arg=idp-certificate-authority=( path to your ca certificate ) \
   --auth-provider-arg=id-token=( your id_token )
```

به‌عنوان مثال، اجرای دستور زیر پس از احراز هویت در ارائه‌دهنده هویت شما:

```bash
kubectl config set-credentials mmosley  \
        --auth-provider=oidc  \
        --auth-provider-arg=idp-issuer-url=https://oidcidp.tremolo.lan:8443/auth/idp/OidcIdP  \
        --auth-provider-arg=client-id=kubernetes  \
        --auth-provider-arg=client-secret=1db158f6-177d-4d9c-8a8b-d36869918ec5  \
        --auth-provider-arg=refresh-token=q1bKLFOyUiosTfawzA93TzZIDzH2TNa2SMm0zEiPKTUwME6BkEo6Sql5yUWVBSWpKUGphaWpxSVAfekBOZbBhaEW+VlFUeVRGcluyVF5JT4+haZmPsluFoFu5XkpXk5BXqHega4GAXlF+ma+vmYpFcHe5eZR+slBFpZKtQA= \
        --auth-provider-arg=idp-certificate-authority=/root/ca.pem \
        --auth-provider-arg=id-token=eyJraWQiOiJDTj1vaWRjaWRwLnRyZW1vbG8ubGFuLCBPVT1EZW1vLCBPPVRybWVvbG8gU2VjdXJpdHksIEw9QXJsaW5ndG9uLCBTVD1WaXJnaW5pYSwgQz1VUy1DTj1rdWJlLWNhLTEyMDIxNDc5MjEwMzYwNzMyMTUyIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJodHRwczovL29pZGNpZHAudHJlbW9sby5sYW46ODQ0My9hdXRoL2lkcC9PaWRjSWRQIiwiYXVkIjoia3ViZXJuZXRlcyIsImV4cCI6MTQ4MzU0OTUxMSwianRpIjoiMm96US15TXdFcHV4WDlHZUhQdy1hZyIsImlhdCI6MTQ4MzU0OTQ1MSwibmJmIjoxNDgzNTQ5MzMxLCJzdWIiOiI0YWViMzdiYS1iNjQ1LTQ4ZmQtYWIzMC0xYTAxZWU0MWUyMTgifQ.w6p4J_6qQ1HzTG9nrEOrubxIMb9K5hzcMPxc9IxPx2K4xO9l-oFiUw93daH3m5pluP6K7eOE6txBuRVfEcpJSwlelsOsW8gb8VJcnzMS9EnZpeA0tW_p-mnkFc3VcfyXuhe5R3G7aa5d8uHv70yJ9Y3-UhjiN9EhpMdfPAoEB9fYKKkJRzF7utTTIPGrSaSU6d2pcpfYKaxIwePzEkT4DfcQthoZdy9ucNvvLoi1DIC-UocFD8HLs8LYKEqSxQvOcvnThbObJ9af71EwmuE21fO5KzMW20KtAeget1gnldOosPtz1G5EwvaQ401-RPQzPGMVBld0_zMCAwZttJ4knw
```

که پیکربندی زیر را تولید می‌کند:

```yaml
users:
- name: mmosley
  user:
    auth-provider:
      config:
        client-id: kubernetes
        client-secret: 1db158f6-177d-4d9c-8a8b-d36869918ec5
        id-token: eyJraWQiOiJDTj1vaWRjaWRwLnRyZW1vbG8ubGFuLCBPVT1EZW1vLCBPPVRybWVvbG8gU2VjdXJpdHksIEw9QXJsaW5ndG9uLCBTVD1WaXJnaW5pYSwgQz1VUy1DTj1rdWJlLWNhLTEyMDIxNDc5MjEwMzYwNzMyMTUyIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJodHRwczovL29pZGNpZHAudHJlbW9sby5sYW46ODQ0My9hdXRoL2lkcC9PaWRjSWRQIiwiYXVkIjoia3ViZXJuZXRlcyIsImV4cCI6MTQ4MzU0OTUxMSwianRpIjoiMm96US15TXdFcHV4WDlHZUhQdy1hZyIsImlhdCI6MTQ4MzU0OTQ1MSwibmJmIjoxNDgzNTQ5MzMxLCJzdWIiOiI0YWViMzdiYS1iNjQ1LTQ4ZmQtYWIzMC0xYTAxZWU0MWUyMTgifQ.w6p4J_6qQ1HzTG9nrEOrubxIMb9K5hzcMPxc9IxPx2K4xO9l-oFiUw93daH3m5pluP6K7eOE6txBuRVfEcpJSwlelsOsW8gb8VJcnzMS9EnZpeA0tW_p-mnkFc3VcfyXuhe5R3G7aa5d8uHv70yJ9Y3-UhjiN9EhpMdfPAoEB9fYKKkJRzF7utTTIPGrSaSU6d2pcpfYKaxIwePzEkT4DfcQthoZdy9ucNvvLoi1DIC-UocFD8HLs8LYKEqSxQvOcvnThbObJ9af71EwmuE21fO5KzMW20KtAeget1gnldOosPtz1G5EwvaQ401-RPQzPGMVBld0_zMCAwZttJ4knw
        idp-certificate-authority: /root/ca.pem
        idp-issuer-url: https://oidcidp.tremolo.lan:8443/auth/idp/OidcIdP
        refresh-token: q1bKLFOyUiosTfawzA93TzZIDzH2TNa2SMm0zEiPKTUwME6BkEo6Sql5yUWVBSWpKUGphaWpxSVAfekBOZbBhaEW+VlFUeVRGcluyVF5JT4+haZmPsluFoFu5XkpXk5BXq
      name: oidc
```

پس از انقضای `id_token` شما، `kubectl` تلاش می‌کند با استفاده از `refresh_token` و `client_secret`
آن را تازه‌سازی کند و مقادیر جدید `refresh_token` و `id_token` را در `.kube/config` ذخیره می‌کند.

##### گزینه ۲ - استفاده از آرگومان خط فرمان `--token` {#option-2-use-the-token-option}

دستور `kubectl` به شما امکان می‌دهد توکن را با آرگومان خط فرمان `--token` ارسال کنید.
`id_token` را در این گزینه کپی و جای‌گذاری کنید:

```bash
kubectl --token=eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL21sYi50cmVtb2xvLmxhbjo4MDQzL2F1dGgvaWRwL29pZGMiLCJhdWQiOiJrdWJlcm5ldGVzIiwiZXhwIjoxNDc0NTk2NjY5LCJqdGkiOiI2RDUzNXoxUEpFNjJOR3QxaWVyYm9RIiwiaWF0IjoxNDc0NTk2MzY5LCJuYmYiOjE0NzQ1OTYyNDksInN1YiI6Im13aW5kdSIsInVzZXJfcm9sZSI6WyJ1c2VycyIsIm5ldy1uYW1lc3BhY2Utdmlld2VyIl0sImVtYWlsIjoibXdpbmR1QG5vbW9yZWplZGkuY29tIn0.f2As579n9VNoaKzoF-dOQGmXkFKf1FMyNV0-va_B63jn-_n9LGSCca_6IVMP8pO-Zb4KvRqGyTP0r3HkHxYy5c81AnIh8ijarruczl-TK_yF5akjSTHFZD-0gRzlevBDiH8Q79NAr-ky0P4iIXS8lY9Vnjch5MF74Zx0c3alKJHJUnnpjIACByfF2SCaYzbWFMUNat-K1PaUk5-ujMBG7yYnr95xD-63n8CO8teGUAAEMx6zRjzfhnhbzX-ajwZLGwGUBT4WqjMs70-6a7_8gZmLZb2az1cZynkFRj2BaCkVT3A2RrjeEwZEtGXlMqKJ1_I2ulrOVsYx01_yD35-rw get nodes
```

### احراز هویت با توکن Webhook

_احراز هویت webhook_ در کوبرنتیز سازوکاری است که با ارسال یک فراخوانی HTTP، توکن‌های bearer را اعتبارسنجی می‌کند.

در ارتباط با نحوهٔ پیکربندی API server، گزینه‌های زیر وجود دارند:

* `--authentication-token-webhook-config-file`: یک فایل پیکربندی که چگونگی دسترسی به سرویس webhook راه دور را توصیف می‌کند.
* `--authentication-token-webhook-cache-ttl`: مدت زمانی که تصمیم‌های احراز هویت در حافظهٔ نهان نگهداری می‌شوند. مقدار پیش‌فرض دو دقیقه است.
* `--authentication-token-webhook-version`: مشخص می‌کند که برای ارسال و دریافت اطلاعات از webhook، از آبجکت‌های `TokenReview` با نسخهٔ `authentication.k8s.io/v1beta1` استفاده شود یا `authentication.k8s.io/v1`. مقدار پیش‌فرض `v1beta1` است.

فایل پیکربندی از قالب فایل [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
استفاده می‌کند. در این فایل، `clusters` به سرویس راه دور و
`users` به webhook مربوط به API server اشاره می‌کند. یک نمونه به شکل زیر است:

```yaml
# Kubernetes API version
apiVersion: v1
# kind of the API object
kind: Config
# clusters refers to the remote service.
clusters:
  - name: name-of-remote-authn-service
    cluster:
      certificate-authority: /path/to/ca.pem         # CA for verifying the remote service.
      server: https://authn.example.com/authenticate # URL of remote service to query. 'https' recommended for production.

# users refers to the API server's webhook configuration.
users:
  - name: name-of-api-server
    user:
      client-certificate: /path/to/cert.pem # cert for the webhook plugin to use
      client-key: /path/to/key.pem          # key matching the cert

# kubeconfig files require a context. Provide one for the API server.
current-context: webhook
contexts:
- context:
    cluster: name-of-remote-authn-service
    user: name-of-api-server
  name: webhook
```

هنگامی که یک کلاینت تلاش می‌کند با استفاده از توکن bearer، همان‌طور که
[پیش‌تر](#putting-a-bearer-token-in-a-request) بیان شد، نزد API server احراز هویت شود، webhook احراز هویت یک آبجکت `TokenReview` سریال‌شده با JSON را که شامل توکن است، با متد POST به سرویس راه دور ارسال می‌کند.

توجه داشته باشید که آبجکت‌های API مربوط به webhook مشمول همان [قواعد سازگاری نسخه‌بندی](/docs/concepts/overview/kubernetes-api/)
هستند که برای سایر آبجکت‌های API کوبرنتیز اعمال می‌شود. پیاده‌سازان باید فیلد `apiVersion` درخواست را بررسی کنند تا از deserialize شدن صحیح اطمینان یابند،
و **باید** با یک آبجکت `TokenReview` هم‌نسخه با درخواست پاسخ دهند.

{{< tabs name="TokenReview_request" >}}
{{% tab name="authentication.k8s.io/v1" %}}
{{< note >}}
به‌منظور سازگاری با نسخه‌های قبلی، API server کوبرنتیز به‌طور پیش‌فرض بررسی‌های توکن (token review) را با نسخهٔ `authentication.k8s.io/v1beta1` ارسال می‌کند.
برای انتخاب دریافت بررسی‌های توکن با نسخهٔ `authentication.k8s.io/v1`، باید API server با گزینهٔ `--authentication-token-webhook-version=v1` راه‌اندازی شود.
{{< /note >}}

```yaml
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "TokenReview",
  "spec": {
    # Opaque bearer token sent to the API server
    "token": "014fbff9a07c...",

    # Optional list of the audience identifiers for the server the token was presented to.
    # Audience-aware token authenticators (for example, OIDC token authenticators)
    # should verify the token was intended for at least one of the audiences in this list,
    # and return the intersection of this list and the valid audiences for the token in the response status.
    # This ensures the token is valid to authenticate to the server it was presented to.
    # If no audiences are provided, the token should be validated to authenticate to the Kubernetes API server.
    "audiences": ["https://myserver.example.com", "https://myserver.internal.example.com"]
  }
}
```
{{% /tab %}}
{{% tab name="authentication.k8s.io/v1beta1" %}}
```yaml
{
  "apiVersion": "authentication.k8s.io/v1beta1",
  "kind": "TokenReview",
  "spec": {
    # Opaque bearer token sent to the API server
    "token": "014fbff9a07c...",

    # Optional list of the audience identifiers for the server the token was presented to.
    # Audience-aware token authenticators (for example, OIDC token authenticators)
    # should verify the token was intended for at least one of the audiences in this list,
    # and return the intersection of this list and the valid audiences for the token in the response status.
    # This ensures the token is valid to authenticate to the server it was presented to.
    # If no audiences are provided, the token should be validated to authenticate to the Kubernetes API server.
    "audiences": ["https://myserver.example.com", "https://myserver.internal.example.com"]
  }
}
```
{{% /tab %}}
{{< /tabs >}}

انتظار می‌رود سرویس راه دور فیلد `status` درخواست را برای نشان دادن موفقیت ورود پر کند.
فیلد `spec` در بدنهٔ پاسخ نادیده گرفته می‌شود و می‌توان آن را حذف کرد.
سرویس راه دور باید پاسخ را با همان نسخهٔ API از `TokenReview` که دریافت کرده است برگرداند.
اعتبارسنجی موفق توکن bearer، پاسخی مانند زیر برمی‌گرداند:

{{< tabs name="TokenReview_response_success" >}}
{{% tab name="authentication.k8s.io/v1" %}}
```yaml
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "TokenReview",
  "status": {
    "authenticated": true,
    "user": {
      # Required
      "username": "janedoe@example.com",
      # Optional
      "uid": "42",
      # Optional group memberships
      "groups": ["developers", "qa"],
      # Optional additional information provided by the authenticator.
      # This should not contain confidential data, as it can be recorded in logs
      # or API objects, and is made available to admission webhooks.
      "extra": {
        "extrafield1": [
          "extravalue1",
          "extravalue2"
        ]
      }
    },
    # Optional list audience-aware token authenticators can return,
    # containing the audiences from the `spec.audiences` list for which the provided token was valid.
    # If this is omitted, the token is considered to be valid to authenticate to the Kubernetes API server.
    "audiences": ["https://myserver.example.com"]
  }
}
```
{{% /tab %}}
{{% tab name="authentication.k8s.io/v1beta1" %}}
```yaml
{
  "apiVersion": "authentication.k8s.io/v1beta1",
  "kind": "TokenReview",
  "status": {
    "authenticated": true,
    "user": {
      # Required
      "username": "janedoe@example.com",
      # Optional
      "uid": "42",
      # Optional group memberships
      "groups": ["developers", "qa"],
      # Optional additional information provided by the authenticator.
      # This should not contain confidential data, as it can be recorded in logs
      # or API objects, and is made available to admission webhooks.
      "extra": {
        "extrafield1": [
          "extravalue1",
          "extravalue2"
        ]
      }
    },
    # Optional list audience-aware token authenticators can return,
    # containing the audiences from the `spec.audiences` list for which the provided token was valid.
    # If this is omitted, the token is considered to be valid to authenticate to the Kubernetes API server.
    "audiences": ["https://myserver.example.com"]
  }
}
```
{{% /tab %}}
{{< /tabs >}}

یک درخواست ناموفق پاسخی مانند زیر برمی‌گرداند:

{{< tabs name="TokenReview_response_error" >}}
{{% tab name="authentication.k8s.io/v1" %}}
```yaml
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "TokenReview",
  "status": {
    "authenticated": false,
    # Optionally include details about why authentication failed.
    # If no error is provided, the API will return a generic Unauthorized message.
    # The error field is ignored when authenticated=true.
    "error": "Credentials are expired"
  }
}
```
{{% /tab %}}
{{% tab name="authentication.k8s.io/v1beta1" %}}
```yaml
{
  "apiVersion": "authentication.k8s.io/v1beta1",
  "kind": "TokenReview",
  "status": {
    "authenticated": false,
    # Optionally include details about why authentication failed.
    # If no error is provided, the API will return a generic Unauthorized message.
    # The error field is ignored when authenticated=true.
    "error": "Credentials are expired"
  }
}
```
{{% /tab %}}
{{< /tabs >}}

### پروکسی معکوس احراز هویت‌کننده {#authenticating-proxy}

{{< warning >}}
اگر مرجع صدور گواهی (CA) دارید که در زمینه‌ای دیگر نیز استفاده می‌شود، به آن مرجع صدور گواهی برای شناسایی کلاینت‌های پروکسی احراز هویت‌کننده **اعتماد نکنید**، مگر آنکه خطرات آن و سازوکارهای محافظت از استفادهٔ آن CA را درک کرده باشید.
{{< /warning >}}

API server را می‌توان به‌گونه‌ای پیکربندی کرد که کاربران را از روی مقادیر هدر درخواست، مانند `X-Remote-User`، شناسایی کند.
این قابلیت برای استفاده همراه با یک _پروکسی احراز هویت‌کننده_ طراحی شده است که این هدرها را تنظیم می‌کند.

استفاده از پروکسی معکوس احراز هویت‌کننده با [جعل هویت کاربر](/docs/reference/access-authn-authz/user-impersonation/) متفاوت است.
در جعل هویت کاربر، یک کاربر از API server می‌خواهد درخواست را طوری در نظر بگیرد که گویی توسط کاربری دیگر ارسال شده است. در پروکسی معکوس احراز هویت‌کننده، API server به کلاینت مستقیم خود اعتماد می‌کند که اطلاعات مربوط به هویت اصل (principal) ارسال‌کنندهٔ درخواست اولیه را ارائه دهد.

برای آشنایی با پیکربندی این قابلیت از طریق آرگومان‌های خط فرمان، به [پیکربندی هدرهای درخواست وب](#api-server-authn-config-cli-reverse-proxy) مراجعه کنید.

#### نمونه {#authenticating-proxy-example}

برای مثال، با این پیکربندی:

```
--requestheader-username-headers=X-Remote-User
--requestheader-group-headers=X-Remote-Group
--requestheader-extra-headers-prefix=X-Remote-Extra-
```

این درخواست:

```http
GET / HTTP/1.1
X-Remote-User: fido
X-Remote-Group: dogs
X-Remote-Group: dachshunds
X-Remote-Extra-Acme.com%2Fproject: some-project
X-Remote-Extra-Scopes: openid
X-Remote-Extra-Scopes: profile
```

منجر به این اطلاعات کاربر می‌شود:

```yaml
name: fido
groups:
- dogs
- dachshunds
extra:
  acme.com/project:
  - some-project
  scopes:
  - openid
  - profile
```


#### گواهی کلاینت {#reverse-proxy-client-certificate}

برای جلوگیری از جعل هدر، پروکسی احراز هویت‌کننده ملزم است پیش از بررسی هدرهای درخواست، یک گواهی کلاینت معتبر را به API server ارائه دهد تا در برابر CA مشخص‌شده اعتبارسنجی شود.

برای حالت احراز هویت مبتنی بر هدر درخواست، به مرجع [گزینهٔ خط فرمان](#api-server-authn-config-cli-reverse-proxy) مراجعه کنید.

<!-- deliberately repeating the earlier warning -->
از CA‌ای که در زمینه‌ای دیگر استفاده می‌شود **دوباره استفاده نکنید**، مگر آنکه خطرات آن و سازوکارهای محافظت از استفادهٔ آن CA را درک کرده باشید.

### یکپارچه‌سازی فایل توکن ایستا {#static-token-file}

هنگامی که گزینهٔ `--token-auth-file=<SOMEFILE>` در خط فرمان داده شود، API server توکن‌های bearer ایستا را از یک فایل می‌خواند.
در کوبرنتیز {{< skew currentVersion >}}، توکن‌ها به‌طور نامحدود معتبر می‌مانند و فهرست توکن‌ها بدون راه‌اندازی مجدد API server قابل تغییر نیست.

فایل توکن یک فایل CSV با حداقل ۳ ستون است: توکن، نام کاربر، شناسهٔ یکتای کاربر (uid)،
و پس از آن فهرستی اختیاری از نام گروه‌ها که با ویرگول از هم جدا شده‌اند.


{{< note >}}
اگر بیش از یک گروه دارید، ستون باید داخل دابل‌کوتیشن قرار گیرد، مانند:

```conf
token,user,uid,"group1,group2,group3"
```
{{< /note >}}

استفاده از فایل توکن ایستا برای توکن‌هایی مناسب است که ماهیتاً
بلندمدت و ایستا هستند و شاید هرگز چرخانده (rotate) نشوند. همچنین زمانی مفید است
که کلاینت به یک API server مشخص در control plane محلی باشد،
مانند یک عامل پایش (monitoring agent).

اگر در زمان آماده‌سازی کلاستر از این روش استفاده می‌کنید و سپس به
روش احراز هویت دیگری که برای بلندمدت استفاده خواهد شد منتقل می‌شوید،
باید توکنی را که برای راه‌اندازی اولیه (bootstrap) به کار رفته غیرفعال کنید (این کار نیازمند
راه‌اندازی مجدد هر API server است).

در شرایط دیگر، و به‌ویژه جایی که چرخش بسیار سریع توکن
اهمیت دارد، پروژهٔ کوبرنتیز استفاده از
[احراز هویت‌کنندهٔ توکن webhook](#webhook-token-authentication) را به‌جای این سازوکار توصیه می‌کند.

## جعل هویت کاربر {#user-impersonation}

[جعل هویت کاربر](/docs/reference/access-authn-authz/user-impersonation/) روشی فراهم می‌کند که در آن یک کاربر می‌تواند از طریق هدرهای جعل هویت (impersonation) به‌عنوان کاربری دیگر عمل کند.

## پیکربندی احراز هویت {#api-server-authn-config}

می‌توانید احراز هویت کوبرنتیز را یا با استفاده از
[آرگومان‌های خط فرمان](#api-server-authn-config-cli) یا با استفاده از یک
[فایل پیکربندی](#api-server-authn-config-file) پیکربندی کنید.

معمولاً از ترکیبی از این رویکردها استفاده می‌شود.

### پیکربندی از طریق آرگومان‌های خط فرمان {#api-server-authn-config-cli}

می‌توانید از آرگومان‌های خط فرمان زیر برای پیکربندی نحوهٔ احراز هویت کلاینت‌ها توسط control plane کلاستر خود استفاده کنید.

[مرجع خط فرمان](/docs/reference/command-line-tools-reference/kube-apiserver/) مربوط به API server
تمام آرگومان‌های خط فرمان مرتبط را با جزئیات بیشتری شرح می‌دهد.

#### پیکربندی احراز هویت ناشناس {#api-server-authn-config-cli-anonymous}

`--anonymous-auth`
: مشخص می‌کند که آیا کلاینت‌هایی که احراز هویت نشده‌اند می‌توانند از طریق درگاه امن API server درخواست ارسال کنند یا خیر. درخواست‌های ناشناس دارای نام کاربری `system:anonymous` و نام گروه `system:unauthenticated` هستند. همچنین [درخواست‌های ناشناس](#anonymous-requests) را ببینید.

#### پیکربندی توکن Bootstrap {#api-server-authn-config-cli-bootstrap}

`--enable-bootstrap-token-auth`
: هنگامی که این پرچم تنظیم شده باشد، می‌توانید از [توکن‌های bootstrap](#bootstrap-tokens) برای احراز هویت استفاده کنید.

#### پیکربندی احراز هویت با گواهی {#api-server-authn-config-cli-x-509}

`--client-ca-file`
: مسیر trust anchor(های) مورد استفاده برای اعتبارسنجی هویت کلاینت، زمانی که کلاینت‌ها از احراز هویت با گواهی X.509 استفاده می‌کنند.

#### پیکربندی OIDC {#api-server-authn-config-cli-oidc}

`--oidc-ca-file`
: مسیر trust anchor(های) مورد استفاده برای اعتبارسنجی هویت کلاینت، زمانی که کلاینت‌ها از OIDC استفاده می‌کنند.

`--oidc-client-id`
: شناسهٔ کلاینت (client ID) برای کلاینت OpenID Connect.

`--oidc-username-claim`
: نام یک claim در JWT که برای تعیین نام کاربری استفاده می‌شود. نام claim پیش‌فرض `sub` است، زیرا این claim باید شناسهٔ یکتای کاربر نهایی باشد. می‌توانید claimهای دیگری مانند `email` یا `name` را انتخاب کنید. برای claimهایی غیر از `sub` یا `email`، kube-apiserver یک پیشوند به نام گروه اضافه می‌کند (تا از تداخل نام‌ها جلوگیری شود).

`--oidc-username-prefix`
: پیشوندی که به ابتدای claimهای نام کاربری افزوده می‌شود تا از تداخل با نام‌های موجود (مانند کاربران `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های کاربری‌ای مانند `oidc:jane.doe` ایجاد می‌کند. اگر این آرگومان ارائه نشود و مقدار `--oidc-username-claim` چیزی غیر از `email` باشد، پیشوند به‌طور پیش‌فرض `( Issuer URL )#` خواهد بود که در آن `( Issuer URL )` مقدار `--oidc-issuer-url` است. می‌توانید مقدار پیشوند را `-` تعیین کنید تا افزودن پیشوند به نام کاربری غیرفعال شود.

`--oidc-groups-claim`
: نام یک claim سفارشی OpenID Connect برای تعیین گروه‌های کاربر. claim موجود در توکن باید آرایه‌ای از رشته‌ها باشد. مقدار پیش‌فرض ندارد.

`--oidc-groups-prefix`
: پیشوندی که به ابتدای claimهای گروه افزوده می‌شود تا از تداخل با نام‌های موجود (مانند گروه‌های `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های گروهی مانند `oidc:engineering` و `oidc:infra` ایجاد می‌کند. پیشوند پیش‌فرض `oidc:` است.

`--oidc-issuer-url`
: نشانی URL صادرکنندهٔ OpenID. طرح (scheme) این URL **باید** `https` باشد. اگر نشانی OIDC discovery مربوط به صادرکننده `https://accounts.provider.example/.well-known/openid-configuration` باشد، مقدار آن باید `https://accounts.provider.example` باشد.

`--oidc-required-claim`
: claim‌ای که پیش از آنکه کوبرنتیز یک کلاینت را احراز هویت کند، باید در توکن وجود داشته باشد. قالب آن `key=value` است. می‌توانید این آرگومان را بیش از یک بار مشخص کنید.

`--oidc-signing-algs`
: الگوریتم‌های امضای پذیرفته‌شده. مقادیر مجاز عبارت‌اند از: RS256، RS384، RS512، ES256، ES384، ES512، PS256، PS384، PS512. این مقادیر در [RFC 7518](https://tools.ietf.org/html/rfc7518#section-3.1) تعریف شده‌اند. مقدار پیش‌فرض `RS512` است.

#### پیکربندی ServiceAccount {#api-server-authn-config-cli-sa}

`--api-audiences`
: مخاطب (audience) احراز هویت را برای توکن‌های service account تعریف می‌کند.

`--service-account-extend-token-expiration`
: این پرچم تمدید انقضای projected service account را هنگام تولید توکن فعال می‌کند، که به گذار ایمن از توکن‌های قدیمی (legacy) به قابلیت توکن‌های service account مقید (bound) کمک می‌کند. [احراز هویت اعتبارنامه‌های service account](/docs/concepts/security/service-accounts/#authenticating-credentials) را ببینید.

`--service-account-issuer`
: شناسهٔ صادرکنندهٔ توکن service account. صادرکننده این شناسه را در claim با نام `iss` هر توکن صادرشده اعلام می‌کند. پروژهٔ کوبرنتیز توصیه می‌کند در اینجا از یک URL با طرح `https` استفاده شود.

`--service-account-jwks-uri`
: URI مربوط به [JSON Web Key Set](https://www.rfc-editor.org/rfc/rfc7517) را در سند discovery که در `/.well-known/openid-configuration` ارائه می‌شود، بازنویسی (override) می‌کند.

`--service-account-key-file`
: مسیر فایلی که حاوی کلیدهای عمومی یا خصوصی X.509 با رمزگذاری PEM (از نوع RSA یا ECDSA) است و برای تأیید توکن‌های ServiceAccount استفاده می‌شود. فایل مشخص‌شده می‌تواند حاوی چند کلید باشد و می‌توانید این آرگومان را چندین بار با مسیرهای متفاوت مشخص کنید.

`--service-account-lookup`
: اگر true باشد، API server به‌عنوان بخشی از احراز هویت بررسی می‌کند که توکن‌های ServiceAccount در etcd وجود دارند.

`--service-account-max-token-expiration`
: بیشینهٔ مدت اعتبار یک توکن که توسط صادرکنندهٔ توکن service account ایجاد می‌شود، به‌صورت یک رشتهٔ مدت‌زمان (duration) کوبرنتیز.

`--service-account-signing-endpoint`
: مسیر سوکتی که یک امضاکنندهٔ JWT خارجی روی آن گوش می‌دهد. می‌توانید از این گزینه برای یکپارچه‌سازی با یک امضاکنندهٔ توکن خارجی استفاده کنید.

`--service-account-signing-key-file`
: مسیر فایلی که حاوی کلید خصوصی فعلی صادرکنندهٔ توکن service account است. تغییراتی که در این فایل هنگام اجرای API server اعمال شوند، دوباره خوانده **نمی‌شوند**.

#### پیکربندی توکن ایستا {#api-server-authn-config-cli-bearer}

`--token-auth-file`
: مسیر فایل پیکربندی [توکن‌های bearer ایستا](#static-token-file). تغییراتی که در این فایل هنگام اجرای API server اعمال شوند، دوباره خوانده **نمی‌شوند**.

#### پیکربندی احراز هویت با Webhook {#api-server-authn-config-cli-webhook}

`--authentication-token-webhook-cache-ttl`
: مدت‌زمانی (به‌صورت مشخصات duration کوبرنتیز) که API server باید نتیجهٔ فراخوانی‌های HTTP برای اعتبارسنجی توکن‌ها را در حافظهٔ نهان نگه دارد.

`--authentication-token-webhook-config-file`
: مسیر یک پیکربندی کلاینت با قالب kubeconfig که مشخص می‌کند API server هنگام انجام فراخوانی‌های HTTP چگونه احراز هویت می‌کند. تغییراتی که در این فایل هنگام اجرای API server اعمال شوند، دوباره خوانده **نمی‌شوند**.

`--authentication-token-webhook-version`
: نسخهٔ API مربوط به TokenReview که هنگام انجام فراخوانی‌های HTTP برای بررسی توکن‌ها استفاده می‌شود.

#### پیکربندی احراز هویت درخواست وب {#api-server-authn-config-cli-reverse-proxy}

<!-- trailing whitespace (exactly two spaces) is significant in the following list -->

{{< caution >}}
پیش از تعیین این آرگومان‌های خط فرمان، باید مستندات مربوط به پیکربندی [پروکسی احراز هویت](#authenticating-proxy) را مطالعه کنید،
زیرا توصیه‌های امنیتی مهمی دربارهٔ امنیت اطلاعات وجود دارد
که باید آن‌ها را رعایت کنید.
{{< /caution >}}

`--requestheader-client-ca-file`
: _الزامی._
  مسیر یک بستهٔ گواهی با رمزگذاری PEM که حاوی trust anchor(های) برای اعتبارسنجی هویت پروکسی احراز هویت است.   
  یک [گواهی کلاینت](#reverse-proxy-client-certificate) معتبر
  باید ارائه شود و در برابر مراجع صدور گواهی موجود در فایل مشخص‌شده اعتبارسنجی گردد، پیش از آنکه
  هدرهای درخواست برای نام‌های کاربری بررسی شوند.

`--requestheader-allowed-names`
: _اختیاری._ فهرستی از مقادیر Common Name (CN) که با کاما از هم جدا شده‌اند.  
  اگر تنظیم شود، پیش از بررسی هدرهای درخواست برای نام‌های کاربری، باید یک گواهی کلاینت معتبر
  با CN موجود در فهرست مشخص‌شده ارائه شود. اگر خالی باشد، هر CN مجاز است.

`--requestheader-username-headers`
: _الزامی؛ بدون حساسیت به بزرگی و کوچکی حروف._ نام هدرهایی که برای هویت کاربر، به ترتیب بررسی می‌شوند.  
  نخستین هدری که حاوی مقدار باشد به‌عنوان نام کاربری استفاده می‌شود.

`--requestheader-group-headers`
: _اختیاری؛ بدون حساسیت به بزرگی و کوچکی حروف._
  نام هدرهایی که برای گروه‌های کاربر، به ترتیب بررسی می‌شوند.  
  `X-Remote-Group` پیشنهاد می‌شود.
  تمام مقادیر موجود در تمام هدرهای مشخص‌شده به‌عنوان نام گروه استفاده می‌شوند.

`--requestheader-extra-headers-prefix`
: _اختیاری؛ بدون حساسیت به بزرگی و کوچکی حروف._
  پیشوندهای هدری که برای تعیین اطلاعات اضافی دربارهٔ کاربر جست‌وجو می‌شوند.  
  `X-Remote-Extra-` پیشنهاد می‌شود.
  داده‌های اضافی معمولاً توسط افزونه(های) احراز مجوز پیکربندی‌شده استفاده می‌شوند.
  از هر هدری که با هر یک از پیشوندهای مشخص‌شده آغاز شود، پیشوند حذف می‌شود.
  باقی‌ماندهٔ نام هدر به حروف کوچک تبدیل می‌شود و [رمزگشایی درصدی (percent-decode)](https://tools.ietf.org/html/rfc3986#section-2.1) می‌گردد
  و به کلید extra تبدیل می‌شود و مقدار هدر، مقدار extra خواهد بود.


### پیکربندی از طریق فایل پیکربندی {#api-server-authn-config-file}

{{< feature-state feature_gate_name="StructuredAuthenticationConfiguration" >}}

هنگامی که آرگومان خط فرمان `--authentication-config` را به kube-apiserver می‌دهید، API server
فایلی را که در مسیر مشخص‌شده قرار دارد بارگذاری می‌کند و از محتوای آن فایل برای پیکربندی احراز هویت استفاده می‌کند.

محتوای آن فایل را می‌توان در حین اجرای API server تغییر داد و در این صورت، API server پس از آن فایل را دوباره می‌خواند.

{{< note >}}
تغییرات این فایل باید به‌صورت اتمیک انجام شود (برای مثال: نوشتن در یک فایل موقت هم‌سطح، سپس تغییر نام فایل موقت برای جایگزینی این فایل).
{{< /note >}}

#### مسیر فایل پیکربندی {#api-server-authn-config-cli-general}

`--authentication-config`
: این آرگومان خط فرمان ویژه مشخص می‌کند که می‌خواهید [احراز هویت را با استفاده از یک فایل پیکربندی، پیکربندی کنید](#api-server-authn-config-file).

#### مثال {#api-server-authn-config-file-example}

در اینجا نمونه‌ای از یک فایل پیکربندی احراز هویت (ساختاریافتهٔ) کوبرنتیز آمده است:

{{< highlight yaml "linenos=false,hl_lines=2-5" >}}
---
#
# CAUTION: this is an example configuration.
#          Check and amend this before you use it in your own cluster!
#
apiVersion: apiserver.config.k8s.io/v1
kind: AuthenticationConfiguration
anonymous:
  enabled: false
{{< /highlight >}}

## افزونه‌های اعتبارنامهٔ client-go {#client-go-credential-plugins}

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

`k8s.io/client-go` و ابزارهایی که از آن استفاده می‌کنند، مانند `kubectl` و `kubelet`، قادرند
یک فرمان خارجی را اجرا کنند تا اعتبارنامه‌های کاربر را دریافت نمایند.

این قابلیت برای یکپارچه‌سازی‌های سمت کلاینت با پروتکل‌های احراز هویتی در نظر گرفته شده است که به‌صورت بومی
توسط `k8s.io/client-go` پشتیبانی نمی‌شوند (مانند LDAP، Kerberos، OAuth2، SAML و غیره). افزونه
منطق مختص پروتکل را پیاده‌سازی می‌کند و سپس اعتبارنامه‌های مبهم (opaque) را برای استفاده بازمی‌گرداند. تقریباً تمام موارد استفاده از افزونه‌های اعتبارنامه
به یک مؤلفهٔ سمت سرور با پشتیبانی از [webhook token authenticator](#webhook-token-authentication) نیاز دارند
تا قالب اعتبارنامه‌ای را که افزونهٔ کلاینت تولید کرده است تفسیر کند.

{{< note >}}
نسخه‌های قدیمی‌تر `kubectl` پشتیبانی داخلی برای احراز هویت در AKS و GKE را شامل می‌شدند، اما این پشتیبانی دیگر وجود ندارد.
{{< /note >}}

### نمونهٔ مورد استفاده {#example-use-case}

در یک سناریوی فرضی، یک سازمان یک سرویس خارجی اجرا می‌کند که اعتبارنامه‌های LDAP را
با توکن‌های امضاشدهٔ مختص کاربر مبادله می‌کند. این سرویس همچنین قادر است به درخواست‌های [webhook token
authenticator](#webhook-token-authentication) برای اعتبارسنجی توکن‌ها پاسخ دهد. کاربران باید
یک افزونهٔ اعتبارنامه را روی ایستگاه کاری خود نصب کنند.

برای احراز هویت در برابر API:

* کاربر یک فرمان `kubectl` اجرا می‌کند.
* افزونهٔ اعتبارنامه از کاربر اعتبارنامه‌های LDAP را درخواست می‌کند و اعتبارنامه‌ها را با سرویس خارجی در ازای یک توکن مبادله می‌کند.
* افزونهٔ اعتبارنامه توکن را به client-go بازمی‌گرداند و client-go آن را به‌عنوان توکن bearer در برابر API server استفاده می‌کند.
* API server از [webhook token authenticator](#webhook-token-authentication) برای ارسال یک `TokenReview` به سرویس خارجی استفاده می‌کند.
* سرویس خارجی امضای توکن را تأیید می‌کند و نام کاربری و گروه‌های کاربر را بازمی‌گرداند.

### پیکربندی {#configuration}

افزونه‌های اعتبارنامه از طریق [فایل‌های پیکربندی kubectl](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
و به‌عنوان بخشی از فیلدهای کاربر پیکربندی می‌شوند.

{{< tabs name="exec_plugin_kubeconfig_example_1" >}}
{{% tab name="client.authentication.k8s.io/v1" %}}
```yaml
apiVersion: v1
kind: Config
users:
- name: my-user
  user:
    exec:
      # Command to execute. Required.
      command: "example-client-go-exec-plugin"

      # API version to use when decoding the ExecCredentials resource. Required.
      #
      # The API version returned by the plugin MUST match the version listed here.
      #
      # To integrate with tools that support multiple versions (such as client.authentication.k8s.io/v1beta1),
      # set an environment variable, pass an argument to the tool that indicates which version the exec plugin expects,
      # or read the version from the ExecCredential object in the KUBERNETES_EXEC_INFO environment variable.
      apiVersion: "client.authentication.k8s.io/v1"

      # Environment variables to set when executing the plugin. Optional.
      env:
      - name: "FOO"
        value: "bar"

      # Arguments to pass when executing the plugin. Optional.
      args:
      - "arg1"
      - "arg2"

      # Text shown to the user when the executable doesn't seem to be present. Optional.
      installHint: |
        example-client-go-exec-plugin is required to authenticate
        to the current cluster.  It can be installed:

        On macOS: brew install example-client-go-exec-plugin

        On Ubuntu: apt-get install example-client-go-exec-plugin

        On Fedora: dnf install example-client-go-exec-plugin

        ...

      # Whether or not to provide cluster information, which could potentially contain
      # very large CA data, to this exec plugin as a part of the KUBERNETES_EXEC_INFO
      # environment variable.
      provideClusterInfo: true

      # The contract between the exec plugin and the standard input I/O stream. If the
      # contract cannot be satisfied, this plugin will not be run and an error will be
      # returned. Valid values are "Never" (this exec plugin never uses standard input),
      # "IfAvailable" (this exec plugin wants to use standard input if it is available),
      # or "Always" (this exec plugin requires standard input to function). Required.
      interactiveMode: Never
clusters:
- name: my-cluster
  cluster:
    server: "https://172.17.4.100:6443"
    certificate-authority: "/etc/kubernetes/ca.pem"
    extensions:
    - name: client.authentication.k8s.io/exec # reserved extension name for per cluster exec config
      extension:
        arbitrary: config
        this: can be provided via the KUBERNETES_EXEC_INFO environment variable upon setting provideClusterInfo
        you: ["can", "put", "anything", "here"]
contexts:
- name: my-cluster
  context:
    cluster: my-cluster
    user: my-user
current-context: my-cluster
```
{{% /tab %}}
{{% tab name="client.authentication.k8s.io/v1beta1" %}}
```yaml
apiVersion: v1
kind: Config
users:
- name: my-user
  user:
    exec:
      # Command to execute. Required.
      command: "example-client-go-exec-plugin"

      # API version to use when decoding the ExecCredentials resource. Required.
      #
      # The API version returned by the plugin MUST match the version listed here.
      #
      # To integrate with tools that support multiple versions (such as client.authentication.k8s.io/v1),
      # set an environment variable, pass an argument to the tool that indicates which version the exec plugin expects,
      # or read the version from the ExecCredential object in the KUBERNETES_EXEC_INFO environment variable.
      apiVersion: "client.authentication.k8s.io/v1beta1"

      # Environment variables to set when executing the plugin. Optional.
      env:
      - name: "FOO"
        value: "bar"

      # Arguments to pass when executing the plugin. Optional.
      args:
      - "arg1"
      - "arg2"

      # Text shown to the user when the executable doesn't seem to be present. Optional.
      installHint: |
        example-client-go-exec-plugin is required to authenticate
        to the current cluster.  It can be installed:

        On macOS: brew install example-client-go-exec-plugin

        On Ubuntu: apt-get install example-client-go-exec-plugin

        On Fedora: dnf install example-client-go-exec-plugin

        ...

      # Whether or not to provide cluster information, which could potentially contain
      # very large CA data, to this exec plugin as a part of the KUBERNETES_EXEC_INFO
      # environment variable.
      provideClusterInfo: true

      # The contract between the exec plugin and the standard input I/O stream. If the
      # contract cannot be satisfied, this plugin will not be run and an error will be
      # returned. Valid values are "Never" (this exec plugin never uses standard input),
      # "IfAvailable" (this exec plugin wants to use standard input if it is available),
      # or "Always" (this exec plugin requires standard input to function). Optional.
      # Defaults to "IfAvailable".
      interactiveMode: Never
clusters:
- name: my-cluster
  cluster:
    server: "https://172.17.4.100:6443"
    certificate-authority: "/etc/kubernetes/ca.pem"
    extensions:
    - name: client.authentication.k8s.io/exec # reserved extension name for per cluster exec config
      extension:
        arbitrary: config
        this: can be provided via the KUBERNETES_EXEC_INFO environment variable upon setting provideClusterInfo
        you: ["can", "put", "anything", "here"]
contexts:
- name: my-cluster
  context:
    cluster: my-cluster
    user: my-user
current-context: my-cluster
```
{{% /tab %}}
{{< /tabs >}}

مسیرهای نسبی فرمان نسبت به دایرکتوری فایل پیکربندی تفسیر می‌شوند. اگر
KUBECONFIG روی `/home/jane/kubeconfig` تنظیم شده باشد و فرمان exec برابر `./bin/example-client-go-exec-plugin` باشد،
فایل اجرایی `/home/jane/bin/example-client-go-exec-plugin` اجرا می‌شود.

```yaml
- name: my-user
  user:
    exec:
      # Path relative to the directory of the kubeconfig
      command: "./bin/example-client-go-exec-plugin"
      apiVersion: "client.authentication.k8s.io/v1"
      interactiveMode: Never
```

### فرمت‌های ورودی و خروجی

دستور اجراشده یک آبجکت `ExecCredential` را در `stdout` چاپ می‌کند. `k8s.io/client-go`
با استفاده از اعتبارنامه‌های بازگردانده‌شده در `status`، در برابر API کوبرنتیز احراز هویت می‌کند.
به دستور اجراشده، یک آبجکت `ExecCredential` از طریق متغیر محیطی `KUBERNETES_EXEC_INFO`
به‌عنوان ورودی داده می‌شود. این ورودی شامل اطلاعات مفیدی مانند نسخه API مورد انتظار
آبجکت `ExecCredential` بازگردانده‌شده و همچنین این است که آیا افزونه می‌تواند برای تعامل
با کاربر از `stdin` استفاده کند یا خیر.

هنگامی که دستور از یک نشست تعاملی (یعنی یک ترمینال) اجرا می‌شود، `stdin` می‌تواند مستقیماً در اختیار
افزونه قرار گیرد. افزونه‌ها باید از فیلد `spec.interactive` در آبجکت `ExecCredential` ورودی
موجود در متغیر محیطی `KUBERNETES_EXEC_INFO` استفاده کنند تا مشخص شود آیا `stdin` فراهم شده است یا خیر.
نیازمندی افزونه به `stdin` (یعنی اینکه `stdin` برای اجرای موفق افزونه اختیاری است، اکیداً لازم است،
یا هرگز استفاده نمی‌شود) از طریق فیلد `user.exec.interactiveMode` در
[kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
اعلام می‌شود (مقادیر معتبر در جدول زیر آمده است). فیلد `user.exec.interactiveMode` در
`client.authentication.k8s.io/v1beta1` اختیاری و در `client.authentication.k8s.io/v1` الزامی است.

{{< table caption="مقادیر interactiveMode" >}}
| مقدار `interactiveMode` | معنا |
| ----------------------- | ------- |
| `Never` | این افزونه exec هرگز نیازی به ورودی استاندارد ندارد؛ بنابراین افزونه exec صرف‌نظر از اینکه ورودی استاندارد برای دریافت ورودی از کاربر در دسترس باشد یا نباشد، اجرا خواهد شد. |
| `IfAvailable` | این افزونه exec در صورت در دسترس بودن ورودی استاندارد مایل به استفاده از آن است، اما در صورت در دسترس نبودن آن نیز می‌تواند کار کند. بنابراین افزونه exec صرف‌نظر از اینکه stdin برای دریافت ورودی از کاربر در دسترس باشد یا نباشد، اجرا خواهد شد. اگر ورودی استاندارد برای دریافت ورودی از کاربر در دسترس باشد، در اختیار این افزونه exec قرار می‌گیرد. |
| `Always` | این افزونه exec برای اجرا به ورودی استاندارد نیاز دارد؛ بنابراین افزونه exec تنها در صورتی اجرا می‌شود که ورودی استاندارد برای دریافت ورودی از کاربر در دسترس باشد. اگر ورودی استاندارد برای دریافت ورودی از کاربر در دسترس نباشد، افزونه exec اجرا نخواهد شد و اجراکننده افزونه exec یک خطا بازمی‌گرداند. |
{{< /table >}}

برای استفاده از اعتبارنامه‌های توکن حامل (bearer token)، افزونه یک توکن را در status آبجکت
[`ExecCredential`](/docs/reference/config-api/client-authentication.v1beta1/#client-authentication-k8s-io-v1beta1-ExecCredential)
بازمی‌گرداند.

{{< tabs name="exec_plugin_ExecCredential_example_1" >}}
{{% tab name="client.authentication.k8s.io/v1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1",
  "kind": "ExecCredential",
  "status": {
    "token": "my-bearer-token"
  }
}
```
{{% /tab %}}
{{% tab name="client.authentication.k8s.io/v1beta1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1beta1",
  "kind": "ExecCredential",
  "status": {
    "token": "my-bearer-token"
  }
}
```
{{% /tab %}}
{{< /tabs >}}

همچنین می‌توان یک گواهی کلاینت و کلید با قالب PEM را برای استفاده از احراز هویت کلاینت TLS بازگرداند.
اگر افزونه در فراخوانی بعدی گواهی و کلید متفاوتی بازگرداند، `k8s.io/client-go`
اتصال‌های موجود با سرور را می‌بندد تا یک TLS handshake جدید را اجبار کند.

در صورت مشخص شدن، هر دو مقدار `clientKeyData` و `clientCertificateData` باید حاضر باشند.

`clientCertificateData` می‌تواند شامل گواهی‌های میانی اضافی برای ارسال به سرور باشد.

{{< tabs name="exec_plugin_ExecCredential_example_2" >}}
{{% tab name="client.authentication.k8s.io/v1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1",
  "kind": "ExecCredential",
  "status": {
    "clientCertificateData": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
    "clientKeyData": "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----"
  }
}
```
{{% /tab %}}
{{% tab name="client.authentication.k8s.io/v1beta1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1beta1",
  "kind": "ExecCredential",
  "status": {
    "clientCertificateData": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
    "clientKeyData": "-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----"
  }
}
```
{{% /tab %}}
{{< /tabs >}}

به‌صورت اختیاری، پاسخ می‌تواند شامل زمان انقضای اعتبارنامه باشد که به‌صورت یک مهر زمانی
[RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) قالب‌بندی می‌شود.

وجود یا عدم وجود زمان انقضا تأثیرات زیر را دارد:

- اگر زمان انقضا درج شده باشد، توکن حامل و اعتبارنامه‌های TLS تا رسیدن به زمان انقضا،
  یا تا زمانی که سرور با کد وضعیت HTTP برابر با 401 پاسخ دهد، یا تا زمان خروج فرایند، در حافظه نهان نگهداری می‌شوند.
- اگر زمان انقضا درج نشده باشد، توکن حامل و اعتبارنامه‌های TLS تا زمانی که
  سرور با کد وضعیت HTTP برابر با 401 پاسخ دهد یا تا زمان خروج فرایند، در حافظه نهان نگهداری می‌شوند.

{{< tabs name="exec_plugin_ExecCredential_example_3" >}}
{{% tab name="client.authentication.k8s.io/v1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1",
  "kind": "ExecCredential",
  "status": {
    "token": "my-bearer-token",
    "expirationTimestamp": "2018-03-05T17:30:20-08:00"
  }
}
```
{{% /tab %}}
{{% tab name="client.authentication.k8s.io/v1beta1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1beta1",
  "kind": "ExecCredential",
  "status": {
    "token": "my-bearer-token",
    "expirationTimestamp": "2018-03-05T17:30:20-08:00"
  }
}
```
{{% /tab %}}
{{< /tabs >}}

برای اینکه افزونه exec بتواند اطلاعات مختص کلاستر را به دست آورد، مقدار `provideClusterInfo` را در فیلد `user.exec`
در [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) تنظیم کنید.
در این صورت، این اطلاعات مختص کلاستر در متغیر محیطی `KUBERNETES_EXEC_INFO` در اختیار افزونه قرار می‌گیرد.
اطلاعات این متغیر محیطی را می‌توان برای اجرای منطق دریافت اعتبارنامه مختص کلاستر به کار برد.
مانیفست `ExecCredential` زیر نمونه‌ای از اطلاعات کلاستر را توصیف می‌کند.

{{< tabs name="exec_plugin_ExecCredential_example_4" >}}
{{% tab name="client.authentication.k8s.io/v1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1",
  "kind": "ExecCredential",
  "spec": {
    "cluster": {
      "server": "https://172.17.4.100:6443",
      "certificate-authority-data": "LS0t...",
      "config": {
        "arbitrary": "config",
        "this": "can be provided via the KUBERNETES_EXEC_INFO environment variable upon setting provideClusterInfo",
        "you": ["can", "put", "anything", "here"]
      }
    },
    "interactive": true
  }
}
```
{{% /tab %}}
{{% tab name="client.authentication.k8s.io/v1beta1" %}}
```json
{
  "apiVersion": "client.authentication.k8s.io/v1beta1",
  "kind": "ExecCredential",
  "spec": {
    "cluster": {
      "server": "https://172.17.4.100:6443",
      "certificate-authority-data": "LS0t...",
      "config": {
        "arbitrary": "config",
        "this": "can be provided via the KUBERNETES_EXEC_INFO environment variable upon setting provideClusterInfo",
        "you": ["can", "put", "anything", "here"]
      }
    },
    "interactive": true
  }
}
```
{{% /tab %}}
{{< /tabs >}}

## دسترسی API به اطلاعات احراز هویت یک کلاینت {#self-subject-review}

{{< feature-state for_k8s_version="v1.28" state="stable" >}}

می‌توانید از API به نام SelfSubjectReview استفاده کنید تا دریابید
کلاستر کوبرنتیز شما چگونه اطلاعات احراز هویت شما را به‌عنوان یک کلاینت شناسایی و نگاشت می‌کند.
این امر چه زمانی که به‌عنوان کاربر (که معمولاً نمایانگر
یک شخص واقعی است) احراز هویت می‌شوید و چه زمانی که به‌عنوان ServiceAccount احراز هویت می‌شوید، کار می‌کند.

در یک کلاستر معمول کوبرنتیز، همه کاربران احراز هویت‌شده می‌توانند SelfSubjectReview ایجاد کنند.
دسترسی به این کار توسط
[ClusterRole](/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) توکار `system:basic-user` مجاز شده است.

توانایی یک کلاینت برای آگاهی از هویت خود، هنگام عیب‌یابی یک جریان احراز هویت پیچیده که در یک کلاستر کوبرنتیز به کار رفته است، بسیار مفید است؛
برای مثال، اگر از [احراز هویت توکن با webhook](/docs/reference/access-authn-authz/authentication/#webhook-token-authentication)
یا یک [پروکسی احراز هویت](/docs/reference/access-authn-authz/authentication/#authenticating-proxy) استفاده می‌کنید.

اگر می‌خواهید این اطلاعات را در خط فرمان پرس‌وجو کنید، به
[دسترسی CLI به اطلاعات احراز هویت](#self-subject-review-cli) مراجعه کنید.

### دسترسی HTTP به اطلاعات احراز هویت {#self-subject-review-http-api}

SelfSubjectReview هیچ فیلد قابل پیکربندی ندارد. هنگام دریافت یک درخواست، API server کوبرنتیز
فیلد status را با ویژگی‌های کاربر پر می‌کند و آن را به کاربر بازمی‌گرداند.
این کار یک منبع نام‌دار را در کلاستر شما **ذخیره نمی‌کند**: نمی‌توانید
SelfSubjectReview را بازیابی کنید و پس از تکمیل درخواست `POST` شما، دور ریخته می‌شود.

نمونه درخواست (بدنه درخواست یک SelfSubjectReview خواهد بود):

```http
POST /apis/authentication.k8s.io/v1/selfsubjectreviews
```

```json
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview"
}
```

نمونه پاسخ:

```json
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview",
  "status": {
    "userInfo": {
      "username": "janedoe@example.com",
      "groups": [
        "viewers",
        "editors",
        "system:authenticated"
      ]
    }
  }
}
```


{{< note >}}
API server کوبرنتیز فیلد `userInfo` را پس از اعمال همه سازوکارهای احراز هویت پر می‌کند،
از جمله [جعل هویت (impersonation)](/docs/reference/access-authn-authz/authentication/#user-impersonation).
اگر شما یا یک پروکسی احراز هویت با استفاده از جعل هویت یک SelfSubjectReview ایجاد کنید،
جزئیات و ویژگی‌های کاربری را مشاهده می‌کنید که هویت او جعل شده است.
{{< /note >}}

این پاسخ نمونه همه فیلدهای موجود را نشان نداد؛ همه سازوکارهای
احراز هویت تمام فیلدهای موجود را پر نمی‌کنند.
برای مشاهده فیلدهای موجود، به [مرجع API مربوط به SelfSubjectReview](/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/)
مراجعه کنید.

در اینجا مثال دیگری آمده است که فیلدهای `uid` و `extra` را نیز شامل می‌شود:

<!-- YAML highlighting intentional; JSON is valid YAML -->
```yaml
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview",
  "status": {
    "userInfo": {
      "username": "janedoe@example.com",
      "groups": [
        "viewers",
        "editors",
        "system:authenticated"
      ],
      "uid": "000042",
      "extra": {
        "firstName": [
          "Jane"
        ],
        "familyName": [
          "Doe"
        ],
        "projectAssignments": [
          "web-frontend",
          "ai-training-proof-of-concept"
        ],
      }
    }
  }
}
```

داده‌های این فیلدهای اختیاری از یکپارچه‌سازی احراز هویت شما
یا از پایگاه داده کاربری که آن استفاده می‌کند می‌آیند. نام کاربری،
UID، اطلاعات اضافی (extra) و همه گروه‌هایی که نامشان با
`system:` شروع نمی‌شود، همگی از خارج از کوبرنتیز تأمین می‌شوند.


هنگام پرس‌وجو از API کوبرنتیز از طریق HTTP، می‌توانید با استفاده از هدر HTTP به نام `Accept:` پاسخ را
در قالب JSON یا YAML درخواست کنید؛ برای مثال:

{{< tabs name="self_subject_attributes_review_Example_1" >}}
{{% tab name="JSON" %}}
```http
POST /apis/authentication.k8s.io/v1/selfsubjectreviews HTTP/1.1
Accept: application/json;q=1.0
Content-Type: application/json
…other request headers

{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview"
}

```

---

```json
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview",
  "status": {
    "userInfo": {
      "username": "jane.doe",
      "uid": "b79dbf30-0c6a-11ed-861d-0242ac120002",
      "groups": [
        "students",
        "teachers",
        "system:authenticated"
      ],
      "extra": {
        "skills": [
          "reading",
          "learning"
        ],
        "subjects": [
          "math",
          "sports"
        ]
      }
    }
  }
}
```
{{% /tab %}}

{{% tab name="YAML" %}}
```http
POST /apis/authentication.k8s.io/v1/selfsubjectreviews HTTP/1.1
Accept: application/yaml;q=1.0
Content-Type: application/json
…other request headers

{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview"
}

```

---

```yaml
apiVersion: authentication.k8s.io/v1
kind: SelfSubjectReview
status:
  userInfo:
    username: jane.doe
    uid: b79dbf30-0c6a-11ed-861d-0242ac120002
    groups:
    - students
    - teachers
    - system:authenticated
    extra:
      skills:
      - reading
      - learning
      subjects:
      - math
      - sports
```
{{% /tab %}}
{{< /tabs >}}

### دسترسی CLI به اطلاعات احراز هویت {#self-subject-review-cli}

برای سهولت، زیردستور `kubectl auth whoami` نیز در دسترس است:
```shell
kubectl auth whoami
```

خروجی مشابه زیر است:
```console
  ATTRIBUTE         VALUE
  Username          george.boole
  Groups            [system:authenticated]
```

برای جزئیات بیشتر، به [`kubectl auth whoami`](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/)
مراجعه کنید.


## {{% heading "whatsnext" %}}

* برای آشنایی با صدور گواهی برای کاربران، [صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/) را بخوانید
* [مرجع احراز هویت کلاینت (v1)](/docs/reference/config-api/client-authentication.v1/) را بخوانید
* [مرجع احراز هویت کلاینت (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/) را بخوانید
