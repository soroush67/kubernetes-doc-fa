---
title: Drain
id: drain
full_link:
short_description: >
  تخلیه‌ی ایمن Podها از یک نود برای آماده‌سازی جهت نگهداری یا حذف آن.
tags:
- fundamental
- operation
---
فرایند تخلیه‌ی ایمن {{< glossary_tooltip text="Podها" term_id="pod" >}} از یک {{< glossary_tooltip text="نود" term_id="node" >}} برای آماده‌سازی آن جهت نگهداری یا حذف از یک {{< glossary_tooltip text="کلاستر" term_id="cluster" >}}.

<!--more-->

دستور `kubectl drain` برای علامت‌گذاری یک {{< glossary_tooltip text="نود" term_id="node" >}} به‌عنوان نودی که از سرویس خارج می‌شود، استفاده می‌گردد.
هنگام اجرا، این دستور همه‌ی {{< glossary_tooltip text="Podها" term_id="pod" >}} را از {{< glossary_tooltip text="نود" term_id="node" >}} تخلیه (evict) می‌کند.
اگر یک درخواست تخلیه به‌طور موقت رد شود، `kubectl drain` تا زمانی که همه‌ی {{< glossary_tooltip text="Podها" term_id="pod" >}} خاتمه یابند یا مهلت زمانی قابل‌پیکربندی به پایان برسد، دوباره تلاش می‌کند.
