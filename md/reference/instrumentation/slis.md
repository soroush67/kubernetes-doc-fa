---
reviewers:
- logicalhan
title: معیارهای SLI اجزای کوبرنتیز
linkTitle: معیارهای شاخص سطح خدمت (SLI)
content_type: reference
weight: 20
description: >-
  شاخص‌های سطح بالا برای سنجش قابلیت اطمینان و کارایی اجزای کوبرنتیز.
---

<!-- overview -->

{{< feature-state feature_gate_name="ComponentSLIs" >}}

به‌طور پیش‌فرض، کوبرنتیز {{< skew currentVersion >}} معیارهای شاخص سطح خدمت (Service Level Indicator یا SLI) را
برای فایل اجرایی هر یک از اجزای کوبرنتیز منتشر می‌کند. این نقطه پایانی (endpoint) معیارها روی
پورت HTTPS سرویس‌دهی هر جزء و در مسیر `/metrics/slis` در دسترس قرار می‌گیرد.
[Feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام
`ComponentSLIs` از نسخه v1.27 به‌صورت پیش‌فرض برای هر جزء کوبرنتیز فعال است.

<!-- body -->

## معیارهای SLI {#sli-metrics}

با فعال بودن معیارهای SLI، هر جزء کوبرنتیز دو معیار را
به‌ازای هر بررسی سلامت (healthcheck) و با برچسب مربوط به آن ارائه می‌کند:

- یک gauge (که وضعیت فعلی بررسی سلامت را نشان می‌دهد)
- یک counter (که تعداد تجمعیِ مشاهده‌شده برای هر وضعیت بررسی سلامت را ثبت می‌کند)

می‌توانید از اطلاعات این معیارها برای محاسبه آمار دسترس‌پذیری هر جزء استفاده کنید.
برای مثال، API server سلامت etcd را بررسی می‌کند. شما می‌توانید محاسبه و گزارش کنید که etcd
از دید کلاینت خود، یعنی API server، چقدر در دسترس یا ناavailable بوده است.


داده‌های gauge در prometheus به این شکل است:

```
# HELP kubernetes_healthcheck [ALPHA] This metric records the result of a single healthcheck.
# TYPE kubernetes_healthcheck gauge
kubernetes_healthcheck{name="autoregister-completion",type="healthz"} 1
kubernetes_healthcheck{name="autoregister-completion",type="readyz"} 1
kubernetes_healthcheck{name="etcd",type="healthz"} 1
kubernetes_healthcheck{name="etcd",type="readyz"} 1
kubernetes_healthcheck{name="etcd-readiness",type="readyz"} 1
kubernetes_healthcheck{name="informer-sync",type="readyz"} 1
kubernetes_healthcheck{name="log",type="healthz"} 1
kubernetes_healthcheck{name="log",type="readyz"} 1
kubernetes_healthcheck{name="ping",type="healthz"} 1
kubernetes_healthcheck{name="ping",type="readyz"} 1
```

و داده‌های counter به این شکل است:

```
# HELP kubernetes_healthchecks_total [ALPHA] This metric records the results of all healthcheck.
# TYPE kubernetes_healthchecks_total counter
kubernetes_healthchecks_total{name="autoregister-completion",status="error",type="readyz"} 1
kubernetes_healthchecks_total{name="autoregister-completion",status="success",type="healthz"} 15
kubernetes_healthchecks_total{name="autoregister-completion",status="success",type="readyz"} 14
kubernetes_healthchecks_total{name="etcd",status="success",type="healthz"} 15
kubernetes_healthchecks_total{name="etcd",status="success",type="readyz"} 15
kubernetes_healthchecks_total{name="etcd-readiness",status="success",type="readyz"} 15
kubernetes_healthchecks_total{name="informer-sync",status="error",type="readyz"} 1
kubernetes_healthchecks_total{name="informer-sync",status="success",type="readyz"} 14
kubernetes_healthchecks_total{name="log",status="success",type="healthz"} 15
kubernetes_healthchecks_total{name="log",status="success",type="readyz"} 15
kubernetes_healthchecks_total{name="ping",status="success",type="healthz"} 15
kubernetes_healthchecks_total{name="ping",status="success",type="readyz"} 15
```

## استفاده از این داده‌ها {#using-this-data}

نقطه پایانی معیارهای SLI اجزا برای جمع‌آوری (scrape) با فرکانس بالا طراحی شده است. جمع‌آوری
با فرکانس بالا به این معناست که سیگنال gauge با جزئیات (granularity) بیشتری در اختیار شما قرار می‌گیرد و
می‌توان از آن برای محاسبه SLOها استفاده کرد. نقطه پایانی `/metrics/slis` داده‌های خام لازم را
برای محاسبه SLO دسترس‌پذیری جزء مربوط در کوبرنتیز فراهم می‌کند.
