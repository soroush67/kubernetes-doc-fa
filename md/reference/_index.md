---
title: مرجع
approvers:
- chenopis
linkTitle: "مرجع"
main_menu: true
weight: 70
content_type: concept
no_list: true
---

<!-- overview -->

این بخش از مستندات کوبرنتیز شامل مراجع است.

<!-- body -->

## مرجع API

* [واژه‌نامه](/docs/reference/glossary/) - فهرستی جامع و استاندارد از اصطلاحات کوبرنتیز

* [مرجع API کوبرنتیز](/docs/reference/kubernetes-api/)
* [مرجع تک‌صفحه‌ای API برای کوبرنتیز {{< param "version" >}}](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/)
* [استفاده از API کوبرنتیز](/docs/reference/using-api/) - مروری بر API کوبرنتیز.
* [کنترل دسترسی به API](/docs/reference/access-authn-authz/) - جزئیات نحوهٔ کنترل دسترسی به API در کوبرنتیز
* [برچسب‌ها، حاشیه‌نویسی‌ها و Taintهای شناخته‌شده](/docs/reference/labels-annotations-taints/)

## کتابخانه‌های کلاینت با پشتیبانی رسمی

برای فراخوانی API کوبرنتیز از یک زبان برنامه‌نویسی می‌توانید از
[کتابخانه‌های کلاینت](/docs/reference/using-api/client-libraries/) استفاده کنید. کتابخانه‌های کلاینت با پشتیبانی رسمی عبارت‌اند از:

- [کتابخانه کلاینت Go برای کوبرنتیز](https://github.com/kubernetes/client-go/)
- [کتابخانه کلاینت Python برای کوبرنتیز](https://github.com/kubernetes-client/python)
- [کتابخانه کلاینت Java برای کوبرنتیز](https://github.com/kubernetes-client/java)
- [کتابخانه کلاینت JavaScript برای کوبرنتیز](https://github.com/kubernetes-client/javascript)
- [کتابخانه کلاینت C# برای کوبرنتیز](https://github.com/kubernetes-client/csharp)
- [کتابخانه کلاینت Haskell برای کوبرنتیز](https://github.com/kubernetes-client/haskell)

## CLI

* [kubectl](/docs/reference/kubectl/) - ابزار اصلی خط فرمان برای اجرای دستورات و مدیریت کلاسترهای کوبرنتیز.
  * [JSONPath](/docs/reference/kubectl/jsonpath/) - راهنمای نحو برای استفاده از [عبارات JSONPath](https://goessner.net/articles/JsonPath/) در kubectl.
* [kubeadm](/docs/reference/setup-tools/kubeadm/) - ابزار خط فرمان برای راه‌اندازی آسان یک کلاستر امن کوبرنتیز.

## مؤلفه‌ها

* [kubelet](/docs/reference/command-line-tools-reference/kubelet/) - عامل
  اصلی که روی هر نود اجرا می‌شود. kubelet مجموعه‌ای از PodSpecها را دریافت می‌کند
  و اطمینان می‌دهد کانتینرهای توصیف‌شده در آن‌ها در حال اجرا و سالم هستند.
* [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/) -
  یک REST API که داده‌های آبجکت‌های API مانند Podها،
  Serviceها و replication controllerها را اعتبارسنجی و پیکربندی می‌کند.
* [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/) -
  دیمنی که حلقه‌های کنترلی اصلی همراه با کوبرنتیز را در خود جای داده است.
* [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/) - می‌تواند
  هدایت ساده جریان TCP/UDP یا هدایت round-robin ترافیک TCP/UDP را میان
  مجموعه‌ای از بک‌اندها انجام دهد.
* [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/) -
  زمان‌بندی که دسترس‌پذیری، کارایی و ظرفیت را مدیریت می‌کند.
  
  * [سیاست‌های زمان‌بند](/docs/reference/scheduling/policies)
  * [پروفایل‌های زمان‌بند](/docs/reference/scheduling/config#profiles)

* فهرست [پورت‌ها و پروتکل‌ها](/docs/reference/networking/ports-and-protocols/) که
  باید روی نودهای control plane و worker باز باشند

## APIهای پیکربندی

این بخش مستندات APIهای «منتشرنشده» را در خود جای داده است که برای
پیکربندی مؤلفه‌ها یا ابزارهای کوبرنتیز به کار می‌روند. بیشتر این APIها
از طریق API server به شیوهٔ RESTful ارائه نمی‌شوند، با این حال برای
استفاده یا مدیریت یک کلاستر توسط کاربر یا اپراتور ضروری هستند.


* [kubeconfig (v1)](/docs/reference/config-api/kubeconfig.v1/)
* [kuberc (v1alpha1)](/docs/reference/config-api/kuberc.v1alpha1/) و
  [kuberc (v1beta1)](/docs/reference/config-api/kuberc.v1beta1/)
* [پذیرش (admission) در kube-apiserver (v1)](/docs/reference/config-api/apiserver-admission.v1/)
  - `admission.k8s.io/v1`
    - [AdmissionReview](/docs/reference/config-api/apiserver-admission.v1/#admission-k8s-io-v1-AdmissionReview)
* [پیکربندی kube-apiserver (v1alpha1)](/docs/reference/config-api/apiserver-config.v1alpha1/) و
  - `apiserver.k8s.io/v1`
    - [AdmissionConfiguration](/docs/reference/config-api/apiserver-config.v1alpha1/#apiserver-k8s-io-v1alpha1-AdmissionConfiguration)
    - [AuthenticationConfiguration](/docs/reference/config-api/apiserver-config.v1alpha1/#apiserver-k8s-io-v1alpha1-AuthenticationConfiguration)
    - [AuthorizationConfiguration](/docs/reference/config-api/apiserver-config.v1alpha1/#apiserver-k8s-io-v1alpha1-AuthorizationConfiguration)
    - [EgressSelectorConfiguration](/docs/reference/config-api/apiserver-config.v1alpha1/#apiserver-k8s-io-v1alpha1-EgressSelectorConfiguration)
    - [TracingConfiguration](/docs/reference/config-api/apiserver-config.v1alpha1/#apiserver-k8s-io-v1alpha1-TracingConfiguration)
 
* [پیکربندی kube-apiserver (v1beta1)](/docs/reference/config-api/apiserver-config.v1beta1/)
  - `apiserver.k8s.io/v1beta1`
    - [AuthenticationConfiguration](/docs/reference/config-api/apiserver-config.v1beta1/#apiserver-k8s-io-v1beta1-AuthenticationConfiguration)
    - [AuthorizationConfiguration](/docs/reference/config-api/apiserver-config.v1beta1/#apiserver-k8s-io-v1beta1-AuthorizationConfiguration)
    - [EgressSelectorConfiguration](/docs/reference/config-api/apiserver-config.v1beta1/#apiserver-k8s-io-v1beta1-EgressSelectorConfiguration)
    - [TracingConfiguration](/docs/reference/config-api/apiserver-config.v1beta1/#apiserver-k8s-io-v1beta1-TracingConfiguration)
 
* [پیکربندی kube-apiserver (v1)](/docs/reference/config-api/apiserver-config.v1/)
  - `apiserver.config.k8s.io/v1`
    - [AdmissionConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-config-k8s-io-v1-AdmissionConfiguration)
    - [AuthenticationConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-config-k8s-io-v1-AuthenticationConfiguration)
    - [AuthorizationConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-config-k8s-io-v1-AuthorizationConfiguration)
    - [EncryptionConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-config-k8s-io-v1-EncryptionConfiguration)
    - [TracingConfiguration](/docs/reference/config-api/apiserver-config.v1/#apiserver-config-k8s-io-v1-TracingConfiguration)
* [محدودیت نرخ رویداد در kube-apiserver (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)
  - `eventratelimit.admission.k8s.io/v1alpha1`
    - [Configuration](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/#eventratelimit-admission-k8s-io-v1alpha1-Configuration)
* [پیکربندی kubelet (v1alpha1)](/docs/reference/config-api/kubelet-config.v1alpha1/)
  - `kubelet.config.k8s.io/v1alpha1`
    - [CredentialProviderConfig](/docs/reference/config-api/kubelet-config.v1alpha1/#kubelet-config-k8s-io-v1alpha1-CredentialProviderConfig)
    - [ImagePullIntent](/docs/reference/config-api/kubelet-config.v1alpha1/#kubelet-config-k8s-io-v1alpha1-ImagePullIntent)
    - [ImagePulledRecord](/docs/reference/config-api/kubelet-config.v1alpha1/#kubelet-config-k8s-io-v1alpha1-ImagePulledRecord)
* [پیکربندی kubelet (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/)
  - `kubelet.config.k8s.io/v1beta1`
    - [CredentialProviderConfig](/docs/reference/config-api/kubelet-config.v1beta1/#kubelet-config-k8s-io-v1beta1-CredentialProviderConfig)
    - [KubeletConfiguration](/docs/reference/config-api/kubelet-config.v1beta1/#kubelet-config-k8s-io-v1beta1-KubeletConfiguration)
    - [SerializedNodeConfigSource](/docs/reference/config-api/kubelet-config.v1beta1/#kubelet-config-k8s-io-v1beta1-SerializedNodeConfigSource)
* [پیکربندی kubelet (v1)](/docs/reference/config-api/kubelet-config.v1/)
  - `kubelet.config.k8s.io/v1`
    - [CredentialProviderConfig](/docs/reference/config-api/kubelet-config.v1/#kubelet-config-k8s-io-v1-CredentialProviderConfig)
* [ارائه‌دهندگان اعتبارنامه kubelet (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/)
  - `credentialprovider.kubelet.k8s.io/v1`
    - [CredentialProviderRequest](/docs/reference/config-api/kubelet-credentialprovider.v1/#credentialprovider-kubelet-k8s-io-v1-CredentialProviderRequest)
    - [CredentialProviderResponse](/docs/reference/config-api/kubelet-credentialprovider.v1/#credentialprovider-kubelet-k8s-io-v1-CredentialProviderResponse)
* [پیکربندی kube-scheduler (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
  - `kubescheduler.config.k8s.io/v1`
    - [DefaultPreemptionArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-DefaultPreemptionArgs)
    - [DynamicResourcesArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-DynamicResourcesArgs)
    - [InterPodAffinityArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-InterPodAffinityArgs)
    - [KubeSchedulerConfiguration](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-KubeSchedulerConfiguration)
    - [NodeAffinityArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeAffinityArgs)
    - [NodeResourcesBalancedAllocationArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeResourcesBalancedAllocationArgs)
    - [NodeResourcesFitArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-NodeResourcesFitArgs)
    - [PodTopologySpreadArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-PodTopologySpreadArgs)
    - [VolumeBindingArgs](/docs/reference/config-api/kube-scheduler-config.v1/#kubescheduler-config-k8s-io-v1-VolumeBindingArgs)
* [پیکربندی kube-controller-manager (v1alpha1)](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)
  - `kubecontrollermanager.config.k8s.io/v1alpha1`
    - [LeaderMigrationConfiguration](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/#controllermanager-config-k8s-io-v1alpha1-LeaderMigrationConfiguration)
    - [KubeControllerManagerConfiguration](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/#kubecontrollermanager-config-k8s-io-v1alpha1-KubeControllerManagerConfiguration)
  - `cloudcontrollermanager.config.k8s.io/v1alpha1`
    - [CloudControllerManagerConfiguration](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/#cloudcontrollermanager-config-k8s-io-v1alpha1-CloudControllerManagerConfiguration)
* [پیکربندی kube-proxy (v1alpha1)](/docs/reference/config-api/kube-proxy-config.v1alpha1/)
  - `kubeproxy.config.k8s.io/v1alpha1`
    - [KubeProxyConfiguration](/docs/reference/config-api/kube-proxy-config.v1alpha1/#kubeproxy-config-k8s-io-v1alpha1-KubeProxyConfiguration)
* [API مربوط به `audit.k8s.io/v1`](/docs/reference/config-api/apiserver-audit.v1/)
  - `audit.k8s.io/v1`
    - [Event](/docs/reference/config-api/apiserver-audit.v1/#audit-k8s-io-v1-Event)
    - [EventList](/docs/reference/config-api/apiserver-audit.v1/#audit-k8s-io-v1-EventList)
    - [Policy](/docs/reference/config-api/apiserver-audit.v1/#audit-k8s-io-v1-Policy)
    - [PolicyList](/docs/reference/config-api/apiserver-audit.v1/#audit-k8s-io-v1-PolicyList)
* [API احراز هویت کلاینت (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/)
  - `client.authentication.k8s.io/v1beta1`
     - [ExecCredential](/docs/reference/config-api/client-authentication.v1beta1/#client-authentication-k8s-io-v1beta1-ExecCredential)
* [API احراز هویت کلاینت (v1)](/docs/reference/config-api/client-authentication.v1/)
  - `client.authentication.k8s.io/v1`
     - [ExecCredential](/docs/reference/config-api/client-authentication.v1/#client-authentication-k8s-io-v1-ExecCredential)
* [پیکربندی WebhookAdmission (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/)
  - `apiserver.config.k8s.io/v1`
    - [WebhookAdmission](/docs/reference/config-api/apiserver-webhookadmission.v1/#apiserver-config-k8s-io-v1-WebhookAdmission)
* [API مربوط به ImagePolicy (v1alpha1)](/docs/reference/config-api/imagepolicy.v1alpha1/)
  - `imagepolicy.k8s.io/v1alpha1`
    - [ImageReview](/docs/reference/config-api/imagepolicy.v1alpha1/#imagepolicy-k8s-io-v1alpha1-ImageReview)

## API پیکربندی برای kubeadm

* [v1beta3](/docs/reference/config-api/kubeadm-config.v1beta3/)
* [v1beta4](/docs/reference/config-api/kubeadm-config.v1beta4/)

## APIهای خارجی

این‌ها APIهایی هستند که توسط پروژه کوبرنتیز تعریف شده‌اند، اما
توسط پروژه اصلی پیاده‌سازی نمی‌شوند:

* [Metrics API (v1beta1)](/docs/reference/external-api/metrics.v1beta1/)
* [Custom Metrics API (v1beta2)](/docs/reference/external-api/custom-metrics.v1beta2)
* [External Metrics API (v1beta1)](/docs/reference/external-api/external-metrics.v1beta1)

## مستندات طراحی

آرشیوی از مستندات طراحی قابلیت‌های کوبرنتیز. نقاط شروع مناسب
[معماری کوبرنتیز](https://git.k8s.io/design-proposals-archive/architecture/architecture.md) و
[مروری بر طراحی کوبرنتیز](https://git.k8s.io/design-proposals-archive) هستند.

## کدگذاری‌ها

ابزارهایی مانند {{< glossary_tooltip text="kubectl" term_id="kubectl" >}}
می‌توانند با قالب‌ها / کدگذاری‌های مختلف کار کنند. این موارد عبارت‌اند از:

* [CBOR](https://cbor.io/)، که روی شبکه استفاده می‌شود اما به‌عنوان قالب خروجی kubectl **در دسترس نیست**
  * بخش [کدگذاری CBOR برای منابع](/docs/reference/using-api/api-concepts/#cbor-encoding) را ببینید
* [JSON](https://www.json.org/)، که به‌عنوان قالب خروجی `kubectl` در دسترس است و در لایهٔ HTTP نیز استفاده می‌شود
* [KYAML](/docs/reference/encodings/kyaml)، گویشی از YAML مختص کوبرنتیز
  * KYAML در اصل یک _قالب خروجی_ است؛ در هر جایی که می‌توانید KYAML را به کوبرنتیز بدهید، می‌توانید هر ورودی معتبر YAML دیگری را نیز ارائه کنید
* [YAML](https://yaml.org/)، که به‌عنوان قالب خروجی `kubectl` در دسترس است و در لایهٔ HTTP نیز استفاده می‌شود

کوبرنتیز همچنین یک [کدگذاری protobuf](/docs/reference/using-api/api-concepts/#protobuf-encoding) اختصاصی دارد که فقط در پیام‌های HTTP استفاده می‌شود.

ابزار `kubectl` از برخی قالب‌های خروجی دیگر مانند _custom columns_ پشتیبانی می‌کند؛
بخش [قالب‌های خروجی](/docs/reference/kubectl/#output-options) را در مرجع kubectl ببینید.
