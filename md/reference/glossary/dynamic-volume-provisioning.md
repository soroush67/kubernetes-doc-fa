---
title: تأمین پویای حجم (Dynamic Volume Provisioning)
id: dynamicvolumeprovisioning
full_link: /docs/concepts/storage/dynamic-provisioning
short_description: >
  به کاربران امکان می‌دهد ایجاد خودکار حجم‌های ذخیره‌سازی را درخواست کنند.

aka: 
tags:
- storage
---
 به کاربران امکان می‌دهد ایجاد خودکار {{< glossary_tooltip text="حجم‌های" term_id="volume" >}} ذخیره‌سازی را درخواست کنند.

<!--more--> 

با تأمین پویا، دیگر لازم نیست مدیران کلاستر از پیش فضای ذخیره‌سازی را تأمین کنند؛ در عوض، فضای ذخیره‌سازی بر اساس درخواست کاربر به‌طور خودکار تأمین می‌شود. تأمین پویای حجم بر پایهٔ یک آبجکت API به نام {{< glossary_tooltip text="StorageClass" term_id="storage-class" >}} کار می‌کند. این آبجکت به یک {{< glossary_tooltip text="افزونهٔ حجم (Volume Plugin)" term_id="volume-plugin" >}} که {{< glossary_tooltip text="حجم" term_id="volume" >}} را تأمین می‌کند و نیز به مجموعه پارامترهایی که باید به آن افزونه ارسال شوند، ارجاع می‌دهد.
