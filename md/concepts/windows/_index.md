---
title: "ویندوز در کوبرنتیز"
simple_list: true
weight: 200 # late in list
description: >-
  کوبرنتیز از نودهایی که Microsoft Windows را اجرا می‌کنند پشتیبانی می‌کند.
---

کوبرنتیز از {{< glossary_tooltip text="نودهای" term_id="node" >}} کارگر (worker) که Linux یا Microsoft Windows را اجرا می‌کنند پشتیبانی می‌کند.

{{% thirdparty-content single="true" %}}

بنیاد CNCF و بنیاد مادر آن، یعنی Linux Foundation، رویکردی بی‌طرف نسبت به فروشندگان (vendor-neutral) در زمینه سازگاری در پیش می‌گیرند. می‌توان [Windows server](https://www.microsoft.com/en-us/windows-server) خود را به‌عنوان یک نود کارگر به یک کلاستر کوبرنتیز اضافه کرد.

بدون توجه به اینکه در کلاستر خود از کدام سیستم‌عامل استفاده می‌کنید، می‌توانید [kubectl را روی Windows نصب و راه‌اندازی کنید](/docs/tasks/tools/install-kubectl-windows/).

اگر از نودهای Windows استفاده می‌کنید، می‌توانید موارد زیر را مطالعه کنید:

* [شبکه در Windows](/docs/concepts/services-networking/windows-networking/)
* [ذخیره‌سازی Windows در کوبرنتیز](/docs/concepts/storage/windows-storage/)
* [مدیریت منابع برای نودهای Windows](/docs/concepts/configuration/windows-resource-management/)
* [پیکربندی RunAsUserName برای Podها و کانتینرهای Windows](/docs/tasks/configure-pod-container/configure-runasusername/)
* [ایجاد یک Pod از نوع HostProcess در Windows](/docs/tasks/configure-pod-container/create-hostprocess-pod/)
* [پیکربندی Group Managed Service Accounts برای Podها و کانتینرهای Windows](/docs/tasks/configure-pod-container/configure-gmsa/)
* [امنیت برای نودهای Windows](/docs/concepts/security/windows-security/)
* [نکات عیب‌یابی در Windows](/docs/tasks/debug/debug-cluster/windows/)
* [راهنمای زمان‌بندی کانتینرهای Windows در کوبرنتیز](/docs/concepts/windows/user-guide)

یا برای مرور کلی، موارد زیر را مطالعه کنید:
