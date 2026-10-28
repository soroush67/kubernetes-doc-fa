---
title: Watch
id: watch
full_link: /docs/reference/using-api/api-concepts/#api-verbs
short_description: >
  فعلی (verb) که برای ردیابی تغییرات یک آبجکت در کوبرنتیز به‌صورت یک جریان (stream) استفاده می‌شود.

aka:
tags:
- API verb
- fundamental
---
فعلی (verb) که برای ردیابی تغییرات یک آبجکت در کوبرنتیز به‌صورت یک جریان (stream) استفاده می‌شود.
از آن برای تشخیص کارآمد تغییرات استفاده می‌شود.

<!--more-->

فعلی (verb) که برای ردیابی تغییرات یک آبجکت در کوبرنتیز به‌صورت یک جریان (stream) استفاده می‌شود. Watchها امکان
تشخیص کارآمد تغییرات را فراهم می‌کنند؛ برای مثال، یک
{{< glossary_tooltip term_id="controller" text="کنترل‌کننده">}} که لازم است هر زمان
ConfigMap تغییر کرد مطلع شود، می‌تواند به‌جای polling از watch استفاده کند.

برای اطلاعات بیشتر، [تشخیص کارآمد تغییرات در مفاهیم API](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) را ببینید.
