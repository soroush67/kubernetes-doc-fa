---
title: دسترسی به کلاسترها
weight: 20
content_type: concept
---

<!-- overview -->

در این مبحث، روش‌های مختلف تعامل با کلاسترها بررسی می‌شود.

<!-- body -->

## نخستین دسترسی با kubectl

برای نخستین دسترسی به API کوبرنتیز، پیشنهاد می‌کنیم از رابط خط فرمان کوبرنتیز،
یعنی `kubectl`، استفاده کنید.

برای دسترسی به یک کلاستر، باید نشانی کلاستر را بدانید و اطلاعات احراز هویت (credentials)
لازم برای دسترسی به آن را در اختیار داشته باشید. معمولاً وقتی مراحل یک
[راهنمای شروع به کار](/docs/setup/) را دنبال می‌کنید، این موارد به‌طور خودکار تنظیم می‌شوند؛
یا ممکن است شخص دیگری کلاستر را راه‌اندازی کرده و اطلاعات احراز هویت و نشانی آن را در اختیارتان گذاشته باشد.

با این دستور، نشانی و اطلاعات احراز هویتی را که kubectl از آن‌ها آگاه است بررسی کنید:

```shell
kubectl config view
```

بسیاری از [مثال‌ها](/docs/reference/kubectl/quick-reference/) مقدمه‌ای بر استفاده از
`kubectl` ارائه می‌دهند و مستندات کامل آن را می‌توانید در
[مرجع kubectl](/docs/reference/kubectl/) بیابید.

## دسترسی مستقیم به REST API

ابزار kubectl یافتن apiserver و احراز هویت در آن را خودش انجام می‌دهد.
اگر می‌خواهید با یک کلاینت http مانند curl یا wget، یا با یک مرورگر، مستقیماً به REST API
دسترسی پیدا کنید، چند روش برای یافتن apiserver و احراز هویت در آن وجود دارد:

- اجرای kubectl در حالت پراکسی.
  - روش توصیه‌شده.
  - از نشانی ذخیره‌شدهٔ apiserver استفاده می‌کند.
  - هویت apiserver را با گواهی خودامضا (self-signed) تأیید می‌کند. حملهٔ مرد میانی (MITM) امکان‌پذیر نیست.
  - در apiserver احراز هویت می‌کند.
  - ممکن است در آینده توازن بار هوشمند و جایگزینی هنگام خرابی (failover) را در سمت کلاینت انجام دهد.
- ارائهٔ مستقیم نشانی و اطلاعات احراز هویت به کلاینت http.
  - روش جایگزین.
  - با برخی انواع کد کلاینت که استفاده از پراکسی برایشان مشکل‌ساز است کار می‌کند.
  - برای محافظت در برابر حملهٔ مرد میانی، باید یک گواهی ریشه را در مرورگر خود وارد کنید.

### استفاده از kubectl proxy

دستور زیر kubectl را در حالتی اجرا می‌کند که در آن مانند یک پراکسی معکوس (reverse proxy) عمل می‌کند.
این دستور یافتن apiserver و احراز هویت را انجام می‌دهد.
آن را به این صورت اجرا کنید:

```shell
kubectl proxy --port=8080
```

برای جزئیات بیشتر، [kubectl proxy](/docs/reference/generated/kubectl/kubectl-commands/#proxy) را ببینید.

سپس می‌توانید API را با curl، wget یا یک مرورگر بررسی کنید؛ برای IPv6 به‌جای localhost
از [::1] استفاده کنید، مانند زیر:

```shell
curl http://localhost:8080/api/
```

خروجی مشابه این است:

```json
{
  "kind": "APIVersions",
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
```

### بدون kubectl proxy

با استفاده از `kubectl apply` و `kubectl describe secret...` همراه با grep/cut، یک توکن برای حساب سرویس پیش‌فرض بسازید:

ابتدا Secret را ایجاد کنید و در آن یک توکن برای ServiceAccount پیش‌فرض درخواست کنید:

```shell
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: default-token
  annotations:
    kubernetes.io/service-account.name: default
type: kubernetes.io/service-account-token
EOF
```

سپس صبر کنید تا کنترل‌کنندهٔ توکن، Secret را با یک توکن پر کند:

```shell
while ! kubectl describe secret default-token | grep -E '^token' >/dev/null; do
  echo "waiting for token..." >&2
  sleep 1
done
```

توکن تولیدشده را دریافت و استفاده کنید:

```shell
APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")
TOKEN=$(kubectl describe secret default-token | grep -E '^token' | cut -f2 -d':' | tr -d " ")

curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
```

خروجی مشابه این است:

```json
{
  "kind": "APIVersions",
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
```

با استفاده از `jsonpath`:

```shell
APISERVER=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')
TOKEN=$(kubectl get secret default-token -o jsonpath='{.data.token}' | base64 --decode)

curl $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
```

خروجی مشابه این است:

```json
{
  "kind": "APIVersions",
  "versions": [
    "v1"
  ],
  "serverAddressByClientCIDRs": [
    {
      "clientCIDR": "0.0.0.0/0",
      "serverAddress": "10.0.1.149:443"
    }
  ]
}
```

مثال‌های بالا از فلگ `--insecure` استفاده می‌کنند. این کار ارتباط را در معرض حملات مرد میانی
قرار می‌دهد. وقتی kubectl به کلاستر دسترسی پیدا می‌کند، برای دسترسی به سرور از یک گواهی ریشهٔ
ذخیره‌شده و گواهی‌های کلاینت استفاده می‌کند. (این گواهی‌ها در دایرکتوری `~/.kube` نصب
می‌شوند.) از آنجا که گواهی‌های کلاستر معمولاً خودامضا هستند، ممکن است برای واداشتن کلاینت http
به استفاده از گواهی ریشه، به پیکربندی ویژه‌ای نیاز باشد.

در برخی کلاسترها، apiserver به احراز هویت نیاز ندارد؛ ممکن است فقط روی localhost سرویس بدهد
یا با یک دیوار آتش (firewall) محافظت شود. استاندارد مشخصی برای این موضوع وجود ندارد.
صفحهٔ [کنترل دسترسی به API](/docs/concepts/security/controlling-access)
توضیح می‌دهد که مدیر کلاستر چگونه می‌تواند این موارد را پیکربندی کند.

## دسترسی برنامه‌نویسی به API

کوبرنتیز به‌طور رسمی از کتابخانه‌های کلاینت [Go](#go-client) و [Python](#python-client)
پشتیبانی می‌کند.

### کلاینت Go

* برای دریافت کتابخانه، دستور `go get k8s.io/client-go@kubernetes-<kubernetes-version-number>` را اجرا کنید.
  برای دستورالعمل‌های تفصیلی نصب، [INSTALL.md](https://github.com/kubernetes/client-go/blob/master/INSTALL.md#for-the-casual-user)
  را ببینید. برای اطلاع از نسخه‌های پشتیبانی‌شده، به
  [https://github.com/kubernetes/client-go](https://github.com/kubernetes/client-go#compatibility-matrix)
  مراجعه کنید.
* برنامهٔ خود را بر پایهٔ کلاینت‌های client-go بنویسید. توجه کنید که client-go آبجکت‌های API
  مخصوص به خود را تعریف می‌کند؛ بنابراین در صورت نیاز، تعریف‌های API را از client-go وارد کنید، نه از مخزن اصلی.
  برای مثال، `import "k8s.io/client-go/kubernetes"` درست است.

کلاینت Go می‌تواند برای یافتن apiserver و احراز هویت در آن، از همان
[فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
که رابط خط فرمان kubectl استفاده می‌کند بهره بگیرد. این
[مثال](https://git.k8s.io/client-go/examples/out-of-cluster-client-configuration/main.go) را ببینید.

اگر برنامه به‌صورت یک Pod در کلاستر مستقر شده است، به [بخش بعدی](#accessing-the-api-from-a-pod) مراجعه کنید.

### کلاینت Python

برای استفاده از [کلاینت Python](https://github.com/kubernetes-client/python)، دستور
`pip install kubernetes` را اجرا کنید. برای گزینه‌های بیشتر نصب، [صفحهٔ کتابخانهٔ کلاینت Python](https://github.com/kubernetes-client/python)
را ببینید.

کلاینت Python می‌تواند برای یافتن apiserver و احراز هویت در آن، از همان
[فایل kubeconfig](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
که رابط خط فرمان kubectl استفاده می‌کند بهره بگیرد. این
[مثال](https://github.com/kubernetes-client/python/tree/master/examples) را ببینید.

### زبان‌های دیگر

برای دسترسی به API از زبان‌های دیگر نیز [کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/) وجود دارد.
برای آگاهی از نحوهٔ احراز هویت آن‌ها، مستندات هر کتابخانه را ببینید.

## دسترسی به API از درون یک Pod

هنگام دسترسی به API از درون یک پاد، یافتن سرور API و احراز هویت در آن
اندکی متفاوت است.

برای جزئیات بیشتر، صفحهٔ [دسترسی به API از درون یک Pod](/docs/tasks/run-application/access-api-from-pod/)
را ببینید.

## دسترسی به سرویس‌های در حال اجرا روی کلاستر

بخش قبلی نحوهٔ اتصال به سرور API کوبرنتیز را توضیح می‌دهد.
برای اطلاعات دربارهٔ اتصال به سایر سرویس‌هایی که روی یک کلاستر کوبرنتیز اجرا می‌شوند، صفحهٔ
[دسترسی به سرویس‌های کلاستر](/docs/tasks/access-application-cluster/access-cluster-services/) را ببینید.

## درخواست تغییر مسیر

قابلیت‌های تغییر مسیر (redirect) منسوخ و حذف شده‌اند. به‌جای آن‌ها از یک پراکسی (توضیح در ادامه) استفاده کنید.

## پراکسی‌های فراوان

هنگام استفاده از کوبرنتیز ممکن است با چند پراکسی مختلف روبه‌رو شوید:

1. [پراکسی kubectl](#directly-accessing-the-rest-api):

   - روی رایانهٔ رومیزی کاربر یا درون یک پاد اجرا می‌شود
   - درخواست‌ها را از یک نشانی localhost به apiserver کوبرنتیز پراکسی می‌کند
   - ارتباط کلاینت با پراکسی از HTTP استفاده می‌کند
   - ارتباط پراکسی با apiserver از HTTPS استفاده می‌کند
   - apiserver را پیدا می‌کند
   - سرآیندهای احراز هویت را اضافه می‌کند

1. [پراکسی apiserver](/docs/tasks/access-application-cluster/access-cluster-services/#discovering-builtin-services):

   - یک دژ (bastion) تعبیه‌شده در apiserver است
   - کاربری را که بیرون از کلاستر است به IPهای کلاستر وصل می‌کند که در غیر این صورت ممکن است در دسترس نباشند
   - درون پردازه‌های apiserver اجرا می‌شود
   - ارتباط کلاینت با پراکسی از HTTPS استفاده می‌کند (یا http، اگر apiserver چنین پیکربندی شده باشد)
   - ارتباط پراکسی با مقصد، بسته به انتخاب پراکسی بر اساس اطلاعات موجود، ممکن است از HTTP یا HTTPS استفاده کند
   - می‌توان از آن برای دسترسی به یک Node، Pod یا Service استفاده کرد
   - هنگام استفاده برای دسترسی به یک Service، توازن بار را انجام می‌دهد

1. [پراکسی kube](/docs/concepts/services-networking/service/#ips-and-vips):

   - روی هر نود اجرا می‌شود
   - ترافیک UDP و TCP را پراکسی می‌کند
   - پروتکل HTTP را درک نمی‌کند
   - توازن بار را فراهم می‌کند
   - فقط برای دسترسی به سرویس‌ها استفاده می‌شود

1. یک پراکسی/متوازن‌کنندهٔ بار در جلوی apiserver(ها):

   - وجود و پیاده‌سازی آن از کلاستری به کلاستر دیگر متفاوت است (برای مثال nginx)
   - میان همهٔ کلاینت‌ها و یک یا چند apiserver قرار می‌گیرد
   - اگر چند apiserver وجود داشته باشد، نقش متوازن‌کنندهٔ بار را ایفا می‌کند.

1. متوازن‌کننده‌های بار ابری روی سرویس‌های خارجی:

   - برخی ارائه‌دهندگان ابری آن‌ها را فراهم می‌کنند (برای مثال AWS ELB و Google Cloud Load Balancer)
   - وقتی نوع سرویس کوبرنتیز `LoadBalancer` باشد، به‌طور خودکار ایجاد می‌شوند
   - فقط از UDP/TCP استفاده می‌کنند
   - پیاده‌سازی آن‌ها بسته به ارائه‌دهندهٔ ابری متفاوت است.

کاربران کوبرنتیز معمولاً لازم نیست نگران چیزی جز دو نوع نخست باشند. مدیر کلاستر
معمولاً اطمینان حاصل می‌کند که انواع بعدی به‌درستی راه‌اندازی شده باشند.
