---
reviewers:
- klueska
- pohly
title: آبجکت‌های API مربوط به DRA
content_type: concept
weight: 10
api_metadata:
- apiVersion: "resource.k8s.io/v1"
  kind: "ResourceClaim"
- apiVersion: "resource.k8s.io/v1"
  kind: "ResourceClaimTemplate"
- apiVersion: "resource.k8s.io/v1"
  kind: "DeviceClass"
- apiVersion: "resource.k8s.io/v1"
  kind: "ResourceSlice"
---

<!-- overview -->

این صفحه انواع (kind) API کوبرنتیز را توضیح می‌دهد که تخصیص پویای منابع
(DRA) برای دسته‌بندی، درخواست و تخصیص دستگاه‌ها از آن‌ها استفاده می‌کند.

<!-- body -->

## اصطلاحات DRA {#terminology}

DRA برای ارائه قابلیت‌های اصلی تخصیص، از انواع API کوبرنتیز زیر استفاده می‌کند. همه این انواع API در
{{< glossary_tooltip text="گروه API" term_id="api-group" >}}
`resource.k8s.io/v1` قرار دارند.

DeviceClass
: دسته‌ای از دستگاه‌ها را که می‌توان درخواست کرد تعریف می‌کند و نیز اینکه چگونه می‌توان ویژگی‌های
  مشخصی از دستگاه را در claimها انتخاب کرد. پارامترهای DeviceClass می‌توانند با صفر یا
  چند دستگاه در ResourceSliceها منطبق شوند. برای درخواست دستگاه‌ها از یک DeviceClass،
  ResourceClaimها ویژگی‌های مشخصی از دستگاه را انتخاب می‌کنند.

ResourceClaim
: درخواستی برای دسترسی به منابع متصل‌شده، مانند
  دستگاه‌ها، در کلاستر را توصیف می‌کند. ResourceClaimها به Podها دسترسی به
  یک منبع مشخص را می‌دهند. ResourceClaimها را می‌توان اپراتورهای بار کاری ایجاد کنند
  یا کوبرنتیز آن‌ها را بر پایه یک ResourceClaimTemplate تولید کند.

ResourceClaimTemplate
: قالبی را تعریف می‌کند که کوبرنتیز برای ایجاد ResourceClaimهای اختصاصی هر Pod برای یک بار کاری
  از آن استفاده می‌کند. ResourceClaimTemplateها به Podها
  دسترسی به منابع جداگانه و مشابه را می‌دهند. هر ResourceClaim که کوبرنتیز
  از روی این قالب تولید می‌کند به یک Pod مشخص متصل (bound) می‌شود. هنگامی که Pod
  پایان می‌یابد، کوبرنتیز ResourceClaim متناظر را حذف می‌کند.

ResourceSlice
: یک یا چند منبع را که به نودها متصل هستند، مانند دستگاه‌ها، نمایندگی می‌کند.
  درایورها ResourceSliceها را در کلاستر ایجاد و مدیریت می‌کنند. هنگامی که یک ResourceClaim
  ایجاد می‌شود و در یک Pod به کار می‌رود، کوبرنتیز از ResourceSliceها برای یافتن نودهایی
  استفاده می‌کند که به منابع درخواست‌شده دسترسی دارند. کوبرنتیز منابع را به
  ResourceClaim تخصیص می‌دهد و Pod را روی نودی زمان‌بندی می‌کند که بتواند به آن
  منابع دسترسی داشته باشد.

### DeviceClass {#deviceclass}

DeviceClass به مدیران کلاستر یا درایورهای دستگاه امکان می‌دهد دسته‌هایی از دستگاه‌ها
را در کلاستر تعریف کنند. DeviceClassها به اپراتورها می‌گویند که چه دستگاه‌هایی را می‌توانند درخواست کنند و
چگونه می‌توانند آن دستگاه‌ها را درخواست کنند. می‌توانید با استفاده از
[زبان عبارت مشترک (CEL)](https://cel.dev) دستگاه‌ها را بر اساس
ویژگی‌های مشخص انتخاب کنید. یک ResourceClaim که به DeviceClass ارجاع می‌دهد، سپس می‌تواند
پیکربندی‌های مشخصی را در همان DeviceClass درخواست کند.

برای ایجاد یک DeviceClass، به
[راه‌اندازی DRA در یک کلاستر](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster) مراجعه کنید.

### ResourceClaimها و ResourceClaimTemplateها {#resourceclaims-templates}

ResourceClaim منابعی را که یک بار کاری به آن‌ها نیاز دارد تعریف می‌کند. هر ResourceClaim
دارای _درخواست‌هایی (requests)_ است که به یک DeviceClass ارجاع می‌دهند و دستگاه‌ها را از همان
DeviceClass انتخاب می‌کنند. ResourceClaimها همچنین می‌توانند از _انتخابگرها (selectors)_ برای فیلتر کردن دستگاه‌هایی که
الزامات مشخصی را برآورده می‌کنند استفاده کنند، و می‌توانند از _محدودیت‌ها (constraints)_ برای محدود کردن دستگاه‌هایی که
می‌توانند یک درخواست را برآورده کنند بهره ببرند. ResourceClaimها را می‌توان اپراتورهای بار کاری ایجاد کنند یا
کوبرنتیز می‌تواند آن‌ها را بر پایه یک ResourceClaimTemplate تولید کند.
ResourceClaimTemplate قالبی را تعریف می‌کند که کوبرنتیز می‌تواند از آن برای
تولید خودکار ResourceClaimها برای Podها استفاده کند.

#### موارد استفاده از ResourceClaimها و ResourceClaimTemplateها {#when-to-use-rc-rct}

روشی که به کار می‌برید به نیازهای شما بستگی دارد، به شرح زیر:

* **ResourceClaim**: می‌خواهید چندین Pod دسترسی به دستگاه‌های مشخصی را با هم به اشتراک بگذارند.
  چرخه عمر ResourceClaimهایی را که ایجاد می‌کنید خودتان به‌صورت دستی مدیریت می‌کنید.
* **ResourceClaimTemplate**: می‌خواهید Podها دسترسی مستقل به
  دستگاه‌های جداگانه با پیکربندی مشابه داشته باشند. کوبرنتیز ResourceClaimها را
  از روی مشخصات (specification) موجود در ResourceClaimTemplate تولید می‌کند. طول عمر هر
  ResourceClaim تولیدشده به طول عمر Pod متناظر آن وابسته است.
* [**PodGroup ResourceClaimTemplate**](#workload-resource-claims): می‌خواهید
  {{< glossary_tooltip text="PodGroupها" term_id="podgroup" >}} دسترسی مستقل به دستگاه‌های جداگانه با پیکربندی مشابه داشته باشند
  که Podهای آن‌ها بتوانند آن دستگاه‌ها را به اشتراک بگذارند. کوبرنتیز یک ResourceClaim برای PodGroup
  از روی مشخصات موجود در ResourceClaimTemplate تولید می‌کند. طول عمر هر
  ResourceClaim تولیدشده به طول عمر PodGroup متناظر آن وابسته است. این روش نیازمند
  فعال بودن قابلیت
  [`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims)
  است.

هنگام تعریف یک بار کاری، می‌توانید از
{{< glossary_tooltip term_id="cel" text="زبان عبارت مشترک (CEL)" >}}
برای فیلتر کردن ویژگی‌ها یا ظرفیت مشخص دستگاه استفاده کنید. پارامترهای قابل‌استفاده
برای فیلتر کردن به دستگاه و درایورها بستگی دارند.

اگر در یک Pod مستقیماً به یک ResourceClaim مشخص ارجاع دهید، آن ResourceClaim
باید از پیش در همان فضای نام (namespace) Pod وجود داشته باشد. اگر ResourceClaim
در آن فضای نام وجود نداشته باشد، Pod زمان‌بندی نخواهد شد. این رفتار مشابه این است
که یک PersistentVolumeClaim باید در همان فضای نام Podی وجود داشته باشد که
به آن ارجاع می‌دهد.

می‌توانید در یک Pod به یک ResourceClaim تولیدشده خودکار ارجاع دهید، اما این کار
توصیه نمی‌شود، زیرا ResourceClaimهای تولیدشده خودکار به طول عمر
Pod یا PodGroupی که تولید آن‌ها را برانگیخته است وابسته‌اند.

برای آگاهی از نحوه درخواست منابع با یکی از این روش‌ها، به
[تخصیص دستگاه‌ها به بارهای کاری با DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/) مراجعه کنید.

#### فهرست اولویت‌بندی‌شده {#prioritized-list}

{{< feature-state feature_gate_name="DRAPrioritizedList" >}}

می‌توانید برای درخواست‌ها در یک ResourceClaim یا
ResourceClaimTemplate فهرستی اولویت‌بندی‌شده از زیردرخواست‌ها (subrequests) ارائه کنید. سپس زمان‌بند، نخستین زیردرخواستی را که قابل تخصیص باشد انتخاب می‌کند.
این کار به کاربران امکان می‌دهد در صورت در دسترس نبودن انتخاب اصلی، دستگاه‌های جایگزینی را مشخص کنند که بار کاری
بتواند از آن‌ها استفاده کند.

در مثال زیر، ResourceClaimTemplate دستگاهی با رنگ سیاه
و اندازه بزرگ را درخواست کرده است. اگر دستگاهی با این ویژگی‌ها در دسترس نباشد، Pod
زمان‌بندی نمی‌شود. با قابلیت فهرست اولویت‌بندی‌شده می‌توان گزینه جایگزین دومی را مشخص کرد که
دو دستگاه با رنگ سفید و اندازه کوچک را درخواست می‌کند. اگر دستگاه سیاه بزرگ در دسترس باشد،
تخصیص داده می‌شود. اگر در دسترس نباشد، اما دو دستگاه سفید کوچک در دسترس باشند،
Pod همچنان می‌تواند اجرا شود.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: prioritized-list-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        firstAvailable:
        - name: large-black
          deviceClassName: resource.example.com
          selectors:
          - cel:
              expression: |-
                device.attributes["resource-driver.example.com"].color == "black" &&
                device.attributes["resource-driver.example.com"].size == "large"
        - name: small-white
          deviceClassName: resource.example.com
          selectors:
          - cel:
              expression: |-
                device.attributes["resource-driver.example.com"].color == "white" &&
                device.attributes["resource-driver.example.com"].size == "small"
          count: 2
```

اگر Pod برای چند نود در کلاستر واجد شرایط باشد، زمان‌بند هنگام امتیازدهی به هر نود،
اندیس زیردرخواست‌های انتخاب‌شده از هر فهرست اولویت‌بندی‌شده را به‌عنوان یکی از ورودی‌ها
به کار می‌برد. بنابراین نودهایی که می‌توانند دستگاه‌های درخواست‌شده در یک
زیردرخواست با رتبه بالاتر را تخصیص دهند، بیش از نودهایی که فقط می‌توانند دستگاه‌های
زیردرخواست‌های با رتبه پایین‌تر را تخصیص دهند، احتمال انتخاب شدن دارند.

این تصمیم به‌ازای هر Pod گرفته می‌شود؛ بنابراین اگر Pod عضو یک ReplicaSet یا
گروه‌بندی مشابه باشد، نمی‌توانید انتظار داشته باشید که برای همه اعضای گروه یک زیردرخواست یکسان
انتخاب شود. بار کاری شما باید بتواند این وضعیت را در نظر بگیرد.

#### ResourceClaimهای بار کاری {#workload-resource-claims}

{{< feature-state feature_gate_name="DRAWorkloadResourceClaims" >}}

هنگامی که Podها را با
[Workload API](/docs/concepts/workloads/workload-api/)
سازماندهی می‌کنید، می‌توانید ResourceClaimها را به‌جای Podهای منفرد برای کل
{{< glossary_tooltip text="PodGroupها" term_id="podgroup" >}}
رزرو کنید و ResourceClaimTemplateها را به‌جای یک Pod واحد برای یک
PodGroup تولید کنید؛ به این ترتیب Podهای درون یک PodGroup می‌توانند
دسترسی به دستگاه‌های تخصیص‌یافته به ResourceClaim تولیدشده را به اشتراک بگذارند.

این قابلیت دو مشکل را هدف قرار می‌دهد:

- فهرست `status.reservedFor` در API مربوط به ResourceClaim حداکثر می‌تواند ۲۵۶ مورد داشته باشد.
  از آنجا که kube-scheduler فقط Podهای منفرد را در آن فهرست ثبت می‌کند، تنها ۲۵۶ Pod
  می‌توانند یک ResourceClaim را به اشتراک بگذارند. با امکان ثبت PodGroupها در
  `status.reservedFor`، بیش از ۲۵۶ Pod می‌توانند یک ResourceClaim را به اشتراک بگذارند.
- Podها فقط زمانی می‌توانند یک ResourceClaim را به اشتراک بگذارند که نام دقیق آن مشخص باشد. برای بارهای کاری
  پیچیده‌ای که _گروه‌هایی_ از Podها را تکثیر می‌کنند، ResourceClaimهایی که Podهای
  هر گروه به اشتراک می‌گذارند باید هنگام افزایش و کاهش مقیاس مجموعه
  گروه‌ها به‌صورت صریح ایجاد و حذف شوند. با تولید ResourceClaimها برای هر PodGroup، یک
  ResourceClaimTemplate واحد می‌تواند مبنایی برای ResourceClaimهایی باشد که هم
  به‌طور خودکار تکثیر می‌شوند و هم میان Podهای یک PodGroup قابل اشتراک‌گذاری‌اند.

API مربوط به PodGroup فیلدی با نام `spec.resourceClaims` تعریف می‌کند که ساختار آن
با فیلد `spec.resourceClaims` در API مربوط به Pod یکسان و معنای آن مشابه است:

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: training-group
  namespace: some-ns
spec:
  ...
  resourceClaims:
  - name: pg-claim
    resourceClaimName: my-pg-claim
  - name: pg-claim-template
    resourceClaimTemplateName: my-pg-template
```

مانند claimهایی که Podها ایجاد می‌کنند، claimهای PodGroup که `resourceClaimName` تعریف می‌کنند
با نام به یک ResourceClaim ارجاع می‌دهند. claimهایی که `resourceClaimTemplateName` تعریف می‌کنند
به یک ResourceClaimTemplate ارجاع می‌دهند که به یک ResourceClaim برای
کل PodGroup تکثیر می‌شود و Podهای آن می‌توانند آن را به اشتراک بگذارند.

هنگامی که یک Pod، claimی با `name`، `resourceClaimName` و
`resourceClaimTemplateName` تعریف کند که همگی با یکی از `spec.resourceClaims` مربوط به PodGroup آن
منطبق باشند، kube-scheduler ResourceClaim را برای
PodGroup رزرو می‌کند، نه برای Pod. اگر claim مربوط به Pod با هیچ‌یک از claimهای PodGroup آن
منطبق نباشد، kube-scheduler ResourceClaim را برای Pod رزرو می‌کند. در هر
دو حالت، رزرو در `status.reservedFor` مربوط به ResourceClaim ثبت می‌شود.
رزروهای PodGroup و تخصیص منبع متناظر با آن‌ها تا زمانی که PodGroup حذف شود در
ResourceClaim باقی می‌مانند، حتی اگر گروه دیگر هیچ Podی نداشته باشد.

هنگامی که یک claim از Pod که با claim مربوط به PodGroup منطبق است،
`resourceClaimTemplateName` تعریف کند، یک ResourceClaim برای
PodGroup تولید می‌شود. سایر Podهای گروه که همان claim را تعریف می‌کنند، آن
ResourceClaim تولیدشده را به اشتراک می‌گذارند، به‌جای آنکه برای هر Pod تولید یک ResourceClaim جدید برانگیخته شود.
چه یک claim از نوع `resourceClaimTemplateName` با claim مربوط به PodGroup منطبق باشد و چه نباشد، نام ResourceClaim تولیدشده در
`status.resourceClaimStatuses` مربوط به Pod ثبت می‌شود.

یک claim منطبق در PodGroup برای یک ResourceClaimTemplate تنها زمانی ایجاد
یک ResourceClaim را برمی‌انگیزد که قابلیت
[`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims)
فعال باشد. وقتی این قابلیت غیرفعال است، به‌جای ایجاد ResourceClaimهای اختصاصی هر Pod،
هیچ ResourceClaimی ایجاد نمی‌شود تا از ایجاد ResourceClaimهای ناخواسته اختصاصی هر Pod در طول ارتقای کلاستر یا
عرضه/بازگردانی (rollout/rollback) این قابلیت
میان `kube-apiserver` و `kube-controller-manager` جلوگیری شود.

ResourceClaimهایی که از یک ResourceClaimTemplate برای یک
PodGroup تولید می‌شوند، از چرخه عمر PodGroup پیروی می‌کنند. ResourceClaim زمانی برای اولین بار
ایجاد می‌شود که هم PodGroup و هم ResourceClaimTemplate آن وجود داشته باشند.
ResourceClaim پس از حذف PodGroup و زمانی که دیگر رزرو نباشد، حذف می‌شود.

مثال زیر را در نظر بگیرید:

```yaml
apiVersion: scheduling.k8s.io/v1beta1
kind: PodGroup
metadata:
  name: training-group
  namespace: some-ns
spec:
  ...
  resourceClaims:
  - name: pg-claim
    resourceClaimName: my-pg-claim
  - name: pg-claim-template
    resourceClaimTemplateName: my-pg-template
---
apiVersion: v1
kind: Pod
metadata:
  name: training-group-pod-1
  namespace: some-ns
spec:
  ...
  schedulingGroup:
    podGroupName: training-group
  resourceClaims:
  - name: pod-claim
    resourceClaimName: my-pod-claim
  - name: pod-claim-template
    resourceClaimTemplateName: my-pod-template
  - name: pg-claim
    resourceClaimName: my-pg-claim
  - name: pg-claim-template
    resourceClaimTemplateName: my-pg-template
```

در این مثال، PodGroup با نام `training-group` یک Pod با نام `training-group-pod-1` دارد.
claimهای `pod-claim` و `pod-claim-template` در Pod با هیچ
claimی از PodGroup منطبق نیستند، بنابراین این claimها تحت تأثیر
PodGroup قرار نمی‌گیرند: ResourceClaim با نام `my-pod-claim` برای Pod رزرو می‌شود و یک
ResourceClaim از ResourceClaimTemplate با نام `my-pod-template` تولید می‌شود و آن نیز
برای Pod رزرو می‌شود. claimهای `pg-claim` و `pg-claim-template` با
claimهای PodGroup منطبق هستند. ResourceClaim با نام `my-pg-claim` برای
PodGroup رزرو می‌شود و یک ResourceClaim از ResourceClaimTemplate
با نام `my-pg-template` تولید می‌شود و آن نیز برای PodGroup رزرو می‌شود.

مرتبط‌سازی ResourceClaimها با منابع Workload API توسط
[feature gate `DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims)
در `kube-apiserver`، `kube-controller-manager`، `kube-scheduler` و `kubelet` کنترل می‌شود.

### ResourceSlice {#resourceslice}

هر ResourceSlice نماینده یک یا چند
{{< glossary_tooltip term_id="device" text="دستگاه" >}} در یک pool است. این pool
توسط یک درایور دستگاه مدیریت می‌شود که ResourceSliceها را ایجاد و مدیریت می‌کند. منابع
موجود در یک pool ممکن است با یک ResourceSlice واحد نمایش داده شوند یا
چند ResourceSlice را در بر بگیرند.

ResourceSliceها اطلاعات مفیدی را برای کاربران دستگاه و زمان‌بند فراهم می‌کنند
و برای تخصیص پویای منابع حیاتی هستند. هر ResourceSlice باید شامل
اطلاعات زیر باشد:

* **Resource pool**: گروهی از یک یا چند منبع که درایور آن‌ها را مدیریت می‌کند.
  pool می‌تواند بیش از یک ResourceSlice را در بر بگیرد. تغییرات منابع موجود در یک
  pool باید در همه ResourceSliceهای آن pool منتشر شود. درایور دستگاهی که
  pool را مدیریت می‌کند مسئول اطمینان از انجام این انتشار است.
* **Devices**: دستگاه‌های موجود در pool مدیریت‌شده. یک ResourceSlice می‌تواند همه
  دستگاه‌های یک pool یا زیرمجموعه‌ای از دستگاه‌های آن را فهرست کند. ResourceSlice
  اطلاعات دستگاه مانند ویژگی‌ها، نسخه‌ها و ظرفیت را تعریف می‌کند. کاربران
  دستگاه می‌توانند با فیلتر کردن اطلاعات دستگاه در ResourceClaimها یا DeviceClassها،
  دستگاه‌ها را برای تخصیص انتخاب کنند.
* **Nodes**: نودهایی که می‌توانند به منابع دسترسی داشته باشند. درایورها می‌توانند انتخاب کنند که
  کدام نودها به منابع دسترسی داشته باشند، چه همه نودهای
  کلاستر، چه یک نود مشخص با نام، و چه نودهایی که برچسب‌های نود مشخصی دارند.

درایورها از یک {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} برای
همسان‌سازی ResourceSliceهای موجود در کلاستر با اطلاعاتی که درایور باید
منتشر کند استفاده می‌کنند. این کنترل‌کننده هر تغییر دستی را بازنویسی می‌کند، مانند زمانی که کاربران کلاستر
ResourceSliceها را ایجاد یا ویرایش می‌کنند.

ResourceSlice نمونه زیر را در نظر بگیرید:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: cat-slice
spec:
  driver: "resource-driver.example.com"
  pool:
    generation: 1
    name: "black-cat-pool"
    resourceSliceCount: 1
  # The allNodes field defines whether any node in the cluster can access the device.
  allNodes: true
  devices:
  - name: "large-black-cat"
    attributes:
      color:
        string: "black"
      size:
        string: "large"
      cat:
        bool: true
```
این ResourceSlice توسط درایور `resource-driver.example.com` در
pool با نام `black-cat-pool` مدیریت می‌شود. فیلد `allNodes: true` نشان می‌دهد که هر نود در
کلاستر می‌تواند به دستگاه‌ها دسترسی داشته باشد. در این ResourceSlice یک دستگاه با نام
`large-black-cat` وجود دارد که ویژگی‌های زیر را دارد:

* `color`: `black`
* `size`: `large`
* `cat`: `true`

یک DeviceClass می‌تواند با استفاده از این ویژگی‌ها این ResourceSlice را انتخاب کند و یک
ResourceClaim می‌تواند دستگاه‌های مشخصی را در آن DeviceClass فیلتر کند.

#### نام‌گذاری و اولویت‌بندی {#resourceslice-naming-and-prioritization}

ترتیبی که زمان‌بند کوبرنتیز دستگاه‌ها را برای تخصیص ارزیابی می‌کند،
با مرتب‌سازی واژه‌نامه‌ای (lexicographical) نام ResourceSliceها و نام poolهای منابع تعیین می‌شود.
زمان‌بند از راهبرد first-fit استفاده می‌کند، یعنی نخستین دستگاه در دسترسی را که
الزامات claim را برآورده کند انتخاب می‌کند.

این موضوع باعث می‌شود اولویت تخصیص منابع از طریق نام‌هایی که به poolها و ResourceSliceها
داده می‌شود قابل تأثیر باشد. توجه کنید که poolهای بدون
[شرایط اتصال (binding conditions)](/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/#device-binding-conditions)
همواره پیش از poolهای دارای شرایط اتصال ارزیابی می‌شوند، صرف‌نظر از نام آن‌ها.

برای درایورهایی که با بسته Go با نام `k8s.io/dynamic-resources/kubeletplugin` یا
کنترل‌کننده ResourceSlice از همان ماژول ساخته شده‌اند، این مؤلفه‌ها به‌طور خودکار نام‌گذاری
ResourceSliceها را مدیریت می‌کنند تا اطمینان حاصل شود که به ترتیب مشخص‌شده توسط درایور ارزیابی می‌شوند.

## دسترسی مدیریتی (Admin access) {#admin-access}

{{< feature-state feature_gate_name="DRAAdminAccess" >}}

می‌توانید یک درخواست را در ResourceClaim یا ResourceClaimTemplate به‌عنوان دارای
قابلیت‌های ممتاز برای وظایف نگهداری و عیب‌یابی علامت‌گذاری کنید. درخواستی که
دسترسی مدیریتی (admin access) دارد، دسترسی به دستگاه‌های در حال استفاده را فراهم می‌کند و ممکن است هنگام در دسترس قرار دادن دستگاه
در یک کانتینر، مجوزهای اضافی را فعال کند:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: large-black-cat-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        exactly:
          deviceClassName: resource.example.com
          allocationMode: All
          adminAccess: true
```

دسترسی مدیریتی (Admin access) یک حالت ممتاز است و نباید در
کلاسترهای چندمستاجری به کاربران عادی داده شود. تنها کاربرانی که مجاز به
ایجاد آبجکت‌های ResourceClaim یا ResourceClaimTemplate در فضاهای نامِ دارای برچسب
`resource.kubernetes.io/admin-access: "true"` (حساس به حروف بزرگ و کوچک) هستند، می‌توانند از فیلد
`adminAccess` استفاده کنند. این کار تضمین می‌کند که کاربران غیرمدیر نمی‌توانند از این
قابلیت سوءاستفاده کنند.

دسترسی مدیریتی (Admin access) توسط
[feature gate `DRAAdminAccess`](/docs/reference/command-line-tools-reference/feature-gates/#DRAAdminAccess)
در `kube-apiserver`، `kube-scheduler` و `kubelet` کنترل می‌شود.

## ویژگی‌های از نوع لیست {#list-type-attributes}

{{< feature-state feature_gate_name="DRAListTypeAttributes" >}}

این قابلیت API مربوط به ResourceSlice را بهبود می‌دهد و به درایورهای DRA اجازه می‌دهد برای ویژگی‌های دستگاه (device attributes) به‌جای مقادیر اسکالر صرف، مقادیر از نوع لیست مشخص کنند.
این امر برای مدل‌سازی توپولوژی‌های داخلی پیچیده‌تر نود مفید است، برای مثال زمانی که یک CPU با چندین PCIe root مجاورت دارد.

برای نویسندگان ResourceClaim (کاربران نهایی)، این به آن معناست که `matchAttribute` و `distinctAttribute` در این موارد بهتر عمل می‌کنند.

- `matchAttribute` — دو ویژگی باید *اشتراک غیرتهی لیست‌ها* داشته باشند، نه اینکه کاملاً یکسان باشند (مقادیر اسکالر به‌صورت لیست‌های تک‌عضوی در نظر گرفته می‌شوند).
  این بدان معناست که اگر یک درایور برای مثال یک مقدار واحد برای PCIe root منتشر کند و درایور دیگری یک لیست منتشر کند، تا زمانی که مقدار واحد در جایی از لیست وجود داشته باشد، قید برقرار است.
- `distinctAttribute` — مقادیر ویژگی باید *دوبه‌دو مجزا* باشند (هیچ مقداری بین هیچ دو دستگاهی مشترک نباشد)

برای کمک به نویسندگان ResourceClaim در استفاده از ویژگی‌هایی که ممکن است لیست باشند، در عبارات CEL، این قابلیت یک تابع CEL به نام `includes()` نیز معرفی می‌کند.

```
# Scalar attribute (backward compatible)
# assume: device.attributes["dra.example.com"].model = "model-a"
device.attributes["dra.example.com"].model.includes("model-a")  # true
device.attributes["dra.example.com"].model.includes("model-b")  # false

# List-type attribute (requires DRAListTypeAttributes)
# assume: device.attributes["dra.example.com"].supported-models= ["model-a", "model-b"]
device.attributes["dra.example.com"].supported-models.includes("model-a")  # true
device.attributes["dra.example.com"].supported-models.includes("model-c")  # false
```

### جزئیات برای نویسندگان درایور DRA {#details-for-dra-driver-authors}

به‌طور پیش‌فرض، هر `DeviceAttribute` دقیقاً یک مقدار اسکالر دارد: یک مقدار بولی، یک عدد صحیح،
یک رشته یا یک رشته نسخه معنایی (semantic version). feature gate با نام `DRAListTypeAttributes`
فیلد `DeviceAttribute` را با چهار فیلد از نوع لیست گسترش می‌دهد تا یک دستگاه بتواند
چندین مقدار را برای یک ویژگی واحد اعلام کند:

- **`bools`** — لیستی از مقادیر بولی
- **`ints`** — لیستی از مقادیر عدد صحیح ۶۴ بیتی
- **`strings`** — لیستی از رشته‌ها (هر کدام حداکثر ۶۴ نویسه)
- **`versions`** — لیستی از رشته‌های نسخه معنایی مطابق مشخصات semver.org نسخه 2.0.0
  (هر کدام حداکثر ۶۴ نویسه)

تعداد کل مقادیر منفرد ویژگی‌ها برای هر دستگاه (فیلدهای اسکالر به‌علاوه تمام عناصر لیست‌ها
روی هم) به **۴۸** محدود است. هنگامی که هر دستگاهی در یک ResourceSlice از این قابلیت یا سایر قابلیت‌های پیشرفته مانند taintها استفاده کند،
آن ResourceSlice حداکثر به **۶۴** دستگاه محدود می‌شود.
use list-type attributes or other advanced features such as taints.

در ادامه مثالی از دستگاهی آمده است که با استفاده از یک ویژگی رشته‌ای از نوع لیست، چندین مدل پشتیبانی‌شده را اعلام می‌کند:

```yaml
kind: ResourceSlice
apiVersion: resource.k8s.io/v1
metadata:
  name: example-resourceslice
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 1
  driver: dra.example.com
  devices:
  - name: gpu-0
    attributes:
      dra.example.com/supported-models:
        strings:
        - model-a
        - model-b
```

ویژگی‌های از نوع لیست توسط
[feature gate با نام `DRAListTypeAttributes`](/docs/reference/command-line-tools-reference/feature-gates/#DRAListTypeAttributes)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.

## ویژگی‌های مشتق‌شده {#derived-attributes}

{{< feature-state feature_gate_name="DRADerivedAttributes" >}}

قیدهای `matchAttribute` و `distinctAttribute` معمولاً نیاز دارند که
دستگاه‌ها ویژگی‌ها را دقیقاً با یک نام یکسان منتشر کنند. اگر یک درایور GPU
ویژگی `pcie_locality` را منتشر کند و یک درایور NIC ویژگی `pcie_root` را (یا همین اطلاعات را
در رشته‌ای مانند `numa0-pcie1` جاسازی کند)، زمان‌بند راهی برای تشخیص اینکه این‌ها
یک مفهوم واحد را نشان می‌دهند ندارد، بنابراین دستگاه‌های این دو درایور
بدون توافق قبلی بر سر یک نام ویژگی مشترک نمی‌توانند در کنار هم قرار بگیرند.

`derivedAttributes` به شما امکان می‌دهد این شکاف را به‌صورت درون‌خطی پر کنید، بدون اینکه منتظر بمانید
درایورها بر سر نام‌های ویژگی مشترک استانداردسازی کنند. یک یا چند ورودی
`derivedAttributes` را به یک درخواست اضافه کنید، در مسیر
`.spec.devices.requests[].exactly` یا
`.spec.devices.requests[].firstAvailable[]`. هر ورودی یک عبارت CEL تعریف می‌کند
که زمان‌بند آن را برای هر دستگاه کاندید آن درخواست ارزیابی می‌کند. نتیجه به یک ویژگی مجازی تبدیل می‌شود که
می‌توان از یک قید `matchAttribute` یا `distinctAttribute` دقیقاً مانند یک ویژگی دستگاهِ
ارائه‌شده توسط درایور به آن ارجاع داد.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  name: gpu-nic-numa-alignment
spec:
  devices:
    requests:
    - name: gpu
      exactly:
        deviceClassName: gpu.example.com
        count: 1
        derivedAttributes:
        - name: derived/numa
          expression: device.attributes["gpu.example.com"].numa
    - name: nic
      exactly:
        deviceClassName: nic.example.com
        count: 1
        derivedAttributes:
        - name: derived/numa
          expression: device.attributes["nic.example.com"].numaNode
    constraints:
    - requests: ["gpu", "nic"]
      matchAttribute: derived/numa
```

در این مثال، درایورهای `gpu` و `nic` اطلاعات توپولوژی را
با نام‌های ویژگی متفاوت (`numa` و `numaNode`) منتشر می‌کنند. هر درخواست
یک مقدار مشترک `derived/numa` را از ویژگی‌های دستگاه خود محاسبه می‌کند
و قید `matchAttribute` دو درخواست را بر اساس آن ویژگی مجازی هم‌تراز می‌کند، حتی با وجود اینکه درایورهای زیربنایی هرگز بر سر یک نام ویژگی مشترک توافق نکرده‌اند.

چند نکته درباره `derivedAttributes`:

- **نام‌گذاری**: `name` باید یک زیردامنه DNS باشد که پس از آن یک `/` و یک
  شناسه زبان C بیاید، یعنی همان قالبی که برای نام ویژگی‌های ارائه‌شده توسط درایور استفاده می‌شود (برای
  مثال `example.com/numaNode` یا `derived/numaNode`). اگر نام
  با یک ویژگی ارائه‌شده توسط درایور که پیش‌تر توسط آن درایور منتشر شده است یکسان باشد،
  مقدار ویژگی مشتق‌شده برای تطبیق قید، مقدار ارائه‌شده توسط درایور را پنهان می‌کند (shadow).
  اگر می‌خواهید از پنهان‌سازی ناخواسته جلوگیری کنید، از پیشوند دامنه‌ای استفاده کنید که هیچ درایوری از آن استفاده نمی‌کند،
  مانند `derived/`.
  می‌توانید برای هر درخواست حداکثر ۳۲ ویژگی مشتق‌شده تعریف کنید.
- **باید توسط یک قید استفاده شود**: هر ویژگی مشتق‌شده باید
  حداقل توسط یک قید `matchAttribute` یا `distinctAttribute` که برای درخواست (یا زیردرخواست) تعریف‌کننده آن
  اعمال می‌شود، ارجاع داده شود.
  در غیر این صورت اعتبارسنجی ResourceClaim ناموفق می‌شود.
- **دامنه و ترتیب ارزیابی**: `expression` یک بار برای هر
  دستگاه کاندید ارزیابی می‌شود، پس از آنکه انتخابگرهای CEL خودِ درخواست
  (`.selectors[].cel`) آن دستگاه را فیلتر کرده باشند. در نتیجه،
  ویژگی‌های مشتق‌شده را نمی‌توان از عبارات انتخابگر ارجاع داد و
  از طریق `device.attributes` در محیط CEL نیز در دسترس نیستند.
- **نوع بازگشتی**: `expression` باید به یک مقدار اسکالر (`string`، `int`،
  `bool` یا یک نسخه معنایی) ارزیابی شود، یا زمانی که feature gate با نام `DRAListTypeAttributes`
  نیز فعال باشد، به لیستی از یکی از همان انواع اسکالر.
- **محدودیت‌های هزینه**: هر عبارت یک حداکثر طول و یک محدودیت برای
  هزینه ارزیابی تخمینی CEL دارد. علاوه بر این، مجموع هزینه تخمینی
  همه عبارات `derivedAttributes` در یک ResourceClaim نیز محدود شده است،
  تا سربار کل افزوده‌شده به یک تلاش زمان‌بندی محدود بماند.
  اگر هر یک از این محدودیت‌ها رعایت نشود، ResourceClaim رد می‌شود.
- **خطاهای زمان اجرا زمان‌بندی را متوقف می‌کنند**: اگر ارزیابی یک عبارت برای
  یک دستگاه کاندید با شکست مواجه شود، برای مثال چون به ویژگی‌ای ارجاع می‌دهد که آن
  دستگاه ندارد، زمان‌بند تخصیص را متوقف می‌کند و زمان‌بندی Pod ناموفق می‌شود،
  به‌جای آنکه آن دستگاه را بی‌صدا نادیده بگیرد. عبارات را محتاطانه بنویسید،
  برای مثال پیش از خواندن یک ویژگی، وجود آن را بررسی کنید.

ویژگی‌های مشتق‌شده توسط
[feature gate با نام `DRADerivedAttributes`](/docs/reference/command-line-tools-reference/feature-gates/#DRADerivedAttributes)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.

برای فهرستی از ویژگی‌های استاندارد دستگاه که درایورهای DRA می‌توانند منتشر کنند، به مرجع
[ویژگی‌های استاندارد دستگاه](/docs/reference/node/dra-standard-device-attributes/)
مراجعه کنید.

## تخصیص منبع توسعه‌یافته (extended resource) توسط DRA {#extended-resource}

{{< feature-state feature_gate_name="DRAExtendedResource" >}}

می‌توانید یک نام منبع توسعه‌یافته (extended resource) برای یک DeviceClass تعیین کنید. سپس زمان‌بند
دستگاه‌های منطبق با آن کلاس را برای درخواست‌های آن منبع توسعه‌یافته انتخاب می‌کند.
این امر به کاربران اجازه می‌دهد همچنان از درخواست‌های منبع توسعه‌یافته در یک Pod استفاده کنند تا
منابع توسعه‌یافته‌ای را که توسط device plugin یا دستگاه‌های DRA ارائه می‌شوند درخواست کنند.
یک منبع توسعه‌یافته یکسان را روی یک نود واحد کلاستر می‌توان یا توسط device plugin یا توسط DRA ارائه کرد.
همچنین یک منبع توسعه‌یافته یکسان را می‌توان روی برخی نودها توسط device plugin و روی نودهای دیگرِ همان کلاستر توسط DRA ارائه کرد.

در مثال زیر، به DeviceClass مقدار extendedResourceName برابر `example.com/gpu` داده شده است.
اگر یک Pod منبع توسعه‌یافته `example.com/gpu: 2` را درخواست کند، می‌توان آن را روی
نودی زمان‌بندی کرد که دو یا چند دستگاه منطبق با DeviceClass داشته باشد.

```yaml
apiVersion: resource.k8s.io/v1
kind: DeviceClass
metadata:
  name: gpu.example.com
spec:
  selectors:
  - cel:
      expression: device.driver == 'gpu.example.com' && device.attributes['gpu.example.com'].type
        == 'gpu'
  extendedResourceName: example.com/gpu
```

علاوه بر این، کاربران می‌توانند از یک منبع توسعه‌یافته ویژه برای تخصیص دستگاه‌ها
بدون نیاز به ایجاد صریح یک ResourceClaim استفاده کنند. برای این کار از پیشوند نام منبع توسعه‌یافته
`deviceclass.resource.kubernetes.io/` به‌همراه نام DeviceClass استفاده می‌شود.
این روش برای هر DeviceClass کار می‌کند، حتی اگر نام منبع توسعه‌یافته‌ای مشخص نکرده باشد.
ResourceClaim حاصل شامل یک درخواست با `ExactCount` برای تعداد
مشخص‌شده از دستگاه‌های آن DeviceClass خواهد بود.

تخصیص منبع توسعه‌یافته توسط DRA توسط
[feature gate با نام `DRAExtendedResource`](/docs/reference/command-line-tools-reference/feature-gates/#DRAExtendedResource)
در `kube-apiserver`، `kube-scheduler`، `kube-controller-manager` و `kubelet` کنترل می‌شود.

برای مشاهده یک راهنمای عملی برای درخواست منابع توسعه‌یافته، به
[تخصیص منابع توسعه‌یافته به یک کانتینر](/docs/tasks/configure-pod-container/extended-resource/)
مراجعه کنید.
