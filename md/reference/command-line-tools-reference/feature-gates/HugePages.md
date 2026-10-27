---
# Removed from Kubernetes
title: HugePages
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.13"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.14"
    toVersion: "1.16"    

removed: true  
---
امکان تخصیص و مصرف [صفحات حجیم (huge pages)](/docs/tasks/manage-hugepages/scheduling-hugepages/) از پیش تخصیص‌یافته را فعال می‌کند.
