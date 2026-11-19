---
title: کنترل دسترسی به API
weight: 30
no_list: true
---

برای آشنایی با اینکه کوبرنتیز دسترسی به API را چگونه پیاده‌سازی و کنترل می‌کند، صفحهٔ [کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) را مطالعه کنید.

مستندات مرجع:

- [احراز هویت](/docs/reference/access-authn-authz/authentication/)
   - [احراز هویت با توکن‌های راه‌اندازی (Bootstrap Tokens)](/docs/reference/access-authn-authz/bootstrap-tokens/)
- [کنترل‌کننده‌های پذیرش (Admission Controllers)](/docs/reference/access-authn-authz/admission-controllers/)
   - [کنترل پذیرش پویا](/docs/reference/access-authn-authz/extensible-admission-controllers/)
   - [کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
- [مجوزدهی (Authorization)](/docs/reference/access-authn-authz/authorization/)
   - [کنترل دسترسی مبتنی بر نقش (RBAC)](/docs/reference/access-authn-authz/rbac/)
   - [کنترل دسترسی مبتنی بر ویژگی (ABAC)](/docs/reference/access-authn-authz/abac/)
   - [مجوزدهی نود](/docs/reference/access-authn-authz/node/)
   - [مجوزدهی از طریق وب‌هوک (Webhook)](/docs/reference/access-authn-authz/webhook/)
- [درخواست‌های امضای گواهی (Certificate Signing Requests)](/docs/reference/access-authn-authz/certificate-signing-requests/)
   - از جمله [تأیید CSR](/docs/reference/access-authn-authz/certificate-signing-requests/#approval-rejection)
     و [امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/#signing)
- حساب‌های سرویس (Service accounts)
  - [راهنمای توسعه‌دهندگان](/docs/tasks/configure-pod-container/configure-service-account/)
  - [مدیریت](/docs/reference/access-authn-authz/service-accounts-admin/)
- [احراز هویت و مجوزدهی kubelet](/docs/reference/access-authn-authz/kubelet-authn-authz/)
  - از جمله [راه‌اندازی TLS (TLS bootstrapping)](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) در kubelet
