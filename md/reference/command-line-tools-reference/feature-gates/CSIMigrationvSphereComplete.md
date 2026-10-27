---
# Removed from Kubernetes
title: CSIMigrationvSphereComplete
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: false
    fromVersion: "1.19"
    toVersion: "1.21"
  - stage: deprecated
    fromVersion: "1.22"
    toVersion: "1.22"

removed: true  
---
ثبت پلاگین درون‌درخت (in-tree) مربوط به vSphere را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند و shimها و منطق ترجمه را فعال می‌سازد تا عملیات مربوط به حجم‌ها از پلاگین درون‌درخت vSphere به پلاگین CSI مربوط به vSphere هدایت شوند. این قابلیت مستلزم فعال بودن feature flagهای CSIMigration و CSIMigrationvSphere و نصب و پیکربندی پلاگین CSI مربوط به vSphere روی تمامی نودهای کلاستر است. این feature flag به نفع feature flag با نام `InTreePluginvSphereUnregister` منسوخ شده است؛ این feature flag از ثبت پلاگین درون‌درخت vSphere جلوگیری می‌کند.
