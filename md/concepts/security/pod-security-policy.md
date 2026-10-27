---
title: سیاست‌های امنیتی Pod
content_type: concept
weight: 30
---

<!-- overview -->

{{% alert title="قابلیت حذف‌شده" color="warning" %}}
PodSecurityPolicy در کوبرنتیز v1.21 [منسوخ شد](/blog/2021/04/08/kubernetes-1-21-release-announcement/#podsecuritypolicy-deprecation)
و در v1.25 از کوبرنتیز حذف شد.
{{% /alert %}}

به‌جای استفاده از PodSecurityPolicy، می‌توانید محدودیت‌های مشابهی را بر پادها با استفاده از
یکی یا هر دوی موارد زیر اعمال کنید:

- [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
- یک افزونهٔ پذیرش شخص ثالث که خودتان آن را مستقر و پیکربندی می‌کنید

برای راهنمای مهاجرت، به [مهاجرت از PodSecurityPolicy به کنترل‌کنندهٔ پذیرش داخلی PodSecurity](/docs/tasks/configure-pod-container/migrate-from-psp/) مراجعه کنید.
برای اطلاعات بیشتر دربارهٔ حذف این API،
به [منسوخ شدن PodSecurityPolicy: گذشته، حال و آینده](/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/) مراجعه کنید.

اگر کوبرنتیز v{{< skew currentVersion >}} را اجرا نمی‌کنید، مستندات مربوط به
نسخهٔ کوبرنتیز خود را بررسی کنید.
