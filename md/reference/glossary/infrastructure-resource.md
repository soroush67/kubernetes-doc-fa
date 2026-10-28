---
title: منبع (زیرساخت)
id: infrastructure-resource
short_description: >
  مقدار مشخصی از زیرساخت که برای مصرف در دسترس است (CPU، حافظه و غیره).

aka:
tags:
- architecture
---
قابلیت‌هایی که در اختیار یک یا چند {{< glossary_tooltip text="نود" term_id="node" >}} قرار می‌گیرند (CPU، حافظه، GPU و غیره) و برای مصرف توسط
{{< glossary_tooltip text="Podهایی" term_id="pod" >}} که روی آن نودها اجرا می‌شوند در دسترس قرار داده می‌شوند.

کوبرنتیز همچنین از اصطلاح _منبع_ برای توصیف یک {{< glossary_tooltip text="منبع API" term_id="api-resource" >}} استفاده می‌کند.

<!--more-->
رایانه‌ها امکانات سخت‌افزاری بنیادینی را فراهم می‌کنند: توان پردازشی، حافظه ذخیره‌سازی، شبکه و غیره.
این منابع ظرفیت محدودی دارند که با واحدی متناسب با همان منبع اندازه‌گیری می‌شود (تعداد CPUها، بایت‌های حافظه و غیره).
کوبرنتیز [منابع](/docs/concepts/configuration/manage-resources-containers/) رایج را برای تخصیص به بارهای کاری انتزاعی می‌کند
و برای مدیریت مصرف توسط {{< glossary_tooltip text="بارهای کاری" term_id="workload" >}} از primitiveهای سیستم‌عامل (برای مثال {{< glossary_tooltip text="cgroups" term_id="cgroup" >}} در لینوکس) استفاده می‌کند.

همچنین می‌توانید از [تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/) برای
مدیریت خودکار تخصیص‌های پیچیده منابع استفاده کنید.
