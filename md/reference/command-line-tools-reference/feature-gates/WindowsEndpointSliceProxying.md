---
# Removed from Kubernetes
title: WindowsEndpointSliceProxying
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.20"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.21"
  - stage: stable
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.24"

removed: true
---
هنگامی که این قابلیت فعال باشد، kube-proxy که روی ویندوز اجرا می‌شود به‌جای Endpoints از EndpointSlices به‌عنوان منبع اصلی داده استفاده می‌کند و این امر بهبود مقیاس‌پذیری و کارایی را ممکن می‌سازد. به [فعال‌سازی Endpoint Slices](/docs/concepts/services-networking/endpoint-slices/) مراجعه کنید.
