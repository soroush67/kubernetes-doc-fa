---
title: "نصب ابزارها"
description: ابزارهای کوبرنتیز را روی رایانهٔ خود راه‌اندازی کنید.
weight: 10
no_list: true
card:
  name: tasks
  weight: 20
  anchors:
  - anchor: "#kubectl"
    title: نصب kubectl
---

{{< note >}}
برای راه‌اندازی یک محیط تمرینی، صفحهٔ [محیط یادگیری](/docs/setup/learning-environment/) را ببینید.
{{< /note >}}

## kubectl

<!-- overview -->
ابزار خط فرمان کوبرنتیز، یعنی [kubectl](/docs/reference/kubectl/kubectl/)، امکان اجرای فرمان‌ها روی کلاسترهای کوبرنتیز را فراهم می‌کند.
با kubectl می‌توانید برنامه‌ها را مستقر کنید، منابع کلاستر را بررسی و مدیریت کنید و لاگ‌ها را مشاهده کنید. برای اطلاعات بیشتر، از جمله فهرست کامل عملیات kubectl، [مستندات مرجع `kubectl`](/docs/reference/kubectl/) را ببینید.

ابزار kubectl را می‌توان روی انواع پلتفرم‌های لینوکس، macOS و ویندوز نصب کرد.
سیستم‌عامل مورد نظر خود را در فهرست زیر پیدا کنید.

- [نصب kubectl روی لینوکس](/docs/tasks/tools/install-kubectl-linux)
- [نصب kubectl روی macOS](/docs/tasks/tools/install-kubectl-macos)
- [نصب kubectl روی ویندوز](/docs/tasks/tools/install-kubectl-windows)

## kind

ابزار [`kind`](https://kind.sigs.k8s.io/) به شما امکان می‌دهد کوبرنتیز را روی رایانهٔ محلی خود اجرا کنید. برای استفاده از این ابزار باید
[Docker](https://www.docker.com/) یا [Podman](https://podman.io/) را نصب کرده باشید.

صفحهٔ [شروع سریع](https://kind.sigs.k8s.io/docs/user/quick-start/) kind
کارهایی را که برای راه‌اندازی و شروع کار با kind لازم است به شما نشان می‌دهد.

<a class="btn btn-primary" href="https://kind.sigs.k8s.io/docs/user/quick-start/" role="button" aria-label="View kind Quick Start Guide">مشاهدهٔ راهنمای شروع سریع kind</a>

## minikube

ابزار [`minikube`](https://minikube.sigs.k8s.io/) نیز مانند `kind` امکان اجرای محلی کوبرنتیز را فراهم می‌کند. این ابزار یک کلاستر محلی کوبرنتیز را به‌صورت همه‌در‌یک یا چندنودی روی رایانهٔ شخصی شما (از جمله رایانه‌های ویندوز، macOS و لینوکس) اجرا می‌کند تا بتوانید کوبرنتیز را امتحان کنید یا از آن در کارهای روزمرهٔ توسعه بهره ببرید.

اگر تمرکزتان بر نصب این ابزار است، می‌توانید راهنمای رسمی
[شروع کنید!](https://minikube.sigs.k8s.io/docs/start/) را دنبال کنید.

<a class="btn btn-primary" href="https://minikube.sigs.k8s.io/docs/start/" role="button" aria-label="View minikube Get Started! Guide">مشاهدهٔ راهنمای «شروع کنید!» minikube</a>

پس از راه‌اندازی `minikube`، می‌توانید از آن برای
[اجرای یک برنامهٔ نمونه](/docs/tutorials/hello-minikube/) استفاده کنید.

## kubeadm

با ابزار {{< glossary_tooltip term_id="kubeadm" text="kubeadm" >}} می‌توانید کلاسترهای کوبرنتیز را ایجاد و مدیریت کنید.
این ابزار اقدامات لازم برای راه‌اندازی و اجرای یک کلاستر حداقلی، کارا و امن را به شیوه‌ای کاربرپسند انجام می‌دهد.

صفحهٔ [نصب kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) روش نصب kubeadm را به شما نشان می‌دهد.
پس از نصب، می‌توانید با آن [یک کلاستر ایجاد کنید](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/).

<a class="btn btn-primary" href="/docs/setup/production-environment/tools/kubeadm/install-kubeadm/" role="button" aria-label="View kubeadm Install Guide">مشاهدهٔ راهنمای نصب kubeadm</a>
