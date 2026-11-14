---
reviewers:
- derekwaynecarr
- janetkuo
title: اشتراک‌گذاری یک کلاستر با فضاهای نام
content_type: task
weight: 340
---

<!-- overview -->
این صفحه نشان می‌دهد که چگونه می‌توان {{< glossary_tooltip text="فضاهای نام" term_id="namespace" >}} را مشاهده کرد، در آن‌ها کار کرد و آن‌ها را حذف کرد.
همچنین در این صفحه نشان داده می‌شود که چگونه می‌توانید با استفاده از فضاهای نام کوبرنتیز، کلاستر خود را به بخش‌های کوچک‌تر تقسیم کنید.

## {{% heading "prerequisites" %}}

* یک [کلاستر کوبرنتیز موجود](/docs/setup/) در اختیار داشته باشید.
* با مفاهیم پایه‌ای {{< glossary_tooltip text="Podها" term_id="pod" >}}،
  {{< glossary_tooltip term_id="service" text="Serviceها" >}} و
  {{< glossary_tooltip text="Deploymentها" term_id="deployment" >}} در کوبرنتیز آشنا باشید.

<!-- steps -->

## مشاهدهٔ فضاهای نام

برای فهرست کردن فضاهای نام فعلی یک کلاستر، از دستور زیر استفاده کنید:

```shell
kubectl get namespaces
```
```console
NAME              STATUS   AGE
default           Active   11d
kube-node-lease   Active   11d
kube-public       Active   11d
kube-system       Active   11d
```

کوبرنتیز در ابتدا با چهار فضای نام اولیه آغاز به کار می‌کند:

* فضای نام `default`: فضای نام پیش‌فرض برای آبجکت‌هایی که فضای نام دیگری برایشان تعیین نشده است.
* فضای نام `kube-node-lease`: این فضای نام آبجکت‌های [Lease](/docs/concepts/architecture/leases/) مرتبط با هر نود را نگه می‌دارد. Leaseهای نود به kubelet امکان می‌دهند [ضربان‌های حیات (heartbeats)](/docs/concepts/architecture/nodes/#heartbeats) را ارسال کند تا control plane بتواند از کار افتادن نود را تشخیص دهد.
* فضای نام `kube-public`: این فضای نام به‌طور خودکار ایجاد می‌شود و برای همهٔ کاربران
  (از جمله کاربرانی که احراز هویت نشده‌اند) قابل خواندن است. این فضای نام عمدتاً برای استفادهٔ خود کلاستر رزرو شده است،
  برای مواردی که برخی منابع باید در سراسر کلاستر به‌صورت عمومی قابل مشاهده و خواندن باشند.
  جنبهٔ عمومی بودن این فضای نام تنها یک قرارداد است، نه یک الزام.
* فضای نام `kube-system`: فضای نام مربوط به آبجکت‌هایی که سیستم کوبرنتیز ایجاد می‌کند.

همچنین می‌توانید خلاصهٔ یک فضای نام مشخص را با دستور زیر دریافت کنید:

```shell
kubectl get namespaces <name>
```

یا اطلاعات تفصیلی آن را با دستور زیر به دست آورید:

```shell
kubectl describe namespaces <name>
```
```console
Name:           default
Labels:         <none>
Annotations:    <none>
Status:         Active

No resource quota.

Resource Limits
 Type       Resource    Min Max Default
 ----               --------    --- --- ---
 Container          cpu         -   -   100m
```

توجه کنید که این جزئیات، هم سهمیهٔ منابع (resource quota) را (در صورت وجود) و هم بازه‌های محدودیت منابع (limit range) را نشان می‌دهند.

سهمیهٔ منابع، مصرف تجمیعی منابع در Namespace را پیگیری می‌کند و به اپراتورهای کلاستر امکان می‌دهد
محدودیت‌های *سخت* مصرف منابع را برای یک Namespace تعریف کنند.

بازهٔ محدودیت، قیدهای حداقل و حداکثر را بر مقدار منابعی تعریف می‌کند که یک موجودیت منفرد می‌تواند در
یک Namespace مصرف کند.

به [کنترل پذیرش: Limit Range](https://git.k8s.io/design-proposals-archive/resource-management/admission_control_limit_range.md) مراجعه کنید.

هر فضای نام می‌تواند در یکی از دو فاز زیر باشد:

* فاز `Active`: فضای نام در حال استفاده است.
* فاز `Terminating`: فضای نام در حال حذف شدن است و نمی‌توان از آن برای آبجکت‌های جدید استفاده کرد.

برای جزئیات بیشتر، به [Namespace](/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)
در مرجع API مراجعه کنید.

## ایجاد یک فضای نام جدید

{{< note >}}
از ایجاد فضای نام با پیشوند `kube-` خودداری کنید، زیرا این پیشوند برای فضاهای نام سیستمی کوبرنتیز رزرو شده است.
{{< /note >}}

یک فایل YAML جدید با نام `my-namespace.yaml` و محتوای زیر ایجاد کنید:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```
سپس دستور زیر را اجرا کنید:

```shell
kubectl create -f ./my-namespace.yaml
```

همچنین می‌توانید فضای نام را با دستور زیر ایجاد کنید:

```shell
kubectl create namespace <insert-namespace-name-here>
``` 

نام فضای نام شما باید یک
[برچسب DNS](/docs/concepts/overview/working-with-objects/names#dns-label-names) معتبر باشد.

فیلد اختیاری `finalizers` وجود دارد که به ناظرها (observables) امکان می‌دهد هنگام حذف فضای نام، منابع را پاک‌سازی کنند.
توجه داشته باشید که اگر یک finalizer ناموجود را مشخص کنید، فضای نام ایجاد می‌شود،
اما هنگامی که کاربر بخواهد آن را حذف کند، در وضعیت `Terminating` گیر می‌کند.

اطلاعات بیشتر دربارهٔ `finalizers` را می‌توانید در
[سند طراحی](https://git.k8s.io/design-proposals-archive/architecture/namespaces.md#finalizers) فضای نام بیابید.

## حذف یک فضای نام

برای حذف یک فضای نام از دستور زیر استفاده کنید:

```shell
kubectl delete namespaces <insert-some-namespace-name>
```

{{< warning >}}
این دستور _همه‌چیز_ را در آن فضای نام حذف می‌کند!
{{< /warning >}}

این عملیات حذف به‌صورت ناهمگام (asynchronous) انجام می‌شود، بنابراین تا مدتی فضای نام را در وضعیت `Terminating` خواهید دید.

## تقسیم کلاستر با استفاده از فضاهای نام کوبرنتیز

به‌طور پیش‌فرض، هر کلاستر کوبرنتیز هنگام راه‌اندازی، یک فضای نام پیش‌فرض ایجاد می‌کند
تا مجموعهٔ پیش‌فرض Podها، Serviceها و Deploymentهای مورد استفادهٔ کلاستر را در خود نگه دارد.

با فرض اینکه یک کلاستر تازه دارید، می‌توانید فضاهای نام موجود را به این صورت بررسی کنید:

```shell
kubectl get namespaces
```
```console
NAME      STATUS    AGE
default   Active    13m
```

### ایجاد فضاهای نام جدید

در این تمرین، دو فضای نام اضافی در کوبرنتیز ایجاد می‌کنید تا محتوای خود را در آن‌ها نگه دارید.

سناریویی را در نظر بگیرید که در آن یک سازمان از یک کلاستر مشترک کوبرنتیز برای موارد کاربرد توسعه و
تولید (production) استفاده می‌کند:

- تیم توسعه می‌خواهد فضایی در کلاستر داشته باشد که در آن بتواند فهرست Podها، Serviceها و
  Deploymentهایی را که برای ساخت و اجرای برنامهٔ خود به کار می‌برد، مشاهده کند.
  در این فضا، منابع کوبرنتیز مدام ایجاد و حذف می‌شوند و محدودیت‌ها دربارهٔ اینکه چه کسی می‌تواند یا نمی‌تواند
  منابع را تغییر دهد، برای امکان‌پذیر کردن توسعهٔ چابک، سهل‌گیرانه‌تر است.

- تیم عملیات می‌خواهد فضایی در کلاستر داشته باشد که در آن بتواند رویه‌های سخت‌گیرانه‌ای را
  دربارهٔ اینکه چه کسی می‌تواند یا نمی‌تواند مجموعهٔ Podها، Serviceها و Deploymentهای اجراکنندهٔ
  سایت تولیدی را دست‌کاری کند، اعمال کند.

یکی از الگوهایی که این سازمان می‌تواند دنبال کند، تقسیم کلاستر کوبرنتیز به دو
فضای نام `development` و `production` است. دو فضای نام جدید برای نگه‌داشتن کارهای خود ایجاد کنید.

فضای نام `development` را با استفاده از kubectl ایجاد کنید:

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-dev.json
```

فضای نام `production` را با استفاده از kubectl ایجاد کنید:

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-prod.json
```

برای اطمینان از درستی کار، همهٔ فضاهای نام موجود در کلاستر را فهرست کنید.

```shell
kubectl get namespaces --show-labels
```

```console
NAME          STATUS    AGE       LABELS
default       Active    32m       <none>
development   Active    29s       name=development
production    Active    23s       name=production
```

### ایجاد Podها در هر فضای نام

هر فضای نام کوبرنتیز، دامنه (scope) را برای Podها، Serviceها و Deploymentهای موجود در کلاستر فراهم می‌کند.
کاربرانی که با یک فضای نام کار می‌کنند، محتوای فضای نام دیگر را نمی‌بینند.
برای نشان دادن این موضوع، یک Deployment و چند Pod در فضای نام `development` ایجاد کنید.

```shell
kubectl create deployment snowflake \
  --image=registry.k8s.io/serve_hostname \
  -n=development --replicas=2
```

شما یک Deployment با اندازهٔ رپلیکای ۲ ایجاد کردید که Podای به نام `snowflake` را
با یک کانتینر ساده که نام میزبان (hostname) را ارائه می‌دهد، اجرا می‌کند.

```shell
kubectl get deployment -n=development
```
```console
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
snowflake    2/2     2            2           2m
```

```shell
kubectl get pods -l app=snowflake -n=development
```
```console
NAME                         READY     STATUS    RESTARTS   AGE
snowflake-3968820950-9dgr8   1/1       Running   0          2m
snowflake-3968820950-vgc4n   1/1       Running   0          2m
```

این نشان می‌دهد که توسعه‌دهندگان می‌توانند هر کاری که می‌خواهند انجام دهند و نگرانی‌ای بابت
تأثیر گذاشتن بر محتوای فضای نام `production` ندارند.

به فضای نام `production` بروید و ببینید که چگونه منابع یک فضای نام از فضای نام دیگر پنهان هستند.
فضای نام `production` باید خالی باشد و دستورهای زیر نباید هیچ خروجی‌ای برگردانند.

```shell
kubectl get deployment -n=production
kubectl get pods -n=production
```

چند Pod در فضای نام `production` ایجاد کنید.

```shell
kubectl create deployment cattle --image=registry.k8s.io/serve_hostname -n=production
kubectl scale deployment cattle --replicas=5 -n=production

kubectl get deployment -n=production
```

```console
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
cattle       5/5     5            5           10s
```

```shell
kubectl get pods -l app=cattle -n=production
```
```console
NAME                      READY     STATUS    RESTARTS   AGE
cattle-2263376956-41xy6   1/1       Running   0          34s
cattle-2263376956-kw466   1/1       Running   0          34s
cattle-2263376956-n4v97   1/1       Running   0          34s
cattle-2263376956-p5p3i   1/1       Running   0          34s
cattle-2263376956-sxpth   1/1       Running   0          34s
```

اکنون باید روشن شده باشد که منابعی که کاربران در یک فضای نام ایجاد می‌کنند، از فضای نام
دیگر پنهان هستند.

با تکامل پشتیبانی از سیاست‌ها در کوبرنتیز، این سناریو گسترش می‌یابد تا نشان دهد چگونه می‌توانید
قواعد مجوزدهی متفاوتی برای هر فضای نام فراهم کنید.

<!-- discussion -->

## درک انگیزهٔ استفاده از فضاهای نام

یک کلاستر واحد باید بتواند نیازهای چندین کاربر یا گروه‌هایی از کاربران را برآورده کند
(که از این پس در این سند _جامعهٔ کاربری_ نامیده می‌شوند).

_فضاهای نام_ کوبرنتیز به پروژه‌ها، تیم‌ها یا مشتریان مختلف کمک می‌کنند تا یک کلاستر کوبرنتیز را به اشتراک بگذارند.

این کار با فراهم کردن موارد زیر انجام می‌شود:

1. یک دامنه برای [نام‌ها](/docs/concepts/overview/working-with-objects/names/).
1. سازوکاری برای اعمال مجوزدهی و سیاست بر بخشی از کلاستر.

استفاده از چندین فضای نام اختیاری است.

هر جامعهٔ کاربری می‌خواهد بتواند جدا از جوامع دیگر کار کند.
هر جامعهٔ کاربری موارد زیر را به‌طور اختصاصی دارد:

1. منابع (Podها، Serviceها، replication controllerها و غیره)
1. سیاست‌ها (چه کسی می‌تواند یا نمی‌تواند در جامعهٔ آن‌ها کارهایی انجام دهد)
1. قیدها (این جامعه مجاز به استفاده از این مقدار سهمیه است و غیره)

اپراتور کلاستر می‌تواند برای هر جامعهٔ کاربری منحصربه‌فرد یک Namespace ایجاد کند.

هر Namespace یک دامنهٔ منحصربه‌فرد برای موارد زیر فراهم می‌کند:

1. منابع نام‌دار (برای جلوگیری از تداخل‌های پایه‌ای نام‌گذاری)
1. واگذاری اختیار مدیریت به کاربران مورد اعتماد
1. امکان محدود کردن مصرف منابع هر جامعه

موارد کاربرد عبارت‌اند از:

1. به‌عنوان اپراتور کلاستر، می‌خواهم از چندین جامعهٔ کاربری روی یک کلاستر واحد پشتیبانی کنم.
1. به‌عنوان اپراتور کلاستر، می‌خواهم اختیار بخش‌هایی از کلاستر را به کاربران مورد اعتماد
   در آن جوامع واگذار کنم.
1. به‌عنوان اپراتور کلاستر، می‌خواهم مقدار منابعی را که هر جامعه می‌تواند مصرف کند محدود کنم
   تا تأثیر آن بر جوامع دیگری که از کلاستر استفاده می‌کنند، محدود شود.
1. به‌عنوان کاربر کلاستر، می‌خواهم با منابع مرتبط با جامعهٔ کاربری خود، جدا از
   کارهایی که جوامع کاربری دیگر روی کلاستر انجام می‌دهند، تعامل داشته باشم.

## درک فضاهای نام و DNS

هنگامی که یک [Service](/docs/concepts/services-networking/service/) ایجاد می‌کنید، یک
[رکورد DNS](/docs/concepts/services-networking/dns-pod-service/) متناظر با آن ایجاد می‌شود.
این رکورد به شکل `<service-name>.<namespace-name>.svc.cluster.local` است؛ یعنی
اگر یک کانتینر از `<service-name>` استفاده کند، این نام به Serviceای که در همان فضای نام قرار دارد
ترجمه (resolve) می‌شود. این ویژگی برای استفاده از پیکربندی یکسان در
چندین فضای نام، مانند Development، Staging و Production، مفید است. اگر بخواهید به
فضاهای نام دیگر دسترسی داشته باشید، باید از نام دامنهٔ کاملاً مشخص (FQDN) استفاده کنید.

## {{% heading "whatsnext" %}}

* دربارهٔ [تنظیم فضای نام ترجیحی](/docs/concepts/overview/working-with-objects/namespaces/#setting-the-namespace-preference) بیشتر بیاموزید.
* دربارهٔ [تنظیم فضای نام برای یک درخواست](/docs/concepts/overview/working-with-objects/namespaces/#setting-the-namespace-for-a-request) بیشتر بیاموزید.
* [طراحی فضاهای نام](https://git.k8s.io/design-proposals-archive/architecture/namespaces.md) را ببینید.
