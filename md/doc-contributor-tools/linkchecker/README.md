# ابزار بررسی لینک‌های داخلی

می‌توانید از [htmltest](https://github.com/wjdp/htmltest) برای بررسی لینک‌های خراب در
[`/content/en/`](https://git.k8s.io/website/content/en/) استفاده کنید. این ابزار هنگام بازآرایی
بخش‌هایی از محتوا، جابه‌جایی صفحه‌ها، یا تغییر نام فایل‌ها یا سرصفحه‌های صفحه‌ها مفید است.

## ابزار چگونه کار می‌کند

`htmltest` لینک‌ها را در فایل‌های HTML تولیدشده‌ی مخزن وب‌سایت کوبرنتیز بررسی می‌کند.
این ابزار با یک دستور `make` اجرا می‌شود که مراحل زیر را انجام می‌دهد:

- سایت را می‌سازد و خروجی HTML را در پوشه‌ی `/public` مخزن محلی `kubernetes/website`
  شما تولید می‌کند
- ایمیج Docker با نام `wdjp/htmltest` را دریافت می‌کند
- مخزن محلی `kubernetes/website` شما را روی ایمیج Docker مونت می‌کند
- فایل‌های تولیدشده در پوشه‌ی `/public` را بررسی می‌کند و هرگاه به لینک داخلی خراب برسد،
  خروجی را در خط فرمان نمایش می‌دهد

## آنچه بررسی می‌شود و آنچه بررسی نمی‌شود

بررسی‌کننده‌ی لینک، فایل‌های HTML تولیدشده را بررسی می‌کند، نه Markdown خام.
ابزار htmltest برای تعیین اینکه کدام محتوا را بررسی کند، به یک فایل پیکربندی به نام
[`.htmltest.yml`](https://git.k8s.io/website/.htmltest.yml) وابسته است.

بررسی‌کننده‌ی لینک موارد زیر را بررسی می‌کند:

- تمام محتوای تولیدشده از Markdown در پوشه‌ی
  [`/content/en/docs`](https://git.k8s.io/website/content/en/docs/)، به‌جز:
  - مراجع API تولیدشده، برای مثال
    https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/
- تمام لینک‌های داخلی، به‌جز:
  - هش‌های خالی (`<a href="#">` یا `[title](#)`) و href های خالی (`<a href="">` یا `[title]()`)
  - لینک‌های داخلی به تصاویر و سایر فایل‌های رسانه‌ای

بررسی‌کننده‌ی لینک موارد زیر را بررسی نمی‌کند:

- لینک‌های موجود در نوار پیمایش بالا و کناری، لینک‌های پانویس (footer)، یا لینک‌های بخش `<head>` یک صفحه،
  مانند لینک‌ها به شیوه‌نامه‌های CSS، اسکریپت‌ها و اطلاعات متا
- صفحه‌های سطح بالا و زیرمجموعه‌های آن‌ها، برای مثال: `/training`، `/community`، `/case-studies/adidas`
- پست‌های وبلاگ
- مستندات مرجع API، برای مثال
  https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/
- محلی‌سازی‌ها

## پیش‌نیازها و نصب

باید موارد زیر را نصب کنید:

* [Docker](https://docs.docker.com/get-docker/)
* [make](https://www.gnu.org/software/make/)

## اجرای بررسی‌کننده‌ی لینک

برای اجرای بررسی‌کننده‌ی لینک:

1. به پوشه‌ی ریشه‌ی مخزن محلی `kubernetes/website` خود بروید.

2. دستور زیر را اجرا کنید:

   ```shell
   make container-internal-linkcheck
   ```

## درک خروجی

اگر بررسی‌کننده‌ی لینک، لینک‌های خراب پیدا کند، خروجی مشابه زیر خواهد بود:

```
tasks/access-kubernetes-api/custom-resources/index.html
  hash does not exist --- tasks/access-kubernetes-api/custom-resources/index.html --> #preserving-unknown-fields
  hash does not exist --- tasks/access-kubernetes-api/custom-resources/index.html --> #preserving-unknown-fields
```

این یک مجموعه از لینک‌های خراب است. گزارش برای هر صفحه‌ای که لینک خراب دارد، یک خروجی اضافه می‌کند.

در این خروجی، فایلی که لینک‌های خراب دارد `tasks/access-kubernetes-api/custom-resources.md` است.

ابزار یک دلیل ارائه می‌دهد: `hash does not exist`. در بیشتر موارد می‌توانید آن را نادیده بگیرید.

نشانی هدف `#preserving-unknown-fields` است.

یکی از راه‌های رفع این مشکل به شرح زیر است:

1. به فایل Markdown دارای لینک خراب بروید.
1. با استفاده از یک ویرایشگر متن، یک جست‌وجوی تمام‌متن (معمولاً Ctrl+F یا Command+F) برای
   نشانی لینک خراب، یعنی `#preserving-unknown-fields`، انجام دهید.
1. لینک را اصلاح کنید. برای لینکی با هش صفحه (یا _anchor_) خراب،
   بررسی کنید که آیا عنوان آن مبحث تغییر نام داده یا حذف شده است.

htmltest را اجرا کنید تا از رفع شدن لینک‌های خراب اطمینان حاصل کنید.
