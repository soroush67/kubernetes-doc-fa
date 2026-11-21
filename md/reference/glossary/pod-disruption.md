---
id: pod-disruption
title: اختلال Pod
full_link: /docs/concepts/workloads/pods/disruptions/
short_description: >
  فرایندی که طی آن Podهای روی نودها به‌صورت داوطلبانه یا غیرداوطلبانه خاتمه می‌یابند.

aka:
related:
 - pod
 - container
tags:
 - operation
---

[اختلال Pod](/docs/concepts/workloads/pods/disruptions/) (Pod disruption) فرایندی است که طی آن
Podهای روی نودها به‌صورت داوطلبانه یا غیرداوطلبانه خاتمه می‌یابند.

<!--more--> 

اختلال‌های داوطلبانه را مالکان برنامه‌ها یا مدیران کلاستر به‌طور عمدی آغاز می‌کنند.
اختلال‌های غیرداوطلبانه ناخواسته‌اند و ممکن است بر اثر مشکلات اجتناب‌ناپذیر، مانند تمام‌شدن
{{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} نودها، یا بر اثر حذف‌های تصادفی رخ دهند.
