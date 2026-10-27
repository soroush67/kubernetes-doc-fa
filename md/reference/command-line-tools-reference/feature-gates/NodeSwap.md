---
title: NodeSwap
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.27"
  - stage: beta
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.34"

---
به kubelet امکان می‌دهد حافظه swap را برای بارهای کاری کوبرنتیز روی یک نود تخصیص دهد.
این قابلیت باید همراه با مقدار `false` برای `KubeletConfiguration.failSwapOn` استفاده شود.
برای جزئیات بیشتر، به [حافظه swap](/docs/concepts/architecture/nodes/#swap-memory) مراجعه کنید.
