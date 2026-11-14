---
title: تأمین ظرفیت مازاد نودها برای یک کلاستر
content_type: task
weight: 10
---


<!-- overview -->

این صفحه شما را در پیکربندی تأمین ظرفیت مازاد (overprovisioning) برای {{< glossary_tooltip text="نود" term_id="node" >}}ها
در کلاستر کوبرنتیز راهنمایی می‌کند. تأمین ظرفیت مازاد نودها راهبردی است که بخشی از منابع محاسباتی کلاستر را
از پیش رزرو می‌کند. این رزرو زمان لازم برای زمان‌بندی Podهای جدید را هنگام رویدادهای مقیاس‌دهی کاهش می‌دهد
و پاسخ‌گویی کلاستر را به افزایش ناگهانی ترافیک یا تقاضای بار کاری بهبود می‌بخشد.

با نگه‌داشتن مقداری ظرفیت استفاده‌نشده، اطمینان حاصل می‌کنید که هنگام ایجاد Podهای جدید، منابع بلافاصله
در دسترس باشند و این Podها در مدتی که کلاستر در حال افزایش مقیاس است، به وضعیت انتظار (pending) نروند.

## {{% heading "prerequisites" %}}

- باید یک کلاستر کوبرنتیز داشته باشید و ابزار خط فرمان kubectl برای ارتباط با کلاستر شما
  پیکربندی شده باشد.
- باید از پیش درک پایه‌ای از
  [Deploymentها](/docs/concepts/workloads/controllers/deployment/)،
  {{< glossary_tooltip text="اولویت" term_id="pod-priority" >}} Pod
  و {{< glossary_tooltip text="PriorityClassها" term_id="priority-class" >}} داشته باشید.
- کلاستر شما باید با یک [مقیاس‌دهنده‌ی خودکار](/docs/concepts/cluster-administration/cluster-autoscaling/)
  راه‌اندازی شده باشد که نودها را بر اساس تقاضا مدیریت می‌کند.

<!-- steps -->

## ایجاد یک PriorityClass

کار را با تعریف یک PriorityClass برای Podهای جانگهدار (placeholder) آغاز کنید. ابتدا یک PriorityClass با
مقدار اولویت منفی ایجاد کنید که به‌زودی آن را به Podهای جانگهدار اختصاص خواهید داد.
سپس یک Deployment راه‌اندازی خواهید کرد که از این PriorityClass استفاده می‌کند.

{{% code_sample language="yaml" file="priorityclass/low-priority-class.yaml" %}}

سپس PriorityClass را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/priorityclass/low-priority-class.yaml
```

در گام بعد، یک Deployment تعریف می‌کنید که از PriorityClass با اولویت منفی استفاده می‌کند و یک کانتینر حداقلی را اجرا می‌کند.
وقتی آن را به کلاستر اضافه کنید، کوبرنتیز این Podهای جانگهدار را برای رزرو ظرفیت اجرا می‌کند. هر زمان که
کمبود ظرفیت پیش بیاید، control plane یکی از این Podهای جانگهدار را به‌عنوان نخستین گزینه برای
{{< glossary_tooltip text="پیش‌دستی (preempt)" term_id="preemption" >}} انتخاب می‌کند.

## اجرای Podهایی که ظرفیت نود را درخواست می‌کنند

مانیفست نمونه را بررسی کنید:

{{% code_sample language="yaml" file="deployments/deployment-with-capacity-reservation.yaml" %}}

### انتخاب یک فضای نام برای Podهای جانگهدار

باید یک {{< glossary_tooltip term_id="namespace" text="فضای نام">}} را که Podهای جانگهدار در آن قرار می‌گیرند،
انتخاب یا ایجاد کنید.

### ایجاد Deployment جانگهدار

بر اساس آن مانیفست، یک Deployment ایجاد کنید:

```shell
# Change the namespace name "example"
kubectl --namespace example apply -f https://k8s.io/examples/deployments/deployment-with-capacity-reservation.yaml
```

## تنظیم درخواست‌های منابع Podهای جانگهدار

درخواست‌ها و محدودیت‌های منابع Podهای جانگهدار را پیکربندی کنید تا مقدار منابع مازادی را که می‌خواهید نگه دارید، مشخص شود. این رزرو تضمین می‌کند که مقدار مشخصی از CPU و حافظه برای Podهای جدید در دسترس باقی بماند.

برای ویرایش Deployment، بخش `resources` را در فایل مانیفست Deployment تغییر دهید
تا درخواست‌ها و محدودیت‌های مناسب تنظیم شوند. می‌توانید این فایل را به‌صورت محلی دانلود کنید و سپس
با هر ویرایشگر متنی که ترجیح می‌دهید، آن را ویرایش کنید.

همچنین می‌توانید Deployment را با kubectl ویرایش کنید:

```shell
kubectl edit deployment capacity-reservation
```

برای مثال، برای رزرو مجموعاً ۰٫۵ CPU و ۱GiB حافظه در میان ۵ Pod جانگهدار،
درخواست‌ها و محدودیت‌های منابع را برای هر Pod جانگهدار به این صورت تعریف کنید:

```yaml
  resources:
    requests:
      cpu: "100m"
      memory: "200Mi"
    limits:
      cpu: "100m"
```

## تنظیم تعداد رونوشت‌های دلخواه

### محاسبه‌ی کل منابع رزروشده

<!-- trailing whitespace in next paragraph is significant -->
برای مثال، با ۵ رونوشت (replica) که هر کدام 0.1 CPU و 200MiB حافظه رزرو می‌کنند:  
کل CPU رزروشده: 5 × 0.1 = 0.5 (در مشخصات Pod، مقدار `500m` را می‌نویسید)  
کل حافظه‌ی رزروشده: 5 × 200MiB = 1GiB (در مشخصات Pod، `1 Gi` را می‌نویسید)  

برای مقیاس‌دهی Deployment، تعداد رونوشت‌ها را بر اساس اندازه‌ی کلاستر و بار کاری مورد انتظار تنظیم کنید:

```shell
kubectl scale deployment capacity-reservation --replicas=5
```

مقیاس‌دهی را بررسی کنید:

```shell
kubectl get deployment capacity-reservation
```

خروجی باید تعداد به‌روزشده‌ی رونوشت‌ها را نشان دهد:

```none
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
capacity-reservation   5/5     5            5           2m
```

{{< note >}}
برخی مقیاس‌دهنده‌های خودکار، به‌ویژه [Karpenter](/docs/concepts/cluster-administration/cluster-autoscaling/#autoscaler-karpenter)،
هنگام بررسی مقیاس‌دهی نودها، قواعد affinity ترجیحی را به‌عنوان قواعد اجباری در نظر می‌گیرند.
اگر از Karpenter یا مقیاس‌دهنده‌ی خودکار نود دیگری استفاده می‌کنید که همین روش اکتشافی را به کار می‌گیرد،
تعداد رونوشتی که در اینجا تنظیم می‌کنید، حداقل تعداد نودهای کلاستر شما را نیز تعیین می‌کند.
{{< /note >}}

## {{% heading "whatsnext" %}}

- درباره‌ی [PriorityClassها](/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass) و تأثیر آن‌ها بر زمان‌بندی Podها بیشتر بیاموزید.
- [مقیاس‌دهی خودکار نودها](/docs/concepts/cluster-administration/cluster-autoscaling/) را بررسی کنید تا اندازه‌ی کلاستر را به‌صورت پویا و بر اساس تقاضای بار کاری تنظیم کنید.
- با [پیش‌دستی Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) آشنا شوید که
  سازوکاری کلیدی در کوبرنتیز برای مدیریت رقابت بر سر منابع است. همان صفحه به _بیرون‌رانی_ (eviction) نیز می‌پردازد
  که ارتباط کمتری با رویکرد Podهای جانگهدار دارد، اما آن هم سازوکاری است که کوبرنتیز
  هنگام رقابت بر سر منابع از آن برای واکنش استفاده می‌کند.
