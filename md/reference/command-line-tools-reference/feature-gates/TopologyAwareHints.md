---
title: TopologyAwareHints
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.22"
  - stage: beta
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.23"
  - stage: beta
    defaultValue: true
    fromVersion: "1.24"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"
    toVersion: "1.35"

removed: true
---
مسیریابی آگاه از توپولوژی را بر پایه راهنمایی‌های توپولوژی (topology hints)
در EndpointSliceها فعال می‌کند. برای جزئیات بیشتر به
[راهنمایی‌های آگاه از توپولوژی](/docs/concepts/services-networking/topology-aware-routing/)
مراجعه کنید.
