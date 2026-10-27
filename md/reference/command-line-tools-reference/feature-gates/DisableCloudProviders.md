---
title: DisableCloudProviders
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"

removed: true
---
فعال‌سازی این feature gate باعث غیرفعال شدن قابلیت‌هایی در `kube-apiserver`،
`kube-controller-manager` و `kubelet` می‌شد که به آرگومان خط فرمان `--cloud-provider`
مربوط بودند.

در کوبرنتیز نسخه v1.31 و نسخه‌های بعد از آن، تنها مقادیر معتبر برای `--cloud-provider`
یا رشته‌ی خالی (بدون یکپارچه‌سازی با ارائه‌دهنده‌ی ابری) و یا "external"
(یکپارچه‌سازی از طریق یک cloud-controller-manager جداگانه) است.
