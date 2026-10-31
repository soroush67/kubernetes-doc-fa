---
title: ترجیحات کاربر kubectl (kuberc)
content_type: concept
weight: 70
---

{{< feature-state state="beta" for_k8s_version="1.34" >}}

با فایل پیکربندی `kuberc` در کوبرنتیز می‌توانید ترجیحات خود را برای
{{<glossary_tooltip text="kubectl" term_id="kubectl">}}
تعریف کنید؛ مانند گزینه‌های پیش‌فرض و نام‌های مستعار (alias) فرمان‌ها. برخلاف فایل kubeconfig، فایل پیکربندی `kuberc`
هیچ‌گونه جزئیاتی دربارهٔ کلاستر، نام‌های کاربری یا گذرواژه‌ها را **در بر ندارد**.

در رایانه‌های Linux و POSIX، مکان پیش‌فرض این فایل پیکربندی `$HOME/.kube/kuberc` است.
مسیر پیش‌فرض در Windows نیز مشابه است: `%USERPROFILE%\.kube\kuberc`.
برای معرفی مسیر یک فایل kuberc سفارشی به kubectl، از گزینهٔ خط فرمان `--kuberc` استفاده کنید
یا متغیر محیطی `KUBERC` را تنظیم کنید.

در فایل `kuberc` با قالب `kubectl.config.k8s.io/v1beta1` می‌توانید انواع زیر از ترجیحات کاربر را
تعریف کنید:

1. [نام‌های مستعار](#aliases): با آن‌ها می‌توانید نسخه‌های کوتاه‌تری از فرمان‌های پرکاربرد خود
   بسازید و در صورت نیاز، گزینه‌ها و آرگومان‌هایی را نیز برایشان تعیین کنید.
2. [پیش‌فرض‌ها](#defaults): با آن‌ها می‌توانید مقادیر پیش‌فرض گزینه‌ها را برای فرمان‌های
   پرکاربرد خود پیکربندی کنید.
3. [سیاست افزونهٔ اعتبارنامه](#credential-plugin-policy): با آن می‌توانید
   سیاستی برای افزونه‌های اعتبارنامهٔ exec پیکربندی کنید.

## aliases

در پیکربندی `kuberc`، بخش _aliases_ به شما امکان می‌دهد میان‌برهای سفارشی
برای فرمان‌های kubectl تعریف کنید و در صورت نیاز، آرگومان‌ها و پرچم‌های خط فرمان را
از پیش برای آن‌ها تعیین کنید.

مثال زیر یک نام مستعار `kubectl getn` برای زیرفرمان `kubectl get` تعریف می‌کند
و افزون بر آن، قالب خروجی JSON را نیز مشخص می‌کند: `--output=json`.

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
aliases:
- name: getn
  command: get
  options:
   - name: output
     default: json
```

در این مثال، تنظیمات زیر به کار رفته است:

1. `name`: نام مستعار نباید با فرمان‌های داخلی تداخل داشته باشد.
1. `command`: فرمان داخلی زیربنایی‌ای را که نام مستعار شما اجرا می‌کند مشخص می‌کند.
   زیرفرمان‌هایی مانند `create role` نیز پشتیبانی می‌شوند.
1. `options`: مقادیر پیش‌فرض گزینه‌ها را مشخص می‌کند. اگر هنگام اجرای `kubectl`
   گزینه‌ای را صریحاً مشخص کنید، مقداری که وارد می‌کنید بر مقدار پیش‌فرض
   تعریف‌شده در `kuberc` اولویت دارد.

با این نام مستعار، اجرای `kubectl getn pods` به‌طور پیش‌فرض خروجی JSON تولید می‌کند. اما
اگر `kubectl getn pods -oyaml` را اجرا کنید، خروجی در قالب YAML خواهد بود.

طرح‌وارهٔ کامل `kuberc` در [این صفحه](/docs/reference/config-api/kuberc.v1beta1/) در دسترس است.

### prependArgs

مثال بعدی، مثال پیشین را گسترش می‌دهد و بخش `prependArgs` را معرفی می‌کند.
این بخش امکان می‌دهد آرگومان‌های دلخواه را بلافاصله پس از فرمان kubectl
و زیرفرمان آن (در صورت وجود) درج کنید.

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
aliases:
  - name: getn
    command: get
    options:
      - name: output
        default: json
    prependArgs:
      - namespace
```

در این مثال، تنظیمات زیر به کار رفته است:

1. `name`: نام مستعار نباید با فرمان‌های داخلی تداخل داشته باشد.
1. `command`: فرمان داخلی زیربنایی‌ای را که نام مستعار شما اجرا می‌کند مشخص می‌کند.
   زیرفرمان‌هایی مانند `create role` نیز پشتیبانی می‌شوند.
1. `options`: مقادیر پیش‌فرض گزینه‌ها را مشخص می‌کند. اگر هنگام اجرای `kubectl`
   گزینه‌ای را صریحاً مشخص کنید، مقداری که وارد می‌کنید بر مقدار پیش‌فرض
   تعریف‌شده در `kuberc` اولویت دارد.
1. `prependArgs`: آرگومان صریحی را مشخص می‌کند که درست پس از فرمان قرار می‌گیرد.
   در اینجا، این تنظیم به `kubectl get namespace test-ns --output json` تبدیل می‌شود.

### appendArgs

مثال بعدی سازوکاری مشابه افزودن آرگومان‌ها به ابتدای فرمان را معرفی می‌کند؛
اما این بار آرگومان‌ها را به انتهای فرمان kubectl اضافه می‌کنیم.

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
aliases:
- name: runx
  command: run
  options:
    - name: image
      default: busybox
    - name: namespace
      default: test-ns
  appendArgs:
    - --
    - custom-arg
```

در این مثال، تنظیمات زیر به کار رفته است:

1. `name`: نام مستعار نباید با فرمان‌های داخلی تداخل داشته باشد.
1. `command`: فرمان داخلی زیربنایی‌ای را که نام مستعار شما اجرا می‌کند مشخص می‌کند.
   زیرفرمان‌هایی مانند `create role` نیز پشتیبانی می‌شوند.
1. `options`: مقادیر پیش‌فرض گزینه‌ها را مشخص می‌کند. اگر هنگام اجرای `kubectl`
   گزینه‌ای را صریحاً مشخص کنید، مقداری که وارد می‌کنید بر مقدار پیش‌فرض
   تعریف‌شده در `kuberc` اولویت دارد.
1. `appendArgs`: آرگومان‌های صریحی را مشخص می‌کند که در انتهای فرمان قرار می‌گیرند.
   در اینجا، این تنظیم به `kubectl run test-pod --namespace test-ns --image busybox -- custom-arg` تبدیل می‌شود.

## defaults

در پیکربندی `kuberc`، بخش `defaults` به شما امکان می‌دهد مقادیر پیش‌فرض
آرگومان‌های خط فرمان را مشخص کنید.

مثال زیر حذف تعاملی را حالت پیش‌فرض اجرای `kubectl delete`
قرار می‌دهد:

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
defaults:
- command: delete
  options:
    - name: interactive
      default: "true"
```

در این مثال، تنظیمات زیر به کار رفته است:

1. `command`: فرمان داخلی را مشخص می‌کند؛ زیرفرمان‌هایی مانند `create role` نیز پشتیبانی می‌شوند.
1. `options`: مقادیر پیش‌فرض گزینه‌ها را مشخص می‌کند. اگر هنگام اجرای `kubectl`
   گزینه‌ای را صریحاً مشخص کنید، مقداری که وارد می‌کنید بر مقدار پیش‌فرض
   تعریف‌شده در `kuberc` اولویت دارد.

با این تنظیم، اجرای `kubectl delete pod/test-pod` به‌طور پیش‌فرض از شما تأیید می‌خواهد.
اما `kubectl delete pod/test-pod --interactive=false` مرحلهٔ تأیید را نادیده می‌گیرد.

## سیاست افزونهٔ اعتبارنامه

{{< feature-state for_k8s_version="v1.35" state="beta" >}}

ویرایشگران یک فایل `kubeconfig` می‌توانند افزونه‌ای اجرایی را مشخص کنند که برای
دریافت اعتبارنامه و احراز هویت کلاینت در برابر کلاستر به کار می‌رود. در پیکربندی
`kuberc` می‌توانید سیاست اجرای چنین افزونه‌هایی را با دو فیلد سطح بالا
تعیین کنید. هر دو فیلد اختیاری هستند.

### credentialPluginPolicy

با فیلد اختیاری `credentialPluginPolicy` می‌توانید سیاستی برای افزونه‌های
اعتبارنامه پیکربندی کنید. این فیلد سه مقدار معتبر دارد:

1. `"AllowAll"`

وقتی سیاست روی `"AllowAll"` تنظیم شود، هیچ محدودیتی برای اجرای افزونه‌ها
وجود نخواهد داشت. این رفتار با رفتار نسخه‌های کوبرنتیز پیش از 1.35
یکسان است.

2. `"DenyAll"`

وقتی سیاست روی `"DenyAll"` تنظیم شود، اجرای هیچ افزونهٔ exec مجاز نخواهد بود.

3. `"Allowlist"`

وقتی سیاست روی `"Allowlist"` تنظیم شود، کاربر می‌تواند اجرای افزونه‌های اعتبارنامه را
به‌صورت گزینشی مجاز کند. در این حالت **باید** فیلد `credentialPluginAllowlist`
را نیز (آن هم در سطح بالا) مشخص کنید. این فیلد در ادامه
توضیح داده شده است.

{{< note >}}
برای حفظ سازگاری با نسخه‌های پیشین، مشخص‌نکردن `credentialPluginPolicy`
یا خالی گذاشتن آن با تنظیم صریح سیاست روی `"AllowAll"` یکسان است.
{{< /note >}}

### credentialPluginAllowlist

{{< note >}}
تنظیم این فیلد در حالتی که `credentialPluginPolicy` برابر با `Allowlist` نیست (از جمله
وقتی آن فیلد وجود ندارد یا خالی است)، خطای پیکربندی محسوب می‌شود.
{{< /note >}}

فیلد `credentialPluginAllowlist` فهرستی از مجموعه‌معیارها (مجموعه‌هایی از
*الزامات*) را برای مجوز اجرای افزونه‌های اعتبارنامه مشخص می‌کند. هر مجموعه از
الزامات به‌نوبت بررسی می‌شود و به محض اینکه افزونه دست‌کم تمام الزامات یکی از
مجموعه‌ها را برآورده کند، اجرای آن مجاز می‌شود. به بیان دیگر، نتیجهٔ کلی اعمال
فهرست مجاز روی افزونهٔ `my-binary-plugin`، _OR منطقی_ تصمیم‌های حاصل از تک‌تک
موارد فهرست است.

برای نمونه، پیکربندی فهرست مجاز زیر را در نظر بگیرید:

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
credentialPluginPolicy: Allowlist
credentialPluginAllowlist:
  - command: foo
  - command: bar
  - command: baz
```

در مثال بالا، فهرست مجاز اجرای افزونه‌هایی را مجاز می‌کند که فرمان آن‌ها "foo"،
"bar" _یا_ "baz" باشد.

{{< note >}}
هر مجموعه از الزامات برای معتبر بودن **باید** دست‌کم یک فیلد غیرخالی و صریحاً
مشخص‌شده داشته باشد. اگر همهٔ فیلدها خالی یا نامشخص باشند، این وضعیت خطای
پیکربندی محسوب می‌شود و اجرای افزونه مجاز نخواهد بود. همین حکم در مواردی
برقرار است که فیلد `credentialPluginAllowlist` مشخص نشده باشد یا صریحاً
به‌صورت فهرست خالی تعیین شده باشد. هدف از این کار جلوگیری از وضعیتی است
که کاربر کلید `credentialPluginAllowlist` را اشتباه تایپ کند و گمان کند
فهرست مجازی تعیین کرده است، در حالی که در واقع چنین نکرده است.

برای نمونه، پیکربندی زیر نامعتبر است:
```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
credentialPluginPolicy: Allowlist
credentialPluginAllowlist:
  - command: ""
```
{{< /note >}}

##### command

فیلد `command` نام افزونهٔ اعتبارنامه‌ای را مشخص می‌کند که اجرای آن مجاز است. این مقدار را
می‌توان به‌صورت نام پایهٔ (basename) افزونهٔ موردنظر یا مسیر کامل آن مشخص کرد. اگر به‌صورت
نام پایه مشخص شود، تصمیم این فیلد در صورتی «مجاز» است که یکی از دو شرط زیر
برقرار باشد:

1. مقدار فیلد `command` دقیقاً برابر با فیلد `command` افزونه باشد.
1. مسیر کامل هم برای `command` فهرست مجاز و هم برای `command` افزونه
   تعیین شود و نتایج برابر باشند.

اگر به‌صورت مسیر کامل مشخص شود، تصمیم این فیلد در صورتی «مجاز» است که
یکی از شرط‌های زیر برقرار باشد:

1. مقدار فیلد `command` دقیقاً برابر با فیلد `command` افزونه باشد (یعنی
   `command` افزونه نیز مسیر کامل باشد).
1. مسیر کامل برای `command` افزونه تعیین شود و فیلد `command` فهرست مجاز
   دقیقاً با آن مطابقت داشته باشد.

در مورد _تعیین مسیر کامل_ که پیش‌تر در این صفحه به آن اشاره شد،
نه پیوندهای نمادین (symlink) و نه الگوهای glob پوسته تفسیر نمی‌شوند.

برای نمونه، مدخلی در فهرست مجاز را با `command` برابر `/usr/local/bin/my-binary` در نظر بگیرید،
که در آن `/usr/local/bin/my-binary` یک پیوند نمادین به `/this/is/a/target` است. اگر `command`
مشخص‌شده در kubeconfig برابر `/this/is/a/target` باشد، اجرای آن مجاز نخواهد بود. برای
اینکه این حالت کار کند، باید `/this/is/a/target` را صریحاً به فهرست مجاز
اضافه کنید. از سوی دیگر، اگر مقدار `command` در kubeconfig برابر
`/usr/local/bin/my-binary` باشد، فهرست مجاز اجرای آن را مجاز می‌کند.

{{< note >}}
تا زمانی که kuberc در مرحلهٔ بتا است، می‌توان در مدخل‌های فهرست مجاز از `name` به‌عنوان
نام مستعار `command` استفاده کرد. از کوبرنتیز 1.36 به بعد، `name` به نفع `command`
منسوخ شده است. تعیین **هم‌زمان** `name` و `command` در یک مدخل فهرست مجاز
خطا محسوب می‌شود، زیرا این تنظیمات از نظر امنیتی حساس هستند.
فیلد `name` پس از رسیدن kuberc به مرحلهٔ GA به‌طور کامل حذف خواهد شد.
{{< /note >}}

### مثال {#credential-plugin-policy-example}

مثال زیر یک سیاست `"Allowlist"` را همراه با فهرست مجاز آن نشان می‌دهد:

{{< tabs name="tab_with_code" >}}
{{< tab name="POSIX" codelang="yaml" >}}
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
credentialPluginPolicy: Allowlist
credentialPluginAllowlist:
  - command: my-trusted-binary
  - command: /usr/local/bin/my-other-trusted-binary
{{< /tab >}}
{{< tab name="Windows" codelang="yaml" >}}
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
credentialPluginPolicy: Allowlist
credentialPluginAllowlist:
  - command: my-trusted-binary
  - command: "C:\my-other-trusted-binary"
{{< /tab >}}
{{< /tabs >}}

### مدیریت سیاست افزونهٔ اعتبارنامه با `kubectl kuberc set`

به‌جای ویرایش مستقیم فایل kuberc، می‌توانید با `kubectl kuberc set`
سیاست افزونهٔ اعتبارنامه را از خط فرمان پیکربندی کنید.

```shell
# Set the policy to deny all credential plugins
kubectl kuberc set --section credentialplugin --policy DenyAll

# Set the policy to allow all credential plugins
kubectl kuberc set --section credentialplugin --policy AllowAll

# Allow only specific credential plugins
kubectl kuberc set --section credentialplugin \
    --policy Allowlist \
    --allowlist-entry command=my-trusted-binary \
    --allowlist-entry command=my-other-trusted-binary
```

در این مثال، پرچم‌های زیر به کار رفته است:

1. `--section credentialplugin`: بخش پیکربندی افزونهٔ اعتبارنامه را انتخاب می‌کند.
1. `--policy`: الزامی است. سیاست را روی `AllowAll`، `DenyAll` یا `Allowlist` تنظیم می‌کند.
1. `--allowlist-entry`: در صورت استفاده از `--policy=Allowlist` الزامی است. افزونهٔ مجاز را
   با جفت‌های `key=value` جداشده با ویرگول مشخص می‌کند. در حال حاضر `command` تنها
   کلید پشتیبانی‌شده است (برای نمونه، `command=<binary-name>`)، اما این قالب
   برای افزوده‌های آینده مانند راستی‌آزمایی digest یا کلید عمومی طراحی شده است.
   برای مجاز کردن چند افزونه، این پرچم را تکرار کنید.

## پیش‌فرض‌های پیشنهادی

نگه‌دارندگان kubectl توصیه می‌کنند kuberc را با پیش‌فرض‌های زیر به کار بگیرید:

{{< caution >}}
اگر از یک ارائه‌دهندهٔ مدیریت‌شدهٔ کوبرنتیز استفاده می‌کنید، مستندات ارائه‌دهندهٔ خود را
دربارهٔ افزونه‌های exec موردنیاز در محیطتان بررسی کنید و به‌جای آن از سیاست
[«Allowlist»](#credentialPluginPolicy) استفاده کنید.

اگر پس از تنظیم سیاست [«DenyAll»](#credentialPluginPolicy) به شکلی که در ادامه
نشان داده شده است با مشکل مواجه شدید، پیام‌های خطای `kubectl` را بررسی کنید تا
مشخص شود اجرای کدام افزونه‌ها متوقف شده است و آن‌ها را با مستندات ارائه‌دهندهٔ
خود تطبیق دهید. در پایان، سیاست را به «Allowlist» تغییر دهید و افزونه‌های
لازم را در فیلد
[credentialPluginAllowlist](#credentialPluginAllowlist) اضافه کنید.
{{< /caution >}}

```yaml
apiVersion: kubectl.config.k8s.io/v1beta1
kind: Preference
defaults:
  # (1) default server-side apply
  - command: apply
    options:
      - name: server-side
        default: "true"

  # (2) default interactive deletion
  - command: delete
    options:
      - name: interactive
        default: "true"

# See the above note about managed providers before selecting DenyAll
credentialPluginPolicy: DenyAll
```

در این مثال، تنظیمات زیر اعمال می‌شود:
1. به‌طور پیش‌فرض از [اعمال سمت سرور (Server-Side Apply)](/docs/reference/using-api/server-side-apply/) استفاده می‌شود.
1. هر بار که `kubectl delete` اجرا شود، به‌طور پیش‌فرض حذف تعاملی انجام می‌شود تا از
   حذف ناخواستهٔ منابع از کلاستر جلوگیری شود.
1. اجرای هیچ افزونهٔ اعتبارنامهٔ اجرایی مجاز نخواهد بود.

## غیرفعال کردن kuberc

برای غیرفعال کردن موقت قابلیت `kuberc`، متغیر محیطی `KUBERC` را با مقدار `off`
تنظیم (و export) کنید:

```shell
export KUBERC=off
```

یا feature gate مربوط را غیرفعال کنید:

```shell
export KUBECTL_KUBERC=false
```

این کار برای عیب‌یابی و بررسی اینکه آیا `kuberc` شما باعث بروز مشکل شده است یا نه، مفید است.
