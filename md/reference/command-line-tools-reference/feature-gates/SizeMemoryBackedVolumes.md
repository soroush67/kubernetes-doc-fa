---
title: SizeMemoryBackedVolumes
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.20"
    toVersion: "1.21"
  - stage: beta
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.32"
    toVersion: "1.34"

removed: true

---
به kubeletها امکان می‌دهد حد اندازه (size limit) حجم‌های (volume) مبتنی بر حافظه، به‌ویژه حجم‌های `emptyDir`، را تعیین کنند.
