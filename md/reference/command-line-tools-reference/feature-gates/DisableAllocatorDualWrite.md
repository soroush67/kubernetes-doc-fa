---
title: DisableAllocatorDualWrite
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"

---
می‌توانید feature gate با نام `MultiCIDRServiceAllocator` را فعال کنید. API server از مهاجرت از تخصیص‌دهنده‌های قدیمی ClusterIP مبتنی بر bitmap به تخصیص‌دهنده‌های جدید IPAddress پشتیبانی می‌کند.

API server عملیات نوشتن را به‌صورت دوگانه (dual-write) روی هر دو تخصیص‌دهنده انجام می‌دهد. این feature gate نوشتن دوگانه را روی تخصیص‌دهنده‌های جدید Cluster IP غیرفعال می‌کند؛ در صورتی که مرحله مربوط به مهاجرت را تکمیل کرده‌اید، می‌توانید این feature gate را فعال کنید.
