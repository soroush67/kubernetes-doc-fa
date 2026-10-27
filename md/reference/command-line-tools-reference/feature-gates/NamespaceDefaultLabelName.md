---
# Removed from Kubernetes
title: NamespaceDefaultLabelName
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: stable
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.23"

removed: true
---
API Server را طوری پیکربندی می‌کند که یک {{< glossary_tooltip text="برچسب" term_id="label" >}} تغییرناپذیر با نام `kubernetes.io/metadata.name` را روی تمام فضاهای نام (namespace) تنظیم کند، به‌طوری که این برچسب حاوی نام فضای نام باشد.
