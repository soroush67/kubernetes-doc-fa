---
reviewers:
- aravindhp
- jayunit100
- jsturtevant
- marosset
title: نکات اشکال‌زدایی در ویندوز
content_type: concept
---

<!-- overview -->

<!-- body -->

## عیب‌یابی در سطح نود {#troubleshooting-node}

1. پادهای من در وضعیت «Container Creating» گیر کرده‌اند یا مدام راه‌اندازی مجدد می‌شوند

   مطمئن شوید که ایمیج pause شما با نسخهٔ سیستم‌عامل ویندوز سازگار است.
   برای دیدن جدیدترین یا توصیه‌شده‌ترین ایمیج pause و کسب اطلاعات بیشتر، به
   [کانتینر pause](/docs/concepts/windows/intro/#pause-container) مراجعه کنید.

   {{< note >}}
   اگر از containerd به‌عنوان محیط اجرای کانتینر استفاده می‌کنید، ایمیج pause در فیلد
   `plugins.plugins.cri.sandbox_image` از فایل پیکربندی config.toml مشخص می‌شود.
   {{< /note >}}

1. وضعیت پادهای من `ErrImgPull` یا `ImagePullBackOff` نشان داده می‌شود

   مطمئن شوید که Pod شما روی یک نود ویندوزی
   [سازگار](https://docs.microsoft.com/virtualization/windowscontainers/deploy-containers/version-compatibility)
   زمان‌بندی می‌شود.

   اطلاعات بیشتر دربارهٔ نحوهٔ تعیین یک نود سازگار برای Pod را می‌توانید در
   [این راهنما](/docs/concepts/windows/user-guide/#ensuring-os-specific-workloads-land-on-the-appropriate-container-host) بیابید.

## عیب‌یابی شبکه {#troubleshooting-network}

1. پادهای ویندوزی من اتصال شبکه ندارند

   اگر از ماشین‌های مجازی استفاده می‌کنید، مطمئن شوید که جعل آدرس MAC (MAC spoofing)
   روی همهٔ آداپتورهای شبکهٔ ماشین مجازی **فعال** باشد.

1. پادهای ویندوزی من نمی‌توانند منابع خارجی را ping کنند

   برای پادهای ویندوزی هیچ قاعدهٔ خروجی برای پروتکل ICMP تنظیم نشده است، اما
   از TCP/UDP پشتیبانی می‌شود. هنگامی که می‌خواهید اتصال به منابع بیرون از
   کلاستر را بررسی کنید، به‌جای `ping <IP>` از دستورهای متناظر `curl <IP>`
   استفاده کنید.

   اگر همچنان با مشکل روبه‌رو هستید، به احتمال زیاد پیکربندی شبکهٔ شما در
   [cni.conf](https://github.com/Microsoft/SDN/blob/master/Kubernetes/flannel/l2bridge/cni/config/cni.conf)
   نیاز به بررسی بیشتری دارد. شما همیشه می‌توانید این فایل ایستا را ویرایش کنید.
   به‌روزرسانی پیکربندی روی همهٔ منابع جدید کوبرنتیز اعمال خواهد شد.

   یکی از الزامات شبکه در کوبرنتیز
   (به [مدل کوبرنتیز](/docs/concepts/cluster-administration/networking/) مراجعه کنید)
   این است که ارتباطات درون کلاستر بدون NAT انجام شود. برای رعایت این الزام، یک
   [ExceptionList](https://github.com/Microsoft/SDN/blob/master/Kubernetes/flannel/l2bridge/cni/config/cni.conf#L20)
   برای همهٔ ارتباطاتی وجود دارد که نمی‌خواهید NAT خروجی روی آن‌ها انجام شود. با این
   حال، معنای این موضوع آن است که باید IP خارجی‌ای را که قصد دسترسی به آن را دارید
   از `ExceptionList` حذف کنید. تنها در این صورت است که ترافیک ارسالی از پادهای
   ویندوزی شما به‌درستی SNAT می‌شود و پاسخی از دنیای بیرون دریافت می‌کند. بر این
   اساس، `ExceptionList` شما در `cni.conf` باید به شکل زیر باشد:

   ```conf
   "ExceptionList": [
                   "10.244.0.0/16",  # Cluster subnet
                   "10.96.0.0/12",   # Service subnet
                   "10.127.130.0/24" # Management (host) subnet
               ]
   ```

1. نود ویندوزی من نمی‌تواند به Serviceهایی از نوع `NodePort` دسترسی پیدا کند

   دسترسی محلی به NodePort از خود نود با شکست مواجه می‌شود. این یک محدودیت
   شناخته‌شده است. دسترسی به NodePort از نودهای دیگر یا کلاینت‌های خارجی کار می‌کند.

1. کارت‌های شبکهٔ مجازی (vNIC) و endpointهای HNS کانتینرها حذف می‌شوند

   این مشکل ممکن است زمانی رخ دهد که پارامتر `hostname-override` به
   [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/) داده نشده باشد.
   برای رفع آن، کاربران باید نام میزبان را به شکل زیر به kube-proxy بدهند:

   ```powershell
   C:\k\kube-proxy.exe --hostname-override=$(hostname)
   ```

1. نود ویندوزی من نمی‌تواند با استفاده از IP سرویس به سرویس‌هایم دسترسی پیدا کند

   این یک محدودیت شناخته‌شده در پشتهٔ شبکهٔ ویندوز است. با این حال، پادهای ویندوزی می‌توانند به IP سرویس دسترسی داشته باشند.

1. هنگام راه‌اندازی kubelet هیچ آداپتور شبکه‌ای پیدا نمی‌شود

   پشتهٔ شبکهٔ ویندوز برای کارکرد شبکهٔ کوبرنتیز به یک آداپتور مجازی نیاز دارد.
   اگر دستورهای زیر (در یک پوستهٔ مدیریتی) هیچ نتیجه‌ای برنگردانند، ایجاد شبکهٔ
   مجازی، که پیش‌نیاز ضروری کارکرد kubelet است، با شکست مواجه شده است:

   ```powershell
   Get-HnsNetwork | ? Name -ieq "cbr0"
   Get-NetAdapter | ? Name -Like "vEthernet (Ethernet*"
   ```

   در مواردی که نام آداپتور شبکهٔ میزبان «Ethernet» نیست، اغلب بهتر است پارامتر
   [InterfaceName](https://github.com/microsoft/SDN/blob/master/Kubernetes/flannel/start.ps1#L7)
   در اسکریپت `start.ps1` را تغییر دهید. در غیر این صورت، خروجی اسکریپت
   `start-kubelet.ps1` را بررسی کنید تا ببینید آیا هنگام ایجاد شبکهٔ مجازی خطایی رخ داده است یا نه.

1. تفکیک نام DNS به‌درستی کار نمی‌کند

   محدودیت‌های DNS در ویندوز را در این [بخش](/docs/concepts/services-networking/dns-pod-service/#dns-windows) بررسی کنید.

1. دستور `kubectl port-forward` با خطای «unable to do port forwarding: wincat not found» شکست می‌خورد

   این قابلیت در کوبرنتیز 1.15 با گنجاندن `wincat.exe` در کانتینر زیرساختی pause
   با نام `mcr.microsoft.com/oss/kubernetes/pause:3.6` پیاده‌سازی شد.
   حتماً از یک نسخهٔ پشتیبانی‌شده از کوبرنتیز استفاده کنید.
   اگر می‌خواهید کانتینر زیرساختی pause خودتان را بسازید، حتماً
   [wincat](https://github.com/kubernetes/kubernetes/tree/master/build/pause/windows/wincat) را در آن بگنجانید.

1. نصب کوبرنتیز من با شکست مواجه می‌شود، چون نود Windows Server من پشت یک پروکسی قرار دارد

   اگر پشت یک پروکسی هستید، باید متغیرهای محیطی PowerShell زیر را تعریف کنید:

   ```PowerShell
   [Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://proxy.example.com:80/", [EnvironmentVariableTarget]::Machine)
   [Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://proxy.example.com:443/", [EnvironmentVariableTarget]::Machine)
   ```

### عیب‌یابی Flannel

1. هنگام استفاده از Flannel، نودهای من پس از پیوستن دوباره به کلاستر دچار مشکل می‌شوند

   هر بار که نودی که قبلاً حذف شده دوباره به کلاستر می‌پیوندد، flannelD تلاش
   می‌کند یک زیرشبکهٔ پاد جدید به آن نود اختصاص دهد. کاربران باید فایل‌های
   پیکربندی زیرشبکهٔ پاد قدیمی را از مسیرهای زیر حذف کنند:

   ```powershell
   Remove-Item C:\k\SourceVip.json
   Remove-Item C:\k\SourceVipRequest.json
   ```

1. فرایند Flanneld در وضعیت «Waiting for the Network to be created» گیر کرده است

   گزارش‌های متعددی دربارهٔ این [مشکل](https://github.com/coreos/flannel/issues/1066) وجود دارد.
   به احتمال زیاد این مشکل به زمان‌بندی تنظیم IP مدیریتی شبکهٔ flannel مربوط است.
   یک راه‌حل موقت این است که `start.ps1` را دوباره اجرا کنید یا آن را به‌صورت دستی و به شکل زیر دوباره راه‌اندازی کنید:

   ```powershell
   [Environment]::SetEnvironmentVariable("NODE_NAME", "<Windows_Worker_Hostname>")
   C:\flannel\flanneld.exe --kubeconfig-file=c:\k\config --iface=<Windows_Worker_Node_IP> --ip-masq=1 --kube-subnet-mgr=1
   ```

1. پادهای ویندوزی من به دلیل نبود فایل `/run/flannel/subnet.env` راه‌اندازی نمی‌شوند

   این خطا نشان می‌دهد که Flannel به‌درستی راه‌اندازی نشده است. می‌توانید
   `flanneld.exe` را دوباره راه‌اندازی کنید، یا فایل‌ها را به‌صورت دستی از
   `/run/flannel/subnet.env` روی master کوبرنتیز به `C:\run\flannel\subnet.env`
   روی نود کارگر ویندوزی کپی کنید و سطر `FLANNEL_SUBNET` را به عدد دیگری تغییر
   دهید. برای نمونه، اگر زیرشبکهٔ 10.244.4.1/24 برای نود مدنظر باشد:

   ```env
   FLANNEL_NETWORK=10.244.0.0/16
   FLANNEL_SUBNET=10.244.4.1/24
   FLANNEL_MTU=1500
   FLANNEL_IPMASQ=true
   ```

### بررسی بیشتر

اگر این مراحل مشکل شما را حل نکرد، می‌توانید برای اجرای کانتینرهای ویندوزی روی نودهای ویندوزی در کوبرنتیز از منابع زیر کمک بگیرید:

* موضوع [Windows Server Container](https://stackoverflow.com/questions/tagged/windows-server-container) در StackOverflow
* انجمن رسمی کوبرنتیز [discuss.kubernetes.io](https://discuss.kubernetes.io/)
* [کانال ‎#SIG-Windows](https://kubernetes.slack.com/messages/sig-windows) در Slack کوبرنتیز
