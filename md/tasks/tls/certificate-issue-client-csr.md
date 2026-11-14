---
title: صدور گواهی برای یک کلاینت API کوبرنتیز با استفاده از CertificateSigningRequest
api_metadata:
- apiVersion: "certificates.k8s.io/v1"
  kind: "CertificateSigningRequest"
  override_link_text: "CSR v1"
weight: 80

# Docs maintenance note
#
# If there is a future page /docs/tasks/tls/certificate-issue-client-manually/ then this page
# should link there, and the new page should link back to this one.
---

<!-- overview -->

کوبرنتیز به شما امکان می‌دهد از یک زیرساخت کلید عمومی (PKI) برای احراز هویت در کلاستر خود به‌عنوان یک کلاینت استفاده کنید.

برای اینکه یک کاربر عادی بتواند احراز هویت شود و API را فراخوانی کند، چند گام لازم است. نخست، این کاربر باید گواهی [X.509](https://www.itu.int/rec/T-REC-X.509) داشته باشد که مرجعی مورد اعتماد کلاستر کوبرنتیز شما آن را صادر کرده است. سپس کلاینت باید این گواهی را به API کوبرنتیز ارائه کند.

در این فرایند از یک [CertificateSigningRequest](/docs/reference/access-authn-authz/certificate-signing-requests/) استفاده می‌کنید و شما یا موجودیت مجاز دیگری باید این درخواست را تأیید کنید.


ابتدا یک کلید خصوصی ایجاد می‌کنید، سپس گواهی را صادر می‌کنید و در پایان آن کلید خصوصی را برای یک کلاینت پیکربندی می‌کنید.

## {{% heading "prerequisites" %}}

* {{< include "task-tutorial-prereqs.md" >}}

* به ابزارهای `kubectl`، `openssl` و `base64` نیاز دارید.

این صفحه فرض می‌کند که از {{< glossary_tooltip term_id="rbac" text="کنترل دسترسی مبتنی بر نقش" >}} (RBAC) کوبرنتیز استفاده می‌کنید.
اگر سازوکارهای امنیتی جایگزین یا تکمیلی برای مجوزدهی دارید، باید آن‌ها را نیز در نظر بگیرید.

<!-- steps -->

## ایجاد کلید خصوصی

در این گام یک کلید خصوصی ایجاد می‌کنید. باید این کلید خصوصی را محرمانه نگه دارید؛ هر کسی که به آن دسترسی داشته باشد می‌تواند خود را به جای این کاربر جا بزند.

```shell
# Create a private key
openssl genrsa -out myuser.key 3072
```

## ایجاد درخواست امضای گواهی X.509 {#create-x.509-certificatessigningrequest}

{{< note >}}
این مورد با API هم‌نام CertificateSigningRequest یکسان نیست؛ فایلی که در اینجا تولید می‌کنید درون CertificateSigningRequest قرار می‌گیرد.
{{< /note >}}

تنظیم ویژگی‌های CN و O در CSR اهمیت دارد. مقدار CN نام کاربر و مقدار O گروهی است که این کاربر به آن تعلق خواهد داشت.
برای آشنایی با گروه‌های استاندارد می‌توانید به [RBAC](/docs/reference/access-authn-authz/rbac/) مراجعه کنید.

```shell
# Change the common name "myuser" to the actual username that you want to use
openssl req -new -key myuser.key -out myuser.csr -subj "/CN=myuser"
```

## ایجاد CertificateSigningRequest کوبرنتیز {#create-k8s-certificatessigningrequest}

سند CSR را با این دستور کدگذاری کنید:

```shell
cat myuser.csr | base64 | tr -d "\n"
```

یک [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/) ایجاد کنید و آن را با kubectl به کلاستر کوبرنتیز ارسال کنید. در ادامه قطعه‌ای از اسکریپت شل آمده است که می‌توانید برای تولید CertificateSigningRequest از آن استفاده کنید.

```shell
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: myuser # example
spec:
  # This is an encoded CSR. Change this to the base64-encoded contents of myuser.csr
  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZqQ0NBVDRDQVFBd0VURVBNQTBHQTFVRUF3d0dZVzVuWld4aE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRgpBQU9DQVE4QU1JSUJDZ0tDQVFFQTByczhJTHRHdTYxakx2dHhWTTJSVlRWMDNHWlJTWWw0dWluVWo4RElaWjBOCnR2MUZtRVFSd3VoaUZsOFEzcWl0Qm0wMUFSMkNJVXBGd2ZzSjZ4MXF3ckJzVkhZbGlBNVhwRVpZM3ExcGswSDQKM3Z3aGJlK1o2MVNrVHF5SVBYUUwrTWM5T1Nsbm0xb0R2N0NtSkZNMUlMRVI3QTVGZnZKOEdFRjJ6dHBoaUlFMwpub1dtdHNZb3JuT2wzc2lHQ2ZGZzR4Zmd4eW8ybmlneFNVekl1bXNnVm9PM2ttT0x1RVF6cXpkakJ3TFJXbWlECklmMXBMWnoyalVnald4UkhCM1gyWnVVV1d1T09PZnpXM01LaE8ybHEvZi9DdS8wYk83c0x0MCt3U2ZMSU91TFcKcW90blZtRmxMMytqTy82WDNDKzBERHk5aUtwbXJjVDBnWGZLemE1dHJRSURBUUFCb0FBd0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnRUJBR05WdmVIOGR4ZzNvK21VeVRkbmFjVmQ1N24zSkExdnZEU1JWREkyQTZ1eXN3ZFp1L1BVCkkwZXpZWFV0RVNnSk1IRmQycVVNMjNuNVJsSXJ3R0xuUXFISUh5VStWWHhsdnZsRnpNOVpEWllSTmU3QlJvYXgKQVlEdUI5STZXT3FYbkFvczFqRmxNUG5NbFpqdU5kSGxpT1BjTU1oNndLaTZzZFhpVStHYTJ2RUVLY01jSVUyRgpvU2djUWdMYTk0aEpacGk3ZnNMdm1OQUxoT045UHdNMGM1dVJVejV4T0dGMUtCbWRSeEgvbUNOS2JKYjFRQm1HCkkwYitEUEdaTktXTU0xMzhIQXdoV0tkNjVoVHdYOWl4V3ZHMkh4TG1WQzg0L1BHT0tWQW9FNkpsYWFHdTlQVmkKdjlOSjVaZlZrcXdCd0hKbzZXdk9xVlA3SVFjZmg3d0drWm89Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400  # one day
  usages:
  - client auth
EOF
```

به‌عنوان راه دیگر، می‌توانید یک فایل مانیفست YAML ایجاد کنید و آن را با `kubectl` اعمال کنید:

{{% code_sample language="yaml" file="tls/myuser.yaml" %}}

مانیفست را اعمال کنید:

```bash
kubectl apply -f myuser.yaml --server-side
```


چند نکته که باید به آن‌ها توجه کنید:

- مقدار `usages` باید `client auth` باشد.
- مقدار `expirationSeconds` را می‌توان طولانی‌تر (برای مثال `864000` برای ده روز) یا کوتاه‌تر (برای مثال `3600` برای یک ساعت) تعیین کرد.
  نمی‌توانید مدتی کوتاه‌تر از ۱۰ دقیقه درخواست کنید.
- مقدار `request` محتوای فایل CSR است که با base64 کدگذاری شده است.

## تأیید CertificateSigningRequest {#approve-certificate-signing-request}

با kubectl درخواست CSR ایجادشده را پیدا کنید و آن را به‌صورت دستی تأیید کنید.

فهرست CSRها را دریافت کنید:

```shell
kubectl get csr
```

درخواست CSR را تأیید کنید:

```shell
kubectl certificate approve myuser
```

## دریافت گواهی

گواهی را از CSR بازیابی کنید تا از درستی آن مطمئن شوید.

```shell
kubectl get csr/myuser -o yaml
```

مقدار گواهی با کدگذاری Base64 در `.status.certificate` قرار دارد.

گواهی صادرشده را از CertificateSigningRequest استخراج کنید.

```shell
kubectl get csr myuser -o jsonpath='{.status.certificate}'| base64 -d > myuser.crt
```

## افزودن گواهی به kubeconfig

گام بعدی افزودن این کاربر به فایل kubeconfig است.

ابتدا باید اعتبارنامه‌های جدید را اضافه کنید:

```shell
kubectl config set-credentials myuser --client-key=myuser.key --client-certificate=myuser.crt --embed-certs=true

```

سپس باید context را اضافه کنید:

```shell
kubectl config set-context myuser --cluster=kubernetes --user=myuser
```

برای آزمایش آن:

```shell
kubectl --context myuser auth whoami
```

باید خروجی‌ای ببینید که تأیید می‌کند شما «myuser» هستید.

## ایجاد Role و RoleBinding

{{< note >}}
اگر از RBAC کوبرنتیز استفاده نمی‌کنید، این گام را نادیده بگیرید و تغییرات مناسب را برای سازوکار مجوزدهی‌ای که کلاستر شما واقعاً از آن استفاده می‌کند اعمال کنید.
{{< /note >}}

اکنون که گواهی ایجاد شده است، باید Role و RoleBinding را برای این کاربر تعریف کنید تا بتواند به منابع کلاستر کوبرنتیز دسترسی داشته باشد.

این یک دستور نمونه برای ایجاد Role برای این کاربر جدید است:

```shell
kubectl create role developer --verb=create --verb=get --verb=list --verb=update --verb=delete --resource=pods
```

معادل YAML:
{{% code_sample language="yaml" file="tls/role.yaml" %}}

این یک دستور نمونه برای ایجاد RoleBinding برای این کاربر جدید است:

```shell
kubectl create rolebinding developer-binding-myuser --role=developer --user=myuser
```

معادل YAML:

{{% code_sample language="yaml" file="tls/rolebinding.yaml" %}}

## {{% heading "whatsnext" %}}

* صفحهٔ [مدیریت گواهی‌های TLS در کلاستر](/docs/tasks/tls/managing-tls-in-a-cluster/) را بخوانید.
* برای جزئیات خود X.509، به بخش ۳.۱ از [RFC 5280](https://tools.ietf.org/html/rfc5280#section-3.1) مراجعه کنید.
* برای اطلاعات دربارهٔ نحو درخواست‌های امضای گواهی PKCS#10، به [RFC 2986](https://tools.ietf.org/html/rfc2986) مراجعه کنید.
* دربارهٔ [ClusterTrustBundleها](/docs/reference/access-authn-authz/certificate-signing-requests/#cluster-trust-bundles) بخوانید.
