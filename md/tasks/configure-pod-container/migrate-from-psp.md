---
title: مهاجرت از PodSecurityPolicy به کنترل‌کنندهٔ پذیرش داخلی PodSecurity
reviewers:
- tallclair
- liggitt
content_type: task
min-kubernetes-server-version: v1.22
weight: 260
---

<!-- overview -->

این صفحه فرایند مهاجرت از PodSecurityPolicyها به کنترل‌کنندهٔ پذیرش (admission controller) داخلی
PodSecurity را شرح می‌دهد. این کار را می‌توان با ترکیبی از اجرای آزمایشی (dry-run) و حالت‌های `audit` و
`warn` به‌طور مؤثر انجام داد، هرچند اگر از PSPهای تغییردهنده (mutating) استفاده شود، کار دشوارتر می‌شود.

## {{% heading "prerequisites" %}}

{{% version-check %}}

اگر در حال حاضر نسخه‌ای از کوبرنتیز به‌جز {{< skew currentVersion >}} را اجرا می‌کنید، بهتر است
این صفحه را در مستندات مربوط به نسخه‌ای از کوبرنتیز که واقعاً اجرا می‌کنید مشاهده کنید.

این صفحه فرض می‌کند که شما از پیش با مفاهیم پایهٔ [پذیرش امنیت Pod](/docs/concepts/security/pod-security-admission/)
آشنا هستید.

<!-- body -->

## رویکرد کلی

برای مهاجرت از PodSecurityPolicy به پذیرش امنیت Pod (Pod Security Admission) راهبردهای متعددی وجود دارد.
مراحل زیر یکی از مسیرهای ممکن برای مهاجرت است که هدف آن به حداقل رساندن هم خطر قطعی در محیط
عملیاتی و هم خطر ایجاد شکاف امنیتی است.

<!-- Keep section header numbering in sync with this list. -->
0. تصمیم بگیرید که آیا پذیرش امنیت Pod برای کاربرد شما مناسب است یا نه.
1. مجوزهای فضای نام را بازبینی کنید
2. PodSecurityPolicyها را ساده و استاندارد کنید
3. فضاهای نام را به‌روزرسانی کنید
   1. سطح امنیت Pod مناسب را شناسایی کنید
   2. سطح امنیت Pod را راستی‌آزمایی کنید
   3. سطح امنیت Pod را اعمال کنید
   4. PodSecurityPolicy را دور بزنید
4. فرایندهای ایجاد فضای نام را بازبینی کنید
5. PodSecurityPolicy را غیرفعال کنید

## ۰. تصمیم بگیرید که آیا پذیرش امنیت Pod برای شما مناسب است {#is-psa-right-for-you}

پذیرش امنیت Pod به‌گونه‌ای طراحی شده است که رایج‌ترین نیازهای امنیتی را بدون پیکربندی اضافه برآورده کند و
مجموعه‌ای استاندارد از سطوح امنیتی را در کلاسترهای مختلف فراهم آورد. با این حال، انعطاف‌پذیری آن از
PodSecurityPolicy کمتر است. به‌طور مشخص، قابلیت‌های زیر در PodSecurityPolicy پشتیبانی می‌شوند، اما در
پذیرش امنیت Pod پشتیبانی نمی‌شوند:

- **تنظیم محدودیت‌های امنیتی پیش‌فرض** - پذیرش امنیت Pod یک کنترل‌کنندهٔ پذیرش غیرتغییردهنده است؛
  یعنی پادها را پیش از اعتبارسنجی تغییر نمی‌دهد. اگر به این جنبه از PSP متکی بوده‌اید، باید یا بارهای
  کاری خود را طوری تغییر دهید که با محدودیت‌های امنیت Pod سازگار باشند، یا برای اعمال این تغییرات از یک
  [وب‌هوک پذیرش تغییردهنده](/docs/reference/access-authn-authz/extensible-admission-controllers/)
  استفاده کنید. برای جزئیات بیشتر، بخش [ساده‌سازی و استانداردسازی PodSecurityPolicyها](#simplify-psps) را در ادامه ببینید.
- **کنترل دقیق بر تعریف سیاست** - پذیرش امنیت Pod فقط از
  [۳ سطح استاندارد](/docs/concepts/security/pod-security-standards/) پشتیبانی می‌کند.
  اگر به کنترل بیشتری بر محدودیت‌های خاص نیاز دارید، باید برای اعمال آن سیاست‌ها از یک
  [وب‌هوک پذیرش اعتبارسنج](/docs/reference/access-authn-authz/extensible-admission-controllers/)
  استفاده کنید.
- **جزئی‌سازی سیاست در سطحی پایین‌تر از فضای نام** - PodSecurityPolicy به شما امکان می‌دهد حتی در یک
  فضای نام واحد، سیاست‌های متفاوتی را به حساب‌های سرویس (Service Account) یا کاربران مختلف متصل کنید.
  این رویکرد مشکلات بسیاری دارد و توصیه نمی‌شود، اما اگر به هر حال به این قابلیت نیاز دارید، باید به‌جای آن
  از یک وب‌هوک شخص ثالث استفاده کنید. استثنای این مورد زمانی است که فقط لازم باشد کاربران یا
  [RuntimeClassهای](/docs/concepts/containers/runtime-class/) مشخصی را به‌طور کامل معاف کنید؛ در این
  حالت، پذیرش امنیت Pod
  [پیکربندی ایستایی برای معافیت‌ها](/docs/concepts/security/pod-security-admission/#exemptions)
  در اختیار می‌گذارد.

حتی اگر پذیرش امنیت Pod همهٔ نیازهای شما را برآورده نکند، به‌گونه‌ای طراحی شده است که _مکمل_ دیگر
سازوکارهای اعمال سیاست باشد و می‌تواند در کنار دیگر وب‌هوک‌های پذیرش، به‌عنوان یک پشتیبان مفید عمل کند.


## ۱. بازبینی مجوزهای فضای نام {#review-namespace-permissions}

پذیرش امنیت Pod با [برچسب‌های روی
فضاهای نام](/docs/concepts/security/pod-security-admission/#pod-security-admission-labels-for-namespaces)
کنترل می‌شود. این یعنی هر کسی که بتواند یک فضای نام را به‌روزرسانی کند (یا آن را patch یا ایجاد کند)،
می‌تواند سطح امنیت Pod آن فضای نام را نیز تغییر دهد و از این راه یک سیاست سخت‌گیرانه‌تر را دور بزند. پیش از
ادامه، مطمئن شوید که فقط کاربران مورد اعتماد و دارای امتیاز ویژه این مجوزهای فضای نام را دارند. اعطای این
مجوزهای قدرتمند به کاربرانی که نباید مجوزهای ارتقایافته داشته باشند توصیه نمی‌شود، اما اگر ناچار به این کار
هستید، باید از یک
[وب‌هوک پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/)
برای اعمال محدودیت‌های بیشتر بر تنظیم برچسب‌های امنیت Pod روی آبجکت‌های Namespace استفاده کنید.

## ۲. ساده‌سازی و استانداردسازی PodSecurityPolicyها {#simplify-psps}

در این بخش، PodSecurityPolicyهای تغییردهنده را کاهش می‌دهید و گزینه‌هایی را که خارج از دامنهٔ
استانداردهای امنیت Pod هستند حذف می‌کنید. تغییرات توصیه‌شده در اینجا را باید روی یک نسخهٔ آفلاین از
PodSecurityPolicy اصلیِ در حال تغییر اعمال کنید. نام PSP کپی‌شده باید با نام اصلی متفاوت باشد و از نظر
الفبایی پیش از آن قرار بگیرد (برای مثال، یک `0` به ابتدای آن اضافه کنید). هنوز سیاست‌های جدید را در
کوبرنتیز ایجاد نکنید؛ این کار در بخش [انتشار سیاست‌های
به‌روزشده](#psp-update-rollout) در ادامه پوشش داده می‌شود.

### ۲.الف. حذف فیلدهای صرفاً تغییردهنده {#eliminate-mutating-fields}

اگر یک PodSecurityPolicy پادها را تغییر دهد، ممکن است هنگامی که سرانجام PodSecurityPolicy را خاموش
می‌کنید، با پادهایی روبه‌رو شوید که الزامات سطح امنیت Pod را برآورده نمی‌کنند. برای جلوگیری از این وضعیت،
باید پیش از جابه‌جایی، همهٔ تغییرات PSP را حذف کنید. متأسفانه PSP فیلدهای تغییردهنده و اعتبارسنج را به‌طور
روشن از هم جدا نمی‌کند، بنابراین این مهاجرت ساده و سرراست نیست.

می‌توانید کار را با حذف فیلدهایی آغاز کنید که صرفاً تغییردهنده هستند و هیچ تأثیری بر سیاست اعتبارسنجی
ندارند. این فیلدها (که در مرجع
[نگاشت PodSecurityPolicyها به استانداردهای امنیت Pod](/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
نیز فهرست شده‌اند) عبارت‌اند از:

- `.spec.defaultAllowPrivilegeEscalation`
- `.spec.runtimeClass.defaultRuntimeClassName`
- `.metadata.annotations['seccomp.security.alpha.kubernetes.io/defaultProfileName']`
- `.metadata.annotations['apparmor.security.beta.kubernetes.io/defaultProfileName']`
- `.spec.defaultAddCapabilities` - این فیلد اگرچه از نظر فنی هم تغییردهنده و هم اعتبارسنج است، باید در
  `.spec.allowedCapabilities` ادغام شود؛ فیلدی که همان اعتبارسنجی را بدون تغییر انجام می‌دهد.

{{< caution >}}
حذف این فیلدها ممکن است باعث شود بارهای کاری فاقد پیکربندی لازم شوند و مشکلاتی پدید آید. برای راهنمایی
دربارهٔ انتشار ایمن این تغییرات، بخش [انتشار سیاست‌های به‌روزشده](#psp-update-rollout) را در ادامه ببینید.
{{< /caution >}}

### ۲.ب. حذف گزینه‌هایی که استانداردهای امنیت Pod آن‌ها را پوشش نمی‌دهند {#eliminate-non-standard-options}

چندین فیلد در PodSecurityPolicy وجود دارد که استانداردهای امنیت Pod آن‌ها را پوشش نمی‌دهند. اگر ناچار
به اعمال این گزینه‌ها هستید، باید پذیرش امنیت Pod را با یک
[وب‌هوک پذیرش](/docs/reference/access-authn-authz/extensible-admission-controllers/)
تکمیل کنید که خارج از دامنهٔ این راهنماست.

ابتدا می‌توانید فیلدهای صرفاً اعتبارسنجی را که استانداردهای امنیت Pod پوشش نمی‌دهند حذف کنید.
این فیلدها (که در مرجع
[نگاشت PodSecurityPolicyها به استانداردهای امنیت Pod](/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
با عبارت «no opinion» فهرست شده‌اند) عبارت‌اند از:

- `.spec.allowedHostPaths`
- `.spec.allowedFlexVolumes`
- `.spec.allowedCSIDrivers`
- `.spec.forbiddenSysctls`
- `.spec.runtimeClass`

همچنین می‌توانید فیلدهای زیر را که به کنترل‌های گروه POSIX / UNIX مربوط‌اند حذف کنید.

{{< caution >}}
اگر هر یک از این فیلدها از راهبرد `MustRunAs` استفاده کند، ممکن است تغییردهنده باشد! حذف آن‌ها ممکن است
باعث شود بارهای کاری گروه‌های لازم را تنظیم نکنند و مشکلاتی پدید آید. برای راهنمایی دربارهٔ انتشار ایمن
این تغییرات، بخش [انتشار سیاست‌های به‌روزشده](#psp-update-rollout) را در ادامه ببینید.
{{< /caution >}}

- `.spec.runAsGroup`
- `.spec.supplementalGroups`
- `.spec.fsGroup`

فیلدهای تغییردهندهٔ باقی‌مانده برای پشتیبانی درست از استانداردهای امنیت Pod لازم‌اند و بعداً باید هر یک
به‌صورت موردی بررسی شوند:

- `.spec.requiredDropCapabilities` - برای حذف `ALL` در پروفایل Restricted لازم است.
- `.spec.seLinux` - (فقط با قاعدهٔ `MustRunAs` تغییردهنده است) برای اعمال الزامات SELinux در
  پروفایل‌های Baseline و Restricted لازم است.
- `.spec.runAsUser` - (با قاعدهٔ `RunAsAny` تغییردهنده نیست) برای اعمال `RunAsNonRoot` در
  پروفایل Restricted لازم است.
- `.spec.allowPrivilegeEscalation` - (فقط در صورتی که روی `false` تنظیم شود تغییردهنده است) برای
  پروفایل Restricted لازم است.

### ۲.ج. انتشار PSPهای به‌روزشده {#psp-update-rollout}

در گام بعد، می‌توانید سیاست‌های به‌روزشده را در کلاستر خود منتشر کنید. باید با احتیاط پیش بروید، زیرا
حذف گزینه‌های تغییردهنده ممکن است باعث شود بارهای کاری فاقد پیکربندی لازم شوند.

برای هر PodSecurityPolicy به‌روزشده:

1. پادهایی را که تحت PSP اصلی اجرا می‌شوند شناسایی کنید. این کار با استفاده از حاشیه‌نویسی (annotation)
   `kubernetes.io/psp` امکان‌پذیر است. برای مثال، با kubectl:
   ```sh
   PSP_NAME="original" # Set the name of the PSP you're checking for
   kubectl get pods --all-namespaces -o jsonpath="{range .items[?(@.metadata.annotations.kubernetes\.io\/psp=='$PSP_NAME')]}{.metadata.namespace} {.metadata.name}{'\n'}{end}"
   ```
2. این پادهای در حال اجرا را با مشخصات (spec) اصلی پاد مقایسه کنید تا معلوم شود که آیا PodSecurityPolicy
   پاد را تغییر داده است یا نه. برای پادهایی که یک [منبع بار کاری](/docs/concepts/workloads/controllers/)
   ایجاد کرده است، می‌توانید پاد را با PodTemplate موجود در منبع کنترل‌کننده مقایسه کنید. اگر تغییری
   شناسایی شد، باید Pod یا PodTemplate اصلی را با پیکربندی مطلوب به‌روزرسانی کنید.
   فیلدهایی که باید بازبینی شوند عبارت‌اند از:
   - `.metadata.annotations['container.apparmor.security.beta.kubernetes.io/*']` (به‌جای * نام هر کانتینر را قرار دهید)
   - `.spec.runtimeClassName`
   - `.spec.securityContext.fsGroup`
   - `.spec.securityContext.seccompProfile`
   - `.spec.securityContext.seLinuxOptions`
   - `.spec.securityContext.supplementalGroups`
   - در کانتینرها، زیر `.spec.containers[*]` و `.spec.initContainers[*]`:
       - `.securityContext.allowPrivilegeEscalation`
       - `.securityContext.capabilities.add`
       - `.securityContext.capabilities.drop`
       - `.securityContext.readOnlyRootFilesystem`
       - `.securityContext.runAsGroup`
       - `.securityContext.runAsNonRoot`
       - `.securityContext.runAsUser`
       - `.securityContext.seccompProfile`
       - `.securityContext.seLinuxOptions`
3. PodSecurityPolicyهای جدید را ایجاد کنید. اگر Role یا ClusterRoleای مجوز `use` را روی همهٔ PSPها
   اعطا کند، ممکن است به‌جای همتاهای تغییردهنده، PSPهای جدید استفاده شوند.
4. پیکربندی مجوزدهی خود را به‌روزرسانی کنید تا دسترسی به PSPهای جدید اعطا شود. در RBAC، این یعنی هر
   Role یا ClusterRoleای را که مجوز `use` را روی PSP اصلی اعطا می‌کند، طوری به‌روزرسانی کنید که این مجوز
   را برای PSP به‌روزشده نیز اعطا کند.
5. راستی‌آزمایی: پس از گذشت مدتی برای تثبیت، فرمان مرحلهٔ ۱ را دوباره اجرا کنید تا ببینید آیا هنوز پادی از
   PSPهای اصلی استفاده می‌کند یا نه. توجه کنید که پس از انتشار سیاست‌های جدید، پادها باید دوباره ایجاد
   شوند تا بتوان آن‌ها را به‌طور کامل راستی‌آزمایی کرد.
6. (اختیاری) پس از آنکه اطمینان یافتید PSPهای اصلی دیگر استفاده نمی‌شوند، می‌توانید آن‌ها را حذف کنید.

## ۳. به‌روزرسانی فضاهای نام {#update-namespaces}

مراحل زیر باید روی تک‌تک فضاهای نام کلاستر انجام شوند. فرمان‌هایی که در این مراحل به آن‌ها اشاره
می‌شود، از متغیر `$NAMESPACE` برای ارجاع به فضای نامِ در حال به‌روزرسانی استفاده می‌کنند.

### ۳.الف. شناسایی سطح امنیت Pod مناسب {#identify-appropriate-level}

کار را با مرور [استانداردهای امنیت Pod](/docs/concepts/security/pod-security-standards/) و
آشنایی با ۳ سطح مختلف آن آغاز کنید.

برای انتخاب سطح امنیت Pod برای فضای نام خود چند راه وجود دارد:

1. **بر اساس الزامات امنیتی فضای نام** - اگر با سطح دسترسی مورد انتظار برای فضای نام آشنا هستید،
   می‌توانید سطح مناسب را بر اساس همان الزامات انتخاب کنید؛ مشابه کاری که ممکن است در یک کلاستر
   جدید انجام دهید.
2. **بر اساس PodSecurityPolicyهای موجود** - با استفاده از مرجع
   [نگاشت PodSecurityPolicyها به استانداردهای امنیت Pod](/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
   می‌توانید هر PSP را به یکی از سطوح استاندارد امنیت Pod نگاشت کنید. اگر PSPهای شما بر پایهٔ
   استانداردهای امنیت Pod نیستند، ممکن است لازم باشد میان انتخاب سطحی که دست‌کم به‌اندازهٔ PSP
   سهل‌گیر است و سطحی که دست‌کم به‌اندازهٔ آن سخت‌گیر است تصمیم بگیرید. با فرمان زیر می‌توانید ببینید
   پادهای یک فضای نام مشخص از کدام PSPها استفاده می‌کنند:
   ```sh
   kubectl get pods -n $NAMESPACE -o jsonpath="{.items[*].metadata.annotations.kubernetes\.io\/psp}" | tr " " "\n" | sort -u
   ```
3. **بر اساس پادهای موجود** - با استفاده از راهبردهای بخش [راستی‌آزمایی سطح امنیت Pod](#verify-pss-level)
   می‌توانید هر دو سطح Baseline و Restricted را آزمایش کنید تا ببینید آیا برای بارهای کاری موجود به‌اندازهٔ
   کافی سهل‌گیر هستند یا نه، و سپس معتبرترین سطحی را که کمترین امتیاز را دارد انتخاب کنید.

{{< caution >}}
گزینه‌های ۲ و ۳ بالا بر پایهٔ پادهای _موجود_ هستند و ممکن است بارهای کاری‌ای را که در حال حاضر اجرا
نمی‌شوند، مانند CronJobها، بارهای کاری مقیاس‌پذیر تا صفر یا دیگر بارهای کاری‌ای که هنوز منتشر نشده‌اند،
از قلم بیندازند.
{{< /caution >}}

### ۳.ب. راستی‌آزمایی سطح امنیت Pod {#verify-pss-level}

پس از آنکه سطح امنیت Pod را برای فضای نام انتخاب کردید (یا اگر در حال آزمودن چند سطح هستید)، بهتر است
ابتدا آن را آزمایش کنید (اگر از سطح Privileged استفاده می‌کنید، می‌توانید از این مرحله بگذرید). امنیت Pod
چندین ابزار برای کمک به آزمایش و انتشار ایمن پروفایل‌ها در اختیار می‌گذارد.

نخست، می‌توانید سیاست را به‌صورت آزمایشی اجرا کنید. این کار پادهای در حال اجرا در فضای نام را در برابر
سیاست اعمال‌شده ارزیابی می‌کند، بی‌آنکه سیاست جدید واقعاً اعمال شود:
```sh
# $LEVEL is the level to dry-run, either "baseline" or "restricted".
kubectl label --dry-run=server --overwrite ns $NAMESPACE pod-security.kubernetes.io/enforce=$LEVEL
```
این فرمان برای هر پاد _موجود_ که در سطح پیشنهادی معتبر نباشد، یک هشدار برمی‌گرداند.

گزینهٔ دوم، یعنی حالت ممیزی (audit)، برای شناسایی بارهای کاری‌ای که در حال حاضر اجرا نمی‌شوند مناسب‌تر
است. در حالت ممیزی (برخلاف حالت اعمال)، پادهایی که سطح سیاست را نقض می‌کنند ممنوع نمی‌شوند، بلکه در
لاگ‌های ممیزی ثبت می‌شوند تا بتوان پس از گذشت مدتی برای تثبیت، آن‌ها را بازبینی کرد. حالت هشدار نیز به
همین شکل کار می‌کند، اما هشدار را بی‌درنگ به کاربر برمی‌گرداند. با فرمان زیر می‌توانید سطح ممیزی را
روی یک فضای نام تنظیم کنید:
```sh
kubectl label --overwrite ns $NAMESPACE pod-security.kubernetes.io/audit=$LEVEL
```

اگر هر یک از این رویکردها به نقض‌های غیرمنتظره‌ای منجر شود، باید یا بارهای کاری ناقض را طوری
به‌روزرسانی کنید که الزامات سیاست را برآورده کنند، یا سطح امنیت Pod فضای نام را سهل‌گیرانه‌تر کنید.

### ۳.ج. اعمال سطح امنیت Pod {#enforce-pod-security-level}

هنگامی که مطمئن شدید سطح انتخاب‌شده را می‌توان به‌طور ایمن روی فضای نام اعمال کرد، می‌توانید فضای نام
را طوری به‌روزرسانی کنید که سطح مطلوب را اعمال کند:

```sh
kubectl label --overwrite ns $NAMESPACE pod-security.kubernetes.io/enforce=$LEVEL
```

### ۳.د. دور زدن PodSecurityPolicy {#bypass-psp}

در پایان، می‌توانید با متصل کردن
{{< example file="policy/privileged-psp.yaml" >}}PSP کاملاً دارای امتیاز ویژه{{< /example >}} به همهٔ
حساب‌های سرویس در فضای نام، PodSecurityPolicy را در سطح فضای نام عملاً دور بزنید.

```sh
# The following cluster-scoped commands are only needed once.
kubectl apply -f privileged-psp.yaml
kubectl create clusterrole privileged-psp --verb use --resource podsecuritypolicies.policy --resource-name privileged

# Per-namespace disable
kubectl create -n $NAMESPACE rolebinding disable-psp --clusterrole privileged-psp --group system:serviceaccounts:$NAMESPACE
```

از آنجا که PSP دارای امتیاز ویژه غیرتغییردهنده است و کنترل‌کنندهٔ پذیرش PSP همواره PSPهای
غیرتغییردهنده را ترجیح می‌دهد، این کار تضمین می‌کند که پادهای این فضای نام دیگر توسط PodSecurityPolicy
تغییر داده یا محدود نمی‌شوند.

مزیت غیرفعال کردن PodSecurityPolicy به این شکل و به‌صورت جداگانه برای هر فضای نام این است که اگر مشکلی
پیش بیاید، می‌توانید با حذف RoleBinding به‌آسانی تغییر را بازگردانید. فقط مطمئن شوید که
PodSecurityPolicyهای از پیش موجود همچنان سر جای خود باقی هستند!

```sh
# Undo PodSecurityPolicy disablement.
kubectl delete -n $NAMESPACE rolebinding disable-psp
```

## ۴. بازبینی فرایندهای ایجاد فضای نام {#review-namespace-creation-process}

اکنون که فضاهای نام موجود برای اعمال پذیرش امنیت Pod به‌روزرسانی شده‌اند، باید مطمئن شوید که فرایندها
و/یا سیاست‌های شما برای ایجاد فضاهای نام جدید نیز به‌روزرسانی شده‌اند تا یک پروفایل امنیت Pod مناسب روی
فضاهای نام جدید اعمال شود.

همچنین می‌توانید کنترل‌کنندهٔ پذیرش امنیت Pod را به‌صورت ایستا پیکربندی کنید تا برای فضاهای نام بدون
برچسب، سطح پیش‌فرضی برای حالت‌های enforce، audit و/یا warn تعیین کند. برای اطلاعات بیشتر،
[پیکربندی کنترل‌کنندهٔ پذیرش](/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller)
را ببینید.

## ۵. غیرفعال‌کردن PodSecurityPolicy {#disable-psp}

اکنون سرانجام آماده‌اید که PodSecurityPolicy را غیرفعال کنید. برای این کار باید پیکربندی پذیرش
(admission) سرور API را تغییر دهید:
[چگونه یک کنترل‌کنندهٔ پذیرش را غیرفعال کنم؟](/docs/reference/access-authn-authz/admission-controllers/#how-do-i-turn-off-an-admission-controller).

برای اطمینان از اینکه کنترل‌کنندهٔ پذیرش PodSecurityPolicy دیگر فعال نیست، می‌توانید با جعل هویت
کاربری که به هیچ PodSecurityPolicy دسترسی ندارد، به‌صورت دستی آزمایشی اجرا کنید (به
[نمونهٔ PodSecurityPolicy](/docs/concepts/security/pod-security-policy/#example) مراجعه کنید)
یا این موضوع را در لاگ‌های سرور API بررسی کنید. سرور API هنگام راه‌اندازی، خطوطی در لاگ می‌نویسد
که افزونه‌های بارگذاری‌شدهٔ کنترل‌کنندهٔ پذیرش را فهرست می‌کنند:

```
I0218 00:59:44.903329      13 plugins.go:158] Loaded 16 mutating admission controller(s) successfully in the following order: NamespaceLifecycle,LimitRanger,ServiceAccount,NodeRestriction,TaintNodesByCondition,Priority,DefaultTolerationSeconds,ExtendedResourceToleration,PersistentVolumeLabel,DefaultStorageClass,StorageObjectInUseProtection,RuntimeClass,DefaultIngressClass,MutatingAdmissionWebhook.
I0218 00:59:44.903350      13 plugins.go:161] Loaded 14 validating admission controller(s) successfully in the following order: LimitRanger,ServiceAccount,PodSecurity,Priority,PersistentVolumeClaimResize,RuntimeClass,CertificateApproval,CertificateSigning,CertificateSubjectRestriction,DenyServiceExternalIPs,ValidatingAdmissionWebhook,ResourceQuota.
```

باید `PodSecurity` را (در میان کنترل‌کننده‌های پذیرش اعتبارسنج) ببینید و هیچ‌یک از دو فهرست
نباید شامل `PodSecurityPolicy` باشد.

هنگامی که مطمئن شدید کنترل‌کنندهٔ پذیرش PSP غیرفعال شده است (و پس از گذشت زمان آزمایشی کافی برای
اطمینان از اینکه به بازگشت به وضعیت قبلی نیازی نخواهید داشت)، می‌توانید PodSecurityPolicyها و
همهٔ Roleها، ClusterRoleها، RoleBindingها و ClusterRoleBindingهای مرتبط با آن‌ها را حذف کنید
(فقط مطمئن شوید که این آبجکت‌ها مجوزهای نامرتبط دیگری اعطا نمی‌کنند).
