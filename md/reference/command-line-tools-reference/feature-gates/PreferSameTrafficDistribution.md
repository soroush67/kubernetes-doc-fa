---
title: PreferSameTrafficDistribution
content_type: feature_gate

_build:
  list: never
  render: false

stages:
- stage: alpha 
  defaultValue: false
  fromVersion: "1.33"
  toVersion: "1.33"
- stage: beta
  defaultValue: true
  fromVersion: "1.34"
  toVersion: "1.34"
- stage: stable
  defaultValue: true
  locked: true
  fromVersion: "1.35"
---
استفاده از مقادیر `PreferSameZone` و `PreferSameNode` را در فیلد
[`trafficDistribution`](/docs/reference/networking/virtual-ips/#traffic-distribution)
در Service امکان‌پذیر می‌کند.
