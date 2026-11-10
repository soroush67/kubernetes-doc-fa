---
title: ارتباط میان کانتینرهای یک Pod با استفاده از حجم (volume) مشترک
content_type: task
weight: 120
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه می‌توان از یک حجم برای برقراری ارتباط میان دو کانتینری
استفاده کرد که در یک Pod اجرا می‌شوند. همچنین ببینید چگونه می‌توان با
[اشتراک‌گذاری فضای نام (namespace) پردازه‌ها](/docs/tasks/configure-pod-container/share-process-namespace/)
میان کانتینرها، امکان ارتباط پردازه‌ها با یکدیگر را فراهم کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

##  ایجاد یک Pod که دو کانتینر را اجرا می‌کند

در این تمرین، یک Pod ایجاد می‌کنید که دو کانتینر را اجرا می‌کند. این دو کانتینر
یک حجم مشترک دارند که می‌توانند از آن برای ارتباط با یکدیگر استفاده کنند. فایل
پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/two-container-pod.yaml" %}}

در فایل پیکربندی می‌بینید که Pod یک حجم با نام `shared-data` دارد.

نخستین کانتینری که در فایل پیکربندی فهرست شده است، یک سرور nginx را اجرا می‌کند.
مسیر اتصال (mount path) حجم مشترک در این کانتینر `/usr/share/nginx/html` است.
کانتینر دوم بر پایه ایمیج debian ساخته شده و مسیر اتصال آن `/pod-data` است.
کانتینر دوم فرمان زیر را اجرا می‌کند و سپس خاتمه می‌یابد.

    echo Hello from the debian container > /pod-data/index.html

توجه کنید که کانتینر دوم فایل `index.html` را در دایرکتوری ریشه سرور nginx
می‌نویسد.

Pod و دو کانتینر آن را ایجاد کنید:

    kubectl apply -f https://k8s.io/examples/pods/two-container-pod.yaml

اطلاعات Pod و کانتینرها را مشاهده کنید:

    kubectl get pod two-containers --output=yaml

بخشی از خروجی در ادامه آمده است:

    apiVersion: v1
    kind: Pod
    metadata:
      ...
      name: two-containers
      namespace: default
      ...
    spec:
      ...
      containerStatuses:

      - containerID: docker://c1d8abd1 ...
        image: debian
        ...
        lastState:
          terminated:
            ...
        name: debian-container
        ...

      - containerID: docker://96c1ff2c5bb ...
        image: nginx
        ...
        name: nginx-container
        ...
        state:
          running:
        ...

می‌بینید که کانتینر debian خاتمه یافته و کانتینر nginx همچنان در حال اجراست.

یک شل (shell) در کانتینر nginx باز کنید:

    kubectl exec -it two-containers -c nginx-container -- /bin/bash

در شل خود، بررسی کنید که nginx در حال اجراست:

    root@two-containers:/# apt-get update
    root@two-containers:/# apt-get install curl procps
    root@two-containers:/# ps aux

خروجی مشابه زیر است:

    USER       PID  ...  STAT START   TIME COMMAND
    root         1  ...  Ss   21:12   0:00 nginx: master process nginx -g daemon off;

به یاد دارید که کانتینر debian فایل `index.html` را در دایرکتوری ریشه nginx ایجاد
کرد. با `curl` یک درخواست GET به سرور nginx بفرستید:

```
root@two-containers:/# curl localhost
```

خروجی نشان می‌دهد که nginx یک صفحه وب را ارائه می‌کند که کانتینر debian آن را نوشته است:

```
Hello from the debian container
```

<!-- discussion -->

## بحث

دلیل اصلی اینکه یک Pod می‌تواند چند کانتینر داشته باشد، پشتیبانی از برنامه‌های
کمکی است که به یک برنامه اصلی یاری می‌رسانند. نمونه‌های رایج برنامه‌های کمکی،
دریافت‌کننده‌های داده (data puller)، ارسال‌کننده‌های داده (data pusher) و پراکسی‌ها
هستند. برنامه‌های کمکی و اصلی اغلب باید با یکدیگر ارتباط برقرار کنند. این ارتباط
معمولاً از طریق یک سامانه فایل مشترک، همان‌گونه که در این تمرین نشان داده شد، یا از
طریق رابط شبکه loopback، یعنی localhost، انجام می‌شود. نمونه‌ای از این الگو، یک
وب‌سرور به همراه یک برنامه کمکی است که یک مخزن Git را برای یافتن به‌روزرسانی‌های
جدید به‌طور دوره‌ای بررسی می‌کند.

حجم به‌کاررفته در این تمرین، راهی برای ارتباط کانتینرها در طول عمر Pod فراهم
می‌کند. اگر Pod حذف و دوباره ایجاد شود، همه داده‌های ذخیره‌شده در حجم مشترک از
دست می‌روند.

## {{% heading "whatsnext" %}}


* درباره [الگوهای کانتینرهای ترکیبی](/blog/2015/06/the-distributed-system-toolkit-patterns/) بیشتر بیاموزید.

* درباره [کانتینرهای ترکیبی برای معماری ماژولار](https://www.slideshare.net/Docker/slideshare-burns) بیاموزید.

* [پیکربندی یک Pod برای استفاده از حجم جهت ذخیره‌سازی](/docs/tasks/configure-pod-container/configure-volume-storage/) را ببینید.

* [پیکربندی یک Pod برای اشتراک‌گذاری فضای نام پردازه‌ها میان کانتینرهای آن](/docs/tasks/configure-pod-container/share-process-namespace/) را ببینید.

* [Volume](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#volume-v1-core) را ببینید.

* [Pod](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#pod-v1-core) را ببینید.
