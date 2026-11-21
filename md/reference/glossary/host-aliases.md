---
title: HostAliases
id: HostAliases
full_link: /docs/reference/generated/kubernetes-api/{{< param "version" >}}/#hostalias-v1-core
short_description: >
  هر HostAliases نگاشتی میان نشانی IP و نام میزبان است که در فایل hosts یک Pod تزریق می‌شود.

aka:
tags:
- operation
---
 هر HostAliases نگاشتی میان نشانی IP و نام میزبان (hostname) است که در فایل hosts یک {{< glossary_tooltip text="Pod" term_id="pod" >}} تزریق می‌شود.

<!--more-->

فیلد [HostAliases](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#hostalias-v1-core) فهرستی اختیاری از نام‌های میزبان و نشانی‌های IP است که در صورت تعیین‌شدن، در فایل hosts مربوط به Pod تزریق می‌شود. این فیلد فقط برای Podهایی معتبر است که از hostNetwork استفاده نمی‌کنند.
