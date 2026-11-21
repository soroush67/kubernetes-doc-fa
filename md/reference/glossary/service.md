---
title: Service
id: service
full_link: /docs/concepts/services-networking/service/
short_description: >
  روشی برای در دسترس قرار دادن برنامه‌ای که روی مجموعه‌ای از Podها اجرا می‌شود، به‌عنوان یک سرویس شبکه.
tags:
- fundamental
- core-object
---
روشی برای در دسترس قرار دادن یک برنامهٔ شبکه که به‌صورت یک یا چند
{{< glossary_tooltip text="Pod" term_id="pod" >}} در کلاستر شما اجرا می‌شود.

<!--more-->

مجموعهٔ Podهایی که یک Service هدف قرار می‌دهد (معمولاً) با یک
{{< glossary_tooltip text="انتخابگر (selector)" term_id="selector" >}} تعیین می‌شود. اگر Podهایی اضافه یا حذف شوند،
مجموعهٔ Podهای منطبق با انتخابگر نیز تغییر می‌کند. Service تضمین می‌کند که ترافیک شبکه
بتواند به مجموعهٔ فعلی Podهای آن بار کاری هدایت شود.

هر Service در کوبرنتیز یا از شبکه‌سازی IP (IPv4، IPv6 یا هر دو) استفاده می‌کند یا به یک نام خارجی در
سامانهٔ نام دامنه (DNS) ارجاع می‌دهد.

انتزاع Service زمینه را برای سازوکارهای دیگری مانند Ingress و Gateway فراهم می‌کند.
