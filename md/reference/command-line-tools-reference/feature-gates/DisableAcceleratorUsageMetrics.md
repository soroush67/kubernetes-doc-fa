---
title: DisableAcceleratorUsageMetrics
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.19"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.24"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.25"
    toVersion: "1.27"    

removed: true  
---
[غیرفعال کردن معیارهای شتاب‌دهنده که توسط kubelet جمع‌آوری می‌شوند](/docs/concepts/cluster-administration/system-metrics/#disable-accelerator-metrics).
