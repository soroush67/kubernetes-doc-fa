---
title: Pod
id: pod
full_link: /docs/concepts/workloads/pods/
short_description: >
  یک Pod مجموعه‌ای از کانتینرهای در حال اجرا در کلاستر شما را نشان می‌دهد.

aka: 
tags:
- core-object
- fundamental
---
 کوچک‌ترین و ساده‌ترین آبجکت کوبرنتیز. یک Pod مجموعه‌ای از {{< glossary_tooltip text="کانتینرهای" term_id="container" >}} در حال اجرا در کلاستر شما را نشان می‌دهد.

<!--more--> 

یک Pod معمولاً برای اجرای یک کانتینر اصلی پیکربندی می‌شود. این Pod همچنین می‌تواند کانتینرهای sidecar اختیاری را اجرا کند که قابلیت‌های تکمیلی مانند ثبت لاگ را فراهم می‌کنند. Podها معمولاً توسط یک {{< glossary_tooltip term_id="deployment" >}} مدیریت می‌شوند.
