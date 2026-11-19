---
title: مشارکت در کد بالادستی کوبرنتیز
content_type: task
weight: 20
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید در پروژهٔ بالادستی (upstream) `kubernetes/kubernetes` مشارکت کنید. با این کار می‌توانید اشکال‌های موجود در مستندات API کوبرنتیز یا محتوای مؤلفه‌های کوبرنتیز مانند `kubeadm`، `kube-apiserver` و `kube-controller-manager` را برطرف کنید.

اگر به‌جای این کار می‌خواهید مستندات مرجع API کوبرنتیز یا مؤلفه‌های `kube-*` را از کد بالادستی دوباره تولید کنید، دستورالعمل‌های زیر را ببینید:

- [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
- [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)

## {{% heading "prerequisites" %}}

- باید این ابزارها را نصب کرده باشید:

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - [Golang](https://go.dev/doc/install) نسخهٔ 1.13 یا بالاتر
  - [Docker](https://docs.docker.com/engine/installation/)
  - [etcd](https://github.com/coreos/etcd/)
  - [make](https://www.gnu.org/software/make/)
  - [کامپایلر/لینکر gcc](https://gcc.gnu.org/)

- متغیر محیطی `GOPATH` باید تنظیم شده باشد و مسیر `etcd` باید در متغیر محیطی `PATH` قرار داشته باشد.

- باید بدانید که چگونه یک درخواست ادغام (pull request) برای یک مخزن GitHub ایجاد کنید. این کار معمولاً شامل ایجاد یک فورک از مخزن است. برای اطلاعات بیشتر، [ایجاد یک درخواست ادغام](https://help.github.com/articles/creating-a-pull-request/) و [گردش کار استاندارد فورک و درخواست ادغام در GitHub](https://gist.github.com/Chaser324/ce0505fbed06b947d962) را ببینید.

<!-- steps -->

## تصویر کلی

مستندات مرجع API کوبرنتیز و مؤلفه‌های `kube-*` مانند `kube-apiserver` و `kube-controller-manager` به‌طور خودکار از کد منبع موجود در [کوبرنتیز بالادستی](https://github.com/kubernetes/kubernetes/) تولید می‌شوند.

هنگامی که در مستندات تولیدشده با اشکالی روبه‌رو می‌شوید، شاید بخواهید برای رفع آن در پروژهٔ بالادستی یک وصله (patch) ایجاد کنید.

## کلون کردن مخزن کوبرنتیز

اگر هنوز مخزن kubernetes/kubernetes را در اختیار ندارید، اکنون آن را دریافت کنید:

```shell
mkdir $GOPATH/src
cd $GOPATH/src
go get github.com/kubernetes/kubernetes
```

پوشهٔ پایهٔ کلون خود از مخزن [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) را مشخص کنید. برای نمونه، اگر برای دریافت مخزن مرحلهٔ قبل را دنبال کرده باشید، پوشهٔ پایهٔ شما `$GOPATH/src/github.com/kubernetes/kubernetes` است. در مراحل بعدی، از این پوشهٔ پایه با عنوان `<k8s-base>` یاد می‌شود.

پوشهٔ پایهٔ کلون خود از مخزن [kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) را مشخص کنید. برای نمونه، اگر برای دریافت مخزن مرحلهٔ قبل را دنبال کرده باشید، پوشهٔ پایهٔ شما `$GOPATH/src/github.com/kubernetes-sigs/reference-docs` است. در مراحل بعدی، از این پوشهٔ پایه با عنوان `<rdocs-base>` یاد می‌شود.

## ویرایش کد منبع کوبرنتیز

مستندات مرجع API کوبرنتیز به‌طور خودکار از یک مشخصهٔ OpenAPI تولید می‌شود و این مشخصه نیز از کد منبع کوبرنتیز تولید می‌شود. اگر می‌خواهید مستندات مرجع API را تغییر دهید، نخستین گام تغییر یک یا چند توضیح (comment) در کد منبع کوبرنتیز است.

مستندات مؤلفه‌های `kube-*` نیز از کد منبع بالادستی تولید می‌شود. برای اصلاح مستندات تولیدشده، باید کد مربوط به مؤلفه‌ای را که می‌خواهید اصلاح کنید تغییر دهید.

### اعمال تغییرات در کد منبع بالادستی

{{< note >}}
مراحل زیر یک نمونه است، نه یک روال کلی. جزئیات در موقعیت شما متفاوت خواهد بود.
{{< /note >}}

در ادامه نمونه‌ای از ویرایش یک توضیح در کد منبع کوبرنتیز آمده است.

در مخزن محلی kubernetes/kubernetes خود، شاخهٔ پیش‌فرض را checkout کنید و مطمئن شوید که به‌روز است:

```shell
cd <k8s-base>
git checkout master
git pull https://github.com/kubernetes/kubernetes master
```

فرض کنید این فایل منبع در شاخهٔ پیش‌فرض، غلط املایی "atmost" را دارد:

[kubernetes/kubernetes/staging/src/k8s.io/api/apps/v1/types.go](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/api/apps/v1/types.go)

در محیط محلی خود، فایل `types.go` را باز کنید و "atmost" را به "at most" تغییر دهید.

بررسی کنید که فایل را تغییر داده‌اید:

```shell
git status
```

خروجی نشان می‌دهد که روی شاخهٔ master هستید و فایل منبع `types.go` تغییر کرده است:

```shell
On branch master
...
    modified:   staging/src/k8s.io/api/apps/v1/types.go
```

### کامیت کردن فایل ویرایش‌شده

دستورهای `git add` و `git commit` را اجرا کنید تا تغییراتی را که تاکنون اعمال کرده‌اید کامیت کنید. در مرحلهٔ بعد، یک کامیت دوم انجام خواهید داد. مهم است که تغییرات خود را در دو کامیت جداگانه نگه دارید.

### تولید مشخصهٔ OpenAPI و فایل‌های مرتبط

به `<k8s-base>` بروید و این اسکریپت‌ها را اجرا کنید:

```shell
./hack/update-codegen.sh
./hack/update-openapi-spec.sh
```

دستور `git status` را اجرا کنید تا ببینید چه فایل‌هایی تولید شده‌اند.

```shell
On branch master
...
    modified:   api/openapi-spec/swagger.json
    modified:   api/openapi-spec/v3/apis__apps__v1_openapi.json
    modified:   pkg/generated/openapi/zz_generated.openapi.go
    modified:   staging/src/k8s.io/api/apps/v1/generated.proto
    modified:   staging/src/k8s.io/api/apps/v1/types_swagger_doc_generated.go
```

محتوای `api/openapi-spec/swagger.json` را ببینید تا مطمئن شوید غلط املایی برطرف شده است. برای نمونه، می‌توانید دستور `git diff -a api/openapi-spec/swagger.json` را اجرا کنید. این کار اهمیت دارد، زیرا `swagger.json` ورودی مرحلهٔ دوم فرایند تولید مستندات است.

دستورهای `git add` و `git commit` را اجرا کنید تا تغییرات خود را کامیت کنید. اکنون دو کامیت دارید: یکی شامل فایل ویرایش‌شدهٔ `types.go` و دیگری شامل مشخصهٔ OpenAPI تولیدشده و فایل‌های مرتبط با آن. این دو کامیت را جدا از هم نگه دارید؛ یعنی کامیت‌های خود را squash نکنید.

تغییرات خود را به‌صورت یک [درخواست ادغام](https://help.github.com/articles/creating-a-pull-request/) به شاخهٔ master مخزن [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) ارسال کنید. درخواست ادغام خود را پیگیری کنید و در صورت نیاز به نظرهای بازبین‌ها پاسخ دهید. پیگیری درخواست ادغام را تا زمان ادغام شدن آن ادامه دهید.

[PR 57758](https://github.com/kubernetes/kubernetes/pull/57758) نمونه‌ای از یک درخواست ادغام است که یک غلط املایی را در کد منبع کوبرنتیز برطرف می‌کند.

{{< note >}}
تشخیص فایل منبع درستی که باید تغییر کند ممکن است دشوار باشد. در نمونهٔ قبل، فایل منبع معتبر در پوشهٔ `staging` در مخزن `kubernetes/kubernetes` قرار دارد. اما در موقعیت شما، ممکن است پوشهٔ `staging` جای یافتن منبع معتبر نباشد. برای راهنمایی، فایل‌های `README` را در مخزن [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/tree/master/staging) و در مخزن‌های مرتبط، مانند [kubernetes/apiserver](https://github.com/kubernetes/apiserver/blob/master/README.md)، بررسی کنید.
{{< /note >}}

### انتقال کامیت به یک شاخهٔ انتشار با cherry pick

در بخش قبل، فایلی را در شاخهٔ master ویرایش کردید و سپس اسکریپت‌هایی را برای تولید مشخصهٔ OpenAPI و فایل‌های مرتبط اجرا کردید. پس از آن، تغییرات خود را در قالب یک درخواست ادغام به شاخهٔ master مخزن kubernetes/kubernetes ارسال کردید. اکنون فرض کنید می‌خواهید تغییر خود را به یک شاخهٔ انتشار منتقل (backport) کنید. برای نمونه، فرض کنید شاخهٔ master برای توسعهٔ نسخهٔ {{< skew latestVersion >}} کوبرنتیز استفاده می‌شود و شما می‌خواهید تغییر خود را به شاخهٔ release-{{< skew prevMinorVersion >}} منتقل کنید.

به یاد داشته باشید که درخواست ادغام شما دو کامیت دارد: یکی برای ویرایش `types.go` و دیگری برای فایل‌هایی که اسکریپت‌ها تولید کرده‌اند. گام بعدی، پیشنهاد یک cherry pick از کامیت نخست به شاخهٔ release-{{< skew prevMinorVersion >}} است. هدف این است که کامیتی را که `types.go` را ویرایش کرده است cherry pick کنید، اما کامیتی را که نتایج اجرای اسکریپت‌ها را در بر دارد منتقل نکنید. برای دستورالعمل‌ها، [پیشنهاد یک Cherry Pick](https://git.k8s.io/community/contributors/devel/sig-release/cherry-picks.md) را ببینید.

{{< note >}}
برای پیشنهاد یک cherry pick، باید مجوز تعیین برچسب و نقطهٔ عطف (milestone) را در درخواست ادغام خود داشته باشید. اگر این مجوزها را ندارید، باید با کسی همکاری کنید که بتواند برچسب و نقطهٔ عطف را برای شما تعیین کند.
{{< /note >}}

هنگامی که درخواست ادغامی برای cherry pick کردن آن یک کامیت به شاخهٔ release-{{< skew prevMinorVersion >}} آماده کردید، گام بعدی اجرای این اسکریپت‌ها در شاخهٔ release-{{< skew prevMinorVersion >}} محیط محلی شماست.

```shell
./hack/update-codegen.sh
./hack/update-openapi-spec.sh
```

اکنون کامیتی را که شامل مشخصهٔ OpenAPI تازه تولیدشده و فایل‌های مرتبط است به درخواست ادغام cherry pick خود اضافه کنید. درخواست ادغام خود را تا زمانی که در شاخهٔ release-{{< skew prevMinorVersion >}} ادغام شود پیگیری کنید.

در این مرحله، هم شاخهٔ master و هم شاخهٔ release-{{< skew prevMinorVersion >}} فایل به‌روزشدهٔ `types.go` شما و مجموعه‌ای از فایل‌های تولیدشده را دارند که تغییر اعمال‌شده در `types.go` را بازتاب می‌دهند. توجه کنید که مشخصهٔ OpenAPI و دیگر فایل‌های تولیدشده در شاخهٔ release-{{< skew prevMinorVersion >}} لزوماً با فایل‌های تولیدشده در شاخهٔ master یکسان نیستند. فایل‌های تولیدشده در شاخهٔ release-{{< skew prevMinorVersion >}} فقط عناصر API مربوط به کوبرنتیز {{< skew prevMinorVersion >}} را در بر دارند. فایل‌های تولیدشده در شاخهٔ master ممکن است عناصری از API را داشته باشند که در {{< skew prevMinorVersion >}} وجود ندارند، اما برای {{< skew latestVersion >}} در حال توسعه هستند.

## تولید مستندات مرجع منتشرشده

بخش قبل نشان داد که چگونه یک فایل منبع را ویرایش کنید و سپس چندین فایل، از جمله `api/openapi-spec/swagger.json` را در مخزن `kubernetes/kubernetes` تولید کنید. فایل `swagger.json` همان فایل تعریف OpenAPI است که برای تولید مستندات مرجع API به کار می‌رود.

اکنون آماده‌اید تا راهنمای [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/) را دنبال کنید و [مستندات مرجع منتشرشدهٔ API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/) را تولید کنید.

## {{% heading "whatsnext" %}}

* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)
