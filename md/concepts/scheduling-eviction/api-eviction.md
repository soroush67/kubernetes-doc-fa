---
title: بیرون‌رانی آغازشده از طریق API
content_type: concept
weight: 110
---

{{< glossary_definition term_id="api-eviction" length="short" >}} </br>

می‌توانید بیرون‌رانی را با فراخوانی مستقیم Eviction API یا به‌صورت برنامه‌نویسی‌شده
با استفاده از یک کلاینت {{<glossary_tooltip term_id="kube-apiserver" text="سرور API">}}، مانند فرمان `kubectl drain`، درخواست کنید. این کار
یک آبجکت `Eviction` ایجاد می‌کند که باعث می‌شود سرور API به Pod خاتمه دهد.

بیرون‌رانی‌های آغازشده از طریق API، [`PodDisruptionBudgets`](/docs/tasks/run-application/configure-pdb/)
و [`terminationGracePeriodSeconds`](/docs/concepts/workloads/pods/pod-lifecycle#pod-termination) پیکربندی‌شدهٔ شما را رعایت می‌کنند.

استفاده از API برای ایجاد یک آبجکت Eviction برای یک Pod، مانند انجام یک
[عملیات `DELETE`](/docs/reference/kubernetes-api/workload-resources/pod-v1/#delete-delete-a-pod) کنترل‌شده با سیاست
روی آن Pod است.

## فراخوانی Eviction API

می‌توانید از یک [کلاینت زبان برنامه‌نویسی کوبرنتیز](/docs/tasks/administer-cluster/access-cluster-api/#programmatic-access-to-the-api)
برای دسترسی به API کوبرنتیز و ایجاد یک آبجکت `Eviction` استفاده کنید. برای این کار،
عملیات موردنظر را با POST ارسال می‌کنید، مشابه مثال زیر:

{{< tabs name="Eviction_example" >}}
{{% tab name="policy/v1" %}}
{{< note >}}
Eviction نسخهٔ `policy/v1` در v1.22 و نسخه‌های بالاتر در دسترس است. در نسخه‌های پیشین از `policy/v1beta1` استفاده کنید.
{{< /note >}}

```json
{
  "apiVersion": "policy/v1",
  "kind": "Eviction",
  "metadata": {
    "name": "quux",
    "namespace": "default"
  }
}
```
{{% /tab %}}
{{% tab name="policy/v1beta1" %}}
{{< note >}}
در v1.22 به نفع `policy/v1` منسوخ شده است
{{< /note >}}

```json
{
  "apiVersion": "policy/v1beta1",
  "kind": "Eviction",
  "metadata": {
    "name": "quux",
    "namespace": "default"
  }
}
```
{{% /tab %}}
{{< /tabs >}}

به‌عنوان راه دیگر، می‌توانید با دسترسی به API با استفاده از
`curl` یا `wget` اقدام به عملیات بیرون‌رانی کنید، مشابه مثال زیر:

```bash
curl -v -H 'Content-type: application/json' https://your-cluster-api-endpoint.example/api/v1/namespaces/default/pods/quux/eviction -d @eviction.json
```

## نحوهٔ کار بیرون‌رانی آغازشده از طریق API

هنگامی که با استفاده از API درخواست بیرون‌رانی می‌کنید، سرور API بررسی‌های پذیرش (admission)
را انجام می‌دهد و به یکی از روش‌های زیر پاسخ می‌دهد:

* `200 OK`: بیرون‌رانی مجاز است، زیرمنبع `Eviction` ایجاد می‌شود و
  Pod حذف می‌شود؛ مشابه ارسال یک درخواست `DELETE` به URL مربوط به Pod.
* `429 Too Many Requests`: بیرون‌رانی در حال حاضر به دلیل
  {{<glossary_tooltip term_id="pod-disruption-budget" text="PodDisruptionBudget">}} پیکربندی‌شده مجاز نیست.
  ممکن است بتوانید بعداً دوباره اقدام به بیرون‌رانی کنید. همچنین ممکن است این
  پاسخ را به دلیل محدودسازی نرخ (rate limiting) API ببینید.
* `500 Internal Server Error`: بیرون‌رانی مجاز نیست، زیرا یک
  پیکربندی نادرست وجود دارد؛ برای مثال، اگر چند PodDisruptionBudget به یک Pod ارجاع دهند.

اگر Podی که می‌خواهید بیرون برانید بخشی از بار کاری‌ای نباشد که
PodDisruptionBudget دارد، سرور API همیشه `200 OK` برمی‌گرداند و
بیرون‌رانی را مجاز می‌داند.

اگر سرور API بیرون‌رانی را مجاز بداند، Pod به شرح زیر حذف می‌شود:

1. منبع `Pod` در سرور API با یک مهر زمانی حذف (deletion timestamp) به‌روزرسانی می‌شود،
   و پس از آن سرور API منبع `Pod` را خاتمه‌یافته در نظر می‌گیرد. منبع
   `Pod` همچنین با مهلت مقرر (grace period) پیکربندی‌شده علامت‌گذاری می‌شود.
1. {{<glossary_tooltip term_id="kubelet" text="kubelet">}} روی نودی که Pod محلی در آن در حال اجراست، متوجه می‌شود که منبع `Pod`
   برای خاتمه علامت‌گذاری شده است و شروع به خاموش کردن مؤدبانه (graceful) Pod
   محلی می‌کند.
1. در حالی که kubelet در حال خاموش کردن Pod است، control plane آن Pod را
   از آبجکت‌های {{<glossary_tooltip term_id="endpoint-slice" text="EndpointSlice">}}
   حذف می‌کند. در نتیجه، کنترل‌کننده‌ها دیگر آن Pod را یک آبجکت معتبر در نظر نمی‌گیرند.
1. پس از پایان مهلت مقرر Pod، kubelet به‌اجبار
   Pod محلی را خاتمه می‌دهد.
1. kubelet به سرور API اعلام می‌کند که منبع `Pod` را حذف کند.
1. سرور API منبع `Pod` را حذف می‌کند.

## عیب‌یابی بیرون‌رانی‌های گیرکرده

در برخی موارد، ممکن است برنامه‌های شما وارد وضعیتی معیوب شوند که در آن Eviction
API تا زمانی که شما مداخله نکنید، فقط پاسخ‌های `429` یا `500` برمی‌گرداند. این وضعیت
ممکن است برای مثال زمانی رخ دهد که یک ReplicaSet برای برنامهٔ شما Podهایی ایجاد می‌کند، اما Podهای
جدید وارد وضعیت `Ready` نمی‌شوند. همچنین ممکن است این رفتار را در مواردی ببینید
که آخرین Pod بیرون‌رانده‌شده مهلت مقرر خاتمهٔ طولانی‌ای داشته است.

اگر متوجه بیرون‌رانی‌های گیرکرده شدید، یکی از راه‌حل‌های زیر را امتحان کنید:

* عملیات خودکاری را که باعث مشکل شده است، لغو یا متوقف کنید. پیش از راه‌اندازی مجدد عملیات،
  برنامهٔ گیرکرده را بررسی کنید.
* مدتی صبر کنید، سپس به‌جای استفاده از Eviction API، Pod را مستقیماً از طریق control plane
  کلاستر خود حذف کنید.

## {{% heading "whatsnext" %}}

* بیاموزید که چگونه با یک [Pod Disruption Budget](/docs/tasks/run-application/configure-pdb/) از برنامه‌های خود محافظت کنید.
* دربارهٔ [بیرون‌رانی ناشی از فشار نود](/docs/concepts/scheduling-eviction/node-pressure-eviction/) بیاموزید.
* دربارهٔ [اولویت و پس‌گیری Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/) بیاموزید.
