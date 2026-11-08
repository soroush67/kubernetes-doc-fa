---
content_type: "reference"
title: برچسب‌های نود که kubelet مقداردهی می‌کند
weight: 40
---

{{< glossary_tooltip text="نودهای" term_id="node" >}} کوبرنتیز از ابتدا با مجموعه‌ای استاندارد از {{< glossary_tooltip text="برچسب‌ها" term_id="label" >}} همراه هستند.

همچنین می‌توانید برچسب‌های دلخواه خود را از طریق پیکربندی kubelet یا با استفاده از API کوبرنتیز روی نودها تنظیم کنید.

## برچسب‌های از پیش تعیین‌شده

برچسب‌های از پیش تعیین‌شده‌ای که کوبرنتیز روی نودها تنظیم می‌کند عبارت‌اند از:

* [`kubernetes.io/arch`](/docs/reference/labels-annotations-taints/#kubernetes-io-arch)
* [`kubernetes.io/hostname`](/docs/reference/labels-annotations-taints/#kubernetesiohostname)
* [`kubernetes.io/os`](/docs/reference/labels-annotations-taints/#kubernetes-io-os)
* [`node.kubernetes.io/instance-type`](/docs/reference/labels-annotations-taints/#nodekubernetesioinstance-type)
  (در صورتی که kubelet از آن آگاه باشد &ndash; ممکن است کوبرنتیز اطلاعات لازم برای تنظیم این برچسب را نداشته باشد)
* [`topology.kubernetes.io/region`](/docs/reference/labels-annotations-taints/#topologykubernetesioregion)
  (در صورتی که kubelet از آن آگاه باشد &ndash; ممکن است کوبرنتیز اطلاعات لازم برای تنظیم این برچسب را نداشته باشد)
* [`topology.kubernetes.io/zone`](/docs/reference/labels-annotations-taints/#topologykubernetesiozone)
  (در صورتی که kubelet از آن آگاه باشد &ndash; ممکن است کوبرنتیز اطلاعات لازم برای تنظیم این برچسب را نداشته باشد)

{{<note>}}
مقدار این برچسب‌ها به ارائه‌دهنده ابری بستگی دارد و قابل اتکا بودن آن تضمین نمی‌شود. برای مثال، مقدار `kubernetes.io/hostname` ممکن است در برخی محیط‌ها با نام نود یکسان باشد و در محیط‌های دیگر مقداری متفاوت داشته باشد.
{{</note>}}

## {{% heading "whatsnext" %}}

- برای مشاهده فهرستی از برچسب‌های رایج، به [برچسب‌ها، حاشیه‌نویسی‌ها و taintهای شناخته‌شده](/docs/reference/labels-annotations-taints/) مراجعه کنید.
- با نحوه [افزودن برچسب به یک نود](/docs/tasks/configure-pod-container/assign-pods-nodes/#add-a-label-to-a-node) آشنا شوید.
