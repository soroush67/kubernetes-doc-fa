---
title: CSIMigrationPortworx
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.24"
  - stage: beta
    defaultValue: false
    fromVersion: "1.25"
    toVersion: "1.30"
  - stage: beta
    defaultValue: true
    fromVersion: "1.31"
    toVersion: "1.32"
  - stage: stable
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"

removed: true
---
لایه‌های سازگاری (shim) و منطق ترجمه را فعال می‌کند تا عملیات حجم (volume) از افزونهٔ درون‌درختی (in-tree) Portworx به افزونهٔ CSI مربوط به Portworx هدایت شود.
این قابلیت مستلزم آن است که درایور CSI مربوط به Portworx در کلاستر نصب و پیکربندی شده باشد.
