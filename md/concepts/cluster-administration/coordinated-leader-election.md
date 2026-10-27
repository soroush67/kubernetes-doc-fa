---
reviewers:
- jpbetz
title: انتخاب رهبر هماهنگ
content_type: concept
weight: 200
---

<!-- overview -->

{{< feature-state feature_gate_name="CoordinatedLeaderElection" >}}

کوبرنتیز {{< skew currentVersion >}} شامل یک قابلیت بتا است که به اجزای {{<
glossary_tooltip text="control plane" term_id="control-plane" >}} اجازه می‌دهد
از طریق _انتخاب رهبر هماهنگ_ (coordinated leader election) به‌طور قطعی یک رهبر را برگزینند.
این قابلیت برای برآورده‌کردن محدودیت‌های اختلاف نسخه (version skew) کوبرنتیز در طول ارتقای کلاستر سودمند است.
در حال حاضر، تنها راهبرد انتخاب داخلی `OldestEmulationVersion` است
که رهبری با پایین‌ترین نسخهٔ شبیه‌سازی را ترجیح می‌دهد و پس از آن، نسخهٔ باینری
و سپس مُهر زمانی ایجاد را ملاک قرار می‌دهد.

## فعال‌سازی انتخاب رهبر هماهنگ

هنگام راه‌اندازی {{< glossary_tooltip text="سرور API"
term_id="kube-apiserver" >}}، اطمینان حاصل کنید که [feature
gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `CoordinatedLeaderElection` فعال است
و گروه API با نام `coordination.k8s.io/v1beta1` نیز
فعال باشد.

این کار را می‌توان با تنظیم پرچم‌های `--feature-gates="CoordinatedLeaderElection=true"` و
`--runtime-config="coordination.k8s.io/v1beta1=true"` انجام داد.

## پیکربندی مؤلفه‌ها

به شرط آنکه feature gate با نام `CoordinatedLeaderElection` را فعال کرده باشید _و_
گروه API با نام `coordination.k8s.io/v1beta1` نیز فعال باشد، اجزای سازگار control plane
به‌طور خودکار و در صورت نیاز از APIهای LeaseCandidate و Lease برای انتخاب رهبر
استفاده می‌کنند.

در کوبرنتیز {{< skew currentVersion >}}، دو مؤلفه از control plane
(kube-controller-manager و kube-scheduler) هنگامی که feature gate و گروه API فعال باشند،
به‌طور خودکار از انتخاب رهبر هماهنگ استفاده می‌کنند.

## انتخاب رهبر برای اجزای کوبرنتیز

کوبرنتیز از [API مربوط به Lease](/docs/concepts/architecture/leases/) برای انجام انتخاب رهبر میان چندین نمونه از یک مؤلفهٔ یکسان control plane، مانند `kube-controller-manager` یا `kube-scheduler`، در یک کلاستر با دسترس‌پذیری بالا استفاده می‌کند.

یک [Lease](/docs/concepts/architecture/leases/) همچون یک قفل توزیع‌شدهٔ سبک عمل می‌کند که توسط [سرور API کوبرنتیز](/docs/reference/command-line-tools-reference/kube-apiserver/) ذخیره می‌شود.
همهٔ نمونه‌های در حال اجرای یک مؤلفه، آبجکت Lease مربوط را پایش می‌کنند یا به‌طور دوره‌ای می‌خوانند
تا تعیین کنند کدام نمونه در حال حاضر نقش رهبر را ایفا می‌کند.

[API مربوط به Lease](/docs/reference/kubernetes-api/cluster-resources/lease-v1/) فیلدهایی
مانند موارد زیر را تعریف می‌کند:

`holderIdentity`
: هویت رهبر فعلی (برای نمونه: نام پاد یا رشته‌ای مبتنی بر نام میزبان).

`acquireTime`
: مُهر زمانی به دست آوردن رهبری.

`renewTime`
: مُهر زمانی آخرین تمدید توسط رهبر.

`leaseDurationSeconds`
: مدت اعتبار lease (نامزدها باید به همین اندازه به‌علاوهٔ یک مهلت کوتاه صبر کنند و سپس برای به دست آوردن یک lease منقضی‌شده تلاش کنند).

`leaseTransitions`
: شمارنده‌ای که نشان می‌دهد رهبری چند بار دست‌به‌دست شده است.

این فیلدها نشان می‌دهند کدام نمونه رهبری را در اختیار دارد و این رهبری تا چه مدت معتبر باقی می‌ماند.

هنگامی که [Lease](/docs/concepts/architecture/leases/) وجود نداشته باشد یا منقضی شده باشد (زمان فعلی > `renewTime` + `leaseDurationSeconds`)، نمونه‌های نامزد تلاش می‌کنند Lease را با هویت خود به‌روزرسانی کنند. کوبرنتیز از طریق `resourceVersion` آبجکت، به _کنترل هم‌روندی خوش‌بینانه_ (optimistic concurrency control) متکی است: به دلیل ناهمخوانی نسخه در تلاش‌های هم‌زمان، تنها یک به‌روزرسانی موفق می‌شود. نمونه‌ای که به‌روزرسانی‌اش پذیرفته شود، _رهبر_ می‌شود.

کوبرنتیز از API مربوط به [LeaseCandidate](/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/)
برای مدیریت انتخاب‌های رهبر استفاده می‌کند. اجزای control plane مانند `kube-controller-manager` و `kube-scheduler` با ایجاد آبجکت‌های LeaseCandidate نقش خود را به‌عنوان نامزد ثبت می‌کنند؛ این آبجکت‌ها همهٔ نمونه‌هایی را که برای رهبری رقابت می‌کنند دنبال می‌کنند و فراداده‌هایی شامل هویت نامزد، نسخهٔ باینری و نسخهٔ شبیه‌سازی آن را در خود دارند.

در طول یک انتخاب، نامزدها از طریق یک [Lease](/docs/concepts/architecture/leases/) مشترک هماهنگ می‌شوند.
control plane کوبرنتیز تضمین می‌کند که تنها یک نامزد با موفقیت [Lease](/docs/concepts/architecture/leases/) را به دست آورد و نقش _رهبر_ را بر عهده بگیرد، در حالی که سایرین به‌عنوان پیرو باقی می‌مانند. اگر _رهبر_ فعلی نتواند [Lease](/docs/concepts/architecture/leases/) را در مهلت زمانی تعیین‌شده تمدید کند، نامزدهای باقی‌مانده برای به دست آوردن رهبری رقابت می‌کنند و یک _رهبر_ جدید انتخاب می‌کنند.

رهبر پس از انتخاب‌شدن، Lease خود را با به‌روزرسانی فیلد `renewTime` به‌طور دوره‌ای تمدید می‌کند
(برای نمونه، تمدید را هر `leaseDurationSeconds` ÷ 2 انجام می‌دهد تا هنگامی که [Lease](/docs/concepts/architecture/leases/) در آستانهٔ انقضاست، از تعارض جلوگیری شود).
تا زمانی که تمدیدها پیش از انقضای lease انجام شوند، نمونهٔ رهبر فعلی رهبری را حفظ می‌کند.
اگر رهبر از کار بیفتد، دسترس‌ناپذیر شود یا تمدید Lease را متوقف کند، آن Lease منقضی می‌شود. سایر نمونه‌های سالم Lease منقضی‌شده را تشخیص می‌دهند و برای یک انتخاب جدید تلاش می‌کنند.

این سازوکار تضمین می‌کند که اگرچه ممکن است برای پایداری و بازیابی، چندین نسخهٔ تکثیرشده از یک مؤلفه در حال اجرا باشند، _در هر لحظه تنها یک نمونه به‌طور فعال وظایف کنترلی را انجام می‌دهد_، در حالی که سایرین در حالت آماده‌به‌کار باقی می‌مانند، Lease را پایش می‌کنند و آماده‌اند در صورت نیاز به‌سرعت مسئولیت را بر عهده بگیرند.
