---
title: حجم ماندگار (Persistent Volume)
id: persistent-volume
full_link: /docs/concepts/storage/persistent-volumes/
short_description: >
  آبجکتی در API که بخشی از فضای ذخیره‌سازی در کلاستر را نمایندگی می‌کند.

aka: 
tags:
- core-object
- storage
---
آبجکتی در API که بخشی از فضای ذخیره‌سازی در کلاستر را نمایندگی می‌کند. این آبجکت ذخیره‌سازی را به‌صورت یک
{{< glossary_tooltip text="منبع" term_id="infrastructure-resource" >}} عمومی و افزونه‌پذیر نمایش می‌دهد که می‌تواند فراتر از چرخهٔ عمر هر
{{< glossary_tooltip text="Pod" term_id="pod" >}} منفرد باقی بماند.

<!--more--> 

آبجکت‌های PersistentVolume (PV) یک API فراهم می‌کنند که جزئیات نحوهٔ تأمین ذخیره‌سازی را از نحوهٔ مصرف آن جدا و انتزاعی می‌کند.
در سناریوهایی که بتوان ذخیره‌سازی را از پیش ایجاد کرد (تأمین ایستا یا static provisioning)، از PVها به‌طور مستقیم استفاده می‌شود.
در سناریوهایی که به ذخیره‌سازی درخواستی (تأمین پویا یا dynamic provisioning) نیاز دارند، به‌جای آن از PersistentVolumeClaimها (PVC) استفاده می‌شود.
