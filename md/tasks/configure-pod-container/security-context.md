---
reviewers:
- erictune
- mikedanese
- thockin
title: پیکربندی زمینهٔ امنیتی برای یک Pod یا کانتینر
content_type: task
weight: 110
---

<!-- overview -->

زمینهٔ امنیتی (security context) تنظیمات مربوط به سطح دسترسی و کنترل دسترسی یک Pod یا کانتینر را تعریف می‌کند. تنظیمات زمینهٔ امنیتی شامل موارد زیر است، اما به آن‌ها محدود نمی‌شود:

* کنترل دسترسی اختیاری (Discretionary Access Control): مجوز دسترسی به یک آبجکت، مانند یک فایل، بر اساس
  [شناسهٔ کاربر (UID) و شناسهٔ گروه (GID)](https://wiki.archlinux.org/index.php/users_and_groups) تعیین می‌شود.

* [لینوکس با امنیت تقویت‌شده (SELinux)](https://en.wikipedia.org/wiki/Security-Enhanced_Linux):
  به آبجکت‌ها برچسب‌های امنیتی اختصاص داده می‌شود.

* اجرا به‌صورت ممتاز (privileged) یا غیرممتاز.

* [قابلیت‌های لینوکس (Linux Capabilities)](https://linux-audit.com/linux-capabilities-hardening-linux-binaries-by-removing-setuid/):
  به یک فرایند برخی از امتیازها داده می‌شود، اما نه همهٔ امتیازهای کاربر root.

* [AppArmor](/docs/tutorials/security/apparmor/):
  با استفاده از پروفایل‌های برنامه، قابلیت‌های هر برنامه به‌طور جداگانه محدود می‌شود.

* [Seccomp](/docs/tutorials/security/seccomp/): فراخوانی‌های سیستمی یک فرایند فیلتر می‌شود.

* فیلد `allowPrivilegeEscalation`: تعیین می‌کند که آیا یک فرایند می‌تواند امتیازهایی بیش از فرایند والد خود به دست آورد یا نه؛ برای مثال با اجرای یک [فایل اجرایی setuid](https://en.wikipedia.org/wiki/Setuid).
  این مقدار بولی مستقیماً تعیین می‌کند که پرچم
  [`no_new_privs`](https://www.kernel.org/doc/Documentation/prctl/no_new_privs.txt)
  روی فرایند کانتینر تنظیم شود یا نه. البته توجه کنید که این مقدار وارونه است: اگر `allowPrivilegeEscalation` برابر true باشد، `no_new_privs` برابر false تنظیم خواهد شد.

  اگر `allowPrivilegeEscalation` در فیلد `securityContext` مشخصات یک کانتینر تعریف نشده باشد، مقدار پیش‌فرض آن true خواهد بود.

  مقدار `allowPrivilegeEscalation: false` با کانتینری که یکی از شرایط زیر را دارد ناسازگار است و بنابراین نمی‌توان آن را همراه با چنین کانتینری تنظیم کرد:

  - به‌صورت ممتاز اجرا می‌شود، یا
  - قابلیت `CAP_SYS_ADMIN` را دارد

* فیلد `readOnlyRootFilesystem`: فایل‌سیستم ریشهٔ کانتینر را به‌صورت فقط‌خواندنی mount می‌کند.

موارد بالا مجموعهٔ کاملی از تنظیمات زمینهٔ امنیتی نیستند؛ برای دیدن فهرست جامع، به
[SecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#securitycontext-v1-core)
مراجعه کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## تنظیم زمینهٔ امنیتی برای یک Pod

برای مشخص کردن تنظیمات امنیتی یک Pod، فیلد `securityContext` را در مشخصات Pod قرار دهید. فیلد `securityContext` یک آبجکت
[PodSecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podsecuritycontext-v1-core) است.
تنظیمات امنیتی‌ای که برای یک Pod مشخص می‌کنید، بر همهٔ کانتینرهای آن Pod اعمال می‌شوند.
در ادامه فایل پیکربندی یک Pod را می‌بینید که یک `securityContext` و یک حجم (volume) از نوع `emptyDir` دارد:

{{% code_sample file="pods/security/security-context.yaml" %}}

در این فایل پیکربندی، فیلد `runAsUser` مشخص می‌کند که در همهٔ کانتینرهای Pod، تمام فرایندها با شناسهٔ کاربر 1000 اجرا شوند. فیلد `runAsGroup` شناسهٔ گروه اصلی 3000 را برای همهٔ فرایندهای درون کانتینرهای Pod تعیین می‌کند. اگر این فیلد حذف شود، شناسهٔ گروه اصلی کانتینرها root(0) خواهد بود. وقتی `runAsGroup` مشخص شده باشد، مالک همهٔ فایل‌های ایجادشده نیز کاربر 1000 و گروه 3000 خواهد بود.
از آنجا که فیلد `fsGroup` مشخص شده است، همهٔ فرایندهای کانتینر عضو گروه تکمیلی با شناسهٔ 2000 نیز هستند.
مالک حجم `/data/demo` و همهٔ فایل‌هایی که در آن حجم ایجاد می‌شوند، گروهی با شناسهٔ 2000 خواهد بود.
علاوه بر این، وقتی فیلد `supplementalGroups` مشخص شده باشد، همهٔ فرایندهای کانتینر عضو گروه‌های مشخص‌شده نیز هستند. اگر این فیلد حذف شود، به معنای خالی بودن آن است.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod security-context-demo
```

یک شل در کانتینر در حال اجرا باز کنید:

```shell
kubectl exec -it security-context-demo -- sh
```

در شل، فرایندهای در حال اجرا را فهرست کنید:

```shell
ps
```

خروجی نشان می‌دهد که فرایندها با کاربر 1000 اجرا می‌شوند که همان مقدار `runAsUser` است:

```none
PID   USER     TIME  COMMAND
    1 1000      0:00 sleep 1h
    6 1000      0:00 sh
...
```

در شل، به مسیر `/data` بروید و تنها دایرکتوری موجود را فهرست کنید:

```shell
cd /data
ls -l
```

خروجی نشان می‌دهد که دایرکتوری `/data/demo` شناسهٔ گروه 2000 دارد که همان مقدار `fsGroup` است.

```none
drwxrwsrwx 2 root 2000 4096 Jun  6 20:08 demo
```

در شل، به مسیر `/data/demo` بروید و یک فایل ایجاد کنید:

```shell
cd demo
echo hello > testfile
```

فایل موجود در دایرکتوری `/data/demo` را فهرست کنید:

```shell
ls -l
```

خروجی نشان می‌دهد که فایل `testfile` شناسهٔ گروه 2000 دارد که همان مقدار `fsGroup` است.

```none
-rw-r--r-- 1 1000 2000 6 Jun  6 20:08 testfile
```

دستور زیر را اجرا کنید:

```shell
id
```

خروجی مشابه زیر است:

```none
uid=1000 gid=3000 groups=2000,3000,4000
```

در خروجی می‌بینید که مقدار `gid` برابر 3000 است که با فیلد `runAsGroup` یکسان است.
اگر `runAsGroup` حذف شده بود، مقدار `gid` همچنان 0 (root) باقی می‌ماند و فرایند می‌توانست با فایل‌هایی که مالکشان گروه root(0) است و نیز گروه‌هایی که مجوزهای لازم را برای گروه root (0) دارند، تعامل داشته باشد. همچنین می‌بینید که `groups` علاوه بر `gid`، شناسه‌های گروهی را که با `fsGroup` و `supplementalGroups` مشخص شده‌اند نیز در بر دارد.

از شل خارج شوید:

```shell
exit
```

### عضویت‌های ضمنی در گروه که در `/etc/group` ایمیج کانتینر تعریف شده‌اند

کوبرنتیز به‌طور پیش‌فرض اطلاعات گروه Pod را با اطلاعات تعریف‌شده در `/etc/group` ایمیج کانتینر ادغام می‌کند.

{{% code_sample file="pods/security/security-context-5.yaml" %}}

زمینهٔ امنیتی این Pod شامل `runAsUser`، `runAsGroup` و `supplementalGroups` است.
با این حال، می‌بینید که گروه‌های تکمیلی واقعی متصل به فرایند کانتینر، شناسه‌های گروهی را نیز شامل می‌شوند که از `/etc/group` ایمیج کانتینر می‌آیند.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-5.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod security-context-demo
```

یک شل در کانتینر در حال اجرا باز کنید:

```shell
kubectl exec -it security-context-demo -- sh
```

هویت فرایند را بررسی کنید:

```shell
id
```

خروجی مشابه زیر است:

```none
uid=1000 gid=3000 groups=3000,4000,50000
```

می‌بینید که `groups` شامل شناسهٔ گروه `50000` است. دلیل این است که کاربر (`uid=1000`) که در ایمیج تعریف شده، به گروه (`gid=50000`) تعلق دارد که در `/etc/group` درون ایمیج کانتینر تعریف شده است.

فایل `/etc/group` را در ایمیج کانتینر بررسی کنید:

```shell
cat /etc/group
```

می‌بینید که کاربر با uid برابر `1000` به گروه `50000` تعلق دارد.

```none
...
user-defined-in-image:x:1000:
group-defined-in-image:x:50000:user-defined-in-image
```

از شل خارج شوید:

```shell
exit
```

{{<note>}}
گروه‌های تکمیلی که _به‌طور ضمنی ادغام می‌شوند_ ممکن است مشکلات امنیتی ایجاد کنند، به‌ویژه هنگام دسترسی به حجم‌ها (برای جزئیات، [kubernetes/kubernetes#112879](https://issue.k8s.io/112879) را ببینید).
اگر می‌خواهید از این وضعیت جلوگیری کنید، بخش زیر را ببینید.
{{</note>}}

## پیکربندی کنترل دقیق SupplementalGroups برای یک Pod {#supplementalgroupspolicy}

{{< feature-state feature_gate_name="SupplementalGroupsPolicy" >}}

برای فعال کردن این قابلیت، باید [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `SupplementalGroupsPolicy` را برای kubelet و kube-apiserver فعال کنید و فیلد `.spec.securityContext.supplementalGroupsPolicy` را برای Pod تنظیم کنید.

فیلد `supplementalGroupsPolicy` سیاست محاسبهٔ گروه‌های تکمیلی برای فرایندهای کانتینر در یک Pod را تعریف می‌کند. این فیلد دو مقدار معتبر دارد:

* مقدار `Merge`: عضویت گروهی تعریف‌شده در `/etc/group` برای کاربر اصلی کانتینر ادغام می‌شود.
  اگر مقداری مشخص نشود، این سیاست پیش‌فرض است.

* مقدار `Strict`: فقط شناسه‌های گروه موجود در فیلدهای `fsGroup`، `supplementalGroups` یا `runAsGroup` به‌عنوان گروه‌های تکمیلی به فرایندهای کانتینر متصل می‌شوند.
  یعنی هیچ عضویت گروهی از `/etc/group` برای کاربر اصلی کانتینر ادغام نمی‌شود.

وقتی این قابلیت فعال باشد، هویت فرایندِ متصل به نخستین فرایند کانتینر نیز در فیلد `.status.containerStatuses[].user.linux` نمایش داده می‌شود. این اطلاعات برای تشخیص اینکه آیا شناسه‌های گروه ضمنی متصل شده‌اند یا نه، مفید است.

{{% code_sample file="pods/security/security-context-6.yaml" %}}

این مانیفست Pod مقدار `supplementalGroupsPolicy=Strict` را تعریف می‌کند. می‌بینید که هیچ‌یک از عضویت‌های گروهی تعریف‌شده در `/etc/group` با گروه‌های تکمیلی فرایندهای کانتینر ادغام نمی‌شوند.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-6.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod security-context-demo
```

هویت فرایند را بررسی کنید:

```shell
kubectl exec -it security-context-demo -- id
```

خروجی مشابه زیر است:

```none
uid=1000 gid=3000 groups=3000,4000
```

وضعیت Pod را ببینید:

```shell
kubectl get pod security-context-demo -o yaml
```

می‌بینید که فیلد `status.containerStatuses[].user.linux` هویت فرایندِ متصل به نخستین فرایند کانتینر را نمایش می‌دهد.

```none
...
status:
  containerStatuses:
  - name: sec-ctx-demo
    user:
      linux:
        gid: 3000
        supplementalGroups:
        - 3000
        - 4000
        uid: 1000
...
```

{{<note>}}
توجه کنید که مقادیر فیلد `status.containerStatuses[].user.linux` همان هویت فرایندی است که _در ابتدا_ به نخستین فرایند کانتینر متصل شده است. اگر کانتینر امتیاز کافی برای انجام فراخوانی‌های سیستمی مرتبط با هویت فرایند داشته باشد
(مانند [`setuid(2)`](https://man7.org/linux/man-pages/man2/setuid.2.html)،
[`setgid(2)`](https://man7.org/linux/man-pages/man2/setgid.2.html) یا
[`setgroups(2)`](https://man7.org/linux/man-pages/man2/setgroups.2.html) و غیره)،
فرایند کانتینر می‌تواند هویت خود را تغییر دهد. بنابراین هویت _واقعی_ فرایند پویا خواهد بود.
{{</note>}}

### پیاده‌سازی‌ها {#implementations-supplementalgroupspolicy}

{{% thirdparty-content %}}

محیط‌های اجرای کانتینر زیر از کنترل دقیق SupplementalGroups پشتیبانی می‌کنند.

در سطح CRI:
- [containerd](https://containerd.io/)، از نسخهٔ v2.0
- [CRI-O](https://cri-o.io/)، از نسخهٔ v1.31

می‌توانید در وضعیت Node ببینید که آیا این قابلیت پشتیبانی می‌شود یا نه.

```yaml
apiVersion: v1
kind: Node
...
status:
  features:
    supplementalGroupsPolicy: true
```
{{<note>}}
در این انتشار آلفا (از v1.31 تا v1.32)، وقتی یک Pod با `SupplementalGroupsPolicy=Strict` روی نودی زمان‌بندی شود که از این قابلیت پشتیبانی نمی‌کند (یعنی `.status.features.supplementalGroupsPolicy=false`)، سیاست گروه‌های تکمیلی آن Pod _بی‌صدا_ به سیاست `Merge` برمی‌گردد.

اما از انتشار بتا (v1.33) به بعد، برای اعمال سخت‌گیرانه‌تر این سیاست، __kubelet ایجاد چنین Podهایی را رد می‌کند، زیرا نود نمی‌تواند سیاست مشخص‌شده را تضمین کند__. وقتی Pod شما رد شود، رویدادهای هشداری با `reason=SupplementalGroupsPolicyNotSupported` مانند نمونهٔ زیر خواهید دید:

```yaml
apiVersion: v1
kind: Event
...
type: Warning
reason: SupplementalGroupsPolicyNotSupported
message: "SupplementalGroupsPolicy=Strict is not supported in this node"
involvedObject:
  apiVersion: v1
  kind: Pod
  ...
```
{{</note>}}


## پیکربندی سیاست تغییر مجوز و مالکیت حجم برای Podها

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

کوبرنتیز به‌طور پیش‌فرض، هنگام mount شدن هر حجم، مالکیت و مجوزهای محتوای آن را به‌صورت بازگشتی تغییر می‌دهد تا با `fsGroup` مشخص‌شده در `securityContext` آن Pod مطابقت داشته باشد.
برای حجم‌های بزرگ، بررسی و تغییر مالکیت و مجوزها ممکن است زمان زیادی ببرد و راه‌اندازی Pod را کند کند. می‌توانید با فیلد `fsGroupChangePolicy` درون `securityContext`، نحوهٔ بررسی و مدیریت مالکیت و مجوزهای یک حجم را توسط کوبرنتیز کنترل کنید.

**fsGroupChangePolicy** - فیلد `fsGroupChangePolicy` رفتار تغییر مالکیت و مجوز حجم را پیش از در دسترس قرار گرفتن آن درون یک Pod تعریف می‌کند.
  این فیلد فقط برای انواعی از حجم اعمال می‌شود که از کنترل مالکیت و مجوزها با `fsGroup` پشتیبانی می‌کنند.
  این فیلد دو مقدار ممکن دارد:

* _OnRootMismatch_: مجوزها و مالکیت فقط در صورتی تغییر می‌کنند که مجوز و مالکیت دایرکتوری ریشه با مجوزهای مورد انتظار حجم مطابقت نداشته باشد.
  این کار می‌تواند زمان لازم برای تغییر مالکیت و مجوز یک حجم را کوتاه‌تر کند.
* _Always_: هنگام mount شدن حجم، مجوز و مالکیت آن همیشه تغییر می‌کند.

برای مثال:

```yaml
securityContext:
  runAsUser: 1000
  runAsGroup: 3000
  fsGroup: 2000
  fsGroupChangePolicy: "OnRootMismatch"
```

{{< note >}}
این فیلد هیچ تأثیری بر انواع حجم‌های موقت (ephemeral) مانند
[`secret`](/docs/concepts/storage/volumes/#secret)،
[`configMap`](/docs/concepts/storage/volumes/#configmap)
و [`emptyDir`](/docs/concepts/storage/volumes/#emptydir) ندارد.
{{< /note >}}

## واگذاری تغییر مجوز و مالکیت حجم به درایور CSI

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

اگر یک درایور [رابط ذخیره‌سازی کانتینر (CSI)](https://github.com/container-storage-interface/spec/blob/master/spec.md) مستقر کنید که از `NodeServiceCapability` با نام `VOLUME_MOUNT_GROUP` پشتیبانی می‌کند، فرایند تنظیم مالکیت و مجوزهای فایل بر اساس `fsGroup` مشخص‌شده در `securityContext` به‌جای کوبرنتیز توسط درایور CSI انجام می‌شود. در این حالت، چون کوبرنتیز هیچ تغییری در مالکیت و مجوزها انجام نمی‌دهد، `fsGroupChangePolicy` اثری ندارد و طبق مشخصات CSI، انتظار می‌رود درایور حجم را با `fsGroup` ارائه‌شده mount کند؛ در نتیجه حجمی به دست می‌آید که `fsGroup` می‌تواند آن را بخواند و در آن بنویسد.

## تنظیم زمینهٔ امنیتی برای یک کانتینر

برای مشخص کردن تنظیمات امنیتی یک کانتینر، فیلد `securityContext` را در مانیفست کانتینر قرار دهید. فیلد `securityContext` یک آبجکت
[SecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#securitycontext-v1-core) است.
تنظیمات امنیتی‌ای که برای یک کانتینر مشخص می‌کنید، فقط بر همان کانتینر اعمال می‌شوند و در صورت هم‌پوشانی، تنظیمات سطح Pod را بازنویسی می‌کنند. تنظیمات کانتینر بر حجم‌های Pod تأثیری ندارند.

در ادامه فایل پیکربندی یک Pod را می‌بینید که یک کانتینر دارد. هم Pod و هم کانتینر فیلد `securityContext` دارند:

{{% code_sample file="pods/security/security-context-2.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-2.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod security-context-demo-2
```

یک شل در کانتینر در حال اجرا باز کنید:

```shell
kubectl exec -it security-context-demo-2 -- sh
```

در شل، فرایندهای در حال اجرا را فهرست کنید:

```shell
ps aux
```

خروجی نشان می‌دهد که فرایندها با کاربر 2000 اجرا می‌شوند. این همان مقدار `runAsUser` است که برای کانتینر مشخص شده و مقدار 1000 را که برای Pod مشخص شده است بازنویسی می‌کند.

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
2000         1  0.0  0.0   4336   764 ?        Ss   20:36   0:00 /bin/sh -c node server.js
2000         8  0.1  0.5 772124 22604 ?        Sl   20:36   0:00 node server.js
...
```

از شل خارج شوید:

```shell
exit
```

## تنظیم قابلیت‌ها برای یک کانتینر

با [قابلیت‌های لینوکس](https://man7.org/linux/man-pages/man7/capabilities.7.html)
می‌توانید امتیازهای مشخصی را به یک فرایند بدهید، بی‌آنکه همهٔ امتیازهای کاربر root را به آن بدهید. برای افزودن یا حذف قابلیت‌های لینوکس برای یک کانتینر، فیلد `capabilities` را در بخش `securityContext` مانیفست کانتینر قرار دهید.

ابتدا ببینید وقتی فیلد `capabilities` را قرار نمی‌دهید چه اتفاقی می‌افتد.
در ادامه فایل پیکربندی‌ای را می‌بینید که هیچ قابلیتی را به کانتینر اضافه یا از آن حذف نمی‌کند:

{{% code_sample file="pods/security/security-context-3.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-3.yaml
```

بررسی کنید که کانتینر Pod در حال اجرا باشد:

```shell
kubectl get pod security-context-demo-3
```

یک شل در کانتینر در حال اجرا باز کنید:

```shell
kubectl exec -it security-context-demo-3 -- sh
```

در شل، فرایندهای در حال اجرا را فهرست کنید:

```shell
ps aux
```

خروجی، شناسه‌های فرایند (PID) کانتینر را نشان می‌دهد:

```
USER  PID %CPU %MEM    VSZ   RSS TTY   STAT START   TIME COMMAND
root    1  0.0  0.0   4336   796 ?     Ss   18:17   0:00 /bin/sh -c node server.js
root    5  0.1  0.5 772124 22700 ?     Sl   18:17   0:00 node server.js
```

در شل، وضعیت فرایند 1 را مشاهده کنید:

```shell
cd /proc/1
cat status
```

خروجی، نقشهٔ بیتی قابلیت‌های فرایند را نشان می‌دهد:

```
...
CapPrm:	00000000a80425fb
CapEff:	00000000a80425fb
...
```

نقشهٔ بیتی قابلیت‌ها را یادداشت کنید و سپس از شل خارج شوید:

```shell
exit
```

سپس کانتینری را اجرا کنید که با کانتینر قبلی یکسان است، با این تفاوت که قابلیت‌های بیشتری برای آن تنظیم شده است.

در ادامه فایل پیکربندی یک Pod را می‌بینید که یک کانتینر اجرا می‌کند. این پیکربندی قابلیت‌های `CAP_NET_ADMIN` و `CAP_SYS_TIME` را اضافه می‌کند:

{{% code_sample file="pods/security/security-context-4.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-4.yaml
```

یک شل در کانتینر در حال اجرا باز کنید:

```shell
kubectl exec -it security-context-demo-4 -- sh
```

در شل، قابلیت‌های فرایند 1 را مشاهده کنید:

```shell
cd /proc/1
cat status
```

خروجی، نقشهٔ بیتی قابلیت‌های فرایند را نشان می‌دهد:

```
...
CapPrm:	00000000aa0435fb
CapEff:	00000000aa0435fb
...
```

قابلیت‌های دو کانتینر را با هم مقایسه کنید:

```
00000000a80425fb
00000000aa0435fb
```

در نقشهٔ بیتی قابلیت‌های کانتینر اول، بیت‌های 12 و 25 خاموش هستند. در کانتینر دوم، بیت‌های 12 و 25 روشن هستند. بیت 12 مربوط به `CAP_NET_ADMIN` و بیت 25 مربوط به `CAP_SYS_TIME` است.
برای دیدن تعریف ثابت‌های قابلیت، به [capability.h](https://github.com/torvalds/linux/blob/master/include/uapi/linux/capability.h) مراجعه کنید.

{{< note >}}
ثابت‌های قابلیت لینوکس به شکل `CAP_XXX` هستند.
اما وقتی قابلیت‌ها را در مانیفست کانتینر خود فهرست می‌کنید، باید بخش `CAP_` ثابت را حذف کنید.
برای مثال، برای افزودن `CAP_SYS_TIME`، مقدار `SYS_TIME` را در فهرست قابلیت‌های خود قرار دهید.
{{< /note >}}

## تنظیم پروفایل Seccomp برای یک کانتینر

برای تنظیم پروفایل Seccomp یک کانتینر، فیلد `seccompProfile` را در بخش `securityContext` مانیفست Pod یا کانتینر خود قرار دهید. فیلد `seccompProfile` یک آبجکت
[SeccompProfile](/docs/reference/generated/kubernetes-api/{{< param "version"
>}}/#seccompprofile-v1-core) است که از `type` و `localhostProfile` تشکیل شده است.
گزینه‌های معتبر برای `type` عبارت‌اند از `RuntimeDefault`، `Unconfined` و `Localhost`. فیلد `localhostProfile` فقط باید زمانی تنظیم شود که `type: Localhost` باشد. این فیلد مسیر پروفایل ازپیش‌پیکربندی‌شده روی نود را نسبت به محل پروفایل‌های Seccomp در kubelet مشخص می‌کند. این محل با فلگ `--root-dir` پیکربندی می‌شود.

در مثال زیر، پروفایل Seccomp روی پروفایل پیش‌فرض محیط اجرای کانتینر نود تنظیم می‌شود:

```yaml
...
securityContext:
  seccompProfile:
    type: RuntimeDefault
```

در مثال زیر، پروفایل Seccomp روی فایلی ازپیش‌پیکربندی‌شده در مسیر
`<kubelet-root-dir>/seccomp/my-profiles/profile-allow.json` تنظیم می‌شود:

```yaml
...
securityContext:
  seccompProfile:
    type: Localhost
    localhostProfile: my-profiles/profile-allow.json
```

## تنظیم پروفایل AppArmor برای یک کانتینر

برای تنظیم پروفایل AppArmor یک کانتینر، فیلد `appArmorProfile` را در بخش `securityContext` کانتینر خود قرار دهید. فیلد `appArmorProfile` یک آبجکت
[AppArmorProfile](/docs/reference/generated/kubernetes-api/{{< param "version"
>}}/#apparmorprofile-v1-core) است که از `type` و `localhostProfile` تشکیل شده است.
گزینه‌های معتبر برای `type` عبارت‌اند از `RuntimeDefault` (پیش‌فرض)، `Unconfined` و `Localhost`. فیلد `localhostProfile` فقط باید زمانی تنظیم شود که مقدار `type` برابر `Localhost` باشد. این فیلد نام پروفایل ازپیش‌پیکربندی‌شده روی نود را مشخص می‌کند. پروفایل باید روی همه نودهایی که برای Pod مناسب هستند بارگذاری شود، زیرا نمی‌دانید Pod روی کدام نود زمان‌بندی خواهد شد.
روش‌های راه‌اندازی پروفایل‌های سفارشی در
[راه‌اندازی نودها با پروفایل‌ها](/docs/tutorials/security/apparmor/#setting-up-nodes-with-profiles) شرح داده شده‌اند.

نکته: اگر `containers[*].securityContext.appArmorProfile.type` به‌صراحت روی `RuntimeDefault` تنظیم شده باشد و AppArmor روی نود فعال نباشد، Pod پذیرفته نمی‌شود. اما اگر `containers[*].securityContext.appArmorProfile.type` مشخص نشده باشد، مقدار پیش‌فرض (که آن هم `RuntimeDefault` است) فقط زمانی اعمال می‌شود که AppArmor روی نود فعال باشد. اگر AppArmor روی نود غیرفعال باشد، Pod پذیرفته می‌شود، اما کانتینر با پروفایل `RuntimeDefault` محدود نمی‌شود.

در مثال زیر، پروفایل AppArmor روی پروفایل پیش‌فرض محیط اجرای کانتینر نود تنظیم می‌شود:

```yaml
...
containers:
- name: container-1
  securityContext:
    appArmorProfile:
      type: RuntimeDefault
```

در مثال زیر، پروفایل AppArmor روی پروفایلی ازپیش‌پیکربندی‌شده با نام `k8s-apparmor-example-deny-write` تنظیم می‌شود:

```yaml
...
containers:
- name: container-1
  securityContext:
    appArmorProfile:
      type: Localhost
      localhostProfile: k8s-apparmor-example-deny-write
```

برای جزئیات بیشتر، [محدود کردن دسترسی یک کانتینر به منابع با AppArmor](/docs/tutorials/security/apparmor/) را ببینید.

## اختصاص برچسب‌های SELinux به یک کانتینر

برای اختصاص برچسب‌های SELinux به یک کانتینر، فیلد `seLinuxOptions` را در بخش `securityContext` مانیفست Pod یا کانتینر خود قرار دهید. فیلد `seLinuxOptions` یک آبجکت
[SELinuxOptions](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#selinuxoptions-v1-core)
است. در مثال زیر یک سطح SELinux اعمال می‌شود:

```yaml
...
securityContext:
  seLinuxOptions:
    level: "s0:c123,c456"
```

{{< note >}}
برای اختصاص برچسب‌های SELinux، ماژول امنیتی SELinux باید روی سیستم‌عامل میزبان بارگذاری شده باشد.
روی نودهای کارگر ویندوزی و نودهای کارگر لینوکسی بدون پشتیبانی از SELinux، این فیلد و هیچ‌یک از feature gateهای SELinux که در ادامه شرح داده می‌شوند، تأثیری ندارند.
{{< /note >}}

### برچسب‌گذاری مجدد کارآمد حجم‌ها در SELinux

{{< feature-state feature_gate_name="SELinuxMountReadWriteOncePod" >}}

کوبرنتیز به‌طور پیش‌فرض برچسب SELinux را با استفاده از گزینه mount با مقدار `-o context=<label>` بی‌درنگ روی حجم‌های (volume) واجد شرایط اعمال می‌کند.

برای بهره‌مندی از این افزایش سرعت، همه شرایط زیر باید برقرار باشند:

* لازم است Pod از یک PersistentVolumeClaim استفاده کند.
* مقدار `spec.securityContext.seLinuxChangePolicy` در Pod باید nil (پیش‌فرض) یا `MountOption` باشد.
* لازم است فیلد `seLinuxOptions` برای Pod (یا برای همه کانتینرهای آن که از PersistentVolumeClaim استفاده می‌کنند) تنظیم شده باشد.
* لازم است PersistentVolume متناظر یکی از موارد زیر باشد:
  * حجمی که از نوع حجم قدیمی و درون‌درختی (in-tree) `iscsi`، `rbd` یا `fc` استفاده می‌کند.
  * یا حجمی که از یک درایور {{< glossary_tooltip text="CSI" term_id="csi" >}} استفاده می‌کند.
    درایور CSI باید با تنظیم `spec.seLinuxMount: true` در نمونه CSIDriver خود اعلام کند که از mount با `-o context` پشتیبانی می‌کند.

اگر هر یک از این شرایط برقرار نباشد، برچسب‌گذاری مجدد SELinux به روش دیگری انجام می‌شود: محیط اجرای کانتینر برچسب SELinux همه inodeهای حجم (فایل‌ها و دایرکتوری‌ها) را به‌صورت بازگشتی تغییر می‌دهد. به‌طور مشخص، این روش برای حجم‌های موقت (ephemeral) کوبرنتیز مانند `secret`، `configMap` و `projected` و نیز برای همه حجم‌هایی به کار می‌رود که نمونه CSIDriver آن‌ها به‌صراحت پشتیبانی از mount با `-o context` را اعلام نکرده است.

هنگام استفاده از این افزایش سرعت، همه Podهایی که هم‌زمان از یک حجم واجد شرایط یکسان روی یک نود استفاده می‌کنند، **باید برچسب SELinux یکسانی داشته باشند**. هر Pod با برچسب SELinux متفاوت نمی‌تواند شروع به کار کند و تا زمانی که همه Podهای دارای برچسب‌های SELinux دیگر که از آن حجم استفاده می‌کنند حذف نشوند، در وضعیت `ContainerCreating` باقی می‌ماند.

{{< feature-state feature_gate_name="SELinuxChangePolicy" >}}
آن دسته از Podهایی که می‌خواهند از برچسب‌گذاری مجدد با گزینه‌های mount صرف‌نظر کنند، می‌توانند `spec.securityContext.seLinuxChangePolicy` را روی `Recursive` تنظیم کنند. این کار زمانی لازم است که چند Pod یک حجم واحد را روی یک نود به اشتراک بگذارند، اما با برچسب‌های SELinux متفاوتی اجرا شوند که دسترسی هم‌زمان به حجم را ممکن می‌کنند. برای مثال، یک Pod ممتاز (privileged) که با برچسب `spc_t` اجرا می‌شود و یک Pod غیرممتاز که با برچسب پیش‌فرض `container_file_t` اجرا می‌شود.
اگر `spec.securityContext.seLinuxChangePolicy` تنظیم نشده باشد (یا مقدار پیش‌فرض `MountOption` را داشته باشد)، فقط یکی از این Podها می‌تواند روی نود اجرا شود و دیگری با خطای
`conflicting SELinux labels of volume <name of the volume>: <label of the running pod> and <label of the pod that can't start>` در وضعیت ContainerCreating باقی می‌ماند.

#### کنترل‌کننده SELinuxWarningController
برای آسان‌تر کردن شناسایی Podهایی که تحت تأثیر تغییر در برچسب‌گذاری مجدد حجم‌های SELinux قرار می‌گیرند، کنترل‌کننده جدیدی به نام `SELinuxWarningController` به kube-controller-manager اضافه شده است.
این کنترل‌کننده به‌طور پیش‌فرض غیرفعال است. برای فعال کردن آن می‌توانید مقدار `--controllers=*,selinux-warning-controller` را در
[فلگ خط فرمان](/docs/reference/command-line-tools-reference/kube-controller-manager/) تنظیم کنید،
یا فیلد `genericControllerManagerConfiguration.controllers` را در
[فیلدهای KubeControllerManagerConfiguration](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/#controllermanager-config-k8s-io-v1alpha1-GenericControllerManagerConfiguration) تنظیم کنید.
این کنترل‌کننده تنها زمانی کار می‌کند که feature gate با نام `SELinuxChangePolicy` فعال باشد.

پس از فعال‌سازی، این کنترل‌کننده Podهای در حال اجرا را زیر نظر می‌گیرد و هر گاه تشخیص دهد که دو Pod از یک حجم یکسان با برچسب‌های SELinux متفاوت استفاده می‌کنند، کارهای زیر را انجام می‌دهد:
1. برای هر دو Pod یک رویداد (event) منتشر می‌کند. در این حالت، دستور `kubectl describe pod <pod-name>` پیام زیر را نشان می‌دهد:
  `SELinuxLabel "<label on the pod>" conflicts with pod <the other pod name> that uses the same volume as this pod
  with SELinuxLabel "<the other pod label>". If both pods land on the same node, only one of them may access the volume`.
2. مقدار متریک `selinux_warning_controller_selinux_volume_conflict` را افزایش می‌دهد. این متریک نام و فضای نام (namespace) هر دو Pod را به‌صورت برچسب در خود دارد تا Podهای تحت تأثیر به‌آسانی شناسایی شوند.

مدیر کلاستر می‌تواند با استفاده از این اطلاعات، Podهای تحت تأثیر این تغییر را شناسایی کند و پیشاپیش آن‌ها را از این بهینه‌سازی خارج کند (یعنی `spec.securityContext.seLinuxChangePolicy: Recursive` را برایشان تنظیم کند).

{{< warning >}}
اکیداً توصیه می‌کنیم در کلاسترهایی که از SELinux استفاده می‌کنند، پیش از ارتقا به کوبرنتیز نسخه v1.37 یا بالاتر، این کنترل‌کننده را فعال کنید و مطمئن شوید که متریک `selinux_warning_controller_selinux_volume_conflict` هیچ تعارضی گزارش نمی‌کند. در این نسخه‌ها `SELinuxMount` به وضعیت GA رسیده و به‌طور پیش‌فرض فعال است.
{{< /warning >}}

#### فهرست feature gateها

رفتار برچسب‌گذاری مجدد حجم‌ها در SELinux با feature gateهای زیر کنترل می‌شود:

* گزینه `SELinuxMountReadWriteOncePod`: بهینه‌سازی را برای حجم‌هایی با `accessModes: ["ReadWriteOncePod"]` فعال می‌کند.
  فعال کردن این feature gate بسیار ایمن است، زیرا ممکن نیست دو Pod یک حجم واحد با این حالت دسترسی را به اشتراک بگذارند. این گزینه از نسخه 1.36 در وضعیت GA قرار دارد.
* گزینه `SELinuxChangePolicy`: فیلد `spec.securityContext.seLinuxChangePolicy` را در Pod و کنترل‌کننده مرتبط با آن، یعنی SELinuxWarningController، را در kube-controller-manager فعال می‌کند. هنگامی که چند Pod با برچسب‌های SELinux متفاوت یک حجم را به اشتراک می‌گذارند، با این گزینه می‌توان Podها را از بهینه‌سازی mount خارج کرد. این گزینه از نسخه 1.36 در وضعیت GA قرار دارد.
* گزینه `SELinuxMount`: بهینه‌سازی را برای همه حجم‌های واجد شرایط فعال می‌کند. این گزینه از نسخه 1.37 در وضعیت GA قرار دارد.
  هنگام ارتقا از نسخه‌های قدیمی‌تر کوبرنتیز که در آن‌ها `SELinuxMount` به‌طور پیش‌فرض غیرفعال بود، توصیه می‌کنیم ابتدا feature gate با نام `SELinuxChangePolicy` و کنترل‌کننده SELinuxWarningController را فعال کنید تا تأثیر این تغییر را بررسی کنید.

## مدیریت دسترسی به فایل‌سیستم `/proc` {#proc-access}

{{< feature-state feature_gate_name="ProcMountType" >}}

در محیط‌های اجرایی که از مشخصات محیط اجرای OCI پیروی می‌کنند، کانتینرها به‌طور پیش‌فرض در حالتی اجرا می‌شوند که در آن چندین مسیر هم پوشانده (masked) و هم فقط‌خواندنی هستند.
در نتیجه، این مسیرها درون فضای نام mount کانتینر وجود دارند و می‌توانند همانند حالتی عمل کنند که کانتینر یک میزبان ایزوله باشد، اما فرایند کانتینر نمی‌تواند در آن‌ها بنویسد. فهرست مسیرهای پوشانده‌شده و فقط‌خواندنی به شرح زیر است:

- مسیرهای پوشانده‌شده:
  - `/proc/asound`
  - `/proc/acpi`
  - `/proc/kcore`
  - `/proc/keys`
  - `/proc/latency_stats`
  - `/proc/timer_list`
  - `/proc/timer_stats`
  - `/proc/sched_debug`
  - `/proc/scsi`
  - `/sys/firmware`
  - `/sys/devices/virtual/powercap`

- مسیرهای فقط‌خواندنی:
  - `/proc/bus`
  - `/proc/fs`
  - `/proc/irq`
  - `/proc/sys`
  - `/proc/sysrq-trigger`


ممکن است بخواهید برای برخی Podها این پوشاندن پیش‌فرض مسیرها را دور بزنید.
رایج‌ترین موقعیت برای این کار زمانی است که می‌خواهید کانتینرهایی را درون یک کانتینر کوبرنتیز (درون یک Pod) اجرا کنید.

فیلد `procMount` در `securityContext` به کاربر امکان می‌دهد درخواست کند که `/proc` کانتینر `Unmasked` باشد، یا فرایند کانتینر آن را به‌صورت خواندنی-نوشتنی mount کند. این قابلیت درباره `/sys/firmware` نیز، که درون `/proc` قرار ندارد، صدق می‌کند.

```yaml
...
securityContext:
  procMount: Unmasked
```

{{< note >}}
تنظیم `procMount` روی Unmasked مستلزم آن است که مقدار `spec.hostUsers` در مشخصات Pod برابر `false` باشد. به بیان دیگر، کانتینری که می‌خواهد `/proc` یا `/sys` پوشانده‌نشده داشته باشد، باید در یک
[فضای نام کاربر](/docs/concepts/workloads/pods/user-namespaces/) نیز قرار داشته باشد.
کوبرنتیز از نسخه v1.12 تا v1.29 این الزام را اعمال نمی‌کرد.
{{< /note >}}

## بحث

زمینه امنیتی (security context) یک Pod روی کانتینرهای آن Pod و در صورت لزوم روی حجم‌های آن نیز اعمال می‌شود. به‌طور مشخص، `fsGroup` و `seLinuxOptions` به شکل زیر روی حجم‌ها اعمال می‌شوند:

* فیلد `fsGroup`: حجم‌هایی که از مدیریت مالکیت پشتیبانی می‌کنند، طوری تغییر داده می‌شوند که مالکیت آن‌ها به GID مشخص‌شده در `fsGroup` تعلق گیرد و این GID بتواند در آن‌ها بنویسد. برای جزئیات بیشتر،
  [سند طراحی مدیریت مالکیت](https://git.k8s.io/design-proposals-archive/storage/volume-ownership-management.md)
  را ببینید.

* فیلد `seLinuxOptions`: حجم‌هایی که از برچسب‌گذاری SELinux پشتیبانی می‌کنند، دوباره برچسب‌گذاری می‌شوند تا برای برچسب مشخص‌شده در `seLinuxOptions` قابل دسترسی باشند. معمولاً کافی است فقط بخش `level` را تنظیم کنید. این بخش برچسب
  [امنیت چنددسته‌ای (MCS)](https://selinuxproject.org/page/NB_MLS)
  را تعیین می‌کند که به همه کانتینرهای Pod و همچنین به حجم‌ها داده می‌شود.

{{< warning >}}
پس از آنکه یک برچسب MCS برای یک Pod مشخص کردید، همه Podهای دارای همان برچسب می‌توانند به آن حجم دسترسی داشته باشند.
اگر به محافظت میان Podها نیاز دارید، باید به هر Pod یک برچسب MCS یکتا اختصاص دهید.
{{< /warning >}}

## پاک‌سازی

اکنون Podها را حذف کنید:

```shell
kubectl delete pod security-context-demo
kubectl delete pod security-context-demo-2
kubectl delete pod security-context-demo-3
kubectl delete pod security-context-demo-4
```

## {{% heading "whatsnext" %}}

* [PodSecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podsecuritycontext-v1-core)
* [SecurityContext](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#securitycontext-v1-core)
* [راهنمای پیکربندی افزونه CRI](https://github.com/containerd/containerd/blob/main/docs/cri/config.md)
* [سند طراحی زمینه‌های امنیتی](https://git.k8s.io/design-proposals-archive/auth/security_context.md)
* [سند طراحی مدیریت مالکیت](https://git.k8s.io/design-proposals-archive/storage/volume-ownership-management.md)
* [پذیرش PodSecurity](/docs/concepts/security/pod-security-admission/)
* [سند طراحی
  AllowPrivilegeEscalation](https://git.k8s.io/design-proposals-archive/auth/no-new-privs.md)
* برای اطلاعات بیشتر درباره سازوکارهای امنیتی در لینوکس،
  [مروری بر قابلیت‌های امنیتی هسته لینوکس](https://www.linux.com/learn/overview-linux-kernel-security-features)
  را ببینید (توجه: بخشی از اطلاعات آن قدیمی است).
* درباره [فضاهای نام کاربر](/docs/concepts/workloads/pods/user-namespaces/)
  برای Podهای لینوکسی مطالعه کنید.
* [مسیرهای پوشانده‌شده در مشخصات محیط اجرای
  OCI](https://github.com/opencontainers/runtime-spec/blob/f66aad47309/config-linux.md#masked-paths)
