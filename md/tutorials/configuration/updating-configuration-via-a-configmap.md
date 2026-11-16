---
title: به‌روزرسانی پیکربندی با استفاده از ConfigMap
content_type: tutorial
weight: 20
---

<!-- overview -->
این صفحه نمونه‌ای گام‌به‌گام از به‌روزرسانی پیکربندی درون یک Pod با استفاده از ConfigMap ارائه می‌دهد
و بر پایهٔ وظیفهٔ [پیکربندی Pod برای استفاده از ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) نوشته شده است.  
در پایان این آموزش، خواهید دانست که چگونه پیکربندی یک برنامهٔ در حال اجرا را تغییر دهید.  
در این آموزش از ایمیج‌های `alpine` و `nginx` به‌عنوان نمونه استفاده می‌شود.

## {{% heading "prerequisites" %}}
{{< include "task-tutorial-prereqs.md" >}}

برای ارسال درخواست‌های HTTP از ترمینال یا خط فرمان، به ابزار خط فرمان [curl](https://curl.se/) نیاز دارید.
اگر `curl` در دسترس ندارید، می‌توانید آن را نصب کنید. برای این کار، مستندات سیستم‌عامل محلی خود را بررسی کنید.

## {{% heading "objectives" %}}
* به‌روزرسانی پیکربندی با استفاده از ConfigMap که به‌صورت حجم (Volume) mount شده است
* به‌روزرسانی متغیرهای محیطی یک Pod با استفاده از ConfigMap
* به‌روزرسانی پیکربندی با استفاده از ConfigMap در یک Pod چندکانتینری
* به‌روزرسانی پیکربندی با استفاده از ConfigMap در Podای که کانتینر کناری (Sidecar Container) دارد

<!-- lessoncontent -->

## به‌روزرسانی پیکربندی با استفاده از ConfigMap که به‌صورت حجم mount شده است {#rollout-configmap-volume}

با دستور `kubectl create configmap` یک ConfigMap از
[مقادیر صریح (literal)](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values) بسازید:

```shell
kubectl create configmap sport --from-literal=sport=football
```

در ادامه نمونه‌ای از مانیفست یک Deployment آمده است که در آن ConfigMap با نام `sport` به‌صورت یک
{{< glossary_tooltip text="حجم" term_id="volume" >}} در تنها کانتینر Pod، mount شده است.
{{% code_sample file="deployments/deployment-with-configmap-as-volume.yaml" %}}

Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-volume.yaml
```

Podهای این Deployment را بررسی کنید تا از آماده بودن آن‌ها مطمئن شوید (تطبیق بر اساس
{{< glossary_tooltip text="انتخابگر" term_id="selector" >}}):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-volume
```

باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                READY   STATUS    RESTARTS   AGE
configmap-volume-6b976dfdcf-qxvbm   1/1     Running   0          72s
configmap-volume-6b976dfdcf-skpvm   1/1     Running   0          72s
configmap-volume-6b976dfdcf-tbc6r   1/1     Running   0          72s
```

روی هر نودی که یکی از این Podها در آن اجرا می‌شود، kubelet داده‌های آن ConfigMap را دریافت می‌کند
و آن‌ها را به فایل‌هایی در یک حجم محلی تبدیل می‌کند.
سپس kubelet آن حجم را، همان‌طور که در الگوی Pod مشخص شده است، در کانتینر mount می‌کند.
کدی که در آن کانتینر اجرا می‌شود اطلاعات را از فایل بارگذاری می‌کند
و با استفاده از آن گزارشی در stdout چاپ می‌کند.
برای بررسی این گزارش، لاگ‌های یکی از Podهای آن Deployment را مشاهده کنید:

```shell
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployments/configmap-volume
```

باید خروجی‌ای مشابه زیر ببینید:

```
Found 3 pods, using pod/configmap-volume-76d9c5678f-x5rgj
Thu Jan  4 14:06:46 UTC 2024 My preferred sport is football
Thu Jan  4 14:06:56 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:06 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:16 UTC 2024 My preferred sport is football
Thu Jan  4 14:07:26 UTC 2024 My preferred sport is football
```

ConfigMap را ویرایش کنید:

```shell
kubectl edit configmap sport
```

در ویرایشگری که باز می‌شود، مقدار کلید `sport` را از `football` به `cricket` تغییر دهید و تغییرات را ذخیره کنید.
ابزار kubectl نیز ConfigMap را متناسب با آن به‌روزرسانی می‌کند (اگر با خطا روبه‌رو شدید، دوباره تلاش کنید).

در ادامه نمونه‌ای از شکل احتمالی آن مانیفست پس از ویرایش آمده است:

```yaml
apiVersion: v1
data:
  sport: cricket
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-04T14:05:06Z"
  name: sport
  namespace: default
  resourceVersion: "1743935"
  uid: 024ee001-fe72-487e-872e-34d6464a8a23
```

باید خروجی زیر را ببینید:

```
configmap/sport edited
```

لاگ‌های یکی از Podهای متعلق به این Deployment را به‌صورت پیوسته دنبال کنید (یعنی جدیدترین ورودی‌ها را دنبال کنید):

```shell
kubectl logs deployments/configmap-volume --follow
```

پس از چند ثانیه، باید ببینید که خروجی لاگ به شکل زیر تغییر می‌کند:

```
Thu Jan  4 14:11:36 UTC 2024 My preferred sport is football
Thu Jan  4 14:11:46 UTC 2024 My preferred sport is football
Thu Jan  4 14:11:56 UTC 2024 My preferred sport is football
Thu Jan  4 14:12:06 UTC 2024 My preferred sport is cricket
Thu Jan  4 14:12:16 UTC 2024 My preferred sport is cricket
```

هنگامی که یک ConfigMap از طریق حجمی از نوع `configMap` یا `projected` به یک Pod در حال اجرا نگاشت شده باشد
و آن ConfigMap را به‌روزرسانی کنید، Pod در حال اجرا تقریباً بلافاصله این به‌روزرسانی را می‌بیند.  
با این حال، برنامهٔ شما تنها در صورتی متوجه این تغییر می‌شود که طوری نوشته شده باشد که تغییرات را به‌صورت دوره‌ای
بررسی کند (poll) یا به‌روزرسانی فایل‌ها را زیر نظر داشته باشد (watch).  
برنامه‌ای که پیکربندی خود را فقط یک بار و هنگام راه‌اندازی بارگذاری می‌کند، متوجه تغییر نخواهد شد.

{{< alert color="info" title="Note" >}}
کل تأخیر از لحظهٔ به‌روزرسانی ConfigMap تا لحظه‌ای که کلیدهای جدید در Pod بازتاب داده می‌شوند،
ممکن است به اندازهٔ دورهٔ همگام‌سازی kubelet طول بکشد.  
همچنین بخش [ConfigMapهای mountشده به‌طور خودکار به‌روزرسانی می‌شوند](/docs/tasks/configure-pod-container/configure-pod-configmap/#mounted-configmaps-are-updated-automatically) را ببینید.
{{< /alert >}}

## به‌روزرسانی متغیرهای محیطی یک Pod با استفاده از ConfigMap {#rollout-configmap-env}

با دستور `kubectl create configmap` یک ConfigMap از
[مقادیر صریح](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values) بسازید:

```shell
kubectl create configmap fruits --from-literal=fruits=apples
```

در ادامه نمونه‌ای از مانیفست یک Deployment آمده است که در آن یک متغیر محیطی از طریق ConfigMap با نام `fruits` پیکربندی شده است.

{{% code_sample file="deployments/deployment-with-configmap-as-envvar.yaml" %}}

Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-as-envvar.yaml
```

Podهای این Deployment را بررسی کنید تا از آماده بودن آن‌ها مطمئن شوید (تطبیق بر اساس
{{< glossary_tooltip text="انتخابگر" term_id="selector" >}}):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-env-var
```

باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                 READY   STATUS    RESTARTS   AGE
configmap-env-var-59cfc64f7d-74d7z   1/1     Running   0          46s
configmap-env-var-59cfc64f7d-c4wmj   1/1     Running   0          46s
configmap-env-var-59cfc64f7d-dpr98   1/1     Running   0          46s
```

جفت کلید-مقدار موجود در ConfigMap به‌صورت یک متغیر محیطی در کانتینر Pod پیکربندی شده است.
برای بررسی این موضوع، لاگ‌های یکی از Podهای متعلق به Deployment را مشاهده کنید.

```shell
kubectl logs deployment/configmap-env-var
```

باید خروجی‌ای مشابه زیر ببینید:

```
Found 3 pods, using pod/configmap-env-var-7c994f7769-l74nq
Thu Jan  4 16:07:06 UTC 2024 The basket is full of apples
Thu Jan  4 16:07:16 UTC 2024 The basket is full of apples
Thu Jan  4 16:07:26 UTC 2024 The basket is full of apples
```

ConfigMap را ویرایش کنید:

```shell
kubectl edit configmap fruits
```

در ویرایشگری که باز می‌شود، مقدار کلید `fruits` را از `apples` به `mangoes` تغییر دهید و تغییرات را ذخیره کنید.
ابزار kubectl نیز ConfigMap را متناسب با آن به‌روزرسانی می‌کند (اگر با خطا روبه‌رو شدید، دوباره تلاش کنید).

در ادامه نمونه‌ای از شکل احتمالی آن مانیفست پس از ویرایش آمده است:

```yaml
apiVersion: v1
data:
  fruits: mangoes
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-04T16:04:19Z"
  name: fruits
  namespace: default
  resourceVersion: "1749472"
```

باید خروجی زیر را ببینید:

```
configmap/fruits edited
```

لاگ‌های Deployment را به‌صورت پیوسته دنبال کنید و خروجی را چند ثانیه زیر نظر بگیرید:

```shell
# As the text explains, the output does NOT change
kubectl logs deployments/configmap-env-var --follow
```

توجه کنید که با وجود ویرایش ConfigMap، خروجی **بدون تغییر** باقی می‌ماند:

```
Thu Jan  4 16:12:56 UTC 2024 The basket is full of apples
Thu Jan  4 16:13:06 UTC 2024 The basket is full of apples
Thu Jan  4 16:13:16 UTC 2024 The basket is full of apples
Thu Jan  4 16:13:26 UTC 2024 The basket is full of apples
```

{{< alert color="info" title="Note" >}}
هرچند مقدار کلید درون ConfigMap تغییر کرده است، متغیر محیطی در Pod همچنان مقدار قبلی را نشان می‌دهد.
دلیل این است که متغیرهای محیطی فرایندی که درون یک Pod اجرا می‌شود، با تغییر دادهٔ منبع به‌روزرسانی **نمی‌شوند**.
اگر بخواهید به‌روزرسانی را اجباری کنید، باید کاری کنید که کوبرنتیز Podهای موجود شما را جایگزین کند.
در این صورت، Podهای جدید با اطلاعات به‌روزشده اجرا خواهند شد.
{{< /alert >}}

می‌توانید این جایگزینی را آغاز کنید. برای این کار، با استفاده از
[`kubectl rollout`](/docs/reference/kubectl/generated/kubectl_rollout/) یک عرضهٔ تدریجی (rollout) برای Deployment انجام دهید:

```shell
# Trigger the rollout
kubectl rollout restart deployment configmap-env-var

# Wait for the rollout to complete
kubectl rollout status deployment configmap-env-var --watch=true
```

سپس Deployment را بررسی کنید:

```shell
kubectl get deployment configmap-env-var
```

باید خروجی‌ای مشابه زیر ببینید:

```
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
configmap-env-var   3/3     3            3           12m
```

Podها را بررسی کنید:

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-env-var
```

عرضهٔ تدریجی باعث می‌شود کوبرنتیز یک {{< glossary_tooltip term_id="replica-set" text="ReplicaSet" >}}
جدید برای Deployment بسازد؛ یعنی Podهای موجود در نهایت خاتمه می‌یابند و Podهای جدید ایجاد می‌شوند.
پس از چند ثانیه، باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                 READY   STATUS        RESTARTS   AGE
configmap-env-var-6d94d89bf5-2ph2l   1/1     Running       0          13s
configmap-env-var-6d94d89bf5-74twx   1/1     Running       0          8s
configmap-env-var-6d94d89bf5-d5vx8   1/1     Running       0          11s
```

{{< alert color="info" title="Note" >}}
لطفاً پیش از ادامهٔ گام‌های بعدی، صبر کنید تا Podهای قدیمی‌تر به‌طور کامل خاتمه یابند.
{{< /alert >}}

لاگ‌های یکی از Podهای این Deployment را مشاهده کنید:

```shell
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployment/configmap-env-var
```

باید خروجی‌ای مشابه زیر ببینید:

```
Found 3 pods, using pod/configmap-env-var-6d9ff89fb6-bzcf6
Thu Jan  4 16:30:35 UTC 2024 The basket is full of mangoes
Thu Jan  4 16:30:45 UTC 2024 The basket is full of mangoes
Thu Jan  4 16:30:55 UTC 2024 The basket is full of mangoes
```

این مثال سناریوی به‌روزرسانی متغیرهای محیطی‌ای را در یک Pod نشان می‌دهد که از یک ConfigMap گرفته شده‌اند.
تغییرات مقادیر ConfigMap در عرضهٔ تدریجی بعدی روی Pod اعمال می‌شوند. اگر Podها به دلیل دیگری ایجاد شوند،
مثلاً هنگام افزایش مقیاس Deployment، Podهای جدید نیز از آخرین مقادیر پیکربندی استفاده می‌کنند؛
اما اگر عرضهٔ تدریجی را آغاز نکنید، ممکن است ببینید که برنامهٔ شما با ترکیبی از مقادیر قدیمی و جدید متغیرهای محیطی اجرا می‌شود.

## به‌روزرسانی پیکربندی با استفاده از ConfigMap در یک Pod چندکانتینری {#rollout-configmap-multiple-containers}

با دستور `kubectl create configmap` یک ConfigMap از
[مقادیر صریح](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values) بسازید:

```shell
kubectl create configmap color --from-literal=color=red
```

در ادامه نمونه‌ای از مانیفست یک Deployment آمده است که مجموعه‌ای از Podها را مدیریت می‌کند و هر Pod دو کانتینر دارد.
این دو کانتینر یک حجم از نوع `emptyDir` را به اشتراک می‌گذارند و از آن برای ارتباط با یکدیگر استفاده می‌کنند.
کانتینر اول یک وب‌سرور (`nginx`) را اجرا می‌کند. مسیر mount حجم مشترک در کانتینر وب‌سرور،
`/usr/share/nginx/html` است. کانتینر کمکی دوم بر پایهٔ `alpine` است و در این کانتینر، حجم `emptyDir`
در مسیر `/pod-data` mount می‌شود. کانتینر کمکی یک فایل HTML می‌نویسد که محتوای آن بر اساس یک ConfigMap تعیین می‌شود.
کانتینر وب‌سرور نیز این فایل HTML را از طریق HTTP ارائه می‌کند.

{{% code_sample file="deployments/deployment-with-configmap-two-containers.yaml" %}}

Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-two-containers.yaml
```

Podهای این Deployment را بررسی کنید تا از آماده بودن آن‌ها مطمئن شوید (تطبیق بر اساس
{{< glossary_tooltip text="انتخابگر" term_id="selector" >}}):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-two-containers
```

باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                        READY   STATUS    RESTARTS   AGE
configmap-two-containers-565fb6d4f4-2xhxf   2/2     Running   0          20s
configmap-two-containers-565fb6d4f4-g5v4j   2/2     Running   0          20s
configmap-two-containers-565fb6d4f4-mzsmf   2/2     Running   0          20s
```

Deployment را در دسترس قرار دهید (ابزار `kubectl` یک
{{<glossary_tooltip text="Service" term_id="service">}} برای شما ایجاد می‌کند):

```shell
kubectl expose deployment configmap-two-containers --name=configmap-service --port=8080 --target-port=80
```

با استفاده از `kubectl` پورت را هدایت (forward) کنید:

```shell
# this stays running in the background
kubectl port-forward service/configmap-service 8080:8080 &
```

به سرویس دسترسی پیدا کنید.

```shell
curl http://localhost:8080
```

باید خروجی‌ای مشابه زیر ببینید:

```
Fri Jan  5 08:08:22 UTC 2024 My preferred color is red
```

ConfigMap را ویرایش کنید:

```shell
kubectl edit configmap color
```

در ویرایشگری که باز می‌شود، مقدار کلید `color` را از `red` به `blue` تغییر دهید و تغییرات را ذخیره کنید.
ابزار kubectl نیز ConfigMap را متناسب با آن به‌روزرسانی می‌کند (اگر با خطا روبه‌رو شدید، دوباره تلاش کنید).

در ادامه نمونه‌ای از شکل احتمالی آن مانیفست پس از ویرایش آمده است:

```yaml
apiVersion: v1
data:
  color: blue
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-05T08:12:05Z"
  name: color
  namespace: configmap
  resourceVersion: "1801272"
  uid: 80d33e4a-cbb4-4bc9-ba8c-544c68e425d6
```

برای چند ثانیه، در یک حلقه به نشانی URL سرویس درخواست بفرستید.

```shell
# Cancel this when you're happy with it (Ctrl-C)
while true; do curl --connect-timeout 7.5 http://localhost:8080; sleep 10; done
```

باید ببینید که خروجی به شکل زیر تغییر می‌کند:

```
Fri Jan  5 08:14:00 UTC 2024 My preferred color is red
Fri Jan  5 08:14:02 UTC 2024 My preferred color is red
Fri Jan  5 08:14:20 UTC 2024 My preferred color is red
Fri Jan  5 08:14:22 UTC 2024 My preferred color is red
Fri Jan  5 08:14:32 UTC 2024 My preferred color is blue
Fri Jan  5 08:14:43 UTC 2024 My preferred color is blue
Fri Jan  5 08:15:00 UTC 2024 My preferred color is blue
```

## به‌روزرسانی پیکربندی از طریق ConfigMap در Podی که کانتینر جانبی دارد {#rollout-configmap-sidecar}

سناریوی بالا را می‌توان با استفاده از یک [کانتینر جانبی (Sidecar Container)](/docs/concepts/workloads/pods/sidecar-containers/)
به‌عنوان کانتینر کمکی برای نوشتن فایل HTML نیز پیاده‌سازی کرد.  
از آنجا که کانتینر جانبی از نظر مفهومی یک کانتینر آغازین (Init Container) است، تضمین می‌شود که پیش از کانتینر اصلی وب‌سرور شروع به کار کند.  
به این ترتیب، هنگامی که وب‌سرور آماده‌ی ارائه‌ی فایل HTML است، این فایل همیشه در دسترس خواهد بود.  

اگر از سناریوی قبلی ادامه می‌دهید، می‌توانید ConfigMap با نام `color` را در این سناریو نیز دوباره به کار ببرید.  
اگر این سناریو را به‌طور مستقل اجرا می‌کنید، با فرمان `kubectl create configmap` یک ConfigMap
از [مقادیر لفظی](/docs/tasks/configure-pod-container/configure-pod-configmap/#create-configmaps-from-literal-values) بسازید:

```shell
kubectl create configmap color --from-literal=color=blue
```

در ادامه، نمونه‌ای از مانیفست یک Deployment آمده است که مجموعه‌ای از Podها را مدیریت می‌کند؛ هر Pod یک کانتینر اصلی و
یک کانتینر جانبی دارد. این دو کانتینر یک حجم (volume) از نوع `emptyDir` را به اشتراک می‌گذارند و از طریق آن با یکدیگر ارتباط برقرار می‌کنند.
کانتینر اصلی یک وب‌سرور (NGINX) را اجرا می‌کند. مسیر اتصال حجم مشترک در کانتینر وب‌سرور
`/usr/share/nginx/html` است. کانتینر دوم یک کانتینر جانبی مبتنی بر Alpine Linux است که نقش
کانتینر کمکی را دارد. در این کانتینر، حجم `emptyDir` در مسیر `/pod-data` متصل می‌شود. کانتینر جانبی
یک فایل HTML می‌نویسد که محتوای آن بر اساس یک ConfigMap تعیین می‌شود. کانتینر وب‌سرور این فایل HTML را از طریق HTTP ارائه می‌دهد.

{{% code_sample file="deployments/deployment-with-configmap-and-sidecar-container.yaml" %}}

Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-and-sidecar-container.yaml
```

Podهای این Deployment را بررسی کنید تا مطمئن شوید آماده هستند (تطبیق بر اساس
{{< glossary_tooltip text="انتخابگر" term_id="selector" >}}):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-sidecar-container
```

باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                           READY   STATUS    RESTARTS   AGE
configmap-sidecar-container-5fb59f558b-87rp7   2/2     Running   0          94s
configmap-sidecar-container-5fb59f558b-ccs7s   2/2     Running   0          94s
configmap-sidecar-container-5fb59f558b-wnmgk   2/2     Running   0          94s
```

Deployment را در معرض دسترسی قرار دهید (ابزار `kubectl` یک
{{<glossary_tooltip text="Service" term_id="service">}} برای شما ایجاد می‌کند):

```shell
kubectl expose deployment configmap-sidecar-container --name=configmap-sidecar-service --port=8081 --target-port=80
```

با استفاده از `kubectl` پورت را هدایت (forward) کنید:

```shell
# this stays running in the background
kubectl port-forward service/configmap-sidecar-service 8081:8081 &
```

به سرویس دسترسی پیدا کنید.

```shell
curl http://localhost:8081
```

باید خروجی‌ای مشابه زیر ببینید:

```
Sat Feb 17 13:09:05 UTC 2024 My preferred color is blue
```

ConfigMap را ویرایش کنید:

```shell
kubectl edit configmap color
```

در ویرایشگری که باز می‌شود، مقدار کلید `color` را از `blue` به `green` تغییر دهید و تغییرات را ذخیره کنید.
ابزار kubectl نیز ConfigMap را بر همین اساس به‌روزرسانی می‌کند (اگر با خطا مواجه شدید، دوباره تلاش کنید).

نمونه‌ای از شکل این مانیفست پس از ویرایش در ادامه آمده است:

```yaml
apiVersion: v1
data:
  color: green
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-02-17T12:20:30Z"
  name: color
  namespace: default
  resourceVersion: "1054"
  uid: e40bb34c-58df-4280-8bea-6ed16edccfaa
```

چند ثانیه نشانی URL سرویس را به‌صورت حلقه‌ای فراخوانی کنید.

```shell
# Cancel this when you're happy with it (Ctrl-C)
while true; do curl --connect-timeout 7.5 http://localhost:8081; sleep 10; done
```

باید ببینید که خروجی به شکل زیر تغییر می‌کند:

```
Sat Feb 17 13:12:35 UTC 2024 My preferred color is blue
Sat Feb 17 13:12:45 UTC 2024 My preferred color is blue
Sat Feb 17 13:12:55 UTC 2024 My preferred color is blue
Sat Feb 17 13:13:05 UTC 2024 My preferred color is blue
Sat Feb 17 13:13:15 UTC 2024 My preferred color is green
Sat Feb 17 13:13:25 UTC 2024 My preferred color is green
Sat Feb 17 13:13:35 UTC 2024 My preferred color is green
```

## به‌روزرسانی پیکربندی از طریق ConfigMap تغییرناپذیری که به‌صورت حجم متصل شده است {#rollout-configmap-immutable-volume}

{{< alert color="info" title="Note" >}}
ConfigMapهای تغییرناپذیر به‌ویژه برای پیکربندی‌هایی به کار می‌روند که ثابت هستند و انتظار نمی‌رود در طول زمان تغییر **کنند**.
علامت‌گذاری یک ConfigMap به‌عنوان تغییرناپذیر باعث بهبود کارایی می‌شود، زیرا kubelet دیگر تغییرات آن را پایش نمی‌کند.

اگر واقعاً لازم است تغییری ایجاد کنید، باید یکی از این کارها را برنامه‌ریزی کنید:

- نام ConfigMap را تغییر دهید و به اجرای Podهایی روی بیاورید که به نام جدید ارجاع می‌دهند
- همه‌ی نودهایی از کلاستر را که پیش‌تر Podی با مقدار قدیمی را اجرا کرده‌اند جایگزین کنید
- kubelet را روی هر نودی که پیش‌تر ConfigMap قدیمی را بارگذاری کرده است، دوباره راه‌اندازی کنید
{{< /alert >}}

نمونه‌ای از مانیفست یک [ConfigMap تغییرناپذیر](/docs/concepts/configuration/configmap/#configmap-immutable) در ادامه نشان داده شده است.
{{% code_sample file="configmap/immutable-configmap.yaml" %}}

ConfigMap تغییرناپذیر را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/configmap/immutable-configmap.yaml
```

در ادامه، نمونه‌ای از مانیفست یک Deployment آمده است که در آن ConfigMap تغییرناپذیر `company-name-20150801` به‌صورت یک
{{< glossary_tooltip text="حجم" term_id="volume" >}} به تنها کانتینر Pod متصل شده است.

{{% code_sample file="deployments/deployment-with-immutable-configmap-as-volume.yaml" %}}

Deployment را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-immutable-configmap-as-volume.yaml
```

Podهای این Deployment را بررسی کنید تا مطمئن شوید آماده هستند (تطبیق بر اساس
{{< glossary_tooltip text="انتخابگر" term_id="selector" >}}):

```shell
kubectl get pods --selector=app.kubernetes.io/name=immutable-configmap-volume
```

باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                          READY   STATUS    RESTARTS   AGE
immutable-configmap-volume-78b6fbff95-5gsfh   1/1     Running   0          62s
immutable-configmap-volume-78b6fbff95-7vcj4   1/1     Running   0          62s
immutable-configmap-volume-78b6fbff95-vdslm   1/1     Running   0          62s
```

کانتینر Pod به داده‌های تعریف‌شده در ConfigMap ارجاع می‌دهد و از آن‌ها برای چاپ یک گزارش در stdout استفاده می‌کند.
می‌توانید با مشاهده‌ی لاگ‌های یکی از Podهای آن Deployment این گزارش را بررسی کنید:

```shell
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployments/immutable-configmap-volume
```

باید خروجی‌ای مشابه زیر ببینید:

```
Found 3 pods, using pod/immutable-configmap-volume-78b6fbff95-5gsfh
Wed Mar 20 03:52:34 UTC 2024 The name of the company is ACME, Inc.
Wed Mar 20 03:52:44 UTC 2024 The name of the company is ACME, Inc.
Wed Mar 20 03:52:54 UTC 2024 The name of the company is ACME, Inc.
```

{{< alert color="info" title="Note" >}}
هنگامی که یک ConfigMap به‌عنوان تغییرناپذیر علامت‌گذاری شود، دیگر نمی‌توان این تغییر را بازگرداند
یا محتوای فیلد data یا binaryData را تغییر داد.  
برای تغییر رفتار Podهایی که از این پیکربندی استفاده می‌کنند،
باید یک ConfigMap تغییرناپذیر جدید بسازید و Deployment را ویرایش کنید
تا الگوی Pod اندکی متفاوتی تعریف شود که به ConfigMap جدید ارجاع می‌دهد.
{{< /alert >}}

با استفاده از مانیفست زیر یک ConfigMap تغییرناپذیر جدید بسازید:

{{% code_sample file="configmap/new-immutable-configmap.yaml" %}}

```shell
kubectl apply -f https://k8s.io/examples/configmap/new-immutable-configmap.yaml
```

باید خروجی‌ای مشابه زیر ببینید:

```
configmap/company-name-20240312 created
```

ConfigMap تازه ایجادشده را بررسی کنید:

```shell
kubectl get configmap
```

باید خروجی‌ای ببینید که هر دو ConfigMap قدیمی و جدید را نشان می‌دهد:

```
NAME                    DATA   AGE
company-name-20150801   1      22m
company-name-20240312   1      24s
```

Deployment را طوری تغییر دهید که به ConfigMap جدید ارجاع دهد.

Deployment را ویرایش کنید:

```shell
kubectl edit deployment immutable-configmap-volume
```

در ویرایشگری که باز می‌شود، تعریف حجم موجود را طوری به‌روزرسانی کنید که از ConfigMap جدید استفاده کند.

```yaml
volumes:
- configMap:
    defaultMode: 420
    name: company-name-20240312 # Update this field
  name: config-volume
```

باید خروجی زیر را ببینید:

```
deployment.apps/immutable-configmap-volume edited
```

این کار یک استقرار تدریجی (rollout) را آغاز می‌کند. صبر کنید تا همه‌ی Podهای قبلی خاتمه یابند و Podهای جدید به وضعیت آماده برسند.

وضعیت Podها را پایش کنید:

```shell
kubectl get pods --selector=app.kubernetes.io/name=immutable-configmap-volume
```

```
NAME                                          READY   STATUS        RESTARTS   AGE
immutable-configmap-volume-5fdb88fcc8-29v8n   1/1     Running       0          13s
immutable-configmap-volume-5fdb88fcc8-52ddd   1/1     Running       0          14s
immutable-configmap-volume-5fdb88fcc8-n5jx4   1/1     Running       0          15s
immutable-configmap-volume-78b6fbff95-5gsfh   1/1     Terminating   0          32m
immutable-configmap-volume-78b6fbff95-7vcj4   1/1     Terminating   0          32m
immutable-configmap-volume-78b6fbff95-vdslm   1/1     Terminating   0          32m
```

در نهایت باید خروجی‌ای مشابه زیر ببینید:

```
NAME                                          READY   STATUS    RESTARTS   AGE
immutable-configmap-volume-5fdb88fcc8-29v8n   1/1     Running   0          43s
immutable-configmap-volume-5fdb88fcc8-52ddd   1/1     Running   0          44s
immutable-configmap-volume-5fdb88fcc8-n5jx4   1/1     Running   0          45s
```

لاگ‌های یکی از Podهای این Deployment را مشاهده کنید:

```shell
# Pick one Pod that belongs to the Deployment, and view its logs
kubectl logs deployment/immutable-configmap-volume
```

باید خروجی‌ای مشابه زیر ببینید:

```
Found 3 pods, using pod/immutable-configmap-volume-5fdb88fcc8-n5jx4
Wed Mar 20 04:24:17 UTC 2024 The name of the company is Fiktivesunternehmen GmbH
Wed Mar 20 04:24:27 UTC 2024 The name of the company is Fiktivesunternehmen GmbH
Wed Mar 20 04:24:37 UTC 2024 The name of the company is Fiktivesunternehmen GmbH
```

پس از آنکه همه‌ی Deploymentها به استفاده از ConfigMap تغییرناپذیر جدید منتقل شدند، توصیه می‌شود ConfigMap قدیمی را حذف کنید.

```shell
kubectl delete configmap company-name-20150801
```

## جمع‌بندی

تغییرات ConfigMapی که به‌صورت حجم به یک Pod متصل شده است، پس از همگام‌سازی بعدی kubelet بدون هیچ وقفه‌ای در دسترس قرار می‌گیرند.

تغییرات ConfigMapی که متغیرهای محیطی یک Pod را پیکربندی می‌کند، پس از استقرار تدریجی بعدی آن Pod در دسترس قرار می‌گیرند.

هنگامی که یک ConfigMap به‌عنوان تغییرناپذیر علامت‌گذاری شود، دیگر نمی‌توان این تغییر را بازگرداند
(نمی‌توانید یک ConfigMap تغییرناپذیر را تغییرپذیر کنید) و همچنین نمی‌توانید هیچ تغییری
در محتوای فیلد `data` یا `binaryData` ایجاد کنید. می‌توانید ConfigMap را حذف و دوباره ایجاد کنید
یا یک ConfigMap جدید و متفاوت بسازید. وقتی یک ConfigMap را حذف می‌کنید،
کانتینرهای در حال اجرا و Podهای آن‌ها نقطه‌ی اتصال خود را به هر حجمی که به
آن ConfigMap موجود ارجاع می‌داده است، حفظ می‌کنند.

## {{% heading "cleanup" %}}

اگر فرمان‌های `kubectl port-forward` هنوز در حال اجرا هستند، آن‌ها را متوقف کنید.

منابعی را که در طول این آموزش ایجاد شده‌اند حذف کنید:

```shell
kubectl delete deployment configmap-volume configmap-env-var configmap-two-containers configmap-sidecar-container immutable-configmap-volume
kubectl delete service configmap-service configmap-sidecar-service
kubectl delete configmap sport fruits color company-name-20240312

kubectl delete configmap company-name-20150801 # In case it was not handled during the task execution
```
