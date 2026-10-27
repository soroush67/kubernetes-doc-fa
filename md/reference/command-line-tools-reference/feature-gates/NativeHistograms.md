---
title: NativeHistograms
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
مؤلفه‌های کوبرنتیز را قادر می‌سازد تا متریک‌ها را با فرمت Prometheus Native Histogram ارائه کنند، که کارایی بهتر و دقت بالاتر در تفکیک باکت‌ها (bucket) را به همراه دارد.
برای اطلاعات بیشتر به [Native Histograms](/docs/reference/instrumentation/native-histograms/) مراجعه کنید.
