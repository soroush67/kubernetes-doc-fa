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

Secretها کنترل بیشتری بر نحوهٔ استفاده از اطلاعات حساس در اختیار شما قرار می‌دهند و خطر افشای تصادفی این اطلاعات را کاهش می‌دهند. مقادیر Secret به‌صورت رشته‌های base64 کدگذاری می‌شوند و به‌طور پیش‌فرض بدون رمزنگاری ذخیره می‌شوند، اما می‌توان آن‌ها را طوری پیکربندی کرد که [در حالت سکون (at rest) رمزنگاری شوند](/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

یک {{< glossary_tooltip text="Pod" term_id="pod" >}} می‌تواند به شیوه‌های گوناگونی به Secret ارجاع دهد، مانند استفاده در یک volume mount یا به‌عنوان متغیر محیطی. Secretها برای داده‌های محرمانه طراحی شده‌اند و [ConfigMapها](/docs/tasks/configure-pod-container/configure-pod-configmap/) برای داده‌های غیرمحرمانه طراحی شده‌اند.
