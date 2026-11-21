---
title: نود
id: node
full_link: /docs/concepts/architecture/nodes/
short_description: >
  نود یک ماشین کارگر در کوبرنتیز است.

aka:
tags:
- core-object
- fundamental
---
 نود یک ماشین کارگر در کوبرنتیز است.

<!--more-->

هر نود کارگر بسته به کلاستر ممکن است یک ماشین مجازی (VM) یا یک ماشین فیزیکی باشد. این نود، دیمن‌ها (daemon) یا سرویس‌های محلیِ لازم برای اجرای {{< glossary_tooltip text="پادها" term_id="pod" >}} را در اختیار دارد و control plane آن را مدیریت می‌کند. دیمن‌های روی هر نود عبارت‌اند از {{< glossary_tooltip text="kubelet" term_id="kubelet" >}}، {{< glossary_tooltip text="kube-proxy" term_id="kube-proxy" >}} و یک محیط اجرای کانتینر که {{< glossary_tooltip text="CRI" term_id="cri" >}} را پیاده‌سازی می‌کند، مانند {{< glossary_tooltip term_id="docker" >}}.

در نسخه‌های اولیهٔ کوبرنتیز، نودها «Minion» نامیده می‌شدند.
