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
  دنباله‌ای از وضعیت‌ها که یک Pod در طول عمر خود از آن‌ها عبور می‌کند.
 
---
 دنباله‌ای از وضعیت‌ها که یک Pod در طول عمر خود از آن‌ها عبور می‌کند.

<!--more--> 

[چرخه حیات Pod](/docs/concepts/workloads/pods/pod-lifecycle/) با وضعیت‌ها یا فازهای یک Pod تعریف می‌شود. هر Pod می‌تواند در یکی از پنج فاز Pending، Running، Succeeded، Failed و Unknown باشد. توصیفی سطح بالا از وضعیت Pod در فیلد `phase` از [PodStatus](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podstatus-v1-core) خلاصه می‌شود.
