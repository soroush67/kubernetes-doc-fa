---
title: حجم (Volume)
id: volume
full_link: /docs/concepts/storage/volumes/
short_description: >
  دایرکتوری حاوی داده که برای کانتینرهای یک پاد قابل دسترسی است.

aka:
tags:
- fundamental
---
 دایرکتوری حاوی داده که برای {{< glossary_tooltip text="کانتینرهای" term_id="container" >}} یک {{< glossary_tooltip term_id="pod" >}} قابل دسترسی است.

<!--more-->

هر حجم در کوبرنتیز به اندازهٔ عمر Podای که آن را در بر می‌گیرد باقی می‌ماند. در نتیجه، عمر حجم از هر کانتینری که درون آن Pod اجرا می‌شود بیشتر است و داده‌های درون حجم پس از راه‌اندازی مجدد کانتینرها حفظ می‌شوند.

برای اطلاعات بیشتر، [ذخیره‌سازی](/docs/concepts/storage/) را ببینید.
