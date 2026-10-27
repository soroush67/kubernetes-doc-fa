---
# Removed from Kubernetes
title: AllowExtTrafficLocalEndpoints
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: false
    fromVersion: "1.4"
    toVersion: "1.6"
  - stage: stable
    defaultValue: true
    fromVersion: "1.7"
    toVersion: "1.9"

removed: true
---
امکان می‌دهد یک Service درخواست‌های خارجی را به endpointهای محلی نود هدایت کند.
