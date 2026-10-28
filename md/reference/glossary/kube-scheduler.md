---
title: kube-scheduler
id: kube-scheduler
full_link: /docs/reference/command-line-tools-reference/kube-scheduler/
short_description: >
  کامپوننت control plane که Podهای تازه ایجادشده‌ای را که هنوز به هیچ نودی اختصاص داده نشده‌اند پایش می‌کند و یک نود را برای اجرای آن‌ها انتخاب می‌کند.

aka: 
tags:
- architecture
---
کامپوننت control plane که {{< glossary_tooltip term_id="pod" text="Podهای" >}} تازه ایجادشده‌ای را که هنوز به هیچ
{{< glossary_tooltip term_id="node" text="نودی">}} اختصاص داده نشده‌اند پایش می‌کند و یک نود را برای اجرای آن‌ها
انتخاب می‌کند.

<!--more-->

عواملی که در تصمیم‌گیری‌های زمان‌بندی در نظر گرفته می‌شوند عبارت‌اند از:
نیازمندی‌های {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} به‌صورت فردی و جمعی،
محدودیت‌های سخت‌افزاری/نرم‌افزاری/سیاستی، مشخصات affinity و anti-affinity،
محلیت داده‌ها (data locality)، تداخل میان بارهای کاری و مهلت‌های زمانی (deadlines).
