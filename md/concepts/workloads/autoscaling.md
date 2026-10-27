---
title: مقیاس‌گذاری خودکار بارهای کاری
description: >-
  با مقیاس‌گذاری خودکار (autoscaling) می‌توانید بارهای کاری خود را به یک شکل یا شکل دیگر به‌طور خودکار به‌روزرسانی کنید. این کار به کلاستر شما امکان می‌دهد با انعطاف و کارایی بیشتری به تغییرات تقاضای منابع واکنش نشان دهد.
content_type: concept
weight: 50
---

<!-- overview -->

در کوبرنتیز می‌توانید یک بار کاری را بسته به تقاضای فعلی منابع _مقیاس‌گذاری_ کنید.
این کار به کلاستر شما امکان می‌دهد با انعطاف و کارایی بیشتری به تغییرات تقاضای منابع واکنش نشان دهد.

هنگام مقیاس‌گذاری یک بار کاری، می‌توانید تعداد replicaهایی را که آن بار کاری مدیریت می‌کند افزایش یا کاهش دهید،
یا منابعِ در دسترس replicaها را به‌صورت درجا (in-place) تنظیم کنید.

رویکرد اول _مقیاس‌گذاری افقی_ و رویکرد دوم _مقیاس‌گذاری عمودی_ نامیده می‌شود.

بسته به مورد استفاده‌تان، روش‌های دستی و خودکاری برای مقیاس‌گذاری بارهای کاری وجود دارد.

<!-- body -->

## مقیاس‌گذاری دستی بارهای کاری

کوبرنتیز از _مقیاس‌گذاری دستی_ بارهای کاری پشتیبانی می‌کند. مقیاس‌گذاری افقی را می‌توان
با استفاده از CLI به نام `kubectl` انجام داد.
برای مقیاس‌گذاری عمودی، باید تعریف منبع (resource definition) بار کاری خود را _patch_ کنید.

برای مشاهده مثال‌هایی از هر دو راهبرد، موارد زیر را ببینید.

- **مقیاس‌گذاری افقی**: [اجرای چند نمونه از برنامه شما](/docs/tutorials/kubernetes-basics/scale/scale-intro/)
- **مقیاس‌گذاری عمودی**: [تغییر اندازه منابع CPU و حافظه اختصاص‌یافته به کانتینرها](/docs/tasks/configure-pod-container/resize-container-resources)

## مقیاس‌گذاری خودکار بارهای کاری

کوبرنتیز همچنین از _مقیاس‌گذاری خودکار_ بارهای کاری پشتیبانی می‌کند که محور اصلی این صفحه است.

مفهوم _مقیاس‌گذاری خودکار_ (Autoscaling) در کوبرنتیز به توانایی به‌روزرسانی خودکار
آبجکتی اشاره دارد که مجموعه‌ای از Podها را مدیریت می‌کند (برای مثال یک
{{< glossary_tooltip text="Deployment" term_id="deployment" >}}).

### مقیاس‌گذاری افقی بارهای کاری

در کوبرنتیز می‌توانید با استفاده از [HorizontalPodAutoscaler](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) (HPA) یک بار کاری را به‌طور خودکار و افقی مقیاس‌گذاری کنید.

این قابلیت به‌صورت یک منبع API کوبرنتیز و یک {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}}
پیاده‌سازی شده است و به‌طور دوره‌ای تعداد {{< glossary_tooltip text="replicaهای" term_id="replica" >}}
یک بار کاری را تنظیم می‌کند تا با میزان مصرف مشاهده‌شده منابع، مانند مصرف CPU یا حافظه، مطابقت داشته باشد.

یک [آموزش گام‌به‌گام](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough) برای پیکربندی HorizontalPodAutoscaler برای یک Deployment وجود دارد.

### مقیاس‌گذاری عمودی بارهای کاری

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

می‌توانید با استفاده از [VerticalPodAutoscaler](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) (VPA) یک بار کاری را به‌طور خودکار و عمودی مقیاس‌گذاری کنید.
برخلاف HPA، VPA به‌طور پیش‌فرض همراه کوبرنتیز نیست، بلکه یک افزونه (add-on) است که ممکن است شما یا مدیر کلاستر پیش از استفاده از آن لازم باشد آن را مستقر کنید.

پس از نصب، این افزونه به شما امکان می‌دهد برای بارهای کاری خود
{{< glossary_tooltip text="CustomResourceDefinitionها" term_id="customresourcedefinition" >}}
(CRDها) ایجاد کنید که تعیین می‌کنند منابع replicaهای مدیریت‌شده _چگونه_ و _چه زمانی_ مقیاس‌گذاری شوند.

{{< note >}}
برای اینکه VPA کار کند، باید [Metrics Server](https://github.com/kubernetes-sigs/metrics-server)
روی کلاستر شما نصب شده باشد.
{{< /note >}}

#### مقیاس‌گذاری عمودی درجای Pod

{{< feature-state feature_gate_name="InPlacePodVerticalScaling" >}}

از کوبرنتیز {{< skew currentVersion >}}، VPA از تغییر اندازه درجای Podها پشتیبانی نمی‌کند،
اما کار روی این یکپارچه‌سازی در حال انجام است.
برای تغییر اندازه دستی Podها به‌صورت درجا، [تغییر اندازه درجای منابع کانتینر](/docs/tasks/configure-pod-container/resize-container-resources/) را ببینید.

### مقیاس‌گذاری خودکار بر اساس اندازه کلاستر

برای بارهای کاری که باید بر اساس اندازه کلاستر مقیاس‌گذاری شوند (برای مثال
`cluster-dns` یا سایر اجزای سیستمی)، می‌توانید از
[_Cluster Proportional Autoscaler_](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler)
استفاده کنید.
درست مانند VPA، این ابزار بخشی از هسته کوبرنتیز نیست و به‌عنوان یک پروژه مستقل
در GitHub میزبانی می‌شود.

Cluster Proportional Autoscaler تعداد {{< glossary_tooltip text="نودهای" term_id="node" >}} قابل زمان‌بندی
و هسته‌ها را زیر نظر می‌گیرد و تعداد replicaهای بار کاری هدف را بر همین اساس مقیاس‌گذاری می‌کند.

اگر تعداد replicaها باید ثابت بماند، می‌توانید بارهای کاری خود را بر اساس اندازه کلاستر به‌صورت عمودی مقیاس‌گذاری کنید؛ برای این کار از
[_Cluster Proportional Vertical Autoscaler_](https://github.com/kubernetes-sigs/cluster-proportional-vertical-autoscaler)
استفاده کنید.
این پروژه **در حال حاضر در مرحله بتا** است و در GitHub در دسترس است.

در حالی که Cluster Proportional Autoscaler تعداد replicaهای یک بار کاری را مقیاس‌گذاری می‌کند،
Cluster Proportional Vertical Autoscaler درخواست‌های منابع (resource requests) یک بار کاری
(برای مثال یک Deployment یا DaemonSet) را بر اساس تعداد نودها و/یا هسته‌ها در کلاستر تنظیم می‌کند.

### مقیاس‌گذاری خودکار مبتنی بر رویداد

همچنین می‌توان بارهای کاری را بر اساس رویدادها مقیاس‌گذاری کرد، برای مثال با استفاده از
[_Kubernetes Event Driven Autoscaler_ (**KEDA**)](https://keda.sh/).

KEDA یک پروژه فارغ‌التحصیل‌شده (graduated) در CNCF است که به شما امکان می‌دهد بارهای کاری خود را بر اساس تعداد
رویدادهایی که باید پردازش شوند، مثلاً تعداد پیام‌های موجود در یک صف، مقیاس‌گذاری کنید. طیف
گسترده‌ای از آداپتورها برای منابع رویداد مختلف وجود دارد که می‌توانید از میان آن‌ها انتخاب کنید.

### مقیاس‌گذاری خودکار بر اساس زمان‌بندی

راهبرد دیگر برای مقیاس‌گذاری بارهای کاری، **زمان‌بندی** عملیات مقیاس‌گذاری است، برای مثال به‌منظور
کاهش مصرف منابع در ساعات کم‌باری.

مشابه مقیاس‌گذاری خودکار مبتنی بر رویداد، چنین رفتاری را می‌توان با استفاده از KEDA به‌همراه
[`Cron` scaler](https://keda.sh/docs/latest/scalers/cron/) آن به دست آورد.
`Cron` scaler به شما امکان می‌دهد زمان‌بندی‌ها (و مناطق زمانی) را برای افزایش یا کاهش مقیاس بارهای کاری خود تعریف کنید.

## مقیاس‌گذاری زیرساخت کلاستر

اگر مقیاس‌گذاری بارهای کاری برای رفع نیازهای شما کافی نیست، می‌توانید خود زیرساخت کلاستر را نیز مقیاس‌گذاری کنید.

مقیاس‌گذاری زیرساخت کلاستر معمولاً به معنای افزودن یا حذف {{< glossary_tooltip text="نودها" term_id="node" >}} است.
برای اطلاعات بیشتر، [مقیاس‌گذاری خودکار نود](/docs/concepts/cluster-administration/node-autoscaling/) را مطالعه کنید.

## {{% heading "whatsnext" %}}

- درباره مقیاس‌گذاری افقی بیشتر بیاموزید
  - [مقیاس‌گذاری یک StatefulSet](/docs/tasks/run-application/scale-stateful-set/)
  - [آموزش گام‌به‌گام HorizontalPodAutoscaler](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
- [تغییر اندازه درجای منابع کانتینر](/docs/tasks/configure-pod-container/resize-container-resources/)
- [مقیاس‌گذاری خودکار سرویس DNS در یک کلاستر](/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)
- درباره [مقیاس‌گذاری خودکار نود](/docs/concepts/cluster-administration/node-autoscaling/) بیاموزید
