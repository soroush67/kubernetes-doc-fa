---
reviewers:
- jayunit100
- jsturtevant
- marosset
title: راهنمای اجرای کانتینرهای ویندوزی در کوبرنتیز
content_type: tutorial
weight: 75
---

<!-- overview -->

این صفحه مروری گام‌به‌گام بر مراحلی ارائه می‌کند که می‌توانید برای اجرای
کانتینرهای ویندوزی با استفاده از کوبرنتیز دنبال کنید.
این صفحه همچنین برخی قابلیت‌های ویژه‌ی ویندوز در کوبرنتیز را برجسته می‌کند.

توجه به این نکته مهم است که ایجاد و استقرار سرویس‌ها و بارهای کاری در کوبرنتیز
برای کانتینرهای لینوکسی و ویندوزی تقریباً به یک شکل انجام می‌شود.
[دستورهای kubectl](/docs/reference/kubectl/) برای تعامل با کلاستر یکسان هستند.
مثال‌های این صفحه برای آغاز سریع تجربه‌ی شما با کانتینرهای ویندوزی ارائه شده‌اند.


<!-- body -->

## اهداف {#objectives}

یک استقرار (deployment) نمونه را برای اجرای کانتینرهای ویندوزی روی یک نود ویندوزی پیکربندی کنید.

## {{% heading "prerequisites" %}}

شما باید از قبل به یک کلاستر کوبرنتیز دسترسی داشته باشید که شامل یک
نود کارگر (worker) با سیستم‌عامل Windows Server باشد.


## شروع کار: استقرار یک بار کاری ویندوزی

فایل YAML نمونه‌ی زیر یک برنامه‌ی وب‌سرور ساده را که درون یک کانتینر ویندوزی اجرا می‌شود، مستقر می‌کند.

یک مانیفست با نام `win-webserver.yaml` و با محتوای زیر ایجاد کنید:

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: win-webserver
  labels:
    app: win-webserver
spec:
  ports:
    # the port that this service should serve on
    - port: 80
      targetPort: 80
  selector:
    app: win-webserver
  type: NodePort
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: win-webserver
  name: win-webserver
spec:
  replicas: 2
  selector:
    matchLabels:
      app: win-webserver
  template:
    metadata:
      labels:
        app: win-webserver
      name: win-webserver
    spec:
     containers:
      - name: windowswebserver
        image: mcr.microsoft.com/windows/servercore:ltsc2019
        command:
        - powershell.exe
        - -command
        - "<#code used from https://gist.github.com/19WAS85/5424431#> ; $$listener = New-Object System.Net.HttpListener ; $$listener.Prefixes.Add('http://*:80/') ; $$listener.Start() ; $$callerCounts = @{} ; Write-Host('Listening at http://*:80/') ; while ($$listener.IsListening) { ;$$context = $$listener.GetContext() ;$$requestUrl = $$context.Request.Url ;$$clientIP = $$context.Request.RemoteEndPoint.Address ;$$response = $$context.Response ;Write-Host '' ;Write-Host('> {0}' -f $$requestUrl) ;  ;$$count = 1 ;$$k=$$callerCounts.Get_Item($$clientIP) ;if ($$k -ne $$null) { $$count += $$k } ;$$callerCounts.Set_Item($$clientIP, $$count) ;$$ip=(Get-NetAdapter | Get-NetIpAddress); $$header='<html><body><H1>Windows Container Web Server</H1>' ;$$callerCountsString='' ;$$callerCounts.Keys | % { $$callerCountsString+='<p>IP {0} callerCount {1} ' -f $$ip[1].IPAddress,$$callerCounts.Item($$_) } ;$$footer='</body></html>' ;$$content='{0}{1}{2}' -f $$header,$$callerCountsString,$$footer ;Write-Output $$content ;$$buffer = [System.Text.Encoding]::UTF8.GetBytes($$content) ;$$response.ContentLength64 = $$buffer.Length ;$$response.OutputStream.Write($$buffer, 0, $$buffer.Length) ;$$response.Close() ;$$responseStatus = $$response.StatusCode ;Write-Host('< {0}' -f $$responseStatus)  } ; "
     nodeSelector:
      kubernetes.io/os: windows
```

{{< note >}}
نگاشت پورت (port mapping) نیز پشتیبانی می‌شود، اما برای سادگی، این مثال
پورت 80 کانتینر را مستقیماً از طریق Service در دسترس قرار می‌دهد.
{{< /note >}}

1. بررسی کنید که همه‌ی نودها سالم هستند:

    ```bash
    kubectl get nodes
    ```

1. سرویس را مستقر کنید و تغییرات Podها را زیر نظر بگیرید:

    ```bash
    kubectl apply -f win-webserver.yaml
    kubectl get pods -o wide -w
    ```

    هنگامی که سرویس به‌درستی مستقر شود، هر دو Pod در وضعیت Ready علامت‌گذاری می‌شوند. برای خروج از دستور watch، کلیدهای Ctrl+C را فشار دهید.

1. بررسی کنید که استقرار با موفقیت انجام شده است. برای راستی‌آزمایی:

    * برای مشاهده‌ی چند Pod فهرست‌شده از نود control plane لینوکسی، از `kubectl get pods` استفاده کنید
    * برای ارتباط نود به Pod در سراسر شبکه، از نود control plane لینوکسی روی پورت 80 نشانی IP Podهای خود `curl` بزنید
      تا پاسخ وب‌سرور را بررسی کنید
    * برای ارتباط Pod به Pod، با استفاده از `kubectl exec` بین Podها (و در صورتی که بیش از یک نود ویندوزی دارید، بین میزبان‌ها) ping بزنید
    * برای ارتباط سرویس به Pod، از نود control plane لینوکسی و از درون Podهای منفرد روی IP مجازی سرویس
      (که در خروجی `kubectl get services` دیده می‌شود) `curl` بزنید
    * برای کشف سرویس (service discovery)، با استفاده از [پسوند DNS پیش‌فرض](/docs/concepts/services-networking/dns-pod-service/#services) کوبرنتیز روی نام سرویس `curl` بزنید
    * برای اتصال ورودی، از نود control plane لینوکسی یا از ماشین‌های خارج از کلاستر روی NodePort `curl` بزنید
    * برای اتصال خروجی، با استفاده از `kubectl exec` از درون Pod روی IPهای خارجی `curl` بزنید

{{< note >}}
به دلیل محدودیت‌های فعلی پلتفرم در پشته‌ی شبکه‌ی ویندوز، میزبان‌های کانتینر ویندوزی نمی‌توانند به IP سرویس‌هایی که روی خودشان زمان‌بندی شده‌اند دسترسی پیدا کنند.
فقط Podهای ویندوزی می‌توانند به IP سرویس‌ها دسترسی داشته باشند.
{{< /note >}}

## قابلیت مشاهده‌پذیری (Observability) {#observability}

### جمع‌آوری لاگ‌ها از بارهای کاری

لاگ‌ها عنصری مهم در مشاهده‌پذیری هستند؛ آن‌ها به کاربران امکان می‌دهند
دیدی نسبت به جنبه‌ی عملیاتی بارهای کاری به دست آورند و از اجزای کلیدی عیب‌یابی مشکلات به شمار می‌روند.
از آنجا که کانتینرهای ویندوزی و بارهای کاری درون آن‌ها رفتاری متفاوت از کانتینرهای لینوکسی دارند،
کاربران در جمع‌آوری لاگ‌ها با دشواری روبه‌رو بودند و این موضوع دید عملیاتی را محدود می‌کرد.
برای نمونه، بارهای کاری ویندوزی معمولاً به گونه‌ای پیکربندی می‌شوند که در ETW (Event Tracing for Windows) لاگ بنویسند
یا ورودی‌ها را به لاگ رویداد برنامه (application event log) ارسال کنند.
[LogMonitor](https://github.com/microsoft/windows-container-tools/tree/master/LogMonitor)، یک ابزار متن‌باز از مایکروسافت،
روش توصیه‌شده برای پایش منابع لاگ پیکربندی‌شده درون یک کانتینر ویندوزی است.
LogMonitor از پایش لاگ‌های رویداد، ارائه‌دهندگان ETW و لاگ‌های سفارشی برنامه پشتیبانی می‌کند
و آن‌ها را به STDOUT هدایت می‌کند تا با `kubectl logs <pod>` قابل مصرف باشند.

دستورالعمل‌های موجود در صفحه‌ی GitHub مربوط به LogMonitor را دنبال کنید تا فایل‌های اجرایی و پیکربندی آن
را در همه‌ی کانتینرهای خود کپی کنید و entrypointهای لازم را اضافه کنید تا LogMonitor لاگ‌های شما را به STDOUT ارسال کند.

## پیکربندی کاربر کانتینر {#configuring-container-user}

### استفاده از نام‌های کاربری قابل پیکربندی کانتینر

کانتینرهای ویندوزی را می‌توان طوری پیکربندی کرد که entrypointها و فرایندهای خود را
با نام‌های کاربری متفاوت از پیش‌فرض ایمیج اجرا کنند.
برای اطلاعات بیشتر [اینجا](/docs/tasks/configure-pod-container/configure-runasusername/) را ببینید.

### مدیریت هویت بار کاری با Group Managed Service Accounts

بارهای کاری کانتینرهای ویندوزی را می‌توان برای استفاده از Group Managed Service Accounts (GMSA) پیکربندی کرد.
Group Managed Service Accountها نوع خاصی از حساب‌های Active Directory هستند که مدیریت خودکار گذرواژه،
مدیریت ساده‌شده‌ی service principal name (SPN) و امکان واگذاری مدیریت به سایر مدیران را در چندین سرور فراهم می‌کنند.
کانتینرهای پیکربندی‌شده با GMSA می‌توانند ضمن حمل هویت پیکربندی‌شده با GMSA، به منابع دامنه‌ی خارجی Active Directory دسترسی پیدا کنند.
برای اطلاعات بیشتر درباره‌ی پیکربندی و استفاده از GMSA برای کانتینرهای ویندوزی [اینجا](/docs/tasks/configure-pod-container/configure-gmsa/) را ببینید.

## Taintها و Tolerationها {#taints-and-tolerations}

کاربران برای زمان‌بندی بارهای کاری لینوکسی و ویندوزی روی نودهای مخصوص هر سیستم‌عامل، باید از ترکیبی از {{<glossary_tooltip text="taint" term_id="taint" >}}
و انتخابگرهای نود (node selector) استفاده کنند.
رویکرد توصیه‌شده در ادامه تشریح شده است
و یکی از اهداف اصلی آن این است که این رویکرد نباید سازگاری بارهای کاری لینوکسی موجود را از بین ببرد.

شما می‌توانید (و باید) برای هر Pod مقدار `.spec.os.name` را تنظیم کنید تا سیستم‌عاملی را که
کانتینرهای آن Pod برای آن طراحی شده‌اند مشخص کنید. برای Podهایی که کانتینرهای لینوکسی اجرا می‌کنند،
`.spec.os.name` را برابر `linux` قرار دهید. برای Podهایی که کانتینرهای ویندوزی اجرا می‌کنند، `.spec.os.name`
را برابر `windows` قرار دهید.

زمان‌بند هنگام تخصیص Podها به نودها از مقدار `.spec.os.name` استفاده نمی‌کند. شما باید
از سازوکارهای معمول کوبرنتیز برای
[تخصیص Podها به نودها](/docs/concepts/scheduling-eviction/assign-pod-node/)
استفاده کنید تا اطمینان یابید control plane کلاستر شما Podها را روی نودهایی قرار می‌دهد که
سیستم‌عامل مناسب را اجرا می‌کنند.

مقدار `.spec.os.name` بر زمان‌بندی Podهای ویندوزی تأثیری ندارد،
بنابراین taintها و tolerationها (یا انتخابگرهای نود) همچنان برای اطمینان از
قرار گرفتن Podهای ویندوزی روی نودهای ویندوزی مناسب لازم هستند.

### اطمینان از قرار گرفتن بارهای کاری مخصوص هر سیستم‌عامل روی میزبان کانتینر مناسب

کاربران می‌توانند با استفاده از taintها و tolerationها اطمینان حاصل کنند که کانتینرهای ویندوزی روی میزبان مناسب زمان‌بندی می‌شوند.
همه‌ی نودهایی که کوبرنتیز {{< skew currentVersion >}} را اجرا می‌کنند، برچسب‌های پیش‌فرض زیر را دارند:

* kubernetes.io/os = [windows|linux]
* kubernetes.io/arch = [amd64|arm64|...]

اگر مشخصات یک Pod، `nodeSelector` ای مانند `"kubernetes.io/os": windows` را تعیین نکرده باشد،
ممکن است Pod روی هر میزبانی، چه ویندوزی و چه لینوکسی، زمان‌بندی شود.
این موضوع می‌تواند مشکل‌ساز باشد، زیرا یک کانتینر ویندوزی فقط روی ویندوز و یک کانتینر لینوکسی فقط روی لینوکس اجرا می‌شود.
بهترین روش برای کوبرنتیز {{< skew currentVersion >}} استفاده از `nodeSelector` است.

با این حال، در موارد بسیاری کاربران تعداد زیادی استقرار از پیش موجود برای کانتینرهای لینوکسی دارند،
و همچنین اکوسیستمی از پیکربندی‌های آماده مانند Helm chartهای جامعه‌ی کاربری، و مواردی از تولید برنامه‌نویسی‌شده‌ی Pod مانند operatorها.
در چنین شرایطی ممکن است تمایلی به اعمال تغییر پیکربندی برای افزودن فیلدهای `nodeSelector` به همه‌ی Podها و قالب‌های Pod نداشته باشید.
گزینه‌ی جایگزین استفاده از taintهاست. از آنجا که kubelet می‌تواند هنگام ثبت (registration) taint تنظیم کند،
می‌توان آن را به‌سادگی تغییر داد تا فقط هنگام اجرا روی ویندوز، به‌طور خودکار یک taint اضافه کند.

برای مثال: `--register-with-taints='os=windows:NoSchedule'`

با افزودن یک taint به همه‌ی نودهای ویندوزی، هیچ چیزی روی آن‌ها زمان‌بندی نخواهد شد (از جمله Podهای لینوکسی موجود).
برای اینکه یک Pod ویندوزی روی یک نود ویندوزی زمان‌بندی شود،
هم به `nodeSelector` و هم به toleration مطابق مناسب برای انتخاب ویندوز نیاز دارد.

```yaml
nodeSelector:
    kubernetes.io/os: windows
    node.kubernetes.io/windows-build: '10.0.20348'
tolerations:
    - key: "os"
      operator: "Equal"
      value: "windows"
      effect: "NoSchedule"
```

### مدیریت چند نسخه‌ی ویندوز در یک کلاستر {#handling-multiple-windows-versions-in-the-same-cluster}

نسخه‌ی Windows Server که هر Pod استفاده می‌کند باید با نسخه‌ی نود مطابقت داشته باشد. اگر می‌خواهید از چند نسخه‌ی
Windows Server در یک کلاستر استفاده کنید، باید برچسب‌های نود و فیلدهای `nodeSelector` اضافی تنظیم کنید.

کوبرنتیز برای ساده‌سازی این کار به‌طور خودکار برچسبی با نام
[`node.kubernetes.io/windows-build`](/docs/reference/labels-annotations-taints/#nodekubernetesiowindows-build)
اضافه می‌کند.

این برچسب شماره‌ی major، minor و build ویندوز را که برای سازگاری باید مطابقت داشته باشند، نشان می‌دهد.
مقادیر مورد استفاده برای هر نسخه‌ی Windows Server در ادامه آمده است:

| نام محصول                            | نسخه                   |
|--------------------------------------|------------------------|
| Windows Server 2022                  | 10.0.20348             |
| Windows Server 2025                  | 10.0.26100             |

### ساده‌سازی با RuntimeClass

از [RuntimeClass] می‌توان برای ساده‌سازی فرایند استفاده از taintها و tolerationها بهره برد.
مدیر کلاستر می‌تواند یک آبجکت `RuntimeClass` ایجاد کند که برای کپسوله‌سازی این taintها و tolerationها به کار می‌رود.

1. این فایل را در `runtimeClasses.yml` ذخیره کنید. این فایل شامل `nodeSelector` مناسب
   برای سیستم‌عامل ویندوز، معماری و نسخه است.

   ```yaml
   ---
   apiVersion: node.k8s.io/v1
   kind: RuntimeClass
   metadata:
     name: windows-2019
   handler: example-container-runtime-handler
   scheduling:
     nodeSelector:
       kubernetes.io/os: 'windows'
       kubernetes.io/arch: 'amd64'
       node.kubernetes.io/windows-build: '10.0.20348'
     tolerations:
     - effect: NoSchedule
       key: os
       operator: Equal
       value: "windows"
   ```

1. دستور `kubectl create -f runtimeClasses.yml` را با دسترسی مدیر کلاستر اجرا کنید
1. مقدار `runtimeClassName: windows-2019` را به‌طور مناسب به مشخصات Podها اضافه کنید

   برای مثال:

   ```yaml
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: iis-2019
     labels:
       app: iis-2019
   spec:
     replicas: 1
     template:
       metadata:
         name: iis-2019
         labels:
           app: iis-2019
       spec:
         runtimeClassName: windows-2019
         containers:
         - name: iis
           image: mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
           resources:
             limits:
               cpu: 1
               memory: 800Mi
             requests:
               cpu: 100m
               memory: 300Mi
           ports:
             - containerPort: 80
     selector:
       matchLabels:
         app: iis-2019
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: iis
   spec:
     type: LoadBalancer
     ports:
     - protocol: TCP
       port: 80
     selector:
       app: iis-2019
   ```

[RuntimeClass]: /docs/concepts/containers/runtime-class/
