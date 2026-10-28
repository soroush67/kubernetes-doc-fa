---
title: Container Runtime
id: container-runtime
full_link: /docs/setup/production-environment/container-runtimes
short_description: >
 محیط اجرای کانتینر نرم‌افزاری است که مسئول اجرای کانتینرها است.

aka:
tags:
- fundamental
- workload
---
 یک مؤلفه بنیادین که کوبرنتیز را قادر می‌سازد کانتینرها را به‌طور مؤثر اجرا کند.
 این مؤلفه مسئول مدیریت اجرا و چرخه عمر کانتینرها در محیط کوبرنتیز است.

<!--more-->

کوبرنتیز از محیط‌های اجرای کانتینر مانند
{{< glossary_tooltip term_id="containerd" >}}، {{< glossary_tooltip term_id="cri-o" >}}
و هر پیاده‌سازی دیگری از [رابط محیط اجرای کانتینر کوبرنتیز (Kubernetes CRI)](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-node/container-runtime-interface.md)
پشتیبانی می‌کند.
