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
این صفحه مروری بر احراز هویت (authentication) در کوبرنتیز ارائه می‌دهد و تمرکز آن بر احراز هویت در [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) است.

<!-- body -->
## کاربران در کوبرنتیز

همه‌ی کلاسترهای کوبرنتیز دو دسته کاربر دارند: حساب‌های سرویس (service account) که کوبرنتیز آن‌ها را مدیریت می‌کند، و کاربران عادی.

فرض بر این است که یک سرویس مستقل از کلاستر، کاربران عادی را به یکی از روش‌های زیر مدیریت می‌کند:

- مدیری که کلیدهای خصوصی را توزیع می‌کند
- یک مخزن کاربران مانند Keystone یا Google Accounts
- فایلی شامل فهرستی از نام‌های کاربری و گذرواژه‌ها

از این نظر، _کوبرنتیز هیچ آبجکتی برای نمایش حساب‌های کاربران عادی ندارد._
نمی‌توان کاربران عادی را با یک فراخوانی API به کلاستر اضافه کرد.

با اینکه نمی‌توان کاربر عادی را از طریق فراخوانی API اضافه کرد، هر کاربری که گواهی معتبری ارائه دهد که مرجع صدور گواهی (CA) کلاستر آن را امضا کرده باشد، احرازهویت‌شده به شمار می‌آید. در این پیکربندی، کوبرنتیز نام کاربری را از فیلد common name در بخش «subject» گواهی (برای مثال، "/CN=bob") تعیین می‌کند. پس از آن، زیرسیستم کنترل دسترسی مبتنی بر نقش (RBAC) تعیین می‌کند که آیا کاربر مجاز به انجام عملیاتی مشخص روی یک منبع هست یا نه.

در مقابل، حساب‌های سرویس کاربرانی هستند که API کوبرنتیز آن‌ها را مدیریت می‌کند. این حساب‌ها به فضاهای نام مشخصی وابسته‌اند و API server آن‌ها را به‌طور خودکار ایجاد می‌کند یا می‌توان آن‌ها را به‌صورت دستی و از طریق فراخوانی‌های API ایجاد کرد. حساب‌های سرویس به مجموعه‌ای از اعتبارنامه‌ها گره خورده‌اند که به‌صورت `Secrets` ذخیره می‌شوند. این اعتبارنامه‌ها در پادها mount می‌شوند تا فرایندهای درون کلاستر بتوانند با API کوبرنتیز ارتباط برقرار کنند.

هر درخواست API یا به یک کاربر عادی وابسته است، یا به یک حساب سرویس، یا به‌عنوان [درخواست ناشناس](#anonymous-requests) در نظر گرفته می‌شود. یعنی هر فرایندی در داخل یا خارج از کلاستر، از کاربر انسانی‌ای که روی ایستگاه کاری خود `kubectl` را اجرا می‌کند گرفته تا `kubelets` روی نودها و اعضای control plane، هنگام ارسال درخواست به API server باید احراز هویت شود؛ در غیر این صورت با آن مانند یک کاربر ناشناس رفتار می‌شود.

اگر برای احراز هویت تلاش کنید و موفق شوید، API server به‌طور خودکار شما را عضو گروه ویژه‌ی `system:authenticated` علامت‌گذاری می‌کند.

## راهبردهای احراز هویت

کوبرنتیز برای احراز هویت درخواست‌های API از طریق افزونه‌های احراز هویت، از گواهی‌های کلاینت، توکن‌های حامل (bearer token) یا یک پراکسی احراز هویت استفاده می‌کند. هنگامی که درخواست‌های HTTP به API server فرستاده می‌شوند، افزونه‌ها تلاش می‌کنند ویژگی‌های زیر را به درخواست نسبت دهند:

* نام کاربری (Username): رشته‌ای که کاربر نهایی را شناسایی می‌کند. مقادیر رایج می‌توانند `kube-admin` یا `jane@example.com` باشند.
* شناسه‌ی کاربر (UID): رشته‌ای که کاربر نهایی را شناسایی می‌کند و تلاش می‌کند از نام کاربری پایدارتر و یکتاتر باشد.
* گروه‌ها (Groups): مجموعه‌ای از رشته‌ها که هر کدام عضویت کاربر را در یک مجموعه‌ی منطقیِ نام‌دار از کاربران نشان می‌دهد.
  مقادیر رایج می‌توانند `system:masters` یا `devops-team` باشند.
* فیلدهای اضافی (Extra fields): نگاشتی از رشته‌ها به فهرست‌هایی از رشته‌ها که اطلاعات تکمیلی‌ای را نگه می‌دارد که ممکن است برای مجوزدهنده‌ها مفید باشد.

{{< note >}}
همه‌ی این مقادیر برای سیستم احراز هویت مبهم (opaque) هستند و فقط زمانی معنا پیدا می‌کنند که یک [مجوزدهنده](/docs/reference/access-authn-authz/authorization/) آن‌ها را تفسیر کند.
{{< /note >}}

## درخواست‌های ناشناس

اگر این قابلیت فعال باشد، درخواست‌هایی که سایر روش‌های احراز هویتِ پیکربندی‌شده آن‌ها را رد نکنند، به‌عنوان درخواست ناشناس در نظر گرفته می‌شوند و نام کاربری `system:anonymous` و گروه `system:unauthenticated` به آن‌ها داده می‌شود.

برای مثال، در سروری که احراز هویت با توکن در آن پیکربندی شده و دسترسی ناشناس نیز فعال است، درخواستی که توکن حامل نامعتبری ارائه کند خطای `401 Unauthorized` دریافت می‌کند، اما با درخواستی که هیچ توکن حاملی ارائه نکند مانند یک درخواست ناشناس رفتار می‌شود.

اگر از [حالت مجوزدهی](/docs/reference/access-authn-authz/authorization/#authorization-modules)ی غیر از `AlwaysAllow` استفاده شود، دسترسی ناشناس به‌طور پیش‌فرض فعال است؛ می‌توانید با ارسال گزینه‌ی خط فرمان `--anonymous-auth=false` به API server آن را غیرفعال کنید.
مجوزدهنده‌های داخلی ABAC و RBAC نیازمند مجوزدهی صریح به کاربر `system:anonymous` یا گروه `system:unauthenticated` هستند؛ اگر قواعد سیاست قدیمی (مربوط به کوبرنتیز نسخه‌ی ۱.۵ یا پیش از آن) دارید، آن دسته از قواعد قدیمی که به کاربر `*` یا گروه `*` دسترسی می‌دهند، به‌طور خودکار به کاربران ناشناس اجازه‌ی دسترسی نمی‌دهند.

### پیکربندی احرازکننده‌ی ناشناس

{{< feature-state feature_gate_name="AnonymousAuthConfigurableEndpoints" >}}

برای پیکربندی احرازکننده‌ی ناشناس می‌توان از `AuthenticationConfiguration` استفاده کرد. اگر فیلد anonymous را در فایل `AuthenticationConfiguration` تنظیم کنید، دیگر نمی‌توانید گزینه‌ی خط فرمان `--anonymous-auth` را تنظیم کنید.

مزیت اصلی پیکربندی احرازکننده‌ی ناشناس با فایل پیکربندی احراز هویت این است که افزون بر فعال و غیرفعال کردن احراز هویت ناشناس، می‌توانید تعیین کنید کدام endpointها از احراز هویت ناشناس پشتیبانی کنند.

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

در پیکربندی بالا، فقط endpointهای `/livez`، `/readyz` و `/healthz` برای درخواست‌های ناشناس در دسترس هستند. هیچ endpoint دیگری به‌صورت ناشناس در دسترس نخواهد بود، حتی اگر پیکربندی مجوزدهی شما اجازه‌ی آن را بدهد.

## روش‌های احراز هویت

می‌توانید چند روش احراز هویت را هم‌زمان فعال کنید. معمولاً باید دست‌کم از دو روش استفاده کنید:

- [توکن‌های حساب سرویس](/docs/concepts/security/service-accounts/#authenticating-credentials) برای ServiceAccountها
- دست‌کم یک روش دیگر برای احراز هویت کاربران (عادی)

روش‌های احراز هویت موجود عبارت‌اند از:

* [گواهی‌های کلاینت X.509](#x509-client-certificates)
* [توکن‌های راه‌اندازی](#bootstrap-tokens)
* [توکن‌های حساب سرویس](#service-account-tokens)
* [فایل توکن ایستا](#static-token-file)
* [یکپارچه‌سازی‌های خارجی](#external-integrations)
  * [توکن‌های وب JSON](#json-web-token-authentication)
  * [توکن‌های OpenID Connect](#openid-connect-tokens)
  * [احراز هویت با توکن از طریق Webhook](#webhook-token-authentication)
  * [پراکسی معکوسِ احراز هویت](#authenticating-proxy)

هنگامی که چند ماژول احرازکننده فعال باشد، نخستین ماژولی که درخواست را با موفقیت احراز هویت کند، ارزیابی را متوقف می‌کند و بقیه بررسی نمی‌شوند.
API server هیچ تضمینی درباره‌ی ترتیب اجرای احرازکننده‌ها نمی‌دهد.

### گواهی‌های کلاینت X.509 {#x509-client-certificates}

هر کلاینت کوبرنتیز که گواهی کلاینت معتبری ارائه دهد که مرجع صدور گواهیِ _اعتماد کلاینت_ (client trust CA) کلاستر آن را امضا کرده باشد، احرازهویت‌شده به شمار می‌آید. در این پیکربندی، کوبرنتیز نام کاربری را از فیلد `commonName` در بخش _subject_ گواهی تعیین می‌کند (برای مثال، `commonName=bob` نشان‌دهنده‌ی کاربری با نام کاربری "bob" است).
پس از آن، سازوکارهای [مجوزدهی](/docs/reference/access-authn-authz/authorization) کوبرنتیز تعیین می‌کنند که آیا کاربر مجاز به انجام عملیاتی مشخص روی یک منبع هست یا نه.

احراز هویت با گواهی کلاینت با ارسال گزینه‌ی `--client-ca-file=<SOMEFILE>` به API server فعال می‌شود.
این گزینه مرجع صدور گواهیِ _اعتماد کلاینت_ کلاستر را پیکربندی می‌کند.
فایلِ مشخص‌شده باید شامل یک یا چند مرجع صدور گواهی باشد که API server بتواند هنگام اعتبارسنجی گواهی‌های کلاینت از آن‌ها استفاده کند.
اگر یک گواهی کلاینت ارائه و تأیید شود، common name موجود در subject به‌عنوان نام کاربری درخواست استفاده می‌شود. گواهی‌های کلاینت همچنین می‌توانند عضویت کاربر در گروه‌ها را از طریق فیلدهای organization گواهی مشخص کنند. برای اینکه کاربر عضو چند گروه باشد، چند فیلد organization در گواهی قرار دهید.

برای آشنایی با نحوه‌ی تولید گواهی کلاینت، به [مدیریت گواهی‌ها](/docs/tasks/administer-cluster/certificates/) مراجعه کنید یا [مثال](#x509-client-certificates-example) کوتاهی را که در ادامه‌ی همین صفحه آمده است بخوانید.

#### گواهی‌های کلاینت سازگار با کوبرنتیز {#x509-client-certificates-k8s}

می‌توانید گواهی معتبری را که یک CA در زنجیره‌ی اعتمادِ موردپذیرش API server برای گواهی‌های کلاینت صادر کرده است ارائه دهید و از آن برای احراز هویت در کوبرنتیز استفاده کنید.
گواهی باید معتبر باشد؛ API server این موضوع را بر اساس ویژگی‌های `notBefore` و `notAfter` استاندارد X.509 بررسی می‌کند. همچنین گواهی باید دارای _کاربرد کلید توسعه‌یافته_ (extended key usage) باشد که احراز هویت کلاینت (`ClientAuth`) را شامل شود.

{{< note >}}
کوبرنتیز {{< skew currentVersion >}} از _ابطال_ (revocation) گواهی پشتیبانی نمی‌کند.
هر گواهی‌ای که صادر شود تا زمان انقضا معتبر باقی می‌ماند.
{{< /note >}}

##### نگاشت نام کاربری {#x509-client-certificates-k8s-username}

کوبرنتیز انتظار دارد گواهی کلاینت دارای ویژگی `commonName` (با OID `2.5.4.3`) باشد که به‌عنوان نام کاربری subject استفاده می‌شود.

##### نگاشت شناسه‌ی کاربر

{{< feature-state feature_gate_name="AllowParsingUserUIDFromCertAuth" >}}

برای استفاده از این قابلیت، گواهی باید ویژگی `1.3.6.1.4.1.57683.2` را داشته باشد و [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `AllowParsingUserUIDFromCertAuth` نیز باید فعال باشد (این feature gate به‌طور پیش‌فرض فعال است).

کوبرنتیز می‌تواند یک UID **اختیاری** برای کاربر را از گواهی استخراج کند.
UID با نام کاربری متفاوت است؛ مقداری مبهم است که معنای آن را درخواست‌دهنده‌ی گواهی، یا کسی که قواعد تأیید گواهی را تنظیم کرده است، تعیین می‌کند.

برای مثال، UID ممکن است در یک کلاستر `1042` (یک عدد صحیح ساده) باشد، اما گواهی دیگری ممکن است از `d3f77937-ec82-4f16-8010-61821abe315a` (یک UUID) به‌عنوان UID استفاده کند.

مثالی برای توضیح این موضوع: فرض کنید گواهی‌ای دارید که common name آن "Ada Lovelace" است و ویژگی `uid` (با OID `0.9.2342.19200300.100.1.1`) نیز با مقدار "aaking1815" در آن تنظیم شده است. در این حالت کوبرنتیز نام کاربری کلاینت را "Ada Lovelace" در نظر می‌گیرد و ویژگی `uid` را نادیده می‌گیرد، زیرا این ویژگی همان OID مختص CNCF که کوبرنتیز به دنبال آن است نیست.
اگر می‌خواهید کوبرنتیز مقدار `aaking1815` را به‌عنوان UID بشناسد، این مقدار باید به‌عنوان مقدار ویژگی OID `1.3.6.1.4.1.57683.2` در subject گواهی تنظیم شود.

##### نگاشت گروه {#x509-client-certificates-k8s-group}

می‌توانید با قرار دادن ایستای اطلاعات گروه در گواهی، کاربر را به گروه‌ها نگاشت کنید. برای هر گروهی که کاربر عضو آن است، نام گروه را به‌عنوان یک `organization` (با OID `2.5.6.4`) در subject گواهی خود اضافه کنید.
برای اینکه کاربر عضو چند گروه باشد، چند organization در subject گواهی قرار دهید (ترتیب آن‌ها اهمیتی ندارد).
برای کاربر نمونه، distinguished name گواهی می‌تواند CN=Ada&nbsp;Lovelace,O=Users,O=Staff,O=Programmers باشد که او را در گروه‌های "Programmers"، "Staff"، "system:authenticated" و "Users" قرار می‌دهد.

قرار دادن اطلاعات گروه در گواهی اختیاری است؛ اگر هیچ گروهی در گواهی مشخص نکنید، کاربر فقط عضو "system:authenticated" خواهد بود.

##### گواهی‌های کلاینت نودها {#x509-client-certificates-nodes}

کوبرنتیز می‌تواند همین رویکرد را برای هویت نودها نیز به کار ببرد؛ نودها کلاینت‌هایی از API server کوبرنتیز هستند که یک {{<glossary_tooltip term_id="kubelet" text="kubelet">}} را اجرا می‌کنند (همچنین، هرچند در اینجا اهمیت کمتری دارد، API server معمولاً خودش نیز کلاینتِ هر نود است).
برای مثال، نودی با نام "server-1a-antarctica42" و نام دامنه‌ی "server-1a-antarctica42.cluster.example" می‌تواند از گواهی‌ای استفاده کند که برای "CN=system:node:server-1a-antarctica/42,O=system:nodes" صادر شده است. در این صورت نام کاربری نود "system:node:server-1a-antarctica/g42" خواهد بود و نود عضو گروه‌های "system:authenticated" و "system:nodes" است.

kubelet برای احراز هویت در API server کلاستر از گواهی و کلید خصوصی نود استفاده می‌کند.

{{< note >}}
هویت‌های ماشینی نودها با {{< glossary_tooltip text="ServiceAccountها" term_id="service-account" >}} یکسان نیستند.
{{< /note >}}

#### مثال {#x509-client-certificates-example}

می‌توانید با ابزار خط فرمان `openssl` یک درخواست امضای گواهی (CSR) تولید کنید:

```bash
# This example assumes that you already have a private key alovelace.pem
openssl req -new -key alovelace.pem -out alovelace-csr.pem -subj "/CN=alovelace/O=app1/O=app2"
```

این دستور یک درخواست امضا برای نام کاربری "alovelace" ایجاد می‌کند که به دو گروه "app1" و "app2" تعلق دارد. سپس می‌توانید این درخواست امضا را به مرجع صدور گواهیِ اعتماد کلاینتِ کلاستر خود بدهید تا آن را امضا کند و گواهی‌ای به دست آورید که بتوانید از آن برای احراز هویت کلاینت در کلاستر استفاده کنید.

### توکن‌های راه‌اندازی

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

برای ساده‌سازی راه‌اندازی (bootstrapping) کلاسترهای جدید، کوبرنتیز نوعی توکن حامل با مدیریت پویا به نام *توکن راه‌اندازی* (Bootstrap Token) دارد. این توکن‌ها به‌صورت Secret در فضای نام `kube-system` ذخیره می‌شوند و در آنجا می‌توان آن‌ها را به‌صورت پویا مدیریت و ایجاد کرد. Controller Manager شامل کنترل‌کننده‌ای به نام TokenCleaner است که توکن‌های راه‌اندازی را پس از انقضا حذف می‌کند.

این توکن‌ها به شکل `[a-z0-9]{6}.[a-z0-9]{16}` هستند. بخش نخست، شناسه‌ی توکن (Token ID) و بخش دوم، رمز توکن (Token Secret) است. توکن را به این صورت در یک سرآیند HTTP مشخص می‌کنید:

```http
Authorization: Bearer 781292.db7bc3a58fc5f07e
```

باید احرازکننده‌ی توکن راه‌اندازی را با فلگ `--enable-bootstrap-token-auth` روی API Server فعال کنید. همچنین باید کنترل‌کننده‌ی TokenCleaner را از طریق آرگومان خط فرمان `--controllers` برای kube-controller-manager فعال کنید.
این کار با مقداری مانند `--controllers=*,tokencleaner` انجام می‌شود.
اگر از ابزار `kubeadm` برای راه‌اندازی کلاستر استفاده کنید، این کار را برای شما انجام می‌دهد.

این احرازکننده، درخواست را با هویت `system:bootstrap:<Token ID>` احراز می‌کند. این هویت در گروه `system:bootstrappers` قرار می‌گیرد. نام‌گذاری و گروه‌ها عمداً محدود شده‌اند تا کاربران از به‌کارگیری این توکن‌ها پس از مرحله‌ی راه‌اندازی منصرف شوند. از این نام‌های کاربری و گروه می‌توان برای تدوین سیاست‌های مجوزدهی مناسب جهت پشتیبانی از راه‌اندازی کلاستر استفاده کرد (و `kubeadm` نیز از آن‌ها استفاده می‌کند).

برای مستندات مفصل درباره‌ی احرازکننده و کنترل‌کننده‌های توکن راه‌اندازی و نیز نحوه‌ی مدیریت این توکن‌ها با `kubeadm`، به [توکن‌های راه‌اندازی](/docs/reference/access-authn-authz/bootstrap-tokens/) مراجعه کنید.

#### قرار دادن توکن حامل در درخواست

هنگام استفاده از احراز هویت با توکن حامل در یک کلاینت HTTP، API server انتظار دارد سرآیند `Authorization` با مقدار `Bearer
<token>` وجود داشته باشد. توکن حامل باید دنباله‌ای از نویسه‌ها باشد که بتوان آن را تنها با امکانات کدگذاری و نقل‌قول (quoting) خود HTTP در مقدار یک سرآیند HTTP قرار داد. برای مثال، اگر توکن حامل `31ada4fd-adec-460c-809a-9e56ceb75269` باشد، در سرآیند HTTP به شکل زیر نمایش داده می‌شود.

```http
Authorization: Bearer 31ada4fd-adec-460c-809a-9e56ceb75269
```


### توکن‌های حساب سرویس

حساب سرویس، احرازکننده‌ای است که به‌طور خودکار فعال است و برای تأیید درخواست‌ها از توکن‌های حاملِ امضاشده استفاده می‌کند. این افزونه دو فلگ اختیاری می‌پذیرد:

* فلگ `--service-account-key-file`: فایلی شامل کلیدهای خصوصی یا عمومی RSA یا ECDSA از نوع x509 با کدگذاری PEM که برای تأیید توکن‌های ServiceAccount به کار می‌رود. فایل مشخص‌شده می‌تواند چند کلید داشته باشد و می‌توان این فلگ را چند بار با فایل‌های مختلف مشخص کرد. اگر مشخص نشود، از --tls-private-key-file استفاده می‌شود.
* فلگ `--service-account-lookup`: اگر فعال باشد، توکن‌هایی که از API حذف شده‌اند باطل می‌شوند.

[ServiceAccountها](/docs/concepts/security/service-accounts/) معمولاً به‌طور خودکار توسط API server ایجاد می‌شوند و از طریق [کنترل‌کننده‌ی پذیرش](/docs/reference/access-authn-authz/admission-controllers/) `ServiceAccount` به پادهایی که در کلاستر اجرا می‌شوند مرتبط می‌شوند.
توکن‌های حامل در مسیرهای شناخته‌شده‌ای در پادها mount می‌شوند و به کلاینت‌های درون کلاستر امکان می‌دهند در API server احراز هویت شوند. می‌توان ServiceAccountها را با فیلد `serviceAccountName` در `spec` یک Pod به‌طور صریح به Podها مرتبط کرد.

{{< note >}}
معمولاً فیلد `serviceAccountName` حذف می‌شود، زیرا این کار به‌طور خودکار انجام می‌شود.
{{< /note >}}

در ادامه مانیفستی (ناقص) برای یک Deployment آمده است که با ServiceAccountی به نام bob-the-bot اجرا می‌شود:

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

توکن‌های حامل حساب سرویس برای استفاده در خارج از کلاستر نیز کاملاً معتبرند و می‌توان از آن‌ها برای ایجاد هویت برای کارهای طولانی‌مدتی که می‌خواهند با API کوبرنتیز ارتباط برقرار کنند استفاده کرد. برای ایجاد دستی یک حساب سرویس، از دستور `kubectl create
serviceaccount (NAME)` استفاده کنید. این دستور یک حساب سرویس در فضای نام فعلی ایجاد می‌کند.

```bash
kubectl create serviceaccount jenkins
```

```none
serviceaccount/jenkins created
```

می‌توانید توکن مرتبط با آن را به‌صورت دستی ایجاد کنید:

```bash
kubectl create token jenkins
```

```none
eyJhbGciOiJSUzI1NiIsImtp...
```

توکن ایجادشده یک [توکن وب JSON](https://www.rfc-editor.org/rfc/rfc7519) (JWT) امضاشده است.

از این JWT امضاشده می‌توان به‌عنوان توکن حامل برای احراز هویت با هویتِ حساب سرویس مربوطه استفاده کرد. برای آشنایی با نحوه‌ی قرار دادن توکن در درخواست، به [بخش بالا](#putting-a-bearer-token-in-a-request) مراجعه کنید. معمولاً این توکن‌ها برای دسترسی درون‌کلاستری به API server در پادها mount می‌شوند، اما از خارج از کلاستر نیز می‌توان از آن‌ها استفاده کرد.

حساب‌های سرویس با نام کاربری `system:serviceaccount:(NAMESPACE):(SERVICEACCOUNT)` احراز هویت می‌شوند و به گروه‌های `system:serviceaccounts` و `system:serviceaccounts:(NAMESPACE)` تخصیص داده می‌شوند.

{{< warning >}}
از آنجا که توکن‌های حساب سرویس می‌توانند در آبجکت‌های API از نوع Secret نیز ذخیره شوند، هر کاربری که دسترسی نوشتن روی Secretها داشته باشد می‌تواند توکن درخواست کند، و هر کاربری که دسترسی خواندن آن Secretها را داشته باشد می‌تواند با هویت آن حساب سرویس احراز هویت شود. هنگام اعطای مجوز به حساب‌های سرویس و اعطای قابلیت خواندن یا نوشتن Secretها، احتیاط کنید.
{{< /warning >}}

## یکپارچه‌سازی‌های خارجی

کوبرنتیز به‌طور بومی از JWT و OpenID Connect (OIDC) پشتیبانی می‌کند. برای اطلاعات بیشتر، [احراز هویت با JSON Web Token](#json-web-token-authentication) را ببینید.

یکپارچه‌سازی با سایر پروتکل‌های احراز هویت (برای مثال LDAP، SAML، Kerberos و طرح‌های جایگزین X.509)
را می‌توان با استفاده از یک [پروکسی احراز هویت](#authenticating-proxy) یا از طریق یکپارچه‌سازی با یک
[وبهوک احراز هویت](#webhook-token-authentication) انجام داد.

همچنین می‌توانید از هر روش سفارشی دیگری که [گواهی‌های کلاینت X.509](#x509-client-certificates) را برای کلاینت‌ها صادر می‌کند استفاده کنید،
به این شرط که API server به گواهی‌های معتبر اعتماد کند.
برای آشنایی با نحوهٔ تولید یک گواهی، بخش [گواهی‌های کلاینت X.509](#x509-client-certificates) را
بخوانید.

اگر برای کلاینت‌ها گواهی صادر می‌کنید، شما (به‌عنوان مدیر پلتفرم ابری) مسئول هستید
اطمینان حاصل کنید که مدت اعتبار گواهی و سایر تصمیم‌های طراحی‌تان سطح امنیت
مناسبی فراهم می‌کنند.

### احراز هویت با JSON Web Token

می‌توانید کوبرنتیز را طوری پیکربندی کنید که کاربران را با توکن‌های سازگار با [JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519) (JWT) احراز هویت کند. کوبرنتیز برای توکن‌های ServiceAccount که خودش صادر می‌کند از سازوکار احراز هویت JWT استفاده می‌کند. شما نیز می‌توانید از همین سازوکار برای یکپارچه‌سازی با سایر منابع هویت بهره بگیرید.

احرازکنندهٔ هویت (authenticator) ابتدا تلاش می‌کند توکن هویت خام (raw ID token) را تجزیه کند و سپس بررسی می‌کند که این توکن را صادرکنندهٔ (issuer) پیکربندی‌شده امضا کرده باشد.
برای توکن‌هایی که خارج از کلاستر صادر شده‌اند، کلید عمومی لازم برای بررسی امضا با استفاده از OIDC discovery از نقطهٔ پایانی عمومی صادرکننده به دست می‌آید.

حداقل محتوای معتبر یک JWT **باید** شامل ادعاهای (claims) زیر باشد:

```javascript
{
  "iss": "https://example.com",   // must match the issuer.url
  "aud": ["my-app"],              // at least one of the entries in issuer.audiences must match the "aud" claim in presented JWTs.
  "exp": 1234567890,              // token expiration as Unix time (the number of seconds elapsed since January 1, 1970 UTC)
  "<username-claim>": "user"      // this is the username claim configured in the claimMappings.username.claim or claimMappings.username.expression
}
```

#### نوع انتخابگر خروجی JWT

{{< feature-state feature_gate_name="StructuredAuthenticationConfigurationEgressSelector" >}}

با فیلد `egressSelectorType` در پیکربندی صادرکنندهٔ JWT می‌توانید مشخص کنید که کدام _انتخابگر خروجی_ (egress selector) برای ارسال تمام ترافیک مرتبط با صادرکننده (discovery، JWKS، ادعاهای توزیع‌شده و غیره) به کار رود.
برای استفاده از این قابلیت باید feature gate با نام `StructuredAuthenticationConfigurationEgressSelector` فعال باشد.

#### توکن‌های OpenID Connect

[OpenID Connect](https://openid.net/connect/) گونه‌ای از OAuth2 است که برخی از ارائه‌دهندگان OAuth2، به‌ویژه Microsoft Entra ID، Salesforce و Google، از آن پشتیبانی می‌کنند.
مهم‌ترین افزونهٔ این پروتکل نسبت به OAuth2، فیلد دیگری به نام [ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) است که همراه با توکن دسترسی (access token) بازگردانده می‌شود.
این توکن یک JSON Web Token (JWT) است که فیلدهای شناخته‌شده‌ای مانند ایمیل کاربر دارد و سرور آن را امضا می‌کند.

احرازکنندهٔ هویت برای شناسایی کاربر، مقدار `id_token` (و نه `access_token`) را از [پاسخ توکن](https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse) در OAuth2 به‌عنوان توکن حامل (bearer token) به کار می‌برد. برای آشنایی با نحوهٔ قرار دادن توکن در درخواست، [بخش بالا](#putting-a-bearer-token-in-a-request) را ببینید.

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

1. به ارائه‌دهندهٔ هویت (identity provider) خود وارد شوید.
1. ارائه‌دهندهٔ هویت یک `access_token`، یک `id_token` و یک `refresh_token` در اختیار شما قرار می‌دهد.
1. هنگام کار با `kubectl`، مقدار `id_token` را با آرگومان خط فرمان `--token` به کار ببرید یا آن را مستقیماً به فایل `kubeconfig` خود اضافه کنید.
1. ابزار `kubectl` مقدار `id_token` شما را در سرآیندی به نام Authorization به سرور API می‌فرستد.
1. سرور API از معتبر بودن امضای JWT اطمینان حاصل می‌کند.
1. بررسی می‌شود که `id_token` منقضی نشده باشد.

   اگر عبارت‌های CEL در `AuthenticationConfiguration` پیکربندی شده باشند، اعتبارسنجی ادعاها و/یا کاربر انجام می‌شود.

1. بررسی می‌شود که کاربر مجوز لازم را داشته باشد.
1. پس از تأیید مجوز، سرور API پاسخی به `kubectl` بازمی‌گرداند.
1. ابزار `kubectl` نتیجه را به کاربر اطلاع می‌دهد.

از آنجا که تمام داده‌های لازم برای تأیید هویت شما در `id_token` وجود دارد، کوبرنتیز نیازی ندارد برای این کار با ارائه‌دهندهٔ هویت تماس بگیرد. در مدلی که همهٔ درخواست‌ها بی‌حالت (stateless) هستند، این روش راه‌حلی بسیار مقیاس‌پذیر برای احراز هویت فراهم می‌کند. با این حال، چند چالش نیز به همراه دارد:

1. کوبرنتیز هیچ «رابط وبی» برای آغاز فرایند احراز هویت ندارد. هیچ مرورگر یا رابطی برای دریافت اطلاعات اعتبارسنجی (credentials) وجود ندارد و به همین دلیل باید ابتدا نزد ارائه‌دهندهٔ هویت خود احراز هویت کنید.
1. امکان ابطال `id_token` وجود ندارد. این توکن مانند یک گواهی است، بنابراین باید عمر کوتاهی (فقط چند دقیقه) داشته باشد و همین موضوع ممکن است دریافت توکن جدید در هر چند دقیقه را بسیار آزاردهنده کند.
1. برای احراز هویت در داشبورد کوبرنتیز، باید از فرمان `kubectl proxy` یا یک پراکسی معکوس (reverse proxy) استفاده کنید که `id_token` را به درخواست‌ها تزریق کند.

#### پیکربندی سرور API

##### استفاده از آرگومان‌های خط فرمان

برای فعال کردن این افزونه، آرگومان‌های خط فرمان زیر را برای سرور API پیکربندی کنید:

| پارامتر | توضیح | مثال | الزامی |
| --------- | ----------- | ------- | ------- |
| `--oidc-issuer-url` | نشانی URL ارائه‌دهنده‌ای که سرور API از طریق آن کلیدهای عمومی امضا را کشف می‌کند. فقط نشانی‌هایی پذیرفته می‌شوند که از طرح `https://` استفاده کنند. این مقدار معمولاً همان نشانی discovery ارائه‌دهنده است که مسیر آن خالی شده باشد. | اگر نشانی OIDC discovery صادرکننده `https://accounts.provider.example/.well-known/openid-configuration` باشد، مقدار باید `https://accounts.provider.example` باشد. | بله |
| `--oidc-client-id` | شناسهٔ کلاینتی که همهٔ توکن‌ها باید برای آن صادر شده باشند. | kubernetes | بله |
| `--oidc-username-claim` | ادعای JWT که به‌عنوان نام کاربری استفاده می‌شود. مقدار پیش‌فرض `sub` است که انتظار می‌رود شناسهٔ یکتای کاربر نهایی باشد. مدیران بسته به ارائه‌دهندهٔ خود می‌توانند ادعاهای دیگری مانند `email` یا `name` را انتخاب کنند. با این حال، به ادعاهایی غیر از `email` پیشوندی برابر با نشانی صادرکننده افزوده می‌شود تا از تداخل نام‌ها با سایر افزونه‌ها جلوگیری شود. | sub | خیر |
| `--oidc-username-prefix` | پیشوندی که به ابتدای ادعاهای نام کاربری افزوده می‌شود تا از تداخل با نام‌های موجود (مانند کاربران `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های کاربری‌ای مانند `oidc:jane.doe` ایجاد می‌کند. اگر این آرگومان تعیین نشود و مقدار `--oidc-username-claim` چیزی غیر از `email` باشد، پیشوند به‌طور پیش‌فرض `( Issuer URL )#` خواهد بود که در آن `( Issuer URL )` مقدار `--oidc-issuer-url` است. با مقدار `-` می‌توان افزودن هرگونه پیشوند را غیرفعال کرد. | `oidc:` | خیر |
| `--oidc-groups-claim` | ادعای JWT که به‌عنوان گروه کاربر استفاده می‌شود. اگر این ادعا وجود داشته باشد، باید آرایه‌ای از رشته‌ها باشد. | groups | خیر |
| `--oidc-groups-prefix` | پیشوندی که به ابتدای ادعاهای گروه افزوده می‌شود تا از تداخل با نام‌های موجود (مانند گروه‌های `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های گروهی مانند `oidc:engineering` و `oidc:infra` ایجاد می‌کند. | `oidc:` | خیر |
| `--oidc-required-claim` | یک جفت key=value که ادعای الزامی در ID Token را توصیف می‌کند. در صورت تعیین، بررسی می‌شود که این ادعا با مقدار منطبق در ID Token وجود داشته باشد. برای تعیین چند ادعا، این آرگومان را تکرار کنید. | `claim=value` | خیر |
| `--oidc-ca-file` | مسیر گواهی مرجع صدور گواهی (CA) که گواهی وب ارائه‌دهندهٔ هویت شما را امضا کرده است. مقدار پیش‌فرض، CAهای ریشهٔ میزبان است. | `/etc/kubernetes/ssl/kc-ca.pem` | خیر |
| `--oidc-signing-algs` | الگوریتم‌های امضای پذیرفته‌شده. مقدار پیش‌فرض RS256 است. مقادیر مجاز عبارت‌اند از: RS256، RS384، RS512، ES256، ES384، ES512، PS256، PS384، PS512. این مقادیر در RFC 7518 به نشانی https://tools.ietf.org/html/rfc7518#section-3.1 تعریف شده‌اند. | `RS512` | خیر |

##### پیکربندی احراز هویت از طریق فایل {#using-authentication-configuration}

{{< feature-state feature_gate_name="StructuredAuthenticationConfiguration" >}}

با روش فایل پیکربندی می‌توانید چندین احرازکنندهٔ هویت JWT را پیکربندی کنید که هر کدام `issuer.url` و `issuer.discoveryURL` یکتای خود را دارند. فایل پیکربندی حتی امکان تعیین عبارت‌های [CEL](/docs/reference/using-api/cel/) را فراهم می‌کند تا ادعاها را به ویژگی‌های کاربر نگاشت کنید و ادعاها و اطلاعات کاربر را اعتبارسنجی کنید.
همچنین هر زمان که فایل پیکربندی تغییر کند، سرور API احرازکننده‌های هویت را به‌طور خودکار دوباره بارگذاری می‌کند.
برای پایش آخرین زمان بارگذاری مجدد پیکربندی در سرور API می‌توانید از متریک `apiserver_authentication_config_controller_automatic_reload_last_timestamp_seconds` استفاده کنید.

باید مسیر فایل پیکربندی احراز هویت را با آرگومان خط فرمان `--authentication-config` به سرور API بدهید. اگر بخواهید به‌جای فایل پیکربندی از آرگومان‌های خط فرمان استفاده کنید، این آرگومان‌ها همچنان مانند گذشته کار می‌کنند. برای دسترسی به قابلیت‌های جدید، مانند پیکربندی چند احرازکنندهٔ هویت یا تعیین چند مخاطب (audience) برای یک صادرکننده، به استفاده از فایل پیکربندی روی بیاورید.

برای استفاده از احراز هویت ساخت‌یافته، آرگومان خط فرمان `--authentication-config` را برای kube-apiserver تعیین کنید. نمونه‌ای از فایل پیکربندی احراز هویت ساخت‌یافته در ادامه آمده است.

{{< note >}}
تعیین هم‌زمان `--authentication-config` با هر یک از آرگومان‌های خط فرمان `--oidc-*` پیکربندی نادرست به شمار می‌رود. در این حالت، سرور API خطا گزارش می‌کند و بلافاصله خارج می‌شود.
اگر می‌خواهید به پیکربندی احراز هویت ساخت‌یافته روی بیاورید، باید آرگومان‌های خط فرمان `--oidc-*` را حذف کنید و به‌جای آن‌ها از فایل پیکربندی استفاده کنید.
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

* عبارت قاعدهٔ اعتبارسنجی ادعا

  فیلد `jwt.claimValidationRules[i].expression` عبارتی را نشان می‌دهد که CEL آن را ارزیابی می‌کند.
  عبارت‌های CEL به محتوای بدنهٔ توکن دسترسی دارند که در متغیر CEL با نام `claims` سازمان‌دهی شده است.
  متغیر `claims` نگاشتی از نام ادعاها (به‌صورت رشته) به مقادیر ادعاها (از هر نوعی) است.

* عبارت قاعدهٔ اعتبارسنجی کاربر

  فیلد `jwt.userValidationRules[i].expression` عبارتی را نشان می‌دهد که CEL آن را ارزیابی می‌کند.
  عبارت‌های CEL به محتوای `userInfo` دسترسی دارند که در متغیر CEL با نام `user` سازمان‌دهی شده است.
  برای آشنایی با طرح‌وارهٔ `user`، به مستندات API مربوط به [UserInfo](/docs/reference/generated/kubernetes-api/v{{< skew currentVersion >}}/#userinfo-v1-authentication-k8s-io) مراجعه کنید.

* عبارت نگاشت ادعا

  فیلدهای `jwt.claimMappings.username.expression`، `jwt.claimMappings.groups.expression`، `jwt.claimMappings.uid.expression` و
  `jwt.claimMappings.extra[i].valueExpression` عبارتی را نشان می‌دهند که CEL آن را ارزیابی می‌کند.
  عبارت‌های CEL به محتوای بدنهٔ توکن دسترسی دارند که در متغیر CEL با نام `claims` سازمان‌دهی شده است.
  متغیر `claims` نگاشتی از نام ادعاها (به‌صورت رشته) به مقادیر ادعاها (از هر نوعی) است.

  برای اطلاعات بیشتر، [مستندات CEL](/docs/reference/using-api/cel/) را ببینید.

  در ادامه نمونه‌هایی از `AuthenticationConfiguration` با محتوای توکن‌های مختلف آمده است.

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

  که محتوای (payload) توکن آن به این صورت است:

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

  این توکن با پیکربندی `AuthenticationConfiguration` بالا، آبجکت `UserInfo` زیر را تولید می‌کند و کاربر با موفقیت احراز هویت می‌شود.

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
  {{% tab name="شکست در اعتبارسنجی claim" %}}
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

  که محتوای توکن آن به این صورت است:

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

  احراز هویت این توکن با پیکربندی `AuthenticationConfiguration` بالا ناموفق خواهد بود، زیرا
  مقدار claim با نام `hd` برابر با `example.com` تنظیم نشده است. در این حالت، سرور API خطای `401 Unauthorized` برمی‌گرداند.
  {{% /tab %}}
  {{% tab name="شکست در اعتبارسنجی کاربر" %}}
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

  که محتوای توکن آن به این صورت است:

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

  این توکن با پیکربندی `AuthenticationConfiguration` بالا، آبجکت `UserInfo` زیر را تولید می‌کند:

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

  این آبجکت در اعتبارسنجی کاربر رد می‌شود، زیرا نام کاربری با `system:` آغاز می‌شود.
  در این حالت، سرور API خطای `401 Unauthorized` برمی‌گرداند.
  {{% /tab %}}
  {{< /tabs >}}



##### محدودیت‌ها {#oidc-limitations}

1. ادعاهای توزیع‌شده (distributed claims) از طریق عبارت‌های [CEL](/docs/reference/using-api/cel/) کار نمی‌کنند.

کوبرنتیز هیچ ارائه‌دهندهٔ هویت (Identity Provider) مبتنی بر OpenID Connect ارائه نمی‌کند.
می‌توانید از یک ارائه‌دهندهٔ هویت عمومی و موجود مبتنی بر OpenID Connect استفاده کنید یا ارائه‌دهندهٔ هویت
خودتان را که از پروتکل OpenID Connect پشتیبانی می‌کند اجرا کنید.

ارائه‌دهندهٔ هویت برای کار با کوبرنتیز باید شرایط زیر را داشته باشد:

1. از [OpenID connect discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) پشتیبانی کند.

   کلید عمومی لازم برای بررسی امضا، با استفاده از سازوکار OIDC discovery از نقطهٔ پایانی (endpoint) عمومی صادرکننده به دست می‌آید.
   اگر از فایل پیکربندی احراز هویت استفاده می‌کنید، لازم نیست ارائه‌دهندهٔ هویت نقطهٔ پایانی discovery را به‌صورت عمومی در دسترس قرار دهد.
   می‌توانید نقطهٔ پایانی discovery را در مکانی جدا از صادرکننده (مثلاً به‌صورت محلی در داخل کلاستر) میزبانی کنید و
   مقدار `issuer.discoveryURL` را در فایل پیکربندی مشخص کنید.

1. روی TLS و با رمزهایی (cipher) که منسوخ نشده‌اند اجرا شود.
1. گواهی‌ای داشته باشد که یک CA آن را امضا کرده است (حتی اگر آن CA تجاری نباشد یا خودامضا باشد).

نکته‌ای دربارهٔ شرط شمارهٔ ۳ بالا، یعنی لزوم داشتن گواهی امضاشده توسط CA: اگر ارائه‌دهندهٔ هویت
خودتان را مستقر می‌کنید، گواهی وب‌سرور آن **باید** با گواهی‌ای امضا شده باشد که پرچم `CA` آن
برابر با `TRUE` است، حتی اگر این گواهی خودامضا باشد. علت این است که پیاده‌سازی کلاینت TLS در زبان Go
در رعایت استانداردهای مربوط به اعتبارسنجی گواهی بسیار سخت‌گیر است. اگر CA در دسترس ندارید،
می‌توانید با ابزارهای استاندارد تولید گواهی، یک CA ساده و یک گواهی امضاشده به همراه جفت کلید آن بسازید.

#### استفاده از kubectl

##### گزینهٔ ۱ - احرازکنندهٔ OIDC

گزینهٔ نخست، استفاده از احرازکنندهٔ `oidc` در kubectl است. این احرازکننده مقدار `id_token` را به‌عنوان توکن حامل (bearer token)
در همهٔ درخواست‌ها قرار می‌دهد و پس از منقضی شدن توکن، آن را تازه‌سازی می‌کند. پس از ورود به ارائه‌دهندهٔ هویت خود،
با kubectl مقادیر `id_token`، `refresh_token`، `client_id` و `client_secret` را اضافه کنید تا افزونه پیکربندی شود.

این افزونه از ارائه‌دهندگانی که در پاسخ تازه‌سازی توکن، مقدار `id_token` را برنمی‌گردانند پشتیبانی نمی‌کند
و این ارائه‌دهندگان باید از [گزینهٔ ۲](#option-2-use-the-token-option) (تعیین `--token`) استفاده کنند.

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

برای نمونه، دستور زیر را پس از احراز هویت نزد ارائه‌دهندهٔ هویت خود اجرا کنید:

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

این دستور پیکربندی زیر را تولید می‌کند:

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

پس از منقضی شدن `id_token`، ابزار `kubectl` تلاش می‌کند با استفاده از `refresh_token` و `client_secret`
مقدار `id_token` را تازه‌سازی کند و مقادیر جدید `refresh_token` و `id_token` را در فایل `.kube/config` ذخیره می‌کند.

##### گزینهٔ ۲ - استفاده از آرگومان خط فرمان `--token` {#option-2-use-the-token-option}

با دستور `kubectl` می‌توانید توکن را از طریق آرگومان خط فرمان `--token` ارسال کنید.
مقدار `id_token` را کپی کنید و در این گزینه قرار دهید:

```bash
kubectl --token=eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL21sYi50cmVtb2xvLmxhbjo4MDQzL2F1dGgvaWRwL29pZGMiLCJhdWQiOiJrdWJlcm5ldGVzIiwiZXhwIjoxNDc0NTk2NjY5LCJqdGkiOiI2RDUzNXoxUEpFNjJOR3QxaWVyYm9RIiwiaWF0IjoxNDc0NTk2MzY5LCJuYmYiOjE0NzQ1OTYyNDksInN1YiI6Im13aW5kdSIsInVzZXJfcm9sZSI6WyJ1c2VycyIsIm5ldy1uYW1lc3BhY2Utdmlld2VyIl0sImVtYWlsIjoibXdpbmR1QG5vbW9yZWplZGkuY29tIn0.f2As579n9VNoaKzoF-dOQGmXkFKf1FMyNV0-va_B63jn-_n9LGSCca_6IVMP8pO-Zb4KvRqGyTP0r3HkHxYy5c81AnIh8ijarruczl-TK_yF5akjSTHFZD-0gRzlevBDiH8Q79NAr-ky0P4iIXS8lY9Vnjch5MF74Zx0c3alKJHJUnnpjIACByfF2SCaYzbWFMUNat-K1PaUk5-ujMBG7yYnr95xD-63n8CO8teGUAAEMx6zRjzfhnhbzX-ajwZLGwGUBT4WqjMs70-6a7_8gZmLZb2az1cZynkFRj2BaCkVT3A2RrjeEwZEtGXlMqKJ1_I2ulrOVsYx01_yD35-rw get nodes
```

### احراز هویت توکن با وب‌هوک

در کوبرنتیز، _احراز هویت با وب‌هوک_ (webhook authentication) سازوکاری است که برای تأیید توکن‌های حامل (bearer token) یک فراخوانی HTTP به سرویسی بیرونی انجام می‌دهد.

برای پیکربندی API server از گزینه‌های زیر استفاده می‌شود:

* گزینهٔ `--authentication-token-webhook-config-file` فایل پیکربندی‌ای است که نحوهٔ دسترسی به سرویس وب‌هوک راه‌دور را توصیف می‌کند.
* گزینهٔ `--authentication-token-webhook-cache-ttl` مدت زمان نگهداری تصمیم‌های احراز هویت در حافظهٔ نهان (cache) را تعیین می‌کند. مقدار پیش‌فرض آن دو دقیقه است.
* گزینهٔ `--authentication-token-webhook-version` تعیین می‌کند که برای ارسال و دریافت اطلاعات از وب‌هوک، از آبجکت‌های `TokenReview` نسخهٔ `authentication.k8s.io/v1beta1` استفاده شود یا نسخهٔ `authentication.k8s.io/v1`. مقدار پیش‌فرض آن `v1beta1` است.

فایل پیکربندی از قالب فایل [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) استفاده می‌کند. در این فایل، `clusters` به سرویس راه‌دور و `users` به وب‌هوک API server اشاره دارد. نمونه‌ای از آن در ادامه آمده است:

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

هنگامی که یک کلاینت، همان‌طور که [پیش‌تر](#putting-a-bearer-token-in-a-request) توضیح داده شد، می‌کوشد با یک توکن حامل نزد API server احراز هویت شود، وب‌هوک احراز هویت یک آبجکت `TokenReview` سریال‌شده به JSON را که حاوی توکن است، با درخواست POST به سرویس راه‌دور می‌فرستد.

توجه کنید که آبجکت‌های API وب‌هوک نیز مانند دیگر آبجکت‌های API کوبرنتیز از همان [قواعد سازگاری نسخه‌بندی](/docs/concepts/overview/kubernetes-api/) پیروی می‌کنند. پیاده‌سازان باید فیلد `apiVersion` درخواست را بررسی کنند تا از واسریال‌سازی درست آن مطمئن شوند، و **باید** با یک آبجکت `TokenReview` هم‌نسخه با درخواست پاسخ دهند.

{{< tabs name="TokenReview_request" >}}
{{% tab name="authentication.k8s.io/v1" %}}
{{< note >}}
برای حفظ سازگاری با نسخه‌های پیشین، API server کوبرنتیز به‌طور پیش‌فرض بازبینی‌های توکن را با نسخهٔ `authentication.k8s.io/v1beta1` ارسال می‌کند.
برای دریافت بازبینی‌های توکن با نسخهٔ `authentication.k8s.io/v1`، باید API server را با گزینهٔ `--authentication-token-webhook-version=v1` راه‌اندازی کرد.
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

انتظار می‌رود سرویس راه‌دور فیلد `status` درخواست را پر کند تا موفقیت ورود را نشان دهد.
فیلد `spec` در بدنهٔ پاسخ نادیده گرفته می‌شود و می‌توان آن را حذف کرد.
سرویس راه‌دور باید پاسخ را با همان نسخه‌ای از API `TokenReview` برگرداند که دریافت کرده است.
در صورت اعتبارسنجی موفق توکن حامل، پاسخی مانند زیر برگردانده می‌شود:

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

در صورت ناموفق بودن درخواست، پاسخی مانند زیر برگردانده می‌شود:

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

### پراکسی معکوس احراز هویت‌کننده {#authenticating-proxy}

{{< warning >}}
اگر مرجع صدور گواهی (CA) شما در زمینهٔ دیگری نیز استفاده می‌شود، برای شناسایی کلاینت‌های پراکسی احراز هویت‌کننده به آن مرجع صدور گواهی اعتماد **نکنید**، مگر آنکه خطرها و سازوکارهای محافظت از نحوهٔ استفاده از آن CA را به‌خوبی بشناسید.
{{< /warning >}}

می‌توان API server را طوری پیکربندی کرد که کاربران را از روی مقادیر سرآیندهای درخواست، مانند `X-Remote-User`، شناسایی کند.
این قابلیت برای استفاده همراه با یک _پراکسی احراز هویت‌کننده_ (authenticating proxy) طراحی شده است که این سرآیندها را تنظیم می‌کند.

استفاده از پراکسی معکوس احراز هویت‌کننده با [جعل هویت کاربر](/docs/reference/access-authn-authz/user-impersonation/) (user impersonation) تفاوت دارد.
در جعل هویت کاربر، یک کاربر از API server می‌خواهد که با درخواست چنان رفتار کند که گویی کاربر دیگری آن را فرستاده است. اما در پراکسی معکوس احراز هویت‌کننده، API server به کلاینت مستقیم خود اعتماد می‌کند تا اطلاعات مربوط به هویت موجودیتی را که درخواست اصلی را ارسال کرده است، در اختیارش بگذارد.

برای آشنایی با پیکربندی این قابلیت از طریق آرگومان‌های خط فرمان، به [پیکربندی سرآیندهای درخواست وب](#api-server-authn-config-cli-reverse-proxy) مراجعه کنید.

#### نمونه {#authenticating-proxy-example}

برای نمونه، با این پیکربندی:

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

به اطلاعات کاربری زیر منجر می‌شود:

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

برای جلوگیری از جعل سرآیندها، پراکسی احراز هویت‌کننده باید پیش از بررسی سرآیندهای درخواست، یک گواهی کلاینت معتبر به API server ارائه کند تا در برابر CA مشخص‌شده اعتبارسنجی شود.

برای حالت احراز هویت با سرآیند درخواست، به مرجع [گزینه‌های خط فرمان](#api-server-authn-config-cli-reverse-proxy) مراجعه کنید.

<!-- deliberately repeating the earlier warning -->
از CAای که در زمینهٔ دیگری استفاده می‌شود دوباره استفاده **نکنید**، مگر آنکه خطرها و سازوکارهای محافظت از نحوهٔ استفاده از آن CA را به‌خوبی بشناسید.

### یکپارچه‌سازی با فایل توکن ایستا {#static-token-file}

هنگامی که گزینهٔ `--token-auth-file=<SOMEFILE>` در خط فرمان به API server داده شود، این سرور توکن‌های حامل ایستا را از یک فایل می‌خواند.
در کوبرنتیز {{< skew currentVersion >}}، این توکن‌ها برای همیشه معتبر می‌مانند و فهرست توکن‌ها را نمی‌توان بدون راه‌اندازی دوبارهٔ API server تغییر داد.

فایل توکن یک فایل CSV با دست‌کم ۳ ستون است: توکن، نام کاربری و uid کاربر، که پس از آن‌ها می‌توان فهرستی اختیاری از نام گروه‌ها را به‌صورت جداشده با ویرگول آورد.


{{< note >}}
اگر بیش از یک گروه دارید، آن ستون باید درون گیومهٔ دوتایی قرار گیرد؛ برای نمونه:

```conf
token,user,uid,"group1,group2,group3"
```
{{< /note >}}

استفاده از فایل توکن ایستا برای توکن‌هایی مناسب است که ذاتاً طولانی‌مدت و ایستا هستند و شاید هرگز چرخش (rotation) نیابند. این روش همچنین زمانی سودمند است که کلاینت، مانند یک عامل پایش، به‌صورت محلی در کنار یک API server مشخص در control plane قرار دارد.

اگر از این روش در هنگام آماده‌سازی کلاستر استفاده می‌کنید و سپس به روش احراز هویت دیگری که قرار است در درازمدت به کار رود مهاجرت می‌کنید، باید توکنی را که برای راه‌اندازی اولیه (bootstrapping) استفاده شده است غیرفعال کنید (این کار به راه‌اندازی دوبارهٔ هر یک از API serverها نیاز دارد).

در سایر موقعیت‌ها، به‌ویژه هنگامی که چرخش بسیار سریع توکن اهمیت دارد، پروژهٔ کوبرنتیز توصیه می‌کند به‌جای این سازوکار از یک [احرازکنندهٔ هویت توکن با وب‌هوک](#webhook-token-authentication) استفاده کنید.

## جعل هویت کاربر

[جعل هویت کاربر](/docs/reference/access-authn-authz/user-impersonation/) روشی فراهم می‌کند که با آن یک کاربر می‌تواند از طریق سرآیندهای جعل هویت، در نقش کاربری دیگر عمل کند.

## پیکربندی احراز هویت {#api-server-authn-config}

احراز هویت در کوبرنتیز را می‌توانید با استفاده از [آرگومان‌های خط فرمان](#api-server-authn-config-cli) یا یک [فایل پیکربندی](#api-server-authn-config-file) پیکربندی کنید.

معمولاً ترکیبی از این دو روش به کار گرفته می‌شود.

### پیکربندی از طریق آرگومان‌های خط فرمان {#api-server-authn-config-cli}

با آرگومان‌های خط فرمان زیر می‌توانید نحوهٔ احراز هویت کلاینت‌ها توسط control plane کلاستر خود را پیکربندی کنید.

[مرجع خط فرمان](/docs/reference/command-line-tools-reference/kube-apiserver/) سرور API
همهٔ آرگومان‌های خط فرمان مرتبط را با جزئیات بیشتری شرح می‌دهد.

#### پیکربندی احراز هویت ناشناس {#api-server-authn-config-cli-anonymous}

`--anonymous-auth`
: تعیین می‌کند که آیا کلاینت‌هایی که احراز هویت نشده‌اند می‌توانند از طریق پورت امن سرور API درخواست ارسال کنند یا نه. نام کاربری درخواست‌های ناشناس `system:anonymous` و نام گروه آن‌ها `system:unauthenticated` است. همچنین بخش [درخواست‌های ناشناس](#anonymous-requests) را ببینید.

#### پیکربندی توکن راه‌اندازی {#api-server-authn-config-cli-bootstrap}

`--enable-bootstrap-token-auth`
: وقتی این فلگ تنظیم شده باشد، می‌توانید برای احراز هویت از [توکن‌های راه‌اندازی (bootstrap tokens)](#bootstrap-tokens) استفاده کنید.

#### پیکربندی احراز هویت با گواهی {#api-server-authn-config-cli-x-509}

`--client-ca-file`
: مسیر لنگر (یا لنگرهای) اعتماد برای اعتبارسنجی هویت کلاینت، در حالتی که کلاینت‌ها از احراز هویت با گواهی X.509 استفاده می‌کنند.

#### پیکربندی OIDC {#api-server-authn-config-cli-oidc}

`--oidc-ca-file`
: مسیر لنگر (یا لنگرهای) اعتماد برای اعتبارسنجی هویت کلاینت، در حالتی که کلاینت‌ها از OIDC استفاده می‌کنند.

`--oidc-client-id`
: شناسهٔ کلاینت برای کلاینت OpenID Connect.

`--oidc-username-claim`
: نام یک claim در JWT برای تعیین نام کاربری؛ یعنی claimی که به‌عنوان نام کاربری به کار می‌رود. نام پیش‌فرض این claim برابر `sub` است، زیرا این مقدار باید شناسه‌ای یکتا برای کاربر نهایی باشد. می‌توانید claimهای دیگری مانند `email` یا `name` را انتخاب کنید. برای claimهایی غیر از `sub` یا `email`، kube-apiserver یک پیشوند به نام گروه اضافه می‌کند (تا از تداخل نام‌ها جلوگیری شود).

`--oidc-username-prefix`
: پیشوندی که به ابتدای claimهای نام کاربری افزوده می‌شود تا از تداخل با نام‌های موجود (مانند کاربران `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های کاربری‌ای مانند `oidc:jane.doe` ایجاد می‌کند. اگر این آرگومان ارائه نشود و `--oidc-username-claim` مقداری غیر از `email` داشته باشد، پیشوند به‌طور پیش‌فرض `( Issuer URL )#` خواهد بود که در آن `( Issuer URL )` مقدار `--oidc-issuer-url` است. برای غیرفعال کردن پیشوندگذاری نام کاربری، می‌توانید مقدار پیشوند را `-` تعیین کنید.

`--oidc-groups-claim`
: نام یک claim سفارشی OpenID Connect برای تعیین گروه‌های کاربر. این claim در توکن باید آرایه‌ای از رشته‌ها باشد. مقدار پیش‌فرضی ندارد.

`--oidc-groups-prefix`
:  پیشوندی که به ابتدای claimهای گروه افزوده می‌شود تا از تداخل با نام‌های موجود (مانند گروه‌های `system:`) جلوگیری شود. برای مثال، مقدار `oidc:` نام‌های گروهی مانند `oidc:engineering` و `oidc:infra` ایجاد می‌کند. پیشوند پیش‌فرض `oidc:` است.

`--oidc-issuer-url`
: نشانی URL صادرکنندهٔ OpenID. طرح (scheme) این URL **باید** `https` باشد. اگر نشانی کشف OIDC صادرکننده `https://accounts.provider.example/.well-known/openid-configuration` باشد، مقدار این آرگومان باید `https://accounts.provider.example` باشد.

`--oidc-required-claim`
: claimی که باید پیش از احراز هویت کلاینت توسط کوبرنتیز در توکن وجود داشته باشد. قالب آن `key=value` است. می‌توانید این آرگومان را بیش از یک بار مشخص کنید.

`--oidc-signing-algs`
: الگوریتم‌های امضای پذیرفته‌شده. مقادیر مجاز عبارت‌اند از: RS256، RS384، RS512، ES256، ES384، ES512، PS256، PS384 و PS512. این مقادیر در [RFC 7518](https://tools.ietf.org/html/rfc7518#section-3.1) تعریف شده‌اند. مقدار پیش‌فرض `RS512` است.

#### پیکربندی ServiceAccount {#api-server-authn-config-cli-sa}

`--api-audiences`
: مخاطب (audience) احراز هویت را برای توکن‌های حساب سرویس تعریف می‌کند.

`--service-account-extend-token-expiration`
: این فلگ تمدید انقضای توکن‌های projected حساب سرویس را هنگام تولید توکن فعال می‌کند. این قابلیت به گذار امن از توکن‌های قدیمی به قابلیت توکن‌های مقید حساب سرویس کمک می‌کند. بخش [احراز هویت اعتبارنامه‌های حساب سرویس](/docs/concepts/security/service-accounts/#authenticating-credentials) را ببینید.

`--service-account-issuer`
: شناسهٔ صادرکنندهٔ توکن حساب سرویس. صادرکننده این شناسه را در claim `iss` هر توکن صادرشده درج می‌کند. پروژهٔ کوبرنتیز توصیه می‌کند در اینجا از یک URL با طرح `https` استفاده کنید.

`--service-account-jwks-uri`
: نشانی URI مربوط به [JSON Web Key Set](https://www.rfc-editor.org/rfc/rfc7517) را در سند کشفی که در `/.well-known/openid-configuration` ارائه می‌شود، بازنویسی می‌کند.

`--service-account-key-file`
: مسیر فایلی حاوی کلیدهای عمومی یا خصوصی X.509 با کدگذاری PEM (از نوع RSA یا ECDSA) که برای تأیید توکن‌های ServiceAccount استفاده می‌شوند. فایل مشخص‌شده می‌تواند چند کلید داشته باشد و می‌توانید این آرگومان را چند بار با مسیرهای مختلف تعیین کنید.

`--service-account-lookup`
: اگر مقدار آن true باشد، سرور API در فرایند احراز هویت بررسی می‌کند که توکن‌های ServiceAccount در etcd وجود داشته باشند.

`--service-account-max-token-expiration`
: بیشینهٔ مدت اعتبار توکنی که صادرکنندهٔ توکن حساب سرویس ایجاد می‌کند، به‌صورت یک رشتهٔ مدت‌زمان کوبرنتیز.

`--service-account-signing-endpoint`
: مسیر سوکتی که یک امضاکنندهٔ خارجی JWT روی آن گوش می‌دهد. با این آرگومان می‌توانید با یک امضاکنندهٔ خارجی توکن یکپارچه شوید.

`--service-account-signing-key-file`
: مسیر فایلی که کلید خصوصی فعلی صادرکنندهٔ توکن حساب سرویس را در خود دارد. تغییراتی که هنگام اجرای سرور API در این فایل اعمال شوند، دوباره خوانده **نمی‌شوند**.

#### پیکربندی توکن ایستا {#api-server-authn-config-cli-bearer}

`--token-auth-file`
: مسیر فایل پیکربندی برای [توکن‌های حامل ایستا (static bearer tokens)](#static-token-file). تغییراتی که هنگام اجرای سرور API در این فایل اعمال شوند، دوباره خوانده **نمی‌شوند**.

#### پیکربندی احراز هویت وب‌هوک {#api-server-authn-config-cli-webhook}

`--authentication-token-webhook-cache-ttl`
: مدت زمانی (به‌صورت یک مشخصهٔ مدت‌زمان کوبرنتیز) که سرور API باید نتیجهٔ فراخوانی‌های HTTP برای اعتبارسنجی توکن‌ها را در حافظهٔ نهان نگه دارد.

`--authentication-token-webhook-config-file`
: مسیر یک پیکربندی کلاینت در قالب kubeconfig که مشخص می‌کند سرور API هنگام انجام فراخوانی‌های HTTP چگونه احراز هویت شود. تغییراتی که هنگام اجرای سرور API در این فایل اعمال شوند، دوباره خوانده **نمی‌شوند**.

`--authentication-token-webhook-version`
: نسخهٔ API مربوط به TokenReview که هنگام انجام فراخوانی‌های HTTP برای بررسی توکن‌ها به کار می‌رود.

#### پیکربندی احراز هویت درخواست وب {#api-server-authn-config-cli-reverse-proxy}

<!-- trailing whitespace (exactly two spaces) is significant in the following list -->

{{< caution >}}
پیش از تعیین این آرگومان‌های خط فرمان، باید مستندات مربوط به پیکربندی [پروکسی احراز هویت](#authenticating-proxy)
را بخوانید، زیرا این مستندات توصیه‌های مهمی دربارهٔ امنیت اطلاعات دارند که باید از آن‌ها پیروی کنید.
{{< /caution >}}

`--requestheader-client-ca-file`
: _الزامی._
  مسیر یک بستهٔ گواهی با کدگذاری PEM که لنگر (یا لنگرهای) اعتماد را برای اعتبارسنجی هویت پروکسی احراز هویت در خود دارد.   
  پیش از آنکه هدرهای درخواست برای یافتن نام‌های کاربری بررسی شوند، باید یک [گواهی کلاینت](#reverse-proxy-client-certificate)
  معتبر ارائه شود و با مراجع صدور گواهی موجود در فایل مشخص‌شده
  اعتبارسنجی شود.

`--requestheader-allowed-names`
: _اختیاری._ فهرستی از مقادیر Common Name (CN) که با کاما از هم جدا شده‌اند.  
  اگر تنظیم شود، پیش از آنکه هدرهای درخواست برای یافتن نام‌های کاربری بررسی شوند، باید یک گواهی
  کلاینت معتبر ارائه شود که CN آن در فهرست مشخص‌شده باشد.
  اگر خالی باشد، هر CNی مجاز است.

`--requestheader-username-headers`
: _الزامی؛ بدون حساسیت به بزرگی و کوچکی حروف._ نام هدرهایی که به ترتیب برای یافتن هویت کاربر بررسی می‌شوند.  
  نخستین هدری که مقدار داشته باشد، به‌عنوان نام کاربری استفاده می‌شود.

`--requestheader-group-headers`
: _اختیاری؛ بدون حساسیت به بزرگی و کوچکی حروف._
  نام هدرهایی که به ترتیب برای یافتن گروه‌های کاربر بررسی می‌شوند.  
  استفاده از `X-Remote-Group` پیشنهاد می‌شود.
  همهٔ مقادیر موجود در همهٔ هدرهای مشخص‌شده به‌عنوان نام گروه استفاده می‌شوند.

`--requestheader-extra-headers-prefix`
: _اختیاری؛ بدون حساسیت به بزرگی و کوچکی حروف._
  پیشوندهای هدری که برای تعیین اطلاعات اضافی دربارهٔ کاربر جست‌وجو می‌شوند.  
  استفاده از `X-Remote-Extra-` پیشنهاد می‌شود.
  داده‌های اضافی معمولاً توسط افزونه (یا افزونه‌های) مجوزدهی پیکربندی‌شده استفاده می‌شوند.
  از هر هدری که با یکی از پیشوندهای مشخص‌شده شروع شود، آن پیشوند حذف می‌شود.
  باقی‌ماندهٔ نام هدر به حروف کوچک تبدیل و [رمزگشایی درصدی (percent-decoded)](https://tools.ietf.org/html/rfc3986#section-2.1) می‌شود
  و به کلید اضافی تبدیل می‌شود، و مقدار هدر نیز مقدار اضافی خواهد بود.


### پیکربندی از طریق فایل پیکربندی {#api-server-authn-config-file}

{{< feature-state feature_gate_name="StructuredAuthenticationConfiguration" >}}

وقتی آرگومان خط فرمان `--authentication-config` را به kube-apiserver می‌دهید، سرور API
فایلی را از مسیری که مشخص کرده‌اید بارگذاری می‌کند و از محتوای آن برای پیکربندی احراز هویت استفاده می‌کند.

محتوای این فایل را می‌توان هنگام اجرای سرور API تغییر داد؛ در این صورت، سرور API پس از آن فایل را دوباره می‌خواند.

{{< note >}}
تغییرات این فایل باید به‌صورت اتمیک انجام شوند (برای مثال: ابتدا در یک فایل موقت هم‌جوار بنویسید و سپس با تغییر نام فایل موقت، آن را جایگزین این فایل کنید).
{{< /note >}}

#### مسیر فایل پیکربندی {#api-server-authn-config-cli-general}

`--authentication-config`
: این آرگومان خط فرمان ویژه مشخص می‌کند که می‌خواهید [احراز هویت را با استفاده از یک فایل پیکربندی، پیکربندی کنید](#api-server-authn-config-file).

#### مثال {#api-server-authn-config-file-example}

در ادامه نمونه‌ای از یک فایل پیکربندی احراز هویت (ساختاریافتهٔ) کوبرنتیز آمده است:

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

## افزونه‌های اعتبارنامهٔ client-go

{{< feature-state for_k8s_version="v1.22" state="stable" >}}

کتابخانهٔ `k8s.io/client-go` و ابزارهایی که از آن استفاده می‌کنند، مانند `kubectl` و `kubelet`، می‌توانند
یک فرمان خارجی را برای دریافت اعتبارنامه‌های کاربر اجرا کنند.

این قابلیت برای یکپارچه‌سازی سمت کلاینت با پروتکل‌های احراز هویتی طراحی شده است که
`k8s.io/client-go` به‌صورت بومی از آن‌ها پشتیبانی نمی‌کند (مانند LDAP، Kerberos، OAuth2، SAML و غیره). افزونه
منطق مخصوص پروتکل را پیاده‌سازی می‌کند و سپس اعتبارنامه‌هایی مبهم (opaque) را برای استفاده برمی‌گرداند. تقریباً همهٔ
موارد استفاده از افزونه‌های اعتبارنامه به یک مؤلفهٔ سمت سرور نیاز دارند که از [احرازکنندهٔ توکن وب‌هوک](#webhook-token-authentication)
پشتیبانی کند تا قالب اعتبارنامهٔ تولیدشده توسط افزونهٔ کلاینت را تفسیر کند.

{{< note >}}
نسخه‌های قدیمی‌تر `kubectl` پشتیبانی داخلی برای احراز هویت در AKS و GKE داشتند، اما این پشتیبانی دیگر وجود ندارد.
{{< /note >}}

### نمونهٔ مورد استفاده

در یک مورد استفادهٔ فرضی، سازمانی یک سرویس خارجی را اجرا می‌کند که اعتبارنامه‌های LDAP را
با توکن‌های امضاشدهٔ مخصوص هر کاربر مبادله می‌کند. این سرویس همچنین می‌تواند به درخواست‌های
[احرازکنندهٔ توکن وب‌هوک](#webhook-token-authentication) برای اعتبارسنجی توکن‌ها پاسخ دهد. کاربران
باید یک افزونهٔ اعتبارنامه را روی ایستگاه کاری خود نصب کنند.

برای احراز هویت در برابر API:

* کاربر یک فرمان `kubectl` اجرا می‌کند.
* افزونهٔ اعتبارنامه اعتبارنامه‌های LDAP را از کاربر درخواست می‌کند و آن‌ها را با سرویس خارجی در ازای یک توکن مبادله می‌کند.
* افزونهٔ اعتبارنامه توکن را به client-go برمی‌گرداند و client-go از آن به‌عنوان توکن حامل (bearer token) در برابر سرور API استفاده می‌کند.
* سرور API با استفاده از [احرازکنندهٔ توکن وب‌هوک](#webhook-token-authentication) یک `TokenReview` را به سرویس خارجی ارسال می‌کند.
* سرویس خارجی امضای توکن را تأیید می‌کند و نام کاربری و گروه‌های کاربر را برمی‌گرداند.

### پیکربندی

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

مسیرهای نسبی فرمان، نسبت به دایرکتوری فایل پیکربندی تفسیر می‌شوند. اگر مقدار
KUBECONFIG برابر `/home/jane/kubeconfig` و فرمان exec برابر `./bin/example-client-go-exec-plugin` باشد،
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

### قالب‌های ورودی و خروجی

فرمان اجراشده یک آبجکت `ExecCredential` را در `stdout` چاپ می‌کند. کتابخانهٔ `k8s.io/client-go`
با استفاده از اعتبارنامه‌های برگردانده‌شده در `status`، در برابر API کوبرنتیز احراز هویت می‌کند.
یک آبجکت `ExecCredential` نیز از طریق متغیر محیطی `KUBERNETES_EXEC_INFO` به‌عنوان ورودی به فرمان اجراشده داده می‌شود.
این ورودی اطلاعات مفیدی دارد؛ مثلاً نسخهٔ API مورد انتظار برای آبجکت `ExecCredential` برگشتی، و اینکه آیا افزونه
می‌تواند برای تعامل با کاربر از `stdin` استفاده کند یا نه.

هنگامی که افزونه از یک نشست تعاملی (یعنی یک ترمینال) اجرا می‌شود، می‌توان `stdin` را مستقیماً در اختیار آن گذاشت.
افزونه‌ها باید با استفاده از فیلد `spec.interactive` در آبجکت `ExecCredential` ورودی که از متغیر محیطی
`KUBERNETES_EXEC_INFO` دریافت می‌شود، تشخیص دهند که آیا `stdin` فراهم شده است یا نه. نیازمندی‌های یک افزونه
به `stdin` (یعنی اینکه برای اجرای موفق افزونه، `stdin` اختیاری است، الزاماً لازم است یا هرگز استفاده نمی‌شود)
از طریق فیلد `user.exec.interactiveMode` در
[kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) اعلام می‌شود
(برای مقادیر معتبر، جدول زیر را ببینید). فیلد `user.exec.interactiveMode` در
`client.authentication.k8s.io/v1beta1` اختیاری و در `client.authentication.k8s.io/v1` الزامی است.

{{< table caption="مقادیر interactiveMode" >}}
| مقدار `interactiveMode` | معنا |
| ----------------------- | ------- |
| `Never` | این افزونهٔ exec هرگز به ورودی استاندارد نیاز ندارد؛ بنابراین صرف‌نظر از اینکه ورودی استاندارد برای دریافت ورودی کاربر در دسترس باشد یا نه، اجرا می‌شود. |
| `IfAvailable` | این افزونهٔ exec ترجیح می‌دهد در صورت در دسترس بودن ورودی استاندارد از آن استفاده کند، اما بدون آن نیز می‌تواند کار کند. بنابراین صرف‌نظر از اینکه stdin برای دریافت ورودی کاربر در دسترس باشد یا نه، اجرا می‌شود. اگر ورودی استاندارد برای دریافت ورودی کاربر در دسترس باشد، در اختیار این افزونهٔ exec قرار می‌گیرد. |
| `Always` | این افزونهٔ exec برای اجرا به ورودی استاندارد نیاز دارد؛ بنابراین فقط در صورتی اجرا می‌شود که ورودی استاندارد برای دریافت ورودی کاربر در دسترس باشد. اگر ورودی استاندارد در دسترس نباشد، افزونهٔ exec اجرا نمی‌شود و اجراکنندهٔ افزونهٔ exec خطا برمی‌گرداند. |
{{< /table >}}

برای استفاده از اعتبارنامه‌های توکن حامل (bearer token)، افزونه یک توکن را در status آبجکت
[`ExecCredential`](/docs/reference/config-api/client-authentication.v1beta1/#client-authentication-k8s-io-v1beta1-ExecCredential) برمی‌گرداند.

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

به‌عنوان جایگزین، می‌توان یک گواهی و کلید کلاینت با کدگذاری PEM برگرداند تا از احراز هویت کلاینت TLS استفاده شود.
اگر افزونه در فراخوانی بعدی گواهی و کلید متفاوتی برگرداند، `k8s.io/client-go`
اتصال‌های موجود با سرور را می‌بندد تا دست‌دهی (handshake) جدید TLS انجام شود.

در صورت تعیین، هر دو فیلد `clientKeyData` و `clientCertificateData` باید وجود داشته باشند.

فیلد `clientCertificateData` می‌تواند گواهی‌های میانی بیشتری را برای ارسال به سرور در خود داشته باشد.

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

پاسخ می‌تواند به‌صورت اختیاری زمان انقضای اعتبارنامه را نیز در قالب یک برچسب زمانی
[RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) در بر داشته باشد.

وجود یا نبودِ زمان انقضا پیامدهای زیر را دارد:

- اگر زمان انقضا درج شده باشد، توکن حامل و اعتبارنامه‌های TLS تا رسیدن زمان انقضا،
  یا تا زمانی که سرور با کد وضعیت HTTP 401 پاسخ دهد، یا تا خروج فرایند در حافظهٔ نهان نگه‌داری می‌شوند.
- اگر زمان انقضا درج نشده باشد، توکن حامل و اعتبارنامه‌های TLS تا زمانی که
  سرور با کد وضعیت HTTP 401 پاسخ دهد یا تا خروج فرایند در حافظهٔ نهان نگه‌داری می‌شوند.

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

برای اینکه افزونهٔ exec بتواند اطلاعات مختص کلاستر را دریافت کند، `provideClusterInfo` را در فیلد `user.exec`
در [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) تنظیم کنید.
در این صورت، این اطلاعات مختص کلاستر از طریق متغیر محیطی `KUBERNETES_EXEC_INFO` در اختیار افزونه قرار می‌گیرد.
می‌توان از اطلاعات این متغیر محیطی برای پیاده‌سازی منطق دریافت اعتبارنامه به‌صورت مختص هر کلاستر استفاده کرد.
مانیفست `ExecCredential` زیر نمونه‌ای از اطلاعات کلاستر را نشان می‌دهد.

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

با API مربوط به SelfSubjectReview می‌توانید دریابید که کلاستر کوبرنتیز شما
چگونه اطلاعات احراز هویتتان را نگاشت می‌کند تا شما را به‌عنوان یک کلاینت شناسایی کند.
این روش، چه به‌عنوان یک کاربر (که معمولاً نمایندهٔ یک شخص واقعی است) احراز هویت کنید
و چه به‌عنوان یک ServiceAccount، کار می‌کند.

در یک کلاستر کوبرنتیز معمولی، همهٔ کاربران احراز هویت‌شده می‌توانند SelfSubjectReview ایجاد کنند.
این دسترسی را
[ClusterRole](/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) داخلی `system:basic-user` مجاز می‌کند.

توانایی کلاینت در شناختن هویت خودش، هنگام عیب‌یابی یک جریان پیچیدهٔ احراز هویت در کلاستر کوبرنتیز بسیار سودمند است؛
برای نمونه، اگر از [احراز هویت با توکن وب‌هوک](/docs/reference/access-authn-authz/authentication/#webhook-token-authentication)
یا یک [پراکسی احراز هویت](/docs/reference/access-authn-authz/authentication/#authenticating-proxy) استفاده می‌کنید.

اگر می‌خواهید این اطلاعات را از خط فرمان پرس‌وجو کنید،
[دسترسی CLI به اطلاعات احراز هویت](#self-subject-review-cli) را ببینید.

### دسترسی HTTP به اطلاعات احراز هویت {#self-subject-review-http-api}

آبجکت‌های SelfSubjectReview هیچ فیلد قابل‌پیکربندی‌ای ندارند. سرور API کوبرنتیز
با دریافت درخواست، status را با ویژگی‌های کاربر پر می‌کند و آن را به کاربر برمی‌گرداند.
این کار **هیچ** منبع نام‌داری را در کلاستر شما ذخیره نمی‌کند: نمی‌توانید
SelfSubjectReview را بازیابی کنید و پس از تکمیل درخواست `POST` شما، دور ریخته می‌شود.

نمونهٔ درخواست (بدنهٔ درخواست یک SelfSubjectReview است):

```http
POST /apis/authentication.k8s.io/v1/selfsubjectreviews
```

```json
{
  "apiVersion": "authentication.k8s.io/v1",
  "kind": "SelfSubjectReview"
}
```

نمونهٔ پاسخ:

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
سرور API کوبرنتیز پس از اعمال همهٔ سازوکارهای احراز هویت، از جمله
[جعل هویت (impersonation)](/docs/reference/access-authn-authz/authentication/#user-impersonation)، فیلد `userInfo` را پر می‌کند.
اگر شما یا یک پراکسی احراز هویت با استفاده از جعل هویت یک SelfSubjectReview ایجاد کنید،
جزئیات و ویژگی‌های کاربری را می‌بینید که هویتش جعل شده است.
{{< /note >}}

این نمونهٔ پاسخ همهٔ فیلدهای موجود را نشان نمی‌دهد؛ همهٔ سازوکارهای
احراز هویت همهٔ فیلدهای موجود را پر نمی‌کنند.
برای دیدن فیلدهای موجود، [مرجع API آبجکت SelfSubjectReview](/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/) را ببینید.

نمونهٔ دیگری که فیلدهای `uid` و `extra` را نیز در بر دارد، در ادامه آمده است:

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

داده‌های این فیلدهای اختیاری از یکپارچه‌سازی احراز هویت شما یا از پایگاه دادهٔ کاربرانی
که آن یکپارچه‌سازی استفاده می‌کند، به دست می‌آیند. نام کاربری، UID، اطلاعات اضافی
و همهٔ گروه‌هایی که نامشان با `system:` شروع نمی‌شود، همگی از بیرون کوبرنتیز تأمین می‌شوند.


هنگام پرس‌وجو از API کوبرنتیز از طریق HTTP، می‌توانید با استفاده از سرآیند HTTP با نام `Accept:`
پاسخ را در قالب JSON یا YAML درخواست کنید؛ برای نمونه:

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

برای راحتی، زیرفرمان `kubectl auth whoami` نیز در دسترس است:
```shell
kubectl auth whoami
```

خروجی مشابه زیر است:
```console
  ATTRIBUTE         VALUE
  Username          george.boole
  Groups            [system:authenticated]
```

برای جزئیات بیشتر، [`kubectl auth whoami`](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/) را ببینید.


## {{% heading "whatsnext" %}}

* برای آشنایی با صدور گواهی برای کاربران، [صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/) را بخوانید.
* [مرجع احراز هویت کلاینت (v1)](/docs/reference/config-api/client-authentication.v1/) را بخوانید.
* [مرجع احراز هویت کلاینت (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/) را بخوانید.
