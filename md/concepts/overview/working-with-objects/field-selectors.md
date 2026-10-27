---
title: انتخابگرهای فیلد
content_type: concept
weight: 70
---

_انتخابگرهای فیلد_ (field selectors) به شما امکان می‌دهند {{< glossary_tooltip text="آبجکت‌های" term_id="object" >}} کوبرنتیز را بر اساس
مقدار یک یا چند فیلد منبع انتخاب کنید. در اینجا چند نمونه از پرس‌وجوهای انتخابگر فیلد آمده است:

* `metadata.name=my-service`
* `metadata.namespace!=default`
* `status.phase=Pending`

این فرمان `kubectl` همه‌ی Podهایی را انتخاب می‌کند که مقدار فیلد [`status.phase`](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase) آن‌ها برابر با `Running` است:

```shell
kubectl get pods --field-selector status.phase=Running
```

{{< note >}}
انتخابگرهای فیلد در اصل *فیلترهای* منابع هستند. به‌طور پیش‌فرض هیچ انتخابگر/فیلتری اعمال نمی‌شود، یعنی همه‌ی منابعِ نوع مشخص‌شده انتخاب می‌شوند. به همین دلیل، پرس‌وجوهای `kubectl get pods` و `kubectl get pods --field-selector ""` در `kubectl` معادل یکدیگر هستند.
{{< /note >}}

## فیلدهای پشتیبانی‌شده

انتخابگرهای فیلد پشتیبانی‌شده بسته به نوع منبع کوبرنتیز متفاوت هستند. همه‌ی انواع منابع از فیلدهای `metadata.name` و `metadata.namespace` پشتیبانی می‌کنند. استفاده از انتخابگرهای فیلد پشتیبانی‌نشده منجر به خطا می‌شود. برای مثال:

```shell
kubectl get ingress --field-selector foo.bar=baz
```
```
Error from server (BadRequest): Unable to find "ingresses" that match label selector "", field selector "foo.bar=baz": "foo.bar" is not a known field selector: only "metadata.name", "metadata.namespace"
```

### فهرست فیلدهای پشتیبانی‌شده

| Kind                      | فیلدها                                                                                                                                                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pod                       | `spec.nodeName`<br>`spec.restartPolicy`<br>`spec.schedulerName`<br>`spec.serviceAccountName`<br>`spec.hostNetwork`<br>`status.phase`<br>`status.podIP`<br>`status.podIPs`<br>`status.nominatedNodeName`                                                                            |
| Event                     | `involvedObject.kind`<br>`involvedObject.namespace`<br>`involvedObject.name`<br>`involvedObject.uid`<br>`involvedObject.apiVersion`<br>`involvedObject.resourceVersion`<br>`involvedObject.fieldPath`<br>`reason`<br>`reportingComponent`<br>`source`<br>`type` |
| Secret                    | `type`                                                                                                                                                                                                                                                          |
| Service                   | `spec.clusterIP`<br>`spec.type`                                                                                                                                                                                                                                 |
| Namespace                 | `status.phase`                                                                                                                                                                                                                                                  |
| ReplicaSet                | `status.replicas`                                                                                                                                                                                                                                               |
| ReplicationController     | `status.replicas`                                                                                                                                                                                                                                               |
| Job                       | `status.successful`                                                                                                                                                                                                                                             |
| Node                      | `spec.unschedulable`                                                                                                                                                                                                                                            |
| CertificateSigningRequest | `spec.signerName`                                                                                                                                                                                                                                               |

### فیلدهای منابع سفارشی

همه‌ی انواع منابع سفارشی از فیلدهای `metadata.name` و `metadata.namespace` پشتیبانی می‌کنند.

علاوه بر این، فیلد `spec.versions[*].selectableFields` در یک {{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}}
اعلام می‌کند که از کدام فیلدهای دیگر یک منبع سفارشی می‌توان در انتخابگرهای فیلد استفاده کرد. برای اطلاعات بیشتر درباره‌ی نحوه‌ی استفاده از انتخابگرهای فیلد با CustomResourceDefinitionها،
[فیلدهای قابل‌انتخاب برای منابع سفارشی](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#crd-selectable-fields) را ببینید.

## عملگرهای پشتیبانی‌شده

می‌توانید از عملگرهای `=`، `==` و `!=` در انتخابگرهای فیلد استفاده کنید (`=` و `==` به یک معنا هستند). برای مثال، این فرمان `kubectl` همه‌ی Serviceهای کوبرنتیز را که در فضای نام `default` نیستند انتخاب می‌کند:

```shell
kubectl get services  --all-namespaces --field-selector metadata.namespace!=default
```
{{< note >}}
[عملگرهای مبتنی بر مجموعه](/docs/concepts/overview/working-with-objects/labels/#set-based-requirement)
(`in`، `notin`، `exists`) برای انتخابگرهای فیلد پشتیبانی نمی‌شوند.
{{< /note >}}

## انتخابگرهای زنجیره‌ای

همانند انتخابگرهای [برچسب](/docs/concepts/overview/working-with-objects/labels) و سایر انتخابگرها، انتخابگرهای فیلد را می‌توان به‌صورت فهرستی جداشده با ویرگول به هم زنجیر کرد. این فرمان `kubectl` همه‌ی Podهایی را انتخاب می‌کند که `status.phase` آن‌ها برابر با `Running` نیست و فیلد `spec.restartPolicy` آن‌ها برابر با `Always` است:

```shell
kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always
```

## چند نوع منبع

می‌توانید انتخابگرهای فیلد را برای چند نوع منبع به‌طور هم‌زمان به کار ببرید. این فرمان `kubectl` همه‌ی StatefulSetها و Serviceهایی را که در فضای نام `default` نیستند انتخاب می‌کند:

```shell
kubectl get statefulsets,services --all-namespaces --field-selector metadata.namespace!=default
```
