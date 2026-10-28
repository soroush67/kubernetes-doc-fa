---
title: Node-pressure eviction
id: node-pressure-eviction
full_link: /docs/concepts/scheduling-eviction/node-pressure-eviction/
short_description: >
  Node-pressure eviction فرایندی است که در آن kubelet برای بازیابی منابع روی نودها، Podها را به‌صورت پیشگیرانه از کار می‌اندازد.
aka:
- kubelet eviction
tags:
- operation
---
Node-pressure eviction فرایندی است که در آن {{<glossary_tooltip term_id="kubelet" text="kubelet">}} برای بازیابی {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} روی نودها، Podها را به‌صورت پیشگیرانه خاتمه می‌دهد.

<!--more-->

kubelet منابعی مانند CPU، حافظه، فضای دیسک و inodeهای سیستم فایل را روی نودهای کلاستر شما پایش می‌کند. هنگامی که یک یا چند مورد از این منابع به سطوح مصرف مشخصی برسند، kubelet می‌تواند برای بازیابی منابع و جلوگیری از کمبود آن‌ها، یک یا چند Pod را روی نود به‌صورت پیشگیرانه از کار بیندازد.

Node-pressure eviction با [تخلیه آغازشده از طریق API (API-initiated eviction)](/docs/concepts/scheduling-eviction/api-eviction/) یکسان نیست.
