---
title: UserNamespacesHostNetworkSupport
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.35"
---
هنگامی که این ویژگی فعال باشد، Podها می‌توانند به‌طور همزمان از `hostNetwork` و [User Namespaceها](/docs/concepts/workloads/pods/user-namespaces) استفاده کنند.
