---
title: به‌روزرسانی یک Deployment بدون قطعی
content_type: task
weight: 16
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید یک Deployment در حال اجرا را با استفاده از
به‌روزرسانی تدریجی (rolling update) به نسخهٔ جدیدی ارتقا دهید. در به‌روزرسانی تدریجی،
Podهای قدیمی به‌تدریج با Podهای جدید جایگزین می‌شوند و به این ترتیب برنامهٔ شما در
سراسر این فرایند در دسترس می‌ماند.

## {{% heading "objectives" %}}

- راه‌اندازی یک به‌روزرسانی تدریجی روی یک Deployment.
- پایش پیشرفت عرضه (rollout).
- توقف موقت و ازسرگیری عرضه.
- پیکربندی پارامترهای راهبرد به‌روزرسانی تدریجی.
- (در صورت نیاز) بازگشت به یک بازبینی (revision) قبلی.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

به یک Deployment موجود نیاز دارید. اگر Deployment ندارید، Deployment مربوط به nginx
را طبق صفحهٔ
[اجرای یک برنامهٔ بی‌حالت با استفاده از Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
ایجاد کنید:

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

## انجام به‌روزرسانی تدریجی

هر تغییری در فیلد `.spec.template` یک Deployment، یک به‌روزرسانی تدریجی را آغاز
می‌کند. کوبرنتیز Podهای جدیدی با پیکربندی به‌روزشده ایجاد می‌کند و Podهای قدیمی را
به‌تدریج خاتمه می‌دهد.

### به‌روزرسانی با `kubectl apply`

می‌توانید با ویرایش مانیفست Deployment و اعمال تغییر، یک به‌روزرسانی تدریجی را آغاز کنید. این روش زمانی مناسب است که مانیفست‌ها را در سامانهٔ کنترل نسخه نگه می‌دارید.

ابتدا Deployment فعلی را در یک فایل محلی ذخیره کنید:

```shell
kubectl get deployment nginx-deployment -o yaml > /tmp/nginx-deployment.yaml
```

فایل `/tmp/nginx-deployment.yaml` را ویرایش کنید و مقدار `.spec.template.spec.containers[0].image`
را از `nginx:1.14.2` به `nginx:1.16.1` تغییر دهید.

پیش از اعمال، تغییرات محلی خود را با وضعیت کلاستر مقایسه کنید:

```shell
kubectl diff -f /tmp/nginx-deployment.yaml
```

خروجی مشابه زیر است:

```
diff -u -N /tmp/LIVE/apps.v1.Deployment.default.nginx-deployment /tmp/MERGED/apps.v1.Deployment.default.nginx-deployment
--- /tmp/LIVE/apps.v1.Deployment...
+++ /tmp/MERGED/apps.v1.Deployment...
@@ -29,7 +29,7 @@
       containers:
-      - image: nginx:1.14.2
+      - image: nginx:1.16.1
         name: nginx
```

مانیفست به‌روزشده را اعمال کنید:

```shell
kubectl apply -f /tmp/nginx-deployment.yaml
```

### به‌روزرسانی فقط ایمیج کانتینر

برای به‌روزرسانی ایمیج کانتینر بدون ویرایش فایل مانیفست، از
`kubectl set image` استفاده کنید:

```shell
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
```

خروجی مشابه زیر است:

```
deployment.apps/nginx-deployment image updated
```

بررسی کنید که ایمیج به‌روز شده باشد:

```shell
kubectl get deployment nginx-deployment -o jsonpath='{.spec.template.spec.containers[0].image}'
```

خروجی مشابه زیر است:

```
nginx:1.16.1
```

## پایش پیشرفت عرضه

برای مشاهدهٔ پیشرفت یک به‌روزرسانی تدریجی، از `kubectl rollout status` استفاده کنید:

```shell
kubectl rollout status deployment/nginx-deployment
```

خروجی مشابه زیر است:

```
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
deployment "nginx-deployment" successfully rolled out
```

پس از پایان عرضه، وضعیت Deployment را بررسی کنید:

```shell
kubectl get deployment nginx-deployment
```

خروجی مشابه زیر است:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           2m
```

## توقف موقت و ازسرگیری عرضه

می‌توانید یک عرضه را موقتاً متوقف کنید تا یک به‌روزرسانی نیمه‌کاره را بررسی کنید یا
چند تغییر را در قالب یک عرضهٔ واحد اعمال کنید.

### توقف موقت عرضه

```shell
kubectl rollout pause deployment/nginx-deployment
```

خروجی مشابه زیر است:

```
deployment.apps/nginx-deployment paused
```

### اعمال تغییرات بیشتر در حالت توقف

در مدتی که عرضه متوقف است، می‌توانید تغییرات دیگری نیز اعمال کنید. این تغییرات تا
زمانی که عرضه را از سر نگیرید، عرضهٔ جدیدی را آغاز نمی‌کنند:

```shell
kubectl set image deployment/nginx-deployment nginx=nginx:1.17.0
```

{{< note >}}
می‌توانید چندین تغییر را روی یک Deployment متوقف‌شده اعمال کنید. کوبرنتیز هنگام
ازسرگیری عرضه، همهٔ این تغییرات را با هم اعمال می‌کند.
{{< /note >}}

### ازسرگیری عرضه

```shell
kubectl rollout resume deployment/nginx-deployment
```

خروجی مشابه زیر است:

```
deployment.apps/nginx-deployment resumed
```

بررسی کنید که عرضه به پایان برسد:

```shell
kubectl rollout status deployment/nginx-deployment
```

## پیکربندی راهبرد به‌روزرسانی تدریجی

منابع Deployment از دو
[نوع راهبرد به‌روزرسانی](/docs/concepts/workloads/controllers/deployment/#strategy)
پشتیبانی می‌کنند:

- راهبرد **RollingUpdate** (پیش‌فرض): Podهای قدیمی را به‌تدریج با Podهای جدید جایگزین می‌کند.
- راهبرد **Recreate**: پیش از ایجاد Podهای جدید، همهٔ Podهای موجود را خاتمه می‌دهد.
  این کار باعث قطعی می‌شود.

در راهبرد RollingUpdate، پارامترهای زیر نحوهٔ انجام به‌روزرسانی را در کوبرنتیز کنترل می‌کنند:

| پارامتر | مورد کنترل | پیش‌فرض | مثال |
|-----------|----------|---------|---------|
| `maxUnavailable` | حداکثر تعداد Podهایی که در طول به‌روزرسانی می‌توانند در دسترس نباشند | 25% | `1` یا `25%` |
| `maxSurge` | حداکثر تعداد Podهای اضافی که در طول به‌روزرسانی می‌توانند ایجاد شوند | 25% | `1` یا `25%` |

{{< note >}}
فیلدهای `maxUnavailable` و `maxSurge` یک عدد مطلق یا یک درصد را می‌پذیرند.
کوبرنتیز درصدها را بر اساس تعداد رونوشت‌های مطلوب محاسبه می‌کند و نتیجه را برای
`maxUnavailable` به پایین و برای `maxSurge` به بالا گرد می‌کند.
{{< /note >}}

برای پیکربندی این پارامترها، از `kubectl patch` استفاده کنید:

```shell
kubectl patch deployment nginx-deployment -p \
  '{"spec":{"strategy":{"rollingUpdate":{"maxUnavailable":"25%","maxSurge":"25%"}}}}'
```

همچنین می‌توانید این فیلدها را در مانیفست Deployment و زیر
`.spec.strategy.rollingUpdate` تنظیم کنید. برای مثال‌های تفصیلی، بخش‌های
[max unavailable](/docs/concepts/workloads/controllers/deployment/#max-unavailable)
و [max surge](/docs/concepts/workloads/controllers/deployment/#max-surge)
را در مستندات مفهومی Deployment ببینید.

### تشخیص عرضهٔ متوقف‌مانده

اگر یک عرضه در مدت زمانی که با `.spec.progressDeadlineSeconds` (پیش‌فرض: ۶۰۰ ثانیه) تعیین شده است پیشرفتی نداشته باشد، کوبرنتیز وضعیت `Progressing` آن Deployment را `False` اعلام می‌کند. برای بررسی این وضعیت، Deployment را توصیف کنید:

```shell
kubectl describe deployment nginx-deployment
```

در بخش `Conditions` خروجی، به دنبال وضعیت `Progressing` بگردید. متوقف‌ماندن عرضه معمولاً نشان می‌دهد که Podهای جدید نمی‌توانند راه‌اندازی شوند. بخش `Events` خروجی می‌تواند به تشخیص مشکل کمک کند.

## بازگشت به یک بازبینی قبلی {#rollback}

اگر نسخهٔ جدید مشکلاتی ایجاد کند، می‌توانید به یک بازبینی قبلی بازگردید.

### مشاهدهٔ تاریخچهٔ عرضه

```shell
kubectl rollout history deployment/nginx-deployment
```

خروجی مشابه زیر است:

```
deployment.apps/nginx-deployment
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

{{< note >}}
ستون `CHANGE-CAUSE` مقدار حاشیه‌نویسی (annotation) `kubernetes.io/change-cause`
را در زمان ایجاد هر بازبینی نشان می‌دهد. این حاشیه‌نویسی به‌طور خودکار تنظیم **نمی‌شود**،
اما اگر از یک راهکار خودکار برای مدیریت Deploymentها استفاده می‌کنید، ممکن است ابزار
مورد استفادهٔ شما متنی را در این حاشیه‌نویسی بنویسد.
{{< /note >}}

### بازگشت به بازبینی قبلی

```shell
kubectl rollout undo deployment/nginx-deployment
```

خروجی مشابه زیر است:

```
deployment.apps/nginx-deployment rolled back
```

### بازگشت به یک بازبینی مشخص

```shell
kubectl rollout undo deployment/nginx-deployment --to-revision=1
```

بررسی کنید که بازگشت به پایان برسد:

```shell
kubectl rollout status deployment/nginx-deployment
```

{{< note >}}
تاریخچهٔ بازبینی‌های هر Deployment در ReplicaSetهایی که آن Deployment کنترل می‌کند ذخیره می‌شود.
کوبرنتیز به‌طور پیش‌فرض ۱۰ ReplicaSet قدیمی را نگه می‌دارد. می‌توانید این محدودیت را
با تنظیم `.spec.revisionHistoryLimit` در مانیفست Deployment تغییر دهید. تنظیم این مقدار روی `0` امکان بازگشت را به‌کلی غیرفعال می‌کند.
{{< /note >}}

## {{% heading "cleanup" %}}

Deployment را حذف کنید:

```shell
kubectl delete deployment nginx-deployment
```

## {{% heading "whatsnext" %}}

- دربارهٔ [Deploymentها](/docs/concepts/workloads/controllers/deployment/) بیشتر بیاموزید.
- با نحوهٔ [مقیاس‌دهی دستی یک Deployment](/docs/tasks/run-application/scale-deployment/) آشنا شوید.
- راهنمای گام‌به‌گام [مقیاس‌دهی خودکار افقی Pod](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) را دنبال کنید.
- ببینید چگونه می‌توان [یک به‌روزرسانی تدریجی را روی یک DaemonSet انجام داد](/docs/tasks/manage-daemon/update-daemon-set/).
