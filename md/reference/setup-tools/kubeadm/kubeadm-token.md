---
reviewers:
- luxas
- jbeda
title: kubeadm token
content_type: concept
weight: 70
---
<!-- overview -->

توکن‌های راه‌اندازی اولیه (Bootstrap tokens) برای برقراری اعتماد دوطرفه میان نودی که به کلاستر می‌پیوندد و یک نود control plane به کار می‌روند؛ این فرایند در [احراز هویت با توکن‌های راه‌اندازی اولیه](/docs/reference/access-authn-authz/bootstrap-tokens/) شرح داده شده است.

دستور `kubeadm init` یک توکن اولیه با طول عمر (TTL) ۲۴ ساعته می‌سازد. با دستورهای زیر می‌توانید این توکن را مدیریت کنید و همچنین توکن‌های جدیدی بسازید و آن‌ها را مدیریت کنید.

<!-- body -->
## kubeadm token create {#cmd-token-create}
{{< include "generated/kubeadm_token/kubeadm_token_create.md" >}}

## kubeadm token delete {#cmd-token-delete}
{{< include "generated/kubeadm_token/kubeadm_token_delete.md" >}}

## kubeadm token generate {#cmd-token-generate}
{{< include "generated/kubeadm_token/kubeadm_token_generate.md" >}}

## kubeadm token list {#cmd-token-list}
{{< include "generated/kubeadm_token/kubeadm_token_list.md" >}}

## {{% heading "whatsnext" %}}

* دستور [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) برای راه‌اندازی اولیه یک نود کارگر کوبرنتیز و پیوستن آن به کلاستر
