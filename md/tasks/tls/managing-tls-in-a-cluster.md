---
title: مدیریت گواهی‌های TLS در کلاستر
content_type: task
reviewers:
- mikedanese
- beacham
- liggit
---

<!-- overview -->

کوبرنتیز یک API به نام `certificates.k8s.io` فراهم می‌کند که با آن می‌توانید گواهی‌های TLS امضاشده توسط یک مرجع صدور گواهی (Certificate Authority یا CA) تحت کنترل خودتان را تهیه کنید. بارهای کاری شما می‌توانند از این CAها و گواهی‌ها برای برقراری اعتماد استفاده کنند.

API ‏`certificates.k8s.io` از پروتکلی مشابه [پیش‌نویس ACME](https://github.com/ietf-wg-acme/acme/) استفاده می‌کند.

{{< note >}}
گواهی‌هایی که با API ‏`certificates.k8s.io` ایجاد می‌شوند، با یک [CA اختصاصی](#configuring-your-cluster-to-provide-signing) امضا می‌شوند. می‌توان کلاستر را طوری پیکربندی کرد که برای این منظور از CA ریشه‌ی کلاستر استفاده کند، اما هرگز نباید به این موضوع تکیه کنید. فرض نکنید که این گواهی‌ها در برابر CA ریشه‌ی کلاستر اعتبارسنجی می‌شوند.
{{< /note >}}




## {{% heading "prerequisites" %}}


{{< include "task-tutorial-prereqs.md" >}}

به ابزار `cfssl` نیاز دارید. می‌توانید `cfssl` را از
[https://github.com/cloudflare/cfssl/releases](https://github.com/cloudflare/cfssl/releases) دانلود کنید.

برخی از مراحل این صفحه از ابزار `jq` استفاده می‌کنند. اگر `jq` را ندارید، می‌توانید آن را از طریق منابع نرم‌افزاری سیستم‌عامل خود نصب کنید یا از
[https://jqlang.github.io/jq/](https://jqlang.github.io/jq/) دریافت کنید.

<!-- steps -->

## اعتماد به TLS در کلاستر

اعتماد به [CA سفارشی](#configuring-your-cluster-to-provide-signing) از سوی برنامه‌ای که به‌صورت پاد اجرا می‌شود، معمولاً به پیکربندی اضافه‌ای در برنامه نیاز دارد. باید بسته‌ی گواهی CA را به فهرست گواهی‌های CA مورد اعتماد کلاینت یا سرور TLS اضافه کنید. برای مثال، در پیکربندی TLS زبان Golang این کار را با تجزیه‌ی زنجیره‌ی گواهی و افزودن گواهی‌های تجزیه‌شده به فیلد `RootCAs` در ساختار
[`tls.Config`](https://pkg.go.dev/crypto/tls#Config) انجام می‌دهید.

{{< note >}}
با اینکه ممکن است گواهی CA سفارشی در سیستم فایل (در ConfigMap ‏`kube-root-ca.crt`) وجود داشته باشد، نباید از این مرجع صدور گواهی برای هیچ هدفی جز تأیید endpointهای داخلی کوبرنتیز استفاده کنید. نمونه‌ای از endpoint داخلی کوبرنتیز، Service با نام `kubernetes` در فضای نام default است.

اگر می‌خواهید برای بارهای کاری خود از یک مرجع صدور گواهی سفارشی استفاده کنید، باید آن CA را جداگانه تولید کنید و گواهی CA آن را از طریق یک
[ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap) توزیع کنید که پادهای شما اجازه‌ی خواندن آن را داشته باشند.
{{< /note >}}

## درخواست گواهی

بخش زیر نشان می‌دهد چگونه برای یک سرویس کوبرنتیز که از طریق DNS به آن دسترسی پیدا می‌شود، گواهی TLS ایجاد کنید.

{{< note >}}
این آموزش از CFSSL، یعنی جعبه‌ابزار PKI و TLS شرکت Cloudflare، استفاده می‌کند. برای اطلاعات بیشتر، مقاله‌ی وبلاگ Cloudflare با عنوان
[Introducing CFSSL - CloudFlare's PKI toolkit](https://blog.cloudflare.com/introducing-cfssl/) را ببینید.
{{< /note >}}

## ایجاد درخواست امضای گواهی

با اجرای دستور زیر، یک کلید خصوصی و یک درخواست امضای گواهی (certificate signing request یا CSR) تولید کنید:

```shell
cat <<EOF | cfssl genkey - | cfssljson -bare server
{
  "hosts": [
    "my-svc.my-namespace.svc.cluster.local",
    "my-pod.my-namespace.pod.cluster.local",
    "192.0.2.24",
    "10.0.34.2"
  ],
  "CN": "my-pod.my-namespace.pod.cluster.local",
  "key": {
    "algo": "ecdsa",
    "size": 256
  }
}
EOF
```

در اینجا `192.0.2.24` همان IP کلاستری سرویس، `my-svc.my-namespace.svc.cluster.local` نام DNS سرویس، `10.0.34.2` آدرس IP پاد و `my-pod.my-namespace.pod.cluster.local` نام DNS پاد است. باید خروجی‌ای مشابه زیر ببینید:

```
2022/02/01 11:45:32 [INFO] generate received request
2022/02/01 11:45:32 [INFO] received CSR
2022/02/01 11:45:32 [INFO] generating key: ecdsa-256
2022/02/01 11:45:32 [INFO] encoded CSR
```

این دستور دو فایل تولید می‌کند: فایل `server.csr` که حاوی درخواست گواهی
[PKCS#10](https://tools.ietf.org/html/rfc2986) با کدگذاری PEM است، و فایل `server-key.pem` که حاوی کلید با کدگذاری PEM برای گواهی‌ای است که هنوز باید ایجاد شود.

## ایجاد آبجکت CertificateSigningRequest برای ارسال به API کوبرنتیز

یک مانیفست CSR (به‌صورت YAML) تولید کنید و آن را به سرور API بفرستید. این کار را می‌توانید با اجرای دستور زیر انجام دهید:

```shell
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: my-svc.my-namespace
spec:
  request: $(cat server.csr | base64 | tr -d '\n')
  signerName: example.com/serving
  usages:
  - digital signature
  - key encipherment
  - server auth
EOF
```

توجه کنید که فایل `server.csr` ایجادشده در مرحله‌ی ۱ با base64 کدگذاری شده و در فیلد `.spec.request` قرار گرفته است. همچنین گواهی‌ای با کاربردهای کلید "digital signature"، "key encipherment" و "server auth" درخواست می‌کنید که قرار است امضاکننده‌ی نمونه‌ی `example.com/serving` آن را امضا کند. باید یک `signerName` مشخص درخواست شود. برای اطلاعات بیشتر، مستندات [نام‌های امضاکننده‌ی پشتیبانی‌شده](/docs/reference/access-authn-authz/certificate-signing-requests/#signers) را ببینید.

اکنون CSR باید در API با وضعیت Pending قابل مشاهده باشد. می‌توانید با اجرای دستور زیر آن را ببینید:

```shell
kubectl describe csr my-svc.my-namespace
```

```none
Name:                   my-svc.my-namespace
Labels:                 <none>
Annotations:            <none>
CreationTimestamp:      Tue, 01 Feb 2022 11:49:15 -0500
Requesting User:        yourname@example.com
Signer:                 example.com/serving
Status:                 Pending
Subject:
        Common Name:    my-pod.my-namespace.pod.cluster.local
        Serial Number:
Subject Alternative Names:
        DNS Names:      my-pod.my-namespace.pod.cluster.local
                        my-svc.my-namespace.svc.cluster.local
        IP Addresses:   192.0.2.24
                        10.0.34.2
Events: <none>
```

## گرفتن تأیید برای CertificateSigningRequest {#get-the-certificate-signing-request-approved}

تأیید [درخواست امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/) یا با یک فرایند تأیید خودکار انجام می‌شود یا به‌صورت موردی توسط مدیر کلاستر. اگر مجاز به تأیید درخواست گواهی هستید، می‌توانید این کار را به‌صورت دستی با `kubectl` انجام دهید؛ برای مثال:

```shell
kubectl certificate approve my-svc.my-namespace
```

```none
certificatesigningrequest.certificates.k8s.io/my-svc.my-namespace approved
```

اکنون باید خروجی زیر را ببینید:

```shell
kubectl get csr
```

```none
NAME                  AGE   SIGNERNAME            REQUESTOR              REQUESTEDDURATION   CONDITION
my-svc.my-namespace   10m   example.com/serving   yourname@example.com   <none>              Approved
```

این یعنی درخواست گواهی تأیید شده است و منتظر است تا امضاکننده‌ی درخواست‌شده آن را امضا کند.

## امضای CertificateSigningRequest {#sign-the-certificate-signing-request}

در ادامه، نقش یک امضاکننده‌ی گواهی را بازی می‌کنید، گواهی را صادر می‌کنید و آن را در API بارگذاری می‌کنید.

یک امضاکننده معمولاً API ‏CertificateSigningRequest را برای یافتن آبجکت‌هایی با `signerName` خودش زیر نظر می‌گیرد، بررسی می‌کند که آن‌ها تأیید شده باشند، برای آن درخواست‌ها گواهی امضا می‌کند و وضعیت آبجکت API را با گواهی صادرشده به‌روزرسانی می‌کند.

### ایجاد مرجع صدور گواهی

برای ارائه‌ی امضای دیجیتال روی گواهی جدید، به یک مرجع صدور گواهی نیاز دارید.

ابتدا با اجرای دستور زیر یک گواهی امضا ایجاد کنید:

```shell
cat <<EOF | cfssl gencert -initca - | cfssljson -bare ca
{
  "CN": "My Example Signer",
  "key": {
    "algo": "rsa",
    "size": 2048
  }
}
EOF
```

باید خروجی‌ای مشابه زیر ببینید:

```none
2022/02/01 11:50:39 [INFO] generating a new CA key and certificate from CSR
2022/02/01 11:50:39 [INFO] generate received request
2022/02/01 11:50:39 [INFO] received CSR
2022/02/01 11:50:39 [INFO] generating key: rsa-2048
2022/02/01 11:50:39 [INFO] encoded CSR
2022/02/01 11:50:39 [INFO] signed certificate with serial number 263983151013686720899716354349605500797834580472
```

این دستور یک فایل کلید مرجع صدور گواهی (`ca-key.pem`) و یک گواهی (`ca.pem`) تولید می‌کند.

### صدور گواهی

{{% code_sample file="tls/server-signing-config.json" %}}

با استفاده از پیکربندی امضای `server-signing-config.json` و همچنین فایل کلید و گواهی مرجع صدور گواهی، درخواست گواهی را امضا کنید:

```shell
kubectl get csr my-svc.my-namespace -o jsonpath='{.spec.request}' | \
  base64 --decode | \
  cfssl sign -ca ca.pem -ca-key ca-key.pem -config server-signing-config.json - | \
  cfssljson -bare ca-signed-server
```

باید خروجی‌ای مشابه زیر ببینید:

```
2022/02/01 11:52:26 [INFO] signed certificate with serial number 576048928624926584381415936700914530534472870337
```

این دستور یک فایل گواهی سرویس‌دهی امضاشده با نام `ca-signed-server.pem` تولید می‌کند.

### بارگذاری گواهی امضاشده

در پایان، گواهی امضاشده را در وضعیت آبجکت API قرار دهید:

```shell
kubectl get csr my-svc.my-namespace -o json | \
  jq '.status.certificate = "'$(base64 ca-signed-server.pem | tr -d '\n')'"' | \
  kubectl replace --raw /apis/certificates.k8s.io/v1/certificatesigningrequests/my-svc.my-namespace/status -f -
```

{{< note >}}
این دستور از ابزار خط فرمان [`jq`](https://jqlang.github.io/jq/) برای قرار دادن محتوای کدگذاری‌شده با base64 در فیلد `.status.certificate` استفاده می‌کند.
اگر `jq` را ندارید، می‌توانید خروجی JSON را در یک فایل ذخیره کنید، این فیلد را به‌صورت دستی پر کنید و فایل حاصل را بارگذاری کنید.
{{< /note >}}

پس از تأیید CSR و بارگذاری گواهی امضاشده، دستور زیر را اجرا کنید:

```shell
kubectl get csr
```

خروجی مشابه زیر است:
```none
NAME                  AGE   SIGNERNAME            REQUESTOR              REQUESTEDDURATION   CONDITION
my-svc.my-namespace   20m   example.com/serving   yourname@example.com   <none>              Approved,Issued
```

## دانلود گواهی و استفاده از آن

اکنون، به‌عنوان کاربر درخواست‌دهنده، می‌توانید با اجرای دستور زیر گواهی صادرشده را دانلود کنید و در فایل `server.crt` ذخیره کنید:

```shell
kubectl get csr my-svc.my-namespace -o jsonpath='{.status.certificate}' \
    | base64 --decode > server.crt
```

اکنون می‌توانید `server.crt` و `server-key.pem` را در یک
{{< glossary_tooltip text="Secret" term_id="secret" >}}
قرار دهید تا بعداً آن را در یک Pod مانت کنید (برای مثال، برای استفاده در یک وب‌سرور که HTTPS ارائه می‌دهد).

```shell
kubectl create secret tls server --cert server.crt --key server-key.pem
```

```none
secret/server created
```

در پایان، می‌توانید `ca.pem` را در یک {{< glossary_tooltip text="ConfigMap" term_id="configmap" >}}
ذخیره کنید و از آن به‌عنوان ریشه‌ی اعتماد برای تأیید گواهی سرویس‌دهی استفاده کنید:

```shell
kubectl create configmap example-serving-ca --from-file ca.crt=ca.pem
```

```none
configmap/example-serving-ca created
```

## تأیید CertificateSigningRequestها {#approving-certificate-signing-requests}

مدیر کوبرنتیز (با مجوزهای مناسب) می‌تواند با دستورهای `kubectl certificate
approve` و `kubectl certificate deny`، CertificateSigningRequestها را به‌صورت دستی تأیید (یا رد) کند. با این حال، اگر قصد دارید از این API به‌طور گسترده استفاده کنید، بهتر است نوشتن یک کنترل‌کننده‌ی خودکار گواهی را در نظر بگیرید.

{{< caution >}}
توانایی تأیید CSRها تعیین می‌کند چه کسی در محیط شما به چه کسی اعتماد کند. این توانایی نباید به‌صورت گسترده یا بی‌ملاحظه اعطا شود.

پیش از اعطای مجوز `approve`، باید مطمئن شوید که هم الزامات تأییدی را که بر عهده‌ی تأییدکننده است **و** هم پیامدهای صدور یک گواهی مشخص را با اطمینان درک می‌کنید.
{{< /caution >}}

چه تأییدکننده یک ماشین باشد و چه انسانی که مانند مثال بالا از kubectl استفاده می‌کند، نقش _تأییدکننده_ این است که بررسی کند CSR دو شرط را برآورده می‌کند:

1. موجودیت درخواست‌کننده‌ی (subject) CSR کلید خصوصی‌ای را که برای امضای CSR استفاده شده است در اختیار دارد. این شرط با تهدید جعل هویت یک موجودیت مجاز توسط شخص ثالث مقابله می‌کند. در مثال بالا، این مرحله یعنی بررسی اینکه پاد کلید خصوصی‌ای را که برای تولید CSR استفاده شده در اختیار دارد.
2. موجودیت درخواست‌کننده‌ی CSR مجاز است در زمینه‌ی درخواست‌شده عمل کند. این شرط با تهدید پیوستن یک موجودیت ناخواسته به کلاستر مقابله می‌کند. در مثال بالا، این مرحله یعنی بررسی اینکه پاد اجازه‌ی مشارکت در سرویس درخواست‌شده را دارد.

تأییدکننده باید CSR را فقط و فقط در صورتی تأیید کند که این دو شرط برآورده شده باشند و در غیر این صورت باید آن را رد کند.

برای اطلاعات بیشتر درباره‌ی تأیید گواهی و کنترل دسترسی، صفحه‌ی مرجع
[درخواست‌های امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/)
را بخوانید.

## پیکربندی کلاستر برای ارائه‌ی امضا

این صفحه فرض می‌کند که یک امضاکننده برای سرویس‌دهی به API گواهی‌ها راه‌اندازی شده است. کنترل‌کننده‌ی مدیریت (controller manager) کوبرنتیز یک پیاده‌سازی پیش‌فرض از امضاکننده ارائه می‌دهد. برای فعال‌سازی آن، پارامترهای `--cluster-signing-cert-file` و `--cluster-signing-key-file` را همراه با مسیرهای جفت‌کلید مرجع صدور گواهی خود به controller manager بدهید.
