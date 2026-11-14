---
title: مهاجرت عامل‌های تله‌متری و امنیتی از dockershim
content_type: task 
reviewers:
- SergeyKanzhelev
weight: 60
---

<!-- overview -->

{{% thirdparty-content %}}

پشتیبانی کوبرنتیز از یکپارچه‌سازی مستقیم با Docker Engine منسوخ و سپس حذف شده است. بیشتر برنامه‌ها وابستگی مستقیمی به محیط اجرایی‌ای که کانتینرها را میزبانی می‌کند ندارند. با این حال، هنوز بسیاری از عامل‌های تله‌متری و پایش برای جمع‌آوری فراداده، لاگ‌ها و متریک‌های کانتینرها به Docker وابسته‌اند. این سند اطلاعاتی را درباره‌ی شیوه‌ی شناسایی این وابستگی‌ها گردآوری کرده و پیوندهایی را برای مهاجرت این عامل‌ها به ابزارهای عمومی یا محیط‌های اجرای جایگزین ارائه می‌دهد.

## عامل‌های تله‌متری و امنیتی

درون یک کلاستر کوبرنتیز، چند روش مختلف برای اجرای عامل‌های تله‌متری یا امنیتی وجود دارد. برخی از این عامل‌ها هنگامی که به‌صورت DaemonSet یا مستقیماً روی نودها اجرا می‌شوند، به Docker Engine وابستگی مستقیم دارند.

### چرا برخی عامل‌های تله‌متری با Docker Engine ارتباط برقرار می‌کنند؟

کوبرنتیز در آغاز به‌طور خاص برای کار با Docker Engine نوشته شده بود. کوبرنتیز شبکه و زمان‌بندی را بر عهده داشت و برای راه‌اندازی و اجرای کانتینرها (درون پادها) روی هر نود به Docker Engine متکی بود. برخی اطلاعات مرتبط با تله‌متری، مانند نام پاد، فقط از طریق مؤلفه‌های کوبرنتیز در دسترس است. برخی داده‌های دیگر، مانند متریک‌های کانتینر، بر عهده‌ی محیط اجرای کانتینر نیست. به همین دلیل، عامل‌های تله‌متری اولیه برای ارائه‌ی تصویری دقیق باید هم از محیط اجرای کانتینر *و هم* از کوبرنتیز پرس‌وجو می‌کردند. به‌مرور زمان، کوبرنتیز توانایی پشتیبانی از چند محیط اجرا را به دست آورد و اکنون از هر محیط اجرایی که با [رابط محیط اجرای کانتینر](/docs/concepts/architecture/cri/) سازگار باشد پشتیبانی می‌کند.

برخی عامل‌های تله‌متری به‌طور خاص به ابزارهای Docker Engine متکی‌اند. برای مثال، یک عامل ممکن است برای فهرست کردن کانتینرها و فرایندها فرمانی مانند
[`docker ps`](https://docs.docker.com/engine/reference/commandline/ps/)
یا [`docker top`](https://docs.docker.com/engine/reference/commandline/top/) را اجرا کند، یا برای دریافت جریانی لاگ‌ها از [`docker logs`](https://docs.docker.com/engine/reference/commandline/logs/) استفاده کند. اگر نودهای کلاستر فعلی شما از Docker Engine استفاده می‌کنند و به محیط اجرای کانتینر دیگری روی بیاورید، این فرمان‌ها دیگر کار نخواهند کرد.

### شناسایی DaemonSetهایی که به Docker Engine وابسته‌اند {#identify-docker-dependency}

اگر پادی بخواهد `dockerd` در حال اجرا روی نود را فراخوانی کند، باید یکی از این دو کار را انجام دهد:

- سامانه‌ی فایلی را که سوکت ممتاز (privileged) دیمن Docker در آن قرار دارد، به‌صورت یک
  {{< glossary_tooltip text="حجم (volume)" term_id="volume" >}} مانت کند؛ یا
- مسیر مشخص سوکت ممتاز دیمن Docker را مستقیماً، آن هم به‌صورت یک حجم، مانت کند.

برای مثال، در ایمیج‌های COS، Docker سوکت دامنه‌ی یونیکس خود را در مسیر `/var/run/docker.sock` در دسترس قرار می‌دهد. یعنی مشخصات (spec) پاد شامل یک مانت حجم `hostPath` برای `/var/run/docker.sock` خواهد بود.

در ادامه نمونه‌ای از یک اسکریپت شل آمده است که پادهای دارای مانتی را پیدا می‌کند که مستقیماً به سوکت Docker نگاشت شده است. این اسکریپت فضای نام و نام پاد را در خروجی نمایش می‌دهد. برای بررسی سایر مانت‌ها می‌توانید بخش `grep '/var/run/docker.sock'` را حذف کنید.

```bash
kubectl get pods --all-namespaces \
-o=jsonpath='{range .items[*]}{"\n"}{.metadata.namespace}{":\t"}{.metadata.name}{":\t"}{range .spec.volumes[*]}{.hostPath.path}{", "}{end}{end}' \
| sort \
| grep '/var/run/docker.sock'
```

{{< note >}}
یک پاد از راه‌های دیگری نیز می‌تواند به Docker روی میزبان دسترسی پیدا کند. برای نمونه، ممکن است به‌جای مسیر کامل، پوشه‌ی والد یعنی `/var/run` مانت شود (مانند [این
نمونه](https://gist.github.com/itaysk/7bc3e56d69c4d72a549286d98fd557dd)).
اسکریپت بالا فقط رایج‌ترین موارد را شناسایی می‌کند.
{{< /note >}}

### شناسایی وابستگی به Docker در عامل‌های نود

اگر نودهای کلاستر شما سفارشی‌سازی شده‌اند و عامل‌های امنیتی و تله‌متری دیگری روی نود نصب می‌کنند، از فروشنده‌ی عامل بپرسید که آیا این عامل به Docker وابستگی دارد یا نه.

### فروشندگان عامل‌های تله‌متری و امنیتی

هدف این بخش گردآوری اطلاعات درباره‌ی عامل‌های گوناگون تله‌متری و امنیتی است که ممکن است به محیط‌های اجرای کانتینر وابسته باشند.

نسخه‌ی در حال تکمیل دستورالعمل‌های مهاجرت مربوط به فروشندگان مختلف عامل‌های تله‌متری و امنیتی را در [یک سند Google](https://docs.google.com/document/d/1ZFi4uKit63ga5sxEiZblfb-c23lFhvy6RXVPikS8wf0/edit#) نگهداری می‌کنیم.
برای دریافت دستورالعمل‌های به‌روز مهاجرت از dockershim، لطفاً با فروشنده تماس بگیرید.

## مهاجرت از dockershim

### [Aqua](https://www.aquasec.com)

به هیچ تغییری نیاز نیست: پس از تغییر محیط اجرا، همه‌چیز باید بدون مشکل کار کند.

### [Datadog](https://www.datadoghq.com/product/)

نحوه‌ی مهاجرت:
[منسوخ شدن Docker در کوبرنتیز](https://docs.datadoghq.com/agent/guide/docker-deprecation/)
نام پادی که به Docker Engine دسترسی دارد ممکن است شامل هر یک از موارد زیر باشد:

- `datadog-agent`
- `datadog`
- `dd-agent`

### [Dynatrace](https://www.dynatrace.com/)

نحوه‌ی مهاجرت:
[مهاجرت از متریک‌های مختص Docker به متریک‌های عمومی کانتینر در Dynatrace](https://community.dynatrace.com/t5/Best-practices/Migrating-from-Docker-only-to-generic-container-metrics-in/m-p/167030#M49)

اعلامیه‌ی پشتیبانی از containerd: [دستیابی خودکار به دید کامل (full-stack) در محیط‌های کوبرنتیز مبتنی بر containerd](https://www.dynatrace.com/news/blog/get-automated-full-stack-visibility-into-containerd-based-kubernetes-environments/)

اعلامیه‌ی پشتیبانی از CRI-O: [دستیابی خودکار به دید کامل در کانتینرهای کوبرنتیز مبتنی بر CRI-O (بتا)](https://www.dynatrace.com/news/blog/get-automated-full-stack-visibility-into-your-cri-o-kubernetes-containers-beta/)

نام پادی که به Docker دسترسی دارد ممکن است شامل این مورد باشد: 
- `dynatrace-oneagent`

### [Falco](https://falco.org)

نحوه‌ی مهاجرت:

[مهاجرت Falco از dockershim](https://falco.org/docs/getting-started/deployment/#docker-deprecation-in-kubernetes)
ابزار Falco از هر محیط اجرای سازگار با CRI پشتیبانی می‌کند (در پیکربندی پیش‌فرض از containerd استفاده می‌شود)؛ همه‌ی جزئیات در مستندات آن توضیح داده شده است.
نام پادی که به Docker دسترسی دارد ممکن است شامل این مورد باشد: 
- `falco`

### [Prisma Cloud Compute](https://docs.paloaltonetworks.com/prisma/prisma-cloud.html)

بخش «Install Prisma Cloud on a CRI (non-Docker) cluster» را در [مستندات Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/install/install_kubernetes.html) بررسی کنید.
نام پادی که به Docker دسترسی دارد ممکن است چیزی شبیه این باشد:
- `twistlock-defender-ds`

### [SignalFx (Splunk)](https://www.splunk.com/en_us/investor-relations/acquisitions/signalfx.html)

عامل SignalFx Smart Agent (منسوخ‌شده) برای کوبرنتیز از چند پایشگر (monitor) مختلف استفاده می‌کند، از جمله
`kubernetes-cluster`، `kubelet-stats/kubelet-metrics` و `docker-container-stats`.
پایشگر `kubelet-stats` پیش‌تر از سوی فروشنده به نفع `kubelet-metrics` منسوخ شده بود.
پایشگر `docker-container-stats` همان پایشگری است که حذف dockershim بر آن اثر می‌گذارد.
از `docker-container-stats` همراه با محیط‌های اجرای کانتینری به‌جز Docker Engine استفاده نکنید.


نحوه‌ی مهاجرت از عامل وابسته به dockershim:
1. پایشگر `docker-container-stats` را از فهرست [پایشگرهای پیکربندی‌شده](https://github.com/signalfx/signalfx-agent/blob/main/docs/monitor-config.md) حذف کنید.
   توجه کنید که اگر این پایشگر را همراه با محیط اجرایی غیر از dockershim فعال نگه دارید، در صورت نصب بودن docker روی نود متریک‌های نادرست گزارش می‌شود و در صورت نصب نبودن آن، هیچ متریکی گزارش نمی‌شود.
2. [پایشگر `kubelet-metrics` را فعال و پیکربندی کنید](https://github.com/signalfx/signalfx-agent/blob/main/docs/monitors/kubelet-metrics.md).


{{< note >}}
مجموعه‌ی متریک‌های جمع‌آوری‌شده تغییر خواهد کرد. قواعد هشدار و داشبوردهای خود را بازبینی کنید.
{{< /note >}}

نام پادی که به Docker دسترسی دارد ممکن است چیزی شبیه این باشد:

- `signalfx-agent`

### Yahoo Kubectl Flame

ابزار Flame از محیط‌های اجرای کانتینر به‌جز Docker پشتیبانی نمی‌کند. برای اطلاعات بیشتر،
[https://github.com/yahoo/kubectl-flame/issues/51](https://github.com/yahoo/kubectl-flame/issues/51) را ببینید.
