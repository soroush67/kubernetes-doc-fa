---
title: فاز kubeadm reset
weight: 90
content_type: concept
---

دستور `kubeadm reset phase` امکان اجرای مرحله‌های مجزای فرایند بازنشانی نود را فراهم می‌کند. به این ترتیب می‌توانید بخشی از کار را به kubeadm بسپارید و اگر به سفارشی‌سازی نیاز دارید، بقیهٔ کار را خودتان انجام دهید.

دستور `kubeadm reset phase` با [گردش کار kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/#reset-workflow) سازگار است و هر دو در پشت صحنه از کد یکسانی استفاده می‌کنند.

## دستور فاز kubeadm reset {#cmd-reset-phase}

{{< tabs name="tab-phase" >}}
{{< tab name="phase" include="generated/kubeadm_reset/kubeadm_reset_phase.md" />}}
{{< /tabs >}}

## فاز preflight در kubeadm reset {#cmd-reset-phase-preflight}

با این فاز می‌توانید بررسی‌های پیش از اجرا را روی نودی که در حال بازنشانی است انجام دهید.

{{< tabs name="tab-preflight" >}}
{{< tab name="preflight" include="generated/kubeadm_reset/kubeadm_reset_phase_preflight.md" />}}
{{< /tabs >}}

## فاز remove-etcd-member در kubeadm reset {#cmd-reset-phase-remove-etcd-member}

با این فاز می‌توانید عضو etcd مربوط به این نود control plane را از کلاستر etcd حذف کنید.

{{< tabs name="tab-remove-etcd-member" >}}
{{< tab name="remove-etcd-member" include="generated/kubeadm_reset/kubeadm_reset_phase_remove-etcd-member.md" />}}
{{< /tabs >}}

## فاز cleanup-node در kubeadm reset {#cmd-reset-phase-cleanup-node}

با این فاز می‌توانید عملیات پاک‌سازی را روی این نود انجام دهید.

{{< tabs name="tab-cleanup-node" >}}
{{< tab name="cleanup-node" include="generated/kubeadm_reset/kubeadm_reset_phase_cleanup-node.md" />}}
{{< /tabs >}}

## {{% heading "whatsnext" %}}

* دستور [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) برای راه‌اندازی اولیهٔ یک نود control plane در کوبرنتیز
* دستور [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) برای متصل کردن یک نود به کلاستر
* دستور [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) برای بازگرداندن هر تغییری که `kubeadm init` یا `kubeadm join` روی این میزبان ایجاد کرده است
* دستور [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) برای آزمودن قابلیت‌های آزمایشی
