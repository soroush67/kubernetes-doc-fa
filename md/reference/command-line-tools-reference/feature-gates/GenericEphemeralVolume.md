---
# Removed from Kubernetes
title: GenericEphemeralVolume
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.20"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    

removed: true  
---
امکان استفاده از حجم‌های موقت (ephemeral) درون‌خطی (inline) را فراهم می‌کند که از تمام قابلیت‌های حجم‌های معمولی پشتیبانی می‌کنند (برای نمونه، می‌توانند توسط فروشندگان ذخیره‌سازی شخص ثالث ارائه شوند، از ردیابی ظرفیت ذخیره‌سازی پشتیبانی می‌کنند، امکان بازیابی از اسنپ‌شات را دارند و غیره).
به [حجم‌های موقت (Ephemeral Volumes)](/docs/concepts/storage/ephemeral-volumes/) مراجعه کنید.
