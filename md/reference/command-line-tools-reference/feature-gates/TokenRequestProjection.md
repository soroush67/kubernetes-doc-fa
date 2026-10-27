---
# Removed from Kubernetes
title: TokenRequestProjection
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.11"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.19"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.21"    

removed: true
---
امکان تزریق توکن‌های service account به یک Pod را از طریق [حجم `projected`](/docs/concepts/storage/volumes/#projected) فراهم می‌کند.
