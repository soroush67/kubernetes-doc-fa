---
title: تخلیه‌ی آغازشده از طریق API
id: api-eviction
full_link: /docs/concepts/scheduling-eviction/api-eviction/
short_description: >
  تخلیه‌ی آغازشده از طریق API فرایندی است که در آن با استفاده از Eviction API یک آبجکت
  Eviction ایجاد می‌کنید تا خاتمه‌ی تدریجی و منظم پاد آغاز شود.
aka:
tags:
- operation
---
تخلیه‌ی آغازشده از طریق API فرایندی است که در آن با استفاده از [Eviction API](/docs/reference/generated/kubernetes-api/{{<param "version">}}/#create-eviction-pod-v1-core)
یک آبجکت `Eviction` ایجاد می‌کنید تا خاتمه‌ی تدریجی و منظم پاد آغاز شود.

<!--more-->

می‌توانید با فراخوانی مستقیم Eviction API از طریق یک کلاینت kube-apiserver، مانند فرمان `kubectl drain`، درخواست تخلیه بدهید.
پس از ایجاد یک آبجکت `Eviction`، سرور API پاد را خاتمه می‌دهد.

تخلیه‌های آغازشده از طریق API به [`PodDisruptionBudgets`](/docs/tasks/run-application/configure-pdb/)
و [`terminationGracePeriodSeconds`](/docs/concepts/workloads/pods/pod-lifecycle#pod-termination) پیکربندی‌شده‌ی شما پایبند هستند.

تخلیه‌ی آغازشده از طریق API با [تخلیه‌ی ناشی از فشار منابع نود](/docs/concepts/scheduling-eviction/node-pressure-eviction/) یکسان نیست.

* برای اطلاعات بیشتر، [تخلیه‌ی آغازشده از طریق API](/docs/concepts/scheduling-eviction/api-eviction/) را ببینید.
