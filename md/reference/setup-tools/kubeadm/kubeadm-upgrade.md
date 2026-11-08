---
reviewers:
- luxas
- jbeda
title: kubeadm upgrade
content_type: concept
weight: 40
---
<!-- overview -->
دستور `kubeadm upgrade` دستوری کاربرپسند است که منطق پیچیدهٔ ارتقا را در قالب یک دستور واحد ارائه می‌کند و هم برنامه‌ریزی ارتقا و هم اجرای واقعی آن را پشتیبانی می‌کند.


<!-- body -->

## راهنمای kubeadm upgrade

مراحل انجام ارتقا با kubeadm در [این سند](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) شرح داده شده است.
برای نسخه‌های قدیمی‌تر kubeadm، به مجموعه‌مستندات قدیمی‌تر وب‌سایت کوبرنتیز مراجعه کنید.

با دستور `kubeadm upgrade diff` می‌توانید تغییراتی را که روی مانیفست‌های Pod ایستا اعمال خواهند شد، مشاهده کنید.

در کوبرنتیز نسخهٔ v1.15.0 و بالاتر، دستورهای `kubeadm upgrade apply` و `kubeadm upgrade node` گواهی‌های تحت مدیریت kubeadm را روی همان نود، از جمله گواهی‌های ذخیره‌شده در فایل‌های kubeconfig، به‌طور خودکار تمدید نیز می‌کنند.
برای غیرفعال‌کردن این رفتار می‌توانید فلگ `--certificate-renewal=false` را به دستور بدهید. برای جزئیات بیشتر دربارهٔ تمدید گواهی‌ها، به [مستندات مدیریت گواهی‌ها](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs) مراجعه کنید.

{{< note >}}
دستورهای `kubeadm upgrade apply` و `kubeadm upgrade plan` یک فلگ قدیمی `--config` دارند که با آن می‌توان هنگام برنامه‌ریزی یا ارتقای یک نود control plane مشخص، کلاستر را دوباره پیکربندی کرد. توجه داشته باشید که فرایند ارتقا برای این سناریو طراحی نشده است و گزارش‌هایی از نتایج غیرمنتظره در این زمینه وجود دارد.
{{</ note >}}

## kubeadm upgrade plan {#cmd-upgrade-plan}
{{< include "generated/kubeadm_upgrade/kubeadm_upgrade_plan.md" >}}

## kubeadm upgrade apply  {#cmd-upgrade-apply}
{{< include "generated/kubeadm_upgrade/kubeadm_upgrade_apply.md" >}}

## kubeadm upgrade diff {#cmd-upgrade-diff}
{{< include "generated/kubeadm_upgrade/kubeadm_upgrade_diff.md" >}}

## kubeadm upgrade node {#cmd-upgrade-node}
{{< include "generated/kubeadm_upgrade/kubeadm_upgrade_node.md" >}}


## {{% heading "whatsnext" %}}

* اگر کلاستر خود را با kubeadm نسخهٔ v1.7.x یا پایین‌تر راه‌اندازی کرده‌اید، برای پیکربندی آن جهت استفاده از `kubeadm upgrade` به [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/) مراجعه کنید.
