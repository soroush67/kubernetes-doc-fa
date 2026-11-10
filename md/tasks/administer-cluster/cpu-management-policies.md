---
title: کنترل سیاست‌های مدیریت CPU روی نود
reviewers:
- sjenning
- ConnorDoyle
- balajismaniam

content_type: task
min-kubernetes-server-version: v1.26
weight: 140
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

کوبرنتیز بسیاری از جنبه‌های نحوهٔ اجرای پادها روی نودها را از دید کاربر پنهان و انتزاعی نگه می‌دارد و این رفتار عمدی است. با این حال، برخی از بارهای کاری برای اینکه عملکرد قابل‌قبولی داشته باشند، به تضمین‌های قوی‌تری از نظر تأخیر و/یا کارایی نیاز دارند. kubelet روش‌هایی فراهم می‌کند که با آن‌ها می‌توان سیاست‌های پیچیده‌تری برای جای‌گذاری بار کاری به کار گرفت، بی‌آنکه لازم باشد دستورهای صریح جای‌گذاری به این لایهٔ انتزاعی اضافه شود.

برای اطلاعات بیشتر دربارهٔ مدیریت منابع، به مستندات [مدیریت منابع برای پادها و کانتینرها](/docs/concepts/configuration/manage-resources-containers) مراجعه کنید.

برای اطلاعات بیشتر دربارهٔ نحوهٔ پیاده‌سازی مدیریت منابع در kubelet، به مستندات [مدیران منابع نود](/docs/concepts/policy/node-resource-managers) مراجعه کنید.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

اگر از نسخهٔ قدیمی‌تری از کوبرنتیز استفاده می‌کنید، مستندات مربوط به همان نسخه‌ای را که واقعاً اجرا می‌کنید مطالعه کنید.


<!-- steps -->

## پیکربندی سیاست‌های مدیریت CPU

به‌طور پیش‌فرض، kubelet برای اعمال محدودیت‌های CPU پادها از [سهمیهٔ CFS](https://en.wikipedia.org/wiki/Completely_Fair_Scheduler) (CFS quota) استفاده می‌کند. هنگامی که تعداد زیادی پاد وابسته به CPU روی نود اجرا می‌شوند، بار کاری ممکن است بسته به اینکه پاد محدود (throttle) شده باشد یا نه و اینکه در زمان زمان‌بندی کدام هسته‌های CPU در دسترس باشند، به هسته‌های مختلف CPU منتقل شود. بسیاری از بارهای کاری به این جابه‌جایی حساس نیستند و بنابراین بدون هیچ مداخله‌ای به‌خوبی کار می‌کنند.

با این حال، در بارهای کاری‌ای که وابستگی به حافظهٔ نهان CPU (CPU cache affinity) و تأخیر زمان‌بندی تأثیر چشمگیری بر کارایی آن‌ها دارد، kubelet امکان استفاده از سیاست‌های جایگزین مدیریت CPU را فراهم می‌کند تا بتوان برخی ترجیحات جای‌گذاری را روی نود تعیین کرد.

## پشتیبانی از ویندوز

{{< feature-state feature_gate_name="WindowsCPUAndMemoryAffinity" >}}

پشتیبانی از مدیر CPU (CPU Manager) را می‌توان با استفاده از feature gate با نام `WindowsCPUAndMemoryAffinity` روی ویندوز فعال کرد؛ این قابلیت به پشتیبانی محیط اجرای کانتینر نیز نیاز دارد. پس از فعال کردن این feature gate، مراحل زیر را برای پیکربندی [سیاست مدیر CPU](#configuration) دنبال کنید.

## پیکربندی

سیاست مدیر CPU با فلگ `--cpu-manager-policy` در kubelet یا فیلد `cpuManagerPolicy` در [KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/) تنظیم می‌شود. دو سیاست پشتیبانی می‌شود:

* [`none`](#none-policy): سیاست پیش‌فرض.
* [`static`](#static-policy): به پادهایی با ویژگی‌های منبعی مشخص اجازه می‌دهد وابستگی (affinity) و انحصار بیشتری روی CPUهای نود داشته باشند.

مدیر CPU به‌صورت دوره‌ای به‌روزرسانی‌های منابع را از طریق CRI می‌نویسد تا تخصیص‌های CPU موجود در حافظه را با cgroupfs هماهنگ کند. بسامد این هماهنگ‌سازی با یک مقدار پیکربندی جدید kubelet، یعنی `--cpu-manager-reconcile-period`، تنظیم می‌شود. اگر این مقدار مشخص نشود، به‌طور پیش‌فرض برابر با مدت‌زمان `--node-status-update-frequency` خواهد بود.

رفتار سیاست static را می‌توان با فلگ `--cpu-manager-policy-options` به‌دقت تنظیم کرد. این فلگ فهرستی از گزینه‌های سیاست به شکل `key=value` را می‌پذیرد که با کاما از هم جدا شده‌اند. اگر [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `CPUManagerPolicyOptions` را غیرفعال کنید، دیگر نمی‌توانید سیاست‌های مدیر CPU را به‌دقت تنظیم کنید. در این حالت، مدیر CPU فقط با تنظیمات پیش‌فرض خود کار می‌کند.

افزون بر feature gate سطح بالای `CPUManagerPolicyOptions`، گزینه‌های سیاست به دو گروه تقسیم می‌شوند: گزینه‌های با کیفیت آلفا (به‌طور پیش‌فرض پنهان) و گزینه‌های با کیفیت بتا (به‌طور پیش‌فرض قابل‌مشاهده). این گروه‌ها به ترتیب با feature gateهای `CPUManagerPolicyAlphaOptions` و `CPUManagerPolicyBetaOptions` کنترل می‌شوند. برخلاف رویهٔ استاندارد کوبرنتیز، این feature gateها گروه‌هایی از گزینه‌ها را کنترل می‌کنند، زیرا افزودن یک feature gate جداگانه برای هر گزینه بیش از حد دست‌وپاگیر می‌بود.

## تغییر سیاست مدیر CPU

از آنجا که سیاست مدیر CPU فقط هنگام ایجاد پادهای جدید توسط kubelet اعمال می‌شود، تغییر سادهٔ آن از "none" به "static" روی پادهای موجود اثری ندارد. بنابراین برای تغییر درست سیاست مدیر CPU روی یک نود، مراحل زیر را انجام دهید:

1. نود را [تخلیه (drain)](/docs/tasks/administer-cluster/safely-drain-node) کنید.
2. kubelet را متوقف کنید.
3. فایل وضعیت قدیمی مدیر CPU را حذف کنید. مسیر این فایل به‌طور پیش‌فرض
`/var/lib/kubelet/cpu_manager_state` است. با این کار وضعیتی که CPUManager نگه می‌دارد پاک می‌شود تا مجموعه‌های CPU (cpu-sets) که سیاست جدید تنظیم می‌کند با آن تداخل نداشته باشند.
4. پیکربندی kubelet را ویرایش کنید و سیاست مدیر CPU را به مقدار دلخواه تغییر دهید.
5. kubelet را راه‌اندازی کنید.

این فرایند را برای هر نودی که باید سیاست مدیر CPU آن تغییر کند تکرار کنید. اگر این فرایند را انجام ندهید، kubelet مدام از کار می‌افتد و دوباره راه‌اندازی می‌شود (crashloop) و خطای زیر را نشان می‌دهد:

```
could not restore state from checkpoint: configured policy "static" differs from state checkpoint policy "none", please drain this node and delete the CPU manager checkpoint file "/var/lib/kubelet/cpu_manager_state" before restarting Kubelet
```

{{< note >}}
اگر مجموعهٔ CPUهای آنلاین روی نود تغییر کند، باید نود را تخلیه کنید و مدیر CPU را با حذف فایل وضعیت `cpu_manager_state` در دایرکتوری ریشهٔ kubelet به‌صورت دستی بازنشانی کنید.
{{< /note >}}

### پیکربندی سیاست `none`

این سیاست هیچ گزینهٔ پیکربندی اضافه‌ای ندارد.

### پیکربندی سیاست `static`

این سیاست یک مخزن مشترک (shared pool) از CPUها را مدیریت می‌کند که در ابتدا همهٔ CPUهای نود را در بر دارد. تعداد CPUهایی که می‌توان به‌صورت انحصاری تخصیص داد برابر است با کل CPUهای نود منهای CPUهایی که با گزینه‌های `--kube-reserved` یا `--system-reserved` در kubelet رزرو شده‌اند. از نسخهٔ 1.17 به بعد، می‌توان فهرست CPUهای رزروشده را به‌صراحت با گزینهٔ `--reserved-cpus` در kubelet مشخص کرد. فهرست صریح CPUهایی که با `--reserved-cpus` مشخص می‌شود بر رزرو CPU تعیین‌شده با `--kube-reserved` و `--system-reserved` اولویت دارد. CPUهایی که با این گزینه‌ها رزرو می‌شوند، به تعداد صحیح و به ترتیب صعودی شناسهٔ هستهٔ فیزیکی، از مخزن مشترک اولیه برداشته می‌شوند. این مخزن مشترک مجموعه‌ای از CPUهاست که همهٔ کانتینرهای پادهای `BestEffort` و `Burstable` روی آن اجرا می‌شوند. کانتینرهای پادهای `Guaranteed` که مقدار `requests` CPU آن‌ها کسری است نیز روی CPUهای مخزن مشترک اجرا می‌شوند. فقط به کانتینرهایی CPU انحصاری اختصاص داده می‌شود که هم بخشی از یک پاد `Guaranteed` باشند و هم مقدار `requests` CPU آن‌ها عدد صحیح باشد.

{{< note >}}
هنگامی که سیاست static فعال است، kubelet نیاز دارد که با استفاده از `--kube-reserved` و/یا `--system-reserved` یا `--reserved-cpus`، مقداری بزرگ‌تر از صفر CPU رزرو شود. دلیل این است که رزرو صفر CPU باعث می‌شود مخزن مشترک بتواند خالی شود.
{{< /note >}}

### گزینه‌های سیاست static {#cpu-policy-static--options}

می‌توانید گروه‌هایی از گزینه‌ها را بر اساس سطح بلوغشان با استفاده از feature gateهای زیر فعال یا غیرفعال کنید:
* `CPUManagerPolicyBetaOptions` به‌طور پیش‌فرض فعال است. برای پنهان کردن گزینه‌های سطح بتا آن را غیرفعال کنید.
* `CPUManagerPolicyAlphaOptions` به‌طور پیش‌فرض غیرفعال است. برای نمایش گزینه‌های سطح آلفا آن را فعال کنید.
همچنان باید هر گزینه را با استفاده از گزینهٔ `CPUManagerPolicyOptions` در kubelet فعال کنید.

گزینه‌های زیر برای سیاست static در `CPUManager` وجود دارند:
* `full-pcpus-only` (GA، به‌طور پیش‌فرض قابل‌مشاهده) (نسخهٔ 1.33 یا بالاتر)
* `distribute-cpus-across-numa` (بتا، به‌طور پیش‌فرض قابل‌مشاهده) (نسخهٔ 1.33 یا بالاتر)
* `align-by-socket` (آلفا، به‌طور پیش‌فرض پنهان) (نسخهٔ 1.25 یا بالاتر)
* `distribute-cpus-across-cores` (آلفا، به‌طور پیش‌فرض پنهان) (نسخهٔ 1.31 یا بالاتر)
* `strict-cpu-reservation` (GA، به‌طور پیش‌فرض قابل‌مشاهده) (نسخهٔ 1.35 یا بالاتر)
* `prefer-align-cpus-by-uncorecache` (GA، به‌طور پیش‌فرض قابل‌مشاهده) (نسخهٔ 1.36 یا بالاتر)

گزینهٔ `full-pcpus-only` را می‌توان با افزودن `full-pcpus-only=true` به گزینه‌های سیاست CPUManager فعال کرد.
به همین ترتیب، گزینهٔ `distribute-cpus-across-numa` را می‌توان با افزودن `distribute-cpus-across-numa=true` به گزینه‌های سیاست CPUManager فعال کرد.
وقتی هر دو تنظیم شوند، اثرشان «افزایشی» است؛ به این معنا که CPUها به‌جای هسته‌های منفرد، در قالب بسته‌هایی از CPUهای فیزیکی کامل (full-pcpus) میان نودهای NUMA توزیع می‌شوند.
گزینهٔ سیاست `align-by-socket` را می‌توان با افزودن `align-by-socket=true` به گزینه‌های سیاست `CPUManager` فعال کرد. این گزینه نیز با گزینه‌های سیاست `full-pcpus-only` و `distribute-cpus-across-numa` به‌صورت افزایشی عمل می‌کند.

گزینهٔ `distribute-cpus-across-cores` را می‌توان با افزودن `distribute-cpus-across-cores=true` به گزینه‌های سیاست `CPUManager` فعال کرد.
در حال حاضر نمی‌توان این گزینه را هم‌زمان با گزینه‌های سیاست `full-pcpus-only` یا `distribute-cpus-across-numa` استفاده کرد.

برای فعال کردن گزینهٔ `strict-cpu-reservation`، مقدار `strict-cpu-reservation=true` را به گزینه‌های سیاست CPUManager اضافه کنید، سپس فایل `/var/lib/kubelet/cpu_manager_state` را حذف کنید و kubelet را دوباره راه‌اندازی کنید.

گزینهٔ `prefer-align-cpus-by-uncorecache` را می‌توان با افزودن `prefer-align-cpus-by-uncorecache` به گزینه‌های سیاست `CPUManager` فعال کرد. اگر از گزینه‌های ناسازگار استفاده شود، kubelet راه‌اندازی نمی‌شود و خطای مربوط در لاگ‌ها توضیح داده می‌شود.

برای جزئیات بیشتر دربارهٔ رفتار هر یک از گزینه‌هایی که می‌توانید پیکربندی کنید، به مستندات [مدیران منابع نود](/docs/concepts/policy/node-resource-managers) مراجعه کنید.

## {{% heading "whatsnext" %}}

* دربارهٔ [مدیران منابع در سطح پاد](/docs/concepts/resource-management/resource-managers/#pod-level-resource-managers) مطالعه کنید.
