---
title: MemoryQoS
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
محافظت از حافظه و محدودسازی (throttling) میزان استفاده از آن را برای Podها و کانتینرها با استفاده از کنترلر حافظه در cgroup v2 فعال می‌کند. هنگامی که `memoryThrottlingFactor` تنظیم شده باشد، `kubelet` مقدار `memory.high` را برای محدودسازی کانتینرهای Burstable و BestEffort تنظیم می‌کند. هنگامی که `memoryReservationPolicy` روی `TieredReservation` تنظیم شده باشد، `kubelet` در صورت نیاز مقادیر `memory.min` و `memory.low` را برای محافظت چندلایه از حافظه تنظیم می‌کند. این قابلیت هم به فعال‌سازی feature gate و هم به تنظیم پیکربندی `kubelet` نیاز دارد.
