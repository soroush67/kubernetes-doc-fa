---
title: LoadBalancerIPMode
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.29"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.31"
  - stage: stable
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.34"

removed: true
---
امکان تنظیم `ipMode` را برای Serviceهایی فراهم می‌کند که مقدار `type` آن‌ها برابر `LoadBalancer` است.
برای اطلاعات بیشتر، به [مشخص‌کردن IPMode در وضعیت load balancer](/docs/concepts/services-networking/service/#load-balancer-ip-mode) مراجعه کنید.
