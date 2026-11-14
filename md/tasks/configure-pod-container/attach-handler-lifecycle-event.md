---
title: اتصال هندلرها به رویدادهای چرخه حیات کانتینر
weight: 180
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توان هندلرها (handlers) را به رویدادهای چرخه حیات کانتینر متصل کرد. کوبرنتیز از رویدادهای postStart و preStop پشتیبانی می‌کند. کوبرنتیز رویداد postStart را بلافاصله پس از شروع به کار یک کانتینر و رویداد preStop را بلافاصله پیش از خاتمه یافتن کانتینر ارسال می‌کند. هر کانتینر می‌تواند برای هر رویداد یک هندلر تعیین کند.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}




<!-- steps -->

## تعریف هندلرهای postStart و preStop

در این تمرین، یک Pod می‌سازید که یک کانتینر دارد. این کانتینر برای رویدادهای postStart و preStop هندلر دارد.

فایل پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="pods/lifecycle-events.yaml" %}}

در فایل پیکربندی می‌بینید که فرمان postStart یک فایل `message` در دایرکتوری `/usr/share` کانتینر می‌نویسد. فرمان preStop نیز nginx را به‌شکلی آرام و کنترل‌شده (graceful) خاموش می‌کند. این کار در مواردی مفید است که کانتینر به دلیل بروز خطا در حال خاتمه یافتن باشد.

Pod را ایجاد کنید:

    kubectl apply -f https://k8s.io/examples/pods/lifecycle-events.yaml

بررسی کنید که کانتینرِ درون Pod در حال اجرا باشد:

    kubectl get pod lifecycle-demo

یک شل (shell) در کانتینری که در Pod شما اجرا می‌شود باز کنید:

    kubectl exec -it lifecycle-demo -- /bin/bash

در شل، بررسی کنید که هندلر `postStart` فایل `message` را ایجاد کرده باشد:

    root@lifecycle-demo:/# cat /usr/share/message

خروجی، متنی را نشان می‌دهد که هندلر postStart نوشته است:

    Hello from the postStart handler





<!-- discussion -->

## بحث

کوبرنتیز رویداد postStart را بلافاصله پس از ایجاد کانتینر ارسال می‌کند. با این حال، هیچ تضمینی وجود ندارد که هندلر postStart پیش از نقطه ورود (entrypoint) کانتینر فراخوانی شود. هندلر postStart نسبت به کد کانتینر به‌صورت ناهمگام اجرا می‌شود، اما مدیریت کانتینر از سوی کوبرنتیز تا پایان کار این هندلر متوقف می‌ماند. وضعیت کانتینر نیز تا زمانی که هندلر postStart به پایان نرسد، به RUNNING تغییر نمی‌کند.

کوبرنتیز رویداد preStop را بلافاصله پیش از خاتمه یافتن کانتینر ارسال می‌کند. مدیریت کانتینر از سوی کوبرنتیز تا پایان کار هندلر preStop متوقف می‌ماند، مگر آنکه مهلت خاتمه (grace period) Pod به پایان برسد. برای جزئیات بیشتر، به [چرخه حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/) مراجعه کنید.

{{< note >}}
کوبرنتیز رویداد preStop را فقط زمانی ارسال می‌کند که یک Pod یا کانتینری درون Pod *خاتمه داده شود*. بنابراین، هنگامی که Pod *به‌طور کامل اجرا شده و پایان یافته باشد* (completed)، قلاب (hook) preStop فراخوانی نمی‌شود. برای جزئیات این محدودیت، به [قلاب‌های کانتینر](/docs/concepts/containers/container-lifecycle-hooks/#container-hooks) مراجعه کنید.
{{< /note >}}




## {{% heading "whatsnext" %}}


* درباره [قلاب‌های چرخه حیات کانتینر](/docs/concepts/containers/container-lifecycle-hooks/) بیشتر بیاموزید.
* درباره [چرخه حیات یک Pod](/docs/concepts/workloads/pods/pod-lifecycle/) بیشتر بیاموزید.


### مرجع

* [Lifecycle](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#lifecycle-v1-core)
* [Container](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#container-v1-core)
* فیلد `terminationGracePeriodSeconds` را در [PodSpec](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podspec-v1-core) ببینید.
