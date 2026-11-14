---
title: پیکربندی GMSA برای Podها و کانتینرهای ویندوزی
content_type: task
weight: 30
---

<!-- overview -->

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

این صفحه نشان می‌دهد که چگونه می‌توان
[حساب‌های سرویس مدیریت‌شدهٔ گروهی](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview) (Group Managed Service Accounts یا GMSA)
را برای Podها و کانتینرهایی که روی نودهای ویندوزی اجرا می‌شوند پیکربندی کرد. حساب‌های سرویس مدیریت‌شدهٔ گروهی
نوع خاصی از حساب‌های Active Directory هستند که مدیریت خودکار گذرواژه،
مدیریت ساده‌شدهٔ نام اصلی سرویس (service principal name یا SPN) و امکان واگذاری مدیریت
به سایر مدیران در چندین سرور را فراهم می‌کنند.

در کوبرنتیز، مشخصات اعتبارنامهٔ GMSA (GMSA credential spec) در سطح کل کلاستر و
به‌صورت منابع سفارشی (Custom Resources) پیکربندی می‌شوند. می‌توان Podهای ویندوزی و نیز تک‌تک کانتینرهای درون یک Pod را
طوری پیکربندی کرد که هنگام تعامل با سایر سرویس‌های ویندوزی، برای کارکردهای مبتنی بر دامنه (مانند احراز هویت Kerberos)
از یک GMSA استفاده کنند.

## {{% heading "prerequisites" %}}

باید یک کلاستر کوبرنتیز داشته باشید و ابزار خط فرمان `kubectl` نیز باید
برای ارتباط با کلاستر شما پیکربندی شده باشد. انتظار می‌رود کلاستر نودهای کارگر ویندوزی داشته باشد.
این بخش مجموعه‌ای از گام‌های اولیه را شرح می‌دهد که برای هر کلاستر یک بار باید انجام شوند:

### نصب CRD مربوط به GMSACredentialSpec

برای تعریف نوع منبع سفارشی `GMSACredentialSpec`، باید یک
[CustomResourceDefinition](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) (CRD)
برای منابع مشخصات اعتبارنامهٔ GMSA روی کلاستر پیکربندی شود. فایل
[YAML](https://github.com/kubernetes-sigs/windows-gmsa/blob/master/admission-webhook/deploy/gmsa-crd.yml)
مربوط به CRD این قابلیت را دانلود کنید و آن را با نام gmsa-crd.yaml ذخیره کنید. سپس CRD را با دستور `kubectl apply -f gmsa-crd.yaml` نصب کنید.

### نصب وب‌هوک‌ها برای اعتبارسنجی کاربران GMSA

برای پر کردن و اعتبارسنجی ارجاع‌ها به مشخصات اعتبارنامهٔ GMSA در سطح Pod یا کانتینر،
باید دو وب‌هوک (webhook) روی کلاستر کوبرنتیز پیکربندی شود:

1. یک وب‌هوک تغییردهنده (mutating) که ارجاع‌ها به GMSAها را (که با نام در مشخصات Pod آمده‌اند)
   به مشخصات کامل اعتبارنامه در قالب JSON درون مشخصات Pod گسترش می‌دهد.

1. یک وب‌هوک اعتبارسنج (validating) که اطمینان حاصل می‌کند حساب سرویس Pod مجاز به استفاده از همهٔ GMSAهای ارجاع‌شده است.

نصب وب‌هوک‌های بالا و آبجکت‌های مرتبط با آن‌ها به گام‌های زیر نیاز دارد:

1. یک جفت کلید گواهی بسازید (که برای برقراری ارتباط کانتینر وب‌هوک با کلاستر استفاده می‌شود).

1. یک Secret حاوی گواهی بالا نصب کنید.

1. یک Deployment برای منطق اصلی وب‌هوک بسازید.

1. پیکربندی‌های وب‌هوک اعتبارسنج و تغییردهنده را با ارجاع به آن Deployment بسازید.

برای استقرار و پیکربندی وب‌هوک‌های GMSA و آبجکت‌های مرتبطِ ذکرشده در بالا
می‌توان از یک [اسکریپت](https://github.com/kubernetes-sigs/windows-gmsa/blob/master/admission-webhook/deploy/deploy-gmsa-webhook.sh)
استفاده کرد. این اسکریپت را می‌توان با گزینهٔ `--dry-run=server` اجرا کرد
تا تغییراتی را که روی کلاستر شما اعمال خواهد شد بازبینی کنید.

همچنین می‌توان از [قالب YAML](https://github.com/kubernetes-sigs/windows-gmsa/blob/master/admission-webhook/deploy/gmsa-webhook.yml.tpl)
که این اسکریپت به کار می‌برد، برای استقرار دستی وب‌هوک‌ها و آبجکت‌های مرتبط
(با جایگزینی مناسب پارامترها) استفاده کرد.

<!-- steps -->

## پیکربندی GMSAها و نودهای ویندوزی در Active Directory

پیش از آنکه بتوان Podها را در کوبرنتیز برای استفاده از GMSAها پیکربندی کرد، باید GMSAهای موردنظر
مطابق توضیحات
[مستندات GMSA ویندوز](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/getting-started-with-group-managed-service-accounts#BKMK_Step1)
در Active Directory ایجاد شوند.
نودهای کارگر ویندوزی (که بخشی از کلاستر کوبرنتیز هستند) نیز باید مطابق توضیحات
[مستندات GMSA ویندوز](https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/getting-started-with-group-managed-service-accounts#to-add-member-hosts-using-the-set-adserviceaccount-cmdlet)
در Active Directory طوری پیکربندی شوند که به اعتبارنامه‌های محرمانهٔ مرتبط با GMSA موردنظر دسترسی داشته باشند.

## ایجاد منابع مشخصات اعتبارنامهٔ GMSA

پس از نصب CRD مربوط به GMSACredentialSpec (به شرحی که پیش‌تر آمد)، می‌توان منابع سفارشی
حاوی مشخصات اعتبارنامهٔ GMSA را پیکربندی کرد. مشخصات اعتبارنامهٔ GMSA
هیچ دادهٔ محرمانه یا حساسی ندارد؛ بلکه اطلاعاتی است که محیط اجرای کانتینر
می‌تواند با آن، GMSA موردنظرِ یک کانتینر را برای ویندوز توصیف کند. مشخصات اعتبارنامهٔ GMSA
را می‌توان با یک
[اسکریپت PowerShell](https://github.com/kubernetes-sigs/windows-gmsa/tree/master/scripts/GenerateCredentialSpecResource.ps1) کمکی در قالب YAML تولید کرد.

گام‌های زیر نحوهٔ تولید دستی YAML مشخصات اعتبارنامهٔ GMSA را نشان می‌دهند؛ ابتدا مشخصات در قالب JSON ساخته و سپس تبدیل می‌شود:

1. [ماژول](https://github.com/MicrosoftDocs/Virtualization-Documentation/blob/live/windows-server-container-tools/ServiceAccounts/CredentialSpec.psm1)
   CredentialSpec را وارد کنید: `ipmo CredentialSpec.psm1`

1. با استفاده از `New-CredentialSpec` یک مشخصات اعتبارنامه در قالب JSON بسازید.
   برای ساختن مشخصات اعتبارنامهٔ GMSA با نام WebApp1، دستور
   `New-CredentialSpec -Name WebApp1 -AccountName WebApp1 -Domain $(Get-ADDomain -Current LocalComputer)` را اجرا کنید.

1. برای نمایش مسیر فایل JSON از `Get-CredentialSpec` استفاده کنید.

1. فایل credspec را از قالب JSON به قالب YAML تبدیل کنید و فیلدهای سرآیند لازم یعنی
   `apiVersion`، `kind`، `metadata` و `credspec` را به آن بیفزایید تا به یک
   منبع سفارشی GMSACredentialSpec تبدیل شود که بتوان آن را در کوبرنتیز پیکربندی کرد.

پیکربندی YAML زیر یک مشخصات اعتبارنامهٔ GMSA با نام `gmsa-WebApp1` را توصیف می‌کند:

```yaml
apiVersion: windows.k8s.io/v1
kind: GMSACredentialSpec
metadata:
  name: gmsa-WebApp1  # This is an arbitrary name but it will be used as a reference
credspec:
  ActiveDirectoryConfig:
    GroupManagedServiceAccounts:
    - Name: WebApp1   # Username of the GMSA account
      Scope: CONTOSO  # NETBIOS Domain Name
    - Name: WebApp1   # Username of the GMSA account
      Scope: contoso.com # DNS Domain Name
  CmsPlugins:
  - ActiveDirectory
  DomainJoinConfig:
    DnsName: contoso.com  # DNS Domain Name
    DnsTreeName: contoso.com # DNS Domain Name Root
    Guid: 244818ae-87ac-4fcd-92ec-e79e5252348a  # GUID of the Domain
    MachineAccountName: WebApp1 # Username of the GMSA account
    NetBiosName: CONTOSO  # NETBIOS Domain Name
    Sid: S-1-5-21-2126449477-2524075714-3094792973 # SID of the Domain
```

منبع مشخصات اعتبارنامهٔ بالا را می‌توان با نام `gmsa-Webapp1-credspec.yaml` ذخیره کرد
و با دستور `kubectl apply -f gmsa-Webapp1-credspec.yml` روی کلاستر اعمال کرد.

## پیکربندی ClusterRole برای فعال‌سازی RBAC روی مشخصات اعتبارنامهٔ GMSA مشخص

برای هر منبع مشخصات اعتبارنامهٔ GMSA باید یک ClusterRole تعریف شود. این نقش
به یک سوژه (subject)، که معمولاً یک حساب سرویس است، اجازه می‌دهد فعل `use` را روی یک منبع GMSA مشخص به کار ببرد.
مثال زیر یک ClusterRole را نشان می‌دهد که استفاده از
مشخصات اعتبارنامهٔ `gmsa-WebApp1` بالا را مجاز می‌کند. فایل را با نام gmsa-webapp1-role.yaml ذخیره کنید
و با دستور `kubectl apply -f gmsa-webapp1-role.yaml` اعمال کنید.

```yaml
# Create the Role to read the credspec
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: webapp1-role
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["use"]
  resourceNames: ["gmsa-WebApp1"]
```

## انتساب نقش به حساب‌های سرویس برای استفاده از credspecهای GMSA مشخص

حساب سرویسی که Podها با آن پیکربندی خواهند شد، باید به
ClusterRole ساخته‌شده در بالا متصل شود. با این کار، حساب سرویس مجاز می‌شود از منبع
مشخصات اعتبارنامهٔ GMSA موردنظر استفاده کند. نمونهٔ زیر نشان می‌دهد که حساب سرویس پیش‌فرض
به ClusterRole با نام `webapp1-role` متصل می‌شود تا از منبع مشخصات اعتبارنامهٔ `gmsa-WebApp1` که در بالا ساخته شد استفاده کند.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: allow-default-svc-account-read-on-gmsa-WebApp1
  namespace: default
subjects:
- kind: ServiceAccount
  name: default
  namespace: default
roleRef:
  kind: ClusterRole
  name: webapp1-role
  apiGroup: rbac.authorization.k8s.io
```

## پیکربندی ارجاع به مشخصات اعتبارنامهٔ GMSA در مشخصات Pod

برای تعیین ارجاع به منابع سفارشی مشخصات اعتبارنامهٔ GMSA موردنظر در مشخصات Pod،
از فیلد `securityContext.windowsOptions.gmsaCredentialSpecName` در مشخصات Pod استفاده می‌شود.
این فیلد همهٔ کانتینرهای موجود در مشخصات Pod را برای استفاده از GMSA مشخص‌شده پیکربندی می‌کند. در ادامه نمونه‌ای از
مشخصات Pod آمده است که در آن این فیلد برای ارجاع به `gmsa-WebApp1` پر شده است:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: with-creds
  name: with-creds
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      run: with-creds
  template:
    metadata:
      labels:
        run: with-creds
    spec:
      securityContext:
        windowsOptions:
          gmsaCredentialSpecName: gmsa-webapp1
      containers:
      - image: mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
        imagePullPolicy: Always
        name: iis
      nodeSelector:
        kubernetes.io/os: windows
```

تک‌تک کانتینرهای موجود در مشخصات Pod نیز می‌توانند با استفاده از فیلد
`securityContext.windowsOptions.gmsaCredentialSpecName` در سطح هر کانتینر، credspec مربوط به GMSA موردنظر خود را تعیین کنند. برای مثال:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: with-creds
  name: with-creds
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      run: with-creds
  template:
    metadata:
      labels:
        run: with-creds
    spec:
      containers:
      - image: mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
        imagePullPolicy: Always
        name: iis
        securityContext:
          windowsOptions:
            gmsaCredentialSpecName: gmsa-Webapp1
      nodeSelector:
        kubernetes.io/os: windows
```

هنگامی که مشخصات Podهایی با فیلدهای GMSA پرشده (به شرح بالا) در یک کلاستر اعمال می‌شوند،
رویدادهای زیر به ترتیب رخ می‌دهند:

1. وب‌هوک تغییردهنده همهٔ ارجاع‌ها به منابع مشخصات اعتبارنامهٔ GMSA را تفسیر می‌کند
   و آن‌ها را به محتوای مشخصات اعتبارنامهٔ GMSA گسترش می‌دهد.

1. وب‌هوک اعتبارسنج اطمینان حاصل می‌کند که حساب سرویس مرتبط با Pod
   برای به‌کاربردن فعل `use` روی مشخصات اعتبارنامهٔ GMSA مشخص‌شده مجاز است.

1. محیط اجرای کانتینر هر کانتینر ویندوزی را با مشخصات اعتبارنامهٔ GMSA مشخص‌شده
   پیکربندی می‌کند تا کانتینر بتواند هویت آن GMSA را در
   Active Directory به خود بگیرد و با همان هویت به سرویس‌های دامنه دسترسی پیدا کند.

## احراز هویت در اشتراک‌های شبکه با استفاده از نام میزبان یا FQDN

اگر در اتصال از Podها به اشتراک‌های SMB با استفاده از نام میزبان یا FQDN مشکل دارید،
اما از طریق نشانی IPv4 به این اشتراک‌ها دسترسی دارید، مطمئن شوید که کلید رجیستری زیر روی نودهای ویندوزی تنظیم شده باشد.

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Services\hns\State" /v EnableCompartmentNamespace /t REG_DWORD /d 1
```

پس از آن، Podهای در حال اجرا باید دوباره ساخته شوند تا تغییرات رفتاری را دریافت کنند.
اطلاعات بیشتر دربارهٔ نحوهٔ استفاده از این کلید رجیستری را می‌توانید
[اینجا](https://github.com/microsoft/hcsshim/blob/885f896c5a8548ca36c88c4b87fd2208c8d16543/internal/uvm/create.go#L74-L83) بیابید.

## عیب‌یابی

اگر در راه‌اندازی GMSA در محیط خود با مشکل روبه‌رو هستید،
چند گام عیب‌یابی وجود دارد که می‌توانید انجام دهید.

نخست، مطمئن شوید که credspec به Pod منتقل شده است. برای این کار باید
با `exec` وارد یکی از Podهای خود شوید و خروجی دستور `nltest.exe /parentdomain` را بررسی کنید.

در مثال زیر، Pod مقدار credspec را به‌درستی دریافت نکرده است:

```PowerShell
kubectl exec -it iis-auth-7776966999-n5nzr powershell.exe
```

اجرای `nltest.exe /parentdomain` به خطای زیر می‌انجامد:

```output
Getting parent domain failed: Status = 1722 0x6ba RPC_S_SERVER_UNAVAILABLE
```

اگر Pod شما credspec را به‌درستی دریافت کرده است، در گام بعد ارتباط با دامنه را بررسی کنید.
ابتدا از داخل Pod، با یک nslookup سریع ریشهٔ دامنهٔ خود را پیدا کنید.

این کار سه نکته را به ما نشان می‌دهد:

1. ‏Pod می‌تواند به DC دسترسی پیدا کند.
1. ‏DC می‌تواند به Pod دسترسی پیدا کند.
1. ‏DNS به‌درستی کار می‌کند.

اگر آزمون DNS و ارتباط با موفقیت انجام شد، در گام بعد باید بررسی کنید که آیا Pod
ارتباط کانال امن (secure channel) را با دامنه برقرار کرده است یا نه. برای این کار، باز هم
با `exec` وارد Pod خود شوید و دستور `nltest.exe /query` را اجرا کنید.

```PowerShell
nltest.exe /query
```

این دستور خروجی زیر را تولید می‌کند:

```output
I_NetLogonControl failed: Status = 1722 0x6ba RPC_S_SERVER_UNAVAILABLE
```

این خروجی نشان می‌دهد که Pod به دلیلی نتوانسته است با حساب مشخص‌شده در credspec
وارد دامنه شود. می‌توانید با اجرای دستور زیر برای ترمیم کانال امن تلاش کنید:

```PowerShell
nltest /sc_reset:domain.example
```

اگر دستور با موفقیت اجرا شود، خروجی‌ای مشابه زیر خواهید دید:

```output
Flags: 30 HAS_IP  HAS_TIMESERV
Trusted DC Name \\dc10.domain.example
Trusted DC Connection Status Status = 0 0x0 NERR_Success
The command completed successfully
```

اگر کار بالا خطا را برطرف کرد، می‌توانید با افزودن قلاب چرخهٔ حیات (lifecycle hook)
زیر به مشخصات Pod، این گام را خودکار کنید. اگر خطا برطرف نشد، باید
credspec خود را دوباره بررسی کنید و از درستی و کامل بودن آن مطمئن شوید.

```yaml
        image: registry.domain.example/iis-auth:1809v1
        lifecycle:
          postStart:
            exec:
              command: ["powershell.exe","-command","do { Restart-Service -Name netlogon } while ( $($Result = (nltest.exe /query); if ($Result -like '*0x0 NERR_Success*') {return $true} else {return $false}) -eq $false)"]
        imagePullPolicy: IfNotPresent
```

اگر بخش `lifecycle` نشان‌داده‌شده در بالا را به مشخصات Pod خود اضافه کنید، Pod
دستورهای فهرست‌شده را اجرا می‌کند تا سرویس `netlogon` را آن‌قدر راه‌اندازی مجدد کند که دستور `nltest.exe /query` بدون خطا پایان یابد.
