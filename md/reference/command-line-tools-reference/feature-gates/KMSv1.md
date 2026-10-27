---
title: KMSv1
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.28"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.29"  
    
---
API نسخه ۱ KMS (KMS v1) را برای رمزنگاری داده‌های در حالت سکون (encryption at rest) فعال می‌کند. برای جزئیات بیشتر، به
[استفاده از ارائه‌دهنده KMS برای رمزنگاری داده‌ها](/docs/tasks/administer-cluster/kms-provider)
مراجعه کنید.
