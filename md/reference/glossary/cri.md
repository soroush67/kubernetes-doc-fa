---
title: رابط محیط اجرای کانتینر (CRI)
id: cri
full_link: /docs/concepts/architecture/cri
short_description: >
  پروتکلی برای ارتباط میان kubelet و محیط اجرای کانتینر محلی.

aka:
tags:
  - fundamental
---

پروتکل اصلی برای ارتباط میان {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و محیط اجرای کانتینر.

<!--more-->

رابط محیط اجرای کانتینر (Container Runtime Interface) در کوبرنتیز، پروتکل اصلی
[gRPC](https://grpc.io) را برای ارتباط میان
[مؤلفه‌های نود](/docs/concepts/architecture/#node-components)، یعنی
{{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و
{{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}}، تعریف می‌کند.
