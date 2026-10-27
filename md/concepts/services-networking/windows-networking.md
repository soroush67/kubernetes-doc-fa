---
reviewers:
- aravindhp
- jayunit100
- jsturtevant
- marosset
title: شبکه‌بندی در ویندوز
content_type: concept
weight: 110
---

<!-- overview -->

کوبرنتیز از اجرای نودها بر روی لینوکس یا ویندوز پشتیبانی می‌کند. می‌توانید هر دو نوع نود را
در یک کلاستر واحد با یکدیگر ترکیب کنید.
این صفحه مروری بر شبکه‌بندی مختص سیستم‌عامل ویندوز ارائه می‌دهد.

<!-- body -->
## شبکه‌بندی کانتینر در ویندوز {#networking}

شبکه‌بندی کانتینرهای ویندوز از طریق
[افزونه‌های CNI](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
ارائه می‌شود.
کانتینرهای ویندوز از نظر شبکه‌بندی شبیه ماشین‌های مجازی عمل می‌کنند.
هر کانتینر یک آداپتور شبکه مجازی (vNIC) دارد که به یک سوئیچ مجازی Hyper-V (vSwitch) متصل است.
سرویس شبکه میزبان (HNS) و سرویس محاسبات میزبان (HCS) با یکدیگر همکاری می‌کنند تا کانتینرها را ایجاد کنند و
vNICهای کانتینرها را به شبکه‌ها متصل نمایند. HCS مسئول مدیریت کانتینرهاست، در حالی که HNS
مسئول مدیریت منابع شبکه‌ای مانند موارد زیر است:

* شبکه‌های مجازی (از جمله ایجاد vSwitchها)
* Endpointها / vNICها
* فضاهای نام (Namespaces)
* سیاست‌ها، از جمله کپسوله‌سازی بسته‌ها، قوانین توزیع بار، ACLها و قوانین NAT.

HNS و vSwitch در ویندوز، فضای نام را پیاده‌سازی می‌کنند و
می‌توانند در صورت نیاز برای یک پاد یا کانتینر، کارت‌های شبکه مجازی ایجاد کنند. با این حال، بسیاری از پیکربندی‌ها
مانند DNS، مسیرها (routes) و متریک‌ها در پایگاه داده رجیستری ویندوز ذخیره می‌شوند، نه به‌صورت
فایل در مسیر `/etc` که روش ذخیره‌سازی این پیکربندی‌ها در لینوکس است. رجیستری ویندوز مربوط به کانتینر
از رجیستری میزبان جداست، بنابراین مفاهیمی مانند نگاشت `/etc/resolv.conf` از
میزبان به داخل کانتینر، همان تأثیری را که در لینوکس دارند، ندارند. این موارد باید
با استفاده از APIهای ویندوز که در بستر همان کانتینر اجرا می‌شوند پیکربندی شوند. بنابراین
پیاده‌سازی‌های CNI باید به‌جای تکیه بر نگاشت فایل‌ها برای انتقال جزئیات شبکه
به پاد یا کانتینر، HNS را فراخوانی کنند.

## حالت‌های شبکه {#network-modes}

ویندوز از پنج درایور/حالت شبکه‌بندی مختلف پشتیبانی می‌کند: L2bridge، L2tunnel،
Overlay (بتا)، Transparent و NAT. در یک کلاستر ناهمگن شامل نودهای کارگر ویندوز و لینوکس،
باید راهکار شبکه‌بندی‌ای را انتخاب کنید که هم با ویندوز و هم با لینوکس سازگار باشد.
جدول زیر افزونه‌های خارج از درخت (out-of-tree) پشتیبانی‌شده در ویندوز را فهرست می‌کند،
همراه با توصیه‌هایی درباره اینکه هر CNI در چه مواردی استفاده شود:

| درایور شبکه | توضیح | تغییرات بسته کانتینر | افزونه‌های شبکه | ویژگی‌های افزونه شبکه |
| -------------- | ----------- | ------------------------------ | --------------- | ------------------------------ |
| L2bridge       | کانتینرها به یک vSwitch خارجی متصل می‌شوند. کانتینرها به شبکه زیرین (underlay) متصل‌اند، هرچند شبکه فیزیکی نیازی به یادگیری MACهای کانتینرها ندارد، زیرا این آدرس‌ها در ورودی/خروجی بازنویسی می‌شوند. | MAC به MAC میزبان بازنویسی می‌شود و IP ممکن است با استفاده از سیاست HNS OutboundNAT به IP میزبان بازنویسی شود. | [win-bridge](https://www.cni.dev/plugins/current/main/win-bridge/)، [Azure-CNI](https://github.com/Azure/azure-container-networking/blob/master/docs/cni.md)، [Flannel host-gateway](https://github.com/flannel-io/flannel/blob/master/Documentation/backends.md#host-gw) از win-bridge استفاده می‌کند | win-bridge از حالت شبکه L2bridge استفاده می‌کند و کانتینرها را به شبکه زیرین میزبان‌ها متصل می‌کند که بهترین کارایی را ارائه می‌دهد. برای اتصال بین نودها به مسیرهای تعریف‌شده توسط کاربر (UDR) نیاز دارد. |
| L2Tunnel | این حالت یک مورد خاص از l2bridge است، اما فقط در Azure استفاده می‌شود. تمام بسته‌ها به میزبان مجازی‌سازی ارسال می‌شوند و در آنجا سیاست SDN اعمال می‌شود. | MAC بازنویسی می‌شود، IP در شبکه زیرین قابل مشاهده است | [Azure-CNI](https://github.com/Azure/azure-container-networking/blob/master/docs/cni.md) | Azure-CNI امکان یکپارچه‌سازی کانتینرها با Azure vNET را فراهم می‌کند و به آن‌ها اجازه می‌دهد از مجموعه قابلیت‌هایی که [Azure Virtual Network ارائه می‌دهد](https://azure.microsoft.com/en-us/services/virtual-network/) بهره ببرند. برای مثال، اتصال امن به سرویس‌های Azure یا استفاده از Azure NSGها. برای مشاهده چند نمونه، [azure-cni for some examples](https://docs.microsoft.com/azure/aks/concepts-network#azure-cni-advanced-networking) را ببینید |
| Overlay | به کانتینرها یک vNIC داده می‌شود که به یک vSwitch خارجی متصل است. هر شبکه overlay زیرشبکه IP مخصوص به خود را دارد که با یک پیشوند IP سفارشی تعریف می‌شود. درایور شبکه overlay از کپسوله‌سازی VXLAN استفاده می‌کند. | با یک هدر بیرونی کپسوله می‌شود. | [win-overlay](https://www.cni.dev/plugins/current/main/win-overlay/)، [Flannel VXLAN](https://github.com/flannel-io/flannel/blob/master/Documentation/backends.md#vxlan) (از win-overlay استفاده می‌کند) | win-overlay زمانی باید استفاده شود که بخواهید شبکه‌های مجازی کانتینرها از شبکه زیرین میزبان‌ها ایزوله باشند (مثلاً به دلایل امنیتی). اگر در مرکز داده خود با محدودیت IP مواجه هستید، امکان استفاده مجدد از IPها را برای شبکه‌های overlay مختلف (که برچسب‌های VNID متفاوتی دارند) فراهم می‌کند. این گزینه در Windows Server 2019 به [KB4489899](https://support.microsoft.com/help/4489899) نیاز دارد. |
| Transparent (مورد استفاده خاص برای [ovn-kubernetes](https://github.com/openvswitch/ovn-kubernetes)) | به یک vSwitch خارجی نیاز دارد. کانتینرها به یک vSwitch خارجی متصل می‌شوند که ارتباط درون‌پادی را از طریق شبکه‌های منطقی (سوئیچ‌ها و روترهای منطقی) امکان‌پذیر می‌کند. | برای دسترسی به پادهایی که روی یک میزبان نیستند، بسته از طریق تونل‌زنی [GENEVE](https://datatracker.ietf.org/doc/draft-gross-geneve/) یا [STT](https://datatracker.ietf.org/doc/draft-davie-stt/) کپسوله می‌شود.  <br/> بسته‌ها بر اساس اطلاعات فراداده تونل که توسط کنترل‌کننده شبکه ovn ارائه می‌شود، هدایت یا حذف می‌شوند. <br/> برای ارتباط شمال-جنوب، NAT انجام می‌شود. | [ovn-kubernetes](https://github.com/openvswitch/ovn-kubernetes) | [استقرار از طریق ansible](https://github.com/openvswitch/ovn-kubernetes/tree/master/contrib). ACLهای توزیع‌شده را می‌توان از طریق سیاست‌های کوبرنتیز اعمال کرد. از IPAM پشتیبانی می‌کند. توزیع بار بدون kube-proxy قابل دستیابی است. NAT بدون استفاده از iptables/netsh انجام می‌شود. |
| NAT (*در کوبرنتیز استفاده نمی‌شود*) | به کانتینرها یک vNIC داده می‌شود که به یک vSwitch داخلی متصل است. DNS/DHCP با استفاده از یک مؤلفه داخلی به نام [WinNAT](https://techcommunity.microsoft.com/t5/virtualization/windows-nat-winnat-capabilities-and-limitations/ba-p/382303) ارائه می‌شود | MAC و IP به MAC/IP میزبان بازنویسی می‌شوند. | [nat](https://github.com/Microsoft/windows-container-networking/tree/master/plugins/nat) | برای کامل بودن فهرست در اینجا آمده است |

همان‌طور که در بالا بیان شد، [افزونه CNI](https://github.com/flannel-io/cni-plugin) مربوط به
[Flannel](https://github.com/coreos/flannel)
نیز در ویندوز از طریق
[بک‌اند شبکه VXLAN](https://github.com/coreos/flannel/blob/master/Documentation/backends.md#vxlan) (**پشتیبانی بتا**؛ واگذاری به win-overlay)
و [بک‌اند شبکه host-gateway](https://github.com/coreos/flannel/blob/master/Documentation/backends.md#host-gw) (پشتیبانی پایدار؛ واگذاری به win-bridge)
[پشتیبانی می‌شود](https://github.com/flannel-io/cni-plugin#windows-support-experimental).

این افزونه از واگذاری کار به یکی از افزونه‌های CNI مرجع (win-overlay،
win-bridge) پشتیبانی می‌کند تا در ویندوز همراه با دیمون Flannel (Flanneld) برای
تخصیص خودکار اجاره زیرشبکه نود و ایجاد شبکه HNS کار کند. این افزونه
فایل پیکربندی خودش (cni.conf) را می‌خواند و آن را با متغیرهای محیطی
فایل subnet.env تولیدشده توسط FlannelD ترکیب می‌کند. سپس برای برقراری اتصالات شبکه، کار را به یکی از
افزونه‌های CNI مرجع واگذار می‌کند و پیکربندی صحیح
حاوی زیرشبکه اختصاص‌یافته به نود را به افزونه IPAM (برای مثال: `host-local`) ارسال می‌کند.

برای آبجکت‌های Node، Pod و Service، جریان‌های شبکه‌ای زیر برای
ترافیک TCP/UDP پشتیبانی می‌شوند:

* Pod → Pod (IP)
* Pod → Pod (نام)
* Pod → Service (Cluster IP)
* Pod → Service (PQDN، اما تنها در صورتی که شامل «.» نباشد)
* Pod → Service (FQDN)
* Pod → خارجی (IP)
* Pod → خارجی (DNS)
* Node → Pod
* Pod → Node

## مدیریت آدرس IP (IPAM) {#ipam}

گزینه‌های IPAM زیر در ویندوز پشتیبانی می‌شوند:

* [host-local](https://github.com/containernetworking/plugins/tree/master/plugins/ipam/host-local)
* [azure-vnet-ipam](https://github.com/Azure/azure-container-networking/blob/master/docs/ipam.md) (فقط برای azure-cni)
* [Windows Server IPAM](https://docs.microsoft.com/windows-server/networking/technologies/ipam/ipam-top) (گزینه جایگزین در صورتی که هیچ IPAM‌ای تنظیم نشده باشد)

## Direct Server Return (DSR) {#dsr}

{{< feature-state feature_gate_name="WinDSR" >}}

یک حالت توزیع بار که در آن اصلاح آدرس IP و LBNAT مستقیماً در پورت vSwitch کانتینر انجام می‌شود؛
ترافیک سرویس با IP مبدأ تنظیم‌شده روی IP پادِ مبدأ می‌رسد.
این حالت با اجازه دادن به ترافیک بازگشتی که از طریق متعادل‌کننده‌های بار مسیریابی می‌شود تا
متعادل‌کننده بار را دور بزند و مستقیماً به کلاینت پاسخ دهد، بهینه‌سازی کارایی ایجاد می‌کند؛
بدین ترتیب بار روی متعادل‌کننده بار کاهش می‌یابد و تأخیر کلی نیز کم می‌شود.
برای اطلاعات بیشتر،
[Direct Server Return (DSR) in a nutshell](https://techcommunity.microsoft.com/blog/networkingblog/direct-server-return-dsr-in-a-nutshell/693710) را بخوانید.

## توزیع بار و Serviceها {#load-balancing-and-services}

{{< glossary_tooltip text="Service" term_id="service" >}} در کوبرنتیز یک انتزاع است
که مجموعه‌ای منطقی از Podها و روشی برای دسترسی به آن‌ها از طریق شبکه را تعریف می‌کند.
در کلاستری که شامل نودهای ویندوز است، می‌توانید از انواع Service زیر استفاده کنید:

* `NodePort`
* `ClusterIP`
* `LoadBalancer`
* `ExternalName`

شبکه‌بندی کانتینر در ویندوز از چند جنبه مهم با شبکه‌بندی لینوکس تفاوت دارد.
[مستندات مایکروسافت درباره شبکه‌بندی کانتینر ویندوز](https://docs.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture)
جزئیات و پیش‌زمینه بیشتری ارائه می‌دهد.

در ویندوز، می‌توانید از تنظیمات زیر برای پیکربندی Serviceها و
رفتار توزیع بار استفاده کنید:

{{< table caption="تنظیمات Service در ویندوز" >}}
| ویژگی | توضیح | حداقل نسخه build پشتیبانی‌شده سیستم‌عامل ویندوز | نحوه فعال‌سازی |
| ------- | ----------- | -------------------------- | ------------- |
| Session affinity | تضمین می‌کند که اتصال‌های یک کلاینت مشخص هر بار به همان Pod هدایت شوند. | Windows Server 2022 | مقدار `service.spec.sessionAffinity` را روی "ClientIP" تنظیم کنید |
| Direct Server Return (DSR) | یادداشت‌های [DSR](#dsr) در بالا را ببینید. | Windows Server 2019 | آرگومان خط فرمان زیر را تنظیم کنید (با فرض نسخه {{< skew currentVersion >}}): ` --enable-dsr=true` |
| Preserve-Destination | از DNAT ترافیک سرویس صرف‌نظر می‌کند و در نتیجه IP مجازی سرویس هدف را در بسته‌هایی که به Pod پشتیبان می‌رسند حفظ می‌کند. همچنین ارسال نود به نود را غیرفعال می‌کند. | Windows Server, version 1903 | مقدار `"preserve-destination": "true"` را در annotationهای سرویس تنظیم کنید و DSR را در kube-proxy فعال کنید. |
| شبکه‌بندی دوپشته IPv4/IPv6 | ارتباطات بومی IPv4-به-IPv4 به‌موازات IPv6-به-IPv6 به سمت کلاستر، از آن و درون آن | Windows Server 2019 | [IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/#windows-support) را ببینید |
| حفظ IP کلاینت | تضمین می‌کند که IP مبدأ ترافیک ورودی (ingress) حفظ شود. همچنین ارسال نود به نود را غیرفعال می‌کند. |  Windows Server 2019  | مقدار `service.spec.externalTrafficPolicy` را روی "Local" تنظیم کنید و DSR را در kube-proxy فعال کنید |
{{< /table >}}

## محدودیت‌ها {#limitations}

قابلیت‌های شبکه‌ای زیر در نودهای ویندوز پشتیبانی _نمی‌شوند_:

* حالت شبکه‌بندی میزبان (Host networking mode)
* دسترسی محلی به NodePort از خود نود (برای نودهای دیگر یا کلاینت‌های خارجی کار می‌کند)
* بیش از ۶۴ پاد پشتیبان (یا آدرس مقصد یکتا) برای یک Service واحد
* ارتباط IPv6 بین پادهای ویندوز متصل به شبکه‌های overlay
* سیاست ترافیک محلی (Local Traffic Policy) در حالت غیر DSR
* ارتباط خروجی با استفاده از پروتکل ICMP از طریق `win-overlay`، `win-bridge` یا با استفاده از افزونه Azure-CNI.
  به‌طور مشخص، صفحه داده ویندوز ([VFP](https://www.microsoft.com/research/project/azure-virtual-filtering-platform/))
  از جابه‌جایی (transposition) بسته‌های ICMP پشتیبانی نمی‌کند، و این یعنی:
  * بسته‌های ICMP که به مقاصدی در همان شبکه هدایت می‌شوند (مانند ارتباط پاد به پاد از طریق ping)
    مطابق انتظار کار می‌کنند؛
  * بسته‌های TCP/UDP مطابق انتظار کار می‌کنند؛
  * بسته‌های ICMP که قرار است از یک شبکه راه دور عبور کنند (مثلاً ارتباط پاد با اینترنت خارجی از طریق ping)
    قابل جابه‌جایی نیستند و بنابراین به مبدأ خود بازگردانده نخواهند شد؛
  * از آنجا که بسته‌های TCP/UDP همچنان قابل جابه‌جایی هستند، هنگام اشکال‌یابی اتصال با دنیای بیرون
    می‌توانید `ping <destination>` را با `curl <destination>` جایگزین کنید.

سایر محدودیت‌ها:

* افزونه‌های شبکه مرجع ویندوز یعنی win-bridge و win-overlay به دلیل نبود پیاده‌سازی `CHECK`،
  [مشخصات CNI](https://github.com/containernetworking/cni/blob/master/SPEC.md) نسخه v0.4.0
  را پیاده‌سازی نمی‌کنند.
* افزونه CNI مربوط به Flannel VXLAN در ویندوز محدودیت‌های زیر را دارد:
  * اتصال نود به پاد تنها برای پادهای محلی و با Flannel نسخه v0.12.0 (یا بالاتر) امکان‌پذیر است.
  * Flannel به استفاده از VNI برابر 4096 و پورت UDP برابر 4789 محدود است. برای جزئیات بیشتر درباره این پارامترها،
    مستندات رسمی بک‌اند
    [Flannel VXLAN](https://github.com/coreos/flannel/blob/master/Documentation/backends.md#vxlan)
    را ببینید.
