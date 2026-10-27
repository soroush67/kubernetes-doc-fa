---
title: BtreeWatchCache
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.33"

---
در صورت فعال بودن، API server پیاده‌سازی قدیمی _watch cache_ مبتنی بر HashMap را با پیاده‌سازی مبتنی بر BTree جایگزین می‌کند. این جایگزینی ممکن است به بهبود عملکرد منجر شود.
