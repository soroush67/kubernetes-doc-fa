---
title: تأمین پویای حجم
id: dynamicvolumeprovisioning
full_link: /docs/concepts/storage/dynamic-provisioning
short_description: >
  به کاربران اجازه می‌دهد ایجاد خودکار حجم‌های ذخیره‌سازی را درخواست کنند.

aka: 
tags:
- storage
---
 به کاربران اجازه می‌دهد ایجاد خودکار {{< glossary_tooltip text="حجم‌های" term_id="volume" >}} ذخیره‌سازی را درخواست کنند.

<!--more--> 

تأمین پویا (Dynamic provisioning) نیاز مدیران کلاستر به تأمین پیشاپیش ذخیره‌سازی را از میان برمی‌دارد. در عوض، ذخیره‌سازی را به‌صورت خودکار و بنا به درخواست کاربر تأمین می‌کند. تأمین پویای حجم بر پایهٔ یک آبجکت API به نام {{< glossary_tooltip text="StorageClass" term_id="storage-class" >}} انجام می‌شود که به یک {{< glossary_tooltip text="افزونهٔ حجم" term_id="volume-plugin" >}} اشاره می‌کند؛ این افزونه یک {{< glossary_tooltip text="حجم" term_id="volume" >}} را تأمین می‌کند و StorageClass مجموعه‌ای از پارامترها را نیز برای ارسال به افزونهٔ حجم مشخص می‌کند.
