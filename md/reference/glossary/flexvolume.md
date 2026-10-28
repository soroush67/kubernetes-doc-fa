---
title: FlexVolume
id: flexvolume
full_link: /docs/concepts/storage/volumes/#flexvolume
short_description: >
    FlexVolume یک رابط منسوخ‌شده برای ایجاد افزونه‌های حجم (volume) خارج از درخت کد (out-of-tree) است. {{< glossary_tooltip text="Container Storage Interface" term_id="csi" >}} رابطی جدیدتر است که چندین مشکل FlexVolume را برطرف می‌کند.


aka: 
tags:
- storage 
---
 FlexVolume یک رابط منسوخ‌شده برای ایجاد افزونه‌های حجم (volume) خارج از درخت کد (out-of-tree) است. {{< glossary_tooltip text="Container Storage Interface" term_id="csi" >}} رابطی جدیدتر است که چندین مشکل FlexVolume را برطرف می‌کند.

<!--more--> 

FlexVolumeها به کاربران امکان می‌دهند درایورهای خود را بنویسند و پشتیبانی از حجم‌های (volumes) خود را به کوبرنتیز اضافه کنند. فایل‌های باینری درایور FlexVolume و وابستگی‌های آن باید روی ماشین‌های میزبان نصب شوند. این کار به دسترسی root نیاز دارد. SIG Storage توصیه می‌کند در صورت امکان یک درایور {{< glossary_tooltip text="CSI" term_id="csi" >}} پیاده‌سازی شود، زیرا این رابط محدودیت‌های FlexVolumeها را برطرف می‌کند.

* [FlexVolume در مستندات کوبرنتیز](/docs/concepts/storage/volumes/#flexvolume)
* [اطلاعات بیشتر درباره FlexVolumeها](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-storage/flexvolume.md)
* [پرسش‌های متداول افزونه حجم برای فروشندگان ذخیره‌سازی](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md)
