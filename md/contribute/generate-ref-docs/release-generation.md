---
title: تولید مستندات مرجع برای یک انتشار
linkTitle: تولید برای انتشار
content_type: task
weight: 15
---

<!-- overview -->

این صفحه توضیح می‌دهد که چگونه همهٔ مجموعه‌های مستندات مرجع کوبرنتیز را برای یک انتشار جدید از نو تولید کنید. همچنین نشان می‌دهد که خروجی تولیدشده را چگونه به چند درخواست ادغام (pull request) تقسیم کنید تا بازبین‌ها بتوانند آن‌ها را یکی‌یکی بررسی کنند.

بخش‌ها را به ترتیب دنبال کنید. هر مجموعهٔ مرجع بخش مخصوص خود را دارد. این بخش مجموعه را می‌سازد، آن را در کلون وب‌سایت شما کپی می‌کند و در پایان صفحه‌ای را برای بررسی معرفی می‌کند. به این ترتیب می‌توانید پیش از شروع مجموعهٔ بعدی، کار یک مجموعه را تمام کنید. بخش [خلاصه](#summary) در انتهای صفحه همهٔ هدف‌ها (target)، خروجی هر کدام و درخواست‌های ادغامی را که باید باز کنید فهرست می‌کند.

{{< note >}}
سرپرست مستندات تیم انتشار (Release Team Docs Lead) و دستیاران مستندات (Docs shadows) این فرایند را در طول هر چرخهٔ انتشار اجرا می‌کنند. [راهنمای نقش مستندات](https://github.com/kubernetes/sig-release/tree/master/release-team/role-handbooks/docs) در مخزن `kubernetes/sig-release` بقیهٔ وظایف این نقش را پوشش می‌دهد. اگر مراحلی مخصوص تولید مستندات مرجع به این راهنما اضافه شد، این صفحه را مطابق آن به‌روز کنید.
{{< /note >}}

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخزن‌های محلی

به کلون‌های محلی از مخزن‌های `kubernetes/website` و `kubernetes-sigs/reference-docs` نیاز دارید.

اگر هنوز مخزن `kubernetes/website` را fork و کلون نکرده‌اید، صفحهٔ [کار با یک کلون محلی](/docs/contribute/new-content/open-a-pr/#fork-the-repo) را ببینید. مخزن `reference-docs` را کلون کنید:

```shell
git clone https://github.com/kubernetes-sigs/reference-docs
```

در ادامهٔ مراحل، کلون `kubernetes/website` شما با `<web-base>` و کلون `reference-docs` شما با `<rdocs-base>` مشخص می‌شود.

## تنظیم متغیرهای ساخت

این متغیرها را در پوستهٔ (shell) خود تنظیم کنید. این مقادیر برای همهٔ فرمان‌های `make` در مراحل بعدی اعمال می‌شوند.

```shell
export K8S_WEBROOT=<your-path-to>/website     # your website clone (<web-base>)
export K8S_RELEASE={{< skew currentVersionAddMinor 1 >}}.0
```

مقدار `K8S_RELEASE` را برابر یک نسخهٔ کامل انتشار قرار دهید، مانند `{{< skew currentVersionAddMinor 1 >}}.0` یا `{{< skew currentVersionAddMinor 1 >}}.0-rc.1`. هدف‌های ساخت نام دایرکتوری نسخه‌دار را، مانند `v{{< skew currentVersionAddMinor 1 "_" >}}`، از نسخهٔ اصلی (major) و فرعی (minor) به دست می‌آورند.

## ایجاد دایرکتوری‌های نسخه‌دار

این فرمان را در `<rdocs-base>` اجرا کنید:

```shell
make createversiondirs
```

این فرمان دایرکتوری پیکربندی انتشار جدید را زیر `gen-apidocs/config/` ایجاد می‌کند و فایل `config.yaml` را از انتشار قبلی در آن کپی می‌کند.

به‌ندرت لازم است این فایل را ویرایش کنید. تنظیماتی که در هر انتشار تغییر می‌کنند، یعنی گروه‌های API و فهرست منابع، در این فایل خالی هستند. هدف‌های ساخت این صفحه گزینهٔ `--auto-detect` را ارسال می‌کنند و در نتیجه تولیدکننده این تنظیمات را از `swagger.json` می‌خواند. آنچه در فایل باقی می‌ماند، نام‌گذاری و حذف عملیات‌هاست که از سازوکار داخلی API (API machinery) پیروی می‌کند، نه از سطح API.

وقتی مرجع تولیدشده نادرست به نظر می‌رسد، تا جایی که می‌توانید علت را در [پروژهٔ بالادستی](/docs/contribute/generate-ref-docs/contribute-upstream/) برطرف کنید. توضیحات و اطلاعیه‌های منسوخ‌شدن از توضیحات کد Go در `kubernetes/kubernetes` می‌آیند و اصلاحی که آنجا انجام شود به دست همهٔ خوانندگان آن API می‌رسد. فایل `config.yaml` را فقط برای مواردی ویرایش کنید که تصمیم‌گیری دربارهٔ آن‌ها تنها با تولیدکننده است؛ مانند عملیاتی بدون عنوان (`operation_categories`)، نقطهٔ پایانی (endpoint) که مرجع نباید منتشر کند (`excluded_operations`)، یا گروهی که نامش در شناسه‌های عملیات به شکلی متفاوت از منابعش نوشته شده است (`operation_group_map`). هر مدخل به همهٔ انتشارهای بعدی منتقل می‌شود، پس فایل را تا حد ممکن کوچک نگه دارید.

## دریافت مشخصهٔ OpenAPI

تولیدکنندهٔ مرجع API فایل `gen-apidocs/config/<version>/swagger.json` را می‌خواند. مشخصه‌ای که در مخزن `kubernetes/kubernetes` کامیت می‌شود، مقادیر مجاز فیلدهای شمارشی (enumerated) را ندارد و بنابراین مرجعی که از آن ساخته شود نیز این مقادیر را نخواهد داشت. بهتر است مرجعی تولید کنید که مقادیر مجاز را فهرست کند و برای این کار باید چند مرحلهٔ اضافی را انجام دهید.

یکی از دو گزینهٔ زیر را انتخاب کنید.

### گزینهٔ ۱: تولید مشخصه از کد منبع

از این گزینه استفاده کنید، مگر اینکه نتوانید نیازمندی‌های زیر را فراهم کنید. این گزینه به کلون شخصی از `kubernetes/kubernetes` نیاز ندارد، به کلونی که از قبل دارید دست نمی‌زند و مشخصه‌ای تولید می‌کند که مقادیر enum را در بر دارد.

```shell
make updateapispec-enums-from-source
```

این هدف مخزن `kubernetes/kubernetes` را در تگ `v$K8S_RELEASE` به‌صورت سطحی (shallow) در یک دایرکتوری موقت کلون می‌کند و اسکریپت بالادستی `hack/update-openapi-spec.sh` را در آنجا با حفظ مقادیر enum اجرا می‌کند. سپس مشخصهٔ حاصل را در دایرکتوری پیکربندی نسخه‌دار کپی می‌کند، بررسی می‌کند که مقادیر enum را در بر داشته باشد و در پایان نسخهٔ checkout‌شده را حذف می‌کند. این هدف علاوه بر ابزارهای ذکرشده در پیش‌نیازها، به موارد زیر نیاز دارد:

* ابزارهای `jq`، `curl` و `openssl` در `PATH` شما
* دسترسی به شبکه، برای کلون کردن تگ و دانلود ماژول‌های Go و etcd
* پورت‌های TCP آزاد 2379 و 8050

اسکریپت بالادستی etcd را روی پورت 2379 و یک API server موقت را روی پورت 8050 راه‌اندازی می‌کند. اگر هر یک از این پورت‌ها اشغال است، `ETCD_PORT` یا `API_PORT` را تنظیم کنید. این اسکریپت نسخهٔ مخصوص خود از etcd را دانلود می‌کند و `kube-apiserver` را می‌سازد، پس انتظار داشته باشید اجرای اول چند دقیقه طول بکشد.

برای اینکه نسخهٔ موقت checkout‌شده و گزارش تولید را برای عیب‌یابی نگه دارید:

```shell
KEEP_TMP=1 make updateapispec-enums-from-source
```

### گزینهٔ ۲: تولید مشخصه در یک کلون محلی

این گزینه را زمانی به کار ببرید که از قبل کلونی از `kubernetes/kubernetes` دارید و کلون دومی نمی‌خواهید. در این حالت مرحلهٔ کلون کردن حذف می‌شود، اما همچنان همان تولیدکنندهٔ گزینهٔ ۱ را اجرا می‌کنید و این تولیدکننده کلون شما را تغییر می‌دهد.

پیش از ادامه، تغییرات موجود در کلون خود را commit یا stash کنید. مسیر زیر را با مسیر کلون محلی خود جایگزین کنید و سپس تگ انتشار را checkout کنید:

```shell
export K8S_ROOT="<your-path-to>/kubernetes"
cd "$K8S_ROOT"
git checkout "v$K8S_RELEASE"
```

سپس اسکریپت `hack/update-openapi-spec.sh` را با `KUBE_OPENAPI_SPEC_KEEP_ENUMS=true` اجرا کنید تا فایل `api/openapi-spec/swagger.json` از نو تولید شود. این کار به همان ابزارها و پورت‌های آزادی نیاز دارد که در گزینهٔ ۱ توضیح داده شد:

```shell
KUBE_OPENAPI_SPEC_KEEP_ENUMS=true hack/update-openapi-spec.sh
```

{{< note >}}
بدون `KUBE_OPENAPI_SPEC_KEEP_ENUMS=true`، مشخصه هیچ مقدار enum ندارد و مرجع API منتشرشده مقادیر ممکن هیچ‌یک از فیلدهای شمارشی را نشان نمی‌دهد.
{{< /note >}}

مشخصهٔ ازنوتولیدشده را از درخت کاری (working tree) کلون خود به دایرکتوری پیکربندی نسخه‌داری که پیش‌تر ایجاد کردید کپی کنید. به جای `<rdocs-base>` مسیر کلون `reference-docs` خود را قرار دهید:

```shell
cd "<rdocs-base>"
cp "$K8S_ROOT/api/openapi-spec/swagger.json" \
  gen-apidocs/config/v{{< skew currentVersionAddMinor 1 "_" >}}/swagger.json
```

پس از کپی، فایل‌های ازنوتولیدشده را در کلون خود به حالت قبل برگردانید. اسکریپت فایل `swagger.json` و فایل‌های OpenAPI v3 زیر `api/openapi-spec/` را با حفظ مقادیر enum بازنویسی کرده است و بنابراین این فایل‌ها دیگر با آنچه در `kubernetes/kubernetes` کامیت شده مطابقت ندارند. شما فقط به نسخه‌ای نیاز دارید که همین حالا کپی کردید. با بازگرداندن این فایل‌ها کلون شما تمیز می‌ماند و می‌توانید به شاخهٔ خود برگردید:

```shell
git -C "$K8S_ROOT" checkout -- api/openapi-spec
```

### بررسی مشخصه

هر گزینه‌ای را که به کار ببرید، می‌توانید هر زمان که بخواهید وجود مقادیر enum را در یک مشخصه بررسی کنید:

```shell
./hack/verify-enum-swagger.sh gen-apidocs/config/<version>/swagger.json
```

## راه‌اندازی پیش‌نمایش محلی

پیش‌نمایش را یک بار در ترمینال دوم راه‌اندازی کنید و بگذارید در حال اجرا بماند. هر بار که هدف‌های کپی صفحه‌ای را جایگزین می‌کنند، Hugo آن صفحه را دوباره بارگذاری می‌کند؛ بنابراین می‌توانید هر مجموعهٔ مرجع را بلافاصله پس از تولید بررسی کنید.

```shell
cd <web-base>
git submodule update --init --recursive --depth 1   # if not already done
make container-serve
```

سرور Hugo پیش‌نمایش را در نشانی `http://localhost:1313/` ارائه می‌کند.

{{< note >}}
کار روی هر مجموعه را از یک شاخهٔ به‌روز در `<web-base>` شروع کنید، آن را تولید کنید، در پیش‌نمایش بررسی کنید و سپس commit کنید. بخش [درخواست‌های ادغام](#pull-requests) مشخص می‌کند که برای هر مجموعه چه درخواستی، در چه زمانی و با چه توضیحی باید باز شود.
{{< /note >}}

## تولید مرجع API کوبرنتیز

ابزار `gen-apidocs` این مجموعه، یعنی مرجع HTML برای API، را از مشخصهٔ OpenAPI که دریافت کردید می‌سازد. خروجی ساخت پیش از آنکه هدف آن را کپی کند، در `gen-apidocs/build/html/` قرار می‌گیرد.

```shell
cd <rdocs-base>
make copyapi
```

این هدف دو فایل در `<web-base>` می‌نویسد:

```
static/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/index.html
static/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/js/navData.js
```

مسیر `/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/` را در پیش‌نمایش بررسی کنید. منبعی مانند Pod را باز کنید و عبارت `Possible enum values` را در صفحه جست‌وجو کنید؛ وجود این عبارت تأیید می‌کند که مقادیر enum از طریق مشخصه به مرجع رسیده‌اند.

برای اینکه بدانید برای این مجموعه چه درخواستی باید باز کنید، بخش [درخواست‌های ادغام](#pull-requests) را ببینید.

## تولید صفحه‌های مرجع API در قالب Markdown

ابزار `gen-apidocs` این مجموعه را نیز از همان مشخصه می‌سازد؛ یعنی مرجع API در قالب Markdown که Hugo آن را به شکل صفحه‌های عادی نمایش می‌دهد. خروجی ساخت در `gen-apidocs/build/markdown/` قرار می‌گیرد.

```shell
cd <rdocs-base>
make copyapimd
```

این هدف محتوای `<web-base>/content/en/docs/reference/kubernetes-api/` را جایگزین می‌کند و فایل `_index.md` را که به‌صورت دستی نگهداری می‌شود حفظ می‌کند.

مسیر `/docs/reference/kubernetes-api/` را در پیش‌نمایش بررسی کنید. تعداد صفحه‌های تولیدشده را با انتشار قبلی مقایسه کنید:

```shell
find <web-base>/content/en/docs/reference/kubernetes-api -name '*.md' | wc -l
```

برای اینکه بدانید برای این مجموعه چه درخواستی باید باز کنید، بخش [درخواست‌های ادغام](#pull-requests) را ببینید.

## تولید مرجع کامپوننت‌ها

ابزار `gen-compdocs` خروجی خود را از `k8s.io/kubernetes` و از ماژول‌های staging در `k8s.io` می‌سازد که فایل `go.mod` نسخهٔ آن‌ها را با دستورهای `replace` تثبیت می‌کند. فرمان `go get` اولی را به‌روز می‌کند و بقیه را تغییر نمی‌دهد، پس نسخهٔ کل مجموعه را یک‌جا ارتقا دهید:

```shell
cd <rdocs-base>/gen-compdocs
STAGING=v0.${K8S_RELEASE#*.}
go get k8s.io/kubernetes@v$K8S_RELEASE
KK=$(go list -m -f '{{.Dir}}' k8s.io/kubernetes)

# every staging module of this release
for m in $(awk '/=> \.\/staging\/src\//{print $1}' "$KK/go.mod"); do
  go mod edit -replace="$m=$m@$STAGING" -require="$m@$STAGING"
done

# entries left from a release with a different set of staging modules
for m in $(go mod edit -json | jq -r '.Replace[].Old.Path'); do
  grep -q "$m => ./staging/src/$m" "$KK/go.mod" ||
    go mod edit -dropreplace="$m" -droprequire="$m"
done

go mod tidy
go mod edit -go=$(go list -m -f '{{.GoVersion}}' k8s.io/kubernetes)
go mod tidy
```

{{< note >}}
اگر فرمان `go get` یا `go mod tidy` برای یکی از ماژول‌های `k8s.io` خطای `unknown revision` یا خطای 404 از `sum.golang.org` گزارش کرد، ماژول‌های staging این انتشار هنوز منتشر نشده‌اند. این ماژول‌ها چند ساعت پس از تگ `kubernetes/kubernetes` منتشر می‌شوند. با این فرمان بررسی کنید:

```shell
git ls-remote --tags https://github.com/kubernetes/api.git "v0.${K8S_RELEASE#*.}"
```

اگر نتیجه خالی بود، باید صبر کنید. این موضوع دربارهٔ مرجع API پیکربندی نیز صدق می‌کند. دو مجموعهٔ مرجع API فقط مشخصهٔ OpenAPI را می‌خوانند، پس می‌توانید در این فاصله آن‌ها را تولید کنید.
{{< /note >}}

حلقه‌ها مجموعهٔ ماژول‌ها را از `kubernetes/kubernetes` می‌خوانند، زیرا انتشارها ماژول‌های staging را اضافه و حذف می‌کنند و ممکن است `go.mod` هنوز ماژول‌هایی از یک انتشار قدیمی‌تر را فهرست کند. دستور `go` در آخر تنظیم می‌شود، چون تا وقتی ماژول‌های قدیمی هنوز در گراف وابستگی‌ها باشند، `go mod tidy` آن را دوباره بالا می‌برد.

تغییرات را بررسی کنید:

```shell
git diff go.mod
```

اکنون همهٔ وابستگی‌های `k8s.io`، همهٔ دستورهای `replace` و دستور `go` باید با انتشار جدید مطابقت داشته باشند. وابستگی‌های خارج از مجموعهٔ staging، مانند `k8s.io/klog/v2` و بسته‌های Goldmark، نسخه‌های خود را حفظ می‌کنند.

سپس صفحه‌های کامپوننت‌های اصلی را بسازید و کپی کنید:

```shell
cd <rdocs-base>
make copycomp-core
```

ابزار `gen-compdocs` همهٔ صفحه‌های کامپوننت‌ها را در `gen-compdocs/build/` می‌نویسد و این هدف فایل‌های `kube-apiserver.md`، `kube-controller-manager.md`، `kube-scheduler.md`، `kube-proxy.md` و `kubelet.md` را از آنجا به `<web-base>/content/en/docs/reference/command-line-tools-reference/` کپی می‌کند.

مسیر `/docs/reference/command-line-tools-reference/` را در پیش‌نمایش بررسی کنید.

برای اینکه بدانید برای این مجموعه چه درخواستی باید باز کنید، بخش [درخواست‌های ادغام](#pull-requests) را ببینید.

{{< note >}}
مرجع کامپوننت‌ها، kubectl و kubeadm سه درخواست ادغام جداگانه هستند، هرچند هر سه را `gen-compdocs` تولید می‌کند. هر هدف `copycomp-*` ابتدا همهٔ صفحه‌های کامپوننت‌ها را از نو می‌سازد و این کار چند دقیقه طول می‌کشد. برای اینکه فقط یک بار بسازید و هر سه مجموعه را کپی کنید، `make copycomp` را اجرا کنید و سپس نتیجه را به سه شاخه تقسیم کنید.
{{< /note >}}

## تولید مرجع kubectl

صفحه‌های kubectl از همان ساخت `gen-compdocs` به دست می‌آیند که مرجع کامپوننت‌ها از آن تولید می‌شود، اما باید در درخواست ادغام جداگانهٔ خود قرار بگیرند.

```shell
cd <rdocs-base>
make copycomp-kubectl
```

این هدف فایل `kubectl.md` و یک دایرکتوری برای هر زیرفرمان را در `<web-base>/content/en/docs/reference/kubectl/generated/` می‌نویسد و فایل `_index.md` را که به‌صورت دستی نگهداری می‌شود حفظ می‌کند.

مسیر `/docs/reference/kubectl/generated/` را در پیش‌نمایش بررسی کنید و صفحهٔ یکی از زیرفرمان‌ها، مانند `kubectl apply`، را باز کنید.

برای اینکه بدانید برای این مجموعه چه درخواستی باید باز کنید، بخش [درخواست‌های ادغام](#pull-requests) را ببینید.

## تولید مرجع kubeadm

صفحه‌های kubeadm نیز از `gen-compdocs` به دست می‌آیند و باید در درخواست ادغام جداگانهٔ خود قرار بگیرند.

```shell
cd <rdocs-base>
make copycomp-kubeadm
```

این هدف فایل `kubeadm.md` و یک دایرکتوری برای هر زیرفرمان را در `<web-base>/content/en/docs/reference/setup-tools/kubeadm/generated/` می‌نویسد و فایل‌های `_index.md` و `README.md` را که به‌صورت دستی نگهداری می‌شوند حفظ می‌کند.

مسیر `/docs/reference/setup-tools/kubeadm/generated/` را در پیش‌نمایش بررسی کنید.

برای اینکه بدانید برای این مجموعه چه درخواستی باید باز کنید، بخش [درخواست‌های ادغام](#pull-requests) را ببینید.

## تولید مرجع API پیکربندی

ابزار `genref` نوع‌های پیکربندی Go هر کامپوننت را از ماژول‌های staging در `k8s.io` می‌خواند. این ابزار هیچ دستور `replace` ندارد، پس فقط وابستگی‌ها تعیین می‌کنند که کدام انتشار را مستند می‌کنید:

```shell
cd <rdocs-base>/genref
STAGING=v0.${K8S_RELEASE#*.}
OLD=$(go mod edit -json | jq -r '.Require[] | select(.Path=="k8s.io/api") | .Version')

# every k8s.io module pinned to the previous release
go get $(go mod edit -json | jq -r --arg v "$OLD" --arg s "$STAGING" \
  '.Require[] | select(.Version==$v and (.Path|startswith("k8s.io/"))) | .Path + "@" + $s')

go mod tidy
go mod edit -go=$(go list -m -f '{{.GoVersion}}' k8s.io/api)
go mod tidy
```

انتخاب بر اساس نسخهٔ قدیمی، ماژول‌های staging را در بر می‌گیرد و به `k8s.io/klog/v2`، `k8s.io/gengo` و دیگر مخزن‌های مستقل دست نمی‌زند. تغییرات را بررسی کنید:

```shell
git diff go.mod
```

همچنین نسخهٔ انتشار را در مقصد پیوند `externalPackages` در فایل `genref/config.yaml` به‌روز کنید؛ این پیوند خوانندگان را به مرجع API منتشرشده هدایت می‌کند.

### بررسی نسخه‌های جدید API

ابزار `genref` برای هر مدخل در `genref/config.yaml` یک صفحه تولید می‌کند و هر مدخل یک بستهٔ Go و مسیری را مشخص می‌کند که به یک نسخهٔ API ختم می‌شود:

```yaml
  - name: kubelet-config
    title: Kubelet Configuration (v1)
    package: k8s.io/kubelet
    path: config/v1
```

کامپوننتی که ارائهٔ نسخهٔ جدیدی از API پیکربندی خود را آغاز می‌کند، یک دایرکتوری نسخه به کد منبع Go خود اضافه می‌کند. برای دیدن نسخه‌های موجود در این انتشار، دایرکتوری‌های نسخهٔ یک کامپوننت را فهرست کنید:

```shell
cd <rdocs-base>/genref
go mod download
ls "$(go list -m -f '{{.Dir}}' k8s.io/kubelet)/config"
```

برای اینکه همهٔ مدخل‌های `config.yaml` را یک‌جا با کد منبع مقایسه کنید، فرمان زیر را اجرا کنید:

```shell
awk '$1=="package:"{pkg=$2} $1=="path:"{print pkg, $2}' config.yaml | sort -u |
while read -r pkg path; do
  dir=$(go list -m -f '{{.Dir}}' "$pkg" 2>/dev/null) || continue
  parent=$(dirname "$path")
  for v in $(find "$dir/$parent" -maxdepth 1 -mindepth 1 -type d -name 'v[0-9]*'); do
    grep -q "path: $parent/$(basename "$v")\$" config.yaml ||
      echo "$pkg $parent/$(basename "$v")"
  done
done | sort -u
```

هر خط یک گزینهٔ احتمالی است، نه کمبودی که حتماً باید پر شود. چند نسخهٔ قدیمی‌تر عمداً کنار گذاشته شده‌اند و دلیل آن در توضیحات `config.yaml` ثبت شده است. وقتی کامپوننتی نسخه‌ای را ارائه می‌کند که خوانندگان آن را پیکربندی می‌کنند، مدخلی برای آن اضافه کنید و تا زمانی که کامپوننت هنوز نسخهٔ قدیمی‌تری را ارائه می‌کند، مدخل آن را نگه دارید.

### ساخت و کپی صفحه‌ها

```shell
cd <rdocs-base>
make copyconfigapi
```

ابزار `genref` صفحه‌های تولیدشده را در `genref/output/md/` می‌نویسد و هدف هنگام کپی، آن‌ها را دسته‌بندی می‌کند: بیشتر صفحه‌ها به `content/en/docs/reference/config-api/` می‌روند؛ صفحه‌های APIهای metrics به `content/en/docs/reference/external-api/` می‌روند، زیرا پروژه آن‌ها را تعریف می‌کند اما از طریق API server ارائه نمی‌دهد؛ و صفحه‌هایی که وب‌سایت منتشر نمی‌کند نادیده گرفته می‌شوند.

هر دو بخش را در پیش‌نمایش بررسی کنید و مطمئن شوید هیچ صفحه‌ای که برای انتشار قبلی منتشر کرده بودید حذف نشده است:

```shell
cd <web-base>
git status content/en/docs/reference/config-api/ content/en/docs/reference/external-api/
```

برای اینکه بدانید برای این مجموعه چه درخواستی باید باز کنید، بخش [درخواست‌های ادغام](#pull-requests) را ببینید.

## خلاصه

{{< table caption="مجموعه‌های مرجع، مولدی که هر کدام را می‌سازد و محل قرار گرفتن خروجی آن" >}}
| مجموعهٔ مرجع | مولد در `<rdocs-base>` | هدف | خروجی در `<web-base>` |
| --- | --- | --- | --- |
| مرجع API کوبرنتیز، HTML | `gen-apidocs` | `make copyapi` | `static/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/` |
| مرجع API کوبرنتیز، Markdown | `gen-apidocs` | `make copyapimd` | `content/en/docs/reference/kubernetes-api/` |
| مؤلفه‌ها | `gen-compdocs` | `make copycomp-core` | `content/en/docs/reference/command-line-tools-reference/` |
| مرجع kubectl | `gen-compdocs` | `make copycomp-kubectl` | `content/en/docs/reference/kubectl/generated/` |
| مرجع kubeadm | `gen-compdocs` | `make copycomp-kubeadm` | `content/en/docs/reference/setup-tools/kubeadm/generated/` |
| APIهای پیکربندی | `genref` | `make copyconfigapi` | `content/en/docs/reference/config-api/`، `content/en/docs/reference/external-api/` |
{{< /table >}}

هر هدف کپی، پیش از کپی کردن، ابتدا مجموعهٔ مربوط را می‌سازد. برای ساختن همهٔ
مجموعه‌ها بدون کپی کردن چیزی در نسخهٔ کلون‌شدهٔ وبسایت، دستور
`make api apimd comp configapi` را اجرا کنید.

### درخواست‌های ادغام

هر مجموعهٔ مرجع درخواست ادغام (pull request) جداگانه‌ای در مخزن وبسایت دارد که
در مجموع شش درخواست می‌شود؛ سمت مولدها نیز به سه درخواست ادغام نیاز دارد. هر
درخواست ادغام وبسایت را همراه با درخواست ادغام `reference-docs` که به آن وابسته
است باز کنید و تا زمانی که آن درخواست ادغام نشده است، درخواست وبسایت را نگه دارید.

{{< table caption="درخواست‌های ادغامی که باید برای هر مجموعهٔ مرجع باز شوند" >}}
| مجموعهٔ مرجع | درخواست ادغام در `kubernetes-sigs/reference-docs` | درخواست ادغام در `kubernetes/website` |
| --- | --- | --- |
| مرجع API کوبرنتیز، HTML | پوشهٔ `gen-apidocs/config/<version>/`، یعنی پیکربندی و مشخصه: یک درخواست ادغام برای هر دو مجموعهٔ API | `Update the Kubernetes API reference for v{{< skew currentVersionAddMinor 1 >}}` |
| مرجع API کوبرنتیز، Markdown | همان درخواست ادغام `gen-apidocs` | `Update the generated API reference pages for v{{< skew currentVersionAddMinor 1 >}}` |
| مؤلفه‌ها | فایل‌های `gen-compdocs/go.mod` و `go.sum`: یک درخواست ادغام برای مجموعه‌های مؤلفه‌ها، kubectl و kubeadm | `Update the component reference for v{{< skew currentVersionAddMinor 1 >}}` |
| مرجع kubectl | همان درخواست ادغام `gen-compdocs` | `Update the kubectl reference for v{{< skew currentVersionAddMinor 1 >}}` |
| مرجع kubeadm | همان درخواست ادغام `gen-compdocs` | `Update the kubeadm reference for v{{< skew currentVersionAddMinor 1 >}}` |
| APIهای پیکربندی | مسیرهای `genref/go.mod`، `genref/config.yaml` و `genref/output/md/`: یک درخواست ادغام | `Update the configuration API reference for v{{< skew currentVersionAddMinor 1 >}}` |
{{< /table >}}

در هر درخواست ادغام وبسایت توضیح دهید که خروجی را چگونه تولید کرده‌اید تا
بازبین بتواند آن را بازتولید کند:

```text
Regenerated the kubectl reference for v{{< skew currentVersionAddMinor 1 >}}.0.

- Generated with `make copycomp-kubectl` from kubernetes-sigs/reference-docs at commit <commit>
- Generator changes: kubernetes-sigs/reference-docs#<pull request>
- Generated files only, with no hand edits
```

برای دو مجموعهٔ مرجع API، روش تولید مشخصهٔ OpenAPI را نیز بنویسید، زیرا خروجی
تولیدشده این موضوع را نشان نمی‌دهد: `generated from source with make updateapispec-enums-from-source`
یا `generated in a local clone with KUBE_OPENAPI_SPEC_KEEP_ENUMS=true`.

{{< caution >}}
صفحه‌های تولیدشده را به‌صورت دستی ویرایش نکنید، زیرا انتشار بعدی این ویرایش را
بازنویسی می‌کند. به‌جای آن، متن را [در پروژهٔ بالادستی](/docs/contribute/generate-ref-docs/contribute-upstream/)
یا در مولد اصلاح کنید.
{{< /caution >}}

## {{% heading "whatsnext" %}}

* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
* [تولید مستندات مرجع برای APIهای پیکربندی](/docs/contribute/generate-ref-docs/config-api/)
* [تولید صفحه‌های مرجع برای مؤلفه‌ها و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای فرمان‌های kubectl](/docs/contribute/generate-ref-docs/kubectl/)
* [تولید مستندات مرجع برای متریک‌ها](/docs/contribute/generate-ref-docs/metrics-reference/)
* [مشارکت در کد بالادستی کوبرنتیز](/docs/contribute/generate-ref-docs/contribute-upstream/)
* [راهنمای نقش مستندات](https://github.com/kubernetes/sig-release/tree/master/release-team/role-handbooks/docs)
  در `kubernetes/sig-release`
