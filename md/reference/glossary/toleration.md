---
title: تحمل‌پذیری (Toleration)
id: toleration
full_link: /docs/concepts/scheduling-eviction/taint-and-toleration/
short_description: >
  آبجکتی هسته‌ای که از سه ویژگی الزامی کلید، مقدار و اثر تشکیل می‌شود. تحمل‌پذیری‌ها امکان زمان‌بندی پادها را روی نودها یا گروه‌هایی از نودها که لکه (taint) منطبق دارند فراهم می‌کنند.

aka:
tags:
- core-object
- fundamental
---
 آبجکتی هسته‌ای که از سه ویژگی الزامی کلید (key)، مقدار (value) و اثر (effect) تشکیل می‌شود. تحمل‌پذیری‌ها امکان زمان‌بندی پادها را روی نودها یا گروه‌هایی از نودها که {{< glossary_tooltip text="لکه‌های" term_id="taint" >}} منطبق دارند فراهم می‌کنند.

<!--more-->

تحمل‌پذیری‌ها و {{< glossary_tooltip text="لکه‌ها" term_id="taint" >}} با هم کار می‌کنند تا اطمینان حاصل شود که پادها روی نودهای نامناسب زمان‌بندی نمی‌شوند. یک یا چند تحمل‌پذیری روی یک {{< glossary_tooltip text="پاد" term_id="pod" >}} اعمال می‌شود. هر تحمل‌پذیری نشان می‌دهد که آن {{< glossary_tooltip text="پاد" term_id="pod" >}} مجاز است (اما ملزم نیست) روی نودها یا گروه‌هایی از نودها که {{< glossary_tooltip text="لکه‌های" term_id="taint" >}} منطبق دارند زمان‌بندی شود.
