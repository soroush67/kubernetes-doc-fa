---
reviewers:
- luxas
- jbeda
title: فرمان kubeadm config
content_type: concept
weight: 50
---

<!-- overview -->
هنگام اجرای `kubeadm init`، ابزار kubeadm آبجکت `ClusterConfiguration` را در قالب یک ConfigMap با نام `kubeadm-config` در فضای نام (namespace) `kube-system` در کلاستر شما بارگذاری می‌کند. این پیکربندی سپس هنگام اجرای `kubeadm join`، `kubeadm reset` و `kubeadm upgrade` خوانده می‌شود.

با فرمان `kubeadm config print` می‌توانید پیکربندی ایستای پیش‌فرضی را که kubeadm برای `kubeadm init` و `kubeadm join` به کار می‌برد چاپ کنید.

{{< note >}}
خروجی این فرمان فقط نقش یک نمونه را دارد و باید آن را به‌صورت دستی ویرایش کنید تا با محیط شما سازگار شود. فیلدهایی را که از مقدارشان مطمئن نیستید حذف کنید تا kubeadm در زمان اجرا با بررسی میزبان، مقدار پیش‌فرض آن‌ها را تعیین کند.
{{< /note >}}

برای اطلاعات بیشتر درباره `init` و `join` به [استفاده از kubeadm init با فایل پیکربندی](/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file) یا [استفاده از kubeadm join با فایل پیکربندی](/docs/reference/setup-tools/kubeadm/kubeadm-join/#config-file) مراجعه کنید.

برای اطلاعات بیشتر درباره استفاده از API پیکربندی kubeadm به [سفارشی‌سازی مؤلفه‌ها با API ابزار kubeadm](/docs/setup/production-environment/tools/kubeadm/control-plane-flags) مراجعه کنید.

با فرمان `kubeadm config migrate` می‌توانید فایل‌های پیکربندی قدیمی خود را که از یک نسخه منسوخ API استفاده می‌کنند به نسخه‌ای جدیدتر و پشتیبانی‌شده از API تبدیل کنید.

برای اعتبارسنجی یک فایل پیکربندی می‌توانید از `kubeadm config validate` استفاده کنید.

برای فهرست کردن و دریافت ایمیج‌های موردنیاز kubeadm می‌توانید از `kubeadm config images list` و `kubeadm config images pull` استفاده کنید.

<!-- body -->
## فرمان kubeadm config print {#cmd-config-print}

{{< include "generated/kubeadm_config/kubeadm_config_print.md" >}}

## فرمان kubeadm config print init-defaults {#cmd-config-print-init-defaults}

{{< include "generated/kubeadm_config/kubeadm_config_print_init-defaults.md" >}}

## فرمان kubeadm config print join-defaults {#cmd-config-print-join-defaults}

{{< include "generated/kubeadm_config/kubeadm_config_print_join-defaults.md" >}}

## فرمان kubeadm config migrate {#cmd-config-migrate}

{{< include "generated/kubeadm_config/kubeadm_config_migrate.md" >}}

## فرمان kubeadm config validate {#cmd-config-validate}

{{< include "generated/kubeadm_config/kubeadm_config_validate.md" >}}

## فرمان kubeadm config images list {#cmd-config-images-list}

{{< include "generated/kubeadm_config/kubeadm_config_images_list.md" >}}

## فرمان kubeadm config images pull {#cmd-config-images-pull}

{{< include "generated/kubeadm_config/kubeadm_config_images_pull.md" >}}

## {{% heading "whatsnext" %}}

* [فرمان kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/) برای ارتقای یک کلاستر کوبرنتیز به نسخه‌ای جدیدتر
