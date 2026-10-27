---
# Removed from Kubernetes
title: CSIMigration
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
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.26"    

removed: true
---
لایه‌های سازگاری (shim) و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) را از افزونه‌های درون‌درخت (in-tree) به افزونه‌های CSI متناظر که از پیش نصب شده‌اند هدایت کند.
