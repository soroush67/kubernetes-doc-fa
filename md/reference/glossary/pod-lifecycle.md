---
title: چرخه حیات Pod
id: pod-lifecycle
full-link: /docs/concepts/workloads/pods/pod-lifecycle/
related:
 - pod
 - container
tags:
 - fundamental
short_description: >
  توالی حالت‌هایی که یک Pod در طول عمر خود از آن‌ها عبور می‌کند.
 
---
 توالی حالت‌هایی که یک Pod در طول عمر خود از آن‌ها عبور می‌کند.

<!--more--> 

[چرخه حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/) بر اساس حالت‌ها یا فازهای یک Pod تعریف می‌شود. پنج فاز ممکن برای Pod وجود دارد: Pending، Running، Succeeded، Failed و Unknown. توصیف کلی وضعیت Pod در فیلد `phase` از [PodStatus](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podstatus-v1-core) خلاصه شده است.
