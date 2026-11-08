---
title: فازهای kubeadm upgrade
weight: 40
content_type: concept
---

## فاز kubeadm upgrade apply {#cmd-apply-phase}

با استفاده از فازهای `kubeadm upgrade apply` می‌توانید مراحل جداگانهٔ ارتقای اولیهٔ یک نود control plane را به‌انتخاب خود اجرا کنید.

{{< tabs name="tab-apply-phase" >}}
{{< tab name="phase" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase.md" />}}
{{< tab name="preflight" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_preflight.md" />}}
{{< tab name="control-plane" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_control-plane.md" />}}
{{< tab name="upload-config" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_upload-config.md" />}}
{{< tab name="kubelet-config" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_kubelet-config.md" />}}
{{< tab name="bootstrap-token" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_bootstrap-token.md" />}}
{{< tab name="addon" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_addon.md" />}}
{{< tab name="post-upgrade" include="generated/kubeadm_upgrade/kubeadm_upgrade_apply_phase_post-upgrade.md" />}}
{{< /tabs >}}

## فاز kubeadm upgrade node {#cmd-node-phase}

با استفاده از فازهای `kubeadm upgrade node` می‌توانید مراحل جداگانهٔ ارتقای نودهای control plane ثانویه یا نودهای کارگر را به‌انتخاب خود اجرا کنید.

{{< tabs name="tab-upgrade-phase" >}}
{{< tab name="phase" include="generated/kubeadm_upgrade/kubeadm_upgrade_node_phase.md" />}}
{{< tab name="preflight" include="generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_preflight.md" />}}
{{< tab name="control-plane" include="generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_control-plane.md" />}}
{{< tab name="kubelet-config" include="generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_kubelet-config.md" />}}
{{< tab name="addon" include="generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_addon.md" />}}
{{< tab name="post-upgrade" include="generated/kubeadm_upgrade/kubeadm_upgrade_node_phase_post-upgrade.md" />}}
{{< /tabs >}}

## {{% heading "whatsnext" %}}

* دستور [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) برای راه‌اندازی اولیهٔ یک نود control plane کوبرنتیز
* دستور [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) برای متصل کردن یک نود به کلاستر
* دستور [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) برای بازگرداندن تمام تغییراتی که `kubeadm init` یا `kubeadm join` روی این میزبان اعمال کرده‌اند
* دستور [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) برای ارتقای یک نود kubeadm
* دستور [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) برای آزمودن قابلیت‌های آزمایشی
