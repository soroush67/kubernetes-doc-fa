---
title: "تغییر محیط اجرای کانتینر روی یک نود از Docker Engine به containerd"
weight: 10
content_type: task 
---

این راهنما مراحل لازم برای تغییر محیط اجرای کانتینر (container runtime) از Docker به containerd را شرح می‌دهد. این راهنما برای اپراتورهای کلاستری که کوبرنتیز نسخهٔ ۱.۲۳ یا قدیمی‌تر را اجرا می‌کنند کاربرد دارد. همچنین یک سناریوی نمونه برای مهاجرت از dockershim به containerd را پوشش می‌دهد. سایر محیط‌های اجرای کانتینر را می‌توانید از این [صفحه](/docs/setup/production-environment/container-runtimes/) انتخاب کنید.

## {{% heading "prerequisites" %}}

{{% thirdparty-content %}}

ابتدا containerd را نصب کنید. برای اطلاعات بیشتر به
[مستندات نصب containerd](https://containerd.io/docs/getting-started/)
مراجعه کنید و برای پیش‌نیازهای مشخص،
[راهنمای containerd](/docs/setup/production-environment/container-runtimes/#containerd) را دنبال کنید.

## تخلیهٔ نود

```shell
kubectl drain <node-to-drain> --ignore-daemonsets
```

به‌جای `<node-to-drain>` نام نودی را که تخلیه می‌کنید قرار دهید.

## متوقف کردن daemon داکر

```shell
systemctl stop kubelet
systemctl disable docker.service --now
```

## نصب Containerd

برای مشاهدهٔ مراحل دقیق نصب containerd، این [راهنما](/docs/setup/production-environment/container-runtimes/#containerd) را دنبال کنید.

{{< tabs name="tab-cri-containerd-installation" >}}
{{% tab name="Linux" %}}

1. بستهٔ `containerd.io` را از مخازن رسمی Docker نصب کنید.
   دستورالعمل‌های راه‌اندازی مخزن Docker برای توزیع لینوکس موردنظرتان و
   نصب بستهٔ `containerd.io` را می‌توانید در
   [Getting started with containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md) بیابید.

1. containerd را پیکربندی کنید:

   ```shell
   sudo mkdir -p /etc/containerd
   containerd config default | sudo tee /etc/containerd/config.toml
   ```
1. containerd را مجدداً راه‌اندازی کنید:

   ```shell
   sudo systemctl restart containerd
   ```
{{% /tab %}}
{{% tab name="Windows (PowerShell)" %}}

یک نشست PowerShell باز کنید، متغیر `$Version` را برابر نسخهٔ موردنظر قرار دهید (برای مثال `$Version="1.4.3"`) و
سپس فرمان‌های زیر را اجرا کنید:

1. containerd را دانلود کنید:

   ```powershell
   curl.exe -L https://github.com/containerd/containerd/releases/download/v$Version/containerd-$Version-windows-amd64.tar.gz -o containerd-windows-amd64.tar.gz
   tar.exe xvf .\containerd-windows-amd64.tar.gz
   ```

2. فایل‌ها را استخراج و پیکربندی کنید:

   ```powershell
   Copy-Item -Path ".\bin\" -Destination "$Env:ProgramFiles\containerd" -Recurse -Force
   cd $Env:ProgramFiles\containerd\
   .\containerd.exe config default | Out-File config.toml -Encoding ascii

   # Review the configuration. Depending on setup you may want to adjust:
   # - the sandbox_image (Kubernetes pause image)
   # - cni bin_dir and conf_dir locations
   Get-Content config.toml

   # (Optional - but highly recommended) Exclude containerd from Windows Defender Scans
   Add-MpPreference -ExclusionProcess "$Env:ProgramFiles\containerd\containerd.exe"
   ```

3. containerd را راه‌اندازی کنید:

   ```powershell
   .\containerd.exe --register-service
   Start-Service containerd
   ```

{{% /tab %}}
{{< /tabs >}}

## پیکربندی kubelet برای استفاده از containerd به‌عنوان محیط اجرای کانتینر

فایل `/var/lib/kubelet/kubeadm-flags.env` را ویرایش کنید و محیط اجرای containerd را به فلگ‌ها اضافه کنید:
`--container-runtime-endpoint=unix:///run/containerd/containerd.sock`.

کاربرانی که از kubeadm استفاده می‌کنند باید بدانند که ابزار kubeadm سوکت CRI میزبان را در فایل

`/var/lib/kubelet/instance-config.yaml` روی هر نود ذخیره می‌کند. می‌توانید این فایل `/var/lib/kubelet/instance-config.yaml` را روی نود ایجاد کنید.

با فایل `/var/lib/kubelet/instance-config.yaml` می‌توانید پارامتر `containerRuntimeEndpoint` را تنظیم کنید.

مقدار این پارامتر را می‌توانید برابر مسیر سوکت CRI انتخابی خود قرار دهید (برای مثال `unix:///run/containerd/containerd.sock`).

## راه‌اندازی مجدد kubelet

```shell
systemctl start kubelet
```

## بررسی سلامت نود

فرمان `kubectl get nodes -o wide` را اجرا کنید؛ containerd باید به‌عنوان محیط اجرای نودی که هم‌اکنون تغییر دادیم نمایش داده شود.

## حذف Docker Engine

{{% thirdparty-content %}}

اگر نود سالم به نظر می‌رسد، Docker را حذف کنید.

{{< tabs name="tab-remove-docker-engine" >}}
{{% tab name="CentOS" %}}

```shell
sudo dnf remove docker-ce docker-ce-cli
```
{{% /tab %}}
{{% tab name="Debian" %}}

```shell
sudo apt-get purge docker-ce docker-ce-cli
```
{{% /tab %}}
{{% tab name="Fedora" %}}

```shell
sudo dnf remove docker-ce docker-ce-cli
```
{{% /tab %}}
{{% tab name="Ubuntu" %}}

```shell
sudo apt-get purge docker-ce docker-ce-cli
```
{{% /tab %}}
{{< /tabs >}}

فرمان‌های بالا ایمیج‌ها، کانتینرها، حجم‌ها (volumes) یا فایل‌های پیکربندی سفارشی‌شده را از میزبان شما حذف نمی‌کنند.
برای حذف آن‌ها، دستورالعمل‌های Docker برای [حذف Docker Engine](https://docs.docker.com/engine/install/ubuntu/#uninstall-docker-engine) را دنبال کنید.

{{< caution >}}
اجرای دستورالعمل‌های Docker برای حذف Docker Engine ممکن است به حذف containerd نیز منجر شود. هنگام اجرای فرمان‌ها احتیاط کنید.
{{< /caution >}}

## خارج کردن نود از حالت cordon

```shell
kubectl uncordon <node-to-uncordon>
```

به‌جای `<node-to-uncordon>` نام نودی را که پیش‌تر تخلیه کرده بودید قرار دهید.
