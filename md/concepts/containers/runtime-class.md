---
reviewers:
  - tallclair
  - dchen1107
title: کلاس محیط اجرا (Runtime Class)
content_type: concept
weight: 30
hide_summary: true # Listed separately in section index
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

این صفحه منبع RuntimeClass و سازوکار انتخاب محیط اجرا را شرح می‌دهد.

قابلیت RuntimeClass برای انتخاب پیکربندی محیط اجرای کانتینر به کار می‌رود. از این پیکربندی برای اجرای کانتینرهای یک Pod استفاده می‌شود.

<!-- body -->

## انگیزه

می‌توانید برای Podهای مختلف، RuntimeClassهای متفاوتی تعیین کنید تا میان کارایی و امنیت توازن برقرار شود. برای مثال، اگر بخشی از بار کاری شما به سطح بالایی از تضمین امنیت اطلاعات نیاز داشته باشد، ممکن است بخواهید آن Podها را طوری زمان‌بندی کنید که در محیط اجرای کانتینری اجرا شوند که از مجازی‌سازی سخت‌افزاری بهره می‌برد. در این صورت از جداسازی بیشترِ این محیط اجرای جایگزین بهره‌مند می‌شوید، هرچند بهای آن مقداری سربار اضافی است.

همچنین می‌توانید از RuntimeClass استفاده کنید تا Podهای مختلف را با یک محیط اجرای کانتینر یکسان، اما با تنظیمات متفاوت اجرا کنید.

## راه‌اندازی

1. پیاده‌سازی CRI را روی نودها پیکربندی کنید (وابسته به محیط اجرا)
2. منابع RuntimeClass متناظر را ایجاد کنید

### 1. پیکربندی پیاده‌سازی CRI روی نودها

پیکربندی‌هایی که از طریق RuntimeClass در دسترس‌اند، به پیاده‌سازی رابط محیط اجرای کانتینر (Container Runtime Interface یا CRI) وابسته هستند. برای آگاهی از نحوهٔ پیکربندی، مستندات مربوط به پیاده‌سازی CRI خود را ([در ادامه](#cri-configuration)) ببینید.

{{< note >}}
به‌طور پیش‌فرض، RuntimeClass فرض می‌کند که پیکربندی نودها در سراسر کلاستر یکسان است؛ یعنی همهٔ نودها از نظر محیط‌های اجرای کانتینر به یک شکل پیکربندی شده‌اند. برای پشتیبانی از پیکربندی‌های ناهمگون نودها، بخش [زمان‌بندی](#scheduling) را در ادامه ببینید.
{{< /note >}}

هر پیکربندی یک نام `handler` متناظر دارد که RuntimeClass به آن ارجاع می‌دهد. این handler باید یک [نام برچسب DNS](/docs/concepts/overview/working-with-objects/names/#dns-label-names) معتبر باشد.

### 2. ایجاد منابع RuntimeClass متناظر

هر یک از پیکربندی‌هایی که در مرحلهٔ ۱ راه‌اندازی شده‌اند، باید یک نام `handler` مرتبط داشته باشد که آن پیکربندی را مشخص می‌کند. برای هر handler، یک آبجکت RuntimeClass متناظر ایجاد کنید.

منبع RuntimeClass در حال حاضر تنها ۲ فیلد مهم دارد: نام RuntimeClass (`metadata.name`) و handler (`handler`). تعریف این آبجکت به شکل زیر است:

```yaml
# RuntimeClass is defined in the node.k8s.io API group
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  # The name the RuntimeClass will be referenced by.
  # RuntimeClass is a non-namespaced resource.
  name: myclass 
# The name of the corresponding CRI configuration
handler: myconfiguration 
```

نام هر آبجکت RuntimeClass باید یک
[نام زیردامنهٔ DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

{{< note >}}
توصیه می‌شود عملیات نوشتن روی RuntimeClass (ایجاد/به‌روزرسانی/وصله/حذف) فقط به مدیر کلاستر محدود شود. این وضعیت معمولاً پیش‌فرض است. برای جزئیات بیشتر،
[مروری بر مجوزدهی](/docs/reference/access-authn-authz/authorization/) را ببینید.
{{< /note >}}

## نحوهٔ استفاده

پس از پیکربندی RuntimeClassها برای کلاستر، می‌توانید برای استفاده از آن‌ها، فیلد `runtimeClassName` را در مشخصات Pod تعیین کنید. برای مثال:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  # ...
```

با این کار به kubelet دستور داده می‌شود که برای اجرای این Pod از RuntimeClass نام‌برده استفاده کند. اگر RuntimeClass نام‌برده وجود نداشته باشد یا CRI نتواند handler متناظر را اجرا کند، Pod وارد [فاز](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) پایانی `Failed` می‌شود. برای مشاهدهٔ پیام خطا، به دنبال [رویداد](/docs/tasks/debug/debug-application/debug-running-pod/) متناظر بگردید.

اگر هیچ `runtimeClassName` تعیین نشود، از RuntimeHandler پیش‌فرض استفاده می‌شود که رفتاری معادل حالت غیرفعال بودن قابلیت RuntimeClass دارد.

### پیکربندی CRI

برای جزئیات بیشتر دربارهٔ راه‌اندازی محیط‌های اجرای CRI، [نصب CRI](/docs/setup/production-environment/container-runtimes/) را ببینید.

#### {{< glossary_tooltip term_id="containerd" >}}

handlerهای محیط اجرا از طریق فایل پیکربندی containerd در مسیر
`/etc/containerd/config.toml` پیکربندی می‌شوند. handlerهای معتبر در بخش runtimes پیکربندی می‌شوند:

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.${HANDLER_NAME}]
```

برای جزئیات بیشتر، [مستندات پیکربندی](https://github.com/containerd/containerd/blob/main/docs/cri/config.md) containerd را ببینید:

#### {{< glossary_tooltip term_id="cri-o" >}}

handlerهای محیط اجرا از طریق فایل پیکربندی CRI-O در مسیر `/etc/crio/crio.conf` پیکربندی می‌شوند. handlerهای معتبر در
[جدول crio.runtime](https://github.com/cri-o/cri-o/blob/master/docs/crio.conf.5.md#crioruntime-table) پیکربندی می‌شوند:

```
[crio.runtime.runtimes.${HANDLER_NAME}]
  runtime_path = "${PATH_TO_BINARY}"
```

برای جزئیات بیشتر، [مستندات پیکربندی](https://github.com/cri-o/cri-o/blob/master/docs/crio.conf.5.md) CRI-O را ببینید.

## زمان‌بندی

{{< feature-state for_k8s_version="v1.16" state="beta" >}}

با تعیین فیلد `scheduling` برای یک RuntimeClass، می‌توانید محدودیت‌هایی تنظیم کنید تا Podهایی که با این RuntimeClass اجرا می‌شوند، روی نودهایی زمان‌بندی شوند که از آن پشتیبانی می‌کنند. اگر `scheduling` تنظیم نشده باشد، فرض بر این است که همهٔ نودها از این RuntimeClass پشتیبانی می‌کنند.

برای اطمینان از اینکه Podها روی نودهای پشتیبانی‌کننده از یک RuntimeClass مشخص قرار می‌گیرند، آن مجموعه از نودها باید یک برچسب مشترک داشته باشند که سپس با فیلد `runtimeclass.scheduling.nodeSelector` انتخاب می‌شود. در مرحلهٔ پذیرش (admission)، nodeSelector مربوط به RuntimeClass با nodeSelector مربوط به Pod ادغام می‌شود؛ در نتیجه، اشتراک مجموعهٔ نودهایی که هر یک انتخاب می‌کنند در نظر گرفته می‌شود. اگر تعارضی وجود داشته باشد، Pod رد می‌شود.

اگر روی نودهای پشتیبانی‌کننده taint اعمال شده باشد تا از اجرای Podهای دارای RuntimeClass دیگر روی آن‌ها جلوگیری شود، می‌توانید `tolerations` را به RuntimeClass اضافه کنید. همانند `nodeSelector`، این tolerationها نیز در مرحلهٔ پذیرش با tolerationهای Pod ادغام می‌شوند؛ در نتیجه، اجتماع مجموعهٔ نودهایی که هر یک تحمل می‌کنند در نظر گرفته می‌شود.

برای آشنایی بیشتر با پیکربندی انتخابگر (selector) نود و tolerationها،
[تخصیص Podها به نودها](/docs/concepts/scheduling-eviction/assign-pod-node/) را ببینید.

### سربار Pod

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

می‌توانید منابع _سربار_ مرتبط با اجرای یک Pod را مشخص کنید. با اعلام سربار، کلاستر (از جمله زمان‌بند) می‌تواند هنگام تصمیم‌گیری دربارهٔ Podها و منابع، آن را به حساب آورد.

سربار Pod در RuntimeClass از طریق فیلد `overhead` تعریف می‌شود. با استفاده از این فیلد، می‌توانید سربار اجرای Podهایی را که از این RuntimeClass استفاده می‌کنند مشخص کنید و اطمینان یابید که این سربارها در کوبرنتیز به حساب آورده می‌شوند.

## {{% heading "whatsnext" %}}

- [طراحی RuntimeClass](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/585-runtime-class/README.md)
- [طراحی زمان‌بندی RuntimeClass](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/585-runtime-class/README.md#runtimeclass-scheduling)
- {{< api-reference page="node/runtime-class-v1" text="مرجع API برای RuntimeClass" >}}
- دربارهٔ مفهوم [سربار Pod](/docs/concepts/scheduling-eviction/pod-overhead/) بخوانید
- [طراحی قابلیت PodOverhead](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/688-pod-overhead)
