---
# Removed from Kubernetes
title: BoundServiceAccountTokenVolume
content_type: feature_gate

_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.13"
    toVersion: "1.20"
  - stage: beta 
    defaultValue: true
    fromVersion: "1.21"
    toVersion: "1.21"    
  - stage: stable
    defaultValue: true
    fromVersion: "1.22"
    toVersion: "1.23"    

removed: true
---
حجم‌های ServiceAccount را به‌گونه‌ای مهاجرت می‌دهد که از یک projected volume متشکل از ServiceAccountTokenVolumeProjection استفاده کنند. مدیران کلاستر می‌توانند با استفاده از متریک
`serviceaccount_stale_tokens_total` بارهای کاری‌ای را که به توکن‌های توسعه‌یافته (extended tokens) وابسته هستند پایش کنند. اگر چنین بار کاری‌ای وجود ندارد، با اجرای `kube-apiserver` همراه با
فلگ `--service-account-extend-token-expiration=false` توکن‌های توسعه‌یافته را غیرفعال کنید.

برای جزئیات بیشتر، [Bound Service Account Tokens](https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1205-bound-service-account-tokens/README.md) را مطالعه کنید.
