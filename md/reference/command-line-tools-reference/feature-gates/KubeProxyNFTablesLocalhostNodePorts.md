---
title: KubeProxyNFTablesLocalhostNodePorts
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"

---
امکان پروکسی کردن Serviceهای از نوع NodePort از طریق localhost را در حالت nftables در kube-proxy فعال می‌کند.
