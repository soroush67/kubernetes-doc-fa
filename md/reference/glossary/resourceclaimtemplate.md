---
title: ResourceClaimTemplate
id: resourceclaimtemplate
full_link: /docs/concepts/resource-management/dynamic-resource-allocation/dra-api/#resourceclaims-templates
short_description: >
  قالبی را تعریف می‌کند که کوبرنتیز از روی آن ResourceClaimها را ایجاد می‌کند. برای فراهم‌کردن دسترسی به منابع جداگانه و مشابه، به‌ازای هر Pod یا هر PodGroup، استفاده می‌شود.

tags:
- workload
---
 قالبی را تعریف می‌کند که کوبرنتیز برای ایجاد
{{< glossary_tooltip text="ResourceClaimها" term_id="resourceclaim" >}}
از آن استفاده می‌کند.
ResourceClaimTemplateها در
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
برای فراهم‌کردن _دسترسی به منابع جداگانه و مشابه، به‌ازای هر Pod یا هر {{< glossary_tooltip text="PodGroup" term_id="podgroup" >}}_ به کار می‌روند.

<!--more-->

هنگامی که یک ResourceClaimTemplate در مشخصات بار کاری ارجاع داده می‌شود،
کوبرنتیز به‌طور خودکار آبجکت‌های ResourceClaim را بر اساس آن قالب ایجاد می‌کند.
هر ResourceClaim به یک Pod یا PodGroup مشخص متصل است. وقتی Pod
خاتمه می‌یابد یا PodGroup حذف می‌شود، کوبرنتیز ResourceClaim متناظر را حذف می‌کند.
ResourceClaimTemplateهای مربوط به PodGroup نیازمند آن هستند که قابلیت
[`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims)
فعال شده باشد.
