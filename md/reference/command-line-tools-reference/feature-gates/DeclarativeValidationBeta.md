---
title: DeclarativeValidationBeta
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.36"
---
کلید ایمنی سراسری برای قوانین اعتبارسنجی در سطح بتا (`+k8s:beta`). در صورت مشاهده‌ی پسرفت‌ها (regressions)، این گیت را غیرفعال کنید تا آن قوانین به حالت سایه (shadow mode) بازگردند.

در حالت سایه، اعتبارسنجی اعلانی (declarative validation) همچنان اجرا می‌شود و عدم‌تطابق‌ها ثبت و اندازه‌گیری می‌شوند، اما درخواست‌ها را رد نمی‌کنند؛ اعتبارسنجی دست‌نویس همچنان مرجع نهایی باقی می‌ماند.

اعمال قوانین برای منابعی که از `WithDeclarativeEnforcement()` استفاده می‌کنند:

- بدون پیشوند: همیشه اعمال می‌شود، صرف‌نظر از این گیت.
- `+k8s:beta`: در صورتی که این گیت فعال باشد (حالت پیش‌فرض) اعمال می‌شود، در غیر این صورت در حالت سایه اجرا می‌شود.
- `+k8s:alpha`: همیشه در حالت سایه اجرا می‌شود.

این گیت مستقل از
[feature gate با نام `DeclarativeValidation`](/docs/reference/command-line-tools-reference/feature-gates/#DeclarativeValidation)
عمل می‌کند؛ این feature gate فقط گزارش‌دهی عدم‌تطابق‌ها را کنترل می‌کند.
