---
title: تعیین علت شکست Pod
content_type: task
weight: 30
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه پیام خاتمهٔ یک کانتینر را بنویسید و بخوانید.

پیام‌های خاتمه (termination messages) راهی در اختیار کانتینرها می‌گذارند تا اطلاعات مربوط به رویدادهای مهلک را در محلی بنویسند که ابزارهایی مانند داشبوردها و نرم‌افزارهای پایش بتوانند به‌آسانی آن را بازیابی و نمایش دهند. در بیشتر موارد، اطلاعاتی را که در پیام خاتمه قرار می‌دهید باید در [لاگ‌های کوبرنتیز](/docs/concepts/cluster-administration/logging/) عمومی نیز بنویسید.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

<!-- steps -->

## نوشتن و خواندن پیام خاتمه

در این تمرین، یک Pod می‌سازید که یک کانتینر را اجرا می‌کند. مانیفست این Pod فرمانی را مشخص می‌کند که هنگام شروع کانتینر اجرا می‌شود:

{{% code_sample file="debug/termination.yaml" %}}

1. یک Pod بر اساس فایل پیکربندی YAML بسازید:

    ```shell
    kubectl apply -f https://k8s.io/examples/debug/termination.yaml
    ```
    
    در فیلدهای `command` و `args` فایل YAML می‌بینید که کانتینر به مدت ۱۰ ثانیه به خواب می‌رود و سپس عبارت "Sleep expired" را در فایل `/dev/termination-log` می‌نویسد. کانتینر پس از نوشتن پیام "Sleep expired" خاتمه می‌یابد.

1. اطلاعات Pod را نمایش دهید:

    ```shell
    kubectl get pod termination-demo
    ```

    فرمان بالا را تا زمانی که Pod دیگر در حال اجرا نباشد تکرار کنید.

1. اطلاعات مفصل Pod را نمایش دهید:

    ```shell
    kubectl get pod termination-demo --output=yaml
    ```

    خروجی شامل پیام "Sleep expired" است:

    ```yaml
    apiVersion: v1
    kind: Pod
    ...
        lastState:
          terminated:
            containerID: ...
            exitCode: 0
            finishedAt: ...
            message: |
              Sleep expired
            ...
    ```

1. با استفاده از یک قالب Go، خروجی را طوری فیلتر کنید که فقط پیام خاتمه را در بر بگیرد:

    ```shell
    kubectl get pod termination-demo -o go-template="{{range .status.containerStatuses}}{{.lastState.terminated.message}}{{end}}"
    ```

اگر یک Pod چندکانتینری را اجرا می‌کنید، می‌توانید با یک قالب Go نام کانتینر را نیز در خروجی بگنجانید. به این ترتیب می‌توانید دریابید کدام‌یک از کانتینرها با شکست مواجه شده است:

```shell
kubectl get pod multi-container-pod -o go-template='{{range .status.containerStatuses}}{{printf "%s:\n%s\n\n" .name .lastState.terminated.message}}{{end}}'
```

## سفارشی‌سازی پیام خاتمه

کوبرنتیز پیام‌های خاتمه را از فایل پیام خاتمه‌ای بازیابی می‌کند که در فیلد `terminationMessagePath` کانتینر مشخص شده است. مقدار پیش‌فرض این فیلد `/dev/termination-log` است. با سفارشی‌سازی این فیلد می‌توانید به کوبرنتیز بگویید از فایل دیگری استفاده کند. کوبرنتیز از محتوای فایل مشخص‌شده برای پر کردن پیام وضعیت کانتینر، چه در صورت موفقیت و چه در صورت شکست، استفاده می‌کند.

پیام خاتمه قرار است وضعیت نهایی کوتاهی باشد، مانند پیام شکست یک assertion. ‏kubelet پیام‌هایی را که طولشان بیش از ۴۰۹۶ بایت باشد کوتاه می‌کند.

مجموع طول پیام‌ها در همهٔ کانتینرها به ۱۲ کیبی‌بایت محدود است و این مقدار به‌طور مساوی میان کانتینرها تقسیم می‌شود. برای مثال، اگر ۱۲ کانتینر (`initContainers` یا `containers`) وجود داشته باشد، هر کدام ۱۰۲۴ بایت فضا برای پیام خاتمه در اختیار دارند.

مسیر پیش‌فرض پیام خاتمه `/dev/termination-log` است. پس از راه‌اندازی یک Pod نمی‌توانید مسیر پیام خاتمه را تنظیم کنید.

در مثال زیر، کانتینر پیام‌های خاتمه را در `/tmp/my-log` می‌نویسد تا کوبرنتیز آن‌ها را بازیابی کند:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: msg-path-demo
spec:
  containers:
  - name: msg-path-demo-container
    image: debian
    terminationMessagePath: "/tmp/my-log"
```

افزون بر این، کاربران می‌توانند برای سفارشی‌سازی بیشتر، فیلد `terminationMessagePolicy` کانتینر را تنظیم کنند. مقدار پیش‌فرض این فیلد "`File`" است؛ یعنی پیام‌های خاتمه فقط از فایل پیام خاتمه بازیابی می‌شوند. با تنظیم `terminationMessagePolicy` روی "`FallbackToLogsOnError`" می‌توانید به کوبرنتیز بگویید که اگر فایل پیام خاتمه خالی بود و کانتینر با خطا خارج شد، از آخرین بخش خروجی لاگ کانتینر استفاده کند. خروجی لاگ به ۲۰۴۸ بایت یا ۸۰ خط، هر کدام که کمتر باشد، محدود است.

## {{% heading "whatsnext" %}}

* فیلد `terminationMessagePath` را در
  [Container](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#container-v1-core) ببینید.
* بخش [ImagePullBackOff](/docs/concepts/containers/images/#imagepullbackoff) را در صفحهٔ [ایمیج‌ها](/docs/concepts/containers/images/) ببینید.
* دربارهٔ [بازیابی لاگ‌ها](/docs/concepts/cluster-administration/logging/) بیاموزید.
* دربارهٔ [قالب‌های Go](https://pkg.go.dev/text/template) بیاموزید.
* دربارهٔ [وضعیت Pod](/docs/tasks/debug/debug-application/debug-init-containers/#understanding-pod-status) و [فاز Pod](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) بیاموزید.
* دربارهٔ [وضعیت‌های کانتینر](/docs/concepts/workloads/pods/pod-lifecycle/#container-states) بیاموزید.
