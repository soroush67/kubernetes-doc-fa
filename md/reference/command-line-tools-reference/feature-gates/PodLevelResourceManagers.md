---
title: PodLevelResourceManagers
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
    defaultValue: false
    fromVersion: "1.37"
---
فعال‌سازی _مدیران منابع در سطح Pod_: قابلیتی که به مدیران Topology، CPU و Memory امکان می‌دهد از اطلاعات موجود در `.spec.resources` برای انجام هم‌ترازی NUMA برای کل یک Pod استفاده کنند و منابع کانتینرهای درون آن Pod را به‌صورت انعطاف‌پذیر مدیریت نمایند.
