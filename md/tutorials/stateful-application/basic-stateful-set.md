---
reviewers:
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: مبانی StatefulSet
content_type: tutorial
weight: 10
---

<!-- overview -->
این آموزش مقدمه‌ای بر مدیریت برنامه‌ها با
{{< glossary_tooltip text="StatefulSetها" term_id="statefulset" >}} است.
در این آموزش نشان داده می‌شود که چگونه Podهای StatefulSetها را ایجاد، حذف، مقیاس‌دهی و به‌روزرسانی کنید.


## {{% heading "prerequisites" %}}

پیش از شروع این آموزش، بهتر است با مفاهیم زیر در کوبرنتیز آشنا شوید:

* [Podها](/docs/concepts/workloads/pods/)
* [DNS کلاستر](/docs/concepts/services-networking/dns-pod-service/)
* [Serviceهای Headless](/docs/concepts/services-networking/service/#headless-services)
* [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/)
* [تأمین PersistentVolumeها](/docs/concepts/storage/dynamic-provisioning/)
* ابزار خط فرمان [kubectl](/docs/reference/kubectl/kubectl/)

{{% include "task-tutorial-prereqs.md" %}}
باید `kubectl` را طوری پیکربندی کنید که از یک context با فضای نام (namespace) `default` استفاده کند.
اگر از یک کلاستر موجود استفاده می‌کنید، مطمئن شوید که استفاده از فضای نام پیش‌فرض آن کلاستر برای تمرین مشکلی ایجاد نمی‌کند. بهتر است در کلاستری تمرین کنید که هیچ بار کاری واقعی روی آن اجرا نمی‌شود.

همچنین خواندن صفحهٔ مفهومی [StatefulSetها](/docs/concepts/workloads/controllers/statefulset/) مفید است.

{{< alert color="info" title="Note" >}}
این آموزش فرض می‌کند که کلاستر شما برای تأمین پویای PersistentVolumeها پیکربندی شده است. همچنین به یک [StorageClass پیش‌فرض](/docs/concepts/storage/storage-classes/#default-storageclass) نیاز دارید.
اگر کلاستر شما برای تأمین پویای ذخیره‌سازی پیکربندی نشده است، باید پیش از شروع این آموزش دو حجم (volume) یک گیبی‌بایتی را به‌صورت دستی تأمین کنید و کلاستر خود را طوری تنظیم کنید که این PersistentVolumeها به الگوهای PersistentVolumeClaim تعریف‌شده در StatefulSet نگاشت شوند.
{{< /alert >}}

## {{% heading "objectives" %}}

StatefulSetها برای استفاده با برنامه‌های حالت‌مند (stateful) و سامانه‌های توزیع‌شده طراحی شده‌اند. با این حال، مدیریت برنامه‌های حالت‌مند و سامانه‌های توزیع‌شده روی کوبرنتیز موضوعی گسترده و پیچیده است. برای اینکه ویژگی‌های پایه‌ای StatefulSet را نشان دهیم و این دو موضوع را با هم درنیامیزیم، در این آموزش یک برنامهٔ وب ساده را با استفاده از یک StatefulSet مستقر می‌کنید.

پس از این آموزش، با موارد زیر آشنا خواهید شد:

* چگونگی ایجاد یک StatefulSet
* چگونگی مدیریت Podها به‌دست StatefulSet
* چگونگی حذف یک StatefulSet
* چگونگی مقیاس‌دهی یک StatefulSet
* چگونگی به‌روزرسانی Podهای یک StatefulSet

<!-- lessoncontent -->

## ایجاد یک StatefulSet

کار را با ایجاد یک StatefulSet (و Serviceای که به آن وابسته است) با استفاده از نمونهٔ زیر آغاز کنید. این نمونه شبیه نمونه‌ای است که در صفحهٔ مفهومی [StatefulSetها](/docs/concepts/workloads/controllers/statefulset/) آمده است.
این نمونه یک [Service از نوع headless](/docs/concepts/services-networking/service/#headless-services) به نام `nginx` ایجاد می‌کند تا نشانی‌های IP مربوط به Podهای StatefulSet با نام `web` را منتشر کند.

{{% code_sample file="application/web/web.yaml" %}}

باید دست‌کم از دو پنجرهٔ ترمینال استفاده کنید. در ترمینال اول، با استفاده از
[`kubectl get`](/docs/reference/generated/kubectl/kubectl-commands/#get) ایجاد Podهای StatefulSet را {{< glossary_tooltip text="پایش" term_id="watch" >}} کنید.

```shell
# use this terminal to run commands that specify --watch
# end this watch when you are asked to start a new watch
kubectl get pods --watch -l app=nginx
```

در ترمینال دوم، با استفاده از
[`kubectl apply`](/docs/reference/generated/kubectl/kubectl-commands/#apply) سرویس headless و StatefulSet را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/web/web.yaml
```
```
service/nginx created
statefulset.apps/web created
```

فرمان بالا دو Pod ایجاد می‌کند که هر کدام یک وب‌سرور [NGINX](https://www.nginx.com) را اجرا می‌کنند. ابتدا Service با نام `nginx` را دریافت کنید...
```shell
kubectl get service nginx
```
```
NAME      TYPE         CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
nginx     ClusterIP    None         <none>        80/TCP    12s
```
...سپس StatefulSet با نام `web` را دریافت کنید تا مطمئن شوید هر دو با موفقیت ایجاد شده‌اند:
```shell
kubectl get statefulset web
```
```
NAME   READY   AGE
web    2/2     37s
```

### ایجاد ترتیبی Podها

هر StatefulSet به‌طور پیش‌فرض Podهای خود را با ترتیبی دقیق ایجاد می‌کند.

در یک StatefulSet با _n_ رپلیکا، هنگام استقرار Podها، آن‌ها به‌صورت پی‌درپی و به ترتیب از _{0..n-1}_ ایجاد می‌شوند. خروجی فرمان `kubectl get` را در ترمینال اول بررسی کنید. در نهایت، خروجی شبیه نمونهٔ زیر خواهد بود.

```shell
# Do not start a new watch;
# this should already be running
kubectl get pods --watch -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     0/1       Pending   0          0s
web-0     0/1       Pending   0         0s
web-0     0/1       ContainerCreating   0         0s
web-0     1/1       Running   0         19s
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         18s
```

توجه کنید که Pod با نام `web-1` تا زمانی که Pod با نام `web-0` در وضعیت _Running_ (به [فاز Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) مراجعه کنید) و _Ready_ (به `type` در [شرایط Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) مراجعه کنید) قرار نگیرد، راه‌اندازی نمی‌شود.

در ادامهٔ این آموزش، [راه‌اندازی موازی](#parallel-pod-management) را نیز تمرین خواهید کرد.

{{< alert color="info" title="Note" >}}
برای پیکربندی عدد ترتیبی صحیحی که به هر Pod در یک StatefulSet اختصاص داده می‌شود، به [عدد ترتیبی آغازین](/docs/concepts/workloads/controllers/statefulset/#start-ordinal) مراجعه کنید.
{{< /alert >}}

## Podها در یک StatefulSet

هر Pod در یک StatefulSet یک شاخص ترتیبی یکتا و یک هویت شبکه‌ای پایدار دارد.

### بررسی شاخص ترتیبی Pod

Podهای StatefulSet را دریافت کنید:

```shell
kubectl get pods -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          1m
web-1     1/1       Running   0          1m
```

همان‌طور که در صفحهٔ مفهومی [StatefulSetها](/docs/concepts/workloads/controllers/statefulset/) گفته شد، Podهای یک StatefulSet هویتی ماندگار و یکتا دارند. این هویت بر پایهٔ یک شاخص ترتیبی یکتاست که {{< glossary_tooltip term_id="controller" text="کنترل‌کننده">}}ٔ StatefulSet به هر Pod اختصاص می‌دهد.  
نام Podها به شکل `<statefulset name>-<ordinal index>` است.
از آنجا که StatefulSet با نام `web` دو رپلیکا دارد، دو Pod با نام‌های `web-0` و `web-1` ایجاد می‌کند.

### استفاده از هویت‌های شبکه‌ای پایدار

هر Pod یک نام میزبان (hostname) پایدار بر پایهٔ شاخص ترتیبی خود دارد. با استفاده از
[`kubectl exec`](/docs/reference/generated/kubectl/kubectl-commands/#exec) فرمان `hostname` را در هر Pod اجرا کنید:

```shell
for i in 0 1; do kubectl exec "web-$i" -- sh -c 'hostname'; done
```
```
web-0
web-1
```

با استفاده از [`kubectl run`](/docs/reference/generated/kubectl/kubectl-commands/#run) کانتینری را اجرا کنید که فرمان `nslookup` را از بستهٔ `dnsutils` فراهم می‌کند.
با اجرای `nslookup` روی نام میزبان Podها می‌توانید نشانی‌های DNS درون‌کلاستری آن‌ها را بررسی کنید:

```shell
kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm
```
این فرمان یک پوستهٔ (shell) جدید باز می‌کند. در آن پوستهٔ جدید، این فرمان را اجرا کنید:
```shell
# Run this in the dns-test container shell
nslookup web-0.nginx
```
خروجی شبیه زیر است:
```
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-0.nginx
Address 1: 10.244.1.6

nslookup web-1.nginx
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-1.nginx
Address 1: 10.244.2.6
```

(و اکنون با `exit` از پوستهٔ کانتینر خارج شوید)

رکورد CNAME سرویس headless به رکوردهای SRV اشاره می‌کند (یک رکورد برای هر Podای که در وضعیت Running و Ready است). رکوردهای SRV نیز به رکوردهای A اشاره می‌کنند که نشانی‌های IP مربوط به Podها را در خود دارند.

در یک ترمینال، Podهای StatefulSet را پایش کنید:

```shell
# Start a new watch
# End this watch when you've seen that the delete is finished
kubectl get pod --watch -l app=nginx
```
در ترمینال دوم، با استفاده از
[`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands/#delete) همهٔ Podهای StatefulSet را حذف کنید:

```shell
kubectl delete pod -l app=nginx
```
```
pod "web-0" deleted
pod "web-1" deleted
```

صبر کنید تا StatefulSet آن‌ها را دوباره راه‌اندازی کند و هر دو Pod به وضعیت Running و Ready برسند:

```shell
# This should already be running
kubectl get pod --watch -l app=nginx
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     0/1       ContainerCreating   0          0s
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          2s
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         34s
```

با استفاده از `kubectl exec` و `kubectl run` نام میزبان Podها و ورودی‌های DNS درون‌کلاستری آن‌ها را مشاهده کنید. ابتدا نام میزبان Podها را ببینید:

```shell
for i in 0 1; do kubectl exec web-$i -- sh -c 'hostname'; done
```
```
web-0
web-1
```
سپس این فرمان را اجرا کنید:
```shell
kubectl run -i --tty --image busybox:1.28 dns-test --restart=Never --rm
```
این فرمان یک پوستهٔ جدید باز می‌کند.  
در آن پوستهٔ جدید، این فرمان را اجرا کنید:
```shell
# Run this in the dns-test container shell
nslookup web-0.nginx
```
خروجی شبیه زیر است:
```
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-0.nginx
Address 1: 10.244.1.7

nslookup web-1.nginx
Server:    10.0.0.10
Address 1: 10.0.0.10 kube-dns.kube-system.svc.cluster.local

Name:      web-1.nginx
Address 1: 10.244.2.8
```

(و اکنون با `exit` از پوستهٔ کانتینر خارج شوید)

اعداد ترتیبی، نام‌های میزبان، رکوردهای SRV و نام‌های رکورد A مربوط به Podها تغییری نکرده‌اند، اما ممکن است نشانی‌های IP مرتبط با Podها تغییر کرده باشند. در کلاستری که برای این آموزش استفاده شده، این نشانی‌ها تغییر کرده‌اند. به همین دلیل مهم است که برنامه‌های دیگر را طوری پیکربندی نکنید که از طریق نشانی IP یک Pod خاص به Podهای یک StatefulSet متصل شوند (اتصال به Podها از طریق تحلیل نام میزبان آن‌ها مشکلی ندارد).

#### کشف Podهای مشخص در یک StatefulSet

اگر لازم است اعضای فعال یک StatefulSet را پیدا کنید و به آن‌ها متصل شوید، باید رکورد CNAME سرویس headless (`nginx.default.svc.cluster.local`) را پرس‌وجو کنید. رکوردهای SRV مرتبط با این CNAME فقط شامل Podهایی از StatefulSet خواهند بود که در وضعیت Running و Ready هستند.

اگر برنامهٔ شما از قبل منطق اتصالی را پیاده‌سازی کرده است که زنده‌بودن (liveness) و آمادگی (readiness) را بررسی می‌کند، می‌توانید از رکوردهای SRV مربوط به Podها (`web-0.nginx.default.svc.cluster.local` و `web-1.nginx.default.svc.cluster.local`) استفاده کنید؛ زیرا این رکوردها پایدار هستند و برنامهٔ شما می‌تواند نشانی Podها را هنگامی که به وضعیت Running و Ready می‌رسند کشف کند.

اگر برنامهٔ شما می‌خواهد هر Pod سالمی را در یک StatefulSet پیدا کند و در نتیجه نیازی به ردگیری تک‌تک Podها ندارد، می‌توانید به نشانی IP یک Service از نوع `type: ClusterIP` متصل شوید که Podهای آن StatefulSet پشتیبان آن هستند. می‌توانید از همان Serviceای استفاده کنید که StatefulSet را ردگیری می‌کند (و در فیلد `serviceName` مربوط به StatefulSet مشخص شده است)، یا از یک Service جداگانه که مجموعهٔ درستی از Podها را انتخاب می‌کند.

### نوشتن در ذخیره‌سازی پایدار

PersistentVolumeClaimهای مربوط به `web-0` و `web-1` را دریافت کنید:

```shell
kubectl get pvc -l app=nginx
```
خروجی شبیه زیر است:
```
NAME        STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
www-web-0   Bound     pvc-15c268c7-b507-11e6-932f-42010a800002   1Gi        RWO           48s
www-web-1   Bound     pvc-15c79307-b507-11e6-932f-42010a800002   1Gi        RWO           48s
```

کنترل‌کنندهٔ StatefulSet دو
{{< glossary_tooltip text="PersistentVolumeClaim" term_id="persistent-volume-claim" >}}
ایجاد کرده است که به دو
{{< glossary_tooltip text="PersistentVolume" term_id="persistent-volume" >}}
متصل (bound) شده‌اند.

از آنجا که کلاستر استفاده‌شده در این آموزش برای تأمین پویای PersistentVolumeها پیکربندی شده است، این PersistentVolumeها به‌طور خودکار ایجاد و متصل شده‌اند.

وب‌سرور NGINX به‌طور پیش‌فرض یک فایل index را از مسیر `/usr/share/nginx/html/index.html` ارائه می‌کند. فیلد `volumeMounts` در `spec` مربوط به StatefulSet تضمین می‌کند که دایرکتوری `/usr/share/nginx/html` بر پایهٔ یک PersistentVolume باشد.

نام میزبان Podها را در فایل‌های `index.html` آن‌ها بنویسید و بررسی کنید که وب‌سرورهای NGINX این نام‌های میزبان را ارائه می‌کنند:

```shell
for i in 0 1; do kubectl exec "web-$i" -- sh -c 'echo "$(hostname)" > /usr/share/nginx/html/index.html'; done

for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```
```
web-0
web-1
```

{{< alert color="info" title="Note" >}}
اگر به‌جای آن برای فرمان curl بالا پاسخ‌های **403 Forbidden** دریافت کردید، باید مجوزهای دایرکتوری‌ای را که با `volumeMounts` سوار (mount) شده است اصلاح کنید (این مشکل ناشی از [باگی در هنگام استفاده از حجم‌های hostPath](https://github.com/kubernetes/kubernetes/issues/2630) است). برای این کار، فرمان زیر را اجرا کنید:

`for i in 0 1; do kubectl exec web-$i -- chmod 755 /usr/share/nginx/html; done`

و سپس فرمان `curl` بالا را دوباره امتحان کنید.
{{< /alert >}}

در یک ترمینال، Podهای StatefulSet را پایش کنید:

```shell
# End this watch when you've reached the end of the section.
# At the start of "Scaling a StatefulSet" you'll start a new watch.
kubectl get pod --watch -l app=nginx
```

در ترمینال دوم، همهٔ Podهای StatefulSet را حذف کنید:

```shell
kubectl delete pod -l app=nginx
```
```
pod "web-0" deleted
pod "web-1" deleted
```
خروجی فرمان `kubectl get` را در ترمینال اول بررسی کنید و صبر کنید تا همهٔ Podها به وضعیت Running و Ready برسند.

```shell
# This should already be running
kubectl get pod --watch -l app=nginx
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     0/1       ContainerCreating   0          0s
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          2s
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         34s
```

بررسی کنید که وب‌سرورها همچنان نام میزبان خود را ارائه می‌کنند:

```
for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```
```
web-0
web-1
```

با اینکه `web-0` و `web-1` دوباره زمان‌بندی شده‌اند، همچنان نام میزبان خود را ارائه می‌کنند؛ زیرا PersistentVolumeهای مرتبط با PersistentVolumeClaimهای آن‌ها دوباره به `volumeMounts` آن‌ها سوار می‌شوند. فارغ از اینکه `web-0` و `web-1` روی کدام نود زمان‌بندی شوند، PersistentVolumeهای آن‌ها به نقاط اتصال مناسب سوار خواهند شد.

## مقیاس‌دهی یک StatefulSet

مقیاس‌دهی یک StatefulSet به افزایش یا کاهش تعداد رپلیکاها (مقیاس‌دهی افقی) گفته می‌شود.
این کار با به‌روزرسانی فیلد `replicas` انجام می‌شود. برای مقیاس‌دهی یک StatefulSet می‌توانید از
[`kubectl scale`](/docs/reference/generated/kubectl/kubectl-commands/#scale) یا
[`kubectl patch`](/docs/reference/generated/kubectl/kubectl-commands/#patch) استفاده کنید.

### افزایش مقیاس

افزایش مقیاس به معنای افزودن رپلیکاهای بیشتر است.
به شرط آنکه برنامهٔ شما بتواند کار را میان اعضای StatefulSet توزیع کند، مجموعهٔ جدید و بزرگ‌تر Podها می‌تواند بخش بیشتری از آن کار را انجام دهد.

در یک پنجرهٔ ترمینال، Podهای StatefulSet را پایش کنید:

```shell
# If you already have a watch running, you can continue using that.
# Otherwise, start one.
# End this watch when there are 5 healthy Pods for the StatefulSet
kubectl get pods --watch -l app=nginx
```

در پنجرهٔ ترمینال دیگری، با استفاده از `kubectl scale` تعداد رپلیکاها را به ۵ برسانید:

```shell
kubectl scale sts web --replicas=5
```
```
statefulset.apps/web scaled
```

خروجی فرمان `kubectl get` را در ترمینال اول بررسی کنید و صبر کنید تا سه Pod افزوده‌شده به وضعیت Running و Ready برسند.

```shell
# This should already be running
kubectl get pod --watch -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          2h
web-1     1/1       Running   0          2h
NAME      READY     STATUS    RESTARTS   AGE
web-2     0/1       Pending   0          0s
web-2     0/1       Pending   0         0s
web-2     0/1       ContainerCreating   0         0s
web-2     1/1       Running   0         19s
web-3     0/1       Pending   0         0s
web-3     0/1       Pending   0         0s
web-3     0/1       ContainerCreating   0         0s
web-3     1/1       Running   0         18s
web-4     0/1       Pending   0         0s
web-4     0/1       Pending   0         0s
web-4     0/1       ContainerCreating   0         0s
web-4     1/1       Running   0         19s
```

کنترل‌کنندهٔ StatefulSet تعداد رپلیکاها را تغییر داد. همانند [ایجاد StatefulSet](#ordered-pod-creation)، کنترل‌کنندهٔ StatefulSet هر Pod را به‌صورت پی‌درپی و بر اساس شاخص ترتیبی آن ایجاد کرد و پیش از راه‌اندازی هر Pod، منتظر ماند تا Pod پیشین در وضعیت Running و Ready قرار گیرد.

### کاهش مقیاس

کاهش مقیاس به معنای کم کردن تعداد رپلیکاهاست. برای مثال، ممکن است به این دلیل این کار را انجام دهید که سطح ترافیک یک سرویس کاهش یافته است و در مقیاس فعلی، منابعی بیکار مانده‌اند.

در یک ترمینال، Podهای StatefulSet را پایش کنید:

```shell
# End this watch when there are only 3 Pods for the StatefulSet
kubectl get pod --watch -l app=nginx
```

در ترمینال دیگری، با استفاده از `kubectl patch` مقیاس StatefulSet را دوباره به سه رپلیکا کاهش دهید:

```shell
kubectl patch sts web -p '{"spec":{"replicas":3}}'
```
```
statefulset.apps/web patched
```

صبر کنید تا `web-4` و `web-3` به وضعیت Terminating بروند.

```shell
# This should already be running
kubectl get pods --watch -l app=nginx
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     1/1       Running             0          3h
web-1     1/1       Running             0          3h
web-2     1/1       Running             0          55s
web-3     1/1       Running             0          36s
web-4     0/1       ContainerCreating   0          18s
NAME      READY     STATUS    RESTARTS   AGE
web-4     1/1       Running   0          19s
web-4     1/1       Terminating   0         24s
web-4     1/1       Terminating   0         24s
web-3     1/1       Terminating   0         42s
web-3     1/1       Terminating   0         42s
```

### خاتمهٔ ترتیبی Podها

control plane هر بار یک Pod را، به ترتیب معکوس شاخص ترتیبی آن، حذف کرد و پیش از حذف Pod بعدی منتظر ماند تا هر Pod به‌طور کامل خاموش شود.

PersistentVolumeClaimهای StatefulSet را دریافت کنید:

```shell
kubectl get pvc -l app=nginx
```
```
NAME        STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
www-web-0   Bound     pvc-15c268c7-b507-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-1   Bound     pvc-15c79307-b507-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-2   Bound     pvc-e1125b27-b508-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-3   Bound     pvc-e1176df6-b508-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-4   Bound     pvc-e11bb5f8-b508-11e6-932f-42010a800002   1Gi        RWO           13h

```

هنوز پنج PersistentVolumeClaim و پنج PersistentVolume وجود دارد.
هنگام بررسی [ذخیره‌سازی پایدار](#writing-to-stable-storage) یک Pod دیدید که با حذف Podهای یک StatefulSet، PersistentVolumeهای سوارشده به آن Podها حذف نمی‌شوند. این موضوع زمانی که حذف Pod در اثر کاهش مقیاس StatefulSet رخ می‌دهد نیز صادق است.

## به‌روزرسانی StatefulSetها

کنترل‌کنندهٔ StatefulSet از به‌روزرسانی‌های خودکار پشتیبانی می‌کند. راهبرد مورد استفاده با فیلد `spec.updateStrategy` در آبجکت API مربوط به StatefulSet تعیین می‌شود. با این قابلیت می‌توانید ایمیج‌های کانتینر، درخواست‌ها و/یا محدودیت‌های منابع، برچسب‌ها و حاشیه‌نویسی‌های (annotation) Podهای یک StatefulSet را ارتقا دهید.

دو راهبرد به‌روزرسانی معتبر وجود دارد: `RollingUpdate` (پیش‌فرض) و `OnDelete`.

### RollingUpdate {#rolling-update}

راهبرد به‌روزرسانی `RollingUpdate` همهٔ Podهای یک StatefulSet را به ترتیب معکوس شمارهٔ ترتیبی‌شان به‌روزرسانی می‌کند و در این کار تضمین‌های StatefulSet را رعایت می‌کند.

برای StatefulSetی که از راهبرد `RollingUpdate` استفاده می‌کند، می‌توانید با تعیین `.spec.updateStrategy.rollingUpdate.partition` به‌روزرسانی‌ها را به _بخش‌ها_ (partitions) تقسیم کنید. این کار را در ادامهٔ همین آموزش تمرین خواهید کرد.

ابتدا یک به‌روزرسانی غلتان (rolling update) ساده را امتحان کنید.

در یک پنجرهٔ ترمینال، StatefulSet به نام `web` را patch کنید تا ایمیج کانتینر دوباره تغییر کند:

```shell
kubectl patch statefulset web --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"registry.k8s.io/nginx-slim:0.24"}]'
```
```
statefulset.apps/web patched
```

در ترمینالی دیگر، Podهای این StatefulSet را زیر نظر بگیرید:

```shell
# End this watch when the rollout is complete
#
# If you're not sure, leave it running one more minute
kubectl get pod -l app=nginx --watch
```
خروجی مشابه زیر است:
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          7m
web-1     1/1       Running   0          7m
web-2     1/1       Running   0          8m
web-2     1/1       Terminating   0         8m
web-2     1/1       Terminating   0         8m
web-2     0/1       Terminating   0         8m
web-2     0/1       Terminating   0         8m
web-2     0/1       Terminating   0         8m
web-2     0/1       Terminating   0         8m
web-2     0/1       Pending   0         0s
web-2     0/1       Pending   0         0s
web-2     0/1       ContainerCreating   0         0s
web-2     1/1       Running   0         19s
web-1     1/1       Terminating   0         8m
web-1     0/1       Terminating   0         8m
web-1     0/1       Terminating   0         8m
web-1     0/1       Terminating   0         8m
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         6s
web-0     1/1       Terminating   0         7m
web-0     1/1       Terminating   0         7m
web-0     0/1       Terminating   0         7m
web-0     0/1       Terminating   0         7m
web-0     0/1       Terminating   0         7m
web-0     0/1       Terminating   0         7m
web-0     0/1       Pending   0         0s
web-0     0/1       Pending   0         0s
web-0     0/1       ContainerCreating   0         0s
web-0     1/1       Running   0         10s
```

Podهای این StatefulSet به ترتیب معکوس شمارهٔ ترتیبی به‌روزرسانی می‌شوند. کنترل‌کنندهٔ StatefulSet هر Pod را خاتمه می‌دهد و پیش از به‌روزرسانی Pod بعدی صبر می‌کند تا آن Pod به وضعیت Running و Ready برسد. توجه کنید که کنترل‌کنندهٔ StatefulSet تا زمانی که Pod قبلی در ترتیب به وضعیت Running و Ready نرسد، به‌روزرسانی Pod بعدی را آغاز نمی‌کند؛ با این حال، هر Podی را که در حین به‌روزرسانی با شکست مواجه شود، به نسخهٔ فعلی همان Pod بازمی‌گرداند.

Podهایی که به‌روزرسانی را دریافت کرده‌اند به نسخهٔ به‌روزشده بازگردانده می‌شوند و Podهایی که هنوز به‌روزرسانی را دریافت نکرده‌اند به نسخهٔ قبلی بازمی‌گردند. به این ترتیب، کنترل‌کننده می‌کوشد در صورت بروز خرابی‌های گاه‌به‌گاه نیز برنامه را سالم و به‌روزرسانی را سازگار نگه دارد.

برای مشاهدهٔ ایمیج‌های کانتینر، Podها را دریافت کنید:

```shell
for p in 0 1 2; do kubectl get pod "web-$p" --template '{{range $i, $c := .spec.containers}}{{$c.image}}{{end}}'; echo; done
```
```
registry.k8s.io/nginx-slim:0.24
registry.k8s.io/nginx-slim:0.24
registry.k8s.io/nginx-slim:0.24

```

اکنون همهٔ Podهای این StatefulSet ایمیج کانتینر قبلی را اجرا می‌کنند.

{{< alert color="info" title="Note" >}}
برای مشاهدهٔ وضعیت به‌روزرسانی غلتان یک StatefulSet می‌توانید از دستور `kubectl rollout status sts/<name>` نیز استفاده کنید.
{{< /alert >}}

#### آماده‌سازی یک به‌روزرسانی

برای StatefulSetی که از راهبرد `RollingUpdate` استفاده می‌کند، می‌توانید با تعیین `.spec.updateStrategy.rollingUpdate.partition` به‌روزرسانی‌ها را به _بخش‌ها_ تقسیم کنید.

برای آشنایی بیشتر، می‌توانید بخش [به‌روزرسانی‌های غلتان بخش‌بندی‌شده](/docs/concepts/workloads/controllers/statefulset/#partitions) را در صفحهٔ مفاهیم StatefulSet بخوانید.

با استفاده از فیلد `partition` در `.spec.updateStrategy.rollingUpdate` می‌توانید به‌روزرسانی یک StatefulSet را از پیش آماده کنید. در این به‌روزرسانی، Podهای موجود در StatefulSet را بدون تغییر نگه می‌دارید و در همین حال الگوی Pod (pod template) آن StatefulSet را تغییر می‌دهید. سپس شما، یا در محیطی خارج از آموزش، یک سازوکار خودکارسازی خارجی، می‌توانید آن به‌روزرسانیِ آماده‌شده را راه‌اندازی کنید.

ابتدا StatefulSet به نام `web` را patch کنید تا یک partition به فیلد `updateStrategy` اضافه شود:

```shell
# The value of "partition" determines which ordinals a change applies to
# Make sure to use a number bigger than the last ordinal for the
# StatefulSet
kubectl patch statefulset web -p '{"spec":{"updateStrategy":{"type":"RollingUpdate","rollingUpdate":{"partition":3}}}}'
```
```
statefulset.apps/web patched
```

برای تغییر ایمیج کانتینری که این StatefulSet استفاده می‌کند، آن را دوباره patch کنید:

```shell
kubectl patch statefulset web --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/image", "value":"registry.k8s.io/nginx-slim:0.21"}]'
```
```
statefulset.apps/web patched
```

یکی از Podهای این StatefulSet را حذف کنید:

```shell
kubectl delete pod web-2
```
```
pod "web-2" deleted
```

صبر کنید تا Pod جایگزینِ `web-2` به وضعیت Running و Ready برسد:

```shell
# End the watch when you see that web-2 is healthy
kubectl get pod -l app=nginx --watch
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     1/1       Running             0          4m
web-1     1/1       Running             0          4m
web-2     0/1       ContainerCreating   0          11s
web-2     1/1       Running   0         18s
```

ایمیج کانتینر این Pod را دریافت کنید:

```shell
kubectl get pod web-2 --template '{{range $i, $c := .spec.containers}}{{$c.image}}{{end}}'
```
```
registry.k8s.io/nginx-slim:0.24
```

دقت کنید که با وجود اینکه راهبرد به‌روزرسانی `RollingUpdate` است، StatefulSet این Pod را با ایمیج کانتینر اصلی بازگردانده است. علت این است که شمارهٔ ترتیبی این Pod از مقدار `partition` تعیین‌شده در `updateStrategy` کمتر است.

#### انتشار قناری

اکنون می‌خواهید یک [انتشار قناری](https://glossary.cncf.io/canary-deployment/) (canary rollout) از آن تغییر آماده‌شده را امتحان کنید.

برای انتشار قناری (به‌منظور آزمودن الگوی تغییریافته)، کافی است مقدار `partition` را که [در بالا](#staging-an-update) تعیین کردید کاهش دهید.

برای کاهش partition، این StatefulSet را patch کنید:

```shell
# The value of "partition" should match the highest existing ordinal for
# the StatefulSet
kubectl patch statefulset web -p '{"spec":{"updateStrategy":{"type":"RollingUpdate","rollingUpdate":{"partition":2}}}}'
```
```
statefulset.apps/web patched
```

اکنون control plane جایگزینی `web-2` را آغاز می‌کند؛ این کار با یک **حذف** ملایم (graceful) و سپس ایجاد یک Pod جدید پس از کامل شدن حذف انجام می‌شود. صبر کنید تا Pod جدید `web-2` به وضعیت Running و Ready برسد.

```shell
# This should already be running
kubectl get pod -l app=nginx --watch
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     1/1       Running             0          4m
web-1     1/1       Running             0          4m
web-2     0/1       ContainerCreating   0          11s
web-2     1/1       Running   0         18s
```

کانتینر این Pod را دریافت کنید:

```shell
kubectl get pod web-2 --template '{{range $i, $c := .spec.containers}}{{$c.image}}{{end}}'
```
```
registry.k8s.io/nginx-slim:0.21

```

هنگامی که مقدار `partition` را تغییر دادید، کنترل‌کنندهٔ StatefulSet به‌طور خودکار Pod `web-2` را به‌روزرسانی کرد، زیرا شمارهٔ ترتیبی این Pod بزرگ‌تر یا مساوی `partition` بود.

Pod `web-1` را حذف کنید:

```shell
kubectl delete pod web-1
```
```
pod "web-1" deleted
```

صبر کنید تا Pod `web-1` به وضعیت Running و Ready برسد.

```shell
# This should already be running
kubectl get pod -l app=nginx --watch
```
خروجی مشابه زیر است:
```
NAME      READY     STATUS        RESTARTS   AGE
web-0     1/1       Running       0          6m
web-1     0/1       Terminating   0          6m
web-2     1/1       Running       0          2m
web-1     0/1       Terminating   0         6m
web-1     0/1       Terminating   0         6m
web-1     0/1       Terminating   0         6m
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         18s
```

ایمیج کانتینر Pod `web-1` را دریافت کنید:

```shell
kubectl get pod web-1 --template '{{range $i, $c := .spec.containers}}{{$c.image}}{{end}}'
```
```
registry.k8s.io/nginx-slim:0.24
```

Pod `web-1` به پیکربندی اصلی خود بازگردانده شد، زیرا شمارهٔ ترتیبی آن از partition کمتر بود. وقتی partition تعیین شده باشد، با به‌روزرسانی `.spec.template` در StatefulSet، همهٔ Podهایی که شمارهٔ ترتیبی‌شان بزرگ‌تر یا مساوی partition است به‌روزرسانی می‌شوند. اگر Podی با شمارهٔ ترتیبی کمتر از partition حذف شود یا به هر شکل دیگری خاتمه یابد، به پیکربندی اصلی خود بازگردانده می‌شود.

#### انتشارهای مرحله‌ای

با استفاده از به‌روزرسانی غلتان بخش‌بندی‌شده می‌توانید یک انتشار مرحله‌ای (مثلاً انتشار خطی، هندسی یا نمایی) را به روشی مشابه انتشار [قناری](#rolling-out-a-canary) انجام دهید. برای انجام انتشار مرحله‌ای، مقدار `partition` را برابر شمارهٔ ترتیبی‌ای قرار دهید که می‌خواهید کنترل‌کننده به‌روزرسانی را در آن متوقف کند.

مقدار partition در حال حاضر `2` است. آن را به `0` تغییر دهید:

```shell
kubectl patch statefulset web -p '{"spec":{"updateStrategy":{"type":"RollingUpdate","rollingUpdate":{"partition":0}}}}'
```
```
statefulset.apps/web patched
```

صبر کنید تا همهٔ Podهای این StatefulSet به وضعیت Running و Ready برسند.

```shell
# This should already be running
kubectl get pod -l app=nginx --watch
```
خروجی مشابه زیر است:
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     1/1       Running             0          3m
web-1     0/1       ContainerCreating   0          11s
web-2     1/1       Running             0          2m
web-1     1/1       Running   0         18s
web-0     1/1       Terminating   0         3m
web-0     1/1       Terminating   0         3m
web-0     0/1       Terminating   0         3m
web-0     0/1       Terminating   0         3m
web-0     0/1       Terminating   0         3m
web-0     0/1       Terminating   0         3m
web-0     0/1       Pending   0         0s
web-0     0/1       Pending   0         0s
web-0     0/1       ContainerCreating   0         0s
web-0     1/1       Running   0         3s
```

جزئیات ایمیج کانتینر Podهای این StatefulSet را دریافت کنید:

```shell
for p in 0 1 2; do kubectl get pod "web-$p" --template '{{range $i, $c := .spec.containers}}{{$c.image}}{{end}}'; echo; done
```
```
registry.k8s.io/nginx-slim:0.21
registry.k8s.io/nginx-slim:0.21
registry.k8s.io/nginx-slim:0.21
```

با تغییر مقدار `partition` به `0`، به StatefulSet اجازه دادید فرایند به‌روزرسانی را ادامه دهد.

### OnDelete {#on-delete}

برای انتخاب این راهبرد به‌روزرسانی در یک StatefulSet، مقدار `.spec.updateStrategy.type` را `OnDelete` قرار دهید.

StatefulSet به نام `web` را patch کنید تا از راهبرد به‌روزرسانی `OnDelete` استفاده کند:

```shell
kubectl patch statefulset web -p '{"spec":{"updateStrategy":{"type":"OnDelete", "rollingUpdate": null}}}'
```
```
statefulset.apps/web patched
```

با انتخاب این راهبرد به‌روزرسانی، کنترل‌کنندهٔ StatefulSet پس از تغییر فیلد `.spec.template` در StatefulSet، Podها را به‌طور خودکار به‌روزرسانی نمی‌کند. در این حالت باید انتشار را خودتان مدیریت کنید؛ یا به‌صورت دستی یا با یک سازوکار خودکارسازی جداگانه.

## حذف StatefulSetها

یک StatefulSet از هر دو نوع حذف _غیرآبشاری_ (non-cascading) و _آبشاری_ (cascading) پشتیبانی می‌کند. در **حذف** غیرآبشاری، با حذف StatefulSet، Podهای آن حذف نمی‌شوند. در **حذف** آبشاری، هم StatefulSet و هم Podهای آن حذف می‌شوند.

برای آشنایی کلی با حذف آبشاری، صفحهٔ [استفاده از حذف آبشاری در یک کلاستر](/docs/tasks/administer-cluster/use-cascading-deletion/) را بخوانید.

### حذف غیرآبشاری

در یک پنجرهٔ ترمینال، Podهای این StatefulSet را زیر نظر بگیرید.

```
# End this watch when there are no Pods for the StatefulSet
kubectl get pods --watch -l app=nginx
```

برای حذف StatefulSet از دستور [`kubectl delete`](/docs/reference/generated/kubectl/kubectl-commands/#delete) استفاده کنید. حتماً پارامتر `--cascade=orphan` را به دستور بدهید. این پارامتر به کوبرنتیز می‌گوید که فقط StatefulSet را حذف کند و هیچ‌یک از Podهای آن را حذف **نکند**.

```shell
kubectl delete statefulset web --cascade=orphan
```
```
statefulset.apps "web" deleted
```

برای بررسی وضعیت Podها، آن‌ها را دریافت کنید:

```shell
kubectl get pods -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          6m
web-1     1/1       Running   0          7m
web-2     1/1       Running   0          5m
```

با اینکه `web` حذف شده است، همهٔ Podها همچنان در وضعیت Running و Ready هستند. اکنون `web-0` را حذف کنید:

```shell
kubectl delete pod web-0
```
```
pod "web-0" deleted
```

Podهای این StatefulSet را دریافت کنید:

```shell
kubectl get pods -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-1     1/1       Running   0          10m
web-2     1/1       Running   0          7m
```

از آنجا که StatefulSet به نام `web` حذف شده است، `web-0` دوباره راه‌اندازی نشده است.

در یک ترمینال، Podهای این StatefulSet را زیر نظر بگیرید.

```shell
# Leave this watch running until the next time you start a watch
kubectl get pods --watch -l app=nginx
```

در ترمینال دوم، StatefulSet را دوباره ایجاد کنید. توجه کنید که اگر Service به نام `nginx` را حذف نکرده باشید (که نباید حذف کرده باشید)، خطایی خواهید دید که نشان می‌دهد این Service از قبل وجود دارد.

```shell
kubectl apply -f https://k8s.io/examples/application/web/web.yaml
```
```
statefulset.apps/web created
service/nginx unchanged
```

این خطا را نادیده بگیرید. این خطا فقط نشان می‌دهد که تلاشی برای ایجاد Service بدون سرآیند (headless) به نام _nginx_ انجام شده، در حالی که این Service از قبل وجود داشته است.

خروجی دستور `kubectl get` را که در ترمینال اول در حال اجراست بررسی کنید.

```shell
# This should already be running
kubectl get pods --watch -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-1     1/1       Running   0          16m
web-2     1/1       Running   0          2m
NAME      READY     STATUS    RESTARTS   AGE
web-0     0/1       Pending   0          0s
web-0     0/1       Pending   0         0s
web-0     0/1       ContainerCreating   0         0s
web-0     1/1       Running   0         18s
web-2     1/1       Terminating   0         3m
web-2     0/1       Terminating   0         3m
web-2     0/1       Terminating   0         3m
web-2     0/1       Terminating   0         3m
```

هنگامی که StatefulSet به نام `web` دوباره ایجاد شد، ابتدا `web-0` را دوباره راه‌اندازی کرد. از آنجا که `web-1` از قبل در وضعیت Running و Ready بود، پس از رسیدن `web-0` به وضعیت Running و Ready، StatefulSet این Pod را به سرپرستی گرفت. چون StatefulSet را با `replicas` برابر 2 دوباره ایجاد کرده بودید، پس از ایجاد دوبارهٔ `web-0` و مشخص شدن اینکه `web-1` از قبل در وضعیت Running و Ready است، `web-2` خاتمه یافت.

اکنون دوباره محتوای فایل `index.html` را که وب‌سرورهای Podها ارائه می‌کنند بررسی کنید:

```shell
for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```

```
web-0
web-1
```

با اینکه هم StatefulSet و هم Pod `web-0` را حذف کردید، این Pod همچنان نام میزبانی را ارائه می‌کند که در ابتدا در فایل `index.html` آن نوشته شده بود. علت این است که StatefulSet هرگز PersistentVolumeهای مرتبط با یک Pod را حذف نمی‌کند. وقتی StatefulSet را دوباره ایجاد کردید و `web-0` دوباره راه‌اندازی شد، PersistentVolume اصلی آن دوباره متصل (mount) شد.

### حذف آبشاری

در یک پنجرهٔ ترمینال، Podهای این StatefulSet را زیر نظر بگیرید.

```shell
# Leave this running until the next page section
kubectl get pods --watch -l app=nginx
```

در ترمینالی دیگر، StatefulSet را دوباره حذف کنید. این بار پارامتر `--cascade=orphan` را حذف کنید.

```shell
kubectl delete statefulset web
```

```
statefulset.apps "web" deleted
```

خروجی دستور `kubectl get` را که در ترمینال اول در حال اجراست بررسی کنید و صبر کنید تا همهٔ Podها به وضعیت Terminating بروند.

```shell
# This should already be running
kubectl get pods --watch -l app=nginx
```

```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          11m
web-1     1/1       Running   0          27m
NAME      READY     STATUS        RESTARTS   AGE
web-0     1/1       Terminating   0          12m
web-1     1/1       Terminating   0         29m
web-0     0/1       Terminating   0         12m
web-0     0/1       Terminating   0         12m
web-0     0/1       Terminating   0         12m
web-1     0/1       Terminating   0         29m
web-1     0/1       Terminating   0         29m
web-1     0/1       Terminating   0         29m

```

همان‌طور که در بخش [کاهش مقیاس](#scaling-down) دیدید، Podها یکی‌یکی و به ترتیب معکوس شاخص‌های ترتیبی‌شان خاتمه می‌یابند. کنترل‌کنندهٔ StatefulSet پیش از خاتمه دادن به هر Pod صبر می‌کند تا Pod بعدی در ترتیب به‌طور کامل خاتمه یابد.

{{< alert color="info" title="Note" >}}
اگرچه حذف آبشاری یک StatefulSet را همراه با Podهای آن حذف می‌کند، این حذف آبشاری Service بدون سرآیندِ مرتبط با StatefulSet را حذف **نمی‌کند**. باید Service به نام `nginx` را به‌صورت دستی حذف کنید.
{{< /alert >}}

```shell
kubectl delete service nginx
```

```
service "nginx" deleted
```

StatefulSet و Service بدون سرآیند را یک بار دیگر ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/web/web.yaml
```

```
service/nginx created
statefulset.apps/web created
```

وقتی همهٔ Podهای این StatefulSet به وضعیت Running و Ready رسیدند، محتوای فایل‌های `index.html` آن‌ها را دریافت کنید:

```shell
for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```

```
web-0
web-1
```

با اینکه StatefulSet و همهٔ Podهای آن را به‌طور کامل حذف کردید، Podها همراه با PersistentVolumeهای متصل‌شده‌شان دوباره ایجاد می‌شوند و `web-0` و `web-1` همچنان نام میزبان خود را ارائه می‌کنند.

در پایان، Service به نام `nginx` را حذف کنید...

```shell
kubectl delete service nginx
```

```
service "nginx" deleted
```

...و سپس StatefulSet به نام `web` را:

```shell
kubectl delete statefulset web
```

```
statefulset "web" deleted
```

## سیاست مدیریت Pod

برای برخی سامانه‌های توزیع‌شده، تضمین‌های ترتیبی StatefulSet غیرضروری یا نامطلوب هستند. این سامانه‌ها فقط به یکتایی و هویت نیاز دارند.

برای پرهیز از این ترتیب سخت‌گیرانه، می‌توانید یک [سیاست مدیریت Pod](/docs/concepts/workloads/controllers/statefulset/#pod-management-policies) تعیین کنید؛ یا `OrderedReady` (پیش‌فرض) یا `Parallel`.

### مدیریت Pod با OrderedReady

مدیریت Pod با `OrderedReady` حالت پیش‌فرض StatefulSetهاست. این سیاست به کنترل‌کنندهٔ StatefulSet می‌گوید که تضمین‌های ترتیبیِ نشان‌داده‌شده در بالا را رعایت کند.

زمانی از این سیاست استفاده کنید که برنامهٔ شما نیاز دارد یا انتظار دارد تغییرات، مانند انتشار نسخهٔ جدیدی از برنامه، دقیقاً به ترتیب شمارهٔ ترتیبی (شمارهٔ Pod) که StatefulSet فراهم می‌کند انجام شوند. به بیان دیگر، اگر Podهای `app-0`، `app-1` و `app-2` را داشته باشید، کوبرنتیز ابتدا `app-0` را به‌روزرسانی و بررسی می‌کند. پس از موفقیت بررسی‌ها، کوبرنتیز `app-1` و در پایان `app-2` را به‌روزرسانی می‌کند.

اگر دو Pod دیگر اضافه کنید، کوبرنتیز ابتدا `app-3` را راه‌اندازی می‌کند و پیش از استقرار `app-4` صبر می‌کند تا `app-3` سالم شود.

از آنجا که این تنظیم پیش‌فرض است، پیش‌تر استفاده از آن را تمرین کرده‌اید.

### مدیریت موازی Podها

گزینهٔ دیگر، یعنی مدیریت Pod به‌صورت `Parallel`، به کنترل‌کنندهٔ StatefulSet اعلام می‌کند که همهٔ Podها را به‌طور موازی راه‌اندازی یا خاتمه دهد. در این حالت، کنترل‌کننده پیش از راه‌اندازی یا خاتمهٔ یک Pod دیگر منتظر نمی‌ماند تا Podها به وضعیت `Running` و `Ready` برسند یا کاملاً خاتمه یابند.

گزینهٔ مدیریت Pod به‌صورت `Parallel` فقط بر رفتار عملیات مقیاس‌دهی اثر می‌گذارد و بر به‌روزرسانی‌ها اثری ندارد. کوبرنتیز همچنان تغییرات را به‌ترتیب اعمال می‌کند. برنامهٔ این آموزش بسیار ساده است: یک وب‌سرور که نام میزبان (hostname) خود را به شما اعلام می‌کند. از آنجا که این برنامه یک StatefulSet است، نام میزبان هر Pod متفاوت و قابل پیش‌بینی است.

{{% code_sample file="application/web/web-parallel.yaml" %}}

این مانیفست با مانیفستی که پیش‌تر دانلود کردید یکسان است، با این تفاوت که مقدار `.spec.podManagementPolicy` در StatefulSet با نام `web` روی `Parallel` تنظیم شده است.

در یک ترمینال، Podهای StatefulSet را زیر نظر بگیرید.

```shell
# Leave this watch running until the end of the section
kubectl get pod -l app=nginx --watch
```

در ترمینالی دیگر، StatefulSet را برای مدیریت Pod به‌صورت `Parallel` دوباره پیکربندی کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/web/web-parallel.yaml
```
```
service/nginx updated
statefulset.apps/web updated
```

ترمینالی را که فرمان watch در آن در حال اجراست باز نگه دارید. در یک پنجرهٔ ترمینال دیگر، StatefulSet را مقیاس‌دهی کنید:

```shell
kubectl scale statefulset/web --replicas=5
```
```
statefulset.apps/web scaled
```

خروجی ترمینالی را که فرمان `kubectl get` در آن در حال اجراست بررسی کنید. این خروجی ممکن است چیزی شبیه به این باشد:

```
web-3     0/1       Pending   0         0s
web-3     0/1       Pending   0         0s
web-3     0/1       Pending   0         7s
web-3     0/1       ContainerCreating   0         7s
web-2     0/1       Pending   0         0s
web-4     0/1       Pending   0         0s
web-2     1/1       Running   0         8s
web-4     0/1       ContainerCreating   0         4s
web-3     1/1       Running   0         26s
web-4     1/1       Running   0         2s
```


این StatefulSet سه Pod جدید راه‌اندازی کرد و پیش از راه‌اندازی Podهای دوم و سوم منتظر نماند تا Pod اول به وضعیت Running و Ready برسد.

این رویکرد زمانی سودمند است که بار کاری شما بخشی دارای حالت (stateful) داشته باشد یا Podها باید بتوانند یکدیگر را با نام‌گذاری قابل پیش‌بینی شناسایی کنند، به‌ویژه اگر گاهی لازم باشد ظرفیت بسیار بیشتری را به‌سرعت فراهم کنید. اگر این سرویس وب سادهٔ آموزشی ناگهان ۱٬۰۰۰٬۰۰۰ درخواست اضافه در دقیقه دریافت کند، می‌خواهید Podهای بیشتری اجرا کنید، اما نمی‌خواهید برای راه‌اندازی تک‌تک Podهای جدید منتظر بمانید. راه‌اندازی موازی Podهای اضافی، فاصلهٔ زمانی میان درخواست ظرفیت اضافه و آماده‌شدن آن برای استفاده را کوتاه می‌کند.

## {{% heading "cleanup" %}}

اکنون باید دو ترمینال باز داشته باشید تا فرمان‌های `kubectl` را برای پاک‌سازی در آن‌ها اجرا کنید.

```shell
kubectl delete sts web
# sts is an abbreviation for statefulset
```

می‌توانید با فرمان `kubectl get` حذف‌شدن این Podها را زیر نظر بگیرید.
```shell
# end the watch when you've seen what you need to
kubectl get pod -l app=nginx --watch
```
```
web-3     1/1       Terminating   0         9m
web-2     1/1       Terminating   0         9m
web-3     1/1       Terminating   0         9m
web-2     1/1       Terminating   0         9m
web-1     1/1       Terminating   0         44m
web-0     1/1       Terminating   0         44m
web-0     0/1       Terminating   0         44m
web-3     0/1       Terminating   0         9m
web-2     0/1       Terminating   0         9m
web-1     0/1       Terminating   0         44m
web-0     0/1       Terminating   0         44m
web-2     0/1       Terminating   0         9m
web-2     0/1       Terminating   0         9m
web-2     0/1       Terminating   0         9m
web-1     0/1       Terminating   0         44m
web-1     0/1       Terminating   0         44m
web-1     0/1       Terminating   0         44m
web-0     0/1       Terminating   0         44m
web-0     0/1       Terminating   0         44m
web-0     0/1       Terminating   0         44m
web-3     0/1       Terminating   0         9m
web-3     0/1       Terminating   0         9m
web-3     0/1       Terminating   0         9m
```

هنگام حذف، StatefulSet همهٔ Podها را هم‌زمان حذف می‌کند و پیش از حذف هر Pod منتظر نمی‌ماند تا Pod بعدی آن در ترتیب شماره‌ها خاتمه یابد.

ترمینالی را که فرمان `kubectl get` در آن در حال اجراست ببندید و Service با نام `nginx` را حذف کنید:

```shell
kubectl delete svc nginx
```

رسانه‌های ذخیره‌سازی پایدار مربوط به PersistentVolumeهای استفاده‌شده در این آموزش را حذف کنید.

```shell
kubectl get pvc
```
```
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
www-web-0   Bound    pvc-2bf00408-d366-4a12-bad0-1869c65d0bee   1Gi        RWO            standard       25m
www-web-1   Bound    pvc-ba3bfe9c-413e-4b95-a2c0-3ea8a54dbab4   1Gi        RWO            standard       24m
www-web-2   Bound    pvc-cba6cfa6-3a47-486b-a138-db5930207eaf   1Gi        RWO            standard       15m
www-web-3   Bound    pvc-0c04d7f0-787a-4977-8da3-d9d3a6d8d752   1Gi        RWO            standard       15m
www-web-4   Bound    pvc-b2c73489-e70b-4a4e-9ec1-9eab439aa43e   1Gi        RWO            standard       14m
```

```shell
kubectl get pv
```
```
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS   REASON   AGE
pvc-0c04d7f0-787a-4977-8da3-d9d3a6d8d752   1Gi        RWO            Delete           Bound    default/www-web-3   standard                15m
pvc-2bf00408-d366-4a12-bad0-1869c65d0bee   1Gi        RWO            Delete           Bound    default/www-web-0   standard                25m
pvc-b2c73489-e70b-4a4e-9ec1-9eab439aa43e   1Gi        RWO            Delete           Bound    default/www-web-4   standard                14m
pvc-ba3bfe9c-413e-4b95-a2c0-3ea8a54dbab4   1Gi        RWO            Delete           Bound    default/www-web-1   standard                24m
pvc-cba6cfa6-3a47-486b-a138-db5930207eaf   1Gi        RWO            Delete           Bound    default/www-web-2   standard                15m
```

```shell
kubectl delete pvc www-web-0 www-web-1 www-web-2 www-web-3 www-web-4
```

```
persistentvolumeclaim "www-web-0" deleted
persistentvolumeclaim "www-web-1" deleted
persistentvolumeclaim "www-web-2" deleted
persistentvolumeclaim "www-web-3" deleted
persistentvolumeclaim "www-web-4" deleted
```

```shell
kubectl get pvc
```

```
No resources found in default namespace.
```
{{< alert color="info" title="Note" >}}
همچنین باید رسانه‌های ذخیره‌سازی پایدار مربوط به PersistentVolumeهای استفاده‌شده در این آموزش را حذف کنید.
برای اطمینان از بازپس‌گیری کامل همهٔ فضای ذخیره‌سازی، مراحل لازم را متناسب با محیط، پیکربندی ذخیره‌سازی و روش تأمین (provisioning) خود دنبال کنید.
{{< /alert >}}
