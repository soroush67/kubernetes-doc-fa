---
reviewers:
- erictune
- mimowo
- soltysh
title: Jobها
api_metadata:
- apiVersion: "batch/v1"
  kind: "Job"
content_type: concept
description: >-
  Jobها وظایف یک‌باره‌ای را نمایش می‌دهند که تا تکمیل اجرا می‌شوند و سپس متوقف می‌شوند.
feature:
  title: اجرای دسته‌ای
  description: >
    کوبرنتیز علاوه بر سرویس‌ها می‌تواند بارهای کاری دسته‌ای و CI شما را نیز مدیریت کند و در صورت تمایل، کانتینرهایی را که از کار می‌افتند جایگزین کند.
weight: 50
hide_summary: true # Listed separately in section index
---

<!-- overview -->

یک Job یک یا چند Pod ایجاد می‌کند و تا زمانی که تعداد مشخصی از آن‌ها با موفقیت خاتمه یابند، به تلاش مجدد برای اجرای Podها ادامه می‌دهد.
با تکمیل موفق Podها، Job تکمیل‌های موفق را ردیابی می‌کند. هنگامی که تعداد مشخصی
از تکمیل‌های موفق حاصل شود، وظیفه (یعنی Job) کامل می‌شود. حذف یک Job، Podهایی را که ایجاد کرده است
پاک‌سازی می‌کند. تعلیق یک Job، Podهای فعال آن را تا زمانی که Job
دوباره از سر گرفته شود حذف می‌کند.

یک حالت ساده، ایجاد یک آبجکت Job برای اجرای مطمئن یک Pod تا تکمیل است.
اگر Pod نخست از کار بیفتد یا حذف شود (برای مثال
به دلیل خرابی سخت‌افزار نود یا راه‌اندازی مجدد نود)، آبجکت Job یک Pod جدید آغاز می‌کند.

همچنین می‌توانید از یک Job برای اجرای موازی چند Pod استفاده کنید.

اگر می‌خواهید یک Job (چه یک وظیفه‌ی منفرد و چه چند وظیفه به‌صورت موازی) را طبق یک زمان‌بندی اجرا کنید،
به [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) مراجعه کنید.

<!-- body -->

## اجرای یک Job نمونه

در اینجا یک پیکربندی نمونه‌ی Job آمده است. این Job عدد π را تا ۲۰۰۰ رقم محاسبه و چاپ می‌کند.
تکمیل آن حدود ۱۰ ثانیه طول می‌کشد.

{{% code_sample file="controllers/job.yaml" %}}

می‌توانید این مثال را با فرمان زیر اجرا کنید:

```shell
kubectl apply -f https://kubernetes.io/examples/controllers/job.yaml
```

خروجی مشابه زیر است:

```
job.batch/pi created
```

وضعیت Job را با `kubectl` بررسی کنید:

{{< tabs name="Check status of Job" >}}
{{< tab name="kubectl describe job pi" codelang="bash" >}}
Name:           pi
Namespace:      default
Selector:       batch.kubernetes.io/controller-uid=c9948307-e56d-4b5d-8302-ae2d7b7da67c
Labels:         batch.kubernetes.io/controller-uid=c9948307-e56d-4b5d-8302-ae2d7b7da67c
                batch.kubernetes.io/job-name=pi
                ...
Annotations:    batch.kubernetes.io/job-tracking: ""
Parallelism:    1
Completions:    1
Start Time:     Mon, 02 Dec 2019 15:20:11 +0200
Completed At:   Mon, 02 Dec 2019 15:21:16 +0200
Duration:       65s
Pods Statuses:  0 Running / 1 Succeeded / 0 Failed
Pod Template:
  Labels:  batch.kubernetes.io/controller-uid=c9948307-e56d-4b5d-8302-ae2d7b7da67c
           batch.kubernetes.io/job-name=pi
  Containers:
   pi:
    Image:      perl:5.34.0
    Port:       <none>
    Host Port:  <none>
    Command:
      perl
      -Mbignum=bpi
      -wle
      print bpi(2000)
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From            Message
  ----    ------            ----  ----            -------
  Normal  SuccessfulCreate  21s   job-controller  Created pod: pi-xf9p4
  Normal  Completed         18s   job-controller  Job completed
{{< /tab >}}
{{< tab name="kubectl get job pi -o yaml" codelang="bash" >}}
apiVersion: batch/v1
kind: Job
metadata:
  annotations: batch.kubernetes.io/job-tracking: ""
             ...  
  creationTimestamp: "2022-11-10T17:53:53Z"
  generation: 1
  labels:
    batch.kubernetes.io/controller-uid: 863452e6-270d-420e-9b94-53a54146c223
    batch.kubernetes.io/job-name: pi
  name: pi
  namespace: default
  resourceVersion: "4751"
  uid: 204fb678-040b-497f-9266-35ffa8716d14
spec:
  backoffLimit: 4
  completionMode: NonIndexed
  completions: 1
  parallelism: 1
  selector:
    matchLabels:
      batch.kubernetes.io/controller-uid: 863452e6-270d-420e-9b94-53a54146c223
  suspend: false
  template:
    metadata:
      creationTimestamp: null
      labels:
        batch.kubernetes.io/controller-uid: 863452e6-270d-420e-9b94-53a54146c223
        batch.kubernetes.io/job-name: pi
    spec:
      containers:
      - command:
        - perl
        - -Mbignum=bpi
        - -wle
        - print bpi(2000)
        image: perl:5.34.0
        imagePullPolicy: IfNotPresent
        name: pi
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Never
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  active: 1
  ready: 0
  startTime: "2022-11-10T17:53:57Z"
  uncountedTerminatedPods: {}
{{< /tab >}}
{{< /tabs >}}

برای مشاهده‌ی Podهای تکمیل‌شده‌ی یک Job، از `kubectl get pods` استفاده کنید.

برای فهرست کردن همه‌ی Podهای متعلق به یک Job به شکلی قابل خواندن توسط ماشین، می‌توانید از فرمانی مانند این استفاده کنید:

```shell
pods=$(kubectl get pods --selector=batch.kubernetes.io/job-name=pi --output=jsonpath='{.items[*].metadata.name}')
echo $pods
```

خروجی مشابه زیر است:

```
pi-5rwd7
```

در اینجا، انتخابگر همان انتخابگر Job است. گزینه‌ی `--output=jsonpath` عبارتی را مشخص می‌کند
که نام هر Pod را از فهرست بازگردانده‌شده استخراج می‌کند.

خروجی استاندارد یکی از Podها را مشاهده کنید:

```shell
kubectl logs $pods
```

روش دیگری برای مشاهده‌ی لاگ‌های یک Job:

```shell
kubectl logs jobs/pi
```

خروجی مشابه زیر است:

