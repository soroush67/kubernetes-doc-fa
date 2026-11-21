---
title: فضای نام (Namespace)
id: namespace
full_link: /docs/concepts/overview/working-with-objects/namespaces
short_description: >
  انتزاعی که کوبرنتیز برای پشتیبانی از جداسازی گروه‌هایی از منابع درون یک کلاستر واحد از آن استفاده می‌کند.

aka: 
tags:
- fundamental
---
انتزاعی که کوبرنتیز برای پشتیبانی از جداسازی گروه‌هایی از {{< glossary_tooltip text="منابع API" term_id="api-resource" >}}
درون یک {{< glossary_tooltip text="کلاستر" term_id="cluster" >}} واحد از آن استفاده می‌کند.

<!--more--> 

فضاهای نام برای سازمان‌دهی آبجکت‌ها در یک کلاستر استفاده می‌شوند و راهی برای تقسیم منابع کلاستر فراهم می‌کنند. نام منابع باید درون هر فضای نام یکتا باشد، اما لازم نیست در میان فضاهای نام مختلف یکتا باشد. دامنه‌بندی مبتنی بر فضای نام فقط برای منابع وابسته به فضای نام _(برای مثال: Pods، Deployments، Services)_ کاربرد دارد و برای منابع سطح کلاستر _(برای مثال: StorageClasses، Nodes، PersistentVolumes)_ کاربردی ندارد.
