---
title: قیدهای پخش توپولوژی Pod
content_type: concept
weight: 40
---


<!-- overview -->

می‌توانید از _قیدهای پخش توپولوژی_ (topology spread constraints) استفاده کنید تا کنترل کنید
{{< glossary_tooltip text="پادها" term_id="Pod" >}} چگونه در کلاستر شما
میان دامنه‌های خرابی (failure-domain) مانند regionها، zoneها، نودها و سایر دامنه‌های توپولوژی
تعریف‌شده توسط کاربر پخش شوند. این کار می‌تواند به دستیابی به دسترس‌پذیری بالا و نیز بهره‌وری کارآمد
از منابع کمک کند.

می‌توانید [قیدهای سطح کلاستر](#cluster-level-default-constraints) را به‌عنوان پیش‌فرض تنظیم کنید،
یا قیدهای پخش توپولوژی را برای بارهای کاری منفرد پیکربندی کنید.

<!-- body -->

## انگیزه

فرض کنید کلاستری با حداکثر بیست نود دارید و می‌خواهید یک
{{< glossary_tooltip text="بار کاری" term_id="workload" >}}
اجرا کنید که تعداد replicaهای مورد استفادهٔ خود را به‌طور خودکار مقیاس‌بندی می‌کند. تعداد پادها ممکن است
از دو تا پانزده عدد متغیر باشد.
هنگامی که فقط دو Pod وجود دارد، ترجیح می‌دهید هر دوی آن پادها روی یک نود
اجرا نشوند: در غیر این صورت این خطر وجود دارد که خرابی یک نود واحد، بار کاری شما را
از دسترس خارج کند.

علاوه بر این کاربرد پایه، برخی نمونه‌های کاربرد پیشرفته نیز وجود دارد که
بارهای کاری شما را قادر می‌سازد از دسترس‌پذیری بالا و بهره‌وری کلاستر بهره‌مند شوند.

با افزایش مقیاس و اجرای پادهای بیشتر، دغدغهٔ دیگری اهمیت پیدا می‌کند. فرض کنید
سه نود دارید که هر کدام پنج Pod را اجرا می‌کنند. نودها ظرفیت کافی
برای اجرای این تعداد replica دارند؛ با این حال، کلاینت‌هایی که با این بار کاری تعامل دارند
میان سه مرکز داده (یا zone زیرساختی) مختلف تقسیم شده‌اند. اکنون
نگرانی کمتری دربارهٔ خرابی یک نود واحد دارید، اما متوجه می‌شوید که تأخیر (latency)
بیش از حد دلخواه شماست و هزینه‌های شبکهٔ مرتبط با
ارسال ترافیک شبکه میان zoneهای مختلف را پرداخت می‌کنید.

تصمیم می‌گیرید که در شرایط عادی ترجیح می‌دهید تعداد مشابهی replica
در هر zone زیرساختی [زمان‌بندی](/docs/concepts/scheduling-eviction/) شود،
و مایلید کلاستر در صورت بروز مشکل خود را ترمیم کند.

قیدهای پخش توپولوژی Pod روشی اعلانی برای پیکربندی این موضوع در اختیار شما قرار می‌دهند.

## فیلد `topologySpreadConstraints`

API مربوط به Pod شامل فیلدی به نام `spec.topologySpreadConstraints` است. نحوهٔ استفاده از این فیلد
به شکل زیر است:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  # Configure a topology spread constraint
  topologySpreadConstraints:
    - maxSkew: <integer>
      minDomains: <integer> # optional
      topologyKey: <string>
      whenUnsatisfiable: <string>
      labelSelector: <object>
      matchLabelKeys: <list> # optional; beta since v1.27
      nodeAffinityPolicy: [Honor|Ignore] # optional; beta since v1.26
      nodeTaintsPolicy: [Honor|Ignore] # optional; beta since v1.26
  ### other Pod fields go here
```

{{< note >}}
برای هر ترکیب مشخص از `topologyKey` و مقدار `whenUnsatisfiable` تنها یک `topologySpreadConstraint` می‌تواند وجود داشته باشد. برای مثال، اگر یک `topologySpreadConstraint` تعریف کرده باشید که از `topologyKey` با مقدار "kubernetes.io/hostname" و مقدار `whenUnsatisfiable` برابر با "DoNotSchedule" استفاده می‌کند، تنها در صورتی می‌توانید `topologySpreadConstraint` دیگری برای `topologyKey` با مقدار "kubernetes.io/hostname" اضافه کنید که از مقدار متفاوتی برای `whenUnsatisfiable` استفاده کنید.
{{< /note >}}

می‌توانید با اجرای `kubectl explain Pod.spec.topologySpreadConstraints` دربارهٔ این فیلد بیشتر بخوانید یا
به بخش [زمان‌بندی](/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling) در مرجع API مربوط به Pod مراجعه کنید.

### تعریف قید پخش

می‌توانید یک یا چند مدخل `topologySpreadConstraints` تعریف کنید تا به
kube-scheduler دستور دهید هر Pod ورودی را نسبت به پادهای موجود در سراسر
کلاستر چگونه قرار دهد. این فیلدها عبارت‌اند از:

- **maxSkew** میزانی را توصیف می‌کند که پادها می‌توانند به‌طور نابرابر توزیع شوند. شما باید
  این فیلد را مشخص کنید و عدد آن باید بزرگ‌تر از صفر باشد. معنای آن بسته به
  مقدار `whenUnsatisfiable` متفاوت است:

  - اگر `whenUnsatisfiable: DoNotSchedule` را انتخاب کنید، `maxSkew` حداکثر
    اختلاف مجاز میان تعداد پادهای منطبق در توپولوژی هدف
    و _کمینهٔ سراسری_ را تعریف می‌کند
    (کمینهٔ تعداد پادهای منطبق در یک دامنهٔ واجد شرایط، یا صفر اگر تعداد دامنه‌های واجد شرایط کمتر از MinDomains باشد).
    برای مثال، اگر ۳ zone داشته باشید که به ترتیب ۲، ۲ و ۱ پاد منطبق دارند،
    و `MaxSkew` برابر با 1 تنظیم شده باشد، آنگاه کمینهٔ سراسری برابر با 1 است.
  - اگر `whenUnsatisfiable: ScheduleAnyway` را انتخاب کنید، زمان‌بند به توپولوژی‌هایی
    که به کاهش skew کمک می‌کنند اولویت بالاتری می‌دهد.

- **minDomains** کمینهٔ تعداد دامنه‌های واجد شرایط را نشان می‌دهد. این فیلد اختیاری است.
  یک دامنه نمونهٔ مشخصی از یک توپولوژی است. دامنهٔ واجد شرایط دامنه‌ای است که
  نودهای آن با انتخابگر نود منطبق باشند.

  <!-- OK to remove this note once v1.29 Kubernetes is out of support -->
  {{< note >}}
  پیش از کوبرنتیز v1.30، فیلد `minDomains` تنها در صورتی در دسترس بود که
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates-removed/) با نام `MinDomainsInPodTopologySpread`
  فعال بود (که از v1.28 به‌طور پیش‌فرض فعال است). در کلاسترهای قدیمی‌تر کوبرنتیز ممکن است به‌صراحت
  غیرفعال شده باشد یا این فیلد در دسترس نباشد.
  {{< /note >}}

  - مقدار `minDomains` در صورت مشخص شدن باید بزرگ‌تر از 0 باشد.
    تنها می‌توانید `minDomains` را همراه با `whenUnsatisfiable: DoNotSchedule` مشخص کنید.
  - هنگامی که تعداد دامنه‌های واجد شرایط دارای کلیدهای توپولوژی منطبق کمتر از `minDomains` باشد،
    پخش توپولوژی Pod کمینهٔ سراسری را 0 در نظر می‌گیرد و سپس محاسبهٔ `skew` انجام می‌شود.
    کمینهٔ سراسری برابر با کمینهٔ تعداد پادهای منطبق در یک دامنهٔ واجد شرایط است،
    یا صفر اگر تعداد دامنه‌های واجد شرایط کمتر از `minDomains` باشد.
  - هنگامی که تعداد دامنه‌های واجد شرایط دارای کلیدهای توپولوژی منطبق برابر یا بیشتر از
    `minDomains` باشد، این مقدار هیچ تأثیری بر زمان‌بندی ندارد.
  - اگر `minDomains` را مشخص نکنید، قید طوری رفتار می‌کند که گویی `minDomains` برابر با 1 است.

- **topologyKey** کلید [برچسب‌های نود](#node-labels) است. نودهایی که برچسبی با این کلید
	و مقادیر یکسان دارند، در یک توپولوژی در نظر گرفته می‌شوند.
  ما هر نمونه از یک توپولوژی (به عبارت دیگر، یک جفت <key, value>) را یک دامنه می‌نامیم. زمان‌بند
  تلاش می‌کند تعداد متوازنی از پادها را در هر دامنه قرار دهد.
	همچنین، دامنهٔ واجد شرایط را دامنه‌ای تعریف می‌کنیم که نودهای آن الزامات
	nodeAffinityPolicy و nodeTaintsPolicy را برآورده کنند.

- **whenUnsatisfiable** نشان می‌دهد که اگر یک Pod قید پخش را برآورده نکند، چگونه با آن رفتار شود:
  - `DoNotSchedule` (پیش‌فرض) به زمان‌بند می‌گوید آن را زمان‌بندی نکند.
  - `ScheduleAnyway` به زمان‌بند می‌گوید آن را همچنان زمان‌بندی کند و در عین حال به نودهایی که skew را کمینه می‌کنند اولویت دهد.

- **labelSelector** برای یافتن پادهای منطبق استفاده می‌شود. پادهایی
  که با این انتخابگر برچسب منطبق باشند، برای تعیین
  تعداد پادها در دامنهٔ توپولوژی متناظرشان شمرده می‌شوند.
  برای جزئیات بیشتر، به [انتخابگرهای برچسب](/docs/concepts/overview/working-with-objects/labels/#label-selectors)
  مراجعه کنید.

- **matchLabelKeys** فهرستی از کلیدهای برچسب پاد است که برای انتخاب گروهی از پادها به کار می‌رود که
  skew پخش بر روی آن‌ها محاسبه می‌شود. هنگام ایجاد پاد،
  kube-apiserver از این کلیدها برای جست‌وجوی مقادیر در برچسب‌های پاد ورودی استفاده می‌کند،
  و آن برچسب‌های کلید-مقدار با هر `labelSelector` موجود ادغام می‌شوند.
  وجود یک کلید یکسان در هر دوی `matchLabelKeys` و `labelSelector` ممنوع است.
  هنگامی که `labelSelector` تنظیم نشده باشد، نمی‌توان `matchLabelKeys` را تنظیم کرد.
  کلیدهایی که در برچسب‌های پاد وجود ندارند نادیده گرفته می‌شوند.
  یک فهرست null یا خالی به این معناست که تطبیق فقط بر اساس `labelSelector` انجام می‌شود.

  {{< caution >}}
  استفاده از `matchLabelKeys` با برچسب‌هایی که ممکن است مستقیماً روی پادها به‌روزرسانی شوند توصیه نمی‌شود.
  حتی اگر برچسب پادی را که در `matchLabelKeys` مشخص شده است **مستقیماً** ویرایش کنید
  (یعنی Pod را ویرایش کنید و نه یک Deployment را)،
  kube-apiserver به‌روزرسانی برچسب را در `labelSelector` ادغام‌شده منعکس نمی‌کند.
  {{< /caution >}}

  با `matchLabelKeys`، نیازی به به‌روزرسانی `pod.spec` میان بازبینی‌های (revision) مختلف ندارید.
  کنترل‌کننده/اپراتور فقط کافی است برای بازبینی‌های مختلف، مقادیر متفاوتی را به یک کلید برچسب یکسان
  اختصاص دهد. برای مثال، اگر یک Deployment را پیکربندی می‌کنید، می‌توانید از برچسبی با کلید
  [pod-template-hash](/docs/concepts/workloads/controllers/deployment/#pod-template-hash-label) استفاده کنید که
  به‌طور خودکار توسط کنترل‌کنندهٔ Deployment اضافه می‌شود تا میان بازبینی‌های مختلف
  در یک Deployment واحد تمایز قائل شوید.

  ```yaml
      topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: DoNotSchedule
            labelSelector:
              matchLabels:
                app: foo
            matchLabelKeys:
              - pod-template-hash
  ```

  {{< note >}}
  فیلد `matchLabelKeys` یک فیلد در سطح بتا است و در 1.27 به‌طور پیش‌فرض فعال است. می‌توانید آن را با غیرفعال کردن
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `MatchLabelKeysInPodTopologySpread` غیرفعال کنید.

  پیش از v1.34، `matchLabelKeys` به‌صورت ضمنی مدیریت می‌شد.
  از v1.34 به بعد، برچسب‌های کلید-مقدار متناظر با `matchLabelKeys` به‌صراحت در `labelSelector` ادغام می‌شوند.
  می‌توانید این رفتار را غیرفعال کرده و با غیرفعال کردن
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `MatchLabelKeysInPodTopologySpreadSelectorMerge` در kube-apiserver به رفتار پیشین بازگردید.
  {{< /note >}}

- **nodeAffinityPolicy** نشان می‌دهد که هنگام محاسبهٔ skew پخش توپولوژی پاد،
  با nodeAffinity/nodeSelector پاد چگونه رفتار خواهیم کرد. گزینه‌ها عبارت‌اند از:
  - Honor: فقط نودهای منطبق با nodeAffinity/nodeSelector در محاسبات گنجانده می‌شوند.
  - Ignore: nodeAffinity/nodeSelector نادیده گرفته می‌شوند. همهٔ نودها در محاسبات گنجانده می‌شوند.

  اگر این مقدار null باشد، رفتار معادل سیاست Honor است.

  {{< note >}}
  `nodeAffinityPolicy` در 1.26 به مرحلهٔ بتا رسید و در 1.33 به GA ارتقا یافت.
  این قابلیت در مرحلهٔ بتا به‌طور پیش‌فرض فعال است و می‌توانید آن را با غیرفعال کردن
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `NodeInclusionPolicyInPodTopologySpread` غیرفعال کنید.
  {{< /note >}}

- **nodeTaintsPolicy** نشان می‌دهد که هنگام محاسبهٔ skew پخش توپولوژی پاد،
  با taintهای نود چگونه رفتار خواهیم کرد. گزینه‌ها عبارت‌اند از:
  - Honor: نودهای بدون taint، به همراه نودهای دارای taint که پاد ورودی
    برای آن‌ها toleration دارد، گنجانده می‌شوند.
  - Ignore: taintهای نود نادیده گرفته می‌شوند. همهٔ نودها گنجانده می‌شوند.

  اگر این مقدار null باشد، رفتار معادل سیاست Ignore است.

  {{< note >}}
  `nodeTaintsPolicy` در 1.26 به مرحلهٔ بتا رسید و در 1.33 به GA ارتقا یافت.
  این قابلیت در مرحلهٔ بتا به‌طور پیش‌فرض فعال است و می‌توانید آن را با غیرفعال کردن
  [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) با نام `NodeInclusionPolicyInPodTopologySpread` غیرفعال کنید.
  {{< /note >}}

هنگامی که یک Pod بیش از یک `topologySpreadConstraint` تعریف کند، این قیدها
با استفاده از عملگر منطقی AND ترکیب می‌شوند: kube-scheduler برای Pod ورودی به دنبال نودی می‌گردد
که همهٔ قیدهای پیکربندی‌شده را برآورده کند.

### برچسب‌های نود

قیدهای پخش توپولوژی برای شناسایی دامنه(های) توپولوژی‌ای که هر {{< glossary_tooltip text="نود" term_id="node" >}}
در آن قرار دارد، به برچسب‌های نود متکی هستند.
برای مثال، یک نود ممکن است این برچسب‌ها را داشته باشد:
```yaml
  region: us-east-1
  zone: us-east-1a
```

{{< note >}}
برای اختصار، این مثال از کلیدهای برچسب
[شناخته‌شده](/docs/reference/labels-annotations-taints/)
`topology.kubernetes.io/zone` و `topology.kubernetes.io/region` استفاده نمی‌کند. با این حال،
آن کلیدهای برچسب ثبت‌شده همچنان به کلیدهای برچسب خصوصی
(بدون پیشوند) `region` و `zone` که در اینجا استفاده شده‌اند، ترجیح داده می‌شوند.

نمی‌توانید فرض قابل اتکایی دربارهٔ معنای یک کلید برچسب خصوصی
در زمینه‌های مختلف داشته باشید.
{{< /note >}}

فرض کنید یک کلاستر ۴ نودی با برچسب‌های زیر دارید:

```
NAME    STATUS   ROLES    AGE     VERSION   LABELS
node1   Ready    <none>   4m26s   v1.16.0   node=node1,zone=zoneA
node2   Ready    <none>   3m58s   v1.16.0   node=node2,zone=zoneA
node3   Ready    <none>   3m17s   v1.16.0   node=node3,zone=zoneB
node4   Ready    <none>   2m43s   v1.16.0   node=node4,zone=zoneB
```

در این صورت، کلاستر از نظر منطقی به شکل زیر دیده می‌شود:

{{<mermaid>}}
graph TB
    subgraph "zoneB"
        n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        n1(Node1)
        n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4 k8s;
    class zoneA,zoneB cluster;
{{< /mermaid >}}

## سازگاری

باید قیدهای پخش توپولوژی Pod یکسانی را روی همهٔ پادهای یک گروه تنظیم کنید.

معمولاً اگر از یک کنترل‌کنندهٔ بار کاری مانند Deployment استفاده می‌کنید، قالب پاد
این کار را برای شما انجام می‌دهد. اگر قیدهای پخش متفاوتی را با هم ترکیب کنید، کوبرنتیز
از تعریف API فیلد پیروی می‌کند؛ با این حال، احتمال بیشتری وجود دارد که رفتار
گیج‌کننده شود و عیب‌یابی آن کمتر سرراست باشد.

به سازوکاری نیاز دارید تا اطمینان حاصل کنید همهٔ نودهای یک دامنهٔ توپولوژی (مانند یک
region ارائه‌دهندهٔ ابری) به‌طور یکنواخت برچسب‌گذاری شده‌اند.
برای اینکه نیازی به برچسب‌گذاری دستی نودها نداشته باشید، بیشتر کلاسترها به‌طور خودکار
برچسب‌های شناخته‌شده‌ای مانند `kubernetes.io/hostname` را مقداردهی می‌کنند. بررسی کنید که آیا
کلاستر شما از این قابلیت پشتیبانی می‌کند یا خیر.

## نمونه‌های قید پخش توپولوژی

### مثال: یک قید پخش توپولوژی {#example-one-topologyspreadconstraint}

فرض کنید یک کلاستر ۴ نودی دارید که در آن ۳ Pod با برچسب `foo: bar` به ترتیب روی
node1، node2 و node3 قرار دارند:

{{<mermaid>}}
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class zoneA,zoneB cluster;
{{< /mermaid >}}

اگر می‌خواهید یک Pod ورودی به‌طور یکنواخت همراه با پادهای موجود در میان zoneها پخش شود،
می‌توانید از مانیفستی مشابه زیر استفاده کنید:

{{% code_sample file="pods/topology-spread-constraints/one-constraint.yaml" %}}

بر اساس این مانیفست، `topologyKey: zone` به این معناست که توزیع یکنواخت فقط بر
نودهایی اعمال می‌شود که برچسب `zone: <any value>` دارند (نودهایی که برچسب `zone`
ندارند نادیده گرفته می‌شوند). فیلد `whenUnsatisfiable: DoNotSchedule` به زمان‌بند می‌گوید
اگر نتوانست راهی برای برآورده کردن قید بیابد، اجازه دهد Pod ورودی در وضعیت pending باقی بماند.

اگر زمان‌بند این Pod ورودی را در zone `A` قرار می‌داد، توزیع پادها
به `[3, 1]` تبدیل می‌شد. این یعنی skew واقعی برابر با 2 (محاسبه‌شده به‌صورت `3 - 1`) می‌شد که
`maxSkew: 1` را نقض می‌کند. برای برآورده کردن قیدها و شرایط این مثال،
Pod ورودی فقط می‌تواند روی نودی در zone `B` قرار گیرد:

{{<mermaid>}}
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        p4(mypod) --> n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;
{{< /mermaid >}}

یا

{{<mermaid>}}
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        p4(mypod) --> n3
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;
{{< /mermaid >}}

می‌توانید spec مربوط به Pod را برای برآورده کردن انواع مختلف الزامات تنظیم کنید:

- `maxSkew` را به مقدار بزرگ‌تری، مانند `2`، تغییر دهید تا Pod ورودی بتواند
  در zone `A` نیز قرار گیرد.
- `topologyKey` را به `node` تغییر دهید تا پادها به‌جای zoneها به‌طور یکنواخت
  میان نودها توزیع شوند. در مثال بالا، اگر `maxSkew` برابر با `1` باقی بماند، Pod ورودی
  فقط می‌تواند روی نود `node4` قرار گیرد.
- `whenUnsatisfiable: DoNotSchedule` را به `whenUnsatisfiable: ScheduleAnyway` تغییر دهید
  تا اطمینان حاصل شود که Pod ورودی همیشه قابل زمان‌بندی است (با فرض اینکه سایر APIهای زمان‌بندی
  برآورده شده باشند). با این حال، ترجیح داده می‌شود که در دامنهٔ توپولوژی‌ای قرار گیرد که
  پادهای منطبق کمتری دارد. (توجه داشته باشید که این ترجیح به‌طور مشترک
  با سایر اولویت‌های داخلی زمان‌بندی، مانند نسبت استفاده از منابع، نرمال‌سازی می‌شود).

### مثال: چند قید پخش توپولوژی {#example-multiple-topologyspreadconstraints}

این مثال بر پایهٔ مثال قبلی بنا شده است. فرض کنید یک کلاستر ۴ نودی دارید که در آن ۳
Pod موجود با برچسب `foo: bar` به ترتیب روی node1، node2 و node3 قرار دارند:

{{<mermaid>}}
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;
{{< /mermaid >}}

می‌توانید دو قید پخش توپولوژی را ترکیب کنید تا پخش پادها را هم
بر اساس نود و هم بر اساس zone کنترل کنید:

{{% code_sample file="pods/topology-spread-constraints/two-constraints.yaml" %}}

در این حالت، برای انطباق با قید اول، Pod ورودی فقط می‌تواند روی
نودهای zone `B` قرار گیرد؛ در حالی که از نظر قید دوم، Pod ورودی فقط می‌تواند
روی نود `node4` زمان‌بندی شود. زمان‌بند فقط گزینه‌هایی را در نظر می‌گیرد که همهٔ
قیدهای تعریف‌شده را برآورده کنند، بنابراین تنها جای‌گذاری معتبر روی نود `node4` است.

### مثال: قیدهای پخش توپولوژی متعارض {#example-conflicting-topologyspreadconstraints}

چندین قید می‌توانند به تعارض منجر شوند. فرض کنید یک کلاستر ۳ نودی دارید که در ۲ zone گسترده شده است:

{{<mermaid>}}
graph BT
    subgraph "zoneB"
        p4(Pod) --> n3(Node3)
        p5(Pod) --> n3
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n1
        p3(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3,p4,p5 k8s;
    class zoneA,zoneB cluster;
{{< /mermaid >}}

اگر
[`two-constraints.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/topology-spread-constraints/two-constraints.yaml)
(مانیفست مثال قبلی) را
روی **این** کلاستر اعمال کنید، خواهید دید که Pod با نام `mypod` در وضعیت `Pending` باقی می‌ماند.
دلیل این امر آن است که: برای برآورده کردن قید اول، Pod با نام `mypod` فقط می‌تواند
در zone `B` قرار گیرد؛ در حالی که از نظر قید دوم، Pod با نام `mypod`
فقط می‌تواند روی نود `node2` زمان‌بندی شود. اشتراک این دو قید
یک مجموعهٔ تهی است و زمان‌بند نمی‌تواند Pod را جای‌گذاری کند.

برای غلبه بر این وضعیت، می‌توانید مقدار `maxSkew` را افزایش دهید یا
یکی از قیدها را طوری تغییر دهید که از `whenUnsatisfiable: ScheduleAnyway` استفاده کند. بسته به
شرایط، ممکن است تصمیم بگیرید یک Pod موجود را به‌صورت دستی حذف کنید؛ برای مثال،
اگر در حال عیب‌یابی این موضوع هستید که چرا انتشار (rollout) یک رفع اشکال پیش نمی‌رود.

#### تعامل با وابستگی نود و انتخابگرهای نود

اگر Pod ورودی دارای `spec.nodeSelector` یا `spec.affinity.nodeAffinity` تعریف‌شده باشد،
زمان‌بند نودهای غیرمنطبق را از محاسبات skew کنار می‌گذارد.

### مثال: قیدهای پخش توپولوژی همراه با وابستگی نود {#example-topologyspreadconstraints-with-nodeaffinity}

فرض کنید یک کلاستر ۵ نودی دارید که در zoneهای A تا C گسترده شده است:

{{<mermaid>}}
graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
class n1,n2,n3,n4,p1,p2,p3 k8s;
class p4 plain;
class zoneA,zoneB cluster;
{{< /mermaid >}}

{{<mermaid>}}
graph BT
    subgraph "zoneC"
        n5(Node5)
    end

classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
class n5 k8s;
class zoneC cluster;
{{< /mermaid >}}

و می‌دانید که zone `C` باید مستثنا شود. در این حالت، می‌توانید مانیفستی
مانند زیر بنویسید تا Pod با نام `mypod` به‌جای zone `C` در zone `B` قرار گیرد.
به همین ترتیب، کوبرنتیز `spec.nodeSelector` را نیز رعایت می‌کند.

{{% code_sample file="pods/topology-spread-constraints/one-constraint-with-nodeaffinity.yaml" %}}

## قراردادهای ضمنی

برخی قراردادهای ضمنی وجود دارد که در اینجا ارزش توجه دارند:

- فقط پادهایی که در همان فضای نام (namespace) Pod ورودی قرار دارند می‌توانند نامزدهای منطبق باشند.

- زمان‌بند فقط نودهایی را در نظر می‌گیرد که همهٔ `topologySpreadConstraints[*].topologyKey` را به‌طور هم‌زمان داشته باشند.
  نودهایی که هر یک از این `topologyKeys` را نداشته باشند کنار گذاشته می‌شوند. این به آن معناست که:

  1. هیچ یک از پادهای واقع روی آن نودهای کنارگذاشته‌شده بر محاسبهٔ `maxSkew` تأثیر نمی‌گذارند؛ در
     [مثال](#example-conflicting-topologyspreadconstraints) بالا، فرض کنید نود `node1`
     برچسب "zone" نداشته باشد، در این صورت آن ۲ Pod
     نادیده گرفته می‌شوند و بنابراین Pod ورودی در zone `A` زمان‌بندی خواهد شد.
  2. Pod ورودی هیچ شانسی برای زمان‌بندی روی این نوع نودها ندارد؛
     در مثال بالا، فرض کنید نود `node5` برچسبی با **غلط تایپی** به‌صورت `zone-typo: zoneC` داشته باشد
     (و هیچ برچسب `zone` تنظیم نشده باشد). پس از پیوستن نود `node5` به کلاستر، این نود کنار گذاشته می‌شود و
     پادهای این بار کاری روی آن زمان‌بندی نمی‌شوند.

- آگاه باشید که اگر `topologySpreadConstraints[*].labelSelector` در Pod ورودی
  با برچسب‌های خود آن منطبق نباشد، چه اتفاقی می‌افتد. در
  مثال بالا، اگر برچسب‌های Pod ورودی را حذف کنید، همچنان می‌تواند روی
  نودهای zone `B` قرار گیرد، زیرا قیدها همچنان برآورده می‌شوند. با این حال، پس از این
  جای‌گذاری، میزان عدم توازن کلاستر بدون تغییر باقی می‌ماند؛ همچنان zone `A`
  دارای ۲ Pod با برچسب `foo: bar` و zone `B` دارای ۱ Pod با برچسب
  `foo: bar` است. اگر این آن چیزی نیست که انتظار دارید،
  `topologySpreadConstraints[*].labelSelector` بار کاری را به‌روزرسانی کنید تا با برچسب‌های قالب پاد منطبق شود.

## قیدهای پیش‌فرض سطح کلاستر

می‌توان قیدهای پخش توپولوژی پیش‌فرضی را برای یک کلاستر تنظیم کرد. قیدهای پخش
توپولوژی پیش‌فرض تنها و تنها در صورتی بر یک Pod اعمال می‌شوند که:

- هیچ قیدی در `.spec.topologySpreadConstraints` خود تعریف نکرده باشد.
- به یک Service، ReplicaSet، StatefulSet یا ReplicationController تعلق داشته باشد.

قیدهای پیش‌فرض را می‌توان به‌عنوان بخشی از آرگومان‌های افزونهٔ `PodTopologySpread`
در یک [پروفایل زمان‌بندی](/docs/reference/scheduling/config/#profiles) تنظیم کرد.
این قیدها با همان [API بالا](#topologyspreadconstraints-field) مشخص می‌شوند، با این تفاوت که
`labelSelector` باید خالی باشد. انتخابگرها از Serviceها،
ReplicaSetها، StatefulSetها یا ReplicationControllerهایی که Pod به آن‌ها تعلق دارد محاسبه می‌شوند.

یک پیکربندی نمونه ممکن است به شکل زیر باشد:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration

profiles:
  - schedulerName: default-scheduler
    pluginConfig:
      - name: PodTopologySpread
        args:
          defaultConstraints:
            - maxSkew: 1
              topologyKey: topology.kubernetes.io/zone
              whenUnsatisfiable: ScheduleAnyway
          defaultingType: List
```
### قیدهای پیش‌فرض داخلی {#internal-default-constraints}

{{< feature-state for_k8s_version="v1.24" state="stable" >}}

اگر هیچ قید پیش‌فرض سطح کلاستری برای پخش توپولوژی پاد پیکربندی نکنید،
kube-scheduler طوری عمل می‌کند که گویی قیدهای توپولوژی پیش‌فرض زیر را مشخص کرده‌اید:

```yaml
defaultConstraints:
  - maxSkew: 3
    topologyKey: "kubernetes.io/hostname"
    whenUnsatisfiable: ScheduleAnyway
  - maxSkew: 5
    topologyKey: "topology.kubernetes.io/zone"
    whenUnsatisfiable: ScheduleAnyway
```

همچنین، افزونهٔ قدیمی `SelectorSpread` که رفتاری معادل ارائه می‌دهد،
به‌طور پیش‌فرض غیرفعال است.

{{< note >}}
افزونهٔ `PodTopologySpread` به نودهایی که کلیدهای توپولوژی مشخص‌شده در قیدهای پخش را
ندارند امتیاز نمی‌دهد. این امر ممکن است هنگام استفاده از قیدهای توپولوژی پیش‌فرض
به رفتار پیش‌فرض متفاوتی در مقایسه با افزونهٔ قدیمی `SelectorSpread` منجر شود.

اگر انتظار نمی‌رود نودهای شما **هر دو** برچسب `kubernetes.io/hostname` و
`topology.kubernetes.io/zone` را داشته باشند، به‌جای استفاده از پیش‌فرض‌های کوبرنتیز،
قیدهای خودتان را تعریف کنید.
{{< /note >}}

اگر نمی‌خواهید از قیدهای پخش پیش‌فرض Pod برای کلاستر خود استفاده کنید،
می‌توانید با تنظیم `defaultingType` به `List` و خالی گذاشتن
`defaultConstraints` در پیکربندی افزونهٔ `PodTopologySpread`، این پیش‌فرض‌ها را غیرفعال کنید:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration

profiles:
  - schedulerName: default-scheduler
    pluginConfig:
      - name: PodTopologySpread
        args:
          defaultConstraints: []
          defaultingType: List
```

## مقایسه با podAffinity و podAntiAffinity {#comparison-with-podaffinity-podantiaffinity}

در کوبرنتیز، [وابستگی و ضدوابستگی میان پادها (inter-Pod affinity and anti-affinity)](/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)
کنترل می‌کنند که پادها نسبت به یکدیگر چگونه زمان‌بندی شوند؛ یا متراکم‌تر
یا پراکنده‌تر.

`podAffinity`
: پادها را جذب می‌کند؛ می‌توانید تلاش کنید هر تعداد پاد را در دامنه(های)
  توپولوژی واجد شرایط متراکم کنید.

`podAntiAffinity`
: پادها را دفع می‌کند. اگر آن را روی حالت `requiredDuringSchedulingIgnoredDuringExecution` تنظیم کنید،
  فقط یک Pod می‌تواند در یک دامنهٔ توپولوژی واحد زمان‌بندی شود؛ اگر
  `preferredDuringSchedulingIgnoredDuringExecution` را انتخاب کنید، توانایی اعمال اجباری
  قید را از دست می‌دهید.

برای کنترل دقیق‌تر، می‌توانید قیدهای پخش توپولوژی را برای توزیع
پادها در دامنه‌های توپولوژی مختلف مشخص کنید تا به دسترس‌پذیری بالا یا
صرفه‌جویی در هزینه دست یابید. این کار همچنین می‌تواند به به‌روزرسانی تدریجی (rolling update) بارهای کاری و افزایش مقیاس
replicaها به‌صورت روان کمک کند.

برای زمینهٔ بیشتر، بخش
[انگیزه](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/895-pod-topology-spread#motivation)
در پیشنهاد بهبود (enhancement proposal) مربوط به قیدهای پخش توپولوژی Pod را ببینید.

## محدودیت‌های شناخته‌شده

- هیچ تضمینی وجود ندارد که قیدها هنگام حذف پادها همچنان برآورده بمانند. برای
  مثال، کاهش مقیاس یک Deployment ممکن است به توزیع نامتوازن پادها منجر شود.

  می‌توانید از ابزاری مانند [Descheduler](https://github.com/kubernetes-sigs/descheduler)
  برای متوازن کردن دوبارهٔ توزیع پادها استفاده کنید.
- پادهای منطبق روی نودهای دارای taint نیز در نظر گرفته می‌شوند.
  به [Issue 80921](https://github.com/kubernetes/kubernetes/issues/80921) مراجعه کنید.
- زمان‌بند از پیش از همهٔ zoneها یا سایر دامنه‌های توپولوژی‌ای که یک کلاستر دارد
  اطلاع ندارد. این دامنه‌ها از روی نودهای موجود در
  کلاستر تعیین می‌شوند. این موضوع می‌تواند در کلاسترهای دارای مقیاس‌بندی خودکار مشکل‌ساز شود، هنگامی که یک node pool (یا
  node group) به صفر نود کاهش مقیاس یافته باشد و انتظار داشته باشید کلاستر افزایش مقیاس یابد،
  زیرا در این حالت، آن دامنه‌های توپولوژی تا زمانی که دست‌کم یک نود در آن‌ها
  وجود نداشته باشد در نظر گرفته نمی‌شوند.

  می‌توانید با استفاده از یک مقیاس‌دهندهٔ خودکار نود (Node autoscaler) که از
  قیدهای پخش توپولوژی Pod و نیز از مجموعهٔ کلی دامنه‌های توپولوژی آگاه است،
  این مشکل را دور بزنید.
- پادهایی که با labelSelector خودشان منطبق نیستند، «پادهای شبح» (ghost pods) ایجاد می‌کنند. اگر
  برچسب‌های یک پاد با `labelSelector` در قید پخش توپولوژی آن منطبق نباشند، آن پاد
  خودش را در محاسبات پخش به حساب نمی‌آورد. این به آن معناست که:
  - چندین پاد از این نوع ممکن است به‌سادگی روی یک توپولوژی انباشته شوند (تا زمانی که پادهای منطبق تازه ایجاد یا حذف شوند)، زیرا زمان‌بندی این پادها نتیجهٔ محاسبهٔ پخش را تغییر نمی‌دهد.
  - قید پخش به شیوه‌ای ناخواسته عمل می‌کند که به احتمال زیاد با انتظارات شما مطابقت ندارد

  اطمینان حاصل کنید که برچسب‌های پاد شما با `labelSelector` در قیدهای پخش منطبق هستند.
  معمولاً یک پاد باید با انتخابگر قید پخش توپولوژی خودش منطبق باشد.

## {{% heading "whatsnext" %}}

- مقالهٔ وبلاگ [معرفی PodTopologySpread](/blog/2020/05/introducing-podtopologyspread/)
  `maxSkew` را با جزئیاتی توضیح می‌دهد و برخی نمونه‌های کاربرد پیشرفته را نیز پوشش می‌دهد.
- بخش [زمان‌بندی](/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling) در
  مرجع API مربوط به Pod را مطالعه کنید.
