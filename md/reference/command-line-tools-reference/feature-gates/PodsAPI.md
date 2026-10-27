---
title: PodsAPI
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
سرویس gRPC مربوط به Pods API در kubelet را فعال می‌کند.
برای جزئیات بیشتر، [Pods API در kubelet](/docs/reference/node/kubelet-pods-api/) را ببینید.
