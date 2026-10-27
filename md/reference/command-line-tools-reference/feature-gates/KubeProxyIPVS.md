---
title: KubeProxyIPVS
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.37"
---

پشتیبانی از [حالت پراکسی `ipvs`](/docs/reference/networking/virtual-ips/#proxy-mode-ipvs) منسوخ‌شده را در kube-proxy فعال می‌کند.
