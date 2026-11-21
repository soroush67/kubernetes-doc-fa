---
title: PodTemplate
id: pod-template
short_description: >
  الگویی برای ایجاد Podها.

aka: 
  - pod template
tags:
- core-object

---
آبجکتی در API که الگویی (template) برای ایجاد {{< glossary_tooltip text="Podها" term_id="pod" >}} تعریف می‌کند.
API مربوط به PodTemplate در تعریف‌های API مربوط به مدیریت بار کاری، مانند
{{< glossary_tooltip text="Deployment" term_id="deployment" >}} یا
{{< glossary_tooltip text="StatefulSetها" term_id="StatefulSet" >}}، نیز جاسازی شده است.

<!--more--> 

با الگوهای Pod می‌توانید فراداده‌های مشترک (مانند برچسب‌ها یا الگویی برای نام یک Pod جدید) را تعریف کنید
و وضعیت مطلوب یک Pod را نیز مشخص کنید.
کنترل‌کننده‌های [مدیریت بار کاری](/docs/concepts/workloads/controllers/) از الگوهای Pod
(که درون آبجکت دیگری مانند Deployment یا StatefulSet جاسازی شده‌اند)
برای تعریف و مدیریت یک یا چند {{< glossary_tooltip text="Pod" term_id="pod" >}} استفاده می‌کنند.
هنگامی که چند Pod بر پایهٔ یک الگوی یکسان وجود داشته باشد، به آن‌ها
{{< glossary_tooltip term_id="replica" text="رپلیکا" >}} گفته می‌شود.
اگرچه می‌توانید یک آبجکت PodTemplate را مستقیماً ایجاد کنید، به‌ندرت به این کار نیاز پیدا می‌کنید.
