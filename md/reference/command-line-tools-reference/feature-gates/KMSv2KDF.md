---
title: KMSv2KDF
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.28"  
    toVersion: "1.28"
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.31"

removed: true
---
امکان می‌دهد KMS v2 کلیدهای رمزنگاری داده با کاربرد یک‌بار مصرف تولید کند.
برای جزئیات بیشتر، [استفاده از KMS Provider برای رمزنگاری داده‌ها](/docs/tasks/administer-cluster/kms-provider) را ببینید.
اگر feature gate با نام `KMSv2` در کلاستر شما فعال نباشد، مقدار feature gate با نام `KMSv2KDF` تأثیری نخواهد داشت.
