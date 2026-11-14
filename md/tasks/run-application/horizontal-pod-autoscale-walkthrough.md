---
reviewers:
- fgrzadkowski
- jszczepkowski
- justinsb
- directxman12
title: راهنمای گام‌به‌گام HorizontalPodAutoscaler
content_type: task
weight: 100
min-kubernetes-server-version: 1.23
---

<!-- overview -->

یک [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
(یا به‌اختصار HPA) یک منبع بار کاری (مانند یک {{< glossary_tooltip text="Deployment" term_id="deployment" >}} یا
{{< glossary_tooltip text="StatefulSet" term_id="statefulset" >}}) را به‌طور خودکار به‌روزرسانی می‌کند. هدف از این کار
این است که مقیاس بار کاری به‌صورت خودکار با میزان تقاضا هماهنگ شود.

مقیاس‌دهی افقی یعنی در پاسخ به افزایش بار،
{{< glossary_tooltip text="Podهای" term_id="pod" >}} بیشتری مستقر شوند.
این روش با مقیاس‌دهی _عمودی_ تفاوت دارد. در کوبرنتیز، مقیاس‌دهی عمودی به معنای
اختصاص منابع بیشتر (برای مثال حافظه یا CPU) به Podهایی است که از قبل برای آن بار کاری
در حال اجرا هستند.

اگر بار کاهش یابد و تعداد Podها از حداقل پیکربندی‌شده بیشتر باشد،
HorizontalPodAutoscaler به منبع بار کاری (Deployment، StatefulSet
یا هر منبع مشابه دیگری) دستور می‌دهد که مقیاس را کاهش دهد.

این سند شما را گام‌به‌گام با مثالی همراهی می‌کند که در آن HorizontalPodAutoscaler
برای مدیریت خودکار مقیاس یک برنامهٔ وب نمونه فعال می‌شود. این بار کاری نمونه
یک سرور Apache httpd است که مقداری کد PHP را اجرا می‌کند.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}} اگر نسخهٔ قدیمی‌تری
از کوبرنتیز را اجرا می‌کنید، به نسخهٔ مستندات مربوط به همان انتشار مراجعه کنید (بنگرید به
[نسخه‌های موجود مستندات](/docs/home/supported-doc-versions/)).

برای دنبال کردن این راهنما، به کلاستری نیز نیاز دارید که
[Metrics Server](https://github.com/kubernetes-sigs/metrics-server#readme) در آن مستقر و پیکربندی شده باشد.
سرویس Metrics Server کوبرنتیز معیارهای منابع را از
{{<glossary_tooltip term_id="kubelet" text="kubeletهای">}} کلاستر شما جمع‌آوری می‌کند و این معیارها را
از طریق [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) در دسترس قرار می‌دهد. این سرویس برای این کار
از یک [APIService](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) استفاده می‌کند
تا انواع جدیدی از منبع را اضافه کند که مقادیر خوانده‌شدهٔ معیارها را نمایش می‌دهند.

برای آشنایی با نحوهٔ استقرار Metrics Server،
[مستندات metrics-server](https://github.com/kubernetes-sigs/metrics-server#deployment) را ببینید.

اگر از {{< glossary_tooltip term_id="minikube" >}} استفاده می‌کنید، برای فعال کردن metrics-server دستور زیر را اجرا کنید:

```shell
minikube addons enable metrics-server
```

<!-- steps -->

## اجرا و در دسترس قرار دادن سرور php-apache

برای نمایش عملکرد HorizontalPodAutoscaler، ابتدا یک Deployment راه‌اندازی می‌کنید که کانتینری با ایمیج
`hpa-example` اجرا می‌کند و سپس با استفاده از مانیفست زیر، آن را به‌صورت یک {{< glossary_tooltip term_id="service">}}
در دسترس قرار می‌دهید:

{{% code_sample file="application/php-apache.yaml" %}}

برای این کار، دستور زیر را اجرا کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml
```

```
deployment.apps/php-apache created
service/php-apache created
```

## ایجاد HorizontalPodAutoscaler {#create-horizontal-pod-autoscaler}

اکنون که سرور در حال اجراست، مقیاس‌دهندهٔ خودکار (autoscaler) را با استفاده از `kubectl` ایجاد کنید.
زیرفرمان [`kubectl autoscale`](/docs/reference/generated/kubectl/kubectl-commands#autoscale)،
که بخشی از `kubectl` است، در این کار به شما کمک می‌کند.

به‌زودی دستوری را اجرا می‌کنید که یک HorizontalPodAutoscaler ایجاد می‌کند. این HorizontalPodAutoscaler
تعداد رپلیکاهای Podهای تحت کنترل Deployment به نام php-apache را، که در گام نخست این دستورالعمل
ایجاد کردید، بین ۱ تا ۱۰ نگه می‌دارد.

به‌طور تقریبی، {{<glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller">}} HPA تعداد رپلیکاها را
(با به‌روزرسانی Deployment) افزایش یا کاهش می‌دهد تا میانگین مصرف CPU در همهٔ Podها در حد ۵۰٪ باقی بماند.
سپس Deployment، آبجکت ReplicaSet را به‌روزرسانی می‌کند (این بخشی از سازوکار همهٔ Deploymentها در کوبرنتیز است)
و پس از آن، ReplicaSet بر اساس تغییر در `.spec` خود، Podهایی را اضافه یا حذف می‌کند.

از آنجا که هر Pod از طریق `kubectl run` مقدار ۲۰۰ میلی‌هسته (milli-core) درخواست می‌کند، این به معنای
میانگین مصرف CPU برابر با ۱۰۰ میلی‌هسته است.
برای اطلاعات بیشتر دربارهٔ این الگوریتم، [جزئیات الگوریتم](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/#algorithm-details)
را ببینید.


برای ایجاد HorizontalPodAutoscaler دستور زیر را اجرا کنید:

```shell
kubectl autoscale deployment php-apache --cpu=50% --min=1 --max=10
```

```
horizontalpodautoscaler.autoscaling/php-apache autoscaled
```

با اجرای دستور زیر می‌توانید وضعیت فعلی HorizontalPodAutoscaler تازه‌ایجادشده را بررسی کنید:

```shell
# You can use "hpa" or "horizontalpodautoscaler"; either name works OK.
kubectl get hpa
```

خروجی مشابه زیر است:
```
NAME         REFERENCE                     TARGET    MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   0% / 50%  1         10        1          18s
```

(اگر HorizontalPodAutoscalerهای دیگری با نام‌های متفاوت می‌بینید، به این معناست که از قبل وجود داشته‌اند
و معمولاً مشکلی ایجاد نمی‌کنند.)

توجه کنید که مصرف فعلی CPU برابر با ۰٪ است، زیرا هیچ کلاینتی به سرور درخواست ارسال نمی‌کند
(ستون ``TARGET`` میانگین مصرف را در همهٔ Podهای تحت کنترل Deployment مربوطه نشان می‌دهد).

## افزایش بار {#increase-load}

در ادامه، ببینید مقیاس‌دهندهٔ خودکار چگونه به افزایش بار واکنش نشان می‌دهد.
برای این کار، Pod دیگری راه‌اندازی می‌کنید که نقش کلاینت را ایفا کند. کانتینر درون این Pod کلاینت
در یک حلقهٔ بی‌پایان اجرا می‌شود و پیوسته به سرویس php-apache درخواست می‌فرستد.

```shell
# Run this in a separate terminal
# so that the load generation continues and you can carry on with the rest of the steps
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```

اکنون دستور زیر را اجرا کنید:
```shell
# type Ctrl+C to end the watch when you're ready
kubectl get hpa php-apache --watch
```

پس از حدود یک دقیقه، باید افزایش بار CPU را ببینید؛ برای مثال:

```
NAME         REFERENCE                     TARGET      MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   305% / 50%  1         10        1          3m
```

و سپس رپلیکاهای بیشتری را؛ برای مثال:
```
NAME         REFERENCE                     TARGET      MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   305% / 50%  1         10        7          3m
```

در اینجا مصرف CPU به ۳۰۵٪ مقدار درخواست‌شده رسیده است.
در نتیجه، اندازهٔ Deployment به ۷ رپلیکا تغییر یافته است:

```shell
kubectl get deployment php-apache
```

باید ببینید که تعداد رپلیکاها با عدد گزارش‌شده در HorizontalPodAutoscaler مطابقت دارد:
```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
php-apache   7/7      7           7           19m
```

{{< note >}}
ممکن است چند دقیقه طول بکشد تا تعداد رپلیکاها پایدار شود. از آنجا که میزان بار
به هیچ شکلی کنترل نمی‌شود، ممکن است تعداد نهایی رپلیکاها با این مثال متفاوت باشد.
{{< /note >}}

## توقف تولید بار {#stop-load}

برای پایان دادن به مثال، ارسال بار را متوقف کنید.

در ترمینالی که Pod اجراکنندهٔ ایمیج `busybox` را در آن ایجاد کردید، با فشردن
`<Ctrl> + C` تولید بار را متوقف کنید.

سپس (پس از حدود یک دقیقه) وضعیت نهایی را بررسی کنید:

```shell
# type Ctrl+C to end the watch when you're ready
kubectl get hpa php-apache --watch
```

خروجی مشابه زیر است:

```
NAME         REFERENCE                     TARGET       MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   0% / 50%     1         10        1          11m
```

و Deployment نیز نشان می‌دهد که مقیاس آن کاهش یافته است:

```shell
kubectl get deployment php-apache
```

```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
php-apache   1/1     1            1           27m
```

پس از آنکه مصرف CPU به ۰ رسید، HPA به‌طور خودکار تعداد رپلیکاها را به ۱ کاهش داد.

مقیاس‌دهی خودکار رپلیکاها ممکن است چند دقیقه طول بکشد.

<!-- discussion -->

## مقیاس‌دهی خودکار بر اساس چند معیار و معیارهای سفارشی

با استفاده از نسخهٔ API `autoscaling/v2` می‌توانید معیارهای دیگری را نیز برای مقیاس‌دهی خودکار
Deployment `php-apache` به کار بگیرید.

ابتدا YAML مربوط به HorizontalPodAutoscaler خود را در قالب `autoscaling/v2` دریافت کنید:

```shell
kubectl get hpa php-apache -o yaml > /tmp/hpa-v2.yaml
```

فایل `/tmp/hpa-v2.yaml` را در یک ویرایشگر باز کنید؛ باید YAMLی شبیه به این ببینید:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
status:
  observedGeneration: 1
  lastScaleTime: <some-time>
  currentReplicas: 1
  desiredReplicas: 1
  currentMetrics:
  - type: Resource
    resource:
      name: cpu
      current:
        averageUtilization: 0
        averageValue: 0
```

توجه کنید که فیلد `targetCPUUtilizationPercentage` با آرایه‌ای به نام `metrics` جایگزین شده است.
معیار مصرف CPU یک *معیار منبع* (resource metric) است، زیرا به‌صورت درصدی از منبعی بیان می‌شود
که روی کانتینرهای Pod مشخص شده است. توجه کنید که علاوه بر CPU می‌توانید معیارهای منبع دیگری نیز تعیین کنید.
به‌طور پیش‌فرض، تنها معیار منبع پشتیبانی‌شدهٔ دیگر `memory` است. نام این منابع از کلاستری به کلاستر دیگر
تغییر نمی‌کند و تا زمانی که API `metrics.k8s.io` در دسترس باشد، این منابع همیشه در دسترس خواهند بود.

همچنین می‌توانید معیارهای منبع را به‌جای درصدی از مقدار درخواست‌شده، به‌صورت مقادیر مستقیم مشخص کنید.
برای این کار، به‌جای `Utilization` از `target.type` با مقدار `AverageValue` استفاده کنید و
به‌جای فیلد `target.averageUtilization`، فیلد متناظر `target.averageValue` را تنظیم کنید.

```
  metrics:
  - type: Resource
    resource:
      name: memory
      target:
        type: AverageValue
        averageValue: 500Mi
```

دو نوع دیگر از معیارها نیز وجود دارد که هر دو *معیار سفارشی* (custom metrics) به شمار می‌روند:
معیارهای Pod و معیارهای آبجکت. ممکن است نام این معیارها مختص هر کلاستر باشد و این معیارها
به راه‌اندازی پیشرفته‌تری برای پایش کلاستر نیاز دارند.

نخستین نوع از این معیارهای جایگزین، *معیارهای Pod* است. این معیارها Podها را توصیف می‌کنند،
در میان Podها میانگین‌گیری می‌شوند و با یک مقدار هدف مقایسه می‌شوند تا تعداد رپلیکاها تعیین شود.
عملکرد آن‌ها بسیار شبیه معیارهای منبع است، با این تفاوت که *فقط* از نوع `target` با مقدار `AverageValue` پشتیبانی می‌کنند.

معیارهای Pod با استفاده از یک بلوک معیار مانند نمونهٔ زیر مشخص می‌شوند:

```yaml
type: Pods
pods:
  metric:
    name: packets-per-second
  target:
    type: AverageValue
    averageValue: 1k
```

دومین نوع معیار جایگزین، *معیارهای آبجکت* است. این معیارها به‌جای توصیف Podها، آبجکت دیگری را
در همان فضای نام (namespace) توصیف می‌کنند. این معیارها لزوماً از خود آن آبجکت دریافت نمی‌شوند؛
فقط آن را توصیف می‌کنند. معیارهای آبجکت از هر دو نوع `target` یعنی `Value` و `AverageValue`
پشتیبانی می‌کنند. با `Value`، مقدار هدف مستقیماً با معیار بازگردانده‌شده از API مقایسه می‌شود.
با `AverageValue`، مقدار بازگردانده‌شده از API معیارهای سفارشی پیش از مقایسه با هدف، بر تعداد Podها
تقسیم می‌شود. مثال زیر نمایش YAML معیار `requests-per-second` است.

```yaml
type: Object
object:
  metric:
    name: requests-per-second
  describedObject:
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    name: main-route
  target:
    type: Value
    value: 2k
```

اگر چند بلوک معیار از این نوع تعیین کنید، HorizontalPodAutoscaler هر معیار را به‌نوبت در نظر می‌گیرد؛
یعنی برای هر معیار، تعداد رپلیکای پیشنهادی را محاسبه می‌کند و سپس معیاری را انتخاب می‌کند
که بیشترین تعداد رپلیکا را به دست می‌دهد.

برای مثال، اگر سامانهٔ پایش شما معیارهایی دربارهٔ ترافیک شبکه جمع‌آوری کند،
می‌توانید تعریف بالا را با استفاده از `kubectl edit` به شکل زیر به‌روزرسانی کنید:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
  - type: Pods
    pods:
      metric:
        name: packets-per-second
      target:
        type: AverageValue
        averageValue: 1k
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        name: main-route
      target:
        type: Value
        value: 10k
status:
  observedGeneration: 1
  lastScaleTime: <some-time>
  currentReplicas: 1
  desiredReplicas: 1
  currentMetrics:
  - type: Resource
    resource:
      name: cpu
    current:
      averageUtilization: 0
      averageValue: 0
  - type: Object
    object:
      metric:
        name: requests-per-second
      describedObject:
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        name: main-route
      current:
        value: 10k
```

در این صورت، HorizontalPodAutoscaler شما تلاش می‌کند اطمینان حاصل کند که هر Pod تقریباً ۵۰٪
از CPU درخواستی خود را مصرف می‌کند و ۱۰۰۰ بسته در ثانیه را پاسخ می‌دهد، و همهٔ Podهای پشت
Ingress به نام main-route در مجموع ۱۰۰۰۰ درخواست در ثانیه را پاسخ می‌دهند.

### مقیاس‌دهی خودکار بر اساس معیارهای دقیق‌تر

بسیاری از خطوط لولهٔ معیارها (metrics pipelines) به شما امکان می‌دهند معیارها را یا با نام
یا با مجموعه‌ای از توصیفگرهای اضافی به نام _برچسب‌ها_ توصیف کنید. برای همهٔ انواع معیارهای غیرمنبعی
(Pod، آبجکت و خارجی، که در ادامه توضیح داده می‌شود) می‌توانید یک انتخابگر (selector) برچسب اضافی
تعیین کنید که به خط لولهٔ معیار شما ارسال می‌شود. برای نمونه، اگر معیاری به نام `http_requests`
را با برچسب `verb` جمع‌آوری می‌کنید، می‌توانید بلوک معیار زیر را تعیین کنید تا مقیاس‌دهی
فقط بر اساس درخواست‌های GET انجام شود:

```yaml
type: Object
object:
  metric:
    name: http_requests
    selector: {matchLabels: {verb: GET}}
```

این انتخابگر از همان نحوی پیروی می‌کند که انتخابگرهای کامل برچسب در کوبرنتیز به کار می‌برند.
اگر نام و انتخابگر با چند سری داده مطابقت داشته باشند، خط لولهٔ پایش تعیین می‌کند که این سری‌ها
چگونه در قالب یک مقدار واحد ادغام شوند. انتخابگر به‌صورت افزوده اعمال می‌شود و نمی‌تواند معیارهایی را
انتخاب کند که آبجکت‌هایی **غیر** از آبجکت هدف را توصیف می‌کنند (در نوع `Pods`، آبجکت هدف همان
Podهای هدف و در نوع `Object`، همان آبجکت توصیف‌شده است).

### مقیاس‌دهی خودکار بر اساس معیارهای نامرتبط با آبجکت‌های کوبرنتیز

ممکن است لازم باشد برنامه‌هایی که روی کوبرنتیز اجرا می‌شوند، بر اساس معیارهایی مقیاس‌دهی خودکار شوند
که ارتباط آشکاری با هیچ آبجکتی در کلاستر کوبرنتیز ندارند؛ مانند معیارهایی که یک سرویس میزبانی‌شده را
توصیف می‌کنند و هیچ ارتباط مستقیمی با فضاهای نام کوبرنتیز ندارند. در کوبرنتیز 1.10 و نسخه‌های بعدی،
می‌توانید این نیاز را با *معیارهای خارجی* (external metrics) برطرف کنید.

استفاده از معیارهای خارجی به شناخت سامانهٔ پایش شما نیاز دارد؛ راه‌اندازی آن مشابه راه‌اندازی لازم
برای استفاده از معیارهای سفارشی است. معیارهای خارجی به شما امکان می‌دهند کلاستر خود را بر اساس
هر معیاری که در سامانهٔ پایش شما موجود است، به‌طور خودکار مقیاس‌دهی کنید. یک بلوک `metric` با
`name` و `selector`، مانند نمونهٔ بالا، تعیین کنید و به‌جای نوع `Object` از نوع معیار `External` استفاده کنید.
اگر چند سری زمانی با `metricSelector` مطابقت داشته باشند، HorizontalPodAutoscaler مجموع مقادیر آن‌ها را
به کار می‌برد. معیارهای خارجی از هر دو نوع هدف `Value` و `AverageValue` پشتیبانی می‌کنند و این انواع
دقیقاً همانند زمانی عمل می‌کنند که از نوع `Object` استفاده می‌کنید.

برای مثال، اگر برنامهٔ شما وظایفی را از یک سرویس صف میزبانی‌شده پردازش می‌کند، می‌توانید بخش زیر را
به مانیفست HorizontalPodAutoscaler خود اضافه کنید تا مشخص کنید به ازای هر ۳۰ وظیفهٔ در انتظار،
به یک کارگر (worker) نیاز دارید.

```yaml
- type: External
  external:
    metric:
      name: queue_messages_ready
      selector:
        matchLabels:
          queue: "worker_tasks"
    target:
      type: AverageValue
      averageValue: 30
```

در صورت امکان، بهتر است به‌جای معیارهای خارجی از انواع هدف معیارهای سفارشی استفاده کنید، زیرا
ایمن‌سازی API معیارهای سفارشی برای مدیران کلاستر آسان‌تر است. از آنجا که API معیارهای خارجی
به‌طور بالقوه امکان دسترسی به هر معیاری را فراهم می‌کند، مدیران کلاستر باید هنگام در دسترس قرار دادن
آن احتیاط کنند.

## پیوست: شرایط وضعیت Horizontal Pod Autoscaler

هنگام استفاده از قالب `autoscaling/v2` برای HorizontalPodAutoscaler، می‌توانید *شرایط وضعیت*
(status conditions) را ببینید که کوبرنتیز روی HorizontalPodAutoscaler تنظیم می‌کند. این شرایط وضعیت
نشان می‌دهند که آیا HorizontalPodAutoscaler می‌تواند مقیاس را تغییر دهد یا نه، و آیا در حال حاضر
به هر شکلی محدود شده است یا نه.

این شرایط در فیلد `status.conditions` نمایش داده می‌شوند. برای دیدن شرایطی که بر یک HorizontalPodAutoscaler
اثر می‌گذارند، می‌توانیم از `kubectl describe hpa` استفاده کنیم:

```shell
kubectl describe hpa cm-test
```

```
Name:                           cm-test
Namespace:                      prom
Labels:                         <none>
Annotations:                    <none>
CreationTimestamp:              Fri, 16 Jun 2017 18:09:22 +0000
Reference:                      ReplicationController/cm-test
Metrics:                        ( current / target )
  "http_requests" on pods:      66m / 500m
Min replicas:                   1
Max replicas:                   4
ReplicationController pods:     1 current / 1 desired
Conditions:
  Type                  Status  Reason                  Message
  ----                  ------  ------                  -------
  AbleToScale           True    ReadyForNewScale        the last scale time was sufficiently old as to warrant a new scale
  ScalingActive         True    ValidMetricFound        the HPA was able to successfully calculate a replica count from pods metric http_requests
  ScalingLimited        False   DesiredWithinRange      the desired replica count is within the acceptable range
Events:
```

برای این HorizontalPodAutoscaler، چند شرط را در وضعیت سالم می‌بینید. شرط نخست، `AbleToScale`،
نشان می‌دهد که آیا HPA می‌تواند مقیاس‌ها را دریافت و به‌روزرسانی کند یا نه، و همچنین آیا شرایط
مربوط به عقب‌نشینی (backoff) مانع مقیاس‌دهی می‌شوند یا نه. شرط دوم، `ScalingActive`، نشان می‌دهد
که آیا HPA فعال است (یعنی تعداد رپلیکاهای هدف صفر نیست) و می‌تواند مقیاس‌های مطلوب را محاسبه کند یا نه.
هنگامی که مقدار این شرط `False` باشد، معمولاً نشان‌دهندهٔ مشکل در دریافت معیارهاست. در نهایت،
آخرین شرط، `ScalingLimited`، نشان می‌دهد که مقیاس مطلوب به حداکثر یا حداقل تعیین‌شده در
HorizontalPodAutoscaler محدود شده است. این نشانه‌ای است که شاید بخواهید محدودیت‌های حداقل
یا حداکثر تعداد رپلیکا را در HorizontalPodAutoscaler خود افزایش یا کاهش دهید.

## کمیت‌ها

همهٔ معیارها در HorizontalPodAutoscaler و APIهای معیارها با نمادگذاری ویژه‌ای از اعداد صحیح
مشخص می‌شوند که در کوبرنتیز با نام {{< glossary_tooltip term_id="quantity" text="کمیت">}} شناخته می‌شود.
برای مثال، کمیت `10500m` در نمادگذاری اعشاری به‌صورت `10.5` نوشته می‌شود. این APIها در صورت امکان
اعداد صحیح را بدون پسوند بازمی‌گردانند و در غیر این صورت، معمولاً کمیت‌ها را بر حسب میلی‌واحد بازمی‌گردانند.
به همین دلیل ممکن است ببینید مقدار معیار شما میان `1` و `1500m`، یا در نمادگذاری اعشاری میان `1` و `1.5`،
نوسان می‌کند.

## سناریوهای ممکن دیگر

### ایجاد مقیاس‌دهنده‌ی خودکار به‌صورت اعلانی

به‌جای اینکه با دستور `kubectl autoscale` یک HorizontalPodAutoscaler را به‌صورت دستوری (imperative) ایجاد کنیم، می‌توانیم با مانیفست زیر آن را به‌صورت اعلانی (declarative) بسازیم:

{{% code_sample file="application/hpa/php-apache.yaml" %}}

سپس با اجرای دستور زیر، مقیاس‌دهنده‌ی خودکار را ایجاد کنید:

```shell
kubectl create -f https://k8s.io/examples/application/hpa/php-apache.yaml
```

```
horizontalpodautoscaler.autoscaling/php-apache created
```
