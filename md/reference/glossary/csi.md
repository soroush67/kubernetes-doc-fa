---
title: رابط ذخیره‌سازی کانتینر (CSI)
id: csi
full_link: /docs/concepts/storage/volumes/#csi
short_description: >
    رابط ذخیره‌سازی کانتینر (CSI) یک رابط استاندارد برای در دسترس قرار دادن سیستم‌های ذخیره‌سازی برای کانتینرها تعریف می‌کند.


aka: 
tags:
- storage 
---
 رابط ذخیره‌سازی کانتینر (Container Storage Interface یا CSI) یک رابط استاندارد برای در دسترس قرار دادن سیستم‌های ذخیره‌سازی برای کانتینرها تعریف می‌کند.

<!--more--> 

با استفاده از رابط CSI، فروشندگان می‌توانند افزونه‌های ذخیره‌سازی سفارشی برای کوبرنتیز بسازند، بی‌آنکه لازم باشد آن‌ها را به مخزن کوبرنتیز اضافه کنند (افزونه‌های خارج از درخت یا out-of-tree). برای استفاده از درایور CSI یک ارائه‌دهندهٔ ذخیره‌سازی، ابتدا باید [آن را در کلاستر خود مستقر کنید](https://kubernetes-csi.github.io/docs/deploying.html). پس از آن می‌توانید یک {{< glossary_tooltip text="کلاس ذخیره‌سازی" term_id="storage-class" >}} بسازید که از آن درایور CSI استفاده کند.

* [رابط CSI در مستندات کوبرنتیز](/docs/concepts/storage/volumes/#csi)
* [فهرست درایورهای CSI موجود](https://kubernetes-csi.github.io/docs/drivers.html)
