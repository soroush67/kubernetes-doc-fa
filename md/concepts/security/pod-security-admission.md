---
reviewers:
- tallclair
- liggitt
title: Pod Security Admission
description: >
  مروری بر کنترل‌کنندهٔ Pod Security Admission که می‌تواند استانداردهای امنیتی Pod
  را اعمال کند.
content_type: concept
weight: 20
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

[استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/) در کوبرنتیز
سطوح ایزوله‌سازی متفاوتی را برای پادها تعریف می‌کنند. این استانداردها به شما اجازه می‌دهند تعریف کنید که
می‌خواهید رفتار پادها را به شیوه‌ای روشن و یکپارچه چگونه محدود کنید.

کوبرنتیز یک {{< glossary_tooltip text="کنترل‌کنندهٔ پذیرش"
term_id="admission-controller" >}} داخلی به نام _Pod Security_ برای اعمال استانداردهای امنیتی Pod ارائه می‌دهد. محدودیت‌های امنیتی Pod
هنگام ایجاد پادها در سطح {{< glossary_tooltip text="فضای نام" term_id="namespace" >}}
اعمال می‌شوند.

### اعمال داخلی Pod Security admission

این صفحه بخشی از مستندات کوبرنتیز v{{< skew currentVersion >}} است.
اگر نسخهٔ دیگری از کوبرنتیز را اجرا می‌کنید، به مستندات آن انتشار مراجعه کنید.

<!-- body -->

## سطوح امنیتی Pod

Pod Security admission الزاماتی را بر [Security
Context](/docs/tasks/configure-pod-container/security-context/) یک Pod و سایر فیلدهای مرتبط، مطابق با
سه سطح تعریف‌شده توسط [استانداردهای امنیتی
Pod](/docs/concepts/security/pod-security-standards) اعمال می‌کند: `privileged`، `baseline` و
`restricted`. برای بررسی عمیق این الزامات، به صفحهٔ [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards)
مراجعه کنید.

## برچسب‌های Pod Security Admission برای فضاهای نام

پس از فعال شدن این قابلیت یا نصب webhook، می‌توانید فضاهای نام را طوری پیکربندی کنید که حالت
کنترل پذیرشی را که می‌خواهید برای امنیت پاد در هر فضای نام استفاده کنید تعریف کنند. کوبرنتیز مجموعه‌ای از
{{< glossary_tooltip term_id="label" text="برچسب‌ها" >}} را تعریف می‌کند که می‌توانید آن‌ها را تنظیم کنید تا مشخص کنید کدام یک از
سطوح ازپیش‌تعریف‌شدهٔ استاندارد امنیتی Pod را می‌خواهید برای یک فضای نام استفاده کنید. برچسبی که انتخاب می‌کنید
تعیین می‌کند که {{< glossary_tooltip text="control plane" term_id="control-plane" >}}
در صورت تشخیص یک تخلف احتمالی چه اقدامی انجام دهد:

{{< table caption="حالت‌های Pod Security Admission" >}}
حالت | توضیح
:---------|:------------
**enforce** | تخلف از سیاست باعث رد شدن پاد می‌شود.
**audit** | تخلف از سیاست باعث افزوده شدن یک حاشیه‌نویسی ممیزی به رویداد ثبت‌شده در [لاگ ممیزی](/docs/tasks/debug/debug-cluster/audit/) می‌شود، اما در غیر این صورت مجاز است.
**warn** | تخلف از سیاست باعث نمایش هشداری به کاربر می‌شود، اما در غیر این صورت مجاز است.
{{< /table >}}

یک فضای نام می‌تواند هر یک یا همهٔ حالت‌ها را پیکربندی کند، یا حتی برای حالت‌های مختلف سطح متفاوتی تنظیم کند.

برای هر حالت، دو برچسب وجود دارد که سیاست مورد استفاده را تعیین می‌کنند:

```yaml
# The per-mode level label indicates which policy level to apply for the mode.
#
# MODE must be one of `enforce`, `audit`, or `warn`.
# LEVEL must be one of `privileged`, `baseline`, or `restricted`.
pod-security.kubernetes.io/<MODE>: <LEVEL>

# Optional: per-mode version label that can be used to pin the policy to the
# version that shipped with a given Kubernetes minor version (for example v{{< skew currentVersion >}}).
#
# MODE must be one of `enforce`, `audit`, or `warn`.
# VERSION must be a valid Kubernetes minor version, or `latest`.
pod-security.kubernetes.io/<MODE>-version: <VERSION>
```

برای دیدن نمونهٔ کاربرد، به [اعمال استانداردهای امنیتی Pod با برچسب‌های فضای نام](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels) مراجعه کنید.

## منابع بار کاری و قالب‌های Pod

پادها اغلب به‌صورت غیرمستقیم، با ایجاد یک [آبجکت
بار کاری](/docs/concepts/workloads/controllers/) مانند یک {{< glossary_tooltip
term_id="deployment" >}} یا {{< glossary_tooltip term_id="job">}}، ایجاد می‌شوند. آبجکت بار کاری
یک _قالب Pod_ تعریف می‌کند و یک {{< glossary_tooltip term_id="controller" text="کنترل‌کننده" >}} برای
منبع بار کاری، پادها را بر اساس آن قالب ایجاد می‌کند. برای کمک به شناسایی زودهنگام تخلفات، هر دو
حالت audit و warning بر منابع بار کاری اعمال می‌شوند. با این حال، حالت enforce بر منابع بار کاری
اعمال **نمی‌شود** و فقط بر آبجکت‌های پاد حاصل اعمال می‌شود.

## استثناها

می‌توانید _استثناهایی_ از اعمال امنیت پاد تعریف کنید تا ایجاد پادهایی که
در غیر این صورت به دلیل سیاست مرتبط با یک فضای نام مشخص ممنوع بودند مجاز شود.
استثناها را می‌توان به‌صورت ایستا در
[پیکربندی کنترل‌کنندهٔ پذیرش](/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller) پیکربندی کرد.

استثناها باید به‌صراحت برشمرده شوند. درخواست‌هایی که معیارهای استثنا را برآورده می‌کنند توسط
کنترل‌کنندهٔ پذیرش _نادیده گرفته می‌شوند_ (همهٔ رفتارهای `enforce`، `audit` و `warn` نادیده گرفته می‌شوند). ابعاد استثنا عبارت‌اند از:

- **نام‌های کاربری:** درخواست‌های کاربرانی که نام کاربری احراز هویت‌شده (یا جعل هویت‌شدهٔ) مستثنا دارند
  نادیده گرفته می‌شوند.
- **RuntimeClassNameها:** پادها و [منابع بار کاری](#workload-resources-and-pod-templates)ی که نام کلاس محیط اجرای مستثنا را مشخص می‌کنند
  نادیده گرفته می‌شوند.
- **فضاهای نام:** پادها و [منابع بار کاری](#workload-resources-and-pod-templates) در یک فضای نام مستثنا نادیده گرفته می‌شوند.

{{< caution >}}

بیشتر پادها توسط یک کنترل‌کننده در پاسخ به یک [منبع
بار کاری](#workload-resources-and-pod-templates) ایجاد می‌شوند، به این معنا که مستثنا کردن یک کاربر نهایی تنها
او را هنگام ایجاد مستقیم پادها از اعمال سیاست معاف می‌کند، اما نه هنگام ایجاد یک منبع بار کاری.
حساب‌های سرویس کنترل‌کننده‌ها (مانند `system:serviceaccount:kube-system:replicaset-controller`)
عموماً نباید مستثنا شوند، زیرا این کار به‌طور ضمنی هر کاربری را که بتواند
منبع بار کاری متناظر را ایجاد کند مستثنا می‌کند.

{{< /caution >}}

به‌روزرسانی‌های فیلدهای پاد زیر از بررسی‌های سیاست مستثنا هستند، به این معنا که اگر یک درخواست به‌روزرسانی پاد
فقط این فیلدها را تغییر دهد، رد نخواهد شد، حتی اگر پاد ناقض
سطح سیاست فعلی باشد:

- هرگونه به‌روزرسانی metadata **به‌جز** تغییرات در حاشیه‌نویسی‌های seccomp یا AppArmor:
  - `seccomp.security.alpha.kubernetes.io/pod` (منسوخ)
  - `container.seccomp.security.alpha.kubernetes.io/*` (منسوخ)
  - `container.apparmor.security.beta.kubernetes.io/*` (منسوخ)
- به‌روزرسانی‌های معتبر `.spec.activeDeadlineSeconds`
- به‌روزرسانی‌های معتبر `.spec.tolerations`

## متریک‌ها

در اینجا متریک‌های Prometheus که توسط kube-apiserver در معرض دسترسی قرار می‌گیرند آمده است:

- `pod_security_errors_total`: این متریک تعداد خطاهایی را نشان می‌دهد که مانع ارزیابی عادی می‌شوند.
  خطاهای غیرمهلک ممکن است باعث شوند جدیدترین پروفایل restricted برای اعمال استفاده شود.
- `pod_security_evaluations_total`: این متریک تعداد ارزیابی‌های سیاستی را که رخ داده‌اند نشان می‌دهد،
  بدون احتساب درخواست‌های نادیده‌گرفته‌شده یا مستثنا در طول صادرسازی.
- `pod_security_exemptions_total`: این متریک تعداد درخواست‌های مستثنا را نشان می‌دهد، بدون احتساب درخواست‌های
  نادیده‌گرفته‌شده یا خارج از دامنه.

## {{% heading "whatsnext" %}}

- [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards)
- [اعمال استانداردهای امنیتی Pod](/docs/setup/best-practices/enforcing-pod-security-standards)
- [اعمال استانداردهای امنیتی Pod با پیکربندی کنترل‌کنندهٔ پذیرش داخلی](/docs/tasks/configure-pod-container/enforce-standards-admission-controller)
- [اعمال استانداردهای امنیتی Pod با برچسب‌های فضای نام](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels)

اگر نسخهٔ قدیمی‌تری از کوبرنتیز را اجرا می‌کنید و می‌خواهید به نسخه‌ای از کوبرنتیز
ارتقا دهید که PodSecurityPolicyها را در بر ندارد،
[مهاجرت از PodSecurityPolicy به کنترل‌کنندهٔ پذیرش داخلی PodSecurity](/docs/tasks/configure-pod-container/migrate-from-psp) را مطالعه کنید.
