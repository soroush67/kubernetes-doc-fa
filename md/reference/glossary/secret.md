---
title: Secret
id: secret
full_link: /docs/concepts/configuration/secret/
short_description: >
  اطلاعات حساس مانند گذرواژه‌ها، توکن‌های OAuth و کلیدهای ssh را ذخیره می‌کند.

aka:
tags:
- core-object
- security
---
 اطلاعات حساس مانند گذرواژه‌ها، توکن‌های OAuth و کلیدهای SSH را ذخیره می‌کند.

<!--more-->

با استفاده از Secretها کنترل بیشتری بر نحوهٔ استفاده از اطلاعات حساس خواهید داشت و خطر افشای ناخواستهٔ آن‌ها نیز کاهش می‌یابد. مقادیر Secret به‌صورت رشته‌های base64 کدگذاری می‌شوند و به‌طور پیش‌فرض بدون رمزنگاری ذخیره می‌شوند، اما می‌توان آن‌ها را طوری پیکربندی کرد که
[در حالت سکون رمزنگاری شوند](/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

هر {{< glossary_tooltip text="Pod" term_id="pod" >}} می‌تواند به روش‌های گوناگونی به Secret ارجاع دهد؛ برای نمونه از طریق اتصال (mount) یک حجم (volume) یا به‌صورت یک متغیر محیطی.
Secretها برای داده‌های محرمانه طراحی شده‌اند و
[ConfigMapها](/docs/tasks/configure-pod-container/configure-pod-configmap/) برای داده‌های غیرمحرمانه.
