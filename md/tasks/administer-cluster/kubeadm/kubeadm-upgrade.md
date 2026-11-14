---
reviewers:
- sig-cluster-lifecycle
title: ارتقای کلاسترهای kubeadm
content_type: task
weight: 30
---

<!-- overview -->

این صفحه توضیح می‌دهد که چگونه یک کلاستر کوبرنتیز ایجادشده با kubeadm را از نسخهٔ
{{< skew currentVersionAddMinor -1 >}}.x به نسخهٔ {{< skew currentVersion >}}.x و همچنین از نسخهٔ
{{< skew currentVersion >}}.x به {{< skew currentVersion >}}.y (که در آن `y > x`) ارتقا دهید. رد شدن از نسخه‌های MINOR
در هنگام ارتقا پشتیبانی نمی‌شود. برای جزئیات بیشتر، به [سیاست اختلاف نسخه (Version Skew Policy)](/releases/version-skew-policy/) مراجعه کنید.

برای دیدن اطلاعات مربوط به ارتقای کلاسترهایی که با نسخه‌های قدیمی‌تر kubeadm ایجاد شده‌اند،
به صفحه‌های زیر مراجعه کنید:

- [ارتقای کلاستر kubeadm از {{< skew currentVersionAddMinor -2 >}} به {{< skew currentVersionAddMinor -1 >}}](https://v{{< skew currentVersionAddMinor -1 "-" >}}.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [ارتقای کلاستر kubeadm از {{< skew currentVersionAddMinor -3 >}} به {{< skew currentVersionAddMinor -2 >}}](https://v{{< skew currentVersionAddMinor -2 "-" >}}.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [ارتقای کلاستر kubeadm از {{< skew currentVersionAddMinor -4 >}} به {{< skew currentVersionAddMinor -3 >}}](https://v{{< skew currentVersionAddMinor -3 "-" >}}.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [ارتقای کلاستر kubeadm از {{< skew currentVersionAddMinor -5 >}} به {{< skew currentVersionAddMinor -4 >}}](https://v{{< skew currentVersionAddMinor -4 "-" >}}.docs.kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

پروژهٔ کوبرنتیز توصیه می‌کند که بی‌درنگ به آخرین انتشارهای وصله‌ای (patch) ارتقا دهید و
اطمینان حاصل کنید که یک انتشار فرعی (minor) پشتیبانی‌شده از کوبرنتیز را اجرا می‌کنید.
پیروی از این توصیه به حفظ امنیت شما کمک می‌کند.

روند کلی ارتقا به شرح زیر است:

1. ارتقای نود اصلی control plane.
1. ارتقای نودهای control plane دیگر.
1. ارتقای نودهای کارگر (worker).

## {{% heading "prerequisites" %}}

- حتماً [یادداشت‌های انتشار](https://git.k8s.io/kubernetes/CHANGELOG) را با دقت بخوانید.
- کلاستر باید از control plane ایستا و پادهای etcd یا etcd خارجی استفاده کند.
- از همهٔ اجزای مهم، مانند وضعیت سطح برنامه که در پایگاه داده ذخیره شده است، نسخهٔ پشتیبان تهیه کنید.
  دستور `kubeadm upgrade` به بارهای کاری شما دست نمی‌زند و فقط اجزای داخلی کوبرنتیز را تغییر می‌دهد، اما تهیهٔ نسخهٔ پشتیبان همیشه یک رویهٔ توصیه‌شده است.
- [Swap باید غیرفعال باشد](https://serverfault.com/questions/684771/best-way-to-disable-swap-in-linux).

### اطلاعات تکمیلی

- دستورالعمل‌های زیر مشخص می‌کنند که در طول فرایند ارتقا، هر نود را چه زمانی باید تخلیه (drain) کنید.
  اگر ارتقای نسخهٔ **فرعی** را برای هر kubelet انجام می‌دهید، **باید**
  ابتدا نود (یا نودهایی) را که ارتقا می‌دهید تخلیه کنید. ممکن است روی نودهای control plane
  پادهای CoreDNS یا بارهای کاری حیاتی دیگری در حال اجرا باشند. برای اطلاعات بیشتر،
  [تخلیهٔ نودها](/docs/tasks/administer-cluster/safely-drain-node/) را ببینید.
- پروژهٔ کوبرنتیز توصیه می‌کند که نسخه‌های kubelet و kubeadm با هم یکسان باشند.
  به‌جای این کار می‌توانید از نسخه‌ای از kubelet استفاده کنید که از kubeadm قدیمی‌تر است، به شرط آنکه
  در محدودهٔ نسخه‌های پشتیبانی‌شده قرار داشته باشد.
  برای جزئیات بیشتر، به [اختلاف نسخهٔ kubeadm با kubelet](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#kubeadm-s-skew-against-the-kubelet) مراجعه کنید.
- همهٔ کانتینرها پس از ارتقا دوباره راه‌اندازی می‌شوند، زیرا مقدار هش مشخصات (spec) کانتینر تغییر می‌کند.
- برای اطمینان از اینکه سرویس kubelet پس از ارتقا با موفقیت دوباره راه‌اندازی شده است،
  می‌توانید دستور `systemctl status kubelet` را اجرا کنید یا لاگ‌های سرویس را با `journalctl -xeu kubelet` ببینید.
- دستور `kubeadm upgrade` از فلگ `--config` همراه با
[نوع API `UpgradeConfiguration`](/docs/reference/config-api/kubeadm-config.v1beta4) پشتیبانی می‌کند که با آن
می‌توان فرایند ارتقا را پیکربندی کرد.
- دستور `kubeadm upgrade` از پیکربندی مجدد یک کلاستر موجود پشتیبانی نمی‌کند. برای این کار، مراحل
  [پیکربندی مجدد کلاستر kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure) را دنبال کنید.

### ملاحظات ارتقای etcd

از آنجا که پاد ایستای `kube-apiserver` همواره در حال اجراست (حتی اگر
نود را تخلیه کرده باشید)، هنگامی که ارتقایی با kubeadm انجام می‌دهید که شامل
ارتقای etcd نیز هست، درخواست‌های در حال پردازش به سرور، در مدتی که پاد ایستای جدید etcd
در حال راه‌اندازی مجدد است، متوقف می‌مانند. برای دور زدن این مشکل، می‌توان فرایند
`kube-apiserver` را چند ثانیه پیش از اجرای دستور `kubeadm upgrade
apply` به‌طور فعال متوقف کرد. با این کار، درخواست‌های در حال پردازش تکمیل و اتصال‌های موجود
بسته می‌شوند و پیامدهای از دسترس خارج شدن etcd به حداقل می‌رسد. این کار را می‌توان
به‌صورت زیر روی نودهای control plane انجام داد:

```shell
killall -s SIGTERM kube-apiserver # trigger a graceful kube-apiserver shutdown
sleep 20 # wait a little bit to permit completing in-flight requests
kubeadm upgrade ... # execute a kubeadm upgrade command
```

<!-- steps -->

## تغییر مخزن بسته‌ها

اگر از مخازن بستهٔ متعلق به جامعه (`pkgs.k8s.io`) استفاده می‌کنید، باید
مخزن بسته را برای انتشار فرعی موردنظر کوبرنتیز فعال کنید. این موضوع در سند
[تغییر مخزن بستهٔ کوبرنتیز](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
توضیح داده شده است.

{{% legacy-repos-deprecation %}}

## تعیین نسخهٔ مقصد ارتقا

آخرین انتشار وصله‌ای کوبرنتیز {{< skew currentVersion >}} را با استفاده از مدیر بستهٔ سیستم‌عامل پیدا کنید:

{{< tabs name="k8s_install_versions" >}}
{{% tab name="Ubuntu، Debian یا HypriotOS" %}}

```shell
# Find the latest {{< skew currentVersion >}} version in the list.
# It should look like {{< skew currentVersion >}}.x-*, where x is the latest patch.
sudo apt update
sudo apt-cache madison kubeadm
```

{{% /tab %}}
{{% tab name="CentOS، RHEL یا Fedora" %}}

برای سیستم‌های دارای DNF4 (Fedora < 41، RHEL/CentOS < 10):
```shell
# Find the latest {{< skew currentVersion >}} version in the list.
# It should look like {{< skew currentVersion >}}.x-*, where x is the latest patch.
sudo dnf list --showduplicates kubeadm --disableexcludes=kubernetes
```
برای سیستم‌های دارای DNF5:
```shell
# Find the latest {{< skew currentVersion >}} version in the list.
# It should look like {{< skew currentVersion >}}.x-*, where x is the latest patch.
sudo dnf list --showduplicates kubeadm --setopt=disable_excludes=kubernetes
```

{{% /tab %}}
{{< /tabs >}}

اگر نسخه‌ای را که انتظار دارید به آن ارتقا دهید نمی‌بینید، [بررسی کنید که آیا از مخازن بستهٔ کوبرنتیز استفاده می‌شود.](/docs/tasks/administer-cluster/kubeadm/change-package-repository/#verifying-if-the-kubernetes-package-repositories-are-used)

## ارتقای نودهای control plane

روند ارتقا روی نودهای control plane باید هر بار روی یک نود انجام شود.
نودی از control plane را که می‌خواهید ابتدا ارتقا دهید انتخاب کنید. این نود باید فایل `/etc/kubernetes/admin.conf` را داشته باشد.

### فراخوانی «kubeadm upgrade»

**برای نخستین نود control plane**

1. ارتقای kubeadm:

   {{< tabs name="k8s_install_kubeadm_first_cp" >}}
   {{% tab name="Ubuntu، Debian یا HypriotOS" %}}

   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo apt-mark unhold kubeadm && \
   sudo apt-get update && sudo apt-get install -y kubeadm='{{< skew currentVersion >}}.x-*' && \
   sudo apt-mark hold kubeadm
   ```

   {{% /tab %}}
   {{% tab name="CentOS، RHEL یا Fedora" %}}

   برای سیستم‌های دارای DNF4 (Fedora < 41، RHEL/CentOS < 10):
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo dnf install -y kubeadm-'{{< skew currentVersion >}}.x-*' --disableexcludes=kubernetes
   ```
   برای سیستم‌های دارای DNF5:
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo dnf install -y kubeadm-'{{< skew currentVersion >}}.x-*' --setopt=disable_excludes=kubernetes
   ```

   {{% /tab %}}
   {{< /tabs >}}

1. بررسی کنید که دانلود به‌درستی انجام شده و نسخهٔ موردانتظار را دارد:

   ```shell
   kubeadm version
   ```

1. برنامهٔ ارتقا را بررسی کنید:

   ```shell
   sudo kubeadm upgrade plan
   ```

   این دستور بررسی می‌کند که آیا کلاستر شما قابل ارتقاست و نسخه‌هایی را که می‌توانید به آن‌ها ارتقا دهید دریافت می‌کند.
   همچنین جدولی از وضعیت نسخه‌های پیکربندی اجزا نمایش می‌دهد.

   {{< note >}}
   دستور `kubeadm upgrade` گواهی‌هایی را که روی این نود مدیریت می‌کند نیز به‌طور خودکار تمدید می‌کند.
   برای انصراف از تمدید گواهی‌ها می‌توانید از فلگ `--certificate-renewal=false` استفاده کنید.
   برای اطلاعات بیشتر، [راهنمای مدیریت گواهی‌ها](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs) را ببینید.
   {{</ note >}}

1. نسخه‌ای را برای ارتقا انتخاب کنید و دستور مناسب را اجرا کنید. برای نمونه:

   ```shell
   # replace x with the patch version you picked for this upgrade
   sudo kubeadm upgrade apply v{{< skew currentVersion >}}.x
   ```

   پس از پایان اجرای دستور، باید خروجی زیر را ببینید:

   ```
   [upgrade/successful] SUCCESS! Your cluster was upgraded to "v{{< skew currentVersion >}}.x". Enjoy!

   [upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.
   ```

   {{< note >}}
   در نسخه‌های پیش از v1.28، حالت پیش‌فرض kubeadm این بود که افزونه‌ها (از جمله CoreDNS و kube-proxy) را
   بلافاصله در طول اجرای `kubeadm upgrade apply` ارتقا دهد، صرف‌نظر از اینکه نمونه‌های دیگری از control plane
   وجود داشته باشند که هنوز ارتقا نیافته‌اند. این رفتار ممکن است مشکلات سازگاری ایجاد کند. از نسخهٔ v1.28 به بعد،
   حالت پیش‌فرض kubeadm این است که پیش از آغاز ارتقای افزونه‌ها بررسی کند که آیا همهٔ نمونه‌های control plane
   ارتقا یافته‌اند یا نه. شما باید نمونه‌های control plane را به‌ترتیب ارتقا دهید، یا دست‌کم اطمینان حاصل کنید که
   ارتقای آخرین نمونهٔ control plane تا زمانی که همهٔ نمونه‌های دیگر control plane به‌طور کامل ارتقا نیافته‌اند آغاز نشود.
   ارتقای افزونه‌ها پس از ارتقای آخرین نمونهٔ control plane انجام خواهد شد.
   {{</ note >}}

1. افزونهٔ ارائه‌دهندهٔ CNI خود را به‌صورت دستی ارتقا دهید.

   ممکن است ارائه‌دهندهٔ رابط شبکهٔ کانتینر (CNI) شما دستورالعمل‌های ارتقای مخصوص به خود را داشته باشد.
   صفحهٔ [افزونه‌ها](/docs/concepts/cluster-administration/addons/) را بررسی کنید تا
   ارائه‌دهندهٔ CNI خود را پیدا کنید و ببینید آیا مراحل ارتقای اضافی لازم است یا نه.

   اگر ارائه‌دهندهٔ CNI به‌صورت DaemonSet اجرا می‌شود، این مرحله روی نودهای control plane دیگر لازم نیست.

**برای نودهای control plane دیگر**

مانند نخستین نود control plane عمل کنید، اما به‌جای دستور:

```shell
sudo kubeadm upgrade node
```

از دستور زیر استفاده نکنید، بلکه برعکس؛ یعنی دستور بالا را به‌جای دستور زیر به کار ببرید:

```shell
sudo kubeadm upgrade apply
```

همچنین دیگر نیازی به فراخوانی `kubeadm upgrade plan` و ارتقای افزونهٔ ارائه‌دهندهٔ CNI نیست.

### تخلیهٔ نود

نود را با علامت‌گذاری آن به‌عنوان غیرقابل‌زمان‌بندی و بیرون راندن بارهای کاری، برای نگهداری آماده کنید:

```shell
# replace <node-to-drain> with the name of your node you are draining
kubectl drain <node-to-drain> --ignore-daemonsets
```

### ارتقای kubelet و kubectl

{{< note >}}
روی نودهای لینوکسی، kubelet به‌طور پیش‌فرض فقط از cgroups v2 پشتیبانی می‌کند.
در کوبرنتیز {{< skew currentVersion >}}، گزینهٔ پیکربندی `FailCgroupV1` در kubelet به‌طور پیش‌فرض روی `true` تنظیم شده است.

برای آشنایی بیشتر، به [مستندات منسوخ شدن cgroup v1 در کوبرنتیز](/docs/concepts/architecture/cgroups/#deprecation-of-cgroup-v1) مراجعه کنید.
{{</ note >}}

1. ارتقای kubelet و kubectl:

   {{< tabs name="k8s_install_kubelet" >}}
   {{% tab name="Ubuntu، Debian یا HypriotOS" %}}

   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo apt-mark unhold kubelet kubectl && \
   sudo apt-get update && sudo apt-get install -y kubelet='{{< skew currentVersion >}}.x-*' kubectl='{{< skew currentVersion >}}.x-*' && \
   sudo apt-mark hold kubelet kubectl
   ```

   {{% /tab %}}
   {{% tab name="CentOS، RHEL یا Fedora" %}}

   برای سیستم‌های دارای DNF4 (Fedora < 41، RHEL/CentOS < 10):
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo dnf install -y kubelet-'{{< skew currentVersion >}}.x-*' kubectl-'{{< skew currentVersion >}}.x-*' --disableexcludes=kubernetes
   ```
   برای سیستم‌های دارای DNF5:
   ```shell
   # replace x in {{< skew currentVersion >}}.x-* with the latest patch version
   sudo dnf install -y kubelet-'{{< skew currentVersion >}}.x-*' kubectl-'{{< skew currentVersion >}}.x-*' --setopt=disable_excludes=kubernetes
   ```

   {{% /tab %}}
   {{< /tabs >}}

1. kubelet را دوباره راه‌اندازی کنید:

   ```shell
   sudo systemctl daemon-reload
   sudo systemctl restart kubelet
   ```

### خارج کردن نود از حالت cordon

نود را با علامت‌گذاری آن به‌عنوان قابل‌زمان‌بندی، دوباره به چرخهٔ کار بازگردانید:

```shell
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```

## ارتقای نودهای کارگر

روند ارتقا روی نودهای کارگر باید هر بار روی یک نود یا چند نود انجام شود،
به‌گونه‌ای که حداقل ظرفیت لازم برای اجرای بارهای کاری شما به خطر نیفتد.

صفحه‌های زیر نحوهٔ ارتقای نودهای کارگر لینوکس و ویندوز را نشان می‌دهند:

* [ارتقای نودهای لینوکس](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
* [ارتقای نودهای ویندوز](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)

## بررسی وضعیت کلاستر

پس از ارتقای kubelet روی همهٔ نودها، با اجرای دستور زیر از هر جایی که kubectl به کلاستر
دسترسی دارد، بررسی کنید که همهٔ نودها دوباره در دسترس هستند:

```shell
kubectl get nodes
```

ستون `STATUS` باید برای همهٔ نودهای شما مقدار `Ready` را نشان دهد و شمارهٔ نسخه نیز باید به‌روز شده باشد.

## بازیابی از وضعیت خرابی

اگر `kubeadm upgrade` با شکست مواجه شود و به وضعیت قبلی بازنگردد، برای نمونه به دلیل خاموش شدن غیرمنتظره در حین اجرا، می‌توانید `kubeadm upgrade` را دوباره اجرا کنید.
این دستور خودتوان (idempotent) است و در نهایت اطمینان حاصل می‌کند که وضعیت واقعی با وضعیت مطلوبی که اعلام کرده‌اید یکسان باشد.

برای بازیابی از یک وضعیت نامناسب، می‌توانید `sudo kubeadm upgrade apply --force` را نیز بدون تغییر نسخه‌ای که کلاستر شما اجرا می‌کند، اجرا کنید.

در طول ارتقا، kubeadm پوشه‌های پشتیبان زیر را در مسیر `/etc/kubernetes/tmp` می‌نویسد:

- `kubeadm-backup-etcd-<date>-<time>`
- `kubeadm-backup-manifests-<date>-<time>`

پوشهٔ `kubeadm-backup-etcd` حاوی نسخهٔ پشتیبانی از داده‌های عضو محلی etcd برای این نود control plane است.
در صورت شکست ارتقای etcd و کار نکردن بازگشت خودکار، می‌توان محتوای این پوشه را
به‌صورت دستی در `/var/lib/etcd` بازیابی کرد. اگر از etcd خارجی استفاده شود، این پوشهٔ پشتیبان خالی خواهد بود.

پوشهٔ `kubeadm-backup-manifests` حاوی نسخهٔ پشتیبانی از فایل‌های مانیفست پادهای ایستا برای این نود control plane است.
در صورت شکست ارتقا و کار نکردن بازگشت خودکار، می‌توان محتوای این پوشه را
به‌صورت دستی در `/etc/kubernetes/manifests` بازیابی کرد. اگر به هر دلیلی فایل مانیفست یک جزء خاص پیش و پس از ارتقا
تفاوتی نداشته باشد، فایل پشتیبانی برای آن نوشته نخواهد شد.

{{< note >}}
پس از ارتقای کلاستر با kubeadm، پوشهٔ پشتیبان `/etc/kubernetes/tmp` باقی می‌ماند و
این فایل‌های پشتیبان باید به‌صورت دستی پاک شوند.
{{</ note >}}

## سازوکار

دستور `kubeadm upgrade apply` کارهای زیر را انجام می‌دهد:

- بررسی می‌کند که کلاستر شما در وضعیتی قابل ارتقا باشد:
  - سرور API در دسترس باشد
  - همهٔ نودها در وضعیت `Ready` باشند
  - وضعیت control plane سالم باشد
- سیاست‌های اختلاف نسخه را اعمال می‌کند.
- اطمینان حاصل می‌کند که ایمیج‌های control plane روی ماشین موجود باشند یا قابل دریافت باشند.
- اگر پیکربندی‌های اجزا به ارتقای نسخه نیاز داشته باشند، جایگزین‌هایی تولید می‌کند و/یا از مقادیر جایگزین ارائه‌شده توسط کاربر استفاده می‌کند.
- اجزای control plane را ارتقا می‌دهد، یا اگر هر یک از آن‌ها بالا نیاید، به وضعیت قبلی بازمی‌گرداند.
- مانیفست‌های جدید `CoreDNS` و `kube-proxy` را اعمال می‌کند و اطمینان حاصل می‌کند که همهٔ قوانین RBAC لازم ایجاد شده باشند.
- گواهی‌های مدیریت‌شده توسط kubeadm را که اجزای control plane از آن‌ها استفاده می‌کنند، هم‌زمان با ارتقای این اجزا و با استفاده از گواهی و کلید CA محلی تمدید می‌کند. تمدید گواهی‌ها به‌طور پیش‌فرض فعال است؛ برای غیرفعال کردن آن از `--certificate-renewal=false` استفاده کنید.

دستور `kubeadm upgrade node` روی نودهای control plane دیگر کارهای زیر را انجام می‌دهد:

- پیکربندی `ClusterConfiguration` مربوط به kubeadm را از کلاستر دریافت می‌کند.
- گواهی‌های مدیریت‌شده توسط kubeadm را که اجزای control plane از آن‌ها استفاده می‌کنند، هم‌زمان با ارتقای این اجزا و با استفاده از گواهی و کلید CA محلی تمدید می‌کند. تمدید گواهی‌ها به‌طور پیش‌فرض فعال است؛ برای غیرفعال کردن آن از `--certificate-renewal=false` استفاده کنید.
- مانیفست‌های پادهای ایستای اجزای control plane را ارتقا می‌دهد.
- پیکربندی kubelet را برای این نود ارتقا می‌دهد.

دستور `kubeadm upgrade node` روی نودهای کارگر کارهای زیر را انجام می‌دهد:

- پیکربندی `ClusterConfiguration` مربوط به kubeadm را از کلاستر دریافت می‌کند.
- پیکربندی kubelet را برای این نود ارتقا می‌دهد.
