---
title: ردگیری (Trace) اجزای سیستم کوبرنتیز
reviewers:
- logicalhan
- lilic
content_type: concept
weight: 90
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.27" state="beta" >}}

ردگیری‌های (traces) اجزای سیستم، تأخیر عملیات در کلاستر و روابط میان آن‌ها را ثبت می‌کنند.

اجزای کوبرنتیز ردگیری‌ها را با استفاده از
[پروتکل OpenTelemetry](https://opentelemetry.io/docs/specs/otlp/)
و صادرکنندهٔ gRPC منتشر می‌کنند و می‌توان آن‌ها را با استفاده از یک
[OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector#-opentelemetry-collector) گردآوری کرد و به پشتوانه‌های (backends) ردگیری هدایت کرد.

<!-- body -->

## گردآوری ردگیری‌ها

اجزای کوبرنتیز دارای صادرکننده‌های gRPC داخلی برای OTLP هستند تا ردگیری‌ها را صادر کنند، چه با یک OpenTelemetry Collector
و چه بدون آن.

برای راهنمای کامل گردآوری ردگیری‌ها و استفاده از collector، 
[شروع کار با OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started/) را ببینید.
با این حال، چند نکتهٔ خاص اجزای کوبرنتیز وجود دارد که باید به آن‌ها توجه کرد.

به‌طور پیش‌فرض، اجزای کوبرنتیز ردگیری‌ها را با استفاده از صادرکنندهٔ grpc برای OTLP روی
[پورت IANA مربوط به OpenTelemetry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=opentelemetry)، یعنی 4317، صادر می‌کنند.
برای نمونه، اگر collector به‌صورت sidecar در کنار یک جزء کوبرنتیز اجرا شود،
پیکربندی گیرندهٔ زیر spanها را گردآوری کرده و آن‌ها را در خروجی استاندارد لاگ می‌کند:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
exporters:
  # Replace this exporter with the exporter for your backend
  exporters:
    debug:
      verbosity: detailed
service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [debug]
```

برای ارسال مستقیم ردگیری‌ها به یک پشتوانه بدون استفاده از collector،
فیلد endpoint را در فایل پیکربندی ردگیری کوبرنتیز با نشانی پشتوانهٔ ردگیری مورد نظر مشخص کنید.
این روش نیاز به collector را از میان می‌برد و ساختار کلی را ساده‌تر می‌کند.

برای پیکربندی سرآیندهای (headers) پشتوانهٔ ردگیری، از جمله جزئیات احراز هویت، می‌توان از متغیرهای محیطی با `OTEL_EXPORTER_OTLP_HEADERS` استفاده کرد؛
[پیکربندی OTLP Exporter](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/) را ببینید.

افزون بر این، برای پیکربندی ویژگی‌های منبع ردگیری مانند نام کلاستر کوبرنتیز، فضای نام، نام Pod و غیره،
می‌توان از متغیرهای محیطی با `OTEL_RESOURCE_ATTRIBUTES` نیز استفاده کرد؛ [OTLP Kubernetes Resource](https://opentelemetry.io/docs/specs/semconv/resource/k8s/) را ببینید.

## ردگیری‌های اجزا

### ردگیری‌های kube-apiserver

kube-apiserver برای درخواست‌های HTTP ورودی، و برای درخواست‌های خروجی
به webhookها، etcd و درخواست‌های بازگشتی (re-entrant)، span تولید می‌کند. این جزء
[W3C Trace Context](https://www.w3.org/TR/trace-context/) را همراه درخواست‌های خروجی منتشر می‌کند،
اما از زمینهٔ ردگیری (trace context) پیوست‌شده به درخواست‌های ورودی استفاده نمی‌کند،
زیرا kube-apiserver اغلب یک endpoint عمومی است.

#### فعال‌سازی ردگیری در kube-apiserver

برای فعال‌سازی ردگیری، یک فایل پیکربندی ردگیری را با
`--tracing-config-file=<path-to-config>` به kube-apiserver بدهید. این یک پیکربندی نمونه است که
spanها را برای ۱ درخواست از هر ۱۰۰۰۰ درخواست ثبت می‌کند و از endpoint پیش‌فرض OpenTelemetry استفاده می‌کند:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: TracingConfiguration
# default value
#endpoint: localhost:4317
samplingRatePerMillion: 100
```

برای اطلاعات بیشتر دربارهٔ ساختار `TracingConfiguration`،
[API پیکربندی سرور API (v1)](/docs/reference/config-api/apiserver-config.v1/#apiserver-k8s-io-v1-TracingConfiguration) را ببینید.

### ردگیری‌های kubelet

{{< feature-state feature_gate_name="KubeletTracing" >}}

واسط CRI در kubelet و سرورهای http احراز هویت‌شدهٔ آن برای تولید
spanهای ردگیری ابزارگذاری (instrument) شده‌اند. همانند apiserver، endpoint و نرخ نمونه‌برداری قابل پیکربندی‌اند.
انتشار زمینهٔ ردگیری نیز پیکربندی شده است. تصمیم نمونه‌برداری یک span والد همیشه رعایت می‌شود.
نرخ نمونه‌برداری ارائه‌شده در پیکربندی ردگیری برای spanهای بدون والد اعمال می‌شود.
اگر ردگیری بدون endpoint پیکربندی‌شده فعال شود، نشانی پیش‌فرض گیرندهٔ OpenTelemetry Collector یعنی "localhost:4317" تنظیم می‌شود.

#### فعال‌سازی ردگیری در kubelet

برای فعال‌سازی ردگیری، [پیکربندی ردگیری](https://github.com/kubernetes/component-base/blob/release-1.27/tracing/api/v1/types.go) را اعمال کنید.
این قطعه‌ای نمونه از پیکربندی kubelet است که spanها را برای ۱ درخواست از هر ۱۰۰۰۰ درخواست ثبت می‌کند و از endpoint پیش‌فرض OpenTelemetry استفاده می‌کند:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
tracing:
  # default value
  #endpoint: localhost:4317
  samplingRatePerMillion: 100
```

اگر `samplingRatePerMillion` روی یک میلیون (`1000000`) تنظیم شود، هر
span به صادرکننده ارسال خواهد شد.

kubelet در کوبرنتیز v{{< skew currentVersion >}} spanها را از
زباله‌روبی (garbage collection)، روال همگام‌سازی Pod و همچنین هر متد gRPC
گردآوری می‌کند. kubelet زمینهٔ ردگیری را همراه درخواست‌های gRPC منتشر می‌کند تا
زمان‌های اجرای کانتینری که ابزارگذاری ردگیری دارند، مانند CRI-O و containerd،
بتوانند spanهای صادرشدهٔ خود را با زمینهٔ ردگیری kubelet مرتبط کنند.
ردگیری‌های حاصل دارای پیوندهای والد-فرزند میان spanهای kubelet و
زمان اجرای کانتینر خواهند بود که هنگام اشکال‌زدایی مشکلات نود
زمینهٔ سودمندی فراهم می‌کند.

لطفاً توجه داشته باشید که صادر کردن spanها همیشه با سربار کارایی اندکی
در بخش شبکه و CPU همراه است که به پیکربندی کلی
سیستم بستگی دارد. اگر چنین مشکلی در کلاستری که ردگیری در آن فعال است
رخ دهد، مشکل را با کاهش
`samplingRatePerMillion` یا غیرفعال کردن کامل ردگیری با حذف
پیکربندی برطرف کنید.

## پایداری

ابزارگذاری ردگیری هنوز در حال توسعهٔ فعال است و ممکن است
به شیوه‌های گوناگونی تغییر کند. این شامل نام spanها، ویژگی‌های پیوست‌شده،
endpointهای ابزارگذاری‌شده و غیره است. تا زمانی که این قابلیت به وضعیت پایدار ارتقا نیابد،
هیچ تضمینی برای سازگاری رو به عقب ابزارگذاری ردگیری وجود ندارد.

## {{% heading "whatsnext" %}}

* دربارهٔ [شروع کار با OpenTelemetry Collector](https://opentelemetry.io/docs/collector/getting-started/) بخوانید
* دربارهٔ [پیکربندی OTLP Exporter](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/) بخوانید
