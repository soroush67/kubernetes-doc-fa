---
# Removed from Kubernetes
title: ExpandInUsePersistentVolumes
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.14"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.15"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.26"    

removed: true  
---
امکان گسترش PVCهای در حال استفاده را فعال می‌کند. به
[تغییر اندازه یک PersistentVolumeClaim در حال استفاده](/docs/concepts/storage/persistent-volumes/#resizing-an-in-use-persistentvolumeclaim)
مراجعه کنید.
