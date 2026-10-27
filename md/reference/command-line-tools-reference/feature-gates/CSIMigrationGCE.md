---
title: CSIMigrationGCE
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
    toVersion: "1.27" 

removed: true
---
پوسته‌های سازگاری (shim) و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) را از افزونه درون‌درخت (in-tree) GCE-PD به افزونه PD CSI هدایت کند. از بازگشت به افزونه درون‌درخت GCE برای عملیات مانت (mount) روی نودهایی که این قابلیت در آن‌ها غیرفعال است یا افزونه PD CSI روی آن‌ها نصب و پیکربندی نشده است، پشتیبانی می‌کند. از بازگشت به افزونه درون‌درخت برای عملیات تأمین (provision) پشتیبانی نمی‌کند؛ برای این عملیات باید افزونه CSI نصب و پیکربندی شده باشد. فعال بودن feature flag با نام CSIMigration الزامی است.
