---
id: pod-disruption
title: اختلال در Pod
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

[اختلال در Pod](/docs/concepts/workloads/pods/disruptions/) فرایندی است که طی آن
Podهای روی نودها به‌صورت داوطلبانه یا غیرداوطلبانه خاتمه می‌یابند.

<!--more--> 

اختلال‌های داوطلبانه به‌صورت عمدی توسط مالکان برنامه یا مدیران کلاستر آغاز می‌شوند.
اختلال‌های غیرداوطلبانه عمدی نیستند و می‌توانند در اثر مشکلات اجتناب‌ناپذیری مانند تمام شدن
{{< glossary_tooltip text="منابع" term_id="infrastructure-resource" >}} نودها،
یا در اثر حذف‌های ناخواسته رخ دهند.
