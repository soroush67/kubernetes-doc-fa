---
title: "تکمیل خودکار bash در لینوکس"
description: "برخی پیکربندی‌های اختیاری برای تکمیل خودکار bash در لینوکس."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

### مقدمه

اسکریپت تکمیل خودکار (completion) kubectl برای Bash را می‌توان با فرمان `kubectl completion bash` تولید کرد.
با فراخوانی (source) این اسکریپت در شل، تکمیل خودکار kubectl فعال می‌شود.

با این حال، اسکریپت تکمیل به
[**bash-completion**](https://github.com/scop/bash-completion)
وابسته است؛ بنابراین ابتدا باید این نرم‌افزار را نصب کنید
(برای بررسی اینکه bash-completion از قبل نصب شده است یا نه، می‌توانید فرمان `type _init_completion` را اجرا کنید).

### نصب bash-completion

بستهٔ bash-completion در بسیاری از مدیران بسته ارائه می‌شود
([اینجا](https://github.com/scop/bash-completion#installation) را ببینید).
می‌توانید آن را با فرمان‌هایی مانند `apt-get install bash-completion` یا `dnf install bash-completion` نصب کنید.

فرمان‌های بالا فایل `/usr/share/bash-completion/bash_completion` را ایجاد می‌کنند
که اسکریپت اصلی bash-completion است. بسته به مدیر بستهٔ شما،
ممکن است لازم باشد این فایل را به‌صورت دستی در فایل `~/.bashrc` فراخوانی کنید.

برای اطمینان، شل خود را دوباره بارگذاری کنید و فرمان `type _init_completion` را اجرا کنید.
اگر فرمان با موفقیت اجرا شد، تنظیمات شما کامل است؛ در غیر این صورت، خط زیر را به فایل `~/.bashrc` اضافه کنید:

```bash
source /usr/share/bash-completion/bash_completion
```

شل خود را دوباره بارگذاری کنید و با اجرای `type _init_completion` بررسی کنید که bash-completion به‌درستی نصب شده باشد.

### فعال‌سازی تکمیل خودکار kubectl

#### Bash

اکنون باید مطمئن شوید که اسکریپت تکمیل kubectl در همهٔ نشست‌های شل شما
فراخوانی می‌شود. این کار به دو روش انجام‌پذیر است:

{{< tabs name="kubectl_bash_autocompletion" >}}
{{< tab name="کاربر" codelang="bash" >}}
echo 'source <(kubectl completion bash)' >>~/.bashrc
{{< /tab >}}
{{< tab name="سیستم" codelang="bash" >}}
kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
sudo chmod a+r /etc/bash_completion.d/kubectl
{{< /tab >}}
{{< /tabs >}}

اگر برای kubectl یک نام مستعار (alias) دارید، می‌توانید تکمیل شل را طوری گسترش دهید که با آن نام مستعار نیز کار کند:

```bash
echo 'alias k=kubectl' >>~/.bashrc
echo 'complete -o default -F __start_kubectl k' >>~/.bashrc
```

{{< note >}}
ابزار bash-completion همهٔ اسکریپت‌های تکمیل موجود در `/etc/bash_completion.d` را فراخوانی می‌کند.
{{< /note >}}

هر دو روش معادل یکدیگرند. پس از بارگذاری دوبارهٔ شل، تکمیل خودکار kubectl باید کار کند.
برای فعال‌سازی تکمیل خودکار bash در نشست فعلی شل، فایل ~/.bashrc را فراخوانی کنید:

```bash
source ~/.bashrc
```
