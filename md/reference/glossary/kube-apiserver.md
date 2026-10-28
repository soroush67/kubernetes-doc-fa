---
title: سرور API
id: kube-apiserver
full_link: /docs/concepts/architecture/#kube-apiserver
short_description: >
  مؤلفه control plane که API کوبرنتیز را ارائه می‌دهد.

aka:
- kube-apiserver
tags:
- architecture
- fundamental
---
 سرور API مؤلفه‌ای از {{< glossary_tooltip text="control plane" term_id="control-plane" >}} کوبرنتیز است که API کوبرنتیز را در دسترس قرار می‌دهد.
سرور API لایه جلویی (front end) control plane کوبرنتیز است.

<!--more-->

پیاده‌سازی اصلی سرور API کوبرنتیز، [kube-apiserver](/docs/reference/generated/kube-apiserver/) است.
kube-apiserver طوری طراحی شده است که به‌صورت افقی مقیاس‌پذیر باشد&mdash;یعنی با استقرار نمونه‌های بیشتر مقیاس می‌یابد.
می‌توانید چندین نمونه از kube-apiserver را اجرا کنید و ترافیک را میان این نمونه‌ها متعادل کنید.
