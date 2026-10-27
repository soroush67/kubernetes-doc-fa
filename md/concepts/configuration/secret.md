---
reviewers:
  - mikedanese
title: Secretها
api_metadata:
- apiVersion: "v1"
  kind: "Secret"
content_type: concept
feature:
  title: مدیریت Secretها و پیکربندی
  description: >
    Secretها و پیکربندی برنامه را بدون بازسازی ایمیج خود
    و بدون افشای Secretها در پیکربندی پشتهٔ خود مستقر و به‌روزرسانی کنید.
weight: 30
---

<!-- overview -->

Secret آبجکتی است که مقدار کمی دادهٔ حساس مانند
گذرواژه، توکن یا کلید را در خود دارد. در غیر این صورت ممکن بود چنین اطلاعاتی در
مشخصات یک {{< glossary_tooltip term_id="pod" >}} یا در یک
{{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} قرار داده شود. استفاده از
Secret به این معناست که نیازی ندارید داده‌های محرمانه را در کد
برنامهٔ خود بگنجانید.

از آنجا که Secretها را می‌توان مستقل از Podهایی که از آن‌ها استفاده می‌کنند ایجاد کرد،
خطر افشای Secret (و داده‌های آن) در طول گردش کار
ایجاد، مشاهده و ویرایش Podها کمتر است. کوبرنتیز و برنامه‌هایی که در
کلاستر شما اجرا می‌شوند نیز می‌توانند احتیاط‌های بیشتری در مورد Secretها به کار گیرند، مانند اجتناب از
نوشتن داده‌های حساس در ذخیره‌سازی غیرفرار.

Secretها مشابه {{< glossary_tooltip text="ConfigMapها" term_id="configmap" >}} هستند،
اما به‌طور خاص برای نگهداری داده‌های محرمانه در نظر گرفته شده‌اند.

{{< caution >}}
Secretهای کوبرنتیز به‌طور پیش‌فرض به‌صورت رمزگذاری‌نشده در ذخیره‌گاه دادهٔ زیربنایی سرور API
(etcd) ذخیره می‌شوند. هر کسی که به API دسترسی داشته باشد می‌تواند یک Secret را بازیابی یا تغییر دهد، و هر کسی که به etcd دسترسی داشته باشد نیز می‌تواند.
افزون بر این، هر کسی که مجاز به ایجاد یک Pod در یک فضای نام باشد می‌تواند از آن دسترسی برای خواندن
هر Secret در آن فضای نام استفاده کند؛ این شامل دسترسی غیرمستقیم مانند توانایی ایجاد یک
Deployment نیز می‌شود.

برای استفادهٔ ایمن از Secretها، دست‌کم گام‌های زیر را بردارید:

1. [رمزگذاری در حالت سکون (Encryption at Rest)](/docs/tasks/administer-cluster/encrypt-data/) را برای Secretها فعال کنید.
1. [قواعد RBAC را فعال یا پیکربندی کنید](/docs/reference/access-authn-authz/authorization/) تا
   دسترسی به Secretها با کمترین سطح امتیاز باشد.
1. دسترسی به Secret را به کانتینرهای مشخص محدود کنید.
1. [استفاده از فراهم‌کنندگان ذخیره‌گاه خارجی Secret را در نظر بگیرید](https://secrets-store-csi-driver.sigs.k8s.io/concepts.html#provider-for-the-secrets-store-csi-driver).

برای رهنمودهای بیشتر دربارهٔ مدیریت و بهبود امنیت Secretهای خود، به
[روش‌های خوب برای Secretهای کوبرنتیز](/docs/concepts/security/secrets-good-practices) مراجعه کنید.

{{< /caution >}}

برای جزئیات بیشتر [امنیت اطلاعات برای Secretها](#information-security-for-secrets) را ببینید.

<!-- body -->

## کاربردهای Secretها

می‌توانید از Secretها برای مقاصدی مانند موارد زیر استفاده کنید:

- [تنظیم متغیرهای محیطی برای یک کانتینر](/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data).
- [فراهم کردن اعتبارنامه‌هایی مانند کلیدهای SSH یا گذرواژه‌ها برای Podها](/docs/tasks/inject-data-application/distribute-credentials-secure/#provide-prod-test-creds).
- [اجازه دادن به kubelet برای دریافت ایمیج‌های کانتینر از رجیستری‌های خصوصی](/docs/tasks/configure-pod-container/pull-image-private-registry/).

control plane کوبرنتیز نیز از Secretها استفاده می‌کند؛ برای نمونه،
[Secretهای توکن راه‌اندازی (bootstrap token)](#bootstrap-token-secrets) سازوکاری برای
کمک به خودکارسازی ثبت نودها هستند.

### مورد کاربرد: dotfileها در یک حجم secret

می‌توانید با تعریف کلیدی که با نقطه آغاز می‌شود داده‌های خود را «پنهان» کنید.
این کلید نمایانگر یک dotfile یا فایل «پنهان» است. برای نمونه، هنگامی که Secret زیر
در حجم `secret-volume` mount شود، این حجم شامل یک فایل منفرد
به نام `.secret-file` خواهد بود و این فایل در کانتینر `dotfile-test-container`
در مسیر `/etc/secret-volume/.secret-file` حاضر خواهد بود.

{{< note >}}
فایل‌هایی که با نویسهٔ نقطه آغاز می‌شوند در خروجی `ls -l` پنهان‌اند؛
برای دیدن آن‌ها هنگام فهرست کردن محتوای دایرکتوری باید از `ls -la` استفاده کنید.
{{< /note >}}

{{% code_sample language="yaml" file="secret/dotfile-secret.yaml" %}}

### مورد کاربرد: Secretای که تنها برای یک کانتینر در Pod قابل مشاهده است

برنامه‌ای را در نظر بگیرید که باید درخواست‌های HTTP را رسیدگی کند، منطق تجاری پیچیده‌ای
را اجرا کند و سپس برخی پیام‌ها را با HMAC امضا کند. از آنجا که این برنامه منطق
پیچیده‌ای دارد، ممکن است یک آسیب‌پذیری خواندن فایل از راه دور به‌صورت ناشناخته در
سرور وجود داشته باشد که بتواند کلید خصوصی را برای مهاجم افشا کند.

می‌توان این برنامه را به دو فرایند در دو کانتینر تقسیم کرد: یک کانتینر frontend
که تعامل با کاربر و منطق تجاری را رسیدگی می‌کند اما نمی‌تواند
کلید خصوصی را ببیند؛ و یک کانتینر امضاکننده که می‌تواند کلید خصوصی را ببیند و به
درخواست‌های امضای ساده از سوی frontend پاسخ می‌دهد (برای نمونه، از طریق شبکهٔ localhost).

با این رویکرد تفکیک‌شده، مهاجم اکنون باید سرور برنامه را فریب دهد
تا کاری نسبتاً دلخواه انجام دهد، که ممکن است دشوارتر از وادار کردن آن
به خواندن یک فایل باشد.

### جایگزین‌های Secretها

به‌جای استفاده از Secret برای محافظت از داده‌های محرمانه، می‌توانید از میان جایگزین‌ها انتخاب کنید.

برخی از گزینه‌های شما عبارت‌اند از:

- اگر جزء بومی ابر شما نیاز دارد نزد برنامهٔ دیگری احراز هویت کند که
  می‌دانید درون همان کلاستر کوبرنتیز اجرا می‌شود، می‌توانید از یک
  [ServiceAccount](/docs/reference/access-authn-authz/authentication/#service-account-tokens)
  و توکن‌های آن برای شناسایی کلاینت خود استفاده کنید.
- ابزارهای شخص ثالثی وجود دارند که می‌توانید آن‌ها را درون یا بیرون از کلاستر خود اجرا کنید
  و داده‌های حساس را مدیریت می‌کنند. برای نمونه، سرویسی که Podها از طریق HTTPS به آن دسترسی پیدا می‌کنند
  و در صورتی که کلاینت به‌درستی احراز هویت کند (برای نمونه، با یک توکن ServiceAccount)
  یک Secret را آشکار می‌کند.
- برای احراز هویت، می‌توانید یک امضاکنندهٔ سفارشی برای گواهی‌های X.509 پیاده‌سازی کنید و از
  [CertificateSigningRequestها](/docs/reference/access-authn-authz/certificate-signing-requests/)
  استفاده کنید تا آن امضاکنندهٔ سفارشی برای Podهایی که به گواهی نیاز دارند گواهی صادر کند.
- می‌توانید از یک [device plugin](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
  برای در اختیار قرار دادن سخت‌افزار رمزگذاری محلیِ نود به یک Pod مشخص استفاده کنید. برای نمونه، می‌توانید
  Podهای مورد اعتماد را روی نودهایی زمان‌بندی کنید که یک Trusted Platform Module دارند که خارج از باند پیکربندی شده است.

همچنین می‌توانید دو یا چند مورد از این گزینه‌ها، از جمله گزینهٔ استفاده از خود آبجکت‌های Secret، را با هم ترکیب کنید.

برای نمونه: یک {{< glossary_tooltip text="اپراتور" term_id="operator-pattern" >}} پیاده‌سازی (یا مستقر) کنید
که توکن‌های نشست کوتاه‌عمر را از یک سرویس خارجی دریافت می‌کند و سپس بر اساس
آن توکن‌های نشست کوتاه‌عمر، Secretهایی ایجاد می‌کند. Podهایی که در کلاستر شما اجرا می‌شوند می‌توانند از توکن‌های نشست استفاده کنند
و اپراتور اطمینان حاصل می‌کند که این توکن‌ها معتبرند. این تفکیک به این معناست که می‌توانید Podهایی را اجرا کنید که از
سازوکارهای دقیق صدور و تازه‌سازی آن توکن‌های نشست آگاه نیستند.

## انواع Secret {#secret-types}

هنگام ایجاد یک Secret، می‌توانید نوع آن را با استفاده از فیلد `type` در
منبع [Secret](/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)،
یا برخی پرچم‌های خط فرمان معادل در `kubectl` (در صورت وجود) مشخص کنید.
نوع Secret برای تسهیل پردازش برنامه‌نویسی‌شدهٔ داده‌های Secret استفاده می‌شود.

کوبرنتیز چندین نوع داخلی برای برخی سناریوهای کاربرد رایج فراهم می‌کند.
این انواع از نظر اعتبارسنجی‌های انجام‌شده و محدودیت‌هایی که
کوبرنتیز بر آن‌ها اعمال می‌کند با یکدیگر تفاوت دارند.

| نوع داخلی                         | کاربرد                                   |
| ------------------------------------- |---------------------------------------- |
| `Opaque`                              | داده‌های دلخواه تعریف‌شده توسط کاربر            |
| `kubernetes.io/service-account-token` | توکن ServiceAccount                    |
| `kubernetes.io/dockercfg`             | فایل سریال‌شدهٔ `~/.dockercfg`          |
| `kubernetes.io/dockerconfigjson`      | فایل سریال‌شدهٔ `~/.docker/config.json` |
| `kubernetes.io/basic-auth`            | اعتبارنامه‌ها برای احراز هویت پایه    |
| `kubernetes.io/ssh-auth`              | اعتبارنامه‌ها برای احراز هویت SSH      |
| `kubernetes.io/tls`                   | داده‌ها برای یک کلاینت یا سرور TLS         |
| `bootstrap.kubernetes.io/token`       | داده‌های توکن راه‌اندازی                    |

می‌توانید با اختصاص یک رشتهٔ غیرخالی به‌عنوان مقدار
`type` برای یک آبجکت Secret، نوع Secret مخصوص خود را تعریف و استفاده کنید (رشتهٔ خالی به‌عنوان نوع `Opaque` در نظر گرفته می‌شود).

کوبرنتیز هیچ محدودیتی بر نام نوع اعمال نمی‌کند. با این حال، اگر
از یکی از انواع داخلی استفاده می‌کنید، باید همهٔ الزامات تعریف‌شده
برای آن نوع را برآورده کنید.

اگر نوعی از Secret را برای استفادهٔ عمومی تعریف می‌کنید، از این قرارداد پیروی کنید
و نوع Secret را طوری ساختار دهید که نام دامنهٔ شما پیش از نام بیاید و با
یک `/` از آن جدا شود. برای نمونه: `cloud-hosting.example.net/cloud-api-credentials`.

### Secretهای Opaque

اگر در مانیفست Secret نوعی را به‌صراحت مشخص نکنید، `Opaque` نوع پیش‌فرض Secret
است. هنگامی که با استفاده از `kubectl` یک Secret ایجاد می‌کنید، باید از
زیرفرمان `generic` برای مشخص کردن نوع Secret از نوع `Opaque` استفاده کنید. برای نمونه،
فرمان زیر یک Secret خالی از نوع `Opaque` ایجاد می‌کند:

```shell
kubectl create secret generic empty-secret
kubectl get secret empty-secret
```

خروجی به این شکل است:

```
NAME           TYPE     DATA   AGE
empty-secret   Opaque   0      2m6s
```

ستون `DATA` تعداد اقلام داده‌ای ذخیره‌شده در Secret را نشان می‌دهد.
در این مورد، `0` به این معناست که یک Secret خالی ایجاد کرده‌اید.

### Secretهای توکن ServiceAccount

Secret از نوع `kubernetes.io/service-account-token` برای ذخیرهٔ
اعتبارنامهٔ توکنی استفاده می‌شود که یک
{{< glossary_tooltip text="ServiceAccount" term_id="service-account" >}} را شناسایی می‌کند. این
یک سازوکار قدیمی (legacy) است که اعتبارنامه‌های بلندمدت ServiceAccount را برای
Podها فراهم می‌کند.

در کوبرنتیز v1.22 و نسخه‌های بعدی، رویکرد توصیه‌شده این است که به‌جای آن یک
توکن ServiceAccount کوتاه‌عمر و با چرخش خودکار را با استفاده از API
[`TokenRequest`](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
دریافت کنید. می‌توانید این توکن‌های کوتاه‌عمر را با روش‌های زیر به دست آورید:

* API `TokenRequest` را یا مستقیماً یا با استفاده از یک کلاینت API مانند
  `kubectl` فراخوانی کنید. برای نمونه، می‌توانید از فرمان
  [`kubectl create token`](/docs/reference/generated/kubectl/kubectl-commands#-em-token-em-)
  استفاده کنید.
* یک توکن mount‌شده را در یک
  [حجم projected](/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume)
  در مانیفست Pod خود درخواست کنید. کوبرنتیز توکن را ایجاد کرده و آن را در Pod mount می‌کند.
  هنگامی که Podی که توکن در آن mount شده حذف شود، توکن به‌طور خودکار
  نامعتبر می‌شود. برای جزئیات،
  [راه‌اندازی یک Pod با استفاده از projection توکن service account](/docs/tasks/configure-pod-container/configure-service-account/#launch-a-pod-using-service-account-token-projection) را ببینید.

{{< note >}}
تنها در صورتی باید یک Secret توکن ServiceAccount ایجاد کنید
که نتوانید از API `TokenRequest` برای دریافت توکن استفاده کنید
و ریسک امنیتی ماندگار کردن یک اعتبارنامهٔ توکن بدون انقضا
در یک آبجکت API قابل خواندن برای شما پذیرفتنی باشد. برای دستورالعمل‌ها،
[ایجاد دستی یک توکن API بلندمدت برای یک ServiceAccount](/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount) را ببینید.
{{< /note >}}

هنگام استفاده از این نوع Secret، باید اطمینان حاصل کنید که
حاشیه‌نویسی `kubernetes.io/service-account.name` روی نام یک
ServiceAccount موجود تنظیم شده باشد. اگر هم ServiceAccount و هم
آبجکت Secret را ایجاد می‌کنید، باید ابتدا آبجکت ServiceAccount را ایجاد کنید.

پس از ایجاد Secret، یک {{< glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller" >}} کوبرنتیز
برخی فیلدهای دیگر مانند حاشیه‌نویسی `kubernetes.io/service-account.uid` و کلید
`token` در فیلد `data` را پر می‌کند که با یک توکن احراز هویت مقداردهی می‌شود.

پیکربندی نمونهٔ زیر یک Secret توکن ServiceAccount را اعلام می‌کند:

{{% code_sample language="yaml" file="secret/serviceaccount-token-secret.yaml" %}}

پس از ایجاد Secret، صبر کنید تا کوبرنتیز کلید `token` را در فیلد `data` مقداردهی کند.

برای اطلاعات بیشتر دربارهٔ نحوهٔ کار ServiceAccountها، مستندات
[ServiceAccount](/docs/concepts/security/service-accounts/) را ببینید.
همچنین می‌توانید فیلد `automountServiceAccountToken` و فیلد
`serviceAccountName` در
[`Pod`](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#pod-v1-core)
را برای اطلاعات دربارهٔ ارجاع به اعتبارنامه‌های ServiceAccount از درون Podها بررسی کنید.

### Secretهای پیکربندی Docker

اگر Secretای برای ذخیرهٔ اعتبارنامه‌های دسترسی به یک رجیستری ایمیج کانتینر ایجاد می‌کنید،
باید یکی از مقادیر `type` زیر را برای آن Secret به کار ببرید:

- `kubernetes.io/dockercfg`: یک `~/.dockercfg` سریال‌شده را ذخیره می‌کند که
  قالب قدیمی برای پیکربندی خط فرمان Docker است. فیلد
  `data` در Secret شامل کلید `.dockercfg` است که مقدار آن محتوای یک
  فایل `~/.dockercfg` کدگذاری‌شده با base64 است.
- `kubernetes.io/dockerconfigjson`: یک JSON سریال‌شده را ذخیره می‌کند که از
  همان قواعد قالب فایل `~/.docker/config.json` پیروی می‌کند، که قالب جدیدی
  برای `~/.dockercfg` است. فیلد `data` در Secret باید شامل کلید
  `.dockerconfigjson` باشد که مقدار آن محتوای یک فایل
  `~/.docker/config.json` کدگذاری‌شده با base64 است.

در زیر نمونه‌ای از Secret از نوع `kubernetes.io/dockercfg` آمده است:

{{% code_sample language="yaml" file="secret/dockercfg-secret.yaml" %}}

{{< note >}}
اگر نمی‌خواهید کدگذاری base64 را انجام دهید، می‌توانید به‌جای آن از
فیلد `stringData` استفاده کنید.
{{< /note >}}

هنگامی که Secretهای پیکربندی Docker را با استفاده از یک مانیفست ایجاد می‌کنید، سرور API
بررسی می‌کند که آیا کلید مورد انتظار در فیلد `data` وجود دارد یا نه، و
تأیید می‌کند که آیا مقدار ارائه‌شده را می‌توان به‌عنوان یک JSON معتبر تجزیه کرد یا نه. سرور API
اعتبارسنجی نمی‌کند که آیا JSON واقعاً یک فایل پیکربندی Docker است یا نه.

همچنین می‌توانید از `kubectl` برای ایجاد یک Secret برای دسترسی به یک
رجیستری کانتینر استفاده کنید، مثلاً هنگامی که فایل پیکربندی Docker ندارید:

```shell
kubectl create secret docker-registry secret-tiger-docker \
  --docker-email=tiger@acme.example \
  --docker-username=tiger \
  --docker-password=pass1234 \
  --docker-server=my-registry.example:5000
```

این فرمان یک Secret از نوع `kubernetes.io/dockerconfigjson` ایجاد می‌کند.

فیلد `.data.dockerconfigjson` را از آن Secret جدید بازیابی کنید و
داده‌ها را رمزگشایی کنید:

```shell
kubectl get secret secret-tiger-docker -o jsonpath='{.data.*}' | base64 -d
```

خروجی معادل سند JSON زیر است (که یک فایل پیکربندی
Docker معتبر نیز هست):

```json
{
  "auths": {
    "my-registry.example:5000": {
      "username": "tiger",
      "password": "pass1234",
      "email": "tiger@acme.example",
      "auth": "dGlnZXI6cGFzczEyMzQ="
    }
  }
}
```

{{< caution >}}
مقدار `auth` در آنجا با base64 کدگذاری شده است؛ مبهم شده اما محرمانه نیست.
هر کسی که بتواند آن Secret را بخواند می‌تواند توکن bearer دسترسی به رجیستری را به دست آورد.

پیشنهاد می‌شود از [فراهم‌کنندگان اعتبارنامه (credential providers)](/docs/tasks/administer-cluster/kubelet-credential-provider/) برای فراهم کردن پویا و ایمن pull secretها در صورت نیاز استفاده کنید.
{{< /caution >}}

### Secret احراز هویت پایه

نوع `kubernetes.io/basic-auth` برای ذخیرهٔ اعتبارنامه‌های لازم
برای احراز هویت پایه فراهم شده است. هنگام استفاده از این نوع Secret، فیلد `data` در
Secret باید شامل یکی از دو کلید زیر باشد:

- `username`: نام کاربری برای احراز هویت
- `password`: گذرواژه یا توکن برای احراز هویت

هر دو مقدار دو کلید بالا رشته‌هایی کدگذاری‌شده با base64 هستند. به‌عنوان
جایگزین، می‌توانید محتوای متن ساده را با استفاده از فیلد `stringData` در
مانیفست Secret ارائه کنید.

مانیفست زیر نمونه‌ای از یک Secret احراز هویت پایه است:

{{% code_sample language="yaml" file="secret/basicauth-secret.yaml" %}}

{{< note >}}
فیلد `stringData` برای یک Secret با server-side apply به‌خوبی کار نمی‌کند.
{{< /note >}}

نوع Secret احراز هویت پایه تنها برای راحتی فراهم شده است.
می‌توانید برای اعتبارنامه‌های مورد استفاده در احراز هویت پایه از نوع `Opaque` استفاده کنید.
با این حال، استفاده از نوع Secret تعریف‌شده و عمومی (`kubernetes.io/basic-auth`) به دیگران
کمک می‌کند هدف Secret شما را درک کنند و قراردادی برای اینکه چه نام‌های کلیدی
مورد انتظار است تعیین می‌کند.

### Secretهای احراز هویت SSH

نوع داخلی `kubernetes.io/ssh-auth` برای ذخیرهٔ داده‌های مورد استفاده در
احراز هویت SSH فراهم شده است. هنگام استفاده از این نوع Secret، باید یک
جفت کلید-مقدار `ssh-privatekey` را در فیلد `data` (یا `stringData`)
به‌عنوان اعتبارنامهٔ SSH مورد استفاده مشخص کنید.

مانیفست زیر نمونه‌ای از Secretای است که برای احراز هویت با کلید عمومی/خصوصی
SSH استفاده می‌شود:

{{% code_sample language="yaml" file="secret/ssh-auth-secret.yaml" %}}

نوع Secret احراز هویت SSH تنها برای راحتی فراهم شده است.
می‌توانید برای اعتبارنامه‌های مورد استفاده در احراز هویت SSH از نوع `Opaque` استفاده کنید.
با این حال، استفاده از نوع Secret تعریف‌شده و عمومی (`kubernetes.io/ssh-auth`) به دیگران
کمک می‌کند هدف Secret شما را درک کنند و قراردادی برای اینکه چه نام‌های کلیدی
مورد انتظار است تعیین می‌کند.
API کوبرنتیز تأیید می‌کند که کلیدهای الزامی برای Secretای از این نوع تنظیم شده باشند.

{{< caution >}}
کلیدهای خصوصی SSH به‌تنهایی ارتباط مورد اعتمادی میان کلاینت SSH و
سرور میزبان برقرار نمی‌کنند. برای کاهش حملات «مرد میانی» (man in the middle) به ابزار دیگری برای برقراری اعتماد
نیاز است، مانند فایل `known_hosts` که به یک ConfigMap اضافه شده باشد.
{{< /caution >}}

### Secretهای TLS

نوع Secret با نام `kubernetes.io/tls` برای ذخیرهٔ
یک گواهی و کلید مرتبط با آن است که معمولاً برای TLS استفاده می‌شوند.

یکی از کاربردهای رایج Secretهای TLS پیکربندی رمزگذاری در حین انتقال برای
یک [Ingress](/docs/concepts/services-networking/ingress/) است، اما می‌توانید از آن
با منابع دیگر یا مستقیماً در بار کاری خود نیز استفاده کنید.
هنگام استفاده از این نوع Secret، کلیدهای `tls.key` و `tls.crt` باید
در فیلد `data` (یا `stringData`) پیکربندی Secret ارائه شوند، هرچند سرور API
در واقع مقادیر هر کلید را اعتبارسنجی نمی‌کند.

به‌عنوان جایگزینی برای استفاده از `stringData`، می‌توانید از فیلد `data` برای ارائهٔ
گواهی و کلید خصوصی کدگذاری‌شده با base64 استفاده کنید. برای جزئیات،
[محدودیت‌های نام‌ها و داده‌های Secret](#restriction-names-data) را ببینید.

YAML زیر شامل یک پیکربندی نمونه برای یک Secret TLS است:

{{% code_sample language="yaml" file="secret/tls-auth-secret.yaml" %}}

نوع Secret TLS تنها برای راحتی فراهم شده است.
می‌توانید برای اعتبارنامه‌های مورد استفاده در احراز هویت TLS از نوع `Opaque` استفاده کنید.
با این حال، استفاده از نوع Secret تعریف‌شده و عمومی (`kubernetes.io/tls`)
به تضمین یکپارچگی قالب Secret در پروژهٔ شما کمک می‌کند. سرور API
تأیید می‌کند که کلیدهای الزامی برای Secretای از این نوع تنظیم شده باشند.

برای ایجاد یک Secret TLS با استفاده از `kubectl`، از زیرفرمان `tls` استفاده کنید:

```shell
kubectl create secret tls my-tls-secret \
  --cert=path/to/cert/file \
  --key=path/to/key/file
```

جفت کلید عمومی/خصوصی باید از پیش وجود داشته باشد. گواهی کلید عمومی برای `--cert` باید با قالب .PEM کدگذاری شده باشد
و باید با کلید خصوصی داده‌شده برای `--key` مطابقت داشته باشد.

### Secretهای توکن راه‌اندازی (Bootstrap token)

نوع Secret با نام `bootstrap.kubernetes.io/token` برای
توکن‌هایی است که در فرایند راه‌اندازی نود استفاده می‌شوند. این نوع، توکن‌هایی را ذخیره می‌کند که برای امضای
ConfigMapهای شناخته‌شده استفاده می‌شوند.

یک Secret توکن راه‌اندازی معمولاً در فضای نام `kube-system` ایجاد می‌شود و
به شکل `bootstrap-token-<token-id>` نام‌گذاری می‌شود که در آن `<token-id>` رشته‌ای
۶ نویسه‌ای از شناسهٔ توکن است.

به‌عنوان یک مانیفست کوبرنتیز، یک Secret توکن راه‌اندازی ممکن است به شکل
زیر باشد:

{{% code_sample language="yaml" file="secret/bootstrap-token-secret-base64.yaml" %}}

یک Secret توکن راه‌اندازی کلیدهای زیر را زیر `data` مشخص می‌کند:

- `token-id`: رشته‌ای تصادفی ۶ نویسه‌ای به‌عنوان شناسهٔ توکن. الزامی.
- `token-secret`: رشته‌ای تصادفی ۱۶ نویسه‌ای به‌عنوان Secret واقعی توکن. الزامی.
- `description`: رشته‌ای خوانا برای انسان که توضیح می‌دهد توکن
  برای چه منظوری استفاده می‌شود. اختیاری.
- `expiration`: یک زمان مطلق UTC با استفاده از [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339) که مشخص می‌کند توکن
  چه زمانی باید منقضی شود. اختیاری.
- `usage-bootstrap-<usage>`: یک پرچم بولی که کاربرد اضافی‌ای را برای
  توکن راه‌اندازی نشان می‌دهد.
- `auth-extra-groups`: فهرستی جداشده با ویرگول از نام‌های گروه‌هایی که
  علاوه بر گروه `system:bootstrappers`، احراز هویت به‌عنوان آن‌ها انجام خواهد شد.

به‌عنوان جایگزین، می‌توانید مقادیر را در فیلد `stringData` در Secret
بدون کدگذاری base64 ارائه کنید:

{{% code_sample language="yaml" file="secret/bootstrap-token-secret-literal.yaml" %}}

{{< note >}}
فیلد `stringData` برای یک Secret با server-side apply به‌خوبی کار نمی‌کند.
{{< /note >}}

## کار با Secretها

### ایجاد یک Secret

برای ایجاد یک Secret چندین گزینه وجود دارد:

- [استفاده از `kubectl`](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
- [استفاده از یک فایل پیکربندی](/docs/tasks/configmap-secret/managing-secret-using-config-file/)
- [استفاده از ابزار Kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/)

#### محدودیت‌های نام‌ها و داده‌های Secret {#restriction-names-data}

نام یک آبجکت Secret باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

هنگام ایجاد فایل پیکربندی برای یک Secret می‌توانید فیلد `data` و/یا `stringData`
را مشخص کنید. فیلدهای `data` و `stringData` اختیاری‌اند.
مقادیر همهٔ کلیدها در فیلد `data` باید رشته‌هایی کدگذاری‌شده با base64 باشند.
اگر تبدیل به رشتهٔ base64 مطلوب نیست، می‌توانید به‌جای آن فیلد
`stringData` را مشخص کنید که رشته‌های دلخواه را به‌عنوان مقدار می‌پذیرد.

کلیدهای `data` و `stringData` باید از نویسه‌های الفبایی-عددی،
`-`، `_` یا `.` تشکیل شده باشند. همهٔ جفت‌های کلید-مقدار در فیلد `stringData` به‌صورت داخلی
در فیلد `data` ادغام می‌شوند. اگر کلیدی هم در فیلد `data` و هم در
فیلد `stringData` ظاهر شود، مقدار مشخص‌شده در فیلد `stringData`
اولویت دارد.

#### حد اندازه {#restriction-data-size}

اندازهٔ هر Secret منفرد به 1MiB محدود است. این محدودیت برای جلوگیری از ایجاد
Secretهای بسیار بزرگ است که می‌توانند حافظهٔ سرور API و kubelet را تمام کنند.
با این حال، ایجاد تعداد زیادی Secret کوچک‌تر نیز می‌تواند حافظه را تمام کند. می‌توانید
از یک [سهمیهٔ منابع](/docs/concepts/policy/resource-quotas/) برای محدود کردن
تعداد Secretها (یا منابع دیگر) در یک فضای نام استفاده کنید.

### ویرایش یک Secret

می‌توانید یک Secret موجود را ویرایش کنید، مگر آنکه [تغییرناپذیر](#secret-immutable) باشد. برای
ویرایش یک Secret، از یکی از روش‌های زیر استفاده کنید:

- [استفاده از `kubectl`](/docs/tasks/configmap-secret/managing-secret-using-kubectl/#edit-secret)
- [استفاده از یک فایل پیکربندی](/docs/tasks/configmap-secret/managing-secret-using-config-file/#edit-secret)

همچنین می‌توانید داده‌های یک Secret را با استفاده از [ابزار Kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/#edit-secret) ویرایش کنید. با این حال، این
روش یک آبجکت `Secret` جدید با داده‌های ویرایش‌شده ایجاد می‌کند.

بسته به اینکه Secret را چگونه ایجاد کرده‌اید و Secret در
Podهای شما چگونه استفاده می‌شود، به‌روزرسانی‌های آبجکت‌های `Secret` موجود به‌طور خودکار به
Podهایی که از داده‌ها استفاده می‌کنند منتشر می‌شوند. برای اطلاعات بیشتر، به بخش [استفاده از Secretها به‌صورت فایل در یک Pod](#using-secrets-as-files-from-a-pod) مراجعه کنید.

### استفاده از یک Secret

Secretها را می‌توان به‌عنوان حجم‌های داده mount کرد یا به‌صورت
{{< glossary_tooltip text="متغیرهای محیطی" term_id="container-env-variables" >}}
در اختیار گذاشت تا توسط یک کانتینر در Pod استفاده شوند. Secretها را همچنین می‌توان توسط سایر بخش‌های
سیستم، بدون آنکه مستقیماً در اختیار Pod قرار گیرند، استفاده کرد. برای نمونه، Secretها می‌توانند
اعتبارنامه‌هایی را نگه دارند که سایر بخش‌های سیستم باید برای تعامل با سیستم‌های
خارجی از طرف شما استفاده کنند.

منابع حجم Secret اعتبارسنجی می‌شوند تا اطمینان حاصل شود که ارجاع آبجکت مشخص‌شده
واقعاً به آبجکتی از نوع Secret اشاره می‌کند. بنابراین، یک Secret
باید پیش از هر Podی که به آن وابسته است ایجاد شود.

اگر Secret قابل دریافت نباشد (شاید به این دلیل که وجود ندارد، یا
به دلیل قطع موقت ارتباط با سرور API)، kubelet
به‌طور دوره‌ای اجرای آن Pod را دوباره تلاش می‌کند. kubelet همچنین یک Event
برای آن Pod گزارش می‌کند که شامل جزئیات مشکل دریافت Secret است.

#### Secretهای اختیاری {#restriction-secret-must-exist}

هنگامی که در یک Pod به یک Secret ارجاع می‌دهید، می‌توانید Secret را _اختیاری_ علامت‌گذاری کنید،
مانند مثال زیر. اگر یک Secret اختیاری وجود نداشته باشد،
کوبرنتیز آن را نادیده می‌گیرد.

{{% code_sample language="yaml" file="secret/optional-secret.yaml" %}}

به‌طور پیش‌فرض، Secretها الزامی‌اند. هیچ‌یک از کانتینرهای یک Pod آغاز نمی‌شوند تا زمانی که
همهٔ Secretهای غیراختیاری در دسترس باشند.

اگر یک Pod به کلید مشخصی در یک Secret غیراختیاری ارجاع دهد و آن Secret
وجود داشته باشد اما کلید نام‌برده را نداشته باشد، Pod در حین راه‌اندازی با شکست مواجه می‌شود.

### استفاده از Secretها به‌صورت فایل در یک Pod {#using-secrets-as-files-from-a-pod}

اگر می‌خواهید در یک Pod به داده‌های یک Secret دسترسی داشته باشید، یکی از راه‌ها این است که
کوبرنتیز مقدار آن Secret را به‌صورت فایلی درون
سیستم فایل یک یا چند کانتینر Pod در دسترس قرار دهد.

برای دستورالعمل‌ها، به
[ایجاد یک Pod که از طریق یک Volume به داده‌های secret دسترسی دارد](/docs/tasks/inject-data-application/distribute-credentials-secure/#create-a-pod-that-has-access-to-the-secret-data-through-a-volume) مراجعه کنید.

هنگامی که یک حجم حاوی داده‌های یک Secret باشد و آن Secret به‌روزرسانی شود، کوبرنتیز
این تغییر را ردگیری می‌کند و داده‌های حجم را با رویکردی مبتنی بر سازگاری نهایی (eventually-consistent) به‌روزرسانی می‌کند.

{{< note >}}
کانتینری که از یک Secret به‌صورت mount حجم
[subPath](/docs/concepts/storage/volumes#using-subpath) استفاده می‌کند،
به‌روزرسانی‌های خودکار Secret را دریافت نمی‌کند.
{{< /note >}}

kubelet حافظهٔ نهانی از کلیدها و مقادیر جاری Secretهایی که در
حجم‌های Podهای آن نود استفاده می‌شوند نگه می‌دارد.
می‌توانید شیوه‌ای را که kubelet تغییرات نسبت به مقادیر ذخیره‌شده در حافظهٔ نهان را تشخیص می‌دهد پیکربندی کنید. فیلد
`configMapAndSecretChangeDetectionStrategy` در
[پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/) کنترل می‌کند
که kubelet از کدام راهبرد استفاده کند. راهبرد پیش‌فرض `Watch` است.

به‌روزرسانی‌های Secretها می‌توانند از طریق سازوکار watch در API (پیش‌فرض)، بر پایهٔ
یک حافظهٔ نهان با زمان ماندگاری (time-to-live) تعریف‌شده، یا با پرس‌وجوی دوره‌ای از سرور API کلاستر در هر
حلقهٔ همگام‌سازی kubelet منتشر شوند.

در نتیجه، کل تأخیر از لحظه‌ای که Secret به‌روزرسانی می‌شود تا لحظه‌ای
که کلیدهای جدید در Pod project می‌شوند می‌تواند به اندازهٔ دورهٔ همگام‌سازی kubelet به‌علاوهٔ تأخیر
انتشار حافظهٔ نهان باشد، که تأخیر انتشار حافظهٔ نهان به نوع حافظهٔ نهان انتخاب‌شده بستگی دارد
(به همان ترتیبی که در پاراگراف قبل آمد، این مقادیر عبارت‌اند از:
تأخیر انتشار watch، TTL پیکربندی‌شدهٔ حافظهٔ نهان، یا صفر برای پرس‌وجوی مستقیم).

### استفاده از Secretها به‌صورت متغیرهای محیطی

برای استفاده از یک Secret در یک {{< glossary_tooltip text="متغیر محیطی" term_id="container-env-variables" >}}
در یک Pod:

1. برای هر کانتینر در مشخصات Pod خود، به ازای هر کلید Secret که می‌خواهید استفاده کنید
   یک متغیر محیطی به فیلد
   `env[].valueFrom.secretKeyRef` اضافه کنید.
1. ایمیج و/یا خط فرمان خود را طوری تغییر دهید که برنامه مقادیر را
   در متغیرهای محیطی مشخص‌شده جست‌وجو کند.

برای دستورالعمل‌ها، به
[تعریف متغیرهای محیطی کانتینر با استفاده از داده‌های Secret](/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data) مراجعه کنید.

توجه به این نکته مهم است که بازهٔ نویسه‌های مجاز برای نام متغیرهای محیطی
در Podها [محدود](/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) است.
اگر کلیدهایی با این قواعد مطابقت نداشته باشند، آن کلیدها در اختیار کانتینر شما قرار نمی‌گیرند،
هرچند Pod اجازهٔ آغاز به کار دارد.

### Secretهای دریافت ایمیج کانتینر {#using-imagepullsecrets}

اگر می‌خواهید ایمیج‌های کانتینر را از یک مخزن خصوصی دریافت کنید، به راهی نیاز دارید تا
kubelet روی هر نود بتواند نزد آن مخزن احراز هویت کند. می‌توانید
_Secretهای دریافت ایمیج (image pull Secrets)_ را برای ممکن ساختن این کار پیکربندی کنید. این Secretها در سطح Pod
پیکربندی می‌شوند.

#### استفاده از imagePullSecrets

فیلد `imagePullSecrets` فهرستی از ارجاع‌ها به Secretهای موجود در همان فضای نام است.
می‌توانید از `imagePullSecrets` برای ارسال Secretای که حاوی گذرواژهٔ رجیستری ایمیج Docker (یا دیگر رجیستری‌ها) است
به kubelet استفاده کنید. kubelet از این اطلاعات برای دریافت یک ایمیج خصوصی از طرف Pod شما استفاده می‌کند.
برای اطلاعات بیشتر دربارهٔ فیلد `imagePullSecrets`،
[PodSpec API](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) را ببینید.

##### مشخص کردن دستی یک imagePullSecret

می‌توانید نحوهٔ مشخص کردن `imagePullSecrets` را از مستندات
[ایمیج‌های کانتینر](/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod)
بیاموزید.

##### ترتیب دادن پیوست خودکار imagePullSecrets

می‌توانید `imagePullSecrets` را به‌صورت دستی ایجاد کنید و از یک ServiceAccount به آن‌ها ارجاع دهید. فیلد
`imagePullSecrets` هر Podی که با آن ServiceAccount یا به‌طور پیش‌فرض با آن ServiceAccount ایجاد شود،
روی مقدار مربوط به آن service account تنظیم خواهد شد.
برای توضیح تفصیلی این فرایند،
[افزودن ImagePullSecrets به یک service account](/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account) را ببینید.

### استفاده از Secretها با Podهای ایستا {#restriction-static-pod}

نمی‌توانید از ConfigMapها یا Secretها با {{< glossary_tooltip text="Podهای ایستا" term_id="static-pod" >}} استفاده کنید.

## Secretهای تغییرناپذیر {#secret-immutable}

{{< feature-state for_k8s_version="v1.21" state="stable" >}}

کوبرنتیز به شما امکان می‌دهد Secretهای (و ConfigMapهای) مشخصی را _تغییرناپذیر_ علامت‌گذاری کنید.
جلوگیری از تغییر داده‌های یک Secret موجود مزایای زیر را دارد:

- شما را از به‌روزرسانی‌های تصادفی (یا ناخواسته) که ممکن است باعث از کار افتادن برنامه‌ها شوند محافظت می‌کند
- (برای کلاسترهایی که به‌طور گسترده از Secretها استفاده می‌کنند - دست‌کم ده‌ها هزار mount یکتای Secret
  به Pod)، تغییر به Secretهای تغییرناپذیر با کاهش چشمگیر بار روی kube-apiserver
  کارایی کلاستر شما را بهبود می‌بخشد. kubelet نیازی ندارد برای Secretهایی که
  به‌عنوان تغییرناپذیر علامت‌گذاری شده‌اند یک [watch] نگه دارد.

### علامت‌گذاری یک Secret به‌عنوان تغییرناپذیر {#secret-immutable-create}

می‌توانید با تنظیم فیلد `immutable` روی `true` یک Secret تغییرناپذیر ایجاد کنید. برای نمونه،

```yaml
apiVersion: v1
kind: Secret
metadata: ...
data: ...
immutable: true
```

همچنین می‌توانید هر Secret تغییرپذیر موجود را به‌روزرسانی کنید تا تغییرناپذیر شود.

{{< note >}}
هنگامی که یک Secret یا ConfigMap به‌عنوان تغییرناپذیر علامت‌گذاری شود، بازگرداندن این تغییر
یا تغییر محتوای فیلد `data` _ممکن نیست_. تنها می‌توانید Secret را حذف و دوباره ایجاد کنید.
Podهای موجود نقطهٔ mount به Secret حذف‌شده را حفظ می‌کنند - توصیه می‌شود
این Podها را دوباره ایجاد کنید.
{{< /note >}}

## امنیت اطلاعات برای Secretها

اگرچه ConfigMap و Secret به شیوه‌ای مشابه کار می‌کنند، کوبرنتیز برخی محافظت‌های
اضافی را برای آبجکت‌های Secret اعمال می‌کند.

Secretها اغلب مقادیری را نگه می‌دارند که طیفی از اهمیت را در بر می‌گیرند و بسیاری از آن‌ها می‌توانند
باعث ارتقای سطح دسترسی درون کوبرنتیز (مانند توکن‌های service account) و در
سیستم‌های خارجی شوند. حتی اگر یک برنامهٔ منفرد بتواند دربارهٔ قدرت
Secretهایی که انتظار تعامل با آن‌ها را دارد استدلال کند، برنامه‌های دیگر درون همان فضای نام می‌توانند
آن فرض‌ها را نامعتبر سازند.

پیکربندی مجوزدهی بر نحوهٔ دسترسی به داده‌های Secret درون یک فضای نام تأثیر می‌گذارد.
برای نمونه، اعطای مجوزهای **list** یا **watch** روی Secretها به یک سوژه (subject) اجازه می‌دهد
همهٔ داده‌های Secret در آن فضای نام را بخواند، نه فقط Secretهایی که به‌صراحت
توسط Podهای آن ارجاع داده شده‌اند. دسترسی را به حداقل مجموعهٔ مجوزهای
لازم برای کارکرد یک بار کاری محدود کنید و از اعطای نقش‌های گسترده‌ای مانند
`cluster-admin` اجتناب کنید، مگر آنکه برای مقاصد مدیریتی لازم باشد.

همچنین [مستندات مجوزدهی](/docs/reference/access-authn-authz/rbac/) را ببینید.

یک Secret تنها در صورتی به یک نود ارسال می‌شود که Podی روی آن نود به آن نیاز داشته باشد.
برای mount کردن Secretها در Podها، kubelet نسخه‌ای از داده‌ها را در یک `tmpfs` ذخیره می‌کند
تا داده‌های محرمانه در ذخیره‌سازی ماندگار نوشته نشوند.
هنگامی که Podی که به Secret وابسته است حذف شود، kubelet نسخهٔ محلی خود
از داده‌های محرمانهٔ Secret را حذف می‌کند.

ممکن است چندین کانتینر در یک Pod وجود داشته باشد. به‌طور پیش‌فرض، کانتینرهایی که تعریف می‌کنید
تنها به ServiceAccount پیش‌فرض و Secret مرتبط با آن دسترسی دارند.
برای فراهم کردن دسترسی به هر Secret دیگری، باید به‌صراحت متغیرهای محیطی تعریف کنید یا یک حجم را در
کانتینر نگاشت کنید.

ممکن است Secretهایی برای چندین Pod روی یک نود وجود داشته باشد. با این حال، تنها
Secretهایی که یک Pod درخواست می‌کند به‌طور بالقوه درون کانتینرهای آن قابل مشاهده‌اند.
بنابراین، یک Pod به Secretهای Pod دیگر دسترسی ندارد.

### پیکربندی دسترسی با کمترین سطح امتیاز به Secretها

برای تقویت تدابیر امنیتی پیرامون Secretها، از فضاهای نام جداگانه برای جداسازی دسترسی به secretهای mount‌شده استفاده کنید.

{{< warning >}}
هر کانتینری که با `privileged: true` روی یک نود اجرا شود می‌تواند به همهٔ
Secretهای مورد استفاده روی آن نود دسترسی داشته باشد.
{{< /warning >}}

## {{% heading "whatsnext" %}}

- برای رهنمودهای مدیریت و بهبود امنیت Secretهای خود، به
  [روش‌های خوب برای Secretهای کوبرنتیز](/docs/concepts/security/secrets-good-practices) مراجعه کنید.
- بیاموزید که چگونه [Secretها را با استفاده از `kubectl` مدیریت کنید](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
- بیاموزید که چگونه [Secretها را با استفاده از فایل پیکربندی مدیریت کنید](/docs/tasks/configmap-secret/managing-secret-using-config-file/)
- بیاموزید که چگونه [Secretها را با استفاده از kustomize مدیریت کنید](/docs/tasks/configmap-secret/managing-secret-using-kustomize/)
- [مرجع API](/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/) مربوط به `Secret` را بخوانید
