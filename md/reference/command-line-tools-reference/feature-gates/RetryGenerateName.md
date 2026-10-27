---
title: RetryGenerateName
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
امکان تلاش مجدد برای ایجاد آبجکت را فراهم می‌کند، در مواردی که انتظار می‌رود
{{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}
یک [نام](/docs/concepts/overview/working-with-objects/names/#names) تولید کند.

هنگامی که این قابلیت فعال باشد، درخواست‌هایی که از `generateName` استفاده می‌کنند، در صورتی که
control plane تداخل نام با یک آبجکت موجود را تشخیص دهد، به‌طور خودکار و حداکثر تا سقف ۸ تلاش در مجموع دوباره انجام می‌شوند.
