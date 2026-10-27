---
title: KubeletCrashLoopBackOffMax
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.34"
  - stage: beta
    defaultValue: true
    fromVersion: "1.35"
---
پشتیبانی از حداکثر مقدار backoff قابل پیکربندی برای هر نود را، در زمان راه‌اندازی مجدد
کانتینرهایی که در وضعیت `CrashLoopBackOff` قرار دارند، فعال می‌کند.
برای جزئیات بیشتر، فیلد `crashLoopBackOff.maxContainerRestartPeriod` را در
[فایل پیکربندی kubelet](/docs/reference/config-api/kubelet-config.v1beta1/) بررسی کنید.
