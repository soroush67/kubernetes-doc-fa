---
title: kubeadm certs
content_type: concept
weight: 90
---

دستور `kubeadm certs` ابزارهایی برای مدیریت گواهی‌ها فراهم می‌کند. برای آشنایی بیشتر با نحوه استفاده از این دستورها، به [مدیریت گواهی‌ها با kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/) مراجعه کنید.

## دستور kubeadm certs {#cmd-certs}

این دستور مجموعه‌ای از عملیات را برای کار با گواهی‌های کوبرنتیز در اختیار شما می‌گذارد.

{{< tabs name="tab-certs" >}}
{{< tab name="نمای کلی" include="generated/kubeadm_certs/_index.md" />}}
{{< /tabs >}}

## دستور kubeadm certs renew {#cmd-certs-renew}

می‌توانید با زیردستور `all` همه گواهی‌های کوبرنتیز را تمدید کنید یا آن‌ها را به‌صورت انتخابی تمدید کنید. برای جزئیات بیشتر، به [تمدید دستی گواهی‌ها](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#manual-certificate-renewal) مراجعه کنید.

{{< tabs name="tab-certs-renew" >}}
{{< tab name="renew" include="generated/kubeadm_certs/kubeadm_certs_renew.md" />}}
{{< tab name="all" include="generated/kubeadm_certs/kubeadm_certs_renew_all.md" />}}
{{< tab name="admin.conf" include="generated/kubeadm_certs/kubeadm_certs_renew_admin.conf.md" />}}
{{< tab name="apiserver-etcd-client" include="generated/kubeadm_certs/kubeadm_certs_renew_apiserver-etcd-client.md" />}}
{{< tab name="apiserver-kubelet-client" include="generated/kubeadm_certs/kubeadm_certs_renew_apiserver-kubelet-client.md" />}}
{{< tab name="apiserver" include="generated/kubeadm_certs/kubeadm_certs_renew_apiserver.md" />}}
{{< tab name="controller-manager.conf" include="generated/kubeadm_certs/kubeadm_certs_renew_controller-manager.conf.md" />}}
{{< tab name="etcd-healthcheck-client" include="generated/kubeadm_certs/kubeadm_certs_renew_etcd-healthcheck-client.md" />}}
{{< tab name="etcd-peer" include="generated/kubeadm_certs/kubeadm_certs_renew_etcd-peer.md" />}}
{{< tab name="etcd-server" include="generated/kubeadm_certs/kubeadm_certs_renew_etcd-server.md" />}}
{{< tab name="front-proxy-client" include="generated/kubeadm_certs/kubeadm_certs_renew_front-proxy-client.md" />}}
{{< tab name="scheduler.conf" include="generated/kubeadm_certs/kubeadm_certs_renew_scheduler.conf.md" />}}
{{< tab name="super-admin.conf" include="generated/kubeadm_certs/kubeadm_certs_renew_super-admin.conf.md" />}}
{{< /tabs >}}

## دستور kubeadm certs certificate-key {#cmd-certs-certificate-key}

با این دستور می‌توانید یک کلید گواهی جدید برای control plane تولید کنید. این کلید را می‌توان با فلگ `--certificate-key` به [`kubeadm init`](/docs/reference/setup-tools/kubeadm/kubeadm-init) و [`kubeadm join`](/docs/reference/setup-tools/kubeadm/kubeadm-join) داد تا هنگام پیوستن نودهای control plane دیگر، گواهی‌ها به‌طور خودکار کپی شوند.

{{< tabs name="tab-certs-certificate-key" >}}
{{< tab name="certificate-key" include="generated/kubeadm_certs/kubeadm_certs_certificate-key.md" />}}
{{< /tabs >}}

## دستور kubeadm certs check-expiration {#cmd-certs-check-expiration}

این دستور تاریخ انقضای گواهی‌های موجود در PKI محلی را که kubeadm مدیریت می‌کند بررسی می‌کند. برای جزئیات بیشتر، به [بررسی انقضای گواهی‌ها](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#check-certificate-expiration) مراجعه کنید.

{{< tabs name="tab-certs-check-expiration" >}}
{{< tab name="check-expiration" include="generated/kubeadm_certs/kubeadm_certs_check-expiration.md" />}}
{{< /tabs >}}

## دستور kubeadm certs generate-csr {#cmd-certs-generate-csr}

با این دستور می‌توانید برای همه گواهی‌های control plane و فایل‌های kubeconfig، کلید و CSR تولید کنید. سپس کاربر می‌تواند CSRها را با CA دلخواه خود امضا کند. برای آشنایی بیشتر با نحوه استفاده از این دستور، به [امضای درخواست‌های امضای گواهی (CSR) تولیدشده با kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#signing-csr) مراجعه کنید.

{{< tabs name="tab-certs-generate-csr" >}}
{{< tab name="generate-csr" include="generated/kubeadm_certs/kubeadm_certs_generate-csr.md" />}}
{{< /tabs >}}

## {{% heading "whatsnext" %}}

* دستور [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) برای راه‌اندازی اولیه یک نود control plane کوبرنتیز
* دستور [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) برای متصل کردن یک نود به کلاستر
* دستور [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) برای بازگرداندن تغییراتی که `kubeadm init` یا `kubeadm join` روی این میزبان اعمال کرده‌اند
