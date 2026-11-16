---
reviewers:
- stclair
title: محدود کردن دسترسی یک کانتینر به منابع با AppArmor
content_type: tutorial
weight: 30
---

<!-- overview -->

{{< feature-state feature_gate_name="AppArmor" >}}

این صفحه نشان می‌دهد که چگونه پروفایل‌های AppArmor را روی نودهای خود بارگذاری کنید و این پروفایل‌ها را در Podها اعمال کنید. برای آشنایی بیشتر با شیوه‌ای که کوبرنتیز با استفاده از AppArmor دامنهٔ دسترسی Podها را محدود می‌کند، به
[محدودیت‌های امنیتی هستهٔ لینوکس برای Podها و کانتینرها](/docs/concepts/security/linux-kernel-security-constraints/#apparmor) مراجعه کنید.

## {{% heading "objectives" %}}


* نمونه‌ای از نحوهٔ بارگذاری یک پروفایل روی نود را ببینید
* با نحوهٔ اعمال پروفایل روی یک Pod آشنا شوید
* با نحوهٔ بررسی بارگذاری‌شدن پروفایل آشنا شوید
* ببینید هنگام نقض یک پروفایل چه اتفاقی می‌افتد
* ببینید هنگامی که یک پروفایل قابل بارگذاری نباشد چه اتفاقی می‌افتد



## {{% heading "prerequisites" %}}


ماژول AppArmor یک ماژول اختیاری هسته و یک قابلیت اختیاری کوبرنتیز است؛ بنابراین پیش از ادامه، پشتیبانی نودهای خود از آن را بررسی کنید:

1. ماژول هستهٔ AppArmor فعال باشد: برای آنکه هستهٔ لینوکس بتواند یک پروفایل AppArmor را اعمال کند، ماژول هستهٔ AppArmor باید نصب و فعال باشد. چندین توزیع، مانند Ubuntu و SUSE، این ماژول را به‌طور پیش‌فرض فعال می‌کنند و بسیاری از توزیع‌های دیگر نیز پشتیبانی اختیاری از آن ارائه می‌دهند. برای بررسی فعال‌بودن ماژول، فایل `/sys/module/apparmor/parameters/enabled` را بررسی کنید:

   ```shell
   cat /sys/module/apparmor/parameters/enabled
   Y
   ```

   پیش از پذیرش Podی که AppArmor به‌صراحت برای آن پیکربندی شده است، kubelet بررسی می‌کند که AppArmor روی میزبان فعال باشد.

1. محیط اجرای کانتینر از AppArmor پشتیبانی کند: همهٔ محیط‌های اجرای کانتینر رایجی که کوبرنتیز از آن‌ها پشتیبانی می‌کند، از جمله {{< glossary_tooltip term_id="containerd" >}} و {{< glossary_tooltip term_id="cri-o" >}}، باید از AppArmor پشتیبانی کنند. لطفاً به مستندات محیط اجرای مربوطه مراجعه کنید و اطمینان حاصل کنید که کلاستر الزامات استفاده از AppArmor را برآورده می‌کند.

1. پروفایل بارگذاری شده باشد: برای اعمال AppArmor روی یک Pod، پروفایلی از AppArmor تعیین می‌شود که هر کانتینر باید با آن اجرا شود. اگر هر یک از پروفایل‌های تعیین‌شده در هسته بارگذاری نشده باشد، kubelet آن Pod را رد می‌کند. برای مشاهدهٔ پروفایل‌های بارگذاری‌شده روی یک نود، می‌توانید فایل `/sys/kernel/security/apparmor/profiles` را بررسی کنید. برای مثال:

   ```shell
   ssh gke-test-default-pool-239f5d02-gyn2 "sudo cat /sys/kernel/security/apparmor/profiles | sort"
   ```
   ```
   apparmor-test-deny-write (enforce)
   apparmor-test-audit-write (enforce)
   docker-default (enforce)
   k8s-nginx (enforce)
   ```

   برای جزئیات بیشتر دربارهٔ بارگذاری پروفایل‌ها روی نودها، به
   [راه‌اندازی نودها با پروفایل‌ها](#setting-up-nodes-with-profiles) مراجعه کنید.

<!-- lessoncontent -->

## ایمن‌سازی یک Pod

{{< alert color="info" title="Note" >}}
پیش از نسخهٔ v1.30 کوبرنتیز، AppArmor از طریق حاشیه‌نویسی‌ها (annotations) تعیین می‌شد. برای مشاهدهٔ مستندات مربوط به این API منسوخ‌شده، از انتخابگر نسخهٔ مستندات استفاده کنید.
{{< /alert >}}

پروفایل‌های AppArmor را می‌توان در سطح Pod یا در سطح کانتینر تعیین کرد. پروفایل AppArmor کانتینر بر پروفایل Pod اولویت دارد.

```yaml
securityContext:
  appArmorProfile:
    type: <profile_type>
```

که در آن `<profile_type>` یکی از مقادیر زیر است:

* مقدار `RuntimeDefault` برای استفاده از پروفایل پیش‌فرض محیط اجرا
* مقدار `Localhost` برای استفاده از پروفایلی که روی میزبان بارگذاری شده است (ادامه را ببینید)
* مقدار `Unconfined` برای اجرا بدون AppArmor

برای جزئیات کامل API پروفایل AppArmor، به [تعیین محدودسازی AppArmor](#specifying-apparmor-confinement) مراجعه کنید.

برای اطمینان از اعمال‌شدن پروفایل، می‌توانید با بررسی ویژگی proc فرایند ریشهٔ کانتینر، بررسی کنید که این فرایند با پروفایل درست اجرا می‌شود:

```shell
kubectl exec <pod_name> -- cat /proc/1/attr/current
```

خروجی باید چیزی شبیه به این باشد:

```
cri-containerd.apparmor.d (enforce)
```

## مثال

*در این مثال فرض شده است که شما از قبل کلاستری با پشتیبانی از AppArmor راه‌اندازی کرده‌اید.*

ابتدا پروفایلی را که می‌خواهید استفاده کنید روی نودهای خود بارگذاری کنید. این پروفایل همهٔ عملیات نوشتن در فایل را مسدود می‌کند:

```
#include <tunables/global>

profile k8s-apparmor-example-deny-write flags=(attach_disconnected) {
  #include <abstractions/base>

  file,

  # Deny all file writes.
  deny /** w,
}
```

از آنجا که نمی‌دانید Pod روی کدام نود زمان‌بندی خواهد شد، پروفایل باید روی همهٔ نودها بارگذاری شود. در این مثال می‌توانید برای نصب پروفایل‌ها از SSH استفاده کنید، اما روش‌های دیگری نیز در [راه‌اندازی نودها با پروفایل‌ها](#setting-up-nodes-with-profiles) بررسی شده‌اند.

```shell
# This example assumes that node names match host names, and are reachable via SSH.
NODES=($( kubectl get node -o jsonpath='{.items[*].status.addresses[?(.type == "Hostname")].address}' ))

for NODE in ${NODES[*]}; do ssh $NODE 'sudo apparmor_parser -q <<EOF
#include <tunables/global>

profile k8s-apparmor-example-deny-write flags=(attach_disconnected) {
  #include <abstractions/base>

  file,

  # Deny all file writes.
  deny /** w,
}
EOF'
done
```

سپس یک Pod سادهٔ «Hello AppArmor» را با پروفایل deny-write اجرا کنید:

{{% code_sample file="pods/security/hello-apparmor.yaml" %}}

```shell
kubectl create -f hello-apparmor.yaml
```

با بررسی `/proc/1/attr/current` می‌توانید تأیید کنید که کانتینر واقعاً با آن پروفایل اجرا می‌شود:

```shell
kubectl exec hello-apparmor -- cat /proc/1/attr/current
```

خروجی باید به این صورت باشد:
```
k8s-apparmor-example-deny-write (enforce)
```

در پایان، می‌توانید ببینید که اگر با نوشتن در یک فایل پروفایل را نقض کنید، چه اتفاقی می‌افتد:

```shell
kubectl exec hello-apparmor -- touch /tmp/test
```
```
touch: /tmp/test: Permission denied
error: error executing remote command: command terminated with non-zero exit code: Error executing in Docker Container: 1
```

برای جمع‌بندی، ببینید اگر بخواهید پروفایلی را تعیین کنید که بارگذاری نشده است، چه اتفاقی می‌افتد:

```shell
kubectl create -f /dev/stdin <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: hello-apparmor-2
spec:
  securityContext:
    appArmorProfile:
      type: Localhost
      localhostProfile: k8s-apparmor-example-allow-write
  containers:
  - name: hello
    image: busybox:1.28
    command: [ "sh", "-c", "echo 'Hello AppArmor!' && sleep 1h" ]
EOF
```
```
pod/hello-apparmor-2 created
```

با اینکه Pod با موفقیت ایجاد شد، بررسی بیشتر نشان می‌دهد که در وضعیت Pending گیر کرده است:

```shell
kubectl describe pod hello-apparmor-2
```
```
Name:          hello-apparmor-2
Namespace:     default
Node:          gke-test-default-pool-239f5d02-x1kf/10.128.0.27
Start Time:    Tue, 30 Aug 2016 17:58:56 -0700
Labels:        <none>
Annotations:   container.apparmor.security.beta.kubernetes.io/hello=localhost/k8s-apparmor-example-allow-write
Status:        Pending
... 
Events:
  Type     Reason     Age              From               Message
  ----     ------     ----             ----               -------
  Normal   Scheduled  10s              default-scheduler  Successfully assigned default/hello-apparmor to gke-test-default-pool-239f5d02-x1kf
  Normal   Pulled     8s               kubelet            Successfully pulled image "busybox:1.28" in 370.157088ms (370.172701ms including waiting)
  Normal   Pulling    7s (x2 over 9s)  kubelet            Pulling image "busybox:1.28"
  Warning  Failed     7s (x2 over 8s)  kubelet            Error: failed to get container spec opts: failed to generate apparmor spec opts: apparmor profile not found k8s-apparmor-example-allow-write
  Normal   Pulled     7s               kubelet            Successfully pulled image "busybox:1.28" in 90.980331ms (91.005869ms including waiting)
```

یک رویداد (Event) پیام خطا را همراه با علت آن ارائه می‌دهد؛ عبارت‌بندی دقیق این پیام به محیط اجرا بستگی دارد:
```
  Warning  Failed     7s (x2 over 8s)  kubelet            Error: failed to get container spec opts: failed to generate apparmor spec opts: apparmor profile not found 
```

## مدیریت

### راه‌اندازی نودها با پروفایل‌ها

کوبرنتیز {{< skew currentVersion >}} هیچ سازوکار داخلی برای بارگذاری پروفایل‌های AppArmor روی نودها ارائه نمی‌دهد. پروفایل‌ها را می‌توان از طریق زیرساخت سفارشی یا ابزارهایی مانند
[Kubernetes Security Profiles Operator](https://github.com/kubernetes-sigs/security-profiles-operator) بارگذاری کرد.

زمان‌بند نمی‌داند کدام پروفایل‌ها روی کدام نود بارگذاری شده‌اند؛ بنابراین مجموعهٔ کامل پروفایل‌ها باید روی همهٔ نودها بارگذاری شود. روش جایگزین این است که برای هر پروفایل (یا هر دسته از پروفایل‌ها) یک برچسب نود روی نود اضافه کنید و با استفاده از یک
[انتخابگر نود (node selector)](/docs/concepts/scheduling-eviction/assign-pod-node/) اطمینان حاصل کنید که Pod روی نودی دارای پروفایل موردنیاز اجرا می‌شود.

## نوشتن پروفایل‌ها

تعیین درست پروفایل‌های AppArmor می‌تواند کار دشواری باشد. خوشبختانه ابزارهایی برای کمک به این کار وجود دارند:

* ابزارهای `aa-genprof` و `aa-logprof` با پایش فعالیت و لاگ‌های یک برنامه و مجاز شمردن اقداماتی که انجام می‌دهد، قواعد پروفایل را تولید می‌کنند. دستورالعمل‌های بیشتر در
  [مستندات AppArmor](https://gitlab.com/apparmor/apparmor/wikis/Profiling_with_tools) ارائه شده است.
* ابزار [bane](https://github.com/jfrazelle/bane) یک مولد پروفایل AppArmor برای Docker است که از یک زبان سادهٔ پروفایل استفاده می‌کند.

برای اشکال‌زدایی مشکلات AppArmor، می‌توانید لاگ‌های سیستم را بررسی کنید تا ببینید دقیقاً چه چیزی رد شده است. سامانهٔ AppArmor پیام‌های مفصلی را در `dmesg` ثبت می‌کند و خطاها را معمولاً می‌توان در لاگ‌های سیستم یا با `journalctl` پیدا کرد. اطلاعات بیشتر در
[AppArmor failures](https://gitlab.com/apparmor/apparmor/wikis/AppArmor_Failures) ارائه شده است.


## تعیین محدودسازی AppArmor

{{< alert color="caution" title="Caution" >}}
پیش از نسخهٔ v1.30 کوبرنتیز، AppArmor از طریق حاشیه‌نویسی‌ها تعیین می‌شد. برای مشاهدهٔ مستندات مربوط به این API منسوخ‌شده، از انتخابگر نسخهٔ مستندات استفاده کنید.
{{< /alert >}}

### پروفایل AppArmor در security context {#appArmorProfile}

فیلد `appArmorProfile` را می‌توانید در `securityContext` یک کانتینر یا در `securityContext` یک Pod تعیین کنید. اگر پروفایل در سطح Pod تنظیم شود، به‌عنوان پروفایل پیش‌فرض برای همهٔ کانتینرهای آن Pod (از جمله کانتینرهای init، sidecar و ephemeral) استفاده می‌شود. اگر هم پروفایل AppArmor در سطح Pod و هم در سطح کانتینر تنظیم شده باشد، پروفایل کانتینر استفاده می‌شود.

هر پروفایل AppArmor دو فیلد دارد:

فیلد `type` _(الزامی)_ - نوع پروفایل AppArmor را که اعمال خواهد شد مشخص می‌کند. گزینه‌های معتبر عبارت‌اند از:

`Localhost`
: پروفایلی که از پیش روی نود بارگذاری شده است (با `localhostProfile` تعیین می‌شود).

`RuntimeDefault`
: پروفایل پیش‌فرض محیط اجرای کانتینر.

`Unconfined`
: بدون اعمال AppArmor.

فیلد `localhostProfile` - نام پروفایلی که روی نود بارگذاری شده است و باید استفاده شود. برای کارکرد درست، این پروفایل باید از پیش روی نود پیکربندی شده باشد. این گزینه باید تنها و تنها زمانی ارائه شود که مقدار `type` برابر با `Localhost` باشد.


## {{% heading "whatsnext" %}}


منابع بیشتر:

* [راهنمای سریع زبان پروفایل AppArmor](https://gitlab.com/apparmor/apparmor/wikis/QuickProfileLanguage)
* [مرجع سیاست‌های اصلی AppArmor](https://gitlab.com/apparmor/apparmor/wikis/Policy_Layout)
