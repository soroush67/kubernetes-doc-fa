---
# Removed from Kubernetes
title: ExternalPolicyForExternalIP
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.22"

removed: true  
---
رفع یک باگ که در آن ExternalTrafficPolicy روی ExternalIPهای Service اعمال نمی‌شد.
