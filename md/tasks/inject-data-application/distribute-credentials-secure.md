---
title: توزیع امن اعتبارنامه‌ها با استفاده از Secretها
content_type: task
weight: 50
min-kubernetes-server-version: v1.6
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه داده‌های حساس، مانند گذرواژه‌ها و کلیدهای رمزنگاری، را به‌صورت امن به Podها تزریق کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

### تبدیل داده‌های محرمانه به نمایش base-64

فرض کنید می‌خواهید دو داده‌ی محرمانه داشته باشید: نام کاربری `my-app` و گذرواژه‌ی `39528$vdg7Jb`. ابتدا با یک ابزار کدگذاری base64، نام کاربری و گذرواژه‌ی خود را به نمایش base64 تبدیل کنید. در مثال زیر از برنامه‌ی base64 استفاده شده است که معمولاً در دسترس است:

```shell
echo -n 'my-app' | base64
echo -n '39528$vdg7Jb' | base64
```

خروجی نشان می‌دهد که نمایش base-64 نام کاربری شما `bXktYXBw` و نمایش base-64 گذرواژه‌ی شما `Mzk1MjgkdmRnN0pi` است.

{{< caution >}}
برای کاهش خطرات امنیتی ابزارهای خارجی، از یک ابزار محلی استفاده کنید که سیستم‌عامل شما به آن اعتماد دارد.
{{< /caution >}}

<!-- steps -->

## ایجاد یک Secret

در ادامه یک فایل پیکربندی آمده است که می‌توانید با آن یک Secret حاوی نام کاربری و گذرواژه‌ی خود ایجاد کنید:

{{% code_sample file="pods/inject/secret.yaml" %}}

1. Secret را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/secret.yaml
   ```

1. اطلاعات Secret را مشاهده کنید:

   ```shell
   kubectl get secret test-secret
   ```

   خروجی:

   ```
   NAME          TYPE      DATA      AGE
   test-secret   Opaque    2         1m
   ```

1. اطلاعات جزئی‌تر Secret را مشاهده کنید:

   ```shell
   kubectl describe secret test-secret
   ```

   خروجی:

   ```
   Name:       test-secret
   Namespace:  default
   Labels:     <none>
   Annotations:    <none>

   Type:   Opaque

   Data
   ====
   password:   13 bytes
   username:   7 bytes
   ```

### ایجاد مستقیم یک Secret با kubectl

اگر می‌خواهید از مرحله‌ی کدگذاری Base64 صرف‌نظر کنید، می‌توانید همان Secret را با دستور `kubectl create secret` ایجاد کنید. برای مثال:

```shell
kubectl create secret generic test-secret --from-literal='username=my-app' --from-literal='password=39528$vdg7Jb'
```

این روش راحت‌تر است. در روش مفصلی که پیش‌تر نشان داده شد، هر مرحله به‌صراحت انجام شد تا آنچه در پشت صحنه رخ می‌دهد روشن شود.

## ایجاد Podای که از طریق یک حجم (Volume) به داده‌های محرمانه دسترسی دارد

در ادامه یک فایل پیکربندی آمده است که می‌توانید با آن یک Pod ایجاد کنید:

{{% code_sample file="pods/inject/secret-pod.yaml" %}}

1. Pod را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/secret-pod.yaml
   ```

1. بررسی کنید که Pod شما در حال اجرا است:

   ```shell
   kubectl get pod secret-test-pod
   ```

   خروجی:

   ```
   NAME              READY     STATUS    RESTARTS   AGE
   secret-test-pod   1/1       Running   0          42m
   ```

1. یک پوسته (shell) در کانتینری که در Pod شما اجرا می‌شود باز کنید:

   ```shell
   kubectl exec -i -t secret-test-pod -- /bin/bash
   ```

1. داده‌های محرمانه از طریق حجمی که در مسیر `/etc/secret-volume` مانت شده است در اختیار کانتینر قرار می‌گیرند.

   در پوسته‌ی خود، فایل‌های موجود در پوشه‌ی `/etc/secret-volume` را فهرست کنید:

   ```shell
   # Run this in the shell inside the container
   ls /etc/secret-volume
   ```

   خروجی دو فایل را نشان می‌دهد؛ یک فایل برای هر داده‌ی محرمانه:

   ```
   password username
   ```

1. در پوسته‌ی خود، محتوای فایل‌های `username` و `password` را نمایش دهید:

   ```shell
   # Run this in the shell inside the container
   echo "$( cat /etc/secret-volume/username )"
   echo "$( cat /etc/secret-volume/password )"
   ```

   خروجی، نام کاربری و گذرواژه‌ی شما است:

   ```
   my-app
   39528$vdg7Jb
   ```

ایمیج یا خط فرمان خود را طوری تغییر دهید که برنامه فایل‌ها را در پوشه‌ی `mountPath` جست‌وجو کند. هر کلید در نگاشت `data` آبجکت Secret به نام یک فایل در این پوشه تبدیل می‌شود.

### نگاشت کلیدهای Secret به مسیرهای مشخص فایل

همچنین می‌توانید مسیرهایی را درون حجم که کلیدهای Secret در آن‌ها قرار می‌گیرند کنترل کنید. برای تغییر مسیر مقصد هر کلید، از فیلد `.spec.volumes[].secret.items` استفاده کنید:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      items:
      - key: username
        path: my-group/my-username
```

هنگامی که این Pod را مستقر می‌کنید، موارد زیر رخ می‌دهد:

- کلید `username` از `mysecret` به‌جای مسیر `/etc/foo/username` در مسیر `/etc/foo/my-group/my-username` در دسترس کانتینر قرار می‌گیرد.
- کلید `password` از آن آبجکت Secret در حجم قرار داده نمی‌شود.

اگر کلیدها را به‌صراحت با `.spec.volumes[].secret.items` فهرست کنید، به نکات زیر توجه کنید:

- فقط کلیدهایی که در `items` مشخص شده‌اند در حجم قرار می‌گیرند.
- برای استفاده از همه‌ی کلیدهای Secret، باید همه‌ی آن‌ها در فیلد `items` فهرست شوند.
- همه‌ی کلیدهای فهرست‌شده باید در Secret مربوط وجود داشته باشند؛ در غیر این صورت حجم ایجاد نمی‌شود.

### تنظیم مجوزهای POSIX برای کلیدهای Secret

می‌توانید بیت‌های مجوز دسترسی فایل POSIX را برای یک کلید Secret تنظیم کنید. اگر هیچ مجوزی مشخص نکنید، به‌طور پیش‌فرض از `0644` استفاده می‌شود. همچنین می‌توانید یک حالت پیش‌فرض فایل POSIX برای کل حجم Secret تعیین کنید و در صورت نیاز آن را برای هر کلید جداگانه بازنویسی کنید.

برای مثال، می‌توانید حالت پیش‌فرض را به این شکل مشخص کنید:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      defaultMode: 0400
```

این Secret در مسیر `/etc/foo` مانت می‌شود و همه‌ی فایل‌هایی که با مانت حجم Secret ایجاد می‌شوند مجوز `0400` دارند.

{{< note >}}
اگر یک Pod یا الگوی Pod را با JSON تعریف می‌کنید، توجه داشته باشید که مشخصات JSON از لیترال‌های هشت‌هشتی (octal) برای اعداد پشتیبانی نمی‌کند، زیرا JSON مقدار `0400` را مقدار _دهدهی_ `400` در نظر می‌گیرد. بنابراین در JSON برای `defaultMode` از مقادیر دهدهی استفاده کنید. اگر YAML می‌نویسید، می‌توانید `defaultMode` را به‌صورت هشت‌هشتی بنویسید.
{{< /note >}}

## تعریف متغیرهای محیطی کانتینر با استفاده از داده‌های Secret

می‌توانید داده‌های Secretها را به‌صورت متغیرهای محیطی در کانتینرهای خود استفاده کنید.

اگر کانتینری از قبل یک Secret را در قالب متغیر محیطی استفاده کند، تا زمانی که آن کانتینر دوباره راه‌اندازی نشود، به‌روزرسانی Secret را نمی‌بیند. راهکارهای شخص ثالثی وجود دارند که هنگام تغییر Secretها، راه‌اندازی مجدد را آغاز می‌کنند.

### تعریف یک متغیر محیطی کانتینر با داده‌های یک Secret

- یک متغیر محیطی را به‌صورت یک جفت کلید-مقدار در یک Secret تعریف کنید:

  ```shell
  kubectl create secret generic backend-user --from-literal=backend-username='backend-admin'
  ```

- در مشخصات Pod، مقدار `backend-username` تعریف‌شده در Secret را به متغیر محیطی `SECRET_USERNAME` اختصاص دهید.

  {{% code_sample file="pods/inject/pod-single-secret-env-variable.yaml" %}}

- Pod را ایجاد کنید:

  ```shell
  kubectl create -f https://k8s.io/examples/pods/inject/pod-single-secret-env-variable.yaml
  ```

- در پوسته‌ی خود، محتوای متغیر محیطی کانتینر `SECRET_USERNAME` را نمایش دهید.

  ```shell
  kubectl exec -i -t env-single-secret -- /bin/sh -c 'echo $SECRET_USERNAME'
  ```

  خروجی مشابه زیر است:

  ```
  backend-admin
  ```

### تعریف متغیرهای محیطی کانتینر با داده‌های چند Secret

- مانند مثال قبل، ابتدا Secretها را ایجاد کنید.

  ```shell
  kubectl create secret generic backend-user --from-literal=backend-username='backend-admin'
  kubectl create secret generic db-user --from-literal=db-username='db-admin'
  ```

- متغیرهای محیطی را در مشخصات Pod تعریف کنید.

  {{% code_sample file="pods/inject/pod-multiple-secret-env-variable.yaml" %}}

- Pod را ایجاد کنید:

  ```shell
  kubectl create -f https://k8s.io/examples/pods/inject/pod-multiple-secret-env-variable.yaml
  ```

- در پوسته‌ی خود، متغیرهای محیطی کانتینر را نمایش دهید.

  ```shell
  kubectl exec -i -t envvars-multiple-secrets -- /bin/sh -c 'env | grep _USERNAME'
  ```

  خروجی مشابه زیر است:

  ```
  DB_USERNAME=db-admin
  BACKEND_USERNAME=backend-admin
  ```

## پیکربندی همه‌ی جفت‌های کلید-مقدار یک Secret به‌عنوان متغیرهای محیطی کانتینر

{{< note >}}
این قابلیت در کوبرنتیز نسخه‌ی v1.6 و بالاتر در دسترس است.
{{< /note >}}

- یک Secret حاوی چند جفت کلید-مقدار ایجاد کنید:

  ```shell
  kubectl create secret generic test-secret --from-literal=username='my-app' --from-literal=password='39528$vdg7Jb'
  ```

- با استفاده از envFrom، همه‌ی داده‌های Secret را به‌عنوان متغیرهای محیطی کانتینر تعریف کنید.
  هر کلید Secret به نام یک متغیر محیطی در Pod تبدیل می‌شود.

  {{% code_sample file="pods/inject/pod-secret-envFrom.yaml" %}}

- Pod را ایجاد کنید:

  ```shell
  kubectl create -f https://k8s.io/examples/pods/inject/pod-secret-envFrom.yaml
  ```

- در پوسته‌ی خود، متغیرهای محیطی کانتینر `username` و `password` را نمایش دهید.

  ```shell
  kubectl exec -i -t envfrom-secret -- /bin/sh -c 'echo "username: $username\npassword: $password\n"'
  ```

  خروجی مشابه زیر است:

  ```
  username: my-app
  password: 39528$vdg7Jb
  ```

## مثال: ارائه‌ی اعتبارنامه‌های محیط تولید و آزمایش به Podها با استفاده از Secretها {#provide-prod-test-creds}

این مثال یک Pod را نشان می‌دهد که از Secretی حاوی اعتبارنامه‌های محیط تولید (production) استفاده می‌کند و Pod دیگری که از Secretی با اعتبارنامه‌های محیط آزمایش استفاده می‌کند.

1. یک Secret برای اعتبارنامه‌های محیط تولید ایجاد کنید:

   ```shell
   kubectl create secret generic prod-db-secret --from-literal=username=produser --from-literal=password=Y4nys7f11
   ```

   خروجی مشابه زیر است:

   ```
   secret "prod-db-secret" created
   ```

1. یک Secret برای اعتبارنامه‌های محیط آزمایش ایجاد کنید.

   ```shell
   kubectl create secret generic test-db-secret --from-literal=username=testuser --from-literal=password=iluvtests
   ```

   خروجی مشابه زیر است:

   ```
   secret "test-db-secret" created
   ```

   {{< note >}}
   نویسه‌های خاصی مانند `$`، `\`، `*`، `=` و `!` توسط [پوسته](https://en.wikipedia.org/wiki/Shell_(computing))ی شما تفسیر می‌شوند و باید گریز (escape) داده شوند.

   در بیشتر پوسته‌ها، ساده‌ترین راه برای گریز دادن گذرواژه این است که آن را درون علامت نقل‌قول تکی (`'`) قرار دهید.
   برای مثال، اگر گذرواژه‌ی واقعی شما `S!B\*d$zDsb=` است، باید دستور را به این شکل اجرا کنید:

   ```shell
   kubectl create secret generic dev-db-secret --from-literal=username=devuser --from-literal=password='S!B\*d$zDsb='
   ```

   برای گذرواژه‌هایی که از فایل خوانده می‌شوند (`--from-file`)، نیازی به گریز دادن نویسه‌های خاص نیست.
   {{< /note >}}

1. مانیفست‌های Pod را ایجاد کنید:

   ```shell
   cat <<EOF > pod.yaml
   apiVersion: v1
   kind: List
   items:
   - kind: Pod
     apiVersion: v1
     metadata:
       name: prod-db-client-pod
       labels:
         name: prod-db-client
     spec:
       volumes:
       - name: secret-volume
         secret:
           secretName: prod-db-secret
       containers:
       - name: db-client-container
         image: myClientImage
         volumeMounts:
         - name: secret-volume
           readOnly: true
           mountPath: "/etc/secret-volume"
   - kind: Pod
     apiVersion: v1
     metadata:
       name: test-db-client-pod
       labels:
         name: test-db-client
     spec:
       volumes:
       - name: secret-volume
         secret:
           secretName: test-db-secret
       containers:
       - name: db-client-container
         image: myClientImage
         volumeMounts:
         - name: secret-volume
           readOnly: true
           mountPath: "/etc/secret-volume"
   EOF
   ```

   {{< note >}}
   مشخصات این دو Pod فقط در یک فیلد با هم تفاوت دارند؛ این ویژگی ایجاد Podهایی با قابلیت‌های متفاوت از یک الگوی مشترک Pod را آسان می‌کند.
   {{< /note >}}

1. با اجرای دستور زیر، همه‌ی این آبجکت‌ها را روی سرور API اعمال کنید:

   ```shell
   kubectl create -f pod.yaml
   ```

هر دو کانتینر فایل‌های زیر را در سیستم فایل خود خواهند داشت و مقدار این فایل‌ها با محیط هر کانتینر متناسب است:

```
/etc/secret-volume/username
/etc/secret-volume/password
```

می‌توانید با استفاده از دو حساب سرویس (service account)، مشخصات پایه‌ی Pod را باز هم ساده‌تر کنید:

1. حساب سرویس `prod-user` همراه با `prod-db-secret`
1. حساب سرویس `test-user` همراه با `test-db-secret`

در این صورت، مشخصات Pod به این شکل کوتاه می‌شود:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: prod-db-client-pod
  labels:
    name: prod-db-client
spec:
  serviceAccount: prod-db-client
  containers:
  - name: db-client-container
    image: myClientImage
```

### منابع

- [Secret](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#secret-v1-core)
- [Volume](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#volume-v1-core)
- [Pod](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#pod-v1-core)

## {{% heading "whatsnext" %}}

- درباره‌ی [Secretها](/docs/concepts/configuration/secret/) بیشتر بیاموزید.
- درباره‌ی [حجم‌ها](/docs/concepts/storage/volumes/) بیاموزید.
