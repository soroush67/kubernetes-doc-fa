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
علاوه بر [افزونه‌های پذیرش داخلی (compiled-in)](/docs/reference/access-authn-authz/admission-controllers/)،
می‌توان افزونه‌های پذیرش را به‌صورت افزونه‌های توسعه‌ای (extension) تولید کرد و آن‌ها را در قالب webhook اجرا نمود که در زمان اجرا پیکربندی می‌شوند.
این صفحه نحوهٔ ساخت، پیکربندی، استفاده و پایش admission webhookها را شرح می‌دهد.

<!-- body -->

## admission webhookها چیستند؟

Admission webhookها فراخوانی‌های HTTP (callback) هستند که درخواست‌های پذیرش را دریافت می‌کنند و پردازشی روی آن‌ها انجام می‌دهند. می‌توانید دو نوع admission webhook تعریف کنید:
[validating admission webhook](/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)
و
[mutating admission webhook](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook).
Mutating admission webhookها ابتدا فراخوانی می‌شوند و می‌توانند آبجکت‌های ارسال‌شده به API server را برای اعمال مقادیر پیش‌فرض سفارشی تغییر دهند.
پس از آنکه همهٔ تغییرات آبجکت کامل شد و آبجکت ورودی توسط API server اعتبارسنجی گردید،
validating admission webhookها فراخوانی می‌شوند و می‌توانند درخواست‌ها را برای اعمال سیاست‌های سفارشی رد کنند.

{{< note >}}
Admission webhookهایی که برای اعمال سیاست باید اطمینان داشته باشند که وضعیت نهایی آبجکت را مشاهده می‌کنند،
باید از validating admission webhook استفاده کنند، زیرا آبجکت‌ها پس از مشاهده توسط mutating webhookها همچنان قابل تغییرند.
{{< /note >}}

## آزمایش با admission webhookها

Admission webhookها در اصل بخشی از control plane کلاستر هستند. باید آن‌ها را با نهایت احتیاط
بنویسید و مستقر کنید. اگر قصد دارید admission webhookهای درجه‌ی تولید (production-grade) بنویسید یا مستقر کنید،
لطفاً [راهنماهای کاربر](/docs/reference/access-authn-authz/extensible-admission-controllers/#write-an-admission-webhook-server)
را مطالعه کنید.
در ادامه، نحوهٔ آزمایش سریع با admission webhookها شرح داده می‌شود.

### پیش‌نیازها

* اطمینان حاصل کنید که کنترل‌کننده‌های پذیرش MutatingAdmissionWebhook و ValidatingAdmissionWebhook
  فعال هستند.
  [اینجا](/docs/reference/access-authn-authz/admission-controllers/#is-there-a-recommended-set-of-admission-controllers-to-use)
  مجموعه‌ای از کنترل‌کننده‌های پذیرش توصیه‌شده برای فعال‌سازی عمومی آمده است.

* اطمینان حاصل کنید که API با نام `admissionregistration.k8s.io/v1` فعال است.

### نوشتن یک سرور admission webhook

لطفاً به پیاده‌سازی [سرور admission webhook](https://github.com/kubernetes/kubernetes/blob/release-1.21/test/images/agnhost/webhook/main.go)
مراجعه کنید که در یک آزمون e2e کوبرنتیز اعتبارسنجی شده است. این webhook درخواست
`AdmissionReview` ارسالی از سوی API serverها را پردازش می‌کند و تصمیم خود را
در قالب یک آبجکت `AdmissionReview` و با همان نسخه‌ای که دریافت کرده است بازمی‌گرداند.

برای جزئیات داده‌های ارسالی به webhookها، بخش [درخواست webhook](#request) را ببینید.

برای داده‌های مورد انتظار از webhookها، بخش [پاسخ webhook](#response) را ببینید.

سرور admission webhook نمونه، فیلد `ClientAuth` را
[خالی](https://github.com/kubernetes/kubernetes/blob/v1.22.0/test/images/agnhost/webhook/config.go#L38-L39)
می‌گذارد که مقدار پیش‌فرض آن `NoClientCert` است. این بدان معناست که سرور webhook
هویت کلاینت‌ها، که فرض بر این است API serverها هستند، را احراز هویت نمی‌کند. اگر به
mutual TLS یا روش‌های دیگری برای احراز هویت کلاینت‌ها نیاز دارید، به
بخش [احراز هویت API serverها](#authenticate-apiservers) مراجعه کنید.

### استقرار سرویس admission webhook

سرور webhook در آزمون e2e درون کلاستر کوبرنتیز و از طریق
[API مربوط به Deployment](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#deployment-v1-apps) مستقر می‌شود.
این آزمون همچنین یک [سرویس](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#service-v1-core)
را به‌عنوان درگاه جلویی (front-end) سرور webhook ایجاد می‌کند. به
[کد](https://github.com/kubernetes/kubernetes/blob/v1.22.0/test/e2e/apimachinery/webhook.go#L748) مراجعه کنید.

همچنین می‌توانید webhookهای خود را بیرون از کلاستر مستقر کنید. در این صورت باید
پیکربندی webhookهای خود را متناسب با آن به‌روزرسانی کنید.

### پیکربندی admission webhookها به‌صورت پویا

می‌توانید به‌صورت پویا مشخص کنید که کدام منابع مشمول کدام admission webhookها شوند. این کار از طریق
[ValidatingWebhookConfiguration](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#validatingwebhookconfiguration-v1-admissionregistration-k8s-io)
یا
[MutatingWebhookConfiguration](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#mutatingwebhookconfiguration-v1-admissionregistration-k8s-io)
انجام می‌شود.

در ادامه نمونه‌ای از `ValidatingWebhookConfiguration` آمده است؛ پیکربندی mutating webhook نیز مشابه آن است.
برای جزئیات هر فیلد پیکربندی، بخش [پیکربندی webhook](#webhook-configuration) را ببینید.

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
باید مقدار `<CA_BUNDLE>` را در مثال بالا با یک CA bundle معتبر جایگزین کنید؛
این مقدار یک CA bundle با رمزگذاری PEM (مقدار فیلد با Base64 کدگذاری می‌شود) برای اعتبارسنجی گواهی سرور webhook است.
{{< /note >}}

فیلد `scope` مشخص می‌کند که فقط منابع با دامنهٔ کلاستر ("Cluster") یا
منابع با دامنهٔ فضای نام ("Namespaced") با این قاعده تطبیق داده شوند. مقدار "&lowast;" به این معناست که هیچ محدودیتی در دامنه وجود ندارد.

{{< note >}}
هنگام استفاده از `clientConfig.service`، گواهی سرور باید برای
`<svc_name>.<svc_namespace>.svc` معتبر باشد.
{{< /note >}}

{{< note >}}
مهلت زمانی پیش‌فرض برای فراخوانی یک webhook برابر ۱۰ ثانیه است.
می‌توانید `timeout` را تنظیم کنید و توصیه می‌شود برای webhookها از مهلت زمانی کوتاه استفاده شود.
اگر فراخوانی webhook با پایان مهلت زمانی مواجه شود، درخواست مطابق
سیاست شکست (failure policy) آن webhook مدیریت می‌شود.
{{< /note >}}

هنگامی که یک API server درخواستی دریافت می‌کند که با یکی از `rules` تطبیق دارد،
API server یک درخواست `admissionReview` را مطابق آنچه در
`clientConfig` مشخص شده است به webhook ارسال می‌کند.

پس از ایجاد پیکربندی webhook، سیستم چند ثانیه زمان لازم دارد
تا پیکربندی جدید را اعمال کند.

### احراز هویت API serverها   {#authenticate-apiservers}

اگر admission webhookهای شما به احراز هویت نیاز دارند، می‌توانید
API serverها را طوری پیکربندی کنید که برای احراز هویت خود نزد
webhookها از basic auth، bearer token یا گواهی (cert) استفاده کنند. تکمیل این پیکربندی شامل سه مرحله است.

* هنگام راه‌اندازی API server، مکان فایل پیکربندی کنترل پذیرش را
  از طریق فلگ `--admission-control-config-file` مشخص کنید.

* در فایل پیکربندی کنترل پذیرش، مشخص کنید که کنترل‌کننده
  MutatingAdmissionWebhook و کنترل‌کننده ValidatingAdmissionWebhook
  باید اطلاعات احراز هویت را از کجا بخوانند. این اطلاعات در فایل‌های kubeConfig ذخیره می‌شوند
  (بله، با همان طرحواره‌ای که kubectl استفاده می‌کند)، بنابراین نام فیلد
  `kubeConfigFile` است. در ادامه نمونه‌ای از فایل پیکربندی کنترل پذیرش آمده است:

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

برای اطلاعات بیشتر دربارهٔ `AdmissionConfiguration`، به
[مرجع AdmissionConfiguration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/) مراجعه کنید.
برای جزئیات هر فیلد پیکربندی، بخش [پیکربندی webhook](#webhook-configuration) را ببینید.

در فایل kubeConfig، اطلاعات احراز هویت را ارائه کنید:

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

البته باید سرور webhook را طوری تنظیم کنید که این درخواست‌های احراز هویت را مدیریت کند.

### احراز هویت نزد admission webhookها {#authenticating-to-admission-webhooks}

{{< feature-state feature_gate_name="APIServerWebhookAuthenticationToken" >}}

به‌عنوان جایگزینی برای مدیریت دستی اطلاعات احراز هویت که در
[احراز هویت API serverها](#authenticate-apiservers) شرح داده شد، `kube-apiserver` می‌تواند
توکن‌های ServiceAccount کوتاه‌مدت و دارای دامنهٔ محدود را برای احراز هویت نزد admission
webhookها صادر کند. این سازوکار از API مربوط به
[TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
استفاده می‌کند تا توکن‌هایی صادر کند که به یک پیکربندی مشخص webhook متصل (bound) هستند و
به API groupهای خاصی محدود می‌شوند.

{{< note >}}
این سازوکار صدور توکن را پیاده‌سازی می‌کند. دریافت و ارائهٔ خودکار توکن
توسط `kube-apiserver` و API serverهای تجمیعی (aggregated) هنگام فراخوانی
webhookها، همراه با یک کتابخانهٔ تأیید توکن در سمت webhook، بخشی از
این سازوکار نیستند.
{{< /note >}}

#### نحوهٔ کار

API مربوط به TokenRequest گسترش یافته است تا از صدور توکن‌های متصل به
آبجکت‌های ValidatingWebhookConfiguration یا MutatingWebhookConfiguration پشتیبانی کند.
این توکن‌ها شامل ادعاهای گواهی (attestation claims) هستند که مشخص می‌کنند دارندهٔ توکن
مجاز است دربارهٔ کدام API groupها از webhook پرس‌وجو کند. اگر
پیکربندی webhook ارجاع‌شده حذف شود، توکن نامعتبر می‌شود.

برای درخواست یک توکن احراز هویت webhook، یک TokenRequest باید شامل موارد زیر باشد:

1. **یک فیلد `.spec.boundObjectRef`** که به یک ValidatingWebhookConfiguration یا
   یک MutatingWebhookConfiguration ارجاع می‌دهد. پیکربندی webhook ارجاع‌شده باید
   وجود داشته باشد و نباید برای حذف علامت‌گذاری شده باشد.

1. **یک فیلد `.spec.attestations`** با دقیقاً یک مدخل: کلید
   `admissionReviewAPIGroups` با مقداری از نوع آرایهٔ رشته‌ای تک‌عنصری که
   API group تحت پوشش این توکن را مشخص می‌کند. مقدار `"*"` به معنای همهٔ API groupهاست.
   API group مشخص‌شده باید با یکی از قواعد (rule) در پیکربندی webhook
   ارجاع‌شده مطابقت داشته باشد.

1. **یک فیلد `.spec.audiences`** با دقیقاً یک عنصر که با نقطهٔ پایانی (endpoint) webhook
   مطابقت دارد:
   - برای webhookهای پیکربندی‌شده با URL: audience باید دقیقاً با
     URL یکسان باشد.
   - برای webhookهای پیکربندی‌شده با service: audience باید با الگوی
     `https://<name>.<namespace>.svc:<port>[<path>]` مطابقت داشته باشد؛ در این الگو `<port>` به‌طور پیش‌فرض
     `443` است و اگر `<path>` در پیکربندی webhook مشخص نشده باشد، پیش‌فرض آن `/` است.

1. **یک مقدار `.spec.expirationSeconds`**. حداکثر زمان انقضای مجاز برای
   توکن‌های متصل به webhook برابر ۶۰۰ ثانیه (۱۰ دقیقه) است.

#### الزامات مجوزدهی

هنگام صدور یک توکن احراز هویت webhook، دو سطح از مجوزدهی بررسی می‌شود:

1. درخواست‌دهنده باید مجوز `create` را روی `serviceaccounts/token` برای
   حساب سرویس (service account) هدف داشته باشد (مجوزدهی استاندارد TokenRequest).

1. حساب سرویسی که در TokenRequest نام برده شده است باید مجوز `attest`
   را روی منبع `admissionReviewAPIGroups` در API group با نام `authentication.k8s.io`
   داشته باشد، با یک `resourceName` که با API group مشخص‌شده در
   attestation مطابقت دارد (یا `"*"` برای همهٔ API groupها).

پیکربندی RBAC نمونهٔ زیر به یک service account اجازه می‌دهد توکن‌های احراز هویت webhook را
با دامنهٔ API group با نام `mygroup.example.com` درخواست کند:

{{% code_sample language="yaml" file="access/extensible-admission-controllers/webhook-auth-attest-clusterrole.yaml" %}}

#### ادعاهای توکن و تأیید آن از طریق TokenReview

هنگامی که یک توکن احراز هویت webhook از طریق
[TokenReview](/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/)
تأیید می‌شود،
کلیدهای اضافی زیر در فیلد `.status.user.extra` پاسخ مقداردهی می‌شوند:

برای توکن‌های متصل به یک ValidatingWebhookConfiguration:
- `authentication.kubernetes.io/validatingwebhookconfiguration-name`
- `authentication.kubernetes.io/validatingwebhookconfiguration-uid`

برای توکن‌های متصل به یک MutatingWebhookConfiguration:
- `authentication.kubernetes.io/mutatingwebhookconfiguration-name`
- `authentication.kubernetes.io/mutatingwebhookconfiguration-uid`

برای همهٔ توکن‌های احراز هویت webhook:
- `attestation.authentication.kubernetes.io/admissionReviewAPIGroups` --
  API group که توکن برای آن مجاز است.

JWT زیرین این ادعاها را در فضای نام ادعاهای خصوصی `kubernetes.io` شامل می‌شود.
برای مثال، توکنی که به یک MutatingWebhookConfiguration متصل است:

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

## درخواست و پاسخ webhook

### درخواست {#request}

درخواست‌ها به webhookها به‌صورت POST و با `Content-Type: application/json` ارسال می‌شوند
و بدنهٔ آن‌ها یک آبجکت API با نام `AdmissionReview` از API group با نام `admission.k8s.io` است که
به JSON سریالیزه شده است.

Webhookها می‌توانند با فیلد `admissionReviewVersions` در پیکربندی خود مشخص کنند که
چه نسخه‌هایی از آبجکت‌های `AdmissionReview` را می‌پذیرند:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  admissionReviewVersions: ["v1", "v1beta1"]
```

`admissionReviewVersions` هنگام ایجاد پیکربندی webhook یک فیلد الزامی است.
Webhookها موظف‌اند دست‌کم از یک نسخهٔ `AdmissionReview` که API server فعلی و قبلی
آن را می‌شناسند پشتیبانی کنند.

API serverها نخستین نسخهٔ `AdmissionReview` از فهرست `admissionReviewVersions` را که خود پشتیبانی می‌کنند ارسال می‌کنند.
اگر هیچ‌یک از نسخه‌های فهرست توسط API server پشتیبانی نشود، ایجاد پیکربندی مجاز نخواهد بود.
اگر API server با پیکربندی webhookی روبه‌رو شود که پیش‌تر ایجاد شده است و از هیچ‌یک از نسخه‌های `AdmissionReview`
که API server می‌تواند ارسال کند پشتیبانی نمی‌کند، تلاش‌ها برای فراخوانی webhook ناموفق خواهد بود و مشمول [سیاست شکست](#failure-policy) می‌شود.

این مثال داده‌های موجود در یک آبجکت `AdmissionReview` را برای درخواست
به‌روزرسانی زیرمنبع `scale` از یک `Deployment` با نسخهٔ `apps/v1` نشان می‌دهد:

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

وب‌هوک‌ها با کد وضعیت HTTP برابر 200 و `Content-Type: application/json` پاسخ می‌دهند و بدنه‌ی پاسخ شامل یک آبجکت `AdmissionReview` (در همان نسخه‌ای که برای وب‌هوک ارسال شده است) است که بخش `response` در آن تکمیل و به JSON سریال‌سازی شده است.

بخش `response` دست‌کم باید شامل فیلدهای زیر باشد:

* `uid`، که از `request.uid` ارسال‌شده به وب‌هوک کپی می‌شود
* `allowed`، که مقدار آن یا `true` است یا `false`

نمونه‌ای از یک پاسخ حداقلی از سوی وب‌هوک برای اجازه دادن به یک درخواست:

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

نمونه‌ای از یک پاسخ حداقلی از سوی وب‌هوک برای رد یک درخواست:

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

هنگام رد کردن یک درخواست، وب‌هوک می‌تواند با استفاده از فیلد `status` کد HTTP و پیامی را که به کاربر بازگردانده می‌شود سفارشی کند. آبجکت status مشخص‌شده به کاربر بازگردانده می‌شود.
برای جزئیات بیشتر درباره‌ی نوع `status`، [مستندات API](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#status-v1-meta) را ببینید.
نمونه‌ای از پاسخ برای رد یک درخواست، همراه با سفارشی‌سازی کد وضعیت HTTP و پیامی که به کاربر نمایش داده می‌شود:

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

هنگام اجازه دادن به یک درخواست، یک وب‌هوک پذیرش از نوع mutating می‌تواند به‌صورت اختیاری آبجکت ورودی را نیز تغییر دهد.
این کار با استفاده از فیلدهای `patch` و `patchType` در پاسخ انجام می‌شود.
تنها `patchType` که در حال حاضر پشتیبانی می‌شود `JSONPatch` است.
برای جزئیات بیشتر، مستندات [JSON patch](https://jsonpatch.com/) را ببینید.
برای `patchType: JSONPatch`، فیلد `patch` شامل آرایه‌ای از عملیات JSON patch است که با base64 کدگذاری شده است.

برای مثال، یک عملیات patch منفرد که `spec.replicas` را تنظیم می‌کند، به این صورت است:
`[{"op": "add", "path": "/spec/replicas", "value": 3}]`

این مقدار پس از کدگذاری با Base64 به صورت `W3sib3AiOiAiYWRkIiwgInBhdGgiOiAiL3NwZWMvcmVwbGljYXMiLCAidmFsdWUiOiAzfV0=` درمی‌آید.

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

وب‌هوک‌های پذیرش می‌توانند به‌صورت اختیاری پیام‌های هشدار بازگردانند که در هدرهای HTTP با نام `Warning` و با کد هشدار 299 به کلاینت درخواست‌دهنده بازگردانده می‌شوند. هشدارها را می‌توان هم در پاسخ‌های پذیرش مجاز و هم در پاسخ‌های ردشده ارسال کرد.

اگر وب‌هوکی پیاده‌سازی می‌کنید که هشدار بازمی‌گرداند:

* پیشوند "Warning:" را در پیام قرار ندهید
* از پیام‌های هشدار برای شرح مشکلاتی استفاده کنید که کلاینتِ ارسال‌کننده‌ی درخواست API باید آن‌ها را اصلاح کند یا از آن‌ها آگاه باشد
* در صورت امکان، هشدارها را به 120 نویسه محدود کنید

{{< caution >}}
پیام‌های هشدار منفرد با بیش از 256 نویسه ممکن است پیش از بازگردانده شدن به کلاینت‌ها توسط API server کوتاه شوند.
اگر بیش از 4096 نویسه پیام هشدار (از همه‌ی منابع) اضافه شود، پیام‌های هشدار اضافی نادیده گرفته می‌شوند.
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

## پیکربندی وب‌هوک {#webhook-configuration}

برای ثبت وب‌هوک‌های پذیرش، آبجکت‌های API از نوع `MutatingWebhookConfiguration` یا `ValidatingWebhookConfiguration` را ایجاد کنید.
نام یک آبجکت `MutatingWebhookConfiguration` یا `ValidatingWebhookConfiguration` باید یک
[نام زیردامنه‌ی DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

{{< note >}}
نام‌هایی که به `.static.k8s.io` ختم می‌شوند برای
[کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
رزرو شده‌اند و نمی‌توان از آن‌ها برای پیکربندی‌های وب‌هوکِ مبتنی بر API استفاده کرد. این رزرو
زمانی اعمال می‌شود که
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ManifestBasedAdmissionControlConfig) با نام `ManifestBasedAdmissionControlConfig` فعال باشد.
{{< /note >}}

هر پیکربندی می‌تواند شامل یک یا چند وب‌هوک باشد.
اگر چند وب‌هوک در یک پیکربندی واحد مشخص شوند، باید به هر یک نامی یکتا داده شود.
این کار لازم است تا تطبیق لاگ‌های ممیزی و متریک‌های حاصل با پیکربندی‌های فعال آسان‌تر شود.

هر وب‌هوک موارد زیر را تعریف می‌کند.

### تطبیق درخواست‌ها: rules {#matching-requests-rules}

هر وب‌هوک باید فهرستی از قواعد (rules) را مشخص کند که برای تعیین این‌که آیا یک درخواست به API server باید به وب‌هوک ارسال شود یا خیر به کار می‌روند.
هر قاعده یک یا چند operation، apiGroup، apiVersion و resource و همچنین یک دامنه‌ی منبع (scope) را مشخص می‌کند:

* `operations` یک یا چند عملیاتی را که باید تطبیق داده شوند فهرست می‌کند. می‌تواند `"CREATE"`، `"UPDATE"`، `"DELETE"`، `"CONNECT"`
  یا `"*"` برای تطبیق همه باشد.
* `apiGroups` یک یا چند گروه API را که باید تطبیق داده شوند فهرست می‌کند. `""` گروه API هسته (core) است. `"*"` با همه‌ی گروه‌های API تطبیق می‌یابد.
* `apiVersions` یک یا چند نسخه‌ی API را که باید تطبیق داده شوند فهرست می‌کند. `"*"` با همه‌ی نسخه‌های API تطبیق می‌یابد.
* `resources` یک یا چند منبع را که باید تطبیق داده شوند فهرست می‌کند.

  * `"*"` با همه‌ی منابع تطبیق می‌یابد، اما با زیرمنبع‌ها (subresources) خیر.
  * `"*/*"` با همه‌ی منابع و زیرمنبع‌ها تطبیق می‌یابد.
  * `"pods/*"` با همه‌ی زیرمنبع‌های Pod ها تطبیق می‌یابد.
  * `"*/status"` با همه‌ی زیرمنبع‌های status تطبیق می‌یابد.

* `scope` دامنه‌ای را که باید تطبیق داده شود مشخص می‌کند. مقادیر معتبر `"Cluster"`، `"Namespaced"` و `"*"` هستند.
  زیرمنبع‌ها با دامنه‌ی منبع والد خود تطبیق می‌یابند. مقدار پیش‌فرض `"*"` است.

  * `"Cluster"` یعنی فقط منابعی که در سطح کلاستر هستند با این قاعده تطبیق می‌یابند (آبجکت‌های API از نوع Namespace در سطح کلاستر هستند).
  * `"Namespaced"` یعنی فقط منابعی که به فضای نام تعلق دارند با این قاعده تطبیق می‌یابند.
  * `"*"` یعنی هیچ محدودیتی از نظر دامنه وجود ندارد.

اگر یک درخواست ورودی با `operations`، `groups`، `versions`، `resources` و `scope` مشخص‌شده در هر یک از `rules` یک وب‌هوک تطبیق یابد، درخواست به آن وب‌هوک ارسال می‌شود.

در ادامه نمونه‌های دیگری از قواعد آمده است که می‌توان برای مشخص کردن منابعی که باید رهگیری شوند از آن‌ها استفاده کرد.

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

تطبیق درخواست‌های ایجاد برای همه‌ی منابع (اما نه زیرمنبع‌ها) در همه‌ی گروه‌ها و نسخه‌های API:

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

تطبیق درخواست‌های به‌روزرسانی برای همه‌ی زیرمنبع‌های `status` در همه‌ی گروه‌ها و نسخه‌های API:

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

### منابع مجازی مستثناشده {#excluded-virtual-resources}

{{< feature-state feature_gate_name="ExcludeAdmissionWebhookVirtualResources" >}}

وب‌هوک‌های پذیرش برای منابع احراز هویت و مجوزدهیِ غیرپایدار (مجازی) زیر فراخوانی نمی‌شوند، حتی اگر `rules` یک وب‌هوک با آن‌ها تطبیق داشته باشد:

* [TokenReviews]({{< relref "/docs/reference/kubernetes-api/definitions/token-review-v1-authentication/" >}})
* [SelfSubjectReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-review-v1-authentication/" >}})
* [LocalSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/local-subject-access-review-v1-authorization/" >}})
* [SelfSubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-access-review-v1-authorization/" >}})
* [SelfSubjectRulesReviews]({{< relref "/docs/reference/kubernetes-api/definitions/self-subject-rules-review-v1-authorization/" >}})
* [SubjectAccessReviews]({{< relref "/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/" >}})

وب‌هوکی که این منابع را رهگیری کند می‌تواند کلاستر را از مسیر احراز هویت و مجوزدهیِ خودش بیرون بیندازد: برای مثال، یک وب‌هوکِ دچار خطا که با `subjectaccessreviews` تطبیق دارد می‌تواند بررسی‌های مجوزدهی را که خود کلاستر به آن‌ها وابسته است مسدود کند. مستثنا کردن این منابع، وب‌هوک‌های پذیرش را با [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/) و [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/) هم‌راستا می‌کند، که همواره این منابع را مستثنا کرده‌اند.

اگر پیکربندی وب‌هوکی را با قاعده‌ای ایجاد یا به‌روزرسانی کنید که صراحتاً نام یکی از این منابع را آورده است، API server هشداری بازمی‌گرداند و به شما اطلاع می‌دهد که آن قاعده تأثیری ندارد. همچنین API server هنگام بارگذاری هر پیکربندی وب‌هوکِ موجودی که چنین قاعده‌ای دارد، نام آن را لاگ می‌کند تا بتوانید پیش از ارتقا کلاستر خود را بررسی کنید. قاعده‌هایی که فقط از طریق نویسه‌ی عام (`"*"`) در `apiGroups` یا `resources` با این منابع تطبیق می‌یابند علامت‌گذاری نمی‌شوند، زیرا قصد آن‌ها مبهم است.

رهگیری این منابع مجازی توسط وب‌هوک‌ها از کوبرنتیز v1.37 منسوخ شده است. به‌عنوان یک راهکار موقت، می‌توانید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/#ExcludeAdmissionWebhookVirtualResources) با نام `ExcludeAdmissionWebhookVirtualResources` را روی `false` تنظیم کنید تا رفتار قبلی بازگردانده شود. برنامه این است که وقتی این قابلیت به مرحله‌ی پایدار برسد، این feature gate روی حالت فعال قفل شود و پس از آن وب‌هوک‌های پذیرش دیگر نتوانند این منابع را رهگیری کنند.

### تطبیق درخواست‌ها: objectSelector {#matching-requests-objectselector}

وب‌هوک‌ها می‌توانند با مشخص کردن یک `objectSelector`، به‌صورت اختیاری رهگیری درخواست‌ها را بر اساس برچسب‌های آبجکت‌هایی که برایشان ارسال می‌شوند محدود کنند. در صورت مشخص شدن، objectSelector هم روی object و هم روی oldObject که به وب‌هوک ارسال می‌شود ارزیابی می‌شود و اگر هر یک از این دو آبجکت با انتخابگر (selector) تطبیق یابد، تطبیق‌یافته در نظر گرفته می‌شود.

یک آبجکت null (`oldObject` در مورد ایجاد، یا `newObject` در مورد حذف)، یا آبجکتی که نمی‌تواند برچسب داشته باشد (مانند آبجکت `DeploymentRollback` یا `PodProxyOptions`)، تطبیق‌یافته در نظر گرفته نمی‌شود.

از انتخابگر آبجکت فقط در صورتی استفاده کنید که وب‌هوک به‌صورت opt-in عمل می‌کند، زیرا کاربران نهایی می‌توانند با تنظیم برچسب‌ها از وب‌هوک پذیرش عبور کنند.

این مثال یک وب‌هوک از نوع mutating را نشان می‌دهد که با `CREATE` هر منبعی (اما نه زیرمنبع‌ها) که برچسب `foo: bar` را دارد تطبیق می‌یابد:

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

برای نمونه‌های بیشتر از انتخابگرهای برچسب، [مفهوم برچسب‌ها](/docs/concepts/overview/working-with-objects/labels) را ببینید.

### تطبیق درخواست‌ها: namespaceSelector {#matching-requests-namespaceselector}

وب‌هوک‌ها می‌توانند با مشخص کردن یک `namespaceSelector`، به‌صورت اختیاری رهگیری درخواست‌ها برای منابعِ دارای فضای نام را بر اساس برچسب‌های فضای نام حاوی آن‌ها محدود کنند.

`namespaceSelector` بر اساس این‌که برچسب‌های فضای نام با انتخابگر تطبیق دارند یا خیر، تصمیم می‌گیرد که آیا وب‌هوک روی درخواستی برای یک منبعِ دارای فضای نام (یا یک آبجکت Namespace) اجرا شود یا نه.
اگر خود آبجکت یک فضای نام باشد، تطبیق روی object.metadata.labels انجام می‌شود.
اگر آبجکت یک منبع در سطح کلاستر غیر از Namespace باشد، `namespaceSelector` تأثیری ندارد.

این مثال یک وب‌هوک از نوع mutating را نشان می‌دهد که با `CREATE` هر منبعِ دارای فضای نام در فضای نامی که برچسب "runlevel" آن برابر "0" یا "1" نیست تطبیق می‌یابد:

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

این مثال یک وب‌هوک از نوع validating را نشان می‌دهد که با `CREATE` هر منبعِ دارای فضای نام در فضای نامی که با "environment" برابر "prod" یا "staging" مرتبط است تطبیق می‌یابد:

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

برای نمونه‌های بیشتر از انتخابگرهای برچسب، [مفهوم برچسب‌ها](/docs/concepts/overview/working-with-objects/labels) را ببینید.

### تطبیق درخواست‌ها: matchPolicy {#matching-requests-matchpolicy}

API serverها می‌توانند آبجکت‌ها را از طریق چند گروه یا نسخه‌ی API در دسترس قرار دهند.

برای مثال، اگر یک وب‌هوک فقط برای برخی گروه‌ها/نسخه‌های API قاعده‌ای مشخص کرده باشد
(مانند `apiGroups:["apps"], apiVersions:["v1","v1beta1"]`)
و درخواستی برای تغییر منبع از طریق گروه/نسخه‌ی API دیگری (مانند `extensions/v1beta1`) صادر شود،
آن درخواست به وب‌هوک ارسال نخواهد شد.

`matchPolicy` به وب‌هوک اجازه می‌دهد تعیین کند `rules` آن چگونه برای تطبیق درخواست‌های ورودی به کار روند.
مقادیر مجاز `Exact` یا `Equivalent` هستند.

* `Exact` یعنی یک درخواست فقط در صورتی باید رهگیری شود که دقیقاً با یکی از قواعد مشخص‌شده تطبیق یابد.
* `Equivalent` یعنی یک درخواست در صورتی باید رهگیری شود که منبعی را که در `rules` فهرست شده است تغییر دهد، حتی اگر از طریق گروه یا نسخه‌ی API دیگری باشد.

در مثال بالا، وب‌هوکی که فقط برای `apps/v1` ثبت شده بود می‌توانست از `matchPolicy` استفاده کند:

* `matchPolicy: Exact` یعنی درخواست `extensions/v1beta1` به وب‌هوک ارسال نمی‌شود
* `matchPolicy: Equivalent` یعنی درخواست `extensions/v1beta1` به وب‌هوک ارسال می‌شود
  (با تبدیل آبجکت‌ها به نسخه‌ای که وب‌هوک مشخص کرده بود: `apps/v1`)

مشخص کردن `Equivalent` توصیه می‌شود و تضمین می‌کند که وب‌هوک‌ها هنگامی که ارتقاها نسخه‌های جدید منبع را در API server فعال می‌کنند، همچنان منابعی را که انتظار دارند رهگیری کنند.

وقتی ارائه‌ی یک منبع توسط API server متوقف می‌شود، دیگر معادل نسخه‌های دیگر آن منبع که هنوز ارائه می‌شوند در نظر گرفته نمی‌شود.
برای مثال، deploymentهای `extensions/v1beta1` ابتدا منسوخ و سپس (در کوبرنتیز v1.16) حذف شدند.

از زمان آن حذف، وب‌هوکی با قاعده‌ی `apiGroups:["extensions"], apiVersions:["v1beta1"], resources:["deployments"]`
deploymentهایی را که از طریق APIهای `apps/v1` ایجاد می‌شوند رهگیری نمی‌کند. به همین دلیل، وب‌هوک‌ها باید ترجیحاً برای نسخه‌های پایدار منابع ثبت شوند.

این مثال یک وب‌هوک از نوع validating را نشان می‌دهد که تغییرات deploymentها را (صرف‌نظر از گروه یا نسخه‌ی API) رهگیری می‌کند و همواره یک آبجکت `Deployment` از `apps/v1` دریافت می‌کند:

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

مقدار پیش‌فرض `matchPolicy` برای وب‌هوک‌های پذیرش `Equivalent` است.

### تطبیق درخواست‌ها: `matchConditions` {#matching-requests-matchconditions}

{{< feature-state feature_gate_name="AdmissionWebhookMatchConditions" >}}

اگر به فیلتر کردن دقیق‌تر درخواست‌ها نیاز دارید، می‌توانید برای وب‌هوک‌ها _شرایط تطبیق_ (match conditions) تعریف کنید. این شرایط زمانی مفید هستند که قواعد تطبیق، `objectSelectors` و `namespaceSelectors` همچنان فیلتری را که می‌خواهید بر این‌که چه زمانی از طریق HTTP فراخوانی انجام شود فراهم نمی‌کنند. شرایط تطبیق [عبارت‌های CEL](/docs/reference/using-api/cel/) هستند. برای این‌که وب‌هوک فراخوانی شود، همه‌ی شرایط تطبیق باید به true ارزیابی شوند.

در اینجا مثالی آمده است که چند کاربرد مختلف از شرایط تطبیق را نشان می‌دهد:

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
می‌توانید در فیلد `matchConditions` برای هر وب‌هوک حداکثر 64 عنصر تعریف کنید.
{{< /note >}}

شرایط تطبیق به متغیرهای CEL زیر دسترسی دارند:

- `object` - آبجکت موجود در درخواست ورودی. مقدار آن برای درخواست‌های DELETE برابر null است. نسخه‌ی آبجکت ممکن است بر اساس [matchPolicy](#matching-requests-matchpolicy) تبدیل شود.
- `oldObject` - آبجکت موجود. مقدار آن برای درخواست‌های CREATE برابر null است.
- `request` - بخش درخواست از [AdmissionReview](#request)، به‌جز `object` و `oldObject`.
- `authorizer` - یک CEL Authorizer. می‌توان از آن برای انجام بررسی‌های مجوزدهی برای principal (کاربر احراز هویت‌شده) درخواست استفاده کرد. برای جزئیات بیشتر، بخش
  [Authz](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz) را در مستندات کتابخانه‌ی CEL کوبرنتیز ببینید.
- `authorizer.requestResource` - میان‌بری برای یک بررسی مجوزدهی که با منبع درخواست (group، resource، (subresource)، namespace، name) پیکربندی شده است.

برای اطلاعات بیشتر درباره‌ی عبارت‌های CEL، به
[مرجع Common Expression Language در کوبرنتیز](/docs/reference/using-api/cel/) مراجعه کنید.

در صورت بروز خطا هنگام ارزیابی یک شرط تطبیق، وب‌هوک هرگز فراخوانی نمی‌شود. اینکه درخواست رد شود یا نه، به شرح زیر تعیین می‌شود:

1. اگر **هر** شرط تطبیقی به `false` ارزیابی شود (صرف‌نظر از خطاهای دیگر)، API server وب‌هوک را نادیده می‌گیرد.
2. در غیر این صورت:
    - برای [`failurePolicy: Fail`](#failure-policy)، درخواست رد می‌شود (بدون فراخوانی وب‌هوک).
    - برای [`failurePolicy: Ignore`](#failure-policy)، درخواست ادامه می‌یابد اما وب‌هوک نادیده گرفته می‌شود.

### تماس با webhook

پس از آنکه API server تشخیص داد که یک درخواست باید به یک webhook ارسال شود،
باید بداند چگونه با آن webhook تماس بگیرد. این موضوع در بخش `clientConfig`
از پیکربندی webhook مشخص می‌شود.

webhookها را می‌توان از طریق یک URL یا یک ارجاع به سرویس (service reference) فراخوانی کرد
و در صورت نیاز می‌توان یک CA bundle سفارشی برای تأیید اتصال TLS در آن‌ها قرار داد.

#### URL

مقدار `url` نشانی webhook را به شکل استاندارد URL
(`scheme://host:port/path`) مشخص می‌کند.

مقدار `host` نباید به سرویسی اشاره کند که درون کلاستر در حال اجراست؛ برای این منظور
به‌جای آن با تعیین فیلد `service` از یک ارجاع به سرویس استفاده کنید.
در برخی API serverها ممکن است host از طریق DNS خارجی تفسیر و resolve شود
(برای مثال، `kube-apiserver` نمی‌تواند DNS داخل کلاستر را resolve کند، زیرا این کار
نقض لایه‌بندی (layering violation) خواهد بود). `host` می‌تواند یک نشانی IP نیز باشد.

توجه داشته باشید که استفاده از `localhost` یا `127.0.0.1` به‌عنوان `host`
پرخطر است، مگر آنکه دقت زیادی به خرج دهید تا این webhook روی تمام هاست‌هایی اجرا شود
که یک API server را اجرا می‌کنند و ممکن است لازم باشد با این webhook تماس بگیرند.
چنین نصب‌هایی به احتمال زیاد قابل‌حمل نیستند یا به‌سادگی در یک کلاستر جدید اجرا نمی‌شوند.

scheme باید "https" باشد؛ یعنی URL باید با "https://" آغاز شود.

استفاده از نام کاربری یا احراز هویت پایه (basic auth) (برای مثال `user:password@`) مجاز نیست.
همچنین fragmentها (`#...`) و پارامترهای query (`?...`) مجاز نیستند.

در ادامه مثالی از یک mutating webhook آمده است که برای فراخوانی یک URL پیکربندی شده است
(و انتظار دارد گواهی TLS با استفاده از ریشه‌های اعتماد سیستم تأیید شود، بنابراین caBundle را مشخص نمی‌کند):

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  clientConfig:
    url: "https://my-webhook.example.com:9443/my-webhook-path"
```

#### ارجاع به سرویس

بخش `service` درون `clientConfig` ارجاعی به سرویس این webhook است.
اگر webhook درون کلاستر در حال اجراست، باید به‌جای `url` از `service` استفاده کنید.
فضای نام (namespace) و نام سرویس الزامی هستند. پورت اختیاری است و مقدار پیش‌فرض آن 443 است.
مسیر (path) اختیاری است و مقدار پیش‌فرض آن "/" است.

در ادامه مثالی از یک mutating webhook آمده است که برای فراخوانی یک سرویس روی پورت "1234"
در زیرمسیر "/my-path" پیکربندی شده است و اتصال TLS را با استفاده از یک CA bundle سفارشی
در برابر ServerName برابر با `my-service-name.my-service-namespace.svc` تأیید می‌کند:

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
باید مقدار `<CA_BUNDLE>` را در مثال بالا با یک CA bundle معتبر جایگزین کنید؛
این مقدار یک CA bundle با کدگذاری PEM است که برای اعتبارسنجی گواهی سرور webhook به کار می‌رود.
{{< /note >}}

### عوارض جانبی

webhookها معمولاً فقط روی محتوای `AdmissionReview` ارسال‌شده به آن‌ها عمل می‌کنند.
با این حال، برخی webhookها در جریان پردازش درخواست‌های admission تغییراتی خارج از این جریان (out-of-band) اعمال می‌کنند.

webhookهایی که تغییرات out-of-band اعمال می‌کنند («عوارض جانبی» یا side effects) باید یک سازوکار تطبیق (reconciliation)
نیز داشته باشند (مانند یک کنترل‌کننده) که به‌صورت دوره‌ای وضعیت واقعی سیستم را تعیین کند و
داده‌های out-of-band را که توسط admission webhook تغییر یافته‌اند، مطابق با واقعیت تنظیم کند.
دلیل این امر آن است که فراخوانی یک admission webhook تضمین نمی‌کند که آبجکت پذیرفته‌شده همان‌گونه که هست، یا اصلاً، ذخیره شود.
webhookهای بعدی می‌توانند محتوای آبجکت را تغییر دهند، ممکن است هنگام نوشتن در ذخیره‌سازی با تعارض (conflict) مواجه شویم،
یا سرور ممکن است پیش از ذخیره‌شدن آبجکت خاموش شود.

علاوه بر این، webhookهای دارای عوارض جانبی باید هنگام پردازش درخواست‌های admission با `dryRun: true`
از اعمال این عوارض جانبی صرف‌نظر کنند.
یک webhook باید به‌صراحت اعلام کند که هنگام اجرا با `dryRun` عارضه جانبی نخواهد داشت،
در غیر این صورت درخواست dry-run به webhook ارسال نخواهد شد و درخواست API با شکست مواجه می‌شود.

webhookها با استفاده از فیلد `sideEffects` در پیکربندی webhook مشخص می‌کنند که آیا عوارض جانبی دارند یا خیر:

* `None`: فراخوانی webhook هیچ عارضه جانبی نخواهد داشت.
* `NoneOnDryRun`: فراخوانی webhook احتمالاً عوارض جانبی خواهد داشت، اما اگر درخواستی با
  `dryRun: true` به webhook ارسال شود، webhook عوارض جانبی را سرکوب می‌کند (webhook
  از `dryRun` آگاه است).

در ادامه مثالی از یک validating webhook آمده است که اعلام می‌کند برای درخواست‌های `dryRun: true` عارضه جانبی ندارد:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    sideEffects: NoneOnDryRun
```

### مهلت‌های زمانی (Timeouts)

از آنجا که webhookها به تأخیر درخواست‌های API می‌افزایند، باید در کمترین زمان ممکن ارزیابی را انجام دهند.
فیلد `timeoutSeconds` امکان پیکربندی این را فراهم می‌کند که API server تا چه مدت برای پاسخ یک webhook منتظر بماند
تا فراخوانی را شکست‌خورده تلقی کند.

اگر مهلت زمانی پیش از پاسخ webhook به پایان برسد، فراخوانی webhook نادیده گرفته می‌شود یا
درخواست API بر اساس [سیاست شکست](#failure-policy) رد می‌شود.

مقدار مهلت زمانی باید بین 1 تا 30 ثانیه باشد.

در ادامه مثالی از یک validating webhook با مهلت زمانی سفارشی 2 ثانیه آمده است:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
webhooks:
  - name: my-webhook.example.com
    timeoutSeconds: 2
```

مهلت زمانی پیش‌فرض برای یک admission webhook برابر با 10 ثانیه است.

### سیاست فراخوانی مجدد (Reinvocation policy)

یک ترتیب واحد از افزونه‌های mutating admission (از جمله webhookها) برای همه حالت‌ها کارآمد نیست
(برای نمونه به https://issue.k8s.io/64333 مراجعه کنید). یک mutating webhook می‌تواند ساختار فرعی جدیدی
به آبجکت اضافه کند (مانند افزودن یک `container` به یک `pod`)، و سایر افزونه‌های mutating که پیش‌تر
اجرا شده‌اند ممکن است درباره این ساختارهای جدید نظر یا قاعده‌ای داشته باشند (مانند تنظیم `imagePullPolicy` روی همه کانتینرها).

برای آنکه افزونه‌های mutating admission بتوانند تغییرات اعمال‌شده توسط افزونه‌های دیگر را مشاهده کنند،
اگر یک mutating webhook آبجکتی را تغییر دهد، افزونه‌های mutating admission درونی (built-in) دوباره اجرا می‌شوند،
و mutating webhookها می‌توانند با تعیین `reinvocationPolicy` مشخص کنند که آیا خودشان نیز دوباره فراخوانی شوند یا خیر.

مقدار `reinvocationPolicy` می‌تواند `Never` یا `IfNeeded` باشد. مقدار پیش‌فرض آن `Never` است.

* `Never`: webhook نباید در یک ارزیابی admission منفرد بیش از یک بار فراخوانی شود.
* `IfNeeded`: اگر آبجکتِ در حال پذیرش پس از فراخوانی اولیه webhook توسط افزونه‌های admission دیگر تغییر کند،
  webhook ممکن است به‌عنوان بخشی از ارزیابی admission دوباره فراخوانی شود.

نکات مهمی که باید به آن‌ها توجه کرد:

* تضمین نمی‌شود که تعداد فراخوانی‌های اضافی دقیقاً یک بار باشد.
* اگر فراخوانی‌های اضافی به تغییرات بیشتری در آبجکت منجر شوند، تضمین نمی‌شود که webhookها
  دوباره فراخوانی شوند.
* ترتیب webhookهایی که از این گزینه استفاده می‌کنند ممکن است برای کمینه‌کردن تعداد فراخوانی‌های اضافی تغییر کند.
* برای اعتبارسنجی یک آبجکت پس از آنکه تکمیل شدن همه تغییرات تضمین شده است، به‌جای آن از یک validating admission
  webhook استفاده کنید (برای webhookهای دارای عوارض جانبی توصیه می‌شود).

در ادامه مثالی از یک mutating webhook آمده است که انتخاب کرده است در صورت تغییر آبجکت توسط افزونه‌های admission بعدی
دوباره فراخوانی شود:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  reinvocationPolicy: IfNeeded
```

mutating webhookها باید [خودتوان (idempotent)](#idempotence) باشند؛ یعنی بتوانند آبجکتی را که پیش‌تر پذیرفته
و احتمالاً تغییر داده‌اند، با موفقیت پردازش کنند. این موضوع برای همه mutating admission webhookها صادق است، زیرا هر تغییری که
بتوانند در یک آبجکت اعمال کنند ممکن است از قبل در آبجکت ارائه‌شده توسط کاربر وجود داشته باشد، اما برای webhookهایی که
فراخوانی مجدد را انتخاب می‌کنند، این امر ضروری است.

### سیاست شکست (Failure policy)

فیلد `failurePolicy` مشخص می‌کند که خطاهای رخ‌داده هنگام _فراخوانی_ admission webhook چگونه مدیریت شوند.
مقادیر مجاز `Ignore` یا `Fail` هستند.

* `Ignore` به این معناست که خطای فراخوانی webhook نادیده گرفته می‌شود و درخواست API اجازه ادامه می‌یابد.
* `Fail` به این معناست که خطای فراخوانی webhook باعث شکست admission و رد شدن درخواست API می‌شود.

سیاست شکست برای انواع خطاهای زیر اعمال می‌شود:

* خطاهای شبکه، مهلت‌های زمانی یا شکست در اتصال هنگام تماس با webhook.
* webhook یک پاسخ HTTP غیر 2xx یا یک پاسخ نامعتبر (malformed) برگرداند.
* API server در سریال‌سازی درخواست admission یا ایجاد یک کلاینت HTTP داخلی برای webhook ناموفق باشد.
* (فقط برای mutating webhookها) پاسخ شامل نوع patch غیرقابل رمزگشایی یا پشتیبانی‌نشده باشد.

اگر نوشتن در API کوبرنتیز از طریق یک فراخوانی admission رد شود، این یک _رد شدن (rejection)_ است،
اما کوبرنتیز آن را شکست (failure) به حساب نمی‌آورد.
API server کوبرنتیز زمانی که به webhook با موفقیت دسترسی پیدا می‌کند و پیاده‌سازی webhook
درخواست را به‌صراحت رد کرده است (با تعیین `allowed: false` در پاسخ)، سیاست شکست را **اعمال نمی‌کند**.
یک رد صریح که به‌درستی منتقل شده باشد، صرف‌نظر از تنظیم `failurePolicy`، همیشه درخواست API را رد می‌کند.

در ادامه یک mutating webhook آمده است که پیکربندی شده تا در صورت بروز خطا هنگام فراخوانی admission webhook، درخواست API را رد کند:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
webhooks:
- name: my-webhook.example.com
  failurePolicy: Fail
```

مقدار پیش‌فرض `failurePolicy` برای admission webhookها برابر `Fail` است.

## پایش admission webhookها

API server راه‌هایی برای پایش رفتار admission webhookها فراهم می‌کند. این
سازوکارهای پایش به مدیران کلاستر کمک می‌کنند به پرسش‌هایی از این دست پاسخ دهند:

1. کدام mutating webhook آبجکت را در یک درخواست API تغییر داده است؟

2. mutating webhook چه تغییری را روی آبجکت اعمال کرده است؟

3. کدام webhookها به‌طور مکرر درخواست‌های API را رد می‌کنند؟ دلیل رد شدن چیست؟

### حاشیه‌نویسی‌های ممیزی (auditing annotations) برای mutating webhook

گاهی دانستن اینکه کدام mutating webhook آبجکت را در یک درخواست API تغییر داده و webhook چه تغییری
اعمال کرده است، مفید است.

API server کوبرنتیز روی هر فراخوانی mutating webhook [ممیزی (auditing)](/docs/tasks/debug/debug-cluster/audit/) انجام می‌دهد.
هر فراخوانی یک حاشیه‌نویسی (annotation) ممیزی تولید می‌کند که ثبت می‌کند آیا آبجکت درخواست توسط آن فراخوانی تغییر کرده است یا خیر،
و به‌صورت اختیاری یک annotation تولید می‌کند که patch اعمال‌شده از پاسخ admission webhook را ثبت می‌کند. این annotationها
در رویداد ممیزی (audit event) مربوط به درخواست داده‌شده و در مرحله‌ای مشخص از اجرای آن تنظیم می‌شوند؛ سپس این رویداد
بر اساس یک سیاست مشخص پیش‌پردازش شده و در یک backend نوشته می‌شود.

سطح ممیزی (audit level) یک رویداد تعیین می‌کند کدام annotationها ثبت شوند:

- در سطح ممیزی `Metadata` یا بالاتر، یک annotation با کلید
  `mutation.webhook.admission.k8s.io/round_{round idx}_index_{order idx}` همراه با یک payload از نوع JSON ثبت می‌شود
  که نشان می‌دهد یک webhook برای درخواست داده‌شده فراخوانی شده است و اینکه آبجکت را تغییر داده است یا خیر.

  برای مثال، annotation زیر برای یک webhook که دوباره فراخوانی شده ثبت می‌شود. این webhook
  در زنجیره mutating webhookها سومین webhook است و در طول فراخوانی، آبجکت درخواست را تغییر نداده است.

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

  annotation زیر برای یک webhook که در دور اول فراخوانی شده ثبت می‌شود. این webhook
  در زنجیره mutating webhookها اولین webhook است و در طول فراخوانی، آبجکت درخواست را تغییر داده است.

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

- در سطح ممیزی `Request` یا بالاتر، یک annotation با کلید
  `patch.webhook.admission.k8s.io/round_{round idx}_index_{order idx}` همراه با یک payload از نوع JSON ثبت می‌شود
  که نشان می‌دهد یک webhook برای درخواست داده‌شده فراخوانی شده است و چه patchی روی آبجکت درخواست اعمال شده است.

  برای مثال، annotation زیر برای یک webhook که دوباره فراخوانی شده ثبت می‌شود. این webhook در زنجیره
  mutating webhookها چهارمین webhook است و با یک JSON patch پاسخ داده که روی آبجکت درخواست اعمال شده است.

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

### متریک‌های admission webhook

API server متریک‌های Prometheus را از طریق نقطه پایانی `/metrics` ارائه می‌کند که می‌توان از آن‌ها برای پایش و
عیب‌یابی وضعیت API server استفاده کرد. متریک‌های زیر وضعیت مرتبط با admission webhookها را ثبت می‌کنند.

#### تعداد رد شدن‌ها توسط admission webhookها در API server

گاهی دانستن اینکه کدام admission webhookها به‌طور مکرر درخواست‌های API را رد می‌کنند و
دلیل رد شدن چیست، مفید است.

API server یک متریک شمارنده (counter) در Prometheus ارائه می‌کند که رد شدن‌ها توسط admission webhookها را ثبت می‌کند.
این متریک‌ها برای مشخص‌کردن علت‌های رد شدن توسط webhook(ها) برچسب‌گذاری شده‌اند:

- `name`: نام webhookی که درخواست را رد کرده است.
- `operation`: نوع عملیات درخواست، که می‌تواند یکی از `CREATE`،
  `UPDATE`، `DELETE` و `CONNECT` باشد.
- `type`: نوع admission webhook، که می‌تواند یکی از `admit` و `validating` باشد.
- `error_type`: مشخص می‌کند که آیا در طول فراخوانی webhook خطایی رخ داده که
  باعث رد شدن شده است. مقدار آن می‌تواند یکی از موارد زیر باشد:

  - `calling_webhook_error`: خطاهای ناشناخته یا خطاهای مهلت زمانی از سوی admission webhook رخ داده است و
    [سیاست شکست](#failure-policy) webhook روی `Fail` تنظیم شده است.
  - `no_error`: هیچ خطایی رخ نداده است. webhook درخواست را با `allowed: false` در پاسخ admission
    رد کرده است. برچسب متریک `rejection_code` مقدار `.status.code` تنظیم‌شده در پاسخ admission را ثبت می‌کند.
  - `apiserver_internal_error`: یک خطای داخلی API server رخ داده است.

- `rejection_code`: کد وضعیت HTTP که هنگام رد کردن یک درخواست توسط webhook
  در پاسخ admission تنظیم شده است.

نمونه‌ای از متریک‌های تعداد رد شدن‌ها:

```
# HELP apiserver_admission_webhook_rejection_count [ALPHA] Admission webhook rejection count, identified by name and broken out for each admission type (validating or admit) and operation. Additional labels specify an error type (calling_webhook_error or apiserver_internal_error if an error occurred; no_error otherwise) and optionally a non-zero rejection code if the webhook rejects the request with an HTTP status code (honored by the apiserver when the code is greater or equal to 400). Codes greater than 600 are truncated to 600, to keep the metrics cardinality bounded.
# TYPE apiserver_admission_webhook_rejection_count counter
apiserver_admission_webhook_rejection_count{error_type="calling_webhook_error",name="always-timeout-webhook.example.com",operation="CREATE",rejection_code="0",type="validating"} 1
apiserver_admission_webhook_rejection_count{error_type="calling_webhook_error",name="invalid-admission-response-webhook.example.com",operation="CREATE",rejection_code="0",type="validating"} 1
apiserver_admission_webhook_rejection_count{error_type="no_error",name="deny-unwanted-configmap-data.example.com",operation="CREATE",rejection_code="400",type="validating"} 13
```

## بهترین روش‌ها و هشدارها

برای مشاهده توصیه‌ها و ملاحظات هنگام نوشتن mutating admission webhookها،
به
[روش‌های خوب برای Admission Webhookها](/docs/concepts/cluster-administration/admission-webhooks-good-practices)
مراجعه کنید.
