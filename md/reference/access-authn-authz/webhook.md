---
reviewers:
- erictune
- lavalamp
- deads2k
- liggitt
title: حالت Webhook
content_type: concept
weight: 36
---

<!-- overview -->
WebHook یک callback مبتنی بر HTTP است: یک درخواست HTTP POST که هنگام وقوع یک رویداد ارسال می‌شود؛ یعنی یک اعلان ساده‌ی رویداد از طریق HTTP POST. یک برنامه‌ی وب که WebHookها را پیاده‌سازی می‌کند، هنگام رخ دادن رویدادهای مشخص، پیامی را به یک URL ارسال (POST) می‌کند.


<!-- body -->
در صورت تعیین حالت `Webhook`، کوبرنتیز برای تعیین سطح دسترسی کاربران، از یک سرویس REST خارجی پرس‌وجو می‌کند.

## قالب فایل پیکربندی {#configuration-file-format}

حالت `Webhook` به یک فایل برای پیکربندی HTTP نیاز دارد که با فلگ `--authorization-webhook-config-file=SOME_FILENAME` مشخص می‌شود.

فایل پیکربندی از قالب فایل [kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) استفاده می‌کند. در این فایل، «users» به webhook سرور API و «clusters» به سرویس راه دور اشاره دارد.

نمونه‌ای از پیکربندی که از احراز هویت کلاینت مبتنی بر HTTPS استفاده می‌کند:

```yaml
# Kubernetes API version
apiVersion: v1
# kind of the API object
kind: Config
# clusters refers to the remote service.
clusters:
  - name: name-of-remote-authz-service
    cluster:
      # CA for verifying the remote service.
      certificate-authority: /path/to/ca.pem
      # URL of remote service to query. Must use 'https'. May not include parameters.
      server: https://authz.example.com/authorize

# users refers to the API Server's webhook configuration.
users:
  - name: name-of-api-server
    user:
      client-certificate: /path/to/cert.pem # cert for the webhook plugin to use
      client-key: /path/to/key.pem          # key matching the cert

# kubeconfig files require a context. Provide one for the API Server.
current-context: webhook
contexts:
- context:
    cluster: name-of-remote-authz-service
    user: name-of-api-server
  name: webhook
```

## بار داده‌ی درخواست‌ها {#request-payloads}

هنگامی که باید درباره‌ی مجوزدهی تصمیم‌گیری شود، سرور API یک آبجکت `SubjectAccessReview` از نوع `authorization.k8s.io/v1beta1` را که به‌صورت JSON سریالایز شده و عمل مورد نظر را توصیف می‌کند، POST می‌کند. این آبجکت شامل فیلدهایی است که کاربری را که قصد ارسال درخواست دارد توصیف می‌کنند، و همچنین یا جزئیات منبعی که به آن دسترسی پیدا می‌شود، یا ویژگی‌های درخواست را در بر دارد.

توجه داشته باشید که آبجکت‌های API مربوط به webhook تابع همان [قواعد سازگاری نسخه‌بندی](/docs/concepts/overview/kubernetes-api/) آبجکت‌های دیگر API کوبرنتیز هستند. پیاده‌سازان باید از تعهدات سازگاری سهل‌گیرانه‌تر برای آبجکت‌های بتا آگاه باشند و برای اطمینان از deserialize صحیح، فیلد "apiVersion" درخواست را بررسی کنند. علاوه بر این، سرور API باید گروه افزونه‌های API با نام `authorization.k8s.io/v1beta1` را فعال کند (`--runtime-config=authorization.k8s.io/v1beta1=true`).

نمونه‌ای از بدنه‌ی درخواست:

```json
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "spec": {
    "resourceAttributes": {
      "namespace": "kittensandponies",
      "verb": "get",
      "group": "unicorn.example.org",
      "resource": "pods"
    },
    "user": "jane",
    "group": [
      "group1",
      "group2"
    ]
  }
}
```

انتظار می‌رود سرویس راه دور فیلد `status` درخواست را پر کند و با اجازه دادن یا ندادن دسترسی پاسخ دهد. فیلد `spec` در بدنه‌ی پاسخ نادیده گرفته می‌شود و می‌توان آن را حذف کرد. یک پاسخ موافق به‌صورت زیر خواهد بود:

```json
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "status": {
    "allowed": true
  }
}
```

برای رد کردن دسترسی دو روش وجود دارد.

روش اول در بیشتر موارد ترجیح داده می‌شود و نشان می‌دهد که webhook مجوزدهی اجازه نمی‌دهد یا درباره‌ی درخواست «نظری ندارد»؛ اما اگر مجوزدهنده‌های (authorizer) دیگری پیکربندی شده باشند، به آن‌ها فرصت داده می‌شود که درخواست را مجاز کنند. اگر مجوزدهنده‌ی دیگری وجود نداشته باشد یا هیچ‌یک از آن‌ها درخواست را مجاز نکنند، درخواست ممنوع می‌شود. webhook پاسخ زیر را برمی‌گرداند:

```json
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "status": {
    "allowed": false,
    "reason": "user does not have read access to the namespace"
  }
}
```

روش دوم بلافاصله درخواست را رد می‌کند و ارزیابی توسط سایر مجوزدهنده‌های پیکربندی‌شده را کوتاه می‌کند (short-circuit). این روش فقط باید توسط webhookهایی به کار رود که اطلاعات دقیقی از پیکربندی کامل مجوزدهنده‌های کلاستر دارند. webhook پاسخ زیر را برمی‌گرداند:

```json
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "status": {
    "allowed": false,
    "denied": true,
    "reason": "user does not have read access to the namespace"
  }
}
```

دسترسی به مسیرهای غیرمنبعی (non-resource) به‌صورت زیر ارسال می‌شود:

```json
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "spec": {
    "nonResourceAttributes": {
      "path": "/debug",
      "verb": "get"
    },
    "user": "jane",
    "group": [
      "group1",
      "group2"
    ]
  }
}
```

{{< feature-state feature_gate_name="AuthorizeWithSelectors" >}}

هنگام فراخوانی یک webhook مجوزدهی، کوبرنتیز انتخابگرهای (selector) برچسب و فیلد را در درخواست به webhook مجوزدهی ارسال می‌کند. webhook مجوزدهی در صورت تمایل می‌تواند تصمیم‌های مجوزدهی خود را با در نظر گرفتن انتخابگرهای محدوده‌دار فیلد و برچسب اتخاذ کند.

[مستندات API مربوط به SubjectAccessReview](/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/) رهنمودهایی درباره‌ی نحوه‌ی تفسیر و پردازش این فیلدها توسط webhookهای مجوزدهی ارائه می‌دهد؛ به‌ویژه درباره‌ی استفاده از الزامات تجزیه‌شده (parsed requirements) به‌جای رشته‌های خام انتخابگر، و نحوه‌ی مدیریت ایمن عملگرهای ناشناخته.

```json
{
  "apiVersion": "authorization.k8s.io/v1beta1",
  "kind": "SubjectAccessReview",
  "spec": {
    "resourceAttributes": {
      "verb": "list",
      "group": "",
      "resource": "pods",
      "fieldSelector": {
        "requirements": [
          {"key":"spec.nodeName", "operator":"In", "values":["mynode"]}
        ]
      },
      "labelSelector": {
        "requirements": [
          {"key":"example.com/mykey", "operator":"In", "values":["myvalue"]}
        ]
      }
    },
    "user": "jane",
    "group": [
      "group1",
      "group2"
    ]
  }
}
```

مسیرهای غیرمنبعی عبارت‌اند از: `/api`، `/apis`، `/metrics`، `/logs`، `/debug`، `/healthz`، `/livez`، `/openapi/v2`، `/readyz` و `/version.`. کلاینت‌ها برای کشف منابع و نسخه‌های موجود روی سرور، به دسترسی به `/api`، `/api/*`، `/apis`، `/apis/*` و `/version` نیاز دارند. می‌توان دسترسی به سایر مسیرهای غیرمنبعی را بدون محدود کردن دسترسی به REST API مسدود کرد.

برای اطلاعات بیشتر، به [مستندات API مربوط به SubjectAccessReview](/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/) و [پیاده‌سازی webhook.go](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go) مراجعه کنید.
