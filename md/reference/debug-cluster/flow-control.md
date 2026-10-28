---
title: کنترل جریان
weight: 130
---

<!-- overview -->

قابلیت «اولویت و انصاف API» (API Priority and Fairness) رفتار kube-apiserver کوبرنتیز را در شرایط بار بیش از حد کنترل می‌کند. اطلاعات بیشتر درباره‌ی آن را می‌توانید در مستندات
[اولویت و انصاف API](/docs/concepts/cluster-administration/flow-control/)
بیابید.

<!-- body -->

## عیب‌یابی {#diagnostics}

هر پاسخ HTTP از یک API server که قابلیت اولویت و انصاف در آن فعال است، دو هدر اضافی دارد: `X-Kubernetes-PF-FlowSchema-UID` و `X-Kubernetes-PF-PriorityLevel-UID`، که به ترتیب flow schemaی که با درخواست مطابقت یافته و سطح اولویتی که درخواست به آن اختصاص داده شده است را مشخص می‌کنند. نام آبجکت‌های API در این هدرها درج نمی‌شود (تا در صورتی که کاربر درخواست‌دهنده مجوز مشاهده‌ی آن‌ها را نداشته باشد، جزئیاتی افشا نشود). هنگام عیب‌یابی می‌توانید از دستوری مانند زیر استفاده کنید:

```shell
kubectl get flowschemas -o custom-columns="uid:{metadata.uid},name:{metadata.name}"
kubectl get prioritylevelconfigurations -o custom-columns="uid:{metadata.uid},name:{metadata.name}"
```

تا نگاشتی از UIDها به نام‌ها را برای هر دو FlowSchema و PriorityLevelConfiguration به دست آورید.

## نقاط پایانی اشکال‌زدایی {#debug-endpoints}

وقتی قابلیت `APIPriorityAndFairness` فعال باشد، `kube-apiserver` مسیرهای اضافی زیر را روی پورت‌های HTTP(S) خود ارائه می‌کند.

باید مطمئن شوید که مجوز دسترسی به این نقاط پایانی را دارید. اگر از کاربر admin استفاده می‌کنید، لازم نیست کار خاصی انجام دهید. در صورت نیاز، می‌توان با پیروی از مستندات [RBAC](/docs/reference/access-authn-authz/rbac/) و با مشخص کردن `nonResourceURLs`، مجوز دسترسی به `/debug/api_priority_and_fairness/` را اعطا کرد.

- `/debug/api_priority_and_fairness/dump_priority_levels` - فهرستی از
  همه‌ی سطوح اولویت و وضعیت فعلی هر یک. می‌توانید آن را به این صورت دریافت کنید:

  ```shell
  kubectl get --raw /debug/api_priority_and_fairness/dump_priority_levels
  ```

  خروجی با قالب CSV و مشابه نمونه‌ی زیر خواهد بود:

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

  توضیح برخی از نام ستون‌ها:
  - `IsQuiescing` نشان می‌دهد که آیا این سطح اولویت پس از تخلیه‌ی صف‌هایش حذف خواهد شد یا خیر.

- `/debug/api_priority_and_fairness/dump_queues` - فهرستی از همه‌ی
  صف‌ها و وضعیت فعلی آن‌ها. می‌توانید آن را به این صورت دریافت کنید:

  ```shell
  kubectl get --raw /debug/api_priority_and_fairness/dump_queues
  ```

  خروجی با قالب CSV و مشابه نمونه‌ی زیر خواهد بود:

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

  توضیح برخی از نام ستون‌ها:
  - `NextDispatchR`: مقدار نشانگر پیشرفت R، بر حسب seat-second، که در آن
    درخواست بعدی ارسال (dispatch) خواهد شد.
  - `InitialSeatsSum`: مجموع InitialSeats مرتبط با همه‌ی درخواست‌ها در
    یک صف مشخص.
  - `MaxSeatsSum`: مجموع MaxSeats مرتبط با همه‌ی درخواست‌ها در یک
    صف مشخص.
  - `TotalWorkSum`: مجموع کل کار، بر حسب seat-second، همه‌ی
    درخواست‌های در انتظار در یک صف مشخص.

  نکته: `seat-second` (با اختصار `ss`) در دنیای APF معیاری برای سنجش کار، بر حسب seat-second، است.

- `/debug/api_priority_and_fairness/dump_requests` - فهرستی از همه‌ی درخواست‌ها
  شامل درخواست‌هایی که در صف منتظرند و درخواست‌هایی که در حال اجرا هستند.
  می‌توانید آن را به این صورت دریافت کنید:

  ```shell
  kubectl get --raw /debug/api_priority_and_fairness/dump_requests
  ```

  خروجی با قالب CSV و مشابه نمونه‌ی زیر خواهد بود:

  ```none
  PriorityLevelName, FlowSchemaName,   QueueIndex, RequestIndexInQueue, FlowDistingsher,                        ArriveTime,                     InitialSeats, FinalSeats, AdditionalLatency, StartTime
  exempt,            exempt,           -1,         -1,                  ,                                       2023-07-15T04:51:25.596404345Z, 1,            0,          0s,                2023-07-15T04:51:25.596404345Z
  workload-low,      service-accounts, 14,         0,                   system:serviceaccount:default:loadtest, 2023-07-18T00:12:51.386556253Z, 10,           0,          0s,                0001-01-01T00:00:00Z
  workload-low,      service-accounts, 14,         1,                   system:serviceaccount:default:loadtest, 2023-07-18T00:12:51.487092539Z, 10,           0,          0s,                0001-01-01T00:00:00Z
  ```

  با دستوری مانند زیر می‌توانید فهرستی با جزئیات بیشتر دریافت کنید:

  ```shell
  kubectl get --raw '/debug/api_priority_and_fairness/dump_requests?includeRequestDetails=1'
  ```

  خروجی با قالب CSV و مشابه نمونه‌ی زیر خواهد بود:

  ```none
  PriorityLevelName, FlowSchemaName,   QueueIndex, RequestIndexInQueue, FlowDistingsher,                        ArriveTime,                     InitialSeats, FinalSeats, AdditionalLatency, StartTime,                      UserName,                               Verb,   APIPath,                                   Namespace,   Name,   APIVersion, Resource,   SubResource
  exempt,            exempt,           -1,         -1,                  ,                                       2023-07-15T04:51:25.596404345Z, 1,            0,          0s,                2023-07-15T04:51:25.596404345Z, system:serviceaccount:system:admin,     list,   /api/v1/namespaces/kube-stress/configmaps, kube-stress, ,       v1,         configmaps,
  workload-low,      service-accounts, 14,         0,                   system:serviceaccount:default:loadtest, 2023-07-18T00:13:08.986534842Z, 10,           0,          0s,                0001-01-01T00:00:00Z,           system:serviceaccount:default:loadtest, list,   /api/v1/namespaces/kube-stress/configmaps, kube-stress, ,       v1,         configmaps,
  workload-low,      service-accounts, 14,         1,                   system:serviceaccount:default:loadtest, 2023-07-18T00:13:09.086476021Z, 10,           0,          0s,                0001-01-01T00:00:00Z,           system:serviceaccount:default:loadtest, list,   /api/v1/namespaces/kube-stress/configmaps, kube-stress, ,       v1,         configmaps,
  ```

  توضیح برخی از نام ستون‌ها:
  - `QueueIndex`: اندیس صف. برای سطوح اولویتی که صف ندارند، مقدار آن 1- خواهد بود.
  - `RequestIndexInQueue`: اندیس یک درخواست مشخص در صف. برای درخواست‌های
    در حال اجرا، مقدار آن 1- خواهد بود.
  - `InitialSeats`: تعداد seatهایی که در مرحله‌ی اولیه
    (عادی) اجرای درخواست اشغال می‌شوند.
  - `FinalSeats`: تعداد seatهایی که در مرحله‌ی نهایی
    اجرای درخواست اشغال می‌شوند، با احتساب اعلان‌های WATCH مرتبط.
  - `AdditionalLatency`: زمان اضافی صرف‌شده در مرحله‌ی نهایی اجرای درخواست.
    در این بازه‌ی زمانی، FinalSeats اشغال خواهد بود. این مقدار به معنای تأخیری
    نیست که کاربر مشاهده می‌کند.
  - `StartTime`: زمانی که اجرای یک درخواست آغاز می‌شود. برای درخواست‌های
    در صف، مقدار آن 0001-01-01T00:00:00Z خواهد بود.

## ثبت لاگ اشکال‌زدایی {#debug-logging}

در سطح جزئیات `-v=3` یا بالاتر، API server برای هر درخواست یک خط httplog در لاگ API server ثبت می‌کند که شامل ویژگی‌های زیر است.

- `apf_fs`: نام flow schemaی که درخواست در آن طبقه‌بندی شده است.
- `apf_pl`: نام سطح اولویت مربوط به آن flow schema.
- `apf_iseats`: تعداد seatهای تعیین‌شده برای مرحله‌ی اولیه
  (عادی) اجرای درخواست.
- `apf_fseats`: تعداد seatهای تعیین‌شده برای مرحله‌ی نهایی
  اجرای درخواست (با احتساب اعلان‌های `watch` مرتبط).
- `apf_additionalLatency`: مدت زمان مرحله‌ی نهایی
  اجرای درخواست.

در سطوح بالاتر جزئیات، خطوط لاگی وجود خواهد داشت که جزئیات نحوه‌ی رسیدگی APF به درخواست را نمایش می‌دهند و عمدتاً برای اشکال‌زدایی هستند.

## هدرهای پاسخ {#response-headers}

APF دو هدر زیر را به هر پیام پاسخ HTTP اضافه می‌کند. این هدرها در لاگ ممیزی (audit log) ظاهر نمی‌شوند. می‌توان آن‌ها را از سمت کلاینت مشاهده کرد. برای کلاینت‌هایی که از `klog` استفاده می‌کنند، برای مشاهده‌ی این هدرها از سطح جزئیات `-v=8` یا بالاتر استفاده کنید.

- `X-Kubernetes-PF-FlowSchema-UID` شامل UID آبجکت FlowSchema است
  که درخواست مربوطه در آن طبقه‌بندی شده است.
- `X-Kubernetes-PF-PriorityLevel-UID` شامل UID آبجکت
  PriorityLevelConfiguration مرتبط با آن FlowSchema است.

## {{% heading "whatsnext" %}}

برای کسب اطلاعات پایه درباره‌ی جزئیات طراحی اولویت و انصاف API، به
[پیشنهاد بهبود (enhancement proposal)](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/1040-priority-and-fairness) مراجعه کنید.
