---
title: استفاده از پراکسی HTTP برای دسترسی به API کوبرنتیز
content_type: task
weight: 40
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان با استفاده از یک پراکسی HTTP به API کوبرنتیز دسترسی داشت.


## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

اگر هنوز برنامه‌ای در کلاستر خود اجرا نکرده‌اید، با وارد کردن دستور زیر یک برنامه‌ی Hello world را راه‌اندازی کنید:

```shell
kubectl create deployment hello-app --image=gcr.io/google-samples/hello-app:2.0 --port=8080
```

<!-- steps -->

## استفاده از kubectl برای راه‌اندازی سرور پراکسی

دستور زیر یک پراکسی به سرور API کوبرنتیز راه‌اندازی می‌کند:

    kubectl proxy --port=8080

## کاوش در API کوبرنتیز

هنگامی که سرور پراکسی در حال اجراست، می‌توانید با استفاده از `curl`، `wget` یا یک مرورگر، API را کاوش کنید.

نسخه‌های API را دریافت کنید:

    curl http://localhost:8080/api/

خروجی باید مشابه زیر باشد:

    {
      "kind": "APIVersions",
      "versions": [
        "v1"
      ],
      "serverAddressByClientCIDRs": [
        {
          "clientCIDR": "0.0.0.0/0",
          "serverAddress": "10.0.2.15:8443"
        }
      ]
    }

فهرست پادها را دریافت کنید:

    curl http://localhost:8080/api/v1/namespaces/default/pods

خروجی باید مشابه زیر باشد:

    {
      "kind": "PodList",
      "apiVersion": "v1",
      "metadata": {
        "resourceVersion": "33074"
      },
      "items": [
        {
          "metadata": {
            "name": "kubernetes-bootcamp-2321272333-ix8pt",
            "generateName": "kubernetes-bootcamp-2321272333-",
            "namespace": "default",
            "uid": "ba21457c-6b1d-11e6-85f7-1ef9f1dab92b",
            "resourceVersion": "33003",
            "creationTimestamp": "2016-08-25T23:43:30Z",
            "labels": {
              "pod-template-hash": "2321272333",
              "run": "kubernetes-bootcamp"
            },
            ...
    }

## {{% heading "whatsnext" %}}

درباره‌ی [kubectl proxy](/docs/reference/generated/kubectl/kubectl-commands#proxy) بیشتر بیاموزید.
