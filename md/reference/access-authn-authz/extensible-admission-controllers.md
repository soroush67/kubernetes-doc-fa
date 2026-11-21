---
reviewers:
- smarterclayton
- lavalamp
- caesarxuchao
- deads2k
- liggitt
- jpbetz
title: کنترل پذیرش پویا
content_type: concept
weight: 45
---

<!-- overview -->
علاوه بر [افزونه‌های پذیرش کامپایل‌شده در کد](/docs/reference/access-authn-authz/admission-controllers/)،
می‌توان افزونه‌های پذیرش (admission plugins) را به‌صورت افزونه‌های جانبی توسعه داد و آن‌ها را
به شکل وب‌هوک‌هایی اجرا کرد که در زمان اجرا پیکربندی می‌شوند.
این صفحه چگونگی ساخت، پیکربندی، استفاده و پایش وب‌هوک‌های پذیرش را شرح می‌دهد.

<!-- body -->

## وب‌هوک‌های پذیرش چه هستند؟

وب‌هوک‌های پذیرش (admission webhooks) فراخوانی‌های بازگشتی HTTP هستند که درخواست‌های پذیرش را
دریافت می‌کنند و کاری روی آن‌ها انجام می‌دهند. می‌توانید دو نوع وب‌هوک پذیرش تعریف کنید:
[وب‌هوک پذیرش اعتبارسنج](/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)
و
[وب‌هوک پذیرش تغییردهنده](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook).
ابتدا وب‌هوک‌های پذیرش تغییردهنده فراخوانی می‌شوند و می‌توانند آبجکت‌های ارسال‌شده به API server را
برای اعمال مقادیر پیش‌فرض سفارشی تغییر دهند. پس از پایان همه‌ی تغییرات آبجکت و پس از آنکه
API server آبجکت ورودی را اعتبارسنجی کرد، وب‌هوک‌های پذیرش اعتبارسنج فراخوانی می‌شوند و
می‌توانند برای اعمال سیاست‌های سفارشی، درخواست‌ها را رد کنند.

{{< note >}}
وب‌هوک‌های پذیرشی که برای اعمال سیاست باید مطمئن باشند وضعیت نهایی آبجکت را می‌بینند،
باید از وب‌هوک پذیرش اعتبارسنج استفاده کنند؛ زیرا آبجکت‌ها ممکن است پس از دیده‌شدن
به‌دست وب‌هوک‌های تغییردهنده، باز هم تغییر کنند.
{{< /note >}}

## آزمودن وب‌هوک‌های پذیرش

وب‌هوک‌های پذیرش در اصل بخشی از control plane کلاستر هستند. بنابراین باید آن‌ها را با
احتیاط بسیار بنویسید و مستقر کنید. اگر قصد نوشتن یا استقرار وب‌هوک‌های پذیرش در سطح محیط
عملیاتی را دارید، لطفاً
[راهنماهای کاربر](/docs/reference/access-authn-authz/extensible-admission-controllers/#write-an-admission-webhook-server)
را مطالعه کنید. در ادامه، روش آزمودن سریع وب‌هوک‌های پذیرش را شرح می‌دهیم.

### پیش‌نیازها

* مطمئن شوید که کنترل‌کننده‌های پذیرش MutatingAdmissionWebhook و ValidatingAdmissionWebhook
  فعال هستند.
  [در این بخش](/docs/reference/access-authn-authz/admission-controllers/#is-there-a-recommended-set-of-admission-controllers-to-use)
  مجموعه‌ای پیشنهادی از کنترل‌کننده‌های پذیرش آمده است که به‌طور کلی فعال‌کردن آن‌ها توصیه می‌شود.

* مطمئن شوید که API ‏`admissionregistration.k8s.io/v1` فعال است.

### نوشتن سرور وب‌هوک پذیرش

لطفاً به پیاده‌سازی [سرور وب‌هوک پذیرش](https://github.com/kubernetes/kubernetes/blob/release-1.21/test/images/agnhost/webhook/main.go)
مراجعه کنید که در یکی از آزمون‌های e2e کوبرنتیز اعتبارسنجی شده است. این وب‌هوک درخواست
`AdmissionReview` ارسال‌شده از سوی API serverها را پردازش می‌کند و تصمیم خود را در قالب یک آبجکت
`AdmissionReview` با همان نسخه‌ای که دریافت کرده بود، بازمی‌گرداند.

برای جزئیات داده‌هایی که به وب‌هوک‌ها ارسال می‌شود، بخش [درخواست وب‌هوک](#request) را ببینید.

برای داده‌هایی که از وب‌هوک‌ها انتظار می‌رود، بخش [پاسخ وب‌هوک](#response) را ببینید.

در سرور وب‌هوک پذیرش نمونه، فیلد `ClientAuth`
[خالی](https://github.com/kubernetes/kubernetes/blob/v1.22.0/test/images/agnhost/webhook/config.go#L38-L39)
رها شده است که مقدار پیش‌فرض آن `NoClientCert` است. یعنی سرور وب‌هوک هویت کلاینت‌ها را که
قاعدتاً API serverها هستند، احراز نمی‌کند. اگر به TLS دوطرفه یا روش‌های دیگری برای احراز هویت
کلاینت‌ها نیاز دارید، بخش [احراز هویت API serverها](#authenticate-apiservers) را ببینید.

### استقرار سرویس وب‌هوک پذیرش

سرور وب‌هوک در آزمون e2e با استفاده از
[API مربوط به Deployment](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#deployment-v1-apps)
در کلاستر کوبرنتیز مستقر می‌شود. این آزمون همچنین یک
[Service](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#service-v1-core)
به‌عنوان واسط جلویی سرور وب‌هوک ایجاد می‌کند.
[کد](https://github.com/kubernetes/kubernetes/blob/v1.22.0/test/e2e/apimachinery/webhook.go#L748)
را ببینید.

همچنین می‌توانید وب‌هوک‌های خود را بیرون از کلاستر مستقر کنید. در این صورت باید پیکربندی
وب‌هوک‌های خود را متناسب با آن به‌روزرسانی کنید.

### پیکربندی پویای وب‌هوک‌های پذیرش

می‌توانید به‌صورت پویا تعیین کنید که چه منابعی تحت پوشش چه وب‌هوک‌های پذیرشی باشند. این کار با
[ValidatingWebhookConfiguration](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#validatingwebhookconfiguration-v1-admissionregistration-k8s-io)
یا
[MutatingWebhookConfiguration](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#mutatingwebhookconfiguration-v1-admissionregistration-k8s-io)
انجام می‌شود.

در ادامه نمونه‌ای از یک `ValidatingWebhookConfiguration` آمده است؛ پیکربندی وب‌هوک تغییردهنده نیز
مشابه آن است. برای جزئیات هر فیلد پیکربندی، بخش [پیکربندی وب‌هوک](#webhook-configuration) را ببینید.

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: "pod-policy.example.com"
webhooks:
- name: "pod-policy.example.com"
  rules:
  - apiGroups:   [""]
    apiVersions: ["v1"]
    operations:  ["CREATE"]
    resources:   ["pods"]
    scope:       "Namespaced"
  clientConfig:
    service:
      namespace: "example-namespace"
      name: "example-service"
    caBundle: <CA_BUNDLE>
  admissionReviewVersions: ["v1"]
  sideEffects: None
  timeoutSeconds: 5
```

{{< note >}}
باید `<CA_BUNDLE>` را در نمونه‌ی بالا با یک بسته‌ی CA معتبر جایگزین کنید. این بسته‌ی CA باید
با کدگذاری PEM باشد (مقدار فیلد با Base64 کدگذاری می‌شود) و برای اعتبارسنجی گواهی سرور وب‌هوک
به کار می‌رود.
{{< /note >}}

فیلد `scope` مشخص می‌کند که آیا فقط منابع در سطح کلاستر ("Cluster") یا فقط منابع در سطح
فضای نام (namespace) ‏("Namespaced") با این قاعده تطبیق داده شوند. مقدار "&lowast;" به این معناست
که هیچ محدودیتی از نظر دامنه وجود ندارد.

{{< note >}}
هنگام استفاده از `clientConfig.service`، گواهی سرور باید برای
`<svc_name>.<svc_namespace>.svc` معتبر باشد.
{{< /note >}}

{{< note >}}
مهلت زمانی پیش‌فرض برای فراخوانی یک وب‌هوک ۱۰ ثانیه است.
می‌توانید `timeout` را تنظیم کنید و توصیه می‌شود برای وب‌هوک‌ها مهلت زمانی کوتاهی در نظر بگیرید.
اگر مهلت فراخوانی وب‌هوک به پایان برسد، درخواست بر اساس سیاست خرابی (failure policy) وب‌هوک
رسیدگی می‌شود.
{{< /note >}}

هنگامی که API server درخواستی دریافت می‌کند که با یکی از `rules` تطبیق دارد، یک درخواست
`admissionReview` را به وب‌هوکی که در `clientConfig` مشخص شده است ارسال می‌کند.

پس از ایجاد پیکربندی وب‌هوک، چند ثانیه طول می‌کشد تا سیستم پیکربندی جدید را اعمال کند.

### احراز هویت API serverها   {#authenticate-apiservers}

اگر وب‌هوک‌های پذیرش شما به احراز هویت نیاز دارند، می‌توانید API serverها را طوری پیکربندی کنید
که برای احراز هویت خود نزد وب‌هوک‌ها از احراز هویت پایه (basic auth)، توکن حامل (bearer token)
یا گواهی استفاده کنند. تکمیل این پیکربندی سه مرحله دارد.

* هنگام راه‌اندازی API server، محل فایل پیکربندی کنترل پذیرش را با فلگ
  `--admission-control-config-file` مشخص کنید.

* در فایل پیکربندی کنترل پذیرش، مشخص کنید که کنترل‌کننده‌ی MutatingAdmissionWebhook و
  کنترل‌کننده‌ی ValidatingAdmissionWebhook اعتبارنامه‌ها را از کجا بخوانند. اعتبارنامه‌ها در
  فایل‌های kubeConfig ذخیره می‌شوند (بله، همان طرح‌واره‌ای که kubectl از آن استفاده می‌کند)؛
  بنابراین نام فیلد `kubeConfigFile` است. در ادامه نمونه‌ای از فایل پیکربندی کنترل پذیرش آمده است:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: ValidatingAdmissionWebhook
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: WebhookAdmissionConfiguration
    kubeConfigFile: "<path-to-kubeconfig-file>"
- name: MutatingAdmissionWebhook
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: WebhookAdmissionConfiguration
    kubeConfigFile: "<path-to-kubeconfig-file>"
```

برای اطلاعات بیشتر درباره‌ی `AdmissionConfiguration`،
[مرجع AdmissionConfiguration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/) را ببینید.
برای جزئیات هر فیلد پیکربندی، بخش [پیکربندی وب‌هوک](#webhook-configuration) را ببینید.

در فایل kubeConfig، اعتبارنامه‌ها را وارد کنید:

```yaml
apiVersion: v1
kind: Config
users:
# name should be set to the DNS name of the service or the host (including port) of the URL the webhook is configured to speak to.
# If a non-443 port is used for services, it must be included in the name when configuring 1.16+ API servers.
#
# For a webhook configured to speak to a service on the default port (443), specify the DNS name of the service:
# - name: webhook1.ns1.svc
#   user: ...
#
# For a webhook configured to speak to a service on non-default port (e.g. 8443), specify the DNS name and port of the service in 1.16+:
# - name: webhook1.ns1.svc:8443
#   user: ...
# and optionally create a second stanza using only the DNS name of the service for compatibility with 1.15 API servers:
# - name: webhook1.ns1.svc
#   user: ...
#
# For webhooks configured to speak to a URL, match the host (and port) specified in the webhook's URL. Examples:
# A webhook with `url: https://www.example.com`:
# - name: www.example.com
#   user: ...
#
# A webhook with `url: https://www.example.com:443`:
# - name: www.example.com:443
#   user: ...
#
# A webhook with `url: https://www.example.com:8443`:
# - name: www.example.com:8443
#   user: ...
#
- name: 'webhook1.ns1.svc'
  user:
    client-certificate-data: "<pem encoded certificate>"
    client-key-data: "<pem encoded key>"
# The `name` supports using * to wildcard-match prefixing segments.
- name: '*.webhook-company.org'
  user:
    password: "<password>"
    username: "<name>"
# '*' is the default match.
- name: '*'
  user:
    token: "<token>"
```

البته باید سرور وب‌هوک را طوری راه‌اندازی کنید که بتواند این درخواست‌های احراز هویت را پردازش کند.

### احراز هویت نزد وب‌هوک‌های پذیرش {#authenticating-to-admission-webhooks}

{{< feature-state feature_gate_name="APIServerWebhookAuthenticationToken" >}}

به‌عنوان جایگزینی برای مدیریت دستی اعتبارنامه‌ها که در بخش
[احراز هویت API serverها](#authenticate-apiservers) شرح داده شد، ‏`kube-apiserver` می‌تواند
توکن‌های ServiceAccount کوتاه‌مدت و دامنه‌دار برای احراز هویت نزد وب‌هوک‌های پذیرش صادر کند.
این سازوکار از API ‏
[TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
برای صدور توکن‌هایی استفاده می‌کند که به یک پیکربندی وب‌هوک مشخص وابسته‌اند و دامنه‌ی آن‌ها
به گروه‌های API خاصی محدود است.

{{< note >}}
این سازوکار فقط صدور توکن را پیاده‌سازی می‌کند. دریافت و ارائه‌ی خودکار توکن به‌دست
`kube-apiserver` و API serverهای تجمیعی (aggregated) هنگام فراخوانی وب‌هوک‌ها، و نیز کتابخانه‌ای
برای راستی‌آزمایی توکن در سمت وب‌هوک، بخشی از این سازوکار نیستند.
{{< /note >}}

#### نحوه‌ی کار

‏API ‏TokenRequest گسترش یافته است تا بتواند توکن‌هایی صادر کند که به آبجکت‌های
ValidatingWebhookConfiguration یا MutatingWebhookConfiguration وابسته‌اند.
این توکن‌ها شامل ادعاهای گواهی‌دهی (attestation claims) هستند که مشخص می‌کنند حامل توکن
مجاز است درباره‌ی کدام گروه‌های API از وب‌هوک پرس‌وجو کند. اگر پیکربندی وب‌هوک ارجاع‌داده‌شده
حذف شود، توکن نامعتبر می‌شود.

برای درخواست توکن احراز هویت وب‌هوک، TokenRequest باید شامل موارد زیر باشد:

1. **فیلد `.spec.boundObjectRef`** که به یک ValidatingWebhookConfiguration یا
   یک MutatingWebhookConfiguration ارجاع می‌دهد. پیکربندی وب‌هوک ارجاع‌داده‌شده باید
   وجود داشته باشد و نباید برای حذف علامت‌گذاری شده باشد.

1. **فیلد `.spec.attestations`** با دقیقاً یک مدخل: کلید
   `admissionReviewAPIGroups` با مقداری از نوع آرایه‌ی رشته‌ای تک‌عنصری که گروه API تحت پوشش
   این توکن را مشخص می‌کند. مقدار `"*"` به معنای همه‌ی گروه‌های API است.
   گروه API مشخص‌شده باید با یکی از قاعده‌های پیکربندی وب‌هوک ارجاع‌داده‌شده تطبیق داشته باشد.

1. **فیلد `.spec.audiences`** با دقیقاً یک عنصر که با نقطه‌ی پایانی (endpoint) وب‌هوک
   تطبیق داشته باشد:
   - برای وب‌هوک‌هایی که با URL پیکربندی شده‌اند: مخاطب (audience) باید دقیقاً با URL یکسان باشد.
   - برای وب‌هوک‌هایی که با Service پیکربندی شده‌اند: مخاطب باید با الگوی
     `https://<name>.<namespace>.svc:<port>[<path>]` تطبیق داشته باشد؛ اگر در پیکربندی وب‌هوک
     مقداری مشخص نشده باشد، مقدار پیش‌فرض `<port>` برابر `443` و مقدار پیش‌فرض `<path>`
     برابر `/` است.

1. **مقدار `.spec.expirationSeconds`**. حداکثر زمان انقضای مجاز برای توکن‌های وابسته به
   وب‌هوک ۶۰۰ ثانیه (۱۰ دقیقه) است.

#### الزامات مجوزدهی

هنگام صدور توکن احراز هویت وب‌هوک، دو سطح از مجوزدهی بررسی می‌شود:

1. درخواست‌کننده باید روی `serviceaccounts/token` برای حساب سرویس هدف، مجوز `create`
   داشته باشد (مجوزدهی استاندارد TokenRequest).

1. حساب سرویسی که نام آن در TokenRequest آمده است، باید روی منبع `admissionReviewAPIGroups`
   در گروه API ‏`authentication.k8s.io` مجوز `attest` داشته باشد؛ آن هم با یک `resourceName`
   که با گروه API مشخص‌شده در گواهی‌دهی تطبیق داشته باشد (یا `"*"` برای همه‌ی گروه‌های API).

نمونه‌ی پیکربندی RBAC زیر به یک حساب سرویس اجازه می‌دهد توکن‌های احراز هویت وب‌هوکی
درخواست کند که دامنه‌ی آن‌ها به گروه API ‏`mygroup.example.com` محدود است:

{{% code_sample language="yaml" file="access/extensible-admission-controllers/webhook-auth-attest-clusterrole.yaml" %}}

#### ادعاهای توکن و راستی‌آزمایی با TokenReview

هنگامی که یک توکن احراز هویت وب‌هوک از طریق
[TokenReview](/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/)
راستی‌آزمایی می‌شود، کلیدهای اضافی زیر در فیلد `.status.user.extra` پاسخ مقداردهی می‌شوند:

برای توکن‌های وابسته به یک ValidatingWebhookConfiguration:
- `authentication.kubernetes.io/validatingwebhookconfiguration-name`
- `authentication.kubernetes.io/validatingwebhookconfiguration-uid`

برای توکن‌های وابسته به یک MutatingWebhookConfiguration:
- `authentication.kubernetes.io/mutatingwebhookconfiguration-name`
- `authentication.kubernetes.io/mutatingwebhookconfiguration-uid`

برای همه‌ی توکن‌های احراز هویت وب‌هوک:
- `attestation.authentication.kubernetes.io/admissionReviewAPIGroups` --
  گروه API‌ای که توکن برای آن مجاز است.

توکن JWT زیربنایی این ادعاها را در فضای نام ادعاهای خصوصی `kubernetes.io` قرار می‌دهد.
برای نمونه، توکنی که به یک MutatingWebhookConfiguration وابسته است:

```json
{
  "kubernetes.io": {
    "mutatingwebhookconfiguration": {
      "name": "my-webhook",
      "uid": "44e818f2-2ad0-4432-9816-3a649ca9945c"
    },
    "attestations": {
      "admissionReviewAPIGroups": ["mygroup.example.com"]
    }
  }
}
```

## درخواست و پاسخ وب‌هوک

### درخواست

درخواست‌ها به وب‌هوک‌ها به‌صورت درخواست POST با `Content-Type: application/json` ارسال می‌شوند
و بدنه‌ی آن‌ها یک آبجکت API از نوع `AdmissionReview` در گروه API ‏`admission.k8s.io` است که
به JSON سریال‌سازی شده است.

وب‌هوک‌ها می‌توانند با فیلد `admissionReviewVersions` در پیکربندی خود مشخص کنند که
کدام نسخه‌های آبجکت `AdmissionReview` را می‌پذیرند:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  admissionReviewVersions: ["v1", "v1beta1"]
```

فیلد `admissionReviewVersions` هنگام ایجاد پیکربندی‌های وب‌هوک الزامی است.
وب‌هوک‌ها باید دست‌کم از یک نسخه‌ی `AdmissionReview` پشتیبانی کنند که API server فعلی و
نسخه‌ی پیشین آن آن را بشناسند.

‏API serverها نخستین نسخه‌ی `AdmissionReview` در فهرست `admissionReviewVersions` را که
پشتیبانی می‌کنند، ارسال می‌کنند. اگر API server از هیچ‌یک از نسخه‌های این فهرست پشتیبانی نکند،
اجازه‌ی ایجاد پیکربندی داده نمی‌شود. اگر API server با پیکربندی وب‌هوکی روبه‌رو شود که پیش‌تر
ایجاد شده و از هیچ‌یک از نسخه‌های `AdmissionReview` که API server قادر به ارسال آن‌هاست
پشتیبانی نمی‌کند، تلاش‌ها برای فراخوانی وب‌هوک با شکست روبه‌رو می‌شوند و
[سیاست خرابی](#failure-policy) بر آن‌ها اعمال می‌شود.

این نمونه داده‌های موجود در یک آبجکت `AdmissionReview` را برای درخواستی نشان می‌دهد که
زیرمنبع `scale` یک `Deployment` از نوع `apps/v1` را به‌روزرسانی می‌کند:

```yaml
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "request": {
    # Random uid uniquely identifying this admission call
    "uid": "705ab4f5-6393-11e8-b7cc-42010a800002",

    # Fully-qualified group/version/kind of the incoming object
    "kind": {
      "group": "autoscaling",
      "version": "v1",
      "kind": "Scale"
    },

    # Fully-qualified group/version/kind of the resource being modified
    "resource": {
      "group": "apps",
      "version": "v1",
      "resource": "deployments"
    },

    # Subresource, if the request is to a subresource
    "subResource": "scale",

    # Fully-qualified group/version/kind of the incoming object in the original request to the API server
    # This only differs from `kind` if the webhook specified `matchPolicy: Equivalent` and the original
    # request to the API server was converted to a version the webhook registered for
    "requestKind": {
      "group": "autoscaling",
      "version": "v1",
      "kind": "Scale"
    },

    # Fully-qualified group/version/kind of the resource being modified in the original request to the API server
    # This only differs from `resource` if the webhook specified `matchPolicy: Equivalent` and the original
    # request to the API server was converted to a version the webhook registered for
    "requestResource": {
      "group": "apps",
      "version": "v1",
      "resource": "deployments"
    },

    # Subresource, if the request is to a subresource
    # This only differs from `subResource` if the webhook specified `matchPolicy: Equivalent` and the original
    # request to the API server was converted to a version the webhook registered for
    "requestSubResource": "scale",

    # Name of the resource being modified
    "name": "my-deployment",

    # Namespace of the resource being modified, if the resource is namespaced (or is a Namespace object)
    "namespace": "my-namespace",

    # operation can be CREATE, UPDATE, DELETE, or CONNECT
    "operation": "UPDATE",

    "userInfo": {
      # Username of the authenticated user making the request to the API server
      "username": "admin",

      # UID of the authenticated user making the request to the API server
      "uid": "014fbff9a07c",

      # Group memberships of the authenticated user making the request to the API server
      "groups": [
        "system:authenticated",
        "my-admin-group"
      ],

      # Arbitrary extra info associated with the user making the request to the API server
      # This is populated by the API server authentication layer
      "extra": {
        "some-key": [
          "some-value1",
          "some-value2"
        ]
      }
    },

    # object is the new object being admitted. It is null for DELETE operations
    "object": {
      "apiVersion": "autoscaling/v1",
      "kind": "Scale"
    },

    # oldObject is the existing object. It is null for CREATE and CONNECT operations
    "oldObject": {
      "apiVersion": "autoscaling/v1",
      "kind": "Scale"
    },

    # options contain the options for the operation being admitted, like meta.k8s.io/v1 CreateOptions,
    # UpdateOptions, or DeleteOptions. It is null for CONNECT operations
    "options": {
      "apiVersion": "meta.k8s.io/v1",
      "kind": "UpdateOptions"
    },

    # dryRun indicates the API request is running in dry run mode and will not be persisted
    # Webhooks with side effects should avoid actuating those side effects when dryRun is true
    "dryRun": false
  }
}
```

### پاسخ

وب‌هوک‌ها با کد وضعیت HTTP ‏۲۰۰ و سرآیند `Content-Type: application/json` پاسخ می‌دهند. بدنهٔ پاسخ یک آبجکت `AdmissionReview` است که به JSON سریال‌سازی شده، بخش `response` آن پر شده و نسخهٔ آن با نسخهٔ درخواست ارسال‌شده یکی است.

بخش `response` دست‌کم باید فیلدهای زیر را داشته باشد:

* فیلد `uid` که از مقدار `request.uid` ارسال‌شده به وب‌هوک کپی می‌شود
* فیلد `allowed` که مقدار آن `true` یا `false` است

نمونه‌ای از کمینه‌ترین پاسخ وب‌هوک برای اجازه دادن به یک درخواست:

```json
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "response": {
    "uid": "<value from request.uid>",
    "allowed": true
  }
}
```

نمونه‌ای از کمینه‌ترین پاسخ وب‌هوک برای رد کردن یک درخواست:

```json
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "response": {
    "uid": "<value from request.uid>",
    "allowed": false
  }
}
```

وب‌هوک هنگام رد کردن یک درخواست می‌تواند کد HTTP و پیامی را که به کاربر بازگردانده می‌شود، با فیلد `status` سفارشی کند. آبجکت وضعیتِ تعیین‌شده به کاربر بازگردانده می‌شود. برای جزئیات نوع `status` به [مستندات API](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#status-v1-meta) مراجعه کنید.
نمونه‌ای از پاسخی که درخواست را رد می‌کند و کد وضعیت HTTP و پیام نمایش‌داده‌شده به کاربر را سفارشی می‌کند:

```json
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "response": {
    "uid": "<value from request.uid>",
    "allowed": false,
    "status": {
      "code": 403,
      "message": "You cannot do this because it is Tuesday and your name starts with A"
    }
  }
}
```

هنگامی که وب‌هوک پذیرش تغییردهنده (mutating admission webhook) به درخواستی اجازه می‌دهد، می‌تواند در صورت تمایل آبجکت ورودی را نیز تغییر دهد. این کار با فیلدهای `patch` و `patchType` در پاسخ انجام می‌شود. در حال حاضر تنها مقدار پشتیبانی‌شده برای `patchType`، مقدار `JSONPatch` است. برای جزئیات بیشتر به مستندات [JSON patch](https://jsonpatch.com/) مراجعه کنید. وقتی `patchType: JSONPatch` تنظیم شده باشد، فیلد `patch` شامل آرایه‌ای از عملیات‌های JSON patch است که با base64 کدگذاری شده است.

برای نمونه، یک عملیات patch منفرد که `spec.replicas` را تنظیم می‌کند به این صورت است:
`[{"op": "add", "path": "/spec/replicas", "value": 3}]`

شکل کدگذاری‌شدهٔ آن با base64 چنین است: `W3sib3AiOiAiYWRkIiwgInBhdGgiOiAiL3NwZWMvcmVwbGljYXMiLCAidmFsdWUiOiAzfV0=`

بنابراین پاسخ وب‌هوک برای افزودن آن برچسب به این صورت خواهد بود:

```json
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "response": {
    "uid": "<value from request.uid>",
    "allowed": true,
    "patchType": "JSONPatch",
    "patch": "W3sib3AiOiAiYWRkIiwgInBhdGgiOiAiL3NwZWMvcmVwbGljYXMiLCAidmFsdWUiOiAzfV0="
  }
}
```

وب‌هوک‌های پذیرش می‌توانند در صورت تمایل پیام‌های هشداری بازگردانند که در سرآیندهای HTTP `Warning` با کد هشدار ۲۹۹ به کلاینتِ درخواست‌دهنده بازگردانده می‌شوند. هشدارها را می‌توان هم همراه پاسخ‌های پذیرشِ مجاز و هم همراه پاسخ‌های ردشده ارسال کرد.

اگر وب‌هوکی پیاده‌سازی می‌کنید که هشدار بازمی‌گرداند:

* پیشوند "Warning:" را در پیام قرار ندهید
* از پیام‌های هشدار برای توصیف مشکلاتی استفاده کنید که کلاینتِ ارسال‌کنندهٔ درخواست API باید آن‌ها را اصلاح کند یا از آن‌ها آگاه باشد
* در صورت امکان، طول هشدارها را به ۱۲۰ نویسه محدود کنید

{{< caution >}}
ممکن است سرور API پیام‌های هشدارِ منفردِ بلندتر از ۲۵۶ نویسه را پیش از بازگرداندن به کلاینت‌ها کوتاه کند.
اگر مجموع پیام‌های هشدارِ افزوده‌شده (از همهٔ مبدأها) از ۴۰۹۶ نویسه بیشتر شود، پیام‌های هشدار اضافی نادیده گرفته می‌شوند.
{{< /caution >}}

```json
{
  "apiVersion": "admission.k8s.io/v1",
  "kind": "AdmissionReview",
  "response": {
    "uid": "<value from request.uid>",
    "allowed": true,
    "warnings": [
      "duplicate envvar entries specified with name MY_ENV",
      "memory request less than 4MB specified for container mycontainer, which will not start successfully"
    ]
  }
}
```

## پیکربندی وب‌هوک

برای ثبت وب‌هوک‌های پذیرش، آبجکت‌های API از نوع `MutatingWebhookConfiguration` یا `ValidatingWebhookConfiguration` ایجاد کنید.
نام هر آبجکت `MutatingWebhookConfiguration` یا `ValidatingWebhookConfiguration` باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

{{< note >}}
نام‌هایی که به `.static.k8s.io` ختم می‌شوند برای
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
رزرو شده‌اند و نمی‌توان از آن‌ها برای پیکربندی‌های وب‌هوکِ مبتنی بر API استفاده کرد. این محدودیت
زمانی اعمال می‌شود که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig) مربوط به `ManifestBasedAdmissionControlConfig` فعال باشد.
{{< /note >}}

هر پیکربندی می‌تواند یک یا چند وب‌هوک داشته باشد.
اگر چند وب‌هوک در یک پیکربندی تعریف شوند، هر کدام باید نامی یکتا داشته باشد.
این الزام برای آن است که تطبیق لاگ‌های ممیزی (audit) و متریک‌های حاصل با پیکربندی‌های فعال آسان‌تر شود.

هر وب‌هوک موارد زیر را تعریف می‌کند.

### تطبیق درخواست‌ها: rules

هر وب‌هوک باید فهرستی از قواعد را مشخص کند که با آن‌ها تعیین می‌شود آیا درخواستی که به سرور API می‌رسد باید به وب‌هوک ارسال شود یا نه.
هر قاعده یک یا چند عملیات، گروه API، نسخهٔ API و منبع، و همچنین یک دامنهٔ منبع (scope) را مشخص می‌کند:

* فیلد `operations` یک یا چند عملیات را برای تطبیق فهرست می‌کند. مقدار آن می‌تواند `"CREATE"`، `"UPDATE"`، `"DELETE"`، `"CONNECT"`
  یا `"*"` برای تطبیق با همهٔ عملیات‌ها باشد.
* فیلد `apiGroups` یک یا چند گروه API را برای تطبیق فهرست می‌کند. مقدار `""` گروه API هسته است و `"*"` با همهٔ گروه‌های API تطبیق می‌یابد.
* فیلد `apiVersions` یک یا چند نسخهٔ API را برای تطبیق فهرست می‌کند. مقدار `"*"` با همهٔ نسخه‌های API تطبیق می‌یابد.
* فیلد `resources` یک یا چند منبع را برای تطبیق فهرست می‌کند.

  * مقدار `"*"` با همهٔ منابع تطبیق می‌یابد، اما نه با زیرمنابع.
  * مقدار `"*/*"` با همهٔ منابع و زیرمنابع تطبیق می‌یابد.
  * مقدار `"pods/*"` با همهٔ زیرمنابعِ پادها تطبیق می‌یابد.
  * مقدار `"*/status"` با همهٔ زیرمنابعِ status تطبیق می‌یابد.

* فیلد `scope` دامنه‌ای را برای تطبیق مشخص می‌کند. مقادیر معتبر `"Cluster"`، `"Namespaced"` و `"*"` هستند.
  زیرمنابع با دامنهٔ منبعِ والد خود تطبیق داده می‌شوند. مقدار پیش‌فرض `"*"` است.

  * مقدار `"Cluster"` به این معناست که فقط منابعِ در دامنهٔ کلاستر با این قاعده تطبیق می‌یابند (آبجکت‌های API از نوع Namespace در دامنهٔ کلاستر قرار دارند).
  * مقدار `"Namespaced"` به این معناست که فقط منابعِ وابسته به فضای نام (namespace) با این قاعده تطبیق می‌یابند.
  * مقدار `"*"` به این معناست که هیچ محدودیتی از نظر دامنه وجود ندارد.

اگر درخواست ورودی با یکی از مقادیر مشخص‌شده برای `operations`، `groups`، `versions`،
`resources` و `scope` در هر یک از `rules` یک وب‌هوک تطبیق یابد، درخواست به آن وب‌هوک ارسال می‌شود.

در ادامه نمونه‌های دیگری از قواعد آمده است که می‌توان با آن‌ها مشخص کرد کدام منابع باید رهگیری شوند.

تطبیق درخواست‌های `CREATE` یا `UPDATE` برای `deployments` و `replicasets` در `apps/v1` و `apps/v1beta1`:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
...
webhooks:
- name: my-webhook.example.com
  rules:
  - operations: ["CREATE", "UPDATE"]
    apiGroups: ["apps"]
    apiVersions: ["v1", "v1beta1"]
    resources: ["deployments", "replicasets"]
    scope: "Namespaced"
  ...
```

تطبیق درخواست‌های ایجاد برای همهٔ منابع (اما نه زیرمنابع) در همهٔ گروه‌ها و نسخه‌های API:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    rules:
      - operations: ["CREATE"]
        apiGroups: ["*"]
        apiVersions: ["*"]
        resources: ["*"]
        scope: "*"
```

تطبیق درخواست‌های به‌روزرسانی برای همهٔ زیرمنابعِ `status` در همهٔ گروه‌ها و نسخه‌های API:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    rules:
      - operations: ["UPDATE"]
        apiGroups: ["*"]
        apiVersions: ["*"]
        resources: ["*/status"]
        scope: "*"
```

### منابع مجازیِ مستثنا {#excluded-virtual-resources}

{{< feature-state feature_gate_name="ExcludeAdmissionWebhookVirtualResources" >}}

وب‌هوک‌های پذیرش برای منابع احراز هویت و مجوزدهیِ زیر که ماندگار نمی‌شوند (منابع مجازی)
فراخوانی نمی‌شوند، حتی اگر `rules` یک وب‌هوک با آن‌ها تطبیق یابد:

* [TokenReviews]({{< relref "/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/" >}})
* [SelfSubjectReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-review-v1-authentication/" >}})
* [LocalSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/local-subject-access-review-v1-authorization/" >}})
* [SelfSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization/" >}})
* [SelfSubjectRulesReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-rules-review-v1-authorization/" >}})
* [SubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/" >}})

وب‌هوکی که این منابع را رهگیری کند ممکن است مسیر احراز هویت و مجوزدهیِ خودِ کلاستر را مسدود کند.
برای مثال، وب‌هوکِ معیوبی که با `subjectaccessreviews` تطبیق می‌یابد می‌تواند بررسی‌های مجوزدهی‌ای
را که خودِ کلاستر به آن‌ها وابسته است مسدود کند. با مستثنا کردن این منابع، رفتار وب‌هوک‌های پذیرش
با [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)
و [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/)
هماهنگ می‌شود؛ این دو همواره این منابع را مستثنا کرده‌اند.

اگر پیکربندی وب‌هوکی را با قاعده‌ای ایجاد یا به‌روزرسانی کنید که صراحتاً نام یکی از این منابع را آورده
باشد، سرور API هشداری بازمی‌گرداند و اعلام می‌کند که آن قاعده هیچ اثری ندارد. سرور API همچنین هنگام
بارگذاری پیکربندی‌های وب‌هوکِ موجود، نام هر پیکربندی‌ای را که چنین قاعده‌ای داشته باشد در لاگ ثبت
می‌کند تا بتوانید پیش از ارتقا، کلاستر خود را ممیزی کنید. قواعدی که تنها از طریق یک نویسهٔ عام
(`"*"`) در `apiGroups` یا `resources` با این منابع تطبیق می‌یابند علامت‌گذاری نمی‌شوند، زیرا
هدف آن‌ها مبهم است.

رهگیری این منابع مجازی توسط وب‌هوک‌ها از نسخهٔ v1.37 کوبرنتیز منسوخ (deprecated) شده است.
به‌عنوان راه‌حلی موقت، می‌توانید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ExcludeAdmissionWebhookVirtualResources)
مربوط به `ExcludeAdmissionWebhookVirtualResources` را روی `false` تنظیم کنید تا رفتار قبلی بازگردد.
برنامه این است که وقتی این قابلیت به مرحلهٔ پایدار برسد، این feature gate در حالت فعال قفل شود؛
از آن پس وب‌هوک‌های پذیرش دیگر نمی‌توانند این منابع را رهگیری کنند.

### تطبیق درخواست‌ها: objectSelector

وب‌هوک‌ها می‌توانند در صورت تمایل با تعیین `objectSelector`، درخواست‌های رهگیری‌شده را بر اساس
برچسب‌های آبجکت‌هایی که قرار است برایشان ارسال شوند محدود کنند. در صورت تعیین این فیلد، انتخابگر
(selector) آبجکت هم روی object و هم روی oldObject که قرار است به وب‌هوک ارسال شوند ارزیابی می‌شود،
و اگر هر یک از این دو آبجکت با انتخابگر تطبیق یابد، تطبیق برقرار تلقی می‌شود.

آبجکت تهی (`oldObject` در حالت ایجاد، یا `newObject` در حالت حذف)
یا آبجکتی که نمی‌تواند برچسب داشته باشد (مانند آبجکت `DeploymentRollback` یا `PodProxyOptions`)
تطبیق‌یافته در نظر گرفته نمی‌شود.

از انتخابگر آبجکت فقط زمانی استفاده کنید که وب‌هوک اختیاری (opt-in) باشد، زیرا کاربران نهایی
می‌توانند با تنظیم برچسب‌ها از وب‌هوک پذیرش عبور کنند.

این نمونه یک وب‌هوک تغییردهنده را نشان می‌دهد که با عملیات `CREATE` روی هر منبعی (اما نه زیرمنابع) که برچسب `foo: bar` دارد تطبیق می‌یابد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  objectSelector:
    matchLabels:
      foo: bar
  rules:
  - operations: ["CREATE"]
    apiGroups: ["*"]
    apiVersions: ["*"]
    resources: ["*"]
    scope: "*"
```

برای نمونه‌های بیشتری از انتخابگرهای برچسب، به [مفهوم برچسب‌ها](/docs/concepts/overview/working-with-objects/labels)
مراجعه کنید.

### تطبیق درخواست‌ها: namespaceSelector

وب‌هوک‌ها می‌توانند در صورت تمایل با تعیین `namespaceSelector`، درخواست‌های رهگیری‌شده برای
منابعِ وابسته به فضای نام را بر اساس برچسب‌های فضای نامِ دربرگیرنده محدود کنند.

فیلد `namespaceSelector` تعیین می‌کند که آیا وب‌هوک روی درخواستی برای یک منبعِ وابسته به فضای نام
(یا یک آبجکت Namespace) اجرا شود یا نه؛ این تصمیم بر این اساس گرفته می‌شود که آیا برچسب‌های فضای نام
با انتخابگر تطبیق دارند یا خیر.
اگر خودِ آبجکت یک فضای نام باشد، تطبیق روی object.metadata.labels انجام می‌شود.
اگر آبجکت منبعی در دامنهٔ کلاستر به‌جز Namespace باشد، `namespaceSelector` هیچ اثری ندارد.

این نمونه یک وب‌هوک تغییردهنده را نشان می‌دهد که با عملیات `CREATE` روی هر منبعِ وابسته به فضای نام
در فضای نامی تطبیق می‌یابد که برچسب "runlevel" آن مقدار "0" یا "1" ندارد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    namespaceSelector:
      matchExpressions:
        - key: runlevel
          operator: NotIn
          values: ["0","1"]
    rules:
      - operations: ["CREATE"]
        apiGroups: ["*"]
        apiVersions: ["*"]
        resources: ["*"]
        scope: "Namespaced"
```

این نمونه یک وب‌هوک اعتبارسنج (validating) را نشان می‌دهد که با عملیات `CREATE` روی هر منبعِ وابسته
به فضای نام در فضای نامی تطبیق می‌یابد که "environment" آن "prod" یا "staging" است:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    namespaceSelector:
      matchExpressions:
        - key: environment
          operator: In
          values: ["prod","staging"]
    rules:
      - operations: ["CREATE"]
        apiGroups: ["*"]
        apiVersions: ["*"]
        resources: ["*"]
        scope: "Namespaced"
```

برای نمونه‌های بیشتری از انتخابگرهای برچسب، به [مفهوم برچسب‌ها](/docs/concepts/overview/working-with-objects/labels)
مراجعه کنید.

### تطبیق درخواست‌ها: matchPolicy

سرورهای API می‌توانند آبجکت‌ها را از طریق چندین گروه یا نسخهٔ API در دسترس قرار دهند.

برای مثال، اگر وب‌هوکی فقط برای برخی گروه‌ها/نسخه‌های API قاعده تعریف کرده باشد
(مانند `apiGroups:["apps"], apiVersions:["v1","v1beta1"]`)
و درخواستی برای تغییر منبع از طریق گروه/نسخهٔ API دیگری (مانند `extensions/v1beta1`) ارسال شود،
آن درخواست به وب‌هوک فرستاده نمی‌شود.

با فیلد `matchPolicy`، وب‌هوک می‌تواند تعیین کند که `rules` آن چگونه برای تطبیق درخواست‌های ورودی به کار رود.
مقادیر مجاز `Exact` یا `Equivalent` هستند.

* مقدار `Exact` به این معناست که درخواست فقط زمانی رهگیری شود که دقیقاً با یک قاعدهٔ مشخص‌شده تطبیق یابد.
* مقدار `Equivalent` به این معناست که اگر درخواست منبعی را که در `rules` فهرست شده تغییر دهد،
  حتی از طریق گروه یا نسخهٔ API دیگری، رهگیری شود.

در نمونهٔ بالا، وب‌هوکی که فقط برای `apps/v1` ثبت شده بود می‌توانست از `matchPolicy` استفاده کند:

* تنظیم `matchPolicy: Exact` به این معناست که درخواست `extensions/v1beta1` به وب‌هوک ارسال نمی‌شود
* تنظیم `matchPolicy: Equivalent` به این معناست که درخواست `extensions/v1beta1` به وب‌هوک ارسال می‌شود
  (و آبجکت‌ها به نسخه‌ای که وب‌هوک مشخص کرده، یعنی `apps/v1`، تبدیل می‌شوند)

توصیه می‌شود مقدار `Equivalent` را تعیین کنید؛ این کار تضمین می‌کند که وقتی ارتقاها نسخه‌های جدیدی
از منبع را در سرور API فعال می‌کنند، وب‌هوک‌ها همچنان منابعی را که انتظار دارند رهگیری کنند.

وقتی سرور API دیگر منبعی را ارائه نکند، آن منبع دیگر با نسخه‌های دیگرِ همان منبع که هنوز ارائه می‌شوند
معادل در نظر گرفته نمی‌شود.
برای مثال، deploymentهای `extensions/v1beta1` ابتدا منسوخ و سپس (در کوبرنتیز v1.16) حذف شدند.

از زمان این حذف، وب‌هوکی که قاعدهٔ `apiGroups:["extensions"], apiVersions:["v1beta1"], resources:["deployments"]`
را دارد، deploymentهایی را که از طریق APIهای `apps/v1` ایجاد می‌شوند رهگیری نمی‌کند. به همین دلیل،
بهتر است وب‌هوک‌ها برای نسخه‌های پایدارِ منابع ثبت شوند.

این نمونه یک وب‌هوک اعتبارسنج را نشان می‌دهد که تغییرات deploymentها را (صرف‌نظر از گروه یا نسخهٔ API)
رهگیری می‌کند و همیشه یک آبجکت `Deployment` با نسخهٔ `apps/v1` برای آن ارسال می‌شود:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  matchPolicy: Equivalent
  rules:
  - operations: ["CREATE","UPDATE","DELETE"]
    apiGroups: ["apps"]
    apiVersions: ["v1"]
    resources: ["deployments"]
    scope: "Namespaced"
```

مقدار پیش‌فرض `matchPolicy` برای وب‌هوک‌های پذیرش، `Equivalent` است.

### تطبیق درخواست‌ها: `matchConditions`

{{< feature-state feature_gate_name="AdmissionWebhookMatchConditions" >}}

اگر به فیلتر کردن دقیق‌تر درخواست‌ها نیاز دارید، می‌توانید برای وب‌هوک‌ها _شرایط تطبیق_ تعریف کنید.
این شرایط زمانی مفیدند که ببینید قواعد تطبیق، `objectSelectors` و `namespaceSelectors` هنوز
فیلتری را که برای تعیین زمانِ فراخوانی از طریق HTTP می‌خواهید فراهم نمی‌کنند. شرایط تطبیق،
[عبارت‌های CEL](/docs/reference/using-api/cel/) هستند. برای فراخوانی وب‌هوک، همهٔ شرایط تطبیق
باید به true ارزیابی شوند.

در اینجا نمونه‌ای آمده است که چند کاربرد مختلف شرایط تطبیق را نشان می‌دهد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    matchPolicy: Equivalent
    rules:
      - operations: ['CREATE','UPDATE']
        apiGroups: ['*']
        apiVersions: ['*']
        resources: ['*']
    failurePolicy: 'Ignore' # Fail-open (optional)
    sideEffects: None
    clientConfig:
      service:
        namespace: my-namespace
        name: my-webhook
      caBundle: '<omitted>'
    # You can have up to 64 matchConditions per webhook
    matchConditions:
      - name: 'exclude-leases' # Each match condition must have a unique name
        expression: '!(request.resource.group == "coordination.k8s.io" && request.resource.resource == "leases")' # Match non-lease resources.
      - name: 'exclude-kubelet-requests'
        expression: '!("system:nodes" in request.userInfo.groups)' # Match requests made by non-node users.
      - name: 'rbac' # Skip RBAC requests, which are handled by the second webhook.
        expression: 'request.resource.group != "rbac.authorization.k8s.io"'

  # This example illustrates the use of the 'authorizer'. The authorization check is more expensive
  # than a simple expression, so in this example it is scoped to only RBAC requests by using a second
  # webhook. Both webhooks can be served by the same endpoint.
  - name: rbac.my-webhook.example.com
    matchPolicy: Equivalent
    rules:
      - operations: ['CREATE','UPDATE']
        apiGroups: ['rbac.authorization.k8s.io']
        apiVersions: ['*']
        resources: ['*']
    failurePolicy: 'Fail' # Fail-closed (the default)
    sideEffects: None
    clientConfig:
      service:
        namespace: my-namespace
        name: my-webhook
      caBundle: '<omitted>'
    # You can have up to 64 matchConditions per webhook
    matchConditions:
      - name: 'breakglass'
        # Skip requests made by users authorized to 'breakglass' on this webhook.
        # The 'breakglass' API verb does not need to exist outside this check.
        expression: '!authorizer.group("admissionregistration.k8s.io").resource("validatingwebhookconfigurations").name("my-webhook.example.com").check("breakglass").allowed()'
```

{{< note >}}
برای هر وب‌هوک می‌توانید حداکثر ۶۴ عنصر در فیلد `matchConditions` تعریف کنید.
{{< /note >}}

شرایط تطبیق به متغیرهای CEL زیر دسترسی دارند:

- متغیر `object`: آبجکتِ درخواست ورودی. مقدار آن برای درخواست‌های DELETE تهی است. ممکن است
  نسخهٔ آبجکت بر اساس [matchPolicy](#matching-requests-matchpolicy) تبدیل شود.
- متغیر `oldObject`: آبجکت موجود. مقدار آن برای درخواست‌های CREATE تهی است.
- متغیر `request`: بخش درخواستِ [AdmissionReview](#request)، به‌جز `object` و `oldObject`.
- متغیر `authorizer`: یک مجوزدهندهٔ CEL. از آن می‌توان برای انجام بررسی‌های مجوزدهی برای
  هویتِ اصلیِ (principal) درخواست، یعنی کاربر احراز هویت‌شده، استفاده کرد. برای جزئیات بیشتر به
  [Authz](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz) در مستندات کتابخانهٔ CEL کوبرنتیز
  مراجعه کنید.
- متغیر `authorizer.requestResource`: میان‌بری برای بررسی مجوزدهی‌ای که با منبعِ درخواست
  (گروه، منبع، (زیرمنبع)، فضای نام، نام) پیکربندی شده است.

برای اطلاعات بیشتر دربارهٔ عبارت‌های CEL، به
[مرجع Common Expression Language در کوبرنتیز](/docs/reference/using-api/cel/) مراجعه کنید.

اگر هنگام ارزیابی یک شرط تطبیق خطایی رخ دهد، وب‌هوک هرگز فراخوانی نمی‌شود. اینکه درخواست رد شود
یا نه، به این صورت تعیین می‌شود:

1. اگر **هر یک** از شرایط تطبیق به `false` ارزیابی شده باشد (صرف‌نظر از خطاهای دیگر)، سرور API از وب‌هوک صرف‌نظر می‌کند.
2. در غیر این صورت:
    - برای [`failurePolicy: Fail`](#failure-policy)، درخواست (بدون فراخوانی وب‌هوک) رد می‌شود.
    - برای [`failurePolicy: Ignore`](#failure-policy)، پردازش درخواست ادامه می‌یابد، اما از وب‌هوک صرف‌نظر می‌شود.

### تماس با وب‌هوک

پس از اینکه سرور API تشخیص داد درخواستی باید به یک وب‌هوک فرستاده شود، باید بداند چگونه با آن وب‌هوک تماس بگیرد. این موضوع در بخش `clientConfig` از پیکربندی وب‌هوک مشخص می‌شود.

وب‌هوک‌ها را می‌توان از طریق یک URL یا یک ارجاع به سرویس فراخوانی کرد. همچنین در صورت نیاز می‌توان یک بستهٔ CA سفارشی برای تأیید اتصال TLS در پیکربندی آن‌ها گنجاند.

#### نشانی URL

فیلد `url` مکان وب‌هوک را در قالب استاندارد URL (`scheme://host:port/path`) مشخص می‌کند.

مقدار `host` نباید به سرویسی اشاره کند که درون کلاستر اجرا می‌شود؛ در این حالت به‌جای آن با تعیین فیلد `service` از ارجاع به سرویس استفاده کنید. در برخی سرورهای API ممکن است نام میزبان از طریق DNS خارجی تفکیک (resolve) شود. برای نمونه، `kube-apiserver` نمی‌تواند نام‌های DNS درون کلاستر را تفکیک کند، زیرا این کار نقض لایه‌بندی است. مقدار `host` می‌تواند یک نشانی IP نیز باشد.

توجه کنید که استفاده از `localhost` یا `127.0.0.1` به‌عنوان `host` پرخطر است، مگر اینکه با دقت بسیار این وب‌هوک را روی همهٔ میزبان‌هایی اجرا کنید که سرور API روی آن‌ها اجرا می‌شود و ممکن است لازم باشد این وب‌هوک را فراخوانی کند. چنین نصب‌هایی احتمالاً قابل‌حمل نیستند یا به‌سادگی در یک کلاستر جدید اجرا نمی‌شوند.

طرح (scheme) باید "https" باشد؛ یعنی URL باید با "https://" آغاز شود.

استفاده از اطلاعات کاربر یا احراز هویت پایه (basic auth)، برای نمونه `user:password@`، مجاز نیست. قطعه‌ها (`#...`) و پارامترهای پرس‌وجو (`?...`) نیز مجاز نیستند.

نمونهٔ زیر یک وب‌هوک تغییردهنده (mutating) را نشان می‌دهد که برای فراخوانی یک URL پیکربندی شده است. این وب‌هوک انتظار دارد گواهی TLS با ریشه‌های اعتماد سیستم تأیید شود و به همین دلیل caBundle را مشخص نمی‌کند:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  clientConfig:
    url: "https://my-webhook.example.com:9443/my-webhook-path"
```

#### ارجاع به سرویس

بخش `service` درون `clientConfig` ارجاعی به سرویسِ این وب‌هوک است. اگر وب‌هوک درون کلاستر اجرا می‌شود، باید به‌جای `url` از `service` استفاده کنید. فضای نام (namespace) و نام سرویس الزامی هستند. پورت اختیاری است و مقدار پیش‌فرض آن 443 است. مسیر نیز اختیاری است و مقدار پیش‌فرض آن "/" است.

نمونهٔ زیر یک وب‌هوک تغییردهنده را نشان می‌دهد که برای فراخوانی یک سرویس روی پورت "1234" و در زیرمسیر "/my-path" پیکربندی شده است و اتصال TLS را با استفاده از یک بستهٔ CA سفارشی در برابر ServerName با مقدار `my-service-name.my-service-namespace.svc` تأیید می‌کند:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  clientConfig:
    caBundle: <CA_BUNDLE>
    service:
      namespace: my-service-namespace
      name: my-service-name
      path: /my-path
      port: 1234
```

{{< note >}}
باید `<CA_BUNDLE>` را در نمونهٔ بالا با یک بستهٔ CA معتبر جایگزین کنید؛ یعنی بسته‌ای با کدگذاری PEM که برای اعتبارسنجی گواهی سرور وب‌هوک به کار می‌رود.
{{< /note >}}

### اثرات جانبی

وب‌هوک‌ها معمولاً فقط روی محتوای `AdmissionReview` ارسال‌شده به آن‌ها عمل می‌کنند. با این حال، برخی وب‌هوک‌ها در جریان پردازش درخواست‌های پذیرش (admission)، تغییراتی را خارج از این جریان (out-of-band) نیز اعمال می‌کنند.

وب‌هوک‌هایی که تغییرات خارج از جریان («اثرات جانبی») ایجاد می‌کنند، باید یک سازوکار تطبیق (reconciliation) نیز داشته باشند (مانند یک کنترل‌کننده) که به‌طور دوره‌ای وضعیت واقعی را تعیین کند و داده‌های خارج از جریانی را که وب‌هوک پذیرش تغییر داده است، مطابق با واقعیت اصلاح کند. دلیل این است که فراخوانی یک وب‌هوک پذیرش تضمین نمی‌کند که آبجکتِ پذیرفته‌شده عیناً، یا حتی اصلاً، ذخیره شود. ممکن است وب‌هوک‌های بعدی محتوای آبجکت را تغییر دهند، هنگام نوشتن در ذخیره‌ساز تعارضی پیش آید، یا سرور پیش از ذخیرهٔ آبجکت خاموش شود.

افزون بر این، وب‌هوک‌های دارای اثر جانبی باید هنگام رسیدگی به درخواست‌های پذیرش با `dryRun: true` از اعمال آن اثرات جانبی صرف‌نظر کنند. هر وب‌هوک باید صراحتاً اعلام کند که هنگام اجرا با `dryRun` اثر جانبی نخواهد داشت؛ در غیر این صورت، درخواست dry-run به وب‌هوک فرستاده نمی‌شود و به‌جای آن درخواست API با شکست مواجه می‌شود.

وب‌هوک‌ها با فیلد `sideEffects` در پیکربندی وب‌هوک مشخص می‌کنند که آیا اثر جانبی دارند یا نه:

* `None`: فراخوانی وب‌هوک هیچ اثر جانبی نخواهد داشت.
* `NoneOnDryRun`: فراخوانی وب‌هوک ممکن است اثر جانبی داشته باشد، اما اگر درخواستی با
  `dryRun: true` به وب‌هوک فرستاده شود، وب‌هوک از اعمال اثرات جانبی خودداری می‌کند (یعنی وب‌هوک
  از `dryRun` آگاه است).

نمونهٔ زیر یک وب‌هوک اعتبارسنج (validating) را نشان می‌دهد که اعلام می‌کند روی درخواست‌های `dryRun: true` اثر جانبی ندارد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    sideEffects: NoneOnDryRun
```

### مهلت‌های زمانی

از آنجا که وب‌هوک‌ها تأخیر درخواست‌های API را افزایش می‌دهند، باید تا حد امکان سریع ارزیابی شوند. با فیلد `timeoutSeconds` می‌توان تعیین کرد که سرور API پیش از آنکه فراخوانی را شکست‌خورده تلقی کند، چه مدت منتظر پاسخ وب‌هوک بماند.

اگر مهلت زمانی پیش از پاسخ وب‌هوک به پایان برسد، بسته به [سیاست شکست](#failure-policy)، یا فراخوانی وب‌هوک نادیده گرفته می‌شود یا درخواست API رد می‌شود.

مقدار مهلت زمانی باید بین ۱ تا ۳۰ ثانیه باشد.

نمونهٔ زیر یک وب‌هوک اعتبارسنج را با مهلت زمانی سفارشی ۲ ثانیه نشان می‌دهد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    timeoutSeconds: 2
```

مقدار پیش‌فرض مهلت زمانی برای یک وب‌هوک پذیرش ۱۰ ثانیه است.

### سیاست فراخوانی مجدد

یک ترتیب واحد برای افزونه‌های پذیرش تغییردهنده (از جمله وب‌هوک‌ها) در همهٔ موارد کارساز نیست (برای نمونه، https://issue.k8s.io/64333 را ببینید). یک وب‌هوک تغییردهنده می‌تواند زیرساختار جدیدی به آبجکت اضافه کند (مانند افزودن یک `container` به یک `pod`) و افزونه‌های تغییردهندهٔ دیگری که پیش‌تر اجرا شده‌اند ممکن است دربارهٔ این ساختارهای جدید نظری داشته باشند (مانند تنظیم `imagePullPolicy` روی همهٔ کانتینرها).

برای آنکه افزونه‌های پذیرش تغییردهنده بتوانند تغییراتی را که افزونه‌های دیگر اعمال کرده‌اند مشاهده کنند، اگر یک وب‌هوک تغییردهنده آبجکتی را تغییر دهد، افزونه‌های پذیرش تغییردهندهٔ داخلی دوباره اجرا می‌شوند. وب‌هوک‌های تغییردهنده نیز می‌توانند با تعیین `reinvocationPolicy` کنترل کنند که آیا خودشان هم دوباره فراخوانی شوند یا نه.

فیلد `reinvocationPolicy` را می‌توان روی `Never` یا `IfNeeded` تنظیم کرد. مقدار پیش‌فرض آن `Never` است.

* `Never`: وب‌هوک نباید در یک ارزیابی پذیرش بیش از یک بار فراخوانی شود.
* `IfNeeded`: اگر افزونه‌های پذیرش دیگر پس از نخستین فراخوانی وب‌هوک، آبجکتِ در حال پذیرش را
  تغییر دهند، ممکن است وب‌هوک در جریان همان ارزیابی پذیرش دوباره فراخوانی شود.

نکات مهمی که باید به آن‌ها توجه کرد:

* تضمینی وجود ندارد که تعداد فراخوانی‌های اضافی دقیقاً یک بار باشد.
* اگر فراخوانی‌های اضافی به تغییرات بیشتری در آبجکت بینجامد، تضمینی برای فراخوانی دوبارهٔ
  وب‌هوک‌ها وجود ندارد.
* ممکن است ترتیب وب‌هوک‌هایی که از این گزینه استفاده می‌کنند تغییر کند تا تعداد فراخوانی‌های اضافی به حداقل برسد.
* برای اعتبارسنجی یک آبجکت پس از آنکه تکمیل همهٔ تغییرات تضمین شد، به‌جای این گزینه از یک وب‌هوک
  پذیرش اعتبارسنج استفاده کنید (این روش برای وب‌هوک‌های دارای اثر جانبی توصیه می‌شود).

نمونهٔ زیر یک وب‌هوک تغییردهنده را نشان می‌دهد که اگر افزونه‌های پذیرش بعدی آبجکت را تغییر دهند، فراخوانی مجدد را می‌پذیرد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  reinvocationPolicy: IfNeeded
```

وب‌هوک‌های تغییردهنده باید [خودتوان (idempotent)](/docs/concepts/cluster-administration/admission-webhooks-good-practices/#ordering-idempotence) باشند؛ یعنی بتوانند آبجکتی را که پیش‌تر پذیرفته و احتمالاً تغییر داده‌اند، با موفقیت پردازش کنند. این موضوع دربارهٔ همهٔ وب‌هوک‌های پذیرش تغییردهنده صادق است، زیرا هر تغییری که آن‌ها می‌توانند در یک آبجکت ایجاد کنند ممکن است از پیش در آبجکتِ ارائه‌شده از سوی کاربر وجود داشته باشد؛ اما برای وب‌هوک‌هایی که فراخوانی مجدد را برمی‌گزینند، این ویژگی ضروری است.

### سیاست شکست

فیلد `failurePolicy` تعیین می‌کند که با خطاهایی که هنگام _فراخوانی_ وب‌هوک پذیرش رخ می‌دهند، چگونه رفتار شود. مقادیر مجاز `Ignore` یا `Fail` هستند.

* مقدار `Ignore` یعنی خطا در فراخوانی وب‌هوک نادیده گرفته می‌شود و درخواست API می‌تواند ادامه یابد.
* مقدار `Fail` یعنی خطا در فراخوانی وب‌هوک باعث شکست پذیرش و رد درخواست API می‌شود.

سیاست شکست برای انواع خطاهای زیر اعمال می‌شود:

* خطاهای شبکه، اتمام مهلت زمانی یا شکست اتصال هنگام تماس با وب‌هوک.
* وب‌هوک پاسخ HTTP غیر از 2xx یا پاسخی با قالب نادرست برمی‌گرداند.
* سرور API نمی‌تواند درخواست پذیرش را سریال‌سازی کند یا یک کلاینت HTTP داخلی برای وب‌هوک بسازد.
* (فقط برای وب‌هوک‌های تغییردهنده) پاسخ شامل وصله‌ای (patch) است که رمزگشایی‌پذیر نیست یا نوع آن پشتیبانی نمی‌شود.

اگر نوشتن در API کوبرنتیز از طریق یک فراخوان پذیرش رد شود، این یک _رد کردن_ است و کوبرنتیز آن را شکست به شمار نمی‌آورد. وقتی سرور API کوبرنتیز با موفقیت به وب‌هوک دسترسی پیدا کند و پیاده‌سازی وب‌هوک صراحتاً درخواست را رد کرده باشد (با تعیین `allowed: false` در پاسخ)، سیاست شکست را اعمال **نمی‌کند**. رد صریحی که به‌درستی منتقل شده باشد، صرف‌نظر از مقدار `failurePolicy`، همیشه درخواست API را رد می‌کند.

نمونهٔ زیر وب‌هوک تغییردهنده‌ای را نشان می‌دهد که طوری پیکربندی شده است که اگر هنگام فراخوانی وب‌هوک پذیرش خطایی رخ دهد، درخواست API را رد کند:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  failurePolicy: Fail
```

مقدار پیش‌فرض `failurePolicy` برای وب‌هوک‌های پذیرش `Fail` است.

## پایش وب‌هوک‌های پذیرش

سرور API روش‌هایی برای پایش رفتار وب‌هوک‌های پذیرش فراهم می‌کند. این سازوکارهای پایش به مدیران کلاستر کمک می‌کنند به پرسش‌هایی مانند پرسش‌های زیر پاسخ دهند:

1. کدام وب‌هوک تغییردهنده آبجکت را در یک درخواست API تغییر داد؟

2. وب‌هوک تغییردهنده چه تغییری روی آبجکت اعمال کرد؟

3. کدام وب‌هوک‌ها مکرراً درخواست‌های API را رد می‌کنند؟ دلیل رد چیست؟

### حاشیه‌نویسی‌های ممیزی وب‌هوک تغییردهنده

گاهی دانستن اینکه کدام وب‌هوک تغییردهنده آبجکت را در یک درخواست API تغییر داده و چه تغییری اعمال کرده است، مفید است.

سرور API کوبرنتیز برای هر فراخوانی وب‌هوک تغییردهنده [ممیزی (auditing)](/docs/tasks/debug/debug-cluster/audit/) انجام می‌دهد. هر فراخوانی یک حاشیه‌نویسی (annotation) ممیزی تولید می‌کند که ثبت می‌کند آیا آبجکت درخواست در آن فراخوانی تغییر کرده است یا نه. همچنین در صورت نیاز، حاشیه‌نویسی دیگری تولید می‌کند که وصلهٔ اعمال‌شده از پاسخ پذیرش وب‌هوک را ثبت می‌کند. این حاشیه‌نویسی‌ها در رویداد ممیزیِ درخواست مربوط و در مرحلهٔ مشخصی از اجرای آن تنظیم می‌شوند؛ سپس این رویداد بر اساس یک سیاست مشخص پیش‌پردازش و در یک بک‌اند نوشته می‌شود.

سطح ممیزی یک رویداد تعیین می‌کند که کدام حاشیه‌نویسی‌ها ثبت شوند:

- در سطح ممیزی `Metadata` یا بالاتر، حاشیه‌نویسی‌ای با کلید
  `mutation.webhook.admission.k8s.io/round_{round idx}_index_{order idx}` همراه با محتوای JSON ثبت
  می‌شود که نشان می‌دهد یک وب‌هوک برای درخواست مورد نظر فراخوانی شده و آیا آبجکت را تغییر داده است یا نه.

  برای نمونه، حاشیه‌نویسی زیر برای وب‌هوکی ثبت می‌شود که دوباره فراخوانی شده است. این وب‌هوک در
  زنجیرهٔ وب‌هوک‌های تغییردهنده در جایگاه سوم قرار دارد و در طول فراخوانی، آبجکت درخواست را تغییر
  نداده است.

  ```yaml
  # the audit event recorded
  {
      "kind": "Event",
      "apiVersion": "audit.k8s.io/v1",
      "annotations": {
          "mutation.webhook.admission.k8s.io/round_1_index_2": "{\"configuration\":\"my-mutating-webhook-configuration.example.com\",\"webhook\":\"my-webhook.example.com\",\"mutated\": false}"
          # other annotations
          ...
      }
      # other fields
      ...
  }
  ```

  ```yaml
  # the annotation value deserialized
  {
      "configuration": "my-mutating-webhook-configuration.example.com",
      "webhook": "my-webhook.example.com",
      "mutated": false
  }
  ```

  حاشیه‌نویسی زیر برای وب‌هوکی ثبت می‌شود که در دور نخست فراخوانی شده است. این وب‌هوک در زنجیرهٔ
  وب‌هوک‌های تغییردهنده در جایگاه نخست قرار دارد و در طول فراخوانی، آبجکت درخواست را تغییر داده است.

  ```yaml
  # the audit event recorded
  {
      "kind": "Event",
      "apiVersion": "audit.k8s.io/v1",
      "annotations": {
          "mutation.webhook.admission.k8s.io/round_0_index_0": "{\"configuration\":\"my-mutating-webhook-configuration.example.com\",\"webhook\":\"my-webhook-always-mutate.example.com\",\"mutated\": true}"
          # other annotations
          ...
      }
      # other fields
      ...
  }
  ```

  ```yaml
  # the annotation value deserialized
  {
      "configuration": "my-mutating-webhook-configuration.example.com",
      "webhook": "my-webhook-always-mutate.example.com",
      "mutated": true
  }
  ```

- در سطح ممیزی `Request` یا بالاتر، حاشیه‌نویسی‌ای با کلید
  `patch.webhook.admission.k8s.io/round_{round idx}_index_{order idx}` همراه با محتوای JSON ثبت
  می‌شود که نشان می‌دهد یک وب‌هوک برای درخواست مورد نظر فراخوانی شده و چه وصله‌ای روی آبجکت درخواست
  اعمال شده است.

  برای نمونه، حاشیه‌نویسی زیر برای وب‌هوکی ثبت می‌شود که دوباره فراخوانی شده است. این وب‌هوک در
  زنجیرهٔ وب‌هوک‌های تغییردهنده در جایگاه چهارم قرار دارد و با یک وصلهٔ JSON پاسخ داده است که روی
  آبجکت درخواست اعمال شده است.

  ```yaml
  # the audit event recorded
  {
      "kind": "Event",
      "apiVersion": "audit.k8s.io/v1",
      "annotations": {
          "patch.webhook.admission.k8s.io/round_1_index_3": "{\"configuration\":\"my-other-mutating-webhook-configuration.example.com\",\"webhook\":\"my-webhook-always-mutate.example.com\",\"patch\":[{\"op\":\"add\",\"path\":\"/data/mutation-stage\",\"value\":\"yes\"}],\"patchType\":\"JSONPatch\"}"
          # other annotations
          ...
      }
      # other fields
      ...
  }
  ```

  ```yaml
  # the annotation value deserialized
  {
      "configuration": "my-other-mutating-webhook-configuration.example.com",
      "webhook": "my-webhook-always-mutate.example.com",
      "patchType": "JSONPatch",
      "patch": [
          {
              "op": "add",
              "path": "/data/mutation-stage",
              "value": "yes"
          }
      ]
  }
  ```

### معیارهای وب‌هوک پذیرش

سرور API معیارهای Prometheus را از طریق نقطهٔ پایانی `/metrics` در دسترس قرار می‌دهد که می‌توان از آن‌ها برای پایش و عیب‌یابی وضعیت سرور API استفاده کرد. معیارهای زیر وضعیت مربوط به وب‌هوک‌های پذیرش را ثبت می‌کنند.

#### شمار ردهای وب‌هوک پذیرش در سرور API

گاهی دانستن اینکه کدام وب‌هوک‌های پذیرش مکرراً درخواست‌های API را رد می‌کنند و دلیل رد چیست، مفید است.

سرور API یک معیار شمارندهٔ (counter) Prometheus ارائه می‌کند که ردهای وب‌هوک پذیرش را ثبت می‌کند. این معیارها برچسب‌هایی دارند که علت یا علت‌های رد را مشخص می‌کنند:

- `name`: نام وب‌هوکی که درخواست را رد کرده است.
- `operation`: نوع عملیات درخواست؛ می‌تواند یکی از `CREATE`،
  `UPDATE`، `DELETE` و `CONNECT` باشد.
- `type`: نوع وب‌هوک پذیرش؛ می‌تواند یکی از `admit` و `validating` باشد.
- `error_type`: مشخص می‌کند آیا در طول فراخوانی وب‌هوک خطایی رخ داده است که به رد درخواست
  انجامیده باشد یا نه. مقدار آن می‌تواند یکی از موارد زیر باشد:

  - `calling_webhook_error`: خطاهای ناشناخته یا خطاهای اتمام مهلت زمانی از سوی وب‌هوک پذیرش رخ داده و
    [سیاست شکست](#failure-policy) وب‌هوک روی `Fail` تنظیم شده است.
  - `no_error`: هیچ خطایی رخ نداده است. وب‌هوک درخواست را با `allowed: false` در پاسخ پذیرش رد کرده
    است. برچسب `rejection_code` در این معیارها مقدار `.status.code` تنظیم‌شده در پاسخ پذیرش را ثبت می‌کند.
  - `apiserver_internal_error`: یک خطای داخلی در سرور API رخ داده است.

- `rejection_code`: کد وضعیت HTTP که هنگام رد درخواست از سوی وب‌هوک، در پاسخ پذیرش
  تنظیم شده است.

نمونه‌ای از معیارهای شمار ردها:

```
# HELP apiserver_admission_webhook_rejection_count [ALPHA] Admission webhook rejection count, identified by name and broken out for each admission type (validating or admit) and operation. Additional labels specify an error type (calling_webhook_error or apiserver_internal_error if an error occurred; no_error otherwise) and optionally a non-zero rejection code if the webhook rejects the request with an HTTP status code (honored by the apiserver when the code is greater or equal to 400). Codes greater than 600 are truncated to 600, to keep the metrics cardinality bounded.
# TYPE apiserver_admission_webhook_rejection_count counter
apiserver_admission_webhook_rejection_count{error_type="calling_webhook_error",name="always-timeout-webhook.example.com",operation="CREATE",rejection_code="0",type="validating"} 1
apiserver_admission_webhook_rejection_count{error_type="calling_webhook_error",name="invalid-admission-response-webhook.example.com",operation="CREATE",rejection_code="0",type="validating"} 1
apiserver_admission_webhook_rejection_count{error_type="no_error",name="deny-unwanted-configmap-data.example.com",operation="CREATE",rejection_code="400",type="validating"} 13
```

## بهترین شیوه‌ها و هشدارها

برای آشنایی با توصیه‌ها و ملاحظات مربوط به نوشتن وب‌هوک‌های پذیرش تغییردهنده،
[شیوه‌های خوب وب‌هوک‌های پذیرش](/docs/concepts/cluster-administration/admission-webhooks-good-practices) را ببینید.
