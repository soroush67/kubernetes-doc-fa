---
reviewers:
- fgrzadkowski
- piosz
title: خط لوله‌ی متریک‌های منابع
content_type: concept
weight: 15
---

<!-- overview -->

در کوبرنتیز، _Metrics API_ مجموعه‌ای پایه از متریک‌ها را برای پشتیبانی از مقیاس‌دهی خودکار و موارد استفاده‌ی مشابه فراهم می‌کند. این API اطلاعات مربوط به میزان مصرف منابع نودها و پادها، از جمله متریک‌های CPU و حافظه، را در دسترس قرار می‌دهد. اگر Metrics API را در کلاستر خود مستقر کنید، کلاینت‌های API کوبرنتیز می‌توانند این اطلاعات را پرس‌وجو کنند و شما نیز می‌توانید مجوزهای این کار را با سازوکارهای کنترل دسترسی کوبرنتیز مدیریت کنید.

مقیاس‌دهنده‌های [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) (HPA) و [VerticalPodAutoscaler](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) (VPA) از داده‌های Metrics API استفاده می‌کنند تا تعداد رپلیکاها و منابع بار کاری را متناسب با تقاضای مشتریان تنظیم کنند.

همچنین می‌توانید متریک‌های منابع را با فرمان [`kubectl top`](/docs/reference/generated/kubectl/kubectl-commands#top) مشاهده کنید.

{{< note >}}
‏Metrics API و خط لوله‌ی متریکی که این API امکان‌پذیر می‌کند، تنها حداقل متریک‌های CPU و حافظه را برای فعال‌سازی مقیاس‌دهی خودکار با HPA و/یا VPA ارائه می‌دهند. اگر می‌خواهید مجموعه‌ی کامل‌تری از متریک‌ها فراهم کنید، می‌توانید با استقرار یک [خط لوله‌ی متریک](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/#full-metrics-pipeline) دوم که از _Custom Metrics API_ استفاده می‌کند، Metrics API ساده‌تر را تکمیل کنید.
{{< /note >}}


شکل ۱ معماری خط لوله‌ی متریک‌های منابع را نشان می‌دهد.

{{< mermaid >}}
flowchart RL
subgraph cluster[Cluster]
direction RL
S[ <br><br> ]
A[Metrics-<br>Server]
subgraph B[Nodes]
direction TB
D[cAdvisor] --> C[kubelet]
E[Container<br>runtime] --> D
E1[Container<br>runtime] --> D
P[pod data] -.- C
end
L[API<br>server]
W[HPA]
C ---->|node level<br>resource metrics| A -->|metrics<br>API| L --> W
end
L ---> K[kubectl<br>top]
classDef box fill:#fff,stroke:#000,stroke-width:1px,color:#000;
class W,B,P,K,cluster,D,E,E1 box
classDef spacewhite fill:#ffffff,stroke:#fff,stroke-width:0px,color:#000
class S spacewhite
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
class A,L,C k8s
{{< /mermaid >}}

شکل ۱. خط لوله‌ی متریک‌های منابع

اجزای این معماری، به ترتیب از راست به چپ در شکل، عبارت‌اند از:

* ابزار [cAdvisor](https://github.com/google/cadvisor): دیمنی برای جمع‌آوری، تجمیع و ارائه‌ی متریک‌های کانتینر که در kubelet گنجانده شده است.
* مؤلفه‌ی [kubelet](/docs/concepts/architecture/#kubelet): عامل نود برای مدیریت منابع کانتینرها. متریک‌های منابع از طریق endpointهای `/metrics/resource` و `/stats` در API مربوط به kubelet در دسترس هستند.
* [متریک‌های منابع در سطح نود](/docs/reference/instrumentation/node-metrics): APIای که kubelet برای کشف و بازیابی آمار خلاصه‌شده‌ی هر نود فراهم می‌کند و از طریق endpoint `/metrics/resource` در دسترس است.
* مؤلفه‌ی [metrics-server](#metrics-server): افزونه‌ی کلاستر که متریک‌های منابع دریافت‌شده از هر kubelet را جمع‌آوری و تجمیع می‌کند. سرور API، ‏Metrics API را برای استفاده‌ی HPA، ‏VPA و فرمان `kubectl top` ارائه می‌دهد. ‏Metrics Server یک پیاده‌سازی مرجع از Metrics API است.
* رابط [Metrics API](#metrics-api): یک API کوبرنتیز که دسترسی به میزان CPU و حافظه‌ی مصرفی را برای مقیاس‌دهی خودکار بار کاری فراهم می‌کند. برای اینکه این قابلیت در کلاستر شما کار کند، به یک سرور افزونه‌ی API نیاز دارید که Metrics API را ارائه دهد.

  {{< note >}}
  ابزار cAdvisor از خواندن متریک‌ها از cgroupها پشتیبانی می‌کند که با محیط‌های اجرای کانتینر رایج در لینوکس کار می‌کند. اگر از محیط اجرای کانتینری استفاده می‌کنید که سازوکار دیگری برای جداسازی منابع دارد، مثلاً مجازی‌سازی، آن محیط اجرای کانتینر باید از [CRI Container Metrics](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-node/cri-container-stats.md) پشتیبانی کند تا متریک‌ها در دسترس kubelet قرار گیرند.
  {{< /note >}}

<!-- body -->

## Metrics API
{{< feature-state for_k8s_version="1.37" state="stable" >}}

مؤلفه‌ی metrics-server، ‏Metrics API را پیاده‌سازی می‌کند. با این API می‌توانید به میزان مصرف CPU و حافظه‌ی نودها و پادهای کلاستر خود دسترسی داشته باشید. نقش اصلی آن، تأمین متریک‌های مصرف منابع برای مؤلفه‌های مقیاس‌دهنده‌ی خودکار کوبرنتیز است.

در ادامه، نمونه‌ای از درخواست Metrics API برای نود `minikube` آمده است که برای خوانایی بیشتر، خروجی آن به `jq` فرستاده شده است:

```shell
kubectl get --raw "/apis/metrics.k8s.io/v1/nodes/minikube" | jq '.'
```

همین فراخوانی API با استفاده از `curl` به این صورت است:

```shell
curl http://localhost:8080/apis/metrics.k8s.io/v1/nodes/minikube
```

نمونه‌ی پاسخ:

```json
{
  "kind": "NodeMetrics",
  "apiVersion": "metrics.k8s.io/v1",
  "metadata": {
    "name": "minikube",
    "selfLink": "/apis/metrics.k8s.io/v1/nodes/minikube",
    "creationTimestamp": "2022-01-27T18:48:43Z"
  },
  "timestamp": "2022-01-27T18:48:33Z",
  "window": "30s",
  "usage": {
    "cpu": "487558164n",
    "memory": "732212Ki"
  }
}
```

در ادامه، نمونه‌ای از درخواست Metrics API برای پاد `kube-scheduler-minikube` در فضای نام (namespace) `kube-system` آمده است که برای خوانایی بیشتر، خروجی آن به `jq` فرستاده شده است:

```shell
kubectl get --raw "/apis/metrics.k8s.io/v1/namespaces/kube-system/pods/kube-scheduler-minikube" | jq '.'
```

همین فراخوانی API با استفاده از `curl` به این صورت است:

```shell
curl http://localhost:8080/apis/metrics.k8s.io/v1/namespaces/kube-system/pods/kube-scheduler-minikube
```

نمونه‌ی پاسخ:

```json
{
  "kind": "PodMetrics",
  "apiVersion": "metrics.k8s.io/v1",
  "metadata": {
    "name": "kube-scheduler-minikube",
    "namespace": "kube-system",
    "selfLink": "/apis/metrics.k8s.io/v1/namespaces/kube-system/pods/kube-scheduler-minikube",
    "creationTimestamp": "2022-01-27T19:25:00Z"
  },
  "timestamp": "2022-01-27T19:24:31Z",
  "window": "30s",
  "containers": [
    {
      "name": "kube-scheduler",
      "usage": {
        "cpu": "9559630n",
        "memory": "22244Ki"
      }
    }
  ]
}
```

‏Metrics API در مخزن [k8s.io/metrics](https://github.com/kubernetes/metrics) تعریف شده است. باید [لایه‌ی تجمیع API](/docs/tasks/extend-kubernetes/configure-aggregation-layer/) را فعال کنید و یک [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/) برای API ‏`metrics.k8s.io` ثبت کنید.

برای آشنایی بیشتر با Metrics API، به [طراحی API متریک‌های منابع](https://git.k8s.io/design-proposals-archive/instrumentation/resource-metrics-api.md)، [مخزن metrics-server](https://github.com/kubernetes-sigs/metrics-server) و [API متریک‌های منابع](https://github.com/kubernetes/metrics#resource-metrics-api) مراجعه کنید.


{{< note >}}
برای دسترسی به Metrics API، باید metrics-server یا آداپتور جایگزینی را که این API را ارائه می‌دهد مستقر کنید.
{{< /note >}}

## اندازه‌گیری مصرف منابع

### CPU

میزان CPU به صورت میانگین مصرف هسته و بر حسب واحدهای cpu گزارش می‌شود. در کوبرنتیز، یک cpu معادل ۱ vCPU/هسته در ارائه‌دهندگان ابری و ۱ هایپرترد (hyper-thread) در پردازنده‌های اینتل روی سخت‌افزار فیزیکی (bare-metal) است.

این مقدار از محاسبه‌ی نرخ تغییرات یک شمارنده‌ی تجمعی CPU به دست می‌آید که هسته‌ی سیستم‌عامل (در هر دو هسته‌ی لینوکس و ویندوز) فراهم می‌کند. بازه‌ی زمانی استفاده‌شده برای محاسبه‌ی CPU در فیلد window در Metrics API نشان داده می‌شود.

برای آشنایی بیشتر با نحوه‌ی تخصیص و اندازه‌گیری منابع CPU در کوبرنتیز، به [مفهوم CPU](/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu) مراجعه کنید.

### حافظه

میزان حافظه به صورت مجموعه‌ی کاری (working set) و بر حسب بایت، در لحظه‌ی جمع‌آوری متریک گزارش می‌شود.

در حالت ایدئال، «مجموعه‌ی کاری» مقدار حافظه‌ی در حال استفاده‌ای است که در شرایط فشار حافظه نمی‌توان آن را آزاد کرد. با این حال، نحوه‌ی محاسبه‌ی مجموعه‌ی کاری به سیستم‌عامل میزبان بستگی دارد و معمولاً برای رسیدن به یک تخمین، به‌شدت به روش‌های اکتشافی (heuristics) متکی است.

مدل کوبرنتیز برای مجموعه‌ی کاری یک کانتینر انتظار دارد که محیط اجرای کانتینر، حافظه‌ی ناشناس (anonymous memory) مرتبط با آن کانتینر را به حساب آورد. متریک مجموعه‌ی کاری معمولاً بخشی از حافظه‌ی کش‌شده (مبتنی بر فایل) را نیز شامل می‌شود، زیرا سیستم‌عامل میزبان همیشه نمی‌تواند صفحه‌های حافظه را بازپس بگیرد.

برای آشنایی بیشتر با نحوه‌ی تخصیص و اندازه‌گیری منابع حافظه در کوبرنتیز، به [مفهوم حافظه](/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory) مراجعه کنید.

## Metrics Server

مؤلفه‌ی metrics-server متریک‌های منابع را از kubeletها دریافت می‌کند و آن‌ها را از طریق Metrics API در سرور API کوبرنتیز در اختیار HPA و VPA قرار می‌دهد. همچنین می‌توانید این متریک‌ها را با فرمان `kubectl top` مشاهده کنید.

مؤلفه‌ی metrics-server برای پیگیری نودها و پادهای کلاستر از API کوبرنتیز استفاده می‌کند و برای دریافت متریک‌ها، هر نود را از طریق HTTP پرس‌وجو می‌کند. این مؤلفه همچنین یک نمای داخلی از فراداده‌ی پادها می‌سازد و حافظه‌ی نهانی از وضعیت سلامت پادها نگه می‌دارد. این اطلاعات کش‌شده‌ی سلامت پادها از طریق API افزونه‌ای که metrics-server ارائه می‌دهد در دسترس است.

برای مثال، در یک پرس‌وجوی HPA، ‏metrics-server باید مشخص کند کدام پادها با انتخابگرهای (selector) برچسب در Deployment مطابقت دارند.

مؤلفه‌ی metrics-server برای جمع‌آوری متریک‌ها از هر نود، API مربوط به [kubelet](/docs/reference/command-line-tools-reference/kubelet/) را فراخوانی می‌کند. بسته به نسخه‌ی metrics-server، از یکی از این endpointها استفاده می‌شود:

* ‏endpoint منبع متریک‌ها `/metrics/resource` در نسخه‌ی v0.6.0 و بالاتر، یا
* ‏endpoint مربوط به Summary API یعنی `/stats/summary` در نسخه‌های قدیمی‌تر

## {{% heading "whatsnext" %}}

برای آشنایی بیشتر با metrics-server، به [مخزن metrics-server](https://github.com/kubernetes-sigs/metrics-server) مراجعه کنید.

همچنین می‌توانید موارد زیر را بررسی کنید:

* [طراحی metrics-server](https://git.k8s.io/design-proposals-archive/instrumentation/metrics-server.md)
* [پرسش‌های متداول metrics-server](https://github.com/kubernetes-sigs/metrics-server/blob/master/FAQ.md)
* [مشکلات شناخته‌شده‌ی metrics-server](https://github.com/kubernetes-sigs/metrics-server/blob/master/KNOWN_ISSUES.md)
* [انتشارهای metrics-server](https://github.com/kubernetes-sigs/metrics-server/releases)
* [مقیاس‌دهی خودکار افقی پادها](/docs/tasks/run-application/horizontal-pod-autoscale/)

برای آشنایی با نحوه‌ی ارائه‌ی متریک‌های نود توسط kubelet و چگونگی دسترسی به آن‌ها از طریق API کوبرنتیز، [داده‌های متریک نود](/docs/reference/instrumentation/node-metrics) را مطالعه کنید.
