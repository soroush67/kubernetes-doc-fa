---
title: ایجاد یک Pod از نوع HostProcess در ویندوز
content_type: task
weight: 50
min-kubernetes-server-version: 1.23
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.26" state="stable" >}}

با کانتینرهای HostProcess ویندوز می‌توانید بارهای کاری (workload) کانتینری‌شده را روی میزبان ویندوزی اجرا کنید. این کانتینرها مانند فرایندهای عادی عمل می‌کنند، اما در صورت داشتن مجوزهای کاربری مناسب، به فضای نام (namespace) شبکهٔ میزبان، ذخیره‌سازی و دستگاه‌های آن دسترسی دارند. از کانتینرهای HostProcess می‌توان برای استقرار افزونه‌های شبکه، پیکربندی‌های ذخیره‌سازی، افزونه‌های دستگاه، kube-proxy و سایر مؤلفه‌ها روی نودهای ویندوزی استفاده کرد، بدون آنکه به پراکسی‌های اختصاصی یا نصب مستقیم سرویس‌های میزبان نیاز باشد.

کارهای مدیریتی مانند نصب وصله‌های امنیتی، جمع‌آوری لاگ رویدادها و موارد دیگر را می‌توان بدون نیاز به ورود اپراتورهای کلاستر به تک‌تک نودهای ویندوزی انجام داد. کانتینرهای HostProcess می‌توانند با هر کاربری که روی میزبان موجود است یا در دامنهٔ ماشین میزبان قرار دارد اجرا شوند؛ به این ترتیب مدیران می‌توانند دسترسی به منابع را از طریق مجوزهای کاربری محدود کنند. اگرچه جداسازی سیستم فایل و فرایند پشتیبانی نمی‌شود، هنگام شروع کانتینر یک حجم (volume) جدید روی میزبان ایجاد می‌شود تا فضای کاری تمیز و یکپارچه‌ای در اختیار کانتینر قرار گیرد. کانتینرهای HostProcess را همچنین می‌توان بر پایهٔ ایمیج‌های پایهٔ موجود ویندوز ساخت. این کانتینرها همان [الزامات سازگاری](https://docs.microsoft.com/virtualization/windowscontainers/deploy-containers/version-compatibility) کانتینرهای Windows Server را به ارث نمی‌برند؛ یعنی لازم نیست نسخهٔ ایمیج‌های پایه با نسخهٔ میزبان یکسان باشد. با این حال، توصیه می‌شود از همان نسخهٔ ایمیج پایه‌ای استفاده کنید که بارهای کاری کانتینر Windows Server شما از آن استفاده می‌کنند تا ایمیج‌های بلااستفاده فضای نود را اشغال نکنند. کانتینرهای HostProcess از [اتصال حجم‌ها](#volume-mounts) درون حجم کانتینر نیز پشتیبانی می‌کنند.

### چه زمانی باید از کانتینر HostProcess ویندوز استفاده کنم؟

- زمانی که باید کارهایی انجام دهید که به فضای نام شبکهٔ میزبان نیاز دارند. کانتینرهای HostProcess به رابط‌های شبکه و نشانی‌های IP میزبان دسترسی دارند.
- زمانی که به منابعی روی میزبان، مانند سیستم فایل، لاگ رویدادها و غیره، نیاز دارید.
- برای نصب درایورهای دستگاه خاص یا سرویس‌های ویندوز.
- برای یکپارچه‌سازی کارهای مدیریتی و سیاست‌های امنیتی. این کار سطح مجوزهای مورد نیاز نودهای ویندوزی را کاهش می‌دهد.

## {{% heading "prerequisites" %}}

<!-- change this when graduating to stable -->

این راهنما مختص کوبرنتیز نسخهٔ v{{< skew currentVersion >}} است. اگر از کوبرنتیز v{{< skew currentVersion >}} استفاده نمی‌کنید، مستندات نسخهٔ کوبرنتیز خود را بررسی کنید.

در کوبرنتیز {{< skew currentVersion >}}، قابلیت کانتینر HostProcess به‌طور پیش‌فرض فعال است. kubelet با ارسال پرچم hostprocess از طریق CRI، مستقیماً با containerd ارتباط برقرار می‌کند. برای اجرای کانتینرهای HostProcess می‌توانید از آخرین نسخهٔ containerd (نسخهٔ 1.6 به بعد) استفاده کنید.
[نحوهٔ نصب containerd.](/docs/setup/production-environment/container-runtimes/#containerd)

## محدودیت‌ها

محدودیت‌های زیر مربوط به کوبرنتیز v{{< skew currentVersion >}} هستند:

- کانتینرهای HostProcess به
  {{< glossary_tooltip text="محیط اجرای کانتینر" term_id="container-runtime" >}}
  containerd نسخهٔ 1.6 یا بالاتر نیاز دارند و نسخهٔ 1.7 توصیه می‌شود.
- Podهای HostProcess فقط می‌توانند شامل کانتینرهای HostProcess باشند. این محدودیتی فعلی در سیستم‌عامل ویندوز است؛ کانتینرهای ویندوزی غیرممتاز نمی‌توانند یک vNIC را با فضای نام IP میزبان به اشتراک بگذارند.
- کانتینرهای HostProcess به‌صورت یک فرایند روی میزبان اجرا می‌شوند و جز محدودیت‌های منابعی که بر حساب کاربری HostProcess اعمال می‌شود، هیچ‌گونه جداسازی ندارند. جداسازی سیستم فایل و جداسازی Hyper-V هیچ‌کدام برای کانتینرهای HostProcess پشتیبانی نمی‌شوند.
- اتصال حجم‌ها پشتیبانی می‌شود و حجم‌ها زیر حجم کانتینر متصل می‌شوند. به
  [اتصال حجم‌ها](#volume-mounts) مراجعه کنید.
- به‌طور پیش‌فرض، مجموعهٔ محدودی از حساب‌های کاربری میزبان برای کانتینرهای HostProcess در دسترس است.
  به [انتخاب حساب کاربری](#choosing-a-user-account) مراجعه کنید.
- محدودیت‌های منابع (دیسک، حافظه، تعداد CPU) به همان شیوهٔ فرایندهای روی میزبان پشتیبانی می‌شوند.
- اتصال Named pipe و سوکت‌های دامنهٔ یونیکس هیچ‌کدام پشتیبانی **نمی‌شوند** و به‌جای آن باید از طریق مسیرشان روی میزبان به آن‌ها دسترسی پیدا کرد (مثلاً \\\\.\\pipe\\\*)

## الزامات پیکربندی Pod از نوع HostProcess

برای فعال‌سازی Pod از نوع HostProcess در ویندوز باید پیکربندی‌های درستی را در پیکربندی امنیتی Pod تنظیم کنید. از میان سیاست‌های تعریف‌شده در [استانداردهای امنیتی Pod](/docs/concepts/security/pod-security-standards)، سیاست‌های baseline و restricted اجازهٔ اجرای Podهای HostProcess را نمی‌دهند. بنابراین توصیه می‌شود Podهای HostProcess مطابق با پروفایل privileged اجرا شوند.

هنگام اجرا تحت سیاست privileged، پیکربندی‌های زیر باید تنظیم شوند تا ایجاد Pod از نوع HostProcess امکان‌پذیر شود:

<table>
  <caption style="display: none">مشخصات سیاست privileged</caption>
  <thead>
    <tr>
      <th>کنترل</th>
      <th>سیاست</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="white-space: nowrap"><a href="/docs/concepts/security/pod-security-standards"><tt>securityContext.windowsOptions.hostProcess</tt></a></td>
      <td>
        <p>Podهای ویندوزی امکان اجرای <a href="/docs/tasks/configure-pod-container/create-hostprocess-pod">
        کانتینرهای HostProcess</a> را فراهم می‌کنند که دسترسی ممتاز به نود ویندوزی را ممکن می‌سازند. </p>
        <p><strong>مقادیر مجاز</strong></p>
        <ul>
          <li><code>true</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/docs/concepts/security/pod-security-standards"><tt>hostNetwork</tt></a></td>
      <td>
        <p>Podهایی که شامل کانتینرهای HostProcess هستند باید از فضای نام شبکهٔ میزبان استفاده کنند.</p>
        <p><strong>مقادیر مجاز</strong></p>
        <ul>
          <li><code>true</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/docs/tasks/configure-pod-container/configure-runasusername/"><tt>securityContext.windowsOptions.runAsUserName</tt></a></td>
      <td>
        <p>مشخص کردن کاربری که کانتینر HostProcess باید با آن اجرا شود، در مشخصات Pod الزامی است.</p>
        <p><strong>مقادیر مجاز</strong></p>
        <ul>
          <li><code>NT AUTHORITY\SYSTEM</code></li>
          <li><code>NT AUTHORITY\Local service</code></li>
          <li><code>NT AUTHORITY\NetworkService</code></li>
          <li>نام گروه‌های کاربری محلی (توضیحات پایین را ببینید)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="white-space: nowrap"><a href="/docs/concepts/security/pod-security-standards"><tt>runAsNonRoot</tt></a></td>
      <td>
        <p>از آنجا که کانتینرهای HostProcess دسترسی ممتاز به میزبان دارند، فیلد <tt>runAsNonRoot</tt> را نمی‌توان روی true تنظیم کرد.</p>
        <p><strong>مقادیر مجاز</strong></p>
        <ul>
          <li>تعریف‌نشده/Nil</li>
          <li><code>false</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### نمونهٔ مانیفست (بخشی از آن) {#manifest-example}

```yaml
spec:
  securityContext:
    windowsOptions:
      hostProcess: true
      runAsUserName: "NT AUTHORITY\\Local service"
  hostNetwork: true
  containers:
  - name: test
    image: image1:latest
    command:
      - ping
      - -t
      - 127.0.0.1
  nodeSelector:
    "kubernetes.io/os": windows
```

## اتصال حجم‌ها

کانتینرهای HostProcess امکان اتصال حجم‌ها درون فضای حجم کانتینر را پشتیبانی می‌کنند. رفتار اتصال حجم‌ها بسته به نسخهٔ محیط اجرای containerd که روی نود استفاده می‌شود، متفاوت است.

### نسخهٔ 1.6 از containerd

برنامه‌هایی که درون کانتینر اجرا می‌شوند می‌توانند مستقیماً از طریق مسیرهای نسبی یا مطلق به حجم‌های متصل‌شده دسترسی داشته باشند. هنگام ایجاد کانتینر، متغیر محیطی `$CONTAINER_SANDBOX_MOUNT_POINT` تنظیم می‌شود و مسیر مطلق حجم کانتینر روی میزبان را در اختیار قرار می‌دهد. مسیرهای نسبی بر اساس پیکربندی `.spec.containers.volumeMounts.mountPath` تعیین می‌شوند.

برای مثال، برای دسترسی به توکن‌های حساب سرویس، ساختارهای مسیر زیر درون کانتینر پشتیبانی می‌شوند:

- `.\var\run\secrets\kubernetes.io\serviceaccount\`
- `$CONTAINER_SANDBOX_MOUNT_POINT\var\run\secrets\kubernetes.io\serviceaccount\`

### نسخهٔ 1.7 از containerd (و بالاتر)

برنامه‌هایی که درون کانتینر اجرا می‌شوند می‌توانند مستقیماً از طریق `mountPath` مشخص‌شده در volumeMount به حجم‌های متصل‌شده دسترسی داشته باشند (درست مانند کانتینرهای لینوکسی و کانتینرهای ویندوزی غیر HostProcess).

برای حفظ سازگاری با نسخه‌های قبلی، همچنین می‌توان با استفاده از همان مسیرهای نسبی پیکربندی‌شده در containerd نسخهٔ 1.6 به حجم‌ها دسترسی داشت.

برای مثال، برای دسترسی به توکن‌های حساب سرویس درون کانتینر می‌توانید از یکی از مسیرهای زیر استفاده کنید:

- `c:\var\run\secrets\kubernetes.io\serviceaccount`
- `/var/run/secrets/kubernetes.io/serviceaccount/`
- `$CONTAINER_SANDBOX_MOUNT_POINT\var\run\secrets\kubernetes.io\serviceaccount\`

## محدودیت‌های منابع

محدودیت‌های منابع (دیسک، حافظه، تعداد CPU) روی job اعمال می‌شوند و در سطح کل job معتبرند. برای مثال، با تنظیم محدودیت 10MB، حافظهٔ تخصیص‌یافته به هر آبجکت job از نوع HostProcess حداکثر 10MB خواهد بود. این رفتار مشابه سایر انواع کانتینرهای ویندوزی است. این محدودیت‌ها به همان شیوه‌ای مشخص می‌شوند که در حال حاضر برای هر ارکستراتور یا محیط اجرایی مورد استفاده مشخص می‌شوند. تنها تفاوت در نحوهٔ محاسبهٔ مصرف منبع دیسک برای ردیابی منابع است که ناشی از تفاوت در شیوهٔ راه‌اندازی اولیهٔ کانتینرهای HostProcess است.

## انتخاب حساب کاربری

### حساب‌های سیستمی

به‌طور پیش‌فرض، کانتینرهای HostProcess می‌توانند با یکی از سه حساب سرویس پشتیبانی‌شدهٔ ویندوز اجرا شوند:

- **[LocalSystem](https://docs.microsoft.com/windows/win32/services/localsystem-account)**
- **[LocalService](https://docs.microsoft.com/windows/win32/services/localservice-account)**
- **[NetworkService](https://docs.microsoft.com/windows/win32/services/networkservice-account)**

باید برای هر کانتینر HostProcess یک حساب سرویس مناسب ویندوز انتخاب کنید و هدفتان محدود کردن سطح مجوزها باشد تا از آسیب تصادفی (یا حتی مخرب) به میزبان جلوگیری شود. حساب سرویس LocalSystem در میان این سه، بالاترین سطح مجوز را دارد و فقط در صورت ضرورت مطلق باید از آن استفاده شود. در صورت امکان، از حساب سرویس LocalService استفاده کنید، زیرا کمترین سطح مجوز را در میان این سه گزینه دارد.

### حساب‌های محلی {#local-accounts}

در صورت پیکربندی، کانتینرهای HostProcess می‌توانند با حساب‌های کاربری محلی نیز اجرا شوند؛ با این کار اپراتورهای نود می‌توانند دسترسی دقیق و جزئی به بارهای کاری بدهند.

برای اجرای کانتینرهای HostProcess با یک کاربر محلی، ابتدا باید یک گروه کاربری محلی روی نود ایجاد شود و نام آن گروه در فیلد `runAsUserName` در استقرار مشخص شود. پیش از راه‌اندازی کانتینر HostProcess، یک حساب کاربری محلی **موقت** جدید ایجاد و به گروه کاربری مشخص‌شده افزوده می‌شود و کانتینر با این حساب اجرا می‌شود. این روش مزایای متعددی دارد، از جمله اینکه دیگر نیازی به مدیریت گذرواژه‌های حساب‌های کاربری محلی نیست. می‌توان از یک کانتینر HostProcess اولیه که با یک حساب سرویس اجرا می‌شود، برای آماده‌سازی گروه‌های کاربری برای کانتینرهای HostProcess بعدی استفاده کرد.

{{< note >}}
اجرای کانتینرهای HostProcess با حساب‌های کاربری محلی به containerd نسخهٔ 1.7 یا بالاتر نیاز دارد.
{{< /note >}}

مثال:

1. یک گروه کاربری محلی روی نود ایجاد کنید (این کار را می‌توان در یک کانتینر HostProcess دیگر انجام داد).

    ```cmd
    net localgroup hpc-localgroup /add
    ```

1. به گروه کاربری محلی، دسترسی به منابع مورد نظر روی نود را اعطا کنید.
   این کار را می‌توان با ابزارهایی مانند [icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls) انجام داد.

1. مقدار `runAsUserName` را برای Pod یا کانتینرهای جداگانه، برابر نام گروه کاربری محلی قرار دهید.

    ```yaml
    securityContext:
      windowsOptions:
        hostProcess: true
        runAsUserName: hpc-localgroup
    ```

1. Pod را زمان‌بندی کنید!

## ایمیج پایه برای کانتینرهای HostProcess

کانتینرهای HostProcess را می‌توان از هر یک از [ایمیج‌های پایهٔ کانتینر ویندوز](https://learn.microsoft.com/virtualization/windowscontainers/manage-containers/container-base-images) موجود ساخت.

علاوه بر این، یک ایمیج پایهٔ جدید مخصوص کانتینرهای HostProcess ایجاد شده است!
برای اطلاعات بیشتر، [پروژهٔ گیت‌هاب windows-host-process-containers-base-image](https://github.com/microsoft/windows-host-process-containers-base-image#overview) را ببینید.

## عیب‌یابی کانتینرهای HostProcess

- کانتینرهای HostProcess با خطای `failed to create user process token: failed to logon user: Access is denied.: unknown` شروع به کار نمی‌کنند.

  مطمئن شوید که containerd با حساب سرویس `LocalSystem` یا `LocalService` اجرا می‌شود. حساب‌های کاربری (حتی حساب‌های Administrator) مجوز ایجاد توکن ورود برای هیچ‌یک از [حساب‌های کاربری](#choosing-a-user-account) پشتیبانی‌شده را ندارند.
