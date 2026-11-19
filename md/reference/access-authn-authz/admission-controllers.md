---
reviewers:
- lavalamp
- davidopp
- derekwaynecarr
- erictune
- janetkuo
- thockin
title: کنترل پذیرش در کوبرنتیز
linkTitle: کنترل پذیرش
content_type: concept
weight: 40
---

<!-- overview -->
این صفحه مروری بر _کنترل‌کننده‌های پذیرش_ (admission controllers) ارائه می‌دهد.

کنترل‌کنندهٔ پذیرش قطعه‌کدی است که درخواست‌های ارسالی به سرور API کوبرنتیز را پس از احراز هویت و مجوزدهی، اما پیش از ذخیره‌شدن منبع، رهگیری می‌کند.

برخی از قابلیت‌های مهم کوبرنتیز تنها زمانی به‌درستی پشتیبانی می‌شوند که یک کنترل‌کنندهٔ پذیرش فعال باشد. در نتیجه، سرور API کوبرنتیزی که با مجموعهٔ مناسبی از کنترل‌کننده‌های پذیرش پیکربندی نشده باشد، سروری ناقص است و از همهٔ قابلیت‌هایی که انتظار دارید پشتیبانی نخواهد کرد.

<!-- body -->
## کنترل‌کننده‌های پذیرش چه هستند؟

کنترل‌کننده‌های پذیرش کدهایی درون {{< glossary_tooltip term_id="kube-apiserver" text="سرور API" >}} کوبرنتیز هستند که داده‌های رسیده در درخواستی برای تغییر یک منبع را بررسی می‌کنند.

کنترل‌کننده‌های پذیرش بر درخواست‌هایی اعمال می‌شوند که آبجکت‌ها را ایجاد، حذف یا تغییر می‌دهند. این کنترل‌کننده‌ها می‌توانند فعل‌های سفارشی را نیز مسدود کنند؛ برای نمونه، درخواستی برای اتصال به یک پاد از طریق پراکسی سرور API. کنترل‌کننده‌های پذیرش درخواست‌های خواندن آبجکت‌ها (**get**، **watch** یا **list**) را مسدود _نمی‌کنند_ (و نمی‌توانند مسدود کنند)، زیرا عملیات خواندن از لایهٔ کنترل پذیرش عبور نمی‌کند.

سازوکارهای کنترل پذیرش می‌توانند _اعتبارسنج_ (validating)، _تغییردهنده_ (mutating) یا هر دو باشند. کنترل‌کننده‌های تغییردهنده می‌توانند داده‌های منبعِ در حال تغییر را اصلاح کنند، اما کنترل‌کننده‌های اعتبارسنج چنین اجازه‌ای ندارند.

کنترل‌کننده‌های پذیرش در کوبرنتیز {{< skew currentVersion >}} شامل موارد [فهرست](#what-does-each-admission-controller-do) زیر هستند، درون فایل اجرایی `kube-apiserver` کامپایل شده‌اند و تنها مدیر کلاستر می‌تواند آن‌ها را پیکربندی کند.

### نقاط توسعهٔ کنترل پذیرش

در میان [فهرست](#what-does-each-admission-controller-do) کامل، چهار کنترل‌کنندهٔ ویژه وجود دارد:
[MutatingAdmissionWebhook](#mutatingadmissionwebhook)،
[MutatingAdmissionPolicy](#mutatingadmissionpolicy)،
[ValidatingAdmissionWebhook](#validatingadmissionwebhook) و
[ValidatingAdmissionPolicy](#validatingadmissionpolicy).
دو کنترل‌کنندهٔ وب‌هوک، به‌ترتیب [وب‌هوک‌های کنترل پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks) تغییردهنده و اعتبارسنجی را اجرا می‌کنند که در API پیکربندی شده‌اند. کنترل‌کننده‌های MutatingAdmissionPolicy و ValidatingAdmissionPolicy نیز راهی برای جاسازی کد اعلانی تغییر یا اعتبارسنجی درون خود API فراهم می‌کنند، بی‌آنکه به فراخوانی‌های HTTP خارجی نیازی باشد.

با این چهار کنترل‌کنندهٔ پذیرش می‌توانید رفتار کلاستر را در زمان پذیرش سفارشی کنید.

### مراحل کنترل پذیرش

فرایند کنترل پذیرش در دو مرحله انجام می‌شود. در مرحلهٔ نخست، کنترل‌کننده‌های پذیرش تغییردهنده اجرا می‌شوند و در مرحلهٔ دوم، کنترل‌کننده‌های پذیرش اعتبارسنج. یادآوری می‌کنیم که برخی کنترل‌کننده‌ها هر دو نقش را دارند.

اگر هر یک از کنترل‌کننده‌ها در هر یک از این دو مرحله درخواست را رد کند، کل درخواست بی‌درنگ رد می‌شود و خطایی به کاربر نهایی بازگردانده می‌شود.

در پایان، کنترل‌کننده‌های پذیرش افزون بر اینکه گاهی آبجکت مورد نظر را تغییر می‌دهند، ممکن است گاهی اثرات جانبی نیز داشته باشند؛ یعنی منابع مرتبط را در جریان پردازش درخواست تغییر دهند. افزایش میزان مصرف سهمیه (quota) نمونهٔ شاخص ضرورت این کار است. هر اثر جانبی از این دست به فرایند بازپس‌گیری یا هماهنگ‌سازی متناظری نیاز دارد، زیرا هیچ کنترل‌کنندهٔ پذیرشی با قطعیت نمی‌داند که یک درخواست از همهٔ کنترل‌کننده‌های پذیرش دیگر نیز عبور خواهد کرد.

ترتیب این فراخوانی‌ها را در نمودار زیر می‌توانید ببینید.

{{< figure src="/docs/reference/access-authn-authz/admission-control-phases.svg" alt="Sequence diagram for kube-apiserver handling requests during the admission phase showing mutation webhooks, followed by validatingadmissionpolicies and finally validating webhooks. It shows that the continue until the first rejection, or being accepted by all of them. It also shows that mutations by mutating webhooks cause all previously called webhooks to be called again." class="diagram-large" link="[https://mermaid.live/edit#pako:eNqtVm1v2zYQ_isHDcZazO-O34QhQJdiazAEKJquAwZ9oaSzxZoiNZJy4gT-7ztSL1bs5sPQ6otE8rm75-45inwOEpViEAa9HnxgewSrwKCFjZL2nj8hbIWKmRAHYAZsxg1wI3-2oNEUmFhMIS29UWZtYcLRaMttVsbDROWjHHXOeDr4aprPETemRDOardfjSPZ6z1xyGz5Hgc0wxygIo0BiaTUTUdCPgoYELUAUTKfFI03Tl8F_S5SJnyfjnGut9LvEKm1oyuoSj_1IAj215y9McxYLNJWFX6qWmbP6bbf1sX-aTRcJzl3sc8hnfLQ3SijtgQ8Zt3gGE0oVXRS85k8qixSxg9tqPJyBvpV6JI_HY68XyUg2FXjP2Vaz3E05OxLxc6URaYXAhB1YokRqamBJgsbwmAtuD31gMgWTqVKkECOURcqcmLhHfQDLc_QO0so9-RtWAcjJezSJ7hbxvubSol20XRnjgBXcoCaXkFE4weWW-obAxhpqG-3GnmaaU19wJaHImEFH68Gt5aVl1k0_YJwptTN9ci2EeiCi8QH2THBiTcjWQaEETzgan92GS9-4J1zraAgn-rfWB3QVY9bzSaj2XFJbl_QWfmrDtXFN_5V6nuL0gVKM0bl0ZS1sxYjCgdo4g_wsAhNGdcM0qRlnVg069CBhpUHvrtC456o0lEdCY4rTgmjTkXL1LNsyLmuRjk07FExbqkfBpIW_SAm3h_37cvndx1u3-ifJpiVaKqGbuffqfQNd2szB3RupSEml0y9-Qmn-5MdtT74wTfMbq4W3bnW_oYprJSqDWD3CH5SNiZVWlyD4NdbXN1XWlUBn4lzSvWsKTEHb79bxJf7LqWPIojM6s0GZulJXA1_YwfW1L1wIn6pGhzc43A77kGikDQYMCpW-revvgN6AihZ2a0md59WiJnbJJhkmu2qqoP9oxcA0cd1_B353G5zapc3uY70TTl3oNXPhGkwIt3KvdnhmdDiZtAsnlncq5ZuDa_-q3qBi_3rDNyARU0zfvqjN6wz_rvv4fzGsjX44RVK_ZdjRu6kicOkgrunEK7FPVi3rc0edynaWXib86XspN2X9bsqX-vwA0q3E1PvU8u5n3hGqPhxasNsfDuy2lotiCup7hGZPmdIfac4BuhsAhQv6dJjytLoE9IP62kHXG39ene4Z9JnihpXC-mOVzGjj_6NU3lhqVW6zINzQj5tG1fFYH7YNhJVW3R9k0owx5XRRuKuuU_5WRW4od9Q3in5UQTgZ-zBB-Bw8BuFgNpsOF_PF-mo-nkxmq-WsHxwINFkOr8aT5WoxW01Wy8l4fewHT57ZZDieL-fr8WI8W01XV7Px9PgfcW89xA](https://mermaid.live/edit#pako:eNqtVm1v2zYQ_isHDcZazO-O34QhQJdiazAEKJquAwZ9oaSzxZoiNZJy4gT-7ztSL1bs5sPQ6otE8rm75-45inwOEpViEAa9HnxgewSrwKCFjZL2nj8hbIWKmRAHYAZsxg1wI3-2oNEUmFhMIS29UWZtYcLRaMttVsbDROWjHHXOeDr4aprPETemRDOardfjSPZ6z1xyGz5Hgc0wxygIo0BiaTUTUdCPgoYELUAUTKfFI03Tl8F_S5SJnyfjnGut9LvEKm1oyuoSj_1IAj215y9McxYLNJWFX6qWmbP6bbf1sX-aTRcJzl3sc8hnfLQ3SijtgQ8Zt3gGE0oVXRS85k8qixSxg9tqPJyBvpV6JI_HY68XyUg2FXjP2Vaz3E05OxLxc6URaYXAhB1YokRqamBJgsbwmAtuD31gMgWTqVKkECOURcqcmLhHfQDLc_QO0so9-RtWAcjJezSJ7hbxvubSol20XRnjgBXcoCaXkFE4weWW-obAxhpqG-3GnmaaU19wJaHImEFH68Gt5aVl1k0_YJwptTN9ci2EeiCi8QH2THBiTcjWQaEETzgan92GS9-4J1zraAgn-rfWB3QVY9bzSaj2XFJbl_QWfmrDtXFN_5V6nuL0gVKM0bl0ZS1sxYjCgdo4g_wsAhNGdcM0qRlnVg069CBhpUHvrtC456o0lEdCY4rTgmjTkXL1LNsyLmuRjk07FExbqkfBpIW_SAm3h_37cvndx1u3-ifJpiVaKqGbuffqfQNd2szB3RupSEml0y9-Qmn-5MdtT74wTfMbq4W3bnW_oYprJSqDWD3CH5SNiZVWlyD4NdbXN1XWlUBn4lzSvWsKTEHb79bxJf7LqWPIojM6s0GZulJXA1_YwfW1L1wIn6pGhzc43A77kGikDQYMCpW-revvgN6AihZ2a0md59WiJnbJJhkmu2qqoP9oxcA0cd1_B353G5zapc3uY70TTl3oNXPhGkwIt3KvdnhmdDiZtAsnlncq5ZuDa_-q3qBi_3rDNyARU0zfvqjN6wz_rvv4fzGsjX44RVK_ZdjRu6kicOkgrunEK7FPVi3rc0edynaWXib86XspN2X9bsqX-vwA0q3E1PvU8u5n3hGqPhxasNsfDuy2lotiCup7hGZPmdIfac4BuhsAhQv6dJjytLoE9IP62kHXG39ene4Z9JnihpXC-mOVzGjj_6NU3lhqVW6zINzQj5tG1fFYH7YNhJVW3R9k0owx5XRRuKuuU_5WRW4od9Q3in5UQTgZ-zBB-Bw8BuFgNpsOF_PF-mo-nkxmq-WsHxwINFkOr8aT5WoxW01Wy8l4fewHT57ZZDieL-fr8WI8W01XV7Px9PgfcW89xA)" >}}

## چرا به آن‌ها نیاز دارم؟

برخی از قابلیت‌های مهم کوبرنتیز تنها زمانی به‌درستی پشتیبانی می‌شوند که یک کنترل‌کنندهٔ پذیرش فعال باشد. در نتیجه، سرور API کوبرنتیزی که با مجموعهٔ مناسبی از کنترل‌کننده‌های پذیرش پیکربندی نشده باشد، سروری ناقص است و از همهٔ قابلیت‌هایی که انتظار دارید پشتیبانی نخواهد کرد.

## چگونه یک کنترل‌کنندهٔ پذیرش را فعال کنم؟

فلگ `enable-admission-plugins` در سرور API کوبرنتیز فهرستی از افزونه‌های کنترل پذیرش را، جداشده با ویرگول، دریافت می‌کند که باید پیش از تغییر آبجکت‌ها در کلاستر فراخوانی شوند.
برای نمونه، خط فرمان زیر افزونه‌های کنترل پذیرش `NamespaceLifecycle` و `LimitRanger` را فعال می‌کند:

```shell
kube-apiserver --enable-admission-plugins=NamespaceLifecycle,LimitRanger ...
```

{{< note >}}
بسته به شیوهٔ استقرار کلاستر کوبرنتیز و نحوهٔ راه‌اندازی سرور API، ممکن است لازم باشد این تنظیمات را به روش‌های متفاوتی اعمال کنید. برای نمونه، اگر سرور API به‌صورت یک سرویس systemd مستقر شده باشد، باید فایل واحد systemd را ویرایش کنید و اگر کوبرنتیز به‌صورت خودمیزبان (self-hosted) مستقر شده باشد، می‌توانید فایل مانیفست سرور API را تغییر دهید.
{{< /note >}}

## چگونه یک کنترل‌کنندهٔ پذیرش را غیرفعال کنم؟

فلگ `disable-admission-plugins` در سرور API کوبرنتیز فهرستی از افزونه‌های کنترل پذیرش را، جداشده با ویرگول، دریافت می‌کند که باید غیرفعال شوند؛ حتی اگر در فهرست افزونه‌های پیش‌فرض فعال قرار داشته باشند.

```shell
kube-apiserver --disable-admission-plugins=PodNodeSelector,AlwaysDeny ...
```

## کدام افزونه‌ها به‌طور پیش‌فرض فعال هستند؟

برای دیدن افزونه‌های پذیرش فعال، دستور زیر را اجرا کنید:

```shell
kube-apiserver -h | grep enable-admission-plugins
```

در کوبرنتیز {{< skew currentVersion >}}، افزونه‌های پیش‌فرض عبارت‌اند از:

```shell
CertificateApproval, CertificateSigning, CertificateSubjectRestriction, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, LimitRanger, MutatingAdmissionPolicy, MutatingAdmissionWebhook, NamespaceLifecycle, PersistentVolumeClaimResize, PodSecurity, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook
```

## هر کنترل‌کنندهٔ پذیرش چه کاری انجام می‌دهد؟

### AlwaysAdmit {#alwaysadmit}

{{< feature-state for_k8s_version="v1.13" state="deprecated" >}}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش اجازهٔ ورود همهٔ پادها به کلاستر را می‌دهد. این کنترل‌کننده **منسوخ** شده است، زیرا رفتارش دقیقاً مانند حالتی است که هیچ کنترل‌کنندهٔ پذیرشی وجود نداشته باشد.

### AlwaysDeny {#alwaysdeny}

{{< feature-state for_k8s_version="v1.13" state="deprecated" >}}

**نوع**: اعتبارسنج.

این کنترل‌کننده همهٔ درخواست‌ها را رد می‌کند. کنترل‌کنندهٔ AlwaysDeny **منسوخ** شده است، زیرا کاربرد واقعی ندارد.

### AlwaysPullImages {#alwayspullimages}

**نوع**: تغییردهنده و اعتبارسنج.

این کنترل‌کنندهٔ پذیرش هر Pod جدید را طوری تغییر می‌دهد که سیاست دریافت ایمیج آن الزاماً `Always` باشد. این کار در کلاسترهای چندمستأجره (multitenant) سودمند است، زیرا کاربران مطمئن می‌شوند که ایمیج‌های خصوصی‌شان تنها به دست کسانی استفاده می‌شود که اعتبارنامهٔ لازم برای دریافت آن‌ها را دارند. بدون این کنترل‌کنندهٔ پذیرش، وقتی ایمیجی روی یک نود دریافت شد، هر پادی از هر کاربری می‌تواند تنها با دانستن نام ایمیج و بدون هیچ بررسی مجوزی، از آن استفاده کند (به شرط آنکه Pod روی همان نود زمان‌بندی شود). با فعال بودن این کنترل‌کنندهٔ پذیرش، ایمیج‌ها همیشه پیش از راه‌اندازی کانتینرها دریافت می‌شوند؛ بنابراین داشتن اعتبارنامهٔ معتبر الزامی است.

### CertificateApproval {#certificateapproval}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش درخواست‌های تأیید منابع CertificateSigningRequest را زیر نظر می‌گیرد و بررسی‌های مجوزدهی بیشتری انجام می‌دهد تا مطمئن شود کاربر تأییدکننده اجازهٔ **تأیید** درخواست‌های گواهی را با مقدار `spec.signerName` درخواست‌شده در منبع CertificateSigningRequest دارد.

برای آگاهی بیشتر دربارهٔ مجوزهای لازم برای انجام کارهای مختلف روی منابع CertificateSigningRequest، به [درخواست‌های امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/) مراجعه کنید.

### CertificateSigning {#certificatesigning}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش به‌روزرسانی‌های فیلد `status.certificate` در منابع CertificateSigningRequest را زیر نظر می‌گیرد و بررسی‌های مجوزدهی بیشتری انجام می‌دهد تا مطمئن شود کاربر امضاکننده اجازهٔ **امضای** درخواست‌های گواهی را با مقدار `spec.signerName` درخواست‌شده در منبع CertificateSigningRequest دارد.

برای آگاهی بیشتر دربارهٔ مجوزهای لازم برای انجام کارهای مختلف روی منابع CertificateSigningRequest، به [درخواست‌های امضای گواهی](/docs/reference/access-authn-authz/certificate-signing-requests/) مراجعه کنید.

### CertificateSubjectRestriction {#certificatesubjectrestriction}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش ایجاد منابع CertificateSigningRequest را که مقدار `spec.signerName` آن‌ها `kubernetes.io/kube-apiserver-client` است زیر نظر می‌گیرد و هر درخواستی را که گروه (group یا organization attribute) آن `system:masters` باشد رد می‌کند.

### DefaultIngressClass {#defaultingressclass}

**نوع**: تغییردهنده.

این کنترل‌کنندهٔ پذیرش ایجاد آبجکت‌های `Ingress` را که کلاس ingress مشخصی درخواست نکرده‌اند زیر نظر می‌گیرد و به‌طور خودکار یک کلاس ingress پیش‌فرض به آن‌ها اضافه می‌کند. به این ترتیب، کاربرانی که کلاس ingress خاصی درخواست نمی‌کنند نیازی به توجه به این موضوع ندارند و کلاس پیش‌فرض را دریافت می‌کنند.

اگر هیچ کلاس ingress پیش‌فرضی پیکربندی نشده باشد، این کنترل‌کنندهٔ پذیرش هیچ کاری انجام نمی‌دهد. اگر بیش از یک کلاس ingress به‌عنوان پیش‌فرض علامت‌گذاری شده باشد، این کنترل‌کننده ایجاد هر `Ingress` را با خطا رد می‌کند و مدیر کلاستر باید آبجکت‌های `IngressClass` خود را بازبینی کند و تنها یکی را (با حاشیه‌نویسی "ingressclass.kubernetes.io/is-default-class") به‌عنوان پیش‌فرض علامت بزند. این کنترل‌کنندهٔ پذیرش به‌روزرسانی‌های `Ingress` را نادیده می‌گیرد و تنها هنگام ایجاد عمل می‌کند.

برای آگاهی بیشتر دربارهٔ کلاس‌های ingress و نحوهٔ علامت‌گذاری یکی از آن‌ها به‌عنوان پیش‌فرض، مستندات [Ingress](/docs/concepts/services-networking/ingress/) را ببینید.

### DefaultStorageClass {#defaultstorageclass}

**نوع**: تغییردهنده.

این کنترل‌کنندهٔ پذیرش ایجاد آبجکت‌های `PersistentVolumeClaim` را که کلاس ذخیره‌سازی مشخصی درخواست نکرده‌اند زیر نظر می‌گیرد و به‌طور خودکار یک کلاس ذخیره‌سازی پیش‌فرض به آن‌ها اضافه می‌کند.
به این ترتیب، کاربرانی که کلاس ذخیره‌سازی خاصی درخواست نمی‌کنند نیازی به توجه به این موضوع ندارند و کلاس پیش‌فرض را دریافت می‌کنند.

اگر هیچ `StorageClass` پیش‌فرضی وجود نداشته باشد، این کنترل‌کنندهٔ پذیرش کاری انجام نمی‌دهد. اگر بیش از یک کلاس ذخیره‌سازی به‌عنوان پیش‌فرض علامت‌گذاری شده باشد و سپس یک `PersistentVolumeClaim` بدون تنظیم `storageClassName` ایجاد کنید، کوبرنتیز از جدیدترین `StorageClass` پیش‌فرض ایجادشده استفاده می‌کند.
اگر یک `PersistentVolumeClaim` با مقدار مشخصی برای `volumeName` ایجاد شود و پس از اعمال StorageClass پیش‌فرض، مقدار `storageClassName` حجم ایستا با `storageClassName` آن `PersistentVolumeClaim` یکسان نباشد، این درخواست در وضعیت معلق (pending) باقی می‌ماند.
این کنترل‌کنندهٔ پذیرش به‌روزرسانی‌های `PersistentVolumeClaim` را نادیده می‌گیرد و تنها هنگام ایجاد عمل می‌کند.

برای آگاهی دربارهٔ درخواست‌های حجم پایدار (persistent volume claims)، کلاس‌های ذخیره‌سازی و نحوهٔ علامت‌گذاری یک کلاس ذخیره‌سازی به‌عنوان پیش‌فرض، مستندات [حجم پایدار](/docs/concepts/storage/persistent-volumes/) را ببینید.

### DefaultTolerationSeconds {#defaulttolerationseconds}

**نوع**: تغییردهنده.

اگر پادها از پیش تحملی (toleration) برای taintهای `node.kubernetes.io/not-ready:NoExecute` یا `node.kubernetes.io/unreachable:NoExecute` نداشته باشند، این کنترل‌کنندهٔ پذیرش تحمل پیش‌فرض را برای پادها تنظیم می‌کند تا taintهای `notready:NoExecute` و `unreachable:NoExecute` را بر اساس پارامترهای ورودی `default-not-ready-toleration-seconds` و `default-unreachable-toleration-seconds` در k8s-apiserver تحمل کنند.
مقدار پیش‌فرض `default-not-ready-toleration-seconds` و `default-unreachable-toleration-seconds` برابر با ۵ دقیقه است.

### DenyServiceExternalIPs

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش هر استفادهٔ تازه از فیلد `externalIPs` در `Service` را رد می‌کند. این قابلیت بسیار قدرتمند است (امکان رهگیری ترافیک شبکه را فراهم می‌کند) و سیاست‌ها کنترل خوبی بر آن ندارند. با فعال بودن این کنترل‌کننده، کاربران کلاستر نمی‌توانند Serviceهای جدیدی بسازند که از `externalIPs` استفاده کنند و نمی‌توانند مقادیر جدیدی به `externalIPs` در آبجکت‌های `Service` موجود اضافه کنند. استفاده‌های موجود از `externalIPs` تحت تأثیر قرار نمی‌گیرند و کاربران می‌توانند مقادیری را از `externalIPs` در آبجکت‌های `Service` موجود حذف کنند.

بیشتر کاربران اصلاً به این قابلیت نیاز ندارند و مدیران کلاستر بهتر است غیرفعال کردن آن را بررسی کنند.
کلاسترهایی که واقعاً به این قابلیت نیاز دارند، بهتر است برای مدیریت استفاده از آن یک سیاست سفارشی به کار بگیرند.

این کنترل‌کنندهٔ پذیرش به‌طور پیش‌فرض غیرفعال است.

### EventRateLimit {#eventratelimit}

{{< feature-state for_k8s_version="v1.13" state="alpha" >}}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش مشکل سرازیر شدن انبوه درخواست‌های ذخیرهٔ Eventهای جدید به سرور API را کاهش می‌دهد. مدیر کلاستر می‌تواند محدودیت نرخ رویدادها را به این صورت تعیین کند:

* فعال کردن کنترل‌کنندهٔ پذیرش `EventRateLimit`؛
* ارجاع به یک فایل پیکربندی `EventRateLimit` در فایلی که با فلگ خط فرمان `--admission-control-config-file` به سرور API داده می‌شود:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: EventRateLimit
    path: eventconfig.yaml
...
```

چهار نوع محدودیت را می‌توان در پیکربندی مشخص کرد:

 * `Server`: همهٔ درخواست‌های Event (ایجاد یا تغییر) که سرور API دریافت می‌کند، یک سطل (bucket) مشترک دارند.
 * `Namespace`: هر فضای نام (namespace) سطل اختصاصی خود را دارد.
 * `User`: به هر کاربر یک سطل اختصاص داده می‌شود.
 * `SourceAndObject`: به هر ترکیب از منبع رویداد و آبجکت درگیر در آن، یک سطل اختصاص داده می‌شود.

در ادامه نمونه‌ای از فایل `eventconfig.yaml` برای چنین پیکربندی‌ای آمده است:

```yaml
apiVersion: eventratelimit.admission.k8s.io/v1alpha1
kind: Configuration
limits:
  - type: Namespace
    qps: 50
    burst: 100
    cacheSize: 2000
  - type: User
    qps: 10
    burst: 50
```

برای جزئیات بیشتر، [EventRateLimit Config API (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/) را ببینید.

این کنترل‌کنندهٔ پذیرش به‌طور پیش‌فرض غیرفعال است.

### ExtendedResourceToleration {#extendedresourcetoleration}

**نوع**: تغییردهنده.

این افزونه ایجاد نودهای اختصاصی دارای منابع توسعه‌یافته (extended resources) را آسان می‌کند.
اگر اپراتورها بخواهند نودهای اختصاصی با منابع توسعه‌یافته (مانند GPU، FPGA و غیره) ایجاد کنند، باید [روی نود taint بگذارند](/docs/concepts/scheduling-eviction/taint-and-toleration/#example-use-cases) و نام منبع توسعه‌یافته را به‌عنوان کلید آن قرار دهند. اگر این کنترل‌کنندهٔ پذیرش فعال باشد، به‌طور خودکار تحمل‌های لازم برای چنین taintهایی را به پادهایی که منابع توسعه‌یافته درخواست می‌کنند اضافه می‌کند تا کاربران مجبور نباشند این تحمل‌ها را به‌صورت دستی اضافه کنند.

این کنترل‌کنندهٔ پذیرش به‌طور پیش‌فرض غیرفعال است.

### ImagePolicyWebhook {#imagepolicywebhook}

**نوع**: اعتبارسنجی (Validating).

کنترل‌کننده پذیرش (admission controller) ImagePolicyWebhook به یک وب‌هوک (webhook) بک‌اند امکان می‌دهد درباره پذیرش درخواست‌ها تصمیم بگیرد.

این کنترل‌کننده پذیرش به‌طور پیش‌فرض غیرفعال است.

#### قالب فایل پیکربندی {#imagereview-config-file-format}

کنترل‌کننده ImagePolicyWebhook برای تنظیم گزینه‌های رفتاری بک‌اند از یک فایل پیکربندی استفاده می‌کند.
این فایل می‌تواند در قالب json یا yaml باشد و ساختار آن به شکل زیر است:

```yaml
imagePolicy:
  kubeConfigFile: /path/to/kubeconfig/for/backend
  # time in s to cache approval
  allowTTL: 50
  # time in s to cache denial
  denyTTL: 50
  # time in ms to wait between retries
  retryBackoff: 500
  # determines behavior if the webhook backend fails
  defaultAllow: true
```

در فایلی که به فلگ خط فرمان `--admission-control-config-file` سرور API داده می‌شود، به فایل پیکربندی ImagePolicyWebhook ارجاع دهید:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: ImagePolicyWebhook
    path: imagepolicyconfig.yaml
...
```

همچنین می‌توانید پیکربندی را مستقیماً در همین فایل قرار دهید:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: ImagePolicyWebhook
    configuration:
      imagePolicy:
        kubeConfigFile: <path-to-kubeconfig-file>
        allowTTL: 50
        denyTTL: 50
        retryBackoff: 500
        defaultAllow: true
```

فایل پیکربندی ImagePolicyWebhook باید به فایلی در قالب
[kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
ارجاع دهد که اتصال به بک‌اند را برقرار می‌کند.
ارتباط با بک‌اند حتماً باید از طریق TLS انجام شود.

فیلد `cluster` در فایل kubeconfig باید به سرویس راه دور اشاره کند و فیلد `user`
باید مجوزدهنده (authorizer) بازگردانده‌شده را در خود داشته باشد.

```yaml
# clusters refers to the remote service.
clusters:
  - name: name-of-remote-imagepolicy-service
    cluster:
      certificate-authority: /path/to/ca.pem    # CA for verifying the remote service.
      server: https://images.example.com/policy # URL of remote service to query. Must use 'https'.

# users refers to the API server's webhook configuration.
users:
  - name: name-of-api-server
    user:
      client-certificate: /path/to/cert.pem # cert for the webhook admission controller to use
      client-key: /path/to/key.pem          # key matching the cert
```

برای پیکربندی‌های بیشتر HTTP، به مستندات
[kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) مراجعه کنید.

#### محتوای درخواست‌ها

هنگامی که سرور API باید درباره پذیرش یک درخواست تصمیم بگیرد، یک آبجکت `ImageReview` از نسخه
`imagepolicy.k8s.io/v1alpha1` را که به‌صورت JSON سریال‌سازی شده و عمل موردنظر را توصیف می‌کند، با متد POST ارسال می‌کند.
این آبجکت فیلدهایی دارد که کانتینرهای در حال پذیرش را توصیف می‌کنند و همچنین همه
حاشیه‌نویسی‌های (annotation) پاد را که با `*.image-policy.k8s.io/*` مطابقت دارند، در بر می‌گیرد.

{{< note >}}
آبجکت‌های API وب‌هوک از همان قواعد سازگاری نسخه‌بندی پیروی می‌کنند که سایر آبجکت‌های API کوبرنتیز
از آن‌ها پیروی می‌کنند. پیاده‌سازان باید بدانند که تعهدات سازگاری برای آبجکت‌های آلفا سست‌تر است
و باید فیلد `apiVersion` درخواست را بررسی کنند تا از واسازی (deserialization) صحیح آن اطمینان یابند.
افزون بر این، سرور API باید گروه افزونه‌های API با نام `imagepolicy.k8s.io/v1alpha1` را
فعال کند (`--runtime-config=imagepolicy.k8s.io/v1alpha1=true`).
{{< /note >}}

نمونه‌ای از بدنه درخواست:

```json
{
  "apiVersion": "imagepolicy.k8s.io/v1alpha1",
  "kind": "ImageReview",
  "spec": {
    "containers": [
      {
        "image": "myrepo/myimage:v1"
      },
      {
        "image": "myrepo/myimage@sha256:beb6bd6a68f114c1dc2ea4b28db81bdf91de202a9014972bec5e4d9171d90ed"
      }
    ],
    "annotations": {
      "mycluster.image-policy.k8s.io/ticket-1234": "break-glass"
    },
    "namespace": "mynamespace"
  }
}
```

انتظار می‌رود سرویس راه دور فیلد `status` درخواست را پر کند و با اجازه‌دادن یا ندادن دسترسی
پاسخ دهد. فیلد `spec` در بدنه پاسخ نادیده گرفته می‌شود و می‌توان آن را حذف کرد. پاسخی که دسترسی را مجاز می‌کند به این شکل است:

```json
{
  "apiVersion": "imagepolicy.k8s.io/v1alpha1",
  "kind": "ImageReview",
  "status": {
    "allowed": true
  }
}
```

برای رد دسترسی، سرویس پاسخ زیر را برمی‌گرداند:

```json
{
  "apiVersion": "imagepolicy.k8s.io/v1alpha1",
  "kind": "ImageReview",
  "status": {
    "allowed": false,
    "reason": "image currently blacklisted"
  }
}
```

{{< note >}}
آبجکت‌های `ImageReview` همه ایمیج‌هایی از Podها را در بر می‌گیرند که قرار است به‌صورت
کانتینر اجرا شوند. این شامل ایمیج‌هایی است که در فیلدهای containers،
initContainers یا ephemeralContainers در مشخصات یک Pod تعیین شده‌اند. در نتیجه،
ایمیج‌هایی که در حجم‌های ایمیج (image volumes) قرار دارند، در محدوده
ImagePolicyWebhook نیستند.
{{< /note >}}

برای مستندات بیشتر به
[API `imagepolicy.v1alpha1`](/docs/reference/config-api/imagepolicy.v1alpha1/) مراجعه کنید.

#### گسترش با حاشیه‌نویسی‌ها

همه حاشیه‌نویسی‌های یک Pod که با `*.image-policy.k8s.io/*` مطابقت دارند، به وب‌هوک ارسال می‌شوند.
ارسال حاشیه‌نویسی‌ها به کاربرانی که از بک‌اند سیاست ایمیج آگاه هستند امکان می‌دهد
اطلاعات بیشتری برای آن بفرستند، و به پیاده‌سازی‌های مختلف بک‌اند نیز امکان می‌دهد
اطلاعات متفاوتی را بپذیرند.

نمونه‌هایی از اطلاعاتی که می‌توانید در این حاشیه‌نویسی‌ها قرار دهید:

* درخواست «شکستن شیشه» (break glass) برای نادیده‌گرفتن یک سیاست در شرایط اضطراری.
* شماره تیکتی از یک سامانه تیکت که درخواست شکستن شیشه را مستند می‌کند
* ارائه سرنخی به سرور سیاست درباره imageID ایمیج ارائه‌شده، تا نیازی به جست‌وجوی آن نباشد

در هر صورت، حاشیه‌نویسی‌ها را کاربر فراهم می‌کند و کوبرنتیز به هیچ وجه آن‌ها را اعتبارسنجی نمی‌کند.

### LimitPodHardAntiAffinityTopology {#limitpodhardantiaffinitytopology}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش هر پادی را که در `requiredDuringSchedulingIgnoredDuringExecution`
کلید توپولوژی `AntiAffinity` دیگری به جز `kubernetes.io/hostname` تعریف کند، رد می‌کند.

این کنترل‌کننده پذیرش به‌طور پیش‌فرض غیرفعال است.

### LimitRanger {#limitranger}

**نوع**: تغییردهنده (Mutating) و اعتبارسنجی.

این کنترل‌کننده پذیرش درخواست ورودی را بررسی می‌کند و اطمینان می‌یابد که هیچ‌یک از
محدودیت‌های فهرست‌شده در آبجکت `LimitRange` در یک `Namespace` نقض نشود. اگر در
استقرار کوبرنتیز خود از آبجکت‌های `LimitRange` استفاده می‌کنید، حتماً باید از این کنترل‌کننده پذیرش
برای اعمال آن محدودیت‌ها استفاده کنید. از LimitRanger همچنین می‌توان برای اعمال درخواست‌های منبع پیش‌فرض
بر Podهایی استفاده کرد که هیچ درخواستی مشخص نکرده‌اند؛ در حال حاضر، LimitRanger پیش‌فرض نیاز ۰٫۱ CPU را
بر همه Podهای فضای نام (namespace) `default` اعمال می‌کند.

برای جزئیات بیشتر، [مرجع API LimitRange](/docs/reference/kubernetes-api/core/limit-range-v1/)
و [نمونه LimitRange](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
را ببینید.

### MutatingAdmissionPolicy {#mutatingadmissionpolicy}

**نوع**: تغییردهنده.

[این کنترل‌کننده پذیرش](/docs/reference/access-authn-authz/mutating-admission-policy/) از زبان عبارت مشترک (Common Expression Language یا CEL) برای اعلام تغییرات روی منابع استفاده می‌کند. تغییرات را می‌توان یا با یک پیکربندی apply تعریف کرد که با راهبرد ادغام server side apply ادغام می‌شود، یا با یک JSON patch.
این کنترل‌کننده زمانی فعال است که هم feature gate `mutatingadmissionpolicy` و هم گروه/نسخه `admissionregistration.k8s.io/v1alpha1` فعال باشند.
اگر هر یک از MutatingAdmissionPolicyها شکست بخورد، درخواست نیز شکست می‌خورد.

### MutatingAdmissionWebhook {#mutatingadmissionwebhook}

**نوع**: تغییردهنده.

این کنترل‌کننده پذیرش همه وب‌هوک‌های تغییردهنده‌ای را که با درخواست مطابقت دارند فراخوانی می‌کند.
وب‌هوک‌های مطابق به‌صورت متوالی فراخوانی می‌شوند و هر یک در صورت تمایل می‌تواند آبجکت را تغییر دهد.

همان‌طور که از نامش پیداست، این کنترل‌کننده پذیرش فقط در مرحله تغییر (mutating) اجرا می‌شود.

اگر وب‌هوکی که این کنترل‌کننده فراخوانی می‌کند اثرات جانبی داشته باشد (برای مثال، کاهش سهمیه)،
*باید* یک سامانه آشتی‌دهی (reconciliation) داشته باشد، زیرا تضمینی وجود ندارد که وب‌هوک‌های بعدی
یا کنترل‌کننده‌های پذیرش اعتبارسنج اجازه دهند درخواست به پایان برسد.

اگر MutatingAdmissionWebhook را غیرفعال کنید، باید آبجکت `MutatingWebhookConfiguration`
را نیز در گروه/نسخه `admissionregistration.k8s.io/v1` از طریق فلگ `--runtime-config`
غیرفعال کنید؛ هر دو به‌طور پیش‌فرض فعال هستند.

#### هنگام نوشتن و نصب وب‌هوک‌های تغییردهنده احتیاط کنید

* وقتی آبجکت‌هایی که کاربران قصد ایجادشان را دارند با آنچه به آن‌ها بازگردانده می‌شود
  متفاوت باشد، ممکن است کاربران سردرگم شوند.
* وقتی آبجکت‌هایی که حلقه‌های کنترلی داخلی قصد ایجادشان را دارند هنگام خواندن مجدد متفاوت باشند،
  ممکن است این حلقه‌ها دچار اختلال شوند.
  * مقداردهی فیلدهایی که در ابتدا تنظیم نشده‌اند، نسبت به بازنویسی فیلدهایی که در درخواست اصلی
    تنظیم شده‌اند، احتمال کمتری دارد که مشکل ایجاد کند. از انجام کار دوم پرهیز کنید.
* تغییرات آینده در حلقه‌های کنترلی منابع داخلی یا منابع شخص ثالث ممکن است
  وب‌هوک‌هایی را که امروز به‌خوبی کار می‌کنند از کار بیندازد. حتی پس از نهایی‌شدن API نصب وب‌هوک،
  تضمین نمی‌شود که همه رفتارهای ممکن وب‌هوک‌ها برای همیشه پشتیبانی شوند.

### NamespaceAutoProvision {#namespaceautoprovision}

**نوع**: تغییردهنده.

این کنترل‌کننده پذیرش همه درخواست‌های ورودی روی منابع وابسته به فضای نام را بررسی می‌کند
و وجود فضای نام ارجاع‌شده را وارسی می‌کند.
اگر فضای نام پیدا نشود، آن را ایجاد می‌کند.
این کنترل‌کننده پذیرش در استقرارهایی مفید است که نمی‌خواهند ایجاد فضای نام را
پیش از استفاده از آن محدود کنند.

### NamespaceExists {#namespaceexists}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش همه درخواست‌ها روی منابع وابسته به فضای نام، به جز خود `Namespace`، را بررسی می‌کند.
اگر فضای نامی که درخواست به آن ارجاع می‌دهد وجود نداشته باشد، درخواست رد می‌شود.

### NamespaceLifecycle {#namespacelifecycle}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش تضمین می‌کند که در یک `Namespace` در حال خاتمه نتوان آبجکت جدیدی ایجاد کرد،
و درخواست‌هایی که در یک `Namespace` ناموجود ارسال می‌شوند رد شوند.
همچنین این کنترل‌کننده پذیرش از حذف سه فضای نام رزروشده سیستمی، یعنی `default`،
`kube-system` و `kube-public`، جلوگیری می‌کند.

حذف یک `Namespace` دنباله‌ای از عملیات را آغاز می‌کند که همه آبجکت‌های آن فضای نام (پادها، سرویس‌ها
و غیره) را حذف می‌کند. برای حفظ یکپارچگی این فرایند، اکیداً توصیه می‌کنیم
این کنترل‌کننده پذیرش را اجرا کنید.

### NodeDeclaredFeatureValidator {#nodedeclaredfeaturevalidator}

{{< feature-state feature_gate_name="NodeDeclaredFeatures" >}}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش عملیات نوشتن روی Podهای مقیدشده (bound) را رهگیری می‌کند تا اطمینان یابد
تغییرات با ویژگی‌هایی که نود میزبان فعلی Pod اعلام کرده است سازگارند.
این کنترل‌کننده برای تعیین مجموعه ویژگی‌های فعال، از فیلد `.status.declaredFeatures` آبجکت Node
استفاده می‌کند. اگر به‌روزرسانی یک Pod به ویژگی‌ای نیاز داشته باشد که در فهرست ویژگی‌های
نود فعلی آن نیست، کنترل‌کننده پذیرش درخواست به‌روزرسانی را رد می‌کند.
این کار از بروز خطاهای زمان اجرا به‌دلیل ناهمخوانی ویژگی‌ها پس از زمان‌بندی Pod جلوگیری می‌کند.

اگر feature gate [`NodeDeclaredFeatures`](/docs/reference/command-line-tools-reference/feature-gates/#NodeDeclaredFeatures) فعال باشد،
این کنترل‌کننده پذیرش به‌طور پیش‌فرض فعال است.

### NodeRestriction {#noderestriction}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش آبجکت‌های `Node` و `Pod` را که یک kubelet می‌تواند تغییر دهد محدود می‌کند. برای اینکه
kubeletها مشمول محدودیت این کنترل‌کننده پذیرش شوند، باید از اعتبارنامه‌هایی در گروه `system:nodes`
با نام کاربری به شکل `system:node:<nodeName>` استفاده کنند.
چنین kubeletهایی فقط مجازند آبجکت API `Node` خودشان را تغییر دهند و از میان آبجکت‌های API `Pod` نیز فقط آن‌هایی را که به نود خودشان مقید شده‌اند تغییر دهند.
به kubeletها اجازه داده نمی‌شود که taintهای آبجکت API `Node` خود را به‌روزرسانی یا حذف کنند.

افزونه پذیرش `NodeRestriction` نمی‌گذارد kubeletها آبجکت API `Node` خود را حذف کنند،
و تغییر برچسب‌های دارای پیشوند `kubernetes.io/` یا `k8s.io/` را از سوی kubelet به شکل زیر کنترل می‌کند:

* **ممنوع** (kubeletها از تغییر این موارد منع می‌شوند):
  * برچسب‌هایی با پیشوند `node-restriction.kubernetes.io/`. این پیشوند برای مدیران رزرو شده است تا آبجکت‌های `Node` را برای جداسازی بارهای کاری برچسب‌گذاری کنند.
  * برچسب‌هایی با پیشوند `node-role.kubernetes.io/` (برای مثال: `node-role.kubernetes.io/control-plane`). این برچسب‌ها محدود شده‌اند تا نودهای فاقد امتیاز نتوانند نقش‌های کلاستر را برای خودشان اعلام کنند.
* **مجاز** (kubeletها می‌توانند این موارد را اضافه، حذف یا به‌روزرسانی کنند):
  * `kubernetes.io/hostname`
  * `kubernetes.io/arch`
  * `kubernetes.io/os`
  * `beta.kubernetes.io/instance-type`
  * `node.kubernetes.io/instance-type`
  * `failure-domain.beta.kubernetes.io/region` (منسوخ)
  * `failure-domain.beta.kubernetes.io/zone` (منسوخ)
  * `topology.kubernetes.io/region`
  * `topology.kubernetes.io/zone`
  * برچسب‌هایی با پیشوند `kubelet.kubernetes.io/`
  * برچسب‌هایی با پیشوند `node.kubernetes.io/`
* **رزروشده**:
  استفاده kubeletها از هر برچسب دیگری با پیشوندهای `kubernetes.io` یا `k8s.io` رزرو شده است.
  افزونه پذیرش `NodeRestriction` معمولاً اجازه استفاده از این برچسب‌ها را نمی‌دهد تا از برچسب‌گذاری غیرمجاز نود روی خودش جلوگیری کند،
  اما ممکن است در آینده، در قالب ویژگی‌های جدید، برچسب‌های بیشتری با این پیشوندها را مجاز کند.

وقتی [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ServiceAccountNodeAudienceRestriction`
فعال باشد، این افزونه پذیرش مخاطبانی (audiences) را نیز محدود می‌کند که kubelet می‌تواند
از طریق API `TokenRequest` برای آن‌ها توکن حساب سرویس درخواست کند. در این حالت، kubelet فقط می‌تواند
برای مخاطبانی توکن درخواست کند که پادهای روی آن نود از قبل به آن‌ها ارجاع داده‌اند (از طریق حجم‌های (volume) توکن حساب سرویس
projected یا درخواست‌های توکن درایور CSI)، یا برای مخاطبانی که صراحتاً
از طریق RBAC و با فعل `request-serviceaccounts-token-audience` اعطا شده‌اند. برای جزئیات بیشتر،
[محدودیت مخاطب توکن حساب سرویس](/docs/reference/access-authn-authz/node/#service-account-token-audience-restriction) را ببینید.

نسخه‌های آینده ممکن است محدودیت‌های بیشتری اضافه کنند تا اطمینان حاصل شود kubeletها فقط حداقل مجموعه
مجوزهای لازم برای عملکرد صحیح را در اختیار دارند.

### OwnerReferencesPermissionEnforcement {#ownerreferencespermissionenforcement}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش از دسترسی به `metadata.ownerReferences` یک آبجکت محافظت می‌کند
تا فقط کاربرانی که مجوز **حذف** (delete) آن آبجکت را دارند بتوانند آن را تغییر دهند.
همچنین این کنترل‌کننده پذیرش از دسترسی به `metadata.ownerReferences[x].blockOwnerDeletion`
یک آبجکت محافظت می‌کند تا فقط کاربرانی که مجوز **به‌روزرسانی** (update) زیرمنبع `finalizers`
در *مالک* ارجاع‌شده را دارند بتوانند آن را تغییر دهند.

### PersistentVolumeClaimResize {#persistentvolumeclaimresize}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش اعتبارسنجی‌های بیشتری برای بررسی درخواست‌های ورودی
تغییر اندازه `PersistentVolumeClaim` پیاده‌سازی می‌کند.

فعال‌کردن کنترل‌کننده پذیرش `PersistentVolumeClaimResize` توصیه می‌شود.
این کنترل‌کننده پذیرش به‌طور پیش‌فرض از تغییر اندازه همه claimها جلوگیری می‌کند، مگر اینکه `StorageClass` آن claim
با تنظیم `allowVolumeExpansion` روی `true` صراحتاً تغییر اندازه را فعال کرده باشد.

برای مثال، همه `PersistentVolumeClaim`هایی که از `StorageClass` زیر ایجاد می‌شوند از گسترش حجم پشتیبانی می‌کنند:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gluster-vol-default
provisioner: kubernetes.io/glusterfs
parameters:
  resturl: "http://192.168.10.100:8080"
  restuser: ""
  secretNamespace: ""
  secretName: ""
allowVolumeExpansion: true
```

برای اطلاعات بیشتر درباره درخواست‌های حجم پایدار (persistent volume claims)، [PersistentVolumeClaimها](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) را ببینید.

### PodNodeSelector {#podnodeselector}

{{< feature-state for_k8s_version="v1.5" state="alpha" >}}

**نوع**: اعتبارسنجی.

این کنترل‌کننده پذیرش با خواندن یک حاشیه‌نویسی فضای نام و یک پیکربندی سراسری،
انتخابگرهای (selector) نودی را که می‌توان در یک فضای نام استفاده کرد، پیش‌فرض‌گذاری و محدود می‌کند.

این کنترل‌کننده پذیرش به‌طور پیش‌فرض غیرفعال است.

#### قالب فایل پیکربندی

کنترل‌کننده `PodNodeSelector` برای تنظیم گزینه‌های رفتاری بک‌اند از یک فایل پیکربندی استفاده می‌کند.
توجه داشته باشید که قالب این فایل پیکربندی در نسخه‌ای آینده به یک فایل نسخه‌بندی‌شده منتقل خواهد شد.
این فایل می‌تواند در قالب json یا yaml باشد و ساختار آن به شکل زیر است:

```yaml
podNodeSelectorPluginConfig:
  clusterDefaultNodeSelector: name-of-node-selector
  namespace1: name-of-node-selector
  namespace2: name-of-node-selector
```

در فایلی که به فلگ خط فرمان `--admission-control-config-file` سرور API داده می‌شود،
به فایل پیکربندی `PodNodeSelector` ارجاع دهید:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: PodNodeSelector
  path: podnodeselector.yaml
...
```

#### قالب حاشیه‌نویسی پیکربندی

کنترل‌کننده `PodNodeSelector` برای اختصاص انتخابگرهای نود به فضاهای نام از کلید حاشیه‌نویسی
`scheduler.alpha.kubernetes.io/node-selector` استفاده می‌کند.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    scheduler.alpha.kubernetes.io/node-selector: name-of-node-selector
  name: namespace3
```

#### رفتار داخلی

این کنترل‌کننده پذیرش رفتار زیر را دارد:

1. اگر `Namespace` حاشیه‌نویسی‌ای با کلید `scheduler.alpha.kubernetes.io/node-selector` داشته باشد،
   مقدار آن به‌عنوان انتخابگر نود استفاده می‌شود.
2. اگر فضای نام چنین حاشیه‌نویسی‌ای نداشته باشد، `clusterDefaultNodeSelector` تعریف‌شده در
   فایل پیکربندی افزونه `PodNodeSelector` به‌عنوان انتخابگر نود استفاده می‌شود.
3. انتخابگر نود پاد از نظر تعارض با انتخابگر نود فضای نام ارزیابی می‌شود. وجود تعارض
   به رد درخواست می‌انجامد.
4. انتخابگر نود پاد با انتخابگر مجاز مختص فضای نام که در فایل پیکربندی افزونه تعریف شده است
   مقایسه و ارزیابی می‌شود. وجود تعارض به رد درخواست می‌انجامد.

{{< note >}}
با افزونه PodNodeSelector می‌توان پادها را وادار کرد که روی نودهایی با برچسب‌های مشخص اجرا شوند. افزونه پذیرش
PodTolerationRestriction را نیز ببینید که با آن می‌توان از اجرای پادها روی نودهایی با taintهای مشخص جلوگیری کرد.
{{< /note >}}

### PodSecurity {#podsecurity}

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

**نوع**: اعتبارسنجی.

کنترل‌کننده پذیرش PodSecurity، Podهای جدید را پیش از پذیرش بررسی می‌کند و بر اساس
security context درخواست‌شده و محدودیت‌های [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/)
مجاز برای فضای نامی که Pod در آن قرار خواهد گرفت، تعیین می‌کند که آیا باید پذیرفته شود یا نه.

برای اطلاعات بیشتر، مستندات [پذیرش امنیت Pod](/docs/concepts/security/pod-security-admission/)
را ببینید.

کنترل‌کننده PodSecurity جایگزین کنترل‌کننده پذیرش قدیمی‌تری به نام PodSecurityPolicy شد.

### PodTolerationRestriction {#podtolerationrestriction}

{{< feature-state for_k8s_version="v1.7" state="alpha" >}}

**نوع**: تغییردهنده و اعتبارسنجی.

کنترل‌کننده پذیرش PodTolerationRestriction هرگونه تعارض بین tolerationهای یک
پاد و tolerationهای فضای نام آن را بررسی می‌کند.
در صورت وجود تعارض، درخواست پاد را رد می‌کند.
سپس tolerationهایی را که روی فضای نام حاشیه‌نویسی شده‌اند با tolerationهای پاد ادغام می‌کند.
مجموعه tolerationهای حاصل با فهرستی از tolerationهای مجاز که روی فضای نام حاشیه‌نویسی شده است، سنجیده می‌شود.
اگر این بررسی موفق باشد، درخواست پاد پذیرفته می‌شود؛ در غیر این صورت رد می‌شود.

اگر فضای نام پاد هیچ toleration پیش‌فرض یا toleration مجاز حاشیه‌نویسی‌شده‌ای نداشته باشد،
در صورت تعیین‌شدن، tolerationهای پیش‌فرض سطح کلاستر یا فهرست tolerationهای مجاز سطح کلاستر
به‌جای آن‌ها استفاده می‌شوند.

اختصاص tolerationها به یک فضای نام از طریق کلید حاشیه‌نویسی `scheduler.alpha.kubernetes.io/defaultTolerations` انجام می‌شود.
فهرست tolerationهای مجاز را می‌توان از طریق کلید حاشیه‌نویسی `scheduler.alpha.kubernetes.io/tolerationsWhitelist` اضافه کرد.

نمونه‌ای از حاشیه‌نویسی‌های فضای نام:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: apps-that-need-nodes-exclusively
  annotations:
    scheduler.alpha.kubernetes.io/defaultTolerations: '[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'
    scheduler.alpha.kubernetes.io/tolerationsWhitelist: '[{"operator": "Exists", "effect": "NoSchedule", "key": "dedicated-node"}]'
```

این کنترل‌کننده پذیرش به‌طور پیش‌فرض غیرفعال است.

### PodTopologyLabels {#podtopologylabels}

{{< feature-state feature_gate_name="PodTopologyLabelsAdmission" >}}

**نوع**: تغییردهنده (Mutating)

کنترل‌کنندهٔ پذیرش PodTopologyLabels زیرمنبع‌های `pods/binding` را برای همهٔ پادهایی که به یک Node متصل شده‌اند تغییر می‌دهد و برچسب‌های توپولوژی متناظر با برچسب‌های همان Node را به آن‌ها اضافه می‌کند. به این ترتیب، برچسب‌های توپولوژی Node به‌صورت برچسب‌های پاد در دسترس قرار می‌گیرند و می‌توان آن‌ها را با استفاده از [Downward API](/docs/concepts/workloads/pods/downward-api/) در اختیار کانتینرهای در حال اجرا گذاشت. برچسب‌هایی که در نتیجهٔ این کنترل‌کننده در دسترس قرار می‌گیرند، برچسب‌های [topology.kubernetes.io/region](/docs/reference/labels-annotations-taints/#topologykubernetesioregion) و [topology.kubernetes.io/zone](/docs/reference/labels-annotations-taints/#topologykubernetesiozone) هستند.

{{<note>}}
اگر یک webhook پذیرش تغییردهنده برچسب‌های زیرمنبع `pods/binding` را اضافه یا تغییر دهد، این تغییرات در نتیجهٔ عملکرد این کنترل‌کننده به برچسب‌های پاد نیز منتقل می‌شوند و برچسب‌هایی را که کلید متعارض دارند بازنویسی می‌کنند.
{{</note>}}

این کنترل‌کنندهٔ پذیرش زمانی فعال می‌شود که feature gate با نام `PodTopologyLabelsAdmission` فعال باشد.

### Priority {#priority}

**نوع**: تغییردهنده و اعتبارسنج.

کنترل‌کنندهٔ پذیرش priority از فیلد `priorityClassName` استفاده می‌کند و مقدار عددی صحیح اولویت را تعیین می‌کند. اگر کلاس اولویت (priority class) پیدا نشود، Pod رد می‌شود.

### ResourceQuota {#resourcequota}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش درخواست ورودی را بررسی می‌کند و اطمینان می‌یابد که هیچ‌یک از محدودیت‌های تعریف‌شده در آبجکت `ResourceQuota` در یک `Namespace` نقض نشود. اگر در استقرار کوبرنتیز خود از آبجکت‌های `ResourceQuota` استفاده می‌کنید، برای اعمال محدودیت‌های سهمیه (quota) **باید** از این کنترل‌کنندهٔ پذیرش استفاده کنید.

برای جزئیات بیشتر، [مرجع API مربوط به ResourceQuota](/docs/reference/kubernetes-api/core/resource-quota-v1/) و [نمونهٔ سهمیهٔ منابع](/docs/concepts/policy/resource-quotas/) را ببینید.

### RuntimeClass {#runtimeclass}

**نوع**: تغییردهنده و اعتبارسنج.

اگر یک RuntimeClass با [سربار پاد](/docs/concepts/scheduling-eviction/pod-overhead/) (Pod overhead) پیکربندی‌شده تعریف کنید، این کنترل‌کنندهٔ پذیرش Podهای ورودی را بررسی می‌کند. این کنترل‌کنندهٔ پذیرش، در صورت فعال بودن، هر درخواست ایجاد Pod را که مقدار سربار در آن از قبل تنظیم شده باشد رد می‌کند. برای Podهایی که یک RuntimeClass در `.spec` آن‌ها پیکربندی و انتخاب شده است، این کنترل‌کنندهٔ پذیرش فیلد `.spec.overhead` را در Pod بر اساس مقدار تعریف‌شده در RuntimeClass متناظر تنظیم می‌کند.

برای اطلاعات بیشتر، [سربار پاد](/docs/concepts/scheduling-eviction/pod-overhead/) را نیز ببینید.

### ServiceAccount {#serviceaccount}

**نوع**: تغییردهنده و اعتبارسنج.

این کنترل‌کنندهٔ پذیرش خودکارسازی را برای [serviceAccountها](/docs/tasks/configure-pod-container/configure-service-account/) پیاده‌سازی می‌کند. پروژهٔ کوبرنتیز اکیداً توصیه می‌کند این کنترل‌کنندهٔ پذیرش را فعال کنید. اگر قصد دارید به هر شکلی از آبجکت‌های `ServiceAccount` کوبرنتیز استفاده کنید، باید این کنترل‌کنندهٔ پذیرش را فعال کنید.

برای تقویت تدابیر امنیتی مربوط به Secretها، از فضاهای نام (namespace) جداگانه استفاده کنید تا دسترسی به Secretهای mount‌شده از یکدیگر جدا شود.

### StorageObjectInUseProtection

**نوع**: تغییردهنده.

افزونهٔ `StorageObjectInUseProtection` نهایی‌کننده‌های (finalizer) `kubernetes.io/pvc-protection` یا `kubernetes.io/pv-protection` را به Persistent Volume Claimها (PVC) یا Persistent Volumeهای (PV) تازه ایجادشده اضافه می‌کند. اگر کاربری یک PVC یا PV را حذف کند، آن PVC یا PV تا زمانی که کنترل‌کنندهٔ PVC Protection یا PV Protection این نهایی‌کننده را از آن حذف نکند، پاک نمی‌شود. برای اطلاعات دقیق‌تر، به [محافظت از آبجکت ذخیره‌سازی در حال استفاده](/docs/concepts/storage/persistent-volumes/#storage-object-in-use-protection) مراجعه کنید.

### TaintNodesByCondition {#taintnodesbycondition}

**نوع**: تغییردهنده.

این کنترل‌کنندهٔ پذیرش Nodeهای تازه ایجادشده را با `NotReady` و `NoSchedule` {{< glossary_tooltip text="taint می‌کند" term_id="taint" >}}. این کار از بروز شرایط رقابتی (race condition) جلوگیری می‌کند که ممکن بود باعث شود Podها پیش از به‌روزرسانی taintهای Nodeهای جدید، یعنی پیش از آنکه این taintها وضعیت گزارش‌شدهٔ Node را به‌درستی منعکس کنند، روی آن Nodeها زمان‌بندی شوند.

### ValidatingAdmissionPolicy {#validatingadmissionpolicy}

**نوع**: اعتبارسنج.

[این کنترل‌کنندهٔ پذیرش](/docs/reference/access-authn-authz/validating-admission-policy/) اعتبارسنجی CEL را برای درخواست‌های ورودیِ منطبق پیاده‌سازی می‌کند. این کنترل‌کننده زمانی فعال است که هم feature gate با نام `validatingadmissionpolicy` و هم group/version مربوط به `admissionregistration.k8s.io/v1alpha1` فعال باشند. اگر هر یک از ValidatingAdmissionPolicyها ناموفق باشد، درخواست ناموفق می‌شود.

### ValidatingAdmissionWebhook {#validatingadmissionwebhook}

**نوع**: اعتبارسنج.

این کنترل‌کنندهٔ پذیرش هر webhook اعتبارسنجی را که با درخواست منطبق باشد فراخوانی می‌کند. webhookهای منطبق به‌صورت موازی فراخوانی می‌شوند و اگر هر یک از آن‌ها درخواست را رد کند، درخواست ناموفق می‌شود. این کنترل‌کنندهٔ پذیرش فقط در مرحلهٔ اعتبارسنجی اجرا می‌شود. برخلاف webhookهایی که کنترل‌کنندهٔ پذیرش `MutatingAdmissionWebhook` فراخوانی می‌کند، webhookهایی که این کنترل‌کننده فراخوانی می‌کند نمی‌توانند آبجکت را تغییر دهند.

اگر webhookای که این کنترل‌کننده فراخوانی می‌کند اثر جانبی داشته باشد (برای مثال، کاهش سهمیه)، *باید* یک سازوکار تطبیق (reconciliation) داشته باشد، زیرا تضمینی وجود ندارد که webhookهای بعدی یا سایر کنترل‌کننده‌های پذیرش اعتبارسنج اجازهٔ تکمیل درخواست را بدهند.

اگر ValidatingAdmissionWebhook را غیرفعال کنید، باید آبجکت `ValidatingWebhookConfiguration` را نیز در group/version مربوط به `admissionregistration.k8s.io/v1` از طریق فلگ `--runtime-config` غیرفعال کنید.

## آیا مجموعهٔ توصیه‌شده‌ای از کنترل‌کننده‌های پذیرش برای استفاده وجود دارد؟

بله. کنترل‌کننده‌های پذیرش توصیه‌شده به‌طور پیش‌فرض فعال هستند (فهرست آن‌ها را [اینجا](/docs/reference/command-line-tools-reference/kube-apiserver/#options) ببینید)، بنابراین لازم نیست آن‌ها را به‌صراحت مشخص کنید. می‌توانید با استفاده از فلگ `--enable-admission-plugins` کنترل‌کننده‌های پذیرش دیگری را علاوه بر مجموعهٔ پیش‌فرض فعال کنید (**ترتیب اهمیتی ندارد**).
