---
title: کنترل دسترسی به API
weight: 30
no_list: true
---

برای آشنایی با نحوه پیاده‌سازی و کنترل دسترسی به API در کوبرنتیز،
[کنترل دسترسی به API کوبرنتیز](/docs/concepts/security/controlling-access/) را مطالعه کنید.

مستندات مرجع:

- [احراز هویت](/docs/reference/access-authn-authz/authentication/)
   - [احراز هویت با Bootstrap Tokenها](/docs/reference/access-authn-authz/bootstrap-tokens/)
- [Admission Controllerها](/docs/reference/access-authn-authz/admission-controllers/)
   - [کنترل پذیرش پویا](/docs/reference/access-authn-authz/extensible-admission-controllers/)
   - [کنترل پذیرش مبتنی بر مانیفست](/docs/reference/access-authn-authz/manifest-admission-control/)
- [مجوزدهی](/docs/reference/access-authn-authz/authorization/)
   - [کنترل دسترسی مبتنی بر نقش (RBAC)](/docs/reference/access-authn-authz/rbac/)
   - [کنترل دسترسی مبتنی بر ویژگی (ABAC)](/docs/reference/access-authn-authz/abac/)
   - [مجوزدهی نود](/docs/reference/access-authn-authz/node/)
   - [مجوزدهی Webhook](/docs/reference/access-authn-authz/webhook/)
- [درخواست‌های امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/)
   - شامل [تأیید CSR](/docs/reference/access-authn-authz/certificate-signing-requests/#approval-rejection)
     و [امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/#signing)
- Service accountها
  - [راهنمای توسعه‌دهندگان](/docs/tasks/configure-pod-container/configure-service-account/)
  - [مدیریت](/docs/reference/access-authn-authz/service-accounts-admin/)
- [احراز هویت و مجوزدهی Kubelet](/docs/reference/access-authn-authz/kubelet-authn-authz/)
  - شامل [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) برای kubelet
