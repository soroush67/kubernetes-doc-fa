---
title: اعلام منابع توسعه‌یافته برای یک نود
content_type: task
weight: 70
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان منابع توسعه‌یافته (extended resources) را برای یک نود مشخص کرد.
با منابع توسعه‌یافته، مدیران کلاستر می‌توانند منابعی در سطح نود را اعلام کنند که در غیر این صورت
برای کوبرنتیز ناشناخته می‌ماندند.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

## دریافت نام نودها

```shell
kubectl get nodes
```

یکی از نودهای خود را برای این تمرین انتخاب کنید.

## اعلام یک منبع توسعه‌یافتهٔ جدید روی یکی از نودها

برای اعلام یک منبع توسعه‌یافتهٔ جدید روی یک نود، یک درخواست HTTP PATCH به
سرور API کوبرنتیز بفرستید. برای مثال، فرض کنید به یکی از نودهای شما چهار دانگل (dongle)
متصل است. در ادامه نمونه‌ای از یک درخواست PATCH آمده است که چهار منبع دانگل را
برای نود شما اعلام می‌کند.

```
PATCH /api/v1/nodes/<your-node-name>/status HTTP/1.1
Accept: application/json
Content-Type: application/json-patch+json
Host: k8s-master:8080

[
  {
    "op": "add",
    "path": "/status/capacity/example.com~1dongle",
    "value": "4"
  }
]
```

توجه کنید که کوبرنتیز نیازی ندارد بداند دانگل چیست یا چه کاربردی دارد.
درخواست PATCH بالا فقط به کوبرنتیز اعلام می‌کند که نود شما چهار چیز دارد که
شما آن‌ها را دانگل می‌نامید.

یک پراکسی راه‌اندازی کنید تا بتوانید به‌سادگی درخواست‌ها را به سرور API کوبرنتیز بفرستید:

```shell
kubectl proxy
```

در یک پنجرهٔ فرمان دیگر، درخواست HTTP PATCH را بفرستید.
به‌جای `<your-node-name>` نام نود خود را قرار دهید:

```shell
curl --header "Content-Type: application/json-patch+json" \
  --request PATCH \
  --data '[{"op": "add", "path": "/status/capacity/example.com~1dongle", "value": "4"}]' \
  http://localhost:8001/api/v1/nodes/<your-node-name>/status
```

{{< note >}}
در درخواست بالا، `~1` کدگذاری نویسهٔ / در مسیر patch است. مقدار مسیر عملیات
در JSON-Patch به‌صورت یک JSON-Pointer تفسیر می‌شود. برای جزئیات بیشتر، بخش ۳ از
[IETF RFC 6901](https://tools.ietf.org/html/rfc6901) را ببینید.
{{< /note >}}

خروجی نشان می‌دهد که ظرفیت نود ۴ دانگل است:

```
"capacity": {
  "cpu": "2",
  "memory": "2049008Ki",
  "example.com/dongle": "4",
```

نود خود را توصیف کنید:

```
kubectl describe node <your-node-name>
```

این بار نیز خروجی، منبع دانگل را نشان می‌دهد:

```yaml
Capacity:
  cpu: 2
  memory: 2049008Ki
  example.com/dongle: 4
```

اکنون توسعه‌دهندگان برنامه می‌توانند Podهایی بسازند که تعداد مشخصی دانگل
درخواست کنند. برای اطلاعات بیشتر،
[تخصیص منابع توسعه‌یافته به یک کانتینر](/docs/tasks/configure-pod-container/extended-resource/) را ببینید.

## بحث

منابع توسعه‌یافته شبیه منابع حافظه و CPU هستند. برای مثال،
همان‌طور که یک نود مقدار مشخصی حافظه و CPU دارد که میان همهٔ مؤلفه‌های
در حال اجرا روی آن نود به اشتراک گذاشته می‌شود، می‌تواند تعداد مشخصی دانگل نیز داشته باشد
که میان همهٔ مؤلفه‌های در حال اجرا روی آن نود به اشتراک گذاشته می‌شود. و همان‌طور که توسعه‌دهندگان برنامه
می‌توانند Podهایی بسازند که مقدار مشخصی حافظه و CPU درخواست کنند،
می‌توانند Podهایی نیز بسازند که تعداد مشخصی دانگل درخواست کنند.

منابع توسعه‌یافته برای کوبرنتیز مبهم (opaque) هستند و کوبرنتیز هیچ اطلاعی
از ماهیت آن‌ها ندارد. کوبرنتیز فقط می‌داند که یک نود تعداد مشخصی از
آن‌ها را دارد. منابع توسعه‌یافته باید به‌صورت مقادیر صحیح اعلام شوند.
برای مثال، یک نود می‌تواند چهار دانگل اعلام کند، اما نمی‌تواند ۴٫۵ دانگل اعلام کند.

### مثال ذخیره‌سازی

فرض کنید یک نود ۸۰۰ GiB از نوع خاصی ذخیره‌سازی دیسک دارد. می‌توانید
برای این ذخیره‌سازی خاص نامی تعریف کنید، مثلاً example.com/special-storage.
سپس می‌توانید آن را در بخش‌هایی با اندازهٔ مشخص، مثلاً ۱۰۰ GiB، اعلام کنید. در این صورت،
نود شما اعلام می‌کند که هشت منبع از نوع
example.com/special-storage دارد.

```yaml
Capacity:
 ...
 example.com/special-storage: 8
```

اگر می‌خواهید درخواست‌هایی با اندازهٔ دلخواه برای ذخیره‌سازی خاص امکان‌پذیر باشد،
می‌توانید ذخیره‌سازی خاص را در بخش‌هایی به اندازهٔ ۱ بایت اعلام کنید. در این صورت،
800Gi منبع از نوع example.com/special-storage اعلام خواهید کرد.

```yaml
Capacity:
 ...
 example.com/special-storage:  800Gi
```

سپس یک کانتینر می‌تواند هر تعداد بایت از ذخیره‌سازی خاص را، تا سقف 800Gi، درخواست کند.

## پاک‌سازی

در ادامه یک درخواست PATCH آمده است که اعلام دانگل را از یک نود حذف می‌کند.

```
PATCH /api/v1/nodes/<your-node-name>/status HTTP/1.1
Accept: application/json
Content-Type: application/json-patch+json
Host: k8s-master:8080

[
  {
    "op": "remove",
    "path": "/status/capacity/example.com~1dongle",
  }
]
```

یک پراکسی راه‌اندازی کنید تا بتوانید به‌سادگی درخواست‌ها را به سرور API کوبرنتیز بفرستید:

```shell
kubectl proxy
```

در یک پنجرهٔ فرمان دیگر، درخواست HTTP PATCH را بفرستید.
به‌جای `<your-node-name>` نام نود خود را قرار دهید:

```shell
curl --header "Content-Type: application/json-patch+json" \
  --request PATCH \
  --data '[{"op": "remove", "path": "/status/capacity/example.com~1dongle"}]' \
  http://localhost:8001/api/v1/nodes/<your-node-name>/status
```

بررسی کنید که اعلام دانگل حذف شده باشد:

```
kubectl describe node <your-node-name> | grep dongle
```

(نباید هیچ خروجی‌ای ببینید)

## {{% heading "whatsnext" %}}

### برای توسعه‌دهندگان برنامه

- [تخصیص منابع توسعه‌یافته به یک کانتینر](/docs/tasks/configure-pod-container/extended-resource/)
- [تخصیص منابع توسعه‌یافته با DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#extended-resource)

### برای مدیران کلاستر

- [پیکربندی محدودیت‌های حداقل و حداکثر حافظه برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
- [پیکربندی محدودیت‌های حداقل و حداکثر CPU برای یک فضای نام](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
- [تخصیص منابع توسعه‌یافته با DRA](/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#extended-resource)
