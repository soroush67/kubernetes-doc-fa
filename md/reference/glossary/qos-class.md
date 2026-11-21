---
title: کلاس QoS
id: qos-class
full_link: /docs/concepts/workloads/pods/pod-qos/
short_description: >
  کلاس QoS (کلاس کیفیت سرویس) روشی در اختیار کوبرنتیز می‌گذارد تا پادهای درون کلاستر را در چند کلاس دسته‌بندی کند و دربارهٔ زمان‌بندی و بیرون‌رانی (eviction) آن‌ها تصمیم بگیرد.

aka: 
tags:
- fundamental
- architecture
related:
 - pod

---
 کلاس QoS (کلاس کیفیت سرویس یا Quality of Service Class) روشی در اختیار کوبرنتیز می‌گذارد تا Podهای درون کلاستر را در چند کلاس دسته‌بندی کند و دربارهٔ زمان‌بندی و بیرون‌رانی (eviction) آن‌ها تصمیم بگیرد.

<!--more--> 
کلاس QoS هر Pod در زمان ایجاد آن و بر اساس تنظیمات درخواست‌ها (requests) و محدودیت‌های (limits) {{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}} آن تعیین می‌شود. از کلاس‌های QoS برای تصمیم‌گیری دربارهٔ زمان‌بندی و بیرون‌رانی Podها استفاده می‌شود.
کوبرنتیز می‌تواند یکی از کلاس‌های QoS زیر را به یک Pod اختصاص دهد: `Guaranteed`، `Burstable` یا `BestEffort`.
