---
title: معیارهای Pod و کانتینر از طریق CRI
content_type: reference
weight: 50
description: >-
  جمع‌آوری معیارهای Pod و کانتینر از طریق CRI.
---


<!-- overview -->

{{< feature-state feature_gate_name="PodAndContainerStatsFromCRI" >}}

[kubelet](/docs/reference/command-line-tools-reference/kubelet/) معیارهای Pod و
کانتینر را از طریق [cAdvisor](https://github.com/google/cadvisor) جمع‌آوری می‌کند. کوبرنتیز به‌عنوان یک قابلیت بتا، امکان می‌دهد جمع‌آوری معیارهای Pod و کانتینر را از طریق
{{< glossary_tooltip term_id="cri" text="رابط زمان‌اجرای کانتینر (Container Runtime Interface)">}} (CRI) پیکربندی کنید. برای استفاده از سازوکار جمع‌آوری مبتنی بر CRI، باید
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `PodAndContainerStatsFromCRI` را فعال کنید و از یک پیاده‌سازی سازگار CRI
(containerd نسخه ۲.۲ یا بالاتر، CRI-O نسخه ۱.۳۱.۰ یا بالاتر) استفاده کنید.

<!-- body -->

## معیارهای Pod و کانتینر از طریق CRI {#cri-pod-container-metrics}

زمانی که `PodAndContainerStatsFromCRI` فعال باشد، kubelet به‌جای بررسی مستقیم سیستم میزبان با استفاده از cAdvisor، آمار Pod و کانتینر را از زمان‌اجرای کانتینر زیرین دریافت می‌کند.
مزایای تکیه بر زمان‌اجرای کانتینر برای این اطلاعات، در مقایسه با جمع‌آوری مستقیم با cAdvisor، شامل موارد زیر است:

- بهبود بالقوه عملکرد، در صورتی که زمان‌اجرای کانتینر پیش‌تر این اطلاعات را در جریان عملیات عادی خود جمع‌آوری کند. در این حالت، می‌توان از داده‌ها دوباره استفاده کرد و نیازی نیست kubelet آن‌ها را دوباره تجمیع کند.

- جداسازی بیشتر kubelet و زمان‌اجرای کانتینر را فراهم می‌کند و امکان جمع‌آوری معیارها را برای زمان‌اجراهایی فراهم می‌سازد که فرایندها را مستقیماً روی میزبانِ kubelet اجرا نمی‌کنند و بنابراین cAdvisor نمی‌تواند آن‌ها را مشاهده کند (برای مثال: زمان‌اجراهای کانتینری که از مجازی‌سازی استفاده می‌کنند).

{{< note >}}
از کوبرنتیز v1.37، جمع‌آوری معیارهای Pod و کانتینر مبتنی بر cAdvisor در kubelet منسوخ شده است. زمان‌اجراهای CRI که معیارهای موردنیاز را پشتیبانی نمی‌کنند، پس از رسیدن این قابلیت به دسترس‌پذیری عمومی (GA)، جمع‌آوری معیارها در سطح Pod و کانتینر را از دست خواهند داد.
{{< /note >}}

## Endpointهای تحت تأثیر {#affected-endpoints}

زمانی که feature gate فعال باشد، kubelet داده‌های سطح Pod و کانتینر را به‌جای cAdvisor از زمان‌اجرای CRI می‌گیرد. آمار سطح نود و سیستم فایل ایمیج‌ها همچنان از cAdvisor جمع‌آوری می‌شود. endpointهای زیر تحت تأثیر قرار می‌گیرند:

### Summary API (`/stats/summary`)

kubelet برای [Summary API](/docs/reference/kubelet-api/stats.v1alpha1/)، آمار Pod و کانتینر را به‌جای cAdvisor از زمان‌اجرای CRI دریافت می‌کند. این آمار شامل آمار CPU، حافظه، شبکه و فرایندها برای Podها و کانتینرها است.

### `/metrics/cadvisor`

kubelet معیارهای Pod و کانتینر را از طریق RPC با نام `ListPodSandboxMetrics` از زمان‌اجرای CRI می‌گیرد و آن‌ها را در endpoint با مسیر `/metrics/cadvisor` ارائه می‌کند. این روش جایگزین جمع‌آوری مبتنی بر cAdvisor در سطح Pod و کانتینر می‌شود و مسیر endpoint و نام معیارها را حفظ می‌کند. معیارهای سطح نود و ماشین در این endpoint همچنان توسط cAdvisor ارائه می‌شوند.

## شناسایی ارائه‌دهنده فعال معیارها {#identifying-the-active-metrics-provider}

kubelet معیاری با نام `kubelet_metrics_provider` را ارائه می‌کند که برچسب `provider` در آن برابر `cri` یا `cadvisor` است. می‌توانید از این معیار برای بررسی اینکه روی یک نود مشخص، کدام منبع آمار Pod و کانتینر را فراهم می‌کند، استفاده کنید.

## الزامات {#requirements}

برای استفاده از جمع‌آوری معیارها مبتنی بر CRI، به موارد زیر نیاز دارید:

- **containerd** نسخه ۲.۲ یا بالاتر، یا **CRI-O** نسخه ۱.۳۱.۰ یا بالاتر
- فعال بودن [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `PodAndContainerStatsFromCRI` روی kubelet

{{< note >}}
CRI-O از نسخه 1.36.3 به بعد، برچسب‌های `namespace`، `pod` و `container` را به معیارهای CRI در endpoint با مسیر `/metrics/cadvisor` افزوده است. نسخه‌های قبلی این برچسب‌ها را شامل نمی‌شوند و این موضوع ممکن است بر کوئری‌های معیاری که برای تطبیق با معیارهای تولیدشده توسط cAdvisor به این برچسب‌ها متکی هستند، تأثیر بگذارد.
{{< /note >}}

## رفتار جایگزین (Fallback) {#fallback-behavior}

اگر زمان‌اجرای CRI معیارهای مورد انتظار را گزارش نکند، kubelet حتی در صورت فعال بودن feature gate، برای جمع‌آوری آمار Pod و کانتینر به cAdvisor بازمی‌گردد. با غیرفعال کردن feature gate و راه‌اندازی مجدد kubelet می‌توانید به‌طور کامل به جمع‌آوری مبتنی بر cAdvisor بازگردید.
