---
title: شرط (Condition)
id: condition
full_link: /docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions
short_description: >
  یک condition وضعیت فعلی یک منبع کوبرنتیز را نشان می‌دهد و اطلاعاتی درباره درست بودن جنبه‌های مشخصی از آن منبع فراهم می‌کند.

aka:
tags:
- fundamental
---
Condition فیلدی در بخش status یک منبع کوبرنتیز است که وضعیت فعلی آن منبع را توصیف می‌کند.

<!--more-->

Conditionها روشی استاندارد برای اطلاع‌رسانی وضعیت منابع از سوی اجزای کوبرنتیز فراهم می‌کنند. هر condition دارای یک `type`، یک `status` (مقدار True، False یا Unknown) و فیلدهای اختیاری مانند `reason` و `message` است که جزئیات بیشتری ارائه می‌دهند. برای مثال، یک Pod ممکن است conditionهایی مانند `Ready`، `ContainersReady` یا `PodScheduled` داشته باشد.
