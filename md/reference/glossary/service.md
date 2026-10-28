---
title: Service
id: service
full_link: /docs/concepts/services-networking/service/
short_description: >
  روشی برای در دسترس قرار دادن یک برنامه که روی مجموعه‌ای از Podها اجرا می‌شود، به‌صورت یک سرویس شبکه‌ای.
tags:
- fundamental
- core-object
---
روشی برای در دسترس قرار دادن یک برنامه شبکه‌ای که به‌صورت یک یا چند
{{< glossary_tooltip text="Pod" term_id="pod" >}} در کلاستر شما اجرا می‌شود.

<!--more-->

مجموعه Podهایی که یک Service هدف قرار می‌دهد، (معمولاً) توسط یک
{{< glossary_tooltip text="انتخابگر (selector)" term_id="selector" >}} تعیین می‌شود. اگر Podهای بیشتری اضافه یا حذف شوند،
مجموعه Podهای منطبق با انتخابگر تغییر خواهد کرد. Service تضمین می‌کند که ترافیک شبکه
بتواند به مجموعه فعلی Podهای بار کاری هدایت شود.

Serviceهای کوبرنتیز یا از شبکه‌بندی IP (IPv4، IPv6 یا هر دو) استفاده می‌کنند، یا به یک نام خارجی در
سامانه نام دامنه (DNS) ارجاع می‌دهند.

انتزاع Service سازوکارهای دیگری مانند Ingress و Gateway را ممکن می‌سازد.
