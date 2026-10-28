---
title: کلاس QoS
id: qos-class
full_link: /docs/concepts/workloads/pods/pod-qos/
short_description: >
  کلاس QoS (کلاس کیفیت سرویس) روشی در اختیار کوبرنتیز قرار می‌دهد تا Podهای درون کلاستر را در چند کلاس دسته‌بندی کند و درباره زمان‌بندی و اخراج (eviction) تصمیم‌گیری کند.

aka: 
tags:
- fundamental
- architecture
related:
 - pod

---
 کلاس QoS (کلاس کیفیت سرویس) روشی در اختیار کوبرنتیز قرار می‌دهد تا Podهای درون کلاستر را در چند کلاس دسته‌بندی کند و درباره زمان‌بندی و اخراج (eviction) تصمیم‌گیری کند.

<!--more--> 
کلاس QoS یک Pod هنگام ایجاد آن و بر اساس تنظیمات درخواست‌ها (requests) و محدودیت‌های (limits) مربوط به {{< glossary_tooltip text="منبع زیرساختی" term_id="infrastructure-resource" >}} آن تعیین می‌شود. کلاس‌های QoS برای تصمیم‌گیری درباره زمان‌بندی و اخراج Podها به کار می‌روند.
کوبرنتیز می‌تواند یکی از کلاس‌های QoS زیر را به یک Pod اختصاص دهد: `Guaranteed`، `Burstable` یا `BestEffort`.
