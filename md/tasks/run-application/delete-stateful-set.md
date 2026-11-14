---
reviewers:
- bprashanth
- erictune
- foxish
- janetkuo
- smarterclayton
title: حذف یک StatefulSet
content_type: task
weight: 60
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه یک {{< glossary_tooltip term_id="StatefulSet" >}} را حذف کنید.

## {{% heading "prerequisites" %}}

- فرض این صفحه بر این است که برنامه‌ای در کلاستر شما اجرا می‌شود که با یک StatefulSet تعریف شده است.

<!-- steps -->

## حذف یک StatefulSet

می‌توانید یک StatefulSet را به همان روشی حذف کنید که سایر منابع را در کوبرنتیز حذف می‌کنید:
از دستور `kubectl delete` استفاده کنید و StatefulSet را با فایل یا با نام آن مشخص کنید.

```shell
kubectl delete -f <file.yaml>
```

```shell
kubectl delete statefulsets <statefulset-name>
```

ممکن است لازم باشد پس از حذف خود StatefulSet، سرویس headless مرتبط با آن را جداگانه حذف کنید.

```shell
kubectl delete service <service-name>
```

هنگامی که یک StatefulSet را با `kubectl` حذف می‌کنید، تعداد رپلیکاهای آن به صفر کاهش می‌یابد
و همهٔ Podهایی که بخشی از این بار کاری هستند نیز حذف می‌شوند. اگر می‌خواهید فقط
خود StatefulSet را حذف کنید و Podها باقی بمانند، از `--cascade=orphan` استفاده کنید. برای نمونه:

```shell
kubectl delete -f <file.yaml> --cascade=orphan
```

با ارسال `--cascade=orphan` به `kubectl delete`، Podهایی که StatefulSet مدیریت می‌کند
حتی پس از حذف خود آبجکت StatefulSet نیز باقی می‌مانند. اگر این Podها برچسب
`app.kubernetes.io/name=MyApp` داشته باشند، می‌توانید آن‌ها را به شکل زیر حذف کنید:

```shell
kubectl delete pods -l app.kubernetes.io/name=MyApp
```

### حجم‌های پایدار (Persistent Volumes)

حذف Podهای یک StatefulSet، حجم‌های مرتبط با آن‌ها را حذف نمی‌کند.
هدف از این رفتار آن است که پیش از حذف حجم، فرصت داشته باشید داده‌ها را از آن کپی کنید.
بسته به کلاس ذخیره‌سازی (storage class) و سیاست بازپس‌گیری (reclaim policy)، حذف PVC
پس از خاتمهٔ Podها ممکن است به حذف حجم‌های پایدار پشتیبان آن منجر شود.
هرگز نباید فرض کنید که پس از حذف درخواست حجم (claim)، همچنان به آن حجم دسترسی خواهید داشت.

{{< note >}}
هنگام حذف یک PVC احتیاط کنید، زیرا ممکن است به از دست رفتن داده‌ها منجر شود.
{{< /note >}}

### حذف کامل یک StatefulSet

برای حذف همه‌چیز در یک StatefulSet، از جمله Podهای مرتبط با آن،
می‌توانید مجموعه‌ای از دستورها مشابه نمونهٔ زیر را اجرا کنید:

```shell
grace=$(kubectl get pods <stateful-set-pod> --template '{{.spec.terminationGracePeriodSeconds}}')
kubectl delete statefulset -l app.kubernetes.io/name=MyApp
sleep $grace
kubectl delete pvc -l app.kubernetes.io/name=MyApp

```

در مثال بالا، Podها برچسب `app.kubernetes.io/name=MyApp` دارند؛
در صورت نیاز، برچسب خودتان را جایگزین آن کنید.

### حذف اجباری Podهای StatefulSet

اگر متوجه شدید که برخی از Podهای StatefulSet شما برای مدتی طولانی در وضعیت 'Terminating'
یا 'Unknown' گیر کرده‌اند، ممکن است لازم باشد به‌صورت دستی مداخله کنید
و Podها را به‌اجبار از apiserver حذف کنید.
این کار به‌طور بالقوه خطرناک است. برای جزئیات بیشتر به
[حذف اجباری Podهای StatefulSet](/docs/tasks/run-application/force-delete-stateful-set-pod/)
مراجعه کنید.

## {{% heading "whatsnext" %}}

دربارهٔ [حذف اجباری Podهای StatefulSet](/docs/tasks/run-application/force-delete-stateful-set-pod/) بیشتر بیاموزید.
