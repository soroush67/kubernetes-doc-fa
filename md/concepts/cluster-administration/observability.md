---
title: مشاهده‌پذیری
reviewers:
weight: 55
content_type: concept
description: >
  با نحوهٔ دستیابی به دید سرتاسری از یک کلاستر کوبرنتیز از طریق گردآوری متریک‌ها، لاگ‌ها و ردها آشنا شوید.
api_metadata:
- apiVersion: "metrics.k8s.io/v1"
  kind: "NodeMetrics"
- apiVersion: "metrics.k8s.io/v1"
  kind: "PodMetrics"
no_list: true
card:
  name: setup
  weight: 60
  anchors:
  - anchor: "#metrics"
    title: متریک‌ها
  - anchor: "#logs"
    title: لاگ‌ها
  - anchor: "#traces"
    title: ردها
---

<!-- overview -->

در کوبرنتیز، مشاهده‌پذیری (observability) فرایند گردآوری و تحلیل متریک‌ها، لاگ‌ها و ردهاست. این سه معمولاً سه ستون مشاهده‌پذیری نامیده می‌شوند و هدف از گردآوری آن‌ها، درک بهتر وضعیت درونی، کارایی و سلامت کلاستر است.

مؤلفه‌های control plane کوبرنتیز و بسیاری از افزونه‌ها این سیگنال‌ها را تولید و منتشر می‌کنند. با تجمیع این سیگنال‌ها و یافتن ارتباط میان آن‌ها، می‌توانید تصویری یکپارچه از control plane، افزونه‌ها و برنامه‌ها در سراسر کلاستر به دست آورید.

شکل ۱ نشان می‌دهد که مؤلفه‌های کلاستر چگونه سه نوع اصلی سیگنال را منتشر می‌کنند.

{{< mermaid >}}
flowchart LR
    A[Cluster components] --> M[Metrics pipeline]
    A --> L[Log pipeline]
    A --> T[Trace pipeline]
    M --> S[(Storage and analysis)]
    L --> S
    T --> S
    S --> O[Operators and automation]
{{< /mermaid >}}

*شکل ۱. نمای کلی سیگنال‌های منتشرشده از مؤلفه‌های کلاستر و مصرف‌کنندگان آن‌ها.*

<!-- body -->
## متریک‌ها

مؤلفه‌های کوبرنتیز متریک‌ها را با [قالب Prometheus](https://prometheus.io/docs/instrumenting/exposition_formats/) از طریق نقطهٔ پایانی `/metrics` خود منتشر می‌کنند. این مؤلفه‌ها عبارت‌اند از:

- kube-controller-manager
- kube-proxy
- kube-apiserver
- kube-scheduler
- kubelet

همچنین kubelet متریک‌هایی را در مسیرهای `/metrics/cadvisor`، `/metrics/resource` و `/metrics/probes` در دسترس قرار می‌دهد. افزونه‌هایی مانند [kube-state-metrics](/docs/concepts/cluster-administration/kube-state-metrics/) نیز این سیگنال‌های control plane را با اطلاعات وضعیت آبجکت‌های کوبرنتیز غنی‌تر می‌کنند.

یک خط لولهٔ متریک معمول در کوبرنتیز، این نقاط پایانی را به‌طور دوره‌ای جمع‌آوری (scrape) می‌کند و نمونه‌ها را در یک پایگاه دادهٔ سری زمانی ذخیره می‌کند (برای مثال با Prometheus).

برای جزئیات و گزینه‌های پیکربندی، [راهنمای متریک‌های سیستم](/docs/concepts/cluster-administration/system-metrics/) را ببینید.

شکل ۲ یک خط لولهٔ متریک رایج در کوبرنتیز را نشان می‌دهد.

{{< mermaid >}}
flowchart LR
    C[Cluster components] --> P[Prometheus scraper]
    P --> TS[(Time series storage)]
    TS --> D[Dashboards and alerts]
    TS --> A[Automated actions]
{{< /mermaid >}}

*شکل ۲. مؤلفه‌های یک خط لولهٔ متریک معمول در کوبرنتیز.*

برای دستیابی به دید چندکلاستری یا چندابری، می‌توان از پایگاه‌های دادهٔ سری زمانی توزیع‌شده (برای مثال Thanos یا Cortex) در کنار Prometheus استفاده کرد.

برای آشنایی با ابزارهای جمع‌آوری متریک و پایگاه‌های دادهٔ سری زمانی، بخش [ابزارهای رایج مشاهده‌پذیری - ابزارهای متریک](#metrics-tools) را ببینید.

### رابط Metrics API

{{< feature-state for_k8s_version="v1.37" state="stable" >}}

رابط Metrics API در کوبرنتیز، میزان مصرف منابع CPU و حافظه را برای نودها و Podها فراهم می‌کند. دستور
`kubectl top` و مؤلفه‌هایی مانند
[HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
و [VerticalPodAutoscaler](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
از این API استفاده می‌کنند.

دستور `kubectl top` از هر دو نسخهٔ `metrics.k8s.io/v1` و `metrics.k8s.io/v1beta1` پشتیبانی می‌کند. این دستور در صورت
در دسترس بودن نسخهٔ `v1` آن را ترجیح می‌دهد و در غیر این صورت به `v1beta1` بازمی‌گردد. در کوبرنتیز v1.37،
کنترل‌کنندهٔ HorizontalPodAutoscaler فقط از `metrics.k8s.io/v1beta1` پشتیبانی می‌کند؛ پشتیبانی از
`metrics.k8s.io/v1` برنامه‌ریزی شده است، اما هنوز در دسترس نیست.

برخلاف نقاط پایانی متریک مؤلفه‌ها که پیش‌تر توضیح داده شد، Metrics API از طریق
[لایهٔ تجمیع API](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) کوبرنتیز ارائه می‌شود.
کلاستر شما باید [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) یا پیاده‌سازی دیگری
را که این API را فراهم می‌کند اجرا کند. این API عمداً فقط متریک‌های منابعِ لازم برای مقیاس‌دهی خودکار
و بررسی‌های پایه را ارائه می‌دهد و جایگزینی برای یک خط لولهٔ پایش کامل نیست.

برای آشنایی با این API، پیاده‌سازی‌های آن و جریان داده از kubeletها به کلاینت‌های آن،
[خط لولهٔ متریک‌های منابع](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/) را ببینید.

#### {{% heading "seealso" %}}

- [متریک‌های سیستم برای مؤلفه‌های کوبرنتیز](/docs/concepts/cluster-administration/system-metrics/)
- [پایش مصرف منابع با metrics-server](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
- [مفهوم kube-state-metrics](/docs/concepts/cluster-administration/kube-state-metrics/)

## لاگ‌ها

لاگ‌ها سابقه‌ای زمانی از رویدادهای درون برنامه‌ها، مؤلفه‌های سیستمی کوبرنتیز و فعالیت‌های مرتبط با امنیت، مانند لاگ ممیزی (audit logging)، فراهم می‌کنند.

محیط‌های اجرای کانتینر، خروجی برنامهٔ کانتینری‌شده را از جریان‌های خروجی استاندارد (`stdout`) و خطای استاندارد (`stderr`) دریافت می‌کنند. هرچند هر محیط اجرا این کار را به شیوهٔ خود پیاده‌سازی می‌کند، یکپارچگی آن با kubelet از طریق _قالب لاگ CRI_ استاندارد شده است و kubelet این لاگ‌ها را از طریق `kubectl logs` در دسترس قرار می‌دهد.

![لاگ‌گیری در سطح نود](/images/docs/user-guide/logging/logging-node-level.png)

*شکل ۳الف. معماری لاگ‌گیری در سطح نود.*

لاگ‌های مؤلفه‌های سیستمی، رویدادهای کلاستر را ثبت می‌کنند و اغلب برای اشکال‌زدایی و عیب‌یابی مفیدند. این مؤلفه‌ها به دو دسته تقسیم می‌شوند: مؤلفه‌هایی که درون کانتینر اجرا می‌شوند و مؤلفه‌هایی که چنین نیستند. برای مثال، `kube-scheduler` و `kube-proxy` معمولاً درون کانتینر اجرا می‌شوند، در حالی که `kubelet` و محیط اجرای کانتینر مستقیماً روی میزبان اجرا می‌شوند.

- روی ماشین‌هایی که از `systemd` استفاده می‌کنند، kubelet و محیط اجرای کانتینر در journald می‌نویسند. در غیر این صورت، در فایل‌های `.log` در دایرکتوری `/var/log` می‌نویسند.
- مؤلفه‌های سیستمی که درون کانتینر اجرا می‌شوند همواره در فایل‌های `.log` در `/var/log` می‌نویسند و سازوکار پیش‌فرض لاگ‌گیری کانتینر را دور می‌زنند.

لاگ‌های مؤلفه‌های سیستمی و کانتینرها که در `/var/log` ذخیره می‌شوند، برای جلوگیری از رشد کنترل‌نشده به چرخش لاگ (log rotation) نیاز دارند. برخی اسکریپت‌های راه‌اندازی کلاستر، چرخش لاگ را به‌طور پیش‌فرض نصب می‌کنند؛ محیط خود را بررسی و در صورت نیاز آن را تنظیم کنید. برای جزئیات مربوط به مکان‌ها، قالب‌ها و گزینه‌های پیکربندی، [مرجع لاگ‌های سیستم](/docs/concepts/cluster-administration/system-logs/) را ببینید.

در بیشتر کلاسترها یک عامل لاگ‌گیری در سطح نود (برای مثال Fluent Bit یا Fluentd) اجرا می‌شود که این فایل‌ها را دنبال می‌کند و ورودی‌ها را به یک مخزن مرکزی لاگ ارسال می‌کند. [راهنمای معماری لاگ‌گیری](/docs/concepts/cluster-administration/logging/) توضیح می‌دهد که چگونه چنین خط لوله‌هایی را طراحی کنید، سیاست نگهداری را اعمال کنید و جریان‌های لاگ را به سامانه‌های پشتیبان بفرستید.

شکل ۳ یک خط لولهٔ رایج تجمیع لاگ را نشان می‌دهد.

{{< mermaid >}}
flowchart LR
    subgraph Sources
        A[Application stdout / stderr]
        B[Control plane logs]
        C[Audit records]
    end
    A --> N[Node log agent]
    B --> N
    C --> N
    N --> L[Central log store]
    L --> Q[Dashboards, alerting, SIEM]
{{< /mermaid >}}

*شکل ۳. مؤلفه‌های یک خط لولهٔ لاگ معمول در کوبرنتیز.*

برای آشنایی با عامل‌های لاگ‌گیری و مخازن مرکزی لاگ، بخش [ابزارهای رایج مشاهده‌پذیری - ابزارهای لاگ‌گیری](#logging-tools) را ببینید.

#### {{% heading "seealso" %}}

- [معماری لاگ‌گیری](/docs/concepts/cluster-administration/logging/)
- [لاگ‌های سیستم](/docs/concepts/cluster-administration/system-logs/)
- [وظایف و آموزش‌های لاگ‌گیری](/docs/tasks/debug/logging/)
- [پیکربندی لاگ ممیزی](/docs/tasks/debug/debug-cluster/audit/)

## ردها

ردها (traces) نشان می‌دهند که درخواست‌ها چگونه میان مؤلفه‌ها و برنامه‌های کوبرنتیز جابه‌جا می‌شوند و تأخیر، زمان‌بندی و روابط میان عملیات‌ها را به یکدیگر پیوند می‌دهند. با گردآوری ردها می‌توانید جریان سرتاسری درخواست‌ها را به‌صورت بصری مشاهده کنید، مشکلات کارایی را تشخیص دهید و گلوگاه‌ها یا تعامل‌های غیرمنتظره را در control plane، افزونه‌ها یا برنامه‌ها شناسایی کنید.

کوبرنتیز {{< skew currentVersion >}} می‌تواند spanها را از طریق [پروتکل OpenTelemetry](/docs/concepts/cluster-administration/system-traces/) (OTLP) صادر کند؛ این کار یا مستقیماً با صادرکننده‌های gRPC داخلی انجام می‌شود یا با ارسال آن‌ها از طریق یک OpenTelemetry Collector.

ابزار OpenTelemetry Collector، spanها را از مؤلفه‌ها و برنامه‌ها دریافت می‌کند، آن‌ها را پردازش می‌کند (برای مثال با اعمال نمونه‌برداری یا حذف اطلاعات حساس) و برای ذخیره‌سازی و تحلیل به یک سامانهٔ پشتیبان ردیابی ارسال می‌کند.

شکل ۴ یک خط لولهٔ معمول ردیابی توزیع‌شده را نشان می‌دهد.

{{< mermaid >}}
flowchart LR
    subgraph Sources
        A[Control plane spans]
        B[Application spans]
    end
    A --> X[OTLP exporter]
    B --> X
    X --> COL[OpenTelemetry Collector]
    COL --> TS[(Tracing backend)]
    TS --> V[Visualization and analysis]
{{< /mermaid >}}

*شکل ۴. مؤلفه‌های یک خط لولهٔ ردیابی معمول در کوبرنتیز.*

برای آشنایی با گردآورنده‌ها و سامانه‌های پشتیبان ردیابی، بخش [ابزارهای رایج مشاهده‌پذیری - ابزارهای ردیابی](#tracing-tools) را ببینید.

#### {{% heading "seealso" %}}

- [ردهای سیستم برای مؤلفه‌های کوبرنتیز](/docs/concepts/cluster-administration/system-traces/)
- [راهنمای شروع کار با OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started/)
- [وظایف پایش و ردیابی](/docs/tasks/debug/monitoring/)

## ابزارهای رایج مشاهده‌پذیری

{{% thirdparty-content %}}

توجه: این بخش به پروژه‌های شخص ثالثی پیوند می‌دهد که قابلیت‌های مشاهده‌پذیری مورد نیاز کوبرنتیز را فراهم می‌کنند.
نویسندگان پروژهٔ کوبرنتیز مسئولیتی در قبال این پروژه‌ها ندارند و این پروژه‌ها به ترتیب الفبایی فهرست شده‌اند. برای افزودن
یک پروژه به این فهرست، پیش از ارسال تغییر، [راهنمای محتوا](/docs/contribute/style/content-guide/) را مطالعه کنید.

### ابزارهای متریک

- پروژهٔ [Cortex](https://cortexmetrics.io/) ذخیره‌سازی بلندمدت و مقیاس‌پذیر افقی برای Prometheus ارائه می‌دهد.
- پروژهٔ [Grafana Mimir](https://grafana.com/oss/mimir/) از Grafana Labs، ذخیره‌سازی چندمستأجری، مقیاس‌پذیر افقی و سازگار با Prometheus فراهم می‌کند.
- سامانهٔ [Prometheus](https://prometheus.io/) یک سامانهٔ پایش است که متریک‌ها را از مؤلفه‌های کوبرنتیز جمع‌آوری و ذخیره می‌کند.
- پروژهٔ [Thanos](https://thanos.io/) قابلیت‌های Prometheus را با پرس‌وجوی سراسری، کاهش نرخ نمونه‌برداری (downsampling) و پشتیبانی از ذخیره‌سازی آبجکت گسترش می‌دهد.

### ابزارهای لاگ‌گیری

- موتور [Elasticsearch](https://www.elastic.co/elasticsearch/) نمایه‌سازی و جست‌وجوی توزیع‌شدهٔ لاگ‌ها را فراهم می‌کند.
- ابزار [Fluent Bit](https://fluentbit.io/) لاگ‌های کانتینرها و نودها را با مصرف اندک منابع گردآوری و ارسال می‌کند.
- ابزار [Fluentd](https://www.fluentd.org/) لاگ‌ها را مسیریابی و تبدیل می‌کند و به مقصدهای متعدد می‌فرستد.
- سامانهٔ [Grafana Loki](https://grafana.com/oss/loki/) لاگ‌ها را در قالبی مبتنی بر برچسب و الهام‌گرفته از Prometheus ذخیره می‌کند.
- پروژهٔ [OpenSearch](https://opensearch.org/) نمایه‌سازی و جست‌وجوی متن‌باز لاگ‌ها را به‌صورت سازگار با APIهای Elasticsearch فراهم می‌کند.

### ابزارهای ردیابی

- سامانهٔ [Grafana Tempo](https://grafana.com/oss/tempo/) ذخیره‌سازی مقیاس‌پذیر و کم‌هزینه برای ردیابی توزیع‌شده ارائه می‌دهد.
- ابزار [Jaeger](https://www.jaegertracing.io/) ردهای توزیع‌شدهٔ ریزسرویس‌ها را ثبت و به‌صورت بصری نمایش می‌دهد.
- ابزار [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) داده‌های تله‌متری، از جمله ردها، را دریافت، پردازش و صادر می‌کند.
- سامانهٔ [Zipkin](https://zipkin.io/) امکان گردآوری و نمایش بصری ردهای توزیع‌شده را فراهم می‌کند.

## {{% heading "whatsnext" %}}

- با نحوهٔ [گردآوری متریک‌های مصرف منابع با metrics-server](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/) آشنا شوید.
- [وظایف و آموزش‌های لاگ‌گیری](/docs/tasks/debug/logging/) را بررسی کنید.
- [راهنماهای وظایف پایش و ردیابی](/docs/tasks/debug/monitoring/) را دنبال کنید.
- برای آشنایی با نقاط پایانی مؤلفه‌ها و پایداری آن‌ها، [راهنمای متریک‌های سیستم](/docs/concepts/cluster-administration/system-metrics/) را مرور کنید.
- برای گزینه‌های شخص ثالث بررسی‌شده، بخش [ابزارهای رایج مشاهده‌پذیری](#common-observability-tools) را مرور کنید.
