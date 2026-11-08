---
title: دستور kubeadm join phase
weight: 90
content_type: concept
---

با دستور `kubeadm join phase` می‌توانید هر یک از گام‌های تجزیه‌ناپذیر فرایند پیوستن به کلاستر را جداگانه اجرا کنید. به این ترتیب، اگر بخواهید سفارشی‌سازی خاصی اعمال کنید، می‌توانید بخشی از کار را به kubeadm بسپارید و بقیه را خودتان تکمیل کنید.

دستور `kubeadm join phase` با [گردش کار kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/#join-workflow) سازگار است و هر دو در پشت صحنه از کد یکسانی استفاده می‌کنند.

## دستور kubeadm join phase {#cmd-join-phase}

{{< tabs name="tab-phase" >}}
{{< tab name="phase" include="generated/kubeadm_join/kubeadm_join_phase.md" />}}
{{< /tabs >}}

## دستور kubeadm join phase preflight {#cmd-join-phase-preflight}

با این مرحله می‌توانید بررسی‌های پیش از اجرا را روی نودی که در حال پیوستن به کلاستر است انجام دهید.

{{< tabs name="tab-preflight" >}}
{{< tab name="preflight" include="generated/kubeadm_join/kubeadm_join_phase_preflight.md" />}}
{{< /tabs >}}

## دستور kubeadm join phase control-plane-prepare {#cmd-join-phase-control-plane-prepare}

با این مرحله می‌توانید یک نود را برای میزبانی control plane آماده کنید.

{{< tabs name="tab-control-plane-prepare" >}}
{{< tab name="control-plane-prepare" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare.md" />}}
{{< tab name="all" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_all.md" />}}
{{< tab name="download-certs" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_download-certs.md" />}}
{{< tab name="certs" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_certs.md" />}}
{{< tab name="kubeconfig" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_kubeconfig.md" />}}
{{< tab name="control-plane" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-prepare_control-plane.md" />}}
{{< /tabs >}}

## دستور kubeadm join phase kubelet-start {#cmd-join-phase-kubelet-start}

با این مرحله می‌توانید تنظیمات و گواهی‌های kubelet را بنویسید و kubelet را راه‌اندازی یا دوباره راه‌اندازی کنید.

{{< tabs name="tab-kubelet-start" >}}
{{< tab name="kubelet-start" include="generated/kubeadm_join/kubeadm_join_phase_kubelet-start.md" />}}
{{< /tabs >}}

## دستور kubeadm join phase etcd-join {#cmd-join-phase-etcd-join}

عضو جدید etcd را به کلاستر etcd اضافه کنید.

{{< tabs name="tab-etcd-join" >}}
{{< tab name="etcd-join" include="generated/kubeadm_join/kubeadm_join_phase_etcd-join.md" />}}
{{< /tabs >}}

## دستور kubeadm join phase control-plane-join {#cmd-join-phase-control-plane-join}

با این مرحله می‌توانید یک نود را به‌عنوان نمونه‌ای از control plane به کلاستر بپیوندانید.

{{< tabs name="tab-control-plane-join" >}}
{{< tab name="control-plane-join" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-join.md" />}}
{{< tab name="all" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-join_all.md" />}}
{{< tab name="mark-control-plane" include="generated/kubeadm_join/kubeadm_join_phase_control-plane-join_mark-control-plane.md" />}}
{{< /tabs >}}

## دستور kubeadm join phase wait-control-plane {#cmd-join-wait-control-plane}

منتظر بمانید تا مؤلفه‌های control plane راه‌اندازی شوند.

{{< tabs name="tab-wait-control-plane" >}}
{{< tab name="wait-control-plane" include="generated/kubeadm_join/kubeadm_join_phase_wait-control-plane.md" />}}
{{< /tabs >}}

## {{% heading "whatsnext" %}}

* دستور [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) برای راه‌اندازی اولیه یک نود control plane در کوبرنتیز
* دستور [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) برای متصل کردن یک نود به کلاستر
* دستور [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) برای بازگرداندن هر تغییری که `kubeadm init` یا `kubeadm join` روی این میزبان ایجاد کرده است
* دستور [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) برای آزمودن قابلیت‌های آزمایشی
