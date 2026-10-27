---
reviewers:
- lavalamp
- davidopp
- derekwaynecarr
- erictune
- janetkuo
- thockin
title: کنترل پذیرش (Admission Control) در کوبرنتیز
linkTitle: کنترل پذیرش
content_type: concept
weight: 40
---

<!-- overview -->
این صفحه مروری بر _admission controllerها_ (کنترل‌کننده‌های پذیرش) ارائه می‌دهد.

یک admission controller قطعه‌ای از کد است که درخواست‌های ارسال‌شده به API server کوبرنتیز را پیش از ماندگار شدن (persistence) منبع، اما پس از احراز هویت و مجوزدهی درخواست، رهگیری می‌کند.

چند قابلیت مهم کوبرنتیز برای آنکه به‌درستی پشتیبانی شوند، به فعال بودن یک admission controller نیاز دارند. در نتیجه، API server کوبرنتیزی که با مجموعه مناسبی از admission controllerها پیکربندی نشده باشد، سروری ناقص است و همه قابلیت‌هایی را که انتظار دارید پشتیبانی نخواهد کرد.

<!-- body -->
## آن‌ها چیستند؟

Admission controllerها کدهایی در {{< glossary_tooltip term_id="kube-apiserver" text="API server" >}} کوبرنتیز هستند که داده‌های موجود در یک درخواست برای تغییر یک منبع را بررسی می‌کنند.

Admission controllerها بر درخواست‌هایی اعمال می‌شوند که آبجکت‌ها را ایجاد، حذف یا تغییر می‌دهند. Admission controllerها همچنین می‌توانند فعل‌های سفارشی (custom verbs) را مسدود کنند؛ برای نمونه درخواست اتصال به یک pod از طریق پروکسی API server. Admission controllerها درخواست‌های خواندن آبجکت‌ها (**get**، **watch** یا **list**) را مسدود _نمی‌کنند_ (و نمی‌توانند بکنند)، زیرا خواندن از لایه کنترل پذیرش عبور نمی‌کند.

سازوکارهای کنترل پذیرش ممکن است _اعتبارسنجی‌کننده_ (validating)، _تغییردهنده_ (mutating) یا هر دو باشند. کنترل‌کننده‌های mutating می‌توانند داده‌های منبعی را که در حال تغییر است اصلاح کنند؛ کنترل‌کننده‌های validating چنین کاری نمی‌توانند بکنند.

admission controllerهای کوبرنتیز {{< skew currentVersion >}} شامل [فهرست](#what-does-each-admission-controller-do) زیر هستند، در باینری `kube-apiserver` کامپایل شده‌اند و تنها مدیر کلاستر می‌تواند آن‌ها را پیکربندی کند.

### نقاط توسعه کنترل پذیرش

در میان کل [فهرست](#what-does-each-admission-controller-do)، چهار کنترل‌کننده ویژه وجود دارد:
[MutatingAdmissionWebhook](#mutatingadmissionwebhook)،
[MutatingAdmissionPolicy](#mutatingadmissionpolicy)،
[ValidatingAdmissionWebhook](#validatingadmissionwebhook) و
[ValidatingAdmissionPolicy](#validatingadmissionpolicy).
دو کنترل‌کننده webhook به‌ترتیب، [webhookهای کنترل پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks) از نوع mutating و validating را اجرا می‌کنند که در API پیکربندی شده‌اند. MutatingAdmissionPolicy و ValidatingAdmissionPolicy روشی برای تعبیه کد تغییر/اعتبارسنجی اعلانی (declarative) در درون API فراهم می‌کنند، بدون آنکه به فراخوانی‌های HTTP خارجی وابسته باشند.

می‌توانید از این چهار admission controller برای سفارشی‌سازی رفتار کلاستر در زمان پذیرش استفاده کنید.

### مراحل کنترل پذیرش

فرایند کنترل پذیرش در دو مرحله پیش می‌رود. در مرحله نخست، admission controllerهای mutating اجرا می‌شوند. در مرحله دوم، admission controllerهای validating اجرا می‌شوند. دوباره یادآوری می‌شود که برخی از کنترل‌کننده‌ها هر دو نقش را دارند.

اگر هر یک از کنترل‌کننده‌ها در هر یک از این دو مرحله درخواست را رد کنند، کل درخواست بلافاصله رد می‌شود و خطایی به کاربر نهایی بازگردانده می‌شود.

سرانجام، admission controllerها علاوه بر آنکه گاهی آبجکت مورد نظر را تغییر می‌دهند، ممکن است گاهی عوارض جانبی (side effects) نیز داشته باشند؛ یعنی در جریان پردازش درخواست، منابع مرتبط را تغییر دهند. افزایش میزان مصرف سهمیه (quota) مثال شاخص دلیل ضرورت این موضوع است. هر عارضه جانبی از این دست به یک فرایند بازپس‌گیری یا هم‌ترازسازی (reconciliation) متناظر نیاز دارد، زیرا یک admission controller مشخص با اطمینان نمی‌داند که درخواست داده‌شده از همه admission controllerهای دیگر عبور خواهد کرد یا نه.

ترتیب این فراخوانی‌ها را در زیر می‌توانید ببینید.

{{< figure src="/docs/reference/access-authn-authz/admission-control-phases.svg" alt="Sequence diagram for kube-apiserver handling requests during the admission phase showing mutation webhooks, followed by validatingadmissionpolicies and finally validating webhooks. It shows that the continue until the first rejection, or being accepted by all of them. It also shows that mutations by mutating webhooks cause all previously called webhooks to be called again." class="diagram-large" link="[https://mermaid.live/edit#pako:eNqtVm1v2zYQ_isHDcZazO-O34QhQJdiazAEKJquAwZ9oaSzxZoiNZJy4gT-7ztSL1bs5sPQ6otE8rm75-45inwOEpViEAa9HnxgewSrwKCFjZL2nj8hbIWKmRAHYAZsxg1wI3-2oNEUmFhMIS29UWZtYcLRaMttVsbDROWjHHXOeDr4aprPETemRDOardfjSPZ6z1xyGz5Hgc0wxygIo0BiaTUTUdCPgoYELUAUTKfFI03Tl8F_S5SJnyfjnGut9LvEKm1oyuoSj_1IAj215y9McxYLNJWFX6qWmbP6bbf1sX-aTRcJzl3sc8hnfLQ3SijtgQ8Zt3gGE0oVXRS85k8qixSxg9tqPJyBvpV6JI_HY68XyUg2FXjP2Vaz3E05OxLxc6URaYXAhB1YokRqamBJgsbwmAtuD31gMgWTqVKkECOURcqcmLhHfQDLc_QO0so9-RtWAcjJezSJ7hbxvubSol20XRnjgBXcoCaXkFE4weWW-obAxhpqG-3GnmaaU19wJaHImEFH68Gt5aVl1k0_YJwptTN9ci2EeiCi8QH2THBiTcjWQaEETzgan92GS9-4J1zraAgn-rfWB3QVY9bzSaj2XFJbl_QWfmrDtXFN_5V6nuL0gVKM0bl0ZS1sxYjCgdo4g_wsAhNGdcM0qRlnVg069CBhpUHvrtC456o0lEdCY4rTgmjTkXL1LNsyLmuRjk07FExbqkfBpIW_SAm3h_37cvndx1u3-ifJpiVaKqGbuffqfQNd2szB3RupSEml0y9-Qmn-5MdtT74wTfMbq4W3bnW_oYprJSqDWD3CH5SNiZVWlyD4NdbXN1XWlUBn4lzSvWsKTEHb79bxJf7LqWPIojM6s0GZulJXA1_YwfW1L1wIn6pGhzc43A77kGikDQYMCpW-revvgN6AihZ2a0md59WiJnbJJhkmu2qqoP9oxcA0cd1_B353G5zapc3uY70TTl3oNXPhGkwIt3KvdnhmdDiZtAsnlncq5ZuDa_-q3qBi_3rDNyARU0zfvqjN6wz_rvv4fzGsjX44RVK_ZdjRu6kicOkgrunEK7FPVi3rc0edynaWXib86XspN2X9bsqX-vwA0q3E1PvU8u5n3hGqPhxasNsfDuy2lotiCup7hGZPmdIfac4BuhsAhQv6dJjytLoE9IP62kHXG39ene4Z9JnihpXC-mOVzGjj_6NU3lhqVW6zINzQj5tG1fFYH7YNhJVW3R9k0owx5XRRuKuuU_5WRW4od9Q3in5UQTgZ-zBB-Bw8BuFgNpsOF_PF-mo-nkxmq-WsHxwINFkOr8aT5WoxW01Wy8l4fewHT57ZZDieL-fr8WI8W01XV7Px9PgfcW89xA](https://mermaid.live/edit#pako:eNqtVm1v2zYQ_isHDcZazO-O34QhQJdiazAEKJquAwZ9oaSzxZoiNZJy4gT-7ztSL1bs5sPQ6otE8rm75-45inwOEpViEAa9HnxgewSrwKCFjZL2nj8hbIWKmRAHYAZsxg1wI3-2oNEUmFhMIS29UWZtYcLRaMttVsbDROWjHHXOeDr4aprPETemRDOardfjSPZ6z1xyGz5Hgc0wxygIo0BiaTUTUdCPgoYELUAUTKfFI03Tl8F_S5SJnyfjnGut9LvEKm1oyuoSj_1IAj215y9McxYLNJWFX6qWmbP6bbf1sX-aTRcJzl3sc8hnfLQ3SijtgQ8Zt3gGE0oVXRS85k8qixSxg9tqPJyBvpV6JI_HY68XyUg2FXjP2Vaz3E05OxLxc6URaYXAhB1YokRqamBJgsbwmAtuD31gMgWTqVKkECOURcqcmLhHfQDLc_QO0so9-RtWAcjJezSJ7hbxvubSol20XRnjgBXcoCaXkFE4weWW-obAxhpqG-3GnmaaU19wJaHImEFH68Gt5aVl1k0_YJwptTN9ci2EeiCi8QH2THBiTcjWQaEETzgan92GS9-4J1zraAgn-rfWB3QVY9bzSaj2XFJbl_QWfmrDtXFN_5V6nuL0gVKM0bl0ZS1sxYjCgdo4g_wsAhNGdcM0qRlnVg069CBhpUHvrtC456o0lEdCY4rTgmjTkXL1LNsyLmuRjk07FExbqkfBpIW_SAm3h_37cvndx1u3-ifJpiVaKqGbuffqfQNd2szB3RupSEml0y9-Qmn-5MdtT74wTfMbq4W3bnW_oYprJSqDWD3CH5SNiZVWlyD4NdbXN1XWlUBn4lzSvWsKTEHb79bxJf7LqWPIojM6s0GZulJXA1_YwfW1L1wIn6pGhzc43A77kGikDQYMCpW-revvgN6AihZ2a0md59WiJnbJJhkmu2qqoP9oxcA0cd1_B353G5zapc3uY70TTl3oNXPhGkwIt3KvdnhmdDiZtAsnlncq5ZuDa_-q3qBi_3rDNyARU0zfvqjN6wz_rvv4fzGsjX44RVK_ZdjRu6kicOkgrunEK7FPVi3rc0edynaWXib86XspN2X9bsqX-vwA0q3E1PvU8u5n3hGqPhxasNsfDuy2lotiCup7hGZPmdIfac4BuhsAhQv6dJjytLoE9IP62kHXG39ene4Z9JnihpXC-mOVzGjj_6NU3lhqVW6zINzQj5tG1fFYH7YNhJVW3R9k0owx5XRRuKuuU_5WRW4od9Q3in5UQTgZ-zBB-Bw8BuFgNpsOF_PF-mo-nkxmq-WsHxwINFkOr8aT5WoxW01Wy8l4fewHT57ZZDieL-fr8WI8W01XV7Px9PgfcW89xA)" >}}

## چرا به آن‌ها نیاز دارم؟

چند قابلیت مهم کوبرنتیز برای آنکه به‌درستی پشتیبانی شوند، به فعال بودن یک admission controller نیاز دارند. در نتیجه، API server کوبرنتیزی که با مجموعه مناسبی از admission controllerها پیکربندی نشده باشد، سروری ناقص است و همه قابلیت‌هایی را که انتظار دارید پشتیبانی نخواهد کرد.

## چگونه یک admission controller را فعال کنم؟

فلگ `enable-admission-plugins` در API server کوبرنتیز فهرستی از افزونه‌های کنترل پذیرش را که با کاما از هم جدا شده‌اند می‌پذیرد تا پیش از تغییر آبجکت‌ها در کلاستر فراخوانی شوند. برای مثال، دستور زیر افزونه‌های کنترل پذیرش `NamespaceLifecycle` و `LimitRanger` را فعال می‌کند:

```shell
kube-apiserver --enable-admission-plugins=NamespaceLifecycle,LimitRanger ...
```

{{< note >}}
بسته به شیوه استقرار کلاستر کوبرنتیز و نحوه راه‌اندازی API server، ممکن است لازم باشد تنظیمات را به روش‌های متفاوتی اعمال کنید. برای مثال، اگر API server به‌صورت یک سرویس systemd مستقر شده باشد، ممکن است لازم باشد فایل unit مربوط به systemd را تغییر دهید؛ و اگر کوبرنتیز به‌صورت خودمیزبان (self-hosted) مستقر شده باشد، می‌توانید فایل مانیفست API server را تغییر دهید.
{{< /note >}}

## چگونه یک admission controller را غیرفعال کنم؟

فلگ `disable-admission-plugins` در API server کوبرنتیز فهرستی از افزونه‌های کنترل پذیرش را که با کاما از هم جدا شده‌اند می‌پذیرد تا غیرفعال شوند، حتی اگر در فهرست افزونه‌هایی باشند که به‌طور پیش‌فرض فعال هستند.

```shell
kube-apiserver --disable-admission-plugins=PodNodeSelector,AlwaysDeny ...
```

## کدام افزونه‌ها به‌طور پیش‌فرض فعال هستند؟

برای مشاهده اینکه کدام افزونه‌های پذیرش فعال هستند:

```shell
kube-apiserver -h | grep enable-admission-plugins
```

در کوبرنتیز {{< skew currentVersion >}}، افزونه‌های پیش‌فرض عبارت‌اند از:

```shell
CertificateApproval, CertificateSigning, CertificateSubjectRestriction, DefaultIngressClass, DefaultStorageClass, DefaultTolerationSeconds, LimitRanger, MutatingAdmissionPolicy, MutatingAdmissionWebhook, NamespaceLifecycle, PersistentVolumeClaimResize, PodSecurity, Priority, ResourceQuota, RuntimeClass, ServiceAccount, StorageObjectInUseProtection, TaintNodesByCondition, ValidatingAdmissionPolicy, ValidatingAdmissionWebhook
```

## هر admission controller چه کاری انجام می‌دهد؟

### AlwaysAdmit {#alwaysadmit}

{{< feature-state for_k8s_version="v1.13" state="deprecated" >}}

**نوع**: Validating.

این admission controller اجازه ورود همه podها به کلاستر را می‌دهد. این کنترل‌کننده **منسوخ‌شده (deprecated)** است، زیرا رفتار آن با نبودن هرگونه admission controller یکسان است.

### AlwaysDeny {#alwaysdeny}

{{< feature-state for_k8s_version="v1.13" state="deprecated" >}}

**نوع**: Validating.

همه درخواست‌ها را رد می‌کند. AlwaysDeny **منسوخ‌شده (deprecated)** است، زیرا معنای واقعی ندارد.

### AlwaysPullImages {#alwayspullimages}

**نوع**: Mutating و Validating.

این admission controller هر Pod جدید را طوری تغییر می‌دهد که سیاست دریافت ایمیج (image pull policy) به‌اجبار روی `Always` تنظیم شود. این کار در یک کلاستر چندمستاجری (multitenant) مفید است تا کاربران مطمئن باشند ایمیج‌های خصوصی آن‌ها فقط توسط کسانی قابل استفاده است که اعتبارنامه‌های لازم برای دریافت آن‌ها را دارند. بدون این admission controller، پس از آنکه یک ایمیج روی یک نود دریافت شد، هر podی از هر کاربری می‌تواند با دانستن نام ایمیج از آن استفاده کند (با فرض آنکه Pod روی نود مناسب زمان‌بندی شود)، بی‌آنکه هیچ بررسی مجوزی روی ایمیج انجام شود. وقتی این admission controller فعال باشد، ایمیج‌ها همیشه پیش از راه‌اندازی کانتینرها دریافت می‌شوند، که به این معنی است که اعتبارنامه‌های معتبر الزامی هستند.

### CertificateApproval {#certificateapproval}

**نوع**: Validating.

این admission controller درخواست‌های تأیید منابع CertificateSigningRequest را زیر نظر می‌گیرد و بررسی‌های مجوز اضافی انجام می‌دهد تا اطمینان حاصل کند کاربر تأییدکننده اجازه **approve** کردن درخواست‌های گواهی با `spec.signerName` درخواست‌شده روی منبع CertificateSigningRequest را دارد.

برای اطلاعات بیشتر درباره مجوزهای لازم برای انجام اقدامات مختلف روی منابع CertificateSigningRequest، به [درخواست‌های امضای گواهی (Certificate Signing Requests)](/docs/reference/access-authn-authz/certificate-signing-requests/) مراجعه کنید.

### CertificateSigning {#certificatesigning}

**نوع**: Validating.

این admission controller به‌روزرسانی‌های فیلد `status.certificate` در منابع CertificateSigningRequest را زیر نظر می‌گیرد و بررسی‌های مجوز اضافی انجام می‌دهد تا اطمینان حاصل کند کاربر امضاکننده اجازه **sign** کردن درخواست‌های گواهی با `spec.signerName` درخواست‌شده روی منبع CertificateSigningRequest را دارد.

برای اطلاعات بیشتر درباره مجوزهای لازم برای انجام اقدامات مختلف روی منابع CertificateSigningRequest، به [درخواست‌های امضای گواهی (Certificate Signing Requests)](/docs/reference/access-authn-authz/certificate-signing-requests/) مراجعه کنید.

### CertificateSubjectRestriction {#certificatesubjectrestriction}

**نوع**: Validating.

این admission controller ایجاد منابع CertificateSigningRequest را که `spec.signerName` آن‌ها `kubernetes.io/kube-apiserver-client` است زیر نظر می‌گیرد. هر درخواستی را که «group» (یا «organization attribute») آن `system:masters` باشد رد می‌کند.

### DefaultIngressClass {#defaultingressclass}

**نوع**: Mutating.

این admission controller ایجاد آبجکت‌های `Ingress` را که هیچ ingress class مشخصی درخواست نکرده‌اند زیر نظر می‌گیرد و به‌طور خودکار یک ingress class پیش‌فرض به آن‌ها اضافه می‌کند. به این ترتیب، کاربرانی که ingress class خاصی درخواست نمی‌کنند، لازم نیست اصلاً نگران آن باشند و کلاس پیش‌فرض را دریافت خواهند کرد.

وقتی هیچ ingress class پیش‌فرضی پیکربندی نشده باشد، این admission controller هیچ کاری انجام نمی‌دهد. وقتی بیش از یک ingress class به‌عنوان پیش‌فرض علامت‌گذاری شده باشد، هر درخواست ایجاد `Ingress` را با یک خطا رد می‌کند و مدیر باید آبجکت‌های `IngressClass` خود را بازبینی کند و تنها یکی از آن‌ها را (با حاشیه‌نویسی (annotation) «ingressclass.kubernetes.io/is-default-class») به‌عنوان پیش‌فرض علامت‌گذاری کند. این admission controller هر به‌روزرسانی `Ingress` را نادیده می‌گیرد؛ فقط هنگام ایجاد عمل می‌کند.

برای اطلاعات بیشتر درباره ingress classها و نحوه علامت‌گذاری یکی از آن‌ها به‌عنوان پیش‌فرض، مستندات [Ingress](/docs/concepts/services-networking/ingress/) را ببینید.

### DefaultStorageClass {#defaultstorageclass}

**نوع**: Mutating.

این admission controller ایجاد آبجکت‌های `PersistentVolumeClaim` را که هیچ storage class مشخصی درخواست نکرده‌اند زیر نظر می‌گیرد و به‌طور خودکار یک storage class پیش‌فرض به آن‌ها اضافه می‌کند. به این ترتیب، کاربرانی که storage class خاصی درخواست نمی‌کنند، لازم نیست اصلاً نگران آن باشند و کلاس پیش‌فرض را دریافت خواهند کرد.

وقتی هیچ `StorageClass` پیش‌فرضی وجود نداشته باشد، این admission controller کاری انجام نمی‌دهد. وقتی بیش از یک storage class به‌عنوان پیش‌فرض علامت‌گذاری شده باشد و سپس یک `PersistentVolumeClaim` بدون تنظیم `storageClassName` ایجاد کنید، کوبرنتیز از آخرین `StorageClass` پیش‌فرضی که ایجاد شده است استفاده می‌کند. وقتی یک `PersistentVolumeClaim` با `volumeName` مشخص ایجاد می‌شود، اگر پس از اعمال هر StorageClass پیش‌فرض بر آن، `storageClassName` مربوط به حجم ایستا (static volume) با `storageClassName` موجود در `PersistentVolumeClaim` مطابقت نداشته باشد، در وضعیت pending باقی می‌ماند. این admission controller هر به‌روزرسانی `PersistentVolumeClaim` را نادیده می‌گیرد؛ فقط هنگام ایجاد عمل می‌کند.

برای اطلاعات درباره persistent volume claimها و storage classها و نحوه علامت‌گذاری یک storage class به‌عنوان پیش‌فرض، مستندات [persistent volume](/docs/concepts/storage/persistent-volumes/) را ببینید.

### DefaultTolerationSeconds {#defaulttolerationseconds}

**نوع**: Mutating.

این admission controller، بر اساس پارامترهای ورودی k8s-apiserver یعنی `default-not-ready-toleration-seconds` و `default-unreachable-toleration-seconds`، تلرانس (toleration) پیش‌فرض از نوع بخشش را برای podها تنظیم می‌کند تا taintهای `notready:NoExecute` و `unreachable:NoExecute` را تحمل کنند، مشروط بر آنکه podها از قبل برای taintهای `node.kubernetes.io/not-ready:NoExecute` یا `node.kubernetes.io/unreachable:NoExecute` toleration نداشته باشند. مقدار پیش‌فرض `default-not-ready-toleration-seconds` و `default-unreachable-toleration-seconds` برابر ۵ دقیقه است.

### DenyServiceExternalIPs

**نوع**: Validating.

این admission controller هر گونه استفاده جدید از فیلد `externalIPs` در `Service` را رد می‌کند. این قابلیت بسیار قدرتمند است (امکان رهگیری ترافیک شبکه را فراهم می‌کند) و به‌خوبی توسط سیاست‌ها کنترل نمی‌شود. وقتی این کنترل‌کننده فعال باشد، کاربران کلاستر نمی‌توانند Serviceهای جدیدی ایجاد کنند که از `externalIPs` استفاده می‌کنند و نمی‌توانند مقادیر جدیدی به `externalIPs` آبجکت‌های `Service` موجود اضافه کنند. استفاده‌های موجود از `externalIPs` تحت تأثیر قرار نمی‌گیرند و کاربران می‌توانند مقادیری را از `externalIPs` آبجکت‌های `Service` موجود حذف کنند.

بیشتر کاربران اصلاً به این قابلیت نیاز ندارند و مدیران کلاستر باید غیرفعال کردن آن را در نظر بگیرند. کلاسترهایی که واقعاً نیاز به استفاده از این قابلیت دارند، باید استفاده از یک سیاست سفارشی را برای مدیریت کاربرد آن در نظر بگیرند.

این admission controller به‌طور پیش‌فرض غیرفعال است.

### EventRateLimit {#eventratelimit}

{{< feature-state for_k8s_version="v1.13" state="alpha" >}}

**نوع**: Validating.

این admission controller مشکل هجوم درخواست‌های ذخیره‌سازی Eventهای جدید به API server را کاهش می‌دهد. مدیر کلاستر می‌تواند محدودیت‌های نرخ Event را به این روش مشخص کند:

* فعال کردن admission controller با نام `EventRateLimit`؛
* ارجاع به یک فایل پیکربندی `EventRateLimit` از درون فایلی که به فلگ خط فرمان `--admission-control-config-file` در API server داده می‌شود:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: EventRateLimit
    path: eventconfig.yaml
...
```

چهار نوع محدودیت وجود دارد که می‌توان در پیکربندی مشخص کرد:

 * `Server`: همه درخواست‌های Event (ایجاد یا تغییر) که API server دریافت می‌کند، یک bucket مشترک را به اشتراک می‌گذارند.
 * `Namespace`: هر فضای نام (namespace) یک bucket اختصاصی دارد.
 * `User`: به هر کاربر یک bucket اختصاص داده می‌شود.
 * `SourceAndObject`: به ازای هر ترکیب از منبع (source) و آبجکت درگیرِ رویداد، یک bucket اختصاص داده می‌شود.

در زیر نمونه‌ای از `eventconfig.yaml` برای چنین پیکربندی‌ای آمده است:

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

این admission controller به‌طور پیش‌فرض غیرفعال است.

### ExtendedResourceToleration {#extendedresourcetoleration}

**نوع**: Mutating.

این افزونه ایجاد نودهای اختصاصی دارای منابع توسعه‌یافته (extended resources) را تسهیل می‌کند. اگر اپراتورها بخواهند نودهای اختصاصی با منابع توسعه‌یافته (مانند GPUها، FPGAها و غیره) ایجاد کنند، انتظار می‌رود [نود را taint کنند](/docs/concepts/scheduling-eviction/taint-and-toleration/#example-use-cases) و نام منبع توسعه‌یافته را به‌عنوان کلید قرار دهند. این admission controller، در صورت فعال بودن، به‌طور خودکار tolerationهای مربوط به این taintها را به podهایی که منابع توسعه‌یافته درخواست می‌کنند اضافه می‌کند، بنابراین کاربران لازم نیست این tolerationها را به‌صورت دستی اضافه کنند.

این admission controller به‌طور پیش‌فرض غیرفعال است.

### ImagePolicyWebhook {#imagepolicywebhook}

**نوع**: اعتبارسنجی (Validating).

کنترل‌کننده پذیرش ImagePolicyWebhook به یک webhook در بک‌اند اجازه می‌دهد تصمیم‌های پذیرش را اتخاذ کند.

این کنترل‌کننده پذیرش به‌صورت پیش‌فرض غیرفعال است.

#### قالب فایل پیکربندی {#imagereview-config-file-format}

ImagePolicyWebhook برای تنظیم گزینه‌های رفتاری بک‌اند از یک فایل پیکربندی استفاده می‌کند.
این فایل می‌تواند به قالب json یا yaml باشد و قالب آن به شرح زیر است:

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

فایل پیکربندی ImagePolicyWebhook را از طریق فایلی که به فلگ خط فرمان `--admission-control-config-file` سرور API داده می‌شود ارجاع دهید:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: ImagePolicyWebhook
    path: imagepolicyconfig.yaml
...
```

همچنین می‌توانید پیکربندی را مستقیماً درون همان فایل جاسازی کنید:

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

فایل پیکربندی ImagePolicyWebhook باید به فایلی با قالب
[kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
ارجاع دهد که اتصال به بک‌اند را برقرار می‌کند.
الزامی است که بک‌اند از طریق TLS ارتباط برقرار کند.

فیلد `cluster` در فایل kubeconfig باید به سرویس راه دور اشاره کند و فیلد `user`
باید شامل authorizer بازگردانده‌شده باشد.

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

برای پیکربندی‌های HTTP بیشتر، به مستندات
[kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) مراجعه کنید.

#### بارهای درخواست (Request payloads)

هنگامی که باید تصمیم پذیرش گرفته شود، سرور API یک آبجکت `ImageReview` از نوع
`imagepolicy.k8s.io/v1alpha1` را که به‌صورت JSON سریال‌سازی شده و عمل موردنظر را توصیف می‌کند، با متد POST ارسال می‌کند.
این آبجکت شامل فیلدهایی است که کانتینرهای در حال پذیرش را توصیف می‌کنند، و همچنین
هر حاشیه‌نویسی (annotation) از Pod که با `*.image-policy.k8s.io/*` مطابقت داشته باشد.

{{< note >}}
آبجکت‌های API مربوط به webhook تابع همان قواعد سازگاری نسخه‌بندی هستند که برای
سایر آبجکت‌های API کوبرنتیز اعمال می‌شود. پیاده‌سازان باید از تعهدات سازگاری سهل‌گیرانه‌تر
برای آبجکت‌های آلفا آگاه باشند و برای اطمینان از deserialize صحیح، فیلد `apiVersion` درخواست را بررسی کنند.
علاوه بر این، سرور API باید گروه افزونه‌های API با نام `imagepolicy.k8s.io/v1alpha1` را فعال کند
(`--runtime-config=imagepolicy.k8s.io/v1alpha1=true`).
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

انتظار می‌رود سرویس راه دور فیلد `status` درخواست را پر کند و
با اجازه دادن یا اجازه ندادن دسترسی پاسخ دهد. فیلد `spec` در بدنه پاسخ نادیده گرفته می‌شود و
می‌توان آن را حذف کرد. یک پاسخ مجاز‌کننده به این صورت خواهد بود:

```json
{
  "apiVersion": "imagepolicy.k8s.io/v1alpha1",
  "kind": "ImageReview",
  "status": {
    "allowed": true
  }
}
```

برای رد کردن دسترسی، سرویس پاسخ زیر را بازمی‌گرداند:

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
آبجکت‌های `ImageReview` شامل تمام ایمیج‌های موجود در Podهایی خواهند بود که قرار است به‌عنوان
کانتینر اجرا شوند. این شامل ایمیج‌هایی است که در فیلدهای containers،
initContainers یا ephemeralContainers در مشخصات Pod تعریف شده‌اند. در نتیجه،
ایمیج‌هایی که در image volumeها قرار دارند، در حوزه ImagePolicyWebhook نیستند.
{{< /note >}}

برای مستندات بیشتر به
[API مربوط به `imagepolicy.v1alpha1`](/docs/reference/config-api/imagepolicy.v1alpha1/) مراجعه کنید.

#### گسترش با حاشیه‌نویسی‌ها (Annotations)

تمام حاشیه‌نویسی‌های (annotation) یک Pod که با `*.image-policy.k8s.io/*` مطابقت داشته باشند، به webhook ارسال می‌شوند.
ارسال حاشیه‌نویسی‌ها به کاربرانی که از بک‌اند سیاست ایمیج آگاه هستند اجازه می‌دهد
اطلاعات اضافی را به آن ارسال کنند، و به پیاده‌سازی‌های مختلف بک‌اند اجازه می‌دهد
اطلاعات متفاوتی را بپذیرند.

نمونه‌هایی از اطلاعاتی که ممکن است در اینجا قرار دهید عبارت‌اند از:

* درخواست «break glass» برای نادیده گرفتن یک سیاست در شرایط اضطراری.
* شماره تیکت از یک سامانه تیکتینگ که درخواست break-glass را مستند می‌کند
* ارائه یک راهنمایی به سرور سیاست درباره imageID ایمیجی که ارائه می‌شود، تا از جست‌وجوی مجدد آن جلوگیری شود

در هر صورت، حاشیه‌نویسی‌ها توسط کاربر ارائه می‌شوند و کوبرنتیز به هیچ وجه آن‌ها را اعتبارسنجی نمی‌کند.

### LimitPodHardAntiAffinityTopology {#limitpodhardantiaffinitytopology}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش هر Podی را که در `requiredDuringSchedulingIgnoredDuringExecution`
کلید توپولوژی `AntiAffinity` غیر از `kubernetes.io/hostname` تعریف کرده باشد، رد می‌کند.

این کنترل‌کننده پذیرش به‌صورت پیش‌فرض غیرفعال است.

### LimitRanger {#limitranger}

**نوع**: تغییردهنده و اعتبارسنجی (Mutating and Validating).

این کنترل‌کننده پذیرش درخواست ورودی را بررسی می‌کند و اطمینان حاصل می‌کند که هیچ‌یک از
محدودیت‌های برشمرده‌شده در آبجکت `LimitRange` در یک `Namespace` را نقض نکند. اگر در استقرار کوبرنتیز خود
از آبجکت‌های `LimitRange` استفاده می‌کنید، باید از این کنترل‌کننده پذیرش برای
اعمال آن محدودیت‌ها استفاده کنید. LimitRanger همچنین می‌تواند برای اعمال درخواست‌های منبع پیش‌فرض به Podهایی
که هیچ‌کدام را مشخص نکرده‌اند به کار رود؛ در حال حاضر، LimitRanger پیش‌فرض یک نیاز ۰٫۱ CPU را برای تمام
Podها در فضای نام (namespace) `default` اعمال می‌کند.

برای جزئیات بیشتر، [مرجع API مربوط به LimitRange](/docs/reference/kubernetes-api/core/limit-range-v1/)
و [نمونه LimitRange](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/) را ببینید.

### MutatingAdmissionPolicy {#mutatingadmissionpolicy}

**نوع**: تغییردهنده (Mutating).

[این کنترل‌کننده پذیرش](/docs/reference/access-authn-authz/mutating-admission-policy/) از Common Expression Language (CEL) برای اعلام تغییرات بر منابع استفاده می‌کند. تغییرات را می‌توان یا با یک apply configuration که با راهبرد ادغام server side apply ادغام می‌شود، یا با یک JSON patch تعریف کرد.
این کنترل‌کننده زمانی فعال می‌شود که هم feature gate با نام `mutatingadmissionpolicy` و هم گروه/نسخه `admissionregistration.k8s.io/v1alpha1` فعال باشند.
اگر هر یک از MutatingAdmissionPolicyها شکست بخورد، درخواست شکست می‌خورد.

### MutatingAdmissionWebhook {#mutatingadmissionwebhook}

**نوع**: تغییردهنده (Mutating).

این کنترل‌کننده پذیرش هر webhook تغییردهنده‌ای را که با درخواست مطابقت داشته باشد فراخوانی می‌کند. webhookهای
منطبق به‌صورت سریالی فراخوانی می‌شوند؛ هر یک در صورت تمایل می‌تواند آبجکت را تغییر دهد.

این کنترل‌کننده پذیرش (همان‌گونه که از نامش پیداست) فقط در فاز تغییر (mutating) اجرا می‌شود.

اگر webhookی که توسط این کنترل‌کننده فراخوانی می‌شود عوارض جانبی داشته باشد (برای مثال، کاهش سهمیه)،
*باید* یک سیستم تطبیق (reconciliation) داشته باشد، زیرا تضمین نمی‌شود که webhookهای بعدی
یا کنترل‌کننده‌های پذیرش اعتبارسنجی اجازه دهند درخواست به پایان برسد.

اگر MutatingAdmissionWebhook را غیرفعال کنید، باید آبجکت `MutatingWebhookConfiguration` را نیز
در گروه/نسخه `admissionregistration.k8s.io/v1` از طریق فلگ `--runtime-config` غیرفعال کنید؛ هر دو به‌صورت پیش‌فرض فعال هستند.

#### هنگام نوشتن و نصب webhookهای تغییردهنده احتیاط کنید

* ممکن است کاربران سردرگم شوند، زیرا آبجکت‌هایی که تلاش می‌کنند ایجاد کنند با
  آنچه دریافت می‌کنند متفاوت است.
* حلقه‌های کنترلی داخلی ممکن است زمانی که آبجکت‌هایی که تلاش می‌کنند ایجاد کنند
  هنگام خواندن مجدد متفاوت باشند، دچار اختلال شوند.
  * تنظیم فیلدهایی که در اصل تنظیم نشده بودند کمتر احتمال دارد مشکل ایجاد کند تا
    بازنویسی فیلدهایی که در درخواست اصلی تنظیم شده بودند. از انجام مورد دوم خودداری کنید.
* تغییرات آتی در حلقه‌های کنترلی برای منابع داخلی یا منابع شخص ثالث
  ممکن است webhookهایی را که امروز به‌خوبی کار می‌کنند از کار بیندازد. حتی پس از نهایی شدن API نصب webhook،
  تضمینی وجود ندارد که تمام رفتارهای ممکن webhook برای همیشه پشتیبانی شوند.

### NamespaceAutoProvision {#namespaceautoprovision}

**نوع**: تغییردهنده (Mutating).

این کنترل‌کننده پذیرش تمام درخواست‌های ورودی روی منابع دارای فضای نام را بررسی می‌کند و
وجود فضای نام ارجاع‌شده را وارسی می‌کند.
اگر فضای نام پیدا نشود، آن را ایجاد می‌کند.
این کنترل‌کننده پذیرش در استقرارهایی مفید است که نمی‌خواهند ایجاد
فضای نام پیش از استفاده از آن را محدود کنند.

### NamespaceExists {#namespaceexists}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش تمام درخواست‌ها روی منابع دارای فضای نام، به‌جز خود `Namespace`، را بررسی می‌کند.
اگر فضای نام ارجاع‌شده در یک درخواست وجود نداشته باشد، درخواست رد می‌شود.

### NamespaceLifecycle {#namespacelifecycle}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش تضمین می‌کند که در یک `Namespace` که در حال خاتمه یافتن است نمی‌توان
آبجکت جدید ایجاد کرد، و اطمینان می‌دهد درخواست‌ها در یک `Namespace` ناموجود رد می‌شوند.
این کنترل‌کننده پذیرش همچنین از حذف سه فضای نام رزرو‌شده سیستمی یعنی `default`،
`kube-system` و `kube-public` جلوگیری می‌کند.

حذف یک `Namespace` دنباله‌ای از عملیات را آغاز می‌کند که تمام آبجکت‌ها (Podها، سرویس‌ها
و غیره) در آن فضای نام را حذف می‌کند. برای تضمین یکپارچگی آن فرایند، اکیداً توصیه می‌کنیم
این کنترل‌کننده پذیرش اجرا شود.

### NodeDeclaredFeatureValidator {#nodedeclaredfeaturevalidator}

{{< feature-state feature_gate_name="NodeDeclaredFeatures" >}}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش نوشتن‌ها روی Podهای متصل‌شده (bound) را رهگیری می‌کند تا اطمینان حاصل شود
تغییرات با ویژگی‌هایی که نودی که Pod در حال حاضر روی آن اجرا می‌شود اعلام کرده سازگار هستند. این کنترل‌کننده از فیلد
`.status.declaredFeatures` در Node برای
تعیین مجموعه ویژگی‌های فعال استفاده می‌کند. اگر به‌روزرسانی Pod به ویژگی‌ای نیاز داشته باشد که
در فهرست ویژگی‌های نود فعلی آن نباشد، کنترل‌کننده پذیرش
درخواست به‌روزرسانی را رد می‌کند. این کار از بروز خطاهای زمان اجرا ناشی از
ناسازگاری ویژگی‌ها پس از زمان‌بندی Pod جلوگیری می‌کند.

اگر feature gate با نام [`NodeDeclaredFeatures`](/docs/reference/command-line-tools-reference/feature-gates/#NodeDeclaredFeatures) فعال باشد،
این کنترل‌کننده پذیرش به‌صورت پیش‌فرض فعال است.

### NodeRestriction {#noderestriction}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش آبجکت‌های `Node` و `Pod` را که یک kubelet می‌تواند تغییر دهد محدود می‌کند. برای اینکه این کنترل‌کننده پذیرش بر kubeletها اعمال شود،
kubeletها باید از اعتبارنامه‌هایی در گروه `system:nodes` استفاده کنند، با نام کاربری به شکل `system:node:<nodeName>`.
چنین kubeletهایی فقط مجاز خواهند بود آبجکت API مربوط به `Node` خودشان را تغییر دهند، و فقط آبجکت‌های API از نوع `Pod` را که به نود آن‌ها متصل شده‌اند تغییر دهند.
kubeletها مجاز نیستند taintها را از آبجکت API مربوط به `Node` خود به‌روزرسانی یا حذف کنند.

افزونه پذیرش `NodeRestriction` از حذف آبجکت API مربوط به `Node` توسط kubeletها جلوگیری می‌کند،
و تغییر برچسب‌ها با پیشوندهای `kubernetes.io/` یا `k8s.io/` توسط kubelet را به شرح زیر اعمال می‌کند:

* **ممنوع** (kubeletها از تغییر این‌ها منع می‌شوند):
  * برچسب‌هایی با پیشوند `node-restriction.kubernetes.io/`. این پیشوند برای برچسب‌گذاری آبجکت‌های `Node` توسط مدیران جهت جداسازی بار کاری رزرو شده است.
  * برچسب‌هایی با پیشوند `node-role.kubernetes.io/` (برای مثال: `node-role.kubernetes.io/control-plane`). این برچسب‌ها محدود شده‌اند تا نودهای بدون سطح دسترسی لازم نتوانند نقش‌های کلاستر را برای خود اعلام کنند.
* **مجاز** (kubeletها می‌توانند این‌ها را اضافه/حذف/به‌روزرسانی کنند):
  * `kubernetes.io/hostname`
  * `kubernetes.io/arch`
  * `kubernetes.io/os`
  * `beta.kubernetes.io/instance-type`
  * `node.kubernetes.io/instance-type`
  * `failure-domain.beta.kubernetes.io/region` (منسوخ‌شده)
  * `failure-domain.beta.kubernetes.io/zone` (منسوخ‌شده)
  * `topology.kubernetes.io/region`
  * `topology.kubernetes.io/zone`
  * برچسب‌هایی با پیشوند `kubelet.kubernetes.io/`
  * برچسب‌هایی با پیشوند `node.kubernetes.io/`
* **رزروشده**:
  استفاده kubeletها از هر برچسب دیگری تحت پیشوندهای `kubernetes.io` یا `k8s.io` رزرو شده است.
  افزونه پذیرش `NodeRestriction` عموماً این برچسب‌ها را برای جلوگیری از خودبرچسب‌گذاری غیرمجاز مجاز نمی‌داند،
  اما ممکن است در آینده، در قالب ویژگی‌های بعدی، برچسب‌های بیشتری را تحت این پیشوندها مجاز کند.

زمانی که [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `ServiceAccountNodeAudienceRestriction`
فعال باشد، این افزونه پذیرش همچنین audienceهایی را که kubelet می‌تواند برای آن‌ها از طریق API مربوط به `TokenRequest`
توکن service account درخواست کند محدود می‌کند. kubelet فقط می‌تواند
برای audienceهایی توکن درخواست کند که پیش‌تر توسط Podهای روی آن نود ارجاع داده شده‌اند (از طریق حجم‌های (volume) توکن
service account از نوع projected یا درخواست‌های توکن درایور CSI)، یا برای audienceهایی که به‌صراحت
از طریق RBAC و با استفاده از فعل `request-serviceaccounts-token-audience` اعطا شده‌اند. برای جزئیات بیشتر،
[محدودیت audience توکن service account](/docs/reference/access-authn-authz/node/#service-account-token-audience-restriction) را ببینید.

نسخه‌های آتی ممکن است محدودیت‌های بیشتری اضافه کنند تا اطمینان حاصل شود kubeletها حداقل مجموعه
مجوزهای لازم برای عملکرد صحیح را دارند.

### OwnerReferencesPermissionEnforcement {#ownerreferencespermissionenforcement}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش از دسترسی به `metadata.ownerReferences` یک آبجکت محافظت می‌کند
به‌طوری که فقط کاربرانی که مجوز **delete** روی آبجکت را دارند بتوانند آن را تغییر دهند.
این کنترل‌کننده پذیرش همچنین از دسترسی به `metadata.ownerReferences[x].blockOwnerDeletion`
یک آبجکت محافظت می‌کند، به‌طوری که فقط کاربرانی که مجوز **update** روی زیرمنبع `finalizers`
مربوط به *مالک* (owner) ارجاع‌شده را دارند بتوانند آن را تغییر دهند.

### PersistentVolumeClaimResize {#persistentvolumeclaimresize}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش اعتبارسنجی‌های اضافی را برای بررسی درخواست‌های تغییر اندازه
`PersistentVolumeClaim` ورودی پیاده‌سازی می‌کند.

فعال‌سازی کنترل‌کننده پذیرش `PersistentVolumeClaimResize` توصیه می‌شود.
این کنترل‌کننده پذیرش به‌صورت پیش‌فرض از تغییر اندازه تمام claimها جلوگیری می‌کند، مگر اینکه `StorageClass` مربوط به claim
به‌صراحت با تنظیم `allowVolumeExpansion` روی `true` تغییر اندازه را فعال کرده باشد.

برای مثال: تمام `PersistentVolumeClaim`هایی که از `StorageClass` زیر ایجاد شوند از گسترش حجم (volume) پشتیبانی می‌کنند:

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

برای اطلاعات بیشتر درباره persistent volume claimها، [PersistentVolumeClaims](/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) را ببینید.

### PodNodeSelector {#podnodeselector}

{{< feature-state for_k8s_version="v1.5" state="alpha" >}}

**نوع**: اعتبارسنجی (Validating).

این کنترل‌کننده پذیرش با خواندن یک حاشیه‌نویسی (annotation) فضای نام و یک پیکربندی سراسری، مقدار پیش‌فرض و محدودیت
انتخابگرهای نود (node selector) قابل استفاده در یک فضای نام را تعیین می‌کند.

این کنترل‌کننده پذیرش به‌صورت پیش‌فرض غیرفعال است.

#### قالب فایل پیکربندی

`PodNodeSelector` برای تنظیم گزینه‌های رفتاری بک‌اند از یک فایل پیکربندی استفاده می‌کند.
توجه داشته باشید که قالب فایل پیکربندی در یک نسخه آینده به یک فایل نسخه‌بندی‌شده تغییر خواهد کرد.
این فایل می‌تواند به قالب json یا yaml باشد و قالب آن به شرح زیر است:

```yaml
podNodeSelectorPluginConfig:
  clusterDefaultNodeSelector: name-of-node-selector
  namespace1: name-of-node-selector
  namespace2: name-of-node-selector
```

فایل پیکربندی `PodNodeSelector` را از طریق فایلی که به فلگ خط فرمان
`--admission-control-config-file` سرور API داده می‌شود ارجاع دهید:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: PodNodeSelector
  path: podnodeselector.yaml
...
```

#### قالب حاشیه‌نویسی پیکربندی

`PodNodeSelector` از کلید حاشیه‌نویسی `scheduler.alpha.kubernetes.io/node-selector` برای تخصیص
انتخابگرهای نود به فضاهای نام استفاده می‌کند.

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
   از مقدار آن به‌عنوان انتخابگر نود استفاده می‌شود.
2. اگر فضای نام چنین حاشیه‌نویسی‌ای نداشته باشد، از `clusterDefaultNodeSelector` تعریف‌شده در
   فایل پیکربندی افزونه `PodNodeSelector` به‌عنوان انتخابگر نود استفاده می‌شود.
3. انتخابگر نود Pod با انتخابگر نود فضای نام از نظر تعارض ارزیابی می‌شود. تعارض
   منجر به رد درخواست می‌شود.
4. انتخابگر نود Pod با انتخابگر مجاز مختص فضای نام که در فایل پیکربندی افزونه تعریف شده است ارزیابی می‌شود.
   تعارض منجر به رد درخواست می‌شود.

{{< note >}}
PodNodeSelector امکان اجبار Podها به اجرا روی نودهای دارای برچسب مشخص را فراهم می‌کند. همچنین افزونه پذیرش
PodTolerationRestriction را ببینید که اجازه می‌دهد از اجرای Podها روی نودهای دارای taint مشخص جلوگیری شود.
{{< /note >}}

### PodSecurity {#podsecurity}

{{< feature-state for_k8s_version="v1.25" state="stable" >}}

**نوع**: اعتبارسنجی (Validating).

کنترل‌کننده پذیرش PodSecurity، Podهای جدید را پیش از پذیرش بررسی می‌کند و بر اساس security context درخواستی و محدودیت‌های
[استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/) مجاز
برای فضای نامی که Pod در آن قرار خواهد گرفت، تعیین می‌کند که آیا باید پذیرفته شود یا خیر.

برای اطلاعات بیشتر، مستندات [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
را ببینید.

PodSecurity جایگزین کنترل‌کننده پذیرش قدیمی‌تری با نام PodSecurityPolicy شد.

### PodTolerationRestriction {#podtolerationrestriction}

{{< feature-state for_k8s_version="v1.7" state="alpha" >}}

**نوع**: تغییردهنده و اعتبارسنجی (Mutating and Validating).

کنترل‌کننده پذیرش PodTolerationRestriction هرگونه تعارض میان toleration‌های یک
Pod و toleration‌های فضای نام آن را بررسی می‌کند.
اگر تعارضی وجود داشته باشد، درخواست Pod را رد می‌کند.
سپس toleration‌هایی را که روی فضای نام حاشیه‌نویسی شده‌اند با toleration‌های Pod ادغام می‌کند.
toleration‌های حاصل با فهرستی از toleration‌های مجاز که روی فضای نام حاشیه‌نویسی شده است بررسی می‌شوند.
اگر بررسی موفق باشد، درخواست Pod پذیرفته می‌شود، در غیر این صورت رد می‌شود.

اگر فضای نام Pod هیچ toleration پیش‌فرض یا toleration مجاز حاشیه‌نویسی‌شده‌ای نداشته باشد، در صورت مشخص بودن،
toleration‌های پیش‌فرض سطح کلاستر یا فهرست toleration‌های مجاز سطح کلاستر به‌جای آن‌ها استفاده می‌شوند.

toleration‌ها برای یک فضای نام از طریق کلید حاشیه‌نویسی `scheduler.alpha.kubernetes.io/defaultTolerations` تخصیص داده می‌شوند.
فهرست toleration‌های مجاز را می‌توان از طریق کلید حاشیه‌نویسی `scheduler.alpha.kubernetes.io/tolerationsWhitelist` اضافه کرد.

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

این کنترل‌کننده پذیرش به‌صورت پیش‌فرض غیرفعال است.

### PodTopologyLabels {#podtopologylabels}

{{< feature-state feature_gate_name="PodTopologyLabelsAdmission" >}}

**نوع**: تغییر‌دهنده (Mutating)

کنترل‌کننده پذیرش PodTopologyLabels زیرمنبع‌های `pods/binding` مربوط به همه Podهایی را که به یک Node متصل (bind) شده‌اند تغییر می‌دهد و برچسب‌های توپولوژی منطبق با برچسب‌های Node مقصد را به آن‌ها اضافه می‌کند.
این کار باعث می‌شود برچسب‌های توپولوژی Node به‌عنوان برچسب‌های Pod در دسترس باشند و بتوان آن‌ها را از طریق
[Downward API](/docs/concepts/workloads/pods/downward-api/)
در اختیار کانتینرهای در حال اجرا قرار داد.
برچسب‌هایی که در نتیجه این کنترل‌کننده در دسترس قرار می‌گیرند، برچسب‌های
[topology.kubernetes.io/region](/docs/reference/labels-annotations-taints/#topologykubernetesioregion) و
[topology.kubernetes.io/zone](/docs/reference/labels-annotations-taints/#topologykubernetesiozone) هستند.

{{<note>}}
اگر هر webhook پذیرشِ تغییر‌دهنده‌ای برچسب‌های زیرمنبع `pods/binding` را اضافه یا اصلاح کند،
این تغییرات در نتیجه عملکرد این کنترل‌کننده به برچسب‌های Pod منتقل می‌شوند
و برچسب‌هایی را که کلید آن‌ها تداخل دارد بازنویسی می‌کنند.
{{</note>}}

این کنترل‌کننده پذیرش زمانی فعال می‌شود که feature gate با نام `PodTopologyLabelsAdmission` فعال باشد.

### Priority {#priority}

**نوع**: تغییر‌دهنده (Mutating) و اعتبارسنج (Validating).

کنترل‌کننده پذیرش Priority از فیلد `priorityClassName` استفاده می‌کند و مقدار صحیح (عددی) اولویت را در آن درج می‌کند.
اگر کلاس اولویت (priority class) پیدا نشود، Pod رد می‌شود.

### ResourceQuota {#resourcequota}

**نوع**: اعتبارسنج (Validating).

این کنترل‌کننده پذیرش، درخواست‌های ورودی را بررسی می‌کند و اطمینان می‌یابد که هیچ‌یک از محدودیت‌های تعریف‌شده در آبجکت `ResourceQuota` موجود در یک `Namespace` نقض نشود. اگر در استقرار کوبرنتیز خود از آبجکت‌های `ResourceQuota` استفاده می‌کنید، **باید** از این کنترل‌کننده پذیرش برای اعمال محدودیت‌های سهمیه استفاده کنید.

برای جزئیات بیشتر، [مرجع API مربوط به ResourceQuota](/docs/reference/kubernetes-api/core/resource-quota-v1/)
و [مثال سهمیه منابع (Resource Quota)](/docs/concepts/policy/resource-quotas/) را ببینید.

### RuntimeClass {#runtimeclass}

**نوع**: تغییر‌دهنده (Mutating) و اعتبارسنج (Validating).

اگر یک RuntimeClass را با پیکربندی [سربار Pod (Pod overhead)](/docs/concepts/scheduling-eviction/pod-overhead/) تعریف کنید،
این کنترل‌کننده پذیرش، Podهای ورودی را بررسی می‌کند.
در صورت فعال بودن، این کنترل‌کننده پذیرش هر درخواست ایجاد Pod را که از قبل مقدار overhead در آن تنظیم شده باشد، رد می‌کند.
برای Podهایی که در `.spec` خود یک RuntimeClass پیکربندی و انتخاب کرده‌اند،
این کنترل‌کننده پذیرش مقدار `.spec.overhead` را در Pod بر اساس مقدار تعریف‌شده در RuntimeClass متناظر تنظیم می‌کند.

برای اطلاعات بیشتر، همچنین [سربار Pod](/docs/concepts/scheduling-eviction/pod-overhead/) را ببینید.

### ServiceAccount {#serviceaccount}

**نوع**: تغییر‌دهنده (Mutating) و اعتبارسنج (Validating).

این کنترل‌کننده پذیرش، خودکارسازی مربوط به
[serviceAccountها](/docs/tasks/configure-pod-container/configure-service-account/) را پیاده‌سازی می‌کند.
پروژه کوبرنتیز قویاً توصیه می‌کند این کنترل‌کننده پذیرش فعال شود.
اگر قصد دارید از آبجکت‌های `ServiceAccount` در کوبرنتیز استفاده کنید، باید این کنترل‌کننده پذیرش را فعال کنید.

برای تقویت تدابیر امنیتی پیرامون Secretها، از فضاهای نام (namespace) جداگانه برای جداسازی دسترسی به Secretهای مونت‌شده استفاده کنید.

### StorageObjectInUseProtection

**نوع**: تغییر‌دهنده (Mutating).

افزونه `StorageObjectInUseProtection` فاینالایزرهای `kubernetes.io/pvc-protection` یا `kubernetes.io/pv-protection`
را به PersistentVolumeClaimها (PVC) یا PersistentVolumeهای (PV) تازه ایجادشده اضافه می‌کند.
اگر کاربر یک PVC یا PV را حذف کند، آن PVC یا PV تا زمانی که کنترل‌کننده حفاظت از PVC یا PV (PVC or PV Protection Controller)
فاینالایزر را از آن حذف نکرده باشد، پاک نخواهد شد.
برای اطلاعات دقیق‌تر،
[حفاظت از آبجکت ذخیره‌سازی در حال استفاده](/docs/concepts/storage/persistent-volumes/#storage-object-in-use-protection)
را ببینید.

### TaintNodesByCondition {#taintnodesbycondition}

**نوع**: تغییر‌دهنده (Mutating).

این کنترل‌کننده پذیرش، Nodeهای تازه ایجادشده را با {{< glossary_tooltip text="taint" term_id="taint" >}}های `NotReady` و `NoSchedule` علامت‌گذاری می‌کند. این taint کردن از بروز وضعیت رقابتی (race condition) جلوگیری می‌کند که ممکن است باعث شود Podها پیش از به‌روزرسانی taintها برای انعکاس دقیق وضعیت‌های گزارش‌شده، روی Nodeهای جدید زمان‌بندی شوند.

### ValidatingAdmissionPolicy {#validatingadmissionpolicy}

**نوع**: اعتبارسنج (Validating).

[این کنترل‌کننده پذیرش](/docs/reference/access-authn-authz/validating-admission-policy/) اعتبارسنجی CEL را برای درخواست‌های ورودیِ منطبق پیاده‌سازی می‌کند.
این کنترل‌کننده زمانی فعال می‌شود که هم feature gate با نام `validatingadmissionpolicy` و هم گروه/نسخه `admissionregistration.k8s.io/v1alpha1` فعال باشند.
اگر هر یک از ValidatingAdmissionPolicyها ناموفق باشد، درخواست ناموفق می‌شود.

### ValidatingAdmissionWebhook {#validatingadmissionwebhook}

**نوع**: اعتبارسنج (Validating).

این کنترل‌کننده پذیرش، همه webhookهای اعتبارسنجی را که با درخواست مطابقت دارند فراخوانی می‌کند. webhookهای منطبق به‌صورت موازی فراخوانی می‌شوند؛ اگر هر یک از آن‌ها درخواست را رد کند، درخواست ناموفق می‌شود. این کنترل‌کننده پذیرش فقط در مرحله اعتبارسنجی اجرا می‌شود؛ برخلاف webhookهایی که کنترل‌کننده پذیرش `MutatingAdmissionWebhook` فراخوانی می‌کند، webhookهایی که این کنترل‌کننده فراخوانی می‌کند نمی‌توانند آبجکت را تغییر دهند.

اگر webhookی که توسط این کنترل‌کننده فراخوانی می‌شود عوارض جانبی داشته باشد (برای مثال، کاهش سهمیه)، **باید** سازوکار تطبیق (reconciliation) داشته باشد، زیرا تضمینی وجود ندارد که webhookهای بعدی یا سایر کنترل‌کننده‌های پذیرشِ اعتبارسنج اجازه تکمیل درخواست را بدهند.

اگر ValidatingAdmissionWebhook را غیرفعال کنید، باید آبجکت `ValidatingWebhookConfiguration` را نیز در گروه/نسخه `admissionregistration.k8s.io/v1` از طریق فلگ `--runtime-config` غیرفعال کنید.

## آیا مجموعه‌ای از کنترل‌کننده‌های پذیرش توصیه‌شده برای استفاده وجود دارد؟

بله. کنترل‌کننده‌های پذیرش توصیه‌شده به‌صورت پیش‌فرض فعال هستند
(فهرست آن‌ها [اینجا](/docs/reference/command-line-tools-reference/kube-apiserver/#options) نمایش داده شده است)،
بنابراین نیازی به تعیین صریح آن‌ها نیست.
می‌توانید با استفاده از فلگ `--enable-admission-plugins` کنترل‌کننده‌های پذیرش بیشتری را علاوه بر مجموعه پیش‌فرض فعال کنید (**ترتیب اهمیتی ندارد**).
