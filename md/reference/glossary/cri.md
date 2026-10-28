---
title: رابط زمان اجرای کانتینر (CRI)
id: cri
full_link: /docs/concepts/architecture/cri
short_description: >
  پروتکل ارتباط میان kubelet و زمان اجرای کانتینر محلی.

aka:
tags:
  - fundamental
---

پروتکل اصلی برای ارتباط میان {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و زمان اجرای کانتینر (Container Runtime).

<!--more-->

رابط زمان اجرای کانتینر (Container Runtime Interface یا CRI) در کوبرنتیز، پروتکل اصلی مبتنی بر [gRPC](https://grpc.io) را برای ارتباط میان
[مؤلفه‌های نود](/docs/concepts/architecture/#node-components)
یعنی {{< glossary_tooltip text="kubelet" term_id="kubelet" >}} و
{{< glossary_tooltip text="زمان اجرای کانتینر" term_id="container-runtime" >}}
تعریف می‌کند.
