---
title: DRAExtendedResource
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: stable
    defaultValue: true
    fromVersion: "1.37"

---
قابلیت [تخصیص منبع توسعه‌یافته (Extended Resource) توسط DRA](/docs/concepts/configuration/manage-resources-containers/#extended-resources-allocation-by-dra) را فعال می‌کند.
این قابلیت امکان تعیین نام یک منبع توسعه‌یافته (extended resource) را در یک DeviceClass فراهم می‌کند.
