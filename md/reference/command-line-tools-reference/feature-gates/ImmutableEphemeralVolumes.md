---
# Removed from Kubernetes
title: ImmutableEphemeralVolumes
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
    toVersion: "1.20"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.24"    

removed: true
---
امکان علامت‌گذاری هر یک از Secretها و ConfigMapها به‌صورت
تغییرناپذیر (immutable) را برای ایمنی و کارایی بهتر فراهم می‌کند.
