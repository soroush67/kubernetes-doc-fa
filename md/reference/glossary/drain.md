---
title: تخلیه (Drain)
id: drain
full_link:
short_description: >
  Podها را به‌طور ایمن از یک نود بیرون می‌کند تا نود برای نگهداری یا حذف آماده شود.
tags:
- fundamental
- operation
---
فرایند بیرون‌کردن ایمن {{< glossary_tooltip text="Podها" term_id="pod" >}} از یک {{< glossary_tooltip text="نود" term_id="node" >}} برای آماده‌سازی آن جهت نگهداری یا حذف از {{< glossary_tooltip text="کلاستر" term_id="cluster" >}}.

<!--more-->

از فرمان `kubectl drain` برای علامت‌گذاری یک {{< glossary_tooltip text="نود" term_id="node" >}} به‌عنوان نودی که از سرویس خارج می‌شود استفاده می‌شود.
این فرمان پس از اجرا، همهٔ {{< glossary_tooltip text="Podها" term_id="pod" >}} را از {{< glossary_tooltip text="نود" term_id="node" >}} بیرون می‌کند.
اگر یک درخواست بیرون‌کردن (eviction) موقتاً رد شود، فرمان `kubectl drain` آن‌قدر تلاش را تکرار می‌کند تا همهٔ {{< glossary_tooltip text="Podها" term_id="pod" >}} خاتمه یابند یا مهلت زمانی قابل پیکربندی به پایان برسد.
