---
title: سیاست‌های زمان‌بندی
content_type: concept
sitemap:
  priority: 0.2 # Scheduling priorities are deprecated
weight: 30
---

<!-- overview -->

در نسخه‌های پیش از v1.23 کوبرنتیز، می‌شد با یک سیاست زمان‌بندی، فرایند *predicates* (پیش‌شرط‌ها) و *priorities* (اولویت‌ها) را مشخص کرد. برای نمونه، می‌توانستید با اجرای دستور `kube-scheduler --policy-config-file <filename>` یا `kube-scheduler --policy-configmap <ConfigMap>` یک سیاست زمان‌بندی تنظیم کنید.

این سیاست زمان‌بندی از نسخهٔ v1.23 کوبرنتیز به بعد پشتیبانی نمی‌شود. فلگ‌های مرتبط با آن، یعنی `policy-config-file`، `policy-configmap`، `policy-configmap-namespace` و `use-legacy-policy-config` نیز دیگر پشتیبانی نمی‌شوند. برای دستیابی به رفتاری مشابه، از [پیکربندی زمان‌بند](/docs/reference/scheduling/config/) استفاده کنید.

## {{% heading "whatsnext" %}}

* دربارهٔ [زمان‌بندی](/docs/concepts/scheduling-eviction/kube-scheduler/) بیاموزید.
* دربارهٔ [پیکربندی kube-scheduler](/docs/reference/scheduling/config/) بیاموزید.
* [مرجع پیکربندی kube-scheduler (v1)](/docs/reference/config-api/kube-scheduler-config.v1/) را مطالعه کنید.
