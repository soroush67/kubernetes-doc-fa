---
reviewers:
- bprashanth
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: اشکال‌زدایی یک StatefulSet
content_type: task
weight: 30
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه یک StatefulSet را اشکال‌زدایی کنید.

## {{% heading "prerequisites" %}}

* باید یک کلاستر کوبرنتیز داشته باشید و ابزار خط فرمان kubectl باید برای ارتباط با کلاستر شما پیکربندی شده باشد.
* باید یک StatefulSet در حال اجرا داشته باشید که می‌خواهید آن را بررسی کنید.

<!-- steps -->

## اشکال‌زدایی یک StatefulSet

برای فهرست کردن همهٔ Podهای متعلق به یک StatefulSet که برچسب `app.kubernetes.io/name=MyApp` روی آن‌ها تنظیم شده است، می‌توانید از دستور زیر استفاده کنید:

```shell
kubectl get pods -l app.kubernetes.io/name=MyApp
```

اگر متوجه شدید که هر یک از Podهای فهرست‌شده برای مدتی طولانی در وضعیت `Unknown` یا `Terminating` باقی مانده است، برای آشنایی با نحوهٔ رسیدگی به آن‌ها به صفحهٔ [حذف Podهای StatefulSet](/docs/tasks/run-application/delete-stateful-set/) مراجعه کنید.
برای اشکال‌زدایی تک‌تک Podهای یک StatefulSet می‌توانید از راهنمای [اشکال‌زدایی Podها](/docs/tasks/debug/debug-application/debug-pods/) کمک بگیرید.

## {{% heading "whatsnext" %}}

دربارهٔ [اشکال‌زدایی یک init-container](/docs/tasks/debug/debug-application/debug-init-containers/) بیشتر بیاموزید.
