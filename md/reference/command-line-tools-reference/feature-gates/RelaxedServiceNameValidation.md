---
title: RelaxedServiceNameValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.34"
    toVersion: "1.35"
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: stable
    locked: true
    defaultValue: true
    fromVersion: "1.37"

---

اعتبارسنجی سهل‌گیرانه‌تر را برای نام آبجکت‌های Service فعال می‌کند و به‌جای [نام‌های برچسب RFC 1035](/docs/concepts/overview/working-with-objects/names/#rfc-1035-label-names)، استفاده از [نام‌های برچسب RFC 1123](/docs/concepts/overview/working-with-objects/names/#dns-label-names) را مجاز می‌سازد.

این قابلیت اجازه می‌دهد نام آبجکت‌های Service با یک رقم آغاز شود.
