---
title: اتصال فرانت‌اند به بک‌اند با استفاده از Serviceها
content_type: tutorial
weight: 70
---

<!-- overview -->

این تمرین نشان می‌دهد که چگونه یک میکروسرویس _فرانت‌اند_ (frontend) و یک میکروسرویس _بک‌اند_ (backend) بسازید. میکروسرویس بک‌اند یک سرویس ساده‌ی خوشامدگو (hello greeter) است. فرانت‌اند با استفاده از nginx و یک آبجکت {{< glossary_tooltip term_id="service" >}} کوبرنتیز، بک‌اند را در دسترس قرار می‌دهد.

## {{% heading "objectives" %}}

* یک میکروسرویس بک‌اند نمونه به نام `hello` را با استفاده از یک آبجکت
  {{< glossary_tooltip term_id="deployment" >}} ایجاد و اجرا کنید.
* از یک آبجکت Service برای ارسال ترافیک به رپلیکاهای متعدد میکروسرویس بک‌اند استفاده کنید.
* یک میکروسرویس فرانت‌اند `nginx` را، باز هم با استفاده از یک آبجکت Deployment، ایجاد و اجرا کنید.
* میکروسرویس فرانت‌اند را طوری پیکربندی کنید که ترافیک را به میکروسرویس بک‌اند بفرستد.
* با استفاده از یک آبجکت Service از نوع `type=LoadBalancer`، میکروسرویس فرانت‌اند را
  در خارج از کلاستر در دسترس قرار دهید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

در این تمرین از
[Serviceهایی با متعادل‌کننده‌ی بار خارجی](/docs/tasks/access-application-cluster/create-external-load-balancer/) استفاده می‌شود
که به محیطی نیاز دارند که از آن‌ها پشتیبانی کند. اگر محیط شما از این قابلیت پشتیبانی نمی‌کند، می‌توانید به‌جای آن از یک Service از نوع
[NodePort](/docs/concepts/services-networking/service/#type-nodeport) استفاده کنید.

<!-- lessoncontent -->

## ایجاد بک‌اند با استفاده از یک Deployment

بک‌اند یک میکروسرویس خوشامدگوی ساده است. فایل پیکربندی Deployment بک‌اند
به این صورت است:

{{% code_sample file="service/access/backend-deployment.yaml" %}}

Deployment بک‌اند را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/service/access/backend-deployment.yaml
```

اطلاعات مربوط به Deployment بک‌اند را مشاهده کنید:

```shell
kubectl describe deployment backend
```

خروجی مشابه زیر است:

```
Name:                           backend
Namespace:                      default
CreationTimestamp:              Mon, 24 Oct 2016 14:21:02 -0700
Labels:                         app=hello
                                tier=backend
                                track=stable
Annotations:                    deployment.kubernetes.io/revision=1
Selector:                       app=hello,tier=backend,track=stable
Replicas:                       3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:                   RollingUpdate
MinReadySeconds:                0
RollingUpdateStrategy:          1 max unavailable, 1 max surge
Pod Template:
  Labels:       app=hello
                tier=backend
                track=stable
  Containers:
   hello:
    Image:              "gcr.io/google-samples/hello-go-gke:1.0"
    Port:               80/TCP
    Environment:        <none>
    Mounts:             <none>
  Volumes:              <none>
Conditions:
  Type          Status  Reason
  ----          ------  ------
  Available     True    MinimumReplicasAvailable
  Progressing   True    NewReplicaSetAvailable
OldReplicaSets:                 <none>
NewReplicaSet:                  hello-3621623197 (3/3 replicas created)
Events:
...
```

## ایجاد آبجکت Service با نام `hello`

کلید ارسال درخواست از فرانت‌اند به بک‌اند، Service بک‌اند است. هر Service
یک نشانی IP و یک رکورد نام DNS پایدار ایجاد می‌کند تا میکروسرویس بک‌اند
همیشه در دسترس باشد. هر Service با استفاده از
{{< glossary_tooltip text="انتخابگرها" term_id="selector" >}}، Podهایی را
پیدا می‌کند که ترافیک را به آن‌ها هدایت می‌کند.

ابتدا فایل پیکربندی Service را بررسی کنید:

{{% code_sample file="service/access/backend-service.yaml" %}}

در فایل پیکربندی می‌بینید که Service با نام `hello` ترافیک را به Podهایی
هدایت می‌کند که برچسب‌های `app: hello` و `tier: backend` را دارند.

Service بک‌اند را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/service/access/backend-service.yaml
```

در این مرحله، یک Deployment به نام `backend` دارید که سه رپلیکا از برنامه‌ی `hello`
را اجرا می‌کند، و یک Service دارید که می‌تواند ترافیک را به آن‌ها هدایت کند. با این حال،
این سرویس نه از خارج از کلاستر در دسترس است و نه نام آن در خارج از کلاستر قابل تفکیک (resolve) است.

## ایجاد فرانت‌اند

اکنون که بک‌اند در حال اجراست، می‌توانید فرانت‌اندی بسازید که از خارج از کلاستر
در دسترس باشد و با پراکسی کردن درخواست‌ها به بک‌اند، به آن متصل شود.

فرانت‌اند با استفاده از نام DNS اختصاص‌داده‌شده به Service بک‌اند، درخواست‌ها را
به Podهای کارگر بک‌اند می‌فرستد. این نام DNS برابر با `hello` است که مقدار
فیلد `name` در فایل پیکربندی `examples/service/access/backend-service.yaml` است.

Podهای موجود در Deployment فرانت‌اند، یک ایمیج nginx را اجرا می‌کنند که طوری پیکربندی شده
است که درخواست‌ها را به Service بک‌اند `hello` پراکسی کند. فایل پیکربندی nginx به این صورت است:

{{% code_sample file="service/access/frontend-nginx.conf" %}}

فرانت‌اند نیز مانند بک‌اند، یک Deployment و یک Service دارد. تفاوت مهمی که
میان سرویس‌های بک‌اند و فرانت‌اند باید به آن توجه کرد این است که پیکربندی
Service فرانت‌اند شامل `type: LoadBalancer` است؛ یعنی این Service از متعادل‌کننده‌ی باری
استفاده می‌کند که ارائه‌دهنده‌ی ابری شما فراهم کرده است و از خارج از کلاستر در دسترس خواهد بود.

{{% code_sample file="service/access/frontend-service.yaml" %}}

{{% code_sample file="service/access/frontend-deployment.yaml" %}}

Deployment و Service فرانت‌اند را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/service/access/frontend-deployment.yaml
kubectl apply -f https://k8s.io/examples/service/access/frontend-service.yaml
```

خروجی تأیید می‌کند که هر دو منبع ایجاد شده‌اند:

```
deployment.apps/frontend created
service/frontend created
```

{{< note >}}
پیکربندی nginx درون [ایمیج کانتینر](/examples/service/access/Dockerfile) قرار داده شده است.
روش بهتر برای این کار، استفاده از یک
[ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) است
تا بتوانید پیکربندی را آسان‌تر تغییر دهید.
{{< /note >}}

## تعامل با Service فرانت‌اند

پس از ایجاد یک Service از نوع LoadBalancer، می‌توانید با این دستور
نشانی IP خارجی را پیدا کنید:

```shell
kubectl get service frontend --watch
```

این دستور پیکربندی Service با نام `frontend` را نمایش می‌دهد و تغییرات آن را
زیر نظر می‌گیرد. در ابتدا، نشانی IP خارجی به‌صورت `<pending>` نمایش داده می‌شود:

```
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)  AGE
frontend   LoadBalancer   10.51.252.116   <pending>     80/TCP   10s
```

اما به‌محض اینکه یک نشانی IP خارجی فراهم شود، پیکربندی به‌روزرسانی می‌شود
و نشانی IP جدید را زیر سرعنوان `EXTERNAL-IP` نشان می‌دهد:

```
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP        PORT(S)  AGE
frontend   LoadBalancer   10.51.252.116   XXX.XXX.XXX.XXX    80/TCP   1m
```

اکنون می‌توان از این نشانی IP برای تعامل با سرویس `frontend` از خارج از
کلاستر استفاده کرد.

## ارسال ترافیک از طریق فرانت‌اند

اکنون فرانت‌اند و بک‌اند به هم متصل شده‌اند. می‌توانید با اجرای دستور curl روی
نشانی IP خارجی Service فرانت‌اند، به این نقطه‌ی پایانی (endpoint) درخواست بفرستید.

```shell
curl http://${EXTERNAL_IP} # replace this with the EXTERNAL-IP you saw earlier
```

خروجی، پیامی را نشان می‌دهد که بک‌اند تولید کرده است:

```json
{"message":"Hello"}
```

## {{% heading "cleanup" %}}

برای حذف Serviceها، این دستور را وارد کنید:

```shell
kubectl delete services frontend backend
```

برای حذف Deploymentها، ReplicaSetها و Podهایی که برنامه‌های بک‌اند و فرانت‌اند را اجرا می‌کنند، این دستور را وارد کنید:

```shell
kubectl delete deployment frontend backend
```

## {{% heading "whatsnext" %}}

* درباره‌ی [Serviceها](/docs/concepts/services-networking/service/) بیشتر بیاموزید.
* درباره‌ی [ConfigMapها](/docs/tasks/configure-pod-container/configure-pod-configmap/) بیشتر بیاموزید.
* درباره‌ی [DNS برای Service و Podها](/docs/concepts/services-networking/dns-pod-service/) بیشتر بیاموزید.
