---
title: تعریف متغیرهای محیطی وابسته
content_type: task
weight: 20
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان برای یک کانتینر در یک Pod کوبرنتیز، متغیرهای محیطی وابسته تعریف کرد.


## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}


<!-- steps -->

## تعریف یک متغیر محیطی وابسته برای یک کانتینر

هنگام ایجاد یک Pod می‌توانید برای کانتینرهایی که در آن Pod اجرا می‌شوند، متغیرهای محیطی وابسته تعیین کنید. برای تعیین متغیرهای محیطی وابسته، می‌توانید در فایل پیکربندی از عبارت $(VAR_NAME) در مقدار `value` بخش `env` استفاده کنید.

در این تمرین، یک Pod ایجاد می‌کنید که یک کانتینر را اجرا می‌کند. فایل پیکربندی این Pod یک متغیر محیطی وابسته را با کاربردهای رایج آن تعریف می‌کند. مانیفست پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/inject/dependent-envars.yaml" %}}

1. یک Pod بر اساس این مانیفست ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/dependent-envars.yaml
   ```
   ```
   pod/dependent-envars-demo created
   ```

2. فهرست Podهای در حال اجرا را نمایش دهید:

   ```shell
   kubectl get pods dependent-envars-demo
   ```
   ```
   NAME                      READY     STATUS    RESTARTS   AGE
   dependent-envars-demo     1/1       Running   0          9s
   ```

3. لاگ‌های کانتینری را که در Pod شما اجرا می‌شود بررسی کنید:

   ```shell
   kubectl logs pod/dependent-envars-demo
   ```
   ```

   UNCHANGED_REFERENCE=$(PROTOCOL)://172.17.0.1:80
   SERVICE_ADDRESS=https://172.17.0.1:80
   ESCAPED_REFERENCE=$(PROTOCOL)://172.17.0.1:80
   ```

همان‌طور که در خروجی بالا می‌بینید، برای `SERVICE_ADDRESS` یک ارجاع وابستگی صحیح، برای `UNCHANGED_REFERENCE` یک ارجاع وابستگی نادرست و برای `ESCAPED_REFERENCE` ارجاعی که از جایگذاری وابستگی صرف‌نظر می‌کند تعریف کرده‌اید.

اگر متغیر محیطی در زمان ارجاع از قبل تعریف شده باشد، ارجاع به‌درستی تحلیل (resolve) می‌شود؛ مانند حالت `SERVICE_ADDRESS`.

توجه کنید که ترتیب در فهرست `env` اهمیت دارد. اگر متغیر محیطی در پایین‌تر از فهرست مشخص شده باشد، «تعریف‌شده» به حساب نمی‌آید. به همین دلیل است که در مثال بالا، `UNCHANGED_REFERENCE` نمی‌تواند `$(PROTOCOL)` را تحلیل کند.

اگر متغیر محیطی تعریف نشده باشد یا تنها برخی از متغیرها تعریف شده باشند، متغیر محیطی تعریف‌نشده مانند یک رشتهٔ معمولی در نظر گرفته می‌شود؛ مانند `UNCHANGED_REFERENCE`. توجه داشته باشید که متغیرهای محیطی‌ای که به‌نادرستی تجزیه شوند، معمولاً مانع از شروع به کار کانتینر نمی‌شوند.

می‌توان نحو `$(VAR_NAME)` را با یک `$` دوگانه گریز (escape) داد؛ یعنی: `$$(VAR_NAME)`. ارجاع‌های گریزداده‌شده هرگز بسط داده نمی‌شوند، صرف‌نظر از اینکه متغیر مورد ارجاع تعریف شده باشد یا نه. این موضوع را می‌توان در حالت `ESCAPED_REFERENCE` در بالا مشاهده کرد.

## {{% heading "whatsnext" %}}


* دربارهٔ [متغیرهای محیطی](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/) بیشتر بیاموزید.
* [EnvVarSource](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#envvarsource-v1-core) را ببینید.
