---
title: تولید دستی گواهی‌ها
content_type: task
weight: 30
---

<!-- overview -->

هنگام استفاده از احراز هویت با گواهی کلاینت (client certificate authentication)، می‌توانید گواهی‌ها را
به‌صورت دستی با ابزارهای [`easyrsa`](https://github.com/OpenVPN/easy-rsa)، [`openssl`](https://github.com/openssl/openssl) یا [`cfssl`](https://github.com/cloudflare/cfssl) تولید کنید.

<!-- body -->

### easyrsa

با ابزار **easyrsa** می‌توانید گواهی‌های کلاستر خود را به‌صورت دستی تولید کنید.

1. نسخهٔ وصله‌شدهٔ `easyrsa3` را دانلود کنید، از حالت فشرده خارج کنید و راه‌اندازی اولیه کنید.

   ```shell
   curl -LO https://dl.k8s.io/easy-rsa/easy-rsa.tar.gz
   tar xzf easy-rsa.tar.gz
   cd easy-rsa-master/easyrsa3
   ./easyrsa init-pki
   ```
1. یک مرجع صدور گواهی (CA) جدید بسازید. گزینهٔ `--batch` حالت خودکار را فعال می‌کند و
   گزینهٔ `--req-cn` نام مشترک (Common Name یا CN) را برای گواهی ریشهٔ جدید CA مشخص می‌کند.

   ```shell
   ./easyrsa --batch "--req-cn=${MASTER_IP}@`date +%s`" build-ca nopass
   ```

1. گواهی و کلید سرور را تولید کنید.

   آرگومان `--subject-alt-name` نشانی‌های IP و نام‌های DNS ممکنی را تعیین می‌کند که از طریق آن‌ها
   به API server دسترسی پیدا می‌شود. مقدار `MASTER_CLUSTER_IP` معمولاً نخستین IP از محدودهٔ CIDR سرویس‌هاست
   که به‌عنوان آرگومان `--service-cluster-ip-range` هم برای API server و هم برای مؤلفهٔ
   controller manager مشخص می‌شود. آرگومان `--days` تعداد روزهایی را تعیین می‌کند
   که پس از آن گواهی منقضی می‌شود.
   همچنین نمونهٔ زیر فرض می‌کند که از `cluster.local` به‌عنوان نام دامنهٔ پیش‌فرض
   DNS استفاده می‌کنید.

   ```shell
   ./easyrsa --subject-alt-name="IP:${MASTER_IP},"\
   "IP:${MASTER_CLUSTER_IP},"\
   "DNS:kubernetes,"\
   "DNS:kubernetes.default,"\
   "DNS:kubernetes.default.svc,"\
   "DNS:kubernetes.default.svc.cluster,"\
   "DNS:kubernetes.default.svc.cluster.local" \
   --days=10000 \
   build-server-full server nopass
   ```

1. فایل‌های `pki/ca.crt`، `pki/issued/server.crt` و `pki/private/server.key` را در دایرکتوری خود کپی کنید.

1. پارامترهای زیر را تکمیل کنید و به پارامترهای راه‌اندازی API server اضافه کنید:

   ```shell
   --client-ca-file=/yourdirectory/ca.crt
   --tls-cert-file=/yourdirectory/server.crt
   --tls-private-key-file=/yourdirectory/server.key
   ```

### openssl

با ابزار **openssl** می‌توانید گواهی‌های کلاستر خود را به‌صورت دستی تولید کنید.

1. یک فایل ca.key با طول ۲۰۴۸ بیت تولید کنید:

   ```shell
   openssl genrsa -out ca.key 2048
   ```

1. بر اساس فایل ca.key، یک فایل ca.crt تولید کنید (با گزینهٔ `-days` مدت اعتبار گواهی را تعیین کنید):

   ```shell
   openssl req -x509 -new -noenc -key ca.key -subj "/CN=${MASTER_IP}" -days 10000 -out ca.crt
   ```

1. یک فایل server.key با طول ۲۰۴۸ بیت تولید کنید:

   ```shell
   openssl genrsa -out server.key 2048
   ```

1. یک فایل پیکربندی برای تولید درخواست امضای گواهی (Certificate Signing Request یا CSR) بسازید.

   پیش از ذخیرهٔ این محتوا در یک فایل (مثلاً `csr.conf`)، حتماً مقادیری را که درون
   براکت‌های زاویه‌دار مشخص شده‌اند (مانند `<MASTER_IP>`) با مقادیر واقعی جایگزین کنید.
   توجه کنید که مقدار `MASTER_CLUSTER_IP` همان IP سرویس کلاستر برای
   API server است که در زیربخش قبلی توضیح داده شد.
   همچنین نمونهٔ زیر فرض می‌کند که از `cluster.local` به‌عنوان نام دامنهٔ پیش‌فرض
   DNS استفاده می‌کنید.

   ```ini
   [ req ]
   default_bits = 2048
   prompt = no
   default_md = sha256
   req_extensions = req_ext
   distinguished_name = dn

   [ dn ]
   C = <country>
   ST = <state>
   L = <city>
   O = <organization>
   OU = <organization unit>
   CN = <MASTER_IP>

   [ req_ext ]
   subjectAltName = @alt_names

   [ alt_names ]
   DNS.1 = kubernetes
   DNS.2 = kubernetes.default
   DNS.3 = kubernetes.default.svc
   DNS.4 = kubernetes.default.svc.cluster
   DNS.5 = kubernetes.default.svc.cluster.local
   IP.1 = <MASTER_IP>
   IP.2 = <MASTER_CLUSTER_IP>

   [ v3_ext ]
   authorityKeyIdentifier=keyid,issuer:always
   basicConstraints=CA:FALSE
   keyUsage=keyEncipherment,dataEncipherment
   extendedKeyUsage=serverAuth,clientAuth
   subjectAltName=@alt_names
   ```

1. درخواست امضای گواهی را بر اساس فایل پیکربندی تولید کنید:

   ```shell
   openssl req -new -key server.key -out server.csr -config csr.conf
   ```

1. گواهی سرور را با استفاده از فایل‌های ca.key، ca.crt و server.csr تولید کنید:

   ```shell
   openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
       -CAcreateserial -out server.crt -days 10000 \
       -extensions v3_ext -extfile csr.conf -sha256
   ```

1. درخواست امضای گواهی را مشاهده کنید:

   ```shell
   openssl req  -noout -text -in ./server.csr
   ```

1. گواهی را مشاهده کنید:

   ```shell
   openssl x509  -noout -text -in ./server.crt
   ```

1. پارامترهای زیر را تکمیل کنید و به پارامترهای راه‌اندازی API server اضافه کنید:

   ```shell
   --client-ca-file=/yourdirectory/ca.crt
   --tls-cert-file=/yourdirectory/server.crt
   --tls-private-key-file=/yourdirectory/server.key
   ```

### cfssl

ابزار **cfssl** ابزار دیگری برای تولید گواهی است.

1. ابزارهای خط فرمان را مطابق دستورهای زیر دانلود کنید، از حالت فشرده خارج کنید و آماده کنید.

   توجه کنید که ممکن است لازم باشد دستورهای نمونه را بر اساس معماری سخت‌افزاری
   و نسخهٔ cfssl مورد استفادهٔ خود تغییر دهید.

   ```shell
   curl -L https://github.com/cloudflare/cfssl/releases/download/v1.5.0/cfssl_1.5.0_linux_amd64 -o cfssl
   chmod +x cfssl
   curl -L https://github.com/cloudflare/cfssl/releases/download/v1.5.0/cfssljson_1.5.0_linux_amd64 -o cfssljson
   chmod +x cfssljson
   curl -L https://github.com/cloudflare/cfssl/releases/download/v1.5.0/cfssl-certinfo_1.5.0_linux_amd64 -o cfssl-certinfo
   chmod +x cfssl-certinfo
   ```

1. یک دایرکتوری برای نگهداری فایل‌های خروجی بسازید و cfssl را راه‌اندازی اولیه کنید:

   ```shell
   mkdir cert
   cd cert
   ../cfssl print-defaults config > config.json
   ../cfssl print-defaults csr > csr.json
   ```

1. یک فایل پیکربندی JSON برای تولید فایل CA بسازید، برای نمونه `ca-config.json`:

   ```json
   {
     "signing": {
       "default": {
         "expiry": "8760h"
       },
       "profiles": {
         "kubernetes": {
           "usages": [
             "signing",
             "key encipherment",
             "server auth",
             "client auth"
           ],
           "expiry": "8760h"
         }
       }
     }
   }
   ```

1. یک فایل پیکربندی JSON برای درخواست امضای گواهی (CSR) مربوط به CA بسازید، برای نمونه
   `ca-csr.json`. حتماً مقادیری را که درون براکت‌های زاویه‌دار مشخص شده‌اند با
   مقادیر واقعی موردنظر خود جایگزین کنید.

   ```json
   {
     "CN": "kubernetes",
     "key": {
       "algo": "rsa",
       "size": 2048
     },
     "names":[{
       "C": "<country>",
       "ST": "<state>",
       "L": "<city>",
       "O": "<organization>",
       "OU": "<organization unit>"
     }]
   }
   ```

1. کلید CA (`ca-key.pem`) و گواهی آن (`ca.pem`) را تولید کنید:

   ```shell
   ../cfssl gencert -initca ca-csr.json | ../cfssljson -bare ca
   ```

1. یک فایل پیکربندی JSON برای تولید کلیدها و گواهی‌های API server بسازید،
   برای نمونه `server-csr.json`. حتماً مقادیر درون براکت‌های زاویه‌دار را با
   مقادیر واقعی موردنظر خود جایگزین کنید. مقدار `<MASTER_CLUSTER_IP>` همان IP سرویس کلاستر
   برای API server است که در زیربخش قبلی توضیح داده شد.
   همچنین نمونهٔ زیر فرض می‌کند که از `cluster.local` به‌عنوان نام دامنهٔ پیش‌فرض
   DNS استفاده می‌کنید.

   ```json
   {
     "CN": "kubernetes",
     "hosts": [
       "127.0.0.1",
       "<MASTER_IP>",
       "<MASTER_CLUSTER_IP>",
       "kubernetes",
       "kubernetes.default",
       "kubernetes.default.svc",
       "kubernetes.default.svc.cluster",
       "kubernetes.default.svc.cluster.local"
     ],
     "key": {
       "algo": "rsa",
       "size": 2048
     },
     "names": [{
       "C": "<country>",
       "ST": "<state>",
       "L": "<city>",
       "O": "<organization>",
       "OU": "<organization unit>"
     }]
   }
   ```

1. کلید و گواهی API server را تولید کنید. این دو به‌طور پیش‌فرض به ترتیب
   در فایل‌های `server-key.pem` و `server.pem` ذخیره می‌شوند:

   ```shell
   ../cfssl gencert -ca=ca.pem -ca-key=ca-key.pem \
        --config=ca-config.json -profile=kubernetes \
        server-csr.json | ../cfssljson -bare server
   ```

## توزیع گواهی CA خودامضا

ممکن است یک نود کلاینت، گواهی CA خودامضا (self-signed) را معتبر نشناسد.
در استقرارهای غیرعملیاتی (non-production) یا استقرارهایی که پشت فایروال یک شرکت اجرا می‌شوند،
می‌توانید گواهی CA خودامضا را میان همهٔ کلاینت‌ها توزیع کنید و
فهرست محلی گواهی‌های معتبر را به‌روزرسانی کنید.

روی هر کلاینت، عملیات زیر را انجام دهید:

```shell
sudo cp ca.crt /usr/local/share/ca-certificates/kubernetes.crt
sudo update-ca-certificates
```

```none
Updating certificates in /etc/ssl/certs...
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d....
done.
```

## API گواهی‌ها

می‌توانید از API `certificates.k8s.io` برای تأمین
گواهی‌های x509 جهت احراز هویت استفاده کنید؛ روش این کار در صفحهٔ وظیفهٔ
[مدیریت TLS در یک کلاستر](/docs/tasks/tls/managing-tls-in-a-cluster)
توضیح داده شده است.
