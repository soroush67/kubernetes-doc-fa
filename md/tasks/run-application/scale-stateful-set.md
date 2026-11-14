---
reviewers:
- bprashanth
- enisoc
- erictune
- foxish
- janetkuo
- kow3ns
- smarterclayton
title: مقیاس‌دهی یک StatefulSet
content_type: task
weight: 50
---

<!-- overview -->

این صفحه نحوهٔ مقیاس‌دهی یک StatefulSet را نشان می‌دهد. منظور از مقیاس‌دهی یک StatefulSet،
افزایش یا کاهش تعداد رونوشت‌های (replicas) آن است.

## {{% heading "prerequisites" %}}

- منابع StatefulSet فقط در کوبرنتیز نسخهٔ 1.5 یا بالاتر در دسترس هستند.
  برای بررسی نسخهٔ کوبرنتیز خود، دستور `kubectl version` را اجرا کنید.

- همهٔ برنامه‌های حالت‌مند (stateful) به‌خوبی مقیاس‌پذیر نیستند. اگر مطمئن نیستید که
  باید StatefulSetهای خود را مقیاس‌دهی کنید یا نه، برای اطلاعات بیشتر به [مفاهیم StatefulSet](/docs/concepts/workloads/controllers/statefulset/)
  یا [آموزش StatefulSet](/docs/tutorials/stateful-application/basic-stateful-set/) مراجعه کنید.

- تنها زمانی مقیاس‌دهی را انجام دهید که مطمئن هستید کلاستر برنامهٔ حالت‌مند شما
  کاملاً سالم است.

<!-- steps -->

## مقیاس‌دهی StatefulSetها

### استفاده از kubectl برای مقیاس‌دهی StatefulSetها

ابتدا StatefulSetی را که می‌خواهید مقیاس‌دهی کنید پیدا کنید.

```shell
kubectl get statefulsets <stateful-set-name>
```

تعداد رونوشت‌های StatefulSet خود را تغییر دهید:

```shell
kubectl scale statefulsets <stateful-set-name> --replicas=<new-replicas>
```

### انجام به‌روزرسانی درجا روی StatefulSetها

به‌عنوان راه دیگر، می‌توانید
[به‌روزرسانی‌های درجا](/docs/concepts/cluster-administration/manage-deployment/#in-place-updates-of-resources)
را روی StatefulSetهای خود انجام دهید.

اگر StatefulSet شما در ابتدا با `kubectl apply` ایجاد شده است،
فیلد `.spec.replicas` را در مانیفست‌های StatefulSet به‌روزرسانی کنید و سپس دستور `kubectl apply` را اجرا کنید:

```shell
kubectl apply -f <stateful-set-file-updated>
```

در غیر این صورت، آن فیلد را با `kubectl edit` ویرایش کنید:

```shell
kubectl edit statefulsets <stateful-set-name>
```

یا از `kubectl patch` استفاده کنید:

```shell
kubectl patch statefulsets <stateful-set-name> -p '{"spec":{"replicas":<new-replicas>}}'
```

## عیب‌یابی

### کاهش مقیاس به‌درستی کار نمی‌کند

وقتی هر یک از Podهای حالت‌مندی که یک StatefulSet مدیریت می‌کند ناسالم باشد، نمی‌توانید مقیاس آن StatefulSet را کاهش دهید.
کاهش مقیاس تنها پس از آن انجام می‌شود که آن Podهای حالت‌مند در حال اجرا و آماده شوند.

اگر مقدار spec.replicas بیشتر از ۱ باشد، کوبرنتیز نمی‌تواند علت ناسالم بودن یک Pod را تشخیص دهد.
این وضعیت ممکن است ناشی از یک خطای دائمی یا یک خطای گذرا باشد. خطای گذرا
می‌تواند در اثر راه‌اندازی مجددی رخ دهد که برای ارتقا یا نگهداری لازم است.

اگر Pod به‌دلیل یک خطای دائمی ناسالم باشد، مقیاس‌دهی بدون رفع آن خطا
ممکن است به وضعیتی منجر شود که تعداد اعضای StatefulSet از حداقل تعداد رونوشت‌های
لازم برای عملکرد درست کمتر شود. این امر ممکن است باعث شود StatefulSet شما از دسترس خارج شود.

اگر Pod به‌دلیل یک خطای گذرا ناسالم باشد و احتمال دارد دوباره در دسترس قرار گیرد،
این خطای گذرا ممکن است در عملیات افزایش یا کاهش مقیاس شما اختلال ایجاد کند. برخی از پایگاه‌داده‌های
توزیع‌شده هنگامی که نودها هم‌زمان به آن‌ها می‌پیوندند و از آن‌ها جدا می‌شوند، دچار مشکل می‌شوند. در این موارد بهتر است
دربارهٔ عملیات مقیاس‌دهی در سطح برنامه تصمیم‌گیری کنید و تنها زمانی
مقیاس‌دهی را انجام دهید که مطمئن هستید کلاستر برنامهٔ حالت‌مند شما
کاملاً سالم است.

## {{% heading "whatsnext" %}}

- دربارهٔ [حذف یک StatefulSet](/docs/tasks/run-application/delete-stateful-set/) بیشتر بیاموزید.
