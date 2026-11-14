---
title: دسترسی به فراداده دستگاه‌های DRA
content_type: task
min-kubernetes-server-version: v1.37
weight: 30
---

{{< feature-state state="beta" for_k8s_version="v1.37" >}}

<!-- overview -->

این صفحه نشان می‌دهد که چگونه می‌توانید از درون کانتینرهایی که از _تخصیص پویای منابع (Dynamic Resource Allocation یا DRA)_ استفاده می‌کنند، به
[فراداده دستگاه (device metadata)](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-metadata)
دسترسی پیدا کنید. بارهای کاری با کمک فراداده دستگاه می‌توانند اطلاعات دستگاه‌های تخصیص‌یافته، مانند ویژگی‌های دستگاه یا جزئیات رابط شبکه، را با خواندن فایل‌های JSON در مسیرهای شناخته‌شده درون کانتینر به دست آورند.

پیش از مطالعه این صفحه، با
[تخصیص پویای منابع (DRA)](/docs/concepts/resource-management/dynamic-resource-allocation/)
و نحوه
[تخصیص دستگاه‌ها به بارهای کاری](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)
آشنا شوید.

<!-- body -->

## {{% heading "prerequisites" %}}

{{< include "task-tutorial-prereqs.md" >}} {{< version-check >}}

* اطمینان حاصل کنید که مدیر کلاستر شما DRA را راه‌اندازی کرده، دستگاه‌ها را متصل کرده و درایورها را نصب کرده است. برای اطلاعات بیشتر،
  [راه‌اندازی DRA در یک کلاستر](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster)
  را ببینید.
* اطمینان حاصل کنید که درایور DRA مستقرشده در کلاستر شما از فراداده دستگاه پشتیبانی می‌کند. نویسندگان درایورهایی که از
  [افزونه kubelet برای DRA](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin)
  استفاده می‌کنند، این پشتیبانی را با
  [`EnableDeviceMetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/kubeletplugin#EnableDeviceMetadata)
  فعال می‌کنند و باید `metadata.resource.k8s.io/v1beta1` را در نسخه‌های انتخاب‌شده بگنجانند.
  هر درایور می‌تواند برای سازگاری با مصرف‌کنندگان قدیمی‌تر، نسخه `v1alpha1` را نیز تولید کند.

## دسترسی به فراداده دستگاه با یک ResourceClaim {#access-metadata-resourceclaim}

وقتی برای تخصیص دستگاه‌ها از یک ResourceClaim که مستقیماً به آن ارجاع داده شده است استفاده می‌کنید، فایل‌های فراداده دستگاه در مسیر زیر درون کانتینر قرار می‌گیرند:

```
/var/run/kubernetes.io/dra-device-attributes/resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json
```

1. مانیفست نمونه زیر را بررسی کنید:

   {{% code_sample file="dra/dra-device-metadata-pod.yaml" %}}

   این مانیفست یک ResourceClaim به نام `gpu-claim` ایجاد می‌کند که یک دستگاه از DeviceClass با نام `gpu.example.com` درخواست می‌کند، و همچنین یک Pod ایجاد می‌کند که فراداده دستگاه را می‌خواند.

1. ResourceClaim و Pod را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/dra/dra-device-metadata-pod.yaml
   ```

1. پس از اجرا شدن Pod، لاگ‌های کانتینر را مشاهده کنید تا فراداده را ببینید:

   ```shell
   kubectl logs gpu-metadata-reader
   ```

   خروجی مشابه زیر است:

   ```
   === DRA device metadata ===
   /var/run/kubernetes.io/dra-device-attributes/resourceclaims/gpu-claim/gpu/gpu.example.com-metadata.json
   {
     "kind": "DeviceMetadata",
     "apiVersion": "metadata.resource.k8s.io/v1beta1",
     ...
   }
   ```

1. برای بررسی کامل فایل فراداده، با exec وارد کانتینر شوید:

   ```shell
   kubectl exec gpu-metadata-reader -- \
     cat /var/run/kubernetes.io/dra-device-attributes/resourceclaims/gpu-claim/gpu/gpu.example.com-metadata.json
   ```

   هر فایل فراداده یک جریان JSON است. این فایل برای هر نسخه API که درایور انتخاب کرده است، یک آبجکت دارد و این آبجکت‌ها به ترتیبی که درایور پیکربندی کرده است قرار می‌گیرند. درایورها باید جدیدترین نسخه را در ابتدا قرار دهند. این آبجکت‌ها فراداده دستگاه معادلی دارند؛ بنابراین ممکن است این دستور بیش از یک آبجکت JSON چاپ کند.

   خروجی شامل ویژگی‌های دستگاه، مانند مدل، نسخه درایور و UUID دستگاه است. ظرفیت‌های دستگاه بخشی از طرح‌واره فراداده نیستند. برای جزئیات ساختار JSON،
   [طرح‌واره فراداده](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-metadata-schema)
   را ببینید.

## دسترسی به فراداده دستگاه با یک ResourceClaimTemplate {#access-metadata-template}

وقتی از یک ResourceClaimTemplate استفاده می‌کنید، کوبرنتیز برای هر Pod یک ResourceClaim تولید می‌کند. از آنجا که نام claim تولیدشده قابل پیش‌بینی نیست، فایل‌های فراداده به‌جای آن در مسیری قرار می‌گیرند که از نام ارجاع claim در Pod استفاده می‌کند:

```
/var/run/kubernetes.io/dra-device-attributes/resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json
```

مقدار `<podClaimName>` با فیلد `name` در مدخل `spec.resourceClaims[]` مربوط به Pod متناظر است. فراداده JSON نیز فیلدی به نام `podClaimName` دارد که این نگاشت را ثبت می‌کند.

1. مانیفست نمونه زیر را بررسی کنید:

   {{% code_sample file="dra/dra-device-metadata-template-pod.yaml" %}}

   این مانیفست یک ResourceClaimTemplate و یک Pod ایجاد می‌کند. برای هر Pod یک ResourceClaim جداگانه تولید می‌شود. مسیر فراداده از نام ارجاع claim در Pod، یعنی `my-gpu`، استفاده می‌کند.

1. ResourceClaimTemplate و Pod را ایجاد کنید:

   ```shell
   kubectl apply -f https://k8s.io/examples/dra/dra-device-metadata-template-pod.yaml
   ```

1. پس از اجرا شدن Pod، فراداده را مشاهده کنید:

   ```shell
   kubectl exec gpu-metadata-template-reader -- \
     cat /var/run/kubernetes.io/dra-device-attributes/resourceclaimtemplates/my-gpu/gpu/gpu.example.com-metadata.json
   ```

## خواندن فراداده در برنامه شما {#read-metadata-application}

### برنامه‌های Go

بسته
[`k8s.io/dynamic-resource-allocation/devicemetadata`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata)
توابع آماده‌ای برای خواندن فایل‌های فراداده فراهم می‌کند. این توابع مذاکره نسخه را به‌طور خودکار انجام می‌دهند؛ یعنی جریان فراداده را رمزگشایی می‌کنند و آن را به انواع داخلی تبدیل می‌کنند تا کد شما بدون بررسی دستی نسخه، با نسخه‌های مختلف طرح‌واره کار کند. این توابع از آبجکت‌هایی با نسخه‌های API ناشناخته صرف‌نظر می‌کنند و نخستین آبجکت سازگار را برمی‌گردانند.

برای یک ResourceClaim که مستقیماً به آن ارجاع داده شده است:

```go
import "k8s.io/dynamic-resource-allocation/devicemetadata"

dm, err := devicemetadata.ReadResourceClaimMetadata("gpu-claim", "gpu")
```

برای یک claim تولیدشده از الگو (با استفاده از نام ارجاع claim در Pod):

```go
dm, err := devicemetadata.ReadResourceClaimTemplateMetadata("my-gpu", "gpu")
```

اگر نام دقیق درایور را می‌دانید، می‌توانید فایل فراداده یک درایور مشخص را بخوانید:

```go
dm, err := devicemetadata.ReadResourceClaimMetadataWithDriverName("gpu.example.com", "gpu-claim", "gpu")
```

توابعی که فراداده همه درایورها را می‌خوانند، یک `*metadata.DeviceMetadata` با درخواست‌های ادغام‌شده و ویژگی‌های جداگانه هر دستگاه برمی‌گردانند. توابعی که نام درایور را می‌پذیرند، آبجکت کامل فراداده را از فایل همان درایور برمی‌گردانند.

توابع کمکی خواندن، فراداده را بدون اعتبارسنجی رمزگشایی می‌کنند. برای فعال کردن اعتبارسنجی، فایل را باز کنید و از
[`DecodeMetadataFromStream`](https://pkg.go.dev/k8s.io/dynamic-resource-allocation/devicemetadata#DecodeMetadataFromStream)
استفاده کنید:

```go
import (
	"encoding/json"
	"os"

	"k8s.io/dynamic-resource-allocation/api/metadata"
	"k8s.io/dynamic-resource-allocation/devicemetadata"
)

func readMetadata(path string) (*metadata.DeviceMetadata, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var deviceMetadata metadata.DeviceMetadata
	var validationErr error
	err = devicemetadata.DecodeMetadataFromStream(
		json.NewDecoder(file),
		&deviceMetadata,
		devicemetadata.DecodeMetadataWithValidationResult(&validationErr),
	)
	if err != nil {
		return nil, err
	}
	if validationErr != nil {
		return nil, validationErr
	}
	return &deviceMetadata, nil
}
```

رمزگشایی و اعتبارسنجی نتایج جداگانه‌ای دارند. خطای اعتبارسنجی مانع از آن نمی‌شود که رمزگشا مقدار `deviceMetadata` را پر کند. اعتبارسنجی زمانی مفید است که فراداده از یک درایور سفارشی می‌آید، زیرا افزونه kubelet برای DRA آبجکت‌ها را پیش از نوشتن اعتبارسنجی نمی‌کند.

برنامه‌هایی که به زبان‌های دیگر نوشته شده‌اند، می‌توانند جریان JSON را آبجکت به آبجکت رمزگشایی کنند، مقدار `apiVersion` هر آبجکت را بررسی کنند، از نسخه‌های ناشناخته صرف‌نظر کنند و نخستین نسخه‌ای را که پشتیبانی می‌کنند به کار ببرند.

## پاک‌سازی {#clean-up}

منابعی را که ایجاد کرده‌اید حذف کنید:

```shell
kubectl delete -f https://k8s.io/examples/dra/dra-device-metadata-pod.yaml
kubectl delete -f https://k8s.io/examples/dra/dra-device-metadata-template-pod.yaml
```

## {{% heading "whatsnext" %}}

* [درباره فراداده دستگاه‌های DRA بیشتر بیاموزید](/docs/concepts/resource-management/dynamic-resource-allocation/dra-observability/#device-metadata)
* [تخصیص دستگاه‌ها به بارهای کاری با DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)
* برای اطلاعات بیشتر درباره طراحی،
  [KEP-5304](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/5304-dra-attributes-downward-api)
  را ببینید.
