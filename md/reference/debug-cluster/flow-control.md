---
title: کنترل جریان
weight: 130
---

<!-- overview -->

قابلیت «اولویت و انصاف API» (API Priority and Fairness) رفتار سرور API کوبرنتیز را در شرایط اضافه‌بار کنترل می‌کند. اطلاعات بیشتر درباره‌ی این قابلیت را می‌توانید در مستندات
[اولویت و انصاف API](/docs/concepts/cluster-administration/flow-control/)
بیابید.

<!-- body -->

## عیب‌یابی

هر پاسخ HTTP از سرور API‌ای که قابلیت اولویت و انصاف در آن فعال است، دو سرآیند (header) اضافه دارد: `X-Kubernetes-PF-FlowSchema-UID` و
`X-Kubernetes-PF-PriorityLevel-UID`. این دو سرآیند به ترتیب طرح‌واره‌ی جریان (flow schema) منطبق با درخواست و سطح اولویتی را که درخواست به آن تخصیص یافته است، مشخص می‌کنند. نام آبجکت‌های API در این سرآیندها درج نمی‌شود تا اگر کاربر درخواست‌دهنده اجازه‌ی مشاهده‌ی آن‌ها را نداشته باشد، جزئیاتی فاش نشود. هنگام عیب‌یابی می‌توانید از دستوری مانند زیر استفاده کنید:

```shell
kubectl get flowschemas -o custom-columns="uid:{metadata.uid},name:{metadata.name}"
kubectl get prioritylevelconfigurations -o custom-columns="uid:{metadata.uid},name:{metadata.name}"
```

تا نگاشتی از UIDها به نام‌ها را هم برای FlowSchemaها و هم برای
PriorityLevelConfigurationها به دست آورید.

## نقاط پایانی عیب‌یابی

وقتی قابلیت `APIPriorityAndFairness` فعال باشد، `kube-apiserver` مسیرهای اضافه‌ی زیر را روی درگاه‌های HTTP(S) خود ارائه می‌کند.

باید مطمئن شوید که مجوز دسترسی به این نقاط پایانی (endpoint) را دارید. اگر از حساب مدیر (admin) استفاده می‌کنید، لازم نیست کاری انجام دهید. در صورت نیاز می‌توان طبق مستندات [RBAC](/docs/reference/access-authn-authz/rbac/) و با مشخص کردن `nonResourceURLs`، مجوز دسترسی به `/debug/api_priority_and_fairness/` را اعطا کرد.

- مسیر `/debug/api_priority_and_fairness/dump_priority_levels`: فهرستی از همه‌ی سطوح اولویت و وضعیت فعلی هر یک. می‌توانید آن را به این صورت دریافت کنید:

  ```shell
  kubectl get --raw /debug/api_priority_and_fairness/dump_priority_levels
  ```

  خروجی در قالب CSV و مشابه زیر خواهد بود:

  ```none
  PriorityLevelName, ActiveQueues, IsIdle, IsQuiescing, WaitingRequests, ExecutingRequests, DispatchedRequests, RejectedRequests, TimedoutRequests, CancelledRequests
  catch-all,         0,            true,   false,       0,               0,                 1,                  0,                0,                0
  exempt,            0,            true,   false,       0,               0,                 0,                  0,                0,                0
  global-default,    0,            true,   false,       0,               0,                 46,                 0,                0,                0
  leader-election,   0,            true,   false,       0,               0,                 4,                  0,                0,                0
  node-high,         0,            true,   false,       0,               0,                 34,                 0,                0,                0
  system,            0,            true,   false,       0,               0,                 48,                 0,                0,                0
  workload-high,     0,            true,   false,       0,               0,                 500,                0,                0,                0
  workload-low,      0,            true,   false,       0,               0,                 0,                  0,                0,                0
  ```

  توضیح برخی از ستون‌ها:
  - ستون `IsQuiescing` نشان می‌دهد که آیا این سطح اولویت پس از خالی شدن صف‌هایش حذف خواهد شد یا نه.

- مسیر `/debug/api_priority_and_fairness/dump_queues`: فهرستی از همه‌ی صف‌ها و وضعیت فعلی آن‌ها. می‌توانید آن را به این صورت دریافت کنید:

  ```shell
  kubectl get --raw /debug/api_priority_and_fairness/dump_queues
  ```

  خروجی در قالب CSV و مشابه زیر خواهد بود:

  ```none
  PriorityLevelName, Index,  PendingRequests, ExecutingRequests, SeatsInUse, NextDispatchR,   InitialSeatsSum, MaxSeatsSum, TotalWorkSum
  workload-low,      14,     27,              0,                 0,          77.64342019ss,   270,             270,         0.81000000ss
  workload-low,      74,     26,              0,                 0,          76.95387841ss,   260,             260,         0.78000000ss
  ...
  leader-election,   0,      0,               0,                 0,          5088.87053833ss, 0,               0,           0.00000000ss
  leader-election,   1,      0,               0,                 0,          0.00000000ss,    0,               0,           0.00000000ss
  ...
  workload-high,     0,      0,               0,                 0,          0.00000000ss,    0,               0,           0.00000000ss
  workload-high,     1,      0,               0,                 0,          1119.44936475ss, 0,               0,           0.00000000ss
  ```

  توضیح برخی از ستون‌ها:
  - ستون `NextDispatchR`: مقدار نمایش‌داده‌شده در شمارنده‌ی پیشرفت R، بر حسب واحد صندلی-ثانیه، که درخواست بعدی در آن مقدار ارسال خواهد شد.
  - ستون `InitialSeatsSum`: مجموع InitialSeats مربوط به همه‌ی درخواست‌های موجود در یک صف مشخص.
  - ستون `MaxSeatsSum`: مجموع MaxSeats مربوط به همه‌ی درخواست‌های موجود در یک صف مشخص.
  - ستون `TotalWorkSum`: مجموع کل کار همه‌ی درخواست‌های در انتظار در یک صف مشخص، بر حسب واحد صندلی-ثانیه.

  نکته: در دنیای APF، واحد `seat-second` (به اختصار `ss`) معیاری برای سنجش میزان کار بر حسب صندلی-ثانیه است.

- مسیر `/debug/api_priority_and_fairness/dump_requests`: فهرستی از همه‌ی درخواست‌ها، شامل درخواست‌هایی که در صف منتظرند و درخواست‌هایی که در حال اجرا هستند. می‌توانید آن را به این صورت دریافت کنید:

  ```shell
  kubectl get --raw /debug/api_priority_and_fairness/dump_requests
  ```

  خروجی در قالب CSV و مشابه زیر خواهد بود:

  ```none
  PriorityLevelName, FlowSchemaName,   QueueIndex, RequestIndexInQueue, FlowDistingsher,                        ArriveTime,                     InitialSeats, FinalSeats, AdditionalLatency, StartTime
  exempt,            exempt,           -1,         -1,                  ,                                       2023-07-15T04:51:25.596404345Z, 1,            0,          0s,                2023-07-15T04:51:25.596404345Z
  workload-low,      service-accounts, 14,         0,                   system:serviceaccount:default:loadtest, 2023-07-18T00:12:51.386556253Z, 10,           0,          0s,                0001-01-01T00:00:00Z
  workload-low,      service-accounts, 14,         1,                   system:serviceaccount:default:loadtest, 2023-07-18T00:12:51.487092539Z, 10,           0,          0s,                0001-01-01T00:00:00Z
  ```

  با دستوری مانند زیر می‌توانید فهرست مفصل‌تری به دست آورید:

  ```shell
  kubectl get --raw '/debug/api_priority_and_fairness/dump_requests?includeRequestDetails=1'
  ```

  خروجی در قالب CSV و مشابه زیر خواهد بود:

  ```none
  PriorityLevelName, FlowSchemaName,   QueueIndex, RequestIndexInQueue, FlowDistingsher,                        ArriveTime,                     InitialSeats, FinalSeats, AdditionalLatency, StartTime,                      UserName,                               Verb,   APIPath,                                   Namespace,   Name,   APIVersion, Resource,   SubResource
  exempt,            exempt,           -1,         -1,                  ,                                       2023-07-15T04:51:25.596404345Z, 1,            0,          0s,                2023-07-15T04:51:25.596404345Z, system:serviceaccount:system:admin,     list,   /api/v1/namespaces/kube-stress/configmaps, kube-stress, ,       v1,         configmaps,
  workload-low,      service-accounts, 14,         0,                   system:serviceaccount:default:loadtest, 2023-07-18T00:13:08.986534842Z, 10,           0,          0s,                0001-01-01T00:00:00Z,           system:serviceaccount:default:loadtest, list,   /api/v1/namespaces/kube-stress/configmaps, kube-stress, ,       v1,         configmaps,
  workload-low,      service-accounts, 14,         1,                   system:serviceaccount:default:loadtest, 2023-07-18T00:13:09.086476021Z, 10,           0,          0s,                0001-01-01T00:00:00Z,           system:serviceaccount:default:loadtest, list,   /api/v1/namespaces/kube-stress/configmaps, kube-stress, ,       v1,         configmaps,
  ```

  توضیح برخی از ستون‌ها:
  - ستون `QueueIndex`: شماره‌ی صف. برای سطوح اولویتی که صف ندارند، مقدار آن ‎-1 خواهد بود.
  - ستون `RequestIndexInQueue`: شماره‌ی یک درخواست مشخص در صف. برای درخواست‌های در حال اجرا، مقدار آن ‎-1 خواهد بود.
  - ستون `InitialSeats`: تعداد صندلی‌هایی که در مرحله‌ی اولیه (عادی) اجرای درخواست اشغال می‌شوند.
  - ستون `FinalSeats`: تعداد صندلی‌هایی که در مرحله‌ی پایانی اجرای درخواست، با احتساب اعلان‌های WATCH مرتبط، اشغال می‌شوند.
  - ستون `AdditionalLatency`: زمان اضافه‌ای که در مرحله‌ی پایانی اجرای درخواست صرف می‌شود. در این بازه‌ی زمانی، صندلی‌های FinalSeats اشغال خواهند بود. این مقدار به معنای تأخیری نیست که کاربر مشاهده کند.
  - ستون `StartTime`: زمانی که اجرای درخواست آغاز می‌شود. برای درخواست‌های داخل صف، مقدار آن 0001-01-01T00:00:00Z خواهد بود.

## ثبت لاگ برای عیب‌یابی

در سطح جزئیات (verbosity) ‏`-v=3` یا بالاتر، سرور API برای هر درخواست یک خط httplog در لاگ سرور API ثبت می‌کند که شامل ویژگی‌های زیر است.

- ویژگی `apf_fs`: نام طرح‌واره‌ی جریانی که درخواست در آن دسته‌بندی شده است.
- ویژگی `apf_pl`: نام سطح اولویت مربوط به آن طرح‌واره‌ی جریان.
- ویژگی `apf_iseats`: تعداد صندلی‌هایی که برای مرحله‌ی اولیه (عادی) اجرای درخواست تعیین شده است.
- ویژگی `apf_fseats`: تعداد صندلی‌هایی که برای مرحله‌ی پایانی اجرای درخواست (با احتساب اعلان‌های `watch` مرتبط) تعیین شده است.
- ویژگی `apf_additionalLatency`: مدت زمان مرحله‌ی پایانی اجرای درخواست.

در سطوح بالاتر جزئیات، خطوطی در لاگ ثبت می‌شوند که جزئیات نحوه‌ی رسیدگی APF به درخواست را نشان می‌دهند و عمدتاً برای عیب‌یابی کاربرد دارند.

## سرآیندهای پاسخ

APF دو سرآیند زیر را به هر پیام پاسخ HTTP اضافه می‌کند. این سرآیندها در لاگ ممیزی (audit log) نمایش داده نمی‌شوند، اما می‌توان آن‌ها را از سمت کلاینت مشاهده کرد. در کلاینت‌هایی که از `klog` استفاده می‌کنند، برای مشاهده‌ی این سرآیندها از سطح جزئیات `-v=8` یا بالاتر استفاده کنید.

- سرآیند `X-Kubernetes-PF-FlowSchema-UID` شامل UID آبجکت FlowSchema‌ای است که درخواست مربوطه در آن دسته‌بندی شده است.
- سرآیند `X-Kubernetes-PF-PriorityLevel-UID` شامل UID آبجکت PriorityLevelConfiguration مرتبط با آن FlowSchema است.

## {{% heading "whatsnext" %}}

برای آشنایی با پیش‌زمینه و جزئیات طراحی قابلیت اولویت و انصاف API، به
[پیشنهاد بهبود](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/1040-priority-and-fairness) مراجعه کنید.
