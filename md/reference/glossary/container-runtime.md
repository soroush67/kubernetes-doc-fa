---
title: محیط اجرای کانتینر
id: container-runtime
full_link: /docs/setup/production-environment/container-runtimes
short_description: >
 محیط اجرای کانتینر نرم‌افزاری است که مسئولیت اجرای کانتینرها را بر عهده دارد.

aka:
tags:
- fundamental
- workload
---
 محیط اجرای کانتینر (container runtime) مؤلفه‌ای بنیادین است که کوبرنتیز به کمک آن کانتینرها را به‌طور مؤثر اجرا می‌کند.
 این مؤلفه مدیریت اجرا و چرخهٔ حیات کانتینرها را در محیط کوبرنتیز بر عهده دارد.

<!--more-->

کوبرنتیز از محیط‌های اجرای کانتینری مانند
{{< glossary_tooltip term_id="containerd" >}}، {{< glossary_tooltip term_id="cri-o" >}}
و هر پیاده‌سازی دیگری از [رابط محیط اجرای کانتینر کوبرنتیز (Kubernetes CRI)](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-node/container-runtime-interface.md) پشتیبانی می‌کند.
