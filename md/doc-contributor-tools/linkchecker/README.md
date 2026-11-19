# ابزار بررسی پیوندهای داخلی

برای یافتن پیوندهای خراب در
[`/content/en/`](https://git.k8s.io/website/content/en/) می‌توانید از [htmltest](https://github.com/wjdp/htmltest) استفاده کنید. این ابزار هنگام بازآرایی بخش‌هایی از محتوا، جابه‌جا کردن صفحه‌ها یا تغییر نام فایل‌ها یا سرعنوان‌های صفحه مفید است.

## نحوهٔ کار ابزار

ابزار `htmltest` پیوندهای موجود در فایل‌های HTML تولیدشدهٔ مخزن وب‌سایت کوبرنتیز را بررسی می‌کند. این ابزار با یک دستور `make` اجرا می‌شود که کارهای زیر را انجام می‌دهد:

- سایت را می‌سازد و خروجی HTML را در پوشهٔ `/public` مخزن محلی `kubernetes/website` شما تولید می‌کند.
- ایمیج Docker با نام `wdjp/htmltest` را دریافت می‌کند.
- مخزن محلی `kubernetes/website` شما را در ایمیج Docker سوار (mount) می‌کند.
- فایل‌های تولیدشده در پوشهٔ `/public` را بررسی می‌کند و هر جا به پیوند داخلی خرابی برخورد کند، آن را در خروجی خط فرمان گزارش می‌دهد.

## مواردی که بررسی می‌شوند و مواردی که بررسی نمی‌شوند

بررسی‌کنندهٔ پیوند، فایل‌های HTML تولیدشده را بررسی می‌کند، نه فایل‌های خام Markdown.
ابزار htmltest برای تعیین محتوایی که باید بررسی شود، به فایل پیکربندی
[`.htmltest.yml`](https://git.k8s.io/website/.htmltest.yml)
وابسته است.

بررسی‌کنندهٔ پیوند موارد زیر را بررسی می‌کند:

- تمام محتوای تولیدشده از Markdown در پوشهٔ
  [`/content/en/docs`](https://git.k8s.io/website/content/en/docs/)، به‌جز:
  - مرجع‌های API تولیدشده، برای نمونه
    https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/
- تمام پیوندهای داخلی، به‌جز:
  - هش‌های خالی (`<a href="#">` یا `[title](#)`) و hrefهای خالی (`<a href="">` یا `[title]()`)
  - پیوندهای داخلی به تصاویر و دیگر فایل‌های رسانه‌ای

بررسی‌کنندهٔ پیوند موارد زیر را بررسی نمی‌کند:

- پیوندهای موجود در نوارهای پیمایش بالا و کناری، پیوندهای پانویس، یا پیوندهای بخش `<head>` صفحه، مانند پیوند به برگه‌های سبک CSS، اسکریپت‌ها و اطلاعات متا
- صفحه‌های سطح بالا و زیرصفحه‌های آن‌ها، برای نمونه: `/training`، `/community`، `/case-studies/adidas`
- نوشته‌های وبلاگ
- مستندات مرجع API، برای نمونه
  https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/
- نسخه‌های بومی‌سازی‌شده

## پیش‌نیازها و نصب

باید این ابزارها را نصب کنید:

* [Docker](https://docs.docker.com/get-docker/)
* [make](https://www.gnu.org/software/make/)

## اجرای بررسی‌کنندهٔ پیوند

برای اجرای بررسی‌کنندهٔ پیوند:

1. به پوشهٔ ریشهٔ مخزن محلی `kubernetes/website` خود بروید.

2. دستور زیر را اجرا کنید:

   ```shell
   make container-internal-linkcheck
   ```

## درک خروجی

اگر بررسی‌کنندهٔ پیوند پیوند خرابی پیدا کند، خروجی مشابه زیر خواهد بود:

```
tasks/access-kubernetes-api/custom-resources/index.html
  hash does not exist --- tasks/access-kubernetes-api/custom-resources/index.html --> #preserving-unknown-fields
  hash does not exist --- tasks/access-kubernetes-api/custom-resources/index.html --> #preserving-unknown-fields
```

این خروجی یک مجموعه از پیوندهای خراب است. گزارش برای هر صفحه‌ای که پیوند خراب دارد، یک خروجی جداگانه اضافه می‌کند.

در این خروجی، فایلی که پیوند خراب دارد `tasks/access-kubernetes-api/custom-resources.md` است.

ابزار دلیل خطا را نیز اعلام می‌کند: `hash does not exist`. در بیشتر موارد می‌توانید این دلیل را نادیده بگیرید.

نشانی مقصد `#preserving-unknown-fields` است.

یکی از راه‌های رفع این مشکل چنین است:

1. به فایل Markdown حاوی پیوند خراب بروید.
1. با یک ویرایشگر متن، نشانی پیوند خراب، یعنی `#preserving-unknown-fields`، را در کل متن جست‌وجو کنید (معمولاً با Ctrl+F یا Command+F).
1. پیوند را اصلاح کنید. برای پیوند هش (یا _لنگر_) خراب در صفحه، بررسی کنید که آیا نام آن موضوع تغییر کرده یا حذف شده است.

برای اطمینان از رفع پیوندهای خراب، htmltest را دوباره اجرا کنید.
