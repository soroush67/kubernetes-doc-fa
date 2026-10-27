---
# Removed from Kubernetes
title: StreamingProxyRedirects
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: false
    fromVersion: "1.5"
    toVersion: "1.5"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.6"
    toVersion: "1.17"    
  - stage: deprecated 
    defaultValue: true
    fromVersion: "1.18"
    toVersion: "1.21"
  - stage: deprecated 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.24"

removed: true
---
به API server دستور می‌دهد که تغییر مسیرهای (redirect) ارسال‌شده از backend (یعنی kubelet) را برای درخواست‌های جریانی (streaming) رهگیری کند و دنبال نماید. درخواست‌های `exec`، `attach` و `port-forward` از نمونه‌های درخواست‌های جریانی هستند.
