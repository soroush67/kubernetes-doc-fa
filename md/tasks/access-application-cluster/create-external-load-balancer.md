---
title: ایجاد یک متعادل‌کنندهٔ بار خارجی
content_type: task
weight: 80
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک متعادل‌کنندهٔ بار (load balancer) خارجی ایجاد کنید.

هنگام ایجاد یک {{< glossary_tooltip text="Service" term_id="service" >}}، می‌توانید به‌طور خودکار یک متعادل‌کنندهٔ بار ابری نیز ایجاد کنید. این متعادل‌کننده یک نشانی IP در دسترس از بیرون فراهم می‌کند که ترافیک را به پورت درست روی نودهای کلاستر شما می‌فرستد، _به شرط آنکه کلاستر شما در محیطی پشتیبانی‌شده اجرا شود و با بستهٔ ارائه‌دهندهٔ متعادل‌کنندهٔ بار ابری مناسب پیکربندی شده باشد_.

همچنین می‌توانید به‌جای Service از یک {{< glossary_tooltip term_id="ingress" >}} استفاده کنید. برای اطلاعات بیشتر، مستندات [Ingress](/docs/concepts/services-networking/ingress/) را ببینید.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

کلاستر شما باید در یک محیط ابری یا محیط دیگری اجرا شود که از پیش، پیکربندی متعادل‌کننده‌های بار خارجی را پشتیبانی می‌کند.


<!-- steps -->

## ایجاد یک Service

### ایجاد یک Service از روی مانیفست

برای ایجاد یک متعادل‌کنندهٔ بار خارجی، خط زیر را به مانیفست Service خود اضافه کنید:

```yaml
    type: LoadBalancer
```

در این صورت مانیفست شما ممکن است چنین باشد:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  type: LoadBalancer
```

### ایجاد یک Service با استفاده از kubectl

همچنین می‌توانید این سرویس را با فرمان `kubectl expose` و فلگ `--type=LoadBalancer` آن ایجاد کنید:

```bash
kubectl expose deployment example --port=8765 --target-port=9376 \
        --name=example-service --type=LoadBalancer
```

این فرمان یک Service جدید ایجاد می‌کند که از همان انتخابگرهای (selector) منبع ارجاع‌شده استفاده می‌کند (در مثال بالا، یک {{< glossary_tooltip text="Deployment" term_id="deployment" >}} با نام `example`).

برای اطلاعات بیشتر، از جمله فلگ‌های اختیاری، به [مرجع `kubectl expose`](/docs/reference/generated/kubectl/kubectl-commands/#expose) مراجعه کنید.

## یافتن نشانی IP

برای یافتن نشانی IP ایجادشده برای سرویس خود، می‌توانید اطلاعات سرویس را از طریق `kubectl` دریافت کنید:

```bash
kubectl describe services example-service
```

خروجی این فرمان باید مشابه زیر باشد:

```
Name:                     example-service
Namespace:                default
Labels:                   app=example
Annotations:              <none>
Selector:                 app=example
Type:                     LoadBalancer
IP Families:              <none>
IP:                       10.3.22.96
IPs:                      10.3.22.96
LoadBalancer Ingress:     192.0.2.89
Port:                     <unset>  8765/TCP
TargetPort:               9376/TCP
NodePort:                 <unset>  30593/TCP
Endpoints:                172.17.0.3:9376
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

نشانی IP متعادل‌کنندهٔ بار در کنار `LoadBalancer Ingress` آمده است.

{{< note >}}
اگر سرویس خود را روی Minikube اجرا می‌کنید، می‌توانید نشانی IP و پورت اختصاص‌یافته را با فرمان زیر پیدا کنید:

```bash
minikube service example-service --url
```
{{< /note >}}

## حفظ IP مبدأ کلاینت

به‌طور پیش‌فرض، IP مبدئی که کانتینر مقصد می‌بیند *IP مبدأ اصلی کلاینت نیست*. برای فعال‌کردن حفظ IP کلاینت، می‌توان فیلدهای زیر را در `.spec` سرویس پیکربندی کرد:

* `.spec.externalTrafficPolicy` - مشخص می‌کند که این Service می‌خواهد ترافیک خارجی را به endpointهای محلیِ نود هدایت کند یا به endpointهای سراسری کلاستر. دو گزینه در دسترس است: `Cluster` (پیش‌فرض) و `Local`. گزینهٔ `Cluster` نشانی IP مبدأ کلاینت را پنهان می‌کند و ممکن است باعث یک پرش (hop) دوم به نود دیگری شود، اما در مجموع توزیع بار خوبی دارد. گزینهٔ `Local` نشانی IP مبدأ کلاینت را حفظ می‌کند و در Serviceهای از نوع LoadBalancer و NodePort از پرش دوم جلوگیری می‌کند، اما خطر توزیع نامتوازن ترافیک را به همراه دارد.
* `.spec.healthCheckNodePort` - پورت نودِ بررسی سلامت (شمارهٔ عددی پورت) را برای سرویس مشخص می‌کند. اگر `healthCheckNodePort` را مشخص نکنید، کنترل‌کنندهٔ سرویس یک پورت از بازهٔ NodePort کلاستر شما اختصاص می‌دهد.  
  این بازه را می‌توانید با تنظیم گزینهٔ خط فرمان API server یعنی `--service-node-port-range` پیکربندی کنید. اگر مقدار `healthCheckNodePort` را خودتان مشخص کنید، Service از همین مقدار استفاده می‌کند، به شرط آنکه `type` سرویس روی LoadBalancer و `externalTrafficPolicy` روی `Local` تنظیم شده باشد.

با تنظیم `externalTrafficPolicy` روی Local در مانیفست Service، این قابلیت فعال می‌شود. برای مثال:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
spec:
  selector:
    app: example
  ports:
    - port: 8765
      targetPort: 9376
  externalTrafficPolicy: Local
  type: LoadBalancer
```

### هشدارها و محدودیت‌های حفظ IPهای مبدأ

سرویس‌های متعادل‌سازی بار برخی از ارائه‌دهندگان ابری اجازه نمی‌دهند برای هر مقصد وزن متفاوتی پیکربندی کنید.

وقتی همهٔ مقصدها از نظر ارسال ترافیک به نودها وزن یکسانی داشته باشند، ترافیک خارجی به‌طور مساوی میان Podهای مختلف توزیع نمی‌شود. متعادل‌کنندهٔ بار خارجی از تعداد Podهایی که روی هر نود به‌عنوان مقصد استفاده می‌شوند آگاه نیست.

در حالتی که `NumServicePods <<  NumNodes` یا `NumServicePods >> NumNodes` باشد، حتی بدون وزن‌دهی نیز توزیعی تقریباً نزدیک به برابر مشاهده می‌شود.

ترافیک داخلی میان Podها باید رفتاری مشابه سرویس‌های ClusterIP داشته باشد و با احتمال برابر میان همهٔ Podها توزیع شود.

## جمع‌آوری زباله برای متعادل‌کننده‌های بار

{{< feature-state for_k8s_version="v1.17" state="stable" >}}

در حالت عادی، منابع متعادل‌کنندهٔ بار مرتبط در ارائه‌دهندهٔ ابری باید کمی پس از حذف یک Service از نوع LoadBalancer پاک‌سازی شوند. اما مشخص شده است که در موارد حاشیه‌ای گوناگون، منابع ابری پس از حذف Service مرتبط، بی‌صاحب (orphaned) باقی می‌مانند. سازوکار محافظت با Finalizer برای LoadBalancerهای Service برای جلوگیری از این مشکل معرفی شد. با استفاده از finalizerها، یک منبع Service تا زمانی که منابع متعادل‌کنندهٔ بار مرتبط با آن نیز حذف نشده باشند، هرگز حذف نمی‌شود.

به‌طور مشخص، اگر `type` یک Service برابر LoadBalancer باشد، کنترل‌کنندهٔ سرویس یک finalizer با نام `service.kubernetes.io/load-balancer-cleanup` به آن متصل می‌کند. این finalizer تنها پس از پاک‌سازی منبع متعادل‌کنندهٔ بار حذف می‌شود. این کار حتی در موارد حاشیه‌ای، مانند از کار افتادن کنترل‌کنندهٔ سرویس، از باقی‌ماندن منابع رهاشدهٔ متعادل‌کنندهٔ بار جلوگیری می‌کند.

## ارائه‌دهندگان متعادل‌کنندهٔ بار خارجی

توجه به این نکته اهمیت دارد که مسیر داده (datapath) برای این قابلیت را یک متعادل‌کنندهٔ بار خارج از کلاستر کوبرنتیز فراهم می‌کند.

وقتی `type` یک Service روی LoadBalancer تنظیم شود، کوبرنتیز برای Podهای درون کلاستر قابلیتی معادل حالتی فراهم می‌کند که `type` برابر ClusterIP باشد، و آن را با برنامه‌ریزی متعادل‌کنندهٔ بار (خارج از کوبرنتیز) گسترش می‌دهد؛ به این صورت که مدخل‌هایی برای نودهای میزبان Podهای مرتبط کوبرنتیز به آن اضافه می‌کند. control plane کوبرنتیز ایجاد متعادل‌کنندهٔ بار خارجی، بررسی‌های سلامت (در صورت نیاز) و قواعد فیلتر بسته‌ها (در صورت نیاز) را خودکار می‌کند. پس از آنکه ارائه‌دهندهٔ ابری یک نشانی IP برای متعادل‌کنندهٔ بار اختصاص داد، control plane آن نشانی IP خارجی را پیدا می‌کند و آن را در آبجکت Service قرار می‌دهد.

## {{% heading "whatsnext" %}}

* آموزش [اتصال برنامه‌ها با Serviceها](/docs/tutorials/services/connect-applications-service/) را دنبال کنید
* دربارهٔ [Service](/docs/concepts/services-networking/service/) بخوانید
* دربارهٔ [Ingress](/docs/concepts/services-networking/ingress/) بخوانید
