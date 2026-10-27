---
# Removed from Kubernetes
title: CSIMigrationOpenStack
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.17"  
  - stage: beta 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.25"    

removed: true
---
شیم‌ها (shims) و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) از افزونه درون‌درختی (in-tree) Cinder به افزونه Cinder CSI هدایت شود. بازگشت به افزونه درون‌درختی Cinder را برای عملیات اتصال (mount) روی نودهایی پشتیبانی می‌کند که این قابلیت در آن‌ها غیرفعال است یا افزونه Cinder CSI روی آن‌ها نصب و پیکربندی نشده است. بازگشت به افزونه درون‌درختی برای عملیات تأمین (provision) پشتیبانی نمی‌شود؛ برای این عملیات باید افزونه CSI نصب و پیکربندی شده باشد. فعال بودن feature flag با نام CSIMigration الزامی است.
