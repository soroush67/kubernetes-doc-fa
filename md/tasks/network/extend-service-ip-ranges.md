---
reviewers:
- thockin
- dwinship
min-kubernetes-server-version: v1.29
title: گسترش بازه‌های IP سرویس
content_type: task
---

<!-- overview -->
{{< feature-state feature_gate_name="MultiCIDRServiceAllocator" >}}

این سند نحوهٔ گسترش بازهٔ IP موجود سرویس (Service) را که به یک کلاستر اختصاص داده شده است، شرح می‌دهد.


## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

{{< version-check >}}

{{< note >}}
هرچند می‌توانید از این قابلیت در نسخه‌های قدیمی‌تر نیز استفاده کنید، این قابلیت تنها از نسخهٔ v1.33 به وضعیت GA رسیده و به‌طور رسمی پشتیبانی می‌شود.
{{< /note >}}

<!-- steps -->

## گسترش بازه‌های IP سرویس

control plane تضمین می‌کند که یک آبجکت ویژهٔ ServiceCIDR با نام شناخته‌شدهٔ `kubernetes` وجود داشته باشد. این آبجکت یک بازهٔ نشانی IP را بر اساس مقدار آرگومان خط فرمان `--service-cluster-ip-range` در kube-apiserver مشخص می‌کند.

```sh
kubectl get servicecidr
```

```
NAME         CIDRS          AGE
kubernetes   10.96.0.0/28   17d
```

سرویس شناخته‌شدهٔ `kubernetes` که endpoint مربوط به kube-apiserver را در اختیار Podها قرار می‌دهد، نخستین نشانی IP را از بازهٔ پیش‌فرض ServiceCIDR محاسبه می‌کند و از همان نشانی به‌عنوان نشانی IP کلاستری خود استفاده می‌کند.

```sh
kubectl get service kubernetes
```

```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   17d
```

در این مثال، سرویس پیش‌فرض از ClusterIP با نشانی 10.96.0.1 استفاده می‌کند که آبجکت IPAddress متناظر با آن وجود دارد.

```sh
kubectl get ipaddress 10.96.0.1
```

```
NAME        PARENTREF
10.96.0.1   services/default/kubernetes
```

آبجکت‌های ServiceCIDR با {{<glossary_tooltip text="finalizerها" term_id="finalizer">}} محافظت می‌شوند تا ClusterIPهای سرویس‌ها بی‌صاحب (orphan) باقی نمانند. finalizer تنها زمانی حذف می‌شود که زیرشبکهٔ دیگری وجود داشته باشد که IPAddressهای موجود را در بر بگیرد، یا هیچ IPAddressای متعلق به این زیرشبکه نباشد.

## افزایش تعداد IPهای در دسترس برای سرویس‌ها

گاهی کاربران نیاز دارند تعداد نشانی‌های در دسترس برای سرویس‌ها را افزایش دهند. پیش‌تر، گسترش بازهٔ سرویس عملیاتی اختلال‌آفرین بود که حتی ممکن بود به از دست رفتن داده‌ها بینجامد. با این قابلیت جدید، کاربران تنها کافی است یک ServiceCIDR جدید اضافه کنند تا تعداد نشانی‌های در دسترس افزایش یابد.

### افزودن یک ServiceCIDR جدید

در کلاستری که بازهٔ 10.96.0.0/28 برای سرویس‌ها دارد، تنها 2^(32-28) - 2 = 14 نشانی IP در دسترس است. سرویس `kubernetes.default` همیشه ایجاد می‌شود؛ بنابراین در این مثال تنها 13 سرویس دیگر می‌توانید ایجاد کنید.

```sh
for i in $(seq 1 13); do kubectl create service clusterip "test-$i" --tcp 80 -o json | jq -r .spec.clusterIP; done
```

```
10.96.0.11
10.96.0.5
10.96.0.12
10.96.0.13
10.96.0.14
10.96.0.2
10.96.0.3
10.96.0.4
10.96.0.6
10.96.0.7
10.96.0.8
10.96.0.9
error: failed to create ClusterIP service: Internal error occurred: failed to allocate a serviceIP: range is full
```

می‌توانید با ایجاد یک ServiceCIDR جدید که بازه‌های نشانی IP را گسترش می‌دهد یا بازه‌های تازه‌ای اضافه می‌کند، تعداد نشانی‌های IP در دسترس برای سرویس‌ها را افزایش دهید.

```sh
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: ServiceCIDR
metadata:
  name: newcidr1
spec:
  cidrs:
  - 10.96.0.0/24
EOF
```

```
servicecidr.networking.k8s.io/newcidr1 created
```

با این کار می‌توانید سرویس‌های جدیدی ایجاد کنید که ClusterIP آن‌ها از این بازهٔ جدید انتخاب می‌شود.

```sh
for i in $(seq 13 16); do kubectl create service clusterip "test-$i" --tcp 80 -o json | jq -r .spec.clusterIP; done
```

```
10.96.0.48
10.96.0.200
10.96.0.121
10.96.0.144
```

### حذف یک ServiceCIDR

اگر IPAddressهایی به یک ServiceCIDR وابسته باشند، نمی‌توانید آن را حذف کنید.

```sh
kubectl delete servicecidr newcidr1
```

```
servicecidr.networking.k8s.io "newcidr1" deleted
```

کوبرنتیز برای پیگیری این رابطهٔ وابستگی، از یک finalizer روی ServiceCIDR استفاده می‌کند.

```sh
kubectl get servicecidr newcidr1 -o yaml
```

```yaml
apiVersion: networking.k8s.io/v1
kind: ServiceCIDR
metadata:
  creationTimestamp: "2023-10-12T15:11:07Z"
  deletionGracePeriodSeconds: 0
  deletionTimestamp: "2023-10-12T15:12:45Z"
  finalizers:
  - networking.k8s.io/service-cidr-finalizer
  name: newcidr1
  resourceVersion: "1133"
  uid: 5ffd8afe-c78f-4e60-ae76-cec448a8af40
spec:
  cidrs:
  - 10.96.0.0/24
status:
  conditions:
  - lastTransitionTime: "2023-10-12T15:12:45Z"
    message: There are still IPAddresses referencing the ServiceCIDR, please remove
      them or create a new ServiceCIDR
    reason: OrphanIPAddress
    status: "False"
    type: Ready
```

با حذف سرویس‌هایی که نشانی‌های IP مانع حذف ServiceCIDR را در اختیار دارند،

```sh
for i in $(seq 13 16); do kubectl delete service "test-$i" ; done
```

```
service "test-13" deleted
service "test-14" deleted
service "test-15" deleted
service "test-16" deleted
```

control plane متوجه این حذف می‌شود. سپس control plane، finalizer مربوط به آن را برمی‌دارد تا ServiceCIDR که در انتظار حذف بود، واقعاً حذف شود.

```sh
kubectl get servicecidr newcidr1
```

```
Error from server (NotFound): servicecidrs.networking.k8s.io "newcidr1" not found
```

## سیاست‌های Service CIDR در کوبرنتیز

مدیران کلاستر می‌توانند سیاست‌هایی برای کنترل ایجاد و تغییر منابع ServiceCIDR در کلاستر پیاده‌سازی کنند. این کار امکان مدیریت متمرکز بازه‌های نشانی IP مورد استفادهٔ سرویس‌ها را فراهم می‌کند و از پیکربندی‌های ناخواسته یا متعارض جلوگیری می‌کند. کوبرنتیز سازوکارهایی مانند Validating Admission Policy را برای اعمال این قواعد فراهم می‌کند.

### جلوگیری از ایجاد یا به‌روزرسانی غیرمجاز ServiceCIDR با استفاده از Validating Admission Policy

ممکن است مدیران کلاستر بخواهند بازه‌های مجاز را محدود کنند یا هرگونه تغییر در بازه‌های IP سرویس کلاستر را به‌طور کامل ممنوع کنند.

{{< note >}}
ServiceCIDR پیش‌فرض با نام "kubernetes" را kube-apiserver برای حفظ سازگاری در کلاستر ایجاد می‌کند و وجود آن برای کارکرد کلاستر الزامی است؛ بنابراین همیشه باید مجاز باشد. برای اطمینان از اینکه `ValidatingAdmissionPolicy` شما ServiceCIDR پیش‌فرض را محدود نمی‌کند، می‌توانید این بند را اضافه کنید:

```yaml
  matchConditions:
  - name: 'exclude-default-servicecidr'
    expression: "object.metadata.name != 'kubernetes'"
```

همان‌طور که در مثال‌های زیر آمده است.
{{</ note >}}

#### محدود کردن بازه‌های Service CIDR به بازه‌هایی مشخص

در ادامه نمونه‌ای از یک `ValidatingAdmissionPolicy` آمده است که تنها در صورتی اجازهٔ ایجاد ServiceCIDR را می‌دهد که بازه‌های آن زیربازه‌ای از بازه‌های `allowed` تعیین‌شده باشند. (برای مثال، این سیاست اجازهٔ ایجاد ServiceCIDR با `cidrs: ['10.96.1.0/24']` یا `cidrs: ['2001:db8:0:0:ffff::/80', '10.96.0.0/20']` را می‌دهد، اما ServiceCIDR با `cidrs: ['172.20.0.0/16']` را مجاز نمی‌داند.) می‌توانید این سیاست را کپی کنید و مقدار `allowed` را به مقداری متناسب با کلاستر خود تغییر دهید.

{{% code_sample file="service/networking/vap-servicecidr-default.yaml" %}}

اگر می‌خواهید `expression` اعتبارسنجی خود را بنویسید، برای آشنایی بیشتر با CEL به [مستندات CEL](https://kubernetes.io/docs/reference/using-api/cel/) مراجعه کنید.

#### محدود کردن هرگونه استفاده از API مربوط به ServiceCIDR

مثال زیر نشان می‌دهد چگونه می‌توان از یک `ValidatingAdmissionPolicy` و binding آن برای محدود کردن ایجاد هرگونه بازهٔ جدید Service CIDR، به‌جز ServiceCIDR پیش‌فرض "kubernetes"، استفاده کرد:

{{% code_sample file="service/networking/vap-servicecidr-deny.yaml" %}}
