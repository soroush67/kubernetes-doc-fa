---
reviewers:
  - tallclair
  - dchen1107
title: Runtime Class
content_type: concept
weight: 30
hide_summary: true # Listed separately in section index
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.20" state="stable" >}}

این صفحه منبع RuntimeClass و سازوکار انتخاب runtime را شرح می‌دهد.

RuntimeClass قابلیتی برای انتخاب پیکربندی container runtime است. پیکربندی container runtime برای اجرای کانتینرهای یک Pod استفاده می‌شود.

<!-- body -->

## انگیزه

می‌توانید برای Podهای مختلف، RuntimeClass متفاوتی تعیین کنید تا توازنی میان عملکرد و امنیت برقرار شود. برای مثال، اگر بخشی از بار کاری شما به سطح بالایی از اطمینان امنیت اطلاعات نیاز دارد، می‌توانید زمان‌بندی آن Podها را طوری انتخاب کنید که در یک container runtime مبتنی بر مجازی‌سازی سخت‌افزاری اجرا شوند. در این صورت از جداسازی بیشتر runtime جایگزین بهره‌مند می‌شوید، هرچند هزینه آن مقداری سربار اضافی است.

همچنین می‌توانید از RuntimeClass برای اجرای Podهای مختلف با همان container runtime اما با تنظیمات متفاوت استفاده کنید.

## راه‌اندازی

1. پیکربندی پیاده‌سازی CRI روی نودها (وابسته به runtime)
2. ایجاد منابع RuntimeClass متناظر

### ۱. پیکربندی پیاده‌سازی CRI روی نودها

پیکربندی‌هایی که از طریق RuntimeClass در دسترس هستند به پیاده‌سازی Container Runtime Interface (CRI) وابسته‌اند. برای نحوه پیکربندی، به مستندات مربوط به پیاده‌سازی CRI خود ([در ادامه](#cri-configuration)) مراجعه کنید.

{{< note >}}
RuntimeClass به‌طور پیش‌فرض فرض می‌کند که پیکربندی نودها در سراسر کلاستر همگن است (یعنی همه نودها از نظر container runtimeها به یک شکل پیکربندی شده‌اند). برای پشتیبانی از پیکربندی‌های ناهمگن نودها، بخش [زمان‌بندی](#scheduling) را در ادامه ببینید.
{{< /note >}}

هر پیکربندی یک نام `handler` متناظر دارد که RuntimeClass به آن ارجاع می‌دهد. handler باید یک [نام برچسب DNS](/docs/concepts/overview/working-with-objects/names/#dns-label-names) معتبر باشد.

### ۲. ایجاد منابع RuntimeClass متناظر

هر یک از پیکربندی‌هایی که در گام ۱ انجام شده‌اند باید یک نام `handler` مرتبط داشته باشند که آن پیکربندی را شناسایی می‌کند. برای هر handler، یک آبجکت RuntimeClass متناظر ایجاد کنید.

منبع RuntimeClass در حال حاضر فقط دو فیلد مهم دارد: نام RuntimeClass (`metadata.name`) و handler (`handler`). تعریف آبجکت به این شکل است:

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

نام یک آبجکت RuntimeClass باید یک [نام زیردامنه DNS](/docs/concepts/overview/working-with-objects/names#dns-subdomain-names) معتبر باشد.

{{< note >}}
توصیه می‌شود عملیات نوشتن روی RuntimeClass (ایجاد/به‌روزرسانی/patch/حذف) به مدیر کلاستر محدود شود. این معمولاً به‌صورت پیش‌فرض برقرار است. برای جزئیات بیشتر، [مروری بر احراز مجوز](/docs/reference/access-authn-authz/authorization/) را ببینید.
{{< /note >}}

## نحوه استفاده

پس از پیکربندی RuntimeClassها برای کلاستر، می‌توانید برای استفاده از آن‌ها یک `runtimeClassName` در spec مربوط به Pod تعیین کنید. برای مثال:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  # ...
```

این کار به kubelet دستور می‌دهد که برای اجرای این Pod از RuntimeClass نام‌برده‌شده استفاده کند. اگر RuntimeClass نام‌برده‌شده وجود نداشته باشد یا CRI نتواند handler متناظر را اجرا کند، Pod وارد [فاز](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) پایانی `Failed` می‌شود. برای مشاهده پیام خطا، به دنبال [رویداد](/docs/tasks/debug/debug-application/debug-running-pod/) متناظر بگردید.

اگر هیچ `runtimeClassName` مشخص نشده باشد، RuntimeHandler پیش‌فرض استفاده می‌شود که معادل رفتار زمانی است که قابلیت RuntimeClass غیرفعال باشد.

### پیکربندی CRI {#cri-configuration}

برای جزئیات بیشتر درباره راه‌اندازی runtimeهای CRI، [نصب CRI](/docs/setup/production-environment/container-runtimes/) را ببینید.

#### {{< glossary_tooltip term_id="containerd" >}}

handlerهای runtime از طریق پیکربندی containerd در مسیر `/etc/containerd/config.toml` تنظیم می‌شوند. handlerهای معتبر در بخش runtimes پیکربندی می‌شوند:

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.${HANDLER_NAME}]
```

برای جزئیات بیشتر، [مستندات پیکربندی](https://github.com/containerd/containerd/blob/main/docs/cri/config.md) containerd را ببینید:

#### {{< glossary_tooltip term_id="cri-o" >}}

handlerهای runtime از طریق پیکربندی CRI-O در مسیر `/etc/crio/crio.conf` تنظیم می‌شوند. handlerهای معتبر در [جدول crio.runtime](https://github.com/cri-o/cri-o/blob/master/docs/crio.conf.5.md#crioruntime-table) پیکربندی می‌شوند:

```
[crio.runtime.runtimes.${HANDLER_NAME}]
  runtime_path = "${PATH_TO_BINARY}"
```

برای جزئیات بیشتر، [مستندات پیکربندی](https://github.com/cri-o/cri-o/blob/master/docs/crio.conf.5.md) CRI-O را ببینید.

## زمان‌بندی {#scheduling}

{{< feature-state for_k8s_version="v1.16" state="beta" >}}

با تعیین فیلد `scheduling` برای یک RuntimeClass می‌توانید محدودیت‌هایی تعیین کنید تا اطمینان یابید Podهایی که با این RuntimeClass اجرا می‌شوند روی نودهایی زمان‌بندی می‌شوند که از آن پشتیبانی می‌کنند. اگر `scheduling` تنظیم نشده باشد، فرض می‌شود که همه نودها از این RuntimeClass پشتیبانی می‌کنند.

برای اطمینان از اینکه Podها روی نودهای پشتیبانی‌کننده از یک RuntimeClass مشخص قرار می‌گیرند، آن مجموعه از نودها باید یک برچسب مشترک داشته باشند که سپس توسط فیلد `runtimeclass.scheduling.nodeSelector` انتخاب می‌شود. nodeSelector مربوط به RuntimeClass در مرحله admission با nodeSelector مربوط به Pod ادغام می‌شود، که در عمل اشتراک مجموعه نودهای انتخاب‌شده توسط هر یک را می‌گیرد. اگر تعارضی وجود داشته باشد، Pod رد می‌شود.

اگر نودهای پشتیبانی‌کننده taint شده باشند تا از اجرای Podهای سایر RuntimeClassها روی آن نود جلوگیری شود، می‌توانید `tolerations` را به RuntimeClass اضافه کنید. همانند `nodeSelector`، tolerationها نیز در مرحله admission با tolerationهای Pod ادغام می‌شوند، که در عمل اجتماع مجموعه نودهای تحمل‌شده توسط هر یک را می‌گیرد.

برای کسب اطلاعات بیشتر درباره پیکربندی انتخابگر نود (node selector) و tolerationها، [اختصاص Podها به نودها](/docs/concepts/scheduling-eviction/assign-pod-node/) را ببینید.

### سربار Pod {#pod-overhead}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

می‌توانید منابع _سربار_ (overhead) مرتبط با اجرای یک Pod را مشخص کنید. اعلام سربار به کلاستر (از جمله زمان‌بند) اجازه می‌دهد هنگام تصمیم‌گیری درباره Podها و منابع، آن را در نظر بگیرد.

سربار Pod در RuntimeClass از طریق فیلد `overhead` تعریف می‌شود. با استفاده از این فیلد می‌توانید سربار اجرای Podهایی را که از این RuntimeClass استفاده می‌کنند مشخص کنید و اطمینان یابید که این سربارها در کوبرنتیز لحاظ می‌شوند.

## {{% heading "whatsnext" %}}

- [طراحی RuntimeClass](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/585-runtime-class/README.md)
- [طراحی زمان‌بندی RuntimeClass](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/585-runtime-class/README.md#runtimeclass-scheduling)
- {{< api-reference page="node/runtime-class-v1" text="مرجع API مربوط به RuntimeClass" >}}
- درباره مفهوم [سربار Pod](/docs/concepts/scheduling-eviction/pod-overhead/) مطالعه کنید
- [طراحی قابلیت PodOverhead](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/688-pod-overhead)
