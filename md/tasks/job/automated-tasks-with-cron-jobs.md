---
title: اجرای وظایف خودکار با CronJob
min-kubernetes-server-version: v1.21
reviewers:
- chenopis
content_type: task
weight: 10
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان با استفاده از آبجکت {{< glossary_tooltip text="CronJob" term_id="cronjob" >}} در کوبرنتیز، وظایف خودکار را اجرا کرد.

## {{% heading "prerequisites" %}}

* {{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## ایجاد یک CronJob {#creating-a-cron-job}

هر کرون‌جاب (cron job) به یک فایل پیکربندی نیاز دارد.
در ادامه، مانیفست یک CronJob آمده است که هر دقیقه یک وظیفهٔ نمایشی ساده را اجرا می‌کند:

{{% code_sample file="application/job/cronjob.yaml" %}}

با این دستور، CronJob نمونه را اجرا کنید:

```shell
kubectl create -f https://k8s.io/examples/application/job/cronjob.yaml
```
خروجی مشابه زیر است:

```
cronjob.batch/hello created
```

پس از ایجاد کرون‌جاب، وضعیت آن را با این دستور دریافت کنید:

```shell
kubectl get cronjob hello
```

خروجی مشابه زیر است:

```
NAME    SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
hello   */1 * * * *   False     0        <none>          10s
```

همان‌طور که از نتیجهٔ دستور پیداست، کرون‌جاب هنوز هیچ جابی (job) را زمان‌بندی یا اجرا نکرده است.
حدود یک دقیقه ایجاد شدن جاب را {{< glossary_tooltip text="زیر نظر بگیرید" term_id="watch" >}}:

```shell
kubectl get jobs --watch
```
خروجی مشابه زیر است:

```
NAME               COMPLETIONS   DURATION   AGE
hello-4111706356   0/1                      0s
hello-4111706356   0/1           0s         0s
hello-4111706356   1/1           5s         5s
```

اکنون یک جاب در حال اجرا را دیدید که کرون‌جاب «hello» آن را زمان‌بندی کرده است.
می‌توانید پایش جاب را متوقف کنید و دوباره کرون‌جاب را مشاهده کنید تا ببینید که جاب را زمان‌بندی کرده است:

```shell
kubectl get cronjob hello
```

خروجی مشابه زیر است:

```
NAME    SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
hello   */1 * * * *   False     0        50s             75s
```

باید ببینید که کرون‌جاب `hello` در زمانی که در ستون `LAST SCHEDULE` مشخص شده است، یک جاب را با موفقیت زمان‌بندی کرده است. در حال حاضر ۰ جاب فعال وجود دارد؛ یعنی جاب یا به پایان رسیده یا با شکست مواجه شده است.

اکنون پادهایی را که آخرین جاب زمان‌بندی‌شده ایجاد کرده است پیدا کنید و خروجی استاندارد یکی از آن‌ها را مشاهده کنید.

{{< note >}}
نام جاب با نام پاد متفاوت است.
{{< /note >}}

```shell
# Replace "hello-4111706356" with the job name in your system
pods=$(kubectl get pods --selector=job-name=hello-4111706356 --output=jsonpath={.items[*].metadata.name})
```
لاگ پاد را نمایش دهید:

```shell
kubectl logs $pods
```
خروجی مشابه زیر است:

```
Fri Feb 22 11:02:09 UTC 2019
Hello from the Kubernetes cluster
```

## حذف یک CronJob {#deleting-a-cron-job}

هر زمان که دیگر به یک کرون‌جاب نیاز نداشتید، آن را با `kubectl delete cronjob <cronjob name>` حذف کنید:

```shell
kubectl delete cronjob hello
```

حذف کرون‌جاب، همهٔ جاب‌ها و پادهایی را که ایجاد کرده است پاک می‌کند و مانع از ایجاد جاب‌های بیشتر توسط آن می‌شود.
برای آشنایی بیشتر با حذف جاب‌ها، بخش [جمع‌آوری زباله](/docs/concepts/architecture/garbage-collection/) را بخوانید.
