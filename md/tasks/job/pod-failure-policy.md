---
title: مدیریت خرابی‌های قابل تلاش مجدد و غیرقابل تلاش مجدد پادها با سیاست خرابی Pod
content_type: task
min-kubernetes-server-version: v1.25
weight: 60
---

{{< feature-state feature_gate_name="JobPodFailurePolicy" >}}

<!-- overview -->

این سند نشان می‌دهد چگونه می‌توانید از
[سیاست خرابی Pod](/docs/concepts/workloads/controllers/job#pod-failure-policy)
در کنار
[سیاست خرابی عقب‌نشینی Pod](/docs/concepts/workloads/controllers/job#pod-backoff-failure-policy)
پیش‌فرض استفاده کنید تا کنترل بهتری بر نحوهٔ رسیدگی به خرابی‌های سطح کانتینر یا سطح Pod
در یک {{<glossary_tooltip text="Job" term_id="job">}} داشته باشید.

تعریف سیاست خرابی Pod می‌تواند به شما کمک کند تا:
* با پرهیز از تلاش‌های مجدد غیرضروری Pod، از منابع محاسباتی بهتر استفاده کنید.
* از شکست Job به دلیل اختلال‌های Pod (مانند {{<glossary_tooltip text="پیش‌دستی (preemption)" term_id="preemption" >}}،
{{<glossary_tooltip text="بیرون‌رانی آغازشده از طریق API" term_id="api-eviction" >}}
یا بیرون‌رانی مبتنی بر {{<glossary_tooltip text="taint" term_id="taint" >}}) جلوگیری کنید.

## {{% heading "prerequisites" %}}

باید از پیش با کاربرد پایهٔ [Job](/docs/concepts/workloads/controllers/job/) آشنا باشید.

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

## سناریوهای کاربرد

سناریوهای کاربرد زیر را برای Jobهایی که سیاست خرابی Pod تعریف می‌کنند در نظر بگیرید:
- [پرهیز از تلاش‌های مجدد غیرضروری Pod](#pod-failure-policy-failjob)
- [نادیده گرفتن اختلال‌های Pod](#pod-failure-policy-ignore)
- [پرهیز از تلاش‌های مجدد غیرضروری Pod بر اساس وضعیت‌های سفارشی Pod](#pod-failure-policy-config-issue)
- [پرهیز از تلاش‌های مجدد غیرضروری Pod به ازای هر اندیس](#backoff-limit-per-index-failindex)

### استفاده از سیاست خرابی Pod برای پرهیز از تلاش‌های مجدد غیرضروری Pod {#pod-failure-policy-failjob}

با مثال زیر می‌توانید یاد بگیرید که چگونه از سیاست خرابی Pod استفاده کنید تا
وقتی خرابی یک Pod نشان‌دهندهٔ یک باگ نرم‌افزاری غیرقابل تلاش مجدد است، از راه‌اندازی‌های
مجدد غیرضروری Pod جلوگیری شود.

1. مانیفست زیر را بررسی کنید:

   {{% code_sample file="/controllers/job-pod-failure-policy-failjob.yaml" %}}

1. مانیفست را اعمال کنید:

   ```sh
   kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-failjob.yaml
   ```

1. پس از حدود ۳۰ ثانیه، کل Job باید خاتمه یافته باشد. وضعیت Job را با اجرای دستور زیر بررسی کنید:

   ```sh
   kubectl get jobs -l job-name=job-pod-failure-policy-failjob -o yaml
   ```

   در وضعیت Job، شرایط (condition) زیر نمایش داده می‌شوند:
   - شرط `FailureTarget`: فیلد `reason` آن روی `PodFailurePolicy` تنظیم شده است و
     فیلد `message` آن اطلاعات بیشتری دربارهٔ خاتمه دارد، مانند
     `Container main for pod default/job-pod-failure-policy-failjob-8ckj8 failed with exit code 42 matching FailJob rule at index 0`.
     کنترل‌کنندهٔ Job این شرط را به محض اینکه Job شکست‌خورده تلقی شود اضافه می‌کند.
     برای جزئیات، [خاتمهٔ Podهای Job](/docs/concepts/workloads/controllers/job/#termination-of-job-pods) را ببینید.
   - شرط `Failed`: همان `reason` و `message` شرط `FailureTarget` را دارد.
     کنترل‌کنندهٔ Job این شرط را پس از خاتمهٔ همهٔ Podهای Job اضافه می‌کند.

   برای مقایسه، اگر سیاست خرابی Pod غیرفعال بود، Job تا رسیدن به `backoffLimit`
   (۶ خرابی) دوباره تلاش می‌کرد. از آنجا که تلاش‌های مجدد از عقب‌نشینی نمایی
   (exponential backoff) استفاده می‌کنند و با `parallelism: 2` خرابی‌ها به‌صورت جفتی رخ
   می‌دهند، فاصلهٔ بین تلاش‌ها با هر تلاش مجدد افزایش می‌یابد. در نتیجه، در این مثال
   دست‌کم ۹ دقیقه طول می‌کشید تا Job شکست بخورد.

#### پاک‌سازی

Job ایجادشده را حذف کنید:

```sh
kubectl delete jobs/job-pod-failure-policy-failjob
```

کلاستر به‌طور خودکار Podها را پاک‌سازی می‌کند.

### استفاده از سیاست خرابی Pod برای نادیده گرفتن اختلال‌های Pod {#pod-failure-policy-ignore}

با مثال زیر می‌توانید یاد بگیرید که چگونه از سیاست خرابی Pod استفاده کنید تا
اختلال‌های Pod باعث افزایش شمارندهٔ تلاش مجدد Pod به سمت حد
`.spec.backoffLimit` نشوند.

{{< caution >}}
زمان‌بندی در این مثال اهمیت دارد، پس بهتر است پیش از اجرا مراحل را بخوانید.
برای ایجاد اختلال در Pod، مهم است که نود را در حالی تخلیه (drain) کنید که Pod روی آن
در حال اجراست (ظرف ۹۰ ثانیه پس از زمان‌بندی Pod).
{{< /caution >}}

1. مانیفست زیر را بررسی کنید:

   {{% code_sample file="/controllers/job-pod-failure-policy-ignore.yaml" %}}

1. مانیفست را اعمال کنید:

   ```sh
   kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-ignore.yaml
   ```

1. این دستور را اجرا کنید تا `nodeName` نودی که Pod روی آن زمان‌بندی شده است را بیابید:

   ```sh
   nodeName=$(kubectl get pods -l job-name=job-pod-failure-policy-ignore -o jsonpath='{.items[0].spec.nodeName}')
   ```

1. نود را تخلیه کنید تا Pod پیش از تکمیل شدن (ظرف ۹۰ ثانیه) بیرون رانده شود:

   ```sh
   kubectl drain nodes/$nodeName --ignore-daemonsets --grace-period=0
   ```

1. فیلد `.status.failed` را بررسی کنید تا مطمئن شوید شمارندهٔ Job افزایش نیافته است:

   ```sh
   kubectl get jobs -l job-name=job-pod-failure-policy-ignore -o yaml
   ```

1. حالت cordon نود را بردارید:

   ```sh
   kubectl uncordon nodes/$nodeName
   ```

اجرای Job از سر گرفته می‌شود و با موفقیت به پایان می‌رسد.

برای مقایسه، اگر سیاست خرابی Pod غیرفعال بود، اختلال Pod به خاتمهٔ کل Job منجر
می‌شد (زیرا `.spec.backoffLimit` روی ۰ تنظیم شده است).

#### پاک‌سازی

Job ایجادشده را حذف کنید:

```sh
kubectl delete jobs/job-pod-failure-policy-ignore
```

کلاستر به‌طور خودکار Podها را پاک‌سازی می‌کند.

### استفاده از سیاست خرابی Pod برای پرهیز از تلاش‌های مجدد غیرضروری Pod بر اساس وضعیت‌های سفارشی Pod {#pod-failure-policy-config-issue}

با مثال زیر می‌توانید یاد بگیرید که چگونه از سیاست خرابی Pod استفاده کنید تا
بر اساس وضعیت‌های سفارشی Pod (Pod Conditions) از راه‌اندازی‌های مجدد غیرضروری Pod جلوگیری شود.

{{< note >}}
مثال زیر از نسخهٔ 1.27 به بعد کار می‌کند، زیرا به انتقال Podهای حذف‌شده در فاز `Pending`
به یک فاز پایانی وابسته است
(ببینید: [فاز Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)).
{{< /note >}}

1. مانیفست زیر را بررسی کنید:

   {{% code_sample file="/controllers/job-pod-failure-policy-config-issue.yaml" %}}

1. مانیفست را اعمال کنید:

   ```sh
   kubectl create -f https://k8s.io/examples/controllers/job-pod-failure-policy-config-issue.yaml
   ```

   توجه کنید که ایمیج به‌اشتباه پیکربندی شده است، زیرا وجود ندارد.

1. وضعیت Podهای Job را با اجرای دستور زیر بررسی کنید:

   ```sh
   kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o yaml
   ```

   خروجی‌ای مشابه این خواهید دید:
   ```yaml
   containerStatuses:
   - image: non-existing-repo/non-existing-image:example
      ...
      state:
      waiting:
         message: Back-off pulling image "non-existing-repo/non-existing-image:example"
         reason: ImagePullBackOff
         ...
   phase: Pending
   ```

   توجه کنید که Pod در فاز `Pending` باقی می‌ماند، زیرا نمی‌تواند ایمیج نادرست
   پیکربندی‌شده را دریافت (pull) کند. این مشکل در اصل می‌تواند گذرا باشد و ایمیج ممکن
   است دریافت شود. اما در این مورد ایمیج وجود ندارد، بنابراین این واقعیت را با یک
   وضعیت سفارشی مشخص می‌کنیم.

1. وضعیت سفارشی را اضافه کنید. ابتدا وصله (patch) را با اجرای دستور زیر آماده کنید:

   ```sh
   cat <<EOF > patch.yaml
   status:
     conditions:
     - type: ConfigIssue
       status: "True"
       reason: "NonExistingImage"
       lastTransitionTime: "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
   EOF
   ```
   سپس با اجرای دستور زیر، یکی از Podهای ایجادشده توسط Job را انتخاب کنید:
   ```
   podName=$(kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o jsonpath='{.items[0].metadata.name}')
   ```

   پس از آن، با اجرای دستور زیر وصله را روی یکی از Podها اعمال کنید:

   ```sh
   kubectl patch pod $podName --subresource=status --patch-file=patch.yaml
   ```

   اگر وصله با موفقیت اعمال شود، پیامی مانند این دریافت خواهید کرد:

   ```sh
   pod/job-pod-failure-policy-config-issue-k6pvp patched
   ```

1. با اجرای دستور زیر Pod را حذف کنید تا به فاز `Failed` منتقل شود:

   ```sh
   kubectl delete pods/$podName
   ```

1. وضعیت Job را با اجرای دستور زیر بررسی کنید:

   ```sh
   kubectl get jobs -l job-name=job-pod-failure-policy-config-issue -o yaml
   ```

   در وضعیت Job، شرط `Failed` را می‌بینید که فیلد `reason` آن برابر با
   `PodFailurePolicy` است. افزون بر این، فیلد `message` اطلاعات دقیق‌تری دربارهٔ
   خاتمهٔ Job دارد، مانند:
   `Pod default/job-pod-failure-policy-config-issue-k6pvp has condition ConfigIssue matching FailJob rule at index 0`.

{{< note >}}
در محیط عملیاتی (production)، مراحل ۳ و ۴ باید با یک کنترل‌کنندهٔ ارائه‌شده از سوی
کاربر خودکار شوند.
{{< /note >}}

#### پاک‌سازی

Job ایجادشده را حذف کنید:

```sh
kubectl delete jobs/job-pod-failure-policy-config-issue
```

کلاستر به‌طور خودکار Podها را پاک‌سازی می‌کند.

### استفاده از سیاست خرابی Pod برای پرهیز از تلاش‌های مجدد غیرضروری Pod به ازای هر اندیس {#backoff-limit-per-index-failindex}

برای جلوگیری از راه‌اندازی‌های مجدد غیرضروری Pod به ازای هر اندیس، می‌توانید از
قابلیت‌های _سیاست خرابی Pod_ و _حد عقب‌نشینی به ازای هر اندیس_ استفاده کنید. این بخش
از صفحه نشان می‌دهد که چگونه این قابلیت‌ها را با هم به کار ببرید.

1. مانیفست زیر را بررسی کنید:

   {{% code_sample file="/controllers/job-backoff-limit-per-index-failindex.yaml" %}}

1. مانیفست را اعمال کنید:

   ```sh
   kubectl create -f https://k8s.io/examples/controllers/job-backoff-limit-per-index-failindex.yaml
   ```

1. پس از حدود ۱۵ ثانیه، وضعیت Podهای Job را بررسی کنید. برای این کار دستور زیر را اجرا کنید:

   ```shell
   kubectl get pods -l job-name=job-backoff-limit-per-index-failindex -o yaml
   ```

   خروجی‌ای مشابه این خواهید دید:

   ```none
   NAME                                            READY   STATUS      RESTARTS   AGE
   job-backoff-limit-per-index-failindex-0-4g4cm   0/1     Error       0          4s
   job-backoff-limit-per-index-failindex-0-fkdzq   0/1     Error       0          15s
   job-backoff-limit-per-index-failindex-1-2bgdj   0/1     Error       0          15s
   job-backoff-limit-per-index-failindex-2-vs6lt   0/1     Completed   0          11s
   job-backoff-limit-per-index-failindex-3-s7s47   0/1     Completed   0          6s
   ```

   توجه کنید که خروجی موارد زیر را نشان می‌دهد:

   * دو Pod اندیس 0 دارند، زیرا حد عقب‌نشینی اجازهٔ یک تلاش مجدد برای این اندیس را
   داده است.
   * فقط یک Pod اندیس 1 دارد، زیرا کد خروج Pod شکست‌خورده با سیاست خرابی Pod دارای
   کنش `FailIndex` مطابقت داشته است.

1. وضعیت Job را با اجرای دستور زیر بررسی کنید:

   ```sh
   kubectl get jobs -l job-name=job-backoff-limit-per-index-failindex -o yaml
   ```

   در وضعیت Job می‌بینید که فیلد `failedIndexes` مقدار "0,1" را نشان می‌دهد، زیرا
   هر دو اندیس شکست خورده‌اند. از آنجا که اندیس 1 دوباره امتحان نشده است، تعداد
   Podهای شکست‌خورده که با فیلد وضعیت "failed" نشان داده می‌شود، برابر با 3 است.

#### پاک‌سازی

Job ایجادشده را حذف کنید:

```sh
kubectl delete jobs/job-backoff-limit-per-index-failindex
```

کلاستر به‌طور خودکار Podها را پاک‌سازی می‌کند.

## جایگزین‌ها

می‌توانید با مشخص کردن فیلد `.spec.backoffLimit` در Job، تنها به
[سیاست خرابی عقب‌نشینی Pod](/docs/concepts/workloads/controllers/job#pod-backoff-failure-policy)
تکیه کنید. با این حال، در بسیاری از موقعیت‌ها یافتن تعادل میان مقداری برای
`.spec.backoffLimit` که به‌قدر کافی کم باشد تا از تلاش‌های مجدد غیرضروری Pod جلوگیری
کند و در عین حال به‌قدر کافی زیاد باشد تا Job بر اثر اختلال‌های Pod خاتمه نیابد،
دشوار است.
