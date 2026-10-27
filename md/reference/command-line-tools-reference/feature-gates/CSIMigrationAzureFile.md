---
title: CSIMigrationAzureFile
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.15"
    toVersion: "1.20"
  - stage: beta
    defaultValue: false
    fromVersion: "1.21"  
    toVersion: "1.23" 
  - stage: beta
    defaultValue: true
    fromVersion: "1.24"  
    toVersion: "1.25" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.29" 
removed: true
---
فعال‌سازی لایه‌های واسط (shim) و منطق ترجمه برای هدایت عملیات حجم (volume) از افزونه درون‌درخت (in-tree) Azure-File به افزونه AzureFile CSI.
در عملیات مانت (mount)، بازگشت به افزونه درون‌درخت AzureFile برای نودهایی پشتیبانی می‌شود که این قابلیت در آن‌ها غیرفعال است یا افزونه AzureFile CSI روی آن‌ها نصب و پیکربندی نشده است. بازگشت به افزونه درون‌درخت برای عملیات تأمین (provision) پشتیبانی نمی‌شود و برای این عملیات باید افزونه CSI نصب و پیکربندی شده باشد.
نیازمند فعال بودن feature flag با نام CSIMigration است.
