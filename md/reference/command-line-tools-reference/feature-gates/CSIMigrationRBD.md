---
title: CSIMigrationRBD
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.23"
    toVersion: "1.27"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.28"
    toVersion: "1.30"

removed: true
---
شیم‌ها (shims) و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم (volume) از افزونه درون‌درختی (in-tree) RBD به افزونه Ceph RBD CSI هدایت شود. این قابلیت نیازمند آن است که feature flagهای CSIMigration و csiMigrationRBD فعال باشند و افزونه Ceph CSI در کلاستر نصب و پیکربندی شده باشد.

این feature gate به نفع feature gate با نام `InTreePluginRBDUnregister` منسوخ شد؛ این feature gate از ثبت افزونه درون‌درختی RBD جلوگیری می‌کند.
