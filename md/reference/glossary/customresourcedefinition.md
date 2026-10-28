---
title: CustomResourceDefinition
id: CustomResourceDefinition
full_link: /docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
short_description: >
  کد سفارشی که یک منبع را تعریف می‌کند تا بدون ساخت یک سرور سفارشی کامل، به سرور API کوبرنتیز اضافه شود.

aka: 
tags:
- fundamental
- operation
- extension
---
نوعی {{< glossary_tooltip text="آبجکت API" term_id="object" >}} که یک API سفارشی جدید را تعریف می‌کند تا بدون ساخت یک سرور سفارشی کامل، به سرور API کوبرنتیز شما اضافه شود.

<!--more-->

اگر {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} داخلی نتوانند نیازهای شما را برآورده کنند، CustomResourceDefinitionها به شما امکان می‌دهند API کوبرنتیز را برای محیط خود گسترش دهید.
