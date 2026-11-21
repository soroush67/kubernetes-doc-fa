---
title: Job
id: job
full_link: /docs/concepts/workloads/controllers/job/
short_description: >
  یک وظیفهٔ محدود یا دسته‌ای (batch) که تا پایان اجرا می‌شود.

aka: 
tags:
- fundamental
- core-object
- workload
---
 یک وظیفهٔ محدود یا دسته‌ای (batch) که تا پایان اجرا می‌شود.

<!--more--> 

یک یا چند آبجکت {{< glossary_tooltip term_id="pod" >}} ایجاد می‌کند و اطمینان می‌دهد که تعداد مشخصی از آن‌ها با موفقیت خاتمه یابند. هم‌زمان با تکمیل موفقیت‌آمیز Podها، آبجکت Job تعداد تکمیل‌های موفق را پیگیری می‌کند.
