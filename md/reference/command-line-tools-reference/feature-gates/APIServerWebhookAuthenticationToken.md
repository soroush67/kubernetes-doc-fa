---
title: APIServerWebhookAuthenticationToken
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.37"
---
به `kube-apiserver` امکان می‌دهد توکن‌های ServiceAccount کوتاه‌مدت و با دامنه محدود را برای احراز هویت در
[admission webhookها](/docs/reference/access-authn-authz/extensible-admission-controllers/#authenticating-to-admission-webhooks)
صادر کند.
این توکن‌ها به یک ValidatingWebhookConfiguration یا MutatingWebhookConfiguration مشخص متصل هستند و از طریق
ادعاهای تأیید (attestation claims) در API
[TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
به گروه‌های API خاصی محدود می‌شوند.
