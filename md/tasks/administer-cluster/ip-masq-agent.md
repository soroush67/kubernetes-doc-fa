---
title: راهنمای کاربر عامل IP Masquerade
content_type: task
weight: 230
---

<!-- overview -->
این صفحه نحوهٔ پیکربندی و فعال‌سازی `ip-masq-agent` را نشان می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

<!-- discussion -->
## راهنمای کاربر عامل IP Masquerade

عامل `ip-masq-agent` قواعد iptables را طوری پیکربندی می‌کند که نشانی IP هر پاد پشت نشانی IP نود
کلاستر پنهان شود. این کار معمولاً هنگام ارسال ترافیک به مقصدهایی انجام می‌شود که بیرون از محدودهٔ
[CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) پادهای کلاستر قرار دارند.

### اصطلاحات کلیدی

* **NAT (ترجمهٔ نشانی شبکه یا Network Address Translation)**:
  روشی برای نگاشت دوبارهٔ یک نشانی IP به نشانی دیگر است که با تغییر اطلاعات نشانی مبدأ و/یا مقصد
  در سرآیند IP انجام می‌شود. این کار معمولاً به دست دستگاهی انجام می‌شود که مسیریابی IP را بر عهده دارد.
* **Masquerading (پنهان‌سازی نشانی)**:
  گونه‌ای از NAT است که معمولاً برای ترجمهٔ نشانی چند به یک به کار می‌رود؛ در این حالت، چندین
  نشانی IP مبدأ پشت یک نشانی واحد پنهان می‌شوند که معمولاً نشانی دستگاه انجام‌دهندهٔ مسیریابی IP
  است. در کوبرنتیز، این نشانی همان نشانی IP نود است.
* **CIDR (مسیریابی بین‌دامنه‌ای بدون کلاس یا Classless Inter-Domain Routing)**:
  این روش بر پایهٔ ماسک‌گذاری زیرشبکه با طول متغیر است و امکان تعیین پیشوندهایی با طول دلخواه را
  فراهم می‌کند. CIDR شیوهٔ تازه‌ای برای نمایش نشانی‌های IP معرفی کرد که امروزه با نام
  **نمادگذاری CIDR** شناخته می‌شود؛ در این نمادگذاری، نشانی یا پیشوند مسیریابی همراه با پسوندی
  نوشته می‌شود که تعداد بیت‌های پیشوند را نشان می‌دهد، مانند 192.168.2.0/24.
* **Link Local (پیوند محلی)**:
  نشانی پیوند محلی، نشانی شبکه‌ای است که فقط برای ارتباط در همان بخش شبکه یا دامنهٔ پخشی
  (broadcast domain) که میزبان به آن متصل است، اعتبار دارد. نشانی‌های پیوند محلی در IPv4 در
  بلوک نشانی 169.254.0.0/16 (به نمادگذاری CIDR) تعریف شده‌اند.

عامل ip-masq-agent قواعد iptables را برای پنهان‌سازی نشانی‌های IP نود/پاد هنگام ارسال ترافیک به
مقصدهای بیرون از محدودهٔ IP نودهای کلاستر و محدودهٔ Cluster IP پیکربندی می‌کند. در واقع، این کار
نشانی‌های IP پادها را پشت نشانی IP نود کلاستر پنهان می‌کند. در برخی محیط‌ها، ترافیکی که به
نشانی‌های «خارجی» فرستاده می‌شود باید از نشانی یک ماشین شناخته‌شده بیاید. برای نمونه، در
Google Cloud هر ترافیکی که به اینترنت می‌رود باید از IP یک ماشین مجازی (VM) بیاید. وقتی از
کانتینرها استفاده می‌شود، مانند Google Kubernetes Engine، ترافیک خروجی با IP پاد رد می‌شود.
برای جلوگیری از این مشکل، باید IP پاد را پشت نشانی IP خودِ ماشین مجازی پنهان کنیم؛ این کار
معمولاً «masquerade» نامیده می‌شود. به‌طور پیش‌فرض، این عامل طوری پیکربندی شده است که سه محدودهٔ
IP خصوصی تعریف‌شده در [RFC 1918](https://tools.ietf.org/html/rfc1918) را
[CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)های بدون پنهان‌سازی در نظر
بگیرد. این محدوده‌ها عبارت‌اند از `10.0.0.0/8`، `172.16.0.0/12` و `192.168.0.0/16`.
این عامل به‌طور پیش‌فرض محدودهٔ پیوند محلی (169.254.0.0/16) را نیز CIDR بدون پنهان‌سازی در نظر
می‌گیرد. همچنین این عامل طوری پیکربندی شده است که هر ۶۰ ثانیه پیکربندی خود را از مسیر
*/etc/config/ip-masq-agent* دوباره بارگذاری کند و این بازه نیز قابل پیکربندی است.

![نمونهٔ masq/non-masq](/images/docs/ip-masq.png)

فایل پیکربندی این عامل باید با نحو YAML یا JSON نوشته شود و می‌تواند سه کلید اختیاری داشته باشد:

* `nonMasqueradeCIDRs`: فهرستی از رشته‌ها با نمادگذاری
  [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) که محدوده‌های بدون
  پنهان‌سازی را مشخص می‌کنند.
* `masqLinkLocal`: مقداری بولی (true/false) که مشخص می‌کند آیا ترافیک به پیشوند پیوند محلی
  `169.254.0.0/16` پنهان‌سازی شود یا نه. مقدار پیش‌فرض آن false است.
* `resyncInterval`: بازهٔ زمانی‌ای که عامل در آن تلاش می‌کند پیکربندی را دوباره از دیسک بارگذاری کند.
  برای نمونه: '30s' که در آن 's' به معنای ثانیه و 'ms' به معنای میلی‌ثانیه است.

ترافیک به محدوده‌های 10.0.0.0/8، 172.16.0.0/12 و 192.168.0.0/16 پنهان‌سازی **نمی‌شود**. هر
ترافیک دیگری (که فرض می‌شود به اینترنت می‌رود) پنهان‌سازی می‌شود. نمونه‌ای از یک مقصد محلی برای
یک پاد می‌تواند نشانی IP نود خودش، نشانی یک نود دیگر یا یکی از نشانی‌های IP در محدودهٔ IP کلاستر
باشد. هر ترافیک دیگری به‌طور پیش‌فرض پنهان‌سازی می‌شود. ورودی‌های زیر مجموعهٔ پیش‌فرض قواعدی را
نشان می‌دهند که ip-masq-agent اعمال می‌کند:

```shell
iptables -t nat -L IP-MASQ-AGENT
```

```none
target     prot opt source               destination
RETURN     all  --  anywhere             169.254.0.0/16       /* ip-masq-agent: cluster-local traffic should not be subject to MASQUERADE */ ADDRTYPE match dst-type !LOCAL
RETURN     all  --  anywhere             10.0.0.0/8           /* ip-masq-agent: cluster-local traffic should not be subject to MASQUERADE */ ADDRTYPE match dst-type !LOCAL
RETURN     all  --  anywhere             172.16.0.0/12        /* ip-masq-agent: cluster-local traffic should not be subject to MASQUERADE */ ADDRTYPE match dst-type !LOCAL
RETURN     all  --  anywhere             192.168.0.0/16       /* ip-masq-agent: cluster-local traffic should not be subject to MASQUERADE */ ADDRTYPE match dst-type !LOCAL
MASQUERADE  all  --  anywhere             anywhere             /* ip-masq-agent: outbound traffic should be subject to MASQUERADE (this match must come after cluster-local CIDR matches) */ ADDRTYPE match dst-type !LOCAL

```

به‌طور پیش‌فرض، در GCE/Google Kubernetes Engine اگر سیاست شبکه (network policy) فعال باشد
یا از CIDR کلاستری بیرون از محدودهٔ 10.0.0.0/8 استفاده کنید، `ip-masq-agent` در کلاستر شما
اجرا می‌شود. اگر در محیط دیگری کار می‌کنید، می‌توانید
[DaemonSet](/docs/concepts/workloads/controllers/daemonset/) مربوط به `ip-masq-agent` را
به کلاستر خود اضافه کنید.

<!-- steps -->

## ایجاد یک ip-masq-agent

برای ایجاد یک ip-masq-agent، دستور kubectl زیر را اجرا کنید:

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/ip-masq-agent/master/ip-masq-agent.yaml
```

همچنین باید برچسب نود مناسب را روی همهٔ نودهایی از کلاستر که می‌خواهید این عامل روی آن‌ها اجرا
شود، اعمال کنید.

```shell
kubectl label nodes my-node node.kubernetes.io/masq-agent-ds-ready=true
```

اطلاعات بیشتر را می‌توانید [اینجا](https://github.com/kubernetes-sigs/ip-masq-agent) در مستندات ip-masq-agent بیابید.

در بیشتر موارد، مجموعهٔ پیش‌فرض قواعد کافی است؛ اما اگر برای کلاستر شما این‌طور نیست، می‌توانید یک
[ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) ایجاد و اعمال کنید
تا محدوده‌های IP تحت تأثیر را سفارشی کنید. برای نمونه، برای اینکه ip-masq-agent فقط محدودهٔ
10.0.0.0/8 را در نظر بگیرد، می‌توانید
[ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/) زیر را در فایلی به نام
"config" ایجاد کنید.

{{< note >}}
مهم است که نام فایل config باشد، زیرا `ip-masq-agent` به‌طور پیش‌فرض از همین نام به‌عنوان کلید
جست‌وجو استفاده می‌کند:

```yaml
nonMasqueradeCIDRs:
  - 10.0.0.0/8
resyncInterval: 60s
```
{{< /note >}}

برای افزودن این configmap به کلاستر خود، دستور زیر را اجرا کنید:

```shell
kubectl create configmap ip-masq-agent --from-file=config --namespace=kube-system
```

این کار فایلی را در مسیر `/etc/config/ip-masq-agent` به‌روزرسانی می‌کند که در هر بازهٔ
`resyncInterval` بررسی و روی نود کلاستر اعمال می‌شود.
پس از پایان بازهٔ همگام‌سازی دوباره، باید تغییرات خود را در قواعد iptables ببینید:

```shell
iptables -t nat -L IP-MASQ-AGENT
```

```none
Chain IP-MASQ-AGENT (1 references)
target     prot opt source               destination
RETURN     all  --  anywhere             169.254.0.0/16       /* ip-masq-agent: cluster-local traffic should not be subject to MASQUERADE */ ADDRTYPE match dst-type !LOCAL
RETURN     all  --  anywhere             10.0.0.0/8           /* ip-masq-agent: cluster-local
MASQUERADE  all  --  anywhere             anywhere             /* ip-masq-agent: outbound traffic should be subject to MASQUERADE (this match must come after cluster-local CIDR matches) */ ADDRTYPE match dst-type !LOCAL
```

به‌طور پیش‌فرض، محدودهٔ پیوند محلی (169.254.0.0/16) نیز به دست عامل ip-masq مدیریت می‌شود و این
عامل قواعد iptables مناسب را برای آن تنظیم می‌کند. برای اینکه ip-masq-agent محدودهٔ پیوند محلی را
نادیده بگیرد، می‌توانید مقدار `masqLinkLocal` را در ConfigMap برابر true قرار دهید.

```yaml
nonMasqueradeCIDRs:
  - 10.0.0.0/8
resyncInterval: 60s
masqLinkLocal: true
```
