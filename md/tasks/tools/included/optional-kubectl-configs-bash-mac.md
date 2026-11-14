---
title: "تکمیل خودکار bash در macOS"
description: "برخی پیکربندی‌های اختیاری برای تکمیل خودکار bash در macOS."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

### مقدمه

اسکریپت تکمیل kubectl برای Bash را می‌توان با دستور `kubectl completion bash` تولید کرد.
با بارگذاری (source) این اسکریپت در پوسته، تکمیل خودکار kubectl فعال می‌شود.

با این حال، اسکریپت تکمیل kubectl به
[**bash-completion**](https://github.com/scop/bash-completion) وابسته است و بنابراین باید پیش از آن، این ابزار را نصب کنید.

{{< warning>}}
دو نسخه از bash-completion وجود دارد: v1 و v2. نسخهٔ v1 برای Bash 3.2
(که نسخهٔ پیش‌فرض در macOS است) و نسخهٔ v2 برای Bash 4.1+ است. اسکریپت تکمیل
kubectl با bash-completion v1 و Bash 3.2 به‌درستی **کار نمی‌کند** و
به **bash-completion v2** و **Bash 4.1+** نیاز دارد. بنابراین برای اینکه بتوانید
تکمیل kubectl را در macOS به‌درستی استفاده کنید، باید Bash 4.1+ را نصب و استفاده کنید
([*دستورالعمل‌ها*](https://apple.stackexchange.com/a/292760)).
دستورالعمل‌های زیر فرض می‌کنند که از Bash 4.1+ استفاده می‌کنید
(یعنی هر نسخه‌ای از Bash که 4.1 یا جدیدتر باشد).
{{< /warning >}}

### ارتقای Bash

دستورالعمل‌های این بخش فرض می‌کنند که از Bash 4.1+ استفاده می‌کنید. برای بررسی نسخهٔ Bash خود، دستور زیر را اجرا کنید:

```bash
echo $BASH_VERSION
```

اگر نسخهٔ آن بیش از حد قدیمی است، می‌توانید آن را با Homebrew نصب یا ارتقا دهید:

```bash
brew install bash
```

پوستهٔ خود را دوباره بارگذاری کنید و بررسی کنید که نسخهٔ موردنظر در حال استفاده است:

```bash
echo $BASH_VERSION $SHELL
```

ابزار Homebrew معمولاً آن را در مسیر `/usr/local/bin/bash` نصب می‌کند.

### نصب bash-completion

{{< note >}}
همان‌طور که اشاره شد، این دستورالعمل‌ها فرض می‌کنند که از Bash 4.1+ استفاده می‌کنید؛ یعنی
bash-completion v2 را نصب خواهید کرد (برخلاف Bash 3.2 و bash-completion v1
که در آن حالت، تکمیل kubectl کار نمی‌کند).
{{< /note >}}

با دستور `type _init_completion` می‌توانید بررسی کنید که آیا bash-completion v2 از قبل نصب شده است یا نه.
اگر نصب نشده است، می‌توانید آن را با Homebrew نصب کنید:

```bash
brew install bash-completion@2
```

همان‌طور که در خروجی این دستور آمده است، خط زیر را به فایل `~/.bash_profile` خود اضافه کنید:

```bash
brew_etc="$(brew --prefix)/etc" && [[ -r "${brew_etc}/profile.d/bash_completion.sh" ]] && . "${brew_etc}/profile.d/bash_completion.sh"
```

پوستهٔ خود را دوباره بارگذاری کنید و با دستور `type _init_completion` بررسی کنید که bash-completion v2 به‌درستی نصب شده است.

### فعال‌سازی تکمیل خودکار kubectl

اکنون باید مطمئن شوید که اسکریپت تکمیل kubectl در همهٔ نشست‌های پوستهٔ شما
بارگذاری می‌شود. چند راه برای این کار وجود دارد:

- اسکریپت تکمیل را در فایل `~/.bash_profile` خود بارگذاری کنید:

    ```bash
    echo 'source <(kubectl completion bash)' >>~/.bash_profile
    ```

- اسکریپت تکمیل را به دایرکتوری `/usr/local/etc/bash_completion.d` اضافه کنید:

    ```bash
    kubectl completion bash >/usr/local/etc/bash_completion.d/kubectl
    ```

- اگر برای kubectl یک نام مستعار (alias) دارید، می‌توانید تکمیل پوسته را طوری گسترش دهید که با آن نام مستعار نیز کار کند:

    ```bash
    echo 'alias k=kubectl' >>~/.bash_profile
    echo 'complete -o default -F __start_kubectl k' >>~/.bash_profile
    ```

- اگر kubectl را با Homebrew نصب کرده‌اید (همان‌طور که
  [اینجا](/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos) توضیح داده شده است)،
  اسکریپت تکمیل kubectl باید از قبل در `/usr/local/etc/bash_completion.d/kubectl` وجود داشته باشد.
  در این صورت، لازم نیست کاری انجام دهید.

   {{< note >}}
   نصب bash-completion v2 از طریق Homebrew همهٔ فایل‌های موجود در دایرکتوری
   `BASH_COMPLETION_COMPAT_DIR` را بارگذاری می‌کند و به همین دلیل دو روش آخر کار می‌کنند.
   {{< /note >}}

در هر صورت، پس از بارگذاری دوبارهٔ پوسته، تکمیل kubectl باید کار کند.
