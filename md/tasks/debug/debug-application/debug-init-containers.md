---
reviewers:
- bprashanth
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: اشکال‌زدایی کانتینرهای Init
content_type: task
weight: 40
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان مشکلات مربوط به اجرای کانتینرهای Init را بررسی کرد. در خط‌فرمان‌های نمونهٔ زیر، Pod با نام `<pod-name>` و کانتینرهای Init با نام‌های `<init-container-1>` و `<init-container-2>` مشخص شده‌اند.

## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* باید با مفاهیم پایهٔ [کانتینرهای Init](/docs/concepts/workloads/pods/init-containers/) آشنا باشید.
* باید پیش‌تر [یک کانتینر Init را پیکربندی کرده باشید](/docs/tasks/configure-pod-container/configure-pod-initialization/#create-a-pod-that-has-an-init-container).

<!-- steps -->

## بررسی وضعیت کانتینرهای Init

وضعیت Pod خود را نمایش دهید:

```shell
kubectl get pod <pod-name>
```

برای نمونه، وضعیت `Init:1/2` نشان می‌دهد که یکی از دو کانتینر Init با موفقیت به پایان رسیده است:

```
NAME         READY     STATUS     RESTARTS   AGE
<pod-name>   0/1       Init:1/2   0          7s
```

برای دیدن نمونه‌های بیشتری از مقادیر وضعیت و معنای آن‌ها، بخش [درک وضعیت Pod](#understanding-pod-status) را ببینید.

## دریافت جزئیات کانتینرهای Init

اطلاعات دقیق‌تری دربارهٔ اجرای کانتینرهای Init مشاهده کنید:

```shell
kubectl describe pod <pod-name>
```

برای نمونه، خروجی این فرمان برای یک Pod با دو کانتینر Init ممکن است به شکل زیر باشد:

```
Init Containers:
  <init-container-1>:
    Container ID:    ...
    ...
    State:           Terminated
      Reason:        Completed
      Exit Code:     0
      Started:       ...
      Finished:      ...
    Ready:           True
    Restart Count:   0
    ...
  <init-container-2>:
    Container ID:    ...
    ...
    State:           Waiting
      Reason:        CrashLoopBackOff
    Last State:      Terminated
      Reason:        Error
      Exit Code:     1
      Started:       ...
      Finished:      ...
    Ready:           False
    Restart Count:   3
    ...
```

همچنین می‌توانید با خواندن فیلد `status.initContainerStatuses` در مشخصات Pod، به‌صورت برنامه‌نویسی‌شده به وضعیت کانتینرهای Init دسترسی پیدا کنید:


```shell
kubectl get pod <pod-name> --template '{{.status.initContainerStatuses}}'
```


این فرمان همان اطلاعات بالا را برمی‌گرداند که با یک [قالب Go](https://pkg.go.dev/text/template) قالب‌بندی شده است.

## دسترسی به لاگ‌های کانتینرهای Init

برای دسترسی به لاگ‌های یک کانتینر Init، نام آن را همراه با نام Pod به فرمان بدهید.

```shell
kubectl logs <pod-name> -c <init-container-2>
```

کانتینرهای Init که یک اسکریپت پوسته (shell) اجرا می‌کنند، فرمان‌ها را هنگام اجرا چاپ می‌کنند. برای نمونه، در Bash می‌توانید این کار را با اجرای `set -x` در ابتدای اسکریپت انجام دهید.



<!-- discussion -->

## درک وضعیت Pod

هر وضعیت Pod که با `Init:` آغاز شود، خلاصه‌ای از وضعیت اجرای کانتینرهای Init را نشان می‌دهد. جدول زیر برخی از مقادیر نمونهٔ وضعیت را که ممکن است هنگام اشکال‌زدایی کانتینرهای Init ببینید، شرح می‌دهد.

وضعیت | معنا
------ | -------
`Init:N/M` | این Pod دارای `M` کانتینر Init است و تاکنون `N` کانتینر از آن‌ها به پایان رسیده‌اند.
`Init:Error` | اجرای یکی از کانتینرهای Init با شکست مواجه شده است.
`Init:CrashLoopBackOff` | یکی از کانتینرهای Init به‌طور مکرر با شکست مواجه شده است.
`Pending` | این Pod هنوز اجرای کانتینرهای Init را آغاز نکرده است.
`PodInitializing` یا `Running` | این Pod اجرای کانتینرهای Init را به پایان رسانده است.
