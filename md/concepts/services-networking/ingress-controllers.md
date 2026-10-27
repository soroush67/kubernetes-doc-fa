---
title: کنترل‌کننده‌های Ingress
description: >-
  برای آنکه یک [Ingress](/docs/concepts/services-networking/ingress/) در کلاستر شما کار کند،
  باید یک _کنترل‌کنندهٔ ingress_ در حال اجرا باشد.
  شما باید دست‌کم یک کنترل‌کنندهٔ ingress انتخاب کنید و از راه‌اندازی آن در کلاستر خود اطمینان حاصل کنید.  
  این صفحه کنترل‌کننده‌های ingress رایجی را که می‌توانید مستقر کنید، فهرست می‌کند.
content_type: concept
weight: 50
---

{{< note >}}
پروژهٔ کوبرنتیز استفاده از [Gateway](https://gateway-api.sigs.k8s.io/) را به‌جای
[Ingress](/docs/concepts/services-networking/ingress/) توصیه می‌کند.
API مربوط به Ingress منجمد شده است.

این به آن معناست که:
* API مربوط به Ingress به‌طور عمومی در دسترس (GA) است و مشمول [تضمین‌های پایداری](/docs/reference/using-api/deprecation-policy/#deprecating-parts-of-the-api) مربوط به APIهای عمومی در دسترس است.
  پروژهٔ کوبرنتیز هیچ برنامه‌ای برای حذف Ingress از کوبرنتیز ندارد.
* API مربوط به Ingress دیگر توسعه داده نمی‌شود و هیچ تغییر
  یا به‌روزرسانی دیگری در آن اعمال نخواهد شد.
{{< /note >}}

<!-- body -->

<!-- overview -->


## کنترل‌کننده‌های Ingress

کوبرنتیز به‌عنوان یک پروژه، از کنترل‌کننده‌های ingress ‏[AWS](https://github.com/kubernetes-sigs/aws-load-balancer-controller#readme) و [GCE](https://git.k8s.io/ingress-gce/README.md#readme) پشتیبانی و آن‌ها را نگهداری می‌کند.



## کنترل‌کننده‌های ingress شخص ثالث

{{% thirdparty-content %}}

* [AKS Application Gateway Ingress Controller](https://docs.microsoft.com/azure/application-gateway/tutorial-ingress-controller-add-on-existing?toc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Faks%2Ftoc.json&bc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fbread%2Ftoc.json) یک کنترل‌کنندهٔ ingress است که [Azure Application Gateway](https://docs.microsoft.com/azure/application-gateway/overview) را پیکربندی می‌کند.
* [Alibaba Cloud API Gateway Ingress](https://www.alibabacloud.com/help/en/api-gateway/cloud-native-api-gateway/user-guide/ingress-managementapig-ngress-management) یک کنترل‌کنندهٔ ingress است که [Alibaba Cloud Native API Gateway](https://www.alibabacloud.com/help/en/api-gateway/cloud-native-api-gateway/product-overview/what-is-cloud-native-api-gateway) را پیکربندی می‌کند؛ این محصول نسخهٔ تجاری [Higress](https://github.com/alibaba/higress) نیز هست.
* [کنترل‌کنندهٔ ingress ‏Apache APISIX](https://github.com/apache/apisix-ingress-controller) یک کنترل‌کنندهٔ ingress مبتنی بر [Apache APISIX](https://github.com/apache/apisix) است.
* [Avi Kubernetes Operator](https://github.com/vmware/load-balancer-and-ingress-services-for-kubernetes) با استفاده از [VMware NSX Advanced Load Balancer](https://avinetworks.com/) توزیع بار در لایه‌های L4 تا L7 را فراهم می‌کند.
* [BFE Ingress Controller](https://github.com/bfenetworks/ingress-bfe) یک کنترل‌کنندهٔ ingress مبتنی بر [BFE](https://www.bfe-networks.net) است.
* [BunkerWeb Ingress Controller](https://docs.bunkerweb.io/latest/integrations/#kubernetes) یک کنترل‌کنندهٔ ingress برای [BunkerWeb](https://www.bunkerweb.io/) است که یک WAF (دیوارهٔ آتش برنامهٔ وب) مبتنی بر nginx است.
* [Cilium Ingress Controller](https://docs.cilium.io/en/stable/network/servicemesh/ingress/) یک کنترل‌کنندهٔ ingress است که بر پایهٔ [Cilium](https://cilium.io/) کار می‌کند.
* [کنترل‌کنندهٔ ingress ‏Citrix](https://github.com/citrix/citrix-k8s-ingress-controller#readme) با
  Citrix Application Delivery Controller کار می‌کند.
* [Contour](https://projectcontour.io/) یک کنترل‌کنندهٔ ingress مبتنی بر [Envoy](https://www.envoyproxy.io/) است.
* [Emissary-Ingress](https://www.getambassador.io/products/api-gateway) API Gateway یک کنترل‌کنندهٔ ingress مبتنی بر [Envoy](https://www.envoyproxy.io)
  است.
* [EnRoute](https://getenroute.io/) یک API gateway مبتنی بر [Envoy](https://www.envoyproxy.io) است که می‌تواند به‌عنوان کنترل‌کنندهٔ ingress اجرا شود.
* F5 BIG-IP [Container Ingress Services for Kubernetes](https://clouddocs.f5.com/containers/latest/userguide/kubernetes/)
  به شما امکان می‌دهد با استفاده از یک Ingress، سرورهای مجازی F5 BIG-IP را پیکربندی کنید.
* [FortiADC Ingress Controller](https://docs.fortinet.com/document/fortiadc/7.0.0/fortiadc-ingress-controller/742835/fortiadc-ingress-controller-overview) از منابع Ingress کوبرنتیز پشتیبانی می‌کند و به شما امکان می‌دهد آبجکت‌های FortiADC را از درون کوبرنتیز مدیریت کنید
* [Gloo](https://gloo.solo.io) یک کنترل‌کنندهٔ ingress متن‌باز مبتنی بر [Envoy](https://www.envoyproxy.io) است
  که قابلیت‌های API gateway را ارائه می‌کند.
* [Higress](https://github.com/alibaba/higress) یک API gateway مبتنی بر [Envoy](https://www.envoyproxy.io) است که می‌تواند به‌عنوان کنترل‌کنندهٔ ingress اجرا شود.
* [HAProxy Ingress Controller for Kubernetes](https://github.com/haproxytech/kubernetes-ingress#readme)
  یک کنترل‌کنندهٔ ingress برای [HAProxy](https://www.haproxy.org/#desc) است.
* [Istio Ingress](https://istio.io/latest/docs/tasks/traffic-management/ingress/kubernetes-ingress/)
  یک کنترل‌کنندهٔ ingress مبتنی بر [Istio](https://istio.io/) است.
* [Kong Ingress Controller for Kubernetes](https://github.com/Kong/kubernetes-ingress-controller#readme)
  یک کنترل‌کنندهٔ ingress است که [Kong Gateway](https://konghq.com/kong/) را هدایت می‌کند.
* [Kusk Gateway](https://kusk.kubeshop.io/) یک کنترل‌کنندهٔ ingress مبتنی بر OpenAPI است که بر پایهٔ [Envoy](https://www.envoyproxy.io) ساخته شده است.
* [N42 Gateway](https://n42-gateway.github.io/) یک کنترل‌کنندهٔ Ingress و Gateway API برای [HAProxy](https://www.haproxy.org/#desc) است.
* [NGINX Ingress Controller for Kubernetes](https://www.nginx.com/products/nginx-ingress-controller/)
  با وب‌سرور [NGINX](https://www.nginx.com/resources/glossary/nginx/) (به‌عنوان پراکسی) کار می‌کند.
* [ngrok-operator](https://github.com/ngrok/ngrok-operator) یک کنترل‌کننده برای [ngrok](https://ngrok.com/) است که از هر دو API ‏Ingress و Gateway برای افزودن دسترسی عمومی امن به Serviceهای K8s شما پشتیبانی می‌کند.
* [OCI Native Ingress Controller](https://github.com/oracle/oci-native-ingress-controller#readme) یک کنترل‌کنندهٔ Ingress برای Oracle Cloud Infrastructure است که به شما امکان می‌دهد [OCI Load Balancer](https://docs.oracle.com/en-us/iaas/Content/Balance/home.htm) را مدیریت کنید.
* [OpenNJet Ingress Controller](https://gitee.com/njet-rd/open-njet-kic) یک کنترل‌کنندهٔ ingress مبتنی بر [OpenNJet](https://njet.org.cn/) است.
* [Pomerium Ingress Controller](https://www.pomerium.com/docs/k8s/ingress.html) مبتنی بر [Pomerium](https://pomerium.com/) است که سیاست دسترسی آگاه از زمینه (context-aware) ارائه می‌کند.
* [Skipper](https://opensource.zalando.com/skipper/kubernetes/ingress-controller/) یک مسیریاب HTTP و reverse proxy برای ترکیب سرویس‌ها، از جمله موارد استفاده‌ای مانند Ingress کوبرنتیز، است که به‌صورت یک کتابخانه برای ساخت پراکسی سفارشی شما طراحی شده است.
* [Traefik Kubernetes Ingress provider](https://doc.traefik.io/traefik/providers/kubernetes-ingress/) یک
  کنترل‌کنندهٔ ingress برای پراکسی [Traefik](https://traefik.io/traefik/) است.
* [Tyk Operator](https://github.com/TykTechnologies/tyk-operator) با استفاده از منابع سفارشی، Ingress را گسترش می‌دهد تا قابلیت‌های مدیریت API را به Ingress بیاورد. Tyk Operator با Tyk Gateway متن‌باز و control plane ‏Tyk Cloud کار می‌کند.
* [Voyager](https://voyagermesh.com) یک کنترل‌کنندهٔ ingress برای
  [HAProxy](https://www.haproxy.org/#desc) است.
* [Wallarm Ingress Controller](https://www.wallarm.com/solutions/waf-for-kubernetes) یک کنترل‌کنندهٔ Ingress است که قابلیت‌های WAAP (WAF) و امنیت API را فراهم می‌کند.

## استفاده از چند کنترل‌کنندهٔ Ingress

می‌توانید هر تعداد کنترل‌کنندهٔ ingress را با استفاده از [ingress class](/docs/concepts/services-networking/ingress/#ingress-class)
درون یک کلاستر مستقر کنید. به `.metadata.name` منبع ingress class خود توجه کنید. هنگام ایجاد یک ingress، برای تعیین فیلد `ingressClassName` روی آبجکت Ingress خود به آن نام نیاز خواهید داشت (به [مرجع IngressSpec v1](/docs/reference/kubernetes-api/service-resources/ingress-v1/#IngressSpec) مراجعه کنید). `ingressClassName` جایگزین [روش قدیمی‌تر حاشیه‌نویسی](/docs/concepts/services-networking/ingress/#deprecated-annotation) است.

اگر برای یک Ingress هیچ IngressClassای تعیین نکنید و کلاستر شما دقیقاً یک IngressClass داشته باشد که به‌عنوان پیش‌فرض علامت‌گذاری شده است، کوبرنتیز IngressClass پیش‌فرض کلاستر را بر Ingress [اعمال می‌کند](/docs/concepts/services-networking/ingress/#default-ingress-class).
برای علامت‌گذاری یک IngressClass به‌عنوان پیش‌فرض، [حاشیه‌نویسی `ingressclass.kubernetes.io/is-default-class`](/docs/reference/labels-annotations-taints/#ingressclass-kubernetes-io-is-default-class) را با مقدار رشته‌ای `"true"` روی آن IngressClass تنظیم می‌کنید.

در حالت ایدئال، همهٔ کنترل‌کننده‌های ingress باید این مشخصات را برآورده کنند، اما کنترل‌کننده‌های ingress
مختلف اندکی متفاوت عمل می‌کنند.

{{< note >}}
حتماً مستندات کنترل‌کنندهٔ ingress خود را مرور کنید تا از نکات احتیاطی انتخاب آن آگاه شوید.
{{< /note >}}



## {{% heading "whatsnext" %}}


* دربارهٔ [Ingress](/docs/concepts/services-networking/ingress/) بیشتر بیاموزید.
