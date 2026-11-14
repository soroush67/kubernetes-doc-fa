---
title: Job با ارتباط پاد به پاد
content_type: task
min-kubernetes-server-version: v1.21
weight: 30
---

<!-- overview -->

در این مثال، یک Job را در [حالت تکمیل نمایه‌دار (Indexed completion mode)](/blog/2021/04/19/introducing-indexed-jobs/)
اجرا می‌کنید و آن را طوری پیکربندی می‌کنید که پادهای ایجادشده توسط Job بتوانند به‌جای نشانی‌های IP پادها، با استفاده از
نام میزبان (hostname) پادها با یکدیگر ارتباط برقرار کنند.

ممکن است پادهای درون یک Job نیاز داشته باشند با یکدیگر ارتباط برقرار کنند. بار کاری کاربر که در هر پاد اجرا می‌شود
می‌تواند از سرور API کوبرنتیز پرس‌وجو کند تا IP پادهای دیگر را به دست آورد، اما تکیه بر سازوکار داخلی
تفکیک نام DNS در کوبرنتیز بسیار ساده‌تر است.

در Jobهایی که در حالت تکمیل نمایه‌دار اجرا می‌شوند، نام میزبان پادها به‌طور خودکار در قالب
`${jobName}-${completionIndex}` تنظیم می‌شود. با استفاده از این قالب می‌توانید نام میزبان پادها را به‌صورت قطعی
بسازید و ارتباط میان پادها را برقرار کنید، *بدون* آنکه لازم باشد برای به دست آوردن نام میزبان یا IP پادها از طریق
درخواست‌های API، یک اتصال کلاینت به control plane کوبرنتیز ایجاد کنید.

این پیکربندی در مواردی سودمند است که به شبکه‌بندی پادها نیاز دارید، اما نمی‌خواهید به اتصال شبکه با
سرور API کوبرنتیز وابسته باشید.

## {{% heading "prerequisites" %}}

باید از پیش با کاربرد پایه‌ای [Job](/docs/concepts/workloads/controllers/job/) آشنا باشید.

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

{{< note >}}
اگر از minikube یا ابزاری مشابه استفاده می‌کنید، ممکن است برای اطمینان از در دسترس بودن DNS لازم باشد
[گام‌های بیشتری](https://minikube.sigs.k8s.io/docs/handbook/addons/ingress-dns/) بردارید.
{{< /note >}}

<!-- steps -->

## راه‌اندازی یک Job با ارتباط پاد به پاد

برای فعال‌سازی ارتباط پاد به پاد با استفاده از نام میزبان پادها در یک Job، باید کارهای زیر را انجام دهید:

1. یک [Service بدون سر (headless Service)](/docs/concepts/services-networking/service/#headless-services)
   با یک انتخابگر (selector) برچسب معتبر برای پادهایی که Job شما ایجاد می‌کند راه‌اندازی کنید. این Service بدون سر
   باید در همان فضای نام (namespace) Job قرار داشته باشد. یک راه ساده برای این کار، استفاده از انتخابگر
   `job-name: <your-job-name>` است، زیرا کوبرنتیز برچسب `job-name` را به‌طور خودکار اضافه می‌کند.
   این پیکربندی باعث می‌شود سیستم DNS رکوردهایی برای نام میزبان پادهایی که Job شما را اجرا می‌کنند ایجاد کند.

1. با افزودن مقدار زیر به مشخصات قالب (template spec) Job، Service بدون سر را به‌عنوان سرویس زیردامنه
   برای پادهای Job پیکربندی کنید:

   ```yaml
   subdomain: <headless-svc-name>
   ```

### مثال

در ادامه، یک مثال کارا از Jobی آمده است که ارتباط پاد به پاد از طریق نام میزبان پادها در آن فعال شده است.
این Job تنها زمانی تکمیل می‌شود که همهٔ پادها با استفاده از نام میزبان، با موفقیت یکدیگر را ping کنند.

{{< note >}}
در اسکریپت Bash که در مثال زیر روی هر پاد اجرا می‌شود، اگر لازم باشد پاد از بیرون فضای نام در دسترس باشد،
می‌توان فضای نام را نیز به‌عنوان پیشوند به نام میزبان پادها افزود.
{{< /note >}}

```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-svc
spec:
  clusterIP: None # clusterIP must be None to create a headless service
  selector:
    job-name: example-job # must match Job name
---
apiVersion: batch/v1
kind: Job
metadata:
  name: example-job
spec:
  completions: 3
  parallelism: 3
  completionMode: Indexed
  template:
    spec:
      subdomain: headless-svc # has to match Service name
      restartPolicy: Never
      containers:
      - name: example-workload
        image: bash:latest
        command:
        - bash
        - -c
        - |
          for i in 0 1 2
          do
            gotStatus="-1"
            wantStatus="0"             
            while [ $gotStatus -ne $wantStatus ]
            do                                       
              ping -c 1 example-job-${i}.headless-svc > /dev/null 2>&1
              gotStatus=$?                
              if [ $gotStatus -ne $wantStatus ]; then
                echo "Failed to ping pod example-job-${i}.headless-svc, retrying in 1 second..."
                sleep 1
              fi
            done                                                         
            echo "Successfully pinged pod: example-job-${i}.headless-svc"
          done
```

پس از اعمال مثال بالا، پادها با استفاده از قالب `<pod-hostname>.<headless-service-name>` از طریق شبکه
به یکدیگر دسترسی پیدا می‌کنند. باید خروجی‌ای مشابه زیر ببینید:

```shell
kubectl logs example-job-0-qws42
```

```
Failed to ping pod example-job-0.headless-svc, retrying in 1 second...
Successfully pinged pod: example-job-0.headless-svc
Successfully pinged pod: example-job-1.headless-svc
Successfully pinged pod: example-job-2.headless-svc
```

{{< note >}}
توجه داشته باشید که قالب نام `<pod-hostname>.<headless-service-name>` که در این مثال استفاده شده است،
در صورتی که سیاست DNS روی `None` یا `Default` تنظیم شده باشد کار نمی‌کند.
به [سیاست DNS پاد](/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) مراجعه کنید.
{{< /note >}}
