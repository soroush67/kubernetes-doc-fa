---
# Removed from Kubernetes
title: CSIMigrationAWSComplete
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
ثبت افزونه درون‌درخت (in-tree) مربوط به EBS را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند و منطق shim و ترجمه را فعال می‌کند تا عملیات حجم از افزونه درون‌درخت AWS-EBS به افزونه EBS CSI هدایت شود. این قابلیت نیازمند فعال بودن feature flagهای CSIMigration و CSIMigrationAWS و همچنین نصب و پیکربندی افزونه EBS CSI روی همه نودهای کلاستر است. این flag به نفع feature flag با نام `InTreePluginAWSUnregister` منسوخ شده است که از ثبت افزونه درون‌درخت EBS جلوگیری می‌کند.
