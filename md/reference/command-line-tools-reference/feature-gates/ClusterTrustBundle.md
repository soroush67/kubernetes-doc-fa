---
title: ClusterTrustBundle
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.36"
  - stage: stable
    defaultValue: true
    fromVersion: "1.37"
---
این feature gate در kube-apiserver و kube-controller-manager کوبرنتیز وجود دارد.

زمانی که در kube-apiserver استفاده شود، پشتیبانی از ClusterTrustBundle را فعال می‌کند.

در kube-controller-manager کوبرنتیز، این feature gate برای کنترل انتشار یک ClusterTrustBundle
برای امضاکننده (signer) `kubernetes.io/kube-apiserver-serving` به کار می‌رود.
