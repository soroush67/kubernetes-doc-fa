---
title: فرمان kubeadm init phase
weight: 90
content_type: concept
---

فرمان `kubeadm init phase` امکان اجرای جداگانهٔ هر یک از گام‌های تجزیه‌ناپذیر فرایند راه‌اندازی اولیه (bootstrap) را فراهم می‌کند. به این ترتیب می‌توانید بخشی از کار را به kubeadm بسپارید و اگر به سفارشی‌سازی نیاز دارید، بخش‌های باقی‌مانده را خودتان انجام دهید.

این فرمان با [گردش کار kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/#init-workflow) سازگار است و هر دو در پشت صحنه از کد یکسانی استفاده می‌کنند.

## فرمان kubeadm init phase preflight {#cmd-phase-preflight}

با این فرمان می‌توانید بررسی‌های پیش از اجرا (preflight) را روی یک نود control plane انجام دهید.

{{< tabs name="tab-preflight" >}}
{{< tab name="preflight" include="generated/kubeadm_init/kubeadm_init_phase_preflight.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase certs {#cmd-phase-certs}

با این فرمان می‌توان همهٔ گواهی‌های موردنیاز kubeadm را ایجاد کرد.

{{< tabs name="tab-certs" >}}
{{< tab name="certs" include="generated/kubeadm_init/kubeadm_init_phase_certs.md" />}}
{{< tab name="all" include="generated/kubeadm_init/kubeadm_init_phase_certs_all.md" />}}
{{< tab name="ca" include="generated/kubeadm_init/kubeadm_init_phase_certs_ca.md" />}}
{{< tab name="apiserver" include="generated/kubeadm_init/kubeadm_init_phase_certs_apiserver.md" />}}
{{< tab name="apiserver-kubelet-client" include="generated/kubeadm_init/kubeadm_init_phase_certs_apiserver-kubelet-client.md" />}}
{{< tab name="front-proxy-ca" include="generated/kubeadm_init/kubeadm_init_phase_certs_front-proxy-ca.md" />}}
{{< tab name="front-proxy-client" include="generated/kubeadm_init/kubeadm_init_phase_certs_front-proxy-client.md" />}}
{{< tab name="etcd-ca" include="generated/kubeadm_init/kubeadm_init_phase_certs_etcd-ca.md" />}}
{{< tab name="etcd-server" include="generated/kubeadm_init/kubeadm_init_phase_certs_etcd-server.md" />}}
{{< tab name="etcd-peer" include="generated/kubeadm_init/kubeadm_init_phase_certs_etcd-peer.md" />}}
{{< tab name="healthcheck-client" include="generated/kubeadm_init/kubeadm_init_phase_certs_etcd-healthcheck-client.md" />}}
{{< tab name="apiserver-etcd-client" include="generated/kubeadm_init/kubeadm_init_phase_certs_apiserver-etcd-client.md" />}}
{{< tab name="sa" include="generated/kubeadm_init/kubeadm_init_phase_certs_sa.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase kubeconfig {#cmd-phase-kubeconfig}

می‌توانید همهٔ فایل‌های kubeconfig موردنیاز را با فراخوانی زیرفرمان `all` ایجاد کنید یا هر یک را جداگانه بسازید.

{{< tabs name="tab-kubeconfig" >}}
{{< tab name="kubeconfig" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig.md" />}}
{{< tab name="all" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig_all.md" />}}
{{< tab name="admin" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig_admin.md" />}}
{{< tab name="kubelet" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig_kubelet.md" />}}
{{< tab name="controller-manager" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig_controller-manager.md" />}}
{{< tab name="scheduler" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig_scheduler.md" />}}
{{< tab name="super-admin" include="generated/kubeadm_init/kubeadm_init_phase_kubeconfig_super-admin.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase etcd {#cmd-phase-etcd}

برای ایجاد یک نمونهٔ محلی etcd بر پایهٔ یک فایل Pod ایستا (static Pod)، از مرحلهٔ زیر استفاده کنید.

{{< tabs name="tab-etcd" >}}
{{< tab name="etcd" include="generated/kubeadm_init/kubeadm_init_phase_etcd.md" />}}
{{< tab name="local" include="generated/kubeadm_init/kubeadm_init_phase_etcd_local.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase control-plane {#cmd-phase-control-plane}

با این مرحله می‌توانید همهٔ فایل‌های Pod ایستای موردنیاز مؤلفه‌های control plane را ایجاد کنید.

{{< tabs name="tab-control-plane" >}}
{{< tab name="control-plane" include="generated/kubeadm_init/kubeadm_init_phase_control-plane.md" />}}
{{< tab name="all" include="generated/kubeadm_init/kubeadm_init_phase_control-plane_all.md" />}}
{{< tab name="apiserver" include="generated/kubeadm_init/kubeadm_init_phase_control-plane_apiserver.md" />}}
{{< tab name="controller-manager" include="generated/kubeadm_init/kubeadm_init_phase_control-plane_controller-manager.md" />}}
{{< tab name="scheduler" include="generated/kubeadm_init/kubeadm_init_phase_control-plane_scheduler.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase kubelet-start {#cmd-phase-kubelet-start}

این مرحله فایل پیکربندی و فایل محیطی kubelet را می‌نویسد و سپس kubelet را راه‌اندازی می‌کند.

{{< tabs name="tab-kubelet-start" >}}
{{< tab name="kubelet-start" include="generated/kubeadm_init/kubeadm_init_phase_kubelet-start.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase wait-control-plane {#cmd-phase-wait-control-plane}

در این مرحله، kubeadm تا راه‌اندازی مؤلفه‌های control plane منتظر می‌ماند.

{{< tabs name="tab-wait-control-plane" >}}
{{< tab name="wait-control-plane" include="generated/kubeadm_init/kubeadm_init_phase_wait-control-plane.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase upload-config {#cmd-phase-upload-config}

با این فرمان می‌توانید پیکربندی kubeadm را در کلاستر خود بارگذاری کنید. همچنین می‌توانید به‌جای آن از [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/) استفاده کنید.

{{< tabs name="upload-config" >}}
{{< tab name="upload-config" include="generated/kubeadm_init/kubeadm_init_phase_upload-config.md" />}}
{{< tab name="all" include="generated/kubeadm_init/kubeadm_init_phase_upload-config_all.md" />}}
{{< tab name="kubeadm" include="generated/kubeadm_init/kubeadm_init_phase_upload-config_kubeadm.md" />}}
{{< tab name="kubelet" include="generated/kubeadm_init/kubeadm_init_phase_upload-config_kubelet.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase upload-certs {#cmd-phase-upload-certs}

برای بارگذاری گواهی‌های control plane در کلاستر، از مرحلهٔ زیر استفاده کنید. گواهی‌ها و کلید رمزنگاری به‌طور پیش‌فرض پس از دو ساعت منقضی می‌شوند.

{{< tabs name="tab-upload-certs" >}}
{{< tab name="upload-certs" include="generated/kubeadm_init/kubeadm_init_phase_upload-certs.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase mark-control-plane {#cmd-phase-mark-control-plane}

برای افزودن برچسب و taint به نود و مشخص‌کردن آن به‌عنوان نود control plane، از مرحلهٔ زیر استفاده کنید.

{{< tabs name="tab-mark-control-plane" >}}
{{< tab name="mark-control-plane" include="generated/kubeadm_init/kubeadm_init_phase_mark-control-plane.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase bootstrap-token {#cmd-phase-bootstrap-token}

برای پیکربندی توکن‌های راه‌اندازی اولیه، از مرحلهٔ زیر استفاده کنید.

{{< tabs name="tab-bootstrap-token" >}}
{{< tab name="bootstrap-token" include="generated/kubeadm_init/kubeadm_init_phase_bootstrap-token.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase kubelet-finalize {#cmd-phase-kubelet-finalize-all}

برای به‌روزرسانی تنظیمات مربوط به kubelet پس از راه‌اندازی اولیهٔ TLS، از مرحلهٔ زیر استفاده کنید. با زیرفرمان `all` می‌توانید همهٔ مراحل `kubelet-finalize` را اجرا کنید.

{{< tabs name="tab-kubelet-finalize" >}}
{{< tab name="kubelet-finalize" include="generated/kubeadm_init/kubeadm_init_phase_kubelet-finalize.md" />}}
{{< tab name="kubelet-finalize-all" include="generated/kubeadm_init/kubeadm_init_phase_kubelet-finalize_all.md" />}}
{{< tab name="kubelet-finalize-enable-client-cert-rotation" include="generated/kubeadm_init/kubeadm_init_phase_kubelet-finalize_enable-client-cert-rotation.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase bootstrap-token {#cmd-phase-bootstrap-token}

برای پیکربندی توکن‌های راه‌اندازی اولیه، از مرحلهٔ زیر استفاده کنید.

{{< tabs name="tab-bootstrap-token" >}}
{{< tab name="bootstrap-token" include="generated/kubeadm_init/kubeadm_init_phase_bootstrap-token.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase addon {#cmd-phase-addon}

می‌توانید همهٔ افزونه‌های موجود را با زیرفرمان `all` نصب کنید یا فقط افزونه‌های دلخواه خود را به‌صورت انتخابی نصب کنید.

{{< tabs name="tab-addon" >}}
{{< tab name="addon" include="generated/kubeadm_init/kubeadm_init_phase_addon.md" />}}
{{< tab name="all" include="generated/kubeadm_init/kubeadm_init_phase_addon_all.md" />}}
{{< tab name="coredns" include="generated/kubeadm_init/kubeadm_init_phase_addon_coredns.md" />}}
{{< tab name="kube-proxy" include="generated/kubeadm_init/kubeadm_init_phase_addon_kube-proxy.md" />}}
{{< /tabs >}}

## فرمان kubeadm init phase show-join-command {#cmd-phase-show-join-command}

این فرمان، دستوری را نمایش می‌دهد که می‌توان آن را با `kubeadm join` به کار برد.

{{< tabs name="tab-show-join-command" >}}
{{< tab name="show-join-command" include="generated/kubeadm_init/kubeadm_init_phase_show-join-command.md" />}}
{{< /tabs >}}

برای دیدن جزئیات بیشتر دربارهٔ هر فیلد در پیکربندی `v1beta4` می‌توانید به [صفحه‌های مرجع API](/docs/reference/config-api/kubeadm-config.v1beta4/) مراجعه کنید.

## {{% heading "whatsnext" %}}

* فرمان [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) برای راه‌اندازی اولیهٔ یک نود control plane کوبرنتیز
* فرمان [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) برای اتصال یک نود به کلاستر
* فرمان [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) برای بازگرداندن همهٔ تغییراتی که `kubeadm init` یا `kubeadm join` روی این میزبان اعمال کرده‌اند
* فرمان [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) برای آزمودن قابلیت‌های آزمایشی
