---
title: "تکمیل خودکار در zsh"
description: "برخی پیکربندی‌های اختیاری برای تکمیل خودکار در zsh."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

اسکریپت تکمیل خودکار kubectl برای Zsh را می‌توان با فرمان `kubectl completion zsh` تولید کرد. با بارگذاری (source) این اسکریپت در پوسته، تکمیل خودکار kubectl فعال می‌شود.

برای فعال‌کردن آن در همهٔ نشست‌های پوسته، خط زیر را به فایل `~/.zshrc` خود اضافه کنید:

```zsh
source <(kubectl completion zsh)
```

اگر برای kubectl یک نام مستعار (alias) تعریف کرده باشید، تکمیل خودکار kubectl به‌طور خودکار با آن نیز کار می‌کند.

پس از بارگذاری مجدد پوسته، تکمیل خودکار kubectl باید کار کند.

اگر با خطایی مانند `2: command not found: compdef` روبه‌رو شدید، خطوط زیر را به ابتدای فایل `~/.zshrc` خود اضافه کنید:

```zsh
autoload -Uz compinit
compinit
```
