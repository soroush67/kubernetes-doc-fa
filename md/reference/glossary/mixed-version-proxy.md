---
title: پراکسی نسخه‌های ترکیبی (MVP)
id: mvp
full_link: /docs/concepts/architecture/mixed-version-proxy/
short_description: >
  قابلیتی که به kube-apiserver اجازه می‌دهد درخواست مربوط به یک منبع را به یک API server همتای دیگر پراکسی کند.
aka: ["MVP"]
tags:
- architecture
---
قابلیتی که به یک kube-apiserver امکان می‌دهد درخواست مربوط به یک منبع را به یک API server همتای دیگر پراکسی کند.

<!--more-->

هنگامی که یک کلاستر دارای چندین API server است که نسخه‌های متفاوتی از کوبرنتیز را اجرا می‌کنند، این
قابلیت باعث می‌شود درخواست‌های مربوط به {{< glossary_tooltip text="منبع" term_id="api-resource" >}}
توسط API server صحیح پاسخ داده شوند.

MVP به‌صورت پیش‌فرض غیرفعال است و با فعال‌کردن
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `UnknownVersionInteroperabilityProxy` هنگام راه‌اندازی
{{< glossary_tooltip text="API Server" term_id="kube-apiserver" >}} می‌توان آن را فعال کرد.
