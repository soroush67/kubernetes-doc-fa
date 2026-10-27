---
# Removed from Kubernetes
title: CSIVolumeFSGroupPolicy
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.19"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.22"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.25"

removed: true  
---
به CSIDriverها اجازه می‌دهد از فیلد `fsGroupPolicy` استفاده کنند.
این فیلد مشخص می‌کند که آیا حجم‌هایی (volumes) که توسط یک CSIDriver ایجاد می‌شوند، هنگام مانت شدن، از تغییر مالکیت و مجوزهای حجم پشتیبانی می‌کنند یا خیر.
