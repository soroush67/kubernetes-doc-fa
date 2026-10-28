---
title: PodTemplate
id: pod-template
short_description: >
  قالبی برای ایجاد Podها.

aka: 
  - pod template
tags:
- core-object

---
یک آبجکت API که قالبی برای ایجاد {{< glossary_tooltip text="Podها" term_id="pod" >}} تعریف می‌کند.
API مربوط به PodTemplate در تعریف‌های API برای مدیریت بار کاری نیز تعبیه می‌شود، مانند
{{< glossary_tooltip text="Deployment" term_id="deployment" >}} یا
{{< glossary_tooltip text="StatefulSets" term_id="StatefulSet" >}}.

<!--more--> 

قالب‌های Pod به شما امکان می‌دهند فراداده‌های مشترک (مانند برچسب‌ها یا قالبی برای نام
یک Pod جدید) را تعریف کنید و همچنین وضعیت مطلوب یک Pod را مشخص نمایید.
کنترل‌کننده‌های [مدیریت بار کاری](/docs/concepts/workloads/controllers/) از قالب‌های Pod
(که در آبجکتی دیگر، مانند Deployment یا StatefulSet، تعبیه شده‌اند)
برای تعریف و مدیریت یک یا چند {{< glossary_tooltip text="Pod" term_id="pod" >}} استفاده می‌کنند.
هنگامی که ممکن است چندین Pod بر پایهٔ یک قالب واحد وجود داشته باشند، به آن‌ها
{{< glossary_tooltip term_id="replica" text="replicaها" >}} گفته می‌شود.
اگرچه می‌توانید یک آبجکت PodTemplate را مستقیماً ایجاد کنید، به‌ندرت نیازی به این کار پیدا می‌کنید.
