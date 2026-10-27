---
title: Feature Gates (حذف‌شده)
weight: 15
content_type: concept
---

<!-- overview -->

این صفحه فهرستی از feature gateهایی را در بر دارد که حذف شده‌اند. اطلاعات این صفحه صرفاً جنبه مرجع دارد.
feature gate حذف‌شده با feature gate‌ای که به مرحلهٔ GA رسیده یا منسوخ (deprecated) شده است تفاوت دارد؛ زیرا
feature gate حذف‌شده دیگر به‌عنوان یک feature gate معتبر شناسایی نمی‌شود.
در مقابل، feature gate در مرحلهٔ GA یا منسوح‌شده همچنان توسط مؤلفه‌های مربوطهٔ کوبرنتیز شناسایی می‌شود،
هرچند دیگر نمی‌تواند هیچ تفاوتی در رفتار کلاستر ایجاد کند.

برای feature gateهایی که هنوز توسط مؤلفه‌های کوبرنتیز شناسایی می‌شوند، لطفاً به
[جدول feature gateهای آلفا/بتا](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features)
یا [جدول feature gateهای ارتقایافته/منسوخ‌شده](/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-graduated-or-deprecated-features) مراجعه کنید.

### feature gateهای حذف‌شده {#feature-gates-that-are-removed}

در جدول زیر:

- ستون «From» شامل نسخهٔ کوبرنتیزی است که در آن یک قابلیت معرفی شده
  یا مرحلهٔ انتشار آن تغییر کرده است.
- ستون «To»، در صورتی که خالی نباشد، شامل آخرین نسخهٔ کوبرنتیزی است که در آن
  همچنان می‌توانید از یک feature gate استفاده کنید. اگر مرحلهٔ قابلیت «Deprecated»
  یا «GA» باشد، ستون «To» نسخهٔ کوبرنتیزی را نشان می‌دهد که در آن قابلیت حذف می‌شود.

<!-- Want to edit this table? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
{{< feature-gate-table show-removed="true" caption="Feature Gates Removed" sortable="true" >}}

## توضیحات feature gateهای حذف‌شده

<!-- Want to edit this list? See https://k8s.io/docs/contribute/new-content/new-features/#ready-for-review-feature-gates -->
{{< feature-gate-list show-removed="true" >}}
