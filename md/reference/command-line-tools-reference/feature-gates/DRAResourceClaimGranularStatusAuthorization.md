---
title: DRAResourceClaimGranularStatusAuthorization
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---

پشتیبانی از مجوزدهی دقیق (granular) برای به‌روزرسانی‌های وضعیت (status) در ResourceClaim را فعال می‌کند.
این قابلیت هنگام تغییر فیلدهای مشخصی در آبجکت‌های status مربوط به ResourceClaim،
به مجوزهای دسترسی دقیق‌تر و تکمیلی نیاز دارد.
