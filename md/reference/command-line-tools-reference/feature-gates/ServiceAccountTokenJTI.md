---
title: ServiceAccountTokenJTI
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.29"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
---
مشخص می‌کند که آیا JTIها (شناسه‌های UUID) در توکن‌های حساب سرویس (service account) تولیدشده درج شوند یا خیر،
و همچنین مشخص می‌کند که آیا این JTIها برای درخواست‌های بعدی که با این توکن‌ها انجام می‌شوند، در گزارش ممیزی (audit log) کوبرنتیز ثبت شوند یا خیر.
