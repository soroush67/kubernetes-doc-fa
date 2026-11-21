---
title: شرط
id: condition
full_link: /docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions
short_description: >
  هر شرط وضعیت فعلی یک منبع کوبرنتیز را نشان می‌دهد و مشخص می‌کند که آیا جنبه‌های معینی از آن منبع برقرار هستند یا نه.

aka:
tags:
- fundamental
---
شرط (condition) فیلدی در بخش وضعیت (status) یک منبع کوبرنتیز است که وضعیت فعلی آن منبع را توصیف می‌کند.

<!--more-->

شرط‌ها روشی استاندارد در اختیار مؤلفه‌های کوبرنتیز می‌گذارند تا وضعیت منابع را به یکدیگر اطلاع دهند. هر شرط یک `type`، یک `status` (با یکی از مقادیر True، False یا Unknown) و فیلدهای اختیاری مانند `reason` و `message` دارد که جزئیات بیشتری ارائه می‌کنند. برای مثال، یک Pod ممکن است شرط‌هایی مانند `Ready`، `ContainersReady` یا `PodScheduled` داشته باشد.
