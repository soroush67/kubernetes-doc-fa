---
reviewers:
- davidopp
- madhusudancs
title: پیکربندی چند زمان‌بند
content_type: task
weight: 20
---

<!-- overview -->

کوبرنتیز همراه با یک زمان‌بند پیش‌فرض ارائه می‌شود که
[اینجا](/docs/reference/command-line-tools-reference/kube-scheduler/) توضیح داده شده است.
اگر زمان‌بند پیش‌فرض نیازهای شما را برآورده نمی‌کند، می‌توانید زمان‌بند خودتان را پیاده‌سازی کنید.
افزون بر این، حتی می‌توانید چند زمان‌بند را هم‌زمان در کنار زمان‌بند پیش‌فرض اجرا کنید
و به کوبرنتیز بگویید برای هر یک از پادهایتان از کدام زمان‌بند استفاده کند. در ادامه
با یک مثال می‌آموزیم که چگونه چند زمان‌بند را در کوبرنتیز اجرا کنیم.

شرح مفصل نحوهٔ پیاده‌سازی یک زمان‌بند از حوصلهٔ این سند خارج است. برای دیدن یک
نمونهٔ مرجع، به پیاده‌سازی kube-scheduler در
[pkg/scheduler](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler)
در پوشهٔ کد منبع کوبرنتیز مراجعه کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## بسته‌بندی زمان‌بند

فایل اجرایی زمان‌بند خود را در یک ایمیج کانتینر بسته‌بندی کنید. در این مثال
می‌توانید از زمان‌بند پیش‌فرض (kube-scheduler) به‌عنوان زمان‌بند دوم استفاده کنید.
[کد منبع کوبرنتیز را از GitHub](https://github.com/kubernetes/kubernetes) کلون کنید
و آن را بسازید.

```shell
git clone https://github.com/kubernetes/kubernetes.git
cd kubernetes
make
```

یک ایمیج کانتینر بسازید که فایل اجرایی kube-scheduler را در خود داشته باشد. فایل
`Dockerfile` لازم برای ساخت این ایمیج در ادامه آمده است:

```docker
FROM busybox
ADD ./_output/local/bin/linux/amd64/kube-scheduler /usr/local/bin/kube-scheduler
```

این فایل را با نام `Dockerfile` ذخیره کنید، ایمیج را بسازید و آن را به یک رجیستری
ارسال (push) کنید. در این مثال، ایمیج به
[Google Container Registry (GCR)](https://cloud.google.com/container-registry/)
ارسال می‌شود. برای جزئیات بیشتر،
[مستندات](https://cloud.google.com/container-registry/docs/) GCR را بخوانید. به‌جای آن
می‌توانید از [docker hub](https://hub.docker.com/search?q=) نیز استفاده کنید. برای جزئیات
بیشتر به [مستندات](https://docs.docker.com/docker-hub/repos/create/#create-a-repository) docker hub مراجعه کنید.

```shell
docker build -t gcr.io/my-gcp-project/my-kube-scheduler:1.0 .     # The image name and the repository
gcloud docker -- push gcr.io/my-gcp-project/my-kube-scheduler:1.0 # used in here is just an example
```

## تعریف یک Deployment کوبرنتیز برای زمان‌بند

اکنون که زمان‌بند شما در یک ایمیج کانتینر قرار دارد، یک پیکربندی پاد برای آن بسازید
و آن را در کلاستر کوبرنتیز خود اجرا کنید. اما به‌جای ایجاد مستقیم یک پاد در کلاستر،
در این مثال می‌توانید از یک [Deployment](/docs/concepts/workloads/controllers/deployment/)
استفاده کنید. هر [Deployment](/docs/concepts/workloads/controllers/deployment/) یک
[Replica Set](/docs/concepts/workloads/controllers/replicaset/) را مدیریت می‌کند که آن نیز
به نوبهٔ خود پادها را مدیریت می‌کند؛ به این ترتیب زمان‌بند در برابر خرابی‌ها مقاوم می‌شود.
پیکربندی Deployment در ادامه آمده است. آن را با نام `my-scheduler.yaml` ذخیره کنید:

{{% code_sample file="admin/sched/my-scheduler.yaml" %}}

در مانیفست بالا، از یک [KubeSchedulerConfiguration](/docs/reference/scheduling/config/)
برای سفارشی‌سازی رفتار پیاده‌سازی زمان‌بند خود استفاده می‌کنید. این پیکربندی هنگام
راه‌اندازی با گزینهٔ `--config` به `kube-scheduler` داده شده است. فایل پیکربندی در
ConfigMap با نام `my-scheduler-config` ذخیره می‌شود. پاد مربوط به Deployment
`my-scheduler`، ConfigMap `my-scheduler-config` را به‌صورت یک حجم (volume) مانت می‌کند.

در پیکربندی زمان‌بند یادشده، پیاده‌سازی زمان‌بند شما با یک
[KubeSchedulerProfile](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-KubeSchedulerProfile)
نمایش داده می‌شود.
{{< note >}}
برای اینکه مشخص شود کدام زمان‌بند مسئول زمان‌بندی یک پاد خاص است، فیلد `spec.schedulerName`
در مانیفست PodTemplate یا Pod باید با فیلد `schedulerName` در `KubeSchedulerProfile` مطابقت داشته باشد.
همهٔ زمان‌بندهایی که در کلاستر اجرا می‌شوند باید نام‌های یکتا داشته باشند.
{{< /note >}}

همچنین توجه کنید که یک حساب سرویس (service account) اختصاصی با نام `my-scheduler` ایجاد
می‌کنید و ClusterRole `system:kube-scheduler` را به آن متصل می‌کنید تا همان مجوزهای
`kube-scheduler` را به دست آورد.

برای شرح مفصل سایر آرگومان‌های خط فرمان، به
[مستندات kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/) و برای
شرح مفصل سایر پیکربندی‌های قابل سفارشی‌سازی `kube-scheduler`، به
[مرجع پیکربندی زمان‌بند](/docs/reference/config-api/kube-scheduler-config.v1/) مراجعه کنید.

## اجرای زمان‌بند دوم در کلاستر

{{< caution >}}
پیش از استقرار چند زمان‌بند یا چند پروفایل زمان‌بندی، صفحهٔ [اجرای چند زمان‌بند](/docs/concepts/scheduling-eviction/running-multiple-schedulers/) را ببینید تا با راهبردهای مختلف استقرار و روش جلوگیری از تعارض در زمان‌بندی منابع آشنا شوید.
{{< /caution >}}

برای اجرای زمان‌بند خود در یک کلاستر کوبرنتیز، Deployment مشخص‌شده در پیکربندی بالا
را در کلاستر ایجاد کنید:

```shell
kubectl create -f my-scheduler.yaml
```

بررسی کنید که پاد زمان‌بند در حال اجرا باشد:

```shell
kubectl get pods --namespace=kube-system
```

```
NAME                                           READY     STATUS    RESTARTS   AGE
....
my-scheduler-lnf4s-4744f                       1/1       Running   0          2m
...
```

در این فهرست، افزون بر پاد kube-scheduler پیش‌فرض، باید یک پاد my-scheduler را نیز
در وضعیت «Running» ببینید.

### فعال‌سازی انتخاب رهبر

برای اجرای چند زمان‌بند با انتخاب رهبر (leader election) فعال، باید کارهای زیر را انجام دهید:

فیلدهای زیر را برای KubeSchedulerConfiguration در ConfigMap `my-scheduler-config` در فایل YAML خود به‌روزرسانی کنید:

* مقدار `leaderElection.leaderElect` را به `true`
* مقدار `leaderElection.resourceNamespace` را به `<lock-object-namespace>`
* مقدار `leaderElection.resourceName` را به `<lock-object-name>`

{{< note >}}
control plane آبجکت‌های قفل را برایتان ایجاد می‌کند، اما فضای نام (namespace) باید از قبل وجود داشته باشد.
می‌توانید از فضای نام `kube-system` استفاده کنید.
{{< /note >}}

اگر RBAC در کلاستر شما فعال است، باید نقش کلاستری `system:kube-scheduler` را به‌روزرسانی کنید.
نام زمان‌بند خود را مانند مثال زیر به resourceNames در قاعدهٔ مربوط به منابع `endpoints` و `leases` اضافه کنید:

```shell
kubectl edit clusterrole system:kube-scheduler
```

{{% code_sample file="admin/sched/clusterrole.yaml" %}}

## تعیین زمان‌بند برای پادها

اکنون که زمان‌بند دوم شما در حال اجراست، چند پاد ایجاد کنید و مشخص کنید که با
زمان‌بند پیش‌فرض یا با زمان‌بندی که مستقر کرده‌اید زمان‌بندی شوند.
برای زمان‌بندی یک پاد با زمان‌بندی مشخص، نام آن زمان‌بند را در مشخصات (spec) آن پاد
تعیین کنید. سه مثال را با هم بررسی می‌کنیم.

- مشخصات پاد بدون هیچ نام زمان‌بند

  {{% code_sample file="admin/sched/pod1.yaml" %}}

  وقتی هیچ نام زمان‌بندی ارائه نشود، پاد به‌طور خودکار با default-scheduler
  زمان‌بندی می‌شود.

  این فایل را با نام `pod1.yaml` ذخیره کنید و آن را به کلاستر کوبرنتیز ارسال کنید.

  ```shell
  kubectl create -f pod1.yaml
  ```

- مشخصات پاد با `default-scheduler`

  {{% code_sample file="admin/sched/pod2.yaml" %}}

  زمان‌بند با قرار دادن نام آن به‌عنوان مقدار `spec.schedulerName` مشخص می‌شود. در این مثال،
  نام زمان‌بند پیش‌فرض، یعنی `default-scheduler`، را ارائه می‌کنیم.

  این فایل را با نام `pod2.yaml` ذخیره کنید و آن را به کلاستر کوبرنتیز ارسال کنید.

  ```shell
  kubectl create -f pod2.yaml
  ```

- مشخصات پاد با `my-scheduler`

  {{% code_sample file="admin/sched/pod3.yaml" %}}

  در این مثال، مشخص می‌کنیم که این پاد باید با زمان‌بندی که مستقر کرده‌ایم، یعنی
  `my-scheduler`، زمان‌بندی شود. توجه کنید که مقدار `spec.schedulerName` باید با نامی
  که برای زمان‌بند در فیلد `schedulerName` از `KubeSchedulerProfile` متناظر ارائه شده است، مطابقت داشته باشد.

  این فایل را با نام `pod3.yaml` ذخیره کنید و آن را به کلاستر کوبرنتیز ارسال کنید.

  ```shell
  kubectl create -f pod3.yaml
  ```

  بررسی کنید که هر سه پاد در حال اجرا باشند.

  ```shell
  kubectl get pods
  ```

<!-- discussion -->

### بررسی اینکه پادها با زمان‌بندهای موردنظر زمان‌بندی شده‌اند

برای اینکه کار با این مثال‌ها ساده‌تر شود، بررسی نکردیم که پادها واقعاً با
زمان‌بندهای موردنظر زمان‌بندی شده‌اند. این موضوع را می‌توان با تغییر ترتیب ارسال
پیکربندی‌های پاد و Deployment در بالا بررسی کرد. اگر همهٔ پیکربندی‌های پاد را پیش از
پیکربندی Deployment زمان‌بند به کلاستر کوبرنتیز ارسال کنیم، می‌بینیم که پاد
`annotation-second-scheduler` برای همیشه در وضعیت «Pending» باقی می‌ماند، در حالی که
دو پاد دیگر زمان‌بندی می‌شوند. به محض اینکه پیکربندی Deployment زمان‌بند را ارسال
کنیم و زمان‌بند جدید اجرا شود، پاد `annotation-second-scheduler` نیز زمان‌بندی می‌شود.

همچنین می‌توانید برای اطمینان از اینکه پادها با زمان‌بندهای موردنظر زمان‌بندی
شده‌اند، ورودی‌های «Scheduled» را در لاگ رویدادها بررسی کنید.

```shell
kubectl get events
```
همچنین می‌توانید با تغییر مانیفست پاد ایستای زمان‌بند اصلی کلاستر روی نودهای
control plane مربوطه، از یک [پیکربندی سفارشی زمان‌بند](/docs/reference/scheduling/config/#multiple-profiles)
یا یک ایمیج کانتینر سفارشی برای آن استفاده کنید.
