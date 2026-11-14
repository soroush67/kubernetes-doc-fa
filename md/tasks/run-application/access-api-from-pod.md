---
title: دسترسی به API کوبرنتیز از درون یک Pod
content_type: task
weight: 120
---

<!-- overview -->

این راهنما نشان می‌دهد که چگونه می‌توان از درون یک پاد به API کوبرنتیز دسترسی داشت.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## دسترسی به API از درون یک Pod

هنگام دسترسی به API از درون یک Pod، شیوهٔ یافتن سرور API و احراز هویت در برابر آن
اندکی با حالتی که کلاینت بیرون از کلاستر است تفاوت دارد.

ساده‌ترین راه برای استفاده از API کوبرنتیز در یک Pod، به‌کارگیری یکی از
[کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/) رسمی است. این
کتابخانه‌ها می‌توانند سرور API را به‌طور خودکار پیدا کنند و احراز هویت را انجام دهند.

### استفاده از کتابخانه‌های کلاینت رسمی

روش‌های توصیه‌شده برای اتصال به API کوبرنتیز از درون یک Pod عبارت‌اند از:

- برای کلاینت Go، از
  [کتابخانهٔ کلاینت Go](https://github.com/kubernetes/client-go/) رسمی استفاده کنید.
  تابع `rest.InClusterConfig()` کشف میزبان API و احراز هویت را به‌طور خودکار انجام می‌دهد.
  [نمونه‌ای از آن را اینجا](https://git.k8s.io/client-go/examples/in-cluster-client-configuration/main.go) ببینید.

- برای کلاینت Python، از
  [کتابخانهٔ کلاینت Python](https://github.com/kubernetes-client/python/) رسمی استفاده کنید.
  تابع `config.load_incluster_config()` کشف میزبان API و احراز هویت را به‌طور خودکار انجام می‌دهد.
  [نمونه‌ای از آن را اینجا](https://github.com/kubernetes-client/python/blob/master/examples/in_cluster_config.py) ببینید.

- کتابخانه‌های دیگری نیز در دسترس هستند؛ برای آشنایی با آن‌ها به صفحهٔ
  [کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/) مراجعه کنید.

در همهٔ این موارد، از اعتبارنامه‌های حساب سرویس (service account) مربوط به Pod
برای برقراری ارتباط امن با سرور API استفاده می‌شود.

### دسترسی مستقیم به REST API

کانتینر شما هنگام اجرا در یک Pod می‌تواند با خواندن متغیرهای محیطی
`KUBERNETES_SERVICE_HOST` و `KUBERNETES_SERVICE_PORT_HTTPS` یک نشانی HTTPS برای
سرور API کوبرنتیز بسازد. نشانی درون‌کلاستری سرور API همچنین در Serviceای به نام
`kubernetes` در فضای نام (namespace) `default` منتشر می‌شود تا پادها بتوانند از
`kubernetes.default.svc` به‌عنوان نام DNS سرور API محلی استفاده کنند.

{{< note >}}
کوبرنتیز تضمین نمی‌کند که سرور API برای نام میزبان `kubernetes.default.svc`
گواهی معتبری داشته باشد؛ اما از control plane **انتظار می‌رود** که برای نام میزبان
یا نشانی IPای که `$KUBERNETES_SERVICE_HOST` نشان می‌دهد، گواهی معتبری ارائه کند.
{{< /note >}}

روش توصیه‌شده برای احراز هویت در برابر سرور API، استفاده از اعتبارنامهٔ یک
[حساب سرویس](/docs/tasks/configure-pod-container/configure-service-account/)
است. هر Pod به‌طور پیش‌فرض به یک حساب سرویس وابسته است و یک اعتبارنامه (توکن)
برای آن حساب سرویس در درخت سیستم فایل هر کانتینر آن Pod، در مسیر
`/var/run/secrets/kubernetes.io/serviceaccount/token` قرار داده می‌شود.

در صورت وجود، یک بستهٔ گواهی نیز در درخت سیستم فایل هر کانتینر، در مسیر
`/var/run/secrets/kubernetes.io/serviceaccount/ca.crt` قرار می‌گیرد که باید برای
اعتبارسنجی گواهی ارائه‌شده از سوی سرور API به کار رود.

در پایان، فضای نام پیش‌فرضی که باید برای عملیات API وابسته به فضای نام استفاده شود،
در هر کانتینر در فایلی به مسیر `/var/run/secrets/kubernetes.io/serviceaccount/namespace`
قرار داده می‌شود.

### استفاده از kubectl proxy

اگر می‌خواهید بدون کتابخانهٔ کلاینت رسمی به API پرس‌وجو بفرستید، می‌توانید
`kubectl proxy` را به‌عنوان [فرمان](/docs/tasks/inject-data-application/define-command-argument-container/)
یک کانتینر کناری (sidecar) جدید در Pod اجرا کنید. به این ترتیب، `kubectl proxy`
در برابر API احراز هویت می‌کند و آن را روی رابط `localhost` پاد در دسترس قرار
می‌دهد تا سایر کانتینرهای Pod بتوانند مستقیماً از آن استفاده کنند.

### بدون استفاده از پراکسی

می‌توان با ارسال مستقیم توکن احراز هویت به سرور API، از به‌کارگیری kubectl proxy
پرهیز کرد. در این حالت، گواهی داخلی اتصال را امن می‌کند.

```shell
# Point to the internal API server hostname
APISERVER=https://kubernetes.default.svc

# Path to ServiceAccount token
SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount

# Read this Pod's namespace
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)

# Read the ServiceAccount bearer token
TOKEN=$(cat ${SERVICEACCOUNT}/token)

# Reference the internal certificate authority (CA)
CACERT=${SERVICEACCOUNT}/ca.crt

# Explore the API with TOKEN
curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/api
```

خروجی مشابه زیر خواهد بود:

```json
{
  "kind": "APIVersions",
  "versions": ["v1"],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
```
