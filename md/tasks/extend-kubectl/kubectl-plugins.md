---
title: گسترش kubectl با افزونه‌ها
reviewers:
- juanvallejo
- soltysh
description: با ایجاد و نصب افزونه‌های kubectl، قابلیت‌های kubectl را گسترش دهید.
content_type: task
---

<!-- overview -->

این راهنما نشان می‌دهد که چگونه افزونه‌هایی برای [kubectl](/docs/reference/kubectl/kubectl/) نصب کنید و بنویسید.
اگر فرمان‌های اصلی `kubectl` را اجزای سازندهٔ بنیادی برای تعامل با یک کلاستر کوبرنتیز بدانیم، مدیر کلاستر می‌تواند افزونه‌ها را ابزاری برای به‌کارگیری این اجزای سازنده و ایجاد رفتارهای پیچیده‌تر در نظر بگیرد.
افزونه‌ها با افزودن زیرفرمان‌های جدید، `kubectl` را گسترش می‌دهند و امکان قابلیت‌های تازه و سفارشی‌ای را فراهم می‌کنند که در توزیع اصلی `kubectl` وجود ندارند.

## {{% heading "prerequisites" %}}

باید یک فایل اجرایی `kubectl` سالم و نصب‌شده در اختیار داشته باشید.

<!-- steps -->

## نصب افزونه‌های kubectl

هر افزونه یک فایل اجرایی مستقل است که نام آن با `kubectl-` آغاز می‌شود. برای نصب یک افزونه، فایل اجرایی آن را به هر مسیری در `PATH` خود منتقل کنید.

همچنین می‌توانید افزونه‌های متن‌باز kubectl را با استفاده از [Krew](https://krew.dev/) پیدا و نصب کنید. Krew یک مدیر افزونه است که جامعهٔ SIG CLI کوبرنتیز آن را نگهداری می‌کند.

{{< caution >}}
افزونه‌های kubectl که از طریق [فهرست افزونه‌های](https://krew.sigs.k8s.io/plugins/) Krew در دسترس هستند، از نظر امنیتی بازبینی نشده‌اند. نصب و اجرای افزونه‌های شخص ثالث با مسئولیت خود شماست، زیرا این افزونه‌ها برنامه‌هایی دلخواه هستند که روی دستگاه شما اجرا می‌شوند.
{{< /caution >}}

### یافتن افزونه‌ها

ابزار `kubectl` فرمان `kubectl plugin list` را فراهم می‌کند که `PATH` شما را برای یافتن فایل‌های اجرایی معتبر افزونه جست‌وجو می‌کند.
اجرای این فرمان باعث پیمایش همهٔ فایل‌های موجود در `PATH` شما می‌شود. همهٔ فایل‌هایی که اجرایی باشند و نامشان با `kubectl-` آغاز شود، *به همان ترتیبی که در `PATH` شما قرار دارند* در خروجی این فرمان نمایش داده می‌شوند.
برای هر فایلی که نامش با `kubectl-` آغاز شود اما اجرایی *نباشد*، یک هشدار نمایش داده می‌شود.
همچنین برای فایل‌های معتبر افزونه‌ای که نامشان با یکدیگر هم‌پوشانی دارد نیز هشدار نمایش داده می‌شود.

می‌توانید با استفاده از [Krew](https://krew.dev/) افزونه‌های `kubectl` را از یک [فهرست افزونه‌ها](https://krew.sigs.k8s.io/plugins/) که جامعه آن را گردآوری کرده است، پیدا و نصب کنید.

#### افزونه‌های create

ابزار `kubectl` به افزونه‌ها اجازه می‌دهد فرمان‌های create سفارشی به شکل `kubectl create something` اضافه کنند؛ کافی است یک فایل اجرایی `kubectl-create-something` در `PATH` قرار دهید.

#### محدودیت‌ها

در حال حاضر نمی‌توان افزونه‌هایی ساخت که فرمان‌های موجود `kubectl` را بازنویسی کنند یا فرمان‌هایی غیر از `create` را گسترش دهند.
برای مثال، اگر افزونه‌ای با نام `kubectl-version` بسازید، آن افزونه هرگز اجرا نمی‌شود، زیرا فرمان موجود `kubectl version` همیشه بر آن اولویت دارد.
به دلیل همین محدودیت، استفاده از افزونه‌ها برای افزودن زیرفرمان‌های جدید به فرمان‌های موجود `kubectl` نیز امکان‌پذیر *نیست*.
برای مثال، اگر بخواهید با نام‌گذاری افزونهٔ خود به‌صورت `kubectl-attach-vm` زیرفرمان `kubectl attach vm` را اضافه کنید، آن افزونه نادیده گرفته می‌شود.

فرمان `kubectl plugin list` برای هر افزونهٔ معتبری که چنین کاری را انجام دهد، هشدار نمایش می‌دهد.

## نوشتن افزونه‌های kubectl

می‌توانید افزونه را با هر زبان برنامه‌نویسی یا اسکریپتی بنویسید که امکان نوشتن فرمان‌های خط فرمان را فراهم کند.

هیچ نصب یا بارگذاری پیشینی برای افزونه لازم نیست. فایل‌های اجرایی افزونه، محیط (environment) را به‌صورت موروثی از فایل اجرایی `kubectl` دریافت می‌کنند.
هر افزونه بر اساس نام خود تعیین می‌کند که کدام مسیر فرمان را پیاده‌سازی کند.
برای مثال، افزونه‌ای با نام `kubectl-foo` فرمان `kubectl foo` را فراهم می‌کند. باید فایل اجرایی افزونه را در جایی از `PATH` خود نصب کنید.

### نمونهٔ افزونه

```bash
#!/bin/bash

# optional argument handling
if [[ "$1" == "version" ]]
then
    echo "1.0.0"
    exit 0
fi

# optional argument handling
if [[ "$1" == "config" ]]
then
    echo "$KUBECONFIG"
    exit 0
fi

echo "I am a plugin named kubectl-foo"
```

### استفاده از افزونه

برای استفاده از یک افزونه، آن را اجرایی کنید:

```shell
sudo chmod +x ./kubectl-foo
```

و آن را در هر جایی از `PATH` خود قرار دهید:

```shell
sudo mv ./kubectl-foo /usr/local/bin
```

اکنون می‌توانید افزونهٔ خود را به‌عنوان یک فرمان `kubectl` فراخوانی کنید:

```shell
kubectl foo
```

```
I am a plugin named kubectl-foo
```

همهٔ آرگومان‌ها و فلگ‌ها بدون تغییر به فایل اجرایی ارسال می‌شوند:

```shell
kubectl foo version
```

```
1.0.0
```

همهٔ متغیرهای محیطی نیز بدون تغییر به فایل اجرایی ارسال می‌شوند:

```bash
export KUBECONFIG=~/.kube/config
kubectl foo config
```

```
/home/<user>/.kube/config
```

```shell
KUBECONFIG=/etc/kube/config kubectl foo config
```

```
/etc/kube/config
```

افزون بر این، نخستین آرگومانی که به افزونه ارسال می‌شود، همیشه مسیر کامل محلی است که افزونه از آنجا فراخوانی شده است (در مثال بالا، مقدار `$0` برابر با `/usr/local/bin/kubectl-foo` خواهد بود).

### نام‌گذاری افزونه

همان‌طور که در مثال بالا دیدید، هر افزونه بر اساس نام فایل خود، مسیر فرمانی را که پیاده‌سازی می‌کند تعیین می‌کند. زیرفرمان‌های موجود در مسیر فرمانِ مورد نظر افزونه با خط تیره (`-`) از یکدیگر جدا می‌شوند.
برای مثال، افزونه‌ای که قرار است هر بار کاربر فرمان `kubectl foo bar baz` را اجرا کند فراخوانی شود، باید نام فایل `kubectl-foo-bar-baz` را داشته باشد.

#### مدیریت فلگ‌ها و آرگومان‌ها

{{< note >}}
سازوکار افزونه‌ها هیچ مقدار سفارشی یا متغیر محیطی ویژهٔ افزونه‌ای برای فرایند افزونه ایجاد _نمی‌کند_.

سازوکار قدیمی‌تر افزونه‌های kubectl متغیرهای محیطی‌ای مانند `KUBECTL_PLUGINS_CURRENT_NAMESPACE` را فراهم می‌کرد؛ اما این کار دیگر انجام نمی‌شود.
{{< /note >}}

افزونه‌های kubectl باید همهٔ آرگومان‌هایی را که به آن‌ها ارسال می‌شود، تجزیه و اعتبارسنجی کنند.
برای آشنایی با جزئیات یک کتابخانهٔ Go که برای نویسندگان افزونه طراحی شده است، به [استفاده از بستهٔ زمان اجرای خط فرمان](#using-the-command-line-runtime-package) مراجعه کنید.

در ادامه چند حالت دیگر را بررسی می‌کنیم که در آن‌ها کاربران هنگام فراخوانی افزونهٔ شما فلگ‌ها و آرگومان‌های بیشتری ارائه می‌کنند. این حالت‌ها بر پایهٔ افزونهٔ `kubectl-foo-bar-baz` از سناریوی بالا هستند.

اگر فرمان `kubectl foo bar baz arg1 --flag=value arg2` را اجرا کنید، سازوکار افزونهٔ kubectl ابتدا تلاش می‌کند افزونه‌ای با طولانی‌ترین نام ممکن پیدا کند که در این مورد `kubectl-foo-bar-baz-arg1` است. اگر این افزونه یافت نشود، kubectl آخرین مقدار جداشده با خط تیره را آرگومان در نظر می‌گیرد (در این مورد `arg1`) و تلاش می‌کند طولانی‌ترین نام ممکن بعدی، یعنی `kubectl-foo-bar-baz`، را پیدا کند.
پس از یافتن افزونه‌ای با این نام، kubectl آن افزونه را فراخوانی می‌کند و همهٔ آرگومان‌ها و فلگ‌های پس از نام افزونه را به‌عنوان آرگومان به فرایند افزونه ارسال می‌کند.

مثال:

```bash
# create a plugin
echo -e '#!/bin/bash\n\necho "My first command-line argument was $1"' > kubectl-foo-bar-baz
sudo chmod +x ./kubectl-foo-bar-baz

# "install" your plugin by moving it to a directory in your $PATH
sudo mv ./kubectl-foo-bar-baz /usr/local/bin

# check that kubectl recognizes your plugin
kubectl plugin list
```

```
The following kubectl-compatible plugins are available:

/usr/local/bin/kubectl-foo-bar-baz
```

```
# test that calling your plugin via a "kubectl" command works
# even when additional arguments and flags are passed to your
# plugin executable by the user.
kubectl foo bar baz arg1 --meaningless-flag=true
```

```
My first command-line argument was arg1
```

همان‌طور که می‌بینید، افزونهٔ شما بر اساس فرمان `kubectl` واردشده توسط کاربر پیدا شد و پس از یافتن آن، همهٔ آرگومان‌ها و فلگ‌های اضافی بدون تغییر به فایل اجرایی افزونه ارسال شدند.

#### نام‌های دارای خط تیره و زیرخط

با اینکه سازوکار افزونهٔ `kubectl` از خط تیره (`-`) در نام فایل افزونه‌ها برای جدا کردن دنبالهٔ زیرفرمان‌های پردازش‌شده توسط افزونه استفاده می‌کند، همچنان می‌توان با به‌کار بردن زیرخط (`_`) در نام فایل، افزونه‌ای ساخت که فراخوانی آن در خط فرمان شامل خط تیره باشد.

مثال:

```bash
# create a plugin containing an underscore in its filename
echo -e '#!/bin/bash\n\necho "I am a plugin with a dash in my name"' > ./kubectl-foo_bar
sudo chmod +x ./kubectl-foo_bar

# move the plugin into your $PATH
sudo mv ./kubectl-foo_bar /usr/local/bin

# You can now invoke your plugin via kubectl:
kubectl foo-bar
```

```
I am a plugin with a dash in my name
```

توجه کنید که استفاده از زیرخط در نام فایل افزونه، مانع از داشتن فرمان‌هایی مانند `kubectl foo_bar` نمی‌شود.
فرمان مثال بالا را می‌توان هم با خط تیره (`-`) و هم با زیرخط (`_`) فراخوانی کرد:

```bash
# You can invoke your custom command with a dash
kubectl foo-bar
```

```
I am a plugin with a dash in my name
```

```bash
# You can also invoke your custom command with an underscore
kubectl foo_bar
```

```
I am a plugin with a dash in my name
```

#### تداخل نام‌ها و پوشانده شدن افزونه‌ها

ممکن است چند افزونه با نام فایل یکسان در مکان‌های مختلفی از `PATH` شما وجود داشته باشند.
برای مثال، اگر مقدار `PATH` برابر با `PATH=/usr/local/bin/plugins:/usr/local/bin/moreplugins` باشد، ممکن است یک نسخه از افزونهٔ `kubectl-foo` در `/usr/local/bin/plugins` و نسخهٔ دیگری در `/usr/local/bin/moreplugins` وجود داشته باشد؛ در این صورت خروجی فرمان `kubectl plugin list` چنین خواهد بود:

```bash
PATH=/usr/local/bin/plugins:/usr/local/bin/moreplugins kubectl plugin list
```

```
The following kubectl-compatible plugins are available:

/usr/local/bin/plugins/kubectl-foo
/usr/local/bin/moreplugins/kubectl-foo
  - warning: /usr/local/bin/moreplugins/kubectl-foo is overshadowed by a similarly named plugin: /usr/local/bin/plugins/kubectl-foo

error: one plugin warning was found
```

در سناریوی بالا، هشدار زیر `/usr/local/bin/moreplugins/kubectl-foo` به شما می‌گوید که این افزونه هرگز اجرا نخواهد شد. در عوض، سازوکار افزونهٔ `kubectl` همیشه فایل اجرایی‌ای را که زودتر در `PATH` شما آمده است، یعنی `/usr/local/bin/plugins/kubectl-foo`، پیدا و اجرا می‌کند.

یکی از راه‌های حل این مشکل این است که مطمئن شوید مکان افزونه‌ای که می‌خواهید با `kubectl` استفاده کنید، همیشه در ابتدای `PATH` شما قرار دارد. برای مثال، اگر می‌خواهید هر بار که فرمان `kubectl foo` فراخوانی می‌شود، همیشه از `/usr/local/bin/moreplugins/kubectl-foo` استفاده شود، مقدار `PATH` خود را به `/usr/local/bin/moreplugins:/usr/local/bin/plugins` تغییر دهید.

#### فراخوانی طولانی‌ترین نام فایل اجرایی

نوع دیگری از پوشانده شدن نیز ممکن است در نام فایل افزونه‌ها رخ دهد. فرض کنید دو افزونهٔ `kubectl-foo-bar` و `kubectl-foo-bar-baz` در `PATH` کاربر وجود دارند. در این حالت، سازوکار افزونهٔ `kubectl` همیشه طولانی‌ترین نام افزونهٔ ممکن را برای فرمان واردشده توسط کاربر انتخاب می‌کند. مثال‌های زیر این موضوع را روشن‌تر می‌کنند:

```bash
# for a given kubectl command, the plugin with the longest possible filename will always be preferred
kubectl foo bar baz
```

```
Plugin kubectl-foo-bar-baz is executed
```

```bash
kubectl foo bar
```

```
Plugin kubectl-foo-bar is executed
```

```bash
kubectl foo bar baz buz
```

```
Plugin kubectl-foo-bar-baz is executed, with "buz" as its first argument
```

```bash
kubectl foo bar buz
```

```
Plugin kubectl-foo-bar is executed, with "buz" as its first argument
```

این انتخاب طراحی تضمین می‌کند که در صورت نیاز بتوان زیرفرمان‌های یک افزونه را در چند فایل پیاده‌سازی کرد و این زیرفرمان‌ها را زیر یک فرمان افزونهٔ «والد» قرار داد:

```bash
ls ./plugin_command_tree
```

```
kubectl-parent
kubectl-parent-subcommand
kubectl-parent-subcommand-subsubcommand
```

### بررسی هشدارهای افزونه

می‌توانید با فرمان `kubectl plugin list` که پیش‌تر به آن اشاره شد، اطمینان حاصل کنید که افزونهٔ شما برای `kubectl` قابل مشاهده است و هیچ هشداری مانع از فراخوانی آن به‌عنوان یک فرمان `kubectl` نمی‌شود.

```bash
kubectl plugin list
```

```
The following kubectl-compatible plugins are available:

test/fixtures/pkg/kubectl/plugins/kubectl-foo
/usr/local/bin/kubectl-foo
  - warning: /usr/local/bin/kubectl-foo is overshadowed by a similarly named plugin: test/fixtures/pkg/kubectl/plugins/kubectl-foo
plugins/kubectl-invalid
  - warning: plugins/kubectl-invalid identified as a kubectl plugin, but it is not executable

error: 2 plugin warnings were found
```

### استفاده از بستهٔ زمان اجرای خط فرمان

اگر افزونه‌ای برای kubectl می‌نویسید و از زبان Go استفاده می‌کنید، می‌توانید از کتابخانه‌های کمکی [cli-runtime](https://github.com/kubernetes/cli-runtime) بهره ببرید.

این کتابخانه‌ها ابزارهای کمکی برای تجزیه یا به‌روزرسانی فایل [kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) کاربر، ارسال درخواست‌های REST به سرور API، یا اتصال فلگ‌های مربوط به پیکربندی و چاپ خروجی فراهم می‌کنند.

برای دیدن نمونه‌ای از کاربرد ابزارهای موجود در مخزن CLI Runtime، به [نمونهٔ افزونهٔ CLI](https://github.com/kubernetes/sample-cli-plugin) مراجعه کنید.

## توزیع افزونه‌های kubectl

اگر افزونه‌ای توسعه داده‌اید تا دیگران از آن استفاده کنند، باید به نحوهٔ بسته‌بندی، توزیع و ارائهٔ به‌روزرسانی‌های آن به کاربران فکر کنید.

### Krew {#distributing-krew}

ابزار [Krew](https://krew.dev/) روشی چندسکویی برای بسته‌بندی و توزیع افزونه‌ها ارائه می‌دهد. به این ترتیب، برای همهٔ سکوهای هدف (Linux، Windows، macOS و غیره) از یک قالب بسته‌بندی واحد استفاده می‌کنید و به‌روزرسانی‌ها را به کاربران خود می‌رسانید.
Krew همچنین یک [فهرست افزونه‌ها](https://krew.sigs.k8s.io/plugins/) نگهداری می‌کند تا دیگران بتوانند افزونهٔ شما را پیدا و نصب کنند.


### مدیریت بستهٔ بومی یا ویژهٔ هر سکو {#distributing-native}

به‌عنوان جایگزین، می‌توانید از مدیران بستهٔ سنتی مانند `apt` یا `dnf` در Linux، Chocolatey در Windows و Homebrew در macOS استفاده کنید. هر مدیر بسته‌ای که بتواند فایل‌های اجرایی جدید را در جایی از `PATH` کاربر قرار دهد، مناسب است.
اگر به‌عنوان نویسندهٔ افزونه این گزینه را انتخاب کنید، مسئولیت به‌روزرسانی بستهٔ توزیع افزونهٔ kubectl خود در چندین سکو برای هر انتشار نیز بر عهدهٔ شما خواهد بود.

### کد منبع {#distributing-source-code}

می‌توانید کد منبع را منتشر کنید؛ برای مثال، به‌صورت یک مخزن Git. اگر این گزینه را انتخاب کنید، هر کسی که بخواهد از آن افزونه استفاده کند باید کد را دریافت کند، یک محیط ساخت (در صورت نیاز به کامپایل) راه‌اندازی کند و افزونه را مستقر کند.
اگر بسته‌های کامپایل‌شده را نیز در دسترس قرار دهید یا از Krew استفاده کنید، نصب آسان‌تر خواهد شد.

## {{% heading "whatsnext" %}}

* برای دیدن [نمونه‌ای مفصل](https://github.com/kubernetes/sample-cli-plugin) از افزونه‌ای که با Go نوشته شده است، به مخزن Sample CLI Plugin سر بزنید.
  در صورت داشتن هرگونه پرسش، می‌توانید با [تیم SIG CLI](https://github.com/kubernetes/community/tree/main/sig-cli) در تماس باشید.
* دربارهٔ [Krew](https://krew.dev/)، مدیر بسته‌ای برای افزونه‌های kubectl، مطالعه کنید.
