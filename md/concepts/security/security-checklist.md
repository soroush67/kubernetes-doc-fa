---
title: فهرست بررسی امنیتی
description: >
  فهرست بررسی پایه برای اطمینان از امنیت در کلاسترهای کوبرنتیز.
content_type: concept
weight: 100
---

<!-- overview -->

هدف این فهرست بررسی ارائه‌ی فهرستی پایه از راهنمایی‌ها همراه با پیوند به مستندات جامع‌تر درباره‌ی هر موضوع است. این فهرست ادعای جامع بودن ندارد و قرار است به‌مرور تکامل یابد.

درباره‌ی نحوه‌ی خواندن و استفاده از این سند:

- ترتیب موضوعات بیانگر ترتیب اولویت نیست.
- برخی از موارد فهرست بررسی در پاراگراف زیر فهرستِ هر بخش به‌تفصیل توضیح داده شده‌اند.

{{< caution >}}
فهرست‌های بررسی به‌تنهایی برای دستیابی به وضعیت امنیتی مطلوب **کافی نیستند**. وضعیت امنیتی مطلوب نیازمند توجه و بهبود مستمر است، اما یک فهرست بررسی می‌تواند نخستین گام در مسیر بی‌پایان آمادگی امنیتی باشد. برخی از توصیه‌های این فهرست ممکن است برای نیازهای امنیتی خاص شما بیش‌ازحد سخت‌گیرانه یا بیش‌ازحد سهل‌گیرانه باشند. از آنجا که امنیت کوبرنتیز «یک راه‌حل برای همه» نیست، هر دسته از موارد فهرست بررسی باید بر اساس شایستگی‌های خودش ارزیابی شود.
{{< /caution >}}

<!-- body -->

## احراز هویت و مجوزدهی {#authentication-authorization}

- [ ] گروه `system:masters` پس از راه‌اندازی اولیه (bootstrapping) برای احراز هویت کاربران یا مؤلفه‌ها استفاده نمی‌شود.
- [ ] kube-controller-manager با گزینه‌ی `--use-service-account-credentials` فعال اجرا می‌شود.
- [ ] گواهی ریشه محافظت می‌شود (یا یک CA آفلاین، یا یک CA آنلاین مدیریت‌شده با کنترل‌های دسترسی مؤثر).
- [ ] گواهی‌های میانی و نهایی (leaf) تاریخ انقضایی دارند که بیش از ۳ سال در آینده نیست.
- [ ] فرایندی برای بازبینی دوره‌ای دسترسی وجود دارد و بازبینی‌ها با فاصله‌ی بیش از ۲۴ ماه انجام نمی‌شوند.
- [ ] برای راهنمایی‌های مرتبط با احراز هویت و مجوزدهی، [شیوه‌های خوب کنترل دسترسی مبتنی بر نقش (RBAC)](/docs/concepts/security/rbac-good-practices/) رعایت می‌شوند.

پس از راه‌اندازی اولیه، نه کاربران و نه مؤلفه‌ها نباید با هویت `system:masters` به API کوبرنتیز احراز هویت شوند. همچنین باید از اجرای کل kube-controller-manager با هویت `system:masters` پرهیز کرد. در واقع، `system:masters` باید فقط به‌عنوان سازوکار اضطراری (break-glass) استفاده شود، نه به‌عنوان یک کاربر مدیر.

## امنیت شبکه {#network-security}

- [ ] افزونه‌های CNI در حال استفاده از سیاست‌های شبکه (network policies) پشتیبانی می‌کنند.
- [ ] سیاست‌های شبکه‌ی ورودی (ingress) و خروجی (egress) برای همه‌ی بارهای کاری کلاستر اعمال شده‌اند.
- [ ] سیاست‌های شبکه‌ی پیش‌فرض در هر فضای نام (namespace) که همه‌ی Podها را انتخاب کرده و همه‌چیز را مسدود می‌کنند، برقرار هستند.
- [ ] در صورت لزوم، از یک service mesh برای رمزنگاری همه‌ی ارتباطات داخل کلاستر استفاده می‌شود.
- [ ] API کوبرنتیز، API مربوط به kubelet و etcd به‌صورت عمومی در اینترنت در دسترس نیستند.
- [ ] دسترسی بارهای کاری به API فراداده‌ی ابر (cloud metadata API) فیلتر می‌شود.
- [ ] استفاده از LoadBalancer و ExternalIPs محدود شده است.

تعدادی از [افزونه‌های رابط شبکه‌ی کانتینر (CNI)](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) قابلیت محدودسازی منابع شبکه‌ای را که Podها می‌توانند با آن‌ها ارتباط برقرار کنند فراهم می‌کنند. این کار معمولاً از طریق [سیاست‌های شبکه (Network Policies)](/docs/concepts/services-networking/network-policies/) انجام می‌شود که یک منبع در سطح فضای نام برای تعریف قواعد فراهم می‌کنند. سیاست‌های شبکه‌ی پیش‌فرضی که در هر فضای نام همه‌ی Podها را انتخاب کرده و تمام ترافیک خروجی و ورودی را مسدود می‌کنند، می‌توانند برای اتخاذ رویکرد فهرست مجاز (allow list) مفید باشند تا اطمینان حاصل شود هیچ بار کاری از قلم نمی‌افتد.

همه‌ی افزونه‌های CNI رمزنگاری در حین انتقال را فراهم نمی‌کنند. اگر افزونه‌ی انتخاب‌شده این قابلیت را نداشته باشد، یک راه‌حل جایگزین می‌تواند استفاده از service mesh برای تأمین این قابلیت باشد.

مخزن داده‌ی etcd مربوط به control plane باید کنترل‌هایی برای محدود کردن دسترسی داشته باشد و در اینترنت به‌صورت عمومی در دسترس نباشد. علاوه بر این، برای برقراری ارتباط امن با آن باید از TLS دوطرفه (mTLS) استفاده شود. مرجع صدور گواهی (certificate authority) مورد استفاده برای این منظور باید اختصاصی etcd باشد.

دسترسی خارجی از اینترنت به kube-apiserver باید محدود شود تا API به‌صورت عمومی در معرض دید قرار نگیرد. دقت کنید که بسیاری از توزیع‌های مدیریت‌شده‌ی کوبرنتیز به‌طور پیش‌فرض API server را به‌صورت عمومی در دسترس قرار می‌دهند. در این حالت می‌توانید از یک bastion host برای دسترسی به سرور استفاده کنید.

دسترسی به API مربوط به [kubelet](/docs/reference/command-line-tools-reference/kubelet/) باید محدود شود و به‌صورت عمومی در دسترس نباشد؛ زیرا تنظیمات پیش‌فرض احراز هویت و مجوزدهی، زمانی که هیچ فایل پیکربندی‌ای با گزینه‌ی `--config` مشخص نشده باشد، بیش‌ازحد سهل‌گیرانه هستند.

اگر برای میزبانی کوبرنتیز از یک ارائه‌دهنده‌ی ابر استفاده می‌شود، دسترسی Podها به API فراداده‌ی ابر در نشانی `169.254.169.254` نیز باید محدود شود یا در صورت عدم نیاز مسدود گردد، زیرا ممکن است اطلاعات را افشا کند.

برای اطلاعات بیشتر درباره‌ی محدودسازی استفاده از LoadBalancer و ExternalIPs، به
[CVE-2020-8554: Man in the middle using LoadBalancer or ExternalIPs](https://github.com/kubernetes/kubernetes/issues/97076)
و [DenyServiceExternalIPs admission controller](/docs/reference/access-authn-authz/admission-controllers/#denyserviceexternalips) مراجعه کنید.

## امنیت Pod {#pod-security}

- [ ] دسترسی‌های RBAC برای `create`، `update`، `patch` و `delete` بارهای کاری فقط در صورت لزوم اعطا می‌شوند.
- [ ] سیاست مناسب Pod Security Standards برای همه‌ی فضاهای نام اعمال و اجباری (enforce) شده است.
- [ ] برای بارهای کاری، محدودیت حافظه (memory limit) تنظیم شده و مقدار آن برابر یا کمتر از درخواست (request) است.
- [ ] محدودیت CPU (CPU limit) ممکن است برای بارهای کاری حساس تنظیم شود.
- [ ] برای نودهایی که از آن پشتیبانی می‌کنند، Seccomp با پروفایل مناسب فراخوانی‌های سیستمی (syscalls) برای برنامه‌ها فعال است.
- [ ] برای نودهایی که از آن پشتیبانی می‌کنند، AppArmor یا SELinux با پروفایل مناسب برای برنامه‌ها فعال است.

مجوزدهی RBAC حیاتی است، اما [نمی‌تواند به‌اندازه‌ی کافی دانه‌ریز باشد تا مجوزدهی روی منابع Podها](/docs/concepts/security/rbac-good-practices/#workload-creation) (یا روی هر منبعی که Podها را مدیریت می‌کند) را ممکن سازد. تنها دانه‌بندی موجود، افعال API روی خود منبع است، برای مثال `create` روی Podها. بدون admission اضافی، مجوز ایجاد این منابع، دسترسی مستقیم و بدون محدودیت به نودهای قابل زمان‌بندی کلاستر را فراهم می‌کند.

[Pod Security Standards](/docs/concepts/security/pod-security-standards/) سه سیاست مختلف شامل privileged، baseline و restricted را تعریف می‌کنند که نحوه‌ی تنظیم فیلدها در `PodSpec` را از نظر امنیتی محدود می‌کنند. این استانداردها را می‌توان در سطح فضای نام با admission جدید [Pod Security](/docs/concepts/security/pod-security-admission/) که به‌طور پیش‌فرض فعال است، یا با یک admission webhook شخص ثالث اعمال کرد. توجه داشته باشید که برخلاف admission حذف‌شده‌ی PodSecurityPolicy که این مورد جایگزین آن شده است، admission [Pod Security](/docs/concepts/security/pod-security-admission/) را می‌توان به‌آسانی با admission webhookها و سرویس‌های خارجی ترکیب کرد.

سیاست `restricted` در admission مربوط به Pod Security، که سخت‌گیرانه‌ترین سیاست در مجموعه‌ی [Pod Security Standards](/docs/concepts/security/pod-security-standards/) است، [می‌تواند در چند حالت اجرا شود](/docs/concepts/security/pod-security-admission/#pod-security-admission-labels-for-namespaces) یعنی `warn`، `audit` یا `enforce` تا [security context](/docs/tasks/configure-pod-container/security-context/) مناسب‌تر بر اساس بهترین شیوه‌های امنیتی به‌تدریج اعمال شود. با این حال، [security context](/docs/tasks/configure-pod-container/security-context/) مربوط به Podها باید جداگانه بررسی شود تا برای موارد استفاده‌ی خاص، امتیازات و دسترسی‌هایی که Podها علاوه بر استانداردهای امنیتی از پیش تعریف‌شده می‌توانند داشته باشند، محدود شود.

برای یک آموزش عملی درباره‌ی [Pod Security](/docs/concepts/security/pod-security-admission/)، به نوشته‌ی وبلاگ [Kubernetes 1.23: Pod Security Graduates to Beta](/blog/2021/12/09/pod-security-admission-beta/) مراجعه کنید.

[محدودیت‌های حافظه و CPU](/docs/concepts/configuration/manage-resources-containers/) باید تنظیم شوند تا منابع حافظه و CPU که یک Pod می‌تواند روی یک نود مصرف کند محدود شود، و در نتیجه از حملات احتمالی DoS توسط بارهای کاری مخرب یا نفوذشده جلوگیری گردد. چنین سیاستی را می‌توان با یک admission controller اعمال کرد. توجه داشته باشید که محدودیت‌های CPU مصرف را کند (throttle) می‌کنند و بنابراین ممکن است بر قابلیت‌های مقیاس‌گذاری خودکار یا کارایی تأثیرات ناخواسته داشته باشند، یعنی فرایند به‌صورت best effort و با منبع CPU موجود اجرا می‌شود.

{{< caution >}}
محدودیت حافظه‌ی بیشتر از درخواست (request) می‌تواند کل نود را در معرض مشکلات OOM قرار دهد.
{{< /caution >}}

### فعال‌سازی Seccomp {#enabling-seccomp}

Seccomp مخفف secure computing mode است و از نسخه‌ی 2.6.12 یکی از قابلیت‌های هسته‌ی لینوکس بوده است. می‌توان از آن برای ایزوله‌سازی (sandbox) امتیازات یک فرایند استفاده کرد و فراخوانی‌هایی را که فرایند می‌تواند از فضای کاربر (userspace) به هسته ارسال کند محدود نمود. کوبرنتیز به شما امکان می‌دهد پروفایل‌های seccomp بارگذاری‌شده روی یک نود را به‌طور خودکار به Podها و کانتینرهای خود اعمال کنید.

Seccomp می‌تواند با کاهش سطح حمله‌ی فراخوانی‌های سیستمی هسته‌ی لینوکس در دسترس داخل کانتینرها، امنیت بارهای کاری شما را بهبود دهد. حالت فیلتر seccomp از BPF بهره می‌گیرد تا یک فهرست مجاز یا مسدود از فراخوانی‌های سیستمی مشخص، با نام پروفایل، ایجاد کند.

از کوبرنتیز 1.27 به بعد، می‌توانید استفاده از `RuntimeDefault` را به‌عنوان پروفایل پیش‌فرض seccomp برای همه‌ی بارهای کاری فعال کنید. یک [آموزش امنیتی](/docs/tutorials/security/seccomp/) در این باره در دسترس است. علاوه بر این، [Kubernetes Security Profiles Operator](https://github.com/kubernetes-sigs/security-profiles-operator) پروژه‌ای است که مدیریت و استفاده از seccomp را در کلاسترها تسهیل می‌کند.

{{< note >}}
Seccomp فقط روی نودهای لینوکس در دسترس است.
{{< /note >}}

### فعال‌سازی AppArmor یا SELinux {#enabling-apparmor-or-selinux}

#### AppArmor

[AppArmor](/docs/tutorials/security/apparmor/) یک ماژول امنیتی هسته‌ی لینوکس است که می‌تواند راهی ساده برای پیاده‌سازی کنترل دسترسی اجباری (MAC) و ممیزی بهتر از طریق لاگ‌های سیستم فراهم کند. یک پروفایل پیش‌فرض AppArmor روی نودهایی که از آن پشتیبانی می‌کنند اعمال می‌شود، یا می‌توان یک پروفایل سفارشی پیکربندی کرد. AppArmor نیز مانند seccomp از طریق پروفایل‌ها پیکربندی می‌شود، به این صورت که هر پروفایل یا در حالت اجرایی (enforcing) کار می‌کند که دسترسی به منابع غیرمجاز را مسدود می‌کند، یا در حالت گزارش (complain) که فقط تخلفات را گزارش می‌دهد. پروفایل‌های AppArmor به‌ازای هر کانتینر و با یک annotation اعمال می‌شوند، که اجازه می‌دهد فرایندها دقیقاً امتیازات مناسب را به دست آورند.

{{< note >}}
AppArmor فقط روی نودهای لینوکس در دسترس است و در
[برخی توزیع‌های لینوکس](https://gitlab.com/apparmor/apparmor/-/wikis/home#distributions-and-ports) فعال است.
{{< /note >}}

#### SELinux

[SELinux](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/selinux_overview.md) نیز یک ماژول امنیتی هسته‌ی لینوکس است که می‌تواند سازوکاری برای پشتیبانی از سیاست‌های امنیتی کنترل دسترسی، از جمله کنترل‌های دسترسی اجباری (MAC)، فراهم کند. برچسب‌های SELinux را می‌توان به کانتینرها یا Podها [از طریق بخش `securityContext` آن‌ها](/docs/tasks/configure-pod-container/security-context/#assign-selinux-labels-to-a-container) اختصاص داد.

{{< note >}}
SELinux فقط روی نودهای لینوکس در دسترس است و در
[برخی توزیع‌های لینوکس](https://en.wikipedia.org/wiki/Security-Enhanced_Linux#Implementations) فعال است.
{{< /note >}}

## لاگ‌ها و ممیزی {#logs-and-auditing}

- [ ] لاگ‌های ممیزی (audit logs)، در صورت فعال بودن، از دسترسی عمومی محافظت می‌شوند.


## جانمایی Pod {#pod-placement}

- [ ] جانمایی Podها مطابق با سطوح حساسیت برنامه انجام می‌شود.
- [ ] برنامه‌های حساس به‌صورت ایزوله روی نودها یا با runtimeهای sandbox مخصوص اجرا می‌شوند.

Podهایی که در سطوح مختلف حساسیت قرار دارند، برای مثال یک Pod برنامه و kube-apiserver، باید روی نودهای جداگانه مستقر شوند. هدف از ایزوله‌سازی نود این است که جلوگیری شود نفوذ از یک کانتینر برنامه (container breakout) به‌طور مستقیم دسترسی به برنامه‌هایی با سطح حساسیت بالاتر را فراهم کند و حرکت آسان در داخل کلاستر (pivot) ممکن نشود. این جداسازی باید اجباری شود تا از استقرار تصادفی Podها روی یک نود مشترک جلوگیری شود. این کار را می‌توان با قابلیت‌های زیر اعمال کرد:

[Node Selectors](/docs/concepts/scheduling-eviction/assign-pod-node/)
: جفت‌های کلید-مقدار، به‌عنوان بخشی از مشخصات Pod، که تعیین می‌کنند Pod روی کدام نودها مستقر شود. این موارد را می‌توان در سطح فضای نام و کلاستر با admission controller مربوط به [PodNodeSelector](/docs/reference/access-authn-authz/admission-controllers/#podnodeselector) اعمال کرد.

[PodTolerationRestriction](/docs/reference/access-authn-authz/admission-controllers/#podtolerationrestriction)
: یک admission controller که به مدیران اجازه می‌دهد [tolerationهای](/docs/concepts/scheduling-eviction/taint-and-toleration/) مجاز در یک فضای نام را محدود کنند. Podهای داخل یک فضای نام فقط می‌توانند از tolerationهایی استفاده کنند که در کلیدهای annotation آبجکت فضای نام مشخص شده‌اند و مجموعه‌ای از tolerationهای پیش‌فرض و مجاز را فراهم می‌کنند.

[RuntimeClass](/docs/concepts/containers/runtime-class/)
: RuntimeClass قابلیتی برای انتخاب پیکربندی container runtime است. پیکربندی container runtime برای اجرای کانتینرهای یک Pod استفاده می‌شود و می‌تواند با هزینه‌ی سربار عملکردی، ایزوله‌سازی بیشتر یا کمتری از میزبان فراهم کند.

## Secrets {#secrets}

- [ ] ConfigMapها برای نگهداری داده‌های محرمانه استفاده نمی‌شوند.
- [ ] رمزنگاری در حالت سکون (encryption at rest) برای API مربوط به Secret پیکربندی شده است.
- [ ] در صورت لزوم، سازوکاری برای تزریق secretهای ذخیره‌شده در ذخیره‌ساز شخص ثالث مستقر و در دسترس است.
- [ ] توکن‌های service account در Podهایی که به آن‌ها نیاز ندارند mount نمی‌شوند.
- [ ] [حجم توکن service account متصل‌شده (bound)](/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume) به‌جای توکن‌های بدون انقضا در حال استفاده است.

Secretهای موردنیاز Podها باید در Secretهای کوبرنتیز نگهداری شوند، نه در جایگزین‌هایی مانند ConfigMap. منابع Secret ذخیره‌شده در etcd باید [در حالت سکون رمزنگاری](/docs/tasks/administer-cluster/encrypt-data/) شوند.

Podهایی که به secret نیاز دارند باید آن‌ها را به‌طور خودکار از طریق حجم (volume) mount شده دریافت کنند، ترجیحاً با ذخیره در حافظه، مانند [گزینه‌ی `emptyDir.medium`](/docs/concepts/storage/volumes/#emptydir). این سازوکار را می‌توان برای تزریق secretها از ذخیره‌سازهای شخص ثالث به‌صورت volume نیز به کار برد، مانند [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/). این روش باید به‌صورت ترجیحی نسبت به اعطای دسترسی RBAC به secretها برای service account مربوط به Pod استفاده شود؛ دسترسی RBAC امکان افزودن secretها به Pod را به‌صورت متغیرهای محیطی یا فایل فراهم می‌کند. توجه داشته باشید که روش متغیر محیطی ممکن است به‌دلیل ثبت crash dumpها در لاگ‌ها و ماهیت غیرمحرمانه‌ی متغیرهای محیطی در لینوکس، در مقایسه با سازوکار مجوزدهی روی فایل‌ها، بیشتر در معرض نشت باشد.

توکن‌های service account نباید در Podهایی که به آن‌ها نیاز ندارند mount شوند. این را می‌توان با تنظیم [`automountServiceAccountToken`](/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server) روی `false` پیکربندی کرد، یا درون service account تا در کل فضای نام اعمال شود، یا به‌طور خاص برای یک Pod. برای کوبرنتیز نسخه‌ی v1.22 و بالاتر، از [Bound Service Accounts](/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume) برای اعتبارنامه‌های service account با مدت اعتبار محدود استفاده کنید.

## ایمیج‌ها {#images}

- [ ] محتوای غیرضروری در ایمیج‌های کانتینر به حداقل رسیده است.
- [ ] ایمیج‌های کانتینر طوری پیکربندی شده‌اند که با کاربر بدون امتیاز (unprivileged) اجرا شوند.
- [ ] ارجاع به ایمیج‌های کانتینر با digest از نوع sha256 (به‌جای تگ‌ها) انجام می‌شود، یا منشأ ایمیج با تأیید امضای دیجیتال آن در زمان استقرار [از طریق admission control](/docs/tasks/administer-cluster/verify-signed-artifacts/#verifying-image-signatures-with-admission-controller) اعتبارسنجی می‌شود.
- [ ] ایمیج‌های کانتینر به‌طور منظم در زمان ساخت و در زمان استقرار اسکن می‌شوند و نرم‌افزارهای آسیب‌پذیر شناخته‌شده وصله (patch) می‌شوند.

ایمیج کانتینر باید حداقل موارد لازم برای اجرای برنامه‌ای را که بسته‌بندی می‌کند در خود داشته باشد. ترجیحاً فقط خود برنامه و وابستگی‌هایش، و ساخت ایمیج از کوچک‌ترین پایه‌ی ممکن. به‌ویژه، ایمیجی که در محیط production استفاده می‌شود نباید شامل shell یا ابزارهای اشکال‌زدایی باشد، زیرا برای عیب‌یابی می‌توان از یک [کانتینر اشکال‌زدایی موقت (ephemeral)](/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container) استفاده کرد.

ایمیج‌ها را طوری بسازید که مستقیماً با یک کاربر بدون امتیاز شروع شوند، با استفاده از [دستور `USER` در Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user). [Security Context](/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) اجازه می‌دهد یک ایمیج کانتینر با کاربر و گروه مشخص و با `runAsUser` و `runAsGroup` اجرا شود، حتی اگر در مانیفست ایمیج مشخص نشده باشد. با این حال، مجوزهای فایل در لایه‌های ایمیج ممکن است باعث شود بدون تغییر ایمیج نتوان فرایند را صرفاً با یک کاربر جدید بدون امتیاز شروع کرد.

از به‌کار بردن تگ‌های ایمیج برای ارجاع به یک ایمیج، به‌ویژه تگ `latest`، خودداری کنید؛ زیرا ایمیجِ پشت یک تگ را می‌توان به‌آسانی در registry تغییر داد. استفاده از digest کامل `sha256` را که برای مانیفست ایمیج منحصربه‌فرد است ترجیح دهید. این سیاست را می‌توان از طریق [ImagePolicyWebhook](/docs/reference/access-authn-authz/admission-controllers/#imagepolicywebhook) اعمال کرد. امضای ایمیج‌ها را نیز می‌توان در زمان استقرار به‌طور خودکار [با یک admission controller تأیید کرد](/docs/tasks/administer-cluster/verify-signed-artifacts/#verifying-image-signatures-with-admission-controller) تا اصالت و یکپارچگی آن‌ها اعتبارسنجی شود.

اسکن یک ایمیج کانتینر می‌تواند از استقرار آسیب‌پذیری‌های بحرانی در کلاستر همراه با ایمیج کانتینر جلوگیری کند. اسکن ایمیج باید پیش از استقرار یک ایمیج کانتینر در کلاستر انجام شود و معمولاً به‌عنوان بخشی از فرایند استقرار در یک pipeline از نوع CI/CD انجام می‌گیرد. هدف از اسکن ایمیج، به‌دست آوردن اطلاعات درباره‌ی آسیب‌پذیری‌های احتمالی در ایمیج کانتینر و راه‌های پیشگیری از آن‌هاست، مانند امتیاز [Common Vulnerability Scoring System (CVSS)](https://www.first.org/cvss/). اگر نتیجه‌ی اسکن ایمیج‌ها با قواعد انطباق (compliance) در pipeline ترکیب شود، فقط ایمیج‌های کانتینری که به‌درستی وصله شده‌اند به محیط Production خواهند رسید.

## کنترل‌کننده‌های پذیرش (Admission controllers)

- [ ] مجموعه‌ای مناسب از کنترل‌کننده‌های پذیرش فعال شده است.
- [ ] یک سیاست امنیتی Pod توسط Pod Security Admission و/یا یک کنترل‌کننده پذیرش مبتنی بر webhook اعمال می‌شود.
- [ ] افزونه‌های زنجیره پذیرش و webhookها به‌صورت امن پیکربندی شده‌اند.

کنترل‌کننده‌های پذیرش می‌توانند به بهبود امنیت کلاستر کمک کنند. با این حال، از آنجا که API server را گسترش می‌دهند، خودشان نیز می‌توانند مخاطراتی ایجاد کنند و
[باید به‌درستی ایمن شوند](/blog/2022/01/19/secure-your-admission-controllers-and-webhooks/).

فهرست‌های زیر تعدادی از کنترل‌کننده‌های پذیرش را معرفی می‌کنند که می‌توان برای تقویت وضعیت امنیتی کلاستر و برنامه‌های خود در نظر گرفت. این فهرست‌ها شامل کنترل‌کننده‌هایی است که ممکن است در بخش‌های دیگر این سند به آن‌ها اشاره شده باشد.

این گروه اول از کنترل‌کننده‌های پذیرش شامل افزونه‌هایی است که
[به‌صورت پیش‌فرض فعال هستند](/docs/reference/access-authn-authz/admission-controllers/#which-plugins-are-enabled-by-default)؛
توصیه می‌شود آن‌ها را فعال نگه دارید، مگر اینکه دقیقاً بدانید چه می‌کنید:

[`CertificateApproval`](/docs/reference/access-authn-authz/admission-controllers/#certificateapproval)
: بررسی‌های مجوز اضافی انجام می‌دهد تا اطمینان حاصل شود کاربر تأییدکننده اجازه تأیید درخواست گواهی را دارد.

[`CertificateSigning`](/docs/reference/access-authn-authz/admission-controllers/#certificatesigning)
: بررسی‌های مجوز اضافی انجام می‌دهد تا اطمینان حاصل شود کاربر امضاکننده اجازه امضای درخواست‌های گواهی را دارد.

[`CertificateSubjectRestriction`](/docs/reference/access-authn-authz/admission-controllers/#certificatesubjectrestriction)
: هر درخواست گواهی را که یک «group» (یا «organization attribute») با مقدار `system:masters` مشخص کرده باشد رد می‌کند.

[`LimitRanger`](/docs/reference/access-authn-authz/admission-controllers/#limitranger)
: محدودیت‌های API مربوط به LimitRange را اعمال می‌کند.

[`MutatingAdmissionWebhook`](/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook)
: امکان استفاده از کنترل‌کننده‌های سفارشی را از طریق webhookها فراهم می‌کند؛ این کنترل‌کننده‌ها می‌توانند درخواست‌هایی را که بررسی می‌کنند تغییر دهند.

[`PodSecurity`](/docs/reference/access-authn-authz/admission-controllers/#podsecurity)
: جایگزین Pod Security Policy است و زمینه‌های امنیتی (security context) Podهای مستقرشده را محدود می‌کند.

[`ResourceQuota`](/docs/reference/access-authn-authz/admission-controllers/#resourcequota)
: سهمیه‌های منابع را اعمال می‌کند تا از مصرف بیش‌ازحد منابع جلوگیری شود.

[`ValidatingAdmissionWebhook`](/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)
: امکان استفاده از کنترل‌کننده‌های سفارشی را از طریق webhookها فراهم می‌کند؛ این کنترل‌کننده‌ها درخواست‌هایی را که بررسی می‌کنند تغییر نمی‌دهند.

گروه دوم شامل افزونه‌هایی است که به‌صورت پیش‌فرض فعال نیستند، اما در وضعیت دسترس‌پذیری عمومی (general availability) قرار دارند و برای بهبود وضعیت امنیتی شما توصیه می‌شوند:

[`DenyServiceExternalIPs`](/docs/reference/access-authn-authz/admission-controllers/#denyserviceexternalips)
: هرگونه استفاده جدید از فیلد `Service.spec.externalIPs` را رد می‌کند. این یک راهکار کاهش مخاطره برای
[CVE-2020-8554: Man in the middle using LoadBalancer or ExternalIPs](https://github.com/kubernetes/kubernetes/issues/97076) است.

[`NodeRestriction`](/docs/reference/access-authn-authz/admission-controllers/#noderestriction)
: مجوزهای kubelet را به تغییر منابع API مربوط به Podهایی که متعلق به خودش هستند یا منبع API مربوط به نودی که نماینده خودش است محدود می‌کند. همچنین از استفاده kubelet از حاشیه‌نویسی (annotation) با پیشوند `node-restriction.kubernetes.io/` جلوگیری می‌کند؛ مهاجمی که به اعتبارنامه‌های kubelet دسترسی دارد می‌تواند از این annotation برای تأثیرگذاری بر جایگذاری Pod روی نود تحت کنترل خود استفاده کند.

گروه سوم شامل افزونه‌هایی است که به‌صورت پیش‌فرض فعال نیستند، اما می‌توان آن‌ها را برای برخی موارد کاربردی در نظر گرفت:

[`AlwaysPullImages`](/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages)
: استفاده از آخرین نسخه یک ایمیج دارای تگ را اجباری می‌کند و اطمینان می‌دهد که استقراردهنده مجوز استفاده از آن ایمیج را دارد.

[`ImagePolicyWebhook`](/docs/reference/access-authn-authz/admission-controllers/#imagepolicywebhook)
: امکان اعمال کنترل‌های اضافی بر ایمیج‌ها را از طریق webhookها فراهم می‌کند.

<!-- The fourth group includes plugins that are not enabled by default, still in
alpha state but could be considered for certain use cases:

[`EventRateLimit`](/docs/reference/access-authn-authz/admission-controllers/#eventratelimit)
: Rate limits adding new Events to the API server.

[`PodNodeSelector`](/docs/reference/access-authn-authz/admission-controllers/#podnodeselector)
: Allows controls of node selectors within namespaces and cluster-wide.

[`PodTolerationRestriction`](/docs/reference/access-authn-authz/admission-controllers/#podtolerationrestriction)
: Allows control of pod tolerations permitted for pods within a namespace. -->

## مرحله بعد

- [ارتقای سطح دسترسی از طریق ایجاد Pod](/docs/reference/access-authn-authz/authorization/#privilege-escalation-via-pod-creation)
  درباره یک خطر خاص در کنترل دسترسی هشدار می‌دهد؛ بررسی کنید که چگونه این تهدید را مدیریت می‌کنید.
  - اگر از RBAC کوبرنتیز استفاده می‌کنید، برای اطلاعات بیشتر درباره مجوزدهی،
    [بهترین روش‌های RBAC](/docs/concepts/security/rbac-good-practices/) را مطالعه کنید.
- [ایمن‌سازی یک کلاستر](/docs/tasks/administer-cluster/securing-a-cluster/) برای اطلاعات درباره محافظت از کلاستر در برابر دسترسی تصادفی یا مخرب.
- [راهنمای چندمستاجری (multi-tenancy) در کلاستر](/docs/concepts/security/multi-tenancy/) برای توصیه‌های مربوط به گزینه‌های پیکربندی و بهترین روش‌ها در چندمستاجری.
- [پست وبلاگ «نگاهی دقیق‌تر به راهنمای مقاوم‌سازی کوبرنتیز از NSA/CISA»](/blog/2021/10/05/nsa-cisa-kubernetes-hardening-guidance/#building-secure-container-images)
  به‌عنوان منبعی تکمیلی برای مقاوم‌سازی کلاسترهای کوبرنتیز.
