---
title: HostAliases
id: HostAliases
full_link: /docs/reference/generated/kubernetes-api/{{< param "version" >}}/#hostalias-v1-core
short_description: >
  HostAliases نگاشتی میان یک آدرس IP و یک نام میزبان (hostname) است که به فایل hosts یک Pod تزریق می‌شود.

aka:
tags:
- operation
---
 HostAliases نگاشتی میان یک آدرس IP و یک نام میزبان (hostname) است که به فایل hosts یک {{< glossary_tooltip text="Pod" term_id="pod" >}} تزریق می‌شود.

<!--more-->

[HostAliases](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#hostalias-v1-core) فهرستی اختیاری از نام‌های میزبان و آدرس‌های IP است که در صورت مشخص شدن، به فایل hosts مربوط به Pod تزریق می‌شود. این قابلیت فقط برای Podهایی معتبر است که از hostNetwork استفاده نمی‌کنند.
