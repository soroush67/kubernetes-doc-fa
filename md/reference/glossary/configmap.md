---
title: ConfigMap
id: configmap
full_link: /docs/concepts/configuration/configmap/
short_description: >
  یک آبجکت API که برای ذخیره داده‌های غیرمحرمانه به‌صورت جفت‌های کلید-مقدار استفاده می‌شود. می‌تواند به‌صورت متغیرهای محیطی، آرگومان‌های خط فرمان یا فایل‌های پیکربندی در یک حجم (volume) مصرف شود.

aka: 
tags:
- core-object
---
 یک آبجکت API که برای ذخیره داده‌های غیرمحرمانه به‌صورت جفت‌های کلید-مقدار استفاده می‌شود.
{{< glossary_tooltip text="Podها" term_id="pod" >}} می‌توانند ConfigMapها را به‌صورت
متغیرهای محیطی، آرگومان‌های خط فرمان یا فایل‌های پیکربندی در یک
{{< glossary_tooltip text="حجم (volume)" term_id="volume" >}} مصرف کنند.

<!--more--> 

ConfigMap به شما امکان می‌دهد پیکربندی وابسته به محیط را از {{< glossary_tooltip text="ایمیج‌های کانتینر" term_id="image" >}} جدا کنید، تا برنامه‌های شما به‌سادگی قابل انتقال باشند.
