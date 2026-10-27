---
title: مدیر کنترل‌کنندهٔ ابری (Cloud Controller Manager)
content_type: concept
weight: 40
theme_lock: light
---

<!-- overview -->

{{< feature-state state="beta" for_k8s_version="v1.11" >}}

فناوری‌های زیرساخت ابری به شما امکان می‌دهند کوبرنتیز را روی ابرهای عمومی، خصوصی و ترکیبی اجرا کنید.
کوبرنتیز به زیرساختی خودکار و مبتنی بر API، بدون وابستگی تنگاتنگ میان
اجزا، باور دارد.

{{< glossary_definition term_id="cloud-controller-manager" length="all" prepend="The cloud-controller-manager is">}}

cloud-controller-manager با استفاده از یک سازوکار افزونه‌ای (plugin)
ساختار یافته است که به ارائه‌دهندگان ابری مختلف اجازه می‌دهد سکوهای خود را با کوبرنتیز یکپارچه کنند.

<!-- body -->

## طراحی

![اجزای کوبرنتیز](/images/docs/components-of-kubernetes.svg)

مدیر کنترل‌کنندهٔ ابری در control plane به‌صورت مجموعه‌ای تکثیرشده از فرایندها اجرا می‌شود
(معمولاً این فرایندها کانتینرهایی درون Podها هستند). هر cloud-controller-manager
چندین {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} را در یک
فرایند واحد پیاده‌سازی می‌کند.


{{< note >}}
همچنین می‌توانید مدیر کنترل‌کنندهٔ ابری را به‌جای اجرا به‌عنوان بخشی از control plane،
به‌صورت یک {{< glossary_tooltip text="افزونه" term_id="addons" >}}ی کوبرنتیز
اجرا کنید.
{{< /note >}}

## کارکردهای مدیر کنترل‌کنندهٔ ابری {#functions-of-the-ccm}

کنترل‌کننده‌های درون مدیر کنترل‌کنندهٔ ابری عبارت‌اند از:

### کنترل‌کنندهٔ نود

کنترل‌کنندهٔ نود مسئول به‌روزرسانی آبجکت‌های {{< glossary_tooltip text="Node" term_id="node" >}}
هنگام ایجاد سرورهای جدید در زیرساخت ابری شماست. کنترل‌کنندهٔ نود اطلاعات مربوط به
میزبان‌هایی را که درون فضای اجاره‌ای (tenancy) شما نزد ارائه‌دهندهٔ ابری اجرا می‌شوند به دست می‌آورد. کنترل‌کنندهٔ نود کارکردهای زیر را انجام می‌دهد:

1. به‌روزرسانی آبجکت Node با شناسهٔ یکتای سرور متناظر که از API ارائه‌دهندهٔ ابری به دست آمده است.
1. افزودن حاشیه‌نویسی و برچسب به آبجکت Node با اطلاعات مختص ابر، مانند منطقه‌ای (region) که نود
   در آن مستقر شده و منابعی (پردازنده، حافظه و غیره) که در اختیار دارد.
1. به دست آوردن نام میزبان و نشانی‌های شبکهٔ نود.
1. بررسی سلامت نود. در صورتی که نودی پاسخ‌گو نباشد، این کنترل‌کننده از طریق
   API ارائه‌دهندهٔ ابری شما بررسی می‌کند که آیا سرور غیرفعال / حذف / خاتمه داده شده است یا نه.
   اگر نود از ابر حذف شده باشد، کنترل‌کننده آبجکت Node را از کلاستر کوبرنتیز شما
   حذف می‌کند.

برخی از پیاده‌سازی‌های ارائه‌دهندگان ابری این کار را میان یک کنترل‌کنندهٔ نود و یک کنترل‌کنندهٔ
چرخهٔ عمر نود جداگانه تقسیم می‌کنند.

### کنترل‌کنندهٔ مسیر

کنترل‌کنندهٔ مسیر مسئول پیکربندی مناسب مسیرها در ابر است
تا کانتینرهای روی نودهای مختلف در کلاستر کوبرنتیز شما
بتوانند با یکدیگر ارتباط برقرار کنند.

بسته به ارائه‌دهندهٔ ابری، کنترل‌کنندهٔ مسیر ممکن است بلوک‌هایی
از نشانی‌های IP را نیز برای شبکهٔ Pod تخصیص دهد.

### کنترل‌کنندهٔ Service

{{< glossary_tooltip text="Serviceها" term_id="service" >}} با اجزای زیرساخت
ابری مانند متعادل‌کننده‌های بار مدیریت‌شده، نشانی‌های IP، پالایش بسته‌های
شبکه و بررسی سلامت مقصد یکپارچه می‌شوند. کنترل‌کنندهٔ Service با APIهای
ارائه‌دهندهٔ ابری شما تعامل می‌کند تا هنگامی که یک منبع Service را تعریف می‌کنید که به متعادل‌کننده‌های بار
و دیگر اجزای زیرساختی نیاز دارد، آن‌ها را راه‌اندازی کند.

## مجوزدهی

این بخش دسترسی‌هایی را که مدیر کنترل‌کنندهٔ ابری برای انجام عملیات خود
روی آبجکت‌های گوناگون API نیاز دارد، به تفکیک شرح می‌دهد.

### کنترل‌کنندهٔ نود {#authorization-node-controller}

کنترل‌کنندهٔ Node تنها با آبجکت‌های Node کار می‌کند. این کنترل‌کننده برای خواندن و
تغییر آبجکت‌های Node به دسترسی کامل نیاز دارد.

`v1/Node`:

- get
- list
- create
- update
- patch
- watch
- delete

### کنترل‌کنندهٔ مسیر {#authorization-route-controller}

کنترل‌کنندهٔ مسیر به رویداد ایجاد آبجکت Node گوش می‌دهد و مسیرها را
به‌طور مناسب پیکربندی می‌کند. این کنترل‌کننده به دسترسی Get روی آبجکت‌های Node نیاز دارد.

`v1/Node`:

- get

### کنترل‌کنندهٔ Service {#authorization-service-controller}

کنترل‌کنندهٔ Service رویدادهای **create**، **update** و **delete** آبجکت‌های Service را پایش می‌کند و سپس
متعادل‌کننده‌های بار را برای آن Serviceها به‌طور مناسب پیکربندی می‌کند.

برای دسترسی به Serviceها، این کنترل‌کننده به دسترسی‌های **list** و **watch** نیاز دارد. برای به‌روزرسانی Serviceها، به
دسترسی‌های **patch** و **update** روی زیرمنبع `status` نیاز دارد.

`v1/Service`:

- list
- get
- watch
- patch
- update

### سایر موارد {#authorization-miscellaneous}

پیاده‌سازی هستهٔ مدیر کنترل‌کنندهٔ ابری به دسترسی برای ایجاد آبجکت‌های Event
نیاز دارد و برای اطمینان از عملکرد امن، به دسترسی برای ایجاد ServiceAccountها نیاز دارد.

`v1/Event`:

- create
- patch
- update

`v1/ServiceAccount`:

- create

ClusterRole مربوط به {{< glossary_tooltip term_id="rbac" text="RBAC" >}} برای مدیر
کنترل‌کنندهٔ ابری به این شکل است:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cloud-controller-manager
rules:
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - '*'
- apiGroups:
  - ""
  resources:
  - nodes/status
  verbs:
  - patch
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - services/status
  verbs:
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - persistentvolumes
  verbs:
  - get
  - list
  - update
  - watch
```


## {{% heading "whatsnext" %}}

* [مدیریت Cloud Controller Manager](/docs/tasks/administer-cluster/running-cloud-controller/#cloud-controller-manager)
  دستورالعمل‌هایی برای اجرا و مدیریت مدیر کنترل‌کنندهٔ ابری ارائه می‌دهد.

* برای ارتقای یک control plane با دسترس‌پذیری بالا (HA) به‌منظور استفاده از مدیر کنترل‌کنندهٔ ابری، به
  [مهاجرت control plane تکثیرشده به استفاده از Cloud Controller Manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/) مراجعه کنید.

* می‌خواهید بدانید چگونه مدیر کنترل‌کنندهٔ ابری خود را پیاده‌سازی کنید یا یک پروژهٔ موجود را گسترش دهید؟

  - مدیر کنترل‌کنندهٔ ابری از رابط‌های Go استفاده می‌کند؛ به‌طور مشخص، رابط `CloudProvider` که در
    [`cloud.go`](https://github.com/kubernetes/cloud-provider/blob/release-1.21/cloud.go#L42-L69)
    از [kubernetes/cloud-provider](https://github.com/kubernetes/cloud-provider) تعریف شده است، تا امکان
    اتصال پیاده‌سازی‌های هر ابری فراهم شود.
  - پیاده‌سازی کنترل‌کننده‌های مشترکی که در این سند برجسته شده‌اند (Node، Route و Service)،
    به‌همراه بخشی از چارچوب‌بندی و رابط مشترک cloudprovider، بخشی از هستهٔ کوبرنتیز است.
    پیاده‌سازی‌های مختص ارائه‌دهندگان ابری خارج از هستهٔ کوبرنتیز قرار دارند و
    رابط `CloudProvider` را پیاده‌سازی می‌کنند.
  - برای اطلاعات بیشتر دربارهٔ توسعهٔ افزونه‌ها،
    به [توسعهٔ Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/) مراجعه کنید.
