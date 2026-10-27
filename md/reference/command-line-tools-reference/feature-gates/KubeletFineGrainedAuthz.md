---
title: KubeletFineGrainedAuthz
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
فعال‌سازی [مجوزدهی دقیق (fine-grained authorization)](/docs/reference/access-authn-authz/kubelet-authn-authz/#fine-grained-authorization)
برای API مبتنی بر HTTP(S) در kubelet.
