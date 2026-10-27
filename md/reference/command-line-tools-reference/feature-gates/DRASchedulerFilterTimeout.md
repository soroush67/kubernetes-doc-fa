---
title: DRASchedulerFilterTimeout
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"

---
امکان متوقف‌کردن عملیات فیلتر در سطح هر نود را در زمان‌بند، پس از گذشت مدت‌زمان مشخصی فعال می‌کند
(به‌طور پیش‌فرض ۱۰ ثانیه، که در پیکربندی افزونه زمان‌بند DynamicResources قابل تنظیم است).
