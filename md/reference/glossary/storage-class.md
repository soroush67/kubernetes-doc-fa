---
title: کلاس ذخیره‌سازی
id: storageclass
full_link: /docs/concepts/storage/storage-classes
short_description: >
  هر StorageClass روشی در اختیار مدیران قرار می‌دهد تا انواع مختلف ذخیره‌سازی موجود را توصیف کنند.

aka: 
tags:
- core-object
- storage
---
 هر StorageClass روشی در اختیار مدیران قرار می‌دهد تا انواع مختلف ذخیره‌سازی موجود را توصیف کنند.

<!--more--> 

هر StorageClass می‌تواند به سطوح کیفیت سرویس (quality-of-service)، سیاست‌های پشتیبان‌گیری یا سیاست‌های دلخواهی که مدیران کلاستر تعیین می‌کنند نگاشت شود. هر StorageClass فیلدهای `provisioner`، `parameters` و `reclaimPolicy` را دارد. این فیلدها زمانی استفاده می‌شوند که لازم باشد یک {{< glossary_tooltip text="حجم پایدار" term_id="persistent-volume" >}} متعلق به آن کلاس به‌صورت پویا فراهم شود. کاربران می‌توانند با استفاده از نام یک آبجکت StorageClass، کلاس مشخصی را درخواست کنند.
