---
title: استقرار یک نسخهٔ جدید با استفاده از استقرار قناری
content_type: tutorial
weight: 10
card:
  name: tutorials
  weight: 60
  title: "اجرای یک استقرار قناری"
---

<!-- overview -->

این آموزش شما را گام‌به‌گام با استقرار یک نسخهٔ قناری (canary release) در کوبرنتیز آشنا می‌کند. با استقرار قناری می‌توانید نسخهٔ جدید یک برنامه را پیش از عرضهٔ کامل، به‌طور ایمن و با بخش کوچکی از ترافیک محیط عملیاتی آزمایش کنید. این رویکرد خطر را به حداقل می‌رساند و امکان دریافت سریع بازخورد از کاربران واقعی را فراهم می‌کند.

برای آشنایی کلی با استقرارهای قناری، بخش [استقرارهای قناری](/docs/concepts/workloads/management/#canary-deployments) را در صفحهٔ مفهومی «مدیریت بارهای کاری» ببینید.

## {{% heading "objectives" %}}

* استقرار یک نسخهٔ پایدار از یک برنامه
* استقرار یک نسخهٔ قناری در کنار نسخهٔ پایدار
* هدایت ترافیک به هر دو نسخه با استفاده از یک Service
* پایش استقرار قناری
* تکمیل عرضه با افزایش مقیاس نسخهٔ قناری و حذف نسخهٔ پایدار

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- lessoncontent -->

## آشنایی با استقرارهای قناری

استقرار قناری راهبردی است که در آن نسخهٔ جدید برنامه را در کنار نسخهٔ موجود مستقر می‌کنید. نسخهٔ جدید (قناری) درصد کوچکی از ترافیک را دریافت می‌کند و به این ترتیب می‌توانید:

* نسخهٔ جدید را با ترافیک واقعی محیط عملیاتی آزمایش کنید
* خطاها، مشکلات کارایی یا رفتارهای غیرمنتظره را پایش کنید
* در صورت شناسایی مشکل، به‌سرعت به نسخهٔ قبلی بازگردید
* اگر نسخهٔ جدید عملکرد خوبی داشت، ترافیک آن را به‌تدریج افزایش دهید

در این آموزش، از برچسب `track` برای تمایز میان نسخهٔ پایدار و نسخهٔ قناری استفاده می‌کنید. نسخهٔ پایدار از `track: stable` و نسخهٔ قناری از `track: canary` استفاده می‌کند. هر دو Deployment برچسب‌های مشترکی (`app.kubernetes.io/name: rollout-demo`) دارند که به Service امکان می‌دهد ترافیک را به هر دو مجموعه از Podها هدایت کند.

نسخهٔ پایدار را با ۳ رونوشت (replica) و نسخهٔ قناری را با ۱ رونوشت مستقر خواهید کرد. از آنجا که هر دو نسخه انتخابگر (selector) یکسانی در Service دارند (`app.kubernetes.io/name: rollout-demo`)، کوبرنتیز ترافیک را میان هر ۴ پاد توزیع بار می‌کند. با این نسبت، تقریباً ۲۵٪ ترافیک به نسخهٔ قناری و ۷۵٪ آن به نسخهٔ پایدار می‌رسد.

## استقرار نسخهٔ پایدار

ابتدا نسخهٔ پایدار برنامهٔ خود را مستقر کنید:

{{% code_sample file="application/canary/app-v1-deployment.yaml" %}}

Deployment پایدار را اعمال کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/canary/app-v1-deployment.yaml
```

بررسی کنید که Deployment ایجاد شده و Podها در حال اجرا هستند:

```shell
kubectl get deployments -l app.kubernetes.io/name=rollout-demo
```

خروجی مشابه زیر است:

```
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
rollout-demo-stable    3/3     3            3           10s
```

Podها را بررسی کنید:

```shell
kubectl get pods -l app.kubernetes.io/name=rollout-demo
```

خروجی مشابه زیر است:

```
NAME                                  READY   STATUS    RESTARTS   AGE
rollout-demo-stable-7d4b9b8c5d-abc12   1/1     Running   0          15s
rollout-demo-stable-7d4b9b8c5d-def34   1/1     Running   0          15s
rollout-demo-stable-7d4b9b8c5d-ghi56   1/1     Running   0          15s
```

## ایجاد یک Service

برای در دسترس قرار دادن برنامه، یک Service ایجاد کنید. انتخابگر این Service از برچسب مشترک (`app.kubernetes.io/name: rollout-demo`) استفاده می‌کند و برچسب `track` را در بر نمی‌گیرد؛ به همین دلیل می‌تواند ترافیک را هم به Podهای پایدار و هم به Podهای قناری هدایت کند:

{{% code_sample file="application/canary/app-service.yaml" %}}

Service را اعمال کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/canary/app-service.yaml
```

بررسی کنید که Service ایجاد شده است:

```shell
kubectl get service rollout-demo-service
```

خروجی مشابه زیر است:

```
NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
rollout-demo-service   ClusterIP   10.96.123.45    <none>        80/TCP    5s
```

با ایجاد یک Pod موقت و ارسال یک درخواست، Service را آزمایش کنید:

```shell
kubectl run curl-test --image=curlimages/curl:latest --rm -it --restart=Never -- curl http://rollout-demo-service
```

باید پاسخ‌هایی از Podهای پایدار ببینید. اگر این فرمان را چند بار اجرا کنید، نام میزبان Podهای مختلف را خواهید دید، اما همهٔ پاسخ‌ها باید نسخهٔ v1 را نشان دهند.

در این مرحله، برنامهٔ شما در وضعیت پایداری قرار دارد. در یک سناریوی واقعی، معمولاً در همین‌جا توقف می‌کنید و نسخهٔ پایدار را تا زمانی که نسخهٔ جدیدی برای استقرار آماده شود، به کار می‌گیرید. گام‌های بعدی نشان می‌دهند که چگونه یک نسخهٔ قناری را وارد کنید.

## استقرار نسخهٔ قناری

برای ایجاد یک Deployment قناری، می‌توانید مانیفست Deployment پایدار را کپی کنید و چند تغییر در آن بدهید:

- مقدار `metadata.name` را تغییر دهید (برای نمونه، به `rollout-demo-canary`)
- برچسب `track` را هم در `metadata.labels` و هم در `spec.selector.matchLabels`/`spec.template.metadata.labels` از `stable` به `canary` تغییر دهید
- تعداد رونوشت‌ها را کمتر تنظیم کنید (برای نمونه، ۱)
- ایمیج کانتینر را به نسخهٔ جدید به‌روزرسانی کنید

مانیفست به‌روزشده باید چنین باشد:

{{% code_sample file="application/canary/app-v2-deployment.yaml" %}}

می‌توانید با `kubectl` مانیفست محلی خود را اعمال کنید یا در صورت تمایل از این نمونهٔ بررسی‌شده استفاده کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/canary/app-v2-deployment.yaml
```

بررسی کنید که هر دو Deployment در حال اجرا هستند:

```shell
kubectl get deployments -l app.kubernetes.io/name=rollout-demo
```

خروجی مشابه زیر است:

```
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
rollout-demo-stable    3/3     3            3           2m
rollout-demo-canary    1/1     1            1           10s
```

همهٔ Podها را بررسی کنید:

```shell
kubectl get pods -l app.kubernetes.io/name=rollout-demo -o wide
```

خروجی مشابه زیر است:

```
NAME                                  READY   STATUS    RESTARTS   AGE   IP           NODE
rollout-demo-stable-7d4b9b8c5d-abc12   1/1     Running   0          2m    10.244.1.5   node1
rollout-demo-stable-7d4b9b8c5d-def34   1/1     Running   0          2m    10.244.1.6   node1
rollout-demo-stable-7d4b9b8c5d-ghi56   1/1     Running   0          2m    10.244.2.7   node2
rollout-demo-canary-8e5c0d9f6a-xyz78   1/1     Running   0          15s   10.244.2.8   node2
```

توجه کنید که اکنون در مجموع ۴ Pod دارید: ۳ Pod پایدار و ۱ Pod قناری.

## آزمایش توزیع ترافیک

از آنجا که هر دو Deployment از انتخابگر یکسانی در Service استفاده می‌کنند (`app.kubernetes.io/name: rollout-demo`)، Service ترافیک را به همهٔ Podها هدایت می‌کند. با ۳ Pod پایدار و ۱ Pod قناری، تقریباً ۲۵٪ درخواست‌ها به نسخهٔ قناری می‌رسد.

برای مشاهدهٔ توزیع ترافیک، Service را چند بار آزمایش کنید:

```shell
kubectl run curl-test --image=curlimages/curl:latest --rm -it --restart=Never -- \
  sh -c 'for i in $(seq 1 10); do curl -s http://rollout-demo-service; echo; done'
```

باید پاسخ‌هایی از هر دو نسخهٔ پایدار و قناری ببینید. این نسبت ممکن است متفاوت باشد، اما باید چند پاسخ از نسخهٔ قناری را در میان پاسخ‌های نسخهٔ پایدار مشاهده کنید.

برای اطمینان از اینکه هر دو نسخه ترافیک دریافت می‌کنند، EndpointSliceهای Service را بررسی کنید:

```shell
kubectl get endpointslices -l kubernetes.io/service-name=rollout-demo-service
```

خروجی مشابه زیر است (برای هر خانوادهٔ آدرس یک EndpointSlice وجود دارد و ستون ENDPOINTS به‌طور پیش‌فرض کوتاه‌شده نمایش داده می‌شود):

```
NAME                          ADDRESSTYPE   PORTS   ENDPOINTS                              AGE
rollout-demo-service-abc12    IPv4          8080    10.244.1.5,10.244.1.6,10.244.2.7 + 1 more...   3m
```

برای دیدن همهٔ آدرس‌های نقاط پایانی، از `-o yaml` استفاده کنید.

## پایش استقرار قناری

استقرار قناری خود را از نظر خطاها، مشکلات کارایی یا رفتارهای غیرمنتظره پایش کنید:

لاگ‌های Pod قناری را بررسی کنید:

```shell
kubectl logs -l app.kubernetes.io/name=rollout-demo,track=canary --tail=50
```

وضعیت Podها را پایش کنید:

```shell
kubectl get pods -l app.kubernetes.io/name=rollout-demo -w
```

برای توقف پایش، کلیدهای Ctrl+C را فشار دهید.

میزان مصرف منابع را بررسی کنید:

```shell
kubectl top pods -l app.kubernetes.io/name=rollout-demo
```

{{< note >}}
فرمان `kubectl top` به نصب بودن [metrics-server](https://github.com/kubernetes-sigs/metrics-server) در کلاستر شما نیاز دارد. اگر این مؤلفه در دسترس نیست، می‌توانید از روش‌های دیگری مانند Prometheus یا ابزارهای پایش ارائه‌دهندهٔ ابری استفاده کنید.
{{< /note >}}

## تنظیم توزیع ترافیک

اگر نسخهٔ قناری عملکرد خوبی دارد، می‌توانید با افزایش مقیاس آن، ترافیک دریافتی‌اش را به‌تدریج بیشتر کنید:

مقیاس نسخهٔ قناری را به ۲ رونوشت افزایش دهید (اکنون ۴۰٪ ترافیک):

```shell
kubectl scale deployment/rollout-demo-canary --replicas=2
```

بررسی کنید که Pod جدید در حال اجرا است:

```shell
kubectl get pods -l app.kubernetes.io/name=rollout-demo
```

به پایش ادامه دهید. اگر همه‌چیز خوب به نظر می‌رسد، می‌توانید مقیاس نسخهٔ قناری را باز هم افزایش و مقیاس نسخهٔ پایدار را کاهش دهید.

## تکمیل عرضه

اگر پایش شما مشکلاتی را در نسخهٔ قناری آشکار کرده باشد، به‌جای تکمیل عرضه باید به نسخهٔ قبلی بازگردید.
برای تمرین یک سناریوی مشکل‌دار، می‌توانید مستقیماً به بخش [بازگرداندن یک استقرار قناری](#rolling-back-a-canary-deployment) بروید.



برای تکمیل عرضه با یک Deployment واحد، ابتدا مقیاس Deployment پایدار را دوباره افزایش دهید تا اگر دریافت ایمیج جدید با شکست مواجه شد، ظرفیتی از دست ندهید. سپس ایمیج و متغیر محیطی `VERSION` را مطابق نسخهٔ جدید به‌روزرسانی کنید، منتظر تکمیل عرضه بمانید و Deployment قناری را حذف کنید:

```shell
kubectl scale deployment/rollout-demo-stable --replicas=3

# Outside of this tutorial, you wouldn't set the
# environment variable $VERSION.
# However, your new application code might need
# other configuration changes after an upgrade.
kubectl set image deployment/rollout-demo-stable rollout-demo=gcr.io/google-samples/hello-app:2.0
kubectl set env deployment/rollout-demo-stable VERSION=v2

# Wait for the rollout to complete
kubectl rollout status deployment/rollout-demo-stable

kubectl delete deployment rollout-demo-canary
```

از آنجا که این کار با موفقیت انجام شد، اکنون آماده‌اید که به بخش [پاک‌سازی](#cleaning-up) بروید. نیازی به دنبال کردن بخش بعدی دربارهٔ بازگرداندن نسخه نیست.

همچنین می‌توانید پیش از شروع پاک‌سازی، بقیهٔ این صفحه را بخوانید؛ چند موضوع دیگر نیز باقی مانده است.

## بازگرداندن یک استقرار قناری

اگر مشکلی در نسخهٔ قناری شناسایی کردید، می‌توانید به‌سرعت به نسخهٔ قبلی بازگردید:

مقیاس استقرار قناری را کاهش دهید:

```shell
kubectl scale deployment/rollout-demo-canary --replicas=0
```

کاهش مقیاس به صفر، Deployment قناری را حفظ می‌کند تا بتوانید هنگام بررسی مشکل، پیکربندی آن را وارسی کنید. پس از پایان بررسی، آن را با `kubectl delete deployment rollout-demo-canary` حذف کنید.

در صورت نیاز، مقیاس نسخهٔ پایدار را دوباره افزایش دهید:

```shell
kubectl scale deployment/rollout-demo-stable --replicas=3
```

پیش از تلاش برای استقرار قناری دیگر، مشکلات نسخهٔ قناری را بررسی کنید.

## تقسیم ترافیک با استفاده از HTTPRoute (اختیاری)


اگر از [Gateway API](https://gateway-api.sigs.k8s.io/) استفاده می‌کنید، می‌توانید با HTTPRoute کنترل دقیق‌تری بر تقسیم ترافیک میان نسخه‌های پایدار و قناری داشته باشید. با این رویکرد، به‌جای تکیه بر تعداد رونوشت‌ها، می‌توانید درصد دقیق توزیع ترافیک را مشخص کنید.

ابتدا برای نسخه‌های پایدار و قناری، Serviceهای جداگانه ایجاد کنید. این رویکرد حتی اگر از Gateway API استفاده نکنید، برای اشکال‌زدایی نیز مفید است. با داشتن Serviceهای جداگانه، می‌توانید هر نسخه را مستقیماً و به‌طور مستقل آزمایش یا پایش کنید.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: rollout-demo-stable-service
spec:
  selector:
    app.kubernetes.io/name: rollout-demo
    track: stable
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: rollout-demo-canary-service
spec:
  selector:
    app.kubernetes.io/name: rollout-demo
    track: canary
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

سپس یک HTTPRoute ایجاد کنید که ترافیک را میان این دو Service تقسیم کند:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: rollout-demo-route
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "rollout-demo.example.com"
  rules:
  - backendRefs:
    - name: rollout-demo-stable-service
      port: 80
      weight: 90
    - name: rollout-demo-canary-service
      port: 80
      weight: 10
```

این پیکربندی، صرف‌نظر از تعداد رونوشت‌ها، ۹۰٪ ترافیک را به Service پایدار و ۱۰٪ آن را به Service قناری هدایت می‌کند.

همچنین می‌توانید از مسیریابی مبتنی بر سرآیند (header) برای ارسال ترافیک مشخصی به نسخهٔ قناری استفاده کنید:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: rollout-demo-route
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "rollout-demo.example.com"
  rules:
  # Rule 1: Route traffic with canary header to canary service
  - matches:
    - headers:
      - type: Exact
        name: env
        value: canary
    backendRefs:
    - name: rollout-demo-canary-service
      port: 80
  # Rule 2: Split remaining traffic 90/10
  - backendRefs:
    - name: rollout-demo-stable-service
      port: 80
      weight: 90
    - name: rollout-demo-canary-service
      port: 80
      weight: 10
```

این پیکربندی همهٔ ترافیکی را که سرآیند `env: canary` دارد به Service قناری می‌فرستد و بقیهٔ ترافیک را به نسبت ۹۰ به ۱۰ میان نسخه‌های پایدار و قناری تقسیم می‌کند.

{{< note >}}
برای استفاده از Gateway API باید یک کنترل‌کنندهٔ Gateway در کلاستر شما نصب شده باشد. برای دستورالعمل‌های نصب و پیاده‌سازی‌های پشتیبانی‌شده، [مستندات Gateway API](https://gateway-api.sigs.k8s.io/) را ببینید.
{{< /note >}}

## خودکارسازی عرضه‌های قناری

در محیط‌های عملیاتی، عرضه‌های قناری معمولاً به‌دست کنترل‌کننده‌ها یا سامانه‌های CI/CD مدیریت می‌شوند که جابه‌جایی ترافیک، پایش، و ارتقا یا بازگرداندن نسخه را خودکار می‌کنند. ابزارهایی مانند Flux، Argo Rollouts، GitLab و بسیاری دیگر می‌توانند تحویل تدریجی، تحلیل و بازگرداندن نسخه را برای شما انجام دهند. این کار گام‌های دستی را کاهش می‌دهد و به اجرای استقرارهای ایمن و تکرارپذیر کمک می‌کند. برای اطلاعات بیشتر، مستندات ابزار استقرار یا کنترل‌کنندهٔ انتخابی خود را ببینید.

## {{% heading "cleanup" %}}

منابع ایجادشده در این آموزش را حذف کنید:

```shell
kubectl delete deployment rollout-demo-stable rollout-demo-canary
kubectl delete service rollout-demo-service
```

اگر برای HTTPRoute، Serviceهای جداگانه ایجاد کرده‌اید، آن‌ها را نیز حذف کنید:

```shell
kubectl delete service rollout-demo-stable-service rollout-demo-canary-service
kubectl delete httproute rollout-demo-route
```

## {{% heading "whatsnext" %}}

* دربارهٔ [استقرارهای قناری](/docs/concepts/workloads/management/#canary-deployments) در صفحهٔ مفهومی «مدیریت بارهای کاری» بیشتر بیاموزید.
* دربارهٔ [Deploymentها](/docs/concepts/workloads/controllers/deployment/) و نحوهٔ مدیریت چرخهٔ عمر برنامه به‌دست آن‌ها بخوانید.
* دربارهٔ [Serviceها](/docs/concepts/services-networking/service/) و اینکه چگونه کشف سرویس و توزیع بار را ممکن می‌کنند، بخوانید.
* برای قابلیت‌های پیشرفتهٔ مدیریت ترافیک، [Gateway API](/docs/concepts/services-networking/gateway/) را بررسی کنید.
* استفاده از [مقیاس‌دهی خودکار افقی Pod](/docs/tasks/run-application/horizontal-pod-autoscale/) را برای تنظیم خودکار تعداد رونوشت‌ها بر اساس معیارها در نظر بگیرید.
