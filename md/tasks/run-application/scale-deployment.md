---
title: مقیاس‌دهی افقی دستی برای یک Deployment
content_type: task
weight: 15
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید یک Deployment را با تغییر تعداد رپلیکاهای آن به‌صورت دستی و افقی مقیاس‌دهی کنید.
با مقیاس‌دهی دستی می‌توانید تعداد Podهای در حال اجرا را مستقیماً کنترل کنید؛ این روش برای تغییرات قابل پیش‌بینی بار یا مدیریت هزینه‌ها مناسب است.

این کار با _مقیاس‌دهی عمودی_ (vertical scaling) تفاوت دارد؛ در مقیاس‌دهی عمودی، تعداد رپلیکاها
ثابت می‌ماند و مقدار منابعی که در اختیار هر Pod قرار می‌گیرد تنظیم می‌شود.

## {{% heading "objectives" %}}

- افزایش مقیاس یک Deployment برای رسیدگی به ترافیک بیشتر.
- کاهش مقیاس یک Deployment برای صرفه‌جویی در منابع.
- رساندن مقیاس یک Deployment به صفر برای تعلیق موقت یک بار کاری.
- درک اینکه چه زمانی باید از مقیاس‌دهی دستی و چه زمانی از HorizontalPodAutoscaler استفاده کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

به یک Deployment موجود نیاز دارید. اگر Deploymentای ندارید و فقط می‌خواهید تمرین کنید،
می‌توانید Deployment مربوط به nginx را از صفحهٔ
[اجرای یک برنامهٔ بدون حالت با استفاده از Deployment](/docs/tasks/run-application/run-stateless-application-deployment/) ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/deployment.yaml
```

بررسی کنید که این Deployment دو Pod را اجرا می‌کند:

```shell
kubectl get deployment nginx-deployment
```

خروجی مشابه زیر است:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           10s
```

<!-- steps -->

## افزایش مقیاس یک Deployment

برای تغییر تعداد رپلیکاهای یک Deployment موجود، چند روش مختلف
وجود دارد.

### افزایش مقیاس با استفاده از `kubectl scale`


برای تنظیم تعداد رپلیکاها از `kubectl scale` استفاده کنید:

```shell
kubectl scale deployment/nginx-deployment --replicas=4
```

خروجی مشابه زیر است:

```
deployment.apps/nginx-deployment scaled
```

بررسی کنید که این Deployment چهار Pod دارد:

```shell
kubectl get deployment nginx-deployment
```

خروجی مشابه زیر است:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   4/4     4            4           1m
```

### مقیاس‌دهی اعلانی با استفاده از `kubectl apply`

به‌جای اجرای یک فرمان دستوری (imperative)، می‌توانید فایل مانیفست را به‌روزرسانی
و آن را اعمال کنید. این روش به‌خوبی با گردش‌کارهایی سازگار است که پیکربندی را
تحت کنترل نسخه نگه می‌دارند.

پیکربندی فعلی Deployment را در یک فایل محلی ذخیره کنید:

```shell
kubectl get deployment nginx-deployment -o yaml > /tmp/nginx-deployment.yaml
```

فایل `/tmp/nginx-deployment.yaml` را ویرایش کنید و مقدار `.spec.replicas` را به `4` تغییر دهید.

پیش از اعمال، تغییرات محلی خود را با وضعیت کلاستر مقایسه کنید:

```shell
kubectl diff -f /tmp/nginx-deployment.yaml
```

مانیفست ویرایش‌شده را اعمال کنید:

```shell
kubectl apply -f /tmp/nginx-deployment.yaml
```

## کاهش مقیاس یک Deployment

برای کاهش تعداد Podها، مقدار `--replicas` را روی عددی کمتر تنظیم کنید:

```shell
kubectl scale deployment/nginx-deployment --replicas=2
```

کوبرنتیز Podهای اضافی را به‌صورت تدریجی و ایمن (graceful) خاتمه می‌دهد و در این کار
تنظیم `terminationGracePeriodSeconds` هر Pod را رعایت می‌کند.

بررسی کنید که این Deployment دو Pod دارد:

```shell
kubectl get pods -l app=nginx
```

خروجی مشابه زیر است:

```
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-66b6c48dd5-7gl6h   1/1     Running   0          2m
nginx-deployment-66b6c48dd5-v8mkd   1/1     Running   0          2m
```

## رساندن مقیاس به صفر

می‌توانید مقیاس یک Deployment را به صفر برسانید تا بار کاری را بدون حذف خود
Deployment به‌طور موقت متوقف کنید:

```shell
kubectl scale deployment/nginx-deployment --replicas=0
```

بررسی کنید که هیچ Podای در حال اجرا نیست:

```shell
kubectl get deployment nginx-deployment
```

خروجی مشابه زیر است:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   0/0     0            0           5m
```

{{< note >}}
رساندن مقیاس به صفر همهٔ Podها را حذف می‌کند، اما Deployment و ReplicaSet آن
حفظ می‌شوند. هر زمان که بخواهید، می‌توانید با تنظیم `--replicas` روی عددی مثبت،
دوباره مقیاس را افزایش دهید.
{{< /note >}}

کاربردهای رایج رساندن مقیاس به صفر عبارت‌اند از:

- تعلیق موقت یک بار کاری برای صرفه‌جویی در منابع
- بازه‌های زمانی اشکال‌زدایی یا نگهداری
- کنترل هزینه در محیط‌های توسعه یا staging

## روش‌های دیگر برای تغییر تعداد رپلیکاها

علاوه بر `kubectl scale`، می‌توانید مقدار `.spec.replicas` را با
`kubectl edit` یا `kubectl patch` نیز تغییر دهید.

### مقیاس‌دهی با استفاده از `kubectl edit`

```shell
kubectl edit deployment nginx-deployment
```

فیلد `.spec.replicas` را در ویرایشگر تغییر دهید، سپس فایل را ذخیره کنید و از ویرایشگر خارج شوید.

### مقیاس‌دهی با استفاده از `kubectl patch`

می‌توانید مقدار `.spec.replicas` را با یک وصلهٔ ادغام راهبردی (strategic merge patch) به‌روزرسانی کنید:

```shell
kubectl patch deployment nginx-deployment -p '{"spec":{"replicas":4}}'
```

برای استفاده در اسکریپت‌ها، از یک وصلهٔ JSON همراه با یک آزمون پیش‌شرط استفاده کنید. فرمان زیر تعداد رپلیکاها را روی ۴ تنظیم می‌کند، اما فقط در صورتی که تعداد فعلی ۲ باشد:

```shell
kubectl patch deployment nginx-deployment --type=json -p='[
  {"op": "test", "path": "/spec/replicas", "value": 2},
  {"op": "replace", "path": "/spec/replicas", "value": 4}
]'
```

اگر مقدار فعلی مطابقت نداشته باشد، عملیات `test` باعث شکست وصله می‌شود. به این ترتیب، وقتی چند نفر یا چند اسکریپت یک Deployment را تغییر می‌دهند، از تغییرات ناخواسته جلوگیری می‌شود.

## چه زمانی از مقیاس‌دهی دستی و چه زمانی از مقیاس‌دهی خودکار استفاده کنیم

| جنبه | مقیاس‌دهی دستی | مقیاس‌دهی خودکار (HPA) |
|--------|---------------|------------------------|
| مناسب برای | تغییرات بار قابل پیش‌بینی، زمان‌بندی‌شده یا یک‌باره | تقاضای متغیر یا غیرقابل پیش‌بینی |
| نحوهٔ کار | شما مقدار `.spec.replicas` را مستقیماً تنظیم می‌کنید | HPA تعداد رپلیکاها را بر اساس معیارهای مشاهده‌شده تنظیم می‌کند |
| زمان پاسخ | بلافاصله پس از اجرای فرمان | با تأخیری کوتاه به معیارها واکنش نشان می‌دهد |
| آگاهی از معیارها | ندارد؛ تعداد رپلیکاها را شما تعیین می‌کنید | معیارهای CPU، حافظه یا معیارهای سفارشی را پایش می‌کند |
| نگهداری | برای تنظیم، به مداخلهٔ دستی نیاز دارد | پس از پیکربندی، به‌طور خودکار کار می‌کند |

{{< caution >}}
اگر یک HorizontalPodAutoscaler یک Deployment را مدیریت می‌کند، تعداد رپلیکاها را به‌صورت دستی تنظیم نکنید.
HPA به‌طور پیوسته تعداد رپلیکاها را هماهنگ (reconcile) می‌کند و هر تغییر دستی را
بازنویسی می‌کند.
{{< /caution >}}

## {{% heading "cleanup" %}}

Deployment را حذف کنید:

```shell
kubectl delete deployment nginx-deployment
```

## {{% heading "whatsnext" %}}

- دربارهٔ [Deploymentها](/docs/concepts/workloads/controllers/deployment/) بیشتر بیاموزید.
- راهنمای گام‌به‌گام [مقیاس‌دهی خودکار افقی Pod](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) را دنبال کنید.
- با نحوهٔ [مقیاس‌دهی یک StatefulSet](/docs/tasks/run-application/scale-stateful-set/) آشنا شوید.
- دربارهٔ [مدیریت منابع](/docs/concepts/cluster-administration/manage-deployment/) مطالعه کنید.
