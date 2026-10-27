---
title: DefaultPodSysctls
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---

فیلد `defaultPodSysctls` را در [KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/) فعال می‌کند و به مدیران نود امکان می‌دهد مجموعه‌ای پیش‌فرض از پارامترهای هسته (sysctls) با دامنه فضای نام (namespaced) را مشخص کنند که `kubelet` آن‌ها را بر همهٔ Podهای موجود روی نود اعمال می‌کند. برای جزئیات بیشتر، به [تنظیم sysctlها برای همهٔ Podها](/docs/tasks/administer-cluster/sysctl-cluster/#setting-sysctls-for-all-pods) مراجعه کنید.
