---
title: افشاری آغازشده توسط API
id: api-eviction
full_link: /docs/concepts/scheduling-eviction/api-eviction/
short_description: >
  افشاری آغازشده توسط API فرایندی است که در آن با استفاده از Eviction API یک آبجکت Eviction ایجاد می‌کنید تا خاتمهٔ مهربانانهٔ (graceful) یک Pod را راه‌اندازی کند.
aka:
tags:
- operation
---
افشاری آغازشده توسط API فرایندی است که در آن با استفاده از [Eviction API](/docs/reference/generated/kubernetes-api/{{<param "version">}}/#create-eviction-pod-v1-core)
یک آبجکت `Eviction` ایجاد می‌کنید تا خاتمهٔ مهربانانهٔ (graceful) یک Pod را راه‌اندازی کند.

<!--more-->

می‌توانید با فراخوانی مستقیم Eviction API و با استفاده از یک کلاینت kube-apiserver، مانند دستور `kubectl drain`، درخواست افشاری (eviction) بدهید.
هنگامی که یک آبجکت `Eviction` ایجاد می‌شود، سرور API آن Pod را خاتمه می‌دهد.

افشاری آغازشده توسط API، مقادیر پیکربندی‌شدهٔ [`PodDisruptionBudgets`](/docs/tasks/run-application/configure-pdb/)
و [`terminationGracePeriodSeconds`](/docs/concepts/workloads/pods/pod-lifecycle#pod-termination) شما را رعایت می‌کند.

افشاری آغازشده توسط API با [افشاری ناشی از فشار منابع نود (node-pressure eviction)](/docs/concepts/scheduling-eviction/node-pressure-eviction/) یکسان نیست.

* برای اطلاعات بیشتر، [افشاری آغازشده توسط API](/docs/concepts/scheduling-eviction/api-eviction/) را ببینید.
