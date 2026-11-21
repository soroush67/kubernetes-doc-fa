---
title: Pod
id: pod
full_link: /docs/concepts/workloads/pods/
short_description: >
  هر Pod نمایانگر مجموعه‌ای از کانتینرهای در حال اجرا در کلاستر شماست.

aka: 
tags:
- core-object
- fundamental
---
 کوچک‌ترین و ساده‌ترین آبجکت کوبرنتیز است. هر Pod نمایانگر مجموعه‌ای از {{< glossary_tooltip text="کانتینرهای" term_id="container" >}} در حال اجرا روی کلاستر شماست.

<!--more--> 

معمولاً هر Pod برای اجرای یک کانتینر اصلی پیکربندی می‌شود. یک Pod می‌تواند کانتینرهای جانبی (sidecar) اختیاری را نیز اجرا کند که قابلیت‌های تکمیلی مانند ثبت لاگ را فراهم می‌کنند. مدیریت Podها معمولاً بر عهدهٔ یک {{< glossary_tooltip term_id="deployment" >}} است.
