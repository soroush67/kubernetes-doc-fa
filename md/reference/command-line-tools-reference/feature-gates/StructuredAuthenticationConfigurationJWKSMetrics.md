---
title: StructuredAuthenticationConfigurationJWKSMetrics
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta 
    defaultValue: true
    fromVersion: "1.35"
---
فعال‌سازی متریک‌های اضافی برای عملیات JSON Web Key Set (JWKS) در احرازهویت‌کننده‌های JWT
که از طریق `--authentication-config` پیکربندی شده‌اند. هنگامی که این قابلیت فعال باشد، API server
متریک‌هایی را درباره‌ی آخرین زمان دریافت JWKS و مقدار هش پاسخ JWKS ثبت می‌کند.
برای جزئیات بیشتر، [مرجع متریک‌ها](/docs/reference/instrumentation/metrics/) را ببینید.
