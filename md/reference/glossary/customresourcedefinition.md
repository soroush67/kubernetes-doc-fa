---
title: CustomResourceDefinition
id: CustomResourceDefinition
full_link: /docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
short_description: >
  کد سفارشی که منبعی را برای افزودن به سرور API کوبرنتیز شما تعریف می‌کند، بدون آنکه لازم باشد یک سرور سفارشی کامل بسازید.

aka: 
tags:
- fundamental
- operation
- extension
---
نوعی {{< glossary_tooltip text="آبجکت API" term_id="object" >}} که یک API سفارشی جدید را برای افزودن به سرور API کوبرنتیز شما تعریف می‌کند، بدون آنکه لازم باشد یک سرور سفارشی کامل بسازید.

<!--more-->

اگر {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} داخلی کوبرنتیز نیازهای شما را برآورده نکنند، می‌توانید با استفاده از آبجکت‌های CustomResourceDefinition، API کوبرنتیز را متناسب با محیط خود گسترش دهید.
