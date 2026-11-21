---
title: kube-scheduler
id: kube-scheduler
full_link: /docs/reference/command-line-tools-reference/kube-scheduler/
short_description: >
  مؤلفه‌ای از control plane که پادهای تازه ایجادشده‌ای را که هنوز به هیچ نودی تخصیص نیافته‌اند زیر نظر می‌گیرد و نودی را برای اجرای آن‌ها انتخاب می‌کند.

aka: 
tags:
- architecture
---
مؤلفه‌ای از control plane که
{{< glossary_tooltip term_id="pod" text="پادهای" >}} تازه ایجادشده‌ای را که هنوز به هیچ
{{< glossary_tooltip term_id="node" text="نودی">}} تخصیص نیافته‌اند زیر نظر می‌گیرد و نودی را برای
اجرای آن‌ها انتخاب می‌کند.

<!--more-->

عواملی که در تصمیم‌گیری‌های زمان‌بندی در نظر گرفته می‌شوند عبارت‌اند از:
نیازمندی‌های فردی و جمعی به {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}}،
محدودیت‌های سخت‌افزاری، نرم‌افزاری و سیاستی، مشخصات وابستگی (affinity) و ضدوابستگی (anti-affinity)،
محلی بودن داده‌ها، تداخل میان بارهای کاری و مهلت‌های زمانی.
