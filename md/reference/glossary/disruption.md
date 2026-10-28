---
title: اختلال
id: disruption
full_link: /docs/concepts/workloads/pods/disruptions/
short_description: >
  رویدادی که باعث از دسترس خارج شدن یک یا چند Pod می‌شود
aka:
tags:
- fundamental
---
 اختلال‌ها (Disruptions) رویدادهایی هستند که باعث می‌شوند یک یا چند
{{< glossary_tooltip term_id="pod" text="Pod" >}} از سرویس‌دهی خارج شوند.
یک اختلال بر {{< glossary_tooltip text="منابع" term_id="api-resource" >}} مدیریت بار کاری،
مانند {{< glossary_tooltip term_id="deployment" >}}، که به Podهای آسیب‌دیده وابسته‌اند،
پیامد دارد.

<!--more-->

اگر شما، به عنوان مدیر کلاستر، یک Pod متعلق به یک اپلیکیشن را از بین ببرید،
کوبرنتیز این حالت را _اختلال داوطلبانه_ (voluntary disruption) می‌نامد. اگر یک Pod
به دلیل خرابی نود یا قطعی‌ای که یک ناحیه خرابی گسترده‌تر را تحت تأثیر قرار می‌دهد، آفلاین شود،
کوبرنتیز این حالت را _اختلال غیرداوطلبانه_ (involuntary disruption) می‌نامد.

برای اطلاعات بیشتر، [اختلال‌ها](/docs/concepts/workloads/pods/disruptions/) را ببینید.
