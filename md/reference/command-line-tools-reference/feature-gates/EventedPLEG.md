---
title: EventedPLEG
content_type: feature_gate
_build:
  list: never
  render: false

stages:
  - stage: alpha
    defaultValue: false
    fromVersion: "1.26"
---
پشتیبانی از دریافت رویدادهای چرخه حیات کانتینر توسط kubelet را از
{{< glossary_tooltip text="container runtime" term_id="container-runtime" >}}
از طریق یک افزونه برای {{<glossary_tooltip term_id="cri" text="CRI">}} فعال می‌کند.
(PLEG مخفف «Pod lifecycle event generator» است).
برای اینکه این قابلیت مفید باشد، باید پشتیبانی از رویدادهای چرخه حیات کانتینر را
در هر container runtime که در کلاستر شما اجرا می‌شود نیز فعال کنید. اگر container runtime پشتیبانی
از رویدادهای چرخه حیات کانتینر را اعلام نکند، kubelet به‌طور خودکار به سازوکار عمومی قدیمی PLEG
بازمی‌گردد، حتی اگر این feature gate را فعال کرده باشید.
