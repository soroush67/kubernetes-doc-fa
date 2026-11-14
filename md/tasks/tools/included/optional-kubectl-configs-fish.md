---
title: "تکمیل خودکار در fish"
description: "پیکربندی اختیاری برای فعال‌سازی تکمیل خودکار در پوسته fish."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

{{< note >}}
برای استفاده از تکمیل خودکار (autocomplete) در Fish به kubectl نسخه 1.23 یا بالاتر نیاز دارید.
{{< /note >}}

اسکریپت تکمیل kubectl برای Fish را می‌توان با فرمان `kubectl completion fish` تولید کرد. با بارگذاری (source) این اسکریپت در پوسته‌تان، تکمیل خودکار kubectl فعال می‌شود.

برای اینکه این قابلیت در همه نشست‌های پوسته فعال باشد، خط زیر را به فایل `~/.config/fish/config.fish` اضافه کنید:

```shell
kubectl completion fish | source
```

پس از بارگذاری مجدد پوسته، تکمیل خودکار kubectl باید کار کند.
