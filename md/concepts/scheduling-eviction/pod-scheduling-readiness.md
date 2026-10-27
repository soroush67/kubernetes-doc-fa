---
title: آمادگی زمان‌بندی Pod
content_type: concept
weight: 40
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.30" state="stable" >}}

Podها به محض ایجاد، آمادهٔ زمان‌بندی در نظر گرفته می‌شدند. زمان‌بند کوبرنتیز
تمام تلاش خود را برای یافتن نودهایی جهت جای‌گذاری همهٔ Podهای در انتظار انجام می‌دهد. با این حال، در
موارد واقعی، برخی Podها ممکن است برای مدتی طولانی در وضعیت «فاقد منابع ضروری» باقی بمانند.
این Podها در عمل زمان‌بند (و یکپارچه‌کننده‌های پایین‌دستی مانند Cluster AutoScaler) را
به‌طور غیرضروری درگیر می‌کنند.

با تعیین یا حذف `.spec.schedulingGates` یک Pod، می‌توانید کنترل کنید که Pod چه زمانی
آمادهٔ در نظر گرفته شدن برای زمان‌بندی است.

<!-- body -->

## پیکربندی schedulingGates برای Pod

فیلد `schedulingGates` شامل فهرستی از رشته‌هاست و هر رشته به‌عنوان
معیاری تلقی می‌شود که Pod باید پیش از قابل زمان‌بندی تلقی شدن آن را برآورده کند. این فیلد تنها
هنگام ایجاد Pod قابل مقداردهی اولیه است (یا توسط کلاینت، یا با تغییر در طول پذیرش). پس از ایجاد،
هر schedulingGate را می‌توان به ترتیب دلخواه حذف کرد، اما افزودن یک scheduling gate جدید مجاز نیست.

{{< figure src="/docs/images/podSchedulingGates.svg" alt="pod-scheduling-gates-diagram" caption="شکل. SchedulingGates در Pod" class="diagram-large" link="https://mermaid.live/edit#pako:eNplkktTwyAUhf8KgzuHWpukaYszutGlK3caFxQuCVMCGSDVTKf_XfKyPlhxz4HDB9wT5lYAptgHFuBRsdKxenFMClMYFIdfUdRYgbiD6ItJTEbR8wpEq5UpUfnDTf-5cbPoJjcbXdcaE61RVJIiqJvQ_Y30D-OCt-t3tFjcR5wZayiVnIGmkv4NiEfX9jijKTmmRH5jf0sRugOP0HyHUc1m6KGMFP27cM28fwSJDluPpNKaXqVJzmFNfHD2APRKSjnNFx9KhIpmzSfhVls3eHdTRrwG8QnxKfEZUUNeYTDBNbiaKRF_5dSfX-BQQQ0FpnEqQLJWhwIX5hyXsjbYl85wTINrgeC2EZd_xFQy7b_VJ6GCdd-itkxALE84dE3fAqXyIUZya6Qqe711OspVCI2ny2Vv35QqVO3-htt66ZWomAvVcZcv8yTfsiSFfJOydZoKvl_ttjLJVlJsblcJw-czwQ0zr9ZeqGDgeR77b2jD8xdtjtDn" >}}
## نمونهٔ استفاده

برای علامت‌گذاری یک Pod به‌عنوان آماده‌نبودن برای زمان‌بندی، می‌توانید آن را با یک یا چند scheduling gate مانند زیر ایجاد کنید:

{{% code_sample file="pods/pod-with-scheduling-gates.yaml" %}}

پس از ایجاد Pod، می‌توانید وضعیت آن را با فرمان زیر بررسی کنید:

```bash
kubectl get pod test-pod
```

خروجی نشان می‌دهد که Pod در وضعیت `SchedulingGated` قرار دارد:

```none
NAME       READY   STATUS            RESTARTS   AGE
test-pod   0/1     SchedulingGated   0          7s
```

همچنین می‌توانید فیلد `schedulingGates` آن را با اجرای فرمان زیر بررسی کنید:

```bash
kubectl get pod test-pod -o jsonpath='{.spec.schedulingGates}'
```

خروجی چنین است:

```none
[{"name":"example.com/foo"},{"name":"example.com/bar"}]
```

برای اطلاع دادن به زمان‌بند که این Pod آمادهٔ زمان‌بندی است، می‌توانید `schedulingGates` آن را به‌طور کامل
با اعمال دوبارهٔ یک مانیفست تغییریافته حذف کنید:

{{% code_sample file="pods/pod-without-scheduling-gates.yaml" %}}

می‌توانید با اجرای فرمان زیر بررسی کنید که آیا `schedulingGates` پاک شده است یا نه:

```bash
kubectl get pod test-pod -o jsonpath='{.spec.schedulingGates}'
```

انتظار می‌رود خروجی خالی باشد. و می‌توانید آخرین وضعیت آن را با اجرای فرمان زیر بررسی کنید:

```bash
kubectl get pod test-pod -o wide
```

با توجه به اینکه test-pod هیچ منبع CPU/حافظه‌ای درخواست نمی‌کند، انتظار می‌رود وضعیت این Pod
از `SchedulingGated` قبلی به `Running` تغییر کند:

```none
NAME       READY   STATUS    RESTARTS   AGE   IP         NODE
test-pod   1/1     Running   0          15s   10.0.0.4   node-2
```

## مشاهده‌پذیری

متریک `scheduler_pending_pods` با یک برچسب جدید `"gated"` همراه است تا مشخص شود که آیا برای یک Pod
تلاش زمان‌بندی شده اما غیرقابل زمان‌بندی اعلام شده است، یا به‌طور صریح به‌عنوان آماده‌نبودن برای
زمان‌بندی علامت‌گذاری شده است. می‌توانید از `scheduler_pending_pods{queue="gated"}` برای بررسی نتیجهٔ متریک استفاده کنید.

## دستورالعمل‌های زمان‌بندی قابل تغییر Pod

می‌توانید دستورالعمل‌های زمان‌بندی Podها را تا زمانی که scheduling gate دارند، با قیدهای مشخصی تغییر دهید.
در سطح کلی، تنها می‌توانید دستورالعمل‌های زمان‌بندی یک Pod را سخت‌گیرانه‌تر کنید. به عبارت دیگر،
دستورالعمل‌های به‌روزشده باید باعث شوند Podها تنها بتوانند روی زیرمجموعه‌ای از نودهایی زمان‌بندی شوند که
پیش‌تر با آن‌ها منطبق بودند. به‌طور مشخص‌تر، قواعد به‌روزرسانی دستورالعمل‌های زمان‌بندی یک Pod به شرح زیر است:

1. برای `.spec.nodeSelector`، تنها افزودن مجاز است. اگر وجود نداشته باشد، تنظیم آن مجاز خواهد بود.

2. برای `spec.affinity.nodeAffinity`، اگر nil باشد، تنظیم هر مقداری مجاز است.

3. اگر `NodeSelectorTerms` خالی بوده باشد، تنظیم آن مجاز خواهد بود.
   اگر خالی نباشد، تنها افزودن `NodeSelectorRequirements` به `matchExpressions`
   یا `fieldExpressions` مجاز است و هیچ تغییری در `matchExpressions`
   و `fieldExpressions` موجود مجاز نخواهد بود. دلیل این امر آن است که عبارت‌های موجود در
   `.requiredDuringSchedulingIgnoredDuringExecution.NodeSelectorTerms` با OR ترکیب می‌شوند،
   در حالی که عبارت‌های موجود در `nodeSelectorTerms[].matchExpressions` و
   `nodeSelectorTerms[].fieldExpressions` با AND ترکیب می‌شوند.

4. برای `.preferredDuringSchedulingIgnoredDuringExecution`، همهٔ به‌روزرسانی‌ها مجاز هستند.
   دلیل این امر آن است که عبارت‌های ترجیحی مرجع قطعی نیستند و بنابراین کنترل‌کننده‌های سیاست
   آن عبارت‌ها را اعتبارسنجی نمی‌کنند.


## {{% heading "whatsnext" %}}

* برای جزئیات بیشتر، [KEP مربوط به PodSchedulingReadiness](https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/3521-pod-scheduling-readiness) را بخوانید
