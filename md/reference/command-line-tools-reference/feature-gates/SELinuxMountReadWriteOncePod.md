---
title: SELinuxMountReadWriteOncePod
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.26"
  - stage: beta
    defaultValue: false
    fromVersion: "1.27"
    toVersion: "1.27"
  - stage: beta
    defaultValue: true
    fromVersion: "1.28"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    fromVersion: "1.36"
---
سرعت راه‌اندازی کانتینر را افزایش می‌دهد؛ به این صورت که kubelet می‌تواند حجم‌های (volumes) یک Pod را مستقیماً با برچسب SELinux صحیح mount کند، به‌جای آنکه برچسب هر فایل روی حجم‌ها را به‌صورت بازگشتی تغییر دهد. پیاده‌سازی اولیه بر حجم‌های ReadWriteOncePod تمرکز داشت.
