---
title: تعریف متغیرهای محیطی برای یک کانتینر
content_type: task
weight: 20
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان برای یک کانتینر در یک Pod کوبرنتیز
متغیرهای محیطی (environment variables) تعریف کرد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## تعریف یک متغیر محیطی برای یک کانتینر

هنگام ایجاد یک Pod، می‌توانید برای کانتینرهایی که در آن Pod اجرا می‌شوند
متغیرهای محیطی تعیین کنید. برای این کار، فیلد `env` یا `envFrom` را در
فایل پیکربندی قرار دهید.

فیلدهای `env` و `envFrom` اثرهای متفاوتی دارند.

`env`
: با این فیلد می‌توانید متغیرهای محیطی یک کانتینر را تعیین کنید و برای هر متغیری که نام می‌برید، مقداری را مستقیماً مشخص کنید.

`envFrom`
: با این فیلد می‌توانید متغیرهای محیطی یک کانتینر را با ارجاع به یک ConfigMap یا یک Secret تعیین کنید.
 هنگامی که از `envFrom` استفاده می‌کنید، همهٔ جفت‌های کلید-مقدار موجود در ConfigMap یا Secret ارجاع‌شده
 به‌عنوان متغیرهای محیطی کانتینر تنظیم می‌شوند.
 همچنین می‌توانید یک رشتهٔ پیشوند مشترک نیز مشخص کنید.

برای اطلاعات بیشتر می‌توانید دربارهٔ [ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables)
و [Secret](/docs/tasks/inject-data-application/distribute-credentials-secure/#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables) مطالعه کنید.

این صفحه نحوهٔ استفاده از `env` را توضیح می‌دهد.

در این تمرین، یک Pod ایجاد می‌کنید که یک کانتینر را اجرا می‌کند. فایل
پیکربندی این Pod یک متغیر محیطی با نام `DEMO_GREETING` و مقدار
`"Hello from the environment"` تعریف می‌کند. مانیفست پیکربندی این Pod
به این شکل است:

{{% code_sample file="pods/inject/envars.yaml" %}}

1. یک Pod بر اساس این مانیفست ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/envars.yaml
   ```

1. فهرست Podهای در حال اجرا را نمایش دهید:

   ```shell
   kubectl get pods -l purpose=demonstrate-envars
   ```

   خروجی مشابه زیر است:

   ```
   NAME            READY     STATUS    RESTARTS   AGE
   envar-demo      1/1       Running   0          9s
   ```

1. فهرست متغیرهای محیطی کانتینر این Pod را نمایش دهید:

   ```shell
   kubectl exec envar-demo -- printenv
   ```

   خروجی مشابه زیر است:

   ```
   NODE_VERSION=4.4.2
   EXAMPLE_SERVICE_PORT_8080_TCP_ADDR=10.3.245.237
   HOSTNAME=envar-demo
   ...
   DEMO_GREETING=Hello from the environment
   DEMO_FAREWELL=Such a sweet sorrow
   ```

{{< note >}}
متغیرهای محیطی‌ای که با فیلد `env` یا `envFrom` تنظیم می‌شوند، هر متغیر
محیطی مشخص‌شده در ایمیج کانتینر را بازنویسی می‌کنند.
{{< /note >}}

{{< note >}}
متغیرهای محیطی می‌توانند به یکدیگر ارجاع دهند، اما ترتیب آن‌ها اهمیت دارد.
متغیرهایی که از متغیرهای دیگرِ تعریف‌شده در همان زمینه استفاده می‌کنند، باید
در ادامهٔ فهرست بیایند. همچنین از ارجاع‌های چرخشی پرهیز کنید.
{{< /note >}}

## استفاده از متغیرهای محیطی در پیکربندی

متغیرهای محیطی‌ای را که در پیکربندی یک Pod زیر
`.spec.containers[*].env[*]` تعریف می‌کنید، می‌توان در بخش‌های دیگر پیکربندی
نیز به کار برد؛ برای مثال در فرمان‌ها و آرگومان‌هایی که برای کانتینرهای Pod
تعیین می‌کنید. در پیکربندی نمونهٔ زیر، متغیرهای محیطی `GREETING`،
`HONORIFIC` و `NAME` به‌ترتیب با مقدارهای `Warm greetings to`، `The Most
Honorable` و `Kubernetes` تنظیم شده‌اند. متغیر محیطی `MESSAGE` همهٔ این
متغیرهای محیطی را با هم ترکیب می‌کند و سپس حاصل را به‌عنوان یک آرگومان خط
فرمان (CLI) به کانتینر `env-print-demo` می‌دهد.

نام متغیرهای محیطی می‌تواند از هر یک از [نویسه‌های ASCII قابل چاپ](https://www.ascii-code.com/characters/printable-characters) به‌جز '=' تشکیل شود.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: print-greeting
spec:
  containers:
  - name: env-print-demo
    image: bash
    env:
    - name: GREETING
      value: "Warm greetings to"
    - name: HONORIFIC
      value: "The Most Honorable"
    - name: NAME
      value: "Kubernetes"
    - name: MESSAGE
      value: "$(GREETING) $(HONORIFIC) $(NAME)"
    command: ["echo"]
    args: ["$(MESSAGE)"]
```

پس از ایجاد Pod، فرمان `echo Warm greetings to The Most Honorable Kubernetes` در کانتینر اجرا می‌شود.

## {{% heading "whatsnext" %}}

* دربارهٔ [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/) بیشتر بیاموزید.
* دربارهٔ [استفاده از Secretها به‌عنوان متغیرهای محیطی](/docs/concepts/configuration/secret/#using-secrets-as-environment-variables) بیاموزید.
* مستندات [EnvVarSource](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#envvarsource-v1-core) را ببینید.
