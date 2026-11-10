---
title: گواهی‌ها و الزامات PKI
reviewers:
- sig-cluster-lifecycle
content_type: concept
weight: 50
---

<!-- overview -->

کوبرنتیز برای احراز هویت روی TLS به گواهی‌های PKI نیاز دارد.
اگر کوبرنتیز را با [kubeadm](/docs/reference/setup-tools/kubeadm/) نصب کنید، گواهی‌هایی که کلاستر شما به آن‌ها نیاز دارد به‌طور خودکار ایجاد می‌شوند.
همچنین می‌توانید گواهی‌های خودتان را ایجاد کنید؛ برای مثال، تا با ذخیره نکردن کلیدهای خصوصی روی سرور API امنیت آن‌ها را بیشتر کنید.
این صفحه گواهی‌هایی را که کلاستر شما به آن‌ها نیاز دارد توضیح می‌دهد.

<!-- body -->

## کلاستر شما چگونه از گواهی‌ها استفاده می‌کند

کوبرنتیز برای عملیات زیر به PKI نیاز دارد:

### گواهی‌های سرور

* گواهی سرور برای نقطهٔ پایانی (endpoint) سرور API
* گواهی سرور برای سرور etcd
* [گواهی‌های سرور](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#client-and-serving-certificates)
  برای هر kubelet (روی هر {{< glossary_tooltip text="نود" term_id="node" >}} یک kubelet اجرا می‌شود)
* گواهی سرور اختیاری برای [پراکسی جلویی (front-proxy)](/docs/tasks/extend-kubernetes/configure-aggregation-layer/)

### گواهی‌های کلاینت

* گواهی‌های کلاینت برای هر kubelet، که برای احراز هویت در سرور API به‌عنوان کلاینت API کوبرنتیز استفاده می‌شوند
* گواهی کلاینت برای هر سرور API، که برای احراز هویت در etcd استفاده می‌شود
* گواهی کلاینت برای مدیر کنترل‌کننده‌ها (controller manager) تا به‌صورت امن با سرور API ارتباط برقرار کند
* گواهی کلاینت برای زمان‌بند تا به‌صورت امن با سرور API ارتباط برقرار کند
* گواهی‌های کلاینت، یکی برای هر نود، تا kube-proxy بتواند در سرور API احراز هویت شود
* گواهی‌های کلاینت اختیاری برای مدیران کلاستر تا در سرور API احراز هویت شوند
* گواهی کلاینت اختیاری برای [پراکسی جلویی](/docs/tasks/extend-kubernetes/configure-aggregation-layer/)

### گواهی‌های سرور و کلاینت kubelet

سرور API برای برقراری اتصال امن با kubelet و احراز هویت خود نزد آن، به یک جفت گواهی و کلید کلاینت نیاز دارد.

در این سناریو، دو رویکرد برای استفاده از گواهی وجود دارد:

* گواهی‌های مشترک: kube-apiserver می‌تواند از همان جفت گواهی و کلیدی استفاده کند که برای احراز هویت کلاینت‌های خود به کار می‌برد. یعنی گواهی‌های موجود، مانند `apiserver.crt` و `apiserver.key`، را می‌توان برای ارتباط با سرورهای kubelet استفاده کرد.

* گواهی‌های جداگانه: به‌عنوان راه دیگر، kube-apiserver می‌تواند یک جفت گواهی و کلید کلاینت جدید برای احراز هویت ارتباط خود با سرورهای kubelet ایجاد کند. در این حالت، یک گواهی مجزا با نام `kubelet-client.crt` و کلید خصوصی متناظر آن، `kubelet-client.key`، ایجاد می‌شوند.

{{< note >}}
گواهی‌های `front-proxy` فقط زمانی لازم هستند که از لایهٔ تجمیع (aggregation layer) سرور API برای پشتیبانی از [یک سرور API افزونه](/docs/tasks/extend-kubernetes/setup-extension-api-server/) استفاده کنید.
{{< /note >}}

سرور etcd نیز برای احراز هویت کلاینت‌ها و همتایان (peers) خود از TLS دوطرفه (mutual TLS) استفاده می‌کند.

## محل ذخیرهٔ گواهی‌ها

اگر کوبرنتیز را با kubeadm نصب کنید، بیشتر گواهی‌ها در `/etc/kubernetes/pki` ذخیره می‌شوند.
همهٔ مسیرهای این مستند نسبت به همین دایرکتوری هستند؛ به‌جز گواهی‌های حساب‌های کاربری که kubeadm آن‌ها را در `/etc/kubernetes` قرار می‌دهد.

## پیکربندی دستی گواهی‌ها

اگر نمی‌خواهید kubeadm گواهی‌های لازم را ایجاد کند، می‌توانید آن‌ها را با استفاده از یک CA ریشهٔ واحد یا با فراهم کردن همهٔ گواهی‌ها ایجاد کنید. برای جزئیات ایجاد مرجع صدور گواهی (certificate authority) خودتان، [گواهی‌ها](/docs/tasks/administer-cluster/certificates/) را ببینید. برای اطلاعات بیشتر دربارهٔ مدیریت گواهی‌ها، [مدیریت گواهی‌ها با kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/) را ببینید.

### یک CA ریشهٔ واحد

می‌توانید یک CA ریشهٔ واحد ایجاد کنید که در اختیار یک مدیر است. سپس این CA ریشه می‌تواند چند CA میانی ایجاد کند و ایجاد بقیهٔ گواهی‌ها را به خود کوبرنتیز واگذار کند.

CAهای لازم:

| مسیر                   | CN پیش‌فرض                | توضیحات                      |
|------------------------|---------------------------|----------------------------------|
| ca.crt,key             | kubernetes-ca             | CA عمومی کوبرنتیز            |
| etcd/ca.crt,key        | etcd-ca                   | برای همهٔ کارکردهای مربوط به etcd   |
| front-proxy-ca.crt,key | kubernetes-front-proxy-ca | برای [پراکسی جلویی](/docs/tasks/extend-kubernetes/configure-aggregation-layer/) |

علاوه بر CAهای بالا، برای مدیریت حساب‌های سرویس (service account) نیز به یک جفت کلید عمومی/خصوصی، یعنی `sa.key` و `sa.pub`، نیاز است.
مثال زیر فایل‌های کلید و گواهی CA را که در جدول قبل آمده‌اند نشان می‌دهد:

```
/etc/kubernetes/pki/ca.crt
/etc/kubernetes/pki/ca.key
/etc/kubernetes/pki/etcd/ca.crt
/etc/kubernetes/pki/etcd/ca.key
/etc/kubernetes/pki/front-proxy-ca.crt
/etc/kubernetes/pki/front-proxy-ca.key
```

### همهٔ گواهی‌ها

اگر نمی‌خواهید کلیدهای خصوصی CA را در کلاستر خود کپی کنید، می‌توانید همهٔ گواهی‌ها را خودتان ایجاد کنید.

گواهی‌های لازم:

| CN پیش‌فرض                    | CA والد                 | O (در Subject) | نوع (kind)             | میزبان‌ها (SAN)                                         |
|-------------------------------|---------------------------|----------------|------------------|-----------------------------------------------------|
| kube-etcd                     | etcd-ca                   |                | server, client   | `<hostname>`, `<Host_IP>`, `localhost`, `127.0.0.1` |
| kube-etcd-peer                | etcd-ca                   |                | server, client   | `<hostname>`, `<Host_IP>`, `localhost`, `127.0.0.1` |
| kube-etcd-healthcheck-client  | etcd-ca                   |                | client           |                                                     |
| kube-apiserver-etcd-client    | etcd-ca                   |                | client           |                                                     |
| kube-apiserver                | kubernetes-ca             |                | server           | `<hostname>`, `<Host_IP>`, `<advertise_IP>`[^1]     |
| kube-apiserver-kubelet-client | kubernetes-ca             | system:masters | client           |                                                     |
| front-proxy-client            | kubernetes-front-proxy-ca |                | client           |                                                     |

{{< note >}}
به‌جای استفاده از گروه ابرکاربر `system:masters` برای `kube-apiserver-kubelet-client`، می‌توان از گروهی با دسترسی کمتر استفاده کرد. ابزار kubeadm برای این منظور از گروه `kubeadm:cluster-admins` استفاده می‌کند.
{{< /note >}}

[^1]: هر IP یا نام DNS دیگری که از طریق آن با کلاستر خود ارتباط برقرار می‌کنید (همان‌طور که [kubeadm](/docs/reference/setup-tools/kubeadm/) استفاده می‌کند: IP پایدار و/یا نام DNS متعادل‌کنندهٔ بار، `kubernetes`، `kubernetes.default`، `kubernetes.default.svc`، `kubernetes.default.svc.cluster`، `kubernetes.default.svc.cluster.local`)

که در آن `kind` به یک یا چند مورد از کاربردهای کلید x509 نگاشت می‌شود؛ این کاربردها در `.spec.usages` نوع [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1#CertificateSigningRequest) نیز مستند شده‌اند:

| نوع (kind)   | کاربرد کلید                                                                       |
|--------|---------------------------------------------------------------------------------|
| server | digital signature, key encipherment, server auth                                |
| client | digital signature, key encipherment, client auth                                |

{{< note >}}
میزبان‌ها/SANهای فهرست‌شده در بالا، موارد توصیه‌شده برای داشتن یک کلاستر کارا هستند؛ اگر یک راه‌اندازی خاص نیاز داشته باشد، می‌توان SANهای بیشتری را به همهٔ گواهی‌های سرور افزود.
{{< /note >}}

{{< note >}}
فقط برای کاربران kubeadm:

* در مستندات kubeadm، سناریویی که در آن گواهی‌های CA را بدون کلیدهای خصوصی در کلاستر خود کپی می‌کنید، CA خارجی نامیده می‌شود.
* اگر فهرست بالا را با PKI ایجادشده توسط kubeadm مقایسه می‌کنید، توجه کنید که در صورت استفاده از etcd خارجی، گواهی‌های `kube-etcd`، `kube-etcd-peer` و `kube-etcd-healthcheck-client` ایجاد نمی‌شوند.

{{< /note >}}

### مسیرهای گواهی‌ها

گواهی‌ها باید در مسیر توصیه‌شده قرار بگیرند (همان‌طور که [kubeadm](/docs/reference/setup-tools/kubeadm/) استفاده می‌کند).
صرف‌نظر از محل قرارگیری، مسیرها باید با استفاده از آرگومان مشخص‌شده تعیین شوند.

| CN پیش‌فرض | مسیر توصیه‌شدهٔ کلید | مسیر توصیه‌شدهٔ گواهی | دستور | آرگومان کلید | آرگومان گواهی |
| --------- | ------------------ | ------------------- | ------- | ----------- | ------------ |
| etcd-ca | etcd/ca.key | etcd/ca.crt | kube-apiserver | | --etcd-cafile |
| kube-apiserver-etcd-client | apiserver-etcd-client.key | apiserver-etcd-client.crt | kube-apiserver | --etcd-keyfile | --etcd-certfile |
| kubernetes-ca | ca.key | ca.crt | kube-apiserver | | --client-ca-file |
| kubernetes-ca | ca.key | ca.crt | kube-controller-manager | --cluster-signing-key-file | --client-ca-file,--root-ca-file,--cluster-signing-cert-file |
| kube-apiserver | apiserver.key | apiserver.crt| kube-apiserver | --tls-private-key-file | --tls-cert-file |
| kube-apiserver-kubelet-client | apiserver-kubelet-client.key | apiserver-kubelet-client.crt | kube-apiserver | --kubelet-client-key | --kubelet-client-certificate |
| front-proxy-ca | front-proxy-ca.key | front-proxy-ca.crt | kube-apiserver | | --requestheader-client-ca-file |
| front-proxy-ca | front-proxy-ca.key | front-proxy-ca.crt | kube-controller-manager | | --requestheader-client-ca-file |
| front-proxy-client | front-proxy-client.key | front-proxy-client.crt | kube-apiserver | --proxy-client-key-file | --proxy-client-cert-file |
| etcd-ca | etcd/ca.key | etcd/ca.crt | etcd | | --trusted-ca-file,--peer-trusted-ca-file |
| kube-etcd | etcd/server.key | etcd/server.crt | etcd | --key-file | --cert-file |
| kube-etcd-peer | etcd/peer.key | etcd/peer.crt | etcd | --peer-key-file | --peer-cert-file |
| etcd-ca| | etcd/ca.crt | etcdctl | | --cacert |
| kube-etcd-healthcheck-client | etcd/healthcheck-client.key | etcd/healthcheck-client.crt | etcdctl | --key | --cert |

همین ملاحظات برای جفت کلید حساب سرویس نیز صدق می‌کند:

| مسیر کلید خصوصی  | مسیر کلید عمومی  | دستور                 | آرگومان                             |
|-------------------|------------------|-------------------------|--------------------------------------|
|  sa.key           |                  | kube-controller-manager | --service-account-private-key-file   |
|                   | sa.pub           | kube-apiserver          | --service-account-key-file           |

مثال زیر مسیرهای فایل [از جدول‌های قبل](#certificate-paths) را نشان می‌دهد که اگر همهٔ کلیدها و گواهی‌ها را خودتان ایجاد می‌کنید، باید آن‌ها را فراهم کنید:

```
/etc/kubernetes/pki/etcd/ca.key
/etc/kubernetes/pki/etcd/ca.crt
/etc/kubernetes/pki/apiserver-etcd-client.key
/etc/kubernetes/pki/apiserver-etcd-client.crt
/etc/kubernetes/pki/ca.key
/etc/kubernetes/pki/ca.crt
/etc/kubernetes/pki/apiserver.key
/etc/kubernetes/pki/apiserver.crt
/etc/kubernetes/pki/apiserver-kubelet-client.key
/etc/kubernetes/pki/apiserver-kubelet-client.crt
/etc/kubernetes/pki/front-proxy-ca.key
/etc/kubernetes/pki/front-proxy-ca.crt
/etc/kubernetes/pki/front-proxy-client.key
/etc/kubernetes/pki/front-proxy-client.crt
/etc/kubernetes/pki/etcd/server.key
/etc/kubernetes/pki/etcd/server.crt
/etc/kubernetes/pki/etcd/peer.key
/etc/kubernetes/pki/etcd/peer.crt
/etc/kubernetes/pki/etcd/healthcheck-client.key
/etc/kubernetes/pki/etcd/healthcheck-client.crt
/etc/kubernetes/pki/sa.key
/etc/kubernetes/pki/sa.pub
```

## پیکربندی گواهی‌ها برای حساب‌های کاربری

این حساب‌های مدیر و حساب‌های سرویس را باید به‌صورت دستی پیکربندی کنید:

| نام فایل                | نام اعتبارنامه            | CN پیش‌فرض                          | O (در Subject)         |
|-------------------------|----------------------------|-------------------------------------|------------------------|
| admin.conf              | default-admin              | kubernetes-admin                    | `<admin-group>`        |
| super-admin.conf        | default-super-admin        | kubernetes-super-admin              | system:masters         |
| kubelet.conf            | default-auth               | system:node:`<nodeName>` (یادداشت را ببینید) | system:nodes           |
| controller-manager.conf | default-controller-manager | system:kube-controller-manager      |                        |
| scheduler.conf          | default-scheduler          | system:kube-scheduler               |                        |

{{< note >}}
مقدار `<nodeName>` برای `kubelet.conf` **باید** دقیقاً با مقدار نام نودی که kubelet هنگام ثبت در apiserver ارائه می‌کند مطابقت داشته باشد. برای جزئیات بیشتر، [مجوزدهی نود](/docs/reference/access-authn-authz/node/) را بخوانید.
{{< /note >}}

{{< note >}}
در مثال بالا، مقدار `<admin-group>` به پیاده‌سازی بستگی دارد. برخی ابزارها گواهی موجود در `admin.conf` پیش‌فرض را طوری امضا می‌کنند که عضو گروه `system:masters` باشد.
گروه `system:masters` یک گروه ابرکاربر اضطراری (break-glass) است که می‌تواند لایهٔ مجوزدهی کوبرنتیز، مانند RBAC، را دور بزند. همچنین برخی ابزارها فایل `super-admin.conf` جداگانه‌ای با گواهی متصل به این گروه ابرکاربر ایجاد نمی‌کنند.

ابزار kubeadm دو گواهی مدیر جداگانه در فایل‌های kubeconfig ایجاد می‌کند.
یکی در `admin.conf` قرار دارد و دارای `Subject: O = kubeadm:cluster-admins, CN = kubernetes-admin` است.
گروه `kubeadm:cluster-admins` یک گروه سفارشی است که به ClusterRole با نام `cluster-admin` متصل شده است.
این فایل روی همهٔ ماشین‌های control plane که kubeadm مدیریت می‌کند ایجاد می‌شود.

دیگری در `super-admin.conf` قرار دارد و دارای `Subject: O = system:masters, CN = kubernetes-super-admin` است.
این فایل فقط روی نودی ایجاد می‌شود که دستور `kubeadm init` روی آن اجرا شده است.
{{< /note >}}

1. برای هر پیکربندی، یک جفت گواهی/کلید x509 با نام مشترک (CN) و سازمان (O) مشخص‌شده ایجاد کنید.

1. برای هر پیکربندی، `kubectl` را به شکل زیر اجرا کنید:

   ```
   KUBECONFIG=<filename> kubectl config set-cluster default-cluster --server=https://<host ip>:6443 --certificate-authority <path-to-kubernetes-ca> --embed-certs
   KUBECONFIG=<filename> kubectl config set-credentials <credential-name> --client-key <path-to-key>.pem --client-certificate <path-to-cert>.pem --embed-certs
   KUBECONFIG=<filename> kubectl config set-context default-system --cluster default-cluster --user <credential-name>
   KUBECONFIG=<filename> kubectl config use-context default-system
   ```

این فایل‌ها به این صورت استفاده می‌شوند:

| نام فایل                | دستور                 | توضیح                                                               |
|-------------------------|-------------------------|-----------------------------------------------------------------------|
| admin.conf              | kubectl                 | کاربر مدیر کلاستر را پیکربندی می‌کند                         |
| super-admin.conf        | kubectl                 | کاربر ابرمدیر کلاستر را پیکربندی می‌کند                   |
| kubelet.conf            | kubelet                 | برای هر نود در کلاستر یکی لازم است.                            |
| controller-manager.conf | kube-controller-manager | باید به مانیفست در `manifests/kube-controller-manager.yaml` افزوده شود |
| scheduler.conf          | kube-scheduler          | باید به مانیفست در `manifests/kube-scheduler.yaml` افزوده شود          |

فهرست زیر مسیر کامل فایل‌های آمده در جدول قبل را نشان می‌دهد:

```
/etc/kubernetes/admin.conf
/etc/kubernetes/super-admin.conf
/etc/kubernetes/kubelet.conf
/etc/kubernetes/controller-manager.conf
/etc/kubernetes/scheduler.conf
```
