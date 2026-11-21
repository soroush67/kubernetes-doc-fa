---
title: FlexVolume
id: flexvolume
full_link: /docs/concepts/storage/volumes/#flexvolume
short_description: >
    رابط FlexVolume یک رابط منسوخ برای ایجاد افزونه‌های حجم (volume) خارج از درخت کد اصلی (out-of-tree) است. {{< glossary_tooltip text="رابط ذخیره‌سازی کانتینر" term_id="csi" >}} رابطی جدیدتر است که چندین مشکل FlexVolume را برطرف می‌کند.


aka: 
tags:
- storage 
---
 رابط FlexVolume یک رابط منسوخ برای ایجاد افزونه‌های حجم (volume) خارج از درخت کد اصلی (out-of-tree) است. {{< glossary_tooltip text="رابط ذخیره‌سازی کانتینر" term_id="csi" >}} رابطی جدیدتر است که چندین مشکل FlexVolume را برطرف می‌کند.

<!--more--> 

با FlexVolume کاربران می‌توانند درایورهای خود را بنویسند و پشتیبانی از حجم‌های خود را به کوبرنتیز اضافه کنند. فایل‌های اجرایی و وابستگی‌های درایورهای FlexVolume باید روی ماشین‌های میزبان نصب شوند و این کار به دسترسی root نیاز دارد. گروه SIG Storage توصیه می‌کند در صورت امکان یک درایور {{< glossary_tooltip text="CSI" term_id="csi" >}} پیاده‌سازی کنید، زیرا این رابط محدودیت‌های FlexVolume را برطرف می‌کند.

* [رابط FlexVolume در مستندات کوبرنتیز](/docs/concepts/storage/volumes/#flexvolume)
* [اطلاعات بیشتر درباره FlexVolume](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-storage/flexvolume.md)
* [پرسش‌های متداول درباره افزونه‌های حجم برای فروشندگان ذخیره‌سازی](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md)
