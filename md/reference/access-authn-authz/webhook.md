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
وب‌هوک (WebHook) یک فراخوانی بازگشتی (callback) مبتنی بر HTTP است؛ یعنی یک درخواست HTTP POST که هنگام رخ دادن رویدادی ارسال می‌شود. به بیان ساده، وب‌هوک نوعی اعلان رویداد از طریق HTTP POST است. هر برنامهٔ وبی که وب‌هوک را پیاده‌سازی کند، هنگام رخ دادن رویدادهای مشخص، پیامی را با POST به یک URL ارسال می‌کند.


<!-- body -->
اگر حالت `Webhook` مشخص شود، کوبرنتیز برای تعیین سطح دسترسی کاربران از یک سرویس REST خارجی پرس‌وجو می‌کند.

## قالب فایل پیکربندی

حالت `Webhook` به یک فایل پیکربندی HTTP نیاز دارد که با فلگ
`--authorization-webhook-config-file=SOME_FILENAME` مشخص می‌شود.

این فایل پیکربندی از قالب فایل
[kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
استفاده می‌کند. در این فایل، بخش «users» به وب‌هوک API Server و بخش «clusters» به سرویس راه دور اشاره دارد.

نمونه‌ای از پیکربندی که از احراز هویت کلاینت با HTTPS استفاده می‌کند:

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

## محتوای درخواست‌ها

هنگامی که API Server باید دربارهٔ مجوز یک درخواست تصمیم بگیرد، یک آبجکت
`SubjectAccessReview` از نوع `authorization.k8s.io/v1beta1` را که به صورت JSON سریال‌سازی شده و آن کنش را توصیف می‌کند، با POST ارسال می‌کند. این آبجکت فیلدهایی دارد که کاربرِ درخواست‌دهنده را توصیف می‌کنند و همچنین یا جزئیات منبعی را که به آن دسترسی خواسته شده، یا ویژگی‌های درخواست را شامل می‌شود.

توجه کنید که آبجکت‌های API وب‌هوک نیز مانند سایر آبجکت‌های API کوبرنتیز، تابع همان
[قواعد سازگاری نسخه‌ها](/docs/concepts/overview/kubernetes-api/)
هستند. پیاده‌سازان باید بدانند که تضمین‌های سازگاری برای آبجکت‌های بتا سست‌تر است و برای اطمینان از سریال‌زدایی درست، فیلد «apiVersion» درخواست را بررسی کنند. افزون بر این، API Server باید گروه افزونه‌های API با نام `authorization.k8s.io/v1beta1` را فعال کند (`--runtime-config=authorization.k8s.io/v1beta1=true`).

نمونه‌ای از بدنهٔ درخواست:

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

انتظار می‌رود سرویس راه دور فیلد `status` درخواست را پر کند و در پاسخ، دسترسی را مجاز یا غیرمجاز اعلام کند. فیلد `spec` در بدنهٔ پاسخ نادیده گرفته می‌شود و می‌توان آن را حذف کرد. پاسخِ مجازکننده چنین است:

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

روش اول در بیشتر موارد ترجیح داده می‌شود و نشان می‌دهد که وب‌هوک مجوزدهی درخواست را مجاز نمی‌داند یا دربارهٔ آن «نظری ندارد»؛ اما اگر مجوزدهنده‌های دیگری پیکربندی شده باشند، به آن‌ها فرصت داده می‌شود تا درخواست را مجاز کنند. اگر مجوزدهندهٔ دیگری وجود نداشته باشد یا هیچ‌یک از آن‌ها درخواست را مجاز نکنند، درخواست رد می‌شود. در این حالت وب‌هوک چنین پاسخی برمی‌گرداند:

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

روش دوم درخواست را فوراً رد می‌کند و ارزیابی توسط سایر مجوزدهنده‌های پیکربندی‌شده را میان‌بُر می‌زند. این روش را فقط وب‌هوک‌هایی باید به کار ببرند که از کل پیکربندی مجوزدهنده‌های کلاستر آگاهی دقیق دارند. در این حالت وب‌هوک چنین پاسخی برمی‌گرداند:

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

درخواست‌های دسترسی به مسیرهای غیرمنبعی به این شکل ارسال می‌شوند:

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

کوبرنتیز هنگام فراخوانی وب‌هوک مجوزدهی، انتخابگرهای (selector) برچسب و فیلدِ موجود در درخواست را نیز به آن ارسال می‌کند. وب‌هوک مجوزدهی در صورت تمایل می‌تواند تصمیم‌های مجوزدهی خود را بر پایهٔ این انتخابگرهای محدودکنندهٔ فیلد و برچسب بگیرد.

[مستندات API مربوط به SubjectAccessReview](/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/)
رهنمودهایی دربارهٔ نحوهٔ تفسیر و پردازش این فیلدها توسط وب‌هوک‌های مجوزدهی ارائه می‌کند؛ به‌ویژه دربارهٔ استفاده از الزامات تجزیه‌شده به جای رشته‌های خام انتخابگر، و نحوهٔ برخورد ایمن با عملگرهای ناشناخته.

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

مسیرهای غیرمنبعی عبارت‌اند از: `/api`، `/apis`، `/metrics`، `/logs`، `/debug`، `/healthz`، `/livez`، `/openapi/v2`، `/readyz` و `/version.`. کلاینت‌ها برای کشف منابع و نسخه‌های موجود روی سرور، به مسیرهای `/api`، `/api/*`، `/apis`، `/apis/*` و `/version` دسترسی نیاز دارند. می‌توان دسترسی به سایر مسیرهای غیرمنبعی را بدون محدود کردن دسترسی به REST API ممنوع کرد.

برای اطلاعات بیشتر، به
[مستندات API مربوط به SubjectAccessReview](/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/)
و
[پیاده‌سازی webhook.go](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apiserver/plugin/pkg/authorizer/webhook/webhook.go)
مراجعه کنید.
