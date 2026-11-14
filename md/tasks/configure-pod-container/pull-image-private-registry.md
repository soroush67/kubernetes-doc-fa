---
title: دریافت ایمیج از یک رجیستری خصوصی
weight: 130
---

<!-- overview -->

این صفحه نشان می‌دهد چگونه یک Pod ایجاد کنید که برای دریافت (pull) ایمیج از یک رجیستری یا مخزن خصوصی ایمیج کانتینر، از یک
{{< glossary_tooltip text="Secret" term_id="secret" >}} استفاده می‌کند. رجیستری‌های خصوصی بسیاری مورد استفاده هستند. در این تمرین، [Docker Hub](https://www.docker.com/products/docker-hub)
به‌عنوان رجیستری نمونه به کار رفته است.

{{% thirdparty-content single="true" %}}

## {{% heading "prerequisites" %}}

* {{< include "task-tutorial-prereqs.md" >}}

* برای انجام این تمرین، به ابزار خط فرمان `docker` و یک
  [شناسه Docker](https://docs.docker.com/docker-id/) نیاز دارید که گذرواژه آن را بدانید.
* اگر از رجیستری کانتینر خصوصی دیگری استفاده می‌کنید، به ابزار خط فرمان آن رجیستری و اطلاعات ورود به آن نیاز دارید.

<!-- steps -->

## ورود به Docker Hub

برای دریافت یک ایمیج خصوصی، باید روی لپ‌تاپ خود نزد رجیستری احراز هویت کنید.

با ابزار `docker` وارد Docker Hub شوید. برای اطلاعات بیشتر، بخش _ورود_ در صفحه
[حساب‌های Docker ID](https://docs.docker.com/docker-id/#log-in) را ببینید.

```shell
docker login
```

هنگامی که از شما خواسته شد، شناسه Docker خود و سپس اعتبارنامه‌ای را که می‌خواهید استفاده کنید (توکن دسترسی یا گذرواژه شناسه Docker) وارد کنید.

فرایند ورود، فایل `config.json` را که یک توکن مجوز در خود نگه می‌دارد ایجاد یا به‌روزرسانی می‌کند.
[نحوه تفسیر این فایل در کوبرنتیز](/docs/concepts/containers/images#config-json) را مرور کنید.

فایل `config.json` را مشاهده کنید:

```shell
cat ~/.docker/config.json
```

خروجی شامل بخشی مشابه زیر است:

```json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "c3R...zE2"
        }
    }
}
```

{{< note >}}
اگر از یک انباره اعتبارنامه Docker (credentials store) استفاده کنید، مدخل `auth` را نخواهید دید؛ به‌جای آن مدخل `credsStore` را می‌بینید که مقدارش نام آن انباره است.
در این حالت، می‌توانید مستقیماً یک Secret ایجاد کنید.
بخش [ایجاد Secret با ارائه اعتبارنامه‌ها در خط فرمان](#create-a-secret-by-providing-credentials-on-the-command-line) را ببینید.
{{< /note >}}

## ایجاد Secret بر پایه اعتبارنامه‌های موجود {#registry-secret-existing-credentials}

هر کلاستر کوبرنتیز برای احراز هویت نزد رجیستری کانتینر و دریافت ایمیج خصوصی، از Secret از نوع `kubernetes.io/dockerconfigjson` استفاده می‌کند.

اگر پیش‌تر دستور `docker login` را اجرا کرده‌اید، می‌توانید آن اعتبارنامه را در کوبرنتیز کپی کنید:

```shell
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
```

اگر به کنترل بیشتری نیاز دارید (برای مثال، برای تعیین فضای نام (namespace) یا برچسب برای Secret جدید)، می‌توانید Secret را پیش از ذخیره‌سازی سفارشی کنید.
حتماً موارد زیر را رعایت کنید:

- نام آیتم داده را `.dockerconfigjson` قرار دهید.
- فایل پیکربندی Docker را با base64 کدگذاری کنید و سپس آن رشته را بدون شکستگی، به‌عنوان مقدار فیلد `data[".dockerconfigjson"]` قرار دهید.
- مقدار `type` را `kubernetes.io/dockerconfigjson` تعیین کنید.

نمونه:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: myregistrykey
  namespace: awesomeapps
data:
  .dockerconfigjson: UmVhbGx5IHJlYWxseSByZWVlZWVlZWVlZWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGx5eXl5eXl5eXl5eXl5eXl5eXl5eSBsbGxsbGxsbGxsbGxsbG9vb29vb29vb29vb29vb29vb29vb29vb29vb25ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cgYXV0aCBrZXlzCg==
type: kubernetes.io/dockerconfigjson
```

اگر پیام خطای `error: no objects passed to create` را دریافت کردید، ممکن است رشته کدگذاری‌شده با base64 نامعتبر باشد.
اگر پیام خطایی مانند `Secret "myregistrykey" is invalid: data[.dockerconfigjson]: invalid value ...` دریافت کردید، یعنی رشته کدگذاری‌شده با base64 در داده‌ها با موفقیت رمزگشایی شده، اما نتوانسته است به‌عنوان فایل `.docker/config.json` تجزیه شود.

## ایجاد Secret با ارائه اعتبارنامه‌ها در خط فرمان

این Secret را با نام `regcred` ایجاد کنید:

```shell
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```

که در آن:

* مقدار `<your-registry-server>` نام دامنه کامل (FQDN) رجیستری خصوصی Docker شماست.
  برای DockerHub از `https://index.docker.io/v1/` استفاده کنید.
* مقدار `<your-name>` نام کاربری Docker شماست.
* مقدار `<your-pword>` گذرواژه Docker شماست.
* مقدار `<your-email>` ایمیل Docker شماست.

اعتبارنامه‌های Docker خود را با موفقیت به‌صورت یک Secret با نام `regcred` در کلاستر تنظیم کردید.

{{< note >}}
تایپ کردن اطلاعات محرمانه در خط فرمان ممکن است باعث شود این اطلاعات بدون محافظت در تاریخچه پوسته (shell) شما ذخیره شوند. همچنین ممکن است این اطلاعات در مدتی که `kubectl` در حال اجراست، برای کاربران دیگر رایانه شما قابل مشاهده باشند.
{{< /note >}}


## بررسی Secret با نام `regcred`

برای درک محتوای Secret با نام `regcred` که ایجاد کرده‌اید، ابتدا آن را در قالب YAML مشاهده کنید:

```shell
kubectl get secret regcred --output=yaml
```

خروجی مشابه زیر است:

```yaml
apiVersion: v1
kind: Secret
metadata:
  ...
  name: regcred
  ...
data:
  .dockerconfigjson: eyJodHRwczovL2luZGV4L ... J0QUl6RTIifX0=
type: kubernetes.io/dockerconfigjson
```

مقدار فیلد `.dockerconfigjson` نمایش base64 اعتبارنامه‌های Docker شماست.

برای اینکه ببینید فیلد `.dockerconfigjson` چه چیزی در خود دارد، داده‌های Secret را به قالبی خوانا تبدیل کنید:

```shell
kubectl get secret regcred --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode
```

خروجی مشابه زیر است:

```json
{"auths":{"your.private.registry.example.com":{"username":"janedoe","password":"xxxxxxxxxxx","email":"jdoe@example.com","auth":"c3R...zE2"}}}
```

برای اینکه ببینید فیلد `auth` چه چیزی در خود دارد، داده‌های کدگذاری‌شده با base64 را به قالبی خوانا تبدیل کنید:

```shell
echo "c3R...zE2" | base64 --decode
```

خروجی، که از به‌هم‌پیوستن نام کاربری و گذرواژه با یک `:` تشکیل شده، مشابه زیر است:

```none
janedoe:xxxxxxxxxxx
```

توجه کنید که داده‌های Secret، توکن مجوزی مشابه فایل محلی `~/.docker/config.json` شما را در بر دارد.

اعتبارنامه‌های Docker خود را با موفقیت به‌صورت یک Secret با نام `regcred` در کلاستر تنظیم کردید.

## ایجاد Pod که از Secret شما استفاده می‌کند

در ادامه، مانیفست یک Pod نمونه آمده است که به اعتبارنامه‌های Docker شما در `regcred` نیاز دارد:

{{% code_sample file="pods/private-reg-pod.yaml" %}}

فایل بالا را روی رایانه خود دانلود کنید:

```shell
curl -L -o my-private-reg-pod.yaml https://k8s.io/examples/pods/private-reg-pod.yaml
```

در فایل `my-private-reg-pod.yaml`، عبارت `<your-private-image>` را با مسیر یک ایمیج در رجیستری خصوصی جایگزین کنید؛ برای مثال:

```none
your.private.registry.example.com/janedoe/jdoe-private:v1
```

کوبرنتیز برای دریافت ایمیج از رجیستری خصوصی به اعتبارنامه نیاز دارد.
فیلد `imagePullSecrets` در فایل پیکربندی مشخص می‌کند که کوبرنتیز باید اعتبارنامه‌ها را از Secret با نام `regcred` بگیرد.

یک Pod ایجاد کنید که از Secret شما استفاده کند و بررسی کنید که Pod در حال اجرا باشد:

```shell
kubectl apply -f my-private-reg-pod.yaml
kubectl get pod private-reg
```

{{< note >}}
برای استفاده از Secretهای دریافت ایمیج در یک Pod (یا یک Deployment یا هر آبجکت دیگری که الگوی Pod دارد و از آن استفاده می‌کنید)، باید مطمئن شوید که Secret مناسب در فضای نام درست وجود دارد. فضای نام مورد نظر همان فضای نامی است که Pod را در آن تعریف کرده‌اید.
{{< /note >}}

همچنین اگر Pod با وضعیت `ImagePullBackOff` راه‌اندازی نشد، رویدادهای Pod را مشاهده کنید:

```shell
kubectl describe pod private-reg
```

اگر سپس رویدادی دیدید که دلیل (reason) آن `FailedToRetrieveImagePullSecret` است، یعنی کوبرنتیز نمی‌تواند Secret با نام مشخص‌شده (در این مثال، `regcred`) را پیدا کند.

مطمئن شوید Secret که مشخص کرده‌اید وجود دارد و نام آن را درست نوشته‌اید.
```shell
Events:
  ...  Reason                           ...  Message
       ------                                -------
  ...  FailedToRetrieveImagePullSecret  ...  Unable to retrieve some image pull secrets (<regcred>); attempting to pull the image may not succeed.
```

## استفاده از ایمیج‌های چند رجیستری

هر Pod می‌تواند چند کانتینر داشته باشد و ایمیج هر کانتینر می‌تواند از رجیستری متفاوتی باشد.
می‌توانید در یک Pod از چند `imagePullSecrets` استفاده کنید و هر کدام می‌تواند چند اعتبارنامه را در بر داشته باشد.

دریافت ایمیج با هر یک از اعتبارنامه‌هایی که با رجیستری مطابقت دارند امتحان می‌شود.
اگر هیچ اعتبارنامه‌ای با رجیستری مطابقت نداشته باشد، دریافت ایمیج بدون مجوز یا با پیکربندی سفارشی مخصوص محیط اجرا امتحان می‌شود.

## {{% heading "whatsnext" %}}

* درباره [Secretها](/docs/concepts/configuration/secret/) بیشتر بیاموزید.
  * یا مرجع API مربوط به {{< api-reference page="core/secret-v1" >}} را بخوانید.
* درباره [استفاده از رجیستری خصوصی](/docs/concepts/containers/images/#using-a-private-registry) بیشتر بیاموزید.
* درباره [افزودن Secretهای دریافت ایمیج به یک حساب سرویس](/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account) بیشتر بیاموزید.
* صفحه [kubectl create secret docker-registry](/docs/reference/generated/kubectl/kubectl-commands/#-em-secret-docker-registry-em-) را ببینید.
* فیلد `imagePullSecrets` را در [تعریف کانتینرهای](/docs/reference/kubernetes-api/workload-resources/pod-v1/#containers) یک Pod ببینید.
