---
title: مدیریت اعلانی آبجکت‌های کوبرنتیز با استفاده از فایل‌های پیکربندی
content_type: task
weight: 10
---

<!-- overview -->
برای ایجاد، به‌روزرسانی و حذف آبجکت‌های کوبرنتیز می‌توانید چندین فایل پیکربندی آبجکت را در یک دایرکتوری ذخیره کنید و با `kubectl apply` آن آبجکت‌ها را به‌صورت بازگشتی و در صورت نیاز ایجاد یا به‌روزرسانی کنید. در این روش، تغییراتی که مستقیماً روی آبجکت‌های زنده اعمال شده‌اند حفظ می‌شوند، بی‌آنکه آن تغییرات به فایل‌های پیکربندی آبجکت بازگردانده و ادغام شوند. همچنین فرمان `kubectl diff` پیش‌نمایشی از تغییراتی که `apply` اعمال خواهد کرد در اختیارتان می‌گذارد.

## {{% heading "prerequisites" %}}

ابزار [`kubectl`](/docs/tasks/tools/) را نصب کنید.

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## مزایا و معایب

ابزار `kubectl` از سه نوع مدیریت آبجکت پشتیبانی می‌کند:

* فرمان‌های دستوری (imperative)
* پیکربندی دستوری آبجکت
* پیکربندی اعلانی (declarative) آبجکت

برای بررسی مزایا و معایب هر یک از این روش‌های مدیریت آبجکت، به [مدیریت آبجکت‌های کوبرنتیز](/docs/concepts/overview/working-with-objects/object-management/) مراجعه کنید.

## نمای کلی

پیکربندی اعلانی آبجکت مستلزم درک عمیقی از تعریف‌ها و پیکربندی آبجکت‌های کوبرنتیز است. اگر هنوز اسناد زیر را مطالعه نکرده‌اید، آن‌ها را بخوانید و مراحلشان را انجام دهید:

* [مدیریت آبجکت‌های کوبرنتیز با استفاده از فرمان‌های دستوری](/docs/tasks/manage-kubernetes-objects/imperative-command/)
* [مدیریت دستوری آبجکت‌های کوبرنتیز با استفاده از فایل‌های پیکربندی](/docs/tasks/manage-kubernetes-objects/imperative-config/)

تعریف اصطلاحاتی که در این سند به کار رفته‌اند در ادامه آمده است:

- *فایل پیکربندی آبجکت / فایل پیکربندی*: فایلی که پیکربندی یک آبجکت کوبرنتیز را تعریف می‌کند. این مبحث نشان می‌دهد که چگونه فایل‌های پیکربندی را به `kubectl apply` بدهید. فایل‌های پیکربندی معمولاً در یک سامانه کنترل نسخه مانند Git نگهداری می‌شوند.
- *پیکربندی زنده آبجکت / پیکربندی زنده*: مقادیر پیکربندی زنده یک آبجکت، آن‌گونه که کلاستر کوبرنتیز مشاهده می‌کند. این مقادیر در ذخیره‌سازی کلاستر کوبرنتیز، که معمولاً etcd است، نگهداری می‌شوند.
- *نویسنده پیکربندی اعلانی / نویسنده اعلانی*: شخص یا مؤلفه‌ای نرم‌افزاری که یک آبجکت زنده را به‌روزرسانی می‌کند. نویسندگان زنده‌ای که در این مبحث به آن‌ها اشاره می‌شود، فایل‌های پیکربندی آبجکت را تغییر می‌دهند و برای نوشتن تغییرات، `kubectl apply` را اجرا می‌کنند.

## نحوه ایجاد آبجکت‌ها

با `kubectl apply` همه آبجکت‌هایی را که در فایل‌های پیکربندی یک دایرکتوری مشخص تعریف شده‌اند، به‌جز آن‌هایی که از قبل وجود دارند، ایجاد کنید:

```shell
kubectl apply -f <directory>
```

این فرمان حاشیه‌نویسی (annotation) `kubectl.kubernetes.io/last-applied-configuration: '{...}'` را روی هر آبجکت تنظیم می‌کند. این حاشیه‌نویسی شامل محتوای فایل پیکربندی آبجکتی است که برای ایجاد آن آبجکت استفاده شده است.

{{< note >}}
برای پردازش بازگشتی دایرکتوری‌ها، فلگ `-R` را اضافه کنید.
{{< /note >}}

نمونه‌ای از یک فایل پیکربندی آبجکت در ادامه آمده است:

{{% code_sample file="application/simple_deployment.yaml" %}}

برای چاپ آبجکتی که ایجاد خواهد شد، `kubectl diff` را اجرا کنید:

```shell
kubectl diff -f https://k8s.io/examples/application/simple_deployment.yaml
```

{{< note >}}
فرمان `diff` از [اجرای آزمایشی سمت سرور (server-side dry-run)](/docs/reference/using-api/api-concepts/#dry-run) استفاده می‌کند که باید روی `kube-apiserver` فعال باشد.

از آنجا که `diff` یک درخواست apply سمت سرور را در حالت اجرای آزمایشی انجام می‌دهد، به مجوزهای `PATCH`، `CREATE` و `UPDATE` نیاز دارد. برای جزئیات بیشتر به [مجوزدهی اجرای آزمایشی](/docs/reference/using-api/api-concepts#dry-run-authorization) مراجعه کنید.

{{< /note >}}

آبجکت را با `kubectl apply` ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/simple_deployment.yaml
```

پیکربندی زنده را با `kubectl get` چاپ کنید:

```shell
kubectl get -f https://k8s.io/examples/application/simple_deployment.yaml -o yaml
```

خروجی نشان می‌دهد که حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` در پیکربندی زنده نوشته شده و با فایل پیکربندی مطابقت دارد:

```yaml
kind: Deployment
metadata:
  annotations:
    # ...
    # This is the json representation of simple_deployment.yaml
    # It was written by kubectl apply when the object was created
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"minReadySeconds":5,"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.14.2","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
  # ...
spec:
  # ...
  minReadySeconds: 5
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        # ...
        name: nginx
        ports:
        - containerPort: 80
        # ...
      # ...
    # ...
  # ...
```

## نحوه به‌روزرسانی آبجکت‌ها

همچنین می‌توانید با `kubectl apply` همه آبجکت‌های تعریف‌شده در یک دایرکتوری را به‌روزرسانی کنید، حتی اگر آن آبجکت‌ها از قبل وجود داشته باشند. این روش کارهای زیر را انجام می‌دهد:

1. فیلدهایی را که در فایل پیکربندی وجود دارند، در پیکربندی زنده تنظیم می‌کند.
2. فیلدهایی را که از فایل پیکربندی حذف شده‌اند، از پیکربندی زنده پاک می‌کند.

```shell
kubectl diff -f <directory>
kubectl apply -f <directory>
```

{{< note >}}
برای پردازش بازگشتی دایرکتوری‌ها، فلگ `-R` را اضافه کنید.
{{< /note >}}

نمونه‌ای از یک فایل پیکربندی در ادامه آمده است:

{{% code_sample file="application/simple_deployment.yaml" %}}

آبجکت را با `kubectl apply` ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/simple_deployment.yaml
```

{{< note >}}
برای سادگی توضیح، فرمان بالا به‌جای یک دایرکتوری به یک فایل پیکربندی واحد اشاره می‌کند.
{{< /note >}}

پیکربندی زنده را با `kubectl get` چاپ کنید:

```shell
kubectl get -f https://k8s.io/examples/application/simple_deployment.yaml -o yaml
```

خروجی نشان می‌دهد که حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` در پیکربندی زنده نوشته شده و با فایل پیکربندی مطابقت دارد:

```yaml
kind: Deployment
metadata:
  annotations:
    # ...
    # This is the json representation of simple_deployment.yaml
    # It was written by kubectl apply when the object was created
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"minReadySeconds":5,"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.14.2","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
  # ...
spec:
  # ...
  minReadySeconds: 5
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        # ...
        name: nginx
        ports:
        - containerPort: 80
        # ...
      # ...
    # ...
  # ...
```

فیلد `replicas` را با استفاده از `kubectl scale` مستقیماً در پیکربندی زنده به‌روزرسانی کنید. در این کار از `kubectl apply` استفاده نمی‌شود:

```shell
kubectl scale deployment/nginx-deployment --replicas=2
```

پیکربندی زنده را با `kubectl get` چاپ کنید:

```shell
kubectl get deployment nginx-deployment -o yaml
```

خروجی نشان می‌دهد که فیلد `replicas` روی ۲ تنظیم شده و حاشیه‌نویسی `last-applied-configuration` فیلد `replicas` را در بر ندارد:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    # ...
    # note that the annotation does not contain replicas
    # because it was not updated through apply
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"minReadySeconds":5,"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.14.2","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
  # ...
spec:
  replicas: 2 # written by scale
  # ...
  minReadySeconds: 5
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        # ...
        name: nginx
        ports:
        - containerPort: 80
      # ...
```

فایل پیکربندی `simple_deployment.yaml` را به‌روزرسانی کنید تا ایمیج از `nginx:1.14.2` به `nginx:1.16.1` تغییر کند و فیلد `minReadySeconds` حذف شود:

{{% code_sample file="application/update_deployment.yaml" %}}

تغییرات انجام‌شده در فایل پیکربندی را اعمال کنید:

```shell
kubectl diff -f https://k8s.io/examples/application/update_deployment.yaml
kubectl apply -f https://k8s.io/examples/application/update_deployment.yaml
```

پیکربندی زنده را با `kubectl get` چاپ کنید:

```shell
kubectl get -f https://k8s.io/examples/application/update_deployment.yaml -o yaml
```

خروجی، تغییرات زیر را در پیکربندی زنده نشان می‌دهد:

* فیلد `replicas` همچنان مقدار ۲ را که `kubectl scale` تنظیم کرده بود حفظ می‌کند. این امر به این دلیل ممکن است که این فیلد در فایل پیکربندی وجود ندارد.
* فیلد `image` از `nginx:1.14.2` به `nginx:1.16.1` به‌روزرسانی شده است.
* حاشیه‌نویسی `last-applied-configuration` با ایمیج جدید به‌روزرسانی شده است.
* فیلد `minReadySeconds` پاک شده است.
* حاشیه‌نویسی `last-applied-configuration` دیگر فیلد `minReadySeconds` را در بر ندارد.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    # ...
    # The annotation contains the updated image to nginx 1.16.1,
    # but does not contain the updated replicas to 2
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.16.1","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
    # ...
spec:
  replicas: 2 # Set by `kubectl scale`.  Ignored by `kubectl apply`.
  # minReadySeconds cleared by `kubectl apply`
  # ...
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.16.1 # Set by `kubectl apply`
        # ...
        name: nginx
        ports:
        - containerPort: 80
        # ...
      # ...
    # ...
  # ...
```

{{< warning >}}
استفاده هم‌زمان از `kubectl apply` و فرمان‌های پیکربندی دستوری آبجکت، یعنی `create` و `replace`، پشتیبانی نمی‌شود. دلیلش این است که `create` و `replace` حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` را که `kubectl apply` برای محاسبه به‌روزرسانی‌ها از آن استفاده می‌کند، حفظ نمی‌کنند.
{{< /warning >}}

## نحوه حذف آبجکت‌ها

برای حذف آبجکت‌هایی که با `kubectl apply` مدیریت می‌شوند، دو روش وجود دارد.

### روش توصیه‌شده: `kubectl delete -f <filename>`

روش توصیه‌شده، حذف دستی آبجکت‌ها با فرمان دستوری است؛ زیرا در این روش به‌روشنی مشخص است چه چیزی حذف می‌شود و احتمال اینکه کاربر ناخواسته چیزی را حذف کند کمتر است:

```shell
kubectl delete -f <filename>
```

### روش جایگزین: `kubectl apply -f <directory> --prune`

به‌عنوان جایگزینی برای `kubectl delete`، می‌توانید از `kubectl apply` استفاده کنید تا آبجکت‌هایی را که مانیفستشان از یک دایرکتوری در سیستم فایل محلی حذف شده است، برای حذف شناسایی کنید.

در کوبرنتیز {{< skew currentVersion >}}، دو حالت هرس (pruning) در kubectl apply در دسترس است:

- هرس مبتنی بر فهرست مجاز (allowlist): این حالت از kubectl نسخه v1.5 وجود داشته است، اما به دلیل مشکلات طراحی آن از نظر کاربردپذیری، درستی و کارایی، همچنان در مرحله آلفا قرار دارد. حالت مبتنی بر ApplySet برای جایگزینی آن طراحی شده است.
- هرس مبتنی بر ApplySet: یک _مجموعه اعمال (apply set)_ آبجکتی سمت سرور است (به‌طور پیش‌فرض یک Secret) که kubectl می‌تواند از آن برای ردیابی دقیق و کارآمد عضویت در مجموعه در طول عملیات‌های **apply** استفاده کند. این حالت در kubectl نسخه v1.27 به‌صورت آلفا و به‌عنوان جایگزینی برای هرس مبتنی بر فهرست مجاز معرفی شد.

{{< tabs name="kubectl_apply_prune" >}}
{{% tab name="فهرست مجاز" %}}

{{< feature-state for_k8s_version="v1.5" state="alpha" >}}

{{< warning >}}
هنگام استفاده از `--prune` همراه با `kubectl apply` در حالت فهرست مجاز احتیاط کنید. اینکه کدام آبجکت‌ها هرس شوند به مقادیر فلگ‌های `--prune-allowlist`، `--selector` و `--namespace` بستگی دارد و بر کشف پویای آبجکت‌های موجود در محدوده متکی است. به‌ویژه اگر مقادیر فلگ‌ها بین دو اجرا تغییر کند، ممکن است آبجکت‌ها به‌طور غیرمنتظره حذف یا حفظ شوند.
{{< /warning >}}

برای استفاده از هرس مبتنی بر فهرست مجاز، فلگ‌های زیر را به فرمان `kubectl apply` خود اضافه کنید:

- `--prune`: آبجکت‌هایی را که پیش‌تر اعمال شده‌اند و در مجموعه ارسال‌شده به اجرای فعلی وجود ندارند، حذف می‌کند.
- `--prune-allowlist`: فهرستی از group-version-kindها (GVK) که برای هرس در نظر گرفته می‌شوند. این فلگ اختیاری است، اما استفاده از آن به‌شدت توصیه می‌شود؛ زیرا مقدار پیش‌فرض آن فهرستی ناقص از انواع وابسته به فضای نام (namespace) و انواع در سطح کلاستر است که ممکن است به نتایج غیرمنتظره‌ای منجر شود.
- `--selector/-l`: با یک انتخابگر (selector) برچسب، مجموعه آبجکت‌هایی را که برای هرس انتخاب می‌شوند محدود می‌کند. این فلگ اختیاری است، اما استفاده از آن به‌شدت توصیه می‌شود.
- `--all`: به‌جای `--selector/-l` از آن استفاده کنید تا همه آبجکت‌هایی را که پیش‌تر اعمال شده‌اند و از انواع موجود در فهرست مجاز هستند، صراحتاً انتخاب کنید.

در هرس مبتنی بر فهرست مجاز، از سرور API همه آبجکت‌هایی از GVKهای موجود در فهرست مجاز که با برچسب‌های داده‌شده (در صورت وجود) مطابقت دارند پرس‌وجو می‌شود و سپس تلاش می‌شود پیکربندی‌های زنده بازگشتی با فایل‌های مانیفست آبجکت تطبیق داده شوند. اگر آبجکتی با پرس‌وجو مطابقت داشته باشد، مانیفستی در دایرکتوری نداشته باشد و حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` را داشته باشد، حذف می‌شود.

```shell
kubectl apply -f <directory> --prune -l <labels> --prune-allowlist=<gvk-list>
```

{{< warning >}}
اعمال همراه با هرس را باید فقط روی دایرکتوری ریشه‌ای اجرا کرد که مانیفست‌های آبجکت را در بر دارد. اجرای آن روی زیردایرکتوری‌ها ممکن است باعث حذف ناخواسته آبجکت‌هایی شود که پیش‌تر اعمال شده‌اند، برچسب‌های داده‌شده (در صورت وجود) را دارند و در آن زیردایرکتوری وجود ندارند.
{{< /warning >}}

{{% /tab %}}

{{% tab name="مجموعه اعمال" %}}

{{< feature-state for_k8s_version="v1.27" state="alpha" >}}

{{< caution >}}
فرمان `kubectl apply --prune --applyset` در مرحله آلفا است و ممکن است در نسخه‌های بعدی تغییراتی ناسازگار با نسخه‌های پیشین در آن ایجاد شود.
{{< /caution >}}

برای استفاده از هرس مبتنی بر ApplySet، متغیر محیطی `KUBECTL_APPLYSET=true` را تنظیم کنید و فلگ‌های زیر را به فرمان `kubectl apply` خود اضافه کنید:
- `--prune`: آبجکت‌هایی را که پیش‌تر اعمال شده‌اند و در مجموعه ارسال‌شده به اجرای فعلی وجود ندارند، حذف می‌کند.
- `--applyset`: نام آبجکتی که kubectl می‌تواند از آن برای ردیابی دقیق و کارآمد عضویت در مجموعه در طول عملیات‌های `apply` استفاده کند.

```shell
KUBECTL_APPLYSET=true kubectl apply -f <directory> --prune --applyset=<name>
```

به‌طور پیش‌فرض، نوع آبجکت والد ApplySet یک Secret است. با این حال، می‌توان از ConfigMap نیز با قالب `--applyset=configmaps/<name>` استفاده کرد. هنگام استفاده از Secret یا ConfigMap، اگر آبجکت از قبل وجود نداشته باشد، kubectl آن را ایجاد می‌کند.

همچنین می‌توان از منابع سفارشی (custom resources) به‌عنوان آبجکت والد ApplySet استفاده کرد. برای فعال کردن این امکان، به تعریف منبع سفارشی (CRD) که منبع موردنظرتان را تعریف می‌کند، برچسب `applyset.kubernetes.io/is-parent-type: true` را اضافه کنید. سپس آبجکتی را که می‌خواهید به‌عنوان والد ApplySet استفاده کنید ایجاد کنید (kubectl این کار را برای منابع سفارشی به‌طور خودکار انجام نمی‌دهد). در پایان، در فلگ applyset به این صورت به آن آبجکت ارجاع دهید: `--applyset=<resource>.<group>/<name>` (برای مثال، `widgets.custom.example.com/widget-name`).

در هرس مبتنی بر ApplySet، kubectl پیش از ارسال آبجکت‌های مجموعه به سرور، برچسب `applyset.kubernetes.io/part-of=<parentID>` را به هر یک از آن‌ها اضافه می‌کند. همچنین به دلایل کارایی، فهرست انواع منابع و فضاهای نامی را که مجموعه در بر دارد جمع‌آوری می‌کند و آن‌ها را در قالب حاشیه‌نویسی‌هایی روی آبجکت والد زنده قرار می‌دهد. در نهایت، در پایان عملیات apply، از سرور API آبجکت‌هایی از آن انواع را در آن فضاهای نام (یا حسب مورد در سطح کلاستر) پرس‌وجو می‌کند که طبق برچسب `applyset.kubernetes.io/part-of=<parentID>` به مجموعه تعلق دارند.

هشدارها و محدودیت‌ها:

- هر آبجکت حداکثر می‌تواند عضو یک مجموعه باشد.
- هنگام استفاده از هر والد وابسته به فضای نام، از جمله Secret پیش‌فرض، فلگ `--namespace` الزامی است. یعنی ApplySetهایی که چند فضای نام را در بر می‌گیرند، باید از یک منبع سفارشی در سطح کلاستر به‌عنوان آبجکت والد استفاده کنند.
- برای استفاده ایمن از هرس مبتنی بر ApplySet با چند دایرکتوری، برای هر دایرکتوری یک نام ApplySet یکتا به کار ببرید.

{{% /tab %}}

{{< /tabs >}}

## نحوه مشاهده یک آبجکت

برای مشاهده پیکربندی یک آبجکت زنده می‌توانید از `kubectl get` همراه با `-o yaml` استفاده کنید:

```shell
kubectl get -f <filename|url> -o yaml
```

## نحوه محاسبه تفاوت‌ها و ادغام تغییرات در apply

{{< caution >}}
یک *وصله (patch)* عملیات به‌روزرسانی‌ای است که به‌جای کل آبجکت، فقط فیلدهای مشخصی از آن را هدف می‌گیرد. به این ترتیب می‌توان تنها مجموعه مشخصی از فیلدهای یک آبجکت را بدون خواندن آن آبجکت به‌روزرسانی کرد.
{{< /caution >}}

وقتی `kubectl apply` پیکربندی زنده یک آبجکت را به‌روزرسانی می‌کند، این کار را با ارسال یک درخواست وصله به سرور API انجام می‌دهد. این وصله به‌روزرسانی‌هایی را تعریف می‌کند که فقط فیلدهای مشخصی از پیکربندی زنده آبجکت را در بر می‌گیرند. فرمان `kubectl apply` این درخواست وصله را با استفاده از فایل پیکربندی، پیکربندی زنده و حاشیه‌نویسی `last-applied-configuration` ذخیره‌شده در پیکربندی زنده محاسبه می‌کند.

### محاسبهٔ وصله‌ی ادغام (merge patch)

فرمان `kubectl apply` محتوای فایل پیکربندی را در حاشیه‌نویسی (annotation) `kubectl.kubernetes.io/last-applied-configuration` می‌نویسد. از این حاشیه‌نویسی برای شناسایی فیلدهایی استفاده می‌شود که از فایل پیکربندی حذف شده‌اند و باید از پیکربندی زنده نیز پاک شوند. مراحل زیر برای محاسبهٔ فیلدهایی که باید حذف یا مقداردهی شوند به کار می‌رود:

1. فیلدهای حذف‌شدنی محاسبه می‌شوند. این فیلدها در `last-applied-configuration` وجود دارند، اما در فایل پیکربندی نیستند.
2. فیلدهایی که باید افزوده یا مقداردهی شوند محاسبه می‌شوند. این فیلدها در فایل پیکربندی وجود دارند و مقدارشان با پیکربندی زنده یکسان نیست.

به مثال زیر توجه کنید. فرض کنید فایل پیکربندی یک آبجکت Deployment چنین است:

{{% code_sample file="application/update_deployment.yaml" %}}

همچنین فرض کنید پیکربندی زندهٔ همین آبجکت Deployment به این صورت است:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    # ...
    # note that the annotation does not contain replicas
    # because it was not updated through apply
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"minReadySeconds":5,"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.14.2","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
  # ...
spec:
  replicas: 2 # written by scale
  # ...
  minReadySeconds: 5
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        # ...
        name: nginx
        ports:
        - containerPort: 80
      # ...
```

محاسبات ادغامی که `kubectl apply` انجام می‌دهد به این شرح است:

1. فیلدهای حذف‌شدنی با خواندن مقادیر از `last-applied-configuration` و مقایسهٔ آن‌ها با مقادیر فایل پیکربندی محاسبه می‌شوند.
   فیلدهایی که در فایل پیکربندی محلی آبجکت صراحتاً null شده‌اند پاک می‌شوند، صرف‌نظر از اینکه در `last-applied-configuration` آمده باشند یا نه.
   در این مثال، `minReadySeconds` در حاشیه‌نویسی `last-applied-configuration` آمده، اما در فایل پیکربندی وجود ندارد.
   **اقدام:** `minReadySeconds` از پیکربندی زنده پاک می‌شود.
2. فیلدهایی که باید مقداردهی شوند با خواندن مقادیر از فایل پیکربندی و مقایسهٔ آن‌ها با مقادیر پیکربندی زنده محاسبه می‌شوند. در این مثال، مقدار `image` در فایل پیکربندی با مقدار آن در پیکربندی زنده یکسان نیست. **اقدام:** مقدار `image` در پیکربندی زنده تنظیم می‌شود.
3. حاشیه‌نویسی `last-applied-configuration` مطابق با مقدار فایل پیکربندی تنظیم می‌شود.
4. نتایج مراحل ۱، ۲ و ۳ در قالب یک درخواست وصله (patch) واحد ادغام و به سرور API فرستاده می‌شوند.

پیکربندی زنده‌ای که از این ادغام به دست می‌آید چنین است:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    # ...
    # The annotation contains the updated image to nginx 1.16.1,
    # but does not contain the updated replicas to 2
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.16.1","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
    # ...
spec:
  selector:
    matchLabels:
      # ...
      app: nginx
  replicas: 2 # Set by `kubectl scale`.  Ignored by `kubectl apply`.
  # minReadySeconds cleared by `kubectl apply`
  # ...
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.16.1 # Set by `kubectl apply`
        # ...
        name: nginx
        ports:
        - containerPort: 80
        # ...
      # ...
    # ...
  # ...
```

### نحوهٔ ادغام انواع مختلف فیلدها

اینکه یک فیلد مشخص در فایل پیکربندی چگونه با پیکربندی زنده ادغام شود، به نوع آن فیلد بستگی دارد. فیلدها انواع مختلفی دارند:

- *اولیه (primitive)*: فیلدی از نوع رشته، عدد صحیح یا بولی.
  برای مثال، `image` و `replicas` فیلدهای اولیه هستند. **اقدام:** جایگزینی.

- *نگاشت (map)* که *آبجکت* نیز نامیده می‌شود: فیلدی از نوع نگاشت یا نوعی مرکب که زیرفیلدهایی دارد. برای مثال، `labels`، `annotations`، `spec` و `metadata` همگی نگاشت هستند. **اقدام:** ادغام عناصر یا زیرفیلدها.

- *فهرست (list)*: فیلدی شامل فهرستی از اقلام که می‌توانند از نوع اولیه یا نگاشت باشند.
  برای مثال، `containers`، `ports` و `args` فهرست هستند. **اقدام:** متغیر است.

وقتی `kubectl apply` یک فیلد نگاشت یا فهرست را به‌روزرسانی می‌کند، معمولاً کل فیلد را جایگزین نمی‌کند، بلکه زیرعناصر آن را یک‌به‌یک به‌روزرسانی می‌کند. برای نمونه، هنگام ادغام `spec` یک Deployment، کل `spec` جایگزین نمی‌شود؛ در عوض زیرفیلدهای `spec`، مانند `replicas`، مقایسه و ادغام می‌شوند.

### ادغام تغییرات فیلدهای اولیه

فیلدهای اولیه جایگزین یا پاک می‌شوند.

{{< note >}}
علامت `-` به معنای «موضوعیت ندارد» به کار رفته است، زیرا از آن مقدار استفاده نمی‌شود.
{{< /note >}}

| فیلد در فایل پیکربندی آبجکت  | فیلد در پیکربندی زندهٔ آبجکت | فیلد در last-applied-configuration | اقدام                                    |
|-------------------------------------|------------------------------------|-------------------------------------|-------------------------------------------|
| بله                                 | بله                                | -                                   | مقدار زنده برابر مقدار فایل پیکربندی قرار می‌گیرد.  |
| بله                                 | خیر                                 | -                                   | مقدار زنده برابر پیکربندی محلی قرار می‌گیرد.           |
| خیر                                  | -                                  | بله                                 | از پیکربندی زنده پاک می‌شود.            |
| خیر                                  | -                                  | خیر                                  | کاری انجام نمی‌شود و مقدار زنده حفظ می‌شود.             |

### ادغام تغییرات فیلدهای نگاشت

فیلدهایی که نگاشت هستند با مقایسهٔ تک‌تک زیرفیلدها یا عناصر نگاشت ادغام می‌شوند:

{{< note >}}
علامت `-` به معنای «موضوعیت ندارد» به کار رفته است، زیرا از آن مقدار استفاده نمی‌شود.
{{< /note >}}

| کلید در فایل پیکربندی آبجکت    | کلید در پیکربندی زندهٔ آبجکت   | فیلد در last-applied-configuration | اقدام                           |
|-------------------------------------|------------------------------------|-------------------------------------|----------------------------------|
| بله                                 | بله                                | -                                   | مقادیر زیرفیلدها مقایسه می‌شوند.        |
| بله                                 | خیر                                 | -                                   | مقدار زنده برابر پیکربندی محلی قرار می‌گیرد.  |
| خیر                                  | -                                  | بله                                 | از پیکربندی زنده حذف می‌شود.   |
| خیر                                  | -                                  | خیر                                  | کاری انجام نمی‌شود و مقدار زنده حفظ می‌شود.     |

### ادغام تغییرات فیلدهای از نوع فهرست

برای ادغام تغییرات یک فهرست، یکی از سه راهبرد زیر به کار می‌رود:

* اگر همهٔ عناصر فهرست اولیه باشند، کل فهرست جایگزین می‌شود.
* در فهرستی از عناصر مرکب، عناصر به‌صورت جداگانه ادغام می‌شوند.
* فهرستی از عناصر اولیه ادغام می‌شود.

انتخاب راهبرد برای هر فیلد به‌طور جداگانه انجام می‌شود.

#### جایگزینی فهرست در صورتی که همهٔ عناصر آن اولیه باشند

با فهرست همانند یک فیلد اولیه رفتار می‌شود و کل فهرست جایگزین یا حذف می‌شود. در این روش ترتیب عناصر حفظ می‌شود.

**مثال:** با `kubectl apply` فیلد `args` یک کانتینر در یک Pod را به‌روزرسانی کنید. با این کار، مقدار `args` در پیکربندی زنده برابر مقدار آن در فایل پیکربندی قرار می‌گیرد.
هر عنصری از `args` که پیش‌تر به پیکربندی زنده افزوده شده باشد از بین می‌رود.
ترتیب عناصر `args` که در فایل پیکربندی تعریف شده‌اند، در پیکربندی زنده حفظ می‌شود.

```yaml
# last-applied-configuration value
    args: ["a", "b"]

# configuration file value
    args: ["a", "c"]

# live configuration
    args: ["a", "b", "d"]

# result after merge
    args: ["a", "c"]
```

**توضیح:** در این ادغام، مقدار فایل پیکربندی به‌عنوان مقدار جدید فهرست به کار رفته است.

#### ادغام جداگانهٔ عناصر در فهرستی از عناصر مرکب:

با فهرست همانند یک نگاشت رفتار می‌شود و یکی از فیلدهای مشخص هر عنصر نقش کلید را دارد. عناصر به‌صورت جداگانه افزوده، حذف یا به‌روزرسانی می‌شوند. در این روش ترتیب عناصر حفظ نمی‌شود.

این راهبرد ادغام از برچسب ویژه‌ای به نام `patchMergeKey` روی هر فیلد استفاده می‌کند. مقدار `patchMergeKey` برای هر فیلد در کد منبع کوبرنتیز تعریف شده است:
[types.go](https://github.com/kubernetes/api/blob/d04500c8c3dda9c980b668c57abc2ca61efcf5c4/core/v1/types.go#L2747)
هنگام ادغام فهرستی از نگاشت‌ها، فیلدی که به‌عنوان `patchMergeKey` یک عنصر تعیین شده است، مانند کلید نگاشت برای آن عنصر به کار می‌رود.

**مثال:** با `kubectl apply` فیلد `containers` یک PodSpec را به‌روزرسانی کنید.
در این حالت، فهرست طوری ادغام می‌شود که گویی نگاشتی است که کلید هر عنصر آن `name` است.

```yaml
# last-applied-configuration value
    containers:
    - name: nginx
      image: nginx:1.16
    - name: nginx-helper-a # key: nginx-helper-a; will be deleted in result
      image: helper:1.3
    - name: nginx-helper-b # key: nginx-helper-b; will be retained
      image: helper:1.3

# configuration file value
    containers:
    - name: nginx
      image: nginx:1.16
    - name: nginx-helper-b
      image: helper:1.3
    - name: nginx-helper-c # key: nginx-helper-c; will be added in result
      image: helper:1.3

# live configuration
    containers:
    - name: nginx
      image: nginx:1.16
    - name: nginx-helper-a
      image: helper:1.3
    - name: nginx-helper-b
      image: helper:1.3
      args: ["run"] # Field will be retained
    - name: nginx-helper-d # key: nginx-helper-d; will be retained
      image: helper:1.3

# result after merge
    containers:
    - name: nginx
      image: nginx:1.16
      # Element nginx-helper-a was deleted
    - name: nginx-helper-b
      image: helper:1.3
      args: ["run"] # Field was retained
    - name: nginx-helper-c # Element was added
      image: helper:1.3
    - name: nginx-helper-d # Element was ignored
      image: helper:1.3
```

**توضیح:**

- کانتینری با نام «nginx-helper-a» حذف شد، زیرا هیچ کانتینری با این نام در فایل پیکربندی وجود نداشت.
- کانتینری با نام «nginx-helper-b» تغییرات `args` در پیکربندی زنده را حفظ کرد. فرمان `kubectl apply` توانست تشخیص دهد که «nginx-helper-b» در پیکربندی زنده همان «nginx-helper-b» در فایل پیکربندی است، هرچند فیلدهای آن‌ها مقادیر متفاوتی داشتند (در فایل پیکربندی `args` وجود نداشت). دلیل این امر یکسان بودن مقدار فیلد `patchMergeKey` (یعنی name) در هر دو بود.
- کانتینری با نام «nginx-helper-c» افزوده شد، زیرا هیچ کانتینری با این نام در پیکربندی زنده وجود نداشت، اما کانتینری با همین نام در فایل پیکربندی آمده بود.
- کانتینری با نام «nginx-helper-d» حفظ شد، زیرا هیچ عنصری با این نام در last-applied-configuration وجود نداشت.

#### ادغام فهرستی از عناصر اولیه

از نسخهٔ ۱.۵ کوبرنتیز، ادغام فهرست‌هایی از عناصر اولیه پشتیبانی نمی‌شود.

{{< note >}}
اینکه کدام‌یک از راهبردهای بالا برای یک فیلد مشخص انتخاب شود، با برچسب `patchStrategy` در [types.go](https://github.com/kubernetes/api/blob/d04500c8c3dda9c980b668c57abc2ca61efcf5c4/core/v1/types.go#L2748) تعیین می‌شود.
اگر برای فیلدی از نوع فهرست هیچ `patchStrategy` مشخص نشده باشد، فهرست جایگزین می‌شود.
{{< /note >}}

{{< comment >}}
TODO(pwittrock): این بخش را برای نسخهٔ ۱.۶ از حالت توضیح خارج کنید

- با فهرست همانند مجموعه‌ای از عناصر اولیه رفتار می‌شود و عناصر به‌صورت جداگانه جایگزین یا حذف می‌شوند. ترتیب و عناصر تکراری حفظ نمی‌شوند.

**مثال:** استفاده از apply برای به‌روزرسانی فیلد `finalizers` در ObjectMeta، عناصری را که به پیکربندی زنده افزوده شده‌اند حفظ می‌کند، اما ترتیب finalizerها از بین می‌رود.
{{< /comment >}}

## مقادیر پیش‌فرض فیلدها

اگر برخی فیلدها هنگام ایجاد آبجکت مشخص نشده باشند، سرور API آن‌ها را در پیکربندی زنده با مقادیر پیش‌فرض پر می‌کند.

در ادامه، یک فایل پیکربندی برای Deployment آمده است. این فایل فیلد `strategy` را مشخص نمی‌کند:

{{% code_sample file="application/simple_deployment.yaml" %}}

آبجکت را با `kubectl apply` ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/simple_deployment.yaml
```

پیکربندی زنده را با `kubectl get` چاپ کنید:

```shell
kubectl get -f https://k8s.io/examples/application/simple_deployment.yaml -o yaml
```

خروجی نشان می‌دهد که سرور API چندین فیلد را در پیکربندی زنده با مقادیر پیش‌فرض پر کرده است. این فیلدها در فایل پیکربندی مشخص نشده بودند.

```yaml
apiVersion: apps/v1
kind: Deployment
# ...
spec:
  selector:
    matchLabels:
      app: nginx
  minReadySeconds: 5
  replicas: 1 # defaulted by apiserver
  strategy:
    rollingUpdate: # defaulted by apiserver - derived from strategy.type
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate # defaulted by apiserver
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        imagePullPolicy: IfNotPresent # defaulted by apiserver
        name: nginx
        ports:
        - containerPort: 80
          protocol: TCP # defaulted by apiserver
        resources: {} # defaulted by apiserver
        terminationMessagePath: /dev/termination-log # defaulted by apiserver
      dnsPolicy: ClusterFirst # defaulted by apiserver
      restartPolicy: Always # defaulted by apiserver
      securityContext: {} # defaulted by apiserver
      terminationGracePeriodSeconds: 30 # defaulted by apiserver
# ...
```

در یک درخواست وصله، فیلدهایی که مقدار پیش‌فرض گرفته‌اند دوباره مقدار پیش‌فرض نمی‌گیرند، مگر اینکه در همان درخواست وصله صراحتاً پاک شوند. این موضوع ممکن است برای فیلدهایی که مقدار پیش‌فرضشان بر اساس مقادیر فیلدهای دیگر تعیین می‌شود، رفتار غیرمنتظره‌ای ایجاد کند. اگر بعداً آن فیلدهای دیگر تغییر کنند، مقادیر پیش‌فرضی که از آن‌ها به دست آمده‌اند به‌روزرسانی نمی‌شوند، مگر اینکه صراحتاً پاک شوند.

به همین دلیل، توصیه می‌شود برخی فیلدهایی را که سرور به آن‌ها مقدار پیش‌فرض می‌دهد، صراحتاً در فایل پیکربندی تعریف کنید، حتی اگر مقادیر دلخواه شما با مقادیر پیش‌فرض سرور یکسان باشد. با این کار، تشخیص مقادیر متعارضی که سرور دوباره به آن‌ها مقدار پیش‌فرض نمی‌دهد آسان‌تر می‌شود.

**مثال:**

```yaml
# last-applied-configuration
spec:
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80

# configuration file
spec:
  strategy:
    type: Recreate # updated value
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80

# live configuration
spec:
  strategy:
    type: RollingUpdate # defaulted value
    rollingUpdate: # defaulted value derived from type
      maxSurge : 1
      maxUnavailable: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80

# result after merge - ERROR!
spec:
  strategy:
    type: Recreate # updated value: incompatible with rollingUpdate
    rollingUpdate: # defaulted value: incompatible with "type: Recreate"
      maxSurge : 1
      maxUnavailable: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

**توضیح:**

1. کاربر یک Deployment را بدون تعریف `strategy.type` ایجاد می‌کند.
2. سرور مقدار پیش‌فرض `RollingUpdate` را برای `strategy.type` قرار می‌دهد و به مقادیر `strategy.rollingUpdate` نیز مقدار پیش‌فرض می‌دهد.
3. کاربر `strategy.type` را به `Recreate` تغییر می‌دهد. مقادیر `strategy.rollingUpdate` همچنان مقادیر پیش‌فرض خود را دارند، درحالی‌که سرور انتظار دارد پاک شده باشند.
   اگر مقادیر `strategy.rollingUpdate` از ابتدا در فایل پیکربندی تعریف شده بودند، روشن‌تر بود که باید حذف شوند.
4. عملیات apply شکست می‌خورد، زیرا `strategy.rollingUpdate` پاک نشده است. فیلد `strategy.rollingupdate` را نمی‌توان همراه با `strategy.type` برابر `Recreate` تعریف کرد.

توصیه: فیلدهای زیر باید صراحتاً در فایل پیکربندی آبجکت تعریف شوند:

- انتخابگرها (selectors) و برچسب‌های PodTemplate در بارهای کاری، مانند Deployment، StatefulSet، Job، DaemonSet، ReplicaSet و ReplicationController
- راهبرد rollout در Deployment

### نحوهٔ پاک کردن فیلدهایی که سرور به آن‌ها مقدار پیش‌فرض داده یا نویسندگان دیگر مقداردهی کرده‌اند

فیلدهایی را که در فایل پیکربندی نیامده‌اند می‌توان با قرار دادن مقدارشان برابر `null` و سپس اعمال فایل پیکربندی پاک کرد.
برای فیلدهایی که سرور به آن‌ها مقدار پیش‌فرض داده است، این کار باعث می‌شود مقادیرشان دوباره مقدار پیش‌فرض بگیرند.

## نحوهٔ تغییر مالکیت یک فیلد میان فایل پیکربندی و نویسندگان دستوری مستقیم

برای تغییر یک فیلد مجزا از یک آبجکت، فقط باید از روش‌های زیر استفاده کنید:

- استفاده از `kubectl apply`.
- نوشتن مستقیم در پیکربندی زنده بدون تغییر فایل پیکربندی؛
برای مثال، استفاده از `kubectl scale`.

### تغییر مالک از نویسندهٔ دستوری مستقیم به فایل پیکربندی

فیلد را به فایل پیکربندی بیفزایید. از آن پس، به‌روزرسانی‌های مستقیم آن فیلد در پیکربندی زنده را که از طریق `kubectl apply` انجام نمی‌شوند متوقف کنید.

### تغییر مالک از فایل پیکربندی به نویسندهٔ دستوری مستقیم

از نسخهٔ ۱.۵ کوبرنتیز، تغییر مالکیت یک فیلد از فایل پیکربندی به یک نویسندهٔ دستوری به مراحل دستی نیاز دارد:

- فیلد را از فایل پیکربندی حذف کنید.
- فیلد را از حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` روی آبجکت زنده حذف کنید.

## تغییر روش‌های مدیریت

آبجکت‌های کوبرنتیز باید در هر زمان فقط با یک روش مدیریت شوند.
جابه‌جایی از یک روش به روش دیگر امکان‌پذیر است، اما فرایندی دستی است.

{{< note >}}
استفاده از حذف دستوری در کنار مدیریت اعلانی مشکلی ندارد.
{{< /note >}}

{{< comment >}}
TODO(pwittrock): باید کاری کنیم که استفاده از فرمان‌های دستوری همراه با پیکربندی اعلانی آبجکت به‌درستی کار کند، به‌طوری که فیلدها در حاشیه‌نویسی نوشته نشوند. سپس این مورد را اضافه کنید.

- استفاده از فرمان‌های دستوری همراه با پیکربندی اعلانی برای مدیریت، به‌طوری که هر کدام فیلدهای متفاوتی را مدیریت کنند.
{{< /comment >}}

### مهاجرت از مدیریت با فرمان‌های دستوری به پیکربندی اعلانی آبجکت

مهاجرت از مدیریت با فرمان‌های دستوری به پیکربندی اعلانی آبجکت شامل چند مرحلهٔ دستی است:

1. آبجکت زنده را در یک فایل پیکربندی محلی صادر کنید:

   ```shell
   kubectl get <kind>/<name> -o yaml > <kind>_<name>.yaml
   ```

1. فیلد `status` را به‌صورت دستی از فایل پیکربندی حذف کنید.

   {{< note >}}
   این مرحله اختیاری است، زیرا `kubectl apply` فیلد status را به‌روزرسانی نمی‌کند، حتی اگر در فایل پیکربندی وجود داشته باشد.
   {{< /note >}}

1. حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` را روی آبجکت تنظیم کنید:

   ```shell
   kubectl replace --save-config -f <kind>_<name>.yaml
   ```

1. فرایندها را طوری تغییر دهید که آبجکت منحصراً با `kubectl apply` مدیریت شود.

{{< comment >}}
TODO(pwittrock): چرا export فیلد status را حذف نمی‌کند؟ به نظر می‌رسد باید این کار را انجام دهد.
{{< /comment >}}

### مهاجرت از پیکربندی دستوری آبجکت به پیکربندی اعلانی آبجکت

1. حاشیه‌نویسی `kubectl.kubernetes.io/last-applied-configuration` را روی آبجکت تنظیم کنید:

   ```shell
   kubectl replace --save-config -f <kind>_<name>.yaml
   ```

1. فرایندها را طوری تغییر دهید که آبجکت منحصراً با `kubectl apply` مدیریت شود.

## تعریف انتخابگرهای کنترل‌کننده و برچسب‌های PodTemplate

{{< warning >}}
به‌روزرسانی انتخابگرهای کنترل‌کننده‌ها اکیداً توصیه نمی‌شود.
{{< /warning >}}

رویکرد توصیه‌شده این است که یک برچسب PodTemplate واحد و تغییرناپذیر تعریف کنید که فقط انتخابگر کنترل‌کننده از آن استفاده کند و معنای دیگری نداشته باشد.

**مثال:**

```yaml
selector:
  matchLabels:
      controller-selector: "apps/v1/deployment/nginx"
template:
  metadata:
    labels:
      controller-selector: "apps/v1/deployment/nginx"
```

## {{% heading "whatsnext" %}}

* [مدیریت آبجکت‌های کوبرنتیز با فرمان‌های دستوری](/docs/tasks/manage-kubernetes-objects/imperative-command/)
* [مدیریت دستوری آبجکت‌های کوبرنتیز با فایل‌های پیکربندی](/docs/tasks/manage-kubernetes-objects/imperative-config/)
* [مرجع فرمان‌های Kubectl](/docs/reference/generated/kubectl/kubectl-commands/)
* [مرجع API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/)
