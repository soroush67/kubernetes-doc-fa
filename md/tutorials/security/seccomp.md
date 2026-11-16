---
reviewers:
- hasheddan
- pjbgf
- saschagrunert
title: محدود کردن فراخوانی‌های سیستمی یک کانتینر با seccomp
content_type: tutorial
weight: 40
min-kubernetes-server-version: v1.22
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.19" state="stable" >}}

واژهٔ Seccomp مخفف secure computing mode (حالت محاسبات امن) است و از نسخهٔ 2.6.12 یکی از قابلیت‌های هستهٔ لینوکس به شمار می‌رود. با آن می‌توان امتیازات (privileges) یک فرایند را در یک محیط ایزوله (sandbox) محدود کرد و فراخوانی‌هایی را که فرایند می‌تواند از فضای کاربر (userspace) به هسته انجام دهد، محدود ساخت. کوبرنتیز به شما امکان می‌دهد پروفایل‌های seccomp بارگذاری‌شده روی یک {{< glossary_tooltip text="نود" term_id="node" >}} را به‌طور خودکار روی Podها و کانتینرهای خود اعمال کنید.

تشخیص امتیازاتی که بارهای کاری شما به آن‌ها نیاز دارند، ممکن است دشوار باشد. در این آموزش یاد می‌گیرید که چگونه پروفایل‌های seccomp را در یک کلاستر محلی کوبرنتیز بارگذاری کنید، چگونه آن‌ها را روی یک Pod اعمال کنید و چگونه ساختن پروفایل‌هایی را آغاز کنید که فقط امتیازات لازم را به فرایندهای کانتینر شما می‌دهند.

## {{% heading "objectives" %}}

* یاد بگیرید که چگونه پروفایل‌های seccomp را روی یک نود بارگذاری کنید
* یاد بگیرید که چگونه یک پروفایل seccomp را روی یک کانتینر اعمال کنید
* ممیزی (auditing) فراخوانی‌های سیستمی (syscall) انجام‌شده توسط فرایند یک کانتینر را مشاهده کنید
* رفتار سیستم را هنگامی که پروفایلی ناموجود مشخص شده است، مشاهده کنید
* نقض یک پروفایل seccomp را مشاهده کنید
* یاد بگیرید که چگونه پروفایل‌های seccomp دقیق و جزئی‌نگر بسازید
* یاد بگیرید که چگونه پروفایل seccomp پیش‌فرض محیط اجرای کانتینر را اعمال کنید

## {{% heading "prerequisites" %}}

برای انجام همهٔ مراحل این آموزش، باید [kind](/docs/tasks/tools/#kind) و [kubectl](/docs/tasks/tools/#kubectl) را نصب کنید.

فرمان‌های این آموزش فرض می‌کنند که از [Docker](https://www.docker.com/) به‌عنوان محیط اجرای کانتینر استفاده می‌کنید. (کلاستری که `kind` می‌سازد ممکن است در درون خود از محیط اجرای کانتینر دیگری استفاده کند.) می‌توانید از [Podman](https://podman.io/) نیز استفاده کنید، اما در آن صورت برای انجام موفق کارها باید [دستورالعمل‌های](https://kind.sigs.k8s.io/docs/user/rootless/) ویژه‌ای را دنبال کنید.

این آموزش چند نمونه را نشان می‌دهد که هنوز در مرحلهٔ بتا هستند (از نسخهٔ v1.25) و نمونه‌های دیگری که فقط از قابلیت‌های seccomp عرضه‌شدهٔ عمومی (generally available) استفاده می‌کنند. باید مطمئن شوید که کلاستر شما برای نسخه‌ای که استفاده می‌کنید [به‌درستی پیکربندی شده است](https://kind.sigs.k8s.io/docs/user/quick-start/#setting-kubernetes-version).

همچنین در این آموزش از ابزار `curl` برای دانلود نمونه‌ها روی رایانهٔ شما استفاده می‌شود. اگر ترجیح می‌دهید، می‌توانید مراحل را برای استفاده از ابزار دیگری تطبیق دهید.

{{< alert color="info" title="Note" >}}
نمی‌توان پروفایل seccomp را روی کانتینری اعمال کرد که با تنظیم `privileged: true` در `securityContext` آن اجرا می‌شود. کانتینرهای ممتاز (privileged) همیشه به‌صورت `Unconfined` اجرا می‌شوند.
{{< /alert >}}

<!-- steps -->

## دانلود پروفایل‌های نمونهٔ seccomp {#download-profiles}

محتوای این پروفایل‌ها را بعداً بررسی خواهیم کرد، اما فعلاً آن‌ها را در پوشه‌ای به نام `profiles/` دانلود کنید تا بتوان آن‌ها را در کلاستر بارگذاری کرد.

{{< tabs name="tab_with_code" >}}
{{< tab name="audit.json" >}}
{{% code_sample file="pods/security/seccomp/profiles/audit.json" %}}
{{< /tab >}}
{{< tab name="violation.json" >}}
{{% code_sample file="pods/security/seccomp/profiles/violation.json" %}}
{{< /tab >}}
{{< tab name="fine-grained.json" >}}
{{% code_sample file="pods/security/seccomp/profiles/fine-grained.json" %}}
{{< /tab >}}
{{< /tabs >}}

این فرمان‌ها را اجرا کنید:

```shell
mkdir ./profiles
curl -L -o profiles/audit.json https://k8s.io/examples/pods/security/seccomp/profiles/audit.json
curl -L -o profiles/violation.json https://k8s.io/examples/pods/security/seccomp/profiles/violation.json
curl -L -o profiles/fine-grained.json https://k8s.io/examples/pods/security/seccomp/profiles/fine-grained.json
ls profiles
```

در پایان آخرین مرحله باید سه پروفایل را در فهرست ببینید:
```
audit.json  fine-grained.json  violation.json
```

## ساخت یک کلاستر محلی کوبرنتیز با kind

برای سادگی، می‌توان از [kind](https://kind.sigs.k8s.io/) برای ساخت یک کلاستر تک‌نودی استفاده کرد که پروفایل‌های seccomp در آن بارگذاری شده‌اند. ابزار kind کوبرنتیز را درون Docker اجرا می‌کند، بنابراین هر نود کلاستر یک کانتینر است. به این ترتیب می‌توان فایل‌ها را در سیستم فایل هر کانتینر سوار (mount) کرد؛ کاری مشابه بارگذاری فایل‌ها روی یک نود.

{{% code_sample file="pods/security/seccomp/kind.yaml" %}}

این پیکربندی نمونهٔ kind را دانلود کنید و آن را در فایلی به نام `kind.yaml` ذخیره کنید:
```shell
curl -L -O https://k8s.io/examples/pods/security/seccomp/kind.yaml
```

با تنظیم ایمیج کانتینر نود می‌توانید نسخهٔ مشخصی از کوبرنتیز را تعیین کنید. برای جزئیات بیشتر، بخش [نودها](https://kind.sigs.k8s.io/docs/user/configuration/#nodes) را در مستندات پیکربندی kind ببینید. این آموزش فرض می‌کند که از کوبرنتیز {{< param "version" >}} استفاده می‌کنید.

به‌عنوان یک قابلیت بتا، می‌توانید کوبرنتیز را طوری پیکربندی کنید که به‌جای بازگشت به `Unconfined`، از پروفایلی استفاده کند که {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} به‌طور پیش‌فرض ترجیح می‌دهد. اگر می‌خواهید این کار را امتحان کنید، پیش از ادامه، بخش [فعال‌سازی استفاده از `RuntimeDefault` به‌عنوان پروفایل seccomp پیش‌فرض برای همهٔ بارهای کاری](#enable-the-use-of-runtimedefault-as-the-default-seccomp-profile-for-all-workloads) را ببینید.

پس از آماده شدن پیکربندی kind، کلاستر kind را با آن پیکربندی بسازید:

```shell
kind create cluster --config=kind.yaml
```

پس از آماده شدن کلاستر جدید کوبرنتیز، کانتینر Docker را که به‌عنوان کلاستر تک‌نودی اجرا می‌شود، شناسایی کنید:

```shell
docker ps
```

باید خروجی‌ای ببینید که نشان می‌دهد کانتینری با نام `kind-control-plane` در حال اجراست. خروجی مشابه این است:

```
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                       NAMES
6a96207fed4b        kindest/node:v1.18.2   "/usr/local/bin/entr…"   27 seconds ago      Up 24 seconds       127.0.0.1:42223->6443/tcp   kind-control-plane
```

اگر سیستم فایل آن کانتینر را بررسی کنید، باید ببینید که پوشهٔ `profiles/` با موفقیت در مسیر پیش‌فرض seccomp مربوط به kubelet بارگذاری شده است. برای اجرای یک فرمان در Pod از `docker exec` استفاده کنید:

```shell
docker exec -it kind-control-plane ls /var/lib/kubelet/seccomp/profiles
```

```
audit.json  fine-grained.json  violation.json
```

اکنون تأیید کرده‌اید که این پروفایل‌های seccomp در دسترس kubelet در حال اجرا درون kind هستند.

## ساخت یک Pod که از پروفایل seccomp پیش‌فرض محیط اجرای کانتینر استفاده می‌کند

بیشتر محیط‌های اجرای کانتینر مجموعه‌ای معقول از فراخوانی‌های سیستمی پیش‌فرض مجاز و غیرمجاز فراهم می‌کنند. با تنظیم نوع seccomp در زمینهٔ امنیتی (security context) یک Pod یا کانتینر روی `RuntimeDefault`، می‌توانید این پیش‌فرض‌ها را برای بار کاری خود به کار بگیرید.

{{< alert color="info" title="Note" >}}
اگر [پیکربندی](/docs/reference/config-api/kubelet-config.v1beta1/) `seccompDefault` را فعال کرده باشید، Podها هرگاه پروفایل seccomp دیگری مشخص نشده باشد، از پروفایل seccomp `RuntimeDefault` استفاده می‌کنند. در غیر این صورت، مقدار پیش‌فرض `Unconfined` است.
{{< /alert >}}

این مانیفست یک Pod است که پروفایل seccomp `RuntimeDefault` را برای همهٔ کانتینرهای خود درخواست می‌کند:

{{% code_sample file="pods/security/seccomp/ga/default-pod.yaml" %}}

آن Pod را بسازید:
```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/default-pod.yaml
```

```shell
kubectl get pod default-pod
```

باید ببینید که Pod با موفقیت آغاز به کار کرده است:
```
NAME        READY   STATUS    RESTARTS   AGE
default-pod 1/1     Running   0          20s
```

پیش از رفتن به بخش بعدی، Pod را حذف کنید:

```shell
kubectl delete pod default-pod --wait --now
```

## ساخت یک Pod با پروفایل seccomp برای ممیزی فراخوانی‌های سیستمی

برای شروع، پروفایل `audit.json` را که همهٔ فراخوانی‌های سیستمی فرایند را ثبت می‌کند، روی یک Pod جدید اعمال کنید.

این مانیفست آن Pod است:

{{% code_sample file="pods/security/seccomp/ga/audit-pod.yaml" %}}

{{< alert color="info" title="Note" >}}
نسخه‌های قدیمی‌تر کوبرنتیز امکان پیکربندی رفتار seccomp را با {{< glossary_tooltip text="حاشیه‌نویسی‌ها" term_id="annotation" >}} فراهم می‌کردند. کوبرنتیز {{< skew currentVersion >}} برای پیکربندی seccomp فقط از فیلدهای درون `.spec.securityContext` پشتیبانی می‌کند و این آموزش همین روش را توضیح می‌دهد.
{{< /alert >}}

Pod را در کلاستر بسازید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/audit-pod.yaml
```

این پروفایل هیچ فراخوانی سیستمی را محدود نمی‌کند، بنابراین Pod باید با موفقیت آغاز به کار کند.

```shell
kubectl get pod audit-pod
```

```
NAME        READY   STATUS    RESTARTS   AGE
audit-pod   1/1     Running   0          30s
```

برای اینکه بتوانید با نقطهٔ پایانی (endpoint) که این کانتینر در معرض دسترسی قرار داده است تعامل کنید، یک {{< glossary_tooltip text="Service" term_id="service" >}} از نوع NodePort بسازید که دسترسی به این نقطهٔ پایانی را از درون کانتینر control plane کلاستر kind ممکن می‌کند.

```shell
kubectl expose pod audit-pod --type NodePort --port 5678
```

بررسی کنید که چه پورتی روی نود به Service اختصاص یافته است.

```shell
kubectl get service audit-pod
```

خروجی مشابه این است:
```
NAME        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
audit-pod   NodePort   10.111.36.142   <none>        5678:32373/TCP   72s
```

اکنون می‌توانید با `curl` از درون کانتینر control plane کلاستر kind و از طریق پورتی که این Service در معرض دسترسی قرار داده است، به آن نقطهٔ پایانی دسترسی پیدا کنید. برای اجرای فرمان `curl` درون کانتینر control plane از `docker exec` استفاده کنید:

```shell
# Change 32373 to the port number you saw from "kubectl get service audit-pod"
docker exec -it kind-control-plane curl localhost:32373
```

```
just made some syscalls!
```

می‌بینید که فرایند در حال اجراست، اما در واقع چه فراخوانی‌های سیستمی‌ای انجام داده است؟ از آنجا که این Pod در یک کلاستر محلی اجرا می‌شود، باید بتوانید این فراخوانی‌ها را در `/var/log/syslog` روی سیستم محلی خود ببینید. یک پنجرهٔ ترمینال جدید باز کنید و با `tail` خروجی را برای فراخوانی‌های `http-echo` دنبال کنید:

```shell
# The log path on your computer might be different from "/var/log/syslog"
tail -f /var/log/syslog | grep 'http-echo'
```

باید همین حالا چند گزارش از فراخوانی‌های سیستمی انجام‌شده توسط `http-echo` ببینید و اگر دوباره `curl` را درون کانتینر control plane اجرا کنید، خروجی بیشتری در گزارش نوشته می‌شود.

برای نمونه:
```
Jul  6 15:37:40 my-machine kernel: [369128.669452] audit: type=1326 audit(1594067860.484:14536): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=51 compat=0 ip=0x46fe1f code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669453] audit: type=1326 audit(1594067860.484:14537): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=54 compat=0 ip=0x46fdba code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669455] audit: type=1326 audit(1594067860.484:14538): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=202 compat=0 ip=0x455e53 code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669456] audit: type=1326 audit(1594067860.484:14539): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=288 compat=0 ip=0x46fdba code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669517] audit: type=1326 audit(1594067860.484:14540): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=0 compat=0 ip=0x46fd44 code=0x7ffc0000
Jul  6 15:37:40 my-machine kernel: [369128.669519] audit: type=1326 audit(1594067860.484:14541): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=270 compat=0 ip=0x4559b1 code=0x7ffc0000
Jul  6 15:38:40 my-machine kernel: [369188.671648] audit: type=1326 audit(1594067920.488:14559): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=270 compat=0 ip=0x4559b1 code=0x7ffc0000
Jul  6 15:38:40 my-machine kernel: [369188.671726] audit: type=1326 audit(1594067920.488:14560): auid=4294967295 uid=0 gid=0 ses=4294967295 pid=29064 comm="http-echo" exe="/http-echo" sig=0 arch=c000003e syscall=202 compat=0 ip=0x455e53 code=0x7ffc0000
```

با نگاه کردن به مقدار `syscall=` در هر خط، می‌توانید کم‌کم فراخوانی‌های سیستمی موردنیاز فرایند `http-echo` را بشناسید. هرچند بعید است این موارد همهٔ فراخوانی‌های سیستمی آن را دربر بگیرند، می‌توانند پایه‌ای برای ساخت یک پروفایل seccomp برای این کانتینر باشند.

پیش از رفتن به بخش بعدی، Service و Pod را حذف کنید:

```shell
kubectl delete service audit-pod --wait
kubectl delete pod audit-pod --wait --now
```

## ساخت یک Pod با پروفایل seccomp که باعث نقض می‌شود

برای نمایش، پروفایلی را روی Pod اعمال کنید که هیچ فراخوانی سیستمی را مجاز نمی‌داند.

مانیفست این نمایش چنین است:

{{% code_sample file="pods/security/seccomp/ga/violation-pod.yaml" %}}

تلاش کنید Pod را در کلاستر بسازید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/violation-pod.yaml
```

Pod ساخته می‌شود، اما مشکلی وجود دارد. اگر وضعیت Pod را بررسی کنید، باید ببینید که آغاز به کار آن ناموفق بوده است.

```shell
kubectl get pod violation-pod
```

```
NAME            READY   STATUS             RESTARTS   AGE
violation-pod   0/1     CrashLoopBackOff   1          6s
```

همان‌طور که در نمونهٔ قبلی دیدید، فرایند `http-echo` به فراخوانی‌های سیستمی نسبتاً زیادی نیاز دارد. در اینجا با تنظیم `"defaultAction": "SCMP_ACT_ERRNO"` به seccomp دستور داده شده است که در برابر هر فراخوانی سیستمی خطا برگرداند. این کار بسیار امن است، اما امکان انجام هر کار معناداری را از بین می‌برد. آنچه واقعاً می‌خواهید این است که فقط امتیازات موردنیاز بارهای کاری را به آن‌ها بدهید.

پیش از رفتن به بخش بعدی، Pod را حذف کنید:

```shell
kubectl delete pod violation-pod --wait --now
```

## ساخت یک Pod با پروفایل seccomp که فقط فراخوانی‌های سیستمی لازم را مجاز می‌داند

اگر نگاهی به پروفایل `fine-grained.json` بیندازید، برخی از فراخوانی‌های سیستمی را خواهید دید که در syslog نمونهٔ اول مشاهده شدند؛ نمونه‌ای که در آن پروفایل مقدار `"defaultAction":
"SCMP_ACT_LOG"` را تنظیم کرده بود. اکنون پروفایل مقدار `"defaultAction": "SCMP_ACT_ERRNO"` را تنظیم می‌کند، اما مجموعه‌ای از فراخوانی‌های سیستمی را به‌صراحت در بلوک `"action": "SCMP_ACT_ALLOW"` مجاز می‌داند. در حالت ایدئال، کانتینر با موفقیت اجرا می‌شود و هیچ پیامی به `syslog` فرستاده نمی‌شود.

مانیفست این نمونه چنین است:

{{% code_sample file="pods/security/seccomp/ga/fine-pod.yaml" %}}

Pod را در کلاستر خود بسازید:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/fine-pod.yaml
```

```shell
kubectl get pod fine-pod
```

باید ببینید که Pod با موفقیت آغاز به کار کرده است:
```
NAME        READY   STATUS    RESTARTS   AGE
fine-pod   1/1     Running   0          30s
```

یک پنجرهٔ ترمینال جدید باز کنید و با `tail` مدخل‌هایی از گزارش را که به فراخوانی‌های `http-echo` اشاره می‌کنند، زیر نظر بگیرید:

```shell
# The log path on your computer might be different from "/var/log/syslog"
tail -f /var/log/syslog | grep 'http-echo'
```

سپس Pod را با یک Service از نوع NodePort در معرض دسترسی قرار دهید:

```shell
kubectl expose pod fine-pod --type NodePort --port 5678
```

بررسی کنید که چه پورتی روی نود به Service اختصاص یافته است:

```shell
kubectl get service fine-pod
```

خروجی مشابه این است:
```
NAME        TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
fine-pod    NodePort   10.111.36.142   <none>        5678:32373/TCP   72s
```

با `curl` از درون کانتینر control plane کلاستر kind به آن نقطهٔ پایانی دسترسی پیدا کنید:

```shell
# Change 32373 to the port number you saw from "kubectl get service fine-pod"
docker exec -it kind-control-plane curl localhost:32373
```

```
just made some syscalls!
```

نباید هیچ خروجی‌ای در `syslog` ببینید. دلیلش این است که پروفایل همهٔ فراخوانی‌های سیستمی لازم را مجاز دانسته و مشخص کرده است که اگر فراخوانی‌ای خارج از این فهرست انجام شود، خطا رخ دهد. این وضعیت از دیدگاه امنیتی ایدئال است، اما به تلاشی برای تحلیل برنامه نیاز داشت. خوب بود اگر راه ساده‌ای وجود داشت که بدون این‌همه تلاش، به چنین سطحی از امنیت نزدیک‌تر شویم.

پیش از رفتن به بخش بعدی، Service و Pod را حذف کنید:

```shell
kubectl delete service fine-pod --wait
kubectl delete pod fine-pod --wait --now
```

## فعال‌سازی استفاده از `RuntimeDefault` به‌عنوان پروفایل پیش‌فرض seccomp برای همهٔ بارهای کاری

{{< feature-state state="stable" for_k8s_version="v1.27" >}}

برای استفاده از پروفایل پیش‌فرض seccomp، باید kubelet را روی هر نودی که می‌خواهید از این قابلیت در آن استفاده کنید، با
[پرچم خط فرمان](/docs/reference/command-line-tools-reference/kubelet)
`--seccomp-default` اجرا کنید.

در صورت فعال بودن این قابلیت، kubelet به‌جای حالت `Unconfined` (غیرفعال بودن seccomp)، به‌طور پیش‌فرض از پروفایل seccomp با نام `RuntimeDefault` استفاده می‌کند. این پروفایل را محیط اجرای کانتینر تعریف می‌کند. هدف پروفایل‌های پیش‌فرض این است که مجموعه‌ای قوی از پیش‌فرض‌های امنیتی فراهم کنند و در عین حال کارکرد بار کاری را حفظ کنند. ممکن است پروفایل‌های پیش‌فرض در محیط‌های اجرای کانتینر مختلف و نسخه‌های انتشار آن‌ها با یکدیگر متفاوت باشند؛ برای نمونه، پروفایل‌های CRI-O و containerd با هم تفاوت دارند.

{{< alert color="info" title="Note" >}}
فعال‌سازی این قابلیت نه فیلد `securityContext.seccompProfile` در API کوبرنتیز را تغییر می‌دهد و نه حاشیه‌نویسی‌های (annotations) منسوخ‌شده را به بار کاری اضافه می‌کند. به این ترتیب، کاربران می‌توانند هر زمان که بخواهند، بدون تغییر واقعی در پیکربندی بار کاری، تغییرات را به حالت قبل بازگردانند. برای بررسی اینکه یک کانتینر از کدام پروفایل seccomp استفاده می‌کند، می‌توانید از ابزارهایی مانند
[`crictl inspect`](https://github.com/kubernetes-sigs/cri-tools) استفاده کنید.
{{< /alert >}}

برخی بارهای کاری ممکن است در مقایسه با بقیه به محدودیت‌های کمتری روی فراخوانی‌های سیستمی (syscall) نیاز داشته باشند. بنابراین ممکن است این بارهای کاری حتی با پروفایل `RuntimeDefault` نیز در زمان اجرا با شکست مواجه شوند. برای کاهش احتمال چنین شکستی می‌توانید:

- بار کاری را به‌صورت صریح در حالت `Unconfined` اجرا کنید.
- قابلیت `SeccompDefault` را برای نودها غیرفعال کنید و همچنین اطمینان حاصل کنید که بارهای کاری روی نودهایی زمان‌بندی می‌شوند که این قابلیت در آن‌ها غیرفعال است.
- یک پروفایل seccomp سفارشی برای بار کاری بسازید.

اگر این قابلیت را در کلاستری مشابه محیط عملیاتی به کار می‌گیرید، پروژهٔ کوبرنتیز توصیه می‌کند که ابتدا این feature gate را روی زیرمجموعه‌ای از نودهای خود فعال کنید و اجرای بارهای کاری را آزمایش کنید و سپس این تغییر را در کل کلاستر اعمال کنید.

اطلاعات دقیق‌تر دربارهٔ راهبرد احتمالی ارتقا و بازگشت به نسخهٔ قبلی را می‌توانید در پیشنهاد بهبود کوبرنتیز (Kubernetes Enhancement Proposal یا KEP) مرتبط بیابید:
[Enable seccomp by default](https://github.com/kubernetes/enhancements/tree/9a124fd29d1f9ddf2ff455c49a630e3181992c25/keps/sig-node/2413-seccomp-by-default#upgrade--downgrade-strategy).

در کوبرنتیز {{< skew currentVersion >}} می‌توانید پروفایل seccomp را پیکربندی کنید که هنگام تعریف نشدن پروفایل seccomp مشخصی در spec یک Pod اعمال می‌شود. با این حال، همچنان باید این رفتار پیش‌فرض را برای هر نودی که می‌خواهید از آن استفاده کنید، فعال کنید.

اگر کلاستری با کوبرنتیز {{< skew currentVersion >}} اجرا می‌کنید و می‌خواهید این قابلیت را فعال کنید، یا kubelet را با پرچم خط فرمان `--seccomp-default` اجرا کنید، یا این قابلیت را از طریق [فایل پیکربندی kubelet](/docs/tasks/administer-cluster/kubelet-config-file/) فعال کنید. برای فعال‌سازی این feature gate در [kind](https://kind.sigs.k8s.io)، اطمینان حاصل کنید که `kind` حداقل نسخهٔ موردنیاز کوبرنتیز را فراهم می‌کند و قابلیت `SeccompDefault` را
[در پیکربندی kind](https://kind.sigs.k8s.io/docs/user/quick-start/#enable-feature-gates-in-your-cluster) فعال می‌کند:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    image: kindest/node:v1.28.0@sha256:9f3ff58f19dcf1a0611d11e8ac989fdb30a28f40f236f59f0bea31fb956ccf5c
    kubeadmConfigPatches:
      - |
        kind: JoinConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            seccomp-default: "true"
  - role: worker
    image: kindest/node:v1.28.0@sha256:9f3ff58f19dcf1a0611d11e8ac989fdb30a28f40f236f59f0bea31fb956ccf5c
    kubeadmConfigPatches:
      - |
        kind: JoinConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            seccomp-default: "true"
```

اگر کلاستر آماده باشد، پادی که به این شکل اجرا شود:

```shell
kubectl run --rm -it --restart=Never --image=alpine alpine -- sh
```

اکنون باید پروفایل پیش‌فرض seccomp را به همراه داشته باشد. برای بررسی این موضوع می‌توانید با `docker exec` دستور `crictl inspect` را برای کانتینر روی نود worker در kind اجرا کنید:

```shell
docker exec -it kind-worker bash -c \
    'crictl inspect $(crictl ps --name=alpine -q) | jq .info.runtimeSpec.linux.seccomp'
```

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64", "SCMP_ARCH_X86", "SCMP_ARCH_X32"],
  "syscalls": [
    {
      "names": ["..."]
    }
  ]
}
```

## {{% heading "whatsnext" %}}

برای آشنایی بیشتر با seccomp در لینوکس می‌توانید این منابع را مطالعه کنید:

* [مروری بر seccomp](https://lwn.net/Articles/656307/)
* [پروفایل‌های امنیتی Seccomp برای Docker](https://docs.docker.com/engine/security/seccomp/)
