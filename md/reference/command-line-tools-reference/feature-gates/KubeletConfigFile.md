---
# Removed from Kubernetes
title: KubeletConfigFile
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.8"
    toVersion: "1.9"
  - stage: deprecated
    fromVersion: "1.10"
    toVersion: "1.10"

removed: true
---
امکان بارگذاری پیکربندی kubelet را از یک فایل فراهم می‌کند که با استفاده از یک فایل پیکربندی مشخص می‌شود.
برای جزئیات بیشتر، به [تنظیم پارامترهای kubelet از طریق فایل پیکربندی](/docs/tasks/administer-cluster/kubelet-config-file/) مراجعه کنید.
