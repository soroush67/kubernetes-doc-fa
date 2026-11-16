---
title: مدیر کنترل‌کننده ابری
content_type: concept
weight: 40
theme_lock: light
---

<!-- overview -->

{{< feature-state state="beta" for_k8s_version="v1.11" >}}

فناوری‌های زیرساخت ابری امکان اجرای کوبرنتیز را روی ابرهای عمومی، خصوصی و ترکیبی فراهم می‌کنند. رویکرد کوبرنتیز زیرساختی خودکار و مبتنی بر API است که در آن مؤلفه‌ها به یکدیگر وابستگی تنگاتنگ ندارند.

{{< glossary_definition term_id="cloud-controller-manager" length="all" prepend="The cloud-controller-manager is">}}

ساختار مدیر کنترل‌کننده ابری (cloud-controller-manager) بر پایه سازوکار افزونه‌ای (plugin) طراحی شده است. با این سازوکار، ارائه‌دهندگان مختلف خدمات ابری می‌توانند پلتفرم‌های خود را با کوبرنتیز یکپارچه کنند.

<!-- body -->

## طراحی

![مؤلفه‌های کوبرنتیز](/images/docs/components-of-kubernetes.svg)

مدیر کنترل‌کننده ابری به‌صورت مجموعه‌ای تکثیرشده از پردازه‌ها در control plane اجرا می‌شود (این پردازه‌ها معمولاً کانتینرهایی درون Podها هستند). هر نمونه از cloud-controller-manager چندین {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} را در قالب یک پردازه واحد پیاده‌سازی می‌کند.


{{< note >}}
همچنین می‌توانید مدیر کنترل‌کننده ابری را به‌جای اجرا به‌عنوان بخشی از control plane، به‌صورت یک {{< glossary_tooltip text="افزونه" term_id="addons" >}} کوبرنتیز اجرا کنید.
{{< /note >}}

## وظایف مدیر کنترل‌کننده ابری {#functions-of-the-ccm}

کنترل‌کننده‌های درون مدیر کنترل‌کننده ابری عبارت‌اند از:

### کنترل‌کننده نود

هنگامی که سرورهای جدیدی در زیرساخت ابری شما ایجاد می‌شوند، کنترل‌کننده نود مسئول به‌روزرسانی آبجکت‌های {{< glossary_tooltip text="Node" term_id="node" >}} است. این کنترل‌کننده اطلاعات میزبان‌هایی را که در فضای اختصاصی (tenancy) شما نزد ارائه‌دهنده ابری اجرا می‌شوند به دست می‌آورد. کنترل‌کننده نود وظایف زیر را انجام می‌دهد:

1. به‌روزرسانی آبجکت Node با شناسه یکتای سرور متناظر که از API ارائه‌دهنده ابری دریافت می‌شود.
1. افزودن حاشیه‌نویسی (annotation) و برچسب به آبجکت Node با اطلاعات مختص ابر، مانند منطقه‌ای (region) که نود در آن مستقر شده است و منابعی (CPU، حافظه و غیره) که در اختیار دارد.
1. به دست آوردن نام میزبان و نشانی‌های شبکه نود.
1. بررسی سلامت نود. اگر نودی پاسخگو نباشد، این کنترل‌کننده با استفاده از API ارائه‌دهنده ابری بررسی می‌کند که آیا سرور غیرفعال، حذف یا خاتمه داده شده است یا خیر. اگر نود از ابر حذف شده باشد، کنترل‌کننده آبجکت Node را از کلاستر کوبرنتیز شما حذف می‌کند.

در برخی از پیاده‌سازی‌های ارائه‌دهندگان ابری، این وظایف میان یک کنترل‌کننده نود و یک کنترل‌کننده جداگانه برای چرخه حیات نود تقسیم می‌شود.

### کنترل‌کننده مسیر

کنترل‌کننده مسیر مسئول پیکربندی صحیح مسیرها در ابر است تا کانتینرهایی که روی نودهای مختلف کلاستر کوبرنتیز شما قرار دارند بتوانند با یکدیگر ارتباط برقرار کنند.

بسته به ارائه‌دهنده ابری، ممکن است کنترل‌کننده مسیر بلوک‌هایی از نشانی‌های IP را نیز برای شبکه Podها تخصیص دهد.

### کنترل‌کننده سرویس

{{< glossary_tooltip text="سرویس‌ها" term_id="service" >}} با مؤلفه‌های زیرساخت ابری مانند متعادل‌کننده‌های بار مدیریت‌شده، نشانی‌های IP، فیلترکردن بسته‌های شبکه و بررسی سلامت مقصد یکپارچه می‌شوند. هنگامی که یک منبع Service تعریف می‌کنید که به این مؤلفه‌ها نیاز دارد، کنترل‌کننده سرویس با APIهای ارائه‌دهنده ابری شما تعامل می‌کند تا متعادل‌کننده‌های بار و دیگر مؤلفه‌های زیرساختی را راه‌اندازی کند.

## مجوزدهی

این بخش دسترسی‌هایی را که مدیر کنترل‌کننده ابری برای انجام عملیات خود روی آبجکت‌های مختلف API نیاز دارد، به تفکیک شرح می‌دهد.

### کنترل‌کننده نود {#authorization-node-controller}

کنترل‌کننده نود فقط با آبجکت‌های Node کار می‌کند و برای خواندن و تغییر این آبجکت‌ها به دسترسی کامل نیاز دارد.

`v1/Node`:

- get
- list
- create
- update
- patch
- watch
- delete

### کنترل‌کننده مسیر {#authorization-route-controller}

کنترل‌کننده مسیر به رویداد ایجاد آبجکت‌های Node گوش می‌دهد و مسیرها را به‌درستی پیکربندی می‌کند. این کنترل‌کننده به دسترسی Get روی آبجکت‌های Node نیاز دارد.

`v1/Node`:

- get

### کنترل‌کننده سرویس {#authorization-service-controller}

کنترل‌کننده سرویس رویدادهای **create**، **update** و **delete** آبجکت‌های Service را زیر نظر می‌گیرد و سپس متعادل‌کننده‌های بار را برای آن Serviceها به‌درستی پیکربندی می‌کند.

این کنترل‌کننده برای دسترسی به Serviceها به مجوزهای **list** و **watch** نیاز دارد. برای به‌روزرسانی Serviceها نیز به مجوزهای **patch** و **update** روی زیرمنبع `status` نیاز دارد.

`v1/Service`:

- list
- get
- watch
- patch
- update

### سایر موارد {#authorization-miscellaneous}

پیاده‌سازی هسته مدیر کنترل‌کننده ابری به دسترسی برای ایجاد آبجکت‌های Event نیاز دارد. همچنین برای تضمین عملکرد امن، به دسترسی برای ایجاد ServiceAccountها نیاز دارد.

`v1/Event`:

- create
- patch
- update

`v1/ServiceAccount`:

- create

نقش ClusterRole مربوط به {{< glossary_tooltip term_id="rbac" text="RBAC" >}} برای مدیر کنترل‌کننده ابری به این شکل است:

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

* صفحه [مدیریت مدیر کنترل‌کننده ابری](/docs/tasks/administer-cluster/running-cloud-controller/#running-cloud-controller-manager)
  دستورالعمل‌هایی برای اجرا و مدیریت مدیر کنترل‌کننده ابری ارائه می‌دهد.

* برای ارتقای یک control plane با دسترس‌پذیری بالا (HA) به‌گونه‌ای که از مدیر کنترل‌کننده ابری استفاده کند، به صفحه
  [مهاجرت control plane تکثیرشده به استفاده از مدیر کنترل‌کننده ابری](/docs/tasks/administer-cluster/controller-manager-leader-migration/) مراجعه کنید.

* می‌خواهید بدانید چگونه مدیر کنترل‌کننده ابری خود را پیاده‌سازی کنید یا یک پروژه موجود را گسترش دهید؟

  - مدیر کنترل‌کننده ابری از واسط‌های Go استفاده می‌کند؛ به‌طور مشخص، واسط `CloudProvider` که در
    [`cloud.go`](https://github.com/kubernetes/cloud-provider/blob/release-1.21/cloud.go#L42-L69)
    از مخزن [kubernetes/cloud-provider](https://github.com/kubernetes/cloud-provider) تعریف شده است. این واسط امکان افزودن پیاده‌سازی‌های هر ارائه‌دهنده ابری را فراهم می‌کند.
  - پیاده‌سازی کنترل‌کننده‌های مشترکی که در این سند به آن‌ها اشاره شد (Node، Route و Service)، به همراه بخشی از چارچوب پایه و واسط مشترک cloudprovider، جزئی از هسته کوبرنتیز است.
    پیاده‌سازی‌های مختص ارائه‌دهندگان ابری خارج از هسته کوبرنتیز قرار دارند و واسط `CloudProvider` را پیاده‌سازی می‌کنند.
  - برای اطلاعات بیشتر درباره توسعه افزونه‌ها،
    به صفحه [توسعه مدیر کنترل‌کننده ابری](/docs/tasks/administer-cluster/developing-cloud-controller-manager/) مراجعه کنید.
