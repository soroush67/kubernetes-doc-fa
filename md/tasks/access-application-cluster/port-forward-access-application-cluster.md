---
title: استفاده از Port Forwarding برای دسترسی به برنامه‌ها در یک کلاستر
content_type: task
weight: 40
min-kubernetes-server-version: v1.10
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه با استفاده از `kubectl port-forward` به یک سرور MongoDB
که در یک کلاستر کوبرنتیز اجرا می‌شود متصل شوید. این نوع اتصال برای اشکال‌زدایی
پایگاه داده می‌تواند مفید باشد.

## {{% heading "prerequisites" %}}

* {{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}
* ابزار [MongoDB Shell](https://www.mongodb.com/try/download/shell) را نصب کنید.

<!-- steps -->

## ایجاد Deployment و Service برای MongoDB

1. یک Deployment ایجاد کنید که MongoDB را اجرا کند:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-deployment.yaml
   ```

   خروجی یک فرمان موفق تأیید می‌کند که Deployment ایجاد شده است:

   ```
   deployment.apps/mongo created
   ```

   وضعیت پاد را مشاهده کنید تا از آماده بودن آن مطمئن شوید:

   ```shell
   kubectl get pods
   ```

   خروجی، پاد ایجادشده را نمایش می‌دهد:

   ```
   NAME                     READY   STATUS    RESTARTS   AGE
   mongo-75f59d57f4-4nd6q   1/1     Running   0          2m4s
   ```

   وضعیت Deployment را مشاهده کنید:

   ```shell
   kubectl get deployment
   ```

   خروجی نشان می‌دهد که Deployment ایجاد شده است:

   ```
   NAME    READY   UP-TO-DATE   AVAILABLE   AGE
   mongo   1/1     1            1           2m21s
   ```

   هر Deployment به‌طور خودکار یک ReplicaSet را مدیریت می‌کند.
   وضعیت ReplicaSet را با فرمان زیر مشاهده کنید:

   ```shell
   kubectl get replicaset
   ```

   خروجی نشان می‌دهد که ReplicaSet ایجاد شده است:

   ```
   NAME               DESIRED   CURRENT   READY   AGE
   mongo-75f59d57f4   1         1         1       3m12s
   ```

2. یک Service ایجاد کنید تا MongoDB را در شبکه در دسترس قرار دهد:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-service.yaml
   ```

   خروجی یک فرمان موفق تأیید می‌کند که Service ایجاد شده است:

   ```
   service/mongo created
   ```

   Service ایجادشده را بررسی کنید:

   ```shell
   kubectl get service mongo
   ```

   خروجی، Service ایجادشده را نمایش می‌دهد:

   ```
   NAME    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)     AGE
   mongo   ClusterIP   10.96.41.183   <none>        27017/TCP   11s
   ```

3. بررسی کنید که سرور MongoDB در Pod در حال اجرا است و روی پورت 27017 گوش می‌دهد:

   ```shell
   # Change mongo-75f59d57f4-4nd6q to the name of the Pod
   kubectl get pod mongo-75f59d57f4-4nd6q --template='{{(index (index .spec.containers 0).ports 0).containerPort}}{{"\n"}}'
   ```

   خروجی، پورت MongoDB را در آن Pod نمایش می‌دهد:

   ```
   27017
   ```

   پورت 27017 پورت رسمی TCP برای MongoDB است.

## هدایت یک پورت محلی به پورتی روی Pod

1. فرمان `kubectl port-forward` امکان می‌دهد با استفاده از نام منبع، مانند نام یک پاد، پاد منطبق را برای هدایت پورت (port forward) انتخاب کنید.


   ```shell
   # Change mongo-75f59d57f4-4nd6q to the name of the Pod
   kubectl port-forward mongo-75f59d57f4-4nd6q 28015:27017
   ```

   که معادل است با

   ```shell
   kubectl port-forward pods/mongo-75f59d57f4-4nd6q 28015:27017
   ```

   یا

   ```shell
   kubectl port-forward deployment/mongo 28015:27017
   ```

   یا

   ```shell
   kubectl port-forward replicaset/mongo-75f59d57f4 28015:27017
   ```

   یا

   ```shell
   kubectl port-forward service/mongo 28015:27017
   ```

   هر یک از فرمان‌های بالا کار می‌کند. خروجی مشابه زیر است:

   ```
   Forwarding from 127.0.0.1:28015 -> 27017
   Forwarding from [::1]:28015 -> 27017
   ```

   {{< note >}}
   فرمان `kubectl port-forward` به خط فرمان بازنمی‌گردد. برای ادامهٔ تمرین‌ها باید ترمینال دیگری باز کنید.
   {{< /note >}}

2. رابط خط فرمان MongoDB را اجرا کنید:

   ```shell
   mongosh --port 28015
   ```

3. در اعلان خط فرمان MongoDB، فرمان `ping` را وارد کنید:

   ```
   db.runCommand( { ping: 1 } )
   ```

   یک درخواست ping موفق، این خروجی را برمی‌گرداند:

   ```
   { ok: 1 }
   ```

### انتخاب اختیاری پورت محلی توسط _kubectl_ {#let-kubectl-choose-local-port}

اگر به پورت محلی خاصی نیاز ندارید، می‌توانید با نحوی کمی ساده‌تر، انتخاب و
تخصیص پورت محلی را به `kubectl` بسپارید و به این ترتیب از مدیریت تداخل پورت‌های
محلی خلاص شوید:

```shell
kubectl port-forward deployment/mongo :27017
```

ابزار `kubectl` یک شمارهٔ پورت محلی آزاد پیدا می‌کند (و از شماره‌پورت‌های پایین
پرهیز می‌کند، زیرا ممکن است برنامه‌های دیگر از آن‌ها استفاده کنند). خروجی مشابه زیر است:

```
Forwarding from 127.0.0.1:63753 -> 27017
Forwarding from [::1]:63753 -> 27017
```

<!-- discussion -->

## بحث

اتصال‌هایی که به پورت محلی 28015 برقرار می‌شوند، به پورت 27017 پادی هدایت
می‌شوند که سرور MongoDB را اجرا می‌کند. با برقراری این اتصال، می‌توانید از
ایستگاه کاری محلی خود برای اشکال‌زدایی پایگاه داده‌ای که در Pod اجرا می‌شود استفاده کنید.

{{< note >}}
فرمان `kubectl port-forward` فقط برای پورت‌های TCP پیاده‌سازی شده است.
پشتیبانی از پروتکل UDP در
[issue 47862](https://github.com/kubernetes/kubernetes/issues/47862) پیگیری می‌شود.
{{< /note >}}

## ملاحظات مجوزدهی و امنیت

دسترسی به `kubectl port-forward` با سازوکارهای مجوزدهی کوبرنتیز مانند {{< glossary_tooltip text="کنترل دسترسی مبتنی بر نقش (RBAC)" term_id="rbac" >}} کنترل می‌شود. مجوزدهی را سرور API کوبرنتیز اعمال می‌کند، نه کلاینت `kubectl`.

برای استفاده از `kubectl port-forward`، کاربر باید مجوز دسترسی به منبع هدف (برای مثال یک Pod یا Service) و زیرمنبع `portforward` را داشته باشد. مجوزهای لازم معمولاً شامل `get` روی `pods` و `create` روی `pods/portforward` است.

مدیران کلاستر باید این مجوزها را با دقت محدود کنند، زیرا هدایت پورت می‌تواند دسترسی مستقیم شبکه‌ای به بارهای کاری فراهم کند و ممکن است کنترل‌های سطح شبکه را دور بزند.

## {{% heading "whatsnext" %}}

دربارهٔ [kubectl port-forward](/docs/reference/generated/kubectl/kubectl-commands/#port-forward) بیشتر بیاموزید.
