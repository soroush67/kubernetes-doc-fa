---
title: مدیریت Secretها با استفاده از Kustomize
content_type: task
weight: 30
description: ایجاد آبجکت‌های Secret با استفاده از فایل kustomization.yaml.
---

<!-- overview -->

ابزار `kubectl` از [ابزار مدیریت آبجکت Kustomize](/docs/tasks/manage-kubernetes-objects/kustomization/) برای مدیریت Secretها و ConfigMapها پشتیبانی می‌کند. شما با Kustomize یک *مولد منبع* (resource generator) ایجاد می‌کنید که یک Secret تولید می‌کند و می‌توانید آن را با `kubectl` روی سرور API اعمال کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## ایجاد یک Secret

برای تولید یک Secret می‌توانید یک `secretGenerator` را در فایل `kustomization.yaml` تعریف کنید که به فایل‌های موجود دیگر، فایل‌های `.env` یا مقادیر لفظی (literal) ارجاع می‌دهد. برای مثال، دستورالعمل‌های زیر یک فایل kustomization برای نام کاربری `admin` و گذرواژه `1f2d1e2e67df` ایجاد می‌کنند.

{{< note >}}
فیلد `stringData` در Secret با اعمال سمت سرور (server-side apply) به‌خوبی کار نمی‌کند.
{{< /note >}}

### ایجاد فایل kustomization

{{< tabs name="داده‌های Secret" >}}
{{< tab name="مقادیر لفظی" codelang="yaml" >}}
secretGenerator:
- name: database-creds
  literals:
  - username=admin
  - password=1f2d1e2e67df
{{< /tab >}}
{{% tab name="فایل‌ها" %}}
1.  اطلاعات احراز هویت را در فایل‌ها ذخیره کنید. نام فایل‌ها کلیدهای Secret خواهند بود:

    ```shell
    echo -n 'admin' > ./username.txt
    echo -n '1f2d1e2e67df' > ./password.txt
    ```
    پرچم `-n` تضمین می‌کند که در انتهای فایل‌های شما نویسه خط جدید وجود نداشته باشد.

1.  فایل `kustomization.yaml` را ایجاد کنید:

    ```yaml
    secretGenerator:
    - name: database-creds
      files:
      - username.txt
      - password.txt
    ```
{{% /tab %}}
{{% tab name="فایل‌های .env" %}}
همچنین می‌توانید با ارائه فایل‌های `.env`، مولد secretGenerator را در فایل `kustomization.yaml` تعریف کنید. برای مثال، فایل `kustomization.yaml` زیر داده‌ها را از فایل `.env.secret` دریافت می‌کند:

```yaml
secretGenerator:
- name: db-user-pass
  envs:
  - .env.secret
```
{{% /tab %}}
{{< /tabs >}}

در همه این حالت‌ها، نیازی به کدگذاری مقادیر با base64 نیست. نام فایل YAML **باید** `kustomization.yaml` یا `kustomization.yml` باشد.

### اعمال فایل kustomization

برای ایجاد Secret، دایرکتوری حاوی فایل kustomization را اعمال کنید:

```shell
kubectl apply -k <directory-path>
```

خروجی مشابه زیر است:

```
secret/database-creds-5hdh7hhgfk created
```

هنگام تولید یک Secret، نام آن از هش‌کردن داده‌های Secret و افزودن مقدار هش به انتهای نام ساخته می‌شود. به این ترتیب، هر بار که داده‌ها تغییر کنند، یک Secret جدید تولید می‌شود.

برای اطمینان از ایجاد Secret و رمزگشایی داده‌های آن، دستور زیر را اجرا کنید:

```shell
kubectl get -k <directory-path> -o jsonpath='{.data}' 
```

خروجی مشابه زیر است:

```
{ "password": "MWYyZDFlMmU2N2Rm", "username": "YWRtaW4=" }
```

```
echo 'MWYyZDFlMmU2N2Rm' | base64 --decode
```

خروجی مشابه زیر است:

```
1f2d1e2e67df
```

برای اطلاعات بیشتر، به
[مدیریت Secretها با استفاده از kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/#verify-the-secret) و
[مدیریت اعلانی آبجکت‌های کوبرنتیز با استفاده از Kustomize](/docs/tasks/manage-kubernetes-objects/kustomization/) مراجعه کنید.

## ویرایش یک Secret {#edit-secret}

1.  در فایل `kustomization.yaml`، داده‌ها را تغییر دهید؛ برای مثال مقدار `password` را.
1.  دایرکتوری حاوی فایل kustomization را اعمال کنید:

    ```shell
    kubectl apply -k <directory-path>
    ```

    خروجی مشابه زیر است:

    ```
    secret/db-user-pass-6f24b56cc8 created
    ```

به‌جای به‌روزرسانی آبجکت `Secret` موجود، Secret ویرایش‌شده به‌صورت یک آبجکت `Secret` جدید ایجاد می‌شود. ممکن است لازم باشد ارجاع‌های Podهای خود به این Secret را به‌روزرسانی کنید.

## پاک‌سازی

برای حذف یک Secret، از `kubectl` استفاده کنید:

```shell
kubectl delete secret db-user-pass
```

## {{% heading "whatsnext" %}}

- درباره [مفهوم Secret](/docs/concepts/configuration/secret/) بیشتر بخوانید
- یاد بگیرید چگونه [Secretها را با استفاده از kubectl مدیریت کنید](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
- یاد بگیرید چگونه [Secretها را با استفاده از فایل پیکربندی مدیریت کنید](/docs/tasks/configmap-secret/managing-secret-using-config-file/)
