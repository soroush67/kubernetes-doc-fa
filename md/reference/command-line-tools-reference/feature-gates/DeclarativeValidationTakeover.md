---
title: DeclarativeValidationTakeover
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: false
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: deprecated
    defaultValue: false
    fromVersion: "1.36"
    toVersion: "1.36"
  - stage: deprecated
    defaultValue: false
    locked: true
    fromVersion: "1.37"
---
منسوخ‌شده: این گیت با
[feature gate با نام `DeclarativeValidationBeta`](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidationBeta)
جایگزین شده است.

پیش از کوبرنتیز نسخه 1.36، این گیت خطاهای اعتبارسنجی اعلانی (declarative validation) را معتبر و مرجع قرار می‌داد و جایگزین خطاهای نوشته‌شده به‌صورت دستی برای قواعدی می‌شد که پیاده‌سازی اعلانی داشتند.

سرور API دیگر این گیت را در نظر نمی‌گیرد. به‌جای آن از `DeclarativeValidationBeta` استفاده کنید تا مشخص شود که آیا قواعد `+k8s:beta` اعمال شوند یا خیر.

این feature gate فقط روی مؤلفهٔ `kube-apiserver` عمل می‌کند.
