---
title: LegacyServiceAccountTokenCleanUp
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
    toVersion: "1.29"
  - stage: stable
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"

removed: true
---
فعال‌سازی پاک‌سازی
[توکن‌های service account](/docs/concepts/security/service-accounts/#get-a-token)
مبتنی بر Secret، در صورتی که در بازه زمانی مشخص‌شده (به‌طور پیش‌فرض یک سال) استفاده نشده باشند.
