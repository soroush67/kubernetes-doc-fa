---
title: ConfigMapها
api_metadata:
- apiVersion: "v1"
  kind: "ConfigMap"
content_type: concept
weight: 20
---

<!-- overview -->

{{< glossary_definition term_id="configmap" prepend="A ConfigMap is" length="all" >}}

{{< caution >}}
ConfigMap هیچ‌گونه محرمانگی یا رمزگذاری‌ای فراهم نمی‌کند.
اگر داده‌هایی که می‌خواهید ذخیره کنید محرمانه‌اند، به‌جای ConfigMap از یک
{{< glossary_tooltip text="Secret" term_id="secret" >}} استفاده کنید،
یا برای خصوصی نگه داشتن داده‌هایتان از ابزارهای اضافی (شخص ثالث) بهره ببرید.
{{< /caution >}}

<!-- body -->
## انگیزه

از ConfigMap برای تنظیم داده‌های پیکربندی به‌صورت جدا از کد برنامه استفاده کنید.

برای نمونه، فرض کنید در حال توسعهٔ برنامه‌ای هستید که می‌توانید آن را روی
رایانهٔ خودتان (برای توسعه) و در ابر (برای رسیدگی به ترافیک واقعی) اجرا کنید.
کد را طوری می‌نویسید که در یک متغیر محیطی به نام `DATABASE_HOST` جست‌وجو کند.
در محیط محلی، آن متغیر را روی `localhost` تنظیم می‌کنید. در ابر، آن را طوری تنظیم می‌کنید که
به یک {{< glossary_tooltip text="Service" term_id="service" >}} کوبرنتیز
اشاره کند که جزء پایگاه داده را در اختیار کلاستر شما قرار می‌دهد.
این کار به شما امکان می‌دهد یک ایمیج کانتینر را که در ابر اجرا می‌شود دریافت کنید و
در صورت نیاز دقیقاً همان کد را به‌صورت محلی اشکال‌زدایی کنید.

{{< note >}}
ConfigMap برای نگهداری حجم‌های بزرگ داده طراحی نشده است. داده‌های ذخیره‌شده در یک
ConfigMap نمی‌توانند از 1 MiB بیشتر باشند. اگر نیاز دارید تنظیماتی را ذخیره کنید که
از این حد بزرگ‌ترند، بهتر است mount کردن یک حجم یا استفاده از یک
پایگاه داده یا سرویس فایل جداگانه را در نظر بگیرید.
{{< /note >}}

## آبجکت ConfigMap

ConfigMap یک {{< glossary_tooltip text="آبجکت API" term_id="object" >}} است
که به شما امکان می‌دهد پیکربندی را برای استفادهٔ سایر آبجکت‌ها ذخیره کنید. برخلاف بیشتر
آبجکت‌های کوبرنتیز که یک `spec` دارند، ConfigMap دارای فیلدهای `data` و `binaryData`
است. این فیلدها جفت‌های کلید-مقدار را به‌عنوان مقدار خود می‌پذیرند. هر دو فیلد `data`
و `binaryData` اختیاری‌اند. فیلد `data` برای نگهداری
رشته‌های UTF-8 طراحی شده است، در حالی که فیلد `binaryData` برای نگهداری
داده‌های دودویی به‌صورت رشته‌های کدگذاری‌شده با base64 طراحی شده است.

نام یک ConfigMap باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

هر کلید زیر فیلد `data` یا `binaryData` باید از
نویسه‌های الفبایی-عددی، `-`، `_` یا `.` تشکیل شده باشد. کلیدهای ذخیره‌شده در `data` نباید
با کلیدهای فیلد `binaryData` هم‌پوشانی داشته باشند.

از نسخهٔ v1.19 به بعد، می‌توانید یک فیلد `immutable` را به تعریف ConfigMap
اضافه کنید تا یک [ConfigMap تغییرناپذیر](#configmap-immutable) ایجاد کنید.

## ConfigMapها و Podها

می‌توانید یک `spec` برای Pod بنویسید که به یک ConfigMap اشاره کند و کانتینر(های)
آن Pod را بر اساس داده‌های ConfigMap پیکربندی کند. Pod و ConfigMap باید در
یک {{< glossary_tooltip text="فضای نام (namespace)" term_id="namespace" >}} یکسان باشند.

{{< note >}}
`spec` یک {{< glossary_tooltip text="Pod ایستا" term_id="static-pod" >}} نمی‌تواند به یک ConfigMap
یا هیچ آبجکت API دیگری اشاره کند.
{{< /note >}}

در اینجا نمونه‌ای از یک ConfigMap آمده است که برخی کلیدهای آن مقادیر منفرد دارند
و مقدار برخی کلیدهای دیگر شبیه قطعه‌ای از یک قالب
پیکربندی است.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: game-demo
data:
  # property-like keys; each key maps to a simple value
  player_initial_lives: "3"
  ui_properties_file_name: "user-interface.properties"

  # file-like keys
  game.properties: |
    enemy.types=aliens,monsters
    player.maximum-lives=5
  user-interface.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true
```

چهار روش مختلف وجود دارد که می‌توانید با آن‌ها از یک ConfigMap برای پیکربندی
یک کانتینر درون یک Pod استفاده کنید:

1. درون فرمان و آرگومان‌های (args) یک کانتینر
1. متغیرهای محیطی برای یک کانتینر
1. افزودن یک فایل در یک حجم فقط‌خواندنی، تا برنامه آن را بخواند
1. نوشتن کدی که درون Pod اجرا شود و با استفاده از API کوبرنتیز یک ConfigMap را بخواند

این روش‌های مختلف برای شیوه‌های متفاوت مدل‌سازی
داده‌های مصرفی مناسب‌اند.
در سه روش نخست،
{{< glossary_tooltip text="kubelet" term_id="kubelet" >}} هنگام راه‌اندازی کانتینر(های) یک Pod
از داده‌های ConfigMap استفاده می‌کند.

روش چهارم به این معناست که باید کدی برای خواندن ConfigMap و داده‌های آن بنویسید.
با این حال، از آنجا که مستقیماً از API کوبرنتیز استفاده می‌کنید، برنامهٔ شما می‌تواند
مشترک دریافت به‌روزرسانی‌ها شود تا هر زمان ConfigMap تغییر کرد مطلع شود و
به آن واکنش نشان دهد. با دسترسی مستقیم به API کوبرنتیز، این
روش همچنین به شما امکان می‌دهد به ConfigMapای در یک فضای نام دیگر دسترسی داشته باشید.

در اینجا نمونه‌ای از یک Pod آمده است که از مقادیر `game-demo` برای پیکربندی یک Pod استفاده می‌کند:

{{% code_sample file="configmap/configure-pod.yaml" %}}

ConfigMap میان مقادیر ویژگی تک‌خطی و
مقادیر چندخطیِ شبیه فایل تفاوتی قائل نمی‌شود.
آنچه اهمیت دارد این است که Podها و سایر آبجکت‌ها چگونه آن مقادیر را مصرف می‌کنند.

در این مثال، تعریف یک حجم و mount کردن آن درون کانتینر `demo`
در مسیر `/config` دو فایل ایجاد می‌کند،
یعنی `/config/game.properties` و `/config/user-interface.properties`،
با اینکه ConfigMap چهار کلید دارد. دلیل این است که تعریف Pod
یک آرایهٔ `items` را در بخش `volumes` مشخص می‌کند.
اگر آرایهٔ `items` را به‌طور کامل حذف کنید، هر کلید در ConfigMap به
فایلی با همان نام کلید تبدیل می‌شود و ۴ فایل خواهید داشت.

## استفاده از ConfigMapها

ConfigMapها را می‌توان به‌عنوان حجم‌های داده mount کرد. ConfigMapها را همچنین می‌توان توسط سایر
بخش‌های سیستم، بدون آنکه مستقیماً در اختیار Pod قرار گیرند، استفاده کرد. برای نمونه،
ConfigMapها می‌توانند داده‌هایی را نگه دارند که سایر بخش‌های سیستم باید برای پیکربندی از آن‌ها استفاده کنند.

رایج‌ترین روش استفاده از ConfigMapها، پیکربندی تنظیمات برای
کانتینرهایی است که در یک Pod در همان فضای نام اجرا می‌شوند. همچنین می‌توانید از یک
ConfigMap به‌صورت جداگانه استفاده کنید.

برای نمونه،
ممکن است با {{< glossary_tooltip text="افزونه‌ها" term_id="addons" >}}
یا {{< glossary_tooltip text="اپراتورهایی" term_id="operator-pattern" >}} مواجه شوید که
رفتار خود را بر اساس یک ConfigMap تنظیم می‌کنند.

### استفاده از ConfigMapها به‌صورت فایل در یک Pod

برای مصرف یک ConfigMap در یک حجم در یک Pod:

1. یک ConfigMap ایجاد کنید یا از یک ConfigMap موجود استفاده کنید. چندین Pod می‌توانند به
   یک ConfigMap یکسان ارجاع دهند.
1. تعریف Pod خود را تغییر دهید تا یک حجم زیر `.spec.volumes[]` اضافه شود. هر نامی
   که می‌خواهید برای حجم انتخاب کنید و فیلد `.spec.volumes[].configMap.name` را طوری تنظیم کنید
   که به آبجکت ConfigMap شما ارجاع دهد.
1. یک `.spec.containers[].volumeMounts[]` به هر کانتینری که به
   ConfigMap نیاز دارد اضافه کنید. `.spec.containers[].volumeMounts[].readOnly = true` را مشخص کنید و
   `.spec.containers[].volumeMounts[].mountPath` را روی نام دایرکتوری بلااستفاده‌ای تنظیم کنید
   که می‌خواهید ConfigMap در آن ظاهر شود.
1. ایمیج یا خط فرمان خود را طوری تغییر دهید که برنامه در آن دایرکتوری به دنبال فایل‌ها بگردد.
   هر کلید در نگاشت `data` مربوط به ConfigMap به نام فایلی
   زیر `mountPath` تبدیل می‌شود.

این نمونه‌ای از یک Pod است که یک ConfigMap را در یک حجم mount می‌کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    configMap:
      name: myconfigmap
```

به هر ConfigMapای که می‌خواهید استفاده کنید باید در `.spec.volumes` ارجاع داده شود.

اگر چندین کانتینر در Pod وجود داشته باشد، هر کانتینر به بلوک `volumeMounts`
مخصوص خود نیاز دارد، اما برای هر ConfigMap تنها یک `.spec.volumes` لازم است.

#### ConfigMapهای mount‌شده به‌طور خودکار به‌روزرسانی می‌شوند

هنگامی که یک ConfigMap که در حال حاضر در یک حجم مصرف می‌شود به‌روزرسانی شود، کلیدهای projectشده نیز سرانجام به‌روزرسانی می‌شوند.
kubelet در هر همگام‌سازی دوره‌ای بررسی می‌کند که آیا ConfigMap mount‌شده به‌روز است یا نه.
با این حال، kubelet برای دریافت مقدار فعلی ConfigMap از حافظهٔ نهان (cache) محلی خود استفاده می‌کند.
نوع حافظهٔ نهان را می‌توان با استفاده از فیلد `configMapAndSecretChangeDetectionStrategy` در
[ساختار KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/) پیکربندی کرد.
یک ConfigMap می‌تواند از طریق watch (پیش‌فرض)، بر پایهٔ ttl، یا با هدایت
همهٔ درخواست‌ها مستقیماً به سرور API منتشر شود.
در نتیجه، کل تأخیر از لحظه‌ای که ConfigMap به‌روزرسانی می‌شود تا لحظه‌ای
که کلیدهای جدید در Pod project می‌شوند می‌تواند به اندازهٔ دورهٔ همگام‌سازی kubelet به‌علاوهٔ تأخیر
انتشار حافظهٔ نهان باشد، که تأخیر انتشار حافظهٔ نهان به نوع حافظهٔ نهان انتخاب‌شده بستگی دارد
(به ترتیب برابر با تأخیر انتشار watch، مقدار ttl حافظهٔ نهان، یا صفر است).

ConfigMapهایی که به‌صورت متغیر محیطی مصرف می‌شوند به‌طور خودکار به‌روزرسانی نمی‌شوند و نیازمند راه‌اندازی مجدد Pod هستند.

{{< note >}}
کانتینری که از یک ConfigMap به‌صورت mount حجم [subPath](/docs/concepts/storage/volumes#using-subpath) استفاده می‌کند، به‌روزرسانی‌های ConfigMap را دریافت نخواهد کرد.
{{< /note >}}


### استفاده از ConfigMapها به‌صورت متغیرهای محیطی

برای استفاده از یک ConfigMap در یک {{< glossary_tooltip text="متغیر محیطی" term_id="container-env-variables" >}}
در یک Pod:

1. برای هر کانتینر در مشخصات Pod خود، به ازای هر کلید ConfigMap که می‌خواهید استفاده کنید
   یک متغیر محیطی به فیلد
   `env[].valueFrom.configMapKeyRef` اضافه کنید.
1. ایمیج و/یا خط فرمان خود را طوری تغییر دهید که برنامه مقادیر را
   در متغیرهای محیطی مشخص‌شده جست‌وجو کند.

این نمونه‌ای از تعریف یک ConfigMap به‌عنوان متغیر محیطی Pod است:

ConfigMap زیر (myconfigmap.yaml) دو ویژگی را ذخیره می‌کند: username و access_level:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
data:
  username: k8s-admin
  access_level: "1"
```

فرمان زیر آبجکت ConfigMap را ایجاد می‌کند:

```shell
kubectl apply -f myconfigmap.yaml
```

Pod زیر محتوای ConfigMap را به‌صورت متغیرهای محیطی مصرف می‌کند:

{{% code_sample file="configmap/env-configmap.yaml" %}}

فیلد `envFrom` به کوبرنتیز دستور می‌دهد از منابعی که درون آن قرار گرفته‌اند متغیرهای محیطی ایجاد کند.
`configMapRef` درونی با نام به یک ConfigMap ارجاع می‌دهد و همهٔ جفت‌های کلید-مقدار آن را انتخاب می‌کند.
Pod را به کلاستر خود اضافه کنید، سپس لاگ‌های آن را بازیابی کنید تا خروجی فرمان printenv را ببینید.
این کار باید تأیید کند که دو جفت کلید-مقدار از ConfigMap به‌عنوان متغیرهای محیطی تنظیم شده‌اند:

```shell
kubectl apply -f env-configmap.yaml
```
```shell
kubectl logs pod/env-configmap
```
خروجی مشابه زیر است:
```console
...
username: "k8s-admin"
access_level: "1"
...
```

گاهی یک Pod به همهٔ مقادیر یک ConfigMap نیاز ندارد.
برای نمونه، ممکن است Pod دیگری داشته باشید که فقط از مقدار username در ConfigMap استفاده می‌کند.
برای این مورد کاربرد، می‌توانید به‌جای آن از نحو `env.valueFrom` استفاده کنید که به شما امکان می‌دهد کلیدهای منفرد را در
یک ConfigMap انتخاب کنید. نام متغیر محیطی همچنین می‌تواند با کلید درون ConfigMap متفاوت باشد.
برای نمونه:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
  - name: envars-test-container
    image: nginx
    env:
    - name: CONFIGMAP_USERNAME
      valueFrom:
        configMapKeyRef:
          name: myconfigmap
          key: username
```

در Podی که از این مانیفست ایجاد می‌شود، خواهید دید که متغیر محیطی
`CONFIGMAP_USERNAME` روی مقدار `username` از ConfigMap تنظیم شده است.
سایر کلیدهای داده‌های ConfigMap در محیط کپی نمی‌شوند.


توجه به این نکته مهم است که بازهٔ نویسه‌های مجاز برای نام متغیرهای
محیطی در Podها [محدود](/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config) است.
اگر کلیدهایی با این قواعد مطابقت نداشته باشند، آن کلیدها در اختیار کانتینر شما قرار نمی‌گیرند،
هرچند Pod اجازهٔ آغاز به کار دارد.

## ConfigMapهای تغییرناپذیر {#configmap-immutable}

{{< feature-state for_k8s_version="v1.21" state="stable" >}}

قابلیت _Secretها و ConfigMapهای تغییرناپذیر_ در کوبرنتیز گزینه‌ای برای تنظیم
Secretها و ConfigMapهای منفرد به‌صورت تغییرناپذیر فراهم می‌کند. برای کلاسترهایی که به‌طور گسترده از ConfigMapها استفاده می‌کنند
(دست‌کم ده‌ها هزار mount یکتای ConfigMap به Pod)، جلوگیری از تغییر
داده‌های آن‌ها مزایای زیر را دارد:

- شما را از به‌روزرسانی‌های تصادفی (یا ناخواسته) که ممکن است باعث از کار افتادن برنامه‌ها شوند محافظت می‌کند
- با بستن watchها برای ConfigMapهایی که به‌عنوان تغییرناپذیر علامت‌گذاری شده‌اند، بار روی kube-apiserver را
  به‌طور چشمگیری کاهش می‌دهد و در نتیجه کارایی کلاستر شما را بهبود می‌بخشد.

می‌توانید با تنظیم فیلد `immutable` روی `true` یک ConfigMap تغییرناپذیر ایجاد کنید.
برای نمونه:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  ...
data:
  ...
immutable: true
```

هنگامی که یک ConfigMap به‌عنوان تغییرناپذیر علامت‌گذاری شود، بازگرداندن این تغییر
یا تغییر محتوای فیلد `data` یا `binaryData` _ممکن نیست_. تنها می‌توانید
ConfigMap را حذف و دوباره ایجاد کنید. از آنجا که Podهای موجود نقطهٔ mount
به ConfigMap حذف‌شده را حفظ می‌کنند، توصیه می‌شود این Podها را دوباره ایجاد کنید.

## {{% heading "whatsnext" %}}

* دربارهٔ [Secretها](/docs/concepts/configuration/secret/) بخوانید.
* مطلب [پیکربندی یک Pod برای استفاده از یک ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) را بخوانید.
* دربارهٔ [تغییر یک ConfigMap (یا هر آبجکت دیگر کوبرنتیز)](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/) بخوانید
* مطلب [The Twelve-Factor App](https://12factor.net/) را بخوانید تا انگیزهٔ
  جداسازی کد از پیکربندی را درک کنید.
