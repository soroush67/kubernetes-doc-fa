---
title: "زمان‌بندی، پس‌گیری و بیرون‌رانی"
weight: 95
content_type: concept
no_list: true
---

در کوبرنتیز، زمان‌بندی (scheduling) به معنای اطمینان از این است که {{<glossary_tooltip text="Podها" term_id="pod">}}
با {{<glossary_tooltip text="نودها" term_id="node">}} تطبیق داده شوند تا
{{<glossary_tooltip text="kubelet" term_id="kubelet">}} بتواند آن‌ها را اجرا کند. پس‌گیری (preemption)
فرایند خاتمه دادن به Podهایی با {{<glossary_tooltip text="اولویت" term_id="pod-priority">}} پایین‌تر است
تا Podهایی با اولویت بالاتر بتوانند روی نودها زمان‌بندی شوند. بیرون‌رانی (eviction) فرایند
خاتمه دادن به یک یا چند Pod روی نودها است.

## زمان‌بندی

* [زمان‌بند کوبرنتیز](/docs/concepts/scheduling-eviction/kube-scheduler/)
* [اجرای چند زمان‌بند](/docs/concepts/scheduling-eviction/running-multiple-schedulers/)
* [اختصاص Podها به نودها](/docs/concepts/scheduling-eviction/assign-pod-node/)
* [سربار Pod](/docs/concepts/scheduling-eviction/pod-overhead/)
* [قیدهای پخش توپولوژی Pod](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
* [Taintها و Tolerationها](/docs/concepts/scheduling-eviction/taint-and-toleration/)
* [چارچوب زمان‌بندی](/docs/concepts/scheduling-eviction/scheduling-framework)
* [تنظیم کارایی زمان‌بند](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
* [بسته‌بندی منابع (Bin Packing) برای منابع توسعه‌یافته](/docs/concepts/scheduling-eviction/resource-bin-packing/)
* [آمادگی زمان‌بندی Pod](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
* [زمان‌بندی PodGroup](/docs/concepts/scheduling-eviction/podgroup-scheduling/)
* [زمان‌بندی گروهی (Gang Scheduling)](/docs/concepts/scheduling-eviction/gang-scheduling/)
* [زمان‌بندی آگاه از توپولوژی](/docs/concepts/scheduling-eviction/topology-aware-scheduling/)
* [پس‌گیری آگاه از بار کاری](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
* [Descheduler](https://github.com/kubernetes-sigs/descheduler#descheduler-for-kubernetes)
* [قابلیت‌های اعلام‌شده توسط نود](/docs/concepts/scheduling-eviction/node-declared-features/)

## اختلال Pod

{{<glossary_definition term_id="pod-disruption" length="all">}}

* [اولویت و پس‌گیری Pod](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
* [بیرون‌رانی ناشی از فشار نود](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
* [بیرون‌رانی آغازشده از طریق API](/docs/concepts/scheduling-eviction/api-eviction/)
