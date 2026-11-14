---
title: پردازش موازی با استفاده از بسط‌دادن قالب
content_type: task
min-kubernetes-server-version: v1.8
weight: 50
---

<!-- overview -->

این تکلیف نشان می‌دهد که چگونه می‌توان چندین {{< glossary_tooltip text="Job" term_id="job" >}} را بر پایهٔ یک قالب مشترک اجرا کرد. با این روش می‌توانید دسته‌هایی از کار را به‌صورت موازی پردازش کنید.

در این مثال فقط سه مورد وجود دارد: _apple_ (سیب)، _banana_ (موز) و _cherry_ (گیلاس). Jobهای نمونه هر مورد را با چاپ یک رشته و سپس توقفی کوتاه پردازش می‌کنند.

برای آشنایی با نحوهٔ به‌کارگیری این الگو در موارد استفادهٔ واقعی‌تر، بخش [استفاده از Jobها در بارهای کاری واقعی](#using-jobs-in-real-workloads) را ببینید.

## {{% heading "prerequisites" %}}

باید با کاربرد پایه و غیرموازی [Job](/docs/concepts/workloads/controllers/job/) آشنا باشید.

{{< include "task-tutorial-prereqs.md" >}}

برای قالب‌سازی پایه به ابزار خط فرمان `sed` نیاز دارید.

برای دنبال‌کردن مثال قالب‌سازی پیشرفته، به یک نسخهٔ نصب‌شده و سالم از [Python](https://www.python.org/) و کتابخانهٔ قالب Jinja2 برای Python نیاز دارید.

پس از راه‌اندازی Python، می‌توانید Jinja2 را با اجرای دستور زیر نصب کنید:

```shell
pip install --user jinja2
```

<!-- steps -->

## ایجاد Jobها بر پایهٔ یک قالب

ابتدا قالب Job زیر را در فایلی با نام `job-tmpl.yaml` دانلود کنید. محتوای فایلی که دانلود می‌کنید چنین است:

{{% code_sample file="application/job/job-tmpl.yaml" %}}

```shell
# Use curl to download job-tmpl.yaml
curl -L -s -O https://k8s.io/examples/application/job/job-tmpl.yaml
```

فایلی که دانلود کرده‌اید هنوز یک {{< glossary_tooltip text="مانیفست" term_id="manifest" >}} معتبر کوبرنتیز نیست. این قالب در واقع نمایشی YAML از یک آبجکت Job است که چند جانگه‌دار (placeholder) دارد و پیش از استفاده باید آن‌ها را پر کرد. نحو `$ITEM` برای کوبرنتیز معنایی ندارد.


### ایجاد مانیفست‌ها از روی قالب

قطعه‌کد شل زیر با استفاده از `sed` رشتهٔ `$ITEM` را با متغیر حلقه جایگزین می‌کند و نتیجه را در یک دایرکتوری موقت با نام `jobs` می‌نویسد. اکنون آن را اجرا کنید:

```shell
# Expand the template into multiple files, one for each item to be processed.
mkdir ./jobs
for i in apple banana cherry
do
  cat job-tmpl.yaml | sed "s/\$ITEM/$i/" > ./jobs/job-$i.yaml
done
```

بررسی کنید که کار به‌درستی انجام شده باشد:

```shell
ls jobs/
```

خروجی مشابه زیر است:

```
job-apple.yaml
job-banana.yaml
job-cherry.yaml
```

می‌توانید از هر نوع زبان قالب‌سازی (مثلاً Jinja2 یا ERB) استفاده کنید، یا برنامه‌ای بنویسید که مانیفست‌های Job را تولید کند.

### ایجاد Jobها از روی مانیفست‌ها

سپس همهٔ Jobها را با یک دستور kubectl ایجاد کنید:

```shell
kubectl create -f ./jobs
```

خروجی مشابه زیر است:

```
job.batch/process-item-apple created
job.batch/process-item-banana created
job.batch/process-item-cherry created
```

اکنون وضعیت Jobها را بررسی کنید:

```shell
kubectl get jobs -l jobgroup=jobexample
```

خروجی مشابه زیر است:

```
NAME                  COMPLETIONS   DURATION   AGE
process-item-apple    1/1           14s        22s
process-item-banana   1/1           12s        21s
process-item-cherry   1/1           12s        20s
```

گزینهٔ `-l` در kubectl فقط Jobهایی را انتخاب می‌کند که عضو این گروه از Jobها هستند (ممکن است Jobهای نامرتبط دیگری نیز در سیستم وجود داشته باشند).

با استفاده از همان {{< glossary_tooltip text="انتخابگر برچسب" term_id="selector" >}} می‌توانید Podها را نیز بررسی کنید:


```shell
kubectl get pods -l jobgroup=jobexample
```

خروجی مشابه زیر است:

```
NAME                        READY     STATUS      RESTARTS   AGE
process-item-apple-kixwv    0/1       Completed   0          4m
process-item-banana-wrsf7   0/1       Completed   0          4m
process-item-cherry-dnfu9   0/1       Completed   0          4m
```

با این دستور واحد می‌توانیم خروجی همهٔ Jobها را یک‌جا بررسی کنیم:

```shell
kubectl logs -f -l jobgroup=jobexample
```

خروجی باید چنین باشد:

```
Processing item apple
Processing item banana
Processing item cherry
```

### پاک‌سازی {#cleanup-1}

```shell
# Remove the Jobs you created
# Your cluster automatically cleans up their Pods
kubectl delete job -l jobgroup=jobexample
```

## استفاده از پارامترهای پیشرفتهٔ قالب

در [مثال نخست](#create-jobs-based-on-a-template)، هر نمونه از قالب یک پارامتر داشت و همان پارامتر در نام Job نیز به کار می‌رفت. اما [نام‌ها](/docs/concepts/overview/working-with-objects/names/#names) محدودند و فقط می‌توانند نویسه‌های مشخصی داشته باشند.

این مثال کمی پیچیده‌تر از [زبان قالب Jinja](https://palletsprojects.com/p/jinja/) استفاده می‌کند تا مانیفست‌ها و سپس آبجکت‌هایی را از روی آن مانیفست‌ها تولید کند؛ در این مثال هر Job چندین پارامتر دارد.

در این بخش از تکلیف، از یک اسکریپت یک‌خطی Python برای تبدیل قالب به مجموعه‌ای از مانیفست‌ها استفاده می‌کنید.

ابتدا قالب آبجکت Job زیر را کپی کرده و در فایلی با نام `job.yaml.jinja2` قرار دهید:


```liquid
{% set params = [{ "name": "apple", "url": "http://dbpedia.org/resource/Apple", },
                  { "name": "banana", "url": "http://dbpedia.org/resource/Banana", },
                  { "name": "cherry", "url": "http://dbpedia.org/resource/Cherry" }]
%}
{% for p in params %}
{% set name = p["name"] %}
{% set url = p["url"] %}
---
apiVersion: batch/v1
kind: Job
metadata:
  name: jobexample-{{ name }}
  labels:
    jobgroup: jobexample
spec:
  template:
    metadata:
      name: jobexample
      labels:
        jobgroup: jobexample
    spec:
      containers:
      - name: c
        image: busybox:1.28
        command: ["sh", "-c", "echo Processing URL {{ url }} && sleep 5"]
      restartPolicy: Never
{% endfor %}
```

قالب بالا با استفاده از فهرستی از دیکشنری‌های Python (خطوط ۱ تا ۴)، دو پارامتر برای هر آبجکت Job تعریف می‌کند. یک حلقهٔ `for` به‌ازای هر مجموعه از پارامترها یک مانیفست Job تولید می‌کند (خطوط باقی‌مانده).

این مثال بر یکی از ویژگی‌های YAML تکیه دارد: یک فایل YAML می‌تواند چندین سند (در اینجا، مانیفست‌های کوبرنتیز) داشته باشد که با `---` در یک خط جداگانه از هم جدا می‌شوند. می‌توانید خروجی را مستقیماً از طریق پایپ به `kubectl` بفرستید تا Jobها ایجاد شوند.

سپس با استفاده از این برنامهٔ یک‌خطی Python قالب را بسط دهید:

```shell
alias render_template='python -c "from jinja2 import Template; import sys; print(Template(sys.stdin.read()).render());"'
```

با استفاده از `render_template`، پارامترها و قالب را به یک فایل YAML واحد تبدیل کنید که مانیفست‌های کوبرنتیز را در بر دارد:

```shell
# This requires the alias you defined earlier
cat job.yaml.jinja2 | render_template > jobs.yaml
```

می‌توانید فایل `jobs.yaml` را مشاهده کنید تا مطمئن شوید اسکریپت `render_template` به‌درستی کار کرده است.

هنگامی که مطمئن شدید `render_template` همان‌طور که می‌خواهید کار می‌کند، می‌توانید خروجی آن را از طریق پایپ به `kubectl` بفرستید:

```shell
cat job.yaml.jinja2 | render_template | kubectl apply -f -
```

کوبرنتیز Jobهایی را که ایجاد کرده‌اید می‌پذیرد و اجرا می‌کند.

### پاک‌سازی {#cleanup-2}

```shell
# Remove the Jobs you created
# Your cluster automatically cleans up their Pods
kubectl delete job -l jobgroup=jobexample
```


<!-- discussion -->

## استفاده از Jobها در بارهای کاری واقعی

در یک مورد استفادهٔ واقعی، هر Job محاسبهٔ قابل‌توجهی انجام می‌دهد؛ برای نمونه، رندر یک فریم از یک فیلم یا پردازش بازه‌ای از سطرهای یک پایگاه داده. اگر در حال رندر یک فیلم باشید، مقدار `$ITEM` را برابر شمارهٔ فریم قرار می‌دهید. اگر در حال پردازش سطرهای یک جدول پایگاه داده باشید، `$ITEM` را طوری تنظیم می‌کنید که بازهٔ سطرهای مورد پردازش را نشان دهد.

در این تکلیف، دستوری را اجرا کردید که خروجی Podها را با واکشی لاگ‌هایشان جمع‌آوری می‌کرد. در یک مورد استفادهٔ واقعی، هر Pod متعلق به یک Job پیش از پایان کار، خروجی خود را در یک ذخیره‌سازی ماندگار می‌نویسد. می‌توانید برای هر Job از یک PersistentVolume یا از یک سرویس ذخیره‌سازی خارجی استفاده کنید. برای نمونه، اگر در حال رندر فریم‌های یک فیلم هستید، داده‌های فریم رندرشده را با HTTP و روش `PUT` به یک URL بفرستید و برای هر فریم از URL متفاوتی استفاده کنید.

## برچسب‌های Jobها و Podها

پس از ایجاد یک Job، کوبرنتیز به‌طور خودکار {{< glossary_tooltip text="برچسب‌های" term_id="label" >}} دیگری اضافه می‌کند که Podهای یک Job را از Podهای Job دیگر متمایز می‌کنند.

در این مثال، هر Job و قالب Pod آن یک برچسب دارند: `jobgroup=jobexample`.

خود کوبرنتیز به برچسب‌هایی با نام `jobgroup` توجهی نمی‌کند. تعیین یک برچسب برای همهٔ Jobهایی که از روی یک قالب ایجاد می‌کنید، کار با همهٔ آن Jobها را به‌صورت هم‌زمان آسان می‌کند. در [مثال نخست](#create-jobs-based-on-a-template) از یک قالب برای ایجاد چند Job استفاده کردید. این قالب تضمین می‌کند که هر Pod نیز همان برچسب را بگیرد، بنابراین می‌توانید همهٔ Podهای این Jobهای قالب‌محور را با یک دستور واحد بررسی کنید.

{{< note >}}
کلید برچسب `jobgroup` ویژه یا رزروشده نیست. می‌توانید طرح برچسب‌گذاری دلخواه خود را انتخاب کنید. در صورت تمایل می‌توانید از [برچسب‌های پیشنهادی](/docs/concepts/overview/working-with-objects/common-labels/#labels) استفاده کنید.
{{< /note >}}

## روش‌های جایگزین

اگر قصد دارید تعداد زیادی آبجکت Job ایجاد کنید، ممکن است با این موارد روبه‌رو شوید:

- حتی با استفاده از برچسب‌ها، مدیریت این‌همه Job دشوار است.
- اگر Jobهای زیادی را به‌صورت دسته‌ای ایجاد کنید، ممکن است بار سنگینی بر control plane کوبرنتیز وارد کنید. همچنین ممکن است سرور API کوبرنتیز نرخ درخواست‌های شما را محدود کند و درخواست‌هایتان را به‌طور موقت با وضعیت 429 رد کند.
- محدودیت {{< glossary_tooltip text="سهمیهٔ منابع" term_id="resource-quota" >}} روی Jobها شما را محدود می‌کند: هنگامی که حجم زیادی از کار را در یک دسته ایجاد می‌کنید، سرور API برخی از درخواست‌های شما را برای همیشه رد می‌کند.

[الگوهای Job](/docs/concepts/workloads/controllers/job/#job-patterns) دیگری نیز وجود دارند که با آن‌ها می‌توانید حجم زیادی از کار را بدون ایجاد تعداد بسیار زیادی آبجکت Job پردازش کنید.

همچنین می‌توانید نوشتن [کنترل‌کنندهٔ](/docs/concepts/architecture/controller/) اختصاصی خود را برای مدیریت خودکار آبجکت‌های Job در نظر بگیرید.
