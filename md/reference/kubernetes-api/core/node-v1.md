---
api_metadata:
  apiVersion: "v1"
  import: "k8s.io/api/core/v1"
  kind: "Node"
content_type: "api_reference"
description: "Node یک نود کاری در کوبرنتیز است. هر نود یک شناسه یکتا در کش (یعنی در etcd) دارد."
title: "Node"
weight: 70
auto_generated: true
---

<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`apiVersion: v1`

`import "k8s.io/api/core/v1"`


## Node {#Node}

Node یک نود کاری در کوبرنتیز است. هر نود یک شناسه یکتا در کش (یعنی در etcd) دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion نسخه‌دار بودن طرح‌واره (schema) این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST مرتبط با این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/object-meta-v1-meta#ObjectMeta" >}}">ObjectMeta</a></em></td>
      <td>فراداده استاندارد آبجکت. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</td>
    </tr>
    <tr>
      <td><code>spec</code><br/><em><a href="{{< ref "#NodeSpec" >}}">NodeSpec</a></em></td>
      <td>Spec رفتار یک نود را تعریف می‌کند. https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
    <tr>
      <td><code>status</code><br/><em><a href="{{< ref "#NodeStatus" >}}">NodeStatus</a></em></td>
      <td>آخرین وضعیت مشاهده‌شده نود. این مقدار را سیستم تعیین می‌کند و فقط‌خواندنی است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status</td>
    </tr>
  </tbody>
</table>


## NodeSpec {#NodeSpec}

NodeSpec ویژگی‌هایی را توصیف می‌کند که نود با آن‌ها ایجاد می‌شود.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>configSource</code><br/><em><a href="{{< ref "#NodeConfigSource" >}}">NodeConfigSource</a></em></td>
      <td>منسوخ‌شده: پیش‌تر برای تعیین منبع پیکربندی نود در قابلیت DynamicKubeletConfig استفاده می‌شد. این قابلیت حذف شده است.</td>
    </tr>
    <tr>
      <td><code>externalID</code><br/><em>string</em></td>
      <td>منسوخ‌شده. همه kubeletها این فیلد را مقداردهی نمی‌کنند. این فیلد پس از نسخه 1.13 حذف می‌شود. نگاه کنید به: https://issues.k8s.io/61966</td>
    </tr>
    <tr>
      <td><code>podCIDR</code><br/><em>string</em></td>
      <td>PodCIDR بازه IP پادهای اختصاص‌یافته به نود را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>podCIDRs</code><br/><em>string array</em><br/><em>patch strategy: merge</em></td>
      <td>podCIDRs بازه‌های IP اختصاص‌یافته به نود را نشان می‌دهد که Podهای روی آن نود از آن‌ها استفاده می‌کنند. اگر این فیلد مشخص شود، مدخل صفرم باید با فیلد podCIDR یکسان باشد. این فیلد برای هر یک از IPv4 و IPv6 حداکثر یک مقدار می‌تواند داشته باشد.</td>
    </tr>
    <tr>
      <td><code>podPreemptionPolicy</code><br/><em><a href="{{< ref "#NodePodPreemptionPolicy" >}}">NodePodPreemptionPolicy</a></em></td>
      <td>PodPreemptionPolicy رفتارهای پیشدستی (preemption) در سطح نود را برای پادهای این نود کنترل می‌کند. این فیلد آلفا است و برای استفاده از آن باید feature gate با نام InPlacePodVerticalScalingSchedulerPreemption فعال شود.</td>
    </tr>
    <tr>
      <td><code>providerID</code><br/><em>string</em></td>
      <td>شناسه نودی که ارائه‌دهنده ابری (cloud provider) اختصاص داده است، با قالب: \<ProviderName>://\<ProviderSpecificNodeID></td>
    </tr>
    <tr>
      <td><code>taints</code><br/><em><a href="{{< ref "#Taint" >}}">Taint array</a></em></td>
      <td>در صورت تعیین، taintهای نود را مشخص می‌کند.</td>
    </tr>
    <tr>
      <td><code>unschedulable</code><br/><em>boolean</em></td>
      <td>Unschedulable قابلیت زمان‌بندی پادهای جدید روی نود را کنترل می‌کند. به‌طور پیش‌فرض نود قابل زمان‌بندی است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration</td>
    </tr>
  </tbody>
</table>


## NodeStatus {#NodeStatus}

NodeStatus اطلاعاتی درباره وضعیت فعلی یک نود است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>addresses</code><br/><em><a href="{{< ref "#NodeAddress" >}}">NodeAddress array</a></em><br/><em>patch strategy: merge on key <code>type</code></em></td>
      <td>فهرست نشانی‌هایی که نود از طریق آن‌ها در دسترس است. در صورت وجود، از ارائه‌دهنده ابری پرس‌وجو می‌شود. اطلاعات بیشتر: https://kubernetes.io/docs/reference/node/node-status/#addresses توجه: این فیلد قابل ادغام (mergeable) تعریف شده است، اما کلید ادغام به‌اندازه کافی یکتا نیست و ادغام آن ممکن است به خرابی داده‌ها منجر شود. به‌جای آن، فراخوان‌کننده‌ها باید از patch با جایگزینی کامل استفاده کنند. برای نمونه، نگاه کنید به https://pr.k8s.io/79391. مصرف‌کننده‌ها باید فرض کنند نشانی‌ها ممکن است در طول عمر یک Node تغییر کنند. با این حال، استثناهایی وجود دارد که ممکن است این امکان وجود نداشته باشد، مانند Podهایی که نشانی یک Node را در status خودشان به ارث می‌برند یا مصرف‌کننده‌های downward API (status.hostIP).</td>
    </tr>
    <tr>
      <td><code>allocatable</code><br/><em>object</em></td>
      <td>Allocatable منابعی از نود را نشان می‌دهد که برای زمان‌بندی در دسترس هستند. مقدار پیش‌فرض آن برابر با Capacity است.</td>
    </tr>
    <tr>
      <td><code>capacity</code><br/><em>object</em></td>
      <td>Capacity مجموع منابع یک نود را نشان می‌دهد. اطلاعات بیشتر: https://kubernetes.io/docs/reference/node/node-status/#capacity</td>
    </tr>
    <tr>
      <td><code>conditions</code><br/><em><a href="{{< ref "#NodeCondition" >}}">NodeCondition array</a></em><br/><em>patch strategy: merge on key <code>type</code></em></td>
      <td>Conditions آرایه‌ای از شرایط مشاهده‌شده فعلی نود است. اطلاعات بیشتر: https://kubernetes.io/docs/reference/node/node-status/#condition</td>
    </tr>
    <tr>
      <td><code>config</code><br/><em><a href="{{< ref "#NodeConfigStatus" >}}">NodeConfigStatus</a></em></td>
      <td>وضعیت پیکربندی‌ای که از طریق قابلیت پیکربندی پویای Kubelet به نود اختصاص داده شده است.</td>
    </tr>
    <tr>
      <td><code>daemonEndpoints</code><br/><em><a href="{{< ref "#NodeDaemonEndpoints" >}}">NodeDaemonEndpoints</a></em></td>
      <td>نقاط پایانی (endpoint) دیمن‌هایی که روی Node اجرا می‌شوند.</td>
    </tr>
    <tr>
      <td><code>declaredFeatures</code><br/><em>string array</em></td>
      <td>DeclaredFeatures قابلیت‌های مرتبط با feature gateها را نشان می‌دهد که نود آن‌ها را اعلام کرده است.</td>
    </tr>
    <tr>
      <td><code>features</code><br/><em><a href="{{< ref "#NodeFeatures" >}}">NodeFeatures</a></em></td>
      <td>Features مجموعه قابلیت‌هایی را توصیف می‌کند که پیاده‌سازی CRI آن‌ها را پیاده‌سازی کرده است.</td>
    </tr>
    <tr>
      <td><code>images</code><br/><em><a href="{{< ref "#ContainerImage" >}}">ContainerImage array</a></em></td>
      <td>فهرست ایمیج‌های کانتینر روی این نود</td>
    </tr>
    <tr>
      <td><code>nodeInfo</code><br/><em><a href="{{< ref "#NodeSystemInfo" >}}">NodeSystemInfo</a></em></td>
      <td>مجموعه‌ای از شناسه‌ها/uuidها برای شناسایی یکتای نود. اطلاعات بیشتر: https://kubernetes.io/docs/reference/node/node-status/#info</td>
    </tr>
    <tr>
      <td><code>phase</code><br/><em>string</em></td>
      <td>NodePhase آخرین فاز مشاهده‌شده از چرخه عمر نود است. اطلاعات بیشتر: https://kubernetes.io/docs/concepts/nodes/node/#phase این فیلد هرگز مقداردهی نمی‌شود و اکنون منسوخ شده است.<br/><br/>مقادیر ممکن enum:<br/> - `"Pending"` یعنی نود توسط سیستم ایجاد یا اضافه شده است، اما پیکربندی نشده است.<br/> - `"Running"` یعنی نود پیکربندی شده است و مؤلفه‌های کوبرنتیز روی آن در حال اجرا هستند.<br/> - `"Terminated"` یعنی نود از کلاستر حذف شده است.</td>
    </tr>
    <tr>
      <td><code>runtimeHandlers</code><br/><em><a href="{{< ref "#NodeRuntimeHandler" >}}">NodeRuntimeHandler array</a></em></td>
      <td>runtime handlerهای در دسترس.</td>
    </tr>
    <tr>
      <td><code>volumesAttached</code><br/><em><a href="{{< ref "#AttachedVolume" >}}">AttachedVolume array</a></em></td>
      <td>فهرست حجم‌هایی (volume) که به نود متصل شده‌اند.</td>
    </tr>
    <tr>
      <td><code>volumesInUse</code><br/><em>string array</em></td>
      <td>فهرست حجم‌های قابل اتصالی که نود از آن‌ها استفاده می‌کند (mount شده‌اند).</td>
    </tr>
  </tbody>
</table>


## NodeList {#NodeList}

NodeList فهرست کامل همه Nodeهایی است که در master ثبت شده‌اند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>apiVersion</code><br/><em>string</em></td>
      <td>APIVersion نسخه‌دار بودن طرح‌واره (schema) این نمایش از یک آبجکت را تعریف می‌کند. سرورها باید طرح‌واره‌های شناخته‌شده را به آخرین مقدار داخلی تبدیل کنند و می‌توانند مقادیر ناشناخته را رد کنند. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</td>
    </tr>
    <tr>
      <td><code>items</code>&nbsp;<strong>*</strong><br/><em><a href="{{< ref "node-v1#Node" >}}">Node array</a></em></td>
      <td>فهرست نودها</td>
    </tr>
    <tr>
      <td><code>kind</code><br/><em>string</em></td>
      <td>Kind رشته‌ای است که منبع REST مرتبط با این آبجکت را مشخص می‌کند. سرورها می‌توانند آن را از نقطه پایانی (endpoint) که کلاینت درخواست‌ها را به آن ارسال می‌کند استنتاج کنند. قابل به‌روزرسانی نیست. به‌صورت CamelCase است. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
    <tr>
      <td><code>metadata</code><br/><em><a href="{{< ref "../definitions/list-meta-v1-meta#ListMeta" >}}">ListMeta</a></em></td>
      <td>فراداده استاندارد فهرست. اطلاعات بیشتر: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</td>
    </tr>
  </tbody>
</table>


## AttachedVolume {#AttachedVolume}

AttachedVolume یک حجم (volume) متصل به نود را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>devicePath</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>DevicePath مسیر دستگاهی را نشان می‌دهد که حجم باید در آن در دسترس باشد.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نام حجم متصل‌شده</td>
    </tr>
  </tbody>
</table>


## ConfigMapNodeConfigSource {#ConfigMapNodeConfigSource}

ConfigMapNodeConfigSource اطلاعات لازم برای ارجاع به یک ConfigMap به‌عنوان منبع پیکربندی Node را در بر دارد. این API از نسخه 1.22 منسوخ شده است: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>kubeletConfigKey</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>KubeletConfigKey مشخص می‌کند کدام کلید از ConfigMap ارجاع‌شده با ساختار KubeletConfiguration متناظر است. این فیلد در همه حالت‌ها الزامی است.</td>
    </tr>
    <tr>
      <td><code>name</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Name برابر با metadata.name از ConfigMap ارجاع‌شده است. این فیلد در همه حالت‌ها الزامی است.</td>
    </tr>
    <tr>
      <td><code>namespace</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>Namespace برابر با metadata.namespace از ConfigMap ارجاع‌شده است. این فیلد در همه حالت‌ها الزامی است.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code><br/><em>string</em></td>
      <td>ResourceVersion برابر با metadata.ResourceVersion از ConfigMap ارجاع‌شده است. استفاده از این فیلد در Node.Spec ممنوع و در Node.Status الزامی است.</td>
    </tr>
    <tr>
      <td><code>uid</code><br/><em>string</em></td>
      <td>UID برابر با metadata.UID از ConfigMap ارجاع‌شده است. استفاده از این فیلد در Node.Spec ممنوع و در Node.Status الزامی است.</td>
    </tr>
  </tbody>
</table>


## ContainerImage {#ContainerImage}

یک ایمیج کانتینر را توصیف می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>names</code><br/><em>string array</em></td>
      <td>نام‌هایی که این ایمیج با آن‌ها شناخته می‌شود. برای مثال ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"]</td>
    </tr>
    <tr>
      <td><code>sizeBytes</code><br/><em>integer</em></td>
      <td>اندازه ایمیج بر حسب بایت.</td>
    </tr>
  </tbody>
</table>


## DaemonEndpoint {#DaemonEndpoint}

DaemonEndpoint اطلاعات مربوط به یک نقطه پایانی (endpoint) واحد از Daemon را در بر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>Port</code>&nbsp;<strong>*</strong><br/><em>integer</em></td>
      <td>شماره پورت نقطه پایانی مورد نظر.</td>
    </tr>
  </tbody>
</table>


## NodeAddress {#NodeAddress}

NodeAddress اطلاعات مربوط به نشانی نود را در بر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>address</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نشانی نود.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع نشانی نود؛ یکی از Hostname، ExternalIP یا InternalIP.</td>
    </tr>
  </tbody>
</table>


## NodeCondition {#NodeCondition}

NodeCondition اطلاعات شرط (condition) مربوط به یک نود را در بر دارد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>lastHeartbeatTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که به‌روزرسانی مربوط به یک شرط مشخص دریافت شده است.</td>
    </tr>
    <tr>
      <td><code>lastTransitionTime</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>آخرین زمانی که شرط از یک وضعیت به وضعیت دیگر تغییر کرده است.</td>
    </tr>
    <tr>
      <td><code>message</code><br/><em>string</em></td>
      <td>پیامی قابل‌خواندن برای انسان که جزئیات آخرین تغییر وضعیت را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>reason</code><br/><em>string</em></td>
      <td>دلیل (مختصر) آخرین تغییر وضعیت شرط.</td>
    </tr>
    <tr>
      <td><code>status</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>وضعیت شرط؛ یکی از True، False یا Unknown.</td>
    </tr>
    <tr>
      <td><code>type</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نوع شرط نود.</td>
    </tr>
  </tbody>
</table>


## NodeConfigSource {#NodeConfigSource}

NodeConfigSource منبع پیکربندی نود را مشخص می‌کند. دقیقاً یکی از زیرفیلدها (به‌جز metadata) باید غیر nil باشد. این API از نسخه 1.22 منسوخ شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>configMap</code><br/><em><a href="{{< ref "#ConfigMapNodeConfigSource" >}}">ConfigMapNodeConfigSource</a></em></td>
      <td>ConfigMap ارجاعی به ConfigMap مربوط به یک Node است.</td>
    </tr>
  </tbody>
</table>

## NodeConfigStatus {#NodeConfigStatus}

NodeConfigStatus وضعیت پیکربندی‌ای را توصیف می‌کند که از طریق Node.Spec.ConfigSource به نود اختصاص داده شده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>active</code><br/><em><a href="{{< ref "#NodeConfigSource" >}}">NodeConfigSource</a></em></td>
      <td>فیلد Active پیکربندیِ checkpoint‌شده‌ای را گزارش می‌دهد که نود در حال حاضر به‌طور فعال از آن استفاده می‌کند. بسته به اینکه تلاش برای استفاده از پیکربندی Assigned به خطا بینجامد یا نه، Active نسخه فعلی پیکربندی Assigned یا پیکربندی فعلی LastKnownGood را نشان می‌دهد.</td>
    </tr>
    <tr>
      <td><code>assigned</code><br/><em><a href="{{< ref "#NodeConfigSource" >}}">NodeConfigSource</a></em></td>
      <td>فیلد Assigned پیکربندیِ checkpoint‌شده‌ای را گزارش می‌دهد که نود سعی می‌کند از آن استفاده کند. هنگامی که Node.Spec.ConfigSource به‌روزرسانی شود، نود محتوای پیکربندی مرتبط را همراه با رکوردی که پیکربندی موردنظر را مشخص می‌کند، در دیسک محلی checkpoint می‌کند. نود برای انتخاب checkpoint پیکربندی خود به این رکورد مراجعه می‌کند و آن را در Assigned گزارش می‌دهد. Assigned فقط پس از آنکه رکورد در دیسک checkpoint شد، در status به‌روزرسانی می‌شود. هنگام راه‌اندازی مجدد Kubelet، این مؤلفه با بارگذاری و اعتبارسنجی محتوای checkpoint‌شده‌ای که Assigned به آن اشاره می‌کند، تلاش می‌کند پیکربندی Assigned را به پیکربندی Active تبدیل کند.</td>
    </tr>
    <tr>
      <td><code>error</code><br/><em>string</em></td>
      <td>فیلد Error هر مشکلی را که هنگام تطبیق Spec.ConfigSource با پیکربندی Active رخ دهد توصیف می‌کند. برای مثال، خطاها ممکن است هنگام checkpoint کردن Spec.ConfigSource در رکورد محلی Assigned، checkpoint کردن محتوای مرتبط با Spec.ConfigSource، یا بارگذاری یا اعتبارسنجی پیکربندی Assigned و موارد مشابه رخ دهند. خطاها ممکن است در مراحل مختلف همگام‌سازی پیکربندی پیش بیایند. خطاهای مراحل اولیه (مانند خطاهای دانلود یا checkpoint کردن) به بازگشت به LastKnownGood منجر نمی‌شوند و ممکن است با تلاش‌های مجدد Kubelet برطرف شوند. خطاهای مراحل بعدی (مانند بارگذاری یا اعتبارسنجی پیکربندی checkpoint‌شده) به بازگشت به LastKnownGood منجر می‌شوند. در حالت اخیر معمولاً می‌توان خطا را با اصلاح پیکربندی تعیین‌شده در Spec.ConfigSource برطرف کرد. برای یافتن اطلاعات بیشتر جهت اشکال‌زدایی، می‌توانید پیام خطا را در لاگ Kubelet جستجو کنید. Error توصیفی قابل‌خواندن برای انسان از وضعیت خطاست؛ ماشین‌ها می‌توانند بررسی کنند که Error خالی است یا نه، اما نباید به پایداری متن Error در نسخه‌های مختلف Kubelet تکیه کنند.</td>
    </tr>
    <tr>
      <td><code>lastKnownGood</code><br/><em><a href="{{< ref "#NodeConfigSource" >}}">NodeConfigSource</a></em></td>
      <td>فیلد LastKnownGood پیکربندیِ checkpoint‌شده‌ای را گزارش می‌دهد که نود هنگام مواجهه با خطا در استفاده از پیکربندی Assigned به آن بازمی‌گردد. زمانی که نود تشخیص دهد پیکربندی Assigned پایدار و درست است، این پیکربندی به LastKnownGood تبدیل می‌شود. این رفتار در حال حاضر به‌صورت یک دوره آزمون ۱۰ دقیقه‌ای پیاده‌سازی شده است که از زمان به‌روزرسانی رکورد محلی پیکربندی Assigned آغاز می‌شود. اگر پیکربندی Assigned در پایان این دوره Active باشد، به LastKnownGood تبدیل می‌شود. توجه کنید که اگر Spec.ConfigSource به nil بازنشانی شود (استفاده از پیش‌فرض‌های محلی)، LastKnownGood نیز بلافاصله به nil بازنشانی می‌شود، زیرا پیکربندی پیش‌فرض محلی همیشه سالم فرض می‌شود. نباید درباره روش نود برای تشخیص پایداری و درستی پیکربندی فرضی داشته باشید، چون ممکن است این روش در آینده تغییر کند یا قابل پیکربندی شود.</td>
    </tr>
  </tbody>
</table>


## NodeDaemonEndpoints {#NodeDaemonEndpoints}

NodeDaemonEndpoints پورت‌هایی را فهرست می‌کند که daemonهای در حال اجرا روی نود باز کرده‌اند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>kubeletEndpoint</code><br/><em><a href="{{< ref "#DaemonEndpoint" >}}">DaemonEndpoint</a></em></td>
      <td>نقطه پایانی (endpoint) که Kubelet روی آن گوش می‌دهد.</td>
    </tr>
  </tbody>
</table>


## NodeFeatures {#NodeFeatures}

NodeFeatures مجموعه ویژگی‌هایی را توصیف می‌کند که پیاده‌سازی CRI آن‌ها را پیاده‌سازی کرده است. ویژگی‌های موجود در NodeFeatures باید فقط به پیاده‌سازی CRI وابسته باشند و از runtime handlerها مستقل باشند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>supplementalGroupsPolicy</code><br/><em>boolean</em></td>
      <td>اگر محیط اجرا از SupplementalGroupsPolicy و ContainerUser پشتیبانی کند، مقدار SupplementalGroupsPolicy روی true تنظیم می‌شود.</td>
    </tr>
  </tbody>
</table>


## NodePodPreemptionPolicy {#NodePodPreemptionPolicy}

NodePodPreemptionPolicy سیاست‌های سطح نود را تعریف می‌کند که بر preemption پادهای این نود حاکم هستند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>disableResizePreemption</code><br/><em>string array</em></td>
      <td>DisableResizePreemption مالکانی (مانند autoscalerها، operatorها و مدیران) را فهرست می‌کند که درخواست کرده‌اند preemption توسط زمان‌بند و Kubelet برای تغییر اندازه درجا (in-place) پاد روی این نود غیرفعال شود. اگر این فهرست خالی نباشد، preemption ناشی از تغییر اندازه روی این نود غیرفعال است. این فیلد آلفا است و نیاز دارد feature gate با نام InPlacePodVerticalScalingSchedulerPreemption فعال شود.</td>
    </tr>
  </tbody>
</table>


## NodeRuntimeHandler {#NodeRuntimeHandler}

NodeRuntimeHandler مجموعه‌ای از اطلاعات runtime handler است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>features</code><br/><em><a href="{{< ref "#NodeRuntimeHandlerFeatures" >}}">NodeRuntimeHandlerFeatures</a></em></td>
      <td>ویژگی‌های پشتیبانی‌شده.</td>
    </tr>
    <tr>
      <td><code>name</code><br/><em>string</em></td>
      <td>نام runtime handler. برای runtime handler پیش‌فرض خالی است.</td>
    </tr>
  </tbody>
</table>


## NodeRuntimeHandlerFeatures {#NodeRuntimeHandlerFeatures}

NodeRuntimeHandlerFeatures مجموعه‌ای از ویژگی‌هاست که runtime handler پیاده‌سازی کرده است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>recursiveReadOnlyMounts</code><br/><em>boolean</em></td>
      <td>اگر runtime handler از RecursiveReadOnlyMounts پشتیبانی کند، مقدار RecursiveReadOnlyMounts روی true تنظیم می‌شود.</td>
    </tr>
    <tr>
      <td><code>userNamespaces</code><br/><em>boolean</em></td>
      <td>اگر runtime handler از UserNamespaces، از جمله برای حجم‌ها (volumes)، پشتیبانی کند، مقدار UserNamespaces روی true تنظیم می‌شود.</td>
    </tr>
  </tbody>
</table>


## NodeSwapStatus {#NodeSwapStatus}

NodeSwapStatus اطلاعات حافظه swap را نشان می‌دهد.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>capacity</code><br/><em>integer</em></td>
      <td>مقدار کل حافظه swap بر حسب بایت.</td>
    </tr>
  </tbody>
</table>


## NodeSystemInfo {#NodeSystemInfo}

NodeSystemInfo مجموعه‌ای از شناسه‌ها/uuidها برای شناسایی یکتای نود است.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>architecture</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>معماری گزارش‌شده توسط نود</td>
    </tr>
    <tr>
      <td><code>bootID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>شناسه بوت (Boot ID) گزارش‌شده توسط نود.</td>
    </tr>
    <tr>
      <td><code>containerRuntimeVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نسخه ContainerRuntime که نود از طریق API راه دور محیط اجرا گزارش می‌کند (مثلاً containerd://1.4.2).</td>
    </tr>
    <tr>
      <td><code>kernelVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نسخه کرنل که نود با دستور 'uname -r' گزارش می‌کند (مثلاً 3.16.0-0.bpo.4-amd64).</td>
    </tr>
    <tr>
      <td><code>kubeProxyVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>منسوخ‌شده: نسخه KubeProxy که نود گزارش می‌کند.</td>
    </tr>
    <tr>
      <td><code>kubeletVersion</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>نسخه Kubelet که نود گزارش می‌کند.</td>
    </tr>
    <tr>
      <td><code>machineID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>MachineID گزارش‌شده توسط نود. برای شناسایی یکتای ماشین در کلاستر، استفاده از این فیلد ترجیح داده می‌شود. برای اطلاعات بیشتر به man(5) machine-id مراجعه کنید: http://man7.org/linux/man-pages/man5/machine-id.5.html</td>
    </tr>
    <tr>
      <td><code>operatingSystem</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>سیستم‌عاملی که نود گزارش می‌کند</td>
    </tr>
    <tr>
      <td><code>osImage</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>ایمیج سیستم‌عامل (OS Image) که نود از /etc/os-release گزارش می‌کند (مثلاً Debian GNU/Linux 7 (wheezy)).</td>
    </tr>
    <tr>
      <td><code>runningInUserNamespace</code><br/><em>boolean</em></td>
      <td>مشخص می‌کند که نود در یک user namespace اجرا می‌شود یا نه.</td>
    </tr>
    <tr>
      <td><code>swap</code><br/><em><a href="{{< ref "#NodeSwapStatus" >}}">NodeSwapStatus</a></em></td>
      <td>اطلاعات swap که نود گزارش می‌کند.</td>
    </tr>
    <tr>
      <td><code>systemUUID</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>SystemUUID گزارش‌شده توسط نود. برای شناسایی یکتای ماشین، MachineID ترجیح داده می‌شود. این فیلد مختص میزبان‌های Red Hat است: https://access.redhat.com/documentation/en-us/red_hat_subscription_management/1/html/rhsm/uuid</td>
    </tr>
  </tbody>
</table>


## Taint {#Taint}

نودی که این Taint به آن متصل شده است، روی هر پادی که Taint را تحمل (tolerate) نکند، «اثر» (effect) اعمال می‌کند.

<hr>

<table>
  <thead><tr><th>Field</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>effect</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>الزامی. اثر taint روی پادهایی که taint را تحمل نمی‌کنند. اثرهای معتبر عبارت‌اند از NoSchedule، PreferNoSchedule و NoExecute.<br/><br/>Possible enum values:<br/> - `"NoExecute"` هر پادِ در حال اجرایی را که taint را تحمل نمی‌کند، بیرون می‌راند (evict). در حال حاضر توسط NodeController اعمال می‌شود.<br/> - `"NoSchedule"` اجازه نمی‌دهد پادهای جدید روی نود زمان‌بندی شوند، مگر اینکه taint را تحمل کنند؛ اما به همه پادهایی که بدون عبور از زمان‌بند به Kubelet ارسال شده‌اند اجازه شروع می‌دهد و همه پادهای در حال اجرا نیز به کار خود ادامه می‌دهند. توسط زمان‌بند اعمال می‌شود.<br/> - `"PreferNoSchedule"` مانند TaintEffectNoSchedule است، با این تفاوت که زمان‌بند تلاش می‌کند پادهای جدید را روی نود زمان‌بندی نکند، اما زمان‌بندی پادهای جدید روی نود را به‌طور کامل ممنوع نمی‌کند. توسط زمان‌بند اعمال می‌شود.</td>
    </tr>
    <tr>
      <td><code>key</code>&nbsp;<strong>*</strong><br/><em>string</em></td>
      <td>الزامی. کلید taint که باید روی نود اعمال شود.</td>
    </tr>
    <tr>
      <td><code>timeAdded</code><br/><em><a href="{{< ref "../definitions/time-v1-meta#Time" >}}">Time</a></em></td>
      <td>TimeAdded زمانی را نشان می‌دهد که taint در آن اضافه شده است.</td>
    </tr>
    <tr>
      <td><code>value</code><br/><em>string</em></td>
      <td>مقدار taint متناظر با کلید taint.</td>
    </tr>
  </tbody>
</table>



## Operations {#Operations}

<hr>


### `post` Create

#### HTTP Request

POST /api/v1/nodes



#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند، مرتبط است. طول مقدار باید کمتر از ۱۲۸ نویسه یا برابر با آن باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که مشاهده می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه فیلدهای ناشناخته و تکراریِ مشاهده‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch

#### HTTP Request

PATCH /api/v1/nodes/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره (persist) شوند. دستورالعمل dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش درخواست متوقف می‌شود. مقادیر معتبر: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند، مرتبط است. طول مقدار باید کمتر از ۱۲۸ نویسه یا برابر با آن باشد و فقط شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (application/apply-patch) الزامی است، اما برای انواع patch غیر apply (JsonPatch، MergePatch، StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که مشاهده می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بعد از آن است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگشتی از سرور شامل همه فیلدهای ناشناخته و تکراریِ مشاهده‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>Force درخواست‌های Apply را «اجباری» می‌کند. به این معنا که کاربر مالکیت فیلدهای دارای تعارض را که در اختیار دیگران است، دوباره به دست می‌آورد. پرچم Force برای درخواست‌های patch از نوع غیر apply نباید تنظیم شود.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>

### `put` Replace

#### HTTP Request

PUT /api/v1/nodes/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته برای دستور dryRun به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند نسبت داده می‌شود. طول مقدار آن باید حداکثر ۱۲۸ نویسه باشد و فقط می‌تواند شامل نویسه‌های قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>fieldValidation به سرور می‌گوید با آبجکت‌هایی در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته‌ای را که بی‌صدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه 1.23 بود. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، از طریق هدر استاندارد پاسخ هشدار (warning) یک هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق خواهد بود و از میان فیلدهای تکراری فقط آخرین مورد ذخیره می‌شود. این رفتار پیش‌فرض در نسخه 1.23 و بالاتر است. - Strict: اگر قرار باشد فیلد ناشناخته‌ای از آبجکت حذف شود یا فیلد تکراری وجود داشته باشد، درخواست با خطای BadRequest رد می‌شود. خطای بازگردانده‌شده از سرور شامل همه فیلدهای ناشناخته و تکراری است که با آن‌ها مواجه شده است.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete

#### HTTP Request

DELETE /api/v1/nodes/{name}


#### Path Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. مقدار نامعتبر یا ناشناخته برای دستور dryRun به پاسخ خطا منجر می‌شود و پردازش درخواست در همان نقطه متوقف خواهد شد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه، پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر یعنی حذف فوری. اگر این مقدار nil باشد، از دوره مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت مشخص نشدن، مقدار پیش‌فرض به ازای هر آبجکت تعیین می‌شود. مقدار صفر یعنی حذف فوری.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که روند عادی حذف به‌دلیل خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. منبعی خراب در نظر گرفته می‌شود که به‌دلیل الف) غیرقابل تبدیل بودن داده‌های آن، مثلاً در صورت شکست رمزگشایی، یا ب) ناموفق بودن رمزگشایی آن به یک آبجکت، نتوان آن را با موفقیت از ذخیره‌سازی زیرین بازیابی کرد. نکته: حذف ناایمن، محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به روند عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید آن را صراحتاً فعال کند</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا خیر. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه شیوه‌ای. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص همان منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری است که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
  </tbody>
</table>


#### Body Parameters

<table>
  <thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### Response

<table>
  <thead><tr><th>Status</th><th>Description</th><th>Response</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
    <tr>
      <td>202</td>
      <td>Accepted</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>

### `delete` حذف مجموعه

#### درخواست HTTP

DELETE /api/v1/nodes



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار این پارامتر 'true' باشد، خروجی به‌صورت خوانا (pretty-printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به جز مقدار continue) به کار ببرند و سرور ممکن است مقدار continue ناشناخته را رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور همراه با یک توکن continue خطای 410 ResourceExpired را برمی‌گرداند. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. در این حالت سرور فهرستی را برمی‌گرداند که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی ناسازگار است؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدشان پس از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion که سرور برگردانده است شروع کنند، بدون آنکه تغییری را از دست بدهند.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>وجود این پارامتر نشان می‌دهد که تغییرات نباید ماندگار شوند. مقدار dryRun نامعتبر یا ناشناخته باعث بازگشت پاسخ خطا می‌شود و پردازش بیشتر درخواست انجام نخواهد شد. مقادیر معتبر عبارت‌اند از: - All: تمام مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگشتی بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>gracePeriodSeconds</code></td>
      <td><em>integer</em></td>
      <td>مدت زمان بر حسب ثانیه پیش از آنکه آبجکت حذف شود. مقدار باید یک عدد صحیح نامنفی باشد. مقدار صفر به معنای حذف فوری است. اگر این مقدار nil باشد، از دوره مهلت پیش‌فرض نوع مشخص‌شده استفاده می‌شود. در صورت عدم تعیین، مقدار پیش‌فرض به‌ازای هر آبجکت تعیین می‌شود. مقدار صفر به معنای حذف فوری است.</td>
    </tr>
    <tr>
      <td><code>ignoreStoreReadErrorWithClusterBreakingPotential</code></td>
      <td><em>boolean</em></td>
      <td>اگر روی true تنظیم شود، در صورتی که جریان عادی حذف با خطای آبجکت خراب (corrupt) شکست بخورد، حذف ناایمن منبع را فعال می‌کند. منبعی خراب در نظر گرفته می‌شود که بازیابی موفق آن از ذخیره‌سازی زیرین ممکن نباشد، به این دلایل: الف) داده‌های آن قابل تبدیل نباشد، مثلاً به‌دلیل شکست در رمزگشایی، یا ب) رمزگشایی آن به یک آبجکت ناموفق باشد. توجه: حذف ناایمن محدودیت‌های finalizer را نادیده می‌گیرد، بررسی‌های پیش‌شرط را رد می‌کند و آبجکت را از ذخیره‌سازی حذف می‌کند. هشدار: اگر بار کاری مرتبط با منبعی که به‌صورت ناایمن حذف می‌شود به جریان عادی حذف وابسته باشد، این کار ممکن است کلاستر را دچار اختلال کند. فقط در صورتی از آن استفاده کنید که واقعاً بدانید چه می‌کنید. مقدار پیش‌فرض false است و کاربر باید برای فعال‌سازی آن صراحتاً اقدام کند.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگشتی بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌ها است.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست برگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. تعیین limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواستی (حتی صفر آیتم) برگرداند، در صورتی که تمام آبجکت‌های درخواستی فیلتر شوند؛ کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه استفاده کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را برگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های برگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این ویژگی گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که از limit برای دریافت بخش‌های کوچک‌تر یک نتیجه بسیار بزرگ استفاده می‌کند، همه آبجکت‌های ممکن را می‌بیند. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه اولین نتیجه فهرست وجود داشته است برگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>orphanDependents</code></td>
      <td><em>boolean</em></td>
      <td>منسوخ‌شده: لطفاً از PropagationPolicy استفاده کنید؛ این فیلد در نسخه 1.7 منسوخ خواهد شد. مشخص می‌کند که آیا آبجکت‌های وابسته باید یتیم (orphan) شوند یا نه. اگر true/false باشد، finalizer با نام "orphan" به فهرست finalizerهای آبجکت اضافه یا از آن حذف می‌شود. فقط یکی از این فیلد یا PropagationPolicy را می‌توان تنظیم کرد، نه هر دو را.</td>
    </tr>
    <tr>
      <td><code>propagationPolicy</code></td>
      <td><em>string</em></td>
      <td>مشخص می‌کند که آیا garbage collection انجام شود و به چه روشی. فقط یکی از این فیلد یا OrphanDependents را می‌توان تنظیم کرد، نه هر دو را. سیاست پیش‌فرض بر اساس finalizerهای موجود در metadata.finalizers و سیاست پیش‌فرض مختص منبع تعیین می‌شود. مقادیر قابل قبول عبارت‌اند از: 'Orphan' - وابسته‌ها را یتیم می‌کند؛ 'Background' - به garbage collector اجازه می‌دهد وابسته‌ها را در پس‌زمینه حذف کند؛ 'Foreground' - یک سیاست آبشاری که همه وابسته‌ها را در پیش‌زمینه حذف می‌کند.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی برای نسخه‌های منبعی تعیین می‌کند که درخواست می‌تواند از آن‌ها پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود برای فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>`sendInitialEvents=true` را می‌توان همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch طبق معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظارت را ارسال می‌کند. هنگامی که گزینه `sendInitialEvents` تنظیم شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - `resourceVersionMatch` برابر NotOlderThan به این معنا تفسیر می‌شود: «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid برگردانده می‌شود. مقدار پیش‌فرض: اگر `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگشتی را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. در این قالب، تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش به کار می‌رود:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (مثلاً "object.metadata.uid") و از قالب fieldSelector ("metadata.uid") استفاده نمی‌کند. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal در CEL هستند که درون تک‌نقل‌قول قرار می‌گیرند و با پیشوند '0x' شروع می‌شوند؛ این دو به‌ترتیب کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای هش 64 بیتی FNV-1a تعیین می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای شامل‌نشونده آن برابر 2^64 است.  مثال‌ها:   تقسیم به 2 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به 4 shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و فعال‌سازی feature gate با نام ShardedListAndWatch را لازم دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی برای فراخوانی list/watch. این مقدار مدت فراخوانی را بدون توجه به فعالیت یا عدم فعالیت محدود می‌کند.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/delete-options-v1-meta#DeleteOptions" >}}">DeleteOptions</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/status-v1-meta#Status" >}}">Status</a></em></td>
    </tr>
  </tbody>
</table>


### `get` خواندن

#### درخواست HTTP

GET /api/v1/nodes/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار این پارامتر 'true' باشد، خروجی به‌صورت خوانا (pretty-printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (مانند curl و wget) باشد.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>

### `get` List

#### HTTP Request

GET /api/v1/nodes



#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار آن 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent نشان دهد درخواست از یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) ارسال شده است.</td>
    </tr>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks رویدادهای watch با نوع "BOOKMARK" را درخواست می‌کند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه زمانی مشخصی بازگردانده می‌شوند، و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک پرسمان قبلی استفاده کنند که پارامترهای پرسمان آن (به‌جز مقدار continue) کاملاً یکسان باشد، و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به‌همراه یک continue token پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه خطای 410 ارسال کند؛ در این حالت سرور فهرستی را از کلید بعدی و از جدیدترین snapshot بازمی‌گرداند که با نتایج فهرست قبلی سازگار نیست؛ یعنی آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلید آن‌ها پس از "کلید بعدی" باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهای آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌هاست.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌های آن‌ها. مقدار پیش‌فرض شامل همه آبجکت‌هاست.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که در یک فراخوانی فهرست بازگردانده می‌شود. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان پرسمان اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است تعداد آیتم‌های کمتری از مقدار درخواست‌شده (حتی صفر آیتم) بازگرداند؛ بنابراین کلاینت‌ها برای تشخیص وجود نتایج بیشتر باید فقط به حضور فیلد continue تکیه کنند. سرورها ممکن است آرگومان limit را پشتیبانی نکنند و همه نتایج موجود را بازگردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌هایی که از یک فراخوانی فهرست واحد بدون limit به‌دست می‌آیند یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. به این ویژگی گاهی snapshot سازگار گفته می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول یک فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که در زمان محاسبه اولین نتیجه فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی را تعیین می‌کند که درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch تعیین می‌کند که resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. اکیداً توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض: تنظیم‌نشده</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را بازتولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌صورت معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از RV) آبجکت‌های تحت نظر را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شود، لازم است گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به شرح زیر است:<br/> - مقدار `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای دست‌کم به‌روز به اندازه `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد که دست‌کم به اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت به معنای «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به‌دلیل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() به‌همراه || (عملگر OR منطقی) برای مشخص کردن یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیر فیلدها از نحو CEL با ریشه object استفاده می‌کند (برای مثال "object.metadata.uid") و قالب fieldSelector ("metadata.uid") نیست. مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  hexStart و hexEnd رشته‌های literal در CEL هستند که داخل تک‌نقل‌قول قرار می‌گیرند و با پیشوند '0x' شروع می‌شوند؛ این دو مقدار، کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای hash ۶۴ بیتی FNV-1a تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را محدود می‌کند، صرف‌نظر از هرگونه فعالیت یا عدم فعالیت.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#NodeList" >}}">NodeList</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch

#### درخواست HTTP

GET /api/v1/watch/nodes/{name}


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>allowWatchBookmarks درخواست می‌کند رویدادهای watch با نوع "BOOKMARK" نیز ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند ممکن است این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در بازه‌های زمانی مشخصی بازگردانده می‌شوند، و نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>گزینه continue باید هنگام دریافت نتایج بیشتر از سرور تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند مقدار continue را از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز مقدار continue) استفاده کنند و سرور ممکن است مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به دلیل تغییر پیکربندی در سرور، سرور همراه با یک continue token با خطای 410 ResourceExpired پاسخ می‌دهد. اگر کلاینت به یک فهرست سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا آغاز کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکنی که همراه خطای 410 دریافت کرده است ارسال کند. سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته می‌شود و با نتایج فهرست قبلی ناسازگار است؛ آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند یک watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>انتخابگری برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه آبجکت‌ها را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشند، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. اگر همه آبجکت‌های درخواستی فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم (حتی صفر آیتم) بازگرداند؛ از این رو کلاینت‌ها باید فقط از وجود فیلد continue برای تشخیص وجود نتایج بیشتر استفاده کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در این صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری وجود ندارد. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند آبجکت‌هایی که هنگام استفاده از continue بازگردانده می‌شوند، با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور اولین درخواست ایجاد، تغییر یا حذف شده باشد، در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رویکرد گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت بخش‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده کند. اگر آبجکت‌ها در طول فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت بازگردانده می‌شود که هنگام محاسبه نتیجه اولین فهرست وجود داشته است.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty print) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) باشد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>resourceVersion محدودیتی تعیین می‌کند که درخواست از چه نسخه‌های منبعی می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود که وضعیت فعلی آبجکت‌های مجموعه را تولید می‌کنند. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) به‌صورت `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. سپس جریان watch به روال معمول ادامه می‌یابد و رویدادهای مربوط به تغییرات آبجکت‌های تحت نظر (پس از آن RV) را ارسال می‌کند. هنگام تنظیم گزینه `sendInitialEvents`، باید گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این صورت است:<br/> - `resourceVersionMatch` برابر NotOlderThan به معنای «داده‌ای دست‌کم به‌روز مانند `resourceVersion` ارائه‌شده» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ی همگام شده باشد که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است. اگر `resourceVersion` تنظیم نشده باشد، این حالت «خواندن سازگار» تفسیر می‌شود و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه شروع پردازش درخواست همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شود یا تنظیم نشده باشد، خطای Invalid بازگردانده می‌شود. اگر `resourceVersion=""` یا `resourceVersion="0"` باشد (به دلایل سازگاری با نسخه‌های قبلی) مقدار پیش‌فرض true است و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>shardSelector فهرست آبجکت‌های بازگردانده‌شده را با یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه hash استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو CEL با ریشه object استفاده می‌کنند (مثلاً "object.metadata.uid") و نه از قالب fieldSelector (یعنی "metadata.uid"). مسیرهای پشتیبانی‌شده در حال حاضر:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL و درون single quote هستند که پیشوند '0x' دارند و کران پایین شمول‌پذیر (inclusive) و کران بالای شمول‌ناپذیر (exclusive) را بر فضای hash ‏FNV-1a شصت‌وچهاربیتی تعریف می‌کنند. بازه کامل [0x0, 0x10000000000000000) است که در آن کران بالای شمول‌ناپذیر برابر 2^64 است.  مثال‌ها:   تقسیم به ۲ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به ۴ shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی فراخوانی list/watch. این مقدار مدت فراخوانی را صرف‌نظر از هرگونه فعالیت یا عدم فعالیت محدود می‌کند.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>

### `get` Watch List

#### درخواست HTTP

GET /api/v1/watch/nodes



#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>allowWatchBookmarks</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر allowWatchBookmarks درخواست می‌کند که رویدادهای watch با نوع "BOOKMARK" ارسال شوند. سرورهایی که bookmark را پیاده‌سازی نکرده‌اند می‌توانند این پرچم را نادیده بگیرند و ارسال bookmarkها به صلاحدید سرور است. کلاینت‌ها نباید فرض کنند که bookmarkها در فاصله‌های زمانی مشخصی ارسال می‌شوند و همچنین نباید انتظار داشته باشند که سرور در طول یک نشست حتماً رویداد BOOKMARK ارسال کند. اگر درخواست از نوع watch نباشد، این فیلد نادیده گرفته می‌شود.</td>
    </tr>
    <tr>
      <td><code>continue</code></td>
      <td><em>string</em></td>
      <td>هنگام دریافت نتایج بیشتر از سرور باید گزینه continue تنظیم شود. از آنجا که این مقدار را سرور تعیین می‌کند، کلاینت‌ها فقط می‌توانند از مقدار continue حاصل از نتیجه یک کوئری قبلی با پارامترهای کوئری یکسان (به‌جز خود مقدار continue) استفاده کنند و سرور می‌تواند مقداری از continue را که نمی‌شناسد رد کند. اگر مقدار continue مشخص‌شده دیگر معتبر نباشد، چه به‌دلیل انقضا (معمولاً پنج تا پانزده دقیقه) و چه به‌دلیل تغییر پیکربندی در سرور، سرور با خطای 410 ResourceExpired به‌همراه یک continue token پاسخ می‌دهد. اگر کلاینت به فهرستی سازگار نیاز دارد، باید فهرست‌گیری را بدون فیلد continue از ابتدا شروع کند. در غیر این صورت، کلاینت می‌تواند درخواست فهرست دیگری را با توکن دریافت‌شده همراه با خطای 410 ارسال کند؛ سرور با فهرستی پاسخ می‌دهد که از کلید بعدی شروع می‌شود، اما از جدیدترین snapshot گرفته شده است و با نتایج فهرست قبلی سازگار نیست - آبجکت‌هایی که پس از اولین درخواست فهرست ایجاد، تغییر یا حذف شده‌اند، تا زمانی که کلیدهایشان بعد از «کلید بعدی» باشد، در پاسخ گنجانده می‌شوند. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. کلاینت‌ها می‌توانند watch را از آخرین مقدار resourceVersion بازگردانده‌شده توسط سرور آغاز کنند و هیچ تغییری را از دست ندهند.</td>
    </tr>
    <tr>
      <td><code>fieldSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس فیلدهایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>labelSelector</code></td>
      <td><em>string</em></td>
      <td>یک انتخابگر (selector) برای محدود کردن فهرست آبجکت‌های بازگردانده‌شده بر اساس برچسب‌هایشان. مقدار پیش‌فرض همه‌چیز را شامل می‌شود.</td>
    </tr>
    <tr>
      <td><code>limit</code></td>
      <td><em>integer</em></td>
      <td>پارامتر limit حداکثر تعداد پاسخ‌هایی است که یک فراخوانی فهرست بازمی‌گرداند. اگر آیتم‌های بیشتری وجود داشته باشد، سرور فیلد `continue` را در فراداده فهرست روی مقداری تنظیم می‌کند که می‌توان آن را همراه با همان کوئری اولیه برای دریافت مجموعه بعدی نتایج به کار برد. در صورتی که همه آبجکت‌های درخواست‌شده فیلتر شوند، تنظیم limit ممکن است کمتر از تعداد درخواستی آیتم (حتی صفر آیتم) بازگرداند و کلاینت‌ها برای تشخیص اینکه نتایج بیشتری در دسترس است یا نه، باید فقط به وجود فیلد continue تکیه کنند. سرورها می‌توانند آرگومان limit را پشتیبانی نکنند و در آن صورت همه نتایج موجود را بازمی‌گردانند. اگر limit مشخص شده باشد و فیلد continue خالی باشد، کلاینت‌ها می‌توانند فرض کنند که نتیجه دیگری در دسترس نیست. این فیلد زمانی که watch برابر true باشد پشتیبانی نمی‌شود. سرور تضمین می‌کند که آبجکت‌های بازگردانده‌شده هنگام استفاده از continue با آبجکت‌های یک فراخوانی فهرست واحد بدون limit یکسان باشند؛ یعنی هیچ آبجکتی که پس از صدور درخواست اول ایجاد، تغییر یا حذف شده باشد در درخواست‌های ادامه‌دار بعدی گنجانده نمی‌شود. این رفتار گاهی «snapshot سازگار» نامیده می‌شود و تضمین می‌کند کلاینتی که برای دریافت تکه‌های کوچک‌تر از یک نتیجه بسیار بزرگ از limit استفاده می‌کند، همه آبجکت‌های ممکن را مشاهده خواهد کرد. اگر آبجکت‌ها در حین فهرست‌گیری تکه‌تکه به‌روزرسانی شوند، نسخه‌ای از آبجکت که هنگام محاسبه نتیجه اول فهرست وجود داشته است بازگردانده می‌شود.</td>
    </tr>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>resourceVersion</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersion محدودیتی تعیین می‌کند که درخواست از کدام نسخه‌های منبع می‌تواند پاسخ داده شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>resourceVersionMatch</code></td>
      <td><em>string</em></td>
      <td>پارامتر resourceVersionMatch مشخص می‌کند resourceVersion چگونه در فراخوانی‌های فهرست اعمال شود. به‌شدت توصیه می‌شود در فراخوانی‌های فهرستی که resourceVersion در آن‌ها تنظیم شده است، resourceVersionMatch نیز تنظیم شود. برای جزئیات به https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions مراجعه کنید. مقدار پیش‌فرض تنظیم‌نشده است.</td>
    </tr>
    <tr>
      <td><code>sendInitialEvents</code></td>
      <td><em>boolean</em></td>
      <td>می‌توان `sendInitialEvents=true` را همراه با `watch=true` تنظیم کرد. در این حالت، جریان watch با رویدادهای مصنوعی (synthetic) آغاز می‌شود تا وضعیت فعلی آبجکت‌های موجود در مجموعه را ارائه دهد. پس از ارسال همه این رویدادها، یک رویداد مصنوعی "Bookmark" ارسال می‌شود. این bookmark مقدار ResourceVersion (RV) متناظر با مجموعه آبجکت‌ها را گزارش می‌کند و با حاشیه‌نویسی (annotation) `"k8s.io/initial-events-end": "true"` علامت‌گذاری می‌شود. پس از آن، جریان watch به‌صورت معمول ادامه می‌یابد و رویدادهای watch مربوط به تغییرات (پس از آن RV) در آبجکت‌های تحت نظارت را ارسال می‌کند. وقتی گزینه `sendInitialEvents` تنظیم شده باشد، باید گزینه `resourceVersionMatch` نیز تنظیم شود. معنای درخواست watch به این شرح است:<br/> - `resourceVersionMatch` برابر NotOlderThan   به‌معنای «داده‌ای که دست‌کم به‌اندازه `resourceVersion` ارائه‌شده جدید باشد» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت با `resourceVersion`ای همگام شده باشد   که دست‌کم به‌اندازه مقدار ارائه‌شده در ListOptions تازه است.   اگر `resourceVersion` تنظیم نشده باشد، این حالت به‌معنای «خواندن سازگار» تفسیر می‌شود   و رویداد bookmark زمانی ارسال می‌شود که وضعیت دست‌کم تا لحظه‌ای   که پردازش درخواست آغاز شده است همگام شده باشد.<br/> - اگر `resourceVersionMatch` روی هر مقدار دیگری تنظیم شده باشد یا تنظیم نشده باشد،   خطای Invalid بازگردانده می‌شود. مقدار پیش‌فرض در صورتی که `resourceVersion=""` یا `resourceVersion="0"` باشد true است (به‌دلایل سازگاری با نسخه‌های قبلی) و در غیر این صورت false است.</td>
    </tr>
    <tr>
      <td><code>shardSelector</code></td>
      <td><em>string</em></td>
      <td>پارامتر shardSelector فهرست آبجکت‌های بازگردانده‌شده را با استفاده از یک عبارت shard selector مبتنی بر CEL محدود می‌کند. قالب آن از تابع shardRange() همراه با || (عملگر OR منطقی) برای تعیین یک یا چند بازه هش استفاده می‌کند:    shardRange(object.metadata.uid, '0x0', '0x8000000000000000')   shardRange(object.metadata.uid, '0x0', '0x8000000000000000') || shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')  مسیرهای فیلد از نحو (syntax) ریشه‌گرفته از آبجکت به سبک CEL استفاده می‌کنند (مثلاً "object.metadata.uid") و از قالب fieldSelector (یعنی "metadata.uid") استفاده نمی‌کنند. در حال حاضر مسیرهای زیر پشتیبانی می‌شوند:   - object.metadata.uid   - object.metadata.namespace  مقادیر hexStart و hexEnd رشته‌های literal در CEL و داخل single quote با پیشوند '0x' هستند که کران پایین شامل‌شونده و کران بالای شامل‌نشونده را روی فضای هش 64 بیتی FNV-1a تعریف می‌کنند. بازه کامل برابر [0x0, 0x10000000000000000) است که در آن کران بالای شامل‌نشونده برابر 2^64 است.  مثال‌ها:   تقسیم به دو shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')     shard 1: shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')   تقسیم به چهار shard:     shard 0: shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000')     shard 1: shardRange(object.metadata.uid, '0x4000000000000000', '0x8000000000000000')     shard 2: shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')     shard 3: shardRange(object.metadata.uid, '0xc000000000000000', '0x10000000000000000')  این فیلد آلفا است و نیاز به فعال‌سازی feature gate با نام ShardedListAndWatch دارد.</td>
    </tr>
    <tr>
      <td><code>timeoutSeconds</code></td>
      <td><em>integer</em></td>
      <td>مهلت زمانی (timeout) فراخوانی list/watch. این مقدار مدت فراخوانی را محدود می‌کند، صرف‌نظر از هر فعالیت یا عدم فعالیتی.</td>
    </tr>
    <tr>
      <td><code>watch</code></td>
      <td><em>boolean</em></td>
      <td>تغییرات منابع توصیف‌شده را زیر نظر می‌گیرد و آن‌ها را به‌صورت جریانی از اعلان‌های افزودن، به‌روزرسانی و حذف بازمی‌گرداند. resourceVersion را مشخص کنید.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "../definitions/watch-event-v1-meta#WatchEvent" >}}">WatchEvent</a></em></td>
    </tr>
  </tbody>
</table>


### `patch` Patch Status

#### درخواست HTTP

PATCH /api/v1/nodes/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نمی‌گیرد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول این مقدار باید کمتر از ۱۲۸ کاراکتر یا برابر با آن باشد و فقط شامل کاراکترهای قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint. این فیلد برای درخواست‌های apply (از نوع application/apply-patch) الزامی است، اما برای انواع patch غیر از apply (یعنی JsonPatch، MergePatch و StrategicMergePatch) اختیاری است.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته را که بی‌سروصدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و فقط آخرین فیلد از میان فیلدهای تکراری ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest ناموفق می‌کند. خطایی که سرور بازمی‌گرداند شامل همه فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
    <tr>
      <td><code>force</code></td>
      <td><em>boolean</em></td>
      <td>پارامتر Force درخواست‌های Apply را «اجباری» می‌کند. به این معنا که کاربر فیلدهای دارای تعارض را که متعلق به دیگران هستند دوباره در اختیار می‌گیرد. پرچم Force برای درخواست‌های patch غیر از apply باید تنظیم نشده باشد.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "../definitions/patch-v1-meta#Patch" >}}">Patch</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>


### `get` Read Status

#### درخواست HTTP

GET /api/v1/nodes/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>


### `put` Replace Status

#### درخواست HTTP

PUT /api/v1/nodes/{name}/status


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام Node</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>pretty</code></td>
      <td><em>string</em></td>
      <td>اگر مقدار 'true' باشد، خروجی به‌صورت خوانا (pretty printed) نمایش داده می‌شود. مقدار پیش‌فرض 'false' است، مگر آنکه user-agent یک مرورگر یا ابزار HTTP خط فرمان (curl و wget) را نشان دهد.</td>
    </tr>
    <tr>
      <td><code>dryRun</code></td>
      <td><em>string</em></td>
      <td>در صورت وجود، نشان می‌دهد که تغییرات نباید ذخیره شوند. یک دستور dryRun نامعتبر یا ناشناخته به پاسخ خطا منجر می‌شود و پردازش بیشتر درخواست انجام نمی‌گیرد. مقادیر معتبر عبارت‌اند از: - All: همه مراحل dry run پردازش می‌شوند</td>
    </tr>
    <tr>
      <td><code>fieldManager</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldManager نامی است که به عامل یا موجودیتی که این تغییرات را اعمال می‌کند مرتبط می‌شود. طول این مقدار باید کمتر از ۱۲۸ کاراکتر یا برابر با آن باشد و فقط شامل کاراکترهای قابل چاپ باشد، مطابق تعریف https://golang.org/pkg/unicode/#IsPrint.</td>
    </tr>
    <tr>
      <td><code>fieldValidation</code></td>
      <td><em>string</em></td>
      <td>پارامتر fieldValidation به سرور دستور می‌دهد با آبجکت‌های موجود در درخواست (POST/PUT/PATCH) که فیلدهای ناشناخته یا تکراری دارند چگونه رفتار کند. مقادیر معتبر عبارت‌اند از: - Ignore: فیلدهای ناشناخته را که بی‌سروصدا از آبجکت حذف می‌شوند نادیده می‌گیرد و از میان فیلدهای تکراری، همه را به‌جز آخرین فیلدی که رمزگشا (decoder) با آن مواجه می‌شود نادیده می‌گیرد. این رفتار پیش‌فرض پیش از نسخه v1.23 است. - Warn: برای هر فیلد ناشناخته‌ای که از آبجکت حذف می‌شود و برای هر فیلد تکراری که با آن مواجه می‌شود، یک هشدار از طریق هدر استاندارد پاسخ هشدار ارسال می‌کند. اگر خطای دیگری وجود نداشته باشد، درخواست همچنان موفق می‌شود و فقط آخرین فیلد از میان فیلدهای تکراری ذخیره می‌شود. این رفتار پیش‌فرض در نسخه v1.23 و بالاتر است. - Strict: اگر قرار باشد هر فیلد ناشناخته‌ای از آبجکت حذف شود یا هر فیلد تکراری وجود داشته باشد، درخواست را با خطای BadRequest ناموفق می‌کند. خطایی که سرور بازمی‌گرداند شامل همه فیلدهای ناشناخته و تکراری مشاهده‌شده خواهد بود.</td>
    </tr>
  </tbody>
</table>


#### پارامترهای بدنه

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>body</code></td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
      <td></td>
    </tr>
  </tbody>
</table>


#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
    <tr>
      <td>201</td>
      <td>Created</td>
      <td><em><a href="{{< ref "node-v1#Node" >}}">Node</a></em></td>
    </tr>
  </tbody>
</table>


### `post` Create Connect Proxy

#### درخواست HTTP

POST /api/v1/nodes/{name}/proxy


#### پارامترهای مسیر

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
  </tbody>
</table>


#### پارامترهای کوئری

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیح</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی فعلی به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### پاسخ

<table>
  <thead><tr><th>وضعیت</th><th>توضیح</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>

### `post` Create Connect Proxy Path

#### HTTP Request

POST /api/v1/nodes/{name}/proxy/{path}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete Connect Proxy

#### HTTP Request

DELETE /api/v1/nodes/{name}/proxy


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `delete` Delete Connect Proxy Path

#### HTTP Request

DELETE /api/v1/nodes/{name}/proxy/{path}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` Get Connect Proxy

#### HTTP Request

GET /api/v1/nodes/{name}/proxy


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `get` Get Connect Proxy Path

#### HTTP Request

GET /api/v1/nodes/{name}/proxy/{path}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `head` Head Connect Proxy

#### HTTP Request

HEAD /api/v1/nodes/{name}/proxy


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `head` Head Connect Proxy Path

#### HTTP Request

HEAD /api/v1/nodes/{name}/proxy/{path}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `put` Replace Connect Proxy

#### HTTP Request

PUT /api/v1/nodes/{name}/proxy


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>


### `put` Replace Connect Proxy Path

#### HTTP Request

PUT /api/v1/nodes/{name}/proxy/{path}


#### Path Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><em>string</em></td>
      <td>نام NodeProxyOptions</td>
    </tr>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر منبع</td>
    </tr>
  </tbody>
</table>


#### Query Parameters

<table>
  <thead><tr><th>نام</th><th>نوع</th><th>توضیحات</th></tr></thead>
  <tbody>
    <tr>
      <td><code>path</code></td>
      <td><em>string</em></td>
      <td>مسیر URL که برای درخواست پروکسی جاری به نود استفاده می‌شود.</td>
    </tr>
  </tbody>
</table>



#### Response

<table>
  <thead><tr><th>وضعیت</th><th>توضیحات</th><th>پاسخ</th></tr></thead>
  <tbody>
    <tr>
      <td>200</td>
      <td>OK</td>
      <td><em>string</em></td>
    </tr>
  </tbody>
</table>
