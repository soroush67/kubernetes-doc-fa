---
title: لکه (Taint)
id: taint
full_link: /docs/concepts/scheduling-eviction/taint-and-toleration/
short_description: >
  یک آبجکت هسته‌ای که از سه ویژگی الزامی تشکیل شده است: کلید، مقدار و اثر. لکه‌ها از زمان‌بندی Podها روی نودها یا گروه‌های نود جلوگیری می‌کنند.

aka:
tags:
- fundamental
---
 یک آبجکت هسته‌ای که از سه ویژگی الزامی تشکیل شده است: کلید، مقدار و اثر. لکه‌ها از زمان‌بندی {{< glossary_tooltip text="Podها" term_id="pod" >}} روی {{< glossary_tooltip text="نودها" term_id="node" >}} یا گروه‌های نود جلوگیری می‌کنند.

<!--more-->

لکه‌ها و {{< glossary_tooltip text="تحمل‌ها (tolerations)" term_id="toleration" >}} با هم کار می‌کنند تا Podها روی نودهای نامناسب زمان‌بندی نشوند. هر نود می‌تواند یک یا چند لکه داشته باشد. روی هر نود فقط باید Podهایی زمان‌بندی شوند که تحمل‌های متناظر با لکه‌های پیکربندی‌شده‌ی آن نود را داشته باشند.
