---
title: Service Accounts
description: >
  با آبجکت‌های ServiceAccount در کوبرنتیز آشنا شوید.
api_metadata:
- apiVersion: "v1"
  kind: "ServiceAccount"  
content_type: concept
weight: 25
---

<!-- overview -->

این صفحه آبجکت ServiceAccount را در کوبرنتیز معرفی می‌کند و اطلاعاتی درباره‌ی نحوه‌ی کار حساب‌های سرویس (service accounts)، موارد استفاده، محدودیت‌ها و جایگزین‌ها ارائه می‌دهد و پیوندهایی به منابع راهنمای بیشتر در اختیار شما قرار می‌دهد.

<!-- body -->

## حساب‌های سرویس چیستند؟ {#what-are-service-accounts}

حساب سرویس (service account) نوعی حساب غیرانسانی است که در کوبرنتیز یک هویت مجزا در کلاستر کوبرنتیز فراهم می‌کند. Podهای برنامه، مؤلفه‌های سیستمی و موجودیت‌های داخل و خارج از کلاستر می‌توانند از اعتبارنامه‌های (credentials) یک ServiceAccount مشخص استفاده کنند تا خود را به‌عنوان آن ServiceAccount معرفی کنند. این هویت در موقعیت‌های گوناگونی مفید است، از جمله احراز هویت در برابر API server یا پیاده‌سازی سیاست‌های امنیتی مبتنی بر هویت.

حساب‌های سرویس به‌صورت آبجکت‌های ServiceAccount در API server وجود دارند. حساب‌های سرویس ویژگی‌های زیر را دارند:

* **دارای فضای نام (Namespaced):** هر حساب سرویس به یک
  {{<glossary_tooltip text="فضای نام" term_id="namespace">}} کوبرنتیز وابسته است. با ایجاد هر فضای نام، یک [ServiceAccount با نام `default`](#default-service-accounts) برای آن ساخته می‌شود.

* **سبک‌وزن (Lightweight):** حساب‌های سرویس در کلاستر وجود دارند و در API کوبرنتیز تعریف می‌شوند. می‌توانید حساب‌های سرویس را به‌سرعت برای فعال‌سازی وظایف مشخص ایجاد کنید.

* **قابل‌حمل (Portable):** بسته‌ی پیکربندی یک بار کاری کانتینری پیچیده ممکن است شامل تعریف حساب‌های سرویس برای مؤلفه‌های آن سیستم باشد. سبک‌وزن بودن حساب‌های سرویس و هویت‌های دارای فضای نام، پیکربندی‌ها را قابل‌حمل می‌کند.

حساب‌های سرویس با حساب‌های کاربری (user accounts) که کاربران انسانیِ احراز هویت‌شده در کلاستر هستند، متفاوت‌اند. به‌طور پیش‌فرض، حساب‌های کاربری در API server کوبرنتیز وجود ندارند؛ در عوض، API server هویت‌های کاربران را داده‌ای مبهم (opaque) در نظر می‌گیرد. می‌توانید با روش‌های متعددی به‌عنوان یک حساب کاربری احراز هویت کنید. برخی توزیع‌های کوبرنتیز ممکن است APIهای افزونه‌ی سفارشی اضافه کنند تا حساب‌های کاربری را در API server نمایش دهند.

{{< table caption="مقایسه‌ی حساب‌های سرویس و کاربران" >}}

| توضیح | ServiceAccount | کاربر یا گروه |
| --- | --- | --- |
| محل | API کوبرنتیز (آبجکت ServiceAccount) | خارجی |
| کنترل دسترسی | RBAC کوبرنتیز یا سایر [سازوکارهای مجوزدهی](/docs/reference/access-authn-authz/authorization/#authorization-modules) | RBAC کوبرنتیز یا سایر سازوکارهای مدیریت هویت و دسترسی |
| کاربرد موردنظر | بارهای کاری، خودکارسازی | افراد |

{{< /table >}}

### حساب‌های سرویس پیش‌فرض {#default-service-accounts}

وقتی یک کلاستر ایجاد می‌کنید، کوبرنتیز به‌طور خودکار برای هر فضای نام در کلاستر شما یک آبجکت ServiceAccount با نام `default` ایجاد می‌کند. حساب‌های سرویس `default` در هر فضای نام، به‌جز [مجوزهای پیش‌فرض کشف API](/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings) که در صورت فعال بودن کنترل دسترسی مبتنی بر نقش (RBAC) کوبرنتیز به همه‌ی principalهای احراز هویت‌شده می‌دهد، هیچ مجوز دیگری به‌طور پیش‌فرض دریافت نمی‌کنند. اگر آبجکت ServiceAccount با نام `default` را در یک فضای نام حذف کنید، {{< glossary_tooltip text="control plane" term_id="control-plane" >}} آن را با یک نمونه‌ی جدید جایگزین می‌کند.

اگر Podی را در یک فضای نام مستقر کنید و [ServiceAccount را به‌صورت دستی به Pod اختصاص ندهید](#assign-to-pod)، کوبرنتیز ServiceAccount با نام `default` همان فضای نام را به Pod اختصاص می‌دهد.

## موارد استفاده از حساب‌های سرویس کوبرنتیز {#use-cases}

به‌عنوان یک راهنمای کلی، می‌توانید از حساب‌های سرویس برای فراهم کردن هویت در سناریوهای زیر استفاده کنید:

* Podهای شما نیاز دارند با API server کوبرنتیز ارتباط برقرار کنند، برای مثال در موقعیت‌هایی مانند موارد زیر:
  * فراهم کردن دسترسی فقط‌خواندنی به اطلاعات حساس ذخیره‌شده در Secretها.
  * اعطای [دسترسی بین‌فضاهای نام](#cross-namespace)، مانند اجازه دادن به یک Pod در فضای نام `example` برای خواندن، فهرست کردن و دنبال کردن (watch) آبجکت‌های Lease در فضای نام `kube-node-lease`.
* Podهای شما نیاز دارند با یک سرویس خارجی ارتباط برقرار کنند. برای مثال، یک Pod بار کاری به هویتی برای یک API ابری تجاری نیاز دارد و ارائه‌دهنده‌ی تجاری امکان پیکربندی یک رابطه‌ی اعتماد مناسب را فراهم می‌کند.
* [احراز هویت در برابر یک رجیستری خصوصی ایمیج با استفاده از `imagePullSecret`](/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account).
* یک سرویس خارجی نیاز دارد با API server کوبرنتیز ارتباط برقرار کند. برای مثال، احراز هویت در کلاستر به‌عنوان بخشی از یک pipeline مربوط به CI/CD.
* در کلاستر خود از نرم‌افزار امنیتی شخص ثالثی استفاده می‌کنید که برای گروه‌بندی Podها در زمینه‌های (contexts) مختلف، به هویت ServiceAccount هر Pod متکی است.

## نحوه‌ی استفاده از حساب‌های سرویس {#how-to-use}

برای استفاده از یک حساب سرویس کوبرنتیز، مراحل زیر را انجام می‌دهید:

1. با استفاده از یک کلاینت کوبرنتیز مانند `kubectl` یا یک مانیفست که آبجکت را تعریف می‌کند، یک آبجکت ServiceAccount ایجاد کنید.
1. با استفاده از یک سازوکار مجوزدهی مانند [RBAC](/docs/reference/access-authn-authz/rbac/)، به آبجکت ServiceAccount مجوزها را اعطا کنید.
1. آبجکت ServiceAccount را هنگام ایجاد Pod به Podها اختصاص دهید.

   اگر از هویت یک سرویس خارجی استفاده می‌کنید، به‌جای آن [توکن ServiceAccount را دریافت کنید](#get-a-token) و از آن در همان سرویس استفاده کنید.

برای مشاهده‌ی دستورالعمل‌ها به
[پیکربندی حساب‌های سرویس برای Podها](/docs/tasks/configure-pod-container/configure-service-account/) مراجعه کنید.

### اعطای مجوزها به یک ServiceAccount {#grant-permissions}

می‌توانید از سازوکار داخلی [کنترل دسترسی مبتنی بر نقش (RBAC)](/docs/reference/access-authn-authz/rbac/) کوبرنتیز برای اعطای حداقل مجوزهای موردنیاز به هر حساب سرویس استفاده کنید. شما یک *نقش (role)* ایجاد می‌کنید که دسترسی را اعطا می‌کند و سپس آن نقش را به ServiceAccount خود *متصل (bind)* می‌کنید. RBAC به شما امکان می‌دهد حداقل مجموعه‌ی مجوزها را تعریف کنید تا مجوزهای حساب سرویس از اصل حداقل امتیاز (principle of least privilege) پیروی کنند. Podهایی که از آن حساب سرویس استفاده می‌کنند، بیش از آنچه برای عملکرد صحیح لازم است مجوز دریافت نمی‌کنند.

برای مشاهده‌ی دستورالعمل‌ها به
[مجوزهای ServiceAccount](/docs/reference/access-authn-authz/rbac/#service-account-permissions) مراجعه کنید.

#### دسترسی بین‌فضاهای نام با استفاده از ServiceAccount {#cross-namespace}

می‌توانید از RBAC استفاده کنید تا به حساب‌های سرویس در یک فضای نام اجازه دهید روی منابع در فضای نام دیگری از کلاستر عملیات انجام دهند. برای مثال، سناریویی را در نظر بگیرید که در آن یک حساب سرویس و یک Pod در فضای نام `dev` دارید و می‌خواهید Pod شما Jobهای در حال اجرا در فضای نام `maintenance` را ببیند. می‌توانید یک آبجکت Role ایجاد کنید که مجوز فهرست کردن آبجکت‌های Job را اعطا می‌کند. سپس یک آبجکت RoleBinding در فضای نام `maintenance` ایجاد می‌کنید تا Role را به آبجکت ServiceAccount متصل کند. اکنون Podهای فضای نام `dev` می‌توانند با استفاده از آن حساب سرویس، آبجکت‌های Job را در فضای نام `maintenance` فهرست کنند.

### اختصاص یک ServiceAccount به یک Pod {#assign-to-pod}

برای اختصاص یک ServiceAccount به یک Pod، فیلد `spec.serviceAccountName` را در مشخصات Pod تنظیم می‌کنید. سپس کوبرنتیز به‌طور خودکار اعتبارنامه‌های آن ServiceAccount را در اختیار Pod قرار می‌دهد. در نسخه‌ی v1.22 و بعدتر، کوبرنتیز با استفاده از API مربوط به `TokenRequest` یک توکن کوتاه‌مدت با **چرخش خودکار** دریافت می‌کند و آن را به‌صورت یک [projected volume](/docs/concepts/storage/projected-volumes/#serviceaccounttoken) مانت می‌کند.

به‌طور پیش‌فرض، کوبرنتیز اعتبارنامه‌های ServiceAccount اختصاص‌داده‌شده را در اختیار Pod قرار می‌دهد، چه ServiceAccount با نام `default` باشد و چه یک ServiceAccount سفارشی که شما مشخص کرده‌اید.

برای جلوگیری از تزریق خودکار اعتبارنامه‌ها برای یک ServiceAccount مشخص‌شده یا ServiceAccount با نام `default` توسط کوبرنتیز، فیلد `automountServiceAccountToken` را در مشخصات Pod خود روی `false` تنظیم کنید.

<!-- OK to remove this historical detail after Kubernetes 1.31 is released -->

در نسخه‌های قدیمی‌تر از 1.22، کوبرنتیز یک توکن ایستا و بلندمدت را در قالب یک Secret در اختیار Pod قرار می‌دهد.

#### دریافت دستی اعتبارنامه‌های ServiceAccount {#get-a-token}

اگر به اعتبارنامه‌های یک ServiceAccount نیاز دارید تا آن را در یک مکان غیراستاندارد یا برای مخاطبی (audience) غیر از API server مانت کنید، از یکی از روش‌های زیر استفاده کنید:

* [TokenRequest API](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
  (توصیه‌شده): یک توکن حساب سرویس کوتاه‌مدت را از درون *کد برنامه‌ی* خودتان درخواست کنید. توکن به‌طور خودکار منقضی می‌شود و می‌تواند هنگام انقضا چرخش یابد.
  اگر برنامه‌ی قدیمی دارید که از کوبرنتیز آگاه نیست، می‌توانید از یک کانتینر sidecar در همان Pod برای دریافت این توکن‌ها و در دسترس قرار دادن آن‌ها برای بار کاری برنامه استفاده کنید.
* [Token Volume Projection](/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection)
  (آن هم توصیه‌شده): در کوبرنتیز v1.20 و بعدتر، از مشخصات Pod استفاده کنید تا به kubelet بگویید توکن حساب سرویس را به‌صورت یک *projected volume* به Pod اضافه کند. توکن‌های projected به‌طور خودکار منقضی می‌شوند و kubelet توکن را پیش از انقضا چرخش می‌دهد.
* [Service Account Token Secrets](/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount)
  (توصیه‌نشده): می‌توانید توکن‌های حساب سرویس را به‌صورت Secretهای کوبرنتیز در Podها مانت کنید. این توکن‌ها منقضی نمی‌شوند و چرخش نمی‌یابند. در نسخه‌های پیش از v1.24، یک توکن دائمی به‌طور خودکار برای هر حساب سرویس ایجاد می‌شد. این روش دیگر توصیه نمی‌شود، به‌ویژه در مقیاس بالا، به دلیل ریسک‌های مرتبط با اعتبارنامه‌های ایستا و بلندمدت. [feature gate مربوط به LegacyServiceAccountTokenNoAutoGeneration](/docs/reference/command-line-tools-reference/feature-gates-removed)
  (که از کوبرنتیز v1.24 تا v1.26 به‌طور پیش‌فرض فعال بود) از ایجاد خودکار این توکن‌ها برای ServiceAccountها توسط کوبرنتیز جلوگیری می‌کرد. این feature gate در v1.27 حذف شد، زیرا به وضعیت GA ارتقا یافت؛ همچنان می‌توانید به‌صورت دستی توکن‌های حساب سرویس نامحدود ایجاد کنید، اما باید پیامدهای امنیتی آن را در نظر بگیرید.

#### محدودسازی مخاطب (audience) در نود برای توکن‌های حساب سرویس {#node-audience-restriction}

{{< feature-state feature_gate_name="ServiceAccountNodeAudienceRestriction" >}}

وقتی [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ServiceAccountNodeAudienceRestriction` فعال باشد، admission plugin با نام [NodeRestriction](/docs/reference/access-authn-authz/admission-controllers#noderestriction) مشخص می‌کند که kubelet هنگام ایجاد توکن‌های حساب سرویس از طریق API مربوط به `TokenRequest` چه مخاطب‌هایی (audiences) را می‌تواند درخواست کند. به‌طور پیش‌فرض، kubelet فقط می‌تواند برای مخاطب‌هایی توکن درخواست کند که پیش‌تر توسط Podهای روی آن نود ارجاع داده شده‌اند (از طریق حجم‌های توکن حساب سرویس projected یا درخواست‌های توکن درایور CSI). مدیران می‌توانند با استفاده از قوانین RBAC و فعل (verb) با نام `request-serviceaccounts-token-audience`، به kubeletها دسترسی به مخاطب‌های اضافی را اعطا کنند.

این محدودیت فقط برای kubeletها (هویت‌های نود) اعمال می‌شود و بر سایر فراخوانندگان API مربوط به `TokenRequest` تأثیری ندارد. برای جزئیات و مثال‌های RBAC، به [محدودسازی مخاطب توکن حساب سرویس](/docs/reference/access-authn-authz/node/#service-account-token-audience-restriction) مراجعه کنید.

{{< note >}}
برای برنامه‌هایی که خارج از کلاستر کوبرنتیز شما اجرا می‌شوند، ممکن است به ایجاد یک توکن ServiceAccount بلندمدت که در یک Secret ذخیره می‌شود فکر کنید. این روش احراز هویت را ممکن می‌کند، اما پروژه‌ی کوبرنتیز توصیه می‌کند از آن اجتناب کنید.
توکن‌های bearer بلندمدت یک ریسک امنیتی هستند، زیرا در صورت افشا، توکن می‌تواند مورد سوءاستفاده قرار گیرد. به‌جای آن، یک جایگزین را در نظر بگیرید. برای مثال، برنامه‌ی خارجی شما می‌تواند با یک کلید خصوصی به‌خوبی محافظت‌شده `و` یک گواهی احراز هویت کند، یا از یک سازوکار سفارشی مانند [webhook احراز هویت](/docs/reference/access-authn-authz/authentication/#webhook-token-authentication) که خودتان پیاده‌سازی می‌کنید استفاده کند.

همچنین می‌توانید از TokenRequest برای دریافت توکن‌های کوتاه‌مدت برای برنامه‌ی خارجی خود استفاده کنید.
{{< /note >}}

### محدودسازی دسترسی به Secretها (منسوخ‌شده) {#enforce-mountable-secrets}

{{< feature-state for_k8s_version="v1.32" state="deprecated" >}}

{{< note >}}
`kubernetes.io/enforce-mountable-secrets` از کوبرنتیز v1.32 منسوخ شده است. برای ایزوله کردن دسترسی به secretهای مانت‌شده از فضاهای نام جداگانه استفاده کنید.
{{< /note >}}

کوبرنتیز حاشیه‌نویسی (annotation) ای با نام `kubernetes.io/enforce-mountable-secrets` ارائه می‌دهد که می‌توانید آن را به ServiceAccountهای خود اضافه کنید. وقتی این annotation اعمال شود، secretهای ServiceAccount فقط روی انواع مشخصی از منابع قابل مانت شدن هستند و این کار وضعیت امنیتی کلاستر شما را تقویت می‌کند.

می‌توانید این annotation را با استفاده از یک مانیفست به ServiceAccount اضافه کنید:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    kubernetes.io/enforce-mountable-secrets: "true"
  name: my-serviceaccount
  namespace: my-namespace
```
وقتی این annotation روی "true" تنظیم شود، control plane کوبرنتیز تضمین می‌کند که Secretهای این ServiceAccount مشمول محدودیت‌های مانت مشخصی هستند.

1. نام هر Secret که به‌صورت volume در یک Pod مانت می‌شود باید در فیلد `secrets` مربوط به ServiceAccount آن Pod آمده باشد.
1. نام هر Secret که با استفاده از `envFrom` در یک Pod ارجاع داده می‌شود نیز باید در فیلد `secrets` مربوط به ServiceAccount آن Pod آمده باشد.
1. نام هر Secret که با استفاده از `imagePullSecrets` در یک Pod ارجاع داده می‌شود نیز باید در فیلد `secrets` مربوط به ServiceAccount آن Pod آمده باشد.

با درک و اعمال این محدودیت‌ها، مدیران کلاستر می‌توانند وضعیت امنیتی سخت‌گیرانه‌تری را حفظ کنند و اطمینان یابند که secretها فقط توسط منابع مناسب مورد دسترسی قرار می‌گیرند.

## احراز هویت اعتبارنامه‌های حساب سرویس {#authenticating-credentials}

ServiceAccountها از {{<glossary_tooltip term_id="jwt" text="JSON Web Tokenهای">}} (JWT) امضاشده برای احراز هویت در برابر API server کوبرنتیز و هر سیستم دیگری که رابطه‌ی اعتماد در آن برقرار است استفاده می‌کنند. بسته به نحوه‌ی صدور توکن (یا به‌صورت زمان‌محدود با استفاده از `TokenRequest` یا با استفاده از سازوکار قدیمی مبتنی بر Secret)، توکن ServiceAccount ممکن است زمان انقضا، مخاطب (audience) و زمانی که پس از آن اعتبار توکن *آغاز* می‌شود نیز داشته باشد. وقتی کلاینتی که به‌عنوان یک ServiceAccount عمل می‌کند تلاش می‌کند با API server کوبرنتیز ارتباط برقرار کند، کلاینت یک هدر `Authorization: Bearer <token>` را در درخواست HTTP قرار می‌دهد. API server اعتبار آن توکن bearer را به شرح زیر بررسی می‌کند:

1. امضای توکن را بررسی می‌کند.
1. بررسی می‌کند که آیا توکن منقضی شده است یا نه.
1. بررسی می‌کند که آیا ارجاع‌های آبجکت در claimهای توکن در حال حاضر معتبر هستند یا نه.
1. بررسی می‌کند که آیا توکن در حال حاضر معتبر است یا نه.
1. claimهای مخاطب (audience) را بررسی می‌کند.

API مربوط به TokenRequest برای یک ServiceAccount، _توکن‌های مقید (bound tokens)_ تولید می‌کند. این اتصال به طول عمر کلاینتی مرتبط است، مانند یک Pod، که به‌عنوان آن ServiceAccount عمل می‌کند. برای مشاهده‌ی نمونه‌ای از طرح‌واره (schema) و payload مربوط به JWT یک توکن حساب سرویس Pod مقید، به [Token Volume Projection](/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection) مراجعه کنید.

برای توکن‌هایی که با استفاده از API مربوط به `TokenRequest` صادر شده‌اند، API server همچنین بررسی می‌کند که ارجاع آبجکت مشخصی که از ServiceAccount استفاده می‌کند هنوز وجود داشته باشد، و این کار را با تطبیق {{< glossary_tooltip term_id="uid" text="شناسه‌ی یکتای" >}} آن آبجکت انجام می‌دهد. برای توکن‌های قدیمی که به‌صورت Secret در Podها مانت شده‌اند، API server توکن را با Secret مقایسه و بررسی می‌کند.

برای اطلاعات بیشتر درباره‌ی فرایند احراز هویت، به
[احراز هویت](/docs/reference/access-authn-authz/authentication/#service-account-tokens) مراجعه کنید.

### احراز هویت اعتبارنامه‌های حساب سرویس در کد خودتان {#authenticating-in-code}

اگر سرویس‌هایی دارید که نیاز دارند اعتبارنامه‌های حساب سرویس کوبرنتیز را اعتبارسنجی کنند، می‌توانید از روش‌های زیر استفاده کنید:

* [TokenReview API](/docs/reference/kubernetes-api/authentication-resources/token-review-v1/)
  (توصیه‌شده)
* OIDC discovery

پروژه‌ی کوبرنتیز استفاده از TokenReview API را توصیه می‌کند، زیرا این روش توکن‌هایی را که به آبجکت‌های API مانند Secretها، ServiceAccountها، Podها یا نودها مقید هستند، هنگام حذف آن آبجکت‌ها باطل می‌کند. برای مثال، اگر Podی را که شامل یک توکن ServiceAccount از نوع projected است حذف کنید، کلاستر بلافاصله آن توکن را باطل می‌کند و TokenReview بلافاصله ناموفق می‌شود. اگر به‌جای آن از اعتبارسنجی OIDC استفاده کنید، کلاینت‌های شما تا رسیدن توکن به زمان انقضای آن، توکن را معتبر در نظر می‌گیرند.

برنامه‌ی شما باید همیشه مخاطبی (audience) را که می‌پذیرد تعریف کند و بررسی کند که مخاطب‌های توکن با مخاطب‌هایی که برنامه انتظار دارد مطابقت دارند. این کار به کمینه کردن دامنه‌ی توکن کمک می‌کند تا فقط در برنامه‌ی شما و هیچ جای دیگری قابل استفاده باشد.

## جایگزین‌ها {#alternatives}

* توکن‌های خودتان را با سازوکار دیگری صادر کنید و سپس از [Webhook Token Authentication](/docs/reference/access-authn-authz/authentication/#webhook-token-authentication) برای اعتبارسنجی توکن‌های bearer با سرویس اعتبارسنجی خودتان استفاده کنید.
* هویت‌های خودتان را برای Podها فراهم کنید.
  * [از افزونه‌ی درایور SPIFFE CSI برای ارائه‌ی SPIFFE SVIDها به‌صورت جفت‌های گواهی X.509 به Podها استفاده کنید](https://cert-manager.io/docs/projects/csi-driver-spiffe/).
    {{% thirdparty-content single="true" %}}
  * [از یک service mesh مانند Istio برای ارائه‌ی گواهی‌ها به Podها استفاده کنید](https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/).
* بدون استفاده از توکن‌های حساب سرویس، از خارج از کلاستر در برابر API server احراز هویت کنید:
  * [API server را طوری پیکربندی کنید که توکن‌های OpenID Connect (OIDC) را از ارائه‌دهنده‌ی هویت شما بپذیرد](/docs/reference/access-authn-authz/authentication/#openid-connect-tokens).
  * از حساب‌های سرویس یا حساب‌های کاربری ایجادشده با استفاده از یک سرویس خارجی مدیریت هویت و دسترسی (IAM)، مانند سرویس یک ارائه‌دهنده‌ی ابری، برای احراز هویت در کلاستر خود استفاده کنید.
  * [از API مربوط به CertificateSigningRequest با گواهی‌های کلاینت استفاده کنید](/docs/tasks/tls/managing-tls-in-a-cluster/).
* [kubelet را طوری پیکربندی کنید که اعتبارنامه‌ها را از یک رجیستری ایمیج دریافت کند](/docs/tasks/administer-cluster/kubelet-credential-provider/).
* از یک Device Plugin برای دسترسی به یک Trusted Platform Module (TPM) مجازی استفاده کنید که سپس احراز هویت با استفاده از یک کلید خصوصی را ممکن می‌کند.

## {{% heading "whatsnext" %}}

* یاد بگیرید چگونه [ServiceAccountهای خود را به‌عنوان مدیر کلاستر مدیریت کنید](/docs/reference/access-authn-authz/service-accounts-admin/).
* یاد بگیرید چگونه [یک ServiceAccount را به یک Pod اختصاص دهید](/docs/tasks/configure-pod-container/configure-service-account/).
* [مرجع API مربوط به ServiceAccount](/docs/reference/kubernetes-api/authentication-resources/service-account-v1/) را مطالعه کنید.
