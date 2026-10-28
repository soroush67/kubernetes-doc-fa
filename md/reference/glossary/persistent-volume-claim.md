---
title: Persistent Volume Claim
id: persistent-volume-claim
full_link: /docs/concepts/storage/persistent-volumes/#persistentvolumeclaims
short_description: >
  منابع ذخیره‌سازی تعریف‌شده در یک PersistentVolume را درخواست می‌کند تا بتوان آن را به‌عنوان حجم (volume) در یک کانتینر مانت کرد.

aka: 
tags:
- core-object
- storage
---
منابع ذخیره‌سازی ({{< glossary_tooltip text="resources" term_id="infrastructure-resource" >}}) تعریف‌شده در یک
{{< glossary_tooltip text="PersistentVolume" term_id="persistent-volume" >}} را درخواست می‌کند تا بتوان این ذخیره‌سازی را به‌عنوان
حجم (volume) در یک {{< glossary_tooltip text="کانتینر" term_id="container" >}} مانت کرد.

<!--more--> 

میزان ذخیره‌سازی، نحوه دسترسی به آن (فقط‌خواندنی، خواندنی-نوشتنی و/یا انحصاری) و نحوه بازیابی آن (نگه‌داری، بازچرخانی یا حذف) را مشخص می‌کند. جزئیات خود ذخیره‌سازی در آبجکت PersistentVolume توصیف می‌شود.
