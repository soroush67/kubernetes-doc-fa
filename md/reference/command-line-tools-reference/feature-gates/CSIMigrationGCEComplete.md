---
# Removed from Kubernetes
title: CSIMigrationGCEComplete
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
ثبت افزونه درون‌درخت (in-tree) مربوط به GCE-PD را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند و منطق shim و ترجمه را فعال می‌سازد تا عملیات مربوط به حجم‌ها از افزونه درون‌درخت GCE-PD به افزونه PD CSI هدایت شود. این قابلیت مستلزم فعال بودن feature flagهای `CSIMigration` و `CSIMigrationGCE` و همچنین نصب و پیکربندی افزونه PD CSI روی تمامی نودهای کلاستر است. این flag به نفع feature flag با نام `InTreePluginGCEUnregister` منسوخ شده است؛ این feature flag از ثبت افزونه درون‌درخت GCE PD جلوگیری می‌کند.
