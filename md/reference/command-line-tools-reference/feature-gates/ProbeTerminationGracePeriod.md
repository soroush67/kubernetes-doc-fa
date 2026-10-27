---
title: ProbeTerminationGracePeriod
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: beta
    defaultValue: false
    fromVersion: "1.22"  
    toVersion: "1.24" 
  - stage: beta
    defaultValue: true
    fromVersion: "1.25"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.28"     

removed: true
---
امکان [تنظیم `terminationGracePeriodSeconds` در سطح probe](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#probe-level-terminationgraceperiodseconds) را روی Podها فعال می‌کند. برای جزئیات بیشتر، [پیشنهاد بهبود (enhancement proposal)](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/2238-liveness-probe-grace-period) را ببینید.
