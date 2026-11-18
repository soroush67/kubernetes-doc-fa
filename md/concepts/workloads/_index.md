---
title: "بارهای کاری"
weight: 55
description: >
  با Podها، کوچک‌ترین آبجکت محاسباتی قابل استقرار در کوبرنتیز، و انتزاع‌های سطح بالاتری که به اجرای آن‌ها کمک می‌کنند آشنا شوید.
no_list: true
card:
  title: بارهای کاری و Podها
  name: concepts
  weight: 60
---

{{< glossary_definition term_id="workload" length="short" >}}
بار کاری شما چه از یک مؤلفه تشکیل شده باشد و چه از چند مؤلفه که با هم کار می‌کنند، در کوبرنتیز
آن را درون مجموعه‌ای از [_پادها_](/docs/concepts/workloads/pods) اجرا می‌کنید.
در کوبرنتیز، هر Pod نمایانگر مجموعه‌ای از یک یا چند
{{< glossary_tooltip text="کانتینر" term_id="container" >}} در حال اجرا روی کلاستر شماست.

پادهای کوبرنتیز [چرخه عمر مشخصی](/docs/concepts/workloads/pods/pod-lifecycle/) دارند.
برای مثال، وقتی یک پاد در کلاستر شما در حال اجراست، بروز خطای بحرانی در
{{< glossary_tooltip text="نودی" term_id="node" >}} که آن پاد روی آن اجرا می‌شود باعث می‌شود
همه پادهای آن نود از کار بیفتند. کوبرنتیز چنین خرابی‌ای را نهایی تلقی می‌کند: برای بازیابی
باید یک Pod جدید بسازید، حتی اگر آن نود بعداً دوباره سالم شود.

با این حال، برای اینکه کار بسیار ساده‌تر شود، لازم نیست هر Pod را مستقیماً مدیریت کنید.
در عوض می‌توانید از _منابع بار کاری_ استفاده کنید که مجموعه‌ای از پادها را از طرف شما مدیریت می‌کنند.
این منابع، {{< glossary_tooltip term_id="controller" text="کنترل‌کننده‌هایی" >}} را پیکربندی می‌کنند
که اطمینان می‌دهند تعداد درستی از پادهای مناسب، مطابق با وضعیتی که مشخص کرده‌اید، در حال اجرا باشند.

کوبرنتیز چندین منبع بار کاری داخلی فراهم می‌کند:

* [Deployment](/docs/concepts/workloads/controllers/deployment/) و [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)
  (که جایگزین منبع قدیمی
  {{< glossary_tooltip text="ReplicationController" term_id="replication-controller" >}} شده‌اند).
  ‏Deployment گزینه مناسبی برای مدیریت بار کاری یک برنامه بدون حالت (stateless) در کلاستر شماست؛
  در چنین برنامه‌ای هر Pod در Deployment قابل جایگزینی با دیگری است و در صورت نیاز می‌توان آن را عوض کرد.
* با [StatefulSet](/docs/concepts/workloads/controllers/statefulset/) می‌توانید
  یک یا چند Pod مرتبط را اجرا کنید که به نحوی وضعیت (state) را دنبال می‌کنند. برای مثال، اگر بار کاری شما
  داده‌ها را به‌صورت ماندگار ذخیره می‌کند، می‌توانید یک StatefulSet اجرا کنید که هر Pod را با یک
  [PersistentVolume](/docs/concepts/storage/persistent-volumes/) متناظر می‌کند. کد شما که در
  پادهای آن StatefulSet اجرا می‌شود، می‌تواند داده‌ها را برای بهبود تاب‌آوری کلی، در پادهای دیگرِ
  همان StatefulSet تکثیر کند.
* ‏[DaemonSet](/docs/concepts/workloads/controllers/daemonset/) پادهایی را تعریف می‌کند که
  امکاناتی محلی برای نودها فراهم می‌کنند.
  هر بار که نودی را به کلاستر خود اضافه می‌کنید که با مشخصات یک DaemonSet مطابقت دارد،
  control plane یک Pod از آن DaemonSet را روی نود جدید زمان‌بندی می‌کند.
  هر پاد در یک DaemonSet کاری مشابه یک دیمن (daemon) سیستمی روی یک سرور کلاسیک Unix / POSIX
  انجام می‌دهد. یک DaemonSet ممکن است برای عملکرد کلاستر شما اساسی باشد، مانند
  افزونه‌ای برای اجرای [شبکه کلاستر](/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model)؛
  ممکن است به شما در مدیریت نود کمک کند،
  یا ممکن است رفتاری اختیاری فراهم کند که پلتفرم کانتینری مورد استفاده شما را بهبود می‌بخشد.
* ‏[Job](/docs/concepts/workloads/controllers/job/) و
  [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) روش‌های متفاوتی برای
  تعریف وظایفی فراهم می‌کنند که تا پایان اجرا می‌شوند و سپس متوقف می‌شوند.
  با یک [Job](/docs/concepts/workloads/controllers/job/) می‌توانید
  وظیفه‌ای را تعریف کنید که فقط یک بار تا پایان اجرا شود. با یک
  [CronJob](/docs/concepts/workloads/controllers/cron-jobs/) می‌توانید
  همان Job را چندین بار طبق یک زمان‌بندی اجرا کنید.

در اکوسیستم گسترده‌تر کوبرنتیز، منابع بار کاری شخص ثالثی وجود دارند که رفتارهای
بیشتری فراهم می‌کنند. اگر رفتار خاصی بخواهید که بخشی از هسته کوبرنتیز نیست، می‌توانید با استفاده از یک
[تعریف منبع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
یک منبع بار کاری شخص ثالث اضافه کنید. برای مثال، اگر بخواهید گروهی از پادها را برای برنامه خود اجرا کنید
اما تا زمانی که _همه_ پادها در دسترس نباشند کار را متوقف نگه دارید (مثلاً برای یک وظیفه توزیع‌شده با توان عملیاتی بالا)،
می‌توانید افزونه‌ای را پیاده‌سازی یا نصب کنید که این قابلیت را فراهم می‌کند.

## جای‌گذاری بار کاری

{{< feature-state feature_gate_name="GenericWorkload" >}}

اگرچه منابع بار کاری استاندارد (مانند Deploymentها و Jobها) چرخه عمر پادها را مدیریت می‌کنند،
ممکن است نیازمندی‌های زمان‌بندی پیچیده‌ای داشته باشید که در آن‌ها گروه‌هایی از پادها باید به‌عنوان یک واحد واحد در نظر گرفته شوند.

با [Workload API](/docs/concepts/workloads/workload-api/) می‌توانید `PodGroupTemplates` را برای گروه‌بندی پادها تعریف کنید و سیاست‌های زمان‌بندی پیشرفته‌ای مانند
[زمان‌بندی گروهی (gang scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/) را روی آن‌ها اعمال کنید.
کنترل‌کننده‌ها در زمان اجرا، آبجکت‌های [PodGroup](/docs/concepts/workloads/podgroup-api/) را از روی این قالب‌ها می‌سازند
و `Pods` از طریق فیلد `spec.schedulingGroup` به `PodGroup` خود ارجاع می‌دهند.
این قابلیت به‌ویژه برای بارهای کاری پردازش دسته‌ای و یادگیری ماشین که به جای‌گذاری «همه یا هیچ» نیاز دارند مفید است.

## {{% heading "whatsnext" %}}

علاوه بر مطالعه درباره هر نوع API برای مدیریت بار کاری، می‌توانید نحوه انجام
وظایف مشخص را نیز بخوانید:

* [اجرای یک برنامه بدون حالت با استفاده از Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
* اجرای یک برنامه دارای حالت (stateful) به‌صورت [تک‌نمونه‌ای](/docs/tasks/run-application/run-single-instance-stateful-application/)
  یا به‌صورت [مجموعه تکثیرشده](/docs/tasks/run-application/run-replicated-stateful-application/)
* [اجرای وظایف خودکار با CronJob](/docs/tasks/job/automated-tasks-with-cron-jobs/)

برای آشنایی با سازوکارهای کوبرنتیز برای جداسازی کد از پیکربندی،
به [پیکربندی](/docs/concepts/configuration/) مراجعه کنید.

دو مفهوم پشتیبان وجود دارد که پیش‌زمینه‌ای درباره نحوه مدیریت پادهای برنامه‌ها توسط کوبرنتیز
فراهم می‌کنند:
* [جمع‌آوری زباله (garbage collection)](/docs/concepts/architecture/garbage-collection/) پس از حذف _منبع مالک_ آبجکت‌ها،
  آن‌ها را از کلاستر شما پاک می‌کند.
* [کنترل‌کننده _time-to-live پس از اتمام_](/docs/concepts/workloads/controllers/ttlafterfinished/)
  پس از گذشت مدت‌زمان مشخصی از اتمام Jobها، آن‌ها را حذف می‌کند.

پس از اجرای برنامه، ممکن است بخواهید آن را به‌صورت یک
[Service](/docs/concepts/services-networking/service/) یا، فقط برای برنامه‌های وب،
با استفاده از یک [Ingress](/docs/concepts/services-networking/ingress) در اینترنت در دسترس قرار دهید.
