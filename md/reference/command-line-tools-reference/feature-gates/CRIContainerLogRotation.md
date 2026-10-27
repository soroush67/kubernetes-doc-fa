---
# Removed from Kubernetes
title: CRIContainerLogRotation
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.10"
    toVersion: "1.10"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.11"
    toVersion: "1.20"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"    

removed: true
---
فعال‌سازی چرخش لاگ (log rotation) کانتینر برای container runtime از نوع CRI.
حداکثر اندازه پیش‌فرض یک فایل لاگ ۱۰ مگابایت است و حداکثر تعداد پیش‌فرض
فایل‌های لاگ مجاز برای هر کانتینر ۵ عدد است.
این مقادیر را می‌توان در پیکربندی kubelet تنظیم کرد.
برای جزئیات بیشتر، به [لاگ‌گیری در سطح نود](/docs/concepts/cluster-administration/logging/#logging-at-the-node-level)
مراجعه کنید.
