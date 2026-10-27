---
title: PodObservedGenerationTracking
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: beta
    defaultValue: true
    fromVersion: "1.34"
    toVersion: "1.34"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.35"
---
به kubelet امکان می‌دهد فیلد `observedGeneration` را در `.status` مربوط به Pod تنظیم کند، و همچنین به سایر مؤلفه‌ها امکان می‌دهد `observedGeneration` را در شرایط (conditions) Pod تنظیم کنند.
این قابلیت امکان می‌دهد مقدار `.metadata.generation` مربوط به Pod در لحظه‌ای که وضعیت کلی یا یک شرط مشخص ثبت می‌شد، بازتاب داده شود.
ذخیره‌کردن این مقدار به جلوگیری از خطرات مرتبط با _به‌روزرسانی‌های ازدست‌رفته_ (lost updates) کمک می‌کند.
