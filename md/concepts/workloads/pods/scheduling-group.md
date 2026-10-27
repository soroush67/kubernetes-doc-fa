---
title: گروه زمان‌بندی
content_type: concept
weight: 90
---

<!-- overview -->
{{< feature-state feature_gate_name="GenericWorkload" >}}

می‌توانید یک `Pod` را به یک [PodGroup](/docs/concepts/workloads/podgroup-api/) پیوند دهید تا نشان دهید
که آن `Pod` به گروهی از `Pods` تعلق دارد که با هم زمان‌بندی می‌شوند. این کار به زمان‌بند
امکان می‌دهد به جای رسیدگی مستقل به هر `Pod`، سیاست‌های سطح گروه مانند زمان‌بندی گروهی (gang scheduling) را اعمال کند.

<!-- body -->

## تعیین یک گروه زمان‌بندی

هنگامی که feature gate
[`GenericWorkload`](/docs/reference/command-line-tools-reference/feature-gates/#GenericWorkload)
فعال باشد،
می‌توانید فیلد `spec.schedulingGroup` را در مانیفست `Pod` خود تنظیم کنید. این فیلد از طریق نام، پیوندی به یک آبجکت `PodGroup` مشخص در همان فضای نام برقرار می‌کند.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-0
  namespace: some-ns
spec:
  schedulingGroup:
    podGroupName: training-worker-0
  containers:
  - name: ml-worker
    image: training:v1
```

فیلد `schedulingGroup` تغییرناپذیر است. پس از تنظیم آن، یک `Pod` را نمی‌توان به
`PodGroup` دیگری منتقل کرد.

## رفتار

هنگامی که `spec.schedulingGroup` را تنظیم می‌کنید، زمان‌بند
[PodGroup](/docs/concepts/workloads/podgroup-api/) ارجاع‌داده‌شده را جست‌وجو می‌کند و
[سیاست زمان‌بندی](/docs/concepts/workloads/workload-api/policies/) تعریف‌شده در آن را اعمال می‌کند:

* اگر `PodGroup` از سیاست `basic` استفاده کند، هر `Pod` به‌طور مستقل و با
  رفتار استاندارد کوبرنتیز زمان‌بندی می‌شود. این گروه‌بندی به‌عنوان یک برچسب سطح گروه استفاده می‌شود.
* اگر `PodGroup` از سیاست `gang` استفاده کند، `Pod` وارد یک چرخه‌ی عمر زمان‌بندی «همه یا هیچ»
  می‌شود. زمان‌بند تلاش می‌کند دست‌کم `minCount` عدد از `Pods` گروه را
  به‌طور همزمان جای‌گذاری کند؛ تا زمانی که این حداقل برآورده نشود، هیچ‌یک از آن‌ها به نودها متصل (bind) نمی‌شوند.

{{< feature-state feature_gate_name="CompositePodGroup" >}}

هنگامی که feature gate
[`CompositePodGroup`](/docs/reference/command-line-tools-reference/feature-gates/#CompositePodGroup)
فعال باشد، یک `PodGroup` می‌تواند یک `CompositePodGroup` والد نیز تعیین کند. در یک
بار کاری سلسله‌مراتبی، زمان‌بندی توسط سیاست‌هایی اداره می‌شود که در سراسر درخت گروه تعریف شده‌اند (مانند زمان‌بندی گروهی
چندسطحی یا محدودیت‌های توپولوژی).

## ارجاع‌های گروه ناموجود

اگر یک `Pod` به `PodGroup`ی ارجاع دهد که هنوز وجود ندارد، `Pod` در وضعیت pending باقی می‌ماند.
به همین ترتیب، اگر `PodGroup` ارجاع‌داده‌شده یک `CompositePodGroup` والد را (از طریق
`spec.parentCompositePodGroupName`) تعیین کند که هنوز ایجاد نشده است، زمان‌بندی آغاز نمی‌شود و
`Pod` تا زمانی که کل سلسله‌مراتب گروه در کلاستر وجود داشته باشد، در وضعیت pending باقی می‌ماند.

زمان‌بند پس از آنکه همه‌ی منابع `PodGroup` و
`CompositePodGroup` موردنیاز وجود داشته باشند، به‌طور خودکار `Pod` را دوباره بررسی می‌کند.

## {{% heading "whatsnext" %}}

* درباره‌ی [PodGroup API](/docs/concepts/workloads/podgroup-api/) و چرخه‌ی عمر آن بیاموزید.
* درباره‌ی [CompositePodGroup API](/docs/concepts/workloads/compositepodgroup-api/) بخوانید.
* درباره‌ی [سیاست‌های زمان‌بندی PodGroup](/docs/concepts/workloads/workload-api/policies/) بخوانید.
* الگوریتم [زمان‌بندی گروهی](/docs/concepts/scheduling-eviction/gang-scheduling/) را درک کنید.
