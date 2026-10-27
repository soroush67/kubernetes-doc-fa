---
# Removed from Kubernetes
title: CSIMigrationAzureDisk
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.18"
  - stage: beta
    defaultValue: false
    fromVersion: "1.19"  
    toVersion: "1.22" 
  - stage: beta
    defaultValue: true
    fromVersion: "1.23"  
    toVersion: "1.23" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.26"     

removed: true
---
قابلیت‌های shim و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) از افزونه درون‌درختی (in-tree) Azure-Disk به افزونه AzureDisk CSI هدایت شود.
از بازگشت به افزونه درون‌درختی AzureDisk برای عملیات mount روی نودهایی پشتیبانی می‌کند که این ویژگی در آن‌ها غیرفعال است یا افزونه AzureDisk CSI روی آن‌ها نصب و پیکربندی نشده است. بازگشت به افزونه درون‌درختی برای عملیات provision پشتیبانی نمی‌شود و برای این عملیات باید افزونه CSI نصب و پیکربندی شده باشد.
نیازمند فعال بودن feature flag با نام CSIMigration است.
