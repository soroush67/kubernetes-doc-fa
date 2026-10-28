---
title: Node
id: node
full_link: /docs/concepts/architecture/nodes/
short_description: >
  نود یک ماشین کارگر (worker) در کوبرنتیز است.

aka:
tags:
- core-object
- fundamental
---
 نود یک ماشین کارگر (worker) در کوبرنتیز است.

<!--more-->

یک نود کارگر، بسته به کلاستر، می‌تواند یک ماشین مجازی یا یک ماشین فیزیکی باشد. این نود دارای سرویس‌ها یا دیمن‌های محلی لازم برای اجرای {{< glossary_tooltip text="Podها" term_id="pod" >}} است و توسط control plane مدیریت می‌شود. دیمن‌های موجود بر روی یک نود شامل {{< glossary_tooltip text="kubelet" term_id="kubelet" >}}، {{< glossary_tooltip text="kube-proxy" term_id="kube-proxy" >}} و یک container runtime است که {{< glossary_tooltip text="CRI" term_id="cri" >}} را پیاده‌سازی می‌کند، مانند {{< glossary_tooltip term_id="docker" >}}.

در نسخه‌های اولیه کوبرنتیز، نودها «Minion» نامیده می‌شدند.
