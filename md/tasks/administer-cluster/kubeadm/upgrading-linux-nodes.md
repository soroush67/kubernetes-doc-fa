---
title: ارتقای نودهای لینوکسی
content_type: task
weight: 40
---

<!-- overview -->

این صفحه نحوهٔ ارتقای نودهای کارگر (Worker Nodes) لینوکسیِ ایجادشده با kubeadm را توضیح می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs-node-upgrade.md" >}} {{< version-check >}}
* با [فرایند ارتقای بقیهٔ کلاستر kubeadm خود](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade) آشنا شوید. لازم است پیش از ارتقای نودهای کارگر لینوکسی، نودهای control plane را ارتقا دهید.

<!-- steps -->

## تغییر مخزن بسته‌ها

اگر از مخازن بستهٔ متعلق به جامعه (`pkgs.k8s.io`) استفاده می‌کنید، باید مخزن بستهٔ مربوط به نسخهٔ فرعی (minor) موردنظر کوبرنتیز را فعال کنید. این کار در سند
[تغییر مخزن بستهٔ کوبرنتیز](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
توضیح داده شده است.

{{% legacy-repos-deprecation %}}

## ارتقای نودهای کارگر

### ارتقای kubeadm و kubectl

ابزارهای kubeadm و kubectl را ارتقا دهید:

{{< note >}}
طبق [سیاست اختلاف نسخه](/releases/version-skew-policy/#kubectl)، نسخهٔ kubectl باید حداکثر یک نسخهٔ فرعی با kube-apiserver فاصله داشته باشد.
اگر پیش از ارتقای نودهای کارگر، control plane را چند نسخهٔ فرعی ارتقا می‌دهید، ممکن است kubectl محلیِ نود از محدودهٔ اختلاف مجاز خارج شود. ارتقای هم‌زمان kubectl و kubeadm در این مرحله تضمین می‌کند که kubectl در تمام طول فرایند ارتقای نود در محدودهٔ نسخه‌های پشتیبانی‌شده باقی بماند.
{{< /note >}}

{{< tabs name="k8s_install_kubeadm_worker_nodes" >}}
{{% tab name="Ubuntu، Debian یا HypriotOS" %}}
```shell
# replace x in {{< skew currentVersion >}}.x-* with the latest patch version
sudo apt-mark unhold kubeadm kubectl && \
sudo apt-get update && sudo apt-get install -y kubeadm='{{< skew currentVersion >}}.x-*' kubectl='{{< skew currentVersion >}}.x-*' && \
sudo apt-mark hold kubeadm kubectl
```
{{% /tab %}}
{{% tab name="CentOS، RHEL یا Fedora" %}}
برای سیستم‌های دارای DNF4 (Fedora < 41، RHEL/Centos < 10):
```shell
# replace x in {{< skew currentVersion >}}.x-* with the latest patch version
sudo dnf install -y kubeadm-'{{< skew currentVersion >}}.x-*' kubectl-'{{< skew currentVersion >}}.x-*' --disableexcludes=kubernetes
```
برای سیستم‌های دارای DNF5:
```shell
# replace x in {{< skew currentVersion >}}.x-* with the latest patch version
sudo dnf install -y kubeadm-'{{< skew currentVersion >}}.x-*' kubectl-'{{< skew currentVersion >}}.x-*' --setopt=disable_excludes=kubernetes
```
{{% /tab %}}
{{< /tabs >}}

### اجرای «kubeadm upgrade»

در نودهای کارگر، این دستور پیکربندی محلی kubelet را ارتقا می‌دهد:

```shell
sudo kubeadm upgrade node
```

### تخلیهٔ نود

نود را با علامت‌گذاری به‌عنوان غیرقابل‌زمان‌بندی و بیرون‌راندن بارهای کاری، برای نگهداری آماده کنید:

```shell
# execute this command on a control plane node
# replace <node-to-drain> with the name of your node you are draining
kubectl drain <node-to-drain> --ignore-daemonsets
```

### ارتقای kubelet

1. ابزار kubelet را ارتقا دهید:

   {{< tabs name="k8s_kubelet_and_kubectl" >}}
   {{% tab name="Ubuntu، Debian یا HypriotOS" %}}
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo apt-mark unhold kubelet && \
   sudo apt-get update && sudo apt-get install -y kubelet='{{< skew currentVersion >}}.x-*' && \
   sudo apt-mark hold kubelet
   ```
   {{% /tab %}}
   {{% tab name="CentOS، RHEL یا Fedora" %}}
   برای سیستم‌های دارای DNF4 (Fedora < 41، RHEL/CentOS < 10):
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo dnf install -y kubelet-'{{< skew currentVersion >}}.x-*' --disableexcludes=kubernetes
   ```
   برای سیستم‌های دارای DNF5:
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo dnf install -y kubelet-'{{< skew currentVersion >}}.x-*' --setopt=disable_excludes=kubernetes
   ```
   {{% /tab %}}
   {{< /tabs >}}

1. ابزار kubelet را مجدداً راه‌اندازی کنید:

   ```shell
   sudo systemctl daemon-reload
   sudo systemctl restart kubelet
   ```

### خارج‌کردن نود از حالت cordon

نود را با علامت‌گذاری به‌عنوان قابل‌زمان‌بندی، دوباره به چرخهٔ کار برگردانید:

```shell
# execute this command on a control plane node
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```

## {{% heading "whatsnext" %}}

* نحوهٔ [ارتقای نودهای ویندوزی](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/) را ببینید.
