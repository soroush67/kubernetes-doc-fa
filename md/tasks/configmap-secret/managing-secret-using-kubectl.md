---
title: مدیریت Secretها با استفاده از kubectl
content_type: task
weight: 10
description: ایجاد آبجکت‌های Secret با استفاده از خط فرمان kubectl.
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه با ابزار خط فرمان `kubectl`
{{<glossary_tooltip text="Secretهای" term_id="secret">}} کوبرنتیز را ایجاد، ویرایش، مدیریت و حذف کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## ایجاد یک Secret

هر آبجکت `Secret` داده‌های حساسی مانند اطلاعات احراز هویت (credentials) را ذخیره می‌کند که Podها برای دسترسی به سرویس‌ها از آن‌ها استفاده می‌کنند. برای مثال، ممکن است برای ذخیرهٔ نام کاربری و گذرواژهٔ لازم برای دسترسی به یک پایگاه داده به یک Secret نیاز داشته باشید.

می‌توانید Secret را با ارسال داده‌های خام در خود فرمان ایجاد کنید، یا اطلاعات احراز هویت را در فایل‌هایی ذخیره کنید و آن فایل‌ها را به فرمان بدهید. فرمان‌های زیر یک Secret ایجاد می‌کنند که نام کاربری `admin` و گذرواژهٔ `S!B\*d$zDsb=` را ذخیره می‌کند.

### استفاده از داده‌های خام

فرمان زیر را اجرا کنید:

```shell
kubectl create secret generic db-user-pass \
    --from-literal=username=admin \
    --from-literal=password='S!B\*d$zDsb='
```
برای گریز (escape) نویسه‌های خاصی مانند `$`، `\`، `*`، `=` و `!` در رشته‌ها باید از نقل‌قول تکی `''` استفاده کنید. در غیر این صورت، پوستهٔ شما این نویسه‌ها را تفسیر می‌کند.

{{< note >}}
فیلد `stringData` در Secret با اعمال سمت سرور (server-side apply) به‌خوبی کار نمی‌کند.
{{< /note >}}

### استفاده از فایل‌های منبع

1. اطلاعات احراز هویت را در فایل‌ها ذخیره کنید:

   ```shell
   echo -n 'admin' > ./username.txt
   echo -n 'S!B\*d$zDsb=' > ./password.txt
   ```

   پرچم `-n` تضمین می‌کند که فایل‌های تولیدشده در انتهای متن نویسهٔ خط جدید اضافی نداشته باشند. این نکته اهمیت دارد، زیرا وقتی `kubectl` فایلی را می‌خواند و محتوای آن را به رشته‌ای با کدگذاری base64 تبدیل می‌کند، نویسهٔ خط جدید اضافی نیز کدگذاری می‌شود. لازم نیست نویسه‌های خاص را در رشته‌هایی که در فایل قرار می‌دهید گریز دهید.

1. مسیر فایل‌ها را به فرمان `kubectl` بدهید:

   ```shell
   kubectl create secret generic db-user-pass \
       --from-file=./username.txt \
       --from-file=./password.txt
   ```

   نام پیش‌فرض کلید، همان نام فایل است. در صورت تمایل می‌توانید نام کلید را با `--from-file=[key=]source` تعیین کنید. برای مثال:

   ```shell
   kubectl create secret generic db-user-pass \
       --from-file=username=./username.txt \
       --from-file=password=./password.txt
   ```

با هر دو روش، خروجی مشابه زیر است:

```
secret/db-user-pass created
```

### بررسی Secret {#verify-the-secret}

بررسی کنید که Secret ایجاد شده باشد:

```shell
kubectl get secrets
```

خروجی مشابه زیر است:

```
NAME              TYPE       DATA      AGE
db-user-pass      Opaque     2         51s
```

جزئیات Secret را مشاهده کنید:

```shell
kubectl describe secret db-user-pass
```

خروجی مشابه زیر است:

```
Name:            db-user-pass
Namespace:       default
Labels:          <none>
Annotations:     <none>

Type:            Opaque

Data
====
password:    12 bytes
username:    5 bytes
```

فرمان‌های `kubectl get` و `kubectl describe` به‌طور پیش‌فرض محتوای `Secret` را نمایش نمی‌دهند. هدف از این کار، محافظت از `Secret` در برابر افشای تصادفی یا ذخیره شدن در گزارش ترمینال است.

### رمزگشایی Secret  {#decoding-secret}

1. محتوای Secretی را که ایجاد کرده‌اید مشاهده کنید:

   ```shell
   kubectl get secret db-user-pass -o jsonpath='{.data}'
   ```

   خروجی مشابه زیر است:

   ```json
   { "password": "UyFCXCpkJHpEc2I9", "username": "YWRtaW4=" }
   ```

1. دادهٔ `password` را رمزگشایی کنید:

   ```shell
   echo 'UyFCXCpkJHpEc2I9' | base64 --decode
   ```

   خروجی مشابه زیر است:

   ```
   S!B\*d$zDsb=
   ```

   {{< caution >}}
   این مثال فقط برای اهداف مستندسازی است. در عمل، این روش ممکن است باعث شود فرمانِ حاوی داده‌های کدگذاری‌شده در تاریخچهٔ پوستهٔ شما ذخیره شود. هر کسی که به رایانهٔ شما دسترسی داشته باشد می‌تواند این فرمان را پیدا کند و Secret را رمزگشایی کند. رویکرد بهتر، ترکیب فرمان‌های مشاهده و رمزگشایی است.
   {{< /caution >}}

   ```shell
   kubectl get secret db-user-pass -o jsonpath='{.data.password}' | base64 --decode
   ```

## ویرایش یک Secret {#edit-secret}

می‌توانید یک آبجکت `Secret` موجود را ویرایش کنید، مگر اینکه
[تغییرناپذیر](/docs/concepts/configuration/secret/#secret-immutable) باشد. برای ویرایش یک Secret، فرمان زیر را اجرا کنید:

```shell
kubectl edit secrets <secret-name>
```

این فرمان ویرایشگر پیش‌فرض شما را باز می‌کند و می‌توانید مقادیر Secret را که با base64 کدگذاری شده‌اند در فیلد `data` به‌روزرسانی کنید؛ مانند مثال زیر:

```yaml
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file, it will be
# reopened with the relevant failures.
#
apiVersion: v1
data:
  password: UyFCXCpkJHpEc2I9
  username: YWRtaW4=
kind: Secret
metadata:
  creationTimestamp: "2022-06-28T17:44:13Z"
  name: db-user-pass
  namespace: default
  resourceVersion: "12708504"
  uid: 91becd59-78fa-4c85-823f-6d44436242ac
type: Opaque
```

## پاک‌سازی

برای حذف یک Secret، فرمان زیر را اجرا کنید:

```shell
kubectl delete secret db-user-pass
```

## {{% heading "whatsnext" %}}

- دربارهٔ [مفهوم Secret](/docs/concepts/configuration/secret/) بیشتر بخوانید
- با نحوهٔ [مدیریت Secretها با استفاده از فایل پیکربندی](/docs/tasks/configmap-secret/managing-secret-using-config-file/) آشنا شوید
- با نحوهٔ [مدیریت Secretها با استفاده از kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/) آشنا شوید
