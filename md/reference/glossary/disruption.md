---
title: اختلال
id: disruption
full_link: /docs/concepts/workloads/pods/disruptions/
short_description: >
  رویدادی که باعث خارج شدن یک یا چند Pod از سرویس می‌شود
aka:
tags:
- fundamental
---
 اختلال‌ها (disruptions) رویدادهایی هستند که باعث می‌شوند یک یا چند
{{< glossary_tooltip term_id="pod" text="Pod" >}} از سرویس خارج شوند.
هر اختلال بر {{< glossary_tooltip text="منابع" term_id="api-resource" >}} مدیریت بار کاری
که به Podهای آسیب‌دیده وابسته‌اند، مانند {{< glossary_tooltip term_id="deployment" >}}، تأثیر می‌گذارد.

<!--more-->

اگر شما در نقش اپراتور کلاستر، Pod متعلق به یک برنامه را از بین ببرید،
کوبرنتیز آن را _اختلال داوطلبانه_ می‌نامد. اگر یک Pod به دلیل خرابی نود
یا قطعی‌ای که یک ناحیهٔ خرابی (failure zone) گسترده‌تر را تحت تأثیر قرار می‌دهد از دسترس خارج شود،
کوبرنتیز آن را _اختلال غیرداوطلبانه_ می‌نامد.

برای اطلاعات بیشتر، صفحهٔ [اختلال‌ها](/docs/concepts/workloads/pods/disruptions/) را ببینید.
