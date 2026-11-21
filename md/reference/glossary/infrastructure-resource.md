---
title: منبع (زیرساخت)
id: infrastructure-resource
short_description: >
  مقدار مشخصی از زیرساخت که برای مصرف در دسترس است (CPU، حافظه و غیره).

aka:
tags:
- architecture
---
قابلیت‌هایی (مانند CPU، حافظه، GPU و غیره) که در اختیار یک یا چند {{< glossary_tooltip text="نود" term_id="node" >}} قرار می‌گیرند و
{{< glossary_tooltip text="Podهایی" term_id="pod" >}} که روی آن نودها اجرا می‌شوند، می‌توانند آن‌ها را مصرف کنند.

کوبرنتیز اصطلاح _منبع_ (resource) را برای توصیف یک {{< glossary_tooltip text="منبع API" term_id="api-resource" >}} نیز به کار می‌برد.

<!--more-->
رایانه‌ها امکانات سخت‌افزاری بنیادینی مانند توان پردازشی، حافظهٔ ذخیره‌سازی، شبکه و غیره را فراهم می‌کنند.
ظرفیت این منابع محدود است و با واحدی متناسب با هر منبع (تعداد CPUها، تعداد بایت‌های حافظه و غیره) اندازه‌گیری می‌شود.
کوبرنتیز [منابع](/docs/concepts/configuration/manage-resources-containers/) رایج را برای تخصیص به بارهای کاری انتزاع می‌کند
و برای مدیریت مصرف {{< glossary_tooltip text="بارهای کاری" term_id="workload" >}}) از سازوکارهای پایه‌ای سیستم‌عامل (برای نمونه، {{< glossary_tooltip text="cgroupها" term_id="cgroup" >}} در لینوکس) بهره می‌گیرد.

همچنین می‌توانید با استفاده از [تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/)
تخصیص‌های پیچیدهٔ منابع را به‌صورت خودکار مدیریت کنید.
