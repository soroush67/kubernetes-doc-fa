---
title: مدیریت Secretها با استفاده از فایل پیکربندی
content_type: task
weight: 20
description: ایجاد آبجکت‌های Secret با استفاده از فایل پیکربندی منبع.
---

<!-- overview -->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## ایجاد Secret {#create-the-config-file}

می‌توانید ابتدا آبجکت `Secret` را در یک مانیفست با قالب JSON یا YAML تعریف کنید و سپس آن آبجکت را ایجاد کنید. منبع
[Secret](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#secret-v1-core)
دو نگاشت (map) دارد: `data` و `stringData`. فیلد `data` برای ذخیرهٔ داده‌های دلخواه به‌کار می‌رود که با base64 کدگذاری شده‌اند. فیلد `stringData` برای سهولت کار فراهم شده است و با آن می‌توانید همان داده‌ها را به‌صورت رشته‌های کدگذاری‌نشده وارد کنید. کلیدهای `data` و `stringData` باید فقط از نویسه‌های الفبایی‌عددی، `-`، `_` یا `.` تشکیل شده باشند.

در مثال زیر، دو رشته با استفاده از فیلد `data` در یک Secret ذخیره می‌شوند.

1. رشته‌ها را به base64 تبدیل کنید:

   ```shell
   echo -n 'admin' | base64
   echo -n '1f2d1e2e67df' | base64
   ```

   {{< note >}}
   مقادیر سریال‌شدهٔ JSON و YAML داده‌های Secret به‌صورت رشته‌های base64 کدگذاری می‌شوند. نویسهٔ خط جدید درون این رشته‌ها معتبر نیست و باید حذف شود. کاربران Darwin/macOS هنگام استفاده از ابزار `base64` نباید از گزینهٔ `-b` برای شکستن خطوط طولانی استفاده کنند. در مقابل، کاربران لینوکس *باید* گزینهٔ `-w 0` را به فرمان‌های `base64` اضافه کنند، یا اگر گزینهٔ `-w` در دسترس نیست، از خط لولهٔ `base64 | tr -d '\n'` استفاده کنند.
   {{< /note >}}

   خروجی مشابه زیر است:

   ```
   YWRtaW4=
   MWYyZDFlMmU2N2Rm
   ```

1. مانیفست را ایجاد کنید:

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: mysecret
   type: Opaque
   data:
     username: YWRtaW4=
     password: MWYyZDFlMmU2N2Rm
   ```

   توجه کنید که نام هر آبجکت Secret باید یک
   [نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

1. با استفاده از [`kubectl apply`](/docs/reference/generated/kubectl/kubectl-commands#apply)، Secret را ایجاد کنید:

   ```shell
   kubectl apply -f ./secret.yaml
   ```

   خروجی مشابه زیر است:

   ```
   secret/mysecret created
   ```

برای اطمینان از ایجاد Secret و رمزگشایی داده‌های آن، به
[مدیریت Secretها با استفاده از kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/#verify-the-secret) مراجعه کنید.

### تعیین داده‌های کدگذاری‌نشده هنگام ایجاد Secret

در برخی سناریوها ممکن است بخواهید به‌جای آن از فیلد `stringData` استفاده کنید. با این فیلد می‌توانید رشته‌ای را که با base64 کدگذاری نشده است مستقیماً در Secret قرار دهید و این رشته هنگام ایجاد یا به‌روزرسانی Secret به‌طور خودکار کدگذاری می‌شود.

یک نمونهٔ کاربردی این حالت زمانی است که برنامه‌ای را مستقر می‌کنید که برای ذخیرهٔ یک فایل پیکربندی از Secret استفاده می‌کند و می‌خواهید بخش‌هایی از آن فایل پیکربندی را در طول فرایند استقرار مقداردهی کنید.

برای مثال، اگر برنامهٔ شما از فایل پیکربندی زیر استفاده کند:

```yaml
apiUrl: "https://my.api.com/api/v1"
username: "<user>"
password: "<password>"
```

می‌توانید آن را با تعریف زیر در یک Secret ذخیره کنید:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
stringData:
  config.yaml: |
    apiUrl: "https://my.api.com/api/v1"
    username: <user>
    password: <password>
```

{{< note >}}
فیلد `stringData` در Secret با اعمال سمت سرور (server-side apply) به‌خوبی کار نمی‌کند.
{{< /note >}}

هنگام بازیابی داده‌های Secret، فرمان مقادیر کدگذاری‌شده را برمی‌گرداند، نه مقادیر متن ساده‌ای را که در `stringData` وارد کرده بودید.

برای مثال، اگر فرمان زیر را اجرا کنید:

```shell
kubectl get secret mysecret -o yaml
```

خروجی مشابه زیر است:

```yaml
apiVersion: v1
data:
  config.yaml: YXBpVXJsOiAiaHR0cHM6Ly9teS5hcGkuY29tL2FwaS92MSIKdXNlcm5hbWU6IHt7dXNlcm5hbWV9fQpwYXNzd29yZDoge3twYXNzd29yZH19
kind: Secret
metadata:
  creationTimestamp: 2018-11-15T20:40:59Z
  name: mysecret
  namespace: default
  resourceVersion: "7225"
  uid: c280ad2e-e916-11e8-98f2-025000000001
type: Opaque
```

### تعیین هم‌زمان `data` و `stringData`

اگر یک فیلد را هم در `data` و هم در `stringData` تعیین کنید، مقدار موجود در `stringData` به‌کار می‌رود.

برای مثال، اگر Secret زیر را تعریف کنید:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
stringData:
  username: administrator
```

{{< note >}}
فیلد `stringData` در Secret با اعمال سمت سرور به‌خوبی کار نمی‌کند.
{{< /note >}}

آبجکت `Secret` به این صورت ایجاد می‌شود:

```yaml
apiVersion: v1
data:
  username: YWRtaW5pc3RyYXRvcg==
kind: Secret
metadata:
  creationTimestamp: 2018-11-15T20:46:46Z
  name: mysecret
  namespace: default
  resourceVersion: "7579"
  uid: 91460ecb-e917-11e8-98f2-025000000001
type: Opaque
```

رشتهٔ `YWRtaW5pc3RyYXRvcg==` پس از رمزگشایی به `administrator` تبدیل می‌شود.

## ویرایش Secret {#edit-secret}

برای ویرایش داده‌های Secretی که با استفاده از مانیفست ایجاد کرده‌اید، فیلد `data` یا `stringData` را در مانیفست خود تغییر دهید و فایل را روی کلاستر اعمال کنید. هر آبجکت `Secret` موجود را می‌توانید ویرایش کنید، مگر اینکه
[تغییرناپذیر](/docs/concepts/configuration/secret/#secret-immutable) باشد.

برای مثال، اگر می‌خواهید گذرواژهٔ مثال قبلی را به `birdsarentreal` تغییر دهید، مراحل زیر را انجام دهید:

1. رشتهٔ گذرواژهٔ جدید را کدگذاری کنید:

   ```shell
   echo -n 'birdsarentreal' | base64
   ```

   خروجی مشابه زیر است:

   ```
   YmlyZHNhcmVudHJlYWw=
   ```

1. فیلد `data` را با رشتهٔ گذرواژهٔ جدید به‌روزرسانی کنید:

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: mysecret
   type: Opaque
   data:
     username: YWRtaW4=
     password: YmlyZHNhcmVudHJlYWw=
   ```

1. مانیفست را روی کلاستر اعمال کنید:

   ```shell
   kubectl apply -f ./secret.yaml
   ```

   خروجی مشابه زیر است:

   ```
   secret/mysecret configured
   ```

کوبرنتیز آبجکت `Secret` موجود را به‌روزرسانی می‌کند. به‌طور دقیق‌تر، ابزار `kubectl` متوجه می‌شود که یک آبجکت `Secret` با همین نام از قبل وجود دارد. سپس `kubectl` آبجکت موجود را دریافت می‌کند، تغییرات لازم را برای آن برنامه‌ریزی می‌کند و آبجکت `Secret` تغییریافته را به control plane کلاستر شما ارسال می‌کند.

اگر به‌جای آن از `kubectl apply --server-side` استفاده کرده باشید، `kubectl` از
[اعمال سمت سرور (Server Side Apply)](/docs/reference/using-api/server-side-apply/) استفاده می‌کند.

## پاک‌سازی

برای حذف Secretی که ایجاد کرده‌اید:

```shell
kubectl delete secret mysecret
```

## {{% heading "whatsnext" %}}

- دربارهٔ [مفهوم Secret](/docs/concepts/configuration/secret/) بیشتر بخوانید
- با نحوهٔ [مدیریت Secretها با استفاده از kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/) آشنا شوید
- با نحوهٔ [مدیریت Secretها با استفاده از kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/) آشنا شوید
