---
title: Job نمایه‌دار برای پردازش موازی با تخصیص ایستای کار
content_type: task
min-kubernetes-server-version: v1.21
weight: 30
---

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

<!-- overview -->


در این مثال، یک Job کوبرنتیز اجرا می‌کنید که از چند فرایند کارگر (worker) موازی استفاده می‌کند.
هر کارگر کانتینر جداگانه‌ای است که در Pod مخصوص به خود اجرا می‌شود. هر Pod یک
_شماره‌ی نمایه_ (index number) دارد که control plane به‌طور خودکار آن را تعیین می‌کند؛ به این ترتیب، هر Pod
می‌تواند تشخیص دهد که روی کدام بخش از کل کار باید کار کند.

نمایه‌ی هر پاد در {{< glossary_tooltip text="حاشیه‌نویسی" term_id="annotation" >}}
`batch.kubernetes.io/job-completion-index` و به‌صورت رشته‌ای که مقدار دهدهی آن را نشان می‌دهد، در دسترس است.
برای اینکه فرایند کانتینری‌شده‌ی کار بتواند این نمایه را دریافت کند،
می‌توانید مقدار این حاشیه‌نویسی را با سازوکار [downward API](/docs/concepts/workloads/pods/downward-api/)
منتشر کنید.
برای سهولت کار، control plane به‌طور خودکار downward API را طوری تنظیم می‌کند که
نمایه را در متغیر محیطی `JOB_COMPLETION_INDEX` در اختیار قرار دهد.

در ادامه، مروری بر مراحل این مثال آمده است:

1. **تعریف یک مانیفست Job با استفاده از تکمیل نمایه‌دار**.
   با downward API می‌توانید حاشیه‌نویسی نمایه‌ی پاد را به‌صورت
   متغیر محیطی یا فایل به کانتینر منتقل کنید.
2. **راه‌اندازی یک Job از نوع `Indexed` بر اساس آن مانیفست**.

## {{% heading "prerequisites" %}}

باید از قبل با استفاده‌ی پایه و
غیرموازی از [Job](/docs/concepts/workloads/controllers/job/) آشنا باشید.

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## انتخاب یک رویکرد

برای دسترسی به آیتم کاری از درون برنامه‌ی کارگر، چند گزینه دارید:

1. متغیر محیطی `JOB_COMPLETION_INDEX` را بخوانید. {{< glossary_tooltip text="کنترل‌کننده‌ی" term_id="controller" >}}
   Job این متغیر را به‌طور خودکار به حاشیه‌نویسی حاوی نمایه‌ی
   تکمیل پیوند می‌دهد.
1. فایلی را بخوانید که نمایه‌ی تکمیل را در خود دارد.
1. اگر نتوانید برنامه را تغییر دهید، می‌توانید آن را درون اسکریپتی قرار دهید
   که نمایه را با یکی از روش‌های بالا می‌خواند و آن را به
   ورودی‌ای تبدیل می‌کند که برنامه بتواند از آن استفاده کند.

در این مثال، فرض کنید گزینه‌ی ۳ را انتخاب کرده‌اید و می‌خواهید ابزار
[rev](https://man7.org/linux/man-pages/man1/rev.1.html) را اجرا کنید. این
برنامه یک فایل را به‌عنوان آرگومان می‌پذیرد و محتوای آن را به‌صورت وارونه چاپ می‌کند.

```shell
rev data.txt
```

از ابزار `rev` موجود در ایمیج کانتینر
[`busybox`](https://hub.docker.com/_/busybox) استفاده خواهید کرد.

از آنجا که این فقط یک مثال است، هر Pod تنها بخش بسیار کوچکی از کار را انجام می‌دهد (وارونه کردن یک
رشته‌ی کوتاه). در یک بار کاری واقعی، ممکن است برای نمونه Jobی بسازید که
وظیفه‌ی تولید ۶۰ ثانیه ویدئو بر اساس داده‌های صحنه را نمایندگی می‌کند.
هر آیتم کاری در Job رندر ویدئو، رندر کردن یک فریم مشخص
از آن کلیپ ویدئویی است. تکمیل نمایه‌دار به این معناست که هر Pod در
Job، با شمارش فریم‌ها از ابتدای کلیپ، می‌داند کدام فریم را باید رندر و منتشر کند.

## تعریف یک Job نمایه‌دار

در ادامه، نمونه‌ای از مانیفست Job آمده است که از حالت تکمیل `Indexed` استفاده می‌کند:

{{% code_sample language="yaml" file="application/job/indexed-job.yaml" %}}

در مثال بالا، از متغیر محیطی داخلی `JOB_COMPLETION_INDEX` استفاده می‌کنید
که کنترل‌کننده‌ی Job آن را برای همه‌ی کانتینرها تنظیم می‌کند. یک [کانتینر init](/docs/concepts/workloads/pods/init-containers/)
نمایه را به یک مقدار ایستا نگاشت می‌کند و آن را در فایلی می‌نویسد که از طریق یک [حجم (volume) از نوع emptyDir](/docs/concepts/storage/volumes/#emptydir)
با کانتینرِ اجراکننده‌ی کارگر به اشتراک گذاشته می‌شود.
در صورت تمایل، می‌توانید [متغیر محیطی دلخواه خود را از طریق downward
API تعریف کنید](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
تا نمایه را در اختیار کانتینرها قرار دهید. همچنین می‌توانید فهرستی از مقادیر را
از یک [ConfigMap به‌صورت متغیر محیطی یا فایل](/docs/tasks/configure-pod-container/configure-pod-configmap/) بارگذاری کنید.

به‌عنوان راه دیگر، می‌توانید مستقیماً [با downward API مقدار حاشیه‌نویسی را
به‌صورت یک فایل حجم منتقل کنید](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/#store-pod-fields)؛
مانند مثال زیر:

{{% code_sample language="yaml" file="application/job/indexed-job-vol.yaml" %}}

## اجرای Job

اکنون Job را اجرا کنید:

```shell
# This uses the first approach (relying on $JOB_COMPLETION_INDEX)
kubectl apply -f https://kubernetes.io/examples/application/job/indexed-job.yaml
```

هنگامی که این Job را ایجاد می‌کنید، control plane مجموعه‌ای از Podها را می‌سازد؛ یکی برای هر نمایه‌ای که مشخص کرده‌اید. مقدار `.spec.parallelism` تعیین می‌کند که چند Pod می‌توانند هم‌زمان اجرا شوند، در حالی که `.spec.completions` تعیین می‌کند Job در مجموع چند Pod ایجاد کند.

از آنجا که `.spec.parallelism` کمتر از `.spec.completions` است، control plane پیش از راه‌اندازی Podهای بیشتر، منتظر می‌ماند تا برخی از نخستین Podها کامل شوند.

می‌توانید با تعیین یک مهلت زمانی، منتظر بمانید تا Job با موفقیت به پایان برسد:
```shell
# The check for condition name is case insensitive
kubectl wait --for=condition=complete --timeout=300s job/indexed-job
```

اکنون Job را توصیف کنید و بررسی کنید که با موفقیت انجام شده باشد.


```shell
kubectl describe jobs/indexed-job
```

خروجی مشابه زیر است:

```
Name:              indexed-job
Namespace:         default
Selector:          controller-uid=bf865e04-0b67-483b-9a90-74cfc4c3e756
Labels:            controller-uid=bf865e04-0b67-483b-9a90-74cfc4c3e756
                   job-name=indexed-job
Annotations:       <none>
Parallelism:       3
Completions:       5
Start Time:        Thu, 11 Mar 2021 15:47:34 +0000
Pods Statuses:     2 Running / 3 Succeeded / 0 Failed
Completed Indexes: 0-2
Pod Template:
  Labels:  controller-uid=bf865e04-0b67-483b-9a90-74cfc4c3e756
           job-name=indexed-job
  Init Containers:
   input:
    Image:      docker.io/library/bash
    Port:       <none>
    Host Port:  <none>
    Command:
      bash
      -c
      items=(foo bar baz qux xyz)
      echo ${items[$JOB_COMPLETION_INDEX]} > /input/data.txt

    Environment:  <none>
    Mounts:
      /input from input (rw)
  Containers:
   worker:
    Image:      docker.io/library/busybox
    Port:       <none>
    Host Port:  <none>
    Command:
      rev
      /input/data.txt
    Environment:  <none>
    Mounts:
      /input from input (rw)
  Volumes:
   input:
    Type:       EmptyDir (a temporary directory that shares a pod's lifetime)
    Medium:
    SizeLimit:  <unset>
Events:
  Type    Reason            Age   From            Message
  ----    ------            ----  ----            -------
  Normal  SuccessfulCreate  4s    job-controller  Created pod: indexed-job-njkjj
  Normal  SuccessfulCreate  4s    job-controller  Created pod: indexed-job-9kd4h
  Normal  SuccessfulCreate  4s    job-controller  Created pod: indexed-job-qjwsz
  Normal  SuccessfulCreate  1s    job-controller  Created pod: indexed-job-fdhq5
  Normal  SuccessfulCreate  1s    job-controller  Created pod: indexed-job-ncslj
```

در این مثال، Job را با مقادیر سفارشی برای هر نمایه اجرا می‌کنید. می‌توانید
خروجی یکی از پادها را بررسی کنید:

```shell
kubectl logs indexed-job-fdhq5 # Change this to match the name of a Pod from that Job
```


خروجی مشابه زیر است:

```
xuq
```
