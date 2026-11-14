---
reviewers:
- jpeeler
- pmorie
title: پیکربندی یک Pod برای استفاده از حجم projected جهت ذخیره‌سازی
content_type: task
weight: 100
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان با استفاده از یک حجم (volume) از نوع [`projected`](/docs/concepts/storage/volumes/#projected)، چندین منبع حجم موجود را در یک دایرکتوری واحد mount کرد. در حال حاضر، حجم‌های `secret`، `configMap`، `downwardAPI` و `serviceAccountToken` را می‌توان به‌صورت projected درآورد.

{{< note >}}
`serviceAccountToken` یک نوع حجم نیست.
{{< /note >}}


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}


<!-- steps -->
## پیکربندی یک حجم projected برای یک پاد

در این تمرین، از روی فایل‌های محلی، {{< glossary_tooltip text="Secretهایی" term_id="secret" >}} برای نام کاربری و گذرواژه ایجاد می‌کنید. سپس یک Pod می‌سازید که یک کانتینر را اجرا می‌کند و با استفاده از یک حجم [`projected`](/docs/concepts/storage/volumes/#projected)، این Secretها را در یک دایرکتوری مشترک mount می‌کند.

فایل پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/storage/projected.yaml" %}}

1. Secretها را ایجاد کنید:

    ```shell
    # Create files containing the username and password:
    echo -n "admin" > ./username.txt
    echo -n "1f2d1e2e67df" > ./password.txt

    # Package these files into secrets:
    kubectl create secret generic user --from-file=./username.txt
    kubectl create secret generic pass --from-file=./password.txt
    ```
1. Pod را ایجاد کنید:

    ```shell
    kubectl apply -f https://k8s.io/examples/pods/storage/projected.yaml
    ```
1. بررسی کنید که کانتینرِ Pod در حال اجرا باشد و سپس تغییرات Pod را زیر نظر بگیرید:

    ```shell
    kubectl get --watch pod test-projected-volume
    ```
    خروجی به این شکل است:
    ```
    NAME                    READY     STATUS    RESTARTS   AGE
    test-projected-volume   1/1       Running   0          14s
    ```
1. در یک ترمینال دیگر، به یک shell در کانتینرِ در حال اجرا دسترسی پیدا کنید:

    ```shell
    kubectl exec -it test-projected-volume -- /bin/sh
    ```
1. در shell خود، بررسی کنید که دایرکتوری `projected-volume` شامل منابع projected شما باشد:

    ```shell
    ls /projected-volume/
    ```

## پاک‌سازی

Pod و Secretها را حذف کنید:

```shell
kubectl delete pod test-projected-volume
kubectl delete secret user pass
```



## {{% heading "whatsnext" %}}

* درباره‌ی حجم‌های [`projected`](/docs/concepts/storage/volumes/#projected) بیشتر بیاموزید.
* سند طراحی [حجم همه‌کاره (all-in-one volume)](https://git.k8s.io/design-proposals-archive/node/all-in-one-volume.md) را مطالعه کنید.
