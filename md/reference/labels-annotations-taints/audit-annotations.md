---
title: "حاشیه‌نویسی‌های ممیزی"
weight: 10
---

<!-- overview -->

این صفحه مرجعی برای حاشیه‌نویسی‌های ممیزی (audit annotations) در فضای نام (namespace) `kubernetes.io` است. این حاشیه‌نویسی‌ها بر آبجکت `Event` از گروه API `audit.k8s.io` اعمال می‌شوند.

{{< note >}}
حاشیه‌نویسی‌های زیر در API کوبرنتیز استفاده نمی‌شوند. وقتی [ممیزی را در کلاستر خود فعال می‌کنید](/docs/tasks/debug/debug-cluster/audit/)، داده‌های رویدادهای ممیزی با استفاده از `Event` از گروه API `audit.k8s.io` نوشته می‌شوند. این حاشیه‌نویسی‌ها بر رویدادهای ممیزی اعمال می‌شوند. رویدادهای ممیزی با آبجکت‌های [Event API](/docs/reference/kubernetes-api/cluster-resources/event-v1/) (گروه API `events.k8s.io`) تفاوت دارند.
{{< /note >}}

<!-- body -->

## k8s.io/deprecated

نمونه: `k8s.io/deprecated: "true"`

مقدار این حاشیه‌نویسی **باید** "true" یا "false" باشد. مقدار "true" نشان می‌دهد که درخواست از یک نسخه منسوخ‌شده API استفاده کرده است.

## k8s.io/removed-release

نمونه: `k8s.io/removed-release: "1.22"`

مقدار این حاشیه‌نویسی **باید** در قالب "\<MAJOR>\.\<MINOR>\" باشد. برای درخواست‌هایی که به نسخه‌های منسوخ‌شده API دارای نسخه هدف حذف ارسال می‌شوند، این مقدار برابر با همان نسخه‌ای قرار می‌گیرد که حذف در آن انجام خواهد شد.

## pod-security.kubernetes.io/exempt

نمونه: `pod-security.kubernetes.io/exempt: namespace`

مقدار این حاشیه‌نویسی **باید** یکی از `user`، `namespace` یا `runtimeClass` باشد که با ابعاد [معافیت Pod Security](/docs/concepts/security/pod-security-admission/#exemptions) مطابقت دارند. این حاشیه‌نویسی نشان می‌دهد که معافیت از اعمال PodSecurity بر اساس کدام بُعد انجام شده است.


## pod-security.kubernetes.io/enforce-policy

نمونه: `pod-security.kubernetes.io/enforce-policy: restricted:latest`

مقدار این حاشیه‌نویسی **باید** `privileged:<version>`، `baseline:<version>` یا `restricted:<version>` باشد. این مقادیر با سطوح [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards) مطابقت دارند و همراه با نسخه‌ای می‌آیند که **باید** `latest` یا یک نسخه معتبر کوبرنتیز در قالب `v<MAJOR>.<MINOR>` باشد. این حاشیه‌نویسی سطح اعمالی را مشخص می‌کند که در مرحله پذیرش PodSecurity، آن Pod را مجاز یا رد کرده است.

برای اطلاعات بیشتر، [استانداردهای امنیت Pod](/docs/concepts/security/pod-security-standards/) را ببینید.

## pod-security.kubernetes.io/audit-violations

نمونه:  `pod-security.kubernetes.io/audit-violations: would violate
PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container
"example" must set securityContext.allowPrivilegeEscalation=false), ...`

مقدار این حاشیه‌نویسی جزئیات نقض یک سیاست ممیزی را شرح می‌دهد. این مقدار شامل سطح [استاندارد امنیت Pod](/docs/concepts/security/pod-security-standards/) نقض‌شده و نیز سیاست‌های مشخصی است که در اعمال PodSecurity روی فیلدها نقض شده‌اند.

برای اطلاعات بیشتر، [استانداردهای امنیت Pod](/docs/concepts/security/pod-security-standards/) را ببینید.

## audit.k8s.io/truncated

نمونه: `audit.k8s.io/truncated: "true"`

مقدار این حاشیه‌نویسی همیشه "true" است. این حاشیه‌نویسی نشان می‌دهد که رویداد ممیزی کوتاه شده است، زیرا اندازه آن از حداکثر پیکربندی‌شده فراتر رفته است. کوتاه‌سازی به‌طور پیش‌فرض غیرفعال است و باید به‌صراحت از طریق فلگ‌های API server فعال شود.

برای اطلاعات بیشتر، [ممیزی](/docs/tasks/debug/debug-cluster/audit/) را ببینید.

## apiserver.latency.k8s.io/etcd

نمونه: `apiserver.latency.k8s.io/etcd: "4.730661757s"`

این حاشیه‌نویسی میزان تأخیر ایجادشده در لایه ذخیره‌سازی را نشان می‌دهد و زمان لازم برای ارسال داده به etcd و دریافت کامل پاسخ را در بر می‌گیرد.

مقدار این حاشیه‌نویسی ممیزی شامل زمان صرف‌شده برای پذیرش یا اعتبارسنجی نمی‌شود.

## apiserver.latency.k8s.io/decode-response-object

نمونه: `apiserver.latency.k8s.io/decode-response-object: "450.6649ns"`

این حاشیه‌نویسی زمان صرف‌شده برای رمزگشایی پاسخ دریافتی از لایه ذخیره‌سازی (etcd) را ثبت می‌کند.

## apiserver.latency.k8s.io/apf-queue-wait

نمونه: `apiserver.latency.k8s.io/apf-queue-wait: "100ns"`

این حاشیه‌نویسی مدت زمانی را ثبت می‌کند که یک درخواست به دلیل اولویت‌های API server در صف مانده است.

برای اطلاعات بیشتر درباره این سازوکار، [اولویت و انصاف API](/docs/concepts/cluster-administration/flow-control/) (APF) را ببینید.

## authorization.k8s.io/decision

نمونه: `authorization.k8s.io/decision: "forbid"`

مقدار این حاشیه‌نویسی باید **forbid** یا **allow** باشد. این حاشیه‌نویسی در لاگ‌های ممیزی کوبرنتیز نشان می‌دهد که آیا درخواست مجاز شناخته شده است یا خیر.

برای اطلاعات بیشتر، [ممیزی](/docs/tasks/debug/debug-cluster/audit/) را ببینید.

## authorization.k8s.io/reason

نمونه: `authorization.k8s.io/reason: "Human-readable reason for the decision"`

این حاشیه‌نویسی دلیل [تصمیم](#authorization-k8s-io-decision) ثبت‌شده در لاگ‌های ممیزی کوبرنتیز را بیان می‌کند.

برای اطلاعات بیشتر، [ممیزی](/docs/tasks/debug/debug-cluster/audit/) را ببینید.

## missing-san.invalid-cert.kubernetes.io/$hostname

نمونه: `missing-san.invalid-cert.kubernetes.io/example-svc.example-namespace.svc: "relies on a legacy Common Name field instead of the SAN extension for subject validation"`

در کوبرنتیز نسخه v1.24 و نسخه‌های بعدی استفاده می‌شود.

این حاشیه‌نویسی نشان می‌دهد که یک webhook یا API server تجمیعی از گواهی نامعتبری استفاده می‌کند که `subjectAltNames` ندارد. پشتیبانی از این گواهی‌ها در کوبرنتیز 1.19 به‌طور پیش‌فرض غیرفعال شد و در کوبرنتیز 1.23 حذف شد.

درخواست‌های ارسال‌شده به endpointهایی که از این گواهی‌ها استفاده می‌کنند، با شکست مواجه می‌شوند. سرویس‌هایی که از این گواهی‌ها استفاده می‌کنند باید هرچه زودتر آن‌ها را جایگزین کنند تا هنگام اجرا در محیط‌های کوبرنتیز 1.23 و بالاتر دچار اختلال نشوند.

اطلاعات بیشتر در این باره در مستندات Go آمده است: [X.509 CommonName deprecation](https://go.dev/doc/go1.15#commonname).

## insecure-sha1.invalid-cert.kubernetes.io/$hostname

نمونه: `insecure-sha1.invalid-cert.kubernetes.io/example-svc.example-namespace.svc: "uses an insecure SHA-1 signature"`

در کوبرنتیز نسخه v1.24 و نسخه‌های بعدی استفاده می‌شود.

این حاشیه‌نویسی نشان می‌دهد که یک webhook یا API server تجمیعی از گواهی ناامنی استفاده می‌کند که با هش SHA-1 امضا شده است. پشتیبانی از این گواهی‌های ناامن در کوبرنتیز 1.24 به‌طور پیش‌فرض غیرفعال است و در نسخه‌ای در آینده حذف خواهد شد.

سرویس‌هایی که از این گواهی‌ها استفاده می‌کنند باید هرچه زودتر آن‌ها را جایگزین کنند تا اتصال‌ها به‌درستی ایمن شوند و در نسخه‌های آینده اختلالی پیش نیاید.

اطلاعات بیشتر در این باره در مستندات Go آمده است: [Rejecting SHA-1 certificates](https://go.dev/doc/go1.18#sha1).

## validation.policy.admission.k8s.io/validation_failure

نمونه: `validation.policy.admission.k8s.io/validation_failure: '[{"message": "Invalid value", {"policy": "policy.example.com", {"binding": "policybinding.example.com", {"expressionIndex": "1", {"validationActions": ["Audit"]}]'`

در کوبرنتیز نسخه v1.27 و نسخه‌های بعدی استفاده می‌شود.

این حاشیه‌نویسی نشان می‌دهد که نتیجه اعتبارسنجی یک سیاست پذیرش برای یک درخواست API برابر با false بوده است، یا اینکه اعتبارسنجی در حالی به خطا انجامیده که سیاست با `failurePolicy: Fail` پیکربندی شده بوده است.

مقدار این حاشیه‌نویسی یک آبجکت JSON است. فیلد `message` در این JSON پیام مربوط به شکست اعتبارسنجی را ارائه می‌کند.

فیلدهای `policy`، `binding` و `expressionIndex` در این JSON به‌ترتیب نام `ValidatingAdmissionPolicy`، نام `ValidatingAdmissionPolicyBinding` و اندیس عبارت‌های CEL ناموفق در فهرست `validations` سیاست را مشخص می‌کنند.

فیلد `validationActions` نشان می‌دهد که برای این شکست اعتبارسنجی چه اقداماتی انجام شده است. برای جزئیات بیشتر درباره `validationActions`، [سیاست پذیرش اعتبارسنجی](/docs/reference/access-authn-authz/validating-admission-policy/) را ببینید.
