---
title: SidecarContainers
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
---
امکان تنظیم `restartPolicy` یک init container را روی
`Always` فراهم می‌کند تا آن کانتینر به یک کانتینر sidecar تبدیل شود (init containerهای قابل راه‌اندازی مجدد).
برای جزئیات بیشتر به [کانتینرهای Sidecar و restartPolicy](/docs/concepts/workloads/pods/sidecar-containers/)
مراجعه کنید.
