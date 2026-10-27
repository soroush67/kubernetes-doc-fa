---
# Removed from Kubernetes
title: ExpandPersistentVolumes
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.10"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.11"
    toVersion: "1.23"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.26"    

removed: true  
---
امکان گسترش (expand) حجم‌های پایدار (persistent volume) را فعال می‌کند. به
[گسترش Persistent Volume Claimها](/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims)
مراجعه کنید.
