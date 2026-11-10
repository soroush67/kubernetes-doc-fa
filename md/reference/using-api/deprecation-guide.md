---
reviewers:
- liggitt
- lavalamp
- thockin
- smarterclayton
title: "راهنمای مهاجرت از APIهای منسوخ‌شده"
weight: 45
content_type: reference
---

<!-- overview -->

API کوبرنتیز به‌مرور تکامل می‌یابد و APIها به‌صورت دوره‌ای بازسازمان‌دهی یا ارتقا داده می‌شوند.
با تکامل APIها، API قدیمی منسوخ (deprecated) و در نهایت حذف می‌شود.
این صفحه اطلاعاتی را در بر دارد که هنگام مهاجرت از نسخه‌های منسوخ‌شدهٔ API به نسخه‌های جدیدتر و پایدارتر به آن‌ها نیاز دارید.

<!-- body -->

## فهرست APIهای حذف‌شده به تفکیک نسخهٔ انتشار

### نسخهٔ v1.32

در نسخهٔ **v1.32**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منابع کنترل جریان (Flow control) {#flowcontrol-resources-v132}

نسخهٔ API **flowcontrol.apiserver.k8s.io/v1beta3** برای FlowSchema و PriorityLevelConfiguration از v1.32 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **flowcontrol.apiserver.k8s.io/v1** منتقل کنید که از v1.29 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه در **flowcontrol.apiserver.k8s.io/v1**:
  * فیلد `spec.limited.nominalConcurrencyShares` در PriorityLevelConfiguration فقط زمانی مقدار پیش‌فرض 30 را می‌گیرد که مقداری برای آن تعیین نشده باشد، و مقدار صریح 0 به 30 تغییر نمی‌کند.

### نسخهٔ v1.29

در نسخهٔ **v1.29**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منابع کنترل جریان {#flowcontrol-resources-v129}

نسخهٔ API **flowcontrol.apiserver.k8s.io/v1beta2** برای FlowSchema و PriorityLevelConfiguration از v1.29 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **flowcontrol.apiserver.k8s.io/v1** (در دسترس از v1.29) یا نسخهٔ API **flowcontrol.apiserver.k8s.io/v1beta3** (در دسترس از v1.26) منتقل کنید.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه در **flowcontrol.apiserver.k8s.io/v1**:
  * نام فیلد `spec.limited.assuredConcurrencyShares` در PriorityLevelConfiguration به `spec.limited.nominalConcurrencyShares` تغییر کرده است. این فیلد فقط زمانی مقدار پیش‌فرض 30 را می‌گیرد که مقداری برای آن تعیین نشده باشد، و مقدار صریح 0 به 30 تغییر نمی‌کند.
* تغییرات قابل توجه در **flowcontrol.apiserver.k8s.io/v1beta3**:
  * نام فیلد `spec.limited.assuredConcurrencyShares` در PriorityLevelConfiguration به `spec.limited.nominalConcurrencyShares` تغییر کرده است.

### نسخهٔ v1.27

در نسخهٔ **v1.27**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منبع CSIStorageCapacity {#csistoragecapacity-v127}

نسخهٔ API **storage.k8s.io/v1beta1** برای CSIStorageCapacity از v1.27 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **storage.k8s.io/v1** منتقل کنید که از v1.24 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

### نسخهٔ v1.26

در نسخهٔ **v1.26**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منابع کنترل جریان {#flowcontrol-resources-v126}

نسخهٔ API **flowcontrol.apiserver.k8s.io/v1beta1** برای FlowSchema و PriorityLevelConfiguration از v1.26 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **flowcontrol.apiserver.k8s.io/v1beta2** منتقل کنید.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منبع HorizontalPodAutoscaler {#horizontalpodautoscaler-v126}

نسخهٔ API **autoscaling/v2beta2** برای HorizontalPodAutoscaler از v1.26 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **autoscaling/v2** منتقل کنید که از v1.23 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `targetAverageUtilization` با `target.averageUtilization` و `target.type: Utilization` جایگزین شده است. به [مقیاس‌دهی خودکار بر اساس چند متریک و متریک‌های سفارشی](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics) مراجعه کنید.
### نسخهٔ v1.25

در نسخهٔ **v1.25**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منبع CronJob {#cronjob-v125}

نسخهٔ API **batch/v1beta1** برای CronJob از v1.25 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **batch/v1** منتقل کنید که از v1.21 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منبع EndpointSlice {#endpointslice-v125}

نسخهٔ API **discovery.k8s.io/v1beta1** برای EndpointSlice از v1.25 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **discovery.k8s.io/v1** منتقل کنید که از v1.21 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه در **discovery.k8s.io/v1**:
  * به جای فیلد منسوخ‌شدهٔ `topology["kubernetes.io/hostname"]`، از فیلد `nodeName` در سطح هر Endpoint استفاده کنید.
  * به جای فیلد منسوخ‌شدهٔ `topology["topology.kubernetes.io/zone"]`، از فیلد `zone` در سطح هر Endpoint استفاده کنید.
  * فیلد `topology` با فیلد `deprecatedTopology` جایگزین شده است که در v1 قابل نوشتن نیست.

#### منبع Event {#event-v125}

نسخهٔ API **events.k8s.io/v1beta1** برای Event از v1.25 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **events.k8s.io/v1** منتقل کنید که از v1.19 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه در **events.k8s.io/v1**:
  * مقدار فیلد `type` به `Normal` و `Warning` محدود است.
  * نام فیلد `involvedObject` به `regarding` تغییر کرده است.
  * هنگام ایجاد Eventهای جدید **events.k8s.io/v1**، فیلدهای `action`، `reason`، `reportingController` و `reportingInstance` الزامی هستند.
  * به جای فیلد منسوخ‌شدهٔ `firstTimestamp` از `eventTime` استفاده کنید (نام آن فیلد به `deprecatedFirstTimestamp` تغییر کرده است و در Eventهای جدید **events.k8s.io/v1** مجاز نیست).
  * به جای فیلد منسوخ‌شدهٔ `lastTimestamp` از `series.lastObservedTime` استفاده کنید
    (نام آن فیلد به `deprecatedLastTimestamp` تغییر کرده است و در Eventهای جدید **events.k8s.io/v1** مجاز نیست).
  * به جای فیلد منسوخ‌شدهٔ `count` از `series.count` استفاده کنید
    (نام آن فیلد به `deprecatedCount` تغییر کرده است و در Eventهای جدید **events.k8s.io/v1** مجاز نیست).
  * به جای فیلد منسوخ‌شدهٔ `source.component` از `reportingController` استفاده کنید
    (نام آن فیلد به `deprecatedSource.component` تغییر کرده است و در Eventهای جدید **events.k8s.io/v1** مجاز نیست).
  * به جای فیلد منسوخ‌شدهٔ `source.host` از `reportingInstance` استفاده کنید
    (نام آن فیلد به `deprecatedSource.host` تغییر کرده است و در Eventهای جدید **events.k8s.io/v1** مجاز نیست).

#### منبع HorizontalPodAutoscaler {#horizontalpodautoscaler-v125}

نسخهٔ API **autoscaling/v2beta1** برای HorizontalPodAutoscaler از v1.25 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **autoscaling/v2** منتقل کنید که از v1.23 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `targetAverageUtilization` با `target.averageUtilization` و `target.type: Utilization` جایگزین شده است. به [مقیاس‌دهی خودکار بر اساس چند متریک و متریک‌های سفارشی](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics) مراجعه کنید.

#### منبع PodDisruptionBudget {#poddisruptionbudget-v125}

نسخهٔ API **policy/v1beta1** برای PodDisruptionBudget از v1.25 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **policy/v1** منتقل کنید که از v1.21 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه در **policy/v1**:
  * اگر در یک PodDisruptionBudget نسخهٔ `policy/v1` مقدار `spec.selector` خالی (`{}`) نوشته شود، همهٔ پادهای
    آن فضای نام انتخاب می‌شوند (در `policy/v1beta1`، مقدار خالی `spec.selector` هیچ پادی را انتخاب نمی‌کرد).
    اگر `spec.selector` تنظیم نشده باشد، در هیچ‌یک از دو نسخهٔ API هیچ پادی انتخاب نمی‌شود.

#### منبع PodSecurityPolicy {#psp-v125}

نسخهٔ API **policy/v1beta1** برای PodSecurityPolicy از v1.25 به بعد دیگر ارائه نمی‌شود
و کنترل‌کنندهٔ پذیرش (admission controller) PodSecurityPolicy نیز حذف خواهد شد.

به [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
یا یک [وب‌هوک پذیرش شخص ثالث](/docs/reference/access-authn-authz/extensible-admission-controllers/) مهاجرت کنید.
برای راهنمای مهاجرت، به [مهاجرت از PodSecurityPolicy به کنترل‌کنندهٔ پذیرش داخلی PodSecurity](/docs/tasks/configure-pod-container/migrate-from-psp/) مراجعه کنید.
برای اطلاعات بیشتر دربارهٔ این منسوخ‌شدن، به [منسوخ‌شدن PodSecurityPolicy: گذشته، حال و آینده](/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/) مراجعه کنید.

#### منبع RuntimeClass {#runtimeclass-v125}

نسخهٔ API **node.k8s.io/v1beta1** برای RuntimeClass از v1.25 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **node.k8s.io/v1** منتقل کنید که از v1.20 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

### نسخهٔ v1.22

در نسخهٔ **v1.22**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منابع وب‌هوک {#webhook-resources-v122}

نسخهٔ API **admissionregistration.k8s.io/v1beta1** برای MutatingWebhookConfiguration
و ValidatingWebhookConfiguration از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **admissionregistration.k8s.io/v1** منتقل کنید که از v1.16 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق APIهای جدید در دسترس هستند.
* تغییرات قابل توجه:
  * مقدار پیش‌فرض `webhooks[*].failurePolicy` در v1 از `Ignore` به `Fail` تغییر کرده است.
  * مقدار پیش‌فرض `webhooks[*].matchPolicy` در v1 از `Exact` به `Equivalent` تغییر کرده است.
  * مقدار پیش‌فرض `webhooks[*].timeoutSeconds` در v1 از `30s` به `10s` تغییر کرده است.
  * مقدار پیش‌فرض `webhooks[*].sideEffects` حذف شده و این فیلد الزامی شده است؛
    همچنین در v1 فقط مقادیر `None` و `NoneOnDryRun` مجاز هستند.
  * مقدار پیش‌فرض `webhooks[*].admissionReviewVersions` حذف شده و این فیلد در v1
    الزامی شده است (نسخه‌های پشتیبانی‌شده برای AdmissionReview عبارت‌اند از `v1` و `v1beta1`).
  * در آبجکت‌هایی که از طریق `admissionregistration.k8s.io/v1` ایجاد می‌شوند، مقدار `webhooks[*].name` باید در فهرست یکتا باشد.

#### منبع CustomResourceDefinition {#customresourcedefinition-v122}

نسخهٔ API **apiextensions.k8s.io/v1beta1** برای CustomResourceDefinition از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **apiextensions.k8s.io/v1** منتقل کنید که از v1.16 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `spec.scope` دیگر به‌طور پیش‌فرض مقدار `Namespaced` نمی‌گیرد و باید به‌صراحت مشخص شود.
  * فیلد `spec.version` در v1 حذف شده است؛ به جای آن از `spec.versions` استفاده کنید.
  * فیلد `spec.validation` در v1 حذف شده است؛ به جای آن از `spec.versions[*].schema` استفاده کنید.
  * فیلد `spec.subresources` در v1 حذف شده است؛ به جای آن از `spec.versions[*].subresources` استفاده کنید.
  * فیلد `spec.additionalPrinterColumns` در v1 حذف شده است؛ به جای آن از `spec.versions[*].additionalPrinterColumns` استفاده کنید.
  * فیلد `spec.conversion.webhookClientConfig` در v1 به `spec.conversion.webhook.clientConfig` منتقل شده است.
  * فیلد `spec.conversion.conversionReviewVersions` در v1 به `spec.conversion.webhook.conversionReviewVersions` منتقل شده است.
  * هنگام ایجاد آبجکت‌های CustomResourceDefinition نسخهٔ v1، فیلد `spec.versions[*].schema.openAPIV3Schema` اکنون الزامی است
    و باید یک [شِمای ساختاریافته](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#specifying-a-structural-schema) باشد.
  * هنگام ایجاد آبجکت‌های CustomResourceDefinition نسخهٔ v1، استفاده از `spec.preserveUnknownFields: true` مجاز نیست؛
    این تنظیم باید درون تعریف‌های شِما به‌صورت `x-kubernetes-preserve-unknown-fields: true` مشخص شود.
  * در آیتم‌های `additionalPrinterColumns`، نام فیلد `JSONPath` در v1 به `jsonPath` تغییر کرده است
    (رفع مشکل [#66531](https://github.com/kubernetes/kubernetes/issues/66531)).

#### منبع APIService {#apiservice-v122}

نسخهٔ API **apiregistration.k8s.io/v1beta1** برای APIService از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **apiregistration.k8s.io/v1** منتقل کنید که از v1.10 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منبع TokenReview {#tokenreview-v122}

نسخهٔ API **authentication.k8s.io/v1beta1** برای TokenReview از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **authentication.k8s.io/v1** منتقل کنید که از v1.6 در دسترس است.
* تغییر قابل توجهی وجود ندارد.

#### منابع SubjectAccessReview {#subjectaccessreview-resources-v122}

نسخهٔ API **authorization.k8s.io/v1beta1** برای LocalSubjectAccessReview،
SelfSubjectAccessReview، SubjectAccessReview و SelfSubjectRulesReview از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **authorization.k8s.io/v1** منتقل کنید که از v1.6 در دسترس است.
* تغییرات قابل توجه:
  * نام فیلد `spec.group` در v1 به `spec.groups` تغییر کرده است (رفع مشکل [#32709](https://github.com/kubernetes/kubernetes/issues/32709)).

#### منبع CertificateSigningRequest {#certificatesigningrequest-v122}

نسخهٔ API **certificates.k8s.io/v1beta1** برای CertificateSigningRequest از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **certificates.k8s.io/v1** منتقل کنید که از v1.19 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه در `certificates.k8s.io/v1`:
  * برای کلاینت‌های API که گواهی درخواست می‌کنند:
    * فیلد `spec.signerName` اکنون الزامی است
      (به [امضاکننده‌های شناخته‌شدهٔ کوبرنتیز](/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers) مراجعه کنید)
      و درخواست‌هایی برای `kubernetes.io/legacy-unknown` را نمی‌توان از طریق API `certificates.k8s.io/v1` ایجاد کرد.
    * فیلد `spec.usages` اکنون الزامی است، نمی‌تواند مقدار تکراری داشته باشد و فقط باید کاربردهای شناخته‌شده را در بر داشته باشد.
  * برای کلاینت‌های API که گواهی‌ها را تأیید یا امضا می‌کنند:
    * فیلد `status.conditions` نمی‌تواند نوع‌های تکراری داشته باشد.
    * فیلد `status.conditions[*].status` اکنون الزامی است.
    * مقدار `status.certificate` باید با کدگذاری PEM باشد و فقط بلوک‌های `CERTIFICATE` را در بر داشته باشد.

#### منبع Lease {#lease-v122}

نسخهٔ API **coordination.k8s.io/v1beta1** برای Lease از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **coordination.k8s.io/v1** منتقل کنید که از v1.14 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منبع Ingress {#ingress-v122}

نسخه‌های API **extensions/v1beta1** و **networking.k8s.io/v1beta1** برای Ingress از v1.22 به بعد دیگر ارائه نمی‌شوند.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **networking.k8s.io/v1** منتقل کنید که از v1.19 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * نام فیلد `spec.backend` به `spec.defaultBackend` تغییر کرده است.
  * نام فیلد `serviceName` در backend به `service.name` تغییر کرده است.
  * نام فیلدهای عددی `servicePort` در backend به `service.port.number` تغییر کرده است.
  * نام فیلدهای رشته‌ای `servicePort` در backend به `service.port.name` تغییر کرده است.
  * فیلد `pathType` اکنون برای هر مسیر مشخص‌شده الزامی است. گزینه‌های آن عبارت‌اند از `Prefix`،
    `Exact` و `ImplementationSpecific`. برای تطابق با رفتار تعریف‌نشدهٔ `v1beta1`، از `ImplementationSpecific` استفاده کنید.

#### منبع IngressClass {#ingressclass-v122}

نسخهٔ API **networking.k8s.io/v1beta1** برای IngressClass از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **networking.k8s.io/v1** منتقل کنید که از v1.19 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منابع RBAC {#rbac-resources-v122}

نسخهٔ API **rbac.authorization.k8s.io/v1beta1** برای ClusterRole، ClusterRoleBinding،
Role و RoleBinding از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **rbac.authorization.k8s.io/v1** منتقل کنید که از v1.8 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق APIهای جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منبع PriorityClass {#priorityclass-v122}

نسخهٔ API **scheduling.k8s.io/v1beta1** برای PriorityClass از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **scheduling.k8s.io/v1** منتقل کنید که از v1.14 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

#### منابع ذخیره‌سازی {#storage-resources-v122}

نسخهٔ API **storage.k8s.io/v1beta1** برای CSIDriver، CSINode، StorageClass و VolumeAttachment از v1.22 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **storage.k8s.io/v1** منتقل کنید.
  * منبع CSIDriver از v1.19 در **storage.k8s.io/v1** در دسترس است.
  * منبع CSINode از v1.17 در **storage.k8s.io/v1** در دسترس است.
  * منبع StorageClass از v1.6 در **storage.k8s.io/v1** در دسترس است.
  * منبع VolumeAttachment از v1.13 در **storage.k8s.io/v1** در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق APIهای جدید در دسترس هستند.
* تغییر قابل توجهی وجود ندارد.

### نسخهٔ v1.16

در نسخهٔ **v1.16**، ارائهٔ نسخه‌های منسوخ‌شدهٔ زیر از API متوقف شد:

#### منبع NetworkPolicy {#networkpolicy-v116}

نسخهٔ API **extensions/v1beta1** برای NetworkPolicy از v1.16 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **networking.k8s.io/v1** منتقل کنید که از v1.8 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.

#### منبع DaemonSet {#daemonset-v116}

نسخه‌های API **extensions/v1beta1** و **apps/v1beta2** برای DaemonSet از v1.16 به بعد دیگر ارائه نمی‌شوند.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **apps/v1** منتقل کنید که از v1.9 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `spec.templateGeneration` حذف شده است.
  * فیلد `spec.selector` اکنون الزامی است و پس از ایجاد قابل تغییر نیست؛ برای ارتقای بی‌وقفه،
    از برچسب‌های موجود در قالب (template) به‌عنوان انتخابگر (selector) استفاده کنید.
  * مقدار پیش‌فرض `spec.updateStrategy.type` اکنون `RollingUpdate` است
    (مقدار پیش‌فرض در `extensions/v1beta1` برابر `OnDelete` بود).

#### منبع Deployment {#deployment-v116}

نسخه‌های API **extensions/v1beta1**، **apps/v1beta1** و **apps/v1beta2** برای Deployment از v1.16 به بعد دیگر ارائه نمی‌شوند.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **apps/v1** منتقل کنید که از v1.9 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `spec.rollbackTo` حذف شده است.
  * فیلد `spec.selector` اکنون الزامی است و پس از ایجاد قابل تغییر نیست؛ برای ارتقای بی‌وقفه،
    از برچسب‌های موجود در قالب به‌عنوان انتخابگر استفاده کنید.
  * مقدار پیش‌فرض `spec.progressDeadlineSeconds` اکنون `600` ثانیه است
    (در `extensions/v1beta1` به‌طور پیش‌فرض هیچ مهلتی تعیین نمی‌شد).
  * مقدار پیش‌فرض `spec.revisionHistoryLimit` اکنون `10` است
    (مقدار پیش‌فرض در `apps/v1beta1` برابر `2` بود و در `extensions/v1beta1` به‌طور پیش‌فرض همهٔ نسخه‌ها نگه داشته می‌شدند).
  * مقدار پیش‌فرض `maxSurge` و `maxUnavailable` اکنون `25%` است
    (مقدار پیش‌فرض در `extensions/v1beta1` برابر `1` بود).

#### منبع StatefulSet {#statefulset-v116}

نسخه‌های API **apps/v1beta1** و **apps/v1beta2** برای StatefulSet از v1.16 به بعد دیگر ارائه نمی‌شوند.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **apps/v1** منتقل کنید که از v1.9 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `spec.selector` اکنون الزامی است و پس از ایجاد قابل تغییر نیست؛
    برای ارتقای بی‌وقفه، از برچسب‌های موجود در قالب به‌عنوان انتخابگر استفاده کنید.
  * مقدار پیش‌فرض `spec.updateStrategy.type` اکنون `RollingUpdate` است
    (مقدار پیش‌فرض در `apps/v1beta1` برابر `OnDelete` بود).

#### منبع ReplicaSet {#replicaset-v116}

نسخه‌های API **extensions/v1beta1**، **apps/v1beta1** و **apps/v1beta2** برای ReplicaSet از v1.16 به بعد دیگر ارائه نمی‌شوند.

* مانیفست‌ها و کلاینت‌های API را به نسخهٔ API **apps/v1** منتقل کنید که از v1.9 در دسترس است.
* همهٔ آبجکت‌های ذخیره‌شدهٔ موجود از طریق API جدید در دسترس هستند.
* تغییرات قابل توجه:
  * فیلد `spec.selector` اکنون الزامی است و پس از ایجاد قابل تغییر نیست؛ برای ارتقای بی‌وقفه، از برچسب‌های موجود در قالب به‌عنوان انتخابگر استفاده کنید.

#### منبع PodSecurityPolicy {#psp-v116}

نسخهٔ API **extensions/v1beta1** برای PodSecurityPolicy از v1.16 به بعد دیگر ارائه نمی‌شود.

* مانیفست‌ها و کلاینت API را به نسخهٔ API **policy/v1beta1** منتقل کنید که از v1.10 در دسترس است.
* توجه داشته باشید که نسخهٔ API **policy/v1beta1** برای PodSecurityPolicy در v1.25 حذف خواهد شد.

## اقدامات لازم

### آزمایش با غیرفعال‌کردن APIهای منسوخ‌شده

برای شبیه‌سازی حذف‌های آینده، می‌توانید سرور API را با غیرفعال‌کردن نسخه‌های مشخصی از API راه‌اندازی کنید
و کلاسترهای خود را آزمایش کنید. فلگ زیر را به آرگومان‌های راه‌اندازی سرور API اضافه کنید:

`--runtime-config=<group>/<version>=false`

برای مثال:

`--runtime-config=admissionregistration.k8s.io/v1beta1=false,apiextensions.k8s.io/v1beta1,...`

### یافتن موارد استفاده از APIهای منسوخ‌شده

برای یافتن موارد استفاده از APIهای منسوخ‌شده، از [هشدارهای کلاینت، متریک‌ها و اطلاعات ممیزی موجود در نسخهٔ 1.19 به بعد](/blog/2020/09/03/warnings/#deprecation-warnings)
استفاده کنید.

### مهاجرت به APIهای منسوخ‌نشده

* یکپارچه‌سازی‌ها و کنترل‌کننده‌های سفارشی را به‌روزرسانی کنید تا APIهای منسوخ‌نشده را فراخوانی کنند.
* فایل‌های YAML را طوری تغییر دهید که به APIهای منسوخ‌نشده ارجاع دهند.

  برای تبدیل خودکار یک آبجکت موجود می‌توانید از فرمان `kubectl convert` استفاده کنید:

  `kubectl convert -f <file> --output-version <group>/<version>`.

  برای نمونه، برای تبدیل یک Deployment قدیمی به `apps/v1` می‌توانید این فرمان را اجرا کنید:

  `kubectl convert -f ./my-deployment.yaml --output-version apps/v1`

  ممکن است این تبدیل از مقادیر پیش‌فرضِ نامطلوب استفاده کند. برای آشنایی بیشتر با هر منبع،
  [مرجع API](/docs/reference/kubernetes-api/) کوبرنتیز را ببینید.
  
  {{< note >}}
  ابزار `kubectl convert` به‌طور پیش‌فرض نصب نمی‌شود، هرچند زمانی بخشی از خودِ `kubectl` بود.
  برای جزئیات بیشتر می‌توانید [مسئلهٔ منسوخ‌شدن و حذف](https://github.com/kubernetes/kubectl/issues/725)
  این زیرفرمان داخلی را بخوانید.
  
  برای آشنایی با نحوهٔ راه‌اندازی `kubectl convert` روی رایانهٔ خود، به صفحهٔ مربوط به سیستم‌عامل خود
  مراجعه کنید:
  [Linux](/docs/tasks/tools/install-kubectl-linux/#install-kubectl-convert-plugin)،
  [macOS](/docs/tasks/tools/install-kubectl-macos/#install-kubectl-convert-plugin) یا
  [Windows](/docs/tasks/tools/install-kubectl-windows/#install-kubectl-convert-plugin).
  {{< /note >}}
