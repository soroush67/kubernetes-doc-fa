---
title: کانتینر کمکی (Sidecar Container)
id: sidecar-container
full_link: /docs/concepts/workloads/pods/sidecar-containers/
short_description: >
  یک کانتینر کمکی که در تمام چرخه حیات یک Pod در حال اجرا باقی می‌ماند.
tags:
- fundamental
---
 یک یا چند {{< glossary_tooltip text="کانتینر" term_id="container" >}} که معمولاً پیش از اجرای هر یک از کانتینرهای برنامه راه‌اندازی می‌شوند.

<!--more--> 

کانتینرهای sidecar مانند کانتینرهای معمولی برنامه هستند، اما هدف متفاوتی دارند: کانتینر sidecar یک سرویس محلی در سطح Pod را برای کانتینر اصلی برنامه فراهم می‌کند.
برخلاف {{< glossary_tooltip text="کانتینرهای init" term_id="init-container" >}}، کانتینرهای sidecar
پس از راه‌اندازی Pod نیز به اجرا ادامه می‌دهند.

برای اطلاعات بیشتر، [کانتینرهای Sidecar](/docs/concepts/workloads/pods/sidecar-containers/) را مطالعه کنید.
