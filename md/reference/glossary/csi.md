---
title: Container Storage Interface (CSI)
id: csi
full_link: /docs/concepts/storage/volumes/#csi
short_description: >
    رابط ذخیره‌سازی کانتینر (CSI) یک رابط استاندارد برای در اختیار قرار دادن سامانه‌های ذخیره‌سازی به کانتینرها تعریف می‌کند.


aka: 
tags:
- storage 
---
 رابط ذخیره‌سازی کانتینر (CSI) یک رابط استاندارد برای در اختیار قرار دادن سامانه‌های ذخیره‌سازی به کانتینرها تعریف می‌کند.

<!--more--> 

CSI به فروشندگان اجازه می‌دهد بدون افزودن افزونه‌های ذخیره‌سازی سفارشی خود به مخزن کوبرنتیز، آن‌ها را برای کوبرنتیز ایجاد کنند (افزونه‌های out-of-tree). برای استفاده از درایور CSI یک ارائه‌دهنده ذخیره‌سازی، ابتدا باید آن را [در کلاستر خود مستقر کنید](https://kubernetes-csi.github.io/docs/deploying.html). سپس می‌توانید یک {{< glossary_tooltip text="Storage Class" term_id="storage-class" >}} ایجاد کنید که از آن درایور CSI استفاده می‌کند.

* [CSI در مستندات کوبرنتیز](/docs/concepts/storage/volumes/#csi)
* [فهرست درایورهای CSI موجود](https://kubernetes-csi.github.io/docs/drivers.html)
