---
title: حجم (Volume)
id: volume
full_link: /docs/concepts/storage/volumes/
short_description: >
  یک دایرکتوری حاوی داده که برای کانتینرهای درون یک پاد قابل دسترسی است.

aka:
tags:
- fundamental
---
 یک دایرکتوری حاوی داده که برای {{< glossary_tooltip text="کانتینرها" term_id="container" >}}ِ درون یک {{< glossary_tooltip term_id="pod" >}} قابل دسترسی است.

<!--more-->

یک حجم (volume) در کوبرنتیز تا زمانی که Pod دربرگیرنده‌ی آن وجود دارد، باقی می‌ماند. در نتیجه، حجم عمرِ طولانی‌تری نسبت به هر یک از کانتینرهایی دارد که درون Pod اجرا می‌شوند، و داده‌های موجود در حجم در طول راه‌اندازی مجدد کانتینرها حفظ می‌شود.

برای اطلاعات بیشتر به [ذخیره‌سازی](/docs/concepts/storage/) مراجعه کنید.
