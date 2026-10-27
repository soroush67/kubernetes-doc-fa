---
reviewers:
- lavalamp
title: مؤلفه‌های کوبرنتیز
content_type: concept
description: >
  نمای کلی‌ای از مؤلفه‌های کلیدی که یک کلاستر کوبرنتیز را تشکیل می‌دهند.
weight: 10
theme_lock: light
card:
  title: مؤلفه‌های یک کلاستر
  name: concepts
  weight: 20
---

<!-- overview -->

این صفحه نمای کلی و سطح‌بالایی از مؤلفه‌های ضروری‌ای که یک کلاستر کوبرنتیز را تشکیل می‌دهند ارائه می‌کند.

{{< figure src="/images/docs/components-of-kubernetes.svg" alt="مؤلفه‌های کوبرنتیز" caption="مؤلفه‌های یک کلاستر کوبرنتیز" class="diagram-large" clicktozoom="true" >}}

<!-- body -->

## مؤلفه‌های اصلی

یک کلاستر کوبرنتیز از یک control plane و یک یا چند نود کارگر (worker node) تشکیل شده است.
در ادامه، مرور کوتاهی بر مؤلفه‌های اصلی آمده است:

### مؤلفه‌های control plane

وضعیت کلی کلاستر را مدیریت می‌کنند:

[kube-apiserver](/docs/concepts/architecture/#kube-apiserver)
: سرورِ مؤلفه‌ی مرکزی که HTTP API کوبرنتیز را در دسترس قرار می‌دهد.

[etcd](/docs/concepts/architecture/#etcd)
: مخزن کلید-مقدارِ سازگار و با دسترس‌پذیری بالا برای همه‌ی داده‌های API server.

[kube-scheduler](/docs/concepts/architecture/#kube-scheduler)
: به دنبال Podهایی می‌گردد که هنوز به نودی متصل نشده‌اند و هر Pod را به یک نود مناسب اختصاص می‌دهد.

[kube-controller-manager](/docs/concepts/architecture/#kube-controller-manager)
: {{< glossary_tooltip text="کنترل‌کننده‌ها" term_id="controller" >}} را برای پیاده‌سازی رفتار API کوبرنتیز اجرا می‌کند.

[cloud-controller-manager](/docs/concepts/architecture/#cloud-controller-manager) (اختیاری)
: با ارائه‌دهنده(های) ابری زیرین یکپارچه می‌شود.

### مؤلفه‌های نود

روی هر نود اجرا می‌شوند، Podهای در حال اجرا را نگهداری می‌کنند و محیط اجرایی کوبرنتیز را فراهم می‌کنند:

[kubelet](/docs/concepts/architecture/#kubelet)
: اطمینان حاصل می‌کند که Podها، از جمله کانتینرهایشان، در حال اجرا هستند.

[kube-proxy](/docs/concepts/architecture/#kube-proxy) (اختیاری)
: قواعد شبکه را روی نودها نگهداری می‌کند تا {{< glossary_tooltip text="Serviceها" term_id="service" >}} پیاده‌سازی شوند.

[محیط اجرای کانتینر (Container runtime)](/docs/concepts/architecture/#container-runtime)
: نرم‌افزاری که مسئول اجرای کانتینرها است. برای آگاهی بیشتر،
  [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/) را مطالعه کنید.

{{% thirdparty-content single="true" %}}

ممکن است کلاستر شما روی هر نود به نرم‌افزارهای دیگری نیز نیاز داشته باشد؛ برای مثال، ممکن است
[systemd](https://systemd.io/) را نیز روی یک نود لینوکسی اجرا کنید تا بر مؤلفه‌های محلی نظارت کند.

## افزونه‌ها (Addons)

افزونه‌ها قابلیت‌های کوبرنتیز را گسترش می‌دهند. چند نمونه‌ی مهم عبارت‌اند از:

[DNS](/docs/concepts/architecture/#dns)
: برای تفکیک نام DNS در سطح کل کلاستر.

[رابط کاربری وب](/docs/concepts/architecture/#web-ui-dashboard) (Dashboard)
: برای مدیریت کلاستر از طریق یک رابط وب.

[پایش منابع کانتینر](/docs/concepts/architecture/#container-resource-monitoring)
: برای جمع‌آوری و ذخیره‌ی متریک‌های کانتینرها.

[ثبت لاگ در سطح کلاستر](/docs/concepts/architecture/#cluster-level-logging)
: برای ذخیره‌ی لاگ‌های کانتینرها در یک مخزن مرکزی لاگ.

## انعطاف‌پذیری در معماری

کوبرنتیز در نحوه‌ی استقرار و مدیریت این مؤلفه‌ها انعطاف‌پذیری فراهم می‌کند.
این معماری را می‌توان با نیازهای گوناگون، از محیط‌های توسعه‌ی کوچک
تا استقرارهای عملیاتی در مقیاس بزرگ، تطبیق داد.

برای اطلاعات دقیق‌تر درباره‌ی هر مؤلفه و روش‌های گوناگون پیکربندی معماری
کلاستر خود، صفحه‌ی [معماری کلاستر](/docs/concepts/architecture/) را ببینید.
