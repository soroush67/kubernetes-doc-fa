---
title: "تکمیل خودکار در PowerShell"
description: "پیکربندی‌های اختیاری برای تکمیل خودکار در PowerShell."
headless: true
_build:
  list: never
  render: never
  publishResources: false
---

اسکریپت تکمیل kubectl برای PowerShell را می‌توان با فرمان `kubectl completion powershell` تولید کرد.

برای فعال‌کردن آن در همهٔ نشست‌های پوسته، خط زیر را به فایل `$PROFILE` خود اضافه کنید:

```powershell
kubectl completion powershell | Out-String | Invoke-Expression
```

این فرمان اسکریپت تکمیل خودکار را در هر بار راه‌اندازی PowerShell دوباره تولید می‌کند. همچنین می‌توانید اسکریپت تولیدشده را مستقیماً به فایل `$PROFILE` خود اضافه کنید.

برای افزودن اسکریپت تولیدشده به فایل `$PROFILE`، خط زیر را در اعلان فرمان PowerShell اجرا کنید:

```powershell
kubectl completion powershell >> $PROFILE
```

پس از بارگذاری مجدد پوسته، تکمیل خودکار kubectl باید کار کند.
