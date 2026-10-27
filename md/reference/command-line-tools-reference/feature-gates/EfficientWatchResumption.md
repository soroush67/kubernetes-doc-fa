---
title: EfficientWatchResumption
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.20"
  - stage: beta
    defaultValue: true
    fromVersion: "1.21"  
    toVersion: "1.23" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"  
    toVersion: "1.32"

removed: true
---
امکان ارسال رویدادهای bookmark (اعلان پیشرفت) را که از لایه ذخیره‌سازی منشأ می‌گیرند به کاربران فراهم می‌کند. این قابلیت فقط بر عملیات watch اعمال می‌شود.
