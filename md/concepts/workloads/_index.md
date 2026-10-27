---
title: "بارهای کاری"
weight: 55
description: >
  با Podها، کوچک‌ترین آبجکت محاسباتی قابل استقرار در کوبرنتیز، و انتزاع‌های سطح بالاتری که به شما در اجرای آن‌ها کمک می‌کنند آشنا شوید.
no_list: true
card:
  title: بارهای کاری و Podها
  name: concepts
  weight: 60
---

{{< glossary_definition term_id="workload" length="short" >}}
چه بار کاری شما یک مؤلفه واحد باشد و چه چند مؤلفه که با یکدیگر کار می‌کنند، در کوبرنتیز آن را درون مجموعه‌ای از [_podها_](/docs/concepts/workloads/pods) اجرا می‌کنید.
در کوبرنتیز، یک Pod نمایانگر مجموعه‌ای از یک یا چند
{{< glossary_tooltip text="کانتینر" term_id="container" >}} در حال اجرا بر روی کلاستر شماست.

Podهای کوبرنتیز دارای یک [چرخه حیات تعریف‌شده](/docs/concepts/workloads/pods/pod-lifecycle/) هستند.
برای مثال، هنگامی که یک pod در کلاستر شما در حال اجراست، بروز یک خطای بحرانی در
{{< glossary_tooltip text="نودی" term_id="node" >}} که آن pod روی آن اجرا می‌شود به این معناست که
تمام podهای روی آن نود از کار می‌افتند. کوبرنتیز این سطح از خرابی را نهایی در نظر می‌گیرد: برای بازیابی
باید یک Pod جدید ایجاد کنید، حتی اگر نود بعداً دوباره سالم شود.

با این حال، برای آسان‌تر شدن قابل‌توجه کار، لازم نیست هر Pod را مستقیماً مدیریت کنید.
در عوض، می‌توانید از _منابع بار کاری_ استفاده کنید که مجموعه‌ای از podها را از طرف شما مدیریت می‌کنند.
این منابع {{< glossary_tooltip term_id="controller" text="کنترل‌کننده‌هایی" >}} را پیکربندی می‌کنند
که اطمینان حاصل می‌کنند تعداد درست از نوع درست pod در حال اجرا باشد تا با وضعیتی که مشخص کرده‌اید مطابقت داشته باشد.

کوبرنتیز چندین منبع بار کاری داخلی فراهم می‌کند:

* [Deployment](/docs/concepts/workloads/controllers/deployment/) و [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)
  (جایگزین منبع قدیمی
  {{< glossary_tooltip text="ReplicationController" term_id="replication-controller" >}}).
  Deployment گزینه‌ای مناسب برای مدیریت بار کاری یک برنامه بدون حالت (stateless) در کلاستر شماست،
  جایی که هر Pod در Deployment قابل جایگزینی است و در صورت نیاز می‌تواند عوض شود.
* [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) به شما امکان می‌دهد
  یک یا چند Pod مرتبط را اجرا کنید که به نحوی وضعیت (state) را نگه می‌دارند. برای مثال، اگر بار کاری شما
  داده‌ها را به‌صورت پایدار ثبت می‌کند، می‌توانید یک StatefulSet اجرا کنید که هر Pod را با یک
  [PersistentVolume](/docs/concepts/storage/persistent-volumes/) مرتبط می‌کند. کد شما که در
  Podهای آن StatefulSet اجرا می‌شود، می‌تواند داده‌ها را به Podهای دیگر در همان StatefulSet
  تکثیر کند تا تاب‌آوری کلی بهبود یابد.
* [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) Podهایی را تعریف می‌کند که
  امکاناتی محلی برای نودها فراهم می‌کنند.
  هر بار که نودی را به کلاستر خود اضافه کنید که با مشخصات یک DaemonSet مطابقت داشته باشد،
  control plane یک Pod مربوط به آن DaemonSet را روی نود جدید زمان‌بندی می‌کند.
  هر pod در یک DaemonSet کاری شبیه به یک daemon سیستمی روی یک سرور کلاسیک Unix / POSIX انجام می‌دهد.
  یک DaemonSet ممکن است برای عملکرد کلاستر شما بنیادین باشد، مانند
  افزونه‌ای برای اجرای [شبکه‌بندی کلاستر](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model)،
  ممکن است به مدیریت نود کمک کند،
  یا می‌تواند رفتارهای اختیاری ارائه دهد که پلتفرم کانتینری در حال اجرای شما را بهبود می‌بخشد.
* [Job](/docs/concepts/workloads/controllers/job/) و
  [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) روش‌های متفاوتی برای
  تعریف وظایفی فراهم می‌کنند که تا اتمام اجرا می‌شوند و سپس متوقف می‌گردند.
  می‌توانید از یک [Job](/docs/concepts/workloads/controllers/job/) برای
  تعریف وظیفه‌ای استفاده کنید که فقط یک بار تا اتمام اجرا می‌شود. می‌توانید از یک
  [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) برای اجرای
  همان Job چندین بار بر اساس یک زمان‌بندی استفاده کنید.

در اکوسیستم گسترده‌تر کوبرنتیز، می‌توانید منابع بار کاری شخص ثالث را بیابید که
رفتارهای اضافی فراهم می‌کنند. با استفاده از یک
[custom resource definition](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)،
می‌توانید در صورتی که رفتار خاصی بخواهید که جزو هسته کوبرنتیز نیست، یک منبع بار کاری شخص ثالث را اضافه کنید. برای مثال، اگر بخواهید گروهی از Podها را برای برنامه خود اجرا کنید اما
در صورت در دسترس نبودن _همه_ Podها کار متوقف شود (شاید برای یک وظیفه توزیع‌شده با توان عملیاتی بالا)،
می‌توانید افزونه‌ای را پیاده‌سازی یا نصب کنید که این قابلیت را فراهم کند.

## جایگذاری بار کاری {#workload-placement}

{{< feature-state feature_gate_name="GenericWorkload" >}}

در حالی که منابع بار کاری استاندارد (مانند Deployment و Job) چرخه حیات Podها را مدیریت می‌کنند،
ممکن است نیازمندی‌های زمان‌بندی پیچیده‌ای داشته باشید که در آن‌ها گروه‌هایی از Podها باید به‌عنوان یک واحد واحد در نظر گرفته شوند.

[Workload API](/docs/concepts/workloads/workload-api/) به شما امکان می‌دهد `PodGroupTemplates` را برای گروه‌بندی Podها تعریف کنید و سیاست‌های زمان‌بندی پیشرفته‌ای روی آن‌ها اعمال نمایید،
مانند [gang scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/).
کنترل‌کننده‌ها در زمان اجرا از روی این قالب‌ها آبجکت‌های [PodGroup](/docs/concepts/workloads/podgroup-api/) را ایجاد می‌کنند
و `Pods` از طریق فیلد
`spec.schedulingGroup` به `PodGroup` خود ارجاع می‌دهند. این ویژگی به‌ویژه برای بارهای کاری پردازش دسته‌ای و یادگیری ماشین که به جایگذاری «همه یا هیچ» نیاز دارند، مفید است.

## {{% heading "whatsnext" %}}

علاوه بر مطالعه درباره هر نوع API برای مدیریت بار کاری، می‌توانید نحوه انجام
وظایف مشخص را نیز بخوانید:

* [اجرای یک برنامه بدون حالت با استفاده از Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
* اجرای یک برنامه حالت‌دار به‌صورت [یک نمونه واحد](/docs/tasks/run-application/run-single-instance-stateful-application/)
  یا به‌صورت [یک مجموعه تکثیرشده](/docs/tasks/run-application/run-replicated-stateful-application/)
* [اجرای وظایف خودکار با CronJob](/docs/tasks/job/automated-tasks-with-cron-jobs/)

برای آشنایی با سازوکارهای کوبرنتیز برای جداسازی کد از پیکربندی،
به بخش [پیکربندی](/docs/concepts/configuration/) مراجعه کنید.

دو مفهوم پشتیبان وجود دارند که پیش‌زمینه‌ای درباره نحوه مدیریت podها برای برنامه‌ها توسط کوبرنتیز ارائه می‌دهند:
* [زباله‌روبی (Garbage collection)](/docs/concepts/architecture/garbage-collection/) آبجکت‌ها را
  پس از حذف _منبع مالک_ آن‌ها از کلاستر شما پاکسازی می‌کند.
* [کنترل‌کننده _time-to-live after finished_](/docs/concepts/workloads/controllers/ttlafterfinished/)
  Jobها را پس از گذشت زمان مشخصی از اتمامشان حذف می‌کند.

هنگامی که برنامه شما در حال اجراست، ممکن است بخواهید آن را به‌عنوان یک [Service](/docs/concepts/services-networking/service/) یا، فقط برای برنامه‌های وب،
با استفاده از یک [Ingress](/docs/concepts/services-networking/ingress) در اینترنت در دسترس قرار دهید.
