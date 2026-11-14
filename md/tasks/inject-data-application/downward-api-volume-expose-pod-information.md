---
title: افشای اطلاعات Pod برای کانتینرها از طریق فایل‌ها
content_type: task
weight: 40
---

<!-- overview -->

این صفحه نشان می‌دهد که یک Pod چگونه می‌تواند با استفاده از یک
[حجم `downwardAPI`](/docs/concepts/storage/volumes/#downwardapi)
اطلاعاتی دربارهٔ خودش را در اختیار کانتینرهایی قرار دهد که در آن Pod اجرا می‌شوند.
یک حجم `downwardAPI` می‌تواند فیلدهای Pod و فیلدهای کانتینر را در دسترس قرار دهد.

در کوبرنتیز، دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر برای یک کانتینر در حال اجرا وجود دارد:

* [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
* فایل‌های حجم (volume)، همان‌طور که در این تمرین توضیح داده می‌شود

به این دو روش برای در دسترس قرار دادن فیلدهای Pod و کانتینر، روی هم رفته
_downward API_ گفته می‌شود.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}


<!-- steps -->

## ذخیرهٔ فیلدهای Pod

در این بخش از تمرین، یک Pod با یک کانتینر ایجاد می‌کنید و فیلدهای سطح Pod را
به‌صورت فایل در کانتینر در حال اجرا قرار می‌دهید (project می‌کنید).
مانیفست این Pod در ادامه آمده است:

{{% code_sample file="pods/inject/dapi-volume.yaml" %}}

در این مانیفست می‌بینید که Pod یک حجم `downwardAPI` دارد
و کانتینر این حجم را در مسیر `/etc/podinfo` سوار (mount) می‌کند.

به آرایهٔ `items` در زیر `downwardAPI` نگاه کنید. هر عنصر این آرایه
یک حجم `downwardAPI` را تعریف می‌کند.
عنصر اول مشخص می‌کند که مقدار فیلد `metadata.labels` مربوط به Pod
باید در فایلی به نام `labels` ذخیره شود.
عنصر دوم مشخص می‌کند که مقدار فیلد `annotations` مربوط به Pod
باید در فایلی به نام `annotations` ذخیره شود.

{{< note >}}
فیلدهای این مثال، فیلدهای Pod هستند و
فیلدهای کانتینرِ درون Pod نیستند.
{{< /note >}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-volume.yaml
```

بررسی کنید که کانتینر درون Pod در حال اجرا باشد:

```shell
kubectl get pods
```

لاگ‌های کانتینر را مشاهده کنید:

```shell
kubectl logs kubernetes-downwardapi-volume-example
```

خروجی، محتوای فایل `labels` و فایل `annotations` را نشان می‌دهد:

```
cluster="test-cluster1"
rack="rack-22"
zone="us-est-coast"

build="two"
builder="john-doe"
```

یک پوسته (shell) در کانتینری که در Pod شما اجرا می‌شود باز کنید:

```shell
kubectl exec -it kubernetes-downwardapi-volume-example -- sh
```

در پوستهٔ خود، فایل `labels` را مشاهده کنید:

```shell
/# cat /etc/podinfo/labels
```

خروجی نشان می‌دهد که همهٔ برچسب‌های Pod در فایل `labels`
نوشته شده‌اند:

```shell
cluster="test-cluster1"
rack="rack-22"
zone="us-est-coast"
```

به همین ترتیب، فایل `annotations` را مشاهده کنید:

```shell
/# cat /etc/podinfo/annotations
```

فایل‌های موجود در دایرکتوری `/etc/podinfo` را مشاهده کنید:

```shell
/# ls -laR /etc/podinfo
```

در خروجی می‌بینید که فایل‌های `labels` و `annotations`
در یک زیردایرکتوری موقت قرار دارند که در این مثال
`..2982_06_02_21_47_53.299460680` است. در دایرکتوری `/etc/podinfo`، مسیر `..data`
یک پیوند نمادین (symbolic link) به این زیردایرکتوری موقت است. همچنین در دایرکتوری `/etc/podinfo`،
فایل‌های `labels` و `annotations` پیوند نمادین هستند.

```
drwxr-xr-x  ... Feb 6 21:47 ..2982_06_02_21_47_53.299460680
lrwxrwxrwx  ... Feb 6 21:47 ..data -> ..2982_06_02_21_47_53.299460680
lrwxrwxrwx  ... Feb 6 21:47 annotations -> ..data/annotations
lrwxrwxrwx  ... Feb 6 21:47 labels -> ..data/labels

/etc/..2982_06_02_21_47_53.299460680:
total 8
-rw-r--r--  ... Feb  6 21:47 annotations
-rw-r--r--  ... Feb  6 21:47 labels
```

استفاده از پیوندهای نمادین، به‌روزرسانی پویا و اتمی فراداده‌ها را ممکن می‌کند؛ به‌روزرسانی‌ها
در یک دایرکتوری موقت جدید نوشته می‌شوند و پیوند نمادین `..data` با استفاده از
[rename(2)](http://man7.org/linux/man-pages/man2/rename.2.html) به‌صورت اتمی به‌روزرسانی می‌شود.

{{< note >}}
کانتینری که از Downward API به‌صورت سوارکردن حجم با
[subPath](/docs/concepts/storage/volumes/#using-subpath) استفاده می‌کند،
به‌روزرسانی‌های Downward API را دریافت نخواهد کرد.
{{< /note >}}

از پوسته خارج شوید:

```shell
/# exit
```

## ذخیرهٔ فیلدهای کانتینر

در تمرین قبل، فیلدهای سطح Pod را با استفاده از downward API
در دسترس قرار دادید.
در تمرین بعدی، فیلدهایی را منتقل می‌کنید که بخشی از تعریف Pod هستند،
اما به‌جای کل Pod، از
[کانتینر](/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container)
مشخصی گرفته می‌شوند. مانیفست Pod زیر نیز
تنها یک کانتینر دارد:

{{% code_sample file="pods/inject/dapi-volume-resources.yaml" %}}

در این مانیفست می‌بینید که Pod یک
[حجم `downwardAPI`](/docs/concepts/storage/volumes/#downwardapi)
دارد و تنها کانتینر آن Pod، این حجم را در مسیر `/etc/podinfo` سوار می‌کند.

به آرایهٔ `items` در زیر `downwardAPI` نگاه کنید. هر عنصر این آرایه
یک فایل را در حجم downward API تعریف می‌کند.

عنصر اول مشخص می‌کند که در کانتینری به نام `client-container`،
مقدار فیلد `limits.cpu` با قالبی که `1m` تعیین می‌کند،
باید به‌صورت فایلی به نام `cpu_limit` منتشر شود. فیلد `divisor` اختیاری است و
مقدار پیش‌فرض آن `1` است. مقسوم‌علیه ۱ برای منابع `cpu` به معنای هسته
و برای منابع `memory` به معنای بایت است.

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-volume-resources.yaml
```

یک پوسته در کانتینری که در Pod شما اجرا می‌شود باز کنید:

```shell
kubectl exec -it kubernetes-downwardapi-volume-example-2 -- sh
```

در پوستهٔ خود، فایل `cpu_limit` را مشاهده کنید:

```shell
# Run this in a shell inside the container
cat /etc/podinfo/cpu_limit
```

با دستورهای مشابه می‌توانید فایل‌های `cpu_request`، `mem_limit` و
`mem_request` را مشاهده کنید.

<!-- discussion -->

## نگاشت کلیدها به مسیرهای مشخص و تعیین مجوزهای فایل

می‌توانید کلیدها را به مسیرهای مشخص نگاشت (project) کنید و برای هر فایل
مجوزهای مشخصی تعیین کنید. برای اطلاعات بیشتر،
[Secretها](/docs/concepts/configuration/secret/) را ببینید.

## {{% heading "whatsnext" %}}

* تعریف API مربوط به [`spec`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#PodSpec)
  در Pod را بخوانید. این تعریف شامل تعریف Container (بخشی از Pod) نیز هست.
* فهرست [فیلدهای موجود](/docs/concepts/workloads/pods/downward-api/#available-fields) را که
  می‌توانید با downward API در دسترس قرار دهید، بخوانید.

دربارهٔ حجم‌ها در مرجع API قدیمی بخوانید:
* تعریف API مربوط به [`Volume`](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#volume-v1-core)
  را بررسی کنید که یک حجم عمومی را در Pod تعریف می‌کند تا کانتینرها به آن دسترسی داشته باشند.
* تعریف API مربوط به [`DownwardAPIVolumeSource`](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#downwardapivolumesource-v1-core)
  را بررسی کنید که حجمی حاوی اطلاعات Downward API را تعریف می‌کند.
* تعریف API مربوط به [`DownwardAPIVolumeFile`](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#downwardapivolumefile-v1-core)
  را بررسی کنید که شامل ارجاع‌هایی به فیلدهای آبجکت یا منبع برای
  پر کردن یک فایل در حجم Downward API است.
* تعریف API مربوط به [`ResourceFieldSelector`](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#resourcefieldselector-v1-core)
  را بررسی کنید که منابع کانتینر و قالب خروجی آن‌ها را مشخص می‌کند.
