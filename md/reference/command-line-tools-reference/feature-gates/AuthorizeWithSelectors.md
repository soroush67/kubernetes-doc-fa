---
title: AuthorizeWithSelectors
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.31"
    toVersion: "1.31"
  - stage: beta
    defaultValue: true
    fromVersion: "1.32"
    toVersion: "1.33"
  - stage: stable
    defaultValue: true
    fromVersion: "1.34"
---
به فرایند احراز مجوز (authorization) اجازه می‌دهد از انتخابگرهای فیلد و برچسب (field و label selector) استفاده کند.
فیلدهای `fieldSelector` و `labelSelector` را در [SubjectAccessReview API](/docs/reference/kubernetes-api/definitions/subject-access-review-v1-authorization/) فعال می‌کند،
اطلاعات انتخابگرهای فیلد و برچسب را به [وب‌هوک‌های احراز مجوز](/docs/reference/access-authn-authz/webhook/) ارسال می‌کند،
توابع `fieldSelector` و `labelSelector` را در [کتابخانه CEL مربوط به authorizer](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#AuthzSelectors) فعال می‌کند،
و بررسی فیلدهای `fieldSelector` و `labelSelector` را در [`matchConditions` وب‌هوک احراز مجوز](/docs/reference/access-authn-authz/authorization/#using-configuration-file-for-authorization) امکان‌پذیر می‌سازد.
