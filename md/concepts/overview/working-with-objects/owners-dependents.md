---
title: مالکان و وابسته‌ها
content_type: concept
weight: 90
---

<!-- overview -->

در کوبرنتیز، برخی {{< glossary_tooltip text="آبجکت‌ها" term_id="object" >}}
*مالک* آبجکت‌های دیگر هستند. برای مثال، یک
{{<glossary_tooltip text="ReplicaSet" term_id="replica-set">}} مالک
مجموعه‌ای از پادهاست. این آبجکت‌های تحت مالکیت، *وابسته‌های* (dependents) مالک خود هستند.

مالکیت با سازوکار [برچسب‌ها و انتخابگرها](/docs/concepts/overview/working-with-objects/labels/)
که برخی منابع نیز از آن استفاده می‌کنند متفاوت است. برای مثال، Serviceای را در نظر بگیرید که
آبجکت‌های `EndpointSlice` ایجاد می‌کند. Service از {{<glossary_tooltip text="برچسب‌ها" term_id="label">}} استفاده می‌کند تا control plane بتواند
تعیین کند کدام آبجکت‌های `EndpointSlice` برای آن Service استفاده می‌شوند. علاوه
بر برچسب‌ها، هر `EndpointSlice` که از طرف یک Service مدیریت می‌شود،
یک ارجاع مالک (owner reference) دارد. ارجاع‌های مالک به بخش‌های مختلف کوبرنتیز کمک می‌کنند از
دخالت در آبجکت‌هایی که کنترلشان را بر عهده ندارند پرهیز کنند.

## ارجاع‌های مالک در مشخصات آبجکت

آبجکت‌های وابسته یک فیلد `metadata.ownerReferences` دارند که به
آبجکت مالکشان ارجاع می‌دهد. یک ارجاع مالک معتبر شامل نام آبجکت و یک {{<glossary_tooltip text="UID" term_id="uid">}} 
درون همان {{<glossary_tooltip text="فضای نام" term_id="namespace">}} آبجکت وابسته است. کوبرنتیز مقدار
این فیلد را به‌طور خودکار برای آبجکت‌هایی تنظیم می‌کند که وابسته‌های آبجکت‌های دیگری مانند
ReplicaSetها، DaemonSetها، Deploymentها، Jobها و CronJobها و ReplicationControllerها هستند.
همچنین می‌توانید این روابط را با تغییر مقدار
این فیلد به‌صورت دستی پیکربندی کنید. با این حال، معمولاً نیازی به این کار ندارید و می‌توانید اجازه دهید کوبرنتیز
روابط را به‌طور خودکار مدیریت کند.

آبجکت‌های وابسته همچنین یک فیلد `ownerReferences.blockOwnerDeletion` دارند که
یک مقدار بولی می‌پذیرد و کنترل می‌کند که آیا وابسته‌های مشخصی می‌توانند جلوی حذف آبجکت مالک خود
توسط جمع‌آوری زباله (garbage collection) را بگیرند یا نه. کوبرنتیز این
فیلد را به‌طور خودکار روی `true` تنظیم می‌کند اگر یک {{<glossary_tooltip text="کنترل‌کننده" term_id="controller">}} 
(برای مثال، کنترل‌کنندهٔ Deployment) مقدار فیلد
`metadata.ownerReferences` را تنظیم کند. همچنین می‌توانید مقدار فیلد
`blockOwnerDeletion` را به‌صورت دستی تنظیم کنید تا کنترل کنید کدام وابسته‌ها جلوی
جمع‌آوری زباله را می‌گیرند.

یک admission controller کوبرنتیز، دسترسی کاربر برای تغییر این فیلد در
منابع وابسته را بر اساس مجوزهای حذف مالک کنترل می‌کند. این کنترل
مانع می‌شود که کاربران غیرمجاز حذف آبجکت مالک را به تأخیر بیندازند.

{{< note >}}
ارجاع‌های مالک میان فضاهای نام مختلف بنا به طراحی مجاز نیستند.
وابسته‌های وابسته به فضای نام می‌توانند مالکانی با محدودهٔ کلاستر یا وابسته به فضای نام مشخص کنند.
یک مالک وابسته به فضای نام **باید** در همان فضای نام وابسته وجود داشته باشد.
اگر چنین نباشد، ارجاع مالک غایب تلقی می‌شود و وابسته
پس از تأیید غیبت همهٔ مالکان، مشمول حذف می‌شود.

وابسته‌های با محدودهٔ کلاستر فقط می‌توانند مالکانی با محدودهٔ کلاستر مشخص کنند.
در v1.20 و بالاتر، اگر یک وابستهٔ با محدودهٔ کلاستر یک kind وابسته به فضای نام را به‌عنوان مالک مشخص کند،
چنین تلقی می‌شود که ارجاع مالک غیرقابل حل دارد و نمی‌توان آن را با جمع‌آوری زباله حذف کرد.

در v1.20 و بالاتر، اگر جمع‌آورندهٔ زباله یک `ownerReference` نامعتبر میان فضاهای نام،
یا یک وابستهٔ با محدودهٔ کلاستر با `ownerReference`ای که به یک kind وابسته به فضای نام ارجاع می‌دهد را تشخیص دهد، یک Event هشدار 
با reason برابر `OwnerRefInvalidNamespace` و `involvedObject` برابر وابستهٔ نامعتبر گزارش می‌شود.
می‌توانید با اجرای
`kubectl get events -A --field-selector=reason=OwnerRefInvalidNamespace` وجود این نوع Event را بررسی کنید.
{{< /note >}}

## مالکیت و finalizerها

هنگامی که به کوبرنتیز می‌گویید منبعی را حذف کند، سرور API به
کنترل‌کنندهٔ مدیریت‌کننده اجازه می‌دهد هر [قاعدهٔ finalizer](/docs/concepts/overview/working-with-objects/finalizers/)
مربوط به آن منبع را پردازش کند. {{<glossary_tooltip text="Finalizerها" term_id="finalizer">}}
از حذف تصادفی منابعی که کلاستر شما ممکن است هنوز برای عملکرد صحیح
به آن‌ها نیاز داشته باشد جلوگیری می‌کنند. برای مثال، اگر بخواهید یک [PersistentVolume](/docs/concepts/storage/persistent-volumes/) را که هنوز
توسط یک Pod در حال استفاده است حذف کنید، حذف بلافاصله انجام نمی‌شود، زیرا
`PersistentVolume` دارای finalizer ‏`kubernetes.io/pv-protection` است.
در عوض، [حجم](/docs/concepts/storage/volumes/) در وضعیت `Terminating` باقی می‌ماند تا کوبرنتیز
finalizer را پاک کند، که فقط پس از آنکه `PersistentVolume` دیگر
به یک Pod متصل نباشد رخ می‌دهد. 

کوبرنتیز همچنین هنگامی که از
[حذف آبشاری foreground یا orphan](/docs/concepts/architecture/garbage-collection/#cascading-deletion) استفاده می‌کنید، finalizerهایی به منبع مالک اضافه می‌کند.
در حذف foreground، finalizer ‏`foreground` را اضافه می‌کند تا
کنترل‌کننده پیش از حذف مالک، منابع وابسته‌ای را که
`ownerReferences.blockOwnerDeletion=true` دارند حذف کند. اگر
سیاست حذف orphan را مشخص کنید، کوبرنتیز finalizer ‏`orphan` را اضافه می‌کند تا
کنترل‌کننده پس از حذف آبجکت مالک، منابع وابسته را نادیده بگیرد. 

## {{% heading "whatsnext" %}}

* دربارهٔ [finalizerهای کوبرنتیز](/docs/concepts/overview/working-with-objects/finalizers/) بیشتر بیاموزید.
* دربارهٔ [جمع‌آوری زباله](/docs/concepts/architecture/garbage-collection) بیاموزید.
* مرجع API مربوط به [فرادادهٔ آبجکت](/docs/reference/kubernetes-api/common-definitions/object-meta/#System) را بخوانید.
