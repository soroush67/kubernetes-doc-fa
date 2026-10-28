---
title: Storage Class
id: storageclass
full_link: /docs/concepts/storage/storage-classes
short_description: >
  یک StorageClass راهی در اختیار مدیران قرار می‌دهد تا انواع مختلف ذخیره‌سازی در دسترس را توصیف کنند.

aka: 
tags:
- core-object
- storage
---
 یک StorageClass راهی در اختیار مدیران قرار می‌دهد تا انواع مختلف ذخیره‌سازی در دسترس را توصیف کنند.

<!--more--> 

StorageClassها می‌توانند به سطوح کیفیت سرویس (quality-of-service)، سیاست‌های پشتیبان‌گیری یا سیاست‌های دلخواهی که مدیران کلاستر تعیین می‌کنند نگاشت شوند. هر StorageClass شامل فیلدهای `provisioner`، `parameters` و `reclaimPolicy` است که هنگامی به کار می‌روند که یک {{< glossary_tooltip text="Persistent Volume" term_id="persistent-volume" >}} متعلق به آن کلاس باید به‌صورت پویا تأمین شود. کاربران می‌توانند با استفاده از نام یک آبجکت StorageClass، کلاس مشخصی را درخواست کنند.
