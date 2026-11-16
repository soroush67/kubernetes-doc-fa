---
title: انجام به‌روزرسانی تدریجی
weight: 10
---

## {{% heading "objectives" %}}

یک به‌روزرسانی تدریجی را با kubectl انجام دهید.

## {{% heading "prerequisites" %}}

دستورهای پوسته در این آموزش از نحو پوسته‌ی POSIX استفاده می‌کنند. پوسته‌های
پیش‌فرض بیشتر سیستم‌های Linux و macOS (برای مثال bash، zsh یا sh) از این نحو
پشتیبانی می‌کنند. کاربران ویندوز باید برای اجرای دستورها به همان شکلی که نوشته
شده‌اند، از یک پوسته‌ی سازگار با POSIX مانند
[زیرسیستم ویندوز برای لینوکس (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install)
یا [Git Bash](https://gitforwindows.org/) استفاده کنند.
دستورهایی که از `export`، `$()` و ساختارهای مشابه استفاده می‌کنند، با PowerShell
یا Command Prompt ویندوز سازگار **نیستند**.


## به‌روزرسانی یک برنامه

{{% alert %}}
_به‌روزرسانی‌های تدریجی با جایگزین‌کردن تدریجی نمونه‌های Pod با نمونه‌های جدید،
امکان به‌روزرسانی Deploymentها را بدون هیچ‌گونه وقفه در دسترس‌پذیری فراهم می‌کنند._
{{% /alert %}}

کاربران انتظار دارند برنامه‌ها همیشه در دسترس باشند و از توسعه‌دهندگان انتظار
می‌رود چندین بار در روز نسخه‌های جدید آن‌ها را مستقر کنند. در کوبرنتیز این کار
با به‌روزرسانی‌های تدریجی انجام می‌شود. **به‌روزرسانی تدریجی** (rolling update)
امکان می‌دهد یک Deployment بدون هیچ وقفه‌ای به‌روزرسانی شود. این کار با جایگزین‌کردن
تدریجی Podهای فعلی با Podهای جدید انجام می‌شود. Podهای جدید روی نودهایی که منابع
در دسترس دارند زمان‌بندی می‌شوند و کوبرنتیز پیش از حذف Podهای قدیمی، منتظر
راه‌اندازی Podهای جدید می‌ماند.

در ماژول قبلی، برنامه‌ی خود را برای اجرای چند نمونه مقیاس‌دهی کردیم. این کار
پیش‌نیاز انجام به‌روزرسانی‌ها بدون اثرگذاشتن بر دسترس‌پذیری برنامه است.
به‌طور پیش‌فرض، حداکثر تعداد Podهایی که ممکن است در طول به‌روزرسانی در دسترس
نباشند و حداکثر تعداد Podهای جدیدی که می‌توان ایجاد کرد، یک است. هر دو گزینه را
می‌توان به‌صورت عدد یا درصد (از تعداد Podها) پیکربندی کرد. در کوبرنتیز،
به‌روزرسانی‌ها نسخه‌بندی می‌شوند و هر به‌روزرسانی Deployment را می‌توان به نسخه‌ی
(پایدار) قبلی بازگرداند.

## نمای کلی به‌روزرسانی‌های تدریجی

<!-- animation -->
{{< tutorials/carousel id="myCarousel" interval="3000" >}}
  {{< tutorials/carousel-item image="/docs/tutorials/kubernetes-basics/public/images/module_06_rollingupdates1.svg" active="true" >}}

  {{< tutorials/carousel-item image="/docs/tutorials/kubernetes-basics/public/images/module_06_rollingupdates2.svg" >}}

  {{< tutorials/carousel-item image="/docs/tutorials/kubernetes-basics/public/images/module_06_rollingupdates3.svg" >}}

  {{< tutorials/carousel-item image="/docs/tutorials/kubernetes-basics/public/images/module_06_rollingupdates4.svg" >}}
{{< /tutorials/carousel >}}

{{% alert %}}
اگر یک Deployment به‌صورت عمومی در معرض دسترسی قرار گرفته باشد، Service ترافیک را فقط به Podهایی می‌فرستد که توانایی رسیدگی به درخواست‌ها را دارند.  
به این ترتیب کاربران در طول به‌روزرسانی همچنان به برنامه دسترسی خواهند داشت.
{{% /alert %}}

در طول یک به‌روزرسانی تدریجی، این رفتار با هدایت ترافیک فقط به Podهایی که در حال پاسخ‌گویی به درخواست‌ها هستند، برنامه را در دسترس نگه می‌دارد.
به‌روزرسانی‌های تدریجی امکان انجام کارهای زیر را فراهم می‌کنند:

* انتقال یک برنامه از یک محیط به محیطی دیگر (از طریق به‌روزرسانی ایمیج کانتینر)
* بازگشت به نسخه‌های قبلی
* یکپارچه‌سازی مداوم و تحویل مداوم برنامه‌ها بدون هیچ وقفه‌ای

در آموزش تعاملی زیر، برنامه‌ی خود را به نسخه‌ای جدید به‌روزرسانی می‌کنیم و یک
بازگشت (rollback) نیز انجام می‌دهیم.

### به‌روزرسانی نسخه‌ی برنامه

برای فهرست‌کردن Deploymentها، زیرفرمان `get deployments` را اجرا کنید:

```shell
kubectl get deployments
```

برای فهرست‌کردن Podهای در حال اجرا، زیرفرمان `get pods` را اجرا کنید:

```shell
kubectl get pods
```

برای مشاهده‌ی نسخه‌ی فعلی ایمیج برنامه، زیرفرمان `describe pods` را اجرا کنید
و به دنبال فیلد `Image` بگردید:

```shell
kubectl describe pods
```

برای به‌روزرسانی ایمیج برنامه به نسخه‌ی ۲، از زیرفرمان `set image` و پس از آن
نام Deployment و نسخه‌ی جدید ایمیج استفاده کنید:

```shell
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=docker.io/jocatalin/kubernetes-bootcamp:v2
```

این دستور به Deployment اعلام کرد که از ایمیج دیگری برای برنامه‌ی شما استفاده
کند و یک به‌روزرسانی تدریجی را آغاز کرد. با زیرفرمان `get pods` وضعیت Podهای
جدید را بررسی کنید و خاتمه‌یافتن Pod قدیمی را مشاهده کنید:

```shell
kubectl get pods
```

### تأیید به‌روزرسانی

ابتدا بررسی کنید که سرویس در حال اجرا باشد، زیرا ممکن است آن را در مرحله‌ی
قبلی آموزش حذف کرده باشید. برای این کار `describe services/kubernetes-bootcamp`
را اجرا کنید. اگر سرویس وجود نداشت، می‌توانید آن را با دستور زیر دوباره ایجاد کنید:

```shell
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
```

یک متغیر محیطی به نام `NODE_PORT` ایجاد کنید که مقدار آن پورت نود
اختصاص‌یافته باشد:

```shell
export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo "NODE_PORT=$NODE_PORT"
```

سپس با `curl` به IP و پورت در معرض دسترسی درخواست بفرستید:

```shell
curl http://"$(minikube ip):$NODE_PORT"
```

هر بار که دستور `curl` را اجرا می‌کنید، درخواست شما به Pod متفاوتی می‌رسد.
توجه کنید که اکنون همه‌ی Podها آخرین نسخه (`v2`) را اجرا می‌کنند.

همچنین می‌توانید با اجرای زیرفرمان `rollout status` به‌روزرسانی را تأیید کنید:

```shell
kubectl rollout status deployments/kubernetes-bootcamp
```

برای مشاهده‌ی نسخه‌ی فعلی ایمیج برنامه، زیرفرمان describe pods را اجرا کنید:

```shell
kubectl describe pods
```

در فیلد `Image` خروجی، بررسی کنید که آخرین نسخه‌ی ایمیج (`v2`) را اجرا می‌کنید.

### بازگرداندن یک به‌روزرسانی

بیایید به‌روزرسانی دیگری انجام دهیم و ایمیجی با برچسب `v10` را مستقر کنیم:

```shell
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10
```

برای مشاهده‌ی وضعیت Deployment از `get deployments` استفاده کنید:

```shell
kubectl get deployments
```

توجه کنید که خروجی، تعداد مطلوب Podهای در دسترس را نشان نمی‌دهد. برای
فهرست‌کردن همه‌ی Podها، زیرفرمان `get pods` را اجرا کنید:

```shell
kubectl get pods
```

توجه کنید که وضعیت برخی از Podها `ImagePullBackOff` است.

برای بررسی دقیق‌تر مشکل، زیرفرمان `describe pods` را اجرا کنید:

```shell
kubectl describe pods
```

در بخش `Events` خروجی مربوط به Podهای آسیب‌دیده، می‌بینید که نسخه‌ی `v10`
ایمیج در مخزن وجود نداشته است.

برای بازگرداندن Deployment به آخرین نسخه‌ی سالم، از زیرفرمان `rollout undo`
استفاده کنید:

```shell
kubectl rollout undo deployments/kubernetes-bootcamp
```

دستور `rollout undo` استقرار را به وضعیت شناخته‌شده‌ی قبلی (نسخه‌ی `v2` ایمیج)
بازمی‌گرداند. به‌روزرسانی‌ها نسخه‌بندی می‌شوند و می‌توانید به هر وضعیت
شناخته‌شده‌ی قبلی یک Deployment بازگردید.

با زیرفرمان `get pods` دوباره Podها را فهرست کنید:

```shell
kubectl get pods
```

برای بررسی ایمیج مستقرشده روی Podهای در حال اجرا، از زیرفرمان `describe pods`
استفاده کنید:

```shell
kubectl describe pods
```

اکنون Deployment دوباره از نسخه‌ی پایدار برنامه (`v2`) استفاده می‌کند. بازگشت
با موفقیت انجام شد.

فراموش نکنید که کلاستر محلی خود را پاک‌سازی کنید.

```shell
kubectl delete deployments/kubernetes-bootcamp services/kubernetes-bootcamp
```

## {{% heading "whatsnext" %}}

* درباره‌ی [Deploymentها](/docs/concepts/workloads/controllers/deployment/) بیشتر بیاموزید.
