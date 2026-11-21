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
آبجکتی که مصرف کل منابع را در هر {{< glossary_tooltip term_id="namespace" >}} محدود می‌کند.

<!--more-->

هر ResourceQuota می‌تواند تعداد {{< glossary_tooltip text="منابع API" term_id="api-resource" >}} قابل ایجاد در یک فضای نام (namespace) را به تفکیک نوع محدود کند، یا برای مقدار کل {{< glossary_tooltip text="منابع زیرساختی" term_id="infrastructure-resource" >}} که از طرف آن فضای نام (و آبجکت‌های درون آن) مصرف می‌شود، سقفی تعیین کند.
