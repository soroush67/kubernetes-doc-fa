---
title: پشتهٔ دوگانهٔ IPv4/IPv6
description: >-
  کوبرنتیز به شما امکان می‌دهد شبکهٔ تک‌پشته‌ای IPv4،
  شبکهٔ تک‌پشته‌ای IPv6 یا شبکهٔ دوپشته‌ای (dual-stack) را با
  فعال بودن هر دو خانوادهٔ شبکه پیکربندی کنید. این صفحه نحوهٔ انجام آن را توضیح می‌دهد.
feature:
  title: پشتهٔ دوگانهٔ IPv4/IPv6
  description: >
    تخصیص نشانی‌های IPv4 و IPv6 به Podها و Serviceها
content_type: concept
reviewers:
  - lachie83
  - khenidak
  - aramase
  - bridgetkromhout
weight: 90
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.23" state="stable" >}}

شبکهٔ دوپشته‌ای (dual-stack) IPv4/IPv6 امکان تخصیص هم‌زمان نشانی‌های IPv4 و IPv6 را به
{{< glossary_tooltip text="Podها" term_id="pod" >}} و {{< glossary_tooltip text="Serviceها" term_id="service" >}} فراهم می‌کند.

شبکهٔ دوپشته‌ای IPv4/IPv6 از نسخهٔ 1.21 به‌طور پیش‌فرض برای کلاستر کوبرنتیز شما فعال است
و امکان اختصاص هم‌زمان نشانی‌های IPv4 و IPv6 را فراهم می‌کند.

<!-- body -->

## قابلیت‌های پشتیبانی‌شده

پشتهٔ دوگانهٔ IPv4/IPv6 در کلاستر کوبرنتیز شما قابلیت‌های زیر را فراهم می‌کند:

* شبکهٔ دوپشته‌ای برای Podها (اختصاص یک نشانی IPv4 و یک نشانی IPv6 به هر Pod)
* Serviceهای دارای IPv4 و IPv6
* مسیریابی ترافیک خروجی (egress) Pod به خارج از کلاستر (مثلاً اینترنت) از طریق هر دو رابط IPv4 و IPv6

## پیش‌نیازها

برای بهره‌گیری از کلاسترهای کوبرنتیز دوپشته‌ای IPv4/IPv6، پیش‌نیازهای زیر لازم است:

* کوبرنتیز نسخهٔ 1.20 یا بالاتر

  برای اطلاعات دربارهٔ استفاده از Serviceهای دوپشته‌ای در نسخه‌های قدیمی‌تر
  کوبرنتیز، به مستندات همان نسخه از
  کوبرنتیز مراجعه کنید.

* پشتیبانی ارائه‌دهنده از شبکهٔ دوپشته‌ای (ارائه‌دهندهٔ ابری یا هر ارائه‌دهندهٔ دیگر باید بتواند
  رابط‌های شبکهٔ IPv4/IPv6 قابل مسیریابی را در اختیار نودهای کوبرنتیز قرار دهد)
* یک [افزونهٔ شبکه](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) که
  از شبکهٔ دوپشته‌ای پشتیبانی کند.

## پیکربندی پشتهٔ دوگانهٔ IPv4/IPv6

برای پیکربندی پشتهٔ دوگانهٔ IPv4/IPv6، تخصیص‌های شبکهٔ دوپشته‌ای کلاستر را تنظیم کنید:

* kube-apiserver:
  * `--service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR>`
* kube-controller-manager:
  * `--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>`
  * `--service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR>`
  * مقدار پیش‌فرض `--node-cidr-mask-size-ipv4|--node-cidr-mask-size-ipv6` برای IPv4 برابر /24 و برای IPv6 برابر /64 است
* kube-proxy:
  * `--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>`
* kubelet:
  * `--node-ip=<IPv4 IP>,<IPv6 IP>`
    * این گزینه برای نودهای دوپشته‌ای bare metal (نودهایی که با فلگ `--cloud-provider`
      ارائه‌دهندهٔ ابری تعریف نمی‌کنند) الزامی است. اگر از یک ارائه‌دهندهٔ ابری استفاده می‌کنید
      و می‌خواهید IPهای نودی را که ارائه‌دهندهٔ ابری انتخاب کرده است بازنویسی کنید، گزینهٔ
      `--node-ip` را تنظیم کنید.
    * (ارائه‌دهندگان ابری قدیمیِ درون‌ساخت از `--node-ip` دوپشته‌ای پشتیبانی نمی‌کنند.)

{{< note >}}
نمونه‌ای از یک CIDR در IPv4: `10.244.0.0/16` (هرچند شما بازهٔ نشانی خود را ارائه خواهید کرد)

نمونه‌ای از یک CIDR در IPv6: `fdXY:IJKL:MNOP:15::/64` (این نمونه قالب را نشان می‌دهد اما نشانی
معتبری نیست - [RFC 4193](https://tools.ietf.org/html/rfc4193) را ببینید)
{{< /note >}}

## Serviceها

شما می‌توانید {{< glossary_tooltip text="Serviceهایی" term_id="service" >}} ایجاد کنید که از IPv4، IPv6 یا هر دو استفاده کنند.

خانوادهٔ نشانی یک Service به‌طور پیش‌فرض همان خانوادهٔ نشانیِ نخستین بازهٔ cluster IP سرویس
است (که از طریق فلگ `--service-cluster-ip-range` در kube-apiserver پیکربندی می‌شود).

هنگام تعریف یک Service، می‌توانید به‌صورت اختیاری آن را دوپشته‌ای پیکربندی کنید. برای تعیین رفتار مورد نظر،
فیلد `.spec.ipFamilyPolicy` را روی یکی از مقادیر زیر تنظیم می‌کنید:

* `SingleStack`: سرویس تک‌پشته‌ای. control plane با استفاده از نخستین بازهٔ
  cluster IP سرویسِ پیکربندی‌شده، یک cluster IP برای Service تخصیص می‌دهد.
* `PreferDualStack`: هنگامی که پشتهٔ دوگانه فعال باشد، هر دو cluster IP از نوع IPv4 و IPv6 را برای Service تخصیص می‌دهد. اگر پشتهٔ دوگانه فعال یا پشتیبانی‌شده نباشد، به رفتار تک‌پشته‌ای بازمی‌گردد.
* `RequireDualStack`: هنگامی که پشتهٔ دوگانه فعال باشد، `.spec.clusterIPs` مربوط به Service را از هر دو بازهٔ نشانی IPv4 و IPv6 تخصیص می‌دهد. اگر پشتهٔ دوگانه فعال یا پشتیبانی‌شده نباشد، ایجاد آبجکت API مربوط به Service با شکست مواجه می‌شود.
  * `.spec.clusterIP` را بر اساس خانوادهٔ نشانیِ نخستین عنصر آرایهٔ `.spec.ipFamilies`،
    از فهرست `.spec.clusterIPs` انتخاب می‌کند.

اگر می‌خواهید تعیین کنید کدام خانوادهٔ IP برای حالت تک‌پشته‌ای استفاده شود یا ترتیب خانواده‌های IP
را برای حالت دوپشته‌ای تعریف کنید، می‌توانید با تنظیم فیلد اختیاری
`.spec.ipFamilies` روی Service، خانواده‌های نشانی را انتخاب کنید.

{{< note >}}
فیلد `.spec.ipFamilies` به‌طور مشروط قابل تغییر است: می‌توانید یک خانوادهٔ نشانی IP ثانویه را
اضافه یا حذف کنید، اما نمی‌توانید خانوادهٔ نشانی IP اصلیِ یک Service موجود را تغییر دهید.
{{< /note >}}

می‌توانید `.spec.ipFamilies` را روی هر یک از مقادیر آرایه‌ای زیر تنظیم کنید:

- `["IPv4"]`
- `["IPv6"]`
- `["IPv4","IPv6"]` (دوپشته‌ای)
- `["IPv6","IPv4"]` (دوپشته‌ای)

نخستین خانواده‌ای که فهرست می‌کنید، برای فیلد قدیمی `.spec.clusterIP` استفاده می‌شود.

### سناریوهای پیکربندی Service دوپشته‌ای

این نمونه‌ها رفتار سناریوهای مختلف پیکربندی Service دوپشته‌ای را نشان می‌دهند.

#### گزینه‌های دوپشته‌ای در Serviceهای جدید

1. این مشخصات Service، فیلد `.spec.ipFamilyPolicy` را صراحتاً تعریف نمی‌کند. هنگامی که
   این Service را ایجاد می‌کنید، کوبرنتیز یک cluster IP را از نخستین
   `service-cluster-ip-range` پیکربندی‌شده به Service اختصاص می‌دهد و `.spec.ipFamilyPolicy` را روی `SingleStack` تنظیم می‌کند. ([Serviceهای
   بدون انتخابگر](/docs/concepts/services-networking/service/#services-without-selectors) و
   [Serviceهای headless](/docs/concepts/services-networking/service/#headless-services) دارای انتخابگر
   نیز به همین شکل رفتار می‌کنند.)

   {{% code_sample file="service/networking/dual-stack-default-svc.yaml" %}}

1. این مشخصات Service، مقدار `PreferDualStack` را صراحتاً در `.spec.ipFamilyPolicy` تعریف می‌کند. هنگامی که
   این Service را در یک کلاستر دوپشته‌ای ایجاد می‌کنید، کوبرنتیز هر دو نشانی IPv4 و IPv6
   را به سرویس اختصاص می‌دهد. control plane فیلد `.spec` مربوط به Service را به‌روزرسانی می‌کند تا
   تخصیص‌های نشانی IP را ثبت کند. فیلد `.spec.clusterIPs` فیلد اصلی است و هر دو نشانی IP
   تخصیص‌یافته را در بر دارد؛ `.spec.clusterIP` یک فیلد ثانویه است که مقدار آن از
   `.spec.clusterIPs` محاسبه می‌شود.

   * برای فیلد `.spec.clusterIP`، control plane نشانی IPای را ثبت می‌کند که از
     همان خانوادهٔ نشانیِ نخستین بازهٔ cluster IP سرویس است.
   * در یک کلاستر تک‌پشته‌ای، فیلدهای `.spec.clusterIPs` و `.spec.clusterIP` هر دو تنها
     یک نشانی را فهرست می‌کنند.
   * در کلاستری که پشتهٔ دوگانه در آن فعال است، تعیین `RequireDualStack` در `.spec.ipFamilyPolicy`
     همان رفتار `PreferDualStack` را دارد.

   {{% code_sample file="service/networking/dual-stack-preferred-svc.yaml" %}}

1. این مشخصات Service، مقادیر `IPv6` و `IPv4` را صراحتاً در `.spec.ipFamilies` تعریف می‌کند و
   همچنین `PreferDualStack` را در `.spec.ipFamilyPolicy` تعریف می‌کند. هنگامی که کوبرنتیز یک نشانی IPv6 و
   یک نشانی IPv4 را در `.spec.clusterIPs` اختصاص می‌دهد، `.spec.clusterIP` روی نشانی IPv6 تنظیم می‌شود، زیرا این نشانی
   نخستین عنصر آرایهٔ `.spec.clusterIPs` است و مقدار پیش‌فرض را بازنویسی می‌کند.

   {{% code_sample file="service/networking/dual-stack-preferred-ipfamilies-svc.yaml" %}}

#### پیش‌فرض‌های دوپشته‌ای در Serviceهای موجود

این نمونه‌ها رفتار پیش‌فرض را هنگامی نشان می‌دهند که پشتهٔ دوگانه به‌تازگی در کلاستری
فعال شده است که Serviceها از پیش در آن وجود دارند. (ارتقای یک کلاستر موجود به نسخهٔ 1.21 یا بالاتر،
پشتهٔ دوگانه را فعال می‌کند.)

1. هنگامی که پشتهٔ دوگانه در یک کلاستر فعال می‌شود، control plane، Serviceهای موجود (چه `IPv4` و چه `IPv6`) را
   طوری پیکربندی می‌کند که `.spec.ipFamilyPolicy` روی `SingleStack` و
   `.spec.ipFamilies` روی خانوادهٔ نشانیِ Service موجود تنظیم شود. cluster IP مربوط به Service موجود
   در `.spec.clusterIPs` ذخیره خواهد شد.

   {{% code_sample file="service/networking/dual-stack-default-svc.yaml" %}}

   می‌توانید این رفتار را با استفاده از kubectl و بررسی یک سرویس موجود تأیید کنید.

   ```shell
   kubectl get svc my-service -o yaml
   ```

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     labels:
       app.kubernetes.io/name: MyApp
     name: my-service
   spec:
     clusterIP: 10.0.197.123
     clusterIPs:
     - 10.0.197.123
     ipFamilies:
     - IPv4
     ipFamilyPolicy: SingleStack
     ports:
     - port: 80
       protocol: TCP
       targetPort: 80
     selector:
       app.kubernetes.io/name: MyApp
     type: ClusterIP
   status:
     loadBalancer: {}
   ```

1. هنگامی که پشتهٔ دوگانه در یک کلاستر فعال می‌شود، control plane،
   [Serviceهای headless](/docs/concepts/services-networking/service/#headless-services) موجودِ دارای انتخابگر را
   طوری پیکربندی می‌کند که `.spec.ipFamilyPolicy` روی `SingleStack` و
   `.spec.ipFamilies` روی خانوادهٔ نشانیِ نخستین بازهٔ cluster IP سرویس (که از طریق
   فلگ `--service-cluster-ip-range` در kube-apiserver پیکربندی می‌شود) تنظیم شود، حتی اگر `.spec.clusterIP` روی
   `None` تنظیم شده باشد.

   {{% code_sample file="service/networking/dual-stack-default-svc.yaml" %}}

   می‌توانید این رفتار را با استفاده از kubectl و بررسی یک سرویس headless موجودِ دارای انتخابگر تأیید کنید.

   ```shell
   kubectl get svc my-service -o yaml
   ```

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     labels:
       app.kubernetes.io/name: MyApp
     name: my-service
   spec:
     clusterIP: None
     clusterIPs:
     - None
     ipFamilies:
     - IPv4
     ipFamilyPolicy: SingleStack
     ports:
     - port: 80
       protocol: TCP
       targetPort: 80
     selector:
       app.kubernetes.io/name: MyApp
   ```

#### تغییر Serviceها میان حالت تک‌پشته‌ای و دوپشته‌ای

Serviceها را می‌توان از حالت تک‌پشته‌ای به دوپشته‌ای و از حالت دوپشته‌ای به تک‌پشته‌ای تغییر داد.

1. برای تغییر یک Service از حالت تک‌پشته‌ای به دوپشته‌ای، `.spec.ipFamilyPolicy` را بنا به نیاز از
   `SingleStack` به `PreferDualStack` یا `RequireDualStack` تغییر دهید. هنگامی که این
   Service را از حالت تک‌پشته‌ای به دوپشته‌ای تغییر می‌دهید، کوبرنتیز خانوادهٔ نشانیِ کم‌شده را اختصاص می‌دهد تا
   Service اکنون نشانی‌های IPv4 و IPv6 داشته باشد.

   مشخصات Service را ویرایش کنید و `.spec.ipFamilyPolicy` را از `SingleStack` به `PreferDualStack` به‌روزرسانی کنید.

   پیش از تغییر:

   ```yaml
   spec:
     ipFamilyPolicy: SingleStack
   ```

   پس از تغییر:

   ```yaml
   spec:
     ipFamilyPolicy: PreferDualStack
   ```

1. برای تغییر یک Service از حالت دوپشته‌ای به تک‌پشته‌ای، `.spec.ipFamilyPolicy` را از
   `PreferDualStack` یا `RequireDualStack` به `SingleStack` تغییر دهید. هنگامی که این Service را از
   حالت دوپشته‌ای به تک‌پشته‌ای تغییر می‌دهید، کوبرنتیز تنها نخستین عنصر آرایهٔ `.spec.clusterIPs`
   را نگه می‌دارد، `.spec.clusterIP` را روی همان نشانی IP و `.spec.ipFamilies` را روی خانوادهٔ نشانیِ
   `.spec.clusterIPs` تنظیم می‌کند.

### Serviceهای headless بدون انتخابگر

برای [Serviceهای headless بدون انتخابگر](/docs/concepts/services-networking/service/#without-selectors)
که `.spec.ipFamilyPolicy` آن‌ها صراحتاً تنظیم نشده است، مقدار پیش‌فرض فیلد `.spec.ipFamilyPolicy`
برابر با `RequireDualStack` است.

### Service از نوع LoadBalancer

برای فراهم کردن یک توزیع‌کنندهٔ بار (load balancer) دوپشته‌ای برای Service خود:

* فیلد `.spec.type` را روی `LoadBalancer` تنظیم کنید
* فیلد `.spec.ipFamilyPolicy` را روی `PreferDualStack` یا `RequireDualStack` تنظیم کنید

{{< note >}}
برای استفاده از یک Service دوپشته‌ای از نوع `LoadBalancer`، ارائه‌دهندهٔ ابری شما باید از توزیع‌کننده‌های بار
IPv4 و IPv6 پشتیبانی کند.
{{< /note >}}

## ترافیک خروجی (egress)

اگر می‌خواهید ترافیک خروجی را برای دسترسی به مقصدهای خارج از کلاستر (مثلاً اینترنت
عمومی) از Podی فعال کنید که از نشانی‌های IPv6 غیرقابل مسیریابی عمومی استفاده می‌کند، باید امکان
استفاده از یک نشانی IPv6 قابل مسیریابی عمومی را از طریق سازوکاری مانند پراکسی شفاف (transparent proxying) یا
IP masquerading برای Pod فراهم کنید. پروژهٔ [ip-masq-agent](https://github.com/kubernetes-sigs/ip-masq-agent)
از IP masquerading در کلاسترهای دوپشته‌ای پشتیبانی می‌کند.

{{< note >}}
اطمینان حاصل کنید که ارائه‌دهندهٔ {{< glossary_tooltip text="CNI" term_id="cni" >}} شما از IPv6 پشتیبانی می‌کند.
{{< /note >}}

## پشتیبانی از ویندوز

کوبرنتیز در ویندوز از شبکهٔ تک‌پشته‌ای «فقط IPv6» پشتیبانی نمی‌کند. با این حال،
شبکهٔ دوپشته‌ای IPv4/IPv6 برای Podها و نودها همراه با Serviceهای تک‌خانواده
پشتیبانی می‌شود.

می‌توانید از شبکهٔ دوپشته‌ای IPv4/IPv6 با شبکه‌های `l2bridge` استفاده کنید.

{{< note >}}
شبکه‌های Overlay (VXLAN) در ویندوز از شبکهٔ دوپشته‌ای پشتیبانی **نمی‌کنند**.
{{< /note >}}

می‌توانید دربارهٔ حالت‌های مختلف شبکه در ویندوز، در مبحث
[شبکه در ویندوز](/docs/concepts/services-networking/windows-networking#network-modes) بیشتر بخوانید.

## {{% heading "whatsnext" %}}

* [اعتبارسنجی شبکهٔ دوپشته‌ای IPv4/IPv6](/docs/tasks/network/validate-dual-stack)
* [فعال‌سازی شبکهٔ دوپشته‌ای با استفاده از kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/)
