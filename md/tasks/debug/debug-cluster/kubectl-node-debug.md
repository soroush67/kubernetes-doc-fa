---
title: اشکال‌زدایی نودهای کوبرنتیز با kubectl
content_type: task
min-kubernetes-server-version: 1.20
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان با فرمان `kubectl debug`، یک [نود](/docs/concepts/architecture/nodes/) در حال اجرا در کلاستر کوبرنتیز را اشکال‌زدایی کرد.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

باید مجوز ایجاد Podها و تخصیص این Podهای جدید به نودهای دلخواه را داشته باشید.
همچنین باید مجاز به ایجاد Podهایی باشید که به فایل‌سیستم‌های میزبان دسترسی دارند.


<!-- steps -->

## اشکال‌زدایی یک نود با `kubectl debug node`

برای استقرار یک Pod روی نودی که می‌خواهید عیب‌یابی کنید، از فرمان `kubectl debug node` استفاده کنید.
این فرمان در شرایطی که نمی‌توانید از طریق اتصال SSH به نود خود دسترسی پیدا کنید، کارآمد است.
پس از ایجاد Pod، یک پوسته (shell) تعاملی روی نود باز می‌شود.
برای ایجاد یک پوسته تعاملی روی نودی با نام «mynode»، فرمان زیر را اجرا کنید:

```shell
kubectl debug node/mynode -it --image=ubuntu
```

```console
Creating debugging pod node-debugger-mynode-pdx84 with container debugger on node mynode.
If you don't see a command prompt, try pressing enter.
root@mynode:/#
```

فرمان debug به گردآوری اطلاعات و عیب‌یابی مشکلات کمک می‌کند. از جمله فرمان‌هایی که ممکن است به کار ببرید می‌توان به `ip`، `ifconfig`، `nc`، `ping`، `ps` و مانند آن‌ها اشاره کرد. همچنین می‌توانید ابزارهای دیگری مانند `mtr`، `tcpdump` و `curl` را از طریق مدیر بسته مربوط نصب کنید.

{{< note >}}

فرمان‌های اشکال‌زدایی بسته به ایمیجی که Pod اشکال‌زدایی از آن استفاده می‌کند، ممکن است متفاوت باشند و شاید لازم باشد این فرمان‌ها را نصب کنید.

{{< /note >}}

Pod اشکال‌زدایی به فایل‌سیستم ریشه نود دسترسی دارد که در مسیر `/host` درون Pod سوار (mount) شده است.
اگر kubelet را در یک فضای نام (namespace) فایل‌سیستم اجرا کنید، Pod اشکال‌زدایی ریشه همان فضای نام را می‌بیند، نه ریشه کل نود را. در یک نود لینوکسی معمول، می‌توانید برای یافتن لاگ‌های مرتبط به مسیرهای زیر مراجعه کنید:

`/host/var/log/kubelet.log`
: لاگ‌های `kubelet` که مسئول اجرای کانتینرها روی نود است.

`/host/var/log/kube-proxy.log`
: لاگ‌های `kube-proxy` که مسئول هدایت ترافیک به endpointهای Service است.

`/host/var/log/containerd.log`
: لاگ‌های فرایند `containerd` که روی نود اجرا می‌شود.

`/host/var/log/syslog`
: پیام‌ها و اطلاعات عمومی سیستم را نشان می‌دهد.

`/host/var/log/kern.log`
: لاگ‌های هسته (kernel) را نشان می‌دهد.

هنگام ایجاد یک نشست اشکال‌زدایی روی نود، به نکات زیر توجه کنید:

* فرمان `kubectl debug` نام Pod جدید را بر اساس نام نود به‌طور خودکار تولید می‌کند.
* فایل‌سیستم ریشه نود در مسیر `/host` سوار می‌شود.
* با اینکه کانتینر در فضاهای نام IPC، Network و PID میزبان اجرا می‌شود، Pod دارای امتیاز ویژه (privileged) نیست. بنابراین ممکن است خواندن برخی اطلاعات فرایندها با شکست روبه‌رو شود، زیرا دسترسی به این اطلاعات فقط به کاربران ارشد (superuser) محدود است. برای مثال، فرمان `chroot /host` با شکست روبه‌رو خواهد شد. اگر به یک Pod دارای امتیاز ویژه نیاز دارید، آن را به‌صورت دستی ایجاد کنید یا از پرچم `--profile=sysadmin` استفاده کنید.
* با به‌کارگیری [پروفایل‌های اشکال‌زدایی](/docs/tasks/debug/debug-application/debug-running-pod/#debugging-profiles) می‌توانید ویژگی‌های مشخصی مانند [securityContext](/docs/tasks/configure-pod-container/security-context/) را برای Pod اشکال‌زدایی تنظیم کنید.

## {{% heading "cleanup" %}}

پس از پایان کار با Pod اشکال‌زدایی، آن را حذف کنید:

```shell
kubectl get pods
```

```none
NAME                          READY   STATUS       RESTARTS   AGE
node-debugger-mynode-pdx84    0/1     Completed    0          8m1s
```	

```shell
# Change the pod name accordingly
kubectl delete pod node-debugger-mynode-pdx84 --now
```	

```none
pod "node-debugger-mynode-pdx84" deleted
```

{{< note >}}

اگر نود از کار افتاده باشد (مثلاً از شبکه قطع شده باشد، یا kubelet متوقف شده و دوباره راه‌اندازی نشود و مانند آن)، فرمان `kubectl debug node` کار نخواهد کرد.
در این حالت، به بخش [اشکال‌زدایی یک نود از کار افتاده یا غیرقابل دسترس](/docs/tasks/debug/debug-cluster/#example-debugging-a-down-unreachable-node) مراجعه کنید.

{{< /note >}}
