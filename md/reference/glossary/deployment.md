---
title: Deployment
id: deployment
full_link: /docs/concepts/workloads/controllers/deployment/
short_description: >
  یک برنامهٔ تکثیرشده را در کلاستر شما مدیریت می‌کند.

aka: 
tags:
- fundamental
- core-object
- workload
---
 آبجکتی از API که یک برنامهٔ تکثیرشده را مدیریت می‌کند و این کار را معمولاً با اجرای Podهایی انجام می‌دهد که حالت محلی (local state) ندارند.

<!--more--> 

هر رونوشت (replica) با یک {{< glossary_tooltip term_id="pod" >}} نمایش داده می‌شود و Podها میان
{{< glossary_tooltip text="نودهای" term_id="node" >}} یک کلاستر توزیع می‌شوند.
برای بارهای کاری‌ای که به حالت محلی نیاز دارند، بهتر است از {{< glossary_tooltip term_id="StatefulSet" >}} استفاده کنید.
