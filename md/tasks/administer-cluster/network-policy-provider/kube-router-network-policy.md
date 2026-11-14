---
reviewers:
- murali-reddy
title: استفاده از Kube-router برای NetworkPolicy
content_type: task
weight: 40
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان از [Kube-router](https://github.com/cloudnativelabs/kube-router) برای NetworkPolicy استفاده کرد.


## {{% heading "prerequisites" %}}

باید یک کلاستر کوبرنتیز در حال اجرا داشته باشید. اگر هنوز کلاستری ندارید، می‌توانید با هر یک از نصب‌کننده‌های کلاستر مانند Kops، Bootkube، Kubeadm و غیره یک کلاستر ایجاد کنید.


<!-- steps -->
## نصب افزونهٔ Kube-router
افزونهٔ (addon) Kube-router همراه با یک کنترل‌کنندهٔ سیاست شبکه (Network Policy Controller) ارائه می‌شود. این کنترل‌کننده تغییرات هر NetworkPolicy و پادها را از طریق API server کوبرنتیز زیر نظر می‌گیرد و قواعد iptables و ipsetها را طوری پیکربندی می‌کند که ترافیک، مطابق دستور سیاست‌ها، مجاز یا مسدود شود. برای نصب افزونهٔ Kube-router، لطفاً راهنمای [امتحان Kube-router با نصب‌کننده‌های کلاستر](https://www.kube-router.io/docs/user-guide/#try-kube-router-with-cluster-installers) را دنبال کنید.


## {{% heading "whatsnext" %}}

پس از نصب افزونهٔ Kube-router، می‌توانید راهنمای [اعلان سیاست شبکه](/docs/tasks/administer-cluster/declare-network-policy/) را دنبال کنید تا NetworkPolicy کوبرنتیز را امتحان کنید.
