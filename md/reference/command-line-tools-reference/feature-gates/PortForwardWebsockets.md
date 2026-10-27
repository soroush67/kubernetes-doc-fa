---
title: PortForwardWebsockets
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.30"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
---
امکان استریم از طریق WebSocket برای زیرپروتکل portforward (`port-forward`) را برای کلاینت‌هایی فراهم می‌کند که نسخه v2 (`v2.portforward.k8s.io`) این زیرپروتکل را درخواست می‌کنند.
