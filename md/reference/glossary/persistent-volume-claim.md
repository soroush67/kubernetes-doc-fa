---
title: Persistent Volume Claim
id: persistent-volume-claim
full_link: /docs/concepts/storage/persistent-volumes/#persistentvolumeclaims
short_description: >
  منابع ذخیره‌سازی تعریف‌شده در یک PersistentVolume را درخواست می‌کند تا بتوان آن را به‌صورت یک حجم در کانتینر سوار (mount) کرد.

aka: 
tags:
- core-object
- storage
---
این آبجکت {{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} ذخیره‌سازی تعریف‌شده در یک
{{< glossary_tooltip text="PersistentVolume" term_id="persistent-volume" >}} را درخواست می‌کند تا بتوان این ذخیره‌سازی را به‌صورت
یک حجم (volume) در یک {{< glossary_tooltip text="کانتینر" term_id="container" >}} سوار (mount) کرد.

<!--more--> 

این آبجکت میزان ذخیره‌سازی، نحوهٔ دسترسی به آن (فقط‌خواندنی، خواندنی‌ونوشتنی و/یا انحصاری) و نحوهٔ بازپس‌گیری آن (نگهداری، بازیافت یا حذف) را مشخص می‌کند. جزئیات خودِ ذخیره‌سازی در آبجکت PersistentVolume شرح داده می‌شود.
