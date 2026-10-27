---
title: تولید مستندات مرجع برای یک نسخه
linkTitle: تولید نسخه
content_type: task
weight: 15
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه همه مجموعه‌های مستندات مرجع کوبرنتیز را برای یک نسخه جدید دوباره تولید کنید و چگونه خروجی تولیدشده را به pull requestهایی تقسیم کنید که بازبین‌ها بتوانند هر بار یکی از آن‌ها را بررسی کنند.

بخش‌ها را به ترتیب پیش بروید. هر مجموعه مرجع بخش مخصوص به خود را دارد که آن را می‌سازد، در کلون وب‌سایت شما کپی می‌کند و با صفحه‌ای برای بررسی پایان می‌یابد؛ بنابراین می‌توانید پیش از شروع مجموعه بعدی، کار یک مجموعه را به پایان برسانید. [خلاصه](#summary) در انتهای صفحه، همه targetها، خروجی هر یک و pull requestهایی را که باید باز شوند فهرست می‌کند.

{{< note >}}
Release Team Docs Lead و Docs shadowها این فرایند را در طول یک چرخه انتشار اجرا می‌کنند. [راهنمای نقش Docs](https://github.com/kubernetes/sig-release/tree/master/release-team/role-handbooks/docs) در `kubernetes/sig-release` سایر وظایف این نقش را پوشش می‌دهد. اگر این راهنما مراحل مخصوص خود را برای تولید مستندات مرجع اضافه کرد، این صفحه را مطابق با آن به‌روزرسانی کنید.
{{< /note >}}

## {{% heading "prerequisites" %}}

{{< include "prerequisites-ref-docs.md" >}}

<!-- steps -->

## راه‌اندازی مخازن محلی

به کلون‌های محلی `kubernetes/website` و `kubernetes-sigs/reference-docs` نیاز دارید.

اگر هنوز `kubernetes/website` را fork و clone نکرده‌اید، [کار با یک کلون محلی](/docs/contribute/new-content/open-a-pr/#fork-the-repo) را ببینید.
مخزن `reference-docs` را clone کنید:

```shell
git clone https://github.com/kubernetes-sigs/reference-docs
```

در مراحل باقی‌مانده، کلون `kubernetes/website` شما با `<web-base>` و کلون `reference-docs` شما با `<rdocs-base>` نشان داده می‌شود.

## تنظیم متغیرهای ساخت

این متغیرها را در شل خود تنظیم کنید. آن‌ها برای هر دستور `make` در مراحل بعدی اعمال می‌شوند.

```shell
export K8S_WEBROOT=<your-path-to>/website     # your website clone (<web-base>)
export K8S_RELEASE={{< skew currentVersionAddMinor 1 >}}.0
```

مقدار `K8S_RELEASE` را روی یک نسخه کامل انتشار تنظیم کنید، مانند `{{< skew currentVersionAddMinor 1 >}}.0` یا `{{< skew currentVersionAddMinor 1 >}}.0-rc.1`. targetهای ساخت نام دایرکتوری نسخه‌دار، مانند `v{{< skew currentVersionAddMinor 1 "_" >}}`، را از نسخه major و minor استخراج می‌کنند.

## ایجاد دایرکتوری‌های نسخه‌دار

این دستور را در `<rdocs-base>` اجرا کنید:

```shell
make createversiondirs
```

این دستور دایرکتوری پیکربندی نسخه جدید را زیر `gen-apidocs/config/` ایجاد می‌کند و فایل `config.yaml` را از نسخه قبلی در آن کپی می‌کند.

به‌ندرت نیاز دارید این فایل را ویرایش کنید. تنظیماتی که با هر انتشار تغییر می‌کنند، یعنی گروه‌های API و فهرست منابع، در این فایل خالی هستند: targetهای ساخت در این صفحه گزینه `--auto-detect` را می‌دهند، بنابراین تولیدکننده آن‌ها را از `swagger.json` می‌خواند. آنچه در فایل باقی می‌ماند نام‌گذاری و حذف عملیات است که از ساختار API machinery پیروی می‌کند، نه از سطح API.

وقتی مرجع تولیدشده نادرست به نظر می‌رسد، در صورت امکان علت را [در بالادست (upstream)](/docs/contribute/generate-ref-docs/contribute-upstream/) برطرف کنید: توضیحات و اعلان‌های منسوخ‌شدن از کامنت‌های Go در `kubernetes/kubernetes` می‌آیند و اصلاح در آنجا به همه خوانندگان آن API می‌رسد. فایل `config.yaml` را فقط برای مواردی ویرایش کنید که تنها تولیدکننده درباره آن‌ها تصمیم می‌گیرد، مانند عملیاتی بدون عنوان (`operation_categories`)، نقطه پایانی که مرجع نباید آن را منتشر کند (`excluded_operations`)، یا گروهی که شناسه‌های عملیات آن با منابعش به شکل دیگری نوشته شده‌اند (`operation_group_map`). هر مورد در همه انتشارهای بعدی نیز منتقل می‌شود، پس فایل را مختصر نگه دارید.

## دریافت مشخصات OpenAPI

تولیدکننده مرجع API فایل `gen-apidocs/config/<version>/swagger.json` را می‌خواند. مشخصاتی که `kubernetes/kubernetes` commit می‌کند مقادیر مجاز فیلدهای enum را ندارد، بنابراین مرجعی که از آن ساخته شود نیز آن مقادیر را ندارد. بهتر است مرجعی تولید شود که مقادیر مجاز را فهرست کند؛ به همین دلیل چند گام اضافی برمی‌دارید.

یکی از دو گزینه زیر را انتخاب کنید.

### گزینه ۱: تولید مشخصات از سورس

از این گزینه استفاده کنید، مگر اینکه نتوانید الزامات زیر را برآورده کنید. این گزینه به هیچ کلون شخصی از `kubernetes/kubernetes` نیاز ندارد، کلون‌های موجود شما را دست‌نخورده می‌گذارد و مشخصاتی تولید می‌کند که مقادیر enum را شامل می‌شود.

```shell
make updateapispec-enums-from-source
```

این target یک shallow clone از `kubernetes/kubernetes` را در تگ `v$K8S_RELEASE` در یک دایرکتوری موقت می‌گیرد، اسکریپت upstream با نام `hack/update-openapi-spec.sh` را در آنجا با حفظ مقادیر enum اجرا می‌کند، مشخصات حاصل را در دایرکتوری پیکربندی نسخه‌دار کپی می‌کند، بررسی می‌کند که شامل مقادیر enum باشد و سپس checkout را حذف می‌کند. علاوه بر ابزارهای ذکرشده در پیش‌نیازها، به موارد زیر نیاز دارد:

* `jq`، `curl` و `openssl` در `PATH` شما
* دسترسی به شبکه، برای clone کردن تگ و دانلود ماژول‌های Go و etcd
* آزاد بودن پورت‌های TCP شماره 2379 و 8050

اسکریپت upstream برنامه etcd را روی پورت 2379 و یک API server موقت را روی پورت 8050 راه‌اندازی می‌کند؛ اگر هر یک از این پورت‌ها اشغال است، `ETCD_PORT` یا `API_PORT` را تنظیم کنید. این اسکریپت نسخه مخصوص خود از etcd را دانلود می‌کند و `kube-apiserver` را می‌سازد، پس انتظار داشته باشید اجرای اول چند دقیقه طول بکشد.

برای نگه داشتن checkout موقت و گزارش تولید به‌منظور عیب‌یابی:

```shell
KEEP_TMP=1 make updateapispec-enums-from-source
```

### گزینه ۲: تولید مشخصات در یک کلون محلی

از این گزینه زمانی استفاده کنید که از قبل یک کلون `kubernetes/kubernetes` دارید و نمی‌خواهید کلون دومی داشته باشید. clone کردن را رد می‌کنید، اما همچنان همان تولیدکننده گزینه ۱ را اجرا می‌کنید و این کار کلون شما را تغییر می‌دهد.

پیش از ادامه، هر تغییر موجود در کلون خود را commit یا stash کنید. مسیر زیر را با مسیر کلون محلی خود جایگزین کنید و سپس تگ انتشار را checkout کنید:

```shell
export K8S_ROOT="<your-path-to>/kubernetes"
cd "$K8S_ROOT"
git checkout "v$K8S_RELEASE"
```

سپس `hack/update-openapi-spec.sh` را با `KUBE_OPENAPI_SPEC_KEEP_ENUMS=true` اجرا کنید تا `api/openapi-spec/swagger.json` دوباره تولید شود. این کار به ابزارها و پورت‌های آزادی نیاز دارد که در گزینه ۱ توضیح داده شد:

```shell
KUBE_OPENAPI_SPEC_KEEP_ENUMS=true hack/update-openapi-spec.sh
```

{{< note >}}
بدون `KUBE_OPENAPI_SPEC_KEEP_ENUMS=true`، مشخصات هیچ مقدار enum ندارد و مرجع API منتشرشده، مقادیر ممکن هر فیلد enum را حذف می‌کند.
{{< /note >}}

مشخصات دوباره تولیدشده را از working tree کلون خود در دایرکتوری پیکربندی نسخه‌داری که پیش‌تر ایجاد شد کپی کنید. `<rdocs-base>` را با مسیر کلون `reference-docs` خود جایگزین کنید:

```shell
cd "<rdocs-base>"
cp "$K8S_ROOT/api/openapi-spec/swagger.json" \
  gen-apidocs/config/v{{< skew currentVersionAddMinor 1 "_" >}}/swagger.json
```

پس از کپی، فایل‌های دوباره تولیدشده را در کلون خود بازیابی (restore) کنید. اسکریپت، `swagger.json` و فایل‌های OpenAPI v3 زیر `api/openapi-spec/` را با حفظ مقادیر enum بازنویسی کرد، بنابراین دیگر با آنچه `kubernetes/kubernetes` commit می‌کند مطابقت ندارند. فقط به نسخه‌ای که همین حالا کپی کردید نیاز دارید و بازیابی فایل‌ها کلون شما را تمیز می‌گذارد، بنابراین می‌توانید به شاخه خودتان برگردید:

```shell
git -C "$K8S_ROOT" checkout -- api/openapi-spec
```

### بررسی مشخصات

هر گزینه‌ای که استفاده کرده باشید، می‌توانید در هر زمان مشخصات را از نظر وجود مقادیر enum بررسی کنید:

```shell
./hack/verify-enum-swagger.sh gen-apidocs/config/<version>/swagger.json
```

## راه‌اندازی پیش‌نمایش محلی

پیش‌نمایش را یک بار در ترمینال دوم راه‌اندازی کنید و آن را در حال اجرا بگذارید. Hugo هر صفحه را با جایگزین شدن توسط targetهای کپی دوباره بارگذاری می‌کند، بنابراین می‌توانید هر مجموعه مرجع را بلافاصله پس از تولید بررسی کنید.

```shell
cd <web-base>
git submodule update --init --recursive --depth 1   # if not already done
make container-serve
```

Hugo پیش‌نمایش را در `http://localhost:1313/` ارائه می‌کند.

{{< note >}}
هر مجموعه را از یک شاخه به‌روز در `<web-base>` شروع کنید، آن را تولید کنید، در پیش‌نمایش بررسی کنید و commit کنید. [Pull requestها](#pull-requests) فهرست می‌کند که برای هر مجموعه چه چیزی باید باز شود، چه زمانی باید باز شود و چگونه باید توصیف شود.
{{< /note >}}

## تولید مرجع API کوبرنتیز

`gen-apidocs` این مجموعه، یعنی مرجع API در قالب HTML، را از مشخصات OpenAPI که دریافت کرده‌اید می‌سازد. خروجی ساخت پیش از آنکه target آن را کپی کند، در `gen-apidocs/build/html/` قرار می‌گیرد.

```shell
cd <rdocs-base>
make copyapi
```

این target دو فایل را در `<web-base>` می‌نویسد:

```
static/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/index.html
static/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/js/navData.js
```

آدرس `/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/` را در پیش‌نمایش بررسی کنید. یک منبع مانند Pod را باز کنید و در صفحه عبارت `Possible enum values` را جست‌وجو کنید؛ این کار تأیید می‌کند که مشخصات، مقادیر enum را تا انتها حفظ کرده است.

برای اینکه برای این مجموعه چه چیزی باید باز شود، [Pull requestها](#pull-requests) را ببینید.

## تولید صفحات مرجع API در قالب Markdown

`gen-apidocs` این مجموعه، یعنی مرجع API در قالب Markdown که Hugo آن را به‌صورت صفحات معمولی رندر می‌کند، را نیز از همان مشخصات می‌سازد. خروجی ساخت در `gen-apidocs/build/markdown/` قرار می‌گیرد.

```shell
cd <rdocs-base>
make copyapimd
```

این target دایرکتوری `<web-base>/content/en/docs/reference/kubernetes-api/` را جایگزین می‌کند و فایل `_index.md` را که به‌صورت دستی نگهداری می‌شود حفظ می‌کند.

آدرس `/docs/reference/kubernetes-api/` را در پیش‌نمایش بررسی کنید. تعداد صفحات تولیدشده را با نسخه قبلی مقایسه کنید:

```shell
find <web-base>/content/en/docs/reference/kubernetes-api -name '*.md' | wc -l
```

برای اینکه برای این مجموعه چه چیزی باید باز شود، [Pull requestها](#pull-requests) را ببینید.

## تولید مرجع مؤلفه‌ها

`gen-compdocs` از `k8s.io/kubernetes` و از ماژول‌های staging در `k8s.io` که `go.mod` با دستورهای `replace` آن‌ها را pin می‌کند ساخته می‌شود. `go get` مورد اول را به‌روزرسانی می‌کند و بقیه را رها می‌کند، بنابراین کل مجموعه را یک‌جا جابه‌جا کنید:

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
اگر `go get` یا `go mod tidy` برای یک ماژول `k8s.io` خطای `unknown revision` یا خطای 404 از `sum.golang.org` گزارش کند، ماژول‌های staging این نسخه هنوز منتشر نشده‌اند. آن‌ها چند ساعت پس از تگ `kubernetes/kubernetes` منتشر می‌شوند. با این دستور بررسی کنید:

```shell
git ls-remote --tags https://github.com/kubernetes/api.git "v0.${K8S_RELEASE#*.}"
```

نتیجه خالی یعنی باید صبر کنید. این موضوع درباره مرجع API پیکربندی نیز صدق می‌کند. دو مجموعه مرجع API فقط مشخصات OpenAPI را می‌خوانند، بنابراین می‌توانید در این فاصله آن‌ها را تولید کنید.
{{< /note >}}

حلقه‌ها مجموعه ماژول‌ها را از `kubernetes/kubernetes` می‌خوانند، زیرا انتشارها ماژول‌های staging را اضافه و حذف می‌کنند و `go.mod` ممکن است همچنان ماژول‌های یک نسخه قدیمی‌تر را فهرست کند. دستورالعمل `go` آخر می‌آید: تا زمانی که ماژول‌های قدیمی هنوز در گراف هستند، `go mod tidy` آن را دوباره بالا می‌برد.

آنچه جابه‌جا شده را بررسی کنید:

```shell
git diff go.mod
```

اکنون هر requirement مربوط به `k8s.io`، هر `replace` و دستورالعمل `go` باید نام نسخه جدید را داشته باشند. requirementهای خارج از مجموعه staging، مانند `k8s.io/klog/v2` و بسته‌های Goldmark، نسخه‌های خودشان را حفظ می‌کنند.

سپس صفحات مؤلفه‌های هسته را بسازید و کپی کنید:

```shell
cd <rdocs-base>
make copycomp-core
```

`gen-compdocs` همه صفحات مؤلفه‌ها را در `gen-compdocs/build/` می‌نویسد و target فایل‌های `kube-apiserver.md`، `kube-controller-manager.md`، `kube-scheduler.md`، `kube-proxy.md` و `kubelet.md` را از آنجا به `<web-base>/content/en/docs/reference/command-line-tools-reference/` کپی می‌کند.

آدرس `/docs/reference/command-line-tools-reference/` را در پیش‌نمایش بررسی کنید.

برای اینکه برای این مجموعه چه چیزی باید باز شود، [Pull requestها](#pull-requests) را ببینید.

{{< note >}}
مرجع مؤلفه‌ها، kubectl و kubeadm سه pull request جداگانه هستند، هرچند `gen-compdocs` هر سه را تولید می‌کند. هر target از نوع `copycomp-*` ابتدا همه صفحات مؤلفه‌ها را دوباره می‌سازد که چند دقیقه طول می‌کشد. برای اینکه یک بار بسازید و هر سه مجموعه را کپی کنید، `make copycomp` را اجرا کنید و سپس نتیجه را به سه شاخه تقسیم کنید.
{{< /note >}}

## تولید مرجع kubectl

صفحات kubectl از همان ساخت `gen-compdocs` مرجع مؤلفه‌ها می‌آیند و در pull request جداگانه خود قرار می‌گیرند.

```shell
cd <rdocs-base>
make copycomp-kubectl
```

این target فایل `kubectl.md` و یک دایرکتوری برای هر زیردستور را در `<web-base>/content/en/docs/reference/kubectl/generated/` می‌نویسد و فایل `_index.md` را که به‌صورت دستی نگهداری می‌شود حفظ می‌کند.

آدرس `/docs/reference/kubectl/generated/` را در پیش‌نمایش بررسی کنید و صفحه یک زیردستور مانند `kubectl apply` را باز کنید.

برای اینکه برای این مجموعه چه چیزی باید باز شود، [Pull requestها](#pull-requests) را ببینید.

## تولید مرجع kubeadm

صفحات kubeadm نیز از `gen-compdocs` می‌آیند و در pull request جداگانه خود قرار می‌گیرند.

```shell
cd <rdocs-base>
make copycomp-kubeadm
```

این target فایل `kubeadm.md` و یک دایرکتوری برای هر زیردستور را در `<web-base>/content/en/docs/reference/setup-tools/kubeadm/generated/` می‌نویسد و فایل‌های `_index.md` و `README.md` را که به‌صورت دستی نگهداری می‌شوند حفظ می‌کند.

آدرس `/docs/reference/setup-tools/kubeadm/generated/` را در پیش‌نمایش بررسی کنید.

برای اینکه برای این مجموعه چه چیزی باید باز شود، [Pull requestها](#pull-requests) را ببینید.

## تولید مرجع API پیکربندی

`genref` انواع Go پیکربندی هر مؤلفه را از ماژول‌های staging در `k8s.io` می‌خواند. این ابزار دستور `replace` ندارد، بنابراین فقط requirementها تعیین می‌کنند که کدام نسخه را مستند می‌کنید:

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

انتخاب بر اساس نسخه قدیمی، ماژول‌های staging را برمی‌گیرد و `k8s.io/klog/v2`، `k8s.io/gengo` و سایر مخازن مستقل را دست‌نخورده می‌گذارد. آنچه جابه‌جا شده را بررسی کنید:

```shell
git diff go.mod
```

همچنین نسخه را در هدف پیوند `externalPackages` در `genref/config.yaml` به‌روزرسانی کنید؛ این پیوند خوانندگان را به مرجع API منتشرشده هدایت می‌کند.

### بررسی نسخه‌های جدید API

`genref` برای هر مورد در `genref/config.yaml` یک صفحه تولید می‌کند و هر مورد یک بسته Go و مسیری را که به یک نسخه API ختم می‌شود نام می‌برد:

```yaml
  - name: kubelet-config
    title: Kubelet Configuration (v1)
    package: k8s.io/kubelet
    path: config/v1
```

مؤلفه‌ای که شروع به ارائه نسخه جدیدی از API پیکربندی خود می‌کند، یک دایرکتوری نسخه در سورس Go خود اضافه می‌کند. دایرکتوری‌های نسخه یک مؤلفه را فهرست کنید تا ببینید در این انتشار چه چیزهایی وجود دارد:

```shell
cd <rdocs-base>/genref
go mod download
ls "$(go list -m -f '{{.Dir}}' k8s.io/kubelet)/config"
```

برای مقایسه یک‌جای هر مورد در `config.yaml` با سورس، این دستور را اجرا کنید:

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

هر خط یک مورد کاندید است، نه یک خلأ که حتماً باید پر شود: چند نسخه قدیمی‌تر عمداً کنار گذاشته شده‌اند و کامنت‌های `config.yaml` دلیل آن را ثبت می‌کنند. زمانی یک مورد اضافه کنید که یک مؤلفه نسخه‌ای را ارائه می‌کند که خوانندگان آن را پیکربندی می‌کنند، و تا زمانی که مؤلفه هنوز یک نسخه قدیمی‌تر را ارائه می‌کند، مورد مربوط به آن را نگه دارید.

### ساخت و کپی صفحات

```shell
cd <rdocs-base>
make copyconfigapi
```

`genref` صفحات تولیدشده را در `genref/output/md/` می‌نویسد و target هنگام کپی آن‌ها را دسته‌بندی می‌کند: بیشتر آن‌ها به `content/en/docs/reference/config-api/` می‌روند، APIهای metrics به `content/en/docs/reference/external-api/` می‌روند، زیرا پروژه آن‌ها را تعریف می‌کند اما از API server ارائه نمی‌کند، و صفحاتی که وب‌سایت منتشر نمی‌کند نادیده گرفته می‌شوند.

هر دو بخش را در پیش‌نمایش بررسی کنید و مطمئن شوید که هیچ صفحه‌ای که برای نسخه قبلی منتشر کرده بودید ناپدید نشده است:

```shell
cd <web-base>
git status content/en/docs/reference/config-api/ content/en/docs/reference/external-api/
```

برای اینکه برای این مجموعه چه چیزی باید باز شود، [Pull requestها](#pull-requests) را ببینید.

## خلاصه

{{< table caption="مجموعه‌های مرجع، تولیدکننده‌ای که هر یک را می‌سازد و محل قرارگیری خروجی آن" >}}
| مجموعه مرجع | تولیدکننده در `<rdocs-base>` | هدف (target) | خروجی در `<web-base>` |
| --- | --- | --- | --- |
| API کوبرنتیز، HTML | `gen-apidocs` | `make copyapi` | `static/docs/reference/generated/kubernetes-api/v{{< skew currentVersionAddMinor 1 >}}/` |
| API کوبرنتیز، Markdown | `gen-apidocs` | `make copyapimd` | `content/en/docs/reference/kubernetes-api/` |
| اجزا (Components) | `gen-compdocs` | `make copycomp-core` | `content/en/docs/reference/command-line-tools-reference/` |
| kubectl | `gen-compdocs` | `make copycomp-kubectl` | `content/en/docs/reference/kubectl/generated/` |
| kubeadm | `gen-compdocs` | `make copycomp-kubeadm` | `content/en/docs/reference/setup-tools/kubeadm/generated/` |
| APIهای پیکربندی | `genref` | `make copyconfigapi` | `content/en/docs/reference/config-api/`, `content/en/docs/reference/external-api/` |
{{< /table >}}

هر هدف کپی (copy target) ابتدا فرایند ساخت را انجام می‌دهد. برای ساخت همه مجموعه‌ها بدون کپی‌کردن چیزی در کلون وب‌سایت خود، دستور `make api apimd comp configapi` را اجرا کنید.

### Pull requestها

هر مجموعه مرجع pull request مخصوص خود را در وب‌سایت دارد، یعنی در مجموع شش مورد، و سمت تولیدکننده‌ها به سه مورد نیاز دارد. pull request وب‌سایت را همراه با pull request مربوط به `reference-docs` که به آن نیاز دارد باز کنید و تا زمانی که آن ادغام نشده است، pull request وب‌سایت را در حالت انتظار نگه دارید.

{{< table caption="Pull requestهایی که برای هر مجموعه مرجع باید باز شوند" >}}
| مجموعه مرجع | Pull request به `kubernetes-sigs/reference-docs` | Pull request به `kubernetes/website` |
| --- | --- | --- |
| API کوبرنتیز، HTML | `gen-apidocs/config/<version>/`، شامل پیکربندی و مشخصات (specification): یک pull request برای هر دو مجموعه API | `Update the Kubernetes API reference for v{{< skew currentVersionAddMinor 1 >}}` |
| API کوبرنتیز، Markdown | همان pull request مربوط به `gen-apidocs` | `Update the generated API reference pages for v{{< skew currentVersionAddMinor 1 >}}` |
| اجزا (Components) | `gen-compdocs/go.mod` و `go.sum`: یک pull request برای مجموعه‌های اجزا، kubectl و kubeadm | `Update the component reference for v{{< skew currentVersionAddMinor 1 >}}` |
| kubectl | همان pull request مربوط به `gen-compdocs` | `Update the kubectl reference for v{{< skew currentVersionAddMinor 1 >}}` |
| kubeadm | همان pull request مربوط به `gen-compdocs` | `Update the kubeadm reference for v{{< skew currentVersionAddMinor 1 >}}` |
| APIهای پیکربندی | `genref/go.mod`، `genref/config.yaml` و `genref/output/md/`: یک pull request | `Update the configuration API reference for v{{< skew currentVersionAddMinor 1 >}}` |
{{< /table >}}

در هر pull request وب‌سایت توضیح دهید که خروجی را چگونه تولید کرده‌اید تا بازبین بتواند آن را بازتولید کند:

```text
Regenerated the kubectl reference for v{{< skew currentVersionAddMinor 1 >}}.0.

- Generated with `make copycomp-kubectl` from kubernetes-sigs/reference-docs at commit <commit>
- Generator changes: kubernetes-sigs/reference-docs#<pull request>
- Generated files only, with no hand edits
```

برای دو مجموعه مرجع API، نحوه تولید مشخصات OpenAPI را نیز اضافه کنید، زیرا خروجی تولیدشده آن را نشان نمی‌دهد: `generated from source with
make updateapispec-enums-from-source` یا `generated in a local clone with
KUBE_OPENAPI_SPEC_KEEP_ENUMS=true`.

{{< caution >}}
صفحه‌های تولیدشده را به‌صورت دستی ویرایش نکنید. نسخه بعدی ویرایش شما را بازنویسی می‌کند. به‌جای آن، متن را [در پروژه بالادستی](/docs/contribute/generate-ref-docs/contribute-upstream/) یا در تولیدکننده اصلاح کنید.
{{< /caution >}}

## {{% heading "whatsnext" %}}

* [تولید مستندات مرجع برای API کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-api/)
* [تولید مستندات مرجع برای APIهای پیکربندی](/docs/contribute/generate-ref-docs/config-api/)
* [تولید صفحه‌های مرجع برای اجزا و ابزارهای کوبرنتیز](/docs/contribute/generate-ref-docs/kubernetes-components/)
* [تولید مستندات مرجع برای دستورهای kubectl](/docs/contribute/generate-ref-docs/kubectl/)
* [تولید مستندات مرجع برای متریک‌ها](/docs/contribute/generate-ref-docs/metrics-reference/)
* [مشارکت در کد بالادستی کوبرنتیز](/docs/contribute/generate-ref-docs/contribute-upstream/)
* [راهنمای نقش مستندات](https://github.com/kubernetes/sig-release/tree/master/release-team/role-handbooks/docs)
  در `kubernetes/sig-release`
