---
title: الگوی Operator
content_type: concept
weight: 30
---

<!-- overview -->

Operatorها افزونه‌های نرم‌افزاری برای کوبرنتیز هستند که از
[منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
برای مدیریت برنامه‌ها و اجزای آن‌ها استفاده می‌کنند. Operatorها از
اصول کوبرنتیز، به‌ویژه [حلقهٔ کنترل](/docs/concepts/architecture/controller)، پیروی می‌کنند.

<!-- body -->

## انگیزه

هدف _الگوی operator_ بازتاب هدف اصلی یک اپراتور انسانی است که
یک سرویس یا مجموعه‌ای از سرویس‌ها را مدیریت می‌کند. اپراتورهای انسانی که مسئول
برنامه‌ها و سرویس‌های مشخصی هستند، دانش عمیقی دربارهٔ این دارند که سیستم
چگونه باید رفتار کند، چگونه مستقر شود و در صورت بروز مشکل چگونه باید واکنش نشان داد.

افرادی که بارهای کاری را روی کوبرنتیز اجرا می‌کنند، اغلب دوست دارند از خودکارسازی برای
رسیدگی به کارهای تکراری استفاده کنند. الگوی operator نشان می‌دهد چگونه می‌توانید
کدی بنویسید تا یک کار را فراتر از آنچه خود کوبرنتیز فراهم می‌کند خودکار کنید.

## Operatorها در کوبرنتیز

کوبرنتیز برای خودکارسازی طراحی شده است. به‌طور پیش‌فرض، مقدار زیادی
خودکارسازی داخلی از هستهٔ کوبرنتیز دریافت می‌کنید. می‌توانید از کوبرنتیز
برای خودکارسازی استقرار و اجرای بارهای کاری استفاده کنید، *و* می‌توانید نحوهٔ انجام این کار
توسط کوبرنتیز را نیز خودکار کنید.

مفهوم {{< glossary_tooltip text="الگوی operator" term_id="operator-pattern" >}} در کوبرنتیز
به شما اجازه می‌دهد بدون تغییر کد خود کوبرنتیز، رفتار کلاستر را گسترش دهید؛
این کار با پیوند دادن {{< glossary_tooltip text="کنترل‌کننده‌ها" term_id="controller" >}} به
یک یا چند منبع سفارشی انجام می‌شود. Operatorها کلاینت‌های API کوبرنتیز هستند که به‌عنوان
کنترل‌کننده برای یک [منبع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) عمل می‌کنند.

## یک operator نمونه {#example}

برخی از کارهایی که می‌توانید با یک operator خودکار کنید عبارت‌اند از:

* استقرار یک برنامه در صورت نیاز
* تهیه و بازیابی نسخه‌های پشتیبان از وضعیت آن برنامه
* مدیریت ارتقاهای کد برنامه همراه با تغییرات مرتبط مانند
  طرح‌واره‌های پایگاه داده یا تنظیمات پیکربندی اضافی
* انتشار یک Service برای برنامه‌هایی که از APIهای کوبرنتیز برای
  کشف آن پشتیبانی نمی‌کنند
* شبیه‌سازی خرابی در تمام یا بخشی از کلاستر برای آزمودن تاب‌آوری آن
* انتخاب یک رهبر برای یک برنامهٔ توزیع‌شده که فرایند داخلی
  انتخاب عضو ندارد

یک operator با جزئیات بیشتر چگونه ممکن است به نظر برسد؟ در اینجا یک مثال آمده است:

1. یک منبع سفارشی با نام SampleDB که می‌توانید آن را در کلاستر پیکربندی کنید.
2. یک Deployment که اطمینان حاصل می‌کند یک Pod شامل
   بخش کنترل‌کنندهٔ operator در حال اجراست.
3. یک ایمیج کانتینر از کد operator.
4. کد کنترل‌کننده‌ای که از control plane پرس‌وجو می‌کند تا دریابد کدام منابع SampleDB
   پیکربندی شده‌اند.
5. هستهٔ operator کدی است که به سرور API می‌گوید چگونه
   واقعیت را با منابع پیکربندی‌شده منطبق کند.
   * اگر یک SampleDB جدید اضافه کنید، operator ‏PersistentVolumeClaimها را
     برای فراهم‌کردن ذخیره‌سازی ماندگار پایگاه داده، یک StatefulSet برای اجرای SampleDB و
     یک Job برای انجام پیکربندی اولیه راه‌اندازی می‌کند.
   * اگر آن را حذف کنید، operator یک snapshot تهیه می‌کند و سپس اطمینان حاصل می‌کند که
     StatefulSet و Volumeها نیز حذف شده‌اند.
6. operator همچنین پشتیبان‌گیری‌های منظم از پایگاه داده را مدیریت می‌کند. برای هر منبع SampleDB،
   operator تعیین می‌کند چه زمانی یک Pod ایجاد شود که بتواند به
   پایگاه داده متصل شود و نسخهٔ پشتیبان تهیه کند. این پادها به یک ConfigMap
   و/یا یک Secret متکی خواهند بود که جزئیات اتصال و اعتبارنامه‌های پایگاه داده را در خود دارد.
7. از آنجا که هدف operator فراهم‌کردن خودکارسازی مستحکم برای منبعی است که
   مدیریت می‌کند، کد پشتیبان دیگری نیز وجود خواهد داشت. در این مثال،
   کد بررسی می‌کند که آیا پایگاه داده نسخهٔ قدیمی را اجرا می‌کند و اگر چنین باشد،
   آبجکت‌های Job ایجاد می‌کند که آن را برای شما ارتقا می‌دهند.

## استقرار operatorها

رایج‌ترین روش برای استقرار یک operator، افزودن
Custom Resource Definition و Controller مرتبط با آن به کلاستر است.
Controller معمولاً بیرون از
{{< glossary_tooltip text="control plane" term_id="control-plane" >}} اجرا می‌شود،
تقریباً همان‌طور که هر برنامهٔ کانتینری‌شده‌ای را اجرا می‌کنید.
برای مثال، می‌توانید کنترل‌کننده را در کلاستر خود به‌صورت یک Deployment اجرا کنید.

## استفاده از یک operator {#using-operators}

پس از استقرار یک operator، با افزودن، تغییر یا
حذف نوع منبعی که operator از آن استفاده می‌کند، از آن بهره می‌برید. با دنبال کردن
مثال بالا، یک Deployment برای خود operator راه‌اندازی می‌کنید و سپس:

```shell
kubectl get SampleDB                   # find configured databases

kubectl edit SampleDB/example-database # manually change some settings
```

&hellip;و تمام! operator هم اعمال تغییرات و هم سالم نگه‌داشتن
سرویس موجود را بر عهده خواهد گرفت.

## نوشتن operator اختصاصی {#writing-operator}

اگر در اکوسیستم operatorی وجود ندارد که رفتار مورد نظر شما را پیاده‌سازی کند،
می‌توانید operator اختصاصی خود را بنویسید. 

همچنین می‌توانید یک operator (یعنی یک Controller) را با هر زبان یا محیط اجرایی
پیاده‌سازی کنید که بتواند به‌عنوان [کلاینت API کوبرنتیز](/docs/reference/using-api/client-libraries/) عمل کند.

در ادامه چند کتابخانه و ابزار آمده است که می‌توانید برای نوشتن operator ابرزاد
اختصاصی خود از آن‌ها استفاده کنید.

{{% thirdparty-content %}}

* [Charmed Operator Framework](https://juju.is/)
* [Java Operator SDK](https://github.com/operator-framework/java-operator-sdk)
* [Kopf](https://github.com/nolar/kopf) (Kubernetes Operator Pythonic Framework)
* [kube-rs](https://kube.rs/) (Rust)
* [kubebuilder](https://book.kubebuilder.io/)
* [KubeOps](https://dotnet.github.io/dotnet-operator-sdk/) (.NET operator SDK)
* [Mast](https://docs.ansi.services/mast/user_guide/operator/)
* [Metacontroller](https://metacontroller.github.io/metacontroller/intro.html) همراه با WebHookهایی که
  خودتان پیاده‌سازی می‌کنید
* [Operator Framework](https://operatorframework.io)
* [shell-operator](https://github.com/flant/shell-operator)

## {{% heading "whatsnext" %}}


* [مقالهٔ سفید Operator](https://github.com/cncf/tag-app-delivery/blob/163962c4b1cd70d085107fc579e3e04c2e14d59c/operator-wg/whitepaper/Operator-WhitePaper_v1-0.md)
  از {{< glossary_tooltip text="CNCF" term_id="cncf" >}} را بخوانید.
* دربارهٔ [منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) بیشتر بیاموزید
* operatorهای آماده‌ای را که با مورد استفادهٔ شما تناسب دارند در [OperatorHub.io](https://operatorhub.io/) پیدا کنید
* operator خود را برای استفادهٔ دیگران [منتشر کنید](https://operatorhub.io/)
* [مقالهٔ اصلی CoreOS](https://web.archive.org/web/20170129131616/https://coreos.com/blog/introducing-operators.html)
  را که الگوی operator را معرفی کرد بخوانید (این نسخه‌ای بایگانی‌شده از مقالهٔ اصلی است).
* [مقاله‌ای](https://cloud.google.com/blog/products/containers-kubernetes/best-practices-for-building-kubernetes-operators-and-stateful-apps)
  از Google Cloud دربارهٔ بهترین روش‌های ساخت operatorها بخوانید
