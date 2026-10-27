---
# Removed from Kubernetes
title: TaintBasedEvictions
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.6"
    toVersion: "1.12"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.13"
    toVersion: "1.17"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.20"    

removed: true
---
امکان خارج‌سازی (eviction) پادها از نودها را بر اساس taintهای تعریف‌شده روی نودها و tolerationهای تعریف‌شده روی پادها فعال می‌کند. برای جزئیات بیشتر، [taintها و tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration/) را ببینید.
