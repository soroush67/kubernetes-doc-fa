---
title: Toleration
id: toleration
full_link: /docs/concepts/scheduling-eviction/taint-and-toleration/
short_description: >
  یک آبجکت اصلی که از سه ویژگی الزامی تشکیل شده است: key، value و effect. Tolerationها امکان زمان‌بندی Podها را روی نودها یا گروه‌های نودی که taint متناظر دارند فراهم می‌کنند.

aka:
tags:
- core-object
- fundamental
---
 یک آبجکت اصلی که از سه ویژگی الزامی تشکیل شده است: key، value و effect. Tolerationها امکان زمان‌بندی Podها را روی نودها یا گروه‌های نودی که {{< glossary_tooltip text="taint" term_id="taint" >}}های متناظر دارند فراهم می‌کنند.

<!--more-->

Tolerationها و {{< glossary_tooltip text="taint" term_id="taint" >}}ها با یکدیگر کار می‌کنند تا اطمینان حاصل شود که Podها روی نودهای نامناسب زمان‌بندی نمی‌شوند. یک یا چند toleration روی یک {{< glossary_tooltip text="Pod" term_id="pod" >}} اعمال می‌شود. هر toleration نشان می‌دهد که {{< glossary_tooltip text="Pod" term_id="pod" >}} مجاز است (اما ملزم نیست) روی نودها یا گروه‌های نودی که {{< glossary_tooltip text="taint" term_id="taint" >}}های متناظر دارند زمان‌بندی شود.
