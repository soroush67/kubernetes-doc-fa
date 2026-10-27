---
title: مشاهده‌پذیری
reviewers:
weight: 55
content_type: concept
description: >
  با نحوه‌ی دستیابی به دید سرتاسری نسبت به یک کلاستر کوبرنتیز از طریق گردآوری متریک‌ها، لاگ‌ها و ردگیری‌ها (traces) آشنا شوید.
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
    title: ردگیری‌ها
---

<!-- overview -->

در کوبرنتیز، مشاهده‌پذیری (observability) فرایند گردآوری و تحلیل متریک‌ها، لاگ‌ها و ردگیری‌ها (traces) است که اغلب از آن‌ها با عنوان سه ستون مشاهده‌پذیری یاد می‌شود. هدف از این فرایند، درک بهتر وضعیت داخلی، کارایی و سلامت کلاستر است.

اجزای control plane کوبرنتیز و همچنین بسیاری از افزونه‌ها (add-ons) این سیگنال‌ها را تولید و منتشر می‌کنند. با تجمیع و همبسته‌سازی آن‌ها می‌توانید تصویری یکپارچه از control plane، افزونه‌ها و برنامه‌ها در سراسر کلاستر به دست آورید.

شکل ۱ نشان می‌دهد اجزای کلاستر چگونه سه نوع اصلی سیگنال را منتشر می‌کنند.

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

*شکل ۱. سیگنال‌های سطح بالایی که اجزای کلاستر منتشر می‌کنند و مصرف‌کنندگان آن‌ها.*

<!-- body -->
## متریک‌ها {#metrics}

اجزای کوبرنتیز متریک‌ها را با [قالب Prometheus](https://prometheus.io/docs/instrumenting/exposition_formats/) از طریق endpointهای `/metrics` خود منتشر می‌کنند. این اجزا شامل موارد زیر هستند:

- kube-controller-manager
- kube-proxy
- kube-apiserver
- kube-scheduler
- kubelet

kubelet همچنین متریک‌ها را در `/metrics/cadvisor`، `/metrics/resource` و `/metrics/probes` در دسترس قرار می‌دهد، و افزونه‌هایی مانند [kube-state-metrics](/docs/concepts/cluster-administration/kube-state-metrics/) این سیگنال‌های control plane را با وضعیت آبجکت‌های کوبرنتیز غنی می‌کنند.

یک پایپ‌لاین متریک معمول در کوبرنتیز به‌صورت دوره‌ای این endpointها را scrape می‌کند و نمونه‌ها را در یک پایگاه داده‌ی سری زمانی (برای مثال با Prometheus) ذخیره می‌کند.

برای جزئیات و گزینه‌های پیکربندی، [راهنمای متریک‌های سیستمی](/docs/concepts/cluster-administration/system-metrics/) را ببینید.

شکل ۲ یک پایپ‌لاین متریک رایج در کوبرنتیز را نشان می‌دهد.

{{< mermaid >}}
flowchart LR
    C[Cluster components] --> P[Prometheus scraper]
    P --> TS[(Time series storage)]
    TS --> D[Dashboards and alerts]
    TS --> A[Automated actions]
{{< /mermaid >}}

*شکل ۲. اجزای یک پایپ‌لاین متریک معمول در کوبرنتیز.*

برای دید چندکلاستری یا چندابری، پایگاه‌های داده‌ی سری زمانی توزیع‌شده (برای مثال Thanos یا Cortex) می‌توانند مکمل Prometheus باشند.

برای مشاهده‌ی scraperهای متریک و پایگاه‌های داده‌ی سری زمانی، [ابزارهای رایج مشاهده‌پذیری - ابزارهای متریک](#metrics-tools) را ببینید.

### Metrics API

{{< feature-state for_k8s_version="v1.37" state="stable" >}}

Metrics API کوبرنتیز میزان مصرف منابع CPU و حافظه را برای نودها و Podها فراهم می‌کند. دستور
`kubectl top` و اجزایی مانند
[HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
و [VerticalPodAutoscaler](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
از این API استفاده می‌کنند.

`kubectl top` هر دو نسخه‌ی `metrics.k8s.io/v1` و `metrics.k8s.io/v1beta1` را پشتیبانی می‌کند. این دستور در صورت در دسترس بودن، نسخه‌ی `v1` را ترجیح می‌دهد و در غیر این صورت به `v1beta1` بازمی‌گردد. در کوبرنتیز v1.37، کنترل‌کننده‌ی HorizontalPodAutoscaler فقط از `metrics.k8s.io/v1beta1` پشتیبانی می‌کند؛ پشتیبانی از `metrics.k8s.io/v1` برنامه‌ریزی شده است، اما هنوز در دسترس نیست.

برخلاف endpointهای متریک اجزا که پیش‌تر توضیح داده شد، Metrics API از طریق
[لایه‌ی تجمیع API](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) کوبرنتیز ارائه می‌شود.
کلاستر شما باید [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) یا پیاده‌سازی دیگری را که این API را فراهم می‌کند اجرا کند. Metrics API عمداً فقط متریک‌های منابعِ موردنیاز برای مقیاس‌گذاری خودکار و بررسی‌های پایه را فراهم می‌کند؛ این API جایگزین یک پایپ‌لاین پایش کامل نیست.

برای آشنایی با این API، پیاده‌سازی‌های آن و جریان داده از kubeletها به کلاینت‌های آن،
[پایپ‌لاین متریک‌های منابع](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/) را ببینید.

#### {{% heading "seealso" %}}

- [متریک‌های سیستمی برای اجزای کوبرنتیز](/docs/concepts/cluster-administration/system-metrics/)
- [پایش مصرف منابع با metrics-server](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
- [مفهوم kube-state-metrics](/docs/concepts/cluster-administration/kube-state-metrics/)

## لاگ‌ها {#logs}

لاگ‌ها یک سابقه‌ی زمانی از رویدادها را در برنامه‌ها، اجزای سیستمی کوبرنتیز و فعالیت‌های مرتبط با امنیت، مانند ثبت رویدادهای ممیزی (audit logging)، فراهم می‌کنند.

container runtimeها خروجی برنامه‌ی کانتینری را از جریان‌های خروجی استاندارد (`stdout`) و خطای استاندارد (`stderr`) دریافت می‌کنند. اگرچه runtimeها این کار را به شیوه‌های متفاوتی پیاده‌سازی می‌کنند، یکپارچگی با kubelet از طریق _قالب لاگ CRI_ استاندارد شده است و kubelet این لاگ‌ها را از طریق `kubectl logs` در دسترس قرار می‌دهد.

![لاگ‌گیری در سطح نود](/images/docs/user-guide/logging/logging-node-level.png)

*شکل ۳الف. معماری لاگ‌گیری در سطح نود.*

لاگ‌های اجزای سیستمی، رویدادهای کلاستر را ثبت می‌کنند و اغلب برای اشکال‌زدایی و عیب‌یابی مفیدند. این اجزا به دو دسته تقسیم می‌شوند: اجزایی که در کانتینر اجرا می‌شوند و اجزایی که در کانتینر اجرا نمی‌شوند. برای مثال، `kube-scheduler` و `kube-proxy` معمولاً در کانتینر اجرا می‌شوند، در حالی که `kubelet` و container runtime مستقیماً روی میزبان اجرا می‌شوند.

- روی ماشین‌هایی که `systemd` دارند، kubelet و container runtime در journald می‌نویسند. در غیر این صورت، در فایل‌های `.log` در مسیر `/var/log` می‌نویسند.
- اجزای سیستمی که درون کانتینر اجرا می‌شوند، همواره در فایل‌های `.log` در `/var/log` می‌نویسند و سازوکار پیش‌فرض لاگ‌گیری کانتینر را دور می‌زنند.

لاگ‌های اجزای سیستمی و کانتینرها که در `/var/log` ذخیره می‌شوند، برای جلوگیری از رشد کنترل‌نشده نیازمند چرخش لاگ (log rotation) هستند. برخی اسکریپت‌های آماده‌سازی کلاستر به‌صورت پیش‌فرض چرخش لاگ را نصب می‌کنند؛ محیط خود را بررسی کنید و در صورت نیاز آن را تنظیم نمایید. برای جزئیات مربوط به مسیرها، قالب‌ها و گزینه‌های پیکربندی، [مرجع لاگ‌های سیستمی](/docs/concepts/cluster-administration/system-logs/) را ببینید.

بیشتر کلاسترها یک عامل لاگ‌گیری در سطح نود (برای مثال Fluent Bit یا Fluentd) اجرا می‌کنند که این فایل‌ها را دنبال می‌کند و ورودی‌ها را به یک مخزن مرکزی لاگ ارسال می‌کند. [راهنمای معماری لاگ‌گیری](/docs/concepts/cluster-administration/logging/) توضیح می‌دهد چگونه چنین پایپ‌لاین‌هایی را طراحی کنید، نگهداری (retention) را اعمال کنید و جریان لاگ‌ها را به backendها هدایت نمایید.

شکل ۳ یک پایپ‌لاین رایج تجمیع لاگ را نشان می‌دهد.

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

*شکل ۳. اجزای یک پایپ‌لاین لاگ معمول در کوبرنتیز.*

برای مشاهده‌ی عامل‌های لاگ‌گیری و مخازن مرکزی لاگ، [ابزارهای رایج مشاهده‌پذیری - ابزارهای لاگ‌گیری](#logging-tools) را ببینید.

#### {{% heading "seealso" %}}

- [معماری لاگ‌گیری](/docs/concepts/cluster-administration/logging/)
- [لاگ‌های سیستمی](/docs/concepts/cluster-administration/system-logs/)
- [وظایف و آموزش‌های لاگ‌گیری](/docs/tasks/debug/logging/)
- [پیکربندی audit logging](/docs/tasks/debug/debug-cluster/audit/)

## ردگیری‌ها {#traces}

ردگیری‌ها (traces) نشان می‌دهند درخواست‌ها چگونه میان اجزای کوبرنتیز و برنامه‌ها حرکت می‌کنند و تأخیر، زمان‌بندی و روابط میان عملیات را به هم پیوند می‌دهند. با گردآوری ردگیری‌ها می‌توانید جریان سرتاسری درخواست را مصور کنید، مشکلات کارایی را تشخیص دهید و گلوگاه‌ها یا تعامل‌های غیرمنتظره را در control plane، افزونه‌ها یا برنامه‌ها شناسایی کنید.

کوبرنتیز {{< skew currentVersion >}} می‌تواند spanها را از طریق [OpenTelemetry Protocol](/docs/concepts/cluster-administration/system-traces/) (OTLP) صادر کند، یا مستقیماً با exporterهای gRPC داخلی یا با ارسال آن‌ها از طریق یک OpenTelemetry Collector.

OpenTelemetry Collector، spanها را از اجزا و برنامه‌ها دریافت می‌کند، آن‌ها را پردازش می‌کند (برای مثال با اعمال نمونه‌برداری یا حذف داده‌های حساس) و برای ذخیره‌سازی و تحلیل به یک backend ردگیری ارسال می‌کند.

شکل ۴ یک پایپ‌لاین ردگیری توزیع‌شده‌ی معمول را نشان می‌دهد.

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

*شکل ۴. اجزای یک پایپ‌لاین ردگیری معمول در کوبرنتیز.*

برای مشاهده‌ی collectorها و backendهای ردگیری، [ابزارهای رایج مشاهده‌پذیری - ابزارهای ردگیری](#tracing-tools) را ببینید.

#### {{% heading "seealso" %}}

- [ردگیری‌های سیستمی برای اجزای کوبرنتیز](/docs/concepts/cluster-administration/system-traces/)
- [راهنمای شروع کار با OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started/)
- [وظایف پایش و ردگیری](/docs/tasks/debug/monitoring/)

## ابزارهای رایج مشاهده‌پذیری {#common-observability-tools}

{{% thirdparty-content %}}

نکته: این بخش به پروژه‌های شخص ثالثی پیوند می‌دهد که قابلیت‌های مشاهده‌پذیری موردنیاز کوبرنتیز را فراهم می‌کنند.
نویسندگان پروژه‌ی کوبرنتیز مسئول این پروژه‌ها نیستند و آن‌ها به ترتیب حروف الفبای انگلیسی فهرست شده‌اند. برای افزودن یک
پروژه به این فهرست، پیش از ارسال تغییر، [راهنمای محتوا](/docs/contribute/style/content-guide/) را مطالعه کنید.

### ابزارهای متریک {#metrics-tools}

- [Cortex](https://cortexmetrics.io/) ذخیره‌سازی بلندمدت Prometheus را با قابلیت مقیاس‌پذیری افقی ارائه می‌دهد.
- [Grafana Mimir](https://grafana.com/oss/mimir/) پروژه‌ای از Grafana Labs است که ذخیره‌سازی چندمستاجری (multi-tenant) و مقیاس‌پذیر افقی سازگار با Prometheus را فراهم می‌کند.
- [Prometheus](https://prometheus.io/) سامانه‌ی پایشی است که متریک‌ها را از اجزای کوبرنتیز scrape و ذخیره می‌کند.
- [Thanos](https://thanos.io/) با کوئری سراسری، کاهش نمونه‌برداری (downsampling) و پشتیبانی از ذخیره‌سازی شیء (object storage)، Prometheus را گسترش می‌دهد.

### ابزارهای لاگ‌گیری {#logging-tools}

- [Elasticsearch](https://www.elastic.co/elasticsearch/) نمایه‌سازی و جستجوی توزیع‌شده‌ی لاگ را فراهم می‌کند.
- [Fluent Bit](https://fluentbit.io/) لاگ‌های کانتینر و نود را با مصرف منابع کم گردآوری و ارسال می‌کند.
- [Fluentd](https://www.fluentd.org/) لاگ‌ها را به مقصدهای متعدد مسیریابی و تبدیل می‌کند.
- [Grafana Loki](https://grafana.com/oss/loki/) لاگ‌ها را در قالبی مبتنی بر برچسب و الهام‌گرفته از Prometheus ذخیره می‌کند.
- [OpenSearch](https://opensearch.org/) نمایه‌سازی و جستجوی متن‌باز لاگ را فراهم می‌کند که با APIهای Elasticsearch سازگار است.

### ابزارهای ردگیری {#tracing-tools}

- [Grafana Tempo](https://grafana.com/oss/tempo/) ذخیره‌سازی مقیاس‌پذیر و کم‌هزینه‌ی ردگیری توزیع‌شده را ارائه می‌دهد.
- [Jaeger](https://www.jaegertracing.io/) ردگیری‌های توزیع‌شده‌ی میکروسرویس‌ها را گردآوری و مصور می‌کند.
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) داده‌های تله‌متری، از جمله ردگیری‌ها، را دریافت، پردازش و صادر می‌کند.
- [Zipkin](https://zipkin.io/) گردآوری و مصورسازی ردگیری توزیع‌شده را فراهم می‌کند.

## {{% heading "whatsnext" %}}

- یاد بگیرید چگونه [متریک‌های مصرف منابع را با metrics-server گردآوری کنید](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
- [وظایف و آموزش‌های لاگ‌گیری](/docs/tasks/debug/logging/) را بررسی کنید
- [راهنمای وظایف پایش و ردگیری](/docs/tasks/debug/monitoring/) را دنبال کنید
- برای endpointهای اجزا و پایداری آن‌ها، [راهنمای متریک‌های سیستمی](/docs/concepts/cluster-administration/system-metrics/) را مرور کنید
- بخش [ابزارهای رایج مشاهده‌پذیری](#common-observability-tools) را برای گزینه‌های شخص ثالثِ بررسی‌شده مرور کنید
