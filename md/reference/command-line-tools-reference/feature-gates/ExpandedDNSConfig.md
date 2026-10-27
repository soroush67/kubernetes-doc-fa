---
title: ExpandedDNSConfig
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha 
    defaultValue: false
    fromVersion: "1.22"
    toVersion: "1.25"
  - stage: beta
    defaultValue: true
    fromVersion: "1.26"  
    toVersion: "1.27" 
  - stage: stable
    defaultValue: true
    fromVersion: "1.28"  
    toVersion: "1.29" 
removed: true
---
به kubelet و kube-apiserver اجازه می‌دهد تعداد بیشتری مسیر جستجوی DNS (DNS search path) و فهرست طولانی‌تری از این مسیرها را پشتیبانی کنند. این قابلیت به پشتیبانی از سوی container runtime نیاز دارد (Containerd: نسخه‌ی v1.5.6 یا بالاتر، CRI-O: نسخه‌ی v1.22 یا بالاتر). به بخش [پیکربندی گسترش‌یافته‌ی DNS](/docs/concepts/services-networking/dns-pod-service/#expanded-dns-configuration) مراجعه کنید.
