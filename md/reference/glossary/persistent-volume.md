---
title: Persistent Volume
id: persistent-volume
full_link: /docs/concepts/storage/persistent-volumes/
short_description: >
  آبجکت API که نمایانگر بخشی از ذخیره‌سازی در کلاستر است.

aka: 
tags:
- core-object
- storage
---
یک آبجکت API که نمایانگر بخشی از ذخیره‌سازی در کلاستر است. این آبجکت به‌صورت یک {{< glossary_tooltip text="منبع" term_id="infrastructure-resource" >}} ذخیره‌سازی عمومی و قابل‌اتصال (pluggable) نمایش داده می‌شود که می‌تواند فراتر از چرخه حیات هر {{< glossary_tooltip text="Pod" term_id="pod" >}} منفرد باقی بماند.

<!--more--> 

PersistentVolumeها (PV) یک API فراهم می‌کنند که جزئیات نحوه تأمین ذخیره‌سازی را از نحوه مصرف آن جدا و انتزاعی می‌کند.
PVها مستقیماً در سناریوهایی به کار می‌روند که ذخیره‌سازی را می‌توان از پیش ایجاد کرد (تأمین ایستا یا static provisioning).
برای سناریوهایی که به ذخیره‌سازی بر حسب تقاضا نیاز دارند (تأمین پویا یا dynamic provisioning)، به‌جای آن از PersistentVolumeClaimها (PVC) استفاده می‌شود.
