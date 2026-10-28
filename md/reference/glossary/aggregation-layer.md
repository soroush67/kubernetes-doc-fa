---
title: لایه تجمیع (Aggregation Layer)
id: aggregation-layer
full_link: /docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
short_description: >
  لایه تجمیع به شما امکان می‌دهد APIهای اضافی به سبک کوبرنتیز را در کلاستر خود نصب کنید.

aka: 
tags:
- architecture
- extension
- operation
---
 لایه تجمیع به شما امکان می‌دهد APIهای اضافی به سبک کوبرنتیز را در کلاستر خود نصب کنید.

<!--more-->

هنگامی که {{< glossary_tooltip text="سرور API کوبرنتیز" term_id="kube-apiserver" >}} را برای [پشتیبانی از APIهای اضافی](/docs/tasks/extend-kubernetes/configure-aggregation-layer/) پیکربندی کرده‌اید، می‌توانید آبجکت‌های `APIService` را اضافه کنید تا یک مسیر URL را در API کوبرنتیز «تصاحب» کنند.
