---
title: "مثال: استقرار برنامه‌ی دفتر مهمانان PHP با Redis"
reviewers:
- ahmetb
- jimangel
content_type: tutorial
weight: 20
card:
  name: tutorials
  weight: 30
  title: "مثال بدون حالت: دفتر مهمانان PHP با Redis"
min-kubernetes-server-version: v1.14
source: https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook
---

<!-- overview -->
این آموزش نشان می‌دهد که چگونه یک برنامه‌ی وب ساده و چندلایه را با استفاده از کوبرنتیز و [Docker](https://www.docker.com/) بسازید و مستقر کنید. این برنامه _(برای محیط عملیاتی آماده نیست)_. این مثال از اجزای زیر تشکیل شده است:

* یک نمونه‌ی واحد از [Redis](https://www.redis.io/) برای ذخیره‌ی یادداشت‌های دفتر مهمانان
* چند نمونه از فرانت‌اند وب

## {{% heading "objectives" %}}

* یک نمونه‌ی رهبر (leader) از Redis را راه‌اندازی کنید.
* دو نمونه‌ی پیرو (follower) از Redis را راه‌اندازی کنید.
* فرانت‌اند دفتر مهمانان را راه‌اندازی کنید.
* سرویس فرانت‌اند را در دسترس قرار دهید و آن را مشاهده کنید.
* منابع را پاک‌سازی کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

{{< version-check >}}

<!-- lessoncontent -->

## راه‌اندازی پایگاه داده‌ی Redis

برنامه‌ی دفتر مهمانان داده‌های خود را در Redis ذخیره می‌کند.

### ایجاد Deployment مربوط به Redis

فایل مانیفست زیر یک کنترل‌کننده‌ی Deployment را تعریف می‌کند که یک Pod از Redis را با یک رپلیکا اجرا می‌کند.

{{% code_sample file="application/guestbook/redis-leader-deployment.yaml" %}}

1. یک پنجره‌ی ترمینال را در دایرکتوری‌ای که فایل‌های مانیفست را در آن دانلود کرده‌اید باز کنید.
1. Deployment مربوط به Redis را از فایل `redis-leader-deployment.yaml` اعمال کنید:

   <!---
   for local testing of the content via relative file path
   kubectl apply -f ./content/en/examples/application/guestbook/redis-leader-deployment.yaml
   -->

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-deployment.yaml
   ```

1. برای اطمینان از اجرای Pod مربوط به Redis، فهرست Podها را بررسی کنید:

   ```shell
   kubectl get pods
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME                           READY   STATUS    RESTARTS   AGE
   redis-leader-fb76b4755-xjr2n   1/1     Running   0          13s
   ```

1. برای مشاهده‌ی لاگ‌های Pod رهبر Redis، دستور زیر را اجرا کنید:

   ```shell
   kubectl logs -f deployment/redis-leader
   ```

### ایجاد Service رهبر Redis

برنامه‌ی دفتر مهمانان برای نوشتن داده‌های خود باید با Redis ارتباط برقرار کند. برای هدایت ترافیک به Pod مربوط به Redis، باید یک [Service](/docs/concepts/services-networking/service/) اعمال کنید. هر Service سیاستی را برای دسترسی به Podها تعریف می‌کند.

{{% code_sample file="application/guestbook/redis-leader-service.yaml" %}}

1. Service مربوط به Redis را از فایل `redis-leader-service.yaml` زیر اعمال کنید:

   <!---
   for local testing of the content via relative file path
   kubectl apply -f ./content/en/examples/application/guestbook/redis-leader-service.yaml
   -->

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-service.yaml
   ```

1. برای اطمینان از اجرای Service مربوط به Redis، فهرست Serviceها را بررسی کنید:

   ```shell
   kubectl get service
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME           TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
   kubernetes     ClusterIP   10.0.0.1     <none>        443/TCP    1m
   redis-leader   ClusterIP   10.103.78.24 <none>        6379/TCP   16s
   ```

{{< alert color="info" title="Note" >}}
این فایل مانیفست یک Service با نام `redis-leader` ایجاد می‌کند که مجموعه‌ای از برچسب‌ها را دارد. این برچسب‌ها با برچسب‌هایی که پیش‌تر تعریف شده‌اند مطابقت دارند؛ بنابراین Service ترافیک شبکه را به Pod مربوط به Redis هدایت می‌کند.
{{< /alert >}}

### راه‌اندازی پیروهای Redis

اگرچه رهبر Redis تنها یک Pod است، می‌توانید با افزودن چند پیرو یا رپلیکای Redis، دسترس‌پذیری آن را بالا ببرید و پاسخ‌گوی حجم ترافیک باشید.

{{% code_sample file="application/guestbook/redis-follower-deployment.yaml" %}}

1. Deployment مربوط به Redis را از فایل `redis-follower-deployment.yaml` زیر اعمال کنید:

   <!---
   for local testing of the content via relative file path
   kubectl apply -f ./content/en/examples/application/guestbook/redis-follower-deployment.yaml
   -->

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-deployment.yaml
   ```

1. با بررسی فهرست Podها، از اجرای دو رپلیکای پیرو Redis اطمینان حاصل کنید:

   ```shell
   kubectl get pods
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          37s
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          38s
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          11m
   ```

### ایجاد Service پیروهای Redis

برنامه‌ی دفتر مهمانان برای خواندن داده‌ها باید با پیروهای Redis ارتباط برقرار کند. برای اینکه پیروهای Redis قابل کشف باشند، باید یک [Service](/docs/concepts/services-networking/service/) دیگر راه‌اندازی کنید.

{{% code_sample file="application/guestbook/redis-follower-service.yaml" %}}

1. Service مربوط به Redis را از فایل `redis-follower-service.yaml` زیر اعمال کنید:

   <!---
   for local testing of the content via relative file path
   kubectl apply -f ./content/en/examples/application/guestbook/redis-follower-service.yaml
   -->

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-service.yaml
   ```

1. برای اطمینان از اجرای Service مربوط به Redis، فهرست Serviceها را بررسی کنید:

   ```shell
   kubectl get service
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    3d19h
   redis-follower   ClusterIP   10.110.162.42   <none>        6379/TCP   9s
   redis-leader     ClusterIP   10.103.78.24    <none>        6379/TCP   6m10s
   ```

{{< alert color="info" title="Note" >}}
این فایل مانیفست یک Service با نام `redis-follower` ایجاد می‌کند که مجموعه‌ای از برچسب‌ها را دارد. این برچسب‌ها با برچسب‌هایی که پیش‌تر تعریف شده‌اند مطابقت دارند؛ بنابراین Service ترافیک شبکه را به Pod مربوط به Redis هدایت می‌کند.
{{< /alert >}}

## راه‌اندازی فرانت‌اند دفتر مهمانان و در دسترس قرار دادن آن

اکنون که ذخیره‌سازی Redis دفتر مهمانان شما راه‌اندازی شده و در حال اجراست، سرورهای وب دفتر مهمانان را راه‌اندازی کنید. فرانت‌اند نیز مانند پیروهای Redis با استفاده از یک Deployment کوبرنتیز مستقر می‌شود.

برنامه‌ی دفتر مهمانان از یک فرانت‌اند PHP استفاده می‌کند. این فرانت‌اند طوری پیکربندی شده است که بسته به خواندنی یا نوشتنی بودن درخواست، با Service پیروها یا Service رهبر Redis ارتباط برقرار کند. فرانت‌اند یک رابط JSON ارائه می‌دهد و یک تجربه‌ی کاربری مبتنی بر jQuery-Ajax را در اختیار کاربر قرار می‌دهد.

### ایجاد Deployment فرانت‌اند دفتر مهمانان

{{% code_sample file="application/guestbook/frontend-deployment.yaml" %}}

1. Deployment فرانت‌اند را از فایل `frontend-deployment.yaml` اعمال کنید:

   <!---
   for local testing of the content via relative file path
   kubectl apply -f ./content/en/examples/application/guestbook/frontend-deployment.yaml
   -->

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/frontend-deployment.yaml
   ```

1. برای اطمینان از اجرای سه رپلیکای فرانت‌اند، فهرست Podها را بررسی کنید:

   ```shell
   kubectl get pods -l app=guestbook -l tier=frontend
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME                        READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-5tqhb   1/1     Running   0          47s
   frontend-85595f5bf9-qbzwm   1/1     Running   0          47s
   frontend-85595f5bf9-zchwc   1/1     Running   0          47s
   ```

### ایجاد Service فرانت‌اند

سرویس‌های `Redis` که اعمال کردید فقط از داخل کلاستر کوبرنتیز در دسترس هستند، زیرا نوع پیش‌فرض یک Service، [ClusterIP](/docs/concepts/services-networking/service/#publishing-services-service-types) است. نوع `ClusterIP` یک نشانی IP واحد برای مجموعه Podهایی که Service به آن‌ها اشاره می‌کند فراهم می‌کند. این نشانی IP فقط از داخل کلاستر در دسترس است.

اگر می‌خواهید مهمانان بتوانند به دفتر مهمانان شما دسترسی داشته باشند، باید Service فرانت‌اند را طوری پیکربندی کنید که از بیرون قابل مشاهده باشد تا کلاینت بتواند از بیرون کلاستر کوبرنتیز به Service درخواست بفرستد. با این حال، کاربر کوبرنتیز می‌تواند با استفاده از `kubectl port-forward` به سرویس دسترسی پیدا کند، حتی اگر نوع آن `ClusterIP` باشد.

{{< alert color="info" title="Note" >}}
برخی از ارائه‌دهندگان ابری، مانند Google Compute Engine یا Google Kubernetes Engine، از متعادل‌کننده‌های بار (load balancer) خارجی پشتیبانی می‌کنند. اگر ارائه‌دهنده‌ی ابری شما از متعادل‌کننده‌ی بار پشتیبانی می‌کند و می‌خواهید از آن استفاده کنید، خط `type: LoadBalancer` را از حالت توضیح خارج کنید.
{{< /alert >}}

{{% code_sample file="application/guestbook/frontend-service.yaml" %}}

1. Service فرانت‌اند را از فایل `frontend-service.yaml` اعمال کنید:

   <!---
   for local testing of the content via relative file path
   kubectl apply -f ./content/en/examples/application/guestbook/frontend-service.yaml
   -->

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/frontend-service.yaml
   ```

1. برای اطمینان از اجرای Service فرانت‌اند، فهرست Serviceها را بررسی کنید:

   ```shell
   kubectl get services
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   frontend         ClusterIP   10.97.28.230    <none>        80/TCP     19s
   kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    3d19h
   redis-follower   ClusterIP   10.110.162.42   <none>        6379/TCP   5m48s
   redis-leader     ClusterIP   10.103.78.24    <none>        6379/TCP   11m
   ```

### مشاهده‌ی Service فرانت‌اند با `kubectl port-forward`

1. دستور زیر را اجرا کنید تا پورت `8080` روی ماشین محلی شما به پورت `80` سرویس هدایت شود.

   ```shell
   kubectl port-forward svc/frontend 8080:80
   ```

   خروجی باید مشابه زیر باشد:

   ```
   Forwarding from 127.0.0.1:8080 -> 80
   Forwarding from [::1]:8080 -> 80
   ```

1. برای مشاهده‌ی دفتر مهمانان، صفحه‌ی [http://localhost:8080](http://localhost:8080) را در مرورگر خود باز کنید.

### مشاهده‌ی Service فرانت‌اند با `LoadBalancer`

اگر مانیفست `frontend-service.yaml` را با نوع `LoadBalancer` مستقر کرده‌اید، برای مشاهده‌ی دفتر مهمانان باید نشانی IP آن را پیدا کنید.

1. برای دریافت نشانی IP مربوط به Service فرانت‌اند، دستور زیر را اجرا کنید.

   ```shell
   kubectl get service frontend
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME       TYPE           CLUSTER-IP      EXTERNAL-IP        PORT(S)        AGE
   frontend   LoadBalancer   10.51.242.136   109.197.92.229     80:32372/TCP   1m
   ```

1. نشانی IP خارجی را کپی کنید و برای مشاهده‌ی دفتر مهمانان، صفحه را در مرورگر خود باز کنید.

{{< alert color="info" title="Note" >}}
با نوشتن یک پیام و کلیک روی Submit، چند یادداشت به دفتر مهمانان اضافه کنید. پیامی که نوشته‌اید در فرانت‌اند نمایش داده می‌شود. این پیام نشان می‌دهد که داده‌ها از طریق Serviceهایی که پیش‌تر ایجاد کردید با موفقیت به Redis اضافه شده‌اند.
{{< /alert >}}

## مقیاس‌دهی فرانت‌اند وب

از آنجا که سرورهای شما به‌صورت یک Service تعریف شده‌اند که از یک کنترل‌کننده‌ی Deployment استفاده می‌کند، می‌توانید در صورت نیاز تعداد آن‌ها را افزایش یا کاهش دهید.

1. برای افزایش تعداد Podهای فرانت‌اند، دستور زیر را اجرا کنید:

   ```shell
   kubectl scale deployment frontend --replicas=5
   ```

1. برای بررسی تعداد Podهای فرانت‌اند در حال اجرا، فهرست Podها را مشاهده کنید:

   ```shell
   kubectl get pods
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-5df5m        1/1     Running   0          83s
   frontend-85595f5bf9-7zmg5        1/1     Running   0          83s
   frontend-85595f5bf9-cpskg        1/1     Running   0          15m
   frontend-85595f5bf9-l2l54        1/1     Running   0          14m
   frontend-85595f5bf9-l9c8z        1/1     Running   0          14m
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          97m
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          97m
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          108m
   ```

1. برای کاهش تعداد Podهای فرانت‌اند، دستور زیر را اجرا کنید:

   ```shell
   kubectl scale deployment frontend --replicas=2
   ```

1. برای بررسی تعداد Podهای فرانت‌اند در حال اجرا، فهرست Podها را مشاهده کنید:

   ```shell
   kubectl get pods
   ```

   خروجی باید مشابه زیر باشد:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-cpskg        1/1     Running   0          16m
   frontend-85595f5bf9-l9c8z        1/1     Running   0          15m
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          98m
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          98m
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          109m
   ```

## {{% heading "cleanup" %}}

با حذف Deploymentها و Serviceها، همه‌ی Podهای در حال اجرا نیز حذف می‌شوند. برای حذف چند منبع با یک دستور، از برچسب‌ها استفاده کنید.

1. برای حذف همه‌ی Podها، Deploymentها و Serviceها، دستورهای زیر را اجرا کنید.

   ```shell
   kubectl delete deployment -l app=redis
   kubectl delete service -l app=redis
   kubectl delete deployment frontend
   kubectl delete service frontend
   ```

   خروجی باید مشابه زیر باشد:

   ```
   deployment.apps "redis-follower" deleted
   deployment.apps "redis-leader" deleted
   deployment.apps "frontend" deleted
   service "frontend" deleted
   ```

1. برای اطمینان از اینکه هیچ Podی در حال اجرا نیست، فهرست Podها را بررسی کنید:

   ```shell
   kubectl get pods
   ```

   خروجی باید مشابه زیر باشد:

   ```
   No resources found in default namespace.
   ```

## {{% heading "whatsnext" %}}

* آموزش‌های تعاملی [مبانی کوبرنتیز](/docs/tutorials/kubernetes-basics/) را کامل کنید.
* با استفاده از کوبرنتیز و [حجم‌های پایدار برای MySQL و Wordpress](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/#visit-your-new-wordpress-blog) یک وبلاگ بسازید.
* درباره‌ی [اتصال برنامه‌ها با سرویس‌ها](/docs/tutorials/services/connect-applications-service/) بیشتر بخوانید.
* درباره‌ی [استفاده‌ی مؤثر از برچسب‌ها](/docs/concepts/overview/working-with-objects/labels/#using-labels-effectively) بیشتر بخوانید.

* آموزش [استقرار یک نسخه‌ی قناری](/docs/tutorials/stateless-application/canary-deployment/) را امتحان کنید تا یاد بگیرید چگونه نسخه‌های جدید برنامه را به‌صورت ایمن در محیط عملیاتی آزمایش کنید.
