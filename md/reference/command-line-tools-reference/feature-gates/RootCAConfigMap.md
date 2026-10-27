---
# Removed from Kubernetes
title: RootCAConfigMap
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.13"
    toVersion: "1.19"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.20"
    toVersion: "1.20"
  - stage: stable
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.22"

removed: true
---
`kube-controller-manager` را طوری پیکربندی می‌کند که یک
{{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} با نام `kube-root-ca.crt`
را در هر فضای نام (namespace) منتشر کند. این ConfigMap شامل یک بسته CA (CA bundle) است که برای تأیید اتصال‌ها
به kube-apiserver استفاده می‌شود. برای جزئیات بیشتر، به
[Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md)
مراجعه کنید.
