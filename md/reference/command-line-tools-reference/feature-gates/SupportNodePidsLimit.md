---
# Removed from Kubernetes
title: SupportNodePidsLimit
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.14"
    toVersion: "1.14"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.15"
    toVersion: "1.19"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.23"    

removed: true
---
پشتیبانی از محدودسازی PIDها روی نود را فعال می‌کند. می‌توان پارامتر
`pid=<number>` را در گزینه‌های `--system-reserved` و `--kube-reserved` مشخص کرد
تا اطمینان حاصل شود که تعداد مشخص‌شده‌ای از شناسه‌های فرایند (process ID) به‌ترتیب برای کل سیستم و
برای دیمون‌های سیستمی کوبرنتیز رزرو می‌شود.
