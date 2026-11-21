---
title: تخلیه ناشی از فشار نود
id: node-pressure-eviction
full_link: /docs/concepts/scheduling-eviction/node-pressure-eviction/
short_description: >
  تخلیه ناشی از فشار نود فرایندی است که در آن kubelet به‌طور پیش‌دستانه پادها را با شکست متوقف می‌کند تا منابع نودها را بازپس بگیرد.
aka:
- kubelet eviction
tags:
- operation
---
تخلیه ناشی از فشار نود (Node-pressure eviction) فرایندی است که در آن {{<glossary_tooltip term_id="kubelet" text="kubelet">}} به‌طور پیش‌دستانه پادها را خاتمه می‌دهد تا {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} نودها را بازپس بگیرد.

<!--more-->

مؤلفه kubelet منابعی مانند CPU، حافظه، فضای دیسک و inodeهای فایل‌سیستم را روی نودهای کلاستر شما پایش می‌کند. هنگامی که مصرف یک یا چند مورد از این منابع به سطح مشخصی برسد، kubelet می‌تواند به‌طور پیش‌دستانه یک یا چند پاد را روی آن نود با شکست متوقف کند تا منابع را بازپس بگیرد و از کمبود منابع (starvation) جلوگیری کند.

تخلیه ناشی از فشار نود با [تخلیه آغازشده از طریق API](/docs/concepts/scheduling-eviction/api-eviction/) یکسان نیست.
