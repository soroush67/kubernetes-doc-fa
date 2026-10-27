---
title: KubeletTracing
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"
    toVersion: "1.33"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.34"
---
پشتیبانی از ردیابی توزیع‌شده (distributed tracing) را به kubelet اضافه می‌کند.
در صورت فعال بودن، رابط CRI در kubelet و سرورهای http احرازهویت‌شده به‌گونه‌ای ابزارگذاری می‌شوند که
span های ردیابی OpenTelemetry تولید کنند.
برای جزئیات بیشتر به [ردیابی‌ها برای اجزای سیستمی کوبرنتیز](/docs/concepts/cluster-administration/system-traces) مراجعه کنید.
