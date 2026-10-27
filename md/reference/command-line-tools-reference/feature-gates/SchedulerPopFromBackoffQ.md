---
title: SchedulerPopFromBackoffQ
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
---

رفتار صف زمان‌بندی را با برداشتن Podها از backoffQ در زمانی که activeQ خالی است بهبود می‌بخشد.
این کار امکان می‌دهد Podهایی که به‌طور بالقوه قابل زمان‌بندی هستند در سریع‌ترین زمان ممکن پردازش شوند و اثر تنبیهی صف backoff از بین برود.
