---
title: پردازش موازی ریزدانه با استفاده از صف کار
content_type: task
weight: 30
---

<!-- overview -->

در این مثال، یک Job کوبرنتیز اجرا می‌کنید که چندین وظیفهٔ موازی را در قالب فرایندهای کارگر (worker) اجرا می‌کند و هر کدام از این فرایندها در یک Pod جداگانه اجرا می‌شود.

در این مثال، هر Pod پس از ایجاد شدن، یک واحد کار را از صف وظایف برمی‌دارد، آن را پردازش می‌کند و این کار را تا رسیدن به انتهای صف تکرار می‌کند.

مراحل این مثال به‌طور خلاصه به شرح زیر است:

1. **یک سرویس ذخیره‌سازی برای نگهداری صف کار راه‌اندازی کنید.** در این مثال، برای ذخیرهٔ آیتم‌های کار از Redis استفاده می‌کنید. در [مثال قبلی](/docs/tasks/job/coarse-parallel-processing-work-queue) از RabbitMQ استفاده کردید. در این مثال از Redis و یک کتابخانهٔ کلاینت سفارشی برای صف کار استفاده می‌کنید، زیرا AMQP روش مناسبی در اختیار کلاینت‌ها قرار نمی‌دهد تا خالی شدن یک صف کار با طول محدود را تشخیص دهند. در عمل، یک مخزن ذخیره‌سازی مانند Redis را یک بار راه‌اندازی می‌کنید و از آن برای صف‌های کار Jobهای متعدد و کاربردهای دیگر دوباره استفاده می‌کنید.
1. **یک صف ایجاد کنید و آن را با پیام‌ها پر کنید.** هر پیام نمایانگر یک وظیفه برای انجام است. در این مثال، هر پیام یک عدد صحیح است که یک محاسبهٔ طولانی روی آن انجام می‌دهیم.
1. **یک Job راه‌اندازی کنید که وظایف موجود در صف را پردازش کند.** این Job چندین Pod را راه‌اندازی می‌کند. هر Pod یک وظیفه را از صف پیام برمی‌دارد، آن را پردازش می‌کند و این کار را تا رسیدن به انتهای صف تکرار می‌کند.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

به یک رجیستری ایمیج کانتینر نیاز دارید که بتوانید ایمیج‌ها را برای اجرا در کلاستر خود در آن بارگذاری کنید. این مثال از [Docker Hub](https://hub.docker.com/) استفاده می‌کند، اما می‌توانید آن را برای یک رجیستری ایمیج کانتینر دیگر نیز تطبیق دهید.

همچنین فرض این مثال بر آن است که Docker را به‌صورت محلی نصب کرده‌اید. از Docker برای ساخت ایمیج‌های کانتینر استفاده می‌کنید.

<!-- steps -->

با استفادهٔ پایه و غیرموازی از [Job](/docs/concepts/workloads/controllers/job/) آشنا باشید.

<!-- steps -->

## راه‌اندازی Redis

در این مثال، برای سادگی، تنها یک نمونه از Redis را راه‌اندازی می‌کنید. برای مشاهدهٔ نمونه‌ای از استقرار Redis به‌صورت مقیاس‌پذیر و با افزونگی، به [مثال Redis](https://github.com/kubernetes/examples/tree/master/web/guestbook/) مراجعه کنید.

همچنین می‌توانید فایل‌های زیر را مستقیماً دانلود کنید:

- [`redis-pod.yaml`](/examples/application/job/redis/redis-pod.yaml)
- [`redis-service.yaml`](/examples/application/job/redis/redis-service.yaml)
- [`Dockerfile`](/examples/application/job/redis/Dockerfile)
- [`job.yaml`](/examples/application/job/redis/job.yaml)
- [`rediswq.py`](/examples/application/job/redis/rediswq.py)
- [`worker.py`](/examples/application/job/redis/worker.py)

برای راه‌اندازی یک نمونهٔ واحد از Redis، باید Pod و Service مربوط به redis را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/job/redis/redis-pod.yaml
kubectl apply -f https://k8s.io/examples/application/job/redis/redis-service.yaml
```

## پر کردن صف با وظایف

اکنون صف را با چند «وظیفه» پر می‌کنیم. در این مثال، وظایف رشته‌هایی هستند که باید چاپ شوند.

یک Pod تعاملی موقت برای اجرای Redis CLI راه‌اندازی کنید.

```shell
kubectl run -i --tty temp --image redis --command "/bin/sh"
```
```
Waiting for pod default/redis2-c7h78 to be running, status is Pending, pod ready: false
Hit enter for command prompt
```

اکنون کلید Enter را بزنید، Redis CLI را اجرا کنید و فهرستی شامل چند آیتم کار ایجاد کنید.

```shell
redis-cli -h redis
```
```console
redis:6379> rpush job2 "apple"
(integer) 1
redis:6379> rpush job2 "banana"
(integer) 2
redis:6379> rpush job2 "cherry"
(integer) 3
redis:6379> rpush job2 "date"
(integer) 4
redis:6379> rpush job2 "fig"
(integer) 5
redis:6379> rpush job2 "grape"
(integer) 6
redis:6379> rpush job2 "lemon"
(integer) 7
redis:6379> rpush job2 "melon"
(integer) 8
redis:6379> rpush job2 "orange"
(integer) 9
redis:6379> lrange job2 0 -1
1) "apple"
2) "banana"
3) "cherry"
4) "date"
5) "fig"
6) "grape"
7) "lemon"
8) "melon"
9) "orange"
```

بنابراین، فهرستی که کلید آن `job2` است، صف کار خواهد بود.

نکته: اگر Kube DNS را به‌درستی پیکربندی نکرده‌اید، ممکن است لازم باشد نخستین مرحلهٔ بلوک بالا را به `redis-cli -h $REDIS_SERVICE_HOST` تغییر دهید.


## ایجاد یک ایمیج کانتینر {#create-an-image}

اکنون آماده‌اید ایمیجی بسازید که کارهای موجود در آن صف را پردازش کند.

برای خواندن پیام‌ها از صف پیام، از یک برنامهٔ کارگر پایتون همراه با یک کلاینت Redis استفاده خواهید کرد.

یک کتابخانهٔ کلاینت ساده برای صف کار Redis با نام `rediswq.py` ([دانلود](/examples/application/job/redis/rediswq.py)) در اختیار شما قرار گرفته است.

برنامهٔ «کارگر» در هر Pod از این Job، برای دریافت کار از کتابخانهٔ کلاینت صف کار استفاده می‌کند. کد آن در ادامه آمده است:

{{% code_sample language="python" file="application/job/redis/worker.py" %}}

همچنین می‌توانید فایل‌های [`worker.py`](/examples/application/job/redis/worker.py)، [`rediswq.py`](/examples/application/job/redis/rediswq.py) و [`Dockerfile`](/examples/application/job/redis/Dockerfile) را دانلود کنید و سپس ایمیج کانتینر را بسازید. در ادامه نمونه‌ای از ساخت ایمیج با Docker آمده است:

```shell
docker build -t job-wq-2 .
```

### ارسال (push) ایمیج

برای [Docker Hub](https://hub.docker.com/)، ایمیج برنامهٔ خود را با نام کاربری‌تان برچسب‌گذاری (tag) کنید و با دستورهای زیر آن را به Hub ارسال کنید. به‌جای `<username>` نام کاربری Hub خود را قرار دهید.

```shell
docker tag job-wq-2 <username>/job-wq-2
docker push <username>/job-wq-2
```

باید ایمیج را به یک مخزن عمومی ارسال کنید یا [کلاستر خود را طوری پیکربندی کنید که به مخزن خصوصی شما دسترسی داشته باشد](/docs/concepts/containers/images/).

## تعریف یک Job

مانیفست Jobی که ایجاد خواهید کرد در ادامه آمده است:

{{% code_sample file="application/job/redis/job.yaml" %}}

{{< note >}}
حتماً مانیفست را ویرایش کنید و `gcr.io/myproject` را به مسیر خودتان تغییر دهید.
{{< /note >}}

در این مثال، هر Pod چندین آیتم از صف را پردازش می‌کند و هنگامی که آیتم دیگری باقی نماند، خارج می‌شود. از آنجا که خود کارگرها خالی شدن صف کار را تشخیص می‌دهند و کنترل‌کنندهٔ Job از صف کار اطلاعی ندارد، این کنترل‌کننده برای اطلاع از پایان کار به اعلام کارگرها متکی است. کارگرها با خروج موفقیت‌آمیز، خالی بودن صف را اعلام می‌کنند. بنابراین به محض اینکه **هر یک** از کارگرها با موفقیت خارج شود، کنترل‌کننده متوجه می‌شود که کار به پایان رسیده است و Podها به‌زودی خارج خواهند شد. از این رو، باید تعداد تکمیل (completion count) را برای Job تنظیم‌نشده باقی بگذارید. کنترل‌کنندهٔ Job منتظر می‌ماند تا Podهای دیگر نیز کار خود را به پایان برسانند.

## اجرای Job

اکنون Job را اجرا کنید:

```shell
# this assumes you downloaded and then edited the manifest already
kubectl apply -f ./job.yaml
```

اکنون کمی صبر کنید و سپس وضعیت Job را بررسی کنید:

```shell
kubectl describe jobs/job-wq-2
```
```
Name:             job-wq-2
Namespace:        default
Selector:         controller-uid=b1c7e4e3-92e1-11e7-b85e-fa163ee3c11f
Labels:           controller-uid=b1c7e4e3-92e1-11e7-b85e-fa163ee3c11f
                  job-name=job-wq-2
Annotations:      <none>
Parallelism:      2
Completions:      <unset>
Start Time:       Mon, 11 Jan 2022 17:07:59 +0000
Pods Statuses:    1 Running / 0 Succeeded / 0 Failed
Pod Template:
  Labels:       controller-uid=b1c7e4e3-92e1-11e7-b85e-fa163ee3c11f
                job-name=job-wq-2
  Containers:
   c:
    Image:              container-registry.example/exampleproject/job-wq-2
    Port:
    Environment:        <none>
    Mounts:             <none>
  Volumes:              <none>
Events:
  FirstSeen    LastSeen    Count    From            SubobjectPath    Type        Reason            Message
  ---------    --------    -----    ----            -------------    --------    ------            -------
  33s          33s         1        {job-controller }                Normal      SuccessfulCreate  Created pod: job-wq-2-lglf8
```

می‌توانید با تعیین یک مهلت زمانی، منتظر بمانید تا Job با موفقیت به پایان برسد:
```shell
# The check for condition name is case insensitive
kubectl wait --for=condition=complete --timeout=300s job/job-wq-2
```

```shell
kubectl logs pods/job-wq-2-7r7b2
```
```
Worker with sessionID: bbd72d0a-9e5c-4dd6-abf6-416cc267991f
Initial queue state: empty=False
Working on banana
Working on date
Working on lemon
```

همان‌طور که می‌بینید، یکی از Podهای این Job چندین واحد کار را پردازش کرده است.

<!-- discussion -->

## راهکارهای جایگزین

اگر اجرای یک سرویس صف یا تغییر کانتینرها برای استفاده از صف کار برایتان دشوار است، می‌توانید یکی از دیگر [الگوهای Job](/docs/concepts/workloads/controllers/job/#job-patterns) را در نظر بگیرید.

اگر جریان پیوسته‌ای از کارهای پردازشی پس‌زمینه برای اجرا دارید، بهتر است کارگرهای پس‌زمینهٔ خود را به‌جای Job با یک ReplicaSet اجرا کنید و استفاده از یک کتابخانهٔ پردازش پس‌زمینه مانند [https://github.com/resque/resque](https://github.com/resque/resque) را نیز در نظر بگیرید.
