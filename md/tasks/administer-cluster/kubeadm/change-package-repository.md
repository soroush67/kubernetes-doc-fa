---
title: تغییر مخزن بسته‌های کوبرنتیز
content_type: task
weight: 150
---

<!-- overview -->

این صفحه توضیح می‌دهد که هنگام ارتقای یک کلاستر، چگونه مخزن بسته (package repository) مربوط به نسخهٔ فرعی (minor release) موردنظر کوبرنتیز را فعال کنید. این کار فقط برای کاربرانی لازم است که از مخازن بستهٔ متعلق به جامعه که در `pkgs.k8s.io` میزبانی می‌شوند استفاده می‌کنند.
برخلاف مخازن بستهٔ قدیمی، مخازن بستهٔ متعلق به جامعه به‌گونه‌ای سازمان‌دهی شده‌اند که برای هر نسخهٔ فرعی کوبرنتیز یک مخزن بستهٔ اختصاصی وجود دارد.

{{< note >}}
این راهنما فقط بخشی از فرایند ارتقای کوبرنتیز را پوشش می‌دهد. برای اطلاعات بیشتر دربارهٔ ارتقای کلاسترهای کوبرنتیز، به [راهنمای ارتقا](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) مراجعه کنید.
{{</ note >}}

{{< note >}}
این مرحله فقط هنگام ارتقای کلاستر به یک نسخهٔ **فرعی** دیگر لازم است.
اگر به نسخهٔ وصلهٔ (patch release) دیگری در همان نسخهٔ فرعی ارتقا می‌دهید (برای مثال از
v{{< skew currentVersion >}}.5 به v{{< skew currentVersion >}}.7)، نیازی به دنبال کردن این راهنما ندارید. با این حال، اگر هنوز از مخازن بستهٔ قدیمی استفاده می‌کنید، باید پیش از ارتقا به مخازن بستهٔ جدید متعلق به جامعه مهاجرت کنید (برای جزئیات بیشتر دربارهٔ نحوهٔ انجام این کار، بخش بعدی را ببینید).
{{</ note >}}

## {{% heading "prerequisites" %}}

این سند فرض می‌کند که شما هم‌اکنون از مخازن بستهٔ متعلق به جامعه (`pkgs.k8s.io`) استفاده می‌کنید. در غیر این صورت، اکیداً توصیه می‌شود همان‌طور که در [اطلاعیهٔ رسمی](/blog/2023/08/15/pkgs-k8s-io-introduction/) توضیح داده شده است، به مخازن بستهٔ متعلق به جامعه مهاجرت کنید.

{{% legacy-repos-deprecation %}}

### بررسی استفاده از مخازن بستهٔ کوبرنتیز

اگر مطمئن نیستید که از مخازن بستهٔ متعلق به جامعه استفاده می‌کنید یا از مخازن بستهٔ قدیمی، برای بررسی این موضوع مراحل زیر را انجام دهید:

{{< tabs name="k8s_install_versions" >}}
{{% tab name="Ubuntu، Debian یا HypriotOS" %}}

محتوای فایلی را که مخزن `apt` کوبرنتیز را تعریف می‌کند چاپ کنید:

```shell
# On your system, this configuration file could have a different name
pager /etc/apt/sources.list.d/kubernetes.list
```

اگر خطی مشابه خط زیر می‌بینید:

```
deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/deb/ /
```

**یعنی از مخازن بستهٔ کوبرنتیز استفاده می‌کنید و این راهنما برای شما کاربرد دارد.**
در غیر این صورت، اکیداً توصیه می‌شود همان‌طور که در [اطلاعیهٔ رسمی](/blog/2023/08/15/pkgs-k8s-io-introduction/) توضیح داده شده است، به مخازن بستهٔ کوبرنتیز مهاجرت کنید.

{{% /tab %}}
{{% tab name="CentOS، RHEL یا Fedora" %}}

محتوای فایلی را که مخزن `yum` کوبرنتیز را تعریف می‌کند چاپ کنید:

```shell
# On your system, this configuration file could have a different name
cat /etc/yum.repos.d/kubernetes.repo
```

اگر مقدار `baseurl` مشابه `baseurl` در خروجی زیر است:

```
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl
```

**یعنی از مخازن بستهٔ کوبرنتیز استفاده می‌کنید و این راهنما برای شما کاربرد دارد.**
در غیر این صورت، اکیداً توصیه می‌شود همان‌طور که در [اطلاعیهٔ رسمی](/blog/2023/08/15/pkgs-k8s-io-introduction/) توضیح داده شده است، به مخازن بستهٔ کوبرنتیز مهاجرت کنید.

{{% /tab %}}

{{% tab name="openSUSE یا SLES" %}}

محتوای فایلی را که مخزن `zypper` کوبرنتیز را تعریف می‌کند چاپ کنید:

```shell
# On your system, this configuration file could have a different name
cat /etc/zypp/repos.d/kubernetes.repo
```

اگر مقدار `baseurl` مشابه `baseurl` در خروجی زیر است:

```
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl
```

**یعنی از مخازن بستهٔ کوبرنتیز استفاده می‌کنید و این راهنما برای شما کاربرد دارد.**
در غیر این صورت، اکیداً توصیه می‌شود همان‌طور که در [اطلاعیهٔ رسمی](/blog/2023/08/15/pkgs-k8s-io-introduction/) توضیح داده شده است، به مخازن بستهٔ کوبرنتیز مهاجرت کنید.

{{% /tab %}}
{{< /tabs >}}

{{< note >}}
نشانی (URL) مورد استفاده برای مخازن بستهٔ کوبرنتیز به `pkgs.k8s.io` محدود نیست و می‌تواند یکی از موارد زیر نیز باشد:

- `pkgs.k8s.io`
- `pkgs.kubernetes.io`
- `packages.kubernetes.io`
{{</ note >}}

<!-- steps -->

## جابه‌جایی به مخزن بستهٔ دیگری از کوبرنتیز

این مرحله باید هنگام ارتقا از یک نسخهٔ فرعی کوبرنتیز به نسخهٔ فرعی دیگر انجام شود تا به بسته‌های نسخهٔ فرعی موردنظر کوبرنتیز دسترسی داشته باشید.

{{< tabs name="k8s_upgrade_versions" >}}
{{% tab name="Ubuntu، Debian یا HypriotOS" %}}

1. فایلی را که مخزن `apt` کوبرنتیز را تعریف می‌کند با ویرایشگر متنی دلخواه خود باز کنید:

   ```shell
   nano /etc/apt/sources.list.d/kubernetes.list
   ```

   باید یک خط ببینید که نشانی آن شامل نسخهٔ فرعی فعلی کوبرنتیز شماست. برای مثال، اگر از v{{< skew currentVersionAddMinor -1 "." >}} استفاده می‌کنید، باید خط زیر را ببینید:

   ```
   deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/deb/ /
   ```

1. نسخهٔ موجود در نشانی را به **نسخهٔ فرعی بعدیِ موجود** تغییر دهید؛ برای مثال:

   ```
   deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/deb/ /
   ```

1. فایل را ذخیره کنید و از ویرایشگر متنی خارج شوید. سپس دنبال کردن دستورالعمل‌های ارتقای مربوط را ادامه دهید.

{{% /tab %}}
{{% tab name="CentOS، RHEL یا Fedora" %}}

1. فایلی را که مخزن `yum` کوبرنتیز را تعریف می‌کند با ویرایشگر متنی دلخواه خود باز کنید:

   ```shell
   nano /etc/yum.repos.d/kubernetes.repo
   ```

   باید فایلی ببینید که دو نشانی آن شامل نسخهٔ فرعی فعلی کوبرنتیز شماست. برای مثال، اگر از v{{< skew currentVersionAddMinor -1 "." >}} استفاده می‌کنید، باید محتوای زیر را ببینید:

   ```
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v{{< skew currentVersionAddMinor -1 "." >}}/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   ```

1. نسخهٔ موجود در این نشانی‌ها را به **نسخهٔ فرعی بعدیِ موجود** تغییر دهید؛ برای مثال:

   ```
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/{{< param "version" >}}/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   ```

1. فایل را ذخیره کنید و از ویرایشگر متنی خارج شوید. سپس دنبال کردن دستورالعمل‌های ارتقای مربوط را ادامه دهید.

{{% /tab %}}
{{< /tabs >}}

## {{% heading "whatsnext" %}}

* نحوهٔ [ارتقای نودهای لینوکس](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/) را ببینید.
* نحوهٔ [ارتقای نودهای ویندوز](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/) را ببینید.
