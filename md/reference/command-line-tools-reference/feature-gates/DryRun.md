---
title: DryRun
content_type: feature_gate
_build:
  list: never
  render: false
 
stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.12"
    toVersion: "1.12"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.18"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.27"    

removed: true  
---
درخواست‌های [dry run](/docs/reference/using-api/api-concepts/#dry-run) سمت سرور را فعال می‌کند تا اعتبارسنجی، ادغام و تغییر (mutation) بتوانند بدون ثبت نهایی آزمایش شوند.
