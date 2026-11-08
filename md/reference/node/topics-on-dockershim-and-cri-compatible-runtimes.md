---
title: مقاله‌هایی دربارهٔ حذف dockershim و استفاده از محیط‌های اجرای سازگار با CRI
content_type: reference
weight: 20
---
<!-- overview -->
این صفحه فهرستی از مقاله‌ها و صفحه‌هایی است که یا به منسوخ‌شدن و حذف _dockershim_ از کوبرنتیز می‌پردازند، یا موضوعشان استفاده از محیط‌های اجرای کانتینر سازگار با CRI در پی این حذف است.

<!-- body -->

## پروژهٔ کوبرنتیز

* وبلاگ کوبرنتیز: [پرسش‌های متداول دربارهٔ حذف Dockershim](/blog/2020/12/02/dockershim-faq/) (انتشار نخست: 2020/12/02)

* وبلاگ کوبرنتیز: [نسخهٔ به‌روزشده: پرسش‌های متداول دربارهٔ حذف Dockershim](/blog/2022/02/17/dockershim-faq/) (انتشار نسخهٔ به‌روزشده: 2022/02/17)

* وبلاگ کوبرنتیز: [کوبرنتیز از Dockershim عبور می‌کند: تعهدات و گام‌های بعدی](/blog/2022/01/07/kubernetes-is-moving-on-from-dockershim/) (انتشار: 2022/01/07)

* وبلاگ کوبرنتیز: [حذف Dockershim نزدیک است. آیا آماده‌اید؟](/blog/2021/11/12/are-you-ready-for-dockershim-removal/) (انتشار: 2021/11/12)

* مستندات کوبرنتیز: [مهاجرت از dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/)

* مستندات کوبرنتیز: [محیط‌های اجرای کانتینر](/docs/setup/production-environment/container-runtimes/)

* پیشنهاد بهبود کوبرنتیز: [KEP-2221: حذف dockershim از kubelet](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2221-remove-dockershim/README.md)

* ایشوی پیشنهاد بهبود کوبرنتیز: [حذف dockershim از kubelet](https://github.com/kubernetes/enhancements/issues/2221) (_k/enhancements#2221_)


می‌توانید بازخورد خود را در ایشوی GitHub با عنوان [**بازخوردها و مشکلات حذف Dockershim**](https://github.com/kubernetes/kubernetes/issues/106917) ثبت کنید. (_k/kubernetes/#106917_)

## منابع خارجی {#third-party}

<!-- sort these alphabetically -->

* مستندات EKS در Amazon Web Services: [پایان پشتیبانی Amazon EKS از Dockershim](https://docs.aws.amazon.com/eks/latest/userguide/dockershim-deprecation.html)

* ویدیوی کنفرانس CNCF: [درس‌هایی از مهاجرت کوبرنتیز از Docker به محیط اجرای containerd](https://www.youtube.com/watch?v=uDOu6rK4yOk) (Ana Caylin، در KubeCon Europe 2019)

* وبلاگ Docker.com: [آنچه توسعه‌دهندگان باید دربارهٔ Docker، Docker Engine و Kubernetes v1.20 بدانند](https://www.docker.com/blog/what-developers-need-to-know-about-docker-docker-engine-and-kubernetes-v1-20/) (انتشار: 2020/12/04)

* کانال «_Google Open Source_» در YouTube: [آموزش کوبرنتیز با Google - مهاجرت از Dockershim به Containerd](https://youtu.be/fl7_4hjT52g)

* وبلاگ Microsoft Apps on Azure: [منسوخ‌شدن Dockershim و AKS](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/dockershim-deprecation-and-aks/ba-p/3055902) (انتشار: 2022/01/21)

* وبلاگ Mirantis: [آیندهٔ Dockershim در cri-dockerd است](https://www.mirantis.com/blog/the-future-of-dockershim-is-cri-dockerd/) (انتشار: 2021/04/21)

* مستندات رسمی [Mirantis/cri-dockerd](https://mirantis.github.io/cri-dockerd/) از Mirantis

* منتشرشده در Tripwire: [منسوخ‌شدن پیش‌روی Dockershim چه تأثیری بر کوبرنتیز شما می‌گذارد](https://www.tripwire.com/state-of-security/security-data-protection/cloud/how-dockershim-forthcoming-deprecation-affects-your-kubernetes/) (انتشار: 2021/07/01)
