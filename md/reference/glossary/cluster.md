---
title: کلاستر
id: cluster
full_link: 
short_description: >
   مجموعه‌ای از ماشین‌های کارگر، به نام نود، که برنامه‌های کانتینری‌شده را اجرا می‌کنند. هر کلاستر دست‌کم یک نود کارگر دارد.

aka: 
tags:
- fundamental
- operation
---
مجموعه‌ای از ماشین‌های کارگر، به نام {{< glossary_tooltip text="نودها" term_id="node" >}}،
که برنامه‌های کانتینری‌شده را اجرا می‌کنند. هر کلاستر دست‌کم یک نود کارگر دارد.

<!--more-->
نود(های) کارگر، {{< glossary_tooltip text="Podهایی" term_id="pod" >}} را که
اجزای بار کاری برنامه هستند میزبانی می‌کنند.
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} نودهای کارگر و
Podهای موجود در کلاستر را مدیریت می‌کند. در محیط‌های عملیاتی (production)، control plane معمولاً
بر روی چندین رایانه اجرا می‌شود و یک کلاستر معمولاً چندین نود را اجرا می‌کند و
از این طریق تحمل‌پذیری خطا (fault-tolerance) و دسترس‌پذیری بالا (high availability) را فراهم می‌آورد.
