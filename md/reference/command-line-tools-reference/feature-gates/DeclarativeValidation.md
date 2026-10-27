---
title: DeclarativeValidation
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.33"
    toVersion: "1.35"
  - stage: stable
    defaultValue: true
    locked: true
    fromVersion: "1.36"
---
اختلاف‌های میان اعتبارسنجی اعلانی (declarative validation) در APIهای درون‌درخت (in-tree) کوبرنتیز و اعتبارسنجی دست‌نویس معادل آن‌ها را گزارش می‌کند.

هنگامی که این قابلیت فعال باشد، قواعدی که با `+k8s:alpha` یا `+k8s:beta` علامت‌گذاری شده‌اند در کنار اعتبارسنجی دست‌نویس اجرا می‌شوند و API server هر گونه ناهمخوانی را ثبت (log) می‌کند و آن را در متریک `declarative_validation_mismatch_total` می‌شمارد.

این gate فقط گزارش‌دهی را کنترل می‌کند و تعیین نمی‌کند که API server کدام نتیجه را بازگرداند. وضعیت اعمال‌شدن قواعد به شرح زیر است:

- بدون پیشوند: همواره اعمال می‌شود.
- `+k8s:beta`: زمانی اعمال می‌شود که
  [feature gate با نام `DeclarativeValidationBeta`](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidationBeta)
  فعال باشد (که حالت پیش‌فرض است).
- `+k8s:alpha`: هرگز اعمال نمی‌شود.

این feature gate فقط روی مؤلفه `kube-apiserver` عمل می‌کند.
