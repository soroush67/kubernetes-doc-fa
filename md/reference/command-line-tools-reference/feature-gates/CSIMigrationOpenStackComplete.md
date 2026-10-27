---
# Removed from Kubernetes
title: CSIMigrationOpenStackComplete
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
ثبت افزونه درون‌درختی (in-tree) Cinder را در kubelet و کنترل‌کننده‌های حجم (volume) متوقف می‌کند و shimها و منطق ترجمه را فعال می‌کند تا عملیات حجم از افزونه درون‌درختی Cinder به افزونه Cinder CSI هدایت شود.
این قابلیت نیازمند فعال بودن feature flagهای CSIMigration و CSIMigrationOpenStack است و همچنین لازم است افزونه Cinder CSI روی همه نودهای کلاستر نصب و پیکربندی شده باشد. این فلگ به نفع feature flag با نام `InTreePluginOpenStackUnregister` منسوخ شده است؛ این feature flag از ثبت افزونه درون‌درختی openstack cinder جلوگیری می‌کند.
