---
title: پردازش موازی درشت‌دانه با استفاده از صف کار
content_type: task
weight: 20
---


<!-- overview -->

در این مثال، یک Job کوبرنتیز را با چند فرایند کارگر (worker) موازی اجرا می‌کنید.

در این مثال، هر پاد پس از ایجاد شدن، یک واحد کار را از صف وظایف (task queue) برمی‌دارد، آن را به پایان می‌رساند، از صف حذف می‌کند و سپس خارج می‌شود.

مراحل این مثال به‌طور خلاصه به شرح زیر است:

1. **راه‌اندازی یک سرویس صف پیام.** در این مثال از RabbitMQ استفاده می‌کنید، اما می‌توانید از سرویس دیگری نیز استفاده کنید. در عمل، یک سرویس صف پیام را یک بار راه‌اندازی می‌کنید و آن را برای Jobهای متعددی دوباره به کار می‌برید.
1. **ایجاد یک صف و پر کردن آن با پیام‌ها.** هر پیام نمایانگر یک وظیفه است که باید انجام شود. در این مثال، هر پیام یک عدد صحیح است که محاسبه‌ای طولانی روی آن انجام خواهیم داد.
1. **راه‌اندازی یک Job که وظایف موجود در صف را پردازش می‌کند.** این Job چندین پاد را راه‌اندازی می‌کند. هر پاد یک وظیفه را از صف پیام برمی‌دارد، آن را پردازش می‌کند و خارج می‌شود.

## {{% heading "prerequisites" %}}


باید از پیش با استفادهٔ پایه و غیرموازی از [Job](/docs/concepts/workloads/controllers/job/) آشنا باشید.

{{< include "task-tutorial-prereqs.md" >}}

به یک رجیستری ایمیج کانتینر نیاز دارید تا بتوانید ایمیج‌هایی را که قرار است در کلاستر اجرا شوند در آن بارگذاری کنید.

در این مثال همچنین فرض بر این است که Docker را به‌صورت محلی نصب کرده‌اید.


<!-- steps -->

## راه‌اندازی یک سرویس صف پیام

این مثال از RabbitMQ استفاده می‌کند، اما می‌توانید آن را طوری تطبیق دهید که از سرویس پیام دیگری از نوع AMQP استفاده کند.

در عمل می‌توانید یک سرویس صف پیام را یک بار در کلاستر راه‌اندازی کنید و آن را برای Jobهای متعدد و همچنین برای سرویس‌های طولانی‌مدت دوباره به کار ببرید.

سرویس RabbitMQ را به‌صورت زیر راه‌اندازی کنید:

```shell
# make a Service for the StatefulSet to use
kubectl create -f https://kubernetes.io/examples/application/job/rabbitmq/rabbitmq-service.yaml
```
```
service "rabbitmq-service" created
```

```shell
kubectl create -f https://kubernetes.io/examples/application/job/rabbitmq/rabbitmq-statefulset.yaml
```
```
statefulset "rabbitmq" created
```

## آزمایش سرویس صف پیام

اکنون می‌توانیم دسترسی به صف پیام را آزمایش کنیم. یک پاد تعاملی موقت ایجاد می‌کنیم، چند ابزار روی آن نصب می‌کنیم و با صف‌ها کار می‌کنیم.

ابتدا یک Pod تعاملی موقت ایجاد کنید.

```shell
# Create a temporary interactive container
kubectl run -i --tty temp --image ubuntu:22.04
```
```
Waiting for pod default/temp-loe07 to be running, status is Pending, pod ready: false
... [ previous line repeats several times .. hit return when it stops ] ...
```

توجه کنید که نام پاد و اعلان خط فرمان (command prompt) شما متفاوت خواهد بود.

سپس ابزارهای `amqp-tools` را نصب کنید تا بتوانید با صف‌های پیام کار کنید.
دستورهای زیر کارهایی را نشان می‌دهند که باید درون پوستهٔ تعاملی آن Pod اجرا کنید:

```shell
apt-get update && apt-get install -y curl ca-certificates amqp-tools python3 dnsutils
```

بعداً یک ایمیج کانتینر خواهید ساخت که این بسته‌ها را در خود دارد.

در گام بعد، بررسی می‌کنید که آیا می‌توانید Service مربوط به RabbitMQ را پیدا کنید:

```
# Run these commands inside the Pod
# Note the rabbitmq-service has a DNS name, provided by Kubernetes:
nslookup rabbitmq-service
```
```
Server:        10.0.0.10
Address:    10.0.0.10#53

Name:    rabbitmq-service.default.svc.cluster.local
Address: 10.0.147.152
```
(نشانی‌های IP متفاوت خواهند بود)

اگر افزونهٔ DNS کلاستر به‌درستی پیکربندی نشده باشد، ممکن است گام قبل برای شما کار نکند.
همچنین می‌توانید نشانی IP آن Service را در یک متغیر محیطی پیدا کنید:

```shell
# run this check inside the Pod
env | grep RABBITMQ_SERVICE | grep HOST
```
```
RABBITMQ_SERVICE_SERVICE_HOST=10.0.147.152
```
(نشانی IP متفاوت خواهد بود)

سپس بررسی می‌کنید که آیا می‌توانید یک صف ایجاد کنید و پیام‌ها را منتشر و مصرف کنید.

```shell
# Run these commands inside the Pod
# In the next line, rabbitmq-service is the hostname where the rabbitmq-service
# can be reached.  5672 is the standard port for rabbitmq.
export BROKER_URL=amqp://guest:guest@rabbitmq-service:5672
# If you could not resolve "rabbitmq-service" in the previous step,
# then use this command instead:
BROKER_URL=amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672

# Now create a queue:

/usr/bin/amqp-declare-queue --url=$BROKER_URL -q foo -d
```
```
foo
```

یک پیام را در صف منتشر کنید:
```shell
/usr/bin/amqp-publish --url=$BROKER_URL -r foo -p -b Hello

# And get it back.

/usr/bin/amqp-consume --url=$BROKER_URL -q foo -c 1 cat && echo 1>&2
```
```
Hello
```

در دستور آخر، ابزار `amqp-consume` یک پیام (`-c 1`) را از صف برداشت و آن را به ورودی استاندارد یک دستور دلخواه فرستاد.
در این مورد، برنامهٔ `cat` نویسه‌هایی را که از ورودی استاندارد خوانده است چاپ می‌کند و دستور echo یک کاراکتر بازگشت به ابتدای سطر (carriage return) اضافه می‌کند تا خروجی مثال خوانا باشد.

## پر کردن صف با وظایف

اکنون صف را با چند وظیفهٔ شبیه‌سازی‌شده پر کنید. در این مثال، وظایف رشته‌هایی هستند که باید چاپ شوند.

در عمل، محتوای پیام‌ها می‌تواند این موارد باشد:

- نام فایل‌هایی که باید پردازش شوند
- فلگ‌های اضافی برای برنامه
- بازه‌هایی از کلیدها در یک جدول پایگاه داده
- پارامترهای پیکربندی برای یک شبیه‌سازی
- شمارهٔ فریم‌های صحنه‌ای که باید رندر شود

اگر داده‌های حجیمی وجود دارد که همهٔ پادهای Job باید به‌صورت فقط‌خواندنی به آن دسترسی داشته باشند، معمولاً آن را در یک سیستم فایل اشتراکی مانند NFS قرار می‌دهید و به‌صورت فقط‌خواندنی روی همهٔ پادها mount می‌کنید، یا برنامهٔ درون پاد را طوری می‌نویسید که بتواند داده‌ها را مستقیماً از یک سیستم فایل کلاستری (مثلاً HDFS) بخواند.

در این مثال، صف را با ابزارهای خط فرمان AMQP ایجاد و پر می‌کنید.
در عمل ممکن است برنامه‌ای بنویسید که صف را با استفاده از یک کتابخانهٔ کلاینت AMQP پر کند.

```shell
# Run this on your computer, not in the Pod
/usr/bin/amqp-declare-queue --url=$BROKER_URL -q job1  -d
```
```
job1
```
آیتم‌ها را به صف اضافه کنید:
```shell
for f in apple banana cherry date fig grape lemon melon
do
  /usr/bin/amqp-publish --url=$BROKER_URL -r job1 -p -b $f
done
```

شما ۸ پیام به صف اضافه کردید.

## ایجاد یک ایمیج کانتینر

اکنون آماده‌اید ایمیجی بسازید که آن را به‌عنوان یک Job اجرا خواهید کرد.

این Job از ابزار `amqp-consume` برای خواندن پیام از صف و انجام کار اصلی استفاده می‌کند. در ادامه یک برنامهٔ نمونهٔ بسیار ساده آمده است:

{{% code_sample language="python" file="application/job/rabbitmq/worker.py" %}}

به اسکریپت مجوز اجرا بدهید:

```shell
chmod +x worker.py
```

اکنون یک ایمیج بسازید. یک پوشهٔ موقت ایجاد کنید، به آن بروید و فایل‌های [Dockerfile](/examples/application/job/rabbitmq/Dockerfile) و [worker.py](/examples/application/job/rabbitmq/worker.py) را دانلود کنید. در هر صورت، ایمیج را با این دستور بسازید:

```shell
docker build -t job-wq-1 .
```

برای [Docker Hub](https://hub.docker.com/)، ایمیج برنامهٔ خود را با نام کاربری‌تان برچسب‌گذاری (tag) کنید و با دستورهای زیر آن را به Hub ارسال کنید. به‌جای `<username>` نام کاربری خود در Hub را قرار دهید.

```shell
docker tag job-wq-1 <username>/job-wq-1
docker push <username>/job-wq-1
```

اگر از رجیستری ایمیج کانتینر دیگری استفاده می‌کنید، ایمیج را برچسب‌گذاری کنید و آن را به همان رجیستری ارسال کنید.

## تعریف یک Job

در ادامه یک مانیفست برای Job آمده است. باید یک نسخه از مانیفست Job تهیه کنید (نام آن را `./job.yaml` بگذارید) و نام ایمیج کانتینر را ویرایش کنید تا با نامی که استفاده کرده‌اید مطابقت داشته باشد.

{{% code_sample file="application/job/rabbitmq/job.yaml" %}}

در این مثال، هر پاد روی یک آیتم از صف کار می‌کند و سپس خارج می‌شود.
بنابراین تعداد تکمیل‌های Job با تعداد آیتم‌های کاری انجام‌شده برابر است. به همین دلیل است که در مانیفست نمونه، مقدار `.spec.completions` برابر با `8` تنظیم شده است.

## اجرای Job

اکنون Job را اجرا کنید:

```shell
# this assumes you downloaded and then edited the manifest already
kubectl apply -f ./job.yaml
```

می‌توانید با تعیین یک مهلت زمانی (timeout) منتظر بمانید تا Job با موفقیت به پایان برسد:
```shell
# The check for condition name is case insensitive
kubectl wait --for=condition=complete --timeout=300s job/job-wq-1
```

سپس وضعیت Job را بررسی کنید:

```shell
kubectl describe jobs/job-wq-1
```
```
Name:             job-wq-1
Namespace:        default
Selector:         controller-uid=41d75705-92df-11e7-b85e-fa163ee3c11f
Labels:           controller-uid=41d75705-92df-11e7-b85e-fa163ee3c11f
                  job-name=job-wq-1
Annotations:      <none>
Parallelism:      2
Completions:      8
Start Time:       Wed, 06 Sep 2022 16:42:02 +0000
Pods Statuses:    0 Running / 8 Succeeded / 0 Failed
Pod Template:
  Labels:       controller-uid=41d75705-92df-11e7-b85e-fa163ee3c11f
                job-name=job-wq-1
  Containers:
   c:
    Image:      container-registry.example/causal-jigsaw-637/job-wq-1
    Port:
    Environment:
      BROKER_URL:       amqp://guest:guest@rabbitmq-service:5672
      QUEUE:            job1
    Mounts:             <none>
  Volumes:              <none>
Events:
  FirstSeen  LastSeen   Count    From    SubobjectPath    Type      Reason              Message
  ─────────  ────────   ─────    ────    ─────────────    ──────    ──────              ───────
  27s        27s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-hcobb
  27s        27s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-weytj
  27s        27s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-qaam5
  27s        27s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-b67sr
  26s        26s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-xe5hj
  15s        15s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-w2zqe
  14s        14s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-d6ppa
  14s        14s        1        {job }                   Normal    SuccessfulCreate    Created pod: job-wq-1-p17e0
```



همهٔ پادهای این Job با موفقیت به پایان رسیدند! کار شما تمام است.


<!-- discussion -->

## روش‌های جایگزین

مزیت این رویکرد آن است که لازم نیست برنامهٔ «کارگر» خود را طوری تغییر دهید که از وجود صف کار آگاه باشد. می‌توانید برنامهٔ کارگر را بدون هیچ تغییری در ایمیج کانتینر خود قرار دهید.

استفاده از این رویکرد مستلزم اجرای یک سرویس صف پیام است.
اگر اجرای سرویس صف برایتان دشوار است، شاید بهتر باشد یکی از دیگر [الگوهای Job](/docs/concepts/workloads/controllers/job/#job-patterns) را در نظر بگیرید.

این رویکرد برای هر آیتم کاری یک پاد ایجاد می‌کند. با این حال، اگر انجام هر آیتم کاری تنها چند ثانیه طول بکشد، ایجاد یک Pod برای هر آیتم ممکن است سربار زیادی به همراه داشته باشد. طراحی دیگری را در نظر بگیرید که چند آیتم کاری را در هر Pod اجرا می‌کند؛ مانند آنچه در [مثال صف کار با موازی‌سازی ریزدانه](/docs/tasks/job/fine-parallel-processing-work-queue/) آمده است.

در این مثال، از ابزار `amqp-consume` برای خواندن پیام از صف و اجرای برنامهٔ اصلی استفاده کردید. مزیت این کار آن است که لازم نیست برنامهٔ خود را طوری تغییر دهید که از وجود صف آگاه باشد.
[مثال صف کار با موازی‌سازی ریزدانه](/docs/tasks/job/fine-parallel-processing-work-queue/) نشان می‌دهد که چگونه می‌توان با استفاده از یک کتابخانهٔ کلاینت با صف کار ارتباط برقرار کرد.

## هشدارها

اگر تعداد تکمیل‌ها کمتر از تعداد آیتم‌های موجود در صف تنظیم شود، همهٔ آیتم‌ها پردازش نخواهند شد.

اگر تعداد تکمیل‌ها بیشتر از تعداد آیتم‌های موجود در صف تنظیم شود، Job تکمیل‌شده به نظر نمی‌رسد، حتی اگر همهٔ آیتم‌های صف پردازش شده باشند. در این حالت، Job پادهای اضافی راه‌اندازی می‌کند که در انتظار دریافت پیام مسدود می‌مانند.
باید سازوکار خودتان را برای تشخیص وجود کار و اندازه‌گیری طول صف بسازید و تعداد تکمیل‌ها را متناسب با آن تنظیم کنید.

در این الگو احتمال وقوع یک شرایط رقابتی (race) وجود دارد، هرچند بعید است. اگر کانتینر در فاصلهٔ میان تأیید دریافت پیام توسط دستور `amqp-consume` و خروج موفقیت‌آمیز کانتینر از بین برود، یا اگر نود پیش از آنکه kubelet بتواند موفقیت پاد را به API server گزارش کند از کار بیفتد، Job تکمیل‌شده به نظر نمی‌رسد، حتی اگر همهٔ آیتم‌های صف پردازش شده باشند.
