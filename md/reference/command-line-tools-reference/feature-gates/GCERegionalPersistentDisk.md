---
# Removed from Kubernetes
title: GCERegionalPersistentDisk
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.10"
    toVersion: "1.12"
  - stage: stable
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.16"

removed: true  
---
قابلیت PD منطقه‌ای (regional PD) را در GCE فعال می‌کند.
