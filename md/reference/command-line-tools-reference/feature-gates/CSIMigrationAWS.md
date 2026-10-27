---
# Removed from Kubernetes
title: CSIMigrationAWS
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.16"
  - stage: beta 
    defaultValue: false
    fromVersion: "1.17"
    toVersion: "1.22"    
  - stage: beta 
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"    

removed: true
---
لایه‌های سازگاری (shim) و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) از افزونه درون‌درختی (in-tree) AWS-EBS به افزونه EBS CSI هدایت شوند. از بازگشت به افزونه درون‌درختی EBS برای عملیات mount روی نودهایی که این قابلیت در آن‌ها غیرفعال است یا افزونه EBS CSI روی آن‌ها نصب و پیکربندی نشده است، پشتیبانی می‌کند. از بازگشت به افزونه درون‌درختی برای عملیات provision پشتیبانی نمی‌کند؛ برای این عملیات باید افزونه CSI نصب و پیکربندی شده باشد.
