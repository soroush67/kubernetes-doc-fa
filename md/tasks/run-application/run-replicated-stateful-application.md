---
reviewers:
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: اجرای یک برنامهٔ حالت‌مند تکثیرشده
content_type: tutorial
weight: 30
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه می‌توان یک برنامهٔ حالت‌مند (stateful) تکثیرشده را با استفاده از یک
{{< glossary_tooltip term_id="statefulset" >}} اجرا کرد.
این برنامه یک پایگاه دادهٔ MySQL تکثیرشده است. توپولوژی این مثال از یک سرور اصلی (primary)
و چند رونوشت (replica) تشکیل شده و از تکثیر ناهمگام مبتنی بر سطر (asynchronous row-based
replication) استفاده می‌کند.

{{< note >}}
**این پیکربندی برای محیط عملیاتی مناسب نیست**. تنظیمات MySQL روی مقادیر پیش‌فرض ناامن باقی مانده‌اند
تا تمرکز بر الگوهای کلی اجرای برنامه‌های حالت‌مند در کوبرنتیز حفظ شود.
{{< /note >}}

## {{% heading "prerequisites" %}}

- {{< include "task-tutorial-prereqs.md" >}}
- {{< include "default-storage-class-prereqs.md" >}}
- این آموزش فرض می‌کند که با
  [PersistentVolumeها](/docs/concepts/storage/persistent-volumes/)
  و [StatefulSetها](/docs/concepts/workloads/controllers/statefulset/)
  و همچنین با سایر مفاهیم اصلی مانند [Podها](/docs/concepts/workloads/pods/)،
  [Serviceها](/docs/concepts/services-networking/service/) و
  [ConfigMapها](/docs/tasks/configure-pod-container/configure-pod-configmap/) آشنا هستید.
- آشنایی نسبی با MySQL مفید است، اما هدف این آموزش ارائهٔ الگوهای کلی‌ای است
  که برای سیستم‌های دیگر نیز سودمند باشند.
- از فضای نام (namespace) پیش‌فرض یا فضای نام دیگری استفاده می‌کنید که هیچ آبجکت متعارضی در آن وجود ندارد.
- به یک پردازندهٔ سازگار با AMD64 نیاز دارید.

## {{% heading "objectives" %}}

- یک توپولوژی MySQL تکثیرشده را با یک StatefulSet مستقر کنید.
- ترافیک کلاینت MySQL ارسال کنید.
- مقاومت در برابر از دسترس خارج شدن را مشاهده کنید.
- مقیاس StatefulSet را افزایش و کاهش دهید.

<!-- lessoncontent -->

## استقرار MySQL

استقرار نمونهٔ MySQL از یک ConfigMap، دو Service
و یک StatefulSet تشکیل شده است.

### ایجاد یک ConfigMap {#configmap}

ConfigMap را از فایل پیکربندی YAML زیر ایجاد کنید:

{{% code_sample file="application/mysql/mysql-configmap.yaml" %}}

```shell
kubectl apply -f https://k8s.io/examples/application/mysql/mysql-configmap.yaml
```

این ConfigMap مقادیری برای بازنویسی فایل `my.cnf` فراهم می‌کند تا بتوانید پیکربندی سرور اصلی MySQL
و رونوشت‌های آن را به‌طور مستقل کنترل کنید.
در این مثال، می‌خواهید سرور اصلی بتواند لاگ‌های تکثیر را در اختیار رونوشت‌ها قرار دهد
و رونوشت‌ها هر عملیات نوشتنی را که از طریق تکثیر نرسیده است رد کنند.

خود ConfigMap ویژگی خاصی ندارد که باعث شود بخش‌های مختلف آن
روی Podهای مختلف اعمال شوند.
هر Pod هنگام راه‌اندازی، بر اساس اطلاعاتی که کنترل‌کنندهٔ StatefulSet در اختیارش می‌گذارد،
تصمیم می‌گیرد کدام بخش را بخواند.

### ایجاد Serviceها {#services}

Serviceها را از فایل پیکربندی YAML زیر ایجاد کنید:

{{% code_sample file="application/mysql/mysql-services.yaml" %}}

```shell
kubectl apply -f https://k8s.io/examples/application/mysql/mysql-services.yaml
```

Service بدون سر (headless) محلی برای رکوردهای DNS فراهم می‌کند که
{{< glossary_tooltip text="کنترل‌کننده‌های" term_id="controller" >}} StatefulSet برای هر
Pod عضو این مجموعه ایجاد می‌کنند.
از آنجا که نام این Service بدون سر `mysql` است، می‌توان از درون هر Pod دیگری در همان کلاستر
و فضای نام کوبرنتیز، با resolve کردن `<pod-name>.mysql` به Podها دسترسی داشت.

Service کلاینت با نام `mysql-read` یک Service معمولی است که cluster IP مخصوص به خود را دارد
و اتصال‌ها را بین همهٔ Podهای MySQL که وضعیت Ready گزارش می‌کنند توزیع می‌کند.
مجموعهٔ endpointهای احتمالی شامل سرور اصلی MySQL و همهٔ رونوشت‌ها است.

توجه کنید که فقط کوئری‌های خواندنی می‌توانند از Service کلاینت با توازن بار استفاده کنند.
از آنجا که تنها یک سرور اصلی MySQL وجود دارد، کلاینت‌ها برای انجام عملیات نوشتن باید مستقیماً
(از طریق رکورد DNS آن در Service بدون سر) به Pod اصلی MySQL متصل شوند.

### ایجاد StatefulSet {#statefulset}

در پایان، StatefulSet را از فایل پیکربندی YAML زیر ایجاد کنید:

{{% code_sample file="application/mysql/mysql-statefulset.yaml" %}}

```shell
kubectl apply -f https://k8s.io/examples/application/mysql/mysql-statefulset.yaml
```

با اجرای دستور زیر می‌توانید روند راه‌اندازی را دنبال کنید:

```shell
kubectl get pods -l app=mysql --watch
```

پس از مدتی، باید ببینید که هر ۳ Pod به وضعیت `Running` رسیده‌اند:

```
NAME      READY     STATUS    RESTARTS   AGE
mysql-0   2/2       Running   0          2m
mysql-1   2/2       Running   0          1m
mysql-2   2/2       Running   0          1m
```

برای لغو دنبال کردن، کلیدهای **Ctrl+C** را فشار دهید.

{{< note >}}
اگر هیچ پیشرفتی مشاهده نمی‌کنید، مطمئن شوید که یک تأمین‌کنندهٔ پویای PersistentVolume
(dynamic provisioner) فعال دارید؛ همان‌طور که در [پیش‌نیازها](#before-you-begin) ذکر شده است.
{{< /note >}}

این مانیفست از روش‌های گوناگونی برای مدیریت Podهای حالت‌مند به‌عنوان بخشی از
یک StatefulSet استفاده می‌کند. بخش بعدی برخی از این روش‌ها را برجسته می‌کند تا توضیح دهد
هنگام ایجاد Podها به‌دست StatefulSet چه اتفاقی می‌افتد.

## آشنایی با راه‌اندازی اولیهٔ Podهای حالت‌مند

کنترل‌کنندهٔ StatefulSet، Podها را یکی‌یکی و به ترتیب
اندیس ترتیبی (ordinal index) آن‌ها راه‌اندازی می‌کند.
این کنترل‌کننده پیش از راه‌اندازی هر Pod، منتظر می‌ماند تا Pod قبلی وضعیت Ready را گزارش کند.

افزون بر این، کنترل‌کننده به هر Pod نامی یکتا و پایدار به شکل
`<statefulset-name>-<ordinal-index>` اختصاص می‌دهد؛ در نتیجه Podها با نام‌های `mysql-0`،
`mysql-1` و `mysql-2` ایجاد می‌شوند.

الگوی Pod در مانیفست StatefulSet بالا از این ویژگی‌ها بهره می‌گیرد تا
راه‌اندازی تکثیر MySQL را به‌صورت منظم انجام دهد.

### تولید پیکربندی

پیش از راه‌اندازی هر یک از کانتینرهای تعریف‌شده در مشخصات Pod، ابتدا همهٔ
[کانتینرهای init](/docs/concepts/workloads/pods/init-containers/)
به ترتیب تعریف‌شده اجرا می‌شوند.

نخستین کانتینر init با نام `init-mysql`، فایل‌های پیکربندی ویژهٔ MySQL را
بر اساس اندیس ترتیبی تولید می‌کند.

این اسکریپت اندیس ترتیبی خود را از انتهای نام Pod استخراج می‌کند؛ نامی که
دستور `hostname` برمی‌گرداند.
سپس این عدد ترتیبی را (با یک جابه‌جایی عددی برای پرهیز از مقادیر رزروشده)
در فایلی به نام `server-id.cnf` در پوشهٔ `conf.d` مربوط به MySQL ذخیره می‌کند.
به این ترتیب، هویت یکتا و پایداری که StatefulSet فراهم می‌کند
به حوزهٔ شناسه‌های سرور MySQL منتقل می‌شود که به همین ویژگی‌ها نیاز دارند.

اسکریپت موجود در کانتینر `init-mysql` همچنین یکی از فایل‌های `primary.cnf` یا
`replica.cnf` را از ConfigMap، با کپی کردن محتوای آن در `conf.d`، اعمال می‌کند.
از آنجا که توپولوژی این مثال از یک سرور اصلی MySQL و تعداد دلخواهی رونوشت تشکیل شده است،
اسکریپت Pod با عدد ترتیبی `0` را سرور اصلی و بقیه را
رونوشت در نظر می‌گیرد.
این کار، همراه با
[تضمین ترتیب استقرار](/docs/concepts/workloads/controllers/statefulset/#deployment-and-scaling-guarantees)
کنترل‌کنندهٔ StatefulSet، تضمین می‌کند که سرور اصلی MySQL پیش از ایجاد رونوشت‌ها Ready باشد
تا رونوشت‌ها بتوانند تکثیر را آغاز کنند.

### کلون کردن داده‌های موجود

به‌طور کلی، وقتی یک Pod جدید به‌عنوان رونوشت به مجموعه می‌پیوندد، باید فرض کند که سرور اصلی MySQL
ممکن است از قبل داده داشته باشد. همچنین باید فرض کند که لاگ‌های تکثیر
ممکن است تا ابتدای زمان به عقب نرسند.
این فرض‌های محافظه‌کارانه کلید این هستند که یک StatefulSet در حال اجرا
بتواند در طول زمان مقیاس خود را افزایش و کاهش دهد، به جای آنکه در اندازهٔ اولیه‌اش ثابت بماند.

دومین کانتینر init با نام `clone-mysql`، نخستین باری که یک Pod رونوشت
روی یک PersistentVolume خالی راه‌اندازی می‌شود، عملیات کلون را روی آن انجام می‌دهد.
یعنی همهٔ داده‌های موجود را از یک Pod در حال اجرای دیگر کپی می‌کند
تا وضعیت محلی آن به اندازهٔ کافی سازگار باشد و بتواند تکثیر از سرور اصلی را آغاز کند.

خود MySQL سازوکاری برای این کار فراهم نمی‌کند؛ بنابراین این مثال از
ابزار متن‌باز و پرکاربردی به نام Percona XtraBackup استفاده می‌کند.
در حین کلون، ممکن است کارایی سرور MySQL مبدأ کاهش یابد.
برای به حداقل رساندن تأثیر بر سرور اصلی MySQL، اسکریپت به هر Pod دستور می‌دهد
از Podی کلون کند که اندیس ترتیبی آن یک واحد کمتر است.
این روش کار می‌کند، زیرا کنترل‌کنندهٔ StatefulSet همیشه تضمین می‌کند که Pod شمارهٔ `N`
پیش از راه‌اندازی Pod شمارهٔ `N+1` در وضعیت Ready باشد.

### آغاز تکثیر

پس از اینکه کانتینرهای init با موفقیت به پایان رسیدند، کانتینرهای عادی اجرا می‌شوند.
Podهای MySQL از یک کانتینر `mysql` که سرور اصلی `mysqld` را اجرا می‌کند،
و یک کانتینر `xtrabackup` تشکیل شده‌اند که نقش یک
[sidecar](/blog/2015/06/the-distributed-system-toolkit-patterns) را دارد.

کانتینر جانبی `xtrabackup` فایل‌های دادهٔ کلون‌شده را بررسی می‌کند و تشخیص می‌دهد
که آیا لازم است تکثیر MySQL روی رونوشت راه‌اندازی شود یا نه.
اگر لازم باشد، منتظر می‌ماند تا `mysqld` آماده شود و سپس دستورهای
`CHANGE MASTER TO` و `START SLAVE` را با پارامترهای تکثیری اجرا می‌کند
که از فایل‌های کلون XtraBackup استخراج شده‌اند.

هنگامی که یک رونوشت تکثیر را آغاز می‌کند، سرور اصلی MySQL خود را به خاطر می‌سپارد و
اگر سرور راه‌اندازی مجدد شود یا اتصال قطع شود، به‌طور خودکار دوباره متصل می‌شود.
همچنین، از آنجا که رونوشت‌ها سرور اصلی را با نام DNS پایدار آن
(`mysql-0.mysql`) جست‌وجو می‌کنند، حتی اگر سرور اصلی به دلیل زمان‌بندی مجدد
IP جدیدی برای Pod بگیرد، رونوشت‌ها به‌طور خودکار آن را پیدا می‌کنند.

در پایان، پس از آغاز تکثیر، کانتینر `xtrabackup` به اتصال‌های
Podهای دیگری گوش می‌دهد که درخواست کلون داده دارند.
این سرور برای مدت نامحدود فعال می‌ماند تا اگر مقیاس StatefulSet افزایش یافت، یا
Pod بعدی PersistentVolumeClaim خود را از دست داد و نیاز به انجام دوبارهٔ کلون داشت، پاسخ‌گو باشد.

## ارسال ترافیک کلاینت

می‌توانید با اجرای یک کانتینر موقت با ایمیج `mysql:5.7` و اجرای فایل اجرایی
کلاینت `mysql`، کوئری‌های آزمایشی را به سرور اصلی MySQL (با نام میزبان `mysql-0.mysql`) ارسال کنید.

```shell
kubectl run mysql-client --image=mysql:5.7 -i --rm --restart=Never --\
  mysql -h mysql-0.mysql <<EOF
CREATE DATABASE test;
CREATE TABLE test.messages (message VARCHAR(250));
INSERT INTO test.messages VALUES ('hello');
EOF
```

برای ارسال کوئری‌های آزمایشی به هر سروری که وضعیت Ready را گزارش می‌کند،
از نام میزبان `mysql-read` استفاده کنید:

```shell
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  mysql -h mysql-read -e "SELECT * FROM test.messages"
```

باید خروجی‌ای مانند این دریافت کنید:

```
Waiting for pod default/mysql-client to be running, status is Pending, pod ready: false
+---------+
| message |
+---------+
| hello   |
+---------+
pod "mysql-client" deleted
```

برای اینکه نشان دهید Service `mysql-read` اتصال‌ها را بین سرورها توزیع می‌کند،
می‌توانید `SELECT @@server_id` را در یک حلقه اجرا کنید:

```shell
kubectl run mysql-client-loop --image=mysql:5.7 -i -t --rm --restart=Never --\
  bash -ic "while sleep 1; do mysql -h mysql-read -e 'SELECT @@server_id,NOW()'; done"
```

باید ببینید که مقدار گزارش‌شدهٔ `@@server_id` به‌طور تصادفی تغییر می‌کند، زیرا ممکن است
در هر تلاش برای اتصال، endpoint متفاوتی انتخاب شود:

```
+-------------+---------------------+
| @@server_id | NOW()               |
+-------------+---------------------+
|         100 | 2006-01-02 15:04:05 |
+-------------+---------------------+
+-------------+---------------------+
| @@server_id | NOW()               |
+-------------+---------------------+
|         102 | 2006-01-02 15:04:06 |
+-------------+---------------------+
+-------------+---------------------+
| @@server_id | NOW()               |
+-------------+---------------------+
|         101 | 2006-01-02 15:04:07 |
+-------------+---------------------+
```

هر زمان خواستید حلقه را متوقف کنید، می‌توانید **Ctrl+C** را فشار دهید، اما بهتر است
آن را در پنجرهٔ دیگری در حال اجرا نگه دارید تا تأثیر مراحل بعدی را ببینید.

## شبیه‌سازی خرابی Pod و نود {#simulate-pod-and-node-downtime}

برای نشان دادن افزایش دسترس‌پذیری در خواندن از مجموعهٔ رونوشت‌ها
به جای یک سرور واحد، حلقهٔ `SELECT @@server_id` بالا را در حال اجرا نگه دارید
و در همین حال یک Pod را به‌اجبار از وضعیت Ready خارج کنید.

### از کار انداختن Readiness probe

[کاوشگر آمادگی (readiness probe)](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes)
کانتینر `mysql` دستور `mysql -h 127.0.0.1 -e 'SELECT 1'` را اجرا می‌کند
تا مطمئن شود سرور بالا آمده و می‌تواند کوئری‌ها را اجرا کند.

یکی از راه‌های وادار کردن این کاوشگر آمادگی به شکست، از کار انداختن همین دستور است:

```shell
kubectl exec mysql-2 -c mysql -- mv /usr/bin/mysql /usr/bin/mysql.off
```

این دستور به فایل‌سیستم کانتینر واقعی Pod `mysql-2` دسترسی پیدا می‌کند و
نام دستور `mysql` را تغییر می‌دهد تا کاوشگر آمادگی نتواند آن را پیدا کند.
پس از چند ثانیه، Pod باید یکی از کانتینرهای خود را در وضعیت غیر Ready گزارش کند؛
این موضوع را می‌توانید با اجرای دستور زیر بررسی کنید:

```shell
kubectl get pod mysql-2
```

به دنبال مقدار `1/2` در ستون `READY` بگردید:

```
NAME      READY     STATUS    RESTARTS   AGE
mysql-2   1/2       Running   0          3m
```

در این مرحله، باید ببینید که حلقهٔ `SELECT @@server_id` همچنان اجرا می‌شود،
هرچند دیگر هرگز مقدار `102` را گزارش نمی‌کند.
به یاد داشته باشید که اسکریپت `init-mysql` مقدار `server-id` را برابر با `100 + $ordinal` تعریف کرده بود؛
بنابراین شناسهٔ سرور `102` متعلق به Pod `mysql-2` است.

اکنون Pod را تعمیر کنید؛ پس از چند ثانیه باید دوباره
در خروجی حلقه ظاهر شود:

```shell
kubectl exec mysql-2 -c mysql -- mv /usr/bin/mysql.off /usr/bin/mysql
```

### حذف Podها

StatefulSet نیز، مشابه کاری که ReplicaSet برای Podهای بدون حالت انجام می‌دهد،
Podهای حذف‌شده را دوباره ایجاد می‌کند.

```shell
kubectl delete pod mysql-2
```

کنترل‌کنندهٔ StatefulSet متوجه می‌شود که دیگر Podی با نام `mysql-2` وجود ندارد
و Pod جدیدی با همان نام ایجاد می‌کند که به همان
PersistentVolumeClaim متصل است.
باید ببینید که شناسهٔ سرور `102` برای مدتی از خروجی حلقه ناپدید می‌شود
و سپس خودبه‌خود بازمی‌گردد.

### تخلیهٔ یک نود

اگر کلاستر کوبرنتیز شما چند نود دارد، می‌توانید با اجرای
[drain](/docs/reference/generated/kubectl/kubectl-commands/#drain)
از کار افتادن نود را (مانند زمانی که نودها ارتقا داده می‌شوند) شبیه‌سازی کنید.

ابتدا مشخص کنید که یکی از Podهای MySQL روی کدام نود قرار دارد:

```shell
kubectl get pod mysql-2 -o wide
```

نام نود باید در ستون آخر نمایش داده شود:

```
NAME      READY     STATUS    RESTARTS   AGE       IP            NODE
mysql-2   2/2       Running   0          15m       10.244.5.27   kubernetes-node-9l2t
```

سپس با اجرای دستور زیر نود را تخلیه کنید. این دستور ابتدا نود را cordon می‌کند تا
هیچ Pod جدیدی روی آن زمان‌بندی نشود، و سپس همهٔ Podهای موجود را بیرون می‌کند.
به جای `<node-name>` نام نودی را قرار دهید که در مرحلهٔ قبل پیدا کردید.

{{< caution >}}
تخلیهٔ یک نود ممکن است بر سایر بارهای کاری و برنامه‌هایی که
روی همان نود اجرا می‌شوند تأثیر بگذارد. مرحلهٔ زیر را فقط در یک کلاستر
آزمایشی انجام دهید.
{{< /caution >}}

```shell
# See above advice about impact on other workloads
kubectl drain <node-name> --force --delete-emptydir-data --ignore-daemonsets
```

اکنون می‌توانید زمان‌بندی مجدد Pod روی نود دیگری را دنبال کنید:

```shell
kubectl get pod mysql-2 -o wide --watch
```

خروجی باید چیزی شبیه به این باشد:

```
NAME      READY   STATUS          RESTARTS   AGE       IP            NODE
mysql-2   2/2     Terminating     0          15m       10.244.1.56   kubernetes-node-9l2t
[...]
mysql-2   0/2     Pending         0          0s        <none>        kubernetes-node-fjlm
mysql-2   0/2     Init:0/2        0          0s        <none>        kubernetes-node-fjlm
mysql-2   0/2     Init:1/2        0          20s       10.244.5.32   kubernetes-node-fjlm
mysql-2   0/2     PodInitializing 0          21s       10.244.5.32   kubernetes-node-fjlm
mysql-2   1/2     Running         0          22s       10.244.5.32   kubernetes-node-fjlm
mysql-2   2/2     Running         0          30s       10.244.5.32   kubernetes-node-fjlm
```

باز هم باید ببینید که شناسهٔ سرور `102` برای مدتی از خروجی حلقهٔ
`SELECT @@server_id` ناپدید می‌شود و سپس بازمی‌گردد.

اکنون cordon نود را بردارید تا به وضعیت عادی بازگردد:

```shell
kubectl uncordon <node-name>
```

## تغییر مقیاس تعداد رونوشت‌ها

هنگام استفاده از تکثیر MySQL، می‌توانید با افزودن رونوشت‌ها
ظرفیت پاسخ‌گویی به کوئری‌های خواندنی را افزایش دهید.
در یک StatefulSet، این کار با یک دستور ساده انجام می‌شود:

```shell
kubectl scale statefulset mysql  --replicas=5
```

با اجرای دستور زیر، بالا آمدن Podهای جدید را دنبال کنید:

```shell
kubectl get pods -l app=mysql --watch
```

پس از بالا آمدن آن‌ها، باید ببینید که شناسه‌های سرور `103` و `104` در
خروجی حلقهٔ `SELECT @@server_id` ظاهر می‌شوند.

همچنین می‌توانید بررسی کنید که این سرورهای جدید، داده‌هایی را که پیش از ایجادشان
اضافه کرده بودید در اختیار دارند:

```shell
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  mysql -h mysql-3.mysql -e "SELECT * FROM test.messages"
```

```
Waiting for pod default/mysql-client to be running, status is Pending, pod ready: false
+---------+
| message |
+---------+
| hello   |
+---------+
pod "mysql-client" deleted
```

کاهش دوبارهٔ مقیاس نیز بدون هیچ مشکلی انجام می‌شود:

```shell
kubectl scale statefulset mysql --replicas=3
```

{{< note >}}
اگرچه افزایش مقیاس به‌طور خودکار PersistentVolumeClaimهای جدیدی ایجاد می‌کند،
کاهش مقیاس این PVCها را به‌طور خودکار حذف نمی‌کند.

به این ترتیب می‌توانید انتخاب کنید که این PVCهای راه‌اندازی‌شده را نگه دارید تا
افزایش دوبارهٔ مقیاس سریع‌تر انجام شود، یا پیش از حذف آن‌ها داده‌هایشان را استخراج کنید.
{{< /note >}}

این موضوع را می‌توانید با اجرای دستور زیر ببینید:

```shell
kubectl get pvc -l app=mysql
```

خروجی نشان می‌دهد که با وجود کاهش مقیاس StatefulSet به ۳،
هر ۵ PVC همچنان وجود دارند:

```
NAME           STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
data-mysql-0   Bound     pvc-8acbf5dc-b103-11e6-93fa-42010a800002   10Gi       RWO           20m
data-mysql-1   Bound     pvc-8ad39820-b103-11e6-93fa-42010a800002   10Gi       RWO           20m
data-mysql-2   Bound     pvc-8ad69a6d-b103-11e6-93fa-42010a800002   10Gi       RWO           20m
data-mysql-3   Bound     pvc-50043c45-b1c5-11e6-93fa-42010a800002   10Gi       RWO           2m
data-mysql-4   Bound     pvc-500a9957-b1c5-11e6-93fa-42010a800002   10Gi       RWO           2m
```

اگر قصد ندارید از PVCهای اضافی دوباره استفاده کنید، می‌توانید آن‌ها را حذف کنید:

```shell
kubectl delete pvc data-mysql-3
kubectl delete pvc data-mysql-4
```

## {{% heading "cleanup" %}}

1. حلقهٔ `SELECT @@server_id` را با فشار دادن **Ctrl+C** در ترمینال مربوط به آن لغو کنید،
   یا دستور زیر را از ترمینال دیگری اجرا کنید:

   ```shell
   kubectl delete pod mysql-client-loop --now
   ```

1. StatefulSet را حذف کنید. با این کار، خاتمهٔ Podها نیز آغاز می‌شود.

   ```shell
   kubectl delete statefulset mysql
   ```

1. بررسی کنید که Podها ناپدید شوند.
   ممکن است خاتمهٔ کامل آن‌ها مدتی طول بکشد.

   ```shell
   kubectl get pods -l app=mysql
   ```

   زمانی متوجه می‌شوید Podها خاتمه یافته‌اند که دستور بالا این خروجی را برگرداند:

   ```
   No resources found.
   ```

1. ConfigMap، Serviceها و PersistentVolumeClaimها را حذف کنید.

   ```shell
   kubectl delete configmap,service,pvc -l app=mysql
   ```

1. اگر PersistentVolumeها را به‌صورت دستی تأمین کرده‌اید، باید آن‌ها را نیز به‌صورت دستی
   حذف کنید و منابع زیرساختی مربوط را آزاد کنید.
   اگر از یک تأمین‌کنندهٔ پویا استفاده کرده‌اید، این تأمین‌کننده با مشاهدهٔ حذف
   PersistentVolumeClaimها، PersistentVolumeها را به‌طور خودکار حذف می‌کند.
   برخی تأمین‌کننده‌های پویا (مانند تأمین‌کننده‌های EBS و PD) پس از حذف PersistentVolumeها،
   منابع زیرساختی را نیز آزاد می‌کنند.

## {{% heading "whatsnext" %}}

- درباره‌ی [مقیاس‌دهی یک StatefulSet](/docs/tasks/run-application/scale-stateful-set/) بیشتر بیاموزید.
- درباره‌ی [اشکال‌زدایی یک StatefulSet](/docs/tasks/debug/debug-application/debug-statefulset/) بیشتر بیاموزید.
- درباره‌ی [حذف یک StatefulSet](/docs/tasks/run-application/delete-stateful-set/) بیشتر بیاموزید.
- درباره‌ی [حذف اجباری Podهای یک StatefulSet](/docs/tasks/run-application/force-delete-stateful-set-pod/) بیشتر بیاموزید.
- برای یافتن نمونه‌های دیگری از برنامه‌های حالت‌مند (stateful)، به [مخزن Helm Charts](https://artifacthub.io/)
  مراجعه کنید.
