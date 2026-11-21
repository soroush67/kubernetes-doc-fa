---
title: کانتینر جانبی (Sidecar)
id: sidecar-container
full_link: /docs/concepts/workloads/pods/sidecar-containers/
short_description: >
  کانتینری کمکی که در سراسر چرخهٔ حیات یک Pod در حال اجرا باقی می‌ماند.
tags:
- fundamental
---
 یک یا چند {{< glossary_tooltip text="کانتینر" term_id="container" >}} که معمولاً پیش از اجرای هر کانتینر برنامه‌ای راه‌اندازی می‌شوند.

<!--more--> 

کانتینرهای جانبی (sidecar containers) مانند کانتینرهای عادی برنامه هستند، اما هدف متفاوتی دارند: کانتینر جانبی سرویسی محلی در سطح Pod را در اختیار کانتینر اصلی برنامه قرار می‌دهد.
برخلاف {{< glossary_tooltip text="کانتینرهای init" term_id="init-container" >}}، کانتینرهای جانبی پس از راه‌اندازی Pod همچنان به اجرا ادامه می‌دهند.

برای اطلاعات بیشتر، صفحهٔ [کانتینرهای جانبی](/docs/concepts/workloads/pods/sidecar-containers/) را بخوانید.
