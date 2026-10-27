---
title: ابزار خط فرمان kubectl
content_type: concept
description: >
  kubectl ابزار خط فرمان اصلی برای ارتباط با یک کلاستر کوبرنتیز است. این صفحه نمای کلی‌ای از kubectl و نقش آن در اکوسیستم کوبرنتیز ارائه می‌کند.
weight: 50
card:
  name: concepts
  title: kubectl
  weight: 40
---

<!-- overview -->

{{< glossary_definition prepend="Kubernetes provides a" term_id="kubectl" length="short" >}}

ابزار `kubectl` از طریق [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) با کلاستر شما ارتباط برقرار می‌کند.
`kubectl` برای پیکربندی، به دنبال فایلی با نام `config` در دایرکتوری `$HOME/.kube` می‌گردد.
می‌توانید با تنظیم متغیر محیطی `KUBECONFIG` یا با تنظیم فلگ
[`--kubeconfig`](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)، فایل‌های
[kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) دیگری را مشخص کنید.

<!-- body -->

## نقش kubectl

ابزار `kubectl` رابط اصلی برای ایجاد، بررسی، به‌روزرسانی و حذف آبجکت‌های کوبرنتیز است.
این ابزار مکمل [مؤلفه‌های کوبرنتیز](/docs/concepts/overview/components/) است که درون کلاستر شما اجرا می‌شوند
و نیز مکمل [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) است که این مؤلفه‌ها آن را پیاده‌سازی می‌کنند.
چه `kubectl` را از لپ‌تاپ خود اجرا کنید و چه از یک Pod درون کلاستر، این ابزار درخواست‌ها را به API server ارسال می‌کند.
کلاینت‌های دیگر، مانند [کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/) و داشبوردهای وب
مانند [Headlamp](https://headlamp.dev/)، نیز از طریق همین API ارتباط برقرار می‌کنند.

## kubectl چگونه کار می‌کند

ابزار `kubectl` با استفاده از کلاستر، کاربر و context تعریف‌شده در فایل
[kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) شما، به API server متصل می‌شود و احراز هویت می‌کند.
هنگامی که `kubectl` را از بیرون یک کلاستر اجرا می‌کنید، این ابزار از فایل kubeconfig برای یافتن نشانی API server و اعتبارنامه‌ها استفاده می‌کند.
هنگامی که `kubectl` درون یک Pod اجرا می‌شود (برای مثال، در یک خط لوله‌ی CI/CD)، می‌تواند از احراز هویت درون‌کلاستری
مبتنی بر توکن ServiceAccount که در Pod به‌صورت mount قرار گرفته است استفاده کند.

هنگامی که فرمانی را اجرا می‌کنید، `kubectl` قصد شما را به یک یا چند درخواست HTTP به
[API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) ترجمه می‌کند. API server هر درخواست را اعتبارسنجی می‌کند،
آن را بر وضعیت کلاستر که در {{< glossary_tooltip text="etcd" term_id="etcd" >}} ذخیره شده است اعمال می‌کند و
نتیجه را بازمی‌گرداند. این یعنی هر عملی که با `kubectl` انجام می‌شود، چه ایجاد یک Deployment باشد و چه خواندن لاگ‌ها،
مسیر یکسانِ مبتنی بر API را طی می‌کند.

از آنجا که kubeconfig شما می‌تواند چندین کلاستر، کاربر و context را تعریف کند، می‌توانید از `kubectl` برای
جابه‌جایی میان کلاسترها بدون پیکربندی دوباره‌ی محیط خود استفاده کنید. برای تغییر context فعال،
فرمان `kubectl config use-context` را اجرا کنید.

## با kubectl چه کارهایی می‌توانید انجام دهید

ابزار `kubectl` از عملیات بسیاری پشتیبانی می‌کند که در این دسته‌های کلی قرار می‌گیرند:

* **مدیریت منابع** – آبجکت‌هایی مانند Podها، Deploymentها و Serviceها را ایجاد، به‌روزرسانی و حذف کنید.
  برای مدیریت اعلانی بر اساس فایل‌های پیکربندی، از `kubectl apply` استفاده کنید.
* **بررسی وضعیت کلاستر** – آبجکت‌ها را فهرست و توصیف کنید، رویدادها را مشاهده کنید و میزان مصرف منابع را بررسی کنید.
* **اشکال‌زدایی** – لاگ‌های کانتینرها را مشاهده کنید، فرمان‌هایی را درون یک کانتینر در حال اجرا اجرا کنید، یا پورتی را به یک Pod هدایت (port-forward) کنید.
* **عملیات کلاستر** – نودها را برای نگهداری تخلیه (drain) کنید، نودها را برای جلوگیری از پذیرش بارهای کاری جدید cordon کنید و پیکربندی کلاستر را مدیریت کنید.
* **اسکریپت‌نویسی و خودکارسازی** – خروجی را برای استفاده در اسکریپت‌ها و خطوط لوله، به‌صورت JSON، YAML یا ستون‌های سفارشی با استفاده از [JSONPath](/docs/reference/kubectl/jsonpath/) قالب‌بندی کنید.

برای نحو، مرجع فرمان‌ها و نمونه‌ها، [مستندات مرجع kubectl](/docs/reference/kubectl/) را ببینید.

## اعلانی در برابر دستوری

برای بارهای کاری عملیاتی، [مدیریت اعلانی آبجکت‌ها](/docs/concepts/overview/working-with-objects/object-management/)
با استفاده از `kubectl apply` و فایل‌های پیکربندیِ تحت کنترل نسخه را ترجیح دهید.
مدیریت اعلانی به شما کمک می‌کند تغییرات را ردیابی کنید، به‌صورت گروهی همکاری کنید و با گردش‌کارهای GitOps یکپارچه شوید.
فرمان‌های دستوری (مانند `kubectl create` یا `kubectl run`) برای توسعه و آزمایش مفید هستند،
اما بازتولید و ممیزی آن‌ها دشوارتر است.

## گسترش kubectl با افزونه‌ها

می‌توانید `kubectl` را با [افزونه‌هایی](/docs/tasks/extend-kubectl/kubectl-plugins/) گسترش دهید که
زیرفرمان‌های جدیدی اضافه می‌کنند. افزونه‌ها فایل‌های اجرایی مستقلی هستند که از قرارداد نام‌گذاری `kubectl-<plugin-name>` پیروی می‌کنند.
جامعه‌ی کوبرنتیز افزونه‌های بسیاری را نگهداری می‌کند و می‌توانید آن‌ها را با
مدیر افزونه‌ی [Krew](https://krew.sigs.k8s.io/) مدیریت کنید.

## سازگاری نسخه‌ها

ابزار `kubectl` از اختلاف نسخه‌ی حداکثر یک نسخه‌ی فرعی (minor) بالاتر یا پایین‌تر نسبت به control plane
کلاستر پشتیبانی می‌کند. برای مثال، `kubectl` نسخه‌ی v1.32 با control planeهای نسخه‌ی v1.31، v1.32 و v1.33 کار می‌کند.
استفاده از نسخه‌ی سازگار از بروز رفتارهای غیرمنتظره جلوگیری می‌کند. برای جزئیات،
[سیاست اختلاف نسخه](/releases/version-skew-policy/) را ببینید.

## {{% heading "whatsnext" %}}

* برای جزئیات نحو و فرمان‌ها، [مرجع kubectl](/docs/reference/kubectl/) را مطالعه کنید.
* [kubectl را روی ماشین خود نصب کنید](/docs/tasks/tools/#kubectl).
* درباره‌ی [API کوبرنتیز](/docs/concepts/overview/kubernetes-api/) که `kubectl` از آن استفاده می‌کند بیاموزید.
* [مؤلفه‌های کوبرنتیز](/docs/concepts/overview/components/) را که یک کلاستر را تشکیل می‌دهند مرور کنید.
* [مدیریت آبجکت‌ها](/docs/concepts/overview/working-with-objects/object-management/) و پیکربندی اعلانی را بررسی کنید.
* برای ترکیب‌های نسخه‌ی پشتیبانی‌شده، [سیاست اختلاف نسخه](/releases/version-skew-policy/) را بررسی کنید.
