---
title: Taint
id: taint
full_link: /docs/concepts/scheduling-eviction/taint-and-toleration/
short_description: >
  یک آبجکت اصلی که از سه ویژگی الزامی تشکیل شده است: key، value و effect. Taintها از زمان‌بندی Podها روی نودها یا گروه‌های نود جلوگیری می‌کنند.

aka:
tags:
- fundamental
---
 یک آبجکت اصلی که از سه ویژگی الزامی تشکیل شده است: key، value و effect. Taintها از زمان‌بندی {{< glossary_tooltip text="Podها" term_id="pod" >}} روی {{< glossary_tooltip text="نودها" term_id="node" >}} یا گروه‌های نود جلوگیری می‌کنند.

<!--more-->

Taintها و {{< glossary_tooltip text="tolerationها" term_id="toleration" >}} با یکدیگر کار می‌کنند تا اطمینان حاصل شود که Podها روی نودهای نامناسب زمان‌بندی نمی‌شوند. یک یا چند taint روی یک نود اعمال می‌شود. یک نود باید تنها Podی را بپذیرد که tolerationهای متناسب با taintهای پیکربندی‌شده را داشته باشد.
