---
reviewers:
- logicalhan
title: معیارهای SLI مؤلفه‌های کوبرنتیز
linkTitle: معیارهای شاخص سطح سرویس
content_type: reference
weight: 20
description: >-
  شاخص‌هایی سطح بالا برای سنجش قابلیت اطمینان و کارایی مؤلفه‌های کوبرنتیز.
---

<!-- overview -->

{{< feature-state feature_gate_name="ComponentSLIs" >}}

کوبرنتیز {{< skew currentVersion >}} به‌طور پیش‌فرض برای هر فایل اجرایی (binary) مؤلفه‌های کوبرنتیز، معیارهای شاخص سطح سرویس (Service Level Indicator یا SLI) را منتشر می‌کند. این نقطهٔ پایانی معیارها روی پورت HTTPS سرویس‌دهی هر مؤلفه و در مسیر `/metrics/slis` در دسترس قرار می‌گیرد. از نسخهٔ v1.27، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ComponentSLIs` برای همهٔ مؤلفه‌های کوبرنتیز به‌طور پیش‌فرض فعال است.

<!-- body -->

## معیارهای SLI

با فعال بودن معیارهای SLI، هر مؤلفهٔ کوبرنتیز دو معیار را در دسترس قرار می‌دهد که برای هر بررسی سلامت (healthcheck) برچسب‌گذاری شده‌اند:

- یک گیج (gauge) که وضعیت فعلی بررسی سلامت را نشان می‌دهد
- یک شمارنده (counter) که تعداد تجمعی مشاهده‌شده برای هر وضعیت بررسی سلامت را ثبت می‌کند

با استفاده از اطلاعات این معیارها می‌توانید آمار دسترس‌پذیری هر مؤلفه را محاسبه کنید. برای مثال، API server سلامت etcd را بررسی می‌کند. بر این اساس می‌توانید میزان دسترس‌پذیر یا دسترس‌ناپذیر بودن etcd را، آن‌گونه که کلاینت آن یعنی API server گزارش کرده است، محاسبه و گزارش کنید.


داده‌های گیج Prometheus به این شکل است:

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

در حالی که داده‌های شمارنده به این شکل است:

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

## استفاده از این داده‌ها

نقطهٔ پایانی معیارهای SLI مؤلفه‌ها برای جمع‌آوری (scrape) با بسامد بالا طراحی شده است. جمع‌آوری با بسامد بالا باعث می‌شود سیگنال گیج با جزئیات دقیق‌تری به دست آید و سپس بتوان از آن برای محاسبهٔ SLOها استفاده کرد. نقطهٔ پایانی `/metrics/slis` داده‌های خام لازم برای محاسبهٔ SLO دسترس‌پذیری مؤلفهٔ مربوط در کوبرنتیز را فراهم می‌کند.
