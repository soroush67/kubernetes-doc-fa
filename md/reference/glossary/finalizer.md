---
title: Finalizer
id: finalizer
full_link: /docs/concepts/overview/working-with-objects/finalizers/
short_description: >
  کلیدی دارای فضای نام که به کوبرنتیز می‌گوید پیش از حذف کامل یک آبجکت علامت‌گذاری‌شده برای حذف، تا برآورده شدن شرایط مشخص صبر کند.
aka: 
tags:
- fundamental
- operation
---
Finalizerها کلیدهای دارای فضای نام هستند که به کوبرنتیز می‌گویند پیش از حذف کامل {{< glossary_tooltip text="منابعی" term_id="api-resource" >}} که برای حذف علامت‌گذاری شده‌اند، تا برآورده شدن شرایط مشخص صبر کند.
Finalizerها به {{<glossary_tooltip text="کنترل‌کننده‌ها" term_id="controller">}} هشدار می‌دهند که منابعی را که آبجکت حذف‌شده مالک آن‌ها بوده است پاک‌سازی کنند.

<!--more-->

هنگامی که به کوبرنتیز دستور می‌دهید آبجکتی را که برای آن finalizerهایی تعیین شده است حذف کند، API کوبرنتیز با مقداردهی `.metadata.deletionTimestamp` آبجکت را برای حذف علامت‌گذاری می‌کند و کد وضعیت `202` (در HTTP به معنای «Accepted») را برمی‌گرداند. آبجکت هدف تا زمانی که control plane یا سایر مؤلفه‌ها اقدامات تعریف‌شده توسط finalizerها را انجام می‌دهند، در وضعیت پایان‌یافتن (terminating) باقی می‌ماند.
پس از تکمیل این اقدامات، کنترل‌کننده finalizerهای مربوطه را از آبجکت هدف حذف می‌کند. زمانی که فیلد `metadata.finalizers` خالی شود، کوبرنتیز حذف را کامل‌شده در نظر می‌گیرد و آبجکت را حذف می‌کند.

می‌توانید از finalizerها برای کنترل {{<glossary_tooltip text="garbage collection" term_id="garbage-collection">}} منابع استفاده کنید. برای مثال، می‌توانید یک finalizer تعریف کنید تا پیش از آنکه کنترل‌کننده آبجکتِ در حال نهایی‌سازی را حذف کند، {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} یا زیرساخت مرتبط را پاک‌سازی کند.
