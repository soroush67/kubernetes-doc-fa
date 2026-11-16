---
reviewers:
- klueska
- pohly
title: آبجکت‌های API در DRA
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

این صفحه انواع (kind) API کوبرنتیز را شرح می‌دهد که تخصیص پویای منابع (dynamic resource allocation یا DRA) برای دسته‌بندی، درخواست و تخصیص دستگاه‌ها از آن‌ها استفاده می‌کند.

<!-- body -->

## اصطلاحات DRA {#terminology}

سازوکار DRA برای ارائهٔ قابلیت اصلی تخصیص، از انواع API زیر در کوبرنتیز استفاده می‌کند. همهٔ این انواع API در {{< glossary_tooltip text="گروه API" term_id="api-group" >}} `resource.k8s.io/v1` قرار دارند.

DeviceClass
: دسته‌ای از دستگاه‌ها را تعریف می‌کند که می‌توان آن‌ها را درخواست (claim) کرد، و همچنین مشخص می‌کند که چگونه می‌توان ویژگی‌های (attribute) مشخصی از دستگاه را در درخواست‌ها انتخاب کرد. پارامترهای یک DeviceClass می‌توانند با صفر یا چند دستگاه در ResourceSliceها مطابقت داشته باشند. برای درخواست دستگاه از یک DeviceClass، ResourceClaimها ویژگی‌های مشخصی از دستگاه را انتخاب می‌کنند.

ResourceClaim
: درخواستی را برای دسترسی به منابع متصل در کلاستر، مانند دستگاه‌ها، توصیف می‌کند. آبجکت‌های ResourceClaim دسترسی Podها را به یک منبع مشخص فراهم می‌کنند. این آبجکت‌ها را اپراتورهای بار کاری ایجاد می‌کنند یا کوبرنتیز آن‌ها را بر اساس یک ResourceClaimTemplate تولید می‌کند.

ResourceClaimTemplate
: الگویی را تعریف می‌کند که کوبرنتیز از آن برای ایجاد ResourceClaimهای جداگانه برای هر Pod در یک بار کاری استفاده می‌کند. آبجکت‌های ResourceClaimTemplate دسترسی Podها را به منابع جداگانه و مشابه فراهم می‌کنند. هر ResourceClaim که کوبرنتیز از این الگو تولید می‌کند، به یک Pod مشخص مقید (bound) است. وقتی آن Pod خاتمه می‌یابد، کوبرنتیز ResourceClaim متناظر را حذف می‌کند.

ResourceSlice
: یک یا چند منبع متصل به نودها، مانند دستگاه‌ها، را نمایش می‌دهد. درایورها ResourceSliceها را در کلاستر ایجاد و مدیریت می‌کنند. وقتی یک ResourceClaim ایجاد می‌شود و در یک Pod به کار می‌رود، کوبرنتیز با استفاده از ResourceSliceها نودهایی را پیدا می‌کند که به منابع درخواست‌شده دسترسی دارند. سپس کوبرنتیز منابع را به ResourceClaim تخصیص می‌دهد و Pod را روی نودی زمان‌بندی می‌کند که بتواند به آن منابع دسترسی داشته باشد.

### DeviceClass {#deviceclass}

با یک DeviceClass، مدیران کلاستر یا درایورهای دستگاه می‌توانند دسته‌هایی از دستگاه‌ها را در کلاستر تعریف کنند. آبجکت‌های DeviceClass به اپراتورها نشان می‌دهند که چه دستگاه‌هایی را می‌توانند درخواست کنند و این درخواست را چگونه انجام دهند. می‌توانید از [زبان عبارت مشترک (CEL)](https://cel.dev) برای انتخاب دستگاه‌ها بر اساس ویژگی‌های مشخص استفاده کنید. سپس یک ResourceClaim که به آن DeviceClass ارجاع می‌دهد، می‌تواند پیکربندی‌های مشخصی را درون آن DeviceClass درخواست کند.

برای ایجاد یک DeviceClass، به [راه‌اندازی DRA در یک کلاستر](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster) مراجعه کنید.

### ResourceClaimها و ResourceClaimTemplateها {#resourceclaims-templates}

هر ResourceClaim منابعی را تعریف می‌کند که یک بار کاری به آن‌ها نیاز دارد. هر ResourceClaim دارای _درخواست‌هایی_ (requests) است که به یک DeviceClass ارجاع می‌دهند و از آن DeviceClass دستگاه انتخاب می‌کنند. همچنین ResourceClaimها می‌توانند از _انتخابگرها_ (selectors) برای فیلتر کردن دستگاه‌هایی استفاده کنند که الزامات مشخصی را برآورده می‌کنند، و از _قیدها_ (constraints) برای محدود کردن دستگاه‌هایی بهره بگیرند که می‌توانند یک درخواست را برآورده کنند. اپراتورهای بار کاری می‌توانند ResourceClaimها را ایجاد کنند، یا کوبرنتیز می‌تواند آن‌ها را بر اساس یک ResourceClaimTemplate تولید کند. هر ResourceClaimTemplate الگویی را تعریف می‌کند که کوبرنتیز می‌تواند از آن برای تولید خودکار ResourceClaimها برای Podها استفاده کند.

#### موارد استفاده از ResourceClaimها و ResourceClaimTemplateها {#when-to-use-rc-rct}

روشی که به کار می‌برید، به شرح زیر به نیازهای شما بستگی دارد:

* استفاده از **ResourceClaim**: می‌خواهید چند Pod به دستگاه‌های مشخصی دسترسی مشترک داشته باشند. چرخهٔ عمر ResourceClaimهایی را که ایجاد می‌کنید، خودتان به‌صورت دستی مدیریت می‌کنید.
* استفاده از **ResourceClaimTemplate**: می‌خواهید Podها به‌طور مستقل به دستگاه‌های جداگانه‌ای با پیکربندی مشابه دسترسی داشته باشند. کوبرنتیز ResourceClaimها را از مشخصات (specification) موجود در ResourceClaimTemplate تولید می‌کند. طول عمر هر ResourceClaim تولیدشده به طول عمر Pod متناظر مقید است.
* استفاده از [**ResourceClaimTemplate برای PodGroup**](#workload-resource-claims): می‌خواهید {{< glossary_tooltip text="PodGroupها" term_id="podgroup" >}} به‌طور مستقل به دستگاه‌های جداگانه‌ای با پیکربندی مشابه دسترسی داشته باشند که Podهای هر گروه بتوانند آن‌ها را به اشتراک بگذارند. کوبرنتیز از مشخصات موجود در ResourceClaimTemplate یک ResourceClaim برای PodGroup تولید می‌کند. طول عمر هر ResourceClaim تولیدشده به طول عمر PodGroup متناظر مقید است. این روش مستلزم فعال بودن قابلیت [`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims) است.

هنگام تعریف یک بار کاری، می‌توانید از {{< glossary_tooltip term_id="cel" text="زبان عبارت مشترک (CEL)" >}} برای فیلتر کردن ویژگی‌ها یا ظرفیت مشخصی از دستگاه استفاده کنید. پارامترهای موجود برای فیلتر کردن به دستگاه و درایورها بستگی دارند.

اگر در یک Pod مستقیماً به یک ResourceClaim مشخص ارجاع دهید، آن ResourceClaim باید از قبل در همان فضای نام (namespace) آن Pod وجود داشته باشد. اگر ResourceClaim در آن فضای نام وجود نداشته باشد، Pod زمان‌بندی نمی‌شود. این رفتار مشابه حالتی است که یک PersistentVolumeClaim باید در همان فضای نامِ Podای وجود داشته باشد که به آن ارجاع می‌دهد.

می‌توانید در یک Pod به یک ResourceClaim خودکارتولیدشده ارجاع دهید، اما این کار توصیه نمی‌شود؛ زیرا ResourceClaimهای خودکارتولیدشده به طول عمر Pod یا PodGroupای مقید هستند که تولید آن‌ها را آغاز کرده است.

برای آشنایی با نحوهٔ درخواست منابع با هر یک از این روش‌ها، به [تخصیص دستگاه به بارهای کاری با DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/) مراجعه کنید.

#### فهرست اولویت‌بندی‌شده {#prioritized-list}

{{< feature-state feature_gate_name="DRAPrioritizedList" >}}

می‌توانید برای درخواست‌های یک ResourceClaim یا ResourceClaimTemplate فهرستی اولویت‌بندی‌شده از زیردرخواست‌ها (subrequests) ارائه کنید. در این صورت، زمان‌بند نخستین زیردرخواستی را انتخاب می‌کند که قابل تخصیص باشد. با این کار، کاربران می‌توانند دستگاه‌های جایگزینی را مشخص کنند تا اگر گزینهٔ اصلی در دسترس نبود، بار کاری از آن‌ها استفاده کند.

در مثال زیر، ResourceClaimTemplate دستگاهی با رنگ مشکی و اندازهٔ بزرگ درخواست کرده است. اگر دستگاهی با این ویژگی‌ها در دسترس نباشد، Pod زمان‌بندی نمی‌شود. با قابلیت فهرست اولویت‌بندی‌شده می‌توان گزینهٔ جایگزین دومی را مشخص کرد که دو دستگاه با رنگ سفید و اندازهٔ کوچک درخواست می‌کند. اگر دستگاه بزرگ مشکی در دسترس باشد، همان تخصیص داده می‌شود. اگر در دسترس نباشد اما دو دستگاه کوچک سفید در دسترس باشند، Pod همچنان می‌تواند اجرا شود.

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

اگر Pod واجد شرایط قرار گرفتن روی چند نود در کلاستر باشد، زمان‌بند هنگام امتیازدهی به هر نود، اندیس زیردرخواست‌های انتخاب‌شده از فهرست‌های اولویت‌بندی‌شده را به‌عنوان یکی از ورودی‌ها در نظر می‌گیرد. بنابراین احتمال انتخاب نودهایی که می‌توانند دستگاه‌های درخواست‌شده در یک زیردرخواست با رتبهٔ بالاتر را تخصیص دهند، بیشتر از نودهایی است که فقط می‌توانند دستگاه‌های زیردرخواست‌های با رتبهٔ پایین‌تر را تخصیص دهند.

این تصمیم برای هر Pod به‌طور جداگانه گرفته می‌شود؛ بنابراین اگر Pod عضو یک ReplicaSet یا گروه‌بندی مشابهی باشد، نمی‌توانید مطمئن باشید که برای همهٔ اعضای گروه زیردرخواست یکسانی انتخاب می‌شود. بار کاری شما باید بتواند با این وضعیت سازگار باشد.

#### ResourceClaimهای بار کاری {#workload-resource-claims}

{{< feature-state feature_gate_name="DRAWorkloadResourceClaims" >}}

وقتی Podها را با [Workload API](/docs/concepts/workloads/workload-api/) سازمان‌دهی می‌کنید، می‌توانید ResourceClaimها را به‌جای Podهای منفرد برای کل {{< glossary_tooltip text="PodGroupها" term_id="podgroup" >}} رزرو کنید و ResourceClaimها را به‌جای یک Pod واحد، از روی ResourceClaimTemplateها برای یک PodGroup تولید کنید. بدین ترتیب Podهای درون یک PodGroup می‌توانند به دستگاه‌های تخصیص‌یافته به ResourceClaim تولیدشده دسترسی مشترک داشته باشند.

این قابلیت دو مشکل را هدف قرار می‌دهد:

- فهرست `status.reservedFor` در API مربوط به ResourceClaim حداکثر ۲۵۶ مورد را می‌تواند در خود جای دهد. از آنجا که kube-scheduler فقط Podهای منفرد را در این فهرست ثبت می‌کند، تنها ۲۵۶ Pod می‌توانند یک ResourceClaim را به اشتراک بگذارند. با امکان ثبت PodGroupها در `status.reservedFor`، تعداد بسیار بیشتری از ۲۵۶ Pod می‌توانند یک ResourceClaim را به اشتراک بگذارند.
- اشتراک یک ResourceClaim میان Podها فقط زمانی ممکن است که نام دقیق آن مشخص باشد. در بارهای کاری پیچیده‌ای که _گروه‌هایی_ از Podها را تکثیر می‌کنند، باید ResourceClaimهایی را که Podهای هر گروه به اشتراک می‌گذارند، هنگام افزایش و کاهش مقیاس مجموعهٔ گروه‌ها به‌صراحت ایجاد و حذف کرد. با تولید ResourceClaim برای هر PodGroup، یک ResourceClaimTemplate واحد می‌تواند مبنای ResourceClaimهایی باشد که هم به‌طور خودکار تکثیر می‌شوند و هم میان Podهای یک PodGroup قابل اشتراک‌اند.

در API مربوط به PodGroup فیلدی به نام `spec.resourceClaims` تعریف شده است که ساختاری یکسان و معنایی مشابه با فیلد `spec.resourceClaims` در API مربوط به Pod دارد:

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

همانند درخواست‌های Podها، آن دسته از درخواست‌های PodGroupها که `resourceClaimName` را تعریف می‌کنند، با نام به یک ResourceClaim ارجاع می‌دهند. درخواست‌هایی که `resourceClaimTemplateName` را تعریف می‌کنند، به یک ResourceClaimTemplate ارجاع می‌دهند که از روی آن یک ResourceClaim برای کل PodGroup ساخته می‌شود و Podهای آن گروه می‌توانند آن را به اشتراک بگذارند.

وقتی یک Pod درخواستی تعریف می‌کند که `name`، `resourceClaimName` و `resourceClaimTemplateName` آن همگی با یکی از موارد `spec.resourceClaims` در PodGroup آن مطابقت دارند، kube-scheduler آن ResourceClaim را به‌جای Pod برای PodGroup رزرو می‌کند. اگر درخواست Pod با هیچ‌یک از درخواست‌های PodGroup آن مطابقت نداشته باشد، kube-scheduler آن ResourceClaim را برای Pod رزرو می‌کند. در هر دو حالت، رزرو در `status.reservedFor` آن ResourceClaim ثبت می‌شود. رزروهای PodGroup و تخصیص منابع متناظر با آن‌ها تا زمان حذف PodGroup در ResourceClaim باقی می‌مانند، حتی اگر گروه دیگر هیچ Podای نداشته باشد.

وقتی درخواستی از Pod که با درخواستی از PodGroup مطابقت دارد، `resourceClaimTemplateName` را تعریف کند، یک ResourceClaim برای PodGroup تولید می‌شود. سایر Podهای گروه که همان درخواست را تعریف می‌کنند، به‌جای آنکه برای هر Pod یک ResourceClaim جدید تولید شود، همان ResourceClaim تولیدشده را به اشتراک می‌گذارند. چه درخواستی با `resourceClaimTemplateName` با درخواستی از PodGroup مطابقت داشته باشد و چه نداشته باشد، نام ResourceClaim تولیدشده در `status.resourceClaimStatuses` آن Pod ثبت می‌شود.

درخواست منطبق PodGroup برای یک ResourceClaimTemplate تنها زمانی به ایجاد ResourceClaim منجر می‌شود که قابلیت [`DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims) فعال باشد. وقتی این قابلیت غیرفعال است، به‌جای ایجاد ResourceClaimهای جداگانه برای هر Pod، هیچ ResourceClaimای ایجاد نمی‌شود تا در جریان ارتقای کلاستر یا عرضه و بازگردانی این قابلیت بین `kube-apiserver` و `kube-controller-manager`، ResourceClaimهای ناخواسته‌ای برای هر Pod ساخته نشود.

آن دسته از ResourceClaimهایی که از یک ResourceClaimTemplate برای یک PodGroup تولید می‌شوند، از چرخهٔ عمر PodGroup پیروی می‌کنند. این ResourceClaim نخستین بار زمانی ایجاد می‌شود که هم PodGroup و هم ResourceClaimTemplate آن وجود داشته باشند. این ResourceClaim پس از حذف PodGroup و زمانی که دیگر رزرو نشده باشد، حذف می‌شود.

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

در این مثال، PodGroup با نام `training-group` یک Pod به نام `training-group-pod-1` دارد. درخواست‌های `pod-claim` و `pod-claim-template` این Pod با هیچ‌یک از درخواست‌های PodGroup مطابقت ندارند، بنابراین PodGroup بر آن‌ها اثری ندارد: ResourceClaim با نام `my-pod-claim` برای Pod رزرو می‌شود و یک ResourceClaim نیز از ResourceClaimTemplate با نام `my-pod-template` تولید و برای Pod رزرو می‌شود. اما درخواست‌های `pg-claim` و `pg-claim-template` با درخواست‌های PodGroup مطابقت دارند. در نتیجه، ResourceClaim با نام `my-pg-claim` برای PodGroup رزرو می‌شود و یک ResourceClaim نیز از ResourceClaimTemplate با نام `my-pg-template` تولید و برای PodGroup رزرو می‌شود.

مرتبط کردن ResourceClaimها با منابع Workload API با [feature gate `DRAWorkloadResourceClaims`](/docs/reference/command-line-tools-reference/feature-gates/#DRAWorkloadResourceClaims) در `kube-apiserver`، `kube-controller-manager`، `kube-scheduler` و `kubelet` کنترل می‌شود.

### ResourceSlice {#resourceslice}

هر ResourceSlice یک یا چند {{< glossary_tooltip term_id="device" text="دستگاه" >}} را در یک مخزن (pool) نمایش می‌دهد. این مخزن را یک درایور دستگاه مدیریت می‌کند که ResourceSliceها را ایجاد و مدیریت می‌کند. منابع یک مخزن ممکن است با یک ResourceSlice واحد نمایش داده شوند یا در چند ResourceSlice گسترده باشند.

آبجکت‌های ResourceSlice اطلاعات مفیدی در اختیار کاربران دستگاه‌ها و زمان‌بند قرار می‌دهند و برای تخصیص پویای منابع اهمیتی حیاتی دارند. هر ResourceSlice باید اطلاعات زیر را داشته باشد:

* **مخزن منابع**: گروهی از یک یا چند منبع که درایور مدیریت می‌کند. یک مخزن می‌تواند بیش از یک ResourceSlice را در بر بگیرد. تغییرات منابع یک مخزن باید در همهٔ ResourceSliceهای آن مخزن منتشر شود. درایور دستگاهی که مخزن را مدیریت می‌کند، مسئول اطمینان از انجام این انتشار است.
* **دستگاه‌ها**: دستگاه‌های موجود در مخزن مدیریت‌شده. یک ResourceSlice می‌تواند همهٔ دستگاه‌های یک مخزن یا زیرمجموعه‌ای از آن‌ها را فهرست کند. هر ResourceSlice اطلاعاتی از دستگاه مانند ویژگی‌ها، نسخه‌ها و ظرفیت را تعریف می‌کند. کاربران دستگاه می‌توانند با فیلتر کردن بر اساس اطلاعات دستگاه در ResourceClaimها یا DeviceClassها، دستگاه‌هایی را برای تخصیص انتخاب کنند.
* **نودها**: نودهایی که می‌توانند به منابع دسترسی داشته باشند. درایورها می‌توانند تعیین کنند که کدام نودها به منابع دسترسی دارند؛ چه همهٔ نودهای کلاستر، چه یک نود مشخص با نام، و چه نودهایی که برچسب‌های مشخصی دارند.

درایورها از یک {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}} استفاده می‌کنند تا ResourceSliceهای کلاستر را با اطلاعاتی که درایور باید منتشر کند، هماهنگ (reconcile) کنند. این کنترل‌کننده هرگونه تغییر دستی، مانند ایجاد یا ویرایش ResourceSliceها از سوی کاربران کلاستر، را بازنویسی می‌کند.

نمونهٔ ResourceSlice زیر را در نظر بگیرید:

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
این ResourceSlice را درایور `resource-driver.example.com` در مخزن `black-cat-pool` مدیریت می‌کند. فیلد `allNodes: true` نشان می‌دهد که هر نودی در کلاستر می‌تواند به دستگاه‌ها دسترسی داشته باشد. این ResourceSlice یک دستگاه به نام `large-black-cat` با ویژگی‌های زیر دارد:

* ویژگی `color`: `black`
* ویژگی `size`: `large`
* ویژگی `cat`: `true`

یک DeviceClass می‌تواند با استفاده از این ویژگی‌ها این ResourceSlice را انتخاب کند و یک ResourceClaim می‌تواند دستگاه‌های مشخصی را در آن DeviceClass فیلتر کند.

#### نام‌گذاری و اولویت‌بندی {#resourceslice-naming-and-prioritization}

ترتیبی که زمان‌بند کوبرنتیز دستگاه‌ها را برای تخصیص ارزیابی می‌کند، با مرتب‌سازی واژه‌نامه‌ای (lexicographical) نام ResourceSliceها و مخزن‌های منابع تعیین می‌شود. زمان‌بند از راهبرد «نخستین تطابق» (first-fit) استفاده می‌کند؛ یعنی نخستین دستگاه موجودی را انتخاب می‌کند که الزامات درخواست را برآورده کند.

بنابراین می‌توان با نام‌هایی که به مخزن‌ها و ResourceSliceها داده می‌شود، بر اولویت تخصیص منابع اثر گذاشت. توجه کنید که مخزن‌های بدون [شرایط اتصال](/docs/concepts/resource-management/dynamic-resource-allocation/how-dra-works/#device-binding-conditions) همواره، صرف‌نظر از نامشان، پیش از مخزن‌های دارای شرایط اتصال ارزیابی می‌شوند.

در درایورهایی که با بستهٔ Go با نام `k8s.io/dynamic-resources/kubeletplugin` یا کنترل‌کنندهٔ ResourceSlice همین ماژول ساخته شده‌اند، این مؤلفه‌ها نام‌گذاری ResourceSliceها را به‌طور خودکار مدیریت می‌کنند تا اطمینان حاصل شود که به ترتیبی که درایور مشخص کرده است ارزیابی می‌شوند.

## دسترسی مدیر {#admin-access}

{{< feature-state feature_gate_name="DRAAdminAccess" >}}

می‌توانید یک درخواست را در ResourceClaim یا ResourceClaimTemplate به‌عنوان درخواستی با قابلیت‌های ممتاز برای کارهای نگهداری و عیب‌یابی علامت‌گذاری کنید. درخواستی با دسترسی مدیر، دسترسی به دستگاه‌های در حال استفاده را فراهم می‌کند و ممکن است هنگام در دسترس قرار دادن دستگاه در یک کانتینر، مجوزهای بیشتری را نیز فعال کند:

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

دسترسی مدیر یک حالت ممتاز است و نباید در کلاسترهای چندمستأجری به کاربران عادی اعطا شود. تنها کاربرانی که مجوز ایجاد آبجکت‌های ResourceClaim یا ResourceClaimTemplate را در فضاهای نامِ دارای برچسب `resource.kubernetes.io/admin-access: "true"` (حساس به بزرگی و کوچکی حروف) دارند، می‌توانند از فیلد `adminAccess` استفاده کنند. این کار تضمین می‌کند که کاربران غیرمدیر نتوانند از این قابلیت سوءاستفاده کنند.

دسترسی مدیر با [feature gate `DRAAdminAccess`](/docs/reference/command-line-tools-reference/feature-gates/#DRAAdminAccess) در `kube-apiserver`، `kube-scheduler` و `kubelet` کنترل می‌شود.

## ویژگی‌های فهرستی {#list-type-attributes}

{{< feature-state feature_gate_name="DRAListTypeAttributes" >}}

این قابلیت API مربوط به ResourceSlice را بهبود می‌دهد. با آن، درایورهای DRA می‌توانند برای ویژگی‌های دستگاه، به‌جای مقادیر تکی (scalar)، فهرستی از مقادیر تعیین کنند.
این قابلیت برای مدل‌سازی توپولوژی‌های داخلی پیچیده‌تر نود مفید است؛ برای مثال، زمانی که یک CPU با چند ریشهٔ PCIe مجاورت دارد.

برای نویسندگان ResourceClaim (کاربران نهایی)، این قابلیت به آن معناست که `matchAttribute` و `distinctAttribute` در چنین مواردی بهتر عمل می‌کنند.

- قید `matchAttribute`: به‌جای اینکه دو ویژگی یکسان باشند، باید *اشتراک فهرستی غیرتهی* داشته باشند (مقادیر تکی، فهرست‌هایی تک‌عضوی در نظر گرفته می‌شوند).
  معنای ساده‌اش این است که اگر یک درایور، مثلاً برای ریشهٔ PCIe، یک مقدار تکی منتشر کند و درایور دیگری یک فهرست، تا زمانی که
  آن مقدار تکی در جایی از فهرست وجود داشته باشد، قید برآورده می‌شود.
- قید `distinctAttribute`: مقادیر ویژگی باید *دوبه‌دو جدا از هم* باشند (هیچ مقداری میان هیچ دو دستگاهی مشترک نباشد).

برای اینکه نویسندگان ResourceClaim بتوانند در عبارت‌های CEL از ویژگی‌هایی استفاده کنند که ممکن است فهرستی باشند، این قابلیت تابع CEL جدیدی به نام `includes()` نیز معرفی می‌کند.

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

### جزئیات برای نویسندگان درایورهای DRA

به‌طور پیش‌فرض، هر `DeviceAttribute` دقیقاً یک مقدار تکی نگه می‌دارد: یک مقدار بولی، یک عدد صحیح،
یک رشته یا یک رشتهٔ نسخهٔ معنایی (semantic version). feature gate با نام `DRAListTypeAttributes`،
ساختار `DeviceAttribute` را با چهار فیلد فهرستی گسترش می‌دهد تا یک دستگاه بتواند برای یک ویژگی واحد
چند مقدار اعلام کند:

- فیلد **`bools`**: فهرستی از مقادیر بولی
- فیلد **`ints`**: فهرستی از مقادیر صحیح ۶۴ بیتی
- فیلد **`strings`**: فهرستی از رشته‌ها (هر کدام حداکثر ۶۴ نویسه)
- فیلد **`versions`**: فهرستی از رشته‌های نسخهٔ معنایی مطابق مشخصات semver.org نسخهٔ 2.0.0
  (هر کدام حداکثر ۶۴ نویسه)

مجموع تعداد مقادیر جداگانهٔ ویژگی‌ها برای هر دستگاه (فیلدهای تکی به‌علاوهٔ همهٔ اعضای فهرست‌ها)
به **48** محدود است. هنگامی که هر دستگاهی در یک ResourceSlice از این قابلیت یا سایر قابلیت‌های پیشرفته مانند taintها استفاده کند،
آن ResourceSlice حداکثر به **64** دستگاه محدود می‌شود.
از ویژگی‌های فهرستی یا سایر قابلیت‌های پیشرفته مانند taintها استفاده می‌کنند.

در ادامه، نمونه‌ای از دستگاهی آمده است که با استفاده از یک ویژگی رشته‌ای فهرستی،
چند مدل پشتیبانی‌شده را اعلام می‌کند:

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

قابلیت ویژگی‌های فهرستی با
[feature gate با نام `DRAListTypeAttributes`](/docs/reference/command-line-tools-reference/feature-gates/#DRAListTypeAttributes)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.

## ویژگی‌های مشتق‌شده {#derived-attributes}

{{< feature-state feature_gate_name="DRADerivedAttributes" >}}

قیدهای `matchAttribute` و `distinctAttribute` معمولاً ایجاب می‌کنند که
دستگاه‌ها ویژگی‌ها را دقیقاً با یک نام یکسان منتشر کنند. اگر یک درایور GPU
ویژگی `pcie_locality` و یک درایور NIC ویژگی `pcie_root` را منتشر کند (یا
همان اطلاعات را در رشته‌ای مانند `numa0-pcie1` بگنجاند)، زمان‌بند راهی
برای تشخیص اینکه این دو یک چیز را نشان می‌دهند ندارد. در نتیجه، دستگاه‌های این
دو درایور را نمی‌توان کنار هم قرار داد، مگر آنکه ابتدا بر سر یک نام ویژگی
مشترک توافق شود.

با `derivedAttributes` می‌توانید این شکاف را به‌صورت درجا پر کنید، بی‌آنکه منتظر
بمانید درایورها بر نام‌های ویژگی مشترک استاندارد شوند. یک یا چند مدخل
`derivedAttributes` را در یک درخواست، زیر
`.spec.devices.requests[].exactly` یا
`.spec.devices.requests[].firstAvailable[]` اضافه کنید. هر مدخل یک
عبارت CEL تعریف می‌کند که زمان‌بند آن را برای هر دستگاه نامزدِ آن درخواست
ارزیابی می‌کند. نتیجه به یک ویژگی مجازی تبدیل می‌شود که می‌توان دقیقاً مانند
یک ویژگی دستگاهِ ارائه‌شده از سوی درایور، در یک قید `matchAttribute` یا
`distinctAttribute` به آن ارجاع داد.

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

در این مثال، درایورهای `gpu` و `nic` اطلاعات توپولوژی را با
نام‌های ویژگی متفاوتی (`numa` و `numaNode`) منتشر می‌کنند. هر درخواست
یک مقدار مشترک `derived/numa` را از ویژگی‌های دستگاه خودش محاسبه می‌کند
و قید `matchAttribute` دو درخواست را بر اساس همین ویژگی مجازی هم‌راستا
می‌کند، با اینکه درایورهای زیرین هرگز بر سر یک نام ویژگی مشترک توافق
نکرده‌اند.

چند نکته دربارهٔ `derivedAttributes`:

- **نام‌گذاری**: مقدار `name` باید یک زیردامنهٔ DNS باشد که پس از آن یک `/` و یک
  شناسهٔ C می‌آید؛ همان قالبی که برای نام ویژگی‌های ارائه‌شده از سوی درایور استفاده می‌شود (برای
  مثال، `example.com/numaNode` یا `derived/numaNode`). اگر این نام
  با یک ویژگی ارائه‌شده‌ای که درایور پیش‌تر منتشر کرده است یکسان باشد،
  در تطبیق قیدها مقدار ویژگی مشتق‌شده بر مقدار ارائه‌شده از سوی درایور سایه می‌اندازد و جایگزین آن می‌شود.
  اگر می‌خواهید از سایه‌اندازی ناخواسته جلوگیری کنید، از پیشوند دامنه‌ای استفاده کنید که هیچ درایوری از آن استفاده نمی‌کند،
  مانند `derived/`.
  برای هر درخواست می‌توانید حداکثر ۳۲ ویژگی مشتق‌شده تعریف کنید.
- **الزام استفاده در یک قید**: به هر ویژگی مشتق‌شده باید دست‌کم در یک قید
  `matchAttribute` یا `distinctAttribute` ارجاع داده شود که بر درخواستی (یا زیردرخواستی)
  اعمال می‌شود که آن ویژگی را تعریف کرده است. در غیر این صورت، اعتبارسنجی ResourceClaim ناموفق خواهد بود.
- **دامنه و ترتیب ارزیابی**: عبارت `expression` برای هر دستگاه نامزد یک بار
  ارزیابی می‌شود، آن هم پس از اینکه انتخابگرهای CEL خودِ درخواست
  (`.selectors[].cel`) آن دستگاه را فیلتر کرده باشند. در نتیجه،
  نمی‌توان از عبارت‌های انتخابگر به ویژگی‌های مشتق‌شده ارجاع داد و
  این ویژگی‌ها از طریق `device.attributes` در محیط CEL در دسترس نیستند.
- **نوع خروجی**: نتیجهٔ ارزیابی `expression` باید یک مقدار تکی (`string`، `int`،
  `bool` یا یک نسخهٔ معنایی) باشد، یا اگر feature gate با نام `DRAListTypeAttributes`
  نیز فعال باشد، فهرستی از یکی از همین انواع تکی.
- **محدودیت‌های هزینه**: هر عبارت طول بیشینه‌ای دارد و هزینهٔ تخمینی
  ارزیابی CEL آن نیز محدود است. افزون بر این، مجموع هزینهٔ تخمینی
  همهٔ عبارت‌های `derivedAttributes` در یک ResourceClaim نیز سقف دارد تا
  کل سربار افزوده‌شده به یک تلاش زمان‌بندی محدود بماند. اگر هر یک از این
  محدودیت‌ها رعایت نشود، ResourceClaim رد می‌شود.
- **خطاهای زمان اجرا زمان‌بندی را متوقف می‌کنند**: اگر ارزیابی یک عبارت برای
  یک دستگاه نامزد شکست بخورد، برای مثال به این دلیل که به ویژگی‌ای ارجاع می‌دهد که
  آن دستگاه ندارد، زمان‌بند به‌جای نادیده گرفتن بی‌صدای آن دستگاه، تخصیص را متوقف می‌کند و
  زمان‌بندی Pod ناموفق می‌شود. عبارت‌ها را محتاطانه بنویسید؛
  برای مثال، پیش از خواندن یک ویژگی، وجود آن را بررسی کنید.

قابلیت ویژگی‌های مشتق‌شده با
[feature gate با نام `DRADerivedAttributes`](/docs/reference/command-line-tools-reference/feature-gates/#DRADerivedAttributes)
در `kube-apiserver` و `kube-scheduler` کنترل می‌شود.

برای دیدن فهرست ویژگی‌های استاندارد دستگاه که درایورهای DRA می‌توانند منتشر کنند، به مرجع
[ویژگی‌های استاندارد دستگاه](/docs/reference/node/dra-standard-device-attributes/)
مراجعه کنید.

## تخصیص منابع توسعه‌یافته با DRA {#extended-resource}

{{< feature-state feature_gate_name="DRAExtendedResource" >}}

می‌توانید برای یک DeviceClass نام یک منبع توسعه‌یافته (extended resource) تعیین کنید. در این صورت، زمان‌بند
برای درخواست‌های آن منبع توسعه‌یافته، دستگاه‌های منطبق بر آن کلاس را انتخاب می‌کند.
به این ترتیب، کاربران می‌توانند همچنان از درخواست‌های منبع توسعه‌یافته در یک پاد استفاده کنند تا
منابع توسعه‌یافتهٔ ارائه‌شده از سوی افزونهٔ دستگاه (device plugin) یا دستگاه‌های DRA را درخواست کنند.
یک منبع توسعه‌یافتهٔ واحد روی یک نود از کلاستر می‌تواند یا از سوی افزونهٔ دستگاه ارائه شود یا از سوی DRA.
همچنین یک منبع توسعه‌یافتهٔ واحد می‌تواند در یک کلاستر، روی برخی نودها از سوی افزونهٔ دستگاه و روی نودهای دیگر از سوی DRA ارائه شود.

در مثال زیر، به DeviceClass مقدار `example.com/gpu` به‌عنوان extendedResourceName داده شده است.
اگر یک پاد منبع توسعه‌یافتهٔ `example.com/gpu: 2` را درخواست کند، می‌تواند روی
نودی زمان‌بندی شود که دو دستگاه یا بیشتر منطبق بر این DeviceClass دارد.

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

افزون بر این، کاربران می‌توانند از یک منبع توسعه‌یافتهٔ ویژه استفاده کنند تا بدون
نیاز به ایجاد صریح یک ResourceClaim، دستگاه‌ها را تخصیص دهند. برای این کار، از پیشوند نام منبع توسعه‌یافتهٔ
`deviceclass.resource.kubernetes.io/` به همراه نام DeviceClass استفاده می‌شود.
این روش برای هر DeviceClass کار می‌کند، حتی اگر نام منبع توسعه‌یافته‌ای برای آن تعیین نشده باشد.
ResourceClaim حاصل، درخواستی از نوع `ExactCount` برای
تعداد مشخص‌شده از دستگاه‌های آن DeviceClass خواهد داشت.

تخصیص منابع توسعه‌یافته با DRA با
[feature gate با نام `DRAExtendedResource`](/docs/reference/command-line-tools-reference/feature-gates/#DRAExtendedResource)
در `kube-apiserver`، `kube-scheduler`، `kube-controller-manager` و `kubelet` کنترل می‌شود.

برای یک راهنمای عملی دربارهٔ درخواست منابع توسعه‌یافته، به
[اختصاص منابع توسعه‌یافته به یک کانتینر](/docs/tasks/configure-pod-container/extended-resource/) مراجعه کنید.
