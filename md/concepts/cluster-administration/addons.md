---
title: نصب افزونه‌ها
content_type: concept
weight: 150
---

<!-- overview -->

{{% thirdparty-content %}}

افزونه‌ها (Add-ons) قابلیت‌های کوبرنتیز را گسترش می‌دهند.

این صفحه برخی از افزونه‌های موجود را فهرست می‌کند و به دستورالعمل‌های نصب هر یک
پیوند می‌دهد. این فهرست قصد ندارد جامع باشد.

<!-- body -->

## شبکه و سیاست شبکه

* [ACI](https://www.github.com/noironetworks/aci-containers) شبکهٔ یکپارچهٔ
  کانتینر و امنیت شبکه را با Cisco ACI فراهم می‌کند.
* [Antrea](https://antrea.io/) در لایهٔ ۳/۴ عمل می‌کند تا سرویس‌های شبکه و
  امنیت را برای کوبرنتیز فراهم کند و از Open vSwitch به‌عنوان صفحهٔ دادهٔ
  شبکه بهره می‌گیرد. Antrea یک [پروژهٔ CNCF در سطح Sandbox](https://www.cncf.io/projects/antrea/) است.
* [Calico](https://www.tigera.io/project-calico/) یک ارائه‌دهندهٔ شبکه و سیاست
  شبکه است. Calico از مجموعه‌ای انعطاف‌پذیر از گزینه‌های شبکه پشتیبانی می‌کند تا بتوانید
  کارآمدترین گزینه را برای وضعیت خود برگزینید، از جمله شبکه‌های غیر overlay
  و overlay، با BGP یا بدون آن. Calico از یک موتور یکسان برای
  اعمال سیاست شبکه برای میزبان‌ها، پادها و (در صورت استفاده از Istio و Envoy)
  برنامه‌ها در لایهٔ service mesh استفاده می‌کند.
* [Canal](https://projectcalico.docs.tigera.io/getting-started/kubernetes/flannel/flannel)
  Flannel و Calico را با هم ترکیب می‌کند و شبکه و سیاست شبکه را فراهم می‌آورد.
* [Cilium](https://github.com/cilium/cilium) یک راهکار شبکه، مشاهده‌پذیری
  و امنیت با صفحهٔ دادهٔ مبتنی بر eBPF است. Cilium یک
  شبکهٔ سادهٔ تخت در لایهٔ ۳ فراهم می‌کند که می‌تواند چندین کلاستر را
  در حالت مسیریابی بومی یا حالت overlay/کپسوله‌سازی در بر بگیرد و می‌تواند
  سیاست‌های شبکه را در لایه‌های L3 تا L7 با استفاده از یک مدل امنیتی مبتنی بر هویت که
  از نشانی‌دهی شبکه مستقل است اعمال کند. Cilium می‌تواند جایگزینی برای
  kube-proxy باشد؛ همچنین قابلیت‌های اضافی و اختیاری مشاهده‌پذیری و امنیت ارائه می‌دهد.
  Cilium یک [پروژهٔ CNCF در سطح Graduated](https://www.cncf.io/projects/cilium/) است.
* [CNI-Genie](https://github.com/cni-genie/CNI-Genie) به کوبرنتیز امکان می‌دهد به‌طور یکپارچه
  به یکی از افزونه‌های CNI دلخواه، مانند Calico، Canal، Flannel یا Weave متصل شود.
  CNI-Genie یک [پروژهٔ CNCF در سطح Sandbox](https://www.cncf.io/projects/cni-genie/) است.
* [Contiv](https://contivpp.io/) شبکه‌ای قابل‌پیکربندی (L3 بومی با استفاده از BGP،
  overlay با استفاده از vxlan، L2 کلاسیک و Cisco-SDN/ACI) برای موارد کاربرد گوناگون و یک
  چارچوب سیاست غنی فراهم می‌کند. پروژهٔ Contiv به‌طور کامل [متن‌باز](https://github.com/contiv) است.
  [نصب‌کنندهٔ](https://github.com/contiv/install) آن هر دو گزینهٔ نصب مبتنی بر kubeadm و
  غیر مبتنی بر kubeadm را ارائه می‌دهد.
* [Contrail](https://www.juniper.net/us/en/products-services/sdn/contrail/contrail-networking/)،
  که بر پایهٔ [Tungsten Fabric](https://tungsten.io) ساخته شده، یک سکوی متن‌باز و چندابری
  برای مجازی‌سازی شبکه و مدیریت سیاست است. Contrail و Tungsten
  Fabric با سیستم‌های هماهنگ‌سازی (orchestration) مانند Kubernetes، OpenShift،
  OpenStack و Mesos یکپارچه شده‌اند و حالت‌های جداسازی را برای ماشین‌های مجازی، کانتینرها/پادها
  و بارهای کاری bare metal فراهم می‌کنند.
* [Flannel](https://github.com/flannel-io/flannel#deploying-flannel-manually)
  یک ارائه‌دهندهٔ شبکهٔ overlay است که می‌توان آن را با کوبرنتیز استفاده کرد.
* [Gateway API](/docs/concepts/services-networking/gateway/) یک پروژهٔ متن‌باز است که توسط
  جامعهٔ [SIG Network](https://github.com/kubernetes/community/tree/main/sig-network) مدیریت می‌شود و
  یک API رسا، توسعه‌پذیر و نقش‌محور برای مدل‌سازی شبکهٔ سرویس‌ها فراهم می‌کند.
* [Knitter](https://github.com/ZTE/Knitter/) افزونه‌ای برای پشتیبانی از چندین رابط
  شبکه در یک پاد کوبرنتیز است.
* [kube-router](https://github.com/cloudnativelabs/kube-router) یک راهکار
  متن‌باز و آماده‌به‌کار برای شبکهٔ کوبرنتیز است که هدف آن فراهم‌کردن
  سادگی عملیاتی و کارایی بالاست. این راهکار از API کوبرنتیز،
  BGP و Golang برای مسیر کنترل و از سازه‌های پایه‌ای شبکهٔ لینوکس (IPVS،
  nftables و غیره) برای مسیر داده بهره می‌گیرد. kube-router جایگزینی کم‌سربار ارائه می‌دهد و
  در هر دو k0s و k3s استفاده می‌شود.
* [Multus](https://github.com/k8snetworkplumbingwg/multus-cni) یک افزونهٔ چندگانه برای
  پشتیبانی از چند شبکه در کوبرنتیز است که از همهٔ افزونه‌های CNI
  (مانند Calico، Cilium، Contiv و Flannel) و افزون بر آن از بارهای کاری مبتنی بر SRIOV، DPDK، OVS-DPDK و
  VPP در کوبرنتیز پشتیبانی می‌کند.
* [OVN-Kubernetes](https://github.com/ovn-org/ovn-kubernetes/) یک ارائه‌دهندهٔ
  شبکه برای کوبرنتیز است که بر پایهٔ [OVN (Open Virtual Network)](https://github.com/ovn-org/ovn/) ساخته شده؛
  OVN یک پیاده‌سازی شبکهٔ مجازی است که از پروژهٔ Open vSwitch (OVS) برآمده است.
  OVN-Kubernetes یک پیاده‌سازی شبکهٔ مبتنی بر overlay برای کوبرنتیز فراهم می‌کند
  که شامل پیاده‌سازی مبتنی بر OVS برای متعادل‌سازی بار و سیاست شبکه است.
* [Nodus](https://github.com/akraino-edge-stack/icn-nodus) یک افزونهٔ کنترل‌کنندهٔ
  CNI مبتنی بر OVN است که زنجیره‌سازی توابع سرویس (SFC) مبتنی بر رویکرد بومی‌ابری را فراهم می‌کند.
* افزونهٔ کانتینر (NCP) [NSX-T](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/index.html)
  یکپارچگی میان VMware NSX-T و هماهنگ‌سازهای کانتینر مانند
  کوبرنتیز، و همچنین یکپارچگی میان NSX-T و سکوهای CaaS/PaaS مبتنی بر کانتینر
  مانند Pivotal Container Service (PKS) و OpenShift را فراهم می‌کند.
* [Nuage](https://github.com/nuagenetworks/nuage-kubernetes/blob/v5.1.1-1/docs/kubernetes-1-installation.rst)
  یک سکوی SDN است که شبکه‌ای مبتنی بر سیاست میان Podهای کوبرنتیز
  و محیط‌های غیرکوبرنتیزی، همراه با قابلیت مشاهده و پایش امنیتی، فراهم می‌کند.
* [Romana](https://github.com/romana) یک راهکار شبکه در لایهٔ ۳ برای شبکه‌های
  پاد است که از API مربوط به [NetworkPolicy](/docs/concepts/services-networking/network-policies/) نیز پشتیبانی می‌کند.
* [Spiderpool](https://github.com/spidernet-io/spiderpool) یک راهکار شبکهٔ underlay و RDMA
  برای کوبرنتیز است. Spiderpool روی bare metal، ماشین‌های مجازی
  و محیط‌های ابر عمومی پشتیبانی می‌شود.
* [Terway](https://github.com/AliyunContainerService/terway/) مجموعه‌ای از افزونه‌های CNI
  مبتنی بر محصولات شبکهٔ VPC و ECS شرکت AlibabaCloud است. این مجموعه شبکهٔ بومی VPC
  و سیاست‌های شبکه را در محیط‌های AlibabaCloud فراهم می‌کند.
* [Weave Net](https://github.com/rajch/weave#using-weave-on-kubernetes)
  شبکه و سیاست شبکه را فراهم می‌کند، در هر دو سوی یک گسست شبکه (network partition)
  به کار خود ادامه می‌دهد و به پایگاه دادهٔ خارجی نیاز ندارد.

## کشف سرویس

* [CoreDNS](https://coredns.io) یک سرور DNS انعطاف‌پذیر و توسعه‌پذیر است که می‌توان آن را
  به‌عنوان DNS درون‌کلاستری برای پادها [نصب کرد](https://github.com/coredns/helm).

## مصورسازی و کنترل

* [Dashboard](https://github.com/kubernetes/dashboard#kubernetes-dashboard)
  یک رابط وب داشبورد برای کوبرنتیز است.
* [Headlamp](https://headlamp.dev/) یک رابط کاربری توسعه‌پذیر برای کوبرنتیز است که می‌توان آن را
  درون کلاستر مستقر کرد یا به‌عنوان یک برنامهٔ رومیزی استفاده کرد.

## زیرساخت

* [KubeVirt](https://kubevirt.io/user-guide/#/installation/installation) افزونه‌ای
  برای اجرای ماشین‌های مجازی روی کوبرنتیز است. معمولاً روی کلاسترهای bare-metal اجرا می‌شود.
* [آشکارساز مشکلات نود](https://github.com/kubernetes/node-problem-detector)
  (node problem detector)
  روی نودهای لینوکسی اجرا می‌شود و مشکلات سیستمی را به‌صورت
  [Event](/docs/reference/kubernetes-api/cluster-resources/event-v1/) یا
  [شرایط نود](/docs/concepts/architecture/nodes/#condition) گزارش می‌دهد.

## ابزارگذاری (Instrumentation)

* [kube-state-metrics](/docs/concepts/cluster-administration/kube-state-metrics)

## افزونه‌های قدیمی

چندین افزونهٔ دیگر در پوشهٔ منسوخ‌شدهٔ
[cluster/addons](https://git.k8s.io/kubernetes/cluster/addons) مستند شده‌اند.

افزونه‌هایی که به‌خوبی نگه‌داری می‌شوند باید از اینجا پیوند داده شوند. از PRها استقبال می‌کنیم!
