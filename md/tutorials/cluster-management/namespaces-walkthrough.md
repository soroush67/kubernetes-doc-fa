---
reviewers:
- derekwaynecarr
- janetkuo
title: آشنایی گام‌به‌گام با فضاهای نام
content_type: task
weight: 260
---

<!-- overview -->
{{< glossary_tooltip text="فضاهای نام" term_id="namespace" >}} (namespaces) در کوبرنتیز
به پروژه‌ها، تیم‌ها یا مشتریان مختلف کمک می‌کنند تا از یک کلاستر کوبرنتیز به‌صورت مشترک استفاده کنند.

فضاهای نام این کار را با فراهم کردن موارد زیر انجام می‌دهند:

1. یک دامنه (scope) برای [نام‌ها](/docs/concepts/overview/working-with-objects/names/).
2. سازوکاری برای اعمال مجوزدهی و سیاست‌ها بر بخشی از کلاستر.

استفاده از چند فضای نام اختیاری است.

این مثال نشان می‌دهد که چگونه می‌توان با استفاده از فضاهای نام کوبرنتیز، کلاستر را به بخش‌های کوچک‌تر تقسیم کرد.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}



<!-- steps -->

## پیش‌نیازها

در این مثال فرض بر این است که:

1. یک [کلاستر کوبرنتیز موجود](/docs/setup/) در اختیار دارید.
2. با مفاهیم پایه‌ای {{< glossary_tooltip text="Podها" term_id="pod" >}}، {{< glossary_tooltip term_id="service" text="Serviceها" >}} و {{< glossary_tooltip text="Deploymentها" term_id="deployment" >}} در کوبرنتیز آشنا هستید.

## آشنایی با فضای نام پیش‌فرض

هر کلاستر کوبرنتیز به‌طور پیش‌فرض هنگام راه‌اندازی، یک فضای نام پیش‌فرض ایجاد می‌کند تا مجموعهٔ پیش‌فرض Podها،
Serviceها و Deploymentهایی را که کلاستر از آن‌ها استفاده می‌کند در خود نگه دارد.

اگر کلاستر شما تازه راه‌اندازی شده باشد، می‌توانید فضاهای نام موجود را به این صورت بررسی کنید:

```shell
kubectl get namespaces
```
```
NAME      STATUS    AGE
default   Active    13m
```

## ایجاد فضاهای نام جدید

در این تمرین، دو فضای نام دیگر در کوبرنتیز ایجاد می‌کنیم تا محتوای خود را در آن‌ها نگه داریم.

سناریویی را در نظر بگیرید که در آن یک سازمان از یک کلاستر کوبرنتیز مشترک برای کاربردهای توسعه و تولید (production) استفاده می‌کند.

تیم توسعه می‌خواهد فضایی در کلاستر داشته باشد که در آن بتواند فهرست Podها، Serviceها و Deploymentهایی را
که برای ساخت و اجرای برنامهٔ خود به کار می‌برد مشاهده کند. در این فضا، منابع کوبرنتیز مدام ایجاد و حذف می‌شوند و محدودیت‌های مربوط به اینکه چه کسی
می‌تواند منابع را تغییر دهد یا نمی‌تواند، برای امکان توسعهٔ چابک سهل‌گیرانه‌تر است.

تیم عملیات می‌خواهد فضایی در کلاستر داشته باشد که در آن بتواند رویه‌های سخت‌گیرانه‌ای را دربارهٔ اینکه چه کسی می‌تواند
Podها، Serviceها و Deploymentهای اجراکنندهٔ سایت عملیاتی را دست‌کاری کند یا نمی‌تواند، اعمال کند.

یکی از الگوهایی که این سازمان می‌تواند دنبال کند، تقسیم کلاستر کوبرنتیز به دو فضای نام `development` و `production` است.

بیایید دو فضای نام جدید برای نگهداری کارهای خود ایجاد کنیم.

از فایل [`namespace-dev.yaml`](/examples/admin/namespace-dev.yaml) استفاده کنید که فضای نام `development` را توصیف می‌کند:

{{% code_sample language="yaml" file="admin/namespace-dev.yaml" %}}

فضای نام `development` را با استفاده از kubectl ایجاد کنید.

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-dev.yaml
```

محتوای زیر را در فایل [`namespace-prod.yaml`](/examples/admin/namespace-prod.yaml) ذخیره کنید که فضای نام `production` را توصیف می‌کند:

{{% code_sample language="yaml" file="admin/namespace-prod.yaml" %}}

سپس فضای نام `production` را با استفاده از kubectl ایجاد می‌کنیم.

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-prod.yaml
```

برای اطمینان از درستی کار، همهٔ فضاهای نام موجود در کلاستر را فهرست می‌کنیم.

```shell
kubectl get namespaces --show-labels
```
```
NAME          STATUS    AGE       LABELS
default       Active    32m       <none>
development   Active    29s       name=development
production    Active    23s       name=production
```

## ایجاد Podها در هر فضای نام

هر فضای نام کوبرنتیز دامنه‌ای برای Podها، Serviceها و Deploymentهای موجود در کلاستر فراهم می‌کند.

کاربرانی که با یک فضای نام کار می‌کنند، محتوای فضای نام دیگر را نمی‌بینند.

برای نشان دادن این موضوع، یک Deployment ساده و چند Pod در فضای نام `development` راه‌اندازی می‌کنیم.

ابتدا بررسی می‌کنیم که context فعلی چیست:

```shell
kubectl config view
```
```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: REDACTED
    server: https://130.211.122.180
  name: lithe-cocoa-92103_kubernetes
contexts:
- context:
    cluster: lithe-cocoa-92103_kubernetes
    user: lithe-cocoa-92103_kubernetes
  name: lithe-cocoa-92103_kubernetes
current-context: lithe-cocoa-92103_kubernetes
kind: Config
preferences: {}
users:
- name: lithe-cocoa-92103_kubernetes
  user:
    client-certificate-data: REDACTED
    client-key-data: REDACTED
    token: 65rZW78y8HbwXXtSXuUw9DbP4FLjHi4b
- name: lithe-cocoa-92103_kubernetes-basic-auth
  user:
    password: h5M0FtUUIflBSdI7
    username: admin
```
```shell
kubectl config current-context
```
```
lithe-cocoa-92103_kubernetes
```

گام بعدی، تعریف یک context برای کلاینت kubectl است تا در هر فضای نام کار کند. مقدار فیلدهای «cluster» و «user» از context فعلی کپی می‌شود.

```shell
kubectl config set-context dev --namespace=development \
  --cluster=lithe-cocoa-92103_kubernetes \
  --user=lithe-cocoa-92103_kubernetes

kubectl config set-context prod --namespace=production \
  --cluster=lithe-cocoa-92103_kubernetes \
  --user=lithe-cocoa-92103_kubernetes
```

دستورهای بالا به‌طور پیش‌فرض دو context اضافه می‌کنند که در فایل
`.kube/config` ذخیره می‌شوند. اکنون می‌توانید این contextها را مشاهده کنید و بسته به اینکه
می‌خواهید با کدام فضای نام کار کنید، میان این دو context درخواست جدید جابه‌جا شوید.

برای مشاهدهٔ contextهای جدید:

```shell
kubectl config view
```
```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: REDACTED
    server: https://130.211.122.180
  name: lithe-cocoa-92103_kubernetes
contexts:
- context:
    cluster: lithe-cocoa-92103_kubernetes
    user: lithe-cocoa-92103_kubernetes
  name: lithe-cocoa-92103_kubernetes
- context:
    cluster: lithe-cocoa-92103_kubernetes
    namespace: development
    user: lithe-cocoa-92103_kubernetes
  name: dev
- context:
    cluster: lithe-cocoa-92103_kubernetes
    namespace: production
    user: lithe-cocoa-92103_kubernetes
  name: prod
current-context: lithe-cocoa-92103_kubernetes
kind: Config
preferences: {}
users:
- name: lithe-cocoa-92103_kubernetes
  user:
    client-certificate-data: REDACTED
    client-key-data: REDACTED
    token: 65rZW78y8HbwXXtSXuUw9DbP4FLjHi4b
- name: lithe-cocoa-92103_kubernetes-basic-auth
  user:
    password: h5M0FtUUIflBSdI7
    username: admin
```

اکنون برای کار در فضای نام `development` به آن جابه‌جا می‌شویم.

```shell
kubectl config use-context dev
```

می‌توانید context فعلی خود را به این صورت بررسی کنید:

```shell
kubectl config current-context
```
```
dev
```

از این لحظه، دامنهٔ همهٔ درخواست‌هایی که از خط فرمان به کلاستر کوبرنتیز می‌فرستیم، فضای نام `development` است.

حالا مقداری محتوا ایجاد می‌کنیم.

{{% code_sample file="admin/snowflake-deployment.yaml" %}}

مانیفست را اعمال کنید تا یک Deployment ایجاد شود:

```shell
kubectl apply -f https://k8s.io/examples/admin/snowflake-deployment.yaml
```
یک Deployment با دو رونوشت (replica) ایجاد کرده‌ایم که Pod به نام `snowflake` را با یک کانتینر ساده اجرا می‌کند؛ این کانتینر نام میزبان (hostname) را برمی‌گرداند.

```shell
kubectl get deployment
```
```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
snowflake    2/2     2            2           2m
```

```shell
kubectl get pods -l app=snowflake
```
```
NAME                         READY     STATUS    RESTARTS   AGE
snowflake-3968820950-9dgr8   1/1       Running   0          2m
snowflake-3968820950-vgc4n   1/1       Running   0          2m
```

این عالی است؛ توسعه‌دهندگان می‌توانند هر کاری که می‌خواهند انجام دهند و نگرانی‌ای از بابت تأثیرگذاشتن بر محتوای فضای نام `production` ندارند.

اکنون به فضای نام `production` جابه‌جا می‌شویم تا نشان دهیم که منابع یک فضای نام از فضای نام دیگر پنهان هستند.

```shell
kubectl config use-context prod
```

فضای نام `production` باید خالی باشد و دستورهای زیر نباید چیزی برگردانند.

```shell
kubectl get deployment
kubectl get pods
```

محیط تولید ترجیح می‌دهد بارهای کاری را به‌صورت یکسان و جایگزین‌پذیر (cattle) اجرا کند؛ پس چند Pod از نوع cattle ایجاد می‌کنیم.

```shell
kubectl create deployment cattle --image=registry.k8s.io/serve_hostname --replicas=5

kubectl get deployment
```
```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
cattle       5/5     5            5           10s
```

```shell
kubectl get pods -l app=cattle
```
```
NAME                      READY     STATUS    RESTARTS   AGE
cattle-2263376956-41xy6   1/1       Running   0          34s
cattle-2263376956-kw466   1/1       Running   0          34s
cattle-2263376956-n4v97   1/1       Running   0          34s
cattle-2263376956-p5p3i   1/1       Running   0          34s
cattle-2263376956-sxpth   1/1       Running   0          34s
```

اکنون باید روشن شده باشد که منابعی که کاربران در یک فضای نام ایجاد می‌کنند، از فضای نام دیگر پنهان هستند.

با تکامل پشتیبانی از سیاست‌ها در کوبرنتیز، این سناریو را گسترش خواهیم داد تا نشان دهیم چگونه می‌توانید برای هر فضای نام
قواعد مجوزدهی متفاوتی تعیین کنید.
