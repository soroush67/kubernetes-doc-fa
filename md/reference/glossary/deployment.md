---
title: Deployment
id: deployment
full_link: /docs/concepts/workloads/controllers/deployment/
short_description: >
  یک برنامه تکثیرشده را در کلاستر شما مدیریت می‌کند.

aka: 
tags:
- fundamental
- core-object
- workload
---
 یک آبجکت API که یک برنامه تکثیرشده را مدیریت می‌کند و معمولاً این کار را با اجرای Podهایی انجام می‌دهد که هیچ وضعیت محلی ندارند.

<!--more--> 

هر replica با یک {{< glossary_tooltip term_id="pod" >}} نمایش داده می‌شود و Podها میان {{< glossary_tooltip text="نودهای" term_id="node" >}} یک کلاستر توزیع می‌شوند.
برای بارهای کاری‌ای که به وضعیت محلی نیاز دارند، استفاده از {{< glossary_tooltip term_id="StatefulSet" >}} را در نظر بگیرید.
