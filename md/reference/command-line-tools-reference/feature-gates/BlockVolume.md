---
# Removed from Kubernetes
title: BlockVolume
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.9"
    toVersion: "1.12"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.17"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.21"    

removed: true
---
امکان تعریف و استفاده از دستگاه‌های بلاک خام (raw block devices) را در Podها فعال می‌کند.
برای جزئیات بیشتر به [پشتیبانی از حجم بلاک خام](/docs/concepts/storage/persistent-volumes/#raw-block-volume-support) مراجعه کنید.
