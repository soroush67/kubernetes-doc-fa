---
title: ResourceQuota
id: resource-quota
full_link: /docs/concepts/policy/resource-quotas/
short_description: >
  محدودیت‌هایی فراهم می‌کند که مصرف کل منابع را در هر فضای نام محدود می‌کنند.

aka: 
tags:
- fundamental
- operation
- architecture
---
آبجکتی که مصرف کل منابع را در هر {{< glossary_tooltip term_id="namespace" text="فضای نام" >}} محدود می‌کند.

<!--more-->

یک ResourceQuota می‌تواند تعداد {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} قابل ایجاد در یک فضای نام را بر اساس نوع محدود کند، یا می‌تواند سقفی برای مقدار کل
{{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}}
تعیین کند که به نمایندگی از فضای نام (و آبجکت‌های درون آن) ممکن است مصرف شوند.
