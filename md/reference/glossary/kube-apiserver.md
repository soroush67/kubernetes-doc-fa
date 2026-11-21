---
title: سرور API
id: kube-apiserver
full_link: /docs/concepts/architecture/#kube-apiserver
short_description: >
  مؤلفه‌ای از control plane که API کوبرنتیز را ارائه می‌دهد.

aka:
- kube-apiserver
tags:
- architecture
- fundamental
---
 سرور API مؤلفه‌ای از
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز است که API کوبرنتیز را در دسترس قرار می‌دهد.
سرور API لایهٔ جلویی (front end) control plane کوبرنتیز است.

<!--more-->

پیاده‌سازی اصلی سرور API کوبرنتیز [kube-apiserver](/docs/reference/generated/kube-apiserver/) است.
مؤلفهٔ kube-apiserver برای مقیاس‌پذیری افقی طراحی شده است&mdash;یعنی با استقرار نمونه‌های بیشتر مقیاس می‌یابد.
می‌توانید چند نمونه از kube-apiserver را اجرا کنید و ترافیک را میان این نمونه‌ها توزیع کنید.
