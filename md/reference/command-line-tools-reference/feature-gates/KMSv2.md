---
title: KMSv2
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: true
    fromVersion: "1.27"  
    toVersion: "1.28" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.29"
    toVersion: "1.31"

removed: true
---
API نسخهٔ ۲ KMS را برای رمزنگاری در حالت سکون (encryption at rest) فعال می‌کند. برای جزئیات بیشتر، به
[استفاده از ارائه‌دهندهٔ KMS برای رمزنگاری داده‌ها](/docs/tasks/administer-cluster/kms-provider)
مراجعه کنید.
