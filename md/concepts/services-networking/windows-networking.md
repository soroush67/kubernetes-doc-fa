---
reviewers:
- aravindhp
- jayunit100
- jsturtevant
- marosset
title: شبکه در ویندوز
content_type: concept
weight: 110
---

<!-- overview -->

کوبرنتیز از اجرای نودها روی لینوکس یا ویندوز پشتیبانی می‌کند و می‌توانید هر دو نوع نود را در یک کلاستر واحد کنار هم داشته باشید.
این صفحه نمای کلی‌ای از ویژگی‌های شبکه‌ی مختص سیستم‌عامل ویندوز ارائه می‌دهد.

<!-- body -->
## شبکه‌ی کانتینر در ویندوز {#networking}

شبکه‌ی کانتینرهای ویندوزی از طریق
[افزونه‌های CNI](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
در دسترس قرار می‌گیرد. کانتینرهای ویندوزی از نظر شبکه عملکردی مشابه ماشین‌های مجازی دارند. هر کانتینر یک آداپتور شبکه‌ی مجازی (vNIC) دارد که به یک سوئیچ مجازی Hyper-V (vSwitch) متصل است. سرویس شبکه‌ی میزبان (Host Networking Service یا HNS) و سرویس محاسبات میزبان (Host Compute Service یا HCS) با همکاری یکدیگر کانتینرها را ایجاد می‌کنند و vNICهای کانتینر را به شبکه‌ها متصل می‌کنند. مدیریت کانتینرها بر عهده‌ی HCS است، در حالی که HNS مدیریت منابع شبکه‌ای مانند موارد زیر را بر عهده دارد:

* شبکه‌های مجازی (از جمله ایجاد vSwitchها)
* نقاط پایانی (endpoint) / vNICها
* فضاهای نام
* سیاست‌ها، از جمله کپسوله‌سازی بسته‌ها، قواعد توزیع بار، فهرست‌های کنترل دسترسی (ACL) و قواعد NAT.

سرویس HNS و vSwitch در ویندوز، جداسازی مبتنی بر فضای نام را پیاده‌سازی می‌کنند و می‌توانند در صورت نیاز برای یک پاد یا کانتینر، NICهای مجازی ایجاد کنند. با این حال، بسیاری از پیکربندی‌ها مانند DNS، مسیرها و معیارها به‌جای اینکه مانند لینوکس به‌صورت فایل‌هایی در `/etc` ذخیره شوند، در پایگاه داده‌ی رجیستری ویندوز نگهداری می‌شوند. رجیستری ویندوز هر کانتینر از رجیستری میزبان جداست؛ بنابراین مفاهیمی مانند نگاشت `/etc/resolv.conf` از میزبان به داخل کانتینر، اثری را که در لینوکس دارند در ویندوز ندارند. این تنظیمات باید با استفاده از APIهای ویندوز و در بستر همان کانتینر پیکربندی شوند. به همین دلیل، پیاده‌سازی‌های CNI برای انتقال جزئیات شبکه به پاد یا کانتینر، به‌جای تکیه بر نگاشت فایل‌ها باید HNS را فراخوانی کنند.

## حالت‌های شبکه

ویندوز از پنج درایور یا حالت شبکه‌ی مختلف پشتیبانی می‌کند: L2bridge، L2tunnel، Overlay (بتا)، Transparent و NAT. در یک کلاستر ناهمگون که نودهای کارگر ویندوزی و لینوکسی دارد، باید راهکار شبکه‌ای را انتخاب کنید که با هر دو سیستم‌عامل ویندوز و لینوکس سازگار باشد. جدول زیر افزونه‌های خارج از درخت (out-of-tree) پشتیبانی‌شده در ویندوز را همراه با توصیه‌هایی درباره‌ی زمان مناسب استفاده از هر CNI فهرست می‌کند:

| درایور شبکه | توضیحات | تغییرات بسته‌های کانتینر | افزونه‌های شبکه | ویژگی‌های افزونه‌ی شبکه |
| -------------- | ----------- | ------------------------------ | --------------- | ------------------------------ |
| L2bridge       | کانتینرها به یک vSwitch خارجی متصل می‌شوند. کانتینرها به شبکه‌ی زیرین (underlay) متصل هستند، اما شبکه‌ی فیزیکی نیازی به یادگیری آدرس‌های MAC کانتینرها ندارد، زیرا این آدرس‌ها هنگام ورود و خروج بازنویسی می‌شوند. | آدرس MAC به MAC میزبان بازنویسی می‌شود و ممکن است آدرس IP نیز با استفاده از سیاست OutboundNAT در HNS به IP میزبان بازنویسی شود. | [win-bridge](https://www.cni.dev/plugins/current/main/win-bridge/)، [Azure-CNI](https://github.com/Azure/azure-container-networking/blob/master/docs/cni.md)، [Flannel host-gateway](https://github.com/flannel-io/flannel/blob/master/Documentation/backends.md#host-gw) که از win-bridge استفاده می‌کند | افزونه‌ی win-bridge از حالت شبکه‌ی L2bridge استفاده می‌کند و کانتینرها را به شبکه‌ی زیرین میزبان‌ها متصل می‌کند و بهترین کارایی را ارائه می‌دهد. برای ارتباط بین نودها به مسیرهای تعریف‌شده توسط کاربر (UDR) نیاز دارد. |
| L2Tunnel | این حالت، نوع خاصی از l2bridge است که فقط در Azure استفاده می‌شود. همه‌ی بسته‌ها به میزبان مجازی‌سازی فرستاده می‌شوند و سیاست SDN در آنجا اعمال می‌شود. | آدرس MAC بازنویسی می‌شود و آدرس IP در شبکه‌ی زیرین قابل مشاهده است | [Azure-CNI](https://github.com/Azure/azure-container-networking/blob/master/docs/cni.md) | افزونه‌ی Azure-CNI امکان یکپارچه‌سازی کانتینرها با Azure vNET را فراهم می‌کند و به آن‌ها اجازه می‌دهد از مجموعه قابلیت‌هایی که [Azure Virtual Network ارائه می‌دهد](https://azure.microsoft.com/en-us/services/virtual-network/) بهره ببرند؛ برای نمونه، اتصال امن به سرویس‌های Azure یا استفاده از NSGهای Azure. برای [چند نمونه به azure-cni](https://docs.microsoft.com/azure/aks/concepts-network#azure-cni-advanced-networking) مراجعه کنید |
| Overlay | به کانتینرها یک vNIC متصل به یک vSwitch خارجی داده می‌شود. هر شبکه‌ی overlay زیرشبکه‌ی IP مخصوص به خود را دارد که با یک پیشوند IP سفارشی تعریف می‌شود. درایور شبکه‌ی overlay از کپسوله‌سازی VXLAN استفاده می‌کند. | با یک سرآیند بیرونی کپسوله می‌شود. | [win-overlay](https://www.cni.dev/plugins/current/main/win-overlay/)، [Flannel VXLAN](https://github.com/flannel-io/flannel/blob/master/Documentation/backends.md#vxlan) (از win-overlay استفاده می‌کند) | زمانی باید از win-overlay استفاده کرد که بخواهید شبکه‌های مجازی کانتینرها از شبکه‌ی زیرین میزبان‌ها جدا باشند (برای مثال به دلایل امنیتی). اگر در مرکز داده‌ی خود با محدودیت آدرس IP روبه‌رو هستید، این حالت امکان استفاده‌ی مجدد از IPها را در شبکه‌های overlay مختلف (که برچسب‌های VNID متفاوتی دارند) فراهم می‌کند. این گزینه در Windows Server 2019 به [KB4489899](https://support.microsoft.com/help/4489899) نیاز دارد. |
| Transparent (کاربرد ویژه برای [ovn-kubernetes](https://github.com/openvswitch/ovn-kubernetes)) | به یک vSwitch خارجی نیاز دارد. کانتینرها به یک vSwitch خارجی متصل می‌شوند که ارتباط درون‌پادی را از طریق شبکه‌های منطقی (سوئیچ‌ها و مسیریاب‌های منطقی) ممکن می‌سازد. | برای رسیدن به پادهایی که روی همان میزبان نیستند، بسته از طریق تونل‌زنی [GENEVE](https://datatracker.ietf.org/doc/draft-gross-geneve/) یا [STT](https://datatracker.ietf.org/doc/draft-davie-stt/) کپسوله می‌شود.  <br/> بسته‌ها بر اساس اطلاعات فراداده‌ی تونل که کنترل‌کننده‌ی شبکه‌ی ovn فراهم می‌کند، ارسال یا دور ریخته می‌شوند. <br/> برای ارتباطات شمال-جنوب، NAT انجام می‌شود. | [ovn-kubernetes](https://github.com/openvswitch/ovn-kubernetes) | [استقرار از طریق ansible](https://github.com/openvswitch/ovn-kubernetes/tree/master/contrib). فهرست‌های کنترل دسترسی توزیع‌شده را می‌توان از طریق سیاست‌های کوبرنتیز اعمال کرد. از IPAM پشتیبانی می‌کند. توزیع بار بدون kube-proxy قابل انجام است. عمل NAT بدون استفاده از iptables/netsh انجام می‌شود. |
| NAT (*در کوبرنتیز استفاده نمی‌شود*) | به کانتینرها یک vNIC متصل به یک vSwitch داخلی داده می‌شود. سرویس DNS/DHCP با استفاده از مؤلفه‌ای داخلی به نام [WinNAT](https://techcommunity.microsoft.com/t5/virtualization/windows-nat-winnat-capabilities-and-limitations/ba-p/382303) ارائه می‌شود | آدرس‌های MAC و IP به MAC/IP میزبان بازنویسی می‌شوند. | [nat](https://github.com/Microsoft/windows-container-networking/tree/master/plugins/nat) | برای کامل بودن فهرست در اینجا آمده است |

همان‌طور که در بالا اشاره شد، [افزونه‌ی CNI](https://github.com/flannel-io/cni-plugin) مربوط به
[Flannel](https://github.com/coreos/flannel)
نیز در ویندوز [پشتیبانی می‌شود](https://github.com/flannel-io/cni-plugin#windows-support-experimental)؛ این پشتیبانی از طریق
[بک‌اند شبکه‌ی VXLAN](https://github.com/coreos/flannel/blob/master/Documentation/backends.md#vxlan) (**پشتیبانی بتا**؛ به win-overlay واگذار می‌کند)
و [بک‌اند شبکه‌ی host-gateway](https://github.com/coreos/flannel/blob/master/Documentation/backends.md#host-gw) (پشتیبانی پایدار؛ به win-bridge واگذار می‌کند) فراهم است.

این افزونه از واگذاری کار به یکی از افزونه‌های مرجع CNI (win-overlay و win-bridge) پشتیبانی می‌کند تا همراه با دیمن Flannel در ویندوز (Flanneld)، تخصیص اجاره‌ی زیرشبکه‌ی نود و ایجاد شبکه‌ی HNS را به‌صورت خودکار انجام دهد. این افزونه فایل پیکربندی خود (cni.conf) را می‌خواند و آن را با متغیرهای محیطی فایل subnet.env که FlannelD تولید کرده است، ترکیب می‌کند. سپس کار برقراری اتصالات شبکه را به یکی از افزونه‌های مرجع CNI واگذار می‌کند و پیکربندی درست را که شامل زیرشبکه‌ی تخصیص‌یافته به نود است، به افزونه‌ی IPAM (برای نمونه `host-local`) می‌فرستد.

برای آبجکت‌های Node، Pod و Service، جریان‌های شبکه‌ی زیر برای ترافیک TCP/UDP پشتیبانی می‌شوند:

* Pod → Pod (IP)
* Pod → Pod (نام)
* Pod → Service (Cluster IP)
* Pod → Service (PQDN، اما فقط در صورتی که هیچ "." وجود نداشته باشد)
* Pod → Service (FQDN)
* Pod → خارج از کلاستر (IP)
* Pod → خارج از کلاستر (DNS)
* Node → Pod
* Pod → Node

## مدیریت آدرس IP (IPAM) {#ipam}

گزینه‌های IPAM زیر در ویندوز پشتیبانی می‌شوند:

* [host-local](https://github.com/containernetworking/plugins/tree/master/plugins/ipam/host-local)
* [azure-vnet-ipam](https://github.com/Azure/azure-container-networking/blob/master/docs/ipam.md) (فقط برای azure-cni)
* [Windows Server IPAM](https://docs.microsoft.com/windows-server/networking/technologies/ipam/ipam-top) (گزینه‌ی جایگزین در صورتی که هیچ IPAMی تنظیم نشده باشد)

## بازگشت مستقیم سرور (DSR) {#dsr}

{{< feature-state feature_gate_name="WinDSR" >}}

بازگشت مستقیم سرور (Direct Server Return) حالتی از توزیع بار است که در آن اصلاحات آدرس IP و LBNAT مستقیماً در درگاه vSwitch کانتینر انجام می‌شود و ترافیک سرویس با آدرس IP مبدأ برابر با IP پاد آغازکننده می‌رسد. این حالت با فراهم کردن امکان عبور ترافیک بازگشتی از کنار توزیع‌کننده‌ی بار و پاسخ مستقیم به کلاینت، کارایی را بهبود می‌دهد؛ در نتیجه هم بار روی توزیع‌کننده‌ی بار کاهش می‌یابد و هم تأخیر کلی کمتر می‌شود. برای اطلاعات بیشتر، مقاله‌ی
[Direct Server Return (DSR) in a nutshell](https://techcommunity.microsoft.com/blog/networkingblog/direct-server-return-dsr-in-a-nutshell/693710) را بخوانید.

## توزیع بار و Serviceها

یک {{< glossary_tooltip text="Service" term_id="service" >}} در کوبرنتیز، انتزاعی است که مجموعه‌ای منطقی از Podها و روشی برای دسترسی به آن‌ها از طریق شبکه را تعریف می‌کند.
در کلاستری که نودهای ویندوزی دارد، می‌توانید از انواع Service زیر استفاده کنید:

* `NodePort`
* `ClusterIP`
* `LoadBalancer`
* `ExternalName`

شبکه‌ی کانتینرهای ویندوزی از چند جنبه‌ی مهم با شبکه‌ی لینوکس تفاوت دارد.
[مستندات مایکروسافت درباره‌ی شبکه‌ی کانتینرهای ویندوز](https://docs.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture)
جزئیات و پیش‌زمینه‌ی بیشتری در این باره ارائه می‌دهد.

در ویندوز می‌توانید از تنظیمات زیر برای پیکربندی Serviceها و رفتار توزیع بار استفاده کنید:

{{< table caption="تنظیمات Service در ویندوز" >}}
| قابلیت | توضیحات | حداقل نسخه‌ی پشتیبانی‌شده‌ی سیستم‌عامل ویندوز | نحوه‌ی فعال‌سازی |
| ------- | ----------- | -------------------------- | ------------- |
| وابستگی نشست (Session affinity) | تضمین می‌کند که اتصال‌های یک کلاینت مشخص هر بار به همان Pod فرستاده شوند. | Windows Server 2022 | مقدار `service.spec.sessionAffinity` را برابر "ClientIP" قرار دهید |
| بازگشت مستقیم سرور (DSR) | به یادداشت‌های [DSR](#dsr) در بالا مراجعه کنید. | Windows Server 2019 | آرگومان خط فرمان زیر را تنظیم کنید (با فرض نسخه‌ی {{< skew currentVersion >}}): ` --enable-dsr=true` |
| حفظ مقصد (Preserve-Destination) | از اعمال DNAT روی ترافیک سرویس صرف‌نظر می‌کند و به این ترتیب IP مجازی سرویس مقصد را در بسته‌هایی که به Pod بک‌اند می‌رسند حفظ می‌کند. همچنین ارسال نود به نود را غیرفعال می‌کند. | Windows Server، نسخه‌ی 1903 | مقدار `"preserve-destination": "true"` را در حاشیه‌نویسی‌های سرویس تنظیم کنید و DSR را در kube-proxy فعال کنید. |
| شبکه‌ی دوپشته‌ای IPv4/IPv6 | ارتباطات بومی IPv4 به IPv4 به‌موازات ارتباطات IPv6 به IPv6، به کلاستر، از کلاستر و درون آن | Windows Server 2019 | به [دوپشته‌ای IPv4/IPv6](/docs/concepts/services-networking/dual-stack/#windows-support) مراجعه کنید |
| حفظ IP کلاینت | تضمین می‌کند که IP مبدأ ترافیک ورودی حفظ شود. همچنین ارسال نود به نود را غیرفعال می‌کند. |  Windows Server 2019  | مقدار `service.spec.externalTrafficPolicy` را برابر "Local" قرار دهید و DSR را در kube-proxy فعال کنید |
{{< /table >}}

## محدودیت‌ها

قابلیت‌های شبکه‌ای زیر در نودهای ویندوزی پشتیبانی _نمی‌شوند_:

* حالت شبکه‌ی میزبان (host networking)
* دسترسی محلی به NodePort از خود نود (برای نودهای دیگر یا کلاینت‌های خارجی کار می‌کند)
* بیش از ۶۴ پاد بک‌اند (یا آدرس مقصد یکتا) برای یک Service واحد
* ارتباط IPv6 بین پادهای ویندوزی متصل به شبکه‌های overlay
* سیاست ترافیک محلی (Local Traffic Policy) در حالت غیر DSR
* ارتباط خروجی با پروتکل ICMP از طریق `win-overlay`، `win-bridge` یا با استفاده از افزونه‌ی Azure-CNI.
  به‌طور مشخص، صفحه‌ی داده‌ی ویندوز ([VFP](https://www.microsoft.com/research/project/azure-virtual-filtering-platform/))
  از جابه‌جایی (transposition) بسته‌های ICMP پشتیبانی نمی‌کند و این یعنی:
  * بسته‌های ICMP که به مقصدهایی درون همان شبکه فرستاده می‌شوند (مانند ارتباط پاد با پاد از طریق ping)
    طبق انتظار کار می‌کنند؛
  * بسته‌های TCP/UDP طبق انتظار کار می‌کنند؛
  * بسته‌های ICMP که باید از یک شبکه‌ی راه دور عبور کنند (برای مثال ارتباط پاد با اینترنت خارجی از طریق ping)
    قابل جابه‌جایی نیستند و در نتیجه به مبدأ خود بازگردانده نمی‌شوند؛
  * از آنجا که بسته‌های TCP/UDP همچنان قابل جابه‌جایی هستند، هنگام اشکال‌زدایی اتصال با دنیای بیرون می‌توانید به‌جای `ping <destination>` از
    `curl <destination>` استفاده کنید.

محدودیت‌های دیگر:

* افزونه‌های شبکه‌ی مرجع ویندوز، یعنی win-bridge و win-overlay، به دلیل نبود پیاده‌سازی `CHECK`،
  [مشخصات CNI](https://github.com/containernetworking/cni/blob/master/SPEC.md) نسخه‌ی v0.4.0 را پیاده‌سازی نمی‌کنند.
* افزونه‌ی Flannel VXLAN CNI در ویندوز محدودیت‌های زیر را دارد:
  * اتصال نود به پاد فقط برای پادهای محلی و با Flannel نسخه‌ی v0.12.0 (یا بالاتر) امکان‌پذیر است.
  * استفاده‌ی Flannel به VNI 4096 و درگاه UDP 4789 محدود است. برای جزئیات بیشتر درباره‌ی این پارامترها، به مستندات رسمی بک‌اند
    [Flannel VXLAN](https://github.com/coreos/flannel/blob/master/Documentation/backends.md#vxlan)
    مراجعه کنید.
