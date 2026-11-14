---
title: پیکربندی یک Pod برای استفاده از ConfigMap
content_type: task
weight: 190
card:
  name: tasks
  weight: 50
---

<!-- overview -->
بسیاری از برنامه‌ها به پیکربندی‌هایی وابسته‌اند که هنگام راه‌اندازی اولیه یا در زمان اجرای برنامه استفاده می‌شوند.
در بیشتر موارد لازم است مقادیری را که به پارامترهای پیکربندی نسبت داده شده‌اند، تغییر دهید.
آبجکت‌های ConfigMap سازوکاری در کوبرنتیز هستند که با آن‌ها می‌توانید داده‌های پیکربندی را به
{{< glossary_tooltip text="پادهای" term_id="pod" >}} برنامه تزریق کنید.

مفهوم ConfigMap به شما امکان می‌دهد مصنوعات پیکربندی را از محتوای ایمیج جدا کنید تا برنامه‌های
کانتینری‌شده قابل‌حمل باقی بمانند. برای مثال، می‌توانید یک
{{< glossary_tooltip text="ایمیج کانتینر" term_id="image" >}} واحد را دانلود و اجرا کنید و از آن
برای راه‌اندازی کانتینرهایی با اهداف توسعهٔ محلی، آزمون سیستم یا اجرای بار کاری عملیاتی برای کاربران نهایی استفاده کنید.

این صفحه مجموعه‌ای از مثال‌های کاربردی ارائه می‌دهد که نشان می‌دهند چگونه ConfigMap ایجاد کنید و
Podها را با داده‌های ذخیره‌شده در ConfigMapها پیکربندی کنید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

لازم است ابزار `wget` را نصب کرده باشید. اگر به‌جای `wget` ابزار دیگری
مانند `curl` در اختیار دارید، باید مرحلهٔ دانلود داده‌های نمونه را
متناسب با آن تغییر دهید.

<!-- steps -->

## ایجاد یک ConfigMap

برای ایجاد یک ConfigMap می‌توانید از دستور `kubectl create configmap` یا از یک مولد ConfigMap
در فایل `kustomization.yaml` استفاده کنید.

### ایجاد یک ConfigMap با استفاده از `kubectl create configmap`

با دستور `kubectl create configmap` می‌توانید ConfigMapها را از
[دایرکتوری‌ها](#create-configmaps-from-directories)، [فایل‌ها](#create-configmaps-from-files)
یا [مقادیر لفظی](#create-configmaps-from-literal-values) ایجاد کنید:

```shell
kubectl create configmap <map-name> <data-source>
```

در این دستور، \<map-name> نامی است که می‌خواهید به ConfigMap بدهید و \<data-source>
دایرکتوری، فایل یا مقدار لفظی‌ای است که داده‌ها از آن خوانده می‌شوند.
نام یک آبجکت ConfigMap باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

هنگامی که ConfigMap را بر پایهٔ یک فایل ایجاد می‌کنید، کلید در \<data-source> به‌طور پیش‌فرض
نام پایهٔ (basename) فایل و مقدار آن به‌طور پیش‌فرض محتوای فایل است.

برای دریافت اطلاعات دربارهٔ یک ConfigMap می‌توانید از
[`kubectl describe`](/docs/reference/generated/kubectl/kubectl-commands/#describe) یا
[`kubectl get`](/docs/reference/generated/kubectl/kubectl-commands/#get) استفاده کنید.

#### ایجاد یک ConfigMap از یک دایرکتوری {#create-configmaps-from-directories}

با `kubectl create configmap` می‌توانید از چندین فایل موجود در یک دایرکتوری، یک ConfigMap
بسازید. هنگامی که ConfigMap را بر پایهٔ یک دایرکتوری ایجاد می‌کنید، kubectl فایل‌هایی از آن
دایرکتوری را که نامشان یک کلید معتبر است شناسایی می‌کند و هر یک از آن‌ها را در ConfigMap جدید
بسته‌بندی می‌کند. همهٔ مدخل‌های دایرکتوری به‌جز فایل‌های معمولی نادیده گرفته می‌شوند (برای مثال:
زیردایرکتوری‌ها، پیوندهای نمادین، دستگاه‌ها، لوله‌ها و موارد دیگر).

{{< note >}}
نام هر فایلی که برای ایجاد ConfigMap استفاده می‌شود باید فقط از نویسه‌های مجاز تشکیل شده باشد.
این نویسه‌ها عبارت‌اند از: حروف (`A` تا `Z` و `a` تا `z`)، ارقام (`0` تا `9`)، '-'، '_' یا '.'.
اگر `kubectl create configmap` را روی دایرکتوری‌ای اجرا کنید که نام یکی از فایل‌های آن
نویسهٔ غیرمجاز داشته باشد، ممکن است دستور `kubectl` با شکست مواجه شود.

دستور `kubectl` هنگام برخورد با نام فایل نامعتبر، خطایی چاپ نمی‌کند.
{{< /note >}}

دایرکتوری محلی را ایجاد کنید:

```shell
mkdir -p configure-pod-container/configmap/
```

اکنون پیکربندی نمونه را دانلود کنید و ConfigMap را بسازید:

```shell
# Download the sample files into `configure-pod-container/configmap/` directory
wget https://kubernetes.io/examples/configmap/game.properties -O configure-pod-container/configmap/game.properties
wget https://kubernetes.io/examples/configmap/ui.properties -O configure-pod-container/configmap/ui.properties

# Create the ConfigMap
kubectl create configmap game-config --from-file=configure-pod-container/configmap/
```

دستور بالا هر فایل موجود در دایرکتوری `configure-pod-container/configmap/`، یعنی در اینجا
`game.properties` و `ui.properties` را در ConfigMap با نام game-config بسته‌بندی می‌کند.
با دستور زیر می‌توانید جزئیات این ConfigMap را نمایش دهید:

```shell
kubectl describe configmaps game-config
```

خروجی مشابه زیر است:
```
Name:         game-config
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
game.properties:
----
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
ui.properties:
----
color.good=purple
color.bad=yellow
allow.textmode=true
how.nice.to.look=fairlyNice
```

فایل‌های `game.properties` و `ui.properties` موجود در دایرکتوری `configure-pod-container/configmap/`
در بخش `data` این ConfigMap نمایش داده می‌شوند.

```shell
kubectl get configmaps game-config -o yaml
```
خروجی مشابه زیر است:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2022-02-18T18:52:05Z
  name: game-config
  namespace: default
  resourceVersion: "516"
  uid: b4952dc3-d670-11e5-8cd0-68f728db1985
data:
  game.properties: |
    enemies=aliens
    lives=3
    enemies.cheat=true
    enemies.cheat.level=noGoodRotten
    secret.code.passphrase=UUDDLRLRBABAS
    secret.code.allowed=true
    secret.code.lives=30
  ui.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true
    how.nice.to.look=fairlyNice
```

#### ایجاد ConfigMap از فایل‌ها

با `kubectl create configmap` می‌توانید از یک فایل منفرد یا از چندین فایل، یک ConfigMap
ایجاد کنید.

برای مثال، دستور

```shell
kubectl create configmap game-config-2 --from-file=configure-pod-container/configmap/game.properties
```

ConfigMap زیر را ایجاد می‌کند:

```shell
kubectl describe configmaps game-config-2
```

که خروجی آن مشابه زیر است:

```
Name:         game-config-2
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
game.properties:
----
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
```

برای ایجاد یک ConfigMap از چندین منبع داده، می‌توانید آرگومان `--from-file` را چند بار
به دستور بدهید.

```shell
kubectl create configmap game-config-2 --from-file=configure-pod-container/configmap/game.properties --from-file=configure-pod-container/configmap/ui.properties
```

با دستور زیر می‌توانید جزئیات ConfigMap با نام `game-config-2` را نمایش دهید:

```shell
kubectl describe configmaps game-config-2
```

خروجی مشابه زیر است:

```
Name:         game-config-2
Namespace:    default
Labels:       <none>
Annotations:  <none>

Data
====
game.properties:
----
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
ui.properties:
----
color.good=purple
color.bad=yellow
allow.textmode=true
how.nice.to.look=fairlyNice
```

برای ایجاد ConfigMap از یک فایل env از گزینهٔ `--from-env-file` استفاده کنید؛ برای مثال:

```shell
# Env-files contain a list of environment variables.
# These syntax rules apply:
#   Each line in an env file has to be in VAR=VAL format.
#   Lines beginning with # (i.e. comments) are ignored.
#   Blank lines are ignored.
#   There is no special handling of quotation marks (i.e. they will be part of the ConfigMap value)).

# Download the sample files into `configure-pod-container/configmap/` directory
wget https://kubernetes.io/examples/configmap/game-env-file.properties -O configure-pod-container/configmap/game-env-file.properties
wget https://kubernetes.io/examples/configmap/ui-env-file.properties -O configure-pod-container/configmap/ui-env-file.properties

# The env-file `game-env-file.properties` looks like below
cat configure-pod-container/configmap/game-env-file.properties
enemies=aliens
lives=3
allowed="true"

# This comment and the empty line above it are ignored
```

دستور

```shell
kubectl create configmap game-config-env-file \
       --from-env-file=configure-pod-container/configmap/game-env-file.properties
```

یک ConfigMap ایجاد می‌کند. این ConfigMap را مشاهده کنید:

```shell
kubectl get configmap game-config-env-file -o yaml
```

خروجی مشابه زیر است:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2019-12-27T18:36:28Z
  name: game-config-env-file
  namespace: default
  resourceVersion: "809965"
  uid: d9d1ca5b-eb34-11e7-887b-42010a8002b8
data:
  allowed: '"true"'
  enemies: aliens
  lives: "3"
```

از کوبرنتیز نسخهٔ v1.23 به بعد، ابزار `kubectl` امکان مشخص‌کردن چندبارهٔ آرگومان `--from-env-file`
را برای ایجاد ConfigMap از چندین منبع داده پشتیبانی می‌کند.

```shell
kubectl create configmap config-multi-env-files \
        --from-env-file=configure-pod-container/configmap/game-env-file.properties \
        --from-env-file=configure-pod-container/configmap/ui-env-file.properties
```

این دستور ConfigMap زیر را ایجاد می‌کند:

```shell
kubectl get configmap config-multi-env-files -o yaml
```

که خروجی آن مشابه زیر است:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2019-12-27T18:38:34Z
  name: config-multi-env-files
  namespace: default
  resourceVersion: "810136"
  uid: 252c4572-eb35-11e7-887b-42010a8002b8
data:
  allowed: '"true"'
  color: purple
  enemies: aliens
  how: fairlyNice
  lives: "3"
  textmode: "true"
```

#### تعیین کلید هنگام ایجاد ConfigMap از یک فایل

هنگام استفاده از آرگومان `--from-file` می‌توانید کلیدی غیر از نام فایل را برای استفاده در
بخش `data` ConfigMap خود تعیین کنید:

```shell
kubectl create configmap game-config-3 --from-file=<my-key-name>=<path-to-file>
```

در این دستور، `<my-key-name>` کلیدی است که می‌خواهید در ConfigMap استفاده کنید و `<path-to-file>`
مکان فایل منبع داده‌ای است که می‌خواهید آن کلید نمایانگرش باشد.

برای مثال:

```shell
kubectl create configmap game-config-3 --from-file=game-special-key=configure-pod-container/configmap/game.properties
```

این دستور ConfigMap زیر را ایجاد می‌کند:
```
kubectl get configmaps game-config-3 -o yaml
```

که خروجی آن مشابه زیر است:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2022-02-18T18:54:22Z
  name: game-config-3
  namespace: default
  resourceVersion: "530"
  uid: 05f8da22-d671-11e5-8cd0-68f728db1985
data:
  game-special-key: |
    enemies=aliens
    lives=3
    enemies.cheat=true
    enemies.cheat.level=noGoodRotten
    secret.code.passphrase=UUDDLRLRBABAS
    secret.code.allowed=true
    secret.code.lives=30
```

#### ایجاد ConfigMap از مقادیر لفظی

با استفاده از `kubectl create configmap` همراه با آرگومان `--from-literal` می‌توانید یک مقدار
لفظی را از خط فرمان تعریف کنید:

```shell
kubectl create configmap special-config --from-literal=special.how=very --from-literal=special.type=charm
```

می‌توانید چندین جفت کلید-مقدار را به دستور بدهید. هر جفتی که در خط فرمان وارد می‌شود، به‌صورت
یک مدخل جداگانه در بخش `data` ConfigMap نمایش داده می‌شود.

```shell
kubectl get configmaps special-config -o yaml
```

خروجی مشابه زیر است:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2022-02-18T19:14:38Z
  name: special-config
  namespace: default
  resourceVersion: "651"
  uid: dadce046-d673-11e5-8cd0-68f728db1985
data:
  special.how: very
  special.type: charm
```

### ایجاد ConfigMap با مولد

همچنین می‌توانید یک ConfigMap را با مولدها بسازید و سپس آن را اعمال کنید تا آبجکت مربوط در
سرور API کلاستر ایجاد شود.
مولدها را باید در یک فایل `kustomization.yaml` درون یک دایرکتوری مشخص کنید.

#### تولید ConfigMap از فایل‌ها

برای مثال، برای تولید یک ConfigMap از فایل `configure-pod-container/configmap/game.properties`:

```shell
# Create a kustomization.yaml file with ConfigMapGenerator
cat <<EOF >./kustomization.yaml
configMapGenerator:
- name: game-config-4
  options:
    labels:
      game-config: config-4
  files:
  - configure-pod-container/configmap/game.properties
EOF
```

دایرکتوری kustomization را اعمال کنید تا آبجکت ConfigMap ایجاد شود:

```shell
kubectl apply -k .
```
```
configmap/game-config-4-m9dm2f92bt created
```

می‌توانید ایجادشدن ConfigMap را به این صورت بررسی کنید:

```shell
kubectl get configmap
```
```
NAME                       DATA   AGE
game-config-4-m9dm2f92bt   1      37s
```

و همچنین:

```shell
kubectl describe configmaps/game-config-4-m9dm2f92bt
```
```
Name:         game-config-4-m9dm2f92bt
Namespace:    default
Labels:       game-config=config-4
Annotations:  kubectl.kubernetes.io/last-applied-configuration:
                {"apiVersion":"v1","data":{"game.properties":"enemies=aliens\nlives=3\nenemies.cheat=true\nenemies.cheat.level=noGoodRotten\nsecret.code.p...

Data
====
game.properties:
----
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
Events:  <none>
```

توجه کنید که به نام ConfigMap تولیدشده، پسوندی افزوده شده است که از هش‌کردن محتوا به دست می‌آید.
این کار تضمین می‌کند که هر بار محتوا تغییر کند، یک ConfigMap جدید تولید شود.

#### تعیین کلید هنگام تولید ConfigMap از یک فایل

در مولد ConfigMap می‌توانید کلیدی غیر از نام فایل را برای استفاده تعیین کنید.
برای مثال، برای تولید یک ConfigMap از فایل `configure-pod-container/configmap/game.properties`
با کلید `game-special-key`:

```shell
# Create a kustomization.yaml file with ConfigMapGenerator
cat <<EOF >./kustomization.yaml
configMapGenerator:
- name: game-config-5
  options:
    labels:
      game-config: config-5
  files:
  - game-special-key=configure-pod-container/configmap/game.properties
EOF
```

دایرکتوری kustomization را اعمال کنید تا آبجکت ConfigMap ایجاد شود.
```shell
kubectl apply -k .
```
```
configmap/game-config-5-m67dt67794 created
```

#### تولید ConfigMap از مقادیر لفظی

این مثال نشان می‌دهد چگونه با استفاده از Kustomize و kubectl، یک `ConfigMap` را از دو جفت
کلید/مقدار لفظی `special.type=charm` و `special.how=very` ایجاد کنید. برای این کار
می‌توانید مولد `ConfigMap` را مشخص کنید. فایل `kustomization.yaml` را ایجاد کنید (یا جایگزین کنید)
تا محتوای زیر را داشته باشد:

```yaml
---
# kustomization.yaml contents for creating a ConfigMap from literals
configMapGenerator:
- name: special-config-2
  literals:
  - special.how=very
  - special.type=charm
```

دایرکتوری kustomization را اعمال کنید تا آبجکت ConfigMap ایجاد شود:
```shell
kubectl apply -k .
```
```
configmap/special-config-2-c92b5mmcf2 created
```

## پاک‌سازی میانی

پیش از ادامه، برخی از ConfigMapهایی را که ساخته‌اید پاک کنید:

```bash
kubectl delete configmap special-config
kubectl delete configmap env-config
kubectl delete configmap -l 'game-config in (config-4,config-5)'
```

اکنون که تعریف ConfigMapها را یاد گرفته‌اید، می‌توانید به بخش بعدی بروید و
با نحوهٔ استفاده از این آبجکت‌ها همراه با Podها آشنا شوید.

---

## تعریف متغیرهای محیطی کانتینر با داده‌های ConfigMap

### تعریف یک متغیر محیطی کانتینر با داده‌های یک ConfigMap واحد

1. یک متغیر محیطی را به‌صورت یک جفت کلید-مقدار در یک ConfigMap تعریف کنید:

   ```shell
   kubectl create configmap special-config --from-literal=special.how=very
   ```

2. مقدار `special.how` تعریف‌شده در ConfigMap را در مشخصات Pod به متغیر محیطی
   `SPECIAL_LEVEL_KEY` نسبت دهید.

   {{% code_sample file="pods/pod-single-configmap-env-variable.yaml" %}}

   Pod را ایجاد کنید:

   ```shell
   kubectl create -f https://kubernetes.io/examples/pods/pod-single-configmap-env-variable.yaml
   ```

   اکنون خروجی Pod شامل متغیر محیطی `SPECIAL_LEVEL_KEY=very` است.

### تعریف متغیرهای محیطی کانتینر با داده‌های چند ConfigMap

همانند مثال قبل، ابتدا ConfigMapها را ایجاد کنید.
مانیفستی که استفاده خواهید کرد این است:

{{% code_sample file="configmap/configmaps.yaml" %}}

* ConfigMap را ایجاد کنید:

  ```shell
  kubectl create -f https://kubernetes.io/examples/configmap/configmaps.yaml
  ```

* متغیرهای محیطی را در مشخصات Pod تعریف کنید.

  {{% code_sample file="pods/pod-multiple-configmap-env-variable.yaml" %}}

  Pod را ایجاد کنید:

  ```shell
  kubectl create -f https://kubernetes.io/examples/pods/pod-multiple-configmap-env-variable.yaml
  ```

  اکنون خروجی Pod شامل متغیرهای محیطی `SPECIAL_LEVEL_KEY=very` و `LOG_LEVEL=INFO` است.

  هر گاه آمادهٔ ادامه بودید، آن Pod و ConfigMap را حذف کنید:
  ```shell
  kubectl delete pod dapi-test-pod --now
  kubectl delete configmap special-config
  kubectl delete configmap env-config
  ```

## پیکربندی همهٔ جفت‌های کلید-مقدار یک ConfigMap به‌عنوان متغیرهای محیطی کانتینر

* یک ConfigMap شامل چندین جفت کلید-مقدار ایجاد کنید.

  {{% code_sample file="configmap/configmap-multikeys.yaml" %}}

  ConfigMap را ایجاد کنید:

  ```shell
  kubectl create -f https://kubernetes.io/examples/configmap/configmap-multikeys.yaml
  ```

* با استفاده از `envFrom` همهٔ داده‌های ConfigMap را به‌عنوان متغیرهای محیطی کانتینر تعریف کنید.
  هر کلید ConfigMap به نام متغیر محیطی در Pod تبدیل می‌شود.

  {{% code_sample file="pods/pod-configmap-envFrom.yaml" %}}

  Pod را ایجاد کنید:

  ```shell
  kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-envFrom.yaml
  ```
  اکنون خروجی Pod شامل متغیرهای محیطی `SPECIAL_LEVEL=very` و
  `SPECIAL_TYPE=charm` است.

  هر گاه آمادهٔ ادامه بودید، آن Pod را حذف کنید:
  ```shell
  kubectl delete pod dapi-test-pod --now
  ```

## استفاده از متغیرهای محیطی تعریف‌شده در ConfigMap در فرمان‌های Pod

می‌توانید متغیرهای محیطی تعریف‌شده در ConfigMap را با استفاده از نحو جایگزینی کوبرنتیز
`$(VAR_NAME)` در فیلدهای `command` و `args` یک کانتینر به کار ببرید.

برای مثال، مانیفست Pod زیر را در نظر بگیرید:

{{% code_sample file="pods/pod-configmap-env-var-valueFrom.yaml" %}}

آن Pod را با اجرای دستور زیر ایجاد کنید:

```shell
kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-env-var-valueFrom.yaml
```

این پاد خروجی زیر را از کانتینر `test-container` تولید می‌کند:
```shell
kubectl logs dapi-test-pod
```

```
very charm
```

هر گاه آمادهٔ ادامه بودید، آن Pod را حذف کنید:
```shell
kubectl delete pod dapi-test-pod --now
```

## افزودن داده‌های ConfigMap به یک حجم (Volume)

همان‌طور که در [ایجاد ConfigMap از فایل‌ها](#create-configmaps-from-files) توضیح داده شد،
هنگامی که با استفاده از `--from-file` یک ConfigMap ایجاد می‌کنید، نام فایل به کلیدی تبدیل می‌شود
که در بخش `data` ConfigMap ذخیره می‌شود و محتوای فایل، مقدار آن کلید می‌شود.

مثال‌های این بخش به یک ConfigMap با نام `special-config` اشاره دارند:

{{% code_sample file="configmap/configmap-multikeys.yaml" %}}

ConfigMap را ایجاد کنید:

```shell
kubectl create -f https://kubernetes.io/examples/configmap/configmap-multikeys.yaml
```

### پر کردن یک حجم (Volume) با داده‌های ذخیره‌شده در ConfigMap

نام ConfigMap را در بخش `volumes` مشخصات Pod اضافه کنید. با این کار، داده‌های ConfigMap به دایرکتوری‌ای افزوده می‌شوند که با `volumeMounts.mountPath` مشخص شده است (در این مثال، `/etc/config`). بخش `command` فایل‌های این دایرکتوری را فهرست می‌کند؛ نام این فایل‌ها با کلیدهای ConfigMap یکسان است.

{{% code_sample file="pods/pod-configmap-volume.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-volume.yaml
```

هنگامی که Pod اجرا می‌شود، فرمان `ls /etc/config/` خروجی زیر را تولید می‌کند:

```
SPECIAL_LEVEL
SPECIAL_TYPE
```

داده‌های متنی با کدگذاری نویسه‌ای UTF-8 به شکل فایل در دسترس قرار می‌گیرند. برای استفاده از کدگذاری نویسه‌ای دیگر، از `binaryData` استفاده کنید (برای جزئیات بیشتر، [آبجکت ConfigMap](/docs/concepts/configuration/configmap/#configmap-object) را ببینید).

{{< note >}}
اگر در دایرکتوری `/etc/config` آن ایمیج کانتینر فایل‌هایی وجود داشته باشد، اتصال (mount) حجم باعث می‌شود آن فایل‌های ایمیج دیگر در دسترس نباشند.
{{< /note >}}

هر زمان آماده بودید که ادامه دهید، آن Pod را حذف کنید:
```shell
kubectl delete pod dapi-test-pod --now
```

### افزودن داده‌های ConfigMap به مسیری مشخص در حجم

با فیلد `path` می‌توانید مسیر فایل دلخواه را برای اقلام مشخصی از ConfigMap تعیین کنید. در این مثال، قلم `SPECIAL_LEVEL` در حجم `config-volume` و در مسیر `/etc/config/keys` متصل می‌شود.

{{% code_sample file="pods/pod-configmap-volume-specific-key.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-volume-specific-key.yaml
```

هنگامی که Pod اجرا می‌شود، فرمان `cat /etc/config/keys` خروجی زیر را تولید می‌کند:

```
very
```

{{< caution >}}
مانند قبل، همهٔ فایل‌هایی که پیش‌تر در دایرکتوری `/etc/config/` وجود داشتند، دیگر در دسترس نخواهند بود.
{{< /caution >}}

آن Pod را حذف کنید:
```shell
kubectl delete pod dapi-test-pod --now
```

### نگاشت کلیدها به مسیرهای مشخص و تعیین مجوزهای فایل

می‌توانید کلیدها را به مسیرهای مشخصی نگاشت (project) کنید. برای آشنایی با نحوهٔ نگارش، به بخش مربوط در راهنمای [Secretها](/docs/tasks/inject-data-application/distribute-credentials-secure/#project-secret-keys-to-specific-file-paths) مراجعه کنید.  
همچنین می‌توانید برای کلیدها مجوزهای POSIX تعیین کنید. برای آشنایی با نحوهٔ نگارش، به بخش مربوط در راهنمای [Secretها](/docs/tasks/inject-data-application/distribute-credentials-secure/#set-posix-permissions-for-secret-keys) مراجعه کنید.

### ارجاع‌های اختیاری

می‌توان ارجاع به یک ConfigMap را _اختیاری_ علامت‌گذاری کرد. اگر ConfigMap وجود نداشته باشد، حجم متصل‌شده خالی خواهد بود. اگر ConfigMap وجود داشته باشد اما کلید ارجاع‌داده‌شده در آن نباشد، مسیر متناظر زیر نقطهٔ اتصال ایجاد نمی‌شود. برای جزئیات بیشتر، [ConfigMapهای اختیاری](#optional-configmaps) را ببینید.

### ConfigMapهای متصل‌شده به‌طور خودکار به‌روزرسانی می‌شوند

وقتی یک ConfigMap متصل‌شده به‌روزرسانی می‌شود، محتوای نگاشت‌شدهٔ آن نیز سرانجام به‌روزرسانی می‌شود. این موضوع در حالتی هم صدق می‌کند که ConfigMapی که به‌صورت اختیاری به آن ارجاع داده شده است، پس از شروع Pod ایجاد شود.

‏Kubelet در هر همگام‌سازی دوره‌ای بررسی می‌کند که آیا ConfigMap متصل‌شده به‌روز است یا نه. با این حال، برای دریافت مقدار فعلی ConfigMap از حافظهٔ نهان (cache) محلی خود که مبتنی بر TTL است استفاده می‌کند. در نتیجه، کل تأخیر از لحظهٔ به‌روزرسانی ConfigMap تا لحظه‌ای که کلیدهای جدید در Pod نگاشت می‌شوند، می‌تواند به اندازهٔ مجموع دورهٔ همگام‌سازی kubelet (به‌طور پیش‌فرض ۱ دقیقه) و TTL حافظهٔ نهان ConfigMapها در kubelet (به‌طور پیش‌فرض ۱ دقیقه) باشد. با به‌روزرسانی یکی از حاشیه‌نویسی‌های (annotation) Pod می‌توانید بازخوانی فوری را راه‌اندازی کنید.

{{< note >}}
کانتینری که از یک ConfigMap به‌عنوان حجم [subPath](/docs/concepts/storage/volumes/#using-subpath) استفاده می‌کند، به‌روزرسانی‌های ConfigMap را دریافت نخواهد کرد.
{{< /note >}}

<!-- discussion -->

## آشنایی با ConfigMapها و Podها

منبع ConfigMap در API، داده‌های پیکربندی را به شکل جفت‌های کلید-مقدار ذخیره می‌کند. این داده‌ها را می‌توان در Podها مصرف کرد یا از آن‌ها برای تأمین پیکربندی مؤلفه‌های سیستمی مانند کنترل‌کننده‌ها استفاده کرد. ConfigMap شبیه [Secretها](/docs/concepts/configuration/secret/) است، اما راهی برای کار با رشته‌هایی فراهم می‌کند که اطلاعات حساس ندارند. هم کاربران و هم مؤلفه‌های سیستمی می‌توانند داده‌های پیکربندی را در ConfigMap ذخیره کنند.

{{< note >}}
ConfigMapها باید به فایل‌های properties ارجاع دهند، نه اینکه جایگزین آن‌ها شوند. ConfigMap را چیزی شبیه دایرکتوری `/etc` در لینوکس و محتویات آن در نظر بگیرید. برای مثال، اگر از یک ConfigMap یک [حجم کوبرنتیز](/docs/concepts/storage/volumes/) بسازید، هر قلم داده در ConfigMap با یک فایل جداگانه در آن حجم نمایش داده می‌شود.
{{< /note >}}

فیلد `data` در ConfigMap داده‌های پیکربندی را در خود دارد. همان‌طور که در مثال زیر نشان داده شده است، این داده‌ها می‌توانند ساده باشند (مانند ویژگی‌های جداگانه‌ای که با `--from-literal` تعریف می‌شوند) یا پیچیده (مانند فایل‌های پیکربندی یا قطعه‌های JSON که با `--from-file` تعریف می‌شوند).

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T19:14:38Z
  name: example-config
  namespace: default
data:
  # example of a simple property defined using --from-literal
  example.property.1: hello
  example.property.2: world
  # example of a complex property defined using --from-file
  example.property.file: |-
    property.1=value-1
    property.2=value-2
    property.3=value-3
```

وقتی `kubectl` یک ConfigMap را از ورودی‌هایی می‌سازد که ASCII یا UTF-8 نیستند، این ابزار آن‌ها را به‌جای `data` در فیلد `binaryData` آن ConfigMap قرار می‌دهد. می‌توان منابع دادهٔ متنی و دودویی را در یک ConfigMap با هم ترکیب کرد.

اگر می‌خواهید کلیدهای `binaryData` (و مقادیر آن‌ها) را در یک ConfigMap مشاهده کنید، می‌توانید فرمان `kubectl get configmap -o jsonpath='{.binaryData}' <name>` را اجرا کنید.

‏Podها می‌توانند داده‌ها را از ConfigMapی بارگذاری کنند که از `data` یا `binaryData` استفاده می‌کند.

## ConfigMapهای اختیاری

می‌توانید در مشخصات یک Pod، ارجاع به یک ConfigMap را _اختیاری_ علامت‌گذاری کنید. اگر ConfigMap وجود نداشته باشد، پیکربندی‌ای که این ConfigMap داده‌های آن را در Pod فراهم می‌کند (برای مثال، متغیر محیطی یا حجم متصل‌شده) خالی خواهد بود. اگر ConfigMap وجود داشته باشد اما کلید ارجاع‌داده‌شده در آن نباشد، داده‌ها باز هم خالی خواهند بود.

برای مثال، مشخصات Pod زیر یک متغیر محیطی برگرفته از یک ConfigMap را اختیاری علامت‌گذاری می‌کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox
      command: ["/bin/sh", "-c", "env"]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: a-config
              key: akey
              optional: true # mark the variable as optional
  restartPolicy: Never
```

اگر این Pod را اجرا کنید و ConfigMapی با نام `a-config` وجود نداشته باشد، خروجی خالی خواهد بود. اگر این Pod را اجرا کنید و ConfigMapی با نام `a-config` وجود داشته باشد اما کلیدی با نام `akey` نداشته باشد، خروجی باز هم خالی خواهد بود. اما اگر برای `akey` در ConfigMap با نام `a-config` مقداری تعیین کنید، این Pod آن مقدار را چاپ می‌کند و سپس خاتمه می‌یابد.

همچنین می‌توانید حجم‌ها و فایل‌هایی را که یک ConfigMap فراهم می‌کند، اختیاری علامت‌گذاری کنید. کوبرنتیز همیشه مسیرهای اتصال حجم را ایجاد می‌کند، حتی اگر ConfigMap یا کلید ارجاع‌داده‌شده وجود نداشته باشد. برای مثال، مشخصات Pod زیر حجمی را که به یک ConfigMap ارجاع می‌دهد، اختیاری علامت‌گذاری می‌کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox
      command: ["/bin/sh", "-c", "ls /etc/config"]
      volumeMounts:
      - name: config-volume
        mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: no-config
        optional: true # mark the source ConfigMap as optional
  restartPolicy: Never
```



## محدودیت‌ها

- باید آبجکت `ConfigMap` را پیش از ارجاع به آن در مشخصات Pod ایجاد کنید. راه دیگر این است که ارجاع به ConfigMap را در مشخصات Pod به‌صورت `optional` علامت‌گذاری کنید ([ConfigMapهای اختیاری](#optional-configmaps) را ببینید). اگر به ConfigMapی ارجاع دهید که وجود ندارد و ارجاع را `optional` علامت‌گذاری نکنید، Pod شروع به کار نخواهد کرد. به همین ترتیب، ارجاع به کلیدهایی که در ConfigMap وجود ندارند نیز مانع شروع Pod می‌شود، مگر اینکه ارجاع‌های کلید را `optional` علامت‌گذاری کنید.

- اگر برای تعریف متغیرهای محیطی از ConfigMapها از `envFrom` استفاده کنید، کلیدهایی که نامعتبر تلقی می‌شوند نادیده گرفته می‌شوند. Pod اجازهٔ شروع به کار خواهد داشت، اما نام‌های نامعتبر در گزارش رویدادها (`InvalidVariableNames`) ثبت می‌شوند. پیام گزارش، تک‌تک کلیدهای نادیده‌گرفته‌شده را فهرست می‌کند. برای مثال:

  ```shell
  kubectl get events
  ```

  خروجی مشابه زیر است:
  ```
  LASTSEEN FIRSTSEEN COUNT NAME          KIND  SUBOBJECT  TYPE      REASON                            SOURCE                MESSAGE
  0s       0s        1     dapi-test-pod Pod              Warning   InvalidEnvironmentVariableNames   {kubelet, 127.0.0.1}  Keys [1badkey, 2alsobad] from the EnvFrom configMap default/myconfig were skipped since they are considered invalid environment variable names.
  ```

- هر ConfigMap در یک {{< glossary_tooltip text="فضای نام (namespace)" term_id="namespace" >}} مشخص قرار دارد. Podها فقط می‌توانند به ConfigMapهایی ارجاع دهند که در همان فضای نام Pod قرار دارند.

- نمی‌توانید از ConfigMapها برای {{< glossary_tooltip text="Podهای ایستا" term_id="static-pod" >}} استفاده کنید، زیرا kubelet از این کار پشتیبانی نمی‌کند.

## {{% heading "cleanup" %}}

ConfigMapها و Podهایی را که ساخته‌اید حذف کنید:

```bash
kubectl delete configmaps/game-config configmaps/game-config-2 configmaps/game-config-3 \
               configmaps/game-config-env-file
kubectl delete pod dapi-test-pod --now

# You might already have removed the next set
kubectl delete configmaps/special-config configmaps/env-config
kubectl delete configmap -l 'game-config in (config-4,config-5)'
```

فایل `kustomization.yaml` را که برای تولید ConfigMap از آن استفاده کردید، حذف کنید:

```bash
rm kustomization.yaml
```

اگر دایرکتوری `configure-pod-container` را ایجاد کرده‌اید و دیگر به آن نیازی ندارید، بهتر است آن را نیز حذف کنید یا به سطل بازیافت یا محل فایل‌های حذف‌شده منتقل کنید.

```bash
rm -r configure-pod-container
```

## {{% heading "whatsnext" %}}

* یک مثال واقعی از [پیکربندی Redis با استفاده از ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/) را دنبال کنید.
* مثالی از [به‌روزرسانی پیکربندی از طریق ConfigMap](/docs/tutorials/configuration/updating-configuration-via-a-configmap/) را دنبال کنید.
