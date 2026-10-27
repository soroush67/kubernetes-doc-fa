---
# Removed from Kubernetes
title: CSIMigrationAzureFileComplete
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
ثبت پلاگین درون‌درخت (in-tree) Azure-File را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند و shimها و منطق ترجمه را فعال می‌کند تا عملیات مربوط به حجم‌ها را از پلاگین درون‌درخت Azure-File به پلاگین AzureFile CSI هدایت کند. این قابلیت نیازمند آن است که feature flagهای CSIMigration و CSIMigrationAzureFile فعال باشند و پلاگین AzureFile CSI روی همه نودهای کلاستر نصب و پیکربندی شده باشد. این flag به نفع feature flag با نام `InTreePluginAzureFileUnregister` منسوخ شده است؛ این feature flag از ثبت پلاگین درون‌درخت AzureFile جلوگیری می‌کند.
