---
title: پایش سلامت نود
content_type: task
reviewers:
- Random-Liu
- dchen1107
weight: 20
---

<!-- overview -->

*آشکارساز مشکلات نود (Node Problem Detector)* یک دیمن (daemon) برای پایش سلامت نود و گزارش درباره‌ی آن است.
می‌توانید آشکارساز مشکلات نود را به‌صورت یک `DaemonSet` یا به‌صورت یک دیمن مستقل اجرا کنید.
این ابزار اطلاعات مربوط به مشکلات نود را از دیمن‌های گوناگون جمع‌آوری می‌کند
و این وضعیت‌ها را به‌شکل [Condition](/docs/concepts/architecture/nodes/#condition)های نود
یا به‌شکل [Event](/docs/reference/kubernetes-api/cluster-resources/event-v1)ها به API server گزارش می‌دهد.

برای آشنایی با نحوه‌ی نصب و استفاده از آشکارساز مشکلات نود، به
[مستندات پروژه‌ی Node Problem Detector](https://github.com/kubernetes/node-problem-detector) مراجعه کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## محدودیت‌ها

* آشکارساز مشکلات نود برای گزارش مشکلات کرنل از قالب لاگ کرنل استفاده می‌کند.
  برای آشنایی با نحوه‌ی گسترش قالب لاگ کرنل، به [افزودن پشتیبانی از قالب‌های دیگر لاگ](#support-other-log-format) مراجعه کنید.

## فعال‌سازی آشکارساز مشکلات نود

برخی از ارائه‌دهندگان ابری، آشکارساز مشکلات نود را به‌عنوان یک {{< glossary_tooltip text="افزونه" term_id="addons" >}} فعال می‌کنند.
همچنین می‌توانید آشکارساز مشکلات نود را با `kubectl` یا با ایجاد یک DaemonSet افزونه فعال کنید.

### استفاده از kubectl برای فعال‌سازی آشکارساز مشکلات نود {#using-kubectl}

ابزار `kubectl` انعطاف‌پذیرترین روش مدیریت آشکارساز مشکلات نود را فراهم می‌کند.
می‌توانید پیکربندی پیش‌فرض را بازنویسی کنید تا با محیط شما سازگار شود یا
مشکلات سفارشی نود را تشخیص دهد. برای نمونه:

1. یک پیکربندی برای آشکارساز مشکلات نود، مشابه `node-problem-detector.yaml`، ایجاد کنید:

   {{% code_sample file="debug/node-problem-detector.yaml" %}}

   {{< note >}}
   باید بررسی کنید که مسیر پوشه‌ی لاگ سیستم برای توزیع سیستم‌عامل شما درست باشد.
   {{< /note >}}

1. آشکارساز مشکلات نود را با `kubectl` راه‌اندازی کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/debug/node-problem-detector.yaml
   ```

### استفاده از یک پاد افزونه برای فعال‌سازی آشکارساز مشکلات نود {#using-addon-pod}

اگر از یک راهکار سفارشی برای راه‌اندازی اولیه‌ی کلاستر استفاده می‌کنید و نیازی
به بازنویسی پیکربندی پیش‌فرض ندارید، می‌توانید از پاد افزونه بهره بگیرید تا
فرایند استقرار را بیشتر خودکار کنید.

فایل `node-problem-detector.yaml` را ایجاد کنید و پیکربندی را در پوشه‌ی پاد افزونه،
یعنی `/etc/kubernetes/addons/node-problem-detector`، روی یکی از نودهای control plane ذخیره کنید.

## بازنویسی پیکربندی

[پیکربندی پیش‌فرض](https://github.com/kubernetes/node-problem-detector/tree/v0.8.12/config)
هنگام ساخت ایمیج Docker آشکارساز مشکلات نود در آن جاسازی می‌شود.

با این حال، می‌توانید از یک [`ConfigMap`](/docs/tasks/configure-pod-container/configure-pod-configmap/)
برای بازنویسی پیکربندی استفاده کنید:

1. فایل‌های پیکربندی را در `config/` تغییر دهید.
1. آبجکت `ConfigMap` با نام `node-problem-detector-config` را ایجاد کنید:

   ```shell
   kubectl create configmap node-problem-detector-config --from-file=config/
   ```

1. فایل `node-problem-detector.yaml` را طوری تغییر دهید که از `ConfigMap` استفاده کند:

   {{% code_sample file="debug/node-problem-detector-configmap.yaml" %}}

1. آشکارساز مشکلات نود را با فایل پیکربندی جدید دوباره ایجاد کنید:

   ```shell
   # If you have a node-problem-detector running, delete before recreating
   kubectl delete -f https://k8s.io/examples/debug/node-problem-detector.yaml
   kubectl apply -f https://k8s.io/examples/debug/node-problem-detector-configmap.yaml
   ```

{{< note >}}
این روش فقط برای آشکارساز مشکلات نودی کاربرد دارد که با `kubectl` راه‌اندازی شده باشد.
{{< /note >}}

اگر آشکارساز مشکلات نود به‌عنوان افزونه‌ی کلاستر اجرا شود، بازنویسی پیکربندی پشتیبانی نمی‌شود،
زیرا مدیر افزونه‌ها (Addon manager) از `ConfigMap` پشتیبانی نمی‌کند.

## دیمن‌های تشخیص مشکل

دیمن تشخیص مشکل (problem daemon) یک زیردیمن از آشکارساز مشکلات نود است. این دیمن انواع مشخصی از
مشکلات نود را پایش می‌کند و آن‌ها را به آشکارساز مشکلات نود گزارش می‌دهد.
چند نوع دیمن تشخیص مشکل پشتیبانی می‌شود:

- دیمن‌های نوع `SystemLogMonitor` لاگ‌های سیستم را پایش می‌کنند و مشکلات و متریک‌ها را
  بر اساس قواعد از پیش تعریف‌شده گزارش می‌دهند. می‌توانید پیکربندی‌ها را برای منابع مختلف لاگ،
  مانند [filelog](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/kernel-monitor-filelog.json)،
  [kmsg](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/kernel-monitor.json)،
  [kernel](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/kernel-monitor-counter.json)،
  [abrt](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/abrt-adaptor.json)
  و [systemd](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/systemd-monitor-counter.json)، سفارشی کنید.

- دیمن‌های نوع `SystemStatsMonitor` آمارهای گوناگون مرتبط با سلامت سیستم را به‌صورت متریک جمع‌آوری می‌کنند.
  می‌توانید رفتار این دیمن را با به‌روزرسانی
  [فایل پیکربندی](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/system-stats-monitor.json) آن سفارشی کنید.

- دیمن‌های نوع `CustomPluginMonitor` با اجرای اسکریپت‌های تعریف‌شده توسط کاربر، مشکلات گوناگون نود را
  فراخوانی و بررسی می‌کنند. می‌توانید از پایشگرهای افزونه‌ی سفارشی مختلف برای پایش مشکلات
  مختلف استفاده کنید و رفتار دیمن را با به‌روزرسانی
  [فایل پیکربندی](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/custom-plugin-monitor.json) سفارشی کنید.

- دیمن‌های نوع `HealthChecker` سلامت kubelet و محیط اجرای کانتینر را روی نود بررسی می‌کنند.

### افزودن پشتیبانی از قالب‌های دیگر لاگ {#support-other-log-format}

پایشگر لاگ سیستم در حال حاضر از لاگ‌های مبتنی بر فایل، journald و kmsg پشتیبانی می‌کند.
با پیاده‌سازی یک
[ناظر لاگ (log watcher)](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/pkg/systemlogmonitor/logwatchers/types/log_watcher.go) جدید
می‌توان منابع دیگری نیز افزود.

### افزودن پایشگرهای افزونه‌ی سفارشی

می‌توانید با توسعه‌ی یک افزونه‌ی سفارشی، آشکارساز مشکلات نود را طوری گسترش دهید که هر اسکریپت پایشی را،
به هر زبانی که نوشته شده باشد، اجرا کند. اسکریپت‌های پایش باید از نظر کد خروج و خروجی استاندارد
با پروتکل افزونه سازگار باشند. برای اطلاعات بیشتر، به
[پیشنهاد رابط افزونه](https://docs.google.com/document/d/1jK_5YloSYtboj-DtfjmYKxfNnUxCAvohLnsH5aGCAYQ/edit#) مراجعه کنید.

## صادرکننده

صادرکننده (exporter) مشکلات و/یا متریک‌های نود را به بک‌اندهای مشخصی گزارش می‌دهد.
صادرکننده‌های زیر پشتیبانی می‌شوند:

- **صادرکننده‌ی Kubernetes**: این صادرکننده مشکلات نود را به API server کوبرنتیز گزارش می‌دهد.
  مشکلات موقت به‌صورت Event و مشکلات دائمی به‌صورت Condition نود گزارش می‌شوند.

- **صادرکننده‌ی Prometheus**: این صادرکننده مشکلات و متریک‌های نود را به‌صورت محلی، در قالب متریک‌های Prometheus
  (یا OpenMetrics)، گزارش می‌دهد. می‌توانید نشانی IP و پورت این صادرکننده را با آرگومان‌های
  خط فرمان مشخص کنید.

- **صادرکننده‌ی Stackdriver**: این صادرکننده مشکلات و متریک‌های نود را به Stackdriver
  Monitoring API گزارش می‌دهد. رفتار صادرکردن را می‌توان با یک
  [فایل پیکربندی](https://github.com/kubernetes/node-problem-detector/blob/v0.8.12/config/exporter/stackdriver-exporter.json) سفارشی کرد.

<!-- discussion -->

## توصیه‌ها و محدودیت‌ها

توصیه می‌شود آشکارساز مشکلات نود را برای پایش سلامت نودها در کلاستر خود اجرا کنید.
هنگام اجرای آشکارساز مشکلات نود، باید انتظار سربار منابع اضافه‌ای را روی هر نود داشته باشید.
معمولاً این سربار مشکلی ایجاد نمی‌کند، زیرا:

* لاگ کرنل نسبتاً آهسته رشد می‌کند.
* برای آشکارساز مشکلات نود محدودیت منابع تعیین شده است.
* حتی در بار زیاد نیز مصرف منابع در حد قابل‌قبول است. برای اطلاعات بیشتر، به
  [نتیجه‌ی بنچمارک](https://github.com/kubernetes/node-problem-detector/issues/2#issuecomment-220255629) آشکارساز مشکلات نود مراجعه کنید.
