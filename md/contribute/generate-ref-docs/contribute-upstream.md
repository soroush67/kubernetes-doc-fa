---
title: مشارکت در کد بالادستی (Upstream) کوبرنتیز
content_type: task
weight: 20
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه می‌توانید در پروژهٔ بالادستی `kubernetes/kubernetes` مشارکت کنید.
می‌توانید اشکالاتی را که در مستندات API کوبرنتیز یا در محتوای مؤلفه‌های کوبرنتیز مانند
`kubeadm`، `kube-apiserver` و `kube-controller-manager` یافته‌اید برطرف کنید.

اگر به‌جای آن می‌خواهید مستندات مرجع API کوبرنتیز یا مؤلفه‌های `kube-*` را از کد بالادستی دوباره تولید کنید،
دستورالعمل‌های زیر را ببینید:

- [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
- [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)

## {{% heading "prerequisites" %}}

- باید این ابزارها نصب شده باشند:

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  - [Golang](https://go.dev/doc/install) نسخهٔ 1.13 یا بالاتر
  - [Docker](https://docs.docker.com/engine/installation/)
  - [etcd](https://github.com/coreos/etcd/)
  - [make](https://www.gnu.org/software/make/)
  - [gcc compiler/linker](https://gcc.gnu.org/)

- متغیر محیطی `GOPATH` شما باید تنظیم شده باشد و مسیر `etcd`
  باید در متغیر محیطی `PATH` شما قرار داشته باشد.

- باید بدانید چگونه یک pull request برای یک مخزن GitHub ایجاد کنید.
  معمولاً این کار شامل ایجاد یک fork از مخزن است.
  برای اطلاعات بیشتر، [Creating a Pull Request](https://help.github.com/articles/creating-a-pull-request/)
  و [GitHub Standard Fork & Pull Request Workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962) را ببینید.

<!-- steps -->

## تصویر کلی

مستندات مرجع API کوبرنتیز و مؤلفه‌های `kube-*`
مانند `kube-apiserver` و `kube-controller-manager` به‌طور خودکار
از کد منبع [کوبرنتیز بالادستی](https://github.com/kubernetes/kubernetes/) تولید می‌شوند.

وقتی در مستندات تولیدشده با اشکالی مواجه می‌شوید، می‌توانید
ایجاد یک وصله (patch) برای رفع آن در پروژهٔ بالادستی را در نظر بگیرید.

## کلون کردن مخزن کوبرنتیز

اگر هنوز مخزن kubernetes/kubernetes را ندارید، اکنون آن را دریافت کنید:

```shell
mkdir $GOPATH/src
cd $GOPATH/src
go get github.com/kubernetes/kubernetes
```

دایرکتوری پایهٔ کلون مخزن
[kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) خود را مشخص کنید.
برای مثال، اگر مرحلهٔ قبل را برای دریافت مخزن دنبال کرده باشید،
دایرکتوری پایهٔ شما `$GOPATH/src/github.com/kubernetes/kubernetes` است.
در مراحل بعدی، به دایرکتوری پایهٔ شما با عنوان `<k8s-base>` اشاره می‌شود.

دایرکتوری پایهٔ کلون مخزن
[kubernetes-sigs/reference-docs](https://github.com/kubernetes-sigs/reference-docs) خود را مشخص کنید.
برای مثال، اگر مرحلهٔ قبل را برای دریافت مخزن دنبال کرده باشید،
دایرکتوری پایهٔ شما `$GOPATH/src/github.com/kubernetes-sigs/reference-docs` است.
در مراحل بعدی، به دایرکتوری پایهٔ شما با عنوان `<rdocs-base>` اشاره می‌شود.

## ویرایش کد منبع کوبرنتیز

مستندات مرجع API کوبرنتیز به‌طور خودکار از یک مشخصات OpenAPI تولید می‌شود
که خود از کد منبع کوبرنتیز تولید شده است. اگر
می‌خواهید مستندات مرجع API را تغییر دهید، گام نخست تغییر یک یا چند
توضیح (comment) در کد منبع کوبرنتیز است.

مستندات مؤلفه‌های `kube-*` نیز از کد منبع بالادستی تولید می‌شود.
برای اصلاح مستندات تولیدشده، باید کد مربوط به مؤلفه‌ای را که
می‌خواهید اصلاح کنید تغییر دهید.

### اعمال تغییرات در کد منبع بالادستی

{{< note >}}
مراحل زیر یک مثال هستند و یک روش کلی به شمار نمی‌آیند. جزئیات
در موقعیت شما متفاوت خواهد بود.
{{< /note >}}

در ادامه مثالی از ویرایش یک توضیح (comment) در کد منبع کوبرنتیز آمده است.

در مخزن محلی kubernetes/kubernetes خود، شاخهٔ پیش‌فرض را checkout کنید
و مطمئن شوید که به‌روز است:

```shell
cd <k8s-base>
git checkout master
git pull https://github.com/kubernetes/kubernetes master
```

فرض کنید این فایل منبع در آن شاخهٔ پیش‌فرض دارای غلط تایپی «atmost» است:

[kubernetes/kubernetes/staging/src/k8s.io/api/apps/v1/types.go](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/api/apps/v1/types.go)

در محیط محلی خود، فایل `types.go` را باز کنید و «atmost» را به «at most» تغییر دهید.

بررسی کنید که فایل را تغییر داده‌اید:

```shell
git status
```

خروجی نشان می‌دهد که در شاخهٔ master هستید و فایل منبع `types.go`
تغییر کرده است:

```shell
On branch master
...
    modified:   staging/src/k8s.io/api/apps/v1/types.go
```

### کامیت کردن فایل ویرایش‌شده

دستورهای `git add` و `git commit` را اجرا کنید تا تغییراتی را که تاکنون اعمال کرده‌اید کامیت کنید. در گام بعد،
کامیت دومی انجام خواهید داد. مهم است که تغییرات شما در دو کامیت جداگانه نگه داشته شوند.

### تولید مشخصات OpenAPI و فایل‌های مرتبط

به `<k8s-base>` بروید و این اسکریپت‌ها را اجرا کنید:

```shell
./hack/update-codegen.sh
./hack/update-openapi-spec.sh
```

دستور `git status` را اجرا کنید تا ببینید چه چیزی تولید شده است.

```shell
On branch master
...
    modified:   api/openapi-spec/swagger.json
    modified:   api/openapi-spec/v3/apis__apps__v1_openapi.json
    modified:   pkg/generated/openapi/zz_generated.openapi.go
    modified:   staging/src/k8s.io/api/apps/v1/generated.proto
    modified:   staging/src/k8s.io/api/apps/v1/types_swagger_doc_generated.go
```

محتوای فایل `api/openapi-spec/swagger.json` را بررسی کنید تا مطمئن شوید غلط تایپی برطرف شده است.
برای مثال، می‌توانید دستور `git diff -a api/openapi-spec/swagger.json` را اجرا کنید.
این کار مهم است، زیرا `swagger.json` ورودی مرحلهٔ دوم
فرایند تولید مستندات است.

دستورهای `git add` و `git commit` را اجرا کنید تا تغییرات خود را کامیت کنید. اکنون دو کامیت دارید:
یکی شامل فایل ویرایش‌شدهٔ `types.go` و دیگری شامل مشخصات OpenAPI تولیدشده
و فایل‌های مرتبط. این دو کامیت را جدا از هم نگه دارید. یعنی کامیت‌های خود را squash نکنید.

تغییرات خود را به‌صورت یک
[pull request](https://help.github.com/articles/creating-a-pull-request/)
به شاخهٔ master مخزن
[kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) ارسال کنید.
pull request خود را پایش کنید و در صورت لزوم به نظرات بازبینان پاسخ دهید. پایش pull request را
تا زمان ادغام (merge) شدن آن ادامه دهید.

[PR 57758](https://github.com/kubernetes/kubernetes/pull/57758)
نمونه‌ای از یک pull request است که یک غلط تایپی را در کد منبع کوبرنتیز اصلاح می‌کند.

{{< note >}}
تعیین فایل منبع درست برای تغییر ممکن است دشوار باشد. در مثال
بالا، فایل منبع مرجع در دایرکتوری `staging`
در مخزن `kubernetes/kubernetes` قرار دارد. اما در موقعیت شما، دایرکتوری `staging`
ممکن است محل مناسبی برای یافتن منبع مرجع نباشد. برای راهنمایی، فایل‌های
`README` را در مخزن
[kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/tree/master/staging)
و در مخازن مرتبط، مانند
[kubernetes/apiserver](https://github.com/kubernetes/apiserver/blob/master/README.md)، بررسی کنید.
{{< /note >}}

### Cherry pick کردن کامیت خود در یک شاخهٔ انتشار

در بخش قبل، فایلی را در شاخهٔ master ویرایش کردید و سپس اسکریپت‌ها را اجرا کردید
تا مشخصات OpenAPI و فایل‌های مرتبط تولید شوند. سپس تغییرات خود را در یک pull request
به شاخهٔ master مخزن kubernetes/kubernetes ارسال کردید. اکنون فرض کنید می‌خواهید
تغییر خود را به یک شاخهٔ انتشار backport کنید. برای مثال، فرض کنید شاخهٔ master برای توسعهٔ
کوبرنتیز نسخهٔ {{< skew latestVersion >}} استفاده می‌شود و می‌خواهید تغییر خود را به شاخهٔ
release-{{< skew prevMinorVersion >}} backport کنید.

به یاد داشته باشید که pull request شما دو کامیت دارد: یکی برای ویرایش `types.go`
و دیگری برای فایل‌هایی که اسکریپت‌ها تولید کرده‌اند. گام بعدی پیشنهاد cherry pick کامیت نخست شما
به شاخهٔ release-{{< skew prevMinorVersion >}} است. ایده این است که کامیتی را که
`types.go` را ویرایش کرده cherry pick کنید، نه کامیتی را که نتایج اجرای اسکریپت‌ها را دارد. برای دستورالعمل‌ها،
[Propose a Cherry Pick](https://git.k8s.io/community/contributors/devel/sig-release/cherry-picks.md) را ببینید.

{{< note >}}
پیشنهاد یک cherry pick مستلزم آن است که مجوز تنظیم برچسب و milestone را در
pull request خود داشته باشید. اگر این مجوزها را ندارید، باید با فردی همکاری کنید که بتواند برچسب
و milestone را برای شما تنظیم کند.
{{< /note >}}

هنگامی که یک pull request برای cherry pick کردن تک کامیت خود به شاخهٔ
release-{{< skew prevMinorVersion >}} ایجاد کردید، گام بعدی اجرای این اسکریپت‌ها در شاخهٔ
release-{{< skew prevMinorVersion >}} در محیط محلی شماست.

```shell
./hack/update-codegen.sh
./hack/update-openapi-spec.sh
```

اکنون یک کامیت که شامل مشخصات OpenAPI و فایل‌های مرتبطِ تازه تولیدشده است
به pull request مربوط به cherry-pick خود اضافه کنید. pull request خود را پایش کنید تا زمانی که در شاخهٔ
release-{{< skew prevMinorVersion >}} ادغام شود.

در این مرحله، هم شاخهٔ master و هم شاخهٔ release-{{< skew prevMinorVersion >}} فایل `types.go` به‌روزشدهٔ شما
و مجموعه‌ای از فایل‌های تولیدشده را دارند که تغییر شما در `types.go` را منعکس می‌کنند. توجه داشته باشید که
مشخصات OpenAPI تولیدشده و سایر فایل‌های تولیدشده در شاخهٔ release-{{< skew prevMinorVersion >}} لزوماً
با فایل‌های تولیدشده در شاخهٔ master یکسان نیستند. فایل‌های تولیدشده در شاخهٔ release-{{< skew prevMinorVersion >}}
فقط شامل عناصر API از کوبرنتیز {{< skew prevMinorVersion >}} هستند. فایل‌های تولیدشده در شاخهٔ master ممکن است شامل
عناصر API‌ای باشند که در {{< skew prevMinorVersion >}} وجود ندارند، اما برای {{< skew latestVersion >}} در دست توسعه‌اند.

## تولید مستندات مرجع منتشرشده

بخش قبل نشان داد چگونه یک فایل منبع را ویرایش کنید و سپس
چندین فایل، از جمله `api/openapi-spec/swagger.json` را در مخزن
`kubernetes/kubernetes` تولید کنید.
فایل `swagger.json` همان فایل تعریف OpenAPI است که برای تولید
مستندات مرجع API به کار می‌رود.

اکنون آمادهٔ آن هستید که راهنمای
[تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
را دنبال کنید تا
[مستندات مرجع منتشرشدهٔ API کوبرنتیز](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/)
را تولید کنید.

## {{% heading "whatsnext" %}}

* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
* [تولید مستندات مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)
