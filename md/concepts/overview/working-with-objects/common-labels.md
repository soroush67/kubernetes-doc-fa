---
title: برچسب‌های توصیه‌شده
content_type: concept
weight: 100
---

<!-- overview -->
می‌توانید آبجکت‌های کوبرنتیز را با ابزارهایی فراتر از kubectl و
داشبورد مصورسازی و مدیریت کنید. مجموعه‌ای مشترک از برچسب‌ها به ابزارها امکان می‌دهد به‌صورت تعامل‌پذیر کار کنند
و آبجکت‌ها را به شیوه‌ای مشترک توصیف کنند که همه‌ی ابزارها بتوانند آن را درک کنند.

برچسب‌های توصیه‌شده علاوه بر پشتیبانی از ابزارها، برنامه‌ها را
به شیوه‌ای توصیف می‌کنند که بتوان آن‌ها را پرس‌وجو کرد.


<!-- body -->
فراداده‌ها حول مفهوم _برنامه_ سازمان‌دهی شده‌اند. کوبرنتیز یک
پلتفرم به‌عنوان سرویس (PaaS) نیست و مفهوم رسمی‌ای از برنامه ندارد و آن را الزامی نمی‌کند.
در عوض، برنامه‌ها غیررسمی هستند و با فراداده توصیف می‌شوند. تعریف
اینکه یک برنامه شامل چه چیزهایی است، انعطاف‌پذیر است.

{{< note >}}
این‌ها برچسب‌های توصیه‌شده هستند. این برچسب‌ها مدیریت برنامه‌ها را آسان‌تر می‌کنند،
اما برای هیچ‌یک از ابزارهای هسته‌ای الزامی نیستند.
{{< /note >}}

برچسب‌ها و حاشیه‌نویسی‌های مشترک، پیشوند مشترکی دارند: `app.kubernetes.io`. برچسب‌های
بدون پیشوند مختص کاربران هستند. پیشوند مشترک تضمین می‌کند که برچسب‌های مشترک
با برچسب‌های سفارشی کاربران تداخل نداشته باشند.

## برچسب‌ها

برای بهره‌گیری کامل از این برچسب‌ها، باید آن‌ها را
روی هر آبجکت منبع اعمال کرد.

| کلید                                 | توضیح           | نمونه  | نوع |
| ----------------------------------- | --------------------- | -------- | ---- |
| `app.kubernetes.io/name`            | نام برنامه | `mysql` | string |
| `app.kubernetes.io/instance`        | نامی یکتا که نمونه‌ای از یک برنامه را شناسایی می‌کند | `mysql-abcxyz` | string |
| `app.kubernetes.io/version`         | نسخه‌ی فعلی برنامه (برای مثال، یک [SemVer 1.0](https://semver.org/spec/v1.0.0.html)، هش بازبینی و غیره) | `5.7.21` | string |
| `app.kubernetes.io/component`       | مؤلفه در درون معماری | `database` | string |
| `app.kubernetes.io/part-of`         | نام برنامه‌ی سطح بالاتری که این برنامه بخشی از آن است | `wordpress` | string |
| `app.kubernetes.io/managed-by`      | ابزاری که برای مدیریت عملیات یک برنامه به کار می‌رود | `Helm` | string |

برای نشان‌دادن کاربرد این برچسب‌ها در عمل، آبجکت {{< glossary_tooltip text="StatefulSet" term_id="statefulset" >}} زیر را در نظر بگیرید:

```yaml
# This is an excerpt
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
    app.kubernetes.io/managed-by: Helm
```

## برنامه‌ها و نمونه‌های برنامه‌ها

یک برنامه را می‌توان یک یا چند بار در یک کلاستر کوبرنتیز و
در برخی موارد در یک فضای نام یکسان نصب کرد. برای مثال، WordPress را می‌توان بیش
از یک بار نصب کرد، به‌طوری که وب‌سایت‌های مختلف، نصب‌های جداگانه‌ای از WordPress باشند.

نام برنامه و نام نمونه به‌طور جداگانه ثبت می‌شوند. برای
مثال، WordPress دارای `app.kubernetes.io/name` با مقدار `wordpress` است، در حالی که
یک نام نمونه نیز دارد که به‌صورت `app.kubernetes.io/instance` با مقدار
`wordpress-abcxyz` نمایش داده می‌شود. این کار امکان شناسایی برنامه و نمونه‌ی برنامه
را فراهم می‌کند. هر نمونه از یک برنامه باید نامی یکتا داشته باشد.

## نمونه‌ها

برای نشان‌دادن روش‌های مختلف استفاده از این برچسب‌ها، نمونه‌های زیر با پیچیدگی‌های متفاوت ارائه شده‌اند.

### یک سرویس ساده‌ی بدون حالت

موردی را در نظر بگیرید که یک سرویس ساده‌ی بدون حالت با استفاده از آبجکت‌های `Deployment` و `Service` مستقر شده است. دو قطعه‌ی زیر نشان می‌دهند که چگونه می‌توان از برچسب‌ها در ساده‌ترین شکل استفاده کرد.

از `Deployment` برای نظارت بر Podهایی استفاده می‌شود که خودِ برنامه را اجرا می‌کنند.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/name: myservice
    app.kubernetes.io/instance: myservice-abcxyz
...
```

از `Service` برای در دسترس قرار دادن برنامه استفاده می‌شود.
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: myservice
    app.kubernetes.io/instance: myservice-abcxyz
...
```

### برنامه‌ی وب همراه با پایگاه داده

برنامه‌ای کمی پیچیده‌تر را در نظر بگیرید: یک برنامه‌ی وب (WordPress)
که از یک پایگاه داده (MySQL) استفاده می‌کند و با Helm نصب شده است. قطعه‌های زیر
بخش آغازین آبجکت‌هایی را نشان می‌دهند که برای استقرار این برنامه به کار می‌روند.

بخش آغازین `Deployment` زیر برای WordPress به کار می‌رود:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/name: wordpress
    app.kubernetes.io/instance: wordpress-abcxyz
    app.kubernetes.io/version: "4.9.4"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: server
    app.kubernetes.io/part-of: wordpress
...
```

از `Service` برای در دسترس قرار دادن WordPress استفاده می‌شود:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: wordpress
    app.kubernetes.io/instance: wordpress-abcxyz
    app.kubernetes.io/version: "4.9.4"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: server
    app.kubernetes.io/part-of: wordpress
...
```

MySQL به‌صورت یک `StatefulSet` همراه با فراداده‌هایی هم برای خودش و هم برای برنامه‌ی بزرگ‌تری که به آن تعلق دارد در دسترس قرار می‌گیرد:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
...
```

از `Service` برای در دسترس قرار دادن MySQL به‌عنوان بخشی از WordPress استفاده می‌شود:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
...
```

در `StatefulSet` و `Service` مربوط به MySQL خواهید دید که اطلاعات مربوط به هر دو، یعنی MySQL و WordPress که برنامه‌ی گسترده‌تر است، گنجانده شده است.
