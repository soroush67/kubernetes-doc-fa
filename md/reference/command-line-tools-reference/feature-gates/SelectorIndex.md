---
# Removed from Kubernetes
title: SelectorIndex
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.18"
    toVersion: "1.18"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.19"
    toVersion: "1.19"
  - stage: stable
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.25"

removed: true  
---
امکان استفاده از ایندکس‌های مبتنی بر برچسب (label) و فیلد را در watch cache سرور API فراهم می‌کند تا عملیات list سریع‌تر انجام شود.
