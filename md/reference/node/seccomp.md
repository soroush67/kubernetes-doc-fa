---
content_type: reference
title: کوبرنتیز و Seccomp
weight: 80
---

<!-- overview -->

حالت محاسبات امن (Seccomp، کوتاه‌شدهٔ secure computing mode) از نسخهٔ 2.6.12 به بعد یکی از قابلیت‌های هستهٔ لینوکس است. با این قابلیت می‌توان امتیازهای یک پردازه را در محیطی ایزوله محدود کرد و فراخوانی‌هایی را که آن پردازه می‌تواند از فضای کاربر به هسته انجام دهد، کاهش داد. کوبرنتیز این امکان را به شما می‌دهد که پروفایل‌های seccomp بارگذاری‌شده روی یک {{< glossary_tooltip text="نود" term_id="node" >}} را به‌طور خودکار روی Podها و کانتینرهای خود اعمال کنید.

## فیلدهای Seccomp

{{< feature-state for_k8s_version="v1.19" state="stable" >}}

برای تعیین پروفایل seccomp یک {{< glossary_tooltip text="Pod" term_id="pod" >}} چهار راه وجود دارد:

- برای کل Pod با استفاده از [`spec.securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context)
- برای یک کانتینر با استفاده از [`spec.containers[*].securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1)
- برای یک کانتینر init (قابل راه‌اندازی مجدد / sidecar) با استفاده از [`spec.initContainers[*].securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1)
- برای یک [کانتینر موقت](/docs/concepts/workloads/pods/ephemeral-containers) با استفاده از [`spec.ephemeralContainers[*].securityContext.seccompProfile`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-2)

{{% code_sample file="pods/security/seccomp/fields.yaml" %}}

در مثال بالا، Pod با مقدار `Unconfined` اجرا می‌شود، در حالی که برای `ephemeral-container` و `init-container` به‌طور مشخص مقدار `RuntimeDefault` تعریف شده است. اگر کانتینر موقت یا کانتینر init فیلد `securityContext.seccompProfile` را به‌صراحت تنظیم نکرده بود، این مقدار از Pod به ارث می‌رسید. همین قاعده دربارهٔ کانتینری که پروفایل `Localhost` با نام `my-profile.json` را اجرا می‌کند نیز صادق است.

به‌طور کلی، فیلدهای کانتینرها (از جمله کانتینرهای موقت) نسبت به مقدار تعیین‌شده در سطح Pod اولویت بالاتری دارند و کانتینرهایی که فیلد seccomp را تنظیم نکرده‌اند، پروفایل را از Pod به ارث می‌برند.

{{< note >}}
نمی‌توان پروفایل seccomp را روی Pod یا کانتینری اعمال کرد که با تنظیم `privileged: true` در `securityContext` کانتینر اجرا می‌شود. کانتینرهای دارای امتیاز ویژه همیشه با مقدار `Unconfined` اجرا می‌شوند.
{{< /note >}}

فیلد `seccompProfile.type` می‌تواند یکی از مقادیر زیر را داشته باشد:

`Unconfined`
: بار کاری بدون هیچ محدودیت seccomp اجرا می‌شود.

`RuntimeDefault`
: پروفایل پیش‌فرض seccomp که {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} تعریف کرده است، اعمال می‌شود. هدف پروفایل‌های پیش‌فرض این است که مجموعه‌ای قوی از تنظیمات امنیتی پیش‌فرض را فراهم کنند و در عین حال کارکرد بار کاری را حفظ کنند. این پروفایل‌ها ممکن است در محیط‌های اجرای مختلف کانتینر و نسخه‌های انتشار آن‌ها با یکدیگر متفاوت باشند؛ برای نمونه، می‌توان به تفاوت پروفایل‌های {{< glossary_tooltip text="CRI-O" term_id="cri-o" >}} و {{< glossary_tooltip text="containerd" term_id="containerd" >}} اشاره کرد.

`Localhost`
: پروفایل مشخص‌شده در `localhostProfile` اعمال می‌شود. این پروفایل باید روی دیسک نود در دسترس باشد (مسیر آن در لینوکس `/var/lib/kubelet/seccomp` است). {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}} هنگام ایجاد کانتینر، در دسترس بودن پروفایل seccomp را بررسی می‌کند. اگر پروفایل وجود نداشته باشد، ایجاد کانتینر با خطای `CreateContainerError` ناموفق می‌شود.

### پروفایل‌های `Localhost`

پروفایل‌های Seccomp فایل‌هایی با قالب JSON هستند که از طرح‌وارهٔ تعریف‌شده در [مشخصات محیط اجرای OCI](https://github.com/opencontainers/runtime-spec/blob/f329913/config-linux.md#seccomp) پیروی می‌کنند. هر پروفایل اساساً کنش‌هایی را بر پایهٔ فراخوانی‌های سیستمی منطبق تعریف می‌کند، اما امکان تعیین مقادیر مشخص برای آرگومان‌های فراخوانی‌های سیستمی را نیز فراهم می‌سازد. برای مثال:

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "defaultErrnoRet": 38,
  "syscalls": [
    {
      "names": [
        "adjtimex",
        "alarm",
        "bind",
        "waitid",
        "waitpid",
        "write",
        "writev"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

در پروفایل بالا، مقدار `defaultAction` برابر با `SCMP_ACT_ERRNO` تعریف شده است و برای فراخوانی‌هایی که با کنش‌های تعریف‌شده در `syscalls` منطبق نشوند، به‌عنوان کنش جایگزین به کار می‌رود. کد خطا نیز با فیلد `defaultErrnoRet` برابر با `38` تعیین شده است.

به‌طور کلی کنش‌های زیر امکان‌پذیر هستند:

`SCMP_ACT_ERRNO`
: کد خطای مشخص‌شده را برمی‌گرداند.

`SCMP_ACT_ALLOW`
: اجازهٔ اجرای فراخوانی سیستمی را می‌دهد.

`SCMP_ACT_KILL_PROCESS`
: پردازه را خاتمه می‌دهد.

`SCMP_ACT_KILL_THREAD` و `SCMP_ACT_KILL`
: فقط رشتهٔ اجرایی را خاتمه می‌دهد.

`SCMP_ACT_TRAP`
: سیگنال `SIGSYS` را ارسال می‌کند.

`SCMP_ACT_NOTIFY` و `SECCOMP_RET_USER_NOTIF`.
: به فضای کاربر اطلاع می‌دهد.

`SCMP_ACT_TRACE`
: با مقدار مشخص‌شده به پردازهٔ ردیاب اطلاع می‌دهد.

`SCMP_ACT_LOG`
: پس از ثبت کنش در syslog یا auditd، اجازهٔ اجرای فراخوانی سیستمی را می‌دهد.

برخی از کنش‌ها مانند `SCMP_ACT_NOTIFY` یا `SECCOMP_RET_USER_NOTIF` بسته به محیط اجرای کانتینر، محیط اجرای OCI یا نسخهٔ هستهٔ لینوکس مورد استفاده ممکن است پشتیبانی نشوند. محدودیت‌های دیگری نیز ممکن است وجود داشته باشد؛ برای مثال، نمی‌توان از `SCMP_ACT_NOTIFY` به‌عنوان `defaultAction` یا برای برخی فراخوانی‌های سیستمی مانند `write` استفاده کرد. همهٔ این محدودیت‌ها را یا محیط اجرای OCI ([runc](https://github.com/opencontainers/runc)، [crun](https://github.com/containers/crun)) تعریف می‌کند یا [libseccomp](https://github.com/seccomp/libseccomp).

آرایهٔ JSON با نام `syscalls` فهرستی از آبجکت‌ها را در بر دارد که با فیلد `names` به فراخوانی‌های سیستمی ارجاع می‌دهند. برای مثال، همان‌طور که در نمونهٔ بالا دیده می‌شود، با کنش `SCMP_ACT_ALLOW` می‌توان فهرست مجازی از فراخوانی‌های سیستمی ایجاد کرد. همچنین می‌توان فهرست دیگری با کنش `SCMP_ACT_ERRNO` اما با مقدار بازگشتی (`errnoRet`) متفاوت تعریف کرد.

افزون بر این، می‌توان آرگومان‌های (`args`) ارسال‌شده به برخی فراخوانی‌های سیستمی را نیز مشخص کرد. اطلاعات بیشتر دربارهٔ این کاربردهای پیشرفته را می‌توانید در [مشخصات محیط اجرای OCI](https://github.com/opencontainers/runtime-spec/blob/f329913/config-linux.md#seccomp) و [مستندات Seccomp در هستهٔ لینوکس](https://www.kernel.org/doc/Documentation/prctl/seccomp_filter.txt) بیابید.

## مطالعهٔ بیشتر

- [محدود کردن فراخوانی‌های سیستمی یک کانتینر با seccomp](/docs/tutorials/security/seccomp/)
- [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards/)
