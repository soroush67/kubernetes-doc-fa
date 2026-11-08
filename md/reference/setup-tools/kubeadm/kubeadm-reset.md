---
reviewers:
- luxas
- jbeda
title: kubeadm reset
content_type: concept
weight: 60
---
<!-- overview -->
تغییراتی را که دستورهای `kubeadm init` یا `kubeadm join` ایجاد کرده‌اند، تا حد امکان برمی‌گرداند.

<!-- body -->
{{< include "generated/kubeadm_reset/_index.md" >}}

### گردش کار بازنشانی {#reset-workflow}

دستور `kubeadm reset` فایل‌هایی را که با دستورهای `kubeadm init` یا `kubeadm join` ایجاد شده‌اند، از فایل‌سیستم محلی نود پاک می‌کند. این دستور در نودهای control plane، عضو etcd محلی و پشته‌ای (stacked) همان نود را نیز از کلاستر etcd حذف می‌کند.

با `kubeadm reset phase` می‌توانید هر یک از مراحل این گردش کار را جداگانه اجرا کنید. برای رد شدن از فهرستی از مراحل نیز می‌توانید از فلگ `--skip-phases` استفاده کنید که عملکردی مشابه اجراکننده‌های مراحل در `kubeadm join` و `kubeadm init` دارد.

دستور `kubeadm reset` از فلگ `--config` نیز برای ارسال یک [ساختار `ResetConfiguration`](/docs/reference/config-api/kubeadm-config.v1beta4/) پشتیبانی می‌کند.

### پاک‌سازی اعضای etcd خارجی

اگر از etcd خارجی استفاده شود، `kubeadm reset` هیچ داده‌ای را از etcd حذف نمی‌کند. بنابراین اگر `kubeadm init` را دوباره با همان نقاط پایانی etcd اجرا کنید، وضعیت کلاسترهای قبلی را خواهید دید.

برای پاک کردن داده‌های etcd توصیه می‌شود از کلاینتی مانند etcdctl استفاده کنید؛ برای مثال:

```bash
etcdctl del "" --prefix
```

برای اطلاعات بیشتر، [مستندات etcd](https://github.com/coreos/etcd/tree/master/etcdctl) را ببینید.

### پاک‌سازی پیکربندی CNI

افزونه‌های CNI پیکربندی خود را در دایرکتوری `/etc/cni/net.d` ذخیره می‌کنند. دستور `kubeadm reset` این دایرکتوری را پاک نمی‌کند. اگر پیکربندی یک افزونه CNI روی میزبان باقی بماند و همان میزبان بعداً به‌عنوان نود جدید کوبرنتیز در کلاستری با افزونه CNI متفاوت به کار رود، ممکن است مشکل ایجاد شود و میان افزونه‌های CNI تداخل پیکربندی رخ دهد.

برای پاک‌سازی این دایرکتوری، در صورت نیاز از محتوای آن نسخه پشتیبان بگیرید و سپس دستور زیر را اجرا کنید:

```bash
sudo rm -rf /etc/cni/net.d
```

### پاک‌سازی قواعد ترافیک شبکه

دستور `kubeadm reset` هیچ‌یک از قواعد iptables، nftables یا IPVS را که kube-proxy روی میزبان اعمال کرده است، پاک نمی‌کند. یک حلقه کنترلی در kube-proxy همگام بودن این قواعد را در میزبان هر نود تضمین می‌کند. برای جزئیات بیشتر، [IPهای مجازی و پراکسی‌های Service](/docs/reference/networking/virtual-ips/) را ببینید.

اگر این قواعد پاک نشوند، استفاده دوباره از میزبان به‌عنوان نود کوبرنتیز یا به کار گرفتن آن برای هدفی دیگر نباید مشکلی ایجاد کند.

اگر می‌خواهید این پاک‌سازی را انجام دهید، می‌توانید از همان کانتینر kube-proxy که در کلاستر شما استفاده شده است و فلگ `--cleanup` در فایل اجرایی `kube-proxy` کمک بگیرید:

```bash
docker run --privileged --network=host -v /lib/modules:/lib/modules:ro --rm registry.k8s.io/kube-proxy:v{{< skew currentPatchVersion >}} sh -c "kube-proxy --cleanup && echo DONE"
```

خروجی دستور بالا باید در پایان عبارت `DONE` را چاپ کند. به‌جای Docker می‌توانید از محیط اجرای کانتینر دلخواه خود برای راه‌اندازی این کانتینر استفاده کنید.

### پاک‌سازی $HOME/.kube

دایرکتوری `$HOME/.kube` معمولاً شامل فایل‌های پیکربندی و حافظه نهان kubectl است. پاک نکردن محتوای `$HOME/.kube/cache` مشکلی ایجاد نمی‌کند، اما این دایرکتوری یک فایل مهم نیز دارد: فایل `$HOME/.kube/config` که kubectl از آن برای احراز هویت در سرور API کوبرنتیز استفاده می‌کند. پس از پایان `kubeadm init`، به کاربر گفته می‌شود که فایل `/etc/kubernetes/admin.conf` را در مسیر `$HOME/.kube/config` کپی کند و به کاربر فعلی اجازه دسترسی به آن را بدهد.

دستور `kubeadm reset` هیچ‌یک از محتویات دایرکتوری `$HOME/.kube` را پاک نمی‌کند. باقی ماندن فایل `$HOME/.kube/config` بسته به اینکه پس از اجرای `kubeadm reset` چه کسانی به این میزبان دسترسی داشته باشند، ممکن است مشکل‌ساز شود. اگر همان کلاستر همچنان وجود داشته باشد، اکیداً توصیه می‌شود این فایل را حذف کنید، زیرا اعتبارنامه‌های مدیر که در آن ذخیره شده‌اند همچنان معتبر خواهند ماند.

برای پاک‌سازی این دایرکتوری، محتوای آن را بررسی کنید، در صورت نیاز نسخه پشتیبان بگیرید و دستور زیر را اجرا کنید:

```bash
rm -rf $HOME/.kube
```

### خاموش کردن تدریجی و ایمن kube-apiserver

اگر `kube-apiserver` را با فلگ `--shutdown-delay-duration` پیکربندی کرده‌اید، می‌توانید پیش از اجرای `kubeadm reset`، با دستورهای زیر تلاش کنید Pod سرور API در حال اجرا به‌صورت تدریجی و ایمن خاموش شود:

```bash
yq eval -i '.spec.containers[0].command = []' /etc/kubernetes/manifests/kube-apiserver.yaml
timeout 60 sh -c 'while pgrep kube-apiserver >/dev/null; do sleep 1; done' || true
```

## {{% heading "whatsnext" %}}

* برای راه‌اندازی اولیه یک نود control plane کوبرنتیز، [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) را ببینید.
* برای راه‌اندازی اولیه یک نود کارگر کوبرنتیز و پیوستن آن به کلاستر، [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) را ببینید.
