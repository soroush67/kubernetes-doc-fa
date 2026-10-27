---
# Removed from Kubernetes
title: PodShareProcessNamespace
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.10"
    toVersion: "1.11"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.12"
    toVersion: "1.16"
  - stage: stable
    defaultValue: true
    fromVersion: "1.17"
    toVersion: "1.19"

removed: true
---
امکان تنظیم `shareProcessNamespace` را در یک Pod فراهم می‌کند تا یک فضای نام فرایند (process namespace) واحد بین کانتینرهایی که در همان Pod اجرا می‌شوند به اشتراک گذاشته شود. جزئیات بیشتر را می‌توانید در
[اشتراک‌گذاری فضای نام فرایند بین کانتینرها در یک Pod](/docs/tasks/configure-pod-container/share-process-namespace/) بیابید.
