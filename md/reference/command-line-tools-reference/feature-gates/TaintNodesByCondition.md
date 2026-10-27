---
# Removed from Kubernetes
title: TaintNodesByCondition
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.16"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.18"    

removed: true  
---
امکان اعمال خودکار taint بر روی نودها را بر اساس
[شرایط نود](/docs/concepts/architecture/nodes/#condition) فراهم می‌کند.
