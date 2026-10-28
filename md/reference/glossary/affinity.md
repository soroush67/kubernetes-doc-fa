---
title: Affinity
id: affinity
full_link: /docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity
short_description: >
     قواعدی که زمان‌بند برای تعیین محل قرارگیری Podها از آن‌ها استفاده می‌کند
aka:
tags:
- fundamental
---

در کوبرنتیز، _affinity_ مجموعه‌ای از قواعد است که به زمان‌بند درباره محل قرارگیری Podها راهنمایی می‌دهد.

<!--more-->
دو نوع affinity وجود دارد:
* [node affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity)
* [pod-to-pod affinity](/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)

این قواعد با استفاده از {{< glossary_tooltip term_id="label" text="برچسب‌ها">}} و {{< glossary_tooltip term_id="selector" text="انتخابگرهای (selector)">}} کوبرنتیز که در {{< glossary_tooltip term_id="pod" text="Podها" >}} مشخص می‌شوند تعریف می‌گردند،
و بسته به میزان سخت‌گیری‌ای که می‌خواهید زمان‌بند در اعمال آن‌ها داشته باشد، می‌توانند الزامی (required) یا ترجیحی (preferred) باشند.
