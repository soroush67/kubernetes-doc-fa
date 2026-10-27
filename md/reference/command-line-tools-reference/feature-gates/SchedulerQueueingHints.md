---
title: SchedulerQueueingHints
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.28"
  - stage: beta
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.31"
  - stage: beta
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"
---
[راهنمای صف‌بندی (queueing hints)](/docs/concepts/scheduling-eviction/scheduling-framework/#queueinghint) در زمان‌بند را فعال می‌کند که به کاهش صف‌بندی مجدد غیرضروری کمک می‌کند.
زمان‌بند در صورتی که در کلاستر تغییری رخ دهد که بتواند امکان زمان‌بندی یک Pod را فراهم کند، زمان‌بندی آن Pod را دوباره تلاش می‌کند.
راهنماهای صف‌بندی سیگنال‌هایی داخلی هستند که به زمان‌بند اجازه می‌دهند، بر اساس تلاش‌های قبلی زمان‌بندی، تغییرات کلاستر را که به Pod زمان‌بندی‌نشده مربوط هستند، فیلتر کند.
