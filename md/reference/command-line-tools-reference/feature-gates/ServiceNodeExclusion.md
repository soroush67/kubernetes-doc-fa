---
# Removed from Kubernetes
title: ServiceNodeExclusion
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.18"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.20"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"    

removed: true
---
امکان کنار گذاشتن نودها از load balancerهایی را که توسط یک ارائه‌دهنده ابری ایجاد می‌شوند فعال می‌کند.
نودی که با برچسب «`node.kubernetes.io/exclude-from-external-load-balancers`» برچسب‌گذاری شده باشد، واجد شرایط کنار گذاشته شدن است.
