---
title: ResourceClaimTemplate
id: resourceclaimtemplate
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceclaims-templates
short_description: >
  الگویی تعریف می‌کند که کوبرنتیز بر اساس آن ResourceClaimها را ایجاد می‌کند. از آن برای فراهم کردن
  دسترسی هر Pod یا هر PodGroup به منابع مشابه اما جداگانه استفاده می‌شود.

tags:
- workload
---
 این آبجکت الگویی تعریف می‌کند که کوبرنتیز با استفاده از آن
{{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}} را ایجاد می‌کند.
در [تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
از ResourceClaimTemplateها برای فراهم کردن _دسترسی هر Pod یا هر {{< glossary_tooltip text="PodGroup" term_id="podgroup" >}} به منابع مشابه اما جداگانه_ استفاده می‌شود.

<!--more-->

هنگامی که در مشخصات یک بار کاری به یک ResourceClaimTemplate ارجاع داده شود،
کوبرنتیز به‌طور خودکار آبجکت‌های ResourceClaim را بر اساس این الگو ایجاد می‌کند.
هر ResourceClaim به یک Pod یا PodGroup مشخص متصل می‌شود. هنگامی که Pod
خاتمه می‌یابد یا PodGroup حذف می‌شود، کوبرنتیز ResourceClaim متناظر با آن را حذف می‌کند.
برای استفاده از ResourceClaimTemplateهای مربوط به PodGroup، باید قابلیت
[`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims)
فعال باشد.
