---
# Removed from Kubernetes
title: CSIMigrationAzureDiskComplete
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.17"
    toVersion: "1.20"
  - stage: deprecated
    fromVersion: "1.21"
    toVersion: "1.21"

removed: true
---
ثبت افزونه درون‌درخت (in-tree) مربوط به Azure-Disk را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند و shimها و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم‌ها را از افزونه درون‌درخت Azure-Disk به افزونه AzureDisk CSI هدایت کنند. این قابلیت مستلزم فعال بودن feature flagهای CSIMigration و CSIMigrationAzureDisk و نیز نصب و پیکربندی افزونه AzureDisk CSI روی همه نودهای کلاستر است. این پرچم به نفع feature flag با نام `InTreePluginAzureDiskUnregister` که از ثبت افزونه درون‌درخت AzureDisk جلوگیری می‌کند، منسوخ شده است.
