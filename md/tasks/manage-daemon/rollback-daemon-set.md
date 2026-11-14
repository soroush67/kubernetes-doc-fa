---
reviewers:
- janetkuo
title: انجام بازگردانی (Rollback) روی یک DaemonSet
content_type: task
weight: 20
min-kubernetes-server-version: 1.7
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک {{< glossary_tooltip term_id="daemonset" >}} را به نسخه‌ای قبلی بازگردانید.


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

پیش از این باید با نحوهٔ [انجام به‌روزرسانی تدریجی (rolling update) روی یک
 DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/) آشنا باشید.

<!-- steps -->

## انجام بازگردانی روی یک DaemonSet

### گام ۱: یافتن بازبینی (revision) موردنظر DaemonSet برای بازگشت

اگر فقط می‌خواهید به آخرین بازبینی بازگردید، می‌توانید از این گام صرف‌نظر کنید.

همهٔ بازبینی‌های یک DaemonSet را فهرست کنید:

```shell
kubectl rollout history daemonset <daemonset-name>
```

خروجی این فرمان فهرستی از بازبینی‌های DaemonSet است:

```
daemonsets "<daemonset-name>"
REVISION        CHANGE-CAUSE
1               ...
2               ...
...
```

* علت تغییر (change cause) هنگام ایجاد هر بازبینی، از حاشیه‌نویسی (annotation)
  `kubernetes.io/change-cause` در DaemonSet به آن بازبینی کپی می‌شود. می‌توانید
  با مشخص‌کردن `--record=true` در `kubectl`، فرمان اجراشده را در حاشیه‌نویسی علت تغییر ثبت کنید.

برای دیدن جزئیات یک بازبینی مشخص:

```shell
kubectl rollout history daemonset <daemonset-name> --revision=1
```

خروجی این فرمان جزئیات همان بازبینی است:

```
daemonsets "<daemonset-name>" with revision #1
Pod Template:
Labels:       foo=bar
Containers:
app:
 Image:        ...
 Port:         ...
 Environment:  ...
 Mounts:       ...
Volumes:      ...
```

### گام ۲: بازگشت به یک بازبینی مشخص

```shell
# Specify the revision number you get from Step 1 in --to-revision
kubectl rollout undo daemonset <daemonset-name> --to-revision=<revision>
```

در صورت موفقیت، فرمان خروجی زیر را برمی‌گرداند:

```
daemonset "<daemonset-name>" rolled back
```

{{< note >}}
اگر فلگ `--to-revision` مشخص نشود، kubectl جدیدترین بازبینی را انتخاب می‌کند.
{{< /note >}}

### گام ۳: پیگیری پیشرفت بازگردانی DaemonSet

فرمان `kubectl rollout undo daemonset` به سرور اعلام می‌کند که بازگردانی DaemonSet
را آغاز کند. بازگردانی واقعی به‌صورت ناهمگام درون
{{< glossary_tooltip term_id="control-plane" text="control plane" >}} کلاستر انجام می‌شود.

برای پیگیری پیشرفت بازگردانی:

```shell
kubectl rollout status ds/<daemonset-name>
```

پس از تکمیل بازگردانی، خروجی مشابه زیر است:

```
daemonset "<daemonset-name>" successfully rolled out
```


<!-- discussion -->

## آشنایی با بازبینی‌های DaemonSet

در گام قبلی، با فرمان `kubectl rollout history` فهرستی از بازبینی‌های DaemonSet
به دست آوردید. هر بازبینی در منبعی به نام ControllerRevision ذخیره می‌شود.

برای اینکه ببینید در هر بازبینی چه چیزی ذخیره شده است، منابع خام بازبینی‌های
DaemonSet را پیدا کنید:

```shell
kubectl get controllerrevision -l <daemonset-selector-key>=<daemonset-selector-value>
```

خروجی این فرمان فهرستی از ControllerRevisionها است:

```
NAME                               CONTROLLER                     REVISION   AGE
<daemonset-name>-<revision-hash>   DaemonSet/<daemonset-name>     1          1h
<daemonset-name>-<revision-hash>   DaemonSet/<daemonset-name>     2          1h
```

هر ControllerRevision حاشیه‌نویسی‌ها و قالب (template) یک بازبینی DaemonSet را
ذخیره می‌کند.

فرمان `kubectl rollout undo` یک ControllerRevision مشخص را برمی‌دارد و قالب
DaemonSet را با قالب ذخیره‌شده در آن ControllerRevision جایگزین می‌کند.
کارکرد `kubectl rollout undo` معادل به‌روزرسانی قالب DaemonSet به یک بازبینی
قبلی از طریق فرمان‌های دیگر، مانند `kubectl edit` یا `kubectl apply`، است.

{{< note >}}
بازبینی‌های DaemonSet فقط رو به جلو حرکت می‌کنند. به بیان دیگر، پس از تکمیل
بازگردانی، شمارهٔ بازبینی (فیلد `.revision`) آن ControllerRevision که به آن
بازگشته‌اید افزایش می‌یابد. برای مثال، اگر بازبینی‌های ۱ و ۲ در سیستم موجود باشند
و از بازبینی ۲ به بازبینی ۱ بازگردید، ControllerRevision با `.revision: 1` به
`.revision: 3` تبدیل می‌شود.
{{< /note >}}

## عیب‌یابی

* به [عیب‌یابی به‌روزرسانی تدریجی
  DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/#troubleshooting) مراجعه کنید.
