---
reviewers:
- davidopp
- kevin-wangzefeng
- bsalamat
title: Taintها و Tolerationها
content_type: concept
weight: 50
---


<!-- overview -->
[_وابستگی نود (Node affinity)_](/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
ویژگی‌ای از {{< glossary_tooltip text="پادها" term_id="pod" >}} است که آن‌ها را به‌سوی
مجموعه‌ای از {{< glossary_tooltip text="نودها" term_id="node" >}} *جذب* می‌کند (یا به‌صورت یک ترجیح یا به‌صورت یک
الزام سخت). _Taintها_ عکس این عمل می‌کنند؛ آن‌ها به یک نود اجازه می‌دهند مجموعه‌ای از پادها را دفع کند.

_Tolerationها_ بر پادها اعمال می‌شوند. Tolerationها به زمان‌بند اجازه می‌دهند پادها را روی نودهایی با taintهای منطبق
زمان‌بندی کند. Tolerationها زمان‌بندی را مجاز می‌کنند اما آن را تضمین نمی‌کنند: زمان‌بند به‌عنوان بخشی از کار خود
[پارامترهای دیگری را نیز ارزیابی می‌کند](/docs/concepts/scheduling-eviction/pod-priority-preemption/).

Taintها و tolerationها با هم کار می‌کنند تا اطمینان حاصل شود که پادها روی
نودهای نامناسب زمان‌بندی نمی‌شوند. یک یا چند taint بر یک نود اعمال می‌شود؛ این کار
مشخص می‌کند که نود نباید هیچ پادی را که آن taintها را تحمل نمی‌کند بپذیرد.

<!-- body -->

## مفاهیم

شما با استفاده از [kubectl taint](/docs/reference/generated/kubectl/kubectl-commands#taint) یک taint به نود اضافه می‌کنید.
برای مثال،

```shell
kubectl taint nodes node1 key1=value1:NoSchedule
```

یک taint روی نود `node1` قرار می‌دهد. این taint دارای کلید `key1`، مقدار `value1` و اثر taint برابر با `NoSchedule` است.
این به آن معناست که هیچ پادی نمی‌تواند روی `node1` زمان‌بندی شود، مگر اینکه toleration منطبقی داشته باشد.

برای حذف taint اضافه‌شده توسط دستور بالا، می‌توانید این دستور را اجرا کنید:

```shell
kubectl taint nodes node1 key1=value1:NoSchedule-
```

شما toleration یک پاد را در PodSpec مشخص می‌کنید. هر دو toleration زیر با
taint ایجادشده توسط خط `kubectl taint` بالا «منطبق» هستند، و بنابراین پادی که هر یک از این tolerationها را داشته باشد
می‌تواند روی `node1` زمان‌بندی شود:

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
```

```yaml
tolerations:
- key: "key1"
  operator: "Exists"
  effect: "NoSchedule"
```

زمان‌بند پیش‌فرض کوبرنتیز هنگام انتخاب نودی برای اجرای یک Pod مشخص،
taintها و tolerationها را در نظر می‌گیرد. با این حال، اگر `.spec.nodeName` یک Pod را به‌صورت دستی
مشخص کنید، این کار زمان‌بند را دور می‌زند؛ در این صورت Pod به نودی که آن را به آن اختصاص داده‌اید
متصل (bind) می‌شود، حتی اگر روی آن نود انتخاب‌شده taintهای `NoSchedule` وجود داشته باشد.
اگر چنین اتفاقی بیفتد و نود یک taint از نوع `NoExecute` نیز داشته باشد، kubelet
آن Pod را بیرون می‌کند، مگر اینکه toleration مناسبی تنظیم شده باشد.

در اینجا نمونه‌ای از یک پاد را می‌بینید که چند toleration برای آن تعریف شده است:

{{% code_sample file="pods/pod-with-toleration.yaml" %}}

مقدار پیش‌فرض `operator` برابر با `Equal` است.

یک toleration زمانی با یک taint «منطبق» است که کلیدها یکسان و اثرها نیز یکسان باشند، و:

* `operator` برابر با `Exists` باشد (که در این حالت نباید هیچ `value` مشخص شود)، یا
* `operator` برابر با `Equal` باشد و مقدارها با هم برابر باشند.

{{< note >}}

دو حالت خاص وجود دارد:

اگر `key` خالی باشد، `operator` باید `Exists` باشد که با همهٔ کلیدها و مقدارها منطبق می‌شود.
توجه داشته باشید که `effect` همچنان باید هم‌زمان منطبق شود.

یک `effect` خالی با همهٔ اثرهای دارای کلید `key1` منطبق می‌شود.

{{< /note >}}

مثال بالا از `effect` با مقدار `NoSchedule` استفاده کرد. به‌عنوان جایگزین، می‌توانید از `effect` با مقدار `PreferNoSchedule` استفاده کنید.

مقادیر مجاز برای فیلد `effect` عبارت‌اند از:

`NoExecute`
: این اثر بر پادهایی که هم‌اکنون روی نود در حال اجرا هستند به شرح زیر تأثیر می‌گذارد:

  * پادهایی که taint را تحمل نمی‌کنند، بلافاصله بیرون رانده (evict) می‌شوند
  * پادهایی که taint را تحمل می‌کنند بدون آنکه `tolerationSeconds` را در
    مشخصات toleration خود تعیین کرده باشند، برای همیشه متصل باقی می‌مانند
  * پادهایی که taint را با یک `tolerationSeconds` مشخص تحمل می‌کنند، به مدت زمان
    تعیین‌شده متصل باقی می‌مانند. پس از سپری شدن این زمان،
    کنترل‌کنندهٔ چرخهٔ حیات نود پادها را از نود بیرون می‌راند.

`NoSchedule`
: هیچ Pod جدیدی روی نود دارای taint زمان‌بندی نمی‌شود، مگر اینکه toleration منطبقی
  داشته باشد. پادهایی که هم‌اکنون روی نود در حال اجرا هستند بیرون رانده **نمی‌شوند**.

`PreferNoSchedule`
: `PreferNoSchedule` نسخهٔ «ترجیحی» یا «نرم» `NoSchedule` است.
  control plane *تلاش می‌کند* از قرار دادن Podی که taint را تحمل نمی‌کند
  روی نود خودداری کند، اما این امر تضمین‌شده نیست.

می‌توانید چندین taint روی یک نود و چندین toleration روی یک پاد قرار دهید.
روشی که کوبرنتیز چندین taint و toleration را پردازش می‌کند مانند یک فیلتر است: کار
با همهٔ taintهای یک نود آغاز می‌شود، سپس taintهایی که پاد toleration منطبقی برای آن‌ها دارد نادیده گرفته می‌شوند؛
taintهای باقی‌مانده که نادیده گرفته نشده‌اند، اثرهای مشخص‌شدهٔ خود را بر پاد اعمال می‌کنند. به‌طور خاص،

* اگر دست‌کم یک taint نادیده‌گرفته‌نشده با اثر `NoSchedule` وجود داشته باشد، کوبرنتیز پاد را
روی آن نود زمان‌بندی نمی‌کند
* اگر هیچ taint نادیده‌گرفته‌نشده‌ای با اثر `NoSchedule` وجود نداشته باشد، اما دست‌کم یک taint نادیده‌گرفته‌نشده با
اثر `PreferNoSchedule` وجود داشته باشد، کوبرنتیز *تلاش می‌کند* پاد را روی آن نود زمان‌بندی نکند
* اگر دست‌کم یک taint نادیده‌گرفته‌نشده با اثر `NoExecute` وجود داشته باشد، پاد از
نود بیرون رانده می‌شود (اگر هم‌اکنون روی نود در حال اجرا باشد) و روی
نود زمان‌بندی نمی‌شود (اگر هنوز روی نود در حال اجرا نباشد).

برای مثال، فرض کنید نودی را به این شکل taint کنید

```shell
kubectl taint nodes node1 key1=value1:NoSchedule
kubectl taint nodes node1 key1=value1:NoExecute
kubectl taint nodes node1 key2=value2:NoSchedule
```

و یک پاد دو toleration داشته باشد:

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoExecute"
```

در این حالت، پاد نمی‌تواند روی نود زمان‌بندی شود، زیرا هیچ
tolerationی منطبق با taint سوم وجود ندارد. اما اگر هنگام اضافه شدن taint
از قبل روی نود در حال اجرا باشد، می‌تواند به اجرای خود ادامه دهد، زیرا taint سوم تنها
taint از میان این سه است که توسط پاد تحمل نمی‌شود.

به‌طور معمول، اگر taintی با اثر `NoExecute` به یک نود اضافه شود، هر پادی که
آن taint را تحمل نکند بلافاصله بیرون رانده می‌شود، و پادهایی که آن taint را تحمل می‌کنند
هرگز بیرون رانده نمی‌شوند. با این حال، یک toleration با اثر `NoExecute` می‌تواند
فیلد اختیاری `tolerationSeconds` را مشخص کند که تعیین می‌کند پاد پس از اضافه شدن taint
چه مدت به نود متصل باقی بماند. برای مثال،

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoExecute"
  tolerationSeconds: 3600
```

به این معناست که اگر این پاد در حال اجرا باشد و taint منطبقی به نود اضافه شود،
پاد به مدت ۳۶۰۰ ثانیه به نود متصل باقی می‌ماند و سپس بیرون رانده می‌شود. اگر
taint پیش از پایان این زمان حذف شود، پاد بیرون رانده نخواهد شد.

## عملگرهای مقایسهٔ عددی {#numeric-comparison-operators}

{{< feature-state feature_gate_name="TaintTolerationComparisonOperators" >}}

علاوه بر `Equal` و `Exists`، می‌توانید از عملگرهای مقایسهٔ عددی
(`Gt` و `Lt`) برای تطبیق taintهایی با مقادیر صحیح استفاده کنید. این قابلیت برای زمان‌بندی مبتنی بر آستانه،
مانند تطبیق نودها بر اساس سطح قابلیت اطمینان یا ردهٔ SLA، مفید است.

* `Gt` زمانی منطبق می‌شود که مقدار taint بزرگ‌تر از مقدار toleration باشد.
* `Lt` زمانی منطبق می‌شود که مقدار taint کوچک‌تر از مقدار toleration باشد.

برای عملگرهای عددی، هم مقدار toleration و هم مقدار taint باید اعداد صحیح معتبر باشند.
اگر هر یک از این مقادیر قابل تجزیه به عدد صحیح نباشد، toleration منطبق نمی‌شود.

{{< note >}}
هنگامی که Podی ایجاد می‌کنید که از عملگرهای toleration از نوع `Gt` یا `Lt` استفاده می‌کند، API server اعتبارسنجی می‌کند که
مقادیر toleration اعداد صحیح معتبری باشند. مقادیر taint روی نودها در زمان ثبت نود
اعتبارسنجی نمی‌شوند. اگر نودی مقدار taint غیرعددی داشته باشد (برای مثال،
`servicelevel.organization.example/agreed-service-level=high:NoSchedule`)،
پادهایی که از عملگرهای مقایسهٔ عددی استفاده می‌کنند با آن taint منطبق نمی‌شوند و نمی‌توانند روی آن نود زمان‌بندی شوند.
{{< /note >}}

برای مثال، اگر نودها با مقداری که نمایانگر توافق‌نامهٔ سطح خدمات (SLA) است taint شده باشند:

```shell
kubectl taint nodes node1 servicelevel.organization.example/agreed-service-level=950:NoSchedule
```

یک پاد می‌تواند نودهایی با SLA بزرگ‌تر از ۹۰۰ را تحمل کند:

{{% code_sample file="pods/pod-with-numeric-toleration.yaml" %}}

این toleration با taint روی `node1` منطبق است، زیرا `950 > 900` (برای عملگر `Gt`، مقدار taint  
بزرگ‌تر از مقدار toleration است).  
به همین ترتیب، می‌توانید از عملگر `Lt` برای تطبیق taintهایی استفاده کنید که مقدار taint در آن‌ها  
کوچک‌تر از مقدار toleration است:

```yaml
tolerations:
- key: "servicelevel.organization.example/agreed-service-level"
  operator: "Lt"
  value: "1000"
  effect: "NoSchedule"
```

{{< note >}}
هنگام استفاده از عملگرهای مقایسهٔ عددی:

* هم مقدار toleration و هم مقدار taint باید اعداد صحیح علامت‌دار ۶۴ بیتی معتبر باشند
  (اعدادی با صفر در ابتدا (مثلاً "0550") مجاز نیستند).
* اگر مقداری قابل تجزیه به عدد صحیح نباشد، toleration منطبق نمی‌شود.
* عملگرهای عددی با همهٔ اثرهای taint کار می‌کنند: `NoSchedule`، `PreferNoSchedule` و `NoExecute`.
* برای `PreferNoSchedule` همراه با عملگرهای عددی: اگر toleration یک پاد مقایسهٔ عددی را برآورده نکند
  (مثلاً هنگام استفاده از `Gt`، مقدار taint < مقدار toleration باشد)، زمان‌بند به آن نود اولویت پایین‌تری می‌دهد
  اما اگر گزینهٔ بهتری وجود نداشته باشد، ممکن است همچنان پاد را در آنجا زمان‌بندی کند.
{{< /note >}}

{{< warning >}}

پیش از غیرفعال کردن feature gate با نام `TaintTolerationComparisonOperators`:

* باید همهٔ بارهای کاری‌ای را که از عملگرهای `Gt` یا `Lt` استفاده می‌کنند شناسایی کنید تا از ایجاد حلقه‌های داغ (hot-loop) در کنترل‌کننده جلوگیری شود.
* همهٔ قالب‌های کنترل‌کنندهٔ بار کاری را به‌روزرسانی کنید تا به‌جای آن از عملگرهای `Equal` یا `Exists` استفاده کنند
* هر پاد در وضعیت pending را که از عملگرهای `Gt` یا `Lt` استفاده می‌کند حذف کنید
* متریک `apiserver_request_total` را برای افزایش ناگهانی خطاهای اعتبارسنجی پایش کنید
{{< /warning >}}

## نمونه‌هایی از موارد استفاده

Taintها و tolerationها روشی انعطاف‌پذیر برای هدایت پادها به *دور* از نودها یا بیرون راندن
پادهایی هستند که نباید در حال اجرا باشند. برخی از موارد استفاده عبارت‌اند از

* **نودهای اختصاصی**: اگر می‌خواهید مجموعه‌ای از نودها را به استفادهٔ انحصاری
مجموعهٔ مشخصی از کاربران اختصاص دهید، می‌توانید یک taint به آن نودها اضافه کنید (مثلاً
`kubectl taint nodes nodename dedicated=groupName:NoSchedule`) و سپس toleration متناظر را
به پادهای آن کاربران اضافه کنید (ساده‌ترین راه انجام این کار نوشتن یک
[کنترل‌کنندهٔ پذیرش (admission controller)](/docs/reference/access-authn-authz/admission-controllers/) سفارشی است).
در این صورت پادهای دارای tolerationها مجاز خواهند بود از نودهای دارای taint (اختصاصی) و نیز
هر نود دیگری در کلاستر استفاده کنند. اگر می‌خواهید نودها را به آن‌ها اختصاص دهید *و*
اطمینان حاصل کنید که آن‌ها *فقط* از نودهای اختصاصی استفاده می‌کنند، باید علاوه بر این برچسبی مشابه
taint را به همان مجموعه از نودها اضافه کنید (مثلاً `dedicated=groupName`)، و کنترل‌کنندهٔ پذیرش
نیز باید یک وابستگی نود اضافه کند تا الزام شود که پادها فقط بتوانند روی
نودهایی با برچسب `dedicated=groupName` زمان‌بندی شوند.

* **نودهای دارای سخت‌افزار ویژه**: در کلاستری که زیرمجموعهٔ کوچکی از نودها سخت‌افزار تخصصی
(برای مثال GPU) دارند، مطلوب است پادهایی که به سخت‌افزار تخصصی نیاز ندارند
از آن نودها دور نگه داشته شوند تا برای پادهایی که بعداً می‌رسند و به سخت‌افزار تخصصی
نیاز دارند جا باقی بماند. این کار را می‌توان با taint کردن نودهای دارای سخت‌افزار
تخصصی (مثلاً `kubectl taint nodes nodename special=true:NoSchedule` یا
`kubectl taint nodes nodename special=true:PreferNoSchedule`) و افزودن toleration متناظر
به پادهایی که از سخت‌افزار ویژه استفاده می‌کنند انجام داد. همانند مورد استفادهٔ نودهای اختصاصی،
احتمالاً ساده‌ترین راه اعمال tolerationها استفاده از یک
[کنترل‌کنندهٔ پذیرش](/docs/reference/access-authn-authz/admission-controllers/) سفارشی است.
برای مثال، توصیه می‌شود از [منابع
توسعه‌یافته (Extended Resources)](/docs/concepts/configuration/manage-resources-containers/#extended-resources)
برای نمایش سخت‌افزار ویژه استفاده کنید، نودهای دارای سخت‌افزار ویژه را با نام
منبع توسعه‌یافته taint کنید و کنترل‌کنندهٔ پذیرش
[ExtendedResourceToleration](/docs/reference/access-authn-authz/admission-controllers/#extendedresourcetoleration)
را اجرا کنید. اکنون، چون نودها taint شده‌اند، هیچ پادی بدون
toleration روی آن‌ها زمان‌بندی نمی‌شود. اما هنگامی که پادی را ارسال می‌کنید که
منبع توسعه‌یافته را درخواست می‌کند، کنترل‌کنندهٔ پذیرش `ExtendedResourceToleration`
به‌طور خودکار toleration درست را به پاد اضافه می‌کند و آن پاد روی
نودهای دارای سخت‌افزار ویژه زمان‌بندی می‌شود. این کار تضمین می‌کند که این نودهای دارای سخت‌افزار
ویژه به پادهایی اختصاص یابند که چنین سخت‌افزاری را درخواست می‌کنند و لازم نباشد
tolerationها را به‌صورت دستی به پادهای خود اضافه کنید.

* **بیرون‌رانی مبتنی بر taint**: رفتاری برای بیرون‌رانی که برای هر پاد قابل پیکربندی است
و هنگام بروز مشکل در نودها اعمال می‌شود و در بخش بعدی توضیح داده شده است.

## بیرون‌رانی مبتنی بر taint

{{< feature-state for_k8s_version="v1.18" state="stable" >}}

کنترل‌کنندهٔ نود هنگامی که شرایط خاصی برقرار باشد، به‌طور خودکار یک Node را taint می‌کند.
taintهای زیر به‌صورت داخلی تعریف شده‌اند:

 * `node.kubernetes.io/not-ready`: نود آماده نیست. این وضعیت متناظر با
   این است که NodeCondition با نام `Ready` برابر با "`False`" باشد.
 * `node.kubernetes.io/unreachable`: نود از سوی کنترل‌کنندهٔ نود قابل
   دسترسی نیست. این وضعیت متناظر با این است که NodeCondition با نام `Ready` برابر با "`Unknown`" باشد.
 * `node.kubernetes.io/memory-pressure`: نود تحت فشار حافظه است.
 * `node.kubernetes.io/disk-pressure`: نود تحت فشار دیسک است.
 * `node.kubernetes.io/pid-pressure`: نود تحت فشار PID است.
 * `node.kubernetes.io/network-unavailable`: شبکهٔ نود در دسترس نیست.
 * `node.kubernetes.io/unschedulable`: نود قابل زمان‌بندی نیست.
 * `node.cloudprovider.kubernetes.io/uninitialized`: هنگامی که kubelet با
    یک ارائه‌دهندهٔ ابری «خارجی» راه‌اندازی می‌شود، این taint روی نود تنظیم می‌شود تا آن را
    غیرقابل استفاده علامت‌گذاری کند. پس از آنکه یک کنترل‌کننده از cloud-controller-manager این نود را
    مقداردهی اولیه کرد، kubelet این taint را حذف می‌کند.

در صورتی که قرار باشد نودی تخلیه (drain) شود، کنترل‌کنندهٔ نود یا kubelet taintهای مربوط
را با اثر `NoExecute` اضافه می‌کند. این اثر به‌طور پیش‌فرض برای taintهای
`node.kubernetes.io/not-ready` و `node.kubernetes.io/unreachable` اضافه می‌شود.
اگر وضعیت خطا به حالت عادی بازگردد، kubelet یا کنترل‌کنندهٔ
نود می‌تواند taint(های) مربوط را حذف کند.

در برخی موارد که نود قابل دسترسی نیست، API server قادر به برقراری ارتباط
با kubelet روی نود نیست. تصمیم به حذف پادها تا زمانی که ارتباط با API server
دوباره برقرار نشود، نمی‌تواند به kubelet اطلاع داده شود. در این فاصله،
پادهایی که برای حذف زمان‌بندی شده‌اند ممکن است همچنان روی نود جداافتاده به اجرا ادامه دهند.

{{< note >}}
control plane نرخ افزودن taintهای جدید به نودها را محدود می‌کند. این محدودسازی نرخ،
تعداد بیرون‌رانی‌هایی را که هنگام غیرقابل دسترس شدن هم‌زمان تعداد زیادی نود
(برای مثال: در صورت بروز اختلال در شبکه) آغاز می‌شوند، مدیریت می‌کند.
{{< /note >}}

می‌توانید `tolerationSeconds` را برای یک Pod مشخص کنید تا تعیین کنید آن Pod چه مدت
به یک Node معیوب یا بدون پاسخ متصل باقی بماند.

برای مثال، ممکن است بخواهید برنامه‌ای را که وضعیت محلی (local state) زیادی دارد،
در صورت بروز جداافتادگی شبکه برای مدت طولانی به نود متصل نگه دارید، به این امید
که جداافتادگی برطرف شود و در نتیجه از بیرون‌رانی پاد جلوگیری شود.
tolerationی که برای آن Pod تنظیم می‌کنید ممکن است به این شکل باشد:

```yaml
tolerations:
- key: "node.kubernetes.io/unreachable"
  operator: "Exists"
  effect: "NoExecute"
  tolerationSeconds: 6000
```

{{< note >}}
کوبرنتیز به‌طور خودکار یک toleration برای
`node.kubernetes.io/not-ready` و `node.kubernetes.io/unreachable`
با `tolerationSeconds=300` اضافه می‌کند،
مگر اینکه شما یا یک کنترل‌کننده آن tolerationها را به‌صراحت تنظیم کرده باشید.

این tolerationهای خودکار به این معنا هستند که پادها پس از تشخیص یکی از این مشکلات،
به مدت ۵ دقیقه به نودها متصل باقی می‌مانند.
{{< /note >}}

پادهای [DaemonSet](/docs/concepts/workloads/controllers/daemonset/) با
tolerationهای `NoExecute` برای taintهای زیر و بدون `tolerationSeconds` ایجاد می‌شوند:

  * `node.kubernetes.io/unreachable`
  * `node.kubernetes.io/not-ready`

این کار تضمین می‌کند که پادهای DaemonSet هرگز به دلیل این مشکلات بیرون رانده نشوند.

{{< note >}}
پیش‌تر کنترل‌کنندهٔ نود مسئول افزودن taintها به نودها و بیرون راندن پادها بود. اما پس از نسخهٔ 1.29،
پیاده‌سازی بیرون‌رانی مبتنی بر taint از کنترل‌کنندهٔ نود خارج شده و به مؤلفه‌ای جداگانه
و مستقل به نام taint-eviction-controller منتقل شده است. کاربران می‌توانند به‌صورت اختیاری بیرون‌رانی مبتنی بر taint را
با تنظیم `--controllers=-taint-eviction-controller` در kube-controller-manager غیرفعال کنند.
{{< /note >}}

## Taint کردن نودها بر اساس وضعیت

control plane با استفاده از {{<glossary_tooltip text="کنترل‌کنندهٔ" term_id="controller">}} نود،
به‌طور خودکار taintهایی با اثر `NoSchedule` برای
[وضعیت‌های نود](/docs/concepts/scheduling-eviction/node-pressure-eviction/#node-conditions) ایجاد می‌کند.

زمان‌بند هنگام اتخاذ تصمیم‌های زمان‌بندی، taintها را بررسی می‌کند، نه وضعیت‌های نود را.
این کار تضمین می‌کند که وضعیت‌های نود به‌طور مستقیم بر زمان‌بندی تأثیر نگذارند.
برای مثال، اگر وضعیت نود `DiskPressure` فعال باشد، control plane
taint `node.kubernetes.io/disk-pressure` را اضافه می‌کند و پادهای جدید را
روی نود متأثر زمان‌بندی نمی‌کند. اگر وضعیت نود `MemoryPressure` فعال باشد،
control plane taint `node.kubernetes.io/memory-pressure` را اضافه می‌کند.

می‌توانید با افزودن tolerationهای متناظر به Pod، وضعیت‌های نود را برای پادهای تازه ایجادشده
نادیده بگیرید. control plane همچنین toleration `node.kubernetes.io/memory-pressure`
را به پادهایی اضافه می‌کند که {{< glossary_tooltip text="کلاس QoS" term_id="qos-class" >}}
آن‌ها چیزی غیر از `BestEffort` باشد. دلیل این است که کوبرنتیز با پادهای کلاس‌های QoS `Guaranteed`
یا `Burstable` (حتی پادهایی که هیچ درخواست حافظه‌ای برایشان تنظیم نشده است) طوری رفتار می‌کند که گویی
قادر به کنار آمدن با فشار حافظه هستند، در حالی که پادهای جدید `BestEffort` روی
نود متأثر زمان‌بندی نمی‌شوند.

کنترل‌کنندهٔ DaemonSet به‌طور خودکار tolerationهای `NoSchedule` زیر را
به همهٔ daemonها اضافه می‌کند تا از خراب شدن DaemonSetها جلوگیری شود.

  * `node.kubernetes.io/memory-pressure`
  * `node.kubernetes.io/disk-pressure`
  * `node.kubernetes.io/pid-pressure` (1.14 یا بالاتر)
  * `node.kubernetes.io/unschedulable` (1.10 یا بالاتر)
  * `node.kubernetes.io/network-unavailable` (*فقط شبکهٔ میزبان*)

افزودن این tolerationها سازگاری با نسخه‌های پیشین را تضمین می‌کند. همچنین می‌توانید
tolerationهای دلخواه را به DaemonSetها اضافه کنید.

## Taintها و tolerationهای دستگاه

به‌جای taint کردن کل نودها، مدیران می‌توانند هنگامی که کلاستر از
[تخصیص پویای منابع](/docs/concepts/resource-management/dynamic-resource-allocation/) برای مدیریت سخت‌افزار ویژه استفاده می‌کند،
[دستگاه‌های منفرد را taint کنند](/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#device-taints-and-tolerations).
مزیت این روش آن است که taint کردن می‌تواند دقیقاً سخت‌افزاری را هدف بگیرد
که معیوب است یا به نگهداری نیاز دارد. tolerationها نیز پشتیبانی می‌شوند و می‌توان آن‌ها را هنگام درخواست
دستگاه‌ها مشخص کرد. tolerationها نیز مانند taintها بر همهٔ پادهایی که یک دستگاه تخصیص‌یافتهٔ مشترک دارند اعمال می‌شوند.

## {{% heading "whatsnext" %}}

* دربارهٔ [بیرون‌رانی ناشی از فشار نود](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
  و نحوهٔ پیکربندی آن مطالعه کنید
* دربارهٔ [اولویت Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) مطالعه کنید
* دربارهٔ [taintها و tolerationهای دستگاه](/docs/concepts/resource-management/dynamic-resource-allocation/device-taints/#device-taints-and-tolerations) مطالعه کنید
