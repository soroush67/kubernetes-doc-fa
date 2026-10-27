---
title: CSIMigrationvSphere
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.18"
    toVersion: "1.18"
  - stage: beta
    defaultValue: false
    fromVersion: "1.19"  
    toVersion: "1.24" 
  - stage: beta
    defaultValue: true
    fromVersion: "1.25"  
    toVersion: "1.25" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.28"     

removed: true
---
این قابلیت لایه‌های واسط (shim) و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) از افزونه درون‌درخت (in-tree) vSphere به افزونه vSphere CSI هدایت شود. بازگشت به افزونه درون‌درخت vSphere برای عملیات اتصال (mount) را در نودهایی که این قابلیت در آن‌ها غیرفعال است یا افزونه vSphere CSI روی آن‌ها نصب و پیکربندی نشده است، پشتیبانی می‌کند. بازگشت به افزونه درون‌درخت برای عملیات تأمین (provision) پشتیبانی نمی‌شود و برای این عملیات باید افزونه CSI نصب و پیکربندی شده باشد. فعال بودن feature flag با نام CSIMigration الزامی است.
