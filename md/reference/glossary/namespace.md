---
title: Namespace
id: namespace
full_link: /docs/concepts/overview/working-with-objects/namespaces
short_description: >
  یک انتزاع (abstraction) که کوبرنتیز برای پشتیبانی از جداسازی گروه‌هایی از منابع در یک کلاستر واحد به کار می‌برد.

aka: 
tags:
- fundamental
---
یک انتزاع (abstraction) که کوبرنتیز برای پشتیبانی از جداسازی گروه‌هایی از {{< glossary_tooltip text="منابع API" term_id="api-resource" >}}
در یک {{< glossary_tooltip text="کلاستر" term_id="cluster" >}} واحد به کار می‌برد.

<!--more--> 

فضاهای نام (namespace) برای سازمان‌دهی آبجکت‌ها در یک کلاستر و فراهم‌کردن روشی برای تقسیم منابع کلاستر استفاده می‌شوند. نام منابع باید درون یک فضای نام یکتا باشد، اما لازم نیست در میان فضاهای نام مختلف یکتا باشد. محدودسازی مبتنی بر فضای نام فقط برای منابعِ دارای فضای نام _(برای مثال: Pods، Deployments، Services)_ کاربرد دارد و برای منابع سراسری کلاستر _(برای مثال: StorageClasses، Nodes، PersistentVolumes)_ اعمال نمی‌شود.
