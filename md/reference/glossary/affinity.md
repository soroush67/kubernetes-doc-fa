---
title: وابستگی (Affinity)
id: affinity
full_link: /docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity
short_description: >
     قواعدی که زمان‌بند برای تعیین محل قرارگیری پادها به کار می‌برد
aka:
tags:
- fundamental
---

در کوبرنتیز، _وابستگی_ (affinity) مجموعه‌ای از قواعد است که به زمان‌بند راهنمایی‌هایی درباره محل قرارگیری پادها می‌دهد.

<!--more-->
دو نوع وابستگی وجود دارد:
* [وابستگی نود](/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity)
* [وابستگی پاد به پاد](/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)

این قواعد با استفاده از {{< glossary_tooltip term_id="label" text="برچسب‌های">}} کوبرنتیز
و {{< glossary_tooltip term_id="selector" text="انتخابگرهایی">}} تعریف می‌شوند که در {{< glossary_tooltip term_id="pod" text="پادها" >}} مشخص شده‌اند.
این قواعد بسته به اینکه بخواهید زمان‌بند با چه میزان سخت‌گیری آن‌ها را اعمال کند، می‌توانند الزامی یا ترجیحی باشند.
