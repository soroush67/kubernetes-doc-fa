---
title: فهرست‌کردن همهٔ ایمیج‌های کانتینر در حال اجرا در یک کلاستر
content_type: task
weight: 100
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان با kubectl همهٔ ایمیج‌های کانتینر (Container image) مربوط به Podهای در حال اجرا در یک کلاستر را فهرست کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- steps -->

در این تمرین، با استفاده از kubectl همهٔ Podهای در حال اجرا در یک کلاستر را دریافت می‌کنید و خروجی را طوری قالب‌بندی می‌کنید که فهرست کانتینرهای هر Pod از آن استخراج شود.

## فهرست‌کردن همهٔ ایمیج‌های کانتینر در همهٔ فضاهای نام

- همهٔ Podها را در همهٔ فضاهای نام (namespace) با دستور `kubectl get pods --all-namespaces` دریافت کنید.
- با استفاده از `-o jsonpath={.items[*].spec['initContainers', 'containers'][*].image}` خروجی را طوری قالب‌بندی کنید که فقط فهرست نام ایمیج‌های کانتینر را شامل شود. این عبارت فیلد `image` را به‌صورت بازگشتی از JSON بازگردانده‌شده استخراج می‌کند.
  - برای اطلاعات بیشتر دربارهٔ نحوهٔ استفاده از jsonpath، [مرجع jsonpath](/docs/reference/kubectl/jsonpath/) را ببینید.
- خروجی را با ابزارهای استاندارد `tr`، `sort` و `uniq` قالب‌بندی کنید:
  - از `tr` برای جایگزین‌کردن فاصله‌ها با خط جدید استفاده کنید.
  - از `sort` برای مرتب‌سازی نتایج استفاده کنید.
  - از `uniq` برای شمارش تعداد هر ایمیج استفاده کنید.

```shell
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec['initContainers', 'containers'][*].image}" |\
tr -s '[[:space:]]' '\n' |\
sort |\
uniq -c
```
عبارت jsonpath بالا به این صورت تفسیر می‌شود:

- `.items[*]`: برای هر مقدار بازگردانده‌شده
- `.spec`: بخش spec را دریافت کن
- `['initContainers', 'containers'][*]`: برای هر کانتینر
- `.image`: ایمیج را دریافت کن

{{< note >}}
هنگامی که یک Pod را با نامش دریافت می‌کنید، برای مثال با `kubectl get pod nginx`، باید بخش `.items[*]` را از مسیر حذف کنید، زیرا در این حالت به‌جای فهرستی از آیتم‌ها، تنها یک Pod بازگردانده می‌شود.
{{< /note >}}

## فهرست‌کردن ایمیج‌های کانتینر به تفکیک Pod

با استفاده از عملیات `range` می‌توانید روی عناصر به‌صورت جداگانه پیمایش کنید و قالب‌بندی خروجی را دقیق‌تر کنترل کنید.

```shell
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\
sort
```

## فهرست‌کردن ایمیج‌های کانتینر با فیلتر برچسب Pod

برای هدف‌گرفتن فقط Podهایی که با یک برچسب مشخص مطابقت دارند، از فلگ ‎-l استفاده کنید. دستور زیر فقط Podهایی را انتخاب می‌کند که برچسب‌هایشان با `app=nginx` مطابقت دارد.

```shell
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" -l app=nginx
```

## فهرست‌کردن ایمیج‌های کانتینر با فیلتر فضای نام Pod

برای هدف‌گرفتن فقط Podهای یک فضای نام مشخص، از فلگ namespace استفاده کنید. دستور زیر فقط Podهای موجود در فضای نام `kube-system` را انتخاب می‌کند.

```shell
kubectl get pods --namespace kube-system -o jsonpath="{.items[*].spec.containers[*].image}"
```

## فهرست‌کردن ایمیج‌های کانتینر با go-template به‌جای jsonpath

به‌عنوان جایگزینی برای jsonpath، ابزار kubectl از [go-templateها](https://pkg.go.dev/text/template) نیز برای قالب‌بندی خروجی پشتیبانی می‌کند:

```shell
kubectl get pods --all-namespaces -o go-template --template="{{range .items}}{{range .spec.containers}}{{.image}} {{end}}{{end}}"
```

## {{% heading "whatsnext" %}}

### مرجع

* راهنمای مرجع [Jsonpath](/docs/reference/kubectl/jsonpath/)
* راهنمای مرجع [Go template](https://pkg.go.dev/text/template)
