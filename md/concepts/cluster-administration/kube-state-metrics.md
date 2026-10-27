---
title: متریک‌های وضعیت آبجکت‌های کوبرنتیز
content_type: concept
weight: 75
description: >-
   kube-state-metrics، یک عامل افزونه برای تولید و در معرض قرار دادن متریک‌های سطح کلاستر.
---

وضعیت آبجکت‌های کوبرنتیز در API کوبرنتیز را می‌توان به‌صورت متریک در معرض قرار داد.
یک عامل افزونه به نام [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) می‌تواند به سرور API کوبرنتیز متصل شود و یک نقطهٔ پایانی HTTP را با متریک‌هایی که از وضعیت تک‌تک آبجکت‌های کلاستر تولید شده‌اند در معرض قرار دهد.
این عامل اطلاعات گوناگونی دربارهٔ وضعیت آبجکت‌ها، مانند برچسب‌ها و حاشیه‌نویسی‌ها، زمان‌های راه‌اندازی و خاتمه، وضعیت یا مرحله‌ای (phase) که آبجکت در حال حاضر در آن قرار دارد، در معرض قرار می‌دهد.
برای نمونه، کانتینرهایی که در پادها اجرا می‌شوند، متریک `kube_pod_container_info` را ایجاد می‌کنند.
این متریک شامل نام کانتینر، نام پادی که کانتینر بخشی از آن است، {{< glossary_tooltip text="فضای نامی" term_id="namespace" >}} که پاد در آن اجرا می‌شود، نام ایمیج کانتینر، شناسهٔ ایمیج، نام ایمیج در spec کانتینر، شناسهٔ کانتینر در حال اجرا و شناسهٔ پاد به‌صورت برچسب است.

{{% thirdparty-content single="true" %}}

اکنون می‌توان از یک مؤلفهٔ خارجی که قادر به خواندن (scrape) نقطهٔ پایانی kube-state-metrics است (برای نمونه از طریق Prometheus) برای فعال‌سازی موارد کاربرد زیر استفاده کرد.

## نمونه: استفاده از متریک‌های kube-state-metrics برای پرس‌وجوی وضعیت کلاستر {#example-kube-state-metrics-query-1}

سری‌های متریکی که kube-state-metrics تولید می‌کند برای کسب بینش بیشتر دربارهٔ کلاستر سودمند هستند، زیرا می‌توان از آن‌ها برای پرس‌وجو استفاده کرد.

اگر از Prometheus یا ابزار دیگری که از همان زبان پرس‌وجو استفاده می‌کند بهره می‌برید، پرس‌وجوی PromQL زیر تعداد پادهایی را که آماده نیستند برمی‌گرداند:

```
count(kube_pod_status_ready{condition="false"}) by (namespace, pod)
```

## نمونه: هشداردهی بر پایهٔ kube-state-metrics {#example-kube-state-metrics-alert-1}

متریک‌هایی که از kube-state-metrics تولید می‌شوند، امکان هشداردهی دربارهٔ مشکلات کلاستر را نیز فراهم می‌کنند.

اگر از Prometheus یا ابزار مشابهی که از همان زبان قواعد هشدار استفاده می‌کند بهره می‌برید، هشدار زیر در صورتی فعال می‌شود که پادهایی بیش از ۵ دقیقه در وضعیت `Terminating` مانده باشند:

```yaml
groups:
- name: Pod state
  rules:
  - alert: PodsBlockedInTerminatingState
    expr: count(kube_pod_deletion_timestamp) by (namespace, pod) * count(kube_pod_status_reason{reason="NodeLost"} == 0) by (namespace, pod) > 0
    for: 5m
    labels:
      severity: page
    annotations:
      summary: Pod {{$labels.namespace}}/{{$labels.pod}} blocked in Terminating state.
```
