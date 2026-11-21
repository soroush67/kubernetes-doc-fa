---
title: پراکسی نسخه‌های مختلط (MVP)
id: mvp
full_link: /docs/concepts/architecture/mixed-version-proxy/
short_description: >
  قابلیتی که به kube-apiserver امکان می‌دهد درخواست یک منبع را به سرور API همتای دیگری پراکسی کند.
aka: ["MVP"]
tags:
- architecture
---
قابلیتی که به kube-apiserver امکان می‌دهد درخواست یک منبع را به سرور API همتای دیگری پراکسی کند.

<!--more-->

هنگامی که یک کلاستر چندین سرور API دارد که نسخه‌های متفاوتی از کوبرنتیز را اجرا می‌کنند، این
قابلیت باعث می‌شود درخواست‌های مربوط به {{< glossary_tooltip text="منبع" term_id="api-resource" >}}
توسط سرور API درست پاسخ داده شوند.

قابلیت MVP به‌طور پیش‌فرض غیرفعال است. برای فعال‌سازی آن، باید هنگام راه‌اندازی
{{< glossary_tooltip text="سرور API" term_id="kube-apiserver" >}}، [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `UnknownVersionInteroperabilityProxy` را فعال کنید.
