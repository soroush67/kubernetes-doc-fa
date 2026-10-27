---
# Removed from Kubernetes
title: IngressClassNamespacedParams
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.22"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.23"
    toVersion: "1.24"    

removed: true
---
امکان ارجاع به پارامترهای با محدوده فضای نام (namespace) را در منبع `IngressClass` فراهم می‌کند. این قابلیت دو فیلد `Scope` و `Namespace` را به `IngressClass.spec.parameters` اضافه می‌کند.
