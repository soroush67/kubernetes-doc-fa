---
reviewers:
- caesarxuchao
- mikedanese
title: دسترسی به پوسته‌ی یک کانتینر در حال اجرا
content_type: task
---

<!-- overview -->

این صفحه نشان می‌دهد که چگونه با استفاده از `kubectl exec` به پوسته‌ی (shell) یک کانتینر در حال اجرا دسترسی پیدا کنید.




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}




<!-- steps -->

## دسترسی به پوسته‌ی یک کانتینر

در این تمرین، یک Pod با یک کانتینر ایجاد می‌کنید. این کانتینر ایمیج nginx را اجرا می‌کند. فایل پیکربندی این Pod در ادامه آمده است:

{{% code_sample file="application/shell-demo.yaml" %}}

Pod را ایجاد کنید:

```shell
kubectl apply -f https://k8s.io/examples/application/shell-demo.yaml
```

بررسی کنید که کانتینر در حال اجرا باشد:

```shell
kubectl get pod shell-demo
```

به پوسته‌ی کانتینر در حال اجرا دسترسی پیدا کنید:

```shell
kubectl exec --stdin --tty shell-demo -- /bin/bash
```

{{< note >}}
خط تیره‌ی دوتایی (`--`) آرگومان‌هایی را که می‌خواهید به فرمان ارسال کنید، از آرگومان‌های kubectl جدا می‌کند.
{{< /note >}}

در پوسته‌ی خود، محتویات دایرکتوری ریشه را فهرست کنید:

```shell
# Run this inside the container
ls /
```

در پوسته‌ی خود، فرمان‌های دیگر را نیز امتحان کنید. چند نمونه در ادامه آمده است:

```shell
# You can run these example commands inside the container
ls /
cat /proc/mounts
cat /proc/1/maps
apt-get update
apt-get install -y tcpdump
tcpdump
apt-get install -y lsof
lsof
apt-get install -y procps
ps aux
ps aux | grep nginx
```

## نوشتن صفحه‌ی اصلی برای nginx

دوباره به فایل پیکربندی Pod خود نگاه کنید. این Pod یک حجم (volume) از نوع `emptyDir` دارد و کانتینر این حجم را در مسیر `/usr/share/nginx/html` مانت (mount) می‌کند.

در پوسته‌ی خود، یک فایل `index.html` در دایرکتوری `/usr/share/nginx/html` ایجاد کنید:

```shell
# Run this inside the container
echo 'Hello shell demo' > /usr/share/nginx/html/index.html
```

در پوسته‌ی خود، یک درخواست GET به سرور nginx ارسال کنید:

```shell
# Run this in the shell inside your container
apt-get update
apt-get install curl
curl http://localhost/
```

خروجی، متنی را که در فایل `index.html` نوشته‌اید نشان می‌دهد:

```
Hello shell demo
```

پس از پایان کار با پوسته، `exit` را وارد کنید.

```shell
exit # To quit the shell in the container
```

## اجرای فرمان‌های منفرد در یک کانتینر

در یک پنجره‌ی فرمان معمولی، و نه در پوسته‌ی کانتینر، متغیرهای محیطی کانتینر در حال اجرا را فهرست کنید:

```shell
kubectl exec shell-demo -- env
```

اجرای فرمان‌های دیگر را نیز امتحان کنید. چند نمونه در ادامه آمده است:

```shell
kubectl exec shell-demo -- ps aux
kubectl exec shell-demo -- ls /
kubectl exec shell-demo -- cat /proc/1/mounts
```



<!-- discussion -->

## باز کردن پوسته در Podای که بیش از یک کانتینر دارد

اگر یک Pod بیش از یک کانتینر داشته باشد، برای مشخص کردن کانتینر در فرمان `kubectl exec` از `--container` یا `-c` استفاده کنید. برای مثال، فرض کنید Podای به نام my-pod دارید که دو کانتینر به نام‌های _main-app_ و _helper-app_ دارد. فرمان زیر پوسته‌ای را در کانتینر _main-app_ باز می‌کند.

```shell
kubectl exec -i -t my-pod --container main-app -- /bin/bash
```

{{< note >}}
گزینه‌های کوتاه `-i` و `-t` همان گزینه‌های بلند `--stdin` و `--tty` هستند.
{{< /note >}}


## {{% heading "whatsnext" %}}


* درباره‌ی [kubectl exec](/docs/reference/generated/kubectl/kubectl-commands/#exec) مطالعه کنید.
