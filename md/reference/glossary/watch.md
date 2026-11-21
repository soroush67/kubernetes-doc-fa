---
title: Watch
id: watch
full_link: /docs/reference/using-api/api-concepts/#api-verbs
short_description: >
  فعلی که برای پیگیری تغییرات یک آبجکت در کوبرنتیز به‌صورت یک جریان (stream) به کار می‌رود.

aka:
tags:
- API verb
- fundamental
---
فعلی که برای پیگیری تغییرات یک آبجکت در کوبرنتیز به‌صورت یک جریان (stream) به کار می‌رود.
از این فعل برای تشخیص کارآمد تغییرات استفاده می‌شود.

<!--more-->

فعلی که برای پیگیری تغییرات یک آبجکت در کوبرنتیز به‌صورت یک جریان به کار می‌رود. با watch
می‌توان تغییرات را به‌شکلی کارآمد تشخیص داد؛ برای مثال، یک
{{< glossary_tooltip term_id="controller" text="کنترل‌کننده">}} که باید هر بار از تغییر یک
ConfigMap باخبر شود، می‌تواند به‌جای سرکشی دوره‌ای (polling) از watch استفاده کند.

برای اطلاعات بیشتر، [تشخیص کارآمد تغییرات در مفاهیم API](/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) را ببینید.
