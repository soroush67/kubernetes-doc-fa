---
title: بررسی سیاست‌های پذیرش اعتبارسنج و تغییردهنده
content_type: tutorial
description: >-
  با استفاده از سیاست‌های پذیرش اعلانی و زبان Common Expression Language (CEL)،
  منابع را در زمان پذیرش اعتبارسنجی یا تغییر دهید.
weight: 70
min-kubernetes-server-version: v1.32
---
<!-- overview -->

در این صفحه می‌توانید _سیاست‌های پذیرش_ (admission policies) اعلانی را امتحان کنید. این سیاست‌ها به شما امکان می‌دهند
با زبان Common Expression Language (CEL) منابع را اعتبارسنجی یا تغییر دهید.

کوبرنتیز {{< skew currentVersion >}} از دو نوع سیاست پذیرش پشتیبانی می‌کند:

- [ValidatingAdmissionPolicy](/docs/reference/access-authn-authz/validating-admission-policy/)
- [MutatingAdmissionPolicy](/docs/reference/access-authn-authz/mutating-admission-policy/)

این آموزش هر دو نوع سیاست پذیرش را پوشش می‌دهد.

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}}

برای تعریف سیاست‌های پذیرش، باید مدیر کلاستر باشید. مطمئن شوید که به کلاستری که با آن تمرین می‌کنید
دسترسی مدیریتی دارید.

برای ValidatingAdmissionPolicy به موارد زیر نیاز دارید:
* کلاستری با نسخهٔ 1.30 یا بالاتر.

برای MutatingAdmissionPolicy به موارد زیر نیاز دارید:
* کلاستری با نسخهٔ 1.36 یا بالاتر.

برای بررسی نسخه، دستور `kubectl version` را اجرا کنید.
اگر از نسخهٔ قدیمی‌تری از کوبرنتیز استفاده می‌کنید، مستندات همان نسخه را ببینید.


## سیاست‌های پذیرش اعلانی چه هستند؟

سیاست‌های پذیرش اعلانی جایگزینی اعلانی و درون‌فرایندی (in-process)
برای وب‌هوک‌های پذیرش (admission webhooks) فراهم می‌کنند.

قواعد این سیاست‌ها با زبان CEL تعریف می‌شوند
و به همین دلیل مستقیماً درون API server ارزیابی می‌شوند.

این سیاست‌ها بسیار پیکربندی‌پذیرند و به نویسندگان سیاست امکان می‌دهند منطقی تعریف کنند که مدیران کلاستر
بتوانند آن را بر حسب نیاز پارامتردهی کنند و دامنهٔ اعمال آن را به منابع مشخصی محدود کنند.

### انواع API برای سیاست‌های پذیرش

این دو نوع سیاست اهداف متفاوتی دارند.

ValidatingAdmissionPolicy برای _اعمال محدودیت‌ها_ است.

MutatingAdmissionPolicy برای _تغییر منابع در حین پذیرش_ است.

### اجزای سیاست

هر سیاست اعمال‌شده همیشه یک آبجکت _سیاست_ (ValidatingAdmissionPolicy یا MutatingAdmissionPolicy)
و یک آبجکت _اتصال_ (binding) جداگانه (ValidatingAdmissionPolicyBinding یا MutatingAdmissionPolicyBinding) دارد.

همچنین می‌توانید از _پارامترها_ استفاده کنید که **اختیاری** هستند. برای اطلاعات بیشتر،
[منابع پارامتر](/docs/reference/access-authn-authz/validating-admission-policy/#parameter-resources) (ValidatingAdmissionPolicy) یا
[منابع پارامتر](/docs/reference/access-authn-authz/mutating-admission-policy/#parameter-resources) (MutatingAdmissionPolicy) را ببینید.

آبجکت‌های سیاست، منطق انتزاعی یک سیاست را با زبان CEL توصیف می‌کنند.
برای مثال، یک ValidatingAdmissionPolicy می‌تواند محدودیتی برای تعداد رپلیکاها اعمال کند یا از وجود برچسب‌های مشخصی اطمینان یابد،
در حالی که یک MutatingAdmissionPolicy می‌تواند منابع را تغییر دهد؛ مثلاً یک برچسب پیش‌فرض به یک فضای نام (namespace) اضافه کند.

آبجکت‌های اتصال، سیاست را به کلاستر شما پیوند می‌دهند و دامنهٔ آن را تعیین می‌کنند.
هر ValidatingAdmissionPolicyBinding یا MutatingAdmissionPolicyBinding سیاست را به منابع مشخصی متصل می‌کند.
اگر بخواهید سیاستی را فقط برای زیرمجموعهٔ مشخصی از منابع اعمال کنید، دامنهٔ سیاست را در همین اتصال
(با استفاده از `matchResources`) محدود می‌کنید.

پارامترها امکان می‌دهند پیکربندی رفتار سیاست از تعریف آن جدا شود.
منابع پارامتر به منابعی از کوبرنتیز اشاره دارند که در API در دسترس هستند.
این منابع می‌توانند از انواع داخلی API (مانند ConfigMap) یا
[منابع سفارشی](/docs/concepts/extend-kubernetes/api-extension/custom-resources/) باشند.
سپس اتصال سیاست با استفاده از `spec.paramRef` به یک منبع پارامتر واقعی ارجاع می‌دهد.

اگر سیاستی به پارامتر نیاز نداشته باشد، `spec.paramKind` را مشخص نمی‌کنید.

### عبارت‌های CEL

هر دو نوع سیاست بر زبان عبارتی به نام Common Expression Language (CEL) تکیه دارند.
برای اطلاعات بیشتر، [CEL در کوبرنتیز](/docs/reference/using-api/cel/) را بخوانید.

اگر با CEL تازه آشنا شده‌اید، نوشتن یک عبارت بسیار ساده مانند `false || true` را تمرین کنید.
می‌توانید عبارت‌های CEL را در [CEL Playground](https://playcel.undistro.io) آزمایش کنید.

### کنش‌های سیاست

هر اتصال سیاست پذیرش باید یک یا چند کنش (action) را مشخص کند تا نحوهٔ اعمال سیاست
تعیین شود.

#### ValidatingAdmissionPolicyBinding {#policy-actions-validating}


برای ValidatingAdmissionPolicyBinding، مقادیر پشتیبانی‌شده برای `validationActions` عبارت‌اند از:

Audit
: شکست اعتبارسنجی در رویداد ممیزی (audit event) مربوط به درخواست API ثبت می‌شود.

Warn
: شکست اعتبارسنجی به‌صورت یک
  [هشدار](/blog/2020/09/03/warnings/) به کلاینت درخواست‌دهنده گزارش می‌شود.

Deny
: شکست اعتبارسنجی به رد شدن درخواست می‌انجامد.

بررسی ناموفق سیاست یا خطای رخ‌داده بر اساس همین کنش‌ها اعمال می‌شود.
شکست‌هایی که با `failurePolicy` تعریف می‌شوند، تنها در صورتی بر اساس این کنش‌ها اعمال می‌شوند که `failurePolicy`
روی `Fail` تنظیم شده باشد (یا مشخص نشده باشد).

برای جزئیات بیشتر دربارهٔ ثبت ممیزی برای سیاست‌ها،
[حاشیه‌نویسی‌های ممیزی: شکست‌های اعتبارسنجی](/docs/reference/labels-annotations-taints/audit-annotations/#validation-policy-admission-k8s-io-validation-failure) را ببینید.

مجاز نیستید Deny و Warn را با هم استفاده کنید، زیرا این ترکیب باعث می‌شود شکست اعتبارسنجی
هم در بدنهٔ پاسخ API و هم در سرآیند HTTP `Warning:` تکرار شود.

#### MutatingAdmissionPolicyBinding {#policy-actions-mutating}

برای MutatingAdmissionPolicyBinding، کنش همیشه تغییر آبجکت است.

می‌توانید از JSON Patch یا یک _پیکربندی apply_ (apply configuration) کوبرنتیز استفاده کنید.

## اعمال سیاست از طریق اعتبارسنجی

اکنون تعریف یک ValidatingAdmissionPolicy را امتحان کنید.

نمونهٔ زیر یک ValidatingAdmissionPolicy است که الزام می‌کند هر Deployment چند رپلیکا داشته باشد.

{{< code_sample language="yaml" file="access/manifest-admission-control/vap-min-replicas.yaml" >}}

فیلد `spec.validations` شامل عبارت‌هایی است که با [زبان Common Expression Language (CEL)](https://github.com/google/cel-spec)
نوشته شده‌اند و درخواست را اعتبارسنجی می‌کنند.
اگر حاصل ارزیابی یک عبارت false باشد، بررسی اعتبارسنجی بر اساس فیلد `spec.failurePolicy` اعمال می‌شود.

سیاستی مانند این بنویسید و آن را اعمال کنید.

یا اگر می‌خواهید یک مانیفست آماده را اعمال کنید:

```shell
kubectl apply --server-side -f https://k8s.io/examples/access/manifest-admission-control/vap-min-replicas.yaml
```

این سیاست به‌تنهایی هیچ کاری انجام نمی‌دهد.

می‌توانید ایجاد یک Deployment با ۰ یا ۱ رپلیکا را امتحان کنید؛ این کار انجام می‌شود (مگر اینکه سیاست دیگری مانع آن شود).

---

برای اینکه سیاست کار کند، یک ValidatingAdmissionPolicyBinding تعریف می‌کنید.

فضای نامی را انتخاب کنید که می‌خواهید سیاست جدید را در آن اعمال کنید.

نمونهٔ زیر یک ValidatingAdmissionPolicyBinding برای سیاستی است که ساختید:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: enforce-multiple-replicas-deployments-binding
spec:
  policyName: "enforce-multiple-replicas-deployments"
  validationActions: [Deny]
  matchResources:
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: default # change this to match the namespace you're using
```

{{< caution >}}
هر کسی که دسترسی کامل یا مدیریتی به یک فضای نام داشته باشد، می‌تواند برچسب‌های آن را تغییر دهد. این شامل حذف یک برچسب از
فضای نام نیز می‌شود.

برچسب `kubernetes.io/metadata.name` محافظت‌شده است، اما اگر از برچسب دیگری استفاده می‌کنید، مراقب باشید
که فقط کاربران مورد اعتماد بتوانند برچسب انتخابی شما را حذف یا ویرایش کنند.
{{< /caution >}}

بر اساس آن YAML نمونه یک مانیفست بنویسید (اگر از فضای نام `default` استفاده می‌کنید، می‌توانید
آن را بدون هیچ تغییری به کار ببرید). سپس آن مانیفست را با `kubectl apply` اعمال کنید.


### آزمایش سیاست {#test-admission-policy-validation}

اکنون سیاست را آزمایش کنید. [یک Deployment ایجاد کنید](/docs/tasks/run-application/run-stateless-application-deployment/)
و سپس با `kubectl scale` تعداد رپلیکاهای آن را به ۰ برسانید. چه اتفاقی می‌افتد؟

می‌توانید ValidatingAdmissionPolicyBinding را طوری تغییر دهید که به‌جای Deny،
کنش اعتبارسنجی دیگری داشته باشد. اگر کنش اعتبارسنجی Warning را انتخاب کنید و بخواهید تعداد رپلیکاهای یک Deployment را به ۰ برسانید،
چه اتفاقی می‌افتد؟

{{< note >}}
اگر ValidatingAdmissionPolicyBinding را طوری تغییر داده باشید که فقط به کاربران هشدار دهد، مشکلی وجود دارد&hellip;

نام آن نادرست است! اگر یک ValidatingAdmissionPolicyBinding یا ValidatingAdmissionPolicy مرتبط با آن را طوری تغییر دهید
که فقط هشدار دهد، باید بررسی کنید که آیا لازم است نام سیاست را هم تغییر دهید. نام را تغییر می‌دهید
تا مطمئن شوید که نام‌گذاری کاربران را گمراه نمی‌کند.
{{< /note >}}



### منابع موجود تحت تأثیر قرار نمی‌گیرند {#limitation-admission-policy-validation}

اگر یک Deployment با ۰ یا ۱ رپلیکا داشته باشید و ValidatingAdmissionPolicyBinding را دوباره
به حالت Deny برگردانید، این کار روی هیچ‌یک از منابع موجود اثری ندارد.

(اگر می‌خواستید تعداد رپلیکاهای Deploymentها را دست‌کم به ۲ افزایش دهید، می‌توانستید این کار را
به روش دیگری انجام دهید؛ برای مثال با استفاده از یک {{< glossary_tooltip text="کنترل‌کننده" term_id="controller" >}}).

بخش ValidatingAdmissionPolicy همین‌جا به پایان می‌رسد. اکنون با MutatingAdmissionPolicyها آشنا می‌شوید.

## تغییر منابع هنگام ایجاد یا تغییر آن‌ها {#mutation}

در این مثال، فرض کنید می‌خواهید با استفاده از [پذیرش امنیت Pod](/docs/concepts/security/pod-security-admission/)
مطمئن شوید که فضاهای نام، به‌جز فضاهای نام سیستمی، یک استاندارد امنیت Pod را اعمال می‌کنند.

مشابه اعتبارسنجی، می‌توانید یک MutatingAdmissionPolicy ایجاد کنید که منابع را
در حین پذیرش تغییر دهد. نوع API که باید تغییر دهید Namespace است.

در اینجا یک MutatingAdmissionPolicy آمده است که بخشی از این کار را انجام می‌دهد:

{{< code_sample language="yaml" file="access/manifest-admission-control/default-pod-security-baseline.yaml" >}}

{{< caution >}}
این سیاست یک مقدار **پیش‌فرض** تنظیم می‌کند. کسی که امکان به‌روزرسانی یک Namespace را دارد، می‌تواند برچسب
`pod-security.kubernetes.io/enforce` را از فضای نام حذف کند.

اگر مطمئن نیستید این به چه معناست، مستندات [امنیت](/docs/concepts/security/) را مطالعه کنید یا
از مشاوران امنیت اطلاعات بیرونی راهنمایی بگیرید.
{{< /caution >}}

برای اعمال آن سیاست:

```shell
kubectl apply --server-side -f https://k8s.io/examples/access/manifest-admission-control/default-pod-security-baseline.yaml 
```

برای فعال‌سازی این سیاست به یک MutatingAdmissionPolicyBinding نیاز است؛ برای مثال:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionPolicyBinding
metadata:
  name: default-pod-security-baseline
spec:
  # the name of the MutatingAdmissionPolicy to apply
  policyName: default-pod-security-baseline
```

### آزمایش سیاست {#test-admission-policy-mutation}

ایجاد یک فضای نام جدید با نام `example` را امتحان کنید:

```shell
kubectl create ns example
```

برچسب‌های آن را بررسی کنید:
```shell
kubectl describe ns example
```

با اینکه سطح اعمال پذیرش امنیت Pod را مشخص نکرده‌اید، برچسب تنظیم شده است.

سپس بررسی کنید که آیا راهی برای دور زدن تنظیمات امنیتی پیدا می‌کنید یا نه.
یک مانیفست YAML برای Namespace دیگری بسازید:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: another-example
  labels:
    pod-security.kubernetes.io/enforce: privileged
```

می‌توانید آن فضای نام را از مانیفست محلی و با `kubectl apply --server-side` ایجاد کنید. آیا این کار انجام می‌شود؟

بله، و فضای نام جدید اجرای Podهای privileged را مجاز می‌کند.

این سیاست پذیرش برای اعتبارسنجی یا محدودسازی پیکربندی **نشده** است. این سیاست یک مقدار پیش‌فرض فراهم می‌کند، اما می‌توانید
مقدار دلخواه خود را تنظیم کنید.
با این حال، می‌توانید پذیرش تغییردهنده را با یک سیاست پذیرش اعتبارسنج ترکیب کنید تا هم چیزی را اعمال کنید
و هم رعایت آن را آسان کنید. (این آموزش چگونگی این کار را توضیح نمی‌دهد، اما انجام آن ممکن است.)

فراهم کردن یک مقدار پیش‌فرض مفید به این معناست که وقتی کاربران چیزی تنظیم نمی‌کنند، به نتیجه‌ای بهتر از صرفاً دیدن
یک پیام خطا می‌رسند. فرض کنید قاعدهٔ اعتبارسنجی‌ای داشتید که الزام می‌کرد همهٔ فضاهای نام دست‌کم
استاندارد baseline را اعمال کنند. هر کسی که از آن قاعده خبر نداشت، ممکن بود بخواهد چیزی را مستقر کند و بلافاصله
هنگام ایجاد یک فضای نام با پیام خطا روبه‌رو شود.

### استفاده از یک منبع پارامتر

منابع پارامتر امکان می‌دهند پیکربندی سیاست از تعریف آن جدا باشد.
یک سیاست می‌تواند `paramKind` را تعریف کند که گروه، نسخه و نوع (که GVK نیز نامیده می‌شود)
منبع پارامتر را مشخص می‌کند. سپس یک اتصال سیاست، آن سیاست را به دامنه‌ای که در آن متصل شده است پیوند می‌دهد،
به همان شکلی که یک منبع پارامتر مشخص آن را پیکربندی کرده است.

{{< code_sample language="yaml" file="access/manifest-admission-control/default-pod-security-configurable.yaml" >}}

در اینجا یک MutatingAdmissionPolicyBinding نمونه آمده است:

```yaml
---
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionPolicyBinding
metadata:
  name: default-pod-security-configurable
spec:
  # the name of the MutatingAdmissionPolicy to apply
  policyName: default-pod-security-configurable

  # parameters to use
  paramRef:
    # if the ConfigMap is missing or empty, don't set a default
    # (but do allow namespace creation)
    parameterNotFoundAction: Allow

    # where to find the parameter
    namespace: kube-system
    name: default-pod-security-standard
```

و این هم یک ConfigMap نمونه برای قرار دادن در فضای نام kube-system:

```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: kube-system
  name: default-pod-security-standard
data:
  default: baseline # could also be "restricted"
```

هر دوی این‌ها را تعریف کنید. باید **ابتدا ConfigMap را ایجاد کنید**؛ اتصال انتظار دارد که منبع پارامتر
از قبل وجود داشته باشد (حتی اگر قصد دارید بعداً آن را تغییر دهید).

اکنون MutatingAdmissionPolicyBinding قبلی را حذف کنید:
```shell
kubectl delete mutatingadmissionpolicybindings/default-pod-security-baseline
```

و یک فضای نام جدید ایجاد کنید:
```shell
kubectl create ns yet-another-example
```

```shell
kubectl describe ns yet-another-example
```

آیا برچسب‌ها با مقدار پیش‌فرض تنظیم شدند؟

### تغییر پارامتر

```shell
# This starts an editor that lets you change .data.default for the parameter
kubectl --namespace kube-system edit configmap default-pod-security-standard
```

پس از تغییر آن، ایجاد یک فضای نام دیگر را امتحان کنید. چه اتفاقی می‌افتد؟

## پاک‌سازی

برای حذف منابع ایجادشده، دستورهای زیر را اجرا کنید:

```bash
kubectl delete validatingadmissionpolices/enforce-multiple-replicas-deployments \
               validatingadmissionpolicybindings/enforce-multiple-replicas-deployments

kubectl delete mutatingadmissionpolicies/default-pod-security-baseline \
               mutatingadmissionpolicybindings/default-pod-security-baseline

kubectl delete mutatingadmissionpolicies/default-pod-security-configurable \
               mutatingadmissionpolicybindings/default-pod-security-configurable

kubectl --namespace kube-system delete configmaps/default-pod-security-standard

kubectl delete namespaces/example namespaces/another-example namespaces/yet-another-example
```

اگر Pod یا Namespace آزمایشی دیگری ایجاد کرده‌اید، آن‌ها را هم پاک کنید.
