---
title: نقاط پایانی سلامت API کوبرنتیز
reviewers:
- logicalhan
content_type: concept
weight: 50
---

<!-- overview -->
{{< glossary_tooltip term_id="kube-apiserver" text="سرور API" >}} کوبرنتیز نقاط پایانی (endpoint) API‌ای را فراهم می‌کند که وضعیت فعلی سرور API را نشان می‌دهند.
این صفحه این نقاط پایانی API را معرفی می‌کند و توضیح می‌دهد که چگونه می‌توانید از آن‌ها استفاده کنید.

<!-- body -->

## نقاط پایانی API برای بررسی سلامت

سرور API کوبرنتیز سه نقطهٔ پایانی API (`healthz`، `livez` و `readyz`) را برای نشان دادن وضعیت فعلی سرور API فراهم می‌کند.
نقطهٔ پایانی `healthz` (از نسخهٔ v1.16 کوبرنتیز) منسوخ شده است و به‌جای آن باید از نقاط پایانی دقیق‌تر `livez` و `readyz` استفاده کنید.
می‌توان نقطهٔ پایانی `livez` را همراه با [فلگ](/docs/reference/command-line-tools-reference/kube-apiserver) `--livez-grace-period` به کار برد تا مدت زمان راه‌اندازی مشخص شود.
برای خاموش‌شدن تدریجی و بی‌دردسر (graceful shutdown) می‌توانید [فلگ](/docs/reference/command-line-tools-reference/kube-apiserver) `--shutdown-delay-duration` را همراه با نقطهٔ پایانی `/readyz` تعیین کنید.
ماشین‌هایی که وضعیت `healthz`/`livez`/`readyz` سرور API را بررسی می‌کنند، باید به کد وضعیت HTTP تکیه کنند.
کد وضعیت `200` نشان می‌دهد که سرور API، بسته به نقطهٔ پایانی فراخوانی‌شده، در وضعیت `healthy`/`live`/`ready` قرار دارد.

این نقاط پایانی با نحوهٔ عملکرد [کاوشگرهای HTTP](/docs/concepts/workloads/pods/probes/#http-probes) در کوبرنتیز هم‌راستا هستند:

* **livez**: از این نقطهٔ پایانی برای تعیین اینکه آیا سرور API باید دوباره راه‌اندازی شود یا نه استفاده کنید. اگر `/livez` یک کد وضعیت خطا (مانند 500) برگرداند، احتمالاً سرور API در وضعیتی غیرقابل‌بازیابی، مانند بن‌بست (deadlock)، قرار دارد و باید دوباره راه‌اندازی شود.
* **readyz**: از این نقطهٔ پایانی برای تعیین اینکه آیا سرور API آمادهٔ پذیرش ترافیک است یا نه استفاده کنید. اگر `/readyz` یک کد وضعیت خطا برگرداند، یعنی سرور هنوز در حال مقداردهی اولیه است یا به‌طور موقت نمی‌تواند به درخواست‌ها پاسخ دهد (برای مثال، منتظر در دسترس قرار گرفتن etcd است یا منتظر است تا همگام‌سازی اولیهٔ همهٔ watch cacheهای ثبت‌شده از etcd کامل شود)؛ در این حالت باید ترافیک را از آن دور کرد.

گزینه‌های مفصل‌تری که در ادامه نشان داده شده‌اند، برای استفادهٔ اپراتورهای انسانی در نظر گرفته شده‌اند تا بتوانند کلاستر خود را اشکال‌زدایی کنند یا وضعیت سرور API را درک کنند.

مثال‌های زیر نشان می‌دهند که چگونه می‌توانید با نقاط پایانی API سلامت تعامل داشته باشید.

برای همهٔ نقاط پایانی می‌توانید از پارامتر `verbose` استفاده کنید تا بررسی‌ها و وضعیت آن‌ها چاپ شوند.
این کار می‌تواند به اپراتور انسانی در اشکال‌زدایی وضعیت فعلی سرور API کمک کند، اما برای استفادهٔ ماشین طراحی نشده است:

```shell
curl -k https://localhost:6443/livez?verbose
```

یا از یک میزبان راه دور با احراز هویت:

```shell
kubectl get --raw='/readyz?verbose'
```

خروجی به این شکل خواهد بود:

    [+]ping ok
    [+]log ok
    [+]etcd ok
    [+]poststarthook/watch-cache-initialization ok
    [+]poststarthook/start-kube-apiserver-admission-initializer ok
    [+]poststarthook/generic-apiserver-start-informers ok
    [+]poststarthook/start-apiextensions-informers ok
    [+]poststarthook/start-apiextensions-controllers ok
    [+]poststarthook/crd-informer-synced ok
    [+]poststarthook/bootstrap-controller ok
    [+]poststarthook/rbac/bootstrap-roles ok
    [+]poststarthook/scheduling/bootstrap-system-priority-classes ok
    [+]poststarthook/start-cluster-authentication-info-controller ok
    [+]poststarthook/start-kube-aggregator-informers ok
    [+]poststarthook/apiservice-registration-controller ok
    [+]poststarthook/apiservice-status-available-controller ok
    [+]poststarthook/kube-apiserver-autoregistration ok
    [+]autoregister-completion ok
    [+]poststarthook/apiservice-openapi-controller ok
    healthz check passed

سرور API کوبرنتیز همچنین امکان مستثنا کردن بررسی‌های خاص را فراهم می‌کند.
پارامترهای کوئری را نیز می‌توان مانند این مثال با هم ترکیب کرد:

```shell
curl -k 'https://localhost:6443/readyz?verbose&exclude=etcd'
```

خروجی نشان می‌دهد که بررسی `etcd` مستثنا شده است:

    [+]ping ok
    [+]log ok
    [+]etcd excluded: ok
    [+]poststarthook/watch-cache-initialization ok
    [+]poststarthook/start-kube-apiserver-admission-initializer ok
    [+]poststarthook/generic-apiserver-start-informers ok
    [+]poststarthook/start-apiextensions-informers ok
    [+]poststarthook/start-apiextensions-controllers ok
    [+]poststarthook/crd-informer-synced ok
    [+]poststarthook/bootstrap-controller ok
    [+]poststarthook/rbac/bootstrap-roles ok
    [+]poststarthook/scheduling/bootstrap-system-priority-classes ok
    [+]poststarthook/start-cluster-authentication-info-controller ok
    [+]poststarthook/start-kube-aggregator-informers ok
    [+]poststarthook/apiservice-registration-controller ok
    [+]poststarthook/apiservice-status-available-controller ok
    [+]poststarthook/kube-apiserver-autoregistration ok
    [+]autoregister-completion ok
    [+]poststarthook/apiservice-openapi-controller ok
    [+]shutdown ok
    healthz check passed

## بررسی‌های سلامت جداگانه

{{< feature-state state="alpha" >}}

هر بررسی سلامت یک نقطهٔ پایانی HTTP جداگانه ارائه می‌دهد و می‌توان آن را به‌تنهایی بررسی کرد.
الگوی نشانی بررسی‌های سلامت جداگانه به‌صورت `/livez/<healthcheck-name>` یا `/readyz/<healthcheck-name>` است؛ در این الگو، `livez` و `readyz` به‌ترتیب نشان می‌دهند که می‌خواهید زنده‌بودن (liveness) یا آمادگی (readiness) سرور API را بررسی کنید.
مسیر `<healthcheck-name>` را می‌توان با استفاده از فلگ `verbose` که پیش‌تر توضیح داده شد پیدا کرد؛ کافی است مسیر میان `[+]` و `ok` را بردارید.
این بررسی‌های سلامت جداگانه برای استفادهٔ ماشین‌ها در نظر گرفته نشده‌اند، اما می‌توانند به اپراتور انسانی در اشکال‌زدایی سیستم کمک کنند:

```shell
curl -k https://localhost:6443/livez/etcd
```
