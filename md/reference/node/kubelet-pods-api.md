---
content_type: "reference"
title: رابط Pods API در Kubelet
weight: 20
---

{{< feature-state feature_gate_name="PodsAPI" >}}

رابط Pods API در Kubelet به مؤلفه‌های محلی نود امکان می‌دهد اطلاعات {{< glossary_tooltip text="Pods" term_id="pod" >}} در حال اجرا روی {{< glossary_tooltip term_id="Node" >}} را مستقیماً از `kubelet` دریافت کنند. این روش با حذف وابستگی به سرور API کوبرنتیز برای دریافت اطلاعات محلی نود، قابلیت اطمینان را افزایش می‌دهد و بار {{< glossary_tooltip text="control plane" term_id="control-plane" >}} را نیز کاهش می‌دهد.

دسترسی به این API از طریق مجوزهای فایل روی سوکت UNIX به کاربران مدیر محلی (معمولاً `root`) محدود شده است.

## نقطه پایانی {#endpoint}

این API روی سوکت UNIX در مسیر `/var/lib/kubelet/pods-api/pods-api.sock` گوش می‌دهد.

{{< note >}}
این API روی نودهای Windows پشتیبانی نمی‌شود.
{{< /note >}}

## عملیات {#operations}

این API متدهای gRPC زیر را ارائه می‌کند:

### `ListPods` {#list-pods}

فهرست همه Podهایی را برمی‌گرداند که kubelet در حال حاضر روی نود مدیریت می‌کند.

### `WatchPods` {#watch-pods}

جریانی از به‌روزرسانی‌های Pod را برمی‌گرداند. هر بار که وضعیت یک Pod به‌صورت محلی تغییر کند، kubelet اطلاعات به‌روزشده آن Pod را از طریق این جریان ارسال می‌کند.

### `GetPod` {#get-pod}

اطلاعات Pod مشخصی را که با UID آن شناسایی می‌شود برمی‌گرداند.

## تعریف API {#api-definition}

این API از تعریف protobuf زیر استفاده می‌کند:

```protobuf
import "google/protobuf/field_mask.proto";
import "k8s.io/api/core/v1/generated.proto";

service Pods {
    // ListPods returns a list of v1.Pod, optionally filtered by field mask.
    rpc ListPods(PodListRequest) returns (PodListResponse) {}
    // WatchPods returns a stream of Pod updates, optionally filtered by field mask.
    rpc WatchPods(PodWatchRequest) returns (stream PodWatchResponse) {}
    // GetPod returns a v1.Pod for a given pod's UID, optionally filtered by field mask.
    rpc GetPod(PodGetRequest) returns (PodGetResponse) {}
}

message PodListRequest {
    // Optional field mask in the gRPC metadata, to specify which pod fields to return.
}

message PodListResponse {
    repeated v1.Pod pods = 1;
}

message PodWatchRequest {
    // Optional field mask in the gRPC metadata, to specify which pod fields to return.
}

message PodWatchResponse {
    v1.Pod pod = 1;
}

message PodGetRequest {
    string podUID = 1;
    // Optional field mask in the gRPC metadata, to specify which pod fields to return.
}

message PodGetResponse {
    v1.Pod pod = 1;
}
```

## انتخاب فیلدها {#field-selection}

این API از `google.protobuf.FieldMask` پشتیبانی می‌کند تا کلاینت‌ها بتوانند فقط فیلدهای موردنیاز خود (مانند `status.phase` و `status.podIPs`) را درخواست کنند. به این ترتیب، انتقال داده سبک و کارآمد انجام می‌شود. اگر هیچ ماسک فیلدی ارائه نشود، آبجکت کامل `v1.Pod` برگردانده می‌شود.

## قابلیت اطمینان و دسترس‌پذیری {#reliability}

این API به‌روزترین اطلاعاتی را ارائه می‌دهد که kubelet به‌صورت محلی در اختیار دارد؛ این اطلاعات از حافظه نهان داخلی kubelet و تطبیق آن با محیط اجرای کانتینر به دست می‌آید. حتی اگر ارتباط نود با control plane کوبرنتیز قطع شود، این API همچنان در دسترس می‌ماند.

اگر منابع Pod در kubelet هنوز همگام‌سازی اولیه خود را به پایان نرسانده باشند (برای مثال، بلافاصله پس از راه‌اندازی یا راه‌اندازی مجدد kubelet)، هر عملیات به‌جای داده ناقص، خطای gRPC با کد `FAILED_PRECONDITION` برمی‌گرداند. پس از پایان همگام‌سازی، درخواست‌ها به‌طور عادی پاسخ داده می‌شوند.

## محدودسازی نرخ {#rate-limiting}

مؤلفه `kubelet` برای محافظت از خود در برابر بار بیش از حد، نرخ درخواست‌های `ListPods` و `GetPod` را محدود می‌کند. سرور به‌طور پیش‌فرض `100` درخواست در ثانیه را با ظرفیت انفجاری (burst) `10` توکن می‌پذیرد. درخواست‌هایی که از این حد فراتر بروند، خطای gRPC با کد `RESOURCE_EXHAUSTED` دریافت می‌کنند.

جریان‌های `WatchPods` مشمول این محدودیت نرخ نیستند؛ در عوض، اگر مصرف‌کننده‌ای کند باشد و از جریان رویدادهای خود عقب بماند، اتصال watch آن قطع می‌شود (به [متریک‌ها](#metrics) مراجعه کنید).

## متریک‌ها {#metrics}

مؤلفه `kubelet` متریک‌های زیر را برای Pods API با برچسب‌های `server_api_version` و `status_code` ارائه می‌کند:

* متریک `kubelet_pod_requests_total`: تعداد تجمعی درخواست‌ها به این API.
* متریک `kubelet_pod_requests_list_total`: تعداد درخواست‌ها به نقطه پایانی `ListPods`.
* متریک `kubelet_pod_requests_get_total`: تعداد درخواست‌ها به نقطه پایانی `GetPod`.
* متریک `kubelet_pod_requests_watch_total`: تعداد درخواست‌ها به نقطه پایانی `WatchPods`.

مؤلفه `kubelet` همچنین متریک `kubelet_pod_watch_events_dropped_total` را ارائه می‌کند که تعداد رویدادهای watch را می‌شمارد که به دلیل مصرف نشدن سریع جریان رویداد توسط کلاینت، حذف شده‌اند.
