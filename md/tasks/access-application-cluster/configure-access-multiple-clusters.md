---
title: پیکربندی دسترسی به چندین کلاستر
content_type: task
weight: 30
card:
  name: tasks
  weight: 25
  title: پیکربندی دسترسی به کلاسترها
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان با استفاده از فایل‌های پیکربندی، دسترسی به چندین کلاستر را پیکربندی کرد. پس از اینکه کلاسترها، کاربران و زمینه‌ها (contexts) را در یک یا چند فایل پیکربندی تعریف کردید، می‌توانید با دستور `kubectl config use-context` به‌سرعت میان کلاسترها جابه‌جا شوید.

{{< note >}}
فایلی که برای پیکربندی دسترسی به یک کلاستر استفاده می‌شود، گاهی *فایل kubeconfig* نامیده می‌شود. این عبارت روشی کلی برای اشاره به فایل‌های پیکربندی است و به این معنا نیست که فایلی با نام `kubeconfig` وجود دارد.
{{< /note >}}


{{< warning >}}
فقط از فایل‌های kubeconfig با منبع مورد اعتماد استفاده کنید. استفاده از یک فایل kubeconfig دست‌کاری‌شده ممکن است به اجرای کد مخرب یا افشای فایل‌ها منجر شود.
اگر ناچارید از یک فایل kubeconfig نامطمئن استفاده کنید، ابتدا آن را با دقت بررسی کنید؛ همان‌گونه که یک اسکریپت شل را بررسی می‌کنید.
{{< /warning>}}


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

برای بررسی نصب بودن {{< glossary_tooltip text="kubectl" term_id="kubectl" >}}، دستور `kubectl version --client` را اجرا کنید. نسخهٔ kubectl باید [حداکثر یک نسخهٔ فرعی](/releases/version-skew-policy/#kubectl) با سرور API کلاستر شما فاصله داشته باشد.

<!-- steps -->

## تعریف کلاسترها، کاربران و زمینه‌ها

فرض کنید دو کلاستر دارید: یکی برای کارهای توسعه و دیگری برای کارهای آزمایشی. در کلاستر `development`، توسعه‌دهندگان فرانت‌اند در فضای نامی (namespace) به نام `frontend` و توسعه‌دهندگان ذخیره‌سازی در فضای نامی به نام `storage` کار می‌کنند. در کلاستر `test`، توسعه‌دهندگان در فضای نام پیش‌فرض کار می‌کنند یا در صورت نیاز، فضاهای نام کمکی ایجاد می‌کنند. دسترسی به کلاستر توسعه به احراز هویت با گواهی نیاز دارد و دسترسی به کلاستر آزمایشی به احراز هویت با نام کاربری و گذرواژه.

یک دایرکتوری با نام `config-exercise` ایجاد کنید. سپس در دایرکتوری `config-exercise` فایلی با نام `config-demo` و با محتوای زیر بسازید:

```yaml
apiVersion: v1
kind: Config
preferences: {}

clusters:
- cluster:
  name: development
- cluster:
  name: test

users:
- name: developer
- name: experimenter

contexts:
- context:
  name: dev-frontend
- context:
  name: dev-storage
- context:
  name: exp-test
```

هر فایل پیکربندی، کلاسترها، کاربران و زمینه‌ها را توصیف می‌کند. فایل `config-demo` شما چارچوب لازم برای توصیف دو کلاستر، دو کاربر و سه زمینه را دارد.

به دایرکتوری `config-exercise` بروید و دستورهای زیر را وارد کنید تا جزئیات کلاسترها به فایل پیکربندی افزوده شود:

```shell
kubectl config --kubeconfig=config-demo set-cluster development --server=https://1.2.3.4 --certificate-authority=fake-ca-file
kubectl config --kubeconfig=config-demo set-cluster test --server=https://5.6.7.8 --insecure-skip-tls-verify
```

جزئیات کاربران را به فایل پیکربندی بیفزایید:

{{< caution >}}
ذخیره‌کردن گذرواژه‌ها در پیکربندی کلاینت کوبرنتیز پرخطر است. راهکار بهتر، استفاده از یک افزونهٔ اعتبارنامه و ذخیرهٔ جداگانهٔ آن‌هاست. ببینید: [افزونه‌های اعتبارنامهٔ client-go](/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins)
{{< /caution >}}

```shell
kubectl config --kubeconfig=config-demo set-credentials developer --client-certificate=fake-cert-file --client-key=fake-key-seefile
kubectl config --kubeconfig=config-demo set-credentials experimenter --username=exp --password=some-password
```

{{< note >}}
- برای حذف یک کاربر می‌توانید دستور `kubectl --kubeconfig=config-demo config unset users.<name>` را اجرا کنید.
- برای حذف یک کلاستر می‌توانید دستور `kubectl --kubeconfig=config-demo config unset clusters.<name>` را اجرا کنید.
- برای حذف یک زمینه می‌توانید دستور `kubectl --kubeconfig=config-demo config unset contexts.<name>` را اجرا کنید.
{{< /note >}}

جزئیات زمینه‌ها را به فایل پیکربندی بیفزایید:

```shell
kubectl config --kubeconfig=config-demo set-context dev-frontend --cluster=development --namespace=frontend --user=developer
kubectl config --kubeconfig=config-demo set-context dev-storage --cluster=development --namespace=storage --user=developer
kubectl config --kubeconfig=config-demo set-context exp-test --cluster=test --namespace=default --user=experimenter
```

فایل `config-demo` را باز کنید تا جزئیات افزوده‌شده را ببینید. به‌جای باز کردن فایل `config-demo` می‌توانید از دستور `config view` نیز استفاده کنید.

```shell
kubectl config --kubeconfig=config-demo view
```

خروجی، دو کلاستر، دو کاربر و سه زمینه را نشان می‌دهد:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority: fake-ca-file
    server: https://1.2.3.4
  name: development
- cluster:
    insecure-skip-tls-verify: true
    server: https://5.6.7.8
  name: test
contexts:
- context:
    cluster: development
    namespace: frontend
    user: developer
  name: dev-frontend
- context:
    cluster: development
    namespace: storage
    user: developer
  name: dev-storage
- context:
    cluster: test
    namespace: default
    user: experimenter
  name: exp-test
current-context: ""
kind: Config
preferences: {}
users:
- name: developer
  user:
    client-certificate: fake-cert-file
    client-key: fake-key-file
- name: experimenter
  user:
    # Documentation note (this comment is NOT part of the command output).
    # Storing passwords in Kubernetes client config is risky.
    # A better alternative would be to use a credential plugin
    # and store the credentials separately.
    # See https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins
    password: some-password
    username: exp
```

مقادیر `fake-ca-file`، `fake-cert-file` و `fake-key-file` در بالا، جانگهدارهایی برای مسیر فایل‌های گواهی هستند. باید این مقادیر را با مسیرهای واقعی فایل‌های گواهی در محیط خود جایگزین کنید.

گاهی ممکن است بخواهید به‌جای فایل‌های گواهی جداگانه، داده‌های کدگذاری‌شده با Base64 را مستقیماً در همین‌جا قرار دهید. در این صورت باید پسوند `-data` را به کلیدها اضافه کنید؛ برای نمونه `certificate-authority-data`، `client-certificate-data` و `client-key-data`.

هر زمینه یک سه‌تایی (کلاستر، کاربر، فضای نام) است. برای نمونه، زمینهٔ `dev-frontend` می‌گوید: «از اعتبارنامه‌های کاربر `developer` برای دسترسی به فضای نام `frontend` در کلاستر `development` استفاده کن».

زمینهٔ جاری را تنظیم کنید:

```shell
kubectl config --kubeconfig=config-demo use-context dev-frontend
```

از این پس هر دستور `kubectl` که وارد کنید، روی کلاستر و فضای نامی اعمال می‌شود که در زمینهٔ `dev-frontend` فهرست شده‌اند. همچنین دستور از اعتبارنامه‌های کاربری استفاده می‌کند که در زمینهٔ `dev-frontend` آمده است.

برای دیدن فقط اطلاعات پیکربندی مربوط به زمینهٔ جاری، از فلگ `--minify` استفاده کنید.

```shell
kubectl config --kubeconfig=config-demo view --minify
```

خروجی، اطلاعات پیکربندی مربوط به زمینهٔ `dev-frontend` را نشان می‌دهد:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority: fake-ca-file
    server: https://1.2.3.4
  name: development
contexts:
- context:
    cluster: development
    namespace: frontend
    user: developer
  name: dev-frontend
current-context: dev-frontend
kind: Config
preferences: {}
users:
- name: developer
  user:
    client-certificate: fake-cert-file
    client-key: fake-key-file
```

حال فرض کنید می‌خواهید مدتی در کلاستر آزمایشی کار کنید.

زمینهٔ جاری را به `exp-test` تغییر دهید:

```shell
kubectl config --kubeconfig=config-demo use-context exp-test
```

اکنون هر دستور `kubectl` که اجرا کنید، روی فضای نام پیش‌فرض کلاستر `test` اعمال می‌شود. همچنین دستور از اعتبارنامه‌های کاربری استفاده می‌کند که در زمینهٔ `exp-test` آمده است.

پیکربندی مربوط به زمینهٔ جاری جدید، یعنی `exp-test`، را مشاهده کنید.

```shell
kubectl config --kubeconfig=config-demo view --minify
```

در پایان، فرض کنید می‌خواهید مدتی در فضای نام `storage` از کلاستر `development` کار کنید.

زمینهٔ جاری را به `dev-storage` تغییر دهید:

```shell
kubectl config --kubeconfig=config-demo use-context dev-storage
```

پیکربندی مربوط به زمینهٔ جاری جدید، یعنی `dev-storage`، را مشاهده کنید.

```shell
kubectl config --kubeconfig=config-demo view --minify
```

## ایجاد فایل پیکربندی دوم

در دایرکتوری `config-exercise` فایلی با نام `config-demo-2` و با محتوای زیر بسازید:

```yaml
apiVersion: v1
kind: Config
preferences: {}

contexts:
- context:
    cluster: development
    namespace: ramp
    user: developer
  name: dev-ramp-up
```

فایل پیکربندی بالا یک زمینهٔ جدید با نام `dev-ramp-up` تعریف می‌کند.

## تنظیم متغیر محیطی KUBECONFIG

بررسی کنید که آیا متغیر محیطی‌ای با نام `KUBECONFIG` دارید یا نه. اگر دارید، مقدار فعلی متغیر محیطی `KUBECONFIG` را ذخیره کنید تا بعداً بتوانید آن را بازگردانید. برای نمونه:

### لینوکس

```shell
export KUBECONFIG_SAVED="$KUBECONFIG"
```

### ویندوز PowerShell

```powershell
$Env:KUBECONFIG_SAVED=$ENV:KUBECONFIG
```

متغیر محیطی `KUBECONFIG` فهرستی از مسیرهای فایل‌های پیکربندی است. اعضای این فهرست در لینوکس و مک با دونقطه و در ویندوز با نقطه‌ویرگول از هم جدا می‌شوند. اگر متغیر محیطی `KUBECONFIG` دارید، با فایل‌های پیکربندی موجود در این فهرست آشنا شوید.

دو مسیر را به‌طور موقت به متغیر محیطی `KUBECONFIG` بیفزایید. برای نمونه:

### لینوکس

```shell
export KUBECONFIG="${KUBECONFIG}:config-demo:config-demo-2"
```

### ویندوز PowerShell

```powershell
$Env:KUBECONFIG=("config-demo;config-demo-2")
```

در دایرکتوری `config-exercise` این دستور را وارد کنید:

```shell
kubectl config view
```

خروجی، اطلاعات ادغام‌شدهٔ همهٔ فایل‌هایی را نشان می‌دهد که در متغیر محیطی `KUBECONFIG` فهرست شده‌اند. به‌ویژه توجه کنید که اطلاعات ادغام‌شده هم زمینهٔ `dev-ramp-up` از فایل `config-demo-2` و هم سه زمینهٔ فایل `config-demo` را در بر دارد:

```yaml
contexts:
- context:
    cluster: development
    namespace: frontend
    user: developer
  name: dev-frontend
- context:
    cluster: development
    namespace: ramp
    user: developer
  name: dev-ramp-up
- context:
    cluster: development
    namespace: storage
    user: developer
  name: dev-storage
- context:
    cluster: test
    namespace: default
    user: experimenter
  name: exp-test
```

برای آگاهی بیشتر دربارهٔ نحوهٔ ادغام فایل‌های kubeconfig، به [سازمان‌دهی دسترسی به کلاستر با استفاده از فایل‌های kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/) مراجعه کنید.

## بررسی دایرکتوری ‎$HOME/.kube

اگر از قبل کلاستری دارید و می‌توانید با `kubectl` با آن تعامل کنید، احتمالاً فایلی با نام `config` در دایرکتوری `$HOME/.kube` دارید.

به `$HOME/.kube` بروید و ببینید چه فایل‌هایی در آن وجود دارد. معمولاً فایلی با نام `config` در آنجا هست. ممکن است فایل‌های پیکربندی دیگری نیز در این دایرکتوری باشند. نگاهی کوتاه به محتوای این فایل‌ها بیندازید تا با آن‌ها آشنا شوید.

## افزودن ‎$HOME/.kube/config به متغیر محیطی KUBECONFIG

اگر فایل `$HOME/.kube/config` دارید و این فایل هنوز در متغیر محیطی `KUBECONFIG` فهرست نشده است، اکنون آن را به متغیر محیطی `KUBECONFIG` بیفزایید. برای نمونه:

### لینوکس

```shell
export KUBECONFIG="${KUBECONFIG}:${HOME}/.kube/config"
```

### ویندوز Powershell

```powershell
$Env:KUBECONFIG="$Env:KUBECONFIG;$HOME\.kube\config"
```

اطلاعات پیکربندی ادغام‌شده از همهٔ فایل‌هایی را که اکنون در متغیر محیطی `KUBECONFIG` فهرست شده‌اند، مشاهده کنید. در دایرکتوری config-exercise این دستور را وارد کنید:

```shell
kubectl config view
```

## پاک‌سازی

متغیر محیطی `KUBECONFIG` را به مقدار اولیه‌اش بازگردانید. برای نمونه:<br>

### لینوکس

```shell
export KUBECONFIG="$KUBECONFIG_SAVED"
```

### ویندوز PowerShell

```powershell
$Env:KUBECONFIG=$ENV:KUBECONFIG_SAVED
```

## بررسی هویت (subject) معرفی‌شده در kubeconfig

همیشه روشن نیست که پس از احراز هویت در کلاستر، چه ویژگی‌هایی (نام کاربری، گروه‌ها) خواهید داشت. اگر هم‌زمان بیش از یک کلاستر را مدیریت کنید، این موضوع حتی دشوارتر نیز می‌شود.

برای بررسی ویژگی‌های هویت، مانند نام کاربری، در زمینهٔ کلاینت کوبرنتیزِ انتخاب‌شده، یک زیردستور `kubectl` وجود دارد: `kubectl auth whoami`.

برای آشنایی دقیق‌تر با این موضوع، [دسترسی API به اطلاعات احراز هویت یک کلاینت](/docs/reference/access-authn-authz/authentication/#self-subject-review) را بخوانید.


## {{% heading "whatsnext" %}}

* [سازمان‌دهی دسترسی به کلاستر با استفاده از فایل‌های kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
* [kubectl config](/docs/reference/generated/kubectl/kubectl-commands#config)
