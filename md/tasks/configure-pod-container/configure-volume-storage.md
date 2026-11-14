---
title: پیکربندی یک Pod برای استفاده از حجم (Volume) به‌منظور ذخیره‌سازی
content_type: task
weight: 80
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک Pod را پیکربندی کنید تا برای ذخیره‌سازی از یک حجم (Volume) استفاده کند.

سیستم فایل هر کانتینر فقط تا زمانی وجود دارد که خود کانتینر وجود داشته باشد. بنابراین وقتی یک کانتینر خاتمه می‌یابد و دوباره راه‌اندازی می‌شود، تغییرات سیستم فایل از بین می‌روند. برای ذخیره‌سازی پایدارتری که مستقل از کانتینر باشد، می‌توانید از یک [حجم](/docs/concepts/storage/volumes/) استفاده کنید. این موضوع به‌ویژه برای برنامه‌های حالت‌مند (stateful)، مانند مخازن کلید-مقدار (مثلاً Redis) و پایگاه‌های داده، اهمیت دارد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## پیکربندی یک حجم برای Pod

در این تمرین، یک Pod می‌سازید که یک کانتینر را اجرا می‌کند. این Pod یک حجم از نوع
[emptyDir](/docs/concepts/storage/volumes/#emptydir)
دارد که در تمام طول عمر Pod باقی می‌ماند، حتی اگر کانتینر خاتمه یابد و دوباره راه‌اندازی شود. فایل پیکربندی Pod در ادامه آمده است:

{{% code_sample file="pods/storage/redis.yaml" %}}

1. Pod را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/storage/redis.yaml
   ```

1. بررسی کنید که کانتینر Pod در حال اجرا باشد و سپس تغییرات Pod را زیر نظر بگیرید:

   ```shell
   kubectl get pod redis --watch
   ```

   خروجی به این شکل است:

   ```console
   NAME      READY     STATUS    RESTARTS   AGE
   redis     1/1       Running   0          13s
   ```

1. در یک ترمینال دیگر، یک پوسته (shell) در کانتینر در حال اجرا باز کنید:

   ```shell
   kubectl exec -it redis -- /bin/bash
   ```

1. در پوسته، به مسیر `/data/redis` بروید و سپس یک فایل ایجاد کنید:

   ```shell
   root@redis:/data# cd /data/redis/
   root@redis:/data/redis# echo Hello > test-file
   ```

1. در پوسته، فرایندهای در حال اجرا را فهرست کنید:

   ```shell
   root@redis:/data/redis# apt-get update
   root@redis:/data/redis# apt-get install procps
   root@redis:/data/redis# ps aux
   ```

   خروجی مشابه این است:

   ```console
   USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   redis        1  0.1  0.1  33308  3828 ?        Ssl  00:46   0:00 redis-server *:6379
   root        12  0.0  0.0  20228  3020 ?        Ss   00:47   0:00 /bin/bash
   root        15  0.0  0.0  17500  2072 ?        R+   00:48   0:00 ps aux
   ```

1. در پوسته، فرایند Redis را متوقف (kill) کنید:

   ```shell
   root@redis:/data/redis# kill <pid>
   ```

   که در آن `<pid>` شناسه فرایند (PID) مربوط به Redis است.

1. در ترمینال اصلی، تغییرات Pod مربوط به Redis را زیر نظر بگیرید. پس از مدتی، چیزی شبیه به این خواهید دید:

   ```console
   NAME      READY     STATUS     RESTARTS   AGE
   redis     1/1       Running    0          13s
   redis     0/1       Completed  0         6m
   redis     1/1       Running    1         6m
   ```

در این مرحله، کانتینر خاتمه یافته و دوباره راه‌اندازی شده است. علت این است که مقدار
[restartPolicy](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core)
در Pod مربوط به Redis برابر با `Always` است.

1. یک پوسته در کانتینرِ دوباره راه‌اندازی‌شده باز کنید:

   ```shell
   kubectl exec -it redis -- /bin/bash
   ```

1. در پوسته، به مسیر `/data/redis` بروید و بررسی کنید که فایل `test-file` هنوز آنجا باشد.

   ```shell
   root@redis:/data/redis# cd /data/redis/
   root@redis:/data/redis# ls
   test-file
   ```

1. Pod‌ای را که برای این تمرین ایجاد کرده‌اید حذف کنید:

   ```shell
   kubectl delete pod redis
   ```

## {{% heading "whatsnext" %}}

- مرجع [Volume](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#volume-v1-core) را ببینید.

- مرجع [Pod](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#pod-v1-core) را ببینید.

- کوبرنتیز علاوه بر ذخیره‌سازی روی دیسک محلی که `emptyDir` فراهم می‌کند، از راهکارهای متنوع ذخیره‌سازی متصل به شبکه نیز پشتیبانی می‌کند؛ از جمله PD در GCE و EBS در EC2. این راهکارها برای داده‌های حیاتی ترجیح داده می‌شوند و جزئیاتی مانند متصل‌کردن (mount) و جداکردن (unmount) دستگاه‌ها روی نودها را خودشان مدیریت می‌کنند. برای جزئیات بیشتر، [حجم‌ها](/docs/concepts/storage/volumes/) را ببینید.
