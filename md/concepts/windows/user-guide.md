---
reviewers:
- jayunit100
- jsturtevant
- marosset
title: راهنمای اجرای کانتینرهای ویندوز در کوبرنتیز
content_type: tutorial
weight: 75
---

<!-- overview -->

این صفحه مراحلی را گام‌به‌گام شرح می‌دهد که با دنبال کردن آن‌ها می‌توانید کانتینرهای ویندوز را با کوبرنتیز اجرا کنید.
همچنین برخی از قابلیت‌های مختص ویندوز در کوبرنتیز را معرفی می‌کند.

ایجاد و استقرار سرویس‌ها و بارهای کاری در کوبرنتیز برای کانتینرهای لینوکس و ویندوز تقریباً به یک شکل انجام می‌شود.
[دستورهای kubectl](/docs/reference/kubectl/) برای تعامل با کلاستر نیز در هر دو یکسان هستند.
مثال‌های این صفحه برای این آمده‌اند که کار با کانتینرهای ویندوز را سریع‌تر آغاز کنید.


<!-- body -->

## اهداف

یک استقرار نمونه را پیکربندی کنید تا کانتینرهای ویندوز روی یک نود ویندوز اجرا شوند.

## {{% heading "prerequisites" %}}

باید از پیش به یک کلاستر کوبرنتیز دسترسی داشته باشید که یک نود کارگر (worker node) با سیستم‌عامل Windows Server دارد.


## شروع کار: استقرار یک بار کاری ویندوز

فایل YAML نمونهٔ زیر یک برنامهٔ ساده وب‌سرور را مستقر می‌کند که درون یک کانتینر ویندوز اجرا می‌شود.

یک مانیفست با نام `win-webserver.yaml` و محتوای زیر ایجاد کنید:

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
نگاشت پورت (port mapping) نیز پشتیبانی می‌شود، اما برای سادگی، این مثال پورت 80 کانتینر را مستقیماً در اختیار Service قرار می‌دهد.
{{< /note >}}

1. بررسی کنید که همهٔ نودها سالم باشند:

    ```bash
    kubectl get nodes
    ```

1. سرویس را مستقر کنید و به‌روزرسانی‌های پادها را دنبال کنید:

    ```bash
    kubectl apply -f win-webserver.yaml
    kubectl get pods -o wide -w
    ```

    اگر سرویس به‌درستی مستقر شده باشد، هر دو Pod در وضعیت Ready قرار می‌گیرند. برای خروج از دستور پایش، کلیدهای Ctrl+C را فشار دهید.

1. بررسی کنید که استقرار با موفقیت انجام شده باشد. برای این کار موارد زیر را وارسی کنید:

    * فهرست شدن چند پاد از روی نود control plane لینوکسی؛ برای این کار از `kubectl get pods` استفاده کنید.
    * ارتباط نود با پاد در سطح شبکه؛ از روی نود control plane لینوکسی، با `curl` به پورت 80 نشانی‌های IP پادهای خود درخواست بفرستید تا پاسخ وب‌سرور را بررسی کنید.
    * ارتباط پاد با پاد؛ با استفاده از `kubectl exec` بین پادها (و در صورت داشتن بیش از یک نود ویندوز، بین میزبان‌های مختلف) دستور ping را اجرا کنید.
    * ارتباط سرویس با پاد؛ از روی نود control plane لینوکسی و نیز از درون تک‌تک پادها، با `curl` به IP مجازی سرویس (که در خروجی `kubectl get services` دیده می‌شود) درخواست بفرستید.
    * کشف سرویس (service discovery)؛ با `curl` به نام سرویس همراه با [پسوند پیش‌فرض DNS](/docs/concepts/services-networking/dns-pod-service/#services) کوبرنتیز درخواست بفرستید.
    * اتصال ورودی؛ از روی نود control plane لینوکسی یا از ماشین‌های بیرون از کلاستر، با `curl` به NodePort درخواست بفرستید.
    * اتصال خروجی؛ با استفاده از `kubectl exec` از درون پاد، با `curl` به IPهای بیرونی درخواست بفرستید.

{{< note >}}
به دلیل محدودیت‌های فعلی پشتهٔ شبکهٔ ویندوز، میزبان‌های کانتینر ویندوز نمی‌توانند به IP سرویس‌هایی که روی خودشان زمان‌بندی شده‌اند دسترسی داشته باشند.
فقط پادهای ویندوز می‌توانند به IP سرویس‌ها دسترسی پیدا کنند.
{{< /note >}}

## مشاهده‌پذیری

### جمع‌آوری لاگ‌های بارهای کاری

لاگ‌ها یکی از اجزای مهم مشاهده‌پذیری (observability) هستند؛ با آن‌ها کاربران می‌توانند از جنبهٔ عملیاتی بارهای کاری آگاهی پیدا کنند و همچنین نقشی کلیدی در عیب‌یابی مشکلات دارند.
از آنجا که کانتینرهای ویندوز و بارهای کاری درون آن‌ها رفتاری متفاوت با کانتینرهای لینوکس دارند، جمع‌آوری لاگ‌ها برای کاربران دشوار بود و همین موضوع دید عملیاتی را محدود می‌کرد.
برای مثال، بارهای کاری ویندوز معمولاً طوری پیکربندی می‌شوند که لاگ‌ها را در ETW (Event Tracing for Windows) ثبت کنند یا رکوردها را به لاگ رویدادهای برنامه (application event log) بفرستند.
ابزار متن‌باز [LogMonitor](https://github.com/microsoft/windows-container-tools/tree/master/LogMonitor) که مایکروسافت آن را توسعه داده است، روش توصیه‌شده برای پایش منابع لاگ پیکربندی‌شده درون یک کانتینر ویندوز است.
این ابزار از پایش لاگ‌های رویداد، ارائه‌دهندگان ETW و لاگ‌های سفارشی برنامه پشتیبانی می‌کند و آن‌ها را به STDOUT هدایت می‌کند تا با دستور `kubectl logs <pod>` قابل مشاهده باشند.

دستورالعمل‌های صفحهٔ GitHub ابزار LogMonitor را دنبال کنید تا فایل‌های اجرایی و پیکربندی آن را در همهٔ کانتینرهای خود کپی کنید و نقاط ورود (entrypoint) لازم را اضافه کنید تا LogMonitor لاگ‌های شما را به STDOUT بفرستد.

## پیکربندی کاربر کانتینر

### استفاده از نام‌های کاربری قابل پیکربندی برای کانتینر

می‌توان کانتینرهای ویندوز را طوری پیکربندی کرد که نقاط ورود و فرایندهای خود را با نام‌های کاربری‌ای غیر از نام‌های پیش‌فرض ایمیج اجرا کنند.
برای آشنایی بیشتر با این قابلیت، [این صفحه](/docs/tasks/configure-pod-container/configure-runasusername/) را ببینید.

### مدیریت هویت بار کاری با حساب‌های سرویس مدیریت‌شدهٔ گروهی

می‌توان بارهای کاری کانتینرهای ویندوز را طوری پیکربندی کرد که از حساب‌های سرویس مدیریت‌شدهٔ گروهی (Group Managed Service Accounts یا GMSA) استفاده کنند.
این حساب‌ها نوع خاصی از حساب‌های Active Directory هستند که مدیریت خودکار گذرواژه، مدیریت ساده‌شدهٔ نام اصلی سرویس (SPN) و امکان واگذاری مدیریت به سایر مدیران در چندین سرور را فراهم می‌کنند.
کانتینرهایی که با GMSA پیکربندی شده‌اند، می‌توانند با هویتی که در GMSA تعریف شده است به منابع دامنهٔ Active Directory بیرونی دسترسی پیدا کنند.
برای آشنایی بیشتر با پیکربندی و استفاده از GMSA برای کانتینرهای ویندوز، [این صفحه](/docs/tasks/configure-pod-container/configure-gmsa/) را ببینید.

## Taintها و tolerationها

کاربران باید ترکیبی از {{<glossary_tooltip text="taint" term_id="taint" >}} و انتخابگرهای نود را به کار بگیرند تا بارهای کاری لینوکس و ویندوز روی نودهای مختص سیستم‌عامل خودشان زمان‌بندی شوند.
رویکرد توصیه‌شده در ادامه شرح داده شده است؛ یکی از اهداف اصلی این رویکرد آن است که سازگاری با بارهای کاری لینوکس موجود از بین نرود.

می‌توانید (و بهتر است) برای هر Pod فیلد `.spec.os.name` را تنظیم کنید تا مشخص شود کانتینرهای آن Pod برای کدام سیستم‌عامل طراحی شده‌اند. برای Podهایی که کانتینرهای لینوکس را اجرا می‌کنند، مقدار `.spec.os.name` را `linux` قرار دهید. برای Podهایی که کانتینرهای ویندوز را اجرا می‌کنند، مقدار `.spec.os.name` را `windows` قرار دهید.

زمان‌بند هنگام تخصیص Podها به نودها از مقدار `.spec.os.name` استفاده نمی‌کند. باید از سازوکارهای معمول کوبرنتیز برای [تخصیص پادها به نودها](/docs/concepts/scheduling-eviction/assign-pod-node/) بهره بگیرید تا مطمئن شوید control plane کلاستر شما پادها را روی نودهایی قرار می‌دهد که سیستم‌عامل مناسب را اجرا می‌کنند.

مقدار `.spec.os.name` هیچ تأثیری بر زمان‌بندی پادهای ویندوز ندارد؛ بنابراین برای اطمینان از اینکه پادهای ویندوز روی نودهای ویندوز مناسب قرار می‌گیرند، همچنان به taintها و tolerationها (یا انتخابگرهای نود) نیاز است.

### اطمینان از قرار گرفتن بارهای کاری مختص هر سیستم‌عامل روی میزبان کانتینر مناسب

کاربران می‌توانند با استفاده از taintها و tolerationها اطمینان پیدا کنند که کانتینرهای ویندوز روی میزبان مناسب زمان‌بندی می‌شوند.
همهٔ نودهایی که کوبرنتیز {{< skew currentVersion >}} را اجرا می‌کنند، برچسب‌های پیش‌فرض زیر را دارند:

* kubernetes.io/os = [windows|linux]
* kubernetes.io/arch = [amd64|arm64|...]

اگر در مشخصات یک Pod، فیلد `nodeSelector` مانند `"kubernetes.io/os": windows` تعیین نشده باشد، ممکن است آن Pod روی هر میزبانی، چه ویندوز و چه لینوکس، زمان‌بندی شود.
این وضعیت می‌تواند مشکل‌ساز باشد، زیرا کانتینر ویندوز فقط روی ویندوز و کانتینر لینوکس فقط روی لینوکس اجرا می‌شود.
بهترین شیوه در کوبرنتیز {{< skew currentVersion >}} استفاده از `nodeSelector` است.

با این حال، در بسیاری از موارد کاربران از پیش تعداد زیادی استقرار برای کانتینرهای لینوکس دارند و علاوه بر آن، با اکوسیستمی از پیکربندی‌های آماده، مانند چارت‌های Helm جامعه، و مواردی از تولید برنامه‌نویسی‌شدهٔ Pod، مانند اپراتورها، سروکار دارند.
در چنین شرایطی ممکن است برای تغییر پیکربندی و افزودن فیلدهای `nodeSelector` به همهٔ Podها و قالب‌های Pod تردید داشته باشید.
راه جایگزین، استفاده از taintهاست. از آنجا که kubelet می‌تواند هنگام ثبت نود، taintها را تنظیم کند، به‌سادگی می‌توان آن را طوری تغییر داد که فقط هنگام اجرا روی ویندوز، به‌طور خودکار یک taint اضافه کند.

برای مثال: `--register-with-taints='os=windows:NoSchedule'`

با افزودن یک taint به همهٔ نودهای ویندوز، هیچ چیزی روی آن‌ها زمان‌بندی نمی‌شود (از جمله Podهای لینوکسی موجود).
برای اینکه یک Pod ویندوزی روی یک نود ویندوز زمان‌بندی شود، هم به `nodeSelector` نیاز دارد و هم به toleration منطبق و مناسب برای انتخاب ویندوز.

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

### مدیریت چند نسخهٔ ویندوز در یک کلاستر

نسخهٔ Windows Server که هر پاد از آن استفاده می‌کند باید با نسخهٔ نود یکسان باشد. اگر می‌خواهید چند نسخهٔ Windows Server را در یک کلاستر به کار ببرید، باید برچسب‌های نود و فیلدهای `nodeSelector` بیشتری تنظیم کنید.

کوبرنتیز برای ساده‌تر شدن این کار، به‌طور خودکار برچسب [`node.kubernetes.io/windows-build`](/docs/reference/labels-annotations-taints/#nodekubernetesiowindows-build) را اضافه می‌کند.

این برچسب شمارهٔ نسخهٔ اصلی (major)، نسخهٔ فرعی (minor) و شمارهٔ ساخت (build) ویندوز را نشان می‌دهد که برای سازگاری باید با هم منطبق باشند.
مقادیر مربوط به هر نسخهٔ Windows Server در جدول زیر آمده است:

| نام محصول                            | نسخه                   |
|--------------------------------------|------------------------|
| Windows Server 2022                  | 10.0.20348             |
| Windows Server 2025                  | 10.0.26100             |

### ساده‌سازی با RuntimeClass

با استفاده از [RuntimeClass] می‌توان فرایند به‌کارگیری taintها و tolerationها را ساده‌تر کرد.
مدیر کلاستر می‌تواند یک آبجکت `RuntimeClass` ایجاد کند که این taintها و tolerationها را در خود جای می‌دهد.

1. این فایل را با نام `runtimeClasses.yml` ذخیره کنید. این فایل شامل `nodeSelector` مناسب برای سیستم‌عامل ویندوز، معماری و نسخهٔ آن است.

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

1. به‌عنوان مدیر کلاستر، دستور `kubectl create -f runtimeClasses.yml` را اجرا کنید.
1. در صورت نیاز، `runtimeClassName: windows-2019` را به مشخصات Podها اضافه کنید.

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
