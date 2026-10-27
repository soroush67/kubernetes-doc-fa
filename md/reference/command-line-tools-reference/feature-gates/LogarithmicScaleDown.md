---
title: LogarithmicScaleDown
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.30"
  - stage: stable
    defaultValue: true
    fromVersion: "1.31"
---
فعال‌سازی انتخاب نیمه‌تصادفی Podهایی که باید هنگام کاهش مقیاس (scaledown) توسط کنترل‌کننده تخلیه (evict) شوند، بر اساس دسته‌بندی لگاریتمی (logarithmic bucketing) زمان‌نگارهای Podها.
