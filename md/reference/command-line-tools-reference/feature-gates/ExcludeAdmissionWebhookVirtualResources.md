---
title: ExcludeAdmissionWebhookVirtualResources
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: beta
    defaultValue: true
    fromVersion: "1.37"
---
منابع احراز هویت و مجوزدهی که ذخیره (persist) نمی‌شوند (منابع مجازی)، مانند `TokenReview` و `SubjectAccessReview`، را از admission webhookها مستثنا می‌کند.
این رفتار با مجموعه منابعی که ValidatingAdmissionPolicy و MutatingAdmissionPolicy از پیش مستثنا می‌کنند هم‌خوان است و مانع می‌شود که یک webhook معیوب درخواست‌های احراز هویت و مجوزدهی خودِ کلاستر را مسدود کند.
برای بازگرداندن رفتار قبلی، یعنی ارسال درخواست‌های admission webhook برای این منابع، این feature gate را غیرفعال کنید.
