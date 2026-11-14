---
title: ساخت یک DaemonSet پایه
content_type: task
weight: 5
---
<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان یک {{< glossary_tooltip text="DaemonSet" term_id="daemonset" >}}
پایه ساخت که روی هر نود در یک کلاستر کوبرنتیز یک Pod اجرا کند.
در این صفحه یک مورد استفادهٔ ساده بررسی می‌شود: یک فایل از میزبان سوار (mount) می‌شود، محتوای آن به کمک یک
[کانتینر init](/docs/concepts/workloads/pods/init-containers/) در لاگ ثبت می‌شود و از یک کانتینر pause نیز استفاده می‌شود.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

برای نمایش رفتار DaemonSetها، به یک کلاستر کوبرنتیز با دست‌کم دو نود (یک نود control plane و یک نود کارگر)
نیاز دارید.

## تعریف DaemonSet

در این تمرین، یک DaemonSet پایه ساخته می‌شود که تضمین می‌کند یک نسخه از Pod روی هر نود زمان‌بندی شود.
این Pod از یک کانتینر init برای خواندن محتوای `/etc/machine-id` از میزبان و ثبت آن در لاگ استفاده می‌کند،
و کانتینر اصلی آن یک کانتینر `pause` است که Pod را در حال اجرا نگه می‌دارد.

{{% code_sample file="application/basic-daemonset.yaml" %}}

1. یک DaemonSet بر اساس مانیفست (YAML) بسازید:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/basic-daemonset.yaml
   ```

1. پس از اعمال مانیفست، می‌توانید بررسی کنید که DaemonSet روی هر نود کلاستر یک Pod اجرا می‌کند:

   ```shell
   kubectl get pods -o wide
   ```

   خروجی، به‌ازای هر نود یک Pod فهرست می‌کند و مشابه زیر است:

   ```
   NAME                                READY   STATUS    RESTARTS   AGE    IP       NODE
   example-daemonset-xxxxx             1/1     Running   0          5m     x.x.x.x  node-1
   example-daemonset-yyyyy             1/1     Running   0          5m     x.x.x.x  node-2
   ```

1. برای مشاهدهٔ محتوای فایل `/etc/machine-id` که در لاگ ثبت شده است، می‌توانید
   دایرکتوری لاگی را که از میزبان سوار شده است بررسی کنید:

   ```shell
   kubectl exec <pod-name> -- cat /var/log/machine-id.log
   ```

   در این دستور، `<pod-name>` نام یکی از Podهای شماست.

## {{% heading "cleanup" %}}

برای حذف DaemonSet، این دستور را اجرا کنید:

```shell
kubectl delete --cascade=foreground --ignore-not-found --now daemonsets/example-daemonset
```

این مثال سادهٔ DaemonSet اجزای کلیدی مانند کانتینرهای init و حجم‌های (volume) مسیر میزبان (host path) را معرفی می‌کند
که می‌توان آن‌ها را برای موارد استفادهٔ پیشرفته‌تر گسترش داد. برای جزئیات بیشتر به
[DaemonSet](/docs/concepts/workloads/controllers/daemonset/) مراجعه کنید.

## {{% heading "whatsnext" %}}

* [انجام به‌روزرسانی تدریجی (rolling update) روی یک DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/) را ببینید.
* [ساخت یک DaemonSet برای پذیرفتن Podهای موجود یک DaemonSet دیگر](/docs/concepts/workloads/controllers/daemonset/) را ببینید.
