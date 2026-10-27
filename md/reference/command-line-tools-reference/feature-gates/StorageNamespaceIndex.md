---
title: StorageNamespaceIndex
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.30"
    toVersion: "1.32"
  - stage: deprecated
    defaultValue: true
    fromVersion: "1.33"


---
یک ایندکس‌کننده‌ی فضای نام (namespace) را برای منابعی که در سطح فضای نام تعریف می‌شوند، در کش API server فعال می‌کند تا عملیات list سریع‌تر انجام شود.
