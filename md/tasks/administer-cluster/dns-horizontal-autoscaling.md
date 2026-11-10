---
title: مقیاس‌دهی خودکار سرویس DNS در یک کلاستر
content_type: task
weight: 80
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه مقیاس‌دهی خودکار (autoscaling) سرویس DNS را در کلاستر کوبرنتیز خود فعال و پیکربندی کنید.


## {{% heading "prerequisites" %}}


* {{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* این راهنما فرض می‌کند که نودهای شما از معماری پردازنده AMD64 یا Intel 64 استفاده می‌کنند.

* مطمئن شوید که [DNS کوبرنتیز](/docs/concepts/services-networking/dns-pod-service/) فعال است.



<!-- steps -->

## بررسی اینکه آیا مقیاس‌دهی خودکار افقی DNS از قبل فعال است {#determining-whether-dns-horizontal-autoscaling-is-already-enabled}

فهرست {{< glossary_tooltip text="Deploymentها" term_id="deployment" >}}ی موجود در {{< glossary_tooltip text="فضای نام" term_id="namespace" >}} kube-system کلاستر خود را به دست آورید:

```shell
kubectl get deployment --namespace=kube-system
```

خروجی مشابه زیر است:

    NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
    ...
    kube-dns-autoscaler    1/1     1            1           ...
    ...

اگر در خروجی، «kube-dns-autoscaler» را می‌بینید، مقیاس‌دهی خودکار افقی DNS از قبل فعال است و می‌توانید مستقیماً به بخش [تنظیم پارامترهای مقیاس‌دهی خودکار](#tuning-autoscaling-parameters) بروید.

## یافتن نام Deployment مربوط به DNS {#find-scaling-target}

فهرست Deploymentهای DNS را در فضای نام kube-system کلاستر خود به دست آورید:

```shell
kubectl get deployment -l k8s-app=kube-dns --namespace=kube-system
```

خروجی مشابه زیر است:

    NAME      READY   UP-TO-DATE   AVAILABLE   AGE
    ...
    coredns   2/2     2            2           ...
    ...

اگر Deployment مربوط به سرویس‌های DNS را نمی‌بینید، می‌توانید آن را با نامش نیز جست‌وجو کنید:

```shell
kubectl get deployment --namespace=kube-system
```

و به دنبال Deployment با نام `coredns` بگردید.


هدف مقیاس‌دهی شما چنین است:

    Deployment/<your-deployment-name>

که در آن `<your-deployment-name>` نام Deployment مربوط به DNS شماست. برای مثال، اگر نام Deployment مربوط به DNS شما coredns باشد، هدف مقیاس‌دهی شما Deployment/coredns است.

{{< note >}}
سرویس DNS پیش‌فرض کوبرنتیز، CoreDNS است. این سرویس برچسب `k8s-app=kube-dns` را تنظیم می‌کند تا بتواند در کلاسترهایی که در اصل از kube-dns استفاده می‌کردند نیز کار کند.
{{< /note >}}

## فعال‌سازی مقیاس‌دهی خودکار افقی DNS {#enablng-dns-horizontal-autoscaling}

در این بخش، یک Deployment جدید ایجاد می‌کنید. Podهای این Deployment، کانتینری مبتنی بر ایمیج `cluster-proportional-autoscaler-amd64` اجرا می‌کنند.

فایلی با نام `dns-horizontal-autoscaler.yaml` و با محتوای زیر ایجاد کنید:

{{% code_sample file="admin/dns/dns-horizontal-autoscaler.yaml" %}}

در این فایل، به جای `<SCALE_TARGET>` هدف مقیاس‌دهی خود را قرار دهید.

به دایرکتوری حاوی فایل پیکربندی بروید و برای ایجاد Deployment، این فرمان را وارد کنید:

```shell
kubectl apply -f dns-horizontal-autoscaler.yaml
```

خروجی فرمان در صورت موفقیت چنین است:

    deployment.apps/kube-dns-autoscaler created

اکنون مقیاس‌دهی خودکار افقی DNS فعال شده است.

## تنظیم پارامترهای مقیاس‌دهی خودکار DNS {#tuning-autoscaling-parameters}

بررسی کنید که {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}} با نام kube-dns-autoscaler وجود داشته باشد:

```shell
kubectl get configmap --namespace=kube-system
```

خروجی مشابه زیر است:

    NAME                  DATA      AGE
    ...
    kube-dns-autoscaler   1         ...
    ...

داده‌های این ConfigMap را ویرایش کنید:

```shell
kubectl edit configmap kube-dns-autoscaler --namespace=kube-system
```

به دنبال این خط بگردید:

```yaml
linear: '{"coresPerReplica":256,"min":1,"nodesPerReplica":16}'
```

فیلدها را مطابق نیاز خود تغییر دهید. فیلد «min» حداقل تعداد بک‌اندهای DNS را مشخص می‌کند. تعداد واقعی بک‌اندها با این معادله محاسبه می‌شود:

    replicas = max( ceil( cores × 1/coresPerReplica ) , ceil( nodes × 1/nodesPerReplica ) )

توجه کنید که مقادیر `coresPerReplica` و `nodesPerReplica` هر دو از نوع اعشاری (float) هستند.

ایده این است که وقتی کلاستر از نودهایی با هسته‌های زیاد استفاده می‌کند، `coresPerReplica` تعیین‌کننده باشد و وقتی کلاستر از نودهایی با هسته‌های کمتر استفاده می‌کند، `nodesPerReplica` تعیین‌کننده باشد.

الگوهای مقیاس‌دهی دیگری نیز پشتیبانی می‌شوند. برای جزئیات بیشتر، به [cluster-proportional-autoscaler](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler) مراجعه کنید.

## غیرفعال‌سازی مقیاس‌دهی خودکار افقی DNS

برای تنظیم مقیاس‌دهی خودکار افقی DNS چند گزینه وجود دارد. انتخاب گزینهٔ مناسب به شرایط مختلف بستگی دارد.

### گزینهٔ ۱: کاهش مقیاس Deployment مربوط به kube-dns-autoscaler به ۰ رپلیکا

این گزینه در همهٔ شرایط کار می‌کند. این فرمان را وارد کنید:

```shell
kubectl scale deployment --replicas=0 kube-dns-autoscaler --namespace=kube-system
```

خروجی چنین است:

    deployment.apps/kube-dns-autoscaler scaled

بررسی کنید که تعداد رپلیکاها صفر باشد:

```shell
kubectl get rs --namespace=kube-system
```

خروجی در ستون‌های DESIRED و CURRENT مقدار 0 را نشان می‌دهد:

    NAME                                  DESIRED   CURRENT   READY   AGE
    ...
    kube-dns-autoscaler-6b59789fc8        0         0         0       ...
    ...

### گزینهٔ ۲: حذف Deployment مربوط به kube-dns-autoscaler

این گزینه در صورتی کار می‌کند که kube-dns-autoscaler تحت کنترل خود شما باشد؛ یعنی کسی آن را دوباره ایجاد نکند:

```shell
kubectl delete deployment kube-dns-autoscaler --namespace=kube-system
```

خروجی چنین است:

    deployment.apps "kube-dns-autoscaler" deleted

### گزینهٔ ۳: حذف فایل مانیفست kube-dns-autoscaler از نود master

این گزینه در صورتی کار می‌کند که kube-dns-autoscaler تحت کنترل [Addon Manager](https://git.k8s.io/kubernetes/cluster/addons/README.md) (منسوخ‌شده) باشد و شما به نود master دسترسی نوشتن داشته باشید.

وارد نود master شوید و فایل مانیفست مربوطه را حذف کنید. مسیر رایج این فایل برای kube-dns-autoscaler چنین است:

    /etc/kubernetes/addons/dns-horizontal-autoscaler/dns-horizontal-autoscaler.yaml

پس از حذف فایل مانیفست، Addon Manager نیز Deployment مربوط به kube-dns-autoscaler را حذف خواهد کرد.



<!-- discussion -->

## درک نحوهٔ کار مقیاس‌دهی خودکار افقی DNS

* برنامهٔ cluster-proportional-autoscaler جدا از سرویس DNS مستقر می‌شود.

* یک Pod مقیاس‌دهندهٔ خودکار، کلاینتی را اجرا می‌کند که تعداد نودها و هسته‌های کلاستر را به‌طور دوره‌ای از سرور API کوبرنتیز استعلام می‌کند.

* تعداد رپلیکای مطلوب بر اساس نودها و هسته‌های قابل زمان‌بندی فعلی و پارامترهای مقیاس‌دهی تعیین‌شده محاسبه و بر بک‌اندهای DNS اعمال می‌شود.

* پارامترهای مقیاس‌دهی و نقاط داده از طریق یک ConfigMap در اختیار مقیاس‌دهندهٔ خودکار قرار می‌گیرند و این مقیاس‌دهنده در هر بازهٔ استعلام، جدول پارامترهای خود را تازه‌سازی می‌کند تا با آخرین پارامترهای مقیاس‌دهی مطلوب به‌روز بماند.

* پارامترهای مقیاس‌دهی را می‌توان بدون بازسازی یا راه‌اندازی مجدد Pod مقیاس‌دهندهٔ خودکار تغییر داد.

* مقیاس‌دهندهٔ خودکار یک رابط کنترل‌کننده ارائه می‌دهد که از دو الگوی کنترلی پشتیبانی می‌کند: *خطی (linear)* و *پلکانی (ladder)*.



## {{% heading "whatsnext" %}}

* دربارهٔ [زمان‌بندی تضمین‌شده برای Podهای افزونهٔ حیاتی](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/) مطالعه کنید.
* دربارهٔ [پیاده‌سازی cluster-proportional-autoscaler](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler) بیشتر بیاموزید.
